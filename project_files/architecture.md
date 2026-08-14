# Nurovelle Homepage – Architecture

Stand: 2026-08-14  
Status: in Arbeit

## Zweck dieser Datei

Diese Datei beschreibt ausschließlich die **technische Struktur, Integration und Datenflüsse** des Homepage-Projekts.

Design steht in `styleguide.md`, Projektumfang in `project_overview.md`.

## Seiten / Hauptbestandteile

Aktuell relevante Website-Bestandteile:

- `index.html` – Homepage / bestehender Produktionsstand
- `analyse.html` – KI-Potenzialanalyse, sofern im realen Projektbestand vorhanden
- Leistungsdetailseiten
- Download-/Praxisleitfaden-Ziele
- Impressum
- Datenschutz

Der reale Projektordner ist vor Änderungen auf vorhandene Seiten und Pfade zu prüfen.

## Frontend-Struktur

Ziel ist eine einfache, wartbare HTML/CSS/JS-Struktur.

Typische Struktur:

```text
/
├── index.html
├── analyse.html
├── assets/
├── css/
│   ├── styles.css
│   └── weitere freigegebene CSS-Dateien
└── js/
    └── main.js
```

Bestehende Projektstruktur hat Vorrang, sofern sie nicht gegen eine freigegebene Entscheidung verstößt.

## Design-Code

- `styleguide.md` = fachliche Designquelle
- `nurovelle-tokens.css` = technische Design-Tokens
- CSS-/Animationsreferenzen = technische Referenz, keine eigenständige Designentscheidung

Komponenten sollen bestehende Tokens verwenden und keine neuen Farb-/Gradient-/Spacing-Systeme einführen.

## Navigation

- Breadcrumb-basierter Header
- drei Breadcrumb-Bereiche mit Submenüs
- Hover plus Tastaturzugänglichkeit
- Sidebar-/Hamburger-Steuerung

Die tatsächlichen Selektoren und DOM-Strukturen müssen im Produktionscode geprüft werden.

## KI-Potenzialanalyse

Die Potenzialanalyse ist der zentrale Lead-Flow.

Erhalten bleiben müssen, sofern im bestehenden `analyse.html` vorhanden:

- bestehende Formularfelder
- Pflichtfeldlogik
- Einwilligung / Datenschutz
- Honeypot
- Submission
- API-Anbindung
- Score-/Auswertungslogik
- Lead-Erfassung
- Success-Zustand
- Error-Zustand

Keine API-Endpunkte, Felder oder Datenlogik ohne ausdrückliche Freigabe ändern.

## Homepage-Formular

Der freigegebene Homepage-Stand enthält eine eigene Formularsektion direkt nach der Potenzialanalyse-Sektion.

Layout:

- begleitende Card links
- Formular rechts

Technische Implementierung muss mit dem vorhandenen Lead-/Analyse-Flow abgestimmt werden. Keine neue parallele Datenlogik erfinden.

## Daten- und Integrationssysteme

Zum Gesamtprojekt gehören bereits verbundene Systeme für:

- KI-Potenzialanalyse
- Lead-Datenbank
- Notion
- Nurturing-Mail

Ziel der Homepage-Integration ist, Website-Leads und Analyse-Ergebnisse sauber in die vorhandenen Systeme zu übergeben.

Konkrete Endpunkte, Datenmodelle und Feldzuordnungen sind vor Implementierung im realen System zu prüfen. Diese Datei enthält keine erfundenen API-Schemas.

## Download-Flow

Download-Buttons verwenden reale Downloadziele.

Zustände:

1. Idle
2. Aktion / Loading
3. Success
4. Error / Retry

Der visuelle Success-Zustand darf die reale Download- oder Lead-Aktion nicht ersetzen.

## Detailseiten

Detailseiten verwenden gemeinsame technische Komponenten für:

- Header
- Breadcrumbs
- Sidebar
- Footer
- Hero
- Cards
- FAQ
- Potenzialanalyse-CTA
- Kontakt-/Erstgesprächskomponente

Die Komponenten dürfen parametrisiert werden, ohne pro Seite neue unabhängige Layoutsysteme zu erzeugen.

## Assets

Assetpfade und Bestandsstatus stehen ausschließlich in `assets.md`.

Vor Implementierung:

- Dateiexistenz prüfen
- Endung prüfen
- Pfad prüfen
- keine alten Pfade blind übernehmen

## Responsive / Accessibility

Technische Mindestanforderungen:

- Desktop
- Tablet
- Smartphone
- Tastaturbedienung
- Focus-States
- mobile Tap-Zustände
- `prefers-reduced-motion`
- kein horizontales Scrollen durch Layoutkomponenten

## SEO / Metadaten

Zu prüfen und korrekt zu setzen:

- `<title>`
- Meta Description
- Canonical
- Open Graph
- Twitter Card
- semantische Heading-Struktur
- Alt-Texte für inhaltliche Bilder
- funktionierende interne Links

## Rechtliche Verlinkungen

- Impressum erreichbar
- Datenschutz erreichbar
- Einwilligung im Formular sichtbar und technisch erhalten

Inhaltliche juristische Prüfung ist keine technische Freigabe und wird bei Bedarf als offene Aufgabe in `todo.md` geführt.

## Tests vor Launch

- Navigation / Breadcrumbs
- Sidebar / Burger
- CTA-Ziele
- Links
- Potenzialanalyse
- Formular
- Success / Error
- Downloads
- Detailseiten
- Impressum / Datenschutz
- Desktop / Tablet / Smartphone
- keine Console-Fehler aus den geänderten Funktionen
