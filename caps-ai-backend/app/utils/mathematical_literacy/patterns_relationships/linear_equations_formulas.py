"""Cluster 3: Formulating Linear Equations (y = mx + c) (Subskills 19 to 27)."""
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
)

# --------------------------------------------------------------------------- #
# Subskill 19: Formula from Verbal Description
# --------------------------------------------------------------------------- #
def _gen_pat_formula_from_verbal_description(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_from_verbal_description"
    name = r.choice(SA_NAMES)
    base = r.choice([150, 200, 250, 300])
    rate = r.choice([25, 30, 40, 50])
    correct_ans = f"Cost = {base} + ({rate} × n)"

    prompt = (
        f"{name} hires garden equipment from a plant hire company.\n"
        f"The company charges a fixed administration fee of R {base}, plus R {rate} for each day ($n$) the machine is kept.\n\n"
        f"Which formula correctly calculates the total cost in Rands for $n$ days?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A linear pricing model has a fixed starting constant ($c$) and a variable rate per unit ($m$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Cost}} = \\text{{Fixed Base Fee}} + (\\text{{Daily Rate}} \\times n)$$\n"
        f"$$\\text{{Total Cost}} = {base} + ({rate} \\times n)$$ ✓ [1 Mark: Method – constructing linear equation from verbal terms]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate algebraic formula]"
    )

    d1 = f"Cost = ({base} + {rate}) × n"
    d2 = f"Cost = {rate} + ({base} × n)"
    d3 = f"Cost = {base} × n"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The fixed fee is paid only once; the rate is multiplied by n.",
        tier_2=f"Total cost = {base} + {rate} × n.",
        tier_3=f"Formula is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 20: Formula from Table of Values
# --------------------------------------------------------------------------- #
def _gen_pat_formula_from_table_of_values(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_from_table_of_values"
    name = r.choice(SA_NAMES)
    m = r.choice([15, 20, 25, 30])
    c = r.choice([50, 75, 100])
    x1, x2, x3 = 1, 2, 3
    y1, y2, y3 = m * 1 + c, m * 2 + c, m * 3 + c
    correct_ans = f"y = {m}x + {c}"

    prompt = (
        f"{name} investigates a dataset presented in the table below:\n\n"
        f"| $x$ | {x1} | {x2} | {x3} |\n"
        f"| :---: | :---: | :---: | :---: |\n"
        f"| $y$ | {y1} | {y2} | {y3} |\n\n"
        f"Find the linear equation in the form **$y = mx + c$** that models this relationship."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Determine the constant rate of change (gradient $m$) from consecutive differences, "
        f"then find the initial constant ($c$) by setting $x = 0$ (or substituting a known pair).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{1}} = {m}$$\n"
        f"$$c = y - mx = {y1} - ({m} \\times 1) = {c}$$ ✓ [1 Mark: Method – calculating gradient and solving for y-intercept]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate linear equation]"
    )

    d1 = f"y = {m}x"
    d2 = f"y = {c}x + {m}"
    d3 = f"y = {m+5}x + {c}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the difference in y-values to get m.",
        tier_2=f"Difference = {m}. When x = 1, y = {y1} → c = {y1} - {m} = {c}.",
        tier_3=f"The equation is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 21: Identify Rate and Constant in Formula
# --------------------------------------------------------------------------- #
def _gen_pat_formula_identify_rate_and_constant(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_identify_rate_and_constant"
    name = r.choice(SA_NAMES)
    rate = r.choice([35, 45, 60, 75, 80])
    fixed = r.choice([120, 150, 180, 220, 250])
    correct_ans = f"Rate = R {rate}/hour; Fixed Constant = R {fixed}"

    prompt = (
        f"{name} is billed according to the maintenance formula: **$\\text{{Total}} = {rate} \\times h + {fixed}$**, "
        f"where $h$ is the number of hours worked.\n\n"
        f"Identify the **variable hourly rate** and the **fixed base constant** in this formula."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In any linear relation $y = mx + c$, the coefficient of the variable ($m$) represents the variable rate of change, "
        f"and the standalone number ($c$) represents the fixed constant value.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The coefficient multiplying hours $h$ is {rate}, which is the variable hourly rate.\n"
        f"The standalone constant is {fixed}, which is the fixed call-out / base fee. "
        f"✓ [1 Mark: Method – matching algebraic components to real-world definitions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct parameter identification]"
    )

    custom = [
        correct_ans,
        f"Rate = R {fixed}/hour; Fixed Constant = R {rate}",
        f"Rate = R {rate + fixed}/hour; Fixed Constant = R 0",
        f"Rate = R {rate}/hour; Fixed Constant = R 0",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The number multiplied by h is the hourly rate.",
        tier_2=f"The standalone number is the fixed fee: {fixed}.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 22: Cellphone Contract Monthly Cost
# --------------------------------------------------------------------------- #
def _gen_pat_formula_cellphone_contract_monthly_cost(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_cellphone_contract_monthly_cost"
    name = r.choice(SA_NAMES)
    monthly_sub = r.choice([149.00, 199.00, 249.00, 299.00])
    call_rate = r.choice([1.20, 1.50, 1.75, 2.00])
    extra_mins = r.choice([40, 60, 80, 100, 120])
    call_cost = extra_mins * call_rate
    total_cost = monthly_sub + call_cost
    correct_ans = _fmt_curr(total_cost)

    prompt = (
        f"{name} subscribes to a cell phone package governed by the formula:\n"
        f"**$\\text{{Monthly Bill}} = {_fmt_curr(monthly_sub)} + ({_fmt_curr(call_rate)} \\times m)$**, where $m$ is the number of out-of-bundle call minutes used.\n\n"
        f"Calculate the total monthly bill if {name} uses {extra_mins} out-of-bundle minutes."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the minute usage $m = {extra_mins}$ into the pricing formula.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Call charges}} = {_fmt_curr(call_rate)} \\times {extra_mins} = {_fmt_curr(call_cost)}$$\n"
        f"$$\\text{{Total Bill}} = {_fmt_curr(monthly_sub)} + {_fmt_curr(call_cost)}$$ ✓ [1 Mark: Method – evaluating minute product and adding subscription]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Bill}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(call_cost)  # forgot subscription
    d2 = _fmt_curr(total_cost * 1.15)  # added extra tax
    d3 = _fmt_curr(total_cost - 50)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the call minutes by the call rate, then add the subscription.",
        tier_2=f"Minutes cost = {extra_mins} × {_fmt_curr(call_rate)} = {_fmt_curr(call_cost)}. Add {_fmt_curr(monthly_sub)}.",
        tier_3=f"Total bill = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 23: Electrician Call-out Plus Hours
# --------------------------------------------------------------------------- #
def _gen_pat_formula_electrician_callout_plus_hours(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_electrician_callout_plus_hours"
    name = r.choice(SA_NAMES)
    callout = r.choice([350.00, 400.00, 450.00, 500.00])
    hourly_rate = r.choice([250.00, 300.00, 350.00])
    hours = r.choice([2.5, 3.0, 3.5, 4.0])
    labour = hours * hourly_rate
    total_fee = callout + labour
    correct_ans = _fmt_curr(total_fee)

    prompt = (
        f"{name} calls out a qualified electrician to repair a distribution board.\n"
        f"The billing formula is: **$\\text{{Fee}} = {_fmt_curr(callout)} + ({_fmt_curr(hourly_rate)} \\times h)$**, where $h$ is the hours of labour.\n\n"
        f"Calculate the total fee if the job takes {_fmt(hours)} hours."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply the hours worked by the hourly labour rate, then add the initial call-out fee.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Labour cost}} = {_fmt(hours)} \\times {_fmt_curr(hourly_rate)} = {_fmt_curr(labour)}$$\n"
        f"$$\\text{{Total Fee}} = {_fmt_curr(callout)} + {_fmt_curr(labour)}$$ ✓ [1 Mark: Method – substituting hours into linear formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Fee}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(labour)  # forgot callout
    d2 = _fmt_curr(total_fee + 150)
    d3 = _fmt_curr(total_fee * 0.9)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply hours by hourly rate, then add call-out fee.",
        tier_2=f"Labour = {_fmt(hours)} × {_fmt_curr(hourly_rate)} = {_fmt_curr(labour)}. Add {_fmt_curr(callout)}.",
        tier_3=f"Total fee = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 24: Taxi Fare Flagfall Plus Km
# --------------------------------------------------------------------------- #
def _gen_pat_formula_taxi_fare_flagfall_plus_km(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_taxi_fare_flagfall_plus_km"
    name = r.choice(SA_NAMES)
    flagfall = r.choice([20.00, 25.00, 30.00])
    rate_km = r.choice([10.50, 12.00, 14.50, 15.00])
    distance = r.choice([12, 15, 18, 22, 25])
    distance_cost = distance * rate_km
    total_fare = flagfall + distance_cost
    correct_ans = _fmt_curr(total_fare)

    prompt = (
        f"{name} books a private metered taxi.\n"
        f"The fare structure is modeled by: **$\\text{{Fare}} = {_fmt_curr(flagfall)} + ({_fmt_curr(rate_km)} \\times d)$**, "
        f"where $d$ is the distance driven in kilometres.\n\n"
        f"Calculate the total taxi fare for a trip of {distance} km."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the trip distance $d = {distance}$ km into the linear pricing equation.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Distance charge}} = {distance} \\times {_fmt_curr(rate_km)} = {_fmt_curr(distance_cost)}$$\n"
        f"$$\\text{{Total Fare}} = {_fmt_curr(flagfall)} + {_fmt_curr(distance_cost)}$$ ✓ [1 Mark: Method – evaluating distance product and adding flagfall]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Fare}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(distance_cost)  # forgot flagfall
    d2 = _fmt_curr(total_fare + 20)
    d3 = _fmt_curr(total_fare * 0.85)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply distance by rate per km, then add flagfall.",
        tier_2=f"Distance charge = {distance} × {_fmt_curr(rate_km)} = {_fmt_curr(distance_cost)}. Add {_fmt_curr(flagfall)}.",
        tier_3=f"Total fare = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 25: Event Catering Venue Plus Guests
# --------------------------------------------------------------------------- #
def _gen_pat_formula_event_catering_venue_plus_guests(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_event_catering_venue_plus_guests"
    name = r.choice(SA_NAMES)
    venue = r.choice([2500.00, 3000.00, 3500.00, 4000.00])
    per_guest = r.choice([120.00, 150.00, 180.00, 200.00])
    guests = r.choice([40, 50, 60, 75, 80])
    food_cost = guests * per_guest
    total_event = venue + food_cost
    correct_ans = _fmt_curr(total_event)

    prompt = (
        f"{name} is organizing a community banquet hall event.\n"
        f"The venue hire formula is: **$\\text{{Cost}} = {_fmt_curr(venue)} + ({_fmt_curr(per_guest)} \\times g)$**, "
        f"where $g$ represents the number of attending guests.\n\n"
        f"Calculate the total event cost for {guests} guests."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the variable food and catering cost by multiplying guests by the rate per guest, then add the fixed venue rental fee.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Guest catering}} = {guests} \\times {_fmt_curr(per_guest)} = {_fmt_curr(food_cost)}$$\n"
        f"$$\\text{{Total Cost}} = {_fmt_curr(venue)} + {_fmt_curr(food_cost)}$$ ✓ [1 Mark: Method – substituting guests and summing with venue]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(food_cost)  # forgot venue
    d2 = _fmt_curr(total_event + 500)
    d3 = _fmt_curr(total_event * 0.9)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply number of guests by cost per guest, then add venue fee.",
        tier_2=f"Catering = {guests} × {_fmt_curr(per_guest)} = {_fmt_curr(food_cost)}. Add {_fmt_curr(venue)}.",
        tier_3=f"Total cost = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 26: Maximum Units Affordable from Budget
# --------------------------------------------------------------------------- #
def _gen_pat_formula_calculate_maximum_units_budget(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_calculate_maximum_units_budget"
    name = r.choice(SA_NAMES)
    base = r.choice([150, 200, 250])
    rate = r.choice([25, 30, 40])
    budget = r.choice([600, 750, 850, 1000])
    avail = budget - base
    max_units = avail // rate
    correct_ans = f"{max_units} units"

    prompt = (
        f"{name} has a maximum budget of R {budget} for hiring tool equipment.\n"
        f"The rental cost formula is: **$\\text{{Cost}} = {base} + ({rate} \\times n)$**, where $n$ is the number of days hired.\n\n"
        f"Calculate the maximum number of full days {name} can afford to hire the equipment."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Subtract the mandatory fixed fee from the budget, then divide by the daily rate and round DOWN to whole days.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Remaining budget for days}} = {budget} - {base} = {avail}\\text{{ Rands}}$$\n"
        f"$$n = \\frac{{{avail}}}{{{rate}}} = {_fmt(avail / rate, 2)}$$ ✓ [1 Mark: Method – subtracting base fee and dividing by daily rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"Round down to complete affordable days: **{max_units} units** (days) ✓ [1 Mark: Accuracy – correct downward integer rounding]"
    )

    d1 = f"{max_units + 1} units"  # rounded up (unaffordable)
    d2 = f"{budget // rate} units"  # forgot to subtract base
    d3 = f"{max_units - 1} units"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the fixed fee from your budget first.",
        tier_2=f"Calculate ({budget} - {base}) ÷ {rate} = {_fmt(avail / rate, 2)}.",
        tier_3=f"Round down to whole days: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 27: Temperature Conversion Linear Formula
# --------------------------------------------------------------------------- #
def _gen_pat_formula_temperature_conversion_linear(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_formula_temperature_conversion_linear"
    name = r.choice(SA_NAMES)
    celsius = r.choice([15, 20, 25, 30, 35, 100])
    fahrenheit = round(1.8 * celsius + 32, 1)
    correct_ans = f"{_fmt(fahrenheit)} °F"

    prompt = (
        f"{name} is converting an outdoor temperature reading of {celsius} °C to Fahrenheit.\n"
        f"The linear conversion formula is: **$F = (1,8 \\times C) + 32$**.\n\n"
        f"Calculate the equivalent temperature in degrees Fahrenheit (°F)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the Celsius temperature $C = {celsius}$ into the linear formula.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$F = (1,8 \\times {celsius}) + 32 = {_fmt(1.8 * celsius)} + 32$$ ✓ [1 Mark: Method – substituting Celsius into linear conversion equation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$F = {_fmt(fahrenheit)}^\\circ\\text{{F}}$$ ✓ [1 Mark: Accuracy – accurate product and sum]"
    )

    d1 = f"{_fmt(1.8 * celsius)} °F"  # forgot 32
    d2 = f"{_fmt(celsius + 32)} °F"
    d3 = f"{_fmt(round(fahrenheit + 10, 1))} °F"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the Celsius value by 1,8, then add 32.",
        tier_2=f"1,8 × {celsius} = {_fmt(1.8 * celsius)}. Add 32.",
        tier_3=f"Temperature = {correct_ans}.",
        r=r,
    )
