# Risks — Cajón Family

Red-team pass over the design. Each risk has a category, severity, mitigation, and an attached verification test that goes into `validation.csv` once the prototype exists.

## Acoustic

### A1 — Helmholtz / plate frequency miss-match produces dead bass
**Severity:** medium
**Description:** The Standard's plate (1,1) is predicted at ~84 Hz and `f_H` at ~96 Hz — close enough to couple but not so close that they fight. If the actual tapa thickness, stiffness, or moisture content shifts the plate by ±20 %, the family table needs adjustment.
**Mitigation:** treat 84 Hz / 96 Hz as predictions, not specifications. Measure both modes on the assembled prototype before declaring tuning. Update `validation.csv` and (if delta > 50 cents) revise the family scaling in the workbook.
**Verification test:** measure plate (1,1) by tapping centre of mounted tapa with a finger and reading the spectrum peak (REW); measure `f_H` by mallet-tapping the box centre with the back hole partially blocked to vary `A`. Both should land within ±10 Hz of prediction.

### A2 — Workbook uses no Helmholtz end-correction
**Severity:** high (already corrected in the v1 design.md but flagged for traceability)
**Description:** The original `cajon-design-table.xlsx` formula `f_H = (c/2π)·√(A/(V·L))` set `L = back-panel-thickness` only. The standard end-correction `1.7·r` for a flush-mounted thin-wall orifice is missing. With `L = 0.5″` and 4.5″ hole on the Standard, the spreadsheet predicts ~282 Hz; with the correct `L_eff = 0.5 + 1.7·(4.5/2) = 4.325″` it predicts ~96 Hz, which matches measured cajón behavior in the literature.
**Mitigation:** workbook formulas should be updated to use `L_eff = t_back + 1.7·(d/2)`; design.md uses the corrected expression. The next workbook revision is queued.
**Verification test:** measure `f_H` directly with REW. Acceptance: within ±15 Hz of the corrected prediction; if measurement matches the *uncorrected* prediction, the physics model is wrong.

### A3 — Tapa orthotropy not modeled
**Severity:** low-medium
**Description:** Baltic-birch ply is mildly orthotropic — fibers in alternating layers. The plate (1,1) prediction uses an isotropic clamped-plate formula and can be off by 10–20 %.
**Mitigation:** treat plate prediction as a coarse first-order estimate. Final tuning is by ear and screw-torque adjustment, not by formula.
**Verification test:** plate (1,1) measured value within ±15 % of prediction is acceptable.

### A4 — Snare buzz onset velocity is unmodeled
**Severity:** medium
**Description:** Whether the snare engages at light, medium, or hard strikes depends on contact pressure between strings and tapa, which is currently dialed by ear with no parameter on the design sheet.
**Mitigation:** record subjective onset velocity on first prototype (1–5 scale) per `validation.csv`; if the engagement feel is wrong, document the tuner-peg tension that fixed it, and consider promoting a "snare contact preload" parameter to the workbook in v2.

## Structural

### S1 — Tapa screw torque non-uniformity creates uneven plate boundary
**Severity:** medium
**Description:** Twenty #6 brass screws around a 12 × 18 perimeter — if torque varies, the plate (1,1) becomes asymmetric, with a different mode at each quadrant. This was *the* surprise of the conga's tunable-rim build, and it applies here too.
**Mitigation:** drive screws by hand, "snug not torqued"; verify with a small torque screwdriver if you have one (target ~3 in-lb each). Diagonal-symmetric driving order — opposite-corner pairs, not edge-by-edge.
**Verification test:** tap each tapa quadrant and read the spectrum peak; cross-check the four quadrant peaks for ±10 cents agreement.

### S2 — Inlay pocket leaves insufficient panel above pocket
**Severity:** low
**Description:** A 0.080″ pocket in 0.625″ Compact side panel leaves 0.545″ of structural panel above the pocket. That's enough for stiffness, but if the inlay is in a high-stress zone (corner joints, screw passes), the residual panel could fail under glue-up clamping.
**Mitigation:** keep inlay zone within the central 70 % of the panel; do **not** route within 1″ of any joint edge.
**Verification test:** measure post-inlay panel deflection at centre with 5 lb point load (dial indicator); reject if deflection > 0.020″.

### S3 — Glue-block pop-out under repeat seat loading
**Severity:** low
**Description:** Internal corner glue blocks add rigidity and shift the plate boundary, but they're glued only — no mechanical fasteners. If glue fails (over time, under repeated player weight cycles), the block could pop free and rattle in the cavity.
**Mitigation:** Titebond III, full-length glue surface (1″ × 1″ × panel-height = ~36 in²). Optional drywall-screw belt-and-suspenders fastening from the outside through the panel into the block (countersink + plug to hide).
**Verification test:** static seat-load test the assembled box at 250 lb (heavier than any expected player) for 1 hour; visual + tap inspection of all 8 internal corners after.

