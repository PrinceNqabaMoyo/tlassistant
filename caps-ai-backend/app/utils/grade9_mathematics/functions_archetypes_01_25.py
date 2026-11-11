"""
Grade 9 Mathematics - Functions and Relationships Archetypes 01 to 25
=====================================================================
Grounding:
  - CAPS Grade 9 Mathematics: Term 1 Topic: Functions and relationships
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/05. Functions and relationships.md
  - Chapter 12: From counting to calculating, rules y = mx + c, flow diagrams, tables
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.functions_svg import (
    draw_function_flow_diagram_svg,
    draw_function_table_svg,
    draw_rate_context_graph_svg,
)


def arch_01_flow_diagram_linear_positive_slope_integer_output(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5, 6])
    c = rng.choice([1, 2, 3, 4, 5, 7, 8, 9])
    x = rng.choice([2, 3, 4, 5, 6, 7, 8])
    y = m * x + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× {m}", f"+ {c}", input_str=str(x), output_str="?", seed=seed_val)

    return {
        "subskill": "01_flow_diagram_linear_positive_slope_integer_output",
        "question_text": (
            f"The flow diagram below applies two operations to an input number $x$ to calculate the output number $y$:\n\n"
            f"Determine the **output value ($y$)** when the input value is **$x = {x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply input by {m}: ${m} \\times {x} = {m * x}$", "marks": 1},
            {"step": f"Add {c}: ${m * x} + {c} = {y}$", "marks": 1},
        ],
        "hints": [
            f"First calculate the intermediate output after Step 1: ${m} \\times {x}$.",
            f"Then apply Step 2 by adding ${c}$ to that result.",
            f"Output $y = {m * x} + {c} = {y}$.",
        ],
        "misconception_tags": ["order_of_operations_flow_diagram", "arithmetic_addition_error"],
    }


def arch_02_flow_diagram_linear_negative_slope_integer_output(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-2, -3, -4, -5])
    c = rng.choice([10, 15, 20, 25, 30])
    x = rng.choice([1, 2, 3, 4, 5])
    y = m * x + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× ({m})", f"+ {c}", input_str=str(x), output_str="?", seed=seed_val)

    return {
        "subskill": "02_flow_diagram_linear_negative_slope_integer_output",
        "question_text": (
            f"A mathematical flow diagram processes an input number $x$ using a negative multiplier as shown below:\n\n"
            f"Calculate the **output value ($y$)** when the input value is **$x = {x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply input by {m}: $({m}) \\times {x} = {m * x}$", "marks": 1},
            {"step": f"Add {c}: ${m * x} + {c} = {y}$", "marks": 1},
        ],
        "hints": [
            f"Remember that multiplying a positive number by a negative number gives a negative result: $({m}) \\times {x} = {m * x}$.",
            f"Now add ${c}$: ${m * x} + {c}$.",
            f"Output $y = {y}$.",
        ],
        "misconception_tags": ["negative_multiplication_sign_error", "signed_addition_error"],
    }


def arch_03_flow_diagram_two_step_bracket_operation(rng: random.Random) -> Dict[str, Any]:
    # Operation: y = (x + a) * b
    a = rng.choice([1, 2, 3, 4, 5])
    b = rng.choice([2, 3, 4, 5])
    x = rng.choice([2, 3, 4, 6, 7])
    y = (x + a) * b

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"+ {a}", f"× {b}", input_str=str(x), output_str="?", seed=seed_val)

    return {
        "subskill": "03_flow_diagram_two_step_bracket_operation",
        "question_text": (
            f"Consider the flow diagram shown below where addition precedes multiplication:\n\n"
            f"Find the **output ($y$)** corresponding to the input value **$x = {x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"First add {a}: ${x} + {a} = {x + a}$", "marks": 1},
            {"step": f"Then multiply by {b}: ${x + a} \\times {b} = {y}$", "marks": 1},
        ],
        "hints": [
            f"Follow the arrows in sequence. Step 1 adds ${a}$ to the input.",
            f"${x} + {a} = {x + a}$.",
            f"Step 2 multiplies this result by ${b}$: ${x + a} \\times {b} = {y}$.",
        ],
        "misconception_tags": ["flow_sequence_misunderstanding", "distributive_error"],
    }


def arch_04_flow_diagram_fractional_operator_output(rng: random.Random) -> Dict[str, Any]:
    # Operation: y = (x / d) + c
    d = rng.choice([2, 3, 4, 5])
    k = rng.choice([2, 3, 4, 5, 6])
    x = k * d
    c = rng.choice([3, 5, 7, 9, 11])
    y = (x // d) + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"÷ {d}", f"+ {c}", input_str=str(x), output_str="?", seed=seed_val)

    return {
        "subskill": "04_flow_diagram_fractional_operator_output",
        "question_text": (
            f"In the flow diagram below, the input value is divided by ${d}$ before adding ${c}$:\n\n"
            f"Calculate the **output value ($y$)** when the input value is **$x = {x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide input by {d}: ${x} \\div {d} = {x // d}$", "marks": 1},
            {"step": f"Add {c}: ${x // d} + {c} = {y}$", "marks": 1},
        ],
        "hints": [
            f"Divide ${x}$ by ${d}$ in the first step: ${x} \\div {d} = {x // d}$.",
            f"Add ${c}$ to ${x // d}$.",
            f"Final output $y = {y}$.",
        ],
        "misconception_tags": ["division_flow_error", "fractional_step_confusion"],
    }


def arch_05_flow_diagram_inverse_calculate_input_from_output(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 3, 5, 7])
    x = rng.choice([3, 4, 5, 6, 7, 8])
    y = m * x + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× {m}", f"+ {c}", input_str="x", output_str=str(y), seed=seed_val)

    return {
        "subskill": "05_flow_diagram_inverse_calculate_input_from_output",
        "question_text": (
            f"The flow diagram below maps an unknown input $x$ to an output $y$:\n\n"
            f"If the **output is $y = {y}$**, use inverse operations to determine the **input value ($x$)**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(x),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Inverse Step 2: subtract {c}: ${y} - {c} = {y - c}$", "marks": 1},
            {"step": f"Inverse Step 1: divide by {m}: ${y - c} \\div {m} = {x}$", "marks": 1},
        ],
        "hints": [
            "To find the input from the output, reverse the operations in opposite order.",
            f"Step 2 added ${c}$, so first subtract ${c}$ from ${y}$: ${y} - {c} = {y - c}$.",
            f"Step 1 multiplied by ${m}$, so now divide by ${m}$: ${y - c} \\div {m} = {x}$.",
        ],
        "misconception_tags": ["inverse_operations_order_error", "failure_to_reverse_operations"],
    }


def arch_06_flow_diagram_determine_missing_operator(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.choice([2, 4, 6, 8])
    x = rng.choice([2, 3, 4])
    y = m * x + c

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× {m}", "[ ? ]", input_str=str(x), output_str=str(y), seed=seed_val)

    return {
        "subskill": "06_flow_diagram_determine_missing_operator",
        "question_text": (
            f"In the flow diagram below, an input of $x = {x}$ produces an output of $y = {y}$:\n\n"
            f"Step 1 multiplies the input by ${m}$. Determine the value added in Step 2 (i.e. the missing term $+ c$)."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Evaluate Step 1: ${m} \\times {x} = {m * x}$", "marks": 1},
            {"step": f"Find difference with output: ${y} - {m * x} = {c}$", "marks": 1},
        ],
        "hints": [
            f"After Step 1, the value is ${m} \\times {x} = {m * x}$.",
            f"The final output is ${y}$.",
            f"The difference is ${y} - {m * x} = {c}$.",
        ],
        "misconception_tags": ["missing_operator_calculation", "algebraic_deduction_error"],
    }


def arch_07_table_linear_positive_coefficient_find_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([1, 2, 4, 5])
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [m * x + c for x in x_vals]

    target_idx = 3  # x = 4
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "P" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label=f"y = {m}x + {c}", seed=seed_val)

    return {
        "subskill": "07_table_linear_positive_coefficient_find_outputs",
        "question_text": (
            f"The function table below follows the rule $y = {m}x + {c}$:\n\n"
            f"Determine the missing output value **$P$** when the input is **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {target_x}$ into formula: $y = {m}({target_x}) + {c}$", "marks": 1},
            {"step": f"Calculate: $y = {m * target_x} + {c} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = {target_x}$ into the rule $y = {m}x + {c}$.",
            f"${m} \\times {target_x} = {m * target_x}$.",
            f"$P = {m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["table_substitution_error", "linear_evaluation_miscalculation"],
    }


def arch_08_table_linear_negative_coefficient_find_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-2, -3, -4])
    c = rng.choice([12, 16, 20, 24])
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [m * x + c for x in x_vals]

    target_idx = 2  # x = 3
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "Q" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label=f"y = {m}x + {c}", seed=seed_val)

    return {
        "subskill": "08_table_linear_negative_coefficient_find_outputs",
        "question_text": (
            f"The function table below illustrates a decreasing relationship defined by $y = {m}x + {c}$:\n\n"
            f"Calculate the missing output value **$Q$** when **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {target_x}$: $y = ({m})({target_x}) + {c}$", "marks": 1},
            {"step": f"Evaluate: ${m * target_x} + {c} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = {target_x}$ into $y = {m}x + {c}$.",
            f"$({m}) \\times {target_x} = {m * target_x}$.",
            f"$Q = {m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["negative_gradient_evaluation", "integer_arithmetic_in_table"],
    }


def arch_09_table_linear_missing_input_values(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([2, 5, 7, 8])
    x_vals = [1, 2, 3, 5, 8]
    y_vals = [m * x + c for x in x_vals]

    target_idx = 3  # x = 5
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_x = [str(x) if i != target_idx else "k" for i, x in enumerate(x_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(display_x, y_vals, rule_label=f"y = {m}x + {c}", seed=seed_val)

    return {
        "subskill": "09_table_linear_missing_input_values",
        "question_text": (
            f"In the table below generated by the relationship $y = {m}x + {c}$, an input value **$k$** produces an output of **${target_y}$**:\n\n"
            f"Find the value of **$k$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_x),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: ${m}k + {c} = {target_y}$", "marks": 1},
            {"step": f"Subtract {c}: ${m}k = {target_y - c}$", "marks": 1},
            {"step": f"Divide by {m}: $k = {target_x}$", "marks": 1},
        ],
        "hints": [
            f"Set up the equation ${m}k + {c} = {target_y}$.",
            f"Subtract ${c}$ from both sides: ${m}k = {target_y - c}$.",
            f"Divide by ${m}$: $k = {target_x}$.",
        ],
        "misconception_tags": ["solving_linear_for_input", "inverse_table_lookup"],
    }


def arch_10_table_mixed_missing_inputs_and_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 5])
    c = rng.choice([3, 4, 6])
    x_vals = [1, 2, 4, 7]
    y_vals = [m * x + c for x in x_vals]

    # Target is to calculate y for x = 7
    target_x = 7
    target_y = m * target_x + c

    seed_val = rng.randint(1000, 999999)
    display_y = [str(y_vals[0]), str(y_vals[1]), str(y_vals[2]), "Y"]
    svg = draw_function_table_svg(x_vals, display_y, rule_label=f"y = {m}x + {c}", seed=seed_val)

    return {
        "subskill": "10_table_mixed_missing_inputs_and_outputs",
        "question_text": (
            f"The table below shows input-output pairs governed by $y = {m}x + {c}$:\n\n"
            f"Calculate the output value **$Y$** corresponding to the input **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {target_x}$: $Y = {m}({target_x}) + {c}$", "marks": 1},
            {"step": f"Evaluate: $Y = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Use the function formula $y = {m}x + {c}$.",
            f"Substitute $x = {target_x}$: $Y = {m} \\times {target_x} + {c}$.",
            f"$Y = {m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["function_table_evaluation", "two_step_arithmetic"],
    }


def arch_11_determine_rule_y_equals_mx_plus_c_from_table(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 2, 3, 5, 7])
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [m * x + c for x in x_vals]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, y_vals, rule_label="y = mx + c", seed=seed_val)

    return {
        "subskill": "11_determine_rule_y_equals_mx_plus_c_from_table",
        "question_text": (
            f"Examine the input-output table below:\n\n"
            f"Determine the **constant difference (gradient $m$)** in the linear rule $y = mx + c$."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find difference between consecutive y values: ${y_vals[1]} - {y_vals[0]} = {m}$", "marks": 1},
            {"step": f"Identify gradient $m = {m}$", "marks": 1},
        ],
        "hints": [
            f"Check the change in $y$ as $x$ increases by $1$.",
            f"${y_vals[1]} - {y_vals[0]} = {m}$ and ${y_vals[2]} - {y_vals[1]} = {m}$.",
            f"The constant difference is $m = {m}$.",
        ],
        "misconception_tags": ["gradient_deduction_from_table", "constant_difference_concept"],
    }


def arch_12_determine_rule_with_negative_slope_from_table(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-2, -3, -4, -5])
    c = rng.choice([15, 20, 25, 30])
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [m * x + c for x in x_vals]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, y_vals, rule_label="y = mx + c", seed=seed_val)

    return {
        "subskill": "12_determine_rule_with_negative_slope_from_table",
        "question_text": (
            f"The table below represents a decreasing linear function:\n\n"
            f"Find the **rate of change ($m$)** between consecutive values of $x$ (include the negative sign)."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(m),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate $\\Delta y = {y_vals[1]} - {y_vals[0]} = {m}$", "marks": 1},
        ],
        "hints": [
            f"Subtract the first output from the second output: ${y_vals[1]} - {y_vals[0]}$.",
            f"Notice that the outputs are decreasing by ${abs(m)}$ each time.",
            f"Therefore the rate of change is $m = {m}$.",
        ],
        "misconception_tags": ["negative_slope_sign_omission", "rate_of_change_sign_confusion"],
    }


def arch_13_determine_rule_from_verbal_description(rng: random.Random) -> Dict[str, Any]:
    # e.g. "Multiply input by 4 and then subtract 7"
    m = rng.choice([3, 4, 5, 6, 7])
    c = rng.choice([2, 5, 8, 11])
    x_test = rng.choice([3, 4, 5])
    y_test = m * x_test - c

    return {
        "subskill": "13_determine_rule_from_verbal_description",
        "question_text": (
            f"A function rule is stated verbally: *\"Multiply the input number by ${m}$ and then subtract ${c}$.\"*\n\n"
            f"If the input number is **$x = {x_test}$**, calculate the **output number ($y$)**."
        ),
        "correct_answer": str(y_test),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Formulate algebraic rule: $y = {m}x - {c}$", "marks": 1},
            {"step": f"Substitute $x = {x_test}$: $y = {m}({x_test}) - {c} = {y_test}$", "marks": 1},
        ],
        "hints": [
            f"Write the rule as an algebraic formula: $y = {m}x - {c}$.",
            f"Multiply ${m} \\times {x_test} = {m * x_test}$.",
            f"Subtract ${c}$: ${m * x_test} - {c} = {y_test}$.",
        ],
        "misconception_tags": ["verbal_to_symbolic_translation", "linear_evaluation_order"],
    }


def arch_14_match_flow_diagram_to_algebraic_formula(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 3, 5, 7])

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_flow_diagram_svg(f"× {m}", f"+ {c}", input_str="x", output_str="y", seed=seed_val)

    correct_formula = f"y = {m}x + {c}"
    options = [
        correct_formula,
        f"y = {c}x + {m}",
        f"y = {m}(x + {c})",
        f"y = x + {m * c}",
    ]
    rng.shuffle(options)
    correct_letter = chr(65 + options.index(correct_formula))

    options_formatted = "\n".join([f"**{chr(65+i)}:** ${opt}$" for i, opt in enumerate(options)])

    return {
        "subskill": "14_match_flow_diagram_to_algebraic_formula",
        "question_text": (
            f"Consider the flow diagram below:\n\n"
            f"Which of the following algebraic formulae correctly represents this flow diagram?\n\n"
            f"{options_formatted}\n\n"
            f"Enter the correct option letter (**A**, **B**, **C**, or **D**)."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": correct_letter,
        "marking_schema": [
            {"step": f"Trace operations: $x \\to {m}x \\to {m}x + {c}$", "marks": 1},
            {"step": f"Select matching option {correct_letter}", "marks": 1},
        ],
        "hints": [
            f"Step 1 multiplies $x$ by ${m}$, giving ${m}x$.",
            f"Step 2 adds ${c}$, giving ${m}x + {c}$.",
            f"The matching formula is ${correct_formula}$, corresponding to option **{correct_letter}**.",
        ],
        "misconception_tags": ["matching_flow_to_formula", "distributive_vs_standard_form"],
    }


def arch_15_match_table_of_values_to_formula(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([1, 3, 5])
    x_vals = [1, 2, 3, 4]
    y_vals = [m * x + c for x in x_vals]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, y_vals, rule_label="?", seed=seed_val)

    correct_formula = f"y = {m}x + {c}"
    options = [
        correct_formula,
        f"y = {m+1}x + {c-1}",
        f"y = {m}x - {c}",
        f"y = {c}x + {m}",
    ]
    rng.shuffle(options)
    correct_letter = chr(65 + options.index(correct_formula))
    options_formatted = "\n".join([f"**{chr(65+i)}:** ${opt}$" for i, opt in enumerate(options)])

    return {
        "subskill": "15_match_table_of_values_to_formula",
        "question_text": (
            f"The table below lists values for a linear function:\n\n"
            f"Which formula generates these pairs of values?\n\n"
            f"{options_formatted}\n\n"
            f"Enter the correct option letter (**A**, **B**, **C**, or **D**)."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": correct_letter,
        "marking_schema": [
            {"step": f"Determine constant difference $m = {m}$", "marks": 1},
            {"step": f"Substitute $x=1$ to find $c$: ${m}(1) + c = {y_vals[0]} \\implies c = {c}$", "marks": 1},
            {"step": f"Select option {correct_letter}", "marks": 1},
        ],
        "hints": [
            f"The difference between successive $y$ values is ${y_vals[1]} - {y_vals[0]} = {m}$, so the gradient is ${m}$.",
            f"Test $x = 1$: ${m}(1) + {c} = {y_vals[0]}$, which matches the table.",
            f"Option **{correct_letter}** (${correct_formula}$) is correct.",
        ],
        "misconception_tags": ["table_to_formula_matching", "testing_candidates_in_table"],
    }


def arch_16_equivalent_formulae_algebraic_expansion_check(rng: random.Random) -> Dict[str, Any]:
    # e.g. y = 3(2x + 4) is equivalent to y = 6x + 12
    a = rng.choice([2, 3, 4])
    b = rng.choice([2, 3, 5])
    c = rng.choice([1, 4, 6])
    m_exp = a * b
    c_exp = a * c

    x_test = rng.choice([2, 3, 4])
    y_val = m_exp * x_test + c_exp

    return {
        "subskill": "16_equivalent_formulae_algebraic_expansion_check",
        "question_text": (
            f"Two learners write different formulae for the same function:\n"
            f"* Learner A: $y = {a}({b}x + {c})$\n"
            f"* Learner B: $y = {m_exp}x + {c_exp}$\n\n"
            f"Evaluate both formulae for **$x = {x_test}$** to verify they yield the same result. What is the common value of **$y$**?"
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand Learner A: ${a}({b}x + {c}) = {m_exp}x + {c_exp}$", "marks": 1},
            {"step": f"Evaluate at $x = {x_test}$: ${m_exp}({x_test}) + {c_exp} = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"Using Learner B: substitute $x = {x_test}$ into ${m_exp}x + {c_exp}$.",
            f"${m_exp} \\times {x_test} = {m_exp * x_test}$.",
            f"${m_exp * x_test} + {c_exp} = {y_val}$.",
        ],
        "misconception_tags": ["distributive_expansion_equivalence", "substitution_verification"],
    }


def arch_17_linear_function_evaluate_for_negative_input(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([-5, -2, 3, 7])
    x_neg = rng.choice([-4, -3, -2, -1])
    y_val = m * x_neg + c

    return {
        "subskill": "17_linear_function_evaluate_for_negative_input",
        "question_text": (
            f"A function is defined by the formula $y = {m}x + ({c})$.\n\n"
            f"Calculate the value of **$y$** when the input is **$x = {x_neg}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {x_neg}$: $y = {m}({x_neg}) + ({c})$", "marks": 1},
            {"step": f"Evaluate: ${m * x_neg} + ({c}) = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"Substitute $x = {x_neg}$ into the formula.",
            f"Calculate ${m} \\times ({x_neg}) = {m * x_neg}$.",
            f"Now add $({c})$: ${m * x_neg} + ({c}) = {y_val}$.",
        ],
        "misconception_tags": ["negative_input_multiplication", "signed_addition"],
    }


def arch_18_linear_function_evaluate_for_fractional_input(rng: random.Random) -> Dict[str, Any]:
    # y = m*x + c with fractional input that simplifies to an integer
    m = rng.choice([6, 8, 10, 12])
    denom = rng.choice([2, 4]) if m % 4 == 0 else 2
    numer = rng.choice([1, 3])
    c = rng.choice([2, 5, 7, 9])
    
    # x = numer / denom
    x_times_m = (m * numer) // denom
    y_val = x_times_m + c

    return {
        "subskill": "18_linear_function_evaluate_for_fractional_input",
        "question_text": (
            f"Given the linear function $y = {m}x + {c}$, calculate the value of **$y$** "
            f"when the input is the fraction **$x = \\frac{{{numer}}}{{{denom}}}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply $m \\times x$: ${m} \\times \\frac{{{numer}}}{{{denom}}} = {x_times_m}$", "marks": 1},
            {"step": f"Add constant: ${x_times_m} + {c} = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"First calculate ${m} \\times \\frac{{{numer}}}{{{denom}}} = \\frac{{{m * numer}}}{{{denom}}} = {x_times_m}$.",
            f"Then add ${c}$ to ${x_times_m}$.",
            f"Final output $y = {y_val}$.",
        ],
        "misconception_tags": ["fraction_multiplication_in_functions", "fractional_substitution_error"],
    }


def arch_19_quadratic_function_table_evaluation_y_equals_x_squared(rng: random.Random) -> Dict[str, Any]:
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [x * x for x in x_vals]

    target_idx = 3  # x = 4
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "M" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label="y = x^2", seed=seed_val)

    return {
        "subskill": "19_quadratic_function_table_evaluation_y_equals_x_squared",
        "question_text": (
            f"The table below represents the non-linear quadratic function $y = x^2$:\n\n"
            f"Determine the value of **$M$** when **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {target_x}$: $M = ({target_x})^2 = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Squaring a number means multiplying it by itself.",
            f"$M = {target_x} \\times {target_x} = {target_y}$.",
        ],
        "misconception_tags": ["quadratic_table_evaluation", "confusing_square_with_multiply_by_two"],
    }


def arch_20_quadratic_function_evaluate_y_equals_ax_squared_plus_c(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    c = rng.choice([1, 3, 5])
    x = rng.choice([3, 4, 5])
    y_val = a * (x ** 2) + c

    return {
        "subskill": "20_quadratic_function_evaluate_y_equals_ax_squared_plus_c",
        "question_text": (
            f"A quadratic function is defined by $y = {a}x^2 + {c}$.\n\n"
            f"Calculate the **output value ($y$)** when the input value is **$x = {x}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Square the input: ${x}^2 = {x**2}$", "marks": 1},
            {"step": f"Multiply by {a}: ${a} \\times {x**2} = {a * (x**2)}$", "marks": 1},
            {"step": f"Add {c}: ${a * (x**2)} + {c} = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"Follow the order of operations: square first, then multiply, then add.",
            f"${x}^2 = {x**2}$.",
            f"${a} \\times {x**2} = {a * (x**2)}$, and ${a * (x**2)} + {c} = {y_val}$.",
        ],
        "misconception_tags": ["bodmas_powers_before_multiplication", "quadratic_evaluation_order"],
    }


def arch_21_quadratic_function_find_missing_inputs(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 5, 7, 10])
    x_pos = rng.choice([3, 4, 5, 6])
    y = x_pos ** 2 + c

    return {
        "subskill": "21_quadratic_function_find_missing_inputs",
        "question_text": (
            f"A function has the rule $y = x^2 + {c}$.\n\n"
            f"If the output is **$y = {y}$**, find the **positive input value ($x > 0$)**."
        ),
        "correct_answer": str(x_pos),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: $x^2 + {c} = {y}$", "marks": 1},
            {"step": f"Subtract {c}: $x^2 = {y - c}$", "marks": 1},
            {"step": f"Take positive square root: $x = \\sqrt{{{y - c}}} = {x_pos}$", "marks": 1},
        ],
        "hints": [
            f"Subtract ${c}$ from ${y}$: $x^2 = {y} - {c} = {y - c}$.",
            f"Take the square root of ${y - c}$.",
            f"Since $x > 0$, $x = {x_pos}$.",
        ],
        "misconception_tags": ["quadratic_inverse_operation", "square_root_solving"],
    }


def arch_22_exponential_function_table_powers_of_two(rng: random.Random) -> Dict[str, Any]:
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [2 ** x for x in x_vals]

    target_idx = 4  # x = 5
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "E" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label="y = 2^x", seed=seed_val)

    return {
        "subskill": "22_exponential_function_table_powers_of_two",
        "question_text": (
            f"The table below shows an exponential growth relationship where $y = 2^x$:\n\n"
            f"Determine the value of **$E$** when **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate $2^{{{target_x}}} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"In an exponential function $y = 2^x$, each term doubles the previous term.",
            f"For $x = {target_x}$, $y = 2^{{{target_x}}}$.",
            f"$2^{{{target_x}}} = {target_y}$.",
        ],
        "misconception_tags": ["exponential_table_growth", "confusing_2_power_x_with_2x"],
    }


def arch_23_exponential_function_evaluate_y_equals_a_times_b_to_x(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = 2
    x = rng.choice([2, 3, 4])
    y_val = a * (b ** x)

    return {
        "subskill": "23_exponential_function_evaluate_y_equals_a_times_b_to_x",
        "question_text": (
            f"An exponential function is given by the formula $y = {a} \\times 2^x$.\n\n"
            f"Find the **output value ($y$)** when the input value is **$x = {x}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Evaluate power first: $2^{{{x}}} = {b**x}$", "marks": 1},
            {"step": f"Multiply by coefficient: ${a} \\times {b**x} = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"Calculate the exponential part first: $2^{{{x}}} = {b**x}$.",
            f"Now multiply by ${a}$: ${a} \\times {b**x} = {y_val}$.",
        ],
        "misconception_tags": ["multiplying_base_before_exponent", "exponential_bodmas"],
    }


def arch_24_inverse_proportion_function_xy_equals_k(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([24, 36, 48, 60, 72])
    x_test = rng.choice([x for x in [2, 3, 4, 6, 8, 12] if k % x == 0])
    y_val = k // x_test

    return {
        "subskill": "24_inverse_proportion_function_xy_equals_k",
        "question_text": (
            f"Two variables $x$ and $y$ are inversely proportional such that $x \\times y = {k}$ (or $y = \\frac{{{k}}}{{x}}$).\n\n"
            f"Calculate the value of **$y$** when **$x = {x_test}$**."
        ),
        "correct_answer": str(y_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute $x = {x_test}$: $y = \\frac{{{k}}}{{{x_test}}}$", "marks": 1},
            {"step": f"Evaluate: $y = {y_val}$", "marks": 1},
        ],
        "hints": [
            f"In an inverse proportion, the product of $x$ and $y$ is constant: $x \\times y = {k}$.",
            f"Divide ${k}$ by ${x_test}$: $y = \\frac{{{k}}}{{{x_test}}} = {y_val}$.",
        ],
        "misconception_tags": ["inverse_proportion_concept", "confusing_inverse_with_direct_variation"],
    }


def arch_25_inverse_proportion_table_find_missing_values(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([36, 48, 60])
    factors = [x for x in [1, 2, 3, 4, 6, 12] if k % x == 0][:5]
    x_vals = factors
    y_vals = [k // x for x in x_vals]

    target_idx = 3
    target_x = x_vals[target_idx]
    target_y = y_vals[target_idx]
    display_y = [str(y) if i != target_idx else "H" for i, y in enumerate(y_vals)]

    seed_val = rng.randint(1000, 999999)
    svg = draw_function_table_svg(x_vals, display_y, rule_label=f"xy = {k}", seed=seed_val)

    return {
        "subskill": "25_inverse_proportion_table_find_missing_values",
        "question_text": (
            f"The table below represents an inverse proportion where the product of $x$ and $y$ is constantly equal to ${k}$:\n\n"
            f"Determine the missing output **$H$** when **$x = {target_x}$**."
        ),
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_y),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply product rule: ${target_x} \\times H = {k}$", "marks": 1},
            {"step": f"Solve: $H = \\frac{{{k}}}{{{target_x}}} = {target_y}$", "marks": 1},
        ],
        "hints": [
            f"Notice that $1 \\times {k} = {k}$ and $2 \\times {k // 2} = {k}$. Every column product is ${k}$.",
            f"Therefore, ${target_x} \\times H = {k}$.",
            f"$H = {k} \\div {target_x} = {target_y}$.",
        ],
        "misconception_tags": ["inverse_proportion_table_solving", "constant_product_concept"],
    }
