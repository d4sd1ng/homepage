#!/usr/bin/env python3
"""Erstellt alle rechtlichen Dokumente fuer Autonova"""
import os
from pathlib import Path

OUT = Path(__file__).parent / "legal_output"
OUT.mkdir(exist_ok=True)

# Firmen-Daten
F = {
    "firma": "Autonova",
    "name": "Tino Schneider",
    "strasse": "Berliner Strasse 12",
    "plz": "35039",
    "ort": "Marburg",
    "tel": "06421 9675392",
    "email": "admin@avataryx.de",
    "dsb_name": "Melanie Schenk",
    "dsb_email": "dsb@avataryx.de",
    "registergericht": "Amtsgericht Marburg",
}

###############################################################################
# 1. Datenschutzerklaerung
###############################################################################
DSE = f"""# Datenschutzerklaerung

Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO):

**{F['firma']}**
{F['name']}
{F['strasse']}
{F['plz']} {F['ort']}

Telefon: {F['tel']}
E-Mail: {F['email']}

Datenschutzbeauftragte:
{F['dsb_name']}
E-Mail: {F['dsb_email']}

---

## 1. Allgemeines zur Datenverarbeitung

Wir verarbeiten personenbezogene Daten unserer Nutzer gemaess den Bestimmungen der Europaeischen Datenschutz-Grundverordnung (DSGVO) und dem Bundesdatenschutzgesetz (BDSG). Personenbezogene Daten sind alle Informationen, die sich auf eine identifizierte oder identifizierbare natuerliche Person beziehen.

Wir verarbeiten personenbezogene Daten grundsaetzlich nur, soweit dies zur Vertragserfuellung, zur Durchfuehrung vorvertraglicher Massnahmen, aufgrund einer von Ihnen erteilten Einwilligung oder aufgrund einer gesetzlichen Vorschrift erforderlich ist. Eine Weitergabe von Daten an Dritte erfolgt nur im Rahmen der gesetzlichen Vorgaben.

## 2. Erhebung und Speicherung personenbezogener Daten

### 2.1 Beim Besuch unserer Website

Beim Aufrufen unserer Website werden durch den Browser automatisch Informationen an den Server unserer Website gesendet. Diese Informationen werden in sogenannten Log-Dateien gespeichert:
- IP-Adresse
- Datum und Uhrzeit der Anfrage
- Zeitzonendifferenz zur Greenwich Mean Time (GMT)
- Inhalt der Anforderung (konkrete Seite)
- Zugriffsstatus/HTTP-Statuscode
- Jeweils uebertragene Datenmenge
- Website, von der die Anforderung kommt (Referrer-URL)
- Browser und Betriebssystem
- Name und Version des Browsers/Providers

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. f DSGVO (berechtigte Interessen an der Sicherstellung eines fehlerfreien und sicheren Betriebs).

### 2.2 Bei der Newsletter-Anmeldung

Wenn Sie unseren Newsletter abonnieren, erheben wir folgende Daten:
- E-Mail-Adresse
- Vor- und Nachname (freiwillig)
- Anmeldedatum und -uhrzeit
- Anmeldequelle (Website, Landing Page, etc.)
- IP-Adresse bei der Anmeldung

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. a DSGVO (Einwilligung). Die Einwilligung erfolgt ueber ein Double-Opt-In-Verfahren.

### 2.3 Bei der Nutzung unserer SaaS-Produkte

Bei der Registrierung und Nutzung erheben wir:
- Name, E-Mail-Adresse, Unternehmen
- Zahlungsdaten (ueber Stripe)
- Nutzungsdaten (Login-Zeiten, genutzte Funktionen)
- API-Aufrufe und -Statistiken

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. b DSGVO (Vertragserfuellung) und Art. 6 Abs. 1 S. 1 lit. a DSGVO (Einwilligung soweit ueber die Vertragserfuellung hinausgehend).

### 2.4 Bei Kauf digitaler Produkte (Freelancer-Saeule)

Wir erheben:
- Name und E-Mail-Adresse
- Rechnungsdaten
- Zahlungsdaten (ueber Stripe)
- Lizenzinformationen

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. b DSGVO (Vertragserfuellung).

## 3. Verwendung von Cookies

Wir setzen Cookies ein, um unsere Website nutzerfreundlicher zu gestalten. Einige Cookies bleiben auf Ihrem Endgeraet gespeichert, bis Sie diese loeschen. Sie koennen in den Sicherheitseinstellungen Ihres Browsers festlegen, dass keine Cookies gesetzt werden.

### 3.1 Notwendige Cookies
- Session-Cookies zur Aufrechterhaltung der Anmeldung
- CSRF-Schutz-Cookies

### 3.2 Analyse-Cookies (nur mit Einwilligung)
- _ga, _ga_* (Google Analytics, wenn aktiviert)
- Eigene Analyse-Cookies fuer E-Mail-Oeffnungsraten

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. a DSGVO (Einwilligung ueber Cookie-Banner).

## 4. E-Mail-Marketing und Nurturing

### 4.1 Automatisierte E-Mail-Sequenzen

Wir setzen ein automatisiertes E-Mail-Nurturing-System ein, das auf Basis Ihres Nutzerverhaltens personalisierte E-Mails versendet:
- Willkommens-E-Mails nach Anmeldung
- Produkt-Empfehlungen basierend auf Interessen
- Reaktivierungs-E-Mails bei Inaktivitaet
- Trial-to-Paid-Sequenzen fuer SaaS-Produkte
- Blog-Nurturing-E-Mails basierend auf gelesenen Inhalten

Jede E-Mail enthaelt einen Abmelde-Link. Die Abmeldung wird unverzueglich umgesetzt (max. 48 Stunden).

### 4.2 Tracking von E-Mail-Interaktionen

Wir tracken folgende E-Mail-Interaktionen:
- Oeffnungsrate (Pixel-Tracking)
- Klickrate auf Links
- Bounce-Rate (unzustellbare E-Mails)
- Abmelderate

Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. a DSGVO (Einwilligung bei Anmeldung) und Art. 6 Abs. 1 S. 1 lit. f DSGVO (berechtigtes Interesse an der Optimierung).

## 5. Auftragsverarbeiter

### 5.1 Resend, Inc. (E-Mail-Versand)

**Unternehmen:** Resend, Inc., 548 Market Street, San Francisco, CA 94104, USA
**Zweck:** Versand von E-Mail-Newslettern und Nurturing-Sequenzen
**Datenkategorien:** E-Mail-Adressen, E-Mail-Inhalte, Versandzeitpunkte, Bounce-Informationen, Abmelde-Anfragen
**Rechtsgrundlage:** Auftragsverarbeitungsvertrag (Art. 28 DSGVO) + EU-Standardvertragsklauseln
**Drittlanduebermittlung:** USA. Auf Basis SCCs + EU-US Data Privacy Framework. Resend ist DPF-zertifiziert.

### 5.2 Notion Labs Inc. (Datenbank/CMS)

**Unternehmen:** Notion Labs Inc., 2300 Harrison Street, San Francisco, CA 94110, USA
**Zweck:** Speicherung und Verwaltung von Kontaktdaten, Content und Scheduling
**Datenkategorien:** Kontaktinformationen, E-Mail-Content-Daten, Scheduling-Daten
**Rechtsgrundlage:** Auftragsverarbeitungsvertrag (Art. 28 DSGVO) + Notion DPA + SCCs
**Drittlanduebermittlung:** USA auf Basis SCCs + EU-US DPF

### 5.3 Hetzner Online GmbH (Hosting)

**Unternehmen:** Hetzner Online GmbH, Industriestr. 25, 91710 Gunzenhausen, Deutschland
**Zweck:** Bereitstellung und Betrieb der Server-Infrastruktur
**Datenkategorien:** Server-Logdaten, Nutzerdaten
**Rechtsgrundlage:** Auftragsverarbeitungsvertrag (Art. 28 DSGVO)
**Drittlanduebermittlung:** Keine. Rechenzentren in Deutschland und Finnland (EU).

### 5.4 Stripe, Inc. / Stripe Payments Europe Ltd (Zahlungsabwicklung)

**Unternehmen:** Stripe Payments Europe Ltd, 1 Grand Canal Street Lower, Grand Canal Dock, Dublin, Irland
**Zweck:** Abwicklung von Zahlungen fuer SaaS-Abonnements und digitale Produkte
**Datenkategorien:** Zahlungsdaten, Rechnungsdaten, Kundendaten
**Rechtsgrundlage:** Auftragsverarbeitungsvertrag (Art. 28 DSGVO) + Stripe DPA
**Drittlanduebermittlung:** Irland (EU). Ggf. Teildaten in USA auf Basis SCCs + EU-US DPF.

## 6. Ihre Rechte als Betroffener

Sie haben gemaess DSGVO folgende Rechte:

### 6.1 Auskunftsrecht (Art. 15 DSGVO)
Sie koennen jederzeit Auskunft ueber die zu Ihrer Person gespeicherten Daten verlangen.

### 6.2 Berichtigungsrecht (Art. 16 DSGVO)
Sie koennen die Berichtigung unrichtiger Daten verlangen.

### 6.3 Loeschungsrecht (Art. 17 DSGVO)
Sie koennen die Loeschung Ihrer Daten verlangen, sofern keine gesetzlichen Aufbewahrungsfristen entgegenstehen.

### 6.4 Einschraenkung der Verarbeitung (Art. 18 DSGVO)
Sie koennen die Einschraenkung der Verarbeitung Ihrer Daten verlangen.

### 6.5 Datenuebertragbarkeit (Art. 20 DSGVO)
Sie koennen die Herausgabe Ihrer Daten in einem strukturierten, gaengigen und maschinenlesbaren Format verlangen.

### 6.6 Widerspruchsrecht (Art. 21 DSGVO)
Sie koennen der Verarbeitung Ihrer Daten widersprechen. Bei Direktwerbung haben Sie ein jederzeitiges Widerspruchsrecht ohne Angabe von Gruenden. Der Widerspruch kann per E-Mail an {F['email']} oder ueber den Abmelde-Link in jeder E-Mail erklaert werden.

### 6.7 Widerruf der Einwilligung (Art. 7 Abs. 3 DSGVO)
Sie koennen Ihre Einwilligung jederzeit widerrufen. Der Widerruf beruehrt nicht die Rechtmassigkeit der bis zum Widerruf erfolgten Verarbeitung.

### 6.8 Beschwerderecht (Art. 77 DSGVO)
Sie koennen sich bei einer Aufsichtsbehoerde beschweren. Zustaendig ist:
Der Hessische Datenschutzbeauftragte
Gustav-Stresemann-Ring 1, 65189 Wiesbaden
https://datenschutz.hessen.de

## 7. Datensicherheit

Wir setzen folgende technische und organisatorische Massnahmen ein:
- Verschluesselung der Datenuebertragung (TLS 1.3)
- Verschluesselte Speicherung von Passwoertern (bcrypt)
- Zugriffskontrolle und Authentifizierung
- Regelmassige Sicherheitspruefungen
- Trennung von Test- und Produktivsystemen
- Logging und Monitoring von Zugriffen
- Backup-Strategie mit verschluesselten Backups

## 8. Aufbewahrungsdauer

- Newsletter-Daten: Bis zur Abmeldung, danach 30 Tage fuer Archivierung
- Vertragsdaten: 10 Jahre nach Vertragsende (steuerrechtliche Aufbewahrungspflicht)
- Zahlungsdaten: 10 Jahre (steuerrechtliche Aufbewahrungspflicht)
- Logdaten: 90 Tage
- Double-Opt-In-Nachweise: 3 Jahre nach Einwilligung
- Abmelde-Protokolle: 3 Jahre

## 9. Aenderungen

Wir behalten uns vor, diese Datenschutzerklaerung anzupassen. Die jeweils aktuelle Version finden Sie auf unserer Website. Bei wesentlichen Aenderungen informieren wir Sie per E-Mail.

**Stand:** Mai 2026
**Version:** 1.0 ENTWURF - Vor Verwendung von einem Fachanwalt fuer IT-Recht pruefen lassen!
"""

