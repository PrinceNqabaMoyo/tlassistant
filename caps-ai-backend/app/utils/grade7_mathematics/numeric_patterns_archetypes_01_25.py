"""Grade 7 Mathematics - Numeric Patterns: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Numeric patterns.md
Focus: Ascending & descending sequences, negative extensions, constant differences, geometric sequences, square & cubic numbers, formulas Tn = dn + c, and calculating distant terms.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Extending linear ascending sequence
def arch_01_extending_linear_ascending_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(2, 8)
    d = rng.choice([3, 4, 5, 6, 7])
    t1 = start
    t2 = t1 + d
    t3 = t2 + d
    t4 = t3 + d
    t5 = t4 + d
    t6 = t5 + d
    ans = f"{t5}; {t6}"
    prompt = (
        f"Study the ascending progression:\n"
        f"\\[ {t1};\\; {t2};\\; {t3};\\; {t4};\\; ... \\]\n\n"
        f"1. State the common difference \\(d\\).\n"
        f"2. Write down the 5th and 6th values."
    )
    sol = (
        f"**Step 1:** Calculate common difference:\n"
        f"$$d = {t2} - {t1} = {d}$$\n\n"
        f"**Step 2:** Add {d} to find subsequent terms:\n"
        f"- 5th term: \\({t4} + {d} = {t5}\\)\n"
        f"- 6th term: \\({t5} + {d} = {t6}\\)\n\n"
        f"Next two terms: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_num_01_{rng.randint(100000, 999999)}",
        "subskill": "01_extending_linear_ascending_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_01",
        "hints": {"tier_1": f"Find difference {t2} - {t1}.", "tier_2": f"Add {d} repeatedly.", "tier_3": ans},
        "misconception_tags": ["arithmetic_addition_error_in_sequence_extension"]
    }


# 02. Extending linear descending sequence
def arch_02_extending_linear_descending_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(50, 80)
    d = rng.choice([4, 5, 6, 7, 8])
    t1 = start
    t2 = t1 - d
    t3 = t2 - d
    t4 = t3 - d
    t5 = t4 - d
    t6 = t5 - d
    ans = f"{t5}; {t6}"
    prompt = (
        f"Examine the descending progression:\n"
        f"\\[ {t1};\\; {t2};\\; {t3};\\; {t4};\\; ... \\]\n\n"
        f"State the constant difference and write down the 5th and 6th values."
    )
    sol = (
        f"**Step 1:** Common difference \\(d\\):\n"
        f"$$d = {t2} - {t1} = -{d}$$\n\n"
        f"**Step 2:** Subtract {d} each time:\n"
        f"- 5th term: \\({t4} - {d} = {t5}\\)\n"
        f"- 6th term: \\({t5} - {d} = {t6}\\)\n\n"
        f"Next two terms: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_num_02_{rng.randint(100000, 999999)}",
        "subskill": "02_extending_linear_descending_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_02",
        "hints": {"tier_1": f"Each term decreases by {d}.", "tier_2": f"{t4} - {d} = {t5}.", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_subtracting_in_descending_sequence"]
    }


# 03. Extending sequence backwards into negative integers
def arch_03_extending_sequence_backwards_into_negative(rng: random.Random) -> Dict[str, Any]:
    step = 4
    # -13, -9, -5, -1, 3, 7
    ans = "3"
    prompt = (
        "Fill in the missing number to complete the number sequence in both directions:\n"
        "\\[ -13;\\; -9;\\; -5;\\; -1;\\; \\underline{\\quad\\quad};\\; 7 \\]"
    )
    sol = (
        "**Step 1:** Find the constant difference by subtracting consecutive terms:\n"
        "$$(-1) - (-5) = -1 + 5 = +4$$\n"
        "$$(-5) - (-9) = -5 + 9 = +4$$\n"
        "The pattern increases by 4 each step.\n\n"
        "**Step 2:** Add 4 to \\(-1\\):\n"
        "$$-1 + 4 = \\mathbf{3}$$\n\n"
        "Check: \\(3 + 4 = 7\\) (Matches!)."
    )
    return {
        "id": f"g7_num_03_{rng.randint(100000, 999999)}",
        "subskill": "03_extending_sequence_backwards_into_negative",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_03",
        "hints": {"tier_1": "Difference is +4.", "tier_2": "-1 + 4 = 3.", "tier_3": ans},
        "misconception_tags": ["negative_integer_sequence_addition_error"]
    }


# 04. Constant difference ascending
def arch_04_constant_difference_calculation(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([6, 7, 8, 9, 11])
    c = rng.randint(3, 10)
    terms = [c + i * d for i in range(4)]
    ans = str(d)
    prompt = (
        f"Calculate the common difference \\(d\\) for the arithmetic sequence:\n"
        f"\\[ {terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]} \\]"
    )
    sol = (
        f"**Step 1:** Subtract the 1st term from the 2nd term:\n"
        f"$$d = T_2 - T_1 = {terms[1]} - {terms[0]} = \\mathbf{{{ans}}}$$\n\n"
        f"Check: \\(T_3 - T_2 = {terms[2]} - {terms[1]} = {ans}\\)."
    )
    return {
        "id": f"g7_num_04_{rng.randint(100000, 999999)}",
        "subskill": "04_constant_difference_calculation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_04",
        "hints": {"tier_1": f"Subtract {terms[0]} from {terms[1]}.", "tier_2": f"{terms[1]} - {terms[0]} = {d}.", "tier_3": ans},
        "misconception_tags": ["subtracting_in_wrong_order_for_difference"]
    }


# 05. Constant difference descending
def arch_05_constant_difference_descending(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 6, 7])
    start = 40
    terms = [start - i * d for i in range(4)]
    ans = f"-{d}"
    prompt = (
        f"What is the constant difference \\(d\\) of the descending sequence:\n"
        f"\\[ {terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]} \\]?"
    )
    sol = (
        f"**Step 1:** Use formula \\(d = T_2 - T_1\\):\n"
        f"$$d = {terms[1]} - {terms[0]} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_num_05_{rng.randint(100000, 999999)}",
        "subskill": "05_constant_difference_descending",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_05",
        "hints": {"tier_1": f"T2 - T1 = {terms[1]} - {terms[0]}.", "tier_2": "Because it decreases, difference is negative.", "tier_3": ans},
        "misconception_tags": ["omitting_negative_sign_in_descending_difference"]
    }


# 06. Identify next three terms fractional step
def arch_06_identify_next_three_terms_fractional_step(rng: random.Random) -> Dict[str, Any]:
    ans = "2 1/2; 3; 3 1/2"
    prompt = (
        "Extend the fractional progression by three additional entries:\n"
        "\\[ \\frac{1}{2};\\; 1;\\; 1\\frac{1}{2};\\; 2;\\; ... \\]"
    )
    sol = (
        "**Step 1:** Common difference is \\(+\\frac{1}{2}\\).\n\n"
        "**Step 2:** Add \\(\\frac{1}{2}\\) successively:\n"
        "- 5th term: \\(2 + \\frac{1}{2} = 2\\frac{1}{2}\\)\n"
        "- 6th term: \\(2\\frac{1}{2} + \\frac{1}{2} = 3\\)\n"
        "- 7th term: \\(3 + \\frac{1}{2} = 3\\frac{1}{2}\\)\n\n"
        "Next three terms: **\\(2\\frac{1}{2};\\; 3;\\; 3\\frac{1}{2}\\)**."
    )
    return {
        "id": f"g7_num_06_{rng.randint(100000, 999999)}",
        "subskill": "06_identify_next_three_terms_fractional_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_06",
        "hints": {"tier_1": "Add 1/2 each time.", "tier_2": "2 + 1/2 = 2 1/2.", "tier_3": ans},
        "misconception_tags": ["fraction_sequence_addition_error"]
    }


# 07. Identify next three terms decimal step
def arch_07_identify_next_three_terms_decimal_step(rng: random.Random) -> Dict[str, Any]:
    ans = "2,5; 3,0; 3,5"
    prompt = (
        "Extend the decimal progression by three additional entries:\n"
        "\\[ 0{,}5;\\; 1{,}0;\\; 1{,}5;\\; 2{,}0;\\; ... \\]"
    )
    sol = (
        "**Step 1:** Common difference is \\(+0{,}5\\).\n\n"
        "**Step 2:** Add 0,5 to each subsequent term:\n"
        "- 5th term: \\(2{,}0 + 0{,}5 = 2{,}5\\)\n"
        "- 6th term: \\(2{,}5 + 0{,}5 = 3{,}0\\)\n"
        "- 7th term: \\(3{,}0 + 0{,}5 = 3{,}5\\)\n\n"
        "Next three terms: **2,5; 3,0; 3,5**."
    )
    return {
        "id": f"g7_num_07_{rng.randint(100000, 999999)}",
        "subskill": "07_identify_next_three_terms_decimal_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_07",
        "hints": {"tier_1": "Add 0,5 each time.", "tier_2": "2,0 + 0,5 = 2,5.", "tier_3": ans},
        "misconception_tags": ["decimal_point_pattern_addition_error"]
    }


# 08. Geometric doubling sequence
def arch_08_geometric_doubling_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "64; 128"
    prompt = (
        "The following geometric progression has a constant ratio:\n"
        "\\[ 2;\\; 4;\\; 8;\\; 16;\\; 32;\\; ... \\]\n\n"
        "1. State the multiplicative rule.\n"
        "2. Calculate the 6th and 7th values."
    )
    sol = (
        "**Step 1:** Rule: Multiply by 2 (doubling) each time:\n"
        "$$\\frac{4}{2} = 2, \\quad \\frac{8}{4} = 2$$\n\n"
        "**Step 2:** Next two terms:\n"
        "- 6th term: \\(32 \\times 2 = 64\\)\n"
        "- 7th term: \\(64 \\times 2 = 128\\)\n\n"
        "Next two terms: **\\(64;\\; 128\\)**."
    )
    return {
        "id": f"g7_num_08_{rng.randint(100000, 999999)}",
        "subskill": "08_geometric_doubling_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_08",
        "hints": {"tier_1": "Multiply each term by 2.", "tier_2": "32 × 2 = 64, 64 × 2 = 128.", "tier_3": ans},
        "misconception_tags": ["treating_geometric_sequence_as_arithmetic"]
    }


# 09. Geometric tripling sequence
def arch_09_geometric_tripling_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "243"
    prompt = (
        "Find the 5th term of the geometric sequence:\n"
        "\\[ 3;\\; 9;\\; 27;\\; 81;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** Notice that each term is multiplied by 3:\n"
        "$$3 \\times 3 = 9, \\quad 9 \\times 3 = 27, \\quad 27 \\times 3 = 81$$\n\n"
        "**Step 2:** 5th term: \\(81 \\times 3 = \\mathbf{243}\\)."
    )
    return {
        "id": f"g7_num_09_{rng.randint(100000, 999999)}",
        "subskill": "09_geometric_tripling_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_09",
        "hints": {"tier_1": "Multiply 81 by 3.", "tier_2": "81 × 3 = 243.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_power_of_two_instead_of_three"]
    }


# 10. Geometric halving sequence
def arch_10_geometric_halving_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "4; 2"
    prompt = (
        "Extend the sequence by two more terms:\n"
        "\\[ 64;\\; 32;\\; 16;\\; 8;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** Each term is divided by 2 (halved):\n"
        "$$64 \\div 2 = 32, \\quad 32 \\div 2 = 16, \\quad 16 \\div 2 = 8$$\n\n"
        "**Step 2:** Next two terms:\n"
        "- 5th term: \\(8 \\div 2 = 4\\)\n"
        "- 6th term: \\(4 \\div 2 = 2\\)\n\n"
        "Next two terms: **\\(4;\\; 2\\)**."
    )
    return {
        "id": f"g7_num_10_{rng.randint(100000, 999999)}",
        "subskill": "10_geometric_halving_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_10",
        "hints": {"tier_1": "Divide by 2 each time.", "tier_2": "8 / 2 = 4, 4 / 2 = 2.", "tier_3": ans},
        "misconception_tags": ["halving_division_arithmetic_error"]
    }


# 11. Geometric dividing by ten powers
def arch_11_geometric_dividing_by_ten_powers(rng: random.Random) -> Dict[str, Any]:
    ans = "1; 0,1"
    prompt = (
        "Write down the next two terms in the power-of-ten pattern:\n"
        "\\[ 10000;\\; 1000;\\; 100;\\; 10;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** Each term is divided by 10 (decreasing power of 10):\n"
        "$$10 \\div 10 = 1$$\n"
        "$$1 \\div 10 = 0{,}1$$\n\n"
        "Next two terms: **1; 0,1**."
    )
    return {
        "id": f"g7_num_11_{rng.randint(100000, 999999)}",
        "subskill": "11_geometric_dividing_by_ten_powers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_11",
        "hints": {"tier_1": "Divide by 10.", "tier_2": "10 / 10 = 1, then 1 / 10 = 0,1.", "tier_3": ans},
        "misconception_tags": ["thinking_pattern_stops_at_zero"]
    }


# 12. Square numbers sequence
def arch_12_square_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "49; 64"
    prompt = (
        "The sequence of square numbers begins:\n"
        "\\[ 1;\\; 4;\\; 9;\\; 16;\\; 25;\\; 36;\\; \\dots \\]\n\n"
        "Write down the 7th and 8th square numbers."
    )
    sol = (
        "**Step 1:** The \\(n\\)-th term is given by \\(T_n = n^2\\):\n"
        "- 7th term: \\(7^2 = 7 \\times 7 = \\mathbf{49}\\)\n"
        "- 8th term: \\(8^2 = 8 \\times 8 = \\mathbf{64}\\)\n\n"
        "Result: **\\(49;\\; 64\\)**."
    )
    return {
        "id": f"g7_num_12_{rng.randint(100000, 999999)}",
        "subskill": "12_square_numbers_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_12",
        "hints": {"tier_1": "Calculate 7 × 7 and 8 × 8.", "tier_2": "49 and 64.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_two_instead_of_squaring"]
    }


# 13. Cubic numbers sequence
def arch_13_cubic_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "216"
    prompt = (
        "Determine the 6th term of the sequence of cubic numbers:\n"
        "\\[ 1;\\; 8;\\; 27;\\; 64;\\; 125;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** The formula is \\(T_n = n^3\\).\n\n"
        "**Step 2:** For \\(n = 6\\):\n"
        "$$T_6 = 6^3 = 6 \\times 6 \\times 6 = 36 \\times 6 = \\mathbf{216}$$"
    )
    return {
        "id": f"g7_num_13_{rng.randint(100000, 999999)}",
        "subskill": "13_cubic_numbers_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_13",
        "hints": {"tier_1": "Calculate 6 × 6 × 6.", "tier_2": "36 × 6 = 216.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_three_instead_of_cubing"]
    }


# 14. Triangular numbers sequence
def arch_14_triangular_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    ans = "28"
    prompt = (
        "Triangular numbers represent dots arranged in an equilateral triangle:\n"
        "\\[ 1;\\; 3;\\; 6;\\; 10;\\; 15;\\; 21;\\; \\dots \\]\n\n"
        "What is the 7th triangular number?"
    )
    sol = (
        "**Step 1:** Notice the differences between consecutive terms increase by 1:\n"
        "- \\(+2, +3, +4, +5, +6\\)\n\n"
        "**Step 2:** To get the 7th term, add 7 to the 6th term (21):\n"
        "$$T_7 = 21 + 7 = \\mathbf{28}$$"
    )
    return {
        "id": f"g7_num_14_{rng.randint(100000, 999999)}",
        "subskill": "14_triangular_numbers_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_14",
        "hints": {"tier_1": "The differences are +2, +3, +4, +5, +6. Next difference is +7.", "tier_2": "21 + 7 = 28.", "tier_3": ans},
        "misconception_tags": ["triangular_numbers_step_addition_error"]
    }


# 15. Fibonacci sequence addition rule
def arch_15_fibonacci_sequence_addition_rule(rng: random.Random) -> Dict[str, Any]:
    ans = "34; 55"
    prompt = (
        "In the Fibonacci progression, each entry equals the sum of the two preceding entries:\n"
        "\\[ 1;\\; 1;\\; 2;\\; 3;\\; 5;\\; 8;\\; 13;\\; 21;\\; ... \\]\n\n"
        "Calculate the 9th and 10th entries."
    )
    sol = (
        "**Step 1:** Calculate 9th term:\n"
        "$$13 + 21 = \\mathbf{34}$$\n\n"
        "**Step 2:** Calculate 10th term:\n"
        "$$21 + 34 = \\mathbf{55}$$\n\n"
        "Result: **\\(34;\\; 55\\)**."
    )
    return {
        "id": f"g7_num_15_{rng.randint(100000, 999999)}",
        "subskill": "15_fibonacci_sequence_addition_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_15",
        "hints": {"tier_1": "Add the last two numbers: 13 + 21.", "tier_2": "34, then 21 + 34 = 55.", "tier_3": ans},
        "misconception_tags": ["fibonacci_summing_wrong_terms_error"]
    }


# 16. General rule verbal description
def arch_16_general_rule_verbal_description(rng: random.Random) -> Dict[str, Any]:
    start = 5
    d = 4
    ans = "Start at 5, add 4 each time"
    prompt = (
        "Describe the rule for this sequence in words:\n"
        "\\[ 5;\\; 9;\\; 13;\\; 17;\\; 21;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** The first term is 5.\n"
        "**Step 2:** Each subsequent term increases by 4.\n\n"
        "Rule in words: **Start at 5, add 4 each time**."
    )
    return {
        "id": f"g7_num_16_{rng.randint(100000, 999999)}",
        "subskill": "16_general_rule_verbal_description",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_num_16",
        "hints": {"tier_1": "What is the starting number and step?", "tier_2": "Starts at 5, add 4.", "tier_3": ans},
        "misconception_tags": ["verbal_rule_omitting_starting_value"]
    }


# 17. General formula positive constant Tn = dn + c
def arch_17_formula_from_numeric_rule(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6])
    c = rng.randint(2, 6)
    terms = [d * n + c for n in range(1, 5)]
    ans = f"Tn = {d}n + {c}"
    prompt = (
        f"Derive the algebraic formula \\(T_n\\) for the arithmetic progression:\n"
        f"\\[ {terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; ... \\]"
    )
    sol = (
        f"**Step 1:** Find common difference \\(d\\):\n"
        f"$$d = {terms[1]} - {terms[0]} = {d}$$\n"
        f"So the variable part is \\({d}n\\).\n\n"
        f"**Step 2:** Determine the constant offset \\(c\\) using \\(T_1 = {terms[0]}\\):\n"
        f"$${d}(1) + c = {terms[0]} \\implies {d} + c = {terms[0]} \\implies c = {c}$$\n\n"
        f"General rule: **\\(T_n = {d}n + {c}\\)**."
    )
    return {
        "id": f"g7_num_17_{rng.randint(100000, 999999)}",
        "subskill": "17_formula_from_numeric_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_17",
        "hints": {"tier_1": f"Difference is {d}, so {d}n.", "tier_2": f"When n=1, {d}(1) + c = {terms[0]}, so c = {c}.", "tier_3": ans},
        "misconception_tags": ["confusing_first_term_with_constant_offset"]
    }


# 18. General formula negative constant
def arch_18_general_formula_negative_constant(rng: random.Random) -> Dict[str, Any]:
    d = 4
    c = -1
    terms = [d * n + c for n in range(1, 5)]  # 3, 7, 11, 15
    ans = "Tn = 4n - 1"
    prompt = (
        f"Find the general term formula \\(T_n\\) for:\n"
        f"\\[ {terms[0]};\\; {terms[1]};\\; {terms[2]};\\; {terms[3]};\\; \\dots \\]"
    )
    sol = (
        f"**Step 1:** Common difference \\(d = {terms[1]} - {terms[0]} = 4\\).\n\n"
        f"**Step 2:** When \\(n = 1\\):\n"
        f"$$4(1) + c = 3 \\implies c = 3 - 4 = -1$$\n\n"
        f"Formula: **\\(T_n = 4n - 1\\)**."
    )
    return {
        "id": f"g7_num_18_{rng.randint(100000, 999999)}",
        "subskill": "18_general_formula_negative_constant",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_18",
        "hints": {"tier_1": "d = 4.", "tier_2": "4(1) - 1 = 3.", "tier_3": ans},
        "misconception_tags": ["sign_error_in_formula_constant_calculation"]
    }


# 19. General formula descending negative difference
def arch_19_general_formula_descending_negative_difference(rng: random.Random) -> Dict[str, Any]:
    # 17, 14, 11, 8 -> Tn = -3n + 20
    ans = "Tn = -3n + 20"
    prompt = (
        "Write down the formula for the general term \\(T_n\\) of the descending sequence:\n"
        "\\[ 17;\\; 14;\\; 11;\\; 8;\\; \\dots \\]"
    )
    sol = (
        "**Step 1:** Find difference: \\(14 - 17 = -3\\), so variable term is \\(-3n\\).\n\n"
        "**Step 2:** Find constant offset: when \\(n = 1\\):\n"
        "$$-3(1) + c = 17 \\implies c = 17 + 3 = 20$$\n\n"
        "General formula: **\\(T_n = -3n + 20\\)** (or \\(20 - 3n\\))."
    )
    return {
        "id": f"g7_num_19_{rng.randint(100000, 999999)}",
        "subskill": "19_general_formula_descending_negative_difference",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_19",
        "hints": {"tier_1": "Difference is -3.", "tier_2": "-3(1) + 20 = 17.", "tier_3": ans},
        "misconception_tags": ["negative_difference_formula_setup_error"]
    }


# 20. Calculate 10th term using rule
def arch_20_calculate_10th_term_using_rule(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(2, 7)
    ans_val = m * 10 + c
    ans = str(ans_val)
    prompt = (
        f"A number pattern has the general rule \\(T_n = {m}n + {c}\\).\n\n"
        f"Calculate the 10th term (\\(T_{{10}}\\)) of this sequence."
    )
    sol = (
        f"**Step 1:** Substitute \\(n = 10\\) into the rule:\n"
        f"$$T_{{10}} = {m}(10) + {c}$$\n\n"
        f"**Step 2:** Multiply and add:\n"
        f"$$T_{{10}} = {m * 10} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_num_20_{rng.randint(100000, 999999)}",
        "subskill": "20_calculate_10th_term_using_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_20",
        "hints": {"tier_1": f"Replace n with 10.", "tier_2": f"{m}(10) + {c} = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["adding_before_multiplying_in_term_formula"]
    }


# 21. Calculate 20th term using rule
def arch_21_calculate_20th_term_using_rule(rng: random.Random) -> Dict[str, Any]:
    m = 6
    c = 2
    ans_val = m * 20 - c  # 118
    ans = str(ans_val)
    prompt = (
        f"Given the general rule \\(T_n = {m}n - {c}\\), find the value of \\(T_{{20}}\\)."
    )
    sol = (
        f"**Step 1:** Substitute \\(n = 20\\):\n"
        f"$$T_{{20}} = {m}(20) - {c}$$\n\n"
        f"**Step 2:** Calculate:\n"
        f"$$T_{{20}} = {m * 20} - {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_num_21_{rng.randint(100000, 999999)}",
        "subskill": "21_calculate_20th_term_using_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_21",
        "hints": {"tier_1": "Replace n with 20.", "tier_2": f"6(20) - 2 = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["arithmetic_subtraction_in_formula_evaluation"]
    }


# 22. Calculate 50th term using rule
def arch_22_calculate_50th_term_using_rule(rng: random.Random) -> Dict[str, Any]:
    ans = "107"
    prompt = (
        "The \\(n\\)-th term of a sequence is \\(T_n = 2n + 7\\).\n\n"
        "Calculate the 50th term (\\(T_{50}\\))."
    )
    sol = (
        "**Step 1:** Substitute \\(n = 50\\):\n"
        "$$T_{50} = 2(50) + 7$$\n\n"
        "**Step 2:** Multiply and add:\n"
        "$$T_{50} = 100 + 7 = \\mathbf{107}$$"
    )
    return {
        "id": f"g7_num_22_{rng.randint(100000, 999999)}",
        "subskill": "22_calculate_50th_term_using_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_22",
        "hints": {"tier_1": "Substitute 50 for n.", "tier_2": "2(50) + 7 = 107.", "tier_3": ans},
        "misconception_tags": ["mental_math_large_multiple_error"]
    }


# 23. Calculate 100th term using rule
def arch_23_calculate_100th_term_using_rule(rng: random.Random) -> Dict[str, Any]:
    ans = "401"
    prompt = (
        "Consider the sequence \\(5;\\; 9;\\; 13;\\; 17;\\; \\dots\\) which has rule \\(T_n = 4n + 1\\).\n\n"
        "Calculate the value of the 100th term (\\(T_{100}\\))."
    )
    sol = (
        "**Step 1:** Substitute \\(n = 100\\) into the rule:\n"
        "$$T_{100} = 4(100) + 1$$\n\n"
        "**Step 2:** Calculate:\n"
        "$$T_{100} = 400 + 1 = \\mathbf{401}$$"
    )
    return {
        "id": f"g7_num_23_{rng.randint(100000, 999999)}",
        "subskill": "23_calculate_100th_term_using_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_23",
        "hints": {"tier_1": "4 × 100 + 1.", "tier_2": "400 + 1 = 401.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_ten_instead_of_hundred"]
    }


# 24. Find term position small target
def arch_24_find_term_position_numeric(rng: random.Random) -> Dict[str, Any]:
    # Tn = 4n + 1 = 37 -> 4n = 36 -> n = 9
    ans = "9"
    prompt = (
        "A sequence has general term \\(T_n = 4n + 1\\).\n\n"
        "Which position \\(n\\) in the sequence has a value equal to \\(37\\)?"
    )
    sol = (
        "**Step 1:** Set \\(T_n = 37\\):\n"
        "$$4n + 1 = 37$$\n\n"
        "**Step 2:** Solve for \\(n\\):\n"
        "$$4n = 37 - 1 = 36$$\n"
        "$$n = \\frac{36}{4} = \\mathbf{9}$$\n\n"
        "The 9th term has value 37."
    )
    return {
        "id": f"g7_num_24_{rng.randint(100000, 999999)}",
        "subskill": "24_find_term_position_numeric",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_24",
        "hints": {"tier_1": "Set 4n + 1 = 37.", "tier_2": "4n = 36, so n = 9.", "tier_3": ans},
        "misconception_tags": ["substituting_target_value_for_n_instead_of_tn"]
    }


# 25. Find term position large target
def arch_25_find_term_position_large_target(rng: random.Random) -> Dict[str, Any]:
    # Tn = 5n + 3 = 203 -> 5n = 200 -> n = 40
    ans = "40"
    prompt = (
        "Given the rule \\(T_n = 5n + 3\\), find the term number \\(n\\) for which \\(T_n = 203\\)."
    )
    sol = (
        "**Step 1:** Set up equation:\n"
        "$$5n + 3 = 203$$\n\n"
        "**Step 2:** Subtract 3:\n"
        "$$5n = 200$$\n\n"
        "**Step 3:** Divide by 5:\n"
        "$$n = \\frac{200}{5} = \\mathbf{40}$$\n\n"
        "The **40th** term equals 203."
    )
    return {
        "id": f"g7_num_25_{rng.randint(100000, 999999)}",
        "subskill": "25_find_term_position_large_target",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_num_25",
        "hints": {"tier_1": "5n = 203 - 3.", "tier_2": "n = 200 / 5 = 40.", "tier_3": ans},
        "misconception_tags": ["division_by_five_arithmetic_error"]
    }
