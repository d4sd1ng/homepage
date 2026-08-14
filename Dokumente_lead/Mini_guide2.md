Mini-Guide 2: Daten & Technologie für KI-gestütztes Marketing
1. Warum Daten vor Algorithmen kommen
Guide 1 endete mit der Feststellung: KI ist keine Magie. Der häufigste Grund für scheiternde KI-Projekte im Marketing ist nicht die falsche Technologie, sondern schlechte Datenqualität. Bevor Sie über Modelle nachdenken, müssen Sie Ihre Datenlandschaft verstehen.

Die harte Wahrheit: Ein einfaches lineares Regressionsmodell mit sauberen, relevanten Daten schlägt regelmäßig ein komplexes neuronales Netz mit chaotischen Daten. Dieses Prinzip heißt im Fachjargon "Garbage in, garbage out" – und es gilt im Marketing strenger als in fast jeder anderen Domäne, weil Kundendaten extrem anfällig für Inkonsistenzen sind (doppelte Profile, unterschiedliche E-Mail-Schreibweisen, fehlende Timestamps).

2. Das Daten-Ökosystem für Marketing-KI
Ein KI-taugliches Marketing-Daten-Ökosystem besteht aus fünf Schichten:

Schicht 1: Ereignisdaten (Event Data)
Das Herzstück: Jede Interaktion mit Zeitstempel, Kanal, User-ID und Aktion. Beispiele: E-Mail-Öffnung, Seitenaufruf, Abbruch im Checkout, Klick auf Anzeige. Ohne saubere Ereignisdaten ist prädiktive KI unmöglich.

Schicht 2: Masterdaten (Customer Master)
Die stabile Identität eines Kunden: Eindeutige ID, demografische Merkmale, Segmentzugehörigkeit, Opt-in-Status. Kritisch ist die Identitätsauflösung (Identity Resolution): Kann Ihr System denselben Kunden über E-Mail, Cookie und App-ID erkennen?

Schicht 3: Transaktionsdaten
Wertschöpfende Aktionen: Bestellungen, Abos, Upgrades, Retouren. Diese Daten sind besonders wertvoll für CLV-Berechnungen und Churn-Modelle.

Schicht 4: Verhaltensdrittdaten (optional)
Angereicherte Daten von externen Plattformen (z. B. Wetterdaten für Outdoor-Produkte, Börsenindizes für Finanzmarketing). Diese erhöhen die Vorhersagekraft signifikant, aber nur wenn sie konsistent mit Ihren Ereignisdaten verbunden werden können.

Schicht 5: Feedbackdaten
Die wichtigste, aber am häufigsten übersehene Schicht: War eine KI-Vorhersage richtig? Hat der Kunde gekauft oder nicht? Diese Daten trainieren Ihre Modelle kontinuierlich nach.

3. Datenqualitätskriterien für KI
Prüfen Sie Ihre Daten anhand dieser vier Dimensionen – kein Kompromiss:

Kriterium	Frage	Typisches Marketing-Problem
Vollständigkeit	Fehlen bei 30 % der Kunden das Feld "Branche"?	Unvollständige Formulare, fehlende UTM-Parameter
Konsistenz	Ist "DE" gleich "Deutschland" gleich "Germany"?	Unterschiedliche Länderkodierungen in CRM vs. Newsletter-Tool
Genauigkeit	Stimmt der Zeitstempel der Conversion mit dem tatsächlichen Kaufzeitpunkt überein?	Batch-Prozesse, die Conversions verzögert schreiben
Aktualität	Wann wurde das letzte Mal ein Profil aktualisiert?	Veraltete Firmengrößen in B2B-Datenbanken
Praktische Empfehlung: Beginnen Sie mit einem Data Audit auf einem einzelnen Kanal (z. B. E-Mail-Marketing). Bereinigen Sie dort explizit doppelte Profile und standardisieren Sie Felder – das reicht für erste KI-Piloten.

4. Technologieoptionen im Überblick
Nicht jede KI-Lösung erfordert eine eigene Data Science-Abteilung. Die Wahl hängt von Ihrer Datenreife und internen Kompetenz ab:

Stufe 1: Eingebaute KI in bestehenden Tools (Low Entry)
Beispiele: HubSpot’s Predictive Lead Scoring, Salesforce Einstein, Meta’s Advantage+ Shopping

Vorteile: Keine eigene Infrastruktur, nutzt Ihre vorhandenen Daten

Nachteile: Black Box (keine Einsicht in Modelllogik), wenig Anpassung

Geeignet für: Erste Gehversuche, kleine Marketingteams

Stufe 2: Marketing-spezifische KI-Plattformen
Beispiele: Pecan.ai, Albert.ai, Evolutionary

Vorteile: Vorgefertigte Modelle für typische Marketing-Cases (Churn, CLV, LTV), oft mit Explainability-Funktionen

Nachteile: Zusätzliche Lizenzkosten, benötigt saubere Daten-Integration

Geeignet für: Mittelständische Unternehmen mit Datenbank, aber ohne Data Scientist

Stufe 3: Low-Code/No-Code AutoML
Beispiele: DataRobot, Akkio, obviously.ai

Vorteile: Marketing-Analysten können eigene Modelle bauen ohne Python

Nachteile: Benötigt Verständnis für Feature Engineering und Validierung

Geeignet für: Teams mit einem dedizierten Marketing-Analysten

Stufe 4: Eigenentwicklung (Full Code)
Beispiele: Python mit scikit-learn, TensorFlow, oder proprietäre Lösungen

Vorteile: Vollste Kontrolle, keine Vendor-Lock-in

Nachteile: Hohe Kosten (mind. 1 Data Scientist), laufende Wartung

