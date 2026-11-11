"""
Grade 8 Mathematics - Common Fractions Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs/Mathematics_Gr8/Numbers-Operations-and-Relationships Studio.md (Term 3 Common Fractions).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .common_fractions_archetypes_01_25 import (
    BUILDERS_01_25,
    arch_01_simplifying_fraction_hcf,
    arch_02_equivalent_fractions_missing_numerator,
    arch_03_equivalent_fractions_missing_denominator,
    arch_04_converting_improper_fraction_to_mixed_number,
    arch_05_converting_mixed_number_to_improper_fraction,
    arch_06_comparing_fractions_common_denominator,
    arch_07_ordering_three_fractions_ascending,
    arch_08_fraction_of_whole_number_quantity,
    arch_09_fraction_of_measurement_unit_conversion,
    arch_10_addition_like_denominators_proper,
    arch_11_addition_unlike_denominators_multiples,
    arch_12_addition_unlike_denominators_coprime,
    arch_13_addition_three_fractions_lcd,
    arch_14_addition_mixed_numbers_unlike_denominators,
    arch_15_subtraction_like_denominators,
    arch_16_subtraction_unlike_denominators,
    arch_17_subtraction_from_whole_number,
    arch_18_subtraction_mixed_numbers_with_borrowing,
    arch_19_multiplication_fraction_by_whole_number,
    arch_20_multiplication_two_proper_fractions,
    arch_21_multiplication_three_fractions_cross_cancel,
    arch_22_multiplication_mixed_numbers,
    arch_23_reciprocal_of_fraction_and_mixed_number,
    arch_24_division_whole_number_by_fraction,
    arch_25_division_fraction_by_whole_number,
)
from .common_fractions_archetypes_26_50 import (
    BUILDERS_26_50,
    arch_26_division_two_proper_fractions,
    arch_27_division_mixed_numbers,
    arch_28_squaring_proper_fraction,
    arch_29_squaring_mixed_number,
    arch_30_cubing_proper_fraction,
    arch_31_square_root_of_proper_fraction,
    arch_32_square_root_of_mixed_number,
    arch_33_cube_root_of_proper_fraction,
    arch_34_cube_root_of_mixed_number,
    arch_35_bodmas_brackets_and_addition,
    arch_36_bodmas_multiplication_before_addition,
    arch_37_bodmas_division_before_subtraction,
    arch_38_bodmas_powers_and_operations,
    arch_39_bodmas_roots_and_operations,
    arch_40_word_problem_fraction_of_pocket_money_spent,
    arch_41_word_problem_fractional_sharing_recipe,
    arch_42_word_problem_journey_fraction_remaining,
    arch_43_word_problem_cutting_ribbon_division,
    arch_44_converting_fraction_to_percentage,
    arch_45_converting_percentage_to_simplest_fraction,
    arch_46_diagnosing_fraction_addition_denominator_error,
    arch_47_diagnosing_fraction_division_inversion_error,
    arch_48_diagnosing_mixed_number_squaring_error,
    arch_49_complex_fraction_stacked_division,
    arch_50_common_fractions_capstone_synthesis,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = BUILDERS_01_25 + BUILDERS_26_50

SUBSKILLS: List[str] = [
    # 01 - 10
    "01_simplifying_fraction_hcf",
    "02_equivalent_fractions_missing_numerator",
    "03_equivalent_fractions_missing_denominator",
    "04_converting_improper_fraction_to_mixed_number",
    "05_converting_mixed_number_to_improper_fraction",
    "06_comparing_fractions_common_denominator",
    "07_ordering_three_fractions_ascending",
    "08_fraction_of_whole_number_quantity",
    "09_fraction_of_measurement_unit_conversion",
    "10_addition_like_denominators_proper",
    # 11 - 20
    "11_addition_unlike_denominators_multiples",
    "12_addition_unlike_denominators_coprime",
    "13_addition_three_fractions_lcd",
    "14_addition_mixed_numbers_unlike_denominators",
    "15_subtraction_like_denominators",
    "16_subtraction_unlike_denominators",
    "17_subtraction_from_whole_number",
    "18_subtraction_mixed_numbers_with_borrowing",
    "19_multiplication_fraction_by_whole_number",
    "20_multiplication_two_proper_fractions",
    # 21 - 30
    "21_multiplication_three_fractions_cross_cancel",
    "22_multiplication_mixed_numbers",
    "23_reciprocal_of_fraction_and_mixed_number",
    "24_division_whole_number_by_fraction",
    "25_division_fraction_by_whole_number",
    "26_division_two_proper_fractions",
    "27_division_mixed_numbers",
    "28_squaring_proper_fraction",
    "29_squaring_mixed_number",
    "30_cubing_proper_fraction",
    # 31 - 40
    "31_square_root_of_proper_fraction",
    "32_square_root_of_mixed_number",
    "33_cube_root_of_proper_fraction",
    "34_cube_root_of_mixed_number",
    "35_bodmas_brackets_and_addition",
    "36_bodmas_multiplication_before_addition",
    "37_bodmas_division_before_subtraction",
    "38_bodmas_powers_and_operations",
    "39_bodmas_roots_and_operations",
    "40_word_problem_fraction_of_pocket_money_spent",
    # 41 - 50
    "41_word_problem_fractional_sharing_recipe",
    "42_word_problem_journey_fraction_remaining",
    "43_word_problem_cutting_ribbon_division",
    "44_converting_fraction_to_percentage",
    "45_converting_percentage_to_simplest_fraction",
    "46_diagnosing_fraction_addition_denominator_error",
    "47_diagnosing_fraction_division_inversion_error",
    "48_diagnosing_mixed_number_squaring_error",
    "49_complex_fraction_stacked_division",
    "50_common_fractions_capstone_synthesis",
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
        q.setdefault("topic", "Common fractions")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
