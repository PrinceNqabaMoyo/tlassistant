"""Grade 8 Mathematics — Probability Archetypes (26 to 50).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/03. Probability.md

Archetypes covered:
  26. Complementary events: Sum to one rule (P(E) + P(not E) = 1).
  27. Weather forecasts: Percentage chance of precipitation and non-precipitation.
  28. Two coins: Sample space tree diagram (WITH SVG).
  29. Two coins: Probability of exactly one Head (HT, TH -> 2/4 = 1/2).
  30. Two coins: Probability of at least one Tail (3/4).
  31. Coin and dice: Compound sample space of 12 combined outcomes (WITH SVG).
  32. Coin and dice: Probability of Heads and an even number (3/12 = 1/4).
  33. Coin and dice: Probability of Tails and a prime number (3/12 = 1/4).
  34. Two dice: Two-way table listing all 36 sum outcomes (WITH TABLE).
  35. Two dice: Probability that sum of numbers equals 7 (6/36 = 1/6).
  36. Two dice: Probability that sum of numbers is greater than 9 (6/36 = 1/6).
  37. Two dice: Probability of rolling doubles (matching numbers) (6/36 = 1/6).
  38. Two dice: Probability of an absolute difference between numbers.
  39. Two dice: Fairness analysis of a sum-based two-player game.
  40. Two spinners: Combined outcomes two-way grid (WITH TABLE).
  41. Consecutive draws: Independent events with replacement (WITH SVG).
  42. Consecutive draws: Dependent events without replacement fraction changes.
  43. Independent events: Multiplication rule P(A and B) = P(A) * P(B).
  44. Prediction: Expected number of times an event occurs in N trials (Expected = N * P).
  45. Two-way frequency table: Survey data probability (WITH TABLE).
  46. Two-way frequency table: Conditional frequency within a specified demographic row/column.
  47. Quality control: Probability of selecting a defective item from production batch.
  48. Error analysis: The Gambler's Fallacy (prior independent coin flips do not affect the next).
  49. Error analysis: Treating ordered outcomes (HT vs TH) as a single unordered outcome.
  50. Word problem: School raffle tickets prize probability and fundraising analysis.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .probability_svg import (
    draw_coin_and_dice_tree_svg,
    draw_tree_diagram_two_coins_svg,
)


def _fmt_dec(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 26. Complementary Events: Sum to One Rule
# ----------------------------------------------------------------------
def arch_26_complementary_events_sum_to_one_rule(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([25, 35, 40, 65, 75, 80])
    p_e = pct / 100.0
    p_comp = 1.0 - p_e
    p_comp_pct = 100 - pct

    prompt = (
        f"In a probability experiment, the probability of an event \\(E\\) occurring is \\({pct}\\%\\) "
        f"(\\({_fmt_dec(p_e)}\\)).\n\n"
        f"1. State the mathematical rule relating an event \\(E\\) and its complement \\(\\text{{not }} E\\).\n"
        f"2. Calculate the probability that the event \\(E\\) will NOT occur, expressing your answer as a decimal and as a percentage."
    )
    sol = (
        f"**Complementary Events Principle:**\n"
        f"1. An event and its complement are mutually exclusive and together cover the entire sample space:\n"
        f"\\[ P(E) + P(\\text{{not }} E) = 1 \\implies P(\\text{{not }} E) = 1 - P(E) \\]\n\n"
        f"2. Calculation:\n"
        f"\\[ P(\\text{{not }} E) = 1 - {_fmt_dec(p_e)} = {_fmt_dec(p_comp)} = {p_comp_pct}\\% \\]"
    )
    ans = f"1. P(E) + P(not E) = 1; 2. {_fmt_dec(p_comp)} ({p_comp_pct}%)"
    return {
        "id": f"g8_prob_comp_rule_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_complementary_events_sum_to_one_rule",
        "learning_objective_id": "math_g8_prob_comp_rule",
        "hints": {
            "tier_1": "The sum of the probabilities of all complementary outcomes is always 1 (100%).",
            "tier_2": f"Subtract {pct}% from 100%.",
            "tier_3": f"{_fmt_dec(p_comp)} ({p_comp_pct}%).",
        },
        "misconception_tags": ["forgetting_that_probabilities_sum_to_one"],
    }


# ----------------------------------------------------------------------
# 27. Weather Forecasts: Probability of Rain and No Rain
# ----------------------------------------------------------------------
def arch_27_weather_forecast_percentage_precipitation_probability(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Durban", "Johannesburg", "Cape Town", "Polokwane", "Gqeberha"])
    rain_pct = rng.choice([30, 40, 60, 70, 80])
    no_rain_pct = 100 - rain_pct
    dec_val = _fmt_dec(rain_pct / 100.0)

    prompt = (
        f"A South African Weather Service forecast states that there is an **{rain_pct}% chance of rain** "
        f"in {city} tomorrow.\n\n"
        f"1. Express the probability of rain tomorrow as a decimal and as a common fraction in simplest form.\n"
        f"2. Calculate the probability that it will NOT rain in {city} tomorrow as a percentage."
    )
    gcd = math.gcd(rain_pct, 100)
    sim_num = rain_pct // gcd
    sim_den = 100 // gcd

    sol = (
        f"**Weather Forecast Analysis:**\n"
        f"1. Probability of rain:\n"
        f"- Decimal: \\(\\frac{{{rain_pct}}}{{100}} = {dec_val}\\)\n"
        f"- Simplified fraction: \\(\\frac{{{rain_pct}}}{{100}} = \\frac{{{sim_num}}}{{{sim_den}}}\\)\n\n"
        f"2. Probability of NO rain:\n"
        f"\\[ P(\\text{{no rain}}) = 100\\% - {rain_pct}\\% = {no_rain_pct}\\% \\]"
    )
    ans = f"1. {dec_val} (or {sim_num}/{sim_den}); 2. {no_rain_pct}%"
    return {
        "id": f"g8_prob_weather_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "27_weather_forecast_percentage_precipitation_probability",
        "learning_objective_id": "math_g8_prob_weather",
        "hints": {
            "tier_1": f"Divide {rain_pct} by 100 for decimal and fraction.",
            "tier_2": f"Complementary probability = 100% - {rain_pct}%.",
            "tier_3": ans,
        },
        "misconception_tags": ["misinterpreting_percentage_of_precipitation"],
    }


# ----------------------------------------------------------------------
# 28. Two Coins: Sample Space Tree Diagram (WITH SVG)
# ----------------------------------------------------------------------
def arch_28_two_coins_sample_space_tree_diagram(rng: random.Random) -> Dict[str, Any]:
    svg = draw_tree_diagram_two_coins_svg(seed=rng.randint(100, 999999))

    prompt = (
        "Two fair coins are flipped simultaneously in a compound probability experiment.\n\n"
        "1. List all the outcomes in the compound sample space using ordered pairs (e.g. (H, H)).\n"
        "2. State the total number of equally likely outcomes \\(n(S)\\).\n"
        "3. What is the theoretical probability of obtaining any single specific pair of outcomes?"
    )
    sol = (
        "**Two-Coin Compound Event:**\n"
        "1. Complete sample space: \\(S = \\{{(H, H), (H, T), (T, H), (T, T)\\}}\\)\n"
        "2. Total outcomes: \\(n(S) = 4\\)\n"
        "3. Each branch has probability \\(\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4} = 0{,}25 = 25\\%\\)."
    )
    ans = "1. S = {(H, H), (H, T), (T, H), (T, T)}; 2. n(S) = 4; 3. 1/4 (25%)"
    return {
        "id": f"g8_prob_two_coins_tree_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "28_two_coins_sample_space_tree_diagram",
        "learning_objective_id": "math_g8_prob_two_coins_tree",
        "hints": {
            "tier_1": "There are 2 outcomes for coin 1 and 2 for coin 2: 2 × 2 = 4.",
            "tier_2": "List: (H, H), (H, T), (T, H), (T, T).",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_there_are_only_3_outcomes_by_treating_ht_and_th_as_one"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 29. Two Coins: Probability Exactly One Head
# ----------------------------------------------------------------------
def arch_29_two_coins_probability_exactly_one_head(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair coins are tossed.\n\n"
        "1. List the outcomes from the sample space \\(S = \\{{(H,H), (H,T), (T,H), (T,T)\\}}\\) that contain **exactly one Head**.\n"
        "2. Calculate the theoretical probability of getting exactly one Head."
    )
    sol = (
        "**Calculation:**\n"
        "1. The outcomes containing exactly one Head are **(H, T)** and **(T, H)** (2 favourable outcomes).\n"
        "2. Theoretical probability:\n"
        "\\[ P(\\text{Exactly 1 Head}) = \\frac{n(E)}{n(S)} = \\frac{2}{4} = \\frac{1}{2} = 50\\% \\]"
    )
    ans = "1. {(H, T), (T, H)}; 2. 1/2 (or 2/4 = 50%)"
    return {
        "id": f"g8_prob_two_coins_one_h_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_two_coins_probability_exactly_one_head",
        "learning_objective_id": "math_g8_prob_two_coins_one_h",
        "hints": {
            "tier_1": "(H, T) and (T, H) each have exactly 1 Head.",
            "tier_2": "2 favourable outcomes out of 4 total outcomes.",
            "tier_3": "2/4 = 1/2.",
        },
        "misconception_tags": ["counting_only_ht_and_forgetting_th"],
    }


# ----------------------------------------------------------------------
# 30. Two Coins: Probability At Least One Tail
# ----------------------------------------------------------------------
def arch_30_two_coins_probability_at_least_one_tail(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair coins are flipped.\n\n"
        "1. List the outcomes that satisfy the condition **at least one Tail**.\n"
        "2. Calculate the theoretical probability of obtaining at least one Tail."
    )
    sol = (
        "**Calculation:**\n"
        "1. 'At least one Tail' means 1 Tail or 2 Tails:\n"
        "- Favourable outcomes: **(H, T), (T, H), (T, T)** (3 outcomes).\n"
        "2. Theoretical probability:\n"
        "\\[ P(\\text{At least 1 Tail}) = \\frac{n(E)}{n(S)} = \\frac{3}{4} = 0{,}75 = 75\\% \\]\n"
        "Alternatively: \\(1 - P(\\text{No Tails}) = 1 - P(H, H) = 1 - \\frac{1}{4} = \\frac{3}{4}\\)."
    )
    ans = "1. {(H, T), (T, H), (T, T)}; 2. 3/4 (or 75%)"
    return {
        "id": f"g8_prob_two_coins_at_least_t_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_two_coins_probability_at_least_one_tail",
        "learning_objective_id": "math_g8_prob_two_coins_at_least_t",
        "hints": {
            "tier_1": "'At least one' means 1 or more (only (H, H) is excluded).",
            "tier_2": "3 outcomes out of 4.",
            "tier_3": "3/4.",
        },
        "misconception_tags": ["confusing_at_least_one_with_exactly_one"],
    }


# ----------------------------------------------------------------------
# 31. Coin and Dice: Compound Sample Space 12 (WITH SVG)
# ----------------------------------------------------------------------
def arch_31_coin_and_dice_combined_outcomes_sample_space_12(rng: random.Random) -> Dict[str, Any]:
    svg = draw_coin_and_dice_tree_svg(seed=rng.randint(100, 999999))

    prompt = (
        "In a compound experiment, a fair coin is flipped once and a standard 6-sided die is rolled once.\n\n"
        "1. How many total combined outcomes are in the sample space? Show the multiplication rule.\n"
        "2. List all the outcomes that start with Tails.\n"
        "3. What is the probability of obtaining the specific combined outcome of **(Heads, 5)**?"
    )
    sol = (
        "**Compound Experiment Analysis:**\n"
        "1. Total outcomes = \\(n(\\text{Coin}) \\times n(\\text{Dice}) = 2 \\times 6 = 12\\).\n"
        "2. Outcomes starting with Tails: **{T1, T2, T3, T4, T5, T6}**.\n"
        "3. Each of the 12 outcomes is equally likely:\n"
        "\\[ P(H5) = \\frac{1}{12} \\approx 0{,}083 = 8{,}3\\% \\]"
    )
    ans = "1. 2 × 6 = 12 outcomes; 2. {T1, T2, T3, T4, T5, T6}; 3. 1/12"
    return {
        "id": f"g8_prob_coin_dice_tree_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "31_coin_and_dice_combined_outcomes_sample_space_12",
        "learning_objective_id": "math_g8_prob_coin_dice_tree",
        "hints": {
            "tier_1": "Multiply number of coin options (2) by dice options (6) = 12.",
            "tier_2": "Each individual pair has probability 1/12.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_2_and_6_instead_of_multiplying_for_compound_outcomes"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Coin and Dice: Probability Heads and Even Number
# ----------------------------------------------------------------------
def arch_32_coin_and_dice_probability_heads_and_even_number(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fair coin is flipped and a fair 6-sided die is rolled.\n\n"
        "1. List all the outcomes that include getting **Heads and an even number** on the die.\n"
        "2. Calculate the theoretical probability of getting Heads and an even number, writing your answer in simplest form."
    )
    sol = (
        "**Calculation:**\n"
        "1. Favourable outcomes: **{H2, H4, H6}** (3 outcomes).\n"
        "2. Total outcomes: \\(2 \\times 6 = 12\\).\n"
        "\\[ P(\\text{Heads and Even}) = \\frac{3}{12} = \\frac{1}{4} = 0{,}25 = 25\\% \\]"
    )
    ans = "1. {H2, H4, H6}; 2. 1/4 (or 3/12 = 25%)"
    return {
        "id": f"g8_prob_h_even_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_coin_and_dice_probability_heads_and_even_number",
        "learning_objective_id": "math_g8_prob_h_even",
        "hints": {
            "tier_1": "Even numbers on a die: 2, 4, 6.",
            "tier_2": "Pair with H: H2, H4, H6 (3 outcomes).",
            "tier_3": "3/12 = 1/4.",
        },
        "misconception_tags": ["dividing_by_6_instead_of_12_for_compound_experiment"],
    }


# ----------------------------------------------------------------------
# 33. Coin and Dice: Probability Tails and Prime Number
# ----------------------------------------------------------------------
def arch_33_coin_and_dice_probability_tails_and_prime_number(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fair coin is tossed and a fair 6-sided die is rolled.\n\n"
        "1. List all the outcomes that consist of **Tails and a prime number**.\n"
        "2. Calculate the probability of this event, expressed as a fraction and as a percentage."
    )
    sol = (
        "**Calculation:**\n"
        "1. Prime numbers on a die: {2, 3, 5}.\n"
        "Pairing with Tails gives: **{T2, T3, T5}** (3 favourable outcomes).\n"
        "2. Probability:\n"
        "\\[ P = \\frac{3}{12} = \\frac{1}{4} = 25\\% \\]"
    )
    ans = "1. {T2, T3, T5}; 2. 1/4 (25%)"
    return {
        "id": f"g8_prob_t_prime_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_coin_and_dice_probability_tails_and_prime_number",
        "learning_objective_id": "math_g8_prob_t_prime",
        "hints": {
            "tier_1": "Primes on a die are 2, 3, 5 (1 is not prime).",
            "tier_2": "Favourable: T2, T3, T5 (3 out of 12).",
            "tier_3": "3/12 = 1/4 = 25%.",
        },
        "misconception_tags": ["including_t1_as_a_prime_outcome"],
    }


# ----------------------------------------------------------------------
# 34. Two Dice: Two-Way Table Sample Space 36 (WITH TABLE)
# ----------------------------------------------------------------------
def arch_34_two_dice_two_way_table_sample_space_36(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two standard fair 6-sided dice (one red, one blue) are rolled together.\n\n"
        "1. Calculate the total number of combined outcomes \\(n(S)\\) using the product rule.\n"
        "2. What is the smallest possible sum of the two dice, and what is the largest possible sum?\n"
        "3. How many different pairs of dice outcomes result in a sum of **3**?"
    )
    sol = (
        "**Two-Dice Sample Space Analysis:**\n"
        "1. Total outcomes: \\(6 \\times 6 = 36\\) possible outcomes.\n"
        "2. Smallest sum: \\(1 + 1 = 2\\); Largest sum: \\(6 + 6 = 12\\).\n"
        "3. Outcomes giving sum of 3: **(1, 2)** and **(2, 1)** (2 outcomes)."
    )
    ans = "1. 36; 2. Smallest = 2, Largest = 12; 3. 2 outcomes: (1, 2) and (2, 1)"
    table_data = {
        "headers": ["Die 1 \\ Die 2", "1", "2", "3", "4", "5", "6"],
        "rows": [
            ["1", "2", "3", "4", "5", "6", "7"],
            ["2", "3", "4", "5", "6", "7", "8"],
            ["3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "10"],
            ["5", "6", "7", "8", "9", "10", "11"],
            ["6", "7", "8", "9", "10", "11", "12"],
        ],
    }
    return {
        "id": f"g8_prob_two_dice_grid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "34_two_dice_two_way_table_sample_space_36",
        "learning_objective_id": "math_g8_prob_two_dice_grid",
        "hints": {
            "tier_1": "6 rows × 6 columns = 36 total combinations.",
            "tier_2": "Sums range from 1+1=2 to 6+6=12.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_the_minimum_sum_is_1"],
        "table": table_data,
    }


# ----------------------------------------------------------------------
# 35. Two Dice: Probability Sum Equals Seven
# ----------------------------------------------------------------------
def arch_35_two_dice_probability_sum_equals_seven(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair 6-sided dice are rolled.\n\n"
        "1. List all ordered pairs of numbers \\((d_1, d_2)\\) whose sum is exactly **7**.\n"
        "2. Calculate the theoretical probability of rolling a sum of 7, writing your answer in simplest form."
    )
    sol = (
        "**Sum of 7 Analysis:**\n"
        "1. Favourable pairs: **(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)** (6 favourable outcomes).\n"
        "2. Total outcomes: \\(n(S) = 36\\).\n"
        "\\[ P(\\text{Sum} = 7) = \\frac{6}{36} = \\frac{1}{6} \\]"
    )
    ans = "1. {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}; 2. 1/6 (or 6/36)"
    return {
        "id": f"g8_prob_sum_7_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_two_dice_probability_sum_equals_seven",
        "learning_objective_id": "math_g8_prob_sum_7",
        "hints": {
            "tier_1": "Pairs adding to 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.",
            "tier_2": "There are 6 favourable pairs out of 36.",
            "tier_3": "6/36 = 1/6.",
        },
        "misconception_tags": ["counting_only_three_pairs_by_omitting_reversed_order"],
    }


# ----------------------------------------------------------------------
# 36. Two Dice: Probability Sum Greater Than Nine
# ----------------------------------------------------------------------
def arch_36_two_dice_probability_sum_greater_than_nine(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair 6-sided dice are rolled.\n\n"
        "1. List all pairs of outcomes where the sum of the two dice is **greater than 9** (i.e. sums of 10, 11, or 12).\n"
        "2. Calculate the theoretical probability of rolling a sum greater than 9."
    )
    sol = (
        "**Sum Greater Than 9 Analysis:**\n"
        "1. Favourable pairs:\n"
        "- Sum of 10: (4, 6), (5, 5), (6, 4) [3 pairs]\n"
        "- Sum of 11: (5, 6), (6, 5) [2 pairs]\n"
        "- Sum of 12: (6, 6) [1 pair]\n"
        "Total favourable = \\(3 + 2 + 1 = 6\\) outcomes.\n\n"
        "2. Probability:\n"
        "\\[ P(\\text{Sum} > 9) = \\frac{6}{36} = \\frac{1}{6} \\]"
    )
    ans = "1. 6 pairs: {(4,6), (5,5), (6,4), (5,6), (6,5), (6,6)}; 2. 1/6 (or 6/36)"
    return {
        "id": f"g8_prob_sum_gt_9_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_two_dice_probability_sum_greater_than_nine",
        "learning_objective_id": "math_g8_prob_sum_gt_9",
        "hints": {
            "tier_1": "Count pairs giving sums of 10, 11, and 12.",
            "tier_2": "3 for 10, 2 for 11, 1 for 12 -> 6 pairs.",
            "tier_3": "6/36 = 1/6.",
        },
        "misconception_tags": ["including_pairs_that_sum_to_nine"],
    }


# ----------------------------------------------------------------------
# 37. Two Dice: Probability Doubles Matching Numbers
# ----------------------------------------------------------------------
def arch_37_two_dice_probability_doubles_matching_numbers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair 6-sided dice are rolled simultaneously.\n\n"
        "1. List all outcomes where both dice show the exact same number (rolling 'doubles').\n"
        "2. Calculate the theoretical probability of rolling doubles."
    )
    sol = (
        "**Rolling Doubles Analysis:**\n"
        "1. Matching pairs: **(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)** (6 favourable outcomes).\n"
        "2. Probability:\n"
        "\\[ P(\\text{Doubles}) = \\frac{6}{36} = \\frac{1}{6} \\]"
    )
    ans = "1. {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}; 2. 1/6"
    return {
        "id": f"g8_prob_doubles_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_two_dice_probability_doubles_matching_numbers",
        "learning_objective_id": "math_g8_prob_doubles",
        "hints": {
            "tier_1": "There are 6 possible doubles from (1, 1) to (6, 6).",
            "tier_2": "6 favourable outcomes out of 36 total outcomes.",
            "tier_3": "6/36 = 1/6.",
        },
        "misconception_tags": ["miscounting_number_of_doubles"],
    }


# ----------------------------------------------------------------------
# 38. Two Dice: Probability Difference of Numbers
# ----------------------------------------------------------------------
def arch_38_two_dice_probability_difference_of_numbers(rng: random.Random) -> Dict[str, Any]:
    target_diff = rng.choice([3, 4])
    if target_diff == 3:
        pairs = ["(1, 4)", "(4, 1)", "(2, 5)", "(5, 2)", "(3, 6)", "(6, 3)"]
        frac_str = "6/36 = 1/6"
    else:
        pairs = ["(1, 5)", "(5, 1)", "(2, 6)", "(6, 2)"]
        frac_str = "4/36 = 1/9"

    prompt = (
        f"Two fair 6-sided dice are rolled.\n\n"
        f"Calculate the theoretical probability that the positive difference between the two numbers shown is **{target_diff}**."
    )
    sol = (
        f"**Difference of {target_diff} Analysis:**\n"
        f"Favourable outcomes with positive difference \\(|d_1 - d_2| = {target_diff}\\):\n"
        f"{', '.join(pairs)} ({len(pairs)} favourable outcomes).\n\n"
        f"\\[ P = \\frac{{{len(pairs)}}}{{36}} = {frac_str} \\]"
    )
    ans = frac_str.split("=")[-1].strip()
    return {
        "id": f"g8_prob_diff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_two_dice_probability_difference_of_numbers",
        "learning_objective_id": "math_g8_prob_diff",
        "hints": {
            "tier_1": f"Find pairs whose difference is {target_diff}.",
            "tier_2": f"Count both orders: e.g. (1, {1+target_diff}) and ({1+target_diff}, 1).",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_that_difference_can_occur_in_two_different_orders"],
    }


# ----------------------------------------------------------------------
# 39. Two Dice: Fairness Analysis of Sum-Based Game
# ----------------------------------------------------------------------
def arch_39_two_dice_game_fairness_evaluation_sum_rules(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Lerato and Sipho play a game by rolling two fair 6-sided dice and adding the scores:\n"
        "- **Lerato wins** if the sum is **7 or less** (sums from 2 to 7).\n"
        "- **Sipho wins** if the sum is **8 or more** (sums from 8 to 12).\n\n"
        "1. Count how many of the 36 outcomes give a sum of 7 or less.\n"
        "2. Count how many of the 36 outcomes give a sum of 8 or more.\n"
        "3. Determine if the game is fair or biased towards one player."
    )
    sol = (
        "**Sum Outcomes Analysis:**\n"
        "- Sums 2 to 7: Sum 2 (1), Sum 3 (2), Sum 4 (3), Sum 5 (4), Sum 6 (5), Sum 7 (6):\n"
        "Total for Lerato = \\(1 + 2 + 3 + 4 + 5 + 6 = 21\\) outcomes.\n"
        "\\[ P(\\text{Lerato}) = \\frac{21}{36} = \\frac{7}{12} \\approx 58{,}3\\% \\]\n\n"
        "- Sums 8 to 12: Sum 8 (5), Sum 9 (4), Sum 10 (3), Sum 11 (2), Sum 12 (1):\n"
        "Total for Sipho = \\(5 + 4 + 3 + 2 + 1 = 15\\) outcomes.\n"
        "\\[ P(\\text{Sipho}) = \\frac{15}{36} = \\frac{5}{12} \\approx 41{,}7\\% \\]\n\n"
        "**Conclusion:** The game is **unfair** (biased towards Lerato, who has 21/36 vs Sipho's 15/36)."
    )
    ans = "1. 21 outcomes (21/36); 2. 15 outcomes (15/36); 3. Unfair (biased towards Lerato)"
    return {
        "id": f"g8_prob_sum_game_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "39_two_dice_game_fairness_evaluation_sum_rules",
        "learning_objective_id": "math_g8_prob_sum_game",
        "hints": {
            "tier_1": "Count combinations for sums 2 to 7 vs 8 to 12.",
            "tier_2": "21 outcomes for <= 7; 15 outcomes for >= 8.",
            "tier_3": "Unfair because 21 != 15.",
        },
        "misconception_tags": ["assuming_the_sums_are_split_evenly_between_2_7_and_8_12"],
    }


# ----------------------------------------------------------------------
# 40. Two Spinners: Combined Outcomes Grid (WITH TABLE)
# ----------------------------------------------------------------------
def arch_40_two_spinners_combined_outcomes_two_way_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two spinners are spun:\n"
        "- Spinner 1 has 3 equal sectors numbered: **1, 2, 3**\n"
        "- Spinner 2 has 3 equal sectors colored: **Red (R), Green (G), Blue (B)**\n\n"
        "1. State the total number of combined outcomes.\n"
        "2. List all the outcomes that include the color Green.\n"
        "3. Calculate the probability of obtaining an even number and the color Red."
    )
    sol = (
        "**Combined Outcomes:**\n"
        "1. Total outcomes = \\(3 \\times 3 = 9\\) outcomes.\n"
        "2. Green outcomes: **{(1, G), (2, G), (3, G)}** (3 outcomes).\n"
        "3. Even number and Red: The only even number is 2, so the only outcome is **(2, R)**:\n"
        "\\[ P = \\frac{1}{9} \\]"
    )
    ans = "1. 9; 2. {(1, G), (2, G), (3, G)}; 3. 1/9"
    tbl = {
        "headers": ["Spinner 1 \\ Spinner 2", "Red (R)", "Green (G)", "Blue (B)"],
        "rows": [
            ["1", "(1, R)", "(1, G)", "(1, B)"],
            ["2", "(2, R)", "(2, G)", "(2, B)"],
            ["3", "(3, R)", "(3, G)", "(3, B)"],
        ],
    }
    return {
        "id": f"g8_prob_spinners_grid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "40_two_spinners_combined_outcomes_two_way_table",
        "learning_objective_id": "math_g8_prob_spinners_grid",
        "hints": {
            "tier_1": "3 numbers × 3 colors = 9 outcomes.",
            "tier_2": "Only 1 outcome is (2, R).",
            "tier_3": "1/9.",
        },
        "misconception_tags": ["adding_options_instead_of_multiplying"],
        "table": tbl,
    }


# ----------------------------------------------------------------------
# 41. Consecutive Draws: With Replacement Tree Diagram (WITH SVG)
# ----------------------------------------------------------------------
def arch_41_drawing_two_counters_with_replacement_tree_diagram(rng: random.Random) -> Dict[str, Any]:
    svg = draw_tree_diagram_two_coins_svg(seed=rng.randint(100, 999999))

    prompt = (
        "A pouch contains 3 red beads and 2 white beads (total 5 beads).\n"
        "A bead is drawn at random, its color is noted, and it is **placed back into the pouch** (with replacement). "
        "A second bead is then drawn.\n\n"
        "1. What is the probability of drawing Red on the first draw?\n"
        "2. What is the probability of drawing Red on the second draw?\n"
        "3. Calculate the probability of drawing two red beads consecutively."
    )
    sol = (
        "**With Replacement Analysis:**\n"
        "Because the bead is replaced, the contents and probabilities do not change between draws:\n"
        "1. \\(P(\\text{Red 1}) = \\frac{3}{5}\\)\n"
        "2. \\(P(\\text{Red 2}) = \\frac{3}{5}\\)\n"
        "3. Combined probability:\n"
        "\\[ P(\\text{Red and Red}) = \\frac{3}{5} \\times \\frac{3}{5} = \\frac{9}{25} = 0{,}36 = 36\\% \\]"
    )
    ans = "1. 3/5; 2. 3/5; 3. 9/25 (36%)"
    return {
        "id": f"g8_prob_with_rep_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "41_drawing_two_counters_with_replacement_tree_diagram",
        "learning_objective_id": "math_g8_prob_with_rep",
        "hints": {
            "tier_1": "With replacement means the second draw has the same total of 5 beads.",
            "tier_2": "Multiply: 3/5 × 3/5.",
            "tier_3": "9/25.",
        },
        "misconception_tags": ["reducing_denominator_when_replacement_occurred"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Consecutive Draws: Without Replacement Fraction Change
# ----------------------------------------------------------------------
def arch_42_drawing_two_counters_without_replacement_fraction_change(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A pouch contains 3 red beads and 2 white beads (total 5 beads).\n"
        "A bead is picked at random and **NOT replaced** into the pouch. A second bead is then picked.\n\n"
        "1. What is the probability that the first bead is Red?\n"
        "2. If the first bead was Red, what is the probability that the second bead is also Red?\n"
        "3. Calculate the probability of picking two red beads without replacement."
    )
    sol = (
        "**Without Replacement Analysis:**\n"
        "1. First draw: 3 red beads out of 5 total \\(\\implies P(\\text{Red 1}) = \\frac{3}{5}\\).\n"
        "2. Second draw: Only 2 red beads remain out of 4 total beads \\(\\implies P(\\text{Red 2} \\mid \\text{Red 1}) = \\frac{2}{4} = \\frac{1}{2}\\).\n"
        "3. Combined probability:\n"
        "\\[ P(\\text{Both Red}) = \\frac{3}{5} \\times \\frac{2}{4} = \\frac{6}{20} = \\frac{3}{10} = 30\\% \\]"
    )
    ans = "1. 3/5; 2. 2/4 (or 1/2); 3. 3/10 (or 6/20 = 30%)"
    return {
        "id": f"g8_prob_without_rep_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "42_drawing_two_counters_without_replacement_fraction_change",
        "learning_objective_id": "math_g8_prob_without_rep",
        "hints": {
            "tier_1": "Without replacement means 1 less bead on the second draw (total drops to 4).",
            "tier_2": "Second red probability is 2/4.",
            "tier_3": "3/5 × 2/4 = 6/20 = 3/10.",
        },
        "misconception_tags": ["keeping_the_denominator_as_5_on_the_second_draw"],
    }


# ----------------------------------------------------------------------
# 43. Independent Events: Multiplication Rule
# ----------------------------------------------------------------------
def arch_43_two_stage_event_independent_events_multiplication_rule(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two events \\(A\\) and \\(B\\) are **independent** if the outcome of one does not affect the other.\n\n"
        "1. State the multiplication rule for two independent events \\(P(A \\text{ and } B)\\).\n"
        "2. A fair coin is tossed (Event A) and a fair 6-sided die is rolled (Event B). "
        "Use the multiplication rule to calculate the probability of getting Heads on the coin and a 4 on the die."
    )
    sol = (
        "**Multiplication Rule for Independent Events:**\n"
        "1. \\(P(A \\text{ and } B) = P(A) \\times P(B)\\)\n\n"
        "2. Calculation:\n"
        "- \\(P(\\text{Heads}) = \\frac{1}{2}\\)\n"
        "- \\(P(4) = \\frac{1}{6}\\)\n"
        "\\[ P(\\text{Heads and 4}) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12} \\approx 0{,}083 \\]"
    )
    ans = "1. P(A and B) = P(A) × P(B); 2. 1/12"
    return {
        "id": f"g8_prob_indep_mult_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_two_stage_event_independent_events_multiplication_rule",
        "learning_objective_id": "math_g8_prob_indep_mult",
        "hints": {
            "tier_1": "Multiply the separate probabilities together.",
            "tier_2": "1/2 × 1/6.",
            "tier_3": "1/12.",
        },
        "misconception_tags": ["adding_probabilities_instead_of_multiplying"],
    }


# ----------------------------------------------------------------------
# 44. Prediction: Expected Frequency in N Trials
# ----------------------------------------------------------------------
def arch_44_predicting_number_of_times_event_occurs_in_n_trials(rng: random.Random) -> Dict[str, Any]:
    n_trials = rng.choice([120, 180, 240, 300, 600])
    # Expected number of 6s on a fair die
    expected = n_trials // 6

    prompt = (
        f"A standard fair 6-sided die is rolled **{n_trials} times**.\n\n"
        f"1. What is the theoretical probability of rolling the number 5 on any single roll?\n"
        f"2. Predict the number of times you would expect the number 5 to appear in {n_trials} rolls."
    )
    sol = (
        f"**Expected Value Calculation:**\n"
        f"1. \\(P(5) = \\frac{{1}}{{6}}\\)\n"
        f"2. Expected frequency \\(= N \\times P = {n_trials} \\times \\frac{{1}}{{6}} = {expected}\\) times."
    )
    ans = f"1. 1/6; 2. {expected} times"
    return {
        "id": f"g8_prob_expect_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_predicting_number_of_times_event_occurs_in_n_trials",
        "learning_objective_id": "math_g8_prob_expect",
        "hints": {
            "tier_1": f"Multiply total rolls ({n_trials}) by the probability (1/6).",
            "tier_2": f"{n_trials} / 6.",
            "tier_3": f"{expected} times.",
        },
        "misconception_tags": ["multiplying_trials_by_the_number_on_the_face_5"],
    }


# ----------------------------------------------------------------------
# 45. Two-Way Frequency Table: Survey Data Probability (WITH TABLE)
# ----------------------------------------------------------------------
def arch_45_survey_data_probability_two_way_table_gender_sport(rng: random.Random) -> Dict[str, Any]:
    # Boys: Soccer 25, Cricket 15 -> Total Boys 40
    # Girls: Soccer 20, Cricket 20 -> Total Girls 40
    # Total = 80
    prompt = (
        "A survey was conducted among 80 Grade 8 learners asking for their favourite sport:\n\n"
        "1. How many total learners prefer Soccer?\n"
        "2. If a learner is chosen at random from the entire group of 80 learners, "
        "what is the probability that the learner is a girl who prefers Cricket?"
    )
    sol = (
        "**Two-Way Table Probability:**\n"
        "1. Total Soccer = 25 (Boys) + 20 (Girls) = 45 learners.\n"
        "2. Girls who prefer Cricket = 20 learners.\n"
        "\\[ P(\\text{Girl and Cricket}) = \\frac{20}{80} = \\frac{1}{4} = 0{,}25 = 25\\% \\]"
    )
    ans = "1. 45; 2. 1/4 (or 20/80 = 25%)"
    tbl = {
        "headers": ["Gender", "Soccer", "Cricket", "Total"],
        "rows": [
            ["Boys", "25", "15", "40"],
            ["Girls", "20", "20", "40"],
            ["Total", "45", "35", "80"],
        ],
    }
    return {
        "id": f"g8_prob_survey_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "45_survey_data_probability_two_way_table_gender_sport",
        "learning_objective_id": "math_g8_prob_survey",
        "hints": {
            "tier_1": "Find the cell for Girls and Cricket (20).",
            "tier_2": "Divide 20 by the grand total 80.",
            "tier_3": "20/80 = 1/4.",
        },
        "misconception_tags": ["dividing_by_the_row_total_instead_of_grand_total"],
        "table": tbl,
    }


# ----------------------------------------------------------------------
# 46. Two-Way Table: Conditional Frequency Subset Selection
# ----------------------------------------------------------------------
def arch_46_survey_data_conditional_frequency_subset_selection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Refer to the sports survey of 80 learners (40 Boys and 40 Girls):\n"
        "- Among the 40 Boys: 25 prefer Soccer and 15 prefer Cricket.\n"
        "- Among the 40 Girls: 20 prefer Soccer and 20 prefer Cricket.\n\n"
        "If a learner is selected at random from the **BOYS ONLY**, "
        "what is the probability that this chosen boy prefers Soccer?"
    )
    sol = (
        "**Subgroup (Conditional) Selection:**\n"
        "The sample space is restricted strictly to the group of Boys: \\(n(S) = 40\\).\n"
        "Number of boys who prefer Soccer: \\(n(E) = 25\\).\n"
        "\\[ P = \\frac{25}{40} = \\frac{5}{8} = 0{,}625 = 62{,}5\\% \\]"
    )
    ans = "5/8 (or 25/40 = 62,5%)"
    tbl = {
        "headers": ["Gender", "Soccer", "Cricket", "Total"],
        "rows": [
            ["Boys", "25", "15", "40"],
            ["Girls", "20", "20", "40"],
            ["Total", "45", "35", "80"],
        ],
    }
    return {
        "id": f"g8_prob_cond_sub_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_survey_data_conditional_frequency_subset_selection",
        "learning_objective_id": "math_g8_prob_cond_sub",
        "hints": {
            "tier_1": "The question asks from the BOYS ONLY, so the denominator is 40.",
            "tier_2": "25 boys like Soccer out of 40 boys.",
            "tier_3": "25/40 = 5/8.",
        },
        "misconception_tags": ["dividing_by_80_instead_of_restricted_group_size_40"],
        "table": tbl,
    }


# ----------------------------------------------------------------------
# 47. Quality Control: Defective Items Probability
# ----------------------------------------------------------------------
def arch_47_quality_control_defective_items_probability(rng: random.Random) -> Dict[str, Any]:
    batch_size = rng.choice([200, 500, 1000])
    defective = rng.choice([4, 10, 20])
    good = batch_size - defective
    p_def = defective / batch_size
    pct_def = p_def * 100

    prompt = (
        f"A factory quality inspector tests a batch of **{batch_size} manufactured light bulbs** "
        f"and discovers that **{defective} bulbs** are defective.\n\n"
        f"1. What is the probability that a bulb selected at random from the batch is defective?\n"
        f"2. What is the probability that a bulb selected at random is in good working order?"
    )
    sol = (
        f"**Quality Inspection Probability:**\n"
        f"1. \\(P(\\text{{Defective}}) = \\frac{{{defective}}}{{{batch_size}}} = {_fmt_dec(p_def, 3)} = {_fmt_dec(pct_def)}\\%\\)\n"
        f"2. \\(P(\\text{{Good}}) = 1 - P(\\text{{Defective}}) = \\frac{{{good}}}{{{batch_size}}} = {_fmt_dec(good/batch_size, 3)} = {_fmt_dec(100-pct_def)}\\%\\)"
    )
    ans = f"1. {defective}/{batch_size} ({_fmt_dec(pct_def)}%); 2. {good}/{batch_size} ({_fmt_dec(100-pct_def)}%)"
    return {
        "id": f"g8_prob_qc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "47_quality_control_defective_items_probability",
        "learning_objective_id": "math_g8_prob_qc",
        "hints": {
            "tier_1": f"Divide defective count {defective} by batch size {batch_size}.",
            "tier_2": f"Subtract from 1 to find the probability of a good bulb.",
            "tier_3": ans,
        },
        "misconception_tags": ["inverting_defective_and_good_counts"],
    }


# ----------------------------------------------------------------------
# 48. Error Analysis: Gambler's Fallacy
# ----------------------------------------------------------------------
def arch_48_probability_error_analysis_gamblers_fallacy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A player flips a fair coin 5 times and it lands on **Heads every single time** (HHHHH).\n"
        "The player claims: *\"Because Heads came up 5 times in a row, the coin is now due for a Tails, "
        "so the probability of getting Tails on the 6th flip is much higher than 50%.\"*\n\n"
        "1. Is the player's claim mathematically correct or incorrect?\n"
        "2. State the true probability of obtaining Tails on the 6th flip.\n"
        "3. Name and explain the cognitive misconception illustrated by the player."
    )
    sol = (
        "**Fallacy Analysis:**\n"
        "1. The player's claim is **incorrect**.\n"
        "2. The true probability of obtaining Tails on the 6th flip is still exactly **\\(\\frac{1}{2} = 50\\%\\)**.\n"
        "3. This is known as the **Gambler's Fallacy**. Each toss of a fair coin is an independent event; "
        "the coin has no physical memory of previous flips, so previous outcomes have zero influence on future flips."
    )
    ans = "1. Incorrect; 2. Exactly 1/2 (50%); 3. Gambler's Fallacy (flips are independent; the coin has no memory)"
    return {
        "id": f"g8_prob_gambler_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "48_probability_error_analysis_gamblers_fallacy",
        "learning_objective_id": "math_g8_prob_gambler",
        "hints": {
            "tier_1": "Coins do not have memory of previous trials.",
            "tier_2": "Each flip is independent with P = 1/2.",
            "tier_3": "Gambler's fallacy.",
        },
        "misconception_tags": ["believing_independent_random_trials_compensate_for_past_streaks"],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Ignoring Order in Outcomes
# ----------------------------------------------------------------------
def arch_49_probability_error_analysis_ignoring_order_in_outcomes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When analyzing the simultaneous toss of two fair coins, a learner claims:\n"
        "*\"There are only 3 possible outcomes: two heads, two tails, or one of each. "
        "Therefore, the probability of getting one head and one tail is exactly \\(\\frac{1}{3}\\).\"*\n\n"
        "1. Explain the fatal error in the learner's reasoning.\n"
        "2. Provide the correct sample space and the correct probability of getting one head and one tail."
    )
    sol = (
        "**Error Identification:**\n"
        "1. The learner failed to treat the two coins as distinct trials and ignored the order of outcomes. "
        "The three events described are NOT equally likely. 'One of each' can happen in TWO different ways "
        "(Coin 1 = H, Coin 2 = T) OR (Coin 1 = T, Coin 2 = H).\n\n"
        "2. Correct sample space: \\(S = \\{{(H, H), (H, T), (T, H), (T, T)\\}}\\) (4 equally likely outcomes).\n"
        "Correct probability: \\(P(\\text{One of each}) = \\frac{2}{4} = \\frac{1}{2}\\)."
    )
    ans = "1. Failed to recognize that (H, T) and (T, H) are two distinct equally likely outcomes; 2. S = 4 outcomes, P = 2/4 = 1/2"
    return {
        "id": f"g8_prob_err_order_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "49_probability_error_analysis_ignoring_order_in_outcomes",
        "learning_objective_id": "math_g8_prob_err_order",
        "hints": {
            "tier_1": "There are 4 equally likely outcomes, not 3.",
            "tier_2": "One head and one tail can happen as HT or TH.",
            "tier_3": "Correct probability is 2/4 = 1/2.",
        },
        "misconception_tags": ["treating_unordered_events_as_equally_likely_elementary_outcomes"],
    }


# ----------------------------------------------------------------------
# 50. Word Problem: School Raffle Tickets Prize Probability
# ----------------------------------------------------------------------
def arch_50_compound_probability_word_problem_school_raffle_tickets(rng: random.Random) -> Dict[str, Any]:
    total_tickets = rng.choice([200, 400, 500, 1000])
    bought = rng.choice([5, 10, 20])
    ticket_price = 10  # Rand
    revenue = total_tickets * ticket_price

    p_win = bought / total_tickets
    pct_win = p_win * 100
    gcd = math.gcd(bought, total_tickets)
    sim_num = bought // gcd
    sim_den = total_tickets // gcd

    prompt = (
        f"A school fundraising raffle sells a total of **{total_tickets} tickets** at R{ticket_price} each. "
        f"One winning ticket will be drawn at random for a bicycle prize. "
        f"A learner buys **{bought} tickets**.\n\n"
        f"1. Calculate the total funds raised by selling all {total_tickets} tickets in Rands.\n"
        f"2. Calculate the theoretical probability that this learner wins the bicycle prize, writing your answer as a simplified fraction and as a percentage."
    )
    sol = (
        f"**Raffle Calculations:**\n"
        f"1. Total funds raised: \\({total_tickets} \\times R{ticket_price} = R{revenue:,}\\).\n"
        f"2. Probability of winning:\n"
        f"\\[ P(\\text{{Win}}) = \\frac{{\\text{{Tickets bought}}}}{{\\text{{Total tickets}}}} = \\frac{{{bought}}}{{{total_tickets}}} = \\frac{{{sim_num}}}{{{sim_den}}} = {_fmt_dec(pct_win, 2)}\\% \\]"
    )
    ans = f"1. R{revenue:,}; 2. {sim_num}/{sim_den} ({_fmt_dec(pct_win, 2)}%)"
    return {
        "id": f"g8_prob_raffle_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "50_compound_probability_word_problem_school_raffle_tickets",
        "learning_objective_id": "math_g8_prob_raffle",
        "hints": {
            "tier_1": f"Multiply tickets by price: {total_tickets} × R{ticket_price}.",
            "tier_2": f"Divide tickets bought ({bought}) by total tickets ({total_tickets}).",
            "tier_3": f"{sim_num}/{sim_den}.",
        },
        "misconception_tags": ["confusing_money_amounts_with_probabilities"],
    }
