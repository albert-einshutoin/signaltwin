# Task 05: Adapter Operations Docs

Status: done

## Goal

Document how to switch devices/programs by changing adapter config instead of the risk engine.

## Domain Boundary

This task owns docs only.

## Files

- Modify `docs/adapter-contract.md`
- Modify `README.md`
- Modify `tests/test_adapter_cli.py`

## TDD Checklist

- [x] RED: write `test_docs_describe_adapter_config_switching`.
- [x] Verify RED with the narrow test.
- [x] GREEN: document registry/config/CLI usage.
- [x] Verify GREEN with the same test.

## Done Criteria

- Docs explain adapter config switching.
- Docs reference `docs/device-io-assumptions.md`.
- Docs state risk engine remains unchanged.

## Regression Verification

Run the Phase 11 regression command from `tasks/phase11/phase_test.md`.
