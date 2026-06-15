#!/usr/bin/env python3
"""
Guarded cutover runner for switching the live backend to nurovelle_core.

Default mode is dry-run. A real cutover requires:

  --execute --confirm switch-to-nurovelle-core

The script never prints database URLs or secrets.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import vps_backend_core_preflight as preflight  # noqa: E402


DEFAULT_SSH_TARGET = "d4sd1ng@77.42.74.250"
EXECUTE_CONFIRM = "switch-to-nurovelle-core"
ROLLBACK_CONFIRM = "rollback-nurovelle-core"

OLD_DB = "nurovell_potential_analysis"
NEW_DB = "nurovelle_core"

LIVE_GET_URLS = [
    "https://nurovelle.de/",
    "https://nurovelle.de/homepage/analyse.html",
    "https://nurovelle.de/api/v1/questions?industry=service&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=manufacturing&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=care&tier=basic&include_risk=false",
]


def run_ssh_script(target: str, script: str, timeout: int = 240) -> str:
    script = script.replace("\r\n", "\n").replace("\r", "\n")
    command = [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "ConnectTimeout=12",
        target,
        "bash",
        "-s",
    ]
    completed = subprocess.run(
        command,
        input=script.encode("utf-8"),
        check=False,
        capture_output=True,
        timeout=timeout,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        stdout = completed.stdout.decode("utf-8", errors="replace")
        detail = (stderr or stdout or "").strip()
        raise RuntimeError(detail or f"remote script failed with exit code {completed.returncode}")
    return completed.stdout.decode("utf-8", errors="replace").strip()


def run_live_gets() -> list[str]:
    errors: list[str] = []
    for url in LIVE_GET_URLS:
        request = urllib.request.Request(url, headers={"User-Agent": "nurovelle-core-cutover/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                status = response.getcode()
                if status < 200 or status >= 400:
                    errors.append(f"{url} returned HTTP {status}")
        except urllib.error.HTTPError as error:
            errors.append(f"{url} returned HTTP {error.code}")
        except Exception as error:
            errors.append(f"{url} failed: {error}")
    return errors


def print_preflight(target: str) -> bool:
    checks = preflight.run_checks(target, expected_db=OLD_DB)
    output = {
        "passed": all(check.passed for check in checks),
        "checks": [
            {"name": check.name, "passed": check.passed, "detail": check.detail}
            for check in checks
        ],
    }
    print(json.dumps({"preflight": output}, indent=2, ensure_ascii=False))
    return bool(output["passed"])


def cutover_script() -> str:
    return textwrap.dedent(
        f"""
        set -euo pipefail

        OLD_DB="{OLD_DB}"
        NEW_DB="{NEW_DB}"
        BACKUP_DIR="/opt/nurovell-potential-analysis/backups/postgres"
        COMPOSE_DIR="/opt/nurovell-potential-analysis/compose"
        ENV_FILE="$COMPOSE_DIR/.env.vps"
        TS="$(date -u +%Y%m%d_%H%M%S)"
        FULL_DUMP="$BACKUP_DIR/${{OLD_DB}}_precutover_${{TS}}.dump"
        LEGACY_DATA_DUMP="$BACKUP_DIR/${{OLD_DB}}_legacy_data_${{TS}}.dump"
        ENV_BACKUP="$ENV_FILE.pre_nurovelle_core_${{TS}}"

        mkdir -p "$BACKUP_DIR"

        echo "step=verify_runtime_before"
        docker inspect nurovell_backend --format '{{{{.State.Running}}}}' | grep -qx true
        docker inspect postgres --format '{{{{.State.Running}}}}' | grep -qx true

        current_db="$(DATABASE_URL="$(docker exec nurovell_backend printenv DATABASE_URL)" python3 - <<'PY'
import os
from urllib.parse import urlparse
print(urlparse(os.environ["DATABASE_URL"]).path.lstrip("/"))
PY
)"
        test "$current_db" = "$OLD_DB"

        echo "step=create_precutover_backup"
        docker exec postgres pg_dump -U avataruser --format=custom --dbname="$OLD_DB" > "$FULL_DUMP"
        test -s "$FULL_DUMP"
        docker exec -i postgres pg_restore --list < "$FULL_DUMP" >/dev/null

        echo "step=backup_runtime_env"
        test -f "$ENV_FILE"
        cp "$ENV_FILE" "$ENV_BACKUP"

        echo "step=stop_backend"
        cd "$COMPOSE_DIR"
        docker compose -f docker-compose.vps.yml stop nurovell_backend

        echo "step=copy_legacy_data_to_core"
        docker exec postgres pg_dump -U avataruser --data-only --format=custom --exclude-table=public.alembic_version --dbname="$OLD_DB" > "$LEGACY_DATA_DUMP"
        test -s "$LEGACY_DATA_DUMP"
        docker exec postgres psql -U avataruser -d "$NEW_DB" -v ON_ERROR_STOP=1 -c "
          truncate table
            public.notion_sync_jobs,
            public.newsletter_campaigns,
            public.events,
            public.analysis_reports,
            public.analysis_scores,
            public.analysis_answers,
            public.analysis_sessions,
            public.contacts,
            public.companies,
            public.leads,
            public.admin_users
          restart identity cascade;
        "
        docker exec -i postgres pg_restore -U avataruser --data-only --dbname="$NEW_DB" < "$LEGACY_DATA_DUMP"

        echo "step=switch_database_name"
        OLD_DB="$OLD_DB" NEW_DB="$NEW_DB" ENV_FILE="$ENV_FILE" python3 - <<'PY'
