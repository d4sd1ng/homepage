# Neurova Platform - Technical Architecture Plan

## 🎯 ARCHITEKTUR-UEBERBLICK

### **Hybrid-Modell: Freemium per E-Mail, Premium als SaaS-Plattform**

5 Freemium-Produkte werden als **kostenlose digitale Assets per E-Mail/Download** geliefert (ChatGPT Prompts, Skripte, Templates). Diese sind die "Free Gifts" / Lead-Magnets.

29 Premium-Produkte werden als **SaaS-Plattform mit Dashboard** angeboten. Kunden zahlen ein Abo und nutzen die Module im Browser.

```
FREEMIUM (5x Free Gifts per E-Mail):
  Landingpage → E-Mail-Registrierung → Nurturing-Sequenz (email-agent)
  → Free Gift per E-Mail (Prompt/Skript/Template)
  → Upsell → SaaS-Plattform Abo

PREMIUM (29x SaaS-Plattform mit Dashboard):
  Landingpage → "Kostenlos testen" → SaaS-Registrierung
  → Dashboard mit gebuchten Modulen
  → Stripe Abo (monatlich/jaehrlich)
  → Module laufen serverseitig (bestehende Agenten-Architektur)
```

---

## 📊 BESTANDSAUFNAHME: VORHANDENER CODE

### **Vorhandene Agenten (als Produkt-Engine nutzbar):**

```
AGENT                      | ZEILEN | STATUS    | NUTZEN FUER PRODUKT-LIEFERUNG
---------------------------|--------|-----------|-------------------------------
email-agent/               | 6.059  | Produktiv | KERN: Nurturing + Produkt-Auslieferung
  ├── app.py               |   498  | Stable    | EmailAgent Core
  ├── newsletter_agent.py  | 1.424  | Stable    | Sequenzen + Produkt-E-Mails
  ├── trigger_engine.py    | 1.056  | Stable    | Stripe-Trigger → Liefer-E-Mail
  ├── gdpr_compliance.py   |   564  | Stable    | DSGVO + Consent
  ├── newsletter_scheduler |   504  | Stable    | Scheduling
  ├── ab_testing.py        |   408  | Stable    | A/B Tests
  ├── analytics_dashboard  |   324  | Stable    | Analytics
  ├── api_integrations.py  |   357  | Stable    | CRM + Notion
  ├── linkedin_templates   |   549  | Stable    | LinkedIn Content
  ├── phone_scripts.py     |   636  | Stable    | Telefon-Skripte
  └── load_sequences.py    |   240  | Stable    | Sequenz-Loader
thumbnail-generation-agent/|   992  | Produktiv | PRODUKT: Thumbnail-Skript (Download)
enhanced-seo-optimization/ |   931  | Produktiv | PRODUKT: SEO-Prompt-Pack (E-Mail)
orchestrator-agent/        |   599  | Produktiv | Task-Verteilung
auth-service-agent/        |   750  | Produktiv | Landingpage-Auth
billing-service-agent/     |   550  | Produktiv | KERN: Stripe Payment + Liefer-Trigger
rate-limiter-agent/        |   780  | Produktiv | API-Schutz
approval-agent/            | 1.053  | Produktiv | Freigabe-Workflows
content-approval-agent/    |   603  | Produktiv | Content-Freigabe
content-scheduler-agent/   |   830  | Produktiv | Content-Scheduling
server.py (zentral)        |   522  | Produktiv | API Server
---------------------------|--------|-----------|-------------------------------
GESAMT: ~14.200 Zeilen vorhanden
```

### **5 Freemium-Produkte (per E-Mail/Download geliefert):**

```
PRODUKT                   | FREE GIFT                          | DIENT ALS UPSELL FUER
---------------------------|------------------------------------|---------------------------
Thumbnail Generator        | thumbnail_generation-agent (.py)   | Thumbnail Modul im SaaS
Competitor Analysis        | ChatGPT Prompt + Anleitung         | Competitor Modul im SaaS
Performance Monitoring    | ChatGPT Prompt + Anleitung         | Monitoring Modul im SaaS
Database Optimization     | db-check Skript (.py)              | DB-Opt Modul im SaaS
Customer Journey Mapper   | ChatGPT Prompt + Template          | Journey Modul im SaaS
```

