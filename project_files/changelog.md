## 2026-11-14 - Analyse-Detailseite: Inhaltskorridor 70 bis 1370 festgeschrieben und durchgesetzt

Status: geprueft

Der Nutzer hat den Korridor an der Definitionssektion ausmessen lassen und als verbindlich festgelegt: linke Karte beginnt bei **70 px**, rechte Karte endet bei **1370 px**, Breite **1300 px**, gemessen bei 1440 px Fensterbreite.

Festgeschrieben in `project_files/styleguide.md`, Abschnitt 21.1: die drei Werte als Tabellenzeilen, dazu die Regel, dass jeder Inhalt einer Sektion links bei 70 beginnt und rechts bei 1370 endet, kein Inhalt mittig in einem schmaleren Kasten zentriert wird und der Kopf aus Kicker, Headline und Subline davor bei 69 px sitzt. Referenz ist die Definitionssektion.

Danach wurden alle sichtbaren Inhaltselemente jeder Sektion gegen den Korridor gemessen. Zwei Sektionen lagen daneben.

- `homepage/analyse.html`, `#warum .media-split` im Block `@media(min-width:901px)`: `grid-template-columns` von `minmax(0,.9fr) minmax(580px,1.1fr)` auf `minmax(0,1fr) 544px`. Die Bildspalte war 684 px breit, das 544 px breite Bild stand linksbuendig darin und liess rechts 140 px leer.
- `homepage/analyse.html`, `#nutzen .media-split--visual-left` im selben Block: `grid-template-columns` von `minmax(580px,1.08fr) minmax(0,.92fr)` auf `544px minmax(0,1fr)`, derselbe Grund spiegelbildlich.
- `homepage/analyse.html`, `.faq-grid`: `max-width` von `1120px` auf `none`, `margin` von `16px auto 0` auf `16px 0 0`. Das Raster war mittig in einem schmaleren Kasten zentriert und lief von 160 bis 1280.

Gemessen vorher und nachher bei 1440 px, linke und rechte Kante aller Inhaltselemente je Sektion:

| Sektion | vorher | nachher |
| --- | --- | --- |
| `#was-ist-das` | 70 .. 1370 | 70 .. 1370 |
| `#warum` | 70 .. 1230 | 70 .. 1371 |
| `#leistungen` | 70 .. 1370 | 70 .. 1370 |
| `#einsatzbereiche` | 70 .. 1370 | 70 .. 1370 |
| `#nutzen` | 70 .. 1371 | 70 .. 1371 |
| `#analyse-formular` | 70 .. 1370 | 70 .. 1370 |
| `#faq` | 160 .. 1280 | 69 .. 1371 |

Bildgroesse und Spaltenabstand bleiben unveraendert: Bild 544 px, Luecke zum Text 56 px. In `#warum` sitzt das Bild jetzt von 826 bis 1370 statt 686 bis 1230, die Textspalte waechst entsprechend von 561 auf 700 px. In `#nutzen` bleibt das Bild bei 70 bis 614, die Bulletpoint-Liste beginnt bei 670 statt 798, die Luecke faellt von 184 auf 56 px.

Nebenbefund, kein eigener Auftrag: Durch die volle Korridorbreite sind bei 1440 px alle acht FAQ-Knoepfe einzeilig, Hoehe je 44 px, Knopfbreite 641 px bei 535 px Bedarf des laengsten.

Nachgezogen in `project_files/styleguide.md`: Abschnitt 21.2 um Bildspalte 544 px, Spaltenabstand 56 px, Textspalte 700 px und die Begruendung ergaenzt, warum die Bildspalte fest und nicht als `fr` gesetzt ist. Abschnitt 21.4 auf `max-width: keine`, Kanten 70 und 1370 und Knopfbreite 641 px geaendert.

Geprueft bei 1440, 1280, 1100 und 1000 px. Unveraendert offen und nicht von dieser Aenderung verursacht: unterhalb von 1280 px werden einzelne FAQ-Knoepfe wieder zweizeilig, bei 1100 px einer, bei 1000 px drei; der waagerechte Ueberlauf der Seite und der Konsolenfehler `breadcrumbGroups` bestehen unveraendert aus `origin/main`.

## 2026-11-14 - Analyse-Detailseite: eigenmaechtige Bildausrichtung zurueckgenommen

Status: geprueft

Der Nutzer hat beanstandet, dass das Bild in `#warum` zu weit rechts steht und zu weit vom Text entfernt ist, und dass die Bilder mittig zur Bulletpoint-Liste sitzen sollen. Beides geht auf zwei Zutaten zurueck, die im vorigen Schritt ohne Auftrag ergaenzt worden waren.

- `homepage/analyse.html`, `#warum .section-photo` und `#nutzen .section-photo`: `justify-self:end` beziehungsweise `justify-self:start` entfernt. Diese Angaben hatten das Bild an die Aussenkante gedrueckt.
- `homepage/analyse.html`, `#warum .media-split` und `#nutzen .media-split--visual-left`: `align-items:start!important` entfernt. Die Zeilen sind damit wieder mittig ausgerichtet, das Bild sitzt auf halber Hoehe der Liste.

Gemessen bei 1440 px, Sektion `#warum`: Luecke zwischen Textspalte und Bild von 197 auf 56 px, Bild von 827 bis 1371 auf 686 bis 1230.

Beide Zutaten waren im vorigen Schritt zusaetzlich in `project_files/styleguide.md` als verbindliche Werte eingetragen worden. Damit hat die Dokumentation einen Alleingang nachtraeglich bestaetigt, statt ihn zu verhindern. Die Eintraege sind entfernt.

Ebenfalls korrigiert: Der Einzug der Inhalte stand dort als Spanne von 19 bis 26 px. Das war der Streubereich des vorhandenen Zustands, kein Sollwert, und damit nicht pruefbar. Die Zeile ist auf offen gesetzt, der gemessene Befund ist als offener Punkt beschrieben. Zusaetzlich steht in Abschnitt 21 jetzt die Regel, dass dort verbindliche Einzelwerte stehen und keine Spannen oder Beschreibungen des Ist-Zustands.

Der Nutzer hat den offenen Wert am 2026-11-14 festgelegt: Der Inhaltsblock sitzt auf **70 px**, nicht auf 69.

- `homepage/analyse.html`, `#warum .media-split` und `#nutzen .media-split--visual-left`: `margin-left:1px` und `width:calc(100% - 1px)` ergaenzt. Der Block beginnt damit bei 70 px und laeuft nicht ueber die rechte Inhaltskante hinaus.

Gemessen danach bei 1440 px: `#warum` Inhaltsblock und Bulletpoint-Liste bei 70 px, vorher 69. `#nutzen` Inhaltsblock bei 70 px, Bild 70 bis 614, die Liste bleibt als rechte Spalte bei 798. Zum Vergleich die uebrigen Sektionen, alle unveraendert bei 70: `#was-ist-das`, `#leistungen`, `#einsatzbereiche`.

Der Mechanismus war bisher uneinheitlich: `#einsatzbereiche .panel` erreicht die 70 ueber `margin-left:0.890625px`, bei `#leistungen .num-list` entsteht sie nur durch Rundung. Deshalb wurde fuer die beiden Sektionen ein eindeutiger Versatz gesetzt statt eines weiteren Zufallswerts.

In `project_files/styleguide.md` steht jetzt **70 px, verbindlich** als Einzelwert anstelle der frueheren Spanne, zusammen mit dem Hinweis, wie der Wert in den beiden `media-split`-Sektionen erreicht wird.

## 2026-11-14 - Analyse-Detailseite: sieben Punkte ueberarbeitet

Status: geprueft

Alle Aenderungen in `homepage/analyse.html`, gemessen bei 1440 px.

1. **Hero-Eckenlinien entfernt.** `svg.hero-corner-lines` aus dem Markup geloescht, dazu die Regel `.hero-corner-lines{display:none;}` und der zugehoerige Block in `@media(min-width:901px)`. Markup und CSS sind entfernt, nicht nur ausgeblendet.
2. **Die beiden grossen Bilder 20 Prozent kleiner.** `#warum .section-photo` und `#nutzen .section-photo` von `max-width:680px` auf `544px`. Gerendert vorher 680 mal 511 und 673 mal 505, jetzt beide 544 mal 409. Dazu `justify-self:end` bei `#warum` und `justify-self:start` bei `#nutzen`, damit die Aussenkante buendig zur Inhaltskante bleibt.
3. **FAQ-Knoepfe laenger.** `.faq-grid` `max-width` von 1000 auf 1120 px. Der laengste Knopf, "Ersetzt die Analyse eine technische Konzeption?", braucht 535 px und hatte 490. Jetzt 550 px je Knopf, alle acht einzeilig bei 44 px Hoehe.
4. **Fehlende Trennlinie ergaenzt.** Zwischen `#analyse-formular` und `#faq` fehlte als einziger ein `section-divider`. Jetzt sieben statt sechs.
5. **Modul-Icons 20 Prozent groesser.** `.num-list .module-icon-frame` von 45 auf 54 px, `.num-list .module-icon` von 34 auf 41 px. `.num-list li` `padding-left` von 74 auf 83 px nachgezogen, damit der Abstand von 29 px zwischen Rahmenkante und Text erhalten bleibt.
6. **Footer geprueft.** Die goldene Linie ueber dem Footer ist vorhanden und kommt aus `.footer::before` in `shared-header-footer.css`. `analyse.html` bindet diese Datei ein, `.footer` steht auf `position: relative`, die Linie rendert. Punkt 6 und Punkt 4 waren dieselbe Sache: es fehlte genau eine Linie, und zwar die vor dem FAQ.
7. **Inhaltsbreite vereinheitlicht.** In `#warum` und `#nutzen` steckten Kicker, Headline und Subline innerhalb der Textspalte des `media-split` und wanderten dadurch mit. Gemessen vorher: `#warum` Titel 69 bis 630 statt voller Breite, `#nutzen` Titel erst ab 798. Der Kopf steht jetzt als `.section-inner > .media-copy` vor dem `media-split`, wie in `#leistungen`. Danach alle Sektionen: Titel 69 bis 1371, Subline 69 bis 889.

Zusaetzlich noetig geworden: `align-items:start` auf beiden `media-split`-Zeilen. Durch das Herausziehen des Kopfes stand das Bild sonst 142 beziehungsweise 128 px tief in der Zeile, weil die Spalten mittig ausgerichtet waren.

In `#nutzen` bleibt das Bild links, auf ausdrueckliche Vorgabe des Nutzers.

Alle Masse sind in `project_files/styleguide.md`, Abschnitt 21, festgehalten, auf Wunsch des Nutzers, damit sie abrufbar sind.

Pruefung bei 1440, 1100, 900 und 390 px: Eckenlinien nicht mehr im DOM, sieben Trenner mit einem vor dem FAQ, Icon-Rahmen 54 px, Fotos 544 mal 409 px ab 901 px, Footerlinie vorhanden.

Offen und nicht von dieser Aenderung verursacht, am Ausgangsstand gegengeprueft: ein waagerechter Seitenueberlauf von 290 px bei 1440 und 201 px bei 1100, sowie der Konsolenfehler `Identifier 'breadcrumbGroups' has already been declared`. Beides bestand vorher genauso.

Ebenfalls offen: Bei 1100 px bleibt ein FAQ-Knopf zweizeilig, weil die Inhaltsbreite dort nur rund 962 px betraegt und eine Spalte damit unter den noetigen 535 px liegt. Bei 1440 px ist es geloest.

## 2026-11-14 - Analyse-Grafiken auf gemeinsame Leinwand gebracht

Status: in Arbeit

Der Nutzer wies darauf hin, dass die beiden Grafiken der Angebotskarten weiterhin unterschiedlich gross wirken, und dass meine bisherigen Versuche das Ziel nicht erreichen. Das war zutreffend.

Ursache: Am CSS laesst sich nur der Rahmen einstellen, die Darstellungsgroesse bestimmt aber die Datei. `Analyse.png` hatte ein Motivverhaeltnis von 0,60, `deep_analysis.png` von 0,76. Bei gleicher Rahmenhoehe fuellt das zweite Motiv den Rahmen breiter aus, gemessen 167 mal 222 gegen 126 mal 221 Pixel, also 33 Prozent mehr Flaeche. Gleiche Darstellungsgroesse ist mit zwei verschiedenen Seitenverhaeltnissen in CSS nicht erreichbar, ohne zu verzerren oder zu beschneiden.

Zuvor verworfene Ansaetze, alle rein ueber CSS: gleiche Rahmenhoehe fuer beide, gleiche Flaeche ueber unterschiedliche Rahmenhoehen in zwei Richtungen. Keiner liefert gleich grosse Kaesten.

Der Nutzer hat am 2026-11-14 dem Ersetzen der bestehenden Dateien zugestimmt.

- `homepage/assets/Fotos/Analyse.png`: Motiv freigestellt, auf 963 mal 1600 skaliert, mittig auf eine Leinwand von 1078 mal 1600 gesetzt.
- `homepage/assets/Fotos/deep_analysis.png`: Motiv freigestellt, auf 1078 mal 1428 skaliert, mittig auf dieselbe Leinwand gesetzt.
- `homepage/index.html`: die Attribute `width` und `height` an allen zwoelf `img`-Elementen von 941 mal 1672 beziehungsweise 927 mal 1240 auf 1078 mal 1600 geaendert, damit der Seitenverhaeltnishinweis stimmt.

Beide Motive haben damit dieselbe Flaeche, 1 540 800 gegen 1 539 384 Pixel, Abweichung 0,09 Prozent. Beide Dateien haben dasselbe Seitenverhaeltnis, derselbe Rahmen ergibt deshalb zwangslaeufig denselben Kasten.

Am CSS wurde nichts geaendert, die Rahmenhoehe steht unveraendert auf 220 Pixel.

Ergebnis, gemessenes Motiv in der Seite: kostenlos von 126 mal 221 auf 135 mal 222 Pixel, plus 8 Prozent; tiefgehend von 167 mal 222 auf 151 mal 198 Pixel, minus 19 Prozent. Die zu grosse Grafik wurde also verkleinert, nichts wurde zu ihr hinaufskaliert.

Pruefung bei 1440, 1100, 768 und 390 Pixel: Kasten beider Grafiken identisch, Motivflaechen gleich innerhalb von 0,7 Prozent, beide Dateien geladen, natuerliche Groesse 1078 mal 1600, keine JavaScript-Fehler.

Dateigroesse: `Analyse.png` von 1 169 307 auf 1 171 815 Byte, `deep_analysis.png` von 1 558 549 auf 1 620 377 Byte.

Offen: Die kostenlose Grafik ist um 8 Prozent gewachsen. Auf Wunsch senke ich die Rahmenhoehe von 220 auf 209 Pixel, dann liegt sie bei 126 mal 209 und damit nicht ueber dem heutigen Stand, die tiefgehende bei 141 mal 186. Die Entscheidung steht aus, bis dahin ist nichts veroeffentlicht.

## 2026-11-14 - Formular: optionale Felder Telefon und Website entfernt

Status: geprueft

Vorgabe des Nutzers: die beiden optionalen Felder Telefon und Website streichen, auf jeder Seite, auf der das Formular vorkommt. Der Nutzer hat ausdruecklich auf besondere Vorsicht hingewiesen, weil das Formular mit vielen Stellen zusammenhaengt.

