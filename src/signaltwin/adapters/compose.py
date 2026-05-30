from __future__ import annotations

from typing import Any, Iterable

from signaltwin.adapters.base import AdapterOutput
from signaltwin.normalizer import NormalizedScenario, normalize_scenario
from signaltwin.schema import SignalTwinScenario


def compose_adapter_outputs(
    *,
    scenario: str,
    building: dict[str, Any],
    asset: dict[str, Any],
    maintenance: dict[str, Any],
    expected: dict[str, Any],
    outputs: Iterable[AdapterOutput],
) -> NormalizedScenario:
    bms: dict[str, Any] = {}
    signals: dict[str, dict[str, Any]] = {}

    for output in outputs:
        if output.normalized_key == "bms":
            bms.update(output.payload)
        else:
            signals[output.normalized_key] = output.payload

    scenario_model = SignalTwinScenario.model_validate(
        {
            "scenario": scenario,
            "building": building,
            "asset": asset,
            "maintenance": maintenance,
            "bms": bms,
            "signals": signals,
            "expected": expected,
        }
    )
    return normalize_scenario(scenario_model)
