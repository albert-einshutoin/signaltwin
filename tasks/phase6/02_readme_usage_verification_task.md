# Task 02: README Usage Verification

Status: done

## Goal

Update README with commands that have been executed locally.

## Domain Boundary

This task owns user-facing minimal MVP instructions only.

## Files

- Modify `README.md`

## TDD Checklist

- [ ] RED: run the intended README commands before documenting them.

```bash
pytest
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

Expected before README update:

- commands pass, but README does not yet document them

- [ ] GREEN: add concise install, test, validate, and run sections to README.
- [ ] Verify GREEN by re-running the documented commands exactly as written.

## Done Criteria

- README commands are copied from verified commands, not invented.
- README still states that Edge Kit hardware is outside the minimal MVP.

## Regression Verification

Run the Phase 6 regression command from `tasks/phase6/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add README.md
git commit -m "docs: document minimal mvp usage"
```
