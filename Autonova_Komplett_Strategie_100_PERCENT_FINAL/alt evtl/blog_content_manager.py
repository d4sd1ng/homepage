#!/usr/bin/env python3
"""
Blog Content Manager: CSV anreichern + Email-Agent + Notion Import
B) CSV mit individuellen Inhalten anreichern
C) Nurturing-E-Mail-Jobs fuer email-agent erstellen
A) In Notion Content-Stuecke DB importieren

Usage:
    python blog_content_manager.py --csv "path/to/AIxTools_Blogs_DE_EN.csv"
    python blog_content_manager.py --csv "path/to/AIxTools_Blogs_DE_EN.csv" --notion
"""

import csv
import json
import os
import sys
import argparse
import asyncio
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# --- Unique content templates for 34 blog posts + 42 landing pages ---
BLOG_TITLES_DE = [
    "Realistische KI-Avatare: Wie sie den Kundenservice revolutionieren",
    "Virtuelle Moderatoren: KI-Avatare auf Messen und Events",
    "KI-Avatare fuer E-Learning: Personalisierte Lernerfahrungen",
    "Social Media mit KI-Avataren: 10x mehr Engagement",
    "Rechtliche Aspekte von KI-Avataren: Was Sie wissen muessen",
    "KI-Avatare vs. Stock-Fotos: Warum Avatare gewinnen",
    "Die Psychologie hinter effektiven KI-Avataren",
    "KI-Avatare fuer HR: Onboarding und Schulung automatisieren",
    "DIY KI-Avatar: In 15 Minuten zum eigenen virtuellen Gespraechspartner",
    "KI-Avatare in der Medizin: Patientenaufklaerung neu gedacht",
    "Multilingualle KI-Avatare: Global kommunizieren ohne Grenzen",
    "KI-Avatare fuer Immobilien: Virtuelle Hausfuehrungen 2.0",
    "Die Ethik der KI-Avatare: Wo ziehen wir die Grenze?",
    "KI-Avatare im Einzelhandel: Persoenliche Beratung 24/7",
    "Von der Stimme zum Avatar: KI-Voice-Cloning im Ueberblick",
    "KI-Avatare fuer Webinare: Nie wieder live auftreten",
    "Die Technologie hinter KI-Avataren: Deep Dive",
    "KI-Avatare und Markenidentitaet: Konsistenz ueber alle Kanaele",
    "ROI von KI-Avataren: Zahlen die ueberzeugen",
    "KI-Avatare fuer Non-Profit: Spenden und Aufklaerung",
    "Die Zukunft der KI-Avatare: Trends 2025-2030",
    "KI-Avatare vs. Chatbots: Wann welcher Ansatz besser ist",
    "KI-Avatare fuer Produkt-Demos: Conversion-Raten steigern",
    "Datenschutz bei KI-Avataren: DSGVO-konform umsetzen",
    "KI-Avatare fuer den oeffentlichen Dienst: Buergerkommunikation",
    "Emotionale KI-Avatare: Empathie in der digitalen Kommunikation",
    "KI-Avatare fuer Restaurants: Virtuelle Speisekarten-Berater",
    "A/B-Testing mit KI-Avataren: Was wirklich funktioniert",
    "KI-Avatare und Barrierefreiheit: Inklusive Kommunikation",
    "KI-Avatare im Finanzsektor: Beratung und Aufklaerung",
    "Die besten KI-Avatar-Tools im Vergleich 2025",
    "KI-Avatare fuer Recruiting: Bewerbungsgespraechs-Simulation",
    "KI-Avatare und SEO: Wie Avatare Ihre Sichtbarkeit verbessern",
    "Live-KI-Avatare: Echtzeit-Interaktion mit Kunden",
]

