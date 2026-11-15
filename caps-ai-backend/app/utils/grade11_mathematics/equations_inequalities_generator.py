"""Grade 11 Mathematics — Equations and Inequalities (Deterministic 6-Pillar Generator).
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference curriculum: curriculum_docs_auto/Mathematics_Gr11/Term 1/02. Equations and inequalities.md

Subskills:
  01–25: Quadratic equations by factorisation (monic, common factor, difference of squares, non-monic prime/composite a,
         expand first, algebraic fractions with LCD), completing the square (monic even/odd b, surd roots, non-monic,
         identifying term to add), quadratic formula (exact surds, rounded to 2 decimals with comma decimal, negative a,
         discriminant calculation), k-substitution (bracket squared, biquadratic quartic, quartic with non-real roots,
         fraction bracket), and forming quadratic equations (integer, fractional, conjugate surd roots, sum/product, unknown k).
  26–50: Nature of roots (discriminant classification, condition for equal/real/non-real roots, proving real for all k),
         quadratic inequalities (strict/non-strict less/greater than intervals, negative leading coefficient, common factor,
         difference of squares, rearrange first, perfect squares, algebraic fractions), simultaneous equations (line and parabola,
         sum/product hyperbola, difference forms with xy, line and circle, intersection points), and word problems (consecutive
         integers, rectangle perimeter/area, Pythagoras right triangle, speed-distance-time, comprehensive capstone).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.equations_inequalities_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_mathematics.equations_inequalities_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Equations and inequalities"

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
    return ARCHETYPES["50_comprehensive_equations_inequalities_synthesis"](r)


def _legacy_factorisation(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "01_quadratic_factorisation_monic_integers",
        "02_quadratic_factorisation_common_factor",
        "03_quadratic_factorisation_difference_of_squares",
        "04_quadratic_factorisation_non_monic_prime_a",
        "05_quadratic_factorisation_non_monic_composite_a",
    ])
    return ARCHETYPES[sub](r)


def _legacy_completing_square(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "08_completing_the_square_monic_even_b",
        "09_completing_the_square_monic_surd_roots",
        "10_completing_the_square_monic_odd_b",
        "11_completing_the_square_non_monic",
    ])
    return ARCHETYPES[sub](r)


def _legacy_quadratic_formula(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "13_quadratic_formula_exact_surd_roots",
        "14_quadratic_formula_rounded_two_decimals",
        "15_quadratic_formula_negative_leading_coef",
    ])
    return ARCHETYPES[sub](r)


def _legacy_nature_of_roots(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "26_nature_of_roots_classify_from_equation",
        "27_nature_of_roots_condition_for_equal_roots",
        "28_nature_of_roots_condition_for_real_roots",
        "29_nature_of_roots_condition_for_nonreal_roots",
    ])
    return ARCHETYPES[sub](r)


def _legacy_quadratic_inequalities(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "31_quadratic_inequality_standard_less_than",
        "32_quadratic_inequality_standard_greater_than",
        "33_quadratic_inequality_non_strict_interval",
        "34_quadratic_inequality_non_strict_disjoint",
    ])
    return ARCHETYPES[sub](r)


def _legacy_simultaneous(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "41_simultaneous_linear_quadratic_substitution_parabola",
        "42_simultaneous_linear_quadratic_hyperbola_product",
        "44_simultaneous_linear_quadratic_circle_intersection",
    ])
    return ARCHETYPES[sub](r)


LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "mixed": _legacy_compound,
    "equations_inequalities": _legacy_compound,
    "quadratic_factorisation": _legacy_factorisation,
    "completing_the_square": _legacy_completing_square,
    "quadratic_formula": _legacy_quadratic_formula,
    "nature_of_roots": _legacy_nature_of_roots,
    "quadratic_inequalities": _legacy_quadratic_inequalities,
    "simultaneous_equations": _legacy_simultaneous,
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


def generate_grade11_equations_inequalities_question(
    *,
    subskill: str = "equations_inequalities",
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
