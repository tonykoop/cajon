# CNC — Cajón Family

CNC strategy notes for the three operations on the cajón that benefit from CNC vs hand-tool execution: **(1)** finger-joint corners, **(2)** inlay pockets and inserts, **(3)** the back-panel sound hole.

The cajón is otherwise table-saw / router / hand-tool friendly. There is no complex profile-turning or coupling like the conga or fujara — the box is rectilinear.

## Machine + tooling assumptions

- Router: ShopBot Desktop or equivalent (24″ × 36″ work envelope minimum)
- Spindle: 2.2 kW, variable 6,000–24,000 RPM
- Bits used:
  - **TBN-12.4** — Amana 45739, 12.4° tapered ball-nose, 1/4″ shank — for inlay pocket + insert
  - **SF-1/2** — Amana 46176, 1/2″ straight-flute spiral, 1/4″ shank — for finger joint
  - **DT-14** — Amana 45813, 14° dovetail, 1/2″ — for V2 dovetail (optional)
  - **HSAW-4.5** — 4.5″ hole-saw (alternative to CNC pocket for sound hole)
- Vacuum hold-down preferred for inlay panels; T-track clamps acceptable for joinery.

## Operation 1 — Finger-joint corners (V1)

The 1/2″ spiral bit cuts 0.375″-wide finger pockets. Standard pin spacing is 0.375″; for a 12″ panel that's 32 fingers — even number, alternating pins, mating panels offset by one pin width.

```
Bit:        SF-1/2 (1/2" straight-flute spiral)
Feed:       40 IPM
Plunge:     12 IPM
RPM:        16,000
Step-down:  0.25" per pass (max)
Tool path:  pocket toolpath, ramp entry
```

**Critical:** verify kerf and spiral direction with a test cut on scrap. A down-cut spiral leaves a cleaner top edge but loads chips downward; an up-cut clears chips but tear-outs the top edge of walnut. Compromise: compression bit if you have it; up-cut + skim pass at 0.005″ depth as a finish pass otherwise.

The finger pattern is **mirrored on mating panels** — left side of side panel mates with left side of top panel; the pocket on one is the pin on the other. Generate the mating G-code from the same VCarve project, just toggle the layer.

## Operation 2 — Inlay pocket + insert (Broinwood-derived)

This is the high-leverage CNC operation on the cajón. It's the visual signature.

```
Bit:        TBN-12.4 (12.4° tapered ball-nose)
Feed:       30 IPM
Plunge:     10 IPM
RPM:        18,000
Pocket depth:    0.080–0.100" (pocket = negative, in walnut)
Insert depth:    pocket_depth + 0.020" (positive, in maple)
Tool path:  follow-vector for insert; pocket-clearance for pocket
```

The bit's tapered profile creates undercut walls in the pocket and matching tapered shoulders on the insert. As the insert is pressed in, the tapered shoulder seats against the tapered pocket wall — no glue gaps visible from the top once flush-sanded.

**VCarve allowance setting:** start at 0.000″ (factory default). If dry-fit is too tight (insert won't seat with thumb pressure), increase by 0.005″. If dry-fit is loose (rocks in pocket), decrease by 0.005″. *Always test on scrap before committing to the panel.*

**Panel keep-out:** route only within the central 70 % of the panel — keep 1″ clear of every joint edge so the joinery has solid wood.

## Operation 3 — Sound hole

Two acceptable paths:

**A. CNC pocket (preferred)** — cleanest result, no rasping required.
```
Bit:        SF-1/2 (1/2" straight-flute spiral)
Feed:       30 IPM
Plunge:     8 IPM
RPM:        16,000
Step-down:  0.10" per pass
Tool path:  pocket-clearance, spiral-entry, full-through (back panel is 0.5")
```

**B. Hole saw + jigsaw + rasp** — works fine, more cleanup.
- 4.5″ hole saw on drill press, low RPM (~250)
- Or: drill 1/2″ pilot, jigsaw + circle jig
- Rasp + 220 grit deburr both sides

Either way: **deburr both sides 220 grit minimum.** A sharp inside edge on the sound hole creates audible high-frequency hash on slap strokes.

## Operation 4 — Half-blind dovetail (V2 optional)

```
Bit:        DT-14 (1/2" 14° dovetail)
Feed:       25 IPM
Plunge:     8 IPM (carefully — dovetail bits do not plunge well; ramp instead)
RPM:        14,000
Tool path:  Dovetail-specific (use VCarve's half-blind dovetail wizard)
```

Half-blind dovetails on a CNC need a precision fixture — the bit cuts pin and tail in two different orientations, and the panels must register identically. Use a sled fixture or Whiteside-style dovetail jig with CNC-mounted bits if available.

## File outputs (planned, not yet generated)

- `cajon-fingerjoint-side.nc` — G-code for finger-joint side panel pockets
- `cajon-fingerjoint-top.nc` — G-code for top/bottom panel mating fingers
- `cajon-inlay-pocket.nc` — pocket toolpath for inlay pattern (panel-A example)
- `cajon-inlay-insert.nc` — insert toolpath for matching inlay
- `cajon-soundhole.nc` — pocket toolpath for back-panel sound hole

Generate these from VCarve Pro projects pulling geometry from `cajon-master.scad` (export DXF) and the inlay artwork SVGs (Broinwood-style geometric patterns or custom).

## Setup checklist

Before any CNC pass on a real panel:
- [ ] Spoilboard surfaced flat within 0.005″
- [ ] Vacuum or clamps verified (no movement under hand pressure)
- [ ] Bit depth-of-cut and shank engagement checked
- [ ] X/Y/Z zero set to a permanent reference (not the corner of the workpiece)
- [ ] Test cut on identical-thickness scrap at the same fixture position
- [ ] Dust collection on, ear protection on
- [ ] First 10 % of toolpath observed before walking away
