from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError
from yaml import YAMLError

from signaltwin.schema import SignalTwinScenario


class ScenarioLoadError(Exception):
    pass


def load_scenario(path: str | Path) -> SignalTwinScenario:
    scenario_path = Path(path)

    try:
        raw = _read_yaml_mapping(scenario_path)
        return SignalTwinScenario.model_validate(raw)
    except FileNotFoundError as exc:
        raise ScenarioLoadError(f"Scenario file not found: {scenario_path}") from exc
    except YAMLError as exc:
        raise ScenarioLoadError(f"Failed to parse YAML scenario {scenario_path}: {exc}") from exc
    except ValidationError as exc:
        raise ScenarioLoadError(f"Invalid scenario {scenario_path}: {exc}") from exc


def _read_yaml_mapping(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        loaded = yaml.safe_load(handle)

    if not isinstance(loaded, dict):
        raise YAMLError("scenario root must be a mapping")

    return loaded
