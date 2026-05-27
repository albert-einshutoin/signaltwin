# Phase 11 Test Plan

## Narrow Commands

```bash
pytest tests/test_adapter_registry.py tests/test_adapter_cli.py -v
```

Expected:

- adapter registry resolves all fixture adapters
- config loads all fixture source definitions
- CLI inspection emits schema-validated adapter outputs
- invalid adapter config and fixture errors are user-readable

## Phase Regression

```bash
pytest
python -m signaltwin.cli adapter inspect --config configs/adapter-fixtures.yml
```

Expected:

- `pytest` exits 0
- CLI exits 0
- CLI output includes all normalized keys
