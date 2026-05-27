# Task 04: Acoustic And PZT Fixture Adapters

Status: done

## Goal

Parse acoustic feature and PZT ADC fixtures into normalized frame payloads.

## Domain Boundary

This task owns fixture parsing and simple feature mapping only. It does not implement full signal processing.

## Files

- Create `src/signaltwin/adapters/acoustic_json.py`
- Create `src/signaltwin/adapters/pzt_csv.py`
- Modify `tests/test_fixture_adapters.py`

## TDD Checklist

- [x] RED: write `test_acoustic_json_adapter_returns_acoustic_frame`.
- [x] RED: write `test_pzt_csv_adapter_returns_pzt_frame`.
- [x] RED: write `test_acoustic_json_adapter_rejects_invalid_score`.
- [x] RED: write `test_pzt_csv_adapter_reports_missing_samples`.
- [x] Verify RED:

```bash
pytest tests/test_fixture_adapters.py::test_acoustic_json_adapter_returns_acoustic_frame tests/test_fixture_adapters.py::test_pzt_csv_adapter_returns_pzt_frame -v
```

Expected failure:

- missing adapter modules

- [x] GREEN: implement fixture parsers.
- [x] Verify GREEN:

```bash
pytest tests/test_fixture_adapters.py::test_acoustic_json_adapter_returns_acoustic_frame tests/test_fixture_adapters.py::test_pzt_csv_adapter_returns_pzt_frame -v
```

Expected:

- acoustic output includes frequency response drift and baseline similarity
- PZT output includes attenuation delta, resonance shift, and baseline similarity
- invalid acoustic score values raise `AdapterError`
- empty or malformed PZT samples raise `AdapterError`

## Done Criteria

- No microphone, speaker, PZT, or ADC hardware is required.
- Adapters return schema-validated `AdapterOutput`.

## Regression Verification

Run the Phase 9 regression command from `tasks/phase9/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/adapters/acoustic_json.py src/signaltwin/adapters/pzt_csv.py tests/test_fixture_adapters.py
git commit -m "feat: add acoustic and pzt fixture adapters"
```
