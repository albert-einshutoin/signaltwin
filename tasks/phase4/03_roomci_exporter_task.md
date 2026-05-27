# Task 03: RoomCI Scenario Exporter

Status: done

## Goal

Export a RoomCI-friendly YAML scenario that separates BMS inputs from SignalTwin risk expectations.

## Domain Boundary

This task owns RoomCI YAML serialization only. It does not run RoomCI.

## Files

- Modify `src/signaltwin/exporters.py`
- Modify `tests/test_exporters.py`

## TDD Checklist

- [ ] RED: write `test_roomci_exporter_preserves_bms_and_signaltwin_sections`.
- [ ] Verify RED:

```bash
pytest tests/test_exporters.py::test_roomci_exporter_preserves_bms_and_signaltwin_sections -v
```

Expected failure:

- missing RoomCI exporter

- [ ] GREEN: implement `write_roomci_scenario(scenario, report, path)`.
- [ ] Verify GREEN:

```bash
pytest tests/test_exporters.py::test_roomci_exporter_preserves_bms_and_signaltwin_sections -v
```

Expected:

- YAML contains `inputs.bms`, `inputs.signaltwin`, and `expected.risk_report`

## Done Criteria

- Export makes BMS/SignalTwin responsibility split visible.
- Output is deterministic.

## Regression Verification

Run the Phase 4 regression command from `tasks/phase4/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/exporters.py tests/test_exporters.py
git commit -m "feat: export roomci scenario yaml"
```
