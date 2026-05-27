# Task 04: Scenario Normalization

Status: done

## Goal

Normalize validated scenario objects into internal BMS and mock signal frames before risk scoring.

## Domain Boundary

This task owns in-memory normalization only. It does not calculate risk, export reports, or call hardware adapters.

Scenario-provided signal values are the minimal MVP mock signal frames. Real sensor adapters remain outside the minimal MVP.

## Files

- Create `src/signaltwin/normalizer.py`
- Create `tests/test_normalizer.py`

## TDD Checklist

- [ ] RED: write `test_normalizes_bms_context_and_mock_signal_frames`.
- [ ] RED: write `test_missing_optional_signal_groups_normalize_without_error`.
- [ ] Verify RED:

```bash
pytest tests/test_normalizer.py::test_normalizes_bms_context_and_mock_signal_frames tests/test_normalizer.py::test_missing_optional_signal_groups_normalize_without_error -v
```

Expected failure:

- missing `normalize_scenario`

- [ ] GREEN: implement `normalize_scenario(scenario)` with separate normalized `bms` and `signals` fields.
- [ ] Verify GREEN:

```bash
pytest tests/test_normalizer.py::test_normalizes_bms_context_and_mock_signal_frames tests/test_normalizer.py::test_missing_optional_signal_groups_normalize_without_error -v
```

Expected:

- normalized output exposes BMS context separately from SignalTwin signal frames
- optional signal groups can be absent without exceptions

## Done Criteria

- Risk engine tasks consume normalized data rather than raw YAML dictionaries.
- BMS remains external context.
- Mock signal frame generation is satisfied by converting scenario signal values into normalized frames.

## Regression Verification

Run the Phase 2 regression command from `tasks/phase2/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/normalizer.py tests/test_normalizer.py tasks/phase2
git commit -m "feat: normalize scenario inputs"
```
