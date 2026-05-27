# Task 02: JSON Baseline Store

Status: done

## Goal

Persist baseline snapshots to deterministic JSON.

## Domain Boundary

This task owns JSON save/load only.

## Files

- Modify `src/signaltwin/baseline.py`
- Create `baselines/adapter_fixture_baseline.json`
- Modify `tests/test_baseline_store.py`

## TDD Checklist

- [x] RED: write `test_baseline_store_round_trips_json`.
- [x] RED: write `test_baseline_store_reports_invalid_json`.
- [x] Verify RED.
- [x] GREEN: implement JSON save/load.
- [x] Verify GREEN.

## Done Criteria

- JSON output is deterministic.
- Invalid baseline files raise user-readable errors.
- Stored baseline uses only adapter-normalized payloads.

## Regression Verification

Run the Phase 12 regression command from `tasks/phase12/phase_test.md`.
