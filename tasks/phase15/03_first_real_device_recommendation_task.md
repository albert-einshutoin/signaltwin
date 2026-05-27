# Task 03: First Real-Device Recommendation

Status: done

## Goal

Record which first hardware path should be selected after no-hardware work.

## Domain Boundary

This task owns recommendation docs only.

## Files

- Modify `tasks/hardware-handoff.md`
- Modify `docs/pre-hardware-readiness.md`
- Modify `tests/test_pre_hardware_readiness.py`

## TDD Checklist

- [x] RED: write `test_handoff_recommends_first_real_device_path`.
- [x] Verify RED.
- [x] GREEN: recommend `BMS CSV + Thermal + Visual` as first path unless user chooses otherwise.
- [x] Verify GREEN.

## Done Criteria

- Recommendation is explicit.
- Rationale distinguishes easy building-health evidence from higher-noise WiFi/PZT/acoustic work.
- User can override the selected path before hardware task expansion.

## Regression Verification

Run the Phase 15 regression command from `tasks/phase15/phase_test.md`.