LP_TITLES_DE = [
    "KI-Avatar Landing Page: Erste Eindruecke zaehlen",
    "Landing Page Optimierung mit KI-Avataren: Best Practices",
    "Die ultimative KI-Avatar Demo-Landing-Page",
    "Conversion-Optimierung: KI-Avatare auf Landing Pages",
    "KI-Avatar Showcases: Landing Pages die konvertieren",
    "Trust-Building mit KI-Avataren auf Landing Pages",
    "KI-Avatar Pricing Pages: Transparente Kommunikation",
    "KI-Avatar Feature-Landing-Pages: Highlights visualisieren",
    "Branchen-spezifische KI-Avatar Landing Pages",
    "KI-Avatar Vergleichs-Landing-Pages: Sie gewinnen",
    "Mobile-First KI-Avatar Landing Pages",
    "KI-Avatar Testimonial-Landing-Pages mit virtuellen Stimmen",
    "KI-Avatar Integration-Landing-Pages: API Highlights",
    "KI-Avatar Sicherheits-Landing-Page: Vertrauen schaffen",
    "KI-Avatar Case-Study-Landing-Pages: Echte Ergebnisse",
    "KI-Avatar Onboarding-Landing-Page: Schnellstart-Guide",
    "KI-Avatar ROI-Rechner Landing Page",
    "KI-Avatar Whitepaper-Landing-Page: Lead-Generierung",
    "KI-Avatar Webinar-Landing-Page: Anmeldungen steigern",
    "KI-Avatar Free-Trial Landing Page: Zum Testen einladen",
    "KI-Avatar Enterprise-Landing-Page: B2B-Optimiert",
    "KI-Avatar Startup-Landing-Page: Kosteneffizient einsteigen",
    "KI-Avatar DSGVO-Landing-Page: Compliance sichtbar machen",
    "KI-Avatar Multilingual Landing Page: International gewinnt",
    "KI-Avatar Dark-Mode Landing Page: Modern und ansprechend",
    "KI-Avatar Video-Landing-Page: Demo direkt erleben",
    "KI-Avatar FAQ-Landing-Page: Fragen automatisch beantworten",
    "KI-Avatar Vergleichs-Tabelle Landing Page",
    "KI-Avatar Erfolgsgeschichten Landing Page",
    "KI-Avatar Blog-Hub Landing Page: Content-Bibliothek",
    "KI-Avatar Partner-Landing-Page: Integrationen zeigen",
    "KI-Avatar Roadmap-Landing-Page: Transparenz schaffen",
    "KI-Avatar Community-Landing-Page: Nutzer vorzeigen",
    "KI-Avatar Black-Friday Landing Page: Zeitlich begrenzt",
    "KI-Avatar Jahresrueckblick Landing Page",
    "KI-Avatar Neujahrs-Landing-Page: Vorsaezte mit KI",
    "KI-Avatar Q1-Review Landing Page: Erfolge feiern",
    "KI-Avatar Sommer-Campaign Landing Page",
    "KI-Avatar Back-to-Business Landing Page",
    "KI-Avatar Produkt-Update Landing Page",
    "KI-Avatar Refer-a-Friend Landing Page",
    "KI-Avatar Early-Bird Landing Page: Fruehbucher-Vorteil",
]

