# Task 01: Baseline Snapshot Model

Status: done

## Goal

Create a baseline snapshot model from schema-validated adapter outputs.

## Domain Boundary

This task owns in-memory baseline modeling only.

## Files

- Create `src/signaltwin/baseline.py`
- Create `tests/test_baseline_store.py`

## TDD Checklist

- [x] RED: write `test_baseline_snapshot_from_adapter_outputs`.
- [x] RED: write `test_baseline_snapshot_requires_baseline_id`.
- [x] Verify RED.
- [x] GREEN: implement baseline snapshot primitives.
- [x] Verify GREEN.

## Done Criteria

- Snapshot includes `baseline_id`, timestamp, BMS payload, and signal payloads.
- Snapshot does not include risk report fields.
- Snapshot can be created from fixture adapter outputs.

## Regression Verification

Run the Phase 12 regression command from `tasks/phase12/phase_test.md`.
