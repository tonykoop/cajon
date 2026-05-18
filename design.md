# Cajón Family — Parametric Design Sheet

**Owner:** Tony Koop · Heifer Zephyr Instruments
**Family:** Box drum, six-sided closed box, single thin front plate (tapa), back-port Helmholtz, optional internal snare
**Members:** Compact (CJ-C), Standard (CJ-S, prototype), Bass (CJ-B) — coordinated three-size family
**Manufacturing variants:** four end-to-end paths (V1 finger-joint / V2 dovetail / V3 rabbet / V4 miter+spline) — each with a snare/no-snare option
**Status:** Design v1 — workbook formulas parametric; family tuning predictions populated; first prototype is Standard with finger-joint shell + guitar-string snare; tuning calibration pending first measurement.

---

## Authority boundary

This packet is a pre-build V5 build-packet candidate. The design table,
OpenSCAD master, jig templates, and reviewed SVG sheets are the current planning
authority. They are not a substitute for measured panel stock, CNC test cuts,
seat-load tests, strike-response captures, or snare-onset measurements.

Generated previews, site imagery, visual-BOM layouts, and future concept images
are support artifacts only. The packet records visual and CAD authority in
`visual-output-register.csv`; no image or preview should be used to infer panel
thickness, snare contact geometry, screw positions, joinery tolerances, or CNC
toolpaths.

## 1. Intent

Document the cajón as a portfolio-grade parametric instrument, not as one box. The same design sheet drives three sizes (Compact / Standard / Bass) with a single shared geometric law, and the same shell can be realized through four joinery paths and either lineage of snare:

| Lineage   | Snare                          | Character                                   |
|-----------|--------------------------------|---------------------------------------------|
| Peruvian  | None (or finger-mute pad)      | Dry, woody, deep "thump"; tonal pitch reads cleanly |
| Flamenco  | Guitar strings (adjustable)    | Bright, snappy slap on edges; modern default       |

A fifth artifact — the existing CNC inlay workflow (Broinwood-derived) — is the visual signature: walnut body with maple/yellowheart inlay panels, with the inlay routed before assembly so the pockets are clamped flat.

The cajón's "secret" is that two simultaneous resonators tune together: the Helmholtz cavity (`f_H`) sits within a few semitones of the tapa (1,1) plate mode, and the player perceives the *coupled* note as the bass voice. Designing the family is therefore a matter of co-tuning those two systems while keeping snare-buzz, slap-zone geometry, and seat-height ergonomics inside their own envelopes.

---

## 2. Family scaling law

The cajón family is a *closed-box, single-thin-plate, back-ported Helmholtz* drum. Two governing modes are co-dominant in the bass voice: the front-plate (1,1) bending mode and the cavity Helmholtz mode. Both must be modeled; the perceived bass pitch is the lower of the two if they are well separated, or a coupled hybrid if they are within ~6 semitones.

### 2.1 Tapa front plate — clamped rectangular plate, (1,1) mode

For an orthotropic plywood plate clamped on all four edges (the cajón seats the tapa under screws every ~3″ around the perimeter; the central span is the active region), the (1,1) bending-mode fundamental is approximated by the isotropic clamped-plate expression:

```
f_plate_(1,1) ≈ (π / 2) · (1/a² + 1/b²) · √( D / (ρ · h) )
```

where `a, b` are the clear span (in metres), `h` is plate thickness, `ρ` is panel density, and `D = E·h³ / (12·(1−ν²))` is flexural rigidity.

For a 3 mm Baltic-birch tapa (`E ≈ 8 GPa`, `ρ ≈ 680 kg/m³`, `ν ≈ 0.30`), this places the (1,1) mode in the 60–110 Hz band over the family — which is exactly where you want it for "thump on the centre, snap on the edge."

### 2.2 Cavity — Helmholtz back-port

For the box cavity coupled to a circular back-port:

```
f_H = (c / 2π) · √( A / (V · L_eff) )
       L_eff = t_back + 1.7 · (d_hole / 2)
```

where `V` is internal volume, `A = π·(d/2)²` is the port area, `t_back` is back-panel thickness, and `1.7·r` is the standard end-correction for a thin-wall flush orifice (both sides counted).

The original spreadsheet (`cajon-design-table.xlsx`) used `L_eff = t_back` only. That under-predicts L by ~5–10× for typical cajón dimensions and over-predicts `f_H` by a factor of ~3. The corrected formula is what the workbook uses now; the historical predictions are flagged in `risks.md` as **A4**.

### 2.3 Family scaling

Volume scales roughly with H·W·D, so `f_H ∝ 1/√V` for a constant port. To keep `f_H` proportional to a target pitch span across the family, the port diameter is also scaled — larger box ⇒ larger port to push `f_H` back up; smaller box ⇒ smaller port. The catalog defaults below split the family into a P1 / P2 / P3 voice each separated by ~3–4 semitones.

