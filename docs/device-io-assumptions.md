# SignalTwin Device I/O Assumptions

This document manages the assumed devices, capture programs, raw fixture formats, and normalized targets for the Adapter-ready MVP.

The purpose is to constrain I/O before hardware exists. These assumptions are not purchase requirements. A device can be replaced if its adapter can produce the same normalized SignalTwin payload.

## Adapter-ready Rule

```txt
assumed device or program output
  -> raw fixture contract
  -> adapter parser
  -> schema-validated AdapterOutput
  -> normalized SignalTwin scenario
  -> existing risk engine
```

The risk engine must not depend on hardware names, driver libraries, serial ports, GPIO pins, or capture programs.

## Managed Source Families

| Family | Default Device Assumption | Default Program Assumption | Raw Fixture | Normalized Key | Replacement Rule |
|---|---|---|---|---|---|
| BMS context | Existing BMS export | CSV or JSON export from BMS / BAS / time-series DB | `fixtures/raw/bms_context.csv` | `bms` | Any BMS API or export is acceptable if mapped into the same BMS context fields. |
| WiFi CSI | ESP32 DevKit / ESP32-S3 pair | Espressif `esp-csi` or ESP32-CSI-Tool CSV-like output | `fixtures/raw/wifi_csi.csv` | `wifi_csi` | RuView-like or other CSI tooling is acceptable if mapped into CSI drift, RSSI/SNR, packet loss, and baseline fields. |
| Thermal | MLX90640 32x24 thermal matrix | Python I2C capture script or MLX90640 library output | `fixtures/raw/thermal_matrix.json` | `thermal` | MLX90641, FLIR, or other thermal sources are acceptable if mapped into surface temperatures, cold spots, thermal gradient, and dew point margin. |
| Visual | Raspberry Pi Camera Module 3 or USB camera | Camera capture plus OpenCV/manual label JSON | `fixtures/raw/visual_defects.json` | `visual` | Smartphone photos, IP cameras, or manual inspection labels are acceptable if mapped into detected defects. |
| Acoustic | INMP441 I2S microphone or USB microphone plus speaker | Python/scipy feature extractor over WAV/PCM | `fixtures/raw/acoustic_features.json` | `acoustic` | Any mic/speaker path is acceptable if mapped into acoustic drift, RT60/noise, and baseline fields. |
| PZT | PZT disk or Grove Piezo Vibration Sensor plus ADS1115-like ADC | ADC CSV capture script and simple feature extractor | `fixtures/raw/pzt_adc.csv` | `pzt` | Other ADC/DAQ hardware is acceptable if mapped into attenuation, resonance, event, and baseline fields. |

## BMS Context

### Assumed Device / System

- Building Management System
- BAS export
- time-series DB export
- manually prepared CSV for early PoC

### Assumed Program Output

- CSV first
- JSON API later
- one row can represent a measurement window or summary window

### Required Raw Fields

- `timestamp`
- `room_id`
- `temperature_7d_avg_c`
- `humidity_7d_avg_percent`
- `illuminance_7d_avg_lux`
- `hvac_on_hours_7d`
- `dehumidify_on_hours_7d`

### Adapter Output

- `normalized_key`: `bms`
- payload validates as `BmsContext`
- adapter may preserve extra BMS fields because BMS context is intentionally flexible

## WiFi CSI

### Assumed Device / Program

- ESP32 DevKit or ESP32-S3
- Espressif `esp-csi`
- ESP32-CSI-Tool

### Required Raw Fields

- `timestamp`
- `node_id`
- `path_id`
- `rssi_dbm`
- `snr_db`
- `packet_loss_rate`
- `retransmission_rate`
- `csi_drift_score`
- `multipath_change_score`
- `baseline_similarity`

### Adapter Output

- `normalized_key`: `wifi_csi`
- payload validates against `WifiCsiSignal`
- scores must stay in the `0..1` range

## Thermal Matrix

### Assumed Device / Program

- MLX90640
- Python I2C capture script
- JSON file containing matrix metadata and derived features

### Required Raw Fields

- `timestamp`
- `thermal_id`
- `asset_id`
- `sensor`
- `resolution`
- `matrix_c`
- `surface_temp_min_c`
- `surface_temp_avg_c`
- `surface_temp_max_c`
- `cold_spot_count`
- `thermal_gradient_score`
- `dew_point_margin_min_c`

### Adapter Output

- `normalized_key`: `thermal`
- payload validates against `ThermalSignal`
- matrix data is raw evidence; normalized payload keeps derived feature fields used by the risk engine

## Visual Inspection

### Assumed Device / Program

- Raspberry Pi Camera Module 3
- USB camera
- smartphone photo
- OpenCV pipeline or manual label JSON

### Required Raw Fields

- `timestamp`
- `image_id`
- `asset_id`
- `image_path`
- `detected_defects`

Each detected defect must include:

- `type`
- `severity`

Optional defect fields:

- `area_ratio`
- `length_m`

### Adapter Output

- `normalized_key`: `visual`
- payload validates against `VisualSignal`
- image files are not required for Adapter-ready MVP tests; the fixture may reference a path as metadata

## Acoustic

### Assumed Device / Program

- INMP441 I2S microphone or USB microphone
- small speaker or USB speaker
- Python/scipy feature extractor from WAV/PCM

### Required Raw Fields

- `timestamp`
- `room_id`
- `sample_rate_hz`
- `feature_window_seconds`
- `frequency_response_drift`
- `rt60_seconds`
- `low_freq_resonance_shift`
- `high_freq_absorption_delta`
- `door_seal_leak_score`
- `unusual_noise_score`
- `baseline_similarity`

### Adapter Output

- `normalized_key`: `acoustic`
- payload validates against `AcousticSignal`
- Adapter-ready MVP does not implement full audio DSP; it consumes feature-level fixture output

## PZT / Piezo

### Assumed Device / Program

- PZT disk or Grove Piezo Vibration Sensor
- ADS1115-like ADC first
- CSV capture script
- simple feature extraction from ADC samples

### Required Raw Fields

- `timestamp`
- `sensor_id`
- `asset_id`
- `sample_index`
- `voltage`

Fixture metadata must provide:

- `sample_rate_hz`
- `mode`
- `baseline_id`
- `resonance_shift_percent`
- `attenuation_delta`
- `baseline_similarity`

Adapter output must include at least:

- `peak_amplitude_delta`
- `resonance_shift_percent`
- `attenuation_delta`
- `event_count`
- `baseline_similarity`

### Adapter Output

- `normalized_key`: `pzt`
- payload validates against `PztSignal`
- ADS1115 is a low-speed assumption for early fixture contracts, not a final structural sensing requirement

## Change Control

When changing an assumed device or program:

1. Update this document first.
2. Update `docs/raw-io-fixtures.md` if the raw fixture format changes.
3. Update or add fixture contract tests.
4. Keep the normalized key and schema stable unless the risk model intentionally changes.
5. Do not modify the risk engine to handle a device-specific format.

## Out Of Scope For Adapter-ready MVP

- live serial capture
- GPIO/I2C setup scripts
- camera calibration
- audio DSP from raw WAV
- high-speed DAQ support
- dashboard/API
- baseline database
