from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from signaltwin.cli import app


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNNER = CliRunner()


def test_demo_runner_returns_expected_artifacts(tmp_path: Path) -> None:
    from signaltwin.demo import run_no_hardware_demo

    result = run_no_hardware_demo(output_dir=tmp_path)

    assert set(result.artifacts) == {
        "adapter_inspection.json",
        "drift_comparison.json",
        "drift_comparison.md",
        "risk_report.json",
        "maintenance_report.md",
        "roomci_scenario.yml",
        "api_response.example.json",
        "dashboard_view_model.example.json",
    }
    for artifact in result.artifacts.values():
        assert artifact.is_file()


def test_demo_cli_writes_outputs(tmp_path: Path) -> None:
    result = RUNNER.invoke(app, ["demo", "--output-dir", str(tmp_path)])

    assert result.exit_code == 0
    assert "adapter_inspection.json" in result.output
    assert (tmp_path / "risk_report.json").is_file()
    assert (tmp_path / "drift_comparison.md").is_file()
    assert (tmp_path / "api_response.example.json").is_file()
    assert "Traceback" not in result.output


def test_demo_outputs_are_deterministic(tmp_path: Path) -> None:
    from signaltwin.demo import run_no_hardware_demo

    first_dir = tmp_path / "first"
    second_dir = tmp_path / "second"

    first = run_no_hardware_demo(output_dir=first_dir)
    second = run_no_hardware_demo(output_dir=second_dir)

    assert sorted(first.artifacts) == sorted(second.artifacts)
    for name in first.artifacts:
        assert first.artifacts[name].read_text() == second.artifacts[name].read_text()


def test_demo_adapter_inspection_contains_all_normalized_keys(tmp_path: Path) -> None:
    from signaltwin.demo import run_no_hardware_demo

    result = run_no_hardware_demo(output_dir=tmp_path)
    payload = json.loads(result.artifacts["adapter_inspection.json"].read_text())

    assert [item["normalized_key"] for item in payload["sources"]] == [
        "bms",
        "wifi_csi",
        "thermal",
        "visual",
        "acoustic",
        "pzt",
    ]


def test_proposal_pack_mentions_no_hardware_demo_command() -> None:
    readme = (PROJECT_ROOT / "signaltwin_proposal_pack" / "README.md").read_text()
    completion = (
        PROJECT_ROOT / "signaltwin_proposal_pack" / "docs" / "mvp-completion-report.md"
    ).read_text()
    combined = "\n".join([readme, completion])

    assert "python -m signaltwin.cli demo --output-dir outputs/demo" in combined
    assert "No hardware is required" in combined
    assert "adapter inspection" in combined
