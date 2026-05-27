# Task 02: Dashboard View Model Contract

Status: done

## Goal

Define the data shape a future dashboard needs without implementing the dashboard.

## Domain Boundary

This task owns dashboard view model data only.

## Files

- Modify `src/signaltwin/api_contract.py`
- Modify `tests/test_api_dashboard_contract.py`

## TDD Checklist

- [x] RED: write `test_dashboard_view_model_groups_risks_evidence_and_adapter_status`.
- [x] Verify RED.
- [x] GREEN: implement view model builder.
- [x] Verify GREEN.

## Done Criteria

- View model groups risk scores, evidence, adapter status, baseline comparison, and report links.
- View model is deterministic.
- No frontend runtime is required.

## Regression Verification

Run the Phase 14 regression command from `tasks/phase14/phase_test.md`.