### **29 Premium-Produkte (SaaS-Plattform mit Dashboard):**

```
KATEGORIE                 | MODULE IM DASHBOARD
--------------------------|----------------------------------------------------
Content & Marketing (9)   | SEO Dominator, Social Media, Influencer, Content Calendar,
                          | Video Discovery, Script Gen, Trend Analysis,
                          | Email Marketing, Prompt Optimizer
BI & Analytics (7)        | BI Dashboard, Lead Scoring, Market Research,
                          | Competitor Analysis (Vollversion), Performance (Vollversion),
                          | Customer Journey (Vollversion), Trend Analysis (Vollversion)
Finance & Compliance (5)  | Financial Report, Legal Document, Contract Analysis,
                          | Invoice Processing, Security Audit
Operations & Infra (7)    | DB Optimization (Vollversion), Data Sync, Workflow Engine,
                          | Document Processing, QA Automation, Predictive Maintenance,
                          | API Integration Hub
CX & Sales (4)           | Customer Feedback, Sales Funnel, Brand Monitoring,
                          | Event Management
Industry-Specific (4)    | HR Analytics, Inventory Mgmt, Audio Extraction,
                          | Multi Platform Connector
```

---

## 🏗️ ARCHITEKTUR

### **Pfad 1: Freemium-Fluesse (5 Free Gifts per E-Mail)**

```
ABLAUF FREEMIUM:
  Landingpage → "Kostenlos testen" → E-Mail-Registrierung (Double-Opt-In)
  → email-agent startet Nurturing-Sequenz "freemium_{product_id}"
  → E-Mail 1 (sofort):    Free Gift (Prompt/Skript/Template direkt in E-Mail oder als Download-Link)
  → E-Mail 2 (Tag 2):     "Tipps fuer bessere Ergebnisse"
  → E-Mail 3 (Tag 5):     "Was dir in der Free-Version fehlt"
  → E-Mail 4 (Tag 8):     "So funktioniert die Vollversion im Dashboard"
  → E-Mail 5 (Tag 12):    Upgrade-Angebot: "Jetzt SaaS-Abo starten -30%"

LIEFERUNG DER FREE GIFTS:
  Prompt-Packs: Direkt in E-Mail-Body (formatiert)
  Skripte (.py): Download-Link in E-Mail (72h gueltig, max 3 Downloads)
  Templates: Download-Link in E-Mail
```

### **Pfad 2: SaaS-Plattform (29 Premium-Module)**

```
ABLAUF PREMIUM:
  Landingpage → "Jetzt testen" → SaaS-Registrierung
  → auth-service-agent: Login + JWT
  → billing-service-agent: Stripe Checkout (Abo)
  → Dashboard mit gebuchten Modulen
  → Module laufen serverseitig (bestehende Agenten-Architektur)
  → orchestrator-agent verteilt Tasks an Modul-Agenten
  → Ergebnisse im Dashboard angezeigt

SAAS-ARCHITEKTUR (wie im urspruenglichen Plan):
  KUNDE → neurova.de (React Dashboard) → API Gateway → Agenten (Module)
                                                    → PostgreSQL (Multi-Tenant)
                                                    → Redis (Cache/Queue)
                                                    → Hetzner Cloud (DE)

SAAS-MODULE IM DASHBOARD:
  Jeder Agent folgt dem GenericModuleAgent Interface:
    async def execute(task_data) → Haupt-Logik
    async def get_status() → Status
    async def list_jobs() → Job-Historie
    async def get_usage() → Verbrauch
```

### **Free Gift Assets (was per E-Mail geliefert wird)**

