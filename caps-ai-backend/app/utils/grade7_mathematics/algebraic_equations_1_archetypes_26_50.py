"""Grade 7 Mathematics - Algebraic Equations 1: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 1.md
Focus: Fractions, decimals, two-step division equations, word problems, SVG balance scales, negative integers, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_balance_scale(left_label: str, right_label: str) -> str:
    """Return clean 2D static SVG diagram of a balance scale in perfect equilibrium."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="220" style="background:#ffffff;">\n'
        f'  <defs>\n'
        f'    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">\n'
        f'      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e293b"/>\n'
        f'    </marker>\n'
        f'  </defs>\n'
        f'  <!-- Base and Fulcrum -->\n'
        f'  <line x1="150" y1="200" x2="310" y2="200" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>\n'
        f'  <polygon points="230,110 210,198 250,198" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Horizontal Pivot Beam -->\n'
        f'  <line x1="70" y1="110" x2="390" y2="110" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>\n'
        f'  <circle cx="230" cy="110" r="5" fill="#3b82f6"/>\n'
        f'  <!-- Left Pan Strings & Pan -->\n'
        f'  <line x1="90" y1="110" x2="60" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <line x1="90" y1="110" x2="120" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <path d="M 50 155 Q 90 170 130 155 Z" fill="#cbd5e1" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Left Pan Content -->\n'
        f'  <rect x="65" y="125" width="50" height="28" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
        f'  <text x="90" y="144" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{left_label}</text>\n'
        f'  <!-- Right Pan Strings & Pan -->\n'
        f'  <line x1="370" y1="110" x2="340" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <line x1="370" y1="110" x2="400" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <path d="M 330 155 Q 370 170 410 155 Z" fill="#cbd5e1" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Right Pan Content -->\n'
        f'  <rect x="345" y="125" width="50" height="28" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n'
        f'  <text x="370" y="144" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#92400e" text-anchor="middle">{right_label}</text>\n'
        f'  <text x="230" y="80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Balanced (=)</text>\n'
        f'</svg>'
    )


# 26. Fraction coefficient unit fraction
def arch_26_fraction_coefficient_unit_fraction(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([2, 3, 4, 5])
    rhs = rng.randint(4, 12)
    ans_val = denom * rhs
    ans = str(ans_val)
    prompt = (
        f"Solve the equation with a unit fraction coefficient:\n"
        f"\\[ \\frac{{1}}{{{denom}}}x = {rhs} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by the denominator {denom}:\n"
        f"$$x = {rhs} \\times {denom}$$\n\n"
        f"**Step 2:** Calculate: \\({rhs} \\times {denom} = {ans_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_26_{rng.randint(100000, 999999)}",
        "subskill": "26_fraction_coefficient_unit_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_26",
        "hints": {"tier_1": f"Multiply {rhs} by {denom}.", "tier_2": f"{rhs} × {denom} = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_denominator_instead_of_multiplying"]
    }


# 27. Fraction coefficient non unit fraction
def arch_27_fraction_coefficient_non_unit_fraction(rng: random.Random) -> Dict[str, Any]:
    # (3/4)x = 12 -> x = 12 * 4 / 3 = 16
    ans = "16"
    prompt = (
        "Solve the equation:\n"
        "\\[ \\frac{3}{4}x = 12 \\]"
    )
    sol = (
        "**Step 1:** Multiply both sides by 4 to clear the denominator:\n"
        "$$3x = 12 \\times 4 = 48$$\n\n"
        "**Step 2:** Divide both sides by 3:\n"
        "$$x = \\frac{48}{3} = \\mathbf{16}$$"
    )
    return {
        "id": f"g7_eq1_27_{rng.randint(100000, 999999)}",
        "subskill": "27_fraction_coefficient_non_unit_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_27",
        "hints": {"tier_1": "Multiply by 4, then divide by 3.", "tier_2": "3x = 48, so x = 16.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_numerator_and_dividing_by_denominator"]
    }


# 28. Decimal coefficient equation
def arch_28_decimal_coefficient_equation(rng: random.Random) -> Dict[str, Any]:
    coeff = 0.5
    rhs = rng.choice([8, 12, 14, 20])
    ans_val = int(rhs / coeff)
    ans = str(ans_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ 0{{,}}5x = {rhs} \\]"
    )
    sol = (
        f"**Step 1:** Dividing by \\(0{{,}}5\\) is equivalent to multiplying by 2:\n"
        f"$$x = \\frac{{{rhs}}}{{0{{,}}5}} = {rhs} \\times 2$$\n\n"
        f"**Step 2:** Calculate: \\({rhs} \\times 2 = {ans_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_28_{rng.randint(100000, 999999)}",
        "subskill": "28_decimal_coefficient_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_28",
        "hints": {"tier_1": "Dividing by 0,5 is the same as multiplying by 2.", "tier_2": f"{rhs} × 2 = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_decimal_misplacement"]
    }


