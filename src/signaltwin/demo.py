from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from signaltwin.adapters.base import AdapterInput
from signaltwin.adapters.compose import compose_adapter_outputs
from signaltwin.adapters.config import load_adapter_fixture_config
from signaltwin.adapters.registry import get_adapter
from signaltwin.baseline import create_baseline_snapshot, load_baseline_snapshot
from signaltwin.comparison import compare_to_baseline, comparison_to_json_payload, comparison_to_markdown
from signaltwin.exporters import write_maintenance_report_markdown, write_risk_report_json, write_roomci_scenario
from signaltwin.risk_engine import calculate_risk_report


@dataclass(frozen=True)
class DemoResult:
    artifacts: dict[str, Path]


def run_no_hardware_demo(
    *,
    output_dir: str | Path,
    config_path: str | Path = "configs/adapter-fixtures.yml",
    baseline_path: str | Path = "baselines/adapter_fixture_baseline.json",
) -> DemoResult:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    adapter_config = load_adapter_fixture_config(config_path)
    outputs = [
        get_adapter(source.adapter).load(AdapterInput(path=source.path))
        for source in adapter_config.sources
    ]

    artifacts: dict[str, Path] = {}
    artifacts["adapter_inspection.json"] = output_path / "adapter_inspection.json"
    artifacts["adapter_inspection.json"].write_text(
        json.dumps(_adapter_inspection_payload(adapter_config.sources, outputs), indent=2, sort_keys=True) + "\n"
    )

    current_snapshot = create_baseline_snapshot(
        baseline_id="adapter-fixture-current",
        captured_at="2026-05-24T10:00:00+09:00",
        outputs=outputs,
    )
    baseline = load_baseline_snapshot(baseline_path)
    comparison = compare_to_baseline(baseline, current_snapshot)

    artifacts["drift_comparison.json"] = output_path / "drift_comparison.json"
    artifacts["drift_comparison.json"].write_text(
        json.dumps(comparison_to_json_payload(comparison), indent=2, sort_keys=True) + "\n"
    )

    artifacts["drift_comparison.md"] = output_path / "drift_comparison.md"
    artifacts["drift_comparison.md"].write_text(comparison_to_markdown(comparison))

    normalized = compose_adapter_outputs(
        scenario="no_hardware_demo",
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
        outputs=outputs,
    )
    report = calculate_risk_report(normalized)

    artifacts["risk_report.json"] = output_path / "risk_report.json"
    write_risk_report_json(report, artifacts["risk_report.json"])

    artifacts["maintenance_report.md"] = output_path / "maintenance_report.md"
    write_maintenance_report_markdown(normalized, report, artifacts["maintenance_report.md"])

    artifacts["roomci_scenario.yml"] = output_path / "roomci_scenario.yml"
    write_roomci_scenario(normalized, report, artifacts["roomci_scenario.yml"])

    from signaltwin.api_contract import write_api_dashboard_examples

    artifacts.update(write_api_dashboard_examples(DemoResult(artifacts=dict(sorted(artifacts.items()))), output_path))

    return DemoResult(artifacts=dict(sorted(artifacts.items())))


def _adapter_inspection_payload(sources, outputs) -> dict:
    return {
        "sources": [
            {
                "name": source.name,
                "adapter": source.adapter,
                "normalized_key": output.normalized_key,
                "source_name": output.source_name,
                "fields": sorted(output.payload),
            }
            for source, output in zip(sources, outputs)
        ]
    }
