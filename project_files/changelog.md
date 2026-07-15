# Changelog

## 2026-07-15 – Korrekturfortsetzung und Bereinigung (Layout/Assets)

Status: in Arbeit

Geändert:

- Dritte Bereinigungsstufe: wiederholte lokale Abstandswerte und kleine Radiuswerte in den Komponenten auf zentrale Tokens umgestellt (`--nv-space-*`, `--nv-radius-*`), ohne sectionsinterne Geometrie-Logik zu verändern.
- Zweite Bereinigungsstufe: wiederverwendete Spacing-/Radius-Werte zentral in `homepage/index.html` als Tokens ergänzt (`--nv-space-xxs/xs/sm/md/lg/xl/2xl`, `--nv-radius-sm/md`) und in den Komponenten an mehreren wiederholten Stellen verwendet.
- Verbindliche Mapping-Tabelle erstellt: `project_files/css_value_matrix.md` (Wertquelle, Verantwortlichkeit und Dateigrenzen).
- Zentrale Global-Tokens in `homepage/index.html` ergänzt (`--nv-section-inner-max`, `--nv-section-head-max`, `--nv-section-intro-max`, `--nv-footer-inner-max`, `--nv-section-title-gradient`, `--nv-gold-divider-strong`).
- In `homepage/components/nurovelle-service-cards.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breite) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert.
- In `homepage/components/nurovelle-resources-contact-faq.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert.
- In `homepage/components/nurovelle-section-rhythm.css` wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten, Footer-Basisfarben/Divider) auf zentrale Tokens umgestellt.
- Globale Rhythmus-, Alternation-, Separator- und responsive Sidebar-/Header-Regeln aus `homepage/components/nurovelle-section-rhythm.css` nach `homepage/index.html` verschoben.
- `homepage/components/nurovelle-section-rhythm.css` auf sectionsinterne Regeln fuer Prozess, Why und Footer reduziert.
- Sektion-7-Headerabstaende (`Head`, `Kicker`, `Title`) wieder lokal in `homepage/components/nurovelle-service-cards.css` verankert.
- Download-/Resource-Headerabstaende (`Head`, `Kicker`, `Title`) wieder lokal in `homepage/components/nurovelle-resources-contact-faq.css` verankert.
- Hintergrund-Alternation in `homepage/components/nurovelle-section-rhythm.css` auf den verbindlichen Sequenzstand korrigiert (`#warum-nurovelle`, `#ki-projekt-start`, `#projektidee`, `#potenzialanalyse`, `#formular`, `#leistungen`, `#prozess-zur-loesung`, `#downloads`, `#kontakt`, `#faq`, `.footer`).
- Prozesssektion in `homepage/components/nurovelle-section-rhythm.css` räumlich nachgestaffelt (2 + 2 + 2 über `nth-child`-Offsets), Mobile-Fallback ohne Offset beibehalten.
- Service-Card-Typografie in `homepage/components/nurovelle-service-cards.css` harmonisiert (lesbarere Bullet-, Untertitel- und Ergebnisgrößen).
- Service-Icon-Pfade in `homepage/index.html` auf `assets/cards/service/icons/{1..11}.png` umgestellt.
- Ergebnis-Icon-Injektion in `homepage/index.html` ergänzt (`assets/cards/service/icons/ergebnis.png`) innerhalb der bestehenden Service-Card-JavaScript-Logik.
- Platzhalter-Iconsatz unter `homepage/assets/cards/service/icons/` erstellt (`1.png` bis `11.png`, `ergebnis.png`) zur Stabilisierung fehlender Pfade.

Nicht geändert:

- Formularverarbeitung, Honeypot sowie Success-/Error-Grundlogik in `homepage/index.html`.
- Hero-Partikel-Canvas- und Cube-Grundlogik in `homepage/index.html`.

## 2026-07-14 – Kontrolliertes Homepage-Update in `homepage/index.html`

Status: in Arbeit

Geändert:

- Header-/Breadcrumb-Zielanker in `homepage/index.html` auf die aktuelle Sektionenstruktur angepasst (`#warum-nurovelle`, `#ki-projekt-start`, `#projektidee`, `#potenzialanalyse`, `#formular`, `#prozess-zur-loesung`, `#downloads`, `#kontakt`, `#faq`).
- Sidebar-Linktexte und -Reihenfolge in `homepage/index.html` an den aktuellen Inhaltsstand angepasst (inklusive neuem `Kontakt`-Eintrag).
- Abschnitt `Warum Nurovelle` in `homepage/index.html` inhaltlich auf freigegebenen Textstand umgestellt (2 Einleitungsabsätze + 6 Bulletpoints).
- Abschnitt `Der erste Schritt zu Ihrem KI-Projekt` in `homepage/index.html` textlich bereinigt und CTA auf `Potenzialanalyse starten` angepasst.
- Step-Animation in `homepage/index.html` erweitert: Karten sliden von links ein; Card-Text wird erst nach Ankunft sichtbar; Reduced-Motion-Fallback ohne Textverzögerung.
- Abschnitt `Konkrete KI-Idee` in `homepage/index.html` auf die Reihenfolge Prozessautomatisierung → Datenbasierte Entscheidungshilfe → Interne Wissenssuche umgestellt; breite Bildvariante vergrößert.
- Abschnitt `Vom Geschäftsprozess zur KI-Lösung` in `homepage/index.html` auf die sechs freigegebenen Modulbezeichnungen reduziert (ohne Beschreibungssätze).
- Neuer Abschnitt `Kontakt` in `homepage/index.html` ergänzt (40/60-Layout mit Portrait- und Kontaktkarte, Mobile-Stapelung).
- FAQ-Texte in `homepage/index.html` auf den freigegebenen Wortlaut aktualisiert; kompakte Kennzahlenleisten ergänzt.
- Footer in `homepage/index.html` inhaltlich auf die geforderten Gruppen erweitert (Unternehmensbeschreibung, nützliche Links, Newsletter, Kontakt, Rechtliches, Copyright, Nach-oben-Text, deaktivierte Links für Aktuelles/Team/SEO/Pakete).
- Hero-Sekundär-CTA in `homepage/index.html` auf `Unverbindliches Erstgespräch` mit Ziel `#kontakt` umgestellt.
- Potenzialanalyse- und Formularüberschriften/-texte in `homepage/index.html` an den freigegebenen Wortlaut angenähert.

Nicht geändert:

- Technische Formularfeldnamen und Grund-Submit-Mechanik in `homepage/index.html`.
- Download-Success-/Error-Zustandslogik in `homepage/index.html`.
- Hero-Cube-Asset und Partikel-Canvas-Grundlogik in `homepage/index.html`.

## 2026-07-15 – Platzhalter für fehlende Downloadpfade angelegt

Status: fertig

Geändert:

- `homepage/assets/downloads/checkliste.pdf` als Platzhalterdatei erstellt.
- `homepage/assets/downloads/prompt_guide.pdf` als Platzhalterdatei erstellt.

Nicht geändert:

- `homepage/index.html`.

## 2026-07-07 – Hero-Orb-Originalvorgabe gesichert

Status: fertig

Geändert:

- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Hero-Orb-Abschnitt mit der Originalvorgabe aus dem Chat ersetzt.
- `styleguide.md`: Hero-Animation konkretisiert: Orb kommt hinter den Cube; Originalvorgabe ist SCSS/HAML-Partikel-Orb.
- `nurovelle-animations.css`: bestehende `.nv-hero-orb`-/Conic-Umsetzung als rekonstruierte Adaption gekennzeichnet, nicht als Original.
- `nurovelle-hero-orb-original.scss`: Original-SCSS separat gesichert.
- `nurovelle-hero-orb-original.haml`: Original-HAML separat gesichert.

Nicht geändert:

- `index.html`
- Homepage-Layout
- bestehender Cube
- Produktions-CSS-Verhalten auf der Website

## 2026-07-07 – Divider-Diagonal-Originalreferenz gesichert

Status: fertig

Geändert:

- `nurovelle-divider-diagonal-original-reference.txt`: vom Nutzer gelieferte Diagonal-Section-/Divider-Referenz unverändert gesichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Variante C als technische Prüfvariante mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert.
- `styleguide.md`: Divider-Regeln ergänzt: `skewY()` nur auf Hintergrund-/Pseudo-Elemente, Content bleibt unverzerrt.
- `nurovelle-animations.css`: bestehende Divider-C-CSS als Nurovelle-Adaption gekennzeichnet, nicht als Originalcode.

Nicht geändert:

- `index.html`
- Homepage-Layout
- produktive Section-Divider auf der Website
- Hero-/Cube-Animation
- CTA-Buttons

## 2026-07-07 – SVG-Divider-Originalreferenz gesichert

Status: fertig

Geändert:

