Bonus-Ressource 2.1: Modell-Register-Vorlage (Excel)
Dateiname: Modell-Register-Vorlage.xlsx
Zweck: Zentrale Verwaltung aller KI-Modelle im Marketing

Tabellenblatt 1: "Aktive Modelle"
Spalte A	B	C	D	E	F	G	H	I	J
Modell-ID	Modellname	Einsatzzweck	Kanal	Trainingsdatum	Letzter Retraining	Nächster Retraining	Aktuelle AUC	AUC bei Training	Status
M-001	Lead-Scoring Q1	Lead-Priorisierung	E-Mail	15.01.2025	15.01.2025	15.04.2025	0,78	0,81	Aktiv
M-002	Churn-Prevention	Kündigungsrisiko	CRM	01.02.2025	01.02.2025	01.05.2025	0,72	0,74	Aktiv
M-003	Produktempfehlung	Cross-Selling	Website	10.03.2025	10.03.2025	10.06.2025	0,85	0,84	Aktiv
-	-	-	-	-	-	-	-	-	-
Bedingte Formatierung:

Spalte J (Status):

Grün bei "Aktiv"

Gelb bei "Beobachtung" (AUC-Abfall >0,05)

Rot bei "Inaktiv"

Spalte I (AUC aktuell vs. Training):

Grün wenn >= Training - 0.03

Gelb wenn < Training - 0.03 und >= Training - 0.08

Rot wenn < Training - 0.08

Formeln:

Spalte G (Nächster Retraining) = EDATE(F2, 3) (alle 3 Monate)

Tabellenblatt 2: "Retraining-Log"
Spalte A	B	C	D	E	F	G
Datum	Modell-ID	Grund für Retraining	Neue AUC	AUC vorher	Veränderung	Verantwortlich
15.04.2025	M-001	Geplanter Zyklus	0,82	0,78	+0,04	M. Schmidt
-	-	-	-	-	-	-
Formel Spalte F: =D2-E2

Tabellenblatt 3: "Modell-Features"
Spalte A	B	C	D	E
Modell-ID	Feature-Name	Feature-Typ	Datenquelle	Erlaubt für Vorhersage?
M-001	days_since_last_open	numerisch	E-Mail-Tool	Ja
M-001	email_click_rate_7d	numerisch	E-Mail-Tool	Ja
M-001	total_visits_30d	numerisch	Web-Analytics	Ja
M-001	source_channel	kategorial	CRM	Ja
M-001	age	numerisch	CRM	Nein (Bias-Risiko)
Tabellenblatt 4: "Eskalationsregeln"
Spalte A	B	C	D
Modell-ID	Auslöser	Aktion	Zuständig
Alle	AUC fällt um >0,1	Automatische Benachrichtigung an Data Scientist	Data Scientist
Alle	AUC fällt um >0,15 nach Benachrichtigung	Modell deaktivieren, fallback auf Regel	Head of Marketing
M-001	Kein Retraining nach 4 Monaten	Manueller Check durch Marketing Ops	Marketing Ops
Bonus-Ressource 2.2: RACI-Matrix-Vorlage (Excel)
Dateiname: RACI-Matrix-KI-Marketing.xlsx

Tabellenblatt 1: "RACI-Matrix"
Spalte A	B	C	D	E	F	G
Aktivität / Schritt	Data Engineer	Data Scientist	Marketing Analyst	Campaign Manager	Head of Marketing	Legal
1. Datenbereitstellung	R	C	C	I	A	I
2. Feature-Engineering	C	C	R	C	A	I
3. Modelltraining	I	R	C	I	A	I
4. Validierung & Test	I	R	C	I	A	I
5. Bias-Check	I	C	R	I	A	C
6. Schwellwert-Definition	I	C	C	R	A	I
7. Kampagnen-Integration	C	I	R	C	A	I
8. Performance-Monitoring	I	C	R	I	I	I
9. Retraining	I	R	C	I	A	I
10. Deaktivierung bei Fehler	C	R	C	C	A	I
Legende:

R = Responsible (führt aus)

A = Accountable (genehmigt, trägt Verantwortung)

C = Consulted (wird konsultiert)

I = Informed (wird informiert)

Bedingte Formatierung: Jede Zelle mit R = gelber Hintergrund, A = roter Hintergrund

Tabellenblatt 2: "Rollen-Beschreibungen"
Spalte A	B
Rolle	Beschreibung
Data Engineer	Baut und wartet Datenpipelines, stellt Datenqualität sicher
Data Scientist	Trainiert Modelle, führt Retraining durch, überwacht Performance
Marketing Analyst	Erstellt Features, bereitet Daten für Modell vor, führt Bias-Checks durch
Campaign Manager	Definiert Schwellwerte, integriert Modell in Kampagnen
Head of Marketing	Genehmigt neue Modelle, entscheidet über Budget, ist verantwortlich für Compliance
Legal	Prüft DSGVO-Konformität, genehmigt automatisierte Entscheidungen nach Art. 22
Bonus-Ressource 2.3: ROI-Rechner für KI-Marketing (Excel)
Dateiname: ROI-Rechner-KI-Marketing.xlsx

Tabellenblatt 1: "ROI-Berechnung"
Eingabebereich (gelbe Zellen):

Spalte A	Spalte B	Einheit
Vorher: Conversion Rate	10	%
Nachher: Conversion Rate	18	%
Kontaktierte Leads pro Monat	500	Anzahl
Durchschnittlicher Dealwert	5.000	€
Zusätzlicher Umsatz (monatlich)	=((B2-B1)/100*B3)*B4	€
- Zurechnungsfaktor (KI-Anteil)	80	%
Zurechenbarer Zusatzumsatz	=B6*B7/100	€
Kosten (gelbe Zellen):

Spalte A	Spalte B	Einheit
Einmalige Kosten (Entwicklung)	24.000	€
Monatliche Lizenzkosten	500	€
Monatliche Cloud-Kosten	200	€
Monatliche Personalkosten (Monitoring)	200	€
Gesamt monatliche Kosten	=B11+B12+B13	€
Gesamtkosten (12 Monate)	=B10+(B14*12)	€
Ergebnisse (automatisch berechnet):

Spalte A	Spalte B	Formel
Jährlicher Nutzen	=B8*12	€
ROI (12 Monate)	=((B18-B15)/B15)*100	%
Amortisationszeit (Monate)	=B10/(B8-B14)	Monate
NPV (Net Present Value)	=B18-B15	€
Bedingte Formatierung:

ROI >100 %: grüner Hintergrund

ROI 0–100 %: gelber Hintergrund

ROI <0 %: roter Hintergrund

Tabellenblatt 2: "Szenarien-Vergleich"
Szenario	Conversion Rate	Zusatzumsatz	ROI	Amortisation
Optimistisch	20 %	-	-	-
Realistisch	15 %	-	-	-
Pessimistisch	12 %	-	-	-
(Alle Werte ziehen sich aus den Eingaben des ersten Blatts oder können manuell überschrieben werden)

Bonus-Ressource 2.4: Bias-Check-Checkliste (Excel)
Dateiname: Bias-Check-Checkliste.xlsx

