## 2026-10-22 - KI-Agenten-Vorschau fuer die visuelle Abnahme komprimiert

Status: geprüft

- Ausschliesslich `homepage/preview-detail_ki-agenten.html` neu erzeugt. `tools/detail_pages/build.py` erzeugt ohne Seitenauswahl jetzt nur diese Vorschau; Buero- und SEO-Vorschau bleiben unveraendert.
- `tools/detail_pages/ki_agenten.py` neu: verantwortliche, aus `analyse.html` kopierte CSS-Deklarationen direkt angepasst, keine zusaetzliche Override-Stylesheet-Schicht. `.section-inner` maximal 1000 px; `.detail-hero` mit flexiblen Desktop-Spalten ohne 780-/470-px-Mindestbreiten; `.visual-card--hero img` ohne feste Ueberbreite und ohne 1.6-/1.45-Skalierung. Originalgrafik vollstaendig sichtbar.
- `#hero h1` / `.hero-title-line`: vorhandener Titel bleibt wortgleich in zwei Zeilen, laeuft ueber die Bildspalte; Titelgroesse 28 bis 52 px. Bestehende Typografie numerisch komprimiert: Fliesstext 14 px, Subline 16 px, Abschnittstitel 26 bis 34 px. Keine neuen Schriften, Farben oder CTA-Varianten.
- `.media-split` / `.media-split--visual-left`: feste 580-px-Fotomindestbreiten durch flexible Spalten ersetzt. `.label-list li` und `.num-list li`: auch Beschreibungstexte erhalten vorhandene Goldfarbe. `.num-list`: kompaktere Abstaende, genau acht urspruengliche Module, keine zusaetzlichen Konzeption-/Umsetzungskarten.
- `.analysis-layout` flexibel; `.form-grid` wechselt bei kleinen Breiten auf eine Feldspalte. `.section` erhaelt Scrollabstand fuer den vorhandenen festen Header. Formular bleibt bei mehr Inhalt natuerlich hoeher als ein Viewport; es wird nicht abgeschnitten.
- `tools/detail_pages/reference.py`: nur fuer KI-Vorschau fehlenden Submit-Button `#nurovelle-analysis-submit` mit vorhandener `.hero-cta > .golden-button > .golden-text`-Komponente wiederhergestellt. Wortlaut aus vorhandenem Formulartitel: `Potenzialanalyse starten`. Unsichtbare Feldbeschriftungen aus bestehenden Platzhaltern/Optionen ergaenzt. Formularfelder, Pflicht-Consent, Newsletter, Honeypot, API-/Status-/Ergebnislogik bleiben erhalten.
- `tools/detail_pages/verify.py`: veraltete Gesamttext-/Altrasterpruefung durch konkrete Vergleiche der beauftragten acht Referenzsektionen, uebernommenen Texte, acht Module und acht unveraenderten FAQ ersetzt. Prueft ebenfalls Formularvergleich mit Referenz, exakte Originalscripts plus Referenz-API-/Canvas-Script, erhaltene Sprungziele, lokale Assets/Links, HTML5, CSS und JavaScript-Syntax. Gold-CTA- und FAQ-Materialregeln bleiben identisch zur Analyse; keine neuen `!important`-Regeln. `tools/detail_pages/README.md` auf den tatsaechlichen Einzelvorschau-Ablauf aktualisiert.

Geprueft: Generator und Verifier, Python-Syntax, `git diff --check`; Browser bei 960x600, 1280x720, 1440x900, 390x844 und 320x720 CSS-Pixeln. Kein Inhaltsueberlauf in geprueften Raster-/Text-/CTA-Komponenten; Hero-Titel zweizeilig, Grafik innerhalb der Inhaltsbreite, Hero-CTA im ersten Viewport. Modulbilder und Nutzenfoto laden. FAQ per Maus geoeffnet; unvollstaendiges Formular bleibt beim ersten Pflichtfeld, ohne API-Versand. Keine Seitenfehler in der Browserkonsole.

Nicht geaendert: `homepage/analyse.html`, Originaldetailseiten, `homepage/index.html`, `homepage/shared-header-footer.css`, `homepage/nurovelle-tokens.css`, andere Vorschauen und Assets. Bestehendes Navigations-/FAQ-JavaScript sowie API- und Canvas-Script nicht veraendert.

Offen: visuelle Nutzerfreigabe; echter API-Versand und Zahlung nicht getestet. Reduced-Motion-Regeln statisch geprueft, keine Laufzeit-Emulation verfuegbar. Tastatur-Aktivierung der nativen FAQ wurde durch die Browserautomatisierung nicht ausgeloest und ist daher nicht als erfolgreich getestet gewertet. Bestehende Social-Links des unveraenderten Footers zeigen weiterhin auf `index.html#`. Kein Deployment, keine Uebernahme auf weitere Seiten.

## 2026-10-21 - Freigegebene integrierte Eyecatcher-Positionen implementiert

Status: in Arbeit

