# SignalTwin Edge Kit BOM

This BOM is for the best MVP. It is intentionally low-cost and avoids BMS-duplicate sensors.

## Hardware List

| Item | Quantity | Purpose | Notes |
|---|---:|---|---|
| Raspberry Pi 5 or mini PC | 1 | Edge gateway | Collects and processes data |
| ESP32 DevKit | 2-3 | WiFi CSI nodes | CSI/RSSI/SNR collection |
| PZT piezo sensor | 4-8 | Vibration/resonance sensing | Passive first, active later |
| ADS1115 | 1-2 | ADC for PZT and analog sensors | Low-speed features only |
| INMP441 MEMS microphone | 1-2 | Acoustic sweep recording | I2S input |
| Small speaker | 1 | Acoustic sweep playback | USB or I2S/PWM amp |
| MLX90640 | 1 | Thermal surface map | 32x24 I2C thermal matrix |
| Pi Camera / USB Camera | 1 | Visual inspection | Defect image capture |
| Power supplies | as needed | Stable operation | USB-C / 5V rails |
| Breadboard / jumper wires | as needed | Prototyping | Replace with PCB later |
| Sensor cases and fixtures | as needed | Repeatable measurement | Critical for drift comparison |

## Notes

- The MVP should not duplicate BMS sensors such as temperature/humidity unless needed only for local lab experiments.
- In production, BMS data should be consumed from API/CSV/time-series export.
- PZT + ADS1115 is enough for low-speed vibration/tap-test features, but not enough for high-speed AE or ultrasonic NDT.
