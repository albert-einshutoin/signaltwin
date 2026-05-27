# Task 03: Structural Drift Risks

Status: done

## Goal

Score wood deformation and crack/void risks from PZT, acoustic, visual crack, age, and maintenance delay.

## Domain Boundary

This task owns:

- `wood_deformation_risk`
- `crack_or_void_risk`

It does not own communication or comfort scoring.

## Files

- Modify `src/signaltwin/risk_engine.py`
- Modify `tests/test_risk_engine.py`

## TDD Checklist

- [ ] RED: write `test_pzt_and_visual_crack_create_structural_drift_evidence`.
- [ ] Verify RED:

```bash
pytest tests/test_risk_engine.py::test_pzt_and_visual_crack_create_structural_drift_evidence -v
```

Expected failure:

- structural risk fields are missing or evidence is absent

- [ ] GREEN: add structural drift rules.
- [ ] Verify GREEN:

```bash
pytest tests/test_risk_engine.py::test_pzt_and_visual_crack_create_structural_drift_evidence -v
```

Expected:

- report includes structural scores and evidence for resonance shift, attenuation, acoustic drift, or visual crack where present

## Done Criteria

- Structural scores do not require all signal types to be present.
- Missing PZT or acoustic data contributes zero, not an exception.

## Regression Verification

Run the Phase 3 regression command from `tasks/phase3/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/risk_engine.py tests/test_risk_engine.py
git commit -m "feat: score structural drift risks"
```