Vorherige Bestandsaufnahme, Suche ueber alle HTML-, JS-, JSON-, PY- und MD-Dateien ausserhalb von `.history` und `docs-graph`:

| Fundstelle | Art |
| --- | --- |
| `homepage/index.html` Zeile 2746, 2749 | Eingabefelder |
| `homepage/index.html` Zeile 999, 1002 | Rasterplaetze im CSS |
| `homepage/analyse.html` Zeile 923, 924 | Eingabefelder |
| `homepage/analyse.html` Zeile 1357, 1358 | `getFormState` |
| `homepage/analyse.html` Zeile 1431, 1437, 1479 | Nutzlast an `/analysis/start` und `/lead` |
| `project_files/homepage_postgres_data_contract.md`, `project_files/DATABASE_SCHEMA.md` | Datenbankspalten |

Geaendert wurde nur das Markup und das Raster:

- `homepage/index.html`: `<input name="telefon">` und `<input name="website">` entfernt.
- `homepage/index.html`: die Regeln `.nv-aform__grid > [name=telefon]` und `.nv-aform__grid > [name=website]` entfernt. Die verbleibenden Rasterplaetze von `email` bis `.nv-aform__submit` ruecken um eine Zeile nach: `email` auf `2 / 1 / 3 / 2`, `unternehmen` auf `2 / 2 / 3 / 3`, `branche` auf Zeile 3, `mitarbeiteranzahl` auf Zeile 3, `zeitaufwand` und `datenlage` auf Zeile 4, `herausforderung` auf Zeile 5, Datenschutz auf 6, Newsletter auf 7, Schaltflaeche auf 8. Ohne dieses Nachruecken waeren zwei Loecher im Raster geblieben.
- `homepage/analyse.html`: dieselben beiden Eingabefelder entfernt. Dort gibt es keine festen Rasterplaetze, die Felder fliessen.

Bewusst nicht geaendert: die JavaScript-Zeilen in `homepage/analyse.html`. `getFormState` liest weiterhin `data.get('telefon')` und `data.get('website')`. Ohne die Felder liefert das `null`, und `String(null || '').trim()` ergibt eine leere Zeichenkette. Die Nutzlast an das Backend behaelt damit exakt ihre Form: `company.website` und `contact.phone` bleiben als Schluessel erhalten und tragen einen leeren Wert. Haette man die Zeilen entfernt, waeren die Schluessel aus dem JSON verschwunden, weil `JSON.stringify` Eigenschaften mit `undefined` auslaesst.

Ebenfalls unangetastet: der Honeypot `website_confirmation`, der trotz des aehnlichen Namens ein eigenes Feld ist, die Pruefung in `homepage/index.html` Zeile 4133 und die Abfrage in `homepage/analyse.html` Zeile 1406.

Gemessene Nutzlast nach der Aenderung: `{"company":{"website":""},"contact":{"phone":""}}`. Das Uebergabeobjekt von `homepage/index.html` enthaelt die beiden Namen nicht mehr.

Formularhoehe vorher und nachher: `index.html` bei 1440 px von 649 auf 608 px, bei 390 px von 996 auf 913 px. `analyse.html` bei 1440 px von 635 auf 585 px, bei 390 px von 745 auf 695 px. Felderzahl `index.html` von 19 auf 17, `analyse.html` von 14 auf 12.

Pruefung bei 1440 und 390 px auf beiden Seiten: kein Feld `telefon` oder `website` mehr vorhanden, Honeypot vorhanden, Pflichtfeld Datenschutz vorhanden, keine Luecken im Raster, keine neuen JavaScript-Fehler.

Offen: Die Datenbankspalten `telefon` und `website` bestehen weiter und erhalten kuenftig leere Werte. Ob sie entfallen sollen, ist eine Entscheidung ueber das Datenmodell und wurde nicht getroffen. Ausserdem meldet `homepage/analyse.html` beim Laden `Identifier 'breadcrumbGroups' has already been declared`; der Fehler bestand nachweislich schon vor dieser Aenderung und wurde nicht angefasst.

## 2026-11-14 - Leistungskarten mobil: Bild als Kartenhintergrund, Abstand 20 px

Status: geprueft

Vorgabe des Nutzers: den Abstand oben und unten von 44 auf 20 px senken. Das war mit dem Bildstreifen rechnerisch nicht erreichbar, weil der 0,8 px breite Kartenrahmen und der 28 px hohe Bildstreifen allein schon 28,8 px ergeben. Auf Rueckfrage hat der Nutzer festgelegt, dass das Bild ueberhaupt kein Streifen werden soll, und aus zwei vorgelegten Moeglichkeiten den abgedunkelten Kartenhintergrund gewaehlt. Verworfen: gar kein Bild auf Mobil.

Das Bild lag auf Mobil bisher als Banner oben in der Karte, ein Ausschnitt eines Querformats. Jetzt fuellt es die Karte als Hintergrund, so wie es auf dem Desktop beim Ueberfahren der Karte ohnehin erscheint.

- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__visual`: von `position: static` mit `height: 28px` auf `position: absolute; inset: 0` mit `height: 100%`, dazu `object-position: center` und `filter: brightness(0.3) contrast(1.05) saturate(0.7)` fuer die Lesbarkeit des Textes.
- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__main`: `position` von `static` auf `relative`, `z-index: 2` ergaenzt, `padding` von `15px 12px 0` auf `19px 12px 0`.
- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__left`: `position` von `static` auf `relative`, `z-index: 2` ergaenzt, `padding` von `0 12px 43px` auf `0 12px 19px`.

`position: relative` ist hier unbedenklich, weil die vom Desktop geerbten Versatzwerte beider Bereiche auf 0 stehen. Bei `.nv-s7-card__points` waere es ein Fehler gewesen: dort steht `top: 145.6px` aus der Desktopregel, was die Liste um diesen Betrag nach unten geschoben haette. Dieser Fehler trat in einem Entwurf auf und wurde vor der Uebernahme behoben.

Ergebnis bei 390 px: oben 20 px, unten 20 px, dazwischen 50 px zwischen letztem Stichpunkt und Schaltflaeche. Karte 227 px, vorher 275 px.

Pruefung bei 360, 390, 430, 768 und 900 px: elf Karten, Hoehe 227 bis 241 px, CTA durchgaengig 30 px hoch, Mittenabweichung 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Ab 901 px unveraendert, Karten 88 px, CTA 23 px.

## 2026-11-14 - Leistungskarten mobil: Kartenabstand oben und unten auf 44 px

Status: geprueft

Vorgabe des Nutzers: den im vorigen Schritt angeglichenen Abstand von 37 px auf 44 px erhoehen, oben wie unten.

- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__main`: `padding` von `8px 12px 0` auf `15px 12px 0`. Der obere Abstand setzt sich aus dem 28 px hohen Bildstreifen, dem 0,8 px breiten Kartenrahmen und diesem Innenabstand zusammen und betraegt damit gemessene 44 px.
- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__left`: `padding` von `0 12px 36px` auf `0 12px 43px`. Zusammen mit dem Kartenrahmen ergibt das gemessene 44 px unter der Schaltflaeche.

Ergebnis bei 390 px: oben 44 px, unten 44 px, dazwischen 50 px zwischen letztem Stichpunkt und Schaltflaeche. Karte 275 px, vorher 261 px.

Pruefung bei 360, 390, 430, 768 und 900 px: elf Karten, Hoehe 275 bis 289 px, CTA durchgaengig 30 px hoch, Mittenabweichung 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Ab 901 px unveraendert, Karten 88 px, CTA 23 px.

## 2026-11-14 - Leistungskarten mobil: oberer und unterer Kartenabstand gleich

Status: geprueft

Der Nutzer hat die Begriffe festgelegt: Der obere Abstand ist der Abstand vom Text zum Kartenrand, der untere der Abstand von der Schaltflaeche zum Kartenrand. Drei zuvor vorgelegte Fassungen waren abgelehnt worden, weil darin jeweils der Abstand zwischen Text und Schaltflaeche gegen den unteren Kartenrand gestellt wurde, also das falsche Paar.

Gemessen vorher bei 390 px: oben 37 px vom Kartenrand bis zum Kopfblock, unten 9 px von der Schaltflaeche bis zum Kartenrand.

- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__left`: `padding` von `0 12px 8px` auf `0 12px 36px`. Zusammen mit dem 0,8 px breiten Kartenrahmen ergibt das gemessene 37 px unter der Schaltflaeche.
- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__more`: `margin-top` von 14 auf 50 px, nach ausdruecklicher Vorgabe des Nutzers.

Der obere Abstand von 37 px bleibt unveraendert; er setzt sich aus dem 28 px hohen Bildstreifen und 9 px Innenabstand zusammen.

Ergebnis bei 390 px: oben 37 px, unten 37 px, dazwischen 50 px zwischen letztem Stichpunkt und Schaltflaeche. Karte 261 px, vorher 197 px.

Pruefung bei 360, 390, 430, 768 und 900 px: elf Karten, Hoehe 261 bis 275 px, CTA durchgaengig 30 px hoch, Mittenabweichung 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Ab 901 px unveraendert, Karten 88 px, CTA 23 px.

## 2026-11-14 - Leistungskarten mobil: mehr Abstand zwischen Text und CTA

Status: geprueft

Der Nutzer bemaengelte, dass die CTA-Schaltflaeche zu dicht am Text sitzt. Im vorigen Schritt war `margin-top` von 6 auf 4 px gesenkt worden, um Hoehe zu sparen; gemessen betrug der Abstand vom letzten Stichpunkt bis zur Schaltflaeche 4 px.

- `homepage/index.html`, `@media (max-width: 900px)`, `.nv-s7-card__more`: `margin-top` von 4 auf 14 px.

14 px entspricht dem Abstand, den die Stichpunktliste nach oben hat. Gepruefte Alternativen: 10 px zu knapp, 18 px kostet 4 px Hoehe mehr ohne sichtbaren Gewinn.

Ergebnis bei 390 px: Abstand 14 statt 4 px, Karte 197 statt 187 px. Gegenueber dem Ausgangszustand von 233 px bleibt die Karte 36 px flacher.

Pruefung bei 360, 390, 430, 768 und 900 px: elf Karten, Hoehe 197 bis 211 px, CTA durchgaengig 30 px hoch, Mittenabweichung 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Ab 901 px unveraendert.

## 2026-11-14 - Leistungskarten mobil: flacher, CTA mittig

Status: geprueft

Der Nutzer bemaengelte an den Leistungskarten der Sektion mit den Leistungen, dass sie auf Mobil zu gross sind und dass die CTA-Schaltflaeche zu hoch ist und mittig sitzen soll. Gemessen vorher bei 390 px: Karte 233 px hoch, Bildstreifen oben 56 px, CTA 36 px hoch bei 10,4 px Schrift, linksbuendig bei x 13 statt mittig.

Alle Aenderungen liegen in der bestehenden Abfrage `@media (max-width: 900px)`, der Zuschnitt der Abfrage bleibt unveraendert.

- `homepage/index.html`, `.nv-s7-card__left`: `display` von `block` auf `flex` mit `justify-content: center`, `padding` von `0 12px 10px` auf `0 12px 8px`. Der CTA ist damit mittig; andere Kinder des Bereichs sind auf Mobil ohnehin ausgeblendet.
- `homepage/index.html`, `.nv-s7-card__more`: `height: 30px` ergaenzt, `margin-top` von 6 auf 4 px.
- `homepage/index.html`, `.nv-s7-card__visual`: `height` von 56 auf 28 px.
- `homepage/index.html`, `.nv-s7-card__main`: `padding` von `10px 12px 0` auf `8px 12px 0`.
- `homepage/index.html`, `.nv-s7-card__heading p`: `margin-top` von 5,6 auf 4 px.
- `homepage/index.html`, `.nv-s7-card__points`: `margin` von `8px 0 0 42px` auf `6px 0 0 42px`, `gap` von 5,6 auf 4 px.

Der Nutzer hat am 2026-11-14 aus vier vorgelegten Varianten den 28 px schmalen Bildstreifen gewaehlt. Verworfen: 40 px, 56 px unveraendert, und ganz ohne Bildstreifen.

Ergebnis bei 390 px: Karte 187 statt 233 px, also 46 px oder rund 20 Prozent weniger je Karte. Bei elf Karten rund 500 px weniger Scrollweg.

Pruefung bei 360, 390, 430, 768 und 900 px: elf Karten, Hoehe 187 bis 201 px, CTA durchgaengig 30 px hoch, Mittenabweichung 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Ab 901 px greift die Desktopdarstellung unveraendert, dort bleiben die Karten 88 px hoch mit 23 px hohem CTA.

Offen: Der CTA liegt mit 30 px unter der von Apple empfohlenen Mindestgroesse von 44 px fuer Beruehrungsziele. Die gesamte Karte ist ueber `data-href` anklickbar, der Verweis ist also auch ohne die Schaltflaeche erreichbar.

## 2026-11-14 - Analyse-Angebote: beide Grafiken im gleichen Rahmen

Status: geprueft

Vorgabe des Nutzers: Die Grafiken der beiden Angebotskarten muessen gleich gross sein. Gemessen vorher bei 1440 px: kostenlos 167 mal 294 px, tiefgehend 167 mal 222 px, also 72 px Hoehenunterschied. Ursache war eine Sonderregel, die nur der kostenlosen Karte einen hoeheren Rahmen gab.

- `homepage/index.html`: Regel `.nv-analyse__offer:not(.nv-analyse__offer--deep) .nv-analyse__visual { height: 292px; margin-top: 20px; }` entfernt. Beide Karten nutzen damit die Werte aus `.nv-analyse__visual`, also `height: 220px` und `margin: 56px 0 0`.
- `homepage/index.html`, `@media (max-width: 640px)`: die beiden Regeln zu `.nv-analyse__visual` zu einer zusammengefasst, `grid-area: auto; order: -1; width: 100%; height: 170px; align-self: auto; margin: 0`. Der doppelte Selektor war nur noetig, um die entfernte Sonderregel zu ueberstimmen.

Der Nutzer hat am 2026-11-14 aus drei vorgelegten Moeglichkeiten den kleineren gemeinsamen Rahmen gewaehlt. Verworfen: beide auf 294 px, dort rueckt die tiefgehende Grafik mit 222 px Breite dicht an die Punkteliste. Verworfen: gleiche sichtbare Flaeche statt gleicher Hoehe, dort blieben die Grafiken unterschiedlich hoch.

Rahmen nach der Aenderung, an jeder gepruefen Breite fuer beide Karten identisch: 1440 px 237 mal 222, 1100 px 182 mal 221, 1000 px 164 mal 221, 768 px 270 mal 222, 390 px 317 mal 170.

Die sichtbare Breite bleibt verschieden, 126 gegen 167 px bei 1440 px und 96 gegen 127 px bei 390 px. Das liegt an den Dateien: `Analyse.png` ist 941 mal 1672, `deep_analysis.png` 927 mal 1240. Eine Angleichung der Breite ginge nur ueber Verzerrung oder Beschnitt.

Nebeneffekt: Die kostenlose Karte ist bei 390 px nochmals 20 px kuerzer, 820 statt 840 px, und enthaelt keinen messbaren Leerraum mehr.

Pruefung bei 1440, 1100, 640, 430, 390 und 360 px, je mit und ohne Reduced Motion, beide Angebotskarten: Versatz des angetippten Punktes 0 bis 5 px, Klick oeffnet, erneuter Klick schliesst, Escape schliesst alle, Bildzuordnung folgt dem zuletzt geoeffneten Punkt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler.

## 2026-11-14 - Analyse-Angebote: Karten richten sich unter 980 px nach ihrem Inhalt

Status: geprueft

Der Nutzer bemaengelte, dass die Angebotskarten auf Mobil unnoetig gross sind und sich nicht an den Inhalt anpassen. Die Leere stammte nicht vom Inhalt, sondern aus Regeln, die nur fuer das Nebeneinander auf dem Desktop gedacht sind und unterhalb von 980 px mitliefen, wo die Karten untereinander stehen.

Gemessen bei 390 px vorher: kostenlose Karte 1108 px hoch, davon 183 px Leerraum in der Buehne, Fussbereich 198 px bei 92 px Bedarf.

- `homepage/index.html`, `@media (max-width: 980px)`, `.nv-analyse__offers`: `grid-auto-rows` von `1fr` auf `auto`. Die beiden Karten werden untereinander nicht mehr auf gleiche Hoehe gezogen.
- `homepage/index.html`, `@media (max-width: 980px)`, `.nv-analyse__offer > h3`: `min-height: 0`. Die 64 px dienten der Zeilenangleichung nebeneinander.
- `homepage/index.html`, `@media (max-width: 980px)`, `.nv-analyse__offer-footer`: `min-height: 0`. Die 190 px dienten der Angleichung von Preis und Schaltflaeche nebeneinander.
- `homepage/index.html`, `@media (max-width: 980px)`, `.nv-analyse__stage`: `flex: 0 0 auto`. Die Buehne saugt den uebrigen Platz nicht mehr auf.

Ergebnis, Hoehe der kostenlosen Karte geschlossen: 390 px Breite 1108 auf 840 px, 430 px Breite 1108 auf 840 px, 640 px Breite 1108 auf 761 px, 768 px Breite 727 auf 567 px, 980 px Breite 727 auf 545 px. Die Karte waechst beim Oeffnen eines Punktes wieder mit.

Desktop unveraendert: Ab 1000 px greifen die Regeln nicht. Bei 1440 px sind beide Karten weiterhin 741 px hoch und damit gleich hoch nebeneinander.

Pruefung bei 1440, 1100, 640, 430, 390 und 360 px, je mit und ohne Reduced Motion, beide Angebotskarten: Versatz des angetippten Punktes 0 bis 5 px, Klick oeffnet, erneuter Klick schliesst, Escape schliesst alle, Bildzuordnung folgt dem zuletzt geoeffneten Punkt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler. Zusaetzlich geprueft, dass bei geschlossener Karte das erste Bild aktiv, geladen und mit Deckkraft 1 sichtbar ist.

## 2026-11-14 - Analyse-Angebote: Steuerknoepfe entfernt, nur noch klickbare Karten

Status: geprueft

Vorgabe des Nutzers am 2026-11-14: entweder klickbare Karten oder Steuerelement, nicht beides. Da die Bedienung ueber den Klick auf die Karte ausdruecklich gewuenscht ist, entfallen die drei Knoepfe. Nach dem Wegfall des Akkordeons waren sie ohnehin ohne klare Funktion: `previous` und `next` haetten weitere Punkte geoeffnet, ohne etwas zu schliessen, und `exit` war durch den erneuten Klick auf die Karte doppelt belegt.

- `homepage/index.html`: sechs `button`-Elemente mit der Klasse `nv-analyse__control` entfernt, drei je Angebotskarte, Aktionen `previous`, `next` und `exit`.
- `homepage/index.html`: elf nun wirkungslose CSS-Zeilen zu `.nv-analyse__control` entfernt, davon neun im Hauptteil und zwei in der 640-px-Abfrage.
- `homepage/analysis-offers.js`: Sammlung `controls` entfernt, die drei `click`-Listener entfernt, Funktion `navigate` entfernt, Zeile `controls.forEach(button => { button.hidden = !hasOpenDetails; })` aus `syncState` entfernt.

Erhalten bleiben: `close` als Funktion, Escape schliesst weiterhin alle offenen Punkte und setzt den Fokus zurueck, die Bildzuordnung ueber `is-active`, `activeIndex` und `stage.dataset.checkingDetails`.

Pruefung bei 1440, 1100, 640, 430, 390 und 360 px, je mit und ohne Reduced Motion, beide Angebotskarten: kein `[data-action]`-Element mehr im DOM, Versatz des angetippten Punktes 0 bis 5 px, Klick oeffnet, erneuter Klick schliesst genau diesen Punkt, Escape schliesst alle, Bildzuordnung folgt dem zuletzt geoeffneten Punkt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler.

## 2026-11-14 - Analyse-Angebote: Klick oeffnet die Karte, sonst bewegt sich nichts

Status: geprueft

Der Nutzer meldete weiterhin Springen, mobil wie auf dem Desktop. Alle bisherigen Messungen galten der Hoehe des Abschnitts. Gemessen wurde nun die Position des angetippten Punktes selbst. Ergebnis vorher:

| Aktion | Folge |
| --- | --- |
| Punkt antippen, der unter dem offenen liegt | springt 95 bis 149 px nach oben |
| Punkt antippen, der ueber dem offenen liegt | bleibt stehen |

Ursache ist keine fehlerhafte Logik, sondern Geometrie. Durch das `name`-Attribut waren die `details` ein exklusives Akkordeon. Beim Antippen eines unteren Punktes ging der obere gleichzeitig zu, und alles darunter rutschte um dessen Hoehe nach oben. Solange das Zuklappen erzwungen wird, laesst sich das nicht beheben.

Der Nutzer hat am 2026-11-14 entschieden: Klick auf eine Karte oeffnet diese Karte, sonst passiert nichts. Eine zuvor gepruefte Variante, den Text unter die Punkteliste zu haengen, hat er als unprofessionell verworfen.

- `homepage/index.html`: Attribut `name="nv-analysis-free"` an fuenf und `name="nv-analysis-deep"` an fuenf `details`-Elementen entfernt. Damit schliesst sich kein Punkt mehr von selbst.
- `homepage/index.html`, `.nv-analyse__column`: `align-self: start` ergaenzt. Die Buehne steht auf `align-items: center`, wodurch die Spalte bei jedem Aufklappen neu zentriert wurde und um die halbe Zunahme wanderte, 15 px bei 1440 und 37 px bei 1100 px.
- `homepage/analysis-offers.js`: `activeIndex` ergaenzt, der den zuletzt geoeffneten Punkt festhaelt. `getOpenDetails` liefert diesen, solange er offen ist, sonst wie bisher den ersten offenen. Bildzuordnung und Steuerung folgen damit dem zuletzt geoeffneten Punkt statt dem obersten.
- `homepage/analysis-offers.js`, `navigate`: oeffnet den naechsten Punkt, ohne den aktuellen zu schliessen. Ist der naechste bereits offen, wird `syncState` direkt gerufen, weil dann kein `toggle` ausgeloest wird.
- `homepage/analysis-offers.js`, `close`: schliesst alle offenen Punkte statt nur des ersten und setzt den Fokus wie bisher auf dessen `summary`.
- `homepage/analysis-offers.js`, `toggle`-Listener: merkt sich den gerade geoeffneten Punkt, bevor `syncState` laeuft.

Pruefung bei 1440, 1100, 640, 430, 390 und 360 px, je mit und ohne Reduced Motion, fuer beide Angebotskarten, Punkte in der Reihenfolge 1, 3, 2, 5, 4 angetippt:

- Versatz des angetippten Punktes 0 bis 5 px, vorher 95 bis 149 px
- Klick oeffnet, erneuter Klick schliesst genau diesen Punkt
- `next` oeffnet den folgenden Punkt und laesst den vorigen offen, `previous` ebenso rueckwaerts
- `exit` und Escape schliessen alle Punkte und verstecken die drei Knoepfe
- Bildzuordnung folgt dem zuletzt geoeffneten Punkt
- kein waagerechter Seitenueberlauf, keine JavaScript-Fehler

Nicht geaendert: Texte, IDs, Assetpfade, Aufklappanimation, Bildanimation, Breitenwechsel der Karten von 58 auf 86 Prozent, Bild oben auf Mobil, saemtliche Farben.

## 2026-11-13 - Analyse-Angebote: Bild steht auch auf Mobil fest

Status: geprueft

Auf dem Desktop liegen Punktespalte und Bild in derselben Rasterzelle, das Bild bleibt deshalb stehen, waehrend die Karte darueber waechst. Unterhalb von 640 Pixeln stehen beide untereinander im normalen Textfluss, und das Bild stand unter den Punkten. Jede Karte, die aufging, schob es nach unten, gemessen 147 px bei 390 px Breite.

Der Nutzer hat am 2026-11-13 aus vier vorgelegten Varianten die kompakte gewaehlt: Bild ueber die Punkte, Hoehe auf 170 px.

- `homepage/index.html`, `@media (max-width: 640px)`: Regel `.nv-analyse__offer .nv-analyse__visual, .nv-analyse__offer:not(.nv-analyse__offer--deep) .nv-analyse__visual { order: -1; height: 170px; }` ergaenzt. Der doppelte Selektor ist noetig, weil die bestehende Regel `.nv-analyse__offer:not(.nv-analyse__offer--deep) .nv-analyse__visual` mit 292 px eine hoehere Spezifitaet hat als die Mobilregel `.nv-analyse__visual` und diese bisher ueberstimmte.

Verworfene Varianten: Bild oben in Originalgroesse, die Punkte beginnen dann erst nach rund 300 px Bild. Bild hinter die Karten legen wie auf dem Desktop, bei 390 px decken die Karten es fast vollstaendig ab, sichtbar bleibt nur ein Rest oben rechts. Bild auf Mobil ausblenden, haette die Sektion von 776 auf 481 px verkuerzt, das Bild aber entfernt.

Pruefung bei 360, 390, 430 und 640 px, beide Angebotskarten, jeder der fuenf Punkte einzeln geoeffnet: Bildversatz 0 px, kein abgeschnittener Karteninhalt, kein waagerechter Seitenueberlauf, keine JavaScript-Fehler.

Nebeneffekt bei der kostenlosen Karte: Da `.nv-analyse__offers` unterhalb von 980 px mit `grid-auto-rows: 1fr` beide Karten auf gleiche Hoehe zieht, hat die kostenlose Karte durch das kleinere Bild genug Reserve. Ihre Hoehe aendert sich beim Aufklappen gar nicht mehr. Gemessene Abschnittshoehe bei 390 px: 667,7 px in allen Phasen, Oeffnen, Umschalten und Schliessen.

Desktop unveraendert: Die Regel steht ausschliesslich in der 640-px-Abfrage. Bei 1440 und 1100 px sind Spalten-, Karten- und Bodybreite sowie der Bewegungsverlauf identisch. Der Bildvergleich der geoeffneten Karte weicht bei 1440 px in der kostenlosen Karte in einem Feld von 34 mal 32 Pixeln oben rechts ab. Das ist der `exit`-Knopf mit seinem animierten Goldverlauf, eine Phasenverschiebung von einem Frame, keine Layoutaenderung. Alle anderen Vergleiche: null abweichende Pixel.

Nicht geaendert: `analysis-offers.js`, Bildquelle und Assetpfad, Bildbreite von 100 Prozent auf Mobil, Reihenfolge im Quelltext, Texte, IDs, Desktopregeln.

## 2026-11-13 - Analyse-Angebote: Ausschlag beim Umschalten beseitigt

Status: geprueft

Korrektur zum vorigen Eintrag: Die dort angegebene Tabelle mit null Richtungswechseln beim Umschalten war zu grob abgetastet. Bei 8 Messpunkten pro Sekunde fiel der Ausschlag zwischen die Proben. Mit 125 Messpunkten pro Sekunde und einem Zeitstempel relativ zum Klick ist er eindeutig messbar. Das Entfernen der Breitenanimation hat das Bild ruhig gestellt, den Hoehenausschlag beim Umschalten aber nicht beseitigt.

Zwei Ursachen, beide durch Ausschluss belegt:

1. Ausschlag nach oben. Die Breite wechselt seit dem vorigen Eintrag sofort statt animiert. Beim Umschalten wird die zugehende Karte im selben Moment von 86 auf 58 Prozent schmal. Ihr Text bricht dadurch auf mehr Zeilen um, waehrend ihre Hoehe noch von `auto` auf `0` laeuft. Die `auto`-Hoehe waechst also genau in dem Augenblick, in dem sie schrumpfen soll.
2. Ausschlag nach unten. In `::details-content` lief `content-visibility` ueber `var(--analysis-speed)` gleich 0,5 s, die Hoehe aber ueber das 1,6fache gleich 0,8 s. Bei 0,5 s schaltete der Inhalt der zugehenden Karte diskret auf `hidden`, waehrend ihre Hoehenanimation noch 0,3 s weiterlief. Die Buehne sackte dadurch unter den Endwert und stieg danach wieder an.

Gemessener Ausschlag vorher, Buehnenhoehe beim Umschalten: 1440 px 26,6 px nach oben und 19,5 px nach unten, 1100 px 79,6 px nach oben und 12,4 px nach unten, 390 px 26,5 px nach oben und 12,4 px nach unten.

- `homepage/index.html`, `.nv-analyse__column`: `container-type: inline-size` ergaenzt. Die Spalte wird damit zur Containerreferenz.
- `homepage/index.html`, `.nv-analyse__body`: `width: 86cqw` ergaenzt. Der Inhalt behaelt damit die Breite der geoeffneten Karte, auch waehrend die Karte selbst schmal wird. Der Text bricht nicht mehr um, die ueberstehende Breite deckt das vorhandene `overflow: hidden` der Karte ab.
- `homepage/index.html`, `@media (max-width: 640px)`, `.nv-analyse__body`: `width: 100cqw` ergaenzt, weil die geoeffnete Karte dort 100 statt 86 Prozent breit ist.
- `homepage/index.html`, `.nv-analyse__disclosure::details-content`: erster Wert von `transition-duration` von `var(--analysis-speed)` auf `calc(var(--analysis-speed) * 1.6)` geaendert. `content-visibility` und `height` laufen damit gleich lang, der diskrete Umschaltpunkt faellt mit dem Ende der Hoehenanimation zusammen.

Pruefung, Buehnenhoehe je Phase, 125 Messpunkte pro Sekunde:

| Breite | oeffnen | umschalten | schliessen |
| --- | --- | --- | --- |
| 1440 px | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| 1100 px | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| 640 px | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| 390 px | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |

Gelesen als Ausschlag nach oben in px / Ausschlag nach unten in px / Richtungswechsel.

Darstellung unveraendert: Spaltenbreite, Kartenbreite und Bodybreite sind bei 1440, 1100, 640 und 390 px vor und nach der Aenderung auf das Pixel gleich. Bildvergleich der geoeffneten Karte bei 1440, 1100 und 640 px: null abweichende Pixel. Bei 390 px ist der Screenshot nicht reproduzierbar, zwei Laeufe derselben unveraenderten Fassung weichen um 32132 Pixel voneinander ab, der Vergleich vorher gegen nachher liegt mit 18493 Pixeln darunter.

Funktionspruefung bei 1440 und 390 px, jeweils mit und ohne Reduced Motion, fuer beide Buehnen: fuenf Punkte je Buehne, Knoepfe `previous`, `next` und `exit` erscheinen erst beim Oeffnen und verschwinden beim Schliessen, `next` und `previous` wechseln den Punkt, `exit` schliesst, Escape schliesst, Bodybreite gleich Kartenbreite, kein waagerechter Seitenueberlauf, keine Konsolenfehler.

Nicht geaendert: `analysis-offers.js`, Breitenwerte 58, 86, 88 und 100 Prozent, das `name`-Attribut und damit das Akkordeonverhalten, `interpolate-size`, Opazitaetsverlauf, Bildanimation, Texte, IDs, Assetpfade.

Offen: Unterhalb von 640 px schiebt die aufklappende Karte das darunter liegende Bild weiterhin nach unten. Gestapelte Darstellung, normaler Textfluss, vorbestehend, bewusst nicht angefasst.

## 2026-11-13 - Analyse-Angebote klappen ohne Springen auf

Status: geprueft

Der Nutzer meldete, der Abschnitt springe beim Oeffnen einer Karte hoch und runter statt fluessig aufzugehen.

Ursache: `.nv-analyse__disclosure` animierte die Breite von 58 auf 86 Prozent ueber `transition: width`. Waehrend die Breite laeuft, bricht der Text fortlaufend neu um, die Inhaltshoehe aendert sich also waehrend der Animation. Die Hoehenanimation des `::details-content` von `0` auf `auto` jagt damit einem wandernden Ziel hinterher, schiesst darueber hinaus und korrigiert zurueck. Durch das `name`-Attribut der `details`-Elemente sind die Punkte ein natives Akkordeon: beim Umschalten laufen zwei Hoehenanimationen gegeneinander, was den Ausschlag verstaerkt.

Gemessener Hoehenverlauf der Buehne beim Umschalten, vorher: 403 auf 410, dann auf 358, dann auf 376. Ausschlag 52 px, zwei Richtungswechsel.

- `homepage/index.html`, `.nv-analyse__disclosure`: Deklaration `transition: width var(--analysis-speed) var(--analysis-ease)` entfernt. Die Breite wechselt weiterhin von 58 auf 86 Prozent, nur nicht mehr animiert. Die Hoehenanimation des Aufklappens bleibt vollstaendig erhalten.

Pruefung, Richtungswechsel der Buehnenhoehe je Phase:

| Breite | oeffnen | umschalten | schliessen |
| --- | --- | --- | --- |
| 1440 px | 0 | 0 | 0 |
| 1100 px | 0 | 0 | 0 |
| 640 px | 0 | 0 | 0 |

Vorher lag das Umschalten bei zwei Richtungswechseln und 52 px Ausschlag. Die Kartenbreite wechselt weiterhin von 320 auf 477 px. Das Bild bleibt bei 1440 und 1100 px unbewegt.

Nicht geaendert: Hoehenanimation, Opazitaetsverlauf, `interpolate-size`, das `name`-Attribut und damit das Akkordeonverhalten, Breitenwerte, Texte, `analysis-offers.js`.

Offen: Unterhalb von 640 px schiebt die aufklappende Karte das darunter liegende Bild nach unten. Gestapelte Darstellung, normaler Textfluss, vorbestehend, bewusst nicht angefasst.

## 2026-11-13 - Bild der Analyse-Angebote steht fest

Status: geprueft

Der Nutzer meldete, dass das rechte Bild mitwandert. Vorgabe: Das Bild bleibt an fester Position, die gruenen Karten duerfen darueber laufen.

Ursache: `.nv-analyse__column` und `.nv-analyse__visual` liegen beide in `grid-area: 1 / 1`, die Buehne hat `align-items: center`. Beim Aufklappen waechst die Spalte, die Rasterzeile waechst mit, und das mittig ausgerichtete Bild wird neu zentriert. Zusaetzlich verschob und vergroesserte eine eigene Regel das erste Bild beim Oeffnen.

- `homepage/index.html`, `.nv-analyse__visual`: `align-self: start` ergaenzt und `margin: 0` zu `margin: 56px 0 0` geaendert. Das Bild haengt damit oben an der Buehne statt mittig und wandert beim Wachsen nicht mehr mit. Der Abstand entspricht der bisherigen mittigen Lage im geschlossenen Zustand.
- `.nv-analyse__offer:not(.nv-analyse__offer--deep) .nv-analyse__visual`: `margin-top: 20px` ergaenzt, passend zur groesseren Bildhoehe von 292 px. Der Selektor bestand bereits fuer die Hoehe.
- Regel `.nv-analyse__stage[data-checking-details="true"]:has(.nv-analyse__disclosure[open]) .nv-analyse__image-block:first-child .nv-analyse__image-wrapper { translate: ...; scale: 1.25; }` entfernt. Sie verschob und vergroesserte das Bild beim Oeffnen.
- Im Block `@media (max-width: 640px)`: `align-self: auto; margin: 0` fuer `.nv-analyse__visual` ergaenzt, damit die Aenderung dort nicht greift. Unterhalb von 640 px stehen Bild und Karten untereinander statt uebereinander.

Nicht geaendert: die Ueberlappung selbst. Karten und Bild liegen weiterhin in derselben Rasterzelle, die offene Karte laeuft weiter ueber das Bild. Ebenso unveraendert die Breiten 58 Prozent geschlossen und 86 Prozent offen, der Bildwechsel zwischen den Angeboten, `analysis-offers.js`, Texte, Preise und Assetpfade.

Pruefung, Lage des Bildes relativ zur Buehne, geschlossen gegen offen:

| Breite | vorher | nachher |
| --- | --- | --- |
| 1440 px | 20 auf 54 px, 56 auf 90 px | 20 auf 20 px, 56 auf 56 px |
| 1100 px | wanderte | steht fest |
| 640 px | gestapelt | gestapelt, unveraendert |
| 390 px | gestapelt | gestapelt, unveraendert |

Kein horizontaler Ueberlauf bei 1440, 1100, 640 und 390 px. Geschlossener Zustand bei 1440 px unveraendert gegenueber vorher, es verschiebt sich nichts fuer Besucher, die keine Karte oeffnen.

Offen: Unterhalb von 640 px schiebt die aufklappende Karte das darunter liegende Bild nach unten. Das ist normaler Textfluss in der gestapelten Darstellung und war dort auch vorher so; es wurde bewusst nicht angefasst.

## 2026-11-13 - Hero-Partikel-Canvas laeuft nicht mehr ausserhalb des Sichtfelds

Status: geprueft

Der Nutzer meldete Ruckeln. Die Messung zeigt: Ursache ist der WebGL-Partikelhintergrund im Hero, nicht die neu ergaenzten Abschnitte.

- `homepage/index.html`, Skriptblock des Hero-Partikel-Canvas: Die Zeichenschleife rief `requestAnimationFrame` bedingungslos auf und lief damit dauerhaft weiter, auch weit unterhalb des Heros und in einem unsichtbaren Tab. Sie pruefte als einzige der drei Animationsschleifen der Seite `prefers-reduced-motion` nicht.
- Die Schleife laeuft jetzt nur noch, solange das Canvas im Sichtfeld ist, ueber einen `IntersectionObserver` mit 100 px Vorlauf, und solange der Tab sichtbar ist. Bei reduzierter Bewegung wird ein einzelnes Standbild gezeichnet statt der Schleife.
- Zeichenlogik, Shader, Aufloesung, Bildrate und Erscheinungsbild unveraendert. Keine CSS-Regel, kein Markup und keine andere Datei geaendert.

Messung, Leerlauf ueber drei Sekunden ohne Scrollen, Hauptthread blockiert:

| Zustand | vorher | nachher |
| --- | --- | --- |
| Hero sichtbar | 91 % | 90 % |
| weit unten gescrollt | 91 % | 0 % |
| reduzierte Bewegung | 91 % | 0 % |

Eingegrenzt wurde die Ursache durch Ausschluss: ohne CSS-Animationen unveraendert 91 %, ohne Bilder unveraendert 91 %, ohne das Canvas `heroParticleCanvas` 0 %. Jedes der vier anderen Canvas einzeln entfernt aendert nichts. Die alte `index.html` vom Commit `45ad447` zeigt dieselben 91 %; das Verhalten ist also aelter als die zuletzt ergaenzten Abschnitte.

Einschraenkung: Der Testbrowser rendert mit SwiftShader, also in Software ohne Grafikkarte. Der Absolutwert fuer den sichtbaren Hero ist dadurch ueberzeichnet und auf einem Rechner mit Grafikkarte niedriger. Der Befund, dass die Schleife ausserhalb des Sichtfelds weiterrechnet, ist davon unabhaengig.

Pruefung: Hero nach der Aenderung unveraendert dargestellt, Partikelglobus vorhanden. Angebotsbereich weiterhin funktionsfaehig, Oeffnen, Blaettern und Schliessen durchgespielt. Keine Seitenfehler.

Offen: Ob der Hero auf echter Hardware noch ruckelt, kann hier nicht entschieden werden. Falls ja, waeren eine Begrenzung der Pixeldichte auf 1 statt 2 oder eine Begrenzung der Bildrate zu pruefen; beides veraendert das Erscheinungsbild leicht und ist nicht ohne Freigabe umzusetzen.

## 2026-10-17 - Drei Hero-Grafiken fuer Detailseiten ergaenzt, nachtraeglich dokumentiert

Status: offen

Nachtrag zu Commit `45ad447` vom 2026-10-17, Betreff „neue hero bilder". Der Commit hatte als einziger seit dem 2026-10-13 keinen Changelog-Eintrag; die uebrigen Commits dieses Zeitraums wurden von ihren Autoren selbst dokumentiert. Dieser Eintrag beschreibt ausschliesslich, was der Diff zeigt.

- `homepage/assets/detail_pages_grafics/chatbot_detail_page.png`: neu.
- `homepage/assets/detail_pages_grafics/sprachassistent_detail_page.png`: neu.
- `homepage/assets/detail_pages_grafics/cahtbots_detail_page.png` nach `daten_detail_page.png` umbenannt, Dateiinhalt unveraendert. Der alte Name enthielt einen Schreibfehler; die Datei dient nun der Daten-Detailseite.
- Keine HTML-, CSS- oder JavaScript-Datei im Commit geaendert.

Pruefung: Der alte Name `cahtbots_detail_page.png` war in keiner HTML-Datei verlinkt, die Umbenennung hat also keinen Verweis gebrochen. Alle drei Dateien liegen im Projekt.

Offen: Keine der drei Grafiken ist bisher eingebunden. Im HTML verwendet werden aus diesem Ordner nur `chatbots_detail_grafic.webp`, `daten_dokumente_detail_grafic.webp` und `sockel_loaded_analyse.png`. Zu klaeren ist, auf welchen Detailseiten die drei neuen PNG-Dateien die bestehenden WebP-Grafiken ersetzen sollen und ob sie als PNG oder als WebP eingebunden werden.

## 2026-11-13 - Fehlende Dateien der Startseite ergaenzt, Blocker aufgeloest

Status: geprueft

- `homepage/analysis-offers.js`: neu, vom Nutzer geliefert. Steuert je Angebotskarte die `details`-Elemente `.nv-analyse__disclosure` und die drei Bedienelemente `previous`, `next`, `exit`, blendet diese nur bei geoeffnetem Angebot ein, schaltet den zugehoerigen `.nv-analyse__image-block` auf `is-active` und schliesst per Escape. Reines DOM-Skript ohne Netzwerkaufruf.
- `homepage/assets/seo-check-preview-gunmetal.png`: neu, vom Nutzer geliefert, 1536 x 1024, aus WebP nach PNG mit Alphakanal gewandelt. Entspricht den im Markup angegebenen Abmessungen.
- Keine Zeile in `homepage/index.html` geaendert; die Datei verwies bereits auf beide Pfade.

Pruefung: Alle sieben vom Skript verwendeten Selektoren im Markup vorhanden. `node --check` fehlerfrei. Im Browser durchgespielt: Start geschlossen und ohne Bedienelemente, nach dem Oeffnen drei Bedienelemente und aktiver Bildbereich, Weiter und Zurueck blaettern durch die fuenf Angebote, Schliessen raeumt auf. SEO-Bild mit 1536 x 1024 geladen. Gerendert bei 1440, 900 und 390 px: kein horizontaler Ueberlauf, zehn Sektionen, Formular vorhanden, keine Seitenfehler.

Berichtigung zum Eintrag weiter unten: `assets/cards/cards_problem_loesung/best_card_single%20470x360.webp` fehlte nie. Der Pfad ist URL-kodiert, die Datei existiert mit echtem Leerzeichen im Namen. Die frueher gemeldete fehlende Datei war ein Fehler der Pruefung, nicht der Seite.

Offen: keine. Die Startseite ist deploybar.

## 2026-11-13 - Goldwort-Regel als offene Entscheidung festgehalten

Status: blockiert

- `project_files/todo.md`, Abschnitt Homepage - Design / Komponenten: der Punkt zur Goldwort-Regel ist von `offen` auf `blockiert` gesetzt und um den Widerspruch ergaenzt. `styleguide.md` Zeile 106 schreibt fuer die Website den Goldverlauf ueber den kompletten Text vor, `todo.md` verlangte bisher genau ein tragendes Wort. Beides kann nicht gleichzeitig gelten.
- Festgehalten ist ausserdem der tatsaechliche Produktionsstand: alle `h1`/`h2` tragen ueber `nurovelle.css` den vollen Goldverlauf; Ausnahme sind die drei Abschnitte `#fallbeispiel`, dort traegt genau ein Wort den Verlauf, auf ausdrueckliche Vorgabe des Nutzers.
- Der Nutzer hat entschieden, die Frage vorerst offen zu lassen. Es wurde deshalb weder `styleguide.md` geaendert noch eine der drei Ueberschriften umgestellt.
- Keine Aenderung im Produktionscode.