# 29. Decimal addition equation
def arch_29_decimal_addition_equation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2.5, 3.4, 4.2, 5.1])
    b = round(a + rng.choice([3.1, 4.3, 5.2]), 1)
    ans_val = round(b - a, 1)
    ans = f"{ans_val}".replace(".", ",")
    prompt = (
        f"Solve the equation with decimals:\n"
        f"\\[ x + {str(a).replace('.', ',')} = {str(b).replace('.', ',')} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {str(a).replace('.', ',')} from both sides:\n"
        f"$$x = {str(b).replace('.', ',')} - {str(a).replace('.', ',')}$$\n\n"
        f"**Step 2:** Calculate: \\(x = \\mathbf{{{ans}}}\\)."
    )
    return {
        "id": f"g7_eq1_29_{rng.randint(100000, 999999)}",
        "subskill": "29_decimal_addition_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_29",
        "hints": {"tier_1": f"Subtract {a} from {b}.", "tier_2": f"{b} - {a} = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["decimal_subtraction_alignment_error"]
    }


# 30. Decimal subtraction equation
def arch_30_decimal_subtraction_equation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1.8, 2.4, 3.5])
    diff = rng.choice([3.2, 4.1, 5.3])
    tot = round(a + diff, 1)
    ans = f"{tot}".replace(".", ",")
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ x - {str(a).replace('.', ',')} = {str(diff).replace('.', ',')} \\]"
    )
    sol = (
        f"**Step 1:** Add {str(a).replace('.', ',')} to both sides:\n"
        f"$$x = {str(diff).replace('.', ',')} + {str(a).replace('.', ',')}$$\n\n"
        f"**Step 2:** Calculate: \\(x = \\mathbf{{{ans}}}\\)."
    )
    return {
        "id": f"g7_eq1_30_{rng.randint(100000, 999999)}",
        "subskill": "30_decimal_subtraction_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_30",
        "hints": {"tier_1": f"Add {a} to {diff}.", "tier_2": f"{diff} + {a} = {tot}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_decimal"]
    }