- `nurovelle-divider-svg-original-reference.txt`: vom Nutzer gelieferte SVG-Separator-/Divider-Referenz unverändert gesichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: Variante A als SVG-Schräg-Divider / Separator mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert.
- `styleguide.md`: Divider als verbindlicher Homepage-Bestandteil festgehalten; finale Divider-Form bleibt Prüfentscheidung zwischen SVG-Separator und Diagonal-/Skew-Varianten.
- `nurovelle-animations.css`: Nurovelle-Adaption für SVG-Separator ergänzt, nicht als Originalcode gekennzeichnet.

Nicht geändert:

- `index.html`
- Homepage-Layout
- produktive Section-Divider auf der Website
- Hero-/Cube-Animation
- CTA-Buttons

## 2026-07-07 – Pure-CSS-Angled-Divider-Originalreferenz ergänzt

Status: fertig

Geändert:

- `nurovelle-divider-pure-css-angled-original-reference.scss` als unveränderte Originalreferenz gespeichert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md` um Divider-Variante B mit technischer Einordnung ergänzt.
- `styleguide.md` um Regeln für Variante B ergänzt.
- `decision_log.md` um die Entscheidung zur gesicherten Variante-B-Referenz ergänzt.
- `nurovelle-animations.css` Abschnitt 7B als Nurovelle-Adaption mit Fallback-/Support-Logik ergänzt.
- `todo.md` um Vergleich der Pure-CSS-Angled-Sections gegen SVG- und Skew-Variante ergänzt.

Nicht geändert:

- `index.html`
- produktive Homepage-Struktur
- finale Divider-Auswahl

## 2026-07-07 – CTA-Originalreferenzen und Board-Option gesichert

Status: fertig

Geändert:

- `nurovelle-button-original-references.md`: neue Originalreferenzdatei für Arrow-Reveal, Press-Button und Golden-Button-Farblogik erstellt.
- `nurovelle-section-board-codepen-reference.md`: externe CodePen-Option für Section-/Board-Komponente dokumentiert.
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: CTA-System neu eingeordnet und Board-Option ergänzt.
- `styleguide.md`: CSS-first-Regel und Prüfkomponentenliste ergänzt.
- `decision_log.md`: Entscheidung zur Button-Originalreferenz und Board-Prüfoption ergänzt.
- `todo.md`: Prüfpunkte für Navigation, Burger, Breadcrumbs, Social Buttons, Hero, Divider, Cards, Board und CTA-System ergänzt.

Nicht geändert:

- `index.html`
- produktive Homepage
- finale CTA-Auswahl
- finale Board-/Section-Auswahl
- finale Divider-Auswahl

## 2026-07-07 – 8 Zusatzdateien in Projektfiles übernommen

Status: fertig

Geändert:

- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`: vollständiges Referenzarchiv für die 8 zuvor separat erzeugten Dateien ergänzt.
- `styleguide.md`: Regel ergänzt, dass die Einzeldateien nicht als eigenständige aktive Designquellen gelten.
- `decision_log.md`: Entscheidung zur Konsolidierung der Zusatzdateien dokumentiert.
- `task_contract.md`: Arbeitsregel gegen verstreute Referenzdateien ergänzt.
- `project_overview.md`: CSS-/Interaktionsreferenzen als konsolidierte Projektgrundlage aufgenommen.
- `todo.md`: Konsolidierung abgeschlossen und offene Prüfaufgaben ergänzt.

Übernommen:

1. `nurovelle_cta_button_preview.html`
2. `nurovelle-hero-orb-original.scss`
3. `nurovelle-hero-orb-original.haml`
4. `nurovelle-divider-diagonal-original-reference.txt`
5. `nurovelle-divider-svg-original-reference.txt`
6. `nurovelle-divider-pure-css-angled-original-reference.scss`
7. `nurovelle-button-original-references.md`
8. `nurovelle-section-board-codepen-reference.md`

Nicht geändert:

- `index.html`
- produktive Homepage
- finale Divider-Auswahl
- finale CTA-Auswahl
- finale Hero-Orb-/Cube-Entstehungslogik

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

### Prozess klären

`Welcher Geschäftsprozess verbessert werden soll und welches konkrete Ergebnis durch KI entstehen muss.`

`Mehr erfahren`

Card 2:

### Daten prüfen

`Welche Daten, Systeme und Wissensquellen bereits vorhanden sind und technisch nutzbar gemacht werden können.`

`Mehr erfahren`

Card 3:

### Umsetzung planen

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
