from __future__ import annotations

import importlib
import inspect
from pathlib import Path

import pytest

from signaltwin.adapters.base import AdapterError, AdapterInput
from signaltwin.risk_engine import calculate_risk_report
from signaltwin.scenario_loader import load_scenario


RAW_FIXTURE_DIR = Path("fixtures/raw")


def test_bms_csv_adapter_returns_bms_context() -> None:
    from signaltwin.adapters.bms_csv import BmsCsvAdapter

    output = BmsCsvAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "bms_context.csv"))

    assert output.normalized_key == "bms"
    assert output.payload["humidity_7d_avg_percent"] == 82.0
    assert output.payload["temperature_7d_avg_c"] == 24.2
    assert output.payload["illuminance_7d_avg_lux"] == 110.0
    assert output.payload["hvac_on_hours_7d"] == 88.0


def test_bms_csv_adapter_reports_missing_required_column(tmp_path: Path) -> None:
    from signaltwin.adapters.bms_csv import BmsCsvAdapter

    broken = tmp_path / "bms_context.csv"
    broken.write_text("timestamp,room_id\n2026-05-24T10:00:00+09:00,room-a\n")

    with pytest.raises(AdapterError, match="missing required column"):
        BmsCsvAdapter().load(AdapterInput(path=broken))


def test_wifi_csi_csv_adapter_returns_wifi_frame() -> None:
    from signaltwin.adapters.wifi_csi_csv import WifiCsiCsvAdapter

    output = WifiCsiCsvAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "wifi_csi.csv"))

    assert output.normalized_key == "wifi_csi"
    assert output.payload["csi_drift_score"] == 0.18
    assert output.payload["snr_db"] == 22.4
    assert output.payload["packet_loss_rate"] == 0.061
    assert output.payload["baseline_similarity"] == 0.83


def test_wifi_csi_csv_adapter_rejects_out_of_range_scores(tmp_path: Path) -> None:
    from signaltwin.adapters.wifi_csi_csv import WifiCsiCsvAdapter

    broken = tmp_path / "wifi_csi.csv"
    broken.write_text(
        "timestamp,node_id,path_id,rssi_dbm,snr_db,packet_loss_rate,retransmission_rate,csi_drift_score,multipath_change_score,baseline_similarity\n"
        "2026-05-24T10:00:00+09:00,node,path,-64,22.4,1.4,0.08,0.18,0.24,0.83\n"
    )

    with pytest.raises(AdapterError, match="invalid wifi_csi payload"):
        WifiCsiCsvAdapter().load(AdapterInput(path=broken))


def test_thermal_json_adapter_returns_thermal_frame() -> None:
    from signaltwin.adapters.thermal_json import ThermalJsonAdapter

    output = ThermalJsonAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "thermal_matrix.json"))

    assert output.normalized_key == "thermal"
    assert output.payload["cold_spot_count"] == 4
    assert output.payload["thermal_gradient_score"] == 0.31
    assert output.payload["dew_point_margin_min_c"] == 1.2


def test_thermal_json_adapter_rejects_invalid_matrix_shape(tmp_path: Path) -> None:
    from signaltwin.adapters.thermal_json import ThermalJsonAdapter

    broken = tmp_path / "thermal_matrix.json"
    broken.write_text('{"resolution": "32x24", "matrix_c": [[21.0]], "thermal_gradient_score": 0.2}')

    with pytest.raises(AdapterError, match="32x24"):
        ThermalJsonAdapter().load(AdapterInput(path=broken))


def test_visual_json_adapter_returns_visual_frame() -> None:
    from signaltwin.adapters.visual_json import VisualJsonAdapter

    output = VisualJsonAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "visual_defects.json"))

    assert output.normalized_key == "visual"
    assert output.payload["detected_defects"][0]["type"] == "moss"
    assert output.payload["detected_defects"][0]["severity"] == 0.42