###############################################################################
# 2. AVV Notion
###############################################################################
AVV_NOTION = f"""# Auftragsverarbeitungsvertrag (AVV)
## zwischen {F['firma']} und Notion Labs Inc.

**Stand:** Mai 2026 | **Version:** 1.0 ENTWURF

### Vertragsparteien

**Auftraggeber:**
{F['firma']}
{F['name']}
{F['strasse']}
{F['plz']} {F['ort']}
Telefon: {F['tel']}
E-Mail: {F['email']}

**Auftragsverarbeiter:**
Notion Labs Inc.
2300 Harrison Street
San Francisco, CA 94110, USA

---

## 1. Gegenstand und Dauer

(1) Gegenstand dieses Vertrages ist die Verarbeitung personenbezogener Daten durch den Auftragsverarbeiter im Auftrag des Auftraggebers. Der Auftragsverarbeiter verarbeitet personenbezogene Daten ausschliesslich im Rahmen der Weisungen des Auftraggebers.

(2) Dieser Vertrag ergaenzt die Notion Data Processing Agreement (DPA). Im Falle von Widerspruechen geht dieser Vertrag vor.

(3) Die Laufzeit entspricht der Laufzeit des Notion-Abonnements. Er endet mit der Loeschung aller personenbezogenen Daten beim Auftragsverarbeiter.

## 2. Art und Umfang der Verarbeitung

| Merkmal | Beschreibung |
|:---|:---|
| Art der Daten | Kontaktdaten (Name, E-Mail), E-Mail-Content-Daten, Scheduling-Daten, Analytics-Daten |
| Kategorie betroffener Personen | Newsletter-Abonnenten, SaaS-Nutzer, B2B-Kunden, Website-Besucher |
| Verarbeitungstaetigkeiten | Speicherung, Verwaltung, Scheduling, Analyse |
| Speicherort | USA (Notion betreibt Server ueber AWS us-east-1 / us-west-2) |

## 3. Pflichten des Auftragsverarbeiters

(1) Der Auftragsverarbeiter verarbeitet die Daten nur im Rahmen der Weisungen des Auftraggebers.

(2) Der Auftragsverarbeiter gewaehrleistet die Einhaltung der in Anlage 1 aufgefuehrten technischen und organisatorischen Massnahmen.

(3) Der Auftragsverarbeiter unterrichtet den Auftraggeber unverzueglich bei Verdaechtigen auf Datenschutzverletzungen.

(4) Der Auftragsverarbeiter gewaehrleistet, dass die zur Verarbeitung befugten Personen auf Vertraulichkeit verpflichtet sind.

## 4. Unterbeauftragung

Notion setzt folgende Unterauftragnehmer ein:
- Amazon Web Services, Inc. (Cloud-Hosting)
- Google Cloud Platform (ggf.)

Eine Unterbeauftragung ueber diese hinaus bedarf der vorherigen Zustimmung des Auftraggebers.

## 5. Kontrollrechte

Der Auftraggeber hat das Recht, die Einhaltung der Vorgaben zu kontrollieren. Notion stellt auf Anfrage entsprechende Nachweise bereit (Audit-Berichte, Zertifikate).

## 6. Loeschung und Herausgabe

Nach Beendigung des Auftragsverhaeltnisses loescht Notion alle personenbezogenen Daten innerhalb von 30 Tagen, es sei denn, gesetzliche Aufbewahrungsfristen stehen dem entgegen.

## 7. Datenschutzverletzungen

Notion informiert den Auftraggeber unverzueglich, spaetestens jedoch innerhalb von 48 Stunden nach Bekanntwerden, ueber Datenschutzverletzungen.

---

### Anlage 1: Technische und organisatorische Massnahmen (TOMs)

| Nr. | Massnahme | Umsetzung |
|:---|:---|:---|
| 1 | Zutrittskontrolle | Rechenzentren mit physischem Zugangsschutz (AWS) |
| 2 | Zugangskontrolle | Rollenbasierte Zugriffskontrolle, MFA |
| 3 | Zugriffskontrolle | Berechtigungskonzept, minimale Rechtevergabe |
| 4 | Trennungskontrolle | Logische Trennung der Mandanten |
| 5 | Pseudonymisierung | Datenbank-IDs statt Klardaten wo moeglich |
| 6 | Verschluesselung | TLS 1.3 fuer Uebertragung, AES-256 fuer Speicherung |
| 7 | Integritaet | Versionierung, Backup, Checksummen |
| 8 | Verfuegbarkeit | 99.9% SLA, automatisches Failover |
| 9 | Audit | SOC 2 Type II, ISO 27001 |
| 10 | Aufbewahrung | Automatische Loeschung nach Ablauf |

### Anlage 2: EU-Standardvertragsklauseln

Es gelten die EU-Standardvertragsklauseln gemaess Durchfuehrungsbeschluss (EU) 2021/914:
- Modul 2 (Auftraggeber an Auftragsverarbeiter)
- Klausel 7 (Docking-Klausel)
- Anhang I: Siehe Vertragsparteien oben
- Anhang II: Siehe TOMs Anlage 1

**ENTWURF - Vor Verwendung von einem Fachanwalt pruefen lassen!**
"""

###############################################################################
# 3. AVV Resend/SMTP
###############################################################################
AVV_RESEND = f"""# Auftragsverarbeitungsvertrag (AVV)
## zwischen {F['firma']} und Resend, Inc.

**Stand:** Mai 2026 | **Version:** 1.0 ENTWURF

### Vertragsparteien

**Auftraggeber:**
{F['firma']}
{F['name']}
{F['strasse']}
{F['plz']} {F['ort']}
Telefon: {F['tel']}
E-Mail: {F['email']}

**Auftragsverarbeiter:**
Resend, Inc.
548 Market Street
San Francisco, CA 94104, USA

---

## 1. Gegenstand und Dauer

(1) Gegenstand ist die Verarbeitung personenbezogener Daten im Zusammenhang mit dem Versand von E-Mail-Newslettern, Nurturing-E-Mails und Transaktions-E-Mails.

(2) Die Laufzeit entspricht der Laufzeit des Resend-Abonnements.

## 2. Art und Umfang der Verarbeitung

| Merkmal | Beschreibung |
|:---|:---|
| Art der Daten | E-Mail-Adressen, E-Mail-Inhalte, Versandzeitpunkte, Bounce-Daten |
| Kategorie betroffener Personen | Newsletter-Abonnenten, SaaS-Nutzer, Leads |
| Verarbeitungstaetigkeiten | E-Mail-Versand, Bounce-Verarbeitung, Unsubscribe-Verarbeitung |
| Speicherort | USA (AWS us-east-1 / us-west-2) |

## 3. Spezifische Pflichten

(1) Unsubscribe-Anfragen muessen innerhalb von 48 Stunden umgesetzt werden.

(2) Bounce-Management: Dauerhaft nicht zustellbare Adressen werden automatisch aus dem Versand genommen.

(3) Spam-Beschwerden werden unverzueglich an den Auftraggeber gemeldet.

(4) Der Versand erfolgt gemaess den konfigurierten Raten (max. 100 E-Mails/Minute im Paid-Tarif).

## 4. Unterauftragnehmer

- Amazon Web Services, Inc. (Cloud-Infrastruktur)
- SendGrid (als Fallback/Relay, falls aktiviert)

## 5. EU-Standardvertragsklauseln

Es gelten die EU-Standardvertragsklauseln gemaess Durchfuehrungsbeschluss (EU) 2021/914:
- Modul 2 (Auftraggeber an Auftragsverarbeiter)
- Resend ist unter das EU-US Data Privacy Framework zertifiziert

## 6. TOMs

Identisch mit AVV Notion Anlage 1, zusaetzlich:
- DKIM-Signatur fuer alle ausgehenden E-Mails
- SPF/DKIM/DMARC-Konfiguration
- Automatische Bounce-Verarbeitung
- Rate-Limiting zum Schutz vor Missbrauch

**ENTWURF - Vor Verwendung von einem Fachanwalt pruefen lassen!**
"""