## 2026-11-13 - Schriftangabe in AGENTS.md berichtigt

Status: fertig

- `AGENTS.md`, Abschnitt Typografie: `Eastman Grotesque Alt` als Headline-Schrift durch `Exo 2` ersetzt. Die Angabe widersprach `styleguide.md` Zeile 151, wo `Exo 2` als aktive Display-Schrift steht und ausdruecklich festgehalten ist, dass es kein zweites Fontsystem gibt. Der Nutzer hat bestaetigt, dass `Exo 2` und `Inter` die gueltigen Schriften sind.
- `Eastman Grotesque Alt` in die Liste der nicht neu zu verwendenden Schriften aufgenommen.
- Verweis auf `styleguide.md` als zustaendige Quelle ergaenzt, damit die Angabe nicht erneut auseinanderlaeuft.
- Keine Schrift im Produktionscode geaendert. Die Seiten verwenden unveraendert `Exo 2` und `Inter`.

## 2026-11-13 - Startseite auf den vom Nutzer gelieferten Stand gesetzt

Status: blockiert

- `homepage/index.html`: vollstaendig durch die vom Nutzer hochgeladene Fassung ersetzt. Der bisherige Stand war laut Nutzer nicht der gueltige. Geaendert sind im Wesentlichen der Angebotsbereich `.nv-analyse__*` einschliesslich `.nv-analyse__disclosure`, `.nv-analyse__body`, `.nv-analyse__image-block` und `.nv-analyse__control`, die Hero-CTA-Buttons sowie `.seo-placement__*`. 315 geaenderte Zeilen, 97 Zeilen mehr als zuvor.
- Keine Sektion und kein Element entfernt oder ergaenzt: die Menge der `id`-Werte ist vor und nach dem Austausch identisch, ebenso die Zahl der `section`-Elemente.
- Keine andere Datei geaendert.

