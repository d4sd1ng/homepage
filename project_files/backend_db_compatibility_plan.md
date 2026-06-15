# Backend DB Compatibility Plan

Stand: 2026-06-15

## Zweck

Dieses Dokument beschreibt, was vor einer Umstellung des Live-Backends von `nurovell_potential_analysis` auf `nurovelle_core` passieren muss.

Wichtig:

Eine reine Aenderung von `DATABASE_URL` ist aktuell nicht freigegeben.

## Ist-Zustand Live-Backend

Runtime:

```text
Container: nurovell_backend
DB-Host: postgres
DB-Container: postgres
Aktive DB: nurovell_potential_analysis
Migration-System: Alembic / Flask-Migrate
Aktueller Alembic-Stand: 2026060801
```

Die Live-Backend-Models verwenden aktuell Tabellen im `public` Schema.

## Legacy-Tabellen im Live-Backend

| Tabelle | Zweck | Approx. Rows |
|---|---|---:|
| `admin_users` | Admin Login/User | 0 |
| `alembic_version` | Migrationstand | 1 |
| `companies` | Firmen aus Analyseflow | 8 |
| `contacts` | Kontakte aus Analyseflow | 8 |
| `analysis_sessions` | Analyse-Sessions | 8 |
| `analysis_answers` | Antworten | 336 |
| `analysis_scores` | Scores | 6 |
| `analysis_reports` | Reports | 3 |
| `events` | Tracking/Eventlog | 0 |
| `leads` | Lead-Formular | 3 |
| `newsletter_campaigns` | Newsletter Kampagnen | 0 |
| `notion_sync_jobs` | Notion Sync Queue | 0 |

Die Zahlen sind `pg_stat_user_tables.n_live_tup` und damit Naeherungswerte, keine Dateninhalte.

## Zielstruktur `nurovelle_core`

`nurovelle_core` ist im Runtime-Postgres vorhanden und initialisiert.

Aktuelle Zieltabellen:

```text
analysis.submissions
analysis.answers
analysis.results
homepage.leads
homepage.lead_events
ops.integration_errors
ops.audit_events
```

Zusaetzlich wurde `nurovelle_core` als MVP-Uebergang mit den bestehenden Alembic-Migrationen legacy-kompatibel vorbereitet.

Verifizierte Legacy-Tabellen in `nurovelle_core.public`:

```text
admin_users
alembic_version
companies
contacts
analysis_sessions
analysis_answers
analysis_scores
analysis_reports
events
leads
newsletter_campaigns
notion_sync_jobs
```

Alembic-Stand in `nurovelle_core.public`:

```text
2026060801
```

Diese Struktur ist fachlich sauberer, aber nicht 1:1 kompatibel mit den bestehenden SQLAlchemy-Models.

## Hauptunterschiede

### Analyse

Legacy:

```text
public.companies
public.contacts
public.analysis_sessions
public.analysis_answers
public.analysis_scores
public.analysis_reports
```

Core-Ziel:

```text
analysis.submissions
analysis.answers
analysis.results
```

Unterschied:

- Legacy trennt Firma, Kontakt, Session, Antworten, Score und Report.
- Core fasst Submission-Kontakt-/Firmendaten in `analysis.submissions` zusammen.
- Legacy `analysis_answers.answer_value` ist `jsonb`; Core `analysis.answers.answer` ist aktuell `text`.
- Legacy hat getrennte Score-Spalten; Core speichert Score/Report flexibel als JSONB.

### Leads

Legacy:

```text
public.leads
```

Core-Ziel:

```text
homepage.leads
homepage.lead_events
```

Unterschied:

- Legacy `leads.id` ist Integer.
- Core `homepage.leads.lead_id` ist UUID.
- Legacy nutzt `newsletter_subscribed`; Core nutzt `newsletter`.
- Core hat zusaetzliche Sync-Felder `notion_sync_status` und `email_sync_status`.

### Notion

Legacy:

```text
public.notion_sync_jobs
```

Core-Ziel:

Noch kein vollstaendiges Runtime-Tabellenmodell in `content_system` oder `ops`.

Unterschied:

- Core-Architektur hat lokale Mapping-/Failed-Sync-Strategie dokumentiert.
- Runtime-Backend nutzt aber bereits eine Sync-Queue-Tabelle.

## Migrationsoptionen

### Option A: Legacy-kompatibel in `nurovelle_core`

Beschreibung:

- Bestehende Alembic-Migrationen werden gegen `nurovelle_core` ausgefuehrt.
- Legacy-Tabellen entstehen zunaechst im `public` Schema von `nurovelle_core`.
- Backend kann danach mit minimalem Code-Risiko gegen `nurovelle_core` getestet werden.

Vorteile:

- geringstes Risiko fuer Live-Endpunkte
- nutzt bestehendes Alembic-System
- schnelle Staging-Pruefung moeglich

Nachteile:

- `nurovelle_core` enthaelt zusaetzlich Legacy-Tabellen im `public` Schema
- fachliche Schematrennung wird erst spaeter sauber

### Option B: Backend-Models auf Core-Schemas migrieren

Beschreibung:

- SQLAlchemy-Models bekommen Schema-Zuordnung und ggf. neue Tabellenstruktur.
- Services/Repositories werden auf `analysis.*`, `homepage.*`, `ops.*` angepasst.

