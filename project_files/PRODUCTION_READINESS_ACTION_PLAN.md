# Production Readiness Action Plan

Stand: 2026-06-15

## Zweck

Dieses Dokument uebersetzt `PRODUCTION_READINESS_AUDIT.md` in eine konkrete Abarbeitungsreihenfolge.

Grundsatz:

Neue Features wie Sales Agent, Proposal Agent oder Customer Success Agent werden erst begonnen, wenn die bestehenden Gelb-Module stabiler sind.

## Reihenfolge

| Prioritaet | Modul | Ziel | Ergebnis |
|---:|---|---|---|
| 1 | Homepage | sichtbare Einstiegsstrecke stabilisieren | Homepage Launch-Check bestanden |
| 2 | Potenzialanalyse | Analyseflow fachlich und technisch absichern | Live-E2E mit Branchen-/Edge-Case-Abdeckung |
| 3 | Postgres Core | zentralen Schreibpfad klaeren | Backend schreibt live in `nurovelle_core`; Legacy-Schema-Migration bleibt spaeterer Schritt |
| 4 | Notion Integration | lokale Mappings in echten Sync ueberfuehren | Notion-Seiten werden reproduzierbar erstellt/aktualisiert |
| 5 | Multi-Processor / Atomizer | Qualitaet messbar machen | Atomizer Evaluation und Fehlerlogging |
| 6 | Repurposing / Approval | Drafts freigabefaehig machen | Approval-Gate vor Nutzung |
| 7 | Neue Output-Formate | Mini Guide, Lead Magnet, Podcast, Video Script | erst nach stabilen Gates |

## Phase 1: Homepage Readiness

Ziel:

Die Homepage darf keine offensichtlichen Produktionsrisiken mehr haben.

Tasks:

- [x] Desktop-Ansicht `homepage/index.html` pruefen
- [x] Mobile-Ansicht `homepage/index.html` pruefen
- [x] Desktop-Ansicht `homepage/analyse.html` pruefen
- [x] Mobile-Ansicht `homepage/analyse.html` pruefen
- [x] Lokale Link- und Asset-Pruefung fuer `homepage/index.html` und `homepage/analyse.html`
- [x] Reproduzierbaren nicht-schreibenden Check `tools/check_homepage_readiness.py` anlegen
- [x] `tools/check_homepage_readiness.py` erfolgreich ausfuehren
- [ ] Alle CTAs pruefen
- [x] Impressum-Link pruefen
- [x] Datenschutz-Link pruefen
- [x] Fehlerverhalten bei API-Ausfall technisch absichern
- [x] API-Timeout fuer Analyse-Backend setzen
- [x] Formularvalidierung fuer Pflichtfelder technisch pruefen
- [x] Newsletter-Opt-in nur bei aktiv gesetzter Checkbox senden
- [x] Guardrail: keine direkte DB-/Secret-Bezuege im Homepage-Frontend
- [x] Spam-Schutz-Entscheidung dokumentieren
- [x] Tracking-/Consent-Entscheidung dokumentieren
- [ ] Mobile Ladezeit pruefen
- [ ] OpenGraph-Bild final setzen und testen

Done:

- keine blockierenden visuellen Fehler
- keine toten Hauptlinks
- Formular zeigt bei Fehlern klare Meldungen
- Datenschutz-/Impressum-Pfade erreichbar
- keine direkte DB-Verbindung aus dem Frontend
- Spam-Schutz ist als Honeypot dokumentiert
- Tracking/Consent ist als "keine aktiven Analyse-/Marketing-Cookies" dokumentiert
- Homepage ist visuell fuer Desktop und Mobile abgenommen

## Phase 2: Potenzialanalyse Readiness

Ziel:

Der Analyseflow muss fuer echte Leads belastbar sein.

Tasks:

