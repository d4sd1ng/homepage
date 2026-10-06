# Nurovelle Homepage – Decision Log

Stand: 2026-08-14  
Status: freigegeben

## Zweck dieser Datei

Hier stehen ausschließlich **freigegebene Entscheidungen** und ihr Datum.

Die konkrete aktuelle Regel wird nicht hier dupliziert, sondern in der zuständigen Datei gepflegt.

## 2026-05-17 – Conversion-orientierte B2B-Homepage

Entscheidung: Die Homepage wird als conversion-orientierte B2B-Website aufgebaut.

Aktuelle Umsetzung: siehe `project_overview.md`.

## 2026-05-17 – KI-Potenzialanalyse als primärer Conversion-Pfad

Entscheidung: Die KI-Potenzialanalyse ist der zentrale CTA-/Lead-Pfad.

Aktuelle Ziele und Seitenlogik: siehe `project_overview.md` und `architecture.md`.

## 2026-05-17 – Praxisleitfaden / Downloads als sekundärer Conversion-Pfad

Entscheidung: Downloads bleiben Bestandteil der Website.

Aktueller Umfang: siehe `project_overview.md`; Assets siehe `assets.md`.

## 2026-05-17 – Dunkles Nurovelle Premium-Design

Entscheidung: Schwarz, dunkles Grün/Smaragd, Gunmetal und Gold bilden die Materialsprache.

Aktuelle Designwerte: siehe `styleguide.md` und `nurovelle-tokens.css`.

## 2026-06-20 – SEO als eigene Leistung

Entscheidung: SEO ist ein eigener Leistungsbereich und erhält eine Detailseite; kein separater SEO-Homepage-Abschnitt ist allein dadurch verpflichtend.

## 2026-06-20 – Gemeinsames Detailseiten-System

Entscheidung: Leistungsdetailseiten verwenden ein gemeinsames Grundsystem statt vollständig separater Layouts.

Aktueller Stand/offene Punkte: siehe `project_overview.md` und `todo.md`.

## 2026-06-20 – CSS-/HTML-Boards statt beschrifteter Bildboards

Entscheidung: Steuerbare Boards, Panels, Texte und UI-Flächen werden bevorzugt als HTML/CSS umgesetzt; Bildassets liefern technische Module/Visuals.

## 2026-06-20 – Hero-Assets ohne Texte oder Labels

Entscheidung: Hero-Visuals enthalten keine Texte, Labels, Zahlen, Logos oder lesbare UI.

Aktuelle Bildregeln: siehe `styleguide.md`.

## 2026-06-30 – Keine freie Neuinterpretation bestehender Hero-Formen

Entscheidung: Vorhandene Formen werden nicht frei weiterentwickelt oder ersetzt.

Aktuelle Asset-/Bildregeln: siehe `task_contract.md` und `styleguide.md`.

## 2026-07-02 – Social Icons als SVG/CSS-Komponenten

Entscheidung: Social Icons werden nicht als Bild generiert, sondern als zugängliche SVG/CSS-Komponenten umgesetzt.

## 2026-07-02 – Divider als CSS-/SVG-System

Entscheidung: Divider werden technisch per CSS/SVG umgesetzt. Mehrere Varianten wurden zur Sichtprüfung aufgenommen.

Offener Freigabestatus: siehe `todo.md`.

## 2026-07-02 – CTA-System

Entscheidung: Arrow-Reveal/Circle-Fill, haptischer Press-State und Golden-Materiallogik bilden gemeinsam das CTA-System.

Aktuelle Designregeln: siehe `styleguide.md`.

## 2026-07-02 – Downloadbutton Success-Transformation

Entscheidung: Download-CTAs können nach real erfolgreicher Aktion in einen größeren Bestätigungszustand übergehen; Fehler dürfen keinen Success-State zeigen.

## 2026-07-07 – Referenzdateien sind keine eigenständigen Designquellen

Entscheidung: Originalreferenzen und Prüfvarianten werden als Referenz geführt; aktive Designentscheidungen stehen ausschließlich im Styleguide.

## 2026-07-14 – Breadcrumbs ersetzen klassische Navigation

