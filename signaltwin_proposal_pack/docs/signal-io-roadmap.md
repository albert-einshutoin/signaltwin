# SignalTwin Signal I/O Roadmap

## Purpose

This document defines how SignalTwin should evolve from mock signal frames to real hardware adapters.

The goal is to keep the core risk engine hardware-independent.

## I/O Philosophy

SignalTwin should treat every signal as a normalized frame.

```txt
Mock Scenario
Real Sensor
OSS Output
CSV Log
Manual Inspection
BMS API
```

all become:

```txt
Validated SignalTwin Frame
```

before risk scoring.

## Current Minimal MVP Inputs

The minimal MVP currently supports scenario-provided mock signal values.

These values represent future sensor outputs but do not require hardware.

## BMS Context Frame

BMS data remains input context.

Example fields:

```json
{
  "temperature_7d_avg_c": 24.2,
  "humidity_7d_avg_percent": 82,
  "illuminance_7d_avg_lux": 110,
  "sound_level_7d_avg_db": 38,
  "motion_hours_7d": 18,
  "flow_events_7d": 32,
  "hvac_on_hours_7d": 88,
  "dehumidify_on_hours_7d": 36
}
```

SignalTwin does not own BMS control.

SignalTwin owns interpretation.

## Signal Sources

## 1. WiFi CSI

### Role

Detect wireless propagation and spatial drift.

### Possible Sources

- RuView-like output
- ESP32-CSI-Tool
- Espressif esp-csi
- CSV fixture
- mock scenario values

### Features

- RSSI
- SNR
- packet loss rate
- retransmission rate
- CSI drift score
- multipath change score
- baseline similarity

### Risk Mapping

| Feature | Possible Interpretation |
|---|---|
| CSI drift rises | spatial or propagation environment changed |
| SNR drops | wireless quality or obstruction changed |
| packet loss rises | communication stability risk |
| baseline similarity drops | room/space behavior differs from normal |

## 2. PZT / Vibration

### Role

Detect vibration, resonance, attenuation, and material response drift.

### Possible Sources

- PZT disk
- Grove Piezo Vibration Sensor
- ADS1115 low-speed ADC
- waveform fixture
- mock scenario values

### Features

- peak amplitude delta
- resonance shift percent
- attenuation delta
- arrival time delta
- event count
- baseline similarity

### Risk Mapping

| Feature | Possible Interpretation |
|---|---|
| resonance shift rises | material stiffness or mounting condition may have changed |
| attenuation rises | damping, moisture, void, or contact change may be present |
| event count rises | vibration or impact event increased |
| baseline similarity drops | response differs from normal |

## 3. Acoustic Sweep

### Role

Detect room acoustic response and reflection drift.

### Possible Sources

- INMP441
- USB microphone
- small speaker
- recorded PCM fixture
- mock scenario values

### Features

- RT60
- frequency response drift
- low-frequency resonance shift
- high-frequency absorption delta
- door seal leak score
- baseline similarity

### Risk Mapping

| Feature | Possible Interpretation |
|---|---|
| RT60 changes | room reflection or absorption changed |
| frequency response drifts | furniture, surface, opening, or material state changed |
| low-frequency resonance shifts | room or panel response changed |
| door seal leak score rises | gap or sealing behavior changed |

## 4. Thermal Surface Map

### Role

Detect surface temperature distribution, cold spots, condensation-prone areas, and thermal irregularity.

### Possible Sources

- MLX90640
- MLX90641
- FLIR
- thermal matrix fixture
- mock scenario values

### Features

- surface temp min
- surface temp avg
- surface temp max
- cold spot count
- thermal gradient score
- dew point margin min

### Risk Mapping

| Feature | Possible Interpretation |
|---|---|
| dew point margin low | condensation risk |
| cold spot count rises | localized cold surfaces or thermal bridge hints |
| thermal gradient rises | uneven insulation or surface condition |
| low surface temperature + high humidity | mold / moisture risk increases |

## 5. Visual Inspection

### Role

Detect visible defects and surface degradation.

### Possible Sources

- Pi Camera
- USB Camera
- smartphone photo
- OpenCV pipeline
- manual label fixture
- mock scenario values

### Features

- detected defects
- defect severity
- area ratio
- crack length
- staining score
- moss / mold / rust / efflorescence indicators

### Risk Mapping

| Feature | Possible Interpretation |
|---|---|
| moss severity rises | moisture and surface growth risk |
| crack length rises | crack progression risk |
| rust detected | metal corrosion risk |
| water stain detected | leak or condensation hint |
| efflorescence detected | moisture migration hint |

## Baseline Strategy

Every signal source should be compared to a baseline.

A baseline should be asset-specific.

```txt
asset_id
source
season
normal_range
last_updated_at
features
```

SignalTwin should avoid claiming absolute diagnosis early.

Instead, it should use:

```txt
baseline drift
contextual risk
evidence-backed recommendation
```

## Recommended Baseline Types

| Baseline | Purpose |
|---|---|
| dry season baseline | low moisture condition |
| rainy season baseline | seasonal humidity reference |
| post-maintenance baseline | reset point after repair |
| room-specific baseline | captures room individuality |
| material-specific baseline | captures material response tendency |

## Roadmap

## Stage 1: Mock Frames

Status: complete.

```txt
YAML scenario values are treated as mock signal frames.
```

## Stage 2: Fixture Adapters

Next.

```txt
CSV / JSON / WAV / image / thermal matrix fixtures
```

Purpose:

- test adapters without hardware
- preserve deterministic tests
- support CI

## Stage 3: Real Low-cost Adapters

```txt
ESP32 CSI
MLX90640
Pi Camera
INMP441
PZT + ADC
```

Purpose:

- collect real signals
- compare against fixture behavior
- validate physical feasibility

## Stage 4: Building-level Pilot

```txt
1 property
1-2 rooms
1-2 walls or panels
limited use cases
```

Use cases:

- rainy season moisture risk
- communication drift
- inspection priority recommendation

## Stage 5: Predictive Model Layer

Only after enough data exists.

Candidates:

- PyOD anomaly scoring
- time-series drift detection
- survival analysis
- Bayesian update
- material-specific risk model
- maintenance effect model

## Development Rule

Do not put ML before explainable rule-based risk.

The minimal MVP has correctly prioritized:

```txt
schema
normalization
risk rules
evidence
exports
```

before ML.

## Final Roadmap Summary

```txt
Mock Signal Frames
  ↓
Fixture Adapters
  ↓
Low-cost Real Adapters
  ↓
Asset-specific Baselines
  ↓
Building Health Forecast
  ↓
Maintenance Recommendation
  ↓
RoomCI Scenario Feedback Loop
```
