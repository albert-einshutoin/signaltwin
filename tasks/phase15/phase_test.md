# Phase 15 Test Plan

## Narrow Commands

```bash
pytest tests/test_pre_hardware_readiness.py -v
```

Expected:

- readiness docs mention all no-hardware phases
- hardware handoff docs define entry criteria
- no detailed real-hardware implementation tasks are expanded

## Final No-Hardware Regression

```bash
pytest
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
python -m signaltwin.cli demo --output-dir outputs/demo
```

Expected:

- all commands exit 0
- generated outputs are deterministic and non-empty
- no command requires hardware