- `homepage/index.html`: exakt freigegebene Einbindungen aus `seo-placement-preview.html` uebernommen: Warum Nurovelle neben Einleitung, Automationspakete neben Subline/Bodytext, Downloads tiefer zwischen Titel und Karten ueber letztem Drittel der Prompt-Guide-Spalte.
- Gunmetal-Motiv, Breite 240 px, Homepage-CTA, `rotateY(-18deg)`, 460-ms-Fade-in von links und Reduced-Motion-Regel aus Vorschau erhalten. Vorhandenen Observer unveraendert weiterverwendet.
- Vorschau-`noindex` nicht uebernommen. Alle bisherigen Texte, Formular-/Rechnerlogik, IDs, Scripts und sonstigen Assetreferenzen unveraendert; separate Vorschau erhalten.

Pruefung: HTML5-/CSS-Parser, Identitaet zur freigegebenen Vorschau ohne deren Robots-Metatag, erhaltene IDs/Scripts/Formular und `git diff --check` erfolgreich. Kein Deployment.

## 2026-10-21 - Seitliche Vorschauperspektive entgegengesetzt

Status: in Arbeit

- Nur `homepage/seo-placement-preview.html`: `.seo-placement__display` von `rotateY(18deg)` auf `rotateY(-18deg)` gesetzt. Alle drei Vorschau-Eyecatcher betroffen; Position, Groesse, Motiv, Texte und Einblendeffekt unveraendert. `homepage/index.html` unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-21 - Einblendeffekt fuer integrierte Vorschau-Eyecatcher

Status: in Arbeit

- Nur `homepage/seo-placement-preview.html`: drei `.seo-placement` an vorhandenen `data-seo-promo`-Observer angeschlossen. Beim Eintritt in den sichtbaren Bereich Fade-in mit 32-px-Bewegung von links, Dauer 460 ms. Reduced Motion zeigt die Elemente ohne Animation.
- Positionen, Groesse, innere Perspektive, Texte und Homepage unveraendert. Keine neue JavaScript-Logik.
- HTML5-/CSS-Pruefung und `git diff --check`; visuelle Abnahme offen.

## 2026-10-21 - Positionen in separater Homepage-Vorschau nachjustiert

Status: in Arbeit

- Nur `homepage/seo-placement-preview.html`: Downloads-Eyecatcher tiefer zwischen Titel und Karten sowie nach links ueber das letzte Drittel der Prompt-Guide-Spalte verschoben. Warum-Nurovelle-Eyecatcher um 80 px nach links und 32 px nach unten versetzt. Mobile Positionierungen bleiben im Inhaltsfluss.
- Automationspakete, Eyecatcher-Groesse, Motiv, Perspektive und `homepage/index.html` unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-21 - Separate Homepage-Vorschau integrierter Eyecatcher-Positionen

Status: in Arbeit

- `homepage/seo-placement-preview.html`: separate Homepage-Kopie mit drei kompakten Gunmetal-Eyecatchern innerhalb der vorhandenen Einleitungsbereiche: Warum Nurovelle neben Einleitung, Automationspakete neben Subline/Bodytext, Downloads unter Titel im rechten Bereich ueber Prompt Guide/Checkliste. Keine zusaetzlichen Zwischenbloecke.
- Freigegebenes Motiv und Perspektive erhalten, maximale Breite 240 px. Mobile Positionierung im jeweiligen Einleitungsbereich statt absolut.
- `homepage/index.html` unveraendert, per SHA-256 vor/nach Erstellung bestaetigt. Bestehende Texte, Bilder, Links, Formulare und Scripts in der Vorschau erhalten.
- HTML5-/CSS-Parser, drei Platzierungen und `git diff --check` erfolgreich. Visuelle Desktop-/Mobile-Abnahme offen.

## 2026-10-21 - SEO-Eyecatcher aus Homepage entfernt

Status: in Arbeit

- Alle drei `aside.nv-seo-promo` aus `homepage/index.html` auf Nutzerwunsch entfernt. Damit entfallen auch deren Inhalts- und Randabstaende im Seitenfluss.
- Separate Vorschau und Assets erhalten. Andere Sektionen, Texte, Formulare und JavaScript unveraendert.

