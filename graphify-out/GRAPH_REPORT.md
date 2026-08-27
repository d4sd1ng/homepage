# Graph Report - homepage  (2026-08-23)

## Corpus Check
- Large corpus: 227 files · ~2,409,131 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 803 nodes · 2071 edges · 38 communities (37 shown, 1 thin omitted)
- Extraction: 47% EXTRACTED · 51% INFERRED · 2% AMBIGUOUS · INFERRED: 1061 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Branchenseiten & Querschnitts-Use-Cases
- Case Study, Checkliste & Einführung
- AGB, Datenschutz & rechtliche Grenzen
- ROI-Berechnung & Wirtschaftlichkeit
- Positionierung & Leistungsüberblick
- Einführungsprinzipien der Automatisierung
- Workflow-Module & Aufgabensteuerung
- Wissenszugriff & Systemintegration
- KI-Agenten für Kundenservice & Assistenz
- Datenquellen & CRM/ERP-Abgleich
- Deep-Potenzialanalyse & Kontakt
- Download-Bibliothek & Formulare
- Dokumentenverarbeitung & Abgleich
- KI-Governance & Roadmap-Handlungsfelder
- Automationsgruppen Bau, Büro & Personal
- Paket-Grundstruktur & Zielgruppen
- Paket-Module & Eingabekanäle
- Potenzialanalyse: Ablauf & Defizite
- Belegerfassung & Berichtserstellung
- Prüf- und Validierungsmodule
- SEO, Prototyping & Ausgabequalität
- Prozessschritte & Prüfdimensionen
- Risikoeinordnung & Kontextstruktur
- Analyseergebnis & Priorisierung
- FAQ & Entscheidungsgrundlagen
- Eskalation & Dokumentationspflichten
- Leistungsnachweis, Abnahme & Slack-Setup
- AVV & Datenschutzkonzepte der Pakete
- Freigaben, Berechtigungen & Kontrolle
- Datenschutz-Grundsätze & Betriebsmodell
- Serverstandort & Einrichtungsleistungen
- Preise & Servicevertrag
- Frageerkennung & Gesprächskontext
- Beratung, Dashboards & Seitenarchitektur
- WhatsApp-Module & Prüffristen
- Sockel-Rendering Code
- Rechtsstand & Schlussbestimmungen

