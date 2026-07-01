# Aktueller Stand – Nurovelle Homepage / Assets

Stand: 2026-06-30

## Geprüft

- Projektdateien wurden als aktuelle Arbeitskopien zusammengestellt.
- Der bestehende Startseiten-Brief bleibt die Übergabegrundlage für HTML/CSS/JS.
- Header, Footer, Seitenleiste und Formular/Kontakt werden aus dem Bestand übernommen.
- Asset-Liste existiert separat und wird nicht vollständig in den Brief dupliziert.
- Workflow-Modultabelle liegt als Excel-Datei bei.

## Aktuelle Designentscheidungen

### Goldverläufe

- Goldverlauf 3 ist Hauptverlauf für CTAs.
- Goldverlauf 2 ist Hauptverlauf für Titel.
- Goldverlauf 1 ist Hauptverlauf für Rahmen.

Goldverlauf 1:

```text
#AE8625, #F7EF8A, #D2AC47, #EDC967
```

Goldverlauf 2:

```text
#DFBD69, #926F34
```

Goldverlauf 3:

```text
#F9F295, #E0AA3E, #FAF398, #B88A44
```

Alternativer Gold-Textverlauf für Content-/Dokument-Highlights:

```css
background: linear-gradient(135deg, #C5A059 0%, #FDF0CD 50%, #D4AF37 100%);
```

### Dunkelgrüne / Smaragd-Verläufe

Variante 1 – Deep Obsidian Green:

```css
background: linear-gradient(135deg, #0A1913 0%, #112A20 50%, #1D4234 100%);
```

Variante 2 – Midnight Teal-Emerald:

```css
background: linear-gradient(180deg, #071412 0%, #163A35 100%);
```

### Content-Dokumente

- H1: Bebas Neue, Bold, All Caps, ca. 26 pt, Gold Gradient / Fallback `#D4AF37`.
- H2: Plus Jakarta Sans, Semi-Bold, ca. 18 pt, Deep Emerald Green `#112A20`.
- H3: Plus Jakarta Sans, Medium, ca. 14 pt, Muted Matte Gold `#B38F4D`.
- H4: Plus Jakarta Sans, Bold, All Caps, ca. 10.5 pt, Deep Emerald Green `#112A20`.
- Column Header: Inter Bold, All Caps, ca. 10 pt, White `#FFFFFF` auf Emerald Block `#112A20`.
- Body: Inter Regular, 10.5 pt, Zeilenabstand 1.4, Dark Charcoal `#2A2A2A`.
- Bulletpoint-Header: Plus Jakarta Sans Semi-Bold, 12 pt, Deep Emerald Green `#112A20`.
- Bulletpoints: Inter Regular, 10.5 pt, Text `#2A2A2A`, Bullet Dot Emerald.
- Nummerierung: Inter Regular, 10.5 pt, Text `#2A2A2A`, Zahlen Matte Gold.
- Hervorhebung normal: Inter Italic / Medium, 10.5 pt, Deep Emerald Green `#112A20`.
- Hervorhebung extrem: Inter Extra-Bold, 10.5 pt, Dark Bronze-Gold `#A37A3E`.

## Hero-Formen / Bildgenerierung

Aktueller Status:

- Nicht final abgeschlossen.
- Nur einzelne Formen waren brauchbar.
- Weitere freie Bildgenerierung wurde gestoppt, weil wiederholt neue Formen/Stile entstanden sind.

Verbindliche Regeln, falls Hero-Formen erneut erstellt werden:

- Keine neuen Formen erfinden.
- Nur vorhandene Formen aus der freigegebenen Übersicht verwenden.
- Keine Weiterentwicklung und kein Redesign.
- Eine Form pro Produktionsdatei, hohe Auflösung.
- Form, Proportionen und Designsprache bleiben identisch.
- Objekte freischwebend.
- Kein Sockel, keine Plattform, keine Bodenplatte, keine Auflagefläche.
- Nodes und technische Linien bleiben rund um das Objekt im Raum, nicht nur am Boden.
- Smaragdgrün dezent ergänzen.
- Gold nur als dezente Akzente an Ecken/Knotenpunkten, nicht als durchgehende Goldkanten.
- Kein Gold als Hauptfläche.

## 3D-Icons / Workflow-Module

Aktueller Status:

- Es liegen 3D-Icon-Formen vor, die perspektivisch und als Serie grundsätzlich brauchbar wirken.
- Finaler Nurovelle-Farbstil ist noch nicht geprüft.
- Es existiert noch kein verlässlich freigegebenes Test-Icon in finaler Farbe.
- Keine Aussage über Veredelung, Premium-Finish oder Serienfähigkeit, bevor ein Farbtest bestanden ist.

Nächster Schritt:

- Ein einzelnes Icon in Photoshop CS6 farblich testen.
- Nur Farbtest, keine Stiländerung, keine Veredelung.
- Form bleibt unverändert.

Farbmapping für ersten Test:

| Ausgangsfarbe | Zielfarbe |
|---|---|
| Blau / Lila | Anthrazit / Gunmetal |
| Orange / Gelb | Gold |
| Hellblau / Grün | Smaragdgrün |
| Weiß / Hellgrau | Weiß / Silber oder dunkles Metall, je nach Funktion |

## Nicht geändert

- Projektdateien wurden nicht am Original überschrieben, sondern als aktueller Download-Stand neu zusammengestellt.
- Bestehende Asset-Liste wurde nicht dupliziert.
- Bestehende Formularlogik wurde nicht geändert.
- Bestehende Download-/Datenschutz-/Impressumslogik wurde nicht neu konzipiert.
