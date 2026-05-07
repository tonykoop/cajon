// Cajón Family — OpenSCAD parametric master
// Heifer Zephyr Instruments — Tony Koop
// Generates a six-panel cajón shell with sound-hole, snare-mount keep-out,
// optional inlay zone visualization, and finger-joint corners.
//
// Edit MEMBER below and render. Export DXF (Projection -> Front view) for laser
// or STL for full-body visualization.
//
// Units: inches.

/* [Family member] */
MEMBER = "Standard"; // [Compact, Standard, Bass]

/* [Variant] */
JOINERY = "FingerJoint"; // [FingerJoint, Dovetail, Rabbet, MiterSpline]
SHOW_INLAY_ZONE = true;
SHOW_SNARE_BLOCK = true;
EXPLODE = 0; // 0 = assembled; >0 = exploded view in inches

/* [Override (only used if MEMBER = "Custom")] */
CUSTOM_H = 18;
CUSTOM_W = 12;
CUSTOM_D = 12;
CUSTOM_HOLE = 4.5;

/* [Constants] */
BODY_T   = 0.75;
BACK_T   = 0.5;
TAPA_T   = 0.118;
GLUE_BLOCK = 1.0; // 1" cross-section triangle
$fn = 60;

// === Member dimensions ===
H = MEMBER == "Compact"  ? 15 :
    MEMBER == "Standard" ? 18 :
    MEMBER == "Bass"     ? 22 :
    CUSTOM_H;
W = MEMBER == "Compact"  ? 11 :
    MEMBER == "Standard" ? 12 :
    MEMBER == "Bass"     ? 14 :
    CUSTOM_W;
D = MEMBER == "Compact"  ? 11 :
    MEMBER == "Standard" ? 12 :
    MEMBER == "Bass"     ? 14 :
    CUSTOM_D;
HOLE = MEMBER == "Compact"  ? 4.0 :
       MEMBER == "Standard" ? 4.5 :
       MEMBER == "Bass"     ? 5.0 :
       CUSTOM_HOLE;
BT = MEMBER == "Compact"  ? 0.625 :
     BODY_T;

// === Internal cavity ===
function cavity_volume() = (W - 2*BT) * (D - 2*BT) * (H - BODY_T - BACK_T);

// === Box body (5 panels: top, bottom, 2 sides, back; tapa drawn separately) ===

module side_panel() {
    cube([H, BT, D]);
}

module top_panel() {
    cube([BT, W, D]);
}

module bottom_panel() {
    cube([BT, W, D]);
}

module back_panel() {
    difference() {
        cube([H, W, BACK_T]);
        // Sound hole — centred L-R, 1/3 H from top
        translate([H * 2/3, W/2, -0.1])
            cylinder(h = BACK_T + 0.2, r = HOLE/2);
        // Snare mount block keep-out — interior, top region (visualization only)
        if (SHOW_SNARE_BLOCK) {
            translate([H - 1.5, W/2 - 2.5, BACK_T - 0.05])
                cube([1.0, 5.0, 0.1]);
        }
    }
}

module tapa() {
    cube([H, W, TAPA_T]);
}

// === Inlay zone visualization ===
module inlay_zone(panel_h, panel_w) {
    // 70% of panel area, centred, 1" keep-out from edges
    color("orange", 0.25)
    translate([1, 1, -0.05])
        cube([panel_h - 2, panel_w - 2, 0.05]);
}

// === Glue blocks (8 internal corners) ===
module glue_block(h) {
    // Triangular cross-section, 1" x 1" right angle
    linear_extrude(h)
        polygon([[0,0], [GLUE_BLOCK, 0], [0, GLUE_BLOCK]]);
}

module all_glue_blocks() {
    panel_h = H - BODY_T*2;
    color("saddlebrown", 0.7) {
        // Bottom 4 corners
        translate([BODY_T, BT, BACK_T]) glue_block(panel_h);
        translate([BODY_T, W - BT, BACK_T]) rotate([0, 0, -90]) glue_block(panel_h);
        translate([BODY_T, BT, D - 0]) rotate([0, 0, 0]) mirror([0,0,1]) glue_block(panel_h);
        // (Skipping the others for sketch simplicity — real model gets 8)
    }
}

// === Assemble box ===

module cajon_assembly() {
    // Bottom
    bottom_panel();
    // Top
    translate([H - BODY_T, 0, 0]) top_panel();
    // Side L
    translate([0, 0, 0]) side_panel();
    // Side R
    translate([0, W - BT, 0]) side_panel();
    // Back
    translate([0, 0, D - BACK_T]) back_panel();
    // Tapa (front) — explode out front face
    translate([0, 0, -TAPA_T - EXPLODE]) tapa();

    if (SHOW_INLAY_ZONE) {
        // Side L panel inlay zone
        translate([0, BT/2 - 0.05, 0])
            rotate([90, 0, 90])
                inlay_zone(D, H);
    }

    if (SHOW_SNARE_BLOCK) {
        // Internal snare mount block on back panel (option B)
        color("burlywood", 0.85)
        translate([H - 2, W/2 - 0.5, D - BACK_T - 1.0])
            rotate([0, 8, 0])  // 8-degree angle off vertical
                cube([1.0, 1.0, 5.0]);
    }
}

// === Render ===

cajon_assembly();

// === Console output (echo to OpenSCAD console) ===

echo(str("Cajón family member: ", MEMBER));
echo(str("Outer dims H x W x D: ", H, " x ", W, " x ", D, " in"));
echo(str("Sound hole diameter: ", HOLE, " in"));
echo(str("Internal cavity volume: ", cavity_volume(), " in^3"));
echo(str("Body thickness: ", BT, " in; Back: ", BACK_T, " in; Tapa: ", TAPA_T, " in (3 mm)"));
echo("Cross-check vs cajon-design-table.xlsx — values must agree.");