###############################################################################
# 4. AGB + Impressum + Widerruf
###############################################################################
AGB = f"""# AGB SaaS + Impressum + Widerrufsbelehrung
## {F['firma']}

**WICHTIG: ENTWURF - Vor Verwendung von einem Fachanwalt fuer IT-Recht pruefen lassen!**

---

## A. Allgemeine Geschaeftsbedingungen (AGB) - SaaS

### Geltungsbereich

(1) Diese AGB gelten fuer alle Vertraege zwischen {F['firma']} ({F['name']}, {F['strasse']}, {F['plz']} {F['ort']}) und dem Kunden ueber die Nutzung der Autonova SaaS-Produkte.

(2) Die aktuell veroeffentlichten SaaS-Produkte umfassen:
- Prompt Optimizer
- Content Calendar
- Workflow Automation
- Multi-Platform Connector

(3) Abweichende AGB des Kunden werden nicht anerkannt.

### 1. Vertragsgegenstand

(1) {F['firma']} gewaehrt dem Kunden ein nicht-ausschliessliches, auf die Vertragsdauer beschraenktes Recht zur Nutzung der SaaS-Plattform.

(2) Der Umfang der Nutzungsberechtigung richtet sich nach dem gewaehlten Tarif.

### 2. Preise und Tarife

| Tarif | Monatlich | Jaehrlich (20% Rabatt) | Enthalten |
|:---|:---|:---|:---|
| Free | 0 EUR | 0 EUR | 50 API-Calls, 5 Vorlagen |
| Starter | 9 EUR/Monat | 86 EUR/Jahr | 100 API-Calls, E-Mail-Support, 1 Workspace |
| Professional | 29 EUR/Monat | 278 EUR/Jahr | 1.000 API-Calls, Priority-Support, 5 Workspaces |
| Enterprise | Auf Anfrage | Auf Anfrage | Unlimited, Dedicated Support, Custom SLA |

(3) Alle Preise verstehen sich inklusive der gesetzlichen Mehrwertsteuer von 19%.

(4) Die Zahlung erfolgt ueber Stripe (Kreditkarte, SEPA-Lastschrift).

### 3. Vertragslaufzeit

(1) Monatliche Tarife verlaengern sich jeweils um einen Monat, sofern nicht mit einer Frist von 14 Tagen zum Monatsende gekuendigt wird.

(2) Jaehrliche Tarife verlaengern sich jeweils um ein Jahr, sofern nicht mit einer Frist von 30 Tagen zum Jahresende gekuendigt wird.

(3) Das Recht zur ausserordentlichen Kuendigung aus wichtigem Grund bleibt unberuehrt.

### 4. Nutzungsrechte

(1) Der Kunde erhaelt ein nicht-ausschliessliches, nicht-uebertragbares Recht zur Nutzung der SaaS-Plattform fuer die Vertragsdauer.

(2) Eine Weitergabe der Zugangsdaten an Dritte ist untersagt.

(3) Der Kunde ist fuer die Sicherheit seiner Zugangsdaten verantwortlich.

### 5. Verfuegbarkeit

(1) {F['firma']} bemueht sich um eine Verfuegbarkeit von 99,5% im Jahresdurchschnitt.

(2) Wartungsfenster werden rechtzeitig angekuenigt.

### 6. Datenschutz

Es gilt die Datenschutzerklaerung unter https://autonova.de/datenschutz.

### 7. Haftung

(1) Die Haftung fuer Schaeden infolge von Vorsatz oder grober Fahrlaessigkeit sowie fuer Personenschaeden ist unbeschraenkt.

(2) Bei leicht fahrlaessiger Verletzung wesentlicher Vertragspflichten ist die Haftung auf den vorhersehbaren, vertragstypischen Schaeden beschraenkt.

(3) Die Haftung fuer Datenverlust ist auf den typischen Wiederherstellungsaufwand beschraenkt.

### 8. Schlussbestimmungen

(1) Es gilt das Recht der Bundesrepublik Deutschland.

(2) Gerichtsstand ist {F['ort']}.

(3) Sollten einzelne Bestimmungen unwirksam sein, bleibt die Wirksamkeit der uebrigen Bestimmungen unberuehrt.

---

## B. Impressum

| Angabe | Eintrag |
|:---|:---|
| Firmenname | {F['firma']} |
| Rechtsform | Einzelunternehmen |
| Vertreten durch | {F['name']} |
| Anschrift | {F['strasse']}, {F['plz']} {F['ort']} |
| Kontakt E-Mail | {F['email']} |
| Kontakt Telefon | {F['tel']} |
| Handelsregister | {F['registergericht']} |
| USt-IdNr. | [Bei Beantragung eintragen] |

Verantwortlich fuer den Inhalt nach paragraph 55 Abs. 2 RStV:
{F['name']}
{F['strasse']}
{F['plz']} {F['ort']}

Streitschlichtung: Die Europaeische Kommission stellt eine Plattform zur Online-Streitbeilegung bereit: https://ec.europa.eu/consumers/odr

---

## C. Widerrufsbelehrung

### Widerrufsrecht

Sie haben das Recht, diesen Vertrag innerhalb von 14 Tagen ohne Angabe von Gruenden zu widerrufen.

Die Widerrufsfrist betraegt 14 Tage ab dem Tag des Vertragsabschlusses.

Um Ihr Widerrufsrecht auszuueben, muessen Sie uns ({F['firma']}, {F['strasse']}, {F['plz']} {F['ort']}, {F['email']}) mittels einer eindeutigen Erklaerung (z.B. ein mit der Post versandter Brief oder E-Mail) ueber Ihren Entschluss, diesen Vertrag zu widerrufen, informieren.

### Widerrufsfolgen

Wenn Sie diesen Vertrag widerrufen, haben wir Ihnen alle Zahlungen, die wir von Ihnen erhalten haben, einschliesslich der Lieferkosten (mit Ausnahme der zusaetzlichen Kosten, die sich daraus ergeben, dass Sie eine andere Art der Lieferung als die von uns angebotene guenstige Standardlieferung gewaehlt haben), unverzueglich und spaetestens binnen vierzehn Tagen ab dem Tag zurueckzuzahlen, an dem die Mitteilung ueber Ihren Widerruf dieses Vertrags bei uns eingegangen ist.

### Besondere Hinweise

Bei Dienstleistungen: Wenn Sie die Dienstleistung vor Ablauf der Widerrufsfrist in Anspruch nehmen, erklaeren Sie sich damit einverstanden, dass Sie Ihr Widerrufsrecht bei vollstaendiger Vertragserfuellung verlieren.

### Muster-Widerrufsformular

(Wenn Sie den Vertrag widerrufen wollen, dann fuellen Sie bitte dieses Formular aus und senden Sie es zurueck.)

An: {F['firma']}, {F['strasse']}, {F['plz']} {F['ort']}, {F['email']}

Hiermit widerrufe(n) ich/wir den von mir/uns abgeschlossenen Vertrag ueber den Kauf der folgenden Waren / die Erbringung der folgenden Dienstleistung:

Bestellt am: _______________
Name des Verbrauchers: _______________
Unterschrift: _______________ (nur bei Mitteilung auf Papier)
Datum: _______________

**ENTWURF - Vor Verwendung von einem Fachanwalt pruefen lassen!**
"""