BLOG_TITLES_EN = [
    "Realistic AI Avatars: How They Revolutionize Customer Service",
    "Virtual Moderators: AI Avatars at Trade Shows and Events",
    "AI Avatars for E-Learning: Personalized Learning Experiences",
    "Social Media with AI Avatars: 10x More Engagement",
    "Legal Aspects of AI Avatars: What You Need to Know",
    "AI Avatars vs. Stock Photos: Why Avatars Win",
    "The Psychology Behind Effective AI Avatars",
    "AI Avatars for HR: Automate Onboarding and Training",
    "DIY AI Avatar: Your Own Virtual Spokesperson in 15 Minutes",
    "AI Avatars in Healthcare: Patient Education Reimagined",
    "Multilingual AI Avatars: Communicate Globally Without Borders",
    "AI Avatars for Real Estate: Virtual Tours 2.0",
    "The Ethics of AI Avatars: Where Do We Draw the Line?",
    "AI Avatars in Retail: Personalized Advice 24/7",
    "From Voice to Avatar: AI Voice Cloning Overview",
    "AI Avatars for Webinars: Never Present Live Again",
    "The Technology Behind AI Avatars: A Deep Dive",
    "AI Avatars and Brand Identity: Consistency Across Channels",
    "ROI of AI Avatars: Numbers That Convince",
    "AI Avatars for Non-Profits: Fundraising and Awareness",
    "The Future of AI Avatars: Trends 2025-2030",
    "AI Avatars vs. Chatbots: Which Approach Works Better When",
    "AI Avatars for Product Demos: Boost Conversion Rates",
    "Data Privacy with AI Avatars: GDPR-Compliant Implementation",
    "AI Avatars for Public Services: Citizen Communication",
    "Emotional AI Avatars: Empathy in Digital Communication",
    "AI Avatars for Restaurants: Virtual Menu Consultants",
    "A/B Testing with AI Avatars: What Really Works",
    "AI Avatars and Accessibility: Inclusive Communication",
    "AI Avatars in Finance: Advisory and Education",
    "Best AI Avatar Tools Compared 2025",
    "AI Avatars for Recruiting: Interview Simulation",
    "AI Avatars and SEO: How Avatars Boost Visibility",
    "Live AI Avatars: Real-Time Customer Interaction",
]

LP_TITLES_EN = [
    "AI Avatar Landing Page: First Impressions Count",
    "Landing Page Optimization with AI Avatars: Best Practices",
    "The Ultimate AI Avatar Demo Landing Page",
    "Conversion Optimization: AI Avatars on Landing Pages",
    "AI Avatar Showcases: Landing Pages That Convert",
    "Trust-Building with AI Avatars on Landing Pages",
    "AI Avatar Pricing Pages: Transparent Communication",
    "AI Avatar Feature Landing Pages: Visualize Highlights",
    "Industry-Specific AI Avatar Landing Pages",
    "AI Avatar Comparison Landing Pages: You Win",
    "Mobile-First AI Avatar Landing Pages",
    "AI Avatar Testimonial Landing Pages with Virtual Voices",
    "AI Avatar Integration Landing Pages: API Highlights",
    "AI Avatar Security Landing Page: Build Trust",
    "AI Avatar Case Study Landing Pages: Real Results",
    "AI Avatar Onboarding Landing Page: Quick Start Guide",
    "AI Avatar ROI Calculator Landing Page",
    "AI Avatar Whitepaper Landing Page: Lead Generation",
    "AI Avatar Webinar Landing Page: Boost Signups",
    "AI Avatar Free Trial Landing Page: Invite to Test",
    "AI Avatar Enterprise Landing Page: B2B Optimized",
    "AI Avatar Startup Landing Page: Cost-Efficient Entry",
    "AI Avatar GDPR Landing Page: Make Compliance Visible",
    "AI Avatar Multilingual Landing Page: Win Internationally",
    "AI Avatar Dark Mode Landing Page: Modern and Appealing",
    "AI Avatar Video Landing Page: Experience Demo Directly",
    "AI Avatar FAQ Landing Page: Auto-Answer Questions",
    "AI Avatar Comparison Table Landing Page",
    "AI Avatar Success Stories Landing Page",
    "AI Avatar Blog Hub Landing Page: Content Library",
    "AI Avatar Partner Landing Page: Show Integrations",
    "AI Avatar Roadmap Landing Page: Create Transparency",
    "AI Avatar Community Landing Page: Showcase Users",
    "AI Avatar Black Friday Landing Page: Limited Time",
    "AI Avatar Year in Review Landing Page",
    "AI Avatar New Year Landing Page: Resolutions with AI",
    "AI Avatar Q1 Review Landing Page: Celebrate Wins",
    "AI Avatar Summer Campaign Landing Page",
    "AI Avatar Back-to-Business Landing Page",
    "AI Avatar Product Update Landing Page",
    "AI Avatar Refer-a-Friend Landing Page",
    "AI Avatar Early Bird Landing Page: First-Mover Advantage",
]