```
THUMBNAIL GENERATOR (Skript-Download):
□ thumbnail_generator.py      → Ausfuehrbares Skript (Free-Version: 5/Monat)
□ config.yaml                 → Konfiguration
□ requirements.txt            → Python-Abhaengigkeiten
□ README.md                   → Anleitung
→ Vollversion im SaaS: Unlimited, Serverseitig, Batch-Verarbeitung

COMPETITOR ANALYSIS (Prompt per E-Mail):
□ system_prompt.md            → ChatGPT System-Prompt
□ user_prompts.md             → 5 User-Prompts
□ anleitung.md                → Schritt-fuer-Schritt
→ Vollversion im SaaS: API-gestuetzt, Automatisiert, Export

PERFORMANCE MONITORING (Prompt per E-Mail):
□ system_prompt.md            → ChatGPT System-Prompt
□ user_prompts.md             → 5 User-Prompts
□ anleitung.md                → Anleitung
→ Vollversion im SaaS: Kontinuierliches Monitoring, Alerts, Dashboard

DATABASE OPTIMIZATION (Skript-Download):
□ db_check.py                 → Check-Skript (Free: 1 Tabelle)
□ config.yaml                 → Konfiguration
□ README.md                   → Anleitung
→ Vollversion im SaaS: Alle Tabellen, Auto-Fix, Scheduled Scans

CUSTOM JOURNEY MAPPER (Prompt + Template per E-Mail):
□ system_prompt.md            → ChatGPT System-Prompt
□ template.json               → Journey-Template
□ anleitung.md                → Anleitung
→ Vollversion im SaaS: Visueller Editor, Multi-Journey, Export
```

### **Komponente 4: Nurturing-Funnel (bestehender email-agent)**

```
FUNNEL-ABLAUF:

[FREEMIUM-PFAD]
  Landingpage → "Kostenlos testen" → /api/freemium/{product_id}
  → E-Mail-Registrierung (Double-Opt-In)
  → Nurturing-Sequenz "freemium_{product_id}"
    E-Mail 1 (sofort):    "Hier ist dein kostenloser Zugang"
    E-Mail 2 (Tag 2):     "Tipps fuer bessere Ergebnisse"
    E-Mail 3 (Tag 5):     "So sparst du Zeit mit der Vollversion"
    E-Mail 4 (Tag 8):     "Was dir in der Free-Version fehlt"
    E-Mail 5 (Tag 12):    "Upgrade-Angebot: -30% nur heute"

[PREMIUM-PFAD]
  Landingpage → "Vollversion kaufen" → Stripe Checkout
  → Stripe Webhook → /api/webhook/stripe
  → Trigger: "payment_succeeded"
  → Nurturing-Sequenz "premium_{product_id}"
    E-Mail 1 (sofort):    "Dein Download-Link" (72h gueltig)
    E-Mail 2 (Tag 1):     "Einrichtungshilfe"
    E-Mail 3 (Tag 3):     "Fortgeschrittene Tipps"
    E-Mail 4 (Tag 7):     "Weitere Produkte fuer dich"
    E-Mail 5 (Tag 14):    "Feedback-Anfrage + Cross-Sell"

[NEWSLETTER-PFAD (bestehend)]
  neurova.de → E-Mail-Registrierung
  → Nurturing-Sequenz "newsletter"
    Woechentlich: KI-Tipps + Produkt-Updates + Freemium-Angebote
```

---

## 💾 DATABASE SCHEMA (vereinfacht, SQLite oder PostgreSQL)

