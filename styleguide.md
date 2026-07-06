# Nurovelle Styleguide

Status: Arbeitsfassung / konsolidierte Design- und Dokumentationsgrundlage  
Stand: 2026-07-02  
Geltung: Website, Detailseiten, Hero-Assets, Content-Dokumente, Guides, PDFs, Arbeitsdokumente und Download-Dokumente

---

## 1. Zweck

Dieser Styleguide bündelt die verbindlichen Gestaltungsregeln für Nurovelle.

Er dient als zentrale Referenz für:

- Homepage
- Detailseiten
- Hero- und Icon-Assets
- Download-Dokumente
- Guides
- PDFs
- Arbeitsdokumente
- Prompt-Bibliothek / Prompt-Guide
- Whitepaper
- Checklisten

Ziel ist eine konsistente Premium-Wirkung über Website, Assets und Dokumente hinweg.

---

## 2. Grundprinzip

Nurovelle wirkt:

- technisch
- hochwertig
- sachlich
- kontrolliert
- modern
- B2B-tauglich
- nicht verspielt
- nicht chaotisch futuristisch
- nicht generisch KI-lastig

Design unterstützt Inhalt und Conversion. Design ersetzt keine klare Botschaft.

---

## 3. Markenwirkung

### 3.1 Gewünschte Wirkung

Die Gestaltung soll folgende Wirkung erzeugen:

- Premium
- technische Kompetenz
- Kontrolle
- Klarheit
- Verlässlichkeit
- Business-Relevanz
- moderne KI- und Automatisierungslogik

### 3.2 Nicht gewünschte Wirkung

Nicht erlaubt sind:

- generischer KI-Hype
- bunte SaaS-Optik
- Neon-Look
- Sci-Fi-Kitsch
- überladene Dashboard-Szenen
- zufällige KI-Roboter
- Stockfoto-Ästhetik
- wechselnde Farbstile
- verspielt-futuristische Symbolik

---

## 4. Website-Farbsystem

Das Website-Farbsystem basiert auf dunklen technischen Flächen und goldenen Premium-Akzenten.

### 4.1 Primäre Website-Farben

| Name | Wert | Verwendung |
|---|---:|---|
| Black | `#050706` | tiefster Hintergrund |
| Matte Black | `#080B09` | Hauptflächen, Cards, dunkle Sektionen |
| Deep Green | `#0A1913` | dunkle grüne Grundfläche |
| Emerald | `#112A20` | Akzentflächen, technische Tiefe |
| Dark Teal | `#163A35` | kontrollierte Petrol-/Teal-Akzente |
| Text Light | `#F5F7F4` | heller Haupttext auf dunklem Grund |
| Text Muted | `#B9C3BD` | sekundärer Text auf dunklem Grund |

### 4.2 Goldverläufe Website

```css
--gold-1: linear-gradient(135deg, #AE8625, #F7EF8A, #D2AC47, #EDC967);
--gold-2: linear-gradient(135deg, #DFBD69, #926F34);
--gold-3: linear-gradient(135deg, #F9F295, #E0AA3E, #FAF398, #B88A44);
--gold-text-alt: linear-gradient(135deg, #C5A059 0%, #FDF0CD 50%, #D4AF37 100%);
```

Gold wird eingesetzt für:

- CTA-Buttons
- Rahmen
- aktive Zustände
- Hover-Effekte
- wichtige Highlights
- Divider-Lines
- feine Kanten
- Premium-Akzente

Gold wird nicht flächig als dominierende Hintergrundfarbe verwendet.

### 4.3 Website-Hintergründe

```css
--bg-green-1: linear-gradient(135deg, #0A1913 0%, #112A20 50%, #1D4234 100%);
--bg-green-2: linear-gradient(180deg, #071412 0%, #163A35 100%);
```

Erlaubt:

- matte schwarze Flächen
- sehr dunkles Petrol
- dunkle grün-schwarze Verläufe
- dezente technische Lichtdetails
- kontrollierte smaragdgrüne Linien

Nicht erlaubt:

- helle Vollflächen als neuer Hauptstil
- cyanfarbene Akzente
- blaue Hauptakzente
- violette Glows
- Bronze
- Kupfer
- bunte Verläufe
- Neonfarben

---

## 5. Website-Typografie

| Element | Schrift | Desktop | Mobile | Regel |
|---|---:|---:|---:|---|
| H1 | Bebas Neue | 64–88 px | 42–56 px | große Hero-/Titelwirkung, All Caps möglich |
| Section-H2 | Bebas Neue | 44–60 px | 34–42 px | Goldverlauf oder hell auf dunkel |
| H3 / Card-Titel | Anca Coder / Coder Pro | 18–24 px | 17–21 px | technische Labels und Card-Titel |
| Body | Raleway oder Roboto | 17–19 px | 16–18 px | gut lesbar, keine zu engen Zeilen |
| Label / Zahlen | Anca Coder / Coder Pro | 12–15 px | 12–14 px | technische Akzente |
| Button | Raleway oder Roboto | 15–17 px | 15–16 px | klar, klickbar, nicht verspielt |

### 5.1 Font-Fallbacks

```css
font-family: 'Bebas Neue', Impact, sans-serif;
font-family: 'Anca Coder', 'Coder Pro', monospace;
font-family: 'Raleway', 'Roboto', Arial, sans-serif;
```

---

## 6. Website-Komponenten

### 6.1 Buttons

#### Primärbutton

- Goldverlauf `--gold-3`
- dunkle Schrift oder sehr dunkles Grün/Schwarz
- Pill-Form
- klarer Hover-Zustand
- keine Neonanimation
- keine zufälligen Farbwechsel

