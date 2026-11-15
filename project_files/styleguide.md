# Nurovelle Styleguide

Stand: 2026-10-07  
Status: freigegeben

## Zweck dieser Datei

Diese Datei ist die **einzige fachliche Quelle für Design, visuelle Komponenten und Interaktionsstil**.

Technische Token werden in `nurovelle-tokens.css` gespiegelt.

Projektstruktur gehört in `project_overview.md`, technische Datenflüsse in `architecture.md`.

## 1. Designprinzip

Nurovelle nutzt eine dunkle, technische Premium-Optik:

- mattes Schwarz
- dunkles glänzendes Smaragdgrün
- Gunmetal
- Gold als hochwertiger Akzent
- kontrollierte Glas-/Metallwirkung
- technische B2B-Anmutung
- klare, ruhige Komposition

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Neon
- Bronze/Kupfer als eigenständige Hauptmaterialsprache
- Regenbogenverläufe
- generische KI-Roboter
- Sci-Fi-Konsolen
- Gaming-/Comic-Wirkung
- Casino-/Spielautomatwirkung

## 2. Farben

### Basis

- Schwarz: `#050706`
- Mattes Schwarz: `#080B09`
- Gunmetal: `#252B2C`
- Gunmetal dunkel: `#15191A`
- Deep Green: `#0A1913`
- Emerald: `#112B21`
- Emerald Highlight: `#163A26`
- Gold deep: `#a28557`
- Gold damped: `#ffbb54` 
- Gold warm: `#ff8f00`
- Gold glow: `#a4803f`
- Gold bright: `#C9B25F`


### Text

- Haupttext hell: `#F5F7F4`
- Sekundärtext: `#B9C3BD`
- Text auf Gold: `#050706`

## 3. Goldsystem

Gold wird für Premium-Akzente verwendet:

- CTA
- Rahmen
- aktive Zustände
- Hover-/Focus-Zustände
- Trennlinien
- Knotenpunkte
- technische Highlights
- Titel/Text-Highlights

### Goldrahmen

```css
linear-gradient(135deg, #AE8625, #F7EF8A, #gD2AC47, #EDC967)
```

### Goldtitel

```css
linear-gradient(135deg, #DFBD69, #926F34)
```

### Gold-CTA

```css
linear-gradient(135deg, #F9F295, #E0AA3E, #FAF398, #B88A44)
```

### Metallic-Gold Textverlauf

```css
linear-gradient(135deg, #C5A059 0%, #FDF0CD 50%, #D4AF37 100%)
```

Verwendung: Titel und hochwertige Text-Highlights.

### Goldwort-Regel

Die Regel unterscheidet nach Medium.

**Website:** Die Überschrift trägt den Goldverlauf über den **kompletten Text**. So ist die Homepage umgesetzt und so bleibt es.

**Alles andere** – Dokumente, Angebote, Verträge, Social-Beiträge, Newsletter: In einer Überschrift trägt **genau ein Wort** den Goldverlauf, das inhaltlich tragende. Der Rest der Zeile bleibt im Haupttextton.

- nie zwei goldene Wörter, nie eine ganze goldene Zeile
- das goldene Wort muss optisch Gewicht haben; ein kurzes Wort wirkt in einer langen Überschrift verloren
- findet sich kein tragendes Wort, wird die Überschrift gekürzt statt ein beliebiges Wort eingefärbt

Das Wort **Nurovelle** wird immer in Gold gesetzt, unabhängig vom Umfeld und Medium.

### Goldverlauf in Dokumenten

Dokumente verwenden **einen einzigen** Goldverlauf, nicht mehrere nebeneinander:

```css
linear-gradient(110deg, #B8933F 0%, #C9A659 50%, #A8842F 100%)
```

Drei Stufen, gleichmäßig. Der siebenstufige Website-Verlauf (`--gold-1`) springt mehrfach zwischen hell und dunkel; die Sprünge werden als Wellen quer durch die Wörter sichtbar, und die hellste Stelle landet je nach Textlänge zufällig – bei „Warum Nurovelle" mitten im Markennamen. Für Fließtext auf Papier ist das ungeeignet.

In E-Mails wird kein Verlauf verwendet: `background-clip:text` unterstützen Outlook und Gmail nicht, der Text bliebe unsichtbar. Dort gilt der Vollton `#A8842F`.

