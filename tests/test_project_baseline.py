from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_package_imports():
    import signaltwin

    assert signaltwin.__version__ == "0.1.0"


def test_repository_contains_minimal_mvp_scenarios():
    expected = {
        "coastal_villa_moss_risk.yml",
        "communication_drift.yml",
        "hvac_efficiency_drift.yml",
        "rainy_season_wood_wall.yml",
    }

    actual = {path.name for path in (PROJECT_ROOT / "scenarios").glob("*.yml")}

    assert actual == expected


def test_generated_output_directory_exists():
    generated_dir = PROJECT_ROOT / "outputs" / "generated"

    assert generated_dir.is_dir()
    assert (generated_dir / ".gitkeep").is_file()
