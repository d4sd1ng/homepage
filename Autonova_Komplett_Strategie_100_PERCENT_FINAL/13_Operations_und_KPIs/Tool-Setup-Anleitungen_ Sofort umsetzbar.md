# Tool-Setup-Anleitungen: Sofort umsetzbar

## 🎯 ÜBERSICHT: ESSENTIAL TOOLS FÜR AUTONOVA

### **Reihenfolge der Einrichtung:**
1. **HubSpot CRM** (Lead-Management)
2. **Mailchimp/ConvertKit** (E-Mail-Marketing)
3. **Google Analytics 4** (Website-Tracking)
4. **Calendly** (Terminbuchung)
5. **Zapier** (Automatisierung)

---

## 🏢 1. HUBSPOT CRM SETUP (30-45 Min)

### **Schritt 1: Account erstellen**
1. Gehen Sie zu **hubspot.com/free**
2. Klicken Sie auf "Get free CRM"
3. Registrieren Sie sich mit Ihrer Geschäfts-E-Mail
4. Bestätigen Sie Ihre E-Mail-Adresse
5. Wählen Sie "Sales Hub" als Hauptprodukt

### **Schritt 2: Grundeinstellungen**
1. **Unternehmensprofil vervollständigen:**
   - Firmenname: Autonova
   - Branche: Technology/Software
   - Unternehmensgröße: 1-10 Mitarbeiter
   - Land: Deutschland

2. **Währung und Zeitzone:**
   - Währung: EUR (€)
   - Zeitzone: Europe/Berlin
   - Datumsformat: DD.MM.YYYY

### **Schritt 3: Kontakt-Properties definieren**

#### **Navigieren Sie zu: Einstellungen > Properties > Contact Properties**

#### **Neue Properties erstellen:**

**1. Lead-Quelle (Dropdown)**
```
Property Name: Lead Source
Internal Name: lead_source
Field Type: Dropdown select
Options:
- LinkedIn
- YouTube Autonova
- YouTube Politara
- Website Organic
- Website Paid
- Referral
- Direct
- Other
```

**2. Interesse-Level (Number)**
```
Property Name: Interest Level
Internal Name: interest_level
Field Type: Number
Min Value: 1
Max Value: 10
Description: 1=Cold, 5=Warm, 10=Hot
```

**3. Budget-Range (Dropdown)**
```
Property Name: Budget Range
Internal Name: budget_range
Field Type: Dropdown select
Options:
- Under 500€
- 500€ - 1.500€
- 1.500€ - 5.000€
- 5.000€ - 15.000€
- 15.000€+
- Not disclosed
```

**4. Zeitrahmen (Dropdown)**
```
Property Name: Project Timeframe
Internal Name: project_timeframe
Field Type: Dropdown select
Options:
- ASAP (within 2 weeks)
- 1 Month
- 2-3 Months
- 3-6 Months
- 6+ Months
- Just exploring
```

**5. Unternehmensgröße (Dropdown)**
```
Property Name: Company Size
Internal Name: company_size
Field Type: Dropdown select
Options:
- Freelancer/Solo
- 2-10 employees
- 11-50 employees
- 51-200 employees
- 200+ employees
```

### **Schritt 4: Deal-Pipeline erstellen**

#### **Navigieren Sie zu: Sales > Deals > Pipeline Settings**

#### **Neue Pipeline: "Autonova Sales Process"**

**Pipeline-Stufen:**
```
1. Erstkontakt (0% Wahrscheinlichkeit)
   - Lead ist eingegangen
   - Erste Qualifizierung steht aus

2. Qualifiziert (20% Wahrscheinlichkeit)
   - Lead ist qualifiziert
   - Interesse bestätigt
   - Budget und Zeitrahmen bekannt

3. Potenzial-Analyse (40% Wahrscheinlichkeit)
   - Kostenlose Analyse vereinbart
   - Termin steht fest
   - Vorbereitung läuft

4. Analyse durchgeführt (60% Wahrscheinlichkeit)
   - Analyse-Gespräch abgeschlossen
   - Bedarf identifiziert
   - Lösungsansatz präsentiert

5. Proposal (80% Wahrscheinlichkeit)
   - Angebot erstellt und versendet
   - Kunde prüft Proposal
   - Verhandlungen laufen

6. Verhandlung (90% Wahrscheinlichkeit)
   - Finale Details werden geklärt
   - Vertrag wird vorbereitet
   - Starttermin wird geplant

7. Abgeschlossen - Gewonnen (100% Wahrscheinlichkeit)
   - Vertrag unterschrieben
   - Projekt kann starten

8. Abgeschlossen - Verloren (0% Wahrscheinlichkeit)
   - Deal ist verloren
   - Grund dokumentiert
```