###############################################################################
# 5. Verarbeitungsverzeichnis
###############################################################################
VVT = f"""# Verarbeitungsverzeichnis (VVT)
## gemaess Art. 30 DSGVO

**Verantwortlicher:** {F['firma']}, {F['name']}, {F['strasse']}, {F['plz']} {F['ort']}

**Erstellt:** Mai 2026 | **Naechste Pruefung:** November 2026

---

## Allgemeine Angaben

| Merkmal | Eintrag |
|:---|:---|
| Name | {F['firma']}, {F['name']} |
| Anschrift | {F['strasse']}, {F['plz']} {F['ort']} |
| Kontakt | Tel: {F['tel']}, E-Mail: {F['email']} |
| DSB | {F['dsb_name']} ({F['dsb_email']}) |
| Zweck | Betrieb E-Mail-Nurturing-System, SaaS-Plattform, Verkauf digitaler Produkte |
| Empfaenger | Notion Labs Inc., Resend Inc., Hetzner Online GmbH, Stripe Payments Europe Ltd |
| Drittlanduebermittlung | USA (Notion, Resend), Irland (Stripe EU) |
| TOMs | Siehe Anlage |

---

## VVT-001: Newsletter-Anmeldung

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Anmeldung zum Newsletter, Double-Opt-In |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. a DSGVO (Einwilligung) |
| Datenkategorien | E-Mail, Name, IP, Anmeldedatum |
| Betroffene | Website-Besucher |
| Empfaenger | Resend Inc. (Versand), Notion Labs Inc. (Speicherung) |
| Loeschfrist | Bis Abmeldung + 30 Tage |
| Drittland | USA (SCCs + DPF) |

## VVT-002: E-Mail-Nurturing

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Automatisierte E-Mail-Sequenzen, Personalisierung |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. a und f DSGVO |
| Datenkategorien | Kontaktdata, Interaktionsdaten, Oeffnungsraten |
| Betroffene | Abonnenten |
| Empfaenger | Resend Inc., Notion Labs Inc. |
| Loeschfrist | Bis Abmeldung + 90 Tage |
| Drittland | USA (SCCs + DPF) |

## VVT-003: SaaS-Nutzung

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Bereitstellung der SaaS-Plattform |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. b DSGVO (Vertrag) |
| Datenkategorien | Name, E-Mail, Unternehmen, Nutzungsdaten |
| Betroffene | SaaS-Kunden |
| Empfaenger | Hetzner (Hosting), Stripe (Zahlung) |
| Loeschfrist | 10 Jahre nach Vertragsende |
| Drittland | Keine (Hetzner DE/FI), USA (Stripe ggf.) |

## VVT-004: Zahlungsabwicklung

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Abwicklung von Zahlungen |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. b DSGVO |
| Datenkategorien | Zahlungsdaten, Rechnungsdaten |
| Betroffene | Kunden |
| Empfaenger | Stripe Payments Europe Ltd |
| Loeschfrist | 10 Jahre (steuerrechtlich) |
| Drittland | Irland (EU), USA ggf. (SCCs + DPF) |

## VVT-005: Website-Tracking

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Verbesserung der Website, Analyse |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. a DSGVO (Einwilligung) |
| Datenkategorien | IP, Browserdaten, Verhaltensdaten |
| Betroffene | Website-Besucher |
| Empfaenger | Hetzner Online GmbH |
| Loeschfrist | 90 Tage |
| Drittland | Keine |

## VVT-006: Content-Verwaltung

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Verwaltung von E-Mail-Content und Scheduling |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse) |
| Datenkategorien | Content-Vorlagen, Scheduling-Daten |
| Betroffene | Keine direkten Personenbezuege |
| Empfaenger | Notion Labs Inc. |
| Loeschfrist | Bis zur Loeschung |
| Drittland | USA (SCCs + DPF) |

## VVT-007: Double-Opt-In

| Merkmal | Eintrag |
|:---|:---|
| Zweck | Nachweis der Einwilligung |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. a DSGVO |
| Datenkategorien | E-Mail, Token, IP, Zeitstempel |
| Betroffene | Angemeldete Personen |
| Empfaenger | Resend Inc. (Bestaetigungsmail) |
| Loeschfrist | 3 Jahre |
| Drittland | USA (SCCs + DPF) |

---

### Anlage: Technische und organisatorische Massnahmen

1. **Zutrittskontrolle:** Rechenzentren mit physischem Schutz (Hetzner)
2. **Zugangskontrolle:** Rollenbasierte Authentifizierung, MFA, bcrypt-Passwoerter
3. **Zugriffskontrolle:** Minimale Rechtevergabe, Audit-Logging
4. **Trennungskontrolle:** Docker-Container-Isolation pro Agent
5. **Verschluesselung:** TLS 1.3 (Uebertragung), AES-256 (Speicherung)
6. **Integritaet:** JSON-Schema-Validierung, Versionierung
7. **Verfuegbarkeit:** Automatischer Restart, Health-Checks, Backups
8. **Audit:** Logging aller Verarbeitungsvorgaenge

**ENTWURF - Vor Verwendung von einem Fachanwalt pruefen lassen!**
"""

