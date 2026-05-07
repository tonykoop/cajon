# Build instructions — binary deliverables

Three binary files are not checked in directly because they are generated artifacts:

- `Cajon-Family-Design.xlsx` — parametric workbook (alongside the existing `cajon-design-table.xlsx` reference workbook)
- `Cajon-Family-Capstone.pptx` — capstone slide deck
- `Cajon-Family-Print-Packet.pdf` — printable shop packet

The source-of-truth is in the markdown/CSV files. The generator scripts in `scripts/` produce the binaries on demand.

## Run

From the repo root:

```bash
pip install openpyxl python-pptx reportlab
python scripts/build_all.py
```

This produces all three files in the repo root. To regenerate just one, run the corresponding script directly:

```bash
python scripts/build_xlsx.py     # Cajon-Family-Design.xlsx
python scripts/build_pptx.py     # Cajon-Family-Capstone.pptx
python scripts/build_pdf.py      # Cajon-Family-Print-Packet.pdf
```

## Why generated, not committed?

- The xlsx workbook uses real Excel formulas; the canonical state is the formula graph (encoded by the script), not the cached values.
- Regenerating after editing the source CSVs (BOM, sourcing, validation) is a one-command refresh.
- The scripts double as the design table's documentation: anyone reading `build_xlsx.py` can see exactly which formulas drive which cells.

## Editing the design

To change a dimension, formula, or BOM line:

1. Edit the source — `design.md`, `bom.csv`, `sourcing.csv`, `validation.csv`, etc.
2. Run `python scripts/build_all.py` to regenerate the binaries.
3. Commit both the source change and the regenerated binaries.

## Existing reference workbook

`cajon-design-table.xlsx` is the original artisan-style workbook (in-repo). It contains the family table, BOM, build method, and the Wolfram notebook spec. The new generated `Cajon-Family-Design.xlsx` complements it by ingesting the canonical CSVs and providing the corrected Helmholtz formula. The two coexist; the artisan workbook is the human reference, the generated workbook is the data view.
