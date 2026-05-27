# Phase 5 Test Plan

## Narrow Commands

```bash
pytest tests/test_cli.py -v
```

Expected:

- validate command passes for sample scenario
- run command writes output files
- invalid path exits non-zero

## Manual CLI Verification

```bash
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
find outputs/generated -maxdepth 1 -type f | sort
```

Expected:

- `risk_report.json`
- `maintenance_report.md`
- `roomci_scenario.yml`

## Phase Regression

```bash
pytest
```

Expected:

- exits 0
