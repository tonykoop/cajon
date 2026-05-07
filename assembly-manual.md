# Cajón — Assembly Manual

Covers all four joinery variants (V1 finger-joint, V2 dovetail, V3 rabbet, V4 miter+spline) and all three snare options (A none, B guitar-string, C snare-wire). Steps shared across variants are written once with branching notes where the variants diverge. The manual assumes you have read `design.md` and have `cajon-design-table.xlsx` open for member-specific dimensions.

The first prototype is the **Standard (CJ-S), V1 finger-joint, snare option B**; phases are written from that build. Compact and Bass scale by simple geometry.

---

## Phase 0 — Shop preparation

1. **Acclimate stock** in shop for 1–2 weeks (60–70 °F, 40–55 % RH). Walnut and Baltic birch ply both move; stable stock = stable joints later.
2. **Mill body panels** to nominal thickness ± 0.005″. Final dimensions:
   - Standard sides: 18.000″ × 12.000″ × 0.750″
   - Standard top + bottom: 12.000″ × 12.000″ × 0.750″
   - Standard back panel: 18.000″ × 12.000″ × 0.500″
   - Standard tapa: cut oversized to 18.5″ × 12.5″ × 0.118″ (3 mm); trim flush after assembly
3. **Verify saw kerf width** with a test cut. The finger-joint and spline cuts assume a known kerf; measure yours before sizing rough stock.
4. **Check CNC fixturing** — vacuum hold-down or T-track clamps, surfaced spoilboard within 0.005″ TIR over the working area. Inlay routing is unforgiving of stock movement.
5. **Square** all panels. Diagonals on each panel face must agree within 0.020″.

---

## Phase 1 — CNC inlay (BEFORE assembly)

This phase exists for the inlay-equipped builds. Skip and continue to Phase 2 if no inlay.

### 1.1 Inlay design pass

1. Open the inlay artwork in VCarve Pro (or Aspire). The Broinwood-style design files ship as paired SVG + DXF; import the SVG layer for the visual artwork and DXF for the cut outlines.
2. Confirm panel-fit: the inlay should sit within the central 70–80 % of the panel; do **not** route within 1″ of the joint edge — the joint geometry needs solid wood.
3. Verify two layers exist:
   - **Pocket layer** (negative): the depression cut into the body panel
   - **Insert layer** (positive): the contrasting wood that fills the pocket
4. Set the CNC parameters per design.md §5: TBN 12.4° tapered ball-nose bit, depth 0.080–0.100″, 30 IPM feed, 18,000 RPM spindle.

### 1.2 Pocket cut

1. Mount the **walnut** body panel flat on the CNC bed with vacuum or four-corner T-track clamps.
2. Zero on the panel surface (top of stock = Z0).
3. Run the pocket toolpath. Pause to clear chips between passes if the bit loads up.
4. Inspect the cut: pocket depth uniform within 0.005″ across the panel; no chip-out at edges.

### 1.3 Insert cut

1. Mount the **maple** (or yellowheart, or cherry) inlay blank.
2. Run the insert toolpath. The insert is taller than the pocket is deep — the tapered geometry locks both pieces together as you press them home.
3. Trim the insert backing to ~0.060″ above the inlay shoulder; fit-check by holding it against the pocket.

### 1.4 Glue & flush

1. Apply Titebond III to the pocket. Press the insert in firmly. Place wax paper on top, then a flat plywood caul, then clamp evenly across the panel.
2. Cure 24 h.
3. Remove clamps. Using a drum sander or random-orbit at 80–120 grit, sand the surface flush with the panel. Inspect for any micro-gaps; fill with fine matching sawdust + a drop of CA glue.
4. Sand to 220 grit. Set inlaid panel aside until joinery.

---

## Phase 2A — Joinery (V1 finger joint)

### 2A.1 Layout

For a finger-joint corner with `n` fingers per joint and finger width `w`, panel width `W = n·w`. Standard tongue width is 3/8″ and 12″ panel = 32 fingers. Use a CNC parametric finger jig or a table-saw finger jig.

### 2A.2 Cut

