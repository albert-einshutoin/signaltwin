from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_readiness_doc_mentions_all_no_hardware_phases() -> None:
    text = (PROJECT_ROOT / "docs" / "pre-hardware-readiness.md").read_text()

    for phrase in (
        "Minimal MVP",
        "Adapter-ready MVP",
        "Adapter Registry",
        "Baseline Store",
        "No-Hardware Demo Pipeline",
        "Mock API And Dashboard Contract",
    ):
        assert phrase in text
    assert "hardware-required work" in text


def test_hardware_handoff_requires_selected_device_path() -> None:
    text = (PROJECT_ROOT / "tasks" / "hardware-handoff.md").read_text()

    assert "selected first hardware path" in text
    assert "raw output sample" in text
    assert "fixture adapter with real adapter" in text
    assert "do not expand real hardware implementation tasks" in text


def test_handoff_recommends_first_real_device_path() -> None:
    text = (PROJECT_ROOT / "tasks" / "hardware-handoff.md").read_text()

    assert "BMS CSV + Thermal + Visual" in text
    assert "WiFi CSI / PZT / Acoustic" in text
    assert "user can override" in text


def test_proposal_pack_mentions_pre_hardware_readiness() -> None:
    completion = (
        PROJECT_ROOT / "signaltwin_proposal_pack" / "docs" / "mvp-completion-report.md"
    ).read_text()
    adapter_plan = (
        PROJECT_ROOT / "signaltwin_proposal_pack" / "docs" / "next-phase-adapter-plan.md"
    ).read_text()
    combined = "\n".join([completion, adapter_plan])

    assert "Pre-hardware readiness" in combined
    assert "no-hardware work is complete" in combined
    assert "does not claim real sensor validation" in combined


def test_no_detailed_real_hardware_tasks_are_expanded() -> None:
    task_files = list((PROJECT_ROOT / "tasks").glob("phase*/**/*.md"))
    combined = "\n".join(path.read_text() for path in task_files)

    assert "Status: todo" not in (PROJECT_ROOT / "tasks" / "phase15" / "phase_status.md").read_text()
    assert "real ESP32 capture implementation" not in combined
    assert "real MLX90640 driver implementation" not in combined
    assert "real PZT ADC driver implementation" not in combined
