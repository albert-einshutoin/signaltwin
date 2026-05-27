# Task 01: Moisture Risk

Status: done

## Goal

Score moisture risk from humidity, dew point margin, cold spots, material vulnerability, PZT attenuation, and maintenance delay.

## Domain Boundary

This task owns only `moisture_risk` and its evidence.

## Files

- Create `src/signaltwin/risk_engine.py`
- Create `tests/test_risk_engine.py`

## TDD Checklist

- [ ] RED: write `test_rainy_season_wall_has_high_moisture_risk`.
- [ ] Verify RED:

```bash
pytest tests/test_risk_engine.py::test_rainy_season_wall_has_high_moisture_risk -v
```

Expected failure:

- missing `calculate_risk_report`

- [ ] GREEN: implement minimal `calculate_risk_report(scenario)` and moisture scoring.
- [ ] Verify GREEN:

```bash
pytest tests/test_risk_engine.py::test_rainy_season_wall_has_high_moisture_risk -v
```

Expected:

- `moisture_risk >= 0.70`
- evidence mentions humidity, dew point margin, material, PZT attenuation, and inspection delay

## Done Criteria

- Moisture score is clamped to `0.0..1.0`.
- Evidence uses scenario facts rather than generic text.

## Regression Verification

Run the Phase 3 regression command from `tasks/phase3/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/risk_engine.py tests/test_risk_engine.py
git commit -m "feat: score moisture risk"
```
