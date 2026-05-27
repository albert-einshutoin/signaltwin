# Task 01: Adapter Registry

Status: done

## Goal

Create a registry that resolves adapter names without hard-coding imports in callers.

## Domain Boundary

This task owns registry lookup only. It does not implement CLI or config parsing.

## Files

- Create `src/signaltwin/adapters/registry.py`
- Create `tests/test_adapter_registry.py`

## TDD Checklist

- [x] RED: write `test_registry_resolves_all_fixture_adapters`.
- [x] RED: write `test_registry_rejects_unknown_adapter`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_registry.py::test_registry_resolves_all_fixture_adapters tests/test_adapter_registry.py::test_registry_rejects_unknown_adapter -v
```

Expected failure:

- registry module is missing

- [x] GREEN: implement registry for BMS, WiFi CSI, thermal, visual, acoustic, and PZT fixture adapters.
- [x] Verify GREEN with the same command.

## Done Criteria

- Registry returns adapter instances.
- Unknown adapter names produce user-readable errors.
- Registry does not import `risk_engine`.

## Regression Verification

Run the Phase 11 regression command from `tasks/phase11/phase_test.md`.
