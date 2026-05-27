from pathlib import Path

import yaml
from typer.testing import CliRunner

from signaltwin.cli import app


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNNER = CliRunner()


def test_validate_command_accepts_valid_scenario():
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"

    result = RUNNER.invoke(app, ["validate", str(scenario_path)])

    assert result.exit_code == 0
    assert "rainy_season_wood_wall_risk" in result.output
    assert "room-101-north-wall" in result.output


def test_validate_command_does_not_write_files(tmp_path):
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"

    result = RUNNER.invoke(app, ["validate", str(scenario_path)])

    assert result.exit_code == 0
    assert list(tmp_path.iterdir()) == []


def test_run_command_writes_all_minimal_mvp_outputs(tmp_path):
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"

    result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(tmp_path)])

    assert result.exit_code == 0
    assert (tmp_path / "risk_report.json").is_file()
    assert (tmp_path / "maintenance_report.md").is_file()
    assert (tmp_path / "roomci_scenario.yml").is_file()
    assert "risk_report.json" in result.output


def test_run_command_creates_output_directory(tmp_path):
    output_dir = tmp_path / "nested" / "outputs"
    scenario_path = PROJECT_ROOT / "scenarios" / "communication_drift.yml"

    result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(output_dir)])

    assert result.exit_code == 0
    assert (output_dir / "risk_report.json").is_file()


def test_run_command_exports_roomci_bms_and_signaltwin_sections(tmp_path):
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"

    result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(tmp_path)])

    assert result.exit_code == 0
    exported = yaml.safe_load((tmp_path / "roomci_scenario.yml").read_text())
    assert "bms" in exported["inputs"]
    assert "signaltwin" in exported["inputs"]


def test_validate_command_reports_missing_file():
    missing_path = PROJECT_ROOT / "scenarios" / "missing.yml"

    result = RUNNER.invoke(app, ["validate", str(missing_path)])

    assert result.exit_code != 0
    assert str(missing_path) in result.output
    assert str(missing_path) in result.stderr
    assert "Traceback" not in result.output


def test_run_command_reports_invalid_scenario(tmp_path):
    invalid_path = tmp_path / "invalid.yml"
    invalid_path.write_text(
        """
scenario: invalid
bms: {}
signals: {}
expected: {}
""".strip()
    )

    result = RUNNER.invoke(app, ["run", str(invalid_path), "--output-dir", str(tmp_path)])

    assert result.exit_code != 0
    assert str(invalid_path) in result.output
    assert str(invalid_path) in result.stderr
    assert "building" in result.output
    assert "Traceback" not in result.output