Entscheidung: Der Header verwendet genau drei Breadcrumb-Bereiche mit Submenüs; keine zusätzliche klassische Hauptnavigation.

Aktuelle Struktur: siehe `project_overview.md`; Design: siehe `styleguide.md`.

## 2026-07-14 – Homepage-Reihenfolge neu festgelegt

Entscheidung: Die am 2026-07-14 freigegebene Homepage-Reihenfolge ersetzt ältere Trust-/SEO-/Prozess-Strukturen.

Aktuelle Reihenfolge: siehe `project_overview.md`.

## 2026-07-14 – Hero-Inhalte neu festgelegt

Entscheidung: Kicker, H1, Subline, Zusatzzeile und die zwei aktuellen Hero-CTAs wurden festgelegt; alte Trust-Aussagen und der Praxisleitfaden als zweiter Hero-CTA entfallen.

Aktueller Wortlaut: siehe `project_overview.md`.

## 2026-07-14 – Leistungs- und Download-Card-System konkretisiert

Entscheidung: Homepage-Cards bleiben kompakt, vermeiden Detailseiten-Duplikation; Download-Cards werden als horizontale kompakte Reihe mit Goldgradient-Rahmen geführt.

Aktuelle visuelle Regeln: siehe `styleguide.md`.

## 2026-07-31 – Tapera + Inter als aktives Website-Fontsystem — ABGELÖST am 2026-08-14

Entscheidung: Tapera für Display/Headlines und Inter für UI/Body ersetzen die früheren Website-Fontstacks.

