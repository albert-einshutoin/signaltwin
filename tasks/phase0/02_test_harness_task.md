# Task 02: Test Harness

Status: done

## Goal

Add fixture discovery tests so existing scenarios are treated as regression inputs from the start.

## Domain Boundary

This task verifies repository shape only. It does not parse YAML or validate scenario schemas.

## Files

- Modify `tests/test_project_baseline.py`

## TDD Checklist

- [ ] RED: add `test_repository_contains_minimal_mvp_scenarios`.
- [ ] Verify RED by temporarily expecting a fixture name that does not exist.

```bash
pytest tests/test_project_baseline.py::test_repository_contains_minimal_mvp_scenarios -v
```

Expected failure:

- assertion shows the missing fixture name

- [ ] GREEN: assert the actual fixture set:

```txt
coastal_villa_moss_risk.yml
communication_drift.yml
hvac_efficiency_drift.yml
rainy_season_wood_wall.yml
```

- [ ] Verify GREEN:

```bash
pytest tests/test_project_baseline.py::test_repository_contains_minimal_mvp_scenarios -v
```

Expected:

- test passes

## Done Criteria

- Scenario fixture names are locked by a fast test.
- The test fails clearly if a required sample scenario is removed or renamed.

## Regression Verification

Run the Phase 0 regression command from `tasks/phase0/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_project_baseline.py
git commit -m "test: lock scenario fixture inventory"
```
