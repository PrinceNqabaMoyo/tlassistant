"""
Grade 8 Mathematics - Algebraic Equations 2 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_equations_2_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_classifying_open_vs_closed_number_sentence,
    arch_02_writing_closed_number_sentence_bus_passengers,
    arch_03_writing_closed_number_sentence_discount_pricing,
    arch_04_linear_equation_variables_both_sides_positive_integers,
    arch_05_linear_equation_variables_both_sides_negative_solution,
    arch_06_linear_equation_variables_both_sides_negative_coefficients,
    arch_07_linear_equation_variables_both_sides_zero_solution,
    arch_08_equation_with_single_bracket_on_left,
    arch_09_equation_with_single_bracket_with_negative_multiplier,
    arch_10_equation_with_brackets_on_both_sides,
    arch_11_equation_with_brackets_on_both_sides_mixed_signs,
    arch_12_equation_expanding_two_brackets_on_same_side,
    arch_13_equation_with_subtraction_of_bracket,
    arch_14_equation_nested_brackets_combining_like_terms,
    arch_15_consecutive_integers_summing_to_negative_target,
    arch_16_consecutive_multiples_sum,
    arch_17_consecutive_odd_integers_sum,
    arch_18_cost_comparison_two_cellular_packages,
    arch_19_cost_comparison_two_gym_memberships,
    arch_20_geometric_perimeter_isosceles_triangle_equation,
    arch_21_geometric_perimeter_equilateral_vs_square,
    arch_22_geometric_perimeter_rectangle_opposite_sides_equal,
    arch_23_geometric_angles_triangle_interior_sum,
    arch_24_geometric_angles_vertically_opposite_equation,
    arch_25_geometric_angles_adjacent_supplementary_equation,
)
from .algebraic_equations_2_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_geometric_angles_quadrilateral_interior_sum,
    arch_27_age_problem_parent_and_two_children,
    arch_28_age_problem_future_years_ratio,
    arch_29_distance_speed_time_meeting_problem,
    arch_30_distance_speed_time_overtaking_problem,
    arch_31_money_coin_problem_two_denominations,
    arch_32_tickets_two_tier_pricing_equation,
    arch_33_sharing_items_in_given_ratio_equation,
    arch_34_perimeter_of_parallelogram_equation,
    arch_35_rhombus_side_length_equation,
    arch_36_fraction_equation_single_fraction_equals_binomial,
    arch_37_fraction_equation_difference_of_fractions,
    arch_38_fraction_equation_binomial_numerators,
    arch_39_fraction_equation_monomial_denominator_cancelling,
    arch_40_equation_leading_to_identity_all_real_solutions,
    arch_41_equation_leading_to_contradiction_no_solution,
    arch_42_diagnosing_bracket_expansion_error_in_equations,
    arch_43_diagnosing_variable_cancellation_fallacy,
    arch_44_equation_with_decimal_coefficients_both_sides,
    arch_45_equation_with_square_root_term,
    arch_46_equation_with_cube_root_term,
    arch_47_geometric_area_model_rectangle_area_equation,
    arch_48_work_rate_problem_intro,
    arch_49_water_tank_drainage_linear_equation,
    arch_50_algebraic_equations_2_capstone_synthesis,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_classifying_open_vs_closed_number_sentence",
    "02_writing_closed_number_sentence_bus_passengers",
    "03_writing_closed_number_sentence_discount_pricing",
    "04_linear_equation_variables_both_sides_positive_integers",
    "05_linear_equation_variables_both_sides_negative_solution",
    "06_linear_equation_variables_both_sides_negative_coefficients",
    "07_linear_equation_variables_both_sides_zero_solution",
    "08_equation_with_single_bracket_on_left",
    "09_equation_with_single_bracket_with_negative_multiplier",
    "10_equation_with_brackets_on_both_sides",
    # 11 - 20
    "11_equation_with_brackets_on_both_sides_mixed_signs",
    "12_equation_expanding_two_brackets_on_same_side",
    "13_equation_with_subtraction_of_bracket",
    "14_equation_nested_brackets_combining_like_terms",
    "15_consecutive_integers_summing_to_negative_target",
    "16_consecutive_multiples_sum",
    "17_consecutive_odd_integers_sum",
    "18_cost_comparison_two_cellular_packages",
    "19_cost_comparison_two_gym_memberships",
    "20_geometric_perimeter_isosceles_triangle_equation",
    # 21 - 30
    "21_geometric_perimeter_equilateral_vs_square",
    "22_geometric_perimeter_rectangle_opposite_sides_equal",
    "23_geometric_angles_triangle_interior_sum",
    "24_geometric_angles_vertically_opposite_equation",
    "25_geometric_angles_adjacent_supplementary_equation",
    "26_geometric_angles_quadrilateral_interior_sum",
    "27_age_problem_parent_and_two_children",
    "28_age_problem_future_years_ratio",
    "29_distance_speed_time_meeting_problem",
    "30_distance_speed_time_overtaking_problem",
    # 31 - 40
    "31_money_coin_problem_two_denominations",
    "32_tickets_two_tier_pricing_equation",
    "33_sharing_items_in_given_ratio_equation",
    "34_perimeter_of_parallelogram_equation",
    "35_rhombus_side_length_equation",
    "36_fraction_equation_single_fraction_equals_binomial",
    "37_fraction_equation_difference_of_fractions",
    "38_fraction_equation_binomial_numerators",
    "39_fraction_equation_monomial_denominator_cancelling",
    "40_equation_leading_to_identity_all_real_solutions",
    # 41 - 50
    "41_equation_leading_to_contradiction_no_solution",
    "42_diagnosing_bracket_expansion_error_in_equations",
    "43_diagnosing_variable_cancellation_fallacy",
    "44_equation_with_decimal_coefficients_both_sides",
    "45_equation_with_square_root_term",
    "46_equation_with_cube_root_term",
    "47_geometric_area_model_rectangle_area_equation",
    "48_work_rate_problem_intro",
    "49_water_tank_drainage_linear_equation",
    "50_algebraic_equations_2_capstone_synthesis",
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
        q.setdefault("topic", "Algebraic equations 2")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
