# Phase 0 Goal: Project Baseline

## Goal

Create a Python project baseline that can support TDD implementation of the minimal MVP without mixing setup work into domain tasks.

## Scope

- Python package skeleton
- test layout
- dependency declaration
- fixture discovery checks for existing scenarios
- formatting and import conventions
- deterministic output directory convention

## Non-Goals

- No risk scoring logic
- No YAML parsing beyond fixture existence checks
- No CLI behavior beyond importability if needed
- No hardware adapter work

## Expected Files

- Create `pyproject.toml`
- Create `src/signaltwin/__init__.py`
- Create `tests/test_project_baseline.py`
- Create `.gitignore`
- Create `outputs/generated/.gitkeep`

## Done Criteria

- `pytest` runs successfully.
- Python can import `signaltwin`.
- Runtime dependencies needed by the minimal MVP are declared: Pydantic v2, PyYAML, Typer, and pytest.
- Existing sample scenario files are detected.
- Generated outputs have a dedicated ignored directory.
- `tasks/phase0/phase_status.md` records evidence.