Status: abgelöst durch die Entscheidung vom 2026-08-14 („Exo 2 + Inter als aktives Website-Fontsystem"). Tapera wird nicht weiter verfolgt.

## 2026-08-14 – Exo 2 + Inter als aktives Website-Fontsystem

Entscheidung: Exo 2 für Display/Headlines und Inter für Fließtext, Navigation, Buttons, Formulare, Cards und Footer. Diese Festlegung gilt unabhängig von älteren Einträgen und löst die Entscheidung vom 2026-07-31 (Tapera + Inter) ab.

Begründung der Ablösung: Tapera war in keinem Repo, auf keinem Rechner und auf dem Server vorhanden; die Website fiel deshalb dauerhaft auf Inter zurück. Exo 2 und Inter sind beide unter der Open Font License frei verfügbar und am 2026-08-14 systemweit installiert worden.

Aktuelle Regeln: siehe `styleguide.md` und `nurovelle-tokens.css`.

## 2026-08-14 – Goldwort-Regel nach Medium getrennt

Entscheidung: Auf der Website trägt die Überschrift den Goldverlauf über den kompletten Text – so ist sie umgesetzt und so bleibt es. In allen anderen Medien (Dokumente, Angebote, Verträge, Social-Beiträge, Newsletter) trägt genau ein Wort den Verlauf, das inhaltlich tragende; findet sich keins, wird die Überschrift gekürzt statt ein beliebiges Wort eingefärbt.

Aktuelle Designregeln: siehe `styleguide.md`.

## 2026-08-14 – Ein einziger Goldverlauf für Dokumente

Entscheidung: Dokumente verwenden ausschließlich `linear-gradient(110deg, #B8933F, #C9A659, #A8842F)`. Der siebenstufige Website-Verlauf wird dort nicht eingesetzt, weil seine Hell-Dunkel-Sprünge als Wellen durch die Wörter laufen und die hellste Stelle je nach Textlänge zufällig platziert ist. In E-Mails wird statt eines Verlaufs der Vollton `#A8842F` verwendet.

Aktuelle Designregeln: siehe `styleguide.md`.

## 2026-08-14 – Wortmarke immer in Gold

Entscheidung: Das Wort „Nurovelle" wird überall in Gold gesetzt, unabhängig vom Umfeld.

Aktuelle Designregeln: siehe `styleguide.md`.

## 2026-08-14 – Keine Platzhalterwerte in Erzeugnissen

Entscheidung: Ein Erzeugnis mit Platzhaltern gilt nicht als fertig und wird nicht vorgelegt – auch nicht mit dem Hinweis, die Werte seien vor Veröffentlichung zu ersetzen. Lässt sich eine Zahl nicht belegen, wird das Stück so gebaut, dass es ohne Zahlen trägt. Wird eine unbelegte Zahl trotzdem gewünscht, sind beide Fassungen zu liefern: die mit der Zahl und eine vollständige ohne.

Aktuelle Inhaltsregeln: siehe `task_contract.md`.

## 2026-08-14 – Agenten-Team liest das Homepage-Repo nur lesend

Entscheidung: Das Jude-Agententeam erhält Lesezugriff auf `homepage_repo` als verbindliche Quelle für Vorgaben, Texte, Bilder und Icons. Schreibzugriff besteht nicht und wird nicht eingerichtet.

Aktuelle Arbeitsregeln für das Team: siehe `task_contract.md`.

## 2026-08-14 – Newsletter ohne eigene Gestaltung

Entscheidung: Newsletter werden als reiner Text geführt; eine eigene Gestaltung wird nicht erstellt.

## 2026-08-14 – Projectfiles entflechten

Entscheidung: Eine Information hat genau eine zuständige Projectfile. Der Implementation Brief ist keine aktive Quelle mehr.

Zuständigkeiten:

- Projekt → `project_overview.md`
- Arbeitsregeln → `task_contract.md`
- Entscheidungen → `decision_log.md`
- offene Aufgaben → `todo.md`
- Design → `styleguide.md`
- Technik → `architecture.md`
- Assets → `assets.md`
- Änderungen → `changelog.md`

## 2026-09-06 – Bildregeln für Social-/Content-Posts ergänzt, keine Personen/Hände

Entscheidung: Für generierte Post-Bilder sind realistische Personen-, Hände-
oder Schreibtischaufnahmen nicht freigegeben. Für Abläufe/Fähigkeiten gilt
die technisch-mechanische Modulwelt aus Abschnitt 14 (Mechanik, Schalter,
Relais, Displays, Container, Terminals, Scanner, Speicher, Ventile,
Verteiler, Kontrollmodule) als Standardmotiv, nicht nur für
Website-Stepdiagramme.

Hintergrund: mehrere Erzeugungsversuche am 05./06.09.2026 zeigten wiederholt
verformte Hände bei Nahaufnahmen sowie eine zuverlässig auftretende
Sci-Fi-/Hologramm-Optik, sobald ein Prompt eine abstrakte Datenverbindung
zwischen Systemen als Motiv beschrieb – auch bei ausdrücklichem Verbot im
Prompt selbst. Ausserdem wurde festgestellt, dass die bis dahin in Judes
Rollentexten verwendete VERBOTEN-Liste (u.a. „Platinen", „Stockfoto-
Büroklischee") nie Teil dieses Styleguides war, sondern eigenständig
hinzugedichtet wurde und teils den tatsächlich freigegebenen Assets
widersprach (z.B. `Banner_all_passt.png` mit Platinen-Makrofoto).

Aktuelle Bildregeln: siehe `styleguide.md`, Abschnitt 17a.

## 2026-09-06 – Richtungsreferenzen für Post-Bilder ergänzt

Entscheidung: Neue Bilder unter `austausch/an-team/vorlagen/nurovelle/`
(`1.png`–`16.png`, `reference_posting_*.png`) sind Stimmungs-/Richtungs-
referenzen für Post-Motive, keine fertigen Assets – teils mit fremden
Markennamen, englischem Text oder Bildfehlern, die nicht übernommen werden.
Zwei Richtungen zeichnen sich ab: Server-/Rechenzentrums-Fotografie mit
eingeblendeten Workflow-Panels und Dashboard-Requisiten; sowie dunkle
Würfel-/Modul-Cluster mit goldener Kantenbeleuchtung und Zahnrädern als
konkrete Ausführung der Modulwelt aus Abschnitt 14. Ein verbindliches
Einzelmotiv daraus steht noch aus.

Aktuelle Bildregeln: siehe `styleguide.md`, Abschnitt 17a.

## 2026-10-01 – Analyse-Schieberegler mit 152 px Verkürzung freigegeben

Entscheidung: Die Desktop-Schieberegler der Homepage-Potenzialanalyse verwenden `calc(100% - 152px)`.

Auswirkung: Nur die Track-Breite der bestehenden Slider-Regel wird angepasst; das bestehende Analyse-Spaltenverhältnis und die übrige Analyse-Logik bleiben unverändert.

## 2026-10-01 – Obere Analyse-Cards breiter/schmaler gewichtet

Entscheidung: Die obere Analyse-Card-Reihe verwendet für die Regler-Card und die Ergebnis-Card das Verhältnis `1.14fr / .86fr`. Gauge und Kennzahlenblock der Ergebnis-Card werden linksbündig mit `20px` Spaltenabstand angeordnet.

Auswirkung: Nur die beiden oberen Analyse-Cards werden neu gewichtet; Sliderbreite, innere Regler-Card-Aufteilung, Berechnung und untere Analyse-Cards bleiben unverändert.

## 2026-10-01 – Analyse-Card-Gewichtung und Divider-Korrekturen

Entscheidung: Die obere Analyse-Card-Reihe verwendet `1.28fr / .72fr`; die linke Analyse-Card ist intern gleichmäßig `1fr / 1fr` geteilt. Die Slider nutzen `calc(100% - 64px)`, Text und Wert stehen ohne automatischen Zwischenraum mit `12px` Gap.

Entscheidung: Der Projektstart-Hinweis steht direkt unter der mittleren Card. In der Leistungssektion müssen vertikaler Divider, linker Horizontal-Divider und rechter kurzer Horizontal-Divider im aktiven Zustand gleichzeitig sichtbar sein.

Entscheidung: Der Divider zwischen „Von der Idee zum Projekt“ und „Pakete“ wird sichtbar verstärkt.

## 2026-10-01 – Wiederholungsanteil als Eingabe der Richtwertberechnung

Entscheidung: Die Richtwertberechnung fragt nicht mehr nach dem vom Besucher selbst einzuschätzenden „Anteil automatisierbarer Aufgaben“. Stattdessen wird der beobachtbare „Anteil wiederkehrender Abläufe“ mit der Erklärung „Wie viel dieser Arbeit läuft nach einem ähnlichen Muster ab?“ auf einer Skala von 0–100 % abgefragt. Der Wert übernimmt denselben numerischen Faktor in der bestehenden Berechnungsformel.

## 2026-10-01 – Analyse-Divider und Prozesspfeile

Entscheidung: Der Divider der breiten Analyse-Card wird als eigene mittlere Grid-Spalte zwischen zwei gleich breiten Bereichen aufgebaut. Die Pfeile im sechs-stufigen Ablauf sitzen mittig in den Zwischenräumen und auf Höhe der Modulmitten.

## 2026-10-04 – SEO Toolbox und Automationen in der Hauptnavigation

Entscheidung: Die Hauptnavigation erhält nach den bestehenden Breadcrumbs zwei zusätzliche direkte Breadcrumbs: `SEO Toolbox` → `detail_seo.html` und `Automationen` → `detail_automationen.html`. Die beiden Einträge sind direkte Navigationselemente und keine zusätzlichen Dropdown-Menüs.

## 2026-10-04 – Definition der Potenzialanalyse als eigene Sektion

Entscheidung: „Was ist eine KI-Potenzialanalyse?“ steht auf `analyse.html` als eigenständige Sektion direkt nach dem Hero. Die bestehenden Definitionsinhalte bleiben unverändert. Die Sektion erhält den CTA `KI-Potenzialanalyse starten` mit Ziel `#analyse-formular`.

## 2026-10-04 – Potenzialanalyse-Hero nutzt volle sichtbare Höhe

Entscheidung: Nach der Trennung von Hero und Definitionssektion belegt der Hero auf Desktop die sichtbare Viewport-Höhe unterhalb des Headers. Die Höhe liegt am `#hero` selbst, nicht an einem leeren Wrapper; der bestehende Hero-Inhalt wird vertikal in dieser Fläche ausgerichtet.

## 2026-10-04 – Definitionssektion der Potenzialanalyse als Viewport-Sektion

Entscheidung: Die eigenständige Sektion `#was-ist-das` belegt auf Desktop die volle sichtbare Viewport-Höhe unterhalb des Headers und zentriert ihren bestehenden Inhalt vertikal. Mobile bleibt in natürlicher Inhalts-Höhe.

## 2026-10-04 – Keine Override-Schichten für Analyse-Seitenlayout

Entscheidung: Hero-, Viewport- und Section-Layout von `analyse.html` wird aus einer konsolidierten CSS-Quelle ohne `!important` gesteuert. Hero und Definitionssektion belegen auf Desktop die sichtbare Höhe unterhalb des Headers; weitere Inhaltssektionen folgen bei ausreichender Bildschirmhöhe demselben Viewport-Prinzip. Historische Layout-Override-Schichten werden nicht weitergeführt.

## 2026-10-04 – Größere vertikale Abstände in der Definitionssektion

Entscheidung: `#was-ist-das` bleibt eine Viewport-Sektion. Innerhalb der Sektion werden Subline und Cards sowie Cards und CTA deutlicher voneinander getrennt: Desktop 64 px bzw. 56 px; Mobile 40 px bzw. 36 px.

## 2026-10-04 – CTA der Definitionssektion mittig

Entscheidung: Der CTA unter den beiden Cards in `#was-ist-das` wird horizontal mittig ausgerichtet.

## 2026-10-04 – Einheitliche grüne 3D-Bulletpoints

Entscheidung: Alle echten Bulletpoint-Listen auf `analyse.html` verwenden den grünen 3D-Punkt aus `assets/bulletpoint.png`. Nummerierte Prozessschritte bleiben als nummerierte Elemente bestehen.

## 2026-10-04 – Shared Footer mit vier flexiblen Spalten

Entscheidung: Der Desktop-Footer in `shared-header-footer.css` verwendet vier flexible Grid-Spalten im Verhältnis `1.35fr 1fr 1.2fr 1fr`. Feste Auto-/Pixel-Spalten werden nicht verwendet, damit alle vier Footer-Bereiche einschließlich „Kontakt“ innerhalb des verfügbaren Viewports bleiben.

## 2026-10-04 – Shared Footer bleibt unangetastet

Entscheidung: Der funktionierende Shared Footer wird nicht zur Korrektur eines seitenbezogenen Problems verändert. Abweichungen auf `analyse.html` werden ausschließlich in `analyse.html` behoben.

## 2026-10-04 – Analyse-Hero-Visual wieder in großer Desktop-Proportion

Entscheidung: Das Hero-Visual auf `analyse.html` nutzt auf Desktop ab 1101 px wieder maximal 760 px Breite und die zuvor verwendete Spaltenverteilung `1.08fr / 1.12fr`.

## 2026-10-04 – Analyse-Hero-Bild wird unabhängig von der Grid-Spalte skaliert

Entscheidung: Die Position des Hero-Visuals auf `analyse.html` bleibt über das bestehende Desktop-Grid erhalten. Die Bildgröße wird separat gesteuert: 760 px ab 1101 px und 680 px von 901–1100 px, jeweils um den Mittelpunkt der Visual-Spalte zentriert.

## 2026-10-04 – Analyse-Hero-Visual um festen Mittelpunkt skalieren

Entscheidung: Das Hero-Visual auf `analyse.html` wird nicht durch erneute Grid-Verschiebungen vergrößert. Die bestehende Position bleibt erhalten; der sichtbare Bildinhalt wird auf Desktop per `scale(1.6)` und zwischen 901–1100 px per `scale(1.45)` um den Mittelpunkt skaliert.

## 2026-10-06 – Professionellere Analyse-Hero-Komposition

Entscheidung: Der Desktop-Hero von `analyse.html` wird als gemeinsame Text-/Visual-Einheit um 80 px nach oben versetzt. Der CTA-Abstand beträgt 38 px. Position und Größe des vorhandenen Visuals bleiben bestehen; hinter dem Visual ist nur ein dezenter dunkler Emerald-/Gunmetal-Glow zulässig. Zusätzliche dekorative Objekte werden ohne separate Freigabe nicht ergänzt.

