# Changelog Project Files

## 2026-05-22

Aktualisiert:

- Domain auf nurovelle.de gesetzt.
- Finale Branchenliste eingetragen.
- Finale Service-Liste eingetragen.
- Alte Branchenbezüge entfernt.
- Alte Services verworfen.
- Services und Branchen getrennt dokumentiert.
- Asset-Pfade aktualisiert.
- sections_bg.png als finaler Section-Hintergrund dokumentiert.
- hero/hero_bg_cube_right_final.png als finaler Hero-Hintergrund dokumentiert.
- Card-Bilder bleiben textfrei.
- Card-Texte werden separat im HTML gesetzt.
- Keine freien Texte außerhalb der Project-Files.

## 2026-06-08

Aktualisiert:

- `homepage/analyse.html` an den produktiven Nurovelle-Analyse-Flow angebunden.
- Alte lokale Fake-Auswertung entfernt.
- Formular ruft jetzt die echte API unter `https://nurovelle.de/api/v1` auf.
- Flow: Fragen laden, Analyse starten, Antworten speichern, Scores berechnen, Report erzeugen.
- Ergebnislink zeigt auf `https://nurovelle.de/results/<analysis_id>`.
- `homepage/index.html` kann weiterhin per GET auf `analyse.html` weiterleiten; `analyse.html` übernimmt Query-Parameter als Vorbefüllung.
- Live-Smoke-Test gegen `nurovelle.de` erfolgreich.
- Lead-/Follow-up-Call ergänzt: `POST /api/v1/lead`.
- Newsletter-/Nurturing-Opt-in als separate Checkbox ergänzt.
- Lead-Message enthält Analyse-ID und Ergebnislink für Notion/CRM-Nachbearbeitung.

## 2026-06-08 SEO-/Download-Erweiterung

Aktualisiert:

- `homepage/index.html` um SEO-Tool-Sektion erweitert.
- SEO-Inhalte aus `Landing_pages/` abgeleitet.
- SEO-Karten mit stabilen IDs und `data-landing-source` versehen.
- Download-Bereich namentlich vorbereitet.
- Keine unfertigen Dokumente aus `G:\Projects\Dokumente_lead` auf die Homepage kopiert.
- Download-Karten mit stabilen `data-download-key` Werten versehen.
- Meta Title und Meta Description der Startseite aktualisiert.
- OpenGraph-Basisdaten ergaenzt; finales OG-Bild bleibt offen.
- `project_files/seo_download_sections.md` als technische Notiz ergaenzt.
- `project_files/launch_todo.md` als Launch-Checkliste ergaenzt.

## 2026-06-08 VPS-Deploy

Aktualisiert:

- Homepage-Stand nach GitHub gepusht: `5f0904e`.
- Statische Homepage-Dateien auf den VPS uebertragen.
- VPS-Ablage: `/opt/homepage_repo`.
- Next-Frontend-Static-Ablage: `/opt/nurovell-potential-analysis/frontend/public/homepage`.
- `nurovell_frontend` neu gebaut und gestartet.
- Live-Pfade geprueft:
  - `https://nurovelle.de/homepage/index.html`
  - `https://nurovelle.de/homepage/analyse.html`
- Root-Route `/` wurde nicht umgestellt.
- Keine Public-SSH-Freigabe.
- Keine Firewall-, Tunnel- oder Netzwerk-Aenderungen.

## 2026-06-08 Root-Aktivierung

Aktualisiert:

- Root `https://nurovelle.de/` leitet jetzt auf `/homepage/index.html`.
- `https://nurovelle.de/homepage/index.html` live mit HTTP 200 geprueft.
- `https://nurovelle.de/homepage/analyse.html` live mit HTTP 200 geprueft.
- `https://nurovelle.de/assets/hero/nurovelle_logo.png` live mit HTTP 200 geprueft.
- `https://nurovelle.de/results/<analysis_id>` bleibt erreichbar.
- Aenderung erfolgte nur im Frontend-Container.
- Keine Public-SSH-Freigabe.
- Keine Firewall-, Tunnel- oder Netzwerk-Aenderungen.