Pruefung: Tagbilanz ausgeglichen, Dokument vollstaendig von `<!DOCTYPE html>` bis `</html>`. Gerendert bei 1440, 900 und 390 px: kein horizontaler Ueberlauf, zehn Sektionen, Formular vorhanden. Alle zehn Angebots-Bloecke sind ohne JavaScript sichtbar, es wird kein Inhalt verborgen.

Offen: Die gelieferte Fassung verweist auf zwei Dateien, die weder im Arbeitsbaum noch in der Git-Historie eines Branches existieren:

- `homepage/analysis-offers.js`, eingebunden in Zeile 4134 als `<script src="analysis-offers.js" defer>`. Ohne diese Datei bleiben die sechs Bedienelemente `.nv-analyse__control` (`previous`, `next`, `exit`) ohne Funktion.
- `homepage/assets/seo-check-preview-gunmetal.png`, dreimal eingebunden in den Zeilen 1996, 2169 und 3038 mit `width="1536" height="1024"`. Ohne diese Datei bleibt an drei Stellen ein leerer Bildbereich.

Beide Dateien wurden nicht ersatzweise erzeugt und es wurde kein Fallback eingebaut. Die Startseite ist deshalb nicht zum Deployment freigegeben. Vorbestehend fehlt unveraendert `assets/cards/cards_problem_loesung/best_card_single%20470x360.webp`; dieser Verweis stand bereits vorher so in der Datei.

## 2026-11-13 - Drei Faelle der Case Study in die Detailseiten eingebaut

Status: in Arbeit

- `homepage/detail_datenabgleich.html`: Abschnitt `#fallbeispiel` vor `#kontakt` ergaenzt. Szenario A der Case Study, Belegverarbeitung in einer Steuerkanzlei. Vier Schritte mit den Icons `dokumente`, `datenabgleich`, `api`, `valedierung`.
- `homepage/detail_prozessautomatisierung.html`: Abschnitt `#fallbeispiel` vor `#kontakt` ergaenzt. Szenario B, Angebotserstellung in einem Elektroinstallationsbetrieb. Vier Schritte mit `figur_tablett`, `klembrett`, `speicher_vernetzt`, `mail_bot`.
- `homepage/detail_prompt-engineering.html`: Abschnitt `#fallbeispiel` vor `#kontakt` ergaenzt. Szenario C, Produktbeschreibungen in einem Online-Shop fuer Gartenbedarf. Drei Schritte mit `software`, `lupe_keyword`, `valedierung`; das Dokument nennt fuer dieses Szenario drei Bestandteile, ein vierter wurde nicht erfunden.
- Alle Angaben zu Unternehmensgroesse, Vorgangsvolumen, Aufwand, Investition, Zeitersparnis, Fehler- und Erfolgsquote, Umsatzwirkung, ROI und Amortisation stammen unveraendert aus `Dokumente_lead/final/case_studies/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.docx`. Die Saetze unter UMSETZUNG und die Lerneffekte der REGELBOX sind woertlich uebernommen.
- Je Seite drei auf `#fallbeispiel` begrenzte CSS-Bloecke im seitenlokalen `<style>`: Spaltenbreite 820 px, Stufenaufbau mit Haarlinie, Schrittliste `.fb-schritte`. Eigene Klasse statt `.num-list`, weil zwei Detailseiten `.num-list` seitenlokal als nummerierte Liste ohne `.module-img` definieren.
- Jeder Abschnitt schliesst mit der Herkunftsangabe und dem Link auf `assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf`, die Datei liegt im Projekt und ist bereits von der Startseite verlinkt.
- Keine andere Sektion, kein Text, keine ID, kein Assetpfad und keine bestehende Logik dieser Seiten geaendert. Die uebrigen zehn Detailseiten unveraendert.

Pruefung: Alle Zahlen des Dokuments im jeweiligen Abschnitt wiedergefunden, 14 von 14, 12 von 12 und 13 von 13. Gerendert bei 1440 px: drei Stufen, Icons geladen, genau ein Wort der Ueberschrift im Goldverlauf, Herkunftslink vorhanden, kein horizontaler Ueberlauf. Alle zehn verwendeten Icon-Dateien im Projekt vorhanden.

Offen: visuelle Abnahme durch den Nutzer. Die Goldwort-Fassung der Ueberschrift weicht von `styleguide.md` Abschnitt Goldwort-Regel ab, siehe dort.

## 2026-10-15 - Gemeinsamer Bildbereich fuer die Analyse-Angebote

Status: in Arbeit

- `homepage/index.html`: `.nv-analyse__comparison` gruppiert die vorhandenen Angebote mit einem gemeinsamen Bildbereich `.nv-analyse__visual`. Desktop zweispaltig, bis 980 px untereinander; Bildbreite mobil maximal 320 px.
- `assets/Fotos/Analyse.png` der kostenlosen Potenzialanalyse und `assets/Fotos/deep_analysis.png` der Tiefenanalyse gemaess Nutzerfreigabe zugeordnet. Beide PNG-Dateien unveraendert eingebunden, mit ihren realen Abmessungen und `object-fit: contain` ohne Beschnitt oder Verzerrung.
- `.nv-analyse__image`, `.nv-analyse__image--free` und `.nv-analyse__image--deep`: CSS-Bildwechsel ueber den bestehenden offenen Details-Zustand der Tiefenanalyse; initial kostenloses Bild. Reduced Motion deaktiviert den Uebergang. Keine neue JavaScript-Logik.
- Angebotstexte, Preise, Links, Regler/Gauge, Formular einschliesslich Consent/Honeypot, IDs, alle bestehenden Scripts und Assetpfade unveraendert.

Pruefung: HTML5-Parser ohne Fehler, CSS-Parser, JavaScript-Syntax, JSON-LD, unveraenderte Formular-/Angebots-/Regler-/Script-Struktur und IDs erfolgreich. Im lokalen Browser beide Bilder geladen und Bildwechsel in beide Richtungen sowie gegenseitiges Schliessen der Angebote bestaetigt. Keine Seitenfehler in den abgefragten Konsolenlogs; vorhandene Electron-CSP-Warnungen.

Offen: visuelle Desktop-/Mobile-Abnahme, da Screenshot-Aufnahme mit Zeitueberschreitung scheiterte und die angeforderte 390-px-Viewport-Umstellung nicht wirksam wurde. Tastaturumschaltung und Reduced Motion nicht im Browser bestaetigt. Kein Formularversand, Push oder Deployment.

## 2026-10-14 - Analysesektion ohne Bilder fertig umgesetzt

Status: in Arbeit

- `homepage/index.html`: Reihenfolge Regler/Gauge, gemeinsam gruppierte aufklappbare Analysen und Formular darunter abgeschlossen. Preise, Hinweise und Tiefenanalyse-Link dauerhaft sichtbar, kostenlose Analyse initial offen. Tastatur-Fokusrahmen und native Summary-Bedienung erhalten.
- Dezenter 240-ms-Reveal der geoeffneten Inhalte mit Reduced-Motion-Regel. Mobile Angebotspadding und Titelumbruch angepasst; Preisraster auf verfuegbare Breite begrenzt. Formular ohne perspektivische Neigung ueber volle Inhaltsbreite.
- Hinweis `Formular direkt darunter.` an neue Position angepasst. Alle weiteren Texte, Regler, Gauge, Formularfelder, Consent, Honeypot und Scripts unveraendert.
- Bilder werden spaeter hinzugefuegt; keine leere Bildspalte oder Platzhalter im aktuellen Bereich.

Pruefung: CSS-Parser, unveraenderte Formular-/Regler-/Script-Struktur und Angebotsinhalte bis auf beauftragten Hinweis sowie `git diff --check` erfolgreich.

Offen: gerenderte Desktop-/Mobile-/Tastaturpruefung weiterhin wegen nicht verfuegbarem Browserzugriff ausstehend. Kein Push oder Deployment.

## 2026-10-14 - Analysesektion als aufklappbarer Bereich vorbereitet

Status: in Arbeit

- `homepage/index.html`: zwei bestehende interaktive Cards mit Reglern und Gauge oberhalb erhalten. Beide Analyse-Angebote darunter als native, gemeinsam gruppierte Details-/Summary-Bereiche umgesetzt; kostenlose Analyse initial offen. Preise, Hinweise und Tiefenanalyse-Link bleiben ausserhalb der aufklappbaren Texte sichtbar.
- Bestehendes Formular `#nvAnaForm` unter beide Angebote verschoben, ueber volle Inhaltsbreite. Alle Feldattribute, IDs, Consent, Honeypot und JavaScript unveraendert.
- Neue lokale Klassen `.nv-analyse__disclosure`, `.nv-analyse__summary`, `.nv-analyse__body`; vorhandene Card-Farben und Assets erhalten. Keine externe GSAP-/Tweakpane-Abhaengigkeit eingebaut.
- Hinweis gemaess Nutzerauftrag auf `Formular direkt darunter.` korrigiert; sonstiger Analyse-Wortlaut unveraendert.

Pruefung: CSS-Parser, unveraenderte Angebotsinhalte/Preise, Formularattribute, Regler-Card und gesamte Scripts sowie `git diff --check` erfolgreich.

Offen: eindeutige Bildzuordnung fuer beide Analysen beim Nutzer angefragt. Der gemeinsame Bildbereich und Bildwechsel sind daher noch nicht umgesetzt. Browser-/Mobile-/Tastaturpruefung weiterhin ausstehend. Kein Push oder Deployment.

## 2026-10-14 - Kontakt-Einleitung breiter

Status: in Arbeit

- `homepage/index.html`: `.nv-contact__intro` von maximal 58ch auf 90ch verbreitert, damit der vollstaendige Einleitungstext auf breitem Desktop in zwei Zeilen passt.
- Wortlaut, Typografie, Cards, mobile verfuegbare Inhaltsbreite und JavaScript unveraendert. Kein Abschneiden oder Line-Clamp.

Pruefung: CSS-Parser und `git diff --check` erfolgreich. Tatsaechlicher Zweizeilenumbruch im Browser noch nicht geprueft. Kein Push oder Deployment.

## 2026-10-14 - Projektstart-Card-Texte leichter und ausgerichtet

Status: in Arbeit

- `homepage/index.html`: `.nv-step-card h3` mit Schriftgewicht 600 statt 750, `.nv-step-card p` mit 400 statt 500.
- `.nv-step-item:nth-child(1) .nv-step-card__content` rechtsbuendig, zweite Card zentriert, dritte Card weiterhin linksbuendig. Normale Leserichtung bleibt erhalten.
- Wortlaut, Schriftgroessen, Schriften, Farben, Bilder, Abstaende, CTAs und JavaScript unveraendert.

Pruefung: CSS-Parser, unveraenderte HTML-/JavaScript-Struktur und `git diff --check` erfolgreich. Gerenderte Browserpruefung weiterhin blockiert. Kein Push oder Deployment.

## 2026-10-14 - Card-Hintergrundlogo groesser und dezenter

Status: in Arbeit

- `homepage/index.html`: Logo-Hintergruende von `.nv-analyse__offer`, `.nv-contact__portrait`, `.nv-contact__card` und `.download-item` auf 85 % Breite vergroessert (vorher 46 % bzw. 58 %).
- Logo-Deckkraft im Ruhezustand von 7 % auf 2,5 %, bei vorhandenem Hover/Focus von 20 % auf 4 % reduziert.
- Logo-Asset, Card-Schimmer, Rahmen, Inhalte, Layout und JavaScript unveraendert.

Pruefung: CSS-Parser, unveraenderte HTML-/JavaScript-Struktur und `git diff --check` erfolgreich. Gerenderte Browserpruefung weiterhin blockiert. Kein Push oder Deployment.

## 2026-10-14 - Ablaufmodule enger angeordnet

Status: in Arbeit

- `homepage/index.html`: `.nv-process__steps` auf maximal 1000 px statt 1440 px begrenzt, Spaltengap auf 24 px gesetzt und oberen Abstand von 20 auf 12 px reduziert.
- `.nv-process__visual`: Skalierungsursprung nach oben verlegt und die durch Skalierung ungenutzte Hoehe im unteren Abstand ausgeglichen. Sichtbare Modul-/Sockelgroesse bleibt unveraendert; Abstand zur Beschriftung auf 14 px reduziert.
- `.nv-process__step:not(:last-child)::after`: bestehende Verbindungspfeile mittig im kleineren Spaltengap und auf Hoehe der nach oben gerueckten Module ausgerichtet.
- Texte, Assets, Modulreihenfolge, CTAs, Formulare, JavaScript sowie bestehende Mobile-Visual-Regeln unveraendert.

Pruefung: CSS-Parser, unveraenderte HTML-/JavaScript-Struktur und `git diff --check` erfolgreich.

Offen: gerenderte Desktop-/Mobile-Pruefung durch weiterhin blockierten Browserzugriff. Lokal geaendert; kein Deployment.

## 2026-10-14 - Raster entfernt, Bildeffekte zurueckgenommen und SEO Toolbox erklaert

Status: in Arbeit

- `homepage/index.html`: Raster aus `--nv-holo-face` entfernt; vorhandene Gold-/Smaragd-Schimmer erhalten, Grundflaeche auf vorhandenen Schwarz-Token gesetzt. Unbenutzte `--nv-holo-overlay`-Variable und Bild-Overlay-Regel entfernt.
- `.nv-about__media`, `.nv-step-card` und `.nvp4-projectidea__image`: zusaetzliche Card-Neigung, Materialkanten und Hover-Ausrichtung auf Bildern auf den Stand vor `38eb1d3` zurueckgenommen, einschliesslich mobiler Projektstart-Regeln. Bestehende Staffelung und Bild-Assets erhalten.
- `.nv-analyse__offer--deep .nv-analyse__offer-list li`: ausschliesslich die sechs Bulletpoint-Texte der Tiefenanalyse-Card mit vorhandenem Goldtoken dargestellt. Irrtuemliche Goldfaerbung des Preishinweises zurueckgenommen; beide Angebotshinweise bleiben grau. Gruene Bulletpoint-Symbole und die kostenlose Card unveraendert. Zwei bestehende `!important`-Deklarationen der Hinweisregel durch gezielte Selektoren ersetzt.
- Vorhandene Logo-Hintergrundregeln ueber `--asset-logo-mark` mit dem realen, bereits im Header verwendeten Asset `assets/hero/nurovelle_logo_gold.png` verbunden; vorhandene dezente Deckkraft erhalten.
- Drei bestehende `.nv-seo-promo`-Hinweise um Titel `SEO Toolbox` und Satz `Pruefen Sie Ihre Website auf SEO-Probleme und Verbesserungspotenzial.` ergaenzt (im HTML mit Umlaut). Kompakte schwarze Box mit vorhandenem Goldrahmen; Mobile maximal 320 px. Vorhandener Einflug von links nach rechts, Observer, Reduced Motion, CTA und Link `detail_seo.html` erhalten.
- Formulare, Consent, Honeypot, gesamte JavaScript-Logik, Bilder und Assetpfade unveraendert. Bereits vor Arbeitsbeginn vorhandene Download-Aenderungen erhalten.

