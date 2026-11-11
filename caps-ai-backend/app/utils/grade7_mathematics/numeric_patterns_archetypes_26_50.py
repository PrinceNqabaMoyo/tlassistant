"""Grade 7 Mathematics - Numeric Patterns: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Numeric patterns.md
Focus: Tables of values, SVG visual matchstick & dot patterns, word problems, non-linear sequences, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_matchstick_squares() -> str:
    """Return clean 2D static SVG diagram of consecutive matchstick squares."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 140" width="100%" height="140" style="background:#ffffff;">\n'
        '  <!-- Figure 1: 1 square = 4 sticks -->\n'
        '  <rect x="30" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <circle cx="30" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="80" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="80" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="30" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="55" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 1 (4 sticks)</text>\n'
        '  <!-- Figure 2: 2 squares = 7 sticks -->\n'
        '  <rect x="150" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <rect x="200" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <circle cx="150" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="200" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="250" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="150" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="200" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="250" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="200" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 2 (7 sticks)</text>\n'
        '  <!-- Figure 3: 3 squares = 10 sticks -->\n'
        '  <rect x="320" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <rect x="370" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <rect x="420" y="30" width="50" height="50" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>\n'
        '  <circle cx="320" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="370" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="420" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="470" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="320" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="370" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="420" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="470" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="395" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 3 (10 sticks)</text>\n'
        '</svg>'
    )


