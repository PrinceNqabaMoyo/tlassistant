"""
Grade 7 Mathematics - Exponents, Squares & Cubes Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Exponents.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .exponents_archetypes_01_25 import (
    arch_01_base_and_exponent_identification,
    arch_02_repeated_multiplication_to_power,
    arch_03_power_expanded_to_repeated_multiplication,
    arch_04_evaluating_small_base_powers,
    arch_05_powers_of_ten_evaluation,
    arch_06_zero_exponent_law,
    arch_07_first_power_identity,
    arch_08_comparing_powers_inequality,
    arch_09_calculating_squares_1_to_15,
    arch_10_calculating_squares_multiples_of_ten,
    arch_11_square_root_perfect_squares_1_to_144,
    arch_12_square_root_perfect_squares_169_to_400,
    arch_13_square_root_of_multiples_of_hundred,
    arch_14_estimating_square_roots_between_consecutive_integers,
    arch_15_geometric_area_to_side_length_square_root,
    arch_16_sum_and_difference_of_two_squares,
    arch_17_square_of_a_sum_misconception_check,
    arch_18_difference_of_squares_evaluation,
    arch_19_calculating_cubes_1_to_6,
    arch_20_calculating_cubes_7_to_10,
    arch_21_cube_root_perfect_cubes_1_to_125,
    arch_22_cube_root_perfect_cubes_216_to_1000,
    arch_23_geometric_volume_to_edge_length_cube_root,
    arch_24_cube_of_multiples_of_ten,
    arch_25_cube_root_of_multiples_of_thousand,
)

from .exponents_archetypes_26_50 import (
    arch_26_product_of_powers_same_base,
    arch_27_quotient_of_powers_same_base,
    arch_28_power_of_a_power,
    arch_29_power_of_a_product,
    arch_30_missing_exponent_product_rule,
    arch_31_missing_exponent_quotient_rule,
    arch_32_missing_base_in_cube_equation,
    arch_33_missing_base_in_square_equation,
    arch_34_equivalence_of_exponential_representations,
    arch_35_addition_of_squares,
    arch_36_square_root_of_sum_vs_sum_of_roots,
    arch_37_multiplication_with_powers,
    arch_38_division_involving_powers,
    arch_39_combined_operations_power_and_subtraction,
    arch_40_brackets_and_square_root,
    arch_41_operations_with_cubes_and_cube_roots,
    arch_42_nested_bracket_power_differences,
    arch_43_writing_numbers_as_powers_of_ten,
    arch_44_expanded_powers_of_ten_reconstruction,
    arch_45_astronomical_distance_powers_of_ten,
    arch_46_comparing_powers_of_ten,
    arch_47_doubling_pattern_exponential_growth,
    arch_48_area_of_square_using_exponents,
    arch_49_side_of_square_from_area_using_roots,
    arch_50_volume_of_cube_using_exponents,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 10: Notation & Concepts of Powers
    arch_01_base_and_exponent_identification,
    arch_02_repeated_multiplication_to_power,
    arch_03_power_expanded_to_repeated_multiplication,
    arch_04_evaluating_small_base_powers,
    arch_05_powers_of_ten_evaluation,
    arch_06_zero_exponent_law,
    arch_07_first_power_identity,
    arch_08_comparing_powers_inequality,
    arch_09_calculating_squares_1_to_15,
    arch_10_calculating_squares_multiples_of_ten,
    # 11 - 20: Squares, Cubes, Square Roots & Cube Roots
    arch_11_square_root_perfect_squares_1_to_144,
    arch_12_square_root_perfect_squares_169_to_400,
    arch_13_square_root_of_multiples_of_hundred,
    arch_14_estimating_square_roots_between_consecutive_integers,
    arch_15_geometric_area_to_side_length_square_root,
    arch_16_sum_and_difference_of_two_squares,
    arch_17_square_of_a_sum_misconception_check,
    arch_18_difference_of_squares_evaluation,
    arch_19_calculating_cubes_1_to_6,
    arch_20_calculating_cubes_7_to_10,
    # 21 - 25: Powers of 10 & Mental Estimation
    arch_21_cube_root_perfect_cubes_1_to_125,
    arch_22_cube_root_perfect_cubes_216_to_1000,
    arch_23_geometric_volume_to_edge_length_cube_root,
    arch_24_cube_of_multiples_of_ten,
    arch_25_cube_root_of_multiples_of_thousand,
    # 26 - 34: Exponent Laws & Power Equations
    arch_26_product_of_powers_same_base,
    arch_27_quotient_of_powers_same_base,
    arch_28_power_of_a_power,
    arch_29_power_of_a_product,
    arch_30_missing_exponent_product_rule,
    arch_31_missing_exponent_quotient_rule,
    arch_32_missing_base_in_cube_equation,
    arch_33_missing_base_in_square_equation,
    arch_34_equivalence_of_exponential_representations,
    # 35 - 42: BODMAS with Powers and Roots
    arch_35_addition_of_squares,
    arch_36_square_root_of_sum_vs_sum_of_roots,
    arch_37_multiplication_with_powers,
    arch_38_division_involving_powers,
    arch_39_combined_operations_power_and_subtraction,
    arch_40_brackets_and_square_root,
    arch_41_operations_with_cubes_and_cube_roots,
    arch_42_nested_bracket_power_differences,
    # 43 - 50: Scientific Notation, Powers of 10 & Geometry Applications
    arch_43_writing_numbers_as_powers_of_ten,
    arch_44_expanded_powers_of_ten_reconstruction,
    arch_45_astronomical_distance_powers_of_ten,
    arch_46_comparing_powers_of_ten,
    arch_47_doubling_pattern_exponential_growth,
    arch_48_area_of_square_using_exponents,
    arch_49_side_of_square_from_area_using_roots,
    arch_50_volume_of_cube_using_exponents,
]

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_base_and_exponent_identification",
    "02_repeated_multiplication_to_power",
    "03_power_expanded_to_repeated_multiplication",
    "04_evaluating_small_base_powers",
    "05_powers_of_ten_evaluation",
    "06_zero_exponent_law",
    "07_first_power_identity",
    "08_comparing_powers_inequality",
    "09_calculating_squares_1_to_15",
    "10_calculating_squares_multiples_of_ten",
    # 11 - 20
    "11_square_root_perfect_squares_1_to_144",
    "12_square_root_perfect_squares_169_to_400",
    "13_square_root_of_multiples_of_hundred",
    "14_estimating_square_roots_between_consecutive_integers",
    "15_geometric_area_to_side_length_square_root",
    "16_sum_and_difference_of_two_squares",
    "17_square_of_a_sum_misconception_check",
    "18_difference_of_squares_evaluation",
    "19_calculating_cubes_1_to_6",
    "20_calculating_cubes_7_to_10",
    # 21 - 25
    "21_cube_root_perfect_cubes_1_to_125",
    "22_cube_root_perfect_cubes_216_to_1000",
    "23_geometric_volume_to_edge_length_cube_root",
    "24_cube_of_multiples_of_ten",
    "25_cube_root_of_multiples_of_thousand",
    # 26 - 34
    "26_product_of_powers_same_base",
    "27_quotient_of_powers_same_base",
    "28_power_of_a_power",
    "29_power_of_a_product",
    "30_missing_exponent_product_rule",
    "31_missing_exponent_quotient_rule",
    "32_missing_base_in_cube_equation",
    "33_missing_base_in_square_equation",
    "34_equivalence_of_exponential_representations",
    # 35 - 42
    "35_addition_of_squares",
    "36_square_root_of_sum_vs_sum_of_roots",
    "37_multiplication_with_powers",
    "38_division_involving_powers",
    "39_combined_operations_power_and_subtraction",
    "40_brackets_and_square_root",
    "41_operations_with_cubes_and_cube_roots",
    "42_nested_bracket_power_differences",
    # 43 - 50
    "43_writing_numbers_as_powers_of_ten",
    "44_expanded_powers_of_ten_reconstruction",
    "45_astronomical_distance_powers_of_ten",
    "46_comparing_powers_of_ten",
    "47_doubling_pattern_exponential_growth",
    "48_area_of_square_using_exponents",
    "49_side_of_square_from_area_using_roots",
    "50_volume_of_cube_using_exponents",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["square_calculation"] = arch_09_calculating_squares_1_to_15
DISPATCH_TABLE["square_root_calculation"] = arch_11_square_root_perfect_squares_1_to_144
DISPATCH_TABLE["cube_calculation"] = arch_19_calculating_cubes_1_to_6
DISPATCH_TABLE["cube_root_calculation"] = arch_21_cube_root_perfect_cubes_1_to_125
DISPATCH_TABLE["combined_powers_roots"] = arch_39_combined_operations_power_and_subtraction
DISPATCH_TABLE["solve_power_equation"] = arch_33_missing_base_in_square_equation


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Exponents Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
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
        q.setdefault("grade", 7)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Exponents")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
