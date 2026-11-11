"""Cluster 4: Inverse Proportion Relationships (Subskills 28 to 36)."""
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

# --------------------------------------------------------------------------- #
# Subskill 28: Constant Product Rule Verification
# --------------------------------------------------------------------------- #
def _gen_pat_inv_constant_product_rule(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_constant_product_rule"
    name = r.choice(SA_NAMES)
    k = r.choice([60, 120, 240, 360])
    x1, y1 = 2, k // 2
    x2, y2 = 4, k // 4
    x3, y3 = 6, k // 6
    correct_ans = f"k = {k}"

    prompt = (
        f"{name} is testing whether two variables $x$ and $y$ are in inverse proportion:\n\n"
        f"| $x$ | {x1} | {x2} | {x3} |\n"
        f"| :---: | :---: | :---: | :---: |\n"
        f"| $y$ | {y1} | {y2} | {y3} |\n\n"
        f"Verify the relationship by calculating the **constant product** ($k = x \\times y$)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Two variables are inversely proportional if their product is constant for all corresponding pairs: $x \\times y = k$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$x_1 \\times y_1 = {x1} \\times {y1} = {k}$$\n"
        f"$$x_2 \\times y_2 = {x2} \\times {y2} = {k}$$\n"
        f"$$x_3 \\times y_3 = {x3} \\times {y3} = {k}$$ ✓ [1 Mark: Method – verifying constant product across all pairs]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$k = {k}$$ ✓ [1 Mark: Accuracy – accurate product constant]"
    )

    d1 = f"k = {k // 2}"
    d2 = f"k = {k * 2}"
    d3 = f"k = {y1 // x1}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In inverse proportion, multiply x by y: k = x × y.",
        tier_2=f"Calculate {x1} × {y1} = {k}.",
        tier_3=f"The constant product is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 29: Sharing Cash Prize Among Winners
# --------------------------------------------------------------------------- #
def _gen_pat_inv_sharing_cash_prize_among_winners(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_sharing_cash_prize_among_winners"
    name = r.choice(SA_NAMES)
    total_prize = r.choice([50000, 100000, 150000, 240000])
    winners = r.choice([4, 5, 8, 10, 12])
    payout = total_prize / winners
    correct_ans = _fmt_curr(payout)

    prompt = (
        f"{name} organizes a school fundraising lucky draw with a fixed total jackpot prize of {_fmt_curr(total_prize)}.\n"
        f"The jackpot must be shared equally among all winning ticket holders.\n\n"
        f"Calculate the payout per winner if there are **{winners} winning tickets**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Sharing a fixed total equally among $n$ people is an inverse proportion: $\\text{{Individual share}} = \\frac{{\\text{{Total Prize}}}}{{n}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Share per winner}} = \\frac{{{_fmt_curr(total_prize)}}}{{{winners}}}$$ ✓ [1 Mark: Method – dividing total prize by number of winners]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Share per winner}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency quotient]"
    )

    d1 = _fmt_curr(total_prize / (winners + 1))
    d2 = _fmt_curr(total_prize / (winners - 1)) if winners > 1 else _fmt_curr(total_prize * 2)
    d3 = _fmt_curr(payout * 1.5)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the total prize money by the number of winners.",
        tier_2=f"Calculate {_fmt_curr(total_prize)} ÷ {winners}.",
        tier_3=f"Payout per winner = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 30: Workers and Days to Complete Task
# --------------------------------------------------------------------------- #
def _gen_pat_inv_workers_and_days_to_complete_task(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_workers_and_days_to_complete_task"
    name = r.choice(SA_NAMES)
    w1 = r.choice([2, 3, 4])
    days1 = r.choice([12, 18, 24, 30])
    man_days = w1 * days1
    w2 = r.choice([6, 8, 9])
    # ensure clean division
    while man_days % w2 != 0:
        w2 = r.choice([6, 8, 9, 12])
        if man_days % w2 != 0:
            man_days = 72
            days1 = 72 // w1
    days2 = man_days // w2
    correct_ans = f"{days2} days"

    prompt = (
        f"{name} operates a joinery workshop. It takes {w1} carpenters a total of {days1} days to manufacture a batch of school desks.\n"
        f"All carpenters work at the exact same constant pace.\n\n"
        f"Calculate how many days it will take **{w2} carpenters** to complete the same batch of desks."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The number of workers and the days needed to finish a fixed job are inversely proportional: "
        f"$\\text{{Workers}}_1 \\times \\text{{Days}}_1 = \\text{{Workers}}_2 \\times \\text{{Days}}_2$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total carpenter-days required}} = {w1} \\times {days1} = {man_days}\\text{{ carpenter-days}}$$\n"
        f"$$\\text{{Days for {w2} carpenters}} = \\frac{{{man_days}}}{{{w2}}}$$ ✓ [1 Mark: Method – applying inverse proportion worker-day conservation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Days}} = {days2}\\text{{ days}}$$ ✓ [1 Mark: Accuracy – accurate integer division]"
    )

    d1 = f"{days2 + 2} days"
    d2 = f"{days2 - 1} days"
    d3 = f"{round((w2 / w1) * days1)} days"  # direct proportion error (more workers take more time)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="More workers mean the job takes FEWER days: Total man-days = w1 × days1.",
        tier_2=f"Total effort = {w1} × {days1} = {man_days} carpenter-days. Divide by {w2} workers.",
        tier_3=f"Days needed = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 31: Rectangle Dimensions with Fixed Area
# --------------------------------------------------------------------------- #
def _gen_pat_inv_rectangle_dimensions_fixed_area(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_rectangle_dimensions_fixed_area"
    name = r.choice(SA_NAMES)
    area = r.choice([24, 36, 48, 60, 72])
    length = r.choice([6, 8, 12])
    # ensure length divides area
    while area % length != 0:
        area = 48
    breadth = area // length
    correct_ans = f"{breadth} m"

    prompt = (
        f"{name} designs a vegetable garden that must have a fixed area of **{area} m²**.\n"
        f"If the length of the garden is set at {length} m, calculate the required breadth (width) of the garden.\n\n"
        f"**Formula**: $\\text{{Area}} = l \\times b \\implies b = \\frac{{\\text{{Area}}}}{{l}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"When area is fixed, length and breadth are inversely proportional: as length increases, breadth must decrease to maintain the same area.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$b = \\frac{{\\text{{Area}}}}{{l}} = \\frac{{{area}}}{{{length}}}$$ ✓ [1 Mark: Method – dividing fixed area by length]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$b = {breadth}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate breadth with units]"
    )

    d1 = f"{breadth + 2} m"
    d2 = f"{breadth - 1} m"
    d3 = f"{area - length} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Breadth = Area ÷ Length.",
        tier_2=f"Calculate {area} ÷ {length}.",
        tier_3=f"Breadth = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 32: Travel Speed and Time for Fixed Distance
# --------------------------------------------------------------------------- #
def _gen_pat_inv_travel_speed_and_time_fixed_distance(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_travel_speed_and_time_fixed_distance"
    name = r.choice(SA_NAMES)
    dist = r.choice([300, 360, 420, 480])  # km
    speed = r.choice([60, 80, 100, 120])
    time_hrs = round(dist / speed, 1)
    correct_ans = f"{_fmt(time_hrs)} hours"

    prompt = (
        f"{name} is traveling a fixed route of {dist} km between two cities.\n\n"
        f"Calculate the travel time if {name} drives at an average speed of {speed} km/h.\n\n"
        f"**Formula**: $\\text{{Time}} = \\frac{{\\text{{Distance}}}}{{\\text{{Speed}}}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"For a fixed journey distance, travel time is inversely proportional to speed: traveling faster reduces travel time.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Time}} = \\frac{{{dist}}}{{{speed}}}$$ ✓ [1 Mark: Method – dividing fixed distance by average speed]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Time}} = {_fmt(time_hrs)}\\text{{ hours}}$$ ✓ [1 Mark: Accuracy – accurate time with units]"
    )

    d1 = f"{_fmt(round(time_hrs + 1.0, 1))} hours"
    d2 = f"{_fmt(round(time_hrs - 0.5, 1))} hours"
    d3 = f"{_fmt(round(dist * speed / 1000, 1))} hours"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Time = Distance ÷ Speed.",
        tier_2=f"Calculate {dist} ÷ {speed}.",
        tier_3=f"Travel time = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 33: Pump Flow Rate & Tank Emptying Time
