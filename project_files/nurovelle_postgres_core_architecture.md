# Nurovelle Postgres Core Architecture

Stand: 2026-06-13

## Ziel

Nurovelle soll nicht fuer jeden Workflow eine eigene Postgres-Instanz oder eigene Datenbank bekommen.

Zielbild:

```text
eine zentrale Postgres-Instanz
eine zentrale Datenbank: nurovelle_core
getrennte Schemas pro Systembereich
klare Rollen fuer Backend, n8n und spaetere Services
```

Dadurch bleiben Daten wiederverwendbar, Backups einfacher und n8n kann als Workflow-Orchestrator systemuebergreifend arbeiten.

## Grundregel

Die Datenbank ist zentrale technische Persistenz.

Die statische Homepage verbindet sich nicht direkt mit Postgres.

```text
Homepage
  -> Backend API
  -> Postgres nurovelle_core

n8n
  -> Postgres nurovelle_core
  -> Notion / E-Mail / Follow-up / interne Workflows
```

## Empfohlene Datenbank

```sql
create database nurovelle_core;
```

## Empfohlene Schemas

```sql
create schema if not exists homepage;
create schema if not exists analysis;
create schema if not exists n8n_memory;
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

### `n8n_memory`

Zweck:

- Workflow-Memory
- Follow-up-State
- Retry-State
- n8n-Ausfuehrungsbezug zu Leads, Analysen, Content und Syncs

Typische Tabellen:

- `n8n_memory.workflow_memory`
- `n8n_memory.workflow_runs`
- `n8n_memory.workflow_events`

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

## n8n Memory Tabellen

### `n8n_memory.workflow_memory`

Generischer Memory-Key-Value-Speicher fuer n8n.

```sql
create table if not exists n8n_memory.workflow_memory (
  memory_id uuid primary key default gen_random_uuid(),
  entity_type text not null,
  entity_id text not null,
  memory_key text not null,
  memory_value jsonb not null,
  source text not null default 'n8n',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (entity_type, entity_id, memory_key)
);
```

Beispiel:

```json
{
  "entity_type": "lead",
  "entity_id": "lead_uuid",
  "memory_key": "followup_state",
  "memory_value": {
    "step": "email_1_sent",
    "last_contacted_at": "2026-06-13T10:00:00+02:00",
    "next_action": "wait_3_days"
  }
}
```

### `n8n_memory.workflow_runs`

Speichert konkrete n8n-Ausfuehrungen pro Workflow.

```sql
create table if not exists n8n_memory.workflow_runs (
  run_id uuid primary key default gen_random_uuid(),
  workflow_name text not null,
  workflow_key text not null,
  n8n_execution_id text,
  status text not null default 'started',
  entity_type text,
  entity_id text,
  started_at timestamptz not null default now(),
  finished_at timestamptz,
  error_message text,
  payload jsonb
);
```

### `n8n_memory.workflow_events`

Audit-Log fuer einzelne Schritte innerhalb eines Workflows.

```sql
create table if not exists n8n_memory.workflow_events (
  event_id bigserial primary key,
  run_id uuid references n8n_memory.workflow_runs(run_id) on delete set null,
  workflow_key text not null,
  event_type text not null,
  event_status text not null,
  entity_type text,
  entity_id text,
  payload jsonb,
  error_message text,
  created_at timestamptz not null default now()
);
```

## Rollenmodell

Keine Workflows sollen als Postgres-Superuser arbeiten.

Empfohlene Rollen:

```text
nurovelle_backend_user
nurovelle_n8n_user
nurovelle_readonly_user
nurovelle_migration_user
```

### `nurovelle_backend_user`

Darf:

- in `homepage` schreiben
- in `analysis` schreiben
- begrenzt in `ops` schreiben

Darf nicht:

- n8n-Memory direkt manipulieren, ausser es gibt einen bewussten Backend-Use-Case
- Datenbankstruktur migrieren

### `nurovelle_n8n_user`

Darf:

- in `n8n_memory` lesen/schreiben
- relevante `analysis`- und `homepage`-Daten lesen
- Follow-up-Status in dafuer vorgesehenen Feldern aktualisieren
- Events in `ops` schreiben

Darf nicht:

- Tabellen droppen
- Schemas veraendern
- Rohdaten loeschen
- als Superuser laufen

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

Soll:

- nicht fuer Runtime-Workflows genutzt werden

## Rechte-Grundlage

Beispiel:

```sql
grant usage on schema homepage, analysis, n8n_memory, ops to nurovelle_n8n_user;
grant select on all tables in schema homepage, analysis to nurovelle_n8n_user;
grant select, insert, update on all tables in schema n8n_memory to nurovelle_n8n_user;
grant insert on all tables in schema ops to nurovelle_n8n_user;
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

Neue Workflows bekommen zuerst:

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

- n8n nicht fuer jeden Workflow eine eigene Datenbank erzeugt
- Runtime-User keine Superuser-Rechte haben
- Homepage nicht direkt mit Postgres spricht
- Analyse- und Lead-Daten ueber Backend-API gespeichert werden
- n8n-Memory in `n8n_memory` liegt
- Content-System-Daten spaeter in `content_system` statt in einer separaten Datenbank landen
- Backups fuer `nurovelle_core` definiert sind

