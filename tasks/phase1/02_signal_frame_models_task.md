# Task 02: Signal Frame Models

Status: done

## Goal

Model optional signal groups with bounded numeric fields so each signal domain can be validated independently.

## Domain Boundary

This task owns signal schema only:

- WiFi CSI
- PZT
- acoustic
- thermal
- visual inspection

It does not calculate drift or risk.

## Files

- Modify `src/signaltwin/schema.py`
- Modify `tests/test_schema_contracts.py`

## TDD Checklist

- [ ] RED: write `test_signal_scores_are_bounded_between_zero_and_one`.
- [ ] Verify RED:

```bash
pytest tests/test_schema_contracts.py::test_signal_scores_are_bounded_between_zero_and_one -v
```

Expected failure:

- invalid values are accepted or signal model is missing

- [ ] GREEN: add field constraints for score-like values:

```txt
csi_drift_score
baseline_similarity
packet_loss_rate
retransmission_rate
multipath_change_score
attenuation_delta
frequency_response_drift
thermal_gradient_score
visual defect severity
visual defect area_ratio
```

- [ ] Verify GREEN:

```bash
pytest tests/test_schema_contracts.py::test_signal_scores_are_bounded_between_zero_and_one -v
```

Expected:

- values below 0 or above 1 fail validation where the field is a normalized score

## Done Criteria

- Each signal domain can be present or absent.
- Present signal domains validate their own fields.
- Current sample scenarios remain valid.

## Regression Verification

Run the Phase 1 regression command from `tasks/phase1/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/schema.py tests/test_schema_contracts.py
git commit -m "feat: validate signal frame contracts"
```