###############################################################################
# 6. Finanzmodell
###############################################################################
FINANZ = """# 5-Jahres-Finanzmodell
## Autonova - Nurturing Email System

**ENTWURF - Vor Verwendung von einem Buchhalter/Steuerberater pruefen lassen!**
**Waehrung:** EUR (brutto, inkl. 19% MwSt)

---

## 1. Geschaeftsmodell-Uebersicht

| Saeule | Angebot | Preisstruktur | Zielgruppe |
|:---|:---|:---|:---|
| **Freelancer** | 7 digitale Produkte | Einmalzahlung 47-497 EUR | Selbststaendige |
| **B2B Premium** | 5 Premium-Services | Monatl. 297-1.497 EUR | KMU, Agenturen |
| **SaaS** | 4+ Cloud-Tools | Monatl. 9-97 EUR | Alle |

## 2. Umsatzplanung (5 Jahre)

### Saeule 1: Freelancer (Einmalzahlungen)

| Kennzahl | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|:---|:---|:---|:---|:---|:---|
| Avg. Preis | 147 EUR | 167 EUR | 187 EUR | 197 EUR | 197 EUR |
| Verkaeufe/Monat | 5 | 12 | 20 | 28 | 35 |
| Umsatz/Jahr | 8.820 | 24.048 | 44.880 | 66.192 | 82.740 |

### Saeule 2: B2B Premium (Wiederkehrend)

| Kennzahl | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|:---|:---|:---|:---|:---|:---|
| MRR/kunde | 497 EUR | 547 EUR | 597 EUR | 647 EUR | 697 EUR |
| Kunden | 3 | 7 | 12 | 18 | 25 |
| MRR | 1.491 | 3.829 | 7.164 | 11.646 | 17.425 |
| ARR | 17.892 | 45.948 | 85.968 | 139.752 | 209.100 |

### Saeule 3: SaaS (Wiederkehrend)

| Kennzahl | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|:---|:---|:---|:---|:---|:---|
| ARPU | 19 EUR | 24 EUR | 29 EUR | 34 EUR | 39 EUR |
| Abonnenten | 50 | 200 | 600 | 1.500 | 3.000 |
| MRR | 950 | 4.800 | 17.400 | 51.000 | 117.000 |
| ARR | 11.400 | 57.600 | 208.800 | 612.000 | 1.404.000 |

### Gesamtumsatz

| Jahr | Freelancer | B2B | SaaS | Gesamt |
|:---|:---|:---|:---|:---|
| 1 | 8.820 | 17.892 | 11.400 | 38.112 |
| 2 | 24.048 | 45.948 | 57.600 | 127.596 |
| 3 | 44.880 | 85.968 | 208.800 | 339.648 |
| 4 | 66.192 | 139.752 | 612.000 | 817.944 |
| 5 | 82.740 | 209.100 | 1.404.000 | 1.695.840 |

## 3. Kostenplanung (monatlich)

| Kostenpunkt | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|:---|:---|:---|:---|:---|:---|
| Hetzner Server | 10 | 25 | 50 | 100 | 150 |
| Resend | 0 | 20 | 50 | 150 | 300 |
| Notion | 0 | 0 | 8 | 8 | 8 |
| Stripe-Gebuehren | 30 | 100 | 300 | 800 | 1.800 |
| Domain/SSL | 5 | 5 | 5 | 5 | 5 |
| Marketing | 200 | 500 | 1.000 | 2.000 | 3.500 |
| Personal | 0 | 0 | 2.000 | 4.000 | 7.000 |
| Sonstiges | 50 | 100 | 200 | 400 | 800 |
| **Gesamt/Monat** | **295** | **750** | **3.613** | **7.463** | **13.563** |

## 4. Szenario-Analyse

| Szenario | Jahr 1 | Jahr 3 | Jahr 5 | Marge J5 |
|:---|:---|:---|:---|:---|
| Pessimistisch | 22.000 | 180.000 | 850.000 | 52% |
| **Realistisch (Base)** | **38.000** | **340.000** | **1.560.000** | **62%** |
| Optimistisch | 55.000 | 520.000 | 2.400.000 | 71% |
"""

