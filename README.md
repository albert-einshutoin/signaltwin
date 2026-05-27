# SignalTwin MVP

[日本語版](README.ja.md)

SignalTwin is a **Building Health Forecast Engine** that uses existing BMS time-series data plus non-BMS signal inputs such as WiFi CSI, PZT vibration, acoustic sweep, visual inspection, and thermal surface maps to estimate building deterioration, moisture, mold/moss risk, communication drift, and maintenance priority.

SignalTwin does **not** replace BMS. It uses BMS as an input layer and adds a higher-level interpretation layer for building health.

## Project Status

SignalTwin is a pre-1.0 MVP. The verified path is local, hardware-free, and fixture-based:

- YAML scenario validation
- typed normalization
- rule-based risk scoring
- JSON, Markdown, and RoomCI-compatible exports
- fixture adapter contracts for assumed BMS and signal sources
- static API/dashboard example contracts

It is not a production BMS, field safety system, or deployed monitoring service.

## Core Positioning

```txt
BMS:
  Captures current equipment and environmental state.

SignalTwin:
  Uses BMS data plus signal/visual/thermal/building metadata
  to infer material, space, communication, and maintenance risks.
```

## MVP Stages

1. **SignalTwin Scenario Engine**
   - No hardware required.
   - Uses mock BMS and mock signal data.
   - Produces risk reports and RoomCI scenarios.

2. **SignalTwin Edge Kit**
   - Uses small real devices.
   - ESP32 CSI, PZT, acoustic sweep, MLX90640, and camera inputs.
   - Validates signal drift against physical experiments.

3. **Adapter-ready MVP**
   - No physical devices are required.
   - Uses `fixtures/raw/*` to imitate assumed device and program output.
   - Parses BMS, WiFi CSI, thermal, visual, acoustic, and PZT fixtures through swappable adapters.
   - Validates adapter outputs against the current SignalTwin schema before risk scoring.
   - Keeps the risk engine independent from hardware names, capture programs, and adapter modules.

## Minimal MVP Usage

The minimal MVP is the hardware-free Scenario Engine. It validates YAML
scenarios, calculates rule-based risk scores with evidence, and exports JSON,
Markdown, and RoomCI-compatible YAML.

Install the package in editable mode:

```bash
python -m pip install -e '.[test]'
```

Run the regression suite:

```bash
pytest
```

Validate a scenario:

```bash
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
```

Run a scenario and write generated outputs:

```bash
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

Expected generated files:

```txt
outputs/generated/risk_report.json
outputs/generated/maintenance_report.md
outputs/generated/roomci_scenario.yml
```

The Edge Kit, real sensors, dashboard, API, and ML/anomaly detection are outside
this minimal MVP.

## Adapter-ready MVP Usage

The Adapter-ready MVP proves the next integration boundary without requiring
connected hardware. Device and program assumptions are managed in
`docs/device-io-assumptions.md`, and raw fixture contracts are documented in
`docs/raw-io-fixtures.md`.

No physical devices are required for this stage. Hardware, capture programs, and
fixture formats can change as long as adapters keep returning the same
schema-validated normalized payloads.

Run the adapter-ready regression:

```bash
pytest tests/test_adapter_contracts.py tests/test_raw_fixture_contracts.py tests/test_fixture_adapters.py tests/test_adapter_ready_mvp.py -v
```

The critical path is:

```txt
raw fixture
  -> adapter
  -> schema-validated AdapterOutput
  -> normalized scenario
  -> existing risk engine
```

Inspect configured fixture adapters:

```bash
python -m signaltwin.cli adapter inspect --config configs/adapter-fixtures.yml
```

Use `configs/adapter-fixtures.yml` to switch fixture sources, capture programs,
or future device-specific adapters. The contract is managed in
`docs/device-io-assumptions.md`; the risk engine remains unchanged when adapter
outputs keep the same normalized keys and schema-valid payloads.

## Documentation

- [Documentation index](docs/README.md)
- [Architecture](docs/architecture.md)
- [Scenario format](docs/scenario-format.md)
- [Adapter contract](docs/adapter-contract.md)
- [Device I/O assumptions](docs/device-io-assumptions.md)
- [Pre-hardware readiness](docs/pre-hardware-readiness.md)
- [API/dashboard contract](docs/api-dashboard-contract.md)

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and keep the fixture-based validation path working when changing adapters, scenarios, or risk logic.

Before opening a pull request, run:

```bash
pytest
```

## Security

Please read [SECURITY.md](SECURITY.md) before reporting vulnerabilities. The current project is a local MVP and does not include production API deployment, authentication, tenant isolation, or real-device safety guarantees.

## License

SignalTwin is released under the [MIT License](LICENSE).

## Repository Layout

```txt
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
CHANGELOG.md
README.md
README.ja.md
pyproject.toml
src/
  signaltwin/
tests/
docs/
  README.md
  architecture.md
  io-schema.md
  scenario-format.md
  risk-model.md
  mvp-plan.md
  technology-selection.md
scenarios/
  rainy_season_wood_wall.yml
  coastal_villa_moss_risk.yml
  communication_drift.yml
  hvac_efficiency_drift.yml
outputs/
  risk_report.example.json
  maintenance_report.example.md
  roomci_scenario.example.yml
  generated/
hardware/
  edge-kit-bom.md
  wiring-esp32-csi.md
  wiring-mlx90640.md
  wiring-inmp441.md
  wiring-pzt-ads1115.md
adapters/
  adapter-plan.md
experiments/
  wood_moisture_drift.md
  acoustic_room_drift.md
  csi_obstruction_drift.md
  thermal_condensation_risk.md
tasks/
  status.md
  phase*/
signaltwin_proposal_pack/
  README.md
  docs/
  examples/
```
