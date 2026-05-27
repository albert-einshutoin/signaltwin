from __future__ import annotations

from pathlib import Path

import pytest

from signaltwin.adapters.base import AdapterInput
from signaltwin.adapters.config import load_adapter_fixture_config
from signaltwin.adapters.registry import get_adapter


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_baseline_snapshot_from_adapter_outputs() -> None:
    from signaltwin.baseline import create_baseline_snapshot

    snapshot = create_baseline_snapshot(
        baseline_id="fixture-baseline",
        captured_at="2026-05-24T10:00:00+09:00",
        outputs=_load_fixture_outputs(),
    )

    assert snapshot.baseline_id == "fixture-baseline"
    assert snapshot.captured_at == "2026-05-24T10:00:00+09:00"
    assert snapshot.bms["humidity_7d_avg_percent"] == 82.0
    assert snapshot.signals["wifi_csi"]["csi_drift_score"] == 0.18
    assert "risk_scores" not in snapshot.to_dict()


def test_baseline_snapshot_requires_baseline_id() -> None:
    from signaltwin.baseline import BaselineError, create_baseline_snapshot

    with pytest.raises(BaselineError, match="baseline_id"):
        create_baseline_snapshot(
            baseline_id="",
            captured_at="2026-05-24T10:00:00+09:00",
            outputs=_load_fixture_outputs(),
        )


def test_baseline_store_round_trips_json(tmp_path: Path) -> None:
    from signaltwin.baseline import create_baseline_snapshot, load_baseline_snapshot, save_baseline_snapshot

    snapshot = create_baseline_snapshot(
        baseline_id="fixture-baseline",
        captured_at="2026-05-24T10:00:00+09:00",
        outputs=_load_fixture_outputs(),
    )
    path = tmp_path / "baseline.json"

    save_baseline_snapshot(snapshot, path)
    loaded = load_baseline_snapshot(path)

    assert loaded == snapshot
    assert path.read_text().endswith("\n")


def test_baseline_store_reports_invalid_json(tmp_path: Path) -> None:
    from signaltwin.baseline import BaselineError, load_baseline_snapshot

    path = tmp_path / "baseline.json"
    path.write_text("{not-json")

    with pytest.raises(BaselineError, match="invalid baseline JSON"):
        load_baseline_snapshot(path)


def _load_fixture_outputs():
    config = load_adapter_fixture_config(PROJECT_ROOT / "configs" / "adapter-fixtures.yml")
    return [
        get_adapter(source.adapter).load(AdapterInput(path=source.path))
        for source in config.sources
    ]
