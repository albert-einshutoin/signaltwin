# SignalTwin Task Board

This directory is the operational task board for completing the minimal MVP.

The minimal MVP is the hardware-free SignalTwin Scenario Engine:

- load `scenarios/*.yml`
- validate BMS, asset, maintenance, and signal inputs
- calculate explainable rule-based risk scores
- generate evidence
- export JSON, Markdown, and RoomCI scenario outputs
- expose the flow through a CLI
- prove behavior with tests before implementation

## Task Structure

Each phase lives under `tasks/phaseN/`.

Required files per phase:

- `phase_goal.md`: scope, non-goals, expected files, and done criteria
- `phase_test.md`: exact verification commands and expected results
- `phase_status.md`: phase board using the shared status values
- `NN_short_name_task.md`: one focused task file per domain or implementation slice

Shared status values:

- `todo`: not started
- `in_progress`: currently being implemented
- `blocked`: cannot proceed without a decision or dependency
- `review`: implementation is done, verification or review remains
- `done`: tests, docs, and phase evidence are complete

## TDD Rules

Every implementation task must follow Red-Green-Refactor.

1. RED: write one failing test for one behavior.
2. Verify RED: run the narrow test and confirm it fails for the expected reason.
3. GREEN: write the smallest implementation that passes.
4. Verify GREEN: run the narrow test and confirm it passes.
5. REFACTOR: clean names or duplication only after green.
6. Regression: run the phase test commands before marking the task done.

No production code should be added without a failing test first. If implementation appears before a test, delete it or rewrite the task to restore the RED step.

## Task File Requirements

Each task file must include:

- Goal
- Domain boundary
- Files to create or modify
- Test-first checklist
- Narrow verification command
- Regression verification command
- Done criteria
- Commit checkpoint suggestion

Keep tasks small enough that one task can be reviewed independently. Prefer a task that adds one model, one rule group, one exporter, or one CLI behavior over a task that changes the whole system.

## Minimal MVP Phase Order

| Phase | Name | Purpose |
|---:|---|---|
| 0 | Project Baseline | Create Python package, tooling, test command, and repository invariants. |
| 1 | Schema Contracts | Define Pydantic models for scenarios and output reports. |
| 2 | Scenario Loading And Normalization | Load YAML scenarios, validate contract errors, and normalize BMS/signal frames. |
| 3 | Risk Engine | Implement explainable rule-based risk scoring, including mold/moss handling. |
| 4 | Exporters | Export JSON risk report, Markdown maintenance report, and RoomCI scenario YAML. |
| 5 | CLI Flow | Provide `signaltwin validate` and `signaltwin run`. |
| 6 | MVP Readiness | Run fixture regressions and document the minimal MVP as complete. |

## Completion Rule

A phase is not complete until:

- all task statuses are `done`
- `phase_test.md` commands pass
- generated outputs are deterministic
- evidence is recorded in `phase_status.md`
- the next phase has no known blocker

## Minimal MVP Contract Coverage

The task board must cover every minimal MVP capability from `docs/mvp-plan.md`:

- Load scenario YAML: Phase 2
- Generate mock signal frames: Phase 2, by normalizing scenario-provided signal values into internal frames
- Normalize BMS and signal inputs: Phase 2
- Calculate risk scores: Phase 3
- Generate evidence: Phase 3
- Export JSON report: Phase 4
- Export Markdown report: Phase 4
- Export RoomCI scenario: Phase 4
- Provide user-facing flow: Phase 5
- Verify all fixtures end-to-end: Phase 6

## Post-Minimal MVP Boundary

See `tasks/mvp-roadmap.md`.

Do not create detailed tasks for the final hardware MVP until the no-hardware adapter-ready MVP is complete. The next task batch is limited to fixture-based adapter contracts and adapter implementations that can run without devices.

Adapter-ready MVP completion requires:

- raw fixtures for each assumed source family
- schema-validated adapter outputs
- adapter implementations that do not score risk
- an E2E regression proving adapter outputs can compose into a normalized scenario and reach the existing risk engine
- risk engine isolation from adapter imports

## Pre-Hardware Productization Boundary

After Adapter-ready MVP, additional tasks may still run without hardware. These tasks should improve operability and demo readiness before real devices arrive:

- adapter registry and CLI inspection
- fixture-based baseline snapshots
- repeated measurement comparison
- one-command demo output
- mock API/dashboard response contracts
- pre-hardware readiness evidence

These phases must not require real sensors, serial ports, GPIO, I2C, camera, microphone, ADC, dashboard hosting, or cloud services.
