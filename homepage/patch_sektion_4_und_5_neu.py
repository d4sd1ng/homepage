#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

scripts = (
    ROOT / "patch_sektion_4_neu.py",
    ROOT / "patch_sektion_5_neu.py",
)

for script in scripts:
    result = subprocess.run([sys.executable, str(script)], text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

print("FERTIG: Sektion 4 und Sektion 5 wurden in der richtigen Reihenfolge gepatcht.")
