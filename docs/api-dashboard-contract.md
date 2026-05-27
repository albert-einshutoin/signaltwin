# SignalTwin API And Dashboard Contract

This document defines the hardware-free API and dashboard data contracts for future UI/API work.

No server is required for the current contract tests. FastAPI and Streamlit remain future implementation options, not runtime dependencies for this phase.

## API Response

The API response contract is generated from the no-hardware demo artifacts.

Required sections:

- `status`
- `mode`
- `adapter_status`
- `risk_report`
- `drift_comparison`
- `outputs`

The response lets a future FastAPI service return demo state without changing adapter or risk engine code.

## Dashboard View Model

The dashboard view model groups data for a future Streamlit or web UI.

Required sections:

- `risk_cards`
- `evidence_items`
- `adapter_sources`
- `drift_groups`
- `report_links`
- `recommendation`

The dashboard view model is a static JSON contract. Tests validate the shape without starting a browser, Streamlit process, FastAPI server, database, or hardware capture.

## Handoff

Future UI/API tasks should consume `outputs/demo/api_response.example.json` and `outputs/demo/dashboard_view_model.example.json` first. Runtime service work should come after these contracts are stable.
