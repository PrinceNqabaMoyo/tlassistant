"""Grade 7 Mathematics - Functions and Relationships 1: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 1.md
Focus: Flow diagrams, single & two-step function machines, forward evaluation, and inverse operations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_flow_box(
    inp_val: str,
    op1: str,
    op2: Optional[str] = None,
    out_val: str = "?",
    width: int = 380,
    height: int = 80,
) -> str:
    """Generates a publication-grade SVG flow diagram with input circle, operator rectangle(s), and output circle."""
    elements = []
    # Input circle
    elements.append('<circle cx="40" cy="40" r="24" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>')
    elements.append(f'<text x="40" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{inp_val}</text>')
    
    # Arrow to box 1
    elements.append('<line x1="64" y1="40" x2="105" y2="40" stroke="#1e293b" stroke-width="2"/>')
    elements.append('<polygon points="105,36 115,40 105,44" fill="#1e293b"/>')

    if op2 is None:
        # Single box
        elements.append('<rect x="115" y="16" width="120" height="48" rx="6" fill="#f1f5f9" stroke="#1e293b" stroke-width="2"/>')
        elements.append(f'<text x="175" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">{op1}</text>')
        # Arrow to output
        elements.append('<line x1="235" y1="40" x2="276" y2="40" stroke="#1e293b" stroke-width="2"/>')
        elements.append('<polygon points="276,36 286,40 276,44" fill="#1e293b"/>')
        # Output circle
        elements.append('<circle cx="316" cy="40" r="24" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>')
        elements.append(f'<text x="316" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{out_val}</text>')
    else:
        # Two boxes
        elements.append('<rect x="115" y="16" width="75" height="48" rx="6" fill="#f1f5f9" stroke="#1e293b" stroke-width="2"/>')
        elements.append(f'<text x="152" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{op1}</text>')
        # Connecting arrow
        elements.append('<line x1="190" y1="40" x2="210" y2="40" stroke="#1e293b" stroke-width="2"/>')
        elements.append('<polygon points="210,36 220,40 210,44" fill="#1e293b"/>')
        # Box 2
        elements.append('<rect x="220" y="16" width="75" height="48" rx="6" fill="#f1f5f9" stroke="#1e293b" stroke-width="2"/>')
        elements.append(f'<text x="257" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{op2}</text>')
        # Arrow to output
        elements.append('<line x1="295" y1="40" x2="315" y2="40" stroke="#1e293b" stroke-width="2"/>')
        elements.append('<polygon points="315,36 325,40 315,44" fill="#1e293b"/>')
        # Output circle
        elements.append('<circle cx="350" cy="40" r="24" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>')
        elements.append(f'<text x="350" y="45" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{out_val}</text>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{"".join(elements)}'
        f'</svg>'
    )


# 01. Single operation forward addition
def arch_01_single_operation_forward_addition(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(12, 45)
    c = rng.randint(8, 25)
    ans = str(x + c)
    svg = _svg_flow_box(str(x), f"+ {c}", out_val="?")
    prompt = f"In the flow diagram below, calculate the output value:"
    sol = f"**Step 1:** Apply the operation: $${x} + {c} = \\mathbf{{{ans}}}$$"
    return {
        "id": f"g7_fn1_01_{rng.randint(100000, 999999)}",
        "subskill": "01_single_operation_forward_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_01",
        "hints": {"tier_1": f"Add {c} to the input value {x}.", "tier_2": f"{x} + {c}", "tier_3": ans},
        "misconception_tags": ["addition_error"]
    }


# 02. Single operation forward subtraction
def arch_02_single_operation_forward_subtraction(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(7, 19)
    ans_int = rng.randint(10, 35)
    x = ans_int + c
    ans = str(ans_int)
    svg = _svg_flow_box(str(x), f"- {c}", out_val="?")
    prompt = f"Calculate the output value for the flow diagram:"
    sol = f"**Step 1:** Subtract {c} from the input:\n$${x} - {c} = \\mathbf{{{ans}}}$$"
    return {
        "id": f"g7_fn1_02_{rng.randint(100000, 999999)}",
        "subskill": "02_single_operation_forward_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_02",
        "hints": {"tier_1": f"Subtract {c} from {x}.", "tier_2": f"{x} - {c}", "tier_3": ans},
        "misconception_tags": ["subtraction_order_reversal"]
    }


# 03. Single operation forward multiplication
def arch_03_single_operation_forward_multiplication(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(4, 12)
    m = rng.randint(3, 9)
    ans = str(x * m)
    svg = _svg_flow_box(str(x), f"× {m}", out_val="?")
    prompt = f"Determine the output value for the flow diagram:"
    sol = f"**Step 1:** Multiply the input by {m}:\n$${x} \\times {m} = \\mathbf{{{ans}}}$$"
    return {
        "id": f"g7_fn1_03_{rng.randint(100000, 999999)}",
        "subskill": "03_single_operation_forward_multiplication",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_03",
        "hints": {"tier_1": f"Multiply {x} by {m}.", "tier_2": f"{x} * {m}", "tier_3": ans},
        "misconception_tags": ["times_table_multiplication_error"]
    }


# 04. Single operation forward division
def arch_04_single_operation_forward_division(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(3, 8)
    ans_int = rng.randint(6, 15)
    x = d * ans_int
    ans = str(ans_int)
    svg = _svg_flow_box(str(x), f"÷ {d}", out_val="?")
    prompt = f"Find the output value for the following flow diagram:"
    sol = f"**Step 1:** Divide {x} by {d}:\n$${x} \\div {d} = \\mathbf{{{ans}}}$$"
    return {
        "id": f"g7_fn1_04_{rng.randint(100000, 999999)}",
        "subskill": "04_single_operation_forward_division",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_04",
        "hints": {"tier_1": f"Divide {x} by {d}.", "tier_2": f"{x} / {d}", "tier_3": ans},
        "misconception_tags": ["division_fact_error"]
    }


# 05. Single operation reverse subtraction to addition
def arch_05_single_operation_reverse_subtraction_to_addition(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(9, 24)
    out_val = rng.randint(15, 40)
    inp_val = out_val + c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"- {c}", out_val=str(out_val))
    prompt = f"In the flow diagram below, find the input number \\(x\\):"
    sol = (
        f"**Step 1:** To find the input from the output, use the **inverse operation**.\n"
        f"The inverse of subtracting {c} is adding {c}.\n\n"
        f"**Step 2:**\n$$x = {out_val} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_05_{rng.randint(100000, 999999)}",
        "subskill": "05_single_operation_reverse_subtraction_to_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_05",
        "hints": {"tier_1": f"Use the inverse operation: add {c} to {out_val}.", "tier_2": f"{out_val} + {c}", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_reverse"]
    }


# 06. Single operation reverse addition to subtraction
def arch_06_single_operation_reverse_addition_to_subtraction(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(11, 29)
    inp_val = rng.randint(14, 50)
    out_val = inp_val + c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"+ {c}", out_val=str(out_val))
    prompt = f"Determine the unknown input value \\(x\\):"
    sol = (
        f"**Step 1:** The inverse of adding {c} is subtracting {c}.\n\n"
        f"**Step 2:**\n$$x = {out_val} - {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_06_{rng.randint(100000, 999999)}",
        "subskill": "06_single_operation_reverse_addition_to_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_06",
        "hints": {"tier_1": f"Subtract {c} from {out_val}.", "tier_2": f"{out_val} - {c}", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_subtracting_in_reverse"]
    }


# 07. Single operation reverse division to multiplication
def arch_07_single_operation_reverse_division_to_multiplication(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(4, 9)
    out_val = rng.randint(5, 12)
    inp_val = out_val * d
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"÷ {d}", out_val=str(out_val))
    prompt = f"Find the value of the input \\(x\\):"
    sol = (
        f"**Step 1:** The inverse of dividing by {d} is multiplying by {d}.\n\n"
        f"**Step 2:**\n$$x = {out_val} \\times {d} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_07_{rng.randint(100000, 999999)}",
        "subskill": "07_single_operation_reverse_division_to_multiplication",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_07",
        "hints": {"tier_1": f"Multiply {out_val} by {d}.", "tier_2": f"{out_val} * {d}", "tier_3": ans},
        "misconception_tags": ["dividing_output_again"]
    }


# 08. Single operation reverse multiplication to division
def arch_08_single_operation_reverse_multiplication_to_division(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(4, 9)
    inp_val = rng.randint(6, 14)
    out_val = inp_val * m
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"× {m}", out_val=str(out_val))
    prompt = f"Solve for the input \\(x\\) in the flow diagram:"
    sol = (
        f"**Step 1:** The inverse of multiplying by {m} is dividing by {m}.\n\n"
        f"**Step 2:**\n$$x = {out_val} \\div {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_08_{rng.randint(100000, 999999)}",
        "subskill": "08_single_operation_reverse_multiplication_to_division",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_08",
        "hints": {"tier_1": f"Divide {out_val} by {m}.", "tier_2": f"{out_val} / {m}", "tier_3": ans},
        "misconception_tags": ["multiplying_in_reverse"]
    }


# 09. Two step rule multiply then add
def arch_09_two_step_rule_multiply_then_add(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.randint(3, 8)
    x = rng.randint(4, 10)
    step1 = x * m
    ans = str(step1 + c)
    svg = _svg_flow_box(str(x), f"× {m}", f"+ {c}", out_val="?")
    prompt = f"Determine the final output \\(y\\) for the two-step flow diagram:"
    sol = (
        f"**Step 1 (First operation):** Multiply input by {m}:\n$${x} \\times {m} = {step1}$$\n\n"
        f"**Step 2 (Second operation):** Add {c}:\n$${step1} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_09_{rng.randint(100000, 999999)}",
        "subskill": "09_two_step_rule_multiply_then_add",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_09",
        "hints": {"tier_1": f"First calculate {x} * {m}.", "tier_2": f"Then add {c} to {step1}.", "tier_3": ans},
        "misconception_tags": ["adding_before_multiplying"]
    }


# 10. Two step rule multiply then subtract
def arch_10_two_step_rule_multiply_then_subtract(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 6])
    c = rng.randint(4, 9)
    x = rng.randint(5, 11)
    step1 = x * m
    ans = str(step1 - c)
    svg = _svg_flow_box(str(x), f"× {m}", f"- {c}", out_val="?")
    prompt = f"Calculate the output \\(y\\) from the following flow diagram:"
    sol = (
        f"**Step 1:** $${x} \\times {m} = {step1}$$\n\n"
        f"**Step 2:** $${step1} - {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_10_{rng.randint(100000, 999999)}",
        "subskill": "10_two_step_rule_multiply_then_subtract",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_10",
        "hints": {"tier_1": f"Multiply {x} by {m} first.", "tier_2": f"Subtract {c} from {step1}.", "tier_3": ans},
        "misconception_tags": ["order_of_operations_reversal"]
    }


# 11. Two step rule divide then add
def arch_11_two_step_rule_divide_then_add(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([2, 3, 4])
    quot = rng.randint(4, 9)
    x = d * quot
    c = rng.randint(5, 15)
    ans = str(quot + c)
    svg = _svg_flow_box(str(x), f"÷ {d}", f"+ {c}", out_val="?")
    prompt = f"Calculate the output value for this flow diagram:"
    sol = (
        f"**Step 1:** Divide by {d}:\n$${x} \\div {d} = {quot}$$\n\n"
        f"**Step 2:** Add {c}:\n$${quot} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_11_{rng.randint(100000, 999999)}",
        "subskill": "11_two_step_rule_divide_then_add",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_11",
        "hints": {"tier_1": f"First divide {x} by {d}.", "tier_2": f"Then add {c} to {quot}.", "tier_3": ans},
        "misconception_tags": ["division_order_error"]
    }


# 12. Two step rule divide then subtract
def arch_12_two_step_rule_divide_then_subtract(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 5])
    c = rng.randint(2, 6)
    ans_int = rng.randint(4, 10)
    quot = ans_int + c
    x = d * quot
    ans = str(ans_int)
    svg = _svg_flow_box(str(x), f"÷ {d}", f"- {c}", out_val="?")
    prompt = f"Determine the final output value:"
    sol = (
        f"**Step 1:** $${x} \\div {d} = {quot}$$\n\n"
        f"**Step 2:** $${quot} - {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_12_{rng.randint(100000, 999999)}",
        "subskill": "12_two_step_rule_divide_then_subtract",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_12",
        "hints": {"tier_1": f"Divide {x} by {d}.", "tier_2": f"Subtract {c} from {quot}.", "tier_3": ans},
        "misconception_tags": ["subtraction_arithmetic_slip"]
    }


# 13. Two step rule add then multiply brackets
def arch_13_two_step_rule_add_then_multiply_brackets(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 6)
    m = rng.randint(2, 5)
    x = rng.randint(3, 8)
    step1 = x + c
    ans = str(step1 * m)
    svg = _svg_flow_box(str(x), f"+ {c}", f"× {m}", out_val="?")
    prompt = (
        f"Calculate the output \\(y\\) for the flow diagram:\n\n"
        f"Notice that addition occurs **before** multiplication."
    )
    sol = (
        f"**Step 1:** First add {c} to input {x}:\n$${x} + {c} = {step1}$$\n\n"
        f"**Step 2:** Multiply the result by {m}:\n$${step1} \\times {m} = \\mathbf{{{ans}}}$$\n\n"
        f"*(Algebraic form: \\(y = {m}(x + {c})\\))*"
    )
    return {
        "id": f"g7_fn1_13_{rng.randint(100000, 999999)}",
        "subskill": "13_two_step_rule_add_then_multiply_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_13",
        "hints": {"tier_1": f"Add {c} to {x} first.", "tier_2": f"Multiply {step1} by {m}.", "tier_3": ans},
        "misconception_tags": ["ignoring_operator_sequence_in_flow_diagram"]
    }


# 14. Two step rule subtract then multiply brackets
def arch_14_two_step_rule_subtract_then_multiply_brackets(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(1, 4)
    m = rng.randint(3, 6)
    x = rng.randint(6, 12)
    step1 = x - c
    ans = str(step1 * m)
    svg = _svg_flow_box(str(x), f"- {c}", f"× {m}", out_val="?")
    prompt = f"Find the output value \\(y\\):"
    sol = (
        f"**Step 1:** Subtract {c} from {x}:\n$${x} - {c} = {step1}$$\n\n"
        f"**Step 2:** Multiply the result by {m}:\n$${step1} \\times {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_14_{rng.randint(100000, 999999)}",
        "subskill": "14_two_step_rule_subtract_then_multiply_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_14",
        "hints": {"tier_1": f"Subtract {c} from {x}.", "tier_2": f"Multiply {step1} by {m}.", "tier_3": ans},
        "misconception_tags": ["multiplying_before_subtracting"]
    }


# 15. Two step reverse multiply add to input
def arch_15_two_step_reverse_multiply_add_to_input(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 5])
    c = rng.randint(4, 9)
    inp_val = rng.randint(4, 9)
    out_val = inp_val * m + c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"× {m}", f"+ {c}", out_val=str(out_val))
    prompt = (
        f"Solve for the input \\(x\\) using inverse operations:"
    )
    sol = (
        f"**Step 1:** Reverse the last operation first. The inverse of \\(+ {c}\\) is \\(- {c}\\):\n"
        f"$${out_val} - {c} = {inp_val * m}$$\n\n"
        f"**Step 2:** Reverse the first operation. The inverse of \\(\\times {m}\\) is \\(\\div {m}\\):\n"
        f"$$x = {inp_val * m} \\div {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_15_{rng.randint(100000, 999999)}",
        "subskill": "15_two_step_reverse_multiply_add_to_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_15",
        "hints": {
            "tier_1": f"Reverse order of operations: subtract {c} from {out_val} first.",
            "tier_2": f"Then divide {out_val - c} by {m}.",
            "tier_3": ans
        },
        "misconception_tags": ["dividing_before_subtracting_in_reverse"]
    }


# 16. Two step reverse multiply subtract to input
def arch_16_two_step_reverse_multiply_subtract_to_input(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 6])
    c = rng.randint(5, 11)
    inp_val = rng.randint(3, 8)
    out_val = inp_val * m - c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"× {m}", f"- {c}", out_val=str(out_val))
    prompt = f"Determine the input value \\(x\\):"
    sol = (
        f"**Step 1:** Reverse the subtraction by adding {c}:\n"
        f"$${out_val} + {c} = {inp_val * m}$$\n\n"
        f"**Step 2:** Reverse the multiplication by dividing by {m}:\n"
        f"$$x = {inp_val * m} \\div {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_16_{rng.randint(100000, 999999)}",
        "subskill": "16_two_step_reverse_multiply_subtract_to_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_16",
        "hints": {"tier_1": f"Add {c} to {out_val}.", "tier_2": f"Divide by {m}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_two_step_reverse"]
    }


# 17. Two step reverse divide add to input
def arch_17_two_step_reverse_divide_add_to_input(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([2, 4])
    c = rng.randint(3, 7)
    quot = rng.randint(3, 7)
    out_val = quot + c
    inp_val = quot * d
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"÷ {d}", f"+ {c}", out_val=str(out_val))
    prompt = f"Find the value of input \\(x\\):"
    sol = (
        f"**Step 1:** Subtract {c} from {out_val}:\n$${out_val} - {c} = {quot}$$\n\n"
        f"**Step 2:** Multiply by {d}:\n$$x = {quot} \\times {d} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_17_{rng.randint(100000, 999999)}",
        "subskill": "17_two_step_reverse_divide_add_to_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_17",
        "hints": {"tier_1": f"Subtract {c} from {out_val}.", "tier_2": f"Multiply by {d}.", "tier_3": ans},
        "misconception_tags": ["dividing_instead_of_multiplying"]
    }


# 18. Two step reverse brackets rule to input
def arch_18_two_step_reverse_brackets_rule_to_input(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(3, 7)
    m = rng.choice([2, 3, 4])
    inp_val = rng.randint(4, 9)
    step1 = inp_val + c
    out_val = step1 * m
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"+ {c}", f"× {m}", out_val=str(out_val))
    prompt = (
        f"In the flow diagram, find the input \\(x\\):"
    )
    sol = (
        f"**Step 1:** The last operation was \\(\\times {m}\\). Reverse it by dividing by {m}:\n"
        f"$${out_val} \\div {m} = {step1}$$\n\n"
        f"**Step 2:** The first operation was \\(+ {c}\\). Reverse it by subtracting {c}:\n"
        f"$$x = {step1} - {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_18_{rng.randint(100000, 999999)}",
        "subskill": "18_two_step_reverse_brackets_rule_to_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_18",
        "hints": {"tier_1": f"Divide {out_val} by {m} first.", "tier_2": f"Subtract {c} from {step1}.", "tier_3": ans},
        "misconception_tags": ["reversing_operations_in_wrong_order"]
    }


# 19. Identify operator in single step diagram
def arch_19_identify_operator_in_single_step_diagram(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(4, 9)
    m = rng.randint(4, 9)
    out_val = x * m
    ans = f"× {m}"
    svg = _svg_flow_box(str(x), "[ ? ]", out_val=str(out_val))
    prompt = (
        f"A number machine takes input {x} and produces output {out_val}:\n\n"
        f"State the single mathematical operation (e.g. \"+ 5\", \"× 6\") inside the box."
    )
    sol = (
        f"**Step 1:** Compare {x} and {out_val}.\n"
        f"Since $${x} \\times {m} = {out_val}$$, the operation is **$\\times {m}$**."
    )
    return {
        "id": f"g7_fn1_19_{rng.randint(100000, 999999)}",
        "subskill": "19_identify_operator_in_single_step_diagram",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_19",
        "hints": {"tier_1": f"How do you get from {x} to {out_val} using multiplication?", "tier_2": f"{out_val} / {x} = {m}", "tier_3": ans},
        "misconception_tags": ["confusing_addition_with_multiplication_in_rule"]
    }


# 20. Identify second operator given first
def arch_20_identify_second_operator_given_first(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.randint(3, 9)
    x = rng.randint(4, 8)
    out_val = x * m + c
    ans = f"+ {c}"
    svg = _svg_flow_box(str(x), f"× {m}", "[ ? ]", out_val=str(out_val))
    prompt = (
        f"In the flow diagram below, input {x} is multiplied by {m}, then an unknown operation is applied "
        f"to give {out_val}:\n\n"
        f"Find the missing second operation."
    )
    step1 = x * m
    sol = (
        f"**Step 1:** Calculate after first operation:\n$${x} \\times {m} = {step1}$$\n\n"
        f"**Step 2:** Determine what operation transforms {step1} into {out_val}:\n"
        f"$${out_val} - {step1} = {c}$$\n\n"
        f"Therefore, the second operation is **$+ {c}$**."
    )
    return {
        "id": f"g7_fn1_20_{rng.randint(100000, 999999)}",
        "subskill": "20_identify_second_operator_given_first",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_20",
        "hints": {"tier_1": f"First step is {x} * {m} = {step1}.", "tier_2": f"What must be added to {step1} to get {out_val}?", "tier_3": ans},
        "misconception_tags": ["arithmetic_subtraction_error"]
    }


# 21. Equivalent flow diagrams order of operations
def arch_21_equivalent_flow_diagrams_order_of_operations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider two different flow diagrams for an input \\(x = 6\\):\n\n"
        "- **Machine A:** \\(x \\longrightarrow [\\times 2] \\longrightarrow [+ 6] \\longrightarrow y\\)\n"
        "- **Machine B:** \\(x \\longrightarrow [+ 3] \\longrightarrow [\\times 2] \\longrightarrow y\\)\n\n"
        "Calculate the output \\(y\\) for both machines and explain why they produce the same result."
    )
    sol = (
        "**Step 1: Machine A:**\n"
        "$$6 \\times 2 = 12 \\implies 12 + 6 = 18$$\n\n"
        "**Step 2: Machine B:**\n"
        "$$6 + 3 = 9 \\implies 9 \\times 2 = 18$$\n\n"
        "**Step 3: Explanation:**\n"
        "Machine B computes $$2(x + 3)$$. By the distributive property: $$2(x + 3) = 2x + 6$$, "
        "which is identical to Machine A."
    )
    ans = "18"
    return {
        "id": f"g7_fn1_21_{rng.randint(100000, 999999)}",
        "subskill": "21_equivalent_flow_diagrams_order_of_operations",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn1_21",
        "hints": {"tier_1": "Calculate A: (6 * 2) + 6.", "tier_2": "Calculate B: (6 + 3) * 2.", "tier_3": ans},
        "misconception_tags": ["distributive_law_misconception"]
    }


# 22. Distributive property in flow diagrams
def arch_22_distributive_property_in_flow_diagrams(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner claims that the rule \\(y = 3(x + 4)\\) can be represented by the flow sequence:\n"
        "\\[ x \\longrightarrow [\\times 3] \\longrightarrow [+ 4] \\longrightarrow y \\]\n\n"
        "Is the learner correct? Explain why or why not, and provide the correct flow sequence."
    )
    sol = (
        "**Step 1:** Analyze the algebraic expression \\(y = 3(x + 4)\\):\n"
        "The brackets indicate that 4 is added to \\(x\\) **first**, and the entire sum is then multiplied by 3.\n\n"
        "**Step 2:** Critique the learner's diagram:\n"
        "The learner's sequence calculates $$3x + 4$$, which is **not** equal to $$3(x + 4) = 3x + 12$$.\n\n"
        "**Step 3: Correct flow sequence:**\n"
        "\\[ x \\longrightarrow [+ 4] \\longrightarrow [\\times 3] \\longrightarrow y \\]"
    )
    ans = "No, the correct sequence is add 4 then multiply by 3"
    return {
        "id": f"g7_fn1_22_{rng.randint(100000, 999999)}",
        "subskill": "22_distributive_property_in_flow_diagrams",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_22",
        "hints": {"tier_1": "Does the bracket mean add first or multiply first?", "tier_2": "Add 4 first, then multiply by 3.", "tier_3": ans},
        "misconception_tags": ["ignoring_brackets_in_flow_chains"]
    }


# 23. Integer flow diagram negative input
def arch_23_integer_flow_diagram_negative_input(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([-3, -4, -5, -6, -7])
    m = rng.choice([2, 3, 4])
    c = rng.randint(4, 9)
    step1 = x * m
    ans = str(step1 + c)
    svg = _svg_flow_box(str(x), f"× {m}", f"+ {c}", out_val="?")
    prompt = f"Calculate the output \\(y\\) when the input is a negative integer \\(x = {x}\\):"
    sol = (
        f"**Step 1:** Multiply negative input by {m}:\n$$({x}) \\times {m} = {step1}$$\n\n"
        f"**Step 2:** Add {c}:\n$${step1} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_23_{rng.randint(100000, 999999)}",
        "subskill": "23_integer_flow_diagram_negative_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_23",
        "hints": {"tier_1": "A negative times a positive is negative.", "tier_2": f"{step1} + {c} = {ans}.", "tier_3": ans},
        "misconception_tags": ["negative_integer_multiplication_sign_error"]
    }


# 24. Integer flow diagram negative multiplier
def arch_24_integer_flow_diagram_negative_multiplier(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(4, 9)
    m = rng.choice([-2, -3, -4])
    c = rng.randint(5, 12)
    step1 = x * m
    ans = str(step1 + c)
    svg = _svg_flow_box(str(x), f"× ({m})", f"+ {c}", out_val="?")
    prompt = f"Determine the output \\(y\\) for this integer flow diagram:"
    sol = (
        f"**Step 1:** Multiply {x} by {m}:\n$${x} \\times ({m}) = {step1}$$\n\n"
        f"**Step 2:** Add {c}:\n$${step1} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_24_{rng.randint(100000, 999999)}",
        "subskill": "24_integer_flow_diagram_negative_multiplier",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_24",
        "hints": {"tier_1": f"{x} * ({m}) = {step1}.", "tier_2": f"{step1} + {c}.", "tier_3": ans},
        "misconception_tags": ["sign_rule_addition_negative_integers"]
    }


# 25. Integer flow diagram negative output to input
def arch_25_integer_flow_diagram_negative_output_to_input(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    c = rng.randint(3, 8)
    inp_val = rng.choice([-4, -5, -6, -7])
    out_val = inp_val * m + c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"× {m}", f"+ {c}", out_val=str(out_val))
    prompt = (
        f"Find the integer input \\(x\\) for the flow diagram:"
    )
    sol = (
        f"**Step 1:** Reverse \\(+ {c}\\) by subtracting {c} from output {out_val}:\n"
        f"$${out_val} - {c} = {inp_val * m}$$\n\n"
        f"**Step 2:** Reverse \\(\\times {m}\\) by dividing by {m}:\n"
        f"$$x = \\frac{{{inp_val * m}}}{{{m}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_25_{rng.randint(100000, 999999)}",
        "subskill": "25_integer_flow_diagram_negative_output_to_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "learning_objective_id": "math_g7_fn1_25",
        "hints": {"tier_1": f"{out_val} - {c} = {inp_val * m}.", "tier_2": f"{inp_val * m} / {m}.", "tier_3": ans},
        "misconception_tags": ["subtracting_from_negative_number_sign_confusion"]
    }
