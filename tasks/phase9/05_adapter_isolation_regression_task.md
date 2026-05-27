# Task 05: Adapter Isolation Regression

Status: done

## Goal

Prove adapters are isolated from the risk engine and do not change existing Scenario Engine behavior.

## Domain Boundary

This task owns regression tests only.

## Files

- Modify `tests/test_fixture_adapters.py`

## TDD Checklist

- [x] RED: write `test_risk_engine_does_not_import_adapters`.
- [x] RED: write `test_existing_scenario_engine_still_runs_with_fixture_adapters_present`.
- [x] Verify RED:

```bash
pytest tests/test_fixture_adapters.py::test_risk_engine_does_not_import_adapters tests/test_fixture_adapters.py::test_existing_scenario_engine_still_runs_with_fixture_adapters_present -v
```

Expected failure:

- tests fail until assertions are implemented

- [x] GREEN: add isolation assertions.
- [x] Verify GREEN:

```bash
pytest tests/test_fixture_adapters.py::test_risk_engine_does_not_import_adapters tests/test_fixture_adapters.py::test_existing_scenario_engine_still_runs_with_fixture_adapters_present -v
```

Expected:

- tests pass

## Done Criteria

- `pytest` remains green.
- `src/signaltwin/risk_engine.py` does not import adapter modules.

## Regression Verification

Run the Phase 9 regression command from `tasks/phase9/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_fixture_adapters.py
git commit -m "test: verify adapter isolation"
```
