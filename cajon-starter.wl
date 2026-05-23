(* ::Package:: *)

(* Cajón Family — Acoustic Physics Starter
   Heifer Zephyr Instruments — Tony Koop
   Open in Wolfram Desktop or Wolfram Cloud
   Models the two co-dominant bass voices of the cajón:
     1. Front-plate (1,1) clamped-rectangular bending mode (tapa)
     2. Helmholtz cavity coupled to a back-port hole
   Plus the slap-zone two-zone tone model.
*)

(* === Inputs (edit me) === *)

(* Family geometry, inches *)
hStandard = 18;
wStandard = 12;
dStandard = 12;
bodyT     = 0.75;
backT     = 0.5;
holeD     = 4.5;
tapaT     = 0.118; (* 3 mm Baltic birch *)
topT      = 0.75;

hCompact = 15; wCompact = 11; dCompact = 11; holeDC = 4.0; bodyTC = 0.625;
hBass    = 22; wBass    = 14; dBass    = 14; holeDB = 5.0;

(* Air properties *)
cAir = 343 * 39.3701; (* speed of sound, in/s — 13507 in/s *)

(* Baltic birch ply elastic properties (isotropic approximation) *)
ETapa  = 8.0 * 10^9; (* Pa *)
rhoTapa = 680;       (* kg/m^3 *)
nuTapa = 0.30;

(* === Helmholtz frequency of the back-ported cavity === *)

(* L_eff = back panel thickness + 1.7*r end correction (flush thin-wall orifice) *)
helmFreq[H_, W_, D_, bT_, backTh_, holeDia_] := Module[
  {Vol, Area, Leff},
  Vol  = (W - 2*bT) * (D - 2*bT) * (H - topT - backTh);
  Area = Pi * (holeDia/2)^2;
  Leff = backTh + 1.7 * (holeDia/2);
  cAir / (2*Pi) * Sqrt[Area / (Vol * Leff)]
]

fHStd  = helmFreq[hStandard, wStandard, dStandard, bodyT,  backT, holeD]
fHComp = helmFreq[hCompact,  wCompact,  dCompact,  bodyTC, backT, holeDC]
fHBass = helmFreq[hBass,     wBass,     dBass,     bodyT,  backT, holeDB]

(* Workbook-as-shipped (uncorrected) Helmholtz — for traceability of risks.md A2 *)
helmFreqUncorrected[H_, W_, D_, bT_, backTh_, holeDia_] := Module[
  {Vol, Area, Leff},
  Vol = (W - 2*bT) * (D - 2*bT) * (H - topT - backTh);
  Area = Pi * (holeDia/2)^2;
  Leff = backTh; (* the bug — no 1.7r end correction *)
  cAir / (2*Pi) * Sqrt[Area / (Vol * Leff)]
]

fHStdBuggy = helmFreqUncorrected[hStandard, wStandard, dStandard, bodyT, backT, holeD]
(* Should print ~282 Hz vs corrected ~96 Hz; diff ratio ~3x *)

(* === Tapa front-plate (1,1) mode (clamped rectangular plate, isotropic) === *)

