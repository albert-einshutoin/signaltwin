# Task 01: JSON Risk Report Exporter

Status: done

## Goal

Write deterministic JSON for a `RiskReport`.

## Domain Boundary

This task owns JSON serialization only.

## Files

- Create `src/signaltwin/exporters.py`
- Create `tests/test_exporters.py`

## TDD Checklist

- [ ] RED: write `test_json_exporter_writes_valid_risk_report`.
- [ ] Verify RED:

```bash
pytest tests/test_exporters.py::test_json_exporter_writes_valid_risk_report -v
```

Expected failure:

- missing exporter

- [ ] GREEN: implement `write_risk_report_json(report, path)`.
- [ ] Verify GREEN:

```bash
pytest tests/test_exporters.py::test_json_exporter_writes_valid_risk_report -v
```

Expected:

- file exists
- JSON parses
- parsed content validates as `RiskReport`

## Done Criteria

- JSON uses stable indentation and key ordering.
- Exporter does not mutate the report.

## Regression Verification

Run the Phase 4 regression command from `tasks/phase4/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/exporters.py tests/test_exporters.py
git commit -m "feat: export risk report json"
```
