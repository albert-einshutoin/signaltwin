from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from signaltwin.adapters.base import AdapterError, AdapterInput
from signaltwin.adapters.registry import get_adapter


@dataclass(frozen=True)
class AdapterSourceConfig:
    name: str
    adapter: str
    normalized_key: str
    path: Path


@dataclass(frozen=True)
class AdapterFixtureConfig:
    sources: list[AdapterSourceConfig]


def load_adapter_fixture_config(path: str | Path) -> AdapterFixtureConfig:
    config_path = Path(path)
    try:
        raw = yaml.safe_load(config_path.read_text())
    except OSError as exc:
        raise AdapterError(source="adapter-config", path=config_path, message=str(exc)) from exc
    except yaml.YAMLError as exc:
        raise AdapterError(source="adapter-config", path=config_path, message=str(exc)) from exc

    if not isinstance(raw, dict) or not isinstance(raw.get("sources"), list):
        raise AdapterError(source="adapter-config", path=config_path, message="expected sources list")

    sources: list[AdapterSourceConfig] = []
    for index, source in enumerate(raw["sources"]):
        if not isinstance(source, dict):
            raise AdapterError(source="adapter-config", path=config_path, message=f"invalid source at index {index}")

        name = _required_str(source, "name", config_path)
        adapter_name = _required_str(source, "adapter", config_path)
        normalized_key = _required_str(source, "normalized_key", config_path)
        source_path = _resolve_path(config_path, _required_str(source, "path", config_path))

        adapter = get_adapter(adapter_name)
        if not source_path.is_file():
            raise AdapterError(source=name, path=source_path, message="missing fixture path")
        adapter_output = adapter.load(AdapterInput(path=source_path))
        if adapter_output.normalized_key != normalized_key:
            raise AdapterError(
                source=name,
                path=source_path,
                message=(
                    "normalized_key mismatch: "
                    f"config={normalized_key} adapter={adapter_output.normalized_key}"
                ),
            )

        sources.append(
            AdapterSourceConfig(
                name=name,
                adapter=adapter_name,
                normalized_key=normalized_key,
                path=source_path,
            )
        )

    return AdapterFixtureConfig(sources=sources)


def _required_str(source: dict, key: str, config_path: Path) -> str:
    value = source.get(key)
    if not isinstance(value, str) or not value:
        raise AdapterError(source="adapter-config", path=config_path, message=f"missing required field: {key}")
    return value


def _resolve_path(config_path: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (config_path.parent / ".." / path).resolve()
