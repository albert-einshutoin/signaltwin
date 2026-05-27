# Task 03: Static Example Outputs

Status: done

## Goal

Generate static example API/dashboard payloads for review and future UI work.

## Domain Boundary

This task owns static examples only.

## Files

- Create `outputs/demo/api_response.example.json`
- Create `outputs/demo/dashboard_view_model.example.json`
- Modify `tests/test_api_dashboard_contract.py`

## TDD Checklist

- [x] RED: write `test_static_api_dashboard_examples_match_contract`.
- [x] Verify RED.
- [x] GREEN: generate static examples.
- [x] Verify GREEN.

## Done Criteria

- Example JSON files validate against contract tests.
- Examples are deterministic.
- Examples can be used by future UI/API implementation.

## Regression Verification

Run the Phase 14 regression command from `tasks/phase14/phase_test.md`.
