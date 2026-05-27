# SignalTwin MVP Status

## Current Target

Track the completed hardware-free MVP layers through Phase 15: Minimal MVP,
Adapter-ready MVP, and pre-hardware readiness closeout.

## Phase Board

| Phase | Status | Exit Evidence |
|---:|---|---|
| Phase 0: Project Baseline | done | `pytest` passed with 3 tests; package import, scenario fixture inventory, and generated output convention verified. |
| Phase 1: Schema Contracts | done | `pytest tests/test_project_baseline.py tests/test_schema_contracts.py -v` passed with 9 tests; scenario and report contracts verified. |
| Phase 2: Scenario Loading And Normalization | done | `pytest` passed with 32 tests; all scenario fixtures load and normalize into BMS/signal frames with asset/building metadata. |
| Phase 3: Risk Engine | done | `pytest` passed with 32 tests; rule-based scores do not depend on `expected` labels and recommendations are verified for all fixtures. |
| Phase 4: Exporters | done | `pytest` passed with 32 tests; JSON, Markdown, and RoomCI exports validate deterministically. |
| Phase 5: CLI Flow | done | `pytest` passed with 39 tests; CLI validate/run commands write deterministic outputs and report errors without tracebacks. |
| Phase 6: MVP Readiness | done | `pytest` passed with 41 tests; all scenarios validate, E2E output check passes, and README usage is documented. |
| Phase 7: Adapter Contract Planning | done | `pytest` passed with 48 tests; adapter contracts, errors, docs, and schema-validated adapter outputs are implemented. |
| Phase 8: Raw I/O Fixture Contracts | done | `pytest` passed with 52 tests; raw BMS, WiFi CSI, thermal, visual, acoustic, and PZT fixture contracts are documented and parseable. |
| Phase 9: Fixture Adapter Implementation | done | `pytest` passed with 73 tests; fixture adapters parse raw files, return schema-validated outputs, and remain isolated from the risk engine. |
| Phase 10: Adapter-Ready MVP Readiness | done | `pytest` passed with 73 tests; adapter outputs compose into a normalized scenario and reach the existing risk engine. |
| Phase 11: Adapter Registry And CLI Operations | done | `pytest` passed with 81 tests; config-driven adapter selection and `adapter inspect` CLI work without hardware. |
| Phase 12: Baseline Store And Drift Comparison | done | `pytest` passed with 91 tests; fixture baseline snapshots, JSON storage, and repeated measurement comparison are implemented. |
| Phase 13: No-Hardware Demo Pipeline | done | `pytest` passed with 96 tests; `python -m signaltwin.cli demo --output-dir outputs/demo` regenerates no-hardware demo artifacts. |
| Phase 14: Mock API And Dashboard Contract | done | `pytest` passed with 100 tests; hardware-free API response and dashboard view model contracts are generated from demo artifacts. |
| Phase 15: Pre-Hardware Readiness Closeout | done | `pytest` passed with 111 tests in current OSS verification; pre-hardware readiness and hardware handoff criteria are documented; final hardware tasks remain unexpanded until a hardware path is selected. |

## Global Verification Commands

Run these after each phase once tooling exists:

```bash
pytest
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

Expected result:

- `pytest` exits 0
- `validate` exits 0 for valid fixtures
- `run` exits 0 and writes deterministic output files

## Decision Log

- Minimal MVP is mock/scenario-first and does not require hardware.
- BMS data remains input context. SignalTwin owns interpretation, risk scoring, evidence, and exports.
- Scenario-provided signal values are treated as the minimal MVP mock signal frames.
- Normalization converts scenario YAML into internal frames before risk scoring; risk rules must not parse raw YAML dictionaries.
- Rule-based explainability is required before optional PyOD or ML work.
- Hardware adapters, dashboard, FastAPI, Streamlit, SQLite, and real sensors are outside the minimal MVP.
- Final hardware MVP tasks are intentionally not expanded yet.
- Phase 7-10 are the no-hardware adapter-ready MVP: assumed devices, fixture I/O, swappable adapters, and regression evidence.
- Adapter-ready MVP requires schema-validated adapter outputs and an adapter-to-risk E2E regression, not only fixture parsing.
- Phase 11-15 are pre-hardware productization tasks and still must not require real sensors, serial ports, GPIO, I2C, camera, microphone, ADC, dashboard hosting, or cloud services.