(* Active span: panel size minus 2x screw-engagement margin (about 0.5") *)
plateFreq11[panelW_, panelH_, h_, E_, rho_, nu_] := Module[
  {a, b, hM, Dr, rhoH},
  a = (panelW - 1) * 0.0254;  (* m, clamp inset 0.5" each edge *)
  b = (panelH - 1) * 0.0254;
  hM = h * 0.0254;
  Dr = E * hM^3 / (12 * (1 - nu^2));
  rhoH = rho * hM;
  (Pi/2) * (1/a^2 + 1/b^2) * Sqrt[Dr / rhoH]
]

fpStd  = plateFreq11[wStandard, hStandard, tapaT, ETapa, rhoTapa, nuTapa]
fpComp = plateFreq11[wCompact,  hCompact,  tapaT, ETapa, rhoTapa, nuTapa]
fpBass = plateFreq11[wBass,     hBass,     tapaT, ETapa, rhoTapa, nuTapa]

(* === Cents conversion === *)

cents[fMeasured_, fPredicted_] := 1200 * Log[2, fMeasured/fPredicted];

(* Example: if you measure Standard cavity at 92 Hz, what's the cents error? *)
exampleStdErr = cents[92, fHStd]

(* === Manipulate: design a cajón family member interactively === *)

Manipulate[
  Module[{fH, fP, Vol, Area, Leff},
    Vol  = (W - 2*bT) * (D - 2*bT) * (H - topT - backTh);
    Area = Pi * (holeDia/2)^2;
    Leff = backTh + 1.7 * (holeDia/2);
    fH = cAir / (2*Pi) * Sqrt[Area / (Vol * Leff)];
    fP = plateFreq11[W, H, tapaThk, ETapa, rhoTapa, nuTapa];
    Column[{
      Style["Cajón cavity + plate predictor", 16, Bold],
      Row[{"Internal volume: ", NumberForm[Vol, {6, 1}], " in\.b3"}],
      Row[{"Sound-hole area: ", NumberForm[Area, {5, 2}], " in\.b2"}],
      Row[{"Effective neck L: ", NumberForm[Leff, {4, 2}], " in"}],
      Row[{Style["Helmholtz f_H: ", Bold], NumberForm[fH, {5, 1}], " Hz"}],
      Row[{Style["Plate (1,1) f_p: ", Bold], NumberForm[fP, {5, 1}], " Hz"}],
      Row[{"Coupling ratio: ", NumberForm[fH/fP, {3, 2}],
        If[Abs[1200*Log[2, fH/fP]] < 200, " (tight — coupled bass)",
          If[Abs[1200*Log[2, fH/fP]] < 500, " (moderate — twin voices)",
            " (loose — cavity dominant)"]]}]
    }]
  ],
  {{H, 18, "Outer height (in)"}, 12, 26, 0.5},
  {{W, 12, "Outer width (in)"}, 9, 16, 0.5},
  {{D, 12, "Outer depth (in)"}, 9, 16, 0.5},
  {{bT, 0.75, "Body thickness (in)"}, 0.5, 1.0, 0.0625},
  {{backTh, 0.5, "Back thickness (in)"}, 0.25, 0.75, 0.0625},
  {{holeDia, 4.5, "Sound hole \[Phi] (in)"}, 3.0, 6.0, 0.1},
  {{tapaThk, 0.118, "Tapa thickness (in)"}, 0.080, 0.200, 0.005}
]

(* === Plate-mode visualizer === *)
(* Modes (m,n) of a clamped rectangular plate — schematic isotropic shapes *)

plateMode[m_, n_, x_, y_] := Sin[m*Pi*x] * Sin[n*Pi*y]
                            * (1 - Cos[2*m*Pi*x]) * (1 - Cos[2*n*Pi*y]) / 4;

GraphicsGrid[
  Partition[
    Table[
      DensityPlot[plateMode[m, n, x, y], {x, 0, 1}, {y, 0, 1},
        ColorFunction -> "TemperatureMap", PlotLabel -> Row[{"(", m, ",", n, ")"}],
        Frame -> False, ImageSize -> 200],
      {m, 1, 3}, {n, 1, 3}
    ], 3
  ]
]

(* === Two-zone strike model (schematic) === *)
(* Centre strike → (1,1)-dominant; corner strike → high modes + snare wires *)

centreStrike[t_] := Exp[-3*t] * Sin[2*Pi*fpStd*t];
cornerStrike[t_] := Exp[-12*t] * (Sin[2*Pi*250*t] + 0.6*Sin[2*Pi*800*t]
                                + 0.3*Sin[2*Pi*2000*t]);

Plot[{centreStrike[t], cornerStrike[t]}, {t, 0, 0.3},
  PlotRange -> All, PlotLegends -> {"Centre (bass)", "Corner (slap)"},
  PlotLabel -> "Two-zone strike envelopes (schematic)"]

(* === Snare-wire coupling, schematic === *)

(* Treat snare as ~3 strings, each clamped against tapa, length ~5",
   tension 5-15 N each *)

snareF[L_, T_, mu_] := (1/(2*L)) * Sqrt[T/mu]
(* L in m; T in N; mu = mass per unit length kg/m *)

(* Example: 0.012" steel guitar string = ~0.0004 kg/m, 5 inch length *)
muG12 = 4 * 10^-4;
snareLen = 0.127; (* 5" in m *)

Table[
  {tension, NumberForm[snareF[snareLen, tension, muG12], {5, 1}]},
  {tension, {2, 5, 10, 15, 25}}  (* N *)
]
(* Reads as a schedule of snare partial frequencies vs tension *)

(* === Notes === *)
Print["Open this notebook in Wolfram Desktop or Cloud to interact with Manipulate."]
Print["First-prototype acceptance: f_H within +/- 15 Hz of fHStd; plate (1,1) within +/- 15% of fpStd."]
Print["Update validation.csv with measured values; recompute cents error here."]
