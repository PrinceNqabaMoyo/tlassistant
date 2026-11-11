"""Numbers and Calculations with Numbers Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 1 Topic:
1. Formats, conventions, integers, and fractions (Subskills 1 to 8)
2. Order of operations and calculator mastery (BODMAS) (Subskills 9 to 16)
3. Squares, roots, cubes, and Pythagoras (Subskills 17 to 24)
4. Rounding in context: up, down, 5c cash rounding (Subskills 25 to 33)
5. Ratios, rates, proportions, unit price, speed (Subskills 34 to 43)
6. Percentages, percentage change, reverse VAT, hire purchase (Subskills 44 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .formats_conventions import (
    _gen_num_fmt_sa_decimal_comma_space_grouping,
    _gen_num_fmt_counting_vs_order_vs_code,
    _gen_num_fmt_calculable_vs_non_calculable,
    _gen_num_fmt_negative_numbers_context,
    _gen_num_fmt_scientific_large_numbers_words,
    _gen_num_fmt_fraction_decimal_percentage_equivalence,
    _gen_num_fmt_significant_figures_estimation,
    _gen_num_fmt_calculator_display_translation,
)
from .order_of_operations import (
    _gen_num_op_bodmas_brackets_multiplication_addition,
    _gen_num_op_bodmas_division_fraction_bar,
    _gen_num_op_consecutive_discounts_order,
    _gen_num_op_calculator_memory_chain_totals,
    _gen_num_op_fraction_addition_subtraction_practical,
    _gen_num_op_mixed_number_multiplication,
    _gen_num_op_reciprocal_unit_rate,
    _gen_num_op_estimation_mental_rounding_check,
)
from .squares_roots_cubes import (
    _gen_num_pwr_square_area_calculation,
    _gen_num_pwr_square_root_side_from_area,
    _gen_num_pwr_cube_volume_calculation,
    _gen_num_pwr_cube_root_dimension_from_volume,
    _gen_num_pwr_square_difference_border,
    _gen_num_pwr_pythagoras_hypotenuse_simple,
    _gen_num_pwr_square_scale_factor_area,
    _gen_num_pwr_cube_scale_factor_volume,
)
from .rounding_contexts import (
    _gen_num_rnd_standard_nearest_whole_number,
    _gen_num_rnd_standard_decimal_places_two_dp,
    _gen_num_rnd_context_round_up_passengers_transport,
    _gen_num_rnd_context_round_up_materials_paint,
    _gen_num_rnd_context_round_down_affordability,
    _gen_num_rnd_context_round_down_containers_packed,
    _gen_num_rnd_south_african_cash_rounding_cents,
    _gen_num_rnd_distance_nearest_kilometre,
    _gen_num_rnd_significant_figures_scientific,
)
from .ratios_rates_proportions import (
    _gen_num_rat_simplify_two_term_ratio,
    _gen_num_rat_simplify_mixed_units_ratio,
    _gen_num_rat_divide_quantity_two_parts,
    _gen_num_rat_divide_quantity_three_parts,
    _gen_num_rat_find_missing_term_proportion,
    _gen_num_rat_mixing_ratio_recipe_or_fertilizer,
    _gen_num_rat_unit_rate_best_value_comparison,
    _gen_num_rat_consumption_rate_fuel_economy,
    _gen_num_rat_inverse_proportion_workers_time,
    _gen_num_rat_speed_distance_time_rate,
)
from .percentages_applications import (
    generate_subskill_44,
    generate_subskill_45,
    generate_subskill_46,
    generate_subskill_47,
    generate_subskill_48,
    generate_subskill_49,
    generate_subskill_50,
    generate_subskill_51,
    generate_subskill_52,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Formats & Conventions (8)
    "num_fmt_sa_decimal_comma_space_grouping": _gen_num_fmt_sa_decimal_comma_space_grouping,
    "num_fmt_counting_vs_order_vs_code": _gen_num_fmt_counting_vs_order_vs_code,
    "num_fmt_calculable_vs_non_calculable": _gen_num_fmt_calculable_vs_non_calculable,
    "num_fmt_negative_numbers_context": _gen_num_fmt_negative_numbers_context,
    "num_fmt_scientific_large_numbers_words": _gen_num_fmt_scientific_large_numbers_words,
    "num_fmt_fraction_decimal_percentage_equivalence": _gen_num_fmt_fraction_decimal_percentage_equivalence,
    "num_fmt_significant_figures_estimation": _gen_num_fmt_significant_figures_estimation,
    "num_fmt_calculator_display_translation": _gen_num_fmt_calculator_display_translation,

    # Order of Operations (8)
    "num_op_bodmas_brackets_multiplication_addition": _gen_num_op_bodmas_brackets_multiplication_addition,
    "num_op_bodmas_division_fraction_bar": _gen_num_op_bodmas_division_fraction_bar,
    "num_op_consecutive_discounts_order": _gen_num_op_consecutive_discounts_order,
    "num_op_calculator_memory_chain_totals": _gen_num_op_calculator_memory_chain_totals,
    "num_op_fraction_addition_subtraction_practical": _gen_num_op_fraction_addition_subtraction_practical,
    "num_op_mixed_number_multiplication": _gen_num_op_mixed_number_multiplication,
    "num_op_reciprocal_unit_rate": _gen_num_op_reciprocal_unit_rate,
    "num_op_estimation_mental_rounding_check": _gen_num_op_estimation_mental_rounding_check,

    # Squares, Roots, Cubes & Pythagoras (8)
    "num_pwr_square_area_calculation": _gen_num_pwr_square_area_calculation,
    "num_pwr_square_root_side_from_area": _gen_num_pwr_square_root_side_from_area,
    "num_pwr_cube_volume_calculation": _gen_num_pwr_cube_volume_calculation,
    "num_pwr_cube_root_dimension_from_volume": _gen_num_pwr_cube_root_dimension_from_volume,
    "num_pwr_square_difference_border": _gen_num_pwr_square_difference_border,
    "num_pwr_pythagoras_hypotenuse_simple": _gen_num_pwr_pythagoras_hypotenuse_simple,
    "num_pwr_square_scale_factor_area": _gen_num_pwr_square_scale_factor_area,
    "num_pwr_cube_scale_factor_volume": _gen_num_pwr_cube_scale_factor_volume,

    # Rounding Contexts (9)
    "num_rnd_standard_nearest_whole_number": _gen_num_rnd_standard_nearest_whole_number,
    "num_rnd_standard_decimal_places_two_dp": _gen_num_rnd_standard_decimal_places_two_dp,
    "num_rnd_context_round_up_passengers_transport": _gen_num_rnd_context_round_up_passengers_transport,
    "num_rnd_context_round_up_materials_paint": _gen_num_rnd_context_round_up_materials_paint,
    "num_rnd_context_round_down_affordability": _gen_num_rnd_context_round_down_affordability,
    "num_rnd_context_round_down_containers_packed": _gen_num_rnd_context_round_down_containers_packed,
    "num_rnd_south_african_cash_rounding_cents": _gen_num_rnd_south_african_cash_rounding_cents,
    "num_rnd_distance_nearest_kilometre": _gen_num_rnd_distance_nearest_kilometre,
    "num_rnd_significant_figures_scientific": _gen_num_rnd_significant_figures_scientific,

    # Ratios, Rates, Proportions (10)
    "num_rat_simplify_two_term_ratio": _gen_num_rat_simplify_two_term_ratio,
    "num_rat_simplify_mixed_units_ratio": _gen_num_rat_simplify_mixed_units_ratio,
    "num_rat_divide_quantity_two_parts": _gen_num_rat_divide_quantity_two_parts,
    "num_rat_divide_quantity_three_parts": _gen_num_rat_divide_quantity_three_parts,
    "num_rat_find_missing_term_proportion": _gen_num_rat_find_missing_term_proportion,
    "num_rat_mixing_ratio_recipe_or_fertilizer": _gen_num_rat_mixing_ratio_recipe_or_fertilizer,
    "num_rat_unit_rate_best_value_comparison": _gen_num_rat_unit_rate_best_value_comparison,
    "num_rat_consumption_rate_fuel_economy": _gen_num_rat_consumption_rate_fuel_economy,
    "num_rat_inverse_proportion_workers_time": _gen_num_rat_inverse_proportion_workers_time,
    "num_rat_speed_distance_time_rate": _gen_num_rat_speed_distance_time_rate,

    # Percentages & Applications (9)
    "num_pct_calculate_percentage_of_amount": generate_subskill_44,
    "num_pct_express_one_amount_as_percentage_of_another": generate_subskill_45,
    "num_pct_percentage_increase_calculation": generate_subskill_46,
    "num_pct_percentage_decrease_discount": generate_subskill_47,
    "num_pct_percentage_change_increase_or_decrease": generate_subskill_48,
    "num_pct_reverse_percentage_pre_vat_cost": generate_subskill_49,
    "num_pct_reverse_percentage_pre_discount_price": generate_subskill_50,
    "num_pct_pass_rate_test_score_percentage": generate_subskill_51,
    "num_pct_deposit_and_hire_purchase_percentage": generate_subskill_52,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Numbers and Calculations with Numbers."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
