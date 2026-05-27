# SignalTwin Adapter Contract

Adapters convert device, program, fixture, or API output into schema-validated SignalTwin payloads.

Adapters do not score risk. The risk engine receives normalized payloads and must not know which hardware, capture program, or fixture produced them.

## Source Families

| Family | Normalized Key | Purpose |
|---|---|---|
| BMS | `bms` | Existing BMS context such as humidity, temperature, illuminance, HVAC runtime, and dehumidifier runtime. |
| WiFi CSI | `wifi_csi` | Wireless propagation, RSSI/SNR, packet loss, CSI drift, multipath change, and baseline similarity. |
| thermal | `thermal` | Surface temperature summary, cold spots, thermal gradient, and dew point margin. |
| visual | `visual` | Detected defects such as moss, mold, cracks, stains, rust, or efflorescence. |
| acoustic | `acoustic` | Frequency response drift, RT60, unusual noise, resonance, leak, and baseline similarity. |
| PZT | `pzt` | Vibration, resonance, attenuation, event count, and baseline similarity. |

## Output Shape

Each adapter returns an `AdapterOutput` with:

- `source_family`
- `source_name`
- `path`
- `normalized_key`
- `payload`

The payload must validate against the existing schema model for its `normalized_key`.

## Replacement Rule

Hardware and capture programs can change. The normalized key and schema-valid payload should remain stable.

```txt
device or program output
  -> adapter
  -> schema-validated AdapterOutput
  -> normalized scenario
  -> risk engine
```

If a new device cannot produce the existing normalized payload, update `docs/device-io-assumptions.md` and add tests before changing implementation.

## Adapter Registry And Config

Fixture adapters are selected through `configs/adapter-fixtures.yml`.

Changing a device or capture program should normally mean changing the adapter config and adding a compatible adapter, while the risk engine remains unchanged.

Inspect the configured fixture adapters:

```bash
python -m signaltwin.cli adapter inspect --config configs/adapter-fixtures.yml
```

The command validates adapter outputs and prints source names, normalized keys, and payload fields. It does not calculate risk.
