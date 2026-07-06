# Changelog

## 2026-07-02

Status: fertig

Änderung:
- `styleguide.md` erstellt.
- Dokumentierte Website-, Asset- und Content-Dokument-Regeln aus Projektübersicht, Task Contract und Decision Log in einer zentralen Styleguide-Datei konsolidiert.

Geändert:
- Neue Datei: `styleguide.md`

Nicht geändert:
- `project_overview.md`
- `task_contract.md`
- `decision_log.md`
- `todo.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`

## 2026-07-02 – CSS-FIRST-Regel ergänzt

Status: fertig

Änderung:
- CSS-FIRST-Regel für steuerbare Website-Komponenten ergänzt.
- Regel in `task_contract.md` als verbindliche Arbeitsregel eingetragen.
- Regel in `styleguide.md` als Gestaltungs- und Umsetzungsregel eingetragen.
- Entscheidung in `decision_log.md` dokumentiert.

Geändert:
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `changelog.md`

Nicht geändert:
- `project_overview.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`

Hinweis:
- `todo.md` war im aktuellen `/mnt/data`-Ordner nicht vorhanden und konnte deshalb nicht geprüft oder aktualisiert werden.

## 2026-07-02 – Navigation, Breadcrumbs, Burger-Menü, Social Buttons und Formular-UX ergänzt

Geändert:

- `project_overview.md`: Navigation, Breadcrumbs, Burger-Menü und Social Buttons als verbindliche Komponenten ergänzt.
- `task_contract.md`: Arbeitsregel für Navigation, Burger-Menü, Breadcrumbs, Social Buttons und Formular-UX ergänzt.
- `styleguide.md`: Gestaltungsregeln für Navigation, Burger-Menü, Breadcrumbs, Social Buttons und Formular-UX ergänzt.
- `decision_log.md`: Entscheidung zur Einschränkung der blinden Bestandsübernahme dokumentiert.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: pauschale 1:1-Bestandsübernahme eingeschränkt; Navigation, Burger-Menü, Breadcrumbs, Social Buttons und Formular-UX als verbindliche Prüf- und Umsetzungspunkte ergänzt.

Nicht geändert:

- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`

Hinweis:

- `todo.md` war im aktuellen `/mnt/data`-Ordner nicht vorhanden und konnte deshalb nicht aktualisiert werden.


## 2026-07-02 – Hero-Cube-Hintergrundanimation ergänzt

Status: fertig

Änderung:
- Ausgewählte CSS-/SCSS-Partikel-Orb-Animation als Hero-Hintergrund hinter dem Cube dokumentiert.
- Layer-Reihenfolge, Farbgrenzen, Performance-Regeln und `prefers-reduced-motion` ergänzt.
- SCSS/Haml-Ausgangslogik im Implementation Brief als technische Vorlage aufgenommen.

Geändert:
- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `changelog.md`

Nicht geändert:
- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`


## 2026-07-02 – Hero-Animation von finaler Festlegung auf Prüfvarianten geändert

Geändert:

- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `styleguide.md`
- `decision_log.md`
- `project_overview.md`
- `task_contract.md`

Inhalt:

- Partikel-Orb ist nicht mehr als finale Hero-Hintergrundanimation dokumentiert.
- Partikel-Orb wird als Prüfvariante hinter dem Cube oder als möglicher Cube-Entstehungseffekt geführt.
- Maskierter Conic-/Noise-Lichteffekt ohne Text als zweite Prüfvariante ergänzt.
- Beispieltext/`h1` aus der Vorlage ausdrücklich ausgeschlossen.
- Externe CodePen-Fonts und externe Masken-Dateien nicht als produktive Abhängigkeit erlaubt.
- Finale Entscheidung erst nach visueller Prüfung, Performance-Test und Mobile-Prüfung.
---

## 2026-07-02 – Social-Button-Stil konkretisiert

Geändert:

- `project_overview.md`: Social Buttons als minimalistische, animierte Symbol-Icons ergänzt.
- `task_contract.md`: Social-Button-Regel ergänzt.
- `styleguide.md`: Social-Button-Stil, Farbregel, Animation und Accessibility konkretisiert.
- `decision_log.md`: Entscheidung zu animierten Social-Symbol-Icons dokumentiert.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: Social-Button-Vorgaben im Umsetzungsbrief konkretisiert.

