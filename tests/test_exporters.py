import json
from pathlib import Path

import yaml

from signaltwin.exporters import (
    write_maintenance_report_markdown,
    write_risk_report_json,
    write_roomci_scenario,
)
from signaltwin.normalizer import normalize_scenario
from signaltwin.risk_engine import calculate_risk_report
from signaltwin.scenario_loader import load_scenario
from signaltwin.schema import RiskReport


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def rainy_season_context():
    scenario = normalize_scenario(
        load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")
    )
    report = calculate_risk_report(scenario)
    return scenario, report


def test_json_exporter_writes_valid_risk_report(tmp_path):
    _, report = rainy_season_context()
    output_path = tmp_path / "risk_report.json"

    write_risk_report_json(report, output_path)

    parsed = json.loads(output_path.read_text())
    validated = RiskReport.model_validate(parsed)
    assert validated == report
    assert output_path.read_text().endswith("\n")
    assert '"asset_id": "room-101-north-wall"' in output_path.read_text()


def test_markdown_exporter_includes_asset_scores_evidence_and_action(tmp_path):
    scenario, report = rainy_season_context()
    output_path = tmp_path / "maintenance_report.md"

    write_maintenance_report_markdown(scenario, report, output_path)

    markdown = output_path.read_text()
    assert "# Maintenance Report" in markdown
    assert "room-101-north-wall" in markdown
    assert "moisture_risk" in markdown
    assert "7-day average humidity" in markdown
    assert "within 30 days" in markdown
    assert "hardware" not in markdown.lower()


def test_roomci_exporter_preserves_bms_and_signaltwin_sections(tmp_path):
    scenario, report = rainy_season_context()
    output_path = tmp_path / "roomci_scenario.yml"

    write_roomci_scenario(scenario, report, output_path)

    exported = yaml.safe_load(output_path.read_text())
    assert exported["scenario"] == "signaltwin_rainy_season_wood_wall_risk"
    assert exported["inputs"]["bms"]["humidity_7d_avg_percent"] == 82
    assert exported["inputs"]["signaltwin"]["wifi_csi"]["csi_drift_score"] == 0.18
    assert exported["expected"]["risk_report"]["moisture_risk"] == "high"
    assert exported["expected"]["risk_report"]["recommendation"] == "inspect_within_30_days"