INTRO_DE = [
    "Immer mehr Unternehmen setzen auf KI-Avatare – aber nur wenige nutzen sie richtig. {topic} ist ein Bereich, der besonders viele Chancen bietet. Hier ist, was du wissen musst.",
    "Die Welt der KI-Avatare entwickelt sich rasant. {topic} bietet enorme Potenziale – und einige Herausforderungen. Lass uns einen genaueren Blick werfen.",
    "Wenn du dich fragst, ob sich {topic} fuer dein Unternehmen lohnt, bist du hier richtig. Konkrete Zahlen, echte Beispiele und ein klarer Umsetzungsplan.",
    "Viele Unternehmen zaudern bei {topic} – und verpassen einen echten Wettbewerbsvorteil. Dieser Artikel gibt dir die Infos fuer eine fundierte Entscheidung.",
    "KI-Avatare sind kein Hype mehr, sondern ein bewaehrtes Werkzeug. {topic} liefert direkt messbare Ergebnisse. Lass uns eintauchen.",
]

INTRO_EN = [
    "More companies are adopting AI avatars – but few use them correctly. {topic} offers particular opportunities. Here is what you need to know.",
    "The world of AI avatars is evolving rapidly. {topic} offers enormous potential – and some challenges. Let's take a closer look.",
    "If you're wondering whether {topic} is worth it for your business, you're in the right place. Concrete numbers, real examples and a clear plan.",
    "Many companies hesitate with {topic} – and miss a real competitive advantage. This article gives you the info for an informed decision.",
    "AI avatars are no longer hype, but a proven tool. {topic} delivers directly measurable results. Let's dive in.",
]

SECTION1_DE = [
    "Die Grundlagen: Wie {topic} funktioniert und welche Technologien dahinterstecken – von der Gesichtserkennung bis zur Sprachsynthese.",
    "Technologie im Ueberblick: Was macht {topic} moeglich? Die wichtigsten Komponenten und wie sie zusammenwirken.",
    "Funktionsweise verstehen: {topic} basiert auf fortschrittlichen KI-Modellen. Die Kernkonzepte erklaert – ohne Fachjargon.",
]

SECTION2_DE = [
    "Praxisbeispiele die ueberzeugen: Drei Unternehmen, die {topic} erfolgreich einsetzen – mit konkreten Zahlen.",
    "Anwendung in der Realitaet: {topic} im Arbeitsalltag. Fallstudien aus verschiedenen Branchen zeigen das Potenzial.",
    "Von der Theorie zur Praxis: {topic} Schritt fuer Schritt umgesetzt. Mit Checkliste fuer deine eigene Implementierung.",
]

SECTION3_DE = [
    "Tipps fuer optimale Ergebnisse: Die 5 wichtigsten Dos und Don'ts bei {topic}. Plus: Fehler die Anfaenger machen.",
    "Best Practices und Fallstricke: Was funktioniert bei {topic} wirklich? Bewaehrte Strategien und haeufige Fehler.",
    "Professionell umsetzen: Dein Fahrplan fuer {topic}. Von der Planung bis zur Optimierung.",
]

SECTION1_EN = [
    "The basics: How {topic} works and the technologies behind it – from facial recognition to speech synthesis.",
    "Technology overview: What makes {topic} possible? The key components and how they work together.",
    "Understanding how it works: {topic} is based on advanced AI models. Core concepts explained – no jargon.",
]

SECTION2_EN = [
    "Practical examples that convince: Three companies successfully using {topic} – with concrete numbers.",
    "Application in reality: {topic} in everyday work. Case studies from different industries show the potential.",
    "From theory to practice: {topic} implemented step by step. With a checklist for your own implementation.",
]

SECTION3_EN = [
    "Tips for optimal results: The 5 most important dos and don'ts with {topic}. Plus: mistakes beginners make.",
    "Best practices and pitfalls: What really works with {topic}? Proven strategies and common mistakes.",
    "Professional implementation: Your roadmap for {topic}. From planning to optimization.",
]

