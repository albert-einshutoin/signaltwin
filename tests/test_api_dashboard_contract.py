from __future__ import annotations

import json
from pathlib import Path

import pytest

from signaltwin.demo import run_no_hardware_demo


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_api_response_contract_contains_risk_and_adapter_sections(tmp_path: Path) -> None:
    from signaltwin.api_contract import ApiResponse, build_api_response

    demo = run_no_hardware_demo(output_dir=tmp_path)
    response = build_api_response(demo)
    payload = response.model_dump(exclude_none=True)

    assert isinstance(response, ApiResponse)
    assert payload["status"] == "ok"
    assert payload["mode"] == "no_hardware_demo"
    assert "adapter_status" in payload
    assert "risk_report" in payload
    assert "evidence" in payload["risk_report"]
    assert "recommendation" in payload["risk_report"]
    assert "outputs" in payload
    json.dumps(payload)


def test_dashboard_view_model_groups_risks_evidence_and_adapter_status(tmp_path: Path) -> None:
    from signaltwin.api_contract import DashboardViewModel, build_dashboard_view_model

    demo = run_no_hardware_demo(output_dir=tmp_path)
    view_model = build_dashboard_view_model(demo)

    assert isinstance(view_model, DashboardViewModel)
    assert view_model.title == "SignalTwin No-Hardware Demo"
    assert view_model.risk_cards
    assert view_model.evidence_items
    assert view_model.adapter_sources[0].normalized_key == "bms"
    assert view_model.drift_groups
    assert view_model.report_links


def test_static_api_dashboard_examples_match_contract() -> None:
    from signaltwin.api_contract import validate_api_response, validate_dashboard_view_model

    api_payload = json.loads((PROJECT_ROOT / "outputs" / "demo" / "api_response.example.json").read_text())
    dashboard_payload = json.loads(
        (PROJECT_ROOT / "outputs" / "demo" / "dashboard_view_model.example.json").read_text()
    )

    validate_api_response(api_payload)
    validate_dashboard_view_model(dashboard_payload)


def test_api_response_validation_rejects_invalid_risk_score(tmp_path: Path) -> None:
    from signaltwin.api_contract import build_api_response, validate_api_response

    demo = run_no_hardware_demo(output_dir=tmp_path)
    payload = build_api_response(demo).model_dump(exclude_none=True)
    payload["risk_report"]["risk_scores"]["moisture_risk"] = 1.5

    with pytest.raises(ValueError, match="risk_scores"):
        validate_api_response(payload)


def test_api_dashboard_docs_define_no_runtime_requirement() -> None:
    text = (PROJECT_ROOT / "docs" / "api-dashboard-contract.md").read_text()

    assert "FastAPI" in text
    assert "Streamlit" in text
    assert "No server is required" in text
    assert "dashboard view model" in text
