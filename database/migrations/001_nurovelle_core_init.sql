-- Nurovelle core Postgres initialization
-- Run this inside the nurovelle_core database.
-- Secrets/passwords are intentionally not stored in this repository.

create extension if not exists pgcrypto;

create schema if not exists homepage;
create schema if not exists analysis;
create schema if not exists content_system;
create schema if not exists ops;

do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'nurovelle_backend_user') then
    create role nurovelle_backend_user login;
  end if;

  if not exists (select 1 from pg_roles where rolname = 'nurovelle_readonly_user') then
    create role nurovelle_readonly_user login;
  end if;

  if not exists (select 1 from pg_roles where rolname = 'nurovelle_migration_user') then
    create role nurovelle_migration_user login;
  end if;
end
$$;

create or replace function ops.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

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

create table if not exists analysis.answers (
  id bigserial primary key,
  analysis_id uuid not null references analysis.submissions(analysis_id) on delete cascade,
  question_id text not null,
  category text not null,
  answer text not null,
  created_at timestamptz not null default now(),
  unique (analysis_id, question_id)
);

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

create table if not exists homepage.lead_events (
  id bigserial primary key,
  lead_id uuid not null references homepage.leads(lead_id) on delete cascade,
  event_type text not null,
  event_status text not null,
  payload jsonb,
  error_message text,
  created_at timestamptz not null default now()
);

create table if not exists ops.integration_errors (
  error_id uuid primary key default gen_random_uuid(),
  source_system text not null,
  target_system text,
  entity_type text,
  entity_id text,
  message text not null,
  retryable boolean not null default false,
  payload jsonb,
  created_at timestamptz not null default now()
);

create table if not exists ops.audit_events (
  event_id bigserial primary key,
  actor text not null default 'system',
  action text not null,
  entity_type text,
  entity_id text,
  payload jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_analysis_submissions_email
  on analysis.submissions (email);

create index if not exists idx_analysis_submissions_created_at
  on analysis.submissions (created_at desc);

create index if not exists idx_analysis_submissions_industry
  on analysis.submissions (industry);

create index if not exists idx_analysis_answers_analysis_id
  on analysis.answers (analysis_id);

create index if not exists idx_leads_email
  on homepage.leads (email);

create index if not exists idx_leads_newsletter
  on homepage.leads (newsletter)
  where newsletter = true;

create index if not exists idx_leads_notion_sync_status
  on homepage.leads (notion_sync_status);

create index if not exists idx_lead_events_lead_id_created_at
  on homepage.lead_events (lead_id, created_at desc);

create index if not exists idx_ops_integration_errors_created_at
  on ops.integration_errors (created_at desc);

create index if not exists idx_ops_audit_events_created_at
  on ops.audit_events (created_at desc);

drop trigger if exists trg_analysis_submissions_updated_at on analysis.submissions;
create trigger trg_analysis_submissions_updated_at
before update on analysis.submissions
for each row
execute function ops.set_updated_at();

drop trigger if exists trg_analysis_results_updated_at on analysis.results;
create trigger trg_analysis_results_updated_at
before update on analysis.results
for each row
execute function ops.set_updated_at();

drop trigger if exists trg_homepage_leads_updated_at on homepage.leads;
create trigger trg_homepage_leads_updated_at
before update on homepage.leads
for each row
execute function ops.set_updated_at();

grant usage on schema homepage, analysis, ops to nurovelle_backend_user;
grant select, insert, update on all tables in schema homepage, analysis to nurovelle_backend_user;
grant usage, select on all sequences in schema homepage, analysis to nurovelle_backend_user;
grant insert on all tables in schema ops to nurovelle_backend_user;
grant usage, select on all sequences in schema ops to nurovelle_backend_user;

grant usage on schema homepage, analysis, content_system, ops to nurovelle_readonly_user;
grant select on all tables in schema homepage, analysis, content_system, ops to nurovelle_readonly_user;

grant usage, create on schema homepage, analysis, content_system, ops to nurovelle_migration_user;
grant all privileges on all tables in schema homepage, analysis, content_system, ops to nurovelle_migration_user;
grant all privileges on all sequences in schema homepage, analysis, content_system, ops to nurovelle_migration_user;
grant all privileges on all functions in schema ops to nurovelle_migration_user;

alter default privileges in schema homepage grant select, insert, update on tables to nurovelle_backend_user;
alter default privileges in schema analysis grant select, insert, update on tables to nurovelle_backend_user;
alter default privileges in schema ops grant insert on tables to nurovelle_backend_user;
alter default privileges in schema homepage grant usage, select on sequences to nurovelle_backend_user;
alter default privileges in schema analysis grant usage, select on sequences to nurovelle_backend_user;
alter default privileges in schema ops grant usage, select on sequences to nurovelle_backend_user;

alter default privileges in schema homepage grant select on tables to nurovelle_readonly_user;
alter default privileges in schema analysis grant select on tables to nurovelle_readonly_user;
alter default privileges in schema content_system grant select on tables to nurovelle_readonly_user;
alter default privileges in schema ops grant select on tables to nurovelle_readonly_user;

alter default privileges in schema homepage grant all privileges on tables to nurovelle_migration_user;
alter default privileges in schema analysis grant all privileges on tables to nurovelle_migration_user;
alter default privileges in schema content_system grant all privileges on tables to nurovelle_migration_user;
alter default privileges in schema ops grant all privileges on tables to nurovelle_migration_user;
alter default privileges in schema homepage grant all privileges on sequences to nurovelle_migration_user;
alter default privileges in schema analysis grant all privileges on sequences to nurovelle_migration_user;
alter default privileges in schema content_system grant all privileges on sequences to nurovelle_migration_user;
alter default privileges in schema ops grant all privileges on sequences to nurovelle_migration_user;
