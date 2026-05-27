# Task 01: All Scenario Regression

Status: done

## Goal

Ensure every sample scenario validates and runs through the complete pipeline.

## Domain Boundary

This task owns regression coverage only. It should not add new MVP behavior unless a failing regression exposes a real gap.

## Files

- Create `tests/test_mvp_regression.py`

## TDD Checklist

- [ ] RED: write `test_all_scenarios_run_to_reports`.
- [ ] Verify RED by running the test before the end-to-end helper exists.

```bash
pytest tests/test_mvp_regression.py::test_all_scenarios_run_to_reports -v
```

Expected failure:

- missing helper, command, or output files

- [ ] GREEN: assert the real output set per scenario.
- [ ] Verify GREEN:

```bash
pytest tests/test_mvp_regression.py::test_all_scenarios_run_to_reports -v
```

Expected:

- all scenarios produce JSON, Markdown, and RoomCI YAML in temporary directories

## Done Criteria

- Adding a new fixture automatically exercises the end-to-end pipeline.

## Regression Verification

Run the Phase 6 regression command from `tasks/phase6/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_mvp_regression.py
git commit -m "test: cover all scenario end-to-end runs"
```
