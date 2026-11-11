"""Subskills 45 to 52: Two-Graph Systems, Simultaneous Comparisons & Decision Making for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Prepaid vs Postpaid electricity tariff comparison: find breakeven kWh usage."""
    name = r.choice(SA_NAMES)
    kwh_equal = r.choice([250, 300, 350, 400, 450, 500, 600])

    # Rate diff in rands per kWh
    rate_diff = r.choice([0.50, 0.60, 0.75, 0.80, 1.00, 1.20])
    fixed_postpaid = round(kwh_equal * rate_diff, 2)

    base_rate = r.choice([1.80, 2.10, 2.25, 2.40])
    rate_postpaid = base_rate
    rate_prepaid = round(base_rate + rate_diff, 2)

    prompt = (
        f"{name} is deciding between two municipal electricity billing options for a household:\n"
        f"• Option A (Prepaid): No fixed monthly charge, but electricity costs {_fmt_curr(rate_prepaid)} per kWh.\n"
        f"• Option B (Postpaid / Conventional): A fixed monthly service fee of {_fmt_curr(fixed_postpaid)} plus "
        f"{_fmt_curr(rate_postpaid)} per kWh.\n"
        f"At what monthly electricity consumption (in kWh) will the total cost for both options be exactly equal?"
    )

    correct_ans = f"{_fmt(kwh_equal)} kWh"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Set up the equation Cost A = Cost B [1 mark].\n"
        f"{_fmt(rate_prepaid)} × k = {_fmt(fixed_postpaid)} + ({_fmt(rate_postpaid)} × k).\n"
        f"Step 2: Collect like terms [1 mark].\n"
        f"({_fmt(rate_prepaid)} - {_fmt(rate_postpaid)}) × k = {_fmt(fixed_postpaid)}\n"
        f"{_fmt(rate_diff)} × k = {_fmt(fixed_postpaid)}\n"
        f"k = {_fmt(fixed_postpaid)} ÷ {_fmt(rate_diff)} = {_fmt(kwh_equal)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="45",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Equate the two expressions: (Rate A × k) = Fixed Fee + (Rate B × k).",
        tier_2=f"The difference in per-kWh rate is {_fmt_curr(rate_diff)}. Divide the fixed charge of {_fmt_curr(fixed_postpaid)} by {_fmt_curr(rate_diff)}.",
        tier_3=f"{_fmt_curr(fixed_postpaid)} ÷ {_fmt_curr(rate_diff)} = {_fmt(kwh_equal)} kWh.",
        r=r,
    )


