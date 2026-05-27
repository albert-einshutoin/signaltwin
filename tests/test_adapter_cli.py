from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from signaltwin.cli import app


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNNER = CliRunner()


def test_adapter_inspect_cli_outputs_normalized_keys() -> None:
    result = RUNNER.invoke(
        app,
        ["adapter", "inspect", "--config", str(PROJECT_ROOT / "configs" / "adapter-fixtures.yml")],
    )

    assert result.exit_code == 0
    for normalized_key in ("bms", "wifi_csi", "thermal", "visual", "acoustic", "pzt"):
        assert normalized_key in result.output
    assert "moisture_risk" not in result.output


def test_adapter_inspect_cli_reports_invalid_config_without_traceback(tmp_path: Path) -> None:
    missing_config = tmp_path / "missing.yml"

    result = RUNNER.invoke(app, ["adapter", "inspect", "--config", str(missing_config)])

    assert result.exit_code != 0
    assert str(missing_config) in result.output
    assert "Traceback" not in result.output


def test_adapter_inspect_cli_reports_adapter_error_without_traceback(tmp_path: Path) -> None:
    config_path = tmp_path / "adapter-fixtures.yml"
    fixture_path = tmp_path / "broken.csv"
    fixture_path.write_text("timestamp,room_id\n2026-05-24T10:00:00+09:00,room-a\n")
    config_path.write_text(
        f"""
sources:
  - name: broken-bms
    adapter: bms_csv
    normalized_key: bms
    path: {fixture_path}
""".strip()
    )

    result = RUNNER.invoke(app, ["adapter", "inspect", "--config", str(config_path)])

    assert result.exit_code != 0
    assert "missing required column" in result.output
    assert "Traceback" not in result.output


def test_docs_describe_adapter_config_switching() -> None:
    readme = (PROJECT_ROOT / "README.md").read_text()
    adapter_contract = (PROJECT_ROOT / "docs" / "adapter-contract.md").read_text()
    combined = "\n".join([readme, adapter_contract])

    assert "configs/adapter-fixtures.yml" in combined
    assert "docs/device-io-assumptions.md" in combined
    assert "risk engine remains unchanged" in combined
