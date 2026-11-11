"""
Grade 7 Mathematics - Integers Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_thermometer_svg, draw_number_line_svg, draw_elevation_profile_svg

SA_CITIES = [
    ("Sutherland", -6, 12),
    ("Bethlehem", -4, 15),
    ("Bloemfontein", -3, 17),
    ("Johannesburg", 2, 19),
    ("Underberg", -5, 13),
    ("Standerton", -4, 16),
    ("Kimberley", 0, 20),
]


# ==============================================================================
# CLUSTER 1: Thermometers & Temperature Contexts (01 - 08)
# ==============================================================================

def arch_01_reading_thermometer_above_zero(rng: random.Random) -> Dict[str, Any]:
    temp = rng.randint(8, 38)
    city, _, _ = rng.choice(SA_CITIES)
    svg = draw_thermometer_svg(temp, min_t=-20, max_t=50, show_reading=False, label=f"Weather Station: {city}")

    prompt = (
        f"A laboratory thermometer placed in a weather station in **{city}** shows the reading below.\n\n"
        f"1. Read and write down the temperature shown on the thermometer scale in degrees Celsius ($^\\circ\\text{{C}}$).\n"
        f"2. State whether this integer is positive or negative."
    )
    sol = (
        f"**Step 1:** Observe the top of the mercury/alcohol column against the vertical scale.\n\n"
        f"The liquid level aligns with the **{temp}^\\circ\\text{{C}}** calibration mark [1 Mark: Method].\n\n"
        f"**Step 2:** Because the value is above the $0^\\circ\\text{{C}}$ freezing mark, it is a **positive integer** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\text{{Reading}} = +{temp}^\\circ\\text{{C}} \\text{{ (Positive)}}$$"
    )
    return {
        "id": f"g7_int_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"+{temp}°C (Positive)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "01_reading_thermometer_above_zero",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "temp": temp, "city": city},
        "hints": {
            "tier_1": "Look at the level of the liquid column and compare it with the tick marks on the scale.",
            "tier_2": f"Find 0°C on the scale and count upwards in steps of 10°C.",
            "tier_3": f"The top of the liquid is exactly at {temp}°C, which is a positive integer."
        }
    }


def arch_02_reading_thermometer_below_zero(rng: random.Random) -> Dict[str, Any]:
    temp = -rng.randint(2, 18)
    city, _, _ = rng.choice([c for c in SA_CITIES if c[1] < 0])
    svg = draw_thermometer_svg(temp, min_t=-30, max_t=40, show_reading=False, label=f"Winter Reading: {city}")

    prompt = (
        f"During a cold winter night in **{city}**, an outdoor thermometer displays the mercury level shown below.\n\n"
        f"1. Read and write down the exact temperature shown in degrees Celsius ($^\\circ\\text{{C}}$).\n"
        f"2. Write down the additive inverse of this temperature."
    )
    inverse = -temp
    sol = (
        f"**Step 1:** The liquid level is below the $0^\\circ\\text{{C}}$ benchmark line.\n\n"
        f"Reading the scale downwards from $0$, the level rests at **{temp}^\\circ\\text{{C}}** [1 Mark: Method].\n\n"
        f"**Step 2:** The additive inverse of a negative integer $-a$ is its opposite $+a$ such that $(-a) + a = 0$.\n\n"
        f"$$\\text{{Additive inverse of }} ({temp}) = +{inverse}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Reading = {temp}°C; Additive inverse = +{inverse}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_reading_thermometer_below_zero",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "temp": temp, "city": city},
        "hints": {
            "tier_1": "Notice that the liquid column is below 0°C, so the temperature must be a negative integer.",
            "tier_2": f"Count down from 0°C to find {temp}°C. The additive inverse has the opposite sign.",
            "tier_3": f"Reading is {temp}°C, and its additive inverse is +{inverse}°C."
        }
    }


def arch_03_temperature_rise_from_negative_to_positive(rng: random.Random) -> Dict[str, Any]:
    t_start = -rng.randint(3, 9)
    t_rise = rng.randint(t_start + 12, t_start + 24)
    t_end = t_start + t_rise
    city, _, _ = rng.choice(SA_CITIES)
    svg = draw_number_line_svg(min_val=t_start - 3, max_val=t_end + 3, step=2, jumps=[(t_start, t_end, f"+{t_rise}°C")], label=f"Temperature Rise: {city}")

    prompt = (
        f"At 05:00 in **{city}**, the thermometer read **{t_start}^\\circ\\text{{C}}**.\n\n"
        f"By 13:00, the temperature had **risen by {t_rise}^\\circ\\text{{C}}**.\n\n"
        f"1. Write down an integer addition expression to calculate the new temperature.\n"
        f"2. Calculate the afternoon temperature at 13:00."
    )
    sol = (
        f"**Step 1:** Model the temperature rise as integer addition:\n\n"
        f"$$\\text{{New Temperature}} = ({t_start}) + {t_rise} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute the sum:\n\n"
        f"$$({t_start}) + {t_rise} = {t_end}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Afternoon temperature}} = {t_end}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"({t_start}) + {t_rise} = {t_end}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_temperature_rise_from_negative_to_positive",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "t_start": t_start, "t_end": t_end, "t_rise": t_rise},
        "hints": {
            "tier_1": "Rising by a positive temperature means you add that number to the starting temperature.",
            "tier_2": f"Start at {t_start} on the number line and jump to the right by {t_rise} units.",
            "tier_3": f"({t_start}) + {t_rise} = {t_end}°C."
        }
    }


def arch_04_temperature_drop_from_positive_to_negative(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.randint(4, 12)
    t_drop = rng.randint(t_start + 5, t_start + 15)
    t_end = t_start - t_drop
    city, _, _ = rng.choice(SA_CITIES)
    svg = draw_number_line_svg(min_val=t_end - 3, max_val=t_start + 3, step=2, jumps=[(t_start, t_end, f"-{t_drop}°C")], label=f"Cold Front Drop: {city}")

    prompt = (
        f"In **{city}**, the afternoon temperature was **{t_start}^\\circ\\text{{C}}**.\n\n"
        f"A severe cold front caused the temperature to **drop by {t_drop}^\\circ\\text{{C}}** by midnight.\n\n"
        f"1. Write down an integer subtraction statement for this drop.\n"
        f"2. Calculate the midnight temperature in degrees Celsius."
    )
    sol = (
        f"**Step 1:** Model the temperature drop:\n\n"
        f"$$\\text{{Midnight Temperature}} = {t_start} - {t_drop} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate the resulting negative integer:\n\n"
        f"$${t_start} - {t_drop} = {t_end}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Midnight temperature}} = {t_end}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t_start} - {t_drop} = {t_end}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_temperature_drop_from_positive_to_negative",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "t_start": t_start, "t_drop": t_drop, "t_end": t_end},
        "hints": {
            "tier_1": "Dropping means subtracting the amount of change from the initial value.",
            "tier_2": f"Since {t_drop} is greater than {t_start}, the answer must be below 0°C.",
            "tier_3": f"{t_start} - {t_drop} = {t_end}°C."
        }
    }


def arch_05_temperature_difference_two_south_african_cities(rng: random.Random) -> Dict[str, Any]:
    c1, min_t, _ = rng.choice([c for c in SA_CITIES if c[1] < 0])
    c2 = rng.choice(["Durban", "Cape Town", "Mbombela", "East London"])
    t1 = -rng.randint(3, 8)
    t2 = rng.randint(14, 22)
    diff = t2 - t1
    svg = draw_number_line_svg(min_val=t1 - 2, max_val=t2 + 2, step=4, markers={t1: c1[:4], t2: c2[:4]}, label=f"Comparison: {c1} vs {c2}")

    prompt = (
        f"At 06:00 on a winter morning, the recorded temperature in **{c1}** was **{t1}^\\circ\\text{{C}}**, "
        f"while in **{c2}** the temperature was **{t2}^\\circ\\text{{C}}**.\n\n"
        f"1. Write down an integer expression: $(\\text{{Higher temperature}}) - (\\text{{Lower temperature}})$.\n"
        f"2. Calculate the difference in temperature between the two towns."
    )
    sol = (
        f"**Step 1:** Set up the difference expression:\n\n"
        f"$$\\text{{Difference}} = {t2} - ({t1}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Subtracting a negative number is equivalent to adding its opposite:\n\n"
        f"$${t2} - ({t1}) = {t2} + {abs(t1)} = {diff}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Difference}} = {diff}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t2} - ({t1}) = {diff}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_temperature_difference_two_south_african_cities",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "t1": t1, "t2": t2, "diff": diff},
        "hints": {
            "tier_1": "To find the difference between two values, subtract the smaller value from the larger value.",
            "tier_2": f"Subtracting ({t1}) turns into adding {abs(t1)}.",
            "tier_3": f"{t2} - ({t1}) = {t2} + {abs(t1)} = {diff}°C."
        }
    }


def arch_06_coldest_to_warmest_temperature_ranking(rng: random.Random) -> Dict[str, Any]:
    towns = [("Sutherland", -rng.randint(5, 8)), ("Bethlehem", -rng.randint(2, 4)), ("Johannesburg", rng.randint(1, 4)), ("Pretoria", rng.randint(6, 9)), ("Durban", rng.randint(14, 18))]
    rng.shuffle(towns)
    town_strs = ", ".join(f"**{t[0]}** ({t[1]}^\\circ\\text{{C}})" for t in towns)
    sorted_towns = sorted(towns, key=lambda x: x[1])
    ans_str = "; ".join(f"{t[0]} ({t[1]}°C)" for t in sorted_towns)

    prompt = (
        f"The Weather Bureau recorded the following 06:00 winter temperatures in South African towns:\n\n"
        f"{town_strs}\n\n"
        f"Arrange the towns in order from **coldest to warmest**."
    )
    sol = (
        f"**Step 1:** On a number line, more negative numbers lie further to the left and represent colder temperatures.\n\n"
        f"Comparing the integers: ${' < '.join(str(t[1]) for t in sorted_towns)}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Order from coldest (lowest integer) to warmest (highest integer):\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_coldest_to_warmest_temperature_ranking",
        "hints": {
            "tier_1": "The colder the temperature, the further to the left it is on the number line.",
            "tier_2": "Rank negative numbers with the largest absolute value first.",
            "tier_3": f"Correct order: {ans_str}."
        }
    }


def arch_07_diurnal_temperature_range_calculation(rng: random.Random) -> Dict[str, Any]:
    city, _, _ = rng.choice([c for c in SA_CITIES if c[1] < 0])
    t_min = -rng.randint(4, 9)
    t_max = rng.randint(11, 18)
    r_val = t_max - t_min

    prompt = (
        f"In **{city}**, the minimum temperature recorded at sunrise was **{t_min}^\\circ\\text{{C}}**.\n\n"
        f"By mid-afternoon, the maximum temperature reached **{t_max}^\\circ\\text{{C}}**.\n\n"
        f"Calculate the diurnal temperature range ($T_{{\\text{{max}}}} - T_{{\\text{{min}}}}$) for that day."
    )
    sol = (
        f"**Step 1:** Formula for temperature range:\n\n"
        f"$$\\text{{Range}} = T_{{\\text{{max}}}} - T_{{\\text{{min}}}} = {t_max} - ({t_min}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Simplify double negative:\n\n"
        f"$${t_max} - ({t_min}) = {t_max} + {abs(t_min)} = {r_val}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Diurnal range}} = {r_val}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r_val}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_diurnal_temperature_range_calculation",
        "hints": {
            "tier_1": "Range is always Maximum minus Minimum.",
            "tier_2": f"Subtracting ({t_min}) is the same as adding {abs(t_min)}.",
            "tier_3": f"{t_max} - ({t_min}) = {r_val}°C."
        }
    }


def arch_08_wind_chill_effective_temperature_subtraction(rng: random.Random) -> Dict[str, Any]:
    t_air = -rng.randint(1, 5)
    w_drop = rng.randint(6, 12)
    t_eff = t_air - w_drop

    prompt = (
        f"On the Sani Pass mountain summit, the air temperature is **{t_air}^\\circ\\text{{C}}**.\n\n"
        f"Due to high winds, the wind-chill effect causes the apparent temperature to **drop by {w_drop}^\\circ\\text{{C}}**.\n\n"
        f"Calculate the effective wind-chill temperature felt by hikers."
    )
    sol = (
        f"**Step 1:** Write down the expression:\n\n"
        f"$$\\text{{Effective Temperature}} = ({t_air}) - {w_drop} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Subtracting a positive number from a negative number moves further left into negative integers:\n\n"
        f"$$({t_air}) - {w_drop} = {t_eff}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Effective temperature}} = {t_eff}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t_eff}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_wind_chill_effective_temperature_subtraction",
        "hints": {
            "tier_1": "Start at the air temperature and subtract the wind-chill drop.",
            "tier_2": f"Moving {w_drop} units left from {t_air} gives a larger negative value.",
            "tier_3": f"({t_air}) - {w_drop} = {t_eff}°C."
        }
    }


# ==============================================================================
# CLUSTER 2: Financial Contexts (09 - 16)
# ==============================================================================

def arch_09_bank_overdraft_balance_after_withdrawal(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Sipho", "Naledi", "Thabo", "Kagiso", "Zola"])
    start_bal = rng.randint(120, 280)
    withdraw = start_bal + rng.randint(150, 350)
    overdrawn = start_bal - withdraw

    prompt = (
        f"**{name}** has a bank account balance of **R{start_bal}**.\n\n"
        f"The bank allows an overdraft facility, and {name} withdraws **R{withdraw}** to pay for school textbooks.\n\n"
        f"1. Write down an integer expression modeling this transaction.\n"
        f"2. Calculate {name}'s new account balance (using a negative integer to represent debt)."
    )
    sol = (
        f"**Step 1:** Model the withdrawal:\n\n"
        f"$$\\text{{New Balance}} = {start_bal} - {withdraw} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute the negative balance:\n\n"
        f"$${start_bal} - {withdraw} = -\\text{{R}}{abs(overdrawn)} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{{name} is overdrawn by R{abs(overdrawn)} (Balance: -R{abs(overdrawn)})}}$$"
    )
    return {
        "id": f"g7_int_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"-R{abs(overdrawn)}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_bank_overdraft_balance_after_withdrawal",
        "hints": {
            "tier_1": "Subtract the withdrawal amount from the starting balance.",
            "tier_2": f"Since {withdraw} > {start_bal}, the result will be a negative number.",
            "tier_3": f"{start_bal} - {withdraw} = -R{abs(overdrawn)}."
        }
    }


def arch_10_deposit_into_overdrawn_account(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Lindiwe", "Bongani", "Ayanda", "Farai", "Sindi"])
    overdraft = rng.randint(220, 480)
    deposit = overdraft + rng.randint(100, 300)
    final_bal = -overdraft + deposit

    prompt = (
        f"**{name}'s** bank account is overdrawn with a balance of **-R{overdraft}**.\n\n"
        f"{name} deposits **R{deposit}** into the account.\n\n"
        f"1. Write an integer addition statement to model the deposit.\n"
        f"2. Calculate {name}'s new bank balance."
    )
    sol = (
        f"**Step 1:** Model the deposit:\n\n"
        f"$$\\text{{New Balance}} = (-{overdraft}) + {deposit} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate final positive balance:\n\n"
        f"$$(-{overdraft}) + {deposit} = +\\text{{R}}{final_bal} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Balance is +R{final_bal}}}$$"
    )
    return {
        "id": f"g7_int_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"+R{final_bal}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_deposit_into_overdrawn_account",
        "hints": {
            "tier_1": "Adding money to an overdrawn account reduces the debt.",
            "tier_2": f"(-{overdraft}) + {deposit} is equivalent to {deposit} - {overdraft}.",
            "tier_3": f"Final balance is +R{final_bal}."
        }
    }


def arch_11_business_profit_and_loss_net_position(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Mandla", "Fatima", "Karabo", "Lerato"])
    income = rng.randint(450, 750)
    expenses = income + rng.randint(80, 220)
    net_loss = income - expenses

    prompt = (
        f"**{name}** operates a tuckshop. On Friday, the tuckshop earned **R{income}** in sales income, "
        f"but incurred stock expenses and transport costs totaling **R{expenses}**.\n\n"
        f"1. Write an expression: $(\\text{{Income}}) - (\\text{{Expenses}})$.\n"
        f"2. State whether {name} made a net profit or net loss, and express the result as an integer."
    )
    sol = (
        f"**Step 1:** Calculate net position:\n\n"
        f"$$\\text{{Net Position}} = {income} - {expenses} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Evaluate result:\n\n"
        f"$${income} - {expenses} = -\\text{{R}}{abs(net_loss)} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Net loss of R{abs(net_loss)} (-R{abs(net_loss)})}}$$"
    )
    return {
        "id": f"g7_int_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Net loss of R{abs(net_loss)} (-R{abs(net_loss)})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_business_profit_and_loss_net_position",
        "hints": {
            "tier_1": "Net position = Income minus Expenses.",
            "tier_2": "When expenses exceed income, the business has a net loss (negative integer).",
            "tier_3": f"{income} - {expenses} = -R{abs(net_loss)}."
        }
    }


def arch_12_debt_settlement_multi_creditor_calculation(rng: random.Random) -> Dict[str, Any]:
    debt1 = rng.randint(40, 90)
    debt2 = rng.randint(60, 110)
    cash = rng.randint(debt1 + debt2 + 50, debt1 + debt2 + 150)
    rem = cash - debt1 - debt2

    prompt = (
        f"A learner owes **R{debt1}** to Friend A and **R{debt2}** to Friend B.\n\n"
        f"The learner receives **R{cash}** for completing garden chores.\n\n"
        f"1. Write an integer arithmetic statement showing the cash earned minus both debts.\n"
        f"2. Calculate the money the learner has left after paying both friends in full."
    )
    sol = (
        f"**Step 1:** Total debt is $(-{debt1}) + (-{debt2}) = -\\text{{R}}{debt1 + debt2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Remaining cash:\n\n"
        f"$${cash} - {debt1} - {debt2} = +\\text{{R}}{rem} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Learner has +R{rem} remaining}}$$"
    )
    return {
        "id": f"g7_int_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"+R{rem}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_debt_settlement_multi_creditor_calculation",
        "hints": {
            "tier_1": "Sum both debts and subtract them from the cash earned.",
            "tier_2": f"Total debt = {debt1} + {debt2} = {debt1 + debt2}.",
            "tier_3": f"{cash} - {debt1 + debt2} = R{rem}."
        }
    }


def arch_13_stock_market_point_gain_and_drop(rng: random.Random) -> Dict[str, Any]:
    g1 = rng.randint(45, 95)
    d1 = rng.randint(110, 180)
    net_pts = g1 - d1

    prompt = (
        f"On Monday morning, the JSE All-Share index opened at neutral ($0$ points change).\n\n"
        f"By midday, it had **gained {g1} points**, but by the closing bell, it had **dropped by {d1} points** from its midday peak.\n\n"
        f"Calculate the final closing position in points relative to the morning opening."
    )
    sol = (
        f"**Step 1:** Model index change:\n\n"
        f"$$\\text{{Net Change}} = (+{g1}) - {d1} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute net integer:\n\n"
        f"$${g1} - {d1} = {net_pts} \\text{{ points [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{The index closed at {net_pts} points}}$$"
    )
    return {
        "id": f"g7_int_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{net_pts} points",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_stock_market_point_gain_and_drop",
        "hints": {
            "tier_1": "Gains are positive (+), drops are negative (-).",
            "tier_2": f"{g1} - {d1} gives the net points change.",
            "tier_3": f"Net position is {net_pts} points."
        }
    }


def arch_14_budget_deficit_and_surplus_comparison(rng: random.Random) -> Dict[str, Any]:
    month1_surplus = rng.randint(140, 260)
    month2_deficit = -rng.randint(80, 190)
    diff = month1_surplus - month2_deficit

    prompt = (
        f"In Term 1, a school club recorded a **surplus of +R{month1_surplus}**.\n\n"
        f"In Term 2, due to unexpected costs, the club recorded a **deficit of -R{abs(month2_deficit)}**.\n\n"
        f"Calculate the difference between the Term 1 surplus and the Term 2 deficit: $(+\\text{{R}}{month1_surplus}) - (-\\text{{R}}{abs(month2_deficit)})$."
    )
    sol = (
        f"**Step 1:** Set up subtraction:\n\n"
        f"$$\\text{{Difference}} = {month1_surplus} - ({month2_deficit}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Subtracting a negative integer becomes addition:\n\n"
        f"$${month1_surplus} - ({month2_deficit}) = {month1_surplus} + {abs(month2_deficit)} = \\text{{R}}{diff} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Difference}} = \\text{{R}}{diff}$$"
    )
    return {
        "id": f"g7_int_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_budget_deficit_and_surplus_comparison",
        "hints": {
            "tier_1": "Surplus is positive (+), deficit is negative (-).",
            "tier_2": f"Subtracting ({month2_deficit}) turns into adding {abs(month2_deficit)}.",
            "tier_3": f"{month1_surplus} - ({month2_deficit}) = R{diff}."
        }
    }


def arch_15_combined_cash_assets_and_supplier_debts(rng: random.Random) -> Dict[str, Any]:
    cash = rng.randint(180, 320)
    owed_by_clients = rng.randint(90, 210)
    owed_to_suppliers = cash + owed_by_clients + rng.randint(60, 180)
    net_val = cash + owed_by_clients - owed_to_suppliers

    prompt = (
        f"Fatima owns a small tuckshop. At the end of the day:\n\n"
        f"- Cash in till: **R{cash}**\n"
        f"- Money owed to Fatima by regular clients: **R{owed_by_clients}**\n"
        f"- Money Fatima owes to her wholesale bread supplier: **R{owed_to_suppliers}**\n\n"
        f"Calculate Fatima's net financial position: $\\text{{Cash}} + \\text{{Clients}} - \\text{{Suppliers}}$."
    )
    sol = (
        f"**Step 1:** Add cash assets and customer receivables:\n\n"
        f"$${cash} + {owed_by_clients} = \\text{{R}}{cash + owed_by_clients} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Deduct supplier debt:\n\n"
        f"$${cash + owed_by_clients} - {owed_to_suppliers} = -\\text{{R}}{abs(net_val)} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Net financial position}} = -\\text{{R}}{abs(net_val)} \\text{{ (Deficit)}}$$"
    )
    return {
        "id": f"g7_int_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"-R{abs(net_val)}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_combined_cash_assets_and_supplier_debts",
        "hints": {
            "tier_1": "Add what you have and what you are owed, then subtract what you owe.",
            "tier_2": f"Assets = {cash + owed_by_clients}, Liabilities = {owed_to_suppliers}.",
            "tier_3": f"Net position = -R{abs(net_val)}."
        }
    }


def arch_16_net_worth_negative_equity_assessment(rng: random.Random) -> Dict[str, Any]:
    assets = rng.randint(1200, 2400)
    debts = assets + rng.randint(300, 800)
    net_equity = assets - debts

    prompt = (
        f"A young entrepreneur's small delivery service has assets worth **R{assets}** and debts of **R{debts}**.\n\n"
        f"1. Write down an equation for Net Worth: $\\text{{Net Worth}} = \\text{{Assets}} - \\text{{Debts}}$.\n"
        f"2. Calculate the entrepreneur's net worth as an integer."
    )
    sol = (
        f"**Step 1:** Apply Net Worth formula:\n\n"
        f"$$\\text{{Net Worth}} = {assets} - {debts} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute result:\n\n"
        f"$${assets} - {debts} = -\\text{{R}}{abs(net_equity)} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Net worth is -R{abs(net_equity)} (Negative equity)}}$$"
    )
    return {
        "id": f"g7_int_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"-R{abs(net_equity)}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_net_worth_negative_equity_assessment",
        "hints": {
            "tier_1": "Subtract debts from assets.",
            "tier_2": f"Debts (R{debts}) exceed assets (R{assets}), giving negative equity.",
            "tier_3": f"Net worth = -R{abs(net_equity)}."
        }
    }


# ==============================================================================
# CLUSTER 3: Elevation & Sea Level (17 - 24)
# ==============================================================================

def arch_17_submarine_depth_and_ascent_distance(rng: random.Random) -> Dict[str, Any]:
    depth = -rng.randint(80, 240)
    ascent = rng.randint(30, abs(depth) - 10)
    new_depth = depth + ascent
    svg = draw_elevation_profile_svg(surface_elev=0, points=[("Initial Depth", depth, "#dc2626"), ("New Depth", new_depth, "#2563eb")])

    prompt = (
        f"A South African Navy submarine is cruising at a depth of **{depth} m** relative to sea level ($0$ m).\n\n"
        f"The commander orders the submarine to **ascend by {ascent} m**.\n\n"
        f"1. Write down an integer addition statement modeling this ascent.\n"
        f"2. Calculate the submarine's new depth."
    )
    sol = (
        f"**Step 1:** Model the ascent as adding a positive elevation:\n\n"
        f"$$\\text{{New Depth}} = ({depth}) + {ascent} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute depth:\n\n"
        f"$$({depth}) + {ascent} = {new_depth} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{The new depth is }} {new_depth} \\text{{ m (or }} {abs(new_depth)} \\text{{ m below sea level)}}$$"
    )
    return {
        "id": f"g7_int_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{new_depth} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_submarine_depth_and_ascent_distance",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "depth": depth, "ascent": ascent, "new_depth": new_depth},
        "hints": {
            "tier_1": "Depths below sea level are represented as negative numbers.",
            "tier_2": f"Ascending means moving upwards (+{ascent} m).",
            "tier_3": f"({depth}) + {ascent} = {new_depth} m."
        }
    }


def arch_18_deep_mine_shaft_elevation_below_surface(rng: random.Random) -> Dict[str, Any]:
    surf = rng.randint(1400, 1750)  # Highveld surface elevation above sea level
    shaft_depth = rng.randint(2100, 3200)
    base_elev = surf - shaft_depth
    svg = draw_elevation_profile_svg(surface_elev=surf, points=[("Surface", surf, "#059669"), ("Base", base_elev, "#dc2626")])

    prompt = (
        f"A gold mine shaft in Carletonville has its surface entrance at **+{surf} m** above sea level.\n\n"
        f"The main vertical shaft descends **{shaft_depth} m** straight down into the Earth.\n\n"
        f"Calculate the elevation of the bottom of the shaft relative to sea level."
    )
    sol = (
        f"**Step 1:** Subtract the depth descended from surface elevation:\n\n"
        f"$$\\text{{Base Elevation}} = {surf} - {shaft_depth} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Evaluate integer:\n\n"
        f"$${surf} - {shaft_depth} = {base_elev} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Bottom of shaft is at }} {base_elev} \\text{{ m (i.e. }} {abs(base_elev)} \\text{{ m below sea level)}}$$"
    )
    return {
        "id": f"g7_int_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base_elev} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_deep_mine_shaft_elevation_below_surface",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "surf": surf, "base_elev": base_elev},
        "hints": {
            "tier_1": "Start at the surface elevation and subtract the depth of the shaft.",
            "tier_2": f"Since {shaft_depth} > {surf}, the bottom is below sea level (negative).",
            "tier_3": f"{surf} - {shaft_depth} = {base_elev} m."
        }
    }


def arch_19_diver_depth_relative_to_sea_level(rng: random.Random) -> Dict[str, Any]:
    d1 = -rng.randint(8, 22)
    descent = rng.randint(5, 18)
    d_total = d1 - descent

    prompt = (
        f"A scuba diver exploring Sodwana Bay is at a depth of **{d1} m** relative to the water surface ($0$ m).\n\n"
        f"The diver then descends an additional **{descent} m** to inspect a coral reef ledge.\n\n"
        f"Calculate the diver's new depth relative to sea level."
    )
    sol = (
        f"**Step 1:** Model descending deeper from an existing depth:\n\n"
        f"$$\\text{{New Depth}} = ({d1}) - {descent} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute combined negative depth:\n\n"
        f"$$({d1}) - {descent} = {d_total} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{The diver is at }} {d_total} \\text{{ m (or }} {abs(d_total)} \\text{{ m below surface)}}$$"
    )
    return {
        "id": f"g7_int_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{d_total} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_diver_depth_relative_to_sea_level",
        "hints": {
            "tier_1": "Descending deeper moves further down into negative numbers.",
            "tier_2": f"({d1}) - {descent} = {d_total}.",
            "tier_3": f"Final depth is {d_total} m."
        }
    }


def arch_20_altitude_drop_from_mountain_peak_to_trench(rng: random.Random) -> Dict[str, Any]:
    peak = rng.randint(2800, 3450)  # Drakensberg summit
    trench = -rng.randint(450, 1200)  # Oceanic canyon
    total_drop = peak - trench

    prompt = (
        f"Mafadi peak in the Drakensberg stands at **+{peak} m** above sea level.\n\n"
        f"Off the coast of KwaZulu-Natal, the Tugela submarine canyon plunges to **{trench} m** below sea level.\n\n"
        f"Calculate the total vertical height difference between the mountain summit and the canyon floor."
    )
    sol = (
        f"**Step 1:** Vertical difference formula: $\\text{{Higher}} - \\text{{Lower}}$:\n\n"
        f"$$\\text{{Difference}} = {peak} - ({trench}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Subtracting a negative integer adds its absolute value:\n\n"
        f"$${peak} - ({trench}) = {peak} + {abs(trench)} = {total_drop} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Total vertical difference}} = {total_drop} \\text{{ m}}$$"
    )
    return {
        "id": f"g7_int_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total_drop} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_altitude_drop_from_mountain_peak_to_trench",
        "hints": {
            "tier_1": "Subtract the lower elevation from the higher elevation.",
            "tier_2": f"Subtracting ({trench}) turns into adding {abs(trench)}.",
            "tier_3": f"{peak} - ({trench}) = {total_drop} m."
        }
    }


def arch_21_vertical_distance_between_two_elevations(rng: random.Random) -> Dict[str, Any]:
    e1 = -rng.randint(30, 80)
    e2 = rng.randint(120, 240)
    dist = e2 - e1

    prompt = (
        f"An underground metro station is located at **{e1} m** relative to ground street level ($0$ m).\n\n"
        f"A communication tower above the station stands at **+{e2} m** above ground level.\n\n"
        f"Calculate the total vertical distance between the underground platform and the top of the tower."
    )
    sol = (
        f"**Step 1:** Calculate vertical span:\n\n"
        f"$$\\text{{Distance}} = {e2} - ({e1}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Simplify double negative:\n\n"
        f"$${e2} - ({e1}) = {e2} + {abs(e1)} = {dist} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Vertical distance}} = {dist} \\text{{ m}}$$"
    )
    return {
        "id": f"g7_int_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{dist} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_vertical_distance_between_two_elevations",
        "hints": {
            "tier_1": "Vertical distance is high elevation minus low elevation.",
            "tier_2": f"{e2} - ({e1}) = {e2} + {abs(e1)}.",
            "tier_3": f"Total distance is {dist} m."
        }
    }


def arch_22_underground_parking_basement_levels(rng: random.Random) -> Dict[str, Any]:
    start_fl = rng.randint(3, 8)
    down_levels = start_fl + rng.randint(1, 4)
    final_fl = start_fl - down_levels

    prompt = (
        f"A shopping mall elevator is currently on **Floor +{start_fl}**.\n\n"
        f"The elevator moves **down {down_levels} floors** to the underground parking garage.\n\n"
        f"1. Write an integer subtraction statement for this elevator movement.\n"
        f"2. What basement level number (represented as a negative integer) does the elevator arrive at?"
    )
    sol = (
        f"**Step 1:** Model movement:\n\n"
        f"$$\\text{{Final Floor}} = {start_fl} - {down_levels} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute floor level:\n\n"
        f"$${start_fl} - {down_levels} = {final_fl} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Elevator arrives at Floor {final_fl} (Basement Level {abs(final_fl)})}}$$"
    )
    return {
        "id": f"g7_int_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Floor {final_fl} (Basement {abs(final_fl)})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_underground_parking_basement_levels",
        "hints": {
            "tier_1": "Moving down floors means subtracting.",
            "tier_2": f"{start_fl} - {down_levels} takes the elevator below ground level 0.",
            "tier_3": f"Arrival floor is {final_fl}."
        }
    }


def arch_23_drone_altitude_relative_to_cliff_edge(rng: random.Random) -> Dict[str, Any]:
    h_up = rng.randint(45, 95)
    descent = h_up + rng.randint(60, 140)
    final_pos = h_up - descent

    prompt = (
        f"A surveyor launches a drone from a cliff edge defined as $0$ m elevation.\n\n"
        f"The drone climbs **+{h_up} m** straight up to take aerial photos, then descends **{descent} m** into the valley below the cliff.\n\n"
        f"Calculate the drone's position relative to the cliff edge."
    )
    sol = (
        f"**Step 1:** Model position change:\n\n"
        f"$$\\text{{Position}} = (+{h_up}) - {descent} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate integer value:\n\n"
        f"$${h_up} - {descent} = {final_pos} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Drone is at }} {final_pos} \\text{{ m (or }} {abs(final_pos)} \\text{{ m below cliff edge)}}$$"
    )
    return {
        "id": f"g7_int_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{final_pos} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_drone_altitude_relative_to_cliff_edge",
        "hints": {
            "tier_1": "Climbing is positive, descending is negative.",
            "tier_2": f"{h_up} - {descent} = {final_pos}.",
            "tier_3": f"Position is {final_pos} m relative to cliff edge."
        }
    }


def arch_24_cave_exploration_descent_and_climb(rng: random.Random) -> Dict[str, Any]:
    d_initial = -rng.randint(40, 110)
    climb = rng.randint(15, abs(d_initial) - 5)
    final_d = d_initial + climb

    prompt = (
        f"A spelunker in the Sterkfontein Caves is exploring a cavern at **{d_initial} m** relative to the cave entrance ($0$ m).\n\n"
        f"The spelunker climbs up an internal rock face by **+{climb} m**.\n\n"
        f"Calculate the spelunker's new elevation relative to the cave entrance."
    )
    sol = (
        f"**Step 1:** Model climb:\n\n"
        f"$$\\text{{Elevation}} = ({d_initial}) + {climb} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate result:\n\n"
        f"$$({d_initial}) + {climb} = {final_d} \\text{{ m [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{New elevation is }} {final_d} \\text{{ m (or }} {abs(final_d)} \\text{{ m below entrance)}}$$"
    )
    return {
        "id": f"g7_int_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{final_d} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_cave_exploration_descent_and_climb",
        "hints": {
            "tier_1": "Add the climb (+ elevation) to the initial negative depth.",
            "tier_2": f"({d_initial}) + {climb} reduces the depth.",
            "tier_3": f"New elevation is {final_d} m."
        }
    }


# ==============================================================================
# CLUSTER 4: Number Lines, Ordering & Comparing (25)
# ==============================================================================

def arch_25_identifying_missing_integers_on_number_line(rng: random.Random) -> Dict[str, Any]:
    step = rng.choice([1, 2, 5])
    min_v = -10 * step
    max_v = 10 * step
    target = -rng.choice([1, 2, 3, 4, 6, 7, 8]) * step
    svg = draw_number_line_svg(min_val=min_v, max_val=max_v, step=2*step, markers={target: "A"}, label="Integer Number Line")

    prompt = (
        f"Examine the integer number line below, which is calibrated with consistent equal spacing.\n\n"
        f"Determine the exact integer represented by the marker letter **A**."
    )
    sol = (
        f"**Step 1:** Identify the scale step and origin $0$ on the number line.\n\n"
        f"The marker **A** is situated to the left of $0$, representing a negative integer [1 Mark: Method].\n\n"
        f"**Step 2:** Counting by steps of {step} to the left from $0$ reaches **{target}** [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{A = {target}}}$$"
    )
    return {
        "id": f"g7_int_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_identifying_missing_integers_on_number_line",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "target": target, "step": step},
        "hints": {
            "tier_1": "Locate 0 on the number line and see which side the marker A is on.",
            "tier_2": f"Marker A is to the left of 0, so it must be negative. Count the tick marks in steps of {step}.",
            "tier_3": f"A = {target}."
        }
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
