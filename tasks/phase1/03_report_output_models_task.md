# Task 03: Report Output Models

Status: done

## Goal

Define the output contract before writing the risk engine or exporters.

## Domain Boundary

This task owns the in-memory report shape, not file serialization.

## Files

- Modify `src/signaltwin/schema.py`
- Modify `tests/test_schema_contracts.py`

## TDD Checklist

- [ ] RED: write `test_risk_report_requires_evidence_and_recommendation`.
- [ ] Verify RED:

```bash
pytest tests/test_schema_contracts.py::test_risk_report_requires_evidence_and_recommendation -v
```

Expected failure:

- report model is missing

- [ ] GREEN: add models for:

```txt
RiskScores
Recommendation
RiskReport
```

- [ ] Verify GREEN:

```bash
pytest tests/test_schema_contracts.py::test_risk_report_requires_evidence_and_recommendation -v
```

Expected:

- missing `evidence` or `recommendation` fails validation

## Done Criteria

- Risk score fields match `docs/risk-model.md` and include `moss_risk` because existing scenarios use that expected category.
- Report schema can represent `outputs/risk_report.example.json`.

## Regression Verification

Run the Phase 1 regression command from `tasks/phase1/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/schema.py tests/test_schema_contracts.py
git commit -m "feat: add risk report schema"
```
