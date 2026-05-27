# Phase 10 Goal: Adapter-Ready MVP Readiness

## Goal

Close the no-hardware adapter-ready MVP with regression evidence and documentation.

## Scope

- all fixture adapters run
- adapter outputs compose into a normalized SignalTwin scenario
- composed adapter output reaches the existing risk engine
- all current scenarios still run
- docs updated for adapter-ready usage
- proposal pack synced with adapter-ready status
- final hardware MVP remains unexpanded

## Non-Goals

- No real hardware connection
- No dashboard/API
- No persistence
- No ML

## Expected Files

- Create or modify `tests/test_adapter_ready_mvp.py`
- Modify `README.md`
- Modify `signaltwin_proposal_pack/docs/next-phase-adapter-plan.md`
- Modify `tasks/status.md`
- Modify `tasks/phase10/phase_status.md`

## Done Criteria

- `pytest` passes.
- Adapter fixtures parse and produce normalized frames.
- Adapter outputs can be composed into a risk-scored normalized scenario.
- CLI Scenario Engine still runs.
- README states adapter-ready MVP is hardware-free.
- Final hardware MVP tasks are still not expanded.
