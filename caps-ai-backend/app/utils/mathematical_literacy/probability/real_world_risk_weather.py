"""Cluster 6: Real-World Applications (Weather, Medicine & Risk) (Subskills 45 to 52)."""
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
# Subskill 45: Weather Forecast Precipitation Interpretation
# --------------------------------------------------------------------------- #
def _gen_prob_app_weather_forecast_precipitation_percentage(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_weather_forecast_precipitation_percentage"
    name = r.choice(SA_NAMES)
    town = r.choice(["Bloemfontein", "Mbombela", "Kimberley", "East London", "George"])
    correct_ans = "Thursday (80% probability)"

    prompt = (
        f"{name} consults a 5-day South African Weather Service forecast for {town}:\n\n"
        f"| Day | Mon | Tue | Wed | Thu | Fri |\n"
        f"| :--- | :---: | :---: | :---: | :---: | :---: |\n"
        f"| Probability of Rain | 10% | 25% | 40% | **80%** | 30% |\n\n"
        f"On which day is rain **most likely** to fall?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"On the probability scale, higher percentages indicate greater likelihood.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Comparing the 5 probabilities:\n"
        f"$$10\\% < 25\\% < 30\\% < 40\\% < 80\\%$$\n"
        f"Thursday has the maximum value of 80%. ✓ [1 Mark: Method – comparing probability percentages to find maximum likelihood]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct day and percentage identified]"
    )

    custom = ["Thursday (80% probability)", "Wednesday (40% probability)", "Friday (30% probability)", "Monday (10% probability)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the day with the highest percentage of rain.",
        tier_2="Thursday has 80%, which is higher than all other days.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 46: Veld Fire Danger Index
# --------------------------------------------------------------------------- #
def _gen_prob_app_weather_veld_fire_danger_index(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_weather_veld_fire_danger_index"
    name = r.choice(SA_NAMES)
    fdi = r.choice([82, 85, 90, 94])
    correct_ans = "Extreme Danger (Red warning: no open outdoor fires permitted)"

    prompt = (
        f"In the Free State grassland region, the daily National Veld and Forest Fire Danger Rating Index (FDI) reaches **{fdi}**.\n"
        f"FDI Categories:\n"
        f"  • 0–20: Blue (Safe)\n"
        f"  • 21–45: Green (Moderate)\n"
        f"  • 46–60: Yellow (Dangerous)\n"
        f"  • 61–75: Orange (Very Dangerous)\n"
        f"  • 76–100: Red (Extreme Danger)\n\n"
        f"Identify the fire risk warning level corresponding to an FDI of {fdi}."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The Fire Danger Index evaluates the probability and severity of runaway fires based on ambient temperature, "
        f"wind speed, and relative humidity.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"An FDI of {fdi} falls in the interval 76–100, which is classified as Red (Extreme Danger). "
        f"✓ [1 Mark: Method – matching index value to risk bracket]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct danger rating]"
    )

    custom = [
        correct_ans,
        "Moderate (Green warning)",
        "Dangerous (Yellow warning)",
        "Safe (Blue warning)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Match {fdi} to the FDI bracket.",
        tier_2=f"{fdi} is in the 76–100 range.",
        tier_3=f"Warning level = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 47: Quality Control Pass Rate
# --------------------------------------------------------------------------- #
def _gen_prob_app_manufacturing_quality_control_pass_rate(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_manufacturing_quality_control_pass_rate"
    name = r.choice(SA_NAMES)
    tested = 1000
    defect = r.choice([15, 20, 25, 30])
    passed = tested - defect
    pct_pass = round((passed / tested) * 100, 1)
    correct_ans = f"{_fmt(pct_pass)}% (0,{passed})"

    prompt = (
        f"{name} tests a batch of {tested} manufactured vehicle spark plugs.\n"
        f"Exactly {defect} spark plugs failed the quality assurance test.\n\n"
        f"Calculate the probability that a randomly chosen spark plug from this batch **passed** the test."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First determine the number of items that passed by subtracting defects from total items tested: $\\text{{Passed}} = {tested} - {defect} = {passed}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Pass}}) = \\frac{{{passed}}}{{{tested}}} = {_fmt(passed / tested, 3)}$$\n"
        f"$$\\text{{Percentage}} = {_fmt(passed / tested, 3)} \\times 100\\% = {_fmt(pct_pass)}\\%$$ ✓ [1 Mark: Method – dividing passing count by total tested and converting to %]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Pass}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate percentage and decimal]"
    )

    d1 = f"{_fmt(round(defect / tested * 100, 1))}%"  # fail rate
    d2 = f"{_fmt(round(pct_pass - 5, 1))}%"
    d3 = "100%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the number that passed: {tested} - {defect} = {passed}.",
        tier_2=f"Divide {passed} by {tested}.",
        tier_3=f"Pass probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 48: Medical Test Accuracy & False Positives
# --------------------------------------------------------------------------- #
def _gen_prob_app_medical_screening_test_accuracy(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_medical_screening_test_accuracy"
    name = r.choice(SA_NAMES)
    accuracy_pct = r.choice([95, 96, 98, 99])
    false_pct = 100 - accuracy_pct
    correct_ans = f"{false_pct}% (0,0{false_pct})"

    prompt = (
        f"A medical rapid diagnostic test has a verified accuracy rate of **{accuracy_pct}%**.\n\n"
        f"Calculate the complementary probability of an inaccurate (false) test result."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A test result is either accurate or inaccurate. The sum of both probabilities is 100% (1,0).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Inaccurate}}) = 100\\% - {accuracy_pct}\\% = {false_pct}\\% = 0,0{false_pct}$$ ✓ [1 Mark: Method – subtracting accuracy from 100%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Inaccurate}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate complementary probability]"
    )

    d1 = f"{accuracy_pct}%"
    d2 = f"{false_pct * 2}%"
    d3 = "0%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the accuracy rate from 100%.",
        tier_2=f"100% - {accuracy_pct}% = {false_pct}%.",
        tier_3=f"Error probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 49: National Lottery Sample Space Odds
