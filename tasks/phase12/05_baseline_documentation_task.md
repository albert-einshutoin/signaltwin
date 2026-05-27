# Task 05: Baseline Documentation

Status: done

## Goal

Document baseline and repeated measurement comparison before real devices exist.

## Domain Boundary

This task owns docs only.

## Files

- Modify `docs/architecture.md`
- Create `docs/baseline-and-comparison.md`
- Modify `tests/test_drift_comparison.py`

## TDD Checklist

- [x] RED: write `test_baseline_docs_explain_fixture_based_comparison`.
- [x] Verify RED.
- [x] GREEN: document baseline snapshot, comparison, and hardware-free workflow.
- [x] Verify GREEN.

## Done Criteria

- Docs distinguish baseline comparison from risk scoring.
- Docs state fixture outputs can be used before hardware.
- Docs define when real baseline collection starts.

## Regression Verification

Run the Phase 12 regression command from `tasks/phase12/phase_test.md`.
