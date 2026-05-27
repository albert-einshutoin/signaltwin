# SignalTwin Risk Model

## 1. Model Philosophy

SignalTwin should start with a rule-based and explainable risk engine.

The purpose of the first MVP is not to produce a perfect diagnosis. It is to produce a defensible and traceable building health risk forecast from BMS data and signal drift evidence.

## 2. Core Formula

```txt
risk = f(
  bms_environment_stress,
  signal_drift,
  material_vulnerability,
  orientation_and_location,
  maintenance_delay,
  seasonal_context
)
```

## 3. Risk Categories

SignalTwin should output these risk categories:

- `moisture_risk`
- `mold_risk`
- `wood_deformation_risk`
- `crack_or_void_risk`
- `communication_drift_risk`
- `comfort_degradation_risk`
- `maintenance_priority`

## 4. Example Rule Groups

### 4.1 Moisture Risk

Inputs:

- BMS humidity
- Thermal dew point margin
- Cold spot count
- Material moisture vulnerability
- PZT attenuation delta
- Maintenance delay

Example:

```txt
moisture_risk =
  humidity_score
+ dew_point_margin_score
+ cold_spot_score
+ material_moisture_score
+ pzt_attenuation_score
+ maintenance_delay_score
```

### 4.2 Mold / Moss Risk

Inputs:

- High humidity duration
- Low illuminance / north-facing orientation
- Surface temperature near dew point
- Visual moss detection
- Cleaning delay

### 4.3 Crack or Void Risk

Inputs:

- PZT resonance shift
- PZT attenuation delta
- Acoustic frequency response drift
- Visual crack detection
- Age and maintenance delay

### 4.4 Communication Drift Risk

Inputs:

- WiFi CSI drift score
- SNR delta
- Packet loss rate
- Multipath change score
- Occupancy context from BMS motion data

## 5. Evidence-Based Output

Every risk score should include evidence.

Example:

```json
{
  "risk_scores": {
    "moisture_risk": 0.78,
    "mold_risk": 0.66
  },
  "evidence": [
    "7-day average humidity is 82%",
    "The wall is north-facing cedar panel",
    "Thermal dew point margin is only 1.2°C",
    "PZT attenuation increased by 21% from baseline",
    "Last inspection was 180 days ago"
  ]
}
```

## 6. MVP Approach

### Minimal MVP

- Rule-based score only
- No ML required
- Optional PyOD anomaly score for feature vectors

### Advanced MVP

- Rule-based score + PyOD anomaly score
- Baseline drift detection
- Asset-level calibration
- Maintenance recommendation

## 7. Output Priority

The first product should not claim exact diagnosis. It should claim:

```txt
Building health risk estimation based on signal drift and BMS time-series evidence.
```

This keeps the positioning realistic and defensible.