```sql
-- SUBSCRIBERS (bestehend, erweitert)
CREATE TABLE subscribers (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email           VARCHAR(255) UNIQUE NOT NULL,
    name            VARCHAR(100),
    source          VARCHAR(50) DEFAULT 'landingpage',
    status          VARCHAR(20) DEFAULT 'active',
    gdpr_consent    BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- PRODUCTS
CREATE TABLE products (
    id              VARCHAR(50) PRIMARY KEY,       -- 'competitor-analysis'
    name            VARCHAR(100) NOT NULL,
    category        VARCHAR(50) NOT NULL,
    delivery_type   VARCHAR(10) NOT NULL,          -- 'prompt'/'script'/'template'
    is_freemium     BOOLEAN DEFAULT FALSE,
    freemium_content TEXT,                         -- Was in der Free-E-Mail geliefert wird
    stripe_price_id VARCHAR(100),                  -- Stripe Price ID fuer Premium
    price_cents     INTEGER DEFAULT 0,             -- Einmalpreis in Cent
    description     TEXT,
    download_path   VARCHAR(500),                  -- Pfad zur .zip im Object Storage
    active          BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- PURCHASES (Kaeufe)
CREATE TABLE purchases (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subscriber_id   UUID REFERENCES subscribers(id),
    product_id      VARCHAR(50) REFERENCES products(id),
    stripe_session_id VARCHAR(100),
    amount_cents    INTEGER NOT NULL,
    status          VARCHAR(20) DEFAULT 'completed',
    download_token  VARCHAR(100) UNIQUE,           -- Einmal-Download-Token
    download_expires TIMESTAMPTZ,                  -- 72h gueltig
    download_count  INTEGER DEFAULT 0,             -- Max 3 Downloads
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- SEQUENCE_TRACKING (welche Sequenz wird gerade geliefert)
CREATE TABLE sequence_tracking (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subscriber_id   UUID REFERENCES subscribers(id),
    product_id      VARCHAR(50) REFERENCES products(id),
    sequence_type   VARCHAR(20) NOT NULL,          -- 'freemium'/'premium'/'newsletter'
    current_step    INTEGER DEFAULT 0,
    status          VARCHAR(20) DEFAULT 'active',   -- active/completed/unsubscribed
    started_at      TIMESTAMPTZ DEFAULT NOW(),
    completed_at    TIMESTAMPTZ
);

-- INDEXES
CREATE INDEX idx_subscribers_email ON subscribers(email);
CREATE INDEX idx_purchases_subscriber ON purchases(subscriber_id);
CREATE INDEX idx_purchases_product ON purchases(product_id);
CREATE INDEX idx_sequence_subscriber ON sequence_tracking(subscriber_id, product_id);
```

---

## 🔌 PRODUKT-KATALOG: PREISE + LIEFERUNG

### **5 Freemium-Produkte (0€, E-Mail-Lieferung):**

```
PRODUKT                   | LIEFERUNG        | FREE-INHALT                            | UPS
---------------------------|------------------|----------------------------------------|-----------------------
Thumbnail Generator        | E-Mail + Download| thumbnail_generation-agent.py (Free)   | Vollversion: 29€
Competitor Analysis        | E-Mail (Prompt)  | Basis-Prompt + 3 Szenarien            | Prompt-Pack: 19€
Performance Monitoring     | E-Mail (Prompt)  | Basis-Check-Prompt                     | Prompt-Pack: 19€
Database Optimization      | E-Mail + Download| db-check Skript (1 Tabelle)           | Vollversion: 29€
Customer Journey Mapper    | E-Mail (Prompt)  | Basis-Prompt + 1 Template              | Prompt-Pack: 19€
```

### **29 Premium-Produkte (Einmalzahlung):**