# 31. Two step division with addition
def arch_31_two_step_division_with_addition(rng: random.Random) -> Dict[str, Any]:
    denom = 3
    x_val = rng.choice([6, 9, 12, 15, 18])
    k = rng.randint(2, 6)
    rhs = (x_val // denom) + k
    ans = str(x_val)
    prompt = (
        f"Solve the two-step equation:\n"
        f"\\[ \\frac{{x}}{{{denom}}} + {k} = {rhs} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {k} from both sides:\n"
        f"$$\\frac{{x}}{{{denom}}} = {rhs} - {k} = {rhs - k}$$\n\n"
        f"**Step 2:** Multiply both sides by {denom}:\n"
        f"$$x = ({rhs - k}) \\times {denom} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_31_{rng.randint(100000, 999999)}",
        "subskill": "31_two_step_division_with_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_31",
        "hints": {"tier_1": f"First subtract {k} from {rhs}.", "tier_2": f"Then multiply by {denom}.", "tier_3": ans},
        "misconception_tags": ["multiplying_before_subtracting_constant"]
    }


# 32. Two step division with subtraction
def arch_32_two_step_division_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    denom = 2
    x_val = rng.choice([10, 14, 16, 20])
    k = rng.randint(2, 5)
    rhs = (x_val // denom) - k
    ans = str(x_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ \\frac{{x}}{{{denom}}} - {k} = {rhs} \\]"
    )
    sol = (
        f"**Step 1:** Add {k} to both sides:\n"
        f"$$\\frac{{x}}{{{denom}}} = {rhs} + {k} = {rhs + k}$$\n\n"
        f"**Step 2:** Multiply both sides by {denom}:\n"
        f"$$x = ({rhs + k}) \\times {denom} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_32_{rng.randint(100000, 999999)}",
        "subskill": "32_two_step_division_with_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_32",
        "hints": {"tier_1": f"First add {k} to {rhs}.", "tier_2": f"Then multiply by {denom}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_two_step_division"]
    }


# 33. Word problem money subtraction
def arch_33_word_problem_money_subtraction(rng: random.Random) -> Dict[str, Any]:
    total_m = rng.choice([50, 100, 200])
    left_m = rng.choice([15, 25, 45])
    spent = total_m - left_m
    ans = str(spent)
    prompt = (
        f"Thabo has R{total_m}. He purchases a school bag for R\\(x\\) and has R{left_m} remaining.\n\n"
        f"1. Write an algebraic equation representing this situation.\n"
        f"2. Solve for \\(x\\) to determine the cost of the school bag."
    )
    sol = (
        f"**Step 1:** Set up equation:\n"
        f"$$\\text{{R}}{total_m} - x = \\text{{R}}{left_m}$$\n\n"
        f"**Step 2:** Solve for \\(x\\):\n"
        f"$$x = {total_m} - {left_m} = \\mathbf{{{ans}}}\\text{{ rands}}$$"
    )
    return {
        "id": f"g7_eq1_33_{rng.randint(100000, 999999)}",
        "subskill": "33_word_problem_money_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_33",
        "hints": {"tier_1": f"50 - x = 15.", "tier_2": f"x = {total_m} - {left_m}.", "tier_3": ans},
        "misconception_tags": ["adding_money_left_to_total"]
    }


# 34. Word problem age addition
def arch_34_word_problem_age_addition(rng: random.Random) -> Dict[str, Any]:
    years_ahead = rng.randint(4, 8)
    future_age = rng.randint(16, 21)
    cur_age = future_age - years_ahead
    ans = str(cur_age)
    prompt = (
        f"Sisanda is currently \\(x\\) years old. In {years_ahead} years' time, she will be {future_age} years old.\n\n"
        f"1. Write an equation for her age.\n"
        f"2. Solve the equation to find her current age."
    )
    sol = (
        f"**Step 1:** Set up equation: \\(x + {years_ahead} = {future_age}\\).\n\n"
        f"**Step 2:** Solve for \\(x\\):\n"
        f"$$x = {future_age} - {years_ahead} = \\mathbf{{{ans}}}\\text{{ years old}}$$"
    )
    return {
        "id": f"g7_eq1_34_{rng.randint(100000, 999999)}",
        "subskill": "34_word_problem_age_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_34",
        "hints": {"tier_1": f"x + {years_ahead} = {future_age}.", "tier_2": f"x = {future_age} - {years_ahead}.", "tier_3": ans},
        "misconception_tags": ["adding_future_years_instead_of_subtracting"]
    }


# 35. Word problem temperature change
def arch_35_word_problem_temperature_change(rng: random.Random) -> Dict[str, Any]:
    rise = rng.randint(5, 10)
    final_temp = rng.randint(18, 28)
    orig_temp = final_temp - rise
    ans = str(orig_temp)
    prompt = (
        f"The temperature in Pretoria was \\(T^\\circ\\text{{C}}\\) at dawn. By midday, it rose by "
        f"{rise}^\\circ\\text{{C}} to reach {final_temp}^\\circ\\text{{C}}.\n\n"
        f"Write an equation and solve for the dawn temperature \\(T\\)."
    )
    sol = (
        f"**Step 1:** Set up the equation: \\(T + {rise} = {final_temp}\\).\n\n"
        f"**Step 2:** Solve for \\(T\\):\n"
        f"$$T = {final_temp} - {rise} = \\mathbf{{{ans}}}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_eq1_35_{rng.randint(100000, 999999)}",
        "subskill": "35_word_problem_temperature_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_35",
        "hints": {"tier_1": f"T + {rise} = {final_temp}.", "tier_2": f"{final_temp} - {rise} = {orig_temp}.", "tier_3": ans},
        "misconception_tags": ["temperature_change_direction_error"]
    }


# 36. Geometry perimeter rectangle equation
def arch_36_geometry_perimeter_rectangle_equation(rng: random.Random) -> Dict[str, Any]:
    # 2(x + 5) = 26 -> x + 5 = 13 -> x = 8
    ans = "8"
    prompt = (
        "The perimeter of a rectangle is \\(26\\text{ cm}\\).\n"
        "Its length is \\((x + 5)\\text{ cm}\\) and its width is \\(x\\text{ cm}\\).\n"
        "The perimeter equation simplifies to:\n"
        "\\[ 2(x + 5) + 2x = 26 \\implies 4x + 10 = 26 \\]\n\n"
        "Solve the equation to find \\(x\\)."
    )
    sol = (
        "**Step 1:** Subtract 10 from both sides:\n"
        "$$4x = 26 - 10 = 16$$\n\n"
        "**Step 2:** Divide both sides by 4:\n"
        "$$x = \\frac{16}{4} = \\mathbf{8}\\text{ cm}$$"
    )
    return {
        "id": f"g7_eq1_36_{rng.randint(100000, 999999)}",
        "subskill": "36_geometry_perimeter_rectangle_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_36",
        "hints": {"tier_1": "4x = 26 - 10.", "tier_2": "4x = 16, so x = 4.", "tier_3": ans},
        "misconception_tags": ["confusing_length_with_perimeter"]
    }


# 37. Geometry perimeter equilateral triangle
def arch_37_geometry_perimeter_equilateral_triangle(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(5, 14)
    p = 3 * s
    ans = str(s)
    prompt = (
        f"An equilateral triangle has perimeter \\({p}\\text{{ cm}}\\).\n"
        f"Since all three sides are equal to \\(x\\), the equation is \\(3x = {p}\\).\n\n"
        f"Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1:** Divide the perimeter by 3:\n"
        f"$$x = \\frac{{{p}}}{{3}} = \\mathbf{{{ans}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_eq1_37_{rng.randint(100000, 999999)}",
        "subskill": "37_geometry_perimeter_equilateral_triangle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_37",
        "hints": {"tier_1": f"Divide {p} by 3.", "tier_2": f"{p} / 3 = {s}.", "tier_3": ans},
        "misconception_tags": ["dividing_equilateral_perimeter_by_two"]
    }


# 38. Flow diagram to equation solve
def arch_38_flow_diagram_to_equation_solve(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3, 4, 5])
    c = rng.randint(2, 8)
    x_val = rng.randint(4, 12)
    out = m * x_val + c
    ans = str(x_val)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 90" width="100%" height="90" style="background:#ffffff;">'
        f'<text x="35" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Input x</text>'
        f'<line x1="65" y1="45" x2="105" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="105" y="25" width="70" height="40" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="140" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">× {m}</text>'
        f'<line x1="175" y1="45" x2="215" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="215" y="25" width="70" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="250" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">+ {c}</text>'
        f'<line x1="285" y1="45" x2="325" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="365" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Output {out}</text>'
        f'</svg>'
    )
    prompt = (
        f"A flow diagram applies the following rule:\n"
        f"$$\\text{{Input }} x \\xrightarrow{{\\times {m}}} \\boxed{{\\quad}} \\xrightarrow{{+ {c}}} \\mathbf{{{out}}}$$\n\n"
        f"1. Write an algebraic equation for this flow diagram.\n"
        f"2. Solve for the input \\(x\\) by working backwards."
    )
    sol = (
        f"**Step 1:** Equation: \\({m}x + {c} = {out}\\).\n\n"
        f"**Step 2:** Work backwards (undo operations in reverse order):\n"
        f"- Undo \\(+ {c}\\): \\({out} - {c} = {out - c}\\)\n"
        f"- Undo \\(\\times {m}\\): \\({out - c} \\div {m} = \\mathbf{{{ans}}}\\)\n\n"
        f"Input: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_38_{rng.randint(100000, 999999)}",
        "subskill": "38_flow_diagram_to_equation_solve",
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
        "learning_objective_id": "math_g7_eq1_38",
        "hints": {"tier_1": f"{m}x + {c} = {out}.", "tier_2": f"{out} - {c} = {out - c}, then divide by {m}.", "tier_3": ans},
        "misconception_tags": ["reversing_flow_operations_in_wrong_order"]
    }


