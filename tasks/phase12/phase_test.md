# Phase 12 Test Plan

## Narrow Commands

```bash
pytest tests/test_baseline_store.py tests/test_drift_comparison.py -v
```

Expected:

- baseline snapshots serialize deterministically
- baseline load errors are user-readable
- drift comparison identifies changed fields
- comparison output is stable

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