## God Nodes (most connected - your core abstractions)
1. `Workflow-Modultabelle (35 Module)` - 42 edges
2. `Kostenlose KI-Potenzialanalyse` - 36 edges
3. `Automatisierte Workflows` - 35 edges
4. `Prozessautomatisierung` - 33 edges
5. `Dokumenten-, Daten- und Abgleichsysteme` - 33 edges
6. `KI-Agenten` - 30 edges
7. `ROI-Guide für KI-Automatisierung` - 28 edges
8. `Querschnitts-Use-Case: Dokumentenverarbeitung & Formularerfassung` - 23 edges
9. `ROI-Formel für KI-Projekte` - 23 edges
10. `Deep-Potenzialanalyse (kostenpflichtige Stufe)` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Prinzip: Bestehende Systeme einbeziehen` --semantically_similar_to--> `Nutzen: Weniger Insellösungen`  [INFERRED] [semantically similar]
  index.html → detail_warum-nurovelle.html
- `Schritt: Daten prüfen` --semantically_similar_to--> `Modul 3: Datenprüfung`  [INFERRED] [semantically similar]
  index.html → potenzialanalyse-deep.html
- `Schritt: Umsetzung planen` --semantically_similar_to--> `Modul 5: Anwendungsfallentwicklung`  [INFERRED] [semantically similar]
  index.html → potenzialanalyse-deep.html
- `Prüffeld Automatisierungspotenzial` --semantically_similar_to--> `Prüfdimension Potenzial`  [INFERRED] [semantically similar]
  index.html → analyse.html
- `ROI-/Automatisierungspotenzial-Rechner` --semantically_similar_to--> `ROI-Überschlag je Prozess`  [INFERRED] [semantically similar]
  index.html → potenzialanalyse-deep.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Gestufter Analyse-Funnel: Rechner, Checkliste, kostenlose Ersteinschätzung, Deep-Potenzialanalyse** — index_roi_rechner, index_checkliste_ki_potenziale, analyse_ki_potenzialanalyse, potenzialanalyse_deep_deep_potenzialanalyse, analyse_abgrenzung, index_deep_verweis [EXTRACTED 1.00]
- **Durchgängiges Prinzip: Prozess vor Technologie** — index_prozesse_zuerst, index_machbarkeit_vor_entwicklung, detail_warum_nurovelle_technologie_folgt_aufgabe, detail_warum_nurovelle_nicht_nur_ki, analyse_definition, index_prozess_zur_loesung, detail_warum_nurovelle_projektablauf [INFERRED 0.85]
- **Standardisiertes Paketangebot mit eigener Serverhoheit** — index_automationspakete, index_betreuungspaket, index_handwerkspaket, index_bueropaket, index_eigener_server, index_servicevertrag, index_einfuehrungspreis [EXTRACTED 1.00]
- **Einheitliches Paket-Geschaeftsmodell der drei Branchenpakete** — paket_betreuung_betreuungspaket, paket_buero_bueropaket, paket_handwerk_handwerkspaket, paket_betreuung_servicevertrag, paket_buero_folgepaket_rabatt, paket_handwerk_preis_799_einrichtung [INFERRED 0.85]
- **Prinzip: Das System erfindet nichts, es belegt oder meldet Fehlen** — paket_buero_kein_erfinden_von_antworten, paket_buero_stichwort_klassifikation, paket_handwerk_keine_erfundenen_stunden, paket_handwerk_artikelstamm, paket_betreuung_menschliche_bestaetigung, paket_betreuung_warnbegriffe [INFERRED 0.85]
- **Datensouveraenitaet: eigene EU-Instanz je Kunde statt Anbieter-Cloud** — paket_betreuung_eigene_instanz_eu_server, paket_buero_eigene_instanz_eu_server, paket_handwerk_eigene_instanz_eu_server, paket_betreuung_lokale_spracherkennung, paket_handwerk_lokale_spracherkennung, paket_betreuung_avv_vorlage [INFERRED 0.95]
- **Gemeinsames Modulmuster: Auslöser → Erfassung → Prüfung → Entscheidung → Aktion → Übergabe → Dokumentation** — detail_prozessautomatisierung_modul_ausloeser, detail_prozessautomatisierung_modul_pruefung, detail_prozessautomatisierung_modul_entscheidung, detail_prozessautomatisierung_modul_systemaktion, detail_prozessautomatisierung_modul_uebergabe, detail_prozessautomatisierung_modul_dokumentation, detail_workflows_modul_ausloeser, detail_workflows_modul_validierung, detail_workflows_modul_entscheidung, detail_workflows_modul_systemaktion, detail_workflows_modul_freigabe, detail_workflows_modul_reporting, detail_ki_agenten_modul_eingang, detail_ki_agenten_modul_pruefung, detail_ki_agenten_modul_aktion, detail_ki_agenten_modul_uebergabe, detail_ki_agenten_modul_dokumentation, detail_datenabgleich_modul_eingang, detail_datenabgleich_modul_validierung, detail_datenabgleich_modul_abgleich, detail_datenabgleich_modul_uebergabe, detail_datenabgleich_modul_dokumentation, graphify_out_converted_workflow_module_table_18fd4ddf_modul_automatisierung, graphify_out_converted_workflow_module_table_18fd4ddf_modul_validierung, graphify_out_converted_workflow_module_table_18fd4ddf_modul_entscheidung, graphify_out_converted_workflow_module_table_18fd4ddf_modul_freigabe [INFERRED 0.85]
- **Menschliche Kontrolle als fester Kontrollpunkt in allen Automationsformen** — detail_prozessautomatisierung_klare_entscheidungsgrundlage, detail_ki_agenten_kontrollpunkte, detail_workflows_freigaben_und_kontrolle, detail_datenabgleich_menschliche_pruefung, graphify_out_converted_workflow_module_table_18fd4ddf_modul_freigabe, detail_ki_agenten_berechtigungen, detail_automationen_dsgvo_konforme_verarbeitung [INFERRED 0.85]
- **Beleg- und Rechnungsverarbeitung über alle Seiten hinweg** — detail_automationen_rechnungs_und_belegleser, detail_datenabgleich_dokumentenverarbeitung, detail_datenabgleich_rechnungspruefung, detail_datenabgleich_modul_extraktion, detail_workflows_rechnungsverarbeitung, detail_prozessautomatisierung_rechnungsverarbeitung, graphify_out_converted_workflow_module_table_18fd4ddf_modul_datenextraktion, graphify_out_converted_workflow_module_table_18fd4ddf_modul_erp [INFERRED 0.85]
- **Konversationelle KI-Schicht (Dialog, Prompting, Governance)** — detail_chatbots_ki_chatbots, detail_sprachassistenten_ki_sprachassistenten, detail_prompt_engineering_prompt_system, detail_ki_sicherheit_ki_governance, detail_ki_software_ki_assistenten [INFERRED 0.85]
- **Muster der kontrollierten Uebergabe an Menschen** — detail_chatbots_uebergabe, detail_sprachassistenten_uebergabe, detail_ki_sicherheit_eskalation, detail_prompt_engineering_fehlerfaelle, detail_ki_software_prozessmodule [INFERRED 0.85]
- **Gemeinsame Freigabe- und Zugriffskontrollschicht** — detail_ki_sicherheit_datenfreigabe, detail_ki_sicherheit_zugriffssteuerung, detail_ki_software_sicherheit_und_rollen, detail_ki_software_mcp_integration, detail_sprachassistenten_sicherheits_und_zugriffskonzept, detail_chatbots_freigegebene_wissensquellen [INFERRED 0.85]
- **Neun strukturparallele Branchenseiten aus einem Template** — detailseiten_branchen_bildung_forschung_branchenseite, detailseiten_branchen_dienstleistungen_kmu_branchenseite, detailseiten_branchen_energie_versorgung_branchenseite, detailseiten_branchen_finanzen_versicherung_branchenseite, detailseiten_branchen_gesundheitswesen_pflege_branchenseite, detailseiten_branchen_immobilien_facility_management_branchenseite, detailseiten_branchen_industrie_produktion_branchenseite, detailseiten_branchen_sonstiges_branchenseite, detailseiten_branchen_verwaltung_vertrieb_einkauf_marketing_branchenseite, detailseiten_branchen_sonstiges_branchenseiten_template [EXTRACTED 1.00]
- **Branchenübergreifender Dokumenten-Use-Case** — detailseiten_branchen_gesundheitswesen_pflege_dokumentenverarbeitung, detailseiten_branchen_gesundheitswesen_pflege_schwerpunkt_dokumentation, detailseiten_branchen_finanzen_versicherung_schwerpunkt_antraege, detailseiten_branchen_finanzen_versicherung_schwerpunkt_belege, detailseiten_branchen_immobilien_facility_management_schwerpunkt_vertraege, detailseiten_branchen_verwaltung_vertrieb_einkauf_marketing_schwerpunkt_freigaben, detailseiten_branchen_dienstleistungen_kmu_schwerpunkt_e_mails, detailseiten_branchen_bildung_forschung_schwerpunkt_inhalte [INFERRED 0.85]
- **Anlagen-, Wartungs- und Betriebsdaten-Querschnitt (Energie, Industrie, Immobilien)** — detailseiten_branchen_industrie_produktion_wartungsplanung, detailseiten_branchen_industrie_produktion_betriebsdatenauswertung, detailseiten_branchen_energie_versorgung_schwerpunkt_wartung, detailseiten_branchen_industrie_produktion_schwerpunkt_wartung, detailseiten_branchen_immobilien_facility_management_schwerpunkt_wartung, detailseiten_branchen_energie_versorgung_schwerpunkt_verbrauch, detailseiten_branchen_industrie_produktion_schwerpunkt_maschinen, detailseiten_branchen_immobilien_facility_management_schwerpunkt_objekte [INFERRED 0.85]
- **Kanon der Unverbindlichkeit der kostenlosen KI-Potenzialanalyse** — agb_kostenlose_ki_potenzialanalyse, agb_keine_zahlungspflicht, agb_vertragsschluss, datenschutz_ki_potenzialanalyse, analyse_rechtliche_hinweise_kostenlos_unverbindlich, analyse_rechtliche_hinweise_keine_folgeverpflichtung, analyse_rechtliche_hinweise_gesondertes_angebot [INFERRED 0.95]
- **Wiederholter Haftungs- und Beratungsausschluss über AGB, Datenschutz, Analyse-Hinweise und Impressum** — agb_keine_sonderberatung, datenschutz_keine_sonderberatung, analyse_rechtliche_hinweise_keine_sonderberatung, agb_keine_ergebnisgarantie, datenschutz_keine_ergebnisgarantie, analyse_rechtliche_hinweise_keine_ergebnisgarantie, agb_haftungsbeschraenkung, impressum_haftung_inhalte [INFERRED 0.85]
- **Identischer Anbieter-/Verantwortlichenblock auf allen Rechtsseiten** — agb_anbieter_verantwortlicher, datenschutz_anbieter_verantwortlicher, impressum_anbieter_verantwortlicher, cookie_hinweis_anbieter_verantwortlicher, analyse_rechtliche_hinweise_anbieter_verantwortlicher, impressum_anbieterkennzeichnung_ddg, datenschutz_hetzner_online [EXTRACTED 1.00]
- **ROI-Berechnungsmethode des Guides** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_roi_formel, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_amortisationszeit, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_monatlicher_nettonutzen, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_einmalige_kosten, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_laufende_kosten, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_interner_stundensatz, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_baseline_messung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_prozesskosten [EXTRACTED 1.00]
- **Ablauf vom Selbsttest zur ROI-Messung** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_plan_90_tage, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_ki_potenzial_selbsttest, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_baseline_messung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_pilotprozess, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_quick_wins, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_parallelbetrieb, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_go_no_go_entscheidung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_skalierung_nach_pilot [EXTRACTED 1.00]
- **Nutzendimensionen jenseits reiner Kosteneinsparung** — assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_produktivitaetsgewinn, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_opportunitaetskosten, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_skaleneffekte, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_fehlerkosten, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_risikoreduzierung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_datenqualitaet, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_umsatzwirkung, assets_downloads_roi_guide_ki_automatisierung_nurovelle_formatvorlagen_final_indirekte_einsparungen [EXTRACTED 1.00]
- **Downloadstrecke: Potenzial-Check, Case Study und Prompt-Guide** — assets_downloads_checkliste_ki_potenzial_check, assets_downloads_case_study_ki_automatisierung_nurovelle_final_case_study_ki_automatisierung, assets_downloads_prompt_guide_prompt_guide, assets_downloads_checkliste_ki_potenzialanalyse [INFERRED 0.85]
- **ROI-Bewertungskette: messen, rechnen, pilotieren, entscheiden** — assets_downloads_checkliste_bearbeitungszeiten_nicht_gemessen, assets_downloads_checkliste_roi_potenziale, assets_downloads_case_study_ki_automatisierung_nurovelle_final_einsparpotenzial, assets_downloads_case_study_ki_automatisierung_nurovelle_final_roi_amortisation, assets_downloads_case_study_ki_automatisierung_nurovelle_final_einfuehrungsschritte [INFERRED 0.85]
- **Qualitätssicherung KI-gestützter Ausgaben** — assets_downloads_case_study_ki_automatisierung_nurovelle_final_menschliche_pruefung, assets_downloads_case_study_ki_automatisierung_nurovelle_final_plausibilitaetsregeln, assets_downloads_case_study_ki_automatisierung_nurovelle_final_fallback_prozess, assets_downloads_case_study_ki_automatisierung_nurovelle_final_datencheck, assets_downloads_prompt_guide_prompt_qualitaet [INFERRED 0.75]

## Communities (38 total, 1 thin omitted)

### Community 0 - "Branchenseiten & Querschnitts-Use-Cases"
Cohesion: 0.08
Nodes (88): Branchenseite: Bildung & Forschung, Kernnutzen Bildung & Forschung: Bereitet Lerninhalte, Projektdaten, Wissen und Verwaltung strukturiert auf., Schwerpunkt Daten (Bildung & Forschung), Schwerpunkt Inhalte (Bildung & Forschung), Schwerpunkt Projekte (Bildung & Forschung), Schwerpunkt Verwaltung (Bildung & Forschung), Schwerpunkt Wissen (Bildung & Forschung), Querschnitts-Use-Case: Wissens- & Inhaltsstrukturierung (+80 more)

### Community 1 - "Case Study, Checkliste & Einführung"
Cohesion: 0.06
Nodes (74): Höhere Abschlussquote, Case Study KI-Automatisierung, Datencheck vor Projektstart, DATEV-API-Anbindung, DSGVO-Prüfung, AVV und Hosting, 30-Tage-Fahrplan (Einführungsschritte), Einsparpotenzial, Gemeinsame Erfolgsfaktoren der Automatisierung (+66 more)

### Community 2 - "AGB, Datenschutz & rechtliche Grenzen"
Cohesion: 0.05
Nodes (73): Anbieter / Verantwortlicher (AGB-Kopfblock), Allgemeine Geschäftsbedingungen (Dokument), Verbot der Übermittlung von Geschäftsgeheimnissen und Drittdaten ohne Berechtigung, Newsletter-Anmeldeformular im Footer, Geltungsbereich der AGB, Haftungsbeschränkung für kostenlose Ersteinschätzungen, Keine Zusicherung technischer, wirtschaftlicher oder organisatorischer Umsetzbarkeit, Kein Rechts-, Steuer-, Finanz-, Anlage-, Versicherungs- oder Unternehmensberatungsverhältnis (+65 more)

### Community 3 - "ROI-Berechnung & Wirtschaftlichkeit"
Cohesion: 0.15
Nodes (55): Amortisationszeit (Payback in Monaten), Angebotsbearbeitung, Assistenzmodell: KI bereitet vor, Mensch prüft, Automatisierungspotenzial eines Prozesses, Baseline-Messung vor Projektstart, Beispielrechnung: 192 % ROI im ersten Jahr, Beispielrechnung: technischer Dienstleister, Datenpflege und Dublettenbereinigung (+47 more)

### Community 4 - "Positionierung & Leistungsüberblick"
Cohesion: 0.13
Nodes (32): Typische Einsatzbereiche und mögliche Folgeprojekte, Nutzen: Passende Technologie nach Aufgabe und Nutzen, Prinzip: Technologie folgt der Aufgabe, Verbindung von Prozessanalyse, Softwareentwicklung und KI-Technologie, Warum Nurovelle: Technik mit Systemverständnis, Nutzen: Weniger Insellösungen, Agents: autonome Workflows, API System-Integration (+24 more)

### Community 5 - "Einführungsprinzipien der Automatisierung"
Cohesion: 0.13
Nodes (28): Entlastung von Fachkräften, KI-Automationen – 25 intelligente Helfer, Zeitintensive manuelle Erfassung, Medienbrüche zwischen Kanälen und Systemen, Schrittweise Einführung (2–3 Automationen zuerst), Nachträgliche Erweiterbarkeit des Prüfsystems, KI nur bei unstrukturierten Inhalten, Agent ersetzt keine Mitarbeitenden (+20 more)

### Community 6 - "Workflow-Module & Aufgabensteuerung"
Cohesion: 0.13
Nodes (26): Bessere Transparenz durch Protokolle, Krankmelde-Assistent, §45b-Budgetmonitor, Datenqualität und wiederkehrende Prüfungen, Modul: Aktualisierung, Modul: Dokumentation, Modul: Übergabe, Anwendung: Aufgabensteuerung (+18 more)

### Community 7 - "Wissenszugriff & Systemintegration"
Cohesion: 0.14
Nodes (26): Antworterstellung, Strukturierte Datenerfassung und Lead-Erfassung, Freigegebene Wissensquellen, Systemintegration des Chatbots, Definierte Themenbereiche und Grenzen, Wissenszugriff auf freigegebene Inhalte, Compliance-Anforderungen, Datenfreigabe und Schutzklassen (+18 more)

### Community 8 - "KI-Agenten für Kundenservice & Assistenz"
Cohesion: 0.16
Nodes (24): Angehörigen-Information bei Verspätung, Angehörigen-Informations-Agent, E-Mail- und Chat-Sortierung, Google-Bewertungssystem, Gruppe Marketing & Kommunikation, Interner Betriebsassistent, 24/7-Telefonassistent, Anwendung: Interne Assistenz (+16 more)

### Community 9 - "Datenquellen & CRM/ERP-Abgleich"
Cohesion: 0.15
Nodes (24): Material- und Verbrauchsprotokoll, Standardisierte Schnittstellen (API, E-Mail, Messenger, CRM, ERP), Anwendung: CRM- und ERP-Abgleich, Anwendung: Datenmigration, Datenquellen: Dokumente, Tabellen, Formulare, E-Mails, Stammdaten, Systemdaten, Anwendung: Stammdatenpflege, Anwendung: CRM- und ERP-Prozesse, Einsatzrahmen: Aufgaben, Daten, Systeme, Regeln, Berechtigungen, Kontrolle (+16 more)

### Community 10 - "Deep-Potenzialanalyse & Kontakt"
Cohesion: 0.18
Nodes (20): Abgrenzung: Was die kostenlose Analyse nicht ist, Prüfdimension Systeme, Prinzip: Bestehende Systeme einbeziehen, Verweis auf kostenpflichtige Deep-Potenzialanalyse, Unverbindliches Erstgespräch (Calendly), Leistung 02: KI-Roadmap, Kontaktabschnitt Nurovelle, Tino Schneider (Ansprechpartner, Marburg) (+12 more)

### Community 11 - "Download-Bibliothek & Formulare"
Cohesion: 0.16
Nodes (20): Ablauf in vier Schritten, Analyse-Formular (Branche, Größe, Zeitaufwand, Datenlage), Keine automatische Verpflichtung, Case Study KI-Automatisierung, Checkliste KI-Potenziale (5 Bereiche, 50 Prüfpunkte), Download-Bibliothek (3 Dokumente, 1 Tool), Newsletter-Anmeldung, Potenzialanalyse-Formular (Startseite) (+12 more)

### Community 12 - "Dokumentenverarbeitung & Abgleich"
Cohesion: 0.18
Nodes (20): Dokumenten-Onboarding, Medizinischer Dokumentations-Assistent, Rezept- und Medikamenten-Manager, Dokumenten-, Daten- und Abgleichsysteme, Datenabgleich mehrerer Quellen, Datenaufbereitung und Normalisierung, Anwendung: Dokumentenklassifikation, Dokumentenverarbeitung (+12 more)

### Community 13 - "KI-Governance & Roadmap-Handlungsfelder"
Cohesion: 0.22
Nodes (19): KI-Chatbots, Module des Dialogs (Ablaufkette), KI-Governance, Kontrollierter Betriebsrahmen fuer KI, Individuelle KI-Software, Integrierte KI-Assistenten, KI-Integration (Modelle, Agenten, Prompt-Systeme), Anwendungsfall-Definition (+11 more)

### Community 14 - "Automationsgruppen Bau, Büro & Personal"
Cohesion: 0.20
Nodes (18): Abnahme- und Übergabeprotokoll, Angebots-Generator, Gruppe Baustelle – Bauprozesse intelligent gesteuert, Gruppe Betreuung – Dokumentation und Planung, Gruppe Büro – Digitales Verwaltungsteam, Gruppe Personal – Mitarbeiterprozesse, Schlechtwetter- und Terminwarnung, Termin-Erinnerung und Ausfallschutz (+10 more)

### Community 15 - "Paket-Grundstruktur & Zielgruppen"
Cohesion: 0.22
Nodes (18): Ausgangslage: Dokumentation kostet Betreuungszeit, Betreuungspaket, Eine Anmeldung, eine Oberflaeche, eine Datenbank, Keine erfundenen Zahlen, keine Erfolgsversprechen, Getrennte Zugaenge Chef, Leitung, Betreuungskraefte, Zielgruppe Alltagsbegleitung und Seniorenbetreuung, Ausgangslage: Sortieren, nachfassen, nachfragen kostet Zeit, Bueropaket (+10 more)

### Community 16 - "Paket-Module & Eingabekanäle"
Cohesion: 0.17
Nodes (18): Loeschung der Sprachaufnahme nach Bestaetigung, Lokale Spracherkennung auf eigenem Server, Menschliche Bestaetigung jedes Berichts, Modul Betreuungsbericht, Warnbegriffe und Kategorien (selbstgepflegt), WhatsApp-Sprachnachricht als Eingabekanal, Bewertungsprofil-Einrichtung, Wissenstool erfindet keine Antworten (+10 more)

### Community 17 - "Potenzialanalyse: Ablauf & Defizite"
Cohesion: 0.23
Nodes (17): Definition: Was ist eine KI-Potenzialanalyse, Problem: Fehlende Prozessabgrenzung, Kostenlose KI-Potenzialanalyse, Prüfdimension Prozesse, Problem: Technische Abhängigkeiten, Problem: Unklare Anwendungsfälle, Problem: Unzureichende Datenbasis, Ausgangslagen: von der Prozessfrage zur Projektidee (+9 more)

### Community 18 - "Belegerfassung & Berichtserstellung"
Cohesion: 0.21
Nodes (16): Diktier-Assistent für Betreuungsberichte, Leistungsnachweis- und Abtretungserfassung, Rechnungs- und Belegleser, Regiebericht und Nachtrag, Sprachnachricht-zu-Struktur-Verarbeitung, Anwendung: Formularverarbeitung, Modul: Extraktion, Anwendung: Rechnungsprüfung (+8 more)

### Community 19 - "Prüf- und Validierungsmodule"
Cohesion: 0.28
Nodes (15): Dienstplan-Tausch-System, Geringere Fehlerquote, Modul: Aufbereitung, Modul: Validierung, Prüffelder und Prüfkriterien, Modul: Prüfung, Modul: Entscheidung, Modul: Prüfung (+7 more)

### Community 20 - "SEO, Prototyping & Ausgabequalität"
Cohesion: 0.17
Nodes (15): Technische Architektur, Betrieb und schrittweise Erweiterung, Prototyp und MVP, Verbindliches Ausgabeformat, Optimierung nach Fehleranalyse, Test mit realistischen und unvollstaendigen Eingaben, Zielgruppe (Ton und Detailtiefe), Pilotprojekte als erste Umsetzungsstufe (+7 more)

### Community 21 - "Prozessschritte & Prüfdimensionen"
Cohesion: 0.19
Nodes (13): Prüfdimension Daten, Prüfdimension Potenzial, Projektablauf in acht Schritten, Ablauf: Vom Geschäftsprozess zur KI-Lösung (sechs Schritte), Prüffeld Datenlage, Schritt 1: Aufgabe erfassen, Schritt 3: Daten prüfen, Schritt 2: KI-Potenzial bewerten (+5 more)

### Community 22 - "Risikoeinordnung & Kontextstruktur"
Cohesion: 0.18
Nodes (13): Dialoglogik, Bestandsaufnahme der KI-Anwendungen, Risikoeinordnung von KI-Anwendungen, Rollenmodell (Verantwortliche, Pruefer, Freigabestellen), Verbindliche Verantwortlichkeiten, Aufgabenstruktur, Strukturierte Kontextbereitstellung, Rolle (fachliche Perspektive der KI) (+5 more)

### Community 23 - "Analyseergebnis & Priorisierung"
Cohesion: 0.20
Nodes (12): Ergebnis: Ersteinschätzung statt KI-Ideenliste, Erste Priorisierung der Ansatzpunkte, Problem: Fehlende Reihenfolge, Wie es danach weitergeht (vier Wege), Weg: Deep-Potenzialanalyse, Weg: Individuelles KI-Projekt, Prüffeld Nächster Schritt, Executive Summary (+4 more)

### Community 24 - "FAQ & Entscheidungsgrundlagen"
Cohesion: 0.20
Nodes (12): FAQ zur kostenlosen Potenzialanalyse, Weg: Direkt umsetzbare Lösung, Weg: Noch keine Umsetzung, erst Vorarbeiten, FAQ zu Zusammenarbeit und Umsetzung, Nutzen: Klare Entscheidungen vor der Umsetzung, Nicht ausschließlich KI: klassische Automatisierung oder Individualsoftware, Prototyp: kritische Funktionen zuerst begrenzt prüfen, FAQ zu KI-Projekten und Zusammenarbeit (+4 more)

### Community 25 - "Eskalation & Dokumentationspflichten"
Cohesion: 0.21
Nodes (12): Dokumentation von Anfrage und Antwort, Uebergabe an zustaendige Mitarbeitende, Dokumentation von Nutzung, Aenderungen und Vorfaellen, Eskalation kritischer Vorgaenge, Ueberwachung von Nutzung und Abweichungen, Dokumentation von Nutzung und Einsatzgrenzen, Monitoring von Rankings und Conversions, Strukturierte Datenerfassung im Gespraech (+4 more)

### Community 26 - "Leistungsnachweis, Abnahme & Slack-Setup"
Cohesion: 0.27
Nodes (12): Uebergabe an Abrechnungssystem per Datei oder Schnittstelle, Lokale Texterkennung fuer Leistungsnachweise, Modul Leistungsnachweis pruefen, Modul Onboarding-Checkliste, Abnahme ohne Vorbehalt erst ohne offenen Mangel, Modul Abnahme protokollieren, Fertiges PDF-Abnahmeprotokoll, Signierter Webhook an Kunden- oder Abrechnungssystem (+4 more)

### Community 27 - "AVV & Datenschutzkonzepte der Pakete"
Cohesion: 0.30
Nodes (12): AVV-Vorlage, Datenschutzkonzept Betreuungspaket, Nicht-medizinische Abgrenzung, AVV-Vorlage, Datenschutzkonzept Bueropaket, Speicherung fremder E-Mail-Inhalte als Datenschutzrisiko, Modul Posteingang, AVV-Vorlage (+4 more)

### Community 28 - "Freigaben, Berechtigungen & Kontrolle"
Cohesion: 0.29
Nodes (11): DSGVO-konforme Verarbeitung und Verschlüsselung, Urlaubs-Manager, Anonymisierung und Maskierung, Menschliche Prüfung für unklare Fälle, Berechtigungen und begrenzte Datenzugriffe, Begrenzter Handlungsspielraum und Kontrollpunkte, Anwendung: Freigabeworkflows, Klare Entscheidungsgrundlage vor der Automatisierung (+3 more)

### Community 29 - "Datenschutz-Grundsätze & Betriebsmodell"
Cohesion: 0.29
Nodes (10): Datenschutz: Löschung personenbezogener Angaben, anonymisierte Auswertung, Problem: Ungeklärte Risiken (Datenschutz, Informationssicherheit), Grundsätze der Umsetzung (sechs Voraussetzungen), Nutzen: Kontrollierte Umsetzung (begrenzte Zugriffe und Freigaben), Automatisierung nur wo fachlich sinnvoll und kontrollierbar, Pflicht-Einwilligung Datenschutzerklärung, Betrieb auf eigenem Server, keine Fremd-Cloud, Leistung 07: KI-Governance (+2 more)

### Community 30 - "Serverstandort & Einrichtungsleistungen"
Cohesion: 0.42
Nodes (9): Eigene getrennte Instanz auf eigenem EU-Server, Einrichtungsleistungen Betreuungspaket, FAQ Serverstandort Deutschland, Eigene getrennte Instanz auf eigenem EU-Server, Einrichtungsleistungen Bueropaket, FAQ Serverstandort Deutschland, Eigene getrennte Instanz auf eigenem EU-Server, Einrichtungsleistungen Handwerkspaket (+1 more)

### Community 31 - "Preise & Servicevertrag"
Cohesion: 0.42
Nodes (9): Folgepaket-Rabatt 349 EUR und 39 EUR je Monat, Preis 799 EUR Einrichtung, Servicevertrag 69 EUR je Monat, Folgepaket-Rabatt 349 EUR und 39 EUR je Monat, Preis 399 EUR Einrichtung, Servicevertrag 69 EUR je Monat, Folgepaket-Rabatt 349 EUR und 39 EUR je Monat, Preis 799 EUR Einrichtung (+1 more)

### Community 32 - "Frageerkennung & Gesprächskontext"
Cohesion: 0.48
Nodes (7): Frageerkennung (Thema und Absicht), Gespraechskontext, Gezielte Rueckfrage bei fehlenden Angaben, Behandlung von Fehlerfaellen und Unsicherheiten, Suchintention (Information, Problem, Vergleich, Leistung, Lokal, Aktion), Erkennung von Thema, Absicht und Kontext, Gezielte Rueckfrage im Gespraech

### Community 33 - "Beratung, Dashboards & Seitenarchitektur"
Cohesion: 0.33
Nodes (7): Chatbot-Potenzialanalyse, Prozessorientierte Benutzeroberflaeche, Dashboards und Reporting, KI-Beratung, Interne Verlinkung, Seitenarchitektur, Sprachpotenzial-Analyse

### Community 34 - "WhatsApp-Module & Prüffristen"
Cohesion: 0.38
Nodes (7): Meta-Versandgebuehren je WhatsApp-Nachricht, Modul Angehoerige informieren, Modul Verspaetung melden, Meta-Versandgebuehren je WhatsApp-Nachricht, Modul Bewertungen, Sperrliste fuer Bewertungsanfragen, DGUV V3, HU/AU und Leiterpruefung als Prueffristen

### Community 36 - "Rechtsstand & Schlussbestimmungen"
Cohesion: 0.67
Nodes (4): Schlussbestimmungen und deutsches Recht, Stand der AGB: 2026-06-01, Stand des Cookie-Hinweises: 2026-06-01, Stand der Datenschutzerklärung: 16. August 2026

## Ambiguous Edges - Review These
- `Tino Schneider (Ansprechpartner, Marburg)` → `Workshop mit Ihrem Team`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to
- `Automationspakete (drei Pakete à vier Funktionen)` → `Prinzip: Technologie folgt der Aufgabe`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to
- `Newsletter-Anmeldung` → `Praxisleitfaden KI-Automatisierung`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to
- `Datenschutzkonzept Betreuungspaket` → `Klartext-Secrets im Repository als Sicherheitsrisiko`  [AMBIGUOUS]
  slack.md · relation: conceptually_related_to
- `Uebergabe an Abrechnungssystem per Datei oder Schnittstelle` → `Slack Incoming Webhook URL`  [AMBIGUOUS]
  slack.md · relation: conceptually_related_to
- `Meta-Versandgebuehren je WhatsApp-Nachricht` → `Preis 799 EUR Einrichtung`  [AMBIGUOUS]
  paket-betreuung.html · relation: conceptually_related_to
- `Bueropaket` → `Uebernahme aus bestehender Anwendungsfamilie`  [AMBIGUOUS]
  paket-handwerk.html · relation: conceptually_related_to
- `Datenschutzkonzept Bueropaket` → `Klartext-Secrets im Repository als Sicherheitsrisiko`  [AMBIGUOUS]
  slack.md · relation: conceptually_related_to
- `Speicherung fremder E-Mail-Inhalte als Datenschutzrisiko` → `Datenschutzkonzept Handwerkspaket`  [AMBIGUOUS]
  paket-buero.html · relation: conceptually_related_to
- `Signierter Webhook an Kunden- oder Abrechnungssystem` → `Slack Signing Secret und Verification Token`  [AMBIGUOUS]
  slack.md · relation: conceptually_related_to
- `Datenschutzkonzept Handwerkspaket` → `Klartext-Secrets im Repository als Sicherheitsrisiko`  [AMBIGUOUS]
  slack.md · relation: conceptually_related_to
- `KI-Automationen – 25 intelligente Helfer` → `Modul: Prozessoptimierung`  [AMBIGUOUS]
  graphify-out/converted/workflow_module_table_18fd4ddf.md · relation: conceptually_related_to
- `Gruppe Personal – Mitarbeiterprozesse` → `Modul: Management`  [AMBIGUOUS]
  graphify-out/converted/workflow_module_table_18fd4ddf.md · relation: conceptually_related_to
- `Dienstplan-Tausch-System` → `Prüffelder und Prüfkriterien`  [AMBIGUOUS]
  detail_automationen.html · relation: conceptually_related_to
- `§45b-Budgetmonitor` → `Prüffelder und Prüfkriterien`  [AMBIGUOUS]
  detail_automationen.html · relation: conceptually_related_to
- `Google-Bewertungssystem` → `Modul: Trendanalyse`  [AMBIGUOUS]
  detail_automationen.html · relation: conceptually_related_to
- `Google-Bewertungssystem` → `Modul: Bildgenerierung`  [AMBIGUOUS]
  graphify-out/converted/workflow_module_table_18fd4ddf.md · relation: conceptually_related_to
- `Rezept- und Medikamenten-Manager` → `Datenabgleich mehrerer Quellen`  [AMBIGUOUS]
  detail_automationen.html · relation: conceptually_related_to
- `Automatisierte Workflows` → `Grundsatz: Assets bleiben textfrei, Text via CSS/HTML`  [AMBIGUOUS]
  graphify-out/converted/workflow_module_table_18fd4ddf.md · relation: conceptually_related_to
- `KI-Sprachassistenten` → `Lokale Sichtbarkeit`  [AMBIGUOUS]
  detail_seo.html · relation: conceptually_related_to
- `Strukturierte Datenerfassung im Gespraech` → `Ueberwachung von Nutzung und Abweichungen`  [AMBIGUOUS]
  detail_ki-sicherheit.html · relation: conceptually_related_to
- `Rollenmodell (Verantwortliche, Pruefer, Freigabestellen)` → `Rolle (fachliche Perspektive der KI)`  [AMBIGUOUS]
  detail_prompt-engineering.html · relation: semantically_similar_to
- `Handlungsfelder fuer KI und Automatisierung` → `SEO und digitale Sichtbarkeit`  [AMBIGUOUS]
  detail_roadmap.html · relation: conceptually_related_to
- `Schwerpunkt Projekte (Bildung & Forschung)` → `Schwerpunkt Freigaben (Verwaltung, Vertrieb, Einkauf & Marketing)`  [AMBIGUOUS]
  detailseiten/branchen/bildung-forschung.html · relation: semantically_similar_to
- `Schwerpunkt Wissen (Bildung & Forschung)` → `Schwerpunkt Formulare (Gesundheitswesen & Pflege)`  [AMBIGUOUS]
  detailseiten/branchen/bildung-forschung.html · relation: semantically_similar_to
- `Schwerpunkt Büro (Dienstleistungen & KMU)` → `Schwerpunkt Abrechnung (Energie & Versorgung)`  [AMBIGUOUS]
  detailseiten/branchen/energie-versorgung.html · relation: semantically_similar_to
- `Schwerpunkt Termine (Gesundheitswesen & Pflege)` → `Schwerpunkt Tickets (Immobilien & Facility Management)`  [AMBIGUOUS]
  detailseiten/branchen/immobilien-facility-management.html · relation: semantically_similar_to
- `Schwerpunkt Ressourcen (Gesundheitswesen & Pflege)` → `Schwerpunkt Objekte (Immobilien & Facility Management)`  [AMBIGUOUS]
  detailseiten/branchen/gesundheitswesen-pflege.html · relation: semantically_similar_to
- `Schwerpunkt Auslastung (Industrie & Produktion)` → `Schwerpunkt Potenziale (Sonstiges)`  [AMBIGUOUS]
  detailseiten/branchen/sonstiges.html · relation: semantically_similar_to
- `Allgemeine Geschäftsbedingungen (Dokument)` → `Sitemap-Verweis auf https://nurovelle.de/homepage/sitemap.xml`  [AMBIGUOUS]
  robots.txt · relation: conceptually_related_to
