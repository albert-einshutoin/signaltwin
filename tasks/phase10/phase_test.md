# Phase 10 Test Plan

## Full Regression

```bash
pytest
```

Expected:

- exits 0

## Adapter Fixture Regression

```bash
pytest tests/test_adapter_ready_mvp.py tests/test_fixture_adapters.py -v
```

Expected:

- all adapter-ready MVP tests pass
- adapter output composition reaches the existing risk engine

## Scenario Engine Regression

```bash
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

Expected:

- both commands exit 0
- generated JSON, Markdown, and RoomCI YAML are non-empty

## Adapter-To-Risk Regression

```bash
pytest tests/test_adapter_ready_mvp.py::test_adapter_outputs_compose_into_risk_report -v
```

Expected:

- fixture adapter outputs are schema-validated
- adapter outputs are composed into one normalized scenario payload
- existing `calculate_risk_report` returns a report with evidence and recommendation
- `src/signaltwin/risk_engine.py` does not import adapter modules
