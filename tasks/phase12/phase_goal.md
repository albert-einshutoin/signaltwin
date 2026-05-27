# Phase 12 Goal: Baseline Store And Drift Comparison

## Goal

Add file-backed baseline snapshots and repeated measurement comparison using fixture adapter outputs.

## Scope

- baseline snapshot model
- JSON baseline store
- current-vs-baseline comparison
- drift summary output
- tests proving no hardware is required

## Non-Goals

- No SQLite yet
- No long-term database migration
- No real sensor capture
- No ML/anomaly scoring
- No risk rule rewrite

## Expected Files

- Create `src/signaltwin/baseline.py`
- Create `src/signaltwin/comparison.py`
- Create `baselines/adapter_fixture_baseline.json`
- Create `tests/test_baseline_store.py`
- Create `tests/test_drift_comparison.py`
- Modify `docs/architecture.md`

## Done Criteria

- Baseline snapshots can be created from adapter outputs.
- Baselines can be saved and loaded deterministically as JSON.
- Current fixture outputs can be compared to a baseline.
- Comparison output can feed demo/report layers without requiring hardware.
