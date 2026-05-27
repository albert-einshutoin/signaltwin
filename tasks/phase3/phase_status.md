# Phase 3 Status: Risk Engine

Status: done

## Tasks

| Task | Status | Evidence |
|---|---|---|
| 01 Moisture Risk | done | `pytest tests/test_risk_engine.py::test_rainy_season_wall_has_high_moisture_risk -v` passed. |
| 02 Mold Moss Risk | done | `pytest tests/test_risk_engine.py::test_coastal_villa_visual_moss_drives_moss_risk -v` passed. |
| 03 Structural Drift Risks | done | `pytest tests/test_risk_engine.py::test_pzt_and_visual_crack_create_structural_drift_evidence -v` passed. |
| 04 Communication And Comfort Risks | done | Communication drift and HVAC comfort degradation tests passed. |
| 05 Recommendation Policy | done | Recommendation parametrized tests passed for moisture, communication, and HVAC fixtures. |

## Blockers

- None.

## Phase Evidence

- `pytest tests/test_risk_engine.py -v` passed with 10 tests.
- `pytest tests/test_project_baseline.py tests/test_schema_contracts.py tests/test_scenario_loader.py tests/test_normalizer.py tests/test_risk_engine.py -v` passed with 29 tests.
- `pytest` passed with 32 tests after Phase 4 regression.
- All scenario fixtures produce bounded scores, evidence, and a recommendation.
- Risk scores do not depend on `expected` labels.