# --------------------------------------------------------------------------- #
def _gen_pat_inv_pump_flow_rate_and_tank_emptying_time(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_pump_flow_rate_and_tank_emptying_time"
    name = r.choice(SA_NAMES)
    vol = r.choice([12000, 15000, 18000, 24000])  # litres
    flow = r.choice([200, 250, 300, 400])  # litres/min
    mins = vol // flow
    correct_ans = f"{mins} minutes"

    prompt = (
        f"{name} uses a submersible pump to drain an irrigation reservoir holding {vol} litres of water.\n"
        f"The pump discharges water at a constant rate of {flow} litres per minute.\n\n"
        f"Calculate the time needed to drain the reservoir completely in minutes."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Emptying time is inversely proportional to pump flow rate: doubling the pumping rate halves the emptying time.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Time}} = \\frac{{\\text{{Total Volume}}}}{{\\text{{Discharge Rate}}}} = \\frac{{{vol}}}{{{flow}}}$$ ✓ [1 Mark: Method – dividing total volume by flow rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Time}} = {mins}\\text{{ minutes}}$$ ✓ [1 Mark: Accuracy – accurate quotient]"
    )

    d1 = f"{mins + 15} minutes"
    d2 = f"{mins - 10} minutes"
    d3 = f"{mins * 2} minutes"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Time = Volume ÷ Discharge rate.",
        tier_2=f"Calculate {vol} ÷ {flow}.",
        tier_3=f"Emptying time = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 34: Inverse Proportion Table Missing Value
