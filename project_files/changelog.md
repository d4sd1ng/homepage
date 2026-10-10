## 2026-10-09 – Issue #54 Leistungskarten-Interaktion und Divider korrigiert

Status: in Arbeit

Geändert:

- `homepage/index.html`: Klick auf eine Leistungskarte öffnet/schließt jetzt den `.is-active`-Zustand statt auf Desktop sofort zur Zielseite zu navigieren; Navigation erfolgt über den vorhandenen `Mehr erfahren`-CTA.
- `homepage/index.html`: rechter horizontaler Divider als eigenes Element `.nv-s7-card__short-rule` in allen 11 Leistungskarten umgesetzt; linker Horizontal-Divider, vertikaler Divider und rechter Horizontal-Divider bleiben im Grundzustand unsichtbar und werden nur bei Hover, Focus oder `.is-active` sichtbar.
- `homepage/index.html`: `Mehr erfahren` verwendet die vorhandene `golden-button`-Komponente; die kartenbezogene Klasse steuert nur Position und Größe.
- `homepage/index.html`: Desktop-Divider bleiben im separaten Mobile-Kartenlayout ausgeblendet.
- `homepage/index.html`: linken Inhaltsblock der geöffneten Leistungskarten um 16px nach oben gesetzt, damit Icon und Rahmen nicht zu tief sitzen.
- `homepage/index.html`: Nummernrahmen von 64.8×68px auf 52×54px und Nummernschrift von 31.2px auf 24px reduziert; Abstand zum Titelblock von 18.4px auf 14.4px reduziert.
- `homepage/index.html`: Bulletpoint-Texte gold gesetzt und die Bulletmarker auf grüne Emerald-Punkte umgestellt; gilt für Einsatzbereiche links und Bulletliste rechts.
- `homepage/index.html`: Einsatzbereich-Bullets links von 15.6px auf 14.4px reduziert und erzwungene Worttrennung entfernt, damit lange Begriffe wie `Daten- und Systemprüfung` und `Maßnahmenpriorisierung` vollständig innerhalb der linken Kartenspalte bleiben.

Nicht geändert:

- Texte, Kartenreihenfolge, IDs und Assetpfade.
- Formular-, Analyse-, Download-, FAQ- und Footer-Logik.
- Header-CTA und allgemeine `golden-button`-Basisregeln.

Offen:

- Visuelle Abnahme des Branches vor Merge.

## 2026-10-09 – Mobile Leistungskarten, SEO-Callouts und CTA-Padding korrigiert

Status: in Arbeit

Geändert:

- `homepage/index.html`: Issue #54 vollständig umgesetzt: linker kurzer Divider, vertikaler Divider und rechter Horizontal-Divider bleiben im Grundzustand unsichtbar und werden bei Hover, Focus oder `.is-active` eingeblendet.
- `homepage/index.html`: Abstand zwischen Icon-Rahmen und linkem kurzen Divider auf eine einzige bestehende Abstandsstufe reduziert; der doppelte Abstand aus Icon-Unterrand plus Divider-Oberrand entfällt.
- `homepage/index.html`: Hinweistext auf `Hover & Klick für mehr Informationen` geändert.
- `homepage/index.html`: `Mehr erfahren` der Leistungskarten auf dieselbe goldene Material-CTA-Sprache wie die übrigen CTAs umgestellt; Mobile-Goldstil bleibt erhalten.

- `homepage/index.html`: die drei Divider der Leistungskarten in Sektion 5 technisch erneut abgesichert: linker kurzer Divider unter dem Icon, vertikaler Divider und rechter horizontaler Divider sind im Grundzustand `opacity: 0` / `visibility: hidden` und werden ausschließlich bei Hover, Focus oder `.is-active` eingeblendet.
- `homepage/index.html`: der rechte horizontale Divider an `.nv-s7-card__points::before` besitzt jetzt eine eigene Sichtbarkeitslogik statt nur indirekt über die Sichtbarkeit des Punkteblocks zu erscheinen. Alle drei Divider bleiben 1.6px stark.

- `homepage/index.html`: Mobile-Leistungskarten bleiben direkt sichtbar; Bildhöhe von 140.8px auf 96px reduziert, Kartenabstand von 32px auf 20px reduziert und Innenabstände von Inhalt, Bulletpoints und CTA verdichtet.
- `homepage/index.html`: normale Mobile-CTAs behalten die bestehende goldene Optik; sichtbare Höhe von 40px auf 36px und horizontales Padding von 14px auf 10px reduziert. Header-CTA bleibt unverändert.
- `homepage/index.html`: drei vorhandene SEO-Toolbox-Callouts von maximal 980px auf maximal 620px reduziert; Mobile-Maximalbreite auf 320px begrenzt.
- `homepage/index.html`: SEO-Callout-Reveal von vertikalem Translate/Scale auf sichtbares Einfliegen von links plus Fade-in umgestellt; Reduced-Motion-Fallback bleibt erhalten.
- `project_files/styleguide.md`: freigegebene Mobile-/SEO-Callout-Regel auf Einflug von links und kompaktere Mobile-Ausführung präzisiert.
- `project_files/decision_log.md`: bestehende SEO-Callout-Entscheidung an die aktuelle Benutzervorgabe angepasst.
- `homepage/index.html`: Grundhintergrund von Hero und allen Homepage-Inhaltssektionen auf einheitlich `#0A1913` / `--color-deep-green` gestellt.
- `homepage/index.html`: normale dunkle Card-Flächen der Leistungskarten, Standard-Analyseangebote, Kontakt-Cards und Download-Cards auf Dark Gunmetal `#15191A` vereinheitlicht; grüne und goldene Card-Varianten unverändert gelassen.
- `homepage/nurovelle.css`: gemeinsame Detailseiten-Grundfläche auf `#080B09` und Standard-Panel-/Form-Card-Flächen auf Dark Gunmetal `#15191A` vereinheitlicht.
- `homepage/detail_*.html`: die vorhandenen Leistungsdetailseiten auf den matten fast schwarzen Grundhintergrund `#080B09` vereinheitlicht; standalone Chatbot-/Datenabgleich-Cards ebenfalls auf Dark Gunmetal gestellt.
- `project_files/styleguide.md`, `homepage.instructions.md`, `project_files/copilot_homepage_update.json` und `project_files/decision_log.md`: das neue Hintergrund- und Card-Farbsystem verbindlich dokumentiert.

Nicht geändert:

- Desktop-Leistungskarten und deren Hover-/Focus-Aufbau.
- Inhalte, Texte, IDs, Assetpfade und Kartenreihenfolge.
- Formular-, Analyse-, Download-, FAQ- und Footer-Logik.
- Header-CTA und Shared-Header/Footer-CSS.

Offen:

- Visuelle Abnahme auf realen Mobile-Breakpoints nach Deployment.

## 2026-10-07 – CTA-Stil auf bestehenden goldenen Analyse-CTA zurückgesetzt

Status: fertig

Geändert:

- Die zuvor fälschlich eingeführte dunkle Card-CTA-Optik für normale Mobile-CTAs wurde wieder entfernt.
- Normale Mobile-CTAs verwenden wieder die bestehende goldene `golden-button`-Optik der Analyse-Angebots-Cards.
- Projektstart- und Leistungskarten-CTAs werden auf Mobile an dieselbe goldene CTA-Sprache angeglichen.
- SEO-Toolbox-Callouts verwenden ebenfalls den normalen goldenen CTA.
- Header-CTA bleibt als einzige separat dimensionierte Variante bestehen.

## 2026-10-07 – Mobile Homepage systematisiert und SEO-Toolbox-Callouts ergänzt

Status: in Arbeit

Geändert:

- `homepage/index.html`: Mobile-Hero auf volle Inhaltsbreite umgestellt; automatische Silbentrennung und aggressive Wortumbrüche auf Mobile entfernt; Hero-Kicker lesbarer skaliert.
- `homepage/index.html`: gemeinsame mobile Section-Abstände für die Homepage zentralisiert und große mobile Leerhöhen reduziert.
- `homepage/index.html`: Abstand zwischen „Warum Nurovelle“-Bulletpoints und Video deutlich reduziert.
- `homepage/index.html`: Projektstart-Cardtexte mit zusätzlichem Innenabstand versehen.
- `homepage/index.html`: „Von der Idee zum Projekt“ zeigt auf Mobile alle drei vorhandenen Bild-/Text-Beispiele statisch untereinander; leere Slider-Zwischenzustände entfallen.
- `homepage/index.html`: normale mobile Homepage-CTAs auf die schmale längliche Form des bestehenden `Mehr erfahren`-Card-CTAs vereinheitlicht; einzeiliger Text; Header-CTA bewusst ausgenommen.
- `homepage/index.html`: Analyse-Bulletmarker auf `assets/bulletpoint.png` als grünen 3D-Punkt umgestellt.
- `homepage/index.html`: sechs Ablauf-Module auf Mobile deutlich kompakter skaliert.
- `homepage/index.html`: drei kompakte SEO-Toolbox-Callouts nach Projektidee, nach Leistungssektion und vor Downloads ergänzt; kurzer Fade-/Glow-Reveal per IntersectionObserver, Reduced-Motion-Fallback vorhanden.
- SEO-Callout verwendet ausschließlich die belegte Aussage „Kostenloser SEO-Check“ und verlinkt auf `detail_seo.html`; unbestätigte Tarifnamen „Agency“/„Pro“ wurden nicht verwendet.
- `project_files/styleguide.md`: verbindliches Homepage-Mobile-System und SEO-Callout-Regeln ergänzt.
- `project_files/decision_log.md`: aktuelle Mobile-, CTA-, Bullet- und SEO-Callout-Entscheidungen dokumentiert.