# 39. Balance scale single unknown SVG
def arch_39_balance_scale_single_unknown_svg(rng: random.Random) -> Dict[str, Any]:
    w_left = rng.randint(3, 7)
    x_val = rng.randint(4, 10)
    w_right = x_val + w_left
    ans = str(x_val)
    svg = _svg_balance_scale(f"x + {w_left} kg", f"{w_right} kg")
    prompt = (
        "The balance scale shown below is in perfect equilibrium:\n\n"
        "1. Write down the algebraic equation represented by the balanced scale.\n"
        "2. Solve for the unknown mass \\(x\\)."
    )
    sol = (
        f"**Step 1:** Since the scale is balanced, Left Pan = Right Pan:\n"
        f"$$x + {w_left} = {w_right}$$\n\n"
        f"**Step 2:** Remove {w_left} kg from both pans:\n"
        f"$$x = {w_right} - {w_left} = \\mathbf{{{ans}}}\\text{{ kg}}$$"
    )
    return {
        "id": f"g7_eq1_39_{rng.randint(100000, 999999)}",
        "subskill": "39_balance_scale_single_unknown_svg",
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
        "learning_objective_id": "math_g7_eq1_39",
        "hints": {"tier_1": f"x + {w_left} = {w_right}.", "tier_2": f"x = {w_right} - {w_left}.", "tier_3": ans},
        "misconception_tags": ["adding_scale_weights_instead_of_balancing"]
    }


