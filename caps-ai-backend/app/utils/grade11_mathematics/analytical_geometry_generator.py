"""Grade 11 Mathematics — Analytical Geometry.
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 2).

Subskills:
  01–25: Distance formula (lengths, missing coordinates, equilateral/isosceles classification),
         Midpoint formula (midpoints, endpoints, collinearity),
         Gradient formula (slopes, horizontal/vertical lines, parallel lines, perpendicular lines, collinear points),
         Equation of straight line (gradient-point, two-point, intercepts),
         Angle of inclination (acute, obtuse, between two lines),
         Triangle properties (right-angled, isosceles, median, altitude).
  26–50: Perpendicular bisectors,
         Quadrilateral coordinate proofs & properties (parallelogram diagonals & 4th vertex,
         rhombus perpendicular diagonals & equal sides, rectangle equal diagonals & right angles, square, trapezium, kite),
         Coordinate areas (triangles, parallelograms),
         Points of intersection, axis intercepts, distance from origin,
         Midpoint theorem coordinate verification, centroid, reflections across axes and y=x,
         and comprehensive multi-step analytical quadrilateral analysis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.analytical_geometry_archetypes_01_25 import (
    ARCHETYPES_01_25,
)
from app.utils.grade11_mathematics.analytical_geometry_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "Analytical geometry"
TOPIC_ID = "grade11_math_analytical_geometry"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS = list(SUBSKILLS)
AVAILABLE_SUBSKILLS = list(SUBSKILLS)

# Backward-compatible legacy builder shims
LEGACY_BUILDERS: Dict[str, Any] = {
    "distance_between_points": ARCHETYPES.get("01_distance_between_two_points_direct", next(iter(ARCHETYPES.values()))),
    "midpoint": ARCHETYPES.get("03_midpoint_of_line_segment", next(iter(ARCHETYPES.values()))),
    "gradient_two_points": ARCHETYPES.get("05_gradient_between_two_points", next(iter(ARCHETYPES.values()))),
    "equation_line_two_points": ARCHETYPES.get("13_equation_straight_line_two_points", next(iter(ARCHETYPES.values()))),
    "parallel_or_perpendicular": ARCHETYPES.get("15_equation_perpendicular_line_through_point", next(iter(ARCHETYPES.values()))),
    "compound": ARCHETYPES.get("01_distance_between_two_points_direct", next(iter(ARCHETYPES.values()))),
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


def generate_questions(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Legacy helper returning a flat list of questions for backward compatibility."""
    res = generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, **kwargs)
    return res.get("questions", [])
