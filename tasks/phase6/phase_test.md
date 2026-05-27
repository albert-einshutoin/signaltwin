# Phase 6 Test Plan

## Full Regression

```bash
pytest
```

Expected:

- exits 0

## Scenario Regression

```bash
for scenario in scenarios/*.yml; do
  python -m signaltwin.cli validate "$scenario"
done
```

Expected:

- every scenario exits 0

## End-to-End Output Check

```bash
rm -rf outputs/generated/*
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
python -m json.tool outputs/generated/risk_report.json >/dev/null
test -s outputs/generated/maintenance_report.md
test -s outputs/generated/roomci_scenario.yml
```

Expected:

- exits 0
- all output files exist and are non-empty