```
PRODUKT                          | PREIS  | LIEFERUNG
----------------------------------|--------|------------------------------------------
--- PROMPT PACKS (17x) ---
SEO Dominator                    |  29€   | E-Mail + Download (.zip mit 5+ Prompts)
Social Media Automation          |  19€   | E-Mail + Download (.zip)
Influencer Outreach              |  19€   | E-Mail + Download (.zip)
Content Calendar                 |  19€   | E-Mail + Download (.zip)
Video Discovery & Repurposing   |  19€   | E-Mail + Download (.zip)
Script Generation                |  19€   | E-Mail + Download (.zip)
Trend Analysis                   |  19€   | E-Mail + Download (.zip)
Prompt Optimizer                 |  14€   | E-Mail (Prompt direkt)
Business Intelligence Dashboard  |  29€   | E-Mail + Download (.zip)
Market Research Automation       |  19€   | E-Mail + Download (.zip)
Lead Scoring Engine              |  29€   | E-Mail + Download (.zip)
Legal Document Analyzer          |  29€   | E-Mail + Download (.zip)
Contract Analysis Tool           |  19€   | E-Mail + Download (.zip)
Customer Feedback Analysis       |  19€   | E-Mail + Download (.zip)
Brand Monitoring                 |  19€   | E-Mail + Download (.zip)
Quality Assurance Automation     |  19€   | E-Mail + Download (.zip)
HR Analytics                     |  19€   | E-Mail + Download (.zip)
--- SCRIPT PACKS (11x) ---
Financial Report Generator       |  49€   | E-Mail + Download (.zip mit .py)
Security Audit Automation        |  49€   | E-Mail + Download (.zip mit .py)
Invoice Processing               |  29€   | E-Mail + Download (.zip mit .py)
Data Synchronization             |  39€   | E-Mail + Download (.zip mit .py)
Document Processing              |  29€   | E-Mail + Download (.zip mit .py)
Predictive Maintenance           |  39€   | E-Mail + Download (.zip mit .py)
Inventory Management AI          |  39€   | E-Mail + Download (.zip mit .py)
Audio Extraction Service         |  29€   | E-Mail + Download (.zip mit .py)
--- TEMPLATE PACKS (6x) ---
Email Marketing Optimizer        |  29€   | E-Mail + Download (.zip)
Workflow Automation Engine       |  19€   | E-Mail + Download (.zip)
API Integration Hub              |  19€   | E-Mail + Download (.zip)
Sales Funnel Optimizer           |  19€   | E-Mail + Download (.zip)
Event Management                 |  19€   | E-Mail + Download (.zip)
Multi Platform Connector         |  19€   | E-Mail + Download (.zip)
```

**BUNDLE-ANGEBOTE:**
```
ALLE 5 FREEMIUM                    → Kostenlos (E-Mail-Registrierung)
CONTENT & MARKETING BUNDLE (9)     →  99€ (statt 169€ einzeln)
BI & ANALYTICS BUNDLE (7)          →  89€ (statt 143€ einzeln)
FINANCE & COMPLIANCE BUNDLE (5)    →  99€ (statt 145€ einzeln)
OPERATIONS & INFRA BUNDLE (7)      →  99€ (statt 193€ einzeln)
CX & SALES BUNDLE (4)             →  59€ (statt 76€ einzeln)
INDUSTRY BUNDLE (4)               →  69€ (statt 106€ einzeln)
KOMPLETT-PAKET (alle 34)           → 399€ (statt ~830€ einzeln)
```

---

## 💳 PREIS-MODELL (Hybrid: Freemium-Downloads + SaaS-Abo)

```
FREEMIUM (5 FREE GIFTS per E-Mail):
□ Kostenlos, nur E-Mail-Registrierung erforderlich
□ Thumbnail Skript: 5/Monat Limit
□ Competitor Prompt: Basis-Version
□ Performance Prompt: Basis-Version
□ DB-Check Skript: 1 Tabelle
□ Journey Prompt + Template: Basis-Version
→ Ziel: Nutzer kennenlernen → Upsell zum SaaS-Abo

SAAS-ABO TIERS (fuer 29 Premium-Module im Dashboard):

STARTER - 49€/MONAT:
□ 3 Module (ausser Freemium)
□ 1.000 Credits/Monat
□ 30 Tage Historie
□ E-Mail Support
□ + Jedes zusaetzliche Modul: 19€/Monat

PROFESSIONAL - 149€/MONAT:
□ 7 Module (ausser Freemium)
□ 5.000 Credits/Monat
□ 90 Tage Historie
□ E-Mail + Chat Support
□ API-Zugang
□ + Jedes zusaetzliche Modul: 15€/Monat

BUSINESS - 399€/MONAT:
□ 15 Module
□ 25.000 Credits/Monat
□ 365 Tage Historie
□ Priority Support
□ API + Webhooks
□ + Jedes zusaetzliche Modul: 10€/Monat

ENTERPRISE - 999€/MONAT:
□ Alle Module
□ Unlimited Credits
□ Unlimited Historie
□ Dedicated Support + SLA
□ SSO/SAML

CONVERSION-PFAD:
  Free Gift → "Das ist toll!" → Upsell-E-Mail → SaaS-Abo
  Conversion-Ziel: 5-10% der Freemium-Nutzer
```