#### Sekundärbutton

- transparenter Hintergrund
- Goldrahmen
- helle Schrift
- Hover: dezente goldene Fläche oder kontrollierter Goldglow

### 6.2 Cards

Cards verwenden:

- dunkle matte Fläche
- dezenter grüner Rahmen oder dunkler Glasrahmen
- klare Innenabstände
- keine langen Fließtexte in Leistungs-Cards
- Gold nur für Akzente, Linien, Hover, CTA oder Highlights

Nicht erlaubt:

- Goldrahmen um jede Card, sofern nicht explizit freigegeben
- helle Card-Flächen als neuer Hauptstil
- überladene Card-Inhalte
- zufällige Icon-Stile

### 6.3 Leistungs-Cards

Normalzustand:

- Icon
- Überschrift

Hover-/Tap-Zustand:

- Bausteine
- Anwendungen
- Kostenfaktor / Nutzen

Desktop:

- Hover öffnet vollständige Card.

Mobile:

- Tap öffnet vollständige Card.
- Zweiter Tap oder Tap auf andere Card schließt vorherige Card.
- Nur ein geöffneter Zustand gleichzeitig erforderlich.

---

## 7. Website-Layoutregeln

### 7.1 Maximalbreite und Abstände

```css
--max-width: 1200px;
--section-padding-desktop: 120px 24px;
--section-padding-tablet: 88px 24px;
--section-padding-mobile: 64px 18px;
--radius-card: 18px;
--radius-button: 999px;
```

### 7.2 Breakpoints

| Breakpoint | Regel |
|---|---|
| ab 1200 px | Desktop-Layout mit maximaler Breite `1200px` |
| 900–1199 px | Tablet: Grids auf 2 Spalten reduzieren |
| unter 900 px | Hero und Text-/Bild-Sektionen stapeln |
| unter 640 px | Cards einspaltig, CTAs untereinander, ausreichende Tap-Flächen |

### 7.3 Mobile Mindestregeln

- Buttons mindestens 44 px hoch.
- Keine abgeschnittenen Card-Inhalte.
- Leistungs-Cards per Tap öffnen.
- CTAs dürfen nicht zu eng stehen.
- Formular- und Success-/Error-Zustände müssen mobil lesbar sein.

---

## 8. Hero- und Bildasset-Regeln

### 8.1 Allgemein

Hero- und Modulassets dienen als technische Visuals. Texte, Labels und Website-Komponenten werden bevorzugt per HTML/CSS gesetzt.

### 8.2 Verbindliche Regeln für Hero-Grafiken

Nicht erlaubt:

- Texte
- Labels
- Zahlen
- Logos
- lesbare UI-Texte
- überladene Dashboards
- Sci-Fi-Konsolen
- wechselnde Farbstile
- Cyan
- Blau
- Violett
- Bronze
- Kupfer
- weiße Plattformen als neues Hauptdesign
- generische KI-Roboter
- Stockfoto-Optik

Erlaubt:

- matte schwarze Hauptflächen
- sehr dunkles Petrol
- dezente smaragdgrüne technische Details
- Gold nur als feiner Premium-Akzent
- abstrakte Systemarchitektur
- Module, Kammern, Glasröhren, technische Linien

### 8.3 CSS-Board-Regel

Boards, Panels, spätere Texte und Darstellungsflächen werden bevorzugt per HTML/CSS umgesetzt.

Grund:

- Höhe frei steuerbar
- Texte sauber kontrollierbar
- Panels responsive steuerbar
- keine KI-Zufallsbeschriftungen
- konsistente Darstellung auf Homepage und Detailseiten

Bildassets liefern nur technische Module und abstrakte Systemelemente.


### 8.5 Hero-Cube-Hintergrundanimation – Prüfvarianten

Die Hero-Animation für den Startseiten-Cube ist **noch nicht final freigegeben**. Es werden zwei CSS-first-Varianten geprüft.

#### Variante A – Partikel-Orb

Mögliche Nutzung:

- hinter dem Cube als räumliche Tiefe
- alternativ als kurzer Entstehungs-/Aufbau-Effekt des Cubes

Regeln:

- Cube bleibt Hauptmotiv.
- Text und CTAs bleiben oberste Ebene.
- Keine bunte Neon-/Regenbogenwirkung.
- Zulässige Lichtwirkung: warmes Gold, dunkles Emerald, sehr dezentes Rotgold nur als Übergang.
- Nicht zulässig: Cyan, Blau, Violett, grelle Neonfarben, überladene Partikelwolken.
- `pointer-events: none;` für den Animationslayer.
- `prefers-reduced-motion: reduce` reduziert oder deaktiviert Bewegung.
- Mobile/Low-Power: Partikelanzahl reduzieren oder Animation abschalten.

#### Variante B – Maskierter Conic-/Noise-Lichteffekt

Mögliche Nutzung:

- als ruhiger technischer Licht-/Punkt-Hintergrund hinter dem Cube
- ohne Textbestandteile
- als Alternative zum Partikel-Orb, falls dieser zu unruhig wirkt

Regeln:

- Beispiel-Text/`h1` aus der Vorlage nicht übernehmen.
- Keine externen CodePen-Font-Abhängigkeiten übernehmen.
- Externe Noise-/Masken-Datei lokal speichern oder durch eigenes lokales Asset ersetzen.
- Farbigkeit auf Nurovelle reduzieren: Gold, dunkles Emerald, warmes Licht, sehr dunkle Basis.
- Rot, Blau, Cyan, Türkis und Regenbogenwirkung aus der Originalvorlage entfernen.
- Browserunterstützung für `mask` / `mask-composite` prüfen.
- `prefers-reduced-motion` berücksichtigen.

