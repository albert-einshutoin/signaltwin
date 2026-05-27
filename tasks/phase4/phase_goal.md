# Phase 4 Goal: Exporters

## Goal

Serialize risk engine outputs into the three minimal MVP artifacts.

## Scope

- `risk_report.json`
- `maintenance_report.md`
- `roomci_scenario.yml`
- deterministic key ordering and stable text

## Non-Goals

- No CLI argument handling
- No dashboard/API
- No external RoomCI execution

## Expected Files

- Create `src/signaltwin/exporters.py`
- Create `tests/test_exporters.py`

## Done Criteria

- Exported JSON validates against `RiskReport`.
- Markdown includes asset, score table, evidence, and recommendation.
- RoomCI YAML preserves BMS context and SignalTwin risk expectations.
