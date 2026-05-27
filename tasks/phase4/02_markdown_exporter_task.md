# Task 02: Markdown Maintenance Report Exporter

Status: done

## Goal

Write a human-readable maintenance report from scenario metadata and risk report output.

## Domain Boundary

This task owns Markdown rendering only.

## Files

- Modify `src/signaltwin/exporters.py`
- Modify `tests/test_exporters.py`

## TDD Checklist

- [ ] RED: write `test_markdown_exporter_includes_asset_scores_evidence_and_action`.
- [ ] Verify RED:

```bash
pytest tests/test_exporters.py::test_markdown_exporter_includes_asset_scores_evidence_and_action -v
```

Expected failure:

- missing Markdown exporter

- [ ] GREEN: implement `write_maintenance_report_markdown(scenario, report, path)`.
- [ ] Verify GREEN:

```bash
pytest tests/test_exporters.py::test_markdown_exporter_includes_asset_scores_evidence_and_action -v
```

Expected:

- Markdown includes asset id, risk table, evidence list, priority, and action

## Done Criteria

- Markdown is stable enough for snapshot-like assertions.
- Markdown does not include hardware-only claims.

## Regression Verification

Run the Phase 4 regression command from `tasks/phase4/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/exporters.py tests/test_exporters.py
git commit -m "feat: export maintenance markdown"
```
