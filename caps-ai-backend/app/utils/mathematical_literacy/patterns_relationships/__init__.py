"""Patterns, relationships and representations Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 3 Topic:
1. Graphs that tell a story & trend interpretation (Subskills 1 to 9)
2. Linear patterns & tables of values (Subskills 10 to 18)
3. Formulating linear equations (y = mx + c) (Subskills 19 to 27)
4. Inverse proportion relationships (Subskills 28 to 36)
5. Two-graph comparisons & break-even analysis (Subskills 37 to 44)
6. Advanced representations, step graphs & modeling (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .story_graphs_trends import (
    _gen_pat_story_increasing_decreasing_constant_segments,
    _gen_pat_story_steepness_and_rate_of_change,
    _gen_pat_story_horizontal_segment_meaning,
    _gen_pat_story_discrete_vs_continuous_data_type,
    _gen_pat_story_discrete_vs_continuous_graph_style,
    _gen_pat_story_independent_vs_dependent_variable_identification,
    _gen_pat_story_vertical_intercept_interpretation,
    _gen_pat_story_horizontal_intercept_interpretation,
    _gen_pat_story_distance_time_average_speed_segment,
)
from .linear_tables_patterns import (
    _gen_pat_linear_constant_difference_identification,
    _gen_pat_linear_find_missing_output_in_table,
    _gen_pat_linear_find_missing_input_in_table,
    _gen_pat_linear_toothpick_tile_pattern_formula,
    _gen_pat_linear_predict_high_term_value,
    _gen_pat_linear_determine_pattern_term_number,
    _gen_pat_linear_direct_proportion_constant_ratio,
    _gen_pat_linear_direct_proportion_origin_property,
    _gen_pat_linear_ordered_pairs_from_table,
)
from .linear_equations_formulas import (
    _gen_pat_formula_from_verbal_description,
    _gen_pat_formula_from_table_of_values,
    _gen_pat_formula_identify_rate_and_constant,
    _gen_pat_formula_cellphone_contract_monthly_cost,
    _gen_pat_formula_electrician_callout_plus_hours,
    _gen_pat_formula_taxi_fare_flagfall_plus_km,
    _gen_pat_formula_event_catering_venue_plus_guests,
    _gen_pat_formula_calculate_maximum_units_budget,
    _gen_pat_formula_temperature_conversion_linear,
)
from .inverse_proportion import (
    _gen_pat_inv_constant_product_rule,
    _gen_pat_inv_sharing_cash_prize_among_winners,
    _gen_pat_inv_workers_and_days_to_complete_task,
    _gen_pat_inv_rectangle_dimensions_fixed_area,
    _gen_pat_inv_travel_speed_and_time_fixed_distance,
    _gen_pat_inv_pump_flow_rate_and_tank_emptying_time,
    _gen_pat_inv_table_missing_value_calculation,
    _gen_pat_inv_graph_characteristics_and_shape,
    _gen_pat_inv_compare_direct_vs_inverse_proportion,
)
from .breakeven_comparisons import (
    _gen_pat_comp_identify_intersection_point,
    _gen_pat_comp_meaning_of_intersection_point,
    _gen_pat_comp_contract_vs_prepaid_cheaper_option,
    _gen_pat_comp_car_rental_plan_comparison,
    _gen_pat_comp_breakeven_units_income_equals_cost,
    _gen_pat_comp_profit_or_loss_calculation,
    _gen_pat_comp_income_formula_and_graph,
    _gen_pat_comp_production_cost_formula_and_graph,
)
from .stepped_graphs_modeling import (
    _gen_pat_rep_convert_formula_to_table_entry,
    _gen_pat_rep_parking_step_tariff_graph_reading,
    _gen_pat_rep_postage_courier_stepped_rate,
    _gen_pat_rep_water_tiered_consumption_graph,
    _gen_pat_rep_bank_account_simple_interest_linear_growth,
    _gen_pat_rep_straight_line_depreciation_model,
    _gen_pat_rep_loan_repayment_balance_reduction,
    _gen_pat_rep_summary_representation_choice,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Graphs that tell a story & trend interpretation (9)
    "pat_story_increasing_decreasing_constant_segments": _gen_pat_story_increasing_decreasing_constant_segments,
    "pat_story_steepness_and_rate_of_change": _gen_pat_story_steepness_and_rate_of_change,
    "pat_story_horizontal_segment_meaning": _gen_pat_story_horizontal_segment_meaning,
    "pat_story_discrete_vs_continuous_data_type": _gen_pat_story_discrete_vs_continuous_data_type,
    "pat_story_discrete_vs_continuous_graph_style": _gen_pat_story_discrete_vs_continuous_graph_style,
    "pat_story_independent_vs_dependent_variable_identification": _gen_pat_story_independent_vs_dependent_variable_identification,
    "pat_story_vertical_intercept_interpretation": _gen_pat_story_vertical_intercept_interpretation,
    "pat_story_horizontal_intercept_interpretation": _gen_pat_story_horizontal_intercept_interpretation,
    "pat_story_distance_time_average_speed_segment": _gen_pat_story_distance_time_average_speed_segment,

    # Cluster 2: Linear patterns & tables of values (9)
    "pat_linear_constant_difference_identification": _gen_pat_linear_constant_difference_identification,
    "pat_linear_find_missing_output_in_table": _gen_pat_linear_find_missing_output_in_table,
    "pat_linear_find_missing_input_in_table": _gen_pat_linear_find_missing_input_in_table,
    "pat_linear_toothpick_tile_pattern_formula": _gen_pat_linear_toothpick_tile_pattern_formula,
    "pat_linear_predict_high_term_value": _gen_pat_linear_predict_high_term_value,
    "pat_linear_determine_pattern_term_number": _gen_pat_linear_determine_pattern_term_number,
    "pat_linear_direct_proportion_constant_ratio": _gen_pat_linear_direct_proportion_constant_ratio,
    "pat_linear_direct_proportion_origin_property": _gen_pat_linear_direct_proportion_origin_property,
    "pat_linear_ordered_pairs_from_table": _gen_pat_linear_ordered_pairs_from_table,

    # Cluster 3: Formulating linear equations (9)
    "pat_formula_from_verbal_description": _gen_pat_formula_from_verbal_description,
    "pat_formula_from_table_of_values": _gen_pat_formula_from_table_of_values,
    "pat_formula_identify_rate_and_constant": _gen_pat_formula_identify_rate_and_constant,
    "pat_formula_cellphone_contract_monthly_cost": _gen_pat_formula_cellphone_contract_monthly_cost,
    "pat_formula_electrician_callout_plus_hours": _gen_pat_formula_electrician_callout_plus_hours,
    "pat_formula_taxi_fare_flagfall_plus_km": _gen_pat_formula_taxi_fare_flagfall_plus_km,
    "pat_formula_event_catering_venue_plus_guests": _gen_pat_formula_event_catering_venue_plus_guests,
    "pat_formula_calculate_maximum_units_budget": _gen_pat_formula_calculate_maximum_units_budget,
    "pat_formula_temperature_conversion_linear": _gen_pat_formula_temperature_conversion_linear,

    # Cluster 4: Inverse proportion relationships (9)
    "pat_inv_constant_product_rule": _gen_pat_inv_constant_product_rule,
    "pat_inv_sharing_cash_prize_among_winners": _gen_pat_inv_sharing_cash_prize_among_winners,
    "pat_inv_workers_and_days_to_complete_task": _gen_pat_inv_workers_and_days_to_complete_task,
    "pat_inv_rectangle_dimensions_fixed_area": _gen_pat_inv_rectangle_dimensions_fixed_area,
    "pat_inv_travel_speed_and_time_fixed_distance": _gen_pat_inv_travel_speed_and_time_fixed_distance,
    "pat_inv_pump_flow_rate_and_tank_emptying_time": _gen_pat_inv_pump_flow_rate_and_tank_emptying_time,
    "pat_inv_table_missing_value_calculation": _gen_pat_inv_table_missing_value_calculation,
    "pat_inv_graph_characteristics_and_shape": _gen_pat_inv_graph_characteristics_and_shape,
    "pat_inv_compare_direct_vs_inverse_proportion": _gen_pat_inv_compare_direct_vs_inverse_proportion,

    # Cluster 5: Two-graph comparisons & break-even analysis (8)
    "pat_comp_identify_intersection_point": _gen_pat_comp_identify_intersection_point,
    "pat_comp_meaning_of_intersection_point": _gen_pat_comp_meaning_of_intersection_point,
    "pat_comp_contract_vs_prepaid_cheaper_option": _gen_pat_comp_contract_vs_prepaid_cheaper_option,
    "pat_comp_car_rental_plan_comparison": _gen_pat_comp_car_rental_plan_comparison,
    "pat_comp_breakeven_units_income_equals_cost": _gen_pat_comp_breakeven_units_income_equals_cost,
    "pat_comp_profit_or_loss_calculation": _gen_pat_comp_profit_or_loss_calculation,
    "pat_comp_income_formula_and_graph": _gen_pat_comp_income_formula_and_graph,
    "pat_comp_production_cost_formula_and_graph": _gen_pat_comp_production_cost_formula_and_graph,

    # Cluster 6: Advanced representations, step graphs & modeling (8)
    "pat_rep_convert_formula_to_table_entry": _gen_pat_rep_convert_formula_to_table_entry,
    "pat_rep_parking_step_tariff_graph_reading": _gen_pat_rep_parking_step_tariff_graph_reading,
    "pat_rep_postage_courier_stepped_rate": _gen_pat_rep_postage_courier_stepped_rate,
    "pat_rep_water_tiered_consumption_graph": _gen_pat_rep_water_tiered_consumption_graph,
    "pat_rep_bank_account_simple_interest_linear_growth": _gen_pat_rep_bank_account_simple_interest_linear_growth,
    "pat_rep_straight_line_depreciation_model": _gen_pat_rep_straight_line_depreciation_model,
    "pat_rep_loan_repayment_balance_reduction": _gen_pat_rep_loan_repayment_balance_reduction,
    "pat_rep_summary_representation_choice": _gen_pat_rep_summary_representation_choice,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Patterns, relationships and representations."""
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