# 40. Balance scale multiple unknowns SVG
def arch_40_balance_scale_multiple_unknowns_svg(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([4, 5, 6, 7, 8, 9, 11])
    total_w = 2 * x_val
    ans = str(x_val)
    svg = _svg_balance_scale("2x kg", f"{total_w} kg")
    prompt = (
        "The balance scale below is in equilibrium:\n\n"
        "Write down the equation and determine the mass of one block \\(x\\)."
    )
    sol = (
        f"**Step 1:** Equation: \\(2x = {total_w}\\).\n\n"
        f"**Step 2:** Divide both sides by 2:\n"
        f"$$x = \\frac{{{total_w}}}{{2}} = \\mathbf{{{ans}}}\\text{{ kg}}$$"
    )
    return {
        "id": f"g7_eq1_40_{rng.randint(100000, 999999)}",
        "subskill": "40_balance_scale_multiple_unknowns_svg",
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
        "learning_objective_id": "math_g7_eq1_40",
        "hints": {"tier_1": f"2x = {total_w}.", "tier_2": f"Divide {total_w} by 2.", "tier_3": ans},
        "misconception_tags": ["subtracting_two_instead_of_dividing_in_scale"]
    }


# 41. Balance scale compound SVG
def arch_41_balance_scale_compound_svg(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([3, 4, 5, 6, 7])
    extra = rng.randint(2, 6)
    tot = 2 * x_val + extra
    ans = str(x_val)
    svg = _svg_balance_scale(f"2x + {extra} kg", f"{tot} kg")
    prompt = (
        "Inspect the balanced scale:\n\n"
        "Determine the mass of \\(x\\)."
    )
    sol = (
        f"**Step 1:** Equation: \\(2x + {extra} = {tot}\\).\n\n"
        f"**Step 2:** Subtract {extra} kg from both sides:\n"
        f"$$2x = {tot} - {extra} = {tot - extra}$$\n\n"
        f"**Step 3:** Divide by 2:\n"
        f"$$x = \\frac{{{tot - extra}}}{{2}} = \\mathbf{{{ans}}}\\text{{ kg}}$$"
    )
    return {
        "id": f"g7_eq1_41_{rng.randint(100000, 999999)}",
        "subskill": "41_balance_scale_compound_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_eq1_41",
        "hints": {"tier_1": f"First remove {extra} kg from both sides.", "tier_2": f"2x = {tot - extra}.", "tier_3": ans},
        "misconception_tags": ["dividing_before_removing_constant_weight"]
    }


# 42. Negative integer solution addition
def arch_42_negative_integer_solution_addition(rng: random.Random) -> Dict[str, Any]:
    # x + 8 = 3 -> x = 3 - 8 = -5
    a = rng.randint(6, 12)
    b = rng.randint(1, 4)
    ans_val = b - a
    ans = str(ans_val)
    prompt = (
        f"Solve the equation in the set of integers (\\(\\mathbb{{Z}}\\)):\n"
        f"\\[ x + {a} = {b} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {a} from both sides:\n"
        f"$$x = {b} - {a}$$\n\n"
        f"**Step 2:** Calculate integer subtraction:\n"
        f"$$x = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_42_{rng.randint(100000, 999999)}",
        "subskill": "42_negative_integer_solution_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_42",
        "hints": {"tier_1": f"Subtract {a} from {b}.", "tier_2": f"{b} - {a} is negative.", "tier_3": ans},
        "misconception_tags": ["integer_subtraction_sign_error"]
    }


# 43. Negative integer solution multiplication
def arch_43_negative_integer_solution_multiplication(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 6])
    ans_val = rng.choice([-3, -4, -5, -6])
    b = a * ans_val
    ans = str(ans_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}x = {b} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{{b}}}{{{a}}}$$\n\n"
        f"**Step 2:** A negative divided by a positive is negative:\n"
        f"$$x = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_43_{rng.randint(100000, 999999)}",
        "subskill": "43_negative_integer_solution_multiplication",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_43",
        "hints": {"tier_1": f"Divide {b} by {a}.", "tier_2": "Negative divided by positive is negative.", "tier_3": ans},
        "misconception_tags": ["negative_division_sign_error"]
    }


