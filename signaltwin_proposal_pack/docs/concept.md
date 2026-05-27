# SignalTwin Concept

## One-line Summary

SignalTwin is a hardware-free Building Health Forecast Scenario Engine that turns BMS context and mock non-BMS signal frames into explainable building health risk reports, maintenance recommendations, and RoomCI scenarios.

日本語では、SignalTwinは **BMS時系列データと非競合センシングのモック信号を統合し、建物ヘルスリスク・メンテナンス推奨・RoomCIシナリオを生成する、ハードウェア非依存のBuilding Health Forecast Scenario Engine** です。

## Background

SignalTwin was inspired by two ideas:

1. NOT A HOTEL's long-term LCM perspective: increasing the value of buildings over decades.
2. The possibility of using accumulated BMS time-series data as the foundation for future predictive AI.

BMS data can already represent important operational and environmental states:

- temperature
- humidity
- illuminance
- sound level
- occupancy or motion
- flow rate
- current and power state
- ON/OFF state
- equipment operation status

These are essential for understanding how a property is currently operating.

However, if the property itself is treated as a long-term asset, then equipment state alone is not enough. The building itself also changes over time.

SignalTwin focuses on the gap between **equipment/environment monitoring** and **building-material health forecasting**.

## What SignalTwin Adds

SignalTwin does not replace BMS.

It adds an interpretation layer above BMS.

```txt
BMS:
  What is happening now?

SignalTwin:
  Why might it be happening?
  What hidden building condition may be changing?
  What should be inspected next?
```

SignalTwin is designed to combine:

- BMS time-series context
- WiFi CSI drift
- PZT / vibration drift
- acoustic response drift
- thermal surface map features
- visual inspection results
- asset metadata
- material metadata
- orientation
- age
- maintenance history

and convert them into:

- moisture risk
- mold / moss risk
- crack or void risk
- communication drift risk
- comfort degradation risk
- maintenance recommendation
- RoomCI scenario output

## Core Product Positioning

SignalTwin should be positioned as:

```txt
A predictive layer that amplifies the value of existing Smart Home / BMS data.
```

It is not:

```txt
A replacement for BMS.
A hardware-first sensor product.
A black-box AI diagnosis system.
```

It is:

```txt
A schema-first, mock-first, explainable building health forecast engine.
```

## Why Mock-first Matters

Future predictive AI cannot be built only at the moment when real hardware is installed.

It requires:

- input schema design
- scenario modeling
- baseline definition
- explainable risk logic
- asset-level interpretation
- repeatable output contracts

The minimal MVP proves these foundations without hardware.

## Conceptual Architecture

```txt
YAML Scenario
  ↓
Schema Contracts
  ↓
Scenario Loading & Normalization
  ↓
Internal BMS / Signal Frames
  ↓
Rule-based Risk Engine
  ↓
Evidence Builder
  ↓
Recommendation Engine
  ↓
JSON / Markdown / RoomCI Export
```

## Design Principles

1. BMS data remains input context.
2. SignalTwin owns interpretation, risk scoring, evidence, and exports.
3. Scenario-provided signal values are treated as minimal MVP mock signal frames.
4. Normalization converts scenario YAML into internal frames before risk scoring.
5. Risk rules must not parse raw YAML dictionaries.
6. Rule-based explainability comes before optional PyOD or ML.
7. Hardware adapters are outside the minimal MVP.
