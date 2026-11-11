"""Subskills 41 to 46: Fundamental counting principle, permutations, lottery combinations, and expected value."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_frac,
    _fmt_pct,
)


def generate_41_fundamental_counting_principle(r: random.Random) -> Dict[str, Any]:
    """Calculate the total number of distinct outcomes using the Fundamental Counting Principle (m × n × p)."""
    tops = r.choice([3, 4, 5])
    bottoms = r.choice([3, 4])
    shoes = r.choice([2, 3])
    jackets = 2

    total_outfits = tops * bottoms * shoes * jackets
    correct_ans = f"{total_outfits} distinct combinations"

    custom_options = [
        correct_ans,
        f"{tops + bottoms + shoes + jackets} distinct combinations",
        f"{tops * bottoms * shoes} distinct combinations",
        f"{total_outfits * 2} distinct combinations",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is planning a wardrobe for a matric valedictory week. {name} has:\n"
        f"- {tops} different shirts/blouses\n"
        f"- {bottoms} different pairs of trousers/skirts\n"
        f"- {shoes} pairs of shoes\n"
        f"- {jackets} different blazers/jackets\n\n"
        f"Using the **Fundamental Counting Principle**, calculate how many unique outfits {name} can create "
        f"consisting of one top, one bottom, one pair of shoes, and one jacket."
    )
    explanation = (
        f"Step 1: The Fundamental Counting Principle states that if event 1 has n₁ outcomes, event 2 has n₂ outcomes, etc., "
        f"the total number of composite outcomes is the product: N = n₁ × n₂ × n₃ × n₄ [M].\n"
        f"Step 2: Total combinations = {tops} × {bottoms} × {shoes} × {jackets} [M].\n"
        f"Step 3: Total = {total_outfits} distinct combinations [A]."
    )
    return _build_question_payload(
        subskill_id="41_fundamental_counting_principle",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the number of choices available at each stage.",
        tier_2=f"Calculate: {tops} × {bottoms} × {shoes} × {jackets}.",
        tier_3=f"{total_outfits} distinct combinations.",
        r=r,
    )


def generate_42_pin_codes_with_repetition(r: random.Random) -> Dict[str, Any]:
    """Calculate the number of possible 4-digit mobile banking PINs with repetition allowed and probability of guessing."""
    num_digits = 4
    total_pins = 10 ** num_digits  # 10 000
    p_guess = 1 / total_pins
    frac_str = f"1/{_fmt(total_pins, 0)}"
    pct = p_guess * 100.0

    correct_ans = f"{_fmt(total_pins, 0)} possible PINs; Probability = {frac_str} ({_fmt(pct, 4)}%)"

    custom_options = [
        correct_ans,
        f"5 040 possible PINs; Probability = 1/5 040 (0,0198%)",
        f"40 possible PINs; Probability = 1/40 (2,5000%)",
        f"9 999 possible PINs; Probability = 1/9 999 (0,0100%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A South African commercial bank requires each customer to create a {num_digits}-digit ATM banking PIN. "
        f"Each digit can be any number from 0 to 9, and repetition of digits is allowed (e.g. 5522 is valid).\n\n"
        f"1. How many different {num_digits}-digit PINs are possible?\n"
        f"2. What is the probability that a thief correctly guesses the PIN on the very first attempt?"
    )
    explanation = (
        f"Step 1: Each of the 4 digit positions has 10 possible choices (0 to 9): 10 × 10 × 10 × 10 = 10⁴ = 10 000 PINs [M].\n"
        f"Step 2: Only 1 PIN is correct out of 10 000 possibilities [M].\n"
        f"Step 3: Probability = 1 / 10 000 = 0,0001 (0,01%) [A]."
    )
    return _build_question_payload(
        subskill_id="42_pin_codes_with_repetition",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 10 choices for each of the 4 positions because repetition is allowed.",
        tier_2=f"Total = 10 × 10 × 10 × 10 = 10 000. Probability of first attempt = 1 ÷ 10 000.",
        tier_3=f"10 000 possible PINs; Probability = 1/10 000 (0,01%).",
        r=r,
    )


def generate_43_arrangements_without_repetition(r: random.Random) -> Dict[str, Any]:
    """Calculate permutations without repetition (arranging committee roles or books in a row)."""
    n_candidates = r.choice([7, 8, 9, 10])
    # Selecting Chairperson, Vice-Chairperson, and Treasurer (3 distinct positions)
    perms = n_candidates * (n_candidates - 1) * (n_candidates - 2)

    correct_ans = f"{_fmt(perms, 0)} possible executive committees"

    distractor_1 = n_candidates * 3
    distractor_2 = math.comb(n_candidates, 3)
    distractor_3 = perms * 2
    custom_options = [
        correct_ans,
        f"{_fmt(distractor_2, 0)} possible executive committees",
        f"{_fmt(distractor_1, 0)} possible executive committees",
        f"{_fmt(distractor_3, 0)} possible executive committees",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A school Representative Council of Learners (RCL) has {n_candidates} elected prefects. "
        f"The committee must elect a **Chairperson**, a **Vice-Chairperson**, and a **Treasurer** from among these {n_candidates} prefects. "
        f"No single person may hold more than one position.\n\n"
        f"How many different executive committee arrangements are possible?"
    )
    explanation = (
        f"Step 1: Position 1 (Chairperson) has {n_candidates} possible choices [M].\n"
        f"Step 2: Position 2 (Vice-Chairperson) has {n_candidates - 1} remaining choices, and Position 3 (Treasurer) has {n_candidates - 2} choices [M].\n"
        f"Step 3: Total permutations = {n_candidates} × {n_candidates - 1} × {n_candidates - 2} = {_fmt(perms, 0)} [A]."
    )
    return _build_question_payload(
        subskill_id="43_arrangements_without_repetition",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Since the roles are distinct and nobody can hold two roles, multiply: n × (n - 1) × (n - 2).",
        tier_2=f"Calculate: {n_candidates} × {n_candidates - 1} × {n_candidates - 2}.",
        tier_3=f"{_fmt(perms, 0)} possible executive committees.",
        r=r,
    )


def generate_44_sa_national_lottery_odds(r: random.Random) -> Dict[str, Any]:
    """Calculate the total number of combinations and probability of winning the South African LOTTO jackpot."""
    total_balls = 52
    drawn_balls = 6
    total_combos = math.comb(total_balls, drawn_balls)  # 20 358 520
    p_jackpot = 1 / total_combos

    frac_str = f"1/{_fmt(total_combos, 0)}"
    correct_ans = f"{_fmt(total_combos, 0)} combinations; Probability = {frac_str}"

    custom_options = [
        correct_ans,
        f"312 combinations; Probability = 1/312",
        f"14 658 134 combinations; Probability = 1/14 658 134",
        f"132 300 000 combinations; Probability = 1/132 300 000",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In the South African National LOTTO game, a player chooses 6 different numbers from the integers 1 to {total_balls}.\n\n"
        f"1. How many different combinations of 6 numbers can be drawn from {total_balls} balls (where draw order does not matter)?\n"
        f"2. What is the probability that a single R 5 ticket matches all 6 winning numbers to claim the jackpot?"
    )
    explanation = (
        f"Step 1: Calculate combinations using nCr: 52! / (6! × (52 - 6)!) [M].\n"
        f"Step 2: 52 × 51 × 50 × 49 × 48 × 47 ÷ (6 × 5 × 4 × 3 × 2 × 1) = {_fmt(total_combos, 0)} combinations [M].\n"
        f"Step 3: Since each ticket holds one unique combination, P(Jackpot) = 1 / {_fmt(total_combos, 0)} [A]."
    )
    return _build_question_payload(
        subskill_id="44_sa_national_lottery_odds",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Order does not matter in Lotto, so use combinations (nCr) with n = 52 and r = 6.",
        tier_2=f"Combinations = 52 C 6 = 20 358 520. Probability = 1 ÷ 20 358 520.",
        tier_3=f"20 358 520 combinations; Probability = 1/20 358 520.",
        r=r,
    )


def generate_45_raffle_draw_probabilities(r: random.Random) -> Dict[str, Any]:
    """Calculate the probability of winning a prize in a school fundraising raffle given multiple tickets purchased."""
    total_tickets = r.choice([500, 800, 1000, 1200, 1500])
    tickets_bought = r.choice([5, 10, 15, 20])
    p_win = tickets_bought / total_tickets
    frac_str = _fmt_frac(tickets_bought, total_tickets)
    pct = round(p_win * 100.0, 2)

    correct_ans = f"P(Win) = {tickets_bought}/{total_tickets} = {frac_str} ({_fmt(pct, 2)}%)"

    custom_options = [
        correct_ans,
        f"P(Win) = 1/{total_tickets} ({_fmt(round(1/total_tickets*100, 2), 2)}%)",
        f"P(Win) = {tickets_bought}/100 ({tickets_bought}%)",
        f"P(Win) = {frac_str} (100%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"A high school prints and sells exactly {total_tickets} numbered raffle tickets at R 20 each to raise funds for the computer lab.\n"
        f"{name} buys {tickets_bought} tickets in the draw for the first prize (a laptop computer).\n\n"
        f"Calculate the probability that {name} wins the first prize, expressed as a simplified fraction and as a percentage."
    )
    explanation = (
        f"Step 1: Identify favorable outcomes: n(E) = {tickets_bought} tickets [M].\n"
        f"Step 2: Identify total possible outcomes: n(S) = {total_tickets} tickets [M].\n"
        f"Step 3: P(Win) = {tickets_bought} / {total_tickets} = {frac_str} or {_fmt(pct, 2)}% [A]."
    )
    return _build_question_payload(
        subskill_id="45_raffle_draw_probabilities",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the number of tickets bought by the total number of tickets sold.",
        tier_2=f"P = {tickets_bought} ÷ {total_tickets}.",
        tier_3=f"P(Win) = {frac_str} ({_fmt(pct, 2)}%).",
        r=r,
    )


def generate_46_expected_value_commercial_competitions(r: random.Random) -> Dict[str, Any]:
    """Calculate the expected monetary value E(X) of a lottery ticket to demonstrate negative expectation."""
    ticket_price = 10.0  # R 10 ticket
    total_tickets = 10000
    first_prize = 50000.0  # 1 prize of R 50 000
    second_prize = 5000.0  # 4 prizes of R 5 000 each (R 20 000)
    num_second = 4

    expected_payout = (1 / total_tickets * first_prize) + (num_second / total_tickets * second_prize)
    expected_net = expected_payout - ticket_price  # e.g. (5.00 + 2.00) - 10.00 = -3.00

    correct_ans = f"Expected Value = {_fmt_curr(expected_net)} per ticket (an expected loss of {_fmt_curr(abs(expected_net))})"

    custom_options = [
        correct_ans,
        f"Expected Value = {_fmt_curr(expected_payout)} per ticket (a guaranteed profit)",
        f"Expected Value = R 0,00 per ticket (fair game)",
        f"Expected Value = {_fmt_curr(first_prize / total_tickets)} per ticket",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial charity competition sells 10 000 tickets at R 10,00 each.\n"
        f"The prize structure is as follows:\n"
        f"- 1st Prize: R 50 000,00 (1 winner)\n"
        f"- 2nd Prize: R 5 000,00 (4 winners)\n\n"
        f"Calculate the **Expected Value (E)** per ticket after deducting the R 10,00 purchase cost, "
        f"and interpret whether this is financially favorable to the player."
    )
    explanation = (
        f"Step 1: Calculate expected gross winnings:\n"
        f"E(Gross) = (1/10 000 × R 50 000) + (4/10 000 × R 5 000) = R 5,00 + R 2,00 = R 7,00 [M].\n"
        f"Step 2: Deduct ticket purchase price: R 7,00 - R 10,00 = -R 3,00 [M].\n"
        f"Step 3: The expected net value is {_fmt_curr(expected_net)} per ticket, meaning on average a player loses {_fmt_curr(abs(expected_net))} for every ticket purchased [A]."
    )
    return _build_question_payload(
        subskill_id="46_expected_value_commercial_competitions",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Expected value = (probability × prize) summed for all prizes, minus ticket price.",
        tier_2=f"Expected gross = (1/10 000 × 50 000) + (4/10 000 × 5 000) = R 7,00. Subtract R 10 ticket cost.",
        tier_3=f"Expected Value = {_fmt_curr(expected_net)} per ticket.",
        r=r,
    )