def _gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Vehicle / Bakkie hire comparison: flat daily fee + km rate vs pure km rate."""
    name = r.choice(SA_NAMES)
    km_equal = r.choice([150, 200, 250, 300, 400, 500])

    diff_km = r.choice([1.50, 2.00, 2.50, 3.00])
    fixed_daily = round(km_equal * diff_km, 2)

    rate_low = r.choice([2.50, 3.00, 3.50])
    rate_high = round(rate_low + diff_km, 2)

    prompt = (
        f"{name} needs to rent a bakkie for a day to move furniture:\n"
        f"• QuickHire: Charges a daily flat fee of {_fmt_curr(fixed_daily)} plus {_fmt_curr(rate_low)} per kilometre driven.\n"
        f"• DriveEasy: Charges no daily flat fee, but charges {_fmt_curr(rate_high)} per kilometre driven.\n"
        f"At what distance (in km) will both rental companies cost the exact same amount?"
    )

    correct_ans = f"{_fmt(km_equal)} km"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Set up the cost equation [1 mark].\n"
        f"QuickHire Cost = DriveEasy Cost\n"
        f"{_fmt(fixed_daily)} + {_fmt(rate_low)} × d = {_fmt(rate_high)} × d.\n"
        f"Step 2: Solve for distance d [1 mark].\n"
        f"{_fmt(fixed_daily)} = ({_fmt(rate_high)} - {_fmt(rate_low)}) × d\n"
        f"{_fmt(fixed_daily)} = {_fmt(diff_km)} × d\n"
        f"d = {_fmt(fixed_daily)} ÷ {_fmt(diff_km)} = {_fmt(km_equal)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="46",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the distance where Daily Fee + (Low Rate × km) = High Rate × km.",
        tier_2=f"The difference in per-km rate is {_fmt_curr(diff_km)}. Divide the flat fee of {_fmt_curr(fixed_daily)} by {_fmt_curr(diff_km)}.",
        tier_3=f"{_fmt_curr(fixed_daily)} ÷ {_fmt_curr(diff_km)} = {_fmt(km_equal)} km.",
        r=r,
    )


def _gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Cellphone contract vs Prepaid comparison."""
    name = r.choice(SA_NAMES)
    minutes_equal = r.choice([120, 150, 180, 200, 240, 300])

    diff_rate = r.choice([0.60, 0.75, 0.80, 1.00, 1.25])
    sub_fee = round(minutes_equal * diff_rate, 2)
    rate_contract = 0.50
    rate_prepaid = round(rate_contract + diff_rate, 2)

    prompt = (
        f"{name} is comparing two cellphone plans for voice calls:\n"
        f"• Plan Alpha (Contract): Monthly subscription of {_fmt_curr(sub_fee)} plus {_fmt_curr(rate_contract)} per minute.\n"
        f"• Plan Beta (Prepaid): No monthly subscription, but calls cost {_fmt_curr(rate_prepaid)} per minute.\n"
        f"How many call minutes per month make Plan Alpha the cheaper option?"
    )

    correct_ans = f"More than {_fmt(minutes_equal)} minutes"
    wrong_1 = f"Fewer than {_fmt(minutes_equal)} minutes"
    wrong_2 = f"Exactly {_fmt(int(minutes_equal * 0.5))} minutes"
    wrong_3 = f"More than {_fmt(int(minutes_equal * 1.5))} minutes"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the break-even calling minutes [1 mark].\n"
        f"{_fmt(sub_fee)} + {_fmt(rate_contract)} × m = {_fmt(rate_prepaid)} × m\n"
        f"{_fmt(sub_fee)} = ({_fmt(rate_prepaid)} - {_fmt(rate_contract)}) × m\n"
        f"m = {_fmt(sub_fee)} ÷ {_fmt(diff_rate)} = {_fmt(minutes_equal)} minutes.\n"
        f"Step 2: Determine which plan is cheaper for higher volume [1 mark].\n"
        f"Because Plan Alpha has a lower per-minute call rate, its total cost grows more slowly, making it cheaper when talk time exceeds {_fmt(minutes_equal)} minutes.\n"
        f"Step 3: Stated condition [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="47",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the break-even minutes first, then determine when the contract with lower per-minute rate becomes more economical.",
        tier_2=f"The break-even point is {_fmt_curr(sub_fee)} ÷ {_fmt_curr(diff_rate)} = {_fmt(minutes_equal)} minutes.",
        tier_3=f"For calls exceeding {_fmt(minutes_equal)} minutes, Plan Alpha is cheaper: {correct_ans}.",
        r=r,
    )


