# Homepage Project Overview – Nurovelle

## Ziel

Erstellung einer klaren B2B-Homepage für Nurovelle.

Die Homepage erklärt, was angeboten wird, für wen es gedacht ist und führt Besucher zur kostenlosen KI-Potenzialanalyse.

## Hauptziel

Besucher sollen verstehen:

- welches Problem gelöst wird
- für wen das Angebot geeignet ist
- welche Ergebnisse sie erwarten können
- warum die Umsetzung glaubwürdig ist
- wie sie Kontakt aufnehmen oder eine Analyse anfordern

## Zielgruppe

- Mittelständische Unternehmen
- technische Betriebe
- Dienstleister
- Selbstständige
- Geschäftsführer
- Operations-Leiter
- Prozessverantwortliche
- Teams mit vielen manuellen Abläufen

## Kernbotschaft

Nurovelle hilft Unternehmen, manuelle Prozesse zu analysieren, Automatisierungspotenziale zu erkennen und KI sinnvoll in bestehende Abläufe einzubauen.

## Haupt-CTA

Kostenlose KI-Potenzialanalyse anfordern

## Potenzialanalyse-Status

Die Potenzialanalyse ist technisch an den produktiven Nurovelle-Analyse-Flow
angebunden.

`homepage/analyse.html` nutzt:

- produktive API: `https://nurovelle.de/api/v1`
- Ergebnisroute: `https://nurovelle.de/results/<analysis_id>`
- Backend-Scoring statt lokaler Frontend-Berechnung

Das Homepage-Formular ist bewusst kompakt. Die vollstaendige Fragen-,
Score- und Report-Logik bleibt im Analyse-Backend.

Nach erfolgreicher Reporterzeugung wird zusaetzlich ein Lead im Backend
angelegt. Dadurch koennen Notion-Sync und Newsletter-/Nurturing-Prozesse
backendseitig greifen, sofern sie auf dem VPS aktiviert sind.

## Neben-CTA

Praxisleitfaden herunterladen

## Finale Branchen

1. Energie & Versorgung
2. Finanzen & Versicherung
3. Industrie & Produktion
4. Verwaltung & HR
5. Marketing & Vertrieb
6. Gesundheitswesen & Pflege
7. Bildung & Forschung
8. Dienstleistung & KMU
9. Sonstige Branchen

## Finale Services

1. Verbrauchsdaten & Betriebsberichte automatisieren
2. Beleg-, Vertrags- & Risikoprüfung automatisieren
3. Produktionsdaten & Qualitätsprozesse automatisieren
4. Dokumentenabläufe & Personalprozesse automatisieren
5. Lead-, Content- & Vertriebsprozesse automatisieren
6. Formular-, Termin- & Dokumentationsabläufe automatisieren
7. Wissens-, Lern- & Forschungsdaten strukturieren
8. Kundenkommunikation & interne Abläufe automatisieren
9. Individuelle Prozessanalyse & Automatisierung

## Tonalität

- sachlich
- professionell
- klar
- kein KI-Hype
- nutzenorientiert
- mittelstandstauglich
- verständlich für Selbstständige und KMU

## Finaler visueller Stil

### Basis

- matte schwarze Flächen
- dunkle grün-schwarze Verläufe
- smaragdgrüne Glow-Effekte nur kontrolliert
- abstrakte Systemarchitektur
- technische Premium-Optik
- klare B2B-SaaS-Anmutung

### Akzentfarbe

Gold wird genutzt für:

- Rahmen
- CTA-Buttons
- aktive Elemente
- Hover-Effekte
- wichtige Highlights
- Divider-Lines
- Premium-Akzente

### Nicht erlaubt

- blaue Hauptfarben
- violette Glow-Effekte
- bunte Verläufe
- generische KI-Roboter
- Stockfotos
- überladene Dashboards
- Services als Branchen ausgeben
- Branchen als Services ausgeben

## Gesamtwirkung

Premium. Technisch. Modern. Kontrolliert. Nicht verspielt. Nicht futuristisch-chaotisch.
