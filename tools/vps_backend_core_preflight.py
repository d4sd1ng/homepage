#!/usr/bin/env python3
"""
Read-only preflight for the Nurovelle backend DB cutover.

This script does not write to the VPS. It verifies that the current runtime
state is compatible with a later switch from nurovell_potential_analysis to
nurovelle_core.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


DEFAULT_SSH_TARGET = "d4sd1ng@77.42.74.250"
OLD_DB = "nurovell_potential_analysis"
NEW_DB = "nurovelle_core"

LIVE_GET_URLS = [
    "https://nurovelle.de/",
    "https://nurovelle.de/homepage/analyse.html",
    "https://nurovelle.de/api/v1/questions?industry=service&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=manufacturing&tier=basic&include_risk=false",
    "https://nurovelle.de/api/v1/questions?industry=care&tier=basic&include_risk=false",
]

COUNT_TABLES = [
    "companies",
    "contacts",
    "analysis_sessions",
    "analysis_answers",
    "analysis_scores",
    "analysis_reports",
    "leads",
    "newsletter_campaigns",
    "notion_sync_jobs",
]


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: Any


def run_ssh(target: str, remote_command: str) -> str:
    command = [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "ConnectTimeout=12",
        target,
        remote_command,
    ]
    completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=45)
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()
        raise RuntimeError(detail or f"ssh command failed with exit code {completed.returncode}")
    return completed.stdout.strip()


def check_live_gets() -> CheckResult:
    errors: list[str] = []
    for url in LIVE_GET_URLS:
        request = urllib.request.Request(url, headers={"User-Agent": "nurovelle-cutover-preflight/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = response.getcode()
                if status < 200 or status >= 400:
                    errors.append(f"{url} returned HTTP {status}")
        except urllib.error.HTTPError as error:
            errors.append(f"{url} returned HTTP {error.code}")
        except Exception as error:
            errors.append(f"{url} failed: {error}")
    return CheckResult("live_get_endpoints", not errors, errors)


def check_runtime_summary(target: str, expected_db: str) -> CheckResult:
    remote = r"""
set -euo pipefail
docker inspect nurovell_backend --format '{{.State.Running}}' >/tmp/nurovelle_backend_running.txt
docker inspect postgres --format '{{.State.Running}}' >/tmp/nurovelle_postgres_running.txt
database_url="$(docker exec nurovell_backend printenv DATABASE_URL || true)"
current_db="$(DATABASE_URL="$database_url" python3 - <<'PY'
import os
from urllib.parse import urlparse
url = os.environ.get("DATABASE_URL", "")
print(urlparse(url).path.lstrip("/") or "")
PY
)"
printf '{"backend_running":"%s","postgres_running":"%s","current_db":"%s"}\n' \
  "$(cat /tmp/nurovelle_backend_running.txt)" \
  "$(cat /tmp/nurovelle_postgres_running.txt)" \
  "$current_db"
"""
    data = json.loads(run_ssh(target, remote))
    errors: list[str] = []
    if data.get("backend_running") != "true":
        errors.append("nurovell_backend is not running")
    if data.get("postgres_running") != "true":
        errors.append("postgres container is not running")
    if data.get("current_db") != expected_db:
        errors.append(f"live backend current_db is {data.get('current_db')!r}, expected {expected_db!r}")
    return CheckResult("runtime_summary", not errors, {"summary": data, "errors": errors})


def check_databases_and_tables(target: str) -> CheckResult:
    old_count_sql = " union all ".join([f"select '{table}', count(*) from public.{table}" for table in COUNT_TABLES])
    new_count_sql = " union all ".join([f"select '{table}', count(*) from public.{table}" for table in COUNT_TABLES])
    remote = f"""
