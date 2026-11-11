"""Subskills 47 to 52: Medical risk, insurance underwriting, weather probabilities, and gambling house edge."""
from __future__ import annotations

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


def generate_47_medical_testing_false_positives(r: random.Random) -> Dict[str, Any]:
    """Calculate the probability that a patient who tests positive actually has the disease (Bayesian insight)."""
    # Population of 10 000 people
    # Prevalence: 1% (100 have condition, 9 900 do not)
    # Test accuracy: 95% true positive rate (95 test +), 5% false positive rate (495 test +)
    # Total positive tests = 95 + 495 = 590
    # Probability truly infected given positive test = 95 / 590 ≈ 16.1%
    total_pop = 10000
    prevalence_pct = 1.0
    true_cases = int(total_pop * (prevalence_pct / 100.0))  # 100
    healthy = total_pop - true_cases  # 9 900

    tp = 95  # 95% of 100
    fp = int(healthy * 0.05)  # 5% of 9 900 = 495
    total_positives = tp + fp  # 590

    prob_true = (tp / total_positives) * 100.0  # 16.1%
    correct_ans = f"n(Positive tests) = {total_positives}; P(Actually infected | Positive test) = {_fmt(prob_true, 1)}%"

    custom_options = [
        correct_ans,
        f"n(Positive tests) = {total_positives}; P(Actually infected | Positive test) = 95,0%",
        f"n(Positive tests) = {true_cases}; P(Actually infected | Positive test) = 1,0%",
        f"n(Positive tests) = {total_pop}; P(Actually infected | Positive test) = 50,0%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A rapid diagnostic screening test for a seasonal viral infection is tested across {total_pop:,} South Africans:\n"
        f"- Disease prevalence in the community is {prevalence_pct}% ({true_cases} people have the disease, and {healthy:,} do not)\n"
        f"- The test correctly identifies 95% of infected individuals (95 True Positives)\n"
        f"- The test produces a 5% False Positive rate in healthy individuals (495 False Positives)\n\n"
        f"Calculate the total number of positive test results, and determine the probability that a person who tests positive **actually has the disease**."
    )
    explanation = (
        f"Step 1: Calculate total positive test results: True Positives + False Positives = {tp} + {fp} = {total_positives} [M].\n"
        f"Step 2: Calculate the conditional probability of having the disease given a positive test: {tp} / {total_positives} [M].\n"
        f"Step 3: {tp} ÷ {total_positives} = {_fmt(prob_true, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="47_medical_testing_false_positives",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total positive tests include both true positives and false positives.",
        tier_2=f"Total positive = {tp} + {fp} = {total_positives}. P(Infected | +) = {tp} ÷ {total_positives}.",
        tier_3=f"P = {_fmt(prob_true, 1)}%.",
        r=r,
    )


