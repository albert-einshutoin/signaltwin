# Task 02: Demo CLI Command

Status: done

## Goal

Expose the no-hardware demo through CLI.

## Domain Boundary

This task owns CLI wiring only.

## Files

- Modify `src/signaltwin/cli.py`
- Modify `tests/test_demo_pipeline.py`

## TDD Checklist

- [x] RED: write `test_demo_cli_writes_outputs`.
- [x] Verify RED.
- [x] GREEN: implement `signaltwin demo --output-dir outputs/demo`.
- [x] Verify GREEN.

## Done Criteria

- CLI writes demo outputs.
- CLI reports output paths.
- CLI errors do not show tracebacks.

## Regression Verification

Run the Phase 13 regression command from `tasks/phase13/phase_test.md`.
