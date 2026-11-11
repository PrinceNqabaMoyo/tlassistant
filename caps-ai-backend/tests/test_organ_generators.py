"""Unit tests for Milestone 2 unbundled organ generators and diagram builders."""

import pytest
from app.utils.natural_sciences.ns9_digestive_system_generator import generate as gen_ns9_digestive
from app.utils.life_sciences.ls11_animal_nutrition_generator import generate as gen_ls11_nutrition
from app.utils.life_sciences.ls11_gaseous_exchange_generator import generate as gen_ls11_gas_exchange
from app.utils.life_sciences.ls11_excretion_humans_generator import generate as gen_ls11_excretion
from app.utils.life_sciences.organ_diagram_builders import (
    build_alveolus_question,
    build_digestive_question,
    build_villus_question,
    build_nephron_question,
)


def test_ns9_digestive_diagram_question():
    q = build_digestive_question(42, grade=9, mode="practice")
    assert q["term"] == 1
    assert q["target_pin"] in ["A", "B", "C", "D"]
    assert "diagram_spec" in q
    spec = q["diagram_spec"]
    assert spec["image_type"] == "human_digestive_system"
    assert len(spec["pins"]) == 4
    for p in spec["pins"]:
        assert "ref" in p
        assert "name" not in p  # Anti-leak: client pins must NOT leak structure names


def test_ls11_animal_nutrition_diagram_questions():
    # Villus question
    q_villus = build_villus_question(101, grade=11, mode="practice")
    assert q_villus["term"] == 2
    assert q_villus["diagram_spec"]["image_type"] == "intestinal_villus"
    assert len(q_villus["diagram_spec"]["pins"]) == 4
    for p in q_villus["diagram_spec"]["pins"]:
        assert "ref" in p
        assert "name" not in p

    # Macroscopic digestive question
    q_digest = build_digestive_question(202, grade=11, mode="practice")
    assert q_digest["diagram_spec"]["image_type"] == "human_digestive_system"
    assert len(q_digest["diagram_spec"]["pins"]) == 4


def test_ls11_gaseous_exchange_diagram_question():
    q = build_alveolus_question(303, grade=11, mode="practice")
    assert q["term"] == 3
    assert q["diagram_spec"]["image_type"] == "alveolus_gas_exchange"
    assert len(q["diagram_spec"]["pins"]) == 4
    for p in q["diagram_spec"]["pins"]:
        assert "ref" in p
        assert "name" not in p


def test_ls11_excretion_diagram_question():
    q = build_nephron_question(404, grade=11, mode="practice")
    assert q["term"] == 3
    assert q["diagram_spec"]["image_type"] == "human_nephron"
    assert len(q["diagram_spec"]["pins"]) == 4
    for p in q["diagram_spec"]["pins"]:
        assert "ref" in p
        assert "name" not in p


def test_unbundled_generators_execution():
    # Test full generator dispatch across subskills
    q1 = gen_ns9_digestive(seed=123)
    assert q1["term"] == 1
    assert "options" in q1 or "marking_points" in q1

    q2 = gen_ls11_nutrition(seed=456)
    assert q2["term"] == 2
    assert "options" in q2 or "marking_points" in q2

    q3 = gen_ls11_gas_exchange(seed=789)
    assert q3["term"] == 3
    assert "options" in q3 or "marking_points" in q3

    q4 = gen_ls11_excretion(seed=999)
    assert q4["term"] == 3
    assert "options" in q4 or "marking_points" in q4