Pruefung: HTML5-Parser, keine verbliebenen Eyecatcher-Elemente und `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-21 - Homepage-Eyecatcher deutlich verkleinert

Status: in Arbeit

- Nur Homepage-Eyecatcher: maximale Breite von 360 auf 240 px reduziert; Typografie und innere Abstaende proportional auf zwei Drittel angepasst. Alle drei Instanzen betroffen. Perspektive, Motiv, Position, CTA-Komponente, Texte und Linkziele unveraendert. Separate Vorschau unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-21 - Freigegebenen Gunmetal-Eyecatcher links eingebunden

Status: in Arbeit

- `homepage/index.html`: drei bestehende SEO-Hinweise auf freigegebenes Gunmetal-Display mit Lupe, HTML-Text und Homepage-CTA umgestellt. Maximal 360 px breit, links an der bestehenden Inhaltskante statt zentriert. Motiv, 18-Grad-Y-Perspektive, Texte und Text-/CTA-Position aus separater Vorschau uebernommen.
- `.nv-seo-promo__display` trennt feste Displayperspektive von der bisherigen Einblendanimation. Bandflaechen entfernt; `.nv-seo-promo__image` und lokale responsive CTA-Dimensionierung ergaenzt. Linkziel bleibt `detail_seo.html`.
- Analysebereich, Formulare, bestehende JavaScript-Logik und andere Assets unveraendert. Separate Vorschau erhalten.

Pruefung: HTML5-/CSS-Parser, drei Einbindungen und `git diff --check`; visuelle Abnahme im Seitenkontext offen. Kein Deployment.

## 2026-10-21 - Original-Homepage-CTA in separater Vorschau

Status: in Arbeit

- `homepage/seo-eyecatcher-preview.html`: vorhandene `nurovelle-tokens.css` und `shared-header-footer.css` eingebunden; eigenen Pillenbutton durch Homepage-Markup `.hero-cta`, `.golden-button`, `.golden-text` ersetzt. Material, Rahmen, Schatten, Grossschreibung und Hover-/Active-Zustaende aus bestehender Komponente. Nur kompakte Schriftgroesse und Mindestbreite lokal angepasst.
- Motiv, Perspektive, Textposition, Linkziel und `homepage/index.html` unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Gunmetal-Grundmaterial in separater Eyecatcher-Vorschau

Status: in Arbeit

- `homepage/assets/seo-check-preview-gunmetal.png`: Farbvariante mit dunklem Gunmetal-Grundmaterial, gruenen Schatten und goldenen Highlights erstellt; vorheriges Motiv erhalten.
- Nur Bildreferenz in `homepage/seo-eyecatcher-preview.html` aktualisiert. Freigegebene aufrechte Perspektive mit rechter Seite nach hinten, Groesse, Text und CTA unveraendert. Homepage nicht angepasst.
- `git diff --check` erfolgreich; visuelle Abnahme der Farbvariante offen.

## 2026-10-20 - Vorschau aufrecht, ausschliesslich rechte Seite nach hinten

Status: in Arbeit

- `homepage/seo-eyecatcher-preview.html`: bisherigen kombinierten Transform durch `perspective(900px) rotateY(18deg)` ersetzt. Keine X-/Z-Drehung und keine Scherung; nur rechte Seite nach hinten. Breite 360 px, Motiv, Text, CTA und Homepage unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-20 - Vorherige Perspektive bei kleiner Vorschaugroesse wiederhergestellt

Status: in Arbeit

- Nur Perspektivmatrix in `homepage/seo-eyecatcher-preview.html` auf den Stand vor der letzten Verkleinerung zurueckgesetzt. Breite bleibt 360 px; Motiv, Lupe, Texte, CTA und Homepage unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-20 - Kompaktere und weniger schraege separate Vorschau

Status: in Arbeit

- `homepage/seo-eyecatcher-preview.html`: maximale Breite von 420 auf 360 px reduziert. Projektive Verkuerzung und Scherung abgeschwaecht, sodass die obere linke Seite weniger nach hinten fluchtet. Textblock weiterhin ohne Innenpadding; vorhandene Motivvariante, Lupe, Text-/CTA-Position und Homepage unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-20 - Lupe in Vorschau weiter nach links

Status: in Arbeit

- Nur Bildreferenz der separaten Vorschau auf neue Variante `homepage/assets/seo-check-preview-loupe-left.png` umgestellt, mit weiter nach links versetzter Lupe. CSS-Perspektive, Groesse, Texte, CTA und Homepage unveraendert. Bisherige Bildvarianten erhalten. Visuelle Abnahme offen.

## 2026-10-20 - Lupe nach links unten und kleinere separate Vorschau

Status: in Arbeit

- Neue Vorschau-Bildvariante `homepage/assets/seo-check-preview-loupe-inset.png` mit nach links unten versetzter Lupe erzeugt; bisheriges Motiv erhalten.
- `homepage/seo-eyecatcher-preview.html`: Variante eingesetzt und maximale Gesamtbreite von 460 auf 420 px reduziert. Perspektivtransform und HTML-Text-/CTA-Position unveraendert. Homepage unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-20 - Linke Vorschauseite minimal abgesenkt

Status: in Arbeit

- Nur separate Vorschau: gemeinsame Drehung um -1 Grad ergaenzt, sodass die linke Seite minimal tiefer steht. Bestehende Perspektivmatrix, Motiv, Texte, CTA und Homepage unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Rueckneigung der Vorschau sichtbar reduziert

Status: in Arbeit

- Nur Transform der separaten Vorschau: vertikale Scherung von .153328203 auf .04 reduziert und vertikalen projektiven Term auf null gesetzt. Vorherige kaum sichtbare Zusatzrotation entfernt; seitliche Perspektivparameter erhalten. Motiv, Texte, CTA und Homepage unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Oberseite der separaten Vorschau leicht nach vorne

Status: in Arbeit

- Nur Perspektivtransform der separaten Vorschau um 4 Grad Vorwaertsneigung der Oberkante ergaenzt. Motiv, Text-/CTA-Position, Groesse und Homepage unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Vorschauperspektive am Originalentwurf abgeglichen

Status: in Arbeit

- Nur `transform` von `.preview` in `homepage/seo-eyecatcher-preview.html` angepasst: projektive Matrix anhand der Kantenrichtung des urspruenglichen Entwurfs statt weiterer unabhaengiger Euler-Drehungen. Visuelle Annaeherung, keine identische Wiederherstellung der urspruenglichen 3D-Kamera behauptet.
- Motivdatei, Texte, CTA, Groesse, Positionierung und Homepage unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Seitliche Perspektivrichtung separat korrigiert

Status: in Arbeit

- Nur Vorschaucontainer in `homepage/seo-eyecatcher-preview.html`: Y-Drehung von -18 auf 18 Grad umgekehrt. X-/Z-Drehung, Motiv, Texte, CTA und Homepage unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Unbeauftragten Motivwechsel zurueckgenommen

Status: in Arbeit

- Separate Vorschau: vorheriges freies Displaymotiv sowie Text-/CTA-Position wiederhergestellt. Nur gemeinsame Perspektive am Vorschaucontainer angepasst; keine Aenderung der Bilddateien oder Homepage.
- Visuelle Abnahme offen.

## 2026-10-20 - Urspruengliches Perspektivmotiv in separater Vorschau

Status: in Arbeit

- `homepage/seo-eyecatcher-preview.html`: urspruengliches Motiv `assets/seo-check-eyecatcher.png` wieder eingesetzt und nachtraegliche Drehungen des Gesamtmotivs entfernt. HTML-Text und CTA auf urspruengliche Displayposition angepasst, ohne eigene Hintergrundbox.
- Homepage und Bilddateien unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Oberkante der Vorschau nach hinten gekippt

Status: in Arbeit

- Nur `homepage/seo-eyecatcher-preview.html`: X-Drehung von 6 auf 18 Grad verstaerkt, damit die Oberkante weiter nach hinten kippt. Seitliche Drehung, Texte, CTA und Homepage unveraendert.
- `git diff --check` erfolgreich; visuelle Abnahme offen.

## 2026-10-20 - Perspektivrichtung der separaten Vorschau korrigiert

Status: in Arbeit

- `homepage/seo-eyecatcher-preview.html`: Y-Drehung von -18 auf 18 Grad und Z-Drehung von -3 auf 3 Grad geaendert. Display, Text und CTA bleiben gemeinsam ausgerichtet.
- Homepage und Assets unveraendert. Visuelle Abnahme offen.

## 2026-10-20 - Gemeinsame Perspektive fuer Display-Vorschau

Status: in Arbeit

- Ausschliesslich `homepage/seo-eyecatcher-preview.html`: gemeinsamer perspektivischer Transform auf `.preview`, sodass Displaymotiv, HTML-Text und klickbarer CTA dieselbe raeumliche Ausrichtung erhalten. Positionierung auf der Displayflaeche erhalten.
- `homepage/index.html` und Bilddateien unveraendert.

Pruefung: HTML5-/CSS-Parser und `git diff --check`; visuelle Nutzerabnahme offen.

## 2026-10-20 - Display-Vorschau ohne aufgeklebte Textbox

Status: in Arbeit

- Nur separate Vorschau: `homepage/assets/seo-check-preview-display.png` mit freier Displayflaeche und seitlicher Lupe vorbereitet. `homepage/seo-eyecatcher-preview.html` verwendet dieses Motiv; Text und bedienbarer Button sitzen ohne eigene Hintergrundbox innerhalb der freien Displayflaeche.
- Maximale Vorschaugroesse bleibt 460 px. `homepage/index.html` und urspruengliches Eyecatcher-Motiv unveraendert.

Pruefung: HTML5, CSS und `git diff --check`; visuelle Nutzerabnahme offen.

## 2026-10-20 - Vorschautext und CTA auf Displayflaeche

Status: in Arbeit

- Ausschliesslich `homepage/seo-eyecatcher-preview.html`: Text und bedienbaren CTA ueber der Displayflaeche statt neben dem Motiv positioniert. Kompakte Gesamtbreite von maximal 460 px erhalten, mobile Typografie angepasst.
- `homepage/index.html`, Assets und Homepage-Funktionalitaet unveraendert.

Pruefung: HTML5-/CSS-Parser und `git diff --check`; visuelle Abnahme offen.

## 2026-10-20 - Eyecatcher-Einbindung zurueckgenommen, separate kleine Vorschau

Status: in Arbeit

- Letzte SEO-Eyecatcher-Einbindung in `homepage/index.html` zurueckgenommen: vorheriges Emerald-Band samt Texten und CTA an allen drei Stellen wiederhergestellt. Andere Homepage-Aenderungen erhalten.
- `homepage/seo-eyecatcher-preview.html`: isolierte Vorschau mit maximal 460 px Gesamtbreite statt 840 px; Motiv 160 px breit, mobil 110 px. Keine Einbindung in der Homepage.
- Vorhandenes Eyecatcher-Asset weiter nur fuer die separate Vorschau verwendet. Keine anderen Assets veraendert.

Pruefung: HTML5, CSS und `git diff --check`; visuelle Nutzerabnahme offen.

## 2026-10-19 - Freigegebenen SEO-Eyecatcher an drei Stellen eingebunden

Status: in Arbeit

- `homepage/assets/seo-check-eyecatcher.png`: transparentes Browserfenster-/Lupenmotiv aus dem freigegebenen visuellen Entwurf vorbereitet und eingebunden. Originalentwurf erhalten; sonstige Assets nicht bearbeitet.
- `homepage/index.html`: alle drei bestehenden `.nv-seo-promo`-Positionen verwenden das Motiv mit echtem HTML-Text „Kostenloser SEO-Check“, „SEO-Probleme erkennen. Potenziale entdecken.“ und bestehender goldener CTA-Komponente mit Text „Website prüfen“. Ziel bleibt `detail_seo.html`.
- Band-Pseudoelemente entfernt. `.nv-seo-promo__image` und responsives Text-/Bildraster ergaenzt, ohne umschliessende Card-Flaeche. Mobile unter 560 px Motiv ueber Text/CTA. Hooks, Einblendung und Reduced-Motion-Regel erhalten.
- Analysebereich, Formulare und bestehende JavaScript-Logik unveraendert.

Pruefung: HTML5-/CSS-Parser, drei Bild-/CTA-Zuordnungen und `git diff --check` erfolgreich. Sichtbares Motiv im Browser geladen; uebrige Positionen verwenden dieselbe Datei mit Lazy Loading. Visuelle Nutzerabnahme offen; kein Deployment.

## 2026-10-19 - SEO-Eyecatcher als Emerald-Band zur Vorschau

Status: in Arbeit

- `homepage/index.html`: `.nv-seo-promo` von abgerundeter schwarzer Card auf Emerald-Band mit schraegen Enden und Goldkante umgestellt. Hintergrundform ueber lokale Pseudoelemente; Texte und CTA bleiben unverzerrt. Desktop- und Mobile-Innenabstand angepasst.
- An allen drei bestehenden Callout-Positionen Titel „SEO Toolbox“ fuer die freigegebene Vorschau durch „Kostenloser SEO-Check“ ersetzt. Beschreibung, CTA „SEO Toolbox öffnen“, Ziel `detail_seo.html`, Hooks, Einblendung und Reduced-Motion-Verhalten erhalten.
- Analysebereich, Formulare und weitere Komponenten unveraendert.

Pruefung: HTML5-/CSS-Parser und `git diff --check` erfolgreich. Drei aktualisierte Hinweise im geladenen Browser-DOM bestaetigt. Visuelle Abnahme der Vorschau offen; kein Deployment.

## 2026-10-19 - Gruene transparente Aufklappfelder

Status: in Arbeit

- `homepage/index.html`: Hintergrund von `.nv-analyse__disclosure` von deckendem Gunmetal auf vorhandenes Emerald mit 85 Prozent Deckkraft umgestellt. Nur die Feldflaeche ist transparent, Schrift und Symbole bleiben deckend; Bilder hinter geoeffneten Feldern koennen dezent durchscheinen.
- Abmessungen, Aufklapplogik, Texte, aeussere Karten, Bilder und Formular unveraendert.

Pruefung: CSS-Parser und `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Aufklappfelder verbreitern sich beim Oeffnen

