"""Natural Sciences Grade 7 Term 2: Separating Mixtures Generator.

Covers:
- Physical separation techniques: Simple distillation, filtration, evaporation, paper chromatography, and separating funnels.
- Simple distillation apparatus: Round-bottom flask, Liebig condenser (counter-current cooling water flow), thermometer, receiving flask.
- Chromatography: Stationary phase (filter paper), mobile phase (solvent), and Rf (retention factor) calculations.
- Practical applications: Desalination of seawater, crude oil fractional distillation, and wastewater treatment.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "apparatus_identification",
    "thermal_separation_principle",
    "cooling_water_flow",
    "elementary_rf_calc",
    "chromatography_separation"
]

from app.utils.natural_sciences.natural_sciences_builders import build_distillation_apparatus_question


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_chromatography_and_separation(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Paper chromatography and separation of complex mixtures."""
    mixture_type = r.choice(["black ink marker pigment", "chlorophyll plant extract", "food dye coloring"])
    solvent = r.choice(["water", "ethanol", "acetone"])
    qid = _make_id("ns7_chromatography", seed, idx)

    # Procedural distances in mm: solvent front and dye spots
    dist_solvent = r.choice([50, 60, 80, 100])
    dist_spot_a = int(dist_solvent * r.choice([0.25, 0.30, 0.40]))
    dist_spot_b = int(dist_solvent * r.choice([0.60, 0.70, 0.80]))
    rf_a = dist_spot_a / dist_solvent
    rf_b = dist_spot_b / dist_solvent

    if mode == "elementary_rf_calc":
        prompt = (
            f"A paper chromatography experiment was conducted to separate pigments in a {mixture_type} using {solvent}.\n"
            f"- Distance travelled by solvent front: ${dist_solvent}\\text{{ mm}}$\n"
            f"- Distance travelled by Pigment A: ${dist_spot_a}\\text{{ mm}}$\n\n"
            f"Calculate the retention factor ($R_f$ value) of Pigment A using the formula:\n"
            f"\\[ R_f = \\frac{{\\text{{distance moved by solute}}}}{{\\text{{distance moved by solvent front}}}} \\]"
        )
        ans_str = f"Rf = {_fmt_sa(rf_a, 2)}"
        memo = (
            f"1. Formula: $R_f = \\frac{{\\text{{distance moved by solute}}}}{{\\text{{distance moved by solvent front}}}}$ [M]\n"
            f"2. Substitution: $R_f = \\frac{{{dist_spot_a}}}{{{dist_solvent}}} = {_fmt_sa(rf_a, 2)}$ [A]"
        )
        hints = {
            "tier_1": "Divide the distance moved by the dye spot by the distance moved by the solvent front.",
            "tier_2": f"Calculate: {dist_spot_a} / {dist_solvent} = {rf_a:.2f}.",
            "tier_3": f"Rf = {_fmt_sa(rf_a, 2)}.",
        }
        marks = 2
        misconceptions = ["rf_inverted_ratio", "omitted_formula_substitution"]
    else:
        # Full compound question: Chromatography + Distillation + Immiscible liquids
        prompt = (
            f"Grade 7 learners investigated methods to separate different mixtures in the science laboratory.\n\n"
            f"1. A paper chromatography strip of {mixture_type} showed two distinct spots: Spot A moved ${dist_spot_a}\\text{{ mm}}$ "
            f"and Spot B moved ${dist_spot_b}\\text{{ mm}}$ while the solvent front moved ${dist_solvent}\\text{{ mm}}$.\n"
            f"   Calculate the $R_f$ value of Spot B.\n"
            f"2. Explain why Spot B travelled further up the chromatography paper than Spot A.\n"
            f"3. Name the most suitable physical separation technique to separate:\n"
            f"   a) Cooking oil and water.\n"
            f"   b) Pure drinking water from salty sea water.\n"
            f"   c) Sand and copper sulphate solution."
        )
        ans_str = (
            f"1. Rf = {_fmt_sa(rf_b, 2)}; "
            f"2. Spot B is more soluble in the mobile solvent phase and has weaker attraction (adhesion) to the stationary paper phase; "
            f"3. a) Separating funnel; b) Simple distillation; c) Filtration."
        )
        memo = (
            f"1. Rf calculation for Spot B [2]:\n"
            f"   $$R_f = \\frac{{{dist_spot_b}\\text{{ mm}}}}{{{dist_solvent}\\text{{ mm}}}} = {_fmt_sa(rf_b, 2)}$$ [2]\n"
            f"2. Solubility and affinity explanation [2]: Pigment B moved further because it is more soluble in the mobile solvent phase [1] "
            f"and has less affinity/adhesion to the cellulose fibres of the stationary paper phase compared to Pigment A [1].\n"
            f"3. Separation methods [3]:\n"
            f"   a) Cooking oil and water: **Separating funnel** (immiscible liquids with different densities) [1].\n"
            f"   b) Pure water from sea water: **Simple distillation** [1].\n"
            f"   c) Sand from copper sulphate: **Filtration** [1]."
        )
        hints = {
            "tier_1": "Rf is spot distance divided by solvent distance. More soluble dyes travel further.",
            "tier_2": f"Rf = {dist_spot_b} / {dist_solvent} = {rf_b:.2f}. Oil and water don't mix (use a separating funnel). Salt water needs distillation to collect pure water.",
            "tier_3": f"1. Rf = {_fmt_sa(rf_b, 2)}. 2. Greater solubility in solvent. 3. a) Separating funnel, b) Distillation, c) Filtration.",
        }
        marks = 7
        misconceptions = ["confused_filtration_with_distillation", "separating_funnel_density_confusion"]

    return {
        "id": qid,
        "question_id": qid,
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
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
                {"id": "mp_1", "desc": "Rf value calculation and substitution", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Chromatography differential solubility mechanism", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct matching of physical separation techniques", "marks": 3, "editable": True},
            ],
            "deductions": [],
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
    """Master entry point for Grade 7 Separating Mixtures."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []
    raw_grade = str(kwargs.get("grade", 7)).replace("grade_", "").replace("g", "").strip()
    gr_int = int(raw_grade) if raw_grade.isdigit() else 7

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("apparatus_identification", "thermal_separation_principle", "cooling_water_flow", "distillation", "distillation_apparatus"):
            q = build_distillation_apparatus_question(sub_seed, grade=gr_int, mode=mode, subskill=subskill)
        elif subskill in ("elementary_rf_calc", "rf_calculation") or mode == "elementary_rf_calc":
            q = _generate_chromatography_and_separation(sub_r, sub_seed, i, mode="elementary_rf_calc")
        elif subskill in ("chromatography", "chromatography_separation"):
            q = _generate_chromatography_and_separation(sub_r, sub_seed, i, mode="compound")
        else:
            # Deterministic subskill cycling between distillation apparatus diagram and chromatography/separation
            if (sub_seed + i) % 2 == 0:
                q = build_distillation_apparatus_question(sub_seed, grade=gr_int, mode=mode)
            else:
                q = _generate_chromatography_and_separation(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
