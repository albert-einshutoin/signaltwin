# Task 01: Demo Runner

Status: done

## Goal

Implement a demo runner that orchestrates fixture adapters, baseline comparison, and existing risk report generation.

## Domain Boundary

This task owns orchestration logic only.

## Files

- Create `src/signaltwin/demo.py`
- Create `tests/test_demo_pipeline.py`

## TDD Checklist

- [x] RED: write `test_demo_runner_returns_expected_artifacts`.
- [x] Verify RED.
- [x] GREEN: implement demo runner.
- [x] Verify GREEN.

## Done Criteria

- Demo runner returns artifact names and payloads.
- Demo runner uses fixture adapters and existing risk engine.
- No hardware access is attempted.

## Regression Verification

Run the Phase 13 regression command from `tasks/phase13/phase_test.md`.
