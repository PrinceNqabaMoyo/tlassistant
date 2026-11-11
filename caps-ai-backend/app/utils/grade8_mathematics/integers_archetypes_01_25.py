"""
Grade 8 Mathematics - Integers Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import (
    draw_thermometer_svg,
    draw_number_line_svg,
    draw_elevation_profile_svg,
    _svg_wrap,
)

SA_CITIES = [
    ("Sutherland", -8, 14),
    ("Bethlehem", -6, 16),
    ("Bloemfontein", -4, 18),
    ("Underberg", -7, 13),
    ("Barkly East", -9, 12),
    ("Standerton", -5, 17),
    ("Kimberley", -2, 21),
]


# ==============================================================================
# CLUSTER 1: Real-World Contexts & Diagrams (01 - 10)
# ==============================================================================

def arch_01_reading_winter_thermometer_subzero(rng: random.Random) -> Dict[str, Any]:
    temp = -rng.randint(2, 12)
    city, _, _ = rng.choice(SA_CITIES)
    svg = draw_thermometer_svg(temp, min_t=-20, max_t=30, show_reading=False, label=f"Weather Station: {city}")

    prompt = (
        f"A weather station thermometer in **{city}** shows the reading below.\n\n"
        f"1. Read and write down the temperature shown in degrees Celsius ($^\\circ\\text{{C}}$).\n"
        f"2. State whether this integer is positive or negative."
    )
    sol = (
        f"**Step 1:** Look at the top of the liquid column on the calibrated scale.\n"
        f"The liquid level aligns with the **{temp}^\\circ\\text{{C}}** mark [1 Mark: Method].\n\n"
        f"**Step 2:** Because the value lies below the freezing mark ($0^\\circ\\text{{C}}$), it is a **negative integer** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\text{{Reading}} = {temp}^\\circ\\text{{C}} \\text{{ (Negative)}}$$"
    )
    ans = f"{temp}°C (Negative)"
    return {
        "id": f"g8_int_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "01_reading_winter_thermometer_subzero",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "temp": temp, "city": city},
        "hints": {
            "tier_1": "Observe whether the liquid column is above or below the 0°C line.",
            "tier_2": "Count the tick marks downwards from 0°C in the negative direction.",
            "tier_3": f"The liquid level rests at {temp}°C, which is negative."
        },
        "misconception_tags": ["confused_positive_negative_thermometer"]
    }


def arch_02_temperature_rise_through_zero(rng: random.Random) -> Dict[str, Any]:
    city, _, _ = rng.choice(SA_CITIES)
    t_start = -rng.randint(3, 8)
    rise = rng.randint(9, 16)
    t_end = t_start + rise

    prompt = (
        f"At 05:00 on a July morning in {city}, the temperature was ${t_start}^\\circ\\text{{C}}$. "
        f"By 13:00, the temperature had increased by ${rise}^\\circ\\text{{C}}$.\n\n"
        f"1. Write down an integer addition expression representing the final temperature.\n"
        f"2. Calculate the afternoon temperature at 13:00."
    )
    sol = (
        f"**Step 1:** Start at ${t_start}^\\circ\\text{{C}}$ and add the increase of $+{rise}^\\circ\\text{{C}}$:\n"
        f"$$\\text{{Expression}} = ({t_start}) + {rise}$$ [1 Mark]\n\n"
        f"**Step 2:** Moving from ${t_start}$ past zero: ${t_start} + {rise} = {t_end}^\\circ\\text{{C}}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Afternoon temperature}} = {t_end}^\\circ\\text{{C}}$$"
    )
    ans = f"1. ({t_start}) + {rise}; 2. {t_end}°C"
    return {
        "id": f"g8_int_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_temperature_rise_through_zero",
        "hints": {
            "tier_1": "Add the positive rise to the negative starting temperature.",
            "tier_2": f"Think of a number line: start at {t_start} and move {rise} units to the right.",
            "tier_3": f"{t_start} + {rise} = {t_end}."
        },
        "misconception_tags": ["incorrect_integer_addition_sign"]
    }


def arch_03_temperature_drop_through_zero(rng: random.Random) -> Dict[str, Any]:
    city, _, _ = rng.choice(SA_CITIES)
    t_noon = rng.randint(4, 9)
    drop = rng.randint(7, 14)
    t_night = t_noon - drop

    prompt = (
        f"In {city}, the afternoon temperature was $+{t_noon}^\\circ\\text{{C}}$. "
        f"Overnight, a cold front caused the temperature to drop by ${drop}^\\circ\\text{{C}}$.\n\n"
        f"Calculate the minimum overnight temperature."
    )
    sol = (
        f"**Step 1:** Starting temperature is $+{t_noon}^\\circ\\text{{C}}$ and drop is ${drop}^\\circ\\text{{C}}$:\n"
        f"$$\\text{{Temperature}} = {t_noon} - {drop}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Subtracting a larger positive number from a smaller positive gives a negative result:\n"
        f"$${t_noon} - {drop} = {t_night}^\\circ\\text{{C}}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Overnight temperature}} = {t_night}^\\circ\\text{{C}}$$"
    )
    ans = f"{t_night}°C"
    return {
        "id": f"g8_int_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_temperature_drop_through_zero",
        "hints": {
            "tier_1": "Subtract the drop from the afternoon temperature.",
            "tier_2": f"Calculate {t_noon} - {drop}.",
            "tier_3": f"{t_noon} - {drop} = {t_night}."
        },
        "misconception_tags": ["subtraction_crossing_zero_error"]
    }


def arch_04_diurnal_temperature_range_calculation(rng: random.Random) -> Dict[str, Any]:
    city, _, _ = rng.choice(SA_CITIES)
    t_min = -rng.randint(3, 8)
    t_max = rng.randint(12, 22)
    range_t = t_max - t_min

    prompt = (
        f"On a particular winter day in {city}, the maximum temperature recorded was $+{t_max}^\\circ\\text{{C}}$ "
        f"and the minimum temperature was ${t_min}^\\circ\\text{{C}}$.\n\n"
        f"1. Write down a subtraction expression to calculate the temperature range: $T_{{\\max}} - T_{{\\min}}$.\n"
        f"2. Calculate the diurnal temperature range in degrees Celsius."
    )
    sol = (
        f"**Step 1:** The formula for temperature range is $T_{{\\max}} - T_{{\\min}}$:\n"
        f"$$\\text{{Expression}} = ({t_max}) - ({t_min})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Subtracting a negative integer is equivalent to adding its positive counterpart:\n"
        f"$${t_max} - ({t_min}) = {t_max} + {-t_min} = {range_t}^\\circ\\text{{C}}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Diurnal range}} = {range_t}^\\circ\\text{{C}}$$"
    )
    ans = f"1. ({t_max}) - ({t_min}); 2. {range_t}°C"
    return {
        "id": f"g8_int_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_diurnal_temperature_range_calculation",
        "hints": {
            "tier_1": "Range is maximum minus minimum: T_max - T_min.",
            "tier_2": f"Notice the double negative: {t_max} - ({t_min}) = {t_max} + {-t_min}.",
            "tier_3": f"{t_max} + {-t_min} = {range_t}°C."
        },
        "misconception_tags": ["double_negative_subtraction_error"]
    }


def arch_05_bank_overdraft_after_withdrawal(rng: random.Random) -> Dict[str, Any]:
    initial_balance = rng.randint(120, 450)
    withdrawal = initial_balance + rng.randint(180, 600)
    overdraft = initial_balance - withdrawal

    prompt = (
        f"Lerato's cheque bank account has an opening balance of **R{initial_balance}**. "
        f"She authorises an electronic debit order payment of **R{withdrawal}** to pay for school textbooks.\n\n"
        f"1. Write down an integer equation for her new balance.\n"
        f"2. Determine her new bank balance, indicating whether the account is in credit or overdrawn."
    )
    sol = (
        f"**Step 1:** Equation: $\\text{{New Balance}} = {initial_balance} - {withdrawal}$ [1 Mark].\n\n"
        f"**Step 2:** Calculate: ${initial_balance} - {withdrawal} = -\\text{{R}}{abs(overdraft)}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{New balance}} = -\\text{{R}}{abs(overdraft)} \\text{{ (Overdrawn by R{abs(overdraft)})}}$$"
    )
    ans = f"1. {initial_balance} - {withdrawal}; 2. -R{abs(overdraft)} (Overdrawn by R{abs(overdraft)})"
    return {
        "id": f"g8_int_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_bank_overdraft_after_withdrawal",
        "hints": {
            "tier_1": "Subtract the withdrawal amount from the current balance.",
            "tier_2": f"Since {withdrawal} > {initial_balance}, the result is negative.",
            "tier_3": f"{initial_balance} - {withdrawal} = -{abs(overdraft)}."
        },
        "misconception_tags": ["overdraft_sign_error"]
    }


def arch_06_deposit_clearing_partial_debt(rng: random.Random) -> Dict[str, Any]:
    debt = -rng.randint(400, 950)
    deposit = rng.randint(150, abs(debt) - 50)
    remaining_debt = debt + deposit

    prompt = (
        f"A small tuckshop in Soweto has an overdrawn bank account balance of **-R{abs(debt)}**. "
        f"The owner deposits **R{deposit}** cash from daily sales into the account.\n\n"
        f"Calculate the new balance of the account."
    )
    sol = (
        f"**Step 1:** Add the deposit to the negative balance:\n"
        f"$$\\text{{Balance}} = ({debt}) + {deposit}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Adding a positive integer to a negative integer with greater absolute value:\n"
        f"$${debt} + {deposit} = {remaining_debt}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{New balance}} = -\\text{{R}}{abs(remaining_debt)} \\text{{ (Overdrawn)}}$$"
    )
    ans = f"-R{abs(remaining_debt)}"
    return {
        "id": f"g8_int_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_deposit_clearing_partial_debt",
        "hints": {
            "tier_1": "Add the deposit amount to the negative debt balance.",
            "tier_2": f"Calculate {debt} + {deposit}.",
            "tier_3": f"The account remains overdrawn by R{abs(remaining_debt)}: -R{abs(remaining_debt)}."
        },
        "misconception_tags": ["debt_addition_sign_confusion"]
    }


def arch_07_business_net_profit_and_loss_period(rng: random.Random) -> Dict[str, Any]:
    rev = rng.randint(1500, 3200)
    exp = rev + rng.randint(400, 1200)
    loss = rev - exp

    prompt = (
        f"In its first month of operations, a student stationery service recorded **R{rev}** in revenue and **R{exp}** in total expenses.\n\n"
        f"1. Write down an integer calculation for the net profit or loss: $\\text{{Revenue}} - \\text{{Expenses}}$.\n"
        f"2. State whether the business achieved a net profit or a net loss, and by what amount."
    )
    sol = (
        f"**Step 1:** Calculation: ${rev} - {exp} = {loss}$ [1 Mark].\n\n"
        f"**Step 2:** Because the result is negative, the business experienced a **net loss** of **R{abs(loss)}** [1 Mark].\n\n"
        f"$$\\therefore \\text{{Net loss of R{abs(loss)}}}$$"
    )
    ans = f"1. {rev} - {exp} = -R{abs(loss)}; 2. Net loss of R{abs(loss)}"
    return {
        "id": f"g8_int_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_business_net_profit_and_loss_period",
        "hints": {
            "tier_1": "Net result = Revenue - Expenses.",
            "tier_2": f"{rev} - {exp} yields a negative value.",
            "tier_3": f"A negative net result indicates a net loss of R{abs(loss)}."
        },
        "misconception_tags": ["loss_profit_sign_confusion"]
    }


def arch_08_mine_shaft_elevation_below_surface(rng: random.Random) -> Dict[str, Any]:
    surface_alt = rng.randint(1400, 1750)
    depth = rng.randint(1800, 2900)
    bottom_alt = surface_alt - depth
    svg = draw_elevation_profile_svg(surface_alt, [("Surface Shaft", surface_alt, "#059669"), ("Shaft Bottom", bottom_alt, "#dc2626")])

    prompt = (
        f"A gold mine in Gauteng has a surface shaft collar situated at an elevation of **+{surface_alt} m** above sea level. "
        f"The main elevator shaft descends vertically downwards by **{depth} m**.\n\n"
        f"Calculate the elevation of the bottom of the mine shaft relative to sea level."
    )
    sol = (
        f"**Step 1:** Subtract the depth descended from the surface elevation:\n"
        f"$$\\text{{Elevation}} = {surface_alt} - {depth}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Subtracting a greater distance gives an elevation below sea level:\n"
        f"$${surface_alt} - {depth} = {bottom_alt}\\text{{ m}}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Elevation at bottom}} = {bottom_alt}\\text{{ m (or {abs(bottom_alt)} m below sea level)}}$$"
    )
    ans = f"{bottom_alt} m"
    return {
        "id": f"g8_int_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_mine_shaft_elevation_below_surface",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "surface": surface_alt, "bottom": bottom_alt},
        "hints": {
            "tier_1": "Subtract the vertical shaft depth from the surface elevation.",
            "tier_2": f"Calculate {surface_alt} - {depth}.",
            "tier_3": f"The elevation is {bottom_alt} m relative to sea level."
        },
        "misconception_tags": ["depth_elevation_subtraction_error"]
    }


def arch_09_diver_depth_and_ascent(rng: random.Random) -> Dict[str, Any]:
    depth = -rng.randint(18, 42)
    ascent = rng.randint(6, abs(depth) - 4)
    new_depth = depth + ascent

    prompt = (
        f"A marine research diver exploring Sodwana Bay is at a depth of **{depth} m** relative to sea level. "
        f"The diver then ascends vertically by **{ascent} m** towards the surface.\n\n"
        f"1. Write down an integer addition expression for the diver's new position.\n"
        f"2. Calculate the diver's new depth relative to sea level."
    )
    sol = (
        f"**Step 1:** Expression: $({depth}) + {ascent}$ [1 Mark].\n\n"
        f"**Step 2:** Calculate: ${depth} + {ascent} = {new_depth}\\text{{ m}}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{New depth}} = {new_depth}\\text{{ m (or {abs(new_depth)} m below sea level)}}$$"
    )
    ans = f"1. ({depth}) + {ascent}; 2. {new_depth} m"
    return {
        "id": f"g8_int_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_diver_depth_and_ascent",
        "hints": {
            "tier_1": "Start at the negative depth and add the positive ascent distance.",
            "tier_2": f"Calculate {depth} + {ascent}.",
            "tier_3": f"{depth} + {ascent} = {new_depth} m."
        },
        "misconception_tags": ["ascent_negative_sign_confusion"]
    }


def arch_10_number_line_missing_integers(rng: random.Random) -> Dict[str, Any]:
    step = rng.choice([2, 3, 5])
    start = -step * 4
    end = step * 4
    val_p = -step * rng.randint(1, 3)
    val_q = step * rng.randint(1, 3)
    markers = {val_p: "P", val_q: "Q"}
    svg = draw_number_line_svg(start, end, step=step, markers=markers, label="Integer Number Line")

    prompt = (
        f"Refer to the integer number line figure with regular steps.\n\n"
        f"1. Identify the integer represented by point **P**.\n"
        f"2. Identify the integer represented by point **Q**.\n"
        f"3. Calculate the distance between point P and point Q."
    )
    dist = val_q - val_p
    sol = (
        f"**Step 1:** Point P is located at **{val_p}** [1 Mark].\n\n"
        f"**Step 2:** Point Q is located at **{val_q}** [1 Mark].\n\n"
        f"**Step 3:** Distance = $Q - P = {val_q} - ({val_p}) = {val_q} + {-val_p} = {dist}$ units [1 Mark].\n\n"
        f"$$\\therefore P = {val_p}, \\quad Q = {val_q}, \\quad \\text{{Distance}} = {dist}$$"
    )
    ans = f"1. P = {val_p}; 2. Q = {val_q}; 3. Distance = {dist}"
    return {
        "id": f"g8_int_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "10_number_line_missing_integers",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "p": val_p, "q": val_q, "step": step},
        "hints": {
            "tier_1": "Observe the step size between tick marks on the number line.",
            "tier_2": f"Point P is to the left of 0 at {val_p}; point Q is to the right at {val_q}.",
            "tier_3": f"Distance is {val_q} - ({val_p}) = {dist}."
        },
        "misconception_tags": ["number_line_step_counting_error"]
    }


# ==============================================================================
# CLUSTER 2: Ordering, Comparing & Properties (11 - 20)
# ==============================================================================

def arch_11_ordering_five_integers_ascending(rng: random.Random) -> Dict[str, Any]:
    nums = rng.sample(range(-25, 25), 5)
    sorted_nums = sorted(nums)
    num_str = ", ".join(f"${n}$" for n in nums)
    ans_str = ", ".join(str(n) for n in sorted_nums)

    prompt = (
        f"Consider the following set of five integers:\n"
        f"$$\\{{ {num_str} \\}}$$\n\n"
        f"Arrange these integers in **ascending order** (from smallest to largest)."
    )
    sol = (
        f"**Step 1:** Negative numbers with larger absolute values are smaller:\n"
        f"$$\\text{{Sorted list}} = {ans_str}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans_str}$$"
    )
    return {
        "id": f"g8_int_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_ordering_five_integers_ascending",
        "hints": {
            "tier_1": "Ascending order means from smallest (most negative) to largest (most positive).",
            "tier_2": "The negative number furthest to the left on the number line comes first.",
            "tier_3": f"The ordered list is: {ans_str}."
        },
        "misconception_tags": ["negative_magnitude_ordering_reversed"]
    }


def arch_12_ordering_five_integers_descending(rng: random.Random) -> Dict[str, Any]:
    nums = rng.sample(range(-30, 30), 5)
    sorted_desc = sorted(nums, reverse=True)
    num_str = ", ".join(f"${n}$" for n in nums)
    ans_str = ", ".join(str(n) for n in sorted_desc)

    prompt = (
        f"Given the five integers:\n"
        f"$$\\{{ {num_str} \\}}$$\n\n"
        f"Arrange these integers in **descending order** (from largest to smallest)."
    )
    sol = (
        f"**Step 1:** Descending order starts with the largest positive integer and moves leftward to the smallest negative integer:\n"
        f"$$\\text{{Descending list}} = {ans_str}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans_str}$$"
    )
    return {
        "id": f"g8_int_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_ordering_five_integers_descending",
        "hints": {
            "tier_1": "Descending order starts from the greatest positive number down to the lowest negative number.",
            "tier_2": "Identify the largest positive number first.",
            "tier_3": f"The correct descending order is: {ans_str}."
        },
        "misconception_tags": ["descending_ascending_confusion"]
    }


def arch_13_comparing_integers_inequality_symbols(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(5, 30)
    b = -rng.randint(5, 30)
    while a == b:
        b = -rng.randint(5, 30)
    sym = "<" if a < b else ">"

    prompt = (
        f"Insert the correct inequality symbol ($<$, $>$, or $=$) between the two integers to make a true mathematical statement:\n\n"
        f"$${a} \\quad \\square \\quad {b}$$\n\n"
        f"Give a clear reason based on the position of the two numbers on a number line."
    )
    sol = (
        f"**Step 1:** On a horizontal number line, numbers increase from left to right.\n"
        f"Because ${a}$ lies to the {'left' if a < b else 'right'} of ${b}$, ${a} {sym} {b}$ [1 Mark: Symbol].\n\n"
        f"**Step 2:** Reason: A number with a {'greater' if abs(a) > abs(b) else 'smaller'} negative value is smaller [1 Mark: Reason].\n\n"
        f"$$\\therefore {a} {sym} {b}$$"
    )
    ans = f"{a} {sym} {b}"
    return {
        "id": f"g8_int_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_comparing_integers_inequality_symbols",
        "hints": {
            "tier_1": "Recall that numbers further to the right on a number line are greater.",
            "tier_2": f"Compare the positions of {a} and {b}.",
            "tier_3": f"{a} {sym} {b}."
        },
        "misconception_tags": ["negative_comparison_symbol_reversal"]
    }


def arch_14_absolute_value_and_distance_from_zero(rng: random.Random) -> Dict[str, Any]:
    val = -rng.randint(6, 45)
    abs_val = abs(val)

    prompt = (
        f"1. What is the distance on a number line between the integer **{val}** and **0**?\n"
        f"2. Write down the value of $|{val}|$."
    )
    sol = (
        f"**Step 1:** Distance is always a non-negative scalar quantity.\n"
        f"The distance between ${val}$ and $0$ is **{abs_val} units** [1 Mark].\n\n"
        f"**Step 2:** The absolute value function strips the direction: $|{val}| = {abs_val}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Distance}} = {abs_val}, \\quad |{val}| = {abs_val}$$"
    )
    ans = f"1. {abs_val} units; 2. {abs_val}"
    return {
        "id": f"g8_int_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_absolute_value_and_distance_from_zero",
        "hints": {
            "tier_1": "Distance from zero is the definition of absolute value.",
            "tier_2": "Absolute value is always non-negative.",
            "tier_3": f"|{val}| = {abs_val}."
        },
        "misconception_tags": ["absolute_value_negative_output"]
    }


def arch_15_opposite_integers_reflection(rng: random.Random) -> Dict[str, Any]:
    val = rng.randint(7, 35)
    neg_val = -val

    prompt = (
        f"1. State the additive inverse (opposite integer) of **{val}**.\n"
        f"2. What is the sum of **{val}** and its additive inverse?\n"
        f"3. What is the total distance between **{val}** and its opposite on a number line?"
    )
    dist = 2 * val
    sol = (
        f"**Step 1:** The additive inverse of ${val}$ is **{neg_val}** [1 Mark].\n\n"
        f"**Step 2:** The sum of any number and its additive inverse is zero: ${val} + ({neg_val}) = 0$ [1 Mark].\n\n"
        f"**Step 3:** Total distance = ${val} - ({neg_val}) = {val} + {val} = {dist}$ units [1 Mark].\n\n"
        f"$$\\therefore \\text{{Additive inverse}} = {neg_val}, \\quad \\text{{Sum}} = 0, \\quad \\text{{Distance}} = {dist}$$"
    )
    ans = f"1. {neg_val}; 2. 0; 3. {dist} units"
    return {
        "id": f"g8_int_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "15_opposite_integers_reflection",
        "hints": {
            "tier_1": "The additive inverse has the opposite sign.",
            "tier_2": "Adding a number to its opposite always yields 0.",
            "tier_3": f"Opposite of {val} is {neg_val}; distance is 2 × {val} = {dist}."
        },
        "misconception_tags": ["additive_inverse_reciprocal_confusion"]
    }


def arch_16_midpoint_between_positive_and_negative_integer(rng: random.Random) -> Dict[str, Any]:
    diff = rng.randint(3, 10) * 2
    mid = rng.randint(-6, 6)
    a = mid - diff // 2
    b = mid + diff // 2

    prompt = (
        f"Determine the exact integer that lies halfway (the midpoint) between **{a}** and **{b}** on a number line."
    )
    sol = (
        f"**Step 1:** Use the midpoint formula: $\\text{{Midpoint}} = \\frac{{a + b}}{{2}}$:\n"
        f"$$\\text{{Midpoint}} = \\frac{{({a}) + ({b})}}{{2}}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate:\n"
        f"$$\\frac{{{a + b}}}{{2}} = {mid}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{Midpoint}} = {mid}$$"
    )
    ans = str(mid)
    return {
        "id": f"g8_int_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_midpoint_between_positive_and_negative_integer",
        "hints": {
            "tier_1": "Add the two numbers together and divide by 2.",
            "tier_2": f"Calculate ({a} + {b}) / 2.",
            "tier_3": f"{a + b} / 2 = {mid}."
        },
        "misconception_tags": ["midpoint_difference_confusion"]
    }


def arch_17_consecutive_negative_integers(rng: random.Random) -> Dict[str, Any]:
    n = -rng.randint(8, 25)
    pred = n - 1
    succ = n + 1

    prompt = (
        f"For the negative integer **{n}**:\n\n"
        f"1. Write down its immediate predecessor (the integer directly to its left on a number line).\n"
        f"2. Write down its immediate successor (the integer directly to its right on a number line)."
    )
    sol = (
        f"**Step 1:** Predecessor = ${n} - 1 = {pred}$ [1 Mark].\n\n"
        f"**Step 2:** Successor = ${n} + 1 = {succ}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Predecessor}} = {pred}, \\quad \\text{{Successor}} = {succ}$$"
    )
    ans = f"1. {pred}; 2. {succ}"
    return {
        "id": f"g8_int_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_consecutive_negative_integers",
        "hints": {
            "tier_1": "To find the integer to the left, subtract 1. To find the integer to the right, add 1.",
            "tier_2": f"{n} - 1 = {pred} and {n} + 1 = {succ}.",
            "tier_3": f"Predecessor: {pred}, Successor: {succ}."
        },
        "misconception_tags": ["predecessor_successor_sign_reversal"]
    }


def arch_18_number_line_vector_jump_addition(rng: random.Random) -> Dict[str, Any]:
    start = -rng.randint(2, 6)
    jump = rng.randint(5, 10)
    end = start + jump
    jumps = [(start, end, f"+{jump}")]
    svg = draw_number_line_svg(-8, 8, step=1, jumps=jumps, label=f"Jump: {start} + {jump}")

    prompt = (
        f"Refer to the number line figure showing an arrow starting at **{start}** and moving to **{end}**.\n\n"
        f"1. Write down the integer addition equation represented by this vector jump.\n"
        f"2. State the final sum."
    )
    sol = (
        f"**Step 1:** The vector begins at ${start}$ and advances $+{jump}$ units to the right [1 Mark].\n"
        f"$$\\text{{Equation}}: ({start}) + {jump} = {end}$$\n\n"
        f"**Step 2:** Final sum is **{end}** [1 Mark].\n\n"
        f"$$\\therefore ({start}) + {jump} = {end}$$"
    )
    ans = f"1. ({start}) + {jump} = {end}; 2. {end}"
    return {
        "id": f"g8_int_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_number_line_vector_jump_addition",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "start": start, "jump": jump, "end": end},
        "hints": {
            "tier_1": "Identify the start of the arrow and the direction and length of the jump.",
            "tier_2": f"The arrow starts at {start} and jumps {jump} units right.",
            "tier_3": f"({start}) + {jump} = {end}."
        },
        "misconception_tags": ["vector_jump_direction_confusion"]
    }


def arch_19_number_line_vector_jump_subtraction(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(2, 5)
    jump = rng.randint(6, 10)
    end = start - jump
    jumps = [(start, end, f"-{jump}")]
    svg = draw_number_line_svg(-8, 8, step=1, jumps=jumps, label=f"Jump: {start} - {jump}")

    prompt = (
        f"Refer to the number line figure showing an arrow starting at **{start}** and pointing leftward to **{end}**.\n\n"
        f"1. Write down the integer subtraction equation represented by this diagram.\n"
        f"2. Explain why the result is negative."
    )
    sol = (
        f"**Step 1:** Starting at $+{start}$ and jumping ${jump}$ units leftward represents:\n"
        f"$${start} - {jump} = {end}$$ [1 Mark]\n\n"
        f"**Step 2:** The result is negative because the backward jump (${jump}$) exceeds the starting distance from zero (${start}$), ending at ${end}$ [1 Mark].\n\n"
        f"$$\\therefore {start} - {jump} = {end}$$"
    )
    ans = f"1. {start} - {jump} = {end}; 2. The subtrahend exceeds the minuend, moving past 0 to {end}."
    return {
        "id": f"g8_int_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_number_line_vector_jump_subtraction",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "start": start, "jump": jump, "end": end},
        "hints": {
            "tier_1": "Moving to the left represents subtraction on a number line.",
            "tier_2": f"Start at {start} and subtract {jump}.",
            "tier_3": f"{start} - {jump} = {end}."
        },
        "misconception_tags": ["subtraction_leftward_movement_confusion"]
    }


def arch_20_rational_and_integer_classification(rng: random.Random) -> Dict[str, Any]:
    int_sample = -rng.randint(2, 15)
    frac_sample = f"{rng.randint(1, 4)}/{rng.randint(5, 9)}"
    dec_sample = f"-{rng.randint(1, 8)}.{rng.randint(1, 9)}"
    zero_sample = "0"
    pos_sample = f"{rng.randint(12, 35)}"

    prompt = (
        f"From the following list of real numbers:\n"
        f"$$\\{{ {int_sample}, \\quad {frac_sample}, \\quad {dec_sample}, \\quad {zero_sample}, \\quad {pos_sample} \\}}$$\n\n"
        f"Identify all elements that belong to the set of integers ($\\mathbb{{Z}}$)."
    )
    integers_list = [str(int_sample), zero_sample, pos_sample]
    ans_str = ", ".join(integers_list)
    sol = (
        f"**Step 1:** The set of integers ($\\mathbb{{Z}}$) consists of whole numbers and their negative counterparts: "
        r"$\mathbb{Z} = \{ \dots, -3, -2, -1, 0, 1, 2, 3, \dots \}$." "\n\n"
        f"**Step 2:** Fractions (${frac_sample}$) and non-terminating decimals (${dec_sample}$) are non-integer rationals.\n"
        f"$$\\therefore \\text{{Integers}} = \\{{ {ans_str} \\}}$$ [2 Marks]"
    )
    return {
        "id": f"g8_int_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_rational_and_integer_classification",
        "hints": {
            "tier_1": "Integers do not contain fractional or decimal parts.",
            "tier_2": "Zero, positive whole numbers, and negative whole numbers are integers.",
            "tier_3": f"The integers are: {ans_str}."
        },
        "misconception_tags": ["fraction_classified_as_integer"]
    }


# ==============================================================================
# CLUSTER 3: Addition & Subtraction Calculations (21 - 25)
# ==============================================================================

def arch_21_addition_of_two_negative_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(12, 45)
    b = rng.randint(11, 38)
    ans = -(a + b)

    prompt = (
        f"Evaluate the following integer addition problem:\n\n"
        f"$$(-{a}) + (-{b})$$\n\n"
        f"Show your reasoning regarding signs."
    )
    sol = (
        f"**Step 1:** When adding two negative integers, add their absolute values and retain the negative sign:\n"
        f"$$(-{a}) + (-{b}) = -({a} + {b})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $-({a + b}) = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_addition_of_two_negative_integers",
        "hints": {
            "tier_1": "Adding two negative numbers gives a more negative number.",
            "tier_2": f"Add {a} + {b} and put a negative sign in front.",
            "tier_3": f"-({a} + {b}) = {ans}."
        },
        "misconception_tags": ["negative_plus_negative_positive_error"]
    }


def arch_22_addition_of_positive_and_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(15, 50)
    b = rng.randint(15, 50)
    while a == b:
        b = rng.randint(15, 50)
    pos_first = rng.choice([True, False])
    if pos_first:
        expr = f"{a} + (-{b})"
        ans = a - b
    else:
        expr = f"(-{b}) + {a}"
        ans = a - b

    prompt = (
        f"Evaluate the integer sum:\n\n"
        f"$${expr}$$\n\n"
        f"Show all working steps."
    )
    sol = (
        f"**Step 1:** Adding a negative integer is equivalent to subtraction:\n"
        f"$${expr} = {a} - {b}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: ${a} - {b} = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_addition_of_positive_and_negative_integer",
        "hints": {
            "tier_1": "Adding a negative number is the same as subtracting.",
            "tier_2": f"Rewrite as {a} - {b}.",
            "tier_3": f"{a} - {b} = {ans}."
        },
        "misconception_tags": ["positive_negative_addition_sign_confusion"]
    }


def arch_23_subtraction_of_positive_from_smaller_positive(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(25, 60)
    diff = rng.randint(7, 24)
    a = b - diff
    ans = -diff

    prompt = (
        f"Calculate the value of:\n\n"
        f"$${a} - {b}$$"
    )
    sol = (
        f"**Step 1:** Subtracting a larger positive integer from a smaller one yields a negative integer:\n"
        f"$${a} - {b} = -({b} - {a})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $-({b - a}) = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_subtraction_of_positive_from_smaller_positive",
        "hints": {
            "tier_1": "Since you are subtracting a larger number from a smaller one, the result is negative.",
            "tier_2": f"Find the difference ({b} - {a}) and add a minus sign.",
            "tier_3": f"{a} - {b} = {ans}."
        },
        "misconception_tags": ["subtraction_order_inversion_error"]
    }


def arch_24_subtraction_of_positive_from_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(14, 48)
    b = rng.randint(12, 35)
    ans = -(a + b)

    prompt = (
        f"Evaluate the following expression:\n\n"
        f"$$(-{a}) - {b}$$"
    )
    sol = (
        f"**Step 1:** Subtracting a positive number from a negative number moves further left on the number line:\n"
        f"$$(-{a}) - {b} = -({a} + {b})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $-({a + b}) = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_subtraction_of_positive_from_negative",
        "hints": {
            "tier_1": "Starting at a negative number and subtracting makes it more negative.",
            "tier_2": f"Combine {a} and {b} with a negative sign: -({a} + {b}).",
            "tier_3": f"-{a} - {b} = {ans}."
        },
        "misconception_tags": ["negative_minus_positive_confusion"]
    }


def arch_25_subtraction_of_negative_double_negative_rule(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(15, 60)
    b = rng.randint(12, 45)
    ans = a + b

    prompt = (
        f"Evaluate the expression showing the application of the double-negative sign rule:\n\n"
        f"$${a} - (-{b})$$"
    )
    sol = (
        f"**Step 1:** Apply the rule that subtracting a negative number is equivalent to adding its opposite:\n"
        f"$$-(-{b}) = +{b}$$\n"
        f"$${a} - (-{b}) = {a} + {b}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: ${a} + {b} = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_subtraction_of_negative_double_negative_rule",
        "hints": {
            "tier_1": "Two negative signs in a row (-(-b)) turn into a plus sign.",
            "tier_2": f"Rewrite {a} - (-{b}) as {a} + {b}.",
            "tier_3": f"{a} + {b} = {ans}."
        },
        "misconception_tags": ["double_negative_rule_forgotten"]
    }
