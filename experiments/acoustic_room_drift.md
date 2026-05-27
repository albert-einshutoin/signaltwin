# Experiment: Acoustic Room Drift

## Purpose

Validate whether room state changes appear in acoustic impulse response and frequency response.

## Changes to Test

- Door open vs closed
- Curtain open vs closed
- Furniture moved
- Soft material added
- Window seal partially open

## Inputs

- Sweep signal
- Recorded PCM
- RT60
- Frequency response
- Baseline similarity

## Expected Features

- RT60 change
- Low-frequency resonance shift
- High-frequency absorption delta
- Door/window leak score

## Output

- acoustic_response_drift
- room_resonance_change
- door_seal_leak_hint
