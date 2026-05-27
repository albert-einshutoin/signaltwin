# SignalTwin Architecture

## 1. Concept

SignalTwin is a Building Health Forecast Engine. It combines existing BMS time-series data with non-BMS signal inputs to estimate building and room health risks.

SignalTwin focuses on information that is usually not directly captured by BMS:

- WiFi CSI / wireless propagation drift
- PZT vibration / resonance drift
- Acoustic impulse response / room resonance drift
- Visual inspection defects such as cracks, moss, rust, efflorescence, water stains
- Thermal surface temperature maps
- Material metadata, orientation, building age, and maintenance history

## 2. Relationship with BMS

BMS already captures current equipment and environmental state:

- Temperature
- Humidity
- Illuminance
- Sound level
- Motion / occupancy detection
- Flow rate
- Current / power
- ON/OFF state

SignalTwin should not duplicate these sensors. Instead, it uses BMS data as input.

```txt
BMS Data
  temperature / humidity / illuminance / sound level / motion / flow / current / ON-OFF
        ↓
SignalTwin Input Normalization
        ↓
Signal Inputs
  WiFi CSI / PZT / Acoustic / Visual / Thermal
        ↓
Asset Metadata
  material / orientation / age / maintenance history
        ↓
Building Health Forecast Engine
        ↓
Risk Report / Maintenance Recommendation / RoomCI Scenario
```

## 3. Core Components

### 3.1 Adapters

Adapters normalize data from mock, real devices, BMS CSV/API, or existing OSS.

```txt
adapters/
  mock_bms_adapter
  csv_bms_adapter
  mock_wifi_csi_adapter
  esp32_csi_adapter
  mock_pzt_adapter
  pzt_adc_adapter
  mock_acoustic_adapter
  inmp441_adapter
  mock_thermal_adapter
  mlx90640_adapter
  mock_visual_adapter
  camera_adapter
```

### 3.2 Normalization Layer

All inputs are normalized into common frames:

- BmsFrame
- WifiCsiFrame
- PztFrame
- AcousticFrame
- ThermalFrame
- VisualInspectionFrame
- AssetMetadata
- MaintenanceHistory

### 3.3 Baseline Store

SignalTwin is based on drift detection. The baseline store keeps normal states for each room, asset, sensor, and path.

Examples:

- Dry wood wall baseline
- Normal room acoustic response
- Normal WiFi CSI propagation
- Normal thermal surface distribution
- Post-maintenance baseline

Before hardware exists, baseline snapshots can be created from fixture adapter
outputs. This validates repeated measurement comparison and demo flow without
claiming real sensor validation.

### 3.4 Forecast Engine

The engine calculates:

- Drift scores
- Anomaly scores
- Material risk adjustments
- Seasonal corrections
- Maintenance delay penalties
- Final risk scores

### 3.5 Outputs

SignalTwin outputs:

- `risk_report.json`
- `maintenance_report.md`
- `roomci_scenario.yml`
- Dashboard/API response in the Edge Kit MVP

## 4. Core Principle

SignalTwin should be positioned as:

```txt
BMS = current state acquisition and equipment control
SignalTwin = building health interpretation and future risk forecasting
```

It is not a BMS replacement. It is an upper-layer engine that increases the value of BMS data.
