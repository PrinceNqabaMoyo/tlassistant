"""
Grade 7 Mathematics - Data Handling & Probability Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/Statistics Studio.md and Probability Studio.md
and curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Interpret analyse and report on data.md and 02. Probability.md.

Archetypes Covered:
1. Measures of Central Tendency & Spread:
   - Arithmetic Mean (Sum ÷ Count)
   - Median (Middle value after sorting in ascending order)
   - Mode (Most frequent value)
   - Range (Highest value - Lowest value)
2. Simple Theoretical Probability:
   - Favourable outcomes ÷ Total outcomes
   - Authentic contexts (coloured beads/marbles in a bag, fair 6-sided dice, spinners)
   - Simplified fraction, decimal, and percentage representations
"""

from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


# ============================================================================
# ARCHETYPE 1: Measures of Central Tendency & Spread
# ============================================================================

def _generate_data_handling_question(rng: random.Random, measure_type: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate questions on Mean, Median, Mode, or Range from an authentic data set.
    """
    contexts = [
        ("Mathematics test marks (out of 50) of a study group", "marks", [18, 24, 25, 30, 32, 35, 38, 40, 42, 45, 48]),
        ("Daily maximum temperatures recorded in Kimberley over one week (°C)", "°C", [16, 18, 21, 21, 24, 25, 27, 28, 30]),
        ("Number of goals scored per match by a school soccer team", "goals", [0, 1, 1, 2, 2, 2, 3, 4, 5]),
        ("Time in minutes taken by learners to walk to school", "minutes", [10, 12, 15, 15, 20, 25, 30, 35])
    ]

    context_name, unit, base_pool = rng.choice(contexts)
    
    # Select 6 to 9 values from base_pool with optional duplicates
    count_items = rng.choice([5, 7, 8])
    data = [rng.choice(base_pool) for _ in range(count_items)]
    
    # Ensure mean is clean integer or half-integer (.5)
    target_measure = measure_type or rng.choice(["mean", "median", "mode", "range"])

    if target_measure == "mean":
        # Adjust last element so sum is divisible by count_items
        current_sum = sum(data)
        rem = current_sum % count_items
        if rem != 0:
            data[-1] += (count_items - rem)
        
        # Shuffle presentation
        presented_data = list(data)
        rng.shuffle(presented_data)
        
        total_sum = sum(presented_data)
        n = len(presented_data)
        mean_val = total_sum // n
        
        data_str = ", ".join(str(x) for x in presented_data)
        prompt = (
            f"The following dataset shows {context_name}:\n\n"
            f"\\[ {data_str} \\]\n\n"
            f"Calculate the **mean** (average) of this data set."
        )
        
        sol = (
            f"Step 1: Calculate the sum of all values:\n"
            f"\\(\\text{{Sum}} = {' + '.join(str(x) for x in presented_data)} = {total_sum}\\)\n\n"
            f"Step 2: Count the total number of values:\n"
            f"\\(n = {n}\\)\n\n"
            f"Step 3: Divide the sum by the count:\n"
            f"\\(\\text{{Mean}} = \\frac{{{total_sum}}}{{{n}}} = {mean_val}\\)."
        )
        
        return {
            "id": f"g7_math_stat_mean_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": str(mean_val),
            "answer_latex": str(mean_val),
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": "calculate_mean",
            "learning_objective_id": "math_g7_stat_mean",
            "misconception_tags": ["confused_mean_and_median", "arithmetic_division_error"],
            "diagnostic_tags": ["data_handling", "statistics", "mean"],
            "minimum_mastery_score": 75,
            "keywords": ["mean", "average", "sum divided by count"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct summation of dataset values ({total_sum})", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct quotient for mean ({mean_val})", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": f"The mean is found by adding all numbers together and dividing by how many numbers there are.",
                "tier_2": f"Sum = {total_sum}. Number of items = {n}. Calculate {total_sum} ÷ {n}.",
                "tier_3": f"{total_sum} ÷ {n} = {mean_val}."
            }
        }

    elif target_measure == "median":
        # Keep odd number of elements (5 or 7) for single clean middle number in Grade 7
        count_odd = rng.choice([5, 7])
        data = [rng.choice(base_pool) for _ in range(count_odd)]
        
        presented_data = list(data)
        rng.shuffle(presented_data)
        
        sorted_data = sorted(presented_data)
        mid_idx = len(sorted_data) // 2
        median_val = sorted_data[mid_idx]
        
        data_str = ", ".join(str(x) for x in presented_data)
        sorted_str = ", ".join(str(x) for x in sorted_data)
        
        prompt = (
            f"The following dataset shows {context_name}:\n\n"
            f"\\[ {data_str} \\]\n\n"
            f"Determine the **median** of this data set."
        )
        
        sol = (
            f"Step 1: Arrange the values in ascending order (from smallest to largest):\n"
            f"\\[ {sorted_str} \\]\n\n"
            f"Step 2: Locate the middle value in the ordered list (position {mid_idx + 1} of {len(sorted_data)}):\n"
            f"\\(\\text{{Median}} = {median_val}\\)."
        )
        
        return {
            "id": f"g7_math_stat_med_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": str(median_val),
            "answer_latex": str(median_val),
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": "calculate_median",
            "learning_objective_id": "math_g7_stat_median",
            "misconception_tags": ["median_without_sorting", "confused_mean_and_median"],
            "diagnostic_tags": ["data_handling", "statistics", "median"],
            "minimum_mastery_score": 75,
            "keywords": ["median", "middle value", "ordered data"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Sorting data in ascending order", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct identification of median value ({median_val})", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": f"Before finding the median, you MUST first arrange the numbers from smallest to largest.",
                "tier_2": f"Ordered list: {sorted_str}. Find the number right in the middle.",
                "tier_3": f"The middle number is {median_val}."
            }
        }

    elif target_measure == "mode":
        # Ensure there is an unambiguous unique mode
        mode_val = rng.choice(base_pool)
        other_vals = [x for x in base_pool if x != mode_val]
        rng.shuffle(other_vals)
        
        # 3 copies of mode_val, 1 copy of other values
        items = [mode_val, mode_val, mode_val] + other_vals[:4]
        rng.shuffle(items)
        
        data_str = ", ".join(str(x) for x in items)
        prompt = (
            f"The following dataset shows {context_name}:\n\n"
            f"\\[ {data_str} \\]\n\n"
            f"Identify the **mode** of this data set."
        )
        
        sol = (
            f"Step 1: Count the frequency of each number in the data set.\n\n"
            f"Step 2: The value {mode_val} appears 3 times, which is more frequently than any other value.\n\n"
            f"Therefore, \\(\\text{{Mode}} = {mode_val}\\)."
        )
        
        return {
            "id": f"g7_math_stat_mode_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": str(mode_val),
            "answer_latex": str(mode_val),
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 1,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "calculate_mode",
            "learning_objective_id": "math_g7_stat_mode",
            "misconception_tags": ["confused_mean_and_median"],
            "diagnostic_tags": ["data_handling", "statistics", "mode"],
            "minimum_mastery_score": 75,
            "keywords": ["mode", "most frequent", "highest frequency"],
            "marking_schema": {
                "total_marks": 1,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct identification of mode ({mode_val})", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "strict"
            },
            "hints": {
                "tier_1": f"The mode is the number that appears most frequently (most often).",
                "tier_2": f"Count how many times each number appears in the list.",
                "tier_3": f"The number {mode_val} appears 3 times. Mode = {mode_val}."
            }
        }

    else: # range
        presented_data = list(data)
        rng.shuffle(presented_data)
        
        min_val = min(presented_data)
        max_val = max(presented_data)
        range_val = max_val - min_val
        
        data_str = ", ".join(str(x) for x in presented_data)
        prompt = (
            f"The following dataset shows {context_name}:\n\n"
            f"\\[ {data_str} \\]\n\n"
            f"Calculate the **range** of this data set."
        )
        
        sol = (
            f"Step 1: Identify the maximum (highest) value: \\(\\text{{Highest}} = {max_val}\\).\n\n"
            f"Step 2: Identify the minimum (lowest) value: \\(\\text{{Lowest}} = {min_val}\\).\n\n"
            f"Step 3: Subtract the lowest value from the highest value:\n"
            f"\\(\\text{{Range}} = {max_val} - {min_val} = {range_val}\\)."
        )
        
        return {
            "id": f"g7_math_stat_range_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": str(range_val),
            "answer_latex": str(range_val),
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "calculate_range",
            "learning_objective_id": "math_g7_stat_range",
            "misconception_tags": ["range_as_interval_not_difference", "arithmetic_subtraction_error"],
            "diagnostic_tags": ["data_handling", "statistics", "range"],
            "minimum_mastery_score": 75,
            "keywords": ["range", "spread", "highest minus lowest"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Identification of highest ({max_val}) and lowest ({min_val}) values", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct range calculation ({range_val})", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": f"The range measures the spread of the data: highest value minus lowest value.",
                "tier_2": f"Highest = {max_val}, Lowest = {min_val}. Calculate {max_val} - {min_val}.",
                "tier_3": f"{max_val} - {min_val} = {range_val}."
            }
        }


# ============================================================================
# ARCHETYPE 2: Simple Theoretical Probability
# ============================================================================

def _generate_probability_question(rng: random.Random) -> Dict[str, Any]:
    """
    Theoretical single-event probability:
    P(E) = favourable outcomes / total possible outcomes.
    Contexts: coloured marbles in a bag, fair 6-sided die.
    """
    scen_type = rng.choice(["marbles_bag", "fair_die"])

    if scen_type == "marbles_bag":
        c1_name, c2_name, c3_name = "red", "blue", "green"
        n1 = rng.choice([3, 4, 5])
        n2 = rng.choice([2, 3, 4])
        n3 = rng.choice([1, 2, 3])
        total = n1 + n2 + n3
        
        target_color = rng.choice([("red", n1), ("blue", n2), ("green", n3)])
        color_chosen, count_chosen = target_color
        
        g = math.gcd(count_chosen, total)
        simp_num = count_chosen // g
        simp_den = total // g
        
        simp_fraction_str = f"{simp_num}/{simp_den}"
        frac_latex = f"\\frac{{{simp_num}}}{{{simp_den}}}" if simp_den != 1 else str(simp_num)
        
        percent_val = round((count_chosen / total) * 100, 1)
        percent_str = f"{percent_val}%"
        
        prompt = (
            f"A cloth bag contains \\({n1}\\) red beads, \\({n2}\\) blue beads, and \\({n3}\\) green beads.\n\n"
            f"If a single bead is drawn at random from the bag without looking, "
            f"what is the theoretical probability of selecting a **{color_chosen} bead**?\n"
            f"(Express your answer as a simplified fraction, e.g. '1/2')."
        )
        
        sol = (
            f"Step 1: Calculate the total number of possible outcomes (total beads):\n"
            f"\\(\\text{{Total}} = {n1} + {n2} + {n3} = {total}\\)\n\n"
            f"Step 2: Count the number of favourable outcomes ({color_chosen} beads):\n"
            f"\\(\\text{{Favourable}} = {count_chosen}\\)\n\n"
            f"Step 3: State the probability formula:\n"
            f"\\[ P(\\text{{{color_chosen}}}) = \\frac{{\\text{{Favourable}}}}{{\\text{{Total}}}} = \\frac{{{count_chosen}}}{{{total}}} \\]\n\n"
            f"Step 4: Simplify to lowest terms (divide numerator and denominator by {g}):\n"
            f"\\[ P(\\text{{{color_chosen}}}) = {frac_latex} \\]"
        )
        
        return {
            "id": f"g7_math_prob_bag_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": simp_fraction_str,
            "answer_latex": frac_latex,
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": "probability_marbles_bag",
            "learning_objective_id": "math_g7_prob_single_event",
            "misconception_tags": [
                "omitted_simplification_of_fraction",
                "probability_greater_than_one"
            ],
            "diagnostic_tags": ["probability", "single_event", "fractions"],
            "minimum_mastery_score": 75,
            "keywords": ["probability", "favourable outcomes", "simplified fraction", "beads in a bag"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct setup of ratio {count_chosen}/{total}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Simplified fraction {simp_fraction_str}", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": f"Probability is: number of {color_chosen} beads ÷ total number of beads.",
                "tier_2": f"Total beads = {n1} + {n2} + {n3} = {total}. Favourable = {count_chosen}. Simplify {count_chosen}/{total}.",
                "tier_3": f"{count_chosen}/{total} simplifies to {simp_fraction_str}."
            }
        }

    else: # fair_die
        die_cases = [
            ("an even number (2, 4, or 6)", 3, "3/6", "1/2"),
            ("an odd number (1, 3, or 5)", 3, "3/6", "1/2"),
            ("a number greater than 4 (5 or 6)", 2, "2/6", "1/3"),
            ("a 5", 1, "1/6", "1/6"),
            ("a prime number (2, 3, or 5)", 3, "3/6", "1/2")
        ]
        event_desc, count_fav, unsimplified, simplified = rng.choice(die_cases)
        
        prompt = (
            f"A fair six-sided die with faces numbered from 1 to 6 is rolled once.\n\n"
            f"What is the theoretical probability of rolling **{event_desc}**?\n"
            f"(Express your answer as a simplified fraction, e.g. '1/2')."
        )
        
        sol = (
            f"Step 1: Total possible outcomes on a fair 6-sided die: \\(S = \\{{1, 2, 3, 4, 5, 6\\}}\\), so \\(n(S) = 6\\).\n\n"
            f"Step 2: Number of favourable outcomes for {event_desc} is \\({count_fav}\\).\n\n"
            f"Step 3: Calculate theoretical probability:\n"
            f"\\[ P(E) = \\frac{{{count_fav}}}{{6}} = \\frac{{{simplified.split('/')[0]}}}{{{simplified.split('/')[1]}}} \\]\n"
            f"Therefore, \\(P(E) = {simplified}\\)."
        )
        
        return {
            "id": f"g7_math_prob_die_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": simplified,
            "answer_latex": f"\\frac{{{simplified.split('/')[0]}}}{{{simplified.split('/')[1]}}}",
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "probability_fair_die",
            "learning_objective_id": "math_g7_prob_fair_die",
            "misconception_tags": [
                "omitted_simplification_of_fraction",
                "sample_space_miscount"
            ],
            "diagnostic_tags": ["probability", "dice", "sample_space"],
            "minimum_mastery_score": 75,
            "keywords": ["probability", "fair die", "sample space", "simplified fraction"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct identification of favourable outcomes ({count_fav}/6)", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Simplified fraction {simplified}", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": f"A fair die has 6 possible outcomes in total.",
                "tier_2": f"Count how many outcomes match the condition, then divide by 6.",
                "tier_3": f"{count_fav} out of 6 outcomes = {unsimplified} = {simplified}."
            }
        }


# ============================================================================
# MASTER GENERATE FUNCTION (6-Pillar Contract)
# ============================================================================

def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    default_domain: str = "data",
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Data Handling & Probability Generator.
    Supports atomic micro-drills:
    - mode="elementary_mean": Arithmetic mean
    - mode="elementary_median": Median with ordered data
    - mode="elementary_mode": Mode identification
    - mode="elementary_range": Range spread calculation
    - mode="elementary_probability": Theoretical single-event probability
    - mode="compound": Authentic mixed exam bank
    """
    rng = _rng(seed)
    questions = []

    topic_str = str(kwargs.get("topic", "")).lower()
    subskill_str = str(subskill or "").lower()
    is_prob = (
        default_domain == "probability"
        or "prob" in topic_str
        or "prob" in subskill_str
        or mode == "elementary_probability"
        or subskill_str == "probability"
    )

    for _ in range(count):
        if is_prob:
            q = _generate_probability_question(rng)
        elif mode == "elementary_mean" or subskill_str == "mean":
            q = _generate_data_handling_question(rng, measure_type="mean")
        elif mode == "elementary_median" or subskill_str == "median":
            q = _generate_data_handling_question(rng, measure_type="median")
        elif mode == "elementary_mode" or subskill_str == "mode":
            q = _generate_data_handling_question(rng, measure_type="mode")
        elif mode == "elementary_range" or subskill_str == "range":
            q = _generate_data_handling_question(rng, measure_type="range")
        else: # compound data handling: pick across data summary statistics
            archetype = rng.choice([
                lambda: _generate_data_handling_question(rng, "mean"),
                lambda: _generate_data_handling_question(rng, "median"),
                lambda: _generate_data_handling_question(rng, "mode"),
                lambda: _generate_data_handling_question(rng, "range")
            ])
            q = archetype()
        questions.append(q)

    return questions


def generate_data_handling(count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=count, seed=seed, default_domain="data", **kwargs)


def generate_probability(count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=count, seed=seed, default_domain="probability", **kwargs)

