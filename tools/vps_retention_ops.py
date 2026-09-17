#!/usr/bin/env python3
"""
Install and audit VPS retention controls for the Nurovelle runtime.

Default mode is audit. A real install requires:

  python tools/vps_retention_ops.py --install --execute --confirm install-vps-retention

This script never prints secrets.
"""

from __future__ import annotations

import argparse
import json
import secrets
import shlex
import subprocess
import sys
import textwrap


DEFAULT_SSH_TARGET = "d4sd1ng@77.42.74.250"
INSTALL_CONFIRM = "install-vps-retention"
REMOTE_RETENTION_SCRIPT = "/usr/local/sbin/nurovelle_retention.py"

JOURNALD_CONFIG = textwrap.dedent(
    """
    [Journal]
    SystemMaxUse=1G
    SystemKeepFree=1G
    SystemMaxFileSize=128M
    MaxRetentionSec=14day
    Compress=yes
    """
).strip()

LOGROTATE_CONFIG = textwrap.dedent(
    """
    /var/log/syslog
    /var/log/auth.log
    /var/log/kern.log
    /var/log/messages
    /var/log/nginx/*.log
    /var/log/apache2/*.log
    /opt/nurovell-potential-analysis/logs/*.log
    /opt/nurovell-potential-analysis/backend/logs/*.log
    /opt/nurovell-potential-analysis/frontend/logs/*.log
    /opt/nurovell-potential-analysis/compose/logs/*.log
    {
      daily
      rotate 14
      maxage 30
      missingok
      notifempty
      compress
      delaycompress
      copytruncate
      dateext
      sharedscripts
    }

    /var/lib/docker/containers/*/*.log
    {
      weekly
      rotate 8
      maxage 56
      missingok
      notifempty
      compress
      delaycompress
      copytruncate
      dateext
    }
    """
).strip()