#### Prüfentscheidung

Final wird erst nach visueller Prüfung entschieden, ob verwendet wird:

1. Partikel-Orb hinter dem Cube.
2. Partikel-Orb als Entstehungseffekt.
3. Maskierter Conic-/Noise-Hintergrund.
4. Eine reduzierte Kombination, sofern Performance und Lesbarkeit eindeutig besser sind.


### 8.4 Bildserien

Für weitere Hero- und Icon-Assets gilt:

- keine freie Neuinterpretation
- keine neuen Formen ohne Auftrag
- keine Stiländerung ohne Auftrag
- keine Prompt-Umformulierung ohne dokumentierte Freigabe
- bei Bildserien nur eine Variable ändern: Form oder konkretes Motiv
- zuerst ein Test-Asset prüfen, dann Serienumsetzung entscheiden

---

## 9. Detailseiten-Layout

Für Detailseiten gilt eine gemeinsame Vorlage.

### 9.1 Verbindliche Reihenfolge

1. Hero
2. Was ist ...?
3. Warum ist ... wichtig / entscheidend?
4. Unsere Lösungen / Leistungen für ...
5. Steigerung von ... durch ...
6. Ihr Nutzen von ...
7. Typische Einsatzbereiche
8. Was damit möglich wird
9. FAQ
10. Erstgespräch-CTA mit Portraitkarte

### 9.2 Layoutregeln je Abschnitt

| Abschnitt | Layoutregel |
|---|---|
| Punkt 2 | nur Überschrift und Blocktext |
| Punkt 3 | schwarze Cards |
| Punkt 4 | Problem-/Lösungs-Cards |
| Punkt 5 | CSS-Cards |
| Punkt 6 | CSS-Cards |
| Punkt 7 | wie Homepage |
| Punkt 8 | wie Card auf Homepage |
| Punkt 10 | rechteckige Kontaktkarte mit rundem Portrait, Social-Media-Icons und Kontaktdaten |

### 9.3 Entfernte Detailseiten-Elemente

Nicht als Standardsektion verwenden:

- Für wen geeignet
- So läuft die Zusammenarbeit

Grund:

- Besucher sollen nicht vorsortiert oder ausgeschlossen werden.
- Zusammenarbeit ist bereits auf der Homepage erklärt.

---

## 10. Content-Dokumente: eigenes Layoutsystem

Content-Dokumente, Guides, PDFs, Arbeitsdokumente und Download-Dokumente verwenden ein eigenes Typografie- und Farbsystem.

Website-Verläufe dürfen nicht ungeprüft auf Content-Dokumente übertragen werden.

### 10.1 Geltungsbereich

Dieses Dokumentlayout gilt für:

- Prompt Engineering Guide
- Prompt-Bibliothek
- Whitepaper
- Miniguides
- Checklisten
- Arbeitsdokumente
- PDF-Downloads
- Word-Dokumente
- Angebotsnahe Dokumente
- interne Dokumentationsunterlagen

### 10.2 Dokument-Farbpalette

| Name | Wert | Verwendung |
|---|---:|---|
| Deep Emerald | `#112A20` | H2, H4, Tabellenkopf, Bulletpoint-Header, starke Strukturflächen |
| Muted Matte Gold | `#B38F4D` | H3, Akzentüberschriften, dezente Hervorhebung |
| Gold Fallback | `#D4AF37` | H1-Fallback, Nummerierungsakzent, Premium-Akzent |
| Dark Bronze-Gold | `#A37A3E` | sehr starke Hervorhebung im Text |
| Dark Charcoal | `#2A2A2A` | normaler Fließtext |
| White | `#FFFFFF` | Text auf Emerald-Flächen |

### 10.3 Dokument-Typografie

| Element | Schrift | Größe | Farbe / Stil | Regel |
|---|---:|---:|---|---|
| H1 | Bebas Neue | ca. 26 pt | Gold Gradient / Fallback `#D4AF37` | Bold, All Caps |
| H2 | Plus Jakarta Sans | ca. 18 pt | Deep Emerald `#112A20` | Semi-Bold |
| H3 | Plus Jakarta Sans | ca. 14 pt | Muted Matte Gold `#B38F4D` | Medium |
| H4 | Plus Jakarta Sans | ca. 10.5 pt | Deep Emerald `#112A20` | Bold, All Caps |
| Column Header | Inter | ca. 10 pt | weiß auf Emerald-Block `#112A20` | Bold, All Caps |
| Body | Inter | 10.5 pt | Dark Charcoal `#2A2A2A` | Regular, Line Space 1.4 |
| Bulletpoint-Header | Plus Jakarta Sans | 12 pt | Deep Emerald `#112A20` | Semi-Bold |
| Bulletpoints | Inter | 10.5 pt | Text `#2A2A2A`, Bullet Dot Emerald | Regular |
| Numbering | Inter | 10.5 pt | Text `#2A2A2A`, Nummern Matte Gold | Regular |
| Hervorhebung normal | Inter | 10.5 pt | Deep Emerald `#112A20` | Italic oder Medium |
| Hervorhebung extrem | Inter | 10.5 pt | Dark Bronze-Gold `#A37A3E` | Extra-Bold |

### 10.4 Dokument-Layoutregeln

#### Seitenwirkung

Dokumente wirken:

- klar
- hochwertig
- sachlich
- lesbar
- strukturiert
- professionell
- nicht wie eine Website-Kopie

#### Grundlayout

- helle oder neutrale Dokumentflächen sind erlaubt
- dunkle Emerald-Blöcke nur gezielt für Struktur und Tabellenköpfe verwenden
- Gold nur als Akzent, nicht als dominante Fläche
- keine überladenen Schatten
- keine Website-Glow-Effekte
- keine großflächigen dunklen Verläufe ohne gesonderte Freigabe

#### Textfluss

- kurze Absätze
- klare Zwischenüberschriften
- strukturierte Bulletpoints
- Tabellen für Vergleichs- und Prozessinformationen
- keine unnötig engen Zeilenabstände
- keine überlangen Fließtextblöcke ohne Gliederung

### 10.5 Tabellenstil Dokumente

Tabellen verwenden:

- Headerzeile: Deep Emerald `#112A20`
- Headertext: Weiß `#FFFFFF`, Inter Bold, All Caps, ca. 10 pt
- Tabelleninhalt: Inter Regular, 10.5 pt, Dark Charcoal `#2A2A2A`
- Linien: dezent, nicht schwer
- Hervorhebungen: Matte Gold oder Deep Emerald
- keine bunten Ampelfarben ohne fachlichen Grund

### 10.6 Bulletpoint-Stil Dokumente

Bulletpoints verwenden:

- Bullet Dot in Emerald
- Text in Inter Regular, 10.5 pt
- Einzug sauber und konsistent
- Bulletpoint-Header in Plus Jakarta Sans Semi-Bold, 12 pt, Deep Emerald

Nicht verwenden:

- uneinheitliche Bulletzeichen
- zu starke Einrückungen
- Website-Icon-Bullets ohne Freigabe
- überladene Bulletpoint-Blöcke

### 10.7 Nummerierungen Dokumente

Nummerierungen verwenden:

- Inter Regular, 10.5 pt
- Nummern in Matte Gold
- Text in Dark Charcoal
- konsistente Abstände

Geeignet für:

- Prozessschritte
- Kapitelunterpunkte
- Checklisten
- Bewertungsmodelle
- Umsetzungsreihenfolgen

### 10.8 Hervorhebungen Dokumente

Normale Hervorhebung:

- Inter Italic oder Medium
- Deep Emerald `#112A20`

Starke Hervorhebung:

- Inter Extra-Bold
- Dark Bronze-Gold `#A37A3E`

Nicht verwenden:

- Neonfarben
- zufällige Unterstreichungen
- mehrere konkurrierende Hervorhebungsfarben
- Website-Goldverlauf für normale Textpassagen

---

## 11. Cover-Regeln für Dokumente

Cover dürfen hochwertiger und stärker gestaltet sein als Innenseiten, müssen aber kontrolliert bleiben.

### 11.1 Cover erlaubt

- großes H1 in Bebas Neue
- Goldakzent oder Gold-Fallback
- dunkle Emerald-/Schwarz-Akzentfläche
- klare Unterzeile
- Autor / Marke / Kontaktinformation
- dezente technische Linien oder abstrakte Struktur

### 11.2 Cover nicht erlaubt

- generische KI-Roboter
- überladene technische Hintergründe
- bunte Verläufe
- Cyan / Blau / Violett als Hauptwirkung
- Bronze / Kupfer
- schlechte Lesbarkeit durch zu dunkle Textflächen
- zufällige Bildstile ohne Bezug zu Nurovelle

---

## 12. Website vs. Dokumente

| Bereich | Website | Dokumente |
|---|---|---|
| Hauptwirkung | dunkel, technisch, Premium | klar, lesbar, hochwertig, strukturiert |
| H1 | sehr groß, Bebas Neue, ggf. Goldverlauf | Bebas Neue, ca. 26 pt, Gold/Fallback |
| Body | Raleway / Roboto | Inter Regular |
| Akzente | Goldverläufe, Hover, CTA | Matte Gold, Emerald, sparsame Hervorhebung |
| Hintergrund | Schwarz / Deep Green / Petrol | hell/neutral oder gezielt Emerald-Struktur |
| Interaktion | Hover, Tap, CTA | nicht relevant |
| Bildsprache | technische Systemarchitektur | sparsam, erklärend, nicht überladen |

Regel:

Website-Design darf nicht 1:1 auf Dokumente übertragen werden. Dokumente benötigen bessere Lesbarkeit, klarere Struktur und weniger visuelle Effekte.

---

## 13. Tonalität

Nurovelle kommuniziert:

- sachlich
- professionell
- klar
- direkt
- nutzenorientiert
- mittelstandstauglich
- ohne KI-Hype
- ohne übertriebene Versprechen

Nicht verwenden:

- leere Marketingphrasen
- übertriebene Superlative
- unbewiesene Erfolgszahlen
- künstliche Dringlichkeit
- unklare Buzzword-Ketten

---

## 14. CTA- und Conversion-Regeln Website

### 14.1 Haupt-CTA

```text
Kostenlose KI-Potenzialanalyse anfordern
```

### 14.2 Neben-CTA

```text
Praxisleitfaden herunterladen
```

### 14.3 Linklogik Startseite

- Potenzialanalyse-, Anfrage- und Erstgespräch-CTAs führen zu `analyse.html`.
- Download-CTAs führen zu `#downloads` oder `praxisleitfaden.html`.
- Kein zusätzlicher Kontakt-/Formularbereich auf der Startseite.
- Kein eigener Roadmap-CTA.

---

