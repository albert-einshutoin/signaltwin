# SignalTwin Hardware Handoff

This document defines the entry criteria for expanding real hardware implementation tasks.

## Handoff Rule

Do not expand real hardware implementation tasks until a selected first hardware path is confirmed.

For tooling checks, the rule is: do not expand real hardware implementation tasks.

The selected first hardware path must include:

- target source family
- specific device or system
- expected raw output sample or official program output shape
- adapter replacement plan
- acceptance criteria for replacing fixture adapter with real adapter

## Recommended First Path

Recommended selected first hardware path:

```txt
BMS CSV + Thermal + Visual
```

Rationale:

- BMS CSV is already close to operational building data.
- Thermal and visual evidence are easier to explain for moisture, mold, moss, insulation, and visible degradation.
- WiFi CSI / PZT / Acoustic are valuable but noisier and should follow after the first physical path is stable.

The user can override this recommendation before hardware task expansion.

## Adapter Replacement Acceptance Criteria

A real adapter is acceptable when:

- it can run from a captured raw output sample
- it returns the same `normalized_key` as the fixture adapter
- it returns schema-valid payloads
- it passes equivalent fixture-based tests
- the existing risk engine remains unchanged
- CLI/demo flows still run without hardware when using fixture config

## Deferred Real Hardware Tasks

The following tasks remain intentionally unexpanded:

- ESP32 CSI live capture
- MLX90640 I2C live capture
- camera capture and calibration
- INMP441 or USB microphone capture
- PZT/ADC live capture
- field mounting and calibration

Do not create those implementation tasks until the selected first hardware path and raw output sample are available.