### S4 — Tapa cracking at slap zone over time
**Severity:** medium
**Description:** Repeated bending of the unscrewed top 4–5″ slap-zone over the working life of the cajón fatigues the 3 mm Baltic ply. Eventual delamination is a real failure mode on heavily-played cajons (~1000+ hours).
**Mitigation:** spec only BB-grade or marine-grade ply (consistent layer adhesion); do not over-tighten the lower screws (which would tense the slap zone at rest); if a crack forms, the tapa is field-replaceable since it's only screwed (not glued).
**Verification test:** none on the prototype — this is a long-term failure mode. Note the tapa as a known wear item in the final README.

### S5 — Joint failure under transport
**Severity:** low
**Description:** A 25-lb hollow box is awkward in a car. Drops or impact loads on a corner could split a finger / dovetail / spline joint.
**Mitigation:** all four joinery options spec full-length glue surfaces. Titebond III is rated 4000+ psi shear; well above any plausible impact load on a glued joint area >12 in² per corner. A padded gig-bag for transport is the cheap fix.

## Ergonomic

### E1 — Seat height misfit for short or tall players
**Severity:** medium
**Description:** Standard cajón height of 18″ matches a default 175 cm-ish adult. A 5'4" player lands their thighs near horizontal (good); a 6'4" player lands them angled-down (uncomfortable, hand position too low).
**Mitigation:** publish three sizes (Compact 15″, Standard 18″, Bass 22″) so player-fit can be matched at order time. Note in the README that the Bass is acoustically deepest *and* tallest — there are players who need a Bass for fit, not for tone.
**Verification test:** none — this is documentation-only.

### E2 — Slap-zone hand fatigue
**Severity:** low
**Description:** A poorly-tuned slap zone (over-tight upper screws, or unscrewed margin too short) makes the player hit harder to get the snap, fatiguing fingers and wrists.
**Mitigation:** spec the unscrewed margin at 4–5″ and test the slap stroke for snap with mild effort before declaring the build done. If the player has to hit hard, the build is wrong.

## Supply

### SU1 — Tapa thickness inconsistency from supplier
**Severity:** medium
**Description:** "3 mm" Baltic birch is nominal. Real sheets from non-BB-grade sources can vary ±0.010″, which is ±8 % of the nominal — and plate (1,1) varies as `h³`, so a 10 % thickness change means a ~30 % stiffness change, ~15 % frequency shift.
**Mitigation:** spec BB grade or better and spot-check thickness on arrival. Reject sheets >0.010″ off nominal.
**Verification test:** caliper measurement at 5 points per sheet; record in `validation.csv` per build.

### SU2 — Hard-to-source 3 mm ply (regional availability)
**Severity:** low
**Description:** US suppliers stock 3 mm Baltic birch, but it's a special-order item — not on shelves at big-box stores. International builds may struggle.
**Mitigation:** RFQ document lists Ocooch Hardwoods as US-preferred; alternates: Veneer Supplies, Anderson International. UK/EU builders: search for "3mm birch ply BB grade marine."

### SU3 — Brass screws supplier substitution
**Severity:** low
**Description:** "Brass-plated" steel screws look identical at first glance and are easy to swap in by mistake. Brass plate corrodes; solid brass does not. Also, plated screws magnetically pick up sawdust at the workbench.
**Mitigation:** spec "solid brass" explicitly in `bom.csv` and `sourcing.csv`. Verify with a magnet test on the workbench before installation.

## Fit / finish

### F1 — Inlay press-fit too tight cracks insert
**Severity:** medium
**Description:** Broinwood-style inlay is unforgiving: too-tight fit splits the maple insert when pressed home; too-loose leaves a visible gap line. The inlay-allowance setting in VCarve is the single tuning knob.
**Mitigation:** test cut on scrap before committing. Adjust allowance ±0.005″ until the dry-fit drops in with mild thumb pressure.
**Verification test:** inspect inlay for hairline cracks after press; reject if any cracks visible.

### F2 — Squeeze-out into cavity creates rattle
**Severity:** low
**Description:** Glue squeeze-out from joinery into the cavity — if it dries as a hard bead — can vibrate audibly during play, sounding like a "buzz of unknown origin" that drives the maker mad.
**Mitigation:** wipe squeeze-out with a damp cloth before glue cures; inspect interior with a flashlight after final cure; hand-pick out any beads with a chisel.

### F3 — Finish bleed onto tapa edge
**Severity:** low
**Description:** Arm-R-Seal poly applied to the body can bleed onto the tapa edge at the joint, sealing the slap-zone gap and changing the slap acoustics.
**Mitigation:** mask the tapa's perimeter before finishing the body. Apply tung oil to tapa first (penetrating, no surface film), then mask + finish body.

---

## Risk roll-up

| Category | Highest severity | Open count |
|----------|------------------|------------|
| Acoustic | A2 (closed in design.md, flagged for workbook) | 4 |
| Structural | S1, S4 (medium) | 5 |
| Ergonomic | E1 (medium, doc-only) | 2 |
| Supply | SU1 (medium) | 3 |
| Fit/finish | F1 (medium) | 3 |
| **Total** | | **17** |

The single highest-leverage risk on first prototype is **A2 / SU1 in combination** — the workbook's old Helmholtz formula was wrong, *and* tapa thickness can vary in the supply chain. If the build comes in off-pitch, the question to ask first is "what was the actual tapa thickness?" — not "is the design wrong?"
