# Phase 13 Test Plan

## Narrow Commands

```bash
pytest tests/test_demo_pipeline.py -v
```

Expected:

- demo runner writes expected outputs
- demo output is deterministic
- demo command does not require hardware

## Phase Regression

```bash
pytest
python -m signaltwin.cli demo --output-dir outputs/demo
```

Expected:

- `pytest` exits 0
- demo command exits 0
- demo output includes adapter inspection, drift comparison, risk report, maintenance report, and RoomCI scenario
