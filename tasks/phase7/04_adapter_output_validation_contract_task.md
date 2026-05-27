# Task 04: Adapter Output Validation Contract

Status: done

## Goal

Make adapter outputs schema-validated so fixture parsers cannot return arbitrary dictionaries.

## Domain Boundary

This task owns the adapter output contract only. It does not parse real fixture files.

## Files

- Modify `src/signaltwin/adapters/base.py`
- Modify `tests/test_adapter_contracts.py`

## TDD Checklist

- [x] RED: write `test_adapter_output_validates_signal_payload`.
- [x] RED: write `test_adapter_output_validates_bms_payload`.
- [x] RED: write `test_adapter_output_rejects_unknown_normalized_key`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_output_validates_signal_payload tests/test_adapter_contracts.py::test_adapter_output_validates_bms_payload tests/test_adapter_contracts.py::test_adapter_output_rejects_unknown_normalized_key -v
```

Expected failure:

- adapter output validation helper is missing

- [x] GREEN: implement validation for `bms`, `wifi_csi`, `pzt`, `acoustic`, `thermal`, and `visual`.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_contracts.py::test_adapter_output_validates_signal_payload tests/test_adapter_contracts.py::test_adapter_output_validates_bms_payload tests/test_adapter_contracts.py::test_adapter_output_rejects_unknown_normalized_key -v
```

Expected:

- valid payloads are accepted
- invalid payloads raise `AdapterError`
- unknown normalized keys raise `AdapterError`

## Done Criteria

- `AdapterOutput` includes `source_family`, `source_name`, `path`, `normalized_key`, and `payload`.
- Payload validation uses existing schema models from `signaltwin.schema`.
- Adapter validation does not import `risk_engine`.

## Regression Verification

Run the Phase 7 regression command from `tasks/phase7/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/base.py tests/test_adapter_contracts.py
git commit -m "feat: validate adapter output payloads"
```