import os
from pathlib import Path

env_file = Path(os.environ["ENV_FILE"])
old_db = os.environ["OLD_DB"]
new_db = os.environ["NEW_DB"]
text = env_file.read_text()
if old_db not in text:
    raise SystemExit(f"old db marker not found in {{env_file}}")
if new_db in text:
    raise SystemExit(f"new db marker already present in {{env_file}}")
env_file.write_text(text.replace(old_db, new_db, 1))
PY

        echo "step=start_backend"
        docker compose -f docker-compose.vps.yml up -d --build nurovell_backend

        echo "step=verify_runtime_after"
        sleep 5
        docker inspect nurovell_backend --format '{{{{.State.Running}}}}' | grep -qx true
        current_db="$(DATABASE_URL="$(docker exec nurovell_backend printenv DATABASE_URL)" python3 - <<'PY'
import os
from urllib.parse import urlparse
print(urlparse(os.environ["DATABASE_URL"]).path.lstrip("/"))
PY
)"
        test "$current_db" = "$NEW_DB"

        printf 'env_backup=%s\\nfull_backup=%s\\nlegacy_data_dump=%s\\n' "$ENV_BACKUP" "$FULL_DUMP" "$LEGACY_DATA_DUMP"
        """
    ).strip()


def rollback_script(env_backup: str) -> str:
    return textwrap.dedent(
        f"""
        set -euo pipefail

        COMPOSE_DIR="/opt/nurovell-potential-analysis/compose"
        ENV_FILE="$COMPOSE_DIR/.env.vps"
        ENV_BACKUP="{env_backup}"

        test -f "$ENV_BACKUP"
        cp "$ENV_BACKUP" "$ENV_FILE"
        cd "$COMPOSE_DIR"
        docker compose -f docker-compose.vps.yml up -d --build nurovell_backend
        sleep 5
        docker inspect nurovell_backend --format '{{{{.State.Running}}}}' | grep -qx true
        echo "rollback=env_restored_and_backend_started"
        """
    ).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Guarded VPS DB cutover runner.")
    parser.add_argument("--ssh-target", default=DEFAULT_SSH_TARGET)
    parser.add_argument("--execute", action="store_true", help="Run the real cutover.")
    parser.add_argument("--confirm", default="", help="Required confirmation word for execute/rollback.")
    parser.add_argument("--rollback-env-backup", default="", help="Remote .env backup path for rollback.")
    args = parser.parse_args()

    if args.rollback_env_backup:
        if args.confirm != ROLLBACK_CONFIRM:
            print(f"rollback refused: pass --confirm {ROLLBACK_CONFIRM!r}", file=sys.stderr)
            return 2
        try:
            output = run_ssh_script(args.ssh_target, rollback_script(args.rollback_env_backup), timeout=180)
            live_errors = run_live_gets()
        except Exception as error:
            print(json.dumps({"rollback": "failed", "error": str(error)}, indent=2))
            return 1
        print(json.dumps({"rollback": "completed", "remote_output": output, "live_get_errors": live_errors}, indent=2))
        return 0 if not live_errors else 1

    preflight_ok = print_preflight(args.ssh_target)
    if not args.execute:
        print("dry_run=true")
        print(f"execute_requires=--execute --confirm {EXECUTE_CONFIRM}")
        return 0 if preflight_ok else 1

    if args.confirm != EXECUTE_CONFIRM:
        print(f"cutover refused: pass --confirm {EXECUTE_CONFIRM!r}", file=sys.stderr)
        return 2
    if not preflight_ok:
        print("cutover refused: preflight failed", file=sys.stderr)
        return 1

    try:
        output = run_ssh_script(args.ssh_target, cutover_script(), timeout=420)
        live_errors = run_live_gets()
    except Exception as error:
        print(json.dumps({"cutover": "failed", "error": str(error)}, indent=2))
        return 1

    result = {"cutover": "completed", "remote_output": output, "live_get_errors": live_errors}
    print(json.dumps(result, indent=2))
    return 0 if not live_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