CTA_DE = [
    "Erstelle jetzt deinen KI-Avatar und ueberzeuge dich selbst!",
    "Starte heute mit KI-Avataren – dein erster ist kostenlos!",
    "Probiere den KI-Avatar-Generator aus und sieh den Unterschied!",
    "Jetzt KI-Avatar erstellen: Schneller, einfacher, professioneller!",
    "Dein KI-Avatar wartet: Jetzt Generator starten!",
]

CTA_EN = [
    "Create your AI avatar now and see for yourself!",
    "Start with AI avatars today – your first one is free!",
    "Try the AI avatar generator and see the difference!",
    "Create AI avatar now: Faster, easier, more professional!",
    "Your AI avatar is waiting: Start the generator now!",
]


def _get_unique_content(idx: int, is_lp: bool) -> Dict[str, str]:
    """Generate unique content for a given index and type."""
    titles_de = LP_TITLES_DE if is_lp else BLOG_TITLES_DE
    titles_en = LP_TITLES_EN if is_lp else BLOG_TITLES_EN
    max_idx = len(titles_de) - 1
    i = min(idx, max_idx)

    t_de = titles_de[i]
    t_en = titles_en[i]

    return {
        "titel_de": t_de,
        "titel_en": t_en,
        "meta_de": f"Entdecke, wie {t_de} dein Business transformiert. Praxisnaher Guide mit Tipps und Tools.",
        "meta_en": f"Discover how {t_en} transforms your business. Practical guide with tips and tools.",
        "intro_de": INTRO_DE[i % len(INTRO_DE)].format(topic=t_de),
        "intro_en": INTRO_EN[i % len(INTRO_EN)].format(topic=t_en),
        "s1_de": SECTION1_DE[i % len(SECTION1_DE)].format(topic=t_de),
        "s1_en": SECTION1_EN[i % len(SECTION1_EN)].format(topic=t_en),
        "s2_de": SECTION2_DE[i % len(SECTION2_DE)].format(topic=t_de),
        "s2_en": SECTION2_EN[i % len(SECTION2_EN)].format(topic=t_en),
        "s3_de": SECTION3_DE[i % len(SECTION3_DE)].format(topic=t_de),
        "s3_en": SECTION3_EN[i % len(SECTION3_EN)].format(topic=t_en),
        "cta_de": CTA_DE[i % len(CTA_DE)],
        "cta_en": CTA_EN[i % len(CTA_EN)],
    }


def enrich_csv(input_csv: str, output_csv: str) -> List[Dict[str, Any]]:
    """Read CSV and enrich each row with unique content."""
    enriched_rows = []
    rows = []

    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        for row in reader:
            rows.append(row)

    blog_idx = 0
    lp_idx = 0

    new_fields = [
        'Titel_DE', 'Meta_DE', 'Einleitung_DE', 'Abschnitt1_DE', 'Abschnitt2_DE', 'Abschnitt3_DE', 'CTA_DE',
        'Titel_EN', 'Meta_EN', 'Einleitung_EN', 'Abschnitt1_EN', 'Abschnitt2_EN', 'Abschnitt3_EN', 'CTA_EN',
    ]
    all_fields = fieldnames + new_fields

    for row in rows:
        asset = row.get('Asset', '')
        is_lp = asset.startswith('Avatar_LP')
        idx = lp_idx if is_lp else blog_idx

        if is_lp:
            lp_idx += 1
        else:
            blog_idx += 1

        content = _get_unique_content(idx, is_lp)
        enriched = dict(row)
        enriched['Titel_DE'] = content['titel_de']
        enriched['Meta_DE'] = content['meta_de']
        enriched['Einleitung_DE'] = content['intro_de']
        enriched['Abschnitt1_DE'] = content['s1_de']
        enriched['Abschnitt2_DE'] = content['s2_de']
        enriched['Abschnitt3_DE'] = content['s3_de']
        enriched['CTA_DE'] = content['cta_de']
        enriched['Titel_EN'] = content['titel_en']
        enriched['Meta_EN'] = content['meta_en']
        enriched['Einleitung_EN'] = content['intro_en']
        enriched['Abschnitt1_EN'] = content['s1_en']
        enriched['Abschnitt2_EN'] = content['s2_en']
        enriched['Abschnitt3_EN'] = content['s3_en']
        enriched['CTA_EN'] = content['cta_en']
        enriched_rows.append(enriched)

    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"[B] Angereicherte CSV gespeichert: {output_csv}")
    print(f"    {len(enriched_rows)} Zeilen mit einzigartigem Content angereichert")
    print(f"    Blog-Artikel: {blog_idx}, Landing Pages: {lp_idx}")
    return enriched_rows


def create_nurturing_emails(enriched_rows: List[Dict[str, Any]], output_dir: str):
    """Create nurturing email jobs from enriched CSV data."""
    os.makedirs(output_dir, exist_ok=True)
    jobs = []
    start_date = datetime(2026, 5, 12)

    blog_rows = [r for r in enriched_rows if not r['Asset'].startswith('Avatar_LP')]
    lp_rows = [r for r in enriched_rows if r['Asset'].startswith('Avatar_LP')]

    # 12 weekly blog nurturing emails
    for i, row in enumerate(blog_rows[:12]):
        send_date = start_date + timedelta(weeks=i)
        job = {
            "id": f"blog_nurture_w{i+1}",
            "type": "blog_nurturing",
            "scheduled_at": send_date.strftime("%Y-%m-%d"),
            "subject_de": f"KI-Insight der Woche: {row['Titel_DE']}",
            "subject_en": f"AI Insight of the Week: {row['Titel_EN']}",
            "body_de": f"{row['Einleitung_DE']}\n\n{row['Abschnitt1_DE']}\n\n{row['Abschnitt2_DE']}\n\n{row['Abschnitt3_DE']}\n\n{row['CTA_DE']}",
            "body_en": f"{row['Einleitung_EN']}\n\n{row['Abschnitt1_EN']}\n\n{row['Abschnitt2_EN']}\n\n{row['Abschnitt3_EN']}\n\n{row['CTA_EN']}",
            "content_type": "blog_nurturing",
            "asset": row['Asset'],
            "status": "scheduled",
        }
        jobs.append(job)

    # 8 bi-weekly landing page promo emails
    for i, row in enumerate(lp_rows[:8]):
        send_date = start_date + timedelta(weeks=12 + i * 2)
        job = {
            "id": f"lp_promo_w{12 + i*2 + 1}",
            "type": "landing_page_promo",
            "scheduled_at": send_date.strftime("%Y-%m-%d"),
            "subject_de": f"Neu: {row['Titel_DE']}",
            "subject_en": f"New: {row['Titel_EN']}",
            "body_de": f"{row['Einleitung_DE']}\n\n{row['Abschnitt1_DE']}\n\n{row['CTA_DE']}",
            "body_en": f"{row['Einleitung_EN']}\n\n{row['Abschnitt1_EN']}\n\n{row['CTA_EN']}",
            "content_type": "landing_page_promo",
            "asset": row['Asset'],
            "status": "scheduled",
        }
        jobs.append(job)

    # Save jobs
    jobs_file = os.path.join(output_dir, "blog_nurturing_jobs.json")
    with open(jobs_file, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)

    # Create email-agent sequence config
    blog_emails = [j for j in jobs if j['type'] == 'blog_nurturing']
    lp_emails = [j for j in jobs if j['type'] == 'landing_page_promo']

    config = {
        "blog_nurturing_sequence": {
            "name": "KI-Avatar Blog Nurturing",
            "sequence_type": "blog_nurturing",
            "trigger": "newsletter_subscription",
            "total_emails": len(blog_emails),
            "emails": blog_emails,
        },
        "landing_page_promo_sequence": {
            "name": "KI-Avatar Landing Page Promo",
            "sequence_type": "landing_page_promo",
            "trigger": "lead_magnet_download",
            "total_emails": len(lp_emails),
            "emails": lp_emails,
        },
    }

    config_file = os.path.join(output_dir, "blog_sequences_config.json")
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"[C] Nurturing-E-Mail-Jobs erstellt:")
    print(f"    Blog Nurturing: {len(blog_emails)} E-Mails (woechentlich ab 12.05.2026)")
    print(f"    Landing Page Promo: {len(lp_emails)} E-Mails (2-woechentlich ab 28.07.2026)")
    print(f"    Jobs: {jobs_file}")
    print(f"    Config: {config_file}")
    return jobs, config