Status: in Arbeit

- `homepage/index.html`: `.nv-analyse__column` stellt die verfuegbare Breite bereit. Einzelne `.nv-analyse__disclosure` sind geschlossen 58 Prozent und geoeffnet 86 Prozent breit; mobil 88 bzw. 100 Prozent. Nur das aktive Feld verbreitert sich, mit lokalem Breitenuebergang und Reduced-Motion-Regel.
- Aeussere Karten, Texte, Bilder, CTA, Preise, Formular und JavaScript unveraendert.

Pruefung: HTML5-/CSS-Parser und `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Gemeinsames Kartensystem, groesseres linkes Motiv und mittiger CTA

Status: in Arbeit

- `homepage/index.html`: beide Analyse-Angebote verwenden nun die vorhandene `.nv-acard`-Komponente fuer Rahmen, Flaeche, Innenabstand, Tiefenschatten und Hover-/Fokusverhalten wie die Rechnerkarten. Doppelte eigene Shell-Regeln und dekoratives Hintergrundlogo entfernt.
- Linkes Analysebild auf 292 px Hoehe vergroessert; rechtes Bild bleibt 220 px hoch. Damit erhalten beide proportional dargestellten Bilddateien etwa dieselbe Breite von 164 px. Keine Bilddateien bearbeitet.
- `.nv-analyse__offer .hero-cta`: horizontal zentriert. Mobile bestehende CTA-Breite beibehalten.
- Texte, Preise, Links, Formular und JavaScript unveraendert.

Pruefung: HTML5- und CSS-Parser sowie `git diff --check` erfolgreich. Optische Groessenabnahme offen.

## 2026-10-19 - Einstiegssatz und reduzierte Analyse-Textbreite

Status: in Arbeit

- `homepage/index.html`: freigegebenen Satz unter dem Titel der kostenlosen Analyse eingefuegt: „Für eine erste unverbindliche Einschätzung Ihrer Prozesse und Automatisierungspotenziale.“
- `.nv-analyse__column`: Desktop-Textbreite von 78 auf 66 Prozent reduziert. Mobile-Regel mit 100 Prozent, Bilder, Preise, weitere Texte, Formular und JavaScript unveraendert.

Pruefung: HTML5-Struktur, CSS-Parser und `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Tiefenanalyse zeigt ausschliesslich Erweiterungen

