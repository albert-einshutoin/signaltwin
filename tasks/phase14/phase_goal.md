# Phase 14 Goal: Mock API And Dashboard Contract

## Goal

Define hardware-free API and dashboard data contracts before building a real dashboard or service.

## Scope

- API response schema for scenario/risk/demo status
- dashboard view model contract
- static JSON examples
- optional FastAPI/Streamlit plan only, not runtime dependency
- docs for future UI/API implementation

## Non-Goals

- No long-running web server required
- No browser UI implementation required
- No deployment
- No authentication
- No database

## Expected Files

- Create `src/signaltwin/api_contract.py`
- Create `docs/api-dashboard-contract.md`
- Create `outputs/demo/api_response.example.json`
- Create `outputs/demo/dashboard_view_model.example.json`
- Create `tests/test_api_dashboard_contract.py`

## Done Criteria

- API response contract can be generated from no-hardware demo outputs.
- Dashboard view model is deterministic.
- Docs define what a future dashboard/API should consume.
- No service process is required for tests.