# --------------------------------------------------------------------------- #
def _gen_pat_inv_table_missing_value_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_table_missing_value_calculation"
    name = r.choice(SA_NAMES)
    k = 120
    x1, y1 = 2, 60
    x2, y2 = 4, 30
    target_x = r.choice([5, 6, 8, 10])
    target_y = k // target_x
    correct_ans = f"{target_y}"

    prompt = (
        f"{name} is completing the following table of **inversely proportional** values where $x \\times y = {k}$:\n\n"
        f"| $x$ | {x1} | {x2} | **{target_x}** |\n"
        f"| :---: | :---: | :---: | :---: |\n"
        f"| $y$ | {y1} | {y2} | **M** |\n\n"
        f"Calculate the missing value **M** when $x = {target_x}$."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In an inverse proportion, the product $x \\times y = k$ is constant for every column.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$k = {x1} \\times {y1} = {k}$$\n"
        f"$$M = \\frac{{k}}{{{target_x}}} = \\frac{{{k}}}{{{target_x}}}$$ ✓ [1 Mark: Method – dividing constant product by target x]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$M = {target_y}$$ ✓ [1 Mark: Accuracy – accurate integer division]"
    )

    d1 = f"{target_y + 4}"
    d2 = f"{target_y - 2}"
    d3 = f"{k - target_x}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In inverse proportion, x × y = constant product k.",
        tier_2=f"Constant k = {k}. Calculate {k} ÷ {target_x}.",
        tier_3=f"Value M = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 35: Graph Characteristics and Shape of Inverse Proportion
