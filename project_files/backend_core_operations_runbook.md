# Backend Core Operations Runbook

Stand: 2026-06-15

## Zweck

Dieses Runbook dokumentiert die Betriebsbefehle fuer den aktuellen Backend-DB-Stand.

Aktuell:

```text
Live-Backend DB: nurovelle_core
Rollback-DB: nurovell_potential_analysis
```

Keine Secrets werden in diesem Dokument gespeichert.

## Post-Cutover-Preflight

Lokal aus dem Homepage-Repo:

```powershell
python tools\vps_backend_core_preflight.py --expected-db nurovelle_core
```

Erwartung:

- `runtime_summary` gruen
- `current_db` ist `nurovelle_core`
- Tabellen-Counts zwischen `nurovell_potential_analysis` und `nurovelle_core` stimmen ueberein
- Backup-Dateien sind vorhanden
- Live-GET-Endpunkte sind gruen

## Homepage/API-Readiness

```powershell
python tools\check_homepage_readiness.py
```

Erwartung:

- lokale Links/Assets gruen
- Branchenliste gruen
- Live-GETs gruen
- Frontend-Guardrails gruen

## Runtime-Status pruefen

Auf dem VPS:

```bash
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' | grep -E 'nurovell_backend|postgres|nurovell_frontend'
```

Erwartung:

- `nurovell_backend` laeuft
- `postgres` ist `healthy`
- `nurovell_frontend` laeuft

## Backend-Logs pruefen

```bash
docker logs --since 20m nurovell_backend 2>&1 | tail -200
```

Kritisch:

- Tracebacks
- DB connection errors
- Migration errors
- 5xx-Hinweise im API-Pfad

## Rollback

Rollback nur ausloesen, wenn der Live-Betrieb mit `nurovelle_core` fehlschlaegt.

Lokal aus dem Homepage-Repo:

```powershell
python tools\vps_backend_core_cutover.py --rollback-env-backup /opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_20260615_181902 --confirm rollback-nurovelle-core
```

Danach pruefen:

```powershell
python tools\vps_backend_core_preflight.py --expected-db nurovell_potential_analysis
python tools\check_homepage_readiness.py
```

## Nicht tun

- alte Datenbank nicht loeschen
- Backups nicht loeschen
- keine Secrets in Projektdateien schreiben
- keine direkte DB-Verbindung in die Homepage einbauen
- keine Firewall-, Tunnel- oder Heimnetz-Aenderungen fuer diesen DB-Betrieb
