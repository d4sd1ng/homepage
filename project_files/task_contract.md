# Homepage Task Contract – Nurovelle

## Ziel dieses Dokuments

Dieses Dokument definiert, was die Homepage leisten muss und was nicht gebaut wird.

## Hauptaufgabe

Die Homepage führt Besucher zur Anfrage einer kostenlosen KI-Potenzialanalyse.

## Arbeitsregeln

- Project-Files sind Pflicht.
- Keine frei erfundenen Inhalte.
- Keine alten Branchenlisten verwenden.
- Keine alten Service-Listen verwenden.
- Branchen und Services bleiben getrennt.
- Card-Bilder bleiben textfrei.
- Card-Texte werden separat im HTML gesetzt.
- Änderungen erfolgen sektionweise.
- Layout wird nur auf ausdrückliche Anweisung geändert.

## Definition of Done

Die Homepage ist fertig, wenn folgende Punkte erfüllt sind:

- Startseite ist vollständig strukturiert
- Hero-Bereich hat klare Headline, Subline und CTA
- Nutzen ist verständlich erklärt
- Zielgruppe ist klar benannt
- Leistungsbereiche sind sichtbar
- finale Branchenliste ist korrekt eingebunden
- finale Services sind korrekt eingebunden
- Ablauf ist einfach erklärt
- Leadformular ist eingebunden
- Whitepaper-CTA ist vorhanden
- SEO-Sektion ist vorhanden
- Download-Bereich ist namentlich vorbereitet
- Datenschutzlink ist vorhanden
- Impressumlink ist vorhanden
- Seite funktioniert auf Desktop und Mobil
- keine Platzhaltertexte mehr vorhanden
- keine veralteten Branchen- oder Servicebegriffe mehr vorhanden

Hinweis fuer Download-Bereich:

- Download-Karten duerfen vor finaler Freigabe als Platzhalter sichtbar sein.
- Unfertige Dokumente aus `G:\Projects\Dokumente_lead` duerfen nicht auf die Homepage kopiert werden.
- Sobald finale Dokumente vorhanden sind, werden nur die finalen Dateien verlinkt.

## Finale Branchen

1. Energie & Versorgung
2. Finanzen & Versicherung
3. Industrie & Produktion
4. Verwaltung & HR
5. Marketing & Vertrieb
6. Gesundheitswesen & Pflege
7. Bildung & Forschung
8. Dienstleistung & KMU
9. Sonstige Branchen

## Finale Services

1. Verbrauchsdaten & Betriebsberichte automatisieren
2. Beleg-, Vertrags- & Risikoprüfung automatisieren
3. Produktionsdaten & Qualitätsprozesse automatisieren
4. Dokumentenabläufe & Personalprozesse automatisieren
5. Lead-, Content- & Vertriebsprozesse automatisieren
6. Formular-, Termin- & Dokumentationsabläufe automatisieren
7. Wissens-, Lern- & Forschungsdaten strukturieren
8. Kundenkommunikation & interne Abläufe automatisieren
9. Individuelle Prozessanalyse & Automatisierung

## Fokus

Priorität hat Conversion.

Design unterstützt den Inhalt. Design ersetzt keinen klaren Text.

## Nicht Teil dieser Version

- Loginbereich
- Kundenportal
- komplexes Dashboard
- SaaS-Abrechnung
- Blog-System
- Newsletter-Archiv
- mehrsprachige Website
- vollständiges CRM
- eigene Authentifizierung

## Technische Mindestanforderungen

- schnelle Ladezeit
- responsive Layout
- saubere Sections
- klare CTA-Buttons
- Formularweiterleitung oder Formularspeicherung
- Potenzialanalyse-Formular nutzt den produktiven Nurovelle-Analyse-Flow
- keine lokale Fake-Auswertung fuer Analyse-Ergebnisse
- Tracking optional
- SEO-Grundstruktur

## SEO- und Download-Regeln

SEO-Sektion:

- Inhalte werden aus `Landing_pages/` abgeleitet.
- Karten muessen stabile IDs behalten.
- `data-landing-source` dokumentiert die jeweilige Quell-Datei.
- Karten duerfen bis zur finalen Detailseiten-Entscheidung auf die Potenzialanalyse zeigen.

Download-Sektion:

- Vor finaler Dokumentfreigabe keine Download-Dateien hinterlegen.
- Karten nutzen stabile `data-download-key` Werte.
- Sichtbarer Status bleibt `In Vorbereitung`, solange kein finales Asset existiert.
- Spaetere finale Downloads sollen ohne Layout-Umbau ergaenzt werden.

## Potenzialanalyse-Integration

Die statische Homepage darf keine Scores selbst berechnen.

Verbindlicher Flow fuer `homepage/analyse.html`:

1. `GET https://nurovelle.de/api/v1/questions?industry=<industry>&tier=basic&include_risk=false`
2. `POST https://nurovelle.de/api/v1/analysis/start`
3. `POST https://nurovelle.de/api/v1/analysis/<analysis_id>/answers`
4. `POST https://nurovelle.de/api/v1/analysis/<analysis_id>/score`
5. `POST https://nurovelle.de/api/v1/analysis/<analysis_id>/report`
6. `POST https://nurovelle.de/api/v1/lead`
7. Link zu `https://nurovelle.de/results/<analysis_id>`

Das Formular darf kompakt bleiben. Die vollstaendige Fragen-/Score-Logik bleibt
im Analyse-Backend.

Lead-/Nurturing-Regel:

- Kontakt wird nach erfolgreichem Report als Lead gespeichert.
- Newsletter/Nurturing wird nur bei aktiver Checkbox als Opt-in gesendet.
- Notion und E-Mail-Versand werden nicht direkt aus der Homepage aufgerufen.
- Notion/Newsletter bleiben Backend-/Worker-Aufgabe.

## Inhaltliche Mindestanforderungen

Die Homepage muss diese Fragen beantworten:

1. Was bietet Nurovelle an?
2. Für wen ist es gedacht?
3. Welches Problem wird gelöst?
4. Was bekommt der Kunde konkret?
5. Wie läuft der Prozess ab?
6. Warum ist das glaubwürdig?
7. Was soll der Besucher jetzt tun?
