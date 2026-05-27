# Task 03: Drift Comparison Engine

Status: done

## Goal

Compare current adapter outputs against a stored baseline.

## Domain Boundary

This task owns deterministic comparison only. It does not calculate final risk scores.

## Files

- Create `src/signaltwin/comparison.py`
- Create `tests/test_drift_comparison.py`

## TDD Checklist

- [x] RED: write `test_comparison_detects_numeric_field_delta`.
- [x] RED: write `test_comparison_ignores_missing_optional_fields`.
- [x] RED: write `test_comparison_groups_results_by_normalized_key`.
- [x] Verify RED.
- [x] GREEN: implement comparison engine.
- [x] Verify GREEN.

## Done Criteria

- Numeric deltas are reported.
- Results are grouped by `bms`, `wifi_csi`, `thermal`, `visual`, `acoustic`, and `pzt`.
- Comparison output is deterministic.

## Regression Verification

Run the Phase 12 regression command from `tasks/phase12/phase_test.md`.
