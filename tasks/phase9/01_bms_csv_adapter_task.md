# Task 01: BMS CSV Adapter

Status: done

## Goal

Parse BMS CSV fixture data into normalized BMS context payloads.

## Domain Boundary

This task owns BMS CSV fixture parsing only.

## Files

- Create `src/signaltwin/adapters/bms_csv.py`
- Create `tests/test_fixture_adapters.py`

## TDD Checklist

- [x] RED: write `test_bms_csv_adapter_returns_bms_context`.
- [x] RED: write `test_bms_csv_adapter_reports_missing_required_column`.
- [x] Verify RED:

```bash
pytest tests/test_fixture_adapters.py::test_bms_csv_adapter_returns_bms_context -v
```

Expected failure:

- missing adapter module

- [x] GREEN: implement BMS CSV fixture parser.
- [x] Verify GREEN:

```bash
pytest tests/test_fixture_adapters.py::test_bms_csv_adapter_returns_bms_context -v
```

Expected:

- output has humidity, temperature, illuminance, HVAC hours, and timestamp
- missing required columns raise `AdapterError`

## Done Criteria

- Adapter does not score risk.
- Adapter does not require real BMS access.
- Adapter returns schema-validated `AdapterOutput`.

## Regression Verification

Run the Phase 9 regression command from `tasks/phase9/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/bms_csv.py tests/test_fixture_adapters.py
git commit -m "feat: add bms csv fixture adapter"
```
