# Nurovelle Styleguide

Stand: 2026-07-31  
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

- Hero-Orb kommt hinter den bestehenden Cube / Würfel
- Originalvorgabe ist die SCSS/HAML-Partikel-Orb-Animation mit `.wrap` und 300 `.c`-Partikeln
- goldene Cube-Ecken dürfen dezent pulsieren
- ruhiger technischer Lichtimpuls
- keine unkontrollierte Bewegung des gesamten Hero-Visuals
- keine freie Conic-/Noise-Mask-Interpretation als Ersatz für die Original-Orb-Vorgabe

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

Divider werden auf der Homepage verbindlich eingesetzt.

Die finale Divider-Form ist noch nicht freigegeben und muss live beurteilt werden. Aktive Prüfvarianten:

- Variante A: SVG-Schräg-Divider / Separator
- Variante B: Pure-CSS-Angled-Sections
- Variante C: Diagonal Box / SkewY + Clip-Path

Für Variante A liegt die Nutzerreferenz separat als `nurovelle-divider-svg-original-reference.txt` vor.
Für Variante B liegt die Nutzerreferenz separat als `nurovelle-divider-pure-css-angled-original-reference.scss` vor.
Für Variante C liegt die Nutzerreferenz separat als `nurovelle-divider-diagonal-original-reference.txt` vor.

Regeln für alle Divider:

- Divider sind Pflichtbestandteil der Homepage, aber die konkrete Variante bleibt Prüfentscheidung.
- Umsetzung per HTML/CSS/SVG, nicht als Bild, GIF oder Video.
- Keine Demo-Farben übernehmen.
- Keine Demo-Texte, fremden Links, Playground-Controls oder Beispielseitenstruktur übernehmen.
- Farben ausschließlich aus dem Nurovelle-System ableiten: mattes Schwarz, sehr dunkles Petrol/Smaragd, Gold nur als feiner Akzent.
- Divider dürfen Inhalte, CTAs, Cards, Text und Hero-Visuals nicht verdecken.
- `overflow-x: hidden` darf kontrolliert eingesetzt werden, um horizontales Scrollen durch breite oder gedrehte Divider zu verhindern.
- Desktop, Tablet und Mobile müssen geprüft werden.

Regeln für Variante A:

- SVG sitzt als absolut positionierter Separator am unteren Section-Rand.
- SVG nutzt `preserveAspectRatio="none"`, damit die schräge Fläche über volle Breite skaliert.
- Mobile darf mit breiterem SVG und leichter Rotation geprüft werden.
- Demo-Grün aus der Referenz wird nicht übernommen.

Regeln für Variante B:

- Section-Kanten dürfen über `clip-path: polygon(...)` angeschnitten werden.
- CSS-Trigonometrie (`tan()`, `cos()`, `atan2()`) darf nur als progressive Enhancement mit Fallback geprüft werden.
- SCSS-Winkelwerte müssen mit Guardrails begrenzt werden.
- `@property`-Fallbacks für Winkel, Abstand und Hypotenuse dürfen geprüft werden.
- Content, Text, Cards, CTAs und Hero-Visuals dürfen nicht verzerrt oder aus dem sicheren Bereich gedrückt werden.
- Demo-Fonts, Demo-Verläufe, Support-Infoboxen, Code-Demos, Linkeffekte und Footer-Lochmuster werden nicht übernommen.

Regeln für Variante C:

- `skewY()` nur auf Hintergrund-/Pseudo-Elemente anwenden.
- Content, Text, Cards, CTAs und Hero-Visuals bleiben unverzerrt.
- Winkel-/Padding-Berechnung darf geprüft werden.
- `clip-path` darf geprüft werden.

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
- Hero Orb hinter Cube — Originalvorgabe SCSS/HAML, Adaption nur nach Freigabe
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

---

## 19. CSS-First-Regel und Prüfkomponenten – Nachtrag 2026-07-07

Für kontrollierbare Website-Elemente gilt CSS-first.

Das betrifft insbesondere:

- Navigation neu bewerten
- Burger-Menü
- Breadcrumbs
- Social Buttons
- Hero-Animation hinter dem Cube / Cube-Entstehungseffekt
- alternative Hero-Hintergrundvariante mit Conic-/Noise-Maske
- Divider-System
- SVG-Schräg-Divider
- Pure-CSS-Angled-Sections
- Diagonal Box / SkewY + Clip-Path
- Card-Interaktionen
- Frosted-Glass-/Overlay-Card als Prüfvariante
- Section-/Board-Referenz
- Dashboard-/Board-Komponente als Prüfvariante
- CTA-Button-System
- Arrow-Reveal
- Press-Button-Logik
- Golden-Button-Farblogik
- Downloadbutton → größerer Danke-/Bestätigungsbutton

Regel:

- Originalreferenzen werden separat gesichert.
- Nurovelle-Adaptionen werden klar als Adaptionen gekennzeichnet.
- Demo-Farben, Demo-Texte, externe Demo-Assets, React-/styled-components-Pflichten und fehlerhafte ARIA-Bezeichnungen werden nicht übernommen.
- Finale Nutzung erst nach Live-Prüfung und Freigabe.

## 20. CTA-Button-System – Nachtrag 2026-07-07

Die Button-Referenzen liegen zusätzlich separat vor:

```text
nurovelle-button-original-references.md
```

Für das Nurovelle-CTA-System gilt:

- Arrow-Reveal / Circle-Fill ist die Start-CTA-Logik.
- Press-Button ist die haptische Klick-/Active-Logik.
- Golden-Button-Farblogik liefert die Material-/Farbgrundlage.
- Es wird nur die Logik der Referenzen übernommen, nicht deren Demo-Farben oder Demo-Struktur.
- React und styled-components sind keine Pflicht.
- Die finale Website-Umsetzung erfolgt als HTML/CSS/JS-Komponente.

## 21. Section-/Board-Option – Nachtrag 2026-07-07

Die CodePen-Referenz `https://codepen.io/josephrexme/pen/oNNpZYJ` ist als Option für eine Section-/Board-Komponente aufgenommen.

Status:

- Prüfvariante
- nicht final
- keine 1:1-Übernahme

Ausgeschlossen:

- Demo-Texte
- Demo-Farben
- Demo-Logo
- Finanz-/Wallet-Kontext
- externe Bild-URLs
- fehlerhafte `arial-label`-Schreibweise

Verbindlich bei Adaption:

- `aria-label` korrekt setzen
- Nurovelle-Farbsystem verwenden
- Focus-/Hover-Zustände prüfen
- Mobile und Desktop prüfen

## 20. Referenzcode-Archiv / übernommene Zusatzdateien

Status: aktiv als Dokumentationsregel seit 2026-07-07

Die zuvor separat erzeugten 8 Arbeits-/Referenzdateien wurden in die Projektfiles übernommen. Maßgebliche Sammelstelle ist:

```text
NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md
```

Dort liegen die Originalreferenzen und Arbeitsstände als Archivanhang.

Verbindliche Trennung:

- Originalreferenz: unverändert dokumentierter Ausgangscode oder Arbeitsstand.
- Nurovelle-Adaption: abgeleitete Umsetzung mit Nurovelle-Farben, Klassen und Regeln.
- Prüfvariante: noch nicht final freigegeben.
- Produktionscode: erst nach Sichtprüfung und ausdrücklicher Freigabe.

Die ehemaligen Einzeldateien sind nicht als eigenständige aktive Designquellen zu behandeln. Sie dienen nur noch als Ursprung der übernommenen Archivblöcke.


---

## Verbindlicher Homepage-Stand – 2026-07-14

Status: freigegeben

Diese Festlegung ersetzt abweichende ältere Homepage-Strukturen und Textstände in dieser Datei. Ältere Angaben zu Trust-Bereich, klassischer Navigation, zusätzlichem SEO-Bereich als aktuelle Sektion, ausführlichen Prozesskarten oder einer anderen Sektionsreihenfolge dürfen nicht mehr verwendet werden.

### Header

