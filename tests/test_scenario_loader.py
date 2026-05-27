from pathlib import Path

import pytest

from signaltwin.scenario_loader import ScenarioLoadError, load_scenario


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_loads_rainy_season_wood_wall_scenario():
    scenario = load_scenario(PROJECT_ROOT / "scenarios" / "rainy_season_wood_wall.yml")

    assert scenario.scenario == "rainy_season_wood_wall_risk"
    assert scenario.asset.id == "room-101-north-wall"


def test_load_scenario_accepts_string_path():
    scenario = load_scenario(str(PROJECT_ROOT / "scenarios" / "communication_drift.yml"))

    assert scenario.scenario == "wireless_propagation_drift"


def test_all_repository_scenarios_load():
    paths = sorted((PROJECT_ROOT / "scenarios").glob("*.yml"))

    assert paths
    for path in paths:
        scenario = load_scenario(path)
        assert scenario.scenario
        assert scenario.asset.id


def test_missing_scenario_path_reports_path():
    missing_path = PROJECT_ROOT / "scenarios" / "missing.yml"

    with pytest.raises(ScenarioLoadError) as exc_info:
        load_scenario(missing_path)

    assert str(missing_path) in str(exc_info.value)


def test_invalid_scenario_reports_validation_section(tmp_path):
    invalid_path = tmp_path / "invalid.yml"
    invalid_path.write_text(
        """
scenario: invalid
asset:
  id: asset-a
  type: wall
  orientation: north
maintenance: {}
bms: {}
signals: {}
expected: {}
""".strip()
    )

    with pytest.raises(ScenarioLoadError) as exc_info:
        load_scenario(invalid_path)

    message = str(exc_info.value)
    assert str(invalid_path) in message
    assert "building" in message


def test_invalid_yaml_reports_parse_error(tmp_path):
    invalid_path = tmp_path / "invalid-yaml.yml"
    invalid_path.write_text("scenario: [broken")

    with pytest.raises(ScenarioLoadError) as exc_info:
        load_scenario(invalid_path)

    message = str(exc_info.value)
    assert str(invalid_path) in message
    assert "YAML" in message