# --------------------------------------------------------------------------- #
def _gen_prob_app_national_lottery_sample_space_odds(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_national_lottery_sample_space_odds"
    name = r.choice(SA_NAMES)
    correct_ans = "Virtually 0 (extremely unlikely: 1 in 14 million chance)"

    prompt = (
        f"{name} buys one ticket for the South African National Lottery (Lotto).\n"
        f"The game requires correctly guessing 6 numbers from a pool of 52 balls.\n"
        f"The total number of possible combinations is approximately 14 000 000.\n\n"
        f"On the probability scale, how would you classify the likelihood of winning the jackpot with one ticket?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"$$P(\\text{{Jackpot}}) = \\frac{{1}}{{14\\ 000\\ 000}} \\approx 0,0000000714$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Because this number is so astronomically small and sits directly adjacent to zero on the probability scale, "
        f"it is classified as virtually impossible or extremely unlikely. ✓ [1 Mark: Method – evaluating 1 in 14 million against probability scale benchmarks]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate verbal description]"
    )

    custom = [
        correct_ans,
        "Even chance (50% because you either win or lose)",
        "Likely (75%)",
        "Impossible (0% exact mathematical impossibility)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="1 in 14 million is very close to zero.",
        tier_2="It is extremely unlikely (almost 0).",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 50: Motor Vehicle Insurance Risk Tier
# --------------------------------------------------------------------------- #
def _gen_prob_app_motor_vehicle_insurance_risk_tier(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_motor_vehicle_insurance_risk_tier"
    name = r.choice(SA_NAMES)
    correct_ans = "Young, inexperienced drivers have a statistically higher collision probability"

    prompt = (
        f"{name} is 19 years old and shopping for car insurance.\n"
        f"Insurance actuarial statistics show that drivers aged 18–24 have a higher accident rate than drivers aged 35–50.\n\n"
        f"Why do short-term insurance companies charge younger drivers higher monthly premiums?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Insurance premiums are calculated directly based on the probability of a claim occurring (actuarial risk).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Because empirical historical data shows younger drivers have a higher probability of collision claims, "
        f"the insurer incurs greater financial risk and must charge a higher premium to offset that probability. "
        f"✓ [1 Mark: Method – connecting higher empirical accident probability to risk premiums]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct risk rationale]"
    )

    custom = [
        correct_ans,
        "Insurance companies dislike young people",
        "Older drivers never have any accidents",
        "The price of petrol is higher for younger drivers",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Insurance premiums depend on the probability of an accident.",
        tier_2="Higher risk probability leads to higher premiums.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 51: Blood Type Donor Compatibility Probability
# --------------------------------------------------------------------------- #
def _gen_prob_app_blood_type_donor_compatibility(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_blood_type_donor_compatibility"
    name = r.choice(SA_NAMES)
    type_o_pct = 45  # South African National Blood Service: ~45% Type O
    type_a_pct = 32
    type_b_pct = 18
    type_ab_pct = 5
    correct_ans = "45% (0,45)"

    prompt = (
        f"According to South African National Blood Service (SANBS) statistics:\n"
        f"  • Blood Group O: 45%\n"
        f"  • Blood Group A: 32%\n"
        f"  • Blood Group B: 18%\n"
        f"  • Blood Group AB: 5%\n\n"
        f"Calculate the theoretical probability that a randomly selected donor at a blood drive is **Blood Group O**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Population frequencies translate directly into empirical probabilities for random individual selection.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Blood Group O}}) = \\frac{{45}}{{100}} = 0,45 = 45\\%$$ ✓ [1 Mark: Method – expressing percentage frequency as probability]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate probability expression]"
    )

    custom = ["45% (0,45)", "32% (0,32)", "18% (0,18)", "5% (0,05)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the frequency percentage for Blood Group O.",
        tier_2="Group O frequency is 45%.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 52: Decision Making Under Uncertainty
# --------------------------------------------------------------------------- #
def _gen_prob_app_decision_making_under_uncertainty(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_app_decision_making_under_uncertainty"
    name = r.choice(SA_NAMES)
    cost_marquee = 4500
    rain_prob = r.choice([75, 80, 85])
    correct_ans = f"Rent the marquee tent (high 75–85% probability of rain threatens the event)"

    prompt = (
        f"{name} is hosting an outdoor wedding reception in {r.choice(SA_NAMES)}'s garden.\n"
        f"A commercial marquee tent costs R {_fmt(cost_marquee)} to rent.\n"
        f"The 24-hour weather forecast indicates an **{rain_prob}% probability of heavy thunderstorms**.\n\n"
        f"What is the most prudent, mathematically sound decision based on this probability?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Decision making under uncertainty balances the likelihood of an adverse event against the cost of prevention.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"An {rain_prob}% probability represents a very high likelihood of rain (close to 1,0 on the scale). "
        f"Proceeding without shelter carries an 80%+ chance of ruining the event, whereas renting the tent guarantees shelter. "
        f"✓ [1 Mark: Method – applying high probability assessment to risk mitigation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – logical decision justified by probability]"
    )

    custom = [
        f"Rent the marquee tent (high 75–85% probability of rain threatens the event)",
        "Do not rent the tent because rain is impossible",
        "Assume the forecast is completely wrong and ignore it",
        "Cancel the wedding permanently",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="An {rain_prob}% rain probability means rain is very likely.",
        tier_2="Risking an outdoor wedding in 80%+ rain is unwise.",
        tier_3=f"The best decision is: {correct_ans}.",
        r=r,
    )