---

## 🚀 IMPLEMENTIERUNGS-ROADMAP

### **SPRINT 1 (Woche 1-2): 5 Free Gifts erstellen**

```
WOCHE 1: 5 FREEMIUM-PRODUKTE (Free Gifts per E-Mail)
□ Thumbnail Generator: bestehenden Agenten als standalone .py paketieren
  - thumbnail_generation-agent/app.py → thumbnail_generator.py (standalone)
  - config.yaml + requirements.txt + README.md + setup.sh
  - Free-Version: 5 Thumbnails/Monat Limit einbauen
□ Competitor Analysis: ChatGPT Prompt-Pack erstellen
  - system_prompt.md + user_prompts.md (5 Szenarien)
  - variablen.md + beispiel_output.md + anleitung.md
□ Performance Monitoring: ChatGPT Prompt-Pack
□ Database Optimization: db-check Skript (.py)
□ Customer Journey Mapper: ChatGPT Prompt-Pack + Template

WOCHE 2: FREEMIUM LANDINGPAGES + DELIVERY
□ 5 Freemium-Landingpages (eine pro Free Gift)
□ 5 Nurturing-Sequenzen (je 5 E-Mails + Upsell)
□ Download-Link-System: Token-basiert, 72h gueltig, max 3 Downloads
□ End-to-End Test: Registrierung → E-Mail → Download
```

### **SPRINT 2 (Woche 3-6): SaaS-Plattform Core + erste 3 Module**

```
WOCHE 3: DATABASE + AUTH
□ PostgreSQL Schema (Multi-Tenant)
□ auth-service-agent: Register/Login/JWT mit tenant_id
□ Stripe Customer Creation bei Register

WOCHE 4: BILLING + API GATEWAY
□ billing-service-agent: Stripe Checkout (4 Abo-Tiers)
□ Webhook-Handler + Customer Portal
□ Credit-System + Usage-Tracking
□ server.py: /api/v1/ Route-Struktur + Tenant-Middleware

WOCHE 5: ORCHESTRATOR + MODULE REGISTRY
□ orchestrator-agent: Module Registry + Job-Tracking
□ GenericModuleAgent Basisklasse
□ React Dashboard Setup (Vite + React 18 + TypeScript)

WOCHE 6: FIRST 3 SaaS-MODULE
□ thumbnail-generation-agent → ModuleAgent adaptieren (Vollversion)
□ enhanced-seo-optimization → ModuleAgent adaptieren
□ email-agent (Marketing-Teile) → ModuleAgent adaptieren
□ Dashboard: Login + Module-Uebersicht + Billing
```

### **SPRINT 3 (Woche 7-12): Weitere SaaS-Module + Dashboard**

```
WOCHE 7-8: BI & ANALYTICS MODULE
□ Competitor Analysis (Vollversion im Dashboard)
□ Customer Journey Mapper (Vollversion)
□ Performance Monitoring (Vollversion)
□ Database Optimization (Vollversion)
□ Lead Scoring Engine

WOCHE 9-10: FINANCE & COMPLIANCE MODULE
□ Financial Report Generator
□ Legal Document Analyzer
□ Security Audit Automation
□ Invoice Processing

WOCHE 11-12: CONTENT & MARKETING + OPS MODULE
□ Social Media Automation
□ Content Calendar
□ Data Synchronization
□ Workflow Automation
□ Je Modul: React-Komponente + API-Endpunkte
```

### **SPRINT 4 (Woche 13-16): Restliche Module + Enterprise**

