from __future__ import annotations

import csv
import json
from pathlib import Path


RAW_FIXTURE_DIR = Path("fixtures/raw")


def test_bms_and_wifi_raw_fixtures_parse() -> None:
    bms_rows = _csv_rows(RAW_FIXTURE_DIR / "bms_context.csv")
    wifi_rows = _csv_rows(RAW_FIXTURE_DIR / "wifi_csi.csv")

    assert bms_rows[0].keys() >= {
        "timestamp",
        "room_id",
        "temperature_7d_avg_c",
        "humidity_7d_avg_percent",
        "illuminance_7d_avg_lux",
        "hvac_on_hours_7d",
        "dehumidify_on_hours_7d",
    }
    assert wifi_rows[0].keys() >= {
        "timestamp",
        "node_id",
        "path_id",
        "rssi_dbm",
        "snr_db",
        "packet_loss_rate",
        "retransmission_rate",
        "csi_drift_score",
        "multipath_change_score",
        "baseline_similarity",
    }


def test_thermal_and_visual_raw_fixtures_parse() -> None:
    thermal = _json_payload(RAW_FIXTURE_DIR / "thermal_matrix.json")
    visual = _json_payload(RAW_FIXTURE_DIR / "visual_defects.json")

    assert thermal["resolution"] == "32x24"
    assert len(thermal["matrix_c"]) == 24
    assert all(len(row) == 32 for row in thermal["matrix_c"])
    assert {"cold_spot_count", "thermal_gradient_score", "dew_point_margin_min_c"} <= thermal.keys()

    assert visual["detected_defects"]
    assert {"type", "severity"} <= visual["detected_defects"][0].keys()


def test_acoustic_and_pzt_raw_fixtures_parse() -> None:
    acoustic = _json_payload(RAW_FIXTURE_DIR / "acoustic_features.json")
    pzt_rows = _csv_rows(RAW_FIXTURE_DIR / "pzt_adc.csv")

    assert {
        "sample_rate_hz",
        "frequency_response_drift",
        "rt60_seconds",
        "unusual_noise_score",
        "baseline_similarity",
    } <= acoustic.keys()
    assert pzt_rows[0].keys() >= {
        "timestamp",
        "sensor_id",
        "asset_id",
        "sample_rate_hz",
        "mode",
        "baseline_id",
        "sample_index",
        "voltage",
    }


def test_raw_io_fixture_doc_mentions_all_fixture_files() -> None:
    text = Path("docs/raw-io-fixtures.md").read_text()

    for fixture_name in (
        "bms_context.csv",
        "wifi_csi.csv",
        "thermal_matrix.json",
        "visual_defects.json",
        "acoustic_features.json",
        "pzt_adc.csv",
    ):
        assert fixture_name in text


def _csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as fixture_file:
        return list(csv.DictReader(fixture_file))


def _json_payload(path: Path) -> dict:
    return json.loads(path.read_text())
