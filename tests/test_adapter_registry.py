from __future__ import annotations

from pathlib import Path

import pytest

from signaltwin.adapters.base import AdapterError


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_registry_resolves_all_fixture_adapters() -> None:
    from signaltwin.adapters.registry import get_adapter, registered_adapter_names

    expected = {
        "bms_csv",
        "wifi_csi_csv",
        "thermal_json",
        "visual_json",
        "acoustic_json",
        "pzt_csv",
    }

    assert set(registered_adapter_names()) == expected
    for adapter_name in expected:
        assert get_adapter(adapter_name).source_name


def test_registry_rejects_unknown_adapter() -> None:
    from signaltwin.adapters.registry import get_adapter

    with pytest.raises(AdapterError, match="unknown adapter"):
        get_adapter("missing_adapter")


def test_adapter_fixture_config_loads_all_sources() -> None:
    from signaltwin.adapters.config import load_adapter_fixture_config

    config = load_adapter_fixture_config(PROJECT_ROOT / "configs" / "adapter-fixtures.yml")

    assert [source.normalized_key for source in config.sources] == [
        "bms",
        "wifi_csi",
        "thermal",
        "visual",
        "acoustic",
        "pzt",
    ]
    assert all(source.path.is_file() for source in config.sources)


def test_adapter_fixture_config_rejects_missing_path(tmp_path: Path) -> None:
    from signaltwin.adapters.config import load_adapter_fixture_config

    config_path = tmp_path / "adapter-fixtures.yml"
    config_path.write_text(
        """
sources:
  - name: broken
    adapter: bms_csv
    normalized_key: bms
    path: missing.csv
""".strip()
    )

    with pytest.raises(AdapterError, match="missing fixture path"):
        load_adapter_fixture_config(config_path)


def test_adapter_fixture_config_rejects_adapter_key_mismatch(tmp_path: Path) -> None:
    from signaltwin.adapters.config import load_adapter_fixture_config

    config_path = tmp_path / "adapter-fixtures.yml"
    fixture_path = tmp_path / "bms_context.csv"
    fixture_path.write_text(
        "timestamp,room_id,temperature_7d_avg_c,humidity_7d_avg_percent,illuminance_7d_avg_lux,"
        "hvac_on_hours_7d,dehumidify_on_hours_7d\n"
        "2026-05-24T10:00:00+09:00,room-a,24.2,82,110,88,36\n"
    )
    config_path.write_text(
        f"""
sources:
  - name: mismatched
    adapter: bms_csv
    normalized_key: wifi_csi
    path: {fixture_path}
""".strip()
    )

    with pytest.raises(AdapterError, match="normalized_key mismatch"):
        load_adapter_fixture_config(config_path)