### **Schritt 5: E-Mail-Templates erstellen**

#### **Navigieren Sie zu: Sales > Templates**

#### **Template 1: Erste Kontaktaufnahme**
```
Subject: Ihre Anfrage zur KI-Automatisierung

Hallo {{contact.firstname}},

vielen Dank für Ihr Interesse an unseren KI-Lösungen!

Ich habe gesehen, dass Sie sich über {{contact.lead_source}} bei uns gemeldet haben. Das freut mich sehr.

Um Ihnen bestmöglich helfen zu können, würde ich gerne mehr über Ihre aktuelle Situation erfahren:

• Welche Prozesse kosten Sie aktuell am meisten Zeit?
• Haben Sie bereits Erfahrungen mit Automatisierung gemacht?
• Was ist Ihr Ziel für die nächsten 3-6 Monate?

Falls Sie mögen, können wir gerne ein kurzes 15-minütiges Gespräch führen, in dem ich Ihnen zeige, wie andere Unternehmen ähnliche Herausforderungen gelöst haben.

Hier können Sie direkt einen Termin buchen: [Calendly-Link]

Beste Grüße,
{{user.firstname}} {{user.lastname}}
Autonova - KI für Unternehmer
```

#### **Template 2: Potenzial-Analyse Follow-up**
```
Subject: Ihre kostenlose Potenzial-Analyse - Zusammenfassung

Hallo {{contact.firstname}},

vielen Dank für das interessante Gespräch heute!

Wie besprochen, hier die wichtigsten Erkenntnisse:

🎯 Identifizierte Herausforderungen:
• [Hauptproblem 1]
• [Hauptproblem 2]
• [Hauptproblem 3]

💡 Lösungsansätze:
• [Lösungsvorschlag 1]
• [Lösungsvorschlag 2]
• [Lösungsvorschlag 3]

💰 Geschätztes Einsparpotenzial:
• Zeitersparnis: [X] Stunden/Woche
• Kosteneinsparung: [X]€/Monat
• ROI: [X]% in [Y] Monaten

Nächste Schritte:
1. Detailliertes Angebot bis [Datum]
2. Technische Machbarkeitsprüfung
3. Projektstart: [Zeitrahmen]

Falls Sie Fragen haben, melden Sie sich gerne!

Beste Grüße,
{{user.firstname}}
```

#### **Template 3: Proposal Follow-up**
```
Subject: Ihr Angebot für [Projektname] - Fragen?

Hallo {{contact.firstname}},

ich wollte mich kurz melden bezüglich des Angebots, das ich Ihnen am [Datum] gesendet habe.

Haben Sie bereits Gelegenheit gehabt, es durchzugehen?

Falls Sie Fragen haben oder einzelne Punkte besprechen möchten, bin ich gerne da. Oft hilft ein kurzes Gespräch, um Unklarheiten zu beseitigen.

Hier sind die wichtigsten Punkte nochmal zusammengefasst:
• Projektumfang: [Kurzbeschreibung]
• Zeitrahmen: [X] Wochen
• Investment: [X]€
• Erwartete Ergebnisse: [Nutzen]

Soll ich einen Termin für ein kurzes Gespräch einrichten?

Beste Grüße,
{{user.firstname}}
```

### **Schritt 6: Automatisierungen einrichten**

#### **Navigieren Sie zu: Automation > Workflows**