### CTA-Materialgold

Für die freigegebene haptische CTA-Materialwirkung:

```css
--cta-gold-dark: #A54E07;
--cta-gold-mid: #B47E11;
--cta-gold-light: #FEF1A2;
--cta-gold-core: #BC881B;
--cta-gold-border: #A55D07;
--cta-gold-inner-dark: #8B4208;
--cta-gold-inner-mid: #B17D10;
--cta-gold-highlight: #FAE385;
--cta-gold-text-dark: #783205;
--cta-gold-material: linear-gradient(160deg, #A54E07, #B47E11, #FEF1A2, #BC881B, #A54E07);
```

Die Wirkung bleibt hochwertig und ruhig. Kein übertriebener Glanz.

## 4. Typografie

Aktive Website-Schriften:

- Display / große Headlines: `Exo 2`
- Fließtext, Navigation, Buttons, Formulare, Cards und Footer: `Inter`

Beide sind variable TrueType-Schriften unter der Open Font License und seit 2026-08-14 systemweit installiert (`/usr/local/share/fonts/nurovelle/`), inklusive aller Schnitte von Thin bis Black. Für die Website sind sie zusätzlich als Webfont einzubinden – siehe `todo.md`.

Es gibt kein zweites Fontsystem. Ältere Stacks sind abgelöst; die Historie steht in `decision_log.md`.

## 5. Layout

- maximale Inhaltsbreite: `75rem`
- Seitengutter über Token `--page-gutter`
- großzügige, aber konsistente Section-Abstände
- Section-Separator und Titel nicht unnötig weit auseinander
- keine individuellen Abstands-Overrides, wenn eine zentrale Regel zuständig ist
- Mobile wird aus demselben Layoutsystem responsiv reduziert

## 6. Section-Hintergründe

- Homepage `index.html`: einheitlicher Deep-Green-/Emerald-Grundhintergrund `#0A1913` über alle Inhaltssektionen; kein Wechsel zwischen mehreren Schwarz-/Grüntönen.
- Detailseiten: einheitlicher matter, fast schwarzer Grundhintergrund `#080B09`.
- Header und Footer dürfen ihre bestehende dunkle Systemfläche behalten.
- Gunmetal dient als Card-/Technikfläche, nicht als wechselnder Section-Hintergrund.
- keine hellen Vollflächen
- keine Stockfoto-Hintergründe
- Gold niemals als großflächiger Section-Hintergrund

## 7. Header

Aufbau:

- Logo links
- drei Breadcrumb-Bereiche im Header
- Breadcrumbs ersetzen die klassische Navigation
- Submenüs öffnen per Hover; Tastaturzugang muss erhalten bleiben
- Analyse-CTA rechts
- Hamburger/Sidebar-Steuerung gemäß bestehender freigegebener Struktur

Breadcrumbs:

- Chevron-/Pfeilsegmente
- semantische Navigation
- aktueller Punkt klar sichtbar
- Hover/Focus/Active im Nurovelle-System

## 8. Sidebar

- bestehende freigegebene Grundstruktur beibehalten
- keine neue Informationsarchitektur ohne Auftrag
- Öffnen/Schließen über Hamburger
- keine Überlagerung des eigentlichen Seiteninhalts
- auf mobilen Breakpoints sauber aus dem Layout nehmen oder als freigegebenes Overlay führen

## 9. Hero

Hero-Visual:

- bestehender freigegebener Cube/Würfel
- keine Texte, Labels, Zahlen oder Logos im Bild
- dunkles Gunmetal / Smaragd / Gold-Highlights

Animation:

- Partikel-Orb hinter dem Cube
- Originalquelle: SCSS/HAML-Partikel-Orb mit `.wrap` und 300 `.c`-Partikeln
- Cube selbst nicht unkontrolliert bewegen
- goldene Eck-/Knotenpunkte dürfen dezent pulsieren
- ruhiger technischer Lichtimpuls
- `prefers-reduced-motion` berücksichtigen

## 10. CTAs

Es gibt zwei visuelle CTA-Varianten:

1. Full Gold
2. Gold Outline

Beide verwenden dieselbe Interaktionslogik:

- rechter Pfeil initial sichtbar
- linker Pfeil initial außerhalb
- Hover/Focus: rechter Pfeil verlässt den Button
- linker Pfeil fährt ein
- Text verschiebt sich kontrolliert
- Circle-Fill expandiert
- Active/Klick: gesamte Buttonfläche drückt sich haptisch ab
- Materialwirkung aus dem CTA-Goldsystem

Nicht verwenden:

- generische Flat Buttons
- einfache Standard-Gold-Pills ohne die freigegebene Interaktion
- zusätzliche Buttonvarianten ohne Freigabe

## 11. Download-Button

Zustände:

1. Idle
2. Loading/Aktion
3. Success – größere Bestätigungsfläche
4. Error/Retry

Success darf nur nach echter erfolgreicher Aktion gezeigt werden.

## 12. Cards

### Homepage-Leistungskarten

Struktur:

- Icon mit Rahmen
- Trennlinie
- Nummer mit eigenem Rahmen
- Titel
- Untertitel
- maximal vier Bulletpoints
- `Mehr erfahren`

Keine langen Detailseiten-Texte auf Homepage-Cards.

Interaktion:

- gesamte Karte bewegt/rotiert/flipt als Einheit
- interne Elemente bewegen sich nicht unabhängig voneinander
- Card bleibt an ihrer Layoutposition
- Desktop: Hover/Focus
- Mobile: Tap/Focus
- Reduced-Motion-Fallback

### Weitere Card-Systeme

- normale dunkle Cards verwenden einheitlich Dark Gunmetal `#15191A` / `--color-gunmetal-dark`
- ausdrücklich grüne Cards behalten ihre freigegebene Emerald-/Green-Fläche
- ausdrücklich goldene Cards behalten ihre freigegebene Gold-Fläche
- Problem-/Lösungs-Cards
- CSS-Cards
- Frosted-Glass/Overlay nur dort, wo ausdrücklich freigegeben oder noch als Prüfvariante geführt

## 13. Download-Cards

- vier schmale Cards in einer horizontalen Reihe im gemeinsamen Displaycontainer
- gleiche Breite
- kompakte Höhe
- vollständiger Goldgradient-Rahmen
- separater Goldgradient-Rahmen um das Dokument-Icon
- Titel
- kurze Beschreibung
- bestehender Download-CTA
- keine doppelten PDF/XLSX-Labels
- auf kleinen Screens horizontal scrollen statt ungefragt auf 2×2 umzubauen

Rahmenprinzip:

```css
background:
  linear-gradient(var(--color-gunmetal-dark), var(--color-gunmetal-dark)) padding-box,
  var(--gradient-gold-border) border-box;
border: 1px solid transparent;
```

## 14. Stepdiagramm / Workflow

- technisch-mechanische Modulwelt
- vorhandene freigegebene Module und Assets
- klare Stepdiagramm-Anordnung
- keine zusätzlichen erfundenen Schritte
- keine Texte innerhalb von Modulbildern
- Module können eine konsistente Basis / ein Pedestal erhalten, wenn dies bereits freigegeben ist
- keine separate Erklär-Card pro Schritt

Zulässige Bildsprache:

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

## 15. Divider

Divider sind Bestandteil des Systems, finale konkrete Variante bleibt nur dann offen, wenn sie in `todo.md` noch als offen geführt wird.

Prüfvarianten:

- SVG-Schräg-Divider
- Pure-CSS-Angled-Sections
- Diagonal Box / SkewY + Clip-Path

Allgemein:

- HTML/CSS/SVG, nicht als Bild
- Nurovelle-Farben
- Content nie verzerren
- keine Inhalte verdecken
- kein horizontales Scrollen erzeugen
- responsive und reduced-motion beachten

## 16. Social Icons

- SVG / Inline-SVG / freigegebene Iconbibliothek
- nur Symbol sichtbar
- `aria-label` Pflicht
- keine Bildgenerierung
- dezenter Lift/Scale/Glow/Linienimpuls
- keine Bounce-/Comic-/Rainbow-Effekte

## 17. Bildstil / Nurovelle Assets

Alle neu erstellten Nurovelle-Bilder:

