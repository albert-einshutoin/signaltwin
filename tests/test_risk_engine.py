from pathlib import Path

import pytest

from signaltwin.normalizer import normalize_scenario
from signaltwin.risk_engine import calculate_risk_report
from signaltwin.scenario_loader import load_scenario


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def report_for(scenario_name: str):
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / scenario_name)
    return calculate_risk_report(normalize_scenario(scenario))


def test_rainy_season_wall_has_high_moisture_risk():
    report = report_for("rainy_season_wood_wall.yml")

    assert report.risk_scores.moisture_risk >= 0.70
    assert_evidence_contains(report.evidence, "humidity")
    assert_evidence_contains(report.evidence, "dew point")
    assert_evidence_contains(report.evidence, "cedar")
    assert_evidence_contains(report.evidence, "PZT")
    assert_evidence_contains(report.evidence, "inspection")


def test_coastal_villa_visual_moss_drives_moss_risk():
    report = report_for("coastal_villa_moss_risk.yml")

    assert report.risk_scores.moss_risk >= 0.70
    assert_evidence_contains(report.evidence, "visual moss")
    assert_evidence_contains(report.evidence, "cleaning")


def test_pzt_and_visual_crack_create_structural_drift_evidence():
    report = report_for("rainy_season_wood_wall.yml")

    assert report.risk_scores.wood_deformation_risk >= 0.35
    assert report.risk_scores.crack_or_void_risk >= 0.30
    assert_evidence_contains(report.evidence, "resonance")
    assert_evidence_contains(report.evidence, "attenuation")
    assert_evidence_contains(report.evidence, "crack")


def test_wireless_propagation_fixture_has_high_communication_drift():
    report = report_for("communication_drift.yml")

    assert report.risk_scores.communication_drift_risk >= 0.70
    assert_evidence_contains(report.evidence, "CSI")
    assert_evidence_contains(report.evidence, "packet loss")
    assert_evidence_contains(report.evidence, "SNR")


def test_hvac_fixture_has_comfort_degradation_signal():
    report = report_for("hvac_efficiency_drift.yml")

    assert report.risk_scores.comfort_degradation_risk >= 0.60
    assert_evidence_contains(report.evidence, "HVAC")
    assert_evidence_contains(report.evidence, "thermal gradient")


@pytest.mark.parametrize(
    ("scenario_name", "expected_action"),
    [
        ("rainy_season_wood_wall.yml", "within 30 days"),
        ("communication_drift.yml", "AP position or interference"),
        ("hvac_efficiency_drift.yml", "filter and airflow"),
    ],
)
def test_recommendation_matches_highest_actionable_risk(scenario_name, expected_action):
    report = report_for(scenario_name)

    assert report.recommendation.priority in {"medium_high", "high"}
    assert expected_action in report.recommendation.action
    assert report.recommendation.maintenance_type


def test_all_scenarios_produce_bounded_scores_and_evidence():
    for path in sorted((PROJECT_ROOT / "scenarios").glob("*.yml")):
        report = report_for(path.name)
        scores = report.risk_scores.model_dump(exclude_none=True)

        assert report.asset_id
        assert report.evidence
        assert all(0.0 <= value <= 1.0 for value in scores.values())


def test_risk_scores_do_not_depend_on_expected_labels():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")
    normalized = normalize_scenario(scenario)
    altered = normalized.model_copy(
        update={
            "expected": {
                "moisture_risk": "low",
                "mold_risk": "low",
                "moss_risk": "low",
                "comfort_degradation_risk": "low",
                "maintenance_recommendation": "none",
            },
        },
    )

    original_report = calculate_risk_report(normalized)
    altered_report = calculate_risk_report(altered)

    assert altered_report.risk_scores == original_report.risk_scores
    assert altered_report.recommendation == original_report.recommendation


def test_zero_dew_point_margin_is_treated_as_high_moisture_risk():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")
    normalized = normalize_scenario(scenario)
    thermal = normalized.signals.thermal.model_copy(update={"dew_point_margin_min_c": 0.0})
    altered = normalized.model_copy(
        update={"signals": normalized.signals.model_copy(update={"thermal": thermal})},
    )

    report = calculate_risk_report(altered)

    assert_evidence_contains(report.evidence, "dew point margin is only 0C")


def test_missing_thermal_signal_does_not_create_mold_dew_point_penalty():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "communication_drift.yml")
    normalized = normalize_scenario(scenario)

    report = calculate_risk_report(normalized)

    assert report.risk_scores.mold_risk == 0.0


def assert_evidence_contains(evidence: list[str], expected_text: str):
    assert any(expected_text.lower() in item.lower() for item in evidence), evidence