def _gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Distance-time catch-up problem between two vehicles/travelers."""
    name_a = r.choice(["Bongani", "Sipho", "Thabo", "Jabu"])
    name_b = r.choice(["Lerato", "Zanele", "Nomvula", "Keletso"])

    # Speed A (slower), Speed B (faster)
    speed_a = r.choice([60, 70, 80])
    diff_speed = r.choice([20, 30, 40])
    speed_b = speed_a + diff_speed

    # Head start in hours
    head_start_hours = r.choice([1, 2, 3])
    lead_distance = speed_a * head_start_hours

    # Time for B to catch A: t = lead_distance / diff_speed
    # Choose clean integer time
    combos = [
        (60, 90, 30, 1, 60, 2, 180),
        (60, 90, 30, 2, 120, 4, 360),
        (70, 105, 35, 1, 70, 2, 210),
        (80, 120, 40, 1, 80, 2, 240),
        (80, 100, 20, 1, 80, 4, 400),
        (60, 100, 40, 2, 120, 3, 300),
    ]
    speed_a, speed_b, diff_speed, head_start_hours, lead_distance, t_catch, dist_catch = r.choice(combos)

    prompt = (
        f"{name_a} and {name_b} travel along the N1 highway in the same direction.\n"
        f"• {name_a} departs at 06:00 travelling at a constant speed of {_fmt(speed_a)} km/h.\n"
        f"• {name_b} departs {_fmt(head_start_hours)} hour(s) later travelling at a constant speed of {_fmt(speed_b)} km/h.\n"
        f"How many hours after {name_b}'s departure will {name_b} overtake {name_a}, and at what distance from the starting point?"
    )

    correct_ans = f"{_fmt(t_catch)} hours and {_fmt(dist_catch)} km"
    wrong_1 = f"{_fmt(t_catch + 1)} hours and {_fmt(dist_catch + 50)} km"
    wrong_2 = f"{_fmt(t_catch)} hours and {_fmt(lead_distance)} km"
    wrong_3 = f"{_fmt(t_catch + 2)} hours and {_fmt(dist_catch * 1.5)} km"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate {name_a}'s head start distance [1 mark].\n"
        f"Distance lead = Speed × Time = {_fmt(speed_a)} km/h × {_fmt(head_start_hours)} h = {_fmt(lead_distance)} km.\n"
        f"Step 2: Calculate relative speed and catch-up time [1 mark].\n"
        f"Relative closing speed = {_fmt(speed_b)} - {_fmt(speed_a)} = {_fmt(diff_speed)} km/h.\n"
        f"Catch-up time for {name_b} = {_fmt(lead_distance)} ÷ {_fmt(diff_speed)} = {_fmt(t_catch)} hours.\n"
        f"Step 3: Calculate catch-up distance [1 mark].\n"
        f"Distance = {_fmt(speed_b)} km/h × {_fmt(t_catch)} h = {_fmt(dist_catch)} km ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="48",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine the head start distance, divide by the difference in speeds, and multiply by the faster driver's speed.",
        tier_2=f"Lead distance is {_fmt(lead_distance)} km. The speed difference is {_fmt(diff_speed)} km/h, taking {_fmt(t_catch)} hours to close.",
        tier_3=f"Catch-up occurs after {_fmt(t_catch)} hours at {_fmt(speed_b)} × {_fmt(t_catch)} = {_fmt(dist_catch)} km.",
        r=r,
    )


def _gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Gym / Sports club membership vs pay-per-visit breakeven."""
    name = r.choice(SA_NAMES)
    visits_equal = r.choice([6, 8, 10, 12, 14, 15, 16])

    diff_visit = r.choice([25, 30, 40, 50, 60])
    monthly_fee = visits_equal * diff_visit
    member_visit_fee = r.choice([15, 20, 25, 30])
    guest_visit_fee = member_visit_fee + diff_visit

    prompt = (
        f"{name} is considering joining a local fitness centre:\n"
        f"• Option 1 (Member): Monthly membership fee of {_fmt_curr(monthly_fee)} plus {_fmt_curr(member_visit_fee)} per visit.\n"
        f"• Option 2 (Casual / Guest): No monthly membership fee, but {_fmt_curr(guest_visit_fee)} per visit.\n"
        f"What is the minimum number of visits {name} must make in a month for the membership (Option 1) to be cheaper than pay-per-visit?"
    )

    min_visits = visits_equal + 1
    correct_ans = f"{_fmt(min_visits)} visits"
    wrong_1 = f"{_fmt(visits_equal)} visits"
    wrong_2 = f"{_fmt(max(1, visits_equal - 2))} visits"
    wrong_3 = f"{_fmt(visits_equal + 4)} visits"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the break-even number of visits where costs are equal [1 mark].\n"
        f"{_fmt(monthly_fee)} + {_fmt(member_visit_fee)} × v = {_fmt(guest_visit_fee)} × v\n"
        f"{_fmt(monthly_fee)} = ({_fmt(guest_visit_fee)} - {_fmt(member_visit_fee)}) × v = {_fmt(diff_visit)} × v\n"
        f"v = {_fmt(monthly_fee)} ÷ {_fmt(diff_visit)} = {_fmt(visits_equal)} visits.\n"
        f"Step 2: Determine threshold for Option 1 to be cheaper [1 mark].\n"
        f"At {_fmt(visits_equal)} visits, both options cost the exact same. Therefore, {name} needs at least {_fmt(visits_equal)} + 1 = {_fmt(min_visits)} visits for membership to save money.\n"
        f"Step 3: Stated minimum visits [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="49",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the break-even number of visits, then add 1 to determine when the membership option becomes strictly cheaper.",
        tier_2=f"Break-even visits = {_fmt_curr(monthly_fee)} ÷ {_fmt_curr(diff_visit)} = {_fmt(visits_equal)} visits.",
        tier_3=f"At {_fmt(visits_equal)} visits costs are equal; at {_fmt(min_visits)} visits or more Option 1 is cheaper.",
        r=r,
    )


