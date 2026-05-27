from __future__ import annotations

from signaltwin.adapters._helpers import float_value, read_first_csv_row
from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput


class BmsCsvAdapter(Adapter):
    source_name = "bms-csv-fixture"

    required_columns = {
        "timestamp",
        "room_id",
        "temperature_7d_avg_c",
        "humidity_7d_avg_percent",
        "illuminance_7d_avg_lux",
        "hvac_on_hours_7d",
        "dehumidify_on_hours_7d",
    }

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        row = read_first_csv_row(adapter_input.path, self.source_name, self.required_columns)
        payload = {
            "temperature_7d_avg_c": float_value(row, "temperature_7d_avg_c", self.source_name, adapter_input.path),
            "humidity_7d_avg_percent": float_value(row, "humidity_7d_avg_percent", self.source_name, adapter_input.path),
            "illuminance_7d_avg_lux": float_value(row, "illuminance_7d_avg_lux", self.source_name, adapter_input.path),
            "hvac_on_hours_7d": float_value(row, "hvac_on_hours_7d", self.source_name, adapter_input.path),
            "dehumidify_on_hours_7d": float_value(row, "dehumidify_on_hours_7d", self.source_name, adapter_input.path),
        }
        return AdapterOutput(
            source_family="bms",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="bms",
            payload=payload,
        )
