# Validation Report

**Status:** pre-build validation plan complete; measured prototype data not yet available.

## Current result

The packet is ready for a human shop review before the first physical build. All acoustic values are predictions from the design table and first-order models. No row in `validation.csv` should be read as measured performance until the `measured_value` and `measurement_date` columns are populated.

## Prototype under test

| Field | Value |
|---|---|
| Member | CJ-S Standard |
| Variant | V1 finger joint |
| Snare | Option B, guitar-string snare |
| Body | 3/4 in walnut shell |
| Tapa | 3 mm Baltic birch |
| Back | 1/2 in Baltic birch, 4.5 in sound hole |

## Acceptance gates

| Gate | Target | Pass condition | Current state |
|---|---|---|---|
| Shell squareness | Diagonals matched | Each face diagonal pair within 1/16 in | Pending build |
| Seat load | Static load | 250 lb for 1 hour, no joint opening or new rattle | Pending build |
| Sound hole | 4.500 in diameter | +/-0.020 in, clean deburred edge | Pending build |
| Tapa screw pattern | 3 in perimeter spacing with top slap-zone relief | Holes within +/-0.10 in; upper corners left loose | Pending build |
| Helmholtz response | 96 Hz predicted | Measured within +/-15 Hz or model revised | Pending build |
| Plate (1,1) | 84 Hz predicted | Measured within +/-15 percent or model revised | Pending build |
| Coupled bass | 90 Hz predicted | Perceived bass peak documented | Pending build |
| Slap separation | +5 dB at 1 kHz | Corner strike at least +5 dB vs center strike | Pending build |
| Snare onset | Medium strike | No buzz on light tap, clean buzz on medium slap | Pending build |
| Finish feel | Smooth body, natural tapa | No sticky finish, no film bridging slap zone | Pending build |

## Test sequence

1. Inspect panel thickness, flatness, and squareness before cutting joinery.
2. Dry-fit shell in the square assembly jig and record diagonal measurements.
3. Glue shell, cure 24 hours, then repeat diagonal and rocking checks.
4. Mount tapa with the screw template and a diagonal driving pattern.
5. Run the 250 lb seat-load test before snare tensioning.
6. Record center-tap spectrum, corner-slap spectrum, and T60.
7. Tension snare until the onset target is met.
8. Update `validation.csv` and this report with measured values.

## Preliminary risk read

The design has no measured blocker yet. The highest-risk unknowns are tapa material variation, screw torque uniformity, and snare preload. Those are all controllable during build, which makes this a good fast public candidate after a human verifies the joinery plan and physically builds CJ-S.

## Human review checklist

- Confirm the workbook formula for Helmholtz uses `L_eff = t_back + 1.7*r` before presenting the workbook as final.
- Confirm the square assembly jig can clamp the exact outside dimensions without denting finished faces.
- Confirm tuner hardware does not interfere with the player or with the sound-hole airflow.
- Confirm public photos show the real prototype, not placeholder imagery.
