# Task 02: Adapter Fixture Config

Status: done

## Goal

Define a config file that lists which adapter parses which fixture path.

## Domain Boundary

This task owns config schema and loading only.

## Files

- Create `configs/adapter-fixtures.yml`
- Create `src/signaltwin/adapters/config.py`
- Modify `tests/test_adapter_registry.py`

## TDD Checklist

- [x] RED: write `test_adapter_fixture_config_loads_all_sources`.
- [x] RED: write `test_adapter_fixture_config_rejects_missing_path`.
- [x] Verify RED with the narrow tests.
- [x] GREEN: implement config loader.
- [x] Verify GREEN with the same tests.

## Done Criteria

- Config names every fixture adapter.
- Config paths are validated before adapter execution.
- Config format is documented by tests.

## Regression Verification

Run the Phase 11 regression command from `tasks/phase11/phase_test.md`.
