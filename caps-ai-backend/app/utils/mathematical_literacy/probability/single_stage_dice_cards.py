"""Cluster 2: Single-Stage Theoretical Probability & Equipment (Subskills 10 to 18)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 10: Single Fair Coin Toss
# --------------------------------------------------------------------------- #
def _gen_prob_single_fair_coin_toss(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_fair_coin_toss"
    name = r.choice(SA_NAMES)
    outcome = r.choice(["Heads", "Tails"])
    correct_ans = "1/2 (50%)"

    prompt = (
        f"{name} flips an unbiased South African R5 coin.\n\n"
        f"Calculate the theoretical probability of the coin landing on **{outcome}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A standard coin has 2 mutually exclusive, equally likely outcomes in its sample space: $S = \\{{\\text{{Heads}}, \\text{{Tails}}\\}}$ ($n(S) = 2$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There is exactly 1 favourable outcome ({outcome}).\n"
        f"$$P(\\text{{{outcome}}}) = \\frac{{n(\\text{{{outcome}}})}}{{n(S)}} = \\frac{{1}}{{2}}$$ ✓ [1 Mark: Method – dividing favourable outcome by total outcomes in sample space]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{{outcome}}}) = \\frac{{1}}{{2}} = 0,5 = 50\\%$$ ✓ [1 Mark: Accuracy – accurate probability expression]"
    )

    custom = ["1/2 (50%)", "1/4 (25%)", "1/1 (100%)", "0 (0%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 2 sides on a coin, and 1 side is {outcome}.",
        tier_2="Probability = 1 ÷ 2 = 1/2 = 50%.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 11: Single 6-Sided Die Specific Number
# --------------------------------------------------------------------------- #
def _gen_prob_single_six_sided_die_number(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_six_sided_die_number"
    name = r.choice(SA_NAMES)
    num = r.choice([1, 2, 3, 4, 5, 6])
    correct_ans = "1/6"

    prompt = (
        f"{name} rolls an ordinary, fair six-sided die once.\n\n"
        f"Calculate the theoretical probability of rolling the number **{num}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A standard six-sided die has six equally likely faces: $S = \\{{1; 2; 3; 4; 5; 6\\}}$, so $n(S) = 6$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There is only one face with the number {num}: $n({num}) = 1$.\n"
        f"$$P({num}) = \\frac{{1}}{{6}}$$ ✓ [1 Mark: Method – ratio of single favourable face to 6 total faces]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P({num}) = \\frac{{1}}{{6}}$$ (or $16,7\\%$) ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    d1 = f"{num}/6"
    d2 = "1/2"
    d3 = "5/6"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There is only one {num} on a six-sided die.",
        tier_2="Divide 1 by total outcomes 6.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 12: 6-Sided Die Even or Odd Number
# --------------------------------------------------------------------------- #
def _gen_prob_single_six_sided_die_even_odd(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_six_sided_die_even_odd"
    name = r.choice(SA_NAMES)
    is_even = r.choice([True, False])
    event_type = "even" if is_even else "odd"
    fav_set = "{2; 4; 6}" if is_even else "{1; 3; 5}"
    correct_ans = "1/2 (50%)"

    prompt = (
        f"{name} rolls a standard fair 6-sided die.\n\n"
        f"Calculate the theoretical probability of rolling an **{event_type} number**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The sample space of a 6-sided die is $S = \\{{1; 2; 3; 4; 5; 6\\}}$ ($n(S) = 6$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The {event_type} numbers are {fav_set}, which gives 3 favourable outcomes: $n(\\text{{{event_type}}}) = 3$.\n"
        f"$$P(\\text{{{event_type}}}) = \\frac{{3}}{{6}} = \\frac{{1}}{{2}}$$ ✓ [1 Mark: Method – counting favourable outcomes and simplifying]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{{event_type}}}) = \\frac{{1}}{{2}} = 50\\%$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    custom = ["1/2 (50%)", "1/6 (16,7%)", "2/3 (66,7%)", "1/3 (33,3%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Count how many {event_type} numbers exist on a die.",
        tier_2=f"The {event_type} numbers are {fav_set} (3 numbers out of 6).",
        tier_3=f"Probability = 3/6 = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 13: 6-Sided Die Prime Numbers
# --------------------------------------------------------------------------- #
def _gen_prob_single_six_sided_die_prime_numbers(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_six_sided_die_prime_numbers"
    name = r.choice(SA_NAMES)
    correct_ans = "1/2 (50%)"

    prompt = (
        f"{name} rolls a fair six-sided die.\n\n"
        f"Calculate the theoretical probability of rolling a **prime number**.\n"
        f"(Recall: A prime number has exactly two distinct factors: 1 and itself; 1 is not prime)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The sample space is $S = \\{{1; 2; 3; 4; 5; 6\\}}$ ($n(S) = 6$).\n"
        f"The prime numbers between 1 and 6 are $\\{{2; 3; 5\\}}$ (1 is not prime; 4 and 6 are composite).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There are 3 prime outcomes: $n(\\text{{prime}}) = 3$.\n"
        f"$$P(\\text{{prime}}) = \\frac{{3}}{{6}} = \\frac{{1}}{{2}}$$ ✓ [1 Mark: Method – identifying primes on die and creating probability fraction]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{prime}}) = \\frac{{1}}{{2}} = 50\\%$$ ✓ [1 Mark: Accuracy – accurate probability value]"
    )

    custom = ["1/2 (50%)", "2/3 (66,7%)", "1/3 (33,3%)", "4/6 (66,7%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="List the prime numbers on a die: 2, 3, and 5.",
        tier_2="There are 3 primes out of 6 numbers.",
        tier_3=f"Probability = 3/6 = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 14: 6-Sided Die Greater / Less Than
# --------------------------------------------------------------------------- #
def _gen_prob_single_six_sided_die_greater_less(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_six_sided_die_greater_less"
    name = r.choice(SA_NAMES)
    is_greater = r.choice([True, False])

    if is_greater:
        threshold = 4
        fav = "{5; 6}"
        count = 2
        correct_ans = "1/3 (33,3%)"
        prompt = f"{name} rolls a 6-sided die. Calculate the probability of rolling a number **greater than 4**."
    else:
        threshold = 3
        fav = "{1; 2}"
        count = 2
        correct_ans = "1/3 (33,3%)"
        prompt = f"{name} rolls a 6-sided die. Calculate the probability of rolling a number **strictly less than 3**."

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total possible outcomes = 6 ($S = \\{{1; 2; 3; 4; 5; 6\\}}$).\n"
        f"Favourable outcomes matching the condition = {fav} ($n = {count}$ outcomes).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P = \\frac{{{count}}}{{6}} = \\frac{{1}}{{3}}$$ ✓ [1 Mark: Method – dividing count by 6 and simplifying]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P = \\frac{{1}}{{3}} \\approx 33,3\\%$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    custom = ["1/3 (33,3%)", "1/2 (50%)", "2/3 (66,7%)", "1/6 (16,7%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Count how many numbers match the condition: {fav}.",
        tier_2=f"There are {count} numbers out of 6.",
        tier_3=f"Probability = {count}/6 = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 15: Eight-Sided Die (Octahedral)
# --------------------------------------------------------------------------- #
def _gen_prob_single_eight_sided_die(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_eight_sided_die"
    name = r.choice(SA_NAMES)
    # 8-sided die numbered 1 to 8
    event_type = r.choice([
        ("an odd number", "{1; 3; 5; 7}", 4, "1/2 (50%)"),
        ("a number greater than 5", "{6; 7; 8}", 3, "3/8 (37,5%)"),
        ("a factor of 8", "{1; 2; 4; 8}", 4, "1/2 (50%)"),
        ("the number 8", "{8}", 1, "1/8 (12,5%)"),
    ])
    desc, fav_set, count, correct_str = event_type
    correct_ans = correct_str

    prompt = (
        f"{name} plays a board game using an unbiased 8-sided die (octahedral die) numbered 1 to 8.\n\n"
        f"Calculate the theoretical probability of rolling **{desc}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An 8-sided die has 8 equally likely outcomes: $S = \\{{1; 2; 3; 4; 5; 6; 7; 8\\}}$ ($n(S) = 8$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Favourable outcomes for '{desc}' are {fav_set}, which gives {count} outcomes.\n"
        f"$$P = \\frac{{{count}}}{{8}}$$ ✓ [1 Mark: Method – dividing favourable outcomes by 8]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P = {correct_str}$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    custom = ["1/2 (50%)", "3/8 (37,5%)", "1/8 (12,5%)", "5/8 (62,5%)", "1/4 (25%)"]
    options, _ = _build_options(correct_ans, r, [correct_ans, "1/4 (25%)", "5/8 (62,5%)", "1/8 (12,5%)"])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="An 8-sided die has 8 total outcomes.",
        tier_2=f"Count favourable outcomes in {fav_set}: {count} out of 8.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 16: Standard Deck Suit Probability
# --------------------------------------------------------------------------- #
def _gen_prob_single_standard_deck_suit(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_standard_deck_suit"
    name = r.choice(SA_NAMES)
    suit = r.choice(["Hearts (Red)", "Diamonds (Red)", "Spades (Black)", "Clubs (Black)"])
    correct_ans = "1/4 (25%)"

    prompt = (
        f"{name} draws one card at random from a standard, well-shuffled 52-card playing deck (without Jokers).\n\n"
        f"Calculate the theoretical probability of selecting a card from the suit of **{suit}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A standard deck contains 52 cards divided equally into 4 suits of 13 cards each: Hearts, Diamonds, Spades, and Clubs.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There are 13 cards of {suit} out of 52 total cards.\n"
        f"$$P = \\frac{{13}}{{52}} = \\frac{{1}}{{4}}$$ ✓ [1 Mark: Method – dividing suit cards by 52 and simplifying]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P = \\frac{{1}}{{4}} = 25\\%$$ ✓ [1 Mark: Accuracy – accurate simplified fraction and percentage]"
    )

    custom = ["1/4 (25%)", "1/2 (50%)", "1/13 (7,7%)", "4/52 (7,7%)"]
    options, _ = _build_options(correct_ans, r, custom)

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"52-Card Suit Distribution ({name})",
        "sectors": [
            {"label": "Hearts (13)", "value": 13},
            {"label": "Diamonds (13)", "value": 13},
            {"label": "Spades (13)", "value": 13},
            {"label": "Clubs (13)", "value": 13},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 4 equal suits in a 52-card deck.",
        tier_2="Each suit has 13 cards out of 52: 13/52.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 17: Standard Deck Face Card Probability
# --------------------------------------------------------------------------- #
def _gen_prob_single_standard_deck_face_card(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_standard_deck_face_card"
    name = r.choice(SA_NAMES)
    correct_ans = "3/13 (23,1%)"

    prompt = (
        f"{name} draws a single card from a complete 52-card deck.\n\n"
        f"Calculate the theoretical probability of selecting a **picture card (face card: Jack, Queen, or King)**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In each of the 4 suits, there are 3 picture cards (Jack, Queen, King). "
        f"Therefore, there are $4 \\times 3 = 12$ picture cards in total in the deck.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Picture Card}}) = \\frac{{12}}{{52}} = \\frac{{12 \\div 4}}{{52 \\div 4}} = \\frac{{3}}{{13}}$$ ✓ [1 Mark: Method – dividing 12 face cards by 52 and simplifying by 4]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Picture Card}}) = \\frac{{3}}{{13}} \\approx 23,1\\%$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    custom = ["3/13 (23,1%)", "1/13 (7,7%)", "4/13 (30,8%)", "1/4 (25%)"]
    options, _ = _build_options(correct_ans, r, custom)

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"52-Card Picture Card Distribution ({name})",
        "sectors": [
            {"label": "Hearts (13)", "value": 13},
            {"label": "Diamonds (13)", "value": 13},
            {"label": "Spades (13)", "value": 13},
            {"label": "Clubs (13)", "value": 13},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 3 picture cards per suit × 4 suits = 12 picture cards.",
        tier_2="Divide 12 by 52 and simplify.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 18: Standard Deck Ace Probability
# --------------------------------------------------------------------------- #
def _gen_prob_single_standard_deck_ace(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_single_standard_deck_ace"
    name = r.choice(SA_NAMES)
    rank = r.choice(["Ace", "King", "Queen", "Jack", "Ten", "Seven"])
    correct_ans = "1/13 (7,7%)"

    prompt = (
        f"{name} picks one card at random from a standard 52-card pack.\n\n"
        f"Calculate the theoretical probability of drawing an **{rank}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"There are exactly 4 cards of rank '{rank}' in a standard deck (one in each of the 4 suits).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{{rank}}}) = \\frac{{4}}{{52}} = \\frac{{4 \\div 4}}{{52 \\div 4}} = \\frac{{1}}{{13}}$$ ✓ [1 Mark: Method – dividing 4 cards by 52 and simplifying]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{{rank}}}) = \\frac{{1}}{{13}} \\approx 7,7\\%$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    custom = ["1/13 (7,7%)", "4/13 (30,8%)", "1/4 (25%)", "1/52 (1,9%)"]
    options, _ = _build_options(correct_ans, r, custom)

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"52-Card Ace Distribution ({name})",
        "sectors": [
            {"label": "Hearts (13)", "value": 13},
            {"label": "Diamonds (13)", "value": 13},
            {"label": "Spades (13)", "value": 13},
            {"label": "Clubs (13)", "value": 13},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 4 of each card rank in a standard deck.",
        tier_2="Divide 4 by 52: 4/52 = 1/13.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )
