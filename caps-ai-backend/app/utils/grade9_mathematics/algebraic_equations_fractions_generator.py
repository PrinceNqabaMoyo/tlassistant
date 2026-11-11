"""Grade 9 Mathematics - Equations 2 (Algebraic Equations with Fractions & Quadratics) Generator.
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 2.md
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md

100% CAPS-aligned deterministic question generator (50 Semantic Archetypes).
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .equations_fractions_archetypes_01_25 import (
    arch_01_fraction_linear_basic_monomial_denominator,
    arch_02_fraction_linear_two_step_additive,
    arch_03_fraction_linear_two_step_subtractive,
    arch_04_fraction_linear_binomial_numerator_simple,
    arch_05_fraction_linear_binomial_numerator_subtraction,
    arch_06_fraction_linear_coefficient_binomial_numerator,
    arch_07_fraction_linear_coefficient_negative_binomial,
    arch_08_fraction_balance_scale_model_visual,
    arch_09_fraction_linear_both_sides_monomial,
    arch_10_fraction_linear_sum_two_fractions_same_denominator,
    arch_11_fraction_linear_sum_two_fractions_lcd_coprime,
    arch_12_fraction_linear_diff_two_fractions_lcd,
    arch_13_fraction_linear_binomial_numerators_add_lcd,
    arch_14_fraction_linear_binomial_numerators_sub_negative_distrib,
    arch_15_fraction_linear_binomial_numerators_diff_lcd_multiple,
    arch_16_fraction_linear_three_fractions_lcd,
    arch_17_fraction_linear_constant_term_clearing,
    arch_18_fraction_cross_multiplication_basic,
    arch_19_fraction_cross_multiplication_coefficients,
    arch_20_fraction_cross_multiplication_variable_denominator,
    arch_21_fraction_cross_multiplication_both_variable_denominators,
    arch_22_fraction_brackets_distributive_monomial,
    arch_23_fraction_brackets_expanded_with_lcd,
    arch_24_geometric_perimeter_fractional_side_svg,
    arch_25_error_analysis_forgot_lcd_multiplication_on_rhs,
)
from .equations_fractions_archetypes_26_50 import (
    arch_26_error_analysis_sign_error_distributing_negative_fraction,
    arch_27_quadratic_zero_product_already_factorised,
    arch_28_quadratic_zero_product_mixed_signs,
    arch_29_quadratic_zero_product_with_leading_coefficient,
    arch_30_quadratic_common_factor_monomial,
    arch_31_quadratic_common_factor_with_coefficient,
    arch_32_quadratic_common_factor_negative_leading,
    arch_33_quadratic_difference_of_squares_basic,
    arch_34_quadratic_difference_of_squares_with_coefficient,
    arch_35_quadratic_difference_of_squares_common_factor_first,
    arch_36_quadratic_trinomial_standard_both_positive,
    arch_37_quadratic_trinomial_standard_both_negative,
    arch_38_quadratic_trinomial_standard_opposite_signs,
    arch_39_quadratic_trinomial_perfect_square,
    arch_40_quadratic_rearrange_rhs_to_standard_form,
    arch_41_quadratic_expand_brackets_then_factorise,
    arch_42_quadratic_geometric_area_rectangle_svg,
    arch_43_error_analysis_divided_by_variable_lost_zero_root,
    arch_44_literal_equation_subject_linear_fraction_simple,
    arch_45_literal_equation_subject_triangle_area_fraction,
    arch_46_literal_equation_subject_temperature_conversion,
    arch_47_literal_equation_subject_linear_rational_expression,
    arch_48_word_problem_fractional_age_relation,
    arch_49_word_problem_fractional_number_sum,
    arch_50_word_problem_speed_distance_time_fractional,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_fraction_linear_basic_monomial_denominator": arch_01_fraction_linear_basic_monomial_denominator,
    "02_fraction_linear_two_step_additive": arch_02_fraction_linear_two_step_additive,
    "03_fraction_linear_two_step_subtractive": arch_03_fraction_linear_two_step_subtractive,
    "04_fraction_linear_binomial_numerator_simple": arch_04_fraction_linear_binomial_numerator_simple,
    "05_fraction_linear_binomial_numerator_subtraction": arch_05_fraction_linear_binomial_numerator_subtraction,
    "06_fraction_linear_coefficient_binomial_numerator": arch_06_fraction_linear_coefficient_binomial_numerator,
    "07_fraction_linear_coefficient_negative_binomial": arch_07_fraction_linear_coefficient_negative_binomial,
    "08_fraction_balance_scale_model_visual": arch_08_fraction_balance_scale_model_visual,
    "09_fraction_linear_both_sides_monomial": arch_09_fraction_linear_both_sides_monomial,
    "10_fraction_linear_sum_two_fractions_same_denominator": arch_10_fraction_linear_sum_two_fractions_same_denominator,
    "11_fraction_linear_sum_two_fractions_lcd_coprime": arch_11_fraction_linear_sum_two_fractions_lcd_coprime,
    "12_fraction_linear_diff_two_fractions_lcd": arch_12_fraction_linear_diff_two_fractions_lcd,
    "13_fraction_linear_binomial_numerators_add_lcd": arch_13_fraction_linear_binomial_numerators_add_lcd,
    "14_fraction_linear_binomial_numerators_sub_negative_distrib": arch_14_fraction_linear_binomial_numerators_sub_negative_distrib,
    "15_fraction_linear_binomial_numerators_diff_lcd_multiple": arch_15_fraction_linear_binomial_numerators_diff_lcd_multiple,
    "16_fraction_linear_three_fractions_lcd": arch_16_fraction_linear_three_fractions_lcd,
    "17_fraction_linear_constant_term_clearing": arch_17_fraction_linear_constant_term_clearing,
    "18_fraction_cross_multiplication_basic": arch_18_fraction_cross_multiplication_basic,
    "19_fraction_cross_multiplication_coefficients": arch_19_fraction_cross_multiplication_coefficients,
    "20_fraction_cross_multiplication_variable_denominator": arch_20_fraction_cross_multiplication_variable_denominator,
    "21_fraction_cross_multiplication_both_variable_denominators": arch_21_fraction_cross_multiplication_both_variable_denominators,
    "22_fraction_brackets_distributive_monomial": arch_22_fraction_brackets_distributive_monomial,
    "23_fraction_brackets_expanded_with_lcd": arch_23_fraction_brackets_expanded_with_lcd,
    "24_geometric_perimeter_fractional_side_svg": arch_24_geometric_perimeter_fractional_side_svg,
    "25_error_analysis_forgot_lcd_multiplication_on_rhs": arch_25_error_analysis_forgot_lcd_multiplication_on_rhs,
    "26_error_analysis_sign_error_distributing_negative_fraction": arch_26_error_analysis_sign_error_distributing_negative_fraction,
    "27_quadratic_zero_product_already_factorised": arch_27_quadratic_zero_product_already_factorised,
    "28_quadratic_zero_product_mixed_signs": arch_28_quadratic_zero_product_mixed_signs,
    "29_quadratic_zero_product_with_leading_coefficient": arch_29_quadratic_zero_product_with_leading_coefficient,
    "30_quadratic_common_factor_monomial": arch_30_quadratic_common_factor_monomial,
    "31_quadratic_common_factor_with_coefficient": arch_31_quadratic_common_factor_with_coefficient,
    "32_quadratic_common_factor_negative_leading": arch_32_quadratic_common_factor_negative_leading,
    "33_quadratic_difference_of_squares_basic": arch_33_quadratic_difference_of_squares_basic,
    "34_quadratic_difference_of_squares_with_coefficient": arch_34_quadratic_difference_of_squares_with_coefficient,
    "35_quadratic_difference_of_squares_common_factor_first": arch_35_quadratic_difference_of_squares_common_factor_first,
    "36_quadratic_trinomial_standard_both_positive": arch_36_quadratic_trinomial_standard_both_positive,
    "37_quadratic_trinomial_standard_both_negative": arch_37_quadratic_trinomial_standard_both_negative,
    "38_quadratic_trinomial_standard_opposite_signs": arch_38_quadratic_trinomial_standard_opposite_signs,
    "39_quadratic_trinomial_perfect_square": arch_39_quadratic_trinomial_perfect_square,
    "40_quadratic_rearrange_rhs_to_standard_form": arch_40_quadratic_rearrange_rhs_to_standard_form,
    "41_quadratic_expand_brackets_then_factorise": arch_41_quadratic_expand_brackets_then_factorise,
    "42_quadratic_geometric_area_rectangle_svg": arch_42_quadratic_geometric_area_rectangle_svg,
    "43_error_analysis_divided_by_variable_lost_zero_root": arch_43_error_analysis_divided_by_variable_lost_zero_root,
    "44_literal_equation_subject_linear_fraction_simple": arch_44_literal_equation_subject_linear_fraction_simple,
    "45_literal_equation_subject_triangle_area_fraction": arch_45_literal_equation_subject_triangle_area_fraction,
    "46_literal_equation_subject_temperature_conversion": arch_46_literal_equation_subject_temperature_conversion,
    "47_literal_equation_subject_linear_rational_expression": arch_47_literal_equation_subject_linear_rational_expression,
    "48_word_problem_fractional_age_relation": arch_48_word_problem_fractional_age_relation,
    "49_word_problem_fractional_number_sum": arch_49_word_problem_fractional_number_sum,
    "50_word_problem_speed_distance_time_fractional": arch_50_word_problem_speed_distance_time_fractional,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_equations_fractions_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Equations 2 (fractions & quadratics) question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        chosen_subskill = subskill
        builder = ARCHETYPE_MAP[subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Equations 2"
    q["term"] = 2
    q["learning_objective_id"] = f"g9_eq_frac_{chosen_subskill}"
    q["archetype"] = chosen_subskill

    # Sync prompt and question text
    if "question_text" in q and "prompt" not in q:
        q["prompt"] = q["question_text"]
    elif "prompt" in q and "question_text" not in q:
        q["question_text"] = q["prompt"]

    # Sync answer aliases
    if "correct_answer" in q:
        q["correct_value"] = q["correct_answer"]
        q["expected_answer"] = q["correct_answer"]
    elif "correct_value" in q:
        q["correct_answer"] = q["correct_value"]
        q["expected_answer"] = q["correct_value"]

    # Worked solution from hints or marking schema
    hints = q.get("hints", [])
    if hints and "sample_answer" not in q:
        q["sample_answer"] = hints[-1]
    if hints and "worked_solution" not in q:
        q["worked_solution"] = "\n".join(hints)

    schema = q.get("marking_schema")
    if isinstance(schema, list) and "marks" not in q:
        q["marks"] = sum(p.get("marks", 1) for p in schema if isinstance(p, dict)) or 2
    elif "marks" not in q:
        q["marks"] = 2

    q.setdefault("caps_weight_percent", 15)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("mode", "compound")
    q.setdefault("difficulty", "medium")

    return q


# Canonical generator aliases
generate_grade9_equations_question = generate_grade9_equations_fractions_question


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
        q = generate_grade9_equations_fractions_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
