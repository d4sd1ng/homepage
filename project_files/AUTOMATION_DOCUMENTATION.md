# AUTOMATION_DOCUMENTATION

Version: 1.0  
Status: Zielarchitektur  
Projekt: Nurovelle  
Dokumenttyp: Technische Dokumentation

---

# 1. Zweck

Dieses Dokument beschreibt die Automationen des Nurovelle-Systems.

Abgedeckt werden:

- Trigger
- Bedingungen
- Aktionen
- Zielsysteme
- Fehlerbehandlung
- Retry-Logik

---

# 2. Automationsübersicht

```text
Website Event
    ↓
Backend Event
    ↓
Automation Router
    ↓
Agent / CRM / E-Mail / Report
    ↓
Statusupdate
```

---

# 3. Automation A001 – Lead aus Website erstellen

## Trigger

Kontaktformular abgeschickt.

## Bedingungen

Pflichtfelder:

- email
- privacy_consent
- source

## Aktionen

1. Eingaben validieren
2. Lead-Dublette prüfen
3. Lead in Notion erstellen oder aktualisieren
4. Quelle speichern
5. Status auf `New` setzen
6. Bestätigungsmail auslösen, falls Opt-in vorhanden

## Zielsysteme

- Backend API
- Notion
- Resend

## Fehlerbehandlung

| Fehler | Aktion |
|---|---|
| Notion API nicht erreichbar | Retry Queue |
| E-Mail ungültig | Vorgang abbrechen |
| Datenschutz fehlt | Lead ohne Newsletter speichern oder Vorgang blockieren, je nach Formularregel |

---

# 4. Automation A002 – Potenzialanalyse starten

## Trigger

User startet Analyse-Wizard.

## Bedingungen

- Session vorhanden
- Analyse-Typ gewählt

## Aktionen

1. Analyse-ID erzeugen
2. Analyse-Datensatz erstellen
3. Status `Started` setzen
4. Wizard-Fortschritt speichern

## Zielsysteme

- Backend
- Notion Analyses

---

# 5. Automation A003 – Antworten speichern

## Trigger

User beantwortet Frage im Wizard.

## Bedingungen

- analysis_id vorhanden
- question_id gültig
- answer_value vorhanden

## Aktionen

1. Antwort validieren
2. Antwort speichern
3. Fortschritt aktualisieren
4. Optional Zwischenscore berechnen

## Fehlerbehandlung

| Fehler | Aktion |
|---|---|
| Ungültige question_id | Antwort ablehnen |
| Analyse nicht gefunden | Session prüfen |
| Speicherung fehlgeschlagen | Retry Queue oder lokaler Zwischenspeicher |

---

# 6. Automation A004 – Analyse abschließen

## Trigger

Letzte Frage beantwortet oder Analyse wird aktiv abgeschlossen.

## Bedingungen

- Mindestanzahl Pflichtfragen beantwortet
- Lead-Daten vorhanden
- Datenschutz bestätigt

## Aktionen

1. Antworten finalisieren
2. Scoring berechnen
3. Findings erzeugen
4. Report Agent starten
5. Analyse-Status auf `Completed` setzen
6. Lead-Status aktualisieren
7. Ergebnis-Mail vorbereiten

## Zielsysteme

- Analyse Engine
- Report Agent
- Notion
- Resend

---

# 7. Automation A005 – Report erstellen

## Trigger

Analyse abgeschlossen.

## Bedingungen

- Scores vorhanden
- Findings vorhanden oder Fallback erlaubt
- analysis_id vorhanden

## Aktionen

1. Reportdaten laden
2. HTML-Report erzeugen
3. PDF-Report erzeugen
4. PDF-Link speichern
5. CRM aktualisieren
6. Versand vorbereiten

## Fehlerbehandlung

| Fehler | Aktion |
|---|---|
| PDF-Erstellung fehlgeschlagen | Retry Queue |
| Findings fehlen | Fallback-Report |
| Speichern fehlgeschlagen | Retry Queue |

---

# 8. Automation A006 – Ergebnis-Mail senden

## Trigger

Report erfolgreich erstellt.

## Bedingungen

- email vorhanden
- privacy_consent vorhanden
- report_url oder pdf_url vorhanden

## Aktionen

1. Mailtemplate auswählen
2. Report-Link einfügen
3. E-Mail über Resend senden
4. Versandstatus speichern
5. Lead in Nurturing aufnehmen, falls Opt-in vorhanden

## Zielsysteme

- Resend
- Notion

---

# 9. Automation A007 – Nurturing starten

## Trigger

Lead erfüllt Nurturing-Bedingungen.

## Bedingungen

- newsletter_opt_in = true
- lead_status nicht Customer
- gültige E-Mail vorhanden

## Aktionen

1. Segment bestimmen
2. passende Sequenz auswählen
3. Kampagnenstatus setzen
4. erste Nurturing-Mail planen

## Sequenzlogik

| Segment | Sequenz |
|---|---|
| Cold | Trust-Aufbau |
| Warm | Problem/Lösung |
| Hot | Termin-Einladung |
| Deep Interest | Deep-Analyse-Angebot |