set -euo pipefail
docker exec postgres psql -U avataruser -d postgres -v ON_ERROR_STOP=1 -t -A -F $'\\t' -c "
select 'db_exists', datname from pg_database where datname in ('{OLD_DB}', '{NEW_DB}') order by datname;
"
docker exec postgres psql -U avataruser -d {NEW_DB} -v ON_ERROR_STOP=1 -t -A -F $'\\t' -c "
select 'schema_exists', schema_name from information_schema.schemata where schema_name in ('analysis', 'homepage', 'content_system', 'ops', 'public') order by schema_name;
select 'alembic', version_num from public.alembic_version;
"
docker exec postgres psql -U avataruser -d {OLD_DB} -v ON_ERROR_STOP=1 -t -A -F $'\\t' -c "{old_count_sql};" | sed 's/^/old_count\\t/'
docker exec postgres psql -U avataruser -d {NEW_DB} -v ON_ERROR_STOP=1 -t -A -F $'\\t' -c "{new_count_sql};" | sed 's/^/new_count\\t/'
"""
    lines = [line for line in run_ssh(target, remote).splitlines() if line.strip()]
    dbs = sorted(line.split("\t", 1)[1] for line in lines if line.startswith("db_exists\t"))
    schemas = sorted(line.split("\t", 1)[1] for line in lines if line.startswith("schema_exists\t"))
    alembic = [line.split("\t", 1)[1] for line in lines if line.startswith("alembic\t")]
    counts = {}
    count_errors: list[str] = []
    old_counts: dict[str, int] = {}
    new_counts: dict[str, int] = {}
    for line in lines:
        parts = line.split("\t")
        if len(parts) == 3 and parts[0] == "old_count" and parts[1] in COUNT_TABLES:
            old_counts[parts[1]] = int(parts[2])
        if len(parts) == 3 and parts[0] == "new_count" and parts[1] in COUNT_TABLES:
            new_counts[parts[1]] = int(parts[2])

    for table in COUNT_TABLES:
        old_count = old_counts.get(table)
        new_count = new_counts.get(table)
        counts[table] = {"old": old_count, "new": new_count}
        if old_count != new_count:
            count_errors.append(f"{table} count mismatch: old={old_count}, new={new_count}")

    expected_schemas = ["analysis", "content_system", "homepage", "ops", "public"]
    errors: list[str] = []
    if set(dbs) != {NEW_DB, OLD_DB}:
        errors.append(f"database list mismatch: {dbs}")
    if schemas != expected_schemas:
        errors.append(f"schema list mismatch: {schemas}")
    if alembic != ["2026060801"]:
        errors.append(f"unexpected alembic version: {alembic}")
    errors.extend(count_errors)
    return CheckResult(
        "databases_tables_counts",
        not errors,
        {"dbs": dbs, "schemas": schemas, "alembic": alembic, "counts": counts, "errors": errors},
    )


def check_backups(target: str) -> CheckResult:
    remote = r"""
set -euo pipefail
backup_dir=/opt/nurovell-potential-analysis/backups/postgres
if [ ! -d "$backup_dir" ]; then
  printf '[]\n'
  exit 0
fi
find "$backup_dir" -maxdepth 1 -type f \( -name '*.dump' -o -name '*.sql' \) -printf '%f\t%s\n' | sort
"""
    lines = [line for line in run_ssh(target, remote).splitlines() if line.strip()]
    backups = []
    for line in lines:
        name, size = line.split("\t", 1)
        backups.append({"name": name, "bytes": int(size)})
    has_dump = any(item["name"].endswith(".dump") and item["bytes"] > 0 for item in backups)
    return CheckResult("backup_files_present", has_dump, backups)


def run_checks(target: str, expected_db: str = OLD_DB) -> list[CheckResult]:
    checks = [
        check_runtime_summary(target, expected_db),
        check_databases_and_tables(target),
        check_backups(target),
        check_live_gets(),
    ]
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only VPS backend DB cutover preflight.")
    parser.add_argument("--ssh-target", default=DEFAULT_SSH_TARGET)
    parser.add_argument("--expected-db", default=OLD_DB, choices=[OLD_DB, NEW_DB])
    args = parser.parse_args()

    try:
        checks = run_checks(args.ssh_target, expected_db=args.expected_db)
    except Exception as error:
        print(json.dumps({"passed": False, "error": str(error)}, indent=2, ensure_ascii=False))
        return 1

    output = {
        "passed": all(check.passed for check in checks),
        "checks": [
            {"name": check.name, "passed": check.passed, "detail": check.detail}
            for check in checks
        ],
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if output["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
