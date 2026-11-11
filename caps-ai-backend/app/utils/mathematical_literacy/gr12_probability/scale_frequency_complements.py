"""Subskills 01 to 08: Probability scales, relative frequency, theoretical probability, and addition rules."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_frac,
    _fmt_pct,
)


def generate_01_probability_three_forms(r: random.Random) -> Dict[str, Any]:
    """Express a probability in fractional, decimal, and percentage formats."""
    fav = r.choice([3, 4, 6, 8, 12])
    total = r.choice([16, 20, 25, 40, 50])
    dec_val = fav / total
    pct_val = dec_val * 100.0
    frac_str = _fmt_frac(fav, total)

    correct_ans = f"Fraction: {frac_str}; Decimal: {_fmt(dec_val, 2)}; Percentage: {_fmt_pct(pct_val, 1)}"
    custom_options = [
        correct_ans,
        f"Fraction: {total}/{fav}; Decimal: {_fmt(total/fav, 2)}; Percentage: {_fmt_pct((total/fav)*100, 1)}",
        f"Fraction: {frac_str}; Decimal: {_fmt(dec_val * 10, 2)}; Percentage: {_fmt_pct(pct_val / 10, 1)}",
        f"Fraction: 1/{fav}; Decimal: {_fmt(1/fav, 2)}; Percentage: {_fmt_pct((1/fav)*100, 1)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a box containing {total} raffle tickets sold at a high school sports day, {fav} tickets "
        f"belong to Grade 12 learners.\n\n"
        f"If a single ticket is drawn at random, express the probability of winning a prize in three standard forms: "
        f"as a simplified common fraction, as a decimal, and as a percentage."
    )
    explanation = (
        f"Step 1: Simplified fraction = {fav}/{total} = {frac_str} [M].\n"
        f"Step 2: Decimal = {fav} ÷ {total} = {_fmt(dec_val, 2)} [M].\n"
        f"Step 3: Percentage = {_fmt(dec_val, 2)} × 100% = {_fmt_pct(pct_val, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="01_probability_three_forms",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide favorable outcomes by total outcomes, then convert to decimal and percentage.",
        tier_2=f"Fraction is {fav}/{total} = {frac_str}. Divide {fav} by {total}.",
        tier_3=f"Fraction: {frac_str}, Decimal: {_fmt(dec_val, 2)}, Percentage: {_fmt_pct(pct_val, 1)}.",
        r=r,
    )


def generate_02_theoretical_probability_single_draw(r: random.Random) -> Dict[str, Any]:
    """Calculate the theoretical probability of a single random event from a defined sample space."""
    yellow = r.choice([3, 4, 5])
    black = r.choice([4, 6, 7])
    total = yellow + black
    p_frac = _fmt_frac(yellow, total)
    pct = (yellow / total) * 100.0

    correct_ans = f"{p_frac} (or {_fmt(yellow/total, 3)}; {_fmt_pct(pct, 1)})"
    custom_options = [
        correct_ans,
        f"{_fmt_frac(black, total)} (or {_fmt(black/total, 3)}; {_fmt_pct((black/total)*100, 1)})",
        f"{_fmt_frac(yellow, black)} (or {_fmt(yellow/black, 3)})",
        f"1/{total} (or {_fmt(1/total, 3)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A traditional beaded pouch contains {yellow} yellow beads and {black} black beads.\n"
        f"A craft worker draws one bead completely at random without looking.\n\n"
        f"Calculate the theoretical probability that the bead drawn is yellow."
    )
    explanation = (
        f"Step 1: Total possible outcomes in sample space = {yellow} + {black} = {total} beads [M].\n"
        f"Step 2: Number of favorable outcomes (yellow) = {yellow} [M].\n"
        f"Step 3: Probability P(Yellow) = {yellow}/{total} = {p_frac} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="02_theoretical_probability_single_draw",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add up the total number of beads to find the sample space size.",
        tier_2=f"Total beads = {yellow} + {black} = {total}. Favourable = {yellow}.",
        tier_3=f"Probability is {p_frac}.",
        r=r,
    )


def generate_03_relative_frequency_vs_theoretical(r: random.Random) -> Dict[str, Any]:
    """Calculate relative frequency from experimental trials and compare with theoretical probability."""
    trials = r.choice([50, 100, 200])
    heads = r.choice([22, 28, 48, 54, 95])
    rel_freq = heads / trials
    theo_prob = 0.50

    correct_ans = f"Relative frequency = {_fmt(rel_freq, 2)} ({heads}/{trials}); Theoretical probability = 0,50 (1/2)"
    custom_options = [
        correct_ans,
        f"Relative frequency = 0,50; Theoretical probability = {_fmt(rel_freq, 2)}",
        f"Relative frequency = {heads}%; Theoretical probability = {trials}%",
        f"Relative frequency = {_fmt(rel_freq * 1.5, 2)}; Theoretical probability = 1,00",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a classroom experiment, a fair South African R 5 coin was tossed {trials} times.\n"
        f"The coin landed on heads {heads} times and tails {trials - heads} times.\n\n"
        f"Calculate the experimental relative frequency of tossing heads, and state how it compares to the theoretical probability."
    )
    explanation = (
        f"Step 1: Relative frequency = Number of successful trials ÷ Total trials = {heads} ÷ {trials} = {_fmt(rel_freq, 2)} [M].\n"
        f"Step 2: Theoretical probability for a fair coin is strictly 1 ÷ 2 = 0,50 (50%) [M].\n"
        f"Step 3: Conclusion: Relative frequency is {_fmt(rel_freq, 2)}; Theoretical is 0,50 [A]."
    )
    return _build_question_payload(
        subskill_id="03_relative_frequency_vs_theoretical",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Relative frequency is based on actual experiment trials: outcomes divided by total flips.",
        tier_2=f"Calculate {heads} ÷ {trials} = {_fmt(rel_freq, 2)}.",
        tier_3="Theoretical probability for a fair coin is always 0,50.",
        r=r,
    )


def generate_04_law_of_large_numbers(r: random.Random) -> Dict[str, Any]:
    """Explain how relative frequency converges to theoretical probability as trials increase."""
    correct_ans = "Law of Large Numbers: As the number of experimental trials increases, relative frequency converges toward theoretical probability"

    custom_options = [
        correct_ans,
        "Law of Averages: After 10 consecutive tails, a head is physically guaranteed on the next toss",
        "Trial Fatigue: The coin becomes magnetically biased as more tosses occur",
        "Independent Deviation: Increasing trials causes experimental error to multiply infinitely",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A learner tosses a coin 10 times and gets 8 heads (relative frequency = 0,80).\n"
        f"When they repeat the experiment with 10 000 tosses, they get 5 012 heads (relative frequency = 0,5012).\n\n"
        f"State the foundational probability law that explains why the relative frequency moved so close to 0,50."
    )
    explanation = (
        f"Step 1: Small sample sizes exhibit high random variance [M].\n"
        f"Step 2: As trials expand to 10 000, random fluctuations average out [M].\n"
        f"Step 3: This principle is the Law of Large Numbers [A]."
    )
    return _build_question_payload(
        subskill_id="04_law_of_large_numbers",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about what happens when you repeat an experiment thousands of times.",
        tier_2="Random luck evens out as the number of trials becomes very large.",
        tier_3="This is known as the Law of Large Numbers.",
        r=r,
    )


def generate_05_complementary_event_rule(r: random.Random) -> Dict[str, Any]:
    """Calculate the probability of the complement of an event: P(not A) = 1 - P(A)."""
    p_pct = r.choice([65, 72, 80, 85])
    p_dec = p_pct / 100.0
    comp_dec = 1.0 - p_dec
    comp_pct = 100 - p_pct

    correct_ans = f"P(not Rain) = 1 - {_fmt(p_dec, 2)} = {_fmt(comp_dec, 2)} (or {comp_pct}%)"
    custom_options = [
        correct_ans,
        f"P(not Rain) = {_fmt(p_dec, 2)} (or {p_pct}%)",
        f"P(not Rain) = 0,00 (an impossible event)",
        f"P(not Rain) = {_fmt(comp_dec * 2, 2)} (or {comp_pct * 2}%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The South African Weather Service forecasts a {p_pct}% probability of rainfall in Cape Town tomorrow.\n\n"
        f"Using the complementary event rule:\n"
        f"P(not A) = 1 - P(A)\n"
        f"calculate the probability that it will NOT rain tomorrow."
    )
    explanation = (
        f"Step 1: Express P(Rain) as a decimal: {p_pct}% = {_fmt(p_dec, 2)} [M].\n"
        f"Step 2: Apply complement formula: P(not Rain) = 1 - {_fmt(p_dec, 2)} [M].\n"
        f"Step 3: P(not Rain) = {_fmt(comp_dec, 2)} ({comp_pct}%) [A]."
    )
    return _build_question_payload(
        subskill_id="05_complementary_event_rule",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the given probability from 1 (or 100%).",
        tier_2=f"Calculate 100% - {p_pct}%.",
        tier_3=f"The probability of no rain is {_fmt(comp_dec, 2)} ({comp_pct}%).",
        r=r,
    )


def generate_06_mutually_exclusive_addition_rule(r: random.Random) -> Dict[str, Any]:
    """Calculate P(A or B) for mutually exclusive events: P(A or B) = P(A) + P(B)."""
    p_a_pct = r.choice([25, 30, 35])
    p_b_pct = r.choice([15, 20, 25])
    p_union_pct = p_a_pct + p_b_pct
    p_union_dec = p_union_pct / 100.0

    correct_ans = f"P(A or B) = {_fmt(p_a_pct/100, 2)} + {_fmt(p_b_pct/100, 2)} = {_fmt(p_union_dec, 2)} ({p_union_pct}%)"
    custom_options = [
        correct_ans,
        f"P(A or B) = {_fmt(p_a_pct/100, 2)} × {_fmt(p_b_pct/100, 2)} = {_fmt((p_a_pct*p_b_pct)/10000, 4)}",
        f"P(A or B) = {_fmt((p_a_pct - p_b_pct)/100, 2)} ({p_a_pct - p_b_pct}%)",
        f"P(A or B) = 1,00 (100%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commuter transport survey finds that a worker has a {p_a_pct}% probability of travelling by train (Event A) "
        f"and a {p_b_pct}% probability of travelling by bus (Event B). A commuter cannot travel on both at the same time "
        f"(the events are mutually exclusive, so P(A and B) = 0).\n\n"
        f"Calculate the probability that a randomly chosen commuter travels by either train OR bus."
    )
    explanation = (
        f"Step 1: Formula for mutually exclusive events: P(A or B) = P(A) + P(B) [M].\n"
        f"Step 2: Substitute: {p_a_pct}% + {p_b_pct}% = {p_union_pct}% [M].\n"
        f"Step 3: P(A or B) = {_fmt(p_union_dec, 2)} ({p_union_pct}%) [A]."
    )
    return _build_question_payload(
        subskill_id="06_mutually_exclusive_addition_rule",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For mutually exclusive events, simply add the two probabilities together.",
        tier_2=f"Calculate {p_a_pct}% + {p_b_pct}%.",
        tier_3=f"The probability is {_fmt(p_union_dec, 2)} ({p_union_pct}%).",
        r=r,
    )


def generate_07_general_addition_rule(r: random.Random) -> Dict[str, Any]:
    """Calculate P(A or B) for non-mutually exclusive events: P(A) + P(B) - P(A and B)."""
    p_a = 0.60  # e.g. plays soccer
    p_b = 0.40  # e.g. plays cricket
    p_both = 0.15  # plays both
    p_union = p_a + p_b - p_both
    union_pct = round(p_union * 100, 1)

    correct_ans = f"P(A or B) = {_fmt(p_a, 2)} + {_fmt(p_b, 2)} - {_fmt(p_both, 2)} = {_fmt(p_union, 2)} ({_fmt_pct(union_pct)})"
    custom_options = [
        correct_ans,
        f"P(A or B) = {_fmt(p_a, 2)} + {_fmt(p_b, 2)} = {_fmt(p_a + p_b, 2)} (100%)",
        f"P(A or B) = {_fmt(p_a, 2)} × {_fmt(p_b, 2)} = 0,24",
        f"P(A or B) = {_fmt(p_union - 0.1, 2)} (75%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a high school grade:\n"
        f"• The probability that a learner plays soccer (Event A) is {_fmt(p_a, 2)} (60%).\n"
        f"• The probability that a learner plays cricket (Event B) is {_fmt(p_b, 2)} (40%).\n"
        f"• The probability that a learner plays both sports (Event A and B) is {_fmt(p_both, 2)} (15%).\n\n"
        f"Using the general addition rule:\n"
        f"P(A or B) = P(A) + P(B) - P(A and B)\n"
        f"calculate the probability that a learner plays soccer OR cricket."
    )
    explanation = (
        f"Step 1: Formula: P(A or B) = P(A) + P(B) - P(A and B) [M].\n"
        f"Step 2: Substitute: {_fmt(p_a, 2)} + {_fmt(p_b, 2)} - {_fmt(p_both, 2)} = {_fmt(p_union, 2)} [M].\n"
        f"Step 3: P(A or B) = {_fmt(p_union, 2)} ({_fmt_pct(union_pct)}) [A]."
    )
    return _build_question_payload(
        subskill_id="07_general_addition_rule",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the two separate probabilities, then subtract the double-counted intersection.",
        tier_2=f"Calculate {_fmt(p_a, 2)} + {_fmt(p_b, 2)} - {_fmt(p_both, 2)}.",
        tier_3=f"The result is {_fmt(p_union, 2)} ({_fmt_pct(union_pct)}).",
        r=r,
    )


def generate_08_probability_scale_endpoints(r: random.Random) -> Dict[str, Any]:
    """Identify impossible vs certain events on the probability continuum."""
    marker_val = r.choice([0.0, 0.25, 0.5, 0.75, 1.0])
    d_spec_08 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Probability Continuum Scale (Focus Value: {_fmt(marker_val, 2)})",
        "categories": ["Impossible (0)", "Unlikely (0,25)", "Even Chance (0,50)", "Likely (0,75)", "Certain (1)"],
        "values": [0.0, 0.25, 0.5, 0.75, 1.0],
        "series": [
            {"name": "Probability", "values": [0.0, 0.25, 0.5, 0.75, 1.0]}
        ],
    }
    correct_ans = "Probability = 0 means impossible; Probability = 1 (or 100%) means certain; all probabilities must lie between 0 and 1 inclusive"

    custom_options = [
        correct_ans,
        "Probability = -1 means impossible; Probability = 100 means certain",
        "Probabilities can exceed 100% when events occur during peak hours",
        "Probability = 0,5 means impossible; Probability = 1 means highly likely",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the probability continuum scale shown in the diagram (ranging from 0 to 1).\n"
        f"State the meaning of the endpoints (0 and 1) on the probability continuum and specify the allowable numerical range for any probability value."
    )
    explanation = (
        f"Step 1: Probability of 0 means the event has zero chance of occurring (impossible event) [M].\n"
        f"Step 2: Probability of 1 (100%) means the event is guaranteed to occur (certain event) [M].\n"
        f"Step 3: All valid probabilities satisfy 0 ≤ P(E) ≤ 1 [A]."
    )
    return _build_question_payload(
        subskill_id="08_probability_scale_endpoints",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall the boundaries of the probability scale.",
        tier_2="0 means impossible; 1 means certain.",
        tier_3="Valid probabilities always lie between 0 and 1 inclusive.",
        r=r,
        diagram_spec=d_spec_08,
    )



