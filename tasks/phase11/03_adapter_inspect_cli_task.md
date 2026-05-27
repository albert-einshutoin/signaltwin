# Task 03: Adapter Inspect CLI

Status: done

## Goal

Expose fixture adapter inspection through CLI so users can verify I/O without hardware.

## Domain Boundary

This task owns CLI inspection only. It does not run risk scoring.

## Files

- Modify `src/signaltwin/cli.py`
- Create `tests/test_adapter_cli.py`

## TDD Checklist

- [x] RED: write `test_adapter_inspect_cli_outputs_normalized_keys`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_cli.py::test_adapter_inspect_cli_outputs_normalized_keys -v
```

Expected failure:

- CLI command is missing

- [x] GREEN: implement `adapter inspect --config configs/adapter-fixtures.yml`.
- [x] Verify GREEN with the same command.

## Done Criteria

- CLI output includes source name, normalized key, and payload summary.
- CLI does not calculate risk.
- No hardware is required.

## Regression Verification

Run the Phase 11 regression command from `tasks/phase11/phase_test.md`.