def _gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: In-house delivery vehicle vs Outsourced courier service."""
    name = r.choice(SA_NAMES)
    deliveries_equal = r.choice([80, 100, 120, 150, 180, 200])

    diff_cost = r.choice([20, 25, 30, 35, 40])
    fixed_inhouse = deliveries_equal * diff_cost
    inhouse_var = r.choice([15, 20, 25, 30])
    courier_flat = inhouse_var + diff_cost

    prompt = (
        f"{name}'s bakery delivers specialty celebration cakes across the city:\n"
        f"• In-House Delivery: Buying and operating a dedicated delivery scooter costs {_fmt_curr(fixed_inhouse)} "
        f"per month in insurance and depreciation, plus {_fmt_curr(inhouse_var)} in fuel and maintenance per delivery.\n"
        f"• Outsourced Courier: A local courier company charges a flat rate of {_fmt_curr(courier_flat)} per delivery with zero monthly retainer.\n"
        f"Calculate the monthly delivery volume at which both options cost the same."
    )

    correct_ans = f"{_fmt(deliveries_equal)} deliveries"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Set up the equation of total costs [1 mark].\n"
        f"In-House Cost = Courier Cost\n"
        f"{_fmt(fixed_inhouse)} + ({_fmt(inhouse_var)} × d) = {_fmt(courier_flat)} × d.\n"
        f"Step 2: Solve for number of deliveries d [1 mark].\n"
        f"{_fmt(fixed_inhouse)} = ({_fmt(courier_flat)} - {_fmt(inhouse_var)}) × d = {_fmt(diff_cost)} × d\n"
        f"d = {_fmt(fixed_inhouse)} ÷ {_fmt(diff_cost)} = {_fmt(deliveries_equal)} deliveries.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="50",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Set up Fixed Cost + (Variable Cost × d) = Courier Rate × d.",
        tier_2=f"Difference per delivery is {_fmt_curr(courier_flat)} - {_fmt_curr(inhouse_var)} = {_fmt_curr(diff_cost)}. Divide {_fmt_curr(fixed_inhouse)} by {_fmt_curr(diff_cost)}.",
        tier_3=f"{_fmt_curr(fixed_inhouse)} ÷ {_fmt_curr(diff_cost)} = {_fmt(deliveries_equal)} deliveries.",
        r=r,
    )


def _gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Read intersection coordinates from two-graph comparison with diagram_spec."""
    name = r.choice(SA_NAMES)
    x_int = r.choice([100, 150, 200, 250, 300, 400])
    fixed_a = r.choice([300, 400, 500, 600])
    rate_a = 2.0
    y_int = fixed_a + int(rate_a * x_int)
    rate_b = y_int / x_int

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "cartesian_system",
        "title": "Comparison of Service Provider A and Provider B",
        "x_label": "Units of Service Used (x)",
        "y_label": "Total Cost in Rands (R)",
        "x_range": [0, int(x_int * 1.6)],
        "y_range": [0, int(y_int * 1.6)],
        "lines": [
            {
                "label": "Provider A",
                "points": [[0, fixed_a], [x_int, y_int], [int(x_int * 1.6), fixed_a + int(rate_a * x_int * 1.6)]],
                "color": "#2563eb",
            },
            {
                "label": "Provider B",
                "points": [[0, 0], [x_int, y_int], [int(x_int * 1.6), int(rate_b * x_int * 1.6)]],
                "color": "#f59e0b",
            },
        ],
        "points_of_interest": [
            {"x": x_int, "y": y_int, "label": f"Intersection ({x_int}; {_fmt_curr(y_int)})"}
        ],
    }

    test_higher = int(x_int * 1.3)
    prompt = (
        f"Refer to the accompanying graph showing the cost comparison between Provider A (blue line) "
        f"and Provider B (amber line).\n"
        f"Based on the graph, which provider is cheaper if a consumer uses {_fmt(test_higher)} units of service per month?"
    )

    correct_ans = "Provider A is cheaper"
    wrong_1 = "Provider B is cheaper"
    wrong_2 = "Both providers cost the exact same amount"
    wrong_3 = "Neither provider is viable"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the intersection point [1 mark].\n"
        f"The two lines intersect at x = {_fmt(x_int)} units and y = {_fmt_curr(y_int)}.\n"
        f"Step 2: Inspect the graph for usage above {_fmt(x_int)} units [1 mark].\n"
        f"For usage x = {_fmt(test_higher)} (which is greater than {_fmt(x_int)}), the blue line (Provider A) lies below the amber line (Provider B).\n"
        f"Step 3: Stated recommendation [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="51",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The cheaper provider is represented by the line that lies lower (closer to the horizontal axis) at that usage level.",
        tier_2=f"Find x = {_fmt(test_higher)} on the horizontal axis and see which line has a lower y-value.",
        tier_3=f"At {_fmt(test_higher)} units, Provider A (blue line) is below Provider B, so Provider A is cheaper.",
        r=r,
        diagram_spec=diagram_spec,
    )