def generate_48_insurance_risk_expected_claims(r: random.Random) -> Dict[str, Any]:
    """Calculate the expected number of claims and total claims cost for an insurance pool."""
    n_policies = r.choice([2000, 3000, 4000, 5000])
    claim_rate_pct = r.choice([3.0, 4.0, 5.0])
    avg_claim = r.choice([25000.0, 30000.0, 35000.0])

    expected_claims = int(n_policies * (claim_rate_pct / 100.0))
    total_claims_cost = expected_claims * avg_claim
    premium_per_policy = total_claims_cost / n_policies  # pure risk premium

    correct_ans = f"{expected_claims} claims; Total Cost = {_fmt_curr(total_claims_cost)}; Pure Premium = {_fmt_curr(premium_per_policy)}/month"

    custom_options = [
        correct_ans,
        f"{expected_claims * 2} claims; Total Cost = {_fmt_curr(total_claims_cost * 2)}; Pure Premium = {_fmt_curr(premium_per_policy * 2)}/month",
        f"{int(claim_rate_pct)} claims; Total Cost = {_fmt_curr(avg_claim)}; Pure Premium = {_fmt_curr(avg_claim / n_policies)}/month",
        f"{n_policies} claims; Total Cost = {_fmt_curr(n_policies * avg_claim)}; Pure Premium = {_fmt_curr(avg_claim)}/month",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A vehicle short-term insurer covers {n_policies:,} delivery motorbikes in Gauteng.\n"
        f"- Historical accident claim rate is {_fmt(claim_rate_pct, 1)}% per year\n"
        f"- The average repair claim payout is {_fmt_curr(avg_claim)}\n\n"
        f"Calculate:\n"
        f"1. The expected number of accident claims in one year\n"
        f"2. The total expected claims payout\n"
        f"3. The pure risk premium each motorbike owner must pay per year just to cover expected accident costs"
    )
    explanation = (
        f"Step 1: Expected claims = {n_policies:,} × {_fmt(claim_rate_pct, 1)}% = {expected_claims} claims [M].\n"
        f"Step 2: Total cost = {expected_claims} × {_fmt_curr(avg_claim)} = {_fmt_curr(total_claims_cost)} [M].\n"
        f"Step 3: Pure annual risk premium per bike = {_fmt_curr(total_claims_cost)} ÷ {n_policies:,} = {_fmt_curr(premium_per_policy)}/year [A]."
    )
    return _build_question_payload(
        subskill_id="48_insurance_risk_expected_claims",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply total policies by the claim percentage, then multiply by average claim cost.",
        tier_2=f"Claims = {n_policies} × {claim_rate_pct}%. Total = {expected_claims} × {_fmt_curr(avg_claim)}.",
        tier_3=f"{expected_claims} claims; Total Cost = {_fmt_curr(total_claims_cost)}.",
        r=r,
    )


def generate_49_actuarial_life_expectancy_risk_loading(r: random.Random) -> Dict[str, Any]:
    """Calculate the insurance premium loading based on mortality and lifestyle risk factors."""
    base_premium = 320.0
    smoker_loading_pct = 45.0  # +45% for tobacco smokers
    hazardous_occupation_pct = 25.0  # +25% for mining engineer

    loaded_premium = base_premium * (1 + (smoker_loading_pct + hazardous_occupation_pct) / 100.0)
    increase = loaded_premium - base_premium

    correct_ans = f"Loaded Monthly Premium = {_fmt_curr(loaded_premium)} (an extra {_fmt_curr(increase)} per month)"

    custom_options = [
        correct_ans,
        f"Loaded Monthly Premium = {_fmt_curr(base_premium * 1.45)} (an extra {_fmt_curr(base_premium * 0.45)} per month)",
        f"Loaded Monthly Premium = {_fmt_curr(base_premium * 2.0)} (an extra {_fmt_curr(base_premium)} per month)",
        f"Loaded Monthly Premium = {_fmt_curr(base_premium + smoker_loading_pct + hazardous_occupation_pct)} (an extra R 70,00 per month)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} applies for a R 1 000 000 life assurance policy with a standard non-smoker base monthly premium of {_fmt_curr(base_premium)}.\n\n"
        f"Because {name} is a tobacco smoker and works underground as a mining supervisor, the underwriters apply two cumulative risk loadings:\n"
        f"- Smoker risk loading: +{_fmt(smoker_loading_pct, 0)}%\n"
        f"- Hazardous occupation loading: +{_fmt(hazardous_occupation_pct, 0)}%\n\n"
        f"Calculate {name}'s new loaded monthly premium and state how much extra {name} will pay each month."
    )
    explanation = (
        f"Step 1: Total risk loading percentage = {_fmt(smoker_loading_pct, 0)}% + {_fmt(hazardous_occupation_pct, 0)}% = 70% [M].\n"
        f"Step 2: Extra cost = {_fmt_curr(base_premium)} × 70% = {_fmt_curr(increase)} [M].\n"
        f"Step 3: New loaded monthly premium = {_fmt_curr(base_premium)} + {_fmt_curr(increase)} = {_fmt_curr(loaded_premium)} [A]."
    )
    return _build_question_payload(
        subskill_id="49_actuarial_life_expectancy_risk_loading",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the two percentage loadings together (45% + 25% = 70%), then apply this to the base premium.",
        tier_2=f"Loaded premium = {_fmt_curr(base_premium)} × 1,70.",
        tier_3=f"Loaded Monthly Premium = {_fmt_curr(loaded_premium)}.",
        r=r,
    )


