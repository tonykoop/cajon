# CAD / MCP Session Log — Cajón Family

Records every external-tool or MCP session that produced or modified an artifact
in this packet. Required by the V5 build-packet standard before any artifact may
claim MCP provenance.

One row per session × artifact. Add a new row immediately after each session.
Do not back-fill or estimate session IDs.

---

## Session log

| session_id | tool | input_authority | outputs | role | authority_result | review_status | notes |
|---|---|---|---|---|---|---|---|
| pending-blender-hero | Blender MCP | cad/cajon-master.scad (OpenSCAD STL export) | images/hero-render.png | concept_render | pending_measurement | pending | Planned: 3/4 view, 2048×1536 sRGB, studio lighting. See images/render-brief.md for full spec. |
| pending-blender-explode | Blender MCP | cad/cajon-master.scad (OpenSCAD STL export) | images/assembly-explode.png | concept_render | pending_measurement | pending | Planned: panels offset along face normals, exploded assembly diagram frame. |
| pending-blender-material-birch | Blender MCP | cad/cajon-master.scad; images/blender-scene.blend | images/material-study/birch-ply.png | concept_render | pending_measurement | pending | Planned: birch ply material variant, same camera as hero render. |
| pending-blender-material-walnut | Blender MCP | cad/cajon-master.scad; images/blender-scene.blend | images/material-study/walnut.png | concept_render | pending_measurement | pending | Planned: walnut material variant. |
| pending-blender-material-mdf | Blender MCP | cad/cajon-master.scad; images/blender-scene.blend | images/material-study/painted-mdf.png | concept_render | pending_measurement | pending | Planned: painted MDF variant. |
| pending-blender-scene | Blender MCP | cad/cajon-master.scad | images/blender-scene.blend | tool_source | pending_measurement | pending | Planned: saved .blend scene with reproducible camera, lighting, material nodes. Required by issue #4 acceptance criteria. |

## Authority boundary

No Blender MCP session has executed yet. All rows above are planning placeholders.
The `pending_measurement` authority_result blocks any render from being promoted
to fabrication or derived_preview authority until a real session ID replaces the
`pending-*` placeholders and review_status advances to `self_checked` or better.

Blender MCP requires Claude Desktop. When a session runs:
1. Replace the `pending-*` session_id with the actual session timestamp or ID.
2. Set `authority_result` to `concept_only` (renders are not dimensional authority).
3. Set `review_status` to `self_checked`.
4. Update `visual-output-register.csv` rows to match.
