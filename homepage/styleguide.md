# Nurovelle Styleguide

Stand: 2026-07-05  
Status: aktive Design- und Komponentenquelle

Dieser Styleguide bündelt die verbindlichen Designregeln für Homepage und Detailseiten. Er ersetzt verstreute Zwischenstände und verweist für konkrete CSS-Umsetzung nur auf zwei technische Dateien:

- `nurovelle-tokens.css`
- `nurovelle-animations.css`

## 1. Designprinzip

Nurovelle nutzt eine dunkle, technische Premium-Optik:

- matte schwarze Flächen
- sehr dunkles Petrol / dunkles Grün-Schwarz
- Gold als hochwertiger Akzent
- klare B2B-SaaS-Anmutung
- kontrollierte technische Animationen
- keine Bildgenerierung für steuerbare UI-Komponenten

## 2. Farben

### Basisflächen

- Schwarz: `#050706`
- Mattes Schwarz: `#080B09`
- Tiefgrün: `#0A1913`
- Smaragd dunkel: `#112A20`
- Dunkles Teal/Petrol: `#163A35`

### Text

- Haupttext hell: `#F5F7F4`
- Sekundärtext: `#B9C3BD`
- Text auf Gold: `#050706`

### Gold

Gold wird eingesetzt für:

- CTA-Buttons
- Rahmen
- aktive Elemente
- Hover-/Fokuszustände
- Divider
- feine Lichtkanten
- Premium-Akzente

Verbindliche Goldverläufe liegen in `nurovelle-tokens.css`.

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Neon
- Bronze
- Kupfer
- Gaming-/Comic-Buttonwirkung
- Casino-/Spielautomatwirkung

## 3. Typografie

Aktive Schriftentscheidung:

- Display / große Headlines: `Tapera`
- Fließtext, Navigation, Buttons, Formulare, Cards, Footer: `Inter`

Keine Rückkehr zu den alten Font-Stacks aus früheren Zwischenständen:

- Bebas Neue
- Anca Coder / Coder Pro
- Raleway / Roboto als Hauptsystem

## 4. Layoutgrundlagen

- Maximalbreite: `75rem`
- Seitengutter: responsiv über `--page-gutter`
- Sections arbeiten mit großzügigem vertikalem Abstand
- Mobile Layouts werden nicht separat neu gestaltet, sondern aus dem gleichen System sauber reduziert

## 5. Header

Der Header folgt dem freigegebenen Vorgabedesign.

Aufbau:

- Logo links, klickbar zur Startseite
- Breadcrumbs im Header
- Analyse-CTA rechts
- Hamburger unterhalb des Headers zur Sidebar-Steuerung

Der Analyse-CTA führt zu:

```text
analyse.html
```

Der Header-CTA verwendet die freigegebene CTA-Button-Komponente aus `nurovelle-animations.css`.

## 6. Sidebar

Die Sidebar bleibt gemäß Vorgabedesign.

Einzige funktionale Festlegung:

- Öffnen und Schließen über den Hamburger unter dem Header

Keine neue Sidebar-Struktur und keine frei erfundene Zusatzlogik.

## 7. Hero

### Homepage-Hero

Inhalt:

```text
KI-Agenten für echte Geschäftsprozesse.
```

Subline:

```text
Nurovelle entwickelt individuelle KI-Systeme für Datenverarbeitung, Wissenszugriff, Prozessautomatisierung und Unternehmenssoftware.
```

Zusatzzeile:

```text
Von der Potenzialanalyse über Prompt Engineering und MCP bis zur Umsetzung maßgeschneiderter KI-Lösungen.
```

CTAs:

- `Kostenlose KI-Potenzialanalyse anfordern` → `analyse.html`
- `Praxisleitfaden herunterladen` → Download-Bereich
- `Kostenloses Erstgespräch vereinbaren` → Kontakt-/Portraitbereich

Hero-Visual:

- bestehender finaler Cube / Würfel
- keine Texte im Bild
- keine Labels
- keine Zahlen
- keine Logos

Animation:

- goldene Cube-Ecken dürfen dezent pulsieren
- ruhiger technischer Lichtimpuls
- keine unkontrollierte Bewegung des gesamten Hero-Visuals

## 8. CTAs und Buttons

Aktive Buttonvarianten:

1. CTA-Button mit Arrow-Reveal und Gold-Fill
2. Press-Button mit haptischer Absenkung
3. Downloadbutton mit Success-/Danke-Transformation

Die technische Umsetzung liegt in `nurovelle-animations.css`.

Grundregeln:

- keine generischen Standard-Gold-Pills
- keine neuen Buttonvarianten ohne Freigabe
- Hover, Focus und Tap müssen funktionieren
- Success-Zustände nur nach echter erfolgreicher Aktion setzen