Nicht geändert:

- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`
- `todo.md` nicht vorhanden


---

## 2026-07-02 – Section-Divider als Prüfvariante ergänzt

Geändert:

- `project_overview.md`: Section-Divider als verbindlich vorgesehene Homepage-Komponente ergänzt.
- `task_contract.md`: Arbeitsregel für CSS-/SVG-Divider ergänzt.
- `styleguide.md`: Divider-Gestaltungsregeln, Farbgrenzen, technische Regeln und responsive Anforderungen ergänzt.
- `decision_log.md`: Entscheidung zu Section-Dividern als CSS-/SVG-Prüfvariante dokumentiert.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: Abschnitt 19 „Section-Divider“ mit Prüfvariante A aufgenommen.

Inhalt:

- Schräger SVG-Separator als Prüfvariante A dokumentiert.
- Beispiel-Farbwerte ausdrücklich nicht übernommen.
- Umsetzung CSS-first per HTML/CSS/SVG festgelegt.
- Keine Bildgenerierung für Divider.
- Mobile-, z-index-, Overflow- und Performance-Regeln ergänzt.

Nicht geändert:

- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`
- `todo.md` nicht vorhanden

## 2026-07-02 – Divider-Prüfvariante B ergänzt

Geändert:

- `project_overview.md`: Pure-CSS-Angled-Sections als zweite Divider-Prüfvariante ergänzt.
- `task_contract.md`: Arbeitsregel für Divider-Prüfvariante B ergänzt.
- `styleguide.md`: technische und gestalterische Regeln für `clip-path`-/CSS-Trigonometrie-Divider ergänzt.
- `decision_log.md`: Entscheidung zu Divider-Prüfvariante B dokumentiert.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: Abschnitt 19.6 „Prüfvariante B – Pure-CSS-Angled-Sections“ ergänzt.

Festgelegt:

- Variante B wird geprüft, aber nicht final freigegeben.
- Umsetzung per HTML/CSS/SCSS, keine Bildgenerierung.
- Beispiel-Demo wird nicht 1:1 übernommen.
- Nurovelle-Farb- und Stilregeln bleiben verbindlich.
- Browser-Support, Mobile-Verhalten und Lesbarkeit müssen geprüft werden.

## 2026-07-02 – Divider-Prüfvariante C ergänzt

Geändert:

- `project_overview.md`: Diagonal Box / SkewY + Clip-Path als dritte Divider-Prüfvariante ergänzt.
- `task_contract.md`: verbindliche Arbeitsregeln für Prüfvariante C ergänzt.
- `styleguide.md`: technische und gestalterische Regeln für Diagonal-Box-/SkewY-/Clip-Path-Divider ergänzt.
- `decision_log.md`: Entscheidung zu Divider-Prüfvariante C dokumentiert.
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`: Abschnitt 19.7 „Prüfvariante C – Diagonal Box / SkewY + Clip-Path“ ergänzt.

Festgelegt:

- Demo-Farben werden nicht übernommen.
- Keine Lila-, Pink-, Cyan-, Blau-, Pastell-, Regenbogen- oder Neon-Verläufe.
- Farben ausschließlich aus dem Nurovelle-System.
- Content bleibt horizontal und unverzerrt.
- Demo-Texte, Controls, Formeln, Beispielgrafiken und fremde Links werden nicht übernommen.
- Finale Divider-Auswahl bleibt offen bis zur visuellen und technischen Prüfung der Varianten A, B und C.


## 2026-07-02 – Breadcrumb-Prüfvariante ergänzt

Status: fertig

Änderung:
- Ausgewählte Breadcrumb-Referenz als CSS-Pfeil-/Chevron-Prüfvariante aufgenommen.
- Regeln für semantische Breadcrumb-Navigation, Active-/Hover-Zustände, Mobile-Prüfung und Farbanpassung ergänzt.
- FreeFrontend-CSS-Infografik-Sammlung als optionale Inspirationsquelle notiert, ohne automatische Designfreigabe.

Geändert:
- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `changelog.md`

Nicht übernommen:
- Demo-Farben
- hellgrüner Hover
- Google-Font-Import
- Prefixfree-Script
- Beispieltexte
- Nummernkreise als Pflichtbestandteil

Nicht geändert:
- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`

