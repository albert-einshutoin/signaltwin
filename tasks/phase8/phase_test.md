# Phase 8 Test Plan

## Narrow Commands

```bash
pytest tests/test_raw_fixture_contracts.py -v
```

Expected:

- raw fixture files exist
- CSV/JSON fixtures parse
- required raw columns/keys are present

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