## 9. Download- / Danke-Button

Die Download-Interaktion ist verbindlich als Microinteraction vorgesehen.

Verhalten:

- Startzustand: Downloadbutton / Anfragebutton
- Während Aktion: Ladezustand aus realer Download- oder Formularlogik
- Erfolgszustand: größerer Danke-/Bestätigungsbutton
- Fehlerzustand: Fehler-/Retry-Button

Der Button darf nicht in den Danke-Zustand wechseln, wenn die Aktion technisch fehlgeschlagen ist.

Konkrete CSS-Basis:

- `.nv-download-confirm`
- `.nv-download-confirm.is-success`

## 10. Breadcrumbs

Breadcrumbs werden als Chevron-/Pfeil-Segmente umgesetzt.

Grundregeln:

- im Header integriert
- über `aria-label="Breadcrumb"`
- aktueller Punkt mit `aria-current="page"`
- keine externen Fonts oder Demo-Scripts

Konkrete CSS-Basis:

- `.nv-breadcrumb`

## 11. Cards

Card-Varianten:

- schwarze Cards für Relevanz-/Warum-Bereiche
- Problem-Lösungs-Cards für Nutzen-/Problemabschnitte
- CSS-Cards für Einsatzbereiche und verwandte Leistungen
- Frosted-Glass / Overlay-Reveal als Prüfvariante

Konkrete CSS-Basis:

- `.nv-reveal-card`
- `.nv-reveal-card.is-open`

Mobile:

- Hover-Logik wird per Tap/Focus beziehungsweise `.is-open` abgebildet

## 12. Social Icons

Social Icons werden als CSS/SVG-Komponenten umgesetzt.

Regeln:

- nur Symbol sichtbar
- keine sichtbaren Textlabels
- `aria-label` Pflicht
- keine Bildgenerierung
- Farben aus Nurovelle-System

Konkrete CSS-Basis:

- `.nv-socials`
- `.nv-social`

## 13. Divider

Divider-Varianten sind Prüfvarianten und müssen live beurteilt werden:

- SVG-Schräg-Divider
- Pure-CSS-Angled-Sections
- Diagonal Box / SkewY + Clip-Path

Keine Demo-Farben übernehmen.

## 14. Detailseiten

Detailseiten nutzen eine gemeinsame Vorlage.

Aktuelle Layoutlogik:

1. Hero wie Homepage-Hero, aber mit passendem Bild je Detailseite
2. Was ist ...? — nur Überschrift und Blocktext, keine Cards
3. Warum wichtig / entscheidend? — schwarze Cards
4. Ihr Nutzen — Problem-Lösungs-Cards
5. Typische Einsatzbereiche — CSS-Cards
6. Verwandte Leistungen — CSS-Cards
7. FAQ — wie Homepage, Akkordeon / Expander, 8 Fragen
8. Potenzialanalyse — gleiche Card wie Homepage, bestehender CTA
9. Kontakt / Erstgespräch — rechteckige Card, rundes Portrait-Mockup, Social Icons, Kontakt / Erstgespräch-CTA
10. Formular

## 15. Workflow-Bildsprache

Ein Workflow wird technisch-mechanisch gedacht, nicht als generisches Dashboard.

Zulässige Modulwelt:

- Mechanik
- Schalter
- Relais
- Displays
- Container
- Terminals
- Scanner
- Speicher
- Ventile
- Verteiler
- Kontrollmodule

## 16. Animationen

Aktive Animationen und Interaktionen liegen in `nurovelle-animations.css`:

- CTA Arrow-Reveal + Gold-Fill
- Press-Button / haptische Absenkung
- Downloadbutton → Danke-/Bestätigungsbutton
- Breadcrumb Chevron-Segmente
- Hero Orb / Cube-Entstehung
- Conic-/Noise-Mask
- Divider-Prüfvarianten
- Card Overlay-Reveal
- Social Icon Hover/Focus
- Board-/Dashboard-Prüfvariante
- Reduced Motion

## 17. Accessibility und Motion

Pflicht:

- Tastaturbedienung
- sichtbare Focus-States
- sinnvolle `aria-label`s bei Iconlinks
- `prefers-reduced-motion`
- keine Success-Zustände ohne echte Aktion

## 18. Aktive Dateien

Verbindliche Designquelle:

```text
styleguide.md
```

Technische CSS-Quellen:

```text
nurovelle-tokens.css
nurovelle-animations.css
```

Nicht als aktive Designquelle führen:

- alte Prompt-/Design-/Brief-Zwischenstände
- einzelne fremde CSS-Fragmente ohne Nurovelle-Namen
- doppelte Token-Dateien
- separate Animations-Referenz als dauerhafte Pflichtdatei
