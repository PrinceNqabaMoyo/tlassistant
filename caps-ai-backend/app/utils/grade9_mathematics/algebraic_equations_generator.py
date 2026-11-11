"""Grade 9 Mathematics - Algebraic Equations 1 Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 1.md
  curriculum_docs/Mathematics_Gr9/Equations Studio.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .equations_archetypes_01_25 import (
    arch_01_inspection_number_sentence_additive,
    arch_02_inspection_number_sentence_multiplicative,
    arch_03_inspection_table_of_values_solution,
    arch_04_balance_scale_model_two_step_equation,
    arch_05_linear_one_step_additive_inverse,
    arch_06_linear_one_step_multiplicative_inverse,
    arch_07_linear_two_step_positive_integers,
    arch_08_linear_two_step_with_subtraction,
    arch_09_linear_two_step_negative_coefficient,
    arch_10_linear_two_step_negative_solution,
    arch_11_variables_both_sides_positive_integers,
    arch_12_variables_both_sides_negative_solution,
    arch_13_variables_both_sides_fractional_solution,
    arch_14_brackets_single_expansion,
    arch_15_brackets_with_subtraction,
    arch_16_brackets_one_side_variable_other,
    arch_17_brackets_both_sides,
    arch_18_brackets_negative_multiplier,
    arch_19_brackets_two_terms_lhs,
    arch_20_geometric_supplementary_angles_equation,
    arch_21_geometric_triangle_angles_sum_equation,
    arch_22_geometric_vertically_opposite_angles,
    arch_23_geometric_perimeter_rectangle_equation,
    arch_24_check_solution_by_substitution,
    arch_25_word_problem_consecutive_integers,
)
from .equations_archetypes_26_50 import (
    arch_26_word_problem_age_relation,
    arch_27_word_problem_taxi_fare_linear,
    arch_28_word_problem_perimeter_isosceles_triangle,
    arch_29_quadratic_equation_factorised_two_positive_roots,
    arch_30_quadratic_equation_factorised_mixed_roots,
    arch_31_quadratic_equation_common_factor,
    arch_32_quadratic_equation_difference_of_squares_positive_root,
    arch_33_quadratic_equation_difference_of_squares_with_coefficient,
    arch_34_quadratic_equation_trinomial_standard_form,
    arch_35_quadratic_equation_trinomial_mixed_signs,
    arch_36_quadratic_equation_rhs_non_zero_rearrange,
    arch_37_quadratic_equation_perfect_square,
    arch_38_exponential_equation_base_two_integer,
    arch_39_exponential_equation_base_three_integer,
    arch_40_exponential_equation_base_five_integer,
    arch_41_exponential_equation_linear_exponent,
    arch_42_exponential_equation_negative_exponent,
    arch_43_exponential_equation_fractional_base,
    arch_44_exponential_equation_base_ten_powers,
    arch_45_equation_with_algebraic_fraction_cross_multiplication,
    arch_46_equation_with_single_fraction_term,
    arch_47_error_analysis_diagnosing_sign_error_in_transposition,
    arch_48_error_analysis_diagnosing_division_by_zero_variable,
    arch_49_geometric_application_pythagoras_equation,
    arch_50_compound_multi_step_equation_solving_challenge,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_inspection_number_sentence_additive": arch_01_inspection_number_sentence_additive,
    "02_inspection_number_sentence_multiplicative": arch_02_inspection_number_sentence_multiplicative,
    "03_inspection_table_of_values_solution": arch_03_inspection_table_of_values_solution,
    "04_balance_scale_model_two_step_equation": arch_04_balance_scale_model_two_step_equation,
    "05_linear_one_step_additive_inverse": arch_05_linear_one_step_additive_inverse,
    "06_linear_one_step_multiplicative_inverse": arch_06_linear_one_step_multiplicative_inverse,
    "07_linear_two_step_positive_integers": arch_07_linear_two_step_positive_integers,
    "08_linear_two_step_with_subtraction": arch_08_linear_two_step_with_subtraction,
    "09_linear_two_step_negative_coefficient": arch_09_linear_two_step_negative_coefficient,
    "10_linear_two_step_negative_solution": arch_10_linear_two_step_negative_solution,
    "11_variables_both_sides_positive_integers": arch_11_variables_both_sides_positive_integers,
    "12_variables_both_sides_negative_solution": arch_12_variables_both_sides_negative_solution,
    "13_variables_both_sides_fractional_solution": arch_13_variables_both_sides_fractional_solution,
    "14_brackets_single_expansion": arch_14_brackets_single_expansion,
    "15_brackets_with_subtraction": arch_15_brackets_with_subtraction,
    "16_brackets_one_side_variable_other": arch_16_brackets_one_side_variable_other,
    "17_brackets_both_sides": arch_17_brackets_both_sides,
    "18_brackets_negative_multiplier": arch_18_brackets_negative_multiplier,
    "19_brackets_two_terms_lhs": arch_19_brackets_two_terms_lhs,
    "20_geometric_supplementary_angles_equation": arch_20_geometric_supplementary_angles_equation,
    "21_geometric_triangle_angles_sum_equation": arch_21_geometric_triangle_angles_sum_equation,
    "22_geometric_vertically_opposite_angles": arch_22_geometric_vertically_opposite_angles,
    "23_geometric_perimeter_rectangle_equation": arch_23_geometric_perimeter_rectangle_equation,
    "24_check_solution_by_substitution": arch_24_check_solution_by_substitution,
    "25_word_problem_consecutive_integers": arch_25_word_problem_consecutive_integers,
    "26_word_problem_age_relation": arch_26_word_problem_age_relation,
    "27_word_problem_taxi_fare_linear": arch_27_word_problem_taxi_fare_linear,
    "28_word_problem_perimeter_isosceles_triangle": arch_28_word_problem_perimeter_isosceles_triangle,
    "29_quadratic_equation_factorised_two_positive_roots": arch_29_quadratic_equation_factorised_two_positive_roots,
    "30_quadratic_equation_factorised_mixed_roots": arch_30_quadratic_equation_factorised_mixed_roots,
    "31_quadratic_equation_common_factor": arch_31_quadratic_equation_common_factor,
    "32_quadratic_equation_difference_of_squares_positive_root": arch_32_quadratic_equation_difference_of_squares_positive_root,
    "33_quadratic_equation_difference_of_squares_with_coefficient": arch_33_quadratic_equation_difference_of_squares_with_coefficient,
    "34_quadratic_equation_trinomial_standard_form": arch_34_quadratic_equation_trinomial_standard_form,
    "35_quadratic_equation_trinomial_mixed_signs": arch_35_quadratic_equation_trinomial_mixed_signs,
    "36_quadratic_equation_rhs_non_zero_rearrange": arch_36_quadratic_equation_rhs_non_zero_rearrange,
    "37_quadratic_equation_perfect_square": arch_37_quadratic_equation_perfect_square,
    "38_exponential_equation_base_two_integer": arch_38_exponential_equation_base_two_integer,
    "39_exponential_equation_base_three_integer": arch_39_exponential_equation_base_three_integer,
    "40_exponential_equation_base_five_integer": arch_40_exponential_equation_base_five_integer,
    "41_exponential_equation_linear_exponent": arch_41_exponential_equation_linear_exponent,
    "42_exponential_equation_negative_exponent": arch_42_exponential_equation_negative_exponent,
    "43_exponential_equation_fractional_base": arch_43_exponential_equation_fractional_base,
    "44_exponential_equation_base_ten_powers": arch_44_exponential_equation_base_ten_powers,
    "45_equation_with_algebraic_fraction_cross_multiplication": arch_45_equation_with_algebraic_fraction_cross_multiplication,
    "46_equation_with_single_fraction_term": arch_46_equation_with_single_fraction_term,
    "47_error_analysis_diagnosing_sign_error_in_transposition": arch_47_error_analysis_diagnosing_sign_error_in_transposition,
    "48_error_analysis_diagnosing_division_by_zero_variable": arch_48_error_analysis_diagnosing_division_by_zero_variable,
    "49_geometric_application_pythagoras_equation": arch_49_geometric_application_pythagoras_equation,
    "50_compound_multi_step_equation_solving_challenge": arch_50_compound_multi_step_equation_solving_challenge,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_algebraic_equations_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Algebraic Equations 1 question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Equations 1"
    q["term"] = 2
    return q


generate_grade9_equations_question = generate_grade9_algebraic_equations_question


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """6-Pillar Generator Contract entry point."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    if subskill and subskill in ARCHETYPE_MAP:
        candidates = [subskill]
    else:
        candidates = SUBSKILLS

    for i in range(count):
        sub = candidates[i % len(candidates)] if len(candidates) > 1 else candidates[0]
        sub_seed = r.randint(1, 1_000_000_000)
        q = generate_grade9_algebraic_equations_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