async def import_to_notion(enriched_rows: List[Dict[str, Any]], api_key: str, database_id: str):
    """Import enriched CSV data into Notion Content-Stuecke DB."""
    try:
        from notion_client import Client
    except ImportError:
        print("[A] FEHLER: notion-client nicht installiert! pip install notion-client")
        return False

    client = Client(auth=api_key)
    imported = 0
    errors = 0

    for row in enriched_rows:
        asset = row.get('Asset', '')
        is_lp = asset.startswith('Avatar_LP')
        content_type = "Landing Page" if is_lp else "Blog-Artikel"

        try:
            client.pages.create(
                parent={"database_id": database_id.replace("-", "")},
                properties={
                    "Titel": {"title": [{"text": {"content": row['Titel_DE']}}]},
                    "Typ": {"select": {"name": content_type}},
                    "Kanal": {"select": {"name": "Autonova"}},
                    "Status": {"status": {"name": "Idee"}},
                    "Lead-Magnet": {"checkbox": is_lp},
                },
            )
            imported += 1
            if imported % 10 == 0:
                print(f"    {imported}/{len(enriched_rows)} importiert...")
        except Exception as e:
            errors += 1
            if errors <= 3:
                print(f"    Fehler bei {asset}: {e}")

    print(f"[A] Notion Import abgeschlossen: {imported} importiert, {errors} Fehler")
    return imported > 0


def main():
    parser = argparse.ArgumentParser(description="Blog Content Manager")
    parser.add_argument("--csv", required=True, help="Pfad zur AIxTools_Blogs_DE_EN.csv")
    parser.add_argument("--notion", action="store_true", default=False, help="In Notion importieren (A)")
    parser.add_argument("--output-dir", default=None, help="Ausgabeverzeichnis")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"FEHLER: CSV nicht gefunden: {csv_path}")
        sys.exit(1)

    output_dir = args.output_dir or str(csv_path.parent / "blog_content_output")
    os.makedirs(output_dir, exist_ok=True)

    enriched_csv = os.path.join(output_dir, "AIxTools_Blogs_ENRICHED.csv")
    email_dir = os.path.join(output_dir, "email_agent_data")

    print("=" * 60)
    print("BLOG CONTENT MANAGER")
    print("=" * 60)

    # B: CSV anreichern
    print("\n[SCHRITT 1] CSV mit einzigartigem Content anreichern...")
    enriched_rows = enrich_csv(str(csv_path), enriched_csv)

    # C: Email-Agent Integration
    print("\n[SCHRITT 2] Nurturing-E-Mail-Jobs erstellen...")
    jobs, config = create_nurturing_emails(enriched_rows, email_dir)

    # A: Notion Import (optional)
    if args.notion:
        api_key = os.getenv("NOTION_API_KEY")
        db_id = os.getenv("NOTION_CONTENT_DB_ID")
        if not api_key or not db_id:
            print("\n[A] Notion Import uebersprungen:")
            print("    Setze NOTION_API_KEY und NOTION_CONTENT_DB_ID")
            print("    $env:NOTION_API_KEY='...'; $env:NOTION_CONTENT_DB_ID='...'")
        else:
            print("\n[SCHRITT 3] In Notion Content-Stuecke DB importieren...")
            asyncio.run(import_to_notion(enriched_rows, api_key, db_id))

    print("\n" + "=" * 60)
    print("ABGESCHLOSSEN!")
    print("=" * 60)
    print(f"Output: {output_dir}")
    print(f"Angereicherte CSV: {enriched_csv}")
    print(f"Email-Agent Daten: {email_dir}")


if __name__ == "__main__":
    main()