- `Anbieter / Verantwortlicher (AGB-Kopfblock)` → `Unausgefüllter Platzhalter [Name / Firma] im Geltungsbereich`  [AMBIGUOUS]
  agb.html · relation: conceptually_related_to
- `Unausgefüllter Platzhalter [Name / Firma] im Geltungsbereich` → `Anbieterkennzeichnung nach § 5 DDG`  [AMBIGUOUS]
  agb.html · relation: conceptually_related_to
- `Stand der AGB: 2026-06-01` → `Stand der Datenschutzerklärung: 16. August 2026`  [AMBIGUOUS]
  datenschutz.html · relation: conceptually_related_to
- `Newsletter-Anmeldeformular im Footer` → `Grundsatz der Datenverarbeitung / Erforderlichkeit`  [AMBIGUOUS]
  agb.html · relation: conceptually_related_to
- `Grundsatz der Datenverarbeitung / Erforderlichkeit` → `Einwilligung und Widerruf für nicht erforderliche Cookies`  [AMBIGUOUS]
  cookie-hinweis.html · relation: conceptually_related_to
- `Erhobene Formulardaten (Name, E-Mail, Unternehmen, Branche, Größe, Website, Telefon, Herausforderung)` → `Einbeziehung öffentlich sichtbarer Informationen (z. B. Website des Anfragenden)`  [AMBIGUOUS]
  analyse-rechtliche-hinweise.html · relation: conceptually_related_to
