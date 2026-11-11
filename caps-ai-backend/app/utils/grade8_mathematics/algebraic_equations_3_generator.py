"""
Grade 8 Mathematics - Algebraic Equations 3 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 3.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_equations_3_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_orchard_linear_growth_target_milestone,
    arch_02_orchard_comparing_two_growth_rates_break_even,
    arch_03_population_linear_decline_milestone,
    arch_04_break_even_two_linear_service_plans,
    arch_05_exponential_equation_base_2_simple,
    arch_06_exponential_equation_base_3_simple,
    arch_07_exponential_equation_base_5_simple,
    arch_08_exponential_equation_base_10_powers,
    arch_09_exponential_equation_linear_exponent_addition,
    arch_10_exponential_equation_linear_exponent_subtraction,
    arch_11_exponential_equation_coefficient_multiplier,
    arch_12_exponential_equation_negative_exponent_concept,
    arch_13_equation_fractional_denominator_one_term,
    arch_14_equation_fractional_numerator_binomial,
    arch_15_equation_fractional_subtraction_binomial,
    arch_16_equation_fractions_sum_two_denominators,
    arch_17_equation_fractions_difference_two_denominators,
    arch_18_equation_fraction_equals_fraction,
    arch_19_equation_brackets_both_sides_positive,
    arch_20_equation_brackets_both_sides_mixed_signs,
    arch_21_equation_brackets_with_negative_multiplier,
    arch_22_equation_two_brackets_distributed_same_side,
    arch_23_equation_difference_of_two_brackets,
    arch_24_geometry_angles_on_straight_line_algebraic,
    arch_25_geometry_three_angles_on_straight_line,
)
from .algebraic_equations_3_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_geometry_vertically_opposite_angles_algebraic,
    arch_27_geometry_triangle_interior_angles_algebraic,
    arch_28_geometry_isosceles_triangle_base_angles_algebraic,
    arch_29_geometry_exterior_angle_of_triangle_algebraic,
    arch_30_consecutive_integers_algebraic_sum_product_puzzle,
    arch_31_consecutive_even_integers_with_multiplier,
    arch_32_speed_distance_time_opposing_directions,
    arch_33_speed_distance_time_same_direction_catch_up,
    arch_34_money_saving_target_weekly_deposit,
    arch_35_commercial_discount_and_vat_equation,
    arch_36_water_reservoir_inflow_outflow_balance,
    arch_37_perimeter_composite_shape_algebraic,
    arch_38_area_rectangle_algebraic_dimensions,
    arch_39_fraction_equation_bracket_in_numerator,
    arch_40_fraction_equation_variable_in_denominator_simple,
    arch_41_fraction_equation_variable_in_denominator_two_step,
    arch_42_identity_equation_infinite_solutions_proof,
    arch_43_contradiction_equation_no_solution_proof,
    arch_44_diagnosing_distributive_sign_error,
    arch_45_diagnosing_fraction_clearing_common_error,
    arch_46_equation_with_mixed_decimals_and_brackets,
    arch_47_exponential_equation_fractional_base,
    arch_48_exponential_equation_with_root_powers,
    arch_49_two_container_liquid_transfer_equation,
    arch_50_algebraic_equations_3_capstone_synthesis,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_orchard_linear_growth_target_milestone",
    "02_orchard_comparing_two_growth_rates_break_even",
    "03_population_linear_decline_milestone",
    "04_break_even_two_linear_service_plans",
    "05_exponential_equation_base_2_simple",
    "06_exponential_equation_base_3_simple",
    "07_exponential_equation_base_5_simple",
    "08_exponential_equation_base_10_powers",
    "09_exponential_equation_linear_exponent_addition",
    "10_exponential_equation_linear_exponent_subtraction",
    # 11 - 20
    "11_exponential_equation_coefficient_multiplier",
    "12_exponential_equation_negative_exponent_concept",
    "13_equation_fractional_denominator_one_term",
    "14_equation_fractional_numerator_binomial",
    "15_equation_fractional_subtraction_binomial",
    "16_equation_fractions_sum_two_denominators",
    "17_equation_fractions_difference_two_denominators",
    "18_equation_fraction_equals_fraction",
    "19_equation_brackets_both_sides_positive",
    "20_equation_brackets_both_sides_mixed_signs",
    # 21 - 30
    "21_equation_brackets_with_negative_multiplier",
    "22_equation_two_brackets_distributed_same_side",
    "23_equation_difference_of_two_brackets",
    "24_geometry_angles_on_straight_line_algebraic",
    "25_geometry_three_angles_on_straight_line",
    "26_geometry_vertically_opposite_angles_algebraic",
    "27_geometry_triangle_interior_angles_algebraic",
    "28_geometry_isosceles_triangle_base_angles_algebraic",
    "29_geometry_exterior_angle_of_triangle_algebraic",
    "30_consecutive_integers_algebraic_sum_product_puzzle",
    # 31 - 40
    "31_consecutive_even_integers_with_multiplier",
    "32_speed_distance_time_opposing_directions",
    "33_speed_distance_time_same_direction_catch_up",
    "34_money_saving_target_weekly_deposit",
    "35_commercial_discount_and_vat_equation",
    "36_water_reservoir_inflow_outflow_balance",
    "37_perimeter_composite_shape_algebraic",
    "38_area_rectangle_algebraic_dimensions",
    "39_fraction_equation_bracket_in_numerator",
    "40_fraction_equation_variable_in_denominator_simple",
    # 41 - 50
    "41_fraction_equation_variable_in_denominator_two_step",
    "42_identity_equation_infinite_solutions_proof",
    "43_contradiction_equation_no_solution_proof",
    "44_diagnosing_distributive_sign_error",
    "45_diagnosing_fraction_clearing_common_error",
    "46_equation_with_mixed_decimals_and_brackets",
    "47_exponential_equation_fractional_base",
    "48_exponential_equation_with_root_powers",
    "49_two_container_liquid_transfer_equation",
    "50_algebraic_equations_3_capstone_synthesis",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, b in enumerate(BUILDERS, start=1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

for name, b in zip(SUBSKILLS, BUILDERS):
    DISPATCH_TABLE[name] = b
    prefix = name.split("_")[0]
    DISPATCH_TABLE[prefix] = b
    short_slug = "_".join(name.split("_")[1:])
    DISPATCH_TABLE[short_slug] = b


def get_subskills() -> List[str]:
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
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
        q.setdefault("topic", "Algebraic equations 3")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
