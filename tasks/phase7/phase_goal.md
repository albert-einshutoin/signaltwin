# Phase 7 Goal: Adapter Contract Planning

## Goal

Define hardware-replaceable adapter contracts before implementing any device-specific parser.

## Scope

- adapter base interface
- normalized frame boundary
- adapter error model
- source/device metadata model
- adapter output validation contract
- docs for supported assumed device families

## Non-Goals

- No real hardware connection
- No CSV parsing
- No image, WAV, CSI, thermal, or ADC feature extraction
- No risk engine changes except tests proving adapters do not require them

## Expected Files

- Create `src/signaltwin/adapters/__init__.py`
- Create `src/signaltwin/adapters/base.py`
- Create `docs/adapter-contract.md`
- Create `tests/test_adapter_contracts.py`

## Done Criteria

- Adapter interface can represent BMS, WiFi CSI, thermal, visual, acoustic, and PZT sources.
- Adapter output identifies source family, source name, input path, normalized key, and schema-validated payload.
- Adapter output payload validates against existing BMS or signal schema models before risk scoring.
- Adapter errors are user-readable.
- Existing `pytest` suite remains green.
