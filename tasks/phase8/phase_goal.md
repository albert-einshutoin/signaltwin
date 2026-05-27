# Phase 8 Goal: Raw I/O Fixture Contracts

## Goal

Define raw fixture formats for assumed devices so adapter development can proceed without hardware.

## Scope

- BMS CSV fixture contract
- WiFi CSI CSV fixture contract
- thermal matrix JSON fixture contract
- visual defect JSON fixture contract
- acoustic feature JSON fixture contract
- PZT ADC CSV fixture contract

## Non-Goals

- No parser implementation
- No real device connection
- No feature extraction from real image/audio/waveform files

## Expected Files

- Create `docs/raw-io-fixtures.md`
- Create `fixtures/raw/bms_context.csv`
- Create `fixtures/raw/wifi_csi.csv`
- Create `fixtures/raw/thermal_matrix.json`
- Create `fixtures/raw/visual_defects.json`
- Create `fixtures/raw/acoustic_features.json`
- Create `fixtures/raw/pzt_adc.csv`
- Create `tests/test_raw_fixture_contracts.py`

## Done Criteria

- Every assumed device family has a raw fixture.
- Each fixture can be loaded by standard Python libraries.
- Fixtures include enough fields to map into current SignalTwin signal frames.