Nicht geändert:

- `homepage/shared-header-footer.css`; der Header-CTA bleibt als eigene Variante bestehen.
- Desktop-Layout außerhalb der bestehenden Mobile-Media-Query.
- Formulardaten, Feldnamen, Submission-, Consent-, Honeypot-, Success-/Error-Logik.
- bestehende Assetpfade und vorhandene Projektidee-/Ablaufbilder.

Geprüft:

- keine doppelten HTML-IDs im geänderten `homepage/index.html`.
- Anzahl öffnender/schließender `section`-, `aside`- und `script`-Elemente stimmt überein.
- Klammeranzahl für CSS/JavaScript im Gesamtfile ist ausgeglichen.
- drei SEO-Callouts und genau ein zugehöriger Observer sind vorhanden.
- keine neue `!important`-Regel hinzugefügt; die bisherige `!important`-Positionierung des mobilen Projektidee-Sliders wurde entfernt.

Offen:

- visuelle Abnahme der Breakpoints 320, 360, 390 und 430 px nach Deployment.
- Browserkonsolen- und reale Touch-Prüfung nach Deployment.

## 2026-10-07 – Hero-Randformen auf analyse.html als gefüllte CSS-Dreiecke neu aufgebaut

Status: in Arbeit

Geändert:

- Nur `homepage/analyse.html` geändert.
- Die bisherige schmale Linien-/Box-Shadow-Konstruktion unten links wurde vollständig entfernt.
- Vertikale Randform unten links neu aus vier ineinanderliegenden, vollflächigen CSS-Dreiecken aufgebaut:
  - äußerer Emerald-Verlauf
  - heller Gold-/Lichtverlauf
  - Goldverlauf
  - innerer Gunmetal-Verlauf
- Horizontale Randform unten rechts neu aus drei vollflächigen CSS-Dreiecken aufgebaut:
  - Emerald-Verlauf
  - Goldverlauf
  - Gunmetal-Verlauf
- Die Dreiecke teilen dieselbe Grundgeometrie; die horizontale Variante verwendet nur andere Proportionen.
- Die gestaffelten Goldlinien oben rechts bleiben unverändert.
- Hero-Text, CTA, Visual, Visual-Größe, Visual-Position, Header, Footer und weitere Sektionen bleiben unverändert.
- Noch kein Rollout auf weitere Detailseiten; zuerst Sichtprüfung auf `analyse.html`.

## 2026-10-07 – Untere linke Hero-Randform korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html` und alle 13 `homepage/detail_*.html`: die massive dreieckige Fläche unten links entfernt.
- Ersetzt durch eine schmale, nach unten aus dem Viewport laufende diagonale Randform aus Gold, Emerald und Gunmetal.
- Die Form endet nicht sichtbar im Hero, sondern läuft unterhalb des Viewports weiter.
- Die gestaffelten Goldlinien oben rechts bleiben unverändert.
- Keine Änderungen an Hero-Text, CTA, Visual, Header, Footer oder anderen Sektionen.

Ursache:

- Die vorherige `clip-path`-Fläche erzeugte einen großen dunklen Keil statt des gewünschten schmalen Randakzents.

## 2026-10-06 – SEO Toolbox an Seitenende und Nurovelle-Design angepasst

Status: in Arbeit

Geändert:

- `homepage/detail_seo.html`: bestehende Toolbox-Box aus dem Hero an das Ende des Hauptinhalts vor den Footer verschoben; maximal 800px und mobile Inhaltsbreite erhalten.
- `.nv-seo-inline`: vorhandenen Gold-3-Rahmen der Nurovelle-Komponenten übernommen.
- Hero: doppelten CTA `SEO-Potenzial analysieren` entfernt; `Kostenloser SEO-Check` mit bestehender ID `nv-seo-trigger` bleibt erhalten und verweist auf `#nv-seo-inline`.
- Kontaktbereich: `SEO-Potenzial analysieren` verweist auf `#nv-seo-inline` statt `analyse.html`.
- Toolbox-Repository, `apps/web/app/toolbox/embed/widget.css`: Exo 2 und Inter, Gunmetal-Fläche, Goldtitel, kompakte Auswahlfelder und helle Eingaben nach der vom Nutzer gelieferten Homepage-Analysevorlage. Vorhandene Webfonts unter `apps/web/public/toolbox/fonts/` wiederverwendet.

Nicht geändert:

- Header-CTA zur KI-Potenzialanalyse, Seitentexte, Assetpfade der Homepage, FAQ, Newsletterformular, Accounts, Login, Tarifprüfungen und Tool-Ausführung.

## 2026-10-06 – Hero-Randformen auf alle Detailseiten ausgerollt

Status: fertig

Geändert:

- Die auf `analyse.html` freigegebene CSS-Formsprache wurde auf alle 13 Dateien `homepage/detail_*.html` übertragen.
- Oben rechts: gestaffelte offene Goldlinien.
- Unten links: auslaufende Emerald-/Gunmetal-/Gold-Form.
- Keine Form unten rechts.
- Moderne Detailseiten mit `.hero-viewport` und ältere Detailseiten mit der ersten Hero-Section werden mit demselben CSS-Block unterstützt.
- Hero-Inhalt bleibt durch getrennte Z-Ebenen über den Dekorformen.
- Keine Änderungen an Header, Footer, Texten, CTA, Hero-Grafiken oder übrigen Sektionen.

## 2026-10-06 – Hero-Randformen sichtbar gemacht

Status: fertig

Geändert:

- `homepage/analyse.html`: Stacking-Kontext des Hero korrigiert.
- `.hero-viewport::before` (Goldlinien oben rechts) und `.hero-viewport::after` (auslaufende Form unten links) liegen jetzt über dem schwarzen Hero-Hintergrund.
- Der eigentliche Hero-Inhalt liegt weiterhin darüber.
- Keine Änderung an Form, Größe, Position, Farben, Text, CTA, Visual oder Shared Header/Footer.

Ursache:

- `#hero` hatte `z-index:1`, während beide Randformen auf `z-index:0` lagen. Da `#hero` eine deckende schwarze Fläche hat, wurden die Formen vollständig dahinter verdeckt.

## 2026-10-06 – Falsch gesetzte Hero-Form unten rechts entfernt

Status: fertig

Geändert:

- `homepage/analyse.html`: den unten rechts ergänzten Emerald-/Gold-Keil vollständig entfernt.
- Im Hero verbleiben nur die gestaffelten Goldlinien oben rechts und die auslaufende Form unten links.
- Keine Änderung an Text, CTA, Hero-Visual, Glow, Header/Footer oder anderen Sektionen.

Ursache:

- Der unten rechts gesetzte Keil entsprach in der Formsprache erneut der zuvor verworfenen Form 7 und widersprach damit der abgestimmten Komposition.

## 2026-10-06 – CSS-Randformen im Analyse-Hero als Pilot umgesetzt

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: ausschließlich im Desktop-Hero drei CSS-Randformen ergänzt.
- Oben rechts: gestaffelte offene Goldlinien nach der ausgewählten Form 3.
- Unten links: schmale Emerald-/Gunmetal-/Gold-Form, die bis an den unteren Viewportrand läuft und dort optisch ausläuft.
- Unten rechts: kleiner Emerald-/Gold-Keil als sekundärer Gegenakzent.
- Alle Formen liegen hinter dem Hero-Inhalt, reagieren nicht auf Pointer-Eingaben und verwenden keine zusätzlichen HTML-Elemente oder Bildassets.
- Vorhandene Hero-Texte, CTA, Visual-Größe, Visual-Position und Glow bleiben unverändert.
- Umsetzung zunächst nur auf `analyse.html`; Übertragung auf weitere Detailseiten erst nach Sichtprüfung und Freigabe.

Nicht geändert:

- `shared-header-footer.css`, `index.html`, übrige Detailseiten und Hero-Inhalte.

## 2026-10-06 – Analyse-Hero neu ausbalanciert

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Inhalt auf Desktop als Einheit um 80 px nach oben verschoben.
- Text und Visual bleiben in derselben vertikalen Grid-Achse zentriert.
- CTA-Abstand unter dem Fließtext von 78 px auf 38 px reduziert.
- Bestehende horizontale Visual-Position und bestehende Bildskalierung bleiben unverändert.
- Hinter dem Hero-Visual wurde ausschließlich per CSS-Pseudoelement ein dezenter dunkler Emerald-/Gunmetal-Glow ergänzt.
- Keine Card, kein Rahmen und keine zusätzlichen dekorativen Objekte ergänzt.
- Shared Header/Footer und übrige Sektionen unverändert.

## 2026-10-06 – SEO Toolbox als kompakte Inline-Box

Status: in Arbeit

Geändert:

- `homepage/detail_seo.html`: Toolbox unter dem bestehenden Hero eingebettet, maximal 800px breit und auf Mobile volle Inhaltsbreite. Der bestehende SEO-Check-CTA verweist auf die Box statt auf E-Mail.
- `.nv-seo-inline` und dessen iframe-Regel begrenzen die Box; die modale Widget-Einbindung wurde auf dieser Seite entfernt.
- `homepage/seo-toolbox-inline.js`: automatische iframe-Höhe mit Prüfung von Nachrichtenursprung und Absender; vorhandene Owner-Rückkehr wird an das Embed weitergegeben.

Nicht geändert:

- Seitentexte, Header, Footer, FAQ, Newsletterformular, Assetpfade und Toolbox-Zugriffsprüfung.
## 2026-10-04 – Sichtbaren Inhalt des Analyse-Hero-Visuals vergrößert

Status: fertig

Geändert:

- `homepage/analyse.html`: Das Hero-Bild bleibt an derselben Position und wird zusätzlich um seinen eigenen Mittelpunkt skaliert.
- Desktop ab 1101 px: `scale(1.6)`.
- Desktop/Tablet 901–1100 px: `scale(1.45)`.
- Grid, Textspalte, Hero-Position, Shared Header/Footer und übrige Sektionen bleiben unverändert.

Ursache:

- Die vorherige Änderung erhöhte zwar die CSS-Bildbreite, vergrößerte den sichtbaren Diagramminhalt aber kaum. Deshalb wird jetzt das gerenderte Bild selbst skaliert, ohne das Grid erneut zu verschieben.

## 2026-10-04 – Hero-Bild tatsächlich vergrößert, Position beibehalten

Status: fertig

Geändert:

- `homepage/analyse.html`: Desktop-Grid auf die vorherige Text-/Bildposition `1.35fr / .85fr` zurückgesetzt.
- Das Hero-Bild wird jetzt selbst auf 760 px Breite gesetzt; nicht nur seine Grid-Spalte.
- Das Bild wird relativ zur bestehenden Visual-Spalte zentriert, damit sein Mittelpunkt beim Vergrößern an derselben Position bleibt.
- Im Bereich 901–1100 px wird das Bild analog tatsächlich auf 680 px Breite gesetzt.
- Shared Header/Footer und übrige Sektionen unverändert.

Ursache:

- Die vorherige Änderung vergrößerte primär die rechte Grid-Spalte. Wegen `width:100%` am Bild blieb dessen effektive Größe an die Spaltenbreite gebunden; dadurch änderte sich vor allem die Position.

## 2026-10-04 – Hero-Bild der Analyse wieder vergrößert

Status: fertig

Geändert:

- `homepage/analyse.html`: Desktop-Hero-Visual wieder auf die zuvor verwendete Größe von maximal 760 px gesetzt.
- Desktop-Spaltenverhältnis wieder auf `1.08fr / 1.12fr` mit mindestens 560 px für die Visual-Spalte gesetzt.
- Tablet-Bereich 901–1100 px bleibt unverändert bei maximal 680 px.
- Shared Header/Footer und übrige Sektionen unverändert.

Ursache:

- Beim CSS-Cleanup war das Desktop-Hero-Visual von 760 px auf 650 px verkleinert und die Textspalte verbreitert worden.

## 2026-10-04 – Shared Footer zurückgesetzt, Analyse lokal korrigiert

Status: fertig

Geändert:

- `homepage/shared-header-footer.css` exakt auf den funktionierenden Stand vor den letzten beiden Footer-Eingriffen zurückgesetzt.
- `homepage/analyse.html`: nur dort `.footer, .footer * { box-sizing: border-box; }` ergänzt, weil die Seite bisher `border-box` ausschließlich auf `main` und dessen Inhalte beschränkte.
- `index.html` unverändert.

Nicht geändert:

- Shared Footer Grid, Typografie, Abstände und Inhalte.
- Header und übrige Seiten.

## 2026-10-04 – Shared Footer auf vier flexible Spalten zurückgestellt

Status: fertig

Geändert:

- `homepage/shared-header-footer.css`: Footer-Grid wieder auf vier flexible Spalten `1.35fr 1fr 1.2fr 1fr` gestellt.
- Die feste Kombination `320px / auto / 304px / auto` mit `space-between` wurde entfernt.
- Spaltenabstand auf 48 px gesetzt und `align-items:start` ergänzt.
- Änderung ausschließlich im Shared Footer; keine Seiten-spezifischen Footer-Regeln ergänzt.

Ursache:

- Der aktuelle Shared Footer verwendete feste und intrinsische Spaltenbreiten plus `space-between`. Dadurch konnte die vierte Spalte „Kontakt“ aus dem sichtbaren Bereich gedrückt werden. Die vorherige Box-Sizing-Korrektur allein änderte diese Grid-Geometrie nicht.

## 2026-10-04 – Grüne 3D-Bulletpoints auf Analyse-Seite wiederhergestellt

Status: fertig

Geändert:

- `homepage/analyse.html`: sämtliche echten Bulletpoint-Listen verwenden wieder den freigegebenen grünen 3D-Punkt aus `assets/bulletpoint.png`.
- Betroffen sind `.card-bullets`, `.label-list`, `.dot-list` und `.result-points`.
- Der Sonderfall in der goldenen Summary-Card verwendet ebenfalls denselben grünen 3D-Punkt statt eines dunklen bzw. goldenen Punktes.
- Die nummerierte `.num-list` bleibt unverändert, da sie keine Bulletpoints, sondern nummerierte Schritte verwendet.

Ursache:

- Bei der Konsolidierung der Analyse-CSS wurden die früheren 3D-Bullet-Regeln zusammen mit den Override-Schichten entfernt; dadurch fielen die Listen auf alte goldene/dunkle Punktregeln zurück.

## 2026-10-04 – CTA unter den Definitions-Cards zentriert

Status: fertig

Geändert:

- `homepage/analyse.html`: Der CTA `KI-Potenzialanalyse starten` sitzt mittig unter den beiden Definitions-Cards.
- Bestehende Abstände und Viewport-Höhe bleiben unverändert.

## 2026-10-04 – Abstände in der Definitionssektion vergrößert

Status: fertig

Geändert:

- `homepage/analyse.html`: Die Viewport-Höhe von `#was-ist-das` bleibt unverändert bestehen.
- Abstand zwischen Subline und den beiden Definitions-Cards auf Desktop auf 64 px erhöht.
- Abstand zwischen den Definitions-Cards und dem CTA auf Desktop auf 56 px erhöht.
- Auf Mobile werden 40 px zwischen Subline und Cards sowie 36 px zwischen Cards und CTA verwendet.
- Keine `!important`-Regeln ergänzt.

Nicht geändert:

- Cards, Texte, CTA-Ziel, Viewport-Logik und übrige Sektionen.

## 2026-10-04 – Analyse-Layout von Override-Schichten bereinigt

Status: fertig

Geändert:

- `homepage/analyse.html`: widersprüchliche Hero-, Viewport- und Section-Regeln aus mehreren historischen Korrekturblöcken entfernt.
- Die nachgeschobenen Style-Blöcke `DETAILSEITE — finale Proportionen und Abstände` und `analyse-layout-normalization` wurden aufgelöst.
- Hero, Definitionssektion und allgemeiner Section-Rhythmus besitzen jetzt eine einzige konsolidierte Layoutquelle ohne `!important`.
- Hero und `#was-ist-das` nutzen auf Desktop `min-height: calc(100dvh - var(--header-height))`.
- Die übrigen Inhaltssektionen nutzen auf Desktop ab 720 px Höhe ebenfalls die sichtbare Höhe unterhalb des Headers; bei kleineren Desktop-Höhen bleibt natürliche Inhaltshöhe mit 42 px Vertikalabstand.
- Aktuell wirksame Hero-Spaltenbreiten, Bildgrößen, Inhaltsbreiten und Abstände wurden in die konsolidierte Quelle übernommen.

Nicht geändert:

- Texte, CTA-Ziele, Formular-/API-Logik, Header/Footer, Breadcrumbs und fachliche Inhalte.
- Komponentenbezogene `!important`-Altlasten außerhalb des Hero-/Viewport-/Section-Layouts wurden nicht Bestandteil dieser Änderung.

## 2026-10-04 – Definitionssektion auf volle Viewport-Höhe gesetzt

Status: fertig

Geändert:

- `homepage/analyse.html`: Die eigenständige Sektion `#was-ist-das` nutzt auf Desktop jetzt wie der Hero die volle sichtbare Höhe unterhalb des Headers.
- `#was-ist-das` erhält `min-height: calc(100dvh - var(--header-height))`, `display:flex` und vertikale Zentrierung.
- Die bestehende Inhaltsbreite, beide Cards, Texte und der CTA bleiben unverändert.

Ursache:

- Eine spätere Normalisierungsregel setzte für alle Nicht-Hero-Sektionen `min-height:0` und `height:auto` mit `!important` und übersteuerte damit die ältere Viewport-Regel.

## 2026-10-04 – Hero der Potenzialanalyse auf volle sichtbare Höhe gezogen

Status: fertig

Geändert:

- `homepage/analyse.html`: Nach dem Herauslösen der Definitionssektion nutzt der Hero selbst auf Desktop jetzt die volle sichtbare Höhe unterhalb des Headers.
- Die bisherige `100dvh`-Mindesthöhe des leeren `.hero-viewport`-Wrappers wurde entfernt.
- `#hero` erhält `min-height: calc(100dvh - var(--header-height))` und zentriert seinen bestehenden Inhalt vertikal innerhalb dieser Fläche.

