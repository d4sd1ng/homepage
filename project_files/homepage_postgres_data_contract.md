# Homepage Postgres Data Contract

Stand: 2026-06-15

## Zweck

Dieses Dokument definiert, welche Daten aus `homepage/analyse.html` im Backend in Postgres gespeichert werden sollen.

Wichtig:

- Die statische Homepage verbindet sich nicht direkt mit Postgres.
- Die Homepage sendet nur an `https://nurovelle.de/api/v1`.
- Speicherung, Notion-Sync und Newsletter-/Nurturing-Prozesse bleiben Backend-Aufgabe.
- Zentrale Datenbank- und Schema-Strategie siehe `project_files/nurovelle_postgres_core_architecture.md`.
- Ausfuehrbare Tabelleninitialisierung siehe `database/migrations/001_nurovelle_core_init.sql`.

## Frontend-Quelle

Formularfelder aus `homepage/analyse.html`:

- `vorname`
- `nachname`
- `email`
- `unternehmen`
- `branche`
- `mitarbeiteranzahl`
- `zeitaufwand`
- `datenlage`
- `herausforderung`
- `telefon`
- `website`
- `newsletter`

## API-Flow

```text
GET  /questions?industry=<industry>&tier=basic&include_risk=false
POST /analysis/start
POST /analysis/<analysis_id>/answers
POST /analysis/<analysis_id>/score
POST /analysis/<analysis_id>/report
POST /lead
```

## Branchenwerte

Sichtbare Werte:

```text
Energie & Versorgung
Finanzen & Versicherung
Industrie & Produktion
Verwaltung, Vertrieb, Einkauf & Marketing
Gesundheitswesen & Pflege
Immobilien & Facility Management
Bildung & Forschung
Dienstleistungen & KMU
Sonstiges
```

Aktuelles API-Mapping:

```text
Industrie & Produktion              -> manufacturing
Gesundheitswesen & Pflege           -> care
alle anderen aktuellen Branchen      -> service
```

## Empfohlene Tabellen

### `analysis.submissions`

Speichert den Start einer Potenzialanalyse.

```sql
create table if not exists analysis.submissions (
  analysis_id uuid primary key,
  source text not null default 'nurovelle_homepage_static',
  status text not null default 'started',

  company_name text not null,
  industry text not null,
  branch_label text not null,
  company_size text,
  website text,

  first_name text not null,
  last_name text not null,
  email text not null,
  phone text,

  weekly_time_spend text not null,
  data_state text not null,
  challenge text not null,

  result_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
```

### `analysis.answers`

Speichert die vom Frontend aus Formularangaben abgeleiteten Backend-Antworten.

```sql
create table if not exists analysis.answers (
  id bigserial primary key,
  analysis_id uuid not null references analysis.submissions(analysis_id) on delete cascade,
  question_id text not null,
  category text not null,
  answer text not null,
  created_at timestamptz not null default now(),
  unique (analysis_id, question_id)
);
```

### `analysis.results`

Speichert Score- und Reportstatus. Die konkreten Score-/Report-Strukturen bleiben flexibel als JSONB, weil sie aus dem Analyse-Backend kommen.

```sql
create table if not exists analysis.results (
  analysis_id uuid primary key references analysis.submissions(analysis_id) on delete cascade,
  score_status text not null default 'pending',
  report_status text not null default 'pending',
  score_payload jsonb,
  report_payload jsonb,
  report_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
```

### `homepage.leads`

Speichert Kontakt- und Follow-up-Daten nach erfolgreicher Reporterzeugung.

```sql
create table if not exists homepage.leads (
  lead_id uuid primary key,
  analysis_id uuid references analysis.submissions(analysis_id) on delete set null,

  name text not null,
  email text not null,
  phone text,
  company text,
  message text not null,
  newsletter boolean not null default false,

  source text not null default 'nurovelle_homepage_analysis',
  status text not null default 'new',
  notion_sync_status text not null default 'pending',
  email_sync_status text not null default 'pending',

  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
```

### `homepage.lead_events`

Optionaler Audit-Log fuer Notion, Newsletter und manuelle Nachbearbeitung.

```sql
create table if not exists homepage.lead_events (
  id bigserial primary key,
  lead_id uuid not null references homepage.leads(lead_id) on delete cascade,
  event_type text not null,
  event_status text not null,
  payload jsonb,
  error_message text,
  created_at timestamptz not null default now()
);
```

## Empfohlene Indizes

```sql
create index if not exists idx_analysis_submissions_email
  on analysis.submissions (email);

create index if not exists idx_analysis_submissions_created_at
  on analysis.submissions (created_at desc);

create index if not exists idx_analysis_submissions_industry
  on analysis.submissions (industry);

create index if not exists idx_leads_email
  on homepage.leads (email);

create index if not exists idx_leads_newsletter
  on homepage.leads (newsletter)
  where newsletter = true;

create index if not exists idx_leads_notion_sync_status
  on homepage.leads (notion_sync_status);

create index if not exists idx_lead_events_lead_id_created_at
  on homepage.lead_events (lead_id, created_at desc);
```

## Datenschutzregeln

- `newsletter=true` nur speichern, wenn die Checkbox aktiv gesetzt wurde.
- Keine direkte Notion- oder Resend-Verbindung aus der Homepage.
- Personenbezogene Daten nur im Backend speichern und nach definierter Frist loeschen oder anonymisieren.
- Analyse-Reports duerfen intern anonymisiert ausgewertet werden, aber Kontaktfelder muessen trennbar bleiben.

## Mindest-Payload aus der Homepage

### `/analysis/start`

```json
{
  "company": {
    "company_name": "Beispiel GmbH",
    "industry": "service",
    "company_size": "11_50",
    "website": "https://example.com"
  },
  "contact": {
    "first_name": "Max",
    "last_name": "Mustermann",
    "email": "max@example.com",
    "phone": "+49..."
  },
  "source": "nurovelle_homepage_static",
  "initial_context": {
    "branch_label": "Immobilien & Facility Management",
    "weekly_time_spend": "10–25 Stunden pro Woche",
    "data_state": "mehrere Quellen",
    "challenge": "..."
  }
}
```

### `/lead`

```json
{
  "name": "Max Mustermann",
  "email": "max@example.com",
  "phone": "+49...",
  "company": "Beispiel GmbH",
  "newsletter": true,
  "message": "Analyse-ID: ...\nErgebnis: https://nurovelle.de/results/...\n..."
}
```
