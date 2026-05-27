# Phase 14 Test Plan

## Narrow Commands

```bash
pytest tests/test_api_dashboard_contract.py -v
```

Expected:

- API response examples validate
- dashboard view model examples validate
- docs mention future FastAPI/Streamlit without requiring them

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
