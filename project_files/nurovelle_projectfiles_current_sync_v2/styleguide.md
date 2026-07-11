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

- Display / große Headlines: `Eastman Grotesque Alt`
- Fließtext, Navigation, Buttons, Formulare, Cards, Footer: `Inter`

Keine Rückkehr zu den alten Font-Stacks aus früheren Zwischenständen:

- Tapera / Tappera
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


## 7.1 Aktuelle Startseiten-Reihenfolge

Für die laufende Homepage-Umsetzung gilt die aktuell freigegebene Reihenfolge:

1. Hero
2. Über Nurovelle
3. Der erste Schritt zu Ihrem KI-Projekt
4. Sie haben bereits eine konkrete KI-Idee?
5. Kostenlose KI-Potenzialanalyse
6. KI-Leistungen von Nurovelle
7. Vom Geschäftsprozess zur KI-Lösung
8. Warum Nurovelle
9. Download-Bereich
10. Analyse-Seite / Formularweiterleitung
11. Success-/Error-Zustand in `analyse.html`

Diese Reihenfolge überschreibt ältere Zwischenstände, in denen die Potenzialanalyse vor der Projektidee stand. Neu ergänzt ist eine About-Nurovelle-Section direkt nach dem Hero. Projektidee steht vor Potenzialanalyse; die Potenzialanalyse kommt eine Sektion später.

### Section 2 – Über Nurovelle

Layout:

- links Video- oder Video-Preview-Fläche
- rechts Text
- keine neue Farbwelt
- CTA optional zu `analyse.html`

Text:

```text
ÜBER NUROVELLE
KI-LÖSUNGEN, DIE IN REALEN PROZESSEN FUNKTIONIEREN

Nurovelle entwickelt individuelle KI-Systeme, die sich an konkreten Geschäftsprozessen orientieren. Wir analysieren bestehende Abläufe, identifizieren sinnvolle Potenziale und setzen Lösungen um, die im Arbeitsalltag tatsächlich entlasten.

PROZESSE VERSTEHEN
Bestehende Abläufe, Engpässe und manuelle Arbeitsschritte werden systematisch analysiert.

POTENZIALE ERKENNEN
Wir prüfen, wo KI, Automatisierung oder intelligente Datenverarbeitung einen echten Nutzen schaffen.

INDIVIDUELL ENTWICKELN
Lösungen werden passend zu den vorhandenen Systemen, Anforderungen und Arbeitsweisen konzipiert.

NACHHALTIG INTEGRIEREN
Das Ergebnis sind nutzbare KI-Systeme, die Prozesse vereinfachen und langfristig weiterentwickelt werden können.
```

### Aktuelle Divider-Abfolge für die Live-Übersicht

- Hero → Section 2 „Über Nurovelle“: Divider A – SVG-Schräg-Divider / Separator
- Section 2 „Über Nurovelle“ → Section 3 „Der erste Schritt zu Ihrem KI-Projekt“: Divider A erneut
- Section 3 „Der erste Schritt zu Ihrem KI-Projekt“ → Section 4 „Sie haben bereits eine konkrete KI-Idee?“: Divider B normal
- Section 4 „Sie haben bereits eine konkrete KI-Idee?“ → Section 5 „Kostenlose KI-Potenzialanalyse“: Divider B reverse
- Section 5 „Kostenlose KI-Potenzialanalyse“ → Section 6 „KI-Leistungen von Nurovelle“: Divider C

Die Abfolge dient der Live-Prüfung und ist noch keine finale Auswahl einer einzigen Divider-Variante.

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


### Korrektur 2026-07-10 – Divider-A-Doppelprüfung

Für die aktuelle Live-Prüfung ist die Divider-Abfolge testweise. Variante A muss zweimal direkt nacheinander über aufeinanderfolgende Section-Übergänge dargestellt werden, damit ihre Wirkung im wiederholten Einsatz beurteilt werden kann. Erst nach Sichtprüfung wird festgelegt, welcher Divider tatsächlich verwendet wird.

Testabfolge:

1. Hero → Section 2: Divider A
2. Section 2 → Section 3: Divider A erneut
3. Section 3 → Section 4: Divider B normal
4. Section 4 → Section 5: Divider B reverse
5. Section 5 → Section 6: Divider C
