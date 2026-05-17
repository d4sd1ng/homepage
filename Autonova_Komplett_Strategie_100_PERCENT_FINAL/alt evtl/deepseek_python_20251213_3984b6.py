# Generierung einer CSV mit SEO-optimierten Blog-Entwürfen DE + EN für Emails 15-90

# Wir erstellen eine einfache CSV-Struktur:
# Email Nr, Asset, Titel_DE, Meta_DE, Einleitung_DE, Hauptabschnitt1_DE, Hauptabschnitt2_DE, Hauptabschnitt3_DE, CTA_DE, 
# Titel_EN, Meta_EN, Einleitung_EN, Hauptabschnitt1_EN, Hauptabschnitt2_EN, Hauptabschnitt3_EN, CTA_EN

import csv
import os

# Emails 15-90 und zugehörige Assets aus Mapping
emails_assets = [
    (i, f"Avatar_Blog{i-14}" if i <= 48 else f"Avatar_LP{i-48}") for i in range(15, 91)
]

# Zielverzeichnis
output_dir = 'mnt/e/projects/agents/Nurtoring Email'

# Stelle sicher, dass das Verzeichnis existiert
os.makedirs(output_dir, exist_ok=True)

# Vollständiger Pfad zur CSV-Datei
blogs_file_path = os.path.join(output_dir, 'AIxTools_Blogs_DE_EN.csv')

# CSV Header
header = ["Email Nr", "Asset",
          "Titel_DE", "Meta_DE", "Einleitung_DE", "Hauptabschnitt1_DE", "Hauptabschnitt2_DE", "Hauptabschnitt3_DE", "CTA_DE",
          "Titel_EN", "Meta_EN", "Einleitung_EN", "Hauptabschnitt1_EN", "Hauptabschnitt2_EN", "Hauptabschnitt3_EN", "CTA_EN"]

with open(blogs_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    
    for email_nr, asset in emails_assets:
        # Beispiel-Titel und Meta (hier kann man später Keyword-Varianten anpassen)
        titel_de = f"Blog-Thema {email_nr} – KI Avatar Generator"
        meta_de = f"Erfahre, wie KI Avatare für Marketing, Social Media und Teams erstellt werden. Artikel {email_nr}."
        einleitung_de = f"Dieser Artikel erklärt, wie du KI Avatare effizient für dein Business einsetzen kannst. Blog {email_nr}."
        ha1_de = "Funktionsweise und Vorteile der KI Avatare."
        ha2_de = "Praxisbeispiele und Einsatzmöglichkeiten."
        ha3_de = "Tipps für optimale Ergebnisse mit KI Avataren."
        cta_de = "Erstelle jetzt deinen KI-Avatar und steigere deine Sichtbarkeit!"

        titel_en = f"Blog Topic {email_nr} – AI Avatar Generator"
        meta_en = f"Learn how AI avatars are created for marketing, social media and teams. Article {email_nr}."
        einleitung_en = f"This article explains how to efficiently use AI avatars for your business. Blog {email_nr}."
        ha1_en = "Functionality and advantages of AI avatars."
        ha2_en = "Practical examples and use cases."
        ha3_en = "Tips for optimal results with AI avatars."
        cta_en = "Create your AI avatar now and boost your visibility!"

        writer.writerow([email_nr, asset,
                         titel_de, meta_de, einleitung_de, ha1_de, ha2_de, ha3_de, cta_de,
                         titel_en, meta_en, einleitung_en, ha1_en, ha2_en, ha3_en, cta_en])

print(f"CSV-Datei wurde erfolgreich erstellt: {blogs_file_path}")
print(f"Anzahl der generierten Blog-Entwürfe: {len(emails_assets)}")
print(f"Dateigröße: {os.path.getsize(blogs_file_path) / 1024:.2f} KB")

# Zeige die ersten 5 Zeilen zur Überprüfung
print("\nErste 5 Zeilen der CSV-Datei:")
with open(blogs_file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 6:  # Header + 5 Datenzeilen
            print(f"Zeile {i+1}: {line.strip()}")