Pruefung: CSS-Parser, JavaScript-Syntax, identische Formular-/Script-/Bildstruktur und `git diff --check` erfolgreich.

Offen: gerenderte Desktop-/Mobile- und Reduced-Motion-Pruefung sowie Browserkonsole, da Browsernavigation blockiert war. Lokal geaendert; kein Push oder Deployment.

## 2026-10-13 - Holo-Card: isolierte Musterkarte mit leichter Ruhe-Neigung

Status: in Arbeit

- Isolierte lokale Musterdatei `/home/d4sd1ng/.codex/visualizations/2026/10/12/01a13205-05ad-70e3-a3bf-b8ed1a0c86df/holo-card-sample.html` erstellt. `.holo-shell` verwendet 2 Grad X-/minus 3 Grad Y-Neigung und 4 px vertikalen Versatz im Ruhezustand. Bei Hover auf hoverfaehigen Geraeten und bei Tastaturfokus richtet sie sich gerade aus. Keine Mausverfolgung oder Dauerschwebe-Animation.
- `.holo-shell::before` bildet eine um 4,8 px versetzte, scharfe Seitenkante; `.holo-card` verwendet eine dunkle transparente Flaeche und vorhandene Nurovelle-Goldmaterialien ohne Blur. Vorhandene Schriften, PDF-Icon, Downloadziel und Text der ersten Homepage-Downloadkarte wiederverwendet. Reduced Motion deaktiviert Neigung und Uebergang.
- `homepage/index.html` und `homepage/shared-header-footer.css` waehrend dieser Musterarbeit unveraendert; SHA-256 vor und nach der Arbeit identisch. Kein Rollout auf vorhandene Cards, kein Push oder Deployment.

Pruefung: HTML-/CSS-Parser, vorhandene lokale Asset-/Font-/Downloadpfade, Ruhe-/Hover-/Fokus-Regeln und Reduced Motion statisch erfolgreich geprueft.

Offen: gerenderte Desktop-/Mobile-Pruefung durch weiterhin blockierten Browserzugriff nicht durchgefuehrt. Visuelle Freigabe des Musters vor einer Uebertragung auf die Homepage ausstehend.

## 2026-10-13 - FAQ: Fragenblock nicht mehr ueber volle Sektionsbreite

Status: fertig

- `homepage/index.html`, `.nv-faq-grid`: die bislang voll gestreckte Flex-Zeile durch zwei gleich breite Grid-Spalten ersetzt. `width: max-content` dimensioniert den Fragenblock anhand der laengsten Frage, `max-width: 100%` begrenzt ihn auf die verfuegbare Sektionsbreite. Vorhandene linke Ausrichtung und 16-px-Spaltengap erhalten; die einzelnen Frage-Buttons bleiben auf volle Spaltenbreite gestreckt.
- `.nv-faq-item p`: `contain: inline-size` verhindert, dass aufgeklappte Antworttexte die inhaltsbasierte Breite des Fragenblocks vergroessern. Die Antworthoehe bleibt inhaltsabhaengig.
- Vorhandene mobile `.nv-faq-grid`-Regel auf eine volle Grid-Spalte mit `width: 100%` angepasst. Mobile Mindesthoehe, Textumbruch und kompakte Abstaende unveraendert.
- Sektionsbreite, Ueberschrift, alle acht Fragen und Antworten, Gold-Buttons, Footer, Assets, IDs, Links, Formulare und JavaScript unveraendert. Keine neuen globalen Overrides oder `!important`-Regeln.

Pruefung: lokale HTML-/CSS-Parser, unveraenderte FAQ-Inhalte und HTML-Struktur, Grid-/Breitenregeln fuer Desktop und Mobile, JavaScript-Syntax, Formular-/Linkvertraege, bestehende Regressionstests und `git diff --check` erfolgreich.

Offen: keine gerenderte Desktop-/Mobile-Pruefung wegen weiterhin blockiertem Browserzugriff. Aenderung lokal ausgefuehrt; kein Push oder Deployment.

## 2026-10-13 - Footer: Copyright mittig und golden

Status: fertig

- `homepage/shared-header-footer.css`: `.footer-bottom` verwendet gleich breite aeussere Grid-Spalten um die Copyright-Spalte. `.footer .footer-copy` steht mittig in der unteren Zeile unter dem Pfeil, mit zentriertem Text und dem vorhandenen Gold-Token `--nv-gold-highlight` / `#FAE385`. Rechtliche Links bleiben links in derselben Desktop-Zeile.
- Copyright aus der gemeinsamen grauen Textregel herausgenommen. Bestehende wirksame Schriftwerte erhalten und die vorhandene Copyright-Regel gezielt gegen die allgemeine Footer-Absatzregel abgegrenzt. Mobile behaelt eine eigene, mittige Copyright-Zeile mit erlaubtem Textumbruch.
- Wortlaut, Links, Assets, IDs, Formulare und JavaScript unveraendert. Keine neuen Overrides, Farben oder `!important`-Regeln. Die gemeinsame Footer-CSS wirkt auf alle Seiten, die sie einbinden.

Pruefung: bestehende lokale Regressionstests, HTML-/CSS-Parser, JavaScript-Syntax, unveraenderte Formularvertraege, Copyright-Spalte, Zentrierung, Goldtoken und Mobile-Umbruchregeln erfolgreich. Gerenderte Desktop-/Mobile-Pruefung weiterhin durch Browserzugriff blockiert. Kein Push oder Deployment.

Offen: FAQ-Buttons sollen gleichmaessig gestreckt bleiben, jedoch in einem schmaleren Fragenblock statt ueber die volle Seitenbreite. Die gewuenschte maximale Desktop-Breite ist noch nicht festgelegt; FAQ bis zur Klaerung unveraendert.

## 2026-10-13 - Leistungskarten: urspruengliche Hintergrundzustaende wiederhergestellt

Status: fertig

- `homepage/index.html`: `.nv-s7-card` wieder mit transparentem Hintergrund im geschlossenen Zustand. Die vorhandene Hover-/Focus-/Aktiv-Regel verwendet wieder `var(--color-gunmetal-dark)`. Beide Regeln entsprechen dem Stand vor der Hintergrund-Aenderung in `4903c28`.
- Ausschliesslich diese beiden Hintergrunddeklarationen geaendert. Alle elf Leistungskarten, Texte, Layout, Assets, Links, IDs, JavaScript, Formulare, andere Card-Farben, Paket-Preiszeilen und Bullet-Farben bleiben erhalten. Keine neuen Overrides oder `!important`-Regeln.

Pruefung: lokale HTML-/CSS-Parser, JavaScript-Syntax, unveraenderte Formular-/Linkvertraege, Hintergrundzustaende, bestehende Regressionstests und `git diff --check` erfolgreich.

Offen: FAQ-Kuerzung wartet auf Klaerung, ob Hauptueberschrift oder einzelne Fragen gemeint sind. Keine gerenderte Desktop-/Mobile-Pruefung wegen weiterhin blockiertem Browserzugriff. Kein Push oder Deployment.

## 2026-10-13 - Automationspakete: goldene Bullet-Titel und Preiszeilen

Status: fertig

- `homepage/index.html`, `.nv-pack__features li`: die zwölf alleinstehenden Funktions-/Bullet-Titel ohne Beschreibung verwenden gemäß Screenshot-Auftrag Gold `#FAE385` statt Off-White. Grüne 3D-Punkte unverändert.
- `.nv-pack__price b` und `.nv-pack__price span`: beide direkt in den vorhandenen Regeln auf `grid-row: 1` gesetzt. Die bereits festgelegten Spalten 2 für den Betrag und 1 für die Bezeichnung sowie `align-items: baseline` bleiben erhalten. Der zuerst im DOM stehende Betrag kann die anschließend platzierte Bezeichnung damit nicht mehr in eine zweite automatische Grid-Zeile verschieben.
- Alle sechs vorhandenen Preis-/Bezeichnungspaare der drei Paket-Cards erfasst. Wortlaut, Beträge, Farben der Preise und ihrer Bezeichnungen, Fonts, Abstände, CTA, Assets, IDs, Formulare, JavaScript und Detailseiten unverändert. Keine neuen Selektoren, Override-Blöcke oder `!important`-Regeln.

Prüfung: lokale HTML-/CSS-Parser, unveränderte sechs Preis-/Bezeichnungspaare, gleiche explizite Grid-Zeile bei getrennten Spalten und Baseline-Ausrichtung, Goldton der zwölf Paket-Bullets, grüne Marker, bestehende Regressionstests sowie `git diff --check` erfolgreich.

Offen: keine erneute gerenderte Desktop-/Mobile-Prüfung wegen weiterhin blockiertem Browserzugriff. Kein Push oder Deployment ausgeführt.

## 2026-10-13 - Homepage: FAQ-Breite und Bullet-/Preisfarben korrigiert

Status: fertig

- `homepage/index.html`: `.nv-resource-section__inner` wieder auf dieselbe maximale Inhaltsbreite `1560px` wie die übrigen Homepage-Sektionen gesetzt. Die zuvor von Codex entfernte Breitenbegrenzung war nicht die beauftragte Korrektur. Kompakte FAQ-Abstände, natürliche Inhaltshöhe ohne Viewport-Mindesthöhe und bestehende Mobile-Regeln bleiben erhalten.
- `.nv-about__bullets`, `.nv-s7-card__uses li`, `.nv-s7-card__points li`, `.nv-analyse__offer-list li`, `.nv-ainfo li` und `.nv-checklist-result__insights li`: Bullet-Text auf den vorhandenen Off-White-Token `--color-text-light` / `#F5F7F4` gesetzt. `.nv-pack__features li` verwendet bereits diesen Wert und bleibt unverändert.
- Gemäß anschließendem Screenshot-Auftrag die beiden vorhandenen Goldtöne getauscht: `.nv-about__bullets strong`, `.nv-analyse__offer-list strong` und `.nv-ainfo li strong` verwenden jetzt `#FAE385`, zuvor der Ton von Einführungspreis und Listenpreis.
- `.nv-analyse__offer-price` verwendet jetzt `#D4AF37`, zuvor der Ton der Bullet-Titel. Dies gilt sowohl für `199 € · für Sie kostenlos` als auch für die vorhandenen Namen `Einführungspreis` / `Listenpreis` und ihre Werte `555 € netto` / `699 € netto`. Wortlaut, Beträge, Preisbedingungen und Ausrichtung unverändert.
- Grüne Marker aus `assets/Bulletpoint.png`, Hintergrund `#010603`, Card-Farben, Footer, Typografie, Detailseiten, Formularverträge, zwölf Script-Blöcke und alle IDs unverändert. Keine neuen Selektoren, Override-Blöcke, Blur-/Glow-Effekte oder `!important`-Regeln.

Prüfung: lokale HTML-/CSS-Parser, JavaScript-Syntax und JSON-LD, 60 unveränderte eindeutige IDs, unveränderte Formular- und Linkverträge, Vergleich der FAQ-Breite mit Analyse-/Leistungssektion, kompakte FAQ-Höhen-/Abstandsregeln, grüne Marker, Off-White-Bullet-Text, Goldton-Zuordnung für Titel und Preise sowie `git diff --check` erfolgreich.

Offen: Ergebnis nicht erneut im Browser gerendert geprüft; Browserzugriff weiterhin durch das Werkzeug blockiert. Kein Push oder Deployment durchgeführt.

## 2026-10-13 - Homepage: dunkleres Green, kompakte FAQ und gemeinsame Footer-Zeile

Status: fertig

- Screenshot-Prüfung: die beiden gemessenen FAQ-Hintergrundpixel zeigen `rgb(5, 20, 10)` / `#05140A`. Der Nutzer bestätigt, dass dieser Ton zu hell ist, und gibt anschließend das bereits auf der Homepage vorhandene, deutlich dunklere Green `#010603` frei.
- `homepage/index.html`: die vorhandene seitenlokale Definition `--color-deep-green` auf `#010603` geändert. Damit verwenden Homepage-Hero und alle zehn Inhaltssektionen den neu freigegebenen Ton. Die gemeinsame Token-Datei und Detailseiten-Farbwerte bleiben unverändert; kein zusätzlicher Override-Block.
- FAQ `.nv-resource-section`: Viewport-Mindesthöhe entfernt, Inhalt oben ausgerichtet, vertikales Padding von 83,2/105 px auf beidseitig 32 px reduziert. `.nv-resource-section__inner` nutzt die verfügbare Inhaltsbreite statt zusätzlicher Begrenzung auf 1560 px.
- `.nv-resource-section__head`: Abstand zur Fragenliste von 92,8 auf 20 px reduziert. Titel- und Subline-Abstände auf je 12 px reduziert. Die doppelten Titel-/Intro-Definitionen in diesem FAQ-Regelbereich konsolidiert; wirksame Typografie erhalten.
- `.nv-faq-layout` und `.nv-faq-grid`: Desktop-Spaltengap 16 px. `.nv-faq-col`: Zeilenabstand 8 px statt 24 px. `.nv-faq-item summary`: Desktop-Padding 4/8 px und Mindesthöhe 36 px statt 8/10 px und 44 px; Antworten mit 8/8/12 px Innenabstand. Fragen und Antworten unverändert.
- Mobile FAQ: 8 px Listengap, volle Spaltenbreite, 6/8 px Buttonpadding bei weiterhin mindestens 44 px Höhe. FAQ aus der allgemeinen mobilen 56-px-Sektions- und 32-px-Headerabstandsregel herausgenommen, damit die kompakte FAQ-Basis auch mobil wirksam bleibt.
- `homepage/shared-header-footer.css`: `.footer-bottom` hat auf Desktop zwei Spalten. `.footer-top` belegt Zeile 1, rechts; `.footer-legal` und `.footer-copy` teilen sich Zeile 2 am unteren Footer-Rand. Auf schmalen Viewports bis 900 px dürfen die Rechtstexte umbrechen und das Copyright folgt in einer eigenen Zeile, ohne horizontalen Überlauf.
- Keine Änderungen an Texten, Fonts, IDs, Formularen, JavaScript, Assets, Detailseiten oder Deploy-Konfigurationen. Keine neue Blur-/Glow-Wirkung und keine neuen `!important`-Regeln.

Prüfung: lokale HTML-/CSS-Parser, JavaScript-Syntax und JSON-LD, 60 unveränderte eindeutige IDs, zwölf unveränderte Script-Blöcke, Formular- und Linkverträge, Farbtokens, FAQ-Desktop-/Mobile-Regeln, gemeinsame Desktop-Footer-Zeile, Reduced-Motion-Regeln und `git diff --check` erfolgreich.

Offen: keine neue gerenderte Desktop-/Mobile-Browserprüfung, da das Browserwerkzeug den Zugriff weiterhin blockiert. Der Screenshot belegt den Ausgangszustand, nicht das Ergebnis dieser Änderungen. Kein Push oder Deployment ausgeführt.

## 2026-10-13 - Homepage: Blur-Korrektur und fehlende Card-Grundfarbe

Status: in Arbeit

