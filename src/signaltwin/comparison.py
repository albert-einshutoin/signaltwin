from __future__ import annotations

from typing import Any

from signaltwin.baseline import BaselineSnapshot


Comparison = dict[str, dict[str, dict[str, float]]]


def compare_to_baseline(baseline: BaselineSnapshot, current: BaselineSnapshot) -> Comparison:
    comparison: Comparison = {}

    _compare_payload_group(comparison, "bms", baseline.bms, current.bms)

    for normalized_key in sorted(set(baseline.signals) | set(current.signals)):
        _compare_payload_group(
            comparison,
            normalized_key,
            baseline.signals.get(normalized_key, {}),
            current.signals.get(normalized_key, {}),
        )

    return comparison


def comparison_to_json_payload(comparison: Comparison) -> dict[str, Any]:
    groups = []
    for normalized_key, fields in comparison.items():
        groups.append(
            {
                "normalized_key": normalized_key,
                "fields": [
                    {
                        "field": field,
                        "baseline": values["baseline"],
                        "current": values["current"],
                        "delta": values["delta"],
                    }
                    for field, values in fields.items()
                ],
            }
        )
    return {"groups": groups}


def comparison_to_markdown(comparison: Comparison) -> str:
    lines = ["# SignalTwin Drift Comparison", ""]
    if not comparison:
        return "\n".join(lines + ["No comparable numeric drift fields."]) + "\n"

    for normalized_key, fields in comparison.items():
        lines.extend([f"## {normalized_key}", "", "| Field | Baseline | Current | Delta |", "|---|---:|---:|---:|"])
        for field, values in fields.items():
            lines.append(
                f"| {field} | {_format_number(values['baseline'])} | "
                f"{_format_number(values['current'])} | {_format_signed(values['delta'])} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _compare_payload_group(
    comparison: Comparison, normalized_key: str, baseline_payload: dict[str, Any], current_payload: dict[str, Any]
) -> None:
    fields: dict[str, dict[str, float]] = {}
    for field in sorted(set(baseline_payload) & set(current_payload)):
        baseline_value = baseline_payload[field]
        current_value = current_payload[field]
        if _is_number(baseline_value) and _is_number(current_value):
            baseline_number = float(baseline_value)
            current_number = float(current_value)
            delta = round(current_number - baseline_number, 6)
            if delta != 0:
                fields[field] = {
                    "baseline": baseline_number,
                    "current": current_number,
                    "delta": delta,
                }

    if fields:
        comparison[normalized_key] = fields


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _format_number(value: float) -> str:
    return f"{value:g}"


def _format_signed(value: float) -> str:
    return f"{value:+g}"