Hinweis:
- `todo.md` ist im aktuellen `/mnt/data`-Ordner nicht vorhanden.


## 2026-07-02 – Breadcrumb-Referenz, FreeFrontend-Quelle und Card-Prüfvariante ergänzt

Status: fertig

Änderung:
- Breadcrumb-Referenz als CSS-Prüfvariante dokumentiert.
- FreeFrontend CSS Infographics als optionale Inspirationsquelle aufgenommen.
- CodePen „Frosted glass card overlay“ als Card-Prüfvariante dokumentiert.

Geändert:
- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`
- `changelog.md`

Nicht geändert:
- `asset_liste_v34.md`
- `workflow_module_table_aktualisiert.xlsx`

Hinweis:
- `todo.md` ist im aktuellen `/mnt/data`-Ordner nicht vorhanden und konnte deshalb nicht aktualisiert werden.
- Demo-Farben, Demo-Texte, externe Bilder, externe Scripts und fremde Typografie wurden nicht als Nurovelle-Vorgabe übernommen.

## 2026-07-02 – Dashboard-Board-Section-Prüfvariante ergänzt

Geändert:

- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`

Ergänzung:

- CodePen `https://codepen.io/josephrexme/pen/oNNpZYJ` als Section-/Board-Prüfvariante aufgenommen.
- Festgelegt: keine Demo-Farben, keine Demo-Texte, keine Demo-Logos, keine externen Avatar-/Bild-URLs, keine Bildgenerierung.
- Festgelegt: Umsetzung nur per HTML/CSS/SVG und nur nach Prüfung von Lesbarkeit, Responsiveness, Accessibility und Performance.
- Nurovelle-Farbsystem bleibt verbindlich.


---

## 2026-07-02 – CTA-Button-Prüfvariante: Arrow-Reveal zu Press-Button

Geändert:

- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`

Änderung:

- CTA-Button-Prüfvariante aufgenommen.
- Arrow-/Circle-Reveal-Logik als Startzustand dokumentiert.
- Übergang in haptische Press-/Button-Base-Logik dokumentiert.
- Demo-Farben und Demo-Texte ausdrücklich ausgeschlossen.
- Umsetzung als HTML/CSS/JS-Komponente ohne React-/styled-components-Pflicht festgelegt.

Status: fertig

---

## 2026-07-02 – CTA-Goldfarbe ergänzt

Geändert:

- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`

Änderung:
Die vom Nutzer gelieferte Golden-Button-Farblogik wurde als Prüfgrundlage für die CTA-Button-Variante aufgenommen. Dokumentiert wurden Goldverlauf, Lichtkante, Innenkante, Press-State-Regel und Ausschlüsse wie Demo-Text, React-Pflicht, Styled-Components-Pflicht und übertriebene Glanzwirkung.

---

## 2026-07-02 – Downloadbutton-Transformation ergänzt

Geändert:

- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`

Ergänzung:

- Downloadbutton kann als Prüfvariante nach Klick/Tap oder erfolgreicher Aktion in einen größeren Danke-/Bestätigungsbutton transformieren.
- Ursprüngliche Referenzseite ist noch offen.
- Umsetzung nur per HTML/CSS/JS.
- Keine Bildgenerierung, keine Demo-Farben, keine fremden Texte.
- Success-/Error-Logik darf nicht durch Animation ersetzt werden.


## 2026-07-02 – Statuskorrektur UX-/CSS-Komponenten

Geändert:

- `project_overview.md`
- `task_contract.md`
- `styleguide.md`
- `decision_log.md`
- `NUROVELLE_HOMEPAGE_IMPLEMENTATION_BRIEF.md`

Änderung:

- Divider-Auswahl als live zu prüfend markiert.
- Hero-Animationslösung als live zu prüfend markiert.
- Button-Animation als bereits bestimmt markiert.
- Breadcrumb-Ausführung als bereits bestimmt markiert.
- Section-Zuordnung und Rolle von Temkuri/Zra bleiben offen.

Status: fertig