- `homepage/index.html`: die von Codex erneut eingeführten weichen 8-/21-px-Schatten aus `--gold-glow` entfernt. Der vorherige scharfe 0-px-Lichtkanteneffekt und die separate `nv-gold-shine`-Titelanimation bleiben erhalten.
- Die zusätzlich eingeführten statischen Filter auf `.nvp4-projectidea__idea h3` und `.nv-process__step h3` entfernt.
- `.nv-seo-promo.is-visible`: den hinzugefügten verschwommenen Goldglow einschließlich `nv-seo-promo-glow`-Keyframes und überflüssiger Reduced-Motion-Animationsregel entfernt. Einflug, Fade-in und bestehender Scroll-Observer bleiben erhalten.
- `.nv-s7-card`: die bislang transparente Grundfläche direkt in der vorhandenen Basisregel auf `var(--color-gunmetal-dark)` geändert. Die identische Hintergrunddeklaration aus der vorhandenen Hover-/Focus-/Aktiv-Regel entfernt. Damit verwenden auch inaktive Desktop-Cards und die mobile Card-Grundfläche Dark Gunmetal `#15191A`.
- Hintergrundprüfung: alle zehn Homepage-Inhaltssektionen verwenden bereits `--color-deep-green`; sowohl die Homepage-Definition als auch der eingebundene Runtime-Token sind `#05140A`. Diese bereits freigegebenen Werte nicht erneut oder abweichend verändert. Paket-, Analyse-, Kontakt-, Download- und Checklisten-Cards verwenden den vorhandenen Gunmetal-Token. Ausdrücklich grüne und goldene Flächen unverändert.
- Keine neuen CSS-Selektoren, Override-Blöcke oder `!important`-Regeln. Keine Texte, IDs, Assetpfade, zwölf Script-Blöcke, Formularverträge, Detailseiten oder Deploy-Konfigurationen geändert.

Prüfung: offline HTML-/CSS-Parser, JavaScript-Syntax, JSON-LD, unveränderte IDs/Formulare/Links, Oberflächen-Token, alle sieben Bullet-Marker-Regeln, FAQ-Regeln, Footer-Reihenfolge, Calendly-Zuordnung, Reduced-Motion-Regeln und `git diff --check` erfolgreich. Die deklarierte Grundfarbe aller elf Service-Cards geprüft, nicht deren Live-Darstellung.

Offen: Der vorherige Eintrag ist kein Nachweis, dass alle GitHub-Issues visuell gelöst sind. Der Nutzer meldet weiterhin falsche Live-Hintergrund-/Card-Farben. Live-Browserzugriff bleibt trotz Nutzerfreigabe durch die Werkzeugrichtlinie blockiert. Screenshot des tatsächlich falschen Zustands angefordert; Ursache dieses verbleibenden Darstellungsunterschieds noch nicht nachgewiesen. Keine erneute Live-Prüfung, kein Push und kein Deployment durchgeführt.

## 2026-10-13 - Homepage: GitHub-Issues 56, 57, 58 und 74 bis 78

Status: fertig

- `homepage/index.html`, Issue 57: `--color-deep-green` nach ausdrücklicher Nutzerfreigabe von `#0A1913` auf `#05140A` geändert. Die Pflichtdokumente wurden nicht geändert; die aktuelle Nutzerfreigabe hat Vorrang vor dem dortigen Farbwert.
- Issue 77 und Nutzerkorrektur zu allen Homepage-Bulletpoints: `.nv-about__bullets strong::before`, `.nv-s7-card__uses li::before`, `.nv-s7-card__points li::before`, `.nv-pack__features li::before`, `.nv-analyse__offer-list li::before`, `.nv-ainfo li::before` und `.nv-checklist-result__insights li::before` verwenden das vorhandene Asset `assets/Bulletpoint.png` mit 9 px. Falsche Kleinschreibung in den mobilen Analyse-Regeln korrigiert. Nummerierte Abläufe bleiben unverändert.
- Issues 74 und 77: `.nv-analyse__offer--deep` erbt jetzt wie die kostenlose Analyse das vorhandene Dark Gunmetal `#15191A`. Die Paket-Cards nutzen bereits diesen Token. Auch `.nv-checklist-modal` und `.nv-checklist-modal__result` verwenden ihn jetzt. Grüne und goldene Flächen bleiben erhalten.
- Issue 56: `.nv-analyse__offer-list li` und `strong` sowie `.nv-ainfo li` auf vorhandenes Gold `#d4af37` umgestellt. Die laufende Rahmenanimation von `.nv-ametrics > div` und `.nv-aform__row` entfernt; statischer Rahmenschein bleibt erhalten.
- Nutzerkorrektur zum Titelglow: vorhandenen mehrteiligen `--gold-glow` der Detailseiten auf der Homepage wiederverwendet. Die vorhandene Titelanimation umfasst jetzt zusätzlich `.nv-pack__title`, `.downloads-section .section-title`, `.nv-step-card h3`, `.nv-s7-card__heading h3`, `.nv-s7-card__uses .nv-s7-card__uses-title`, `.nv-acard__title`, `.nv-analyse__offer h3`, `.nv-aform > h3`, `.nv-contact__portrait h3`, `.nv-contact__card h3`, `.download-item h3` und `.nv-checklist-modal__head h3`. Alle erhalten eine Reduced-Motion-Ausnahme. `.nvp4-projectidea__idea h3` und `.nv-process__step h3` erhalten statischen Titelglow.
- Mobile Titel: die vorhandenen Regeln für `h1`, `h2`, `h3`, `.hero-title-l1` und `.hero-subtitle-l1` erlauben mit `overflow-wrap: break-word` den Umbruch überlanger Wörter. Texte und Schriftgrößen bleiben unverändert.
- Issue 76: `.nv-faq-layout` nutzt die volle bestehende Inhaltsbreite ohne zusätzliche Zentrierung; `.nv-faq-item summary` hat 8/10 px Innenabstand, mindestens 44 px Höhe und wächst bei mehrzeiligen Fragen mit.
- Issue 75: in allen drei `.nv-seo-promo`-Elementen ausschließlich die beauftragten Texte `SEO TOOLBOX`, `Kostenloser SEO-Check` und `Kostenlosen SEO-Check öffnen und die SEO Toolbox ansehen.` sowie ihre Card-Hülle entfernt. Der vorhandene CTA `SEO Toolbox öffnen` mit Link `detail_seo.html` bleibt. Der bestehende Scroll-Observer bleibt unverändert; der Einflug verwendet -160 px auf Desktop und -40 px mobil sowie einen kurzen Goldglow. Die mobile Offset-Variable überschreibt die Reduced-Motion-Transformation nicht mehr.
- Issue 78: fünf Calendly-SVGs aus den Analyse-CTAs in Header, Hero, Projektstart, Projektidee und Prozess entfernt. Vier Calendly-SVGs an Termin-Links unverändert erhalten.
- `homepage/shared-header-footer.css`, Issue 58: `.footer-bottom`, `.footer-top`, `.footer-legal` und `.footer-copy` ordnen Pfeil, Rechtslinks und Copyright untereinander an; der untere Footer-Innenabstand beträgt 16 statt 43,2 px. Die Homepage-DOM-Reihenfolge entspricht dieser Darstellung. `.footer-newsletter__btn` verwendet für Hover und Tastaturfokus den vorhandenen goldenen Farb-, Hintergrund-, Lift- und Schatteneffekt.
- Unverändert: alle zwölf Script-Blöcke, 60 eindeutige IDs, Formularfelder und Attribute, Consent und Honeypot, CTA-Ziele, Downloads, Assets selbst, nummerierte Schritte und Detailseiten-Dateien. Die gemeinsame Footer-CSS wirkt auch auf andere Seiten, die sie bereits einbinden.

Prüfung: HTML-Parser ohne Fehler, CSS-Parser, JavaScript-Syntax und JSON-LD, unveränderte Formularverträge, Titel- und Reduced-Motion-Regeln sowie `git diff --check` erfolgreich. Im lokalen Browser bei 1440 x 900 px Paket-Cards, FAQ-Auf-/Zuklappen, Analyse-Cards, Pflichtfeldvalidierung, Rechner-Stundensatz und Footer-Reihenfolge geprüft. Alle zehn Inhaltssektionen haben `rgb(5, 20, 10)`; alle 93 vorhandenen gewöhnlichen Listenmarker referenzieren das korrekte Asset. Alle elf Haupt-/Sektionsüberschriften haben Glow und Titelanimation. Keine Seitenfehler in der Konsole, nur die Electron-CSP-Warnung der Browserumgebung.

Offen bei der Prüfung: 390 x 844 px als mobile Erstansicht geprüft; die dort erkannten abgeschnittenen Titel korrigiert. Die abschließende mobile Browserprüfung wurde anschließend durch die URL-Sicherheitsrichtlinie des Browserwerkzeugs blockiert. Der Newsletter-Hover ist als CSS-Regel geprüft, seine tatsächliche Zeiger-/Fokusdarstellung konnte in dieser Browserumgebung nicht bestätigt werden. Reduced Motion wurde statisch geprüft, nicht als Betriebssystemeinstellung emuliert. Kein Live-Formularversand und kein Deployment durchgeführt; GitHub-Issues bleiben offen.

## 2026-10-12 – Analyse: FAQ, Bulletpoints, Hero-Asset und Titelanimation

Status: in Arbeit

- `homepage/analyse.html`: doppelte CSS-Definitionen der Ergebnis-Karte entfernt; ihre Bullet-Texte auf vorhandenen Goldverlauf umgestellt.
- FAQ-Grid von 1300 auf maximal 1000 px reduziert, Abstände von 36 auf 16/20 px, FAQ-Summary-Höhen auf kompakte Mindesthöhe 44 px mit 8/14 px Innenabstand angepasst; FAQ aus der Desktop-Viewport-Mindesthöhenregel ausgenommen.
- Doppelte Hintergrund-Animationsregeln und die Ganzkarten-Animation entfernt; Shine-Animation nur auf Titel `.result-strip h3` und `.form-panel h3` belassen.
- Hero-Bildverweis auf `assets/detail_pages_grafics/sockel_loaded_analyse.png` umgestellt und fünf Bulletpunkt-Verweise auf `assets/Bulletpoint.png` korrigiert; Marker auf 10 px ohne überlagerte Kontur gesetzt.
- Formularfunktion und übrige Hero-Geometrie nicht geändert.

Blockiert: Die beiden Assets liegen laut lokalem `git status` in der Staging-Area, sind aber noch nicht committed und gepusht. Vor dem Merge müssen sie unter den oben dokumentierten, exakt geschriebenen Pfaden in `main` vorhanden sein.

## 2026-10-12 – Analyse-Divider vereinheitlicht und doppelte Linien entfernt

Status: in Arbeit

- `homepage/analyse.html`: vorhandene `.section-divider`-Basisregel auf den bestehenden, 2 px starken Goldverlauf und Glow der vorherigen Sektions-Pseudolinien umgestellt.
- Alte Regel `main > section:nth-child(n+4):before` entfernt. Sie erzeugte an nachfolgenden Sektionen zusätzliche Linien oberhalb des bereits vorhandenen Dividers.
- Alle sechs vorhandenen `section-divider`-Elemente bleiben unverändert. Hero und Folgesektionen nutzen jetzt dieselbe Einzelregel; keine neuen Overrides.
- Goldwinkel, Partikelhintergrund, Texte, CTA, Grafik und übrige Abschnitte unverändert.

Offen: Visuelle Browserprüfung nach Bereitstellung.

## 2026-10-12 – Hero-Divider identisch zu den folgenden Abschnittstrennern

Status: in Arbeit

- `homepage/analyse.html`: gesondertes `hero-bottom-divider`-Element innerhalb des Hero-Viewports samt zugehöriger CSS-Regel vollständig entfernt.
- Nach dem schließenden Hero-Viewport exakt dasselbe `<div class="section-divider" aria-hidden="true"></div>` eingefügt, das bereits zwischen den folgenden Sektionen verwendet wird.
- Bestehende `.section-divider`-CSS-Regel unverändert übernommen. Kein Override hinzugefügt.
- Goldwinkel, Hero-Texte, CTA, Grafik, WebGL-Partikelhintergrund sowie übrige Abschnittstrenner unverändert.

Offen: Visuelle Kontrolle nach Bereitstellung, noch kein Merge.

## 2026-10-12 – Analyse-Goldwinkel: rechte Knickpunkte getrennt

Status: in Arbeit

- In `homepage/analyse.html` ausschließlich die rechten Knickpunkte der SVG-Winkel 2–5 angepasst: x=545, 530, 515, 500 statt gemeinsam x=560.
- Der erste Winkel bleibt bei x=560 unverändert. Die linke Staffelung (x=110/130/150/170/190), obere Positionen (y=0/15/30/45/60) und unteren Enden (y=450/430/410/390/370) bleiben unverändert.
- Divider, Textabstände, CTA, Grafik, Partikelhintergrund, Farben und alle weiteren Bereiche unverändert.

Offen: Visuelle Kontrolle und Freigabe vor Merge.

## 2026-10-12 – Analyse-Goldwinkel gemäß bestätigter 20-px-Geometrie

Status: in Arbeit

- `homepage/analyse.html`: nur die fünf SVG-Pfade im oberen rechten Hero geändert.
- Erster Winkel bleibt `M110 0 H560 V450`; Winkel 2–5 beginnen links bei x=130/150/170/190 und enden unten bei y=430/410/390/370, mit bestehender 15-px-Höhenstaffelung.
- Rechter Eckpunkt aller Winkel bleibt bei x=560. Keine Änderungen an Divider, Hero-Inhalt, Glow, Partikelhintergrund, SVG-Farben oder CSS.

Offen: Visuelle Kontrolle vor Merge.

## 2026-10-12 – Goldwinkel-Abstand auf 15 px verdichtet

Status: in Arbeit

- In `homepage/analyse.html` alle fünf SVG-Winkel mit 15 px Vertikal- und Horizontalversatz angeordnet, statt der auseinandergezogenen Staffelung.
- Schenkellängen pro Winkel bleiben identisch: 450/435/420/405/390 px; größter Winkel weiterhin 450 px.
- Index-Hero-Divider und alle übrigen Elemente unverändert.

Offen: Visuelle Freigabe vor Merge.

## 2026-10-12 – Gleichschenklige Goldwinkel und Index-Hero-Divider korrigiert

Status: in Arbeit

- Fünf goldene SVG-Winkel: pro Winkel sind horizontaler und vertikaler Schenkel exakt gleich lang (450/390/330/270/210 px).
- Sichtbar getrennte Endpunkte der Winkel durch abgestufte Längen; bisherige falsche SVG-Pfade ersetzt.
- Hero-Divider exakt mit der `index.html`-Technik direkt an der Unterkante des Hero-Viewports platziert: links/rechts 7 %, Höhe 0,8 px, auslaufender Goldverlauf und Schatten.
- Den zwischen Hero und nächster Sektion eingefügten separaten Divider entfernt, damit an dieser Grenze nur eine Linie gezeichnet wird.
- Andere Sektionen, Partikelshader, Texte, Grafik, CTA und Textabstände unverändert.

Offen: Visuelle Kontrolle vor Merge.

## 2026-10-12 – Analyse-Hero: Goldwinkel als echte SVG-Linien, Divider wiederhergestellt

Status: in Arbeit