- transparenter Hintergrund
- dunkles glänzendes Smaragdgrün
- Gunmetal
- Gold-Highlights
- räumliche Form erhalten
- technische Glas-/Metallwirkung
- keine freien neuen Materialien
- keine Texte, Labels oder Logos, sofern nicht ausdrücklich beauftragt

Bestehende Formen nicht neu interpretieren.

### 17a. Bildstil für Social-Media- und Content-Posts

Ergänzt am 2026-09-06 (siehe `decision_log.md`), weil dieser Abschnitt bisher
nur Website-Assets abdeckte. Für Beiträge, die einen Ablauf oder eine
Fähigkeit zeigen sollen, gilt zusätzlich:

- **Keine Menschen, Hände oder Schreibtisch-/Büro-Fotografie.** Realistische
  Personenaufnahmen sind für generierte Post-Bilder ausdrücklich nicht
  freigegeben – unabhängig von Blickrichtung oder Bildausschnitt.
- Für einen Ablauf/eine Fähigkeit ist die in Abschnitt 14 bereits
  freigegebene technisch-mechanische Bildsprache (Mechanik, Schalter,
  Relais, Displays, Container, Terminals, Scanner, Speicher, Ventile,
  Verteiler, Kontrollmodule) die richtige Wahl – nicht nur für
  Stepdiagramme auf der Website, sondern ebenso für Einzelmotive in Posts.
- Die in Abschnitt 1 bereits ausgeschlossenen Motive (generische
  KI-Roboter, Sci-Fi-Konsolen, Gaming-/Comic-Wirkung) gelten hier ebenso.
