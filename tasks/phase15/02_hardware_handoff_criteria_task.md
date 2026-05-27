# Task 02: Hardware Handoff Criteria

Status: done

## Goal

Define the exact criteria for expanding real hardware tasks.

## Domain Boundary

This task owns handoff criteria only. It does not create real hardware implementation tasks.

## Files

- Create `tasks/hardware-handoff.md`
- Modify `tests/test_pre_hardware_readiness.py`

## TDD Checklist

- [x] RED: write `test_hardware_handoff_requires_selected_device_path`.
- [x] Verify RED.
- [x] GREEN: document hardware handoff criteria.
- [x] Verify GREEN.

## Done Criteria

- Handoff requires selected first hardware path.
- Handoff requires expected raw output sample or official program output shape.
- Handoff requires acceptance criteria for replacing fixture adapter with real adapter.
- Final hardware task expansion remains deferred.

## Regression Verification

Run the Phase 15 regression command from `tasks/phase15/phase_test.md`.
