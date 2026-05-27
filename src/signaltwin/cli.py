from __future__ import annotations

from pathlib import Path

import typer

from signaltwin.adapters.base import AdapterError, AdapterInput
from signaltwin.adapters.config import load_adapter_fixture_config
from signaltwin.adapters.registry import get_adapter
from signaltwin.baseline import BaselineError
from signaltwin.demo import run_no_hardware_demo
from signaltwin.exporters import (
    write_maintenance_report_markdown,
    write_risk_report_json,
    write_roomci_scenario,
)
from signaltwin.normalizer import normalize_scenario
from signaltwin.risk_engine import calculate_risk_report
from signaltwin.scenario_loader import ScenarioLoadError, load_scenario


app = typer.Typer(no_args_is_help=True)
adapter_app = typer.Typer(no_args_is_help=True)
app.add_typer(adapter_app, name="adapter")


@app.command()
def validate(scenario_path: Path) -> None:
    try:
        scenario = load_scenario(scenario_path)
    except ScenarioLoadError as exc:
        _fail(exc)

    typer.echo(f"valid: {scenario.scenario}")
    typer.echo(f"asset: {scenario.asset.id}")


@app.command()
def run(scenario_path: Path, output_dir: Path = typer.Option(Path("outputs/generated"))) -> None:
    try:
        scenario = normalize_scenario(load_scenario(scenario_path))
    except ScenarioLoadError as exc:
        _fail(exc)

    report = calculate_risk_report(scenario)
    output_dir.mkdir(parents=True, exist_ok=True)

    risk_report_path = output_dir / "risk_report.json"
    maintenance_report_path = output_dir / "maintenance_report.md"
    roomci_scenario_path = output_dir / "roomci_scenario.yml"

    write_risk_report_json(report, risk_report_path)
    write_maintenance_report_markdown(scenario, report, maintenance_report_path)
    write_roomci_scenario(scenario, report, roomci_scenario_path)

    typer.echo(f"wrote: {risk_report_path}")
    typer.echo(f"wrote: {maintenance_report_path}")
    typer.echo(f"wrote: {roomci_scenario_path}")


@adapter_app.command("inspect")
def inspect_adapters(config: Path = typer.Option(Path("configs/adapter-fixtures.yml"), "--config")) -> None:
    try:
        adapter_config = load_adapter_fixture_config(config)
        for source in adapter_config.sources:
            adapter = get_adapter(source.adapter)
            output = adapter.load(AdapterInput(path=source.path))
            typer.echo(
                f"{source.name}: adapter={source.adapter} normalized_key={output.normalized_key} "
                f"source={output.source_name} fields={','.join(sorted(output.payload))}"
            )
    except AdapterError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1)


@app.command()
def demo(output_dir: Path = typer.Option(Path("outputs/demo"), "--output-dir")) -> None:
    try:
        result = run_no_hardware_demo(output_dir=output_dir)
    except (AdapterError, BaselineError) as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1)

    for artifact in result.artifacts.values():
        typer.echo(f"wrote: {artifact}")


def _fail(exc: ScenarioLoadError) -> None:
    typer.echo(str(exc), err=True)
    raise typer.Exit(code=1)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
