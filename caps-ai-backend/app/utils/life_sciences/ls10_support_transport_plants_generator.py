"""Life Sciences Grade 10 Term 2: Support and Transport Systems in Plants Generator.

Covers:
- Dicotyledonous leaf transverse cross-section anatomy (3-layer anti-leak diagram plate).
- Transpiration stream forces: Root pressure, capillarity (cohesion & adhesion), and transpiration pull.
- Factors affecting transpiration: Light intensity, temperature, wind, and relative humidity.
- Potometer investigations: Calculation of rate of water uptake, control variables, and validity conditions.
- Wilting versus guttation (hydathodes vs stomatal aperture).

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.plant_physiology_builders import build_plant_leaf_question


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_potometer_experiment(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Experimental investigation into transpiration rate using a potometer."""
    plant = r.choice(["leafy Geranium shoot", "Ligustrum (Privet) twig", "Ficus shoot", "Hibiscus branch"])
    variable = r.choice(["wind speed (using an electric fan)", "ambient temperature (20°C vs 35°C)", "relative humidity (clear plastic bag covering)", "light intensity (darkness vs bright lamp)"])

    # Procedural numbers for bubble movement: distance in mm over time in minutes
    dist_baseline = r.choice([15, 20, 25, 30])
    time_min = 10
    rate_baseline = dist_baseline / time_min

    if "wind" in variable or "temperature" in variable or "light" in variable:
        dist_treatment = dist_baseline + r.choice([15, 20, 25])
        expected_effect = "increases"
    else:  # humidity
        dist_treatment = max(3, dist_baseline - r.choice([8, 10, 12]))
        expected_effect = "decreases"

    rate_treatment = dist_treatment / time_min
    qid = _make_id("ls10_potometer", seed, idx)

    if mode == "elementary_transpiration_forces":
        prompt = (
            "Water moves continuously from the roots through the stem to the leaves in the transpiration stream.\n\n"
            "1. Name the primary upward suction force driving the movement of water through the xylem.\n"
            "2. Define the terms 'cohesion' and 'adhesion' in the context of capillary action inside xylem vessels."
        )
        ans_str = "1. Transpiration pull; 2. Cohesion = attraction between water molecules; Adhesion = attraction between water molecules and xylem walls."
        memo = (
            "1. Primary suction force: Transpiration pull (negative suction pressure created by evaporation). [1]\n"
            "2. Definitions [2]:\n"
            "   - Cohesion: Intermolecular attractive force between polar water molecules forming an unbroken water column. [1]\n"
            "   - Adhesion: Attractive force between water molecules and the hydrophilic cellulose/lignin walls of xylem vessels. [1]"
        )
        hints = {
            "tier_1": "Think about what happens at the leaf surface when water evaporates.",
            "tier_2": "Cohesion is water-to-water; adhesion is water-to-xylem vessel wall. Transpiration pull is the suction force.",
            "tier_3": "1. Transpiration pull. 2. Cohesion = water-water attraction; Adhesion = water-xylem wall attraction.",
        }
        marks = 3
        misconceptions = ["confused_cohesion_with_adhesion", "confused_transpiration_pull_with_root_pressure"]
    else:
        # Full compound potometer question
        prompt = (
            f"Life Sciences learners set up a bubble potometer using a freshly cut {plant} to investigate the effect of "
            f"**{variable}** on the rate of transpiration.\n\n"
            f"- Under baseline laboratory conditions, the air bubble moved ${_fmt_sa(dist_baseline)}\\text{{ mm}}$ in ${time_min}\\text{{ minutes}}$.\n"
            f"- Under the experimental condition ({variable}), the air bubble moved ${_fmt_sa(dist_treatment)}\\text{{ mm}}$ in ${time_min}\\text{{ minutes}}$.\n\n"
            f"1. Identify the independent and dependent variables in this investigation.\n"
            f"2. Calculate the rate of water uptake (in $\\text{{mm/min}}$) under experimental conditions.\n"
            f"3. Explain why the shoot had to be cut and attached to the potometer apparatus under water.\n"
            f"4. State TWO structural features of leaves that minimize transpirational water loss in arid environments."
        )
        ans_str = (
            f"1. Independent: {variable}; Dependent: Rate of transpiration (bubble movement distance in mm/min); "
            f"2. {_fmt_sa(rate_treatment)} mm/min; "
            f"3. Prevents air bubbles from entering xylem vessels and breaking the cohesive water column; "
            f"4. Thick waxy cuticle, sunken stomata, trichomes (hairs), reduced leaf surface area."
        )
        memo = (
            f"1. Variables [2]:\n"
            f"   - Independent variable: {variable} [1]\n"
            f"   - Dependent variable: Rate of water uptake / transpiration (distance moved by bubble per unit time) [1]\n"
            f"2. Rate calculation [2]:\n"
            f"   $$\\text{{Rate}} = \\frac{{{dist_treatment}\\text{{ mm}}}}{{{time_min}\\text{{ min}}}} = {_fmt_sa(rate_treatment)}\\text{{ mm/min}}$$ [2]\n"
            f"3. Reason for cutting under water [2]: Cutting the shoot under water prevents air from being sucked into the cut xylem vessels [1], "
            f"which would break the continuous cohesive water column (cavitation/embolism) [1].\n"
            f"4. Adaptations (any 2) [2]: Thick waxy cuticle, sunken stomata, rolled leaves, leaf spines/reduced surface area, epidermal hairs."
        )
        hints = {
            "tier_1": "Independent variable is what the investigator manipulates; dependent is what is measured. Rate is distance divided by time.",
            "tier_2": f"Calculate: {dist_treatment} mm / {time_min} min = {rate_treatment} mm/min. Air in xylem stops transpiration pull.",
            "tier_3": f"1. Indep: {variable}; Dep: rate of transpiration. 2. {rate_treatment} mm/min. 3. Prevents air bubbles entering xylem. 4. Thick cuticle, sunken stomata.",
        }
        marks = 8
        misconceptions = ["independent_dependent_inversion", "potometer_measures_transpiration_directly_error", "omitted_cavitation_rationale"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "mode": mode,
        "subskill": "potometer",
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Experimental variables identification", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculated rate with correct units", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Apparatus setup rationale (water column integrity)", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Leaf structural adaptations for water conservation", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 10 Support & Transport Systems in Plants."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = (seed + i) if seed is not None else r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("leaf_anatomy", "plant_leaf", "plant_leaf_cross_section", "transpiration_adaptation", "vascular_transport", "stomatal_mechanism"):
            q = build_plant_leaf_question(sub_seed, grade=10, mode=mode, subskill=subskill)
        elif subskill in ("potometer", "transpiration_forces") or mode == "elementary_transpiration_forces":
            q = _generate_potometer_experiment(sub_r, sub_seed, i, mode)
        else:
            # Alternating between leaf diagram builder and potometer investigation
            if (sub_seed + i) % 2 == 0:
                q = build_plant_leaf_question(sub_seed, grade=10, mode=mode)
            else:
                q = _generate_potometer_experiment(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
