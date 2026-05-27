# SignalTwin MVP Plan

## 1. Minimal MVP: SignalTwin Scenario Engine

### Purpose

Validate the product concept without hardware.

The minimal MVP uses:

- Mock BMS data
- Mock signal data
- Material metadata
- Orientation / location / age
- Maintenance history
- Rule-based risk engine

### Deliverables

```txt
README.md
architecture.md
io-schema.md
scenario-format.md
risk-model.md
scenarios/*.yml
outputs/risk_report.example.json
outputs/maintenance_report.example.md
outputs/roomci_scenario.example.yml
```

### Capabilities

- Load scenario YAML
- Generate mock signal frames
- Normalize BMS and signal inputs
- Calculate risk scores
- Generate evidence
- Export JSON report
- Export Markdown report
- Export RoomCI scenario

### Technology

- Python
- Pydantic
- YAML
- Typer
- pytest

The minimal MVP does not require pandas, numpy, scipy, PyOD, FastAPI, Streamlit, SQLite, or OpenCV. Those remain future or optional technologies for real signal processing, UI/API work, and hardware PoC stages.

### Success Criteria

- BMS and SignalTwin responsibilities are clearly separated.
- A scenario can produce a risk report.
- A scenario can export a RoomCI-compatible scenario.
- No hardware is required.

## 2. Best MVP: SignalTwin Edge Kit

### Purpose

Validate SignalTwin with a small number of real sensors.

### Hardware

- Raspberry Pi 5 or mini PC
- ESP32 DevKit x 2-3
- PZT sensor x 4-8
- ADS1115 x 1-2
- INMP441 x 1-2
- Small speaker x 1
- MLX90640 x 1
- Pi Camera or USB Camera x 1
- Power supply, wiring, cases, mounting fixtures

### Capabilities

- Capture WiFi CSI using ESP32
- Capture PZT vibration / resonance features
- Capture acoustic sweep response
- Capture thermal matrix
- Capture visual inspection images
- Combine with BMS CSV/API mock
- Build baseline
- Detect drift
- Produce building health risk forecast

### Technology

- Raspberry Pi or mini PC
- ESP32-CSI-Tool / esp-csi
- RuView as WiFi sensing reference
- Python
- FastAPI
- Streamlit
- SQLite
- OpenCV
- numpy / scipy / pandas
- PyOD

### Success Criteria

- At least one physical experiment shows measurable drift.
- SignalTwin produces a risk report from real + mock inputs.
- The dashboard shows BMS context, signal drift, and risk output.
- RoomCI scenario export works.

## 3. Development Order

```txt
Phase 1: Schema first
Phase 2: Mock scenario engine
Phase 3: Risk model and report exporters
Phase 4: WiFi CSI adapter
Phase 5: Thermal and visual adapters
Phase 6: Acoustic and PZT adapters
Phase 7: Dashboard and API
Phase 8: RoomCI scenario integration
```

## 4. Recommendation

Start with the minimal MVP. It proves the concept and keeps the hardware optional.

Then add real adapters one by one:

```txt
mock adapter
  → ESP32 CSI adapter
  → MLX90640 thermal adapter
  → camera adapter
  → acoustic adapter
  → PZT adapter
```
