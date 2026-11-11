"""
Grade 8 Mathematics - Functions and Relationships 2 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 2.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .functions_2_archetypes_01_25 import (
    arch_01_evaluating_linear_formula_positive_slope,
    arch_02_evaluating_linear_formula_negative_slope,
    arch_03_evaluating_bracketed_formula_distributive,
    arch_04_evaluating_quadratic_formula_simple,
    arch_05_evaluating_quadratic_formula_with_constant,
    arch_06_evaluating_exponential_formula_base_two,
    arch_07_evaluating_exponential_formula_base_three,
    arch_08_evaluating_exponential_formula_shifted_exponent,
    arch_09_evaluating_cubic_formula,
    arch_10_evaluating_inverse_proportion_formula,
    arch_11_completing_table_for_exponential_function,
    arch_12_completing_table_for_quadratic_function,
    arch_13_completing_table_non_consecutive_inputs_linear,
    arch_14_solving_for_input_linear_equation,
    arch_15_solving_for_input_linear_with_brackets,
    arch_16_solving_for_input_quadratic_equation,
    arch_17_solving_for_input_exponential_equation,
    arch_18_solving_for_input_inverse_proportion_equation,
    arch_19_matching_formula_to_linear_table_negative_slope,
    arch_20_matching_formula_to_quadratic_table,
    arch_21_matching_formula_to_exponential_table,
    arch_22_calculating_gradient_from_non_consecutive_table_points,
    arch_23_deducing_linear_rule_from_two_distant_table_entries,
    arch_24_verbal_description_to_algebraic_formula_linear,
    arch_25_verbal_description_to_algebraic_formula_with_brackets,
)

from .functions_2_archetypes_26_50 import (
    arch_26_translating_flow_diagram_to_algebraic_equation,
    arch_27_translating_algebraic_equation_to_flow_diagram,
    arch_28_definition_of_function_one_to_one_and_many_to_one,
    arch_29_identifying_non_function_relation_one_to_many,
    arch_30_identifying_domain_and_range_discrete_set,
    arch_31_completing_table_with_fractional_outputs,
    arch_32_completing_table_with_negative_outputs,
    arch_33_equivalent_linear_formulae_verification,
    arch_34_real_world_electricity_stepped_or_linear_tariff,
    arch_35_real_world_plumber_callout_plus_hourly_rate,
    arch_36_real_world_car_rental_daily_plus_per_km,
    arch_37_real_world_baking_ingredient_ratio_function,
    arch_38_real_world_currency_conversion_exchange_rate_function,
    arch_39_geometry_perimeter_of_regular_polygon_function,
    arch_40_geometry_area_of_square_as_quadratic_function,
    arch_41_geometry_area_of_rectangle_fixed_width_linear_function,
    arch_42_geometry_circumference_of_circle_function,
    arch_43_finding_output_for_very_large_input_in_linear_model,
    arch_44_finding_input_for_very_large_output_in_linear_model,
    arch_45_comparing_two_delivery_services_cheaper_option,
    arch_46_break_even_distance_for_two_car_hire_companies,
    arch_47_evaluating_two_step_function_with_integers,
    arch_48_mystery_formula_identification_from_three_points,
    arch_49_distinguishing_linear_quadratic_exponential_tables,
    arch_50_full_representation_conversion_quad_verbal_table_formula,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10
    arch_01_evaluating_linear_formula_positive_slope,
    arch_02_evaluating_linear_formula_negative_slope,
    arch_03_evaluating_bracketed_formula_distributive,
    arch_04_evaluating_quadratic_formula_simple,
    arch_05_evaluating_quadratic_formula_with_constant,
    arch_06_evaluating_exponential_formula_base_two,
    arch_07_evaluating_exponential_formula_base_three,
    arch_08_evaluating_exponential_formula_shifted_exponent,
    arch_09_evaluating_cubic_formula,
    arch_10_evaluating_inverse_proportion_formula,
    # 11 - 20
    arch_11_completing_table_for_exponential_function,
    arch_12_completing_table_for_quadratic_function,
    arch_13_completing_table_non_consecutive_inputs_linear,
    arch_14_solving_for_input_linear_equation,
    arch_15_solving_for_input_linear_with_brackets,
    arch_16_solving_for_input_quadratic_equation,
    arch_17_solving_for_input_exponential_equation,
    arch_18_solving_for_input_inverse_proportion_equation,
    arch_19_matching_formula_to_linear_table_negative_slope,
    arch_20_matching_formula_to_quadratic_table,
    # 21 - 28
    arch_21_matching_formula_to_exponential_table,
    arch_22_calculating_gradient_from_non_consecutive_table_points,
    arch_23_deducing_linear_rule_from_two_distant_table_entries,
    arch_24_verbal_description_to_algebraic_formula_linear,
    arch_25_verbal_description_to_algebraic_formula_with_brackets,
    arch_26_translating_flow_diagram_to_algebraic_equation,
    arch_27_translating_algebraic_equation_to_flow_diagram,
    arch_28_definition_of_function_one_to_one_and_many_to_one,
    # 29 - 36
    arch_29_identifying_non_function_relation_one_to_many,
    arch_30_identifying_domain_and_range_discrete_set,
    arch_31_completing_table_with_fractional_outputs,
    arch_32_completing_table_with_negative_outputs,
    arch_33_equivalent_linear_formulae_verification,
    arch_34_real_world_electricity_stepped_or_linear_tariff,
    arch_35_real_world_plumber_callout_plus_hourly_rate,
    arch_36_real_world_car_rental_daily_plus_per_km,
    # 37 - 44
    arch_37_real_world_baking_ingredient_ratio_function,
    arch_38_real_world_currency_conversion_exchange_rate_function,
    arch_39_geometry_perimeter_of_regular_polygon_function,
    arch_40_geometry_area_of_square_as_quadratic_function,
    arch_41_geometry_area_of_rectangle_fixed_width_linear_function,
    arch_42_geometry_circumference_of_circle_function,
    arch_43_finding_output_for_very_large_input_in_linear_model,
    arch_44_finding_input_for_very_large_output_in_linear_model,
    # 45 - 50
    arch_45_comparing_two_delivery_services_cheaper_option,
    arch_46_break_even_distance_for_two_car_hire_companies,
    arch_47_evaluating_two_step_function_with_integers,
    arch_48_mystery_formula_identification_from_three_points,
    arch_49_distinguishing_linear_quadratic_exponential_tables,
    arch_50_full_representation_conversion_quad_verbal_table_formula,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_evaluating_linear_formula_positive_slope",
    "02_evaluating_linear_formula_negative_slope",
    "03_evaluating_bracketed_formula_distributive",
    "04_evaluating_quadratic_formula_simple",
    "05_evaluating_quadratic_formula_with_constant",
    "06_evaluating_exponential_formula_base_two",
    "07_evaluating_exponential_formula_base_three",
    "08_evaluating_exponential_formula_shifted_exponent",
    "09_evaluating_cubic_formula",
    "10_evaluating_inverse_proportion_formula",
    # 11 - 20
    "11_completing_table_for_exponential_function",
    "12_completing_table_for_quadratic_function",
    "13_completing_table_non_consecutive_inputs_linear",
    "14_solving_for_input_linear_equation",
    "15_solving_for_input_linear_with_brackets",
    "16_solving_for_input_quadratic_equation",
    "17_solving_for_input_exponential_equation",
    "18_solving_for_input_inverse_proportion_equation",
    "19_matching_formula_to_linear_table_negative_slope",
    "20_matching_formula_to_quadratic_table",
    # 21 - 28
    "21_matching_formula_to_exponential_table",
    "22_calculating_gradient_from_non_consecutive_table_points",
    "23_deducing_linear_rule_from_two_distant_table_entries",
    "24_verbal_description_to_algebraic_formula_linear",
    "25_verbal_description_to_algebraic_formula_with_brackets",
    "26_translating_flow_diagram_to_algebraic_equation",
    "27_translating_algebraic_equation_to_flow_diagram",
    "28_definition_of_function_one_to_one_and_many_to_one",
    # 29 - 36
    "29_identifying_non_function_relation_one_to_many",
    "30_identifying_domain_and_range_discrete_set",
    "31_completing_table_with_fractional_outputs",
    "32_completing_table_with_negative_outputs",
    "33_equivalent_linear_formulae_verification",
    "34_real_world_electricity_stepped_or_linear_tariff",
    "35_real_world_plumber_callout_plus_hourly_rate",
    "36_real_world_car_rental_daily_plus_per_km",
    # 37 - 44
    "37_real_world_baking_ingredient_ratio_function",
    "38_real_world_currency_conversion_exchange_rate_function",
    "39_geometry_perimeter_of_regular_polygon_function",
    "40_geometry_area_of_square_as_quadratic_function",
    "41_geometry_area_of_rectangle_fixed_width_linear_function",
    "42_geometry_circumference_of_circle_function",
    "43_finding_output_for_very_large_input_in_linear_model",
    "44_finding_input_for_very_large_output_in_linear_model",
    # 45 - 50
    "45_comparing_two_delivery_services_cheaper_option",
    "46_break_even_distance_for_two_car_hire_companies",
    "47_evaluating_two_step_function_with_integers",
    "48_mystery_formula_identification_from_three_points",
    "49_distinguishing_linear_quadratic_exponential_tables",
    "50_full_representation_conversion_quad_verbal_table_formula",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases
DISPATCH_TABLE["linear"] = arch_01_evaluating_linear_formula_positive_slope
DISPATCH_TABLE["quadratic"] = arch_04_evaluating_quadratic_formula_simple
DISPATCH_TABLE["exponential"] = arch_06_evaluating_exponential_formula_base_two
DISPATCH_TABLE["table"] = arch_13_completing_table_non_consecutive_inputs_linear
DISPATCH_TABLE["inverse"] = arch_14_solving_for_input_linear_equation


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            idx = int(archetype_index)
            if idx in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[idx]
            elif 1 <= idx <= len(BUILDERS):
                builder = BUILDERS[idx - 1]

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 8)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Functions and relationships 2")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
