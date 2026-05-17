import csv

# Definition der NEUEN Kategorien mit Anzahl Assets pro Typ
new_categories = {
    "Avatar Generator": {
        "case_study": 2,
        "checklist": 2,
        "mini_guide": 2,
        "blog": 8
    },
    "YouTube Automations": {
        "case_study": 2,
        "checklist": 2,
        "mini_guide": 2,
        "blog": 8
    },
    "BookWriter": {
        "case_study": 2,
        "checklist": 2,
        "mini_guide": 2,
        "blog": 8
    },
    "Multi-Input Prozessor": {
        "case_study": 2,
        "checklist": 2,
        "mini_guide": 2,
        "blog": 8
    },
    "Nurturing Email Agent": {
        "case_study": 2,
        "checklist": 2,
        "mini_guide": 2,
        "blog": 8
    }
}

# CSV-Datei Pfad
existing_library_path = '/mnt/data/AIxTools_Asset_Bibliothek.csv'

# 1. Bestehende Bibliothek einlesen und höchste Nummer finden
max_nummer = 0
existing_rows = []

try:
    with open(existing_library_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Header speichern
        existing_rows = list(reader)
        
        # Höchste Nummer finden
        for row in existing_rows:
            if row and row[0].isdigit():
                max_nummer = max(max_nummer, int(row[0]))
    
    print(f"Bestehende Bibliothek geladen: {len(existing_rows)} Assets")
    print(f"Hoechste vorhandene Nummer: {max_nummer}")
    
except FileNotFoundError:
    print("Bibliothek nicht gefunden - erstelle neue Datei")
    header = ["Nummer", "Asset-Name", "Type", "Kategorie",
              "Titel_DE", "Meta_DE", "Einleitung_DE", "Hauptabschnitt1_DE", "Hauptabschnitt2_DE", "Hauptabschnitt3_DE", "CTA_DE",
              "Titel_EN", "Meta_EN", "Einleitung_EN", "Hauptabschnitt1_EN", "Hauptabschnitt2_EN", "Hauptabschnitt3_EN", "CTA_EN"]

# 2. Neue Assets vorbereiten
new_assets = []
asset_nummer = max_nummer + 1  # Nächste freie Nummer

for category, asset_types in new_categories.items():
    for asset_type, count in asset_types.items():
        for i in range(count):
            # Asset-Name generieren
            asset_name = f"{category.replace(' ', '_')}_{asset_type}_{i+1}"
            
            # Type in lesbarem Format
            type_readable = asset_type.replace('_', ' ').title()
            
            # Deutsche Inhalte - angepasst nach Asset-Typ
            if asset_type == "case_study":
                titel_de = f"{category} Fallstudie: Erfolgsgeschichte {i+1}"
                meta_de = f"Praxisbeispiel: Wie {category} erfolgreich implementiert wurde."
                einleitung_de = f"Diese Fallstudie zeigt die erfolgreiche Implementierung von {category}."
                ha1_de = f"Ausgangssituation und Herausforderungen"
                ha2_de = f"Implementierung von {category}"
                ha3_de = f"Ergebnisse und ROI-Analyse"
                cta_de = f"Starten Sie Ihre eigene Erfolgsgeschichte mit {category}!"
                
            elif asset_type == "checklist":
                titel_de = f"{category} Checkliste: Schritt-fuer-Schritt Anleitung {i+1}"
                meta_de = f"Praktische Checkliste fuer die effektive Nutzung von {category}."
                einleitung_de = f"Diese Checkliste hilft Ihnen bei der optimalen Verwendung von {category}."
                ha1_de = f"Vorbereitung und Setup"
                ha2_de = f"Wichtige Schritte zur Implementierung"
                ha3_de = f"Kontrolle und Optimierung"
                cta_de = f"Laden Sie die {category} Checkliste herunter!"
                
            elif asset_type == "mini_guide":
                titel_de = f"{category} Mini-Guide: Schnellstart {i+1}"
                meta_de = f"Kompakter Leitfaden fuer den schnellen Einstieg in {category}."
                einleitung_de = f"Dieser Mini-Guide ermoeglicht Ihnen einen schnellen Start mit {category}."
                ha1_de = f"Grundlagen von {category}"
                ha2_de = f"Best Practices und Tipps"
                ha3_de = f"Haeufige Fehler vermeiden"
                cta_de = f"Jetzt mit {category} durchstarten!"
                
            else:  # blog
                titel_de = f"{category} - Blog {i+1}"
                meta_de = f"Entdecke, wie {category} effektiv eingesetzt wird. Artikel {i+1}."
                einleitung_de = f"Dieser Artikel zeigt, wie {category} Unternehmen und Anwender unterstuetzt."
                ha1_de = f"Funktionsweise und Vorteile von {category}"
                ha2_de = f"Praxisbeispiele und Anwendungsfaelle"
                ha3_de = f"Tipps fuer optimale Nutzung von {category}"
                cta_de = f"Jetzt {category} ausprobieren und Effizienz steigern!"
            
            # Englische Inhalte - angepasst nach Asset-Typ
            if asset_type == "case_study":
                titel_en = f"{category} Case Study: Success Story {i+1}"
                meta_en = f"Real-world example: How {category} was successfully implemented."
                einleitung_en = f"This case study demonstrates the successful implementation of {category}."
                ha1_en = f"Initial Situation and Challenges"
                ha2_en = f"Implementation of {category}"
                ha3_en = f"Results and ROI Analysis"
                cta_en = f"Start your own success story with {category}!"
                
            elif asset_type == "checklist":
                titel_en = f"{category} Checklist: Step-by-Step Guide {i+1}"
                meta_en = f"Practical checklist for effective use of {category}."
                einleitung_en = f"This checklist helps you optimize your use of {category}."
                ha1_en = f"Preparation and Setup"
                ha2_en = f"Key Implementation Steps"
                ha3_en = f"Control and Optimization"
                cta_en = f"Download the {category} Checklist!"
                
            elif asset_type == "mini_guide":
                titel_en = f"{category} Mini-Guide: Quick Start {i+1}"
                meta_en = f"Compact guide for getting started quickly with {category}."
                einleitung_en = f"This mini-guide enables you to get started quickly with {category}."
                ha1_en = f"Fundamentals of {category}"
                ha2_en = f"Best Practices and Tips"
                ha3_en = f"Avoiding Common Mistakes"
                cta_en = f"Get started with {category} now!"
                
            else:  # blog
                titel_en = f"{category} - Blog {i+1}"
                meta_en = f"Discover how {category} can be effectively used. Article {i+1}."
                einleitung_en = f"This article explains how {category} supports businesses and users."
                ha1_en = f"Functionality and benefits of {category}"
                ha2_en = f"Practical examples and use cases"
                ha3_en = f"Tips for optimal usage of {category}"
                cta_en = f"Try {category} now and boost efficiency!"
            
            # Neue Zeile erstellen
            new_row = [
                asset_nummer,
                asset_name,
                type_readable,
                category,
                titel_de, meta_de, einleitung_de, ha1_de, ha2_de, ha3_de, cta_de,
                titel_en, meta_en, einleitung_en, ha1_en, ha2_en, ha3_en, cta_en
            ]
            new_assets.append(new_row)
            asset_nummer += 1

# 3. Aktualisierte Bibliothek schreiben
with open(existing_library_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(existing_rows)  # Bestehende Assets
    writer.writerows(new_assets)     # Neue Assets

# Erfolgsmeldung
print(f"\n[OK] {len(new_assets)} neue Assets hinzugefuegt!")
print(f"[OK] Gesamtzahl Assets in Bibliothek: {len(existing_rows) + len(new_assets)}")
print(f"[OK] Neue Nummern: {max_nummer + 1} bis {asset_nummer - 1}")
print(f"\nVerteilung der neuen Assets:")
print(f"- Case Studies: {2 * len(new_categories)} Assets")
print(f"- Checklists: {2 * len(new_categories)} Assets")
print(f"- Mini-Guides: {2 * len(new_categories)} Assets")
print(f"- Blogs: {8 * len(new_categories)} Assets")