# Task 05: Recommendation Policy

Status: done

## Goal

Convert risk scores and expected scenario categories into deterministic maintenance priority and action text.

## Domain Boundary

This task owns recommendation selection only.

## Files

- Modify `src/signaltwin/risk_engine.py`
- Modify `tests/test_risk_engine.py`

## TDD Checklist

- [ ] RED: write `test_recommendation_matches_highest_actionable_risk`.
- [ ] Verify RED:

```bash
pytest tests/test_risk_engine.py::test_recommendation_matches_highest_actionable_risk -v
```

Expected failure:

- recommendation is missing or generic

- [ ] GREEN: implement priority thresholds:

```txt
high: score >= 0.70
medium_high: score >= 0.60
medium: score >= 0.40
low_medium: score >= 0.25
low: score < 0.25
```

- [ ] Verify GREEN:

```bash
pytest tests/test_risk_engine.py::test_recommendation_matches_highest_actionable_risk -v
```

Expected:

- rainy-season wall recommends inspection within 30 days
- communication drift recommends AP/interference inspection
- HVAC drift recommends filter/airflow inspection

## Done Criteria

- Recommendation includes priority, action, and maintenance type.
- Report does not claim exact diagnosis.

## Regression Verification

Run the Phase 3 regression command from `tasks/phase3/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/risk_engine.py tests/test_risk_engine.py
git commit -m "feat: add maintenance recommendation policy"
```
