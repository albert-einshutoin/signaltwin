from __future__ import annotations

from signaltwin.adapters._helpers import read_json_object
from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput


class VisualJsonAdapter(Adapter):
    source_name = "visual-json-fixture"

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        raw = read_json_object(adapter_input.path, self.source_name)
        return AdapterOutput(
            source_family="visual",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="visual",
            payload={"detected_defects": raw.get("detected_defects", [])},
        )