# 44. Negative coefficient linear equation
def arch_44_negative_coefficient_linear_equation(rng: random.Random) -> Dict[str, Any]:
    neg_a = rng.choice([-2, -3, -4, -5])
    x_val = rng.randint(3, 8)
    b = neg_a * x_val
    ans = str(x_val)
    prompt = (
        f"Solve the equation:\n"
        f"\\[ {neg_a}x = {b} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by the negative coefficient \\({neg_a}\\):\n"
        f"$$x = \\frac{{{b}}}{{{neg_a}}}$$\n\n"
        f"**Step 2:** A negative number divided by a negative number is positive:\n"
        f"$$x = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_44_{rng.randint(100000, 999999)}",
        "subskill": "44_negative_coefficient_linear_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_44",
        "hints": {"tier_1": f"Divide {b} by {neg_a}.", "tier_2": "Negative divided by negative is positive.", "tier_3": ans},
        "misconception_tags": ["negative_divided_by_negative_sign_error"]
    }


# 45. Subtracting negative number equation
def arch_45_subtracting_negative_number_equation(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(3, 8)
    tot = rng.randint(10, 20)
    ans_val = tot - k
    ans = str(ans_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ x - (-{k}) = {tot} \\]"
    )
    sol = (
        f"**Step 1:** Subtracting a negative number is equivalent to addition:\n"
        f"$$x + {k} = {tot}$$\n\n"
        f"**Step 2:** Subtract {k} from both sides:\n"
        f"$$x = {tot} - {k} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_45_{rng.randint(100000, 999999)}",
        "subskill": "45_subtracting_negative_number_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_45",
        "hints": {"tier_1": f"x - (-{k}) becomes x + {k}.", "tier_2": f"x = {tot} - {k}.", "tier_3": ans},
        "misconception_tags": ["double_negative_simplification_error"]
    }


