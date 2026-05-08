# Cajon Family Print Packet

**Root-mode packet:** public-review cajon prototype  
**First build:** CJ-S Standard, V1 finger joint, snare option B  
**Status:** pre-build; measurement fields are pending

## Quick Start

1. Build only the Standard prototype first.
2. Make the square assembly fixture, tapa screw template, and back-panel template before cutting final stock.
3. Mill walnut panels to final thickness and square before joinery.
4. Route any inlay before assembly.
5. Glue the shell square, then mount the tapa with the screw template.
6. Validate tone, buzz, seat load, and finish before calling the packet public-ready.

## Design Summary

The cajon is a six-sided closed box with one thin front plate. The back sound hole creates the Helmholtz cavity response; the tapa creates the plate response; the two couple into the bass voice. The upper tapa corners are intentionally less constrained so the corner strike creates a crisp slap.

| Member | Size | Sound hole | Predicted cavity | Predicted plate |
|---|---:|---:|---:|---:|
| CJ-C Compact | 15 x 11 x 11 in | 4.0 in | 107 Hz | 107 Hz |
| CJ-S Standard | 18 x 12 x 12 in | 4.5 in | 96 Hz | 84 Hz |
| CJ-B Bass | 22 x 14 x 14 in | 5.0 in | 77 Hz | 60 Hz |

## Standard Prototype Critical Dimensions

| Feature | Dimension | Check |
|---|---:|---|
| Outer height | 18.000 in | +/-0.020 in |
| Outer width | 12.000 in | +/-0.020 in |
| Outer depth | 12.000 in | +/-0.020 in |
| Body thickness | 0.750 in | +/-0.005 in |
| Back thickness | 0.500 in | +/-0.005 in |
| Tapa thickness | 3 mm / 0.118 in | reject inconsistent sheets |
| Sound hole | 4.500 in diameter | +/-0.020 in |
| Tapa screws | #6 x 3/4 in brass | 3 in spacing except slap zone |
| Slap zone | upper 4-5 in corners | no screws in active corner zone |

## Build Flow

### 1. Stock and Layout

- Acclimate walnut and birch ply.
- Confirm actual tapa thickness at five points.
- Cut panels oversize, then square and mill to final dimensions.
- Mark centerlines and datum edges before any decorative work.

### 2. Inlay Before Assembly

- Keep inlay at least 1 in away from joint edges.
- Use shallow pockets, 0.080-0.100 in.
- Clamp inserts under a flat caul and flush-sand after cure.
- Do not inlay the tapa.

### 3. Joinery and Shell

- V1: finger joints, first prototype default.
- V2: half-blind dovetail, later showpiece.
- V3: rabbet, fastest baseline.
- V4: miter plus spline, visual showpiece.
- Glue in the square assembly fixture and check diagonals before cure.

### 4. Back Panel and Snare

- Cut and deburr the 4.5 in sound hole.
- Drill tuner holes with the back-panel template.
- Mount the angled snare block so strings contact the inside tapa near the slap zone.

### 5. Tapa Mount

- Use the screw template.
- Drive screws by hand in a diagonal pattern.
- Keep screw pressure even; overtightening changes the plate mode.
- Leave the upper corner slap zones loose.

### 6. Finish

- Tapa: tung oil, no thick film.
- Body: satin oil/poly blend or satin polyurethane.
- Round or soften corners for seating comfort.
- Mask the tapa edge so finish does not bridge the slap gap.

## Validation Sheet

| Test | Result | Initials |
|---|---|---|
| Panel thickness recorded | ____ | ____ |
| Shell diagonals within 1/16 in | ____ | ____ |
| Seat load 250 lb for 1 hour | ____ | ____ |
| Sound-hole diameter verified | ____ | ____ |
| Tapa screw pattern verified | ____ | ____ |
| Helmholtz frequency recorded | ____ Hz | ____ |
| Plate mode recorded | ____ Hz | ____ |
| Slap spectral delta recorded | ____ dB | ____ |
| Snare onset set to medium strike | ____ | ____ |
| No unintended rattles | ____ | ____ |

## Public-Release Checklist

- `validation.csv` contains measured values for CJ-S.
- `validation-report.md` summarizes the measured outcome.
- Site hero and visual BOM images use actual build photos.
- Supplier prices and lead times have been rechecked.
- The workbook and `design.md` agree on Helmholtz end correction.
- Public text credits cajon tradition and avoids novelty claims about the cultural form.

## File Map

Use `README.md` for the public overview, `design.md` for calculations, `assembly-manual.md` for shop sequence, `jig-decision.md` for fixtures, and `validation-report.md` for release status.
