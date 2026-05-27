# Task 02: WiFi CSI CSV Adapter

Status: done

## Goal

Parse ESP32-CSI-like CSV fixture data into normalized WiFi CSI frame payloads.

## Domain Boundary

This task owns WiFi CSI fixture parsing only.

## Files

- Create `src/signaltwin/adapters/wifi_csi_csv.py`
- Modify `tests/test_fixture_adapters.py`

## TDD Checklist

- [x] RED: write `test_wifi_csi_csv_adapter_returns_wifi_frame`.
- [x] RED: write `test_wifi_csi_csv_adapter_rejects_out_of_range_scores`.
- [x] Verify RED:

```bash
pytest tests/test_fixture_adapters.py::test_wifi_csi_csv_adapter_returns_wifi_frame -v
```

Expected failure:

- missing adapter module

- [x] GREEN: implement WiFi CSI CSV fixture parser.
- [x] Verify GREEN:

```bash
pytest tests/test_fixture_adapters.py::test_wifi_csi_csv_adapter_returns_wifi_frame -v
```

Expected:

- output includes `csi_drift_score`, `snr_delta_db`, `packet_loss_rate`, and `baseline_similarity`
- out-of-range score values raise `AdapterError`

## Done Criteria

- Adapter can be replaced by RuView-like output later without risk engine changes.
- Adapter returns schema-validated `AdapterOutput`.

## Regression Verification

Run the Phase 9 regression command from `tasks/phase9/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/wifi_csi_csv.py tests/test_fixture_adapters.py
git commit -m "feat: add wifi csi csv fixture adapter"
```