| Member        | H (in) | W (in) | D (in) | Body t (in) | Back t (in) | Port d (in) | Tapa t (mm) | Predicted f_H (Hz) | Predicted plate (1,1) (Hz) | Tonal voice |
|---------------|--------|--------|--------|-------------|-------------|-------------|-------------|--------------------|-----------------------------|-------------|
| Compact (CJ-C)| 15     | 11     | 11     | 0.625       | 0.50        | 4.0         | 3           | 107                | 107                         | bright A2/G♯2 |
| **Standard (CJ-S) ⭐** | 18 | 12 | 12 | 0.75        | 0.50        | 4.5         | 3           | **96**             | **84**                      | balanced G2 |
| Bass (CJ-B)   | 22     | 14     | 14     | 0.75        | 0.50        | 5.0         | 3           | 77                 | 60                          | deep D♯2/E2 |

All values from the parametric design sheet; the workbook is the source of truth for any update.

The Compact accidentally lands with `f_H ≈ f_plate` — that's the "tightly coupled" regime and produces the punchiest, most pitch-distinct bass in the family. The Bass deliberately separates them by ~5 semitones so the cavity rumble dominates; the plate then acts mainly as the slap voice.

---

## 3. Snare strategy

The cajón has three valid snare paths. The workbook supports all three; the first prototype runs **option B**:

| ID | Snare                        | Mechanism                                                                                       | Use                              |
|----|------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------|
| A  | None (Peruvian)              | bare cavity; finger pad or palm mute on outside if a softer, more melodic voice is wanted        | trad / world percussion          |
| B  | Guitar-string snare ⭐        | 3–4 wound or plain steel guitar strings clamped on an angled internal block; tension adjustable via guitar tuners | flamenco / modern default        |
| C  | Snare-drum wires             | a section of standard snare-drum wires mounted on a tension lever; thicker buzz, less articulate | studio / loud genres             |

Snare wires sit *behind* the tapa, lightly contacting the inside face. The contact force is the tunable: too light = no buzz; too heavy = chokes the slap and overhangs the bass.

---

## 4. Joinery / construction variants

The shell is a six-sided box. Five of the six faces (top, bottom, two sides, back) are 3/4″ Black Walnut by default; the sixth face is the 3 mm Baltic birch tapa. The four major joinery paths each ship as a manufacturable option:

| ID | Joint                  | Method                              | Strength | Visual                                | Difficulty | Notes |
|----|------------------------|-------------------------------------|----------|---------------------------------------|------------|-------|
| V1 | Finger / box joint ⭐  | table saw + jig OR CNC parametric   | ★★★      | ★★★ — contrasting maple fingers possible | medium     | First-prototype default; CNC route enables variable-width fingers |
| V2 | Half-blind dovetail    | CNC                                 | ★★★      | ★★★ — heirloom                          | hard       | Showpiece path; needs jig fixtures + dust collection             |
| V3 | Rabbet                 | table saw or router                 | ★★       | ★ — hidden                              | easy       | Commercial baseline; quickest to build                            |
| V4 | Miter + spline         | table saw + spline jig              | ★★★      | ★★★ — contrasting splines visible       | medium     | Clean show-up corners; spline inlay ties to the inlay aesthetic   |

V1 (finger joint) is the recommended first prototype: it tolerates ±0.005″ panel error gracefully, the jig is reusable, and the visible joint complements the inlay.

The tolerance claim is a design target, not a measured result. Validate it with
scrap finger-joint samples and the square assembly jig before cutting show
stock.

---

## 5. CNC inlay strategy

The cajón's six flat faces are a perfect canvas for the Broinwood-style ball-nose inlay technique. Critical rule: **route inlay before assembly.** Once the box is glued, you cannot clamp panels flat for routing.

The workflow ships in detail on `cajon-design-table.xlsx` § "CNC Inlay Workflow". Summary:

1. Two paired toolpaths per inlay element: a *pocket* (negative) cut into the body panel and an *insert* (positive) cut from contrasting wood. Both use the same TBN 12.4° tapered-ball-nose bit.
2. Pocket depth 0.080–0.100″; feed 30 IPM at 18,000 RPM in walnut. Test-cut on scrap to dial allowance.
3. The inlay-allowance setting in VCarve Pro controls press-fit. Too tight cracks the insert; too loose leaves a visible gap line.
4. Glue with Titebond III, clamp flat with wax-paper underlay, cure 24 hours, then drum-sand the panel flush before joinery.

Visual layout default for the prototype:
- **Side panels (2):** geometric mandala or Celtic-knot pattern, ~70% of panel area
- **Back panel:** rosette around the sound hole only
- **Top (seat):** subtle border inlay; nothing raised (you sit on it)
- **Tapa:** no inlay (active surface, you hit it; preserve plate uniformity)

---

## 6. Critical dimensions (Standard, V1 finger-joint, snare option B)

These are the numbers that drive cut-list, drawings, and CNC. Anything not here is either derived in the workbook or a non-critical aesthetic choice.