Status: in Arbeit

- `homepage/index.html`: Aufklapppunkt „Überblick“ samt Kurztext ausschliesslich aus der Tiefenanalyse entfernt. Einen zugehoerigen Bildzustand entfernt; fuenf Erweiterungen und ein Ausgangsbildzustand bleiben.
- Ueberblick der kostenlosen Analyse, dauerhaft sichtbarer Erweiterungshinweis, CSS, JavaScript, Preise, Assets und Formular unveraendert.

Pruefung: HTML5-Struktur, verbleibende Aufklapppunkte, Bildzustandsanzahl und `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Kurze Ueberblicktexte und breitere Textspalten

Status: in Arbeit

- `homepage/index.html`: beide Ueberblick-Inhalte durch die ausdruecklich freigegebenen Kurztexte ersetzt. Kostenlos: „Wir prüfen Ihre Prozesse, Daten und Automatisierungspotenziale und empfehlen den sinnvollsten nächsten Schritt.“ Tiefgehend: „Wir vertiefen die Analyse und erstellen eine konkrete Grundlage für die technische und wirtschaftliche Umsetzung.“
- `.nv-analyse__stage`, `.nv-analyse__column`, `.nv-analyse__visual`: Text und Bild auf Desktop in derselben Grid-Zelle angeordnet. Textspalte 78 Prozent, Bildbereich rechts 40 Prozent; Text liegt vor dem teilweise ueberlappenden Bild. Mobile bis 640 px weiter untereinander ohne Ueberlagerung.
- Preise, sonstige Leistungstexte, Formular, JavaScript und Assets unveraendert.

Pruefung: HTML5- und CSS-Parser sowie `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Workshop aus Tiefenanalyse entfernt

