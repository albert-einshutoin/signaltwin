import json
from pathlib import Path

import yaml
from typer.testing import CliRunner

from signaltwin.cli import app
from signaltwin.schema import RiskReport


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNNER = CliRunner()


def test_all_scenarios_run_to_reports(tmp_path):
    scenario_paths = sorted((PROJECT_ROOT / "scenarios").glob("*.yml"))

    assert scenario_paths
    for scenario_path in scenario_paths:
        output_dir = tmp_path / scenario_path.stem
        result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(output_dir)])

        assert result.exit_code == 0, result.output
        assert (output_dir / "risk_report.json").is_file()
        assert (output_dir / "maintenance_report.md").is_file()
        assert (output_dir / "roomci_scenario.yml").is_file()

        report = RiskReport.model_validate_json((output_dir / "risk_report.json").read_text())
        roomci = yaml.safe_load((output_dir / "roomci_scenario.yml").read_text())
        markdown = (output_dir / "maintenance_report.md").read_text()

        assert report.asset_id
        assert report.evidence
        assert roomci["inputs"]["bms"]
        assert "signaltwin" in roomci["inputs"]
        assert report.asset_id in markdown


def test_generated_risk_report_json_is_parseable_after_cli_run(tmp_path):
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"
    result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(tmp_path)])

    assert result.exit_code == 0, result.output
    parsed = json.loads((tmp_path / "risk_report.json").read_text())
    assert parsed["asset_id"] == "room-101-north-wall"