Vorteile:

- sauberere Zielarchitektur
- weniger Doppelstruktur

Nachteile:

- groesserer Code-Eingriff
- hoehere Regression-Gefahr
- mehr Testaufwand vor Live-Umschaltung

## Empfehlung

Fuer MVP/Readiness:

1. Option A als Zwischenschritt nutzen. Status: entschieden und vorbereitet.
2. Legacy-Tabellen in `nurovelle_core` mit Alembic aufbauen. Status: erledigt.
3. Daten aus `nurovell_potential_analysis` in `nurovelle_core` kopieren. Status: erledigt.
4. Backend in einer Test-/Staging-Session gegen `nurovelle_core` starten. Status: read-only Smoke erledigt.
5. Schreibenden E2E mit markiertem Testdatensatz pruefen. Status: offen.
6. Erst danach Runtime-`DATABASE_URL` umstellen. Status: blockiert.
7. Option B spaeter als kontrollierte Refactoring-/Migrationphase planen. Status: offen.

Grund:

Die bestehende Live-Strecke ist bereits auf die Legacy-Models abgestimmt. Eine sofortige Schema-Migration wuerde zu viele Veraenderungen gleichzeitig erzwingen.

## Konkrete naechste Schritte

### 1. Schema-only Backup

```bash
pg_dump --schema-only nurovell_potential_analysis > schema_legacy.sql
```

Status:

```text
/opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_schema_20260615_175622.sql
```

### 2. Data Backup

```bash
pg_dump --format=custom nurovell_potential_analysis > nurovell_potential_analysis_backup_YYYYMMDD_HHMMSS.dump
```

Status:

```text
/opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_backup_20260615_175622.dump
```

Der Dump wurde mit `pg_restore --list` erfolgreich gelesen.

### 3. Alembic gegen `nurovelle_core` testen

Nicht live umschalten.

Stattdessen:

- separate Test-Env mit `DATABASE_URL` auf `nurovelle_core`
- `flask db upgrade` oder aequivalenter Alembic-Befehl
- pruefen, ob Legacy-Tabellen im `public` Schema von `nurovelle_core` entstehen

Status:

- isolierte Testdatenbank `nurovelle_core_alembic_test_*` erstellt
- Alembic bis `2026060801` erfolgreich ausgefuehrt
- Tabellen und Alembic-Version verifiziert
- Testdatenbank danach wieder entfernt
- Alembic danach gegen `nurovelle_core` ausgefuehrt
- dafuer war `CREATE` auf Schema `public` fuer `nurovell_potential_user` notwendig

### 4. Datenmigration testen

Testweise nur nach Backup:

- `companies`
- `contacts`
- `analysis_sessions`
- `analysis_answers`
- `analysis_scores`
- `analysis_reports`
- `leads`

Status:

- Legacy-Daten wurden serverintern nach `nurovelle_core.public` kopiert.
- Row-Counts stimmen zwischen `nurovell_potential_analysis.public` und `nurovelle_core.public` ueberein.

Verifizierte Counts:

| Tabelle | Rows |
|---|---:|
| `analysis_answers` | 336 |
| `analysis_reports` | 3 |
| `analysis_scores` | 6 |
| `analysis_sessions` | 8 |
| `companies` | 8 |
| `contacts` | 8 |
| `leads` | 3 |

### 5. Backend-Smoke gegen `nurovelle_core`

Nicht-schreibend:

- Fragen laden
- Health/Status, falls vorhanden

Status:

- DB-Lesezugriff gegen `nurovelle_core`: erfolgreich
- `analysis_sessions`: 8
- `leads`: 3
- `GET /api/v1/questions?industry=service...`: 200, 48 Fragen
- `GET /api/v1/questions?industry=manufacturing...`: 200, 50 Fragen
- `GET /api/v1/questions?industry=care...`: 200, 48 Fragen

Schreibend nur mit bewusstem Testdatensatz:

- Analyse starten
- Antworten speichern
- Score berechnen
- Report erzeugen
- Lead speichern

Status:

- offen

### 6. Umschaltentscheidung

Erst wenn alle Tests gruen sind:

- `DATABASE_URL` umstellen
- Backend neu starten
- Live-Smoke
- Rollback-Pfad bereithalten

## Akzeptanzkriterien vor Umschaltung

- Backup von `nurovell_potential_analysis` vorhanden. Status: erledigt.
- Restore-Test mindestens einmal durchgefuehrt. Status: offen.
- `nurovelle_core` enthaelt alle Tabellen, die das aktuelle Backend erwartet. Status: erledigt.
- Alembic-Version in `nurovelle_core` ist konsistent. Status: erledigt.
- Read-only Backend-Smoke gegen `nurovelle_core` erfolgreich. Status: erledigt.
- Schreibender E2E mit Testdatensatz erfolgreich. Status: offen.
- Rollback auf alte `DATABASE_URL` dokumentiert
- keine Secrets in Repo oder Chat dokumentiert

## Offene Entscheidung

Soll `nurovelle_core` kurzfristig Legacy-Tabellen im `public` Schema enthalten?

Empfehlung:

Ja, als Uebergangsloesung.

Status:

Diese Entscheidung wurde fuer den MVP-Uebergang umgesetzt. Die saubere fachliche Schema-Migration bleibt danach separat.