## 15. Nicht verhandelbare Verbote

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Neon-Look
- Bronze
- Kupfer
- generische KI-Roboter
- Stockfotos
- überladene Dashboards
- Sci-Fi-Konsolen
- zufällige UI-Texte in Bildern
- weiße Plattformen als neuer Hauptstil
- wechselnde Materialsprache
- freie Neuinterpretation bestehender Formen
- neue Layoutideen ohne Auftrag
- nicht freigegebene Assets als finale Assets

---

## 16. Arbeitsregeln

Für jede Umsetzung gilt:

- Bestehende Entscheidungen übernehmen.
- Bestehende Vorlagen übernehmen.
- Bestehende Designs übernehmen.
- Keine Änderung ohne Auftrag.
- Keine Kürzung ohne Auftrag.
- Keine Erweiterung ohne Auftrag.
- Keine Layoutänderung ohne Auftrag.
- Fehlende Assets markieren, nicht erfinden.
- Unklare technische Quellen als fehlend markieren, nicht frei ersetzen.

---

## 17. Status

Dieser Styleguide konsolidiert den dokumentierten Stand.

Er ersetzt keine Einzelentscheidung aus dem Decision Log, sondern macht die bestehenden Design- und Dokumentregeln zentral nutzbar.

Bei Konflikten gilt die Priorität:

1. Explizite aktuelle Benutzervorgabe
2. `task_contract.md`
3. `decision_log.md`
4. `project_overview.md`
5. `todo.md`
6. Eigene Vorschläge nur nach Freigabe

---

## 9. CSS-FIRST-Regel

Alle steuerbaren Website-Komponenten werden grundsätzlich zuerst als HTML/CSS-Lösung geplant und nicht als Bild generiert.

Dazu gehören insbesondere:

- Boards
- Panels
- Karten
- Buttons
- Hover-Zustände
- Animationen
- Rahmen
- Divider
- Glows
- Textflächen
- Sektion-Hintergründe
- responsive Layoutflächen

Bildassets werden nur für Motive verwendet, die nicht sinnvoll per CSS erzeugbar sind. Dazu gehören insbesondere:

- freigestellte 3D-Objekte
- technische Module
- abstrakte Visuals
- Portraits
- Mockups
- komplexe räumliche Illustrationen

Texte, Labels, Zahlen, UI-Beschriftungen und Layoutflächen dürfen nicht als Bildbestandteil erzeugt werden, wenn sie per HTML/CSS kontrollierbar sind.

Prüfreihenfolge bei neuen visuellen Anforderungen:

1. Kann die Anforderung sauber per HTML/CSS umgesetzt werden?
2. Falls ja: keine Bildgenerierung verwenden.
3. Falls nein: Bildasset nur für den nicht-codefähigen visuellen Anteil erstellen.
4. Text, Layoutzustände, Responsiveness und Interaktionen bleiben im Code.


## 18. Navigation, Breadcrumbs, Burger-Menü und Social Buttons

Diese Komponenten sind Bestandteil des Website-Systems und werden CSS-first umgesetzt.

### 18.1 Navigation

Die Navigation muss klar, conversion-orientiert und responsiv sein.

Vorgaben:

- Desktop-Header mit klarer Linkstruktur
- sichtbarer Haupt-CTA
- aktive Zustände
- Hover-Zustände
- Focus-Zustände
- keine überladene Navigation
- keine zufälligen Template-Navigationsstile

### 18.2 Mobile Burger-Menü

Mobile Navigation wird über ein echtes Burger-Menü umgesetzt.

Vorgaben:

- Button mit semantischem Label
- `aria-expanded`-Zustand
- sichtbarer Open-/Close-Zustand
- Menü darf keine Inhalte abschneiden
- CTA bleibt sichtbar
- Impressum und Datenschutz bleiben erreichbar
- Tap-Flächen mindestens 44 px Höhe

### 18.3 Breadcrumbs

Breadcrumbs werden für Unterseiten und Detailseiten eingesetzt.

Beispielstruktur:

```text
Startseite / Leistungen / KI-Agenten
```

Regeln:

- semantisch als Navigation
- dezente Darstellung
- helle Schrift auf dunklem Grund
- Gold nur für aktiven Zustand, Hover oder Divider-Akzent
- nicht auf der Startseite erforderlich

### 18.4 Social Buttons

Social Buttons werden für Portrait-/Kontaktkarten und relevante Kontaktbereiche genutzt.

Verbindlicher Stil:

- nur das jeweilige Plattform-Symbol, kein Text im Button
- Symbol als SVG oder Icon-Font im Code, nicht als neu generiertes Bild
- transparente oder matte dunkle Fläche, kein schwerer Kastenlook
- Symbol in der richtigen Plattformfarbe oder in einer freigegebenen Nurovelle-kompatiblen Markenfarb-Variante
- keine weißen Standard-Symbole als finale Lösung, wenn die Plattformfarbe gefordert ist
- keine Labels im sichtbaren Button; Barrierefreiheit über `aria-label`
- gleiche optische Größe und gleiche Grundlinie für alle Icons
- ausreichende Tap-Fläche, auch wenn nur das Symbol sichtbar ist

Animationsregel:

- Animation per CSS, nicht als GIF/Video/Bildsequenz
- ruhiger Hover-/Focus-Effekt: leichtes Anheben, Skalierung, Glow oder Linienimpuls
- Animation muss zum jeweiligen Icon passen und darf nicht verspielt wirken
- keine Regenbogen-, Neon-, Bounce- oder Comic-Wirkung
- `prefers-reduced-motion` berücksichtigen

Referenzwirkung:

- ähnlich einer minimalistischen Icon-Reihe auf dunklem Hintergrund
- sichtbar sind nur die Plattformzeichen
- keine zusätzlichen Textlabels
- keine zufälligen Icon-Stile oder gemischten Strichstärken

