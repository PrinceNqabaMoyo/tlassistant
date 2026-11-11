"""Linear relationships, constant differences, and formula modeling (Subskills 1-9) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Identifying a linear relationship from a table via constant first differences."""
    first_diff = r.choice([15, 25, 40, 50, 75])
    intercept = r.choice([50, 100, 120, 150])
    ans_str = f"Linear (Constant difference of R {_fmt(first_diff)},00)"

    prompt = (
        f"A catering business charges the following total amounts for varying numbers of lunch guests:\n\n"
        f"| Number of Guests (x) | 10 | 20 | 30 | 40 |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Total Cost in Rands (y) | R {intercept + first_diff * 10:,} | R {intercept + first_diff * 20:,} | R {intercept + first_diff * 30:,} | R {intercept + first_diff * 40:,} |\n\n"
        f"Identify the mathematical type of this relationship and the constant difference between consecutive steps of 10 guests."
    )
    explanation = (
        f"Step 1: Calculate the first differences between consecutive output values:\n"
        f"- {intercept + first_diff * 20} - {intercept + first_diff * 10} = {first_diff * 10}\n"
        f"- {intercept + first_diff * 30} - {intercept + first_diff * 20} = {first_diff * 10}. [1 mark]\n"
        f"Step 2: Note that for every 10 guests, the cost increases by a constant R {first_diff * 10},00 "
        f"(R {first_diff},00 per guest). [1 mark]\n"
        f"Step 3: Conclude relationship type:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "Inverse Proportion (Constant product)",
        "Constant Ratio / Exponential (Increasing differences)",
        f"Linear (Constant difference of R {_fmt(first_diff + 10)},00)",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_1",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the difference between consecutive cost values; if it is constant, the relationship is linear.",
        f"Difference per 10 guests is constant at R {first_diff * 10},00 (R {first_diff},00 per guest).",
        f"Type = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Formulating a linear equation y = mx + c from a word problem."""
    name = r.choice(SA_NAMES)
    callout_fee = r.choice([150, 200, 250, 300])
    hourly_rate = r.choice([180, 220, 250, 300])
    ans_str = f"Cost = {_fmt_curr(callout_fee)} + ({_fmt_curr(hourly_rate)} × hours)"

    prompt = (
        f"{name} operates a home electrical repair service.\n"
        f"The pricing structure includes a fixed call-out fee of {_fmt_curr(callout_fee)} plus a labour charge "
        f"of {_fmt_curr(hourly_rate)} for each hour of work.\n\n"
        f"Write down the linear formula representing the total cost (in Rands) for a job taking 'h' hours."
    )
    explanation = (
        f"Step 1: Identify the fixed cost (vertical intercept c):\n"
        f"\\text{{Fixed call-out fee}} = {_fmt_curr(callout_fee)}. [1 mark]\n"
        f"Step 2: Identify the variable rate (gradient m):\n"
        f"\\text{{Hourly rate}} = {_fmt_curr(hourly_rate)}\\text{{ per hour}}. [1 mark]\n"
        f"Step 3: Assemble into standard linear equation y = c + mx:\n"
        f"\\text{{Formula}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Cost = {_fmt_curr(hourly_rate)} + ({_fmt_curr(callout_fee)} × hours)",
        f"Cost = {_fmt_curr(callout_fee + hourly_rate)} × hours",
        f"Cost = {_fmt_curr(callout_fee)} × ({_fmt_curr(hourly_rate)} + hours)",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_2",
        prompt,
        ans_str,
        options,
        explanation,
        "Fixed call-out fee is added once; hourly rate is multiplied by hours.",
        f"Total Cost = Fixed ({_fmt_curr(callout_fee)}) + Variable ({_fmt_curr(hourly_rate)} × h).",
        f"Formula = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Completing missing values in a linear input-output table."""
    base_rate = 35.0  # e.g. R 35 per kg
    fixed_fee = 50.0  # Delivery fee
    # table: x = [2, 5, 8, M] -> y = [120, 225, 330, 470]
    # M = (470 - 50) / 35 = 12
    ans_val = 12
    ans_str = f"{ans_val} kg"

    prompt = (
        f"A courier company charges for parcels using the formula:\n"
        f"Cost = R 50,00 + (R 35,00 × mass in kg).\n\n"
        f"Study the table of values below:\n"
        f"| Mass in kg (x) | 2 | 5 | 8 | M |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Total Cost in Rands (y) | R 120,00 | R 225,00 | R 330,00 | R 470,00 |\n\n"
        f"Determine the missing mass value 'M'."
    )
    explanation = (
        f"Step 1: Set up the equation using the given total cost of R 470,00:\n"
        f"470 = 50 + (35 \\times M). [1 mark]\n"
        f"Step 2: Subtract 50 from 470 and divide by 35:\n"
        f"35 \\times M = 470 - 50 = 420\n"
        f"M = 420 \\div 35 [1 mark]\n"
        f"Step 3: State the final mass value:\n"
        f"M = {ans_str}. [1 mark]"
    )
    distractors = [
        "10 kg",
        "14 kg",
        "11 kg",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_3",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract R 50 from R 470, then divide by R 35.",
        "470 - 50 = 420. 420 ÷ 35 = 12.",
        f"Missing value M = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Calculating gradient (rate of change) from two points on a graph."""
    h1 = r.choice([1, 2, 3])
    h2 = h1 + r.choice([3, 4, 5])
    rate = r.choice([50, 60, 75, 80, 100])
    base = r.choice([80, 100, 120])
    c1 = base + h1 * rate
    c2 = base + h2 * rate
    gradient = float(rate)
    ans_str = f"R {_fmt(gradient)},00 per hour"

    prompt = (
        f"Refer to the plumber's charges linear graph shown in the diagram passing through recorded points:\n"
        f"• ({h1} hours ; R {_fmt(c1)},00)\n"
        f"• ({h2} hours ; R {_fmt(c2)},00)\n\n"
        f"Calculate the plumber's hourly labor rate (the gradient / rate of change of the graph).\n"
        f"*(Formula: \\text{{Gradient}} = \\frac{{y_2 - y_1}}{{x_2 - x_1}}.)*"
    )
    explanation = (
        f"Step 1: Identify coordinates: (x_1, y_1) = ({h1}; {c1}), (x_2, y_2) = ({h2}; {c2}). [1 mark]\n"
        f"Step 2: Apply the gradient formula:\n"
        f"\\text{{Gradient}} = \\frac{{{c2} - {c1}}}{{{h2} - {h1}}} = \\frac{{{c2 - c1}}}{{{h2 - h1}}} = {gradient:.0f} [1 mark]\n"
        f"Step 3: State the hourly rate with units:\n"
        f"\\text{{Hourly rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"R {_fmt(gradient + 15)},00 per hour",
        f"R {_fmt(gradient - 15)},00 per hour",
        f"R {_fmt(c1 / h1)},00 per hour",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    d_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Labor Charges: ({h1} h; R {c1}) to ({h2} h; R {c2})",
        "lines": [{"name": "Charges", "points": [{"x": h1, "y": c1}, {"x": h2, "y": c2}]}],
    }
    return _build_question_payload(
        "subskill_4",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract y values (450 - 210) and divide by the difference in x values (6 - 2).",
        "240 ÷ 4 = 60.",
        f"Gradient = {ans_str}.",
        r,
        difficulty="medium",
        diagram_spec=d_spec,
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Identifying vertical intercept (c) from a graph and interpreting its contextual meaning."""
    fixed_charge = 120.0
    ans_str = f"R {_fmt(fixed_charge)},00 (the fixed base fee charged before any usage)"

    prompt = (
        f"A straight-line graph represents the monthly cost of a piped gas account against cubic metres consumed.\n"
        f"The line intersects the vertical cost axis (y-axis) at R 120,00 when gas consumption is 0 m³.\n\n"
        f"State the value of the vertical intercept and explain what it represents in this real-world context."
    )
    explanation = (
        f"Step 1: Read the vertical intercept at x = 0:\n"
        f"\\text{{Intercept}} = R 120,00. [1 mark]\n"
        f"Step 2: Contextual interpretation:\n"
        f"At zero gas consumption, the customer must still pay R 120,00. This represents the basic fixed connection/network charge. [1 mark]\n"
        f"Step 3: State the combined answer:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "R 0,00 (free initial gas consumption)",
        f"R {_fmt(fixed_charge)},00 (the maximum monthly limit on gas usage)",
        "R 12,00 (the variable rate per cubic metre)",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_5",
        prompt,
        ans_str,
        options,
        explanation,
        "The vertical intercept occurs where consumption is 0 and represents the fixed charge.",
        "Vertical intercept = R 120, representing fixed basic fee.",
        f"Answer = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Direct proportion without fixed cost (y = kx passing through origin)."""
    rate_per_kg = 24.50
    kg_val = r.choice([4, 6, 8, 12, 15])
    cost = round(kg_val * rate_per_kg, 2)
    ans_str = _fmt_curr(cost)

    prompt = (
        f"Braai charcoal is sold in bulk at a direct proportion rate of {_fmt_curr(rate_per_kg)} per kilogram, "
        f"with no base packaging fee (Cost = R 24,50 × kg).\n"
        f"Calculate the total cost for {kg_val} kg of charcoal."
    )
    explanation = (
        f"Step 1: Note that direct proportion passes through the origin (0; 0) with formula y = kx. [1 mark]\n"
        f"Step 2: Multiply the quantity by the unit rate:\n"
        f"\\text{{Cost}} = {kg_val} \\times 24,50 = {cost:.2f} [1 mark]\n"
        f"Step 3: State the final cost:\n"
        f"\\text{{Total cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(cost * 1.25, 2)),
        _fmt_curr(round(cost - 24.50, 2)),
        _fmt_curr(round(kg_val * 20.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_6",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply {kg_val} kg by {_fmt_curr(rate_per_kg)}.",
        f"Calculate {kg_val} × 24,50.",
        f"Cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Evaluate linear formula output given independent variable."""
    fixed = 250.0
    rate_km = 4.50
    km = r.choice([60, 85, 120, 150, 200])
    total = round(fixed + (km * rate_km), 2)
    ans_str = _fmt_curr(total)

    prompt = (
        f"A bakkie hire company uses the formula:\n"
        f"Total Cost = R 250,00 + (R 4,50 × distance in km).\n\n"
        f"Calculate the total cost for hiring the bakkie for a trip of {km} km."
    )
    explanation = (
        f"Step 1: Substitute {km} km into the formula:\n"
        f"\\text{{Total}} = 250 + (4,50 \\times {km}). [1 mark]\n"
        f"Step 2: Calculate variable travel cost and add fixed fee:\n"
        f"4,50 \\times {km} = {_fmt(km * rate_km)}\n"
        f"\\text{{Total}} = 250 + {_fmt(km * rate_km)} = {total:.2f} [1 mark]\n"
        f"Step 3: State the final total cost:\n"
        f"\\text{{Total cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(km * rate_km, 2)),
        _fmt_curr(round(total + 50, 2)),
        _fmt_curr(round(total - 50, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_7",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply {km} by R 4,50 and add R 250.",
        f"Variable = {km} × 4,50 = {_fmt(km * rate_km)}. Total = 250 + {_fmt(km * rate_km)}.",
        f"Cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Solving for independent variable given total dependent value (x = (y - c) / m)."""
    fixed = 180.0
    rate_per_shirt = 45.0
    target_budget = 900.0
    # shirts = (900 - 180) / 45 = 720 / 45 = 16
    shirts = int((target_budget - fixed) / rate_per_shirt)
    ans_str = f"{shirts} T-shirts"

    prompt = (
        f"A screen-printing shop charges for customized sports jerseys according to the formula:\n"
        f"Total Cost = R 180,00 + (R 45,00 × number of T-shirts).\n\n"
        f"If a school club has a total budget of {_fmt_curr(target_budget)}, "
        f"how many T-shirts can they afford to print?"
    )
    explanation = (
        f"Step 1: Set up the equation with the given budget:\n"
        f"900 = 180 + (45 \\times n). [1 mark]\n"
        f"Step 2: Subtract the fixed setup fee and divide by R 45:\n"
        f"45 \\times n = 900 - 180 = 720\n"
        f"n = 720 \\div 45 [1 mark]\n"
        f"Step 3: State the number of shirts:\n"
        f"n = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{shirts - 2} T-shirts",
        f"{shirts + 2} T-shirts",
        f"{int(target_budget / rate_per_shirt)} T-shirts",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_8",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract R 180 from R 900, then divide by R 45.",
        "900 - 180 = 720. 720 ÷ 45 = 16.",
        f"Affordable quantity = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Compare two linear service providers using algebraic formulas."""
    km = 100.0
    # Provider 1: R 300 base + R 5/km -> 300 + 500 = R 800
    # Provider 2: R 150 base + R 7/km -> 150 + 700 = R 850
    cost_1 = 300.0 + (5.0 * km)  # 800
    cost_2 = 150.0 + (7.0 * km)  # 850
    diff = abs(cost_2 - cost_1)
    ans_str = f"Provider 1 is cheaper by {_fmt_curr(diff)}"

    prompt = (
        f"A business compares two truck rental quotes for a 100 km delivery trip:\n"
        f"• Provider 1: Cost = R 300,00 + (R 5,00 × km)\n"
        f"• Provider 2: Cost = R 150,00 + (R 7,00 × km)\n\n"
        f"Calculate the cost for both providers for 100 km and determine which provider is cheaper, and by how much."
    )
    explanation = (
        f"Step 1: Calculate the cost for Provider 1 at 100 km:\n"
        f"\\text{{Cost 1}} = 300 + (5 \\times 100) = 300 + 500 = {_fmt_curr(cost_1)}. [1 mark]\n"
        f"Step 2: Calculate the cost for Provider 2 at 100 km:\n"
        f"\\text{{Cost 2}} = 150 + (7 \\times 100) = 150 + 700 = {_fmt_curr(cost_2)}. [1 mark]\n"
        f"Step 3: Subtract to compare:\n"
        f"850 - 800 = {diff:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Provider 2 is cheaper by {_fmt_curr(diff)}",
        f"Provider 1 is cheaper by {_fmt_curr(round(diff * 2, 2))}",
        "Both providers charge the exact same cost",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_9",
        prompt,
        ans_str,
        options,
        explanation,
        "Evaluate both formulas for 100 km and subtract the two totals.",
        f"Provider 1 = R 800. Provider 2 = R 850. Difference = {_fmt_curr(diff)}.",
        f"Outcome = {ans_str}.",
        r,
        difficulty="medium",
    )