Tabellenblatt 1: "Bias-Check vor Go-Live"
Spalte A	B	C	D
Check	Ergebnis	Verantwortlich	Datum
1. Datengrundlage			
1.1 Wurden historische Daten auf verzerrte Repräsentation geprüft?	☐ Ja / ☐ Nein	-	-
1.2 Sind alle relevanten Kundensegmente in den Trainingsdaten vertreten?	☐ Ja / ☐ Nein	-	-
1.3 Enthalten die Daten geschützte Merkmale (Alter, Geschlecht, Ethnie, Religion)?	☐ Ja / ☐ Nein	-	-
2. Feature-Prüfung			
2.1 Wurden geschützte Merkmale aus dem Training entfernt?	☐ Ja / ☐ Nein / ☐ Nicht zutreffend	-	-
2.2 Gibt es Proxy-Features (z. B. Postleitzahl als Ersatz für Ethnie)?	☐ Ja / ☐ Nein	-	-
2.3 Sind die Features für alle Segmente gleichermaßen aussagekräftig?	☐ Ja / ☐ Nein	-	-
3. Performance nach Segment			
3.1 AUC für Segment A (z. B. Bestandskunden)	___	-	-
3.2 AUC für Segment B (z. B. Neukunden)	___	-	-
3.3 Differenz zwischen Segmenten	___ (sollte <0,1 sein)	-	-
3.4 False Positive Rate für Segment A	___ %	-	-
3.5 False Positive Rate für Segment B	___ %	-	-
3.6 Differenz der FPR	___ % (sollte <10 % sein)	-	-
4. Entscheidung			
4.1 Modell ist frei von signifikantem Bias	☐ Ja / ☐ Nein	-	-
4.2 Bei Bias: Dokumentation und Begründung liegt vor	☐ Ja / ☐ Nein / ☐ Nicht zutreffend	-	-
4.3 Freigabe durch Head of Marketing	☐ Ja / ☐ Nein	-	-
4.4 Freigabe durch Legal/Compliance (falls erforderlich)	☐ Ja / ☐ Nein / ☐ Nicht zutreffend	-	-
Freigabe-Datum: __________
Unterschrift (Head of Marketing): __________

Tabellenblatt 2: "Bias-Dokumentation bei Auffälligkeit"
Spalte A	B
Betroffenes Segment	-
Art des Bias (z. B. niedrigere AUC, höhere FPR)	-
Ursache (vermutet)	-
Geschäftliche Begründung für dennoch Go-Live	-
Maßnahmen zur Risikominimierung	-
Datum der nächsten Überprüfung	-
Bonus-Ressource 2.5: Retraining-Kalender-Vorlage (Excel)
Dateiname: Retraining-Kalender-Vorlage.xlsx

Tabellenblatt 1: "Retraining-Plan 12 Monate"
Spalte A	B	C	D	E	F
Modell-ID	Modellname	Jan	Feb	Mrz	Apr	Mai	Jun	Jul	Aug	Sep	Okt	Nov	Dez
M-001	Lead-Scoring	☐	☐	☐	□	□	□	□	□	□	□	□	□
M-002	Churn-Prevention	□	☐	□	□	□	□	□	□	□	□	□	□
M-003	Produktempfehlung	□	□	☐	□	□	□	□	□	□	□	□	□
Legende:

☐ = Retraining geplant

□ = kein Retraining

✓ (durchgestrichen) = Retraining durchgeführt

Bedingte Formatierung: Zellen mit ☐ werden 14 Tage vor Termin gelb, am Termin rot

Tabellenblatt 2: "Retraining-Log (detailliert)"
Spalte A	B	C	D	E	F	G	H
Datum	Modell-ID	Grund	Neue AUC	AUC vorher	Veränderung	Neue Features hinzugefügt?	Verantwortlich
-	-	Geplant / Drift / Neue Daten / Sonstiges	-	-	-	Ja / Nein	-
Tabellenblatt 3: "Automated Retraining Pipeline" (Checkliste)
Spalte A	B
Automatisierungsschritt	Status (☐ Ja / ☐ Nein)
Datenextraktion automatisiert	☐
Feature-Engineering automatisiert	☐
Modelltraining automatisiert	☐
Validierung auf Testdaten automatisiert	☐
Performance-Vergleich mit Vorgängermodell	☐
Bei Verbesserung: automatisches Deployment	☐
Bei Verschlechterung: Benachrichtigung an Team	☐
Rollback-Funktion bei Fehlschlag	☐
Logging aller Retrainings	☐
Damit ist Schritt 2 (Bonus-Ressourcen) abgeschlossen.

Schritt 4: Weiteres Asset – 10 KI-Marketing-Tools im Vergleich + Checkliste: KI-ready Daten
Hier sind die zwei zusätzlichen Assets als Textvorlagen (können ebenfalls als PDF oder direkt in Guides eingebettet werden).

