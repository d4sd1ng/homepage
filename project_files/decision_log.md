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

