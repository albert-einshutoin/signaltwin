# Task 01: Adapter-Ready E2E Regression

Status: done

## Goal

Prove fixture adapters and the existing Scenario Engine can coexist.

## Domain Boundary

This task owns E2E regression only.

## Files

- Create `tests/test_adapter_ready_mvp.py`

## TDD Checklist

- [x] RED: write `test_adapter_ready_mvp_parses_all_raw_fixtures`.
- [x] RED: write `test_adapter_ready_mvp_keeps_scenario_cli_working`.
- [x] RED: write `test_adapter_ready_mvp_adapter_outputs_are_schema_validated`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_ready_mvp.py -v
```

Expected failure:

- missing test helpers or missing adapter fixture outputs

- [x] GREEN: implement regression assertions.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_ready_mvp.py -v
```

Expected:

- tests pass

## Done Criteria

- Raw fixtures parse.
- Adapter outputs are schema-validated.
- Scenario CLI still validates and runs.

## Regression Verification

Run the Phase 10 regression command from `tasks/phase10/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_adapter_ready_mvp.py
git commit -m "test: add adapter-ready mvp regression"
```
