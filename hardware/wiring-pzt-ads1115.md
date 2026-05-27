# Wiring: PZT + ADS1115

## Purpose

PZT sensors capture vibration, tap-test response, and resonance drift from walls, floors, boards, or fixtures.

## Hardware

- PZT piezo disk or PZT patch
- ADS1115 ADC
- Optional protection circuit
- Optional op-amp
- Raspberry Pi / ESP32 / STM32
- Mounting adhesive or fixture

## Passive Sensing I/O

```txt
PZT sensor
  → protection circuit
  → amplifier optional
  → ADS1115 ADC
  → I2C
  → Raspberry Pi / ESP32
```

## Active Sensing I/O

```txt
MCU / DAC / PWM
  → driver circuit
  → PZT transmitter

PZT receiver
  → amplifier
  → ADC
```

## SignalTwin Adapter Output

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

## MVP Limitations

ADS1115 is suitable for low-speed vibration/tap-test features. It is not suitable for high-speed acoustic emission or ultrasonic NDT. For high-speed use, use a faster ADC/DAQ.
