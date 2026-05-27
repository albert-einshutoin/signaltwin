# Wiring: MLX90640 Thermal Camera

## Purpose

MLX90640 captures a 32x24 thermal matrix for surface temperature maps.

## Hardware

- MLX90640 module
- Raspberry Pi or ESP32
- Jumper wires

## I/O

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
```

## SignalTwin Adapter Output

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

## MVP Notes

The value is not room temperature. The value is surface temperature distribution, cold spots, thermal gradients, and dew point margin.
