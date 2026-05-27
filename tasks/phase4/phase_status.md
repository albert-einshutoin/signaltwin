# Phase 4 Status: Exporters

Status: done

## Tasks

| Task | Status | Evidence |
|---|---|---|
| 01 JSON Risk Report Exporter | done | `pytest tests/test_exporters.py::test_json_exporter_writes_valid_risk_report -v` passed. |
| 02 Markdown Maintenance Report Exporter | done | `pytest tests/test_exporters.py::test_markdown_exporter_includes_asset_scores_evidence_and_action -v` passed. |
| 03 RoomCI Scenario Exporter | done | `pytest tests/test_exporters.py::test_roomci_exporter_preserves_bms_and_signaltwin_sections -v` passed. |

## Blockers

- None.

## Phase Evidence

- `pytest tests/test_exporters.py -v` passed with 3 tests.
- `pytest tests/test_project_baseline.py tests/test_schema_contracts.py tests/test_scenario_loader.py tests/test_normalizer.py tests/test_risk_engine.py tests/test_exporters.py -v` passed with 32 tests.
- `pytest` passed with 32 tests.
- JSON export validates through `RiskReport`.
- Markdown export includes asset, scores, evidence, and recommendation.
- RoomCI export preserves separate `inputs.bms` and `inputs.signaltwin` sections.
