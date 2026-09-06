# Nurovelle Styleguide

Stand: 2026-09-06  
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
- Gold damped: `#C5B358` 
- Gold warm: `#ad8047`
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
linear-gradient(135deg, #AE8625, #F7EF8A, #D2AC47, #EDC967)
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

- Wechsel zwischen mattem Schwarz und sehr dunklem Grün/Smaragd
- Gunmetal als technische Fläche oder Tiefe
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

- schwarze Cards
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
  linear-gradient(var(--color-black), var(--color-black)) padding-box,
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
