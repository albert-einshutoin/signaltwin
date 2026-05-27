# Phase 0 Test Plan

## Narrow Commands

```bash
pytest tests/test_project_baseline.py -v
```

Expected:

- package import test passes
- scenario fixture discovery test passes
- generated output directory convention test passes

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
- no warnings caused by project setup

## Manual Checks

```bash
find scenarios -maxdepth 1 -name '*.yml' | sort
find outputs -maxdepth 2 -type f | sort
```

Expected:

- all existing scenario fixtures are still present
- generated outputs are separated under `outputs/generated/`