### 18.5 Formular-UX

Formularbereiche werden conversion-orientiert geprüft.

Bestehende technische Logik darf erhalten bleiben. UX, Reihenfolge, Microcopy, mobile Lesbarkeit und Success-/Error-Zustände dürfen verbessert werden, solange Datenschutz, Einwilligung und API-Flow erhalten bleiben.

### 18.6 Section-Divider

Section-Divider werden als technische Übergangselemente zwischen ausgewählten Sections eingesetzt.

Prüfvariante A:

- schräger SVG-Separator
- absolute Positionierung am unteren Rand der vorherigen Section
- zwei überlagerte SVG-Paths für Tiefe
- `preserveAspectRatio="none"` für volle Breite
- responsive Anpassung über Breite, Rotation und vertikalen Versatz

Gestaltungsregeln:

- Basisflächen: mattes Schwarz, Deep Green, Emerald, dunkles Petrol
- Gold nur als feiner Layer, Linie, Glow oder Kantenakzent
- keine hellgrünen Beispiel-Farben übernehmen
- keine Cyan-, Blau-, Violett-, Regenbogen- oder Neonflächen
- keine Stock-/Bilddivider
- keine übermäßig dekorativen Wellen oder verspielten Formen

Technische Regeln:

- Umsetzung per HTML/CSS/SVG
- Divider sind Teil des Layoutsystems und keine Bildassets
- `overflow-x: hidden` nur gezielt einsetzen, wenn SVG-Breite Mobile-Overflow erzeugt
- z-index sauber definieren
- keine Inhalte verdecken
- keine Layoutsprünge beim Laden
- Mobile-Version separat prüfen
- Animation nur dezent und mit `prefers-reduced-motion`

Beispielwirkung:

- technischer, kantiger Section-Übergang
- mehr Tiefe zwischen dunklen Flächen
- kontrollierter Premium-Look statt harter Standardkante

### 18.7 Divider-Prüfvariante B – Pure-CSS-Angled-Sections

Als zweite Divider-/Übergangsvariante werden Pure-CSS-Angled-Sections geprüft.

Technik:

- schräge Section-Kanten per `clip-path: polygon(...)`
- Winkelsteuerung per CSS-Variable, z. B. `--angle`
- vertikale Ausgleichsfläche über `--space`
- Kantenlänge über `--hypot`
- optional Schattenkante über `::after`
- optionale SCSS-Berechnung mit `math.tan()` / `math.cos()`
- optionale native CSS-Trigonometrie nur mit `@supports` und Fallback

Gestaltungsregeln:

- keine Übernahme der Demo-Farbverläufe
- keine bunten Pastell-, Regenbogen-, Cyan-, Blau- oder Violettverläufe
- Section-Flächen bleiben Nurovelle-konform: Schwarz, Deep Green, Emerald, dunkles Petrol
- Gold nur als sehr dezente Kanten-, Schatten- oder Highlight-Linie
- Überschriften werden nicht zwingend mit dem Winkel rotiert; Lesbarkeit hat Vorrang
- keine interaktive Demo-Codebox, keine Demo-Hinweise, keine fremden Footer-Inhalte

Technische Regeln:

- Einsatz nur nach Desktop-/Tablet-/Mobile-Test
- kein horizontales Scrollen
- keine Überdeckung von Text, Cards, CTAs oder Hero-Visuals
- bei instabilem Browser-Support fallback auf SCSS-Werte oder SVG-Divider
- `@supports` für native CSS-Trigonometrie verwenden, falls diese Variante genutzt wird

### 18.8 Divider-Prüfvariante C – Diagonal Box / SkewY + Clip-Path

Als dritte Divider-/Übergangsvariante wird eine Diagonal-Box-Technik geprüft.

Technische Idee:

- Section-Hintergrund über `::before` oder vergleichbares Pseudo-Element
- diagonale Wirkung über `transform: skewY(var(--angle))`
- Content bleibt auf normaler Ebene und wird nicht transformiert
- sicherer Inhaltsbereich über CSS-Variablen wie `--angle`, `--abs-angle`, `--tan-alpha`, `--skew-padding`, `--clip-padding`
- optionaler `clip-path`-Abschnitt für nicht verzerrte Hintergrundflächen

Gestaltungsregeln:

- keine Übernahme der Demo-Farben
- keine Lila-/Pink-/Cyan-/Blau-Verläufe
- keine Pastell-, Regenbogen- oder Neonwirkung
- Nurovelle-Farben verwenden: `#050706`, `#080B09`, `#0A1913`, `#112A20`, `#163A35`
- Gold nur als schmaler Akzent, Linie, Lichtkante oder Hover-Verstärkung
- Text, Cards, CTAs und Navigation bleiben horizontal und unverzerrt
- keine Playground-Controls, Demo-Texte, Formeln oder erklärende Beispielgrafiken übernehmen

Prüfanforderungen:

- kein horizontales Scrollen
- stabile Darstellung auf Desktop, Tablet und Mobile
- ausreichender Abstand zwischen schräger Kante und Content
- kein Verdecken von CTAs oder Karten
- Browser-Support für `tan()` prüfen oder Fallback mit festen/SCSS-berechneten Werten nutzen


### 18.9 Breadcrumb-Prüfvariante – Pfeil-/Chevron-Breadcrumbs

Die ausgewählte Breadcrumb-Referenz wird als mögliche CSS-Umsetzung für Unterseiten und Detailseiten aufgenommen.

Gestaltungsziel:

- technisch
- kompakt
- lesbar
- hochwertig
- nicht verspielt
- passend zu dunklem Nurovelle-Layout

