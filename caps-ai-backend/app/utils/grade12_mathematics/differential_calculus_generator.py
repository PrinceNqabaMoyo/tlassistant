"""Grade 12 Mathematics - Differential Calculus Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/04. Differential calculus.md.

Covers:
  - Intuitive limits, indeterminate forms (0/0) via factorisation and rationalisation.
  - Average gradient (secant line) and average rate of change over intervals.
  - Differentiation from first principles: linear, quadratic, hyperbolic, and cubic.
  - Rules of differentiation: power rule, negative/fractional exponents, surds, expansions, rational splitting.
  - Tangents and normals: gradient of tangent, equation of tangent, parallel and perpendicular tangents.
  - Second derivatives, concavity tests, and points of inflection.
  - Cubic functions: stationary turning points, classification via second derivative test, intervals of increase/decrease.
  - Cubic curve sketching, determining cubic equations from intercepts and turning points.
  - Interpretation of graphs: sign of derivative, f(x)*f'(x) > 0, connections between f and f'.
  - Number of real roots of f(x) = k from local extrema.
  - Rates of change and kinematics (displacement, velocity, acceleration, projectile maximum height).
  - Applied optimisation: maximum area, box volume, cylindrical containers.

Strictly zero-LLM, deterministic execution with 50 distinct semantic archetypes.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .differential_calculus_archetypes_01_25 import BUILDERS_01_25, SUBSKILLS_01_25
from .differential_calculus_archetypes_26_50 import BUILDERS_26_50, SUBSKILLS_26_50

ALL_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
ALL_BUILDERS.update(BUILDERS_01_25)
ALL_BUILDERS.update(BUILDERS_26_50)

ORDERED_SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())

SUBSKILLS: Dict[str, str] = {}
SUBSKILLS.update(SUBSKILLS_01_25)
SUBSKILLS.update(SUBSKILLS_26_50)

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_compound_nsc_exam_differential_calculus",
    "compound_first_principles": "08_first_principles_general_quadratic",
    "first_principles": "08_first_principles_general_quadratic",
    "first_principles_differentiation": "08_first_principles_general_quadratic",
    "compound_cubic": "30_cubic_stationary_turning_points",
    "cubic_curve_analysis": "30_cubic_stationary_turning_points",
    "elementary_difference_quotient": "04_average_gradient_secant_line",
    "elementary_power_rule": "13_power_rule_polynomial_terms",
    "elementary_tangent_line": "23_equation_of_tangent_line_to_parabola",
    "elementary_first_principles": "08_first_principles_general_quadratic",
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates deterministic Grade 12 Differential Calculus questions."""
    base_seed = 42 if seed is None else int(seed)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        item_seed = base_seed + i * 17
        rng = random.Random(item_seed)

        target = subskill
        if target and target in LEGACY_ALIASES:
            target = LEGACY_ALIASES[target]

        if target and target in ALL_BUILDERS:
            builder = ALL_BUILDERS[target]
        elif mode and mode in LEGACY_ALIASES:
            builder = ALL_BUILDERS[LEGACY_ALIASES[mode]]
        elif mode in ALL_BUILDERS:
            builder = ALL_BUILDERS[mode]
        else:
            chosen_sub = rng.choice(ORDERED_SUBSKILLS)
            builder = ALL_BUILDERS[chosen_sub]

        q = builder(rng)
        q["seed"] = item_seed
        q["term"] = 1
        q["caps_weight_percent"] = 25
        q["suggested_duration_mins"] = 6
        questions.append(q)

    return questions
