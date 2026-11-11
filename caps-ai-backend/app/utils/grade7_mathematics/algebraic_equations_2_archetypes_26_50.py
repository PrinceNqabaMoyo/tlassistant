"""Grade 7 Mathematics - Algebraic Equations 2: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 2.md
Focus: Word problems, fractions, decimals, combining like terms, SVG balance scales, verification, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_balance_scale(left_label: str, right_label: str) -> str:
    """Return clean 2D static SVG diagram of a balance scale in perfect equilibrium."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="220" style="background:#ffffff;">\n'
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
        f'  <rect x="55" y="125" width="70" height="28" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>\n'
        f'  <text x="90" y="144" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{left_label}</text>\n'
        f'  <!-- Right Pan Strings & Pan -->\n'
        f'  <line x1="370" y1="110" x2="340" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <line x1="370" y1="110" x2="400" y2="155" stroke="#64748b" stroke-width="1.5"/>\n'
        f'  <path d="M 330 155 Q 370 170 410 155 Z" fill="#cbd5e1" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <!-- Right Pan Content -->\n'
        f'  <rect x="335" y="125" width="70" height="28" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>\n'
        f'  <text x="370" y="144" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">{right_label}</text>\n'
        f'  <text x="230" y="80" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Balanced (=)</text>\n'
        f'</svg>'
    )


# 26. Word problem cellphone airtime
def arch_26_word_problem_cellphone_airtime(rng: random.Random) -> Dict[str, Any]:
    fixed_fee = 50
    rate_per_min = 2
    mins = rng.randint(25, 60)
    total_cost = fixed_fee + rate_per_min * mins
    ans = str(mins)
    prompt = (
        f"A mobile contract costs a fixed fee of R{fixed_fee} per month plus R{rate_per_min} per minute of calling.\n"
        f"Kagiso's total bill for last month was R{total_cost}.\n\n"
        f"Solve the equation \\({rate_per_min}m + {fixed_fee} = {total_cost}\\) to find the number of minutes \\(m\\) used."
    )
    sol = (
        f"**Step 1:** Subtract fixed fee:\n"
        f"$${rate_per_min}m = {total_cost} - {fixed_fee} = {total_cost - fixed_fee}$$\n\n"
        f"**Step 2:** Divide by rate per minute:\n"
        f"$$m = \\frac{{{total_cost - fixed_fee}}}{{{rate_per_min}}} = \\mathbf{{{ans}}}\\text{{ minutes}}$$"
    )
    return {
        "id": f"g7_eq2_26_{rng.randint(100000, 999999)}",
        "subskill": "26_word_problem_cellphone_airtime",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_26",
        "hints": {"tier_1": f"2m = {total_cost} - {fixed_fee}.", "tier_2": f"m = {total_cost - fixed_fee} / 2.", "tier_3": ans},
        "misconception_tags": ["dividing_total_bill_without_subtracting_fixed_fee"]
    }


