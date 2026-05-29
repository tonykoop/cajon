# Cajón Family — Blender MCP Render Brief

This brief specifies the complete render setup for issue #4 (Blender MCP hero
render + assembly explode test). All outputs remain `pending_measurement` until
a Blender MCP session executes them and updates `cad/mcp-session-log.md`.

---

## Source geometry

- Input: `cad/cajon-master.scad` → export STL via OpenSCAD (or STEP from `cnc/`
  if available).
- Target member: CJ-S Standard (18 × 12 × 12 in) is the first-prototype default.
  Run all three members (CJ-C, CJ-S, CJ-B) for the family-group render if time
  permits.
- Assembly components to model as separate objects:
  1. Back panel
  2. Left side panel
  3. Right side panel
  4. Top panel
  5. Bottom panel
  6. Tapa (front face, with sound hole)
  7. Snare wires (simplified as parallel line objects, V2/B variant)

---

## Hero render spec

- **Camera**: 3/4 view, 45° elevation, camera positioned so the tapa (front face)
  and one side panel are both visible. Place the sound hole in the upper half of
  the frame.
- **Resolution**: 2048 × 1536 px (4:3 ratio), sRGB color space.
- **Lighting**: three-point studio setup — key light upper right, fill light left,
  rim light behind/below. No HDR environment that implies a real location.
- **Material**: default birch ply (light tan, subtle grain, semi-gloss finish).
- **Output**: `images/hero-render.png`
- **Authority**: concept_only — marketing image, not dimensional. Register in
  `visual-output-register.csv` as `concept_only` after execution.

---

## Assembly explode spec

- **Layout**: explode each panel along its outward face normal by a uniform offset
  (suggest 80–120 mm) so the interior is clearly visible.
- **Snare wires**: offset along the Z-axis (vertical) to show their relationship
  to the tapa.
- **Camera**: same 3/4 angle as hero render.
- **Frame**: render one still frame of the exploded state (not animation).
- **Output**: `images/assembly-explode.png` at 2048 × 1536 px.
- **Callouts** (optional): numbered arrows pointing to each panel, keyed to
  assembly-manual.md section numbers. Use Blender annotation layer or composite
  in post.
- **Authority**: concept_only (annotated communication, not fabrication geometry).

---

## Material study spec (three variants, same camera as hero)

All three at 2048 × 1536 px, using the saved scene from `images/blender-scene.blend`.

| File | Material | Wood grain direction | Finish |
|---|---|---|---|
| `images/material-study/birch-ply.png` | Baltic birch ply | horizontal on side panels | semi-gloss polyurethane |
| `images/material-study/walnut.png` | American walnut | horizontal | oil finish (matte) |
| `images/material-study/painted-mdf.png` | MDF with gloss paint | N/A | satin black |

---

## Scene file requirement

Save the final camera position, lighting setup, and material nodes to
`images/blender-scene.blend` before ending the session. This file is required
by the issue #4 acceptance criteria so the render is reproducible without
manual reconstruction.

---

## Provenance steps (complete after each render)

1. Add a real session row to `cad/mcp-session-log.md` with actual session ID/timestamp.
2. Update `visual-output-register.csv`: change `pending_measurement` to `concept_only`
   for each executed render.
3. Confirm no gamma double-correction: the output PNG should be sRGB tagged. Verify
   in an image viewer that whites are not blown out vs the Blender viewport preview.
4. Confirm file sizes are reasonable (hero render: typically 1–4 MB for 2048×1536 PNG).
