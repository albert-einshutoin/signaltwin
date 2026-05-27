# Task 04: Adapter CLI Error Handling

Status: done

## Goal

Ensure adapter CLI failures are concise and do not expose tracebacks.

## Domain Boundary

This task owns CLI error behavior only.

## Files

- Modify `src/signaltwin/cli.py`
- Modify `tests/test_adapter_cli.py`

## TDD Checklist

- [x] RED: write `test_adapter_inspect_cli_reports_invalid_config_without_traceback`.
- [x] RED: write `test_adapter_inspect_cli_reports_adapter_error_without_traceback`.
- [x] Verify RED with the narrow tests.
- [x] GREEN: implement concise error handling.
- [x] Verify GREEN with the same tests.

## Done Criteria

- Invalid config exits non-zero.
- Adapter failure exits non-zero.
- Output includes path/source context.
- Output does not include `Traceback`.

## Regression Verification

Run the Phase 11 regression command from `tasks/phase11/phase_test.md`.
