# Task 03: CLI Error Handling

Status: done

## Goal

Make CLI failures precise and non-zero.

## Domain Boundary

This task owns CLI error presentation only.

## Files

- Modify `src/signaltwin/cli.py`
- Modify `tests/test_cli.py`

## TDD Checklist

- [ ] RED: write `test_validate_command_reports_missing_file`.
- [ ] RED: write `test_run_command_reports_invalid_scenario`.
- [ ] Verify RED:

```bash
pytest tests/test_cli.py::test_validate_command_reports_missing_file tests/test_cli.py::test_run_command_reports_invalid_scenario -v
```

Expected failure:

- command crashes with traceback or exits 0

- [ ] GREEN: catch `ScenarioLoadError` and show concise path-aware error text.
- [ ] Verify GREEN:

```bash
pytest tests/test_cli.py::test_validate_command_reports_missing_file tests/test_cli.py::test_run_command_reports_invalid_scenario -v
```

Expected:

- non-zero exit code
- output includes failed path or section

## Done Criteria

- User-facing CLI errors do not require reading a Python traceback.

## Regression Verification

Run the Phase 5 regression command from `tasks/phase5/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/cli.py tests/test_cli.py
git commit -m "feat: handle cli scenario errors"
```
