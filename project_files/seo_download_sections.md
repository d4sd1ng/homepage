# SEO- und Download-Sektionen

## Ziel

Die Startseite enthaelt jetzt zwei vorbereitete Erweiterungen:

- SEO-Tool-Sektion fuer sichtbarkeitsbezogene KI-Systeme
- Download-Sektion fuer spaetere Lead-Magnet-Dokumente

## SEO-Sektion

Datei:

- `homepage/index.html`

Section-ID:

- `#seo-tools`

Regeln:

- Karten verlinken vorerst auf `#analyse`.
- Karten besitzen stabile IDs.
- `data-landing-source` verweist auf die jeweilige Quelle in `Landing_pages/`.
- Detailseiten oder finale SEO-Ziellinks koennen spaeter ohne Layout-Umbau ersetzt werden.

Aktuelle SEO-Karten:

- `#seo-dominator`
- `#seo-keyword-navigator`
- `#seo-onpage-optimizer`
- `#seo-meta-snippet`
- `#seo-technical-scanner`
- `#seo-content-brief`
- `#seo-page-speed`
- `#seo-image-optimizer`
- `#seo-broken-link-checker`
- `#seo-audit-checklist`
- `#seo-serp-watcher`

## Download-Sektion

Datei:

- `homepage/index.html`

Section-ID:

- `#downloads`

Kompatibilitaetsanker:

- `#leitfaden`

Regeln:

- Es wurden keine Dateien aus `G:\Projects\Dokumente_lead` kopiert.
- Downloads sind nur namentlich vorbereitet.
- Sichtbarer Status bleibt `In Vorbereitung`, bis finale Dokumente freigegeben sind.
- Finale Dateien werden spaeter ueber echte Links eingebunden.

Aktuelle Download-Keys:

- `praxisleitfaden-ki-automatisierung-mittelstand`
- `roi-guide-ki-automatisierung`
- `mini-guide-prozessanalyse`
- `case-study-ki-automatisierung`

## Spaetere Finalisierung

Wenn die finalen Dokumente bereit sind:

1. Finale Dateien in einen freigegebenen Download-Pfad legen.
2. `span.download-card-action` durch echte Download-Links ersetzen.
3. `data-final-asset` mit dem finalen Dateinamen befuellen.
4. Status von `In Vorbereitung` auf den finalen Download-Hinweis aendern.
5. Links im Browser und mobil testen.