#### **Workflow 1: Neue Lead-Benachrichtigung**
```
Trigger: Contact is created
Actions:
1. Send internal email notification
2. Create task: "Qualify new lead within 24h"
3. Add to sequence: "New Lead Nurturing"
```

#### **Workflow 2: Lead-Scoring**
```
Trigger: Contact property changes
Conditions:
- If Lead Source = LinkedIn → +10 points
- If Budget Range = 5.000€+ → +20 points
- If Timeframe = ASAP → +15 points
- If Company Size = 11+ employees → +10 points

Actions:
- Update Interest Level based on total score
- If score >40: Create high-priority task
```

---

## 📧 2. MAILCHIMP SETUP (20-30 Min)

### **Schritt 1: Account erstellen**
1. Gehen Sie zu **mailchimp.com**
2. Klicken Sie auf "Sign Up Free"
3. Registrieren Sie sich mit Ihrer Geschäfts-E-Mail
4. Bestätigen Sie Ihre E-Mail-Adresse
5. Vervollständigen Sie Ihr Profil

### **Schritt 2: Audience erstellen**

#### **Navigieren Sie zu: Audience > All contacts**

#### **Audience-Einstellungen:**
```
Audience Name: Autonova Newsletter
Default From Email: info@autonova.de
Default From Name: Autonova
Remind people how they signed up: 
"Sie erhalten diese E-Mail, weil Sie sich für unseren Newsletter angemeldet haben."

Contact Information:
Company: Autonova
Address: [Ihre Geschäftsadresse]
Phone: [Ihre Telefonnummer]
```

#### **Audience Fields erstellen:**
```
1. FNAME (First Name) - Text
2. LNAME (Last Name) - Text  
3. COMPANY (Company) - Text
4. LEADSOURCE (Lead Source) - Text
5. INTERESTS (Interests) - Text
```

### **Schritt 3: Signup-Forms erstellen**

#### **Navigieren Sie zu: Audience > Signup forms**

#### **Form 1: Website Newsletter**
```
Form Name: Newsletter Signup
Form Type: Embedded form

Fields:
- Email Address (required)
- First Name (required)
- Company (optional)

Settings:
- Double opt-in: Enabled
- Welcome email: Enabled
- Thank you page: Custom URL to your website
```

#### **Form 2: Lead Magnet Download**
```
Form Name: Lead Magnet - KI Tools Guide
Form Type: Embedded form

Fields:
- Email Address (required)
- First Name (required)
- Company (required)
- Biggest Challenge (dropdown)

Settings:
- Double opt-in: Enabled
- Immediate download link in welcome email
```

### **Schritt 4: E-Mail-Sequenzen importieren**

#### **Navigieren Sie zu: Automations > Customer Journeys**

#### **Automation 1: Willkommens-Sequenz**
```
Trigger: Someone subscribes to Newsletter
Delay: Immediate

Email 1: Welcome + Lead Magnet (Day 0)
Email 2: About Me + Credibility (Day 2)  
Email 3: Case Study + Social Proof (Day 5)
Email 4: Free Resource + CTA (Day 8)
```

#### **Automation 2: Lead Nurturing**
```
Trigger: Downloads Lead Magnet
Delay: 1 day after download

Email 1: Additional Resources (Day 1)
Email 2: Common Mistakes (Day 4)
Email 3: Success Stories (Day 7)
Email 4: Free Consultation Offer (Day 10)
```

### **Schritt 5: E-Mail-Templates erstellen**

#### **Template 1: Newsletter**
```
Subject: [Autonova Weekly] KI-Trends und praktische Tipps

Header: Autonova Logo + Navigation
Content Blocks:
1. Personal Note (150 words)
2. This Week's Tip (200 words)
3. Recommended Resource (100 words)
4. YouTube Video Highlight (100 words)
5. Call-to-Action (50 words)

Footer: 
- Contact Information
- Social Media Links
- Unsubscribe Link
```

### **Schritt 6: Analytics einrichten**

#### **Navigieren Sie zu: Reports > View reports**

