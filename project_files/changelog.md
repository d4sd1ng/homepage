Changelog
2026-07-16 – Calendly-Icon auf Gesprächs-CTAs ergänzt
Status: geprüft
Geändert:
    • Das vorhandene wiederverwendbare Calendly-Inline-SVG (#nv-calendly-mark, 20px) zusätzlich in die drei zum Gespräch auffordernden CTAs in homepage/index.html eingefügt: Header-CTA (Unverbindliches Erstgespräch), Hero-Sekundär-CTA (Unverbindliches Erstgespräch, Ziel #kontakt) und Kontaktkarten-CTA (Erstgespräch vereinbaren, Ziel analyse.html). 
    • Eine einzelne CSS-Regel .golden-button:has(.nv-calendly-icon) { --nv-golden-display: inline-flex; gap: 8px; } ergänzt, damit das Icon innerhalb des Golden Buttons inline links vor dem Text sitzt. Zuvor saß das Icon durch die Standard-inline-block-Darstellung außerhalb der eigentlichen Buttonfläche in einer eigenen Zeile ("ganz wo anders"). Die Regel nutzt das bestehende Display-Variablensystem (--nv-golden-display) und korrigiert zugleich die Platzierung der vier bereits vorhandenen Potenzialanalyse-Icon-CTAs. 
Nicht geändert:
    • CTA-Texte, CTA-Ziele, aria-label-Werte und Formularlogik in homepage/index.html. 
    • Der Projektprüfungs-CTA Projektidee prüfen lassen bleibt bewusst ohne Calendly-Icon, da er nicht zu einem Gespräch auffordert. 
Konflikt / Entscheidungsänderung:
    • Diese Änderung hebt die bisherige Festlegung im Eintrag „CTA auf Golden Button reduziert“ vom selben Tag („Gesprächs- und Projektprüfungs-CTAs bleiben ohne Calendly-Zeichen“) für die Gesprächs-CTAs auf. Grundlage ist die explizite aktuelle Benutzervorgabe, die laut Prioritätenrangfolge über der früheren Entscheidung in decision_log.md/changelog.md steht. Projektprüfungs-CTAs bleiben weiterhin ohne Calendly-Zeichen. 
Verifikation:
    • homepage/index.html headless in Chromium gerendert; Header-, Hero- und Kontakt-CTA per Screenshot geprüft: Das Calendly-Icon sitzt in allen Gesprächs-CTAs inline auf dem Button. Keine JavaScript-Fehler beim Laden. Calendly-Icon-Referenzen im Dokument: 7 (4 Potenzialanalyse + 3 Gespräch). 
2026-07-16 – CTA auf Golden Button reduziert
Status: geprüft
Geändert:
    • CTA-Darstellung in homepage/index.html auf die Golden-Button-Farb-, Rahmen- und Schattenlogik reduziert. 
    • Click-Button-Front-, Edge-, Base- und Bewegungs-Layer aus den CTA-Markups und CTA-Regeln entfernt. 
    • Verbleibende CTA-Komponente auf golden-button und golden-text bereinigt. 
    • Golden-Button-Farben und -Verlauf exakt auf die gesonderte Button-Vorgabe zurückgeführt; Header-CTA bei 11px auf Großbuchstaben gestellt und Sektions-CTAs auf 13px reduziert. 
    • Bulletpoints in Warum Nurovelle auf runde Goldmarker umgestellt; fett gesetzte Einleitungen bis zum Doppelpunkt gold hervorgehoben und den jeweiligen Erklärungstext darunter angeordnet. 
    • Kicker sowie Kreis- und Fetthervorhebungen in Warum Nurovelle vom gelblicheren Akzent auf den vorhandenen dunkleren Root-Goldton --nv-gold-inner-mid umgestellt. 
    • Abstand zwischen Hero-Unterzeile und Fließtext auf 32px erhöht; CTA-Höhe und Mindestabstand zum folgenden Sektionstrenner als Root-Werte mit 44px beziehungsweise 2 × 44px verankert. 
    • In Warum Nurovelle das vorhandene assets/bulletpoint.png in einen runden Goldrahmen gesetzt, den Punkt Klare nächste Schritte vollständig entfernt und das Video auf Desktop um 24px nach rechts sowie 42px nach unten verschoben. 
    • Marker in Warum Nurovelle auf 14px verkleinert und zur ersten Textzeile mittig ausgerichtet; Video-Versatz auf Desktop auf 148px nach rechts und 168px nach unten erhöht. 
    • Warum Nurovelle auf ein stabiles Grid mit bis zu 760px breiter Textspalte, 320px breiter Videospalte und 48px Spaltenabstand umgestellt; Video ohne freien Transform mittig zur Bulletpoint-Liste ausgerichtet. 
    • Breitenänderung in Warum Nurovelle auf die beiden Absätze unter dem Titel begrenzt; Bulletpoint-Liste wieder um 82px schmaler gesetzt und der sichtbare Abstand zum mittig ausgerichteten Video bei 48px gehalten. 
    • Marker in Warum Nurovelle auf 11px reduziert, Goldüberschriften explizit fett gesetzt, Bullet-/Videoabstand auf 80px erhöht und ausschließlich die beiden oberen Absätze um weitere 52px verbreitert. 
    • Marker in Warum Nurovelle an der Mitte des gesamten Bullettextblocks ausgerichtet; Videoabstand auf Desktop auf 120px und im aktiven einspaltigen Layout auf 88px erhöht. 
    • Marker in Warum Nurovelle auf 7px reduziert und zur goldenen Überschriftszeile ausgerichtet; Videoabstand gegenüber dem ursprünglichen Stand auf Desktop auf 144px und im einspaltigen Layout auf 264px verdreifacht. 
    • Markerposition anschließend direkt an die jeweilige goldene Überschriftszeile gebunden und dort unabhängig von der Länge des Erklärungstextes vertikal zentriert. 
    • Desktop-Videoabstand in Warum Nurovelle von einem breitenreduzierenden Grid-Margin auf eine Verschiebung des vollständigen Frames umgestellt, sodass die Videobreite erhalten bleibt. 
    • Im aktiven einspaltigen Layout den Videoframe bei 640px Breite rechtsbündig positioniert und den vertikalen Textabstand exakt auf 260px gesetzt; Mobile unter 640px bleibt vollbreit. 
    • Den 260px-Abstand im einspaltigen Warum Nurovelle-Layout vom Video-Margin an die verantwortliche Grid-Regel als row-gap verschoben. 
    • Videoframe in Warum Nurovelle von der quadratischen Mindesthöhe auf ein durchgängiges rechteckiges 16:9-Seitenverhältnis für Desktop, Tablet und Mobile umgestellt. 
    • Videoframe in Warum Nurovelle bei 640 × 360px belassen und im Desktop-Grid mit 220px sichtbarem Abstand wieder rechts neben den Bulletpoints angeordnet. 
    • Beide Absätze unter dem Titel Warum Nurovelle bis zur Bulletpoint-Liste auf eine eigene Breite von 955px gesetzt; die Bulletpoint-Liste behält separat ihre schmalere Breite. 
    • Feste Hero-Höhe durch eine Mindesthöhe ersetzt und den unteren Hero-Abstand an --nv-section-divider-before-gap gebunden, damit die Hero-Trennlinie bei umgebrochenen CTAs nicht mehr durch die Buttons läuft. 
    • Abstand zwischen Hero-Untertitel und folgendem Fließtext über --nv-hero-subtitle-body-gap von 32px auf 40px erhöht. 
    • Abstand zwischen dem zweiten Textabsatz und der Bulletpoint-Liste in Warum Nurovelle von 34px auf 80px erhöht; der Abstand zwischen den beiden Absätzen bleibt unverändert. 
    • Cards in Projektstart auf Desktop als symmetrische diagonale Folge mit 0px, 400px und 800px Horizontalversatz angeordnet; erst beim ersten sichtbaren Eintritt der gesamten Sektion fahren die vorhandenen Cards nacheinander vollständig vom linken Sektionsrand ein und blenden ihren Text jeweils nach Erreichen der Zielposition ein. Cardtext um 9px angehoben und rechts um 22px weiter in den Rahmen gesetzt. 
    • Sichtbaren Card-Gesamtrahmen in Projektstart aus der linken Kante der ersten und rechten Kante der letzten Card gebildet und zusammen mit der CTA auf derselben Sektionsmittelachse zentriert; diagonale Anordnung bis zum Mobile-Breakpoint erhalten. Rechten Textinnenabstand anhand der tatsächlichen PNG-Rahmenkante auf 82px beziehungsweise proportional 65px mobil erhöht. 
    • Der anhand der sichtbaren PNG-Fläche zentrierte Cardframe verwendet auf Desktop die gleichmäßigen Versätze 0px, 400px und 800px, auf Tablet 0px, 260px und 520px und wird erst unter 640px ohne Versatz gestapelt. 
    • In den Projektstart-Cards den Abstand zwischen Titel und Beschreibung von 10px auf 6px sowie zwischen Beschreibung und der Linie über Mehr erfahren von 18px auf 14px reduziert. 
    • Vertikalen Abstand der drei Projektstart-Cards durch jeweils -120px Zeilenüberlappung verkürzt, sodass alle drei vollständigen Cards zusammen mit der CTA innerhalb der aktuellen Desktop-/Tablet-Bildschirmhöhe sichtbar sind; Mobile bleibt ohne Überlappung gestapelt. 
    • Gesamten Cardframe in Projektstart um exakt 35px nach links verschoben; CTA, Überschrift, Einleitung, Card-Abstände und Animation bleiben unverändert. 
    • Rundlauf in Von der Idee zum Projekt korrigiert: bisheriges Bild 2 (assets/Fotos/13.png) an Position 1 gesetzt, Wide-Grid der richtigen Slide zugeordnet, Bild und Text als gemeinsamer Frame zentriert und Abstand Desktop/Tablet/Mobile jeweils um 30% reduziert. Die Übergänge sind so synchronisiert, dass das auslaufende Bild den rechten Rand exakt dann erreicht, wenn das folgende Bild die mittige Stoppposition erreicht. Titel Interne Wissenssuche in Unternehmenswissen schnell finden geändert. 
    • Die sechs vorhandenen Ablaufmodule als räumlich nach rechts absteigende 2-2-2-Folge angeordnet: Schritte 1/2 oben, die Reihe 3/4 um eine Modulposition nach rechts und eine Ebene nach unten versetzt, die Reihe 5/6 nochmals entsprechend versetzt. Dadurch sitzt Schritt 3 unter Schritt 2 und Schritt 5 unter Schritt 4. Die Paare sind horizontal verbunden; die Übergänge 2→3 und 4→5 verbinden die Ebenen seitlich. Inhalte, Assets, Leistungen und Kontakt blieben unverändert. 
    • Die zunächst pauschale Linksneigung der Modul-Visuals entfernt und durch eine gemeinsame Fluchtpunkt-Perspektive ersetzt: Die Module drehen sich abhängig von ihrer horizontalen Position nach innen; obere Module werden als hintere Ebene kleiner, mittlere bleiben neutral skaliert und untere werden als vordere Ebene größer. Sockel und Aufsatz teilen jeweils dieselbe Transformation und denselben Tiefenschatten. Reihenfolge, Texte und 2-2-2-Geometrie blieben unverändert; Tablet und Mobile bleiben unverzerrt. 
    • Modul-Aufbauten und Sockel in der Ablaufsektion deutlich vergrößert, die Tiefenstaffelung entsprechend angehoben und die Modulbezeichnungen von 16px auf 12px reduziert. 
    • Kontaktsektion gemäß freigegebener Zweispaltenstruktur aufgebaut: links die Portraitkarte mit assets/Whisk_ac35ee0e10.jpg, rundem Goldrahmen, Name, Marke und vier beschrifteten Social-Symbolen; rechts und deutlich tiefer versetzt die bestehende Erstgesprächskarte mit unveränderten Texten, separatem CTA zu analyse.html sowie verlinkter E-Mail und Telefonnummer. Beide Karten verwenden schwarzes Nurovelle-Material und werden entsprechend der Skizze durch eine kurze horizontale Goldlinie verbunden. Nicht dokumentierte Social-Profilziele wurden nicht erfunden. 
    • Beide Kartentitel der Kontaktsektion vom weißen Textton auf den vorhandenen Goldton --nv-gold-accent umgestellt. 
    • E-Mail, Telefon und Standort aus der rechten Karte entfernt und unter Portrait, Identität und Social-Symbolen in der linken Karte angeordnet. Portraitkarte und Kontaktkarte ohne horizontalen Abstand direkt an derselben Kante positioniert; ausschließlich die rechte Kontaktkarte bleibt um 330px vertikal versetzt. Eine Verbindungslinie wird nicht verwendet. 
    • Sämtliche Typografie der rechten Kontaktkarte um zwei bis drei Größenstufen reduziert: Titel auf maximal 30px, Fließtext auf 13px und CTA-Schrift auf 11px. 
    • Rechte Kontaktkarte auf Desktop von gemessenen 666px exakt um 30% auf 466.2px verschmälert; Portraitbreite, gemeinsamer horizontaler Ansatz und vertikaler Versatz blieben unverändert. 
    • Das Calendly-Zeichen als wiederverwendbares 20px-Inline-SVG ausschließlich in die vier Potenzialanalyse-CTAs einschließlich Formularbutton eingefügt; Gesprächs- und Projektprüfungs-CTAs bleiben ohne Calendly-Zeichen. 
    • FAQ-Titel sichtbar beibehalten und alle acht FAQ-Auslöser direkt an die bestehende Golden-Button-Darstellung der CTAs gebunden. Das vorhandene Kennzahlen-Liniendiagramm steht auf Desktop und Tablet rechts neben der FAQ-Spalte; mobil wird es darunter angeordnet. 
Nicht geändert:
    • CTA-Texte, Ziele und Formularlogik in homepage/index.html. 
2026-07-15 – Korrekturfortsetzung und Bereinigung (Layout/Assets)
Status: in Arbeit
Geändert:
    • Dritte Bereinigungsstufe: wiederholte lokale Abstandswerte und kleine Radiuswerte in den Komponenten auf zentrale Tokens umgestellt (--nv-space-*, --nv-radius-*), ohne sectionsinterne Geometrie-Logik zu verändern. 
    • Zweite Bereinigungsstufe: wiederverwendete Spacing-/Radius-Werte zentral in homepage/index.html als Tokens ergänzt (--nv-space-xxs/xs/sm/md/lg/xl/2xl, --nv-radius-sm/md) und in den Komponenten an mehreren wiederholten Stellen verwendet. 
    • Verbindliche Mapping-Tabelle erstellt: project_files/css_value_matrix.md (Wertquelle, Verantwortlichkeit und Dateigrenzen). 
    • Zentrale Global-Tokens in homepage/index.html ergänzt (--nv-section-inner-max, --nv-section-head-max, --nv-section-intro-max, --nv-footer-inner-max, --nv-section-title-gradient, --nv-gold-divider-strong). 
    • In homepage/components/nurovelle-service-cards.css wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breite) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert. 
    • In homepage/components/nurovelle-resources-contact-faq.css wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten) auf zentrale Tokens umgestellt; sectionsinterne Geometrie blieb unverändert. 
    • In homepage/components/nurovelle-section-rhythm.css wiederverwendete Global-Literale (Textfarben, Titelgradient, globale Max-Breiten, Footer-Basisfarben/Divider) auf zentrale Tokens umgestellt. 
    • Globale Rhythmus-, Alternation-, Separator- und responsive Sidebar-/Header-Regeln aus homepage/components/nurovelle-section-rhythm.css nach homepage/index.html verschoben. 
    • homepage/components/nurovelle-section-rhythm.css auf sectionsinterne Regeln fuer Prozess, Why und Footer reduziert. 
    • Sektion-7-Headerabstaende (Head, Kicker, Title) wieder lokal in homepage/components/nurovelle-service-cards.css verankert. 
    • Download-/Resource-Headerabstaende (Head, Kicker, Title) wieder lokal in homepage/components/nurovelle-resources-contact-faq.css verankert. 
    • Hintergrund-Alternation in homepage/components/nurovelle-section-rhythm.css auf den verbindlichen Sequenzstand korrigiert (#warum-nurovelle, #ki-projekt-start, #projektidee, #potenzialanalyse, #formular, #leistungen, #prozess-zur-loesung, #downloads, #kontakt, #faq, .footer). 
    • Prozesssektion in homepage/components/nurovelle-section-rhythm.css räumlich nachgestaffelt (2 + 2 + 2 über nth-child-Offsets), Mobile-Fallback ohne Offset beibehalten. 
    • Service-Card-Typografie in homepage/components/nurovelle-service-cards.css harmonisiert (lesbarere Bullet-, Untertitel- und Ergebnisgrößen). 
    • Service-Icon-Pfade in homepage/index.html auf assets/cards/service/icons/{1..11}.png umgestellt. 
    • Ergebnis-Icon-Injektion in homepage/index.html ergänzt (assets/cards/service/icons/ergebnis.png) innerhalb der bestehenden Service-Card-JavaScript-Logik. 
    • Platzhalter-Iconsatz unter homepage/assets/cards/service/icons/ erstellt (1.png bis 11.png, ergebnis.png) zur Stabilisierung fehlender Pfade. 
Nicht geändert:
    • Formularverarbeitung, Honeypot sowie Success-/Error-Grundlogik in homepage/index.html. 
    • Hero-Partikel-Canvas- und Cube-Grundlogik in homepage/index.html. 
2026-07-14 – Kontrolliertes Homepage-Update in homepage/index.html
Status: in Arbeit
Geändert:
    • Header-/Breadcrumb-Zielanker in homepage/index.html auf die aktuelle Sektionenstruktur angepasst (#warum-nurovelle, #ki-projekt-start, #projektidee, #potenzialanalyse, #formular, #prozess-zur-loesung, #downloads, #kontakt, #faq). 
    • Sidebar-Linktexte und -Reihenfolge in homepage/index.html an den aktuellen Inhaltsstand angepasst (inklusive neuem Kontakt-Eintrag). 
    • Abschnitt Warum Nurovelle in homepage/index.html inhaltlich auf freigegebenen Textstand umgestellt (2 Einleitungsabsätze + 6 Bulletpoints). 
    • Abschnitt Der erste Schritt zu Ihrem KI-Projekt in homepage/index.html textlich bereinigt und CTA auf Potenzialanalyse starten angepasst. 
    • Step-Animation in homepage/index.html erweitert: Karten sliden von links ein; Card-Text wird erst nach Ankunft sichtbar; Reduced-Motion-Fallback ohne Textverzögerung. 
    • Abschnitt Konkrete KI-Idee in homepage/index.html auf die Reihenfolge Prozessautomatisierung → Datenbasierte Entscheidungshilfe → Interne Wissenssuche umgestellt; breite Bildvariante vergrößert. 
    • Abschnitt Vom Geschäftsprozess zur KI-Lösung in homepage/index.html auf die sechs freigegebenen Modulbezeichnungen reduziert (ohne Beschreibungssätze). 
    • Neuer Abschnitt Kontakt in homepage/index.html ergänzt (40/60-Layout mit Portrait- und Kontaktkarte, Mobile-Stapelung). 
    • FAQ-Texte in homepage/index.html auf den freigegebenen Wortlaut aktualisiert; kompakte Kennzahlenleisten ergänzt. 
    • Footer in homepage/index.html inhaltlich auf die geforderten Gruppen erweitert (Unternehmensbeschreibung, nützliche Links, Newsletter, Kontakt, Rechtliches, Copyright, Nach-oben-Text, deaktivierte Links für Aktuelles/Team/SEO/Pakete). 
    • Hero-Sekundär-CTA in homepage/index.html auf Unverbindliches Erstgespräch mit Ziel #kontakt umgestellt. 
    • Potenzialanalyse- und Formularüberschriften/-texte in homepage/index.html an den freigegebenen Wortlaut angenähert. 
Nicht geändert:
    • Technische Formularfeldnamen und Grund-Submit-Mechanik in homepage/index.html. 
    • Download-Success-/Error-Zustandslogik in homepage/index.html. 
    • Hero-Cube-Asset und Partikel-Canvas-Grundlogik in homepage/index.html. 
2026-07-15 – Platzhalter für fehlende Downloadpfade angelegt
Status: fertig
Geändert:
    • homepage/assets/downloads/checkliste.pdf als Platzhalterdatei erstellt. 
    • homepage/assets/downloads/prompt_guide.pdf als Platzhalterdatei erstellt. 
Nicht geändert:
    • homepage/index.html. 
2026-07-07 – Hero-Orb-Originalvorgabe gesichert
Status: fertig
Geändert:
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md: Hero-Orb-Abschnitt mit der Originalvorgabe aus dem Chat ersetzt. 
    • styleguide.md: Hero-Animation konkretisiert: Orb kommt hinter den Cube; Originalvorgabe ist SCSS/HAML-Partikel-Orb. 
    • nurovelle-animations.css: bestehende .nv-hero-orb-/Conic-Umsetzung als rekonstruierte Adaption gekennzeichnet, nicht als Original. 
    • nurovelle-hero-orb-original.scss: Original-SCSS separat gesichert. 
    • nurovelle-hero-orb-original.haml: Original-HAML separat gesichert. 
Nicht geändert:
    • index.html 
    • Homepage-Layout 
    • bestehender Cube 
    • Produktions-CSS-Verhalten auf der Website 
2026-07-07 – Divider-Diagonal-Originalreferenz gesichert
Status: fertig
Geändert:
    • nurovelle-divider-diagonal-original-reference.txt: vom Nutzer gelieferte Diagonal-Section-/Divider-Referenz unverändert gesichert. 
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md: Variante C als technische Prüfvariante mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert. 
    • styleguide.md: Divider-Regeln ergänzt: skewY() nur auf Hintergrund-/Pseudo-Elemente, Content bleibt unverzerrt. 
    • nurovelle-animations.css: bestehende Divider-C-CSS als Nurovelle-Adaption gekennzeichnet, nicht als Originalcode. 
Nicht geändert:
    • index.html 
    • Homepage-Layout 
    • produktive Section-Divider auf der Website 
    • Hero-/Cube-Animation 
    • CTA-Buttons 
2026-07-07 – SVG-Divider-Originalreferenz gesichert
Status: fertig
Geändert:
    • nurovelle-divider-svg-original-reference.txt: vom Nutzer gelieferte SVG-Separator-/Divider-Referenz unverändert gesichert. 
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md: Variante A als SVG-Schräg-Divider / Separator mit Originalreferenz, übernehmbarem Kern und ausgeschlossenen Demo-Bestandteilen dokumentiert. 
    • styleguide.md: Divider als verbindlicher Homepage-Bestandteil festgehalten; finale Divider-Form bleibt Prüfentscheidung zwischen SVG-Separator und Diagonal-/Skew-Varianten. 
    • nurovelle-animations.css: Nurovelle-Adaption für SVG-Separator ergänzt, nicht als Originalcode gekennzeichnet. 
Nicht geändert:
    • index.html 
    • Homepage-Layout 
    • produktive Section-Divider auf der Website 
    • Hero-/Cube-Animation 
    • CTA-Buttons 
2026-07-07 – Pure-CSS-Angled-Divider-Originalreferenz ergänzt
Status: fertig
Geändert:
    • nurovelle-divider-pure-css-angled-original-reference.scss als unveränderte Originalreferenz gespeichert. 
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md um Divider-Variante B mit technischer Einordnung ergänzt. 
    • styleguide.md um Regeln für Variante B ergänzt. 
    • decision_log.md um die Entscheidung zur gesicherten Variante-B-Referenz ergänzt. 
    • nurovelle-animations.css Abschnitt 7B als Nurovelle-Adaption mit Fallback-/Support-Logik ergänzt. 
    • todo.md um Vergleich der Pure-CSS-Angled-Sections gegen SVG- und Skew-Variante ergänzt. 
Nicht geändert:
    • index.html 
    • produktive Homepage-Struktur 
    • finale Divider-Auswahl 
2026-07-07 – CTA-Originalreferenzen und Board-Option gesichert
Status: fertig
Geändert:
    • nurovelle-button-original-references.md: neue Originalreferenzdatei für Arrow-Reveal, Press-Button und Golden-Button-Farblogik erstellt. 
    • nurovelle-section-board-codepen-reference.md: externe CodePen-Option für Section-/Board-Komponente dokumentiert. 
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md: CTA-System neu eingeordnet und Board-Option ergänzt. 
    • styleguide.md: CSS-first-Regel und Prüfkomponentenliste ergänzt. 
    • decision_log.md: Entscheidung zur Button-Originalreferenz und Board-Prüfoption ergänzt. 
    • todo.md: Prüfpunkte für Navigation, Burger, Breadcrumbs, Social Buttons, Hero, Divider, Cards, Board und CTA-System ergänzt. 
Nicht geändert:
    • index.html 
    • produktive Homepage 
    • finale CTA-Auswahl 
    • finale Board-/Section-Auswahl 
    • finale Divider-Auswahl 
2026-07-07 – 8 Zusatzdateien in Projektfiles übernommen
Status: fertig
Geändert:
    • NUROVELLE_CSS_ANIMATIONEN_REFERENZ.md: vollständiges Referenzarchiv für die 8 zuvor separat erzeugten Dateien ergänzt. 
    • styleguide.md: Regel ergänzt, dass die Einzeldateien nicht als eigenständige aktive Designquellen gelten. 
    • decision_log.md: Entscheidung zur Konsolidierung der Zusatzdateien dokumentiert. 
    • task_contract.md: Arbeitsregel gegen verstreute Referenzdateien ergänzt. 
    • project_overview.md: CSS-/Interaktionsreferenzen als konsolidierte Projektgrundlage aufgenommen. 
    • todo.md: Konsolidierung abgeschlossen und offene Prüfaufgaben ergänzt. 
Übernommen:
    1. nurovelle_cta_button_preview.html 
    2. nurovelle-hero-orb-original.scss 
    3. nurovelle-hero-orb-original.haml 
    4. nurovelle-divider-diagonal-original-reference.txt 
    5. nurovelle-divider-svg-original-reference.txt 
    6. nurovelle-divider-pure-css-angled-original-reference.scss 
    7. nurovelle-button-original-references.md 
    8. nurovelle-section-board-codepen-reference.md 
Nicht geändert:
    • index.html 
    • produktive Homepage 
    • finale Divider-Auswahl 
    • finale CTA-Auswahl 
    • finale Hero-Orb-/Cube-Entstehungslogik 

Verbindlicher Homepage-Stand – 2026-07-14
Status: freigegeben
Diese Festlegung ersetzt abweichende ältere Homepage-Strukturen und Textstände in dieser Datei. Ältere Angaben zu Trust-Bereich, klassischer Navigation, zusätzlichem SEO-Bereich als aktuelle Sektion, ausführlichen Prozesskarten oder einer anderen Sektionsreihenfolge dürfen nicht mehr verwendet werden.
Header
    • Breadcrumbs ersetzen die klassische Navigation vollständig. 
    • Der Header enthält genau drei Breadcrumbs mit Submenüs. 
    • Die Submenüs öffnen sich per Hover. 
    • Keine zusätzliche klassische Hauptnavigation. 
Verbindliche Homepage-Reihenfolge
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
Hero
Kicker:
INDIVIDUELLE KI-SYSTEME
H1:
KI-Agenten für echte Geschäftsprozesse.
Subline:
Nurovelle entwickelt individuelle KI-Systeme für Datenverarbeitung, Wissenszugriff, Prozessautomatisierung und Unternehmenssoftware.
Zusatzzeile:
Von der Potenzialanalyse über Prompt Engineering und MCP bis zur Umsetzung maßgeschneiderter KI-Lösungen.
CTAs:
    • Kostenlose KI-Potenzialanalyse anfordern → Potenzialanalyse 
    • Unverbindliches Erstgespräch → Kontaktbereich 
Nicht verwenden:
    • Künstliche Intelligenz. Echte Ergebnisse. 
    • 35+ Jahre Code 
    • Trust-Aussagen im Hero 
    • Praxisleitfaden als zweiter Hero-CTA 
Warum Nurovelle
    • Der Abschnitt benötigt eine Einleitung aus mindestens zwei bis drei Sätzen. 
    • Danach folgen fünf bis sechs konkrete Bulletpoints. 
    • Keine Trust-Kennzahlenleiste. 
    • Keine Unternehmensgeschichte. 
    • Keine unbelegten Erfahrungs- oder Leistungsversprechen. 
    • Der finale Wortlaut der Einleitung und Bulletpoints ist noch nicht freigegeben und darf nicht frei erfunden werden. 
Der erste Schritt zu Ihrem KI-Projekt
Einleitung:
Ob erste Orientierung oder konkrete Projektidee: Wir prüfen Prozesse, Daten und technische Voraussetzungen und zeigen den passenden nächsten Schritt.
Card 1:
Prozess klären
Welcher Geschäftsprozess verbessert werden soll und welches konkrete Ergebnis durch KI entstehen muss.
Mehr erfahren
Card 2:
Daten prüfen
Welche Daten, Systeme und Wissensquellen bereits vorhanden sind und technisch nutzbar gemacht werden können.
Mehr erfahren
Card 3:
Umsetzung planen
Ob ein KI-Agent, ein Wissenssystem, Automatisierung oder individuelle Software der sinnvolle nächste Schritt ist.
Mehr erfahren
CTA:
Potenzialanalyse starten
Sie haben bereits eine konkrete KI-Idee?
Einleitung:
Wir prüfen Machbarkeit, Datenlage und Integrationsaufwand, bevor unnötige Entwicklungs- oder Folgekosten entstehen.
CTA:
Projektidee prüfen lassen
Kostenlose KI-Potenzialanalyse
    • Eigene Sektion vor dem Formular. 
    • Nicht mit dem Formular oder einer Trust-Section vermischen. 
    • Der finale vollständige Text dieser Sektion ist noch nicht freigegeben und darf nicht frei ergänzt werden. 
Formular
    • Eigene Sektion direkt nach der Potenzialanalyse. 
    • Formular rechts, begleitende Card links. 
    • Pflichtfelder, Einwilligung, Datenschutz, Honeypot, Submission sowie Success-/Error-Logik bleiben erhalten. 
    • Der finale Text der linken Card ist noch nicht freigegeben. 
KI-Leistungen von Nurovelle
Jede Leistungskarte enthält:
    • links oben ein Icon mit Rahmen 
    • rechts daneben einen Trennstrich 
    • eine Nummer mit eigenem Rahmen 
    • Titel und Untertitel 
    • eine mittig angeordnete Nummernkarte links neben dem Inhaltsbereich 
    • maximal vier Bulletpoints 
Inhaltsregeln:
    • Kein zusätzlicher Fließtext, der die Bulletpoints wiederholt. 
    • Keine weitere Text-Card auf der Leistungskarte. 
    • Titel, Untertitel und Bulletpoints dürfen denselben Inhalt nicht mehrfach ausdrücken. 
    • Keine vollständigen Detailseiten-Inhalte auf der Homepage. 
Vom Geschäftsprozess zur KI-Lösung
    • Die bisherigen Prozesskarten mit Beschreibungstexten entfallen. 
    • Nur Module in der freigegebenen Stepdiagramm-Anordnung verwenden. 
    • Je Modul ausschließlich die Modulbezeichnung anzeigen. 
    • Keine Erklärungssätze, Bulletpoints oder zusätzlichen Cards. 
    • Kein CTA. 
Download-Bereich
    • Eigene Sektion nach dem Stepdiagramm. 
    • Bestehende Downloads mit kurzen, nicht wiederholenden Beschreibungen. 
    • Finale Einzeltexte sind noch zu prüfen. 
Kontakt
    • Eigene Kontaktsektion nach dem Download-Bereich. 
    • Nicht mit Potenzialanalyse oder Formular vermischen. 
    • Finale Kontakttexte sind noch zu prüfen. 
FAQ
    • Abschnitt 12. 
    • Bestehende Fragen und Antworten nicht ungeprüft verändern. 
    • Finale FAQ-Texte sind gesondert zu prüfen. 
Footer
Verbindlicher Beschreibungstext:
Individuelle KI-Systeme für reale Geschäftsprozesse.
Keine lange Leistungsbeschreibung, Unternehmensgeschichte oder technische Erklärung im Footer.
Textstatus
    • Kein bisheriger vollständiger Sektionstext darf ungeprüft als final verwendet werden. 
    • Nur die in diesem Nachtrag wörtlich festgelegten Texte gelten als freigegeben. 
    • Fehlende Texte dürfen nicht selbstständig erfunden, ergänzt oder aus alten Dateien übernommen werden. 

