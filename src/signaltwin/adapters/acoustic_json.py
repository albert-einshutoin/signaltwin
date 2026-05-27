from __future__ import annotations

from signaltwin.adapters._helpers import read_json_object
from signaltwin.adapters.base import Adapter, AdapterInput, AdapterOutput


class AcousticJsonAdapter(Adapter):
    source_name = "acoustic-json-fixture"

    def load(self, adapter_input: AdapterInput) -> AdapterOutput:
        raw = read_json_object(adapter_input.path, self.source_name)
        payload = {
            "frequency_response_drift": raw.get("frequency_response_drift"),
            "rt60_seconds": raw.get("rt60_seconds"),
            "low_freq_resonance_shift": raw.get("low_freq_resonance_shift"),
            "high_freq_absorption_delta": raw.get("high_freq_absorption_delta"),
            "door_seal_leak_score": raw.get("door_seal_leak_score"),
            "unusual_noise_score": raw.get("unusual_noise_score"),
            "baseline_similarity": raw.get("baseline_similarity"),
        }
        return AdapterOutput(
            source_family="acoustic",
            source_name=self.source_name,
            path=adapter_input.path,
            normalized_key="acoustic",
            payload=payload,
        )
