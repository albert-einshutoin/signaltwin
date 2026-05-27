from __future__ import annotations

from pathlib import Path

import pytest


def test_adapter_contract_requires_source_name_and_load() -> None:
    from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput

    class FakeAdapter(Adapter):
        source_name = "fake-thermal"

        def load(self, adapter_input: AdapterInput) -> AdapterOutput:
            return AdapterOutput(
                source_family="thermal",
                source_name=self.source_name,
                path=adapter_input.path,
                normalized_key="thermal",
                payload={"thermal_gradient_score": 0.31},
            )

    output = FakeAdapter().load(AdapterInput(path=Path("fixtures/raw/thermal_matrix.json")))

    assert output.source_name == "fake-thermal"
    assert output.normalized_key == "thermal"
    assert output.payload == {"thermal_gradient_score": 0.31}


def test_adapter_error_includes_source_and_path() -> None:
    from signaltwin.adapters.base import AdapterError

    error = AdapterError(
        source="wifi-csi",
        path=Path("fixtures/raw/wifi_csi.csv"),
        message="missing required column: csi_drift_score",
    )

    assert "wifi-csi" in str(error)
    assert "fixtures/raw/wifi_csi.csv" in str(error)
    assert "missing required column: csi_drift_score" in str(error)


def test_adapter_output_validates_signal_payload() -> None:
    from signaltwin.adapters.base import AdapterOutput

    output = AdapterOutput(
        source_family="wifi_csi",
        source_name="esp-csi-fixture",
        path=Path("fixtures/raw/wifi_csi.csv"),
        normalized_key="wifi_csi",
        payload={"csi_drift_score": 0.25, "packet_loss_rate": 0.04},
    )

    assert output.payload == {"csi_drift_score": 0.25, "packet_loss_rate": 0.04}


def test_adapter_output_validates_bms_payload() -> None:
    from signaltwin.adapters.base import AdapterOutput

    output = AdapterOutput(
        source_family="bms",
        source_name="bms-csv-fixture",
        path=Path("fixtures/raw/bms_context.csv"),
        normalized_key="bms",
        payload={"humidity_7d_avg_percent": 82, "temperature_7d_avg_c": 24.2},
    )

    assert output.payload["humidity_7d_avg_percent"] == 82


def test_adapter_output_rejects_unknown_normalized_key() -> None:
    from signaltwin.adapters.base import AdapterError, AdapterOutput

    with pytest.raises(AdapterError, match="unknown normalized key"):
        AdapterOutput(
            source_family="unknown",
            source_name="unknown-fixture",
            path=Path("fixtures/raw/unknown.csv"),
            normalized_key="unknown",
            payload={},
        )


def test_adapter_output_rejects_invalid_signal_payload() -> None:
    from signaltwin.adapters.base import AdapterError, AdapterOutput

    with pytest.raises(AdapterError, match="wifi_csi"):
        AdapterOutput(
            source_family="wifi_csi",
            source_name="esp-csi-fixture",
            path=Path("fixtures/raw/wifi_csi.csv"),
            normalized_key="wifi_csi",
            payload={"csi_drift_score": 1.25},
        )


def test_adapter_contract_doc_mentions_all_source_families() -> None:
    doc = Path("docs/adapter-contract.md")

    text = doc.read_text()

    for source_family in ("BMS", "WiFi CSI", "thermal", "visual", "acoustic", "PZT"):
        assert source_family in text
