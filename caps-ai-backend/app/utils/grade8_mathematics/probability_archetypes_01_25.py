"""Grade 8 Mathematics — Probability Archetypes (01 to 25).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/03. Probability.md

Archetypes covered:
  01. Probability scale: Word descriptions (impossible, unlikely, even chance, likely, certain).
  02. Probability scale: Numerical bounds from 0 to 1 with milestone fractions (WITH SVG).
  03. Conversion: Common fractions, decimals, and percentages for probability values.
  04. Definitions: Outcome vs Event distinction with concrete examples.
  05. Sample space: Listing all possible single-stage outcomes for coins and dice.
  06. Fair coin: Theoretical probability of heads or tails.
  07. Fair dice: Theoretical probability of rolling a specific number (1/6).
  08. Fair dice: Theoretical probability of even or odd numbers (3/6 = 1/2).
  09. Fair dice: Theoretical probability of prime numbers (2, 3, 5 -> 3/6 = 1/2).
  10. Fair dice: Theoretical probability of numbers greater or less than a threshold.
  11. Eight-sided dice: Theoretical probability of outcomes on an octahedral die.
  12. Relative frequency: Calculation from coin toss experimental tally.
  13. Relative frequency: Calculation from dice rolling frequency table.
  14. Relative frequency vs theoretical probability comparison.
  15. Law of large numbers: Convergence of relative frequency to theoretical probability.
  16. Fair vs unfair games: Definition and mathematical criterion (P(win) = P(lose)).
  17. Game analysis: Single dice rules verifying equal winning conditions.
  18. Game analysis: Identifying unfair asymmetric scoring rules.
  19. Spinner: Equal sectors theoretical probability (WITH SVG).
  20. Spinner: Unequal sectors probability calculation (WITH SVG).
  21. Marbles in bag: Probability of drawing a specified single color.
  22. Marbles in bag: Complementary event ('not red').
  23. Marbles in bag: Effect of adding or removing items on probability.
  24. Playing cards: Probability of drawing a specific suit (hearts, diamonds, spades, clubs).
  25. Playing cards: Probability of drawing a face card (Jack, Queen, King) or Ace.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .probability_svg import (
    draw_probability_scale_svg,
    draw_spinner_svg,
)


def _fmt_dec(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 01. Probability Scale: Word Descriptions
# ----------------------------------------------------------------------
def arch_01_probability_scale_word_descriptions_mapping(rng: random.Random) -> Dict[str, Any]:
    events = [
        ("The sun will rise in the east tomorrow morning", "Certain (1)", 1.0),
        ("A standard coin will land showing Heads", "Even chance (0,5)", 0.5),
        ("A fish will walk across dry land breathing air", "Impossible (0)", 0.0),
        ("Rolling a 6 on a fair 6-sided die", "Unlikely (1/6)", 1 / 6),
        ("Drawing a red or black card from a standard deck", "Certain (1)", 1.0),
        ("Winning the national lottery jackpot with a single ticket", "Very unlikely", 0.0000001),
        ("A pregnant mother giving birth to a male infant", "Even chance (0,5)", 0.5),
        ("Selecting an odd number when rolling a standard die", "Even chance (0,5)", 0.5),
    ]
    rng.shuffle(events)
    ev, desc, p_val = events[0]

    prompt = (
        f"Consider the following real-world statement:\n"
        f"**\"{ev}\"**\n\n"
        f"1. Assign the most appropriate word description from the standard probability scale "
        f"(Impossible, Very unlikely, Unlikely, Even chance, Likely, Very likely, Certain).\n"
        f"2. State the approximate numerical probability value associated with your choice."
    )
    sol = (
        f"**Probability Scale Assessment:**\n"
        f"- The event \"{ev}\" corresponds to: **{desc}**.\n"
        f"- Approximate numerical probability: \\(P \\approx {_fmt_dec(p_val, 2)}\\)."
    )
    ans = f"1. {desc}; 2. {_fmt_dec(p_val, 2)}"
    return {
        "id": f"g8_prob_scale_words_{rng.randint(100000, 999999)}",
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
        "subskill": "01_probability_scale_word_descriptions_mapping",
        "learning_objective_id": "math_g8_prob_scale_words",
        "hints": {
            "tier_1": "Recall the continuous milestones: Impossible (0) to Certain (1).",
            "tier_2": f"Consider whether this event is guaranteed, 50-50, or cannot happen.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_unlikely_with_impossible"],
    }


# ----------------------------------------------------------------------
# 02. Probability Scale: Numerical Bounds Zero to One (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_probability_scale_numerical_bounds_zero_to_one(rng: random.Random) -> Dict[str, Any]:
    marker_choice = rng.choice([
        (0.2, "Unlikely (0,2)"),
        (0.5, "Even chance (0,5)"),
        (0.8, "Likely (0,8)"),
    ])
    val, label = marker_choice
    svg = draw_probability_scale_svg(val, label, seed=rng.randint(100, 999999))

    prompt = (
        f"On a mathematical probability scale from 0 to 1:\n\n"
        f"1. Explain why a probability can never be less than 0 or greater than 1.\n"
        f"2. State the exact numeric value that represents an event that has an even chance of happening.\n"
        f"3. Write this even chance value as a fraction, a decimal, and a percentage."
    )
    sol = (
        f"**1. Numerical Limits of Probability:**\n"
        f"Probability is defined as \\(P(E) = \\frac{{n(E)}}{{n(S)}}\\). Since an event cannot occur fewer than 0 times, "
        f"\\(P(E) \\ge 0\\). Since an event cannot occur more times than the total number of all possible outcomes \\(n(S)\\), "
        f"\\(P(E) \\le 1\\). Therefore, probability strictly lies in the interval \\([0; 1]\\).\n\n"
        f"**2. Even Chance Value:** \\(0{{,}}5\\).\n"
        f"**3. Three Forms:** Fraction \\(\\frac{{1}}{{2}}\\), Decimal \\(0{{,}}5\\), Percentage \\(50\\%\\)."
    )
    ans = "1. Cannot happen < 0 or > total outcomes; 2. 0,5; 3. 1/2, 0,5, 50%"
    return {
        "id": f"g8_prob_scale_bounds_{rng.randint(100000, 999999)}",
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
        "subskill": "02_probability_scale_numerical_bounds_zero_to_one",
        "learning_objective_id": "math_g8_prob_scale_bounds",
        "hints": {
            "tier_1": "Probability ranges from 0 (impossible) to 1 (certain).",
            "tier_2": "Even chance is halfway: 1/2.",
            "tier_3": "1/2 = 0,5 = 50%.",
        },
        "misconception_tags": ["stating_probabilities_greater_than_one_or_negative"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Conversion: Common Fraction, Decimal, Percentage
# ----------------------------------------------------------------------
def arch_03_convert_probability_fraction_decimal_percentage(rng: random.Random) -> Dict[str, Any]:
    frac_choice = rng.choice([
        (1, 4, "0,25", "25%"),
        (3, 4, "0,75", "75%"),
        (1, 5, "0,2", "20%"),
        (4, 5, "0,8", "80%"),
        (1, 10, "0,1", "10%"),
        (3, 10, "0,3", "30%"),
        (1, 20, "0,05", "5%"),
    ])
    num, den, dec_str, pct_str = frac_choice

    prompt = (
        f"A probability is given as the common fraction \\(\\frac{{{num}}}{{{den}}}\\).\n\n"
        f"1. Convert this probability into a decimal fraction.\n"
        f"2. Convert this probability into a percentage."
    )
    sol = (
        f"**Conversion Steps:**\n"
        f"1. Decimal: \\(\\frac{{{num}}}{{{den}}} = {dec_str}\\)\n"
        f"2. Percentage: \\({dec_str} \\times 100\\% = {pct_str}\\)"
    )
    ans = f"1. {dec_str}; 2. {pct_str}"
    return {
        "id": f"g8_prob_conv_{rng.randint(100000, 999999)}",
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
        "subskill": "03_convert_probability_fraction_decimal_percentage",
        "learning_objective_id": "math_g8_prob_conv",
        "hints": {
            "tier_1": f"Divide {num} by {den} to find the decimal.",
            "tier_2": "Multiply decimal by 100 to find the percentage.",
            "tier_3": ans,
        },
        "misconception_tags": ["arithmetic_division_error_in_converting_fractions"],
    }


# ----------------------------------------------------------------------
# 04. Definitions: Outcome vs Event Distinction
# ----------------------------------------------------------------------
def arch_04_distinguish_outcome_vs_event_definitions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In probability theory, there is an important distinction between an **outcome** and an **event**.\n\n"
        "1. Define the term **outcome**.\n"
        "2. Define the term **event**.\n"
        "3. Using a fair 6-sided die, give one example of a single outcome and one example of a compound event."
    )
    sol = (
        "**Definitions and Concrete Examples:**\n"
        "1. **Outcome:** A single possible result of an experiment or trial (e.g. rolling a 4).\n"
        "2. **Event:** A collection of one or more outcomes satisfying a specified condition (a subset of the sample space).\n"
        "3. **Dice Examples:**\n"
        "- Example of an outcome: Rolling the number 3.\n"
        "- Example of an event: Rolling an even number (consisting of the three outcomes {2, 4, 6})."
    )
    ans = "1. Outcome is a single trial result; 2. Event is a collection of one or more outcomes; 3. Outcome: rolling 3; Event: rolling an even number {2, 4, 6}"
    return {
        "id": f"g8_prob_out_ev_{rng.randint(100000, 999999)}",
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
        "subskill": "04_distinguish_outcome_vs_event_definitions",
        "learning_objective_id": "math_g8_prob_out_ev",
        "hints": {
            "tier_1": "An outcome is one specific result; an event can contain multiple outcomes.",
            "tier_2": "Rolling 5 is an outcome; rolling an odd number is an event.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_outcome_and_event_as_synonyms"],
    }


# ----------------------------------------------------------------------
# 05. Sample Space: Listing All Possible Single-Stage Outcomes
# ----------------------------------------------------------------------
def arch_05_sample_space_listing_single_coin_and_dice(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        ("rolling a standard 6-sided die", "S = {1, 2, 3, 4, 5, 6}", 6),
        ("tossing a standard fair coin", "S = {Heads, Tails}", 2),
        ("drawing a card from 4 aces (Hearts, Diamonds, Clubs, Spades)", "S = {Ace of Hearts, Ace of Diamonds, Ace of Clubs, Ace of Spades}", 4),
        ("rolling an 8-sided octahedral die numbered 1 to 8", "S = {1, 2, 3, 4, 5, 6, 7, 8}", 8),
    ])
    action, space_str, total_n = context

    prompt = (
        f"For the probability experiment of **{action}**:\n\n"
        f"1. Write down the complete sample space \\(S\\) using set notation.\n"
        f"2. State the total number of possible outcomes \\(n(S)\\)."
    )
    sol = (
        f"**Sample Space:**\n"
        f"1. \\({space_str}\\)\n"
        f"2. \\(n(S) = {total_n}\\)"
    )
    ans = f"1. {space_str}; 2. n(S) = {total_n}"
    return {
        "id": f"g8_prob_sample_space_{rng.randint(100000, 999999)}",
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
        "subskill": "05_sample_space_listing_single_coin_and_dice",
        "learning_objective_id": "math_g8_prob_sample_space",
        "hints": {
            "tier_1": "List every distinct possible outcome in curly braces { ... }.",
            "tier_2": f"Count the total number of outcomes: {total_n}.",
            "tier_3": ans,
        },
        "misconception_tags": ["omitting_possible_outcomes_from_sample_space"],
    }


# ----------------------------------------------------------------------
# 06. Fair Coin: Theoretical Probability Heads or Tails
# ----------------------------------------------------------------------
def arch_06_theoretical_probability_single_fair_coin_heads_or_tails(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["Heads", "Tails"])
    prompt = (
        f"A fair coin has two identical sides: Heads and Tails. It is tossed once.\n\n"
        f"1. What is the theoretical probability of obtaining **{target}**?\n"
        f"2. Express your answer as a common fraction, as a decimal, and as a percentage."
    )
    sol = (
        f"**Calculation of Theoretical Probability:**\n"
        f"- Sample space: \\(S = \\{{\\text{{Heads}}, \\text{{Tails}}\\}}\\), so \\(n(S) = 2\\).\n"
        f"- Favourable outcome: \\(n({target}) = 1\\).\n"
        f"\\[ P({target}) = \\frac{{n(E)}}{{n(S)}} = \\frac{{1}}{{2}} = 0{{,}}5 = 50\\% \\]"
    )
    ans = "1. 1/2; 2. 1/2, 0,5, 50%"
    return {
        "id": f"g8_prob_coin_{rng.randint(100000, 999999)}",
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
        "subskill": "06_theoretical_probability_single_fair_coin_heads_or_tails",
        "learning_objective_id": "math_g8_prob_coin",
        "hints": {
            "tier_1": "There is 1 favorable outcome out of 2 possible outcomes.",
            "tier_2": "1/2 = 0,5 = 50%.",
            "tier_3": ans,
        },
        "misconception_tags": ["stating_probability_as_a_ratio_instead_of_fraction"],
    }


# ----------------------------------------------------------------------
# 07. Fair Dice: Theoretical Probability Specific Number
# ----------------------------------------------------------------------
def arch_07_theoretical_probability_single_dice_specific_number(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([1, 2, 3, 4, 5, 6])
    prompt = (
        f"A standard, fair six-sided die is rolled once.\n\n"
        f"Determine the theoretical probability of rolling the number **{target}**, showing formula and working."
    )
    sol = (
        f"**Theoretical Probability:**\n"
        f"- Sample space: \\(S = \\{{1, 2, 3, 4, 5, 6\\}}\\), \\(n(S) = 6\\).\n"
        f"- Favourable outcomes: \\(n({{{target}}}) = 1\\).\n"
        f"\\[ P({target}) = \\frac{{n(E)}}{{n(S)}} = \\frac{{1}}{{6}} \\]"
    )
    ans = "1/6"
    return {
        "id": f"g8_prob_dice_num_{rng.randint(100000, 999999)}",
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
        "subskill": "07_theoretical_probability_single_dice_specific_number",
        "learning_objective_id": "math_g8_prob_dice_num",
        "hints": {
            "tier_1": f"Only one face shows {target}.",
            "tier_2": "Divide 1 by total faces 6.",
            "tier_3": "1/6.",
        },
        "misconception_tags": ["thinking_higher_numbers_have_lower_probability"],
    }


# ----------------------------------------------------------------------
# 08. Fair Dice: Even or Odd Numbers
# ----------------------------------------------------------------------
def arch_08_theoretical_probability_single_dice_even_odd_numbers(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["even", "odd"])
    favourable = "{2, 4, 6}" if choice == "even" else "{1, 3, 5}"

    prompt = (
        f"A fair 6-sided die is rolled.\n\n"
        f"1. List the set of outcomes that represent rolling an **{choice} number**.\n"
        f"2. Calculate the theoretical probability of rolling an **{choice} number**, writing your answer in simplest fractional form."
    )
    sol = (
        f"**1. Outcomes for {choice} number:** \\({favourable}\\), so \\(n(E) = 3\\).\n\n"
        f"**2. Probability:**\n"
        f"\\[ P(\\text{{{choice}}}) = \\frac{{n(E)}}{{n(S)}} = \\frac{{3}}{{6}} = \\frac{{1}}{{2}} \\]"
    )
    ans = f"1. {favourable}; 2. 1/2"
    return {
        "id": f"g8_prob_even_odd_{rng.randint(100000, 999999)}",
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
        "subskill": "08_theoretical_probability_single_dice_even_odd_numbers",
        "learning_objective_id": "math_g8_prob_even_odd",
        "hints": {
            "tier_1": f"Identify the {choice} numbers between 1 and 6.",
            "tier_2": f"3 outcomes out of 6.",
            "tier_3": "3/6 simplifies to 1/2.",
        },
        "misconception_tags": ["forgetting_to_simplify_3_over_6"],
    }


# ----------------------------------------------------------------------
# 09. Fair Dice: Prime Numbers
# ----------------------------------------------------------------------
def arch_09_theoretical_probability_single_dice_prime_numbers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fair 6-sided die is rolled once.\n\n"
        "1. List all the prime numbers on the die (Note: 1 is NOT a prime number).\n"
        "2. Calculate the theoretical probability of rolling a prime number."
    )
    sol = (
        "**Prime Numbers on a Die:**\n"
        "1. The prime numbers between 1 and 6 are **{2, 3, 5}** (3 prime numbers). Note that 1 has only one factor, so it is not prime.\n"
        "2. Theoretical probability:\n"
        "\\[ P(\\text{Prime}) = \\frac{n(\\text{Primes})}{n(S)} = \\frac{3}{6} = \\frac{1}{2} \\]"
    )
    ans = "1. {2, 3, 5}; 2. 1/2 (or 3/6)"
    return {
        "id": f"g8_prob_prime_{rng.randint(100000, 999999)}",
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
        "subskill": "09_theoretical_probability_single_dice_prime_numbers",
        "learning_objective_id": "math_g8_prob_prime",
        "hints": {
            "tier_1": "Prime numbers have exactly two distinct factors: 2, 3, 5.",
            "tier_2": "1 is not prime; 4 and 6 are composite.",
            "tier_3": "3/6 = 1/2.",
        },
        "misconception_tags": ["treating_one_as_a_prime_number"],
    }


# ----------------------------------------------------------------------
# 10. Fair Dice: Greater or Less Than Threshold
# ----------------------------------------------------------------------
def arch_10_theoretical_probability_single_dice_greater_or_less_than_threshold(rng: random.Random) -> Dict[str, Any]:
    threshold = rng.choice([2, 3, 4, 5])
    greater = rng.choice([True, False])
    if greater:
        cond_str = f"greater than {threshold}"
        favourable = [x for x in range(1, 7) if x > threshold]
    else:
        cond_str = f"less than {threshold}"
        favourable = [x for x in range(1, 7) if x < threshold]

    k = len(favourable)
    gcd = math.gcd(k, 6)
    sim_num = k // gcd
    sim_den = 6 // gcd
    ans_frac = f"{sim_num}/{sim_den}" if sim_den != 1 else "1"

    prompt = (
        f"A standard 6-sided die is rolled.\n\n"
        f"Calculate the theoretical probability of rolling a number **{cond_str}**."
    )
    sol = (
        f"**Calculation:**\n"
        f"- Outcomes {cond_str}: \\({set(favourable)}\\), so \\(n(E) = {k}\\).\n"
        f"- Total outcomes: \\(n(S) = 6\\).\n"
        f"\\[ P = \\frac{{{k}}}{{6}} = \\frac{{{sim_num}}}{{{sim_den}}} \\]"
    )
    ans = f"{ans_frac} (or {k}/6)"
    return {
        "id": f"g8_prob_thresh_{rng.randint(100000, 999999)}",
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
        "subskill": "10_theoretical_probability_single_dice_greater_or_less_than_threshold",
        "learning_objective_id": "math_g8_prob_thresh",
        "hints": {
            "tier_1": f"List the numbers strictly {cond_str}.",
            "tier_2": f"Count how many: {k} out of 6.",
            "tier_3": ans_frac,
        },
        "misconception_tags": ["including_the_threshold_number_in_strict_inequality"],
    }


# ----------------------------------------------------------------------
# 11. Eight-Sided Dice: Theoretical Probability on Octahedral Die
# ----------------------------------------------------------------------
def arch_11_theoretical_probability_eight_sided_octahedral_dice(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([2, 5, 7, 8])
    prompt = (
        f"An eight-sided (octahedral) fair die has faces numbered from 1 to 8. It is rolled once.\n\n"
        f"1. What is the theoretical probability of rolling the number **{target}**?\n"
        f"2. What is the theoretical probability of rolling an even number on this 8-sided die?"
    )
    sol = (
        f"**Octahedral Die Analysis:**\n"
        f"- Total outcomes: \\(n(S) = 8\\).\n"
        f"1. \\(P({target}) = \\frac{{1}}{{8}}\\)\n"
        f"2. Even numbers on the die are \\(\\{{2, 4, 6, 8\\}}\\) (4 outcomes):\n"
        f"\\[ P(\\text{{Even}}) = \\frac{{4}}{{8}} = \\frac{{1}}{{2}} \\]"
    )
    ans = "1. 1/8; 2. 1/2 (or 4/8)"
    return {
        "id": f"g8_prob_d8_{rng.randint(100000, 999999)}",
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
        "subskill": "11_theoretical_probability_eight_sided_octahedral_dice",
        "learning_objective_id": "math_g8_prob_d8",
        "hints": {
            "tier_1": "There are 8 equal faces: sample space has 8 outcomes.",
            "tier_2": "Even numbers: 2, 4, 6, 8 (4 outcomes).",
            "tier_3": "1/8 and 4/8 = 1/2.",
        },
        "misconception_tags": ["dividing_by_6_out_of_habit_from_standard_dice"],
    }


# ----------------------------------------------------------------------
# 12. Relative Frequency: Coin Toss Experimental Tally
# ----------------------------------------------------------------------
def arch_12_relative_frequency_calculation_coin_flips(rng: random.Random) -> Dict[str, Any]:
    total_flips = rng.choice([20, 50, 100])
    heads = rng.randint(int(total_flips * 0.4), int(total_flips * 0.6))
    tails = total_flips - heads
    pct = round((tails / total_flips) * 100, 1)

    prompt = (
        f"A learner tosses a coin {total_flips} times in an experiment. "
        f"The recorded tally shows that Heads occurred {heads} times and Tails occurred {tails} times.\n\n"
        f"1. Calculate the **relative frequency** of Tails as a common fraction.\n"
        f"2. Convert this relative frequency into a percentage."
    )
    sol = (
        f"**Calculation of Relative Frequency:**\n"
        f"1. \\(\\text{{Relative Frequency of Tails}} = \\frac{{\\text{{Frequency of Tails}}}}{{\\text{{Total Trials}}}} = \\frac{{{tails}}}{{{total_flips}}}\\)\n"
        f"2. Percentage: \\(\\frac{{{tails}}}{{{total_flips}}} \\times 100\\% = {_fmt_dec(pct)}\\%\\)"
    )
    ans = f"1. {tails}/{total_flips}; 2. {_fmt_dec(pct)}%"
    return {
        "id": f"g8_prob_rel_freq_coin_{rng.randint(100000, 999999)}",
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
        "subskill": "12_relative_frequency_calculation_coin_flips",
        "learning_objective_id": "math_g8_prob_rel_freq_coin",
        "hints": {
            "tier_1": f"Relative frequency = {tails} / {total_flips}.",
            "tier_2": "Convert to percentage by multiplying by 100.",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_by_heads_instead_of_total_flips"],
    }


# ----------------------------------------------------------------------
# 13. Relative Frequency: Dice Rolling Frequency Table
# ----------------------------------------------------------------------
def arch_13_relative_frequency_calculation_dice_rolls(rng: random.Random) -> Dict[str, Any]:
    total_rolls = 60
    f3 = rng.choice([8, 10, 12, 14])
    pct = round((f3 / total_rolls) * 100, 1)

    prompt = (
        f"In a classroom experiment, a 6-sided die is rolled {total_rolls} times. "
        f"The number **3** appeared {f3} times.\n\n"
        f"1. State the formula for relative frequency.\n"
        f"2. Calculate the relative frequency of rolling a 3 as a simplified fraction.\n"
        f"3. How does this compare with the expected theoretical probability of \\(\\frac{{1}}{{6}}\\)?"
    )
    gcd = math.gcd(f3, total_rolls)
    sim_num = f3 // gcd
    sim_den = total_rolls // gcd

    sol = (
        f"**1. Formula:** \\(\\text{{Relative Frequency}} = \\frac{{\\text{{Frequency of Outcome}}}}{{\\text{{Total Number of Trials}}}}\\)\n\n"
        f"**2. Calculation:**\n"
        f"\\[ \\frac{{{f3}}}{{{total_rolls}}} = \\frac{{{sim_num}}}{{{sim_den}}} \\approx {_fmt_dec(f3/total_rolls, 3)} \\]\n\n"
        f"**3. Comparison:**\n"
        f"The theoretical probability is \\(\\frac{{1}}{{6}} = \\frac{{10}}{{60}} \\approx 0{{,}}167\\). "
        f"The experimental relative frequency (\\({sim_num}/{sim_den}\\)) is close to \\(1/6\\), "
        f"reflecting random experimental variation."
    )
    ans = f"1. frequency / total trials; 2. {sim_num}/{sim_den}; 3. Close to theoretical 1/6 (10/60)"
    return {
        "id": f"g8_prob_rel_freq_dice_{rng.randint(100000, 999999)}",
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
        "subskill": "13_relative_frequency_calculation_dice_rolls",
        "learning_objective_id": "math_g8_prob_rel_freq_dice",
        "hints": {
            "tier_1": f"Relative frequency = {f3} / {total_rolls}.",
            "tier_2": "Simplify the fraction by dividing numerator and denominator by common factor.",
            "tier_3": f"{sim_num}/{sim_den}.",
        },
        "misconception_tags": ["confusing_relative_frequency_with_absolute_frequency"],
    }


# ----------------------------------------------------------------------
# 14. Relative Frequency vs Theoretical Probability Comparison
# ----------------------------------------------------------------------
def arch_14_relative_frequency_vs_theoretical_probability_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the fundamental mathematical difference between **theoretical probability** "
        "and **relative frequency** (experimental probability). Include the formula used to calculate each."
    )
    sol = (
        "**Comparison:**\n"
        "1. **Theoretical Probability:** The calculated chance of an event happening based on mathematical reasoning "
        "and equal likelihood, without needing to perform an actual test:\n"
        "\\[ P(E) = \\frac{n(E)}{n(S)} = \\frac{\\text{Number of favourable outcomes}}{\\text{Total number of possible outcomes}} \\]\n\n"
        "2. **Relative Frequency:** The actual proportion of times an event occurred during a physical experiment or trial:\n"
        "\\[ \\text{Relative Frequency} = \\frac{\\text{Observed frequency of event}}{\\text{Total number of trials performed}} \\]"
    )
    ans = "Theoretical probability is calculated mathematically (n(E)/n(S)); Relative frequency is measured from actual experiment trials (frequency/trials)"
    return {
        "id": f"g8_prob_theory_vs_exp_{rng.randint(100000, 999999)}",
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
        "subskill": "14_relative_frequency_vs_theoretical_probability_comparison",
        "learning_objective_id": "math_g8_prob_theory_vs_exp",
        "hints": {
            "tier_1": "One is calculated before the experiment; the other is measured from real trials.",
            "tier_2": "Theoretical: n(E)/n(S); Relative frequency: observed / total trials.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_experimental_results_must_match_theoretical_values_exactly"],
    }


# ----------------------------------------------------------------------
# 15. Law of Large Numbers: Increased Trials Convergence
# ----------------------------------------------------------------------
def arch_15_law_of_large_numbers_increased_trials_convergence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two learners test a fair coin:\n"
        "- Learner A flips the coin **10 times** and gets 7 Heads (relative frequency = 70%).\n"
        "- Learner B flips the coin **1 000 times** and gets 508 Heads (relative frequency = 50,8%).\n\n"
        "1. Explain why Learner B's result is much closer to the theoretical probability of 50% than Learner A's.\n"
        "2. What general principle in probability does this illustrate?"
    )
    sol = (
        "**Explanation & Principle:**\n"
        "1. In a small number of trials (e.g. 10 tosses), random chance fluctuations have a large percentage impact. "
        "Over a very large number of trials (e.g. 1 000 tosses), individual random variations average out, causing "
        "the relative frequency to stabilize and approach the theoretical probability.\n\n"
        "2. This illustrates the **Law of Large Numbers**: As the number of trials increases, the experimental "
        "relative frequency gets closer and closer to the theoretical probability."
    )
    ans = "1. Random fluctuations average out over many trials; 2. Law of Large Numbers (larger sample size approaches theoretical probability)"
    return {
        "id": f"g8_prob_lln_{rng.randint(100000, 999999)}",
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
        "subskill": "15_law_of_large_numbers_increased_trials_convergence",
        "learning_objective_id": "math_g8_prob_lln",
        "hints": {
            "tier_1": "Think about why more tests give a more reliable average.",
            "tier_2": "Law of Large Numbers states that relative frequency converges to theoretical probability as trials increase.",
            "tier_3": ans,
        },
        "misconception_tags": ["believing_10_trials_is_sufficient_to_disprove_a_fair_coin"],
    }


# ----------------------------------------------------------------------
# 16. Fair vs Unfair Game: Definition and Criterion
# ----------------------------------------------------------------------
def arch_16_fair_vs_unfair_game_definition_and_criterion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In probability, games of chance are classified as either **fair** or **unfair**.\n\n"
        "1. Give the precise mathematical definition of a **fair game**.\n"
        "2. What condition must be met for two competing players (Player A and Player B) in a fair game?"
    )
    sol = (
        "**1. Definition of a Fair Game:**\n"
        "A game in which every player has an equal chance of winning and an equal chance of losing, "
        "with no built-in mathematical advantage or bias towards any participant.\n\n"
        "**2. Mathematical Condition:**\n"
        "\\[ P(\\text{Player A wins}) = P(\\text{Player B wins}) \\]\n"
        "If there are two players and no draws, \\(P(\\text{Win}) = \\frac{1}{2} = 0{,}5\\)."
    )
    ans = "1. Every player has an equal probability of winning; 2. P(Player A wins) = P(Player B wins) = 0,5"
    return {
        "id": f"g8_prob_fair_def_{rng.randint(100000, 999999)}",
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
        "subskill": "16_fair_vs_unfair_game_definition_and_criterion",
        "learning_objective_id": "math_g8_prob_fair_def",
        "hints": {
            "tier_1": "Fair means equal chance for both players.",
            "tier_2": "P(Win) must equal P(Lose) = 1/2.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_fairness_with_luck"],
    }


# ----------------------------------------------------------------------
# 17. Fair Game Analysis: Dice Rules Even vs Odd
# ----------------------------------------------------------------------
def arch_17_fair_game_analysis_dice_rules_even_vs_odd(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Thabo and Zola play a dice game using a single fair 6-sided die.\n"
        "The rules are:\n"
        "- If an **even number** (2, 4, 6) is rolled, Thabo wins 1 point.\n"
        "- If an **odd number** (1, 3, 5) is rolled, Zola wins 1 point.\n\n"
        "1. Calculate the probability of Thabo winning on a roll.\n"
        "2. Calculate the probability of Zola winning on a roll.\n"
        "3. Is this game fair? Justify your answer mathematically."
    )
    sol = (
        "**Game Analysis:**\n"
        "1. Thabo's winning outcomes: {2, 4, 6} \\(\\implies P(\\text{Thabo}) = \\frac{3}{6} = \\frac{1}{2}\\).\n"
        "2. Zola's winning outcomes: {1, 3, 5} \\(\\implies P(\\text{Zola}) = \\frac{3}{6} = \\frac{1}{2}\\).\n"
        "3. **Fairness:** The game **is fair** because both players have an identical theoretical probability of winning "
        "(\\(P = \\frac{1}{2}\\))."
    )
    ans = "1. 1/2; 2. 1/2; 3. Yes, fair because both probabilities are equal to 1/2"
    return {
        "id": f"g8_prob_fair_game_{rng.randint(100000, 999999)}",
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
        "subskill": "17_fair_game_analysis_dice_rules_even_vs_odd",
        "learning_objective_id": "math_g8_prob_fair_game",
        "hints": {
            "tier_1": "Calculate the probability for each player.",
            "tier_2": "Thabo: 3/6; Zola: 3/6.",
            "tier_3": "Equal probabilities mean the game is fair.",
        },
        "misconception_tags": ["assuming_the_first_player_always_has_an_advantage"],
    }


# ----------------------------------------------------------------------
# 18. Unfair Game Analysis: Asymmetric Scoring Rules
# ----------------------------------------------------------------------
def arch_18_unfair_game_analysis_asymmetric_scoring_rules(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A carnival game operator uses a fair 6-sided die with the following rules:\n"
        "- A player wins a prize ONLY if a **6** is rolled.\n"
        "- The operator wins if any other number (1, 2, 3, 4, or 5) is rolled.\n\n"
        "1. Calculate the player's probability of winning.\n"
        "2. Calculate the operator's probability of winning.\n"
        "3. Is the game fair or unfair? Explain why carnival games are designed this way."
    )
    sol = (
        "**Analysis:**\n"
        "1. Player wins on {6}: \\(P(\\text{Player}) = \\frac{1}{6}\\).\n"
        "2. Operator wins on {1, 2, 3, 4, 5}: \\(P(\\text{Operator}) = \\frac{5}{6}\\).\n"
        "3. **Fairness:** The game is **unfair** (biased towards the operator). Carnival and casino games are intentionally "
        "designed with asymmetric rules so that the house/operator has a much higher mathematical probability of winning "
        "over many rounds, ensuring profitability."
    )
    ans = "1. 1/6; 2. 5/6; 3. Unfair; designed with a house edge so the operator makes a long-term profit"
    return {
        "id": f"g8_prob_unfair_game_{rng.randint(100000, 999999)}",
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
        "subskill": "18_unfair_game_analysis_asymmetric_scoring_rules",
        "learning_objective_id": "math_g8_prob_unfair_game",
        "hints": {
            "tier_1": "Player has 1 winning outcome; operator has 5 winning outcomes.",
            "tier_2": "1/6 vs 5/6.",
            "tier_3": ans,
        },
        "misconception_tags": ["believing_each_player_has_a_50_percent_chance_regardless_of_rules"],
    }


# ----------------------------------------------------------------------
# 19. Spinner: Equal Sectors Probability (WITH SVG)
# ----------------------------------------------------------------------
def arch_19_spinner_equal_sectors_probability(rng: random.Random) -> Dict[str, Any]:
    n_sectors = rng.choice([4, 5, 8])
    if n_sectors == 4:
        sectors = [("Red", "#f87171", 0.25), ("Blue", "#60a5fa", 0.25), ("Green", "#4ade80", 0.25), ("Yellow", "#facc15", 0.25)]
        target = "Blue"
        prob_str = "1/4"
    elif n_sectors == 5:
        sectors = [("1", "#f87171", 0.2), ("2", "#60a5fa", 0.2), ("3", "#4ade80", 0.2), ("4", "#facc15", 0.2), ("5", "#c084fc", 0.2)]
        target = "3"
        prob_str = "1/5"
    else:
        sectors = [(str(i), "#cbd5e1" if i % 2 == 0 else "#93c5fd", 0.125) for i in range(1, 9)]
        target = "even number"
        prob_str = "4/8 = 1/2"

    svg = draw_spinner_svg(sectors, seed=rng.randint(100, 999999))

    prompt = (
        f"A circular spinner is divided into **{n_sectors} equal sectors**.\n\n"
        f"Calculate the theoretical probability of the spinner landing on **{target}** when spun once."
    )
    sol = (
        f"**Calculation of Spinner Probability:**\n"
        f"Since all {n_sectors} sectors have identical angles and areas, each sector has an equal probability:\n"
        f"\\[ P = \\frac{{n(E)}}{{n(S)}} = {prob_str} \\]"
    )
    ans = prob_str.split("=")[-1].strip()
    return {
        "id": f"g8_prob_spin_eq_{rng.randint(100000, 999999)}",
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
        "subskill": "19_spinner_equal_sectors_probability",
        "learning_objective_id": "math_g8_prob_spin_eq",
        "hints": {
            "tier_1": f"All {n_sectors} sectors are equal in size.",
            "tier_2": f"Favourable sectors divided by {n_sectors}.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_the_pointer_position_before_spinning_affects_the_result"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 20. Spinner: Unequal Sectors Probability (WITH SVG)
# ----------------------------------------------------------------------
def arch_20_spinner_unequal_sectors_probability(rng: random.Random) -> Dict[str, Any]:
    # Half red (1/2), quarter blue (1/4), quarter green (1/4)
    sectors = [("Red (180°)", "#f87171", 0.5), ("Blue (90°)", "#60a5fa", 0.25), ("Green (90°)", "#4ade80", 0.25)]
    svg = draw_spinner_svg(sectors, seed=rng.randint(100, 999999))

    prompt = (
        "A circular spinner has unequal sectors:\n"
        "- Red occupies a semicircle (angle of 180°)\n"
        "- Blue occupies a quarter-circle (angle of 90°)\n"
        "- Green occupies a quarter-circle (angle of 90°)\n\n"
        "1. Calculate the theoretical probability of the spinner landing on Red.\n"
        "2. Calculate the theoretical probability of the spinner landing on Blue.\n"
        "3. Are the outcomes Red, Blue, and Green equally likely? Explain."
    )
    sol = (
        "**Sector Angle Calculations:**\n"
        "A full circle has 360°:\n"
        "1. \\(P(\\text{Red}) = \\frac{180^\\circ}{360^\\circ} = \\frac{1}{2} = 50\\%\\)\n"
        "2. \\(P(\\text{Blue}) = \\frac{90^\\circ}{360^\\circ} = \\frac{1}{4} = 25\\%\\)\n"
        "3. **Equally likely?** No. Red is twice as likely as Blue or Green because its sector area is twice as large."
    )
    ans = "1. 1/2; 2. 1/4; 3. No, Red has twice the area of Blue or Green"
    return {
        "id": f"g8_prob_spin_uneq_{rng.randint(100000, 999999)}",
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
        "subskill": "20_spinner_unequal_sectors_probability",
        "learning_objective_id": "math_g8_prob_spin_uneq",
        "hints": {
            "tier_1": "Divide each sector angle by 360°.",
            "tier_2": "180/360 = 1/2; 90/360 = 1/4.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_unequal_sectors_as_having_equal_probability_one_third_each"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 21. Marbles in Bag: Single Color Selection
# ----------------------------------------------------------------------
def arch_21_marbles_in_bag_single_color_selection(rng: random.Random) -> Dict[str, Any]:
    red = rng.choice([4, 5, 6])
    blue = rng.choice([3, 4, 5])
    green = rng.choice([2, 3])
    total = red + blue + green

    target_color = rng.choice(["Red", "Blue", "Green"])
    count = red if target_color == "Red" else (blue if target_color == "Blue" else green)
    gcd = math.gcd(count, total)
    sim_num = count // gcd
    sim_den = total // gcd

    prompt = (
        f"An opaque bag contains **{red} red marbles**, **{blue} blue marbles**, and **{green} green marbles**.\n"
        f"A marble is picked at random from the bag without looking.\n\n"
        f"1. What is the total number of marbles in the bag?\n"
        f"2. Calculate the theoretical probability of picking a **{target_color}** marble, expressing your answer in simplest fractional form."
    )
    sol = (
        f"**Calculation:**\n"
        f"1. Total marbles: \\(n(S) = {red} + {blue} + {green} = {total}\\)\n"
        f"2. Favourable {target_color} marbles: \\(n({target_color}) = {count}\\)\n"
        f"\\[ P({target_color}) = \\frac{{{count}}}{{{total}}} = \\frac{{{sim_num}}}{{{sim_den}}} \\]"
    )
    ans = f"1. {total}; 2. {sim_num}/{sim_den}"
    return {
        "id": f"g8_prob_marbles_{rng.randint(100000, 999999)}",
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
        "subskill": "21_marbles_in_bag_single_color_selection",
        "learning_objective_id": "math_g8_prob_marbles",
        "hints": {
            "tier_1": f"Add all marbles to find the total: {total}.",
            "tier_2": f"Divide {count} by {total} and simplify.",
            "tier_3": f"{sim_num}/{sim_den}.",
        },
        "misconception_tags": ["dividing_by_other_colored_marbles_instead_of_total"],
    }


# ----------------------------------------------------------------------
# 22. Marbles in Bag: Complementary Event ('Not Color')
# ----------------------------------------------------------------------
def arch_22_marbles_in_bag_not_color_complementary_event(rng: random.Random) -> Dict[str, Any]:
    red = 5
    blue = 7
    yellow = 8
    total = red + blue + yellow  # 20

    # P(not red) = (blue + yellow)/20 = 15/20 = 3/4
    not_red = blue + yellow
    prompt = (
        f"A box contains **{red} red counters**, **{blue} blue counters**, and **{yellow} yellow counters**.\n"
        f"A counter is drawn at random.\n\n"
        f"Calculate the theoretical probability that the counter drawn is **NOT red**, showing two different methods:\n"
        f"- Method 1: Adding the non-red counters.\n"
        f"- Method 2: Using the complement rule \\(P(\\text{{not }} E) = 1 - P(E)\\)."
    )
    sol = (
        f"**Total counters:** \\(n(S) = {red} + {blue} + {yellow} = {total}\\).\n\n"
        f"**Method 1 (Direct Count):**\n"
        f"Non-red counters = \\({blue} + {yellow} = {not_red}\\).\n"
        f"\\[ P(\\text{{not red}}) = \\frac{{{not_red}}}{{{total}}} = \\frac{{3}}{{4}} \\]\n\n"
        f"**Method 2 (Complement Rule):**\n"
        f"\\[ P(\\text{{red}}) = \\frac{{{red}}}{{{total}}} = \\frac{{5}}{{20}} = \\frac{{1}}{{4}} \\]\n"
        f"\\[ P(\\text{{not red}}) = 1 - P(\\text{{red}}) = 1 - \\frac{{1}}{{4}} = \\frac{{3}}{{4}} \\]"
    )
    ans = "3/4 (or 15/20 = 75%)"
    return {
        "id": f"g8_prob_not_red_{rng.randint(100000, 999999)}",
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
        "subskill": "22_marbles_in_bag_not_color_complementary_event",
        "learning_objective_id": "math_g8_prob_not_red",
        "hints": {
            "tier_1": f"Total counters = {total}. Non-red counters = {blue} + {yellow} = {not_red}.",
            "tier_2": f"Or 1 - (5/20) = 15/20.",
            "tier_3": "3/4.",
        },
        "misconception_tags": ["calculating_p_red_instead_of_p_not_red"],
    }


# ----------------------------------------------------------------------
# 23. Marbles in Bag: Effect of Adding or Removing Marbles
# ----------------------------------------------------------------------
def arch_23_marbles_in_bag_adding_or_removing_marbles_effect(rng: random.Random) -> Dict[str, Any]:
    orig_red = 6
    orig_total = 10
    added_red = rng.choice([2, 5, 10])
    new_red = orig_red + added_red
    new_total = orig_total + added_red

    p1 = orig_red / orig_total
    p2 = new_red / new_total

    prompt = (
        f"A bag originally contains 6 red marbles and 4 blue marbles (total 10 marbles).\n"
        f"Then, **{added_red} more red marbles** are added to the bag (with no blue marbles added).\n\n"
        f"1. Calculate the original probability of picking a red marble.\n"
        f"2. Calculate the new probability of picking a red marble after adding the {added_red} red marbles.\n"
        f"3. Explain why the probability of picking red increased."
    )
    sol = (
        f"**1. Original Probability:** \\(P_1 = \\frac{{6}}{{10}} = 0{{,}}6 = 60\\%\\)\n\n"
        f"**2. New Probability:**\n"
        f"New red count: \\(6 + {added_red} = {new_red}\\)\n"
        f"New total: \\(10 + {added_red} = {new_total}\\)\n"
        f"\\[ P_2 = \\frac{{{new_red}}}{{{new_total}}} = {_fmt_dec(p2, 2)} \\]\n\n"
        f"**3. Reason:** The proportion of red marbles relative to the total number in the bag increased."
    )
    ans = f"1. 6/10 (60%); 2. {new_red}/{new_total}; 3. Red proportion increased"
    return {
        "id": f"g8_prob_add_marbles_{rng.randint(100000, 999999)}",
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
        "subskill": "23_marbles_in_bag_adding_or_removing_marbles_effect",
        "learning_objective_id": "math_g8_prob_add_marbles",
        "hints": {
            "tier_1": f"Add {added_red} to BOTH the red count and the total count.",
            "tier_2": f"New fraction: {new_red} / {new_total}.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_marbles_only_to_numerator_forgetting_denominator_change"],
    }


# ----------------------------------------------------------------------
# 24. Standard Playing Cards: Suit Selection
# ----------------------------------------------------------------------
def arch_24_standard_playing_cards_suit_selection(rng: random.Random) -> Dict[str, Any]:
    suit = rng.choice(["Hearts", "Diamonds", "Spades", "Clubs"])
    color = "red" if suit in ("Hearts", "Diamonds") else "black"

    prompt = (
        f"A standard deck of playing cards contains 52 cards divided equally into 4 suits:\n"
        f"Hearts (red), Diamonds (red), Spades (black), and Clubs (black).\n"
        f"A card is chosen at random from a well-shuffled deck.\n\n"
        f"1. What is the theoretical probability of selecting a **{suit}** card?\n"
        f"2. What is the theoretical probability of selecting any **{color}** card?"
    )
    sol = (
        f"**Card Probabilities:**\n"
        f"1. Each suit has 13 cards out of 52:\n"
        f"\\[ P(\\text{{{suit}}}) = \\frac{{13}}{{52}} = \\frac{{1}}{{4}} = 25\\% \\]\n"
        f"2. There are 26 {color} cards (2 suits of 13) out of 52:\n"
        f"\\[ P(\\text{{{color}}}) = \\frac{{26}}{{52}} = \\frac{{1}}{{2}} = 50\\% \\]"
    )
    ans = "1. 1/4 (or 13/52); 2. 1/2 (or 26/52)"
    return {
        "id": f"g8_prob_cards_suit_{rng.randint(100000, 999999)}",
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
        "subskill": "24_standard_playing_cards_suit_selection",
        "learning_objective_id": "math_g8_prob_cards_suit",
        "hints": {
            "tier_1": "There are 4 suits (13 cards each) and 2 colors (26 cards each).",
            "tier_2": "13/52 = 1/4; 26/52 = 1/2.",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_there_are_52_cards_in_a_standard_deck"],
    }


# ----------------------------------------------------------------------
# 25. Standard Playing Cards: Face Card or Ace
# ----------------------------------------------------------------------
def arch_25_standard_playing_cards_face_card_or_ace(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["face card (Jack, Queen, or King)", "Ace"])
    if "face" in choice:
        count = 12  # 3 * 4
        frac_str = "12/52 = 3/13"
    else:
        count = 4   # 4 aces
        frac_str = "4/52 = 1/13"

    prompt = (
        f"A card is chosen at random from a complete standard deck of 52 playing cards.\n\n"
        f"Calculate the theoretical probability of selecting a **{choice}**, expressing your answer in simplified form."
    )
    sol = (
        f"**Calculation:**\n"
        f"- Total cards in deck: \\(n(S) = 52\\).\n"
        f"- Number of {choice}s: \\(n(E) = {count}\\).\n"
        f"\\[ P = \\frac{{{count}}}{{52}} = {frac_str} \\]"
    )
    ans = frac_str.split("=")[-1].strip()
    return {
        "id": f"g8_prob_cards_face_{rng.randint(100000, 999999)}",
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
        "subskill": "25_standard_playing_cards_face_card_or_ace",
        "learning_objective_id": "math_g8_prob_cards_face",
        "hints": {
            "tier_1": f"Count how many {choice}s are in the deck of 52.",
            "tier_2": f"{count} out of 52.",
            "tier_3": ans,
        },
        "misconception_tags": ["counting_aces_as_face_cards_or_miscounting_face_cards"],
    }
