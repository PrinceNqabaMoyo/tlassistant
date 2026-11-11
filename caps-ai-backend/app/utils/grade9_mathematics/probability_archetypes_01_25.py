"""Grade 9 Mathematics - Probability Archetypes 01-25 (CAPS Term 4).
Focus: Probability scale (0 to 1), fraction/decimal/percentage representations, single-event probabilities
(coins, dice, spinners, playing cards, marble bags), complementary events, experimental relative frequency,
and two-stage independent events (coins, dice).
100% deterministic, zero LLM calls.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.probability_svg import (
    draw_probability_spinner_svg,
    draw_two_stage_tree_diagram_svg,
)


def _fmt(val: float, decimals: int = 1) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# -----------------------------------------------------------------------------
# 01. Probability Scale: Words to Numbers (0 to 1)
# -----------------------------------------------------------------------------
def arch_01_probability_scale_impossible_certain_words_to_numbers(r: random.Random) -> Dict[str, Any]:
    events = [
        ("The sun rising in the east tomorrow morning", "Certain", "1 (or 100%)", 1.0),
        ("A standard six-sided die landing on the number 8", "Impossible", "0 (or 0%)", 0.0),
        ("A tossed fair coin landing on Heads", "Even chance (equally likely)", "0,5 (or 50% or 1/2)", 0.5),
        ("Snow falling in the middle of summer in Durban", "Extremely unlikely / Impossible", "Close to 0", 0.0),
        ("Selecting a red marble from a bag containing 9 red and 1 blue", "Very likely", "0,9 (or 90%)", 0.9),
        ("Selecting a green marble from a bag containing 1 green and 9 blue", "Very unlikely", "0,1 (or 10%)", 0.1),
    ]
    evt, word_desc, num_desc, val = r.choice(events)

    prompt = (
        f"Consider the event: **\"{evt}\"**.\n"
        f"1. Describe its probability using a word from the probability scale (e.g. Impossible, Unlikely, Even chance, Likely, Certain).\n"
        f"2. State its numerical probability value on the scale from $0$ to $1$."
    )
    ans_str = f"Word: {word_desc}; Numerical: {num_desc}"
    sol = (
        f"• Word description: **{word_desc}**\n"
        f"• Numerical probability: **{num_desc}**\n\n"
        f"On the probability scale:\n"
        f"• $0$ = Impossible\n"
        f"• $0,5$ = Even chance ($50\\%$)\n"
        f"• $1$ = Certain"
    )
    return {
        "subskill": "01_probability_scale_impossible_certain_words_to_numbers",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Word descriptor: {word_desc}", "marks": 1},
            {"step": f"Numerical probability: {num_desc}", "marks": 1},
        ],
        "hints": [
            "0 represents an impossible event; 1 represents a certainty.",
            "An even chance (like a fair coin flip) is 0,5 or 50%.",
        ],
        "misconception_tags": ["probability_scale_boundary_error"],
    }


# -----------------------------------------------------------------------------
# 02. Convert Probability Between Fraction, Decimal, and Percentage
# -----------------------------------------------------------------------------
def arch_02_convert_probability_between_fraction_decimal_percentage(r: random.Random) -> Dict[str, Any]:
    conversions = [
        (1, 4, "0,25", "25%"),
        (1, 2, "0,5", "50%"),
        (3, 4, "0,75", "75%"),
        (1, 5, "0,2", "20%"),
        (2, 5, "0,4", "40%"),
        (3, 5, "0,6", "60%"),
        (4, 5, "0,8", "80%"),
        (1, 10, "0,1", "10%"),
        (3, 10, "0,3", "30%"),
        (7, 10, "0,7", "70%"),
    ]
    num, den, dec_str, pct_str = r.choice(conversions)

    prompt = (
        f"The probability of an event is given as the simplified fraction $P(E) = \\frac{{{num}}}{{{den}}}$.\n"
        f"1. Convert this probability into a **decimal** (using a comma decimal separator).\n"
        f"2. Convert this probability into a **percentage**."
    )
    ans_str = f"Decimal: {dec_str}; Percentage: {pct_str}"
    sol = (
        f"1. Decimal: $\\frac{{{num}}}{{{den}}} = {dec_str}$\n"
        f"2. Percentage: $\\frac{{{num}}}{{{den}}} \\times 100\\% = {pct_str}$"
    )
    return {
        "subskill": "02_convert_probability_between_fraction_decimal_percentage",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Decimal conversion: {dec_str}", "marks": 1},
            {"step": f"Percentage conversion: {pct_str}", "marks": 1},
        ],
        "hints": [
            f"Divide {num} by {den} to find the decimal.",
            "Multiply the decimal by 100 to find the percentage.",
        ],
        "misconception_tags": ["fraction_to_decimal_percentage_conversion_error"],
    }


# -----------------------------------------------------------------------------
# 03. Single Event: Fair Coin Toss
# -----------------------------------------------------------------------------
def arch_03_single_event_fair_coin_toss(r: random.Random) -> Dict[str, Any]:
    target = r.choice(["Heads", "Tails"])
    prompt = (
        f"A fair South African R5 coin is tossed once into the air.\n"
        f"Calculate the theoretical probability of obtaining **{target}**, "
        f"expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{2}"
    sol = (
        "Sample space $S = \\{\\text{Heads}, \\text{Tails}\\}$, so $n(S) = 2$.\n"
        f"Event $E = \\{{\\text{{{target}}}\\}}, so $n(E) = 1$.\n"
        f"$$P(\\text{{{target}}}) = \\frac{{n(E)}}{{n(S)}} = \\frac{{1}}{{2}}$$"
    )
    return {
        "subskill": "03_single_event_fair_coin_toss",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/2",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State sample space size n(S) = 2", "marks": 1},
            {"step": "P(E) = 1/2", "marks": 1},
        ],
        "hints": [
            "A coin has 2 equally likely faces: Heads and Tails.",
            "Probability = (Favourable outcomes) ÷ (Total possible outcomes) = 1 ÷ 2.",
        ],
        "misconception_tags": ["coin_toss_probability_error"],
    }


# -----------------------------------------------------------------------------
# 04. Single Event: Fair Six-Sided Die (Even or Odd)
# -----------------------------------------------------------------------------
def arch_04_single_event_fair_six_sided_die_even_odd(r: random.Random) -> Dict[str, Any]:
    target = r.choice(["an even number", "an odd number"])
    outcomes = "{2; 4; 6}" if "even" in target else "{1; 3; 5}"

    prompt = (
        f"A standard fair six-sided die is rolled once.\n"
        f"Calculate the probability of rolling **{target}**, expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{2}"
    sol = (
        f"Sample space $S = \\{{1; 2; 3; 4; 5; 6\\}}$, so $n(S) = 6$.\n"
        f"Favourable outcomes $E = {outcomes}$, so $n(E) = 3$.\n"
        f"$$P(E) = \\frac{{3}}{{6}} = \\frac{{1}}{{2}}$$"
    )
    return {
        "subskill": "04_single_event_fair_six_sided_die_even_odd",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/2",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"List favourable outcomes {outcomes} (n=3)", "marks": 1},
            {"step": "Simplify 3/6 to 1/2", "marks": 1},
        ],
        "hints": [
            "List the numbers from 1 to 6 that match the condition.",
            "There are 3 matching numbers out of 6 total faces. Simplify 3/6.",
        ],
        "misconception_tags": ["die_even_odd_fraction_simplification_error"],
    }


# -----------------------------------------------------------------------------
# 05. Single Event: Fair Six-Sided Die (Prime or Composite)
# -----------------------------------------------------------------------------
def arch_05_single_event_fair_six_sided_die_prime_composite(r: random.Random) -> Dict[str, Any]:
    is_prime = r.choice([True, False])
    if is_prime:
        target = "a prime number"
        outcomes = "{2; 3; 5}"
        k = 3
        ans_frac = "\\frac{1}{2}"
        note = "Note: 1 is neither prime nor composite; the primes are 2, 3, 5."
    else:
        target = "a composite number"
        outcomes = "{4; 6}"
        k = 2
        ans_frac = "\\frac{1}{3}"
        note = "Note: 1 is neither prime nor composite; the composite numbers are 4 and 6."

    prompt = (
        f"A standard fair six-sided die is rolled once.\n"
        f"Calculate the probability of rolling **{target}**, expressing your answer as a simplified fraction."
    )
    sol = (
        f"Sample space $S = \\{{1; 2; 3; 4; 5; 6\\}}$, so $n(S) = 6$.\n"
        f"{note}\n"
        f"Favourable outcomes $E = {outcomes}$, so $n(E) = {k}$.\n"
        f"$$P(E) = \\frac{{{k}}}{{6}} = {ans_frac}$$"
    )
    return {
        "subskill": "05_single_event_fair_six_sided_die_prime_composite",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/2" if is_prime else "1/3",
        "sample_answer": ans_frac,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"List favourable outcomes {outcomes}", "marks": 1},
            {"step": f"Calculate simplified fraction: {ans_frac}", "marks": 1},
        ],
        "hints": [
            "Remember that 1 is NEITHER prime nor composite.",
            f"Favourable outcomes are {outcomes}. Divide count by 6 and simplify.",
        ],
        "misconception_tags": ["one_is_not_prime_misconception"],
    }


# -----------------------------------------------------------------------------
# 06. Single Event: Fair Die Greater/Less Than Threshold
# -----------------------------------------------------------------------------
def arch_06_single_event_fair_six_sided_die_greater_than_threshold(r: random.Random) -> Dict[str, Any]:
    thresh = r.choice([2, 3, 4])
    favour = [x for x in range(1, 7) if x > thresh]
    k = len(favour)
    gcd_v = math.gcd(k, 6)
    simp_n = k // gcd_v
    simp_d = 6 // gcd_v
    ans_str = f"\\frac{{{simp_n}}}{{{simp_d}}}"

    prompt = (
        f"A standard fair six-sided die is rolled once.\n"
        f"Calculate the probability of rolling a number **strictly greater than {thresh}**, "
        f"expressing your answer as a simplified fraction."
    )
    sol = (
        f"Numbers strictly greater than {thresh} on a die: $\\{{{'; '.join(str(x) for x in favour)}\\}}$, so $n(E) = {k}$.\n"
        f"Total possible outcomes $n(S) = 6$.\n"
        f"$$P(\\text{{number}} > {thresh}) = \\frac{{{k}}}{{6}} = {ans_str}$$"
    )
    return {
        "subskill": "06_single_event_fair_six_sided_die_greater_than_threshold",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{simp_n}/{simp_d}",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify outcomes: {favour} (count={k})", "marks": 1},
            {"step": f"Simplify fraction to {simp_n}/{simp_d}", "marks": 1},
        ],
        "hints": [
            f"'Strictly greater than {thresh}' does not include {thresh}.",
            f"The matching numbers are {favour}.",
        ],
        "misconception_tags": ["strict_inequality_boundary_inclusion_error"],
    }


# -----------------------------------------------------------------------------
# 07. Single Event: Colored Spinner with Equal Sectors
# -----------------------------------------------------------------------------
def arch_07_single_event_colored_spinner_equal_sectors(r: random.Random) -> Dict[str, Any]:
    # 8 equal sectors: 3 Red, 2 Blue, 2 Green, 1 Yellow
    counts = [3, 2, 2, 1]
    labels = ["Red", "Blue", "Green", "Yellow"]
    total_sectors = sum(counts)  # 8

    target_idx = r.randint(0, 3)
    target_col = labels[target_idx]
    target_count = counts[target_idx]

    gcd_v = math.gcd(target_count, total_sectors)
    simp_n = target_count // gcd_v
    simp_d = total_sectors // gcd_v
    ans_str = f"\\frac{{{simp_n}}}{{{simp_d}}}"

    seed_val = r.randint(100, 999999)
    svg = draw_probability_spinner_svg(labels, counts, title="Fair 8-Sector Spinner", seed=seed_val)

    prompt = (
        f"A fair circular spinner has $8$ identical sectors divided as follows:\n"
        f"• $3$ Red sectors\n"
        f"• $2$ Blue sectors\n"
        f"• $2$ Green sectors\n"
        f"• $1$ Yellow sector\n\n"
        f"Calculate the theoretical probability that a single spin lands on **{target_col}**, "
        f"giving your answer as a simplified fraction."
    )
    sol = (
        f"Total sectors $n(S) = {total_sectors}$.\n"
        f"Sectors labelled {target_col}: $n(E) = {target_count}$.\n"
        f"$$P(\\text{{{target_col}}}) = \\frac{{{target_count}}}{{{total_sectors}}} = {ans_str}$$"
    )
    return {
        "subskill": "07_single_event_colored_spinner_equal_sectors",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": f"{simp_n}/{simp_d}",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State P({target_col}) = {target_count}/8", "marks": 1},
            {"step": f"Simplify to {simp_n}/{simp_d}", "marks": 1},
        ],
        "hints": [
            f"Count how many sectors are {target_col} ({target_count}) out of 8 total.",
            f"Simplify the fraction {target_count}/8.",
        ],
        "misconception_tags": ["spinner_fraction_reduction_error"],
    }


# -----------------------------------------------------------------------------
# 08. Single Event: Colored Spinner with Unequal Angles
# -----------------------------------------------------------------------------
def arch_08_single_event_colored_spinner_unequal_sectors(r: random.Random) -> Dict[str, Any]:
    angle = r.choice([45, 60, 90, 120, 135, 180])
    gcd_v = math.gcd(angle, 360)
    simp_n = angle // gcd_v
    simp_d = 360 // gcd_v
    ans_str = f"\\frac{{{simp_n}}}{{{simp_d}}}"
    pct = round((angle / 360) * 100, 1)

    prompt = (
        f"A circular spinner has a **Blue sector** with a central angle of ${angle}^\\circ$.\n"
        f"1. Calculate the probability of landing on Blue as a simplified fraction.\n"
        f"2. Express this probability as a percentage."
    )
    ans_text = f"Fraction: {simp_n}/{simp_d}; Percentage: {_fmt(pct)}%"
    sol = (
        f"A complete circle measures $360^\\circ$.\n"
        f"1. $$P(\\text{{Blue}}) = \\frac{{{angle}^\\circ}}{{360^\\circ}} = {ans_str}$$\n"
        f"2. Percentage: $\\frac{{{simp_n}}}{{{simp_d}}} \\times 100\\% = {_fmt(pct)}\\%$"
    )
    return {
        "subskill": "08_single_event_colored_spinner_unequal_sectors",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_text,
        "sample_answer": sol,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Fraction: {simp_n}/{simp_d}", "marks": 1},
            {"step": f"Percentage: {_fmt(pct)}%", "marks": 1},
        ],
        "hints": [
            f"Divide the sector angle ({angle}°) by the full circle (360°).",
            f"Simplify {angle}/360 and multiply by 100% for the percentage.",
        ],
        "misconception_tags": ["sector_angle_to_probability_error"],
    }


# -----------------------------------------------------------------------------
# 09. Single Event: Bag of Marbles (Simplified Fraction)
# -----------------------------------------------------------------------------
def arch_09_single_event_bag_marbles_simplified_fraction(r: random.Random) -> Dict[str, Any]:
    red = r.randint(4, 8)
    blue = r.randint(3, 6)
    green = r.randint(2, 5)
    total = red + blue + green

    gcd_v = math.gcd(blue, total)
    simp_n = blue // gcd_v
    simp_d = total // gcd_v
    ans_str = f"\\frac{{{simp_n}}}{{{simp_d}}}"

    prompt = (
        f"An opaque bag contains {red} red marbles, {blue} blue marbles, and {green} green marbles.\n"
        f"One marble is drawn at random from the bag.\n"
        f"Calculate the probability of selecting a **blue marble**, giving your answer as a simplified fraction."
    )
    sol = (
        f"Total marbles $n(S) = {red} + {blue} + {green} = {total}$.\n"
        f"Blue marbles $n(\\text{{Blue}}) = {blue}$.\n"
        f"$$P(\\text{{Blue}}) = \\frac{{{blue}}}{{{total}}} = {ans_str}$$"
    )
    return {
        "subskill": "09_single_event_bag_marbles_simplified_fraction",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{simp_n}/{simp_d}",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate total marbles: {total}", "marks": 1},
            {"step": f"Simplify {blue}/{total} to {simp_n}/{simp_d}", "marks": 1},
        ],
        "hints": [
            f"Find the total number of marbles: {red} + {blue} + {green} = {total}.",
            f"Divide the number of blue marbles ({blue}) by {total} and simplify.",
        ],
        "misconception_tags": ["marble_total_addition_error"],
    }


# -----------------------------------------------------------------------------
# 10. Single Event: Standard Deck of Cards (Suits)
# -----------------------------------------------------------------------------
def arch_10_single_event_standard_deck_suits(r: random.Random) -> Dict[str, Any]:
    suit = r.choice(["Hearts", "Diamonds", "Clubs", "Spades"])
    prompt = (
        f"A standard deck contains 52 playing cards (13 cards in each of 4 suits: Hearts, Diamonds, Clubs, Spades).\n"
        f"One card is drawn at random.\n"
        f"Calculate the probability of selecting a card belonging to the **{suit}** suit, "
        f"expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{4}"
    sol = (
        f"Total cards $n(S) = 52$.\n"
        f"Cards in the {suit} suit: $n(E) = 13$.\n"
        f"$$P(\\text{{{suit}}}) = \\frac{{13}}{{52}} = \\frac{{1}}{{4}}$$"
    )
    return {
        "subskill": "10_single_event_standard_deck_suits",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/4",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 13 favourable cards out of 52", "marks": 1},
            {"step": "Simplify 13/52 to 1/4", "marks": 1},
        ],
        "hints": [
            "There are 4 suits in a deck of cards, each with an equal number of cards (13).",
            "13 ÷ 52 simplifies to 1/4.",
        ],
        "misconception_tags": ["playing_card_deck_structure_unfamiliarity"],
    }


# -----------------------------------------------------------------------------
# 11. Single Event: Standard Deck (Face Cards)
# -----------------------------------------------------------------------------
def arch_11_single_event_standard_deck_face_cards(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a standard deck of 52 cards, the face cards are Jacks, Queens, and Kings (3 in each of 4 suits).\n"
        "One card is drawn at random.\n"
        "Calculate the probability of selecting a **face card (picture card)** as a simplified fraction."
    )
    ans_str = "\\frac{3}{13}"
    sol = (
        "Total cards $n(S) = 52$.\n"
        "Face cards: $3 \\times 4 = 12$ cards (Jack, Queen, King across 4 suits).\n"
        "$$P(\\text{Face Card}) = \\frac{12}{52} = \\frac{3}{13}$$"
    )
    return {
        "subskill": "11_single_event_standard_deck_face_cards",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/13",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 12 face cards in a deck", "marks": 1},
            {"step": "Simplify 12/52 to 3/13", "marks": 1},
        ],
        "hints": [
            "Count face cards: 4 Jacks + 4 Queens + 4 Kings = 12.",
            "Simplify the fraction 12/52 by dividing top and bottom by 4.",
        ],
        "misconception_tags": ["face_card_count_error"],
    }


# -----------------------------------------------------------------------------
# 12. Single Event: Standard Deck (Red Ace)
# -----------------------------------------------------------------------------
def arch_12_single_event_standard_deck_red_ace(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "One card is drawn at random from a standard well-shuffled pack of 52 cards.\n"
        "Calculate the probability of selecting a **Red Ace** (Ace of Hearts or Ace of Diamonds), "
        "expressed as a simplified fraction."
    )
    ans_str = "\\frac{1}{26}"
    sol = (
        "Total cards $n(S) = 52$.\n"
        "Red Aces: Ace of Hearts and Ace of Diamonds, so $n(E) = 2$.\n"
        "$$P(\\text{Red Ace}) = \\frac{2}{52} = \\frac{1}{26}$$"
    )
    return {
        "subskill": "12_single_event_standard_deck_red_ace",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/26",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify exactly 2 Red Aces", "marks": 1},
            {"step": "Simplify 2/52 to 1/26", "marks": 1},
        ],
        "hints": [
            "How many Red Aces exist in a pack? (Ace of Hearts, Ace of Diamonds).",
            "Simplify 2 ÷ 52.",
        ],
        "misconception_tags": ["card_colour_suit_intersection_error"],
    }


# -----------------------------------------------------------------------------
# 13. Complementary Event: Not Landing on Color
# -----------------------------------------------------------------------------
def arch_13_complementary_event_not_landing_on_color(r: random.Random) -> Dict[str, Any]:
    # P(E) = 3/10 -> P(not E) = 7/10
    num = r.choice([1, 2, 3, 4])
    den = 10
    comp_num = den - num
    ans_str = f"\\frac{{{comp_num}}}{{{den}}}"

    prompt = (
        f"The probability of a spinner landing on Red is $P(\\text{{Red}}) = \\frac{{{num}}}{{{den}}}$.\n"
        f"Calculate the probability of the spinner **NOT landing on Red** ($P(\\text{{not Red}})$), "
        f"giving your answer as a fraction."
    )
    sol = (
        f"Complementary rule: $P(\\text{{not }} E) = 1 - P(E)$.\n"
        f"$$P(\\text{{not Red}}) = 1 - \\frac{{{num}}}{{{den}}} = \\frac{{{den} - {num}}}{{{den}}} = {ans_str}$$"
    )
    return {
        "subskill": "13_complementary_event_not_landing_on_color",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{comp_num}/{den}",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Use complement rule: 1 - {num}/{den}", "marks": 1},
            {"step": f"Result: {comp_num}/{den}", "marks": 1},
        ],
        "hints": [
            "The sum of an event and its complement is always 1.",
            f"Subtract {num}/{den} from 1.",
        ],
        "misconception_tags": ["complementary_event_subtraction_error"],
    }


# -----------------------------------------------------------------------------
# 14. Complementary Event: Not Rolling a Six
# -----------------------------------------------------------------------------
def arch_14_complementary_event_not_rolling_six(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fair standard die is rolled once.\n"
        "Calculate the probability of **NOT rolling a 6**, expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{5}{6}"
    sol = (
        "Favourable outcomes for 'not 6': $\\{1; 2; 3; 4; 5\\}$, so $n(E) = 5$.\n"
        "$$P(\\text{not } 6) = 1 - P(6) = 1 - \\frac{1}{6} = \\frac{5}{6}$$"
    )
    return {
        "subskill": "14_complementary_event_not_rolling_six",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "5/6",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State P(6) = 1/6 or count 5 non-six faces", "marks": 1},
            {"step": "Result = 5/6", "marks": 1},
        ],
        "hints": [
            "How many faces on a die are NOT a 6? (1, 2, 3, 4, 5).",
            "5 out of 6 faces match.",
        ],
        "misconception_tags": ["die_complementary_probability_error"],
    }


# -----------------------------------------------------------------------------
# 15. Complementary Event: Weather Forecast Rain
# -----------------------------------------------------------------------------
def arch_15_complementary_event_weather_forecast_rain(r: random.Random) -> Dict[str, Any]:
    pct_rain = r.choice([25, 30, 40, 65, 70, 80])
    pct_dry = 100 - pct_rain

    prompt = (
        f"The weather forecast states there is a **{pct_rain}% chance of rain** in Johannesburg tomorrow.\n"
        f"1. What is the probability that it will **NOT rain** tomorrow (as a percentage)?\n"
        f"2. Express the probability that it will not rain as a decimal."
    )
    dec_dry = pct_dry / 100.0
    ans_str = f"Percentage: {pct_dry}%; Decimal: {_fmt(dec_dry, 2)}"
    sol = (
        f"1. $P(\\text{{no rain}}) = 100\\% - {pct_rain}\\% = {pct_dry}\\%$\n"
        f"2. Decimal: $\\frac{{{pct_dry}}}{{100}} = {_fmt(dec_dry, 2)}$"
    )
    return {
        "subskill": "15_complementary_event_weather_forecast_rain",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.01,
        "marking_schema": [
            {"step": f"Percentage: 100% - {pct_rain}% = {pct_dry}%", "marks": 1},
            {"step": f"Decimal: {_fmt(dec_dry, 2)}", "marks": 1},
        ],
        "hints": [
            f"Subtract {pct_rain}% from 100%.",
            f"Divide {pct_dry} by 100 to get the decimal.",
        ],
        "misconception_tags": ["percentage_complement_subtraction_error"],
    }


# -----------------------------------------------------------------------------
# 16. Experimental Relative Frequency: Coin Toss Trials
# -----------------------------------------------------------------------------
def arch_16_experimental_relative_frequency_coin_toss_trials(r: random.Random) -> Dict[str, Any]:
    trials = 200
    heads = r.randint(95, 115)
    rel_freq = round(heads / trials, 3)

    prompt = (
        f"In a science experiment, a coin was tossed $N = {trials}$ times and landed on Heads ${heads}$ times.\n"
        f"1. Calculate the **relative frequency** of landing on Heads (to 3 decimal places).\n"
        f"2. State the **theoretical probability** of landing on Heads for a fair coin (as a decimal)."
    )
    ans_str = f"Relative Frequency: {_fmt(rel_freq, 3)}; Theoretical: 0,5"
    sol = (
        f"1. $\\text{{Relative Frequency}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total Trials}}}} = \\frac{{{heads}}}{{{trials}}} = {_fmt(rel_freq, 3)}$\n"
        f"2. $\\text{{Theoretical Probability}} = \\frac{{1}}{{2}} = 0,5$"
    )
    return {
        "subskill": "16_experimental_relative_frequency_coin_toss_trials",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.005,
        "marking_schema": [
            {"step": f"Relative frequency calculation: {heads}/{trials} = {_fmt(rel_freq, 3)}", "marks": 1},
            {"step": "Theoretical probability: 0,5 (or 1/2)", "marks": 1},
        ],
        "hints": [
            f"Relative frequency = (Count of Heads) ÷ (Total tosses) = {heads} ÷ {trials}.",
            "A fair coin has a theoretical probability of 1/2 = 0,5.",
        ],
        "misconception_tags": ["experimental_vs_theoretical_probability_confusion"],
    }


# -----------------------------------------------------------------------------
# 17. Experimental Relative Frequency: Die Roll Trials
# -----------------------------------------------------------------------------
def arch_17_experimental_relative_frequency_die_roll_trials(r: random.Random) -> Dict[str, Any]:
    trials = 300
    fours = r.randint(45, 58)
    rel_freq = round(fours / trials, 3)
    theo = round(1 / 6, 3)

    prompt = (
        f"A learner rolled a die $N = {trials}$ times and recorded a 4 exactly ${fours}$ times.\n"
        f"1. Calculate the experimental relative frequency of rolling a 4 (to 3 decimal places).\n"
        f"2. State the theoretical probability of rolling a 4 (as a fraction and to 3 decimal places)."
    )
    ans_str = f"Relative frequency: {_fmt(rel_freq, 3)}; Theoretical: 1/6 ({_fmt(theo, 3)})"
    sol = (
        f"1. $\\text{{Relative Frequency}} = \\frac{{{fours}}}{{{trials}}} = {_fmt(rel_freq, 3)}$\n"
        f"2. $\\text{{Theoretical Probability}} = \\frac{{1}}{{6}} \\approx {_fmt(theo, 3)}$"
    )
    return {
        "subskill": "17_experimental_relative_frequency_die_roll_trials",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.005,
        "marking_schema": [
            {"step": f"Relative frequency: {fours}/{trials} = {_fmt(rel_freq, 3)}", "marks": 1},
            {"step": f"Theoretical: 1/6 ≈ {_fmt(theo, 3)}", "marks": 1},
        ],
        "hints": [
            f"Divide {fours} by {trials}.",
            "Theoretical probability of a specific face is 1/6.",
        ],
        "misconception_tags": ["die_relative_frequency_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 18. Law of Large Numbers Comparison
# -----------------------------------------------------------------------------
def arch_18_law_of_large_numbers_comparison_small_vs_large_trials(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Learner A tosses a coin 10 times and gets 8 Heads (relative frequency = 0,8).\n"
        "Learner B tosses the same coin 1 000 times and gets 508 Heads (relative frequency = 0,508).\n"
        "Explain what the **Law of Large Numbers** tells us about which learner's result is closer to the true probability."
    )
    concept = "The Law of Large Numbers states that as the number of experimental trials increases, the relative frequency gets closer and closer to the theoretical probability (0,5). Therefore, Learner B's result with 1 000 trials is far more reliable."
    return {
        "subskill": "18_law_of_large_numbers_comparison_small_vs_large_trials",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Learner B (1 000 trials) per Law of Large Numbers",
        "sample_answer": concept,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that larger sample size (1 000 trials) is more reliable", "marks": 1},
            {"step": "Explain Law of Large Numbers: relative frequency converges to theoretical probability", "marks": 1},
        ],
        "hints": [
            "In a small trial (like 10 tosses), random chance causes huge swings.",
            "Over 1 000 trials, deviations average out toward 0,5.",
        ],
        "misconception_tags": ["law_of_large_numbers_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 19. Sample Space Enumeration: Two Coins
# -----------------------------------------------------------------------------
def arch_19_sample_space_enumeration_two_coins(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair coins are tossed simultaneously.\n"
        "1. Write down the complete sample space $S$ using $H$ for Heads and $T$ for Tails.\n"
        "2. State the total number of possible outcomes, $n(S)$."
    )
    ans_str = "S = {(H, H), (H, T), (T, H), (T, T)}; n(S) = 4"
    sol = (
        "1. Complete sample space:\n"
        "$$S = \\{(H, H); (H, T); (T, H); (T, T)\\}$$\n"
        "2. Total outcomes: $n(S) = 2 \\times 2 = 4$."
    )
    return {
        "subskill": "19_sample_space_enumeration_two_coins",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "List all 4 outcomes: (H,H), (H,T), (T,H), (T,T)", "marks": 1},
            {"step": "State n(S) = 4", "marks": 1},
        ],
        "hints": [
            "First coin can be H or T (2 possibilities). Second coin can be H or T (2 possibilities).",
            "Total = 2 × 2 = 4 outcomes.",
        ],
        "misconception_tags": ["omitting_order_in_two_coins_sample_space"],
    }


# -----------------------------------------------------------------------------
# 20. Compound Event: Two Coins Both Heads
# -----------------------------------------------------------------------------
def arch_20_compound_event_two_coins_both_heads(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair coins are flipped simultaneously.\n"
        "Calculate the probability of obtaining **two Heads** (both coins landing on Heads), "
        "giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{4}"
    sol = (
        "Sample space $S = \\{(H, H); (H, T); (T, H); (T, T)\\}$, so $n(S) = 4$.\n"
        "Event 'both Heads' $E = \\{(H, H)\\}$, so $n(E) = 1$.\n"
        "$$P(\\text{both Heads}) = \\frac{1}{4}$$"
    )
    return {
        "subskill": "20_compound_event_two_coins_both_heads",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/4",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 1 favourable outcome (H,H) out of 4 total", "marks": 1},
            {"step": "P = 1/4", "marks": 1},
        ],
        "hints": [
            "List all 4 outcomes: HH, HT, TH, TT.",
            "Only 1 outcome has two Heads (HH).",
        ],
        "misconception_tags": ["two_coins_independence_multiplication_error"],
    }


# -----------------------------------------------------------------------------
# 21. Compound Event: Two Coins At Least One Tail
# -----------------------------------------------------------------------------
def arch_21_compound_event_two_coins_at_least_one_tail(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair coins are tossed together.\n"
        "Calculate the probability of obtaining **at least one Tail**, "
        "giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{3}{4}"
    sol = (
        "Sample space $S = \\{(H, H); (H, T); (T, H); (T, T)\\}$, so $n(S) = 4$.\n"
        "Outcomes with at least one Tail: $\\{(H, T); (T, H); (T, T)\\}$, so $n(E) = 3$.\n"
        "(Or via complement: $1 - P(\\text{no Tails}) = 1 - P(H, H) = 1 - \\frac{1}{4} = \\frac{3}{4}$).\n"
        "$$P(\\text{at least one Tail}) = \\frac{3}{4}$$"
    )
    return {
        "subskill": "21_compound_event_two_coins_at_least_one_tail",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/4",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 3 favourable outcomes: HT, TH, TT", "marks": 1},
            {"step": "P = 3/4", "marks": 1},
        ],
        "hints": [
            "'At least one' means 1 Tail or 2 Tails.",
            "Out of the 4 outcomes, only HH has 0 Tails. So 3 out of 4 have at least one Tail.",
        ],
        "misconception_tags": ["at_least_one_phrasing_misunderstanding"],
    }


# -----------------------------------------------------------------------------
# 22. Sample Space Enumeration: Coin and Die
# -----------------------------------------------------------------------------
def arch_22_sample_space_enumeration_coin_and_die(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A fair coin is tossed and a standard fair six-sided die is rolled.\n"
        "1. How many total possible outcomes exist in the combined sample space $S$?\n"
        "2. List three examples of outcomes from this sample space."
    )
    ans_str = "Total outcomes: 12 (e.g. H1, H2, T6)"
    sol = (
        "1. Fundamental Counting Principle: $2 \\times 6 = 12$ possible outcomes.\n"
        "2. Sample space: $\\{(H, 1); (H, 2); (H, 3); (H, 4); (H, 5); (H, 6); (T, 1); (T, 2); (T, 3); (T, 4); (T, 5); (T, 6)\\}$."
    )
    return {
        "subskill": "22_sample_space_enumeration_coin_and_die",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "12",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 2 * 6 = 12 total outcomes", "marks": 1},
            {"step": "Provide valid example pairs (Coin, Die)", "marks": 1},
        ],
        "hints": [
            "Multiply the number of coin outcomes (2) by the number of die outcomes (6).",
            "2 × 6 = 12.",
        ],
        "misconception_tags": ["sample_space_product_rule_error"],
    }


# -----------------------------------------------------------------------------
# 23. Compound Event: Coin Heads and Die Even
# -----------------------------------------------------------------------------
def arch_23_compound_event_coin_heads_and_die_even(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A coin is tossed and a six-sided die is rolled.\n"
        "Calculate the probability of obtaining **Heads on the coin AND an even number on the die**, "
        "giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{4}"
    sol = (
        "Total outcomes $n(S) = 2 \\times 6 = 12$.\n"
        "Favourable outcomes: $\\{(H, 2); (H, 4); (H, 6)\\}$, so $n(E) = 3$.\n"
        "Alternatively, since events are independent:\n"
        "$$P(H \\text{ and Even}) = P(H) \\times P(\\text{Even}) = \\frac{1}{2} \\times \\frac{3}{6} = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$$"
    )
    return {
        "subskill": "23_compound_event_coin_heads_and_die_even",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/4",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 3 favourable outcomes out of 12 (or multiply 1/2 * 1/2)", "marks": 1},
            {"step": "Simplify to 1/4", "marks": 1},
        ],
        "hints": [
            "P(Heads) = 1/2. P(Even) = 3/6 = 1/2.",
            "Multiply independent probabilities: 1/2 × 1/2.",
        ],
        "misconception_tags": ["independent_compound_probability_multiplication_error"],
    }


# -----------------------------------------------------------------------------
# 24. Sample Space Grid: Sum of Two Dice
# -----------------------------------------------------------------------------
def arch_24_sample_space_grid_sum_of_two_dice(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two standard six-sided dice are rolled simultaneously and their faces are added together.\n"
        "1. How many total outcomes are in the sample space grid for two dice ($6 \\times 6$)?\n"
        "2. What is the minimum possible sum and the maximum possible sum?"
    )
    ans_str = "Total: 36 outcomes; Minimum sum = 2; Maximum sum = 12"
    sol = (
        "1. Total possible outcomes: $6 \\times 6 = 36$.\n"
        "2. Minimum sum: $1 + 1 = 2$.\n"
        "3. Maximum sum: $6 + 6 = 12$."
    )
    return {
        "subskill": "24_sample_space_grid_sum_of_two_dice",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State 36 total outcomes", "marks": 1},
            {"step": "State minimum sum 2 and maximum sum 12", "marks": 1},
        ],
        "hints": [
            "Each die has 6 faces: 6 × 6 = 36 total pairs.",
            "Lowest roll is 1+1 = 2; highest roll is 6+6 = 12.",
        ],
        "misconception_tags": ["two_dice_grid_dimension_confusion"],
    }


# -----------------------------------------------------------------------------
# 25. Compound Event: Sum of Two Dice Equals Seven
# -----------------------------------------------------------------------------
def arch_25_compound_event_sum_of_two_dice_equals_seven(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two standard six-sided dice are rolled simultaneously.\n"
        "Calculate the probability that the **sum of the two dice is exactly 7**, "
        "expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{6}"
    sol = (
        "Total outcomes $n(S) = 36$.\n"
        "Pairs giving a sum of 7:\n"
        "$$\\{(1, 6); (2, 5); (3, 4); (4, 3); (5, 2); (6, 1)\\}$$\n"
        "Number of favourable outcomes: $n(E) = 6$.\n"
        "$$P(\\text{Sum} = 7) = \\frac{6}{36} = \\frac{1}{6}$$"
    )
    return {
        "subskill": "25_compound_event_sum_of_two_dice_equals_seven",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/6",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "List the 6 pairs summing to 7", "marks": 1},
            {"step": "Simplify 6/36 to 1/6", "marks": 1},
        ],
        "hints": [
            "List pairs that add to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).",
            "There are 6 pairs out of 36 total. 6/36 = 1/6.",
        ],
        "misconception_tags": ["two_dice_sum_pairs_omission_error"],
    }
