# Production Readiness Audit

Stand: 2026-06-15

## Ziel

Dieses Dokument bewertet den produktiven Reifegrad der Nurovelle-Gesamtstrecke.

Es ist bewusst uebergeordnet im Homepage-Repo abgelegt, weil die Homepage der sichtbare Einstieg in die Gesamtstrecke ist und die angrenzenden Systeme koordiniert:

```text
Homepage
  -> Potenzialanalyse API
  -> Postgres / Notion / Follow-up
  -> Multi-Processor
  -> Atomizer
  -> Repurposing
  -> Approval
  -> Sales / Proposal / Customer Success
```

## Status-Legende

```text
Gruen  = production ready oder kurz davor; Hauptpfade getestet, Betrieb kontrollierbar
Gelb   = MVP/teilweise bereit; funktional nutzbar, aber Produktionsrisiken offen
Rot    = nicht gebaut oder nicht einsatzbereit
```

## Gesamtbewertung

| Modul | Status | Kurzbewertung |
|---|---:|---|
| Homepage | Gelb | MVP vorhanden; Responsive, DSGVO, Monitoring, Spam-Schutz und Fehlerseiten muessen final geprueft werden |
| Potenzialanalyse | Gelb/Gruen | API-Flow angebunden und live smoke-getestet; Score-Validierung, Branchenzweige, PDF und Edge Cases brauchen noch Abnahme |
| Notion Integration | Gelb | Lokale Mapping-Strategie existiert; echte Notion-API-Synchronisation ist noch nicht production ready |
| Postgres Core | Gelb/Gruen | Zentrale DB `nurovelle_core` ist vorbereitet; Backend-Umschaltung und Betriebskonzept fehlen noch |
| Multi-Processor | Gelb | Viele Eingabetypen und E2E-Smokes vorhanden; Betrieb, Fehlerpfade, Monitoring und echte Summarizer-Konfiguration offen |
| Atomizer | Gelb | Funktionaler deterministischer MVP; noch nicht semantisch/modelgestuetzt |
| Repurposing Agent | Gelb | Newsletter, Sequenzen, LinkedIn, Karussell und Onepager als MVP; Contentqualitaet noch nicht final marketingreif |
| Newsletter | Gelb | Draft-Erzeugung vorhanden; Versand, Approval und Qualitaetsfreigabe fehlen |
| Approval Workflow | Gelb | Lokale Approval-Speicherung vorbereitet; echter Review-/Freigabeprozess fehlt |
| Sales Agent | Rot | Noch nicht gebaut |
| Proposal Agent | Rot | Noch nicht gebaut |
| Customer Success Agent | Rot | Noch nicht gebaut |

## Modul-Check

### Homepage

Status: Gelb

Vorhanden:

- statische Homepage
- Analyse-Einstieg
- Formularflow zur API
- Branchenliste korrigiert und synchronisiert
- keine direkte DB-Verbindung aus dem Browser

Offen:

- Responsive-Pruefung ueber wichtige Viewports
- Ladezeiten/Core Web Vitals
- Fehlerseiten
- DSGVO/Datenschutztexte und Consent-Logik
- Tracking-Entscheidung
- Formularvalidierung fuer alle Pflichtfelder
- Spam-Schutz
- Monitoring/Alerting fuer Formular- und API-Fehler

### Potenzialanalyse

Status: Gelb/Gruen

Vorhanden:

- `homepage/analyse.html` ruft `https://nurovelle.de/api/v1` auf
- Fragen laden
- Analyse starten
- Antworten speichern
- Score berechnen
- Report erzeugen
- Lead-Call nach Reporterzeugung

Offen:

- alle Fragen fachlich getestet
- alle Branchenzweige getestet
- Score-Modell validiert
- Edge Cases: leere/ungueltige Eingaben, doppelte Leads, API-Timeouts
- Abbruchverhalten
- PDF-/Report-Erzeugung final pruefen
- Fehlerszenarien nachvollziehbar loggen

### Notion Integration

Status: Gelb

Vorhanden:

- lokale Mapping-Dateien
- Failed-Sync-Struktur
- klare Regel: lokale technische Wahrheit, Notion als Arbeitsoberflaeche

Offen:

- echte Notion-API-Synchronisation
- Retry-Strategie
- Konflikterkennung
- Rate-Limit-Behandlung
- Mapping-Validierung gegen echte Notion Page IDs

### Postgres Core

Status: Gelb/Gruen

Vorhanden:

- zentrale Datenbankstrategie `nurovelle_core`
- Schemas fuer `homepage`, `analysis`, `content_system`, `ops`
- Initial-SQL fuer Tabellen und Rollen
- keine n8n-Abhaengigkeit

Offen:

