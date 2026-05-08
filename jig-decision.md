# Jig Decision Log

This cajon is a simple box, so the jigs carry most of the repeatability. The public-review packet treats three fixtures as required for the Standard prototype and two as optional paths for later variants.

## Required jigs for the first prototype

| Jig | Decision | Why it is required | Acceptance check |
|---|---|---|---|
| Square assembly fixture | Build a flat baseboard with two fixed 90-degree fences, four movable clamp blocks, and diagonal check marks. | The shell has to glue square before the tapa can clamp evenly; a twisted box makes the tapa buzz unpredictably. | Dry-fit shell diagonals within 1/16 in before glue; after cure each face sits flat without rocking. |
| Tapa screw drilling template | Make a reusable 1/8 in hardboard or acrylic template indexed from the bottom and centerline. | The 3 in screw spacing and unscrewed top slap zone are tonal features, not decoration. A hand-marked layout is too easy to drift. | Holes land within +/-0.10 in of pattern; top 4.5 in corner slap zone remains undrilled. |
| Back-panel drill template | Make a template with the sound-hole center, tuner holes, and snare-mount pilot locations. | The sound-hole position sets the Helmholtz path and the tuner holes must align with the snare block. | Sound hole center within +/-0.10 in; tuner holes align without string rub. |

## Optional / variant jigs

| Jig | Use when | Decision |
|---|---|---|
| Finger-joint indexing sled | V1 table-saw build without CNC | Recommended if CNC is not used. Use a measured key equal to the actual dado kerf, not nominal cutter size. |
| Spline sled | V4 miter+spline showpiece | Required for V4. Three repeatable slots per corner are a visual commitment; freehand routing is not acceptable. |
| Dovetail vacuum fixture | V2 CNC half-blind dovetail | Required for V2. Treat as a separate CAM setup with sacrificial spoilboard and hold-down tabs. |

## Public-review decision

The first public candidate should ship as **CJ-S / V1 / snare B** with the square assembly fixture, tapa screw template, and back-panel template built before any final stock is cut. That keeps the prototype teachable: reviewers can evaluate tone and ergonomics without confusing fixture error for design error.

## Jig files in this repo

- `jigs/README.md` - fixture overview and build order.
- `jigs/tapa-screw-template.svg` - drill-template concept for the Standard tapa.
- `jigs/square-assembly-fixture.svg` - baseboard and clamp-block layout.