- [x] Fragen fuer `service` laden
- [x] Fragen fuer `manufacturing` laden
- [x] Fragen fuer `care` laden
- [x] Branchenmapping gegen finale Branchenliste pruefen
- [x] Nicht-schreibende Live-GET-Pruefung fuer API-Fragenzweige in `tools/check_homepage_readiness.py`
- [x] Live-E2E mit gueltigen Formularwerten pruefen
- [x] Pflichtfeldfehler pruefen
- [x] API-Timeout im Frontend implementieren
- [x] doppelte E-Mail/Lead-Situation pruefen
- [x] Score-Payload fachlich validieren
- [x] Report-URL pruefen
- [x] Ergebnislink `/results/<analysis_id>` pruefen
- [x] `/lead` Call nach Reporterzeugung pruefen
- [x] Fehlerlogs fuer gescheiterte Analyse/Lead-Speicherung pruefen

Done:

- alle aktiven Branchen erzeugen einen gueltigen API-Industry-Wert
- Analyse kann erfolgreich abgeschlossen werden
- Fehler brechen nicht still ab
- Lead-Speicherung ist nachvollziehbar
- Pflichtfelder werden mit 400/VALIDATION_ERROR abgewiesen
- doppelte `/lead`-Submits erzeugen aktuell separate Leads, also kein automatisches Dedupe
- Ergebnis-URL `https://nurovelle.de/results/<analysis_id>` liefert 200
- Backend-Logs zeigen bei Pflichtfeldfehlern keine unkontrollierten 500er mehr

## Phase 3: Postgres Core Readiness

Ziel:

Neue Analyse- und Lead-Daten sollen kontrolliert in der zentralen Datenbank landen.

Tasks:

- [x] `nurovelle_core` auf VPS angelegt
- [x] Initialmigration ausgefuehrt
- [x] Tabellen und Rollen verifiziert
- [x] `nurovelle_core` im Runtime-Postgres-Container angelegt
- [x] Initialmigration im Runtime-Postgres-Container ausgefuehrt
- [x] Runtime-DB-Assessment dokumentiert
- [x] Backup von `nurovell_potential_analysis` erstellen
- [x] Backup mit `pg_restore --list` pruefen
- [x] Runtime-Passwoerter serverseitig final pruefen ohne Secrets zu dokumentieren
- [x] Backend-Konfiguration auf `nurovelle_core` vorbereitet und isoliert getestet
- [x] Tabellenkompatibilitaet zwischen bestehenden SQLAlchemy-Models und `nurovelle_core` klaeren
- [x] `project_files/backend_db_compatibility_plan.md` erstellen
- [x] Entscheidung treffen: Legacy-Tabellen temporaer in `nurovelle_core.public` nutzen
- [x] Alembic-Migrationen gegen isolierte Testdatenbank pruefen
- [x] Alembic-Migrationen gegen `nurovelle_core` ausfuehren
- [x] Legacy-Daten nach `nurovelle_core.public` kopieren
- [x] Read-only Backend-Smoke gegen `nurovelle_core` ausfuehren
- [x] Restore-Test durchfuehren
- [x] Schreibenden Backend-E2E mit markiertem Testdatensatz gegen `nurovelle_core` ausfuehren
- [x] Markierten Backend-E2E-Testdatensatz aus `nurovelle_core` bereinigen
- [x] Rollback-Pfad fuer `DATABASE_URL`-Umschaltung dokumentieren
- [x] `project_files/backend_database_cutover_plan.md` erstellen
- [x] Runtime-Umschaltung auf `nurovelle_core` ausfuehren
- [x] Post-Cutover-Preflight gegen `nurovelle_core` ausfuehren
- [x] Schreibenden Live-E2E nach Cutover ausfuehren
- [x] Markierten Live-E2E-Testdatensatz nach Cutover bereinigen
- [x] Wartungs-/Deploy-Fenster fuer Runtime-Umschaltung festlegen
- [ ] Schreibpfad fuer `analysis.submissions` testen
- [ ] Schreibpfad fuer `analysis.answers` testen
- [ ] Schreibpfad fuer `analysis.results` testen
- [ ] Schreibpfad fuer `homepage.leads` testen
- [ ] Schreibpfad fuer `homepage.lead_events` testen
- [x] Backup-Befehl dokumentieren
- [x] Restore-Test mit Testdump durchfuehren
- [x] bestehende DB `nurovell_potential_analysis` auf Migrationsbedarf pruefen

