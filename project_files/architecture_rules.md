# Homepage Architecture Rules

## Zweck

Dieses Dokument hält die vorhandenen technischen Bereiche und ihre Grenzen fest.
Es führt keine neue Architekturentscheidung ein.

## Verbindliche Grundlagen

Für Ziel, Umfang und freigegebene Entscheidungen gelten:

1. `project_overview.md`
2. `task_contract.md`
3. `decision_log.md`
4. `todo.md`

Aktuelle ausdrückliche Nutzeranweisungen haben Vorrang.

## Vorhandene Projektbereiche

### Homepage

- `homepage/` enthält die Homepage, Rechtstextseiten, Analyse-Seiten, Styles und
  zugehörige Assets.
- Änderungen an HTML, CSS, JavaScript oder Assetpfaden erfolgen nur auf
  ausdrücklichen Auftrag.
- Bestehende IDs, Klassen, Formularlogik, Consent-Logik und Verlinkungen bleiben
  erhalten, sofern ihre Änderung nicht ausdrücklich beauftragt ist.

### Vite-, React- und Express-Bereich

- `client/` ist der in `vite.config.ts` konfigurierte Vite-Root.
- `server/` enthält den Express-Server für die gebauten statischen Dateien.
- `shared/` enthält gemeinsam verwendete TypeScript-Konstanten.
- Build-, Start- und Prüfkommandos werden durch `package.json` festgelegt.
- Dieser Bereich wird nicht mit der eigenständigen Homepage-Struktur vermischt,
  solange dies nicht ausdrücklich beauftragt ist.

### Werkzeuge und Assets

- `tools/` enthält projektbezogene Hilfswerkzeuge.
- `tools/blender/` enthält Blender-Skripte zur Asset-Erstellung.
- Erzeugte Assets werden nicht automatisch in HTML oder CSS eingebunden.
- Quelldateien und erzeugte Dateien werden nur auf ausdrücklichen Auftrag
  ersetzt, verschoben oder gelöscht.

## Frontend-Regeln

- Boards, Panels, Texte und kontrollierbare Darstellungsflächen werden gemäß
  `task_contract.md` und `decision_log.md` bevorzugt mit HTML und CSS umgesetzt.
- Bildassets enthalten keine erfundenen Texte, Labels, Zahlen, Logos oder
  lesbare UI-Inhalte.
- Responsives Verhalten, Formulare, Downloads, Danke-Seiten und CTA-Logik
  richten sich nach `task_contract.md`.
- Die vorhandene Komponenten-, Farb- und Typografielogik darf nicht ohne
  ausdrücklichen Auftrag ersetzt werden.

## Backend-, API- und Datenbankgrenzen

Für Backend, Analyse-API und Postgres gelten die jeweiligen Fachdokumente:

- `homepage_analysis_api_integration.md`
- `homepage_postgres_data_contract.md`
- `nurovelle_postgres_core_architecture.md`
- `backend_core_operations_runbook.md`

Diese Regeln werden in diesem Dokument nicht dupliziert oder erweitert.

## Änderungsregeln

- Keine Framework-, Build-, Routing-, API- oder Datenbankänderung ohne
  ausdrücklichen Auftrag.
- Keine neue Abhängigkeit ohne vorherige Prüfung des vorhandenen Stacks und
  ausdrückliche Anforderung.
- Änderungen bleiben auf den verantwortlichen Projektbereich beschränkt.
- Bestehende Schnittstellen zwischen `homepage/`, `client/`, `server/`,
  `shared/`, `tools/` und den Assets bleiben erhalten.
- Nach Änderungen werden die für den betroffenen Bereich vorhandenen Prüfungen
  ausgeführt und nicht geprüfte Punkte ausdrücklich benannt.
