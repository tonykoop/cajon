# Resources and Provenance

This file separates stable design references from time-sensitive supplier information so a public reviewer can see what is engineering input, what is shop preference, and what still needs human verification before purchase.

## Local packet sources

| Source | Role in packet | Notes |
|---|---|---|
| `README.md` | Public overview and file map | Root-mode entry point for outside reviewers. |
| `design.md` | Governing design narrative | Corrected Helmholtz end correction is documented here. |
| `cajon-design-table.xlsx` | Minimal workbook seed | Contains the starting cajon design table; workbook formula revision remains a public-release concern. |
| `Cajon-Family-Design.xlsx` | Generated family workbook | Generated from repo CSVs by `scripts/build_xlsx.py`. |
| `bom.csv`, `sourcing.csv`, `cut-list.csv` | Manufacturing packet tables | Costs and lead times are estimates and must be rechecked before buying. |
| `validation.csv` | Test plan and measured-data landing zone | No physical build data is present yet. |

## Acoustic and construction assumptions

| Topic | Stable basis | Packet treatment |
|---|---|---|
| Cavity resonance | Helmholtz resonator with a circular back port and thin-wall end correction | `L_eff = t_back + 1.7*r`; measured cavity response must confirm. |
| Tapa mode | First-order clamped rectangular plate model | Treated as a coarse estimate because plywood is orthotropic. |
| Cajon slap behavior | Traditional loose upper-corner tapa zone | Top 4-5 in at the upper corners remains unscrewed. |
| Snare behavior | Contact preload between internal wires/strings and tapa | Dialed by ear; validation records onset as a 1-5 subjective scale. |
| Seating load | Static shop validation, not formal furniture certification | 250 lb for 1 hour with post-test inspection. |

## Supplier facts to recheck before purchase

The packet names representative suppliers so the BOM is buildable, but it does not freeze current inventory, price, or shipping terms. Before buying material for a public build, recheck:

- Baltic birch 3 mm and 1/2 in grade, thickness tolerance, sheet flatness, and shipping damage policy.
- Walnut board grade, moisture content, delivered thickness, and actual board-foot waste.
- Solid brass #6 x 3/4 in flathead screws; reject brass-plated steel substitutions.
- Guitar tuner hole diameter and string path geometry against the back-panel template.
- Finish VOC rules and curing conditions in the actual shop.

## Public attribution notes

- The cajon is a widely used Afro-Peruvian / flamenco box drum form. The packet should not imply invention of the cultural instrument.
- The novel contribution here is the reproducible public-review build packet: parametric family sizing, jig decisions, validation gates, and documentation discipline.
- The public site should use actual build photography once available. Placeholder hero blocks are acceptable only before the first prototype exists.

## Measurement tools

| Tool | Why it is listed |
|---|---|
| Calipers | Panel thickness, sound-hole diameter, screw-template verification. |
| Framing square and tape | Shell squareness and diagonal checks. |
| Torque screwdriver | Optional but useful for tapa screw uniformity. |
| REW or equivalent spectrum analyzer | Helmholtz, plate, slap-vs-bass spectral delta, T60. |
| Smartphone tuner | Quick shop check, not final evidence by itself. |
