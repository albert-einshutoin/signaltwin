from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from signaltwin.adapters.acoustic_json import AcousticJsonAdapter
from signaltwin.adapters.base import AdapterInput
from signaltwin.adapters.bms_csv import BmsCsvAdapter
from signaltwin.adapters.pzt_csv import PztCsvAdapter
from signaltwin.adapters.thermal_json import ThermalJsonAdapter
from signaltwin.adapters.visual_json import VisualJsonAdapter
from signaltwin.adapters.wifi_csi_csv import WifiCsiCsvAdapter
from signaltwin.cli import app
from signaltwin.risk_engine import calculate_risk_report


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FIXTURE_DIR = PROJECT_ROOT / "fixtures" / "raw"
RUNNER = CliRunner()


def test_adapter_ready_mvp_parses_all_raw_fixtures() -> None:
    outputs = _load_all_adapter_outputs()

    assert {output.normalized_key for output in outputs} == {
        "bms",
        "wifi_csi",
        "thermal",
        "visual",
        "acoustic",
        "pzt",
    }


def test_adapter_ready_mvp_adapter_outputs_are_schema_validated() -> None:
    outputs = _load_all_adapter_outputs()

    assert all(output.payload for output in outputs)
    assert all(isinstance(output.payload, dict) for output in outputs)


def test_adapter_ready_mvp_keeps_scenario_cli_working(tmp_path: Path) -> None:
    scenario_path = PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml"

    validate_result = RUNNER.invoke(app, ["validate", str(scenario_path)])
    run_result = RUNNER.invoke(app, ["run", str(scenario_path), "--output-dir", str(tmp_path)])

    assert validate_result.exit_code == 0
    assert run_result.exit_code == 0
    assert (tmp_path / "risk_report.json").read_text()
    assert (tmp_path / "maintenance_report.md").read_text()
    assert (tmp_path / "roomci_scenario.yml").read_text()


def test_adapter_outputs_compose_into_risk_report() -> None:
    from signaltwin.adapters.compose import compose_adapter_outputs

    normalized = compose_adapter_outputs(
        scenario="adapter_ready_fixture_scenario",
        building={
            "id": "villa-a",
            "location_type": "humid_coastal",
            "age_years": 8,
        },
        asset={
            "id": "room-101-north-wall",
            "type": "wood_wall",
            "orientation": "north",
            "material": {"primary": "wood"},
            "vulnerability": {"moisture": "high"},
        },
        maintenance={"last_inspection_days_ago": 180},
        expected={},
        outputs=_load_all_adapter_outputs(),
    )

    report = calculate_risk_report(normalized)

    assert report.asset_id == "room-101-north-wall"
    assert report.evidence
    assert report.recommendation.action


def test_readme_mentions_adapter_ready_mvp_without_hardware() -> None:
    text = (PROJECT_ROOT / "README.md").read_text()

    assert "Adapter-ready MVP" in text
    assert "No physical devices are required" in text
    assert "docs/device-io-assumptions.md" in text


def test_proposal_pack_mentions_adapter_ready_status() -> None:
    readme = (PROJECT_ROOT / "signaltwin_proposal_pack" / "README.md").read_text()
    completion = (
        PROJECT_ROOT / "signaltwin_proposal_pack" / "docs" / "mvp-completion-report.md"
    ).read_text()
    adapter_plan = (
        PROJECT_ROOT / "signaltwin_proposal_pack" / "docs" / "next-phase-adapter-plan.md"
    ).read_text()

    combined = "\n".join([readme, completion, adapter_plan])

    assert "Adapter-ready MVP" in combined
    assert "hardware is still not required" in combined
    assert "fixture adapters" in combined


def _load_all_adapter_outputs():
    adapters = [
        (BmsCsvAdapter(), "bms_context.csv"),
        (WifiCsiCsvAdapter(), "wifi_csi.csv"),
        (ThermalJsonAdapter(), "thermal_matrix.json"),
        (VisualJsonAdapter(), "visual_defects.json"),
        (AcousticJsonAdapter(), "acoustic_features.json"),
        (PztCsvAdapter(), "pzt_adc.csv"),
    ]
    return [
        adapter.load(AdapterInput(path=RAW_FIXTURE_DIR / fixture_name))
        for adapter, fixture_name in adapters
    ]
