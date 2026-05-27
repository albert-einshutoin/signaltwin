# Phase 13 Goal: No-Hardware Demo Pipeline

## Goal

Create a one-command no-hardware demo pipeline that regenerates adapter inspection, baseline comparison, risk report, maintenance report, and RoomCI output.

## Scope

- demo runner
- deterministic output directory
- adapter-ready demo report
- proposal pack demo sync
- regression proving demo reproducibility

## Non-Goals

- No real hardware
- No dashboard hosting
- No cloud deployment
- No live BMS/API integration

## Expected Files

- Create `src/signaltwin/demo.py`
- Modify `src/signaltwin/cli.py`
- Create `tests/test_demo_pipeline.py`
- Create `outputs/demo/`
- Modify `signaltwin_proposal_pack/README.md`

## Done Criteria

- A single CLI command regenerates no-hardware demo outputs.
- Demo output is deterministic.
- Demo includes adapter fixture inspection and risk report evidence.
- Proposal pack points to the demo flow.
