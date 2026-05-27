from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from signaltwin.adapters.base import AdapterOutput


class BaselineError(Exception):
    def __init__(self, path: str | Path | None, message: str) -> None:
        self.path = Path(path) if path is not None else None
        self.message = message
        prefix = f"{self.path}: " if self.path is not None else ""
        super().__init__(f"{prefix}{message}")


@dataclass(frozen=True)
class BaselineSnapshot:
    baseline_id: str
    captured_at: str
    bms: dict[str, Any]
    signals: dict[str, dict[str, Any]]

    def __post_init__(self) -> None:
        if not self.baseline_id:
            raise BaselineError(path=None, message="baseline_id is required")
        if not self.captured_at:
            raise BaselineError(path=None, message="captured_at is required")

    def to_dict(self) -> dict[str, Any]:
        return {
            "baseline_id": self.baseline_id,
            "captured_at": self.captured_at,
            "bms": dict(self.bms),
            "signals": {key: dict(value) for key, value in self.signals.items()},
        }


def create_baseline_snapshot(
    *, baseline_id: str, captured_at: str, outputs: Iterable[AdapterOutput]
) -> BaselineSnapshot:
    bms: dict[str, Any] = {}
    signals: dict[str, dict[str, Any]] = {}

    for output in outputs:
        if output.normalized_key == "bms":
            bms.update(output.payload)
        else:
            signals[output.normalized_key] = dict(output.payload)

    return BaselineSnapshot(
        baseline_id=baseline_id,
        captured_at=captured_at,
        bms=bms,
        signals=signals,
    )


def save_baseline_snapshot(snapshot: BaselineSnapshot, path: str | Path) -> None:
    baseline_path = Path(path)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    baseline_path.write_text(json.dumps(snapshot.to_dict(), indent=2, sort_keys=True) + "\n")


def load_baseline_snapshot(path: str | Path) -> BaselineSnapshot:
    baseline_path = Path(path)
    try:
        raw = json.loads(baseline_path.read_text())
    except json.JSONDecodeError as exc:
        raise BaselineError(path=baseline_path, message=f"invalid baseline JSON: {exc}") from exc
    except OSError as exc:
        raise BaselineError(path=baseline_path, message=str(exc)) from exc

    if not isinstance(raw, dict):
        raise BaselineError(path=baseline_path, message="baseline JSON root must be an object")

    try:
        return BaselineSnapshot(
            baseline_id=raw["baseline_id"],
            captured_at=raw["captured_at"],
            bms=dict(raw.get("bms", {})),
            signals={key: dict(value) for key, value in raw.get("signals", {}).items()},
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise BaselineError(path=baseline_path, message=f"invalid baseline payload: {exc}") from exc
