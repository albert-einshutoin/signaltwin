# SignalTwin Raw I/O Fixtures

This document defines fixture files used to develop adapters without physical devices.

The device and program assumptions are managed in `docs/device-io-assumptions.md`. These fixtures are development contracts, not final hardware requirements.

## Fixture Inventory

| Fixture | Source Family | Normalized Key | Purpose |
|---|---|---|---|
| `fixtures/raw/bms_context.csv` | BMS context | `bms` | BMS or BAS summary export. |
| `fixtures/raw/wifi_csi.csv` | WiFi CSI | `wifi_csi` | ESP32 CSI-like summary output. |
| `fixtures/raw/thermal_matrix.json` | Thermal | `thermal` | MLX90640-like 32x24 matrix plus derived features. |
| `fixtures/raw/visual_defects.json` | Visual | `visual` | Camera/manual label defect output. |
| `fixtures/raw/acoustic_features.json` | Acoustic | `acoustic` | Feature-level acoustic sweep output. |
| `fixtures/raw/pzt_adc.csv` | PZT | `pzt` | ADC sample rows plus metadata for simple feature mapping. |

## Mapping Rule

```txt
raw fixture
  -> adapter parser
  -> schema-validated AdapterOutput
  -> normalized SignalTwin scenario
```

Adapters may read richer raw values than the risk engine currently uses. The adapter output must still validate against the current normalized schema.