---

# 10. Automation A008 – Newsletter versenden

## Trigger

Newsletter-Kampagne geplant.

## Bedingungen

- Kampagne aktiv
- Empfänger Opt-in gültig
- E-Mail approved

## Aktionen

1. Empfängersegment laden
2. Ausschlüsse prüfen
3. E-Mail versenden
4. Events erfassen
5. KPI aktualisieren

## Ausschlüsse

Nicht versenden an:

- unsubscribed
- bounced
- Customer, falls Kampagne nur für Leads ist
- manuell ausgeschlossene Kontakte

---

# 11. Automation A009 – E-Mail Event verarbeiten

## Trigger

Resend Event.

Events:

- delivered
- opened
- clicked
- bounced
- complained
- unsubscribed

## Aktionen

| Event | Aktion |
|---|---|
| opened | Engagement erhöhen |
| clicked | Lead wärmer markieren |
| bounced | Versand sperren |
| unsubscribed | Newsletter Opt-in deaktivieren |
| complained | Kontakt sperren |

---

# 12. Automation A010 – Terminbuchung verarbeiten

## Trigger

Termin wurde gebucht.

## Bedingungen

- Lead anhand E-Mail identifizierbar
- Terminzeit vorhanden

## Aktionen

1. Appointment-Datensatz erstellen
2. Lead-Status auf `Appointment Booked` setzen
3. Nurturing pausieren
4. Bestätigungsmail senden
5. Gesprächsleitfaden erzeugen

## Zielsysteme

- Kalender
- Notion
- Appointment Agent
- Resend

---

# 13. Automation A011 – Gesprächsleitfaden erzeugen

## Trigger

Termin gebucht.

## Bedingungen

- Analyse vorhanden oder Lead-Daten vorhanden

## Aktionen

1. Analyse laden
2. Score-Zusammenfassung erstellen
3. Pain Points extrahieren
4. Einstiegsfragen formulieren
5. Gesprächsleitfaden speichern

## Ausgabe

- Gesprächszusammenfassung
- Fragenliste
- Angebotsrichtung
- Risiken
- nächste Empfehlung

---

# 14. Automation A012 – Angebot nachfassen

## Trigger

Angebot länger als definierte Frist offen.

## Bedingungen

- Status `Offer Sent`
- kein Abschluss
- kein Lost-Status

## Aktionen

1. Follow-Up vorbereiten
2. Aufgabe im CRM erstellen
3. Optional E-Mail-Entwurf erzeugen

---

# 15. Automation A013 – Kunde gewonnen

## Trigger

Lead-Status wird auf `Customer` gesetzt.

## Aktionen

1. Nurturing stoppen
2. Kundensegment setzen
3. Onboarding starten
4. Projektvorbereitung anlegen
5. Interne Benachrichtigung erstellen

---

# 16. Automation A014 – Retry Queue verarbeiten

## Trigger

Geplanter Retry-Zeitpunkt erreicht.

## Bedingungen

- status = Pending
- retry_count < max_retries

## Aktionen

1. Retry-Datensatz laden
2. Aktion erneut ausführen
3. Ergebnis speichern
4. Bei Erfolg Status `Resolved`
5. Bei Fehler retry_count erhöhen
6. Bei max_retries Status `Failed`

## Backoff-Strategie

| Versuch | Wartezeit |
|---:|---:|
| 1 | 5 Minuten |
| 2 | 30 Minuten |
| 3 | 2 Stunden |
| 4 | 12 Stunden |
| 5 | 24 Stunden |

---

# 17. Automation A015 – Content aus Dokument erzeugen

## Trigger

Neues Quelldokument vorhanden.

## Aktionen

1. Multiprocessor starten
2. Content Atomizer starten
3. Content Repurposing Agent starten
4. Entwürfe speichern
5. Review-Status setzen

## Zielsysteme

- Content-Datenbank
- Agentensystem

---

# 18. Automation A016 – Content Review abschließen

## Trigger

Content wird freigegeben.

## Aktionen

1. Status auf `Approved` setzen
2. Veröffentlichungsdatum prüfen
3. Veröffentlichung oder Planung vorbereiten
4. Kampagne aktualisieren

---

# 19. Fehlerklassen

| Klasse | Bedeutung | Reaktion |
|---|---|---|
| ValidationError | Eingabe ungültig | abbrechen |
| ExternalApiError | Drittanbieterfehler | Retry Queue |
| PermissionError | Zugriff fehlt | Admin prüfen |
| ReportGenerationError | Reportfehler | Retry / Fallback |
| EmailDeliveryError | Versandfehler | Retry / Sperre |
| DataConflictError | Dublette / Konflikt | manuelle Prüfung |

---

# 20. Logging

Jede Automation soll speichern:

- automation_id
- event_id
- timestamp
- input_reference
- output_reference
- status
- error_message
- retry_id

---

# 21. Offene technische Folgeaufgaben

- Konkrete Webhook-Endpunkte finalisieren
- Event-Namen finalisieren
- Retry Worker implementieren oder dokumentieren
- Monitoring-Dashboard ergänzen
- Testfälle je Automation ergänzen
