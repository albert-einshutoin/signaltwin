# Phase 1 Test Plan

## Narrow Commands

```bash
pytest tests/test_schema_contracts.py -v
```

Expected:

- valid scenario dictionaries pass
- malformed scenario dictionaries fail
- output report contract tests pass

## Phase Regression

```bash
pytest tests/test_project_baseline.py tests/test_schema_contracts.py -v
```

Expected:

- exits 0
- no loader, exporter, or risk engine dependency is required
