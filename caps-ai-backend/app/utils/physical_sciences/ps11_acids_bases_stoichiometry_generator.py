"""Physical Sciences Grade 11 & 12 — Acids, Bases & Titration Stoichiometry Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/03. Types of reaction.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/04. Quantitative aspects of chemical change.md
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/03. Acids and bases.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=3 (Gr 11) / term=2 (Gr 12), caps_weight_percent=20, suggested_duration_mins=8.
2. Deconstructible compound questions & atomic sub-drills.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.physical_sciences_builders import build_titration_apparatus_question

TOPIC = "grade11_acids_bases_stoichiometry"

TITRATION_PAIRS = [
    {
        "acid_name": "Hydrochloric acid",
        "acid_formula": "\\text{HCl}",
        "base_name": "Sodium hydroxide",
        "base_formula": "\\text{NaOH}",
        "salt_name": "Sodium chloride (NaCl)",
        "salt_nature": "neutral",
        "indicator": "Bromothymol blue",
        "indicator_color": "green",
        "na": 1,
        "nb": 1,
        "molar_mass_base": 40.0,
    },
    {
        "acid_name": "Sulphuric acid",
        "acid_formula": "\\text{H}_2\\text{SO}_4",
        "base_name": "Sodium hydroxide",
        "base_formula": "\\text{NaOH}",
        "salt_name": "Sodium sulphate (Na2SO4)",
        "salt_nature": "neutral",
        "indicator": "Bromothymol blue",
        "indicator_color": "green",
        "na": 1,
        "nb": 2,
        "molar_mass_base": 40.0,
    },
    {
        "acid_name": "Oxalic acid (ethanedioic acid)",
        "acid_formula": "(\\text{COOH})_2",
        "base_name": "Sodium hydroxide",
        "base_formula": "\\text{NaOH}",
        "salt_name": "Sodium oxalate",
        "salt_nature": "basic (alkaline)",
        "indicator": "Phenolphthalein",
        "indicator_color": "pale pink",
        "na": 1,
        "nb": 2,
        "molar_mass_base": 40.0,
    },
    {
        "acid_name": "Hydrochloric acid",
        "acid_formula": "\\text{HCl}",
        "base_name": "Sodium carbonate",
        "base_formula": "\\text{Na}_2\\text{CO}_3",
        "salt_name": "Sodium chloride (NaCl)",
        "salt_nature": "acidic/neutral",
        "indicator": "Methyl orange",
        "indicator_color": "orange",
        "na": 2,
        "nb": 1,
        "molar_mass_base": 106.0,
    },
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_titration_calculation_question(
    r: random.Random, seed: Optional[int], idx: int, mode: str, grade: int
) -> Dict[str, Any]:
    """Quantitative acid-base titration calculation: (ca * Va) / (cb * Vb) = na / nb."""
    qid = _make_id(f"titration{grade}_calc", seed, idx)
    pair = r.choice(TITRATION_PAIRS)

    va_cm3 = r.choice([20.0, 22.5, 24.0, 25.0, 28.0])
    vb_cm3 = r.choice([25.0, 20.0])
    ca = r.choice([0.10, 0.12, 0.15, 0.20, 0.25])

    na = pair["na"]
    nb = pair["nb"]

    # cb = (ca * va * nb) / (vb * na)
    cb = (ca * va_cm3 * nb) / (vb_cm3 * na)

    prompt = (
        f"In a volumetric titration experiment to determine the concentration of a {pair['base_name']} ({pair['base_formula']}) solution, "
        f"a learner titrates exactly {_fmt_sa(vb_cm3)} cm³ of the base solution in an Erlenmeyer flask with a standard "
        f"{pair['acid_name']} ({pair['acid_formula']}) solution of concentration {_fmt_sa(ca)} mol·dm⁻³ from a burette.\n"
        f"An average volume of {_fmt_sa(va_cm3)} cm³ of acid is required to reach the equivalence endpoint.\n\n"
        f"1. Define a *standard solution*.\n"
        f"2. State suitable indicator for this titration and describe the distinct color change at the endpoint.\n"
        f"3. Calculate the concentration of the {pair['base_name']} solution in mol·dm⁻³.\n"
        f"4. State the function of the white tile placed beneath the conical flask."
    )
    ans_str = (
        f"1. A solution of known concentration; "
        f"2. Indicator: {pair['indicator']} (turns {pair['indicator_color']} at endpoint); "
        f"3. cb = {_fmt_sa(cb, 3)} mol/dm3; "
        f"4. Provides a white neutral contrast background to clearly observe the sharp color transition."
    )
    memo = (
        f"1. Standard solution definition [2]: A solution of precisely known concentration. [2]\n"
        f"2. Indicator selection [2]: {pair['indicator']} [1]; Endpoint color change: transitions to {pair['indicator_color']} at equivalence. [1]\n"
        f"3. Titration concentration calculation [3]:\n"
        f"   $$\\frac{{c_a \\cdot V_a}}{{c_b \\cdot V_b}} = \\frac{{n_a}}{{n_b}}$$ [1M]\n"
        f"   $$\\frac{{({_fmt_sa(ca)})({_fmt_sa(va_cm3)})}}{{c_b \\cdot ({_fmt_sa(vb_cm3)})}} = \\frac{{{na}}}{{{nb}}}$$ [1M]\n"
        f"   $$c_b = \\frac{{({_fmt_sa(ca)})({_fmt_sa(va_cm3)}) \\times {nb}}}{{({_fmt_sa(vb_cm3)}) \\times {na}}} = {_fmt_sa(cb, 3)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$ [1A]\n"
        f"4. White tile function [1]: Provides a neutral, high-contrast reflective surface to detect the exact dropwise color change. [1]"
    )
    hints = {
        "tier_1": "Use the mole ratio equation (ca * Va) / (cb * Vb) = na / nb.",
        "tier_2": f"Here na = {na} and nb = {nb}. Solve for cb: cb = (ca * Va * nb) / (Vb * na).",
        "tier_3": f"cb = {_fmt_sa(cb, 3)} mol·dm⁻³.",
    }
    term = 3 if grade == 11 else 2
    return {
        "id": qid,
        "question_id": qid,
        "term": term,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 8,
        "hints": hints,
        "misconception_tags": ["stoichiometric_ratio_inversion", "titration_formula_volume_unit_error"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Standard solution definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Indicator selection and color change", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Stoichiometric formula, substitution and answer", "marks": 3, "editable": True},
                {"id": "mp_4", "desc": "White tile function", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "11",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 11 & 12 Acids, Bases & Titrations."""
    r = random.Random(seed)
    questions = []
    gr_int = 12 if str(grade).strip() == "12" else 11

    for i in range(count):
        sub_seed = (seed + i * 41) if seed is not None else random.randint(1000, 99999)

        if mode == "scaffold" or subskill in ("titration_apparatus_diagram", "titration_apparatus"):
            q = build_titration_apparatus_question(seed=sub_seed, grade=gr_int, mode=mode)
        elif mode == "elementary_titration_stoichiometry":
            q = _generate_titration_calculation_question(r, sub_seed, i, mode, gr_int)
        else:
            # Deterministic subskill cycling between visual apparatus inspection and quantitative titration
            if (sub_seed + i) % 2 == 0:
                q = build_titration_apparatus_question(seed=sub_seed, grade=gr_int, mode=mode)
            else:
                q = _generate_titration_calculation_question(r, sub_seed, i, mode, gr_int)

        questions.append(q)

    return questions
