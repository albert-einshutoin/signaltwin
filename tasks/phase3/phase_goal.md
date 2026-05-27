# Phase 3 Goal: Risk Engine

## Goal

Implement deterministic, explainable, rule-based risk scoring for the minimal MVP.

## Scope

- moisture risk
- mold/moss risk
- wood deformation risk
- crack or void risk
- communication drift risk
- comfort degradation risk
- maintenance priority and recommendation
- evidence strings tied to input facts

## Non-Goals

- No ML or PyOD
- No baseline database
- No hardware data ingestion
- No dashboard

## Expected Files

- Create `src/signaltwin/risk_engine.py`
- Create `tests/test_risk_engine.py`

## Done Criteria

- Risk scoring is deterministic.
- Every non-zero high-impact score has evidence.
- Existing sample scenarios map to their expected recommendation categories.
- `moss_risk` is represented separately from `mold_risk` when visual moss evidence is present.