Done:

- Backend schreibt live in `nurovelle_core.public`; alte Datenbank bleibt als Rollback-Quelle erhalten
- Runtime-User sind keine Superuser
- Backup und Restore sind einmal geprueft

## Phase 4: Notion Sync Readiness

Ziel:

Notion wird von lokaler Mapping-Vorbereitung zu echter Arbeitsoberflaeche.

Tasks:

- [ ] Ziel-Datenbanken in Notion final definieren
- [ ] Property-Mapping dokumentieren
- [ ] Notion Secret serverseitig setzen
- [ ] Create-Page fuer Lead/Analyse testen
- [ ] Update-Page fuer Status testen
- [ ] Relation zu Analyse/Content testen
- [ ] Failed-Sync speichern
- [ ] Retry-Verhalten testen
- [ ] Rate-Limit-Fehler behandeln
- [ ] Konfliktfall lokal vs. Notion dokumentieren

Done:

- Notion Page IDs werden gespeichert
- Failed Syncs sind nachvollziehbar
- ein Retry kann ohne Datenverlust laufen

## Phase 5: Atomizer Readiness

Ziel:

Der Atomizer wird messbar statt nur funktional.

Tasks:

- [ ] Goldstandard-Fixture mit manuell erwarteten Atoms erstellen
- [ ] Evaluation-Script fuer Precision/Recall-nahe Metriken erstellen
- [ ] Mindestqualitaet pro Atomtyp definieren
- [ ] leere/zu kurze Atom-Batches als Fehler loggen
- [ ] source_reference-Abdeckung messen
- [ ] Dedupe-Ergebnis in Metriken aufnehmen
- [ ] echte Master Assets testen: Whitepaper, Checkliste, Mini Guide, Executive Briefing
- [ ] Persona-/Industry-Klassifikation verbessern
- [ ] Modell-/Promptpfad fuer semantische Extraktion planen

Done:

- Atomizer-Qualitaet ist reproduzierbar messbar
- schlechte Batches fallen sichtbar auf
- Source References sind fuer Review ausreichend

## Phase 6: Repurposing und Approval Readiness

Ziel:

Drafts duerfen nicht ohne Review in Nutzung oder Versand gehen.

Tasks:

- [ ] Qualitaetskriterien fuer Newsletter definieren
- [ ] Qualitaetskriterien fuer LinkedIn Posts definieren
- [ ] Qualitaetskriterien fuer Karussells definieren
- [ ] Approval Request fuer jedes Artifact erzeugen
- [ ] Approved/Rejected/Archived Statusuebergaenge testen
- [ ] Notion-Review-Status mit lokaler Wahrheit abgleichen
- [ ] Versandjobs nur fuer approved Artifacts erlauben
- [ ] Fehlerfall: Artifact ohne Source Atoms blockieren

Done:

- kein Draft wird direkt Versandjob
- jedes Artifact hat Source Atoms
- Approval-Entscheidungen sind nachvollziehbar gespeichert

## Blockierte neue Features

Diese Features bleiben blockiert, bis Phase 1 bis 6 mindestens jeweils ein akzeptierter Smoke-/Readiness-Nachweis haben:

- Sales Agent
- Proposal Agent
- Customer Success Agent

Neue Output-Formate werden erst nach Phase 6 gebaut:

- Mini Guide
- Lead Magnet
- Podcast Script
- Video Script

## Naechster kleinster Schritt

Als naechstes wird Phase 1 gestartet:

1. Homepage lokal und live visuell pruefen.
2. API-Fehlerverhalten in `homepage/analyse.html` pruefen.
3. Formularvalidierung und CTA-Verhalten pruefen.
4. Ergebnisse in `launch_todo.md` abhaken oder als konkrete Fixes erfassen.