Technische Logik:

- Breadcrumb als semantisches `<nav aria-label="Breadcrumb">`
- Links als horizontale Kette
- Pfeilform über rotierte `::after`-Pseudo-Elemente möglich
- aktive Seite und Hover-Zustand visuell unterscheidbar
- Animation nur dezent: Farbimpuls, Kantenlicht, leichter Glow oder kurze Linie
- Mobile: bei wenig Platz kürzen, umbrechen oder horizontal scrollbar mit sichtbarer Kontrolle prüfen

Nicht übernehmen:

- Demo-Farben
- hellgrüner Hover
- Google-Font `Merriweather Sans`
- Prefixfree-Script
- CSS-Counter/Nummern als Standardzwang
- Beispieltexte aus der Referenz
- starke schwarze Box-Shadows, wenn sie zu schwer wirken

Nurovelle-Farblogik:

- Grundfläche: `#050706`, `#080B09`, `#0A1913`, `#112A20`
- Trennung/Kante: dunkles Emerald oder Petrol
- aktueller Zustand: Gold-Akzent, schmale Goldkante oder dezenter Gold-Glow
- Text: hell, gedämpft oder Gold nur bei aktivem Zustand

Optionale externe Recherche:

- `https://freefrontend.com/css-infographics/` darf bei Bedarf als Inspirationsquelle für CSS-Infografiken, kleine technische UI-Elemente und Mikrointeraktionen geprüft werden.
- Keine Übernahme ohne Prüfung gegen Nurovelle-Stil, Responsiveness und CSS-FIRST-Regel.


### 18.10 Card-Prüfvariante – Frosted Glass Overlay Cards

Als zusätzliche Card-Variante wird eine Frosted-Glass-Overlay-Technik geprüft.

Technische Idee:

- Card als echtes HTML-Element
- Bild-/Visualebene optional, aber nicht aus fremden Demo-Quellen
- Infofläche bewegt sich per `transform` von unten in die Card
- Hintergrund-/Overlayebene kann per `filter: blur()` oder `backdrop-filter` wirken
- Hover auf Desktop, Tap/Focus auf Mobile
- Übergang per CSS-Transition

Nurovelle-Anpassung:

- dunkle Grundfläche statt heller Demo-Optik
- matte schwarze, Deep-Green- oder Petrol-Overlays
- Gold nur als schmale Linie, Akzentkante, Hover-Impuls oder aktiver Fokus
- keine weißen Vollflächen, falls sie die Premium-Dark-Ästhetik brechen
- keine Unsplash-/Demo-Bilder
- keine Open-Sans-/Demo-Typografie
- keine bunten Demo-Akzente

Accessibility / UX:

- Card muss per Tastatur fokussierbar sein, falls klickbar
- sichtbarer Focus-State erforderlich
- Mobile darf nicht allein auf Hover angewiesen sein
- Textkontrast prüfen
- reduzierte Bewegung bei `prefers-reduced-motion`
- zu lange Texte vermeiden; Cards bleiben scannbar

Status:

- Prüfvariante, nicht finale Card-Pflicht.
- Einsatz nur, wenn die Variante besser funktioniert als einfache dunkle CSS-Cards.

### Dashboard-Board-Section-Prüfvariante

Die Referenz `https://codepen.io/josephrexme/pen/oNNpZYJ` wird als mögliche technische Section-Variante aufgenommen.

Charakter der Referenz:

- perspektivisches Board
- seitliche Icon-Navigation
- Header-Zeile innerhalb des Boards
- Grid-/Analysefläche
- Listen-/Tabellenbereiche
- animierter Listenmarker beziehungsweise scrollender Highlight-Zustand
- SVG-Icons als echte Code-Elemente
- SCSS/CSS-basierte Schatten, Perspektive und Tiefenwirkung

Mögliche Nurovelle-Nutzung:

- technische Erklärsektion
- Workflow-/Modulübersicht
- Systemarchitektur-Preview
- Analyse-/Prozessvisualisierung
- Section mit Premium-Tech-Anmutung

Nicht übernehmen:

- Demo-Farben
- blaue/lila Board-Palette
- Demo-Verläufe
- Demo-Logo `YOUR COMPANY`
- Personenname, Avatar und externe Bild-URL
- Finanz-/Wallet-/Profit-Texte und Zahlen
- Dribbble-Credit-Block
- fremde Datenstruktur als Inhalt
- unpassende Dashboard- oder Crypto-/Finance-Anmutung

Nurovelle-Anpassung:

- Board-Fläche: `#050706`, `#080B09`, `#0A1913`, `#112A20`
- Tiefenflächen: dunkles Petrol / Emerald
- Gridlinien: sehr dezentes Emerald oder dunkles Petrol
- aktive Icon-Zustände: Goldlinie, Goldpunkt, feiner Gold-Glow oder leichte Aufhellung
- Text: hell, gedämpft, technisch lesbar
- keine Cyan-, Blau-, Violett-, Pastell-, Regenbogen- oder Neonwirkung

Technische Regeln:

- Umsetzung als HTML/CSS/SVG-Komponente.
- Icons als Inline-SVG oder geprüfte Icon-Bibliothek.
- Kein Screenshot, kein gerendertes Bild, keine KI-Bildgenerierung.
- Perspektive mit `transform: perspective(...) rotateX(...) rotateY(...) rotateZ(...)` nur einsetzen, wenn keine Lesbarkeitsprobleme entstehen.
- Mobile braucht eine eigene, reduzierte Darstellung; ein stark perspektivisches Board darf auf Mobile abgeflacht oder in Cards/Rows zerlegt werden.
- Animationen dezent halten und `prefers-reduced-motion` berücksichtigen.
- `aria-label` korrekt schreiben; Demo-Fehler wie `arial-label` nicht übernehmen.

