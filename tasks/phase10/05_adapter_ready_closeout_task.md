# Task 05: Adapter-Ready Closeout

Status: done

## Goal

Close Phase 7-10 and leave the final hardware MVP unexpanded until a hardware path is selected.

## Domain Boundary

This task owns status documentation only.

## Files

- Modify `tasks/status.md`
- Modify `tasks/phase7/phase_status.md`
- Modify `tasks/phase8/phase_status.md`
- Modify `tasks/phase9/phase_status.md`
- Modify `tasks/phase10/phase_status.md`

## TDD Checklist

- [x] RED: inspect task board for incomplete Phase 7-10 statuses.
- [x] Verify RED:

```bash
rg -n "Phase (7|8|9|10).*\\| todo|Status: todo|\\| [^|]+ \\| todo \\|" tasks/phase7 tasks/phase8 tasks/phase9 tasks/phase10 tasks/status.md --glob '!**/05_adapter_ready_closeout_task.md'
```

Expected before closeout:

- incomplete statuses are listed

- [x] GREEN: after implementation and verification, update statuses and evidence.
- [x] Verify GREEN:

```bash
rg -n "Phase (7|8|9|10).*\\| todo|Status: todo|\\| [^|]+ \\| todo \\|" tasks/phase7 tasks/phase8 tasks/phase9 tasks/phase10 tasks/status.md --glob '!**/05_adapter_ready_closeout_task.md'
```

Expected:

- no incomplete Phase 7-10 statuses remain

## Done Criteria

- Phase 7-10 statuses reflect tested reality.
- Adapter-ready MVP evidence includes adapter-to-risk regression results.
- Final hardware MVP remains a roadmap item, not an implementation task list.

## Regression Verification

Run the Phase 10 regression command from `tasks/phase10/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add tasks
git commit -m "docs: close adapter-ready mvp task board"
```
