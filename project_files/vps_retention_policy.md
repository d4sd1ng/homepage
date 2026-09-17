# VPS Retention Policy

Stand: 2026-07-24

## Zweck

Diese Datei dokumentiert die verbindliche Aufteilung fuer Log-Rotation, Docker-Cleanup, Backup-Rotation und Verifikation auf dem VPS.

## Ownership

- Homepage-Deploy bleibt in `/home/runner/work/homepage/homepage/.github/workflows/deploy.yml`.
- Allgemeine VPS-Retention gehoert nicht in die Homepage-Inhalte.
- Serverweite Retention fuer `/opt/nurovell-potential-analysis/...` wird ueber VPS-Ops-Tooling aus diesem Repo verwaltet.

## Installationswerkzeug

Lokal aus dem Homepage-Repo:

```powershell
python tools\vps_retention_ops.py
python tools\vps_retention_ops.py --install --execute --confirm install-vps-retention
```

Verhalten:

- Default ohne `--install`: Audit der Remote-Dateien, Timer und Journal-Nutzung.
- `--install --execute --confirm install-vps-retention`: installiert oder aktualisiert die serverweiten Retention-Dateien.

## Installierte Server-Dateien

- `/etc/systemd/journald.conf.d/nurovelle-retention.conf`
- `/etc/logrotate.d/nurovelle-vps`
- `/usr/local/sbin/nurovelle_retention.py`
- `/etc/systemd/system/nurovelle-docker-prune.service`
- `/etc/systemd/system/nurovelle-docker-prune.timer`
- `/etc/systemd/system/nurovelle-retention-maintenance.service`
- `/etc/systemd/system/nurovelle-retention-maintenance.timer`

## Journald-Retention

Datei:

```text
/etc/systemd/journald.conf.d/nurovelle-retention.conf
```

Regeln:

- `SystemMaxUse=1G`
- `SystemKeepFree=1G`
- `SystemMaxFileSize=128M`
- `MaxRetentionSec=14day`
- `Compress=yes`

Damit sind binaere Journal-Dateien sowohl ueber Groesse als auch ueber Alter begrenzt.

## Log-Rotation

Datei:

```text
/etc/logrotate.d/nurovelle-vps
```

Abgedeckte Loggruppen:

- System-Logs: `/var/log/syslog`, `/var/log/auth.log`, `/var/log/kern.log`, `/var/log/messages`
- Webserver-Logs: `/var/log/nginx/*.log`, `/var/log/apache2/*.log`
- App-/Custom-Logs:
  - `/opt/nurovell-potential-analysis/logs/*.log`
  - `/opt/nurovell-potential-analysis/backend/logs/*.log`
  - `/opt/nurovell-potential-analysis/frontend/logs/*.log`
  - `/opt/nurovell-potential-analysis/compose/logs/*.log`
- Docker-Container-Logs: `/var/lib/docker/containers/*/*.log`

Rotation:

- App-/System-/Web-Logs: taeglich, `rotate 14`, `maxage 30`, komprimiert
- Docker-Container-Logs: woechentlich, `rotate 8`, `maxage 56`, komprimiert

## Docker-Cleanup

Service/Timer:

- `nurovelle-docker-prune.service`
- `nurovelle-docker-prune.timer`

Zeitplan:

- Sonntags um `04:10`

Cleanup-Regeln:

- `docker image prune -af --filter until=168h`
- `docker container prune -f --filter until=168h`
- `docker builder prune -af --filter until=168h`
- `docker volume prune -f`

Schutz:

- Laufende Container werden nicht entfernt.
- Nur ungenutzte Images, gestoppte Container, Build-Cache und verwaiste Volumes werden bereinigt.

## Postgres-Backup-Retention

Pfad:

```text
/opt/nurovell-potential-analysis/backups/postgres
```

Dateitypen:

- `*.dump`
- `*.sql`

Regeln fuer normale Backups:

- die neuesten `14` Backups bleiben immer erhalten
- danach bleibt pro ISO-Kalenderwoche das neueste Backup fuer `8` Wochen erhalten
- alles ausserhalb dieses Fensters wird entfernt

Geschuetzte Backup-Namen:

- Marker: `precutover`, `legacy_data`, `manual`, `schema`
- explizit dauerhaft schuetzen: Dateinamen mit `.keep`, `_keep` oder `-keep`

Regeln fuer geschuetzte Backups:

- die neuesten `12` geschuetzten Backups bleiben immer erhalten
- weitere geschuetzte Backups bleiben bis `180` Tage erhalten
- nur aeltere geschuetzte Backups ausserhalb dieses Fensters duerfen entfernt werden

## Runtime-Env-Backup-Retention

Pfad:

```text
/opt/nurovell-potential-analysis/compose
```

Dateimuster:

```text
.env.vps.pre_nurovelle_core_YYYYMMDD_HHMMSS
```

Regeln:

- die neuesten `12` Env-Backups bleiben immer erhalten
- weitere Env-Backups bleiben bis `90` Tage erhalten
- aeltere Env-Backups ausserhalb dieses Fensters werden entfernt

## Geplanter Scheduler

Service/Timer:

- `nurovelle-retention-maintenance.service`
- `nurovelle-retention-maintenance.timer`

Zeitplan:

- taeglich um `02:15`

Aktion:

- rotiert Postgres-Backups
- rotiert `.env.vps.pre_nurovelle_core_*`

## Verifikation

Read-only:

```powershell
python tools\vps_retention_ops.py
python tools\vps_backend_core_preflight.py --expected-db nurovelle_core
```

`vps_backend_core_preflight.py` meldet jetzt zusaetzlich:

- Anzahl der Postgres-Backups
- Gesamtgroesse der Postgres-Backups
- Alter juengster/aeltester Postgres-Backups
- Anzahl und Gesamtgroesse der Env-Backups
- `pg_restore --list`-Pruefung auf dem neuesten Dump
- Hinweis auf den weiterhin verpflichtenden monatlichen Restore-Test

## Restore-Test-Pflicht

Die automatisierte `pg_restore --list`-Pruefung bestaetigt nur, dass der neueste Dump lesbar ist.

Verbindlich bleibt:

- mindestens monatlich ein nicht-produktiver Restore-Test
- Ergebnis dokumentieren
- bei Fehlern Rotation nicht anpassen, bevor die Restore-Ursache geklaert ist
