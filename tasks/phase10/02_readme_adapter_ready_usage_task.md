# Task 02: README Adapter-Ready Usage

Status: done

## Goal

Document the no-hardware adapter-ready MVP and make clear it is not the final hardware MVP.

## Domain Boundary

This task owns README documentation only.

## Files

- Modify `README.md`

## TDD Checklist

- [x] RED: write `test_readme_mentions_adapter_ready_mvp_without_hardware`.
- [x] Verify RED:

```bash
pytest tests/test_adapter_ready_mvp.py::test_readme_mentions_adapter_ready_mvp_without_hardware -v
```

Expected failure:

- README section missing

- [x] GREEN: add adapter-ready usage section.
- [x] Verify GREEN:

```bash
pytest tests/test_adapter_ready_mvp.py::test_readme_mentions_adapter_ready_mvp_without_hardware -v
```

Expected:

- test passes

## Done Criteria

- README distinguishes minimal MVP, adapter-ready MVP, and final hardware MVP.
- README states assumed devices are replaceable through adapters.

## Regression Verification

Run the Phase 10 regression command from `tasks/phase10/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add README.md tests/test_adapter_ready_mvp.py
git commit -m "docs: document adapter-ready mvp"
```
