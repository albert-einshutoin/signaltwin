from __future__ import annotations

from signaltwin.normalizer import NormalizedScenario, normalize_scenario
from signaltwin.schema import Recommendation, RiskReport, RiskScores, SignalTwinScenario


def calculate_risk_report(scenario: NormalizedScenario | SignalTwinScenario) -> RiskReport:
    normalized = normalize_scenario(scenario) if isinstance(scenario, SignalTwinScenario) else scenario
    evidence: list[str] = []

    moisture = _moisture_risk(normalized, evidence)
    mold = _mold_risk(normalized, evidence)
    moss = _moss_risk(normalized, evidence)
    wood_deformation = _wood_deformation_risk(normalized, evidence)
    crack_or_void = _crack_or_void_risk(normalized, evidence)
    communication = _communication_drift_risk(normalized, evidence)
    comfort = _comfort_degradation_risk(normalized, evidence)

    scores = RiskScores(
        moisture_risk=moisture,
        mold_risk=mold,
        moss_risk=moss,
        wood_deformation_risk=wood_deformation,
        crack_or_void_risk=crack_or_void,
        communication_drift_risk=communication,
        comfort_degradation_risk=comfort,
        maintenance_priority=max(
            moisture,
            mold,
            moss,
            wood_deformation,
            crack_or_void,
            communication,
            comfort,
        ),
    )

    return RiskReport(
        asset_id=normalized.asset_id,
        risk_scores=scores,
        evidence=evidence or ["No high-impact risk evidence was detected."],
        recommendation=_recommendation(scores),
    )


def _moisture_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    bms = scenario.bms
    thermal = scenario.signals.thermal
    pzt = scenario.signals.pzt
    score = 0.0

    humidity = _number(bms.humidity_7d_avg_percent)
    if humidity is not None and humidity >= 80:
        score += 0.30
        evidence.append(f"7-day average humidity is {humidity:g}%.")
    elif humidity is not None and humidity >= 75:
        score += 0.22
        evidence.append(f"7-day average humidity is elevated at {humidity:g}%.")
    elif humidity is not None and humidity >= 70:
        score += 0.12

    dew_margin = _number(thermal.dew_point_margin_min_c if thermal is not None else None)
    if dew_margin is not None and dew_margin <= 1.5:
        score += 0.20
        evidence.append(f"Thermal dew point margin is only {dew_margin:g}C.")
    elif dew_margin is not None and dew_margin <= 2.5:
        score += 0.12

    cold_spots = _number(thermal.cold_spot_count if thermal is not None else None)
    if cold_spots is not None and cold_spots >= 3:
        score += 0.10
        evidence.append(f"Thermal frame shows {cold_spots:g} cold spots.")

    if scenario.asset.vulnerability.moisture == "high":
        score += 0.08

    asset_material = _asset_material_hint(scenario)
    if asset_material:
        score += 0.08
        evidence.append(f"The asset material context includes {asset_material}.")

    attenuation = _number(pzt.attenuation_delta if pzt is not None else None)
    if attenuation is not None and attenuation >= 0.20:
        score += 0.14
        evidence.append(f"PZT attenuation increased by {attenuation * 100:.0f}% from baseline.")

    inspection_days = _number(scenario.maintenance.last_inspection_days_ago)
    if inspection_days is not None and inspection_days >= 180:
        score += 0.10
        evidence.append(f"Last inspection was {inspection_days:g} days ago.")

    return _clamp(score)


def _mold_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    score = 0.0
    humidity = _number(scenario.bms.humidity_7d_avg_percent)
    illuminance = _number(scenario.bms.illuminance_7d_avg_lux)
    thermal = scenario.signals.thermal

    if humidity is not None and humidity >= 80:
        score += 0.26
        evidence.append(f"High humidity duration increases mold risk at {humidity:g}%.")
    elif humidity is not None and humidity >= 75:
        score += 0.18

    if illuminance is not None and illuminance <= 120:
        score += 0.12
        evidence.append(f"Low illuminance context is {illuminance:g} lux.")

    dew_margin = _number(thermal.dew_point_margin_min_c if thermal is not None else None)
    if dew_margin is not None and dew_margin <= 1.5:
        score += 0.16

    if scenario.asset.vulnerability.mold in {"medium", "high"}:
        score += 0.16

    cleaning_days = _number(scenario.maintenance.last_cleaning_days_ago)
    if cleaning_days is not None and cleaning_days >= 180:
        score += 0.10

    return _clamp(score)


