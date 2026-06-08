# Homepage Analysis API Integration

Stand: 2026-06-08

## Status

`homepage/analyse.html` ist an den produktiven Nurovelle-Analyse-Flow angebunden.

## Geltende Regel

Die Homepage berechnet keine Scores lokal.

Die Homepage startet nur den Analyse-Flow und zeigt danach den Ergebnislink.

## API

Basis:

```text
https://nurovelle.de/api/v1
```

Flow:

```text
GET  /questions?industry=<industry>&tier=basic&include_risk=false
POST /analysis/start
POST /analysis/<analysis_id>/answers
POST /analysis/<analysis_id>/score
POST /analysis/<analysis_id>/report
```

Ergebnis:

```text
https://nurovelle.de/results/<analysis_id>
```

## Umsetzung

Die Seite nutzt ein kompaktes Formular:

- Vorname
- Nachname
- E-Mail
- Unternehmen
- Branche
- Unternehmensgroesse
- Zeitaufwand
- Datenlage
- Herausforderung
- Telefon optional
- Website optional

Beim Absenden:

- Branche wird auf einen API-Industry-Key gemappt.
- Echte Fragen werden geladen.
- Formularangaben werden auf gueltige Antwortwerte gemappt.
- Analyse wird im Backend erstellt.
- Scores und Report werden im Backend erzeugt.
- Ergebnislink wird angezeigt.

## Validierung

Live-Smoke-Test am 2026-06-08:

- Fragen geladen: `48`
- Analyse-ID erzeugt
- Antworten gespeichert
- Scores berechnet
- Report erzeugt
- Ergebnisroute liefert `200`

Test-Analyse:

```text
071b8493-875f-48a6-beab-b70e7e0dae84
```

## Nicht erlaubt

- keine lokale Fake-Auswertung
- keine lokalen Score-Regeln in der Homepage
- keine direkte DB-Verbindung
- keine Heimnetz-/Pi-/WireGuard-Abhaengigkeit