- Breadcrumbs ersetzen die klassische Navigation vollständig.
- Der Header enthält genau drei Breadcrumbs mit Submenüs.
- Die Submenüs öffnen sich per Hover.
- Keine zusätzliche klassische Hauptnavigation.

### Verbindliche Homepage-Reihenfolge

1. Hero
2. Warum Nurovelle
3. Der erste Schritt zu Ihrem KI-Projekt
4. Sie haben bereits eine konkrete KI-Idee?
5. Branchen – optional, noch nicht final entschieden
6. Kostenlose KI-Potenzialanalyse
7. Formular
8. KI-Leistungen von Nurovelle
9. Vom Geschäftsprozess zur KI-Lösung
10. Download-Bereich
11. Kontakt
12. FAQ
13. Footer

Ein separater SEO-Bereich ist für einen späteren Ausbau vorgesehen und gehört nicht zur aktuell verbindlichen Reihenfolge.

### Hero

Kicker:

`INDIVIDUELLE KI-SYSTEME`

H1:

`KI-Agenten für echte Geschäftsprozesse.`

Subline:

`Nurovelle entwickelt individuelle KI-Systeme für Datenverarbeitung, Wissenszugriff, Prozessautomatisierung und Unternehmenssoftware.`

Zusatzzeile:

`Von der Potenzialanalyse über Prompt Engineering und MCP bis zur Umsetzung maßgeschneiderter KI-Lösungen.`

CTAs:

- `Kostenlose KI-Potenzialanalyse anfordern` → Potenzialanalyse
- `Unverbindliches Erstgespräch` → Kontaktbereich

Nicht verwenden:

- `Künstliche Intelligenz. Echte Ergebnisse.`
- `35+ Jahre Code`
- Trust-Aussagen im Hero
- Praxisleitfaden als zweiter Hero-CTA

### Warum Nurovelle

- Der Abschnitt benötigt eine Einleitung aus mindestens zwei bis drei Sätzen.
- Danach folgen fünf bis sechs konkrete Bulletpoints.
- Keine Trust-Kennzahlenleiste.
- Keine Unternehmensgeschichte.
- Keine unbelegten Erfahrungs- oder Leistungsversprechen.
- Der finale Wortlaut der Einleitung und Bulletpoints ist noch nicht freigegeben und darf nicht frei erfunden werden.

### Der erste Schritt zu Ihrem KI-Projekt

Einleitung:

`Ob erste Orientierung oder konkrete Projektidee: Wir prüfen Prozesse, Daten und technische Voraussetzungen und zeigen den passenden nächsten Schritt.`

Card 1:

**Prozess klären**

`Welcher Geschäftsprozess verbessert werden soll und welches konkrete Ergebnis durch KI entstehen muss.`

`Mehr erfahren`

Card 2:

**Daten prüfen**

`Welche Daten, Systeme und Wissensquellen bereits vorhanden sind und technisch nutzbar gemacht werden können.`

`Mehr erfahren`

Card 3:

**Umsetzung planen**

`Ob ein KI-Agent, ein Wissenssystem, Automatisierung oder individuelle Software der sinnvolle nächste Schritt ist.`

`Mehr erfahren`

CTA:

`Potenzialanalyse starten`

### Sie haben bereits eine konkrete KI-Idee?

Einleitung:

`Wir prüfen Machbarkeit, Datenlage und Integrationsaufwand, bevor unnötige Entwicklungs- oder Folgekosten entstehen.`

CTA:

`Projektidee prüfen lassen`

### Kostenlose KI-Potenzialanalyse

- Eigene Sektion vor dem Formular.
- Nicht mit dem Formular oder einer Trust-Section vermischen.
- Der finale vollständige Text dieser Sektion ist noch nicht freigegeben und darf nicht frei ergänzt werden.

### Formular

- Eigene Sektion direkt nach der Potenzialanalyse.
- Formular rechts, begleitende Card links.
- Pflichtfelder, Einwilligung, Datenschutz, Honeypot, Submission sowie Success-/Error-Logik bleiben erhalten.
- Der finale Text der linken Card ist noch nicht freigegeben.

### KI-Leistungen von Nurovelle

Jede Leistungskarte enthält:

- links oben ein Icon mit Rahmen
- rechts daneben einen Trennstrich
- eine Nummer mit eigenem Rahmen
- Titel und Untertitel
- eine mittig angeordnete Nummernkarte links neben dem Inhaltsbereich
- maximal vier Bulletpoints

Inhaltsregeln:

- Kein zusätzlicher Fließtext, der die Bulletpoints wiederholt.
- Keine weitere Text-Card auf der Leistungskarte.
- Titel, Untertitel und Bulletpoints dürfen denselben Inhalt nicht mehrfach ausdrücken.
- Keine vollständigen Detailseiten-Inhalte auf der Homepage.

### Vom Geschäftsprozess zur KI-Lösung

- Die bisherigen Prozesskarten mit Beschreibungstexten entfallen.
- Nur Module in der freigegebenen Stepdiagramm-Anordnung verwenden.
- Je Modul ausschließlich die Modulbezeichnung anzeigen.
- Keine Erklärungssätze, Bulletpoints oder zusätzlichen Cards.
- Kein CTA.

### Download-Bereich

- Eigene Sektion nach dem Stepdiagramm.
- Bestehende Downloads mit kurzen, nicht wiederholenden Beschreibungen.
- Finale Einzeltexte sind noch zu prüfen.

### Kontakt

- Eigene Kontaktsektion nach dem Download-Bereich.
- Nicht mit Potenzialanalyse oder Formular vermischen.
- Finale Kontakttexte sind noch zu prüfen.

### FAQ

- Abschnitt 12.
- Bestehende Fragen und Antworten nicht ungeprüft verändern.
- Finale FAQ-Texte sind gesondert zu prüfen.

### Footer

Verbindlicher Beschreibungstext:

`Individuelle KI-Systeme für reale Geschäftsprozesse.`

Keine lange Leistungsbeschreibung, Unternehmensgeschichte oder technische Erklärung im Footer.

### Textstatus

- Kein bisheriger vollständiger Sektionstext darf ungeprüft als final verwendet werden.
- Nur die in diesem Nachtrag wörtlich festgelegten Texte gelten als freigegeben.
- Fehlende Texte dürfen nicht selbstständig erfunden, ergänzt oder aus alten Dateien übernommen werden.

---

## Nachtrag 2026-07-31 – verbindlicher Umsetzungsstand

Dieser Nachtrag geht den Abschnitten oben vor, wo er ihnen widerspricht.

### Schriften

**Exo 2** für Titel, **Inter** für alles Übrige. Inter mit 400, 500, 550, 600, 650, 700, 750, 800.

### Typo-Rollen

Je Rolle eine Größe und ein Gewicht, als `--t-<rolle>` / `--w-<rolle>` in `:root`. Kein Element darf kleiner und zugleich schwerer sein als ein größeres.

sektionstitel clamp(48,7.5vw,100)/800 · hero-kennzahl 42/750 · kartentitel 36/750 · kennzahl 26/650 · subtitle 24/600 · zwischentitel 24/600 · bulletlabel 22/550 · fliesstext 20/400 · kartenbullet 20/500 · feldlabel 20/500 · wert 20/500 · formularfeld 20/400 · kicker-sektion 16/600 · bildunterschrift 16/500 · cta 16/600 · hero-statlabel 16/400 · kicker-karte 15/600

### Flächen

Zwei Sektionsfarben im Wechsel: `#050505` dunkel, `#010603` grün. Karte auf dunkel `#17251d`, Karte auf grün `#1a1a1a`, Elemente darauf `#17251d`. Kein `#000000`.

Die Basisflächen aus Abschnitt 2 (`#050706`, `#080B09`, `#0A1913`, `#112A20`, `#163A35`) sind damit ersetzt.

### Rahmen

Alle Rahmen über `--gold-3`, Doppel-Hintergrund-Technik wegen `border-radius`. Radien 8–12px, keine Pill-Form.

### Skalierung

`body { zoom: 0.8 }` — Werte im Stylesheet sind CSS-Pixel, gerendert wird das 0.8-fache. Hairlines brauchen 1.25px CSS.
