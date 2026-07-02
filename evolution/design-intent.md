# Design Intent — cajon rev A

- Master CAD: `cad/cajon-master.scad` (sha256: c33970154a3aaa114a9b48958d318e404c76e641e9f412e323f79ac2b02813f1), driven by `Cajon-Family-Design.xlsx` (sha256: d51e6aaaaa010b24bf17f511e03ac4ad37278c9b550844330ec9c4292a9f9eab) and `family-spec.csv`.
- Function: Parametric three-member box-drum family (Compact / Standard / Bass) in four manufacturing variants. A thin plywood front plate (tapa) is struck; its plate (1,1) mode couples with a Helmholtz cavity resonance through a back sound hole to produce bass and slap zones. CJ-S Standard is the first public-review prototype.
- Environment: seated hand-played acoustic box drum; plywood plates move with humidity (tapa stiffness ∝ h³); tapa is screwed (field-replaceable), body panels glued.
- Target qty: 1 (CJ-S Standard prototype first). Deadline: TBD. Budget/unit ceiling: TBD.

## Critical dimensions (carry tolerances)

| Feature | Nominal (CJ-S Standard) | Tolerance | Why critical | Source |
| --- | --- | --- | --- | --- |
| Outer HxWxD | 18.0 x 12.0 x 12.0 in | cut-list gate | seating / cavity volume | family-spec.csv CJ-S |
| Tapa thickness | 3.0 mm BB-grade birch | reject sheets >0.010 in off nominal | plate (1,1) ∝ h^3 → pitch | family-spec.csv / risks SU1 |
| Sound hole diameter | 4.5 in | affects f_H via effective length | Helmholtz tuning | family-spec.csv CJ-S |
| Predicted Helmholtz f_H | ~96 Hz (with 1.7·r end correction) | measure on prototype | bass voice | design.md / risks A2 |
| Predicted plate (1,1) | ~84 Hz | measure on prototype | slap/bass coupling | family-spec.csv CJ-S |
| Body / back thickness | 0.750 / 0.500 in | glue-joint squareness | structure | family-spec.csv CJ-S |

## Incidental (free for DFM)

- Finger-joint vs alternative corner variant, inlay/cosmetic detail, external finish, snare-option lineage (A/B), non-mating surface treatment.

## Must-nots (DFM may never violate)

- Do not use the original `cajon-design-table.xlsx` Helmholtz formula without the `1.7·r` end correction (L_eff = L + 1.7·r) — the uncorrected formula mispredicts f_H badly (risks A2).
- Do not spec non-BB / non-marine-grade ply; layer-adhesion and thickness variance (±8%) shift plate pitch ~15% (risks SU1, A1).
- Do not over-tighten the lower tapa screws — it tenses the slap zone at rest (risks mitigation).
- Do not treat family-spec predicted frequencies as measured — they are pre-build predictions pending CJ-S validation.

## Material intent

- Preferred: BB-grade / marine-grade Baltic birch plywood body and tapa per bom.csv; screwed replaceable tapa.
- Acceptable subs: per sourcing.csv (spec-first; price-volatility flags noted; live prices unverified).
- Forbidden: non-BB-grade plywood for the tapa.

## Stage status

Stage 0 intake complete 2026-07-01. Gate A (Alpha shop compile) NOT yet run — no concessions logged, nothing presented as shippable. Status normalized to L2 V5 build-packet candidate (pre-build; not measured/production-ready).