Geeignet für: Große Unternehmen mit >10 Mio. Customer-Profilen

Einsteiger-Empfehlung: Beginnen Sie mit Stufe 1 auf einem Kanal. Sobald Sie einen positiven ROI nachweisen können, evaluieren Sie Stufe 2 für kanalübergreifende Modelle.

5. Feature Engineering für Marketer
Ein Feature ist eine messbare Eigenschaft, die das KI-Modell als Input nutzt. Gute Features sind der Unterschied zwischen einem brauchbaren und einem brillanten Modell. Drei Typen sollten Sie kennen:

Statische Features: Ändern sich selten (Geschlecht, Akquisitionskanal, Gerätetyp bei Erstregistrierung)

Zeitbasierte Features: (Tage seit letzter Öffnung, durchschnittliche Sitzungsdauer der letzten 7 Tage, Saisonalität)

Aggregierte Features: (Anzahl Transaktionen in den letzten 30 Tagen, Gesamtumsatz, Klick-zu-Öffnungs-Ratio)

Praxistipp: Erstellen Sie für jedes Feature eine kurze Dokumentation: Was bedeutet es? Aus welchem Feld wird es berechnet? Welche Einheit? Das nennt sich Feature-Data-Dictionary – und es rettet Sie, wenn Ihr Modell in sechs Monaten unerwartete Ergebnisse liefert.

6. Die Train-Validation-Test-Logik
Sie müssen dieses Prinzip verstehen, um Anbieter kritisch zu hinterfragen und eigene Piloten zu designen:

Trainingsdaten (ca. 60 %): Das Modell lernt Muster. Beispiel: "Kunden, die drei E-Mails in einer Woche öffnen, kaufen häufiger."

Validierungsdaten (ca. 20 %): Das Modell wird während der Entwicklung getunt. Hier vermeiden Sie Overfitting.

Testdaten (ca. 20 %): Vom Modell völlig ungesehen. Die finale Prüfung: Kann das Modell auf neuen Daten genauso gut vorhersagen?

Warnsignal: Wenn ein Anbieter oder Kollege nur von "Accuracy 95 %" spricht, aber nicht sagen kann, auf welchem Datensatz (Training vs. Test) diese Zahl basiert – seien Sie skeptisch.

7. Datenschutz und Compliance (DSGVO)
KI im Marketing bewegt sich in einem engen rechtlichen Rahmen. Drei nicht-verhandelbare Punkte:

Rechtsgrundlage: Prädiktive Profile benötigen eine Einwilligung oder berechtigtes Interesse – prüfen Sie Ihre Einwilligungstexte auf "automatisierte Entscheidungsfindung" gemäß Art. 22 DSGVO.

Auskunftsanspruch: Kunden können verlangen zu erfahren, welche Daten in Ihr KI-Modell einfließen. Sie müssen erklären können, welche Features genutzt werden (kein kompletter Quellcode, aber eine semantische Beschreibung).

Löschkonzepte: Wenn ein Kunde gelöscht wird, müssen seine Daten auch aus allen Trainingsdatensätzen entfernt werden – technisch anspruchsvoll, aber rechtlich notwendig.

8. Erster technischer Pilot: Vorgehen
Datenexport: Ziehen Sie historische Daten aus einem Kanal für die letzten 12 Monate (z. B. E-Mail-Interaktionen + Transaktionen).

Bereinigung: Entfernen Sie Duplikate, standardisieren Sie kategoriale Werte (z. B. "DE"/"Germany" → "DE").

Feature-Tabelle bauen: Erstellen Sie pro Kunde eine Zeile mit Features (z. B. Anzahl Öffnungen letzte 7 Tage) und dem Ziel (z. B. "Hat gekauft: Ja/Nein").

Einfaches Modell: Nutzen Sie ein Low-Code-Tool (z. B. Akkio) oder lassen Sie ein Data-Science-Teammitglied eine logistische Regression laufen.

Test: Prüfen Sie die Vorhersagegüte (z. B. AUC-Wert > 0,7 ist gut für Marketing).

Integration: Exportieren Sie die Vorhersagen als CSV zurück in Ihr Marketing-Tool.

9. Typische Technologiefehler
Echtzeit vs. Batch: Nicht alles muss in Echtzeit sein. Für eine wöchentliche Newsletter-Personalisierung reicht ein Batch-Modell um 3 Uhr morgens.

Cold Start: Neue Produkte oder Kanäle haben keine historischen Daten. Hier helfen regelbasierte Fallbacks oder simple Heuristiken.

Concept Drift: Das Kundenverhalten ändert sich (z. B. nach einem Preisanstieg). Ihr Modell muss regelmäßig (z. B. monatlich) neu trainiert werden.

Fazit für die Praxis
Daten und Technologie sind die Grundlage jedes KI-Marketing-Projekts. Sie brauchen keine Petabyte an Daten oder eine Data-Science-Elite. Sie brauchen aber: saubere Ereignisdaten aus einem Kanal, eine eindeutige Kunden-ID, und das Verständnis für Train/Test-Trennung. Beginnen Sie mit den Daten, die Sie bereits haben – nicht mit denen, die Sie gerne hätten. Ein funktionierendes Modell auf einem Kanal bringt mehr als eine perfekte Architektur auf dem Papier.

Nächste Schritte: Führen Sie das Data Audit auf Ihrem stärksten Kanal durch (meist E-Mail oder CRM). Dokumentieren Sie drei auffällige Qualitätsprobleme und beheben Sie das einfachste (z. B. doppelte Profile). Dann sind Sie bereit für Mini-Guide 3: Erste KI-Modelle im Marketing – von der Theorie zur Kampagne.