# Phase 7 Test Plan

## Narrow Commands

```bash
pytest tests/test_adapter_contracts.py -v
```

Expected:

- base adapter contract tests pass
- adapter error message tests pass
- normalized payload contract tests pass
- adapter outputs validate payloads against existing BMS and signal schema models

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
- existing Scenario Engine tests remain green
