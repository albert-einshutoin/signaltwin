# SignalTwin Proposal Pack

This package contains proposal-ready documentation for the SignalTwin Minimal MVP.

SignalTwin is a hardware-free Building Health Forecast Scenario Engine that turns BMS context and mock non-BMS signal frames into explainable risk reports, maintenance recommendations, and RoomCI scenarios.

## Contents

```txt
docs/
  concept.md
  not-a-hotel-proposal.md
  mvp-completion-report.md
  next-phase-adapter-plan.md
  signal-io-roadmap.md

examples/
  reports/
    rainy_season_wood_wall.report.md
    coastal_villa_moss_risk.report.md
    communication_drift.report.md
    hvac_efficiency_drift.report.md
```

## Current Minimal MVP Status

The minimal MVP is complete as a hardware-free Scenario Engine.

It validates YAML scenarios, normalizes BMS and mock signal frames, scores building health risks with explainable rule-based logic, and exports deterministic JSON, Markdown, and RoomCI scenario outputs.

## Sync Status

This proposal pack is synchronized with the current minimal MVP implementation.

- Example reports under `examples/reports/` are generated from the current `signaltwin` exporter.
- The completion report reflects the current Phase 0-6 task board.
- Adapter-ready MVP work is now defined as a hardware-free fixture adapter stage.
- Hardware is still not required for adapter contract and fixture adapter validation.
- Real hardware adapters, dashboard/API, persistence, and ML remain later work.

## Adapter-ready MVP Status

The Adapter-ready MVP uses fixture adapters to validate I/O boundaries before hardware is selected.

Current fixture adapters cover BMS, WiFi CSI, thermal, visual, acoustic, and PZT source families. The target proof is that raw fixtures can become schema-validated adapter outputs and reach the existing risk engine without hardware-specific dependencies.

## No-Hardware Demo

Run the complete no-hardware demo:

```bash
python -m signaltwin.cli demo --output-dir outputs/demo
```

No hardware is required. The demo regenerates adapter inspection, drift comparison, risk report, maintenance report, and RoomCI scenario outputs from fixture adapters.
