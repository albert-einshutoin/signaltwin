# Wiring: INMP441 Acoustic Sweep Microphone

## Purpose

INMP441 captures PCM audio for acoustic sweep and room response analysis.

## Hardware

- INMP441 I2S MEMS microphone
- Raspberry Pi or ESP32
- Small speaker
- Optional I2S DAC/AMP

## I/O

```txt
INMP441 pins:
- VCC
- GND
- BCLK / SCK
- LRCLK / WS
- SD
- L/R select

Output:
- PCM stream
- sample rate: 16kHz / 44.1kHz / 48kHz
```

## Speaker Options

```txt
Option 1:
- USB speaker from Raspberry Pi

Option 2:
- I2S DAC/AMP → speaker

Option 3:
- ESP32 PWM → amplifier → speaker
```

## SignalTwin Adapter Output

```json
{
  "source": "acoustic_sweep",
  "room_id": "villa-a-room-101",
  "sweep_type": "log_sweep_20hz_20khz",
  "sample_rate": 48000,
  "rt60_seconds": 0.48,
  "frequency_response_drift": 0.19,
  "door_seal_leak_score": 0.23,
  "baseline_similarity": 0.81
}
```

## MVP Notes

BMS may capture sound level. SignalTwin captures acoustic response, not just loudness.
