from __future__ import annotations

from signaltwin.adapters._helpers import float_value, read_first_csv_row
from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput


class WifiCsiCsvAdapter(Adapter):
    source_name = "wifi-csi-csv-fixture"

    required_columns = {
        "timestamp",
        "node_id",
        "path_id",
        "rssi_dbm",
        "snr_db",
        "packet_loss_rate",
        "retransmission_rate",
        "csi_drift_score",
        "multipath_change_score",
        "baseline_similarity",
    }

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        row = read_first_csv_row(adapter_input.path, self.source_name, self.required_columns)
        payload = {
            "rssi_dbm": float_value(row, "rssi_dbm", self.source_name, adapter_input.path),
            "snr_db": float_value(row, "snr_db", self.source_name, adapter_input.path),
            "packet_loss_rate": float_value(row, "packet_loss_rate", self.source_name, adapter_input.path),
            "retransmission_rate": float_value(row, "retransmission_rate", self.source_name, adapter_input.path),
            "csi_drift_score": float_value(row, "csi_drift_score", self.source_name, adapter_input.path),
            "multipath_change_score": float_value(row, "multipath_change_score", self.source_name, adapter_input.path),
            "baseline_similarity": float_value(row, "baseline_similarity", self.source_name, adapter_input.path),
        }
        return AdapterOutput(
            source_family="wifi_csi",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="wifi_csi",
            payload=payload,
        )
