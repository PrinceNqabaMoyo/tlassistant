"""Grade 7 Mathematics - Algebraic Equations 2 Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 2.md
Focus: Two-step equations (ax + b = c, ax - b = c, b - ax = c), bracket equations, variables on both sides, fractions, decimals, SVG balance scales, word problems, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_equations_2_archetypes_01_25 import (
    arch_01_two_step_add_mult_positive_integers,
    arch_02_two_step_sub_mult_positive_integers,
    arch_03_two_step_with_variable_second,
    arch_04_two_step_subtraction_from_constant,
    arch_05_two_step_equation_bracket_positive,
    arch_06_two_step_equation_bracket_subtraction,
    arch_07_two_step_equation_negative_bracket_multiplier,
    arch_08_two_step_equation_negative_multiplier_with_minus,
    arch_09_two_step_division_form_whole_fraction,
    arch_10_two_step_division_form_subtraction_numerator,
    arch_11_variables_both_sides_simple_positive,
    arch_12_variables_both_sides_linear_terms,
    arch_13_variables_both_sides_general,
    arch_14_variables_both_sides_with_subtraction,
    arch_15_negative_coefficient_two_step,
    arch_16_negative_solution_two_step,
    arch_17_zero_solution_two_step,
    arch_18_geometric_perimeter_rectangle_two_step,
    arch_19_geometric_perimeter_isosceles_triangle,
    arch_20_geometric_supplementary_angles_two_step,
    arch_21_geometric_complementary_angles_two_step,
    arch_22_geometric_triangle_angles_algebraic,
    arch_23_word_problem_shopping_unit_cost_plus_fixed,
    arch_24_word_problem_taxi_fare,
    arch_25_word_problem_age_multiplier_plus_years,
)
from .algebraic_equations_2_archetypes_26_50 import (
    arch_26_word_problem_cellphone_airtime,
    arch_27_word_problem_consecutive_even_numbers,
    arch_28_word_problem_consecutive_odd_numbers,
    arch_29_word_problem_perimeter_square_with_algebraic_side,
    arch_30_word_problem_saving_weekly_allowance,
    arch_31_word_problem_temperature_drop_rate,
    arch_32_two_step_with_fractional_coefficient,
    arch_33_two_step_with_fractional_coefficient_subtraction,
    arch_34_two_step_decimal_equation_addition,
    arch_35_two_step_decimal_equation_subtraction,
    arch_36_combining_like_terms_before_solving,
    arch_37_combining_like_terms_subtraction_before_solving,
    arch_38_combining_constants_before_solving,
    arch_39_bracket_expansion_both_sides,
    arch_40_visual_balance_scale_with_brackets,
    arch_41_visual_balance_scale_variables_both_sides,
    arch_42_formal_verification_lhs_rhs_tabular,
    arch_43_checking_multiple_candidate_solutions,
    arch_44_common_misconception_dividing_before_subtraction_trap,
    arch_45_common_misconception_bracket_multiplication_omission_trap,
    arch_46_common_misconception_sign_flip_transposition_trap,
    arch_47_reversing_flow_diagram_two_step,
    arch_48_speed_distance_time_algebraic_equation,
    arch_49_water_tank_draining_equation,
    arch_50_algebraic_equations_2_comprehensive_diagnostic_autopsy,
)

ARCHETYPE_BUILDERS = {
    "01_two_step_add_mult_positive_integers": arch_01_two_step_add_mult_positive_integers,
    "02_two_step_sub_mult_positive_integers": arch_02_two_step_sub_mult_positive_integers,
    "03_two_step_with_variable_second": arch_03_two_step_with_variable_second,
    "04_two_step_subtraction_from_constant": arch_04_two_step_subtraction_from_constant,
    "05_two_step_equation_bracket_positive": arch_05_two_step_equation_bracket_positive,
    "06_two_step_equation_bracket_subtraction": arch_06_two_step_equation_bracket_subtraction,
    "07_two_step_equation_negative_bracket_multiplier": arch_07_two_step_equation_negative_bracket_multiplier,
    "08_two_step_equation_negative_multiplier_with_minus": arch_08_two_step_equation_negative_multiplier_with_minus,
    "09_two_step_division_form_whole_fraction": arch_09_two_step_division_form_whole_fraction,
    "10_two_step_division_form_subtraction_numerator": arch_10_two_step_division_form_subtraction_numerator,
    "11_variables_both_sides_simple_positive": arch_11_variables_both_sides_simple_positive,
    "12_variables_both_sides_linear_terms": arch_12_variables_both_sides_linear_terms,
    "13_variables_both_sides_general": arch_13_variables_both_sides_general,
    "14_variables_both_sides_with_subtraction": arch_14_variables_both_sides_with_subtraction,
    "15_negative_coefficient_two_step": arch_15_negative_coefficient_two_step,
    "16_negative_solution_two_step": arch_16_negative_solution_two_step,
    "17_zero_solution_two_step": arch_17_zero_solution_two_step,
    "18_geometric_perimeter_rectangle_two_step": arch_18_geometric_perimeter_rectangle_two_step,
    "19_geometric_perimeter_isosceles_triangle": arch_19_geometric_perimeter_isosceles_triangle,
    "20_geometric_supplementary_angles_two_step": arch_20_geometric_supplementary_angles_two_step,
    "21_geometric_complementary_angles_two_step": arch_21_geometric_complementary_angles_two_step,
    "22_geometric_triangle_angles_algebraic": arch_22_geometric_triangle_angles_algebraic,
    "23_word_problem_shopping_unit_cost_plus_fixed": arch_23_word_problem_shopping_unit_cost_plus_fixed,
    "24_word_problem_taxi_fare": arch_24_word_problem_taxi_fare,
    "25_word_problem_age_multiplier_plus_years": arch_25_word_problem_age_multiplier_plus_years,
    "26_word_problem_cellphone_airtime": arch_26_word_problem_cellphone_airtime,
    "27_word_problem_consecutive_even_numbers": arch_27_word_problem_consecutive_even_numbers,
    "28_word_problem_consecutive_odd_numbers": arch_28_word_problem_consecutive_odd_numbers,
    "29_word_problem_perimeter_square_with_algebraic_side": arch_29_word_problem_perimeter_square_with_algebraic_side,
    "30_word_problem_saving_weekly_allowance": arch_30_word_problem_saving_weekly_allowance,
    "31_word_problem_temperature_drop_rate": arch_31_word_problem_temperature_drop_rate,
    "32_two_step_with_fractional_coefficient": arch_32_two_step_with_fractional_coefficient,
    "33_two_step_with_fractional_coefficient_subtraction": arch_33_two_step_with_fractional_coefficient_subtraction,
    "34_two_step_decimal_equation_addition": arch_34_two_step_decimal_equation_addition,
    "35_two_step_decimal_equation_subtraction": arch_35_two_step_decimal_equation_subtraction,
    "36_combining_like_terms_before_solving": arch_36_combining_like_terms_before_solving,
    "37_combining_like_terms_subtraction_before_solving": arch_37_combining_like_terms_subtraction_before_solving,
    "38_combining_constants_before_solving": arch_38_combining_constants_before_solving,
    "39_bracket_expansion_both_sides": arch_39_bracket_expansion_both_sides,
    "40_visual_balance_scale_with_brackets": arch_40_visual_balance_scale_with_brackets,
    "41_visual_balance_scale_variables_both_sides": arch_41_visual_balance_scale_variables_both_sides,
    "42_formal_verification_lhs_rhs_tabular": arch_42_formal_verification_lhs_rhs_tabular,
    "43_checking_multiple_candidate_solutions": arch_43_checking_multiple_candidate_solutions,
    "44_common_misconception_dividing_before_subtraction_trap": arch_44_common_misconception_dividing_before_subtraction_trap,
    "45_common_misconception_bracket_multiplication_omission_trap": arch_45_common_misconception_bracket_multiplication_omission_trap,
    "46_common_misconception_sign_flip_transposition_trap": arch_46_common_misconception_sign_flip_transposition_trap,
    "47_reversing_flow_diagram_two_step": arch_47_reversing_flow_diagram_two_step,
    "48_speed_distance_time_algebraic_equation": arch_48_speed_distance_time_algebraic_equation,
    "49_water_tank_draining_equation": arch_49_water_tank_draining_equation,
    "50_algebraic_equations_2_comprehensive_diagnostic_autopsy": arch_50_algebraic_equations_2_comprehensive_diagnostic_autopsy,
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
