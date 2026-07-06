# NUROVELLE HOMEPAGE IMPLEMENTATION BRIEF

Stand: 2026-07-05  
Status: aktive Umsetzungsdatei  
Quelle für Hauptseitenstruktur: Chatstand „KI Website Struktur Verbesserung 20.06.26“ plus spätere Korrekturen aus dem aktuellen Verlauf.

Dieser Brief ist **keine zusätzliche Designquelle**.  
Er beschreibt, **was auf der Hauptseite gebaut wird** und welche bestehenden Design-/CSS-Dateien dafür verbindlich gelten.

Aktive Quellen:

1. `styleguide.md` — verbindliche Design- und Komponentenregeln
2. `nurovelle-tokens.css` — technische Design-Tokens
3. `nurovelle-animations.css` — konkrete CSS-Animationen und Interaktionen
4. `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md` — Umsetzungsbrief für Struktur, Inhalte, CTA-Ziele und Seitenlogik

Keine weiteren Design-Zwischendateien als aktive Quelle verwenden.

---

## 1. Projektziel

Die Nurovelle-Hauptseite wird als conversion-orientierte B2B-Homepage umgesetzt.

Die Seite erklärt klar:

- was Nurovelle anbietet
- für welche Geschäftsprozesse KI sinnvoll eingesetzt werden kann
- warum zuerst eine Potenzialanalyse sinnvoll ist
- welche Leistungen Nurovelle abdeckt
- wie aus einem Geschäftsprozess eine konkrete KI-Lösung wird
- wie Besucher Analyse, Download oder Erstgespräch starten können

Zielgruppen:

- mittelständische Unternehmen
- Startups
- Einzelunternehmer
- Dienstleister
- technische Betriebe
- Geschäftsführer
- Operations-/Prozessverantwortliche
- Teams mit vielen manuellen Abläufen

Keine Einschränkung nur auf Mittelstand.

---

## 2. Conversion-Logik

Die Hauptseite hat drei zentrale Conversion-Pfade.

### 2.1 KI-Potenzialanalyse

Alle CTAs zur kostenlosen KI-Potenzialanalyse führen zu:

```text
analyse.html
```

Primärer CTA-Text:

```text
Kostenlose KI-Potenzialanalyse anfordern
```

Header-CTA kurz:

```text
Kostenlose KI-Potenzialanalyse
```

### 2.2 Praxisleitfaden / Downloads

Alle Download-CTAs führen zum Downloadbereich auf der Hauptseite:

```text
#downloads
```

Download-Buttons nutzen die Animation aus `nurovelle-animations.css`.

Verhalten:

1. Button startet Download-/Anfrageaktion.
2. Während der Aktion wird ein Lade-/Aktionszustand gezeigt.
3. Nur nach echter erfolgreicher Aktion wird der Success-Zustand gesetzt.
4. Button transformiert in größere Danke-/Bestätigungsfläche.
5. Im Fehlerfall entsteht kein Danke-Zustand, sondern ein Fehler-/Retry-Zustand.

Die Analyse-Seite bleibt davon getrennt und nutzt ihre eigene Formular-, Success- und Error-Logik.

### 2.3 Erstgespräch

Alle CTAs zum kostenlosen Erstgespräch führen zu einem Bereich auf der Hauptseite mit Portrait, Social Icons, Kontaktdaten und Erstgespräch-CTA.

Keine separate Erstgespräch-Seite anlegen, solange nicht anders beauftragt.

---

## 3. Hauptseitenstruktur

Die Hauptseite wird in dieser Reihenfolge aufgebaut:

    • Header
    • Hero
    • Warum Nurovelle
    • Sie haben bereits eine konkrete KI-Idee?
    • Der erste Schritt zu Ihrem KI-Projekt
    • Kostenlose KI-Potenzialanalyse
    • Vom Geschäftsprozess zur KI-Lösung
    • KI-Leistungen von Nurovelle
    • Download-Bereich
    • Kontakt-/Erstgespräch-Bereich mit Portrait
    • Formularbereich
    • Footer

