# Nurovelle Homepage – Task Contract

Stand: 2026-08-14  
Status: freigegeben

## Zweck dieser Datei

Diese Datei enthält ausschließlich **Arbeitsregeln**.

Sie beschreibt nicht das Design, die Seitenstruktur oder offene Aufgaben.

## Prioritätenrangfolge

1. Explizite aktuelle Benutzervorgabe
2. `task_contract.md`
3. `decision_log.md`
4. `project_overview.md`
5. `todo.md`
6. `styleguide.md`
7. `architecture.md`
8. `assets.md`
9. technische Referenzdateien
10. bestehender Produktionscode

Bei Widersprüchen gilt immer die höher priorisierte Quelle.

## Pflichtprüfung vor Änderungen

Vor jeder projektbezogenen Änderung sind mindestens zu prüfen:

- `project_overview.md`
- `task_contract.md`
- `decision_log.md`
- `todo.md`
- `styleguide.md`
- `nurovelle-tokens.css`
- relevante CSS-/Animationsreferenzen
- `architecture.md`
- `assets.md`
- `changelog.md`

Zusätzlich muss der tatsächlich zu ändernde Produktionscode geprüft werden.

## Grundregel

Existiert eine exakte Vorgabe, Entscheidung, Vorlage oder bestehende freigegebene Umsetzung, wird sie übernommen.

Nicht erlaubt ohne ausdrücklichen Auftrag:

- interpretieren
- umgestalten
- vereinfachen
- erweitern
- kürzen
- neue Inhalte ergänzen
- Layout verändern
- neue Komponenten erfinden
- Farben verändern
- Fonts verändern
- Assets austauschen
- IDs oder Klassen umbenennen
- bestehende Funktionen entfernen

## Keine stillen Änderungen

Änderungen dürfen nicht nebenbei an Bereichen vorgenommen werden, die nicht zum Auftrag gehören.

Wenn eine notwendige Folgeänderung erkannt wird:

- nicht still ausführen
- als Abhängigkeit oder offenen Punkt dokumentieren
- nur ausführen, wenn sie technisch zwingend zum beauftragten Änderungsumfang gehört

## Keine Annahmen

Fehlt eine notwendige Information:

- vorhandene Projektdateien und Produktionscode prüfen
- vorhandene Entscheidung suchen
- nichts erfinden
- bei weiterhin fehlender Grundlage als `blockiert` oder `offen` dokumentieren

## Produktionscode

- bestehende verantwortliche Regel direkt ändern
- keine Emergency-Overrides
- keine doppelten CSS-Regeln als Workaround
- keine widersprüchlichen Implementierungen
- kein unnötiges `!important`
- reale bestehende Selektoren verwenden
- keine Selektoren aus Annahmen erzeugen

## Inhalte

- freigegebene Texte unverändert übernehmen
- keine Textkürzung ohne Auftrag
- keine Ergänzung nicht freigegebener Aussagen
- keine erfundenen Leistungsversprechen, Kennzahlen, Referenzen oder Erfahrungswerte
- keine vollständigen Detailseiten-Inhalte auf Homepage-Cards kopieren

## Platzhalter

Ein Erzeugnis mit Platzhaltern gilt nicht als fertig und wird nicht vorgelegt. Das gilt auch für einen begleitenden Hinweis wie „vor Veröffentlichung durch belegte Werte ersetzen".

Lässt sich eine Zahl nicht belegen:

- das Stück so bauen, dass es ohne Zahlen trägt – aus Aussagen statt Statistik
- wird die unbelegte Zahl trotzdem gewünscht, sind **beide** Fassungen zu liefern: die mit der Zahl und eine vollständige ohne

## Agenten-Team

Für das Jude-Agententeam gelten dieselben Regeln wie für jede andere Bearbeitung. Zusätzlich:

- `homepage_repo` ist **ausschließlich lesbar**. Kein Anlegen, kein Ändern, kein Löschen, kein Umbenennen – auch nicht von Assets.
- Vor jedem Erzeugnis sind die zuständigen Projectfiles zu lesen; die Rangfolge oben gilt unverändert.
- Was in keiner Projectfile steht, wird nicht erfunden, sondern als `offen` gemeldet.
- Jedes fertige Erzeugnis wird zur Abnahme vorgelegt und geht erst nach Freigabe nach außen.
- Ergebnisse werden nur als geprüft oder geändert bezeichnet, wenn sie es tatsächlich sind.

## Design

Alle Designentscheidungen kommen ausschließlich aus:

```text
styleguide.md
nurovelle-tokens.css
```

Der Task Contract wiederholt keine Farben, Fonts, Verläufe oder Komponentenwerte.

## Assets

Alle Assetnamen, Pfade und Verwendungszwecke kommen ausschließlich aus:

```text
assets.md
```

Vor Verwendung ist zu prüfen, ob das Asset im realen Projektbestand existiert.

Keine Umbenennung, Ersetzung oder Neuinterpretation ohne Auftrag.

## Bildgenerierung / Bildbearbeitung

Für Nurovelle-Bilder gilt immer der freigegebene Nurovelle-Stil und transparenter Hintergrund.

Bei bestehenden Formen:

- Form nicht frei verändern
- keine neue Form erfinden
- keine zusätzliche Plattform oder Bodenplatte
- keine Texte, Labels, Logos oder lesbare UI ins Bild
- bei Serien nur die ausdrücklich genannte Variable ändern

## Dokumentation

Jede Information hat genau eine zuständige Datei.

- Projektumfang und Seitenlogik → `project_overview.md`
- Arbeitsregeln → `task_contract.md`
- Entscheidungen → `decision_log.md`
- offene Aufgaben → `todo.md`
- Design → `styleguide.md`
- Assets → `assets.md`
- technische Struktur → `architecture.md`
- ausgeführte Änderungen → `changelog.md`

Andere Dateien dürfen auf die zuständige Datei verweisen, aber deren Inhalt nicht vollständig duplizieren.

## Statuswerte

Nur diese Statuswerte verwenden:

- offen
- in Arbeit
- fertig
- geprüft
- freigegeben
- blockiert

## Änderungsnachweis

Nach tatsächlichen Projektänderungen muss `changelog.md` aktualisiert werden.

Ein Changelog-Eintrag enthält nur:

- Datum
- Status
- tatsächlich geänderte Dateien/Bereiche
- tatsächlich nicht geänderte relevante Bereiche, wenn dies zur Abgrenzung notwendig ist

## Prüfung vor Abschluss eines Arbeitsauftrags

Vor Meldung eines Ergebnisses prüfen:

- Vorgabe vollständig eingehalten?
- unbeauftragte Änderung vorgenommen?
- alte Quelle statt aktueller Quelle verwendet?
- neue Annahme eingeführt?
- Datei tatsächlich geändert oder nur vorgeschlagen?
- Changelog bei tatsächlicher Änderung aktualisiert?

Nur tatsächlich geprüfte oder geänderte Zustände als solche bezeichnen.
