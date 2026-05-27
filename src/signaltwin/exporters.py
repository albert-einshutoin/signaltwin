from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from signaltwin.normalizer import NormalizedScenario
from signaltwin.schema import RiskReport


def write_risk_report_json(report: RiskReport, path: str | Path) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report.model_dump(exclude_none=True), indent=2, sort_keys=True) + "\n"
    )


def write_maintenance_report_markdown(
    scenario: NormalizedScenario, report: RiskReport, path: str | Path
) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(_maintenance_markdown(scenario, report))


def write_roomci_scenario(
    scenario: NormalizedScenario, report: RiskReport, path: str | Path
) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(_roomci_payload(scenario, report), sort_keys=False))


def _maintenance_markdown(scenario: NormalizedScenario, report: RiskReport) -> str:
    scores = report.risk_scores.model_dump(exclude_none=True)
    lines = [
        "# Maintenance Report",
        "",
        "## Asset",
        "",
        f"- Asset ID: `{scenario.asset_id}`",
        f"- Building ID: `{scenario.building_id}`",
        f"- Type: `{scenario.asset.type}`",
        f"- Orientation: `{scenario.asset.orientation}`",
        "",
        "## Risk Summary",
        "",
        "| Risk | Score | Level |",
        "|---|---:|---|",
    ]

    for risk, score in scores.items():
        lines.append(f"| {risk} | {score:.2f} | {_level(score)} |")

    lines.extend(
        [
            "",
            "## Evidence",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in report.evidence)
    lines.extend(
        [
            "",
            "## Recommendation",
            "",
            f"Priority: **{report.recommendation.priority}**",
            "",
            report.recommendation.action,
            "",
            f"Maintenance type: `{report.recommendation.maintenance_type}`",
            "",
        ]
    )
    return "\n".join(lines)


def _roomci_payload(scenario: NormalizedScenario, report: RiskReport) -> dict[str, Any]:
    return {
        "scenario": f"signaltwin_{scenario.scenario}",
        "description": (
            "SignalTwin minimal MVP export. BMS values remain input context; "
            "SignalTwin values represent non-BMS signal evidence and risk output."
        ),
        "inputs": {
            "bms": scenario.bms.model_dump(exclude_none=True),
            "signaltwin": scenario.signals.model_dump(exclude_none=True),
        },
        "expected": {
            "risk_report": {
                "moisture_risk": _level(report.risk_scores.moisture_risk),
                "mold_risk": _level(report.risk_scores.mold_risk),
                "moss_risk": _level(report.risk_scores.moss_risk or 0.0),
                "wood_deformation_risk": _level(report.risk_scores.wood_deformation_risk),
                "crack_or_void_risk": _level(report.risk_scores.crack_or_void_risk),
                "communication_drift_risk": _level(report.risk_scores.communication_drift_risk),
                "comfort_degradation_risk": _level(report.risk_scores.comfort_degradation_risk),
                "recommendation": _recommendation_slug(report.recommendation.action),
            }
        },
    }


def _level(score: float) -> str:
    if score >= 0.70:
        return "high"
    if score >= 0.60:
        return "medium_high"
    if score >= 0.40:
        return "medium"
    if score >= 0.25:
        return "low_medium"
    return "low"


def _recommendation_slug(action: str) -> str:
    if "within 30 days" in action:
        return "inspect_within_30_days"
    if "within 45 days" in action:
        return "cleaning_within_45_days"
    if "AP position" in action:
        return "inspect_ap_position_or_interference"
    if "filter and airflow" in action:
        return "inspect_hvac_filter_and_airflow"
    return "inspect"
