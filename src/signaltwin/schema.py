from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


Score = float
RiskLevel = Literal["low", "medium", "high"]


class StrictBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class FlexibleBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class Building(StrictBaseModel):
    id: str
    location_type: str
    age_years: int = Field(ge=0)


class Asset(StrictBaseModel):
    id: str
    type: str
    orientation: str
    material: "AssetMaterial" = Field(default_factory=lambda: AssetMaterial())
    vulnerability: "AssetVulnerability" = Field(default_factory=lambda: AssetVulnerability())


class AssetMaterial(StrictBaseModel):
    surface: str | None = None
    backing: str | None = None
    primary: str | None = None


class AssetVulnerability(StrictBaseModel):
    moisture: RiskLevel | None = None
    mold: RiskLevel | None = None
    moss: RiskLevel | None = None
    deformation: RiskLevel | None = None
    comfort_degradation: RiskLevel | None = None
    communication_drift: RiskLevel | None = None
    heat_gain: RiskLevel | None = None
    salt_damage: RiskLevel | None = None


class Maintenance(StrictBaseModel):
    last_inspection_days_ago: int | None = Field(default=None, ge=0)
    last_cleaning_days_ago: int | None = Field(default=None, ge=0)
    last_repair_days_ago: int | None = Field(default=None, ge=0)
    last_repaint_days_ago: int | None = Field(default=None, ge=0)
    last_filter_cleaning_days_ago: int | None = Field(default=None, ge=0)


class BmsContext(StrictBaseModel):
    temperature_7d_avg_c: float | None = None
    humidity_7d_avg_percent: Score | None = Field(default=None, ge=0, le=100)
    illuminance_7d_avg_lux: float | None = Field(default=None, ge=0)
    sound_level_7d_avg_db: float | None = Field(default=None, ge=0)
    motion_hours_7d: float | None = Field(default=None, ge=0)
    flow_events_7d: int | None = Field(default=None, ge=0)
    hvac_on_hours_7d: float | None = Field(default=None, ge=0)
    dehumidify_on_hours_7d: float | None = Field(default=None, ge=0)
    current_amp_avg: float | None = Field(default=None, ge=0)
    device_on_off_changes_7d: int | None = Field(default=None, ge=0)


class WifiCsiSignal(StrictBaseModel):
    csi_drift_score: Score | None = Field(default=None, ge=0, le=1)
    snr_delta_db: float | None = None
    rssi_dbm: float | None = None
    snr_db: float | None = None
    packet_loss_rate: Score | None = Field(default=None, ge=0, le=1)
    retransmission_rate: Score | None = Field(default=None, ge=0, le=1)
    multipath_change_score: Score | None = Field(default=None, ge=0, le=1)
    baseline_similarity: Score | None = Field(default=None, ge=0, le=1)


class PztSignal(StrictBaseModel):
    peak_amplitude_delta: float | None = None
    resonance_shift_percent: float | None = None
    attenuation_delta: Score | None = Field(default=None, ge=0, le=1)
    arrival_time_delta_us: float | None = None
    event_count: int | None = Field(default=None, ge=0)
    baseline_similarity: Score | None = Field(default=None, ge=0, le=1)


class AcousticSignal(StrictBaseModel):
    frequency_response_drift: Score | None = Field(default=None, ge=0, le=1)
    rt60_delta_percent: float | None = None
    rt60_seconds: float | None = Field(default=None, ge=0)
    low_freq_resonance_shift: Score | None = Field(default=None, ge=0, le=1)
    high_freq_absorption_delta: Score | None = Field(default=None, ge=0, le=1)
    door_seal_leak_score: Score | None = Field(default=None, ge=0, le=1)
    unusual_noise_score: Score | None = Field(default=None, ge=0, le=1)
    baseline_similarity: Score | None = Field(default=None, ge=0, le=1)


class ThermalSignal(StrictBaseModel):
    dew_point_margin_min_c: float | None = None
    cold_spot_count: int | None = Field(default=None, ge=0)
    thermal_gradient_score: Score | None = Field(default=None, ge=0, le=1)
    surface_temp_min_c: float | None = None
    surface_temp_avg_c: float | None = None
    surface_temp_max_c: float | None = None


class VisualDefect(StrictBaseModel):
    type: str
    severity: Score = Field(ge=0, le=1)
    area_ratio: Score | None = Field(default=None, ge=0, le=1)
    length_m: float | None = Field(default=None, ge=0)


class VisualSignal(StrictBaseModel):
    detected_defects: list[VisualDefect] = Field(default_factory=list)


class Signals(StrictBaseModel):
    wifi_csi: WifiCsiSignal | None = None
    pzt: PztSignal | None = None
    acoustic: AcousticSignal | None = None
    thermal: ThermalSignal | None = None
    visual: VisualSignal | None = None


class SignalTwinScenario(StrictBaseModel):
    scenario: str
    building: Building
    asset: Asset
    maintenance: Maintenance
    bms: BmsContext
    signals: Signals
    expected: dict[str, Any]


class RiskScores(StrictBaseModel):
    moisture_risk: Score = Field(ge=0, le=1)
    mold_risk: Score = Field(ge=0, le=1)
    moss_risk: Score | None = Field(default=None, ge=0, le=1)
    wood_deformation_risk: Score = Field(ge=0, le=1)
    crack_or_void_risk: Score = Field(ge=0, le=1)
    communication_drift_risk: Score = Field(ge=0, le=1)
    comfort_degradation_risk: Score = Field(ge=0, le=1)
    maintenance_priority: Score | None = Field(default=None, ge=0, le=1)


class Recommendation(StrictBaseModel):
    priority: Literal["low", "low_medium", "medium", "medium_high", "high"]
    action: str
    maintenance_type: str


class RiskReport(StrictBaseModel):
    asset_id: str
    risk_scores: RiskScores
    evidence: list[str] = Field(min_length=1)
    recommendation: Recommendation
