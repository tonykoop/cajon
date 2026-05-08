# Title

Cajon Family Public-Review Prototype

Tony Koop / Heifer Zephyr Instruments. Root-mode packet for a three-member cajon family with a Standard first prototype.

# Project Intent

Turn a mechanically simple box drum into a repeatable, reviewable build. The contribution is not inventing the cajon; it is documenting a clean parametric family, robust joinery paths, explicit jigs, and measured tone/buzz validation so another maker can reproduce the work.

# Family Overview

Compact, Standard, and Bass members share the same layout law: rectangular shell, thin tapa, back sound hole, optional snare. Standard CJ-S is the first build because it sits in the ergonomic and tonal middle of the family.

# Governing Physics

The bass voice comes from a Helmholtz cavity coupled to the first bending mode of the tapa. The Standard target is 96 Hz cavity response and 84 Hz plate response, with the perceived bass expected near the coupled midpoint.

# Critical Geometry

The Standard prototype is 18 x 12 x 12 in with 3/4 in walnut body panels, 1/2 in back panel, 3 mm Baltic birch tapa, and a 4.5 in back sound hole. Tapa screw spacing and the unscrewed slap zone are treated as acoustic geometry.

# Joinery Strategy

V1 finger joint is the first public candidate because it is strong, teachable, and forgiving. V2 dovetail, V3 rabbet, and V4 miter+spline remain documented variants for later builds.

# Tapa and Screw Pattern

The tapa is mounted with #6 brass flathead screws roughly every 3 in. The upper 4-5 in corner zones are intentionally left loose so the corner strike can snap instead of choking.

# Snare Mechanism

Snare option B uses adjustable guitar strings contacting the inside of the tapa near the top. The design validates snare onset by feel and recording: no buzz on a light tap, clean buzz on a medium corner slap.

# Jig Plan

Three fixtures are required before the first build: a square assembly fixture, a tapa screw drilling template, and a back-panel drill template. These convert the simple box into a repeatable instrument rather than a one-off cabinet.

# BOM and Sourcing

The Standard prototype is estimated near 205 USD in materials and consumables. Supplier rows are representative; current prices, stock, and shipping terms must be rechecked before purchase.

# Cut List and Manufacturing Flow

Mill panels, route inlay before assembly, cut joinery, cut/deburr back sound hole, glue the shell square, mount the tapa, tension the snare, finish, and validate. The tapa is screwed, not glued, so it remains serviceable.

# Drawings, CAD, CNC

The repo includes SVG drawing sheets, an OpenSCAD master, CNC notes, and jig drawings. Public-review drawings emphasize datum chains, screw layout, sound-hole placement, and fixture-driven repeatability.

# Validation Plan

Validation measures shell squareness, seat load, sound-hole diameter, tapa torque uniformity, Helmholtz response, plate mode, coupled bass, slap spectral delta, snare onset, and finish feel. Results land in `validation.csv`.

# Risks

The main open risks are acoustic model drift from real plywood, non-uniform tapa screw torque, snare preload, supplier variation in 3 mm birch ply, and placeholder imagery before the prototype is photographed.

# Public Release Readiness

This is a fast public candidate after human build review. The packet is complete enough to invite critique, but the public page should clearly mark the design as pre-build until CJ-S measurements and real build photos exist.

# Next Actions

Build CJ-S V1 with snare B, record measured values, update the workbook formula if any stale Helmholtz cells remain, replace placeholder visuals with shop photos, and rerun the packet validator before release.
