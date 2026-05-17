#!/usr/bin/env python3
"""
Autonova Notion-Setup: Erstellt alle benötigten Datenbanken und Verknüpfungen
für das E-Mail-Scheduling-System in Notion.

Voraussetzungen:
- Notion API Key (Integration erstellen: https://www.notion.so/my-integrations)
- Notion-Page-ID (Seite, unter der die Datenbanken erstellt werden sollen)

Verwendung:
1. pip install notion-client
2. Setze Umgebungsvariablen:
   - NOTION_API_KEY=your_notion_api_key
   - NOTION_PAGE_ID=your_page_id
3. python notion_setup.py
"""

import os
import sys
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

try:
    from notion_client import Client
except ImportError:
    print("FEHLER: notion-client nicht installiert!")
    print("Bitte ausfuehren: pip install notion-client")
    sys.exit(1)


class AutonovaNotionSetup:
    """Erstellt das komplette Autonova Notion-Workspace"""

    def __init__(self, api_key: str, page_id: str):
        self.client = Client(auth=api_key)
        self.page_id = page_id
        self.database_ids: Dict[str, str] = {}

    def setup_all(self):
        """Führt das komplette Setup aus"""
        print("=" * 60)
        print("AUTONOVA NOTION-SETUP")
        print("=" * 60)

        # Schritt 1: Datenbanken erstellen
        print("\n1. Erstelle Datenbanken...")
        self._create_databases()

        # Schritt 2: Verknüpfungen herstellen
        print("\n2. Erstelle Verknuepfungen...")
        self._create_relations()

        # Schritt 3: E-Mail-Sequenzen befüllen
        print("\n3. Befuelle E-Mail-Sequenzen...")
        self._populate_email_sequences()

        # Schritt 4: 12-Wochen-Newsletter importieren
        print("\n4. Importiere 12-Wochen-Newsletter...")
        self._populate_newsletters()

        # Schritt 5: SaaS-Produkte befüllen
        print("\n5. Befuelle SaaS-Produkte...")
        self._populate_saas_products()

        # Schritt 6: Blog-Content aus angereicherter CSV importieren
        print("\n6. Importiere Blog-Content aus CSV...")
        self._populate_blog_content()

        # Schritt 7: E-Mail-Scheduling-Datenbank erstellen
        print("\n7. Erstelle E-Mail-Scheduling-Datenbank...")
        self._create_scheduling_database()

        # Schritt 8: Dashboard-Ansichten erstellen
        print("\n8. Erstelle Dashboard-Hinweise...")
        self._create_dashboard_notes()

        print("\n" + "=" * 60)
        print("SETUP ABGESCHLOSSEN!")
        print(f"Datenbanken erstellt: {len(self.database_ids)}")
        print("=" * 60)

        return self.database_ids

    def _create_databases(self):
        """Erstellt alle 6 Hauptdatenbanken"""

        # 1. E-Mail-Sequenzen
        print("  -> E-Mail-Sequenzen DB...")
        self.database_ids["email_sequences"] = self._create_database(
            title="📧 E-Mail-Sequenzen",
            properties={
                "Name": {"title": {}},
                "Sequenz-Typ": {
                    "select": {
                        "options": [
                            {"name": "Willkommen", "color": "green"},
                            {"name": "Lead-Nurturing", "color": "blue"},
                            {"name": "Onboarding", "color": "purple"},
                            {"name": "Reaktivierung", "color": "orange"},
                            {"name": "SaaS-Trial", "color": "pink"},
                            {"name": "Upsell", "color": "yellow"},
                            {"name": "Newsletter", "color": "gray"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Entwurf", "color": "gray"},
                            {"name": "Aktiv", "color": "green"},
                            {"name": "Pausiert", "color": "yellow"},
                            {"name": "Abgeschlossen", "color": "blue"},
                        ]
                    }
                },
                "Trigger": {
                    "select": {
                        "options": [
                            {"name": "Anmeldung", "color": "green"},
                            {"name": "Kauf", "color": "blue"},
                            {"name": "Inaktivität", "color": "orange"},
                            {"name": "Trial-Start", "color": "purple"},
                            {"name": "Trial-Ende", "color": "red"},
                            {"name": "Manuell", "color": "gray"},
                        ]
                    }
                },
                "Anzahl E-Mails": {"number": {"format": "number"}},
                "Zielgruppe": {
                    "select": {
                        "options": [
                            {"name": "Alle", "color": "gray"},
                            {"name": "Neue Leads", "color": "green"},
                            {"name": "Kunden", "color": "blue"},
                            {"name": "Inaktive", "color": "orange"},
                            {"name": "Trial-User", "color": "purple"},
                        ]
                    }
                },
                "Beschreibung": {"rich_text": {}},
            }
        )

        # 2. E-Mail-Inhalte
        print("  -> E-Mail-Inhalte DB...")
        self.database_ids["email_contents"] = self._create_database(
            title="✉️ E-Mail-Inhalte",
            properties={
                "Betreff": {"title": {}},
                "Delay": {
                    "select": {
                        "options": [
                            {"name": "Sofort", "color": "green"},
                            {"name": "1 Tag", "color": "light_green"},
                            {"name": "2 Tage", "color": "blue"},
                            {"name": "3 Tage", "color": "light_blue"},
                            {"name": "7 Tage", "color": "purple"},
                            {"name": "14 Tage", "color": "orange"},
                            {"name": "30 Tage", "color": "red"},
                            {"name": "90 Tage", "color": "gray"},
                        ]
                    }
                },
                "E-Mail-Typ": {
                    "select": {
                        "options": [
                            {"name": "Willkommen", "color": "green"},
                            {"name": "Content", "color": "blue"},
                            {"name": "Case Study", "color": "purple"},
                            {"name": "Einwände", "color": "orange"},
                            {"name": "CTA", "color": "red"},
                            {"name": "Projekt-Update", "color": "pink"},
                            {"name": "Projekt-Abschluss", "color": "yellow"},
                            {"name": "Reaktivierung", "color": "gray"},
                            {"name": "Trial-Support", "color": "light_blue"},
                            {"name": "Trial-Rabatt", "color": "light_green"},
                            {"name": "Upsell", "color": "light_purple"},
                            {"name": "Newsletter", "color": "brown"},
                        ]
                    }
                },
                "Body-Text": {"rich_text": {}},
                "CTA-Link": {"url": {}},
                "Priorität": {
                    "select": {
                        "options": [
                            {"name": "Hoch", "color": "red"},
                            {"name": "Mittel", "color": "yellow"},
                            {"name": "Niedrig", "color": "gray"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Entwurf", "color": "gray"},
                            {"name": "Freigegeben", "color": "yellow"},
                            {"name": "Geplant", "color": "blue"},
                            {"name": "Gesendet", "color": "green"},
                        ]
                    }
                },
                "A/B-Variante": {"checkbox": {}},
                "Geplantes Versanddatum": {"date": {}},
            }
        )

        # 3. Newsletter-Woche
        print("  -> Newsletter-Woche DB...")
        self.database_ids["newsletter_weeks"] = self._create_database(
            title="📬 Newsletter-Wochen",
            properties={
                "Woche": {"title": {}},
                "Betreff": {"rich_text": {}},
                "Sende-Datum": {"date": {}},
                "Haupt-Thema": {
                    "select": {
                        "options": [
                            {"name": "Ehrlichkeit", "color": "green"},
                            {"name": "Automatisierung", "color": "blue"},
                            {"name": "ChatGPT", "color": "purple"},
                            {"name": "Persönliche Geschichte", "color": "pink"},
                            {"name": "Preisgestaltung", "color": "yellow"},
                            {"name": "Psychologie", "color": "orange"},
                            {"name": "KI-Mythen", "color": "red"},
                            {"name": "Tools", "color": "gray"},
                            {"name": "Skalierung", "color": "light_blue"},
                            {"name": "Community", "color": "light_green"},
                            {"name": "Zukunft", "color": "light_purple"},
                            {"name": "Abschluss", "color": "brown"},
                        ]
                    }
                },
                "CTA": {
                    "select": {
                        "options": [
                            {"name": "Download", "color": "blue"},
                            {"name": "Analyse buchen", "color": "green"},
                            {"name": "Video ansehen", "color": "purple"},
                            {"name": "Beratung", "color": "orange"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Geplant", "color": "yellow"},
                            {"name": "In Arbeit", "color": "blue"},
                            {"name": "Gesendet", "color": "green"},
                        ]
                    }
                },
                "Body-Zusammenfassung": {"rich_text": {}},
            }
        )

        # 4. Content-Stücke
        print("  -> Content-Stuecke DB...")
        self.database_ids["content_pieces"] = self._create_database(
            title="🎬 Content-Stücke",
            properties={
                "Titel": {"title": {}},
                "Typ": {
                    "select": {
                        "options": [
                            {"name": "YouTube-Video", "color": "red"},
                            {"name": "LinkedIn-Post", "color": "blue"},
                            {"name": "Blog-Artikel", "color": "green"},
                            {"name": "Whitepaper", "color": "purple"},
                            {"name": "Podcast", "color": "orange"},
                        ]
                    }
                },
                "Kanal": {
                    "select": {
                        "options": [
                            {"name": "Autonova", "color": "blue"},
                            {"name": "Politara", "color": "red"},
                            {"name": "Beide", "color": "purple"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Idee", "color": "gray"},
                            {"name": "In Arbeit", "color": "yellow"},
                            {"name": "Freigegeben", "color": "blue"},
                            {"name": "Veröffentlicht", "color": "green"},
                        ]
                    }
                },
                "Veröffentlichungs-Datum": {"date": {}},
                "Lead-Magnet": {"checkbox": {}},
                "Themen": {"multi_select": {"options": []}},
                "Beschreibung": {"rich_text": {}},
            }
        )

        # 5. Kontakte / Leads
        print("  -> Kontakte/Leads DB...")
        self.database_ids["contacts"] = self._create_database(
            title="👥 Kontakte & Leads",
            properties={
                "Name": {"title": {}},
                "E-Mail": {"email": {}},
                "Unternehmen": {"rich_text": {}},
                "Branche": {
                    "select": {
                        "options": [
                            {"name": "Gesundheit", "color": "green"},
                            {"name": "Handwerk", "color": "orange"},
                            {"name": "IT/Tech", "color": "blue"},
                            {"name": "Beratung", "color": "purple"},
                            {"name": "E-Commerce", "color": "pink"},
                            {"name": "Finanzen", "color": "yellow"},
                            {"name": "Sonstige", "color": "gray"},
                        ]
                    }
                },
                "Lead-Quelle": {
                    "select": {
                        "options": [
                            {"name": "Website", "color": "blue"},
                            {"name": "LinkedIn", "color": "purple"},
                            {"name": "YouTube", "color": "red"},
                            {"name": "Empfehlung", "color": "green"},
                            {"name": "Event", "color": "orange"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Neu", "color": "gray"},
                            {"name": "Kontaktiert", "color": "yellow"},
                            {"name": "Qualifiziert", "color": "blue"},
                            {"name": "Kunde", "color": "green"},
                            {"name": "Inaktiv", "color": "red"},
                        ]
                    }
                },
                "Interesse": {
                    "multi_select": {
                        "options": [
                            {"name": "SEO", "color": "blue"},
                            {"name": "Automatisierung", "color": "green"},
                            {"name": "SaaS", "color": "purple"},
                            {"name": "Content", "color": "orange"},
                            {"name": "Buchhaltung", "color": "yellow"},
                            {"name": "KI-Beratung", "color": "pink"},
                        ]
                    }
                },
                "Letzter Versand": {"date": {}},
                "Notizen": {"rich_text": {}},
            }
        )

        # 6. SaaS-Produkte
        print("  -> SaaS-Produkte DB...")
        self.database_ids["saas_products"] = self._create_database(
            title="🚀 SaaS-Produkte",
            properties={
                "Produktname": {"title": {}},
                "Preis": {"rich_text": {}},
                "Monatliches MRR-Ziel": {"number": {"format": "euro"}},
                "Trial-Dauer": {
                    "select": {
                        "options": [
                            {"name": "7 Tage", "color": "green"},
                            {"name": "14 Tage", "color": "blue"},
                            {"name": "30 Tage", "color": "purple"},
                        ]
                    }
                },
                "Landing-Page-Status": {
                    "status": {
                        "options": [
                            {"name": "Fehlt", "color": "red"},
                            {"name": "Entwurf", "color": "yellow"},
                            {"name": "Live", "color": "green"},
                        ]
                    }
                },
                "Priorität": {
                    "select": {
                        "options": [
                            {"name": "P1", "color": "red"},
                            {"name": "P2", "color": "yellow"},
                            {"name": "P3", "color": "gray"},
                        ]
                    }
                },
                "Launch-Datum": {"date": {}},
                "Beschreibung": {"rich_text": {}},
            }
        )

        print(f"  -> {len(self.database_ids)} Datenbanken erstellt!")

    def _create_database(self, title: str, properties: Dict) -> str:
        """Erstellt eine einzelne Datenbank"""
        try:
            response = self.client.databases.create(
                parent={"page_id": self.page_id},
                title=[{"type": "text", "text": {"content": title}}],
                properties=properties,
            )
            db_id = response["id"]
            print(f"     ✓ {title} -> {db_id[:8]}...")
            return db_id
        except Exception as e:
            print(f"     ✗ FEHLER bei {title}: {e}")
            return ""

    def _create_relations(self):
        """Fügt Verknüpfungs-Properties zu den Datenbanken hinzu"""
        if not all(self.database_ids.values()):
            print("  WARNUNG: Nicht alle Datenbanken erstellt. Überspringe Verknüpfungen.")
            return

        relations = [
            {
                "db": "email_sequences",
                "name": "E-Mail-Inhalte",
                "relation_config": {
                    "database_id": self.database_ids["email_contents"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Sequenz"},
                },
            },
            {
                "db": "email_contents",
                "name": "Verknüpfter Content",
                "relation_config": {
                    "database_id": self.database_ids["content_pieces"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Verknüpfte E-Mails"},
                },
            },
            {
                "db": "newsletter_weeks",
                "name": "E-Mail-Inhalte",
                "relation_config": {
                    "database_id": self.database_ids["email_contents"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Newsletter-Woche"},
                },
            },
            {
                "db": "newsletter_weeks",
                "name": "Content",
                "relation_config": {
                    "database_id": self.database_ids["content_pieces"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Newsletter"},
                },
            },
            {
                "db": "contacts",
                "name": "Aktuelle Sequenz",
                "relation_config": {
                    "database_id": self.database_ids["email_sequences"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Kontakte"},
                },
            },
            {
                "db": "saas_products",
                "name": "Trial-Sequenz",
                "relation_config": {
                    "database_id": self.database_ids["email_sequences"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "SaaS-Produkt"},
                },
            },
            {
                "db": "contacts",
                "name": "SaaS-Interesse",
                "relation_config": {
                    "database_id": self.database_ids["saas_products"],
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Interessierte Kontakte"},
                },
            },
        ]

        for rel in relations:
            try:
                self.client.databases.update(
                    database_id=self.database_ids[rel["db"]],
                    properties={
                        rel["name"]: {"relation": rel["relation_config"]},
                    },
                )
                print(f"  ✓ Verknuepfung: {rel['db']}.{rel['name']}")
            except Exception as e:
                print(f"  ✗ FEHLER bei Verknuepfung {rel['name']}: {e}")

    def _populate_email_sequences(self):
        """Befüllt die E-Mail-Sequenzen-Datenbank"""

        sequences = [
            {
                "name": "Willkommens-Sequenz",
                "type": "Willkommen",
                "trigger": "Anmeldung",
                "zielgruppe": "Neue Leads",
                "beschreibung": "4 E-Mails nach Potenzial-Analyse-Anmeldung",
                "emails": [
                    {
                        "betreff": "Ihre kostenlose KI-Potenzial-Analyse ist bestätigt ✅",
                        "delay": "Sofort",
                        "typ": "Willkommen",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "Ihr Termin steht fest + wichtige Vorbereitung",
                        "delay": "1 Tag",
                        "typ": "Content",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "Morgen um [Uhrzeit]: Ihre KI-Potenzial-Analyse + Bonus",
                        "delay": "1 Tag",
                        "typ": "CTA",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "Ihr nächster Schritt zur KI-Transformation",
                        "delay": "3 Tage",
                        "typ": "CTA",
                        "priorität": "Mittel",
                    },
                ],
            },
            {
                "name": "Lead-Nurturing-Sequenz",
                "type": "Lead-Nurturing",
                "trigger": "Anmeldung",
                "zielgruppe": "Neue Leads",
                "beschreibung": "4 E-Mails für Leads ohne Terminbuchung",
                "emails": [
                    {
                        "betreff": "[Kostenlos] 10 KI-Tools, die jedes Unternehmen 2025 nutzen sollte",
                        "delay": "7 Tage",
                        "typ": "Content",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "Wie Dr. Müller 40% mehr Umsatz mit KI macht (echte Zahlen)",
                        "delay": "14 Tage",
                        "typ": "Case Study",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "5 KI-Mythen, die Ihr Unternehmen Geld kosten",
                        "delay": "21 Tage",
                        "typ": "Einwände",
                        "priorität": "Mittel",
                    },
                    {
                        "betreff": "Ihre KI-Chance läuft ab (letzte Erinnerung)",
                        "delay": "28 Tage",
                        "typ": "CTA",
                        "priorität": "Hoch",
                    },
                ],
            },
            {
                "name": "Kunden-Onboarding-Sequenz",
                "type": "Onboarding",
                "trigger": "Kauf",
                "zielgruppe": "Kunden",
                "beschreibung": "3 E-Mails nach Vertragsabschluss",
                "emails": [
                    {
                        "betreff": "Willkommen bei Autonova! Ihr Projekt startet jetzt 🚀",
                        "delay": "Sofort",
                        "typ": "Willkommen",
                        "priorität": "Hoch",
                    },
                    {
                        "betreff": "Projektupdate KW [X]: Alles läuft nach Plan ✅",
                        "delay": "7 Tage",
                        "typ": "Projekt-Update",
                        "priorität": "Mittel",
                    },
                    {
                        "betreff": "🎉 Projekt abgeschlossen - Ihre Ergebnisse sind da!",
                        "delay": "30 Tage",
                        "typ": "Projekt-Abschluss",
                        "priorität": "Hoch",
                    },
                ],
            },
            {
                "name": "Reaktivierungs-Sequenz",
                "type": "Reaktivierung",
                "trigger": "Inaktivität",
                "zielgruppe": "Inaktive",
                "beschreibung": "2 E-Mails für inaktive Leads nach 3 Monaten",
                "emails": [
                    {
                        "betreff": "Vermisse ich Sie? (Kurze Frage)",
                        "delay": "90 Tage",
                        "typ": "Reaktivierung",
                        "priorität": "Mittel",
                    },
                    {
                        "betreff": "Letzte E-Mail von mir (Versprochen!)",
                        "delay": "14 Tage",
                        "typ": "Reaktivierung",
                        "priorität": "Niedrig",
                    },
                ],
            },
        ]

        db_id = self.database_ids.get("email_sequences")
        if not db_id:
            print("  WARNUNG: E-Mail-Sequenzen DB nicht gefunden.")
            return

        for seq in sequences:
            try:
                self.client.pages.create(
                    parent={"database_id": db_id},
                    properties={
                        "Name": {"title": [{"text": {"content": seq["name"]}}]},
                        "Sequenz-Typ": {"select": {"name": seq["type"]}},
                        "Trigger": {"select": {"name": seq["trigger"]}},
                        "Zielgruppe": {"select": {"name": seq["zielgruppe"]}},
                        "Anzahl E-Mails": {"number": len(seq["emails"])},
                        "Status": {"status": {"name": "Aktiv"}},
                        "Beschreibung": {"rich_text": [{"text": {"content": seq["beschreibung"]}}]},
                    },
                )
                print(f"  ✓ Sequenz: {seq['name']} ({len(seq['emails'])} E-Mails)")

                # Erstelle einzelne E-Mail-Inhalte
                for i, email in enumerate(seq["emails"]):
                    self._create_email_content(email, seq["name"])

            except Exception as e:
                print(f"  ✗ FEHLER bei Sequenz {seq['name']}: {e}")

    def _create_email_content(self, email: Dict, sequence_name: str):
        """Erstellt einen einzelnen E-Mail-Inhalt-Eintrag"""
        db_id = self.database_ids.get("email_contents")
        if not db_id:
            return

        try:
            self.client.pages.create(
                parent={"database_id": db_id},
                properties={
                    "Betreff": {"title": [{"text": {"content": email["betreff"]}}]},
                    "Delay": {"select": {"name": email["delay"]}},
                    "E-Mail-Typ": {"select": {"name": email["typ"]}},
                    "Priorität": {"select": {"name": email["priorität"]}},
                    "Status": {"status": {"name": "Freigegeben"}},
                },
            )
        except Exception as e:
            print(f"    ✗ FEHLER bei E-Mail: {email['betreff'][:30]}...: {e}")

    def _populate_newsletters(self):
        """Befüllt die Newsletter-Wochen-Datenbank"""

        newsletters = [
            {"woche": "Woche 1 - Der ehrliche Start", "betreff": "Warum ich keine Referenzen zeige", "thema": "Ehrlichkeit", "cta": "Download"},
            {"woche": "Woche 2 - Realitätscheck", "betreff": "ChatGPT kann NICHT alles (und das ist gut so)", "thema": "ChatGPT", "cta": "Download"},
            {"woche": "Woche 3 - DIY Automatisierung", "betreff": "3 Automatisierungen, die Sie heute einrichten können", "thema": "Automatisierung", "cta": "Video ansehen"},
            {"woche": "Woche 4 - ChatGPT richtig nutzen", "betreff": "5 ChatGPT-Prompts, die täglich Zeit sparen", "thema": "ChatGPT", "cta": "Download"},
            {"woche": "Woche 5 - Meine Geschichte", "betreff": "Warum ich mit 58 nochmal neu anfange", "thema": "Persönliche Geschichte", "cta": "Beratung"},
            {"woche": "Woche 6 - Der Automatisierungs-Check", "betreff": "1 Stunde, die Ihnen 1000€ sparen kann", "thema": "Automatisierung", "cta": "Analyse buchen"},
            {"woche": "Woche 7 - Universal-Automatisierungen", "betreff": "Diese 3 Automatisierungen funktionieren in jeder Branche", "thema": "Automatisierung", "cta": "Download"},
            {"woche": "Woche 8 - KI-Konkurrenzanalyse", "betreff": "Wie Ihre Konkurrenz arbeitet (und wie Sie besser werden)", "thema": "Tools", "cta": "Download"},
            {"woche": "Woche 9 - Preise erhöhen", "betreff": "Wie Sie 30% mehr verlangen (und Kunden es gerne zahlen)", "thema": "Preisgestaltung", "cta": "Download"},
            {"woche": "Woche 10 - Kaufmotive", "betreff": "Es ist nicht der Preis (die wahren Kaufmotive)", "thema": "Psychologie", "cta": "Beratung"},
            {"woche": "Woche 11 - KI-Scharlatane", "betreff": "90% der KI-Berater sind Scharlatane", "thema": "KI-Mythen", "cta": "Analyse buchen"},
            {"woche": "Woche 12 - Abschluss & Ausblick", "betreff": "Ihr 12-Wochen-Check: Was haben Sie umgesetzt?", "thema": "Zukunft", "cta": "Beratung"},
        ]

        db_id = self.database_ids.get("newsletter_weeks")
        if not db_id:
            return

        start_date = datetime(2026, 5, 12)  # Nächster Dienstag

        for i, nl in enumerate(newsletters):
            send_date = start_date + timedelta(weeks=i)
            try:
                self.client.pages.create(
                    parent={"database_id": db_id},
                    properties={
                        "Woche": {"title": [{"text": {"content": nl["woche"]}}]},
                        "Betreff": {"rich_text": [{"text": {"content": nl["betreff"]}}]},
                        "Sende-Datum": {"date": {"start": send_date.strftime("%Y-%m-%d")}},
                        "Haupt-Thema": {"select": {"name": nl["thema"]}},
                        "CTA": {"select": {"name": nl["cta"]}},
                        "Status": {"status": {"name": "Geplant"}},
                    },
                )
                print(f"  ✓ {nl['woche']} -> {send_date.strftime('%d.%m.%Y')}")
            except Exception as e:
                print(f"  ✗ FEHLER bei {nl['woche']}: {e}")

    def _populate_saas_products(self):
        """Befüllt die SaaS-Produkte-Datenbank"""

        products = [
            {"name": "Prompt Optimizer", "preis": "299€/Monat", "mrr": 50000, "trial": "14 Tage", "prio": "P1", "lp": "Live"},
            {"name": "SEO Dominator", "preis": "499-999€/Monat", "mrr": 100000, "trial": "14 Tage", "prio": "P1", "lp": "Live"},
            {"name": "Content Calendar Automation", "preis": "899€/Monat", "mrr": 180000, "trial": "14 Tage", "prio": "P1", "lp": "Entwurf"},
            {"name": "Workflow Automation Engine", "preis": "1.199€/Monat", "mrr": 150000, "trial": "14 Tage", "prio": "P1", "lp": "Fehlt"},
            {"name": "Multi-Platform Connector", "preis": "1.499€/Monat", "mrr": 200000, "trial": "14 Tage", "prio": "P1", "lp": "Fehlt"},
            {"name": "Bookwriter", "preis": "5.000-25.000€ einmalig", "mrr": 30000, "trial": "7 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "Web Scraping Service", "preis": "499-1.499€/Monat", "mrr": 40000, "trial": "7 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "HR Analytics Platform", "preis": "999€/Monat", "mrr": 300000, "trial": "30 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "Contract Analysis Tool", "preis": "599€/Monat", "mrr": 240000, "trial": "14 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "Data Synchronization Service", "preis": "1.499€/Monat", "mrr": 525000, "trial": "30 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "Brand Monitoring Service", "preis": "899€/Monat", "mrr": 405000, "trial": "14 Tage", "prio": "P2", "lp": "Fehlt"},
            {"name": "Sales Funnel Optimizer", "preis": "1.499€/Monat", "mrr": 600000, "trial": "14 Tage", "prio": "P2", "lp": "Fehlt"},
        ]

        db_id = self.database_ids.get("saas_products")
        if not db_id:
            return

        for product in products:
            try:
                self.client.pages.create(
                    parent={"database_id": db_id},
                    properties={
                        "Produktname": {"title": [{"text": {"content": product["name"]}}]},
                        "Preis": {"rich_text": [{"text": {"content": product["preis"]}}]},
                        "Monatliches MRR-Ziel": {"number": product["mrr"]},
                        "Trial-Dauer": {"select": {"name": product["trial"]}},
                        "Priorität": {"select": {"name": product["prio"]}},
                        "Landing-Page-Status": {"status": {"name": product["lp"]}},
                    },
                )
                print(f"  ✓ {product['name']} ({product['prio']})")
            except Exception as e:
                print(f"  ✗ FEHLER bei {product['name']}: {e}")

    def _populate_blog_content(self):
        """Importiert angereicherte Blog-Content aus CSV in Content-Stuecke DB"""
        import csv as csv_mod

        db_id = self.database_ids.get("content_pieces")
        if not db_id:
            print("  WARNUNG: Content-Stuecke DB nicht gefunden.")
            return

        # Suche angereicherte CSV
        csv_path = Path(__file__).parent / "blog_content_output" / "AIxTools_Blogs_ENRICHED.csv"
        if not csv_path.exists():
            # Fallback: suche im mnt-Verzeichnis
            csv_path = Path(__file__).parent / "mnt" / "e" / "projects" / "agents" / "Nurtoring Email" / "blog_content_output" / "AIxTools_Blogs_ENRICHED.csv"
        if not csv_path.exists():
            print("  INFO: Keine angereicherte CSV gefunden. Ueberspringe Blog-Import.")
            print(f"  Gesucht in: {csv_path}")
            return

        imported = 0
        errors = 0

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv_mod.DictReader(f)
            for row in reader:
                asset = row.get('Asset', '')
                is_lp = asset.startswith('Avatar_LP')
                content_type = "Landing Page" if is_lp else "Blog-Artikel"
                titel_de = row.get('Titel_DE', asset)
                meta_de = row.get('Meta_DE', '')

                try:
                    self.client.pages.create(
                        parent={"database_id": db_id},
                        properties={
                            "Titel": {"title": [{"text": {"content": titel_de}}]},
                            "Typ": {"select": {"name": content_type}},
                            "Kanal": {"select": {"name": "Autonova"}},
                            "Status": {"status": {"name": "Idee"}},
                            "Lead-Magnet": {"checkbox": is_lp},
                            "Beschreibung": {"rich_text": [{"text": {"content": meta_de[:2000]}}]},
                        },
                    )
                    imported += 1
                except Exception as e:
                    errors += 1
                    if errors <= 3:
                        print(f"  FEHLER bei {asset}: {e}")

        print(f"  {imported} Blog-Content-Stuecke importiert, {errors} Fehler")

    def _create_dashboard_notes(self):
        """Erstellt Hinweis-Seiten für Dashboard-Ansichten"""
        dashboard_content = """# 📊 Autonova Dashboard-Ansichten

## Empfohlene Ansichten in Notion erstellen:

### 1. E-Mail-Kalender (Kalender-Ansicht)
- Datenbank: E-Mail-Inhalte
- Ansichtstyp: Kalender
- Gruppiere nach: Geplantes Versanddatum
- Filter: Status ≠ Gesendet

### 2. Heutige E-Mails (Listen-Ansicht)
- Datenbank: E-Mail-Inhalte
- Filter: Geplantes Versanddatum = Heute
- Sortierung: Priorität (Hoch zuerst)

### 3. Sequenzen-Übersicht (Kanban)
- Datenbank: E-Mail-Sequenzen
- Ansichtstyp: Board
- Gruppiere nach: Status

### 4. Content-Pipeline (Kanban)
- Datenbank: Content-Stücke
- Ansichtstyp: Board
- Gruppiere nach: Status

### 5. Lead-Funnel (Kanban)
- Datenbank: Kontakte & Leads
- Ansichtstyp: Board
- Gruppiere nach: Status

### 6. SaaS-Launch-Tracker (Kanban)
- Datenbank: SaaS-Produkte
- Ansichtstyp: Board
- Gruppiere nach: Landing-Page-Status

### 7. Woche-für-Woche (Timeline)
- Datenbank: Newsletter-Wochen
- Ansichtstyp: Timeline
- Zeitachse: Sende-Datum
"""

        try:
            self.client.pages.create(
                parent={"page_id": self.page_id},
                properties={
                    "title": [{"text": {"content": "📊 Dashboard-Ansichten (Anleitung)"}}],
                },
                children=[
                    {
                        "object": "block",
                        "type": "heading_1",
                        "heading_1": {
                            "rich_text": [{"text": {"content": "Empfohlene Dashboard-Ansichten"}}]
                        },
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [{"text": {"content": "Erstelle die folgenden Ansichten in den jeweiligen Datenbanken für optimale Übersicht."}}]
                        },
                    },
                ],
            )
            print("  ✓ Dashboard-Anleitung erstellt")
        except Exception as e:
            print(f"  ✗ FEHLER bei Dashboard-Anleitung: {e}")


def main():
    """Hauptfunktion"""
    api_key = os.getenv("NOTION_API_KEY")
    page_id = os.getenv("NOTION_PAGE_ID")

    if not api_key:
        print("FEHLER: NOTION_API_KEY nicht gesetzt!")
        print("Setze den API-Key als Umgebungsvariable:")
        print("  $env:NOTION_API_KEY = 'dein_api_key'")
        print()
        print("So bekommst du den API-Key:")
        print("1. Gehe zu https://www.notion.so/my-integrations")
        print("2. Erstelle eine neue Integration")
        print("3. Kopiere den API-Key")
        print("4. Teile die Integration mit deiner Notion-Seite")
        sys.exit(1)

    if not page_id:
        print("FEHLER: NOTION_PAGE_ID nicht gesetzt!")
        print("Setze die Page-ID als Umgebungsvariable:")
        print("  $env:NOTION_PAGE_ID = 'deine_page_id'")
        print()
        print("So bekommst du die Page-ID:")
        print("1. Öffne die Notion-Seite, unter der die DBs erstellt werden sollen")
        print("2. Die Page-ID ist der letzte Teil der URL")
        print("   Beispiel: https://notion.so/workspace/<PAGE_ID>")
        sys.exit(1)

    # Entferne ggf. Bindestriche aus der Page-ID
    page_id = page_id.replace("-", "")

    setup = AutonovaNotionSetup(api_key, page_id)
    database_ids = setup.setup_all()

    # Speichere Database-IDs für spätere Verwendung
    ids_file = os.path.join(os.path.dirname(__file__), "notion_database_ids.json")
    with open(ids_file, "w", encoding="utf-8") as f:
        json.dump(database_ids, f, indent=2, ensure_ascii=False)
    print(f"\nDatabase-IDs gespeichert in: {ids_file}")


    def _create_scheduling_database(self):
        """Erstelle E-Mail-Scheduling-Datenbank mit Timing-Formeln"""
        print("  -> E-Mail-Scheduling DB...")
        self.database_ids["email_scheduling"] = self._create_database(
            title="📅 E-Mail-Scheduling",
            properties={
                "Betreff": {"title": {}},
                "Kontakt": {"relation": {
                    "database_id": self.database_ids.get("contacts", ""),
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Geplante E-Mails"},
                }},
                "Sequenz": {"relation": {
                    "database_id": self.database_ids.get("email_sequences", ""),
                    "type": "two_way_relation",
                    "two_way_relation": {"name": "Geplante E-Mails"},
                }},
                "Trigger-Datum": {"date": {}},
                "Delay (Tage)": {"number": {"format": "number"}},
                "Berechnetes Versanddatum": {"formula": {
                    "expression": "dateAdd(prop(\"Trigger-Datum\"), prop(\"Delay (Tage)\"), \"days\")"
                }},
                "Zielgruppe": {
                    "select": {
                        "options": [
                            {"name": "Freelancer", "color": "green"},
                            {"name": "B2B Premium", "color": "blue"},
                            {"name": "SaaS", "color": "purple"},
                        ]
                    }
                },
                "Versandzeit": {
                    "select": {
                        "options": [
                            {"name": "09:00", "color": "green"},
                            {"name": "10:30", "color": "blue"},
                            {"name": "14:00", "color": "purple"},
                            {"name": "16:00", "color": "orange"},
                        ]
                    }
                },
                "Status": {
                    "status": {
                        "options": [
                            {"name": "Geplant", "color": "yellow"},
                            {"name": "Faellig", "color": "orange"},
                            {"name": "Gesendet", "color": "green"},
                            {"name": "Abgebrochen", "color": "red"},
                            {"name": "Fehlgeschlagen", "color": "gray"},
                        ]
                    }
                },
                "Prioritaet": {
                    "select": {
                        "options": [
                            {"name": "Hoch", "color": "red"},
                            {"name": "Mittel", "color": "yellow"},
                            {"name": "Niedrig", "color": "gray"},
                        ]
                    }
                },
                "E-Mail-Index": {"number": {"format": "number"}},
                "Fehlermeldung": {"rich_text": {}},
            }
        )

        print(f"  ✓ E-Mail-Scheduling DB erstellt mit Timing-Formel")


if __name__ == "__main__":
    main()
