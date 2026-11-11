"""
Grade 9 Mathematics - Functions and Relationships Archetypes 26 to 50
=====================================================================
Grounding:
  - CAPS Grade 9 Mathematics: Term 1 Topic: Functions and relationships
  - Real-world rate contexts (taxis, contracts, tank drainage)
  - Tables with non-consecutive inputs, break-even comparisons, error analysis
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.functions_svg import (
    draw_function_flow_diagram_svg,
    draw_function_table_svg,
    draw_rate_context_graph_svg,
)


def arch_26_real_world_taxi_fare_fixed_plus_per_km_rate(rng: random.Random) -> Dict[str, Any]:
    base_fare = rng.choice([25, 30, 40, 50])
    per_km = rng.choice([8, 10, 12, 15])
    km = rng.choice([5, 8, 12, 15, 20])
    total_cost = base_fare + per_km * km

    seed_val = rng.randint(1000, 999999)
    svg = draw_rate_context_graph_svg(
        initial_val=base_fare,
        rate=per_km,
        max_x=25,
        x_label="Distance (km)",
        y_label="Fare (Rands)",
        context_title="Taxi Fare Structure",
        seed=seed_val,
    )

    return {
        "subskill": "26_real_world_taxi_fare_fixed_plus_per_km_rate",
        "question_text": (
            f"A private taxi service charges a base boarding fee of **R{base_fare}** plus **R{per_km} per kilometre** travelled.\n"
            f"The total fare $C$ (in Rands) for a journey of $d$ kilometres is modelled by $C = {base_fare} + {per_km}d$.\n\n"
            f"Calculate the **total fare (in Rands)** for a trip of **{km} km**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(total_cost),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Distance charge: {km} \\times {per_km} = {km * per_km}", "marks": 1},
            {"step": f"Total fare: {base_fare} + {km * per_km} = {total_cost}", "marks": 1},
        ],
        "hints": [
            f"Use the linear cost model $C = {base_fare} + {per_km}d$.",
            f"Calculate the distance charge: ${per_km} \\times {km} = R{per_km * km}$.",
            f"Add the base fare: $R{base_fare} + R{per_km * km} = R{total_cost}$.",
        ],
        "misconception_tags": ["rate_context_substitution", "fixed_cost_addition_error"],
    }


def arch_27_real_world_cellphone_contract_monthly_plus_per_minute(rng: random.Random) -> Dict[str, Any]:
    fixed_fee = rng.choice([150, 199, 250, 299])
    per_min = rng.choice([1, 2, 3])
    minutes = rng.choice([30, 45, 60, 80])
    total_bill = fixed_fee + per_min * minutes

    return {
        "subskill": "27_real_world_cellphone_contract_monthly_plus_per_minute",
        "question_text": (
            f"A cellphone plan charges a monthly subscription of **R{fixed_fee}** plus **R{per_min} per minute** of out-of-bundle calls.\n"
            f"The monthly bill $B$ is given by $B = {fixed_fee} + {per_min}m$, where $m$ is the number of out-of-bundle call minutes.\n\n"
            f"Calculate the total bill (in Rands) if a subscriber makes **{minutes} minutes** of out-of-bundle calls."
        ),
        "correct_answer": str(total_bill),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate call minutes cost: {per_min} \\times {minutes} = {per_min * minutes}", "marks": 1},
            {"step": f"Add base subscription: {fixed_fee} + {per_min * minutes} = {total_bill}", "marks": 1},
        ],
        "hints": [
            f"Substitute $m = {minutes}$ into $B = {fixed_fee} + {per_min}m$.",
            f"Call cost: ${per_min} \\times {minutes} = R{per_min * minutes}$.",
            f"Total bill: $R{fixed_fee} + R{per_min * minutes} = R{total_bill}$.",
        ],
        "misconception_tags": ["cellphone_cost_modelling", "fixed_plus_variable_rate"],
    }


def arch_28_real_world_water_tank_draining_linear_depletion(rng: random.Random) -> Dict[str, Any]:
    init_vol = rng.choice([1000, 1500, 2000, 2500])
    drain_rate = rng.choice([40, 50, 60, 80])
    hours = rng.choice([5, 8, 10, 12])
    remaining = init_vol - drain_rate * hours

    seed_val = rng.randint(1000, 999999)
    svg = draw_rate_context_graph_svg(
        initial_val=init_vol,
        rate=-drain_rate,
        max_x=20,
        x_label="Hours (t)",
        y_label="Water (L)",
        context_title="Water Tank Depletion",
        seed=seed_val,
    )

    return {
        "subskill": "28_real_world_water_tank_draining_linear_depletion",
        "question_text": (
            f"A water tank initially contains **{init_vol} litres** of water and is drained at a constant rate of **{drain_rate} litres per hour**.\n"
            f"The volume of water remaining $V$ after $t$ hours is modelled by $V = {init_vol} - {drain_rate}t$.\n\n"
            f"Calculate the **remaining volume of water (in litres)** after **{hours} hours**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(remaining),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Water drained: {drain_rate} \\times {hours} = {drain_rate * hours} L", "marks": 1},
            {"step": f"Remaining volume: {init_vol} - {drain_rate * hours} = {remaining} L", "marks": 1},
        ],
        "hints": [
            f"Water drained in {hours} hours = ${drain_rate} \\times {hours} = {drain_rate * hours}$ L.",
            f"Subtract this from initial volume: ${init_vol} - {drain_rate * hours} = {remaining}$ L.",
        ],
        "misconception_tags": ["rate_of_depletion", "linear_decay_evaluation"],
    }


def arch_29_real_world_water_tank_filling_constant_rate(rng: random.Random) -> Dict[str, Any]:
    init_vol = rng.choice([200, 300, 400])
    inflow_rate = rng.choice([25, 30, 40, 50])
    target_vol = rng.choice([800, 1000, 1200])
    # Ensure (target_vol - init_vol) is divisible by inflow_rate
    needed = target_vol - init_vol
    inflow_rate = rng.choice([r for r in [20, 25, 50, 100] if needed % r == 0])
    hours = needed // inflow_rate

    return {
        "subskill": "29_real_world_water_tank_filling_constant_rate",
        "question_text": (
            f"A reservoir contains **{init_vol} litres** of rainwater. Water flows in from a catchment system at a steady rate of **{inflow_rate} litres per hour**.\n"
            f"The formula for the total water volume is $V = {init_vol} + {inflow_rate}t$.\n\n"
            f"How many **hours ($t$)** will it take for the reservoir to reach a total volume of **{target_vol} litres**?"
        ),
        "correct_answer": str(hours),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: {init_vol} + {inflow_rate}t = {target_vol}", "marks": 1},
            {"step": f"Subtract initial: {inflow_rate}t = {needed}", "marks": 1},
            {"step": f"Solve for t: t = {needed} \\div {inflow_rate} = {hours}", "marks": 1},
        ],
        "hints": [
            f"Calculate the additional volume needed: ${target_vol} - {init_vol} = {needed}$ litres.",
            f"Divide this volume by the inflow rate: ${needed} \\div {inflow_rate} = {hours}$ hours.",
        ],
        "misconception_tags": ["solving_linear_rate_equation", "time_to_fill_calculation"],
    }


def arch_30_real_world_temperature_conversion_celsius_to_fahrenheit(rng: random.Random) -> Dict[str, Any]:
    # F = (9/5)*C + 32, choose C multiple of 5
    c_val = rng.choice([10, 15, 20, 25, 30, 35])
    f_val = (9 * c_val) // 5 + 32

    return {
        "subskill": "30_real_world_temperature_conversion_celsius_to_fahrenheit",
        "question_text": (
            f"The formula to convert temperature from degrees Celsius ($C$) to degrees Fahrenheit ($F$) is:\n"
            f"$$F = \\frac{{9}}{{5}}C + 32$$\n\n"
            f"Convert a temperature of **$C = {c_val}^\\circ\\text{{C}}$** into degrees Fahrenheit."
        ),
        "correct_answer": str(f_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply: \\frac{{9}}{{5}} \\times {c_val} = {(9 * c_val) // 5}", "marks": 1},
            {"step": f"Add 32: {(9 * c_val) // 5} + 32 = {f_val}", "marks": 1},
        ],
        "hints": [
            f"Divide ${c_val}$ by $5$: ${c_val} \\div 5 = {c_val // 5}$.",
            f"Multiply by $9$: $9 \\times {c_val // 5} = {(9 * c_val) // 5}$.",
            f"Add $32$: ${(9 * c_val) // 5} + 32 = {f_val}^\\circ\\text{{F}}$.",
        ],
        "misconception_tags": ["temperature_formula_substitution", "fractional_coefficient_evaluation"],
    }


def arch_31_real_world_speed_distance_time_function_graph_rule(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([60, 75, 80, 100, 120])
    time_h = rng.choice([2, 3, 4, 5])
    dist = speed * time_h

    return {
        "subskill": "31_real_world_speed_distance_time_function_graph_rule",
        "question_text": (
            f"A motorist travels at a constant average speed of **{speed} km/h** on the N1 highway.\n"
            f"The relationship between distance $D$ (in kilometres) and travel time $t$ (in hours) is $D = {speed}t$.\n\n"
            f"Calculate the distance travelled (in km) after **{time_h} hours**."
        ),
        "correct_answer": str(dist),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute t = {time_h}: D = {speed} \\times {time_h} = {dist}", "marks": 1},
        ],
        "hints": [
            f"Use distance = speed $\\times$ time.",
            f"$D = {speed} \\times {time_h} = {dist}$ km.",
        ],
        "misconception_tags": ["speed_distance_time_direct_variation", "multiplication_rate"],
    }


def arch_32_real_world_electricity_cost_tiered_or_flat_rate(rng: random.Random) -> Dict[str, Any]:
    unit_cost_cents = rng.choice([150, 180, 200, 220])  # cents per kWh
    kwh = rng.choice([50, 100, 150, 200])
    total_cents = unit_cost_cents * kwh
    total_rands = total_cents // 100

    return {
        "subskill": "32_real_world_electricity_cost_tiered_or_flat_rate",
        "question_text": (
            f"A prepaid electricity meter charges **{unit_cost_cents} cents per kilowatt-hour (kWh)**.\n"
            f"The cost formula in cents is $C = {unit_cost_cents} \\times k$, where $k$ is kWh used.\n\n"
            f"Calculate the cost **in Rands** for consuming **{kwh} kWh** of electricity ($100\\text{{ cents}} = \\text{{R}}1$)."
        ),
        "correct_answer": str(total_rands),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate cents: {unit_cost_cents} \\times {kwh} = {total_cents} c", "marks": 1},
            {"step": f"Convert to Rands: {total_cents} \\div 100 = R{total_rands}", "marks": 1},
        ],
        "hints": [
            f"First find the cost in cents: ${unit_cost_cents} \\times {kwh} = {total_cents}$ cents.",
            f"Convert cents to Rands by dividing by $100$: ${total_cents} \\div 100 = \\text{{R}}{total_rands}$.",
        ],
        "misconception_tags": ["currency_conversion_in_rate", "cents_to_rands_division"],
    }


def arch_33_function_input_output_ordered_pairs_domain_range(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([1, 2, 3])
    x_set = [1, 2, 3, 4]
    y_set = [m * x + c for x in x_set]

    # Ask for maximum element in the range
    max_range = max(y_set)
    dom_str = ", ".join(map(str, x_set))

    return {
        "subskill": "33_function_input_output_ordered_pairs_domain_range",
        "question_text": (
            f"A function is defined by $y = {m}x + {c}$ on the domain $x \\in \\{{{dom_str}\\}}.\n\n"
            f"Determine the **maximum value in the range** of this function."
        ),
        "correct_answer": str(max_range),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify that maximum occurs at largest domain value $x = {x_set[-1]}$", "marks": 1},
            {"step": f"Evaluate: $y = {m}({x_set[-1]}) + {c} = {max_range}$", "marks": 1},
        ],
        "hints": [
            f"For an increasing linear function, the maximum output occurs at the maximum input $x = {x_set[-1]}$.",
            f"Substitute $x = {x_set[-1]}$: $y = {m}({x_set[-1]}) + {c} = {max_range}$.",
        ],
        "misconception_tags": ["domain_and_range_concepts", "maximum_value_evaluation"],
    }


def arch_34_identify_dependent_vs_independent_variable_context(rng: random.Random) -> Dict[str, Any]:
    contexts = [
        ("The cost of petrol ($C$) depends on the number of litres purchased ($L$)", "C", "L"),
        ("The temperature in a greenhouse ($T$) depends on the time of day ($t$)", "T", "t"),
        ("The mass of a loaf of bread ($M$) depends on the amount of flour used ($F$)", "M", "F"),
        ("The total wages earned ($W$) depends on the number of hours worked ($h$)", "W", "h"),
    ]
    statement, dep, indep = rng.choice(contexts)

    return {
        "subskill": "34_identify_dependent_vs_independent_variable_context",
        "question_text": (
            f"Consider this real-world scenario: *\"{statement}\"*.\n\n"
            f"Which variable is the **dependent variable**? (Enter the single variable symbol: **{dep}** or **{indep}**)."
        ),
        "correct_answer": dep,
        "marking_schema": [
            {"step": f"Identify {dep} as the outcome that depends on the independent variable {indep}", "marks": 1},
        ],
        "hints": [
            "The dependent variable is the output quantity whose value relies on the other quantity.",
            f"Here, {dep} is determined by {indep}, so {dep} is the dependent variable.",
        ],
        "misconception_tags": ["dependent_vs_independent_variable", "variable_role_in_context"],
    }


def arch_35_composite_flow_diagram_two_stages(rng: random.Random) -> Dict[str, Any]:
    # x -> (+a) -> (*b) -> (-c) -> y
    a = rng.choice([1, 2, 3])
    b = rng.choice([2, 3, 4])
    c = rng.choice([2, 5, 6])
    x = rng.choice([3, 4, 5])
    y_val = (x + a) * b - c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"+ {a}", f"× {b} then - {c}", input_str=str(x), output_str="?", seed=seed_val)

    return {
        "subskill": "35_composite_flow_diagram_two_stages",
        "question_text": (
            f"In a multi-stage flow diagram, an input $x$ is first increased by ${a}$, "
            f"the result is multiplied by ${b}$, and finally ${c}$ is subtracted:\n\n"
            f"Calculate the **output value ($y$)** when the input is **$x = {x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Stage 1: {x} + {a} = {x + a}", "marks": 1},
            {"step": f"Stage 2: {x + a} \\times {b} = {(x + a) * b}", "marks": 1},
            {"step": f"Stage 3: {(x + a) * b} - {c} = {y_val}", "marks": 1},
        ],
        "hints": [
            f"First add ${a}$: ${x} + {a} = {x + a}$.",
            f"Next multiply by ${b}$: ${x + a} \\times {b} = {(x + a) * b}$.",
            f"Finally subtract ${c}$: ${(x + a) * b} - {c} = {y_val}$.",
        ],
        "misconception_tags": ["multi_step_flow_diagram", "order_of_compound_operations"],
    }


def arch_36_determine_constant_difference_and_zeroth_term(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.choice([2, 3, 5, 7])
    # x = 1, 2, 3, 4 -> y = m*x + c
    x_vals = [1, 2, 3, 4]
    y_vals = [m * x + c for x in x_vals]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, y_vals, rule_label="y = mx + c", seed=seed_val)

    return {
        "subskill": "36_determine_constant_difference_and_zeroth_term",
        "question_text": (
            f"The table below shows input-output pairs for a linear function:\n\n"
            f"Determine the **zeroth term (the constant value $c$ where $x = 0$)** in the rule $y = mx + c$."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find constant difference: $m = {y_vals[1]} - {y_vals[0]} = {m}$", "marks": 1},
            {"step": f"Work backwards to $x=0$: $c = {y_vals[0]} - {m} = {c}$", "marks": 1},
        ],
        "hints": [
            f"The constant difference is $m = {y_vals[1]} - {y_vals[0]} = {m}$.",
            f"When $x = 1$, $y = {y_vals[0]}$. To find the value at $x = 0$, subtract $m$: ${y_vals[0]} - {m} = {c}$.",
            f"The constant term is $c = {c}$.",
        ],
        "misconception_tags": ["zeroth_term_determination", "y_intercept_from_table"],
    }


def arch_37_table_non_consecutive_inputs_find_gradient(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 4, 7])
    x1, x2 = 2, 6
    y1 = m * x1 + c
    y2 = m * x2 + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg([x1, x2], [y1, y2], rule_label="y = mx + c", seed=seed_val)

    return {
        "subskill": "37_table_non_consecutive_inputs_find_gradient",
        "question_text": (
            f"A linear function has the following input-output values:\n\n"
            f"When $x = {x1}$, $y = {y1}$; and when $x = {x2}$, $y = {y2}$.\n\n"
            f"Calculate the **gradient ($m = \\frac{{\\Delta y}}{{\\Delta x}}$)** of this linear function."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Compute $\\Delta y = {y2} - {y1} = {y2 - y1}$", "marks": 1},
            {"step": f"Compute $\\Delta x = {x2} - {x1} = {x2 - x1}$", "marks": 1},
            {"step": f"Calculate gradient: $m = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$", "marks": 1},
        ],
        "hints": [
            f"Change in $y$: ${y2} - {y1} = {y2 - y1}$.",
            f"Change in $x$: ${x2} - {x1} = {x2 - x1}$.",
            f"Gradient $m = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$.",
        ],
        "misconception_tags": ["gradient_with_non_consecutive_inputs", "delta_y_over_delta_x"],
    }


def arch_38_formula_substitution_large_value_extrapolation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 7])
    c = rng.choice([10, 15, 25, 50])
    x_large = rng.choice([50, 100, 200])
    y_val = m * x_large + c

    return {
        "subskill": "38_formula_substitution_large_value_extrapolation",
        "question_text": (
            f"A function rule is given by $y = {m}x + {c}$.\n\n"
            f"Extrapolate and calculate the value of **$y$** when **$x = {x_large}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {x_large}$: $y = {m}({x_large}) + {c}$", "marks": 1},
            {"step": f"Multiply and add: ${m * x_large} + {c} = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = {x_large}$ into the equation.",
            f"${m} \\times {x_large} = {m * x_large}$.",
            f"Now add ${c}$: ${m * x_large} + {c} = {y_val}$.",
        ],
        "misconception_tags": ["large_number_extrapolation", "multiplication_by_multiples_of_ten"],
    }


def arch_39_formula_substitution_solve_for_x_integer_result(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.choice([7, 11, 13, 17])
    x_int = rng.choice([12, 15, 18, 20])
    y_val = m * x_int + c

    return {
        "subskill": "39_formula_substitution_solve_for_x_integer_result",
        "question_text": (
            f"Given the linear formula $y = {m}x + {c}$, find the **input value ($x$)** "
            f"that produces an output of **$y = {y_val}$**."
        ),
        "correct_answer": str(x_int),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: ${m}x + {c} = {y_val}$", "marks": 1},
            {"step": f"Subtract {c}: ${m}x = {y_val - c}$", "marks": 1},
            {"step": f"Divide by {m}: $x = {x_int}$", "marks": 1},
        ],
        "hints": [
            f"Subtract ${c}$ from ${y_val}$: ${y_val} - {c} = {y_val - c}$.",
            f"Divide by ${m}$: ${y_val - c} \\div {m} = {x_int}$.",
        ],
        "misconception_tags": ["solving_for_input_variable", "linear_equation_transposition"],
    }


def arch_40_formula_substitution_solve_for_x_fraction_result(rng: random.Random) -> Dict[str, Any]:
    # e.g. 2x + 1 = 6 -> 2x = 5 -> x = 5/2 or 2.5
    m = 2
    c = rng.choice([1, 3, 5])
    y_val = c + rng.choice([5, 7, 9])
    # x = (y_val - c) / 2
    diff = y_val - c
    ans_dec = diff / 2.0
    # format as South African comma decimal or dot
    ans_str = str(ans_dec)

    return {
        "subskill": "40_formula_substitution_solve_for_x_fraction_result",
        "question_text": (
            f"Given the function rule $y = {m}x + {c}$, solve for **$x$** (as a decimal) "
            f"when the output is **$y = {y_val}$**."
        ),
        "correct_answer": ans_str,
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Subtract {c}: ${m}x = {diff}$", "marks": 1},
            {"step": f"Divide by {m}: $x = \\frac{{{diff}}}{{{m}}} = {ans_dec}$", "marks": 1},
        ],
        "hints": [
            f"Subtract ${c}$ from both sides: ${m}x = {y_val} - {c} = {diff}$.",
            f"Divide by ${m}$: $x = \\frac{{{diff}}}{{{m}}} = {ans_dec}$.",
        ],
        "misconception_tags": ["fractional_input_solution", "decimal_division_in_functions"],
    }


def arch_41_compare_two_linear_plans_find_breakeven_input(rng: random.Random) -> Dict[str, Any]:
    # Plan A: y = m1*x + c1, Plan B: y = m2*x + c2
    # Breakeven: m1*x + c1 = m2*x + c2
    m1 = rng.choice([5, 6, 7])
    m2 = m1 + rng.choice([2, 3])
    x_eq = rng.choice([10, 15, 20])
    c2 = 0
    c1 = (m2 - m1) * x_eq

    return {
        "subskill": "41_compare_two_linear_plans_find_breakeven_input",
        "question_text": (
            f"Two gym membership options are available:\n"
            f"* **Option A:** Fixed registration of **R{c1}** plus **R{m1}** per session ($y = {m1}x + {c1}$)\n"
            f"* **Option B:** No registration fee, but **R{m2}** per session ($y = {m2}x$)\n\n"
            f"Determine the number of sessions ($x$) for which both options cost the exact same amount."
        ),
        "correct_answer": str(x_eq),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Equate costs: ${m1}x + {c1} = {m2}x$", "marks": 1},
            {"step": f"Collect like terms: ${m2 - m1}x = {c1}$", "marks": 1},
            {"step": f"Solve: $x = {c1} \\div {m2 - m1} = {x_eq}$ sessions", "marks": 1},
        ],
        "hints": [
            f"Set the two equations equal to each other: ${m1}x + {c1} = {m2}x$.",
            f"Subtract ${m1}x$ from both sides: ${m2 - m1}x = {c1}$.",
            f"Divide by ${m2 - m1}$: $x = {c1} \\div {m2 - m1} = {x_eq}$.",
        ],
        "misconception_tags": ["breakeven_comparison", "simultaneous_linear_equating"],
    }


def arch_42_linear_function_rate_of_change_interpretation(rng: random.Random) -> Dict[str, Any]:
    # Context: candle burning, height h = 30 - 3t
    h0 = rng.choice([25, 30, 35])
    burn_rate = rng.choice([2, 3, 4])
    t = rng.choice([3, 4, 5])
    h_final = h0 - burn_rate * t

    return {
        "subskill": "42_linear_function_rate_of_change_interpretation",
        "question_text": (
            f"A candle has an initial height of **{h0} cm** and burns down at a constant rate of **{burn_rate} cm per hour**.\n"
            f"The formula for its height is $h = {h0} - {burn_rate}t$, where $t$ is time in hours.\n\n"
            f"Calculate the **height of the candle (in cm)** after burning for **{t} hours**."
        ),
        "correct_answer": str(h_final),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate burnt length: {burn_rate} \\times {t} = {burn_rate * t} cm", "marks": 1},
            {"step": f"Subtract from initial height: {h0} - {burn_rate * t} = {h_final} cm", "marks": 1},
        ],
        "hints": [
            f"Length burnt away in {t} hours = ${burn_rate} \\times {t} = {burn_rate * t}$ cm.",
            f"Remaining height = ${h0} - {burn_rate * t} = {h_final}$ cm.",
        ],
        "misconception_tags": ["rate_of_change_context", "linear_decrease_word_problem"],
    }


def arch_43_step_function_parking_fee_or_postage_rates(rng: random.Random) -> Dict[str, Any]:
    # Parking: First hour R15, each additional hour R10
    first_hour = 15
    add_hour = 10
    hours = rng.choice([3, 4, 5, 6])
    cost = first_hour + (hours - 1) * add_hour

    return {
        "subskill": "43_step_function_parking_fee_or_postage_rates",
        "question_text": (
            f"A shopping centre charges **R{first_hour}** for the first hour of parking and **R{add_hour}** for each additional full hour.\n"
            f"The formula for parking $t$ hours ($t \\ge 1$) is $C = {first_hour} + {add_hour}(t - 1)$.\n\n"
            f"Calculate the total parking fee (in Rands) for a car parked for **{hours} hours**."
        ),
        "correct_answer": str(cost),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Additional hours: {hours} - 1 = {hours - 1}", "marks": 1},
            {"step": f"Additional cost: {hours - 1} \\times {add_hour} = {(hours - 1) * add_hour}", "marks": 1},
            {"step": f"Total: {first_hour} + {(hours - 1) * add_hour} = {cost}", "marks": 1},
        ],
        "hints": [
            f"The first hour costs R{first_hour}.",
            f"There are ${hours} - 1 = {hours - 1}$ additional hours, costing ${hours - 1} \\times {add_hour} = R{(hours - 1) * add_hour}$.",
            f"Total fee: $R{first_hour} + R{(hours - 1) * add_hour} = R{cost}$.",
        ],
        "misconception_tags": ["piecewise_linear_cost", "subtraction_of_base_interval"],
    }


def arch_44_cubic_function_table_evaluation_y_equals_x_cubed(rng: random.Random) -> Dict[str, Any]:
    x_vals = [1, 2, 3, 4]
    y_vals = [x ** 3 for x in x_vals]

    target_idx = 2  # x = 3
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "K" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label="y = x^3", seed=seed_val)

    return {
        "subskill": "44_cubic_function_table_evaluation_y_equals_x_cubed",
        "question_text": (
            f"The table below shows values for the non-linear cubic function $y = x^3$:\n\n"
            f"Determine the value of **$K$** when the input is **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Evaluate $K = ({target_x})^3 = {target_x} \\times {target_x} \\times {target_x} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Cubing a number means multiplying it by itself three times.",
            f"$K = {target_x} \\times {target_x} \\times {target_x} = {target_y}$.",
        ],
        "misconception_tags": ["cubic_power_evaluation", "confusing_cube_with_multiply_by_three"],
    }


def arch_45_rational_function_table_evaluation_simple_hyperbola(rng: random.Random) -> Dict[str, Any]:
    # y = 12 / x
    k = 12
    x_vals = [1, 2, 3, 4, 6]
    y_vals = [k // x for x in x_vals]

    target_idx = 3  # x = 4
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "R" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label=f"y = {k}/x", seed=seed_val)

    return {
        "subskill": "45_rational_function_table_evaluation_simple_hyperbola",
        "question_text": (
            f"The table below presents values for the rational function $y = \\frac{{{k}}}{{x}}$:\n\n"
            f"Calculate the missing value **$R$** when **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {target_x}$: $R = \\frac{{{k}}}{{{target_x}}} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = {target_x}$ into the fraction: $R = \\frac{{{k}}}{{{target_x}}}$.",
            f"${k} \\div {target_x} = {target_y}$.",
        ],
        "misconception_tags": ["rational_function_evaluation", "division_in_formula"],
    }


def arch_46_geometric_pattern_to_function_rule_perimeter(rng: random.Random) -> Dict[str, Any]:
    # e.g. Perimeter of arrangement of n squares: P = 4 + 2(n-1) = 2n + 2
    n = rng.choice([8, 10, 12, 15])
    ans = 2 * n + 2

    return {
        "subskill": "46_geometric_pattern_to_function_rule_perimeter",
        "question_text": (
            f"A row of $n$ identical square tiles placed side-by-side has an outer perimeter (in units) given by $P = 2n + 2$.\n\n"
            f"Calculate the perimeter for a row containing **$n = {n}$ tiles**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $n = {n}$: $P = 2({n}) + 2$", "marks": 1},
            {"step": f"Evaluate: $P = {2 * n} + 2 = {ans}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $n = {n}$ into $P = 2n + 2$.",
            f"$2 \\times {n} = {2 * n}$.",
            f"${2 * n} + 2 = {ans}$.",
        ],
        "misconception_tags": ["pattern_to_function_link", "perimeter_formula_substitution"],
    }


def arch_47_geometric_pattern_to_function_rule_area_growth(rng: random.Random) -> Dict[str, Any]:
    # Area grows as A = 3n + 1
    n = rng.choice([6, 7, 8, 9])
    ans = 3 * n + 1

    return {
        "subskill": "47_geometric_pattern_to_function_rule_area_growth",
        "question_text": (
            f"The total number of shaded unit blocks $A$ in arrangement number $n$ follows the function rule $A = 3n + 1$.\n\n"
            f"Calculate the number of shaded blocks in **arrangement number $n = {n}$**."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $n = {n}$: $A = 3({n}) + 1 = {ans}$", "marks": 1},
        ],
        "hints": [
            f"Multiply $3$ by ${n}$: $3 \\times {n} = {3 * n}$.",
            f"Add $1$: ${3 * n} + 1 = {ans}$.",
        ],
        "misconception_tags": ["area_growth_function", "linear_term_evaluation"],
    }


def arch_48_error_analysis_misidentifying_constant_term_in_rule(rng: random.Random) -> Dict[str, Any]:
    # Learner says rule is y = 4x + 7 instead of y = 4x + 3
    m = 4
    c_correct = 3
    c_mistake = 7
    x_test = 2
    correct_y = m * x_test + c_correct

    return {
        "subskill": "48_error_analysis_misidentifying_constant_term_in_rule",
        "question_text": (
            f"A learner examines a table where $(x=1, y=7)$ and $(x=2, y=11)$.\n"
            f"They identify the gradient as $m = 4$, but incorrectly guess the rule is $y = 4x + {c_mistake}$ by mistakenly using the first $y$-value as the constant term.\n\n"
            f"What is the **correct value of the constant term $c$** in $y = 4x + c$?"
        ),
        "correct_answer": str(c_correct),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x=1, y=7$: $7 = 4(1) + c$", "marks": 1},
            {"step": f"Solve: $c = 7 - 4 = {c_correct}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = 1$ and $y = 7$ into $y = 4x + c$.",
            f"$7 = 4 + c \\implies c = 7 - 4 = {c_correct}$.",
        ],
        "misconception_tags": ["confusing_first_term_with_zeroth_term", "error_analysis_constant_term"],
    }


def arch_49_error_analysis_inverted_operations_in_finding_input(rng: random.Random) -> Dict[str, Any]:
    # Given y = 3x + 6, output y = 21. Correct x = (21-6)/3 = 5.
    # Mistake learner divides first: 21 / 3 = 7, then subtracts 6 = 1.
    m = 3
    c = 6
    x_correct = 5
    y_val = m * x_correct + c  # 21

    return {
        "subskill": "49_error_analysis_inverted_operations_in_finding_input",
        "question_text": (
            f"For the function $y = {m}x + {c}$, a learner tries to find the input for an output of $y = {y_val}$.\n"
            f"They mistakenly divide by ${m}$ first to get ${y_val // m}$, then subtract ${c}$ to get ${(y_val // m) - c}$.\n\n"
            f"Determine the **correct input value ($x$)** by applying inverse operations in the proper reverse order."
        ),
        "correct_answer": str(x_correct),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"First subtract {c}: ${y_val} - {c} = {y_val - c}$", "marks": 1},
            {"step": f"Then divide by {m}: ${y_val - c} \\div {m} = {x_correct}$", "marks": 1},
        ],
        "hints": [
            "In reversing $y = 3x + 6$, undo the addition first, then undo the multiplication.",
            f"${y_val} - {c} = {y_val - c}$.",
            f"${y_val - c} \\div {m} = {x_correct}$.",
        ],
        "misconception_tags": ["inverse_operations_order_error", "reversing_algebraic_steps"],
    }


def arch_50_compound_multi_representation_table_formula_flow_integration(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 5])
    c = rng.choice([4, 7, 9])
    x_val = rng.choice([4, 6, 8])
    y_val = m * x_val + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× {m}", f"+ {c}", input_str=str(x_val), output_str="Y", seed=seed_val)

    return {
        "subskill": "50_compound_multi_representation_table_formula_flow_integration",
        "question_text": (
            f"The flow diagram below represents a function with algebraic formula $y = {m}x + {c}$:\n\n"
            f"Calculate the final output value **$Y$** when the input is **$x = {x_val}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply: {m} \\times {x_val} = {m * x_val}", "marks": 1},
            {"step": f"Add {c}: {m * x_val} + {c} = {y_val}", "marks": 1},
        ],
        "hints": [
            f"Step 1: ${m} \\times {x_val} = {m * x_val}$.",
            f"Step 2: ${m * x_val} + {c} = {y_val}$.",
            f"Final output $Y = {y_val}$.",
        ],
        "misconception_tags": ["multi_representation_synthesis", "flow_and_formula_integration"],
    }
