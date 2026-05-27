from __future__ import annotations

from typing import Any

from signaltwin.schema import (
    Asset,
    BmsContext,
    Building,
    Maintenance,
    Signals,
    SignalTwinScenario,
    StrictBaseModel,
)


class NormalizedScenario(StrictBaseModel):
    scenario: str
    building_id: str
    asset_id: str
    building: Building
    asset: Asset
    bms: BmsContext
    maintenance: Maintenance
    signals: Signals
    expected: dict[str, Any]


def normalize_scenario(scenario: SignalTwinScenario) -> NormalizedScenario:
    return NormalizedScenario(
        scenario=scenario.scenario,
        building_id=scenario.building.id,
        asset_id=scenario.asset.id,
        building=scenario.building,
        asset=scenario.asset,
        bms=scenario.bms,
        maintenance=scenario.maintenance,
        signals=scenario.signals,
        expected=dict(scenario.expected),
    )
