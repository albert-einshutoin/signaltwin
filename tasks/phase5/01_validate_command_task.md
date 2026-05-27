# Task 01: Validate Command

Status: done

## Goal

Add a CLI command that validates a scenario without producing reports.

## Domain Boundary

This task owns validation CLI behavior only.

## Files

- Create `src/signaltwin/cli.py`
- Create `tests/test_cli.py`

## TDD Checklist

- [ ] RED: write `test_validate_command_accepts_valid_scenario`.
- [ ] Verify RED:

```bash
pytest tests/test_cli.py::test_validate_command_accepts_valid_scenario -v
```

Expected failure:

- missing CLI module or command

- [ ] GREEN: implement Typer app with `validate`.
- [ ] Verify GREEN:

```bash
pytest tests/test_cli.py::test_validate_command_accepts_valid_scenario -v
```

Expected:

- exit code 0
- output includes scenario name

## Done Criteria

- Validation command does not write files.

## Regression Verification

Run the Phase 5 regression command from `tasks/phase5/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/cli.py tests/test_cli.py
git commit -m "feat: add scenario validate command"
```
