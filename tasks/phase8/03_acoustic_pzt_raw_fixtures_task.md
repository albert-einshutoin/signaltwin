# Task 03: Acoustic And PZT Fixtures

Status: done

## Goal

Create acoustic feature and PZT ADC raw fixtures for adapter development without microphones or ADC hardware.

## Domain Boundary

This task owns raw fixture contracts only. It does not implement audio or waveform feature extraction.

## Files

- Create `fixtures/raw/acoustic_features.json`
- Create `fixtures/raw/pzt_adc.csv`
- Modify `tests/test_raw_fixture_contracts.py`

## TDD Checklist

- [x] RED: write `test_acoustic_and_pzt_raw_fixtures_parse`.
- [x] Verify RED:

```bash
pytest tests/test_raw_fixture_contracts.py::test_acoustic_and_pzt_raw_fixtures_parse -v
```

Expected failure:

- missing fixture files

- [x] GREEN: add JSON/CSV fixtures.
- [x] Verify GREEN:

```bash
pytest tests/test_raw_fixture_contracts.py::test_acoustic_and_pzt_raw_fixtures_parse -v
```

Expected:

- acoustic fixture exposes feature-level values
- PZT fixture exposes timestamp/sample values plus metadata needed for simple feature extraction

## Done Criteria

- Acoustic fixture can represent INMP441-like feature output but is not tied to that hardware.
- PZT fixture can represent ADS1115-like ADC capture but is not tied to that ADC.

## Regression Verification

Run the Phase 8 regression command from `tasks/phase8/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add fixtures/raw/acoustic_features.json fixtures/raw/pzt_adc.csv tests/test_raw_fixture_contracts.py
git commit -m "test: add acoustic and pzt raw fixtures"
```
