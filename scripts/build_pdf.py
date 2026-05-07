"""
Build Cajon-Family-Print-Packet.pdf — printable shop packet.
Run: python build_pdf.py
Requires: pip install reportlab
"""
from pathlib import Path
import csv

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Cajon-Family-Print-Packet.pdf"


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("CoverTitle", fontName="Helvetica-Bold", fontSize=28,
                         leading=32, textColor=colors.HexColor("#2b2417"),
                         alignment=1, spaceAfter=12))
    s.add(ParagraphStyle("CoverSub", fontName="Helvetica-Oblique", fontSize=13,
                         leading=18, textColor=colors.HexColor("#6b4f2c"),
                         alignment=1, spaceAfter=24))
    s.add(ParagraphStyle("H1Custom", fontName="Helvetica-Bold", fontSize=18,
                         leading=22, textColor=colors.HexColor("#2b2417"),
                         spaceAfter=10, spaceBefore=14))
    s.add(ParagraphStyle("H2Custom", fontName="Helvetica-Bold", fontSize=14,
                         leading=18, textColor=colors.HexColor("#5b3a1c"),
                         spaceAfter=8, spaceBefore=12))
    s.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=11,
                         leading=15, textColor=colors.HexColor("#2b2417"),
                         spaceAfter=8))
    return s


def cover(s):
    return [
        Spacer(1, 1.2 * inch),
        Paragraph("CAJÓN FAMILY", s["CoverTitle"]),
        Paragraph("Printable Shop Packet — v1", s["CoverSub"]),
        Spacer(1, 0.3 * inch),
        Paragraph("Heifer Zephyr Instruments — Tony Koop", s["Body"]),
        Paragraph("Three-member family · four manufacturing variants · optional snare", s["Body"]),
        Paragraph("First prototype: Standard (CJ-S), V1 finger-joint, snare option B", s["Body"]),
        PageBreak(),
    ]


def file_map(s):
    rows = [
        ["File", "Purpose"],
        ["design.md", "Governing physics, family scaling, critical dims, open assumptions"],
        ["bom.csv", "Bill of materials by variant"],
        ["sourcing.csv", "Suppliers, lead times, prices"],
        ["cut-list.csv", "Operation-by-operation cut data"],
        ["validation.csv", "Predicted vs measured tuning + acceptance bands"],
        ["assembly-manual.md", "Phase-by-phase build procedure"],
        ["risks.md", "Red-team failure modes (5 categories)"],
        ["wolfram-starter.wl", "Plate, Helmholtz, two-zone synthesis"],
        ["drawings/*.svg", "Dimensioned drawings"],
        ["cad/cajon-master.scad", "OpenSCAD parametric body"],
        ["cnc/", "CNC bit + feed strategies"],
    ]
    t = Table(rows, colWidths=[2.0 * inch, 4.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F4ECDB")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#C8B89E")),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#C8B89E")),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [
        Paragraph("File map", s["H1Custom"]),
        t,
    ]


def family_table(s):
    rows = [
        ["Member", "H × W × D", "Hole Ø", "Predicted f_H", "Voice"],
        ["Compact (CJ-C)", "15 × 11 × 11 in", "4.0 in", "≈ 107 Hz", "bright G♯2/A2"],
        ["Standard (CJ-S) ⭐", "18 × 12 × 12 in", "4.5 in", "≈ 96 Hz", "balanced G2"],
        ["Bass (CJ-B)", "22 × 14 × 14 in", "5.0 in", "≈ 77 Hz", "deep D♯2/E2"],
    ]
    t = Table(rows, colWidths=[1.6 * inch, 1.6 * inch, 0.9 * inch, 1.2 * inch, 1.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F4ECDB")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#C8B89E")),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#C8B89E")),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
    ]))
    return [
        Paragraph("Family table", s["H1Custom"]),
        t,
    ]


def design_summary(s):
    return [
        Paragraph("Governing physics", s["H1Custom"]),
        Paragraph(
            "The cajón's bass voice is the coupling of two systems within a few semitones: "
            "the front-plate (1,1) clamped-rectangular bending mode (the tapa) and the Helmholtz cavity "
            "with the back-port sound hole. The Standard's predicted plate (1,1) is ~84 Hz; "
            "the cavity is ~96 Hz; the perceived bass is the coupled mode of both.",
            s["Body"]),
        Paragraph("Helmholtz: f_H = (c/2π)·√(A/(V·L_eff)),  L_eff = t_back + 1.7·(d_hole/2)", s["Body"]),
        Paragraph(
            "The 1.7·r end correction was absent from the original spreadsheet formula; "
            "the corrected expression is what the workbook should now use. "
            "(Risk A2 in risks.md tracks this.)",
            s["Body"]),
    ]


def csv_table(s, name, title, max_rows=20):
    src = ROOT / name
    if not src.exists():
        return [Paragraph(f"({name} not found)", s["Body"])]
    with open(src, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    rows = rows[: max_rows + 1]
    t = Table(rows, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F4ECDB")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#C8B89E")),
        ("INNERGRID", (0, 0), (-1, -1), 0.2, colors.HexColor("#C8B89E")),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Paragraph(title, s["H1Custom"]), t, PageBreak()]


def main():
    s = styles()
    doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                            leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.6 * inch)
    story = []
    story.extend(cover(s))
    story.extend(file_map(s))
    story.append(PageBreak())
    story.extend(family_table(s))
    story.extend(design_summary(s))
    story.append(PageBreak())
    story.extend(csv_table(s, "bom.csv", "BOM (excerpt)"))
    story.extend(csv_table(s, "sourcing.csv", "Sourcing"))
    story.extend(csv_table(s, "cut-list.csv", "Cut List"))
    story.extend(csv_table(s, "validation.csv", "Validation"))
    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
