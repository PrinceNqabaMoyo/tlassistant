"""Grade 11 Mathematics — Trigonometric Reductions, Identities & General Solutions.
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1 & 2).

Subskills:
  01–25: Quadrant identification, reductions (180°±θ, 360°-θ, negative angles, 90°±θ co-ratios),
         special angles (0°, 30°, 45°, 60°, 90°, quadrantal), numerical reductions, Cartesian terminal arms.
  26–50: Quotient and square identities, proving identities, general solutions, specific interval solutions,
         2D Area Rule, Sine Rule, Cosine Rule with inline_svg diagrams.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.trigonometry_reductions_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade11_mathematics.trigonometry_reductions_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "Trigonometry"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS = list(SUBSKILLS)
AVAILABLE_SUBSKILLS = list(SUBSKILLS)

# Backward-compatible legacy builder shims
def _legacy_compound(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["29_compound_algebraic_reduction_fraction"](r)

def _legacy_elementary_quadrant(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "02_reduction_quadrant_2_sin",
        "03_reduction_quadrant_2_cos",
        "05_reduction_quadrant_3_sin",
        "06_reduction_quadrant_3_cos",
        "08_reduction_quadrant_4_sin",
        "09_reduction_quadrant_4_cos",
    ])
    return ARCHETYPES[sub](r)

def _legacy_elementary_gensol(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "34_general_solution_sin_basic",
        "35_general_solution_cos_basic",
        "36_general_solution_tan_basic",
    ])
    return ARCHETYPES[sub](r)

LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "elementary_reduction_quadrant": _legacy_elementary_quadrant,
    "elementary_general_solution": _legacy_elementary_gensol,
    "trigonometric_reduction_compound": _legacy_compound,
}

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
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

    builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
    if not builder:
        # Fallback to random archetype if unrecognized
        builder = ARCHETYPES.get(r.choice(SUBSKILLS))

    # Builders in 01_25 and 26_50 accept (r)
    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)

    if seed is not None:
        q["seed"] = seed
    return q


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

        builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
        if not builder:
            builder = ARCHETYPES.get(SUBSKILLS[0])

        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)

        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}
