# Task 03: Proposal Pack Adapter Sync

Status: done

## Goal

Synchronize proposal docs with the adapter-ready MVP once fixture adapters exist.

## Domain Boundary

This task owns proposal docs only.

## Files

- Modify `signaltwin_proposal_pack/README.md`
- Modify `signaltwin_proposal_pack/docs/next-phase-adapter-plan.md`
- Modify `signaltwin_proposal_pack/docs/mvp-completion-report.md`

## TDD Checklist

- [x] RED: write `test_proposal_pack_mentions_adapter_ready_status`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_ready_mvp.py::test_proposal_pack_mentions_adapter_ready_status -v
```

Expected failure:

- proposal pack has no adapter-ready status section

- [x] GREEN: update proposal pack docs.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_ready_mvp.py::test_proposal_pack_mentions_adapter_ready_status -v
```

Expected:

- test passes

## Done Criteria

- Proposal pack states hardware is still not required.
- Proposal pack states fixture adapters are ready for selecting the first real hardware PoC.

## Regression Verification

Run the Phase 10 regression command from `tasks/phase10/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add signaltwin_proposal_pack tests/test_adapter_ready_mvp.py
git commit -m "docs: sync proposal pack with adapter-ready mvp"
```