# 27. Word problem consecutive even numbers
def arch_27_word_problem_consecutive_even_numbers(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([14, 16, 20, 22, 24])
    tot = 2 * n + 2
    ans = str(n)
    prompt = (
        f"The sum of two consecutive even integers is {tot}.\n"
        f"If the smaller integer is \\(n\\), then the equation is:\n"
        f"\\[ n + (n + 2) = {tot} \\implies 2n + 2 = {tot} \\]\n\n"
        f"Solve for the smaller even integer \\(n\\)."
    )
    sol = (
        f"**Step 1:** Subtract 2 from both sides:\n"
        f"$$2n = {tot} - 2 = {tot - 2}$$\n\n"
        f"**Step 2:** Divide by 2:\n"
        f"$$n = \\frac{{{tot - 2}}}{{2}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_27_{rng.randint(100000, 999999)}",
        "subskill": "27_word_problem_consecutive_even_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_27",
        "hints": {"tier_1": f"2n = {tot - 2}.", "tier_2": f"n = {tot - 2} / 2.", "tier_3": ans},
        "misconception_tags": ["consecutive_even_numbers_setup_step_error"]
    }


# 28. Word problem consecutive odd numbers
def arch_28_word_problem_consecutive_odd_numbers(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([15, 17, 21, 23, 27])
    tot = 2 * n + 2
    ans = str(n)
    prompt = (
        f"The sum of two consecutive odd numbers is {tot}.\n"
        f"Solve the equation \\(2n + 2 = {tot}\\) to find the smaller odd number \\(n\\)."
    )
    sol = (
        f"**Step 1:** Subtract 2 from both sides:\n"
        f"$$2n = {tot} - 2 = {tot - 2}$$\n\n"
        f"**Step 2:** Divide by 2:\n"
        f"$$n = \\frac{{{tot - 2}}}{{2}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_28_{rng.randint(100000, 999999)}",
        "subskill": "28_word_problem_consecutive_odd_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_28",
        "hints": {"tier_1": f"2n = {tot - 2}.", "tier_2": f"n = {tot - 2} / 2.", "tier_3": ans},
        "misconception_tags": ["consecutive_odd_numbers_setup_error"]
    }


# 29. Word problem perimeter square with algebraic side
def arch_29_word_problem_perimeter_square_with_algebraic_side(rng: random.Random) -> Dict[str, Any]:
    # 4(2x - 1) = 36 -> 2x - 1 = 9 -> 2x = 10 -> x = 5
    ans = "5"
    prompt = (
        "A square has side length \\((2x - 1)\\text{ cm}\\) and perimeter \\(36\\text{ cm}\\).\n\n"
        "1. Write down an equation: \\(4(2x - 1) = 36\\).\n"
        "2. Solve for \\(x\\)."
    )
    sol = (
        "**Step 1:** Divide both sides by 4:\n"
        "$$2x - 1 = \\frac{36}{4} = 9$$\n\n"
        "**Step 2:** Add 1 to both sides:\n"
        "$$2x = 9 + 1 = 10$$\n\n"
        "**Step 3:** Divide by 2:\n"
        "$$x = \\frac{10}{2} = \\mathbf{5}$$"
    )
    return {
        "id": f"g7_eq2_29_{rng.randint(100000, 999999)}",
        "subskill": "29_word_problem_perimeter_square_with_algebraic_side",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_29",
        "hints": {"tier_1": "Divide 36 by 4 first.", "tier_2": "2x - 1 = 9, so 2x = 10.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_divide_perimeter_by_four"]
    }


# 30. Word problem saving weekly allowance
def arch_30_word_problem_saving_weekly_allowance(rng: random.Random) -> Dict[str, Any]:
    start_amount = 100
    weekly_save = 25
    weeks = rng.randint(6, 12)
    target = start_amount + weekly_save * weeks
    ans = str(weeks)
    prompt = (
        f"Lindiwe has R{start_amount} in her savings account. She saves an additional R{weekly_save} each week.\n"
        f"How many weeks \\(w\\) will it take her to reach R{target}?\n\n"
        f"Solve: \\({weekly_save}w + {start_amount} = {target}\\)."
    )
    sol = (
        f"**Step 1:** Subtract initial savings:\n"
        f"$${weekly_save}w = {target} - {start_amount} = {target - start_amount}$$\n\n"
        f"**Step 2:** Divide by weekly rate:\n"
        f"$$w = \\frac{{{target - start_amount}}}{{{weekly_save}}} = \\mathbf{{{ans}}}\\text{{ weeks}}$$"
    )
    return {
        "id": f"g7_eq2_30_{rng.randint(100000, 999999)}",
        "subskill": "30_word_problem_saving_weekly_allowance",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_30",
        "hints": {"tier_1": f"{weekly_save}w = {target - start_amount}.", "tier_2": f"w = {target - start_amount} / {weekly_save}.", "tier_3": ans},
        "misconception_tags": ["dividing_target_savings_without_subtracting_starting_balance"]
    }


# 31. Word problem temperature drop rate
def arch_31_word_problem_temperature_drop_rate(rng: random.Random) -> Dict[str, Any]:
    # 28 - 3t = 16 -> 3t = 12 -> t = 4
    ans = "4"
    prompt = (
        "The temperature was \\(28^\\circ\\text{C}\\) at 14:00. It dropped at a steady rate of "
        "\\(3^\\circ\\text{C}\\) per hour until it reached \\(16^\\circ\\text{C}\\).\n\n"
        "Solve the equation \\(28 - 3t = 16\\) to find the number of hours \\(t\\) that elapsed."
    )
    sol = (
        "**Step 1:** Rearrange to isolate \\(3t\\):\n"
        "$$3t = 28 - 16 = 12$$\n\n"
        "**Step 2:** Divide by 3:\n"
        "$$t = \\frac{12}{3} = \\mathbf{4}\\text{ hours}$$"
    )
    return {
        "id": f"g7_eq2_31_{rng.randint(100000, 999999)}",
        "subskill": "31_word_problem_temperature_drop_rate",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_31",
        "hints": {"tier_1": "3t = 28 - 16.", "tier_2": "3t = 12, so t = 4.", "tier_3": ans},
        "misconception_tags": ["temperature_rate_equation_setup_error"]
    }


# 32. Two step with fractional coefficient
def arch_32_two_step_with_fractional_coefficient(rng: random.Random) -> Dict[str, Any]:
    # 2/3 x + 4 = 10 -> 2/3 x = 6 -> x = 6 * 3 / 2 = 9
    ans = "9"
    prompt = (
        "Solve the linear equation with a fractional coefficient:\n"
        "\\[ \\frac{2}{3}x + 4 = 10 \\]"
    )
    sol = (
        "**Step 1:** Subtract 4 from both sides:\n"
        "$$\\frac{2}{3}x = 10 - 4 = 6$$\n\n"
        "**Step 2:** Multiply both sides by 3:\n"
        "$$2x = 6 \\times 3 = 18$$\n\n"
        "**Step 3:** Divide both sides by 2:\n"
        "$$x = \\frac{18}{2} = \\mathbf{9}$$"
    )
    return {
        "id": f"g7_eq2_32_{rng.randint(100000, 999999)}",
        "subskill": "32_two_step_with_fractional_coefficient",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_32",
        "hints": {"tier_1": "First subtract 4 from 10.", "tier_2": "2/3 x = 6, multiply by 3/2.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_fraction_inverted_wrong_step"]
    }


# 33. Two step with fractional coefficient subtraction
def arch_33_two_step_with_fractional_coefficient_subtraction(rng: random.Random) -> Dict[str, Any]:
    # 3/5 x - 2 = 7 -> 3/5 x = 9 -> x = 9 * 5 / 3 = 15
    ans = "15"
    prompt = (
        "Solve for \\(x\\):\n"
        "\\[ \\frac{3}{5}x - 2 = 7 \\]"
    )
    sol = (
        "**Step 1:** Add 2 to both sides:\n"
        "$$\\frac{3}{5}x = 7 + 2 = 9$$\n\n"
        "**Step 2:** Multiply by 5 and divide by 3:\n"
        "$$x = \\frac{9 \\times 5}{3} = \\frac{45}{3} = \\mathbf{15}$$"
    )
    return {
        "id": f"g7_eq2_33_{rng.randint(100000, 999999)}",
        "subskill": "33_two_step_with_fractional_coefficient_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_33",
        "hints": {"tier_1": "Add 2 to both sides first: 3/5 x = 9.", "tier_2": "x = 9 × 5 / 3 = 15.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_fractional_two_step"]
    }


# 34. Two step decimal equation addition
def arch_34_two_step_decimal_equation_addition(rng: random.Random) -> Dict[str, Any]:
    # 0.4x + 1.2 = 3.6 -> 0.4x = 2.4 -> x = 6
    ans = "6"
    prompt = (
        "Solve the equation with decimals:\n"
        "\\[ 0{,}4x + 1{,}2 = 3{,}6 \\]"
    )
    sol = (
        "**Step 1:** Subtract 1,2 from both sides:\n"
        "$$0{,}4x = 3{,}6 - 1{,}2 = 2{,}4$$\n\n"
        "**Step 2:** Divide both sides by 0,4:\n"
        "$$x = \\frac{2{,}4}{0{,}4} = \\mathbf{6}$$"
    )
    return {
        "id": f"g7_eq2_34_{rng.randint(100000, 999999)}",
        "subskill": "34_two_step_decimal_equation_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_34",
        "hints": {"tier_1": "3,6 - 1,2 = 2,4.", "tier_2": "2,4 / 0,4 = 6.", "tier_3": ans},
        "misconception_tags": ["decimal_division_misalignment"]
    }


# 35. Two step decimal equation subtraction
def arch_35_two_step_decimal_equation_subtraction(rng: random.Random) -> Dict[str, Any]:
    # 1.5x - 2.0 = 5.5 -> 1.5x = 7.5 -> x = 5
    ans = "5"
    prompt = (
        "Solve for \\(x\\):\n"
        "\\[ 1{,}5x - 2{,}0 = 5{,}5 \\]"
    )
    sol = (
        "**Step 1:** Add 2,0 to both sides:\n"
        "$$1{,}5x = 5{,}5 + 2{,}0 = 7{,}5$$\n\n"
        "**Step 2:** Divide by 1,5:\n"
        "$$x = \\frac{7{,}5}{1{,}5} = \\mathbf{5}$$"
    )
    return {
        "id": f"g7_eq2_35_{rng.randint(100000, 999999)}",
        "subskill": "35_two_step_decimal_equation_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_35",
        "hints": {"tier_1": "5,5 + 2,0 = 7,5.", "tier_2": "7,5 / 1,5 = 5.", "tier_3": ans},
        "misconception_tags": ["decimal_subtraction_miscalculation"]
    }


# 36. Combining like terms before solving
def arch_36_combining_like_terms_before_solving(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 4)
    c2 = rng.randint(2, 4)
    k = rng.randint(3, 8)
    x_val = rng.randint(3, 7)
    tot = (c1 + c2) * x_val + k
    ans = str(x_val)
    prompt = (
        f"Simplify by collecting like terms first, then solve for \\(x\\):\n"
        f"\\[ {c1}x + {c2}x + {k} = {tot} \\]"
    )
    sol = (
        f"**Step 1:** Combine the variable terms \\({c1}x + {c2}x = {c1 + c2}x\\):\n"
        f"$${c1 + c2}x + {k} = {tot}$$\n\n"
        f"**Step 2:** Subtract {k} from both sides:\n"
        f"$${c1 + c2}x = {tot} - {k} = {tot - k}$$\n\n"
        f"**Step 3:** Divide by {c1 + c2}:\n"
        f"$$x = \\frac{{{tot - k}}}{{{c1 + c2}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_36_{rng.randint(100000, 999999)}",
        "subskill": "36_combining_like_terms_before_solving",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_36",
        "hints": {"tier_1": f"Combine {c1}x and {c2}x first.", "tier_2": f"{c1+c2}x = {tot - k}.", "tier_3": ans},
        "misconception_tags": ["adding_coefficients_and_constant_together"]
    }


# 37. Combining like terms subtraction before solving
def arch_37_combining_like_terms_subtraction_before_solving(rng: random.Random) -> Dict[str, Any]:
    c1 = 7
    c2 = 3
    k = 4
    x_val = 6
    tot = (c1 - c2) * x_val + k  # 4 * 6 + 4 = 28
    ans = str(x_val)
    prompt = (
        f"Solve the equation:\n"
        f"\\[ {c1}x - {c2}x + {k} = {tot} \\]"
    )
    sol = (
        f"**Step 1:** Combine \\({c1}x - {c2}x = {c1 - c2}x\\):\n"
        f"$${c1 - c2}x + {k} = {tot}$$\n\n"
        f"**Step 2:** Subtract {k} from both sides:\n"
        f"$${c1 - c2}x = {tot} - {k} = {tot - k}$$\n\n"
        f"**Step 3:** Divide by {c1 - c2}:\n"
        f"$$x = \\frac{{{tot - k}}}{{{c1 - c2}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_37_{rng.randint(100000, 999999)}",
        "subskill": "37_combining_like_terms_subtraction_before_solving",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_37",
        "hints": {"tier_1": f"Combine {c1}x - {c2}x = {c1 - c2}x.", "tier_2": f"{c1-c2}x = {tot - k}.", "tier_3": ans},
        "misconception_tags": ["sign_error_combining_variable_terms"]
    }


# 38. Combining constants before solving
def arch_38_combining_constants_before_solving(rng: random.Random) -> Dict[str, Any]:
    # 4x + 3 - 8 = 15 -> 4x - 5 = 15 -> 4x = 20 -> x = 5
    ans = "5"
    prompt = (
        "Solve the equation by combining numerical constants on the left first:\n"
        "\\[ 4x + 3 - 8 = 15 \\]"
    )
    sol = (
        "**Step 1:** Combine the constant numbers \\(+3 - 8 = -5\\):\n"
        "$$4x - 5 = 15$$\n\n"
        "**Step 2:** Add 5 to both sides:\n"
        "$$4x = 15 + 5 = 20$$\n\n"
        "**Step 3:** Divide by 4:\n"
        "$$x = \\frac{20}{4} = \\mathbf{5}$$"
    )
    return {
        "id": f"g7_eq2_38_{rng.randint(100000, 999999)}",
        "subskill": "38_combining_constants_before_solving",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_38",
        "hints": {"tier_1": "+3 - 8 = -5.", "tier_2": "4x - 5 = 15, so 4x = 20.", "tier_3": ans},
        "misconception_tags": ["integer_constant_combination_error"]
    }


# 39. Bracket expansion both sides
def arch_39_bracket_expansion_both_sides(rng: random.Random) -> Dict[str, Any]:
    # 2(x + 3) = x + 10 -> 2x + 6 = x + 10 -> x = 4
    ans = "4"
    prompt = (
        "Solve the equation by expanding the bracket:\n"
        "\\[ 2(x + 3) = x + 10 \\]"
    )
    sol = (
        "**Step 1:** Expand the bracket using the distributive property:\n"
        "$$2x + 6 = x + 10$$\n\n"
        "**Step 2:** Subtract \\(x\\) from both sides:\n"
        "$$x + 6 = 10$$\n\n"
        "**Step 3:** Subtract 6 from both sides:\n"
        "$$x = 10 - 6 = \\mathbf{4}$$"
    )
    return {
        "id": f"g7_eq2_39_{rng.randint(100000, 999999)}",
        "subskill": "39_bracket_expansion_both_sides",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_eq2_39",
        "hints": {"tier_1": "Expand 2(x + 3) to 2x + 6.", "tier_2": "2x - x = 10 - 6.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_multiply_bracket_constant"]
    }


# 40. Visual balance scale with brackets
def arch_40_visual_balance_scale_with_brackets(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    c = rng.randint(2, 6)
    x_val = rng.randint(3, 9)
    rhs = k * (x_val + c)
    ans = str(x_val)
    svg = _svg_balance_scale(f"{k}(x + {c}) kg", f"{rhs} kg")
    prompt = (
        "The balance scale shown below is in equilibrium:\n\n"
        "1. Write down the equation represented by the balanced scale.\n"
        "2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1:** Equation: \\({k}(x + {c}) = {rhs}\\).\n\n"
        f"**Step 2:** Divide both sides by {k}:\n"
        f"$$x + {c} = \\frac{{{rhs}}}{{{k}}} = {rhs // k}$$\n\n"
        f"**Step 3:** Subtract {c} from both sides:\n"
        f"$$x = {rhs // k} - {c} = \\mathbf{{{ans}}}\\text{{ kg}}$$"
    )
    return {
        "id": f"g7_eq2_40_{rng.randint(100000, 999999)}",
        "subskill": "40_visual_balance_scale_with_brackets",
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
        "learning_objective_id": "math_g7_eq2_40",
        "hints": {"tier_1": f"{k}(x + {c}) = {rhs}.", "tier_2": f"x + {c} = {rhs // k}, so x = {ans}.", "tier_3": ans},
        "misconception_tags": ["dividing_scale_total_by_bracket_terms_incorrectly"]
    }


# 41. Visual balance scale variables both sides
def arch_41_visual_balance_scale_variables_both_sides(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(3, 9)
    c_left = rng.randint(2, 6)
    c_right = 2 * x_val + c_left
    ans = str(x_val)
    svg = _svg_balance_scale(f"3x + {c_left} kg", f"x + {c_right} kg")
    prompt = (
        "The balance scale below contains boxes of mass \\(x\\) and weights on both pans:\n\n"
        "Determine the unknown mass \\(x\\) that keeps the scale balanced."
    )
    sol = (
        f"**Step 1:** Set up equation: \\(3x + {c_left} = x + {c_right}\\).\n\n"
        f"**Step 2:** Remove 1 box \\(x\\) from both pans:\n"
        f"$$2x + {c_left} = {c_right}$$\n\n"
        f"**Step 3:** Remove {c_left} kg from both pans:\n"
        f"$$2x = {c_right - c_left}$$\n\n"
        f"**Step 4:** Divide by 2:\n"
        f"$$x = \\frac{{{c_right - c_left}}}{{2}} = \\mathbf{{{ans}}}\\text{{ kg}}$$"
    )
    return {
        "id": f"g7_eq2_41_{rng.randint(100000, 999999)}",
        "subskill": "41_visual_balance_scale_variables_both_sides",
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
        "learning_objective_id": "math_g7_eq2_41",
        "hints": {"tier_1": f"Subtract x from both sides: 2x + {c_left} = {c_right}.", "tier_2": f"2x = {c_right - c_left}, so x = {ans}.", "tier_3": ans},
        "misconception_tags": ["balance_scale_transposition_error"]
    }


# 42. Formal verification LHS RHS tabular
def arch_42_formal_verification_lhs_rhs_tabular(rng: random.Random) -> Dict[str, Any]:
    ans = "LHS = 4(8) - 7 = 32 - 7 = 25 = RHS. True."
    prompt = (
        "A student claims that \\(x = 8\\) is the solution to \\(4x - 7 = 25\\).\n\n"
        "Perform a formal Left-Hand Side (LHS) vs Right-Hand Side (RHS) check to confirm if this is true."
    )
    sol = (
        "**Verification:**\n"
        "- **LHS** \\(= 4x - 7 = 4(8) - 7 = 32 - 7 = 25\\)\n"
        "- **RHS** \\(= 25\\)\n\n"
        "Since \\(\\text{LHS} = \\text{RHS} = 25\\), the root \\(x = 8\\) is verified as **True**."
    )
    return {
        "id": f"g7_eq2_42_{rng.randint(100000, 999999)}",
        "subskill": "42_formal_verification_lhs_rhs_tabular",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_42",
        "hints": {"tier_1": "Substitute 8 for x in 4x - 7.", "tier_2": "4(8) - 7 = 25.", "tier_3": ans},
        "misconception_tags": ["verification_arithmetic_error"]
    }


# 43. Checking multiple candidate solutions
def arch_43_checking_multiple_candidate_solutions(rng: random.Random) -> Dict[str, Any]:
    ans = "5"
    prompt = (
        "Which value from the candidate set \\(\\{2, 3, 5, 7\\}\\) satisfies the equation:\n"
        "\\[ 3(x - 1) + 4 = 16 \\]"
    )
    sol = (
        "**Test each candidate:**\n"
        "- For \\(x = 2\\): \\(3(1) + 4 = 7 \\neq 16\\)\n"
        "- For \\(x = 3\\): \\(3(2) + 4 = 10 \\neq 16\\)\n"
        "- For \\(x = 5\\): \\(3(4) + 4 = 12 + 4 = 16\\) (Correct!)\n"
        "- For \\(x = 7\\): \\(3(6) + 4 = 22 \\neq 16\\)\n\n"
        "Root: **\\(x = 5\\)**."
    )
    return {
        "id": f"g7_eq2_43_{rng.randint(100000, 999999)}",
        "subskill": "43_checking_multiple_candidate_solutions",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["2", "3", "5", "7"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_43",
        "hints": {"tier_1": "Test each candidate in 3(x - 1) + 4.", "tier_2": "3(4) + 4 = 16.", "tier_3": ans},
        "misconception_tags": ["candidate_testing_bracket_arithmetic_error"]
    }


# 44. Common misconception dividing before subtraction trap
def arch_44_common_misconception_dividing_before_subtraction_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "When dividing an equation by 2, every single term must be divided, giving x + 3 = 9."
    prompt = (
        "To solve \\(2x + 6 = 18\\), a student divided the equation by 2 and wrote:\n"
        "\\[ x + 6 = 9 \\]\n\n"
        "1. Why is this incorrect?\n"
        "2. What is the correct result after dividing all terms by 2?"
    )
    sol = (
        "**Step 1:** The student forgot to divide the term \\(6\\) by 2.\n"
        "By the distributive property of division over addition, dividing both sides by 2 requires dividing EVERY term:\n"
        "$$\\frac{2x}{2} + \\frac{6}{2} = \\frac{18}{2}$$\n\n"
        "**Step 2:** The correct equation is **\\(x + 3 = 9\\)** (which yields \\(x = 6\\))."
    )
    return {
        "id": f"g7_eq2_44_{rng.randint(100000, 999999)}",
        "subskill": "44_common_misconception_dividing_before_subtraction_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_44",
        "hints": {"tier_1": "Dividing both sides divides every term.", "tier_2": "6 / 2 = 3.", "tier_3": ans},
        "misconception_tags": ["dividing_only_variable_and_rhs_terms"]
    }


# 45. Common misconception bracket multiplication omission trap
def arch_45_common_misconception_bracket_multiplication_omission_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: 3 was not multiplied by 4. Correct expansion is 3x + 12 = 27, yielding x = 5."
    prompt = (
        "A student solved \\(3(x + 4) = 27\\) as follows:\n"
        "\\[ 3x + 4 = 27 \\implies 3x = 23 \\implies x = 23/3 \\]\n\n"
        "Identify the student's mistake and solve the equation correctly."
    )
    sol = (
        "**Step 1:** Mistake:\n"
        "The student omitted distributing the factor 3 to the second term \\(4\\).\n"
        "$$3(x + 4) = 3x + 12$$\n\n"
        "**Step 2:** Correct solution:\n"
        "$$3x + 12 = 27 \\implies 3x = 27 - 12 = 15 \\implies x = \\mathbf{5}$$"
    )
    return {
        "id": f"g7_eq2_45_{rng.randint(100000, 999999)}",
        "subskill": "45_common_misconception_bracket_multiplication_omission_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_45",
        "hints": {"tier_1": "3 × 4 = 12.", "tier_2": "3x = 15, so x = 5.", "tier_3": ans},
        "misconception_tags": ["bracket_distribution_constant_omission"]
    }


# 46. Common misconception sign flip transposition trap
def arch_46_common_misconception_sign_flip_transposition_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Moving +8 across the equals sign changes its sign to -8, giving 5x = 20 and x = 4."
    prompt = (
        "When solving \\(5x + 8 = 28\\), a learner wrote \\(5x = 28 + 8 = 36\\).\n\n"
        "Explain the error regarding sign changes and write down the correct solution."
    )
    sol = (
        "**Step 1:** Explanation:\n"
        "To undo \\(+8\\), you must subtract 8 from both sides (additive inverse).\n"
        "The learner added 8 instead of subtracting 8.\n\n"
        "**Step 2:** Correct solution:\n"
        "$$5x = 28 - 8 = 20$$\n"
        "$$x = \\frac{20}{5} = \\mathbf{4}$$"
    )
    return {
        "id": f"g7_eq2_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_misconception_sign_flip_transposition_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_46",
        "hints": {"tier_1": "Subtract 8 from 28.", "tier_2": "5x = 20, so x = 4.", "tier_3": ans},
        "misconception_tags": ["transposing_term_without_changing_sign"]
    }


# 47. Reversing flow diagram two step
def arch_47_reversing_flow_diagram_two_step(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(3, 9)
    x_val = rng.randint(4, 11)
    out = m * x_val - c
    ans = str(x_val)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 90" width="100%" height="90" style="background:#ffffff;">'
        f'<text x="35" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Input x</text>'
        f'<line x1="65" y1="45" x2="105" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="105" y="25" width="70" height="40" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="140" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">× {m}</text>'
        f'<line x1="175" y1="45" x2="215" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="215" y="25" width="70" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="250" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">− {c}</text>'
        f'<line x1="285" y1="45" x2="325" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="365" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Output {out}</text>'
        f'</svg>'
    )
    prompt = (
        f"A calculation rule is given by the flow diagram:\n"
        f"$$\\text{{Input }} x \\xrightarrow{{\\times {m}}} \\boxed{{\\quad}} \\xrightarrow{{- {c}}} \\mathbf{{{out}}}$$\n\n"
        f"Determine the input value \\(x\\) by working backwards."
    )
    sol = (
        f"**Step 1:** Undo \\(- {c}\\) by adding {c}:\n"
        f"$${out} + {c} = {out + c}$$\n\n"
        f"**Step 2:** Undo \\(\\times {m}\\) by dividing by {m}:\n"
        f"$$x = \\frac{{{out + c}}}{{{m}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_47_{rng.randint(100000, 999999)}",
        "subskill": "47_reversing_flow_diagram_two_step",
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
        "learning_objective_id": "math_g7_eq2_47",
        "hints": {"tier_1": f"{out} + {c} = {out + c}.", "tier_2": f"{out + c} / {m} = {ans}.", "tier_3": ans},
        "misconception_tags": ["flow_diagram_reversal_order_error"]
    }


# 48. Speed distance time algebraic equation
def arch_48_speed_distance_time_algebraic_equation(rng: random.Random) -> Dict[str, Any]:
    speed = 15
    walk = 3
    tot = 33
    ans = "2"
    prompt = (
        f"A cyclist travels at \\({speed}\\text{{ km/h}}\\) for \\(t\\) hours, and then walks a further "
        f"\\({walk}\\text{{ km}}\\). The total distance covered is \\({tot}\\text{{ km}}\\).\n\n"
        f"Solve \\({speed}t + {walk} = {tot}\\) to find how many hours \\(t\\) the cyclist rode."
    )
    sol = (
        f"**Step 1:** Subtract walking distance:\n"
        f"$${speed}t = {tot} - {walk} = {tot - walk}$$\n\n"
        f"**Step 2:** Divide by cycling speed:\n"
        f"$$t = \\frac{{{tot - walk}}}{{{speed}}} = \\mathbf{{{ans}}}\\text{{ hours}}$$"
    )
    return {
        "id": f"g7_eq2_48_{rng.randint(100000, 999999)}",
        "subskill": "48_speed_distance_time_algebraic_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_48",
        "hints": {"tier_1": f"15t = {tot - walk}.", "tier_2": f"t = {tot - walk} / 15.", "tier_3": ans},
        "misconception_tags": ["speed_time_distance_equation_error"]
    }


# 49. Water tank draining equation
def arch_49_water_tank_draining_equation(rng: random.Random) -> Dict[str, Any]:
    init_vol = 500
    drain_rate = 20
    rem_vol = 140
    ans = "18"
    prompt = (
        f"A water tank holds {init_vol} litres of water. Water drains out through a tap at a rate of "
        f"{drain_rate} litres per minute.\n\n"
        f"Solve \\({init_vol} - {drain_rate}t = {rem_vol}\\) to determine after how many minutes \\(t\\) "
        f"there will be {rem_vol} litres remaining."
    )
    sol = (
        f"**Step 1:** Rearrange the equation:\n"
        f"$${drain_rate}t = {init_vol} - {rem_vol} = {init_vol - rem_vol}$$\n\n"
        f"**Step 2:** Divide by draining rate:\n"
        f"$$t = \\frac{{{init_vol - rem_vol}}}{{{drain_rate}}} = \\mathbf{{{ans}}}\\text{{ minutes}}$$"
    )
    return {
        "id": f"g7_eq2_49_{rng.randint(100000, 999999)}",
        "subskill": "49_water_tank_draining_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_49",
        "hints": {"tier_1": f"20t = {init_vol - rem_vol}.", "tier_2": f"t = {init_vol - rem_vol} / 20.", "tier_3": ans},
        "misconception_tags": ["draining_rate_sign_error"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_algebraic_equations_2_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "a) x = 7; b) y = 4; c) m = 5; d) 8 kg"
    prompt = (
        "**Grade 7 Algebraic Equations 2 Comprehensive Diagnostic Autopsy**\n\n"
        "1. Solve the two-step equation: \\(4x - 5 = 23\\).\n"
        "2. Solve the bracket equation: \\(3(y + 2) = 18\\).\n"
        "3. Solve with variables on both sides: \\(5m + 4 = 2m + 19\\).\n"
        "4. A balanced scale has \\((2k + 4)\\text{ kg}\\) on the left and \\(20\\text{ kg}\\) on the right. Find \\(k\\)."
    )
    sol = (
        "**Question 1:**\n"
        "$$4x = 23 + 5 = 28 \\implies x = \\frac{28}{4} = \\mathbf{7}$$\n\n"
        "**Question 2:**\n"
        "$$y + 2 = \\frac{18}{3} = 6 \\implies y = 6 - 2 = \\mathbf{4}$$\n\n"
        "**Question 3:**\n"
        "$$5m - 2m = 19 - 4 \\implies 3m = 15 \\implies m = \\mathbf{5}$$\n\n"
        "**Question 4:**\n"
        "$$2k + 4 = 20 \\implies 2k = 16 \\implies k = \\mathbf{8}\\text{ kg}$$"
    )
    return {
        "id": f"g7_eq2_50_{rng.randint(100000, 999999)}",
        "subskill": "50_algebraic_equations_2_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_eq2_50",
        "hints": {
            "tier_1": "1: 4x = 28. 2: y + 2 = 6. 3: 3m = 15. 4: 2k = 16.",
            "tier_2": "1: x = 7. 2: y = 4. 3: m = 5. 4: k = 8.",
            "tier_3": ans
        },
        "misconception_tags": [
            "two_step_transposition_sign_error",
            "bracket_expansion_error",
            "variables_both_sides_collection_error"
        ]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
