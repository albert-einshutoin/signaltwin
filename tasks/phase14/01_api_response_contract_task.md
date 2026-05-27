# Task 01: API Response Contract

Status: done

## Goal

Define a stable API response payload for no-hardware demo results.

## Domain Boundary

This task owns data contract only. It does not start a web server.

## Files

- Create `src/signaltwin/api_contract.py`
- Create `tests/test_api_dashboard_contract.py`

## TDD Checklist

- [x] RED: write `test_api_response_contract_contains_risk_and_adapter_sections`.
- [x] Verify RED.
- [x] GREEN: implement API response contract builder.
- [x] Verify GREEN.

## Done Criteria

- Contract includes adapter status, risk report summary, evidence, recommendation, and generated output paths.
- Contract is serializable to JSON.

## Regression Verification

Run the Phase 14 regression command from `tasks/phase14/phase_test.md`.
