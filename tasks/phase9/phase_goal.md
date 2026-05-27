# Phase 9 Goal: Fixture Adapter Implementation

## Goal

Implement fixture-based adapters that parse raw files and produce normalized SignalTwin frames without real devices.

## Scope

- BMS CSV adapter
- WiFi CSI fixture adapter
- thermal matrix fixture adapter
- visual defect fixture adapter
- acoustic feature fixture adapter
- PZT ADC fixture adapter
- invalid fixture error handling for each adapter family

## Non-Goals

- No real hardware connection
- No dashboard/API
- No baseline database
- No risk rule rewrite
- No CLI adapter command in this phase

## Expected Files

- Create `src/signaltwin/adapters/bms_csv.py`
- Create `src/signaltwin/adapters/wifi_csi_csv.py`
- Create `src/signaltwin/adapters/thermal_json.py`
- Create `src/signaltwin/adapters/visual_json.py`
- Create `src/signaltwin/adapters/acoustic_json.py`
- Create `src/signaltwin/adapters/pzt_csv.py`
- Create `tests/test_fixture_adapters.py`

## Done Criteria

- Each adapter parses its fixture and emits normalized frame payloads.
- Each adapter returns schema-validated `AdapterOutput`.
- Invalid fixture shape, missing required columns, and invalid values surface as `AdapterError`.
- Existing scenario engine tests remain green.
- Risk engine does not import adapter modules.
