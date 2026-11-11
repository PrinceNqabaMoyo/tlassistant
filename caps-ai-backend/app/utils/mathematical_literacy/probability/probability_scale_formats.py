"""Cluster 1: The Probability Scale & Number Formats (Subskills 1 to 9)."""
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
# Subskill 1: Verbal Classification on Probability Scale
# --------------------------------------------------------------------------- #
def _gen_prob_scale_verbal_classification(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_verbal_classification"
    name = r.choice(SA_NAMES)
    choices = [
        ("The sun will rise in the East tomorrow morning", "Certain", "1,0 (100%)", "it is guaranteed by natural laws to occur"),
        ("Rolling a 7 on a standard 6-sided die", "Impossible", "0 (0%)", "a standard die only has numbers 1 to 6"),
        ("Tossing a fair coin and landing on Heads", "Even chance", "0,5 (50%)", "Heads and Tails are equally likely outcomes"),
        ("Selecting a winning ticket where 9 out of 10 tickets win a prize", "Likely", "0,9 (90%)", "the probability is much closer to 1 than 0,5"),
        ("Winning the first division National Lottery jackpot with one ticket", "Very unlikely", "almost 0 (0,000007%)", "the odds are 1 in 14 million"),
    ]
    event, verbal_word, num_rep, reasoning = r.choice(choices)
    correct_ans = verbal_word

    prompt = (
        f"{name} is classifying everyday events on the probability scale:\n\n"
        f"Event: \"**{event}**\"\n\n"
        f"Which word from the probability scale best describes the likelihood of this event?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The probability scale ranges from 0 (Impossible) to 1 (Certain), with 0,5 representing an Even chance.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"For this event, {reasoning}. "
        f"The corresponding numerical probability is {num_rep}. ✓ [1 Mark: Method – matching real-world likelihood to probability scale benchmark]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct verbal term]"
    )

    custom = ["Impossible", "Unlikely", "Even chance", "Likely", "Certain", "Very unlikely"]
    options, _ = _build_options(correct_ans, r, [correct_ans, "Impossible", "Even chance", "Certain"])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Verbal Classification (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about where this event sits on a scale from 0 (never) to 1 (guaranteed).",
        tier_2=f"{event} has a probability of {num_rep}.",
        tier_3=f"The correct term is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 2: Fraction to Decimal and Percentage
# --------------------------------------------------------------------------- #
def _gen_prob_scale_fraction_to_decimal_percentage(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_fraction_to_decimal_percentage"
    name = r.choice(SA_NAMES)
    fracs = [
        (1, 4, 0.25, 25),
        (1, 2, 0.50, 50),
        (3, 4, 0.75, 75),
        (1, 5, 0.20, 20),
        (2, 5, 0.40, 40),
        (3, 5, 0.60, 60),
        (4, 5, 0.80, 80),
        (1, 10, 0.10, 10),
        (3, 10, 0.30, 30),
        (7, 10, 0.70, 70),
    ]
    num, den, dec, pct = r.choice(fracs)
    correct_ans = f"{_fmt(dec)}; {pct}%"

    prompt = (
        f"{name} calculates that the theoretical probability of winning a prize in a competition is **$\\frac{{{num}}}{{{den}}}$**.\n\n"
        f"Express this probability as both a **decimal fraction** and a **percentage**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert a common fraction to a decimal, divide numerator by denominator: $\\frac{{n}}{{d}} = n \\div d$.\n"
        f"To convert to a percentage, multiply the decimal fraction by 100%.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Decimal}} = {num} \\div {den} = {_fmt(dec)}$$\n"
        f"$$\\text{{Percentage}} = {_fmt(dec)} \\times 100\\% = {pct}\\%$$ ✓ [1 Mark: Method – dividing numerator by denominator and multiplying by 100]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate decimal and percentage]"
    )

    d1 = f"{_fmt(dec * 10)}; {pct // 10}%"
    d2 = f"{_fmt(1 - dec)}; {100 - pct}%"
    d3 = f"{_fmt(round(dec / 2, 2))}; {pct // 2}%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Fraction To Decimal Percentage (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide numerator by denominator to find decimal.",
        tier_2=f"{num} ÷ {den} = {_fmt(dec)}. Multiply by 100 to get percentage.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 3: Percentage to Simplified Fraction
# --------------------------------------------------------------------------- #
def _gen_prob_scale_percentage_to_fraction(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_percentage_to_fraction"
    name = r.choice(SA_NAMES)
    choices = [
        (25, "1/4", 25),
        (50, "1/2", 50),
        (75, "3/4", 25),
        (20, "1/5", 20),
        (40, "2/5", 20),
        (60, "3/5", 20),
        (80, "4/5", 20),
        (10, "1/10", 10),
    ]
    pct, simp_frac, gcd_val = r.choice(choices)
    correct_ans = simp_frac

    prompt = (
        f"{name} reads a weather report indicating a **{pct}% chance of thunderstorms**.\n\n"
        f"Express this probability as a **simplified common fraction** in simplest form."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A percentage means 'per hundred'. Write {pct}% as the fraction $\\frac{{{pct}}}{{100}}$, "
        f"then simplify by dividing the numerator and denominator by their greatest common divisor ({gcd_val}).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\frac{{{pct}}}{{100}} = \\frac{{{pct} \\div {gcd_val}}}{{100 \\div {gcd_val}}}$$ ✓ [1 Mark: Method – writing over 100 and dividing by common factor]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P = {simp_frac}$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    d1 = f"{pct}/100"  # unsimplified
    d2 = f"{100 - pct}/100"
    d3 = f"1/{pct}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Percentage To Fraction (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Write as a fraction over 100: {pct}/100.",
        tier_2=f"Divide top and bottom by {gcd_val}.",
        tier_3=f"Simplified fraction = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 4: Decimal to Percentage
# --------------------------------------------------------------------------- #
def _gen_prob_scale_decimal_to_percentage(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_decimal_to_percentage"
    name = r.choice(SA_NAMES)
    dec = r.choice([0.15, 0.35, 0.45, 0.65, 0.85, 0.05, 0.95])
    pct = round(dec * 100, 1)
    correct_ans = f"{_fmt(pct)}%"

    prompt = (
        f"{name} determines that the decimal probability of rain in Cape Town is **{_fmt(dec)}**.\n\n"
        f"Convert this probability to a percentage."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert a decimal probability to a percentage, multiply by 100% (shift the decimal comma 2 places to the right).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Percentage}} = {_fmt(dec)} \\times 100\\%$$ ✓ [1 Mark: Method – multiplying decimal by 100%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Percentage}} = {_fmt(pct)}\\%$$ ✓ [1 Mark: Accuracy – accurate percentage]"
    )

    d1 = f"{_fmt(dec * 10)}%"
    d2 = f"{_fmt(dec)}%"
    d3 = f"{_fmt(100 - pct)}%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Decimal To Percentage (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the decimal by 100.",
        tier_2=f"{_fmt(dec)} × 100 = {_fmt(pct)}%.",
        tier_3=f"The percentage is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 5: Probability Bounds & Validity
# --------------------------------------------------------------------------- #
def _gen_prob_scale_bounds_validity(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_bounds_validity"
    name = r.choice(SA_NAMES)
    invalid_val = r.choice(["-0,25", "1,35", "150%", "-10%", "5/3"])
    correct_ans = f"No, because probability must strictly lie between 0 and 1 (0% and 100%)"

    prompt = (
        f"A learner calculates a probability value of **{invalid_val}** for an experiment.\n\n"
        f"Is this a valid mathematical probability? Explain your reasoning."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"By definition, the probability of any event must lie between 0 (impossible) and 1 (certain), inclusive: $0 \\le P(E) \\le 1$ ($0\\% \\le P(E) \\le 100\\%$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The value {invalid_val} falls outside this boundary (either negative or greater than 1). "
        f"It is physically impossible to have fewer than 0 favourable outcomes, or more favourable outcomes than total possible outcomes. "
        f"✓ [1 Mark: Method – applying probability boundary axioms]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct evaluation]"
    )

    custom = [
        correct_ans,
        "Yes, because probability can be any positive or negative number",
        "Yes, but only if the experiment has multiple outcomes",
        "No, because probabilities can only be whole integer numbers",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Bounds Validity (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Probability can never be less than 0 or greater than 1.",
        tier_2=f"{invalid_val} is outside the range 0 to 1.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 6: Complementary Event Rule
# --------------------------------------------------------------------------- #
def _gen_prob_scale_complementary_event_rule(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_complementary_event_rule"
    name = r.choice(SA_NAMES)
    p_event = r.choice([0.15, 0.25, 0.30, 0.45, 0.60, 0.75])
    p_not = round(1.0 - p_event, 2)
    correct_ans = f"{_fmt(p_not)}"

    prompt = (
        f"{name} knows that the probability of a soccer team winning a match is **$P(\\text{{Win}}) = {_fmt(p_event)}$**.\n"
        f"(Assume in this competition the match cannot end in a draw).\n\n"
        f"Calculate the probability of the team **NOT winning** the match: **$P(\\text{{Not Win}})$**.\n\n"
        f"**Formula**: $P(\\text{{Not }} E) = 1 - P(E)$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An event and its complement encompass all possible outcomes. Their probabilities must sum to 1: $P(E) + P(\\text{{not }} E) = 1$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Not Win}}) = 1 - P(\\text{{Win}}) = 1 - {_fmt(p_event)}$$ ✓ [1 Mark: Method – subtracting probability from 1]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Not Win}}) = {_fmt(p_not)}$$ ✓ [1 Mark: Accuracy – accurate decimal subtraction]"
    )

    d1 = f"{_fmt(p_event)}"
    d2 = f"{_fmt(round(p_not / 2, 2))}"
    d3 = f"{_fmt(round(p_not + 0.1, 2))}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Complementary Event Rule (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the probability from 1: P(not E) = 1 - P(E).",
        tier_2=f"Calculate 1 - {_fmt(p_event)}.",
        tier_3=f"P(not Win) = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 7: Weather Forecast Complementary Percentage
# --------------------------------------------------------------------------- #
def _gen_prob_scale_rain_forecast_complement(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_rain_forecast_complement"
    name = r.choice(SA_NAMES)
    town = r.choice(["Durban", "Johannesburg", "Pretoria", "Gqeberha", "Polokwane"])
    rain_pct = r.choice([30, 40, 60, 70, 80])
    no_rain_pct = 100 - rain_pct
    correct_ans = f"{no_rain_pct}%"

    prompt = (
        f"{name} is checking the weather forecast for {town}.\n"
        f"The South African Weather Service predicts a **{rain_pct}% probability of precipitation (rain)** for tomorrow.\n\n"
        f"Calculate the probability that it will **NOT rain** in {town} tomorrow."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"It will either rain or not rain. The total probability of all outcomes in percentage format is 100%.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Probability of no rain}} = 100\\% - \\text{{Probability of rain}}$$\n"
        f"$$\\text{{Probability of no rain}} = 100\\% - {rain_pct}\\%$$ ✓ [1 Mark: Method – subtracting forecast percentage from 100%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Probability of no rain}} = {no_rain_pct}\\%$$ ✓ [1 Mark: Accuracy – accurate percentage subtraction]"
    )

    d1 = f"{rain_pct}%"
    d2 = f"{no_rain_pct - 10}%"
    d3 = f"{no_rain_pct + 10}%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Rain Forecast Complement (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the rain chance from 100%.",
        tier_2=f"100% - {rain_pct}% = {no_rain_pct}%.",
        tier_3=f"The probability of no rain is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 8: Sum of All Outcomes Equals One
# --------------------------------------------------------------------------- #
def _gen_prob_scale_sum_of_all_outcomes_equals_one(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_sum_of_all_outcomes_equals_one"
    name = r.choice(SA_NAMES)
    p_red = r.choice([0.20, 0.25, 0.30])
    p_blue = r.choice([0.35, 0.40, 0.45])
    p_green = round(1.0 - p_red - p_blue, 2)
    correct_ans = f"{_fmt(p_green)}"

    prompt = (
        f"A prize spinner has only three possible outcomes: Red, Blue, or Green.\n"
        f"  • $P(\\text{{Red}}) = {_fmt(p_red)}$\n"
        f"  • $P(\\text{{Blue}}) = {_fmt(p_blue)}$\n\n"
        f"Calculate the missing probability of the spinner landing on Green: **$P(\\text{{Green}})$**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The sum of all mutually exclusive and exhaustive outcomes in an experiment must equal exactly 1:\n"
        f"$$P(\\text{{Red}}) + P(\\text{{Blue}}) + P(\\text{{Green}}) = 1$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Green}}) = 1 - (P(\\text{{Red}}) + P(\\text{{Blue}}))$$\n"
        f"$$P(\\text{{Green}}) = 1 - ({_fmt(p_red)} + {_fmt(p_blue)}) = 1 - {_fmt(p_red + p_blue)}$$ ✓ [1 Mark: Method – subtracting sum of known probabilities from 1]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Green}}) = {_fmt(p_green)}$$ ✓ [1 Mark: Accuracy – accurate decimal difference]"
    )

    d1 = f"{_fmt(p_red + p_blue)}"
    d2 = f"{_fmt(round(p_green / 2, 2))}"
    d3 = f"{_fmt(round(p_green + 0.1, 2))}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Sum Of All Outcomes Equals One (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="All probabilities in the sample space must add up to 1.",
        tier_2=f"Add {_fmt(p_red)} + {_fmt(p_blue)} = {_fmt(p_red + p_blue)}. Subtract from 1.",
        tier_3=f"P(Green) = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 9: Ordering Events by Likelihood
# --------------------------------------------------------------------------- #
def _gen_prob_scale_ordering_events_likelihood(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_scale_ordering_events_likelihood"
    name = r.choice(SA_NAMES)
    correct_ans = "A, C, B"

    prompt = (
        f"{name} is ranking three events by their probability:\n"
        f"  • Event A: $P(A) = 0,15$ (15%)\n"
        f"  • Event B: $P(B) = 0,80$ (80%)\n"
        f"  • Event C: $P(C) = 0,50$ (50%)\n\n"
        f"Arrange the events in order from **least likely to most likely**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To order events by likelihood, compare their numerical values from smallest to largest.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$0,15 < 0,50 < 0,80$$\n"
        f"Event A ($0,15$) is smallest, Event C ($0,50$) is intermediate, and Event B ($0,80$) is largest. "
        f"✓ [1 Mark: Method – comparing numerical values from smallest to largest]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct sequence]"
    )

    custom = ["A, C, B", "B, C, A", "C, A, B", "A, B, C"]
    options, _ = _build_options(correct_ans, r, custom)

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Probability Continuum [0 to 1]",
        "segment_value_km": 0.25,
        "total_km": 1.0,
        "title": f"Probability Scale: Prob Scale Ordering Events Likelihood (Seed {r.randint(10, 99)})",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Least likely has the smallest probability number.",
        tier_2="0,15 < 0,50 < 0,80.",
        tier_3=f"Order from least to most likely: {correct_ans}.",
        r=r,
    )