Nicht geändert:

- Hero-Texte, Hero-Grafik, CTA, Spaltenbreiten und nachfolgende Sektionen.

## 2026-10-04 – „Was ist eine KI-Potenzialanalyse?“ als eigene Sektion

Status: fertig

Geändert:

- `homepage/analyse.html`: Die Definition „Was ist eine KI-Potenzialanalyse?“ wurde aus dem bisherigen gemeinsamen `.hero-viewport` gelöst und als eigenständige normale Sektion direkt nach dem Hero angeordnet.
- Zwischen Hero und Definition sowie zwischen Definition und Ausgangslage steht jeweils der bestehende Section-Divider.
- Die vorhandenen beiden Inhaltskarten und ihre Texte bleiben unverändert.
- Unter den beiden Karten wurde der freigegebene CTA `KI-Potenzialanalyse starten` mit Ziel `#analyse-formular` ergänzt.

Nicht geändert:

- Hero-Inhalt, Analyseformular, API-Logik, übrige Sektionen und deren Texte.

## 2026-10-04 – SEO Toolbox und Automationen als Haupt-Breadcrumbs ergänzt

Status: fertig

Geändert:

- Die bestehende Hauptnavigation wurde auf allen 32 aktiven HTML-Seiten mit Breadcrumb-Header um zwei direkte Breadcrumbs erweitert.
- `SEO Toolbox` verlinkt auf `detail_seo.html`.
- `Automationen` verlinkt auf `detail_automationen.html`.
- Auf den Branchen-Unterseiten werden die vorhandenen relativen Pfade `../../detail_seo.html` und `../../detail_automationen.html` verwendet.
- Bestehende Breadcrumb-Dropdowns, Header-CTA und übrige Navigation wurden nicht verändert.

## 2026-10-04 – Rechter kurzer Divider aller Leistungs-Cards abgesichert

Status: fertig

Geändert:

- `homepage/index.html`: den rechten kurzen Horizontal-Divider nicht mehr als separates `.nv-s7-card__short-rule`-Element geführt.
- `homepage/index.html`: Divider direkt an `.nv-s7-card__points::before` gebunden. Da alle elf Leistungs-Cards denselben Punkteblock besitzen, wird der Divider jetzt bei jedem Hover-/Focus-/Active-Zustand zusammen mit diesem Block sichtbar.
- `homepage/index.html`: alle elf bisherigen `.nv-s7-card__short-rule`-Markup-Elemente entfernt; keine doppelte Divider-Implementierung bleibt bestehen.

Nicht geändert:

- vertikaler Divider, linker Horizontal-Divider, Card-Inhalte, Card-Größen, Hover-Höhe, Navigation und Leistungsreihenfolge.

## 2026-10-01 – Analyse-Divider, Prozesspfeile und Wiederholungsanteil korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: Divider der breiten Analyse-Card ist jetzt eine eigene mittlere Grid-Spalte zwischen zwei gleich breiten Inhaltsbereichen; damit liegt die Linie strukturell exakt in der Mitte.
- `homepage/index.html`: Prozesspfeile werden horizontal im Zwischenraum der sechs Schritte und vertikal auf Höhe der Modulmitten positioniert.
- `homepage/index.html`: Regler „Anteil automatisierbarer Aufgaben“ ersetzt durch „Anteil wiederkehrender Abläufe“.
- `homepage/index.html`: erklärender Hinweis ergänzt: „Wie viel dieser Arbeit läuft nach einem ähnlichen Muster ab?“
- `homepage/index.html`: Reglerbereich auf 0–100 % erweitert. Die bestehende Berechnungsformel nutzt denselben numerischen Faktor weiter.

Nicht geändert:

- IDs, JavaScript-Berechnungsformel, bestehende Formular-/API-Feldnamen, Datenfaktor, Stundensatzlogik und Ergebniskennzahlen.

## 2026-10-01 – Deep-Analyse-Preise spaltenweise ausgerichtet

Status: fertig

Geändert:

- `homepage/index.html`: „Einführungspreis“ und „Listenpreis“ bleiben in zwei Zeilen, ihre Preiswerte stehen jetzt in einer eigenen zweiten Spalte exakt untereinander.
- `homepage/index.html`: Preiswerte verwenden tabellarische Ziffern und sind rechtsbündig innerhalb der gemeinsamen Preisspalte.

Nicht geändert:

- Preiswerte, Texte, Card-Breite, übrige Analyse- und Paketpreise.

## 2026-10-01 – Deep-Preise und Analyse-Divider korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: Einführungspreis und Listenpreis der Tiefgehenden Potenzialanalyse stehen jetzt als zwei separate Zeilen ohne Trennpunkt untereinander.
- `homepage/index.html`: Divider der breiten oberen Analyse-Card direkt am gesamten 50/50-Split auf `left: 50%` verankert.
- `homepage/index.html`: bisherigen Divider an der rechten Spalte deaktiviert.

Nicht geändert:

- Preise selbst, Analyseberechnung, Card-Breiten, Sliderlogik, Formularlogik und übrige Sektionen.

## 2026-10-01 – Analyse-, Paket-, Projektstart- und Leistungsdetails korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: obere Analyse-Cards auf `1.28fr / .72fr` neu gewichtet; Ergebnis-Card kompakter und nach links ausgerichtet.
- `homepage/index.html`: linke Analyse-Card intern auf `1fr / 1fr` gesetzt, damit der Divider mittig sitzt.
- `homepage/index.html`: Slider auf `calc(100% - 64px)` verbreitert und Text-/Wert-Abstände auf festen `12px`-Gap reduziert.
- `homepage/index.html`: „Manuelle/repetitive Arbeit je Person“ auf „Repetitive Arbeit / Mitarb.“ geändert.
- `homepage/index.html`: Gauge auf `128px` und Ergebnis-Kennzahlkarten auf kompakte `148px`-Spalten gesetzt.
- `homepage/index.html`: Paketpreise über feste Preis-Spalte sauber untereinander ausgerichtet.
- `homepage/index.html`: Pfeile der „Mehr erfahren“-Buttons in Projektstart- und Leistungs-Cards vertikal nachjustiert.
- `homepage/index.html`: Hinweis „Klicken für mehr Informationen“ direkt unter die mittlere Projektstart-Card verschoben.
- `homepage/index.html`: alle drei Divider der Leistungs-Cards im aktiven Zustand mit höherem Stacking und klarerer Goldlinie abgesichert.
- `homepage/index.html`: Divider zwischen „Von der Idee zum Projekt“ und „Pakete“ auf `1.6px` mit stärkerem Gold-Glow angehoben.

Nicht geändert:

- Potenzialberechnung, Formularfelder/-logik, Paketpreise selbst, Card-Texte außerhalb der ausdrücklich genannten Beschriftung und übrige Sektionen.

## 2026-10-01 – Analyse-Cards neu gewichtet

Status: fertig

Geändert:

- `homepage/index.html`: obere Analyse-Card-Aufteilung von `1fr / 1fr` auf `1.14fr / .86fr` geändert, damit die Regler-Card breiter und die Ergebnis-Card schmaler wird.
- `homepage/index.html`: Gauge und Kennzahlenblock in der Ergebnis-Card linksbündig angeordnet und deren Spaltenabstand auf `20px` gesetzt.

Nicht geändert:

- Sliderbreite `calc(100% - 152px)`, innere Aufteilung der linken Regler-Card, Texte, Berechnung, Formularlogik und untere Analyse-Cards.

## 2026-10-01 – Analyse-Schieberegler auf 152 px Verkürzung korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: Desktop-Schieberegler der Potenzialanalyse von `calc(100% - 232px)` auf `calc(100% - 152px)` korrigiert.

Nicht geändert:

- Analyse-Spaltenverhältnis `.88fr / 1.12fr`, Labelbreite, Formularlogik, Inhalte und übrige Homepage-Bereiche.

## 2026-10-01 – Analyse-Schieberegler auf 232 px Verkürzung gesetzt

Status: fertig

Geändert:

- `homepage/index.html`: Desktop-Schieberegler der Potenzialanalyse von `calc(100% - 80px)` auf `calc(100% - 232px)` verkürzt.

Nicht geändert:

- Analyse-Spaltenverhältnis `.88fr / 1.12fr`, Labelbreite, Formularlogik, Inhalte und übrige Homepage-Bereiche.

## 2026-09-30 – Analyse-Styles und Header-CTA repariert

Status: geprüft

Geändert:

- `homepage/analyse.html`: wörtliche `\n`-Zeichen vor `:root` durch echte Zeilenumbrüche ersetzt. Die Seitentokens greifen damit wieder; Hero- und Abschnittsüberschriften haben ihre definierte Größe.
- `homepage/analyse.html`: vorhandenen statischen Goldverlauf für `h1` und `main h2` wiederhergestellt.
- `homepage/shared-header-footer.css`: bestehende `.golden-button`-Basis-, Hover- und Active-Regeln aus `homepage/index.html` für den gemeinsamen Header-CTA ergänzt; dessen Link-Unterstreichung entfernt und vorhandene Icon-Größe übernommen.

