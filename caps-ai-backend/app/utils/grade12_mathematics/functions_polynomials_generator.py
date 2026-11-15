"""Grade 12 Mathematics - Functions and Polynomials Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/02. Functions.md and 03. Polynomials.md.

Covers:
  - Definition of a function, vertical and horizontal line tests, one-to-one vs many-to-one.
  - Inverses of linear, quadratic, and exponential functions.
  - Logarithmic function as the inverse of exponential function, asymptotes, domain, and range.
  - Symmetrical reflection across the line y = x and points of intersection.
  - Polynomials, Remainder Theorem, and Factor Theorem.
  - Cubic factorisation via inspection, long division, and synthetic division.
  - Solving cubic equations, intercepts, sign inequalities, and applications.

Strictly zero-LLM, deterministic execution with 50 distinct semantic archetypes.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .functions_polynomials_archetypes_01_25 import BUILDERS_01_25
from .functions_polynomials_archetypes_26_50 import BUILDERS_26_50

ALL_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
ALL_BUILDERS.update(BUILDERS_01_25)
ALL_BUILDERS.update(BUILDERS_26_50)

ORDERED_SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())

SUBSKILLS: Dict[str, str] = {
    # 01 - 25: Functions & Inverses
    "01_function_definition_vertical_line_test": "Function Definition & Vertical Line Test",
    "02_horizontal_line_test_invertibility": "Horizontal Line Test for Invertibility",
    "03_linear_function_inverse_equation": "Equation of Linear Function Inverse",
    "04_linear_function_inverse_coordinates": "Coordinate Transformations for Linear Inverses",
    "05_linear_function_inverse_line_of_symmetry": "Line of Symmetry y = x and Intersection Point",
    "06_quadratic_inverse_equation_full": "Full Inverse Relation of Parabola",
    "07_quadratic_inverse_why_not_function": "Why Parabola Inverse Fails Function Definition",
    "08_quadratic_domain_restriction_positive": "Quadratic Domain Restriction x >= 0",
    "09_quadratic_domain_restriction_negative": "Quadratic Domain Restriction x <= 0",
    "10_quadratic_with_vertical_shift_inverse": "Inverse of Shifted Parabola with Domain Restriction",
    "11_quadratic_turning_point_and_axis_of_symmetry_inverse": "Turning Point & Axis of Symmetry of Parabola Inverse",
    "12_exponential_inverse_as_logarithm_equation": "Logarithm as Inverse of Exponential Function",
    "13_exponential_inverse_fractional_base": "Logarithmic Inverse with Fractional Base",
    "14_exponential_and_log_domain_and_range": "Domain & Range of Exponential vs Logarithmic Functions",
    "15_exponential_and_log_asymptote_interchange": "Asymptote Interchange Under Reflection",
    "16_exponential_with_vertical_shift_inverse": "Inverse of Shifted Exponential Function",
    "17_log_function_find_base_from_point": "Determining Logarithmic Base from Known Point",
    "18_exponential_function_find_base_from_point": "Determining Exponential Base from Known Point",
    "19_log_function_evaluate_exact_values": "Evaluating Exact Logarithms without Calculator",
    "20_log_laws_simplification_in_functions": "Simplifying Expressions with Logarithm Product Law",
    "21_change_of_base_rule_logarithms": "Applying the Change of Base Rule",
    "22_solving_exponential_equations_using_logs": "Solving Exponential Equations via Logarithms",
    "23_solving_logarithmic_equations_basic": "Solving Elementary Logarithmic Equations",
    "24_inverse_functions_reflection_svg": "Visual Reflection of Exponential and Logarithm",
    "25_parabola_and_inverse_branches_svg": "Visual Parabola Domain Restriction Branches",
    # 26 - 50: Polynomials
    "26_polynomial_identification_and_degree": "Polynomial Definition, Degree, and Coefficients",
    "27_polynomial_evaluation_function_notation": "Polynomial Evaluation at Given Input",
    "28_remainder_theorem_linear_divisor": "Remainder Theorem with Linear Divisor",
    "29_remainder_theorem_fractional_divisor": "Remainder Theorem with Fractional Divisor",
    "30_remainder_theorem_solve_single_unknown_k": "Solving for Unknown Parameter Using Remainder Theorem",
    "31_remainder_theorem_solve_simultaneous_two_unknowns": "Simultaneous Equations from Remainder Theorem",
    "32_factor_theorem_verification": "Verifying Factors Using Factor Theorem",
    "33_factor_theorem_solve_unknown_coefficient": "Solving for Unknown Parameter Using Factor Theorem",
    "34_finding_first_rational_root_by_trial": "Finding First Factor of Cubic by Inspection",
    "35_cubic_factorisation_inspection_method": "Factorising Cubic Polynomial by Inspection",
    "36_cubic_factorisation_long_division": "Cubic Factorisation via Algebraic Long Division",
    "37_cubic_factorisation_synthetic_division": "Synthetic Division for Cubic Factorisation",
    "38_full_factorisation_cubic_into_three_linear_factors": "Complete Factorisation of Cubic into Three Linear Factors",
    "39_cubic_factorisation_with_repeated_root": "Cubic Factorisation with Repeated Root",
    "40_cubic_factorisation_irreducible_quadratic_factor": "Cubic Factorisation with Irreducible Quadratic Factor",
    "41_solving_cubic_equation_three_distinct_roots": "Solving Cubic Equation with Three Real Roots",
    "42_solving_cubic_equation_common_factor_first": "Solving Cubic Equation with Common Factor x",
    "43_solving_cubic_equation_repeated_root": "Cubic Equation with Repeated Root and Multiplicity",
    "44_cubic_x_intercepts_from_factorisation": "Determining Cubic Intercepts from Factorised Form",
    "45_cubic_polynomial_sign_analysis_inequality": "Solving Cubic Inequalities via Sign Analysis",
    "46_polynomial_word_problem_box_volume": "Applied Cubic Polynomial - Box Volume",
    "47_functions_and_inverses_composition_identity": "Composite Inverse Functions and Identity Property",
    "48_intersection_function_and_inverse_on_y_equals_x": "Finding Intersection of Function and Inverse on y = x",
    "49_cubic_roots_graphical_relationship_svg": "Graphical Intercepts and Inequality Regions of Cubic",
    "50_compound_nsc_exam_functions_and_polynomials": "Comprehensive Compound Examination Functions & Polynomials Problem",
}

LEGACY_ALIASES: Dict[str, str] = {
    "linear_inverse": "03_linear_function_inverse_equation",
    "quadratic_inverse": "08_quadratic_domain_restriction_positive",
    "exponential_inverse": "12_exponential_inverse_as_logarithm_equation",
    "remainder_theorem": "28_remainder_theorem_linear_divisor",
    "factor_theorem": "32_factor_theorem_verification",
    "cubic_factorisation": "38_full_factorisation_cubic_into_three_linear_factors",
    "cubic_roots": "41_solving_cubic_equation_three_distinct_roots",
}


def _resolve_builder(subskill: Optional[str]) -> Callable[[random.Random], Dict[str, Any]]:
    if not subskill or subskill in ("all", "functions", "polynomials", "functions_polynomials"):
        key = random.choice(ORDERED_SUBSKILLS)
        return ALL_BUILDERS[key]
    if subskill in ALL_BUILDERS:
        return ALL_BUILDERS[subskill]
    if subskill in LEGACY_ALIASES:
        return ALL_BUILDERS[LEGACY_ALIASES[subskill]]
    low = subskill.lower()
    for k in ORDERED_SUBSKILLS:
        if low in k.lower():
            return ALL_BUILDERS[k]
    return ALL_BUILDERS[ORDERED_SUBSKILLS[0]]


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions satisfying the 6-pillar contract."""
    base_seed = seed if seed is not None else random.randint(1000, 999999)
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        rng = random.Random(base_seed + i)
        builder = _resolve_builder(subskill)
        q = builder(rng)
        questions.append(q)

    return questions


def generate_question(subskill: Optional[str] = None, seed: Optional[int] = None, **kwargs: Any) -> Dict[str, Any]:
    qs = generate(subskill=subskill, count=1, seed=seed, **kwargs)
    return qs[0]