- Backend schreibt noch nicht nachweislich in `nurovelle_core`
- Runtime-Passwoerter/Secrets muessen serverseitig gesetzt werden
- Backup-/Restore-Test
- Migration bestehender Analyse-/Lead-Daten klaeren
- Monitoring fuer DB-Verbindungen und Fehler

### Multi-Processor

Status: Gelb

Vorhanden:

- Multi-Input-Verarbeitung fuer Text, PDF, DOCX, Tabellen, Bild/OCR, Audio/Video-Pfade
- Processed-Source-Speicherung
- E2E-Smokes
- Summary-Workflow mit echtem Summarizer als Voraussetzung

Offen:

- produktive Provider-Konfiguration
- Queue-/Worker-Betrieb
- grosse Dateien und Timeouts
- Fehler-/Recovery-Konzept
- Monitoring
- Betriebsdokumentation

### Atomizer

Status: Gelb

Vorhanden:

- deterministischer MVP-Atomizer
- Content Atom Schema
- Validation
- Scoring
- Dedupe innerhalb Batch und gegen approved Atoms
- Source References mit Abschnitt, Zeile, Seite und Timestamp, wenn Metadaten vorhanden sind

Offen:

- semantische/modelgestuetzte Extraktion
- Evaluation gegen Goldstandard-Atoms
- Qualitaetsmetriken pro Atomtyp
- robuste Persona-/Industry-Klassifikation
- Versionierung und Freigabeprozess
- Monitoring fuer schlechte oder leere Atom-Batches

### Repurposing Agent

Status: Gelb

Vorhanden:

- lokale Draft-Erzeugung aus Content Atoms
- Newsletter
- Sequenzen
- LinkedIn Post
- LinkedIn Karussell
- Onepager
- lokale Notion-Pending-Mappings

Offen:

- Mini Guide
- Lead Magnet
- Podcast Script
- Video Script
- Brand Voice/Style Guide
- fachliche Review-Qualitaet
- echte Notion-Veröffentlichung
- Approval-Gate vor Nutzung

### Approval Workflow

Status: Gelb

Vorhanden:

- Approval Requests
- Approval Decisions
- lokale Speicherung

Offen:

- echte Review-Oberflaeche
- Rollen/Rechte
- Statusuebergaenge
- Audit Trail fuer Freigaben
- Rueckgabe an Repurposing/Publishing

### Sales / Proposal / Customer Success

Status: Rot

Noch nicht bauen, bevor die bestehenden Gelb-Module produktionsreifer sind.

Offen:

- Sales Agent
- Proposal Agent
- Customer Success Agent
- CRM-/Notion-/E-Mail-Anbindung
- Angebots- und Follow-up-Prozesse

## Production-Readiness-Kriterien

Jedes Modul muss vor Gruen diese Punkte erfuellen:

| Bereich | Frage |
|---|---|
| Funktionalitaet | Funktionieren alle Hauptpfade und Pflichtvarianten? |
| Robustheit | Was passiert bei ungueltigen Inputs, Timeouts und leeren Ergebnissen? |
| Monitoring | Wie werden Fehler erkannt? |
| Logging | Was wird technisch und fachlich protokolliert? |
| Recovery | Wie wird ein abgebrochener Lauf fortgesetzt oder sauber wiederholt? |
| Dokumentation | Kann eine andere Person das Modul betreiben? |
| Tests | Gibt es Unit-, Integrations- und E2E-Tests fuer die Hauptpfade? |
| Sicherheit | Sind Secrets, Rollen, Zugriff und Datenschutz geklaert? |
| Datenhaltung | Werden Master, Processed Sources, Atoms, Artifacts, Approvals und Jobs getrennt gespeichert? |

## Naechste Prioritaet

Nicht als naechstes bauen:

- Sales Agent
- Proposal Agent
- Customer Success Agent

Stattdessen:

1. Homepage und Potenzialanalyse auf Produktionsrisiken pruefen.
2. Backend-Schreibpfad auf `nurovelle_core` klaeren.
3. Notion Sync von lokalem Mapping zu echter API bringen.
4. Atomizer-Qualitaet messbar machen.
5. Repurposing-Qualitaet und Approval-Gate verbessern.
6. Erst danach neue Output-Formate wie Mini Guide, Lead Magnet, Podcast und Video Script erweitern.

## Akzeptanzkriterien fuer diesen Audit

Dieser Audit ist brauchbar, wenn:

- alle bekannten Kernmodule erfasst sind
- MVP, production ready und nicht gebaut klar getrennt sind
- keine neuen Features priorisiert werden, solange bestehende Gelb-Module kritische Produktionsluecken haben
- die naechsten Schritte auf Stabilisierung, Monitoring, Tests und Betrieb ausgerichtet sind
