# Phase 2 Goal: Scenario Loading And Normalization

## Goal

Load YAML scenarios from disk into validated schema objects, then normalize BMS and scenario-provided mock signal values into internal frames with clear error behavior.

## Scope

- YAML file reading
- Pydantic validation integration
- mock signal frame normalization from scenario values
- BMS context normalization from scenario values
- deterministic fixture loading in tests
- user-facing load errors

## Non-Goals

- No risk scoring
- No exporters
- No CLI

## Expected Files

- Create `src/signaltwin/scenario_loader.py`
- Create `src/signaltwin/normalizer.py`
- Create `tests/test_scenario_loader.py`
- Create `tests/test_normalizer.py`

## Done Criteria

- All `scenarios/*.yml` load successfully.
- BMS and signal inputs normalize into internal frames before risk scoring.
- Scenario-provided signal values satisfy the minimal MVP mock signal frame requirement.
- Missing file errors identify the path.
- Invalid schema errors identify the failed section.
