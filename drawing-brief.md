# Drawing Brief — Cajón Family

The `drawings/` folder ships dimensioned SVGs for the family. Each SVG follows Heifer Zephyr's standard title block (lower-right) with: drawing name, sheet number, scale, units, project (Cajón Family), date, revision, drafter (Tony Koop). All dimensions in inches unless noted.

Visual authority is tracked in `visual-output-register.csv`. The SVG sheets and
jig templates are review/manufacturing-planning artifacts derived from the
design table and OpenSCAD source; production CNC, panel-thickness, snare-contact,
and strike-response claims still require physical validation.

## Required drawings

| File                              | Sheet | Title                                                | Notes                                       |
|-----------------------------------|-------|------------------------------------------------------|---------------------------------------------|
| `01-family-front-elevation.svg`   | 1/8   | Cajón Family — Front Elevation (C/S/B side-by-side)  | Tapa face dims, sound-hole position, scale  |
| `02-standard-isometric.svg`       | 2/8   | Standard (CJ-S) — Exploded Isometric                  | Six-panel callout; tapa, back, sides, top, bottom + glue blocks |
| `03-back-panel-detail.svg`        | 3/8   | Back Panel — Sound-Hole Position + Snare Mount        | 4.5″ Ø hole, centred L–R, 1/3 H from top    |
| `04-tapa-screw-pattern.svg`       | 4/8   | Tapa Face — Screw Layout + Slap-Zone Margin           | #6 brass every 3″; top 4–5″ unscrewed       |
| `05-finger-joint-detail.svg`      | 5/8   | V1 Finger Joint — Corner Section                      | 3/8″ pin spacing, parametric width          |
| `06-dovetail-detail.svg`          | 6/8   | V2 Half-Blind Dovetail — Corner Section               | 14° pin angle, pin spacing                  |
| `07-snare-mount-detail.svg`       | 7/8   | Snare Option B — Guitar-String Mount Block + Tuner    | 8–12° angled face, contact 1″ below top     |
| `08-cnc-inlay-zone.svg`           | 8/8   | CNC Inlay Zone — Side Panel                            | 70 % active area, 1″ keep-out from edges    |

## Drawing conventions

- **Datums**: bottom outside face = primary horizontal datum (Z = 0); back outside face = secondary; centerline of tapa width = vertical reference.
- **Tolerances**: ±0.020″ default; tighter where called out.
- **Cross-section hatching**: walnut grain at 45° for body wood; light cross-hatch at 90° for plywood (back + tapa).
- **Title block size**: 4″ × 1.5″ at 1:1 scale, lower-right corner.
- **Critical dimensions**: bold, with leader lines pointing to the dimensioned feature.
- **Material callouts**: keyed to `bom.csv` part_id where applicable.

## File status

All eight public-review SVG sheets ship in this root packet. Sheets 02, 06, 07, and 08 are intentionally simplified technical briefs rather than full CAD exports; they identify datums, critical features, fixture logic, and acceptance checks so a CAD operator can redraw them without guessing design intent.