Nicht geändert:

- Texte, Assetpfade, Formular- und JavaScript-Logik sowie die goldene Definition-Card.

## 2026-09-30 – Shared Header-Offset zentralisiert und Gold-Card wiederhergestellt

Status: fertig

Geändert:

- Fixed-Header-Seitenoffset nach `shared-header-footer.css` verschoben.
- Lokalen Body-Headeroffset aus `index.html` und `analyse.html` entfernt.
- Negativen Hero-Versatz der Analyse entfernt; Hero verwendet regulären Abstand.
- Nicht autorisierte Änderung der goldenen Definition-Card vollständig auf den vorherigen Goldzustand zurückgesetzt.

## 2026-09-30 – Analyse sichtbare Hero-/Definition-Fehler korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: negativen Hero-Versatz entfernt und regulären oberen/unteren Hero-Abstand gesetzt.
- Lang laufende H1/H2-Goldanimation entfernt; Überschriften verwenden den Goldverlauf statisch und bleiben dauerhaft lesbar.
- Rechte Definition-Card von Orange auf dunkles Smaragd/Gunmetal mit bestehendem Goldrahmen umgestellt; Textfarben an das dunkle Material angepasst.

Nicht geändert:

- `homepage/shared-header-footer.css`, `homepage/nurovelle-tokens.css`, Inhalte, Formularlogik und übrige Sektionen.

## 2026-09-30 – Verlinkung zur KI-Automationen-Detailseite entfernt

Status: fertig

Geändert:

- KI-Automationen aus den Breadcrumb-Menüs der aktiven HTML-Seiten entfernt.
- `homepage/index.html`: Zielverlinkung der KI-Automationen-Servicekarte entfernt; `Mehr erfahren` bleibt optisch bestehen, ist aber kein Link mehr.
- `homepage/sitemap.xml`: Eintrag für `detail_automationen.html` entfernt.
- `homepage/detail_automationen.html` bleibt als Datei bestehen; Seiteninhalt, Canonical- und Open-Graph-URL wurden nicht verändert.

## 2026-09-30 – Shared Header/Footer vollständig aus index.html bereinigt

Status: fertig

Geändert:

- `homepage/shared-header-footer.css`: Footer-Werte auf den aktuellen freigegebenen `index.html`-Stand synchronisiert (`.footer` Padding, Footer-Titelabstand, `.footer-bottom` Abstand).
- `homepage/index.html`: 67 lokale, bereits in Shared vorhandene Header-/Footer-CSS-Regeln entfernt.
- `homepage/index.html` und `homepage/analyse.html` beziehen Header/Footer jetzt ausschließlich aus `shared-header-footer.css`; gemeinsame Layout-Tokens kommen aus `nurovelle-tokens.css`.

Geprüft:

- Keine lokalen Header-/Footer-Komponentenregeln mehr in `index.html`.
- Keine lokalen Header-/Footer-Komponentenregeln mehr in `analyse.html`.
- Beide Seiten laden `nurovelle-tokens.css` und `shared-header-footer.css` jeweils genau einmal.
- Keine Hero-, Inhalts- oder Sektionskomponente wurde in diesem Bereinigungsschritt geändert.

## 2026-09-30 – Analyse Shared-CSS-Ladereihenfolge korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: `nurovelle-tokens.css` und `shared-header-footer.css` werden jetzt wie auf `index.html` vor dem lokalen Seiten-CSS geladen.
- Späte doppelte Einbindungen der beiden Shared-Dateien entfernt.
- Dadurch stehen Header-Höhe, Logo-Größen, Page-Gutter und weitere Shared-Tokens bereits beim Aufbau der Seite zur Verfügung.

Nicht geändert:

- `homepage/shared-header-footer.css` und `homepage/nurovelle-tokens.css`.
- Texte, Definition-Cards und übrige Inhaltsmodule.

## 2026-09-30 – Analyse-Hero korrekt unter Fixed Header positioniert

Status: fertig

Geändert:

- `homepage/analyse.html`: bestehende Homepage-Basisregel `body { padding-top: var(--header-height); }` übernommen.
- Der Fixed Shared Header wird damit wieder im normalen Seitenfluss kompensiert; der Hero beginnt unterhalb des Headers.

Nicht geändert:

- `homepage/shared-header-footer.css`.
- Hero-Inhalte, Definition-Cards, Texte und übrige Sektionen.

## 2026-09-30 – Anwendungs-Cards kompakter gesetzt

Status: fertig

Geändert:

- `homepage/analyse.html`: „Vorbereitung von Daten, Prozessen oder Schnittstellen“ auf „Vorbereitung von Daten, Prozessen“ gekürzt.
- Innen-Padding der Anwendungs-Cards halbiert: Desktop `9px 12px` → `4.5px 6px`, kurze Desktop-Ansicht `7px 10px` → `3.5px 5px`.

Nicht geändert:

- Card-Höhen, Grid-/Reihenabstände, übrige Texte und andere Sektionen.
- `homepage/shared-header-footer.css`.

## 2026-09-30 – Analyse-Hero von Shared-Header-Höhe entkoppelt

Status: fertig

Geändert:

- `homepage/analyse.html`: verbliebene Hero-Viewport-Berechnungen mit `var(--header-height)` entfernt.
- Der Hero definiert keinen lokalen Header-Offset mehr; Header und Footer bleiben ausschließlich über `shared-header-footer.css` gesteuert.

Nicht geändert:

- `homepage/shared-header-footer.css`.
- Header-/Footer-Markup, Texte, Cards und übrige Inhaltssektionen.

# Changelog

## 2026-09-30 – SEO-Toolbox-Widget auf detail_seo.html eingebunden

Status: in Arbeit

Geändert:

- `homepage/detail_seo.html`: Stylesheet `https://seo.nurovelle.de/toolbox/widget.css` im Head eingebunden.
- `homepage/detail_seo.html`: im bestehenden Hero-CTA-Bereich den Link `Kostenloser SEO-Check` mit `id="nv-seo-trigger"`, bestehender Klasse `btn` und `mailto:info@nurovelle.de` als Ziel ergänzt.
- `homepage/detail_seo.html`: Skript `https://seo.nurovelle.de/toolbox/widget.js` mit `async` vor `</body>` eingebunden.

Nicht geändert:

- Bestehender CTA `SEO-Potenzial analysieren`, übrige Seiteninhalte, Assetpfade, CSS-Regeln und vorhandene JavaScript-Logik.

## 2026-09-30 – Homepage-Deploy auf VPS-Runner umgestellt

Status: in Arbeit

Geändert:

- `.github/workflows/deploy.yml`: Deploy-Job und Fehlerdiagnose laufen direkt auf einem self-hosted Linux-Runner mit Label `vps`; SSH-Aktionen wurden aus diesem Workflow entfernt.
- `.github/workflows/deploy.yml`: Deployment auf `main` beschränkt und den Checkout auf den exakten auslösenden Commit gesetzt.
- `.github/workflows/deploy.yml`: bestehende Versionsmarken, rsync-Ziele, Container-Neustart, Live-Prüfungen, Sitemap-/Robots-Prüfungen und Zertifikatsprüfung erhalten.
- VPS: offiziellen GitHub Actions Runner `2.337.0` mit geprüftem SHA-256 für `d4sd1ng/homepage` installiert, mit Label `vps` registriert und als systemd-Dienst aktiviert; GitHub meldet ihn online.
- `project_files/architecture.md`: Runner-Ausführung, Sicherheitsgrenze und verifizierten VPS-Status dokumentiert.
- `graphify-out/cross-project-relationships.json` und `graphify-out/cross-project-graph.json`: geplanten CTA, dokumentierte Projektbeziehungen und Runner-Zuordnung mit Evidenz festgehalten.

Nicht geändert:

- `.github/workflows/notify-nurovelle-system.yml` und der SEO-Toolbox-Deploy-Workflow.
- Homepage-HTML, sichtbare Texte, Layout, Assets und Formularlogik.

## 2026-09-29 – analyse.html vollständig auf Shared Header/Footer umgestellt

Status: fertig

Geändert:

- `homepage/analyse.html`: sämtliche lokalen Header-CSS-Regeln entfernt.
- `homepage/analyse.html`: sämtliche lokalen Footer-CSS-Regeln entfernt.
- Lokale Breadcrumb-, Logo-, Header-CTA-, Footer- und Mobile-Overrides entfernt.
- Lokale Deklarationen für `--header-height`, `--page-gutter`, `--logo-box`, `--logo-w` und `--logo-h` entfernt.
- Lokales `body padding-top` und `html scroll-padding-top` für den Header entfernt.
- `shared-header-footer.css` bleibt die einzige CSS-Quelle für Header und Footer.
- Seiten-CSS für Hero, Cards, Leistungsumfang, Anwendung, Formular und FAQ erhalten.
- Kein Merge nach `main`.

## 2026-09-29 – Analyse-Breitenkorrektur und Footer-Abstände auf Prüf-Branch

Status: fertig

Geändert:

