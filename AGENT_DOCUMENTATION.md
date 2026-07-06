# AGENT_DOCUMENTATION

Version: 1.0  
Status: Zielarchitektur  
Projekt: Nurovelle  
Dokumenttyp: Technische Dokumentation

---

# 1. Zweck

Dieses Dokument beschreibt die Agenten des Nurovelle-Systems.

Abgedeckt werden:

- Aufgaben
- Eingaben
- Ausgaben
- Trigger
- Abhängigkeiten
- Fehlerfälle
- Qualitätsregeln

---

# 2. Agentenübersicht

```text
Multiprocessor
    ↓
Content Atomizer
    ↓
Content Repurposing Agent
    ↓
Newsletter Agent
    ↓
CRM / Nurturing
```

Weitere Agenten:

- Report Agent
- Lead Agent
- CRM Agent
- Follow-Up Agent
- Appointment Agent
- Quality Control Agent

---

# 3. Multiprocessor

## Aufgabe

Der Multiprocessor verarbeitet große Eingabedokumente und bereitet sie für weitere Agenten auf.

## Eingaben

- Whitepaper
- Mini-Guides
- Checklisten
- Analyseberichte
- Blogtexte
- Rohnotizen
- Transkripte

## Ausgaben

- strukturierte Dokumentabschnitte
- Content-Blöcke
- Metadaten
- Übergabepaket an Content Atomizer

## Trigger

- neues Dokument hochgeladen
- neuer Report erstellt
- neuer Content-Cluster geplant

## Verarbeitungsschritte

1. Dokument einlesen
2. Kapitel erkennen
3. Abschnitte extrahieren
4. Inhalt klassifizieren
5. Übergabestruktur erzeugen
6. An Atomizer weitergeben

## Fehlerfälle

| Fehler | Reaktion |
|---|---|
| Dokument leer | Fehlerstatus setzen |
| Format unbekannt | manuellen Review anfordern |
| Inhalt zu lang | Chunking starten |
| Übergabe fehlgeschlagen | Retry Queue |

---

# 4. Content Atomizer

## Aufgabe

Der Content Atomizer zerlegt große Inhalte in wiederverwendbare Content-Atome.

## Atomtypen

- Claim
- Statistic
- Quote
- Tip
- Framework
- Checklist Item
- Example
- Warning
- CTA Fragment
- Story Fragment

## Eingaben

- strukturierte Abschnitte vom Multiprocessor
- Thema
- Zielgruppe
- Funnel-Stufe

## Ausgaben

Content-Atome mit:

- atom_id
- atom_type
- topic
- content
- target_audience
- funnel_stage
- confidence
- source_reference

## Qualitätsregeln

Ein Atom muss:

- eigenständig verständlich sein
- aus dem Quellinhalt ableitbar sein
- keine unbelegte Behauptung enthalten
- einer klaren Zielgruppe zugeordnet sein
- wiederverwendbar sein

## Trigger

- neues Whitepaper
- neuer Mini-Guide
- neuer Report
- manuelle Content-Erstellung

## Fehlerfälle

| Fehler | Reaktion |
|---|---|
| Atom ohne Aussage | verwerfen |
| Doppelung erkannt | zusammenführen |
| Quelle unklar | Review markieren |
| Zu werblich | Tonalität korrigieren |

---

# 5. Content Repurposing Agent

## Aufgabe

Der Content Repurposing Agent erzeugt aus Content-Atomen neue Formate.

## Eingaben

- Content-Atome
- Zielplattform
- Format
- Zielgruppe
- Funnel-Stufe
- Tonalität

## Ausgaben

- LinkedIn-Posts
- Karussell-Texte
- Newsletter
- Blogartikel
- Mini-Guides
- Checklisten
- Onepager
- Executive Briefings

## Unterstützte Formate

| Format | Ziel |
|---|---|
| LinkedIn Post | Reichweite / Vertrauen |
| Karussell | Erklärung / Aufmerksamkeit |
| Newsletter | Beziehung / Nurturing |
| Mini-Guide | Leadmagnet |
| Checkliste | Anwendung |
| Whitepaper | Autorität |
| Onepager | Angebotskommunikation |

## Qualitätsregeln

Der Agent muss:

- Quelleninhalt einhalten
- keine neuen Fakten erfinden
- CTA-Regeln beachten
- Nurovelle-Schreibweise nutzen
- Zielgruppe berücksichtigen
- Wiederholungen vermeiden

## Fehlerfälle

| Fehler | Reaktion |
|---|---|
| Zu wenig Atome | weitere Atome anfordern |
| Format unvollständig | neu generieren |
| CTA falsch | CTA-Regel anwenden |
| Marke falsch geschrieben | Korrektur erzwingen |

---

# 6. Report Agent

## Aufgabe

Der Report Agent erzeugt aus Analyseergebnissen einen strukturierten Bericht.

## Eingaben

- Analyseantworten
- Scores
- Findings
- Branchenmodul
- Lead-Daten

## Ausgaben

- HTML-Report
- PDF-Report
- Zusammenfassung für CRM
- Empfehlungen

## Report-Bestandteile

- Executive Summary
- Score-Übersicht
- Kategorieanalyse
- Risikobewertung
- Handlungsempfehlungen
- Priorisierung
- CTA zur Deep Analyse oder Beratung

## Qualitätsregeln

Der Report Agent darf:

