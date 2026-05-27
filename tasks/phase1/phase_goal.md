# Phase 1 Goal: Schema Contracts

## Goal

Define strict Pydantic contracts for scenario inputs and report outputs before writing loaders or risk logic.

## Scope

- Scenario model
- BMS context model
- asset/building/maintenance models
- signal models for WiFi CSI, PZT, acoustic, thermal, and visual inspection
- risk report output model
- explicit mold and moss risk representation
- validation errors for missing required sections and invalid values

## Non-Goals

- No file loading
- No risk score calculation
- No exporters
- No CLI

## Expected Files

- Create `src/signaltwin/schema.py`
- Create `tests/test_schema_contracts.py`

## Done Criteria

- All current scenario dictionaries can validate through Pydantic.
- Missing required sections fail with clear validation errors.
- Risk report output schema requires `asset_id`, `risk_scores`, `evidence`, and `recommendation`.
- Risk scores can represent both `mold_risk` and `moss_risk` without losing scenario expectations.
