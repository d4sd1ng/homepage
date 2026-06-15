# Launch Todo

## Vor Launch zwingend

- [x] Homepage-Dateien auf den VPS deployen.
- [x] Root-Route `/` final auf Homepage umstellen.
- [ ] `homepage/index.html` visuell auf Desktop pruefen.
- [ ] `homepage/index.html` visuell auf Smartphone pruefen.
- [ ] `homepage/analyse.html` visuell auf Desktop pruefen.
- [ ] `homepage/analyse.html` visuell auf Smartphone pruefen.
- [ ] Potenzialanalyse-End-to-End live testen.
- [ ] Lead-Speicherung nach Analyse live pruefen.
- [ ] Newsletter-/Nurturing-Opt-in live pruefen.
- [x] Analyse-Frontend mit API-Timeout absichern.
- [x] Analyse-Frontend auf direkte DB-/Secret-Bezuege pruefen.
- [ ] Notion-Integration auf dem VPS aktiv konfigurieren und testen.
- [ ] Resend/E-Mail-Integration auf dem VPS aktiv konfigurieren und testen.
- [x] Impressum-Link pruefen.
- [x] Datenschutz-Link pruefen.
- [ ] Datenschutzerklaerung gegen Lead-, Notion-, Resend- und Newsletter-Flow pruefen.

## SEO-Sektion

- [ ] Entscheiden, ob SEO-Karten vorerst auf `#analyse` bleiben oder eigene Detailseiten bekommen.
- [ ] Falls Detailseiten genutzt werden: finale HTML-Seiten aus `Landing_pages/` erstellen.
- [ ] Fuer jede SEO-Detailseite Meta Title setzen.
- [ ] Fuer jede SEO-Detailseite Meta Description setzen.
- [ ] Fuer jede SEO-Detailseite Canonical setzen.
- [ ] Interne Links von SEO-Karten auf finale Ziele aktualisieren.
- [ ] SEO-Karten mobil pruefen.

## Download-Sektion

- [ ] Finale Dokumente freigeben.
- [ ] Finale Dokumente in den vereinbarten Download-Pfad legen.
- [ ] Keine Entwurfsdateien, Office-Lockfiles oder Temp-Dateien deployen.
- [ ] `data-final-asset` je Download-Karte setzen.
- [ ] Platzhalter `Download folgt` durch echte Download-Links ersetzen.
- [ ] Download-Dateien direkt im Browser testen.
- [ ] Download-CTA und Lead-/Nurturing-Logik final entscheiden.

## Technisches SEO

- [ ] Finales OpenGraph-Bild erstellen.
- [ ] `og:image` auf finales Bild umstellen.
- [ ] OpenGraph-Vorschau testen.
- [ ] LinkedIn-Vorschau testen.
- [ ] Page Title und Meta Description nach finalem Copy-Review pruefen.
- [ ] Mobile Ladezeit pruefen.
- [ ] Bildgroessen und Alt-Texte final pruefen.

## Conversion

- [ ] Haupt-CTA im Hero testen.
- [ ] Analyse-CTA in SEO-Sektion testen.
- [ ] Download-CTA-Verhalten final entscheiden.
- [ ] Calendly- oder Kontaktlink final entscheiden.
- [ ] Danke-Seite erstellen oder bestaetigtes Verhalten nach Formularsubmit festlegen.
- [ ] Ergebnislink `https://nurovelle.de/results/<analysis_id>` live pruefen.

## Deployment / Betrieb

- [ ] Vor Deploy aktuellen Git-Stand committen.
- [x] Statische Homepage per HTTPS pruefen.
- [x] Nach finaler Root-Aktivierung Live-Seite mit HTTPS pruefen.
- [ ] Browser-Cache/CDN-Cache nach Deploy beruecksichtigen.
- [ ] Rollback-Pfad festlegen.
- [ ] Keine Netzwerk-, Tunnel- oder Heimnetz-Aenderungen fuer diesen Launch durchfuehren.

## Deploy-Status 2026-06-08

- GitHub-Stand `5f0904e` ist gepusht.
- VPS-Dateien liegen unter `/opt/homepage_repo`.
- Next-Frontend-Static-Pfad liegt unter `/opt/nurovell-potential-analysis/frontend/public/homepage`.
- Container `nurovell_frontend` wurde neu gebaut und gestartet.
- Live erreichbar:
  - `https://nurovelle.de/homepage/index.html`
  - `https://nurovelle.de/homepage/analyse.html`
- Root `https://nurovelle.de/` wurde danach auf die statische Homepage umgestellt.
- Public SSH wurde nicht geoeffnet.
- Firewall-, Tunnel- und Netzwerkkonfiguration wurden nicht geaendert.

## Root-Status 2026-06-08

- `https://nurovelle.de/` leitet per 307 auf `/homepage/index.html`.
- `https://nurovelle.de/homepage/index.html` liefert 200.
- `https://nurovelle.de/homepage/analyse.html` liefert 200.
- `https://nurovelle.de/assets/hero/nurovelle_logo.png` liefert 200 fuer OpenGraph.
- `https://nurovelle.de/results/<analysis_id>` bleibt erreichbar.
- Root-Umstellung erfolgte nur im Frontend-Container.
- Backend, DB, Firewall, Tunnel und Netzwerkkonfiguration wurden nicht geaendert.
