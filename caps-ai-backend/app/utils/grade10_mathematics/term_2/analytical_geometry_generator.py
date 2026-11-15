"""Grade 10 Mathematics — Term 2 — Analytical Geometry (50-Archetype Deterministic Generator).

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Chapter 8 Analytical Geometry syllabus.
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

from .analytical_geometry_archetypes_01_25 import BUILDERS_01_25
from .analytical_geometry_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade10_math_analytical_geometry"
LEARNING_OBJECTIVE = "math10_analytical_geometry"
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
    "distance": [
        "03_distance_formula_horizontal_and_vertical_lines",
        "04_distance_formula_integer_pythagorean_triples",
        "05_distance_formula_simplest_surd_form",
        "06_distance_formula_with_negative_coordinates",
        "07_distance_formula_solve_unknown_coordinate",
        "08_collinear_points_using_distance",
        "09_classify_triangle_equilateral_isosceles_scalene",
        "10_verify_right_angled_triangle_converse_pythagoras",
    ],
    "midpoint": [
        "11_midpoint_formula_integer_coordinates",
        "12_midpoint_formula_fractional_coordinates",
        "13_midpoint_formula_with_negative_coordinates",
        "14_find_endpoint_given_midpoint_and_one_endpoint",
        "15_midpoint_median_of_a_triangle",
        "16_midpoint_theorem_coordinate_proof",
    ],
    "gradient": [
        "17_gradient_formula_positive_slope",
        "18_gradient_formula_negative_slope",
        "19_gradient_zero_horizontal_line",
        "20_gradient_undefined_vertical_line",
        "21_gradient_fractional_simplification",
        "22_collinear_points_using_gradients",
    ],
    "parallel_perpendicular": [
        "23_parallel_lines_equal_gradients",
        "24_perpendicular_lines_product_of_gradients",
        "25_verify_perpendicular_sides_in_triangle",
        "29_equation_of_line_parallel_to_given_line",
        "30_equation_of_line_perpendicular_to_given_line",
    ],
    "line_equations": [
        "26_equation_of_line_gradient_and_y_intercept",
        "27_equation_of_line_from_gradient_and_point",
        "28_equation_of_line_through_two_points",
        "29_equation_of_line_parallel_to_given_line",
        "30_equation_of_line_perpendicular_to_given_line",
        "31_equation_of_perpendicular_bisector",
        "32_equation_of_median_in_triangle",
        "33_equation_of_altitude_in_triangle",
    ],
    "quadrilaterals": [
        "37_parallelogram_properties_opposite_sides_parallel",
        "38_parallelogram_properties_opposite_sides_equal",
        "39_parallelogram_diagonals_bisect_each_other",
        "40_find_fourth_vertex_of_parallelogram",
        "41_rectangle_proof_parallelogram_with_right_angle",
        "42_rhombus_proof_parallelogram_with_perpendicular_diagonals",
        "43_square_proof_all_sides_equal_and_perpendicular",
        "44_trapezium_proof_one_pair_parallel_sides",
        "45_kite_proof_adjacent_pairs_equal",
    ],
    "area": [
        "46_area_of_triangle_right_angled",
        "47_area_of_rectangle_or_square_on_cartesian_plane",
    ],
    "circles_origin": [
        "48_distance_from_origin",
        "49_circle_center_origin_equation_check",
    ],
    "compound": [
        "50_comprehensive_coordinate_geometry_multi_step_problem",
    ],
    "elementary_distance": [
        "03_distance_formula_horizontal_and_vertical_lines",
        "04_distance_formula_integer_pythagorean_triples",
        "05_distance_formula_simplest_surd_form",
    ],
    "elementary_midpoint": [
        "11_midpoint_formula_integer_coordinates",
        "12_midpoint_formula_fractional_coordinates",
    ],
    "elementary_gradient": [
        "17_gradient_formula_positive_slope",
        "18_gradient_formula_negative_slope",
    ],
    "elementary_parallel_perpendicular": [
        "23_parallel_lines_equal_gradients",
        "24_perpendicular_lines_product_of_gradients",
    ],
    "concepts": SUBSKILLS[:25],
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
    """Generate a single deterministic Grade 10 Analytical Geometry question."""
    rng = random.Random(seed)
    requested = kwargs.get("archetype") or subskill or kwargs.get("mode")
    target = _resolve_target(rng, requested)
    q = ARCHETYPE_BUILDERS[target](rng)
    difficulty = kwargs.get("difficulty")
    if difficulty:
        q["difficulty"] = difficulty
    q["seed"] = seed
    return q


def generate_analytical_geometry_question(
    seed: Optional[int] = None,
    mode: str = "compound",
    difficulty: str = "medium",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Legacy backward-compatible dispatcher."""
    return generate_question(subskill=subskill or mode, seed=seed, difficulty=difficulty, **kwargs)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any] | List[Dict[str, Any]]:
    """Generate one or multiple deterministic Grade 10 Analytical Geometry questions."""
    base = 0 if seed is None else int(seed)
    questions: List[Dict[str, Any]] = []
    for i in range(max(1, int(count))):
        s = base * 1000 + i if seed is not None else None
        item = generate_question(subskill=subskill, seed=s, difficulty=difficulty, **kwargs)
        questions.append(item)
    return questions[0] if count == 1 else questions
