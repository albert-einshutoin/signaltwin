# Wiring: ESP32 CSI Node

## Purpose

ESP32 CSI nodes measure wireless propagation drift.

## Hardware

- ESP32 DevKit
- USB cable
- Optional enclosure and mounting fixture

## I/O

```txt
Input:
- WiFi packets
- Beacon / ping / UDP traffic

Output:
- USB serial logs
- UDP / MQTT / HTTP optional
```

## Suggested Software

- ESP32-CSI-Tool
- Espressif esp-csi
- RuView as reference for spatial sensing concepts

## SignalTwin Adapter Output

```json
{
  "source": "wifi_csi",
  "node_id": "esp32-csi-a",
  "path_id": "ap-to-node-a",
  "rssi_dbm": -64,
  "snr_db": 22.4,
  "csi_drift_score": 0.17,
  "baseline_similarity": 0.83
}
```

## MVP Notes

Start by collecting RSSI/SNR/CSI-derived drift features instead of raw CSI in the core model. Raw CSI can be stored separately.