1. Cut **side panels** with finger pockets on the top and bottom edges (joining to top + bottom panels).
2. Cut **top + bottom panels** with finger pockets on the left and right edges (joining to side panels).
3. Cut **side panels** with finger pockets on the back edge (joining to back panel) — *but use a thinner finger pattern matching the 1/2″ back-panel thickness.* Don't try to use the same 0.75″ finger pattern on a 0.50″ panel — it will blow out.
4. Test-fit dry: 4 sides + 2 caps + 1 back = 6 corner-pairs. All fingers should engage with mild hand pressure; if any pair binds, plane a few thousandths off the proud finger.

### V2 — half-blind dovetail

Same logic, replace finger pattern with a CNC half-blind dovetail at 14° pin angle, pin spacing per drawing 06. Use the dovetail bit listed in `bom.csv`.

### V3 — rabbet

Cut a 3/8″ deep × 3/4″ wide rabbet along the inside top and bottom edges of each side panel. Top + bottom drop into the rabbets; back panel rabbet is the same on the back edge.

### V4 — miter + spline

1. Cut all corner edges at 45° on a table-saw sled.
2. Glue and tape-clamp the four side faces (top + bottom + 2 sides) into a frame with mitered corners.
3. Cure 24 h. Remove tape.
4. Cut spline slots: 3 per corner, 1/8″ wide × 0.6″ deep, on a spline jig. Use a contrasting maple slip; glue, set, trim flush.
5. Glue back panel into a rabbet on the back edge of the frame (V4 uses miter on top/bottom/sides + rabbet for the back).

---

## Phase 3 — Sound hole + back panel features

1. Mark the sound-hole centre on the back panel: centred L–R, 1/3 of the height down from the top edge. For Standard, that's 12″/2 = 6.000″ from a long edge and 18″/3 = 6.000″ from the top edge.
2. Cut the 4.5″-diameter hole. CNC pocket gives the cleanest result; a hole-saw + jigsaw works; rasp the inside edge smooth.
3. Deburr both sides with 220 grit. Inside edge of the hole is acoustically active — sharp edges create unwanted high-frequency hash on slap.
4. (Optional) Rosette inlay around the hole; route before assembly.

---

## Phase 4 — Internal corner glue blocks

1. Rip 8 triangular blocks from walnut offcuts: cross-section ≈ 1″ × 1″ (right-angle face inside, hypotenuse facing the box interior); length = panel height (Standard = 18″; Compact = 15″; Bass = 22″).
2. Glue all 8 blocks into the 8 internal vertical corners of the box (4 top + 4 bottom intersections). Use Titebond III. Don't let glue squeeze-out into the cavity — tool away anything beyond the joint line.
3. Why: rigidity. Cajón corners are the highest-strain area when sat on; glue blocks also subtly shift the (1,1) plate boundary condition by stiffening the perimeter.

---

## Phase 5 — Snare assembly (option B — guitar string snare)

If you are skipping the snare (option A — Peruvian style), continue to Phase 6.

1. Cut the snare mount block: 5″ × 1″ × 1″ maple, with one face angled 8–12° off vertical. The angled face will press against the inside of the tapa.
2. Glue + screw the mount block to the inside of the **back** panel, oriented so the angled face points toward where the tapa will be. The block sits ~1–1.5″ below the top of the back panel — that places the snare contact in the slap zone.
3. Drill 4 holes through the back panel at the bottom of the box for the tuner pegs (3 strings minimum, 4 strings maximum). Holes spaced ~3/4″ apart.
4. Mount tuner pegs on the outside of the back panel. (Use single guitar-tuner-peg style; Stewart-MacDonald sells acoustic-guitar tuner blocks ready-to-use.)
5. **Do not run strings yet.** Do this after the box is glued and the tapa is mounted, because you'll be tensioning while listening to the snare buzz.

For option C (snare wires), substitute a 13″ section of standard snare-drum wires and a tension lever clamped to the inside of the back panel, oriented to lightly contact the tapa.

---

## Phase 6 — Box glue-up

1. Lay all panels flat on a tarp in their final orientation (sides + top + bottom + back; tapa stays separate).
2. Glue all joints: Titebond III on every mating finger / dovetail / rabbet / miter face.
3. Assemble. Use band clamps around the outside perimeter — minimum 4, ideally 8. Verify squareness with a framing square on each face.
4. Diagonal check: measure both diagonals on each face. Adjust band-clamp tension to bring them within 1/16″.
5. Cure 24 h.
6. After cure, remove clamps and sand the entire body to 220 grit. Pay attention to corner edges — soften with a 1/16″ roundover or hand-sanded micro-bevel for player comfort.

