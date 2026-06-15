# Backend Postgres Runtime Assessment

Stand: 2026-06-15

## Zweck

Dieses Dokument haelt fest, welche Postgres-Instanz der Live-Backend-Container aktuell verwendet und was fuer die spaetere Umstellung auf `nurovelle_core` zu beachten ist.

## Aktueller Runtime-Stand

Der Live-Backend-Container `nurovell_backend` liest seine Datenbankverbindung aus `DATABASE_URL`.

Redacted Runtime-Ergebnis vor Cutover:

```text
DATABASE_URL:
  scheme=postgresql
  host=postgres
  port=5432
  db=nurovell_potential_analysis
  user=nurovell_potential_user
```

Redacted Runtime-Ergebnis nach Cutover am 2026-06-15:

```text
DATABASE_URL:
  scheme=postgresql
  host=postgres
  port=5432
  db=nurovelle_core
  user=nurovell_potential_user
```

`host=postgres` meint im Docker-Netzwerk den Container `postgres`.

Der Backend-Container und der Postgres-Container teilen das Docker-Netzwerk:

```text
avatar-generator_internal
```

## Vorhandene Datenbanken im Runtime-Postgres

Im Container `postgres` existieren:

```text
avatargenerator
nurovell_potential_analysis
nurovelle_core
postgres
template0
template1
```

## Umgesetzter Core-Stand

`nurovelle_core` wurde im Runtime-Postgres-Container angelegt und mit der Migration initialisiert:

```text
database/migrations/001_nurovelle_core_init.sql
```

Verifizierte Tabellen:

```text
analysis.answers
analysis.results
analysis.submissions
homepage.lead_events
homepage.leads
ops.audit_events
ops.integration_errors
```

Verifizierte Rollen:

```text
nurovelle_backend_user
nurovelle_migration_user
nurovelle_readonly_user
```

Zusaetzlich wurde `nurovelle_core` legacy-kompatibel fuer das aktuelle Backend vorbereitet:

- Alembic-Migrationen des Backends gegen `nurovelle_core` ausgefuehrt
- Legacy-Tabellen im `public` Schema angelegt
- Alembic-Version `2026060801` verifiziert
- Daten aus `nurovell_potential_analysis.public` nach `nurovelle_core.public` kopiert
- Read-only Backend-Smoke gegen `nurovelle_core` erfolgreich
- Schreibender Backend-E2E gegen `nurovelle_core` erfolgreich und Testdatensatz bereinigt

## Wichtige Einschraenkung

Das Backend wurde nicht blind umgestellt, sondern nach Backup, Restore-Test, Tabellenabgleich, Preflight und schreibendem E2E auf `nurovelle_core` umgeschaltet.

Grund:

Die aktuellen SQLAlchemy-Models verwenden bestehende Tabellen ohne Schema-Praefix, zum Beispiel:

```text
analysis_sessions
analysis_answers
analysis_scores
analysis_reports
companies
contacts
leads
events
notion_sync_jobs
newsletter_campaigns
admin_users
```

Die vorbereitete `nurovelle_core`-Struktur nutzt dagegen fachliche Schemas:

```text
analysis.*
homepage.*
ops.*
content_system.*
```

Die Live-Aenderung von `DATABASE_URL` ist erfolgt. Restore-Test, schreibender E2E gegen `nurovelle_core`, finaler Live-Smoke und Rollback-Sicherung sind erfolgreich dokumentiert.

## Empfohlener Migrationspfad

### Option A: Legacy-Models in `nurovelle_core` spiegeln

Vorteil:

- geringster Code-Eingriff
- Backend kann schneller auf `nurovelle_core` zeigen

Nachteil:

- `nurovelle_core` enthaelt dann zusaetzlich Legacy-Tabellen im `public` Schema
- fachliche Trennung ist weniger sauber

### Option B: Backend-Models auf Schemas migrieren

Vorteil:

- sauberere Zielarchitektur
- `analysis`, `homepage`, `ops` werden echte technische Grenzen

Nachteil:

- mehr Code- und Migrationstest notwendig
- Risiko fuer bestehende Live-Endpunkte hoeher

### Empfohlene MVP-Entscheidung

Kurzfristig:

1. Bestehende Backend-Tabellenstruktur aus `nurovell_potential_analysis` exportieren.
2. Dieselbe Struktur in `nurovelle_core` unter `public` oder bewusst gemappten Schemas testweise aufbauen.
3. Backend gegen `nurovelle_core` in einer Staging-/Test-Session starten.
4. Erst nach erfolgreichem Live-E2E umschalten.

Mittelfristig:

- Backend-Models schrittweise auf fachliche Schemas migrieren.
- Neue Homepage-/Analyse-/Ops-Daten nicht mehr in unstrukturierte Legacy-Tabellen streuen.

## Nicht tun

- `DATABASE_URL` im Live-Backend nicht direkt auf `nurovelle_core` aendern, ohne Tabellenkompatibilitaet zu pruefen.
- Bestehende Datenbank `nurovell_potential_analysis` nicht loeschen.
- Keine Passwoerter oder Secrets in Projektdateien speichern.

## Naechster Schritt

Der konkrete Kompatibilitaets- und Migrationsplan liegt in:

```text
project_files/backend_db_compatibility_plan.md
```

Schema-Export der bestehenden Backend-DB ohne Daten:

```bash
pg_dump --schema-only nurovell_potential_analysis
```

Naechste technische Entscheidung nach Cutover:

- Legacy-kompatiblen Betrieb in `nurovelle_core.public` stabil beobachten.
- Spaeter saubere Model-Migration auf `analysis.*`, `homepage.*`, `ops.*` planen.
