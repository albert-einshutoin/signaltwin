from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from signaltwin.schema import RiskReport, SignalTwinScenario


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_yaml_fixture(name: str) -> dict:
    with (PROJECT_ROOT / "scenarios" / name).open() as handle:
        return yaml.safe_load(handle)


def test_scenario_requires_core_sections():
    scenario = load_yaml_fixture("rainy_season_wood_wall.yml")

    validated = SignalTwinScenario.model_validate(scenario)

    assert validated.scenario == "rainy_season_wood_wall_risk"
    assert validated.building.id == "villa-a"
    assert validated.asset.id == "room-101-north-wall"

    for section in ("building", "asset", "maintenance", "bms", "signals", "expected"):
        broken = deepcopy(scenario)
        broken.pop(section)

        with pytest.raises(ValidationError) as exc_info:
            SignalTwinScenario.model_validate(broken)

        assert section in str(exc_info.value)


def test_all_repository_scenarios_match_schema_contract():
    for path in sorted((PROJECT_ROOT / "scenarios").glob("*.yml")):
        scenario = SignalTwinScenario.model_validate(yaml.safe_load(path.read_text()))

        assert scenario.scenario
        assert scenario.asset.id
        assert scenario.expected


def test_signal_scores_are_bounded_between_zero_and_one():
    scenario = load_yaml_fixture("communication_drift.yml")

    valid = SignalTwinScenario.model_validate(scenario)
    assert valid.signals.wifi_csi.csi_drift_score == pytest.approx(0.31)

    broken = deepcopy(scenario)
    broken["signals"]["wifi_csi"]["csi_drift_score"] = 1.01

    with pytest.raises(ValidationError) as exc_info:
        SignalTwinScenario.model_validate(broken)

    assert "csi_drift_score" in str(exc_info.value)

    broken = deepcopy(load_yaml_fixture("coastal_villa_moss_risk.yml"))
    broken["signals"]["visual"]["detected_defects"][0]["severity"] = -0.01

    with pytest.raises(ValidationError) as exc_info:
        SignalTwinScenario.model_validate(broken)

    assert "severity" in str(exc_info.value)


def test_optional_signal_groups_can_be_absent():
    scenario = load_yaml_fixture("communication_drift.yml")

    validated = SignalTwinScenario.model_validate(scenario)

    assert validated.signals.wifi_csi is not None
    assert validated.signals.pzt is None
    assert validated.signals.acoustic is None
    assert validated.signals.thermal is None
    assert validated.signals.visual is None


def test_maintenance_rejects_unknown_field_names():
    scenario = load_yaml_fixture("rainy_season_wood_wall.yml")
    scenario["maintenance"] = {"last_inspection_days": 180}

    with pytest.raises(ValidationError) as exc_info:
        SignalTwinScenario.model_validate(scenario)

    assert "last_inspection_days" in str(exc_info.value)


def test_bms_rejects_unknown_field_names():
    scenario = load_yaml_fixture("rainy_season_wood_wall.yml")
    scenario["bms"]["humidity_7d_avg_pct"] = scenario["bms"].pop("humidity_7d_avg_percent")

    with pytest.raises(ValidationError) as exc_info:
        SignalTwinScenario.model_validate(scenario)

    assert "humidity_7d_avg_pct" in str(exc_info.value)


def test_risk_report_requires_evidence_and_recommendation():
    report = {
        "asset_id": "room-101-north-wall",
        "risk_scores": {
            "moisture_risk": 0.78,
            "mold_risk": 0.66,
            "moss_risk": 0.0,
            "wood_deformation_risk": 0.41,
            "crack_or_void_risk": 0.35,
            "communication_drift_risk": 0.36,
            "comfort_degradation_risk": 0.58,
        },
        "evidence": ["7-day average humidity is 82%"],
        "recommendation": {
            "priority": "high",
            "action": "Inspect the north wall within 30 days",
            "maintenance_type": "moisture_inspection",
        },
    }

    validated = RiskReport.model_validate(report)

    assert validated.risk_scores.moss_risk == pytest.approx(0.0)
    assert validated.recommendation.priority == "high"

    for section in ("evidence", "recommendation"):
        broken = deepcopy(report)
        broken.pop(section)

        with pytest.raises(ValidationError) as exc_info:
            RiskReport.model_validate(broken)

        assert section in str(exc_info.value)


def test_risk_report_example_matches_output_contract():
    report_path = PROJECT_ROOT / "outputs" / "risk_report.example.json"

    report = RiskReport.model_validate_json(report_path.read_text())

    assert report.asset_id == "room-101-north-wall"
    assert report.risk_scores.moisture_risk == pytest.approx(0.78)
    assert report.risk_scores.moss_risk is None
