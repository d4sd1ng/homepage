# Grow Controller C3 – 12-V-Platine: Stückliste und Anschlussplan R1

Stand: 27.11.2026. Referenz-Layout: `c3_12v_5signals_1fan_WIP_NOT_FOR_ORDER.kicad_pcb`.
Dieses Dokument beschreibt die **aktuell im KiCad-Layout vorhandenen 54 Footprints**; es stellt keine Zusicherung der Belastbarkeit oder eine vollständige elektrische Serienfreigabe dar.

## Funktionsumfang der Platine

- **J1:** einziger 12-V-Eingang über DC-Hohlbuchse, internes 12-V-Lastnetz und Step-down für die C3-Versorgung.
- **J2–J6:** fünf reine GPIO-Steuersignal-Paare. Je **Pin 1 = GND, Pin 2 = GPIO**. Die GPIO-Ausgänge sind Logiksignale und **keine 12-V-Ausgänge**.
- **J7–J12:** sechs einzeln schaltbare 12-V-Motoranschlüsse mit einem N-MOSFET je Kanal.
- **J13:** gemeinsamer 12-V-Lüfteranschluss, **Pin 1 = geschaltetes GND, Pin 2 = +12 V, Pin 3 = TACH / bewusst nicht beschaltet**.
- **JP1:** abziehbare Brücke im 5-V-Servicepfad zum ESP32-C3. Keine automatische Trennung bei gleichzeitigem USB-/DC-Betrieb.

### Stückliste – bestückte Bauteile

| Referenzen | Anzahl | Bauteil / vorgesehener Wert | Bauform / Hinweis |
|---|---:|---|---|
| U_C3 | 1 | ESP32-C3 SuperMini | 2×8-Pin-Modul, steckbar; reale Modulrevision abgleichen |
| C3-Buchsenleisten | 2 | 1×8, 2,54-mm-Buchsenleiste | passend zum konkret gewählten Modul |
| U_PCA | 1 | PCA9685PW, 16-Kanal PWM/I²C | TSSOP-28; Datenblattbezeichnung vor Einkauf abgleichen |
| U_BUCK | 1 | RECOM R-78E5.0-1.0, 12 V→5 V / 1 A | SIP-3; tatsächliches Modul und extern benötigte Kondensatoren prüfen |
| D1 | 1 | 1N5819 | DO-41; Kathodenmarkierung beachten |
| J1 | 1 | Same Sky PJ-037AH | DC-Hohlbuchse, 2 Kontakte, linke Platinenkante, Langlochabstand 6,3 mm |
| J2–J12 | 11 | Phoenix Contact 1757242 | MSTBA 2,5/2-G-5,08, 2-polige PCB-Klemmen |
| Gegenstücke J2–J12 | 11 | Phoenix Contact 1757019 | MSTB 2,5/2-ST-5,08, steckbar |
| J13 | 1 | Phoenix Contact 1757255 | MSTBA 2,5/3-G-5,08, 3-polig |
| Gegenstück J13 | 1 | Phoenix Contact 1757022 | MSTB 2,5/3-ST-5,08 |
| JP1 | 1 | Stiftleiste 1×2 + Kurzschlussbrücke | 2,54 mm |
| QM1–QM6, QFAN | 7 | AO3400A, N-MOSFET, logic-level | SOT-23 |
| RG1–RG6, RGFAN | 7 | 100 Ω | 0805, Gate-Serienwiderstände |
| RPD1–RPD6, RPDFAN | 7 | 100 kΩ | 0805, Gate-Pulldowns |
| DM1–DM6, DFAN | 7 | SS34 | SMA/DO-214AC, Schottky |
| R_SDA, R_SCL | 2 | 4,7 kΩ | 0805, I²C-Pull-up |
| R_OE | 1 | 10 kΩ | 0805, PCA-Ausgangssperre |
| C_PCA | 1 | 100 nF | 0805, PCA-Abblockkondensator |

**Externe Spannungsquelle (separat):** Mean Well GST60A12-P1J, 12 V / 5 A, 60 W, Hohlstecker als Kandidat. Steckerpaarung, Polung und Anlaufstromreserve sind noch am Original zu bestätigen.

### Platinen- und Fertigungsdaten

- Maße: **160 × 116 mm** (vorhandene Kontur).
- **2 Kupferlagen** (F.Cu/B.Cu), **1,6 mm** im PCB-Layout eingestellt.
- **H1–H4:** vier nichtmetallisierte M3-Montagebohrungen mit 3,2 mm Durchmesser; deren Gehäusepositionen sind vorläufig.
- J13-Pin 3 ist als Tacho-Reserve **absichtlich ohne Netz**. Keine Verbindung auf der PCB vorhanden.
- Die bestehende Leiterplatte hat derzeit **keine bestätigte Eingangsicherung** und **keine nachgewiesene automatische USB-Stromquellenumschaltung**.
- Die Strom- und Thermikbilanz einschließlich Motorblockier- und Lüfteranlaufströmen ist offen.

Die Stückliste ist eine **CAD-abgeleitete Bestückungsliste**, nicht die Bestätigung, dass alle Teile im Betrieb bereits verifiziert sind.
