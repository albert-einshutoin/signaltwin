# Phase 5 Goal: CLI Flow

## Goal

Expose the minimal MVP through a CLI that validates and runs scenarios.

## Scope

- `signaltwin validate <scenario.yml>`
- `signaltwin run <scenario.yml> --output-dir <dir>`
- user-facing errors
- deterministic output names

## Non-Goals

- No daemon/API
- No dashboard
- No hardware adapter commands

## Expected Files

- Create `src/signaltwin/cli.py`
- Create `tests/test_cli.py`

## Done Criteria

- CLI validates sample scenarios.
- CLI run writes all three output artifacts.
- CLI errors are non-zero and actionable.
