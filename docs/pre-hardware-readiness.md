# SignalTwin Pre-Hardware Readiness

This document closes the no-hardware development track before real device implementation tasks are expanded.

## Readiness Checklist

| Area | Status | Evidence |
|---|---|---|
| Minimal MVP | done | Scenario YAML to risk report, maintenance report, and RoomCI scenario. |
| Adapter-ready MVP | done | Raw fixtures become schema-validated adapter outputs and reach the existing risk engine. |
| Adapter Registry | done | Adapter config and `adapter inspect` CLI switch fixture sources without hardware. |
| Baseline Store | done | Fixture adapter outputs can be stored as baseline snapshots and compared with current snapshots. |
| No-Hardware Demo Pipeline | done | `python -m signaltwin.cli demo --output-dir outputs/demo` regenerates demo artifacts. |
| Mock API And Dashboard Contract | done | API response and dashboard view model examples are generated without starting a server. |

## Deferred Work

The following work is intentionally deferred until a hardware path is selected:

- real device wiring
- serial, GPIO, I2C, camera, microphone, and ADC capture
- real sensor calibration
- field baseline collection
- physical drift validation
- dashboard/runtime service deployment

This is the hardware-required work boundary.

## Final No-Hardware Position

No-hardware work is complete when tests pass, demo artifacts regenerate, and `tasks/hardware-handoff.md` identifies the selected first hardware path.

The current recommended first path is BMS CSV + Thermal + Visual because it gives the fastest building-health evidence with the lowest signal-processing risk. WiFi CSI / PZT / Acoustic should follow after the first physical path is stable.