```
WOCHE 13-14: RESTLICHE 15 MODULE
□ Alle verbleibenden Module als GenericModuleAgent
□ Modul-spezifische React-Komponenten

WOCHE 15-16: ENTERPRISE + LAUNCH
□ SSO/SAML Integration
□ API-Dokumentation
□ Performance-Optimierung
□ Launch!
```

---

## 📁 PROJEKTSTRUKTUR (Ziel-Zustand)

```
neurova-products/
├── docker-compose.yml              # Backend-Services
├── .env.example
│
├── products/                       # 34 digitale Produkte
│   ├── freemium/                   # 5 kostenlose Produkte
│   │   ├── thumbnail-generator/
│   │   │   ├── thumbnail_generator.py
│   │   │   ├── config.yaml
│   │   │   ├── requirements.txt
│   │   │   ├── setup.sh
│   │   │   └── README.md
│   │   ├── competitor-analysis/
│   │   │   ├── system_prompt.md
│   │   │   ├── user_prompts.md
│   │   │   ├── variablen.md
│   │   │   ├── beispiel_output.md
│   │   │   └── anleitung.md
│   │   ├── performance-monitoring/
│   │   ├── database-optimization/
│   │   └── customer-journey/
│   │
│   └── premium/                    # 29 kostenpflichtige Produkte
│       ├── prompt-packs/           # 17 ChatGPT Prompt-Packs
│       │   ├── seo-dominator/
│       │   ├── social-media-automation/
│       │   ├── influencer-outreach/
│       │   └── ... (14 weitere)
│       ├── script-packs/           # 11 Python Skript-Packs
│       │   ├── financial-report/
│       │   │   ├── financial_report.py
│       │   │   ├── config.yaml
│       │   │   ├── requirements.txt
│       │   │   ├── templates/
│       │   │   │   ├── bilanz_template.xlsx
│       │   │   │   └── guv_template.xlsx
│       │   │   ├── setup.sh
│       │   │   └── README.md
│       │   ├── security-audit/
│       │   └── ... (9 weitere)
│       └── template-packs/         # 6 Template-Packs
│           ├── workflow-automation/
│           │   ├── workflows/
│           │   │   ├── lead_nurturing.yaml
│           │   │   └── content_pipeline.yaml
│           │   ├── prompt.md
│           │   └── README.md
│           └── ... (5 weitere)
│
├── landingpages/                  # Statische HTML-Landingpages
│   ├── index.html                 → Hauptseite (alle Produkte)
│   ├── thumbnail-generator.html
│   ├── competitor-analysis.html
│   ├── seo-dominator.html
│   └── ... (eine pro Produkt)
│
├── sequences/                     # Nurturing-Sequenzen
│   ├── freemium_thumbnail.json
│   ├── freemium_competitor.json
│   ├── premium_seo-dominator.json
│   ├── premium_financial-report.json
│   └── ... (eine pro Produkt + Newsletter)
│
├── email-templates/               # HTML E-Mail-Templates
│   ├── freemium_delivery.html
│   ├── premium_delivery.html
│   ├── upsell.html
│   └── newsletter.html
│
└── backend/                       # Bestehende Autonova-Services
    ├── server.py
    ├── email-agent/
    ├── billing-service-agent/
    ├── orchestrator-agent/
    └── ... (unveraendert)
```

---

## 🔧 PROMPT-PACK TEMPLATE (fuer Modell A)

```
Jedes Prompt-Pack enthaelt 6 Dateien:
1. system_prompt.md   → Haupt-Prompt (Copy-Paste in ChatGPT)
2. user_prompts.md    → 5-10 User-Prompts fuer verschiedene Szenarien
3. variablen.md       → Platzhalter-Definitionen
4. beispiel_output.md → 2-3 Beispiel-Antworten
5. anleitung.md       → Schritt-fuer-Schritt Nutzung
6. tipps.md           → Profi-Tipps + Fehlervermeidung
Lieferung: Direkt in E-Mail-Body (formatiert) oder als .zip Download-Link
```

