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
| 3 | Postgres Core | zentralen Schreibpfad klaeren | Backend schreibt kontrolliert in `nurovelle_core` |
| 4 | Notion Integration | lokale Mappings in echten Sync ueberfuehren | Notion-Seiten werden reproduzierbar erstellt/aktualisiert |
| 5 | Multi-Processor / Atomizer | Qualitaet messbar machen | Atomizer Evaluation und Fehlerlogging |
| 6 | Repurposing / Approval | Drafts freigabefaehig machen | Approval-Gate vor Nutzung |
| 7 | Neue Output-Formate | Mini Guide, Lead Magnet, Podcast, Video Script | erst nach stabilen Gates |

## Phase 1: Homepage Readiness

Ziel:

Die Homepage darf keine offensichtlichen Produktionsrisiken mehr haben.

Tasks:

- [ ] Desktop-Ansicht `homepage/index.html` pruefen
- [ ] Mobile-Ansicht `homepage/index.html` pruefen
- [ ] Desktop-Ansicht `homepage/analyse.html` pruefen
- [ ] Mobile-Ansicht `homepage/analyse.html` pruefen
- [x] Lokale Link- und Asset-Pruefung fuer `homepage/index.html` und `homepage/analyse.html`
- [x] Reproduzierbaren nicht-schreibenden Check `tools/check_homepage_readiness.py` anlegen
- [x] `tools/check_homepage_readiness.py` erfolgreich ausfuehren
- [ ] Alle CTAs pruefen
- [x] Impressum-Link pruefen
- [x] Datenschutz-Link pruefen
- [ ] Fehlerverhalten bei API-Ausfall pruefen
- [ ] Formularvalidierung fuer Pflichtfelder pruefen
- [ ] Newsletter-Opt-in nur bei aktiv gesetzter Checkbox senden
- [ ] Spam-Schutz-Entscheidung dokumentieren
- [ ] Tracking-/Consent-Entscheidung dokumentieren
- [ ] Mobile Ladezeit pruefen
- [ ] OpenGraph-Bild final setzen und testen

Done:

- keine blockierenden visuellen Fehler
- keine toten Hauptlinks
- Formular zeigt bei Fehlern klare Meldungen
- Datenschutz-/Impressum-Pfade erreichbar
- keine direkte DB-Verbindung aus dem Frontend

## Phase 2: Potenzialanalyse Readiness

Ziel:

Der Analyseflow muss fuer echte Leads belastbar sein.

Tasks:

- [x] Fragen fuer `service` laden
- [x] Fragen fuer `manufacturing` laden
- [x] Fragen fuer `care` laden
- [x] Branchenmapping gegen finale Branchenliste pruefen
- [x] Nicht-schreibende Live-GET-Pruefung fuer API-Fragenzweige in `tools/check_homepage_readiness.py`
- [ ] Live-E2E mit gueltigen Formularwerten pruefen
- [ ] Pflichtfeldfehler pruefen
- [ ] API-Timeout simulieren oder manuell ausloesen
- [ ] doppelte E-Mail/Lead-Situation pruefen
- [ ] Score-Payload fachlich validieren
- [ ] Report-URL pruefen
- [ ] Ergebnislink `/results/<analysis_id>` pruefen
- [ ] `/lead` Call nach Reporterzeugung pruefen
- [ ] Fehlerlogs fuer gescheiterte Analyse/Lead-Speicherung pruefen

Done:

- alle aktiven Branchen erzeugen einen gueltigen API-Industry-Wert
- Analyse kann erfolgreich abgeschlossen werden
- Fehler brechen nicht still ab
- Lead-Speicherung ist nachvollziehbar

## Phase 3: Postgres Core Readiness

Ziel:

Neue Analyse- und Lead-Daten sollen kontrolliert in der zentralen Datenbank landen.

Tasks:

- [x] `nurovelle_core` auf VPS angelegt
- [x] Initialmigration ausgefuehrt
- [x] Tabellen und Rollen verifiziert
- [ ] Runtime-Passwoerter serverseitig setzen
- [ ] Backend-Konfiguration auf `nurovelle_core` vorbereiten
- [ ] Schreibpfad fuer `analysis.submissions` testen
- [ ] Schreibpfad fuer `analysis.answers` testen
- [ ] Schreibpfad fuer `analysis.results` testen
- [ ] Schreibpfad fuer `homepage.leads` testen
- [ ] Schreibpfad fuer `homepage.lead_events` testen
- [ ] Backup-Befehl dokumentieren
- [ ] Restore-Test mit Testdump durchfuehren
- [ ] bestehende DB `nurovell_potential_analysis` auf Migrationsbedarf pruefen

Done:

- Backend schreibt nicht mehr unkontrolliert in getrennte Datenbanken
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
