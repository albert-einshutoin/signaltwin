# Task 04: Adapter-To-Risk E2E Regression

Status: done

## Goal

Prove the no-hardware Adapter-ready MVP can turn raw fixture files into a risk report through the existing risk engine.

## Domain Boundary

This task owns E2E regression wiring only. It must not rewrite risk rules or add real hardware dependencies.

## Files

- Modify `tests/test_adapter_ready_mvp.py`

## TDD Checklist

- [x] RED: write `test_adapter_outputs_compose_into_risk_report`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_ready_mvp.py::test_adapter_outputs_compose_into_risk_report -v
```

Expected failure:

- adapter output composition helper is missing

- [x] GREEN: compose BMS and signal adapter outputs into a `NormalizedScenario` compatible object.
- [x] GREEN: call existing `calculate_risk_report` with the composed normalized scenario.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_ready_mvp.py::test_adapter_outputs_compose_into_risk_report -v
```

Expected:

- risk report contains risk scores, evidence, and recommendation
- risk engine does not import adapter modules
- no physical device access is required

## Done Criteria

- The E2E path proves `raw fixture -> adapter -> schema-validated output -> normalized scenario -> risk report`.
- The test uses existing risk engine behavior.
- No adapter module is imported by `src/signaltwin/risk_engine.py`.

## Regression Verification

Run the Phase 10 regression command from `tasks/phase10/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tests/test_adapter_ready_mvp.py
git commit -m "test: prove adapter outputs reach risk engine"
```