# 46. Consecutive numbers sum equation
def arch_46_consecutive_numbers_sum_equation(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(10, 25)
    sum_val = 2 * n + 1
    ans = str(n)
    prompt = (
        f"The sum of two consecutive integers is {sum_val}.\n"
        f"If the smaller integer is \\(n\\), then the equation is:\n"
        f"\\[ 2n + 1 = {sum_val} \\]\n\n"
        f"Solve for the smaller integer \\(n\\)."
    )
    sol = (
        f"**Step 1:** Subtract 1 from both sides:\n"
        f"$$2n = {sum_val} - 1 = {sum_val - 1}$$\n\n"
        f"**Step 2:** Divide by 2:\n"
        f"$$n = \\frac{{{sum_val - 1}}}{{2}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_46_{rng.randint(100000, 999999)}",
        "subskill": "46_consecutive_numbers_sum_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_46",
        "hints": {"tier_1": f"2n = {sum_val - 1}.", "tier_2": f"n = {sum_val - 1} / 2.", "tier_3": ans},
        "misconception_tags": ["consecutive_numbers_equation_setup_error"]
    }


# 47. Common misconception sign error trap
def arch_47_common_misconception_sign_error_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: 7 should be added to 12. Correct root is x = 19."
    prompt = (
        "To solve \\(x - 7 = 12\\), a learner wrote:\n"
        "\\[ x = 12 - 7 = 5 \\]\n\n"
        "1. Identify the error in the learner's method.\n"
        "2. State the correct solution for \\(x\\)."
    )
    sol = (
        "**Step 1:** Identify error:\n"
        "The learner subtracted 7 instead of adding 7 to both sides.\n"
        "The inverse of subtracting 7 is adding 7.\n\n"
        "**Step 2:** Correct solution:\n"
        "$$x = 12 + 7 = \\mathbf{19}$$"
    )
    return {
        "id": f"g7_eq1_47_{rng.randint(100000, 999999)}",
        "subskill": "47_common_misconception_sign_error_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_47",
        "hints": {"tier_1": "Inverse of -7 is +7.", "tier_2": "12 + 7 = 19.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_subtraction_equation"]
    }


# 48. Common misconception division error trap
def arch_48_common_misconception_division_error_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: 20 should be divided by 4, not subtracted by 4. Correct root is x = 5."
    prompt = (
        "A student solved \\(4x = 20\\) as follows:\n"
        "\\[ x = 20 - 4 = 16 \\]\n\n"
        "Explain the misconception and write down the correct solution."
    )
    sol = (
        "**Step 1:** Misconception:\n"
        "The student treated \\(4x\\) as an addition \\(x + 4\\) and subtracted 4.\n"
        "However, \\(4x\\) means \\(4 \\times x\\), and the inverse of multiplication is division.\n\n"
        "**Step 2:** Correct solution:\n"
        "$$x = \\frac{20}{4} = \\mathbf{5}$$"
    )
    return {
        "id": f"g7_eq1_48_{rng.randint(100000, 999999)}",
        "subskill": "48_common_misconception_division_error_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_48",
        "hints": {"tier_1": "Inverse of multiplying by 4 is dividing by 4.", "tier_2": "20 / 4 = 5.", "tier_3": ans},
        "misconception_tags": ["subtracting_coefficient_instead_of_dividing"]
    }


# 49. Checking roots distinguishing valid from invalid
def arch_49_checking_roots_distinguishing_valid_from_invalid(rng: random.Random) -> Dict[str, Any]:
    ans = "Equation A"
    prompt = (
        "Which of the following equations has \\(x = 4\\) as its correct solution?\n\n"
        "**Equation A:** \\(2x + 1 = 9\\)\n"
        "**Equation B:** \\(3x - 2 = 14\\)"
    )
    sol = (
        "**Test x = 4 in Equation A:**\n"
        "$$\\text{LHS} = 2(4) + 1 = 8 + 1 = 9 = \\text{RHS} \\quad \\text{(True!)}$$\n\n"
        "**Test x = 4 in Equation B:**\n"
        "$$\\text{LHS} = 3(4) - 2 = 12 - 2 = 10 \\neq 14 \\quad \\text{(False)}$$\n\n"
        "Therefore, \\(x = 4\\) is the root of **Equation A**."
    )
    return {
        "id": f"g7_eq1_49_{rng.randint(100000, 999999)}",
        "subskill": "49_checking_roots_distinguishing_valid_from_invalid",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Equation A", "Equation B", "Both", "Neither"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_49",
        "hints": {"tier_1": "Substitute x = 4 into both equations.", "tier_2": "2(4) + 1 = 9.", "tier_3": ans},
        "misconception_tags": ["root_verification_arithmetic_error"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_algebraic_equations_1_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "a) x = 9; b) m = 4; c) y = 7; d) 8"
    prompt = (
        "**Grade 7 Algebraic Equations 1 Comprehensive Diagnostic Autopsy**\n\n"
        "1. Solve by inspection: \\(x + 13 = 22\\).\n"
        "2. Solve the multiplication equation: \\(6m = 24\\).\n"
        "3. Solve the two-step equation: \\(3y - 5 = 16\\).\n"
        "4. A balanced scale has a mass of \\((p + 7)\\text{ kg}\\) on one pan and \\(15\\text{ kg}\\) on the other. "
        "Find the value of \\(p\\)."
    )
    sol = (
        "**Question 1:**\n"
        "$$x = 22 - 13 = \\mathbf{9}$$\n\n"
        "**Question 2:**\n"
        "$$m = \\frac{24}{6} = \\mathbf{4}$$\n\n"
        "**Question 3:**\n"
        "$$3y = 16 + 5 = 21 \\implies y = \\frac{21}{3} = \\mathbf{7}$$\n\n"
        "**Question 4:**\n"
        "$$p + 7 = 15 \\implies p = 15 - 7 = \\mathbf{8}$$"
    )
    return {
        "id": f"g7_eq1_50_{rng.randint(100000, 999999)}",
        "subskill": "50_algebraic_equations_1_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_eq1_50",
        "hints": {
            "tier_1": "1: 22 - 13. 2: 24 / 6. 3: (16 + 5)/3. 4: 15 - 7.",
            "tier_2": "1: x = 9. 2: m = 4. 3: y = 7. 4: p = 8.",
            "tier_3": ans
        },
        "misconception_tags": [
            "adding_instead_of_subtracting_constant",
            "subtracting_coefficient_instead_of_dividing",
            "order_of_operations_two_step_equation"
        ]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
