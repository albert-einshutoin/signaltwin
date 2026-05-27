# SignalTwin Proposal for NOT A HOTEL

## Proposal Summary

SignalTwin is a Building Health Forecast Scenario Engine designed to extend the value of NOT A HOTEL's existing Smart Home / BMS infrastructure.

It does not replace BMS.

Instead, it uses BMS time-series data as context and adds non-competing signal layers such as WiFi CSI, PZT vibration, acoustic response, thermal surface maps, visual inspection outputs, material metadata, and maintenance history.

The goal is to estimate hidden building condition changes and generate explainable maintenance recommendations.

## Why This Matters for NOT A HOTEL

NOT A HOTEL is not only operating buildings.

It is packaging the property itself as a long-term asset and experience.

If the goal is to increase value over decades, then it becomes important to continuously understand not only equipment state, but also the state of the building itself.

BMS data is already valuable for understanding:

- temperature
- humidity
- illuminance
- sound level
- occupancy
- flow rate
- current
- power state
- equipment ON/OFF
- operation status

However, BMS does not directly observe:

- moisture inside or near building materials
- wood moisture tendency
- surface condensation risk
- crack or void hints
- moss / mold risk
- acoustic response drift
- WiFi propagation drift
- wall / floor / panel resonance drift
- material-specific aging patterns

SignalTwin focuses on this gap.

## Proposed Positioning

```txt
BMS = the nervous system that understands current operation.
SignalTwin = the predictive layer that interprets hidden building health signals.
```

## Relationship with BMS

| Area | Existing BMS | SignalTwin |
|---|---|---|
| Temperature / humidity | Source of context | Uses as input |
| Equipment ON/OFF | Source of context | Uses as input |
| Power / current / flow | Source of context | Uses as input |
| Equipment operation state | Strong | Uses as input |
| Material moisture risk | Limited | Interprets |
| Crack / void / degradation hint | Limited | Interprets |
| Acoustic / vibration drift | Limited | Interprets |
| Thermal surface irregularity | Limited | Interprets |
| Maintenance priority | Partial | Generates recommendation |
| RoomCI scenario output | Not primary role | Exports scenarios |

## Core Hypothesis

The building may show changes in signals before those changes are clearly visible.

For example:

- a wooden panel may retain more moisture during rainy season
- a north-facing wall may dry more slowly
- a wall or floor may change its resonance response
- WiFi CSI may drift because of space, material, or layout changes
- thermal cold spots may indicate condensation-prone areas
- visual inspection may detect moss, hairline cracks, rust, or staining

SignalTwin stores these changes as time-series signal frames and interprets them against building context.

## Minimal MVP Status

The current minimal MVP is complete as a hardware-free Scenario Engine.

It can:

- validate YAML scenarios
- load and normalize scenario fixtures
- transform raw scenario data into internal BMS and signal frames
- calculate rule-based building health risk scores
- generate explainable evidence
- produce maintenance recommendations
- export deterministic JSON reports
- export Markdown maintenance reports
- export RoomCI scenario YAML
- expose validate and run commands through CLI

## Why This MVP Is Valuable Before Hardware

The first value is not the hardware.

The first value is the I/O design and the building health forecast hypothesis.

By completing the mock-first Scenario Engine, SignalTwin can already demonstrate:

- how BMS context is used without replacing BMS
- what non-competing signal inputs may look like
- how hidden building risks are scored
- how recommendations are explained
- how abnormal building-health scenarios can be exported to RoomCI
- how future real adapters can be connected later

## Example Use Case: Rainy Season Wood Wall Risk

Input:

- BMS humidity remains high for several days
- asset is a north-facing wooden wall
- maintenance interval is long
- mock thermal data shows low dew point margin
- mock PZT data shows resonance shift and attenuation increase
- mock visual inspection detects early moss or staining

Output:

- moisture risk: high
- mold risk: high
- moss risk: medium-high
- inspection priority: high
- recommendation: inspect within 30 days and review dehumidification behavior

## Proposed PoC Scope

Start small.

```txt
Target:
  1 property
  1-2 rooms
  1-2 walls or panels
  limited use cases
```

Recommended first use cases:

1. Moisture / condensation risk
2. Communication / spatial drift
3. Inspection priority recommendation

## Proposed PoC Flow

```txt
Week 1:
  Schema and mock scenario design

Week 2-3:
  Adapter interface planning and optional WiFi CSI adapter

Week 4:
  Baseline collection for selected assets

Week 5-6:
  Abnormal scenario evaluation and report review
```

## Expected Outcomes

- BMS value is amplified, not replaced.
- Hidden building-health hypotheses become visible.
- The team gains asset-level baseline definitions.
- Maintenance priority can be discussed with evidence.
- RoomCI scenarios can simulate building-health conditions.
- Future LCM and predictive maintenance AI can start from structured data.

## Final Message

SignalTwin is a proposal to start accumulating building-health signal structure early.

It respects NOT A HOTEL's existing Smart Home and BMS assets while adding a predictive layer for the invisible condition changes of the building itself.
