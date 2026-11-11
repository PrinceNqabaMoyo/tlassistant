"""Grade 9 Mathematics - Patterns Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/04. Patterns.md:
Inverse and direct proportion, constant products (xy = k), word problems (workers/days, speed/time),
hyperbolas, real-world linear financial models, geometric configurations, and error analysis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .patterns_svg import (
    draw_inverse_proportion_hyperbola_svg,
)


# ----------------------------------------------------------------------
# 26. Inverse Proportion: Constant Product Rule
# ----------------------------------------------------------------------
def arch_26_inverse_proportion_constant_product_rule(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([24, 36, 48, 60, 72])
    x1 = 2
    y1 = k // x1
    x2 = 6
    y2 = k // x2
    x_unknown = 4
    y_target = k // x_unknown

    prompt = (
        f"Two quantities \\(x\\) and \\(y\\) are inversely proportional, meaning their product "
        f"is constant (\\(x \\times y = k\\)).\n\n"
        f"When \\(x = {x1}\\), \\(y = {y1}\\), and when \\(x = {x2}\\), \\(y = {y2}\\).\n\n"
        f"1. Determine the constant of proportionality (\\(k\\)).\n"
        f"2. Calculate \\(y\\) when \\(x = {x_unknown}\\)."
    )
    sol = (
        f"**Inverse Proportion Product Rule:**\n"
        f"1. Constant product: \\(k = x \\times y = {x1} \\times {y1} = {k}\\).\n"
        f"2. For \\(x = {x_unknown}\\): \\(y = \\frac{{{k}}}{{{x_unknown}}} = {y_target}\\)."
    )
    return {
        "id": f"g9_pat_inv_product_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"k = {k}; y = {y_target}",
        "expected_answer": f"k = {k}; y = {y_target}",
        "sample_answer": f"k = {k}; y = {y_target}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate constant product k = {k}", "marks": 1},
            {"desc": f"Solve y = {k} / {x_unknown} = {y_target}", "marks": 1},
        ],
        "hints": [
            "In inverse proportion, x * y is always equal to the same number k.",
            f"Multiply {x1} * {y1} to find k.",
            f"Answers: k = {k} and y = {y_target}.",
        ],
    }


# ----------------------------------------------------------------------
# 27. Inverse Proportion: Workers and Days Problem
# ----------------------------------------------------------------------
def arch_27_inverse_proportion_workers_and_days_problem(rng: random.Random) -> Dict[str, Any]:
    w1 = 4
    d1 = rng.choice([9, 12, 15, 18])
    total_man_days = w1 * d1
    w2 = 6
    ans_days = total_man_days // w2

    prompt = (
        f"A team of \\({w1}\\) builders takes \\({d1}\\) days to complete paving a driveway. "
        f"Assuming all builders work at the same constant rate, how many days would it take "
        f"a team of \\({w2}\\) builders to complete the same job?"
    )
    sol = (
        f"**Man-days Inverse Proportion:**\n"
        f"Total work = \\({w1} \\times {d1} = {total_man_days}\\text{{ worker-days}}\\).\n"
        f"With \\({w2}\\) workers:\n"
        f"\\[ \\text{{Time}} = \\frac{{{total_man_days}}}{{{w2}}} = {ans_days}\\text{{ days}} \\]"
    )
    return {
        "id": f"g9_pat_inv_workers_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ans_days} days",
        "expected_answer": f"{ans_days} days",
        "sample_answer": f"{ans_days} days",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate total work = {total_man_days} worker-days", "marks": 1},
            {"desc": f"Divide by {w2} to get {ans_days} days", "marks": 1},
        ],
        "hints": [
            "More workers take fewer days: this is inverse proportion.",
            f"Total work = {w1} * {d1}.",
            f"Divide by {w2} to find the time: {ans_days} days.",
        ],
    }


# ----------------------------------------------------------------------
# 28. Inverse Proportion: Speed and Travel Time Problem
# ----------------------------------------------------------------------
def arch_28_inverse_proportion_speed_and_travel_time_problem(rng: random.Random) -> Dict[str, Any]:
    # Distance = speed * time
    s1 = 120
    t1 = rng.choice([2, 3, 4])
    dist = s1 * t1
    s2 = rng.choice([60, 80, 90])
    ans_t = dist / s2
    ans_t_str = f"{ans_t:.1f}".rstrip("0").rstrip(".").replace(".", ",")

    prompt = (
        f"A motorist travels between two cities at an average speed of \\({s1}\\text{{ km/h}}\\) "
        f"and the journey takes \\({t1}\\text{{ hours}}\\).\n\n"
        f"How long would the same trip take if the driver traveled at an average speed of "
        f"\\({s2}\\text{{ km/h}}\\)? Express your answer in hours."
    )
    sol = (
        f"**Speed-Time Inverse Proportion:**\n"
        f"Distance: \\(D = {s1} \\times {t1} = {dist}\\text{{ km}}\\).\n"
        f"Time at \\({s2}\\text{{ km/h}}\\):\n"
        f"\\[ T = \\frac{{{dist}}}{{{s2}}} = {ans_t_str}\\text{{ hours}} \\]"
    )
    return {
        "id": f"g9_pat_inv_speed_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ans_t_str} hours",
        "expected_answer": f"{ans_t_str} hours",
        "sample_answer": f"{ans_t_str} hours",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate distance = {dist} km", "marks": 1},
            {"desc": f"Compute time at {s2} km/h: {ans_t_str} hours", "marks": 1},
        ],
        "hints": [
            "Distance = Speed * Time.",
            f"Distance is {dist} km.",
            f"Divide by {s2} km/h to find hours: {ans_t_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Inverse Proportion: Graphical Hyperbola Interpretation
# ----------------------------------------------------------------------
def arch_29_inverse_proportion_graphical_hyperbola_interpretation(rng: random.Random) -> Dict[str, Any]:
    k = 24
    svg = draw_inverse_proportion_hyperbola_svg(k=k, seed=rng.randint(1, 9999))
    test_x = rng.choice([3, 4, 6])
    ans_y = k // test_x

    prompt = (
        f"Consider the inverse proportion curve \\(y = \\frac{{24}}{{x}}\\) displayed in the coordinate axes below.\n\n"
        f"Use the relationship to determine the value of \\(y\\) when \\(x = {test_x}\\)."
    )
    sol = (
        f"**Reading and Calculating Hyperbola Point:**\n"
        f"Substitute \\(x = {test_x}\\) into \\(y = \\frac{{24}}{{x}}\\):\n"
        f"\\[ y = \\frac{{24}}{{{test_x}}} = {ans_y} \\]"
    )
    return {
        "id": f"g9_pat_inv_hyperbola_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans_y),
        "expected_answer": str(ans_y),
        "sample_answer": str(ans_y),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": f"Substitute x = {test_x} into y = 24/x", "marks": 1},
            {"desc": f"State exact coordinate y = {ans_y}", "marks": 1},
        ],
        "hints": [
            f"Divide 24 by {test_x}.",
            f"Coordinate is y = {ans_y}.",
        ],
    }


# ----------------------------------------------------------------------
# 30. Direct Proportion: Constant Ratio Unit Rate
# ----------------------------------------------------------------------
def arch_30_direct_proportion_constant_ratio_unit_rate(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([15, 18, 22, 25])
    x1 = 3
    y1 = rate * x1
    x_target = 7
    y_target = rate * x_target

    prompt = (
        f"The cost of fruit is directly proportional to its mass (\\(y = kx\\)).\n\n"
        f"If \\({x1}\\text{{ kg}}\\) of fruit costs \\(\\text{{R}}{y1}\\):\n"
        f"1. Determine the constant unit rate \\(k\\) (cost per kg).\n"
        f"2. Calculate the cost of \\({x_target}\\text{{ kg}}\\) of fruit."
    )
    sol = (
        f"**Direct Proportion:**\n"
        f"1. Unit rate: \\(k = \\frac{{y}}{{x}} = \\frac{{{y1}}}{{{x1}}} = \\text{{R}}{rate}/\\text{{kg}}\\).\n"
        f"2. Cost for \\({x_target}\\text{{ kg}}\\): \\({x_target} \\times {rate} = \\text{{R}}{y_target}\\)."
    )
    return {
        "id": f"g9_pat_dir_prop_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"k = R{rate}/kg; R{y_target}",
        "expected_answer": f"k = R{rate}/kg; R{y_target}",
        "sample_answer": f"k = R{rate}/kg; R{y_target}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate unit rate k = R{rate}/kg", "marks": 1},
            {"desc": f"Calculate total cost R{y_target}", "marks": 1},
        ],
        "hints": [
            f"Divide {y1} by {x1} to find the price per 1 kg.",
            f"Multiply the unit rate by {x_target}.",
            f"Answers: R{rate}/kg and R{y_target}.",
        ],
    }


# ----------------------------------------------------------------------
# 31. Distinguish Direct vs Inverse Proportion from Given Pairs
# ----------------------------------------------------------------------
def arch_31_distinguish_direct_vs_inverse_proportion_from_tables(rng: random.Random) -> Dict[str, Any]:
    is_direct = rng.choice([True, False])
    if is_direct:
        k = rng.choice([4, 5, 6])
        pairs = [(1, k), (2, 2*k), (3, 3*k), (4, 4*k)]
        prop_type = "Direct Proportion"
        reason = f"y / x is constant ({k})"
    else:
        k = 48
        pairs = [(1, 48), (2, 24), (3, 16), (4, 12)]
        prop_type = "Inverse Proportion"
        reason = f"x * y is constant ({k})"

    pairs_str = ", ".join(f"({x}; {y})" for x, y in pairs)

    prompt = (
        f"Consider the following set of related \\((x; y)\\) data pairs:\n\n"
        f"\\[ {pairs_str} \\]\n\n"
        f"State whether this represents **Direct Proportion** or **Inverse Proportion**, "
        f"and justify your answer mathematically."
    )
    sol = (
        f"**Proportionality Test:**\n"
        f"Notice that {reason}.\n"
        f"Therefore, the relationship is **{prop_type}**."
    )
    return {
        "id": f"g9_pat_distinguish_prop_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{prop_type} ({reason})",
        "expected_answer": f"{prop_type} ({reason})",
        "sample_answer": f"{prop_type} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correctly identify {prop_type}", "marks": 1},
            {"desc": f"Provide valid mathematical reason ({reason})", "marks": 1},
        ],
        "hints": [
            "Check if y/x is constant (direct) or if x*y is constant (inverse).",
            f"The answer is {prop_type}.",
        ],
    }


# ----------------------------------------------------------------------
# 32. Contextual Cellphone Plan Cost Pattern
# ----------------------------------------------------------------------
def arch_32_contextual_cellphone_plan_cost_pattern(rng: random.Random) -> Dict[str, Any]:
    fixed = rng.choice([99, 149, 199])
    rate = round(rng.choice([1.20, 1.50, 1.75]), 2)
    mins = rng.choice([40, 60, 100])
    cost = round(fixed + mins * rate, 2)

    rate_str = f"{rate:.2f}".replace(".", ",")
    cost_str = f"\\text{{R}}{cost:.2f}".replace(".", ",")

    prompt = (
        f"A cellphone contract costs \\(\\text{{R}}{fixed}\\) monthly subscription plus "
        f"\\(\\text{{R}}{rate_str}\\) per minute of calling.\n\n"
        f"1. Write down an algebraic formula for the total monthly cost \\(C\\) for \\(m\\) minutes.\n"
        f"2. Calculate the monthly bill if a user makes \\({mins}\\) minutes of calls."
    )
    rule = f"C = {rate_str}m + {fixed}"
    sol = (
        f"**Linear Cost Model:**\n"
        f"1. Formula: \\({rule}\\).\n"
        f"2. For \\(m = {mins}\\): \\(C = {rate_str}({mins}) + {fixed} = {mins * rate:.2f} + {fixed} = {cost_str}\\)."
    )
    return {
        "id": f"g9_pat_cell_cost_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{rule}; {cost_str}",
        "expected_answer": f"{rule}; {cost_str}",
        "sample_answer": f"{rule}; {cost_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula C = {rate_str}m + {fixed}", "marks": 1},
            {"desc": f"Evaluate bill for {mins} minutes: {cost_str}", "marks": 1},
        ],
        "hints": [
            "Total Cost = (rate * minutes) + fixed subscription.",
            f"Formula: C = {rate_str}m + {fixed}.",
            f"Bill: {cost_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 33. Contextual Taxi Fare Linear Pattern
# ----------------------------------------------------------------------
def arch_33_contextual_taxi_fare_linear_pattern(rng: random.Random) -> Dict[str, Any]:
    base_fee = rng.choice([20, 25, 30])
    per_km = rng.choice([12, 14, 15])
    km = rng.choice([8, 12, 15, 20])
    fare = base_fee + per_km * km

    prompt = (
        f"A metered taxi charges a flat booking fee of \\(\\text{{R}}{base_fee}\\) plus "
        f"\\(\\text{{R}}{per_km}\\) for each kilometre travelled.\n\n"
        f"1. Formulate the equation for total fare \\(F\\) in terms of distance \\(d\\) (in km).\n"
        f"2. Calculate the fare for a journey of \\({km}\\text{{ km}}\\)."
    )
    rule = f"F = {per_km}d + {base_fee}"
    sol = (
        f"**Taxi Fare Model:**\n"
        f"1. Equation: \\({rule}\\).\n"
        f"2. For \\(d = {km}\\): \\(F = {per_km}({km}) + {base_fee} = {per_km * km} + {base_fee} = \\text{{R}}{fare}\\)."
    )
    return {
        "id": f"g9_pat_taxi_fare_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{rule}; R{fare}",
        "expected_answer": f"{rule}; R{fare}",
        "sample_answer": f"{rule}; R{fare}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State equation F = {per_km}d + {base_fee}", "marks": 1},
            {"desc": f"Evaluate fare = R{fare}", "marks": 1},
        ],
        "hints": [
            "Fare = (cost per km * distance) + base fee.",
            f"Multiply {per_km} by {km} and add {base_fee}.",
            f"Fare: R{fare}.",
        ],
    }


# ----------------------------------------------------------------------
# 34. Contextual Savings Plan Arithmetic Growth
# ----------------------------------------------------------------------
def arch_34_contextual_savings_plan_arithmetic_growth(rng: random.Random) -> Dict[str, Any]:
    init = rng.choice([200, 350, 500])
    monthly = rng.choice([150, 200, 250])
    months = 12
    tot = init + monthly * months

    prompt = (
        f"Lerato starts a savings account with an initial deposit of \\(\\text{{R}}{init}\\) "
        f"and adds \\(\\text{{R}}{monthly}\\) at the end of each month.\n\n"
        f"1. Write a general formula for the balance \\(S_n\\) after \\(n\\) months.\n"
        f"2. What will be the accumulated balance at the end of \\(1\\) year (\\(12\\) months)?"
    )
    rule = f"S_n = {monthly}n + {init}"
    sol = (
        f"**Savings Arithmetic Sequence:**\n"
        f"1. Formula: \\({rule}\\).\n"
        f"2. After 12 months: \\(S_{{12}} = {monthly}(12) + {init} = {monthly * 12} + {init} = \\text{{R}}{tot}\\)."
    )
    return {
        "id": f"g9_pat_savings_growth_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{rule}; R{tot}",
        "expected_answer": f"{rule}; R{tot}",
        "sample_answer": f"{rule}; R{tot}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula S_n = {monthly}n + {init}", "marks": 1},
            {"desc": f"Calculate 12-month balance R{tot}", "marks": 1},
        ],
        "hints": [
            f"Balance = {monthly} * months + {init}.",
            f"Substitute n = 12.",
            f"Total: R{tot}.",
        ],
    }


# ----------------------------------------------------------------------
# 35. Contextual Water Tank Depletion Linear Decay
# ----------------------------------------------------------------------
def arch_35_contextual_water_tank_depletion_linear_decay(rng: random.Random) -> Dict[str, Any]:
    full_vol = rng.choice([1000, 1500, 2000])
    rate = rng.choice([25, 40, 50])
    t_min = rng.choice([10, 15, 20])
    rem = full_vol - rate * t_min

    prompt = (
        f"A rainwater tank holds \\({full_vol}\\text{{ L}}\\) when full. It drains through a tap "
        f"at a constant rate of \\({rate}\\text{{ L/min}}\\) for irrigation.\n\n"
        f"1. Write down an equation for the remaining water volume \\(V\\) after \\(t\\) minutes.\n"
        f"2. Calculate the volume remaining after \\({t_min}\\) minutes."
    )
    rule = f"V = {full_vol} - {rate}t"
    sol = (
        f"**Decay Equation:**\n"
        f"1. Equation: \\({rule}\\).\n"
        f"2. For \\(t = {t_min}\\): \\(V = {full_vol} - {rate}({t_min}) = {full_vol} - {rate * t_min} = {rem}\\text{{ L}}\\)."
    )
    return {
        "id": f"g9_pat_water_decay_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{rule}; {rem} L",
        "expected_answer": f"{rule}; {rem} L",
        "sample_answer": f"{rule}; {rem} L",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State equation V = {full_vol} - {rate}t", "marks": 1},
            {"desc": f"Calculate remaining volume {rem} L", "marks": 1},
        ],
        "hints": [
            f"Subtract ({rate} * time) from {full_vol}.",
            f"Remaining volume after {t_min} min is {rem} L.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Linear Graph Story: Matching Distance-Time
# ----------------------------------------------------------------------
def arch_36_linear_graph_story_matching_distance_time(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([60, 80, 100])
    stop_mins = rng.choice([15, 20, 30])
    d1 = speed  # in 1 hour

    prompt = (
        f"A distance-time journey has three stages:\n"
        f"- Stage A: Driving at a steady \\({speed}\\text{{ km/h}}\\) for 1 hour.\n"
        f"- Stage B: Stopping at a petrol station for \\({stop_mins}\\) minutes.\n"
        f"- Stage C: Continuing at a steady speed for another hour.\n\n"
        f"Describe what the gradient (slope) of the line represents in Stage B."
    )
    ans = "Zero gradient (horizontal flat line), representing zero speed while stopped"
    sol = (
        f"**Distance-Time Gradient Interpretation:**\n"
        f"In Stage B, time passes while distance from the origin remains unchanged.\n"
        f"Therefore, the slope is **zero (horizontal line)**, indicating speed is \\(0\\text{{ km/h}}\\)."
    )
    return {
        "id": f"g9_pat_graph_story_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify zero gradient / flat horizontal line", "marks": 1},
            {"desc": "State that speed is zero while stationary", "marks": 1},
        ],
        "hints": [
            "On a distance-time plot, horizontal means stationary (no movement).",
            "The slope is 0.",
        ],
    }


# ----------------------------------------------------------------------
# 37. Linear Pattern: Is Number a Member of Sequence
# ----------------------------------------------------------------------
def arch_37_linear_pattern_is_number_a_member_of_sequence(rng: random.Random) -> Dict[str, Any]:
    d = 6
    c = -1
    # Tn = 6n - 1: terms end in: 5, 11, 17, 23, 29, 35...
    # (val + 1) % 6 == 0
    is_member = rng.choice([True, False])
    if is_member:
        n = rng.choice([35, 42, 51])
        val = 6 * n - 1
        verdict = f"Yes, it is the {n}th term"
    else:
        val = 6 * 40 + 2  # leaves remainder
        verdict = "No, n is not a natural number"

    prompt = (
        f"A sequence is defined by the rule \\(T_n = 6n - 1\\).\n\n"
        f"Determine mathematically whether the number **{val}** is a member of this sequence."
    )
    sol = (
        f"**Membership Test:**\n"
        f"Set \\(6n - 1 = {val} \\implies 6n = {val + 1}\\).\n"
        f"\\(n = \\frac{{{val + 1}}}{{6}} = {(val + 1) / 6:.2f}\\).\n"
        f"Verdict: {verdict}."
    )
    return {
        "id": f"g9_pat_member_test_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": verdict,
        "expected_answer": verdict,
        "sample_answer": verdict,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Solve 6n - 1 = {val}", "marks": 1},
            {"desc": f"State conclusion: {verdict}", "marks": 1},
        ],
        "hints": [
            f"Add 1 to {val} and divide by 6.",
            "If n is a whole counting number, it belongs to the sequence.",
            f"Conclusion: {verdict}.",
        ],
    }


# ----------------------------------------------------------------------
# 38. Two Sequences: Find Common Term and Position
# ----------------------------------------------------------------------
def arch_38_two_sequences_find_common_term_and_position(rng: random.Random) -> Dict[str, Any]:
    # Sequence A: 3n + 10
    # Sequence B: 5n - 4
    # 5n - 4 = 3n + 10 => 2n = 14 => n = 7
    # Common term = 3(7) + 10 = 31
    n_common = rng.choice([5, 6, 7, 8])
    c_a = 10
    # 5n - c_b = 3n + c_a => 2n = c_a + c_b => c_b = 2n - c_a
    c_b = 2 * n_common - c_a

    ans_val = 3 * n_common + c_a
    sign_b = f"- {abs(c_b)}" if c_b < 0 else f"+ {c_b}"

    prompt = (
        f"Two patterns have general terms \\(A_n = 3n + {c_a}\\) and \\(B_n = 5n {sign_b}\\).\n\n"
        f"1. At what position \\(n\\) do both patterns have the exact same term value?\n"
        f"2. What is the shared term value?"
    )
    sol = (
        f"**Equating Sequences:**\n"
        f"\\[ 5n {sign_b} = 3n + {c_a} \\]\n"
        f"\\[ 2n = {c_a - c_b} \\implies n = {n_common} \\]\n"
        f"Shared value: \\(A_{{{n_common}}} = 3({n_common}) + {c_a} = {ans_val}\\)."
    )
    return {
        "id": f"g9_pat_two_seq_common_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"n = {n_common}; Value = {ans_val}",
        "expected_answer": f"n = {n_common}; Value = {ans_val}",
        "sample_answer": f"n = {n_common}; Value = {ans_val}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Equate formulas and solve n = {n_common}", "marks": 1},
            {"desc": f"Evaluate shared term value {ans_val}", "marks": 1},
        ],
        "hints": [
            "Set the two formulas equal to each other.",
            "Solve for n.",
            f"Answers: n = {n_common} and value = {ans_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 39. Sequence with Alternating Addition and Subtraction
# ----------------------------------------------------------------------
def arch_39_sequence_with_alternating_addition_and_subtraction(rng: random.Random) -> Dict[str, Any]:
    # e.g., +5, -2: 10, 15, 13, 18, 16, 21, 19...
    start = rng.choice([10, 15, 20])
    add_s = 5
    sub_s = 2
    terms = [start]
    for _ in range(3):
        terms.append(terms[-1] + add_s)
        terms.append(terms[-1] - sub_s)

    shown = terms[:5]
    next_two = terms[5:7]
    shown_str = "; ".join(str(x) for x in shown)
    ans = f"{next_two[0]}; {next_two[1]}"

    prompt = (
        f"Identify the two alternating operations in the sequence and write down the next two numbers:\n\n"
        f"\\[ {shown_str};\\ \\dots;\\ \\dots \\]"
    )
    sol = (
        f"**Alternating Steps:**\n"
        f"Operations alternate between \\(+{add_s}\\) and \\(-{sub_s}\\).\n"
        f"Next term 1: \\({shown[4]} + {add_s} = {next_two[0]}\\).\n"
        f"Next term 2: \\({next_two[0]} - {sub_s} = {next_two[1]}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_pat_alt_ops_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify pattern (+{add_s}, -{sub_s})", "marks": 1},
            {"desc": f"State next two terms {ans}", "marks": 1},
        ],
        "hints": [
            f"Check the difference between consecutive numbers: +{add_s} then -{sub_s}.",
            f"Next terms: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 40. Sequence of Fractions: Linear Numerator and Denominator
# ----------------------------------------------------------------------
def arch_40_sequence_fractions_linear_numerator_and_denominator(rng: random.Random) -> Dict[str, Any]:
    # e.g., 2/3, 4/5, 6/7, 8/9... Tn = 2n / (2n + 1)
    ans = "\\frac{2n}{2n + 1}"
    t10 = "\\frac{20}{21}"

    prompt = (
        f"Consider the sequence of fractions:\n\n"
        f"\\[ \\frac{{2}}{{3}};\\ \\frac{{4}}{{5}};\\ \\frac{{6}}{{7}};\\ \\frac{{8}}{{9}};\\ \\dots \\]\n\n"
        f"1. Determine the general term formula \\(T_n\\).\n"
        f"2. Calculate the 10th term (\\(T_{{10}}\\))."
    )
    sol = (
        f"**Fraction Sequence Analysis:**\n"
        f"1. Numerators: \\(2;\\ 4;\\ 6;\\ 8 \\implies 2n\\).\n"
        f"2. Denominators: \\(3;\\ 5;\\ 7;\\ 9 \\implies 2n + 1\\).\n"
        f"General formula: \\(T_n = {ans}\\).\n"
        f"For \\(n = 10\\): \\(T_{{10}} = {t10}\\)."
    )
    return {
        "id": f"g9_pat_frac_lin_rule_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_n = {ans}; T_10 = {t10}",
        "expected_answer": f"T_n = {ans}; T_10 = {t10}",
        "sample_answer": f"T_n = {ans}; T_10 = {t10}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula T_n = {ans}", "marks": 1},
            {"desc": f"Calculate T_10 = {t10}", "marks": 1},
        ],
        "hints": [
            "Find the rule for the top and bottom separately.",
            "Top is 2n, bottom is 2n + 1.",
            f"Results: {ans} and {t10}.",
        ],
    }


# ----------------------------------------------------------------------
# 41. Nested Bracket Pattern Expansion
# ----------------------------------------------------------------------
def arch_41_nested_bracket_pattern_expansion(rng: random.Random) -> Dict[str, Any]:
    # Tn = n(n + 1): 2, 6, 12, 20, 30... (pronic numbers)
    target_n = rng.choice([8, 10, 12])
    ans = target_n * (target_n + 1)

    prompt = (
        f"The pronic number pattern follows the formula \\(T_n = n(n + 1)\\):\n\n"
        f"\\[ 2;\\ 6;\\ 12;\\ 20;\\ 30;\\ \\dots \\]\n\n"
        f"Calculate the **{target_n}th** term (\\(T_{{{target_n}}}\\))."
    )
    sol = (
        f"**Evaluating \\(T_n = n(n + 1)\\):**\n"
        f"\\[ T_{{{target_n}}} = {target_n}({target_n} + 1) = {target_n} \\times {target_n + 1} = {ans} \\]"
    )
    return {
        "id": f"g9_pat_pronic_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Calculate {target_n} * {target_n+1} = {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply {target_n} by {target_n + 1}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 42. Geometric Pattern: Hexagonal Perimeter Growth
# ----------------------------------------------------------------------
def arch_42_geometric_pattern_hexagonal_perimeter_growth(rng: random.Random) -> Dict[str, Any]:
    # Linked regular hexagons: 1 hex has 6 sides; 2 hexes share 1 side -> 10 outer sides; 3 hexes share 2 -> 14 outer sides
    # Pn = 4n + 2
    ans = "4n + 2"
    n_hex = rng.choice([15, 20, 25])
    ans_p = 4 * n_hex + 2

    prompt = (
        f"Regular hexagons of side length \\(1\\text{{ cm}}\\) are joined in a line along shared edges.\n\n"
        f"A single hexagon has perimeter \\(6\\text{{ cm}}\\), two linked hexagons have perimeter \\(10\\text{{ cm}}\\), "
        f"and three linked hexagons have perimeter \\(14\\text{{ cm}}\\).\n\n"
        f"1. Write down the general formula \\(P_n\\) for the perimeter of a row of \\(n\\) hexagons.\n"
        f"2. Calculate the perimeter of a row of \\({n_hex}\\) linked hexagons."
    )
    sol = (
        f"**Hexagonal Ring Perimeter:**\n"
        f"Terms: \\(6;\\ 10;\\ 14;\\ \\dots\\)\n"
        f"1. Common difference: \\(d = 10 - 6 = 4\\).\n"
        f"2. Constant: \\(c = 6 - 4 = 2\\).\n"
        f"Formula: \\(P_n = {ans}\\).\n"
        f"For \\(n = {n_hex}\\): \\(P_{{{n_hex}}} = 4({n_hex}) + 2 = {ans_p}\\text{{ cm}}\\)."
    )
    return {
        "id": f"g9_pat_hex_perim_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"P_n = {ans}; P_{n_hex} = {ans_p} cm",
        "expected_answer": f"P_n = {ans}; P_{n_hex} = {ans_p} cm",
        "sample_answer": f"P_n = {ans}; P_{n_hex} = {ans_p} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Derive formula P_n = {ans}", "marks": 1},
            {"desc": f"Compute perimeter {ans_p} cm", "marks": 1},
        ],
        "hints": [
            "Each additional hexagon adds 4 exposed outer sides.",
            f"Formula: Pn = {ans}.",
            f"Perimeter: {ans_p} cm.",
        ],
    }


# ----------------------------------------------------------------------
# 43. Geometric Pattern: Dot Grid Growth
# ----------------------------------------------------------------------
def arch_43_geometric_pattern_dot_grid_growth(rng: random.Random) -> Dict[str, Any]:
    # A rectangular dot array has n rows and (n + 2) columns:
    # D_n = n(n + 2)
    stage_k = rng.choice([5, 6, 7, 8])
    ans = stage_k * (stage_k + 2)

    prompt = (
        f"A series of rectangular dot patterns has \\(n\\) rows and \\(n + 2\\) columns at Stage \\(n\\).\n\n"
        f"1. State the formula for the total number of dots \\(D_n\\).\n"
        f"2. Calculate the total dots at Stage {stage_k}."
    )
    sol = (
        f"**Dot Array Growth:**\n"
        f"1. Total dots: \\(D_n = n(n + 2)\\).\n"
        f"2. For \\(n = {stage_k}\\): \\(D_{{{stage_k}}} = {stage_k}({stage_k + 2}) = {ans}\\)."
    )
    return {
        "id": f"g9_pat_dot_grid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"D_n = n(n + 2); D_{stage_k} = {ans}",
        "expected_answer": f"D_n = n(n + 2); D_{stage_k} = {ans}",
        "sample_answer": f"D_n = n(n + 2); D_{stage_k} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State formula D_n = n(n + 2)", "marks": 1},
            {"desc": f"Calculate {stage_k} * {stage_k+2} = {ans}", "marks": 1},
        ],
        "hints": [
            "Total dots = rows * columns.",
            f"Multiply {stage_k} by {stage_k + 2}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 44. Contextual Tiered Staircase Block Pattern
# ----------------------------------------------------------------------
def arch_44_contextual_tiered_staircase_block_pattern(rng: random.Random) -> Dict[str, Any]:
    # Staircase of n steps has total blocks 1 + 2 + ... + n = n(n+1)/2
    n_steps = rng.choice([15, 20, 25])
    ans = (n_steps * (n_steps + 1)) // 2

    prompt = (
        f"A brick staircase has 1 block in the first step, 2 blocks in the second, and continues adding "
        f"one block per step (total blocks = \\(1 + 2 + 3 + \\dots + n\\)).\n\n"
        f"Using the summation formula \\(S_n = \\frac{{n(n+1)}}{{2}}\\), calculate the total number "
        f"of blocks needed to build a staircase with **{n_steps}** steps."
    )
    sol = (
        f"**Staircase Summation:**\n"
        f"\\[ S_{{{n_steps}}} = \\frac{{{n_steps}({n_steps} + 1)}}{{2}} = \\frac{{{n_steps} \\times {n_steps + 1}}}{{2}} = {ans} \\]"
    )
    return {
        "id": f"g9_pat_staircase_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Apply sum formula for n = {n_steps}", "marks": 1},
            {"desc": f"Calculate total blocks {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply {n_steps} by {n_steps + 1}.",
            "Divide by 2.",
            f"Total blocks: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 45. Seating Arrangement: Tables and Chairs
# ----------------------------------------------------------------------
def arch_45_seating_arrangement_tables_and_chairs(rng: random.Random) -> Dict[str, Any]:
    # 1 table seats 4; 2 tables pushed together seat 6; 3 tables seat 8 -> 2n + 2
    ans = "2n + 2"
    t_tables = rng.choice([18, 24, 30])
    ans_seats = 2 * t_tables + 2

    prompt = (
        f"Square tables are pushed together in a single long row for a banquet.\n\n"
        f"- 1 table seats 4 guests.\n"
        f"- 2 tables pushed together seat 6 guests.\n"
        f"- 3 tables pushed together seat 8 guests.\n\n"
        f"1. Write the general rule for the number of seats \\(S_n\\) in terms of the number of tables \\(n\\).\n"
        f"2. How many guests can be seated if **{t_tables}** tables are joined in a row?"
    )
    sol = (
        f"**Seating Formula:**\n"
        f"1. Each table adds 2 seats along the sides, plus 2 seats at the two ends:\n"
        f"   \\(S_n = {ans}\\).\n"
        f"2. For \\(n = {t_tables}\\): \\(S_{{{t_tables}}} = 2({t_tables}) + 2 = {ans_seats}\\)."
    )
    return {
        "id": f"g9_pat_seating_tables_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"S_n = {ans}; S_{t_tables} = {ans_seats}",
        "expected_answer": f"S_n = {ans}; S_{t_tables} = {ans_seats}",
        "sample_answer": f"S_n = {ans}; S_{t_tables} = {ans_seats}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Derive formula S_n = {ans}", "marks": 1},
            {"desc": f"Calculate {ans_seats} seats for {t_tables} tables", "marks": 1},
        ],
        "hints": [
            "Each table adds 2 side seats, plus 2 end seats.",
            f"Formula: Sn = {ans}.",
            f"Guests: {ans_seats}.",
        ],
    }


# ----------------------------------------------------------------------
# 46. Fence Posts and Planks Pattern
# ----------------------------------------------------------------------
def arch_46_fence_posts_and_planks_pattern(rng: random.Random) -> Dict[str, Any]:
    # n fence sections require n + 1 posts and 3n rails
    sections = rng.choice([15, 20, 25])
    posts = sections + 1
    rails = 3 * sections

    prompt = (
        f"A straight garden fence has \\(n\\) sections. Each section requires \\(3\\) horizontal rails, "
        f"and vertical posts are placed between sections with one extra post at the start.\n\n"
        f"For a fence with **{sections}** sections:\n"
        f"1. How many vertical posts are required?\n"
        f"2. How many horizontal rails are required?"
    )
    sol = (
        f"**Fence Post Formulae:**\n"
        f"1. Posts: \\(n + 1 = {sections} + 1 = {posts}\\).\n"
        f"2. Rails: \\(3n = 3({sections}) = {rails}\\)."
    )
    return {
        "id": f"g9_pat_fence_posts_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Posts = {posts}; Rails = {rails}",
        "expected_answer": f"Posts = {posts}; Rails = {rails}",
        "sample_answer": f"Posts = {posts}; Rails = {rails}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate posts = {posts}", "marks": 1},
            {"desc": f"Calculate rails = {rails}", "marks": 1},
        ],
        "hints": [
            "Posts = sections + 1.",
            "Rails = 3 * sections.",
            f"Answers: {posts} posts and {rails} rails.",
        ],
    }


# ----------------------------------------------------------------------
# 47. Error Analysis: Diagnosing Difference vs Coefficient Confusion
# ----------------------------------------------------------------------
def arch_47_error_analysis_diagnosing_difference_vs_coefficient_confusion(rng: random.Random) -> Dict[str, Any]:
    # Sequence: 4, 9, 14, 19... d = 5. Flawed rule: Tn = n + 5 instead of 5n - 1
    d = 5
    t1 = 4
    c = t1 - d  # -1
    correct_rule = f"{d}n - {abs(c)}"

    prompt = (
        f"A learner is given the sequence \\(4;\\ 9;\\ 14;\\ 19;\\ \\dots\\) and notices the common difference is \\(5\\).\n\n"
        f"The learner writes down the general formula as \\(T_n = n + 5\\).\n\n"
        f"1. Show that the learner's formula is incorrect by testing \\(n = 2\\).\n"
        f"2. Provide the correct general formula \\(T_n\\)."
    )
    sol = (
        f"**Error Analysis:**\n"
        f"1. Test \\(n = 2\\): \\(T_2 = 2 + 5 = 7 \\neq 9\\). The learner confused the coefficient of \\(n\\) with an added constant.\n"
        f"2. Correct formula: Common difference \\(d = 5\\) must multiply \\(n\\): \\(T_n = {correct_rule}\\)."
    )
    return {
        "id": f"g9_pat_err_diff_coeff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_2 = 7 != 9; Correct: T_n = {correct_rule}",
        "expected_answer": f"T_2 = 7 != 9; Correct: T_n = {correct_rule}",
        "sample_answer": f"T_2 = 7 != 9; Correct: T_n = {correct_rule}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Demonstrate test failure at n = 2", "marks": 1},
            {"desc": f"Provide correct rule T_n = {correct_rule}", "marks": 1},
        ],
        "hints": [
            "The common difference must be multiplied by n: Tn = dn + c.",
            f"Correct formula is Tn = {correct_rule}.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Error Analysis: Diagnosing Zeroth Term Omission
# ----------------------------------------------------------------------
def arch_48_error_analysis_diagnosing_zeroth_term_omission(rng: random.Random) -> Dict[str, Any]:
    # Sequence: 7, 11, 15, 19... d = 4. Flawed rule: Tn = 4n + 7 instead of 4n + 3
    d = 4
    t1 = 7
    c = t1 - d  # 3
    flawed_rule = f"{d}n + {t1}"
    correct_rule = f"{d}n + {c}"

    prompt = (
        f"For the sequence \\(7;\\ 11;\\ 15;\\ 19;\\ \\dots\\), a learner wrote \\(T_n = {flawed_rule}\\) "
        f"by placing the first term directly as the constant.\n\n"
        f"Explain the conceptual error and state the correct general formula."
    )
    sol = (
        f"**Zeroth Term Error:**\n"
        f"1. Error: The constant term \\(c\\) is the zeroth term (\\(T_0 = T_1 - d\\)), NOT the first term \\(T_1\\).\n"
        f"2. \\(c = 7 - 4 = 3\\).\n"
        f"Correct formula: \\(T_n = {correct_rule}\\)."
    )
    return {
        "id": f"g9_pat_err_t0_omission_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Constant is T_0 = T_1 - d; Correct: T_n = {correct_rule}",
        "expected_answer": f"Constant is T_0 = T_1 - d; Correct: T_n = {correct_rule}",
        "sample_answer": f"Constant is T_0 = T_1 - d; Correct: T_n = {correct_rule}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Explain that constant c = T_1 - d", "marks": 1},
            {"desc": f"State correct rule T_n = {correct_rule}", "marks": 1},
        ],
        "hints": [
            "c is the value before term 1 (the 0th term).",
            f"c = {t1} - {d} = {c}.",
            f"Correct: Tn = {correct_rule}.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnosing Proportionality Assumption on Affine
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnosing_proportionality_assumption_on_affine(rng: random.Random) -> Dict[str, Any]:
    # Tn = 3n + 2: T10 = 32. Flawed: T20 = 2 * T10 = 64. Correct: T20 = 3(20) + 2 = 62.
    ans_correct = 62
    ans_flawed = 64

    prompt = (
        f"A linear pattern has the rule \\(T_n = 3n + 2\\). Term 10 is \\(T_{{10}} = 32\\).\n\n"
        f"A learner argues that \\(T_{{20}}\\) must be double \\(T_{{10}}\\) (\\(2 \\times 32 = 64\\)).\n\n"
        f"Explain why this doubling method is incorrect for an affine relationship with a non-zero constant, "
        f"and calculate the actual value of \\(T_{{20}}\\)."
    )
    sol = (
        f"**Affine vs Proportional Misconception:**\n"
        f"1. Doubling only works for direct proportion (\\(y = kx\\)). Because of the constant \\(+2\\), "
        f"the relationship is affine, not directly proportional.\n"
        f"2. Correct value: \\(T_{{20}} = 3(20) + 2 = {ans_correct}\\)."
    )
    return {
        "id": f"g9_pat_err_doubling_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Doubling fails because c != 0; Actual T_20 = {ans_correct}",
        "expected_answer": f"Doubling fails because c != 0; Actual T_20 = {ans_correct}",
        "sample_answer": f"Doubling fails because c != 0; Actual T_20 = {ans_correct}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Explain that non-zero constant prevents direct proportionality", "marks": 1},
            {"desc": f"Calculate accurate term T_20 = {ans_correct}", "marks": 1},
        ],
        "hints": [
            "Doubling the position does not double the value when there is a constant term.",
            f"Calculate T20 = 3(20) + 2.",
            f"Actual value: {ans_correct}.",
        ],
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Pattern Investigation Challenge
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_pattern_investigation_challenge(rng: random.Random) -> Dict[str, Any]:
    # Tn = 4n + 3: T1=7, T2=11, T3=15, T4=19
    # 1. Tn = 4n + 3
    # 2. T100 = 403
    # 3. Which term = 203? 4n+3 = 203 => 4n=200 => n=50
    rule = "4n + 3"
    t100 = 403
    target_pos = 50

    prompt = (
        f"A number pattern begins: \\(7;\\ 11;\\ 15;\\ 19;\\ \\dots\\)\n\n"
        f"1. Derive the general formula \\(T_n\\).\n"
        f"2. Calculate the value of the 100th term (\\(T_{{100}}\\)).\n"
        f"3. Which term in the sequence has a value of **203**?"
    )
    sol = (
        f"**Comprehensive Pattern Investigation:**\n"
        f"1. Difference \\(d = 11 - 7 = 4\\); \\(c = 7 - 4 = 3\\).\n"
        f"   Formula: \\(T_n = {rule}\\).\n"
        f"2. 100th term: \\(T_{{100}} = 4(100) + 3 = {t100}\\).\n"
        f"3. Position: \\(4n + 3 = 203 \\implies 4n = 200 \\implies n = {target_pos}\\)."
    )
    return {
        "id": f"g9_pat_compound_challenge_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_n = {rule}; T_100 = {t100}; n = {target_pos}",
        "expected_answer": f"T_n = {rule}; T_100 = {t100}; n = {target_pos}",
        "sample_answer": f"T_n = {rule}; T_100 = {t100}; n = {target_pos}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Derive formula T_n = {rule}", "marks": 1},
            {"desc": f"Compute T_100 = {t100}", "marks": 1},
            {"desc": f"Solve position n = {target_pos}", "marks": 1},
        ],
        "hints": [
            f"Common difference is 4; Tn = {rule}.",
            f"T100 = 4(100) + 3 = {t100}.",
            f"Set 4n + 3 = 203 to find n = {target_pos}.",
        ],
    }
