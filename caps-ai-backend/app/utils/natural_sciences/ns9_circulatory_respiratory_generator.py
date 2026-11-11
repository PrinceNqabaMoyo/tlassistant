"""Grade 9 Natural Sciences — Term 1: Circulatory and Respiratory Systems Topic Generator.

Strictly grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/04. Circulatory and respiratory systems.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Topic-First Architecture:
- Owns the ordered curriculum subskills for Grade 9 Circulatory and Respiratory Systems:
  1. heart_structure_and_double_circulation (calls reusable heart_generator with grade_mask='g9', view='textbook')
  2. breathing_mechanics (inhalation vs. exhalation mechanics: diaphragm, intercostals, volume, pressure)
  3. alveolus_gaseous_exchange (diffusion of O2 and CO2 between alveolus and blood capillary)
  4. heart_blood_vessel_direction (calls reusable heart_generator with grade_mask='g9', view='flow')
  5. blood_vessels_comparison (structural & functional comparison of arteries, veins, and capillaries)
  6. pulse_rate_exercise_investigation (scientific investigation: resting vs. post-exercise pulse rate)
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.heart_generator import generate_heart_question

TOPIC_NAME = "Circulatory and respiratory systems"

ORDERED_SUBSKILLS = [
    "heart_structure_and_double_circulation",
    "breathing_mechanics",
    "alveolus_gaseous_exchange",
    "heart_blood_vessel_direction",
    "blood_vessels_comparison",
    "pulse_rate_exercise_investigation",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_crs"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _gen_breathing_mechanics(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    r = random.Random(seed)
    phase = r.choice(["inhalation", "exhalation"])
    if phase == "inhalation":
        question_text = (
            "During the mechanical process of breathing (ventilation), pressure changes in the thoracic cavity "
            "cause air to move into and out of the lungs.\n\n"
            "1. Describe the action and shape change of the diaphragm muscle during inhalation.\n"
            "2. State how the movement of the rib cage and diaphragm changes the volume and air pressure inside the thoracic cavity.\n"
            "3. Name the two main tubes that branch off from the trachea to carry inhaled air into the left and right lungs."
        )
        ans_str = (
            "1. The diaphragm contracts and flattens (moves downwards); "
            "2. Thoracic cavity volume increases and internal air pressure decreases below atmospheric pressure, drawing air into the lungs; "
            "3. Bronchi (singular: bronchus)."
        )
        memo = (
            "1. Diaphragm contracts and flattens / moves downwards [1].\n"
            "2. Thoracic volume increases [1] and internal pressure decreases [1], pulling air into the lungs.\n"
            "3. Bronchi [1]."
        )
        points = [
            {"point": 1, "desc": "States diaphragm contracts and flattens (moves downwards)"},
            {"point": 2, "desc": "States thoracic volume increases and pressure decreases"},
            {"point": 3, "desc": "Identifies the bronchi"},
        ]
    else:
        question_text = (
            "During the mechanical process of breathing, air enriched with carbon dioxide is expelled from the lungs.\n\n"
            "1. Describe the action and shape change of the diaphragm muscle during exhalation.\n"
            "2. State how the rib cage movement and diaphragm relaxation affect the volume and air pressure inside the chest cavity.\n"
            "3. Trace the reverse pathway of exhaled air from the alveoli to the trachea."
        )
        ans_str = (
            "1. The diaphragm relaxes and arches upwards into a dome shape; "
            "2. Chest cavity volume decreases and internal air pressure increases above atmospheric pressure, forcing air out of the lungs; "
            "3. Alveoli -> bronchioles -> bronchi -> trachea."
        )
        memo = (
            "1. Diaphragm relaxes and becomes dome-shaped / moves upwards [1].\n"
            "2. Chest volume decreases [1] and air pressure increases [1], forcing air out.\n"
            "3. Alveoli -> bronchioles -> bronchi -> trachea [1]."
        )
        points = [
            {"point": 1, "desc": "States diaphragm relaxes into a dome shape"},
            {"point": 2, "desc": "States chest volume decreases and pressure increases"},
            {"point": 3, "desc": "Traces pathway: alveoli -> bronchioles -> bronchi -> trachea"},
        ]

    return {
        "id": f"ns9_crs_breathing_{seed}",
        "question_id": f"ns9_crs_breathing_{seed}",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 1,
        "topic": TOPIC_NAME,
        "subskill": "breathing_mechanics",
        "learning_objective_id": "NS9.T1.CRS.BREATHING_MECHANICS",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "Think of how a syringe or bellows draws in air when its internal volume expands.",
            "tier_2": "When the diaphragm contracts it pulls downward (flattens), increasing chest volume and lowering pressure.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["diaphragm_dome_during_inhalation", "volume_pressure_direct_proportionality_error"],
        "keywords": ["diaphragm", "inhalation", "exhalation", "bronchi", "bronchioles", "trachea", "volume", "pressure"],
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def _gen_alveolus_gaseous_exchange(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    from app.utils.life_sciences.organ_diagram_builders import build_alveolus_question
    q = build_alveolus_question(seed=seed, grade=9, mode=mode)
    q["subject"] = "Natural Sciences"
    q["grade"] = 9
    q["term"] = 1
    q["topic"] = TOPIC_NAME
    q["subskill"] = "alveolus_gaseous_exchange"
    q["mode"] = mode
    return q


def _gen_blood_vessels_comparison(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    ctx = random.Random(seed).choice([
        "In mammalian systemic circulation",
        "During cardiovascular exercise and sustained physical activity",
        "In human clinical vascular physiology",
        "When examining systemic blood distribution through the body"
    ])
    question_text = (
        f"{ctx}, the circulatory system transports blood through three main types of blood vessels: "
        "arteries, veins, and capillaries.\n\n"
        "1. Distinguish between arteries and veins in terms of the direction of blood flow relative to the heart.\n"
        "2. Explain why arteries have thick, muscular, and elastic walls whereas capillaries have walls that are only one cell layer thick.\n"
        "3. State the structural feature inside veins that prevents the backflow of low-pressure blood."
    )
    ans_str = (
        "1. Arteries carry blood away from the heart; veins carry blood towards the heart; "
        "2. Arteries must withstand high blood pressure pumped directly from the ventricles, whereas one-cell-thick capillary walls allow rapid diffusion of oxygen, nutrients, and waste between blood and tissue cells; "
        "3. Valves (semilunar valves inside veins)."
    )
    memo = (
        "1. Arteries: away from heart; Veins: towards heart [1].\n"
        "2. Arteries withstand high pumping pressure [1]; capillaries allow rapid diffusion across a thin barrier [1].\n"
        "3. Valves [1]."
    )
    points = [
        {"point": 1, "desc": "Distinguishes direction: arteries away from heart, veins towards heart"},
        {"point": 2, "desc": "Links artery wall thickness to high pressure and capillary thinness to diffusion"},
        {"point": 3, "desc": "Identifies valves in veins preventing backflow"},
    ]

    return {
        "id": f"ns9_crs_vessels_{seed}",
        "question_id": f"ns9_crs_vessels_{seed}",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 1,
        "topic": TOPIC_NAME,
        "subskill": "blood_vessels_comparison",
        "learning_objective_id": "NS9.T1.CRS.BLOOD_VESSELS",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "Remember: 'A' for Artery = 'A'way from the heart.",
            "tier_2": "Think about blood pressure leaving the ventricles versus substance exchange at the body cells.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["all_arteries_oxygenated_fallacy", "capillary_vs_vein_wall_confusion"],
        "keywords": ["artery", "vein", "capillary", "valves", "diffusion", "blood pressure"],
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def _gen_pulse_rate_investigation(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    r = random.Random(seed)
    rest_bpm = r.choice([68, 70, 72, 74])
    run_bpm = rest_bpm + r.choice([48, 52, 56, 60])

    question_text = (
        f"A Grade 9 learner investigated the effect of strenuous exercise on pulse (heart) rate. "
        f"Her resting heart rate was {rest_bpm} beats per minute (bpm), and immediately after running twice around "
        f"the school field her heart rate was {run_bpm} bpm.\n\n"
        f"1. Identify the independent variable and the dependent variable in this investigation.\n"
        f"2. Calculate the increase in heart rate (in bpm) immediately after exercise.\n"
        f"3. Explain physiologically why the heart rate and breathing rate both increase during strenuous exercise."
    )
    diff = run_bpm - rest_bpm
    ans_str = (
        f"1. Independent variable: Level/duration of physical exercise; Dependent variable: Heart (pulse) rate in bpm; "
        f"2. {run_bpm} - {rest_bpm} = {diff} bpm; "
        f"3. Active muscle cells require a faster rate of cellular respiration to release energy, so the heart pumps faster to deliver more oxygenated blood and glucose to muscles and remove carbon dioxide waste more rapidly."
    )
    memo = (
        f"1. Independent: Exercise / physical activity [1]; Dependent: Heart / pulse rate (bpm) [1].\n"
        f"2. {diff} bpm [1].\n"
        f"3. Muscles require more energy via cellular respiration, needing faster delivery of oxygen and glucose and faster removal of carbon dioxide [1]."
    )
    points = [
        {"point": 1, "desc": "Identifies independent variable (exercise) and dependent variable (pulse rate)"},
        {"point": 2, "desc": f"Calculates increase of {diff} bpm"},
        {"point": 3, "desc": "Links faster circulation to oxygen/glucose delivery for cellular respiration in muscles"},
    ]

    return {
        "id": f"ns9_crs_pulse_{seed}",
        "question_id": f"ns9_crs_pulse_{seed}",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 1,
        "topic": TOPIC_NAME,
        "subskill": "pulse_rate_exercise_investigation",
        "learning_objective_id": "NS9.T1.CRS.EXERCISE_INVESTIGATION",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "The independent variable is what the investigator deliberately changes; the dependent variable is what is measured.",
            "tier_2": "Recall the equation for cellular respiration: Glucose + Oxygen -> Carbon Dioxide + Water + Energy.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["independent_dependent_variable_inversion", "breathing_vs_cellular_respiration_confusion"],
        "keywords": ["pulse", "heart rate", "independent variable", "dependent variable", "cellular respiration"],
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def generate_topic_question(
    seed: int,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
) -> Dict[str, Any]:
    """Generate a single question from the ordered Grade 9 Circulatory & Respiratory subskills."""
    norm_sub = (subskill or "").strip().lower()

    if not norm_sub or norm_sub in ("mixed", "all", "default"):
        # Cycle deterministically through all 6 subskills in sequence starting at index 0 for base seed 1001
        idx = abs(int(seed) - 1001) if int(seed) < 100000 else abs(int(seed))
        norm_sub = ORDERED_SUBSKILLS[idx % len(ORDERED_SUBSKILLS)]

    if norm_sub in ("heart_structure_and_double_circulation", "chambers", "identification_adaptation", "chamber_differentiation"):
        return generate_heart_question(seed=seed, grade=9, mode=mode, subskill="chambers", view=view or "textbook")
    if norm_sub in ("heart_blood_vessel_direction", "vessels", "blood_vessel_direction"):
        return generate_heart_question(seed=seed, grade=9, mode=mode, subskill="vessels", view=view or "flow")
    if norm_sub in ("breathing_mechanics", "breathing"):
        return _gen_breathing_mechanics(seed=seed, mode=mode)
    if norm_sub in ("alveolus_gas_exchange", "alveolus_gaseous_exchange", "alveoli", "gaseous_exchange"):
        return _gen_alveolus_gaseous_exchange(seed=seed, mode=mode)
    if norm_sub in ("blood_vessels_comparison", "blood_vessels"):
        return _gen_blood_vessels_comparison(seed=seed, mode=mode)
    if norm_sub in ("pulse_rate_exercise_investigation", "pulse_rate", "investigation"):
        return _gen_pulse_rate_investigation(seed=seed, mode=mode)

    # Default fallback to heart gross anatomy
    return generate_heart_question(seed=seed, grade=9, mode=mode, subskill="chambers", view=view or "textbook")


def generate(
    seed: Optional[int] = None,
    count: int = 1,
    grade: Any = 9,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """Universal topic generator entry point for Grade 9 Circulatory and Respiratory Systems."""
    base_seed = int(seed) if seed is not None else 1001
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = base_seed * 1000 + i
        if subskill:
            chosen_subskill = subskill
        else:
            # Progress naturally through the topic's ordered subskills
            start_offset = abs(base_seed - 1001) % len(ORDERED_SUBSKILLS)
            chosen_subskill = ORDERED_SUBSKILLS[(start_offset + i) % len(ORDERED_SUBSKILLS)]

        questions.append(
            generate_topic_question(
                seed=sub_seed,
                mode=mode,
                subskill=chosen_subskill,
                view=view,
            )
        )
    return questions
