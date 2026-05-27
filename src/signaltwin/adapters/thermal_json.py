from __future__ import annotations

from signaltwin.adapters._helpers import read_json_object
from signaltwin.adapters.base import Adapter, AdapterError, AdapterInput, AdapterOutput


class ThermalJsonAdapter(Adapter):
    source_name = "thermal-json-fixture"

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        raw = read_json_object(adapter_input.path, self.source_name)
        matrix = raw.get("matrix_c")
        if not _is_32x24_matrix(matrix):
            raise AdapterError(source=self.source_name, path=adapter_input.path, message="expected 32x24 matrix_c")

        payload = {
            "dew_point_margin_min_c": raw.get("dew_point_margin_min_c"),
            "cold_spot_count": raw.get("cold_spot_count"),
            "thermal_gradient_score": raw.get("thermal_gradient_score"),
            "surface_temp_min_c": raw.get("surface_temp_min_c"),
            "surface_temp_avg_c": raw.get("surface_temp_avg_c"),
            "surface_temp_max_c": raw.get("surface_temp_max_c"),
        }
        return AdapterOutput(
            source_family="thermal",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="thermal",
            payload=payload,
        )


def _is_32x24_matrix(matrix: object) -> bool:
    return (
        isinstance(matrix, list)
        and len(matrix) == 24
        and all(isinstance(row, list) and len(row) == 32 for row in matrix)
    )