Keine zusätzlichen Hauptsections ohne gesonderte Freigabe.

---

## 4. Header

Der Header wird nach dem freigegebenen Vorgabedesign umgesetzt.

Aufbau:

- Logo links
- Logo klickbar zur Startseite
- Breadcrumbs im Header
- Analyse-CTA rechts
- Hamburger unterhalb des Headers

CTA rechts:

```text
Kostenlose KI-Potenzialanalyse
```

Ziel:

```text
analyse.html
```

Der Header-CTA verwendet die freigegebene Button-Komponente und Button-Animation aus `nurovelle-animations.css`.

Logo-Animation:

- kontrollierter Spin-Impuls
- startet schnell
- wird langsamer
- kurz vor Stillstand erneuter Impuls möglich
- Breadcrumbs, CTA und Hamburger bleiben stabil

---

## 5. Sidebar

Die Sidebar bleibt nach Vorgabedesign.

Einzige funktionale Festlegung:

- Öffnen und Schließen über den Hamburger unterhalb des Headers

Keine neue Sidebar-Struktur.  
Keine zusätzliche Sidebar-Logik.  
Keine freie Neugestaltung.

---

## 6. Hero

### 6.1 Inhalt

H1:

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

### 6.2 Hero-CTAs

1. Primär:

```text
Kostenlose KI-Potenzialanalyse anfordern → analyse.html
```

2. Sekundär:

```text
Praxisleitfaden herunterladen → #downloads
```

3. Dritter CTA:

```text
Kostenloses Erstgespräch vereinbaren → Kontakt-/Portraitbereich
```

### 6.3 Hero-Visual

- bestehender finaler Cube / Würfel
- Text und CTAs als HTML, nicht im Bild
- keine Texte im Visual
- keine Labels
- keine Zahlen
- keine Logos
- keine generischen Sci-Fi-Dashboards

### 6.4 Hero-Animation

- goldene Cube-Ecken dürfen dezent pulsieren
- ruhiger technischer Lichtimpuls
- Orb-/Entstehungseffekt möglich, wenn live passend
- keine unkontrollierte Bewegung des gesamten Visuals
- Umsetzung per HTML/CSS/JS, nicht per Bildgenerierung

---

## 7. Section 3 — Der erste Schritt zu Ihrem KI-Projekt

Zweck:

Diese Section erklärt, dass Nurovelle nicht mit zufälligen Tools oder fertigen KI-Spielereien startet, sondern mit der Analyse echter Geschäftsprozesse.

Inhaltliche Aufgabe:

- Problemverständnis aufbauen
- manuelle Abläufe sichtbar machen
- Einstieg in Potenzialanalyse vorbereiten
- erklären, dass KI nur dort sinnvoll ist, wo sie echte Abläufe verbessert

Empfohlene Struktur:

- starke Headline
- kurzer erklärender Blocktext
- 3 bis 4 kompakte Nutzen-/Orientierungspunkte
- dezenter Übergang zur Potenzialanalyse-Section

Kernaussage:

```text
Bevor eine KI-Lösung gebaut wird, muss klar sein, welcher Prozess verbessert, beschleunigt oder automatisiert werden soll.
```

Mögliche Punkte:

- Prozesse verstehen
- Potenziale erkennen
- Aufwand und Nutzen einschätzen
- sinnvolle nächste Schritte definieren

CTA-Logik:

- dezenter Verweis zur Potenzialanalyse
- keine konkurrierende neue Conversion

---

## 8. Section 4 — Kostenlose KI-Potenzialanalyse

Zweck:

Diese Section ist einer der wichtigsten Conversion-Punkte der Hauptseite.

Sie erklärt die kostenlose KI-Potenzialanalyse als risikoarmen Einstieg.

Inhalte:

- Analyse bestehender Abläufe
- Identifikation manueller, wiederkehrender oder datenintensiver Prozesse
- Einschätzung, wo KI-Agenten, Automatisierung, Prompt-Systeme, MCP/API-Anbindungen oder Wissenssysteme sinnvoll sind
- grobe Priorisierung nach Nutzen, Umsetzbarkeit und Aufwand
- klare Empfehlung für nächste Schritte

Darstellung:

- gleiche Card-/CTA-Logik wie im Styleguide
- keine neue Gestaltung
- bestehender CTA
- klare Nutzenargumente

Primärer CTA:

```text
Kostenlose KI-Potenzialanalyse anfordern → analyse.html
```

Nicht mit Download-Logik vermischen.  
Die Analyse-Seite ist ein eigener Zielpfad.

---

## 9. Section 5 — Sie haben bereits eine konkrete KI-Idee?

Zweck:

Diese Section holt Besucher ab, die nicht mehr nur Orientierung suchen, sondern bereits eine konkrete Idee, ein internes Problem oder einen Prozesskandidaten haben.

Inhalte:

- Idee prüfen
- Machbarkeit einschätzen
- Datenlage und Schnittstellen klären
- möglichen Prototyp oder Umsetzungspfad definieren
- vermeiden, dass eine Idee technisch umgesetzt wird, ohne geschäftlich sinnvoll zu sein

Darstellung:

- direkte, vertrauensbildende Section
- keine überladene Card-Matrix
- klare Unterscheidung zur allgemeinen Potenzialanalyse

CTA-Optionen:

```text
Kostenloses Erstgespräch vereinbaren → Kontakt-/Portraitbereich
```

oder

```text
Projektidee prüfen lassen → Formularbereich
```

---

## 10. Section 6 — KI-Leistungen von Nurovelle

Zweck:

Diese Section zeigt die Leistungsbereiche von Nurovelle.

SEO wird hier sichtbar als eigener Leistungsbereich geführt und nicht nur als Homepage-Konzept verstanden.

Darstellung:

- CSS-Cards / Service-Cards
- dunkle Karten
- goldene Akzente sparsam
- keine Problemlösungscards in dieser Section
- jede Card führt später optional auf eine Detailseite oder einen Abschnitt

Leistungsbereiche:

1. KI-Potenzialanalyse
2. KI-Agenten für Geschäftsprozesse
3. Prompt Engineering und Prompt-Systeme
4. MCP-, API- und Tool-Anbindungen
5. Prozessautomatisierung
6. Datenverarbeitung und Dokumentenlogik
7. Wissenssysteme / interne KI-Assistenten
8. Individuelle KI-Software und Unternehmenslösungen
9. SEO als Leistung

Optional ergänzbar, wenn bereits vorgesehen:

- Schulung / Einführung / Enablement
- Analyse- und Lead-Systeme
- Content-/Marketing-Automatisierung

Section-CTA:

```text
Kostenlose KI-Potenzialanalyse anfordern → analyse.html
```

Dieser CTA ist hier bewusst gesetzt, weil Section 6 als Potenzialanalyse-CTA festgelegt wurde.

---

## 11. Section 7 — Vom Geschäftsprozess zur KI-Lösung

Zweck:

Diese Section erklärt den Ablauf der Zusammenarbeit auf der Hauptseite.

Sie bleibt auf der Hauptseite und wird auf Detailseiten nicht als eigene Standardsektion wiederholt.

Darstellung:

- Prozess-/Ablaufstruktur
- technische Premium-Optik
- keine überladene Timeline
- klare Schritte
- optional mit CSS-Modulen / Workflow-Grafik

Empfohlene Schritte:

1. Prozess verstehen
2. Potenzial bewerten
3. Lösungskonzept entwickeln
4. Daten, Tools und Schnittstellen prüfen
5. Prototyp oder Automatisierung umsetzen
6. Testen, optimieren und übergeben

Kernaussage:

```text
Nurovelle übersetzt reale Abläufe in konkrete KI-Systeme — von der Analyse bis zur umsetzbaren Lösung.
```

CTA-Logik:

- nach Ablauf/Prozess kann erneut zur Potenzialanalyse verwiesen werden
- kein zusätzlicher neuer Hauptpfad

---

## 12. Section 8 — Warum Nurovelle

Zweck:

Diese Section baut Vertrauen auf und grenzt Nurovelle von generischen KI-Tool-Anbietern ab.

Inhalte:

- Geschäftsprozess statt Tool-Hype
- individuelle Systeme statt Standardlösung
- technische Umsetzbarkeit im Blick
- verständliche Beratung und Umsetzung
- Fokus auf messbare Entlastung, bessere Datenverarbeitung und klare Abläufe
- Schnittstellen-, Daten- und Automatisierungslogik statt nur Texteingabe in Chatbots

Darstellung:

- schwarze Cards
- klare Nutzenargumente
- keine überladene Trust-Wall
- goldene Akzente sparsam

Mögliche Card-Titel:

- Prozessnah statt abstrakt
- Individuell statt von der Stange
- Technisch umsetzbar geplant
- Klarer Nutzen vor Automatisierung
- KI-Agenten mit Systemlogik
- Umsetzung statt nur Beratung

---

## 13. Section 9 — Download-Bereich

Anchor:

```text
#downloads
```

Zweck:

Der Download-Bereich stellt Praxisleitfaden, Whitepaper, Miniguides, Checklisten und Prompt-/Guide-Inhalte als Lead-Magneten bereit.

Geplante Downloads:

- Praxisleitfaden
- Whitepaper
- Miniguides
- Checklisten
- Prompt-Bibliothek / Prompt-Guide

Darstellung:

- eigene Section auf der Hauptseite
- Download-Cards oder Download-Liste
- CTA pro Download
- keine Weiterleitung auf eine separate Downloadseite, sofern nicht später beauftragt

Downloadbutton-Verhalten:

- Download-CTA startet reale Download-/Anfrageaktion
- Button zeigt Ladezustand
- nach Erfolg größerer Danke-/Bestätigungsbutton
- Fehlerzustand als Retry möglich

CSS-Basis:

```text
.nv-download-confirm
.nv-download-confirm.is-success
```

---

## 14. Section 10 — Kontakt-/Erstgespräch-Bereich mit Portrait

Zweck:

Alle Erstgespräch-CTAs führen zu diesem Bereich.

Aufbau:

- rechteckige Card
- rundes Portrait-Mockup
- darunter Social-Media-Icons
- darunter Kontaktinformationen
- darunter Erstgespräch-CTA
- Stil wie Homepage
- goldene Akzente sparsam

Inhalte:

- Name / Ansprechpartner
- kurze Vertrauenszeile
- Kontaktmöglichkeit
- Social Icons als SVG/CSS-Komponenten
- CTA für kostenloses Erstgespräch

CTA:

```text
Kostenloses Erstgespräch vereinbaren
```

Ziel je technischer Umsetzung:

- Anker zum Formularbereich
- Mail-/Kontaktlink
- Terminlink, falls später konkret hinterlegt

Keine neue Erstgespräch-Seite.

---

## 15. Section 11 — Formularbereich

Das Formular bleibt ganz unten auf der Hauptseite.

Zweck:

- Anfrage ermöglichen
- Projektidee einreichen
- Erstgespräch anfragen
- Kontakt aufnehmen

Empfohlene Felder:

- Name
- E-Mail
- Unternehmen
- Website optional
- Anliegen / Projektidee
- gewünschter Kontaktweg optional
- Datenschutz-Zustimmung

Formularlogik:

- Success-Zustand nur nach echter erfolgreicher Übermittlung
- Error-Zustand klar anzeigen
- Datenschutzlink einbinden
- keine Platzhalter als finale Copy stehen lassen

Analyse-Formular auf `analyse.html` bleibt davon getrennt.

---

## 16. Footer

Der Footer wird nach den freigegebenen Vorgabedesigns umgesetzt.

Funktion:

- Abschluss der Hauptseite
- Orientierung
- Kontakt
- rechtliche Links
- erneuter CTA zur Potenzialanalyse oder zum Erstgespräch

Inhalte:

- Logo / Markenname
- Kurzbeschreibung
- Navigation
- Leistungen
- Downloads
- Kontakt
- Impressum
- Datenschutz

CTA-Logik:

- Potenzialanalyse → `analyse.html`
- Erstgespräch → Kontakt-/Portraitbereich oder Formularbereich
- Download → `#downloads`

Keine generische Standard-Footer-Neugestaltung, wenn sie vom Vorgabedesign abweicht.

---

## 17. Komponenten- und CSS-Zuordnung

### Buttons

Verbindliche CSS-Basis:

```text
.nv-btn
.nv-btn-arrow
.nv-press-button
.nv-download-confirm
```

### Breadcrumb

```text
.nv-breadcrumb
```

### Hero

```text
.nv-hero-orb
.nv-conic-mask
.nv-hero-object
```

### Cards

```text
.nv-reveal-card
.nv-reveal-card.is-open
```

### Social Icons

```text
.nv-socials
.nv-social
```

### Board / Workflow-Prüfvariante

```text
.nv-board
```

Board-/Dashboard-Section ist nur Prüfvariante und nicht automatisch für die Hauptseite zu verwenden, wenn der konkrete Bereich ohne Board besser funktioniert.

---

## 18. Typografie

Aktive Schriften:

```text
Tapera + Inter
```

Verwendung:

- Tapera: große Headlines, starke Titel, markante Brand-Headlines
- Inter: Fließtext, Navigation, Buttons, Formular, Cards, Footer, UI

Nicht zurückfallen auf alte Zwischenstände wie Bebas Neue, Coder Pro, Raleway oder Roboto als Hauptsystem.

---

## 19. Farb- und Designregeln

Basis:

- matte schwarze Flächen
- sehr dunkles Petrol / Grün-Schwarz
- Gold als Premium-Akzent
- technische B2B-SaaS-Anmutung

Gold verwenden für:

- CTA-Buttons
- Rahmen
- aktive Zustände
- Hover-/Fokuszustände
- Divider
- feine Lichtkanten
- wichtige Highlights

Nicht verwenden:

- Cyan
- Blau als Hauptfarbe
- Violett
- Neon
- Bronze
- Kupfer
- Gaming-/Comic-Wirkung
- Casino-/Spielautomatwirkung
- generische KI-Roboter
- überladene Dashboards
- Text im Bild

---

## 20. Mobile / Accessibility

Pflicht:

- alle Hover-Zustände auch per Tap/Focus nutzbar
- Tastaturbedienung berücksichtigen
- sichtbare Focus-Zustände
- `aria-label` für Social Icons
- `aria-current="page"` für aktive Breadcrumbs
- `prefers-reduced-motion` beachten
- keine Success-Zustände ohne echte erfolgreiche Aktion

---

## 21. Abgrenzung zu Detailseiten

Dieser Brief beschreibt die Hauptseite.

Detailseiten werden später separat über das gemeinsame Detailseiten-Template umgesetzt.

Bereits bekannte Detailseitenlogik bleibt im Styleguide dokumentiert, wird aber nicht in die Hauptseite hineingemischt.

---

## 22. Umsetzungshinweis

Dieser Brief ist für Entwickler als inhaltliche und strukturelle Umsetzungsgrundlage gedacht.

Reihenfolge der Umsetzung:

1. Tokens einbinden
2. Animations-CSS einbinden
3. Header / Sidebar / Footer nach Vorgabedesign umsetzen
4. Hauptseitenstruktur 1–12 anlegen
5. Hero final einsetzen
6. Sections 3–8 mit den beschriebenen Inhalten bauen
7. Downloadbereich mit echter Success-/Error-Logik anbinden
8. Kontakt-/Portraitbereich bauen
9. Formular am Ende einbinden
10. Links, CTAs, Mobile und Accessibility testen