Asset 4.1: 10 KI-Marketing-Tools im Vergleich
Dateiname: 10-KI-Marketing-Tools-Vergleich.pdf
Umfang: ca. 1.200 Wörter

Einleitung: Die richtige Tool-Auswahl
Die Tool-Landschaft wächst rasant. Dieser Vergleich hilft Ihnen, basierend auf Ihrem Reifegrad (Guide 4) und Budget die passende Lösung zu wählen. Die Tools sind in vier Kategorien eingeteilt, die den Stufen aus Guide 2 entsprechen.

Kategorie 1: Eingebaute KI in bestehenden Tools (Stufe 1)
Tool	Kernfunktion	Marketing-Anwendung	Preis (ca.)	Vorteile	Nachteile
HubSpot Predictive Lead Scoring	Lead-Scoring	B2B-Vertrieb, Priorisierung	In Professional/Enterprise enthalten (ab 1.780 €/Monat)	Keine Extra-Kosten, sofort nutzbar	Black Box, kein Einfluss auf Features
Salesforce Einstein	Scoring, Empfehlungen, Sentiment	CRM-integrierte KI für Vertrieb & Marketing	In Enterprise Edition enthalten (ab 300 €/Nutzer/Monat)	Tiefe CRM-Integration	Teuer bei vielen Usern
Meta Advantage+	Kampagnen-Optimierung	Social Ads (Facebook/Instagram)	Keine extra Kosten (nur Ad-Budget)	Automatische Gebote & Zielgruppen	Kaum Kontrollmöglichkeiten
Google Ads Smart Bidding	Gebotsstrategien	SEA	Keine extra Kosten	Gut erforscht, zuverlässig	Benötigt viele Conversions für Training (>30/Monat)
Für wen geeignet: Kleine Teams, erster Einstieg, kein Data Scientist verfügbar.

Kategorie 2: Marketing-spezifische KI-Plattformen (Stufe 2)
Tool	Kernfunktion	Marketing-Anwendung	Preis (ca.)	Vorteile	Nachteile
Pecan.ai	Prädiktive Modelle (Churn, CLV, LTV)	E-Commerce, SaaS	1.500–5.000 €/Monat	Kein Coding, Marketing-Analysten können Modelle bauen	Teuer für kleine Teams
Albert.ai	Vollautomatische Kampagnenführung	Multi-Channel (Google, Facebook, etc.)	2.000–10.000 €/Monat	Setzt Budget selbstständig um	Sehr teuer, nicht transparent
Evolutionary	Creative-Testing	Anzeigenoptimierung	500–2.000 €/Monat	Testet tausende Kreativ-Varianten	Nur für große Ad-Budgets sinnvoll
Für wen geeignet: Mittelstand mit Marketing-Analysten, die keine Data Scientists haben.

Kategorie 3: Low-Code/No-Code AutoML (Stufe 3)
Tool	Kernfunktion	Marketing-Anwendung	Preis (ca.)	Vorteile	Nachteile
Akkio	AutoML für Marketing-Daten	Lead-Scoring, Churn, Prognosen	500–2.000 €/Monat	Sehr einfach, gute Export-Funktionen	Begrenzte Feature-Kontrolle
DataRobot	Enterprise AutoML	Komplexe Modelle	10.000–50.000 €/Jahr	Sehr mächtig, viele Algorithmen	Teuer, Bedienung komplexer
Obviously.ai	Automatisiertes Feature-Engineering	E-Commerce, B2B	600–2.500 €/Monat	Gute Interpretierbarkeit (Shapley-Werte)	Weniger bekannt, kleinere Community
Für wen geeignet: Teams mit Marketing-Analysten, die selbst Modelle bauen wollen, aber kein Python können.