| Feature                          | Dimension          | Tolerance      | Source                         |
|----------------------------------|--------------------|----------------|--------------------------------|
| Outer height                     | 18.000″            | ±0.020″        | family table                   |
| Outer width                      | 12.000″            | ±0.020″        | family table                   |
| Outer depth                      | 12.000″            | ±0.020″        | family table                   |
| Body panel thickness             | 0.750″             | ±0.005″        | stock spec                     |
| Tapa thickness                   | 0.118″ (3 mm)      | +0/−0.005″     | Baltic birch ply spec          |
| Back panel thickness             | 0.500″             | ±0.005″        | stock spec                     |
| Sound-hole diameter              | 4.500″             | ±0.020″        | family table                   |
| Sound-hole position              | centred L–R, 1/3 H from top on back panel | ±0.10″ | trad practice                  |
| Tapa screw spacing               | every 3″           | ±0.10″         | trad practice                  |
| Slap-zone unscrewed margin       | top 4–5″ of tapa, both upper corners | as drawn | trad practice                  |
| Internal corner glue blocks      | 8× ¾″ triangle, full panel height | hand-fit | rigidity / overtone control    |
| Snare angle (option B)           | 8–12° off vertical, contact 1″ below top | ±2° | trad practice                  |
| Rubber-foot height               | 0.50″              | ±0.05″         | airflow + bass projection      |

Datums for drawings: bottom outside face = primary horizontal datum (Z = 0); back outside face = secondary; centerline of tapa width = vertical reference.

---

## 7. What's parametric vs. what's measured

**Parametric (formula-driven, edit the workbook to change):**
- Helmholtz frequency `f_H` per member
- Plate (1,1) mode estimate per member
- Internal cavity volume
- Sound-hole area and effective neck length
- Family table member dimensions
- Joint / bit / feed parameter recommendations

**Measured (TBD on first prototype, will populate `validation.csv`):**
- Actual `f_H` of the assembled cavity (tap-and-record, expect ±10 Hz from prediction)
- Actual plate (1,1) of the mounted tapa (varies with screw torque and tapa moisture)
- Slap-zone vs centre-strike spectrum delta (`risks.md` E1 acceptance test)
- Snare-buzz onset velocity (subjective; recorded per snare option)
- Sustain T60 of the bass voice
- Actual panel thickness after milling, tapa thickness after finish, and any
  local thinning from CNC inlay pockets
- Finger-joint fit, glue-line closure, diagonal squareness, and seat-load
  behavior

A second-pass design sheet revision happens after the first prototype is measured. The empirical correction (`f_H_predicted` vs `f_H_measured`) gets logged in `validation.csv`, and any cents-error >50 cents triggers a family-table revisit.

---

## 8. Open assumptions

These are explicit so the reviewer knows what is *concept* vs *manufacturable*:

1. **Tapa material is treated as isotropic.** Real Baltic birch ply is mildly orthotropic; the (1,1) prediction is a coarse estimate — expect ±20% from the simple formula. A measured tapa will be the source of truth.
2. **Snare contact pressure is not yet a parameter** in the workbook. It is dialed by ear on the first prototype.
3. **Glue-block contribution to plate clamping is unmodeled.** The 8 internal glue blocks effectively change the plate boundary condition near the corners; we treat the full panel as clamped, which over-stiffens the model slightly.
4. **CNC inlay pocket depth has not been verified to leave structural panel above the pocket.** 0.080″ pocket in 0.625″ stock leaves 0.545″ — comfortably safe — but is recorded as a check in `risks.md` (S2).
5. **Panel material defaulted to Black Walnut** for the visual contrast story; the workbook supports any species but the BOM and cost numbers assume walnut.

---

## 9. First-prototype recommendation

Build the **Standard (CJ-S), V1 finger-joint, snare option B** as the first instrument. Reasons:

- Standard is the family's tonal centre; if its measured tuning lands on prediction, the Compact and Bass scale by simple geometry from there.
- V1 finger-joint is forgiving on stock-prep error and uses the same CNC fixture as future variants.
- Snare option B (guitar strings) is the modern default; the snare can be removed or detensioned to demo "Peruvian style" without rebuilding the box.

Total estimated material cost for prototype: ~$200 (see `bom.csv`). Estimated build time, in-shop, with CNC for joinery and inlay: ~30 hours over 4 days (acclimate / mill / inlay / joinery / glue-up / sand / finish / mount / tune).

---

## 10. References

- `cajon-design-table.xlsx` — workbook source of truth (all formulas live)
- `bom.csv` — bill of materials, all variants
- `sourcing.csv` — suppliers, lead times, price-volatility flags
- `cut-list.csv` — operation-by-operation lumber and stock cuts
- `validation.csv` — predicted vs measured tuning + acceptance bands
- `assembly-manual.md` — phase-by-phase build procedure
- `risks.md` — red-team acoustic / structural / ergonomic / supply / fit-finish failure modes
- `wolfram-starter.wl` — Wolfram package: plate, Helmholtz, two-zone synthesis
- `drawing-brief.md` — list of required drawings + conventions
- `drawings/*.svg` — dimensioned drawings
- `cad/` — SolidWorks placeholders (master layout to follow)
- `cnc/` — CNC inlay and finger-joint cut strategy notes
- `site/index.html` — public build-log site
