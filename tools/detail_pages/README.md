# Detailseiten-Vorschau

Dieses System erzeugt ausschliesslich `homepage/preview-*.html`.
Produktionsseiten, `analyse.html`, Tokens und Shared Header/Footer werden nicht
geschrieben. Aktuell wird ausschliesslich die KI-Agenten-Vorschau zur Abnahme
bearbeitet. Die bereits vorhandenen Bueropaket- und SEO-Vorschauen bleiben unberuehrt.

Voraussetzung: Python mit `beautifulsoup4` und `html5lib`; die Pruefung verwendet
Node.js mit dem bereits im Projekt installierten `postcss`.

## Erstmalige Datenuebernahme

```sh
python3 tools/detail_pages/build.py --extract --pages detail_ki-agenten.html
```

Die bestehenden Texte, Sektionen, IDs, Metadaten, Header/Footer und Scripts
werden in `content/*.json` uebernommen. Vorhandene Seitendaten werden nicht
ueberschrieben. Die Abbildung auf die gemeinsame Reihenfolge erfolgt ueber
`role`; Preise und Datenschutz bleiben als Zusatzsektionen erhalten.

## Vorschauen neu erzeugen

```sh
python3 tools/detail_pages/build.py --pages detail_ki-agenten.html
python3 tools/detail_pages/verify.py --pages detail_ki-agenten.html
```

Das HTML-Geruest steht in `template.html`, die acht verbindlichen Sektionen
werden in `reference.py` direkt aus `homepage/analyse.html` uebernommen.
`ki_agenten.py` korrigiert die verantwortlichen kopierten Layoutdeklarationen
nur fuer diese Vorschau: maximal 1000 px Inhalt, flexible Raster, Titel in zwei
Zeilen, unskalierte Hero-Grafik und einspaltige Formularfelder auf kleinen Breiten.
Keine zusaetzliche Override-Stylesheet-Schicht und keine neuen `!important`-Regeln.
Bildzuordnungen stehen in `pages.json`. Header-Markup und Komponenten stammen
aus der Analyse, Footer und Navigation-/FAQ-Script aus der Originaldetailseite.
Die bestehende `shared-header-footer.css` bleibt unveraendert.

Die Vorschau hat `noindex,nofollow` und liegt neben der Originalseite. Dadurch
bleiben relative Links, lokale Sprunglinks und Originalscripts ohne `base`
oder Pfadumschreibung funktionsfaehig. Links zur Analyse oeffnen weiterhin die
unveraenderte Analyse-Seite.

## Sicherheitsgrenzen

- Original-Pruefsummen verhindern eine unbemerkte Uebernahme veralteter Daten.
- Unbekannte Sektionen oder fehlende Bildzuordnungen brechen den Lauf ab.
- Es gibt keine Ersatzbilder und keinen Schreibmodus fuer Produktionsseiten.
- Die eingebundenen Fachtexte und acht FAQ bleiben wortgleich. Wiederholte
  Konzeption-/Umsetzungskarten und zusaetzliche Listen der Originalseite werden
  entsprechend dem Acht-Sektionen-Auftrag nicht in die Vorschau uebernommen.
- Die Pruefung vergleicht die tatsaechlich zugeordneten Inhalte mit dem Original,
  nicht mehr den inzwischen ausdruecklich ersetzten gesamten Originalaufbau.
- Formular inklusive API-Script, Status-/Ergebnisanzeige, Pflicht-Consent und
  Honeypot stammt unveraendert aus der Analyse. Nur der dort fehlende Submit-CTA
  wird mit vorhandenem Gold-Button und vorhandenem Formulartitel ergaenzt;
  Feldbeschriftungen werden aus vorhandenen Platzhaltern und Optionsbezeichnungen
  als `aria-label` ergaenzt.
- Ein bestandener Strukturtest ist kein Nachweis fuer einen echten API-Versand,
  ein Payment oder eine visuelle Nutzerfreigabe.
- Erst nach visueller Freigabe folgen weitere Seiten und die Produktionsmigration.

## Noch offen

Die Hero-Zuordnung fuer Automationen, Workflows, Warum Nurovelle und
Tiefenanalyse ist noch nicht eindeutig. Dateien sind vorhanden, werden aber
nicht anhand eines unbekannten Bildinhalts geraten. Fuer Betreuung fehlen
zwei freigegebene Fotozuordnungen und fuer Handwerk die zweite.

Die Paket-CTAs bleiben Anfragen und werden nicht als funktionierender Checkout
ausgegeben. Stripe ist unabhaengig vom visuellen Umbau zu vervollstaendigen.
