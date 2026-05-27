# SignalTwin Technology Selection

## 1. Selection Criteria

Technologies are selected based on:

- Compatibility with BMS as input
- Avoiding competition with BMS sensors
- Ability to mock before hardware exists
- Existing OSS availability
- RoomCI integration potential
- Low-cost hardware path
- Explainable output for maintenance decisions

## 2. Minimal MVP Technology

| Area | Selection | Reason |
|---|---|---|
| Language | Python | Fastest for PoC, time-series, signal processing, ML |
| Schema | Pydantic / JSON Schema | Strict I/O definitions |
| Scenario | YAML | Human-readable and RoomCI-friendly |
| CLI | Typer | Simple Python CLI |
| Data | pandas / numpy | BMS and feature processing |
| Signal | scipy | FFT, filtering, signal features |
| Anomaly | PyOD | Optional anomaly score from feature vectors |
| Testing | pytest | Fast validation |
| Output | JSON / Markdown / YAML | CI- and GitHub-friendly |

## 3. Best MVP Technology

| Area | Selection | Reason |
|---|---|---|
| Edge Gateway | Raspberry Pi 5 / mini PC | Python, camera, thermal, storage |
| WiFi CSI | ESP32 + ESP32-CSI-Tool / esp-csi | Low-cost CSI acquisition |
| WiFi Sensing Reference | RuView | Reference for spatial intelligence and CSI usage |
| PZT | PZT + ADC | Low-cost vibration and resonance sensing |
| ADC | ADS1115 first | Simple 16-bit I2C ADC for low-speed features |
| Acoustic | INMP441 + speaker | I2S microphone and sweep playback |
| Thermal | MLX90640 | 32x24 thermal matrix via I2C |
| Visual | Pi Camera / USB Camera + OpenCV | Inspection images and visual defect detection |
| API | FastAPI | Easy adapter/API development |
| Dashboard | Streamlit | Fast PoC dashboard |
| Storage | SQLite first | Simple local storage |
| Time-series optional | InfluxDB | Only if data volume increases |

The managed device and program assumptions for the Adapter-ready MVP are defined in `docs/device-io-assumptions.md`. That document is the source of truth for constraining fixture I/O before hardware exists.

## 4. Existing OSS Usage

| Purpose | OSS / Reference | Usage |
|---|---|---|
| WiFi CSI | ESP32-CSI-Tool | Real CSI capture |
| WiFi CSI | esp-csi | Official Espressif examples |
| Spatial sensing | RuView | Reference for WiFi-based spatial intelligence |
| Thermal | MLX90640 Python drivers | Thermal matrix capture |
| Visual | OpenCV / libcamera / Picamera2 | Image capture and processing |
| Audio | ESP32 I2S examples / scipy | PCM and acoustic feature extraction |
| Anomaly detection | PyOD | Feature-level anomaly detection |

## 5. What SignalTwin Must Build

Existing OSS can help capture data. SignalTwin must build the interpretation layer:

```txt
BMS time-series
+ WiFi CSI
+ PZT vibration
+ Acoustic response
+ Visual defects
+ Thermal matrix
+ Material metadata
+ Maintenance history

→ Building health risk forecast
```

This interpretation layer is the core product value.
