# Phase 3 Test Plan

## Narrow Commands

```bash
pytest tests/test_risk_engine.py -v
```

Expected:

- risk category tests pass
- evidence tests pass
- recommendation tests pass
- mold and moss risk expectations are both covered

## Phase Regression

```bash
pytest tests/test_project_baseline.py tests/test_schema_contracts.py tests/test_scenario_loader.py tests/test_normalizer.py tests/test_risk_engine.py -v
```

Expected:

- exits 0
