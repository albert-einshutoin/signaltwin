# Task 03: Error Messages

Status: done

## Goal

Make loader failures actionable so later CLI errors are not vague.

## Domain Boundary

This task owns error wrapping and messages. It does not own CLI formatting.

## Files

- Modify `src/signaltwin/scenario_loader.py`
- Modify `tests/test_scenario_loader.py`

## TDD Checklist

- [ ] RED: write `test_missing_scenario_path_reports_path`.
- [ ] RED: write `test_invalid_scenario_reports_validation_section`.
- [ ] Verify RED:

```bash
pytest tests/test_scenario_loader.py::test_missing_scenario_path_reports_path tests/test_scenario_loader.py::test_invalid_scenario_reports_validation_section -v
```

Expected failure:

- generic exception or missing custom error

- [ ] GREEN: add `ScenarioLoadError` with path and cause text.
- [ ] Verify GREEN:

```bash
pytest tests/test_scenario_loader.py::test_missing_scenario_path_reports_path tests/test_scenario_loader.py::test_invalid_scenario_reports_validation_section -v
```

Expected:

- error message includes the file path and failed section

## Done Criteria

- CLI can reuse loader errors without losing detail.

## Regression Verification

Run the Phase 2 regression command from `tasks/phase2/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/scenario_loader.py tests/test_scenario_loader.py
git commit -m "feat: report scenario load errors"
```