- `homepage/analyse.html`: die zehn überlagerten CSS-Background-Linien des oberen rechten Hero-Winkels vollständig entfernt und durch fünf einzeln definierte SVG-Pfade mit getrennten Endpunkten (450/420/390/360/330 px horizontal; 370/312/254/196/138 px vertikal) ersetzt.
- Die ursprüngliche `.hero-viewport::before`-Regel ersetzt, keine zusätzliche CSS-Override-Schicht ergänzt.
- Genau ein `section-divider`-Element direkt zwischen Hero-Viewport und nächster Sektion wieder eingesetzt, bestehende Index-Goldverlaufsregel wiederverwendet.
- Das visuelle Ergebnis als auf dem bestehenden Screenshot montierte SVG-/Divider-Vorschau bereitgestellt; dies ist keine vollständige Browserprüfung der produktiven Seite.

Offen: Browser-Abnahme und Freigabe vor Merge.

## 2026-10-12 – Analyse-Hero vertikale Goldschenkel und Divider korrigiert

Status: in Arbeit

- Fünf horizontale Goldlinien wieder mit abgestuften Längen 450/420/390/360/330 px statt einheitlichen 450 px hergestellt.
- Nur die vertikalen Goldschenkel von 205/190/175/160/145 px auf 300/285/270/255/240 px verlängert.
- Abschnitts-Divider auf den gleichen auslaufenden Goldverlauf mit schwachem Glow wie die Trennlinien in `index.html` umgestellt; keine zusätzlichen Divider-Elemente eingefügt.
- Andere Hero-Elemente, Textabstände und Seiten bleiben unverändert.

Offen: Visuelle Browserabnahme; doppelt wahrgenommene Linien auf der Website noch nicht visuell verifiziert.

## 2026-10-12 – Analyse-Hero CSS-Overrides konsolidiert

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: die nachträglich eingefügten redundanten `#hero .detail-hero .sub`- und `.actions`-Overrides entfernt; Abstände in vorhandenen `.detail-hero`-Basisregeln zusammengeführt.
- Doppelte Hero-Hintergrund-/Positionierungsregeln und identische Mobile-Hero-Padding-Wiederholungen entfernt; wirksame Werte in den ursprünglichen Regeln belassen.
- Alle fünf horizontalen Goldwinkel auf 450 px Schenkellänge gebracht, Versatz der Endpunkte beibehalten.
- Subline-Abstand im ursprünglichen CSS auf 52 px, CTA-Abstand auf 70 px gesetzt.
- Zusätzlichen Abschnitts-Divider direkt nach dem Hero entfernt (andere Abschnittstrenner unverändert).

Nicht geändert:

- HTML-Inhalte, Partikelshader, Goldlinien-Geometrie, Glow, Hero-Grafik, andere Abschnitte und andere Seiten.

Offen:

- Browserprüfung nach Deployment; keine generelle Löschung globaler bzw. funktionsnotwendiger Media-Query-Regeln vorgenommen.

## 2026-10-12 – Analyse-Hero: Index-Partikelhintergrund, Winkel und Abstände

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: den bestehenden WebGL-Partikelshader aus `homepage/index.html` unverändert übernommen und auf den Hero-Viewport als Canvas-Ziel ausgerichtet; Canvas hinter dem Hero-Inhalt platziert.
- Den deckenden schwarzen Hero-Sektionshintergrund innerhalb des Viewports transparent gesetzt und einen dezenten dunklen Verlaufs-Overlay zur Lesbarkeit eingefügt.
- Fünf versetzte Goldwinkel: horizontale Schenkel 450, 420, 390, 360, 330 px; vertikale Schenkel 205, 190, 175, 160, 145 px.
- Abstand Subline–Bodytext: 38 px; Abstand Bodytext–CTA: 52 px.
- Bestehenden Emerald-/Gunmetal-Glow direkt hinter der Prozessgrafik sichtbar verstärkt und Bild über der Glow-Ebene positioniert; keine neue Card und kein Rahmen.

Nicht geändert:

- Hero-Texte, CTA-Beschriftung, Hero-Grafik, Leistungsbereich, Formulare und andere Seiten.

Offen:

- Visuelle Browserprüfung des Shader-Hintergrunds, der Staffelung sowie Desktop-/Mobilabstände.

## 2026-10-12 – Analyse-Hero mittig und Goldwinkel länger versetzt

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: die fünf oberen rechten Goldwinkel gegeneinander versetzt und die horizontale Maximallänge auf 450 px gesetzt (weitere Längen 375, 300, 225 und 150 px); vertikale Längen auf 205, 165, 125, 85 und 45 px gestaffelt.
- `homepage/analyse.html`: die bestehende Desktop-Verschiebung `translateY(-80px)` des Hero-Grid entfernt. Die vorhandene vertikale Zentrierung des Hero-Containers bleibt maßgeblich.

Nicht geändert:

- Hero-Grafik, deren Skalierung, Texte, CTA, Leistungsicons, Formular, Header, Footer und andere Seiten.

Offen:

- Visuelle Browserabnahme bei Desktop-Breakpoints und unterschiedlicher Viewporthöhe.

## 2026-10-12 – Issue #55 Hero-Keile und Goldlinien auf analyse.html angepasst

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: beide unteren Hero-Keile samt HTML-Elementen und zugehörigen CSS-Regeln entfernt.
- Gestaffelte Goldlinien oben rechts von `right:clamp(20px,3vw,46px)` auf `right:0` gesetzt.
- Horizontale und vertikale Linienlängen von 100/88/76/64/52 % auf 100/78/57/36/15 % stärker gestaffelt.

Nicht geändert:

- Hero-Bild, übrige Hero-Geometrie, Texte, sieben Leistungsicons, Formulare, Header, Footer, andere Seiten.

Offen:

- Visuelle Browserabnahme der Linienposition und Staffelung.

## 2026-10-12 – Analyse-Leistungsicons auf Originalgröße mit Goldrahmen korrigiert

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: alle sieben Einzelmodule in den bisherigen 45 × 45 px großen Goldverlaufsrahmen eingefügt.
- Modulbilder innerhalb der Rahmen auf 34 × 34 px begrenzt; Einrückung der Texte auf die ursprünglichen 74 px zurückgesetzt.
- Die bestehende Goldrahmen-Optik (10 px Radius, 1,5 px Verlaufskante) wiederhergestellt.

Nicht geändert:

- Einzelmoduldateien, Hero, Leistungsinhalte und Reihenfolge, Keile, Linien, andere Seiten.

Offen:

- Visuelle Abnahme im Browser nach Deployment.

## 2026-10-11 – Issue #55 Original-Module statt Hero-Sprite

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: die fehlerhafte CSS-Sprite-Verwendung des gesamten Hero-Bildes in der Leistungssektion entfernt.
- Die sieben Leistungspunkte verwenden nun jeweils ein einzelnes bereits vorhandenes Modul-Asset aus `assets/Module/` als echtes `img`-Element.
- Verwendete Originaldateien: `analyse/1.png`, `datenanalyse.webp`, `analyse/2.webp`, `Ablauf/umsetzung_struturieren.png`, `analyse/3.png`, `report.webp`, `analyse/4.png`.
- Keine neuen Bildassets erstellt.

Nicht geändert:

- Hero-Bild, die sieben bereits abgestimmten Leistungstexte, Randformen und Linien, andere Seiten.

Offen:

- Visuelle Browserabnahme der Desktop- und Mobile-Darstellung vor Merge.

## 2026-10-11 – Issue #55 Leistungssektion auf sieben Hero-Icons umgestellt

Status: in Arbeit

Geändert:

- `homepage/analyse.html`: die acht nummerierten Leistungspunkte auf sieben Punkte reduziert.
- Die Nummernrahmen der Leistungssektion entfernt; stattdessen werden ausschließlich die sieben Motive aus dem bestehenden Hero-Asset `assets/detail_pages_grafics/Analyse_detail _final.png` als CSS-Sprite verwendet.
- Reihenfolge und Zuordnung: Prozesserfassung, Datenprüfung, Systemanalyse, Anwendungsfallentwicklung, Potenzialbewertung, Nutzen & Priorisierung, Aufgabenklassifikation.
- `Nutzenbewertung` und `Risikobewertung` in `Potenzialbewertung` zusammengeführt; `Priorisierung` als `Nutzen & Priorisierung` konkretisiert.
- Bestehende Beschreibungen wurden nur soweit zusammengeführt, wie es für die 7er-Struktur erforderlich ist.

Nicht geändert:

- Hero-Visual selbst.
- Keile/Randformen und gestaffelte Linien.
- Formular-, Analyse-, Download-, FAQ-, Header- und Footer-Logik.
- Andere Seiten und Assets.

Offen:

- Visuelle Abnahme der sieben Sprite-Ausschnitte auf Desktop und Mobile.

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

## 2026-10-13 - Homepage-Cards: statische 3D-Holo-Optik

Status: in Arbeit

- `homepage/index.html`: den vorhandenen Card-Regeln eine leichte, statische 3D-Neigung mit unterschiedlichen Ausrichtungen je Bereich und Card-Position hinzugefügt. Betroffen sind `.nv-about__media`, `.nv-about__mini > div`, `.nv-step-card`, `.nvp4-projectidea__image`, `.nv-pack__card`, `.nv-analyse__offer`, `.nv-acard` einschliesslich Formular-Card, `.nv-contact__portrait`, `.nv-contact__card` und `.download-item`.
- Vorhandene Gold-/Schwarz-Tokens erzeugen eine scharfkantige, versetzte Materialkante ohne neue Farben oder Glow-/Blur-Regeln. Bestehende Hover-/Focus-Zustaende richten die Karten plan aus. Auf Mobile bleiben die Karten ohne Hover leicht geneigt sichtbar; Projektstart-Karten nutzen dort eine noch kleinere Neigung.
- Die zuvor weiche Rahmenschattierung der betroffenen Info- und Tiefenanalyse-Cards wurde durch die scharfe Kante ersetzt. Keine dauerhafte Kartenbewegung oder Mausverfolgung; vorhandene Card-Inhalte, Bilder, Links, IDs, Formularverhalten und Layout-Raster bleiben erhalten.
- Abschnitt 5 `.nv-s7-card` bleibt unverändert. FAQ-Frage-CTAs, die SEO-Promo und Ablauf-Module sind Controls bzw. bestehende 3D-Module und keine Card-Komponenten dieser Umsetzung.

Offen: gerenderter Desktop-/Mobile-Check durch den Nutzer steht aus. Keine Browseransicht, Tests, Push oder Deployment in diesem Schritt.

## 2026-10-13 - Abschnitt 5: Mobile-Leistungskarten kompakter

Status: in Arbeit

- `homepage/index.html`: Im bestehenden Mobile-Layout von `.nv-s7__cards` den Kartenabstand von 20 px auf 24 px erhöht und die Bannerhöhe von `.nv-s7-card__visual` von 96 px auf 56 px reduziert.
- Desktopdarstellung, Kartentexte, Bilder, Links, CTAs und JavaScript unverändert.

Offen: gerenderte Mobile-Ansicht durch den Nutzer pruefen lassen. Kein Browser- oder Geraete-Rendering in diesem Schritt.

## 2026-10-13 - Abschnitt 5: Mobile-Kartenstruktur ausgerichtet

Status: in Arbeit

- `homepage/index.html`: Im bestehenden Mobile-Regelbereich von `.nv-s7-card__number` die Nummernplakette von 41,6 x 43,2 px auf 34 x 36 px und die Ziffer von 20 px auf 16 px verkleinert. Den Abstand zwischen Plakette und Titel auf 8 px reduziert.
- `.nv-s7-card__points` unter den Titeltext eingerueckt, statt am linken Rand des Karteninhalts zu beginnen.
- Desktop, Karteninhalte, Bildpfade, Links, CTAs und JavaScript unveraendert.

Offen: gerenderte Mobile-Ansicht pruefen lassen. Kein Browser- oder Geraete-Rendering in diesem Schritt.

## 2026-10-13 - FAQ-Fragen auf Textbreite begrenzt

Status: in Arbeit

- `homepage/index.html`: `.nv-faq-grid` verwendet auf Desktop zwei `max-content`-Spalten statt zwei dehnbaren `1fr`-Spalten. `.nv-faq-col` richtet sich ebenfalls nach dem laengsten Fragetext der jeweiligen Spalte.
- Bis 1100 px steht der Fragenblock einspaltig mit maximal 560 px Breite; die bestehende Mobile-Regel bis 640 px behält volle Viewport-Breite. Fragen, Antworten und FAQ-Interaktion unveraendert.

Offen: gerenderte Desktop- und Tablet-Breitenpruefung.

## 2026-10-13 - Bestehende 3D-Card-Oberflaeche auf Homepage-Cards

Status: in Arbeit

- `homepage/index.html`: Raster sowie dezente Gold- und Smaragd-Ebenen der vorhandenen `homepage/xcomponents/nurovelle-tilt-card.css` als `--nv-holo-face` und `--nv-holo-overlay` in die ausgelieferte Homepage-CSS uebernommen. Die Komponenten-Datei selbst wird vom Deploy ausgeschlossen und war in `index.html` nicht eingebunden.
- Die Oberflaeche liegt auf `.nv-about__mini > div`, `.nv-analyse__offer`, `.nv-acard` (auch Paket- und Formular-Cards), `.nv-contact__portrait`, `.nv-contact__card` und `.download-item`. Bildkarten `.nv-about__media`, `.nv-step-card` und `.nvp4-projectidea__image` verwenden die transparente Version ueber dem vorhandenen Bild. Die Video-Play-Steuerung bleibt darueber.
- Die bewegte Rahmen-Animation der Mini-Cards deaktiviert; vorhandene Neigung und Hover-Ausrichtung bleiben. Die scharfe Materialkante sitzt wie bei der vorhandenen Muster-Card diagonal versetzt. Abschnitt 5 `.nv-s7-card` sowie Card-Texte, Bilder, Links und JavaScript unveraendert.

Offen: gerenderte Desktop-, Mobile- und Reduced-Motion-Pruefung. Kein Push oder Deployment in diesem Schritt.

## 2026-10-13 - FAQ-Fragenblock zentriert

Status: in Arbeit

- `homepage/index.html`: `.nv-faq-grid` innerhalb des bestehenden FAQ-Layouts horizontal zentriert.
- FAQ-Titel, Subline, Beschreibung, Fragen, Antworten und Interaktion unveraendert.

Offen: gerenderte Desktop- und Mobile-Pruefung.

## 2026-10-13 - Download-Karten ohne Raster und Hintergrundstrich

Status: in Arbeit

- `homepage/index.html`: `.download-item` wieder mit der bestehenden glatten Gunmetal-Flaeche statt `--nv-holo-face` dargestellt. Versetzte Tiefenschatten an den Karten sowie die Trennlinie von `.download-display__header` entfernt.
- Bestehende Karteneigung, Goldrahmen, Inhalte, Assets und Download-/Checklist-Logik unveraendert.

Offen: gerenderte Desktop- und Mobile-Pruefung.

## 2026-10-13 - Download-Karten am Rand nicht mehr abgeschnitten

Status: in Arbeit

- `homepage/index.html`: `.download-display` verwendet den vorhandenen Abstandstoken `--space-4` statt der nicht definierten Variable `--nv-space-md`. `overflow: visible` laesst die geneigten Karten und ihre Kanten vollstaendig sichtbar.
- Download-Texte, Assets, Links, CTA- und Checklist-Logik unveraendert.

Offen: gerenderte Desktop- und Mobile-Pruefung.
