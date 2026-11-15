"""Grade 11 Mathematics — Functions and Graphs.
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).

Subskills:
  01–25: Parabola (vertex & standard form, turning points, axis of symmetry, intercepts, domain, range,
         finding equations with inline_svg) and Hyperbola (asymptotes, axes of symmetry, intercepts,
         finding equations with inline_svg).
  26–50: Exponential functions (asymptotes, intercepts, domain, range, growth vs decay, finding equations with inline_svg),
         Trigonometric graphs (amplitude, period, range, vertical shift, phase shift, finding equations with inline_svg),
         and Advanced Graph Interpretations (f(x) > 0, f(x).g(x) <= 0, f(x) >= g(x), vertical lengths, max distances).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.functions_graphs_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade11_mathematics.functions_graphs_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "Functions and graphs"
TOPIC_ID = "grade11_math_functions"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS = list(SUBSKILLS)
AVAILABLE_SUBSKILLS = list(SUBSKILLS)

# Backward-compatible legacy builder shims
def _legacy_hyperbola(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["20_hyperbola_equation_from_asymptotes_and_point"](r)

def _legacy_parabola(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["07_parabola_equation_from_turning_point_and_point"](r)

def _legacy_exponential(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["30_exponential_equation_from_asymptote_and_point"](r)

LEGACY_BUILDERS: Dict[str, Any] = {
    "hyperbola_features": _legacy_hyperbola,
    "parabola_features": _legacy_parabola,
    "exponential_features": _legacy_exponential,
    "compound": _legacy_parabola,
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
        builder = ARCHETYPES.get(r.choice(SUBSKILLS))

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
