# Pflichtprüfung einer Detailseite

Ein Befehl, der eine umgestellte Detailseite gegen alle verbindlichen Regeln prüft. Das Skript **liest nur** und ändert nichts.

```
node tools/pruefung/pruefe-seite.cjs <seite.html> [quellseite.html]
```

Beispiel:

```
node tools/pruefung/pruefe-seite.cjs preview-detail_roadmap.html detail_roadmap.html
```

Rückgabewert 0, wenn jede Regel bestanden ist, sonst 1.

## Was geprüft wird

| Regel | Quelle |
| --- | --- |
| Shared Header und Footer: Stylesheet geladen, Header- und Footer-Block zeichengleich mit `analyse.html` | `decision_log.md` 2026-09-30 |
| Alle Assetpfade liegen tatsächlich auf der Platte | `AGENTS.md`, keine erfundenen Pfade |
| Genau eine Trennlinie zwischen je zwei Sektionen | `styleguide.md` 21.5 |
| Kein Textstück, das nicht aus der Quellseite stammt | `nurovelle_homepage_visible_content.md` |
| Jeder Inhaltslink der Quellseite ist übernommen | `AGENTS.md` |
| Jede Sektion hat Kicker, Titel und Subline | `styleguide.md` 21.1 |
| Breiten aller Bausteine bei 1100, 1440, 1600, 1920 und 2560 px | `styleguide.md` 21.0 bis 21.4 |
| Einzug gegenüber der Kopfkante, in jedem Block gleich | `styleguide.md` 21.1 |
| Kein waagerechter Überlauf bei 390 bis 2560 px | `styleguide.md` 21.7 |
| Keine JavaScript-Fehler, keine Fehlantworten, auch bei `prefers-reduced-motion` | `AGENTS.md` |

**Nur bei einer Breite zu messen ist nicht aussagekräftig.** Bei 1440 px beträgt der Einzug aus der 1300er Regel 1 px; Fehler fallen dort nicht auf und erst ab 1600 px. Deshalb prüft das Skript immer alle Breiten.

## Freigegebene Abweichungen

Texte, die bewusst nicht aus der Quellseite stammen, und Links, die bewusst entfallen, stehen je Seite in `freigaben/<seite>.json`:

```json
{
  "texte": ["Definition", "…"],
  "linksOhne": ["index.html#leistungen"]
}
```

Jeder Eintrag dort ist eine ausdrückliche Entscheidung des Nutzers und in `decision_log.md` belegt. Ohne Eintrag meldet das Skript die Abweichung.

## Voraussetzung

Playwright mit dem vorinstallierten Chromium unter `/opt/pw-browsers/chromium`. Das Skript startet seinen eigenen Webserver auf einem freien Port und beendet ihn wieder.
