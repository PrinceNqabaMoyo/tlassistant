"""Cluster 2: Linear Patterns & Tables of Values (Subskills 10 to 18)."""
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
# Subskill 10: Constant Difference Identification
# --------------------------------------------------------------------------- #
def _gen_pat_linear_constant_difference_identification(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_constant_difference_identification"
    name = r.choice(SA_NAMES)
    start = r.choice([5, 8, 12, 15, 20])
    diff = r.choice([3, 4, 5, 6, 7, 8])
    t1, t2, t3, t4 = start, start + diff, start + 2 * diff, start + 3 * diff
    correct_ans = f"{diff}"

    prompt = (
        f"{name} records the consecutive daily output in a production log table:\n\n"
        f"| Day ($n$) | 1 | 2 | 3 | 4 |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| Output ($T_n$) | {t1} | {t2} | {t3} | {t4} |\n\n"
        f"Calculate the **constant first difference** between consecutive terms."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The first difference is found by subtracting each term from the term that immediately follows it: $d = T_{{n+1}} - T_n$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$T_2 - T_1 = {t2} - {t1} = {diff}$$\n"
        f"$$T_3 - T_2 = {t3} - {t2} = {diff}$$\n"
        f"$$T_4 - T_3 = {t4} - {t3} = {diff}$$ ✓ [1 Mark: Method – subtracting consecutive terms to test constancy]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Constant difference}} = {diff}$$ ✓ [1 Mark: Accuracy – accurate constant difference]"
    )

    d1 = f"{diff + 1}"
    d2 = f"{diff * 2}"
    d3 = f"{t1}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the first term from the second term.",
        tier_2=f"{t2} - {t1} = {diff}.",
        tier_3=f"The constant difference is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 11: Find Missing Output in Table
# --------------------------------------------------------------------------- #
def _gen_pat_linear_find_missing_output_in_table(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_find_missing_output_in_table"
    name = r.choice(SA_NAMES)
    rate = r.choice([15, 20, 25, 30, 45])  # e.g. Rands per kg or km
    base = r.choice([0, 10, 25, 50])
    target_x = r.choice([6, 7, 8, 9, 10])
    target_y = base + rate * target_x
    correct_ans = f"{target_y}"

    prompt = (
        f"{name} is completing a table where the relationship follows the formula: **$y = {rate}x + {base}$**.\n\n"
        f"| $x$ (Number of units) | 1 | 2 | 3 | **{target_x}** |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| $y$ (Total cost in Rands) | {base + rate} | {base + 2*rate} | {base + 3*rate} | **A** |\n\n"
        f"Calculate the missing value **A** when $x = {target_x}$."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the input value $x = {target_x}$ into the given linear equation $y = {rate}x + {base}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$y = ({rate} \\times {target_x}) + {base} = {rate * target_x} + {base}$$ ✓ [1 Mark: Method – substituting target x into formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$y = {target_y}$$ ✓ [1 Mark: Accuracy – accurate product and sum]"
    )

    d1 = f"{target_y + rate}"
    d2 = f"{target_y - rate}"
    d3 = f"{rate * target_x}"  # forgot base
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Substitute x into the formula y = rate × x + base.",
        tier_2=f"Calculate ({rate} × {target_x}) + {base}.",
        tier_3=f"Value A = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 12: Find Missing Input in Table
# --------------------------------------------------------------------------- #
def _gen_pat_linear_find_missing_input_in_table(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_find_missing_input_in_table"
    name = r.choice(SA_NAMES)
    rate = r.choice([12, 15, 20, 25])
    base = r.choice([30, 40, 50])
    target_x = r.choice([5, 6, 7, 8, 9])
    target_y = base + rate * target_x
    correct_ans = f"{target_x}"

    prompt = (
        f"{name} is using the linear rule **$\\text{{Cost}} = ({rate} \\times x) + {base}$**.\n"
        f"In the table below, the total cost is {target_y}:\n\n"
        f"| $x$ (Hours) | 1 | 2 | **B** |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Cost (Rands) | {base + rate} | {base + 2*rate} | **{target_y}** |\n\n"
        f"Calculate the missing input value **B** (hours)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Solve for $x$ by reversing the operations: subtract the fixed base amount, then divide by the hourly rate.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$${target_y} = {rate}x + {base}$$\n"
        f"$${rate}x = {target_y} - {base} = {target_y - base}$$\n"
        f"$$x = \\frac{{{target_y - base}}}{{{rate}}}$$ ✓ [1 Mark: Method – isolating x by subtracting base and dividing by rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$x = {target_x}$$ ✓ [1 Mark: Accuracy – accurate quotient]"
    )

    d1 = f"{target_x + 1}"
    d2 = f"{target_x - 1}"
    d3 = f"{target_y // rate}"  # forgot to subtract base
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the fixed amount from the total cost first.",
        tier_2=f"Calculate ({target_y} - {base}) ÷ {rate}.",
        tier_3=f"Input B = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 13: Toothpick / Tile Pattern Formula Derivation
# --------------------------------------------------------------------------- #
def _gen_pat_linear_toothpick_tile_pattern_formula(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_toothpick_tile_pattern_formula"
    name = r.choice(SA_NAMES)
    shape_choice = r.choice([
        ("squares", 3, 1, "4, 7, 10, 13", "3n + 1"),
        ("triangles", 2, 1, "3, 5, 7, 9", "2n + 1"),
        ("hexagons", 5, 1, "6, 11, 16, 21", "5n + 1"),
        ("fences", 4, 2, "6, 10, 14, 18", "4n + 2"),
    ])
    shape, m, c, seq, formula_str = shape_choice
    correct_ans = f"T_n = {formula_str}"

    prompt = (
        f"{name} builds a sequence of joined {shape} using matchsticks.\n"
        f"The number of matchsticks used in the first four diagrams is: **{seq}**.\n\n"
        f"Which formula correctly gives the total number of matchsticks $T_n$ needed for diagram number $n$?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Find the constant difference: each new {shape[:-1]} adds {m} matchsticks, so the gradient $m = {m}$.\n"
        f"The formula has the form $T_n = mn + c$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"For diagram 1 ($n = 1$), the number of matches is {seq.split(',')[0].strip()}.\n"
        f"$$T_1 = ({m} \\times 1) + c \\implies c = {seq.split(',')[0].strip()} - {m} = {c}$$\n"
        f"Therefore, the general rule is $T_n = {m}n + {c}$. ✓ [1 Mark: Method – finding constant difference and solving for constant term]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct formula]"
    )

    d1 = f"T_n = {m}n"
    d2 = f"T_n = {m+1}n + 1"
    d3 = f"T_n = n + {m}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The constant difference gives the number multiplied by n.",
        tier_2=f"Difference is {m}. At n = 1: {m}(1) + c = {seq.split(',')[0].strip()} → c = {c}.",
        tier_3=f"Formula is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 14: Predict High Term Value
# --------------------------------------------------------------------------- #
def _gen_pat_linear_predict_high_term_value(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_predict_high_term_value"
    name = r.choice(SA_NAMES)
    m = r.choice([3, 4, 5, 6])
    c = r.choice([1, 2, 3, 5])
    n = r.choice([25, 50, 75, 100])
    tn = m * n + c
    correct_ans = f"{tn}"

    prompt = (
        f"{name} is creating geometric tile patterns governed by the formula:\n"
        f"**$T_n = {m}n + {c}$**, where $n$ is the pattern number.\n\n"
        f"Calculate the number of tiles needed for pattern number **$n = {n}$**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the high term number $n = {n}$ directly into the linear formula $T_n = {m}n + {c}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$T_{{{n}}} = ({m} \\times {n}) + {c} = {m * n} + {c}$$ ✓ [1 Mark: Method – substituting n into formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$T_{{{n}}} = {tn}$$ ✓ [1 Mark: Accuracy – accurate product and addition]"
    )

    d1 = f"{m * n}"  # forgot constant
    d2 = f"{tn + m}"
    d3 = f"{tn - m}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Substitute n = {n} into the formula.",
        tier_2=f"Calculate ({m} × {n}) + {c}.",
        tier_3=f"Term {n} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 15: Determine Pattern Term Number
# --------------------------------------------------------------------------- #
def _gen_pat_linear_determine_pattern_term_number(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_determine_pattern_term_number"
    name = r.choice(SA_NAMES)
    m = r.choice([3, 4, 5])
    c = r.choice([1, 2, 4])
    target_n = r.choice([15, 20, 24, 30])
    total_pieces = m * target_n + c
    correct_ans = f"Pattern {target_n}"

    prompt = (
        f"{name} knows that the number of sticks in a sequence of patterns is given by $T_n = {m}n + {c}$.\n"
        f"A builder uses exactly **{total_pieces} sticks** to construct one of the patterns.\n\n"
        f"Which pattern number ($n$) was constructed?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Set the formula equal to the total sticks and solve for $n$: ${m}n + {c} = {total_pieces}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$${m}n = {total_pieces} - {c} = {total_pieces - c}$$\n"
        f"$$n = \\frac{{{total_pieces - c}}}{{{m}}}$$ ✓ [1 Mark: Method – subtracting c and dividing by m]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$n = {target_n}$$ ✓ [1 Mark: Accuracy – accurate integer pattern number]"
    )

    d1 = f"Pattern {target_n + 1}"
    d2 = f"Pattern {target_n - 1}"
    d3 = f"Pattern {total_pieces // m}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the constant c, then divide by m.",
        tier_2=f"Calculate ({total_pieces} - {c}) ÷ {m}.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 16: Direct Proportion Constant Ratio
# --------------------------------------------------------------------------- #
def _gen_pat_linear_direct_proportion_constant_ratio(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_direct_proportion_constant_ratio"
    name = r.choice(SA_NAMES)
    unit_cost = r.choice([12.50, 15.00, 18.50, 22.00, 25.00])
    kg1, kg2, kg3 = 2, 4, 6
    c1, c2, c3 = unit_cost * kg1, unit_cost * kg2, unit_cost * kg3
    correct_ans = f"R {_fmt(unit_cost)}/kg"

    prompt = (
        f"{name} records the price of fresh potatoes at a farm stall:\n\n"
        f"| Mass ($x$ in kg) | {kg1} | {kg2} | {kg3} |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Cost ($y$ in Rands) | R {_fmt(c1)} | R {_fmt(c2)} | R {_fmt(c3)} |\n\n"
        f"Calculate the constant rate of proportion ($k = \\frac{{y}}{{x}}$) per kilogram."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In direct proportion, the ratio between the dependent variable and the independent variable is constant: $k = \\frac{{y}}{{x}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$k = \\frac{{{_fmt(c1)}}}{{{kg1}}} = \\frac{{{_fmt(c2)}}}{{{kg2}}} = \\frac{{{_fmt(c3)}}}{{{kg3}}}$$ ✓ [1 Mark: Method – dividing cost by mass to find constant unit rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$k = \\text{{R }}{_fmt(unit_cost)}\\text{{ per kg}}$$ ✓ [1 Mark: Accuracy – accurate unit rate with correct units]"
    )

    d1 = f"R {_fmt(unit_cost * 2)}/kg"
    d2 = f"R {_fmt(unit_cost / 2)}/kg"
    d3 = f"R {_fmt(unit_cost + 5)}/kg"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the cost by the mass: y ÷ x.",
        tier_2=f"Calculate R {_fmt(c1)} ÷ {kg1} kg.",
        tier_3=f"Unit rate = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 17: Direct Proportion Origin Property
# --------------------------------------------------------------------------- #
def _gen_pat_linear_direct_proportion_origin_property(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_direct_proportion_origin_property"
    k = r.choice([15, 20, 25, 30])
    correct_ans = "It is a straight line that passes through the origin (0; 0)"

    prompt = (
        f"Refer to the direct proportion graph below (y = {k}x).\n\n"
        f"What fundamental geometric property must be true for the graph of any direct proportion relationship?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A direct proportion has the algebraic formula y = kx.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"When x = 0, y = k(0) = 0. Therefore the line must be straight and pass through (0; 0). "
        f"✓ [1 Mark: Method – identifying direct proportion origin constraint]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct geometric property]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Direct Proportion (y = {k}x)",
        "lines": [{"points": [[0, 0], [4, k * 4]], "label": f"y = {k}x"}],
    }

    custom = [
        correct_ans,
        "It is a curved hyperbola that never touches the axes",
        "It is a horizontal line with a y-intercept greater than zero",
        "It is a stepped line with discontinuous jumps",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What is y when x = 0 in y = kx?",
        tier_2="When x = 0, y = 0, so the line passes through (0; 0).",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} is plotting the graph of a direct proportion relationship between litres of petrol and total cost.\n\n"
        f"What are the two essential geometric characteristics of any **direct proportion graph**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A relationship is in direct proportion if one variable is a constant multiple of the other ($y = kx$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"When $x = 0$ (0 litres purchased), the cost $y$ must be exactly 0 Rands. "
        f"Because the rate $k$ is constant, the graph has a constant gradient.\n"
        f"Therefore, it must form a straight line that passes directly through the origin $(0; 0)$. "
        f"✓ [1 Mark: Method – identifying zero intercept and linear linearity properties]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct characteristic description]"
    )

    custom = [
        correct_ans,
        "It is a curved line that never touches the axes",
        "It is a horizontal flat line with a positive y-intercept",
        "It is a straight line that crosses the y-axis above zero",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="If you buy 0 items, the cost is 0.",
        tier_2="Direct proportion is linear and starts at (0; 0).",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 18: Ordered Pairs from Table
# --------------------------------------------------------------------------- #
def _gen_pat_linear_ordered_pairs_from_table(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_ordered_pairs_from_table"
    name = r.choice(SA_NAMES)
    x_val = r.choice([3, 4, 5, 6, 8])
    rate = r.choice([10, 15, 20, 25])
    base = r.choice([0, 15, 30])
    y_val = base + rate * x_val
    correct_ans = f"({x_val}; {y_val})"

    prompt = (
        f"{name} is preparing to plot a point on a Cartesian graph from the table below:\n\n"
        f"| Hours ($x$) | Cost in Rands ($y$) |\n"
        f"| :---: | :---: |\n"
        f"| **{x_val}** | **{y_val}** |\n\n"
        f"Write down the correct ordered pair $(x; y)$ coordinates to plot this point."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An ordered pair is written as $(x; y)$ where the horizontal independent coordinate ($x$) is written first, "
        f"followed by the vertical dependent coordinate ($y$), separated by a semicolon in South African notation.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"From the table, $x = {x_val}$ and $y = {y_val}$.\n"
        f"Forming the coordinate pair gives $({x_val}; {y_val})$. ✓ [1 Mark: Method – placing independent x first and dependent y second]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate ordered pair]"
    )

    d1 = f"({y_val}; {x_val})"  # inverted order
    d2 = f"({x_val + 1}; {y_val})"
    d3 = f"({x_val}; {y_val - rate})"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Ordered pairs are always (x; y): x comes first, y comes second.",
        tier_2=f"Here x = {x_val} and y = {y_val}.",
        tier_3=f"The ordered pair is {correct_ans}.",
        r=r,
    )
