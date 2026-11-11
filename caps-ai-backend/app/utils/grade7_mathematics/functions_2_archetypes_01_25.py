"""Grade 7 Mathematics - Functions and Relationships 2: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 2.md
Focus: Function tables, linear rules y = mx + c, constant differences, inverse inputs, fractions, decimals, integers, and quadratic patterns.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Table linear forward fill consecutive x
def arch_01_table_linear_forward_fill_consecutive_x(rng: random.Random) -> Dict[str, Any]:
    # Rule: y = 3x + 2 for x in 1, 2, 3, 4
    m, c = 3, 2
    xs = [1, 2, 3, 4]
    ys = [m * x + c for x in xs]
    ans = str(ys[3])
    table_md = (
        f"| \\(x\\) (Input) | {xs[0]} | {xs[1]} | {xs[2]} | {xs[3]} |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| \\(y\\) (Output) | {ys[0]} | {ys[1]} | {ys[2]} | **?** |\n"
    )
    prompt = (
        f"Use the function rule \\(y = {m}x + {c}\\) to find the missing output value in the table:\n\n"
        f"{table_md}"
    )
    sol = (
        f"**Step 1:** Substitute \\(x = {xs[3]}\\) into the formula \\(y = {m}x + {c}\\):\n"
        f"$$y = {m}({xs[3]}) + {c} = {m * xs[3]} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn2_01_{rng.randint(100000, 999999)}",
        "subskill": "01_table_linear_forward_fill_consecutive_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_01",
        "hints": {"tier_1": f"Multiply {xs[3]} by {m} and add {c}.", "tier_2": f"3(4) + 2.", "tier_3": ans},
        "misconception_tags": ["arithmetic_substitution_error"]
    }


# 02. Table linear forward fill step size two
def arch_02_table_linear_forward_fill_step_size_two(rng: random.Random) -> Dict[str, Any]:
    m, c = 4, 5
    xs = [1, 3, 5, 7]
    ys = [m * x + c for x in xs]
    ans = str(ys[3])
    table_md = (
        f"| \\(x\\) | {xs[0]} | {xs[1]} | {xs[2]} | {xs[3]} |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| \\(y\\) | {ys[0]} | {ys[1]} | {ys[2]} | **?** |\n"
    )
    prompt = (
        f"Complete the table for the rule \\(y = {m}x + {c}\\) when \\(x = {xs[3]}\\):\n\n"
        f"{table_md}"
    )
    sol = (
        f"**Step 1:** Substitute \\(x = {xs[3]}\\):\n"
        f"$$y = {m}({xs[3]}) + {c} = {m * xs[3]} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn2_02_{rng.randint(100000, 999999)}",
        "subskill": "02_table_linear_forward_fill_step_size_two",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_02",
        "hints": {"tier_1": f"Evaluate {m}({xs[3]}) + {c}.", "tier_2": f"28 + 5 = {ans}.", "tier_3": ans},
        "misconception_tags": ["adding_constant_difference_without_checking_step_size"]
    }


# 03. Table linear forward fill large x
def arch_03_table_linear_forward_fill_large_x(rng: random.Random) -> Dict[str, Any]:
    m, c = 5, 1
    target_x = 50
    ans = str(m * target_x + c)
    prompt = (
        f"A table relates input \\(x\\) to output \\(y\\) with the rule \\(y = {m}x + {c}\\):\n\n"
        f"| \\(x\\) | 1 | 2 | 3 | 50 |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| \\(y\\) | {m+c} | {2*m+c} | {3*m+c} | **?** |\n\n"
        f"Calculate the output when \\(x = {target_x}\\)."
    )
    sol = (
        f"**Step 1:** Use the formula directly instead of extending one by one:\n"
        f"$$y = {m}({target_x}) + {c} = {m * target_x} + {c} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn2_03_{rng.randint(100000, 999999)}",
        "subskill": "03_table_linear_forward_fill_large_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_03",
        "hints": {"tier_1": f"Multiply 50 by {m} and add {c}.", "tier_2": f"250 + 1.", "tier_3": ans},
        "misconception_tags": ["attempting_recursive_addition_for_large_terms"]
    }


# 04. Table linear reverse solve single missing x
def arch_04_table_linear_reverse_solve_single_missing_x(rng: random.Random) -> Dict[str, Any]:
    m, c = 2, 7
    target_x = 8
    target_y = m * target_x + c  # 23
    ans = str(target_x)
    table_md = (
        f"| \\(x\\) | 1 | 2 | **?** |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| \\(y\\) | {m+c} | {2*m+c} | {target_y} |\n"
    )
    prompt = (
        f"The relationship between \\(x\\) and \\(y\\) is given by \\(y = {m}x + {c}\\).\n\n"
        f"{table_md}\n"
        f"Determine the missing input value \\(x\\) when \\(y = {target_y}\\)."
    )
    sol = (
        f"**Step 1:** Set up the equation:\n$${m}x + {c} = {target_y}$$\n\n"
        f"**Step 2:** Subtract {c} from both sides:\n$${m}x = {target_y} - {c} = {target_y - c}$$\n\n"
        f"**Step 3:** Divide by {m}:\n$$x = \\frac{{{target_y - c}}}{{{m}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_fn2_04_{rng.randint(100000, 999999)}",
        "subskill": "04_table_linear_reverse_solve_single_missing_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_04",
        "hints": {"tier_1": f"Subtract {c} from {target_y}.", "tier_2": f"Divide by {m}.", "tier_3": ans},
        "misconception_tags": ["substituting_y_into_x_variable"]
    }


# 05. Table linear reverse solve multiple missing x
def arch_05_table_linear_reverse_solve_multiple_missing_x(rng: random.Random) -> Dict[str, Any]:
    # Rule: y = 3x - 1. Find x for y = 14 and y = 29
    ans = "5 and 10"
    prompt = (
        "Given the function rule \\(y = 3x - 1\\), find the two input values \\(x_1\\) and \\(x_2\\) "
        "corresponding to outputs \\(y = 14\\) and \\(y = 29\\)."
    )
    sol = (
        "**Step 1:** For \\(y = 14\\):\n"
        "$$3x - 1 = 14 \\implies 3x = 15 \\implies x_1 = \\mathbf{5}$$\n\n"
        "**Step 2:** For \\(y = 29\\):\n"
        "$$3x - 1 = 29 \\implies 3x = 30 \\implies x_2 = \\mathbf{10}$$\n\n"
        "**Result:** 5 and 10"
    )
    return {
        "id": f"g7_fn2_05_{rng.randint(100000, 999999)}",
        "subskill": "05_table_linear_reverse_solve_multiple_missing_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn2_05",
        "hints": {"tier_1": "Add 1 then divide by 3 for each.", "tier_2": "15 / 3 = 5, 30 / 3 = 10.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_reverse"]
    }


# 06. Table find constant difference rule positive
def arch_06_table_find_constant_difference_rule_positive(rng: random.Random) -> Dict[str, Any]:
    # Table: x: 1, 2, 3, 4 -> y: 5, 9, 13, 17. Constant diff = +4
    ans = "4"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 5 | 9 | 13 | 17 |\n"
    )
    prompt = (
        f"Examine the table of values below:\n\n{table_md}\n"
        f"Determine the constant difference (step size) between consecutive output values."
    )
    sol = (
        "**Step 1:** Subtract consecutive \\(y\\)-values:\n"
        "$$9 - 5 = 4$$\n"
        "$$13 - 9 = 4$$\n"
        "$$17 - 13 = 4$$\n\n"
        "The constant difference is **4**."
    )
    return {
        "id": f"g7_fn2_06_{rng.randint(100000, 999999)}",
        "subskill": "06_table_find_constant_difference_rule_positive",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_06",
        "hints": {"tier_1": "Subtract the first y-value from the second.", "tier_2": "9 - 5 = 4.", "tier_3": ans},
        "misconception_tags": ["difference_calculation_slip"]
    }


# 07. Table find constant difference rule negative
def arch_07_table_find_constant_difference_rule_negative(rng: random.Random) -> Dict[str, Any]:
    # Table: x: 1, 2, 3, 4 -> y: 20, 17, 14, 11. Diff = -3
    ans = "-3"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 20 | 17 | 14 | 11 |\n"
    )
    prompt = (
        f"Examine the decreasing table of values:\n\n{table_md}\n"
        f"State the constant difference between consecutive \\(y\\)-values (including its sign)."
    )
    sol = (
        "**Step 1:** Subtract each term from the next:\n"
        "$$17 - 20 = -3$$\n"
        "$$14 - 17 = -3$$\n"
        "$$11 - 14 = -3$$\n\n"
        "The constant difference is **-3**."
    )
    return {
        "id": f"g7_fn2_07_{rng.randint(100000, 999999)}",
        "subskill": "07_table_find_constant_difference_rule_negative",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_07",
        "hints": {"tier_1": "Since values decrease, the difference is negative.", "tier_2": "17 - 20 = -3.", "tier_3": ans},
        "misconception_tags": ["omitting_negative_sign_in_decreasing_pattern"]
    }


# 08. Table find constant multiplier proportional
def arch_08_table_find_constant_multiplier_proportional(rng: random.Random) -> Dict[str, Any]:
    # y = 6x: 1->6, 2->12, 3->18, 4->24
    ans = "y = 6x"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 6 | 12 | 18 | 24 |\n"
    )
    prompt = (
        f"Determine the general formula relating \\(y\\) to \\(x\\) for this proportional table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Test the ratio \\(\\frac{y}{x}\\) for each pair:\n"
        "$$\\frac{6}{1} = 6, \\quad \\frac{12}{2} = 6, \\quad \\frac{18}{3} = 6, \\quad \\frac{24}{4} = 6$$\n\n"
        "**Step 2:** Formulate rule:\n"
        "Since each \\(y\\) is 6 times \\(x\\), the formula is **\\(y = 6x\\)**."
    )
    return {
        "id": f"g7_fn2_08_{rng.randint(100000, 999999)}",
        "subskill": "08_table_find_constant_multiplier_proportional",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_08",
        "hints": {"tier_1": "Divide y by x for each column.", "tier_2": "Ratio is constantly 6.", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_multiplying_rule"]
    }


# 09. Table find rule form mx plus c
def arch_09_table_find_rule_form_mx_plus_c(rng: random.Random) -> Dict[str, Any]:
    # y = 3x + 4: 1->7, 2->10, 3->13, 4->16
    ans = "y = 3x + 4"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 7 | 10 | 13 | 16 |\n"
    )
    prompt = (
        f"Find the algebraic rule relating \\(y\\) and \\(x\\) in the form \\(y = mx + c\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1: Find the multiplier \\(m\\) (constant difference):**\n"
        "$$10 - 7 = 3, \\quad 13 - 10 = 3 \\implies m = 3$$\n\n"
        "**Step 2: Find the constant \\(c\\):**\n"
        "When \\(x = 1\\), \\(3(1) = 3\\). To reach \\(y = 7\\), we add 4:\n"
        "$$c = 7 - 3 = 4$$\n\n"
        "**Conclusion:** The rule is **\\(y = 3x + 4\\)**."
    )
    return {
        "id": f"g7_fn2_09_{rng.randint(100000, 999999)}",
        "subskill": "09_table_find_rule_form_mx_plus_c",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_09",
        "hints": {"tier_1": "Constant difference is 3, so rule starts with 3x.", "tier_2": "When x = 1, 3(1) + c = 7, so c = 4.", "tier_3": ans},
        "misconception_tags": ["finding_difference_but_missing_constant_c"]
    }


# 10. Table find rule form mx minus c
def arch_10_table_find_rule_form_mx_minus_c(rng: random.Random) -> Dict[str, Any]:
    # y = 5x - 2: 1->3, 2->8, 3->13, 4->18
    ans = "y = 5x - 2"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 3 | 8 | 13 | 18 |\n"
    )
    prompt = (
        f"Determine the general equation for this table of values:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Constant difference: $$8 - 3 = 5 \\implies m = 5$$\n\n"
        "**Step 2:** For \\(x = 1\\): $$5(1) = 5$$. To get \\(y = 3\\), subtract 2:\n"
        "$$c = 3 - 5 = -2$$\n\n"
        "**Rule:** **\\(y = 5x - 2\\)**"
    )
    return {
        "id": f"g7_fn2_10_{rng.randint(100000, 999999)}",
        "subskill": "10_table_find_rule_form_mx_minus_c",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_10",
        "hints": {"tier_1": "Outputs increase by 5 each step (5x).", "tier_2": "5(1) - 2 = 3.", "tier_3": ans},
        "misconception_tags": ["sign_error_on_constant_c"]
    }


# 11. Table find initial value at x zero
def arch_11_table_find_initial_value_at_x_zero(rng: random.Random) -> Dict[str, Any]:
    # y = 4x + 6: x=0 -> y = 6
    ans = "6"
    table_md = (
        "| \\(x\\) | 0 | 1 | 2 | 3 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | **?** | 10 | 14 | 18 |\n"
    )
    prompt = (
        f"In the table below, what is the output value when \\(x = 0\\)?\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Observe constant difference: $$14 - 10 = 4$$.\n\n"
        "**Step 2:** Working backward from \\(x = 1\\) to \\(x = 0\\):\n"
        "$$y(0) = 10 - 4 = \\mathbf{6}$$\n\n"
        "*(Note: \\(y(0)\\) represents the constant term \\(c\\) in \\(y = 4x + 6\\))*."
    )
    return {
        "id": f"g7_fn2_11_{rng.randint(100000, 999999)}",
        "subskill": "11_table_find_initial_value_at_x_zero",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_11",
        "hints": {"tier_1": "Subtract the difference (4) from 10.", "tier_2": "10 - 4 = 6.", "tier_3": ans},
        "misconception_tags": ["assuming_y_is_zero_when_x_is_zero"]
    }


# 12. Table complete both missing x and y
def arch_12_table_complete_both_missing_x_and_y(rng: random.Random) -> Dict[str, Any]:
    # y = 2x + 3. Table: x=4 -> y=?, and y=21 -> x=?
    # y = 2(4)+3 = 11; x = (21-3)/2 = 9
    ans = "y = 11 and x = 9"
    table_md = (
        "| \\(x\\) | 1 | 2 | 4 | **p** |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 5 | 7 | **q** | 21 |\n"
    )
    prompt = (
        f"The table follows the linear rule \\(y = 2x + 3\\):\n\n{table_md}\n"
        f"Calculate the missing values **q** and **p**."
    )
    sol = (
        "**Step 1: Calculate \\(q\\) (forward evaluation at \\(x = 4\\)):**\n"
        "$$q = 2(4) + 3 = 8 + 3 = \\mathbf{11}$$\n\n"
        "**Step 2: Calculate \\(p\\) (reverse evaluation at \\(y = 21\\)):**\n"
        "$$2p + 3 = 21 \\implies 2p = 18 \\implies p = \\mathbf{9}$$\n\n"
        "**Result:** \\(q = 11\\) and \\(p = 9\\)"
    )
    return {
        "id": f"g7_fn2_12_{rng.randint(100000, 999999)}",
        "subskill": "12_table_complete_both_missing_x_and_y",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn2_12",
        "hints": {"tier_1": "Find q using 2(4) + 3.", "tier_2": "Solve 2p + 3 = 21.", "tier_3": ans},
        "misconception_tags": ["confusing_input_and_output_variables"]
    }


# 13. Table detect inconsistent outlier entry
def arch_13_table_detect_inconsistent_outlier_entry(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 3x + 1: x: 1, 2, 3, 4 -> y: 4, 7, 11, 13 (error is 11, should be 10)
    ans = "11 (should be 10)"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 4 | 7 | 11 | 13 |\n"
    )
    prompt = (
        f"A learner recorded the following table for the rule \\(y = 3x + 1\\):\n\n{table_md}\n"
        f"Identify the incorrect \\(y\\)-value and state what it should be."
    )
    sol = (
        "**Step 1:** Verify each pair against \\(y = 3x + 1\\):\n"
        "- \\(x = 1\\): \\(3(1) + 1 = 4\\) (correct)\n"
        "- \\(x = 2\\): \\(3(2) + 1 = 7\\) (correct)\n"
        "- \\(x = 3\\): \\(3(3) + 1 = 10 \\neq 11\\) (error!)\n"
        "- \\(x = 4\\): \\(3(4) + 1 = 13\\) (correct)\n\n"
        "**Conclusion:** The value **11** is incorrect; it should be **10**."
    )
    return {
        "id": f"g7_fn2_13_{rng.randint(100000, 999999)}",
        "subskill": "13_table_detect_inconsistent_outlier_entry",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_13",
        "hints": {"tier_1": "Test 3(3) + 1.", "tier_2": "3(3) + 1 = 10, not 11.", "tier_3": ans},
        "misconception_tags": ["pattern_anomaly_detection_failure"]
    }


# 14. Table fraction input halves
def arch_14_table_fraction_input_halves(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 4x: x = 1/2, 1, 1 1/2, 2 -> y = 2, 4, 6, 8
    ans = "6"
    table_md = (
        "| \\(x\\) | \\(\\frac{1}{2}\\) | 1 | \\(1\\frac{1}{2}\\) | 2 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 2 | 4 | **?** | 8 |\n"
    )
    prompt = (
        f"Complete the table for \\(y = 4x\\) when \\(x = 1\\frac{{1}}{{2}}\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Convert \\(1\\frac{1}{2}\\) to improper fraction \\(\\frac{3}{2}\\):\n\n"
        "**Step 2:** Multiply by 4:\n"
        "$$y = 4 \\times \\frac{3}{2} = \\frac{12}{2} = \\mathbf{6}$$"
    )
    return {
        "id": f"g7_fn2_14_{rng.randint(100000, 999999)}",
        "subskill": "14_table_fraction_input_halves",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_14",
        "hints": {"tier_1": "4 times 1,5 = 6.", "tier_2": "4 * 3/2 = 6.", "tier_3": ans},
        "misconception_tags": ["fraction_multiplication_in_tables"]
    }


# 15. Table fraction input quarters
def arch_15_table_fraction_input_quarters(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 8x + 1: x = 1/4 -> y = 8(1/4) + 1 = 2 + 1 = 3
    ans = "3"
    prompt = (
        "A table relates \\(x\\) and \\(y\\) through the rule \\(y = 8x + 1\\).\n\n"
        "Calculate the value of \\(y\\) when the input is a quarter (\\(x = \\frac{1}{4}\\))."
    )
    sol = (
        "**Step 1:** Multiply 8 by \\(\\frac{1}{4}\\):\n"
        "$$8 \\times \\frac{1}{4} = 2$$\n\n"
        "**Step 2:** Add 1:\n"
        "$$2 + 1 = \\mathbf{3}$$"
    )
    return {
        "id": f"g7_fn2_15_{rng.randint(100000, 999999)}",
        "subskill": "15_table_fraction_input_quarters",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_15",
        "hints": {"tier_1": "One quarter of 8 is 2.", "tier_2": "2 + 1 = 3.", "tier_3": ans},
        "misconception_tags": ["fraction_arithmetic_in_formulae"]
    }


# 16. Table decimal input step zero comma five
def arch_16_table_decimal_input_step_zero_comma_five(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 2x + 1: x: 0,5, 1,0, 1,5, 2,0 -> y: 2, 3, 4, 5
    ans = "4"
    table_md = (
        "| \\(x\\) | 0,5 | 1,0 | 1,5 | 2,0 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 2 | 3 | **?** | 5 |\n"
    )
    prompt = (
        f"Calculate the missing value in the decimal input table for \\(y = 2x + 1\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Substitute \\(x = 1,5\\):\n"
        "$$y = 2(1,5) + 1 = 3 + 1 = \\mathbf{4}$$"
    )
    return {
        "id": f"g7_fn2_16_{rng.randint(100000, 999999)}",
        "subskill": "16_table_decimal_input_step_zero_comma_five",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_16",
        "hints": {"tier_1": "Double 1,5 then add 1.", "tier_2": "3 + 1 = 4.", "tier_3": ans},
        "misconception_tags": ["decimal_multiplication_slip"]
    }


# 17. Table decimal multiplier rule
def arch_17_table_decimal_multiplier_rule(rng: random.Random) -> Dict[str, Any]:
    # Rule: y = 0,5x: 2->1, 4->2, 6->3, 8->4
    ans = "y = 0,5x"
    table_md = (
        "| \\(x\\) | 2 | 4 | 6 | 8 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 1 | 2 | 3 | 4 |\n"
    )
    prompt = (
        f"Find the formula for \\(y\\) in terms of \\(x\\) using decimal notation:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Observe that each \\(y\\) is half of \\(x\\):\n"
        "$$\\frac{1}{2} = 0,5$$\n\n"
        "**Step 2:** Formulate equation:\n"
        "$$y = \\mathbf{0,5x} \\quad (\\text{or } y = \\frac{1}{2}x)$$"
    )
    return {
        "id": f"g7_fn2_17_{rng.randint(100000, 999999)}",
        "subskill": "17_table_decimal_multiplier_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_17",
        "hints": {"tier_1": "Divide 1 by 2.", "tier_2": "0,5x.", "tier_3": ans},
        "misconception_tags": ["confusing_doubling_with_halving"]
    }


# 18. Table integer inputs including negatives
def arch_18_table_integer_inputs_including_negatives(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 2x - 3: x = -2 -> y = 2(-2) - 3 = -7
    ans = "-7"
    table_md = (
        "| \\(x\\) | -2 | -1 | 0 | 1 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | **?** | -5 | -3 | -1 |\n"
    )
    prompt = (
        f"Use the function rule \\(y = 2x - 3\\) to calculate the missing value when \\(x = -2\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Substitute \\(x = -2\\):\n"
        "$$y = 2(-2) - 3 = -4 - 3 = \\mathbf{-7}$$"
    )
    return {
        "id": f"g7_fn2_18_{rng.randint(100000, 999999)}",
        "subskill": "18_table_integer_inputs_including_negatives",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_18",
        "hints": {"tier_1": "2 * (-2) = -4.", "tier_2": "-4 - 3 = -7.", "tier_3": ans},
        "misconception_tags": ["negative_integer_multiplication_in_table"]
    }


# 19. Table negative linear gradient decreasing
def arch_19_table_negative_linear_gradient_decreasing(rng: random.Random) -> Dict[str, Any]:
    # Rule y = -3x + 10: x: 1->7, 2->4, 3->1, 4->-2
    ans = "y = -3x + 10"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 7 | 4 | 1 | -2 |\n"
    )
    prompt = (
        f"Find the algebraic formula \\(y = mx + c\\) for this decreasing function table:\n\n{table_md}"
    )
    sol = (
        "**Step 1: Constant difference:**\n"
        "$$4 - 7 = -3 \\implies m = -3$$\n\n"
        "**Step 2: Find \\(c\\):**\n"
        "When \\(x = 1\\), \\(-3(1) = -3\\). To reach \\(y = 7\\):\n"
        "$$c = 7 - (-3) = 10$$\n\n"
        "**Formula:** **\\(y = -3x + 10\\)**"
    )
    return {
        "id": f"g7_fn2_19_{rng.randint(100000, 999999)}",
        "subskill": "19_table_negative_linear_gradient_decreasing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_19",
        "hints": {"tier_1": "Difference is -3, so multiplier is -3.", "tier_2": "When x = 1, -3(1) + 10 = 7.", "tier_3": ans},
        "misconception_tags": ["missing_negative_gradient_in_table"]
    }


# 20. Table quadratic pattern square numbers
def arch_20_table_quadratic_pattern_square_numbers(rng: random.Random) -> Dict[str, Any]:
    # Rule y = x^2: 1->1, 2->4, 3->9, 4->16, 5->25
    ans = "25"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 | 5 |\n"
        "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 1 | 4 | 9 | 16 | **?** |\n"
    )
    prompt = (
        f"State the missing value in the square number table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Identify the rule by inspecting pairs:\n"
        "$$1^2 = 1, \\quad 2^2 = 4, \\quad 3^2 = 9, \\quad 4^2 = 16$$\n\n"
        "**Step 2:** Evaluate for \\(x = 5\\):\n"
        "$$y = 5^2 = 5 \\times 5 = \\mathbf{25}$$"
    )
    return {
        "id": f"g7_fn2_20_{rng.randint(100000, 999999)}",
        "subskill": "20_table_quadratic_pattern_square_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_20",
        "hints": {"tier_1": "Square the input 5.", "tier_2": "5 * 5 = 25.", "tier_3": ans},
        "misconception_tags": ["treating_square_pattern_as_linear"]
    }


# 21. Table cubic pattern cube numbers
def arch_21_table_cubic_pattern_cube_numbers(rng: random.Random) -> Dict[str, Any]:
    # Rule y = x^3: 1->1, 2->8, 3->27, 4->64
    ans = "64"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 1 | 8 | 27 | **?** |\n"
    )
    prompt = (
        f"Determine the missing output for the cubic relationship table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Identify cubic rule: \\(y = x^3\\)\n\n"
        "**Step 2:** For \\(x = 4\\):\n"
        "$$y = 4^3 = 4 \\times 4 \\times 4 = 16 \\times 4 = \\mathbf{64}$$"
    )
    return {
        "id": f"g7_fn2_21_{rng.randint(100000, 999999)}",
        "subskill": "21_table_cubic_pattern_cube_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_21",
        "hints": {"tier_1": "Multiply 4 by itself three times.", "tier_2": "4 * 4 * 4 = 64.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_3_instead_of_cubing"]
    }


# 22. Table pattern square plus constant
def arch_22_table_pattern_square_plus_constant(rng: random.Random) -> Dict[str, Any]:
    # Rule y = x^2 + 1: 1->2, 2->5, 3->10, 4->17
    ans = "17"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 2 | 5 | 10 | **?** |\n"
    )
    prompt = (
        f"Find the output value for \\(x = 4\\) following the rule \\(y = x^2 + 1\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Square 4:\n$$4^2 = 16$$\n\n"
        "**Step 2:** Add 1:\n$$16 + 1 = \\mathbf{17}$$"
    )
    return {
        "id": f"g7_fn2_22_{rng.randint(100000, 999999)}",
        "subskill": "22_table_pattern_square_plus_constant",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_22",
        "hints": {"tier_1": "4 squared is 16.", "tier_2": "16 + 1 = 17.", "tier_3": ans},
        "misconception_tags": ["squaring_precedence_error"]
    }


# 23. Table pattern double and square
def arch_23_table_pattern_double_and_square(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 2x^2: x = 3 -> 2(9) = 18
    ans = "18"
    prompt = (
        "A function table follows the rule \\(y = 2x^2\\).\n\n"
        "Calculate the output \\(y\\) when the input is \\(x = 3\\)."
    )
    sol = (
        "**Step 1:** Apply exponent first (BODMAS):\n"
        "$$3^2 = 9$$\n\n"
        "**Step 2:** Multiply by 2:\n"
        "$$y = 2 \\times 9 = \\mathbf{18}$$"
    )
    return {
        "id": f"g7_fn2_23_{rng.randint(100000, 999999)}",
        "subskill": "23_table_pattern_double_and_square",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_23",
        "hints": {"tier_1": "Square 3 first to get 9.", "tier_2": "2 * 9 = 18.", "tier_3": ans},
        "misconception_tags": ["multiplying_before_squaring"]
    }


# 24. Table geometric doubling sequence
def arch_24_table_geometric_doubling_sequence(rng: random.Random) -> Dict[str, Any]:
    # y = 2^x: 1->2, 2->4, 3->8, 4->16, 5->32
    ans = "32"
    table_md = (
        "| Step (\\(n\\)) | 1 | 2 | 3 | 4 | 5 |\n"
        "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
        "| Value (\\(T_n\\)) | 2 | 4 | 8 | 16 | **?** |\n"
    )
    prompt = (
        f"Determine the 5th term in this geometric doubling pattern:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Notice that each term is multiplied by 2 (doubled):\n"
        "$$2 \\times 2 = 4$$\n"
        "$$4 \\times 2 = 8$$\n"
        "$$8 \\times 2 = 16$$\n\n"
        "**Step 2:** Next term:\n"
        "$$16 \\times 2 = \\mathbf{32}$$"
    )
    return {
        "id": f"g7_fn2_24_{rng.randint(100000, 999999)}",
        "subskill": "24_table_geometric_doubling_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_24",
        "hints": {"tier_1": "Multiply the previous term by 2.", "tier_2": "16 * 2 = 32.", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_doubling"]
    }


# 25. Table geometric halving sequence
def arch_25_table_geometric_halving_sequence(rng: random.Random) -> Dict[str, Any]:
    # 64, 32, 16, 8, ? -> 4
    ans = "4"
    table_md = (
        "| Step | 1 | 2 | 3 | 4 | 5 |\n"
        "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
        "| Value | 64 | 32 | 16 | 8 | **?** |\n"
    )
    prompt = (
        f"Calculate the 5th term in the halving table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Each term is divided by 2:\n"
        "$$64 \\div 2 = 32, \\quad 32 \\div 2 = 16, \\quad 16 \\div 2 = 8$$\n\n"
        "**Step 2:** Fifth term:\n"
        "$$8 \\div 2 = \\mathbf{4}$$"
    )
    return {
        "id": f"g7_fn2_25_{rng.randint(100000, 999999)}",
        "subskill": "25_table_geometric_halving_sequence",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_25",
        "hints": {"tier_1": "Divide 8 by 2.", "tier_2": "8 / 2 = 4.", "tier_3": ans},
        "misconception_tags": ["halving_arithmetic_slip"]
    }