def _svg_matchstick_triangles() -> str:
    """Return clean 2D static SVG diagram of consecutive matchstick triangles."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 140" width="100%" height="140" style="background:#ffffff;">\n'
        '  <!-- Pattern 1: 1 triangle = 3 sticks -->\n'
        '  <polygon points="50,30 25,80 75,80" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <circle cx="50" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="25" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="75" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="50" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 1 (3 sticks)</text>\n'
        '  <!-- Pattern 2: 2 triangles = 5 sticks -->\n'
        '  <polygon points="180,30 155,80 205,80" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <polygon points="205,80 180,30 230,30" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <circle cx="180" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="230" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="155" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="205" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="192" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 2 (5 sticks)</text>\n'
        '  <!-- Pattern 3: 3 triangles = 7 sticks -->\n'
        '  <polygon points="340,30 315,80 365,80" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <polygon points="365,80 340,30 390,30" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <polygon points="390,30 365,80 415,80" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>\n'
        '  <circle cx="340" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="390" cy="30" r="3" fill="#ef4444"/>\n'
        '  <circle cx="315" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="365" cy="80" r="3" fill="#ef4444"/>\n'
        '  <circle cx="415" cy="80" r="3" fill="#ef4444"/>\n'
        '  <text x="365" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Pattern 3 (7 sticks)</text>\n'
        '</svg>'
    )


# 26. Sequence table missing output
def arch_26_sequence_table_missing_output(rng: random.Random) -> Dict[str, Any]:
    # Rule: Tn = 3n + 4. For n = 8: 3(8) + 4 = 28
    ans = "28"
    prompt = (
        "Complete the missing output value \\(A\\) in the sequence table with rule \\(T_n = 3n + 4\\):\n\n"
        "| Term Position (\\(n\\)) | 1 | 2 | 3 | 5 | 8 |\n"
        "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
        "| Term Value (\\(T_n\\)) | 7 | 10 | 13 | 19 | \\(A\\) |\n\n"
        "Find the value of \\(A\\)."
    )
    sol = (
        "**Step 1:** Use the rule \\(T_n = 3n + 4\\) for \\(n = 8\\):\n"
        "$$A = T_8 = 3(8) + 4$$\n\n"
        "**Step 2:** Calculate: \\(24 + 4 = \\mathbf{28}\\)."
    )
    return {
        "id": f"g7_num_26_{rng.randint(100000, 999999)}",
        "subskill": "26_sequence_table_missing_output",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_26",
        "hints": {"tier_1": "Substitute n = 8 into 3n + 4.", "tier_2": "3(8) + 4 = 28.", "tier_3": ans},
        "misconception_tags": ["table_missing_output_arithmetic_error"]
    }


# 27. Sequence table missing input
def arch_27_sequence_table_missing_input(rng: random.Random) -> Dict[str, Any]:
    # Tn = 5n - 3 = 47 -> 5n = 50 -> n = 10
    ans = "10"
    prompt = (
        "Find the missing term position \\(B\\) in the table governed by \\(T_n = 5n - 3\\):\n\n"
        "| Term Position (\\(n\\)) | 1 | 2 | 3 | \\(B\\) | 20 |\n"
        "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
        "| Term Value (\\(T_n\\)) | 2 | 7 | 12 | 47 | 97 |\n\n"
        "Determine the position \\(B\\)."
    )
    sol = (
        "**Step 1:** Set \\(T_n = 47\\):\n"
        "$$5B - 3 = 47$$\n\n"
        "**Step 2:** Solve for \\(B\\):\n"
        "$$5B = 47 + 3 = 50$$\n"
        "$$B = \\frac{50}{5} = \\mathbf{10}$$"
    )
    return {
        "id": f"g7_num_27_{rng.randint(100000, 999999)}",
        "subskill": "27_sequence_table_missing_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_27",
        "hints": {"tier_1": "5B - 3 = 47.", "tier_2": "5B = 50, so B = 10.", "tier_3": ans},
        "misconception_tags": ["table_missing_input_equation_error"]
    }


# 28. Sequence table both inputs and outputs
def arch_28_missing_values_in_sequence_table(rng: random.Random) -> Dict[str, Any]:
    # Tn = 4n + 2. n=6 -> 26. Tn=50 -> n=12
    ans = "A = 26; B = 12"
    prompt = (
        "Complete the table for the sequence with rule \\(T_n = 4n + 2\\):\n\n"
        "| Term Position (\\(n\\)) | 1 | 2 | 3 | 6 | \\(B\\) |\n"
        "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
        "| Term Value (\\(T_n\\)) | 6 | 10 | 14 | \\(A\\) | 50 |\n\n"
        "Find the values of \\(A\\) and \\(B\\)."
    )
    sol = (
        "**Step 1:** Calculate \\(A\\) for \\(n = 6\\):\n"
        "$$A = 4(6) + 2 = 24 + 2 = \\mathbf{26}$$\n\n"
        "**Step 2:** Calculate \\(B\\) for \\(T_n = 50\\):\n"
        "$$4B + 2 = 50 \\implies 4B = 48 \\implies B = \\mathbf{12}$$\n\n"
        "Result: **\\(A = 26;\\; B = 12\\)**."
    )
    return {
        "id": f"g7_num_28_{rng.randint(100000, 999999)}",
        "subskill": "28_missing_values_in_sequence_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_num_28",
        "hints": {"tier_1": "For A: 4(6) + 2. For B: 4B + 2 = 50.", "tier_2": "A = 26; B = 12.", "tier_3": ans},
        "misconception_tags": ["confusing_input_and_output_in_sequence_table"]
    }


# 29. Determine if number belongs to sequence
def arch_29_determine_if_number_belongs_to_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "No, because (85 - 2) / 3 = 83 / 3 = 27,67 is not a natural number."
    prompt = (
        "A sequence has the general term \\(T_n = 3n + 2\\).\n\n"
        "Determine whether the number \\(85\\) is a term in this sequence. Justify your answer mathematically."
    )
    sol = (
        "**Step 1:** Set \\(T_n = 85\\) and solve for the term position \\(n\\):\n"
        "$$3n + 2 = 85$$\n"
        "$$3n = 85 - 2 = 83$$\n"
        "$$n = \\frac{83}{3} = 27\\frac{2}{3}$$\n\n"
        "**Step 2:** A term position \\(n\\) must be a positive whole number (natural number \\(\\mathbb{N}\\)).\n"
        "Since \\(27\\frac{2}{3}\\) is not an integer, **85 is NOT a term** in this sequence."
    )
    return {
        "id": f"g7_num_29_{rng.randint(100000, 999999)}",
        "subskill": "29_determine_if_number_belongs_to_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_29",
        "hints": {"tier_1": "Check if (85 - 2) is divisible by 3.", "tier_2": "83 is not divisible by 3.", "tier_3": ans},
        "misconception_tags": ["allowing_fractional_term_positions"]
    }


# 30. Matchstick squares pattern SVG
def arch_30_matchstick_squares_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    target_n = rng.choice([15, 20, 25, 30])
    sticks = 3 * target_n + 1
    ans = f"a) Tn = 3n + 1; b) {sticks} sticks"
    svg = _svg_matchstick_squares().replace(
        'text-anchor="middle">Pattern 3 (10 sticks)</text>',
        f'text-anchor="middle">Pattern 3 (10 sticks) | Target n = {target_n}</text>'
    )
    prompt = (
        "Examine the geometric arrangement formed using matchsticks:\n\n"
        "1. Write down the algebraic formula \\(T_n\\) for the matchstick count in stage \\(n\\).\n"
        f"2. How many matchsticks are required to construct stage {target_n}?"
    )
    sol = (
        "**Step 1:** Count the sticks in each figure:\n"
        "- Pattern 1: 4 sticks\n"
        "- Pattern 2: 7 sticks\n"
        "- Pattern 3: 10 sticks\n\n"
        "Common difference \\(d = 7 - 4 = 3\\).\n"
        "Offset \\(c\\): \\(3(1) + c = 4 \\implies c = 1\\).\n"
        "General rule: **\\(T_n = 3n + 1\\)**.\n\n"
        f"**Step 2:** For stage {target_n}:\n"
        f"$$T_{{{target_n}}} = 3({target_n}) + 1 = {3 * target_n} + 1 = \\mathbf{{{sticks}}}\\text{{ sticks}}$$"
    )
    return {
        "id": f"g7_num_30_{rng.randint(100000, 999999)}",
        "subskill": "30_matchstick_squares_pattern_svg",
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
        "learning_objective_id": "math_g7_num_30",
        "hints": {"tier_1": "Pattern adds 3 sticks each step.", "tier_2": f"Tn = 3n + 1. For n={target_n}: 3({target_n})+1 = {sticks}.", "tier_3": ans},
        "misconception_tags": ["multiplying_square_count_by_four_ignoring_shared_sides"]
    }


# 31. Matchstick triangles pattern SVG
def arch_31_matchstick_triangles_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    target_n = rng.choice([25, 30, 40, 50])
    sticks = 2 * target_n + 1
    ans = f"a) Tn = 2n + 1; b) {sticks} sticks"
    svg = _svg_matchstick_triangles().replace(
        'text-anchor="middle">Pattern 3 (7 sticks)</text>',
        f'text-anchor="middle">Pattern 3 (7 sticks) | Target n = {target_n}</text>'
    )
    prompt = (
        "Inspect the triangular matchstick arrangement:\n\n"
        "1. Write down the algebraic formula \\(T_n\\) in terms of \\(n\\).\n"
        f"2. Calculate the matchstick count needed for stage {target_n}."
    )
    sol = (
        "**Step 1:** Number of sticks:\n"
        "- Pattern 1: 3 sticks\n"
        "- Pattern 2: 5 sticks\n"
        "- Pattern 3: 7 sticks\n\n"
        "Common difference \\(d = 5 - 3 = 2\\).\n"
        "Offset \\(c\\): \\(2(1) + c = 3 \\implies c = 1\\).\n"
        "Formula: **\\(T_n = 2n + 1\\)**.\n\n"
        f"**Step 2:** Stage {target_n}:\n"
        f"$$T_{{{target_n}}} = 2({target_n}) + 1 = {2 * target_n} + 1 = \\mathbf{{{sticks}}}\\text{{ sticks}}$$"
    )
    return {
        "id": f"g7_num_31_{rng.randint(100000, 999999)}",
        "subskill": "31_matchstick_triangles_pattern_svg",
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
        "learning_objective_id": "math_g7_num_31",
        "hints": {"tier_1": "Each extra triangle adds 2 matchsticks.", "tier_2": f"Tn = 2n + 1. T{target_n} = 2({target_n})+1 = {sticks}.", "tier_3": ans},
        "misconception_tags": ["multiplying_triangles_by_three_ignoring_shared_edges"]
    }


# 32. Matchstick hexagons pattern SVG
def arch_32_matchstick_hexagons_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "Tn = 5n + 1"
    prompt = (
        "A sequence of connected regular hexagons is built with matchsticks:\n"
        "- 1 hexagon requires 6 sticks.\n"
        "- 2 connected hexagons require 11 sticks.\n"
        "- 3 connected hexagons require 16 sticks.\n\n"
        "Write down the formula \\(T_n\\) for the number of sticks in a row of \\(n\\) hexagons."
    )
    sol = (
        "**Step 1:** Common difference: \\(11 - 6 = 5\\) sticks added per new hexagon.\n\n"
        "**Step 2:** Offset \\(c\\): \\(5(1) + c = 6 \\implies c = 1\\).\n\n"
        "Formula: **\\(T_n = 5n + 1\\)**."
    )
    return {
        "id": f"g7_num_32_{rng.randint(100000, 999999)}",
        "subskill": "32_matchstick_hexagons_pattern_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_32",
        "hints": {"tier_1": "Difference is 5.", "tier_2": "5(1) + 1 = 6.", "tier_3": ans},
        "misconception_tags": ["multiplying_hexagons_by_six"]
    }


# 33. Dot array triangular pattern SVG
def arch_33_dot_array_triangular_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "36 dots"
    prompt = (
        "Triangular numbers represent dots stacked in rows:\n"
        "- Figure 1: 1 dot\n"
        "- Figure 2: 1 + 2 = 3 dots\n"
        "- Figure 3: 1 + 2 + 3 = 6 dots\n"
        "- Figure 4: 1 + 2 + 3 + 4 = 10 dots\n\n"
        "How many dots are in Figure 8?"
    )
    sol = (
        "**Step 1:** The number of dots in Figure \\(n\\) is the sum of integers from 1 to \\(n\\):\n"
        "$$\\text{Sum} = \\frac{n(n + 1)}{2}$$\n\n"
        "**Step 2:** For \\(n = 8\\):\n"
        "$$\\text{Dots} = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = \\frac{8 \\times 9}{2} = \\frac{72}{2} = \\mathbf{36}\\text{ dots}$$"
    )
    return {
        "id": f"g7_num_33_{rng.randint(100000, 999999)}",
        "subskill": "33_dot_array_triangular_pattern_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_33",
        "hints": {"tier_1": "Add 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8.", "tier_2": "8 × 9 / 2 = 36.", "tier_3": ans},
        "misconception_tags": ["triangular_dots_summation_error"]
    }


# 34. Dot array square pattern SVG
def arch_34_dot_array_square_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "144 dots"
    prompt = (
        "A sequence of square dot arrays has:\n"
        "- Array 1: \\(1 \\times 1 = 1\\) dot\n"
        "- Array 2: \\(2 \\times 2 = 4\\) dots\n"
        "- Array 3: \\(3 \\times 3 = 9\\) dots\n\n"
        "How many dots are in Array 12?"
    )
    sol = (
        "**Step 1:** The formula is \\(T_n = n^2\\).\n\n"
        "**Step 2:** For Array 12:\n"
        "$$T_{12} = 12^2 = 12 \\times 12 = \\mathbf{144}\\text{ dots}$$"
    )
    return {
        "id": f"g7_num_34_{rng.randint(100000, 999999)}",
        "subskill": "34_dot_array_square_pattern_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_34",
        "hints": {"tier_1": "Calculate 12 × 12.", "tier_2": "144.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_four_instead_of_squaring_in_dot_array"]
    }


# 35. Word problem savings pattern
def arch_35_word_problem_savings_pattern(rng: random.Random) -> Dict[str, Any]:
    ans = "a) Tn = 5n + 15; b) R115"
    prompt = (
        "Sipho starts a savings plan. In week 1, he saves R20. In week 2, he saves R25. "
        "In week 3, he saves R30, and his weekly savings continue to increase at this constant rate.\n\n"
        "1. Find the general rule \\(T_n\\) for the amount saved in week \\(n\\).\n"
        "2. How much will he save in week 20?"
    )
    sol = (
        "**Step 1:** Common difference \\(d = 25 - 20 = 5\\).\n"
        "When \\(n = 1\\): \\(5(1) + c = 20 \\implies c = 15\\).\n"
        "Formula: **\\(T_n = 5n + 15\\)**.\n\n"
        "**Step 2:** Week 20 savings:\n"
        "$$T_{20} = 5(20) + 15 = 100 + 15 = \\mathbf{\\text{R}115}$$"
    )
    return {
        "id": f"g7_num_35_{rng.randint(100000, 999999)}",
        "subskill": "35_word_problem_savings_pattern",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_num_35",
        "hints": {"tier_1": "Increase is R5 per week.", "tier_2": "Tn = 5n + 15. T20 = 5(20) + 15 = 115.", "tier_3": ans},
        "misconception_tags": ["savings_pattern_formula_offset_error"]
    }


# 36. Word problem stadium seating rows
def arch_36_word_problem_stadium_seating_rows(rng: random.Random) -> Dict[str, Any]:
    ans = "a) Tn = 4n + 8; b) 68 seats"
    prompt = (
        "In an amphitheatre, Row 1 has 12 seats, Row 2 has 16 seats, and Row 3 has 20 seats.\n\n"
        "1. Write down a formula \\(T_n\\) for the number of seats in Row \\(n\\).\n"
        "2. How many seats are in Row 15?"
    )
    sol = (
        "**Step 1:** Common difference \\(d = 16 - 12 = 4\\).\n"
        "When \\(n = 1\\): \\(4(1) + c = 12 \\implies c = 8\\).\n"
        "Rule: **\\(T_n = 4n + 8\\)**.\n\n"
        "**Step 2:** Row 15:\n"
        "$$T_{15} = 4(15) + 8 = 60 + 8 = \\mathbf{68}\\text{ seats}$$"
    )
    return {
        "id": f"g7_num_36_{rng.randint(100000, 999999)}",
        "subskill": "36_word_problem_stadium_seating_rows",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_num_36",
        "hints": {"tier_1": "Add 4 seats each row.", "tier_2": "4(15) + 8 = 68.", "tier_3": ans},
        "misconception_tags": ["seating_pattern_formula_setup_error"]
    }


# 37. Word problem tree growth pattern
def arch_37_word_problem_tree_growth_pattern(rng: random.Random) -> Dict[str, Any]:
    ans = "180 cm"
    prompt = (
        "A sapling is 60 cm tall when planted. It grows at a steady rate of 15 cm each year.\n\n"
        "Using the formula \\(H = 15n + 60\\), calculate the height of the tree after \\(n = 8\\) years."
    )
    sol = (
        "**Step 1:** Substitute \\(n = 8\\):\n"
        "$$H = 15(8) + 60$$\n\n"
        "**Step 2:** Calculate: \\(120 + 60 = \\mathbf{180}\\text{ cm}\\)."
    )
    return {
        "id": f"g7_num_37_{rng.randint(100000, 999999)}",
        "subskill": "37_word_problem_tree_growth_pattern",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_37",
        "hints": {"tier_1": "15 × 8 = 120.", "tier_2": "120 + 60 = 180.", "tier_3": ans},
        "misconception_tags": ["tree_growth_initial_height_omission"]
    }


# 38. Word problem bacterial growth doubling
def arch_38_word_problem_bacterial_growth_doubling(rng: random.Random) -> Dict[str, Any]:
    ans = "160 bacteria"
    prompt = (
        "A culture begins with 5 bacteria. The population doubles every hour:\n"
        "- Hour 0: 5\n"
        "- Hour 1: 10\n"
        "- Hour 2: 20\n\n"
        "How many bacteria will there be after 5 hours?"
    )
    sol = (
        "**Step 1:** Doubling pattern:\n"
        "- Hour 3: \\(20 \\times 2 = 40\\)\n"
        "- Hour 4: \\(40 \\times 2 = 80\\)\n"
        "- Hour 5: \\(80 \\times 2 = \\mathbf{160}\\)\n\n"
        "Formula: \\(5 \\times 2^5 = 5 \\times 32 = 160\\)."
    )
    return {
        "id": f"g7_num_38_{rng.randint(100000, 999999)}",
        "subskill": "38_word_problem_bacterial_growth_doubling",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_38",
        "hints": {"tier_1": "Double the amount 5 times.", "tier_2": "5 -> 10 -> 20 -> 40 -> 80 -> 160.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_five_instead_of_doubling"]
    }


# 39. Flow diagram to pattern
def arch_39_flow_diagram_to_pattern(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([4, 5, 6, 7, 8])
    c = rng.randint(1, 3)
    terms = [m * i - c for i in range(1, 5)]
    ans = "; ".join(str(x) for x in terms)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 90" width="100%" height="90" style="background:#ffffff;">'
        f'<text x="45" y="50" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">n = 1,2,3,4</text>'
        f'<line x1="85" y1="45" x2="115" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="115" y="25" width="70" height="40" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="150" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">× {m}</text>'
        f'<line x1="185" y1="45" x2="225" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<rect x="225" y="25" width="70" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="260" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">− {c}</text>'
        f'<line x1="295" y1="45" x2="335" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="370" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Output Tn</text>'
        f'</svg>'
    )
    prompt = (
        f"An operator machine processes inputs \\(n = 1, 2, 3, 4\\) using the two-stage rule:\n"
        f"$$n \\xrightarrow{{\\times {m}}} \\boxed{{\\quad}} \\xrightarrow{{- {c}}} T_n$$\n\n"
        f"Calculate the first four outputs generated by this machine."
    )
    sol = (
        f"**Calculate each term:**\n"
        f"- \\(n = 1\\): \\({m}(1) - {c} = {terms[0]}\\)\n"
        f"- \\(n = 2\\): \\({m}(2) - {c} = {terms[1]}\\)\n"
        f"- \\(n = 3\\): \\({m}(3) - {c} = {terms[2]}\\)\n"
        f"- \\(n = 4\\): \\({m}(4) - {c} = {terms[3]}\\)\n\n"
        f"First four outputs: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_num_39_{rng.randint(100000, 999999)}",
        "subskill": "39_flow_diagram_to_pattern",
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
        "learning_objective_id": "math_g7_num_39",
        "hints": {"tier_1": f"Multiply n by {m}, then subtract {c}.", "tier_2": f"{m}(1)-{c}={terms[0]}, {m}(2)-{c}={terms[1]}, etc.", "tier_3": ans},
        "misconception_tags": ["flow_diagram_operations_order_error"]
    }


# 40. Two different sequences same first term
def arch_40_two_different_sequences_same_first_term(rng: random.Random) -> Dict[str, Any]:
    ans = "Sequence A adds 4 each time; Sequence B doubles each time."
    prompt = (
        "Two sequences begin with the same first term \\(3\\):\n"
        "**Sequence A:** \\(3;\\; 7;\\; 11;\\; 15;\\; \\dots\\)\n"
        "**Sequence B:** \\(3;\\; 6;\\; 12;\\; 24;\\; \\dots\\)\n\n"
        "Compare the rules governing these two sequences."
    )
    sol = (
        "**Comparison:**\n"
        "- **Sequence A** is an arithmetic sequence with a constant difference of \\(+4\\).\n"
        "- **Sequence B** is a geometric sequence with a constant ratio of \\(\\times 2\\) (doubling).\n\n"
        "Conclusion: **Sequence A adds 4 each time; Sequence B doubles each time**."
    )
    return {
        "id": f"g7_num_40_{rng.randint(100000, 999999)}",
        "subskill": "40_two_different_sequences_same_first_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_40",
        "hints": {"tier_1": "Look at addition vs multiplication.", "tier_2": "A adds 4; B multiplies by 2.", "tier_3": ans},
        "misconception_tags": ["confusing_arithmetic_with_geometric_rate_of_growth"]
    }


# 41. Alternating sign pattern
def arch_41_alternating_sign_pattern(rng: random.Random) -> Dict[str, Any]:
    ans = "-12; 14"
    prompt = (
        "Extend the alternating sign sequence by two terms:\n"
        "\\[ 2;\\; -4;\\; 6;\\; -8;\\; 10;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** The numerical values are consecutive even numbers (2, 4, 6, 8, 10, ...).\n"
        "**Step 2:** The signs alternate: positive, negative, positive, negative, positive...\n\n"
        "Next two terms: **\\(-12;\\; 14\\)**."
    )
    return {
        "id": f"g7_num_41_{rng.randint(100000, 999999)}",
        "subskill": "41_alternating_sign_pattern",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_41",
        "hints": {"tier_1": "Next number is 12 with negative sign, then 14 with positive sign.", "tier_2": "-12, then 14.", "tier_3": ans},
        "misconception_tags": ["alternating_sign_sequence_sign_error"]
    }


# 42. Second order difference quadratic pattern
def arch_42_second_order_difference_quadratic_pattern(rng: random.Random) -> Dict[str, Any]:
    # 2, 5, 10, 17, 26 -> next is 26 + 11 = 37 (Tn = n^2 + 1)
    ans = "37"
    prompt = (
        "Consider the sequence:\n"
        "\\[ 2;\\; 5;\\; 10;\\; 17;\\; 26;\\; \\dots \\]\n\n"
        "Find the differences between consecutive terms and determine the 6th term."
    )
    sol = (
        "**Step 1:** First differences:\n"
        "- \\(5 - 2 = 3\\)\n"
        "- \\(10 - 5 = 5\\)\n"
        "- \\(17 - 10 = 7\\)\n"
        "- \\(26 - 17 = 9\\)\n\n"
        "The differences increase by 2 each time (consecutive odd numbers: 3, 5, 7, 9).\n\n"
        "**Step 2:** The next difference is \\(9 + 2 = 11\\).\n"
        "6th term: \\(26 + 11 = \\mathbf{37}\\)\n\n"
        "*(Note: Formula is \\(T_n = n^2 + 1\\), so \\(6^2 + 1 = 37\\))*"
    )
    return {
        "id": f"g7_num_42_{rng.randint(100000, 999999)}",
        "subskill": "42_second_order_difference_quadratic_pattern",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_42",
        "hints": {"tier_1": "Differences are 3, 5, 7, 9. Next difference is 11.", "tier_2": "26 + 11 = 37.", "tier_3": ans},
        "misconception_tags": ["second_order_difference_calculation_error"]
    }


# 43. Arithmetic vs geometric classification
def arch_43_arithmetic_vs_geometric_classification(rng: random.Random) -> Dict[str, Any]:
    ans = "Arithmetic"
    prompt = (
        "Classify the sequence as **Arithmetic** (constant difference) or **Geometric** (constant ratio):\n"
        "\\[ 4;\\; 9;\\; 14;\\; 19;\\; 24;\\; \\dots \\]"
    )
    sol = (
        "**Check Differences:**\n"
        "$$9 - 4 = 5, \\quad 14 - 9 = 5, \\quad 19 - 14 = 5$$\n\n"
        "Since there is a constant difference of \\(+5\\), it is an **Arithmetic** sequence."
    )
    return {
        "id": f"g7_num_43_{rng.randint(100000, 999999)}",
        "subskill": "43_arithmetic_vs_geometric_classification",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Arithmetic", "Geometric", "Fibonacci", "Quadratic"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_43",
        "hints": {"tier_1": "Does it add a fixed number each time?", "tier_2": "Adding a constant means arithmetic.", "tier_3": ans},
        "misconception_tags": ["confusing_arithmetic_and_geometric_definitions"]
    }


# 44. Common misconception confusing term and position
def arch_44_common_misconception_confusing_term_and_position(rng: random.Random) -> Dict[str, Any]:
    ans = "n is the position/term number (5th term), whereas Tn is the actual value of that term (23)."
    prompt = (
        "In the pattern formula \\(T_n = 4n + 3\\), for \\(n = 5\\) the result is \\(T_5 = 23\\).\n\n"
        "Explain clearly the difference between the symbol \\(n\\) and the symbol \\(T_n\\)."
    )
    sol = (
        "**Explanation:**\n"
        "- **\\(n\\)** represents the **position number** (or term number) in the sequence (e.g. 1st, 2nd, 5th term).\n"
        "- **\\(T_n\\)** represents the **numerical value** of the term at that position.\n\n"
        "Here, \\(n = 5\\) means the 5th term, and its value is \\(T_5 = 23\\)."
    )
    return {
        "id": f"g7_num_44_{rng.randint(100000, 999999)}",
        "subskill": "44_common_misconception_confusing_term_and_position",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_44",
        "hints": {"tier_1": "Think about a queue: position in line vs the person's name/value.", "tier_2": "n is position, Tn is value.", "tier_3": ans},
        "misconception_tags": ["confusing_position_number_with_term_value"]
    }


# 45. Common misconception extending by first difference only
def arch_45_common_misconception_extending_by_first_difference_only(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: the differences are not constant (it multiplies by 2). The next term is 16 × 2 = 32, not 16 + 2 = 18."
    prompt = (
        "A student looked at the sequence \\(2;\\; 4;\\; 8;\\; 16;\\; \\dots\\) and calculated \\(4 - 2 = 2\\).\n"
        "They concluded the next term was \\(16 + 2 = 18\\).\n\n"
        "Identify the misconception in their reasoning and state the correct next term."
    )
    sol = (
        "**Step 1:** Misconception:\n"
        "The student assumed all sequences are arithmetic and checked only the difference between the first two terms.\n"
        "However: \\(8 - 4 = 4\\) and \\(16 - 8 = 8\\). The differences are NOT constant.\n\n"
        "**Step 2:** The sequence doubles each time (geometric progression):\n"
        "Next term: \\(16 \\times 2 = \\mathbf{32}\\)."
    )
    return {
        "id": f"g7_num_45_{rng.randint(100000, 999999)}",
        "subskill": "45_common_misconception_extending_by_first_difference_only",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_45",
        "hints": {"tier_1": "Check if 8 - 4 = 2.", "tier_2": "It doubles, so 16 × 2 = 32.", "tier_3": ans},
        "misconception_tags": ["assuming_non_linear_sequence_is_arithmetic"]
    }


# 46. Common misconception multiplying instead of adding in formula
def arch_46_common_misconception_multiplying_instead_of_adding_in_formula(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: the offset +2 must be added, not multiplied. Correct 10th term is 5(10) + 2 = 52."
    prompt = (
        "For the rule \\(T_n = 5n + 2\\), a learner calculated the 10th term as:\n"
        "\\[ T_{10} = 5 \\times 10 \\times 2 = 100 \\]\n\n"
        "Point out the arithmetic error and write down the correct value of \\(T_{10}\\)."
    )
    sol = (
        "**Step 1:** Error:\n"
        "The learner multiplied by 2 instead of adding 2.\n\n"
        "**Step 2:** Correct calculation:\n"
        "$$T_{10} = 5(10) + 2 = 50 + 2 = \\mathbf{52}$$"
    )
    return {
        "id": f"g7_num_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_misconception_multiplying_instead_of_adding_in_formula",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_46",
        "hints": {"tier_1": "Order of operations: multiply 5 by 10, then add 2.", "tier_2": "50 + 2 = 52.", "tier_3": ans},
        "misconception_tags": ["multiplying_instead_of_adding_formula_constant"]
    }


# 47. Finding missing intermediate term
def arch_47_finding_missing_intermediate_term(rng: random.Random) -> Dict[str, Any]:
    t1 = 7
    t3 = 21
    ans = "14"
    prompt = (
        "An arithmetic sequence has constant difference \\(d\\):\n"
        f"\\[ {t1};\\; \\underline{{\\quad\\quad}};\\; {t3} \\]\n\n"
        "Find the missing intermediate term."
    )
    sol = (
        f"**Step 1:** In an arithmetic sequence, the middle term is the mean (average) of its neighbours:\n"
        f"$$\\text{{Middle term}} = \\frac{{{t1} + {t3}}}{{2}}$$\n\n"
        f"**Step 2:** Calculate: \\(\\frac{{{t1 + t3}}}{{2}} = \\mathbf{{{ans}}}\\).\n\n"
        f"Check: difference is \\(14 - 7 = 7\\) and \\(21 - 14 = 7\\)."
    )
    return {
        "id": f"g7_num_47_{rng.randint(100000, 999999)}",
        "subskill": "47_finding_missing_intermediate_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_47",
        "hints": {"tier_1": f"Add {t1} and {t3}, then divide by 2.", "tier_2": f"({t1} + {t3}) / 2 = 14.", "tier_3": ans},
        "misconception_tags": ["arithmetic_mean_missing_term_error"]
    }


# 48. Finding two missing intermediate terms
def arch_48_finding_two_missing_intermediate_terms(rng: random.Random) -> Dict[str, Any]:
    ans = "10; 15"
    prompt = (
        "Determine the two missing terms in the arithmetic sequence:\n"
        "\\[ 5;\\; \\underline{\\quad\\quad};\\; \\underline{\\quad\\quad};\\; 20 \\]"
    )
    sol = (
        "**Step 1:** Moving from the 1st term (5) to the 4th term (20) takes 3 equal steps of \\(d\\):\n"
        "$$T_4 - T_1 = 3d$$\n"
        "$$20 - 5 = 15 = 3d \\implies d = \\frac{15}{3} = 5$$\n\n"
        "**Step 2:** Add \\(d = 5\\) successively:\n"
        "- 2nd term: \\(5 + 5 = 10\\)\n"
        "- 3rd term: \\(10 + 5 = 15\\)\n\n"
        "Missing terms: **\\(10;\\; 15\\)**."
    )
    return {
        "id": f"g7_num_48_{rng.randint(100000, 999999)}",
        "subskill": "48_finding_two_missing_intermediate_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_48",
        "hints": {"tier_1": "There are 3 steps between 5 and 20. Divide (20 - 5) by 3.", "tier_2": "d = 5.", "tier_3": ans},
        "misconception_tags": ["dividing_total_difference_by_two_instead_of_three"]
    }


# 49. Sum of first n terms observation
def arch_49_sum_of_first_n_terms_observation(rng: random.Random) -> Dict[str, Any]:
    ans = "100"
    prompt = (
        "Observe the pattern of sums of consecutive odd numbers:\n"
        "- \\(1 = 1^2 = 1\\)\n"
        "- \\(1 + 3 = 2^2 = 4\\)\n"
        "- \\(1 + 3 + 5 = 3^2 = 9\\)\n"
        "- \\(1 + 3 + 5 + 7 = 4^2 = 16\\)\n\n"
        "Using this pattern, what is the sum of the first 10 odd numbers?"
    )
    sol = (
        "**Step 1:** The sum of the first \\(n\\) consecutive odd numbers equals \\(n^2\\).\n\n"
        "**Step 2:** For \\(n = 10\\):\n"
        "$$\\text{Sum} = 10^2 = 10 \\times 10 = \\mathbf{100}$$"
    )
    return {
        "id": f"g7_num_49_{rng.randint(100000, 999999)}",
        "subskill": "49_sum_of_first_n_terms_observation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_49",
        "hints": {"tier_1": "The sum is n^2.", "tier_2": "10^2 = 100.", "tier_3": ans},
        "misconception_tags": ["adding_odd_numbers_manually_making_arithmetic_mistakes"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_numeric_patterns_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "a) d = 6; b) Tn = 6n - 2; c) T25 = 148; d) n = 15"
    prompt = (
        "**Grade 7 Arithmetic Progression Diagnostic Autopsy**\n\n"
        "Given the progression: \\(4;\\; 10;\\; 16;\\; 22;\\; ...\\)\n\n"
        "1. State the constant difference \\(d\\).\n"
        "2. Derive the algebraic formula \\(T_n\\).\n"
        "3. Evaluate the 25th entry (\\(T_{25}\\)).\n"
        "4. Solve for index \\(n\\) where \\(T_n = 88\\)."
    )
    sol = (
        "**Question 1:**\n"
        "$$d = 10 - 4 = \\mathbf{6}$$\n\n"
        "**Question 2:**\n"
        "When \\(n = 1\\): \\(6(1) + c = 4 \\implies c = -2\\).\n"
        "General rule: **\\(T_n = 6n - 2\\)**.\n\n"
        "**Question 3:**\n"
        "$$T_{25} = 6(25) - 2 = 150 - 2 = \\mathbf{148}$$\n\n"
        "**Question 4:**\n"
        "$$6n - 2 = 88 \\implies 6n = 90 \\implies n = \\frac{90}{6} = \\mathbf{15}$$\n"
        "The **15th term** has value 88."
    )
    return {
        "id": f"g7_num_50_{rng.randint(100000, 999999)}",
        "subskill": "50_numeric_patterns_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_num_50",
        "hints": {
            "tier_1": "1: d = 10 - 4. 2: Tn = 6n - 2. 3: 6(25) - 2. 4: 6n - 2 = 88.",
            "tier_2": "1: d = 6. 2: Tn = 6n - 2. 3: 148. 4: n = 15.",
            "tier_3": ans
        },
        "misconception_tags": [
            "constant_difference_calculation_error",
            "formula_offset_sign_error",
            "distant_term_calculation_error",
            "term_position_solving_error"
        ]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