- `homepage/analyse.html`: globale `.section-inner`-Breite wieder auf `1560px` gesetzt, damit Kicker, Titel, Subtitle und Bodytext ihre bisherige Position behalten.
- Nur die Inhaltsmodule `.analysis-intro-cards`, `#leistungen .num-list`, `#einsatzbereiche > .section-inner > .panel`, `#analyse-formular .analysis-layout` und `#faq .faq-grid` auf `1300px` begrenzt und zentriert.
- `homepage/shared-header-footer.css`: oberen Footer-Abstand von `43.2px` auf `21.6px` halbiert.
- Abstand zwischen Footer-Titel und folgendem Inhalt von `6.4px` auf `12.8px` verdoppelt.
- Footer-Legal-/Copyright-Bereich weiter nach unten gesetzt; `.footer-bottom`-Abstand oben von `27.2px` auf `54.4px` erhöht.
- Footer-Abstand unten auf `25px` gesetzt.

Nicht geändert:

- Hero-Inhalte
- Formularlogik
- API-Endpunkte
- Texte
- `main`

## 2026-09-29 – Shared Header/Footer in analyse.html korrekt angewandt

Status: fertig

Geändert:

- `homepage/analyse.html`: Header-Markup auf die aktuelle Struktur aus `index.html` umgestellt.
- `homepage/analyse.html`: Footer-Markup auf die aktuelle Struktur aus `index.html` umgestellt.
- Homepage-Anker im Shared Header/Footer für die Detailseite auf `index.html#...` angepasst.
- Footer-"Nach oben"-Link bleibt lokal auf `#hero`.
- `shared-header-footer.css` wird nun nach allen seitenlokalen Styles geladen und ist damit die maßgebliche Header-/Footer-CSS.
- Lokale `!important`-Overrides für Footer-Divider und Footer-Titelabstand entfernt.
- Keine Inhaltssektion außerhalb Header/Footer verändert.

## 2026-09-29 – Analyse-Sektionsbreite und Bullet-Einzug korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: globale Inhaltsbreite der Analyse-Sektionen von `1560px` auf `1300px` gesetzt.
- `homepage/analyse.html`: `.label-list` und `.dot-list` um `30px` nach rechts eingerückt.
- Anwendung, Leistungsumfang und weitere Sektionen folgen damit derselben 1300px-Inhaltsbreite.
- Footer-Abstände noch nicht verändert; Ursache des fehlenden Titelabstands identifiziert: `--nv-space-md` ist nicht definiert.

## 2026-09-29 – Definition-Cards in analyse.html auf 1300px verbreitert

Status: fertig

Geändert:

- `homepage/analyse.html`: `.analysis-intro-cards` von `max-width: 1200px` auf `max-width: 1300px` gesetzt.
- Zentrierung bleibt unverändert.
- Keine weiteren Layout- oder Inhaltsänderungen.

## 2026-09-29 – Hero-Text in analyse.html gekürzt

Status: fertig

Geändert:

- `homepage/analyse.html`: Satz „Grundlage ist Ihr tatsächlicher Betrieb: bestehende Abläufe, Datenquellen und Systeme statt allgemeiner Annahmen.“ aus dem Hero entfernt.
- Card-Breite nicht verändert; aktuell weiterhin `1200px`, da für die gewünschte Verbreiterung noch kein Zielwert festgelegt wurde.

## 2026-09-29 – Footer-Divider in analyse.html auf volle Viewportbreite gesetzt

Status: fertig

Geändert:

- `homepage/analyse.html`: `.footer::before` auf `width: 100vw` gesetzt.
- Der Divider wird über `left: 50%` und `translateX(-50%)` viewportzentriert.
- Damit läuft der Footer-Divider unabhängig von Contentbreite und Footer-Padding über die komplette Seitenbreite.
- Keine weiteren Layoutbereiche verändert.

## 2026-09-29 – Divider und Footer-Abstand in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: normale Section-Divider auf `0.8px` und den Homepage-Goldverlauf gesetzt.
- `homepage/analyse.html`: Footer-Abschlussdivider explizit über `.footer::before` sichtbar abgesichert.
- `homepage/analyse.html`: Abstand zwischen Footer-Titel und folgendem Inhalt auf `var(--nv-space-md)` gesetzt.
- Keine weiteren Inhalte oder Layoutbereiche verändert.

## 2026-09-29 – Hero-Titel und Definition-Cards in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Titel in zwei feste Zeilen aufgeteilt.
- `homepage/analyse.html`: Desktop-Hero-Spalten so angepasst, dass die erste Titelzeile nicht intern umbrechen kann.
- `homepage/analyse.html`: die beiden Definition-Cards auf `max-width: 1200px` gesetzt und horizontal zentriert.
- Keine weiteren Inhalte oder Sektionen verändert.

## 2026-09-29 – Grüne 3D-Bullets aus index.html in analyse.html übernommen

Status: fertig

Geändert:

- `homepage/analyse.html`: normale Bulletpoints verwenden jetzt exakt `assets/bulletpoint.png` wie auf `index.html`.
- Betroffen: `.label-list`, `.dot-list` und `.card-bullets`.
- Der bestehende grüne Rand `#55863f` und die runde Darstellung wurden übernommen.
- Nummerierte Punkte `01–08` im Leistungsumfang bleiben unverändert.

## 2026-09-29 – Hero-Bildpfad in analyse.html korrigiert

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Bildpfad von `assets/Module/detail_pages_grafics/Analyse_detail _final.png` auf den tatsächlich vorhandenen Pfad `assets/detail_pages_grafics/Analyse_detail _final.png` korrigiert.
- Keine weiteren Inhalte oder Layoutregeln verändert.

## 2026-09-29 – Doppelten Footer-Divider in analyse.html entfernt

Status: fertig

Geändert:

- `homepage/analyse.html`: lokale `.footer { border-top: ... }`-Regeln entfernt.
- `homepage/analyse.html`: lokale `.footer-bottom { border-top: ... }`-Regeln entfernt.
- Der Footer verwendet damit nur noch den gemeinsamen Divider aus `shared-header-footer.css` über `.footer::before`.
- Keine Footer-Inhalte oder Abstände verändert.

## 2026-09-29 – Hero-Titel analyse.html zweizeilig festgelegt

Status: fertig

Geändert:

- `homepage/analyse.html`: Hero-Titel mit festem Zeilenumbruch nach „Ihrem“.
- Darstellung: „Wo lohnt sich KI in Ihrem“ / „Unternehmen wirklich?“.
- Keine weiteren Inhalte oder Layoutregeln verändert.

## 2026-09-29 – analyse.html auf Homepage-Breite und Shared Header/Footer umgestellt

Status: fertig

Geändert:

- `homepage/analyse.html`: globalen `body { zoom: 0.8; }`-Hack entfernt.
- `homepage/analyse.html`: Contentbreite auf `1560px` und Seiten-Gutter auf das aktuelle `index.html`-System `clamp(19.2px, 4.8vw, 96px)` angeglichen.
- `homepage/analyse.html`: `nurovelle-tokens.css` und `shared-header-footer.css` eingebunden.
- `homepage/analyse.html`: drei nachträgliche lokale Header-Override-Blöcke entfernt, damit der Shared Header die maßgebliche CSS-Quelle ist.
- `homepage/analyse.html`: Section-Abstände vereinheitlicht und alte Verschiebungs-Hacks (`translateY`, große künstliche Bottom-Margins) neutralisiert.
- Formularstruktur, Pflichtfelder, Honeypot sowie API-/Success-/Error-Logik nicht verändert.

## 2026-09-29 – Zwei CTAs in Leistungssektion ergänzt

Status: fertig

Geändert:

- `homepage/index.html`: unter den 11 Leistungs-Cards in Sektion 5 zwei Golden-CTAs ergänzt.
- CTA 1: `Potenzialanalyse starten` → `#potenzialanalyse`.
- CTA 2: `Erstgespräch vereinbaren` → `#kontakt`.
- Bestehenden Golden-CTA-Stil verwendet; keine Card-Struktur oder übrigen Sektionen verändert.

## 2026-09-28 – Hover-State am Analyseformular-CTA ergänzt

Status: fertig

Geändert:

- `homepage/index.html`: der Submit-Button `.nv-aform__submit` übernimmt jetzt denselben Hover- und Focus-State wie die bestehenden Golden-CTAs.
- `homepage/index.html`: Active-State für `.nv-aform__submit` ergänzt.
- Keine Formularinhalte, Größen oder Abstände verändert.

## 2026-09-28 – Service-Card-Wappen mit echter Goldumrandung

Status: fertig

Geändert:

- `homepage/index.html`: das Wappen/Result-Icon in den Service-Cards verwendet jetzt eine echte durchgehende `1.6px` Gold-Border.
- Die bisherige Konstruktion aus goldener Außenform und schwarzer Innenform wurde entfernt.
- `box-sizing: border-box` hält die vorhandene Icon-Gesamtgröße unverändert.
- Keine Card-Größen, Texte, Abstände oder Positionen verändert.

## 2026-09-28 – Ablaufpfeile horizontal ausgerichtet

Status: fertig

Geändert:

- `homepage/index.html`: die wechselnden `rotate(36deg)`-/`rotate(-36deg)`-Regeln der Ablaufpfeile entfernt.
- Alle fünf Pfeile verwenden jetzt dieselbe bereits vorhandene Position `top: 42px; left: 88%` ohne Rotation.
- Keine Grafikgrößen, Texte oder sonstigen Abstände geändert.

