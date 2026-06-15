# Changelog Project Files

## 2026-05-22

Aktualisiert:

- Domain auf nurovelle.de gesetzt.
- Finale Branchenliste eingetragen.
- Finale Service-Liste eingetragen.
- Alte Branchenbezüge entfernt.
- Alte Services verworfen.
- Services und Branchen getrennt dokumentiert.
- Asset-Pfade aktualisiert.
- sections_bg.png als finaler Section-Hintergrund dokumentiert.
- hero/hero_bg_cube_right_final.png als finaler Hero-Hintergrund dokumentiert.
- Card-Bilder bleiben textfrei.
- Card-Texte werden separat im HTML gesetzt.
- Keine freien Texte außerhalb der Project-Files.

## 2026-06-08

Aktualisiert:

- `homepage/analyse.html` an den produktiven Nurovelle-Analyse-Flow angebunden.
- Alte lokale Fake-Auswertung entfernt.
- Formular ruft jetzt die echte API unter `https://nurovelle.de/api/v1` auf.
- Flow: Fragen laden, Analyse starten, Antworten speichern, Scores berechnen, Report erzeugen.
- Ergebnislink zeigt auf `https://nurovelle.de/results/<analysis_id>`.
- `homepage/index.html` kann weiterhin per GET auf `analyse.html` weiterleiten; `analyse.html` übernimmt Query-Parameter als Vorbefüllung.
- Live-Smoke-Test gegen `nurovelle.de` erfolgreich.
- Lead-/Follow-up-Call ergänzt: `POST /api/v1/lead`.
- Newsletter-/Nurturing-Opt-in als separate Checkbox ergänzt.
- Lead-Message enthält Analyse-ID und Ergebnislink für Notion/CRM-Nachbearbeitung.

## 2026-06-08 SEO-/Download-Erweiterung

Aktualisiert:

- `homepage/index.html` um SEO-Tool-Sektion erweitert.
- SEO-Inhalte aus `Landing_pages/` abgeleitet.
- SEO-Karten mit stabilen IDs und `data-landing-source` versehen.
- Download-Bereich namentlich vorbereitet.
- Keine unfertigen Dokumente aus `G:\Projects\Dokumente_lead` auf die Homepage kopiert.
- Download-Karten mit stabilen `data-download-key` Werten versehen.
- Meta Title und Meta Description der Startseite aktualisiert.
- OpenGraph-Basisdaten ergaenzt; finales OG-Bild bleibt offen.
- `project_files/seo_download_sections.md` als technische Notiz ergaenzt.
- `project_files/launch_todo.md` als Launch-Checkliste ergaenzt.

## 2026-06-08 VPS-Deploy

Aktualisiert:

- Homepage-Stand nach GitHub gepusht: `5f0904e`.
- Statische Homepage-Dateien auf den VPS uebertragen.
- VPS-Ablage: `/opt/homepage_repo`.
- Next-Frontend-Static-Ablage: `/opt/nurovell-potential-analysis/frontend/public/homepage`.
- `nurovell_frontend` neu gebaut und gestartet.
- Live-Pfade geprueft:
  - `https://nurovelle.de/homepage/index.html`
  - `https://nurovelle.de/homepage/analyse.html`
- Root-Route `/` wurde nicht umgestellt.
- Keine Public-SSH-Freigabe.
- Keine Firewall-, Tunnel- oder Netzwerk-Aenderungen.

## 2026-06-08 Root-Aktivierung

Aktualisiert:

- Root `https://nurovelle.de/` leitet jetzt auf `/homepage/index.html`.
- `https://nurovelle.de/homepage/index.html` live mit HTTP 200 geprueft.
- `https://nurovelle.de/homepage/analyse.html` live mit HTTP 200 geprueft.
- `https://nurovelle.de/assets/hero/nurovelle_logo.png` live mit HTTP 200 geprueft.
- `https://nurovelle.de/results/<analysis_id>` bleibt erreichbar.
- Aenderung erfolgte nur im Frontend-Container.
- Keine Public-SSH-Freigabe.
- Keine Firewall-, Tunnel- oder Netzwerk-Aenderungen.

## 2026-06-13 Korrektur Analyse-Branchenliste

Aktualisiert:

- Fehlinterpretation korrigiert: `Immobilien & Facility Management` bleibt eine aktive Branche.
- Alte getrennte Labels `Verwaltung & HR` und `Marketing & Vertrieb` nicht fuer die aktuelle Analyse-Seite verwenden.
- `homepage/analyse.html`, `BRANCHEN_FINAL.md`, `task_contract.md` und `project_overview.md` auf die aktuelle Branchenliste synchronisiert.
- Aktuelle Analyse-Branchen: Energie & Versorgung; Finanzen & Versicherung; Industrie & Produktion; Verwaltung, Vertrieb, Einkauf & Marketing; Gesundheitswesen & Pflege; Immobilien & Facility Management; Bildung & Forschung; Dienstleistungen & KMU; Sonstiges.

## 2026-06-13 Postgres-Datenvertrag Analyse

Ergaenzt:

- `project_files/homepage_postgres_data_contract.md` beschreibt die Postgres-Daten fuer Analyse-Submissions, Antworten, Ergebnisse, Leads und Lead-Events.
- Festgelegt: Homepage sendet nur an die API; Postgres, Notion-Sync und Newsletter-/Nurturing-Prozesse bleiben Backend-Aufgabe.
- `project_files/nurovelle_postgres_core_architecture.md` definiert `nurovelle_core` als zentrale Postgres-Datenbank mit Schemas fuer Homepage, Analyse, Content-System und Ops.
- Analyse-Tabellen im Datenvertrag auf Schema-Namen `analysis.*` und `homepage.*` ausgerichtet.

## 2026-06-14 Postgres-Architektur ohne n8n

Aktualisiert:

- n8n als aktiven Integrationspfad aus der Postgres-Core-Architektur entfernt.
- Schema `n8n_memory`, n8n-Memory-Tabellen und Rolle `nurovelle_n8n_user` entfernt.
- Zentrale Postgres-Strategie bleibt bestehen: eine Datenbank `nurovelle_core`, getrennte Schemas fuer Homepage, Analyse, Content-System und Ops.
- Homepage bleibt weiterhin ohne direkte Postgres-Verbindung; Speicherung erfolgt ueber Backend/API.

## 2026-06-15 Postgres-Initialisierung

Ergaenzt:

- `database/migrations/001_nurovelle_core_init.sql` als ausfuehrbare Initialisierung fuer `nurovelle_core`.
- Schemas `homepage`, `analysis`, `content_system` und `ops` werden angelegt.
- Tabellen fuer Analyse-Submissions, Antworten, Ergebnisse, Leads, Lead-Events und Ops-Logs werden angelegt.
- Rollen `nurovelle_backend_user`, `nurovelle_readonly_user` und `nurovelle_migration_user` werden ohne Passwoerter vorbereitet.
- Projektdateien auf die SQL-Initialisierung verlinkt.
- SQL-Migration auf dem VPS mit `psql` transaktional geprueft: `BEGIN`, Migration, `ROLLBACK`; keine dauerhaften Datenbankobjekte angelegt.
- Aktuell existiert auf dem VPS noch keine Datenbank `nurovelle_core`; vorhandene relevante Datenbank ist `nurovell_potential_analysis`.

Umgesetzt:

- Datenbank `nurovelle_core` auf dem VPS angelegt.
- `database/migrations/001_nurovelle_core_init.sql` produktiv gegen `nurovelle_core` ausgefuehrt.
- Verifiziert: Tabellen in `analysis`, `homepage` und `ops` vorhanden.
- Verifiziert: Rollen `nurovelle_backend_user`, `nurovelle_readonly_user` und `nurovelle_migration_user` vorhanden.
- Keine Passwoerter im Repository gespeichert.

## 2026-06-15 Production Readiness Audit

Ergaenzt:

- `project_files/PRODUCTION_READINESS_AUDIT.md` als uebergeordnetes Readiness-Dokument im Homepage-Repo.
- Bewertet Homepage, Potenzialanalyse, Notion Integration, Postgres Core, Multi-Processor, Atomizer, Repurposing, Approval sowie spaetere Sales-/Proposal-/Customer-Success-Agenten.
- Festgelegt: Vor neuen Sales-/Proposal-/Customer-Success-Features muessen bestehende gelbe Module produktionsreifer gemacht werden.