Kategorie 4: Eigenentwicklung (Stufe 4)
Tool/Technologie	Kernfunktion	Marketing-Anwendung	Preis (ca.)	Vorteile	Nachteile
Python + scikit-learn	Eigene Modelle	Alles möglich	0 € (Open Source) + Entwicklerkosten	Vollste Kontrolle	Benötigt Data Scientist
TensorFlow / PyTorch	Deep Learning	Bilder, Text, komplexe Muster	0 € + Entwicklerkosten	State-of-the-art	Hohe Komplexität
MLflow / Kubeflow	MLOps-Pipelines	Modell-Governance, Retraining	0 € + Infrastrukturkosten	Reproduzierbarkeit	Setup-Aufwand hoch
Für wen geeignet: Große Unternehmen mit Data Science Team (>500 Mitarbeiter oder sehr datengetrieben).

Entscheidungsmatrix: Welches Tool passt zu Ihnen?
Ihr Profil	Monatliches Budget	Technische Kompetenz	Empfehlung
Soloselbständig, erstes KI-Experiment	<200 €	Niedrig	Eingebaute KI im vorhandenen Tool (HubSpot/Meta)
Kleines Team (2–5 Personen)	200–1.000 €	Mittel	Pecan.ai oder Akkio
Mittelstand (10–50 Personen)	1.000–5.000 €	Hoch (Marketing-Analyst)	DataRobot oder Obviously.ai
Enterprise (>100 Personen)	>5.000 €	Sehr hoch (Data Scientist)	Python + MLflow + eigene Entwicklung
Tool-Feature-Vergleich im Detail
Feature	HubSpot	Pecan	Akkio	DataRobot	Eigenentwicklung
Kein Coding nötig	✅	✅	✅	⚠️ (teilweise)	❌
Eigene Features definierbar	❌	⚠️ (begrenzt)	⚠️	✅	✅
Interpretierbarkeit (warum?)	❌	⚠️	✅	✅	✅
DSGVO-konform	✅	✅	✅	✅	✅ (wenn richtig umgesetzt)
Export in CRM/Marketing-Tools	✅	✅	✅	✅	⚠️ (selbst bauen)
Automatisches Retraining	❌	⚠️	⚠️	✅	✅
Monatliche Mindestkosten	Inkl.	1.500 €	500 €	800 €	2.000 € (Personal)
Fazit Tools
Für den ersten Pilot: Nutzen Sie die eingebaute KI Ihrer bestehenden Tools (HubSpot, Salesforce, Meta, Google). Das Risiko ist null, der Lerngewinn hoch.

Für Skalierung mit kleinen Teams: Pecan.ai oder Akkio bieten das beste Preis-Leistungs-Verhältnis.

Für Enterprise mit eigenen Data Scientists: Eigenentwicklung mit Python + scikit-learn, orchestriert mit MLflow.

Asset 4.2: Checkliste: KI-ready Daten
Dateiname: Checkliste-KI-ready-Daten.pdf
Umfang: ca. 800 Wörter
Format: Checkliste zum Abhaken (PDF mit Checkboxen)

Einleitung: Datenqualität entscheidet
Bevor Sie ein KI-Modell trainieren, muss Ihre Datenbasis stimmen. Diese Checkliste hilft Ihnen, den KI-readiness-Grad Ihrer Marketing-Daten zu bestimmen. Jede Frage mit "Ja" zu beantworten ist die Voraussetzung für ein erfolgreiches KI-Projekt.

Ziel: 20–30 Minuten Aufwand. Beantworten Sie alle Fragen ehrlich – lieber jetzt Lücken identifizieren als später im Modell.

