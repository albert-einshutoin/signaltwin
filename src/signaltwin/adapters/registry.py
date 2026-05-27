from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from signaltwin.adapters.acoustic_json import AcousticJsonAdapter
from signaltwin.adapters.base import Adapter, AdapterError
from signaltwin.adapters.bms_csv import BmsCsvAdapter
from signaltwin.adapters.pzt_csv import PztCsvAdapter
from signaltwin.adapters.thermal_json import ThermalJsonAdapter
from signaltwin.adapters.visual_json import VisualJsonAdapter
from signaltwin.adapters.wifi_csi_csv import WifiCsiCsvAdapter


_ADAPTERS: dict[str, type[Adapter]] = {
    "bms_csv": BmsCsvAdapter,
    "wifi_csi_csv": WifiCsiCsvAdapter,
    "thermal_json": ThermalJsonAdapter,
    "visual_json": VisualJsonAdapter,
    "acoustic_json": AcousticJsonAdapter,
    "pzt_csv": PztCsvAdapter,
}


def registered_adapter_names() -> Iterable[str]:
    return tuple(sorted(_ADAPTERS))


def get_adapter(name: str) -> Adapter:
    adapter_type = _ADAPTERS.get(name)
    if adapter_type is None:
        raise AdapterError(source="adapter-registry", path=Path("."), message=f"unknown adapter: {name}")
    return adapter_type()