REMOTE_RETENTION_PYTHON = textwrap.dedent(
    r"""
    #!/usr/bin/env python3
    from __future__ import annotations

    import argparse
    import json
    import re
    import subprocess
    from datetime import datetime, timezone
    from pathlib import Path

    BACKUP_DIR = Path("/opt/nurovell-potential-analysis/backups/postgres")
    ENV_DIR = Path("/opt/nurovell-potential-analysis/compose")
    BACKUP_EXTENSIONS = {".dump", ".sql"}
    PROTECTED_MARKERS = ("precutover", "legacy_data", "manual", "schema")
    KEEP_FOREVER_MARKERS = (".keep", "_keep", "-keep")
    BACKUP_DAILY_KEEP = 14
    BACKUP_WEEKLY_KEEP = 8
    PROTECTED_BACKUP_KEEP = 12
    PROTECTED_BACKUP_MAX_AGE_DAYS = 180
    ENV_BACKUP_KEEP = 12
    ENV_BACKUP_MAX_AGE_DAYS = 90
    TIMESTAMP_RE = re.compile(r"(\d{8}_\d{6})(?=[^0-9]*$)")


    def now_utc() -> datetime:
        return datetime.now(timezone.utc)


    def parse_timestamp(name: str, fallback_epoch: float) -> datetime:
        match = TIMESTAMP_RE.search(name)
        if match:
            return datetime.strptime(match.group(1), "%Y%m%d_%H%M%S").replace(tzinfo=timezone.utc)
        return datetime.fromtimestamp(fallback_epoch, tz=timezone.utc)


    def age_days(path: Path, current_time: datetime) -> int:
        return int((current_time - datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)).total_seconds() // 86400)


    def file_record(path: Path, *, protected: bool, bucket: str, keep: bool, reason: str, current_time: datetime) -> dict[str, object]:
        stat = path.stat()
        return {
            "path": str(path),
            "name": path.name,
            "bytes": stat.st_size,
            "mtime_epoch": round(stat.st_mtime, 3),
            "age_days": age_days(path, current_time),
            "protected": protected,
            "bucket": bucket,
            "keep": keep,
            "reason": reason,
        }


    def classify_backup(path: Path) -> tuple[bool, bool]:
        lower = path.name.lower()
        protected = any(marker in lower for marker in PROTECTED_MARKERS)
        keep_forever = any(marker in lower for marker in KEEP_FOREVER_MARKERS)
        return protected, keep_forever


    def sorted_backups(paths: list[Path]) -> list[Path]:
        return sorted(paths, key=lambda path: parse_timestamp(path.name, path.stat().st_mtime), reverse=True)


    def select_unprotected_backups(paths: list[Path]) -> dict[Path, tuple[str, str]]:
        keep_map: dict[Path, tuple[str, str]] = {}
        for path in paths[:BACKUP_DAILY_KEEP]:
            keep_map[path] = ("daily", f"keep newest {BACKUP_DAILY_KEEP} daily backups")
        weekly_kept = 0
        weekly_keys: set[tuple[int, int]] = set()
        for path in paths[BACKUP_DAILY_KEEP:]:
            timestamp = parse_timestamp(path.name, path.stat().st_mtime)
            weekly_key = (timestamp.isocalendar().year, timestamp.isocalendar().week)
            if weekly_key not in weekly_keys and weekly_kept < BACKUP_WEEKLY_KEEP:
                keep_map[path] = ("weekly", f"keep newest backup for ISO week {weekly_key[0]}-{weekly_key[1]:02d}")
                weekly_keys.add(weekly_key)
                weekly_kept += 1
        return keep_map


    def select_protected_backups(paths: list[Path], current_time: datetime) -> dict[Path, tuple[str, str]]:
        keep_map: dict[Path, tuple[str, str]] = {}
        protected_kept = 0
        for path in paths:
            _, keep_forever = classify_backup(path)
            file_age_days = age_days(path, current_time)
            if keep_forever:
                keep_map[path] = ("protected-forever", "keep due to explicit keep marker in filename")
                continue
            if protected_kept < PROTECTED_BACKUP_KEEP:
                keep_map[path] = ("protected-count", f"keep newest {PROTECTED_BACKUP_KEEP} protected backups")
                protected_kept += 1
                continue
            if file_age_days <= PROTECTED_BACKUP_MAX_AGE_DAYS:
                keep_map[path] = ("protected-age", f"keep protected backups for {PROTECTED_BACKUP_MAX_AGE_DAYS} days")
                continue
        return keep_map


    def select_env_backups(paths: list[Path], current_time: datetime) -> dict[Path, tuple[str, str]]:
        keep_map: dict[Path, tuple[str, str]] = {}
        for path in paths[:ENV_BACKUP_KEEP]:
            keep_map[path] = ("env-count", f"keep newest {ENV_BACKUP_KEEP} env backups")
        for path in paths[ENV_BACKUP_KEEP:]:
            file_age_days = age_days(path, current_time)
            if file_age_days <= ENV_BACKUP_MAX_AGE_DAYS:
                keep_map[path] = ("env-age", f"keep env backups for {ENV_BACKUP_MAX_AGE_DAYS} days")
        return keep_map


    def build_rotation_plan(current_time: datetime) -> dict[str, object]:
        postgres_paths = []
        if BACKUP_DIR.exists():
            postgres_paths = [path for path in BACKUP_DIR.iterdir() if path.is_file() and path.suffix in BACKUP_EXTENSIONS]
        postgres_paths = sorted_backups(postgres_paths)
        protected_paths = [path for path in postgres_paths if classify_backup(path)[0]]
        unprotected_paths = [path for path in postgres_paths if not classify_backup(path)[0]]
        unprotected_keep = select_unprotected_backups(unprotected_paths)
        protected_keep = select_protected_backups(protected_paths, current_time)

        env_paths = []
        if ENV_DIR.exists():
            env_paths = [
                path
                for path in ENV_DIR.iterdir()
                if path.is_file() and path.name.startswith(".env.vps.pre_nurovelle_core_")
            ]
        env_paths = sorted_backups(env_paths)
        env_keep = select_env_backups(env_paths, current_time)

        postgres_actions = []
        for path in postgres_paths:
            protected, _ = classify_backup(path)
            keep_info = protected_keep.get(path) if protected else unprotected_keep.get(path)
            if keep_info:
                postgres_actions.append(file_record(path, protected=protected, bucket=keep_info[0], keep=True, reason=keep_info[1], current_time=current_time))
            else:
                postgres_actions.append(file_record(path, protected=protected, bucket="delete", keep=False, reason="outside daily/weekly/protected retention window", current_time=current_time))

        env_actions = []
        for path in env_paths:
            keep_info = env_keep.get(path)
            if keep_info:
                env_actions.append(file_record(path, protected=False, bucket=keep_info[0], keep=True, reason=keep_info[1], current_time=current_time))
            else:
                env_actions.append(file_record(path, protected=False, bucket="delete", keep=False, reason="outside env backup retention window", current_time=current_time))

        def summarize(actions: list[dict[str, object]], path_label: str) -> dict[str, object]:
            total_bytes = sum(int(item["bytes"]) for item in actions)
            deletions = [item for item in actions if not item["keep"]]
            kept = [item for item in actions if item["keep"]]
            return {
                "path": path_label,
                "count": len(actions),
                "kept_count": len(kept),
                "delete_count": len(deletions),
                "total_bytes": total_bytes,
                "delete_bytes": sum(int(item["bytes"]) for item in deletions),
                "kept_bytes": sum(int(item["bytes"]) for item in kept),
                "files": actions,
            }

        return {
            "generated_at": current_time.isoformat(),
            "policy": {
                "postgres_daily_keep": BACKUP_DAILY_KEEP,
                "postgres_weekly_keep": BACKUP_WEEKLY_KEEP,
                "protected_backup_keep": PROTECTED_BACKUP_KEEP,
                "protected_backup_max_age_days": PROTECTED_BACKUP_MAX_AGE_DAYS,
                "env_backup_keep": ENV_BACKUP_KEEP,
                "env_backup_max_age_days": ENV_BACKUP_MAX_AGE_DAYS,
                "protected_markers": list(PROTECTED_MARKERS),
                "keep_forever_markers": list(KEEP_FOREVER_MARKERS),
            },
            "postgres": summarize(postgres_actions, str(BACKUP_DIR)),
            "env_backups": summarize(env_actions, str(ENV_DIR)),
        }


    def apply_plan(plan: dict[str, object]) -> dict[str, object]:
        deleted: list[str] = []
        for section in ("postgres", "env_backups"):
            files = plan[section]["files"]
            for item in files:
                if item["keep"]:
                    continue
                path = Path(item["path"])
                if path.exists():
                    path.unlink()
                    deleted.append(str(path))
        plan["deleted_paths"] = deleted
        return plan


    def docker_prune() -> dict[str, object]:
        commands = [
            ["docker", "image", "prune", "-af", "--filter", "until=168h"],
            ["docker", "container", "prune", "-f", "--filter", "until=168h"],
            ["docker", "builder", "prune", "-af", "--filter", "until=168h"],
            ["docker", "volume", "prune", "-f"],
        ]
        outputs = []
        for command in commands:
            completed = subprocess.run(command, check=False, capture_output=True, text=True)
            outputs.append(
                {
                    "command": command,
                    "returncode": completed.returncode,
                    "stdout": completed.stdout.strip(),
                    "stderr": completed.stderr.strip(),
                }
            )
            if completed.returncode != 0:
                raise SystemExit(json.dumps({"docker_prune_failed": outputs}, indent=2))
        return {"docker_prune": outputs}


    def main() -> int:
        parser = argparse.ArgumentParser(description="Rotate VPS backups/env backups and prune unused Docker artifacts.")
        parser.add_argument("command", choices=["report", "rotate", "docker-prune", "rotate-all"])
        parser.add_argument("--apply", action="store_true", help="Delete files for rotate/rotate-all.")
        parser.add_argument("--json", action="store_true", help="Emit JSON.")
        args = parser.parse_args()

        current_time = now_utc()
        if args.command == "report":
            plan = build_rotation_plan(current_time)
            print(json.dumps(plan, indent=2))
            return 0
        if args.command == "docker-prune":
            result = docker_prune()
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                for item in result["docker_prune"]:
                    print("command:", " ".join(item["command"]))
                    print(f"returncode: {item['returncode']}")
                    if item["stdout"]:
                        print(item["stdout"])
                    if item["stderr"]:
                        print(item["stderr"])
                    print("")
            return 0

        plan = build_rotation_plan(current_time)
        if args.apply:
            plan = apply_plan(plan)
        if args.command == "rotate-all":
            docker_result = docker_prune()
            plan["docker"] = docker_result["docker_prune"]
        print(json.dumps(plan, indent=2))
        return 0


    if __name__ == "__main__":
        raise SystemExit(main())
    """
).strip()

