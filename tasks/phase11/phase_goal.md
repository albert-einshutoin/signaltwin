# Phase 11 Goal: Adapter Registry And CLI Operations

## Goal

Make fixture adapters operable through config and CLI before real hardware exists.

## Scope

- adapter registry
- adapter source config contract
- fixture inspection CLI
- adapter error surfacing through CLI
- docs for switching assumed devices/program outputs

## Non-Goals

- No live device capture
- No serial, GPIO, I2C, camera, microphone, or ADC access
- No risk engine changes
- No long-running service

## Expected Files

- Create `src/signaltwin/adapters/registry.py`
- Create `src/signaltwin/adapters/config.py`
- Modify `src/signaltwin/cli.py`
- Create `configs/adapter-fixtures.yml`
- Create `tests/test_adapter_registry.py`
- Create `tests/test_adapter_cli.py`
- Modify `docs/adapter-contract.md`

## Done Criteria

- Adapter names resolve through a registry.
- Fixture adapter paths can be read from config.
- CLI can inspect adapter fixture outputs without scoring risk.
- CLI reports adapter errors without tracebacks.
- Existing `pytest` suite remains green.
