from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, ClassVar, Literal

from pydantic import ValidationError

from signaltwin.schema import (
    AcousticSignal,
    BmsContext,
    PztSignal,
    StrictBaseModel,
    ThermalSignal,
    VisualSignal,
    WifiCsiSignal,
)

NormalizedKey = Literal["bms", "wifi_csi", "pzt", "acoustic", "thermal", "visual"]


class AdapterError(Exception):
    def __init__(self, source: str, path: str | Path, message: str) -> None:
        self.source = source
        self.path = Path(path)
        self.message = message
        super().__init__(f"{source}: {self.path}: {message}")


@dataclass(frozen=True)
class AdapterInput:
    path: Path


@dataclass(frozen=True)
class AdapterOutput:
    source_family: str
    source_name: str
    path: Path
    normalized_key: NormalizedKey
    payload: dict[str, Any]

    _payload_models: ClassVar[dict[NormalizedKey, type[StrictBaseModel]]] = {
        "bms": BmsContext,
        "wifi_csi": WifiCsiSignal,
        "pzt": PztSignal,
        "acoustic": AcousticSignal,
        "thermal": ThermalSignal,
        "visual": VisualSignal,
    }

    def __post_init__(self) -> None:
        model = self._payload_models.get(self.normalized_key)
        if model is None:
            raise AdapterError(
                source=self.source_name,
                path=self.path,
                message=f"unknown normalized key: {self.normalized_key}",
            )

        try:
            validated = model.model_validate(self.payload)
        except ValidationError as exc:
            raise AdapterError(
                source=self.source_name,
                path=self.path,
                message=f"invalid {self.normalized_key} payload: {exc}",
            ) from exc

        object.__setattr__(self, "path", Path(self.path))
        object.__setattr__(self, "payload", validated.model_dump(exclude_none=True))


class Adapter(ABC):
    source_name: str

    @abstractmethod
    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        raise NotImplementedError
