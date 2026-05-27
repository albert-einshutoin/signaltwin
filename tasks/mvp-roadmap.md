# SignalTwin MVP Roadmap

## Current State

Phase 0-6 completed the minimal MVP:

```txt
Scenario YAML
  -> schema validation
  -> BMS / mock signal normalization
  -> rule-based risk engine
  -> evidence and recommendation
  -> JSON / Markdown / RoomCI exports
  -> CLI validate / run
```

This is complete without hardware.

## No-Hardware Adapter-Ready MVP

The next MVP should assume target devices, but must not depend on having them physically connected.

Purpose:

- lock raw I/O contracts for likely devices
- keep devices replaceable through adapter boundaries
- parse fixture files that imitate device output
- convert raw fixture data into the existing normalized SignalTwin frames
- prove the existing risk engine stays unchanged

The source of truth for assumed devices, capture programs, raw fixture files, and normalized targets is `docs/device-io-assumptions.md`.

Assumed device families:

| Signal | Default Assumption | Replaceable By |
|---|---|---|
| BMS context | CSV / JSON export | BMS API, time-series DB export |
| WiFi CSI | ESP32-CSI-Tool / esp-csi CSV-like output | RuView-like output, other CSI capture tools |
| Thermal | MLX90640 32x24 matrix fixture | MLX90641, FLIR, other thermal matrix sources |
| Visual | camera image + defect JSON | Pi Camera, USB camera, smartphone photo, manual labels |
| Acoustic | WAV/feature JSON fixture from INMP441-like capture | USB mic, other I2S mic |
| PZT | ADC CSV fixture from PZT + ADS1115-like capture | other ADC/DAQ, higher-speed hardware |

Design rule:

```txt
raw device fixture
  -> adapter parser
  -> schema-validated adapter output
  -> normalized SignalTwin frame bundle
  -> existing risk engine
```

The risk engine must not know which device produced a frame.

Adapter-ready completion requires more than parsing fixtures. Phase 10 must prove
that adapter outputs can be composed into a normalized SignalTwin scenario and
passed through the existing risk engine without importing adapter modules from
the risk layer.

## Final MVP

The final hardware MVP is intentionally not planned as implementation tasks yet.
Phase 15 completed the pre-hardware closeout, so the next planning trigger is a
selected first hardware path and its concrete I/O evidence.

Likely final MVP capabilities:

- real BMS CSV/API adapter
- at least one real non-BMS sensor adapter
- baseline store
- repeated measurement comparison
- dashboard or API
- field PoC report
- clear hardware setup docs

Do not create full implementation tasks for this yet. Use the completed
pre-hardware artifacts and `tasks/hardware-handoff.md` to decide which real
adapter is worth connecting first.

## Next Phase Boundary

Completed no-hardware Adapter-ready phases:

- Phase 7: Adapter Contract Planning
- Phase 8: Raw I/O Fixture Contracts
- Phase 9: Fixture Adapter Implementation
- Phase 10: Adapter-Ready MVP Readiness

Additional pre-hardware productization phases:

- Phase 11: Adapter Registry And CLI Operations
- Phase 12: Baseline Store And Drift Comparison
- Phase 13: No-Hardware Demo Pipeline
- Phase 14: Mock API And Dashboard Contract
- Phase 15: Pre-Hardware Readiness Closeout

These phases are complete and executable without hardware. Real device wiring
should start only after the first hardware path is selected, so the first
hardware PoC only needs adapter replacement and fixture-to-real I/O validation.
