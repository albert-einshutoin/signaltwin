# Task 03: Thermal And Visual JSON Adapters

Status: done

## Goal

Parse thermal matrix and visual defect JSON fixtures into normalized frame payloads.

## Domain Boundary

This task owns thermal and visual JSON fixture parsing only.

## Files

- Create `src/signaltwin/adapters/thermal_json.py`
- Create `src/signaltwin/adapters/visual_json.py`
- Modify `tests/test_fixture_adapters.py`

## TDD Checklist

- [x] RED: write `test_thermal_json_adapter_returns_thermal_frame`.
- [x] RED: write `test_visual_json_adapter_returns_visual_frame`.
- [x] RED: write `test_thermal_json_adapter_rejects_invalid_matrix_shape`.
- [x] RED: write `test_visual_json_adapter_rejects_invalid_defect_severity`.
- [x] Verify RED:

```bash
pytest tests/test_fixture_adapters.py::test_thermal_json_adapter_returns_thermal_frame tests/test_fixture_adapters.py::test_visual_json_adapter_returns_visual_frame -v
```

Expected failure:

- missing adapter modules

- [x] GREEN: implement JSON fixture parsers.
- [x] Verify GREEN:

```bash
pytest tests/test_fixture_adapters.py::test_thermal_json_adapter_returns_thermal_frame tests/test_fixture_adapters.py::test_visual_json_adapter_returns_visual_frame -v
```

Expected:

- thermal output includes cold spots, thermal gradient, and dew point margin
- visual output includes detected defects
- invalid thermal matrix shape raises `AdapterError`
- invalid visual defect severity raises `AdapterError`

## Done Criteria

- MLX90640 and camera assumptions are represented as fixture formats, not hard-coded requirements.
- Adapters return schema-validated `AdapterOutput`.

## Regression Verification

Run the Phase 9 regression command from `tasks/phase9/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/thermal_json.py src/signaltwin/adapters/visual_json.py tests/test_fixture_adapters.py
git commit -m "feat: add thermal and visual fixture adapters"
```
