"""
Build all binary deliverables for the cajón packet.
Run: python scripts/build_all.py
Requires: pip install openpyxl python-pptx reportlab
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SCRIPTS = ["build_xlsx.py", "build_pptx.py", "build_pdf.py"]


def main():
    for s in SCRIPTS:
        path = ROOT / s
        print(f"--- Running {s} ---")
        try:
            subprocess.run([sys.executable, str(path)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"  {s} failed: {e}")


if __name__ == "__main__":
    main()
