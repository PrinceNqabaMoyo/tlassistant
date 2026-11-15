"""Grade 10 Mathematics — Term 1 — Equations and Inequalities Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr10/Term 1/04. Equations and inequalities.md
Focus: Linear equations, quadratic equations, simultaneous equations, word problems, literal equations, linear inequalities.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .equations_inequalities_archetypes_01_25 import BUILDERS_01_25
from .equations_inequalities_archetypes_26_50 import BUILDERS_26_50

TOPIC = "grade10_math_equations_inequalities"
LO = "math10_equations_inequalities"

ALL_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS = list(ALL_BUILDERS.keys())
ARCHETYPES = SUBSKILLS
BUILDERS = ALL_BUILDERS

# Legacy alias mappings for backwards compatibility
LEGACY_MAP: Dict[str, str] = {
    "linear_equations": "03_linear_two_step_ax_plus_b_equals_c",
    "quadratic_by_factorising": "17_quadratic_trinomial_monic_positive_constant",
    "quadratic_restrictions": "24_quadratic_extraneous_root_restriction_elimination",
    "simultaneous_substitution": "25_simultaneous_linear_substitution_direct_variable",
    "simultaneous_elimination": "27_simultaneous_linear_elimination_direct_addition",
    "word_problems": "33_word_problem_sum_and_difference_two_numbers",
    "literal_equations": "39_literal_equation_linear_isolate_single_term",
    "linear_inequalities": "45_linear_inequality_one_step_positive_coeff",
    "concepts": "01_linear_one_step_addition_subtraction",
    "calculation": "03_linear_two_step_ax_plus_b_equals_c",
    "calculations": "03_linear_two_step_ax_plus_b_equals_c",
    "equations": "03_linear_two_step_ax_plus_b_equals_c",
    "inequalities": "45_linear_inequality_one_step_positive_coeff",
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    base_seed = int(seed) if seed is not None else 42
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, int(count))):
        cur_seed = base_seed * 1000 + i if seed is not None else None
        rng = random.Random(cur_seed)

        resolved_subskill = subskill
        if resolved_subskill in LEGACY_MAP:
            resolved_subskill = LEGACY_MAP[resolved_subskill]

        if not resolved_subskill or resolved_subskill in ("mixed", "all", "default"):
            resolved_subskill = rng.choice(SUBSKILLS)
        elif resolved_subskill not in ALL_BUILDERS:
            # Fallback search
            matches = [s for s in SUBSKILLS if resolved_subskill in s]
            resolved_subskill = matches[0] if matches else rng.choice(SUBSKILLS)

        builder = ALL_BUILDERS[resolved_subskill]
        q = builder(rng)
        if seed is not None:
            q["id"] = f"{TOPIC}_{resolved_subskill}_{base_seed}_{i}"
        questions.append(q)

    return {"questions": questions}


generate_question = generate
