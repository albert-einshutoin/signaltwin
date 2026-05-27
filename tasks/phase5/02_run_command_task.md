# Task 02: Run Command

Status: done

## Goal

Add a CLI command that runs the full minimal MVP pipeline for one scenario.

## Domain Boundary

This task owns CLI orchestration only. It calls loader, engine, and exporters.

## Files

- Modify `src/signaltwin/cli.py`
- Modify `tests/test_cli.py`

## TDD Checklist

- [ ] RED: write `test_run_command_writes_all_minimal_mvp_outputs`.
- [ ] Verify RED:

```bash
pytest tests/test_cli.py::test_run_command_writes_all_minimal_mvp_outputs -v
```

Expected failure:

- run command missing or no files written

- [ ] GREEN: implement `run` command.
- [ ] Verify GREEN:

```bash
pytest tests/test_cli.py::test_run_command_writes_all_minimal_mvp_outputs -v
```

Expected:

- writes `risk_report.json`, `maintenance_report.md`, and `roomci_scenario.yml`

## Done Criteria

- Output directory is created if missing.
- Existing curated examples are not overwritten by default.

## Regression Verification

Run the Phase 5 regression command from `tasks/phase5/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/cli.py tests/test_cli.py
git commit -m "feat: add scenario run command"
```