###############################################################################
# 7. Break-Even + CAC/LTV
###############################################################################
BREAKEVEN = """# Break-Even + CAC/LTV Berechnung
## Autonova - Nurturing Email System

**ENTWURF - Vor Verwendung von einem Buchhalter pruefen lassen!**

---

## 1. Break-Even pro Saeule

### Saeule 1: Freelancer (Einmalzahlungen)

| Kennzahl | Wert |
|:---|:---|
| Fixkosten/Monat (anteilig) | 91 EUR |
| Avg. Erloes pro Verkauf | 147 EUR |
| Variable Kosten pro Verkauf | 15 EUR |
| Deckungsbeitrag | 132 EUR |
| **Break-Even Verkaeufe/Monat** | **1** |

### Saeule 2: B2B Premium (Wiederkehrend)

| Kennzahl | Wert |
|:---|:---|
| Fixkosten/Monat (anteilig) | 143 EUR |
| Avg. MRR pro Kunde | 497 EUR |
| Variable Kosten pro Kunde/Monat | 50 EUR |
| Deckungsbeitrag/Monat | 447 EUR |
| **Break-Even Kunden** | **1** |

### Saeule 3: SaaS (Wiederkehrend)

| Kennzahl | Wert |
|:---|:---|
| Fixkosten/Monat (anteilig) | 143 EUR |
| ARPU/Monat | 19 EUR |
| Variable Kosten/User/Monat | 3 EUR |
| Deckungsbeitrag/User/Monat | 16 EUR |
| **Break-Even Abonnenten** | **9** |

**Gesamt-Break-Even: ca. 4-6 Monate nach Launch**

## 2. CAC (Customer Acquisition Cost)

| Kanal | CAC Freelancer | CAC B2B | CAC SaaS |
|:---|:---|:---|:---|
| E-Mail-Nurturing | 12 EUR | 0 EUR (Inbound) | 5 EUR |
| LinkedIn | 25 EUR | 150 EUR | 15 EUR |
| SEO/Content | 8 EUR | 80 EUR | 3 EUR |
| **Durchschnitt** | **15 EUR** | **115 EUR** | **8 EUR** |

## 3. LTV (Lifetime Value)

| Kennzahl | Freelancer | B2B | SaaS |
|:---|:---|:---|:---|
| Avg. Erloes | 147 EUR | 5.964 EUR | 1.140 EUR |
| Verweildauer | 1x | 12 Monate | 30 Monate |
| Churn/Monat | - | 8% | 3% |
| **LTV** | **147 EUR** | **8.736 EUR** | **38 EUR** |

## 4. LTV/CAC Ratio

| Saeule | LTV | CAC | Ratio | Bewertung |
|:---|:---|:---|:---|:---|
| Freelancer | 147 EUR | 15 EUR | **9.8:1** | Ausgezeichnet |
| B2B | 8.736 EUR | 115 EUR | **76:1** | Ausgezeichnet |
| SaaS | 38 EUR | 8 EUR | **4.8:1** | Gut |

Gesamtbewertung: Alle Saeulen sind wirtschaftlich tragfaehig. LTV/CAC > 3:1 gilt als gesund.

## 5. Payback Period

| Saeule | CAC | MRR/Erloes | Payback |
|:---|:---|:---|:---|
| Freelancer | 15 EUR | 147 EUR (einmalig) | sofort |
| B2B | 115 EUR | 497 EUR/Monat | 0,2 Monate |
| SaaS | 8 EUR | 19 EUR/Monat | 0,4 Monate |
"""

###############################################################################
# Alle Dateien schreiben
###############################################################################
files = {
    "Datenschutzerklaerung_Autonova.md": DSE,
    "AVV_Notion_Autonova.md": AVV_NOTION,
    "AVV_Resend_Autonova.md": AVV_RESEND,
    "K2_AGB_Impressum_Widerruf.md": AGB,
    "Verarbeitungsverzeichnis_Autonova.md": VVT,
    "K3_Finanzmodell_5Jahre.md": FINANZ,
    "K4_BreakEven_CAC_LTV.md": BREAKEVEN,
}

for name, content in files.items():
    path = OUT / name
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    size = path.stat().st_size
    print(f"  {name}: {size//1024}KB")

print(f"\nAlle {len(files)} Dokumente erstellt in {OUT}")
