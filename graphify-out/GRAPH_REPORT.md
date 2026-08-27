# Graph Report - homepage  (2026-08-22)

## Corpus Check
- Large corpus: 213 files · ~2,015,992 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 532 nodes · 818 edges · 36 communities (35 shown, 1 thin omitted)
- Extraction: 83% EXTRACTED · 15% INFERRED · 2% AMBIGUOUS · INFERRED: 126 edges (avg confidence: 0.82)
- Token cost: 167,852 input · 0 output

## Community Hubs (Navigation)
- ROI & Wirtschaftlichkeitsrechnung
- Branchenseiten & Zielgruppen
- Case-Study-Szenarien & Deep-Analyse
- Sprachassistenten & Paketangebote
- Paketmodule, Preise & Datenschutz
- Workflows & Download-Ressourcen
- Datenabgleich & KI-Agenten
- Rechtliche Hinweise zur Analyse
- Startseite & Analyse-Einstieg
- KI-Governance & Sicherheit
- Prompt-Systeme & Ausgabequalität
- KI-Roadmap & Priorisierung
- Datenschutz & DSGVO
- Logo-Mark Gestaltung
- Hero-Bildwelt Sphäre
- Prozessautomatisierung-Module
- Individuelle KI-Software & Integration
- SEO & digitale Sichtbarkeit
- Automationen Baustelle & Betreuung
- AGB, Impressum & Hosting
- Wordmark & Markentonalität
- Interner Betriebsassistent
- Favicon-Asset & Auslieferung
- KI-Chatbots & Kundenservice
- Warum Nurovelle / Positionierung
- Call-to-Action-Elemente
- Cookies & Website-Betrieb
- Automationen Pflege & Marketing
- KI-Automationen Überblick
- Leistungsübersicht & Detailseiten
- Prozessschritte Geschäftsprozess zu KI
- Automationen Büro
- Sockel-Rendering Code
- Automationen Personal
- Menschliche Prüfung & Eskalation

