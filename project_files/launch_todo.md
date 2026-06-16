# Launch Todo

## Vor Launch zwingend

- [x] Homepage-Dateien auf den VPS deployen.
- [x] Root-Route `/` final auf Homepage umstellen.
- [x] `homepage/index.html` visuell auf Desktop pruefen.
- [x] `homepage/index.html` visuell auf Smartphone pruefen.
- [x] `homepage/analyse.html` visuell auf Desktop pruefen.
- [x] `homepage/analyse.html` visuell auf Smartphone pruefen.
- [x] Potenzialanalyse-End-to-End live testen.
- [x] Lead-Speicherung nach Analyse live pruefen.
- [x] Pflichtfeldfehler gegen Analyse-Start pruefen.
- [x] Ergebnislink `https://nurovelle.de/results/<analysis_id>` live pruefen.
- [x] `/lead` nach Reporterzeugung pruefen.
- [x] Doppelte `/lead`-Submits beobachten.
- [ ] Newsletter-/Nurturing-Opt-in live pruefen.
- [x] Analyse-Frontend mit API-Timeout absichern.
- [x] Analyse-Frontend auf direkte DB-/Secret-Bezuege pruefen.
- [x] Spam-Schutz als Honeypot dokumentieren.
- [x] Tracking-/Consent-Entscheidung dokumentieren.
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

- [x] Finales OpenGraph-Bild erstellen.
- [x] `og:image` auf finales Hero-Bild umstellen.
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
- [x] Rollback-Pfad festlegen.
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
- `https://nurovelle.de/assets/hero/1.png` liefert 200 fuer OpenGraph.
- `https://nurovelle.de/results/<analysis_id>` bleibt erreichbar.
- Root-Umstellung erfolgte nur im Frontend-Container.
- Backend, DB, Firewall, Tunnel und Netzwerkkonfiguration wurden nicht geaendert.

## Backend-DB-Cutover-Status 2026-06-15

- Live-Backend schreibt jetzt in `nurovelle_core`.
- Alte Datenbank `nurovell_potential_analysis` bleibt als Rollback-Quelle erhalten.
- Pre-Cutover-Backup:
  - `/opt/nurovell-potential-analysis/backups/postgres/nurovell_potential_analysis_precutover_20260615_181902.dump`
- Runtime-Rollback-Datei:
  - `/opt/nurovell-potential-analysis/compose/.env.vps.pre_nurovelle_core_20260615_181902`
- Post-Cutover-Preflight erfolgreich:
  - Backend laeuft
  - Postgres ist healthy
  - Runtime DB ist `nurovelle_core`
  - Tabellen-Counts zwischen alter DB und `nurovelle_core` stimmen ueberein
  - Live-GETs sind gruen
- Schreibender Live-E2E erfolgreich:
  - Fragen geladen
  - Analyse gestartet
  - Antworten gespeichert
  - Score berechnet
  - Report erzeugt
  - Lead gespeichert
- Markierter Testdatensatz wurde danach bereinigt und mit Count `0` verifiziert.
- Backend-Logs nach Neustart zeigen keine kritischen Fehler.
- Formular-Honeypot ist aktiv.
- Cookie-Hinweis nennt keine aktiven Analyse-/Marketing-Cookies.
- Homepage visuell auf Desktop und Smartphone abgenommen.
- Analyse-End-to-End ist live geprueft, inklusive Ergebnis-URL und `/lead`.
- Pflichtfeldfehler bei fehlender Kontakt-E-Mail liefern jetzt `400/VALIDATION_ERROR`.
- Doppelte `/lead`-Submits erzeugen aktuell separate Leads.