Teil 1: Datenverfügbarkeit (10 Fragen)
Nr.	Frage	Status (☐ Ja / ☐ Nein)	Anmerkung
1.1	Haben Sie mindestens 12 Monate historische Daten?	☐	Je mehr, desto besser. Minimum: 6 Monate
1.2	Haben Sie mindestens 1.000 positive Events (z. B. Käufe, Conversions)?	☐	Für stabile Modelle werden 1.000+ Ereignisse empfohlen
1.3	Sind Ihre Daten in einer zentralen Datenbank oder einem Data Warehouse?	☐	Excel-Tabellen zählen nicht als zentral
1.4	Haben Sie eine eindeutige Customer-ID über alle Kanäle hinweg?	☐	Cookie, E-Mail, User-ID müssen zusammengeführt werden können
1.5	Sind Ihre Ereignisse (Öffnungen, Klicks, Käufe) mit Zeitstempeln versehen?	☐	Format: YYYY-MM-DD HH:MM:SS
1.6	Haben Sie Zugriff auf Rohdaten (nicht nur aggregierte Reports)?	☐	Reports sind bereits verdichtet – für KI brauchen Sie die Detaildaten
1.7	Können Sie auf Daten aus mindestens zwei verschiedenen Kanälen zugreifen?	☐	E-Mail + Web + CRM ergibt bessere Modelle
1.8	Haben Sie negative Events dokumentiert (z. B. Abbruch, keine Conversion)?	☐	Modelle brauchen sowohl Ja- als auch Nein-Fälle
1.9	Gibt es dokumentierte Datenquellen (wer liefert was, wie oft)?	☐	Nur was dokumentiert ist, kann genutzt werden
1.10	Fehlen systematisch Daten für bestimmte Kundengruppen?	☐	(Wenn ja: Bias-Risiko)
Auswertung Teil 1:

8–10 Ja: ✅ Datenverfügbarkeit ist gut

5–7 Ja: ⚠️ Verbesserungsbedarf – priorisieren Sie die "Nein"-Punkte

0–4 Ja: ❌ Nicht KI-ready – beginnen Sie mit Datenkonsolidierung

Teil 2: Datenqualität (10 Fragen)
Nr.	Frage	Status (☐ Ja / ☐ Nein)	Anmerkung
2.1	Sind Ihre kategorialen Felder einheitlich formatiert (z. B. "DE" nicht "Germany")?	☐	Inkonsistenzen führen zu fehlerhaften Modellen
2.2	Liegt der Anteil fehlender Werte unter 5 % pro Feld?	☐	Bei mehr als 5 % müssen Sie sinnvoll imputieren
2.3	Gibt es Duplikate in Ihrer Kundendatenbank (<2 %)?	☐	Doppelte Profile verzerren das Training
2.4	Haben Sie ein Verfahren zur Identitätsauflösung (Identity Resolution)?	☐	Gleicher Kunde mit E-Mail vs. Cookie muss erkannt werden
2.5	Sind Ihre Daten frei von systematischen Fehlern (z. B. immer 0 bei bestimmten Feldern)?	☐	Stichprobenartige Plausibilitätsprüfung durchführen
2.6	Werden Ihre Daten regelmäßig (z. B. monatlich) auf Qualität geprüft?	☐	Wenn nicht: Führen Sie eine Qualitätsroutine ein
2.7	Gibt es eine dokumentierte Data-Governance (wer darf was ändern)?	☐	Vermeidet chaotische Änderungen
2.8	Stimmen Zeitstempel mit der Zeitzone Ihrer Kunden überein?	☐	Sonst sind Tageszeit-Muster falsch
2.9	Sind Ihre Daten aktuell (letzte Aktualisierung innerhalb 24 h)?	☐	Für Echtzeit-Modelle kritisch
2.10	Gibt es dokumentierte Ausnahmen/Regeln für Sonderfälle (z. B. Testkunden)?	☐	Testdaten müssen aus Training herausgefiltert werden
Auswertung Teil 2:

8–10 Ja: ✅ Datenqualität ist gut

5–7 Ja: ⚠️ Verbesserungsbedarf – bereinigen Sie vor dem ersten Pilot

0–4 Ja: ❌ Nicht KI-ready – Datenbereinigung ist Ihre erste Aufgabe (Guide 2)

