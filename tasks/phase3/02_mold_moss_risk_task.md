# Task 02: Mold Moss Risk

Status: done

## Goal

Score mold or moss risk from humidity, low illuminance, orientation, visual defects, surface condensation context, and cleaning delay.

## Domain Boundary

This task owns `mold_risk`, `moss_risk`, and their evidence only.

## Files

- Modify `src/signaltwin/risk_engine.py`
- Modify `tests/test_risk_engine.py`

## TDD Checklist

- [ ] RED: write `test_coastal_villa_visual_moss_drives_moss_risk`.
- [ ] Verify RED:

```bash
pytest tests/test_risk_engine.py::test_coastal_villa_visual_moss_drives_moss_risk -v
```

Expected failure:

- `moss_risk` is absent or too low

- [ ] GREEN: add mold/moss scoring rules.
- [ ] Verify GREEN:

```bash
pytest tests/test_risk_engine.py::test_coastal_villa_visual_moss_drives_moss_risk -v
```

Expected:

- `moss_risk` is high for the coastal moss fixture
- evidence mentions visual moss and cleaning delay

## Done Criteria

- Moss fixture maps to expected high moss risk.
- Mold risk remains available for indoor moisture scenarios.
- Rule remains explainable without image ML.

## Regression Verification

Run the Phase 3 regression command from `tasks/phase3/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/risk_engine.py tests/test_risk_engine.py
git commit -m "feat: score mold and moss risk"
```
