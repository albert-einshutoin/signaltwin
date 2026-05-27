from pathlib import Path

from signaltwin.normalizer import normalize_scenario
from signaltwin.scenario_loader import load_scenario
from signaltwin.schema import BmsContext, Signals


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_normalizes_bms_context_and_mock_signal_frames():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")

    normalized = normalize_scenario(scenario)

    assert normalized.scenario == "rainy_season_wood_wall_risk"
    assert normalized.asset_id == "room-101-north-wall"
    assert isinstance(normalized.bms, BmsContext)
    assert isinstance(normalized.signals, Signals)
    assert normalized.bms.humidity_7d_avg_percent == 82
    assert normalized.signals.wifi_csi.csi_drift_score == 0.18
    assert normalized.signals.pzt.attenuation_delta == 0.21
    assert normalized.signals.visual.detected_defects[0].type == "moss"


def test_missing_optional_signal_groups_normalize_without_error():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "communication_drift.yml")

    normalized = normalize_scenario(scenario)

    assert normalized.signals.wifi_csi.packet_loss_rate == 0.061
    assert normalized.signals.pzt is None
    assert normalized.signals.acoustic is None
    assert normalized.signals.thermal is None
    assert normalized.signals.visual is None


def test_normalized_output_separates_bms_and_signaltwin_signals():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "hvac_efficiency_drift.yml")

    normalized = normalize_scenario(scenario)

    assert normalized.bms.hvac_on_hours_7d is not None
    assert not hasattr(normalized.signals, "hvac_on_hours_7d")
    assert normalized.signals.thermal is not None
    assert normalized.signals.wifi_csi is not None


def test_normalized_output_preserves_asset_and_building_metadata():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")

    normalized = normalize_scenario(scenario)

    assert normalized.building.location_type == "coastal"
    assert normalized.building.age_years == 4
    assert normalized.asset.orientation == "north"
    assert normalized.asset.material.surface == "cedar_panel"
    assert normalized.asset.vulnerability.moisture == "high"
