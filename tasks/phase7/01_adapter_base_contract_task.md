# Task 01: Adapter Base Contract

Status: done

## Goal

Create a minimal adapter interface that lets device-specific sources be swapped without changing the risk engine.

## Domain Boundary

This task owns the adapter interface only. It does not parse any real format.

## Files

- Create `src/signaltwin/adapters/__init__.py`
- Create `src/signaltwin/adapters/base.py`
- Create `tests/test_adapter_contracts.py`

## TDD Checklist

- [x] RED: write `test_adapter_contract_requires_source_name_and_load`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_contract_requires_source_name_and_load -v
```

Expected failure:

- missing `signaltwin.adapters.base`

- [x] GREEN: implement `Adapter`, `AdapterInput`, and `AdapterOutput` primitives.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_contract_requires_source_name_and_load -v
```

Expected:

- test passes with a tiny in-test fake adapter

## Done Criteria

- Adapter returns normalized payloads, not risk reports.
- Adapter interface does not import `risk_engine`.

## Regression Verification

Run the Phase 7 regression command from `tasks/phase7/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters tests/test_adapter_contracts.py
git commit -m "feat: add adapter base contract"
```
