# Task 01: Project Skeleton

Status: done

## Goal

Create the smallest Python package structure needed for test-first development.

## Domain Boundary

This task owns packaging only. It must not implement schemas, loaders, risk rules, exporters, or CLI behavior.

## Files

- Create `pyproject.toml`
- Create `src/signaltwin/__init__.py`
- Create `tests/test_project_baseline.py`

## TDD Checklist

- [ ] RED: add `test_package_imports` in `tests/test_project_baseline.py`.
- [ ] Verify RED:

```bash
pytest tests/test_project_baseline.py::test_package_imports -v
```

Expected failure before implementation:

- `ModuleNotFoundError: No module named 'signaltwin'`

- [ ] GREEN: add package skeleton and project config.
- [ ] Verify GREEN:

```bash
pytest tests/test_project_baseline.py::test_package_imports -v
```

Expected:

- test passes

- [ ] REFACTOR: keep package metadata minimal and avoid unused dependencies.

## Done Criteria

- `import signaltwin` works in tests.
- `pyproject.toml` declares Python version and the minimal MVP dependencies: `pydantic>=2`, `pyyaml`, `typer`, and `pytest`.
- No domain behavior is added.

## Regression Verification

Run the Phase 0 regression command from `tasks/phase0/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add pyproject.toml src/signaltwin/__init__.py tests/test_project_baseline.py
git commit -m "chore: add project skeleton"
```