- **Bekannte Generator-Falle:** ein Prompt, der eine *abstrakte
  Datenverbindung zwischen Systemen* als eigenständiges Motiv beschreibt
  („schwebende Symbole", „Verbindungslinien im Raum", „Datencontainer"),
  liefert bei den aktuell eingesetzten Bildgeneratoren zuverlässig
  genau die ausgeschlossene Sci-Fi-/Hologramm-Optik – auch wenn der
  Prompt sie ausdrücklich verbietet. Ein Verbot im Prompt reicht dort
  nachweislich nicht; das Motiv sollte stattdessen konkret aus der
  Modulwelt aus Abschnitt 14 heraus beschrieben werden, nicht abstrakt.
- **Richtungsreferenzen:** `austausch/an-team/vorlagen/nurovelle/` enthält
  seit 2026-09-06 zusätzliche Bilder (`1.png`–`16.png`,
  `reference_posting_*.png`). Das sind Stimmungs-/Richtungsreferenzen,
  keine fertigen Assets zum Nachbauen – einige zeigen fremde Markennamen,
  englischen Text oder Bildfehler (Wasserzeichen-Artefakte) und dürfen so
  nicht übernommen werden (vgl. Entscheidung „Referenzdateien sind keine
  eigenständigen Designquellen", 2026-07-02). Zwei Richtungen zeichnen sich
  ab: dunkle Server-/Rechenzentrums-Fotografie mit eingeblendeten
  Workflow-Panels (Data Ingestion → Model/Automation → Output) und
  Dashboard-Screens als Requisite im Bild – sowie Cluster aus dunklen
  Würfeln/Modulen mit goldener Kantenbeleuchtung und Zahnrädern, eine
  konkrete Ausführung der Modulwelt aus Abschnitt 14. Beide sind mit der
  bestehenden Farb-/Materialsprache vereinbar; ein verbindliches Einzelmotiv
  daraus steht noch aus.

## 18. Accessibility

Pflicht:

- Tastaturbedienung
- sichtbare Focus-States
- ausreichende Tap-Flächen
- semantische Links/Buttons
- `aria-label` bei Iconlinks
- `prefers-reduced-motion`
- Success-Zustände nur nach echter erfolgreicher Aktion

## 19. Technische Designquelle

`nurovelle-tokens.css` enthält die maschinenlesbaren Werte dieses Styleguides.

Bei Konflikt gilt:

1. explizite aktuelle Benutzervorgabe
2. dieser Styleguide
3. `nurovelle-tokens.css`
4. bestehender Produktionscode


## 20. Homepage Mobile-System

Für die produktive Homepage gilt Mobile als vorrangige Darstellungsprüfung.

- Mobile-Sektionen verwenden eine gemeinsame vertikale Abstandslogik statt sektionsweise abweichender Leerhöhen.
- Hero-Inhalt nutzt auf Mobile die verfügbare Inhaltsbreite; künstliche Wort- und Silbentrennung wird nicht verwendet.
- Der Hero-Kicker muss auf Mobile klar lesbar bleiben und darf nicht zur kaum sichtbaren Nebenbeschriftung schrumpfen.
- Normale Homepage-CTAs verwenden auf Mobile dieselbe bestehende goldene CTA-Optik wie die CTAs in den Analyse-Angebots-Cards; sie werden nur kompakt, schmal und einzeilig dimensioniert.
- CTA-Text bleibt auf Mobile einzeilig. Der Header-CTA ist die einzige separat dimensionierte Ausnahme.
- Die 3D-Module im Abschnitt „Vom Geschäftsprozess zur KI-Lösung“ werden auf Mobile deutlich kompakter dargestellt als auf Desktop.
- Echte Bulletpoint-Listen in Analysebereichen verwenden den grünen 3D-Punkt `assets/bulletpoint.png` statt goldener Quadratmarker.
- „Von der Idee zum Projekt“ zeigt auf Mobile alle vorhandenen Bild-/Text-Beispiele ohne leere Slider-Zwischenzustände.
- Video und zugehörige Bulletpoints in „Warum Nurovelle“ bleiben auf Mobile als zusammengehöriger Inhaltsblock mit engem, konsistentem Abstand.
- SEO-Toolbox-Hinweise dürfen auf der Homepage an zwei bis drei definierten Stellen als kompakte, nicht blockierende Callouts eingeblendet werden. Sie erscheinen beim Eintritt in den sichtbaren Bereich von links mit gleichzeitigem Fade-in; kein Scale-/Bounce-Effekt. Auf Mobile bleiben sie klar kleiner als die regulären Inhaltskarten. Kein Modal, kein Dauerblinken, kein neuer CTA-Stil.
- Normale Mobile-CTAs behalten die bestehende goldene CTA-Optik, werden aber mit reduziertem Innenabstand kompakt gehalten; der Header-CTA bleibt ausgenommen.

## 21. Detailseiten: verbindliche Masse

Gilt fuer die Leistungs- und Analysedetailseiten und ist die Vorlage fuer jede weitere Detailseite. Referenz ist `homepage/analyse.html`, Stand 2026-11-14, vom Nutzer festgelegt. Wer hier etwas aendert, traegt den neuen Wert hier ein.

Feste Werte stehen in Pixeln und gelten bei jeder Fensterbreite. Wo ein Wert von der Fensterbreite abhaengt, steht die Formel und zusaetzlich eine Wertetabelle. **Eine Zahl, die nur bei 1440 px gilt, ist keine Vorgabe.**

### 21.0 Container und Seitenraster

| Element | Wert |
| --- | --- |
| `--content-max` | 1560 px |
| `--side` (Seitenrand der Sektion) | `clamp(19.2px, 4.8vw, 96px)` |
| `.section-inner`, Breite | `min(100% - 2 x --side, 1560px)` |
| `.section` `padding-top`/`-bottom`, ab 901 px | 64 px |
| `.section` `padding-top`/`-bottom`, bis 900 px | 40 px |
| **Inhaltsbreite** | **1300 px, fest, mittig im `.section-inner`** |

Daraus ergibt sich:

| Fensterbreite | `--side` | `.section-inner` | Inhalt, 1300 mittig |
| --- | --- | --- | --- |
| 1440 px | 69 px | 69 .. 1371 (1302) | 70 .. 1370 |
| 1600 px | 77 px | 77 .. 1523 (1446) | 150 .. 1450 |
| 1920 px | 92 px | 180 .. 1740 (1560) | 310 .. 1610 |
| 2560 px | 96 px | 500 .. 2060 (1560) | 630 .. 1930 |

Ab 1920 px ist der `.section-inner` auf 1560 px gedeckelt und wandert nur noch mit. Die Einrueckung des Inhalts gegenueber dem Kopf betraegt dann 130 px je Seite.

### 21.1 Inhaltsbreite und Einrueckung

Grundregel: **Kicker, Headline und Subline sitzen an der linken Inhaltskante. Alles andere ist davon eingerueckt.** Das betrifft Karten, Bulletpoint-Listen und alle uebrigen Inhalte.

| Element | Wert |
| --- | --- |
| Kicker, Headline, Subline: linke Kante | Kante des `.section-inner` |
| Headline: Breite | volle `.section-inner`-Breite |
| Subline: `max-width` | 820 px |
| **Inhalt, Breite** | **1300 px, fest** |
| **Inhalt, Ausrichtung** | **mittig im `.section-inner`** |

Der Kopf darf **nicht** innerhalb einer Textspalte eines `media-split` stehen, sonst wandert er mit der Spalte. Verbindliches Muster, wie in `#leistungen`:

```html
<div class="section-inner">
  <div class="media-copy">kicker, h2, p.sub</div>
  <div class="media-split">...Inhalt...</div>
</div>
```

`media-split`-Zeilen bleiben mittig ausgerichtet. Das Bild sitzt auf halber Hoehe der Bulletpoint-Liste.

**Der Inhalt einer Sektion ist 1300 px breit und sitzt mittig im `.section-inner`.** Der Kopf aus Kicker, Headline und Subline sitzt an der Kante des `.section-inner`, also weiter aussen. Daraus entsteht die Einrueckung, die der Nutzer verlangt hat: Kopf aussen, alles danach eingerueckt.

Der `.section-inner` ist nicht fest, er waechst bis `--content-max: 1560px`. Deshalb ist **1300 px der verbindliche Wert, nicht 70 und 1370**. Diese beiden Zahlen sind nur das Ergebnis bei genau 1440 px Fensterbreite und taugen nicht als Vorgabe: eine Sektion ohne Begrenzung misst bei 1440 px ebenfalls 70 .. 1370 und faellt erst bei breiterem Fenster auf.

| Fensterbreite | `.section-inner` | Inhalt, 1300 mittig |
| --- | --- | --- |
| 1440 px | 69 .. 1371 | 70 .. 1370 |
| 1600 px | 77 .. 1523 | 150 .. 1450 |
| 1920 px | 180 .. 1740 | 310 .. 1610 |
| 2560 px | 500 .. 2060 | 630 .. 1930 |

Das gilt fuer jede Art von Inhalt: Karten, Bulletpoint-Listen, nummerierte Listen, `media-split`-Bloecke, Formularbloecke und das FAQ-Raster.

Umgesetzt wird es mit `width:100%`, `max-width:1300px` und `margin-left:auto; margin-right:auto` am Inhaltsblock. Ein Block ohne `max-width` waechst mit dem Fenster mit und ist dann zu breit.

Referenz ist die Definitionssektion: zwei Karten zu je 634 px mit 32 px Spalte, zusammen 1300 px. Am 2026-11-14 vom Nutzer festgelegt und an dieser Sektion gemessen.

Breite der einzelnen Inhaltsbausteine, fest bei jeder Fensterbreite:

| Baustein | Breite |
| --- | --- |
| Karte im Zweierraster (`.panel` in `#was-ist-das`) | 634 px, Spalte 32 px |
| Breites Einzelfeld (`.panel` in `#einsatzbereiche`) | 1300 px |
| Nummerierte Liste (`.num-list`) | 1300 px |
| Eintrag darin (`li`) | 622 px |
| Textspalte im `media-split` | 700 px |
| Bild im `media-split` | 544 px, Spaltenabstand 56 px |
| FAQ-Raster | 1300 px, Knopf 640 px |
| Formularblock (`.form-panel`) | 710 px |

**Pruefung nur bei 1440 px ist nicht aussagekraeftig.** Jede Breitenpruefung wird bei mindestens zwei Fensterbreiten gemessen, davon einer ueber 1560 px.

**Regel fuer diese Datei:** Hier stehen verbindliche Einzelwerte, keine Spannen und keine Beschreibungen des Ist-Zustands. Eine Spanne kann nichts pruefen. Werte, die noch nicht entschieden sind, werden als offen gekennzeichnet und nicht mit einer gemessenen Zahl kaschiert.

### 21.2 Bilder in Textsektionen

| Element | Wert |
| --- | --- |
| `.section-photo`, Breite ab 901 px | 544 px |
| daraus folgende Hoehe bei 4:3 | 409 px |
| Bildspalte im `media-split` | 544 px, fest |
| Spaltenabstand Text zu Bild | 56 px |
| Textspalte, daraus folgende Breite | 700 px |
| `.section-photo`, bis 900 px | volle Spaltenbreite |

In `#nutzen` steht das Bild links, das ist so gewollt und bleibt so.

Die Bildspalte ist auf genau 544 px gesetzt, nicht auf einen Bruchteil. Nur so sitzt das Bild an der Kante des 1300 px breiten Inhaltsblocks. Eine `fr`-Spalte macht die Spalte breiter als das Bild, das Bild bleibt dann linksbuendig darin stehen und die rechte Kante wird nicht erreicht.

Der `media-split` selbst traegt `width:100%`, `max-width:1300px` und `margin-left:auto; margin-right:auto`. Ohne diese Begrenzung waechst er mit dem Fenster mit; die Textspalte war dadurch bei 1920 px 959 px breit statt 700.

### 21.3 Modul-Icons in `.num-list`

| Element | Wert |
| --- | --- |
| `.module-icon-frame` | 54 x 54 px |
| `.module-icon` | 41 x 41 px |
| `.num-list li` `padding-left` | 83 px |
| Abstand Rahmenkante bis Text | 29 px |

Die drei Werte haengen zusammen: `padding-left` ist Rahmenbreite plus 29 px. Wird der Rahmen geaendert, ist der Einzug mitzuziehen.

### 21.4 FAQ

| Element | Wert |
| --- | --- |
| `.faq-grid` `max-width` | 1300 px |
| `.faq-grid` `margin` | `16px auto 0`, mittig |
| Spalten | 2, Abstand 16 px / 20 px |
| Breite je Knopf | 640 px, bei jeder Fensterbreite |
| Breitenbedarf des laengsten Knopfes | 535 px |
| Hoehe je Knopf | 44 px, einzeilig |

Das Raster ist auf 1300 px begrenzt und mittig gesetzt, wie jeder andere Inhaltsblock. Die Knoepfe muessen einzeilig bleiben. Kommen laengere Fragen dazu, ist der Bedarf neu zu messen; mehr als 640 px je Knopf gibt die Inhaltsbreite nicht her, dann muss die Frage kuerzer werden.

### 21.5 Trennlinien

Zwischen je zwei Sektionen steht genau ein `<div class="section-divider" aria-hidden="true"></div>`. Auf `analyse.html` sind das sieben Stueck: nach Hero, Definition, Ausgangslage, Leistungsumfang, Anwendung, Ihr Nutzen und Potenzialanalyse starten.

Die Linie ueber dem Footer ist keine `section-divider`, sondern `.footer::before` aus `shared-header-footer.css`.

| Element | Wert |
| --- | --- |
| `.section-divider`, Hoehe | 2 px |
| `.section-divider`, Aussenabstand | 0 |

**Offen:** Die Trennlinie folgt nicht der Inhaltsbreite von 1300 px. Gemessen 1238 px bei 1440 px Fensterbreite, 1651 px bei 1920 px und 774 px bei 900 px. Bei 1920 px ist sie damit breiter als der `.section-inner` von 1560 px. Ob die Linie auf 1300 px gesetzt wird, ist nicht entschieden und wurde deshalb nicht geaendert.

### 21.6 Hero

Die goldenen Eckenlinien oben rechts, frueher `svg.hero-corner-lines`, sind am 2026-11-14 entfernt worden. Markup und CSS sind geloescht, nicht nur ausgeblendet.

**Hero-Bild**

| Element | Wert |
| --- | --- |
| `#hero .visual-card--hero img` | `display:block; width:100%; max-width:100%; height:auto; max-height:none` |
| Transformationen | **keine** |
| feste Pixelbreiten | **keine** |
| `.hero-viewport` | `overflow-x:clip` |

Das Bild fuellt seine Rasterspalte und behaelt sein Seitenverhaeltnis. Groesse und Platzierung ergeben sich allein aus `#hero .detail-hero`, also aus `grid-template-columns` und `gap`.

**Verboten: `transform: scale()` zum Vergroessern des Hero-Bildes.** Eine Transformation aendert nur die Darstellung, nicht den Platz im Layout. Das Raster rechnet weiter mit der deklarierten Breite, das Bild laeuft aus dem Fenster und wird abgeschnitten. Genau daran ist die frueher Fassung gescheitert: `width:760px` mit `scale(1.6)` ergab einen 1216 px breiten Kasten und bei 1440 px Fensterbreite 290 px Ueberlauf. Soll das Bild groesser werden, wird die Spalte breiter gemacht, nicht das Bild skaliert.

`overflow-x:clip` an `.hero-viewport` ist noetig, weil der dekorative Schein `#hero .visual-card--hero::before` mit `inset:-16% -19%` ueber die Kartenkante hinausreicht. Ohne das Abklemmen erzeugt eine reine Dekoration eine waagerechte Scrollleiste. `clip` statt `hidden`, damit kein Scrollcontainer entsteht.

Gemessenes Ergebnis, Bild stets im Seitenverhaeltnis 1,777:

| Fensterbreite | Bild | Ueberlauf der Seite |
| --- | --- | --- |
| 390 px | 354 x 199 | 0 |
| 900 px | 864 x 486 | 0 |
| 1100 px | 479 x 270 | 0 |
| 1440 px | 631 x 355 | 0 |
| 1920 px | 760 x 428 | 0 |

**Headline und Bild ueberlappen, die Headline liegt davor.** Ab 1101 px teilt `#hero .detail-hero` haelftig, `minmax(0,1fr) minmax(0,1fr)` mit 40 px Abstand. Die Headline traegt `width:max-content` und laeuft dadurch ueber ihre Spalte hinaus ins Bildfeld. Die Textspalte traegt `z-index:3`, das Bild `z-index:1`, die Schrift liegt also vor dem Bild. So bekommt das Bild die volle halbe Breite, ohne dass die Headline umbrechen oder kleiner werden muss.

| Element | Wert |
| --- | --- |
| `#hero .detail-hero`, ab 1101 px | `minmax(0,1fr) minmax(0,1fr)`, `gap:40px` |
| `#hero .detail-hero>div:first-child` | `position:relative; z-index:3` |
| `#hero h1` | `width:max-content; max-width:none` |
| `#hero .lead` | `max-width:none` |
| Schriftgrad der Headline | unveraendert `--t-sektionstitel`, `clamp(40px, 4.6vw, 72px)` |

Der Zeilenumbruch der Headline ist redaktionell gesetzt und steht im Markup: Zeile 1 `Wo lohnt sich KI in Ihrem Unternehmen`, Zeile 2 `wirklich?`. Beide Zeilen sind `span.hero-title-line` mit `white-space:nowrap` oberhalb von 1100 px. Der Wortlaut bleibt unveraendert, nur die Umbruchstelle ist gesetzt.

Keine festen Pixelbreiten fuer Textspalte oder Lead. Die frueheren Werte `minmax(780px,1.35fr)` am Raster und `max-width:760px` am Lead sind entfernt; sie hielten die Textspalte unabhaengig vom tatsaechlichen Bedarf bei 760 bis 787 px und druckten das Bild auf 460 px.

### 21.7 Mobil, bis 900 px Fensterbreite

| Element | Wert |
| --- | --- |
| `--side` | 18 px bei 390 px, nach der Formel `clamp(19.2px, 4.8vw, 96px)` |
| `.section` `padding-top`/`-bottom` | 40 px |
| Inhaltsbreite | volle Breite des `.section-inner`, keine 1300-px-Begrenzung |
| `media-split` | einspaltig, Bild ueber dem Text |
| FAQ-Raster | einspaltig |

Die feste Inhaltsbreite von 1300 px greift nur ab 901 px. Darunter fuellt jeder Inhaltsblock den `.section-inner`, weil dieser ohnehin schmaler als 1300 px ist.

Umbruchpunkte der Seite: **901 px** (Desktop-Block `@media(min-width:901px)`), **900 px** und **640 px**.

**Offen:** Unterhalb von 1280 px werden einzelne FAQ-Knoepfe zweizeilig, bei 1100 px einer, bei 1000 px drei. Nicht entschieden, ob das Raster dort einspaltig wird oder die Fragen gekuerzt werden.
