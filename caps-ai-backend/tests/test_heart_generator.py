"""Tests for Heart Subskill Builder & Topic-First Progression (Milestone 1)."""

import pytest
from app.utils.life_sciences.heart_generator import generate_heart_question, mark_heart_answer
from app.utils.natural_sciences import ns9_circulatory_respiratory_generator as ns9_crs
from app.utils.life_sciences import ls10_transport_systems_animals_generator as ls10_tsa


def test_heart_generator_determinism():
    """Same seed must produce identical question output."""
    q1 = generate_heart_question(seed=12345, grade=10)
    q2 = generate_heart_question(seed=12345, grade=10)
    assert q1["question_text"] == q2["question_text"]
    assert q1["final_answer"] == q2["final_answer"]
    assert q1["diagram_spec"] == q2["diagram_spec"]


def test_anti_leak_contract_no_names_in_pins():
    """Client pins must NEVER leak the anatomical name or key."""
    for seed in [101, 202, 303, 404, 505]:
        q = generate_heart_question(seed=seed, grade=9)
        pins = q["diagram_spec"]["pins"]
        assert len(pins) >= 1
        for p in pins:
            assert "name" not in p, f"LEAK DETECTED: 'name' found in pin {p}"
            assert "key" not in p, f"LEAK DETECTED: 'key' found in pin {p}"
            assert "pin" in p
            assert "ref" in p
            assert "anchor" in p
            assert p["role"] == "target"


def test_seed_entropy_variation():
    """Different seeds must produce varying target sets and/or archetypes."""
    pins_set = set()
    for seed in range(100, 115):
        q = generate_heart_question(seed=seed, grade=10)
        pin_refs = tuple(p["ref"] for p in q["diagram_spec"]["pins"])
        pins_set.add(pin_refs)
    assert len(pins_set) > 5, "Insufficient pin variation across seeds"


def test_grade_9_vs_grade_10_masking():
    """Grade 9 must never select ultrastructures (valves, nodes)."""
    for seed in range(50):
        q_g9 = generate_heart_question(seed=seed, grade=9)
        server_refs = q_g9["_server_verification"]
        for letter, data in server_refs.items():
            assert data["key"] not in ("tricuspid_valve", "bicuspid_valve", "sa_node", "av_node", "semilunar_valves"), (
                f"Grade 9 leaked advanced ultrastructure: {data['key']}"
            )


def test_server_side_marking_synonyms():
    """Marking must tolerate authentic curriculum synonyms."""
    target_entry = {
        "key": "bicuspid_valve",
        "name": "Bicuspid (Mitral) Valve",
        "synonyms": ["bicuspid valve", "mitral valve", "left atrioventricular valve", "left av valve", "bicuspid"],
    }
    assert mark_heart_answer("bicuspid valve", target_entry)["is_correct"] is True
    assert mark_heart_answer("Mitral valve", target_entry)["is_correct"] is True
    assert mark_heart_answer("left AV valve", target_entry)["is_correct"] is True
    assert mark_heart_answer("aorta", target_entry)["is_correct"] is False


def test_ns9_circulatory_respiratory_topic_sequence():
    """Grade 9 Circulatory & Respiratory topic generator must sequence heart questions alongside breathing, alveoli, vessels, and pulse investigation."""
    questions = ns9_crs.generate(seed=1001, count=6, grade=9)
    assert len(questions) == 6

    subskills = [q["subskill"] for q in questions]
    assert subskills == [
        "chamber_differentiation",
        "breathing_mechanics",
        "alveolus_gaseous_exchange",
        "blood_vessel_direction",
        "blood_vessels_comparison",
        "pulse_rate_exercise_investigation",
    ]

    # Question 0 is Heart Textbook Cross-Section with g9 mask
    assert questions[0]["diagram_spec"]["image_type"] == "human_heart"
    assert questions[0]["diagram_spec"]["view"] == "textbook"
    assert questions[0]["diagram_spec"]["grade_mask"] == "g9"

    # Question 2 is Alveolus Gaseous Exchange with g9 mask and anti-leak pins
    assert questions[2]["diagram_spec"]["image_type"] == "alveolus_gas_exchange"
    for p in questions[2]["diagram_spec"]["pins"]:
        assert "name" not in p

    # Question 3 is Heart Blood Flow Schematic with g9 mask
    assert questions[3]["diagram_spec"]["image_type"] == "human_heart"
    assert questions[3]["diagram_spec"]["view"] == "flow"
    assert questions[3]["diagram_spec"]["grade_mask"] == "g9"


def test_ls10_transport_systems_animals_topic_sequence():
    """Grade 10 Transport Systems in Animals topic generator must sequence heart anatomy, cardiac cycle, circulation pathways, vessel histology, pacemaker/ECG, and lymphatic/diseases."""
    questions = ls10_tsa.generate(seed=1001, count=6, grade=10)
    assert len(questions) == 6

    subskills = [q["subskill"] for q in questions]
    assert subskills == [
        "valve_mechanics",
        "cardiac_cycle_phase",
        "open_closed_single_double_circulation",
        "blood_vessel_histology_and_function",
        "electrical_pacemaker",
        "lymphatic_system_and_cardiovascular_diseases",
    ]

    # Question 0: Heart Textbook Cross-Section (g10)
    assert questions[0]["diagram_spec"]["image_type"] == "human_heart"
    assert questions[0]["diagram_spec"]["view"] == "textbook"
    assert questions[0]["diagram_spec"]["grade_mask"] == "g10"
    assert len(questions[0]["simulearn_script"]["steps"]) == 3

    # Question 1: Cardiac Cycle Flow Schematic (g10)
    assert questions[1]["diagram_spec"]["image_type"] == "human_heart"
    assert questions[1]["diagram_spec"]["view"] == "flow"
    assert questions[1]["diagram_spec"]["grade_mask"] == "g10"

    # Question 4: Electrical Pacemaker Exam Paper Line-Art (g10)
    assert questions[4]["diagram_spec"]["image_type"] == "human_heart"
    assert questions[4]["diagram_spec"]["view"] == "exam"
    assert questions[4]["diagram_spec"]["grade_mask"] == "g10"