## 2026-09-28 – Service-Card-Divider ausgerichtet und Ablaufgrafiken vereinheitlicht

Status: fertig

Geändert:

- `homepage/index.html`: horizontalen Divider unter dem Service-Card-Iconrahmen mittig zwischen Iconrahmen und „Einsatzbereiche“ gesetzt (`margin: 14px 0`).
- `homepage/index.html`: alle sechs Ablaufgrafiken auf denselben bereits vorhandenen Skalierungswert `0.58` gesetzt.
- Unterschiedliche Odd-/Even-Skalierung der Ablaufgrafiken entfernt.
- Keine Texte, Pfeile, Grafikquellen, Card-Größen oder übrigen Abstände verändert.

## 2026-09-28 – Abschnitts- und Footer-Divider vereinheitlicht

Status: fertig

Geändert:

- `homepage/index.html`: Abschnitts-Divider von 1.6px auf 0.8px reduziert.
- `homepage/index.html`: FAQ-Divider direkt vor dem Footer entfernt, damit dort nicht zwei Divider übereinander liegen.
- `homepage/index.html`: oberer Footer-Divider auf volle Breite gesetzt (`left: 0; right: 0`) und auf 0.8px reduziert.
- `homepage/index.html`: internen Divider von `.footer-bottom` entfernt.
- `homepage/shared-header-footer.css`: Footer-Divider und `.footer-bottom` synchron angepasst.
- Keine Inhalte, Abstände oder Spalten des Footers verändert.

## 2026-09-28 – Ablauf-Titel getrennt und Prozessgrafiken halbiert

Status: fertig

Geändert:

- `homepage/index.html`: Ablauf-Headline nach „Vom Geschäftsprozess“ getrennt; „zur KI-Lösung“ steht vollständig in der zweiten Zeile.
- `homepage/index.html`: bestehende Skalierung der sechs Ablaufgrafiken inklusive Sockel exakt halbiert (`1 → 0.5`, `0.86 → 0.43`, `1.16 → 0.58`).
- Grafik-Containerhöhen, Beschriftungen, Pfeile, CTA-Abstände und übrige Sektionseinstellungen nicht verändert.

## 2026-09-28 – Service-Card-Divider im geschlossenen Zustand vollständig verborgen

Status: fertig

Geändert:

- `homepage/index.html`: linker kurzer Divider, vertikaler Divider und rechter horizontaler Divider erhalten im geschlossenen Zustand zusätzlich `visibility: hidden`.
- Hover, Focus und `.is-active` setzen die drei Divider explizit auf `visibility: visible` und `opacity: 1`.
- Keine Card-Positionen, Texte, Größen oder Grid-Werte geändert.

## 2026-09-28 – Service-Card-Divider-Fix in aktuellen Refactor-Branch übernommen

Status: fertig

Geändert:

- `homepage/index.html`: die bereits auf `fix/service-card-dividers` vorhandene Divider-Logik in den aktuellen Branch `refactor/shared-header-footer-tokens` übernommen.
- Geschlossene Leistungskarten: linker kurzer Divider, vertikaler Divider und rechter horizontaler Divider sind jetzt `opacity: 0`.
- Geöffnete Leistungskarten: alle drei Divider werden bei Hover, Focus oder `.is-active` mit `opacity: 1` eingeblendet.
- Die drei Divider verwenden 1.6px in der Karten-CSS, damit sie unter dem vorhandenen `zoom: 0.65` sichtbar bleiben.
- Keine Card-Positionen, Texte oder sonstigen Bereiche verändert.

## 2026-09-28 – Erste Header-Basisregeln aus index.html entfernt

Status: fertig

Geändert:

- `homepage/index.html`: ausschließlich die bereits 1:1 in `shared-header-footer.css` vorhandenen Basisregeln für `.site-header`, `.site-header::after` und die Desktop-Basisregel von `.header-inner` entfernt.
- Responsive `.header-inner`-Regeln, Logo-, Breadcrumb-, CTA-, Footer-, globale CTA- und Token-Regeln unverändert gelassen.
- `homepage/shared-header-footer.css` in diesem Schritt nicht verändert.

## 2026-09-28 – Footer-Divider an Abschnittssystem angepasst

Status: fertig

Geändert:

- `homepage/index.html`: den vollbreiten `border-top` des Footers entfernt.
- `homepage/index.html`: Footer-Divider als eingerückten 1.6px-Verlauf mit `left: 7%` / `right: 7%` und Glow umgesetzt, analog zu den übrigen Abschnitts-Dividern.
- `homepage/shared-header-footer.css`: dieselbe Footer-Divider-Regel synchron übernommen.
- Keine Footer-Inhalte, Abstände oder Spalten verändert.

## 2026-09-28 – Shared Header/Footer Stylesheet in index.html eingebunden

Status: fertig

Geändert:

- `homepage/index.html`: `shared-header-footer.css` direkt nach `nurovelle-tokens.css` eingebunden.
- Noch keine Header- oder Footer-Regeln aus dem Inline-CSS entfernt.
- `homepage/shared-header-footer.css` nicht verändert; der vollständige Header-Regelsatz wurde zuvor gegen `index.html` abgeglichen und stimmt regelweise inklusive doppelter Responsive-Selektoren überein.

## 2026-09-28 – Header-Abhängigkeiten in Produktions-Tokens ergänzt

Status: fertig

Geändert:

- `homepage/nurovelle-tokens.css`: die aktuell in `index.html` verwendeten Header-/CTA-Abhängigkeitswerte ergänzt, damit die spätere schrittweise Auslagerung in `shared-header-footer.css` ohne Wertverlust möglich ist.
- `--header-height` und `--page-gutter` auf die aktuell tatsächlich in `index.html` verwendeten Werte gesetzt.
- Logo-Größen, Gold-/CTA-Materialwerte und die vom Header-CTA benötigten Shadow-Werte aus `index.html` übernommen.
- `homepage/index.html` und `homepage/shared-header-footer.css` nicht verändert.

## 2026-09-25 – Analyse-Regler und Consent-Cards korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: Desktop-Schieberegler auf `calc(100% - 80px)` gekürzt.
- Datenschutz- und Newsletter-Card explizit auf jeweils eigene Grid-Zeile und volle Formularbreite gesetzt.
- Keine zusätzlichen CSS-Override-Blöcke angelegt.

## 2026-09-25 – Schieberegler im Richtwert-Rechner gekürzt

Status: fertig

Geändert:

- `homepage/index.html`: ausschließlich die drei Desktop-Schieberegler in „Richtwert berechnen“ deutlich gekürzt (`calc(100% - 72px)` statt `calc(100% - 24px)`).
- Mobile Regel bleibt unverändert bei `width: 100%`.

## 2026-09-25 – Tiefenstaffelung der Ablaufmodule korrigiert

Status: fertig

Geändert:

- `homepage/index.html`: perspektivische Odd/Even-Tiefenstaffelung (`0.86` / `1.16`) der sechs Ablaufmodule wiederhergestellt.
- Nur die vertikale Modulposition zum Sockel wurde auf den Wert des ersten Moduls (`--nv-module-top: 13.6px`) vereinheitlicht; die individuellen Perspektivwinkel bleiben erhalten.

## 2026-09-25 – Paket-Hinweis an Card-Grid ausgerichtet

Status: fertig

Geändert:

- `homepage/index.html`: Hinweistext unter den drei Automationspaketen auf dieselbe maximale Breite und horizontale Zentrierung wie das bestehende Paket-Card-Grid gesetzt.
- `homepage/index.html`: Beträge in den Paket-Cards rechtsbündig angeordnet; die zugehörigen Preisbeschreibungen stehen links.
- `homepage/index.html`: die drei Range-Balken in „Richtwert berechnen“ um 24px gekürzt; Card-Breite, Spalten, Texte, Werte und Auswahlfelder unverändert.
- `homepage/index.html`: Datenschutz- und Newsletter-Card im Analyseformular untereinander über die volle Formularbreite angeordnet.
- `homepage/index.html`: alle sechs Ablaufmodule erhalten dieselbe Skalierung und vertikale Position zum Sockel wie das erste Modul „Aufgabe erfassen“.

Nicht geändert:

- Paket-Cards, Texte, Section-Layout, Header, Footer, übrige Homepage-Bereiche und JavaScript.

## 2026-09-21 – Analyse-Datei: Hero-Viewport und Sektionsabstände

Status: geprüft

Geändert:

- `homepage/analyse_bereinigt_hero_viewport_typo_fix (1).html`: Hero-Mindesthöhe an vorhandenen Body-Zoom angepasst; Einstiegskarten schließen den ersten Desktop-Viewport ab.
- Hero-Mindesthöhe zusätzlich um die Divider-Höhe (2 CSS-Pixel) reduziert, damit die Linie innerhalb des ersten Desktop-Viewports sichtbar ist.
- `.section-divider`: vorhandenen Goldverlauf der Sektionslinien übernommen; doppelte Pseudo-Divider ersetzt, vorhandene FAQ-Trennung als Divider-Element erhalten.
- Sektionsabstände sowie Kicker-/Titel-/Untertitel-/Inhaltsabstände vereinheitlicht; konkurrierende Höhenregeln entfernt, Inhaltssektionen dürfen bei Platzbedarf wachsen.
- `main h2`: Schriftgröße um 2 CSS-Pixel erhöht.

