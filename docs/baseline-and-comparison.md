# SignalTwin Baseline And Comparison

SignalTwin can compare fixture outputs before hardware exists.

The baseline workflow is separate from risk scoring:

```txt
fixture outputs
  -> baseline snapshot
  -> current snapshot
  -> deterministic drift comparison
```

Risk scoring remains the job of the existing risk engine. Baseline comparison reports numeric field deltas so demos and future dashboards can show repeated measurement change without claiming real sensor validation.

## Fixture-based Comparison

Before devices arrive, adapter fixture outputs can be stored as a baseline snapshot. Later fixture outputs can be compared against the stored baseline using the same normalized keys.

This allows development of:

- baseline storage contract
- repeated measurement comparison
- drift summary JSON
- drift summary Markdown
- future dashboard data shape

## Real Baseline Collection

Real baseline collection starts only after a hardware path is selected and a real adapter produces the same schema-validated payloads as the fixture adapter. In planning notes, this is the `real baseline collection` boundary.

Until then, baselines are development artifacts for validating product flow, not field evidence.