def test_visual_json_adapter_rejects_invalid_defect_severity(tmp_path: Path) -> None:
    from signaltwin.adapters.visual_json import VisualJsonAdapter

    broken = tmp_path / "visual_defects.json"
    broken.write_text('{"detected_defects": [{"type": "moss", "severity": 2.0}]}')

    with pytest.raises(AdapterError, match="invalid visual payload"):
        VisualJsonAdapter().load(AdapterInput(path=broken))


def test_acoustic_json_adapter_returns_acoustic_frame() -> None:
    from signaltwin.adapters.acoustic_json import AcousticJsonAdapter

    output = AcousticJsonAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "acoustic_features.json"))

    assert output.normalized_key == "acoustic"
    assert output.payload["frequency_response_drift"] == 0.19
    assert output.payload["baseline_similarity"] == 0.81


def test_acoustic_json_adapter_rejects_invalid_score(tmp_path: Path) -> None:
    from signaltwin.adapters.acoustic_json import AcousticJsonAdapter

    broken = tmp_path / "acoustic_features.json"
    broken.write_text('{"frequency_response_drift": 1.5, "baseline_similarity": 0.81}')

    with pytest.raises(AdapterError, match="invalid acoustic payload"):
        AcousticJsonAdapter().load(AdapterInput(path=broken))


def test_pzt_csv_adapter_returns_pzt_frame() -> None:
    from signaltwin.adapters.pzt_csv import PztCsvAdapter

    output = PztCsvAdapter().load(AdapterInput(path=RAW_FIXTURE_DIR / "pzt_adc.csv"))

    assert output.normalized_key == "pzt"
    assert output.payload["peak_amplitude_delta"] > 0
    assert output.payload["attenuation_delta"] == 0.21
    assert output.payload["resonance_shift_percent"] == 6.8
    assert output.payload["baseline_similarity"] == 0.71


def test_pzt_csv_adapter_uses_fixture_feature_values(tmp_path: Path) -> None:
    from signaltwin.adapters.pzt_csv import PztCsvAdapter

    fixture = tmp_path / "pzt_adc.csv"
    fixture.write_text(
        "timestamp,sensor_id,asset_id,sample_rate_hz,mode,baseline_id,sample_index,voltage,resonance_shift_percent,attenuation_delta,baseline_similarity\n"
        "2026-05-24T10:00:00+09:00,pzt-a,asset-a,860,passive,baseline-a,0,0.01,4.2,0.16,0.77\n"
        "2026-05-24T10:00:00+09:00,pzt-a,asset-a,860,passive,baseline-a,1,0.09,4.2,0.16,0.77\n"
    )

    output = PztCsvAdapter().load(AdapterInput(path=fixture))

    assert output.payload["resonance_shift_percent"] == 4.2
    assert output.payload["attenuation_delta"] == 0.16
    assert output.payload["baseline_similarity"] == 0.77


def test_pzt_csv_adapter_reports_missing_samples(tmp_path: Path) -> None:
    from signaltwin.adapters.pzt_csv import PztCsvAdapter

    broken = tmp_path / "pzt_adc.csv"
    broken.write_text(
        "timestamp,sensor_id,asset_id,sample_rate_hz,mode,baseline_id,sample_index,voltage,resonance_shift_percent,attenuation_delta,baseline_similarity\n"
    )

    with pytest.raises(AdapterError, match="no samples"):
        PztCsvAdapter().load(AdapterInput(path=broken))


def test_risk_engine_does_not_import_adapters() -> None:
    risk_engine = importlib.import_module("signaltwin.risk_engine")
    source = inspect.getsource(risk_engine)

    assert "signaltwin.adapters" not in source
    assert "adapters." not in source
    assert not any(name.startswith("Adapter") for name in risk_engine.__dict__)


def test_existing_scenario_engine_still_runs_with_fixture_adapters_present() -> None:
    scenario = load_scenario("scenarios/rainy_season_wood_wall.yml")

    report = calculate_risk_report(scenario)

    assert report.evidence
    assert report.recommendation.action
