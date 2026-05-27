# Task 03: Output Hygiene

Status: done

## Goal

Create a deterministic generated-output convention so tests and CLI runs do not overwrite curated examples.

## Domain Boundary

This task owns output directory hygiene only. It must not implement exporters.

## Files

- Create `.gitignore`
- Create `outputs/generated/.gitkeep`
- Modify `tests/test_project_baseline.py`

## TDD Checklist

- [ ] RED: add `test_generated_output_directory_exists`.
- [ ] Verify RED:

```bash
pytest tests/test_project_baseline.py::test_generated_output_directory_exists -v
```

Expected failure before implementation:

- assertion that `outputs/generated` does not exist

- [ ] GREEN: create `outputs/generated/.gitkeep` and ignore generated files while keeping `.gitkeep`.
- [ ] Verify GREEN:

```bash
pytest tests/test_project_baseline.py::test_generated_output_directory_exists -v
```

Expected:

- test passes

## Done Criteria

- Generated files go under `outputs/generated/`.
- Curated examples under `outputs/` remain untouched by default CLI runs.

## Regression Verification

Run the Phase 0 regression command from `tasks/phase0/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add .gitignore outputs/generated/.gitkeep tests/test_project_baseline.py
git commit -m "chore: add generated output convention"
```
