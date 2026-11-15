"""Grade 10 Mathematics — Term 2 — Functions (50-Archetype Deterministic Generator).

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Functions syllabus.
Implements the 6-pillar universal generator contract:
  1. Term & Calendar Metadata (term=2, caps_weight_percent=15, duration=8)
  2. 50 Semantic Archetypes (01_... to 50_..., 0 synthetic shims)
  3. Standardized Misconception Taxonomy
  4. Teacher-Editable Marking Schema
  5. Deterministic 3-Tier Pre-baked Hints (Zero-LLM)
  6. Modality-Appropriate Representation (KaTeX, South African comma decimals)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .functions_archetypes_01_25 import BUILDERS_01_25
from .functions_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade10_math_functions"
LEARNING_OBJECTIVE = "math10_functions"
TERM = 2
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 8

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
VALID_SUBSKILLS: List[str] = list(SUBSKILLS)
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)

_LEGACY_ALIASES: Dict[str, List[str]] = {
    "function_notation_eval": [
        "03_function_notation_eval_linear_integer",
        "04_function_notation_eval_linear_fraction",
        "05_function_notation_eval_quadratic",
        "06_function_notation_eval_hyperbola",
        "07_function_notation_eval_exponential",
    ],
    "function_notation_solve": [
        "08_function_notation_solve_linear_input",
        "09_function_notation_solve_quadratic_input",
        "10_function_notation_solve_hyperbola_input",
        "11_function_notation_solve_exponential_input",
    ],
    "domain_range": [
        "18_linear_domain_and_range_intervals",
        "23_quadratic_domain_and_range",
        "29_hyperbola_domain_and_range",
        "35_exponential_domain_and_range",
    ],
    "representation_convert": [
        "01_concept_function_definition_and_relation_test",
        "02_dependent_vs_independent_variable_identification",
    ],
    "linear_gradient_intercept": [
        "12_linear_gradient_and_direction",
        "13_linear_dual_intercepts",
    ],
    "linear_intercepts": [
        "13_linear_dual_intercepts",
    ],
    "linear_find_equation": [
        "14_linear_equation_from_two_points",
        "15_linear_equation_from_gradient_and_point",
        "16_linear_parallel_and_perpendicular_lines",
        "17_linear_horizontal_and_vertical_lines",
    ],
    "quadratic_effect": [
        "20_quadratic_effect_of_parameter_a",
        "21_quadratic_effect_of_parameter_q",
    ],
    "quadratic_features": [
        "19_quadratic_turning_point_and_axis_of_symmetry",
        "22_quadratic_x_and_y_intercepts",
        "24_quadratic_equation_from_turning_point_and_point",
        "25_quadratic_intervals_of_increase_and_decrease",
    ],
    "hyperbola_features": [
        "26_hyperbola_vertical_and_horizontal_asymptotes",
        "27_hyperbola_axes_of_symmetry",
        "28_hyperbola_effect_of_parameter_a",
        "30_hyperbola_x_and_y_intercepts",
        "31_hyperbola_equation_from_asymptote_and_point",
    ],
    "exponential_features": [
        "32_exponential_horizontal_asymptote",
        "33_exponential_y_intercept_calculation",
        "34_exponential_growth_vs_decay",
        "36_exponential_equation_from_asymptote_and_point",
    ],
    "trig_graph_features": [
        "37_trig_sine_amplitude_period_range",
        "38_trig_cosine_amplitude_period_range",
        "39_trig_tangent_period_and_asymptotes",
        "40_trig_effect_of_vertical_shift_q",
        "41_trig_find_equation_from_sketch",
    ],
    "interpret_graph": [
        "44_graph_reading_coordinates_and_values",
        "45_graphical_inequalities_positive_negative",
        "46_graphical_inequalities_comparison",
        "47_vertical_distance_between_two_graphs",
    ],
    "match_equation_graph": [
        "24_quadratic_equation_from_turning_point_and_point",
        "31_hyperbola_equation_from_asymptote_and_point",
        "36_exponential_equation_from_asymptote_and_point",
        "41_trig_find_equation_from_sketch",
    ],
    "parameter_manipulation": [
        "20_quadratic_effect_of_parameter_a",
        "21_quadratic_effect_of_parameter_q",
        "40_trig_effect_of_vertical_shift_q",
        "49_vertical_translation_transformation",
    ],
    "concepts": SUBSKILLS[:25],
    "compound": SUBSKILLS,
    "mixed": SUBSKILLS,
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills."""
    return list(SUBSKILLS)


def _resolve_target(rng: random.Random, subskill: Optional[str]) -> str:
    """Resolve subskill key or alias to a canonical subskill ID."""
    target = (subskill or "").strip()
    if not target or target in ("mixed", "compound", "default", "all", "auto"):
        return rng.choice(SUBSKILLS)
    if target in ARCHETYPE_BUILDERS:
        return target
    if target in _LEGACY_ALIASES:
        return rng.choice(_LEGACY_ALIASES[target])
    if target.startswith("elementary_"):
        candidate = target[len("elementary_"):]
        if candidate in ARCHETYPE_BUILDERS:
            return candidate
        if candidate in _LEGACY_ALIASES:
            return rng.choice(_LEGACY_ALIASES[candidate])
        matches = [k for k in SUBSKILLS if candidate in k]
        return rng.choice(matches) if matches else rng.choice(SUBSKILLS)
    matches = [k for k in SUBSKILLS if target in k]
    return rng.choice(matches) if matches else rng.choice(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 10 Functions question."""
    rng = random.Random(seed)
    requested = kwargs.get("archetype") or subskill
    target = _resolve_target(rng, requested)
    q = ARCHETYPE_BUILDERS[target](rng)
    difficulty = kwargs.get("difficulty")
    if difficulty:
        q["difficulty"] = difficulty
    q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any] | List[Dict[str, Any]]:
    """Generate one or multiple deterministic Grade 10 Functions questions."""
    base = 0 if seed is None else int(seed)
    questions: List[Dict[str, Any]] = []
    for i in range(max(1, int(count))):
        s = base * 1000 + i if seed is not None else None
        item = generate_question(subskill=subskill, seed=s, difficulty=difficulty, **kwargs)
        questions.append(item)
    return questions[0] if count == 1 else questions
