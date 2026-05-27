# SignalTwin Minimal MVP Completion Report

## Current Target

Complete the minimal MVP: a hardware-free Scenario Engine that turns YAML scenarios into explainable risk reports, maintenance reports, and RoomCI scenarios.

## Completion Summary

The minimal MVP is complete.

The project now has:

- project baseline verification
- schema contracts
- scenario loading and normalization
- rule-based risk engine
- deterministic exporters
- CLI validate and run commands
- MVP readiness verification
- README usage documentation
- proposal-ready documentation and generated example reports

## Phase Board

This table records the original minimal MVP closeout through Phase 6. Current pre-hardware status continues in the addendum below and in `../../tasks/status.md`.

| Phase | Status | Exit Evidence |
|---|---|---|
| Phase 0: Project Baseline | done | pytest passed with 3 tests; package import, scenario fixture inventory, and generated output convention verified. |
| Phase 1: Schema Contracts | done | `pytest tests/test_project_baseline.py tests/test_schema_contracts.py -v` passed with 9 tests; scenario and report contracts verified. |
| Phase 2: Scenario Loading And Normalization | done | pytest passed with 32 tests; all scenario fixtures load and normalize into BMS/signal frames with asset/building metadata. |
| Phase 3: Risk Engine | done | pytest passed with 32 tests; rule-based scores do not depend on expected labels and recommendations are verified for all fixtures. |
| Phase 4: Exporters | done | pytest passed with 32 tests; JSON, Markdown, and RoomCI exports validate deterministically. |
| Phase 5: CLI Flow | done | pytest passed with 39 tests; CLI validate/run commands write deterministic outputs and report errors without tracebacks. |
| Phase 6: MVP Readiness | done | pytest passed with 41 tests; all scenarios validate, E2E output check passes, and README usage is documented. |

## Pre-Hardware Addendum

After the minimal MVP closeout, SignalTwin added the hardware-free Adapter-ready MVP and pre-hardware productization layers:

- Phase 7-10: adapter contracts, raw fixture contracts, fixture adapters, and adapter-to-risk E2E regression
- Phase 11: config-driven adapter registry and `adapter inspect` CLI
- Phase 12: fixture baseline snapshots and deterministic drift comparison
- Phase 13: no-hardware demo pipeline
- Phase 14: static API response and dashboard view model contracts
- Phase 15: pre-hardware readiness and hardware handoff criteria

Current full-suite verification is tracked in `../../tasks/status.md`.

## Global Verification Commands

Run these commands after each phase once tooling exists:

```bash
pytest
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

Expected result:

```txt
pytest exits 0
validate exits 0 for valid fixtures
run exits 0 and writes deterministic output files
```

## Current Minimal MVP Capability

SignalTwin can now turn this:

```txt
YAML Scenario
```

into this:

```txt
Normalized BMS Frames
Normalized Signal Frames
Asset / Building Metadata
Risk Scores
Evidence
Maintenance Recommendation
JSON Report
Markdown Report
RoomCI Scenario
```

## What Is In Scope

The minimal MVP includes:

- mock/scenario-first workflow
- YAML scenario input
- normalized BMS context
- normalized mock signal frames
- rule-based risk scoring
- deterministic outputs
- CLI commands
- explainable evidence
- RoomCI scenario export

## What Is Out of Scope

The following are intentionally outside the minimal MVP:

- hardware adapters
- real ESP32 CSI input
- PZT ADC input
- thermal camera input
- visual camera input
- acoustic microphone input
- dashboard
- FastAPI
- Streamlit
- SQLite persistence
- PyOD / ML scoring
- real sensor calibration
- real BMS integration

## Decision Log

- Minimal MVP is mock/scenario-first and does not require hardware.
- BMS data remains input context.
- SignalTwin owns interpretation, risk scoring, evidence, and exports.
- Scenario-provided signal values are treated as minimal MVP mock signal frames.
- Normalization converts scenario YAML into internal frames before risk scoring.
- Risk rules must not parse raw YAML dictionaries.
- Rule-based explainability is required before optional PyOD or ML work.
- Hardware adapters, dashboard, FastAPI, Streamlit, SQLite, and real sensors are outside the minimal MVP.

## MVP Completion Assessment

| Area | Status |
|---|---|
| Minimal MVP | Complete |
| Proposal-ready docs | Complete |
| Hardware PoC | Not started |
| Adapter interface | Next phase |
| NOT A HOTEL proposal readiness | Ready for review |

## Recommended Next Phase

```txt
Phase 7-10: Adapter-ready MVP
```

Deliverables:

- adapter-contract.md
- base adapter interface
- device I/O assumptions document
- raw BMS, WiFi CSI, thermal, visual, acoustic, and PZT fixtures
- CSV/JSON fixture adapters
- adapter contract tests
- adapter-to-risk regression
- proof that existing Scenario Engine tests remain green

The Adapter-ready MVP keeps hardware optional. Hardware is still not required:
fixture adapters validate the I/O boundary first, and the first real hardware PoC
should be selected after adapter-ready regression evidence is green.

## No-Hardware Demo Command

```bash
python -m signaltwin.cli demo --output-dir outputs/demo
```

No hardware is required. The command regenerates adapter inspection, drift comparison, risk report, maintenance report, and RoomCI scenario outputs for proposal review.

## Pre-hardware Readiness

Pre-hardware readiness means the no-hardware work is complete: minimal scenario engine, Adapter-ready MVP, adapter registry, baseline comparison, no-hardware demo, and API/dashboard contracts are all covered by tests and deterministic artifacts.

This does not claim real sensor validation. Hardware PoC awaits a selected device path and a raw output sample before real adapter tasks are expanded.