Nicht geändert:

- Texte, IDs, Assetpfade, Schriftfamilien, Header, Footer und JavaScript einschließlich Formular-/API-Logik.


## 2026-09-06 – Bildregeln für Social-/Content-Posts

Status: fertig

Geändert:

- `styleguide.md`: neuer Abschnitt 17a „Bildstil für Social-Media- und
  Content-Posts" – keine Personen-/Hände-/Schreibtischfotografie in
  generierten Post-Bildern, Verweis auf die bereits freigegebene
  Modulwelt aus Abschnitt 14 als Standardmotiv für Abläufe/Fähigkeiten,
  Warnhinweis zur bekannten Hologramm-Falle bei abstrakt beschriebenen
  Datenverbindungs-Motiven.
- `styleguide.md`, Abschnitt 17a: Absatz „Richtungsreferenzen" ergänzt –
  verweist auf die neuen Bilder in `austausch/an-team/vorlagen/nurovelle/`
  (`1.png`–`16.png`, `reference_posting_*.png`) als Stimmungsreferenz,
  nicht als fertige Assets; haelt zwei erkennbare Richtungen fest
  (Server-/Rechenzentrums-Fotografie mit Workflow-Panels und
  Dashboard-Requisiten; dunkle Wuerfel-/Modul-Cluster mit goldener
  Kantenbeleuchtung und Zahnraedern als Ausfuehrung von Abschnitt 14).
- `decision_log.md`: passender Eintrag ergänzt.

Nicht geändert:

- Abschnitt 17 (Website-Assets) und alle übrigen Abschnitte bleiben
  unverändert.
- Die bestehende VERBOTEN-Liste in Judes eigenem Rollentext (u.a.
  „Platinen") ist NICHT Teil dieser Änderung und wurde hier bewusst
  nicht in den Styleguide übernommen, da sie nie freigegeben war und
  echten Assets widerspricht (siehe `decision_log.md`).

## 2026-08-29 – Homepage-Abstände, Kartenflächen, FAQ und Analyse-Header

Status: fertig

Geändert:

- `homepage/index.html`: Hero-Kicker auf Weiß gesetzt, Subtitle-/Body-Abstand und CTA-/Statistikabstand korrigiert.
- `homepage/index.html`: Kartenflächen und Ergebnisrahmen auf `--color-emerald` vereinheitlicht; Kartenrahmen erscheint beim gemeinsamen `is-visible`-Reveal.
- `homepage/index.html`: Deep-Potenzialanalyse-Text erweitert, CTA näher an den Text gesetzt und FAQ-Elemente auf gleiche Spaltenbreite gestreckt.
- `homepage/analyse.html`: Header-CTA durch `Erstgespräch vereinbaren` mit Calendly-Link ersetzt.

Nicht geändert:

- Bestehende Formular-, API-, Lead-, Newsletter- und Notion-Integrationen.
- Bestehende IDs, Assetpfade, Kartenlinks und JavaScript-Logik.

## 2026-08-30 – Stripe-Testkonfiguration angelegt

Status: fertig

Geändert:

- `homepage/stripe-config.js`: neu angelegt. Setzt `window.NUROVELLE_STRIPE_PUBLISHABLE_KEY` (Publishable Key des Testmodus) und `window.NUROVELLE_STRIPE_MODE` (`test`) nach der bestehenden `window.NUROVELLE_*`-Konvention aus `analyse.html`. Reine Konfiguration, keine Bezahllogik.
- `architecture.md`: Abschnitt „Stripe-Konfiguration" ergänzt.
- `todo.md`: Abschnitt „Zahlung / Stripe" mit drei offenen Punkten ergänzt.

Nicht geändert:

- HTML-Seiten unter `homepage/`: die Datei ist in keiner Seite eingebunden.
- Layout, Texte, Farben, Fonts, Assets, Formular- und Analyse-Logik.
- `.github/workflows/deploy.yml`: der rsync-Ausschluss betrifft keine `.js`-Dateien, die Datei wird ohne Anpassung mit ausgerollt.

Anmerkung: Der Publishable Key ist für den Browser bestimmt und deshalb öffentlich; der Secret Key (`sk_...`) gehört nicht in dieses Repository.

## 2026-08-14 – Goldwort-Regel nach Medium getrennt, ein Goldverlauf für Dokumente

Status: fertig

Geändert:

- `styleguide.md`: Goldwort-Regel nach Medium getrennt (Website: ganze Überschrift; alles andere: ein tragendes Wort). Neuer Abschnitt „Goldverlauf in Dokumenten" mit dem dreistufigen Verlauf und der Begründung, warum der siebenstufige Website-Verlauf dort nicht taugt.
- `decision_log.md`: Eintrag zur Goldwort-Regel entsprechend präzisiert, zweiter Eintrag zum Dokumentverlauf ergänzt.

Nicht geändert:

- `--gold-1` in den 14 HTML-Dateien: der Website-Verlauf bleibt unverändert.
- Produktionscode, Farben, Komponenten, Assets.

Anmerkung: Die Vorlagen für Briefkopf, Angebot, Projektvertrag, AVV und E-Mail-Signatur liegen ausserhalb dieses Repos unter `Jude/data/marke/`. Sie verwenden den dreistufigen Dokumentverlauf.


## 2026-08-14 – Fontsystem auf Exo 2 + Inter, Goldwort-Regel, Regeln für das Agenten-Team

Status: fertig

Geändert:

- `decision_log.md`: fünf neue Entscheidungen aufgenommen (Exo 2 + Inter als Fontsystem, Goldwort-Regel, Wortmarke immer gold, keine Platzhalterwerte, Lesezugriff des Agenten-Teams, Newsletter ohne Gestaltung). Der Eintrag vom 2026-07-31 (Tapera + Inter) ist als abgelöst gekennzeichnet, nicht entfernt.
- `styleguide.md`: Abschnitt 4 auf Exo 2 + Inter umgestellt, Liste abgelöster Fontstacks entfernt; Abschnitt 3 um die Goldwort-Regel ergänzt.
- `nurovelle-tokens.css` (in `project_files/`): `--font-display` von Tapera auf Exo 2 umgestellt.
- `homepage/nurovelle-tokens.css`: `--font-display` und `--font-technical` von Eastman Grotesque Alt auf Exo 2 umgestellt. Die beiden Dateien waren inhaltlich auseinandergelaufen.
- `task_contract.md`: Abschnitte „Platzhalter" und „Agenten-Team" ergänzt.
- `todo.md`: Webfont-Einbindung, Prüfung des Produktionscodes auf alte Fontstacks, Umsetzung der Goldwort-Regel, doppelte Tokens-Datei und nicht eingecheckte Gold-SVGs als offen aufgenommen.

Nicht geändert:

- `index.html` und übriger Produktionscode
- Farben, Abstände, Komponenten und Layout
- Assets im Repo
- `project_overview.md` und `architecture.md`

Anmerkung: Die Schriftdateien selbst liegen ausserhalb des Repos unter `/usr/local/share/fonts/nurovelle/` (Exo 2 und Inter, variable TrueType, jeweils mit OFL-Lizenztext). Die Einbindung als Webfont steht noch aus und ist in `todo.md` geführt.

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

## 2026-08-14 – Projectfiles entflechtet und konsolidiert

Status: fertig

Geändert:

- `project_overview.md`: auf Projektumfang, Conversion-Pfade, Homepage-Struktur und Projektziel reduziert; Stand 2026-07-14 übernommen.
- `task_contract.md`: auf reine Arbeits-, Änderungs- und Dokumentationsregeln reduziert.
- `styleguide.md`: als alleinige Designquelle konsolidiert; Tapera + Inter, Nurovelle-Materialsprache, Goldsystem, Metallic-Gold-Verlauf, CTA-, Card-, Download-, Hero- und Bildregeln zusammengeführt.
- `architecture.md`: neu als alleinige technische Architektur- und Integrationsquelle angelegt.
- `assets.md`: aus vorhandener Assetliste als alleinige Asset-/Pfadquelle konsolidiert.
- `todo.md`: auf ausschließlich offene/laufende Aufgaben reduziert.
- `decision_log.md`: auf Entscheidungen mit Verweisen zur jeweils zuständigen aktiven Datei reduziert.
- `nurovelle-tokens.css`: Designhoheit vom alten Implementation Brief auf `styleguide.md` umgestellt; Fontsystem auf Tapera + Inter synchronisiert; Metallic-Gold- und CTA-Materialtokens aufgenommen.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: als aktive Quelle stillgelegt und auf Archiv-/Weiterleitungsfunktion reduziert.

Nicht geändert:

- `index.html`
- produktive Homepage
- `shared-header-footer.css`
- `NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md`
- reale Backend-/API-Systeme
- reale Notion-/Mail-/Lead-Integrationen
- Assetdateien selbst

## 2026-10-02 – SEO-Widget nach CDN-404 wieder erreichbar

Status: geprüft

Geändert:

- `homepage/detail_seo.html`: bestehende Widget-Skript-URL mit `?v=1fa290b9` versioniert, damit der nach einem Toolbox-Neustart zwischengespeicherte 404-Eintrag umgangen wird.

Nicht geändert:

- Widget-CSS, CTA, Seitentexte, Assetpfade und vorhandene JavaScript-Logik.
