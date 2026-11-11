"""
Grade 8 Mathematics - Functions and Relationships 2 Archetypes 26 to 50.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 2.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def arch_26_translating_flow_diagram_to_algebraic_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(2, 7)

    return {
        "title": "Translating Operational Mapping to Equation",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "26_translating_flow_diagram_to_algebraic_equation",
        "difficulty": "easy",
        "question_text": (
            f"An operational input-output mapping is represented by:\n\n"
            f"$$x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow y$$\n\n"
            f"Write the equivalent algebraic formula expressing $y$ in terms of $x$."
        ),
        "correct_answer": f"y = {m}x + {c}",
        "marking_schema": [
            f"Write linear equation y = {m}x + {c} (1 mark)",
        ],
        "hints": [
            f"First stage multiplies $x$ by {m}: ${m}x$.",
            f"Second stage adds {c}: ${m}x + {c}$.",
            f"Formula: $y = {m}x + {c}$.",
        ],
        "misconception_tags": ["mapping_to_equation_translation_error"],
        "diagram_spec": None,
    }


def arch_27_translating_algebraic_equation_to_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 4, 6])
    c = rng.randint(3, 9)

    return {
        "title": "Translating Algebraic Equation to Operational Chain",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "27_translating_algebraic_equation_to_flow_diagram",
        "difficulty": "medium",
        "question_text": (
            f"For the formula $y = {m}x - {c}$:\n\n"
            f"Identify the two sequential operations in order:\n"
            f"* **Stage 1 operator:** $\\boxed{{?}}$\n"
            f"* **Stage 2 operator:** $\\boxed{{?}}$\n\n"
            f"State your answer in the form: Multiply by {m}, then subtract {c}."
        ),
        "correct_answer": f"Multiply by {m}, then subtract {c}",
        "marking_schema": [
            f"Identify operation 1: Multiply by {m} (1 mark)",
            f"Identify operation 2: Subtract {c} (1 mark)",
        ],
        "hints": [
            f"Order of operations dictates multiplication by {m} occurs first.",
            f"Then subtraction of {c} occurs second.",
        ],
        "misconception_tags": ["operator_order_identification_error"],
        "diagram_spec": None,
    }


def arch_28_definition_of_function_one_to_one_and_many_to_one(rng: random.Random) -> Dict[str, Any]:
    relation_type = rng.choice(["linear", "quadratic"])
    if relation_type == "linear":
        desc = "Each input value $x$ gives exactly one unique output value $y$."
        ans = "Yes"
    else:
        desc = "Two different input values (e.g. $x = 2$ and $x = -2$) produce the same output value ($y = 4$)."
        ans = "Yes"

    return {
        "title": "Definition of Function (Single Output per Input)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "28_definition_of_function_one_to_one_and_many_to_one",
        "difficulty": "medium",
        "question_text": (
            f"In mathematics, a relation is called a **function** if every input value has exactly one output value.\n\n"
            f"Consider a relationship where {desc}\n\n"
            f"Does this relationship qualify as a function? Answer **Yes** or **No**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Apply function definition: Exactly one output per input => {ans} (1 mark)",
        ],
        "hints": [
            "A relationship is a function as long as no single input produces multiple different outputs.",
            "Both one-to-one and many-to-one relations are functions.",
            "Answer: Yes.",
        ],
        "misconception_tags": ["function_definition_many_to_one_confusion"],
        "diagram_spec": None,
    }


def arch_29_identifying_non_function_relation_one_to_many(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([4, 9, 16, 25])
    r_val = int(math.isqrt(x_val))

    return {
        "title": "Identifying Non-Function Relation (One-to-Many)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "29_identifying_non_function_relation_one_to_many",
        "difficulty": "hard",
        "question_text": (
            f"Consider a relation that assigns to each positive number $x$ both its positive and negative square roots:\n\n"
            f"$$\\text{{Input: }} {x_val} \\longrightarrow \\text{{Outputs: }} +{r_val} \\text{{ and }} -{r_val}$$\n\n"
            f"Is this relation a function? Answer **Yes** or **No**."
        ),
        "correct_answer": "No",
        "marking_schema": [
            "Identify that single input yields two outputs (1 mark)",
            "Conclude it is not a function: No (1 mark)",
        ],
        "hints": [
            "A function must assign exactly one output to each input.",
            f"Here, the single input {x_val} gives two outputs (+{r_val} and -{r_val}).",
            "Therefore, it is NOT a function.",
        ],
        "misconception_tags": ["one_to_many_relation_function_fallacy"],
        "diagram_spec": None,
    }


def arch_30_identifying_domain_and_range_discrete_set(rng: random.Random) -> Dict[str, Any]:
    inputs = sorted(rng.sample(range(1, 10), 4))
    m = rng.choice([2, 3])
    outputs = [m * x + 1 for x in inputs]
    in_str = "{" + ", ".join(str(x) for x in inputs) + "}"
    out_str = "{" + ", ".join(str(y) for y in outputs) + "}"

    return {
        "title": "Domain and Range for Discrete Set",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "30_identifying_domain_and_range_discrete_set",
        "difficulty": "medium",
        "question_text": (
            f"A function maps the set of input values (Domain) {in_str} using the rule $y = {m}x + 1$.\n\n"
            f"List the set of output values (Range) in set notation separated by commas."
        ),
        "correct_answer": out_str,
        "marking_schema": [
            f"Evaluate each input: {out_str} (2 marks)",
        ],
        "hints": [
            f"Substitute each input into $y = {m}x + 1$.",
            f"The range is the set of all outputs: {out_str}.",
        ],
        "misconception_tags": ["domain_vs_range_confusion"],
        "diagram_spec": None,
    }


def arch_31_completing_table_with_fractional_outputs(rng: random.Random) -> Dict[str, Any]:
    den = rng.choice([2, 4, 5])
    x_val = rng.choice([1, 3, 7])
    # y = x / den
    ans_fraction = f"{x_val}/{den}"

    return {
        "title": "Completing Table with Fractional Outputs",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "31_completing_table_with_fractional_outputs",
        "difficulty": "medium",
        "question_text": (
            f"A division rule is given by $y = \\frac{{x}}{{{den}}}$.\n\n"
            f"Calculate the output $y$ when the input is $x = {x_val}$. Express your answer as a common fraction."
        ),
        "correct_answer": ans_fraction,
        "marking_schema": [
            f"Substitute x = {x_val}: y = {ans_fraction} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_val}$ in the numerator: $y = \\frac{{{x_val}}}{{{den}}}$.",
        ],
        "misconception_tags": ["fractional_output_representation_error"],
        "diagram_spec": None,
    }


def arch_32_completing_table_with_negative_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.randint(5, 12)
    x_val = rng.randint(6, 10)
    # y = m*x - c ... wait, we want negative output so c - m*x
    # Let y = c - m*x
    out_val = c - m * x_val

    return {
        "title": "Completing Table with Negative Outputs",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "32_completing_table_with_negative_outputs",
        "difficulty": "medium",
        "question_text": (
            f"For the linear function $y = {c} - {m}x$:\n\n"
            f"Determine the negative output value $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Multiply {m} * {x_val} = {m * x_val} (1 mark)",
            f"Subtract: {c} - {m * x_val} = {out_val} (1 mark)",
        ],
        "hints": [
            f"$y = {c} - {m}({x_val}) = {c} - {m * x_val}$.",
            f"${c} - {m * x_val} = {out_val}$.",
        ],
        "misconception_tags": ["signed_integer_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_33_equivalent_linear_formulae_verification(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 4, 5])
    k = rng.choice([10, 15, 20])
    # y = a*(k - x) = a*k - a*x
    c_val = a * k

    return {
        "title": "Verifying Equivalence of Linear Formulae",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "33_equivalent_linear_formulae_verification",
        "difficulty": "medium",
        "question_text": (
            f"Consider two proposed formulae:\n\n"
            f"* **Formula 1:** $y = {a}({k} - x)$\n"
            f"* **Formula 2:** $y = {c_val} - {a}x$\n\n"
            f"Are Formula 1 and Formula 2 mathematically equivalent for all values of $x$? Answer **Yes** or **No**."
        ),
        "correct_answer": "Yes",
        "marking_schema": [
            f"Apply distributive law to Formula 1: {a}({k} - x) = {c_val} - {a}x (1 mark)",
            "Conclude equivalence: Yes (1 mark)",
        ],
        "hints": [
            f"Expand Formula 1: ${a} \\times {k} = {c_val}$ and ${a} \\times (-x) = -{a}x$.",
            f"This gives ${c_val} - {a}x$, which matches Formula 2 exactly.",
            "Answer: Yes.",
        ],
        "misconception_tags": ["distributive_bracket_expansion_error"],
        "diagram_spec": None,
    }


def arch_34_real_world_electricity_stepped_or_linear_tariff(rng: random.Random) -> Dict[str, Any]:
    standing = rng.choice([100, 150, 200])
    rate = rng.choice([2.0, 2.5, 3.0])
    kwh = rng.randint(150, 350)
    total = standing + rate * kwh
    rate_str = str(rate).replace(".", ",")

    return {
        "title": "Electricity Tariff Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "34_real_world_electricity_stepped_or_linear_tariff",
        "difficulty": "medium",
        "question_text": (
            f"A municipal electricity account has a fixed monthly service charge of $\\text{{R}}{standing}$ plus $\\text{{R}}{rate_str}$ per kWh consumed.\n\n"
            f"Calculate the total electricity cost (in Rand) for a household that used **{kwh} kWh** in a month."
        ),
        "correct_answer": f"R{int(total) if total.is_integer() else total}",
        "marking_schema": [
            f"Energy charge: {kwh} * {rate_str} = R{int(rate * kwh)} (1 mark)",
            f"Add standing charge: R{standing} + R{int(rate * kwh)} = R{int(total)} (1 mark)",
        ],
        "hints": [
            f"Consumption cost = ${kwh} \\times \\text{{R}}{rate_str} = \\text{{R}}{int(rate * kwh)}$.",
            f"Total = $\\text{{R}}{standing} + \\text{{R}}{int(rate * kwh)} = \\text{{R}}{int(total)}$.",
        ],
        "misconception_tags": ["standing_charge_omission_error"],
        "diagram_spec": None,
    }


def arch_35_real_world_plumber_callout_plus_hourly_rate(rng: random.Random) -> Dict[str, Any]:
    callout = rng.randint(250, 450)
    hourly = rng.randint(150, 250)
    hours = rng.randint(2, 6)
    total = callout + hourly * hours

    return {
        "title": "Plumber Call-Out Fee and Hourly Labour",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "35_real_world_plumber_callout_plus_hourly_rate",
        "difficulty": "medium",
        "question_text": (
            f"A plumber charges an initial call-out fee of $\\text{{R}}{callout}$ plus $\\text{{R}}{hourly}$ per hour of labour.\n\n"
            f"Calculate the total invoice amount (in Rand) for a repair job taking **{hours} hours**."
        ),
        "correct_answer": f"R{total}",
        "marking_schema": [
            f"Labour cost: {hourly} * {hours} = R{hourly * hours} (1 mark)",
            f"Total invoice: R{callout} + R{hourly * hours} = R{total} (1 mark)",
        ],
        "hints": [
            f"Formula: $C = {hourly}h + {callout}$.",
            f"Labour: ${hourly} \\times {hours} = \\text{{R}}{hourly * hours}$.",
            f"Total: $\\text{{R}}{callout} + \\text{{R}}{hourly * hours} = \\text{{R}}{total}$.",
        ],
        "misconception_tags": ["callout_rate_addition_slip"],
        "diagram_spec": None,
    }


def arch_36_real_world_car_rental_daily_plus_per_km(rng: random.Random) -> Dict[str, Any]:
    daily = rng.randint(300, 500)
    rate_km = 3  # R3 per km
    km_driven = rng.randint(80, 250)
    total = daily + rate_km * km_driven

    return {
        "title": "Car Rental Daily Fee Plus Distance",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "36_real_world_car_rental_daily_plus_per_km",
        "difficulty": "medium",
        "question_text": (
            f"A car rental company charges a daily rental fee of $\\text{{R}}{daily}$ plus $\\text{{R}}{rate_km}$ for every kilometer driven.\n\n"
            f"Determine the total charge (in Rand) for a one-day rental where the vehicle was driven **{km_driven} km**."
        ),
        "correct_answer": f"R{total}",
        "marking_schema": [
            f"Distance charge: {km_driven} * {rate_km} = R{km_driven * rate_km} (1 mark)",
            f"Total: R{daily} + R{km_driven * rate_km} = R{total} (1 mark)",
        ],
        "hints": [
            f"Kilometer cost = ${km_driven} \\times \\text{{R}}{rate_km} = \\text{{R}}{km_driven * rate_km}$.",
            f"Total = $\\text{{R}}{daily} + \\text{{R}}{km_driven * rate_km} = \\text{{R}}{total}$.",
        ],
        "misconception_tags": ["per_km_rate_multiplication_error"],
        "diagram_spec": None,
    }


def arch_37_real_world_baking_ingredient_ratio_function(rng: random.Random) -> Dict[str, Any]:
    flour_per_cake = rng.choice([250, 300, 350])
    cakes = rng.randint(4, 9)
    total_flour = flour_per_cake * cakes

    return {
        "title": "Proportional Ingredient Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "37_real_world_baking_ingredient_ratio_function",
        "difficulty": "easy",
        "question_text": (
            f"A bakery recipe requires **{flour_per_cake} g of flour** per cake.\n\n"
            f"Use the function $F = {flour_per_cake}c$ to find the total grams of flour needed to bake **{cakes} cakes**."
        ),
        "correct_answer": f"{total_flour} g",
        "marking_schema": [
            f"Multiply {flour_per_cake} * {cakes} = {total_flour} g (1 mark)",
        ],
        "hints": [
            f"$F = {flour_per_cake} \\times {cakes} = {total_flour}\\text{{ g}}$.",
        ],
        "misconception_tags": ["direct_proportion_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_38_real_world_currency_conversion_exchange_rate_function(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([18, 19, 20])
    usd = rng.randint(15, 60)
    rand_val = usd * rate

    return {
        "title": "Currency Exchange Linear Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "38_real_world_currency_conversion_exchange_rate_function",
        "difficulty": "easy",
        "question_text": (
            f"The exchange rate converts US Dollars ($D$) to South African Rand ($R$) via the function $R = {rate}D$.\n\n"
            f"Calculate the value in Rand of **${usd}**."
        ),
        "correct_answer": f"R{rand_val}",
        "marking_schema": [
            f"Multiply {rate} * {usd} = R{rand_val} (1 mark)",
        ],
        "hints": [
            f"Multiply ${usd} by the exchange rate {rate}: ${usd} \\times {rate} = \\text{{R}}{rand_val}$.",
        ],
        "misconception_tags": ["currency_exchange_division_reversal"],
        "diagram_spec": None,
    }


def arch_39_geometry_perimeter_of_regular_polygon_function(rng: random.Random) -> Dict[str, Any]:
    sides = rng.choice([5, 6, 8])
    polygon_name = {5: "regular pentagon", 6: "regular hexagon", 8: "regular octagon"}[sides]
    side_len = rng.randint(4, 12)
    p_val = sides * side_len

    return {
        "title": "Polygon Perimeter Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "39_geometry_perimeter_of_regular_polygon_function",
        "difficulty": "easy",
        "question_text": (
            f"The perimeter ($P$) of a {polygon_name} with side length $s$ is given by $P = {sides}s$.\n\n"
            f"Calculate the perimeter (in cm) when the side length is $s = {side_len}\\text{{ cm}}$."
        ),
        "correct_answer": str(p_val),
        "marking_schema": [
            f"Multiply {sides} * {side_len} = {p_val} cm (1 mark)",
        ],
        "hints": [
            f"A {polygon_name} has {sides} equal sides.",
            f"$P = {sides} \\times {side_len} = {p_val}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["polygon_side_count_error"],
        "diagram_spec": None,
    }


def arch_40_geometry_area_of_square_as_quadratic_function(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(6, 15)
    area = s ** 2

    return {
        "title": "Area of Square (Quadratic Function)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "40_geometry_area_of_square_as_quadratic_function",
        "difficulty": "easy",
        "question_text": (
            f"The area of a square ($A$) as a function of its side length ($s$) is modeled by $A = s^2$.\n\n"
            f"Find the area (in $\\text{{cm}}^2$) of a square having a side length of $s = {s}\\text{{ cm}}$."
        ),
        "correct_answer": str(area),
        "marking_schema": [
            f"Calculate s^2: {s}^2 = {area} cm^2 (1 mark)",
        ],
        "hints": [
            f"$A = ({s})^2 = {s} \\times {s} = {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["area_vs_perimeter_multiplication_confusion"],
        "diagram_spec": None,
    }


def arch_41_geometry_area_of_rectangle_fixed_width_linear_function(rng: random.Random) -> Dict[str, Any]:
    width = rng.randint(4, 9)
    length = rng.randint(10, 25)
    area = width * length

    return {
        "title": "Rectangle Area with Fixed Width (Linear Function)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "41_geometry_area_of_rectangle_fixed_width_linear_function",
        "difficulty": "medium",
        "question_text": (
            f"A rectangle has a fixed width of **{width} cm**. Its area ($A$) depends linearly on its length ($l$): $A = {width}l$.\n\n"
            f"Calculate the area (in $\\text{{cm}}^2$) when the length is **{length} cm**."
        ),
        "correct_answer": str(area),
        "marking_schema": [
            f"Calculate A = {width} * {length} = {area} cm^2 (1 mark)",
        ],
        "hints": [
            f"$A = {width} \\times {length} = {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["fixed_dimension_linear_area_error"],
        "diagram_spec": None,
    }


def arch_42_geometry_circumference_of_circle_function(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([7, 14, 21, 28, 35])
    # C = (22/7)*d
    c_val = int((22 * d) / 7)

    return {
        "title": "Circumference of Circle Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "42_geometry_circumference_of_circle_function",
        "difficulty": "medium",
        "question_text": (
            f"The circumference ($C$) of a circle is related to its diameter ($d$) by $C = \\frac{{22}}{{7}}d$.\n\n"
            f"Calculate the circumference (in cm) of a circle with a diameter of $d = {d}\\text{{ cm}}$."
        ),
        "correct_answer": f"{c_val} cm",
        "marking_schema": [
            f"Calculate C = (22/7) * {d} = {c_val} cm (1 mark)",
        ],
        "hints": [
            f"Substitute $d = {d}$: $C = \\frac{{22}}{{7}} \\times {d} = 22 \\times {d // 7} = {c_val}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["circumference_formula_diameter_slip"],
        "diagram_spec": None,
    }


def arch_43_finding_output_for_very_large_input_in_linear_model(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([4, 6, 8])
    c = rng.randint(10, 30)
    x_val = rng.choice([500, 1000])
    ans_val = m * x_val + c

    return {
        "title": "Large Input Evaluation in Linear Model",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "43_finding_output_for_very_large_input_in_linear_model",
        "difficulty": "medium",
        "question_text": (
            f"A production function is defined by $y = {m}x + {c}$.\n\n"
            f"Calculate the output $y$ when the input is $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Substitute x = {x_val}: y = {m}({x_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"${m} \\times {x_val} = {m * x_val}$.",
            f"${m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["large_number_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_44_finding_input_for_very_large_output_in_linear_model(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([5, 8, 10])
    c = rng.randint(20, 50)
    in_val = rng.randint(100, 300)
    out_val = m * in_val + c

    return {
        "title": "Finding Input for Large Output in Linear Model",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "44_finding_input_for_very_large_output_in_linear_model",
        "difficulty": "hard",
        "question_text": (
            f"A business revenue function is $y = {m}x + {c}$.\n\n"
            f"Determine the number of units $x$ that must be sold to achieve a revenue of $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Set up {m}x + {c} = {out_val} (1 mark)",
            f"Solve for x: x = ({out_val} - {c}) / {m} = {in_val} (1 mark)",
        ],
        "hints": [
            f"Subtract {c}: ${m}x = {out_val} - {c} = {out_val - c}$.",
            f"Divide by {m}: $x = \\frac{{{out_val - c}}}{{{m}}} = {in_val}$.",
        ],
        "misconception_tags": ["inverse_operations_large_numbers_error"],
        "diagram_spec": None,
    }


def arch_45_comparing_two_delivery_services_cheaper_option(rng: random.Random) -> Dict[str, Any]:
    # Courier A: C_A = 12d + 40
    # Courier B: C_B = 16d + 20
    dist = rng.randint(3, 8)
    cost_a = 12 * dist + 40
    cost_b = 16 * dist + 20
    cheaper = "Courier A" if cost_a < cost_b else "Courier B" if cost_b < cost_a else "Both cost the same"

    return {
        "title": "Comparing Two Delivery Cost Functions",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "45_comparing_two_delivery_services_cheaper_option",
        "difficulty": "hard",
        "question_text": (
            f"Two delivery companies quote the following rates for delivery distance $d$ (in km):\n\n"
            f"* **Courier A:** $C = 12d + 40$\n"
            f"* **Courier B:** $C = 16d + 20$\n\n"
            f"Which courier service is cheaper for a delivery of **{dist} km**? State **Courier A** or **Courier B**."
        ),
        "correct_answer": cheaper,
        "marking_schema": [
            f"Compute Courier A cost: 12({dist}) + 40 = R{cost_a} (1 mark)",
            f"Compute Courier B cost: 16({dist}) + 20 = R{cost_b} (1 mark)",
            f"Conclude cheaper service: {cheaper} (1 mark)",
        ],
        "hints": [
            f"Courier A: $12({dist}) + 40 = \\text{{R}}{cost_a}$.",
            f"Courier B: $16({dist}) + 20 = \\text{{R}}{cost_b}$.",
            f"Compare: {cheaper} is cheaper.",
        ],
        "misconception_tags": ["function_comparison_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_46_break_even_distance_for_two_car_hire_companies(rng: random.Random) -> Dict[str, Any]:
    # 2d + 300 = 4d + 100 => 2d = 200 => d = 100
    d_break = rng.choice([50, 80, 100, 120])
    rate_diff = 2
    rate_a = 3
    rate_b = rate_a + rate_diff
    base_b = 150
    base_a = base_b + rate_diff * d_break

    return {
        "title": "Break-Even Distance for Two Car Hire Plans",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "46_break_even_distance_for_two_car_hire_companies",
        "difficulty": "hard",
        "question_text": (
            f"Two vehicle rental contracts offer the pricing functions:\n\n"
            f"* **Contract A:** $C = {rate_a}d + {base_a}$\n"
            f"* **Contract B:** $C = {rate_b}d + {base_b}$\n\n"
            f"Find the distance $d$ (in km) where both contracts cost exactly the same amount."
        ),
        "correct_answer": str(d_break),
        "marking_schema": [
            f"Equate costs: {rate_a}d + {base_a} = {rate_b}d + {base_b} (1 mark)",
            f"Solve for d: {rate_diff}d = {base_a - base_b} => d = {d_break} km (2 marks)",
        ],
        "hints": [
            f"Set ${rate_a}d + {base_a} = {rate_b}d + {base_b}$.",
            f"Subtract ${rate_a}d$: ${base_a} = {rate_diff}d + {base_b}$.",
            f"Subtract ${base_b}$: ${rate_diff}d = {base_a - base_b} \\implies d = {d_break}$.",
        ],
        "misconception_tags": ["break_even_solving_error"],
        "diagram_spec": None,
    }


def arch_47_evaluating_two_step_function_with_integers(rng: random.Random) -> Dict[str, Any]:
    m = -rng.randint(2, 5)
    c = -rng.randint(3, 8)
    x_val = rng.randint(2, 6)
    ans_val = m * x_val + c

    return {
        "title": "Evaluating Two-Step Function with Negative Constants",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "47_evaluating_two_step_function_with_integers",
        "difficulty": "medium",
        "question_text": (
            f"A function is given by the rule:\n\n"
            f"$$y = {m}x - {abs(c)}$$\n\n"
            f"Calculate the output $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Multiply {m} * {x_val} = {m * x_val} (1 mark)",
            f"Subtract {abs(c)}: {m * x_val} - {abs(c)} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_val}$: $y = {m}({x_val}) - {abs(c)}$.",
            f"$y = {m * x_val} - {abs(c)} = {ans_val}$.",
        ],
        "misconception_tags": ["double_negative_multiplication_confusion"],
        "diagram_spec": None,
    }


def arch_48_mystery_formula_identification_from_three_points(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 4, 5])
    c = rng.choice([1, 3, 7])
    pts = [(1, m + c), (2, 2 * m + c), (3, 3 * m + c)]

    return {
        "title": "Identifying Mystery Formula from Three Points",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "48_mystery_formula_identification_from_three_points",
        "difficulty": "medium",
        "question_text": (
            f"A relationship contains the coordinate pairs: $({pts[0][0]};\\ {pts[0][1]})$, $({pts[1][0]};\\ {pts[1][1]})$, and $({pts[2][0]};\\ {pts[2][1]})$.\n\n"
            f"Determine the linear formula relating $y$ to $x$ in the form $y = mx + c$."
        ),
        "correct_answer": f"y = {m}x + {c}",
        "marking_schema": [
            f"Determine slope m = {m} (1 mark)",
            f"Determine constant c = {c} (1 mark)",
            f"State formula y = {m}x + {c} (1 mark)",
        ],
        "hints": [
            f"Find the constant difference in $y$: ${pts[1][1]} - {pts[0][1]} = {m}$.",
            f"Substitute $x = 1$: $y = {m}(1) + c = {pts[0][1]} \\implies c = {c}$.",
            f"Equation: $y = {m}x + {c}$.",
        ],
        "misconception_tags": ["coordinate_pair_formula_deduction_error"],
        "diagram_spec": None,
    }


def arch_49_distinguishing_linear_quadratic_exponential_tables(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["linear", "quadratic", "exponential"])
    if choice == "linear":
        m, c = 3, 2
        y_vals = [m * x + c for x in [1, 2, 3, 4]]
        ans = "linear"
        reason = "first differences between outputs are constant (+3)."
    elif choice == "quadratic":
        y_vals = [(x ** 2) + 1 for x in [1, 2, 3, 4]]
        ans = "quadratic"
        reason = "second differences between outputs are constant (+2)."
    else:
        y_vals = [2 ** x for x in [1, 2, 3, 4]]
        ans = "exponential"
        reason = "consecutive outputs have a constant ratio (multiplied by 2)."

    return {
        "title": "Distinguishing Linear, Quadratic, and Exponential Tables",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "49_distinguishing_linear_quadratic_exponential_tables",
        "difficulty": "hard",
        "question_text": (
            f"Analyze the relationship in the table:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Classify the function as **linear**, **quadratic**, or **exponential**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Analyze differences/ratios: {reason} (1 mark)",
            f"Classify as {ans} (1 mark)",
        ],
        "hints": [
            "Check first differences: if constant, it is linear.",
            "Check second differences: if constant, it is quadratic.",
            "Check ratios between consecutive terms: if constant, it is exponential.",
            f"Since {reason}, it is {ans}.",
        ],
        "misconception_tags": ["function_family_classification_error"],
        "diagram_spec": None,
    }


def arch_50_full_representation_conversion_quad_verbal_table_formula(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([1, 5, 8])
    x_val = 6
    ans_val = m * x_val + c

    return {
        "title": "Four-Way Representation Translation",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "50_full_representation_conversion_quad_verbal_table_formula",
        "difficulty": "medium",
        "question_text": (
            f"A function has three equivalent representations:\n\n"
            f"1. **Verbal:** Start with ${c}$ and add ${m}$ per unit of $x$.\n"
            f"2. **Table:** $(1; {m+c}), (2; {2*m+c}), (3; {3*m+c})$\n"
            f"3. **Equation:** $y = {m}x + {c}$\n\n"
            f"Calculate the output $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Evaluate y = {m}({x_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_val}$: $y = {m}({x_val}) + {c} = {m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["representation_translation_error"],
        "diagram_spec": None,
    }
