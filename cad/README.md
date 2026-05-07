# CAD — Cajón Family

This folder is the home for SolidWorks parametric models, OpenSCAD masters, and CAD-export geometry that drives the manufacturing files in `cnc/` and the dimensioned drawings in `drawings/`.

## Status

The cajón is a six-panel rectilinear box, simpler than a turned-shell instrument like the conga or udu. CAD complexity sits in the joinery (finger / dovetail / spline) and the inlay zone, not in the body geometry. As of v1:

- **`cajon-master.scad`** — OpenSCAD parametric master for the box body, sound hole, and finger-joint corners. Edit the parameters at the top, render, and export STL/DXF.
- **SolidWorks model** — *queued for v2*. Standard SW workflow per `instrument-maker-v4/references/solidworks-integration.md`: MasterLayout part + design table linked to `cajon-design-table.xlsx`. The OpenSCAD model is sufficient for v1 cut-list verification.

## Workflow

1. Edit the OpenSCAD master parameters to match the family member you want (Compact / Standard / Bass).
2. Render in OpenSCAD; export DXF (top view) for laser-cutting flat panels OR STL (full body) for visualization.
3. Cross-check OpenSCAD geometry against `cajon-design-table.xlsx` outputs; numbers must agree.

## Files

| File | Purpose |
|------|---------|
| `cajon-master.scad` | OpenSCAD parametric body — edit + render |
| (planned) `cajon-master.sldprt` | SolidWorks part with design table |
| (planned) `cajon-assembly.sldasm` | SolidWorks assembly: 6 panels + glue blocks |
| (planned) `cajon-drawing.slddrw` | SolidWorks drawing → exports the SVGs in `../drawings/` |
