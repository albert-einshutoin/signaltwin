# SignalTwin I/O Schema

This document defines the expected I/O for the SignalTwin MVP.

For Adapter-ready MVP development, assumed devices, capture programs, raw fixture files, and replacement rules are managed in `docs/device-io-assumptions.md`.

## 1. BMS Input

BMS data is treated as an external input. SignalTwin does not duplicate these sensors.

```json
{
  "timestamp": "2026-05-24T10:00:00+09:00",
  "room_id": "villa-a-room-101",
  "temperature_c": 24.2,
  "humidity_percent": 76.5,
  "illuminance_lux": 180,
  "sound_level_db": 38.2,
  "motion_detected": false,
  "flow_rate_l_min": 0.0,
  "current_amp": 1.8,
  "power_state": "on",
  "device_states": {
    "hvac": "dehumidify",
    "ventilation": "on",
    "lighting": "off"
  }
}
```

## 2. WiFi CSI Input

### Device

- ESP32 DevKit
- ESP32-S3 optional

### OSS / References

- ESP32-CSI-Tool
- Espressif esp-csi
- RuView as spatial sensing reference

### Physical I/O

```txt
Input:
- WiFi packet
- Beacon / ping / UDP traffic

Internal:
- CSI amplitude
- CSI phase
- RSSI
- SNR
- channel
- timestamp

Output:
- UART / USB serial
- UDP
- MQTT
- HTTP
- CSV / JSON
```

### SignalTwin Normalized Frame

```json
{
  "source": "wifi_csi",
  "node_id": "esp32-csi-a",
  "room_id": "villa-a-room-101",
  "timestamp": "2026-05-24T10:00:00+09:00",
  "path_id": "ap-to-node-a",
  "rssi_dbm": -64,
  "snr_db": 22.4,
  "packet_loss_rate": 0.021,
  "retransmission_rate": 0.08,
  "csi_drift_score": 0.17,
  "multipath_change_score": 0.24,
  "baseline_similarity": 0.83
}
```

## 3. PZT / Piezo Input

### Device

- PZT piezo disk
- Grove Piezo Vibration Sensor
- ADS1115 ADC
- Optional op-amp and protection circuit

### Physical I/O

```txt
Passive sensing:
PZT sensor
  → protection circuit
  → amplifier
  → ADC
  → ESP32 / Raspberry Pi / STM32

Active sensing:
MCU / DAC / PWM
  → driver circuit
  → PZT transmitter

PZT receiver:
PZT
  → amplifier
  → ADC
```

### SignalTwin Normalized Frame

```json
{
  "source": "pzt",
  "sensor_id": "pzt-wall-a",
  "asset_id": "room-101-north-wall",
  "timestamp": "2026-05-24T10:00:00+09:00",
  "mode": "passive_or_tap_test",
  "peak_amplitude_delta": -0.12,
  "resonance_shift_percent": 6.8,
  "attenuation_delta": 0.21,
  "arrival_time_delta_us": 18,
  "event_count": 3,
  "baseline_similarity": 0.71
}
```

## 4. Acoustic Sweep Input

### Device

- INMP441 I2S MEMS microphone
- Small speaker
- I2S DAC/AMP optional
- Raspberry Pi or ESP32

### Physical I/O

```txt
INMP441:
- VCC
- GND
- BCLK / SCK
- LRCLK / WS
- SD
- L/R select

Output:
- PCM stream
- sample_rate: 16kHz / 44.1kHz / 48kHz
- bit_depth: 16/24/32bit

Speaker:
- PWM → amplifier → speaker
- or I2S DAC/AMP → speaker
- or USB speaker
```

### SignalTwin Normalized Frame

```json
{
  "source": "acoustic_sweep",
  "room_id": "villa-a-room-101",
  "timestamp": "2026-05-24T10:00:00+09:00",
  "sweep_type": "log_sweep_20hz_20khz",
  "sample_rate": 48000,
  "rt60_seconds": 0.48,
  "frequency_response_drift": 0.19,
  "low_freq_resonance_shift": 0.11,
  "high_freq_absorption_delta": 0.07,
  "door_seal_leak_score": 0.23,
  "baseline_similarity": 0.81
}
```

## 5. Visual Inspection Input

### Device

- Raspberry Pi Camera Module 3
- USB Camera
- IP Camera
- Smartphone inspection photo

### Physical I/O

```txt
Raspberry Pi Camera:
- MIPI CSI-2

USB Camera:
- USB UVC

IP Camera:
- RTSP / HTTP

Output:
- JPEG / PNG
- MP4 optional
- image metadata
```

### SignalTwin Normalized Frame

```json
{
  "source": "visual_inspection",
  "image_id": "inspection-wall-north-001",
  "timestamp": "2026-05-24T10:00:00+09:00",
  "camera_id": "pi-camera-01",
  "asset_id": "villa-a-north-wall",
  "image_path": "images/villa-a/north-wall/001.jpg",
  "detected_defects": [
    {
      "type": "moss",
      "severity": 0.42,
      "area_ratio": 0.08
    },
    {
      "type": "hairline_crack",
      "severity": 0.28,
      "length_m": 1.4
    }
  ],
  "metadata": {
    "angle": "front",
    "distance_m": 1.2,
    "lighting": "controlled"
  }
}
```

## 6. Thermal Matrix Input

### Device

- MLX90640
- MLX90641 optional
- FLIR optional

### Physical I/O

```txt
MLX90640:
- VCC
- GND
- SDA
- SCL

Protocol:
- I2C

Output:
- 32 x 24 temperature matrix
- each pixel = temperature value
```

### SignalTwin Normalized Frame

```json
{
  "source": "thermal_matrix",
  "thermal_id": "thermal-wall-001",
  "timestamp": "2026-05-24T10:00:00+09:00",
  "asset_id": "room-101-north-wall",
  "sensor": "MLX90640",
  "resolution": "32x24",
  "surface_temp_min_c": 19.4,
  "surface_temp_avg_c": 21.2,
  "surface_temp_max_c": 23.0,
  "cold_spot_count": 4,
  "thermal_gradient_score": 0.31,
  "dew_point_margin_min_c": 1.2
}
```
