"""Grade 12 Technical Mathematics — Polynomials & Cubic Equations (50 Semantic Archetypes).

Grounded strictly in:
curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/02. Polynomials.md (Chapter 5)

Covers 50 distinct semantic archetypes across:
- Definitions, classification, degree/order, leading coefficients, non-polynomial detection
- Polynomial long division, synthetic division
- Remainder Theorem (monic, non-monic, zero remainder, unknown coefficients k & d, simultaneous unknowns)
- Factor Theorem (verifying linear factors, rational root search, finding unknown coefficients)
- Cubic polynomial factorisation (common factor, grouping in pairs, difference of cubes, quadratic factors)
- Solving cubic equations (distinct real rational roots, repeated roots, non-real quadratic factors)
- Exponential substitutions reducible to cubics
- Reconstructing cubic polynomials from given roots
- Graphic interpretations (x-intercepts from cubic graph)
- Technical engineering applications (open-top sheet metal tray, machined hollow pipe, beam deflection, engineering synthesis)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.technical_mathematics.polynomials_archetypes_01_25 import BUILDERS_01_25
from app.utils.technical_mathematics.polynomials_archetypes_26_50 import ARCHETYPES_26_50

TOPIC = "technical_mathematics_polynomials"
LO = "techmath_poly_ch5"

ALL_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS = list(ALL_BUILDERS.keys())
ARCHETYPES = SUBSKILLS
BUILDERS = ALL_BUILDERS

LEGACY_ALIASES: Dict[str, str] = {
    "remainder_theorem": "08_remainder_theorem_linear_monic_positive_root",
    "unknown_coefficient": "12_remainder_theorem_solve_unknown_coefficient_k",
    "factor_theorem": "16_factor_theorem_verify_linear_factor_monic",
    "solve_cubic": "34_solve_cubic_three_distinct_integer_roots_monic",
    "factorise_cubic": "26_factorise_cubic_grouping_four_terms",
    "synthetic_division": "07_polynomial_synthetic_division_monic_divisor",
    "technical_application": "47_technical_cubic_open_top_sheet_metal_tray_volume",
    "elementary_remainder": "08_remainder_theorem_linear_monic_positive_root",
    "elementary_coeff": "12_remainder_theorem_solve_unknown_coefficient_k",
}


def generate(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates deterministic questions for Grade 12 Technical Mathematics Polynomials."""
    base_seed = int(seed) if seed is not None else 42
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, int(count))):
        cur_seed = base_seed * 1000 + i if seed is not None else None
        rng = random.Random(cur_seed)

        resolved_subskill = subskill
        if resolved_subskill in LEGACY_ALIASES:
            resolved_subskill = LEGACY_ALIASES[resolved_subskill]

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

    return questions


generate_question = generate
