# DATABASE_SCHEMA

Version: 1.0  
Status: Zielarchitektur  
Projekt: Nurovelle  
Dokumenttyp: Technische Dokumentation

---

# 1. Zweck

Dieses Dokument beschreibt die Datenstruktur des Nurovelle-Systems.

Abgedeckt werden:

- Notion CRM
- Analyse-Daten
- Lead-Daten
- Kampagnen-Daten
- Newsletter-Daten
- Agenten-Daten
- Retry-Queue
- Reporting-Daten

---

# 2. Systemübersicht

Das System nutzt mehrere logisch getrennte Datenbereiche.

```text
Website / Analyse Wizard
        ↓
Backend API
        ↓
Analyse Engine
        ↓
Notion CRM
        ↓
Nurturing / Resend
        ↓
Termin / Vertrieb / Projekt
```

---

# 3. Datenbanken

## 3.1 Leads

Zweck:

Speichert alle Kontakte, die über Website, Potenzialanalyse, LinkedIn, Newsletter oder manuelle Erfassung eingehen.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| lead_id | UUID / Text | Ja | Eindeutige Lead-ID |
| created_at | DateTime | Ja | Erstellungszeitpunkt |
| updated_at | DateTime | Ja | Letzte Änderung |
| first_name | Text | Nein | Vorname |
| last_name | Text | Nein | Nachname |
| full_name | Text | Nein | Vollständiger Name |
| email | Email | Ja | Primäre E-Mail-Adresse |
| phone | Text | Nein | Telefonnummer |
| company_id | Relation | Nein | Verknüpfung zur Unternehmen-Datenbank |
| source | Select | Ja | Leadquelle |
| source_detail | Text | Nein | Detailquelle, z. B. LinkedIn-Post, CTA, Landingpage |
| status | Select | Ja | Pipeline-Status |
| lead_temperature | Select | Nein | Cold, Warm, Hot |
| newsletter_opt_in | Checkbox | Ja | Zustimmung zum Newsletter |
| privacy_consent | Checkbox | Ja | Datenschutz-Zustimmung |
| analysis_id | Relation | Nein | Verknüpfung zur Analyse |
| score_total | Number | Nein | Gesamtscore der Analyse |
| segment | Select | Nein | Segment auf Basis Score / Verhalten |
| tags | Multi-Select | Nein | Thematische Zuordnung |
| last_contact_at | DateTime | Nein | Letzter Kontakt |
| next_action | Text | Nein | Nächster geplanter Schritt |
| owner | Person / Text | Nein | Verantwortliche Person |
| notes | Text | Nein | Interne Notizen |

### Status-Werte

| Status | Bedeutung |
|---|---|
| New | Neu eingegangen |
| Analysis Started | Analyse begonnen |
| Analysis Completed | Analyse abgeschlossen |
| Nurturing | In E-Mail-Sequenz |
| Appointment Booked | Termin gebucht |
| Consultation Done | Gespräch durchgeführt |
| Offer Sent | Angebot gesendet |
| Customer | Kunde |
| Lost | Nicht gewonnen |
| Archived | Archiviert |

### Source-Werte

| Quelle | Beschreibung |
|---|---|
| Website | Allgemeine Website |
| Potential Analysis Basic | Kostenlose Analyse |
| Potential Analysis Deep | Kostenpflichtige Analyse |
| LinkedIn | LinkedIn-Beitrag oder Profil |
| Newsletter | Newsletter-Anmeldung |
| Manual | Manuell angelegt |
| Referral | Empfehlung |

---

## 3.2 Companies

Zweck:

Speichert Unternehmensinformationen.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| company_id | UUID / Text | Ja | Eindeutige Unternehmens-ID |
| company_name | Text | Ja | Firmenname |
| industry | Select | Nein | Branche |
| company_size | Select | Nein | Größenklasse |
| website | URL | Nein | Website |
| location | Text | Nein | Standort |
| country | Text | Nein | Land |
| main_contact_id | Relation | Nein | Hauptkontakt |
| leads | Relation | Nein | Zugehörige Leads |
| analyses | Relation | Nein | Zugehörige Analysen |
| maturity_level | Select | Nein | KI-Reifegrad |
| notes | Text | Nein | Interne Notizen |

### Industry-Werte

- Engineering
- Manufacturing
- Service
- Care
- Gastronomy
- Agency
- Other

### Company Size-Werte

- 1-5
- 6-20
- 21-50
- 51-100
- 101-250
- 251-500
- 500+

---

## 3.3 Analyses

Zweck:

Speichert jede durchgeführte Potenzialanalyse.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| analysis_id | UUID / Text | Ja | Eindeutige Analyse-ID |
| created_at | DateTime | Ja | Startzeitpunkt |
| completed_at | DateTime | Nein | Abschlusszeitpunkt |
| lead_id | Relation | Ja | Zugehöriger Lead |
| company_id | Relation | Nein | Zugehöriges Unternehmen |
| analysis_type | Select | Ja | Basic oder Deep |
| industry_module | Select | Nein | Ausgewähltes Branchenmodul |
| status | Select | Ja | Analyse-Status |
| score_total | Number | Nein | Gesamtscore |
| score_ai_maturity | Number | Nein | KI-Reife |
| score_process | Number | Nein | Prozesse |
| score_data | Number | Nein | Datenreife |
| score_infrastructure | Number | Nein | Infrastruktur |
| score_documentation | Number | Nein | Dokumentation |
| score_collaboration | Number | Nein | Zusammenarbeit |
| score_scaling | Number | Nein | Skalierung |
| score_risk | Number | Nein | Risiko-Score |
| report_url | URL | Nein | Link zum Bericht |
| pdf_url | URL | Nein | Link zum PDF |
| raw_answers | JSON / Text | Ja | Antworten aus dem Wizard |
| findings | JSON / Text | Nein | Generierte Findings |
| recommendations | JSON / Text | Nein | Handlungsempfehlungen |

### Status-Werte

| Status | Bedeutung |
|---|---|
| Started | Analyse gestartet |
| In Progress | Analyse läuft |
| Completed | Analyse abgeschlossen |
| Failed | Fehler |
| Archived | Archiviert |

---

## 3.4 Analysis Answers

Zweck:

Speichert einzelne Antworten aus der Potenzialanalyse.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| answer_id | UUID / Text | Ja | Eindeutige Antwort-ID |
| analysis_id | Relation | Ja | Zugehörige Analyse |
| question_id | Text | Ja | ID aus Masterfragekatalog |
| category | Select | Ja | Kategorie |
| answer_value | Number / Text | Ja | Antwortwert |
| normalized_score | Number | Nein | Normalisierter Score |
| risk_weight | Number | Nein | Risikogewichtung |
| evidence_flag | Checkbox | Nein | Für Findings relevant |

---

## 3.5 Campaigns

Zweck:

Speichert Kampagnen, Sequenzen und Nurturing-Strecken.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| campaign_id | UUID / Text | Ja | Eindeutige Kampagnen-ID |
| name | Text | Ja | Kampagnenname |
| type | Select | Ja | Newsletter, Nurturing, Follow-Up |
| status | Select | Ja | Aktiv, Entwurf, Pausiert |
| target_segment | Multi-Select | Nein | Zielsegmente |
| start_date | Date | Nein | Startdatum |
| end_date | Date | Nein | Enddatum |
| emails | Relation | Nein | Zugehörige E-Mails |
| kpi_open_rate | Number | Nein | Öffnungsrate |
| kpi_click_rate | Number | Nein | Klickrate |
| kpi_booking_rate | Number | Nein | Terminrate |

---

## 3.6 Email Sequences

Zweck:

Speichert einzelne E-Mails innerhalb einer Sequenz.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| email_id | UUID / Text | Ja | Eindeutige Mail-ID |
| campaign_id | Relation | Ja | Zugehörige Kampagne |
| sequence_position | Number | Ja | Position in Sequenz |
| subject | Text | Ja | Betreff |
| preview_text | Text | Nein | Vorschautext |
| body_markdown | Text | Ja | E-Mail-Inhalt |
| cta_text | Text | Nein | CTA-Text |
| cta_url | URL | Nein | CTA-Link |
| delay_days | Number | Nein | Abstand zur vorherigen Mail |
| trigger_condition | Text | Nein | Versandbedingung |
| status | Select | Ja | Draft, Approved, Active, Archived |

---

## 3.7 Content Assets

Zweck:

Speichert Content-Bausteine und veröffentlichte Inhalte.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| content_id | UUID / Text | Ja | Eindeutige Content-ID |
| title | Text | Ja | Titel |
| content_type | Select | Ja | Post, Newsletter, Whitepaper, Mini-Guide, Checkliste |
| source_document | Text / URL | Nein | Ursprungsinhalt |
| atom_ids | Relation / Text | Nein | Genutzte Content-Atome |
| platform | Select | Nein | LinkedIn, Website, Newsletter |
| status | Select | Ja | Draft, Review, Approved, Published |
| publish_date | Date | Nein | Veröffentlichungsdatum |
| campaign_id | Relation | Nein | Zugehörige Kampagne |
| body | Text | Ja | Inhalt |

---

## 3.8 Content Atoms

Zweck:

Speichert atomisierte Content-Bausteine.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| atom_id | UUID / Text | Ja | Eindeutige Atom-ID |
| source_id | Text | Ja | Ursprungsdokument |
| atom_type | Select | Ja | Claim, Statistic, Quote, Tip, Framework, Example |
| topic | Text | Ja | Thema |
| content | Text | Ja | Atom-Inhalt |
| target_audience | Select | Nein | Zielgruppe |
| funnel_stage | Select | Nein | Awareness, Consideration, Decision |
| confidence | Number | Nein | Qualität / Sicherheit |
| reuse_count | Number | Nein | Wiederverwendungen |

---

## 3.9 Appointments

Zweck:

Speichert gebuchte Termine.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| appointment_id | UUID / Text | Ja | Eindeutige Termin-ID |
| lead_id | Relation | Ja | Zugehöriger Lead |
| company_id | Relation | Nein | Zugehöriges Unternehmen |
| booked_at | DateTime | Ja | Buchungszeitpunkt |
| appointment_time | DateTime | Ja | Terminzeit |
| status | Select | Ja | Booked, Completed, No Show, Cancelled |
| meeting_url | URL | Nein | Meeting-Link |
| notes | Text | Nein | Gesprächsnotizen |
| next_step | Text | Nein | Nächster Schritt |

---

## 3.10 Retry Queue

Zweck:

Speichert fehlgeschlagene Systemaktionen für erneute Ausführung.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---:|---|
| retry_id | UUID / Text | Ja | Eindeutige Retry-ID |
| created_at | DateTime | Ja | Erstellungszeitpunkt |
| updated_at | DateTime | Ja | Letzte Änderung |
| action_type | Select | Ja | Notion, Resend, Report, Agent |
| payload | JSON / Text | Ja | Ursprüngliche Nutzdaten |
| error_message | Text | Nein | Fehlermeldung |
| retry_count | Number | Ja | Anzahl Versuche |
| max_retries | Number | Ja | Maximale Versuche |
| next_retry_at | DateTime | Ja | Nächster Versuch |
| status | Select | Ja | Pending, Running, Failed, Resolved |

---

# 4. Datenbeziehungen

```text
Company 1:n Leads
Company 1:n Analyses
Lead 1:n Analyses
Lead 1:n Appointments
Campaign 1:n Email Sequences
Campaign 1:n Content Assets
Content Asset n:m Content Atoms
Analysis 1:n Analysis Answers
Analysis 1:n Findings
```

---

# 5. Pflichtlogik

## Lead-Erstellung

Ein Lead darf nur angelegt werden, wenn mindestens vorhanden ist:

- email
- source
- privacy_consent

## Analyse-Erstellung

Eine Analyse darf nur gespeichert werden, wenn vorhanden ist:

- analysis_id
- lead_id
- analysis_type
- raw_answers

## Newsletter-Versand

Newsletter darf nur versendet werden, wenn:

- newsletter_opt_in = true
- privacy_consent = true
- email vorhanden

---

# 6. Datenschutz

Zu speichern:

- Nur notwendige personenbezogene Daten
- Opt-in-Zeitpunkt
- Quelle der Einwilligung
- Abmeldestatus

Zu vermeiden:

- unnötige Gesundheitsdaten
- private Informationen ohne Zweck
- unstrukturierte sensible Notizen

---

# 7. Offene technische Folgeaufgaben

- Exakte Notion Property-Namen finalisieren
- UUID-Strategie festlegen
- Exportformat für Reports festlegen
- Backup-Regel für CRM definieren
- Löschkonzept nach DSGVO ergänzen
