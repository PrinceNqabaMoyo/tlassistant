"""Inverse proportion, constant products, and hyperbolic curves (Subskills 10-18) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Identifying inverse proportion from a table where product x × y = k is constant."""
    total_val = r.choice([2400, 3600, 4800, 6000])
    ans_str = f"Inverse Proportion (Constant product of R {_fmt(total_val)},00)"

    x1, y1 = 2, total_val // 2
    x2, y2 = 4, total_val // 4
    x3, y3 = 6, total_val // 6
    x4, y4 = 8, total_val // 8

    prompt = (
        f"A group of holidaymakers hire a beach chalet. The cost per person depends on the group size as shown below:\n\n"
        f"| Number of People (x) | {x1} | {x2} | {x3} | {x4} |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Cost per Person (y) | R {y1:,} | R {y2:,} | R {y3:,} | R {y4:,} |\n\n"
        f"Identify the mathematical type of this relationship and explain the defining test used."
    )
    explanation = (
        f"Step 1: Test products of paired values (x × y):\n"
        f"- {x1} \\times {y1} = {total_val}\n"
        f"- {x2} \\times {y2} = {total_val}\n"
        f"- {x3} \\times {y3} = {total_val}. [1 mark]\n"
        f"Step 2: Note that since the product x × y is constant, as x doubles, y halves. [1 mark]\n"
        f"Step 3: State the relationship type:\n"
        f"\\text{{Relationship type}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "Direct Proportion (Constant ratio)",
        "Linear with positive intercept (Constant difference)",
        "Step-function relationship",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    d_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Chalet Cost per Person (Total R {total_val:,})",
        "lines": [{"name": "Inverse Curve", "points": [{"x": x1, "y": y1}, {"x": x2, "y": y2}, {"x": x3, "y": y3}, {"x": x4, "y": y4}]}],
    }
    return _build_question_payload(
        "subskill_10",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the number of people by the cost per person for each column.",
        f"The product is always {total_val}, confirming inverse proportion.",
        f"Type = {ans_str}.",
        r,
        difficulty="easy",
        diagram_spec=d_spec,
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Formulate inverse proportion formula y = k / x from context."""
    total_rent = r.choice([3600, 4800, 6000, 7200, 8400])
    ans_str = f"Cost per Person = {_fmt_curr(total_rent)} ÷ n"

    prompt = (
        f"A group of university students agree to rent a shared holiday house in Margate for {_fmt_curr(total_rent)}.\n"
        f"The total rental cost will be shared equally among 'n' students who attend.\n\n"
        f"Write down the inverse proportion formula used to calculate the cost per student."
    )
    explanation = (
        f"Step 1: Identify that total cost is fixed at {_fmt_curr(total_rent)}. [1 mark]\n"
        f"Step 2: Note that sharing equally among n students requires division by n. [1 mark]\n"
        f"Step 3: State the formula:\n"
        f"\\text{{Formula}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Cost per Person = {_fmt_curr(total_rent)} × n",
        f"Cost per Person = {_fmt_curr(total_rent)} - n",
        f"Cost per Person = n ÷ {_fmt_curr(total_rent)}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_11",
        prompt,
        ans_str,
        options,
        explanation,
        "Total fixed cost divided by the number of students.",
        f"Cost per student = {_fmt_curr(total_rent)} ÷ n.",
        f"Formula = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Complete missing table values for an inverse proportion relationship."""
    constant_k = 6000
    # x = 2, 4, 6, P
    # y = 3000, 1500, 1000, 600 -> P = 6000 / 600 = 10
    missing_x = 10
    ans_str = f"P = {missing_x}"

    prompt = (
        f"The table below shows an inverse proportion relationship between the number of workers (x) "
        f"and the days taken to pick an orchard (y):\n\n"
        f"| Workers (x) | 2 | 4 | 6 | P |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Days (y) | 30 | 15 | 10 | 6 |\n\n"
        f"Determine the missing worker value 'P'."
    )
    explanation = (
        f"Step 1: Calculate the constant product k:\n"
        f"k = 2 \\times 30 = 4 \\times 15 = 60\\text{{ worker-days}}. [1 mark]\n"
        f"Step 2: Solve for P using P × 6 = 60:\n"
        f"P = 60 \\div 6 = {missing_x} [1 mark]\n"
        f"Step 3: State the missing value:\n"
        f"\\text{{Missing value}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "P = 8",
        "P = 12",
        "P = 5",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_12",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the constant product (2 × 30 = 60), then divide by 6.",
        "60 ÷ 6 = 10.",
        f"Missing value = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Sharing total hiring cost equally among friends."""
    name = r.choice(SA_NAMES)
    total_cost = 4800.0
    group_size = r.choice([4, 6, 8, 12])
    cost_per_person = round(total_cost / group_size, 2)
    ans_str = _fmt_curr(cost_per_person)

    prompt = (
        f"{name} and friends hire a 16-seater minibus for a weekend sporting tournament for a flat fee of {_fmt_curr(total_cost)}.\n"
        f"If {group_size} friends agree to split the cost equally among themselves,\n"
        f"calculate how much each friend must contribute."
    )
    explanation = (
        f"Step 1: State the formula: \\text{{Contribution}} = \\frac{{\\text{{Total Cost}}}}{{\\text{{Number of Friends}}}}. [1 mark]\n"
        f"Step 2: Divide {_fmt_curr(total_cost)} by {group_size}:\n"
        f"4\\,800 \\div {group_size} = {cost_per_person:.2f} [1 mark]\n"
        f"Step 3: State the per-person contribution:\n"
        f"\\text{{Contribution}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_cost / (group_size - 1), 2)),
        _fmt_curr(round(total_cost / (group_size + 2), 2)),
        _fmt_curr(round(cost_per_person + 100, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_13",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide {_fmt_curr(total_cost)} by {group_size} friends.",
        f"Calculate 4 800 ÷ {group_size}.",
        f"Contribution = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Speed vs travel time relationship for a fixed travel distance (t = d / v)."""
    name = r.choice(SA_NAMES)
    distance = 450.0  # km (e.g. Jhb to Durban)
    speed = r.choice([90, 100, 120])
    time_h = round(distance / speed, 1)
    ans_str = f"{_fmt(time_h)} hours"

    prompt = (
        f"{name} is driving a fixed distance of {distance:.0f} km from Johannesburg to Durban.\n"
        f"If {name} maintains a constant average speed of {speed} km/h,\n"
        f"calculate the travel time in hours.\n"
        f"*(Formula: \\text{{Time}} = \\text{{Distance}} \\div \\text{{Speed}}.)*"
    )
    explanation = (
        f"Step 1: Set up the inverse proportion formula:\n"
        f"\\text{{Time}} = \\frac{{{distance:.0f}}}{{{speed}}}. [1 mark]\n"
        f"Step 2: Perform the division:\n"
        f"{distance:.0f} \\div {speed} = {distance / speed:.2f}\\text{{ hours}} [1 mark]\n"
        f"Step 3: State the rounded travel time:\n"
        f"\\text{{Travel time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(time_h + 1.0, 1))} hours",
        f"{_fmt(round(time_h - 0.8, 1))} hours",
        f"{_fmt(round(speed / distance, 2))} hours",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_14",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the distance of {distance:.0f} km by the speed of {speed} km/h.",
        f"Calculate {distance:.0f} ÷ {speed}.",
        f"Time = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Number of workers vs days required to complete a project."""
    initial_workers = 3
    initial_days = 20
    total_man_days = initial_workers * initial_days  # 60
    new_workers = r.choice([4, 5, 6, 10])
    new_days = total_man_days // new_workers
    ans_str = f"{new_days} days"

    prompt = (
        f"A building contractor estimates that {initial_workers} bricklayers take {initial_days} days to build a perimeter wall.\n"
        f"Assuming all bricklayers work at the exact same pace,\n"
        f"how many days will it take if {new_workers} bricklayers are assigned to the project?"
    )
    explanation = (
        f"Step 1: Calculate total man-days required for the job:\n"
        f"\\text{{Man-days}} = {initial_workers} \\times {initial_days} = {total_man_days}\\text{{ man-days}}. [1 mark]\n"
        f"Step 2: Divide total man-days by the new number of workers:\n"
        f"\\text{{Days}} = {total_man_days} \\div {new_workers} [1 mark]\n"
        f"Step 3: State the number of days:\n"
        f"\\text{{Days required}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{new_days + 3} days",
        f"{max(1, new_days - 2)} days",
        f"{int(initial_days * (new_workers / initial_workers))} days",  # Direct proportion error
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_15",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate total worker-days (3 × 20 = 60), then divide by the new worker count.",
        f"60 ÷ {new_workers} = {new_days}.",
        f"Days = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Interpreting an inverse proportion curve."""
    prompt = (
        "Which of the following descriptions correctly characterizes the shape and behavior of an inverse proportion graph?\n"
    )
    correct = (
        "A downward-sloping curve (hyperbola) that decreases steeply at first, then flattens out towards the horizontal axis."
    )
    distractors = [
        "A straight downward-sloping line that cuts both axes at a 45-degree angle.",
        "A series of disconnected horizontal steps that jump upwards.",
        "An upward-curving line that passes through the origin (0; 0).",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Recall the mathematical formula of inverse proportion: y = k / x. [1 mark]\n"
        "Step 2: Analyze the rate of change:\n"
        "As x increases, y decreases rapidly at small x values, and more gradually as x becomes large, never touching zero. [1 mark]\n"
        "Step 3: State the correct description:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_16",
        prompt,
        correct,
        options,
        explanation,
        "Inverse proportion forms a smooth curve (hyperbola) decreasing towards the x-axis.",
        "As x gets bigger, y gets smaller, flattening out towards zero.",
        f"Correct description = {correct}.",
        r,
        difficulty="easy",
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Calculate reduction in per-person contribution when additional members join."""
    total_cost = 6000.0
    initial_n = 4
    new_n = 6
    contrib_1 = total_cost / initial_n  # 1500
    contrib_2 = total_cost / new_n      # 1000
    savings = round(contrib_1 - contrib_2, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"A group of {initial_n} friends plan to hire a holiday villa for {_fmt_curr(total_cost)} and split the cost equally.\n"
        f"Before booking, {new_n - initial_n} more friends join the group, bringing the total to {new_n} people.\n"
        f"By how much does each person's individual contribution decrease?"
    )
    explanation = (
        f"Step 1: Calculate the contribution for {initial_n} people:\n"
        f"\\text{{Cost for 4}} = 6\\,000 \\div 4 = {_fmt_curr(contrib_1)}. [1 mark]\n"
        f"Step 2: Calculate the contribution for {new_n} people:\n"
        f"\\text{{Cost for 6}} = 6\\,000 \\div 6 = {_fmt_curr(contrib_2)}. [1 mark]\n"
        f"Step 3: Subtract to find the reduction per person:\n"
        f"1\\,500 - 1\\,000 = {savings:.2f}.\n"
        f"\\text{{Reduction}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(contrib_2),
        _fmt_curr(round(savings * 1.5, 2)),
        _fmt_curr(round(savings / 2, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_17",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the per-person cost for 4 people and for 6 people, then find the difference.",
        f"4 people = {_fmt_curr(contrib_1)}. 6 people = {_fmt_curr(contrib_2)}. Difference = {_fmt_curr(savings)}.",
        f"Reduction = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Distinguish between direct proportion, linear with intercept, and inverse proportion graphs."""
    scenarios = [
        (
            "The cost of petrol at R 24,00 per litre where zero litres costs R 0,00.",
            "Direct Proportion (straight line through the origin)"
        ),
        (
            "A metered taxi ride charging a R 50,00 base fee plus R 12,00 per kilometre.",
            "Linear with intercept (straight line starting above the origin)"
        ),
        (
            "The sharing of a fixed R 4 000 bus hire cost equally among an increasing number of passengers.",
            "Inverse Proportion (downward-sloping hyperbola)"
        ),
    ]
    scen_text, correct_type = r.choice(scenarios)
    ans_str = correct_type

    prompt = (
        f"Consider the following real-world scenario:\n"
        f"\"{scen_text}\"\n\n"
        f"Which type of mathematical graph represents this relationship?"
    )
    explanation = (
        f"Step 1: Analyse the relationship structure: \"{scen_text}\". [1 mark]\n"
        f"Step 2: Evaluate the graphical behavior. [1 mark]\n"
        f"Step 3: State the matching type:\n"
        f"\\text{{Classification}} = {ans_str}. [1 mark]"
    )
    distractors = [
        t for _, t in scenarios if t != correct_type
    ] + ["Step function (disconnected horizontal segments)"]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors[:3])
    return _build_question_payload(
        "subskill_18",
        prompt,
        ans_str,
        options,
        explanation,
        "Consider whether the graph starts at zero, has a fixed fee, or involves splitting a fixed total.",
        f"The scenario represents {correct_type}.",
        f"Answer = {ans_str}.",
        r,
        difficulty="easy",
    )
