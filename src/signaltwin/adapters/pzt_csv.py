from __future__ import annotations

from signaltwin.adapters._helpers import float_value, read_csv_rows
from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput


class PztCsvAdapter(Adapter):
    source_name = "pzt-csv-fixture"

    required_columns = {
        "timestamp",
        "sensor_id",
        "asset_id",
        "sample_rate_hz",
        "mode",
        "baseline_id",
        "sample_index",
        "voltage",
        "resonance_shift_percent",
        "attenuation_delta",
        "baseline_similarity",
    }

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        rows = read_csv_rows(adapter_input.path, self.source_name, self.required_columns)
        first_row = rows[0]
        voltages = [float_value(row, "voltage", self.source_name, adapter_input.path) for row in rows]
        peak_to_peak = max(voltages) - min(voltages)
        payload = {
            "peak_amplitude_delta": round(peak_to_peak, 6),
            "resonance_shift_percent": float_value(
                first_row, "resonance_shift_percent", self.source_name, adapter_input.path
            ),
            "attenuation_delta": float_value(first_row, "attenuation_delta", self.source_name, adapter_input.path),
            "event_count": sum(1 for voltage in voltages if abs(voltage) >= 0.08),
            "baseline_similarity": float_value(first_row, "baseline_similarity", self.source_name, adapter_input.path),
        }
        return AdapterOutput(
            source_family="pzt",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="pzt",
            payload=payload,
        )