#### **Wichtige Metriken tracken:**
```
- Open Rate (Ziel: >25%)
- Click Rate (Ziel: >5%)
- Unsubscribe Rate (Ziel: <2%)
- List Growth Rate (Ziel: +50/Woche)
- Conversion Rate (Ziel: >10%)
```

---

## 📊 3. GOOGLE ANALYTICS 4 SETUP (15-20 Min)

### **Schritt 1: Property erstellen**
1. Gehen Sie zu **analytics.google.com**
2. Klicken Sie auf "Messung starten"
3. Erstellen Sie ein Konto: "Autonova"
4. Property-Name: "Autonova Website"
5. Zeitzone: Deutschland
6. Währung: Euro (EUR)

### **Schritt 2: Datenstream einrichten**
```
Platform: Web
Website URL: https://autonova.de
Stream Name: Autonova Website
Enhanced Measurement: Aktiviert
```

### **Schritt 3: Tracking-Code installieren**
1. Kopieren Sie die Measurement ID (G-XXXXXXXXXX)
2. Fügen Sie den Code in den `<head>` Ihrer Website ein:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### **Schritt 4: Ziele (Conversions) einrichten**

#### **Navigieren Sie zu: Configure > Conversions**

#### **Conversion 1: Newsletter Signup**
```
Event Name: newsletter_signup
Parameters:
- method: newsletter_form
- content: homepage_signup
```

#### **Conversion 2: Lead Magnet Download**
```
Event Name: lead_magnet_download
Parameters:
- content: ki_tools_guide
- method: email_signup
```

#### **Conversion 3: Demo Request**
```
Event Name: demo_request
Parameters:
- method: calendly_booking
- content: free_analysis
```

### **Schritt 5: Custom Dimensions**
```
1. Lead Source
2. User Type (New/Returning)
3. Content Category
4. Campaign Source
```

---

## 📅 4. CALENDLY SETUP (10-15 Min)

### **Schritt 1: Account erstellen**
1. Gehen Sie zu **calendly.com**
2. Registrieren Sie sich mit Ihrer Geschäfts-E-Mail
3. Wählen Sie den kostenlosen Plan
4. Verbinden Sie Ihren Google/Outlook Kalender

### **Schritt 2: Event Type erstellen**

#### **Event: Kostenlose Potenzial-Analyse**
```
Event Name: Kostenlose KI-Potenzial-Analyse
Duration: 30 minutes
Buffer Time: 15 min before, 5 min after

Description:
"In diesem kostenlosen Gespräch analysieren wir gemeinsam:
• Ihre aktuellen Herausforderungen
• Potenziale für KI-Automatisierung  
• Konkrete nächste Schritte
• Realistische Einschätzung von Aufwand und Nutzen

Bringen Sie gerne konkrete Beispiele mit!"

Location: Zoom (automatischer Link)
```

#### **Verfügbarkeitszeiten:**
```
Montag: 09:00 - 17:00
Dienstag: 09:00 - 17:00  
Mittwoch: 09:00 - 17:00
Donnerstag: 09:00 - 17:00
Freitag: 09:00 - 15:00

Pausen:
- 12:00 - 13:00 (Mittagspause)
- Keine Termine nach 17:00
```

### **Schritt 3: Fragen für Teilnehmer**
```
1. Wie heißt Ihr Unternehmen? (Required)
2. Wie viele Mitarbeiter haben Sie? (Required)
3. Was ist Ihre größte Herausforderung aktuell? (Required)
4. Haben Sie bereits Erfahrung mit Automatisierung? (Optional)
5. Was ist Ihr grobes Budget für Optimierungen? (Optional)
```

### **Schritt 4: E-Mail-Benachrichtigungen**
```
Confirmation Email (an Teilnehmer):
"Vielen Dank für Ihre Anmeldung! Ich freue mich auf unser Gespräch.

Zur Vorbereitung:
• Denken Sie an konkrete Beispiele für zeitaufwändige Prozesse
• Überlegen Sie sich Ihre wichtigsten Ziele
• Bereiten Sie gerne Fragen vor

Bei Fragen erreichen Sie mich unter: info@autonova.de

Bis bald!
[Ihr Name]"

Reminder Email (24h vorher):
"Hallo [Name], 
morgen um [Zeit] haben wir unseren Termin für die Potenzial-Analyse.
Zoom-Link: [Link]
Falls sich etwas ändert, geben Sie mir gerne Bescheid!"
```

