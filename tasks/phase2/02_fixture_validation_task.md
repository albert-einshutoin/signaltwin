# Task 02: Fixture Validation

Status: done

## Goal

Treat every existing scenario fixture as a contract regression.

## Domain Boundary

This task owns multi-fixture validation only.

## Files

- Modify `tests/test_scenario_loader.py`

## TDD Checklist

- [ ] RED: write parametrized `test_all_repository_scenarios_load`.
- [ ] Verify RED with a `tmp_path` fixture file missing a required section.

```bash
pytest tests/test_scenario_loader.py::test_all_repository_scenarios_load -v
```

Expected failure:

- invalid fixture is reported with the failed section

- [ ] GREEN: parameterize from real `scenarios/*.yml` files.
- [ ] Verify GREEN:

```bash
pytest tests/test_scenario_loader.py::test_all_repository_scenarios_load -v
```

Expected:

- all sample scenarios load

## Done Criteria

- New scenario fixtures automatically enter the loader regression set.

## Regression Verification

Run the Phase 2 regression command from `tasks/phase2/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_scenario_loader.py
git commit -m "test: validate all scenario fixtures"
```
