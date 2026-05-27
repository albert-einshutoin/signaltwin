from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from signaltwin.adapters.base import AdapterError


def read_first_csv_row(path: Path, source: str, required_columns: set[str]) -> dict[str, str]:
    rows = read_csv_rows(path, source, required_columns)
    return rows[0]


def read_csv_rows(path: Path, source: str, required_columns: set[str]) -> list[dict[str, str]]:
    try:
        with path.open(newline="") as fixture_file:
            reader = csv.DictReader(fixture_file)
            fieldnames = set(reader.fieldnames or [])
            missing = required_columns - fieldnames
            if missing:
                raise AdapterError(
                    source=source,
                    path=path,
                    message=f"missing required column: {sorted(missing)[0]}",
                )
            rows = list(reader)
    except AdapterError:
        raise
    except OSError as exc:
        raise AdapterError(source=source, path=path, message=str(exc)) from exc

    if not rows:
        raise AdapterError(source=source, path=path, message="no samples")
    return rows


def read_json_object(path: Path, source: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise AdapterError(source=source, path=path, message=str(exc)) from exc

    if not isinstance(payload, dict):
        raise AdapterError(source=source, path=path, message="JSON root must be an object")
    return payload


def float_value(row: dict[str, Any], key: str, source: str, path: Path) -> float:
    try:
        return float(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise AdapterError(source=source, path=path, message=f"invalid numeric value: {key}") from exc


def int_value(row: dict[str, Any], key: str, source: str, path: Path) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise AdapterError(source=source, path=path, message=f"invalid integer value: {key}") from exc
