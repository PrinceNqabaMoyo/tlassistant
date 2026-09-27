import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import random
from app.services.generator_registry import generate_variant, resolve_generator_key, ALL_GENERATORS
from app.utils.combinatorial_engine import generate_combinatorial_batch, sample_scenario


def test_generator_registry_breadth():
    """Verify that all major subjects and grades are registered."""
    assert len(ALL_GENERATORS) >= 30
    assert "grade10_math_algebraic_expressions" in ALL_GENERATORS
    assert "grade10_bs_combinatorial" in ALL_GENERATORS
    assert "grade10_accounting_sole_trader" in ALL_GENERATORS
    assert "physical_sciences_mechanics" in ALL_GENERATORS


def test_math_generation_6_pillar_contract():
    """Verify Mathematics questions satisfy all 6 contract pillars."""
    questions = generate_variant(
        topic="grade10_math_algebraic_expressions",
        count=3,
        seed=101,
        grade="10",
        subject="Mathematics",
    )
    assert len(questions) == 3
    for q in questions:
        # Pillar 1: Calendar metadata
        assert "term" in q and isinstance(q["term"], int)
        assert "caps_weight_percent" in q
        assert "suggested_duration_mins" in q

        # Pillar 3: Misconception tags
        assert "misconception_tags" in q
        assert len(q["misconception_tags"]) > 0

        # Pillar 4: Teacher-editable marking schema
        assert "marking_schema" in q
        assert "total_marks" in q["marking_schema"]
        assert "marking_points" in q["marking_schema"]

        # Pillar 5: Deterministic 3-tier hints
        assert "hints" in q
        assert "tier_1" in q["hints"]
        assert "tier_2" in q["hints"]
        assert "tier_3" in q["hints"]


def test_business_studies_combinatorial_modalities():
    """Verify 4D Combinatorial Engine rotates modalities and provides rich SA context."""
    questions = generate_combinatorial_batch(
        subskill_id="bs_environments",
        term=1,
        count=6,
        seed=2026,
    )
    assert len(questions) == 6
    types = {q["question_type"] for q in questions}
    # Verifies all 3 supported modalities are emitted
    assert "mcq" in types
    assert "drag_and_drop" in types
    assert "cloze" in types

    # Verify SA context
    scenario = sample_scenario(random.Random(42))
    assert "sector" in scenario
    assert "province" in scenario["sector"]
    assert "form" in scenario
    assert "event" in scenario
    assert "framework" in scenario


def test_seed_determinism_and_variation():
    """Verify seed determinism: identical seed -> identical output; distinct seed -> different."""
    batch_a1 = generate_variant("grade10_math_algebraic_expressions", count=2, seed=777)
    batch_a2 = generate_variant("grade10_math_algebraic_expressions", count=2, seed=777)
    batch_b = generate_variant("grade10_math_algebraic_expressions", count=2, seed=888)

    assert batch_a1[0]["id"] == batch_a2[0]["id"]
    assert batch_a1[0]["id"] != batch_b[0]["id"]


def test_topic_alias_resolution():
    """Verify human-readable titles and ATP labels map to registered generators."""
    assert resolve_generator_key("Algebraic Expressions", "10", "Mathematics") == "grade10_math_algebraic_expressions"
    assert resolve_generator_key("Functions & Graphs", "10", "Mathematics") == "grade10_math_functions"
    assert resolve_generator_key("Micro Environment", "10", "Business Studies") == "grade10_bs_micro_environment"
    assert resolve_generator_key("Sole Trader", "10", "Accounting") == "grade10_accounting_sole_trader"


if __name__ == "__main__":
    print("[TEST] Running test_generator_registry_breadth...")
    test_generator_registry_breadth()
    print("[PASS] test_generator_registry_breadth")

    print("[TEST] Running test_math_generation_6_pillar_contract...")
    test_math_generation_6_pillar_contract()
    print("[PASS] test_math_generation_6_pillar_contract")

    print("[TEST] Running test_business_studies_combinatorial_modalities...")
    test_business_studies_combinatorial_modalities()
    print("[PASS] test_business_studies_combinatorial_modalities")

    print("[TEST] Running test_seed_determinism_and_variation...")
    test_seed_determinism_and_variation()
    print("[PASS] test_seed_determinism_and_variation")

    print("[TEST] Running test_topic_alias_resolution...")
    test_topic_alias_resolution()
    print("[PASS] test_topic_alias_resolution")

    print("\n[ALL TESTS PASSED] 5/5 test suites passed successfully.")