Status: in Arbeit

- `homepage/index.html`: Aufklapppunkt „Workshop mit Ihrem Team“ einschliesslich Beschreibung auf Nutzerwunsch entfernt. Zugehoerige Anzahl der Bildzustaende um einen reduziert.
- Andere Leistungen, CSS, JavaScript, Preise, Assetpfade und Formular unveraendert.

Pruefung: HTML5-Struktur, Zuordnung von Aufklapppunkten und Bildzustaenden sowie `git diff --check` erfolgreich. Visuelle Abnahme offen.

## 2026-10-19 - Leistungsumfang der Tiefenanalyse verdeutlicht

Status: in Arbeit

- `homepage/index.html`: freigegebenen Hinweis dauerhaft sichtbar unter dem Titel der Tiefenanalyse und vor den Aufklapppunkten eingefuegt: „Enthält alle Leistungen der kostenlosen Potenzialanalyse und erweitert diese um folgende Leistungen:“
- Bestehende Inhalte, CSS-Klassen, JavaScript, Bildpfade, Preise und Formular unveraendert.

Pruefung: HTML5-Parser und `git diff --check` erfolgreich. Desktop-/Mobile-Sichtpruefung offen; keine Browserpruefung oder Formularuebermittlung ausgefuehrt.

## 2026-10-19 - Sektionsbody und gemeinsame Analysebreite angeglichen

Status: in Arbeit

- `homepage/index.html`: `.nv-analyse__text` mit unveraendertem Bodytext aus dem zentrierten Rechnercontainer direkt unter die Subline verschoben. `.nv-analyse__intro` erhaelt 32 px Abstand zum folgenden Rechnerbereich.
- `.nv-analyse__offers` und `.nv-analyse__inner > .nv-aform` auf dieselbe maximale Gesamtbreite von 1260 px wie `.nv-analyse__layout` gesetzt. Abweichende mobile Maximalbreite von 618 px entfernt; alle drei Bereiche folgen derselben verfuegbaren Inhaltsbreite. Gleiche Breite der beiden unteren Karten beibehalten; unterschiedliche Gewichtung der oberen Rechnerkarten unveraendert.
- Texte, Preise, Assets, Formular, IDs, JavaScript und andere Sektionen unveraendert.

Pruefung: HTML5-Struktur, CSS-Parser und `git diff --check`. Browserpruefung offen, da der bisherige Browser-Tab nicht mehr vorhanden ist. Kein Deployment.

## 2026-10-19 - Analyse-Kartenbreite, gleiche Hoehen und oberster Ueberblick

Status: in Arbeit

- `homepage/index.html`: allgemeine Einleitungs- und Ergebnistexte beider Analysen unveraendert in den jeweils ersten Aufklapppunkt `Überblick` verschoben, einschliesslich der bisherigen Output-Zwischenzeilen. Bildzustaende um diesen Punkt erweitert; vorhandene JavaScript-Steuerung unveraendert.
- `.nv-analyse__offers`: zentrierte Gesamtbreite auf maximal 1000 px begrenzt, beide Desktop-Karten gleich breit und gleich hoch. Unter 980 px einspaltig mit gleichen Kartenhoehen, gemeinsamer maximaler Breite von 618 px und responsiver Begrenzung durch den Inhaltsbereich.
- `.nv-analyse__inner > .nv-aform`: dieselbe Breite und dieselben seitlichen Kanten wie die gesamte Kartenreihe darueber. Formular-Markup und -Logik unveraendert.
- `.nv-analyse__visual`, `.nv-analyse__image`: beide Motive mit gleicher Hoehe von 220 px, ohne Beschnitt oder Verzerrung; ihre unterschiedlichen Seitenverhaeltnisse bleiben erhalten. `.nv-analyse__offer-footer` gruppiert Preise und Hinweise im normalen Inhaltsfluss. Preisraster mobil einspaltig; Summary-Texte koennen innerhalb ihrer Spalte umbrechen.
- Keine bestehenden Texte gekuerzt oder umformuliert, Preise, Links, IDs, Bildpfade und Bilddateien erhalten. Rechner und andere Sektionen unveraendert.

