# Phase 4 Test Plan

## Narrow Commands

```bash
pytest tests/test_exporters.py -v
```

Expected:

- JSON exporter test passes
- Markdown exporter test passes
- RoomCI exporter test passes

## Phase Regression

```bash
pytest tests/test_project_baseline.py tests/test_schema_contracts.py tests/test_scenario_loader.py tests/test_normalizer.py tests/test_risk_engine.py tests/test_exporters.py -v
```

Expected:

- exits 0
