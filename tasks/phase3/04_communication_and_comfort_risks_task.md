# Task 04: Communication And Comfort Risks

Status: done

## Goal

Score communication drift and comfort degradation from WiFi CSI, packet loss, multipath change, BMS occupancy, HVAC load, humidity, and thermal gradient.

## Domain Boundary

This task owns:

- `communication_drift_risk`
- `comfort_degradation_risk`

## Files

- Modify `src/signaltwin/risk_engine.py`
- Modify `tests/test_risk_engine.py`

## TDD Checklist

- [ ] RED: write `test_wireless_propagation_fixture_has_high_communication_drift`.
- [ ] RED: write `test_hvac_fixture_has_comfort_degradation_signal`.
- [ ] Verify RED:

```bash
pytest tests/test_risk_engine.py::test_wireless_propagation_fixture_has_high_communication_drift tests/test_risk_engine.py::test_hvac_fixture_has_comfort_degradation_signal -v
```

Expected failure:

- risk fields are missing or below expected levels

- [ ] GREEN: add communication and comfort rules.
- [ ] Verify GREEN:

```bash
pytest tests/test_risk_engine.py::test_wireless_propagation_fixture_has_high_communication_drift tests/test_risk_engine.py::test_hvac_fixture_has_comfort_degradation_signal -v
```

Expected:

- communication fixture produces high communication risk
- HVAC fixture produces medium-high comfort degradation risk

## Done Criteria

- Occupancy context can adjust communication risk but does not hide severe packet/SNR drift.
- Comfort degradation uses BMS and thermal/acoustic context without pretending to control HVAC.

## Regression Verification

Run the Phase 3 regression command from `tasks/phase3/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add src/signaltwin/risk_engine.py tests/test_risk_engine.py
git commit -m "feat: score communication and comfort risks"
```
