# Aktueller Homepage-Ausführungsstand

Status: in Arbeit
Stand: 2026-07-10

Diese Datei dokumentiert den aktuellen freigegebenen Stand aus der laufenden Umsetzung. Sie dient als direkte Aktualisierung für die weitere Arbeit an der Nurovelle-Homepage.

## Vorrangregel

Die aktuelle ausdrücklich freigegebene Benutzervorgabe überschreibt ältere Reihenfolgen in Brief, Overview oder Zwischenständen.

Für die aktuelle Umsetzung gilt: Zwischen Hero und dem bisherigen Prozess-Einstieg wird eine neue About-Nurovelle-Section aufgenommen. Projektidee steht vor Potenzialanalyse. Die Potenzialanalyse kommt eine Sektion später.

## Aktuelle Startseiten-Reihenfolge

1. Hero
2. Über Nurovelle
3. Der erste Schritt zu Ihrem KI-Projekt
4. Sie haben bereits eine konkrete KI-Idee?
5. Kostenlose KI-Potenzialanalyse
6. KI-Leistungen von Nurovelle
7. Vom Geschäftsprozess zur KI-Lösung
8. Warum Nurovelle
9. Download-Bereich
10. Analyse-Seite / Formularweiterleitung
11. Success-/Error-Zustand in `analyse.html`

## Neue Section – Über Nurovelle

Position: direkt zwischen Hero und „Der erste Schritt zu Ihrem KI-Projekt“.

ID: `#about-nurovelle`

Layoutvorgabe:

- links Video- oder Video-Preview-Fläche
- rechts Text
- dunkle Nurovelle-Fläche, keine neue Farbwelt
- kein zusätzlicher Formularbereich
- CTA optional zu `analyse.html`, wenn die Section einen CTA erhält

Text:

```text
ÜBER NUROVELLE
KI-LÖSUNGEN, DIE IN REALEN PROZESSEN FUNKTIONIEREN

Nurovelle entwickelt individuelle KI-Systeme, die sich an konkreten Geschäftsprozessen orientieren. Wir analysieren bestehende Abläufe, identifizieren sinnvolle Potenziale und setzen Lösungen um, die im Arbeitsalltag tatsächlich entlasten.

PROZESSE VERSTEHEN
Bestehende Abläufe, Engpässe und manuelle Arbeitsschritte werden systematisch analysiert.

POTENZIALE ERKENNEN
Wir prüfen, wo KI, Automatisierung oder intelligente Datenverarbeitung einen echten Nutzen schaffen.

INDIVIDUELL ENTWICKELN
Lösungen werden passend zu den vorhandenen Systemen, Anforderungen und Arbeitsweisen konzipiert.

NACHHALTIG INTEGRIEREN
Das Ergebnis sind nutzbare KI-Systeme, die Prozesse vereinfachen und langfristig weiterentwickelt werden können.
```

## Aktuelle Divider-Testabfolge

Diese Abfolge ist ausdrücklich testweise. Sie ist keine finale Festlegung des später zu verwendenden Dividers.

1. Hero → Section 2 „Über Nurovelle“: Divider A – SVG-Schräg-Divider / Separator
2. Section 2 „Über Nurovelle“ → Section 3 „Der erste Schritt zu Ihrem KI-Projekt“: Divider A erneut
3. Section 3 „Der erste Schritt zu Ihrem KI-Projekt“ → Section 4 „Sie haben bereits eine konkrete KI-Idee?“: Divider B normal
4. Section 4 „Sie haben bereits eine konkrete KI-Idee?“ → Section 5 „Kostenlose KI-Potenzialanalyse“: Divider B reverse
5. Section 5 „Kostenlose KI-Potenzialanalyse“ → Section 6 „KI-Leistungen von Nurovelle“: Divider C

## Bedeutung für die Umsetzung

- Variante A muss zweimal direkt nacheinander gezeigt werden.
- Dadurch wird sichtbar, wie der SVG-Schräg-Divider über aufeinanderfolgende Sections wirkt.
- Danach werden B normal, B reverse und C als weitere Prüfvarianten gezeigt.
- Erst nach Live-Sichtprüfung wird festgelegt, welcher Divider tatsächlich verwendet wird.
- Keine der Prüfvarianten ist durch diese Abfolge final ausgewählt.

## Weiterhin verbindlich

- keine zusätzlichen Sections ohne Auftrag
- keine Textkürzung ohne Auftrag
- keine Layoutänderung ohne Auftrag
- keine neuen Farben
- keine Demo-Farben aus Referenzen
- keine Bild-, GIF- oder Video-Divider
- keine Verzerrung von Text, Cards, CTAs oder Hero-Visuals
- alle Potenzialanalyse-, Anfrage- und Erstgespräch-CTAs führen zu `analyse.html`
- Download-CTAs führen zu `#downloads` oder `praxisleitfaden.html`
