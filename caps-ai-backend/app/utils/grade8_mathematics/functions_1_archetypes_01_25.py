"""
Grade 8 Mathematics - Functions and Relationships 1 Archetypes 01 to 25.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Functions and relationships 1.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def arch_01_single_step_flow_diagram_multiplication(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6, 7, 8])
    in_val = rng.randint(4, 12)
    out_val = m * in_val

    return {
        "title": "Single-Step Flow Diagram (Multiplication)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "01_single_step_flow_diagram_multiplication",
        "difficulty": "easy",
        "question_text": (
            f"A function machine has the single operational rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when the input is $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Multiply input by {m}: {in_val} * {m} = {out_val} (1 mark)",
        ],
        "hints": [
            f"The rule directs you to multiply the input $x$ by {m}.",
            f"Substitute $x = {in_val}$: $y = {in_val} \\times {m}$.",
            f"$y = {out_val}$.",
        ],
        "misconception_tags": ["multiplication_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_02_single_step_flow_diagram_addition(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(7, 25)
    in_val = rng.randint(5, 20)
    out_val = in_val + c

    return {
        "title": "Single-Step Flow Diagram (Addition)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "02_single_step_flow_diagram_addition",
        "difficulty": "easy",
        "question_text": (
            f"Consider the single-step operational rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Determine the output $y$ when the input is $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Add {c} to input {in_val}: {in_val} + {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"Add the constant {c} to the input.",
            f"${in_val} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["addition_arithmetic_slip"],
        "diagram_spec": None,
    }


def arch_03_two_step_flow_diagram_multiply_then_add(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(2, 9)
    in_val = rng.randint(3, 10)
    out_val = m * in_val + c

    return {
        "title": "Two-Step Flow Diagram (Multiply then Add)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "03_two_step_flow_diagram_multiply_then_add",
        "difficulty": "medium",
        "question_text": (
            f"An input-output rule operates in two consecutive stages:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Stage 1: {in_val} * {m} = {in_val * m} (1 mark)",
            f"Stage 2: {in_val * m} + {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"First multiply {in_val} by {m}: ${in_val} \\times {m} = {in_val * m}$.",
            f"Then add {c}: ${in_val * m} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["two_step_operator_precedence_error"],
        "diagram_spec": None,
    }


def arch_04_two_step_flow_diagram_multiply_then_subtract(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 6)
    c = rng.randint(3, 8)
    in_val = rng.randint(4, 11)
    out_val = m * in_val - c

    return {
        "title": "Two-Step Flow Diagram (Multiply then Subtract)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "04_two_step_flow_diagram_multiply_then_subtract",
        "difficulty": "medium",
        "question_text": (
            f"Evaluate the two-step flow diagram:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{- {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Find the value of $y$ corresponding to $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Stage 1: {in_val} * {m} = {in_val * m} (1 mark)",
            f"Stage 2: {in_val * m} - {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"Stage 1: Multiply $x$ by {m}: ${in_val} \\times {m} = {in_val * m}$.",
            f"Stage 2: Subtract {c}: ${in_val * m} - {c} = {out_val}$.",
        ],
        "misconception_tags": ["subtraction_order_error"],
        "diagram_spec": None,
    }


def arch_05_two_step_flow_diagram_add_then_multiply_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 5)
    in_val = rng.randint(3, 9)
    out_val = (in_val + a) * b

    return {
        "title": "Two-Step Flow Diagram (Add then Multiply / Bracketed Form)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "05_two_step_flow_diagram_add_then_multiply_brackets",
        "difficulty": "medium",
        "question_text": (
            f"Consider the two-step operational rule where addition precedes multiplication:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{+ {a}}} \\longrightarrow \\boxed{{\\times {b}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Stage 1: {in_val} + {a} = {in_val + a} (1 mark)",
            f"Stage 2: {in_val + a} * {b} = {out_val} (1 mark)",
        ],
        "hints": [
            f"Follow the arrows in order: first perform addition.",
            f"${in_val} + {a} = {in_val + a}$.",
            f"Then multiply by {b}: $({in_val + a}) \\times {b} = {out_val}$.",
        ],
        "misconception_tags": ["bracket_operation_order_error"],
        "diagram_spec": None,
    }


def arch_06_two_step_flow_diagram_divide_then_add(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([2, 3, 4, 5])
    k = rng.randint(2, 6)
    in_val = d * k
    c = rng.randint(3, 9)
    out_val = (in_val // d) + c

    return {
        "title": "Two-Step Flow Diagram (Divide then Add)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "06_two_step_flow_diagram_divide_then_add",
        "difficulty": "medium",
        "question_text": (
            f"A function has the rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\div {d}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Find the output $y$ when the input is $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Stage 1: {in_val} / {d} = {in_val // d} (1 mark)",
            f"Stage 2: {in_val // d} + {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"First divide: ${in_val} \\div {d} = {in_val // d}$.",
            f"Then add {c}: ${in_val // d} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["division_flow_diagram_error"],
        "diagram_spec": None,
    }


def arch_07_flow_diagram_with_negative_integer_inputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 6)
    c = rng.randint(2, 8)
    in_val = -rng.randint(2, 7)
    out_val = m * in_val + c

    return {
        "title": "Flow Diagram with Negative Integer Input",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "07_flow_diagram_with_negative_integer_inputs",
        "difficulty": "hard",
        "question_text": (
            f"Evaluate the two-step operational rule for a negative input integer:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Determine the value of $y$ when $x = {in_val}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Multiply negative input: {in_val} * {m} = {in_val * m} (1 mark)",
            f"Add constant: {in_val * m} + {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"Multiplying a negative by a positive yields a negative: $({in_val}) \\times {m} = {in_val * m}$.",
            f"Now add {c}: ${in_val * m} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["negative_integer_multiplication_sign_error"],
        "diagram_spec": None,
    }


def arch_08_flow_diagram_with_fractional_inputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([4, 6, 8, 9])
    num = rng.choice([1, 3])
    den = 2 if m in [4, 6, 8] else 3
    # in_val = num / den
    c = rng.randint(1, 5)
    # y = m * (num / den) + c
    out_val = (m * num) // den + c

    return {
        "title": "Flow Diagram with Fractional Input",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "08_flow_diagram_with_fractional_inputs",
        "difficulty": "hard",
        "question_text": (
            f"An algebraic flow diagram rule is given by:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when the input is the fraction $x = \\frac{{{num}}}{{{den}}}$."
        ),
        "correct_answer": str(out_val),
        "marking_schema": [
            f"Multiply fraction: {m} * ({num}/{den}) = {(m * num) // den} (1 mark)",
            f"Add constant: {(m * num) // den} + {c} = {out_val} (1 mark)",
        ],
        "hints": [
            f"Stage 1: ${m} \\times \\frac{{{num}}}{{{den}}} = \\frac{{{m * num}}}{{{den}}} = {(m * num) // den}$.",
            f"Stage 2: ${(m * num) // den} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["fraction_multiplication_in_function_error"],
        "diagram_spec": None,
    }


def arch_09_flow_diagram_with_decimal_inputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 4, 5])
    in_val = rng.choice([1.2, 1.5, 2.4, 3.5])
    c = rng.choice([1.1, 2.5, 3.2])
    out_val = round(m * in_val + c, 2)
    in_str = str(in_val).replace(".", ",")
    c_str = str(c).replace(".", ",")
    ans_str = str(out_val).replace(".", ",")

    return {
        "title": "Flow Diagram with Decimal Inputs",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "09_flow_diagram_with_decimal_inputs",
        "difficulty": "medium",
        "question_text": (
            f"Evaluate the operational rule for a decimal input:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c_str}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when $x = {in_str}$. Express your answer using comma decimal notation."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Multiply decimal: {in_str} * {m} = {str(round(m * in_val, 2)).replace('.', ',')} (1 mark)",
            f"Add decimal: {ans_str} (1 mark)",
        ],
        "hints": [
            f"${in_val} \\times {m} = {round(m * in_val, 2)}$.",
            f"${round(m * in_val, 2)} + {c} = {out_val}$.",
        ],
        "misconception_tags": ["decimal_arithmetic_in_function_error"],
        "diagram_spec": None,
    }


def arch_10_inverse_flow_diagram_one_step_reversal(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([4, 5, 6, 7, 8])
    in_val = rng.randint(5, 14)
    out_val = m * in_val

    return {
        "title": "Inverse Flow Diagram (One-Step Reversal)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "10_inverse_flow_diagram_one_step_reversal",
        "difficulty": "easy",
        "question_text": (
            f"A function machine multiplies the input by {m}:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"If the output is $y = {out_val}$, use the inverse operation to calculate the input $x$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Apply inverse operation: x = {out_val} / {m} (1 mark)",
            f"Calculate input x = {in_val} (1 mark)",
        ],
        "hints": [
            f"The inverse of multiplying by {m} is dividing by {m}.",
            f"$x = {out_val} \\div {m} = {in_val}$.",
        ],
        "misconception_tags": ["inverse_operation_confusion"],
        "diagram_spec": None,
    }


def arch_11_inverse_flow_diagram_two_step_subtraction_then_division(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(2, 9)
    in_val = rng.randint(4, 12)
    out_val = m * in_val + c

    return {
        "title": "Inverse Operations (Output to Input: Subtract then Divide)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "11_inverse_flow_diagram_two_step_subtraction_then_division",
        "difficulty": "medium",
        "question_text": (
            f"A two-step flow diagram follows the rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"If the output is $y = {out_val}$, work backwards using inverse operations to find the input $x$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Inverse stage 1: {out_val} - {c} = {out_val - c} (1 mark)",
            f"Inverse stage 2: {out_val - c} / {m} = {in_val} (1 mark)",
        ],
        "hints": [
            f"Undo the addition of {c} first: ${out_val} - {c} = {out_val - c}$.",
            f"Then undo multiplication by {m}: ${out_val - c} \\div {m} = {in_val}$.",
        ],
        "misconception_tags": ["inverse_order_of_operations_reversal"],
        "diagram_spec": None,
    }


def arch_12_inverse_flow_diagram_addition_then_division(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 6)
    c = rng.randint(3, 8)
    in_val = rng.randint(4, 12)
    out_val = m * in_val - c

    return {
        "title": "Inverse Operations (Output to Input: Add then Divide)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "12_inverse_flow_diagram_addition_then_division",
        "difficulty": "medium",
        "question_text": (
            f"Consider the two-step input-output rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{- {c}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"If $y = {out_val}$, determine the value of the input $x$."
        ),
        "correct_answer": str(in_val),
        "marking_schema": [
            f"Add constant: {out_val} + {c} = {out_val + c} (1 mark)",
            f"Divide by multiplier: {out_val + c} / {m} = {in_val} (1 mark)",
        ],
        "hints": [
            f"Work backwards: The inverse of subtracting {c} is adding {c}: ${out_val} + {c} = {out_val + c}$.",
            f"The inverse of multiplying by {m} is dividing by {m}: ${out_val + c} \\div {m} = {in_val}$.",
        ],
        "misconception_tags": ["inverse_sign_slip"],
        "diagram_spec": None,
    }


def arch_13_equivalent_flow_diagrams_order_of_operations_comparison(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3])
    c = rng.choice([2, 4, 6])
    x_test = rng.randint(3, 8)
    # Machine A: (x * m) + c
    out_a = (x_test * m) + c
    # Machine B: (x + c) * m
    out_b = (x_test + c) * m
    is_equal = "No"

    return {
        "title": "Equivalent Flow Diagrams (Order of Operations Comparison)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "13_equivalent_flow_diagrams_order_of_operations_comparison",
        "difficulty": "medium",
        "question_text": (
            f"Two flow diagrams are proposed:\n\n"
            f"* **Diagram A:** $x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow y$\n"
            f"* **Diagram B:** $x \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow y$\n\n"
            f"Do Diagram A and Diagram B produce identical outputs for all inputs? Answer **Yes** or **No**."
        ),
        "correct_answer": is_equal,
        "marking_schema": [
            f"Test with input x = {x_test}: Diagram A gives {out_a}, Diagram B gives {out_b} (1 mark)",
            "Conclude that order of operations produces different results: No (1 mark)",
        ],
        "hints": [
            f"Diagram A evaluates $y = {m}x + {c}$.",
            f"Diagram B evaluates $y = {m}(x + {c}) = {m}x + {m * c}$.",
            f"Since ${c} \\neq {m * c}$, they are not equivalent: answer is No.",
        ],
        "misconception_tags": ["flow_diagram_commutativity_fallacy"],
        "diagram_spec": None,
    }


def arch_14_equivalent_flow_diagrams_distributive_equivalence(rng: random.Random) -> Dict[str, Any]:
    # 2 * (x + a) vs 2x + 2a
    mult = rng.choice([2, 3, 4])
    a = rng.randint(2, 5)
    expanded_c = mult * a

    return {
        "title": "Equivalent Flow Diagrams (Distributive Property)",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "14_equivalent_flow_diagrams_distributive_equivalence",
        "difficulty": "medium",
        "question_text": (
            f"Consider the rule $y = {mult}(x + {a})$.\n\n"
            f"Which two-step flow diagram produces the exact same output for any input $x$?\n\n"
            f"* **Option 1:** $x \\longrightarrow \\boxed{{\\times {mult}}} \\longrightarrow \\boxed{{+ {a}}} \\longrightarrow y$\n"
            f"* **Option 2:** $x \\longrightarrow \\boxed{{\\times {mult}}} \\longrightarrow \\boxed{{+ {expanded_c}}} \\longrightarrow y$\n\n"
            f"State whether **Option 1** or **Option 2** is equivalent."
        ),
        "correct_answer": "Option 2",
        "marking_schema": [
            f"Expand distributive brackets: {mult}(x + {a}) = {mult}x + {expanded_c} (1 mark)",
            "Identify matching flow diagram: Option 2 (1 mark)",
        ],
        "hints": [
            f"Use the distributive law: ${mult}(x + {a}) = {mult}x + {mult * a} = {mult}x + {expanded_c}$.",
            f"This matches multiplying by {mult} then adding {expanded_c}.",
            "Option 2 is the correct equivalent diagram.",
        ],
        "misconception_tags": ["distributive_expansion_neglect"],
        "diagram_spec": None,
    }


def arch_15_deducing_missing_multiplier_in_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6, 7])
    c = rng.randint(2, 6)
    x1, y1 = 2, m * 2 + c
    x2, y2 = 3, m * 3 + c

    return {
        "title": "Deducing Missing Multiplier in Flow Diagram",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "15_deducing_missing_multiplier_in_flow_diagram",
        "difficulty": "medium",
        "question_text": (
            f"A flow diagram has an unknown multiplier $m$:\n\n"
            f"$$x \\longrightarrow \\boxed{{\\times m}} \\longrightarrow \\boxed{{+ {c}}} \\longrightarrow y$$\n\n"
            f"When $x = {x1}$, $y = {y1}$, and when $x = {x2}$, $y = {y2}$.\n"
            f"Determine the value of $m$."
        ),
        "correct_answer": str(m),
        "marking_schema": [
            f"Calculate change in output: {y2} - {y1} = {m} (1 mark)",
            f"Deduce multiplier m = {m} (1 mark)",
        ],
        "hints": [
            f"When input increases by 1 (from {x1} to {x2}), the output increases by ${y2} - {y1} = {m}$.",
            f"Therefore, the multiplier $m$ must be {m}.",
        ],
        "misconception_tags": ["multiplier_rate_of_change_deduction_error"],
        "diagram_spec": None,
    }


def arch_16_deducing_missing_constant_in_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(3, 9)
    in_val = rng.randint(3, 8)
    out_val = m * in_val + c

    return {
        "title": "Deducing Missing Constant in Flow Diagram",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "16_deducing_missing_constant_in_flow_diagram",
        "difficulty": "medium",
        "question_text": (
            f"In the function rule below, the constant $c$ is unknown:\n\n"
            f"$$x \\longrightarrow \\boxed{{\\times {m}}} \\longrightarrow \\boxed{{+ c}} \\longrightarrow y$$\n\n"
            f"If an input of $x = {in_val}$ produces an output of $y = {out_val}$, find the value of $c$."
        ),
        "correct_answer": str(c),
        "marking_schema": [
            f"Set up equation: {m}({in_val}) + c = {out_val} (1 mark)",
            f"Solve for c: {out_val} - {m * in_val} = {c} (1 mark)",
        ],
        "hints": [
            f"${m} \\times {in_val} = {m * in_val}$.",
            f"We need ${m * in_val} + c = {out_val}$.",
            f"$c = {out_val} - {m * in_val} = {c}$.",
        ],
        "misconception_tags": ["constant_deduction_equation_error"],
        "diagram_spec": None,
    }


def arch_17_deducing_two_missing_operators_from_input_output_pairs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([2, 4, 7])
    # y = m*x - c
    x1, y1 = 1, m * 1 - c
    x2, y2 = 2, m * 2 - c

    return {
        "title": "Deducing Two Missing Operators from Pairs",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "17_deducing_two_missing_operators_from_input_output_pairs",
        "difficulty": "hard",
        "question_text": (
            f"An algebraic rule follows the form $y = m \\cdot x - c$.\n\n"
            f"* When $x = {x1}$, $y = {y1}$\n"
            f"* When $x = {x2}$, $y = {y2}$\n\n"
            f"Determine the values of $m$ and $c$. Express your answer in the form $m = \\dots;\\ c = \\dots$."
        ),
        "correct_answer": f"m = {m}; c = {c}",
        "marking_schema": [
            f"Find rate of change m = {y2} - {y1} = {m} (1 mark)",
            f"Substitute to find c: {m}(1) - c = {y1} => c = {c} (1 mark)",
        ],
        "hints": [
            f"The difference between outputs is ${y2} - ({y1}) = {m}$, so $m = {m}$.",
            f"Substitute $x = 1$: ${m}(1) - c = {y1} \\implies {m} - c = {y1} \\implies c = {c}$.",
        ],
        "misconception_tags": ["two_unknown_rule_deduction_error"],
        "diagram_spec": None,
    }


def arch_18_completing_table_outputs_from_linear_rule_positive_coeff(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 6)
    c = rng.randint(1, 5)
    x_vals = [1, 2, 3, 5]
    y_vals = [m * x + c for x in x_vals]
    target_x = x_vals[3]
    target_y = y_vals[3]

    return {
        "title": "Completing Table Outputs from Linear Rule",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "18_completing_table_outputs_from_linear_rule_positive_coeff",
        "difficulty": "easy",
        "question_text": (
            f"Given the linear function rule $y = {m}x + {c}$, find the missing output $k$ in the table:\n\n"
            f"| $x$ | 1 | 2 | 3 | {target_x} |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | $k$ |\n\n"
            f"State the value of $k$."
        ),
        "correct_answer": str(target_y),
        "marking_schema": [
            f"Substitute x = {target_x}: y = {m}({target_x}) + {c} = {target_y} (1 mark)",
        ],
        "hints": [
            f"Use the formula $y = {m}x + {c}$.",
            f"Substitute $x = {target_x}$: $k = {m}({target_x}) + {c} = {m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["table_substitution_error"],
        "diagram_spec": None,
    }


def arch_19_completing_table_outputs_from_linear_rule_negative_coeff(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(2, 5)
    c = rng.randint(20, 50)
    # y = -m*x + c
    x_vals = [1, 2, 3, 6]
    y_vals = [-m * x + c for x in x_vals]
    target_x = x_vals[3]
    target_y = y_vals[3]

    return {
        "title": "Completing Table with Negative Coefficient",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "19_completing_table_outputs_from_linear_rule_negative_coeff",
        "difficulty": "medium",
        "question_text": (
            f"A function has the decreasing rule $y = -{m}x + {c}$.\n\n"
            f"| $x$ | 1 | 2 | 3 | {target_x} |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | $p$ |\n\n"
            f"Calculate the value of $p$."
        ),
        "correct_answer": str(target_y),
        "marking_schema": [
            f"Substitute x = {target_x}: y = -{m}({target_x}) + {c} = {target_y} (1 mark)",
        ],
        "hints": [
            f"Substitute $x = {target_x}$ into $y = -{m}x + {c}$.",
            f"$p = -{m}({target_x}) + {c} = -{m * target_x} + {c} = {target_y}$.",
        ],
        "misconception_tags": ["negative_gradient_evaluation_slip"],
        "diagram_spec": None,
    }


def arch_20_completing_table_inputs_from_outputs_using_inverses(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(2, 8)
    target_x = rng.randint(5, 12)
    target_y = m * target_x + c

    return {
        "title": "Finding Input from Table Output",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "20_completing_table_inputs_from_outputs_using_inverses",
        "difficulty": "medium",
        "question_text": (
            f"The rule connecting $x$ and $y$ is $y = {m}x + {c}$.\n\n"
            f"If an entry in the table shows an output value of $y = {target_y}$, determine the corresponding input value $x$."
        ),
        "correct_answer": str(target_x),
        "marking_schema": [
            f"Set up equation {m}x + {c} = {target_y} (1 mark)",
            f"Solve for x: x = ({target_y} - {c}) / {m} = {target_x} (1 mark)",
        ],
        "hints": [
            f"Set $y = {target_y}$ in $y = {m}x + {c}$.",
            f"${m}x + {c} = {target_y} \\implies {m}x = {target_y - c}$.",
            f"$x = \\frac{{{target_y - c}}}{{{m}}} = {target_x}$.",
        ],
        "misconception_tags": ["input_output_role_reversal"],
        "diagram_spec": None,
    }


def arch_21_completing_mixed_table_both_inputs_and_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 6)
    c = rng.randint(1, 7)
    # y = m*x + c
    x1, y1 = 4, m * 4 + c
    x2, y2 = 7, m * 7 + c

    return {
        "title": "Completing Mixed Input/Output Table",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "21_completing_mixed_table_both_inputs_and_outputs",
        "difficulty": "hard",
        "question_text": (
            f"A table follows the function rule $y = {m}x + {c}$:\n\n"
            f"| $x$ | 1 | 2 | {x1} | $b$ |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {m*1+c} | {m*2+c} | $a$ | {y2} |\n\n"
            f"Determine the values of $a$ and $b$. Express your answer as $a = \\dots;\\ b = \\dots$."
        ),
        "correct_answer": f"a = {y1}; b = {x2}",
        "marking_schema": [
            f"Calculate output a = {m}({x1}) + {c} = {y1} (1 mark)",
            f"Calculate input b = ({y2} - {c}) / {m} = {x2} (1 mark)",
        ],
        "hints": [
            f"To find $a$: Substitute $x = {x1}$ into $y = {m}({x1}) + {c} = {y1}$.",
            f"To find $b$: Solve ${m}b + {c} = {y2} \\implies {m}b = {y2 - c} \\implies b = {x2}$.",
        ],
        "misconception_tags": ["mixed_table_forward_backward_slip"],
        "diagram_spec": None,
    }


def arch_22_identifying_independent_and_dependent_variables_in_context(rng: random.Random) -> Dict[str, Any]:
    contexts = [
        ("the number of hours parked ($h$)", "the total parking cost ($C$)", "h", "C"),
        ("the amount of petrol purchased ($L$)", "the total cost in Rand ($R$)", "L", "R"),
        ("the time spent travelling ($t$)", "the distance covered ($d$)", "t", "d"),
        ("the number of text messages sent ($n$)", "the total phone bill ($B$)", "n", "B"),
    ]
    indep_desc, dep_desc, indep_var, dep_var = rng.choice(contexts)

    return {
        "title": "Identifying Independent and Dependent Variables",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "22_identifying_independent_and_dependent_variables_in_context",
        "difficulty": "easy",
        "question_text": (
            f"In a real-world scenario relating {indep_desc} and {dep_desc}:\n\n"
            f"Which quantity represents the **independent variable** (the input quantity that can be chosen freely)?"
        ),
        "correct_answer": indep_desc,
        "marking_schema": [
            f"Identify independent variable correctly: {indep_desc} (1 mark)",
        ],
        "hints": [
            "The independent variable is the input that changes freely.",
            "The dependent variable is the output that depends on the chosen input.",
            f"Here, {dep_desc} depends on {indep_desc}.",
        ],
        "misconception_tags": ["independent_vs_dependent_variable_confusion"],
        "diagram_spec": None,
    }


def arch_23_formulating_algebraic_rule_from_two_column_table(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(1, 8)
    # y = mx + c
    x_vals = [1, 2, 3, 4]
    y_vals = [m * x + c for x in x_vals]

    return {
        "title": "Formulating Algebraic Rule from Table of Values",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "23_formulating_algebraic_rule_from_two_column_table",
        "difficulty": "medium",
        "question_text": (
            f"Study the input-output pairs in the table below:\n\n"
            f"| $x$ | 1 | 2 | 3 | 4 |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Determine the general algebraic formula relating $y$ to $x$. Express your answer in the form $y = mx + c$."
        ),
        "correct_answer": f"y = {m}x + {c}",
        "marking_schema": [
            f"Determine rate of change / multiplier m = {m} (1 mark)",
            f"Determine constant c = y_1 - m = {c} (1 mark)",
            f"State formula y = {m}x + {c} (1 mark)",
        ],
        "hints": [
            f"Observe how $y$ changes as $x$ increases by 1: ${y_vals[1]} - {y_vals[0]} = {m}$.",
            f"So the formula begins $y = {m}x + c$.",
            f"Substitute $x = 1$: $y = {m}(1) + c = {y_vals[0]} \\implies c = {c}$. Thus $y = {m}x + {c}$.",
        ],
        "misconception_tags": ["table_rule_formulation_error"],
        "diagram_spec": None,
    }


def arch_24_formulating_rule_with_fractional_rate_from_table(rng: random.Random) -> Dict[str, Any]:
    # y = (x / d) + c
    d = rng.choice([2, 4])
    c = rng.randint(1, 4)
    x_vals = [2, 4, 6, 8] if d == 2 else [4, 8, 12, 16]
    y_vals = [(x // d) + c for x in x_vals]

    return {
        "title": "Formulating Rule with Division Rate from Table",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "24_formulating_rule_with_fractional_rate_from_table",
        "difficulty": "hard",
        "question_text": (
            f"Examine the values in the table:\n\n"
            f"| $x$ | {x_vals[0]} | {x_vals[1]} | {x_vals[2]} | {x_vals[3]} |\n"
            f"| :--- | :---: | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} |\n\n"
            f"Notice that $y$ increases by only 1 unit while $x$ increases by {d} units.\n"
            f"Write down the formula for $y$ in terms of $x$."
        ),
        "correct_answer": f"y = x/{d} + {c}",
        "marking_schema": [
            f"Recognize gradient 1/{d} (1 mark)",
            f"State formula y = x/{d} + {c} (or y = 0.5x + {c}) (1 mark)",
        ],
        "hints": [
            f"Rate of change is $\\frac{{\\Delta y}}{{\\Delta x}} = \\frac{{1}}{{{d}}}$.",
            f"Formula has the form $y = \\frac{{x}}{{{d}}} + c$.",
            f"For $x = {x_vals[0]}$: $\\frac{{{x_vals[0]}}}{{{d}}} + c = {y_vals[0]} \\implies {x_vals[0]//d} + c = {y_vals[0]} \\implies c = {c}$.",
        ],
        "misconception_tags": ["fractional_slope_misidentification"],
        "diagram_spec": None,
    }


def arch_25_testing_which_formula_matches_a_given_table(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.choice([1, 3, 5])
    correct_formula = f"y = {m}x + {c}"
    distractor_1 = f"y = {m+1}x + {c}"
    distractor_2 = f"y = {m}x + {c+2}"
    x_vals = [1, 2, 3]
    y_vals = [m * x + c for x in x_vals]

    return {
        "title": "Matching Formula to Given Table",
        "topic": "Functions and relationships 1",
        "grade": 8,
        "term": 1,
        "subskill": "25_testing_which_formula_matches_a_given_table",
        "difficulty": "medium",
        "question_text": (
            f"Which of the following formulae correctly describes the relationship in the table?\n\n"
            f"| $x$ | 1 | 2 | 3 |\n"
            f"| :--- | :---: | :---: | :---: |\n"
            f"| $y$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} |\n\n"
            f"* **A:** ${distractor_1}$\n"
            f"* **B:** ${correct_formula}$\n"
            f"* **C:** ${distractor_2}$\n\n"
            f"State the correct letter (**A**, **B**, or **C**)."
        ),
        "correct_answer": "B",
        "marking_schema": [
            f"Test values into formulae (1 mark)",
            "Identify B as the matching formula (1 mark)",
        ],
        "hints": [
            f"Test $x = 1$: Formula B gives $y = {m}(1) + {c} = {y_vals[0]}$, matching the table.",
            f"Test $x = 2$: Formula B gives $y = {m}(2) + {c} = {y_vals[1]}$, matching the table.",
            "Formula B is correct.",
        ],
        "misconception_tags": ["formula_verification_substitution_error"],
        "diagram_spec": None,
    }