DOCKER_PRUNE_SERVICE = textwrap.dedent(
    """
    [Unit]
    Description=Prune unused Docker artifacts for Nurovelle VPS
    After=docker.service
    Wants=docker.service

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/python3 /usr/local/sbin/nurovelle_retention.py docker-prune --json
    """
).strip()

DOCKER_PRUNE_TIMER = textwrap.dedent(
    """
    [Unit]
    Description=Weekly Docker prune for Nurovelle VPS

    [Timer]
    OnCalendar=Sun *-*-* 04:10:00
    Persistent=true

    [Install]
    WantedBy=timers.target
    """
).strip()

RETENTION_SERVICE = textwrap.dedent(
    """
    [Unit]
    Description=Rotate Nurovelle VPS backups and env backups

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/python3 /usr/local/sbin/nurovelle_retention.py rotate --apply --json
    """
).strip()

RETENTION_TIMER = textwrap.dedent(
    """
    [Unit]
    Description=Daily backup/env-backup rotation for Nurovelle VPS

    [Timer]
    OnCalendar=*-*-* 02:15:00
    Persistent=true

    [Install]
    WantedBy=timers.target
    """
).strip()


def run_ssh_script(target: str, script: str, timeout: int = 240) -> str:
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


def heredoc_write(path: str, content: str, mode: str) -> str:
    marker = f"__NUROVELLE_EOF_{secrets.token_hex(12)}__"
    directory = path.rsplit("/", 1)[0]
    return textwrap.dedent(
        f"""
        sudo install -d -m 0755 {shlex.quote(directory)}
        cat <<'{marker}' | sudo tee {shlex.quote(path)} >/dev/null
        {content}
        {marker}
        sudo chmod {mode} {shlex.quote(path)}
        """
    ).strip()


