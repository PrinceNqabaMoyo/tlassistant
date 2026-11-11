"""Grade 7 Mathematics - Algebraic Equations 1 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 1.md
Focus: Concept of an equation, equivalence, solving by inspection, additive & multiplicative inverses, one-step equations (+, -, *, /), two-step equations, fractions, decimals, SVG balance scales, word problems, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_equations_1_archetypes_01_25 import (
    arch_01_equation_balance_concept,
    arch_02_expression_vs_equation_distinction,
    arch_03_solve_addition_equation_inspection,
    arch_04_solve_addition_equation_rhs_variable,
    arch_05_solve_subtraction_equation_inspection,
    arch_06_solve_subtraction_variable_subtrahend,
    arch_07_solve_multiplication_equation_inspection,
    arch_08_solve_division_equation_inspection,
    arch_09_solve_division_variable_in_denominator,
    arch_10_check_solution_by_substitution,
    arch_11_additive_inverse_property,
    arch_12_multiplicative_inverse_property,
    arch_13_two_step_addition_equation_backtracking,
    arch_14_two_step_subtraction_equation_backtracking,
    arch_15_translate_sum_sentence_to_equation,
    arch_16_translate_difference_sentence_to_equation,
    arch_17_translate_product_sentence_to_equation,
    arch_18_geometry_perimeter_square_equation,
    arch_19_geometry_angles_straight_line_equation,
    arch_20_geometry_angles_in_triangle_equation,
    arch_21_table_trial_and_error_root_finding,
    arch_22_multiple_choice_root_selection,
    arch_23_identify_inverse_operation_required,
    arch_24_equations_with_zero_properties,
    arch_25_equations_subtraction_resulting_in_zero,
)
from .algebraic_equations_1_archetypes_26_50 import (
    arch_26_fraction_coefficient_unit_fraction,
    arch_27_fraction_coefficient_non_unit_fraction,
    arch_28_decimal_coefficient_equation,
    arch_29_decimal_addition_equation,
    arch_30_decimal_subtraction_equation,
    arch_31_two_step_division_with_addition,
    arch_32_two_step_division_with_subtraction,
    arch_33_word_problem_money_subtraction,
    arch_34_word_problem_age_addition,
    arch_35_word_problem_temperature_change,
    arch_36_geometry_perimeter_rectangle_equation,
    arch_37_geometry_perimeter_equilateral_triangle,
    arch_38_flow_diagram_to_equation_solve,
    arch_39_balance_scale_single_unknown_svg,
    arch_40_balance_scale_multiple_unknowns_svg,
    arch_41_balance_scale_compound_svg,
    arch_42_negative_integer_solution_addition,
    arch_43_negative_integer_solution_multiplication,
    arch_44_negative_coefficient_linear_equation,
    arch_45_subtracting_negative_number_equation,
    arch_46_consecutive_numbers_sum_equation,
    arch_47_common_misconception_sign_error_trap,
    arch_48_common_misconception_division_error_trap,
    arch_49_checking_roots_distinguishing_valid_from_invalid,
    arch_50_algebraic_equations_1_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_equation_balance_concept": arch_01_equation_balance_concept,
    "02_expression_vs_equation_distinction": arch_02_expression_vs_equation_distinction,
    "03_solve_addition_equation_inspection": arch_03_solve_addition_equation_inspection,
    "04_solve_addition_equation_rhs_variable": arch_04_solve_addition_equation_rhs_variable,
    "05_solve_subtraction_equation_inspection": arch_05_solve_subtraction_equation_inspection,
    "06_solve_subtraction_variable_subtrahend": arch_06_solve_subtraction_variable_subtrahend,
    "07_solve_multiplication_equation_inspection": arch_07_solve_multiplication_equation_inspection,
    "08_solve_division_equation_inspection": arch_08_solve_division_equation_inspection,
    "09_solve_division_variable_in_denominator": arch_09_solve_division_variable_in_denominator,
    "10_check_solution_by_substitution": arch_10_check_solution_by_substitution,
    "11_additive_inverse_property": arch_11_additive_inverse_property,
    "12_multiplicative_inverse_property": arch_12_multiplicative_inverse_property,
    "13_two_step_addition_equation_backtracking": arch_13_two_step_addition_equation_backtracking,
    "14_two_step_subtraction_equation_backtracking": arch_14_two_step_subtraction_equation_backtracking,
    "15_translate_sum_sentence_to_equation": arch_15_translate_sum_sentence_to_equation,
    "16_translate_difference_sentence_to_equation": arch_16_translate_difference_sentence_to_equation,
    "17_translate_product_sentence_to_equation": arch_17_translate_product_sentence_to_equation,
    "18_geometry_perimeter_square_equation": arch_18_geometry_perimeter_square_equation,
    "19_geometry_angles_straight_line_equation": arch_19_geometry_angles_straight_line_equation,
    "20_geometry_angles_in_triangle_equation": arch_20_geometry_angles_in_triangle_equation,
    "21_table_trial_and_error_root_finding": arch_21_table_trial_and_error_root_finding,
    "22_multiple_choice_root_selection": arch_22_multiple_choice_root_selection,
    "23_identify_inverse_operation_required": arch_23_identify_inverse_operation_required,
    "24_equations_with_zero_properties": arch_24_equations_with_zero_properties,
    "25_equations_subtraction_resulting_in_zero": arch_25_equations_subtraction_resulting_in_zero,
    "26_fraction_coefficient_unit_fraction": arch_26_fraction_coefficient_unit_fraction,
    "27_fraction_coefficient_non_unit_fraction": arch_27_fraction_coefficient_non_unit_fraction,
    "28_decimal_coefficient_equation": arch_28_decimal_coefficient_equation,
    "29_decimal_addition_equation": arch_29_decimal_addition_equation,
    "30_decimal_subtraction_equation": arch_30_decimal_subtraction_equation,
    "31_two_step_division_with_addition": arch_31_two_step_division_with_addition,
    "32_two_step_division_with_subtraction": arch_32_two_step_division_with_subtraction,
    "33_word_problem_money_subtraction": arch_33_word_problem_money_subtraction,
    "34_word_problem_age_addition": arch_34_word_problem_age_addition,
    "35_word_problem_temperature_change": arch_35_word_problem_temperature_change,
    "36_geometry_perimeter_rectangle_equation": arch_36_geometry_perimeter_rectangle_equation,
    "37_geometry_perimeter_equilateral_triangle": arch_37_geometry_perimeter_equilateral_triangle,
    "38_flow_diagram_to_equation_solve": arch_38_flow_diagram_to_equation_solve,
    "39_balance_scale_single_unknown_svg": arch_39_balance_scale_single_unknown_svg,
    "40_balance_scale_multiple_unknowns_svg": arch_40_balance_scale_multiple_unknowns_svg,
    "41_balance_scale_compound_svg": arch_41_balance_scale_compound_svg,
    "42_negative_integer_solution_addition": arch_42_negative_integer_solution_addition,
    "43_negative_integer_solution_multiplication": arch_43_negative_integer_solution_multiplication,
    "44_negative_coefficient_linear_equation": arch_44_negative_coefficient_linear_equation,
    "45_subtracting_negative_number_equation": arch_45_subtracting_negative_number_equation,
    "46_consecutive_numbers_sum_equation": arch_46_consecutive_numbers_sum_equation,
    "47_common_misconception_sign_error_trap": arch_47_common_misconception_sign_error_trap,
    "48_common_misconception_division_error_trap": arch_48_common_misconception_division_error_trap,
    "49_checking_roots_distinguishing_valid_from_invalid": arch_49_checking_roots_distinguishing_valid_from_invalid,
    "50_algebraic_equations_1_comprehensive_diagnostic_autopsy": arch_50_algebraic_equations_1_comprehensive_diagnostic_autopsy,
}

SUBSKILLS = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


generate = generate_question
