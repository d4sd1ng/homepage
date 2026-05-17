#!/usr/bin/env python3
prioritaet
Autonova DSGVO-Checkliste + AVV-Templates
Generiert eine vollstaendige DSGVO-Checkliste und AVV-Vorlagen
fuer das Nurturing Email System.

WICHTIG: Dies ist ein ENTWURF - vor Verwendung von einem
Fachanwalt fuer IT-Recht / Datenschutz pruefen lassen!

Verwendung:
    python dsgvo_checkliste.py [--output-dir ./legal_output]
prioritaet

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, asdict


@dataclass
class ChecklistItem:
    id: str
    kategorie: str
    anforderung: str
    beschreibung: str
    umsetzungs_status: str  # offen, in_bearbeitung, umgesetzt, nicht_zutreffend
    verantwortlicher: str
    nachweis_dokument: str
    frist: str
    prioritaet: str  # hoch, mittel, niedrig
    hinweis: str


class DSGVOCheckliste:
    """DSGVO-Checkliste fuer Autonova Nurturing Email System"""

    def __init__(self):
        self.items: List[ChecklistItem] = []
        self._build_checklist()

    def _build_checklist(self):
        """Erstelle die vollstaendige DSGVO-Checkliste"""

        # =====================================================================
        # 1. Rechtsgrundlagen & Verantwortlichkeit
        # =====================================================================
        kategorie = "1. Rechtsgrundlagen & Verantwortlichkeit"
        self.items.extend([
            ChecklistItem(
                id="1.1", kategorie=kategorie,
                anforderung="Verantwortlicher benennen",
                beschreibung="Name, Anschrift, Kontaktdaten des Verantwortlichen (Autonova) muessen in der Datenschutzerklaerung vollstaendig angegeben werden.",
                umsetzungs_status="offen", verantwortlicher="Geschaeftsfuehrung",
                nachweis_dokument="Datenschutzerklaerung", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 13 Abs. 1a DSGVO"
            prioritaet
            ChecklistItem(
                id="1.2", kategorie=kategorie,
                anforderung="Datenschutzbeauftragter (DSB)",
                beschreibung="Pruefung ob ein Datenschutzbeauftragter bestellt werden muss. Bei Kernnaechtigkeit der Verarbeitung (E-Mail-Adressen, Nutzerprofile) wahrscheinlich erforderlich.",
                umsetzungs_status="offen", verantwortlicher="Geschaeftsfuehrung",
                nachweis_dokument="Bestellung DSB", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 37 DSGVO - bei >20 Mitarbeitern in DS-Kernnaechtigkeit oder umfangreicher Verarbeitung"
            prioritaet
            ChecklistItem(
                id="1.3", kategorie=kategorie,
                anforderung="Verarbeitungsverzeichnis (VVT)",
                beschreibung="Fuehren eines Verzeichnisses aller Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Muss alle Verarbeitungsvorgaenge des E-Mail-Systems enthalten.",
                umsetzungs_status="offen", verantwortlicher="DSB / IT",
                nachweis_dokument="Verarbeitungsverzeichnis.xlsx", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 30 DSGVO - Pflicht fuer alle Unternehmen"
            prioritaet
            ChecklistItem(
                id="1.4", kategorie=kategorie,
                anforderung="Rechtsgrundlagen dokumentieren",
                beschreibung="Fuer jede Datenverarbeitung muss die Rechtsgrundlage dokumentiert sein (Einwilligung, Vertrag, berechtigtes Interesse).",
                umsetzungs_status="offen", verantwortlicher="DSB",
                nachweis_dokument="Rechtsgrundlagen-Matrix", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 6 DSGVO - 6 Rechtsgrundlagen"
            prioritaet
        prioritaet

        # =====================================================================
        # 2. Datenerhebung & Einwilligung (E-Mail-System spezifisch)
        # =====================================================================
        kategorie = "2. Datenerhebung & Einwilligung"
        self.items.extend([
            ChecklistItem(
                id="2.1", kategorie=kategorie,
                anforderung="Double-Opt-In fuer Newsletter",
                beschreibung="Jede Newsletter-Anmeldung muss per Double-Opt-In verifiziert werden. Bestaetigungsmail mit Link, kein vorab-Haken.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung",
                nachweis_dokument="Double-Opt-In Implementierung", frist="Vor Launch",
                prioritaet="hoch", hinweis="BGH-Urteil 2016 - Double-Opt-In ist Standard in DE"
            prioritaet
            ChecklistItem(
                id="2.2", kategorie=kategorie,
                anforderung="Einwilligungserklaerung speichern",
                beschreibung="Jede Einwilligung muss mit Timestamp, IP-Adresse und Text der Einwilligung gespeichert werden. Mind. 3 Jahre Aufbewahrung.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung",
                nachweis_dokument="Einwilligungs-Log-System", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 7 Abs. 1 DSGVO - Nachweispflicht"
            prioritaet
            ChecklistItem(
                id="2.3", kategorie=kategorie,
                anforderung="Granulare Einwilligung",
                beschreibung="Getrennte Einwilligungen fuer: Newsletter, Produkt-Updates, Blog-Nurturing, SaaS-Trial. Keine Pauschal-Einwilligung.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung / UX",
                nachweis_dokument="Anmeldeformular-Mockup", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 7 Abs. 2 DSGVO - Einwilligung muss spezifisch sein"
            prioritaet
            ChecklistItem(
                id="2.4", kategorie=kategorie,
                anforderung="Datenerhebung minimieren",
                beschreibung="Nur Daten erheben die noetig sind: E-Mail (Pflicht), Vorname (optional), Branche (optional). Keine ueberfluessigen Felder.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung / UX",
                nachweis_dokument="Formular-Spezifikation", frist="Vor Launch",
                prioritat="mittel", hinweis="Art. 5 Abs. 1c DSGVO - Datenminimierung"
            prioritaet
            ChecklistItem(
                id="2.5", kategorie=kategorie,
                anforderung="Berechtigtes Interesse dokumentieren",
                beschreibung="Fuer bestehende Kunden (Onboarding-Sequenz, Projekt-Updates) kann berechtigtes Interesse als Rechtsgrundlage dienen. Muss dokumentiert und abgewogen werden.",
                umsetzungs_status="offen", verantwortlicher="DSB / Geschaeftsfuehrung",
                nachweis_dokument="Interessenabwaegungs-Dokument", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 6 Abs. 1f DSGVO + Erwaegungsgrund 47"
            prioritaet
        prioritaet

        # =====================================================================
        # 3. Betroffenenrechte
        # =====================================================================
        kategorie = "3. Betroffenenrechte"
        self.items.extend([
            ChecklistItem(
                id="3.1", kategorie=kategorie,
                anforderung="Unsubscribe-Mechanismus",
                beschreibung="Jede E-Mail muss einen funktionierenden Abmelde-Link enthalten. Ein-Klick-Abmeldung ohne Login. Antwort auf Unsubscribe innerhalb 48h.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung",
                nachweis_dokument="Unsubscribe-Implementierung", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 7 Abs. 3 DSGVO + UWG §7"
            prioritaet
            ChecklistItem(
                id="3.2", kategorie=kategorie,
                anforderung="Auskunftsrecht umsetzen",
                beschreibung="Prozess um auf Auskunftsersuchen (Art. 15) innerhalb von 30 Tagen zu antworten. Alle gespeicherten Daten eines Nutzers zusammenstellen.",
                umsetzungs_status="offen", verantwortlicher="DSB / Support",
                nachweis_dokument="Auskunfts-Prozess-Doku", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 15 DSGVO"
            prioritaet
            ChecklistItem(
                id="3.3", kategorie=kategorie,
                anforderung="Loeschrecht umsetzen",
                beschreibung="Prozess zur Loeschung aller Nutzerdaten auf Anfrage. Inkl. Newsletter-Abonnent, E-Mail-Jobs, Tracking-Daten. Loeschbestaetigung senden.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung / DSB",
                nachweis_dokument="Loesch-Prozess-Doku", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 17 DSGVO"
            prioritaet
            ChecklistItem(
                id="3.4", kategorie=kategorie,
                anforderung="Datenuebertragbarkeit",
                beschreibung="Nutzer koennen ihre Daten in strukturiertem Format (JSON/CSV) exportieren.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung",
                nachweis_dokument="Export-Funktion", frist="Nach Launch",
                prioritat="mittel", hinweis="Art. 20 DSGVO"
            prioritaet
            ChecklistItem(
                id="3.5", kategorie=kategorie,
                anforderung="Widerspruchsrecht",
                beschreibung="Bei Direktwerbung: Widerspruch jederzeit moeglich ohne Begruendung. Bei berechtigtem Interesse: Widerspruch mit Begruendung.",
                umsetzungs_status="offen", verantwortlicher="DSB",
                nachweis_dokument="Widerspruchs-Prozess", frist="Vor Launch",
                prioritaet="hoch", hinweis="Art. 21 DSGVO"
            prioritaet
        prioritaet

        # =====================================================================
        # 4. Technische & Organisatorische Massnahmen (TOMs)
        # =====================================================================
        kategorie = "4. Technische & Organisatorische Massnahmen"
        self.items.extend([
            ChecklistItem(
                id="4.1", kategorie=kategorie,
                anforderung="Verschluesselung in Transit",
                beschreibung="SMTP mit TLS (STARTTLS), HTTPS fuer alle Web-Oberflaechen, WireGuard fuer VPS-GPU-Kommunikation.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="DevOps / IT",
                nachweis_dokument="TLS-Konfiguration", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 32 Abs. 1a DSGVO"
            prioritaet
            ChecklistItem(
                id="4.2", kategorie=kategorie,
                anforderung="Verschluesselung ruhender Daten",
                beschreibung="E-Mail-Adressen und persoenliche Daten verschluesselt speichern (AES-256). Passwort-Hashes mit bcrypt.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung",
                nachweis_dokument="Verschluesselungs-Konzept", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 32 Abs. 1a DSGVO"
            prioritaet
            ChecklistItem(
                id="4.3", kategorie=kategorie,
                anforderung="Zugriffskontrolle",
                beschreibung="Rollenbasierte Zugriffskontrolle (Admin, Marketer, Viewer). JWT-Token mit Ablauf. 2FA fuer Admin-Bereich.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung",
                nachweis_dokument="Auth-Konzept", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 32 Abs. 1b DSGVO"
            prioritaet
            ChecklistItem(
                id="4.4", kategorie=kategorie,
                anforderung="Backup & Disaster Recovery",
                beschreibung="Taegliche Backups der Nutzerdaten. Wiederherstellungszeit <24h. Backup-Verschluesselung. Backup-Protokoll dokumentieren.",
                umsetzungs_status="offen", verantwortlicher="DevOps",
                nachweis_dokument="Backup-Konzept", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 32 Abs. 1c DSGVO"
            prioritaet
            ChecklistItem(
                id="4.5", kategorie=kategorie,
                anforderung="Logging & Monitoring",
                beschreibung="Zugriffslogs fuer Admin-Aktionen. Keine IP-Adressen in Nutzer-Logs (DSGVO). Log-Retention: 30 Tage.",
                umsetzungs_status="offen", verantwortlicher="DevOps",
                nachweis_dokument="Logging-Konzept", frist="Vor Launch",
                prioritaet="mittel", hinweis="Art. 32 Abs. 1d DSGVO"
            prioritaet
            ChecklistItem(
                id="4.6", kategorie=kategorie,
                anforderung="Rate-Limiting & Brute-Force-Schutz",
                beschreibung="SMTP Rate-Limit (100/Min), Login-Versuche beschraenken, Account-Lockout bei 5 Fehlversuchen.",
                umsetzungs_status="in_bearbeitung", verantwortlicher="Entwicklung",
                nachweis_dokument="Rate-Limiter-Config", frist="Vor Launch",
                prioritat="mittel", hinweis="Sicherheitsbest Practice"
            prioritaet
        prioritaet

        # =====================================================================
        # 5. Auftragsverarbeitung (AVV)
        # =====================================================================
        kategorie = "5. Auftragsverarbeitung"
        self.items.extend([
            ChecklistItem(
                id="5.1", kategorie=kategorie,
                anforderung="AVV mit Notion",
                beschreibung="Auftragsverarbeitungsvertrag mit Notion Labs Inc. Notion verarbeitet Kontaktdaten, E-Mail-Inhalte und Scheduling-Daten in US-Cloud.",
                umsetzungs_status="offen", verantwortlicher="DSB / Geschaeftsfuehrung",
                nachweis_dokument="AVV_Notion.pdf", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 28 DSGVO - Notion als Auftragsverarbeiter"
            prioritaet
            ChecklistItem(
                id="5.2", kategorie=kategorie,
                anforderung="AVV mit SMTP-Provider",
                beschreibung="AVV mit dem E-Mail-Versand-Dienstleister (z.B. Mailgun, SendGrid, oder eigener SMTP-Server).",
                umsetzungs_status="offen", verantwortlicher="DSB / Geschaeftsfuehrung",
                nachweis_dokument="AVV_SMTP.pdf", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 28 DSGVO"
            prioritaet
            ChecklistItem(
                id="5.3", kategorie=kategorie,
                anforderung="AVV mit Hosting-Provider",
                beschreibung="AVV mit VPS-Hoster und GPU-Worker-Hoster. Server-Standort dokumentieren (EU bevorzugen).",
                umsetzungs_status="offen", verantwortlicher="DSB / DevOps",
                nachweis_dokument="AVV_Hosting.pdf", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 28 DSGVO"
            prioritaet
            ChecklistItem(
                id="5.4", kategorie=kategorie,
                anforderung="AVV mit Zahlungsabwickler",
                beschreibung="Sobald Zahlungen stattfinden: AVV mit Stripe/PayPal/etc. fuer SaaS-Abrechnung.",
                umsetzungs_status="offen", verantwortlicher="DSB / Geschaeftsfuehrung",
                nachweis_dokument="AVV_Zahlung.pdf", frist="Vor SaaS-Launch",
                prioritat="mittel", hinweis="Art. 28 DSGVO"
            prioritaet
        prioritaet

        # =====================================================================
        # 6. Datenschutz-Folgenabschaetzung (DSFA)
        # =====================================================================
        kategorie = "6. Datenschutz-Folgenabschaetzung"
        self.items.extend([
            ChecklistItem(
                id="6.1", kategorie=kategorie,
                anforderung="DSFA durchfuehren",
                beschreibung="Bei umfangreicher Verarbeitung personenbezogener Daten (E-Mail-Tracking, Nutzerverhalten) kann eine DSFA erforderlich sein. Pruefung durch DSB.",
                umsetzungs_status="offen", verantwortlicher="DSB",
                nachweis_dokument="DSFA_Dokument.pdf", frist="Vor Launch",
                prioritat="mittel", hinweis="Art. 35 DSGVO - bei hohem Risiko"
            prioritaet
            ChecklistItem(
                id="6.2", kategorie=kategorie,
                anforderung="E-Mail-Tracking DSGVO-konform",
                beschreibung="Oeffnungs- und Klick-Tracking nur mit expliziter Einwilligung. Pixel-Tracking muss in Datenschutzerklaerung erwaehnt werden.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung / DSB",
                nachweis_dokument="Tracking-Konzept", frist="Vor Launch",
                prioritat="hoch", hinweis="Oeffnungsrate-Tracking ist personenbezogene Datenverarbeitung"
            prioritaet
        prioritaet

        # =====================================================================
        # 7. Datenpannen & Meldepflicht
        # =====================================================================
        kategorie = "7. Datenpannen & Meldepflicht"
        self.items.extend([
            ChecklistItem(
                id="7.1", kategorie=kategorie,
                anforderung="Meldeprozess Datenpanne",
                beschreibung="Prozess zur Meldung einer Datenpanne an Aufsichtsbehoerde innerhalb 72h. Benachrichtigung der Betroffenen bei hohem Risiko.",
                umsetzungs_status="offen", verantwortlicher="DSB / Geschaeftsfuehrung",
                nachweis_dokument="Datenpannen-Notfallplan", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 33 + 34 DSGVO"
            prioritaet
            ChecklistItem(
                id="7.2", kategorie=kategorie,
                anforderung="Datenpannen-Log",
                beschreibung="Dokumentation aller Sicherheitsverletzungen inkl. Auswirkungen und ergriffener Massnahmen.",
                umsetzungs_status="offen", verantwortlicher="DSB",
                nachweis_dokument="Datenpannen-Log.xlsx", frist="Vor Launch",
                prioritaet="mittel", hinweis="Art. 33 Abs. 5 DSGVO"
            prioritaet
        prioritaet

        # =====================================================================
        # 8. Cookie-Consent & Website
        # =====================================================================
        kategorie = "8. Cookie-Consent & Website"
        self.items.extend([
            ChecklistItem(
                id="8.1", kategorie=kategorie,
                anforderung="Cookie-Banner implementieren",
                beschreibung="Opt-In Cookie-Banner (nicht Opt-Out). Nur technisch notwendige Cookies vor Einwilligung. Granulare Cookie-Steuerung.",
                umsetzungs_status="offen", verantwortlicher="Entwicklung / UX",
                nachweis_dokument="Cookie-Banner-Implementierung", frist="Vor Launch",
                prioritat="hoch", hinweis="TTDSG §25 + ePrivacy-Richtlinie"
            prioritaet
            ChecklistItem(
                id="8.2", kategorie=kategorie,
                anforderung="Cookie-Protokoll fuehren",
                beschreibung="Liste aller Cookies mit Name, Zweck, Dauer, Anbieter. Regelmassig aktualisieren.",
                umsetzungs_status="offen", verantwortlicher="DSB / IT",
                nachweis_dokument="Cookie-Liste.xlsx", frist="Vor Launch",
                prioritat="mittel", hinweis="TTDSG §25 Abs. 2"
            prioritaet
        prioritaet

        # =====================================================================
        # 9. Datenschutzerklaerung
        # =====================================================================
        kategorie = "9. Datenschutzerklaerung"
        self.items.extend([
            ChecklistItem(
                id="9.1", kategorie=kategorie,
                anforderung="Vollstaendige Datenschutzerklaerung",
                beschreibung="Alle Verarbeitungen dokumentieren: Newsletter, E-Mail-Sequenzen, Kontaktverwaltung, Notion-Speicherung, Tracking, Cookies, Drittanbieter.",
                umsetzungs_status="offen", verantwortlicher="DSB / Rechtsanwalt",
                nachweis_dokument="Datenschutzerklaerung.html", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 13 + 14 DSGVO"
            prioritaet
            ChecklistItem(
                id="9.2", kategorie=kategorie,
                anforderung="Datenschutzerklaerung in E-Mail-Fusszeile",
                beschreibung="Kurzer Hinweis auf Datenschutzerklaerung in jeder E-Mail (Link).",
                umsetzungs_status="offen", verantwortlicher="Entwicklung",
                nachweis_dokument="E-Mail-Template", frist="Vor Launch",
                prioritat="mittel", hinweis="Best Practice"
            prioritaet
        prioritaet

        # =====================================================================
        # 10. Internationales (UK, CH, US)
        # =====================================================================
        kategorie = "10. Internationales"
        self.items.extend([
            ChecklistItem(
                id="10.1", kategorie=kategorie,
                anforderung="EU-Standardvertragsklauseln (SCC)",
                beschreibung="Bei Datenuebermittlung an Notion (USA): SCC abschliessen. Transfer Impact Assessment durchfuehren.",
                umsetzungs_status="offen", verantwortlicher="DSB / Rechtsanwalt",
                nachweis_dokument="SCC_Notion.pdf", frist="Vor Launch",
                prioritat="hoch", hinweis="Art. 46 DSGVO + Schrems II"
            prioritaet
            ChecklistItem(
                id="10.2", kategorie=kategorie,
                anforderung="UK-GDPR / CH-DSG beachten",
                beschreibung="Bei UK- oder CH-Kunden: Jeweils geltendes Datenschutzrecht beachten. UK Addendum zu SCC.",
                umsetzungs_status="offen", verantwortlicher="DSB",
                nachweis_dokument="UK_Addendum.pdf", frist="Bei internationaler Expansion",
                prioritat="niedrig", hinweis="UK GDPR + CH DSG"
            prioritaet
        prioritaet

    def to_json(self) -> str:
        return json.dumps([asdict(item) for item in self.items], indent=2, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines = [
            "# DSGVO-Checkliste - Autonova Nurturing Email System",
            prioritaet
            f"**Generiert am:** {datetime.now().strftime('%d.%m.%Y')}",
            prioritaet
            "> **WICHTIG:** Dies ist ein ENTWURF. Vor Verwendung von einem Fachanwalt fuer IT-Recht / Datenschutz pruefen lassen!",
            prioritaet
            f"**Gesamt:** {len(self.items)} Pruefpunkte",
            f"**Offen:** {len([i for i in self.items if i.umsetzungs_status == 'offen'])}",
            f"**In Bearbeitung:** {len([i for i in self.items if i.umsetzungs_status == 'in_bearbeitung'])}",
            f"**Umgesetzt:** {len([i for i in self.items if i.umsetzungs_status == 'umgesetzt'])}",
            prioritaet
            "---",
            prioritaet
        prioritaet

        current_kategorie = ""
        for item in self.items:
            if item.kategorie != current_kategorie:
                current_kategorie = item.kategorie
                lines.append(f"## {current_kategorie}")
                lines.append("")

            status_emoji = {"offen": "🔴", "in_bearbeitung": "🟡", "umgesetzt": "🟢", "nicht_zutreffend": "⚪"}.get(item.umsetzungs_status, "⚪")
            prio_badge = {"hoch": "**HOCH**", "mittel": "*mittel*", "niedrig": "niedrig"}.get(item.prioritaet, item.prioritaet)

            lines.append(f"### {item.id} {status_emoji} {item.anforderung}")
            lines.append(f"**Prioritaet:** {prio_badge} | **Frist:** {item.frist} | **Verantwortlich:** {item.verantwortlicher}")
            lines.append(f"")
            lines.append(f"{item.beschreibung}")
            lines.append(f"")
            lines.append(f"*Nachweis:* {item.nachweis_dokument} | *Hinweis:* {item.hinweis}")
            lines.append("")

        lines.append("---")
        lines.append("")
        lines.append("*Erstellt mit dsgvo_checkliste.py - Autonova Nurturing Email System*")

        return "\n".join(lines)


class AVVTemplate:
    """Auftragsverarbeitungsvertrag-Vorlage"""

    def generate_avv(self, auftragsverarbeiter_name: str,
                     auftragsverarbeiter_anschrift: str,
                     auftragsverarbeiter_land: str = "USA",
                     verarbeitungszweck: str = "E-Mail-Nurturing und Kontaktverwaltung",
                     datenkategorien: str = "E-Mail-Adressen, Namen, Unternehmenszugehoerigkeit, Branchen, Interessen, Nutzerverhalten",
                     betroffenen_kategorien: str = "Kunden, Leads, Newsletter-Abonnenten, Trial-User") -> str:
        prioritaet
        Generiert einen AVV-Entwurf basierend auf den DSGVO-Anforderungen.
        prioritaet

        return f"""AUFTRAGSVERARBEITUNGSVERTRAG (AVV)
nach Art. 28 DSGVO

ENTWURF - VOR VERWENDUNG VON RECHTSANWALT PRUEFEN LASSEN

Vertragsschluss: {datetime.now().strftime('%d.%m.%Y')}

=== VERTRAGSPARTEIEN ===

Auftraggeber:
Autonova [Firmenname eintragen]
[Anschrift eintragen]
[Vertreten durch eintragen]

Auftragsverarbeiter:
{auftragsverarbeiter_name}
{auftragsverarbeiter_anschrift}
{auftragsverarbeiter_land}

=== §1 GEGENSTAND UND DAUER ===

(1) Gegenstand dieses Vertrages ist die Erbringung von Datenverarbeitungsleistungen
    durch den Auftragsverarbeiter fuer den Auftraggeber im Rahmen von:
    {verarbeitungszweck}

(2) Die Vereinbarung gilt fuer die gesamte Dauer der Geschaeftsbeziehung.

=== §2 ART UND UMFANG DER VERARBEITUNG ===

(1) Art der Verarbeitung: Speicherung, Verarbeitung, Uebermittlung personenbezogener Daten
    im Rahmen des E-Mail-Nurturing-Systems

(2) Umfang der Verarbeitung:
    - Datenkategorien: {datenkategorien}
    - Betroffenenkategorien: {betroffenen_kategorien}
    - Verarbeitungstaetigkeiten: Erfassung, Speicherung, Organisation, Auswahl, Verwendung,
      Uebermittlung, Loeschung

(3) Der Auftragsverarbeiter verarbeitet die Daten ausschliesslich im Rahmen der
    Weisungen des Auftraggebers und der gesetzlichen Vorgaben.

=== §3 TECHNISCHE UND ORGANISATORISCHE MASSNAHMEN ===

Der Auftragsverarbeiter gewaehrleistet die Einhaltung der in Art. 32 DSGVO
genannten Massnahmen:

(1) Pseudonymisierung und Verschluesselung:
    - Datenuebertragung verschluesselt (TLS 1.2+)
    - Passworter mit bcrypt-Hash gespeichert
    - E-Mail-Adressen bei Bedarf pseudonymisierbar

(2) Vertraulichkeit:
    - Zugang nur fuer autorisiertes Personal
    - Verschwiegenheitspflicht aller Mitarbeiter
    - Regelmaessige Schulung der Mitarbeiter

(3) Integritaet und Verfuegbarkeit:
    - Redundante Systeme
    - Taegliche Backups
    - Wiederherstellungszeit <24h

(4) Evaluierung:
    - Regelmaessige Sicherheitspruefungen
    - Penetrationstests (jaehrlich)
    - Audit-Logs fuer alle Aenderungen

=== §4 KONTROLlRECHTE DES AUFTRAGGEBERS ===

(1) Der Auftraggeber ist berechtigt, sich von der Einhaltung der Pflichten
    des Auftragsverarbeiters zu ueberzeugen.

(2) Der Auftragsverarbeiter gewaehrt dem Auftraggeber auf Verlangen
    Einsicht in die relevanten Systeme und Dokumente.

=== §5 UNTERAUFTRAGSVERARBEITUNG ===

(1) Eine Unterbeauftragung bedarf der vorherigen Zustimmung des Auftraggebers.

(2) Der Auftragsverarbeiter hat die Unterbeauftragung in gleichem Umfang
    vertraglich abzusichern.

=== §6 LOESCHUNG UND HERAUSGABE ===

(1) Nach Beendigung der Verarbeitung hat der Auftragsverarbeiter die Daten
    unverzueglich zu loeschen oder an den Auftraggeber zurueckzugeben.

(2) Gesetzliche Aufbewahrungsfristen bleiben unberuehrt.

=== §7 MELDUNG VON DATENPANnEN ===

(1) Der Auftragsverarbeiter meldet dem Auftraggeber unverzueglich,
    spaetestens jedoch innerhalb von 24 Stunden nach Kenntnis:
    - Jede Verletzung des Schutzes personenbezogener Daten
    - Jeden Verdacht auf eine solche Verletzung
    - Jede behoerdliche Anfrage oder Massnahme

=== §8 AUFKLAERUNG UND MITWIRKUNG ===

(1) Der Auftragsverarbeiter unterstuetzt den Auftraggeber bei der
    Gewaehrung der Betroffenenrechte (Art. 12-22 DSGVO).

(2) Der Auftragsverarbeiter unterstuetzt bei der Datenschutz-Folgenabschaetzung.

=== §9 SCHLUSSBESTIMMUNGEN ===

(1) Es gilt das Recht der Bundesrepublik Deutschland.

(2) Gerichtsstand ist [eintragen].

(3) Aenderungen dieses Vertrages beduerfen der Schriftform.

(4) Sollten einzelne Bestimmungen unwirksam sein, bleibt der uebrige
    Vertrag davon unberuehrt.

=== UNTERSCHRIFTEN ===

Auftraggeber:                                  Auftragsverarbeiter:

________________________                       ________________________
Ort, Datum                                     Ort, Datum

________________________                       ________________________
Unterschrift                                   Unterschrift

=============================
ANLAGE 1: TECHNISCHE UND ORGANISATORISCHE MASSNAHMEN (TOMs)
=============================

| Nr. | Massnahme                          | Umsetzung beim AV                      |
|-----|-----------------------------------|----------------------------------------|
| 1   | Verschluesselung in Transit        | TLS 1.2+ fuer alle Verbindungen        |
| 2   | Verschluesselung ruhender Daten    | AES-256 fuer gespeicherte Daten        |
| 3   | Zugriffskontrolle                  | Rollenbasiert (RBAC), 2FA fuer Admin   |
| 4   | Eingabekontrolle                   | Audit-Logs fuer alle Aenderungen       |
| 5   | Auftragskontrolle                  | Vertragsbindung, Verschwiegenheit      |
| 6   | Verfuegbarkeitskontrolle           | Redundanz, Backups, Monitoring         |
| 7   | Trennungsgebot                     | Getrennte Mandanten/Tenants            |
| 8   | Loeschkonzept                      | Automatische Loeschung nach Aufbewahrung|
| 9   | Pseudonymisierung                  | Soweit moeglich und zweckmaessig      |
| 10  | Datenminimierung                   | Nur noetige Daten verarbeiten          |

=============================
ANLAGE 2: UNTERAUFTRAGSVERARBEITER
=============================

[Bei Bedarf ergaenzen: Liste aller Unterauftragsverarbeiter
mit Name, Anschrift, Verarbeitungszweck]

=============================
ANLAGE 3: DATENUEBERMITTLUNG IN DRITTLAENDER
=============================

{f"Verarbeitung findet in {auftragsverarbeiter_land} statt." if auftragsverarbeiter_land != "Deutschland" else "Keine Datenuebermittlung in Drittländer."}

Bei Datenuebermittlung in die USA:
- EU-Standardvertragsklauseln (SCC) abgeschlossen: [ ] Ja  [ ] Nein
- Transfer Impact Assessment durchgefuehrt: [ ] Ja  [ ] Nein
- Zusaetzliche Massnahmen: [ ] Ja  [ ] Nein
- Datenschutzshield (falls zutreffend): [ ] Ja  [ ] Nein

prioritaet

    def generate_notion_avv(self) -> str:
        """AVV-Vorlage spezifisch fuer Notion"""
        return self.generate_avv(
            auftragsverarbeiter_name="Notion Labs Inc.",
            auftragsverarbeiter_anschrift="2300 Harrison Street, San Francisco, CA 94110, USA",
            auftragsverarbeiter_land="USA",
            verarbeitungszweck="Speicherung und Verwaltung von Kontaktdaten, E-Mail-Sequenz-Daten, Scheduling-Informationen und Content-Stuecken in Notion-Workspace",
            datenkategorien="E-Mail-Adressen, Namen, Unternehmenszugehoerigkeit, Branchen, Interessen, SaaS-Produkt-Interessen, E-Mail-Sequenz-Daten, Versandzeitpunkte",
            betroffenen_kategorien="Kunden, Leads, Newsletter-Abonnenten, Trial-User, SaaS-Nutzer"
        prioritaet

    def generate_smtp_avv(self) -> str:
        """AVV-Vorlage fuer SMTP-Dienstleister"""
        return self.generate_avv(
            auftragsverarbeiter_name="[SMTP-Provider eintragen]",
            auftragsverarbeiter_anschrift="[Anschrift eintragen]",
            auftragsverarbeiter_land="[Land eintragen]",
            verarbeitungszweck="Versand von E-Mail-Newslettern und Nurturing-Sequenzen an Abonnenten",
            datenkategorien="E-Mail-Adressen, E-Mail-Inhalte, Versandzeitpunkte, Oeffnungsraten, Klickraten",
            betroffenen_kategorien="Newsletter-Abonnenten, Leads, Kunden, Trial-User"
        )


def main():
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "legal_output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # DSGVO-Checkliste generieren
    checkliste = DSGVOCheckliste()

    # Markdown
    md_path = output_dir / "DSGVO_Checkliste_Autonova.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(checkliste.to_markdown())
    print(f"✓ DSGVO-Checkliste: {md_path}")

    # JSON
    json_path = output_dir / "DSGVO_Checkliste_Autonova.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(checkliste.to_json())
    print(f"✓ DSGVO-Checkliste JSON: {json_path}")

    # AVV-Vorlagen generieren
    avv = AVVTemplate()

    # Notion AVV
    notion_avv_path = output_dir / "AVV_Notion_Entwurf.txt"
    with open(notion_avv_path, 'w', encoding='utf-8') as f:
        f.write(avv.generate_notion_avv())
    print(f"✓ AVV Notion: {notion_avv_path}")

    # SMTP AVV
    smtp_avv_path = output_dir / "AVV_SMTP_Entwurf.txt"
    with open(smtp_avv_path, 'w', encoding='utf-8') as f:
        f.write(avv.generate_smtp_avv())
    print(f"✓ AVV SMTP: {smtp_avv_path}")

    # Leere AVV-Vorlage
    blank_avv_path = output_dir / "AVV_Vorlage_Leer.txt"
    with open(blank_avv_path, 'w', encoding='utf-8') as f:
        f.write(avv.generate_avv(
            auftragsverarbeiter_name="[Name eintragen]",
            auftragsverarbeiter_anschrift="[Anschrift eintragen]",
        ))
    print(f"✓ AVV Vorlage leer: {blank_avv_path}")

    print(f"\n{len(checkliste.items)} Pruefpunkte generiert")
    print("WICHTIG: Alle Dokumente sind ENTWUERFE - von Fachanwalt pruefen lassen!")


if __name__ == "__main__":
    main()