# --------------------------------------------------------------------------- #
def _gen_pat_inv_graph_characteristics_and_shape(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_graph_characteristics_and_shape"
    k_val = r.choice([60, 100, 120, 240])
    correct_ans = "A smooth, downward-sloping curve (hyperbola) that approaches both axes but never touches or intersects them"

    prompt = (
        f"Refer to the inverse proportion graph below (xy = {k_val}).\n\n"
        f"Which statement accurately describes the shape and characteristics of an **Inverse Proportion** graph?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An inverse proportion has the equation y = k ÷ x.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"As x increases, y decreases asymptotically. The curve is a hyperbola that never touches x=0 or y=0. "
        f"✓ [1 Mark: Method – identifying hyperbolic asymptotic behavior]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct curve description]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Inverse Proportion (xy = {k_val})",
        "lines": [{"points": [[1, k_val], [2, k_val // 2], [4, k_val // 4], [5, k_val // 5]], "label": f"y = {k_val}/x"}],
    }

    custom = [
        correct_ans,
        "A straight line passing through the origin (0; 0)",
        "A vertical straight line parallel to the y-axis",
        "A series of discrete horizontal steps",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Does the product x × y equal a constant?",
        tier_2="As x gets bigger, y gets smaller, creating a smooth downward curve called a hyperbola.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} plots an inverse proportion relationship (such as $y = \\frac{{120}}{{x}}$ for $x > 0$).\n\n"
        f"Which of the following statements correctly describes the shape and appearance of an **inverse proportion graph**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In an inverse proportion $y = \\frac{{k}}{{x}}$, as $x$ increases, $y$ decreases rapidly at first and then flattens out.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Division by zero is undefined, so $x$ can never be 0 (the graph never touches the vertical y-axis).\n"
        f"Similarly, $y$ can never be 0 because $\\frac{{k}}{{x}} = 0$ has no real solution for positive $k$ "
        f"(the graph never touches the horizontal x-axis).\n"
        f"This creates a smooth downward-curving hyperbola. ✓ [1 Mark: Method – explaining asymptotic curve behaviour]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct graphical description]"
    )

    custom = [
        correct_ans,
        "A straight diagonal line that starts at the origin (0; 0) and slopes upwards",
        "A straight downward-sloping line that crosses both the x-axis and y-axis",
        "A horizontal straight line parallel to the x-axis",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall the graph of y = k/x.",
        tier_2="It is a curve that decreases and never touches the axes.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 36: Distinguish Direct vs Inverse Proportion
# --------------------------------------------------------------------------- #
def _gen_pat_inv_compare_direct_vs_inverse_proportion(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_compare_direct_vs_inverse_proportion"
    name = r.choice(SA_NAMES)
    is_direct = r.choice([True, False])

    if is_direct:
        context = "When buying apples, if the mass doubles, the total cost also doubles"
        correct_ans = "Direct proportion (y/x = constant)"
        reason = "both variables increase together at a constant ratio"
    else:
        context = "When painting a fence, if the number of painters doubles, the time needed is halved"
        correct_ans = "Inverse proportion (x × y = constant)"
        reason = "as one variable increases, the other decreases so their product is constant"

    prompt = (
        f"{name} is analyzing the following mathematical relationship:\n"
        f"\"**{context}**\"\n\n"
        f"Classify this relationship as either **direct proportion** or **inverse proportion**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"  • **Direct proportion**: As independent variable increases, dependent variable increases at a constant ratio ($y/x = k$).\n"
        f"  • **Inverse proportion**: As independent variable increases, dependent variable decreases proportionally ($xy = k$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"In this scenario, {reason}. ✓ [1 Mark: Method – matching proportional behaviour to definition]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct proportional classification]"
    )

    custom = [
        "Direct proportion (y/x = constant)",
        "Inverse proportion (x × y = constant)",
        "Exponential growth",
        "Quadratic relationship",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Do both variables increase together, or does one decrease as the other increases?",
        tier_2=f"{context}. This means {reason}.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )
