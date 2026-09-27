"""
Unit tests for Foundational Mathematics Generator: Number Bonds, Fractions & Decomposition
Validates 6-Pillar Generator Architecture Contract (Rules 20-26):
- Calendar & Term metadata
- 5 Modes (compound, elementary_additive, elementary_multiplicative, elementary_fraction_strips, stokke_speed_sprint)
- Standardized misconception taxonomy
- Teacher-editable marking schema
- Deterministic 3-tier pre-baked hints
- Seed determinism
"""

import pytest
from app.utils.foundational_math.number_bonds_generator import generate_number_bonds_drill


def test_modes_contract_compliance():
    modes = [
        "compound",
        "elementary_additive",
        "elementary_multiplicative",
        "elementary_fraction_strips",
        "stokke_speed_sprint"
    ]

    for mode in modes:
        drill = generate_number_bonds_drill(seed=42, mode=mode, grade=8)

        # Pillar 1: Calendar & Term metadata
        assert "term" in drill
        assert drill["term"] in [1, 2, 3, 4]
        assert "caps_weight_percent" in drill
        assert drill["caps_weight_percent"] > 0
        assert "suggested_duration_mins" in drill
        assert drill["suggested_duration_mins"] > 0

        # Pillar 2: Prompt and LaTeX representation
        assert "prompt" in drill and len(drill["prompt"]) > 0
        assert "prompt_latex" in drill

        # Pillar 3: Misconception taxonomy
        assert "misconception_tags" in drill
        assert isinstance(drill["misconception_tags"], list)
        assert len(drill["misconception_tags"]) > 0
        for tag in drill["misconception_tags"]:
            assert tag.islower(), f"Tag {tag} should be lowercase snake_case"

        # Pillar 4: Marking schema
        schema = drill.get("marking_schema")
        assert schema is not None, f"Marking schema missing for mode {mode}"
        assert "total_marks" in schema
        assert schema["total_marks"] > 0
        assert "marking_points" in schema
        assert len(schema["marking_points"]) > 0
        assert "carry_forward_rule" in schema

        # Pillar 5: Deterministic 3-Tier hints
        hints = drill.get("hints")
        assert hints is not None, f"Hints missing for mode {mode}"
        assert "tier_1_location" in hints
        assert "tier_2_directional" in hints
        assert "tier_3_worked_step" in hints
        assert len(hints["tier_1_location"]) > 0
        assert len(hints["tier_2_directional"]) > 0
        assert len(hints["tier_3_worked_step"]) > 0


def test_seed_determinism():
    """Confirms that two generations with the identical seed produce identical values."""
    drill_a = generate_number_bonds_drill(seed=12345, mode="compound")
    drill_b = generate_number_bonds_drill(seed=12345, mode="compound")

    assert drill_a["prompt"] == drill_b["prompt"]
    assert drill_a["prompt_latex"] == drill_b["prompt_latex"]
    assert drill_a["answer"] == drill_b["answer"]
    assert drill_a["hints"] == drill_b["hints"]
    assert drill_a["marking_schema"] == drill_b["marking_schema"]


def test_stokke_speed_sprint_structure():
    """Confirms Stokke 60s speed sprint outputs multiple rapid-fire items."""
    sprint = generate_number_bonds_drill(seed=999, mode="stokke_speed_sprint")
    assert sprint["mode"] == "stokke_speed_sprint"
    items = sprint.get("items", [])
    assert len(items) >= 5, "Stokke sprint should have at least 5 rapid-fire items"
    for item in items:
        assert "expr" in item
        assert "answer" in item
        assert "rule" in item


def test_fraction_strips_tang_visual():
    """Confirms fraction strips output visual bar model partitions and equivalence."""
    fraction_drill = generate_number_bonds_drill(seed=777, mode="elementary_fraction_strips")
    assert fraction_drill["mode"] == "elementary_fraction_strips"
    assert "visual_strip_model" in fraction_drill
    vis = fraction_drill["visual_strip_model"]
    assert "whole_units" in vis
    assert "partitions" in vis
    assert "shaded" in vis
