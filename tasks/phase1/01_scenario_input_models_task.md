# Task 01: Scenario Input Models

Status: done

## Goal

Model the top-level YAML scenario contract with strict required sections.

## Domain Boundary

This task owns top-level scenario, building, asset, maintenance, and BMS context models. It does not own per-signal validation beyond accepting a signals object.

## Files

- Create `src/signaltwin/schema.py`
- Create `tests/test_schema_contracts.py`

## TDD Checklist

- [ ] RED: write `test_scenario_requires_core_sections`.
- [ ] Verify RED:

```bash
pytest tests/test_schema_contracts.py::test_scenario_requires_core_sections -v
```

Expected failure:

- `ImportError` or missing `SignalTwinScenario`

- [ ] GREEN: implement the smallest Pydantic models for:

```txt
SignalTwinScenario
Building
Asset
Maintenance
BmsContext
Signals
```

- [ ] Verify GREEN:

```bash
pytest tests/test_schema_contracts.py::test_scenario_requires_core_sections -v
```

Expected:

- missing `building`, `asset`, `maintenance`, `bms`, `signals`, or `expected` fails validation

## Done Criteria

- Required sections match `docs/scenario-format.md`.
- BMS remains input context and is not modeled as a SignalTwin-owned sensor.

## Regression Verification

Run the Phase 1 regression command from `tasks/phase1/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/schema.py tests/test_schema_contracts.py
git commit -m "feat: add scenario input schema"
```
