# Task 04: Comparison Report Export

Status: done

## Goal

Export drift comparison summaries for demo and review use.

## Domain Boundary

This task owns comparison output formatting only.

## Files

- Modify `src/signaltwin/comparison.py`
- Modify `tests/test_drift_comparison.py`

## TDD Checklist

- [x] RED: write `test_comparison_summary_exports_markdown`.
- [x] RED: write `test_comparison_summary_exports_json_payload`.
- [x] Verify RED.
- [x] GREEN: implement summary export helpers.
- [x] Verify GREEN.

## Done Criteria

- Markdown summary is deterministic.
- JSON payload is deterministic.
- Summary does not require hardware or dashboard.

## Regression Verification

Run the Phase 12 regression command from `tasks/phase12/phase_test.md`.