- nur Findings auf Basis vorhandener Evidence erzeugen
- keine unbelegte Diagnose ausgeben
- keine Branchenannahmen ohne Branchenmodul treffen
- keine neuen CTAs erfinden, wenn eine finale CTA-Seite vorgegeben ist

## Fehlerfälle

| Fehler | Reaktion |
|---|---|
| Score fehlt | Report stoppen |
| Findings leer | Fallback-Report erzeugen |
| PDF-Export fehlgeschlagen | Retry Queue |
| CRM-Speicherung fehlgeschlagen | Retry Queue |

---

# 7. Lead Agent

## Aufgabe

Der Lead Agent verarbeitet neue Leads.

## Eingaben

- Formularinformationen
- Analyseinformationen
- Trackingdaten
- Opt-in-Daten

## Ausgaben

- Lead-Datensatz
- Segment
- Pipeline-Status
- Nurturing-Trigger

## Verarbeitungsschritte

1. Eingabe validieren
2. Dubletten prüfen
3. Lead erstellen oder aktualisieren
4. Quelle speichern
5. Segment bestimmen
6. Nurturing starten

## Fehlerfälle

| Fehler | Reaktion |
|---|---|
| E-Mail fehlt | Lead nicht erstellen |
| Datenschutz fehlt | Newsletter nicht starten |
| Notion nicht erreichbar | Retry Queue |
| Dublette gefunden | bestehenden Lead aktualisieren |

---

# 8. CRM Agent

## Aufgabe

Der CRM Agent hält Notion-Datenbanken aktuell.

## Eingaben

- Lead Events
- Analyse Events
- Termin Events
- E-Mail Events

## Ausgaben

- aktualisierte Notion-Datensätze
- Pipeline-Status
- Tags
- Aufgaben

## Statuslogik

| Event | Neuer Status |
|---|---|
| Analyse gestartet | Analysis Started |
| Analyse abgeschlossen | Analysis Completed |
| Nurturing gestartet | Nurturing |
| Termin gebucht | Appointment Booked |
| Gespräch abgeschlossen | Consultation Done |
| Angebot versendet | Offer Sent |
| Kunde gewonnen | Customer |

---

# 9. Newsletter Agent

## Aufgabe

Der Newsletter Agent erstellt und plant E-Mail-Inhalte.

## Eingaben

- Content-Atome
- Kampagnenziel
- Zielsegment
- Funnel-Stufe

## Ausgaben

- Betreff
- Vorschautext
- Body
- CTA
- Varianten

## E-Mail-Typen

- Willkommensmail
- Nurturing-Mail
- Follow-Up-Mail
- Wochennewsletter
- Reaktivierungsmail

## Qualitätsregeln

Eine E-Mail muss:

- eine klare Hauptaussage haben
- einen klaren CTA haben
- zur Funnel-Stufe passen
- keine falschen Versprechen enthalten
- Opt-out technisch ermöglichen

---

# 10. Follow-Up Agent

## Aufgabe

Der Follow-Up Agent reagiert auf Verhalten.

## Eingaben

- Mail geöffnet
- Link geklickt
- Analyse abgeschlossen
- Termin nicht gebucht
- Termin abgesagt
- Angebot nicht beantwortet

## Ausgaben

- Follow-Up-Mail
- CRM-Statusupdate
- Reminder
- Aufgabe zur manuellen Prüfung

## Triggerlogik

| Trigger | Aktion |
|---|---|
| Analyse abgeschlossen | Ergebnis-Mail senden |
| Keine Terminbuchung nach 3 Tagen | Follow-Up senden |
| Link geklickt | Lead als warm markieren |
| Termin gebucht | Sequenz pausieren |
| Angebot offen 7 Tage | Nachfass-Mail vorbereiten |

---

# 11. Appointment Agent

## Aufgabe

Der Appointment Agent verarbeitet Terminbuchungen.

## Eingaben

- Kalenderbuchung
- Lead-ID
- E-Mail
- Terminzeit

## Ausgaben

- CRM-Update
- Bestätigungsmail
- Gesprächsvorbereitung
- Gesprächsleitfaden

## Besonderheit

Der Agent kann auf Basis der Analyse einen individuellen Gesprächsleitfaden erzeugen.

Inhalt:

- wichtigste Pain Points
- Score-Zusammenfassung
- kritische Risiken
- passende Einstiegsfragen
- mögliche Angebotsrichtung

---

# 12. Quality Control Agent

## Aufgabe

Der Quality Control Agent prüft Inhalte vor Veröffentlichung oder Versand.

## Prüfpunkte

- Marke korrekt: Nurovelle
- keine erfundenen Fakten
- CTA korrekt
- Zielgruppe passend
- Tonalität passend
- keine Dubletten
- keine widersprüchlichen Aussagen
- Datenschutz eingehalten

## Ausgabe

- approved
- needs_review
- rejected

Mit Begründung.

---

# 13. Gemeinsame Agentenregeln

Alle Agenten müssen:

- keine Daten löschen ohne explizite Freigabe
- Quellinformationen respektieren
- keine unbelegten Aussagen erzeugen
- Fehler nachvollziehbar loggen
- Retry Queue nutzen
- Status an CRM zurückmelden

---

# 14. Offene technische Folgeaufgaben

- Agenten-IDs finalisieren
- Prompt-Versionierung ergänzen
- Logging-Format definieren
- Review-Workflow ergänzen
- Testfälle je Agent ergänzen