def _moss_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    visual = scenario.signals.visual
    defects = visual.detected_defects if visual is not None else []
    moss_defects = [defect for defect in defects if defect.type == "moss"]
    score = 0.0

    if moss_defects:
        strongest = max(_number(defect.severity, default=0.0) for defect in moss_defects)
        area = max(_number(defect.area_ratio, default=0.0) for defect in moss_defects)
        score += 0.42 + strongest * 0.25 + area
        evidence.append(f"Visual moss detection severity is {strongest:.2f}.")

    if scenario.asset.vulnerability.moss == "high":
        score += 0.12

    illuminance = _number(scenario.bms.illuminance_7d_avg_lux)
    if illuminance is not None and illuminance <= 100:
        score += 0.08

    cleaning_days = _number(scenario.maintenance.last_cleaning_days_ago)
    if cleaning_days is not None and cleaning_days >= 240:
        score += 0.12
        evidence.append(f"Last cleaning was {cleaning_days:g} days ago.")

    return _clamp(score)


def _wood_deformation_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    pzt = scenario.signals.pzt
    thermal = scenario.signals.thermal
    score = 0.0

    resonance = _number(pzt.resonance_shift_percent if pzt is not None else None)
    if resonance is not None and resonance >= 5:
        score += 0.20
        evidence.append(f"PZT resonance shifted by {resonance:g}%.")

    attenuation = _number(pzt.attenuation_delta if pzt is not None else None)
    if attenuation is not None and attenuation >= 0.20:
        score += 0.12

    thermal_gradient = _number(thermal.thermal_gradient_score if thermal is not None else None)
    if thermal_gradient is not None and thermal_gradient >= 0.30:
        score += 0.08

    if scenario.asset.vulnerability.deformation in {"medium", "high"}:
        score += 0.08

    repair_days = _number(scenario.maintenance.last_repair_days_ago)
    if repair_days is not None and repair_days >= 700:
        score += 0.08

    return _clamp(score)


def _crack_or_void_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    pzt = scenario.signals.pzt
    acoustic = scenario.signals.acoustic
    visual = scenario.signals.visual
    score = 0.0

    resonance = _number(pzt.resonance_shift_percent if pzt is not None else None)
    if resonance is not None and resonance >= 5:
        score += 0.12

    attenuation = _number(pzt.attenuation_delta if pzt is not None else None)
    if attenuation is not None and attenuation >= 0.20:
        score += 0.10
        evidence.append(f"PZT attenuation delta is {attenuation:.2f}.")

    acoustic_drift = _number(acoustic.frequency_response_drift if acoustic is not None else None)
    if acoustic_drift is not None and acoustic_drift >= 0.15:
        score += 0.10
        evidence.append(f"Acoustic frequency response drift is {acoustic_drift:.2f}.")

    defects = visual.detected_defects if visual is not None else []
    if any(defect.type == "hairline_crack" for defect in defects):
        score += 0.12
        evidence.append("Visual inspection detected a hairline crack.")

    return _clamp(score)


def _communication_drift_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    wifi = scenario.signals.wifi_csi
    score = 0.0

    csi = _number(wifi.csi_drift_score if wifi is not None else None)
    if csi is not None and csi >= 0.25:
        score += 0.26
        evidence.append(f"CSI drift score is {csi:.2f}.")
    elif csi is not None and csi >= 0.15:
        score += 0.12

    snr_delta = _number(wifi.snr_delta_db if wifi is not None else None)
    if snr_delta is not None and snr_delta <= -6:
        score += 0.18
        evidence.append(f"SNR delta is {snr_delta:g} dB.")
    elif snr_delta is not None and snr_delta <= -3:
        score += 0.08

    packet_loss = _number(wifi.packet_loss_rate if wifi is not None else None)
    if packet_loss is not None and packet_loss >= 0.05:
        score += 0.18
        evidence.append(f"Packet loss rate is {packet_loss:.3f}.")

    retransmission = _number(wifi.retransmission_rate if wifi is not None else None)
    if retransmission is not None and retransmission >= 0.10:
        score += 0.12

    multipath = _number(wifi.multipath_change_score if wifi is not None else None)
    if multipath is not None and multipath >= 0.25:
        score += 0.12

    similarity = _number(wifi.baseline_similarity if wifi is not None else None, default=1.0)
    if similarity is not None and similarity <= 0.70:
        score += 0.10

    return _clamp(score)


def _comfort_degradation_risk(scenario: NormalizedScenario, evidence: list[str]) -> float:
    bms = scenario.bms
    thermal = scenario.signals.thermal
    acoustic = scenario.signals.acoustic
    score = 0.0

    hvac_hours = _number(bms.hvac_on_hours_7d)
    if hvac_hours is not None and hvac_hours >= 100:
        score += 0.20
        evidence.append(f"HVAC ran for {hvac_hours:g} hours over 7 days.")
    elif hvac_hours is not None and hvac_hours >= 80:
        score += 0.10

    humidity = _number(bms.humidity_7d_avg_percent)
    if humidity is not None and humidity >= 70:
        score += 0.12

    thermal_gradient = _number(thermal.thermal_gradient_score if thermal is not None else None)
    if thermal_gradient is not None and thermal_gradient >= 0.40:
        score += 0.20
        evidence.append(f"Thermal gradient score is {thermal_gradient:.2f}.")

    noise = _number(acoustic.unusual_noise_score if acoustic is not None else None)
    if noise is not None and noise >= 0.30:
        score += 0.12
        evidence.append(f"Unusual acoustic noise score is {noise:.2f}.")

    current = _number(bms.current_amp_avg)
    if current is not None and current >= 3.0:
        score += 0.08

    if scenario.asset.vulnerability.comfort_degradation in {"medium", "high"}:
        score += 0.10

    return _clamp(score)


def _recommendation(scores: RiskScores) -> Recommendation:
    ranked = {
        "moisture_risk": scores.moisture_risk,
        "mold_risk": scores.mold_risk,
        "moss_risk": scores.moss_risk or 0.0,
        "wood_deformation_risk": scores.wood_deformation_risk,
        "crack_or_void_risk": scores.crack_or_void_risk,
        "communication_drift_risk": scores.communication_drift_risk,
        "comfort_degradation_risk": scores.comfort_degradation_risk,
    }
    risk_name, risk_score = max(ranked.items(), key=lambda item: item[1])
    priority = _priority(risk_score)

    if risk_name in {"moisture_risk", "mold_risk", "wood_deformation_risk", "crack_or_void_risk"}:
        return Recommendation(
            priority=priority,
            action="Inspect the affected asset and verify dehumidification operation within 30 days",
            maintenance_type="moisture_inspection",
        )
    if risk_name == "moss_risk":
        return Recommendation(
            priority=priority,
            action="Clean the affected surface and inspect drainage or shading conditions within 45 days",
            maintenance_type="surface_cleaning",
        )
    if risk_name == "communication_drift_risk":
        return Recommendation(
            priority=priority,
            action="Inspect AP position or interference sources",
            maintenance_type="wireless_path_inspection",
        )
    return Recommendation(
        priority=priority,
        action="Inspect HVAC filter and airflow",
        maintenance_type="hvac_filter_airflow_inspection",
    )


def _priority(score: float) -> str:
    if score >= 0.70:
        return "high"
    if score >= 0.60:
        return "medium_high"
    if score >= 0.40:
        return "medium"
    if score >= 0.25:
        return "low_medium"
    return "low"


def _asset_material_hint(scenario: NormalizedScenario) -> str:
    surface = scenario.asset.material.surface or scenario.asset.material.primary or ""
    if surface:
        return surface.replace("_", " ")
    return ""


def _number(value: object, default: float | None = None) -> float | None:
    if value is None:
        return default
    return float(value)


def _clamp(value: float) -> float:
    return round(max(0.0, min(1.0, value)), 4)