def install_script() -> str:
    steps = [
        "set -euo pipefail",
        "sudo -n true >/dev/null",
        heredoc_write("/etc/systemd/journald.conf.d/nurovelle-retention.conf", JOURNALD_CONFIG, "0644"),
        heredoc_write("/etc/logrotate.d/nurovelle-vps", LOGROTATE_CONFIG, "0644"),
        heredoc_write(REMOTE_RETENTION_SCRIPT, REMOTE_RETENTION_PYTHON, "0755"),
        heredoc_write("/etc/systemd/system/nurovelle-docker-prune.service", DOCKER_PRUNE_SERVICE, "0644"),
        heredoc_write("/etc/systemd/system/nurovelle-docker-prune.timer", DOCKER_PRUNE_TIMER, "0644"),
        heredoc_write("/etc/systemd/system/nurovelle-retention-maintenance.service", RETENTION_SERVICE, "0644"),
        heredoc_write("/etc/systemd/system/nurovelle-retention-maintenance.timer", RETENTION_TIMER, "0644"),
        "sudo systemctl restart systemd-journald",
        "sudo systemctl daemon-reload",
        "sudo systemctl enable --now nurovelle-docker-prune.timer nurovelle-retention-maintenance.timer",
        "sudo logrotate -d /etc/logrotate.conf >/tmp/nurovelle-logrotate-dry-run.txt 2>&1 || (cat /tmp/nurovelle-logrotate-dry-run.txt && exit 1)",
        "cat /tmp/nurovelle-logrotate-dry-run.txt",
        "python3 /usr/local/sbin/nurovelle_retention.py report --json",
        "printf '\\n'",
        "sudo systemctl list-timers --all 'nurovelle-*' --no-pager",
        "printf '\\n'",
        "sudo journalctl --disk-usage",
    ]
    return "\n".join(steps)


def audit_script() -> str:
    return textwrap.dedent(
        f"""
        set -euo pipefail
        python3 - <<'PY'
import json
import subprocess
from pathlib import Path

paths = {{
    "journald_conf": Path("/etc/systemd/journald.conf.d/nurovelle-retention.conf"),
    "logrotate_conf": Path("/etc/logrotate.d/nurovelle-vps"),
    "retention_script": Path("{REMOTE_RETENTION_SCRIPT}"),
    "docker_prune_service": Path("/etc/systemd/system/nurovelle-docker-prune.service"),
    "docker_prune_timer": Path("/etc/systemd/system/nurovelle-docker-prune.timer"),
    "retention_service": Path("/etc/systemd/system/nurovelle-retention-maintenance.service"),
    "retention_timer": Path("/etc/systemd/system/nurovelle-retention-maintenance.timer"),
}}

def run(command):
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    return {{
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }}

result = {{
    "files": {{name: path.exists() for name, path in paths.items()}},
    "journal_disk_usage": run(["sudo", "journalctl", "--disk-usage"]),
    "timers": run(["sudo", "systemctl", "list-timers", "--all", "nurovelle-*", "--no-pager"]),
}}

retention_script = paths["retention_script"]
if retention_script.exists():
    result["retention_report"] = run(["sudo", "python3", str(retention_script), "report", "--json"])

print(json.dumps(result, indent=2))
PY
        """
    ).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Install or audit VPS retention controls.")
    parser.add_argument("--ssh-target", default=DEFAULT_SSH_TARGET)
    parser.add_argument("--install", action="store_true", help="Install/update the remote retention controls.")
    parser.add_argument("--execute", action="store_true", help="Run the real install.")
    parser.add_argument("--confirm", default="", help="Required confirmation word for install.")
    args = parser.parse_args()

    if not args.install:
        try:
            output = run_ssh_script(args.ssh_target, audit_script(), timeout=180)
        except Exception as error:
            print(json.dumps({"audit": "failed", "error": str(error)}, indent=2))
            return 1
        print(json.dumps({"audit": "completed", "remote_output": json.loads(output)}, indent=2))
        return 0

    if not args.execute:
        print("dry_run=true")
        print(f"install_requires=--install --execute --confirm {INSTALL_CONFIRM}")
        return 0

    if args.confirm != INSTALL_CONFIRM:
        print(f"install refused: pass --confirm {INSTALL_CONFIRM!r}", file=sys.stderr)
        return 2

    try:
        output = run_ssh_script(args.ssh_target, install_script(), timeout=420)
    except Exception as error:
        print(json.dumps({"install": "failed", "error": str(error)}, indent=2))
        return 1
    print(json.dumps({"install": "completed", "remote_output": output}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
