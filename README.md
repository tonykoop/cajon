# Cajón — Family Design Packet

**Status:** L2 V5 build-packet candidate — pre-build (not a measured or production-ready release yet; see "Current status" below).

**A parametric three-member box-drum family.** The Peruvian / flamenco cajón as a coordinated set of three sizes (Compact / Standard / Bass) in four interchangeable manufacturing variants, with an optional snare lineage.

Part of the [tonykoop/instrument-maker](https://github.com/tonykoop/instrument-maker) catalogue. Heifer Zephyr Instruments — Tony Koop.

---

## What this is

A complete parametric design packet for a coordinated three-member cajón family. The same design sheet drives all three sizes with a shared geometric law; the same shell can be realized through any of four joinery paths and either of three snare options.

| Member        | Outer (H × W × D) | Sound hole | Predicted f_H | Voice |
|---------------|-------------------|------------|---------------|-------|
| Compact (CJ-C)| 15 × 11 × 11 in   | 4.0 in Ø   | ≈ 107 Hz      | bright G♯2/A2 |
| **Standard (CJ-S)** ⭐ | 18 × 12 × 12 in | 4.5 in Ø | ≈ 96 Hz | balanced G2 — first prototype |
| Bass (CJ-B)   | 22 × 14 × 14 in   | 5.0 in Ø   | ≈ 77 Hz       | deep D♯2/E2 |

| ID  | Joint              | Method                              | Notes                                    |
|-----|--------------------|-------------------------------------|------------------------------------------|
| V1 ⭐ | Finger / box joint | Table saw + jig OR CNC parametric   | First-prototype default                  |
| V2  | Half-blind dovetail| CNC                                 | Showpiece, harder fixturing              |
| V3  | Rabbet             | Table saw or router                 | Quick commercial baseline                |
| V4  | Miter + spline     | Table saw + spline jig              | Spline visual ties to inlay              |

| Snare  | Lineage   | Voice                                     |
|--------|-----------|-------------------------------------------|
| A      | Peruvian  | dry, woody, deep "thump"                  |
| B ⭐    | Flamenco  | bright, snappy slap; modern default       |
| C      | Studio    | thicker buzz from snare-drum wires        |

The packet ships acoustic physics, parametric geometry, BOM &middot; sourcing &middot; cut-list &middot; validation, dimensioned drawings, an assembly manual covering all four variants, a red-team risks log, a Wolfram starter notebook, a capstone slide deck, a printable shop packet, and a public build-log site.

## Current authority status

Current status: **pre-build V5 build-packet candidate**. The packet has a
design table, OpenSCAD master, SVG review drawings, CNC/jig notes, print packet,
capstone deck, and explorer, but it is not a measured or production-ready
release yet.

**Blender render scaffolding in place** (Refs #4): `cad/mcp-session-log.md`,
`visual-output-register.csv` render rows, and `images/render-brief.md` are
committed. Actual PNG renders remain `pending_measurement` until a Blender
MCP session runs via Claude Desktop and updates the session log.

Fabrication authority is limited to the named design table, OpenSCAD source,
fixture templates, and reviewed drawing set listed in
`visual-output-register.csv`. Snare response, panel-thickness behavior, joinery
strength, and strike-response claims remain predictions until the Standard
`CJ-S` prototype is built and `validation.csv` contains measured rows.

---

## Governing physics

The cajón's bass voice is the coupling of two systems within a few semitones of each other:

- **Front-plate (1,1) clamped-rectangular bending mode** — the 3 mm Baltic-birch tapa, clamped on all four edges by perimeter screws every 3″, vibrating in a single hump when struck centre.
- **Helmholtz cavity** — the closed walnut box with a 4.5″ back-port hole.

Standard prediction: plate (1,1) ≈ **84 Hz**; cavity ≈ **96 Hz**; perceived bass is the coupled mode of both. Strike centre → bass voice. Strike upper corner → slap zone bends and excites high modes + the snare.

```
f_H = (c / 2π) · √( A / (V · L_eff) )
       L_eff = t_back + 1.7 · (d_hole / 2)
```

The original `cajon-design-table.xlsx` formula used `L_eff = t_back` — missing the 1.7·r end correction. That under-predicted L by ~5–10× and over-predicted f_H by ~3×. Risk **A2** in `risks.md` tracks the correction; `design.md` uses the corrected expression; `cajon-design-table.xlsx` formula update is queued for v2.

For the full derivation, family scaling law, and assumptions, see [`design.md`](design.md).

---

## First prototype

> Build the Standard (CJ-S) in V1 finger-joint with snare option B. Standard is the family's tonal centre; Compact and Bass scale geometrically once Standard's measured tuning lands.

- Estimated material cost: **~$205** (one Standard prototype)
- Estimated build time: **~30 hours over 4 days** with CNC for inlay + joinery
- Default body species: Black walnut · CNC-inlaid sides with maple + yellowheart accents

---

## File map

| File / folder | Purpose |
|---------------|---------|
| [`design.md`](design.md) | Governing physics, family scaling, critical dims, open assumptions |
| [`family-spec.csv`](family-spec.csv) | Three-member sizing law for Compact / Standard / Bass |
| [`cajon-design-table.xlsx`](cajon-design-table.xlsx) | Artisan-style reference workbook (in repo) |
| [`bom.csv`](bom.csv) | Bill of materials, by variant |
| [`sourcing.csv`](sourcing.csv) | Suppliers, lead times, price-volatility flags |
| [`cut-list.csv`](cut-list.csv) | Operation-by-operation cut data |
| [`validation.csv`](validation.csv) | Predicted vs measured tuning + acceptance bands |
| [`validation-report.md`](validation-report.md) | Pre-build validation status, gates, and release checklist |
| [`assembly-manual.md`](assembly-manual.md) | Phase-by-phase build (10 phases × 4 variants × 3 snare options) |
| [`supplier-rfq.md`](supplier-rfq.md) | Q2 2026 batch sourcing summary for prospective suppliers |
| [`drawing-brief.md`](drawing-brief.md) | List of required drawings + conventions |
| [`visual-bom-brief.md`](visual-bom-brief.md) | Visual-BOM photo brief |
| [`photo-shotlist.md`](photo-shotlist.md) | In-shop process photo list |
| [`resources.md`](resources.md) | Provenance, assumptions, and supplier verification notes |
| [`jig-decision.md`](jig-decision.md) | Fixture choices for square assembly, drilling, and repeatability |
| [`risks.md`](risks.md) | Red-team failure-mode walk (17 risks, 5 categories) |
| [`visual-output-register.csv`](visual-output-register.csv) | Visual/CAD authority chain for drawings, templates, generated previews, and image placeholders |
| [`wolfram-starter.wl`](wolfram-starter.wl) | Wolfram package: plate, Helmholtz, two-zone synthesis |
| [`capstone-deck.md`](capstone-deck.md) | Markdown capstone companion for validator and review |
| [`capstone-manifest.json`](capstone-manifest.json) | Capstone file map and public-release concerns |
| [`print-packet.md`](print-packet.md) | Printable shop packet in Markdown |
| [`print-packet.html`](print-packet.html) | Browser-printable shop packet |
| [`drawings/`](drawings/) | Dimensioned SVG drawings (sheets 1–8) |
| [`cad/`](cad/) | OpenSCAD parametric master (`cajon-master.scad`) |
| [`evolution/`](evolution/) | StudioPipeline Stage-0 intake (design intent, master manifest, revisions) |
| [`cnc/`](cnc/) | CNC bit + feed strategies for finger-joint, inlay, sound hole |
| [`jigs/`](jigs/) | Fixture drawings for square assembly and tapa screw layout |
| [`images/`](images/) | Concept/support image placeholders; future real build photos only after prototype evidence exists |
| [`data/`](data/) | Measurement-log landing zone for first-build spectral, load, and fit data |
| [`site/index.html`](site/index.html) | Public build-log site |
| [`scripts/`](scripts/) | Generators for xlsx, pptx, pdf binaries |
| [`BUILD.md`](BUILD.md) | How to regenerate the binary deliverables |
| [`LICENSE`](LICENSE) | CC BY 4.0 |

Generated binaries (run `python scripts/build_all.py`):

- `Cajon-Family-Design.xlsx` — parametric workbook ingesting the CSVs
- `Cajon-Family-Capstone.pptx` — capstone slide deck
- `Cajon-Family-Print-Packet.pdf` — printable shop packet
- `capstone-deck.pptx` and `print-packet.pdf` — validator-compatible root-mode aliases

---

## What's parametric vs measured

| Parametric (formula-driven, edit the workbook to change) | Measured (TBD on first prototype) |
|----------------------------------------------------------|------------------------------------|
| Helmholtz frequency f_H per member                       | Actual f_H of the assembled cavity |
| Plate (1,1) mode estimate per member                     | Actual plate (1,1) of mounted tapa |
| Internal cavity volume                                   | Slap-vs-centre spectral delta      |
| Sound-hole area + L_eff                                  | Snare-buzz onset velocity (subjective) |
| Family table dimensions                                  | Sustain T60 of the bass voice      |
| Joint / bit / feed parameters                            | Tapa screw-torque uniformity       |

---

## Status &amp; roadmap

- **Design v1 — shipped as pre-build V5 candidate.** Governing physics, family scaling, BOM/sourcing/cut-list/validation, drawings, CAD master, CNC notes, jigs, risks, Wolfram starter, build-log site, build scripts, explorer, and authority register.
- **First prototype build — pending.** Standard (CJ-S), V1 finger-joint, snare option B.
- **Tuning calibration — pending first measurement.** Once recorded, the family scaling law gets cross-checked against the data per the empirical-learning loop in the parent `instrument-maker` skill.
- **Drawings v2 — queued.** Current sheets 01–08 are public-review SVGs; next pass should replace simplified sheets with CAD-exported dimension drawings after the first build review.
- **Workbook formula revision — queued.** Replace `L = t_back` with `L_eff = t_back + 1.7·r` in `cajon-design-table.xlsx`.

## Review Evidence

- `git diff --check` is expected to pass for the packet branch.
- `python3 /home/tony/.codex/skills/instrument-maker-v4/scripts/validate_packet.py . --mode root`
  is the root-mode gate before merge review.
- This packet is a pre-build V5 candidate: design, sourcing, cut list,
  drawings, CNC notes, jigs, risks, validation plan, print packet, capstone,
  explorer, and visual authority register are present for human review.
- Empirical/build gates remain deferred until the Standard CJ-S prototype is
  assembled, measured, and logged in `validation.csv`.

---

## License

[CC BY 4.0](LICENSE) — see LICENSE for details.
