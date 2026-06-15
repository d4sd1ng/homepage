# Nurovelle Postgres Core Architecture

Stand: 2026-06-15

## Ziel

Nurovelle soll nicht fuer jeden Workflow eine eigene Postgres-Instanz oder eigene Datenbank bekommen.

Zielbild:

```text
eine zentrale Postgres-Instanz
eine zentrale Datenbank: nurovelle_core
getrennte Schemas pro Systembereich
klare Rollen fuer Backend, Auswertung und spaetere Services
```

Dadurch bleiben Daten wiederverwendbar, Backups einfacher und neue Systembereiche erzeugen nicht jeweils eigene Datenbanken.

## Grundregel

Die Datenbank ist zentrale technische Persistenz.

Die statische Homepage verbindet sich nicht direkt mit Postgres.

```text
Homepage
  -> Backend API
  -> Postgres nurovelle_core
```

## Empfohlene Datenbank

```sql
create database nurovelle_core;
```

Die ausfuehrbare Initialisierung liegt in:

```text
database/migrations/001_nurovelle_core_init.sql
```

Hinweis:

Die SQL-Datei enthaelt keine Passwoerter. Runtime-Zugangsdaten werden auf dem Server gesetzt und nicht im Repository gespeichert.

## Empfohlene Schemas

```sql
create schema if not exists homepage;
create schema if not exists analysis;
create schema if not exists content_system;
create schema if not exists ops;
```

## Schema-Zuständigkeiten

### `homepage`

Zweck:

- Formular-Submissions
- kompakte Lead-Daten aus Website-Flows
- technische Herkunft von Website-Events

Typische Tabellen:

- `homepage.form_submissions`
- `homepage.website_events`

### `analysis`

Zweck:

- Potenzialanalyse
- Fragen
- Antworten
- Scores
- Reports
- Ergebnislinks

Typische Tabellen:

- `analysis.submissions`
- `analysis.answers`
- `analysis.results`
- `analysis.report_snapshots`

Der konkrete Datenvertrag fuer `homepage/analyse.html` liegt in:

```text
project_files/homepage_postgres_data_contract.md
```

### `content_system`

Zweck:

- Content Atoms
- Content Artifacts
- Notion-Mappings
- Approval-Status
- Scheduling-Daten

Hinweis:

Im Multi-Processor-Projekt ist aktuell lokale JSON-Speicherung technische Wahrheit. Wenn dieser Bereich spaeter nach Postgres wandert, soll er in dieses Schema und nicht in eine separate Datenbank.

### `ops`

Zweck:

- technische Logs
- Sync-Fehler
- Queue-/Job-Status
- Integrationsstatus
- Audit-Events

Typische Tabellen:

- `ops.integration_errors`
- `ops.sync_jobs`
- `ops.audit_events`

## Rollenmodell

Keine Runtime-Prozesse sollen als Postgres-Superuser arbeiten.

Empfohlene Rollen:

```text
nurovelle_backend_user
nurovelle_readonly_user
nurovelle_migration_user
```

### `nurovelle_backend_user`

Darf:

- in `homepage` schreiben
- in `analysis` schreiben
- begrenzt in `ops` schreiben

Darf nicht:

- Datenbankstruktur migrieren

### `nurovelle_readonly_user`

Darf:

- fuer Dashboards und manuelle Auswertung lesen

Darf nicht:

- schreiben
- loeschen
- Migrationsbefehle ausfuehren

### `nurovelle_migration_user`

Darf:

- Migrationen ausfuehren
- Schemas und Tabellen veraendern
- bestehende Tabellen, Sequenzen und Ops-Funktionen fuer Migrationen verwalten

Soll:

- nicht fuer Runtime-Workflows genutzt werden

## Rechte-Grundlage

Beispiel:

```sql
grant usage on schema homepage, analysis, ops to nurovelle_backend_user;
grant select, insert, update on all tables in schema homepage, analysis to nurovelle_backend_user;
grant insert on all tables in schema ops to nurovelle_backend_user;

grant usage on schema homepage, analysis, content_system, ops to nurovelle_readonly_user;
grant select on all tables in schema homepage, analysis, content_system, ops to nurovelle_readonly_user;
```

Finale Grants muessen nach den echten Tabellennamen gesetzt werden.

## Backup-Strategie

MVP:

- taegliches DB-Dump-Backup
- mindestens 7 Tage Aufbewahrung
- manuelles Backup vor Schema-Migrationen

Spaeter:

- taegliche Backups
- woechentliche Archivbackups
- Restore-Test mindestens monatlich

Empfohlener Dump:

```text
nurovelle_core_backup_YYYYMMDD_HHMMSS.dump
```

## Keine 20 Postgres-Regel

Neue Systembereiche bekommen zuerst:

1. ein vorhandenes Schema, wenn fachlich passend
2. ein neues Schema innerhalb `nurovelle_core`, wenn wirklich noetig
3. nur in Ausnahmefaellen eine eigene Datenbank
4. keine eigene Postgres-Instanz ohne bewusste Architekturentscheidung

## Wann eine eigene Datenbank erlaubt ist

Nur wenn mindestens einer dieser Gruende zutrifft:

- harte Mandantentrennung
- komplett anderer Backup-/Retention-Zyklus
- sehr hohe Last mit eigenem Tuningbedarf
- regulatorische Trennung
- externer Dienst verlangt eigene Datenbank

Auch dann bleibt eine eigene Instanz die Ausnahme.

## Akzeptanzkriterien

Die Postgres-Core-Architektur gilt als eingehalten, wenn:

- `database/migrations/001_nurovelle_core_init.sql` fuer `nurovelle_core` vorhanden ist
- Runtime-User keine Superuser-Rechte haben
- Homepage nicht direkt mit Postgres spricht
- Analyse- und Lead-Daten ueber Backend-API gespeichert werden
- Content-System-Daten spaeter in `content_system` statt in einer separaten Datenbank landen
- Backups fuer `nurovelle_core` definiert sind