def generate_50_weather_probability_of_precipitation(r: random.Random) -> Dict[str, Any]:
    """Interpret the meteorological meaning of Probability of Precipitation (PoP) in South African forecasts."""
    pop_pct = r.choice([40, 60, 70, 80])
    correct_ans = f"There is a {pop_pct}% probability that measurable rain (≥ 0,2 mm) will fall at any specific location in the forecast area"

    custom_options = [
        correct_ans,
        f"It will rain over exactly {pop_pct}% of the province for the entire 24-hour day",
        f"It will rain for {pop_pct}% of the day (e.g. {pop_pct * 24 // 100} hours of rainfall)",
        f"The rain gauge will fill to {pop_pct}% of maximum rainfall capacity",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The South African Weather Service (SAWS) publishes a forecast for Durban stating: "
        f"'Probability of Precipitation (PoP): {pop_pct}%'.\n\n"
        f"Which of the following statements provides the scientifically and mathematically correct interpretation "
        f"of a {pop_pct}% Probability of Precipitation?"
    )
    explanation = (
        f"Step 1: PoP is defined by meteorologists as PoP = C × A, where C is confidence that rain will occur somewhere, "
        f"and A is the percentage of the area that will receive rain [M].\n"
        f"Step 2: In practical terms, it means there is a {pop_pct}% chance of measurable precipitation at any given point in the forecast region [M].\n"
        f"Step 3: It does NOT mean it will rain for {pop_pct}% of the day or over {pop_pct}% of the total land area [A]."
    )
    return _build_question_payload(
        subskill_id="50_weather_probability_of_precipitation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="PoP represents the probability of measurable rain at any given spot within the forecast area.",
        tier_2="It is a statistical probability of rain occurring at a point, not duration of rain.",
        tier_3=f"There is a {pop_pct}% probability that measurable rain will fall at any specific location.",
        r=r,
    )


def generate_51_sports_betting_implied_probability(r: random.Random) -> Dict[str, Any]:
    """Calculate implied probability from decimal sports betting odds and identify bookmaker margin (overround)."""
    # Odds for Team A, Draw, Team B: 2.20, 3.10, 3.40
    odds_a = 2.20
    odds_draw = 3.10
    odds_b = 3.40

    p_a = (1 / odds_a) * 100.0  # 45.45%
    p_draw = (1 / odds_draw) * 100.0  # 32.26%
    p_b = (1 / odds_b) * 100.0  # 29.41%

    total_implied = p_a + p_draw + p_b  # 107.12%
    bookmaker_margin = total_implied - 100.0  # 7.12%

    correct_ans = f"P(Team A) = {_fmt(p_a, 1)}%; Total Implied = {_fmt(total_implied, 1)}%; Bookmaker Margin = {_fmt(bookmaker_margin, 1)}%"

    custom_options = [
        correct_ans,
        f"P(Team A) = {_fmt(odds_a, 2)}%; Total Implied = 100,0%; Bookmaker Margin = 0,0%",
        f"P(Team A) = 50,0%; Total Implied = 150,0%; Bookmaker Margin = 50,0%",
        f"P(Team A) = {_fmt(p_a, 1)}%; Total Implied = 100,0%; Bookmaker Margin = 0,0%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A licensed South African bookmaker offers the following decimal odds on a PSL soccer fixture between Kaizer Chiefs and Orlando Pirates:\n"
        f"- Kaizer Chiefs win: 2,20\n"
        f"- Draw: 3,10\n"
        f"- Orlando Pirates win: 3,40\n\n"
        f"Calculate the **implied probability** of a Kaizer Chiefs win, the total sum of implied probabilities across all three outcomes, "
        f"and the bookmaker's built-in profit margin (overround)."
    )
    explanation = (
        f"Step 1: Implied probability is calculated as P = 1 / Decimal Odds [M].\n"
        f"P(Chiefs) = 1 ÷ 2,20 = {_fmt(p_a, 1)}% [M].\n"
        f"Step 2: Total implied = (1/2,20 + 1/3,10 + 1/3,40) × 100% = {_fmt(p_a, 1)}% + {_fmt(p_draw, 1)}% + {_fmt(p_b, 1)}% = {_fmt(total_implied, 1)}% [M].\n"
        f"Step 3: The excess over 100% represents the bookmaker's guaranteed profit margin: {_fmt(total_implied, 1)}% - 100% = {_fmt(bookmaker_margin, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="51_sports_betting_implied_probability",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert decimal odds to probability by dividing 1 by the odds (1 ÷ odds).",
        tier_2=f"P(Team A) = 1 ÷ 2,20 = 45,5%. Sum all three implied percentages to find the total.",
        tier_3=f"P(Team A) = {_fmt(p_a, 1)}%; Margin = {_fmt(bookmaker_margin, 1)}%.",
        r=r,
    )


def generate_52_casino_house_edge_roulette(r: random.Random) -> Dict[str, Any]:
    """Critique the mathematical house edge in casino roulette demonstrating long-term certainty of player loss."""
    # European Roulette: 37 pockets (0 to 36). Bet on Red covers 18 pockets. Payout 1:1.
    pockets = 37
    red_pockets = 18
    p_red = red_pockets / pockets  # 18/37 ≈ 48.65%
    p_loss = (pockets - red_pockets) / pockets  # 19/37 ≈ 51.35%

    # Expected value on R 100 bet: (+100 * 18/37) + (-100 * 19/37) = -100/37 = -R 2.70
    house_edge_pct = (1 / pockets) * 100.0  # 2.70%
    ev_r100 = 100.0 * (red_pockets / pockets) - 100.0 * ((pockets - red_pockets) / pockets)

    correct_ans = f"P(Red) = 18/37 (48,6%); House Edge = {_fmt(house_edge_pct, 2)}%; Expected return per R 100 = -{_fmt_curr(abs(ev_r100))}"

    custom_options = [
        correct_ans,
        f"P(Red) = 18/36 (50,0%); House Edge = 0,00%; Expected return per R 100 = R 0,00",
        f"P(Red) = 18/37 (48,6%); House Edge = 5,40%; Expected return per R 100 = -R 5,40",
        f"P(Red) = 19/37 (51,4%); House Edge = -2,70%; Expected return per R 100 = +R 2,70",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a European roulette wheel at a South African casino, there are 37 numbered pockets: "
        f"numbers 1 to 36 (18 red and 18 black) plus a green '0'. A player bets R 100 on Red, which pays even money (1 : 1).\n\n"
        f"Calculate the true probability of winning on Red, the casino's mathematical house edge percentage, "
        f"and the player's expected monetary outcome on a R 100 bet."
    )
    explanation = (
        f"Step 1: Probability of landing on red = 18 / 37 = {_fmt(p_red * 100.0, 1)}% (less than 50%) [M].\n"
        f"Step 2: The single green zero gives the casino its advantage: (1 / 37) × 100% = {_fmt(house_edge_pct, 2)}% [M].\n"
        f"Step 3: On every R 100 bet, the expected return is (18/37 × R 100) - (19/37 × R 100) = -{_fmt_curr(abs(ev_r100))} [A]."
    )
    return _build_question_payload(
        subskill_id="52_casino_house_edge_roulette",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 37 pockets total (not 36). The green 0 ensures the player wins less than 50% of the time.",
        tier_2=f"P(Red) = 18 ÷ 37 = 48,6%. Expected loss per R 100 = R 100 ÷ 37 = R 2,70.",
        tier_3=f"House Edge = {_fmt(house_edge_pct, 2)}%; Expected return per R 100 = -{_fmt_curr(abs(ev_r100))}.",
        r=r,
    )
