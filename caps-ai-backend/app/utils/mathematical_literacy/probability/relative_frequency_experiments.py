"""Cluster 4: Relative Frequency & Experimental Probability (Subskills 28 to 36)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 28: Relative Frequency Calculation
# --------------------------------------------------------------------------- #
def _gen_prob_exp_relative_frequency_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_relative_frequency_calculation"
    name = r.choice(SA_NAMES)
    trials = r.choice([50, 100, 200])
    occurred = r.choice([22, 28, 48, 56, 92])
    rel_freq = round(occurred / trials, 2)
    pct = round(rel_freq * 100, 1)
    correct_ans = f"{_fmt(rel_freq)} ({_fmt(pct)}%)"

    prompt = (
        f"{name} conducts a dice rolling experiment with **{trials} trials**.\n"
        f"A six was rolled **{occurred} times**.\n\n"
        f"Calculate the **experimental relative frequency** of rolling a six."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Relative frequency is the ratio of observed occurrences to the total number of experimental trials conducted: "
        f"$\\text{{Relative Frequency}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total Trials}}}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Relative Frequency}} = \\frac{{{occurred}}}{{{trials}}} = {_fmt(rel_freq)}$$\n"
        f"$$\\text{{Percentage}} = {_fmt(rel_freq)} \\times 100\\% = {_fmt(pct)}\\%$$ ✓ [1 Mark: Method – dividing frequency by total trials]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate relative frequency decimal and percentage]"
    )

    d1 = f"{_fmt(round(occurred / (trials + 10), 2))} ({_fmt(round(occurred / (trials + 10) * 100, 1))}%)"
    d2 = f"{_fmt(round((trials - occurred) / trials, 2))} ({_fmt(round((trials - occurred) / trials * 100, 1))}%)"
    d3 = f"0,17 (16,7%)"  # theoretical probability instead of relative frequency
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Relative frequency = Frequency ÷ Total trials.",
        tier_2=f"Calculate {occurred} ÷ {trials}.",
        tier_3=f"Relative frequency = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 29: Compare Relative to Theoretical Probability
# --------------------------------------------------------------------------- #
def _gen_prob_exp_compare_relative_to_theoretical(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_compare_relative_to_theoretical"
    name = r.choice(SA_NAMES)
    trials = 100
    heads = r.choice([54, 56, 58, 44, 46])
    correct_ans = f"Relative frequency = {heads}% vs Theoretical probability = 50%"

    prompt = (
        f"{name} flips a fair coin {trials} times and obtains Heads {heads} times.\n\n"
        f"Compare the **experimental relative frequency** of Heads with the **theoretical probability** of Heads."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Theoretical probability is based on mathematical deduction: $P(\\text{{Heads}}) = \\frac{{1}}{{2}} = 50\\%$.\n"
        f"Experimental relative frequency is based on actual trial data: $\\frac{{{heads}}}{{{trials}}} = {heads}\\%$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Experimental Relative Frequency}} = \\frac{{{heads}}}{{{trials}}} = {heads}\\%$$\n"
        f"$$\\text{{Theoretical Probability}} = \\frac{{1}}{{2}} = 50\\%$$ ✓ [1 Mark: Method – calculating both metrics correctly]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct comparison stated]"
    )

    custom = [
        correct_ans,
        f"Relative frequency = 50% vs Theoretical probability = {heads}%",
        f"Both relative frequency and theoretical probability are {heads}%",
        "Both relative frequency and theoretical probability are 100%",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Relative frequency comes from the experiment: {heads} out of {trials}.",
        tier_2="Theoretical probability is always 1/2 = 50% for a fair coin.",
        tier_3=f"Comparison: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 30: Law of Large Numbers
# --------------------------------------------------------------------------- #
def _gen_prob_exp_law_of_large_numbers(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_law_of_large_numbers"
    name = r.choice(SA_NAMES)
    correct_ans = "The relative frequency gets closer and closer to the theoretical probability"

    prompt = (
        f"{name} tosses a fair coin 10 times, then 100 times, and finally 10 000 times.\n\n"
        f"According to the **Law of Large Numbers**, what happens to the experimental relative frequency of Heads "
        f"as the number of trials increases to a very large number?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The Law of Large Numbers states that as the number of repetitions of a random experiment increases, "
        f"the relative frequency of an event converges to its theoretical probability.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"With small samples (10 tosses), random variance causes large deviations (e.g. 70% Heads). "
        f"As trials reach 10 000, random fluctuations average out, and the relative frequency approaches 50% (0,50). "
        f"✓ [1 Mark: Method – articulating convergence of empirical frequency to theoretical value]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate principle statement]"
    )

    custom = [
        correct_ans,
        "The relative frequency moves further and further away from the theoretical probability",
        "The coin becomes biased and lands only on Heads",
        "The theoretical probability changes to match the experiment",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="As you do more and more trials, random fluctuations average out.",
        tier_2="Relative frequency approaches the theoretical probability.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 31: Expected Frequency Prediction
# --------------------------------------------------------------------------- #
def _gen_prob_exp_expected_frequency_prediction(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_expected_frequency_prediction"
    name = r.choice(SA_NAMES)
    trials = r.choice([120, 180, 240, 300, 600])
    # roll a six on a 6-sided die: p = 1/6
    expected = trials // 6
    correct_ans = f"{expected} times"

    prompt = (
        f"{name} plans to roll a fair 6-sided die **{trials} times**.\n\n"
        f"Calculate the **expected number of times** that the number 6 should appear.\n\n"
        f"**Formula**: $\\text{{Expected Frequency}} = P(E) \\times \\text{{Total Trials}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The theoretical probability of rolling a six is $P(\\text{{Six}}) = \\frac{{1}}{{6}}$. "
        f"The expected frequency is the product of probability and total trials: $E = P(E) \\times N$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Expected Frequency}} = \\frac{{1}}{{6}} \\times {trials} = \\frac{{{trials}}}{{6}}$$ ✓ [1 Mark: Method – multiplying probability by total trials]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Expected Frequency}} = {expected}\\text{{ times}}$$ ✓ [1 Mark: Accuracy – accurate integer expectation]"
    )

    d1 = f"{expected + 10} times"
    d2 = f"{expected - 5} times"
    d3 = f"{trials // 2} times"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Expected frequency = Probability × Total trials.",
        tier_2=f"Calculate (1/6) × {trials}.",
        tier_3=f"Expected frequency = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 32: Gambler's Fallacy & Independent Trials
# --------------------------------------------------------------------------- #
def _gen_prob_exp_gamblers_fallacy_independent_trials(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_gamblers_fallacy_independent_trials"
    name = r.choice(SA_NAMES)
    consecutive = r.choice([5, 6, 7])
    correct_ans = "1/2 (50%)"

    prompt = (
        f"{name} tosses a fair, unbiased coin and it lands on **Heads {consecutive} times in a row**.\n\n"
        f"What is the theoretical probability that the **next toss** will land on Tails?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Each coin flip is an independent trial: the coin has no memory of past outcomes.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The belief that Tails is 'due' after a run of Heads is a misconception known as the Gambler's Fallacy. "
        f"Because the coin is fair and unbiased, the probability of Tails on any individual toss remains unchanged: "
        f"$$P(\\text{{Tails}}) = \\frac{{1}}{{2}} = 50\\%$$ ✓ [1 Mark: Method – applying independence of trials]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct constant probability]"
    )

    custom = ["1/2 (50%)", "100% (Certain)", "almost 0%", "3/4 (75%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The coin has no memory of past flips.",
        tier_2="Each toss is completely independent.",
        tier_3=f"Probability remains {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 33: Detecting Biased Die
# --------------------------------------------------------------------------- #
def _gen_prob_exp_detecting_biased_die(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_detecting_biased_die"
    name = r.choice(SA_NAMES)
    correct_ans = "Number 6 (it appeared 320 times, far exceeding the expected 100 times)"

    prompt = (
        f"{name} tests a suspicious 6-sided die by rolling it 600 times. Expected frequency for each number is 100.\n"
        f"The experimental results are:\n"
        f"  • 1: 52 times | 2: 58 times | 3: 54 times | 4: 56 times | 5: 60 times | **6: 320 times**\n\n"
        f"Which number indicates that the die is loaded (biased)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"For a fair die rolled 600 times, each face should appear approximately $\\frac{{1}}{{6}} \\times 600 = 100$ times.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Number 6 appeared 320 times, which is more than 3 times its expected theoretical frequency, "
        f"while all other numbers appeared significantly less than expected. ✓ [1 Mark: Method – comparing observed counts with expected frequency of 100]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct biased outcome identification]"
    )

    custom = [
        correct_ans,
        "Number 1 (it appeared only 52 times)",
        "The die is completely fair because every number appeared",
        "Number 5 (it appeared 60 times)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Compare each frequency with the expected frequency of 100.",
        tier_2="Number 6 appeared 320 times (abnormally high).",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 34: Drawing Pin Tack Orientation
# --------------------------------------------------------------------------- #
def _gen_prob_exp_pin_tack_landing_orientation(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_pin_tack_landing_orientation"
    name = r.choice(SA_NAMES)
    total_drops = 200
    point_up = r.choice([124, 132, 140, 148])
    rf = round(point_up / total_drops, 2)
    pct = round(rf * 100, 1)
    correct_ans = f"{_fmt(rf)} ({_fmt(pct)}%)"

    prompt = (
        f"{name} drops a metal drawing pin (thumb tack) {total_drops} times to investigate asymmetrical probability.\n"
        f"The pin landed **point-up {point_up} times** and point-down {total_drops - point_up} times.\n\n"
        f"Calculate the **experimental probability** of the pin landing point-up."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because a drawing pin is not symmetrical, theoretical probability cannot be deduced by simple geometry; "
        f"we must rely on experimental relative frequency.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Point-up}}) = \\frac{{\\text{{Point-up occurrences}}}}{{\\text{{Total drops}}}} = \\frac{{{point_up}}}{{{total_drops}}}$$ ✓ [1 Mark: Method – dividing point-up trials by total drops]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Point-up}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate decimal and percentage]"
    )

    d1 = f"{_fmt(round((total_drops - point_up) / total_drops, 2))} ({_fmt(round((total_drops - point_up) / total_drops * 100, 1))}%)"
    d2 = "0,50 (50%)"  # assumed symmetrical 50/50
    d3 = f"{_fmt(round(point_up / 100, 2))} ({_fmt(point_up)}%)"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the number of times it landed point-up by the total drops.",
        tier_2=f"Calculate {point_up} ÷ {total_drops}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 35: Batch Sampling Defect Estimate
# --------------------------------------------------------------------------- #
def _gen_prob_exp_batch_sampling_defect_estimate(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_batch_sampling_defect_estimate"
    name = r.choice(SA_NAMES)
    sample_size = 500
    defects = r.choice([5, 8, 10, 12, 15])
    shipment_size = r.choice([10000, 20000, 25000, 50000])
    defect_rate = defects / sample_size
    est_defects = int(defect_rate * shipment_size)
    correct_ans = f"{est_defects} defective items"

    prompt = (
        f"{name} is a quality control inspector at an electronics factory.\n"
        f"In a random test sample of {sample_size} components, {defects} are found to be defective.\n\n"
        f"Based on this sample probability, estimate the total number of defective components "
        f"in a full production batch of **{_fmt(shipment_size)} components**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Find the empirical defect probability from the sample: $P(\\text{{Defect}}) = \\frac{{{defects}}}{{{sample_size}}}$.\n"
        f"Then multiply by the total shipment size to predict the expected total defects: $E = P(\\text{{Defect}}) \\times N$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Defect rate}} = \\frac{{{defects}}}{{{sample_size}}} = {_fmt(defect_rate, 4)}$$\n"
        f"$$\\text{{Estimated defects}} = {_fmt(defect_rate, 4)} \\times {shipment_size}$$ ✓ [1 Mark: Method – multiplying sample defect rate by shipment size]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Estimated defects}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate product with units]"
    )

    d1 = f"{est_defects + 50} defective items"
    d2 = f"{est_defects // 2} defective items"
    d3 = f"{defects * 10} defective items"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the defect rate: defects ÷ sample size.",
        tier_2=f"Rate = {defects} ÷ {sample_size}. Multiply by {shipment_size}.",
        tier_3=f"Estimated defects = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 36: Class Survey Empirical Probability
# --------------------------------------------------------------------------- #
def _gen_prob_exp_class_survey_empirical_probability(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_exp_class_survey_empirical_probability"
    name = r.choice(SA_NAMES)
    bus = r.choice([12, 15, 18])
    taxi = r.choice([10, 12, 14])
    walk = r.choice([8, 10, 12])
    total_class = bus + taxi + walk
    pct = round((taxi / total_class) * 100, 1)
    correct_ans = f"{taxi}/{total_class} ({_fmt(pct)}%)"

    prompt = (
        f"{name} conducts a transport survey among all {total_class} learners in a Grade 10 class:\n"
        f"  • Bus: {bus} learners\n"
        f"  • Minibus Taxi: {taxi} learners\n"
        f"  • Walk: {walk} learners\n\n"
        f"Calculate the empirical probability that a randomly chosen learner travels by **Minibus Taxi**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Empirical probability is the number of learners using a taxi divided by the total surveyed learners in the class.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Taxi}}) = \\frac{{{taxi}}}{{{total_class}}} = {_fmt(taxi / total_class, 3)}$$\n"
        f"$$\\text{{Percentage}} = {_fmt(taxi / total_class, 3)} \\times 100\\% = {_fmt(pct)}\\%$$ ✓ [1 Mark: Method – dividing category frequency by total surveyed]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Taxi}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    d1 = f"{bus}/{total_class} ({_fmt(round(bus/total_class*100, 1))}%)"
    d2 = f"{walk}/{total_class} ({_fmt(round(walk/total_class*100, 1))}%)"
    d3 = f"{taxi}/{total_class - taxi}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide taxi learners by the total class learners.",
        tier_2=f"{taxi} ÷ {total_class}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )
