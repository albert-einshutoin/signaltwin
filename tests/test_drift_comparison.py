from __future__ import annotations

from pathlib import Path

from signaltwin.adapters.base import AdapterInput
from signaltwin.adapters.config import load_adapter_fixture_config
from signaltwin.adapters.registry import get_adapter


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_comparison_detects_numeric_field_delta() -> None:
    from signaltwin.baseline import BaselineSnapshot
    from signaltwin.comparison import compare_to_baseline

    baseline = BaselineSnapshot(
        baseline_id="baseline-a",
        captured_at="2026-05-01T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 70.0},
        signals={"wifi_csi": {"csi_drift_score": 0.10}},
    )
    current = BaselineSnapshot(
        baseline_id="current-a",
        captured_at="2026-05-24T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 82.0},
        signals={"wifi_csi": {"csi_drift_score": 0.18}},
    )

    comparison = compare_to_baseline(baseline, current)

    assert comparison["bms"]["humidity_7d_avg_percent"]["delta"] == 12.0
    assert comparison["wifi_csi"]["csi_drift_score"]["delta"] == 0.08


def test_comparison_ignores_missing_optional_fields() -> None:
    from signaltwin.baseline import BaselineSnapshot
    from signaltwin.comparison import compare_to_baseline

    baseline = BaselineSnapshot(
        baseline_id="baseline-a",
        captured_at="2026-05-01T10:00:00+09:00",
        bms={},
        signals={"thermal": {"cold_spot_count": 4}},
    )
    current = BaselineSnapshot(
        baseline_id="current-a",
        captured_at="2026-05-24T10:00:00+09:00",
        bms={},
        signals={"thermal": {"thermal_gradient_score": 0.31}},
    )

    assert compare_to_baseline(baseline, current) == {}


def test_comparison_groups_results_by_normalized_key() -> None:
    from signaltwin.baseline import BaselineSnapshot
    from signaltwin.comparison import compare_to_baseline

    baseline = BaselineSnapshot(
        baseline_id="baseline-a",
        captured_at="2026-05-01T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 75.0},
        signals={"thermal": {"thermal_gradient_score": 0.2}, "pzt": {"attenuation_delta": 0.1}},
    )
    current = BaselineSnapshot(
        baseline_id="current-a",
        captured_at="2026-05-24T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 82.0},
        signals={"thermal": {"thermal_gradient_score": 0.31}, "pzt": {"attenuation_delta": 0.21}},
    )

    comparison = compare_to_baseline(baseline, current)

    assert list(comparison) == ["bms", "pzt", "thermal"]


def test_comparison_summary_exports_markdown() -> None:
    from signaltwin.baseline import BaselineSnapshot
    from signaltwin.comparison import compare_to_baseline, comparison_to_markdown

    baseline = BaselineSnapshot(
        baseline_id="baseline-a",
        captured_at="2026-05-01T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 75.0},
        signals={},
    )
    current = BaselineSnapshot(
        baseline_id="current-a",
        captured_at="2026-05-24T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 82.0},
        signals={},
    )

    markdown = comparison_to_markdown(compare_to_baseline(baseline, current))

    assert "# SignalTwin Drift Comparison" in markdown
    assert "humidity_7d_avg_percent" in markdown
    assert "+7" in markdown


def test_comparison_summary_exports_json_payload() -> None:
    from signaltwin.baseline import BaselineSnapshot
    from signaltwin.comparison import compare_to_baseline, comparison_to_json_payload

    baseline = BaselineSnapshot(
        baseline_id="baseline-a",
        captured_at="2026-05-01T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 75.0},
        signals={},
    )
    current = BaselineSnapshot(
        baseline_id="current-a",
        captured_at="2026-05-24T10:00:00+09:00",
        bms={"humidity_7d_avg_percent": 82.0},
        signals={},
    )

    payload = comparison_to_json_payload(compare_to_baseline(baseline, current))

    assert payload["groups"][0]["normalized_key"] == "bms"
    assert payload["groups"][0]["fields"][0]["field"] == "humidity_7d_avg_percent"


def test_baseline_docs_explain_fixture_based_comparison() -> None:
    doc = PROJECT_ROOT / "docs" / "baseline-and-comparison.md"

    text = doc.read_text()

    assert "fixture outputs" in text
    assert "risk scoring" in text
    assert "real baseline collection" in text


def _load_fixture_outputs():
    config = load_adapter_fixture_config(PROJECT_ROOT / "configs" / "adapter-fixtures.yml")
    return [
        get_adapter(source.adapter).load(AdapterInput(path=source.path))
        for source in config.sources
    ]
