# Task 03: Adapter Contract Documentation

Status: done

## Goal

Document how adapters keep assumed devices replaceable.

## Domain Boundary

This task owns docs only.

## Files

- Create `docs/adapter-contract.md`
- Create or update `docs/device-io-assumptions.md`

## TDD Checklist

- [x] RED: write `test_adapter_contract_doc_mentions_all_source_families`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_contract_doc_mentions_all_source_families -v
```

Expected failure:

- missing `docs/adapter-contract.md`

- [x] GREEN: document BMS, WiFi CSI, thermal, visual, acoustic, and PZT adapter families.
- [x] GREEN: document assumed devices, assumed capture programs, raw fixture files, normalized keys, and replacement rules.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_contract_doc_mentions_all_source_families -v
```

Expected:

- test passes

## Done Criteria

- Docs state that adapters normalize data and do not score risk.
- Docs state assumed devices can be replaced by other sources with the same normalized frame.
- `docs/device-io-assumptions.md` is the source of truth for I/O assumptions before hardware exists.

## Regression Verification

Run the Phase 7 regression command from `tasks/phase7/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add docs/adapter-contract.md docs/device-io-assumptions.md tests/test_adapter_contracts.py
git commit -m "docs: add adapter contract"
```
