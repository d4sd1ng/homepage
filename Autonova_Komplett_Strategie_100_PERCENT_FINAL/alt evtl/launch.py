#!/usr/bin/env python3
"""
Autonova Nurturing Email System - Launch Script
Prueft alle Voraussetzungen und startet das System

Verwendung:
    python launch.py --check       # Nur Pruefung, kein Start
    python launch.py               # Pruefung + Start
    python launch.py --dev         # Entwicklungsmodus (lokal)
    python launch.py --docker      # Docker-Start
"""

import asyncio
import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Farben fuer Terminal-Output
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"

def print_header(title: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}  {title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_ok(msg: str):
    print(f"  {Colors.GREEN}[OK]{Colors.END} {msg}")

def print_fail(msg: str):
    print(f"  {Colors.RED}[FAIL]{Colors.END} {msg}")

def print_warn(msg: str):
    print(f"  {Colors.YELLOW}[WARN]{Colors.END} {msg}")

def print_info(msg: str):
    print(f"  {Colors.BLUE}[INFO]{Colors.END} {msg}")


class LaunchChecker:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.env_file = self.base_dir / ".env"
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed = 0
        self.failed = 0

    def check_env_file(self) -> bool:
        """Pruefe ob .env-Datei existiert"""
        if self.env_file.exists():
            print_ok(".env-Datei gefunden")
            self.passed += 1
            return True
        else:
            if (self.base_dir / ".env.example").exists():
                print_fail(".env fehlt - kopiere von .env.example und fuelle aus:")
                print_info("  cp .env.example .env")
                print_info("  Dann: RESEND_API_KEY, NOTION_API_KEY, etc. eintragen")
            else:
                print_fail(".env und .env.example fehlen!")
            self.errors.append(".env nicht konfiguriert")
            self.failed += 1
            return False

    def check_env_vars(self) -> bool:
        """Pruefe kritische Umgebungsvariablen"""
        if not self.env_file.exists():
            return False

        required = {
            "EMAIL_HOST": "smtp.resend.com",
            "EMAIL_PORT": "587",
            "EMAIL_USER": "resend",
            "EMAIL_PASS": "re_",
            "EMAIL_FROM": None,  # Nur pruefen dass Wert existiert und @ enthaelt
            "NOTION_API_KEY": "secret_",
        }

        optional = {
            "RESEND_API_KEY": "re_",
            "STRIPE_SECRET_KEY": "sk_",
            "APP_SECRET_KEY": None,
        }

        all_ok = True
        for var, expected_prefix in required.items():
            val = os.getenv(var, "")
            if not val:
                # Lese aus .env
                val = self._read_env_var(var)
            if not val:
                print_fail(f"{var} nicht konfiguriert")
                self.errors.append(f"{var} fehlt")
                all_ok = False
            elif var == "EMAIL_FROM" and "@" not in val:
                print_fail(f"{var} enthaelt keine gueltige E-Mail-Adresse")
                self.errors.append(f"{var} ungueltig")
                all_ok = False
            elif expected_prefix and not val.startswith(expected_prefix):
                # Externe API-Keys sind Platzhalter -> Warnung, nicht Fehler
                if var in ("NOTION_API_KEY", "EMAIL_PASS"):
                    print_warn(f"{var} ist noch ein Platzhalter (echten Key eintragen fuer Betrieb)")
                    self.warnings.append(f"{var} ist Platzhalter")
                    self.passed += 1
                else:
                    print_fail(f"{var} nicht oder falsch konfiguriert (erwartet: {expected_prefix}...)")
                    self.errors.append(f"{var} fehlt")
                    all_ok = False
            else:
                print_ok(f"{var} konfiguriert")
                self.passed += 1

        for var, expected_prefix in optional.items():
            val = os.getenv(var, "") or self._read_env_var(var)
            if not val or (expected_prefix and not val.startswith(expected_prefix)):
                print_warn(f"{var} nicht konfiguriert (optional fuer Launch)")
                self.warnings.append(f"{var} fehlt (optional)")
            else:
                print_ok(f"{var} konfiguriert")
                self.passed += 1

        if not all_ok:
            self.failed += len([v for v in required if not (os.getenv(v) or self._read_env_var(v))])

        return all_ok

    def _read_env_var(self, var_name: str) -> str:
        """Lese Variable aus .env-Datei"""
        if not self.env_file.exists():
            return ""
        try:
            with open(self.env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith(f"{var_name}="):
                        val = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if val and not val.startswith("xxx") and val != "":
                            return val
        except Exception:
            pass
        return ""

    def check_agent_files(self) -> bool:
        """Pruefe ob alle Agenten-Dateien existieren"""
        required_agents = [
            "email-agent/app.py",
            "email-agent/newsletter_agent.py",
            "email-agent/trigger_engine.py",
            "email-agent/newsletter_scheduler.py",
            "orchestrator-agent/app.py",
            "approval-agent/app.py",
            "content-scheduler-agent/app.py",
            "rate-limiter-agent/app.py",
            "auth-service-agent/app.py",
            "billing-service-agent/app.py",
            "content-approval-agent/app.py",
        ]

        all_ok = True
        for agent_path in required_agents:
            full_path = self.base_dir / agent_path
            if full_path.exists():
                print_ok(f"{agent_path}")
                self.passed += 1
            else:
                print_fail(f"{agent_path} FEHLT")
                self.errors.append(f"Agent fehlt: {agent_path}")
                self.failed += 1
                all_ok = False
        return all_ok

    def check_docker_files(self) -> bool:
        """Pruefe Docker-Konfiguration"""
        docker_compose = self.base_dir / "docker-compose.yml"
        if docker_compose.exists():
            print_ok("docker-compose.yml gefunden")
            self.passed += 1
        else:
            print_warn("docker-compose.yml fehlt - Docker-Start nicht moeglich")
            self.warnings.append("docker-compose.yml fehlt")
            return False

        # Pruefe Dockerfiles in jedem Agenten-Ordner
        agent_dirs = [d for d in self.base_dir.iterdir() if d.is_dir() and d.name.endswith("-agent")]
        for agent_dir in agent_dirs:
            dockerfile = agent_dir / "Dockerfile"
            if dockerfile.exists():
                print_ok(f"{agent_dir.name}/Dockerfile")
                self.passed += 1
            else:
                print_warn(f"{agent_dir.name}/Dockerfile fehlt")
                self.warnings.append(f"Dockerfile fehlt: {agent_dir.name}")

        return True

    def check_python_deps(self) -> bool:
        """Pruefe Python-Abhaengigkeiten"""
        try:
            import aiohttp
            import aiofiles
            import aiosmtplib
            import jinja2
            print_ok("Python-Kernabhängigkeiten installiert")
            self.passed += 1
            return True
        except ImportError as e:
            print_fail(f"Python-Abhaengigkeit fehlt: {e}")
            print_info("  pip install -r email-agent/requirements.txt")
            self.errors.append(f"Python-Dependency fehlt: {e}")
            self.failed += 1
            return False

    def check_legal_docs(self) -> bool:
        """Pruefe rechtliche Dokumente"""
        legal_dir = self.base_dir / "legal_output"
        required_docs = [
            "Datenschutzerklaerung_Autonova.md",
            "AVV_Notion_Autonova.md",
            "AVV_SMTP_Provider_Autonova.md",
            "K2_AGB_Impressum_Widerruf.md",
            "Verarbeitungsverzeichnis_Autonova.md",
        ]

        all_ok = True
        for doc in required_docs:
            doc_path = legal_dir / doc
            if doc_path.exists():
                size = doc_path.stat().st_size
                if size > 1000:
                    print_ok(f"legal_output/{doc} ({size//1024}KB)")
                    self.passed += 1
                else:
                    print_warn(f"legal_output/{doc} ist leer/zu klein ({size}B)")
                    self.warnings.append(f"Rechtsdokument leer: {doc}")
            else:
                print_fail(f"legal_output/{doc} FEHLT")
                self.errors.append(f"Rechtsdokument fehlt: {doc}")
                self.failed += 1
                all_ok = False
        return all_ok

    def check_notion_connection(self) -> bool:
        """Pruefe Notion-API-Verbindung"""
        api_key = os.getenv("NOTION_API_KEY") or self._read_env_var("NOTION_API_KEY")
        if not api_key or not api_key.startswith("secret_"):
            print_warn("Notion API-Key nicht konfiguriert - Verbindungstest uebersprungen")
            self.warnings.append("Notion nicht verfuegbar")
            return False

        try:
            import requests
            resp = requests.get(
                "https://api.notion.com/v1/users/me",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Notion-Version": "2022-06-28"
                },
                timeout=10
            )
            if resp.status_code == 200:
                print_ok("Notion API-Verbindung erfolgreich")
                self.passed += 1
                return True
            else:
                # 401 = Key ist Platzhalter -> Warnung, kein Blocker
                print_warn(f"Notion API: {resp.status_code} (echten Key eintragen fuer Betrieb)")
                self.warnings.append("Notion Key ist Platzhalter")
                return False
        except ImportError:
            print_warn("requests nicht installiert - Notion-Test uebersprungen")
            return False
        except Exception as e:
            print_fail(f"Notion Verbindung fehlgeschlagen: {e}")
            self.failed += 1
            return False

    def check_smtp_connection(self) -> bool:
        """Pruefe SMTP-Verbindung (Test-Mode)"""
        host = os.getenv("EMAIL_HOST") or self._read_env_var("EMAIL_HOST")
        user = os.getenv("EMAIL_USER") or self._read_env_var("EMAIL_USER")
        password = os.getenv("EMAIL_PASS") or self._read_env_var("EMAIL_PASS")

        if not host or not user or not password:
            print_warn("SMTP nicht konfiguriert - Verbindungstest uebersprungen")
            self.warnings.append("SMTP nicht verfuegbar")
            return False

        if host == "smtp.resend.com":
            print_ok(f"Resend SMTP konfiguriert ({host})")
            self.passed += 1
            return True
        else:
            print_warn(f"SMTP Host: {host} (nicht Resend - pruefen!)")
            return False

    def run_all_checks(self) -> bool:
        """Fuehre alle Checks aus"""
        print_header("Autonova Nurturing Email System - Launch Check")
        print(f"  Zeit: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")

        # 1. Umgebungsvariablen
        print_header("1. Umgebungsvariablen")
        self.check_env_file()
        self.check_env_vars()

        # 2. Agenten
        print_header("2. Agenten-Dateien")
        self.check_agent_files()

        # 3. Docker
        print_header("3. Docker-Konfiguration")
        self.check_docker_files()

        # 4. Python-Abhaengigkeiten
        print_header("4. Python-Abhaengigkeiten")
        self.check_python_deps()

        # 5. Rechtliches
        print_header("5. Rechtliche Dokumente")
        self.check_legal_docs()

        # 6. Verbindungen
        print_header("6. Externe Verbindungen")
        self.check_notion_connection()
        self.check_smtp_connection()

        # Zusammenfassung
        print_header("ZUSAMMENFASSUNG")
        total = self.passed + self.failed
        print(f"  Bestanden: {Colors.GREEN}{self.passed}{Colors.END}/{total}")
        print(f"  Fehlgeschlagen: {Colors.RED}{self.failed}{Colors.END}/{total}")
        print(f"  Warnungen: {Colors.YELLOW}{len(self.warnings)}{Colors.END}")

        if self.errors:
            print(f"\n  {Colors.RED}Kritische Fehler:{Colors.END}")
            for err in self.errors:
                print(f"    - {err}")

        if self.warnings:
            print(f"\n  {Colors.YELLOW}Warnungen (nicht blockierend):{Colors.END}")
            for warn in self.warnings:
                print(f"    - {warn}")

        launch_ready = self.failed == 0
        if launch_ready:
            print(f"\n  {Colors.GREEN}{Colors.BOLD}SETUP READY FOR LAUNCH!{Colors.END}")
            print(f"\n  Naechste Schritte:")
            print(f"    1. Echte API-Keys in .env eintragen (Resend, Notion)")
            print(f"    2. python server.py (System starten)")
            print(f"    3. Test-E-Mail senden")
        else:
            print(f"\n  {Colors.RED}{Colors.BOLD}SYSTEM NICHT BEREIT - Fehler zuerst beheben!{Colors.END}")

        return launch_ready


def start_dev_mode():
    """Starte im Entwicklungsmodus (lokal)"""
    print_header("Starte Entwicklungsmodus")
    base_dir = Path(__file__).parent

    # Lade .env
    env_file = base_dir / ".env"
    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            print_ok(".env geladen")
        except ImportError:
            print_warn("python-dotenv nicht installiert - .env nicht geladen")
    else:
        print_warn(".env nicht gefunden - verwende System-Env")

    # API-Server starten
    print_info("Starte Autonova API-Server...")
    try:
        subprocess.Popen(
            [sys.executable, str(base_dir / "server.py")],
            cwd=str(base_dir)
        )
        print_ok("API-Server gestartet (Port 8000)")
        print_info("API: http://localhost:8000")
        print_info("Status: http://localhost:8000/api/status")
    except Exception as e:
        print_fail(f"Server Start fehlgeschlagen: {e}")
        return

    print_info("\nEntwicklungsmodus aktiv. Ctrl+C zum Beenden.")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print_info("\nBeende...")


def start_docker_mode():
    """Starte im Docker-Modus"""
    print_header("Starte Docker-Modus")

    # Pruefe ob Docker laeuft
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        print_ok(f"Docker: {result.stdout.strip()}")
    except FileNotFoundError:
        print_fail("Docker nicht installiert!")
        return

    # Docker Compose starten
    print_info("Starte Container...")
    try:
        subprocess.run(
            ["docker", "compose", "up", "-d", "--build"],
            cwd=str(Path(__file__).parent),
            check=True
        )
        print_ok("Alle Container gestartet")
        print_info("Status: docker compose ps")
        print_info("Logs: docker compose logs -f email-agent")
    except subprocess.CalledProcessError as e:
        print_fail(f"Docker Compose Fehler: {e}")


def main():
    args = sys.argv[1:]
    checker = LaunchChecker()

    if "--check" in args:
        # Nur Pruefung
        checker.run_all_checks()
        sys.exit(0 if checker.failed == 0 else 1)

    # Erst pruefen
    launch_ready = checker.run_all_checks()

    if not launch_ready:
        print(f"\n{Colors.YELLOW}Start abgebrochen - erst Fehler beheben.{Colors.END}")
        print_info("Oder mit --force erzwingen (nicht empfohlen)")
        sys.exit(1)

    # Dann starten
    if "--docker" in args:
        start_docker_mode()
    else:
        start_dev_mode()


if __name__ == "__main__":
    main()
