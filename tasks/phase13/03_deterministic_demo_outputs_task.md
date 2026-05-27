# Task 03: Deterministic Demo Outputs

Status: done

## Goal

Ensure demo outputs are deterministic across repeated runs.

## Domain Boundary

This task owns output stability tests only.

## Files

- Modify `tests/test_demo_pipeline.py`
- Create or update `outputs/demo/`

## TDD Checklist

- [x] RED: write `test_demo_outputs_are_deterministic`.
- [x] Verify RED.
- [x] GREEN: stabilize ordering and timestamps where needed.
- [x] Verify GREEN.

## Done Criteria

- Repeated demo runs produce the same file names and stable contents.
- Generated outputs remain reviewable in proposal workflows.

## Regression Verification

Run the Phase 13 regression command from `tasks/phase13/phase_test.md`.