Teil 3: Datenzugriff & Infrastruktur (5 Fragen)
Nr.	Frage	Status (☐ Ja / ☐ Nein)	Anmerkung
3.1	Können Sie auf Ihre Daten per SQL oder API zugreifen?	☐	Manueller CSV-Export ist zu langsam für iterative Entwicklung
3.2	Haben Sie eine Testumgebung (von Produktionsdaten getrennt)?	☐	Training niemals auf Produktionsdaten durchführen
3.3	Können Sie Daten pseudonymisieren (DSGVO-konform)?	☐	Für Training mit externen Tools notwendig
3.4	Gibt es einen dokumentierten Datenaktualisierungs-Prozess?	☐	Wer lädt wann neue Daten?
3.5	Haben Sie Backup- und Wiederherstellungsprozesse für Ihre Daten?	☐	Datenschutz und Business Continuity
Auswertung Teil 3:

4–5 Ja: ✅ Infrastruktur ist ausreichend

2–3 Ja: ⚠️ Engpass – priorisieren Sie Zugriffsautomatisierung

0–1 Ja: ❌ Nicht KI-ready – zu manuelle Prozesse

Teil 4: DSGVO & Compliance (5 Fragen – zwingend!)
Nr.	Frage	Status (☐ Ja / ☐ Nein)	Anmerkung
4.1	Haben Sie eine Rechtsgrundlage für die Verarbeitung zu KI-Zwecken (Art. 6 DSGVO)?	☐	Ohne Rechtsgrundlage kein KI-Training
4.2	Informieren Sie Ihre Kunden über automatisierte Entscheidungen (Art. 13–14 DSGVO)?	☐	Pflicht bei Scoring-Systemen
4.3	Können Sie auf Anfrage erklären, welche Daten Ihr Modell nutzt (Auskunftsanspruch)?	☐	Sie müssen die Logik erläutern können (kein Code, aber Features)
4.4	Haben Sie einen Prozess für Löschanträge (Recht auf Vergessenwerden)?	☐	Daten müssen auch aus Trainingsdatensätzen entfernt werden können
4.5	Führen Sie eine Datenschutz-Folgenabschätzung (DSFA) bei hohen Risiken durch?	☐	Erforderlich bei Scoring mit Rechtsfolgen (z. B. Bonität)
Auswertung Teil 4:

5 Ja: ✅ DSGVO-konform

1–4 Ja: ⚠️ Handlungsbedarf – konsultieren Sie Legal vor Go-Live

0 Ja: ❌ Nicht KI-ready – rechtliche Grundlagen zuerst klären

Gesamtauswertung: Ihr KI-readiness Score
Punktevergabe:

Teil 1: 10 Punkte möglich

Teil 2: 10 Punkte möglich

Teil 3: 5 Punkte möglich

Teil 4: 5 Pflichtpunkte (müssen alle erfüllt sein)

Gesamtpunktzahl	Bewertung	Handlungsempfehlung
25–30	🟢 KI-ready	Sie können sofort mit Guide 3 starten
18–24	🟡 Bedingt KI-ready	Beheben Sie die offenen Punkte aus Teil 1–3 (2–4 Wochen Aufwand)
10–17	🟠 Nicht KI-ready	Datenstrategie priorisieren (Guide 2 als Fahrplan nutzen)
0–9	🔴 Weit entfernt	Beginnen Sie mit einer Dateninventur und einem ersten Cleanup-Projekt
Zwingende Bedingung: Teil 4 muss 5/5 Punkte haben – sonst kein Go-Live, unabhängig vom Gesamtscore.

Sofortmaßnahmen (die erste Woche)
Die drei einfachsten Hebel:

Identifizieren Sie die Quelle mit den meisten fehlenden Werten und bereinigen Sie sie

Standardisieren Sie kategoriale Felder in einem Kanal (z. B. CRM)

Richten Sie einen wöchentlichen Datenqualitäts-Check ein (15 Minuten)

Die drei häufigsten Fehler, die Sie heute beheben können:

Doppelte Kundendatensätze zusammenführen

Fehlende Zeitstempel ergänzen

Test- und Systemdaten aus dem Analysedatensatz entfernen

Dokumentation für nächste Woche:

Erstellen Sie eine Liste aller Datenquellen mit Kontaktperson

Notieren Sie drei spezifische KI-Anwendungen, die Sie umsetzen wollen

Prüfen Sie Teil 4 mit Ihrer Legal-Abteilung