---

## ⚡ 5. ZAPIER AUTOMATISIERUNG (20-30 Min)

### **Schritt 1: Account erstellen**
1. Gehen Sie zu **zapier.com**
2. Registrieren Sie sich (Free Plan reicht für den Start)
3. Verbinden Sie Ihre Apps (HubSpot, Mailchimp, Calendly)

### **Schritt 2: Wichtige Zaps erstellen**

#### **Zap 1: Calendly → HubSpot**
```
Trigger: New Calendly Event Scheduled
Action: Create/Update Contact in HubSpot

Mapping:
- Email → Email
- Name → First Name + Last Name  
- Company → Company
- Phone → Phone
- Lead Source → "Calendly Booking"
- Interest Level → 8 (High - booked demo)

Additional Action: Create Deal
- Deal Name: "[Company] - Potenzial-Analyse"
- Stage: "Potenzial-Analyse"
- Amount: 1500 (average deal size)
```

#### **Zap 2: Mailchimp → HubSpot**
```
Trigger: New Mailchimp Subscriber
Action: Create/Update Contact in HubSpot

Mapping:
- Email → Email
- First Name → First Name
- Company → Company
- Lead Source → "Newsletter Signup"
- Interest Level → 3 (Medium - newsletter interest)

Additional Action: Add to Sequence
- Sequence: "Newsletter Subscriber Nurturing"
```

#### **Zap 3: HubSpot → Slack (Optional)**
```
Trigger: New Deal Created in HubSpot
Action: Send Slack Message

Message Template:
"🎯 Neuer Deal erstellt!
Unternehmen: [Company]
Kontakt: [Name]
Wert: [Amount]€
Quelle: [Lead Source]
Link: [Deal URL]"
```

### **Schritt 3: Testing & Aktivierung**
1. Testen Sie jeden Zap mit Testdaten
2. Überprüfen Sie die Datenübertragung
3. Aktivieren Sie alle Zaps
4. Überwachen Sie die ersten Tage auf Fehler

---

## ✅ SETUP-CHECKLISTE

### **Nach dem Setup sollten Sie haben:**

#### **HubSpot CRM:**
- [ ] Account eingerichtet und konfiguriert
- [ ] Custom Properties für Lead-Qualifizierung
- [ ] 7-stufige Sales-Pipeline
- [ ] 3 E-Mail-Templates
- [ ] 2 Automatisierungs-Workflows
- [ ] Lead-Scoring-System

#### **Mailchimp:**
- [ ] Audience mit Custom Fields
- [ ] 2 Signup-Forms (Newsletter + Lead Magnet)
- [ ] 2 E-Mail-Automatisierungen
- [ ] Newsletter-Template
- [ ] Analytics-Tracking aktiviert

#### **Google Analytics 4:**
- [ ] Property und Datenstream eingerichtet
- [ ] Tracking-Code auf Website installiert
- [ ] 3 Conversion-Ziele definiert
- [ ] Custom Dimensions konfiguriert

#### **Calendly:**
- [ ] Event Type "Potenzial-Analyse" erstellt
- [ ] Verfügbarkeitszeiten definiert
- [ ] Qualifizierungs-Fragen eingerichtet
- [ ] E-Mail-Templates angepasst

#### **Zapier:**
- [ ] 3 wichtige Zaps erstellt und getestet
- [ ] Datenfluss zwischen allen Tools
- [ ] Automatische Lead-Qualifizierung
- [ ] Slack-Benachrichtigungen (optional)

### **Gesamtzeit für komplettes Setup: 2-3 Stunden**

**Nach diesem Setup haben Sie ein vollautomatisiertes Lead-Management-System, das von der ersten Kontaktaufnahme bis zum Vertragsabschluss alles trackt und optimiert!**