## 🔧 SKRIPT-PACK TEMPLATE (fuer Modell B)

```
Jedes Skript-Paket enthaelt:
1. produktname.py     → Ausfuehrbares Skript
2. config.yaml        → Konfiguration (API-Keys, Pfade)
3. requirements.txt   → Python-Abhaengigkeiten
4. setup.sh           → Ein-Klick-Setup
5. README.md          → Anleitung
6. beispiele/         → Beispiel-Input/Output
Lieferung: .zip Download-Link in E-Mail (72h gueltig)
```

---

## 💰 KOSTEN-UEBERSICHT (Monatlich, stark reduziert)

```
HETZNER CLOUD (DE):
□ CX11 Server (1 vCPU, 2GB RAM): 4,50€/Monat (nur API + Nginx)
□ PostgreSQL oder SQLite: 0€ (SQLite im Container)
□ Domain neurova.de: 6€/Monat
□ Hetzner Gesamt: ~10,50€/Monat

STRIPE:
□ Transaktionsgebuehr: 1,4% + 0,25€ (DE)
□ Monatliche Gebuehr: 0€

RESEND (SMTP):
□ Free Tier: 100 E-Mails/Tag = 0€

OPENAI API:
□ Nur fuer interne Demo-Generierung: ~5-20€/Monat

GESAMT FIXKOSTEN: ~10-30€/Monat
BREAK-EVEN: 1-2 Premium-Kaeufe (19-49€)

VERGLEICH ZUM ALTEN PLAN:
Alt (SaaS-Platform): ~48-268€/Monat
Neu (Digital Products): ~10-30€/Monat  → 80-90% GUENSTIGER
```

---

## ✅ CHECKLISTE: VON KONZEPT ZU PRODUKT

```
PRO PROMPT PACK (17x):
1. KONZEPT VORHANDEN              ☑ (alle da, ~1.200 Zeilen)
2. system_prompt.md erstellen     ☐ (Haupt-Prompt)
3. user_prompts.md erstellen      ☐ (5-10 Szenarien)
4. variablen.md erstellen         ☐ (Platzhalter)
5. beispiel_output.md erstellen   ☐ (2-3 Beispiele)
6. anleitung.md erstellen         ☐ (Schritt-fuer-Schritt)
7. tipps.md erstellen             ☐ (Profi-Tipps)
8. Stripe Product + Price anlegen ☐
9. Landingpage erstellen          ☐
10. Nurturing-Sequenz erstellen   ☐ (5 E-Mails)
11. End-to-End Test               ☐

PRO SKRIPT PACK (11x):
1. KONZEPT VORHANDEN              ☑ (alle da)
2. produktname.py schreiben       ☐ (Business-Logik)
3. config.yaml erstellen          ☐ (Konfiguration)
4. requirements.txt erstellen     ☐ (Abhaengigkeiten)
5. setup.sh erstellen             ☐ (Ein-Klick-Setup)
6. README.md erstellen            ☐ (Anleitung)
7. beispiele/ erstellen           ☐ (Input/Output)
8. Stripe Product + Price anlegen ☐
9. Landingpage erstellen          ☐
10. Nurturing-Sequenz erstellen   ☐ (5 E-Mails)
11. End-to-End Test               ☐

PRO TEMPLATE PACK (6x):
1. KONZEPT VORHANDEN              ☑ (alle da)
2. templates/ erstellen           ☐ (.json/.yaml/.md)
3. prompt.md erstellen            ☐ (配套 Prompt)
4. README.md erstellen            ☐ (Anleitung)
5. Stripe Product + Price anlegen ☐
6. Landingpage erstellen          ☐
7. Nurturing-Sequenz erstellen   ☐ (5 E-Mails)
8. End-to-End Test               ☐
```

**Status: 34 Konzepte ✓ | 0 Produkte ausgeliefert | ~14.200 Zeilen Backend-Code vorhanden | Launch in 8 Wochen**