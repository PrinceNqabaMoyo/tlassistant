"""Grade 12 Mathematics - Sequences and Series Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/01. Sequences and series.md.

Covers:
  - Arithmetic Sequences and Series: Tn = a + (n - 1)d, Sn = n/2 * [2a + (n - 1)d].
  - Geometric Sequences and Series: Tn = a * r^(n - 1), Sn = a * (r^n - 1) / (r - 1).
  - Infinite Geometric Series: S_inf = a / (1 - r) for -1 < r < 1, recurring decimals.
  - Sigma Notation evaluation: finite arithmetic/geometric and infinite series.
  - Applied problems: bouncing ball, seating arrangements, fractals, proofs.

Strictly zero-LLM, deterministic execution with 50 distinct semantic archetypes.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .sequences_series_archetypes_01_25 import BUILDERS_01_25
from .sequences_series_archetypes_26_50 import BUILDERS_26_50

# Merge all 50 builders
ALL_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
ALL_BUILDERS.update(BUILDERS_01_25)
ALL_BUILDERS.update(BUILDERS_26_50)

ORDERED_SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())

SUBSKILLS: Dict[str, str] = {
    # 01 - 25
    "01_arithmetic_common_diff_and_next_terms": "Arithmetic Common Difference & Next Terms",
    "02_arithmetic_general_term_formula": "Arithmetic General Term Formula Tn = dn + c",
    "03_arithmetic_find_specific_term": "Calculating Specific Term Tk in Arithmetic Sequence",
    "04_arithmetic_find_term_position": "Determining Term Position n in Arithmetic Sequence",
    "05_arithmetic_solve_unknown_terms_linear": "Solving for Unknown Variable x in Arithmetic Sequence",
    "06_arithmetic_solve_simultaneous_a_and_d": "Solving Simultaneous Equations for Arithmetic a and d",
    "07_arithmetic_negative_terms_first_negative": "First Negative Term in Decreasing Arithmetic Sequence",
    "08_arithmetic_between_multiples_count": "Counting Multiples within Interval",
    "09_geometric_common_ratio_and_next_terms": "Geometric Common Ratio & Next Terms",
    "10_geometric_general_term_formula": "Geometric General Term Formula Tn = a*r^(n-1)",
    "11_geometric_find_specific_term": "Calculating Specific Term Tk in Geometric Sequence",
    "12_geometric_find_term_position_log": "Finding Geometric Term Position via Logarithms",
    "13_geometric_solve_unknown_terms_ratio": "Solving for Unknown Variable x in Geometric Sequence",
    "14_geometric_solve_simultaneous_a_and_r": "Solving Simultaneous Equations for Geometric a and r",
    "15_geometric_alternating_signs_analysis": "Alternating Geometric Sequences & Sign Parity",
    "16_arithmetic_mean_insertion": "Inserting Arithmetic Means Between Two Numbers",
    "17_geometric_mean_insertion": "Inserting Geometric Means Between Two Numbers",
    "18_series_definition_partial_sums": "Partial Sums S1..S4 of a Sequence",
    "19_term_from_sum_formula_tn_sn_sn_minus_1": "Determining Tn from Sn Formula via Subtraction",
    "20_arithmetic_series_sum_formula_basic": "Sum of First n Terms of Arithmetic Series",
    "21_arithmetic_series_sum_with_last_term": "Arithmetic Series Sum Using First and Last Terms",
    "22_arithmetic_series_solve_for_n_quadratic": "Solving for Number of Terms n in Arithmetic Series",
    "23_arithmetic_sum_multiples_in_range": "Sum of Multiples in a Range",
    "24_arithmetic_sum_multiples_excluding_others": "Sum of Filtered Multiples in a Range",
    "25_arithmetic_series_word_problem_savings": "Applied Arithmetic Series Word Problem (Savings)",
    # 26 - 50
    "26_geometric_series_sum_formula_basic": "Sum of First n Terms of Geometric Series",
    "27_geometric_series_solve_for_n_log": "Solving for Number of Terms n in Geometric Series",
    "28_sum_to_infinity_condition_for_convergence": "Convergence Condition -1 < r < 1 for Infinite Series",
    "29_sum_to_infinity_calculation": "Calculating Sum to Infinity S_infinity = a / (1 - r)",
    "30_recurring_decimal_to_fraction_geometric": "Converting Recurring Decimals to Fractions via Series",
    "31_infinite_geometric_solve_for_first_term_or_ratio": "Solving for First Term or Ratio from S_infinity",
    "32_sigma_notation_arithmetic_basic": "Evaluating Arithmetic Sigma Notation Sum",
    "33_sigma_notation_arithmetic_non_unit_start": "Arithmetic Sigma Sum with Non-Unit Start Index",
    "34_sigma_notation_geometric_basic": "Evaluating Geometric Sigma Notation Sum",
    "35_sigma_notation_geometric_non_unit_start": "Geometric Sigma Sum with Non-Unit Start Index",
    "36_sigma_notation_infinite_series": "Evaluating Infinite Geometric Sigma Notation Series",
    "37_sigma_notation_solve_upper_limit_arithmetic": "Solving for Upper Limit n in Arithmetic Sigma Sum",
    "38_sigma_notation_solve_upper_limit_geometric": "Solving for Upper Limit n in Geometric Sigma Sum",
    "39_write_series_in_sigma_notation": "Expressing an Explicit Series in Sigma Notation",
    "40_split_sigma_notation_addition": "Splitting Mixed Arithmetic-Geometric Sigma Sum",
    "41_mixed_sequence_alternating_arithmetic_geometric": "Interlaced Mixed Arithmetic-Geometric Sequences",
    "42_quadratic_pattern_first_second_differences": "Quadratic Sequence General Term and Second Difference",
    "43_quadratic_pattern_find_term_position": "Finding Term Position in a Quadratic Sequence",
    "44_geometric_bouncing_ball_total_distance": "Applied Bouncing Ball Infinite Vertical Distance",
    "45_geometric_fractal_perimeter_area_svg": "Geometric Fractal Area Pattern (Nested Squares)",
    "46_arithmetic_pattern_seating_tiles_svg": "Applied Linear Pattern (Desks and Seats)",
    "47_geometric_decay_halflife_or_depreciation": "Applied Geometric Decay and Depreciation",
    "48_series_proof_arithmetic_sn": "Algebraic Proof of Arithmetic Sum Formula Sn",
    "49_series_proof_geometric_sn": "Algebraic Proof of Geometric Sum Formula Sn",
    "50_compound_nsc_exam_multi_step_sequences": "Comprehensive Compound Examination Sequences Problem",
}

# Legacy aliases backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "arithmetic_series_sum": "20_arithmetic_series_sum_formula_basic",
    "geometric_series_sum": "26_geometric_series_sum_formula_basic",
    "sum_to_infinity_convergence": "28_sum_to_infinity_condition_for_convergence",
    "sigma_notation": "32_sigma_notation_arithmetic_basic",
    "arithmetic_series": "20_arithmetic_series_sum_formula_basic",
    "geometric_series": "26_geometric_series_sum_formula_basic",
    "elementary_arithmetic": "20_arithmetic_series_sum_formula_basic",
    "elementary_geometric": "26_geometric_series_sum_formula_basic",
    "elementary_convergence": "29_sum_to_infinity_calculation",
}


def _resolve_builder(subskill: Optional[str]) -> Callable[[random.Random], Dict[str, Any]]:
    if not subskill or subskill in ("all", "sequences_series"):
        key = random.choice(ORDERED_SUBSKILLS)
        return ALL_BUILDERS[key]
    if subskill in ALL_BUILDERS:
        return ALL_BUILDERS[subskill]
    if subskill in LEGACY_ALIASES:
        return ALL_BUILDERS[LEGACY_ALIASES[subskill]]
    # Substring matching fallback
    low = subskill.lower()
    for k in ORDERED_SUBSKILLS:
        if low in k.lower():
            return ALL_BUILDERS[k]
    return ALL_BUILDERS[ORDERED_SUBSKILLS[0]]


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions satisfying the 6-pillar contract."""
    base_seed = seed if seed is not None else random.randint(1000, 999999)
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        rng = random.Random(base_seed + i)
        builder = _resolve_builder(subskill)
        q = builder(rng)
        questions.append(q)

    return questions


def generate_grade12_sequences_series_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Legacy entrypoint single question generator."""
    target_sub = subskill if subskill else (mode if mode.startswith("elementary_") else None)
    qs = generate(subskill=target_sub, count=1, seed=seed, difficulty=difficulty, mode=mode)
    return qs[0]
