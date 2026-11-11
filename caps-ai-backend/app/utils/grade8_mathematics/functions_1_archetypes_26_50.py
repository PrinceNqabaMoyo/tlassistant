"""
Grade 8 Mathematics - Functions and Relationships 1 Archetypes 26 to 50.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 1.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def arch_26_equivalent_formulae_expansion_verification(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(2, 5)
    c = rng.randint(1, 4)
    # y = a * (b*x + c) expanded is (a*b)*x + (a*c)
    exp_m = a * b
    exp_c = a * c
    x_test = rng.randint(2, 5)
    ans_val = exp_m * x_test + exp_c

    return {
        "title": "Equivalent Formulae (Expansion Verification)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "26_equivalent_formulae_expansion_verification",
        "difficulty": "medium",
        "question_text": (
            f"Two learners write different formulae for the same function:\n\n"
            f"* Lerato writes: $y = {a}({b}x + {c})$\n"
            f"* Thabo writes: $y = {exp_m}x + {exp_c}$\n\n"
            f"Are these two expressions equivalent? Answer **Yes** or **No**, and calculate the output value $y$ when $x = {x_test}$."
        ),
        "correct_answer": f"Yes; y = {ans_val}",
        "marking_schema": [
            f"Expand Lerato's expression: {a}({b}x + {c}) = {exp_m}x + {exp_c} (1 mark)",
            f"State equivalence: Yes (1 mark)",
            f"Evaluate for x = {x_test}: y = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Use the distributive law: ${a} \\times {b}x = {exp_m}x$ and ${a} \\times {c} = {exp_c}$.",
            f"Both expressions simplify to ${exp_m}x + {exp_c}$, so they are equivalent.",
            f"For $x = {x_test}$: $y = {exp_m}({x_test}) + {exp_c} = {ans_val}$.",
        ],
        "misconception_tags": ["algebraic_equivalence_verification_error"],
        "diagram_spec": None,
    }


def arch_27_equivalent_formulae_subtraction_factored_form(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    k = rng.randint(2, 4)
    c = rng.randint(1, 3)
    # y = m*(x - k) + c = m*x - m*k + c
    expanded_c = -m * k + c

    return {
        "title": "Equivalent Formulae (Factored vs Expanded Form)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "27_equivalent_formulae_subtraction_factored_form",
        "difficulty": "hard",
        "question_text": (
            f"Expand and simplify the algebraic formula:\n\n"
            f"$$y = {m}(x - {k}) + {c}$$\n\n"
            f"Express your answer in the form $y = mx + c$ (or $y = mx - c$)."
        ),
        "correct_answer": f"y = {m}x - {abs(expanded_c)}" if expanded_c < 0 else f"y = {m}x + {expanded_c}",
        "marking_schema": [
            f"Expand brackets: {m}x - {m * k} (1 mark)",
            f"Combine constant terms: -{m * k} + {c} = {expanded_c} (1 mark)",
            f"State simplified formula (1 mark)",
        ],
        "hints": [
            f"Multiply through by {m}: ${m}(x - {k}) = {m}x - {m * k}$.",
            f"Combine like terms: ${m}x - {m * k} + {c} = {m}x {'- ' + str(abs(expanded_c)) if expanded_c < 0 else '+ ' + str(expanded_c)}$.",
        ],
        "misconception_tags": ["distributive_expansion_sign_error"],
        "diagram_spec": None,
    }


def arch_28_quadratic_function_table_evaluation(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(1, 5)
    # y = x^2 + c
    x_test = rng.randint(3, 8)
    ans_val = (x_test ** 2) + c

    return {
        "title": "Quadratic Function Table Evaluation",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "28_quadratic_function_table_evaluation",
        "difficulty": "medium",
        "question_text": (
            f"A non-linear function is defined by the quadratic rule:\n\n"
            f"$$y = x^2 + {c}$$\n\n"
            f"Calculate the output $y$ when the input is $x = {x_test}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Square the input: {x_test}^2 = {x_test ** 2} (1 mark)",
            f"Add constant: {x_test ** 2} + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Square $x$ first: ${x_test}^2 = {x_test} \\times {x_test} = {x_test ** 2}$.",
            f"Then add {c}: ${x_test ** 2} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["order_of_operations_powers_error"],
        "diagram_spec": None,
    }


def arch_29_quadratic_function_calculating_input_from_square_output(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(1, 6)
    in_val = rng.randint(3, 9)
    out_val = (in_val ** 2) + c

    return {
        "title": "Quadratic Function (Finding Positive Input from Output)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "29_quadratic_function_calculating_input_from_square_output",
        "difficulty": "hard",
        "question_text": (
            f"For the quadratic function $y = x^2 + {c}$:\n\n"
            f"If the output is $y = {out_val}$, determine the positive input value $x$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Subtract constant: x^2 = {out_val} - {c} = {out_val - c} (1 mark)",
            f"Take square root: x = sqrt({out_val - c}) = {in_val} (1 mark)",
        ],
        "hints": [
            f"Subtract {c} from {out_val}: $x^2 = {out_val} - {c} = {out_val - c}$.",
            f"Take the square root: $x = \\sqrt{{{out_val - c}}} = {in_val}$.",
        ],
        "misconception_tags": ["quadratic_inverse_square_root_error"],
        "diagram_spec": None,
    }


def arch_30_inverse_proportion_table_evaluation(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([24, 36, 48, 60, 72, 120])
    divs = [d for d in range(2, 13) if k % d == 0]
    x_test = rng.choice(divs)
    ans_val = k // x_test

    return {
        "title": "Inverse Proportion Table Evaluation",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "30_inverse_proportion_table_evaluation",
        "difficulty": "medium",
        "question_text": (
            f"Two quantities are in inverse proportion according to the formula:\n\n"
            f"$$y = \\frac{{{k}}}{{x}}$$\n\n"
            f"Calculate the value of $y$ when $x = {x_test}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Divide k by x: {k} / {x_test} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_test}$ into the denominator.",
            f"$y = \\frac{{{k}}}{{{x_test}}} = {ans_val}$.",
        ],
        "misconception_tags": ["inverse_proportion_division_error"],
        "diagram_spec": None,
    }


def arch_31_inverse_proportion_constant_product_rule(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([40, 60, 80, 100, 120])
    divs = [d for d in range(2, 20) if k % d == 0]
    x1 = divs[1]
    y1 = k // x1
    x2 = divs[-2]
    y2 = k // x2

    return {
        "title": "Inverse Proportion (Constant Product Property)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "31_inverse_proportion_constant_product_rule",
        "difficulty": "hard",
        "question_text": (
            f"In an inversely proportional relationship, the product $x \\times y$ is constant:\n\n"
            f"| $x$ | {x1} | {x2} |\n"
            f"| :--- | :---: | :---: |\n"
            f"| $y$ | {y1} | $k$ |\n\n"
            f"State the value of the constant product ($x \\cdot y$), and determine the value of $k$."
        ),
        "correct_answer": f"Product = {k}; k = {y2}",
        "marking_schema": [
            f"Calculate constant product: {x1} * {y1} = {k} (1 mark)",
            f"Solve for k: k = {k} / {x2} = {y2} (1 mark)",
        ],
        "hints": [
            f"The product of each column is constant: ${x1} \\times {y1} = {k}$.",
            f"Therefore, ${x2} \\times k = {k} \\implies k = \\frac{{{k}}}{{{x2}}} = {y2}$.",
        ],
        "misconception_tags": ["direct_vs_inverse_proportion_confusion"],
        "diagram_spec": None,
    }


def arch_32_unit_conversion_hours_to_minutes_function(rng: random.Random) -> Dict[str, Any]:
    hours = rng.randint(3, 8)
    ans_min = hours * 60

    return {
        "title": "Unit Conversion Function (Hours to Minutes)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "32_unit_conversion_hours_to_minutes_function",
        "difficulty": "easy",
        "question_text": (
            f"The function relating time in hours ($h$) to time in minutes ($m$) is given by $m = 60h$.\n\n"
            f"Use this formula to calculate the number of minutes in **{hours} hours**."
        ),
        "correct_answer": str(ans_min),
        "marking_schema": [
            f"Apply formula m = 60h: 60 * {hours} = {ans_min} minutes (1 mark)",
        ],
        "hints": [
            f"Multiply the number of hours by 60.",
            f"$m = 60 \\times {hours} = {ans_min}\\text{{ minutes}}$.",
        ],
        "misconception_tags": ["time_conversion_factor_error"],
        "diagram_spec": None,
    }


def arch_33_unit_conversion_kilometers_to_meters_function(rng: random.Random) -> Dict[str, Any]:
    km = rng.choice([2.5, 3.2, 4.75, 5.5, 6.1])
    ans_m = int(km * 1000)
    km_str = str(km).replace(".", ",")

    return {
        "title": "Unit Conversion Function (Kilometers to Meters)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "33_unit_conversion_kilometers_to_meters_function",
        "difficulty": "easy",
        "question_text": (
            f"Distance in meters ($m$) is a function of distance in kilometers ($k$): $m = 1000k$.\n\n"
            f"Calculate the distance in meters for **{km_str} km**."
        ),
        "correct_answer": str(ans_m),
        "marking_schema": [
            f"Multiply by 1000: {km} * 1000 = {ans_m} m (1 mark)",
        ],
        "hints": [
            f"There are 1 000 meters in 1 kilometer.",
            f"${km} \\times 1000 = {ans_m}\\text{{ m}}$.",
        ],
        "misconception_tags": ["metric_conversion_decimal_shift_error"],
        "diagram_spec": None,
    }


def arch_34_unit_conversion_litres_to_millilitres_function(rng: random.Random) -> Dict[str, Any]:
    litres = rng.choice([1.25, 2.5, 3.75, 4.2])
    ans_ml = int(litres * 1000)
    l_str = str(litres).replace(".", ",")

    return {
        "title": "Unit Conversion Function (Litres to Millilitres)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "34_unit_conversion_litres_to_millilitres_function",
        "difficulty": "easy",
        "question_text": (
            f"Volume in millilitres ($ml$) is related to volume in litres ($L$) by the function $ml = 1000L$.\n\n"
            f"Calculate the volume in millilitres for **{l_str} L**."
        ),
        "correct_answer": str(ans_ml),
        "marking_schema": [
            f"Multiply by 1000: {litres} * 1000 = {ans_ml} ml (1 mark)",
        ],
        "hints": [
            f"${litres} \\times 1000 = {ans_ml}\\text{{ ml}}$.",
        ],
        "misconception_tags": ["capacity_conversion_factor_error"],
        "diagram_spec": None,
    }


def arch_35_temperature_conversion_formula_evaluation(rng: random.Random) -> Dict[str, Any]:
    celsius = rng.choice([15, 20, 25, 30, 35])
    # F = (9/5)*C + 32
    fahrenheit = int((9 * celsius) / 5 + 32)

    return {
        "title": "Temperature Conversion Formula Evaluation",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "35_temperature_conversion_formula_evaluation",
        "difficulty": "hard",
        "question_text": (
            f"The formula to convert temperature from degrees Celsius ($C$) to degrees Fahrenheit ($F$) is:\n\n"
            f"$$F = \\frac{{9}}{{5}}C + 32$$\n\n"
            f"Calculate the temperature in degrees Fahrenheit when $C = {celsius}^\\circ\\text{{C}}$."
        ),
        "correct_answer": f"{fahrenheit}°F",
        "marking_schema": [
            f"Multiply (9/5) * {celsius} = {(9 * celsius) // 5} (1 mark)",
            f"Add 32: {(9 * celsius) // 5} + 32 = {fahrenheit} (1 mark)",
        ],
        "hints": [
            f"First calculate $\\frac{{9 \\times {celsius}}}{{5}} = {(9 * celsius) // 5}$.",
            f"Then add 32: ${(9 * celsius) // 5} + 32 = {fahrenheit}^\\circ\\text{{F}}$.",
        ],
        "misconception_tags": ["temperature_formula_bodmas_error"],
        "diagram_spec": None,
    }


def arch_36_distance_speed_time_direct_formula_d_vt(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([60, 75, 80, 90, 100, 120])
    time_h = rng.randint(2, 6)
    dist = speed * time_h

    return {
        "title": "Distance-Speed-Time Linear Function",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "36_distance_speed_time_direct_formula_d_vt",
        "difficulty": "medium",
        "question_text": (
            f"A vehicle travels at a constant speed of **{speed} km/h** according to the distance function $d = {speed}t$, "
            f"where $d$ is distance in km and $t$ is travel time in hours.\n\n"
            f"Calculate the distance travelled after **{time_h} hours**."
        ),
        "correct_answer": f"{dist} km",
        "marking_schema": [
            f"Substitute t = {time_h}: d = {speed} * {time_h} = {dist} km (1 mark)",
        ],
        "hints": [
            f"Distance = Speed $\\times$ Time.",
            f"$d = {speed} \\times {time_h} = {dist}\\text{{ km}}$.",
        ],
        "misconception_tags": ["speed_distance_time_inversion_error"],
        "diagram_spec": None,
    }


def arch_37_cost_function_fixed_fee_plus_rate_per_kg(rng: random.Random) -> Dict[str, Any]:
    fixed = rng.randint(25, 50)
    rate = rng.randint(10, 20)
    mass_kg = rng.randint(4, 12)
    total_cost = fixed + rate * mass_kg

    return {
        "title": "Linear Cost Function (Courier Delivery)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "37_cost_function_fixed_fee_plus_rate_per_kg",
        "difficulty": "medium",
        "question_text": (
            f"A courier service charges a standard booking fee of $\\text{{R}}{fixed}$ plus $\\text{{R}}{rate}$ per kilogram.\n\n"
            f"Write the cost function $C(m)$ in terms of parcel mass $m$ (in kg), "
            f"and calculate the total delivery fee for a parcel with a mass of **{mass_kg} kg**."
        ),
        "correct_answer": f"R{total_cost}",
        "marking_schema": [
            f"State formula C = {rate}m + {fixed} (1 mark)",
            f"Evaluate for m = {mass_kg}: {rate}({mass_kg}) + {fixed} = R{total_cost} (1 mark)",
        ],
        "hints": [
            f"Cost formula: $C = {rate}m + {fixed}$.",
            f"Substitute $m = {mass_kg}$: $C = ({rate} \\times {mass_kg}) + {fixed} = {rate * mass_kg} + {fixed} = \\text{{R}}{total_cost}$.",
        ],
        "misconception_tags": ["linear_cost_modeling_error"],
        "diagram_spec": None,
    }


def arch_38_cost_function_hire_purchase_deposit_plus_monthly(rng: random.Random) -> Dict[str, Any]:
    deposit = rng.randint(200, 500)
    monthly = rng.randint(150, 350)
    months = rng.choice([6, 12, 18, 24])
    total_paid = deposit + monthly * months

    return {
        "title": "Hire Purchase Cost Function",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "38_cost_function_hire_purchase_deposit_plus_monthly",
        "difficulty": "medium",
        "question_text": (
            f"An appliance is purchased on hire purchase with a deposit of $\\text{{R}}{deposit}$ and monthly instalments of $\\text{{R}}{monthly}$.\n\n"
            f"Calculate the total amount paid after **{months} months** using the relationship $T = {monthly}n + {deposit}$."
        ),
        "correct_answer": f"R{total_paid}",
        "marking_schema": [
            f"Calculate total monthly payments: {monthly} * {months} = R{monthly * months} (1 mark)",
            f"Add deposit: R{deposit} + R{monthly * months} = R{total_paid} (1 mark)",
        ],
        "hints": [
            f"Instalments = ${monthly} \\times {months} = \\text{{R}}{monthly * months}$.",
            f"Total = $\\text{{R}}{deposit} + \\text{{R}}{monthly * months} = \\text{{R}}{total_paid}$.",
        ],
        "misconception_tags": ["hire_purchase_deposit_omission"],
        "diagram_spec": None,
    }


def arch_39_geometric_arrangement_red_and_black_squares_formula(rng: random.Random) -> Dict[str, Any]:
    # Arrangement n: red squares = 4n + 2
    n_arr = rng.choice([10, 15, 20, 25])
    ans_red = 4 * n_arr + 2

    return {
        "title": "Geometric Arrangement Rule (Red Squares)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "39_geometric_arrangement_red_and_black_squares_formula",
        "difficulty": "medium",
        "question_text": (
            f"Square arrangements are constructed where the number of red border squares is given by the function:\n\n"
            f"$$y = 4x + 2$$\n\n"
            f"where $x$ is the arrangement number and $y$ is the number of red squares.\n"
            f"Calculate the number of red squares in **arrangement {n_arr}**."
        ),
        "correct_answer": str(ans_red),
        "marking_schema": [
            f"Substitute x = {n_arr}: y = 4({n_arr}) + 2 = {ans_red} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {n_arr}$ into $y = 4x + 2$.",
            f"$y = 4({n_arr}) + 2 = {4 * n_arr} + 2 = {ans_red}$.",
        ],
        "misconception_tags": ["arrangement_formula_substitution_error"],
        "diagram_spec": None,
    }


def arch_40_geometric_tile_arrangement_formula_matching(rng: random.Random) -> Dict[str, Any]:
    # Testing matching formula
    # Let y = 2x + 4
    x1, y1 = 1, 6
    x2, y2 = 2, 8
    x3, y3 = 3, 10
    ans_formula = "y = 2x + 4"

    return {
        "title": "Matching Formula to Geometric Arrangement Data",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "40_geometric_tile_arrangement_formula_matching",
        "difficulty": "medium",
        "question_text": (
            f"An arrangement sequence records the following counts:\n\n"
            f"* Arrangement 1 has 6 tiles\n"
            f"* Arrangement 2 has 8 tiles\n"
            f"* Arrangement 3 has 10 tiles\n\n"
            f"Which of the following formulae correctly models this pattern?\n"
            f"* **A:** $y = x^2 + 5$\n"
            f"* **B:** $y = 2x + 4$\n"
            f"* **C:** $y = 4x + 2$\n\n"
            f"State the correct letter (**A**, **B**, or **C**)."
        ),
        "correct_answer": "B",
        "marking_schema": [
            "Test input-output pairs against candidates (1 mark)",
            "Identify B as the matching model (1 mark)",
        ],
        "hints": [
            "Notice the constant difference is $8 - 6 = 2$, so the multiplier must be 2.",
            "Test $x = 1$ in formula B: $y = 2(1) + 4 = 6$.",
            "Formula B is correct.",
        ],
        "misconception_tags": ["pattern_formula_selection_error"],
        "diagram_spec": None,
    }


def arch_41_linear_function_rate_of_change_gradient_concept(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(4, 9)
    c = rng.randint(2, 8)

    return {
        "title": "Rate of Change (Gradient Concept in Linear Functions)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "41_linear_function_rate_of_change_gradient_concept",
        "difficulty": "medium",
        "question_text": (
            f"Consider the linear function $y = {m}x + {c}$.\n\n"
            f"By how much does the output $y$ change each time the input $x$ increases by $1$ unit? "
            f"(State the constant rate of change)."
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Identify coefficient of x as the rate of change: {m} (1 mark)",
        ],
        "hints": [
            f"In the general form $y = mx + c$, $m$ represents the rate of change.",
            f"Here the coefficient of $x$ is {m}.",
            f"Every time $x$ increases by 1, $y$ increases by {m}.",
        ],
        "misconception_tags": ["rate_of_change_vs_constant_term_confusion"],
        "diagram_spec": None,
    }


def arch_42_linear_function_constant_term_zero_input_intercept(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 8)
    c = rng.randint(5, 20)

    return {
        "title": "Zero-Input Output (Constant Term / y-Intercept)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "42_linear_function_constant_term_zero_input_intercept",
        "difficulty": "easy",
        "question_text": (
            f"A relationship is described by $y = {m}x + {c}$.\n\n"
            f"What is the output value $y$ when the input is zero ($x = 0$)?"
        ),
        "correct_answer": str(c),
        "marking_schema": [
            f"Substitute x = 0: y = {m}(0) + {c} = {c} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = 0$ into the formula.",
            f"$y = {m}(0) + {c} = 0 + {c} = {c}$.",
        ],
        "misconception_tags": ["zero_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_43_finding_output_for_large_input_in_function(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(4, 8)
    c = rng.randint(3, 9)
    in_val = rng.choice([50, 75, 100, 200])
    ans_val = m * in_val + c

    return {
        "title": "Evaluating Function for Large Input (x = 50, 100)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "43_finding_output_for_large_input_in_function",
        "difficulty": "medium",
        "question_text": (
            f"Use the function rule $y = {m}x + {c}$ to calculate the output value $y$ when the input is $x = {in_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Substitute x = {in_val}: y = {m}({in_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Multiply {m} by {in_val}: ${m} \\times {in_val} = {m * in_val}$.",
            f"Add {c}: ${m * in_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["large_input_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_44_finding_input_for_large_output_in_function(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(4, 7)
    c = rng.randint(2, 9)
    in_val = rng.randint(20, 50)
    out_val = m * in_val + c

    return {
        "title": "Finding Input for Given Output (Inverse Linear Calculation)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "44_finding_input_for_large_output_in_function",
        "difficulty": "hard",
        "question_text": (
            f"For the function $y = {m}x + {c}$, find the input value $x$ that results in an output of $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Set up equation {m}x + {c} = {out_val} (1 mark)",
            f"Solve for x: {m}x = {out_val - c} => x = {in_val} (1 mark)",
        ],
        "hints": [
            f"Set up the equation: ${m}x + {c} = {out_val}$.",
            f"Subtract {c}: ${m}x = {out_val - c}$.",
            f"Divide by {m}: $x = \\frac{{{out_val - c}}}{{{m}}} = {in_val}$.",
        ],
        "misconception_tags": ["equation_inverse_order_slip"],
        "diagram_spec": None,
    }


def arch_45_comparing_two_competing_linear_functions(rng: random.Random) -> Dict[str, Any]:
    # Plan A: y = 10x + 50
    # Plan B: y = 15x + 20
    x_test = rng.randint(4, 9)
    cost_a = 10 * x_test + 50
    cost_b = 15 * x_test + 20
    cheaper = "Plan A" if cost_a < cost_b else "Plan B" if cost_b < cost_a else "Both are equal"

    return {
        "title": "Comparing Two Competing Linear Functions",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "45_comparing_two_competing_linear_functions",
        "difficulty": "hard",
        "question_text": (
            f"Two internet service providers charge according to the following functions:\n\n"
            f"* **Plan A:** $C = 10g + 50$\n"
            f"* **Plan B:** $C = 15g + 20$\n\n"
            f"where $C$ is cost in Rand and $g$ is gigabytes of data used.\n"
            f"Which plan is cheaper for a customer using **{x_test} GB** of data? State **Plan A** or **Plan B**."
        ),
        "correct_answer": cheaper,
        "marking_schema": [
            f"Calculate Plan A cost for g = {x_test}: 10({x_test}) + 50 = R{cost_a} (1 mark)",
            f"Calculate Plan B cost for g = {x_test}: 15({x_test}) + 20 = R{cost_b} (1 mark)",
            f"Conclude cheaper plan: {cheaper} (1 mark)",
        ],
        "hints": [
            f"Plan A: $10({x_test}) + 50 = \\text{{R}}{cost_a}$.",
            f"Plan B: $15({x_test}) + 20 = \\text{{R}}{cost_b}$.",
            f"Compare the costs to see which is lower: {cheaper}.",
        ],
        "misconception_tags": ["function_comparison_evaluation_error"],
        "diagram_spec": None,
    }


def arch_46_break_even_input_value_for_two_linear_plans(rng: random.Random) -> Dict[str, Any]:
    # 5x + 60 = 8x + 30 => 3x = 30 => x = 10
    n_break = rng.choice([5, 6, 8, 10, 12])
    diff_m = rng.choice([2, 3, 4])
    base_b = rng.randint(10, 30)
    base_a = base_b + diff_m * n_break
    m_b = 9
    m_a = m_b - diff_m

    return {
        "title": "Break-Even Input for Two Linear Functions",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "46_break_even_input_value_for_two_linear_plans",
        "difficulty": "hard",
        "question_text": (
            f"Two mobile network options charge the following total costs:\n\n"
            f"* **Option 1:** $C_1 = {m_a}m + {base_a}$\n"
            f"* **Option 2:** $C_2 = {m_b}m + {base_b}$\n\n"
            f"Find the number of minutes ($m$) where both options cost exactly the same amount."
        ),
        "correct_answer": str(n_break),
        "marking_schema": [
            f"Equate C_1 = C_2: {m_a}m + {base_a} = {m_b}m + {base_b} (1 mark)",
            f"Solve for m: {diff_m}m = {base_a - base_b} => m = {n_break} (2 marks)",
        ],
        "hints": [
            f"Set ${m_a}m + {base_a} = {m_b}m + {base_b}$.",
            f"Subtract ${m_a}m$: ${base_a} = {diff_m}m + {base_b}$.",
            f"Subtract ${base_b}$: ${diff_m}m = {base_a - base_b} \\implies m = {n_break}$.",
        ],
        "misconception_tags": ["break_even_equation_solving_error"],
        "diagram_spec": None,
    }


def arch_47_evaluating_composite_function_two_stage_rule(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 5)
    c = rng.randint(1, 4)
    # Machine 1: u = a*x + b
    # Machine 2: y = u - c
    in_val = rng.randint(3, 7)
    u_val = a * in_val + b
    out_val = u_val - c

    return {
        "title": "Two-Stage Connected Function Machines",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "47_evaluating_composite_function_two_stage_rule",
        "difficulty": "medium",
        "question_text": (
            f"Two function machines are connected in series:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\text{{Machine 1: }} u = {a}x + {b}}} \\longrightarrow \\boxed{{\\text{{Machine 2: }} y = u - {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the final output $y$ when the initial input is $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Machine 1 intermediate output u = {a}({in_val}) + {b} = {u_val} (1 mark)",
            f"Machine 2 final output y = {u_val} - {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"First calculate $u = {a}({in_val}) + {b} = {u_val}$.",
            f"Now pass $u = {u_val}$ into Machine 2: $y = {u_val} - {c} = {out_val}$.",
        ],
        "misconception_tags": ["composite_function_chain_error"],
        "diagram_spec": None,
    }


def arch_48_function_machine_black_box_mystery_rule(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 5, 6])
    c = rng.choice([2, 4, 7])
    # mystery rule y = mx + c
    x1, y1 = 2, m * 2 + c
    x2, y2 = 4, m * 4 + c
    x_test = 5
    ans_val = m * x_test + c

    return {
        "title": "Black Box Function Machine Mystery Rule",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "48_function_machine_black_box_mystery_rule",
        "difficulty": "hard",
        "question_text": (
            f"A black box function machine produces the following test results:\n\n"
            f"* Input $2 \\longrightarrow$ Output ${y1}$\n"
            f"* Input $4 \\longrightarrow$ Output ${y2}$\n\n"
            f"Determine the underlying linear rule and find the output when the input is $x = {x_test}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Find rate of change: ({y2} - {y1}) / (4 - 2) = {m} (1 mark)",
            f"Deduce rule y = {m}x + {c} (1 mark)",
            f"Evaluate for x = {x_test}: y = {m}({x_test}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"When input changes by 2 (from 2 to 4), output changes by ${y2} - {y1} = {y2 - y1}$.",
            f"Rate of change $m = \\frac{{{y2 - y1}}}{{2}} = {m}$.",
            f"Rule: $y = {m}x + {c}$. For $x = {x_test}$: $y = {m}({x_test}) + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["rate_of_change_delta_step_division_error"],
        "diagram_spec": None,
    }


def arch_49_distinguishing_linear_vs_non_linear_relationships_from_tables(rng: random.Random) -> Dict[str, Any]:
    is_linear = rng.choice([True, False])
    if is_linear:
        m = rng.randint(3, 6)
        c = rng.randint(1, 5)
        x_vals = [1, 2, 3, 4]
        y_vals = [m * x + c for x in x_vals]
        ans = "linear"
        reason = f"the differences between consecutive outputs are constant (+{m})."
    else:
        c = rng.randint(1, 4)
        x_vals = [1, 2, 3, 4]
        y_vals = [(x ** 2) + c for x in x_vals]
        ans = "non-linear"
        reason = f"the differences between consecutive outputs are not constant ({y_vals[1]-y_vals[0]}, {y_vals[2]-y_vals[1]}, {y_vals[3]-y_vals[2]})."

    return {
        "title": "Distinguishing Linear vs Non-Linear Functions",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "49_distinguishing_linear_vs_non_linear_relationships_from_tables",
        "difficulty": "medium",
        "question_text": (
            f"Classify whether the relationship in the table represents a **linear** or **non-linear** function:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Provide your answer as either **linear** or **non-linear**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Examine first differences of outputs (1 mark)",
            f"Correctly classify as {ans} because {reason} (1 mark)",
        ],
        "hints": [
            f"Calculate the differences between adjacent outputs: ${y_vals[1]} - {y_vals[0]}$, ${y_vals[2]} - {y_vals[1]}$, ${y_vals[3]} - {y_vals[2]}$.",
            f"A function is linear only if the first difference is constant.",
            f"Since {reason}, it is {ans}.",
        ],
        "misconception_tags": ["linearity_first_difference_test_error"],
        "diagram_spec": None,
    }


def arch_50_multiple_representations_verbal_table_formula_mapping(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(2, 6)
    x_val = 5
    ans_val = m * x_val + c

    return {
        "title": "Multiple Representations (Verbal, Table, and Formula)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "50_multiple_representations_verbal_table_formula_mapping",
        "difficulty": "medium",
        "question_text": (
            f"A function is represented in three distinct mathematical forms:\n\n"
            f"1. **Verbal description:** \"Multiply the input by ${m}$ and then add ${c}$.\"\n"
            f"2. **Flow diagram:** $x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow y$\n"
            f"3. **Algebraic equation:** $y = {m}x + {c}$\n\n"
            f"Calculate the output $y$ when the input is $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Evaluate y = {m}({x_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Apply any of the equivalent representations to input $x = {x_val}$.",
            f"$y = {m}({x_val}) + {c} = {m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["representation_translation_slip"],
        "diagram_spec": None,
    }
