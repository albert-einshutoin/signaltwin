# Experiment: WiFi CSI Obstruction Drift

## Purpose

Validate whether WiFi CSI detects spatial and obstruction changes relevant to SignalTwin.

## Setup

- ESP32 Node A
- ESP32 Node B or AP
- Fixed positions
- Repeated measurements

## Changes to Test

- Human presence
- Wood panel between nodes
- Wet cloth between nodes
- Metal object between nodes
- Furniture movement

## Inputs

- CSI drift score
- RSSI
- SNR
- Packet loss
- Baseline similarity

## Output

- wireless_propagation_change_score
- communication_drift_risk
- occupancy_context correction
