# Backend Database Cutover Plan

Stand: 2026-06-15

## Ziel

Dieses Dokument beschreibt die sichere Umschaltung des Live-Backends von:

```text
nurovell_potential_analysis
```

auf:

```text
nurovelle_core
```

Die Umschaltung wurde am 2026-06-15 ausgefuehrt.

Aktueller Stand:

```text
Live-Backend DB: nurovelle_core
Rollback-DB: nurovell_potential_analysis
```

## Voraussetzungen

Erledigt:

- `nurovelle_core` existiert im Runtime-Postgres-Container.
- Core-Schemas `analysis`, `homepage`, `content_system`, `ops` existieren.
- Legacy-Tabellen existieren in `nurovelle_core.public`.
- Alembic-Stand in `nurovelle_core.public`: `2026060801`.
- Legacy-Daten aus `nurovell_potential_analysis.public` wurden nach `nurovelle_core.public` kopiert.
- Backup von `nurovell_potential_analysis` existiert.
- Restore-Test war erfolgreich.
- Read-only Backend-Smoke gegen `nurovelle_core` war erfolgreich.
- Schreibender Backend-E2E gegen `nurovelle_core` war erfolgreich.
- Markierter Testdatensatz wurde bereinigt.

Erledigt bei Umschaltung:

- Finaler Pre-Cutover-Backup-Dump erzeugt.
- Alte `.env.vps` serverseitig gesichert.
- Legacy-Daten direkt vor Umschaltung nach `nurovelle_core.public` kopiert.
- `DATABASE_URL` auf `nurovelle_core` umgestellt.
- Backend neu gestartet.
- Live-Smoke ausgefuehrt.
- Schreibender Live-E2E ausgefuehrt und Testdatensatz bereinigt.

Cutover-Artefakte:

```text
/opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_precutover_20260615_181902.dump
/opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_legacy_data_20260615_181902.dump
/opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_20260615_181902
```

## Nicht aendern

- Keine Passwoerter in Repo oder Chat speichern.
- Keine alte Datenbank loeschen.
- Keine alten Backups loeschen.
- Keine Homepage-Direktverbindung zu Postgres einbauen.

## Cutover-Ablauf

Status: ausgefuehrt am 2026-06-15.

### 1. Wartungsfenster setzen

Vorher festlegen:

```text
Startzeit
verantwortliche Person
Rollback-Entscheidungspunkt
```

### 2. Finales Backup erzeugen

Auf dem VPS:

```bash
mkdir -p /opt/nurovell-potential-analysis/backups/postgres

docker exec postgres pg_dump \
  -U avataruser \
  --format=custom \
  --dbname=nurovell_potential_analysis \
  > /opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_precutover_YYYYMMDD_HHMMSS.dump
```

Backup pruefen:

```bash
docker exec -i postgres pg_restore --list \
  < /opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_precutover_YYYYMMDD_HHMMSS.dump
```

### 3. Delta-Daten nach `nurovelle_core` kopieren

Da zwischen dem ersten Kopieren und dem Cutover neue Leads/Analysen entstehen koennen, muss direkt vor der Umschaltung ein Delta- oder Full-Refresh entschieden werden.

MVP-Variante:

- Wartungsfenster kurz halten.
- Backend stoppen.
- `nurovelle_core.public` Legacy-Tabellen leeren.
- Full-Copy aus finalem Backup oder aus `nurovell_potential_analysis` wiederholen.
- Backend auf `nurovelle_core` starten.

Wichtig:

Dieser Schritt darf erst als separater Deploy-Schritt ausgefuehrt werden.

### 4. Alte Runtime-Konfiguration sichern

Datei:

```text
/opt/nurovell-potential-analysis/compose/.env.vps
```

Vor Aenderung kopieren:

```bash
cp /opt/nurovell-potential-analysis/compose/.env.vps \
   /opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_YYYYMMDD_HHMMSS
```

### 5. `DATABASE_URL` umstellen

Nur den Datenbanknamen aendern:

```text
alt: db=nurovell_potential_analysis
neu: db=nurovelle_core
```

User, Passwort, Host und Port bleiben unveraendert, sofern der bestehende Backend-User weiter genutzt wird.

### 6. Backend neu starten

Im Compose-Verzeichnis:

```bash
cd /opt/nurovell-potential-analysis/compose
docker compose -f docker-compose.vps.yml up -d --build nurovell_backend
```

Falls das Projekt einen anderen Compose-Aufruf nutzt, den vorhandenen Deploy-Befehl verwenden und dokumentieren.

### 7. Live-Smoke

Nicht-schreibend:

```text
GET https://nurovelle.de/api/v1/questions?industry=service&tier=basic&include_risk=false
GET https://nurovelle.de/api/v1/questions?industry=manufacturing&tier=basic&include_risk=false
GET https://nurovelle.de/api/v1/questions?industry=care&tier=basic&include_risk=false
```

Schreibend mit markiertem Testdatensatz:

```text
POST /api/v1/analysis/start
POST /api/v1/analysis/<analysis_id>/answers
POST /api/v1/analysis/<analysis_id>/score
POST /api/v1/analysis/<analysis_id>/report
POST /api/v1/lead
```

Danach Testdatensatz bereinigen.

Ausgefuehrtes Ergebnis:

```text
Runtime DB: nurovelle_core
Live GETs: gruen
Schreibender E2E: gruen
Test-Analyse: c0f3eca6-b98e-447e-b0a6-763387181959
Test-Lead: readiness-cutover-20260615202145@example.invalid
Cleanup: verifiziert, alle markierten Testdaten = 0
```

## Rollback

Rollback ausloesen, wenn:

- Backend startet nicht.
- Fragen-Endpunkte liefern nicht 200.
- Analyse-Start scheitert.
- Score/Report/Lead schreiben nicht.
- unerwartete DB-Fehler in Logs erscheinen.

Rollback-Schritte:

1. `.env.vps` aus Backup wiederherstellen.
2. Backend neu starten.
3. Fragen-Endpunkte testen.
4. Live-Homepage `analyse.html` testen.
5. Fehler in `project_files/CHANGELOG_PROJECT_FILES.md` dokumentieren.

Beispiel:

```bash
cp /opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_YYYYMMDD_HHMMSS \
   /opt/nurovell-potential-analysis/compose/.env.vps

cd /opt/nurovell-potential-analysis/compose
docker compose -f docker-compose.vps.yml up -d --build nurovell_backend
```

Aktuelle Rollback-Datei:

```text
/opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_20260615_181902
```

## Akzeptanzkriterien fuer Cutover

Cutover gilt erst als erfolgreich, wenn:

- Backend mit `nurovelle_core` startet.
- alle drei Fragen-Endpunkte 200 liefern.
- schreibender Testdatensatz vollstaendig durchlaeuft.
- Testdatensatz wieder bereinigt wurde.
- keine kritischen Backend-Logs auftreten.
- alte Datenbank weiterhin unveraendert als Rollback-Quelle existiert.
- finaler Stand im Changelog dokumentiert ist.

Status 2026-06-15:

Alle Akzeptanzkriterien sind erfuellt. Die alte Datenbank bleibt als Rollback-Quelle erhalten.
