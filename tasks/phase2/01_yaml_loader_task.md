# Task 01: YAML Loader

Status: done

## Goal

Load one YAML file into a `SignalTwinScenario`.

## Domain Boundary

This task owns file-to-schema conversion only.

## Files

- Create `src/signaltwin/scenario_loader.py`
- Create `tests/test_scenario_loader.py`

## TDD Checklist

- [ ] RED: write `test_loads_rainy_season_wood_wall_scenario`.
- [ ] Verify RED:

```bash
pytest tests/test_scenario_loader.py::test_loads_rainy_season_wood_wall_scenario -v
```

Expected failure:

- `ImportError` or missing `load_scenario`

- [ ] GREEN: implement `load_scenario(path: str | Path) -> SignalTwinScenario`.
- [ ] Verify GREEN:

```bash
pytest tests/test_scenario_loader.py::test_loads_rainy_season_wood_wall_scenario -v
```

Expected:

- scenario name and asset id match the fixture

## Done Criteria

- Loader accepts `str` and `Path`.
- Loader returns schema object, not a raw dictionary.

## Regression Verification

Run the Phase 2 regression command from `tasks/phase2/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/scenario_loader.py tests/test_scenario_loader.py
git commit -m "feat: load scenario yaml"
```
