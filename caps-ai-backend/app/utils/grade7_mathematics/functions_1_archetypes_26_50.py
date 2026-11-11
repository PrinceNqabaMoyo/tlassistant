"""Grade 7 Mathematics - Functions and Relationships 1: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 1.md
Focus: Fractions/decimals in flow diagrams, verbal descriptions to operators, formula extraction, practical contexts, squares, and flow autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from .functions_1_archetypes_01_25 import _svg_flow_box


# 26. Fraction input flow diagram multiplication
def arch_26_fraction_input_flow_diagram_multiplication(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([8, 12, 16, 20])
    ans_val = (3 * mult) // 4
    ans = str(ans_val)
    svg = _svg_flow_box("3/4", f"× {mult}", out_val="?")
    prompt = (
        f"In the flow diagram below, the input is a common fraction \\(\\frac{{3}}{{4}}\\):\n\n"
        f"Calculate the resulting output."
    )
    sol = (
        f"**Step 1:** Multiply the fraction by {mult}:\n"
        f"$$\\frac{{3}}{{4}} \\times {mult} = \\frac{{3 \\times {mult}}}{{4}} = \\frac{{{3 * mult}}}{{4}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_26_{rng.randint(100000, 999999)}",
        "subskill": "26_fraction_input_flow_diagram_multiplication",
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
        "learning_objective_id": "math_g7_fn1_26",
        "hints": {"tier_1": f"Multiply 3 by {mult}, then divide by 4.", "tier_2": f"{3 * mult} / 4 = {ans}.", "tier_3": ans},
        "misconception_tags": ["fraction_multiplication_error"]
    }


# 27. Fraction operator flow diagram one half
def arch_27_fraction_operator_flow_diagram_one_half(rng: random.Random) -> Dict[str, Any]:
    x = rng.choice([12, 16, 18, 22, 26])
    c = rng.randint(2, 7)
    ans = str(x // 2 + c)
    svg = _svg_flow_box(str(x), "× 1/2", f"+ {c}", out_val="?")
    prompt = (
        f"Calculate the output \\(y\\) for this two-step flow diagram with fractional operator:"
    )
    sol = (
        f"**Step 1:** Multiply {x} by \\(\\frac{{1}}{{2}}\\) (halving {x}):\n"
        f"$${x} \\times \\frac{{1}}{{2}} = {x // 2}$$\n\n"
        f"**Step 2:** Add {c}:\n"
        f"$${x // 2} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_27_{rng.randint(100000, 999999)}",
        "subskill": "27_fraction_operator_flow_diagram_one_half",
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
        "learning_objective_id": "math_g7_fn1_27",
        "hints": {"tier_1": f"Half of {x} is {x // 2}.", "tier_2": f"{x // 2} + {c}.", "tier_3": ans},
        "misconception_tags": ["multiplying_fraction_misconception"]
    }


# 28. Decimal input flow diagram addition
def arch_28_decimal_input_flow_diagram_addition(rng: random.Random) -> Dict[str, Any]:
    a_tenths = rng.choice([32, 42, 54, 61])
    b_tenths = rng.choice([15, 23, 33, 45])
    sum_tenths = a_tenths + b_tenths
    a_str = f"{a_tenths // 10},{a_tenths % 10}"
    b_str = f"{b_tenths // 10},{b_tenths % 10}"
    ans = f"{sum_tenths // 10},{sum_tenths % 10}"
    svg = _svg_flow_box(a_str, f"+ {b_str}", out_val="?")
    prompt = (
        f"Determine the decimal output for the flow diagram:"
    )
    sol = (
        f"**Step 1:** Add the decimal numbers:\n"
        f"$${a_str} + {b_str} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_28_{rng.randint(100000, 999999)}",
        "subskill": "28_decimal_input_flow_diagram_addition",
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
        "learning_objective_id": "math_g7_fn1_28",
        "hints": {"tier_1": "Add tenths to tenths, units to units.", "tier_2": f"{a_str} + {b_str}.", "tier_3": ans},
        "misconception_tags": ["decimal_addition_alignment"]
    }


# 29. Decimal operator flow diagram multiply ten
def arch_29_decimal_operator_flow_diagram_multiply_ten(rng: random.Random) -> Dict[str, Any]:
    val = rng.choice([24, 34, 47, 58, 63, 79])
    inp_str = f"{val // 10},{val % 10}"
    ans = str(val)
    svg = _svg_flow_box(inp_str, "× 10", out_val="?")
    prompt = (
        f"Calculate the output \\(y\\) for the flow diagram:"
    )
    sol = (
        f"**Step 1:** Multiplying a decimal by 10 moves the decimal comma 1 place to the right:\n"
        f"$${inp_str} \\times 10 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_29_{rng.randint(100000, 999999)}",
        "subskill": "29_decimal_operator_flow_diagram_multiply_ten",
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
        "learning_objective_id": "math_g7_fn1_29",
        "hints": {"tier_1": "Shift the comma 1 place right.", "tier_2": f"{inp_str} * 10 = {ans}.", "tier_3": ans},
        "misconception_tags": ["decimal_comma_shift_direction"]
    }


# 30. Flow diagram with three sequential inputs
def arch_30_flow_diagram_with_three_sequential_inputs(rng: random.Random) -> Dict[str, Any]:
    # Rule: 3x - 1 for inputs 2, 5, 8 -> outputs 5, 14, 23
    inputs = [2, 5, 8]
    outputs = [3 * x - 1 for x in inputs]
    ans = f"{outputs[0]}, {outputs[1]}, {outputs[2]}"
    prompt = (
        f"A flow diagram applies the rule: multiply by 3, then subtract 1.\n\n"
        f"Calculate the three output values for the inputs **2, 5, and 8**."
    )
    sol = (
        f"**Step 1:** For \\(x = 2\\): $$2 \\times 3 - 1 = 6 - 1 = \\mathbf{{{outputs[0]}}}$$\n\n"
        f"**Step 2:** For \\(x = 5\\): $$5 \\times 3 - 1 = 15 - 1 = \\mathbf{{{outputs[1]}}}$$\n\n"
        f"**Step 3:** For \\(x = 8\\): $$8 \\times 3 - 1 = 24 - 1 = \\mathbf{{{outputs[2]}}}$$"
    )
    return {
        "id": f"g7_fn1_30_{rng.randint(100000, 999999)}",
        "subskill": "30_flow_diagram_with_three_sequential_inputs",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn1_30",
        "hints": {"tier_1": "Apply 3x - 1 to each input separately.", "tier_2": "Outputs are 5, 14, 23.", "tier_3": ans},
        "misconception_tags": ["batch_input_confusion"]
    }


# 31. Flow diagram with three sequential outputs
def arch_31_flow_diagram_with_three_sequential_outputs(rng: random.Random) -> Dict[str, Any]:
    # Rule: * 2 + 5. Outputs: 11, 17, 25 -> inputs: (11-5)/2=3, (17-5)/2=6, (25-5)/2=10
    outputs = [11, 17, 25]
    inputs = [(y - 5) // 2 for y in outputs]
    ans = f"{inputs[0]}, {inputs[1]}, {inputs[2]}"
    prompt = (
        f"A function machine has the rule: **multiply by 2, then add 5**.\n\n"
        f"Use inverse operations to find the inputs that produced outputs **11, 17, and 25**."
    )
    sol = (
        f"**Inverse rule:** Subtract 5, then divide by 2.\n\n"
        f"- For 11: $$(11 - 5) \\div 2 = 6 \\div 2 = \\mathbf{{{inputs[0]}}}$$\n"
        f"- For 17: $$(17 - 5) \\div 2 = 12 \\div 2 = \\mathbf{{{inputs[1]}}}$$\n"
        f"- For 25: $$(25 - 5) \\div 2 = 20 \\div 2 = \\mathbf{{{inputs[2]}}}$$"
    )
    return {
        "id": f"g7_fn1_31_{rng.randint(100000, 999999)}",
        "subskill": "31_flow_diagram_with_three_sequential_outputs",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn1_31",
        "hints": {"tier_1": "Subtract 5 then divide by 2 for each output.", "tier_2": "Inputs are 3, 6, 10.", "tier_3": ans},
        "misconception_tags": ["batch_inverse_error"]
    }


# 32. Flow diagram matching rule in words
def arch_32_flow_diagram_matching_rule_in_words(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(4, 9)
    svg = _svg_flow_box("x", f"× {m}", f"- {c}", out_val="y")
    prompt = (
        f"Consider the flow diagram:\n"
        f"\\[ x \\longrightarrow [\\times {m}] \\longrightarrow [- {c}] \\longrightarrow y \\]\n\n"
        f"State the rule in words describing how \\(y\\) is obtained from \\(x\\)."
    )
    sol = (
        f"**Rule in words:**\n"
        f"\"Multiply the input by {m}, then subtract {c} from the result to get the output.\""
    )
    ans = f"Multiply by {m}, then subtract {c}"
    return {
        "id": f"g7_fn1_32_{rng.randint(100000, 999999)}",
        "subskill": "32_flow_diagram_matching_rule_in_words",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn1_32",
        "hints": {"tier_1": "Read the operation boxes from left to right.", "tier_2": f"Multiply by {m}, then subtract {c}.", "tier_3": ans},
        "misconception_tags": ["verbalizing_operations_in_reverse"]
    }


# 33. Flow diagram translating words to operators
def arch_33_flow_diagram_translating_words_to_operators(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Translate the following instruction into a two-step flow diagram sequence:\n\n"
        "\"*Take any number, divide it by 3, and then add 8 to the quotient.*\"\n\n"
        "Write the operators that belong in Box 1 and Box 2."
    )
    sol = (
        "**Box 1:** \\(\\div 3\\)\n\n"
        "**Box 2:** \\(+ 8\\)\n\n"
        "Sequence: \\[ x \\longrightarrow [\\div 3] \\longrightarrow [+ 8] \\longrightarrow y \\]"
    )
    ans = "÷ 3, + 8"
    return {
        "id": f"g7_fn1_33_{rng.randint(100000, 999999)}",
        "subskill": "33_flow_diagram_translating_words_to_operators",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_33",
        "hints": {"tier_1": "First step is divide by 3.", "tier_2": "Second step is add 8.", "tier_3": ans},
        "misconception_tags": ["word_problem_operation_transposition"]
    }


# 34. Flow diagram writing algebraic formula
def arch_34_flow_diagram_writing_algebraic_formula(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A flow diagram takes input \\(x\\), applies \\([\\times 5]\\), then \\([+ 2]\\) to give output \\(y\\).\n\n"
        "Write down the algebraic formula for \\(y\\) in terms of \\(x\\)."
    )
    sol = (
        "**Step 1:** Multiplying \\(x\\) by 5 gives \\(5x\\).\n\n"
        "**Step 2:** Adding 2 gives \\(5x + 2\\).\n\n"
        "**Formula:**\n"
        "$$y = 5x + 2$$"
    )
    ans = "y = 5x + 2"
    return {
        "id": f"g7_fn1_34_{rng.randint(100000, 999999)}",
        "subskill": "34_flow_diagram_writing_algebraic_formula",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_34",
        "hints": {"tier_1": "Combine 5 times x with + 2.", "tier_2": "y = 5x + 2.", "tier_3": ans},
        "misconception_tags": ["writing_formula_without_variable"]
    }


# 35. Flow diagram evaluating zero input
def arch_35_flow_diagram_evaluating_zero_input(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(4, 9)
    c = rng.randint(5, 14)
    ans = str(c)
    svg = _svg_flow_box("0", f"× {m}", f"+ {c}", out_val="?")
    prompt = (
        f"Calculate the output \\(y\\) when the input is zero (\\(x = 0\\)):"
    )
    sol = (
        f"**Step 1:** Multiply 0 by {m}:\n"
        f"$$0 \\times {m} = 0$$\n\n"
        f"**Step 2:** Add {c}:\n"
        f"$$0 + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_35_{rng.randint(100000, 999999)}",
        "subskill": "35_flow_diagram_evaluating_zero_input",
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
        "learning_objective_id": "math_g7_fn1_35",
        "hints": {"tier_1": "0 times anything is 0.", "tier_2": f"0 + {c} = {c}.", "tier_3": ans},
        "misconception_tags": ["zero_multiplication_property_error"]
    }


# 36. Flow diagram evaluating fractional output
def arch_36_flow_diagram_evaluating_fractional_output(rng: random.Random) -> Dict[str, Any]:
    # Input 5, op: * 2 + 1 -> 11, then / 4 -> 11/4 = 2 3/4
    ans = "11/4"
    prompt = (
        "A flow diagram executes: input \\(5 \\longrightarrow [\\times 2] \\longrightarrow [+ 1] \\longrightarrow [\\div 4] \\longrightarrow y\\).\n\n"
        "Determine the output \\(y\\) as an improper fraction in simplest form."
    )
    sol = (
        "**Step 1:** $$5 \\times 2 = 10$$\n\n"
        "**Step 2:** $$10 + 1 = 11$$\n\n"
        "**Step 3:** $$11 \\div 4 = \\mathbf{\\frac{11}{4}} \\quad (\\text{or } 2\\frac{3}{4})$$"
    )
    return {
        "id": f"g7_fn1_36_{rng.randint(100000, 999999)}",
        "subskill": "36_flow_diagram_evaluating_fractional_output",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_36",
        "hints": {"tier_1": "5 * 2 + 1 = 11.", "tier_2": "11 / 4.", "tier_3": ans},
        "misconception_tags": ["fractional_division_simplification"]
    }


# 37. Flow diagram inverse machine complete reversal
def arch_37_flow_diagram_inverse_machine_complete_reversal(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The forward machine is: \\[ x \\longrightarrow [\\times 3] \\longrightarrow [- 5] \\longrightarrow y \\]\n\n"
        "Draw or write the complete **inverse machine** that takes \\(y\\) as input and outputs \\(x\\)."
    )
    sol = (
        "**Step 1:** Reverse the order of operations and invert each operation:\n"
        "- The last operation was \\([- 5]\\); its inverse is \\([+ 5]\\).\n"
        "- The first operation was \\([\\times 3]\\); its inverse is \\([\\div 3]\\).\n\n"
        "**Inverse Machine:**\n"
        "\\[ y \\longrightarrow [+ 5] \\longrightarrow [\\div 3] \\longrightarrow x \\]"
    )
    ans = "+ 5 then ÷ 3"
    return {
        "id": f"g7_fn1_37_{rng.randint(100000, 999999)}",
        "subskill": "37_flow_diagram_inverse_machine_complete_reversal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_37",
        "hints": {"tier_1": "Reverse the operations and their sequence.", "tier_2": "First + 5, then ÷ 3.", "tier_3": ans},
        "misconception_tags": ["inverting_operations_without_reversing_order"]
    }


# 38. Flow diagram detecting calculation error
def arch_38_flow_diagram_detecting_calculation_error(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(3, 6)
    c = rng.randint(2, 5)
    m = rng.choice([4, 5, 6])
    wrong_ans = x_val + c * m
    ans = str((x_val + c) * m)
    svg = _svg_flow_box(str(x_val), f"+ {c}", f"× {m}", out_val="y")
    prompt = (
        f"A learner processes \\(x = {x_val}\\) through the diagram: \\[ x \\longrightarrow [+ {c}] \\longrightarrow [\\times {m}] \\longrightarrow y \\]\n"
        f"The learner calculates: $${x_val} + {c} \\times {m} = {x_val} + {c * m} = {wrong_ans}$$.\n\n"
        f"Identify the learner's error and state the correct output \\(y\\)."
    )
    sol = (
        "**Step 1: Identify error:**\n"
        "In a flow diagram, operations must be performed in the sequential order of the arrows. "
        "The learner applied BODMAS to a flat written expression instead of completing the addition first.\n\n"
        "**Step 2: Correct calculation:**\n"
        f"$$\\text{{First step: }} {x_val} + {c} = {x_val + c}$$\n"
        f"$$\\text{{Second step: }} {x_val + c} \\times {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_38_{rng.randint(100000, 999999)}",
        "subskill": "38_flow_diagram_detecting_calculation_error",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_38",
        "hints": {"tier_1": f"Calculate ({x_val} + {c}) * {m}.", "tier_2": f"{x_val + c} * {m} = {ans}.", "tier_3": ans},
        "misconception_tags": ["flattening_flow_diagram_without_brackets"]
    }


# 39. Flow diagram comparing two different rules for same input
def arch_39_flow_diagram_comparing_two_different_rules_for_same_input(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Input \\(x = 10\\) is fed into two machines:\n"
        "- Machine P: \\(y = 2x + 15\\)\n"
        "- Machine Q: \\(y = 4x - 3\\)\n\n"
        "Which machine produces the greater output value? Show calculations for both."
    )
    sol = (
        "**Step 1: Machine P:**\n"
        "$$y = 2(10) + 15 = 20 + 15 = 35$$\n\n"
        "**Step 2: Machine Q:**\n"
        "$$y = 4(10) - 3 = 40 - 3 = 37$$\n\n"
        "**Step 3: Conclusion:**\n"
        "**Machine Q** produces the greater output (37 vs 35)."
    )
    ans = "Machine Q"
    return {
        "id": f"g7_fn1_39_{rng.randint(100000, 999999)}",
        "subskill": "39_flow_diagram_comparing_two_different_rules_for_same_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn1_39",
        "hints": {"tier_1": "Evaluate P(10) and Q(10).", "tier_2": "35 vs 37.", "tier_3": ans},
        "misconception_tags": ["arithmetic_substitution_slip"]
    }


# 40. Flow diagram identifying fixed point where input equals output
def arch_40_flow_diagram_identifying_fixed_point_where_input_equals_output(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the function machine rule: \\(y = 2x - 5\\).\n\n"
        "For what input value \\(x\\) does the input equal the output (i.e. \\(y = x\\))?"
    )
    sol = (
        "**Step 1:** Set \\(y = x\\):\n"
        "$$x = 2x - 5$$\n\n"
        "**Step 2:** Solve for \\(x\\):\n"
        "$$5 = 2x - x$$\n"
        "$$x = \\mathbf{5}$$\n\n"
        "**Verification:** If \\(x = 5\\), then \\(y = 2(5) - 5 = 10 - 5 = 5\\)."
    )
    ans = "5"
    return {
        "id": f"g7_fn1_40_{rng.randint(100000, 999999)}",
        "subskill": "40_flow_diagram_identifying_fixed_point_where_input_equals_output",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_40",
        "hints": {"tier_1": "Set 2x - 5 = x.", "tier_2": "2x - x = 5.", "tier_3": ans},
        "misconception_tags": ["fixed_point_algebra_confusion"]
    }


# 41. Geometric context square perimeter flow diagram
def arch_41_geometric_context_square_perimeter_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(8, 19)
    ans = str(4 * s)
    svg = _svg_flow_box(f"s = {s}", "× 4", out_val="P = ?")
    prompt = (
        f"The perimeter \\(P\\) of a square with side length \\(s\\) is modeled by this flow diagram:\n\n"
        f"Calculate the perimeter when side length \\(s = {s}\\text{{ cm}}\\) and state the formula."
    )
    sol = (
        f"**Step 1:** Formula: \\(P = 4s\\)\n\n"
        f"**Step 2:** Calculation:\n"
        f"$$P = 4 \\times {s} = \\mathbf{{{ans}\\text{{ cm}}}}$"
    )
    return {
        "id": f"g7_fn1_41_{rng.randint(100000, 999999)}",
        "subskill": "41_geometric_context_square_perimeter_flow_diagram",
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
        "learning_objective_id": "math_g7_fn1_41",
        "hints": {"tier_1": "Multiply side length by 4.", "tier_2": f"4 * {s} = {ans}.", "tier_3": ans},
        "misconception_tags": ["confusing_perimeter_with_area_in_flow_diagram"]
    }


# 42. Geometric context cube faces flow diagram
def arch_42_geometric_context_cube_faces_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    n_cubes = rng.randint(5, 14)
    ans = str(6 * n_cubes)
    svg = _svg_flow_box(str(n_cubes), "× 6", out_val="?")
    prompt = (
        f"Each cube has 6 flat faces. A function machine calculates total faces for \\(n\\) separate cubes:\n\n"
        f"Calculate the total number of faces on {n_cubes} separate cubes."
    )
    sol = (
        f"**Step 1:** Apply operator: $${n_cubes} \\times 6 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_42_{rng.randint(100000, 999999)}",
        "subskill": "42_geometric_context_cube_faces_flow_diagram",
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
        "learning_objective_id": "math_g7_fn1_42",
        "hints": {"tier_1": f"Multiply {n_cubes} by 6.", "tier_2": f"{n_cubes} * 6 = {ans}.", "tier_3": ans},
        "misconception_tags": ["times_tables_slip"]
    }


# 43. Financial context taxi fare fixed plus per km flow
def arch_43_financial_context_taxi_fare_fixed_plus_per_km_flow(rng: random.Random) -> Dict[str, Any]:
    km = rng.randint(8, 22)
    ans = str(15 + 10 * km)
    svg = _svg_flow_box(f"{km} km", "× 10", "+ 15", out_val="R ?")
    prompt = (
        f"A metered taxi charges R15 base fee plus R10 per kilometer traveled:\n\n"
        f"Calculate the total fare for a trip of {km} km."
    )
    sol = (
        f"**Step 1:** Multiply km by rate per km:\n$${km} \\times 10 = {10 * km}$$\n\n"
        f"**Step 2:** Add fixed base fee:\n$${10 * km} + 15 = \\mathbf{{R{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_43_{rng.randint(100000, 999999)}",
        "subskill": "43_financial_context_taxi_fare_fixed_plus_per_km_flow",
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
        "learning_objective_id": "math_g7_fn1_43",
        "hints": {"tier_1": f"{km} * 10 = {10 * km}.", "tier_2": f"{10 * km} + 15.", "tier_3": ans},
        "misconception_tags": ["fixed_cost_added_before_variable"]
    }


# 44. Financial context hourly wage flow diagram
def arch_44_financial_context_hourly_wage_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    hours = rng.randint(5, 12)
    rate = rng.choice([40, 45, 50, 60])
    ans = str(hours * rate)
    svg = _svg_flow_box(f"{hours} h", f"× {rate}", out_val="R ?")
    prompt = (
        f"A student earns R{rate} per hour for part-time tutoring:\n\n"
        f"Determine total earnings for working {hours} hours."
    )
    sol = (
        f"**Step 1:** Total wage = $${hours} \\times {rate} = \\mathbf{{R{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_44_{rng.randint(100000, 999999)}",
        "subskill": "44_financial_context_hourly_wage_flow_diagram",
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
        "learning_objective_id": "math_g7_fn1_44",
        "hints": {"tier_1": f"{hours} * {rate}.", "tier_2": f"Earnings = R{ans}.", "tier_3": ans},
        "misconception_tags": ["rate_multiplication_error"]
    }


# 45. Financial context cellphone airtime flow diagram
def arch_45_financial_context_cellphone_airtime_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    # Initial airtime R50, calls cost R2 per minute -> balance = 50 - 2m
    m = 15
    ans = str(50 - 2 * m)
    prompt = (
        f"A prepaid phone starts with R50 of airtime. Calls cost R2 per minute.\n\n"
        f"Calculate the airtime balance remaining after making {m} minutes of calls."
    )
    sol = (
        f"**Step 1:** Cost of calls: $${m} \\times 2 = 30$$\n\n"
        f"**Step 2:** Remaining balance:\n$$50 - 30 = \\mathbf{{R{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_45_{rng.randint(100000, 999999)}",
        "subskill": "45_financial_context_cellphone_airtime_flow_diagram",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn1_45",
        "hints": {"tier_1": "15 * 2 = 30.", "tier_2": "50 - 30.", "tier_3": ans},
        "misconception_tags": ["adding_cost_to_balance_instead_of_subtracting"]
    }


# 46. Flow diagram with squared operator
def arch_46_flow_diagram_with_squared_operator(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(5, 13)
    ans = str(x ** 2)
    svg = _svg_flow_box(str(x), "( )²", out_val="?")
    prompt = (
        f"Calculate the output \\(y\\) for this squaring flow diagram:"
    )
    sol = (
        f"**Step 1:** Squaring means multiplying the number by itself:\n"
        f"$${x}^2 = {x} \\times {x} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_46_{rng.randint(100000, 999999)}",
        "subskill": "46_flow_diagram_with_squared_operator",
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
        "learning_objective_id": "math_g7_fn1_46",
        "hints": {"tier_1": f"Multiply {x} by itself.", "tier_2": f"{x} * {x}.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_2_instead_of_squaring"]
    }


# 47. Flow diagram square root operator
def arch_47_flow_diagram_square_root_operator(rng: random.Random) -> Dict[str, Any]:
    root = rng.randint(6, 15)
    sq = root ** 2
    ans = str(root)
    svg = _svg_flow_box(str(sq), "√", out_val="?")
    prompt = (
        f"Determine the output \\(y\\) for the square root machine:"
    )
    sol = (
        f"**Step 1:** The square root of {sq} is the positive number that multiplies by itself to give {sq}:\n"
        f"$$\\sqrt{{{sq}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_47_{rng.randint(100000, 999999)}",
        "subskill": "47_flow_diagram_square_root_operator",
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
        "learning_objective_id": "math_g7_fn1_47",
        "hints": {"tier_1": f"What number squared equals {sq}?", "tier_2": f"{root} * {root} = {sq}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_2_instead_of_square_root"]
    }


# 48. Flow diagram with consecutive multipliers factoring
def arch_48_flow_diagram_with_consecutive_multipliers_factoring(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the two-step flow diagram: \\[ x \\longrightarrow [\\times 2] \\longrightarrow [\\times 3] \\longrightarrow y \\]\n\n"
        "Replace the two separate multiplication boxes with a **single equivalent multiplication box**."
    )
    sol = (
        "**Step 1:** Combine successive factors by multiplication:\n"
        "$$2 \\times 3 = 6$$\n\n"
        "**Step 2:** Single equivalent operation:\n"
        "\\[ x \\longrightarrow [\\mathbf{\\times 6}] \\longrightarrow y \\]"
    )
    ans = "× 6"
    return {
        "id": f"g7_fn1_48_{rng.randint(100000, 999999)}",
        "subskill": "48_flow_diagram_with_consecutive_multipliers_factoring",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn1_48",
        "hints": {"tier_1": "Multiply the two operators: 2 * 3.", "tier_2": "× 6.", "tier_3": ans},
        "misconception_tags": ["adding_multipliers_instead_of_multiplying"]
    }


# 49. Flow diagram reverse with two step integers
def arch_49_flow_diagram_reverse_with_two_step_integers(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4])
    inp_val = rng.randint(2, 6)
    c = inp_val * m + rng.randint(1, 5)
    out_val = inp_val * m - c
    ans = str(inp_val)
    svg = _svg_flow_box("x", f"× {m}", f"- {c}", out_val=str(out_val))
    prompt = (
        f"Find the integer input \\(x\\) for the flow diagram:"
    )
    sol = (
        f"**Step 1:** Reverse \\(- {c}\\) by adding {c} to output \\({out_val}\\):\n"
        f"$${out_val} + {c} = {inp_val * m}$$\n\n"
        f"**Step 2:** Reverse \\(\\times {m}\\) by dividing {inp_val * m} by {m}:\n"
        f"$$x = {inp_val * m} \\div {m} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn1_49_{rng.randint(100000, 999999)}",
        "subskill": "49_flow_diagram_reverse_with_two_step_integers",
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
        "learning_objective_id": "math_g7_fn1_49",
        "hints": {"tier_1": f"{out_val} + {c} = {inp_val * m}.", "tier_2": f"{inp_val * m} / {m} = {ans}.", "tier_3": ans},
        "misconception_tags": ["integer_negative_addition_in_reverse"]
    }


# 50. Flow diagram multi branch input output autopsy
def arch_50_flow_diagram_multi_branch_input_output_autopsy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A function machine applies the rule \\(y = 3x - 4\\).\n\n"
        "Complete the following diagnostic autopsy:\n"
        "1. Calculate the output when \\(x = 6\\).\n"
        "2. Calculate the input that produces output \\(y = 23\\)."
    )
    sol = (
        "**Part 1: Forward calculation (\\(x = 6\\)):**\n"
        "$$y = 3(6) - 4 = 18 - 4 = \\mathbf{14}$$\n\n"
        "**Part 2: Inverse calculation (\\(y = 23\\)):**\n"
        "$$23 + 4 = 27$$\n"
        "$$x = 27 \\div 3 = \\mathbf{9}$$\n\n"
        "**Summary:** 1. \\(y = 14\\); 2. \\(x = 9\\)"
    )
    ans = "1. 14; 2. 9"
    return {
        "id": f"g7_fn1_50_{rng.randint(100000, 999999)}",
        "subskill": "50_flow_diagram_multi_branch_input_output_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn1_50",
        "hints": {"tier_1": "Part 1: 3(6) - 4; Part 2: (23 + 4) / 3.", "tier_2": "14 and 9.", "tier_3": ans},
        "misconception_tags": ["forward_inverse_dual_slip"]
    }