Status:

- Prüfvariante, nicht finale Section-Pflicht.
- Einsatz nur nach Vergleich mit einfacheren CSS-Sections, Card-Grids und Workflow-Komponenten.


## 24. CTA-Button-Prüfvariante – Arrow-Reveal zu Press-Button

Diese Variante ist als Prüfoption für wichtige CTAs dokumentiert.

### 24.1 Technische Logik

Der Button kann aus zwei Bewegungsprinzipien kombiniert werden:

1. **Arrow-/Circle-Reveal-Startlogik**
   - Pfeil rechts sichtbar
   - zweiter Pfeil startet außerhalb des Buttons
   - Text verschiebt sich leicht
   - Kreisfläche expandiert als Hover-Füllbewegung

2. **Press-/Button-Base-Endlogik**
   - sichtbare obere Buttonfläche
   - darunterliegende Button-Basis
   - `:active` senkt die obere Fläche leicht ab
   - haptischer Druckeffekt ohne spielerische Übertreibung

### 24.2 Farbregel

Nicht übernehmen:

- `greenyellow`
- Demo-Türkis
- Demo-Grün
- helle Spiel-/Gaming-Wirkung
- fremde Demo-Verläufe

Erlaubt:

- Goldverlauf für Rahmen, Pfeil, Hover-Füllung oder aktive Fläche
- mattes Schwarz als Grundfläche
- Deep Green / Emerald / dunkles Petrol für Tiefe und Schatten
- sehr dezenter Glow, nur wenn Premium-Optik erhalten bleibt

### 24.3 UX-/Accessibility-Regeln

- semantisch als `<a>` bei Navigation/CTA oder `<button>` bei Aktion
- sichtbarer Focus-State
- mindestens 44 px Tap-Höhe
- keine Animation, die Text unlesbar macht
- `prefers-reduced-motion` berücksichtigen
- Mobile darf reduzierten Hover-/Press-Effekt nutzen

### 24.4 Status

Status: Prüfvariante, nicht finale Freigabe für alle Buttons.

---

## CTA-Button-Farbgrundlage – Gold

Für die CTA-Button-Prüfvariante wird folgende Gold-/Materiallogik als Prüfgrundlage verwendet:

```css
:root {
  --cta-gold-dark: #a54e07;
  --cta-gold-mid: #b47e11;
  --cta-gold-light: #fef1a2;
  --cta-gold-core: #bc881b;
  --cta-gold-border: #a55d07;
  --cta-gold-inner-dark: #8b4208;
  --cta-gold-inner-mid: #b17d10;
  --cta-gold-highlight: #fae385;
  --cta-gold-text-dark: rgb(120, 50, 5);
  --cta-gold-gradient: linear-gradient(160deg, #a54e07, #b47e11, #fef1a2, #bc881b, #a54e07);
}
```

Anwendung:

- Primär-CTA: Goldverlauf als Füllung oder aktive Hover-Fläche.
- Pfeile/Icons: Gold oder dunkler Kontrast abhängig vom Zustand.
- Press-State: reduzierte Tiefe, stabiler Innenrand, keine Gummi-Animation.
- Hover: dezente Lichtverschiebung, keine übertriebene Casino-/Neonwirkung.
- Text: echte Nurovelle-CTA-Texte, nicht Demo-Text.

Nicht übernehmen:

- React-/Styled-Components-Zwang
- Demo-Text „Golden Button“
- `role="button"` auf echtem `<button>`
- übertriebene Glanz-/Spielautomatenwirkung

## Button-Interaktion – Download zu Danke-Zustand

Als weitere CTA-Prüfvariante wird eine Downloadbutton-Transformation festgehalten.

Zielverhalten:

1. Ausgangszustand: Download-Button im Nurovelle-Gold-/Dark-System.
2. Interaktion: Nutzer klickt oder tippt.
3. Übergang: Buttonfläche vergrößert sich oder öffnet sich kontrolliert.
4. Endzustand: größere Danke-/Bestätigungsfläche, zum Beispiel „Danke“, „Download startet“ oder „Anfrage erhalten“.

Gestaltungsregeln:

- Premium, ruhig, B2B-tauglich.
- Keine grellen Demo-Farben.
- Keine Casino-, Spielautomat-, Comic- oder Bounce-Wirkung.
- Gold nur als hochwertiger Akzent, Fläche oder Lichtkante.
- Text bleibt echtes HTML.
- Animation muss reduziert werden können.
- Mobile-Zustand muss ohne Hover funktionieren.


## Statuskorrektur Komponenten 2026-07-02

Aktueller Design-/UX-Status:

- Divider bleiben Sichtprüfungs-Thema. Varianten A, B und C werden erst live bewertet.
- CTA-Button-Animation ist festgelegt: Arrow-/Circle-Reveal-Start, Übergang in haptische Press-Button-Logik, Gold-Farbgrundlage.
- Breadcrumb-Stil ist festgelegt: CSS-Chevron-/Pfeil-Breadcrumbs ohne Demo-Farben, semantisch korrekt, mobil und barrierearm.
- Hero-Animation bleibt Sichtprüfungs-Thema. Orb, Cube-Entstehung und Conic-/Noise-Variante werden live verglichen.
- Komponenten-zu-Section-Zuordnung bleibt offen.
- Temkuri/Zra bleiben als Basis-/Strukturfrage offen.