---

## Phase 7 — Tapa attachment

1. Place the tapa face on the front of the box. Trim flush if oversized.
2. Pre-drill #6 pilot holes through the tapa and into the side / top / bottom panel edges. Spacing: every 3″ around the perimeter.
3. **Critical:** Leave the **top 4–5″** of the tapa **unscrewed** at both upper corners. This unscrewed margin is the slap zone — you bend the tapa here when you strike the corner, which creates the snap.
4. Drive #6 × 3/4″ slotted brass flathead screws by hand. Snug, not torqued — the goal is even contact with the box edges, not crushing pressure.
5. Tap the centre of the tapa with a finger; you should feel and hear a clean low pitch. If you hear a buzz from anywhere other than the snare, find and fix it before installing strings.

---

## Phase 8 — Snare tensioning + tuning

1. Run the snare strings through the tuner-peg block on the outside of the back panel and over the angled snare mount block inside.
2. Tension all strings to mild pressure against the inside of the tapa. Snare buzz onset should engage at a *medium* slap stroke, not at a light tap.
3. Tune by ear:
   - Strike centre of the tapa → bass voice. Should be deep, clean, ringing 90–110 Hz for Standard.
   - Strike upper corner → slap voice. Should engage snare buzz cleanly.
   - Adjust tapa screw torque if the bass voice is buzzing or muffled. Tighter screws = brighter, shorter sustain. Looser = boomier.
4. **Record measurements** in `validation.csv`:
   - Helmholtz frequency (use a tuner; tap centre with mallet, hold)
   - Plate (1,1) frequency (tap tapa centre with finger)
   - Slap-to-bass spectral delta (REW or smartphone spectrum analyzer)

---

## Phase 9 — Finish

1. **Tapa:** apply 100 % pure tung oil cut 50/50 with citrus solvent for the first coat. Let soak in for 15 min, wipe off excess. Cure 24 h. Apply 1–2 more coats of full-strength tung oil. The tapa should *feel* like wood, not plastic.
2. **Body:** apply Arm-R-Seal satin polyurethane in 3 thin coats. Light scuff with 320 grit between coats. Final coat hand-rubbed with steel wool for a satin feel.
3. **Avoid finishing the inside of the cavity** — bare wood absorbs internal reflections more naturally; finished interiors get a glassier high-frequency reflection that some players dislike.

---

## Phase 10 — Feet + final inspection

1. Stick four 1/2″ rubber feet to the bottom panel, one in each corner. Inset 1/2″ from each edge.
2. Final play-test: bass tone (centre), slap (upper corner), tip (mid-edge), brush (drag fingers). Each should produce a distinct voice.
3. Record final cents reading in `validation.csv`. Mark variant + member + tuning instrument used.
4. Photograph per `photo-shotlist.md`.

---

## Compact (CJ-C) and Bass (CJ-B) variants

The Compact and Bass scale by simple geometry. All phases are identical except:

- **Compact:** 15 × 11 × 11; body 0.625″; sound hole 4.0″; tapa 15 × 11 × 0.118″; finger pattern scaled to panel width
- **Bass:** 22 × 14 × 14; body 0.75″; sound hole 5.0″; tapa 22 × 14 × 0.118″; band-clamp count + 2 (use 8–10 for the larger box)

The Bass is heavy — a glued shell is ~25 lb. Two-person glue-up is recommended.

---

## Notes that the workbook does not say

- Tapa screws are slotted-brass for two reasons: visual (they read as old-world hardware), and acoustic (Phillips heads are easier to over-torque, which audibly tightens the bass voice).
- The 4–5″ unscrewed slap zone at the top of the tapa is the *single most important* trad design element. Don't skip it. A fully-screwed tapa sounds dead.
- If the snare buzzes when you strike the centre (not the corner), the snare contact is too tight. Loosen one notch on the tuner peg.
- A new tapa mellows for the first 50–100 hours of play. Do not "fix" it sounding bright on day one.
