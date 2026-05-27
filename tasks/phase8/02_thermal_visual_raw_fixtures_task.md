# Task 02: Thermal And Visual Fixtures

Status: done

## Goal

Create thermal matrix and visual defect raw fixtures that imitate MLX90640-like and camera/label output.

## Domain Boundary

This task owns JSON fixture contracts only.

## Files

- Create `fixtures/raw/thermal_matrix.json`
- Create `fixtures/raw/visual_defects.json`
- Modify `tests/test_raw_fixture_contracts.py`

## TDD Checklist

- [x] RED: write `test_thermal_and_visual_raw_fixtures_parse`.
- [x] Verify RED:

```bash
pytest tests/test_raw_fixture_contracts.py::test_thermal_and_visual_raw_fixtures_parse -v
```

Expected failure:

- missing fixture files

- [x] GREEN: add JSON fixtures.
- [x] Verify GREEN:

```bash
pytest tests/test_raw_fixture_contracts.py::test_thermal_and_visual_raw_fixtures_parse -v
```

Expected:

- thermal fixture has 32x24-like matrix metadata
- visual fixture has detected defects with severity

## Done Criteria

- Thermal fixture can represent MLX90640 but does not require MLX90640-specific code.
- Visual fixture can come from OpenCV, manual labels, or other image pipelines.

## Regression Verification

Run the Phase 8 regression command from `tasks/phase8/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add fixtures/raw/thermal_matrix.json fixtures/raw/visual_defects.json tests/test_raw_fixture_contracts.py
git commit -m "test: add thermal and visual raw fixtures"
```
