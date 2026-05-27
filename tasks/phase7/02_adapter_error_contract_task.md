# Task 02: Adapter Error Contract

Status: done

## Goal

Define adapter errors that can be surfaced by CLI without tracebacks.

## Domain Boundary

This task owns adapter error types only.

## Files

- Modify `src/signaltwin/adapters/base.py`
- Modify `tests/test_adapter_contracts.py`

## TDD Checklist

- [x] RED: write `test_adapter_error_includes_source_and_path`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_error_includes_source_and_path -v
```

Expected failure:

- missing `AdapterError`

- [x] GREEN: implement `AdapterError(source, path, message)`.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_error_includes_source_and_path -v
```

Expected:

- error text includes source, path, and message

## Done Criteria

- Adapter errors are concise and user-readable.
- No traceback is required for normal user mistakes.

## Regression Verification

Run the Phase 7 regression command from `tasks/phase7/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/base.py tests/test_adapter_contracts.py
git commit -m "feat: add adapter error contract"
```
