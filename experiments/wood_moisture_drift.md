# Experiment: Wood Moisture Drift

## Purpose

Validate whether moisture changes in wood appear as measurable drift in PZT, acoustic, thermal, and WiFi CSI features.

## Test Objects

- Dry cedar board
- Moist cedar board
- Re-dried cedar board

## Inputs

- BMS mock humidity and temperature
- PZT response
- Acoustic sweep response
- Thermal matrix
- WiFi CSI drift
- Optional weight measurement
- Optional commercial moisture meter reading

## Hypothesis

Moisture increase should produce at least some drift in:

- PZT attenuation
- Resonance frequency
- Acoustic response
- Thermal cold spots
- WiFi CSI / multipath features

## Output

- moisture_risk
- mold_risk
- wood_deformation_risk
- evidence list
