# Phase 2 Test Plan

## Narrow Commands

```bash
pytest tests/test_scenario_loader.py -v
pytest tests/test_normalizer.py -v
```

Expected:

- all sample scenarios load
- BMS and signal inputs normalize into internal frames
- absent optional signal groups normalize to empty or `None` without exceptions
- missing file test passes
- invalid YAML/schema test passes

## Phase Regression

```bash
pytest tests/test_project_baseline.py tests/test_schema_contracts.py tests/test_scenario_loader.py tests/test_normalizer.py -v
```

Expected:

- exits 0
