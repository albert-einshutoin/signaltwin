# Task 01: BMS And WiFi CSI Fixtures

Status: done

## Goal

Create parseable BMS and WiFi CSI raw fixtures for adapter development without devices.

## Domain Boundary

This task owns raw fixture contracts only. It does not implement adapters.

## Files

- Create `fixtures/raw/bms_context.csv`
- Create `fixtures/raw/wifi_csi.csv`
- Create `tests/test_raw_fixture_contracts.py`

## TDD Checklist

- [x] RED: write `test_bms_and_wifi_raw_fixtures_parse`.
- [x] Verify RED:

```bash
pytest tests/test_raw_fixture_contracts.py::test_bms_and_wifi_raw_fixtures_parse -v
```

Expected failure:

- missing fixture files

- [x] GREEN: add CSV fixtures with required columns.
- [x] Verify GREEN:

```bash
pytest tests/test_raw_fixture_contracts.py::test_bms_and_wifi_raw_fixtures_parse -v
```

Expected:

- test passes

## Done Criteria

- BMS fixture includes humidity, temperature, illuminance, HVAC hours, and timestamp.
- WiFi fixture includes RSSI/SNR, packet loss, retransmission, CSI drift, multipath, and baseline similarity.

## Regression Verification

Run the Phase 8 regression command from `tasks/phase8/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add fixtures/raw/bms_context.csv fixtures/raw/wifi_csi.csv tests/test_raw_fixture_contracts.py
git commit -m "test: add bms and wifi raw fixtures"
```
