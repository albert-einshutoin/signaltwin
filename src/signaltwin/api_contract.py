from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from signaltwin.demo import DemoResult
from signaltwin.schema import Recommendation, RiskReport


class StrictApiModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AdapterStatus(StrictApiModel):
    name: str
    adapter: str
    normalized_key: str
    source_name: str
    fields: list[str]


class ApiResponse(StrictApiModel):
    status: str
    mode: str
    adapter_status: list[AdapterStatus]
    risk_report: RiskReport
    drift_comparison: dict[str, Any]
    outputs: dict[str, str]


class RiskCard(StrictApiModel):
    name: str
    score: float = Field(ge=0, le=1)


class DashboardViewModel(StrictApiModel):
    title: str
    mode: str
    risk_cards: list[RiskCard]
    evidence_items: list[str]
    recommendation: Recommendation
    adapter_sources: list[AdapterStatus]
    drift_groups: list[dict[str, Any]]
    report_links: dict[str, str]


def build_api_response(demo: DemoResult) -> ApiResponse:
    adapter_inspection = _read_json(demo.artifacts["adapter_inspection.json"])
    drift_comparison = _read_json(demo.artifacts["drift_comparison.json"])
    risk_report = _read_json(demo.artifacts["risk_report.json"])

    payload = {
        "status": "ok",
        "mode": "no_hardware_demo",
        "adapter_status": adapter_inspection["sources"],
        "risk_report": {
            "asset_id": risk_report["asset_id"],
            "risk_scores": risk_report["risk_scores"],
            "evidence": risk_report["evidence"],
            "recommendation": risk_report["recommendation"],
        },
        "drift_comparison": drift_comparison,
        "outputs": {name: path.name for name, path in demo.artifacts.items()},
    }
    return _validated_api_response(payload)


def build_dashboard_view_model(demo: DemoResult) -> DashboardViewModel:
    api_response = build_api_response(demo)
    risk_scores = api_response.risk_report.risk_scores.model_dump(exclude_none=True)
    payload = {
        "title": "SignalTwin No-Hardware Demo",
        "mode": api_response.mode,
        "risk_cards": [
            {"name": name, "score": score}
            for name, score in risk_scores.items()
            if isinstance(score, (int, float))
        ],
        "evidence_items": list(api_response.risk_report.evidence),
        "recommendation": api_response.risk_report.recommendation,
        "adapter_sources": list(api_response.adapter_status),
        "drift_groups": list(api_response.drift_comparison["groups"]),
        "report_links": dict(api_response.outputs),
    }
    return _validated_dashboard_view_model(payload)


def write_api_dashboard_examples(demo: DemoResult, output_dir: str | Path) -> dict[str, Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    api_path = output_path / "api_response.example.json"
    dashboard_path = output_path / "dashboard_view_model.example.json"
    api_payload = build_api_response(demo).model_dump(exclude_none=True)
    api_path.write_text(json.dumps(api_payload, indent=2, sort_keys=True) + "\n")
    dashboard_path.write_text(
        json.dumps(
            build_dashboard_view_model(demo).model_dump(exclude_none=True),
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    return {
        "api_response.example.json": api_path,
        "dashboard_view_model.example.json": dashboard_path,
    }


def validate_api_response(payload: dict[str, Any]) -> None:
    response = _validated_api_response(payload)
    if response.status != "ok":
        raise ValueError("API response status must be ok")


def validate_dashboard_view_model(payload: dict[str, Any]) -> None:
    _validated_dashboard_view_model(payload)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def _validated_api_response(payload: dict[str, Any]) -> ApiResponse:
    try:
        return ApiResponse.model_validate(payload)
    except ValidationError as exc:
        raise ValueError(f"invalid API response: {exc}") from exc


def _validated_dashboard_view_model(payload: dict[str, Any]) -> DashboardViewModel:
    try:
        return DashboardViewModel.model_validate(payload)
    except ValidationError as exc:
        raise ValueError(f"invalid dashboard view model: {exc}") from exc
