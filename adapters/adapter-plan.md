# SignalTwin Adapter Plan

## 1. Adapter Strategy

SignalTwin should treat every input source as an adapter.

The first implementation should be mock-first.

```txt
mock adapter
  → real adapter
  → production adapter
```

## 2. Adapter List

| Adapter | MVP Phase | Description |
|---|---|---|
| mock_bms_adapter | minimal | Generates or loads BMS-like time-series |
| csv_bms_adapter | minimal | Loads BMS export CSV |
| mock_wifi_csi_adapter | minimal | Generates CSI drift features |
| esp32_csi_adapter | best MVP | Reads ESP32 CSI logs |
| mock_pzt_adapter | minimal | Generates PZT drift features |
| pzt_adc_adapter | best MVP | Reads PZT via ADC |
| mock_acoustic_adapter | minimal | Generates acoustic response features |
| inmp441_adapter | best MVP | Reads PCM from INMP441 |
| mock_thermal_adapter | minimal | Generates thermal features |
| mlx90640_adapter | best MVP | Reads MLX90640 thermal matrix |
| mock_visual_adapter | minimal | Generates visual defect detections |
| camera_adapter | best MVP | Captures images from Pi/USB camera |

## 3. Adapter Contract

Each adapter should return normalized frames.

```python
class Adapter:
    def read(self) -> list[Frame]:
        ...
```

## 4. Why Mock First

Mock-first development enables:

- Product validation without hardware
- Stable I/O schema before device selection
- RoomCI scenario export
- Later adapter replacement
- Clear separation from BMS
