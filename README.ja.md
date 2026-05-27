# SignalTwin MVP

[English](README.md)

SignalTwin は **Building Health Forecast Engine** です。既存の BMS 時系列データに加えて、WiFi CSI、PZT 振動、音響スイープ、目視点検、熱表面マップなどの非 BMS 信号入力を使い、建物の劣化、湿気、カビ/苔リスク、通信ドリフト、保守優先度を推定します。

SignalTwin は BMS を置き換えません。BMS を入力レイヤーとして使い、その上に建物ヘルスのための高次の解釈レイヤーを追加します。

## コアポジショニング

```txt
BMS:
  現在の設備状態と環境状態を取得する。

SignalTwin:
  BMS データに加えて、信号/画像/熱/建物メタデータを使い、
  材料、空間、通信、保守リスクを推定する。
```

## MVP ステージ

1. **SignalTwin Scenario Engine**
   - ハードウェア不要。
   - モック BMS とモック信号データを使用。
   - リスクレポートと RoomCI シナリオを生成。

2. **SignalTwin Edge Kit**
   - 小型の実デバイスを使用。
   - ESP32 CSI、PZT、音響スイープ、MLX90640、カメラ入力を使用。
   - 物理実験に対して信号ドリフトを検証。

3. **Adapter-ready MVP**
   - 物理デバイス不要。
   - `fixtures/raw/*` を使い、想定デバイスやプログラムの出力を模倣。
   - BMS、WiFi CSI、熱、画像、音響、PZT fixture を差し替え可能な adapter 経由で parse。
   - リスクスコアリング前に adapter 出力を現在の SignalTwin schema で検証。
   - risk engine を hardware 名、capture program、adapter module から独立させる。

## Minimal MVP の使い方

Minimal MVP はハードウェア不要の Scenario Engine です。YAML シナリオを検証し、根拠付きのルールベース risk score を計算し、JSON、Markdown、RoomCI 互換 YAML を export します。

editable mode で package を install します。

```bash
python -m pip install -e '.[test]'
```

regression suite を実行します。

```bash
pytest
```

scenario を検証します。

```bash
python -m signaltwin.cli validate scenarios/rainy_season_wood_wall.yml
```

scenario を実行し、生成 output を書き出します。

```bash
python -m signaltwin.cli run scenarios/rainy_season_wood_wall.yml --output-dir outputs/generated
```

期待される生成ファイル:

```txt
outputs/generated/risk_report.json
outputs/generated/maintenance_report.md
outputs/generated/roomci_scenario.yml
```

Edge Kit、実センサー、dashboard、API、ML/anomaly detection は、この minimal MVP の範囲外です。

## Adapter-ready MVP の使い方

Adapter-ready MVP は、接続済み hardware を必要とせずに次の integration boundary を検証します。デバイスとプログラムの前提は `docs/device-io-assumptions.md` で管理し、raw fixture contract は `docs/raw-io-fixtures.md` に記載しています。

このステージでは物理デバイスは不要です。Adapter が同じ schema-validated normalized payload を返し続ける限り、hardware、capture program、fixture format は変更できます。

adapter-ready regression を実行します。

```bash
pytest tests/test_adapter_contracts.py tests/test_raw_fixture_contracts.py tests/test_fixture_adapters.py tests/test_adapter_ready_mvp.py -v
```

critical path:

```txt
raw fixture
  -> adapter
  -> schema-validated AdapterOutput
  -> normalized scenario
  -> existing risk engine
```

設定済み fixture adapter を確認します。

```bash
python -m signaltwin.cli adapter inspect --config configs/adapter-fixtures.yml
```

`configs/adapter-fixtures.yml` を使うと、fixture source、capture program、将来の device-specific adapter を切り替えられます。Contract は `docs/device-io-assumptions.md` で管理します。Adapter output が同じ normalized key と schema-valid payload を保つ限り、risk engine は変更しません。

## リポジトリ構成

```txt
README.md
README.ja.md
pyproject.toml
src/
  signaltwin/
tests/
docs/
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