Pruefung: HTML5-Parser, CSS-Parser, JavaScript-/JSON-LD-Syntax und `git diff --check` erfolgreich. Formular, IDs, bisherige Scripts und Angebotstexte gegen Sicherung verglichen. Browser-Messungen bei 1280 px Desktop sowie 390 und 320 px Mobile: gleiche Kartenhoehen, identische Formular-/Kartenreihenbreite, aktive Bilder jeweils 220 px hoch, keine Summary-/Preistext-Ueberlaeufe in den geschlossenen Mobilkarten. Abstand vom Aufklappbereich zum Preis 12 px; auch geoeffnete Ueberblick-Punkte geprueft. Navigation vom neuen Ueberblick zum naechsten Punkt und einzelner aktiver Bildzustand bestaetigt. Keine Fehler in abgefragten Konsolenlogs.

Offen: visuelle Nutzerabnahme; Screenshot-Aufnahme scheiterte mit Zeitueberschreitung. Reduced Motion nur statisch geprueft, nicht emuliert. Kein Formularversand und kein Deployment.

## 2026-10-19 - Zwei eigenstaendige Analyse-Karten mit aufklappbaren Bulletpoints

Status: in Arbeit

- `homepage/index.html`: gemeinsame Bildspalte entfernt. Kostenlose und tiefgehende Potenzialanalyse als zwei getrennte Karten nebeneinander innerhalb der vorhandenen 1260-px-Inhaltsbreite umgesetzt; unter 980 px untereinander. Analysenamen stehen dauerhaft als Kartentitel ueber den Inhalten.
- Vier vorhandene kostenlose Leistungspunkte und sechs vorhandene Tiefenanalyse-Punkte als jeweils eigene Details-/Summary-Elemente umgesetzt. Bestehende kostenlose Beschreibungen unveraendert uebernommen; sechs kurze Tiefenanalyse-Erlaeuterungen auf ausdruecklichen Nutzerauftrag ergaenzt. Alle bisherigen Angebotstexte, Preise, Bedingungen und Links erhalten.
- Originalvorlage mit eigenen Inhalts-/Bildspalten, geschlossenem Ausgangszustand, animierter Inhaltshoehe und Bildzustaenden je Karte adaptiert. Jede Karte verwendet ausschliesslich ihr bestaetigtes Originalbild ohne Bildbearbeitung: `assets/Fotos/Analyse.png` bzw. `assets/Fotos/deep_analysis.png`.
- `homepage/analysis-offers.js`: Weiter-, Zurueck- und Schliessen-Steuerung sowie Abstimmung auf abgeschlossene Animationen pro Karte. Eigene Details-Gruppen verhindern gegenseitiges Schliessen zwischen beiden Analysen. Escape schliesst den aktiven Punkt und fuehrt den Fokus zurueck.
- Analyse-Rechner/Gauge oberhalb auf vorhandene 1260 px begrenzt; unveraendertes Formular darunter zentriert auf maximal 800 px. Die Einleitung bleibt an der bestehenden linken Sektionskante.
- Angepasste Klassen: `.nv-analyse__offers`, `.nv-analyse__offer`, `.nv-analyse__disclosure`, `.nv-analyse__summary`, `.nv-analyse__body`, `.nv-analyse__visual`, `.nv-analyse__image`, `.nv-analyse__layout`. Neue lokale Klassen: `.nv-analyse__stage`, `.nv-analyse__column`, `.nv-analyse__image-block`, `.nv-analyse__image-wrapper`, `.nv-analyse__control`. Fruehere `.nv-analyse__comparison`- und gemeinsame Bildwechsel-Regeln entfernt.
- Formularfelder, Consent, Honeypot, Rechner-Markup, alle bisherigen Scripts und IDs sowie saemtliche anderen Sektionen unveraendert. Keine Assets bearbeitet und keine neuen Bibliotheken eingebunden.

Pruefung: HTML5 ohne Parserfehler; CSS, JavaScript-Syntax, JSON-LD, unveraenderte Originaltexte/Preise/IDs/Formular-/Rechner-/Script-Struktur und andere Sektionen sowie `git diff --check` erfolgreich. Im lokalen Browser Desktop-Zweispaltenlayout, eigene Bilder, einzeln geoeffnete Punkte, unabhaengige Karten, Weiter/Zurueck/Schliessen und Escape geprueft. Mobile bei 375 CSS-px einspaltig ohne horizontalen Sektionsueberlauf, oeffnende Bulletpoints und Formular darunter bestaetigt. Keine Fehler in den abgefragten Browserkonsolenlogs.

