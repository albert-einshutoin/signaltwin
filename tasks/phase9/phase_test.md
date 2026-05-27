# Phase 9 Test Plan

## Narrow Commands

```bash
pytest tests/test_fixture_adapters.py -v
```

Expected:

- all fixture adapters parse raw fixture files
- normalized payloads contain expected SignalTwin frame keys
- invalid fixture errors are user-readable
- adapter outputs are schema-validated before leaving adapter modules

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