## God Nodes (most connected - your core abstractions)
1. `KI-Sicherheit & Governance` - 30 edges
2. `KI-Agenten` - 29 edges
3. `Dokumenten-, Daten- und Abgleichsysteme` - 28 edges
4. `Individuelle KI-Software & Integration` - 28 edges
5. `Prozessautomatisierung` - 28 edges
6. `Prompt Engineering` - 27 edges
7. `KI-Roadmap` - 27 edges
8. `Leistungsuebersicht (index.html#leistungen)` - 24 edges
9. `AGB - Allgemeine Geschaeftsbedingungen` - 16 edges
10. `Nurovelle Startseite` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Modellhaftigkeitshinweis: keine echte Kundenreferenz` --semantically_similar_to--> `Ehrlicher Stand: noch kein Produktivkunde, Pilot-Deploy offen`  [INFERRED] [semantically similar]
  assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf → paket-buero.html
- `Szenario B: Angebotserstellung im Handwerk (Elektroinstallation)` --semantically_similar_to--> `Handwerkspaket (Produktpaket)`  [INFERRED] [semantically similar]
  assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf → paket-handwerk.html
- `Mensch bleibt im Prozess (Sonderfälle, Stichprobe, Freigabe)` --semantically_similar_to--> `Modul Regiebericht aus Sprachnachricht`  [INFERRED] [semantically similar]
  assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf → paket-handwerk.html
- `ROI und Amortisation als Entscheidungskriterium` --semantically_similar_to--> `ROI-Überschlag je Prozess`  [INFERRED] [semantically similar]
  assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf → potenzialanalyse-deep.html
- `ROI-Fragen und Priorisierung` --semantically_similar_to--> `ROI und Amortisation als Entscheidungskriterium`  [INFERRED] [semantically similar]
  praxisleitfaden.html → assets/downloads/CASE_STUDY_KI_AUTOMATISIERUNG_NUROVELLE_FINAL.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Rechtliche Absicherung der kostenlosen Potenzialanalyse ueber AGB, Analyse-Hinweise und Datenschutz** — agb_unverbindlichkeit_der_analyse, analyse_rechtliche_hinweise_kostenlos_unverbindlich, datenschutz_ki_potenzialanalyse_datenverarbeitung, analyse_kostenlose_ki_potenzialanalyse, analyse_abgrenzung [INFERRED 0.85]
- **Pruefdimensionen der Potenzialanalyse: Prozesse, Daten, Systeme, Potenzial** — analyse_prozesse, analyse_daten, analyse_systeme, analyse_potenzial, analyse_kostenlose_ki_potenzialanalyse [EXTRACTED 1.00]
- **Dialogfluss des KI-Chatbots von Eingang bis Dokumentation** — detail_chatbots_modul_eingang, detail_chatbots_modul_erkennung, detail_chatbots_modul_kontext, detail_chatbots_modul_rueckfrage, detail_chatbots_modul_wissenszugriff, detail_chatbots_modul_antwort, detail_chatbots_modul_uebergabe, detail_chatbots_modul_dokumentation [EXTRACTED 1.00]
- **Human-in-the-Loop: Kontrollpunkte fuer unklare und kritische Faelle** — detail_datenabgleich_menschliche_pruefung, detail_ki_agenten_uebergabe, detail_prozessautomatisierung_uebergabe, detail_ki_sicherheit_eskalation [INFERRED 0.85]
- **Gemeinsames Acht-Modul-Muster der Leistungsdetailseiten** — detail_ki_agenten_agentenmodule, detail_ki_sicherheit_governance_module, detail_prompt_engineering_prompt_system, detail_prozessautomatisierung_workflow_module, detail_roadmap_roadmap_module [INFERRED 0.85]
- **Gemeinsames Sektionsschema der Detailseiten (ausgangslage, leistungsumfang, module, anwendung, moeglich, nutzen, kontakt, faq)** — detail_datenabgleich_abgleichsysteme, detail_ki_agenten_ki_agenten, detail_ki_sicherheit_ki_governance, detail_ki_software_individuelle_ki_software, detail_prompt_engineering_prompt_engineering, detail_prozessautomatisierung_prozessautomatisierung, detail_roadmap_ki_roadmap [EXTRACTED 1.00]
- **Elf KI-Leistungsbereiche als durchgehender Ablauf** — index_leistungen, index_leistung_potenzialanalyse, index_leistung_ki_roadmap, index_leistung_ki_agenten, index_leistung_chatbots, index_leistung_sprachassistenten, index_leistung_ki_automationen, index_leistung_ki_governance, index_leistung_ki_workflows, index_leistung_daten_abgleich, index_leistung_ki_software, index_leistung_seo_systeme [EXTRACTED 1.00]
- **Sechs Schritte vom Geschäftsprozess zur KI-Lösung** — index_prozess_aufgabe_erfassen, index_prozess_ki_potenzial_bewerten, index_prozess_daten_pruefen, index_prozess_prozess_modellieren, index_prozess_loesung_auswaehlen, index_prozess_umsetzung_strukturieren [EXTRACTED 1.00]
- **Vier Handgriffe des Betreuungspakets in einer Anwendung** — paket_betreuung_betreuungspaket, paket_betreuung_modul_betreuungsbericht, paket_betreuung_modul_angehoerige_informieren, paket_betreuung_modul_verspaetung_melden, paket_betreuung_modul_leistungsnachweis_pruefen, paket_betreuung_whatsapp_sprachnachricht [EXTRACTED 1.00]
- **Gemeinsames Paket-Geschäftsmodell: eigener EU-Server, Servicevertrag, Bündelpreis** — paket_buero_bueropaket, paket_handwerk_handwerkspaket, paket_buero_eigene_instanz, paket_buero_buendelrabatt, paket_handwerk_buendelrabatt [INFERRED 0.85]
- **ROI-Argumentation über drei modellhafte Szenarien** — assets_downloads_case_study_ki_automatisierung_nurovelle_final_szenario_a_steuerkanzlei, assets_downloads_case_study_ki_automatisierung_nurovelle_final_szenario_b_handwerk, assets_downloads_case_study_ki_automatisierung_nurovelle_final_szenario_c_ecommerce, assets_downloads_case_study_ki_automatisierung_nurovelle_final_szenarienvergleich, assets_downloads_case_study_ki_automatisierung_nurovelle_final_roi_amortisation [EXTRACTED 1.00]
- **Kundenreise: Leitfaden, kostenlose Ersteinschätzung, Deep-Analyse, Produktpaket** — praxisleitfaden_praxisleitfaden, potenzialanalyse_deep_kostenlose_ersteinschaetzung, potenzialanalyse_deep_deep_potenzialanalyse, paket_buero_bueropaket, paket_handwerk_handwerkspaket [INFERRED 0.75]
- **ROI-Berechnungsablauf fuer KI-Projekte** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_kostenbasis, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_nutzenbasis, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_baseline_messung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_zielwert_definition, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_amortisationsrechnung [EXTRACTED 1.00]
- **Werkzeugkasten zur KI-Potenzialbewertung** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_ki_potenzial_selbsttest, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_roi_schnellrechner, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_priorisierungsmatrix, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_zehn_prozesse_mit_hohem_roi_potenzial, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_neunzig_tage_plan [INFERRED 0.85]
- **Nurovelle Download-Lead-Magnets** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_guide, assets_downloads_checkliste_ki_potenziale, assets_downloads_prompt_guide [INFERRED 0.75]
- **Branchenseiten fuehren einheitlich in die Potenzialanalyse** — detailseiten_branchen_gesundheitswesen_pflege_seite, detailseiten_branchen_immobilien_facility_management_seite, detailseiten_branchen_industrie_produktion_seite, detailseiten_branchen_sonstiges_seite, detailseiten_branchen_verwaltung_vertrieb_einkauf_marketing_seite, detailseiten_branchen_gesundheitswesen_pflege_potenzialanalyse_cta [EXTRACTED 1.00]
- **Wartung und Anlagen-/Objektdaten als branchenuebergreifender Anwendungsfall** — detailseiten_branchen_immobilien_facility_management_wartung, detailseiten_branchen_immobilien_facility_management_objekte, detailseiten_branchen_industrie_produktion_wartung, detailseiten_branchen_industrie_produktion_maschinen [INFERRED 0.85]
- **Strukturieren und Ordnen von Daten als gemeinsames Nutzenversprechen** — detailseiten_branchen_immobilien_facility_management_kernnutzen, detailseiten_branchen_industrie_produktion_kernnutzen, detailseiten_branchen_verwaltung_vertrieb_einkauf_marketing_kernnutzen, detailseiten_branchen_sonstiges_kernnutzen, detailseiten_branchen_gesundheitswesen_pflege_kernnutzen [INFERRED 0.75]

## Communities (36 total, 1 thin omitted)

### Community 0 - "ROI & Wirtschaftlichkeitsrechnung"
Cohesion: 0.07
Nodes (54): Checkliste KI-Potenziale (Platzhalter), Prompt Guide (Platzhalter), Amortisations- und ROI-Beispielrechnung, Prozess: Angebotsbearbeitung, Baseline-Messung vor dem KI-Pilot, Prozess: Datenpflege, Datenqualitaet als Wirtschaftlichkeitsfaktor, Prozess: Dokumentation (+46 more)

### Community 1 - "Branchenseiten & Zielgruppen"
Cohesion: 0.05
Nodes (47): Schwerpunkt Berichte & Berichtspflichten, Branchenkarte cards_branche/5.png, Branchenuebersicht index.html#branchen, Schwerpunkt Dokumentation, Schwerpunkt Formulare, Kernnutzen: Entlastung von Dokumentation, Terminplanung, Ressourcen und Berichtspflichten, Potenzialanalyse als Einstieg (analyse.html), Schwerpunkt Ressourcen (+39 more)

### Community 2 - "Case-Study-Szenarien & Deep-Analyse"
Cohesion: 0.07
Nodes (40): 30-Tage-Fahrplan für den Pilotstart, Case Study KI-Automatisierung: drei modellhafte Mittelstandsszenarien, Datencheck vor Projektstart, Gemeinsame Erfolgsfaktoren: häufiger, messbarer, regelbasierter Startprozess, Executive Briefing (Quelle der Szenarien), Fazit: Nutzen aus konkreter Prozessverbesserung, nicht aus KI-Strategie, Mensch bleibt im Prozess (Sonderfälle, Stichprobe, Freigabe), Modellhaftigkeitshinweis: keine echte Kundenreferenz (+32 more)

### Community 3 - "Sprachassistenten & Paketangebote"
Cohesion: 0.07
Nodes (37): KI-Chatbots (Detailseite), Daten-Abgleich Detailseite, KI-Governance / KI-Sicherheit Detailseite, Anwendungsfelder Sprache (Telefonservice, Terminvereinbarung, Außendienst), Ausgangslage Telefonie (Anruflast, Wartezeiten, manuelle Notizen), KI-Sprachassistent, Konzeption Sprachassistent, Module des Dialogs (+29 more)

### Community 4 - "Paketmodule, Preise & Datenschutz"
Cohesion: 0.08
Nodes (30): Bündelpreis bei weiterem Paket (349 € / 39 €), Büropaket (Produktpaket), CTA: Büropaket anfragen / Erstgespräch vereinbaren, Datenschutzkonzept Büropaket (DE/EU, TLS, Löschfristen, AVV), Ehrlicher Stand: noch kein Produktivkunde, Pilot-Deploy offen, Eigene getrennte Instanz auf eigenem EU-Server, FAQ Büropaket, Modul Bewertungsanfragen mit Sperrliste (+22 more)

### Community 5 - "Workflows & Download-Ressourcen"
Cohesion: 0.12
Nodes (19): Prompt Engineering Detailseite, Prozessautomatisierung Detailseite, SEO-Monitoring, Anwendungsfelder Workflow (Rechnungen, Freigaben, CRM, Onboarding), Ausgangslage Abläufe (doppelte Eingaben, Medienbrüche, fehlende Statusübersicht), Automatisierte Workflows, Konzeption Workflow, Module des Workflows (+11 more)

### Community 6 - "Datenabgleich & KI-Agenten"
Cohesion: 0.14
Nodes (18): Dokumenten-, Daten- und Abgleichsysteme, Anwendungsfelder Abgleichsysteme (Rechnungspruefung, Vertragspruefung, Stammdatenpflege, Dublettenpruefung, CRM-/ERP-Abgleich, Datenmigration), Datenabgleich (exakte Regeln und tolerante Aehnlichkeitspruefung), Dokumentenverarbeitung (Erkennung, Klassifikation, Feldextraktion), FAQ Dokumenten- und Abgleichsysteme, Klare Entscheidungsgrundlage (Datenquellen, Dokumenttypen und Pruefkriterien vorab festlegen), Leistungsumfang: Konzeption und Umsetzung, Nutzen Abgleichsysteme (weniger Pruefaufwand, weniger Doppelarbeit, bessere Datenqualitaet, Nachvollziehbarkeit) (+10 more)

### Community 7 - "Rechtliche Hinweise zur Analyse"
Cohesion: 0.14
Nodes (16): Unverbindlichkeit der kostenlosen Potenzialanalyse, Vertragsschluss bei spaeteren Leistungen, Abgrenzung: was die kostenlose Analyse nicht ist, Ausgangslage - unklare Anwendungsfaelle, Prozessabgrenzung, Datenbasis, Abhaengigkeiten, Risiken, Reihenfolge, Pruefdimension Daten, Ergebnis: Ersteinschaetzung mit Priorisierung und naechstem Schritt, Kostenlose KI-Potenzialanalyse, Pruefdimension Potenzial (+8 more)

### Community 8 - "Startseite & Analyse-Einstieg"
Cohesion: 0.17
Nodes (16): Ablauf der Analyse in vier Schritten, Deep-Potenzialanalyse (kostenpflichtig), FAQ zur kostenlosen Potenzialanalyse, Naechster Schritt nach der Analyse, Kostenlose KI-Potenzialanalyse (Seite), API System-Integration, Calendly Erstgespräch (30 min), Sektion FAQ — Fragen zu KI-Projekten (+8 more)

### Community 9 - "KI-Governance & Sicherheit"
Cohesion: 0.14
Nodes (15): Anonymisierung (Maskierung/Pseudonymisierung personenbezogener Daten), Datenqualitaet (wiederkehrende Pruefungen, Fehlerquellen sichtbar machen), Anwendungsfelder Governance (interne KI-Nutzung, Agenten mit Systemzugriff, Chatbots, sensible Dokumentenverarbeitung, externe KI-Dienste), Datenfreigabe (zulaessige Quellen, vertrauliche Inhalte), FAQ KI-Governance, Module der Governance (Bestandsaufnahme bis Ueberwachung), KI-Sicherheit & Governance, Klare Entscheidungsgrundlage (Risiken, Zugriffe und Kontrollbedarf vor Einfuehrung einordnen) (+7 more)

### Community 10 - "Prompt-Systeme & Ausgabequalität"
Cohesion: 0.14
Nodes (14): AGB, Datenaufbereitung (Normalisierung, Dubletten, Formatvereinheitlichung), Qualitaetspruefung von KI-Ergebnissen, Anwendungsfelder Prompt-Systeme (Textentwicklung, Berichterstellung, Dokumentenpruefung, Recherche, Wissensmanagement, Kundenservice), Ausgabeformat (Struktur, Umfang, Darstellungsform), FAQ Prompt Engineering, Klare Entscheidungsgrundlage (Einzelprompt, Prompt-System oder technische Integration abwaegen), Kontext (strukturierte Bereitstellung benoetigter Informationen) (+6 more)

### Community 11 - "KI-Roadmap & Priorisierung"
Cohesion: 0.14
Nodes (14): Risikoeinordnung von KI-Anwendungen, Prototyp / MVP als erster Umsetzungsschritt, Anwendungsfelder KI-Roadmap (Unternehmensstrategie, Prozessautomatisierung, Datenverarbeitung, Wissensmanagement, Governance, Pilotprojekte), Bewertung von Nutzen, Aufwand, Risiken und Umsetzbarkeit, FAQ KI-Roadmap, KI-Roadmap, Klare Entscheidungsgrundlage (Reihenfolge und Voraussetzungen der Vorhaben sichtbar machen), Leistungsumfang: Strategie und Planung (+6 more)

### Community 12 - "Datenschutz & DSGVO"
Cohesion: 0.19
Nodes (13): Nurovelle, Tino Schneider (Anbieter / Verantwortlicher), Branchenauswahl im Analyseformular, Potenzialanalyse-Formular, Betroffenenrechte nach DSGVO, DSGVO, Grundsatz der Datenverarbeitung (Art. 6 DSGVO), Keine automatisierte Entscheidung (Art. 22 DSGVO) (+5 more)

### Community 13 - "Logo-Mark Gestaltung"
Cohesion: 0.27
Nodes (13): Alternate Reading as Abstract Head-and-Body Figure, Notched Counter Shape Inside the N, Energetic, Optimistic Brand Tone, Detached Spherical Dot Above the Mark, Glossy Highlight and Gradient Shading, Primary Brand Identity in the Hero Section, Isometric 3D Extrusion Treatment, Geometric Letter-N Monogram (+5 more)

### Community 14 - "Hero-Bildwelt Sphäre"
Cohesion: 0.26
Nodes (13): Bildidee: KI, Datenvernetzung und Reichweite visualisieren, Hero-Asset: Vernetzte Sphaere (round.png), Nurovelle Hero-Bildwelt, Leiterbahn-/Platinen-Metapher, Freigestelltes Motiv auf transparentem Hintergrund, Glasfacetten und Panel-Segmente auf der Kugeloberflaeche, Goldene Leuchtpunkte als Akzent, Einsatz als dekoratives Hero-Visual hinter Headline und Logo (+5 more)

### Community 15 - "Prozessautomatisierung-Module"
Cohesion: 0.15
Nodes (13): Datenschutz, Module des Agenten (Eingang, Kontext, Datenzugriff, Pruefung, Vorbereitung, Aktion, Uebergabe, Dokumentation), Dokumentation ausgefuehrter Agentenaktionen, Anwendungsfelder Prozessautomatisierung (Angebotsprozesse, Rechnungsverarbeitung, Freigabeworkflows, Lead-Verarbeitung, Kunden-Onboarding), Ausloeser (Ereignis, Eingabe oder Zeitpunkt startet den Prozess), Dokumentation von Bearbeitungsstaenden und Prozessschritten, Entscheidung nach festgelegten Regeln, FAQ Prozessautomatisierung (+5 more)

### Community 16 - "Individuelle KI-Software & Integration"
Cohesion: 0.15
Nodes (13): Datenzugriff auf freigegebene Quellen, Anwendungsfelder KI-Software (interne Unternehmenssoftware, Portale, Prozesssteuerung, Dashboards, CRM-/ERP-Erweiterungen, API-/MCP-Integrationen), API-Integration (Datenaustausch, Webhooks, Zielsysteme), Benutzeroberflaechen (rollenbasierte Masken, Pruef- und Freigabeansichten), Betrieb und Erweiterung (spaetere Funktionen und Systemanbindungen), FAQ Individuelle KI-Software, Individuelle KI-Software & Integration, Klare Entscheidungsgrundlage (Integration, internes Tool, Prototyp oder Individualentwicklung abwaegen) (+5 more)

### Community 17 - "SEO & digitale Sichtbarkeit"
Cohesion: 0.19
Nodes (13): SEO-Ausgangslage (unklare Keywords, technische Fehler, Anzeigenabhängigkeit), Content-Struktur, Interne Verlinkung, Keyword-Strategie, Lokale Sichtbarkeit, OnPage-Optimierung, SEO & digitale Sichtbarkeit (Detailseite), Seitenarchitektur (+5 more)

### Community 18 - "Automationen Baustelle & Betreuung"
Cohesion: 0.20
Nodes (11): Paragraf 45b-Budgetmonitor (SGB XI Entlastungsbetrag), Abnahme- und Uebergabeprotokoll, Diktier-Assistent fuer Betreuungsberichte, Gruppe 2 - Baustelle (5 Automationen), Gruppe 4 - Betreuung (6 Automationen), Material- und Verbrauchsprotokoll, Regiebericht und Nachtrag, Schlechtwetter- und Terminwarnung (+3 more)

### Community 19 - "AGB, Impressum & Hosting"
Cohesion: 0.22
Nodes (10): Geltungsbereich der AGB, Haftungsbeschraenkung fuer kostenlose Ersteinschaetzungen, Hetzner Online GmbH (Hosting-Anbieter), Mitwirkungspflicht des Anfragenden, AGB - Allgemeine Geschaeftsbedingungen, Schlussbestimmungen (Recht der Bundesrepublik Deutschland), Hosting und technische Protokolldaten, Haftung für Inhalte und Links (+2 more)

### Community 20 - "Wordmark & Markentonalität"
Cohesion: 0.22
Nodes (10): Approachable, Warm, Non-Corporate Brand Tone, Brand Name "Nurovelle", Intended Placement on Dark Background, Hero Section Brand Identity Role, Wordmark/Logo Lockup Pairing, Possible "Nuro"/Neuro AI Naming Semantics, Rounded Hand-Drawn Sans Lettering, Transparent-Background PNG Overlay Asset (+2 more)

### Community 21 - "Interner Betriebsassistent"
Cohesion: 0.20
Nodes (10): E-Mail- und Chat-Sortierung, Interner Betriebsassistent, Modul Antwort, Modul Dokumentation, Modul Eingang, Modul Erkennung (Thema und Absicht), Modul Kontext (Gespraechsverlauf und Vorgangsdaten), Modul Rueckfrage (+2 more)

### Community 22 - "Favicon-Asset & Auslieferung"
Cohesion: 0.33
Nodes (10): Embedded 600x600 Base64 PNG Payload, Detached Circular Dot (Tittle Accent), Gold-Yellow Brand Color, Isometric 3D Extrusion Style, Extruded N Monogram Mark, Nurovelle Brand Identity, Mark Shared With Hero Logo Asset, Browser Tab Identity Role (+2 more)

### Community 23 - "KI-Chatbots & Kundenservice"
Cohesion: 0.22
Nodes (9): KI-gestuetzte Inhalte als Arbeitshilfen, Typische Einsatzbereiche der Potenzialanalyse, Anwendungsbereiche (Kundenservice, Mitarbeiter-Support, Wissensmanagement), Ausgangslage: Standardanfragen verursachen hohen Aufwand, KI-Chatbots, Klare Entscheidungsgrundlage - freigegebene Themen und Inhalte, Lead-Erfassung ueber den Chatbot, Leistungsumfang von Konzeption bis Umsetzung (+1 more)

### Community 24 - "Warum Nurovelle / Positionierung"
Cohesion: 0.28
Nodes (9): Die passende Lösung, Warum Nurovelle (Detailseite), Strukturiertes Vorgehen, Technik mit Systemverständnis, Anbieterkennzeichnung / Verantwortlicher, Nurovelle, Prozess zuerst — dann Technologie, Tino Schneider (+1 more)

### Community 25 - "Call-to-Action-Elemente"
Cohesion: 0.25
Nodes (8): Kostenlose Potenzialanalyse (analyse.html), CTA: Datenqualitaet erhoehen, CTA: Agentenpotenzial pruefen, CTA: KI-Nutzung absichern, CTA: Loesung entwickeln, CTA: Prompt-Potenzial pruefen, CTA: Prozesse pruefen / Kostenlose Potenzialanalyse starten, CTA: Roadmap entwickeln

### Community 26 - "Cookies & Website-Betrieb"
Cohesion: 0.29
Nodes (8): Analyse- und Marketing-Cookies (aktuell nicht eingebunden), Cookie-Verwaltung ueber Browser-Einstellungen, Datensparsamer Website-Betrieb, Einwilligung und Widerruf (Cookie-Banner), Cookie-Hinweis, Technisch erforderliche Cookies, Cookies und aehnliche Technologien, Lokale Auslieferung von Schriften und Bibliotheken

### Community 27 - "Automationen Pflege & Marketing"
Cohesion: 0.29
Nodes (7): Angehoerigen-Information bei Verspaetung, Angehoerigen-Informations-Agent, Google-Bewertungssystem, Gruppe 5 - Marketing und Kommunikation (5 Automationen), Medizinischer Dokumentations-Assistent, Rezept- und Medikamenten-Manager, 24/7-Telefonassistent

### Community 28 - "KI-Automationen Überblick"
Cohesion: 0.29
Nodes (7): Ausgangslage: Fachkraeftemangel, Dokumentationspflichten, Zeitdruck, Datensicherheit der Automationen (eigene Infrastruktur oder DSGVO-konforme Cloud), 25 KI-Automationen, Nutzen der KI-Automationen (weniger manuelle Arbeit, geringere Fehlerquote), KI-Automationen (Detailseite), Schrittweise Einfuehrung (2-3 Automationen zuerst), Leistung 06 — KI-Automationen

### Community 29 - "Leistungsübersicht & Detailseiten"
Cohesion: 0.29
Nodes (7): KI-Agenten Detailseite, KI-Software Detailseite, KI-Roadmap Detailseite, Leistung 03 — KI-Agenten, Leistung 02 — KI-Roadmap, Leistung 10 — KI-Software, Leistungsuebersicht (index.html#leistungen)

### Community 30 - "Prozessschritte Geschäftsprozess zu KI"
Cohesion: 0.29
Nodes (7): Prozessschritt 1 — Aufgabe erfassen, Prozessschritt 3 — Daten prüfen, Prozessschritt 2 — KI-Potenzial bewerten, Prozessschritt 5 — Lösung auswählen, Prozessschritt 4 — Prozess modellieren, Prozessschritt 6 — Umsetzung strukturieren, Sektion Vom Geschäftsprozess zur KI-Lösung

### Community 31 - "Automationen Büro"
Cohesion: 0.40
Nodes (6): Angebots-Generator, Dokumenten-Onboarding, Gruppe 1 - Buero (6 Automationen), Leistungsnachweis- und Abtretungserfassung, Rechnungs- und Belegleser, Termin-Erinnerung und Ausfallschutz

### Community 33 - "Automationen Personal"
Cohesion: 0.50
Nodes (4): Dienstplan-Tausch-System, Gruppe 3 - Personal (3 Automationen), Krankmelde-Assistent, Urlaubs-Manager

### Community 34 - "Menschliche Prüfung & Eskalation"
Cohesion: 0.67
Nodes (4): Menschliche Pruefung (unklare und kritische Faelle an Mitarbeitende), Uebergabe unklarer oder sensibler Faelle an eine zustaendige Person, Eskalation kritischer Vorgaenge, Uebergabe von Freigaben, Ausnahmen und unklaren Faellen

## Ambiguous Edges - Review These
- `Prozessautomatisierung` → `Leistungsuebersicht (index.html#leistungen)`  [AMBIGUOUS]
  detail_prozessautomatisierung.html · relation: conceptually_related_to
- `CTA: Büropaket anfragen / Erstgespräch vereinbaren` → `Slack Incoming Webhook (Formular-/Benachrichtigungskanal)`  [AMBIGUOUS]
  slack.md · relation: shares_data_with
- `Kostenbasis: einmalige und laufende Kosten` → `Prompt Guide (Platzhalter)`  [AMBIGUOUS]
  assets/downloads/prompt_guide.pdf · relation: conceptually_related_to
- `Schwerpunkt Termine / Terminplanung` → `Schwerpunkt Tickets & Mieteranfragen`  [AMBIGUOUS]
  detailseiten/branchen/immobilien-facility-management.html · relation: semantically_similar_to
- `Brand Name "Nurovelle"` → `Possible "Nuro"/Neuro AI Naming Semantics`  [AMBIGUOUS]
  assets/hero/Nurovelle_schrift.png · relation: semantically_similar_to
- `Nurovelle Logo Mark (3D Yellow N)` → `Alternate Reading as Abstract Head-and-Body Figure`  [AMBIGUOUS]
  assets/hero/nurovelle_logo.png · relation: conceptually_related_to
- `Nurovelle Logo Mark (3D Yellow N)` → `Neuro/AI Symbolism of Mark and Dot`  [AMBIGUOUS]
  assets/hero/nurovelle_logo.png · relation: rationale_for
- `Detached Spherical Dot Above the Mark` → `Neuro/AI Symbolism of Mark and Dot`  [AMBIGUOUS]
  assets/hero/nurovelle_logo.png · relation: rationale_for
- `Notched Counter Shape Inside the N` → `Alternate Reading as Abstract Head-and-Body Figure`  [AMBIGUOUS]
  assets/hero/nurovelle_logo.png · relation: conceptually_related_to
- `Hero-Asset: Vernetzte Sphaere (round.png)` → `Leiterbahn-/Platinen-Metapher`  [AMBIGUOUS]
  assets/hero/round.png · relation: semantically_similar_to
- `Glasfacetten und Panel-Segmente auf der Kugeloberflaeche` → `Leiterbahn-/Platinen-Metapher`  [AMBIGUOUS]
  assets/hero/round.png · relation: conceptually_related_to
- `favicon.svg (Site Favicon Asset)` → `Mark Shared With Hero Logo Asset`  [AMBIGUOUS]
  favicon.svg · relation: semantically_similar_to
- `Detached Circular Dot (Tittle Accent)` → `Nurovelle Brand Identity`  [AMBIGUOUS]
  favicon.svg · relation: conceptually_related_to

## Knowledge Gaps
- **154 isolated node(s):** `Geltungsbereich der AGB`, `Mitwirkungspflicht des Anfragenden`, `Haftungsbeschraenkung fuer kostenlose Ersteinschaetzungen`, `Schlussbestimmungen (Recht der Bundesrepublik Deutschland)`, `Grenzen der Einschaetzung (keine Ergebnisgarantie)` (+149 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Prozessautomatisierung` and `Leistungsuebersicht (index.html#leistungen)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `CTA: Büropaket anfragen / Erstgespräch vereinbaren` and `Slack Incoming Webhook (Formular-/Benachrichtigungskanal)`?**
  _Edge tagged AMBIGUOUS (relation: shares_data_with) - confidence is low._
- **What is the exact relationship between `Kostenbasis: einmalige und laufende Kosten` and `Prompt Guide (Platzhalter)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Schwerpunkt Termine / Terminplanung` and `Schwerpunkt Tickets & Mieteranfragen`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Brand Name "Nurovelle"` and `Possible "Nuro"/Neuro AI Naming Semantics`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Nurovelle Logo Mark (3D Yellow N)` and `Alternate Reading as Abstract Head-and-Body Figure`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Nurovelle Logo Mark (3D Yellow N)` and `Neuro/AI Symbolism of Mark and Dot`?**
  _Edge tagged AMBIGUOUS (relation: rationale_for) - confidence is low._