- `Stand der Datenschutzerklärung: 16. August 2026` → `Stand des Cookie-Hinweises: 2026-06-01`  [AMBIGUOUS]
  datenschutz.html · relation: conceptually_related_to
- `Anbieterkennzeichnung nach § 5 DDG` → `Robots-Meta noindex,follow (Impressum)`  [AMBIGUOUS]
  impressum.html · relation: conceptually_related_to
- `Mittelstand als Zielgruppe` → `KI-Umsetzungsreife (Punkteauswertung)`  [AMBIGUOUS]
  assets/downloads/ROI_GUIDE_KI_AUTOMATISIERUNG_NUROVELLE_Formatvorlagen_FINAL.pdf · relation: conceptually_related_to
- `Amortisationszeit (Payback in Monaten)` → `ROI-Korridore nach Prozessart (Benchmark)`  [AMBIGUOUS]
  assets/downloads/ROI_GUIDE_KI_AUTOMATISIERUNG_NUROVELLE_Formatvorlagen_FINAL.pdf · relation: conceptually_related_to
- `Beispielrechnung: 192 % ROI im ersten Jahr` → `Modellfall 1: Ingenieurbüro für technische Planung`  [AMBIGUOUS]
  assets/downloads/ROI_GUIDE_KI_AUTOMATISIERUNG_NUROVELLE_Formatvorlagen_FINAL.pdf · relation: references