def _gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Multi-month / Annual scenario comparison between two providers."""
    name = r.choice(SA_NAMES)

    # Monthly usage profile across 12 months: low 6 months, high 6 months
    low_usage = r.choice([100, 120, 150])
    high_usage = r.choice([300, 350, 400])

    fixed_a = r.choice([200, 250, 300])
    rate_a = 1.50

    rate_b = 2.50  # Pure usage

    # 6 low months + 6 high months
    cost_a_monthly_low = fixed_a + low_usage * rate_a
    cost_a_monthly_high = fixed_a + high_usage * rate_a
    total_a = 6 * cost_a_monthly_low + 6 * cost_a_monthly_high

    cost_b_monthly_low = low_usage * rate_b
    cost_b_monthly_high = high_usage * rate_b
    total_b = 6 * cost_b_monthly_low + 6 * cost_b_monthly_high

    diff = abs(total_a - total_b)
    cheaper = "Option A" if total_a < total_b else "Option B"

    prompt = (
        f"{name} is calculating annual internet data costs for a family home:\n"
        f"• Option A: Fixed line rental of {_fmt_curr(fixed_a)} per month plus {_fmt_curr(rate_a)} per GB used.\n"
        f"• Option B: No fixed line rental, but {_fmt_curr(rate_b)} per GB used.\n"
        f"The family uses {_fmt(low_usage)} GB per month for 6 off-peak months and {_fmt(high_usage)} GB per month for 6 peak holiday months.\n"
        f"Which option is cheaper over the entire 12-month year, and by what total amount?"
    )

    correct_ans = f"{cheaper} is cheaper by {_fmt_curr(diff)}"
    other = "Option B" if cheaper == "Option A" else "Option A"
    wrong_1 = f"{other} is cheaper by {_fmt_curr(diff)}"
    wrong_2 = f"{cheaper} is cheaper by {_fmt_curr(diff + 500)}"
    wrong_3 = f"Both options cost the exact same amount over the year"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate annual cost for Option A [1 mark].\n"
        f"Low months cost = 6 × [{_fmt_curr(fixed_a)} + ({_fmt(low_usage)} × {_fmt_curr(rate_a)})] = 6 × {_fmt_curr(cost_a_monthly_low)} = {_fmt_curr(6 * cost_a_monthly_low)}.\n"
        f"High months cost = 6 × [{_fmt_curr(fixed_a)} + ({_fmt(high_usage)} × {_fmt_curr(rate_a)})] = 6 × {_fmt_curr(cost_a_monthly_high)} = {_fmt_curr(6 * cost_a_monthly_high)}.\n"
        f"Total Option A = {_fmt_curr(total_a)}.\n"
        f"Step 2: Calculate annual cost for Option B [1 mark].\n"
        f"Low months cost = 6 × ({_fmt(low_usage)} × {_fmt_curr(rate_b)}) = {_fmt_curr(6 * cost_b_monthly_low)}.\n"
        f"High months cost = 6 × ({_fmt(high_usage)} × {_fmt_curr(rate_b)}) = {_fmt_curr(6 * cost_b_monthly_high)}.\n"
        f"Total Option B = {_fmt_curr(total_b)}.\n"
        f"Step 3: Compare totals and difference [1 mark].\n"
        f"Difference = |{_fmt_curr(total_a)} - {_fmt_curr(total_b)}| = {_fmt_curr(diff)}.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="52",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the full 12-month total for both options and compare the sums.",
        tier_2=f"Option A total is {_fmt_curr(total_a)}; Option B total is {_fmt_curr(total_b)}.",
        tier_3=f"{cheaper} is cheaper by {_fmt_curr(diff)}: {correct_ans}.",
        r=r,
    )
