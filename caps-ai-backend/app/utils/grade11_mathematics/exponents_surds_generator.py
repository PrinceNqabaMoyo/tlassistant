"""Grade 11 Mathematics — Exponents and Surds (Deterministic 6-Pillar Generator).
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference curriculum: curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Exponents and surds.md

Subskills:
  01–25: Number classifications, exponent laws (product, quotient, power-of-power, negative exponents,
         composite-to-prime base factorisation), exponential factorisation (common factors, difference of squares,
         trinomials), rational exponents, and surd simplification (radical form, operations, rationalisation).
  26–50: Exponential equations (equal bases, prime base reductions, fractional powers, common factors, k-substitution),
         surd equations (isolated, linear RHS, extraneous roots, k-substitution, quadratic radicand, two radicals),
         nature of roots & real number conditions, exponential applications (population growth, decay, half-life, doubling).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.exponents_surds_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_mathematics.exponents_surds_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Exponents and surds"

# Combine all 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS = list(SUBSKILLS)
AVAILABLE_SUBSKILLS = list(SUBSKILLS)


# Backward-compatible legacy builder shims
def _legacy_compound(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["50_comprehensive_exponents_surds_synthesis"](r)


def _legacy_exponent_laws(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "04_exponent_laws_product_quotient_numerical",
        "05_exponent_laws_power_of_power_negative",
        "06_simplify_exponential_fraction_monomial",
    ])
    return ARCHETYPES[sub](r)


def _legacy_rational_exponent_to_radical(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "11_rational_exponent_to_radical_form",
        "12_radical_to_rational_exponent_form",
        "13_evaluate_numerical_fractional_exponent",
    ])
    return ARCHETYPES[sub](r)


def _legacy_simplify_surd(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "15_simplify_single_surd_prime_factorisation",
        "16_add_subtract_like_surds",
        "17_add_subtract_higher_coefficient_surds",
        "18_multiply_monomial_surds",
    ])
    return ARCHETYPES[sub](r)


def _legacy_rationalise_denominator(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "22_rationalise_monomial_denominator",
        "23_rationalise_binomial_denominator_sum",
        "24_rationalise_binomial_denominator_diff",
        "25_rationalise_two_term_surd_expression_sum",
    ])
    return ARCHETYPES[sub](r)


def _legacy_exponential_application(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "45_exponential_growth_compound_formula",
        "46_exponential_decay_depreciation_model",
        "47_exponential_half_life_decay",
        "48_exponential_bacterial_doubling_model",
    ])
    return ARCHETYPES[sub](r)


LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "exponents_surds": _legacy_compound,
    "mixed": _legacy_compound,
    "exponent_laws": _legacy_exponent_laws,
    "rational_exponent_to_radical": _legacy_rational_exponent_to_radical,
    "simplify_surd": _legacy_simplify_surd,
    "rationalise_denominator": _legacy_rationalise_denominator,
    "exponential_application": _legacy_exponential_application,
}

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
    **LEGACY_BUILDERS,
}


def get_subskills() -> List[str]:
    """Return the list of all 50 semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic question for a subskill."""
    r = random.Random(seed if seed is not None else 42)
    target = subskill or r.choice(SUBSKILLS)

    builder = BUILDERS.get(target)
    if not builder:
        builder = ARCHETYPES.get(r.choice(SUBSKILLS))

    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)

    if seed is not None:
        q["seed"] = seed
    return q


def generate_grade11_exponents_surds_question(
    *,
    subskill: str = "exponents_surds",
    difficulty: str = "medium",
    question_type: str = "typed",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Direct backwards compatibility wrapper returning single question dict."""
    return generate_question(subskill=subskill, seed=seed, difficulty=difficulty, **kwargs)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Primary generator interface required by central generator registry and validation suite."""
    base_seed = 42 if seed is None else int(seed)
    chosen_target = subskill or mode

    questions = []
    for i in range(max(1, count)):
        curr_seed = base_seed * 1000 + i
        r = random.Random(curr_seed)

        target = chosen_target
        if not target or target not in BUILDERS:
            target = SUBSKILLS[i % len(SUBSKILLS)]

        builder = BUILDERS.get(target)
        if not builder:
            builder = ARCHETYPES.get(SUBSKILLS[0])

        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)

        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}
