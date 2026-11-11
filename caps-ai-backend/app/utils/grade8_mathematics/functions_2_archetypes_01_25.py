"""
Grade 8 Mathematics - Functions and Relationships 2 Archetypes 01 to 25.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 2.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def arch_01_evaluating_linear_formula_positive_slope(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 7, 8])
    c = rng.randint(2, 9)
    x_val = rng.randint(4, 12)
    ans_val = m * x_val + c

    return {
        "title": "Evaluating Linear Formula (Positive Slope)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "01_evaluating_linear_formula_positive_slope",
        "difficulty": "easy",
        "question_text": (
            f"A function is defined by the formula:\n\n"
            f"$$y = {m}x + {c}$$\n\n"
            f"Calculate the value of $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Substitute x = {x_val}: y = {m}({x_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute {x_val} in place of $x$.",
            f"$y = {m} \\times {x_val} + {c} = {m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["linear_formula_substitution_error"],
        "diagram_spec": None,
    }


def arch_02_evaluating_linear_formula_negative_slope(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(25, 60)
    x_val = rng.randint(2, 6)
    ans_val = -m * x_val + c

    return {
        "title": "Evaluating Linear Formula (Negative Slope)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "02_evaluating_linear_formula_negative_slope",
        "difficulty": "medium",
        "question_text": (
            f"A decreasing relationship is modeled by the formula:\n\n"
            f"$$y = -{m}x + {c}$$\n\n"
            f"Determine the value of the output $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Multiply -{m} by {x_val}: -{m * x_val} (1 mark)",
            f"Add {c}: -{m * x_val} + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_val}$: $y = -{m}({x_val}) + {c}$.",
            f"$y = -{m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["negative_slope_evaluation_error"],
        "diagram_spec": None,
    }


def arch_03_evaluating_bracketed_formula_distributive(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(2, 4)
    c = rng.randint(1, 5)
    x_val = rng.randint(3, 8)
    ans_val = a * (b * x_val + c)

    return {
        "title": "Evaluating Bracketed Linear Formula",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "03_evaluating_bracketed_formula_distributive",
        "difficulty": "medium",
        "question_text": (
            f"Use the bracketed formula:\n\n"
            f"$$y = {a}({b}x + {c})$$\n\n"
            f"Calculate the output $y$ when the input is $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Evaluate inside brackets: {b}({x_val}) + {c} = {b * x_val + c} (1 mark)",
            f"Multiply by {a}: {a} * {b * x_val + c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Evaluate inside parentheses first: ${b}({x_val}) + {c} = {b * x_val + c}$.",
            f"Then multiply by {a}: ${a} \\times {b * x_val + c} = {ans_val}$.",
        ],
        "misconception_tags": ["bracket_evaluation_order_error"],
        "diagram_spec": None,
    }


def arch_04_evaluating_quadratic_formula_simple(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(5, 15)
    ans_val = x_val ** 2

    return {
        "title": "Evaluating Simple Quadratic Formula (y = x^2)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "04_evaluating_quadratic_formula_simple",
        "difficulty": "easy",
        "question_text": (
            f"Consider the square relationship defined by $y = x^2$.\n\n"
            f"Calculate the value of $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Square the input: {x_val}^2 = {ans_val} (1 mark)",
        ],
        "hints": [
            f"$y = ({x_val})^2 = {x_val} \\times {x_val} = {ans_val}$.",
        ],
        "misconception_tags": ["squaring_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_05_evaluating_quadratic_formula_with_constant(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 9)
    x_val = rng.randint(4, 11)
    ans_val = (x_val ** 2) + c

    return {
        "title": "Evaluating Quadratic Formula with Constant (y = x^2 + c)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "05_evaluating_quadratic_formula_with_constant",
        "difficulty": "medium",
        "question_text": (
            f"A non-linear relationship follows the formula $y = x^2 + {c}$.\n\n"
            f"Calculate the value of $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Square input: {x_val}^2 = {x_val ** 2} (1 mark)",
            f"Add constant: {x_val ** 2} + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"First square {x_val}: ${x_val}^2 = {x_val ** 2}$.",
            f"Then add {c}: ${x_val ** 2} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["quadratic_shift_evaluation_error"],
        "diagram_spec": None,
    }


def arch_06_evaluating_exponential_formula_base_two(rng: random.Random) -> Dict[str, Any]:
    exp = rng.choice([3, 4, 5, 6, 7])
    ans_val = 2 ** exp

    return {
        "title": "Evaluating Exponential Formula (Base 2)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "06_evaluating_exponential_formula_base_two",
        "difficulty": "medium",
        "question_text": (
            f"An exponential function is defined by $y = 2^x$, where the independent variable $x$ is in the exponent.\n\n"
            f"Determine the value of $y$ when $x = {exp}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Evaluate power: 2^{exp} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {exp}$: $y = 2^{{{exp}}}$.",
            f"Multiply 2 by itself {exp} times: $2^{{{exp}}} = {ans_val}$.",
        ],
        "misconception_tags": ["confusing_base_power_with_multiplication"],
        "diagram_spec": None,
    }


def arch_07_evaluating_exponential_formula_base_three(rng: random.Random) -> Dict[str, Any]:
    exp = rng.choice([2, 3, 4, 5])
    ans_val = 3 ** exp

    return {
        "title": "Evaluating Exponential Formula (Base 3)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "07_evaluating_exponential_formula_base_three",
        "difficulty": "medium",
        "question_text": (
            f"Consider the exponential growth formula $y = 3^x$.\n\n"
            f"Calculate the value of $y$ when $x = {exp}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Evaluate 3^{exp} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"$y = 3^{{{exp}}}$.",
            f"Multiply 3 by itself {exp} times: $3^{{{exp}}} = {ans_val}$.",
        ],
        "misconception_tags": ["exponential_powers_of_three_slip"],
        "diagram_spec": None,
    }


def arch_08_evaluating_exponential_formula_shifted_exponent(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([2, 3, 4])
    ans_val = 3 ** (x_val + 1)

    return {
        "title": "Evaluating Exponential Formula (Shifted Exponent y = 3^{x+1})",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "08_evaluating_exponential_formula_shifted_exponent",
        "difficulty": "hard",
        "question_text": (
            f"Given the exponential function $y = 3^{{x + 1}}$:\n\n"
            f"Calculate the output value $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Add exponent: {x_val} + 1 = {x_val + 1} (1 mark)",
            f"Evaluate 3^{x_val + 1} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"First find the exponent: $x + 1 = {x_val} + 1 = {x_val + 1}$.",
            f"Then compute $3^{{{x_val + 1}}} = {ans_val}$.",
        ],
        "misconception_tags": ["shifted_exponent_evaluation_error"],
        "diagram_spec": None,
    }


def arch_09_evaluating_cubic_formula(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([2, 3, 4, 5])
    ans_val = x_val ** 3

    return {
        "title": "Evaluating Cubic Formula (y = x^3)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "09_evaluating_cubic_formula",
        "difficulty": "medium",
        "question_text": (
            f"A cubic function is given by the formula $y = x^3$.\n\n"
            f"Calculate the output $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Cube the input: {x_val}^3 = {ans_val} (1 mark)",
        ],
        "hints": [
            f"$y = ({x_val})^3 = {x_val} \\times {x_val} \\times {x_val} = {ans_val}$.",
        ],
        "misconception_tags": ["cubic_power_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_10_evaluating_inverse_proportion_formula(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([48, 60, 72, 84, 96])
    divs = [d for d in range(3, 13) if k % d == 0]
    x_val = rng.choice(divs)
    ans_val = k // x_val

    return {
        "title": "Evaluating Inverse Proportion Formula (y = k / x)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "10_evaluating_inverse_proportion_formula",
        "difficulty": "medium",
        "question_text": (
            f"An inverse proportion formula is given by:\n\n"
            f"$$y = \\frac{{{k}}}{{x}}$$\n\n"
            f"Determine the value of $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Divide {k} by {x_val}: {k} / {x_val} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {x_val}$ into the denominator.",
            f"$y = \\frac{{{k}}}{{{x_val}}} = {ans_val}$.",
        ],
        "misconception_tags": ["inverse_proportion_calculation_error"],
        "diagram_spec": None,
    }


def arch_11_completing_table_for_exponential_function(rng: random.Random) -> Dict[str, Any]:
    # y = 2^x
    x_vals = [1, 2, 3, 4, 6]
    y_vals = [2 ** x for x in x_vals]
    target_x = x_vals[4]
    target_y = y_vals[4]

    return {
        "title": "Completing Table for Exponential Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "11_completing_table_for_exponential_function",
        "difficulty": "medium",
        "question_text": (
            f"The table below shows input-output pairs for the exponential function $y = 2^x$:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 | {target_x} |\n"
            f"| :--- | :---: | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} | $k$ |\n\n"
            f"Calculate the missing value $k$."
        ),
        "correct_answer": str(target_y),
        "marking_schema": [
            f"Substitute x = {target_x}: y = 2^{target_x} = {target_y} (1 mark)",
        ],
        "hints": [
            f"Use the rule $y = 2^x$.",
            f"For $x = {target_x}$: $k = 2^{{{target_x}}} = {target_y}$.",
        ],
        "misconception_tags": ["exponential_table_missing_value_error"],
        "diagram_spec": None,
    }


def arch_12_completing_table_for_quadratic_function(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(1, 4)
    x_vals = [1, 2, 3, 5]
    y_vals = [(x ** 2) + c for x in x_vals]
    target_x = x_vals[3]
    target_y = y_vals[3]

    return {
        "title": "Completing Table for Quadratic Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "12_completing_table_for_quadratic_function",
        "difficulty": "medium",
        "question_text": (
            f"A quadratic table follows the rule $y = x^2 + {c}$:\n\n"
            f"| $x$ | 1 | 2 | 3 | {target_x} |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | $m$ |\n\n"
            f"Find the value of $m$."
        ),
        "correct_answer": str(target_y),
        "marking_schema": [
            f"Substitute x = {target_x}: y = {target_x}^2 + {c} = {target_y} (1 mark)",
        ],
        "hints": [
            f"Square the input: ${target_x}^2 = {target_x ** 2}$.",
            f"Add {c}: ${target_x ** 2} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["quadratic_table_substitution_slip"],
        "diagram_spec": None,
    }


def arch_13_completing_table_non_consecutive_inputs_linear(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.randint(2, 7)
    x_vals = [1, 4, 10, 25]
    y_vals = [m * x + c for x in x_vals]
    target_x = x_vals[3]
    target_y = y_vals[3]

    return {
        "title": "Completing Table with Non-Consecutive Inputs",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "13_completing_table_non_consecutive_inputs_linear",
        "difficulty": "hard",
        "question_text": (
            f"Notice that the input values in the table are not consecutive:\n\n"
            f"| $x$ | 1 | 4 | 10 | {target_x} |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | $p$ |\n\n"
            f"The relationship is linear with formula $y = {m}x + {c}$. Calculate the value of $p$."
        ),
        "correct_answer": str(target_y),
        "marking_schema": [
            f"Substitute x = {target_x} into y = {m}x + {c}: {m}({target_x}) + {c} = {target_y} (1 mark)",
        ],
        "hints": [
            f"Do not simply add a difference to the previous term since the inputs jump from 10 to {target_x}.",
            f"Substitute directly into the formula: $p = {m}({target_x}) + {c} = {m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["recursive_addition_on_non_consecutive_inputs"],
        "diagram_spec": None,
    }


def arch_14_solving_for_input_linear_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 7])
    c = rng.randint(2, 8)
    in_val = rng.randint(6, 18)
    out_val = m * in_val + c

    return {
        "title": "Solving for Input in Linear Equation",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "14_solving_for_input_linear_equation",
        "difficulty": "medium",
        "question_text": (
            f"For the function $y = {m}x + {c}$:\n\n"
            f"Solve for the input value $x$ when the output is $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Set up equation {m}x + {c} = {out_val} (1 mark)",
            f"Solve for x: x = ({out_val} - {c}) / {m} = {in_val} (1 mark)",
        ],
        "hints": [
            f"Set ${m}x + {c} = {out_val}$.",
            f"Subtract {c}: ${m}x = {out_val - c}$.",
            f"Divide by {m}: $x = \\frac{{{out_val - c}}}{{{m}}} = {in_val}$.",
        ],
        "misconception_tags": ["linear_equation_solving_error"],
        "diagram_spec": None,
    }


def arch_15_solving_for_input_linear_with_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(2, 6)
    in_val = rng.randint(5, 14)
    out_val = a * (in_val - b)

    return {
        "title": "Solving for Input (Bracketed Linear Formula)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "15_solving_for_input_linear_with_brackets",
        "difficulty": "hard",
        "question_text": (
            f"A function is defined by $y = {a}(x - {b})$.\n\n"
            f"Determine the value of the input $x$ that gives an output of $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Divide by {a}: x - {b} = {out_val} / {a} = {out_val // a} (1 mark)",
            f"Add {b}: x = {out_val // a} + {b} = {in_val} (1 mark)",
        ],
        "hints": [
            f"Divide both sides by {a}: $x - {b} = \\frac{{{out_val}}}{{{a}}} = {out_val // a}$.",
            f"Add {b} to both sides: $x = {out_val // a} + {b} = {in_val}$.",
        ],
        "misconception_tags": ["bracketed_equation_inverse_error"],
        "diagram_spec": None,
    }


def arch_16_solving_for_input_quadratic_equation(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(1, 5)
    in_val = rng.randint(4, 12)
    out_val = (in_val ** 2) + c

    return {
        "title": "Solving for Input in Quadratic Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "16_solving_for_input_quadratic_equation",
        "difficulty": "hard",
        "question_text": (
            f"In the quadratic relationship $y = x^2 + {c}$:\n\n"
            f"Find the positive input value $x$ for which $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Subtract {c}: x^2 = {out_val - c} (1 mark)",
            f"Take square root: x = sqrt({out_val - c}) = {in_val} (1 mark)",
        ],
        "hints": [
            f"$x^2 + {c} = {out_val}$.",
            f"$x^2 = {out_val} - {c} = {out_val - c}$.",
            f"$x = \\sqrt{{{out_val - c}}} = {in_val}$.",
        ],
        "misconception_tags": ["square_root_solving_slip"],
        "diagram_spec": None,
    }


def arch_17_solving_for_input_exponential_equation(rng: random.Random) -> Dict[str, Any]:
    exp = rng.choice([3, 4, 5, 6])
    target_y = 2 ** exp

    return {
        "title": "Solving for Exponent in Exponential Function",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "17_solving_for_input_exponential_equation",
        "difficulty": "hard",
        "question_text": (
            f"For the exponential function $y = 2^x$:\n\n"
            f"Determine the input value $x$ when the output is $y = {target_y}$."
        ),
        "correct_answer": str(exp),
        "marking_schema": [
            f"Express {target_y} as power of 2: {target_y} = 2^{exp} (1 mark)",
            f"Equate exponents: x = {exp} (1 mark)",
        ],
        "hints": [
            f"Write the equation: $2^x = {target_y}$.",
            f"Express {target_y} as a power of 2: ${target_y} = 2^{{{exp}}}$.",
            f"Since bases are identical: $x = {exp}$.",
        ],
        "misconception_tags": ["exponential_equation_base_conversion_error"],
        "diagram_spec": None,
    }


def arch_18_solving_for_input_inverse_proportion_equation(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([36, 48, 60, 72, 90])
    divs = [d for d in range(2, 16) if k % d == 0]
    in_val = rng.choice(divs)
    out_val = k // in_val

    return {
        "title": "Solving for Input in Inverse Proportion",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "18_solving_for_input_inverse_proportion_equation",
        "difficulty": "medium",
        "question_text": (
            f"Two quantities are related by $y = \\frac{{{k}}}{{x}}$.\n\n"
            f"Find the value of $x$ when $y = {out_val}$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Set up {out_val} = {k} / x => x = {k} / {out_val} = {in_val} (1 mark)",
        ],
        "hints": [
            f"${out_val} = \\frac{{{k}}}{{x}}$.",
            f"Multiply both sides by $x$: ${out_val}x = {k}$.",
            f"$x = \\frac{{{k}}}{{{out_val}}} = {in_val}$.",
        ],
        "misconception_tags": ["cross_multiplication_inversion_error"],
        "diagram_spec": None,
    }


def arch_19_matching_formula_to_linear_table_negative_slope(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 5])
    c = rng.choice([15, 20, 25])
    # y = -m*x + c
    x_vals = [1, 2, 3, 4]
    y_vals = [-m * x + c for x in x_vals]
    correct_f = f"y = -{m}x + {c}"
    wrong_f1 = f"y = {m}x + {c}"
    wrong_f2 = f"y = -{m}x + {c+5}"

    return {
        "title": "Matching Formula to Negative Slope Table",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "19_matching_formula_to_linear_table_negative_slope",
        "difficulty": "medium",
        "question_text": (
            f"Which formula models the decreasing table below?\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"* **A:** ${wrong_f1}$\n"
            f"* **B:** ${correct_f}$\n"
            f"* **C:** ${wrong_f2}$\n\n"
            f"State the correct letter (**A**, **B**, or **C**)."
        ),
        "correct_answer": "B",
        "marking_schema": [
            f"Determine common difference d = -{m} (1 mark)",
            f"Verify y-intercept / constant term: c = {c} (1 mark)",
            "Identify B as matching formula (1 mark)",
        ],
        "hints": [
            f"The table values decrease by {m} each step, so the gradient is $-{m}$.",
            f"When $x = 1$, $y = -{m}(1) + {c} = {y_vals[0]}$.",
            "Formula B is correct.",
        ],
        "misconception_tags": ["negative_gradient_identification_error"],
        "diagram_spec": None,
    }


def arch_20_matching_formula_to_quadratic_table(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([1, 2, 3])
    x_vals = [1, 2, 3, 4]
    y_vals = [(x ** 2) + c for x in x_vals]
    correct_f = f"y = x^2 + {c}"

    return {
        "title": "Matching Formula to Quadratic Table",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "20_matching_formula_to_quadratic_table",
        "difficulty": "hard",
        "question_text": (
            f"Observe the table of values:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Notice that the first differences are not constant: ${y_vals[1]-y_vals[0]}, {y_vals[2]-y_vals[1]}, {y_vals[3]-y_vals[2]}$.\n"
            f"State the quadratic formula relating $y$ to $x$ in the form $y = x^2 + c$."
        ),
        "correct_answer": correct_f,
        "marking_schema": [
            "Identify non-linear quadratic sequence (1 mark)",
            f"Determine offset constant c = {c} (1 mark)",
            f"State formula {correct_f} (1 mark)",
        ],
        "hints": [
            "Compare $y$ to $x^2$: $1^2=1, 2^2=4, 3^2=9, 4^2=16$.",
            f"Every output is {c} units greater than $x^2$.",
            f"Formula: ${correct_f}$.",
        ],
        "misconception_tags": ["quadratic_table_deduction_error"],
        "diagram_spec": None,
    }


def arch_21_matching_formula_to_exponential_table(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    x_vals = [1, 2, 3, 4]
    y_vals = [base ** x for x in x_vals]
    correct_f = f"y = {base}^x"

    return {
        "title": "Matching Formula to Exponential Table",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "21_matching_formula_to_exponential_table",
        "difficulty": "hard",
        "question_text": (
            f"In the table below, each output is multiplied by a constant factor:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Write the exponential formula relating $y$ to $x$ in the form $y = b^x$."
        ),
        "correct_answer": correct_f,
        "marking_schema": [
            f"Identify constant ratio factor {base} (1 mark)",
            f"State exponential formula {correct_f} (1 mark)",
        ],
        "hints": [
            f"The outputs are multiplied by {base} each time: $\\frac{{{y_vals[1]}}}{{{y_vals[0]}}} = {base}$.",
            f"This indicates an exponential function with base {base}.",
            f"Formula: ${correct_f}$.",
        ],
        "misconception_tags": ["exponential_ratio_formula_identification_error"],
        "diagram_spec": None,
    }


def arch_22_calculating_gradient_from_non_consecutive_table_points(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.randint(1, 8)
    x1, x2 = 2, rng.choice([5, 6, 7])
    y1 = m * x1 + c
    y2 = m * x2 + c
    delta_x = x2 - x1
    delta_y = y2 - y1

    return {
        "title": "Calculating Rate of Change from Non-Consecutive Points",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "22_calculating_gradient_from_non_consecutive_table_points",
        "difficulty": "hard",
        "question_text": (
            f"A linear table contains the two non-consecutive coordinate pairs $({x1};\\ {y1})$ and $({x2};\\ {y2})$.\n\n"
            f"Calculate the constant rate of change (gradient) using the formula:\n"
            f"$$m = \\frac{{\\text{{Change in }} y}}{{\\text{{Change in }} x}} = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$$"
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Calculate delta y: {y2} - {y1} = {delta_y} (1 mark)",
            f"Calculate delta x: {x2} - {x1} = {delta_x} (1 mark)",
            f"Divide to find gradient: {delta_y} / {delta_x} = {m} (1 mark)",
        ],
        "hints": [
            f"Change in $y$: ${y2} - {y1} = {delta_y}$.",
            f"Change in $x$: ${x2} - {x1} = {delta_x}$.",
            f"Rate of change $m = \\frac{{{delta_y}}}{{{delta_x}}} = {m}$.",
        ],
        "misconception_tags": ["gradient_delta_y_over_delta_x_slip"],
        "diagram_spec": None,
    }


def arch_23_deducing_linear_rule_from_two_distant_table_entries(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([2, 5, 8])
    x1, y1 = 2, m * 2 + c
    x2, y2 = 5, m * 5 + c

    return {
        "title": "Deducing Full Linear Rule from Two Distant Entries",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "23_deducing_linear_rule_from_two_distant_table_entries",
        "difficulty": "hard",
        "question_text": (
            f"A linear relationship passes through the entries $x = {x1} \\rightarrow y = {y1}$ and $x = {x2} \\rightarrow y = {y2}$.\n\n"
            f"Determine the complete algebraic equation connecting $x$ and $y$ in the form $y = mx + c$."
        ),
        "correct_answer": f"y = {m}x + {c}",
        "marking_schema": [
            f"Calculate rate of change m = ({y2} - {y1}) / ({x2} - {x1}) = {m} (1 mark)",
            f"Substitute to solve for c: c = {c} (1 mark)",
            f"State full equation y = {m}x + {c} (1 mark)",
        ],
        "hints": [
            f"Find gradient $m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$.",
            f"Substitute $x = {x1}$: $y = {m}({x1}) + c = {y1} \\implies {m * x1} + c = {y1} \\implies c = {c}$.",
            f"The equation is $y = {m}x + {c}$.",
        ],
        "misconception_tags": ["two_point_linear_deduction_error"],
        "diagram_spec": None,
    }


def arch_24_verbal_description_to_algebraic_formula_linear(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 8)
    c = rng.randint(2, 9)

    return {
        "title": "Verbal Description to Algebraic Formula (Linear)",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "24_verbal_description_to_algebraic_formula_linear",
        "difficulty": "easy",
        "question_text": (
            f"Translate the following verbal statement into an algebraic equation:\n\n"
            f"*\"To calculate the output ($y$), multiply the input ($x$) by ${m}$, and then add ${c}$.\"*\n\n"
            f"Write the formula in the form $y = \\dots$."
        ),
        "correct_answer": f"y = {m}x + {c}",
        "marking_schema": [
            f"Represent multiplication: {m}x (1 mark)",
            f"Represent addition of constant: + {c} (1 mark)",
        ],
        "hints": [
            f"Multiplying $x$ by {m} gives ${m}x$.",
            f"Adding {c} gives ${m}x + {c}$.",
            f"Equation: $y = {m}x + {c}$.",
        ],
        "misconception_tags": ["verbal_to_algebraic_translation_error"],
        "diagram_spec": None,
    }


def arch_25_verbal_description_to_algebraic_formula_with_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 5)

    return {
        "title": "Verbal Description to Bracketed Formula",
        "topic": "Functions and relationships 2",
        "grade": 8,
        "term": 1,
        "subskill": "25_verbal_description_to_algebraic_formula_with_brackets",
        "difficulty": "medium",
        "question_text": (
            f"Express this rule algebraically using parentheses:\n\n"
            f"*\"First add ${a}$ to the input ($x$), and then multiply the entire result by ${b}$ to obtain the output ($y$).\"*\n\n"
            f"Write the equation in the form $y = b(x + a)$."
        ),
        "correct_answer": f"y = {b}(x + {a})",
        "marking_schema": [
            f"Formulate bracketed sum (x + {a}) (1 mark)",
            f"Multiply sum by {b}: y = {b}(x + {a}) (1 mark)",
        ],
        "hints": [
            f"Adding {a} first requires parentheses: $(x + {a})$.",
            f"Then multiplying by {b}: $y = {b}(x + {a})$.",
        ],
        "misconception_tags": ["bracket_omission_in_verbal_translation"],
        "diagram_spec": None,
    }
