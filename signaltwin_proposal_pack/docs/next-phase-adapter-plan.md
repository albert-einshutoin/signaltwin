# SignalTwin Next Phase Adapter Plan

## Purpose

The minimal MVP is complete as a hardware-free Scenario Engine.

The next phase is to keep the core engine stable while adding optional real-data adapters.

The immediate target is the Adapter-ready MVP. Hardware is still not required.
The first implementation path uses fixture adapters and constrained raw I/O
contracts before selecting a real hardware PoC path.

The guiding principle is:

```txt
Mock first, Adapter later.
```

## Adapter Strategy

SignalTwin should not rewrite the risk engine for every device.

Instead, each adapter should convert source-specific input into the existing normalized frames.

```txt
Real Device / OSS / CSV / API / Fixture
  ↓
Adapter
  ↓
Schema-validated SignalTwin Standard Frame
  ↓
Risk Engine
```

## Adapter-ready MVP Scope

The Adapter-ready MVP includes:

- `docs/device-io-assumptions.md` as the source of truth for assumed devices and programs
- raw fixtures for BMS, WiFi CSI, thermal, visual, acoustic, and PZT
- fixture adapters that return schema-validated outputs
- adapter-to-risk regression proving fixture adapters can reach the existing risk engine

It excludes live serial capture, GPIO/I2C setup, dashboard/API, persistence, ML, and real sensor calibration.

## Pre-hardware Readiness

Pre-hardware readiness means no-hardware work is complete and real hardware implementation is still gated by hardware handoff criteria.

The current recommended first hardware path is `BMS CSV + Thermal + Visual`.
This does not claim real sensor validation; it identifies the lowest-risk path for the first physical PoC.

## Adapter Priority

Recommended implementation order:

```txt
1. CSV / JSON BMS Adapter
2. WiFi CSI Adapter
3. Thermal Adapter
4. Visual Inspection Adapter
5. Acoustic Adapter
6. PZT Adapter
```

## Phase 7: Adapter Interface Design

### Goal

Define stable adapter contracts before connecting hardware.

### Deliverables

```txt
signaltwin/adapters/base.py
signaltwin/adapters/mock.py
signaltwin/adapters/csv_bms.py
docs/adapter-contract.md
tests/test_adapter_contracts.py
```

### Interface Concept

```python
class SignalAdapter:
    source_name: str

    def load(self, source: str) -> list[SignalFrame]:
        ...

    def normalize(self, raw: object) -> list[SignalFrame]:
        ...
```

### Exit Criteria

- mock adapters still pass existing tests
- adapters cannot bypass schema validation
- adapter output is deterministic
- adapter errors are user-readable
- core risk engine does not know adapter-specific details

## Phase 8-10: Fixture Adapter Readiness

### Purpose

Build fixture adapters before hardware adapters.

### Exit Criteria

- fixture adapters parse BMS, WiFi CSI, thermal, visual, acoustic, and PZT raw files
- fixture adapters return schema-validated outputs
- adapter output composition reaches the existing risk engine
- hardware is still not required

## Phase 9: WiFi CSI Adapter PoC

### Purpose

Connect ESP32 CSI or RuView-like output to SignalTwin.

### Candidate Sources

- ESP32-CSI-Tool CSV / serial logs
- Espressif esp-csi output
- RuView-derived or RuView-like spatial drift output

### Standard Output Frame

```json
{
  "source": "wifi_csi",
  "node_id": "esp32-csi-a",
  "room_id": "room-101",
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

### Exit Criteria

- can parse fixture CSV
- can convert to `WifiCsiFrame`
- can compare against baseline
- can output `csi_drift_score`
- existing scenario engine remains unchanged

## Phase 10: Thermal / Visual Adapter PoC

### Thermal Adapter

Candidate hardware:

- MLX90640
- MLX90641
- FLIR optional

Standard output:

```json
{
  "source": "thermal_matrix",
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

### Visual Adapter

Candidate sources:

- Pi Camera
- USB Camera
- smartphone inspection photo
- OpenCV-based detection
- manually labeled inspection result

Standard output:

```json
{
  "source": "visual_inspection",
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
  ]
}
```

### Exit Criteria

- can load image/thermal fixtures
- can normalize feature outputs
- can calculate dew point margin using BMS humidity context
- can include visual defects in evidence generation

## Phase 11: PZT / Acoustic Adapter PoC

### Acoustic Adapter

Candidate hardware:

- INMP441
- small speaker
- Raspberry Pi or ESP32
- USB microphone optional

Standard output:

```json
{
  "source": "acoustic_sweep",
  "room_id": "villa-a-room-101",
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

### PZT Adapter

Candidate hardware:

- PZT piezo disk
- Grove Piezo Vibration Sensor
- ADS1115 for low-speed measurements
- higher-speed ADC optional
- op-amp / protection circuit optional

Standard output:

```json
{
  "source": "pzt",
  "sensor_id": "pzt-wall-a",
  "asset_id": "room-101-north-wall",
  "mode": "passive_or_tap_test",
  "peak_amplitude_delta": -0.12,
  "resonance_shift_percent": 6.8,
  "attenuation_delta": 0.21,
  "arrival_time_delta_us": 18,
  "event_count": 3,
  "baseline_similarity": 0.71
}
```

### Exit Criteria

- can load waveform fixture
- can extract simple features
- can compare against baseline
- can create evidence without claiming definitive diagnosis

## Adapter Development Rules

1. Adapters normalize data; they do not score risk.
2. Risk engine consumes normalized frames only.
3. All adapter outputs must be schema validated.
4. Real adapters must have equivalent fixture-based tests.
5. Missing hardware should not break the minimal MVP.
6. Hardware-specific dependencies should be optional extras.
7. Adapter errors must not produce tracebacks in CLI.
8. All outputs must remain deterministic.

## Optional Extras Strategy

Use optional dependency groups:

```txt
signaltwin[thermal]
signaltwin[vision]
signaltwin[audio]
signaltwin[csi]
signaltwin[pzt]
signaltwin[dashboard]
```

This keeps the minimal MVP lightweight.

## Recommended Next Implementation Order

```txt
1. Adapter base interface
2. CSV/JSON fixture adapter
3. WiFi CSI fixture adapter
4. Thermal fixture adapter
5. Visual inspection fixture adapter
6. Acoustic fixture adapter
7. PZT fixture adapter
8. Real hardware connection
```
