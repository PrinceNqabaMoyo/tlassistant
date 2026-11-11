"""
Grade 8 Mathematics - Algebraic Equations 1 Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .algebraic_equations_1_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_inspection_one_step_addition,
    arch_02_inspection_one_step_subtraction,
    arch_03_inspection_subtrahend_unknown,
    arch_04_inspection_one_step_multiplication,
    arch_05_inspection_one_step_division,
    arch_06_inspection_divisor_unknown,
    arch_07_inspection_two_step_mult_add,
    arch_08_inspection_two_step_mult_subtract,
    arch_09_inspection_two_step_div_add,
    arch_10_inspection_two_step_div_subtract,
    arch_11_inspection_negative_solution_addition,
    arch_12_inspection_negative_solution_multiplication,
    arch_13_inspection_negative_coefficient_solution,
    arch_14_inspection_two_step_negative_solution,
    arch_15_inspection_variable_on_both_sides_simple,
    arch_16_trial_and_improvement_bracket_evaluation,
    arch_17_trial_and_improvement_identifying_too_high_too_low,
    arch_18_trial_and_improvement_quadratic_inspection,
    arch_19_additive_inverse_property,
    arch_20_multiplicative_inverse_property,
    arch_21_verifying_solution_lhs_equals_rhs,
    arch_22_distinguishing_equation_from_expression,
    arch_23_identifying_root_from_multiple_choice,
    arch_24_translating_thinking_of_a_number_puzzle,
    arch_25_translating_difference_number_puzzle,
)
from .algebraic_equations_1_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_setting_up_equation_consecutive_integers,
    arch_27_setting_up_equation_consecutive_even_integers,
    arch_28_setting_up_equation_perimeter_of_square,
    arch_29_setting_up_equation_perimeter_of_rectangle,
    arch_30_setting_up_equation_perimeter_of_triangle,
    arch_31_setting_up_equation_age_relationship,
    arch_32_setting_up_equation_shopping_cost,
    arch_33_setting_up_equation_taxi_fare,
    arch_34_solving_equation_with_brackets_inspection,
    arch_35_solving_equation_with_brackets_difference,
    arch_36_solving_equation_variable_both_sides_integer_inspection,
    arch_37_solving_equation_with_fractions_common_denominator,
    arch_38_solving_equation_with_negative_constant_both_sides,
    arch_39_flow_diagram_inversion_backtracking,
    arch_40_diagnosing_transposition_sign_error,
    arch_41_diagnosing_division_coefficient_error,
    arch_42_solving_equation_fractional_solution,
    arch_43_verifying_whether_given_value_is_root,
    arch_44_solving_equation_square_root_inspection,
    arch_45_solving_equation_cube_root_inspection,
    arch_46_setting_up_equation_two_angles_complementary,
    arch_47_setting_up_equation_two_angles_supplementary,
    arch_48_solving_equation_zero_product_property_intro,
    arch_49_solving_equation_with_decimals_inspection,
    arch_50_algebraic_equations_1_comprehensive_modelling,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_inspection_one_step_addition",
    "02_inspection_one_step_subtraction",
    "03_inspection_subtrahend_unknown",
    "04_inspection_one_step_multiplication",
    "05_inspection_one_step_division",
    "06_inspection_divisor_unknown",
    "07_inspection_two_step_mult_add",
    "08_inspection_two_step_mult_subtract",
    "09_inspection_two_step_div_add",
    "10_inspection_two_step_div_subtract",
    # 11 - 20
    "11_inspection_negative_solution_addition",
    "12_inspection_negative_solution_multiplication",
    "13_inspection_negative_coefficient_solution",
    "14_inspection_two_step_negative_solution",
    "15_inspection_variable_on_both_sides_simple",
    "16_trial_and_improvement_bracket_evaluation",
    "17_trial_and_improvement_identifying_too_high_too_low",
    "18_trial_and_improvement_quadratic_inspection",
    "19_additive_inverse_property",
    "20_multiplicative_inverse_property",
    # 21 - 30
    "21_verifying_solution_lhs_equals_rhs",
    "22_distinguishing_equation_from_expression",
    "23_identifying_root_from_multiple_choice",
    "24_translating_thinking_of_a_number_puzzle",
    "25_translating_difference_number_puzzle",
    "26_setting_up_equation_consecutive_integers",
    "27_setting_up_equation_consecutive_even_integers",
    "28_setting_up_equation_perimeter_of_square",
    "29_setting_up_equation_perimeter_of_rectangle",
    "30_setting_up_equation_perimeter_of_triangle",
    # 31 - 40
    "31_setting_up_equation_age_relationship",
    "32_setting_up_equation_shopping_cost",
    "33_setting_up_equation_taxi_fare",
    "34_solving_equation_with_brackets_inspection",
    "35_solving_equation_with_brackets_difference",
    "36_solving_equation_variable_both_sides_integer_inspection",
    "37_solving_equation_with_fractions_common_denominator",
    "38_solving_equation_with_negative_constant_both_sides",
    "39_flow_diagram_inversion_backtracking",
    "40_diagnosing_transposition_sign_error",
    # 41 - 50
    "41_diagnosing_division_coefficient_error",
    "42_solving_equation_fractional_solution",
    "43_verifying_whether_given_value_is_root",
    "44_solving_equation_square_root_inspection",
    "45_solving_equation_cube_root_inspection",
    "46_setting_up_equation_two_angles_complementary",
    "47_setting_up_equation_two_angles_supplementary",
    "48_solving_equation_zero_product_property_intro",
    "49_solving_equation_with_decimals_inspection",
    "50_algebraic_equations_1_comprehensive_modelling",
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
        q.setdefault("topic", "Algebraic equations 1")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