Offen: Nutzerabnahme der Darstellung und neuen Tiefenanalyse-Texte. Reduced Motion statisch geprueft, nicht emuliert. Native Enter-/Leertasten-Aktivierung der Summary-Elemente in dieser Browserumgebung nicht abschliessend bestaetigt. Kein Formularversand, Push oder Deployment.

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
## 2026-10-21 - Gemeinsames Detailseiten-System als drei separate Vorschauen

Status: in Arbeit

- Neu: `tools/detail_pages/build.py`, `template.html`, `pages.json`, `verify.py`, `README.md` sowie `content/detail_ki-agenten.json`, `content/paket-buero.json`, `content/detail_seo.json`. Gemeinsames statisches Geruest mit vorhandenen Seitentexten, Sektionen, IDs, Metadaten, Header/Footer und Scripts als Seitendaten. Ausgabe ausschliesslich als separate Vorschau, kein Schreibmodus fuer Produktionsseiten.
- Neu: `homepage/preview-detail_ki-agenten.html`, `homepage/preview-paket-buero.html`, `homepage/preview-detail_seo.html` und `homepage/detail-pages.css`. Gemeinsame Sektionsreihenfolge nach Analyse-Referenz; bestehende Zusatzsektionen bleiben erhalten. Hero-Motive und je zwei Fotos aus den vorhandenen Assetordnern eingebunden, ohne Bildbearbeitung. Textfilter und Glow aus den alten Seitenstyles nicht uebernommen.
- CSS-Bereiche: `.detail-group`, `[data-section-role]`, `.detail-hero`, `.visual-card--hero`, `.detail-photo-layout`, `.detail-photo-layout--reverse`, `.detail-copy`, `.section-photo` sowie bestehende Inhaltsklassen fuer Panels, Listen, Module, Vergleiche, FAQ und SEO-Iframe. Bestehende Basisresets fuer Header/Footer in der Vorschau vor deren unveraendertem Shared-Stylesheet geladen. Keine neue JavaScript-Logik.
- Originale `analyse.html`, `index.html`, `shared-header-footer.css`, `nurovelle-tokens.css` und alle drei Original-Pilotseiten unveraendert. Vorher-/Nachher-Pruefsummen fuer die vier besonders geschuetzten Dateien und Quell-Pruefsummen der Pilotseiten bestaetigt. Originaltexte, Linkziele, IDs, Formularmarkup, Scripts und SEO-Iframe unveraendert uebernommen; kein Deployment.
- Pruefung: drei Vorschauen mit HTML5-Parser fehlerfrei; generatorbasierter Identitaetsvergleich fuer Texte, IDs, Links, Header/Footer, Formulare, Scripts und Iframes erfolgreich. Lokale Assetpfade vorhanden, neun Hero-/Foto-Dateien dekodierbar, CSS geparst, bestehende Inline-Scripts mit `node --check` geprueft, `git diff --check` erfolgreich. KI-Agenten-FAQ per Browser geoeffnet; KI-Agenten bei tatsaechlich 390 px ohne horizontalen Ueberlauf. Alle drei Vorschauen im Browser geladen; SEO ohne erfasste Seitenfehler. Vollstaendige Desktop-/Mobile-Sichtabnahme wegen fehlerhafter Browser-Viewport-/Screenshot-Ausgabe offen. Formulare nicht abgesendet, Reduced Motion nur statisch geprueft.
- Weitere Seiten bleiben bis zur visuellen Freigabe der drei Vorschauen unberuehrt. Offene Hero-/Fotozuordnungen sind in `tools/detail_pages/README.md` benannt.

## 2026-10-21 - Stripe-Secret aus dem Quellcode ausgelagert

Status: in Arbeit

- `homepage/stripe-sample-code/server.rb`: hartcodierten Secret Key entfernt; `STRIPE_SECRET_KEY` wird aus Prozessumgebung beziehungsweise privater `.env` mit `dotenv` geladen. Fehlender oder leerer Key fuehrt zum Abbruch. `NUROVELLE_STRIPE_ENV_FILE` erlaubt einen abweichenden privaten Pfad.
- Bestehenden Key in `/home/d4sd1ng/.config/nurovelle-stripe/.env` ausserhalb von Repository und Webroot gespeichert; Verzeichnis 700, Datei 600. Keyinhalt nicht ausgegeben. `homepage/stripe-sample-code/Gemfile` um `dotenv` ergaenzt, Ladeverhalten in `README.md` dokumentiert.
- Checkout-Routen, Preis-/Integrationsplatzhalter und `homepage/stripe-config.js` unveraendert. Keine Zahlungs-, Produkt-, Webhook- oder Deployment-Aenderung. Aktuelle versionierte Textdateien auf Secret-Key-Literale geprueft: keine Treffer. Alte Git-Versionen nicht umgeschrieben; Schluesselrotation bleibt offen.
- Ruby ist in dieser Umgebung nicht installiert; deshalb kein Serverstart und keine Laufzeitpruefung der Ruby-/dotenv-Integration. Keine Installation durchgefuehrt. Paket-Checkout bleibt unvollstaendig und wurde nicht als funktionierend bestaetigt.