- `Nurovelle` → `Prompt-Guide (Download)`  [AMBIGUOUS]
  assets/downloads/prompt_guide.pdf · relation: references
- `Szenario A: Belegverarbeitung in einer Steuerkanzlei` → `Wissen in einzelnen Köpfen`  [AMBIGUOUS]
  assets/downloads/checkliste.pdf · relation: conceptually_related_to
- `KI-gestützte Mandantenzuordnung` → `Prompt-Qualität`  [AMBIGUOUS]
  assets/downloads/prompt_guide.pdf · relation: conceptually_related_to
- `Checkliste KI-Potenzial-Check` → `Prompt-Guide (Download)`  [AMBIGUOUS]
  assets/downloads/prompt_guide.pdf · relation: conceptually_related_to
- `Prompt-Guide (Download)` → `Prompt-Qualität`  [AMBIGUOUS]
  assets/downloads/prompt_guide.pdf · relation: references

## Knowledge Gaps
- **11 isolated node(s):** `Prozessautomatisierung (Use-Case)`, `Einführungspreis bis 31.12.2026`, `Prompt Engineering (Navigationseintrag)`, `Kategorieanalyse je Bereich`, `Lokale Texterkennung fuer Leistungsnachweise` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Tino Schneider (Ansprechpartner, Marburg)` and `Workshop mit Ihrem Team`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Automationspakete (drei Pakete à vier Funktionen)` and `Prinzip: Technologie folgt der Aufgabe`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Newsletter-Anmeldung` and `Praxisleitfaden KI-Automatisierung`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Datenschutzkonzept Betreuungspaket` and `Klartext-Secrets im Repository als Sicherheitsrisiko`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Uebergabe an Abrechnungssystem per Datei oder Schnittstelle` and `Slack Incoming Webhook URL`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Meta-Versandgebuehren je WhatsApp-Nachricht` and `Preis 799 EUR Einrichtung`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Bueropaket` and `Uebernahme aus bestehender Anwendungsfamilie`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._