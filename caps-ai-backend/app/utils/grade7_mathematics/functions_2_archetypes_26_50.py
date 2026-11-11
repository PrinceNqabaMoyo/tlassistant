"""Grade 7 Mathematics - Functions and Relationships 2: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Functions and relationships 2.md
Focus: Contextual tables (rates, conversions, finance, geometry), variables, proportional reasoning, comparing tables, and diagnostic autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Table matching verbal description
def arch_26_table_matching_verbal_description(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A verbal rule states: \"*The output is 3 less than four times the input.*\"\n\n"
        "1. Write the algebraic rule for \\(y\\) in terms of \\(x\\).\n"
        "2. Calculate the output \\(y\\) when the input \\(x = 6\\)."
    )
    sol = (
        "**Step 1:** Translate into algebraic equation:\n"
        "$$y = 4x - 3$$\n\n"
        "**Step 2:** Substitute \\(x = 6\\):\n"
        "$$y = 4(6) - 3 = 24 - 3 = \\mathbf{21}$$\n\n"
        "**Summary:** 1. \\(y = 4x - 3\\); 2. \\(y = 21\\)"
    )
    ans = "1. y = 4x - 3; 2. 21"
    return {
        "id": f"g7_fn2_26_{rng.randint(100000, 999999)}",
        "subskill": "26_table_matching_verbal_description",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_26",
        "hints": {"tier_1": "Translate '4 times input minus 3'.", "tier_2": "4(6) - 3 = 21.", "tier_3": ans},
        "misconception_tags": ["translating_less_than_subtraction_order"]
    }


# 27. Table translating rule to table values
def arch_27_table_translating_rule_to_table_values(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 2x + 5. Fill table for x = 0, 1, 2, 3 -> y = 5, 7, 9, 11
    ans = "5, 7, 9, 11"
    prompt = (
        "Construct the table of outputs for the rule \\(y = 2x + 5\\) for input values \\(x = 0, 1, 2, 3\\)."
    )
    sol = (
        "**Step 1:** Calculate each pair:\n"
        "- \\(x = 0\\): \\(y = 2(0) + 5 = \\mathbf{5}\\)\n"
        "- \\(x = 1\\): \\(y = 2(1) + 5 = \\mathbf{7}\\)\n"
        "- \\(x = 2\\): \\(y = 2(2) + 5 = \\mathbf{9}\\)\n"
        "- \\(x = 3\\): \\(y = 2(3) + 5 = \\mathbf{11}\\)\n\n"
        "**Table row:** 5, 7, 9, 11"
    )
    return {
        "id": f"g7_fn2_27_{rng.randint(100000, 999999)}",
        "subskill": "27_table_translating_rule_to_table_values",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_27",
        "hints": {"tier_1": "Substitute 0, 1, 2, 3 into 2x + 5.", "tier_2": "Outputs are 5, 7, 9, 11.", "tier_3": ans},
        "misconception_tags": ["batch_table_evaluation_slip"]
    }


# 28. Table cost of items bulk pricing
def arch_28_table_cost_of_items_bulk_pricing(rng: random.Random) -> Dict[str, Any]:
    # Exercise books cost R12 each. Find cost of 15 books.
    ans = "R180"
    table_md = (
        "| Number of Books (\\(n\\)) | 1 | 2 | 5 | 15 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Total Cost in Rand (\\(C\\)) | 12 | 24 | 60 | **?** |\n"
    )
    prompt = (
        f"Exercise books cost R12 each. Complete the pricing table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Rule: \\(C = 12n\\)\n\n"
        "**Step 2:** For \\(n = 15\\):\n"
        "$$C = 12 \\times 15 = \\mathbf{R180}$$"
    )
    return {
        "id": f"g7_fn2_28_{rng.randint(100000, 999999)}",
        "subskill": "28_table_cost_of_items_bulk_pricing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_28",
        "hints": {"tier_1": "Multiply 15 by 12.", "tier_2": "15 * 12 = 180.", "tier_3": ans},
        "misconception_tags": ["unit_rate_multiplication_error"]
    }


# 29. Table distance speed time constant speed
def arch_29_table_distance_speed_time_constant_speed(rng: random.Random) -> Dict[str, Any]:
    # Car travels at constant 80 km/h. Table: 1h->80, 2h->160, 3,5h->?
    ans = "280 km"
    table_md = (
        "| Time in hours (\\(t\\)) | 1 | 2 | 3 | 3,5 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Distance in km (\\(d\\)) | 80 | 160 | 240 | **?** |\n"
    )
    prompt = (
        f"A car travels at a steady 80 km/h. Calculate the distance covered in 3,5 hours:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Formula: \\(d = 80t\\)\n\n"
        "**Step 2:** For \\(t = 3,5\\):\n"
        "$$d = 80 \\times 3,5 = 80 \\times 3 + 80 \\times 0,5 = 240 + 40 = \\mathbf{280\\text{ km}}$$"
    )
    return {
        "id": f"g7_fn2_29_{rng.randint(100000, 999999)}",
        "subskill": "29_table_distance_speed_time_constant_speed",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_29",
        "hints": {"tier_1": "Multiply speed (80) by time (3,5).", "tier_2": "80 * 3,5 = 280.", "tier_3": ans},
        "misconception_tags": ["decimal_time_multiplication_slip"]
    }


# 30. Table conversion litres to millilitres
def arch_30_table_conversion_litres_to_millilitres(rng: random.Random) -> Dict[str, Any]:
    # 1 L = 1000 mL. 4,5 L -> 4500 mL
    ans = "4 500 mL"
    table_md = (
        "| Litres (\\(L\\)) | 1 | 2 | 3 | 4,5 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Millilitres (\\(mL\\)) | 1 000 | 2 000 | 3 000 | **?** |\n"
    )
    prompt = (
        f"Complete the metric capacity conversion table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Conversion rule: \\(mL = 1\\,000 \\times L\\)\n\n"
        "**Step 2:** For \\(L = 4,5\\):\n"
        "$$mL = 4,5 \\times 1\\,000 = \\mathbf{4\\,500\\text{ mL}}$$"
    )
    return {
        "id": f"g7_fn2_30_{rng.randint(100000, 999999)}",
        "subskill": "30_table_conversion_litres_to_millilitres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_30",
        "hints": {"tier_1": "Multiply by 1 000.", "tier_2": "4,5 * 1000 = 4 500.", "tier_3": ans},
        "misconception_tags": ["metric_conversion_power_of_ten_error"]
    }


# 31. Table conversion kilometres to metres
def arch_31_table_conversion_kilometres_to_metres(rng: random.Random) -> Dict[str, Any]:
    ans = "7 200 m"
    prompt = (
        "A runner records distance in kilometres (\\(k\\)) and metres (\\(m\\)).\n\n"
        "Rule: \\(m = 1\\,000k\\).\n"
        "Calculate the distance in metres for \\(k = 7,2\\text{ km}\\)."
    )
    sol = (
        "**Step 1:** Multiply by 1 000:\n"
        "$$7,2 \\times 1\\,000 = \\mathbf{7\\,200\\text{ m}}$$"
    )
    return {
        "id": f"g7_fn2_31_{rng.randint(100000, 999999)}",
        "subskill": "31_table_conversion_kilometres_to_metres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_31",
        "hints": {"tier_1": "1 km = 1 000 m.", "tier_2": "7,2 * 1 000 = 7 200.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_100_instead_of_1000"]
    }


# 32. Table perimeter of regular pentagons
def arch_32_table_perimeter_of_regular_pentagons(rng: random.Random) -> Dict[str, Any]:
    # Regular pentagon has 5 equal sides: P = 5s
    ans = "35 cm"
    table_md = (
        "| Side Length in cm (\\(s\\)) | 2 | 4 | 6 | 7 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Perimeter in cm (\\(P\\)) | 10 | 20 | 30 | **?** |\n"
    )
    prompt = (
        f"A regular pentagon has 5 equal sides. Complete the perimeter table for side length \\(s = 7\\text{{ cm}}\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Formula for regular pentagon perimeter: \\(P = 5s\\)\n\n"
        "**Step 2:** For \\(s = 7\\):\n"
        "$$P = 5 \\times 7 = \\mathbf{35\\text{ cm}}$$"
    )
    return {
        "id": f"g7_fn2_32_{rng.randint(100000, 999999)}",
        "subskill": "32_table_perimeter_of_regular_pentagons",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_32",
        "hints": {"tier_1": "A pentagon has 5 sides. P = 5s.", "tier_2": "5 * 7 = 35.", "tier_3": ans},
        "misconception_tags": ["confusing_pentagon_with_hexagon"]
    }


# 33. Table perimeter of regular hexagons
def arch_33_table_perimeter_of_regular_hexagons(rng: random.Random) -> Dict[str, Any]:
    ans = "54 cm"
    prompt = (
        "A regular hexagon has 6 equal sides with formula \\(P = 6s\\).\n\n"
        "Calculate the perimeter when each side measures 9 cm."
    )
    sol = (
        "**Step 1:** Multiply side length by 6:\n"
        "$$P = 6 \\times 9 = \\mathbf{54\\text{ cm}}$$"
    )
    return {
        "id": f"g7_fn2_33_{rng.randint(100000, 999999)}",
        "subskill": "33_table_perimeter_of_regular_hexagons",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_33",
        "hints": {"tier_1": "Hexagon has 6 sides.", "tier_2": "6 * 9 = 54.", "tier_3": ans},
        "misconception_tags": ["hexagon_side_count_error"]
    }


# 34. Table area of rectangles fixed width
def arch_34_table_area_of_rectangles_fixed_width(rng: random.Random) -> Dict[str, Any]:
    # Fixed width = 4 m. Area = 4 * l. For l = 12 -> 48 m^2
    ans = "48 m²"
    table_md = (
        "| Length in m (\\(l\\)) | 2 | 5 | 8 | 12 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Area in m² (\\(A\\)) | 8 | 20 | 32 | **?** |\n"
    )
    prompt = (
        f"A series of garden plots have a constant width of 4 metres:\n\n{table_md}\n"
        f"Calculate the area of a plot with length 12 metres."
    )
    sol = (
        "**Step 1:** Formula: \\(A = \\text{width} \\times \\text{length} = 4l\\)\n\n"
        "**Step 2:** For \\(l = 12\\):\n"
        "$$A = 4 \\times 12 = \\mathbf{48\\text{ m}^2}$$"
    )
    return {
        "id": f"g7_fn2_34_{rng.randint(100000, 999999)}",
        "subskill": "34_table_area_of_rectangles_fixed_width",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_34",
        "hints": {"tier_1": "Multiply width (4) by length (12).", "tier_2": "4 * 12 = 48.", "tier_3": ans},
        "misconception_tags": ["perimeter_formula_used_for_area"]
    }


# 35. Table cellphone plan cost comparison
def arch_35_table_cellphone_plan_cost_comparison(rng: random.Random) -> Dict[str, Any]:
    # Plan A: C = 2m (R2/min). Plan B: C = 50 + 1m (R50 fee + R1/min)
    # For m = 60 mins: A = 120, B = 50 + 60 = 110. Plan B is cheaper.
    ans = "Plan B (R110 vs R120)"
    prompt = (
        "Compare two cellphone billing options for 60 minutes of calls:\n\n"
        "- **Plan A:** No monthly fee, R2 per minute (\\(C = 2m\\))\n"
        "- **Plan B:** R50 monthly fee, R1 per minute (\\(C = 50 + m\\))\n\n"
        "Which plan is cheaper for 60 minutes of calls?"
    )
    sol = (
        "**Step 1: Calculate Plan A:**\n"
        "$$C_A = 2(60) = \\text{R120}$$\n\n"
        "**Step 2: Calculate Plan B:**\n"
        "$$C_B = 50 + 60 = \\text{R110}$$\n\n"
        "**Conclusion:** **Plan B** is cheaper (R110 vs R120)."
    )
    return {
        "id": f"g7_fn2_35_{rng.randint(100000, 999999)}",
        "subskill": "35_table_cellphone_plan_cost_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn2_35",
        "hints": {"tier_1": "Evaluate both costs for m = 60.", "tier_2": "120 vs 110.", "tier_3": ans},
        "misconception_tags": ["fixed_fee_comparison_misjudgment"]
    }


# 36. Table savings account growth constant deposit
def arch_36_table_savings_account_growth_constant_deposit(rng: random.Random) -> Dict[str, Any]:
    # Starts with R200, adds R50 each month: S = 200 + 50n. For n = 8 months -> 200 + 400 = 600
    ans = "R600"
    prompt = (
        "A learner opens a savings account with R200 and deposits R50 each month.\n\n"
        "Formula: \\(S = 200 + 50n\\), where \\(n\\) is the number of months.\n"
        "Calculate total savings after 8 months."
    )
    sol = (
        "**Step 1:** Substitute \\(n = 8\\):\n"
        "$$S = 200 + 50(8) = 200 + 400 = \\mathbf{R600}$$"
    )
    return {
        "id": f"g7_fn2_36_{rng.randint(100000, 999999)}",
        "subskill": "36_table_savings_account_growth_constant_deposit",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_36",
        "hints": {"tier_1": "Multiply 50 by 8, then add 200.", "tier_2": "200 + 400 = 600.", "tier_3": ans},
        "misconception_tags": ["adding_before_multiplying"]
    }


# 37. Table temperature degrees celsius change
def arch_37_table_temperature_degrees_celsius_change(rng: random.Random) -> Dict[str, Any]:
    # Temperature at 06:00 is -2°C, rises by 3°C each hour: T = -2 + 3h. At 10:00 (h = 4) -> -2 + 12 = 10°C
    ans = "10 °C"
    prompt = (
        "On a winter morning in Sutherland, the temperature at 06:00 was \\(-2^\\circ\\text{C}\\). "
        "It rose steadily by \\(3^\\circ\\text{C}\\) every hour.\n\n"
        "Calculate the temperature 4 hours later (at 10:00)."
    )
    sol = (
        "**Step 1:** Total rise in 4 hours:\n"
        "$$4 \\times 3^\\circ\\text{C} = 12^\\circ\\text{C}$$\n\n"
        "**Step 2:** Final temperature:\n"
        "$$-2 + 12 = \\mathbf{10^\\circ\\text{C}}$$"
    )
    return {
        "id": f"g7_fn2_37_{rng.randint(100000, 999999)}",
        "subskill": "37_table_temperature_degrees_celsius_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_37",
        "hints": {"tier_1": "-2 + (4 * 3).", "tier_2": "-2 + 12 = 10.", "tier_3": ans},
        "misconception_tags": ["negative_starting_temperature_slip"]
    }


# 38. Table identifying dependent and independent variables
def arch_38_table_identifying_dependent_and_independent_variables(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the cost formula \\(C = 15n + 25\\), where \\(n\\) is the number of tickets purchased "
        "and \\(C\\) is the total cost in Rand:\n\n"
        "1. Identify the **independent variable**.\n"
        "2. Identify the **dependent variable**."
    )
    sol = (
        "**Definitions:**\n"
        "- The **independent variable** is the input chosen freely (here, number of tickets \\(n\\)).\n"
        "- The **dependent variable** depends on the choice of input (here, total cost \\(C\\)).\n\n"
        "**Summary:** 1. \\(n\\) (number of tickets); 2. \\(C\\) (total cost)"
    )
    ans = "1. n (number of tickets); 2. C (total cost)"
    return {
        "id": f"g7_fn2_38_{rng.randint(100000, 999999)}",
        "subskill": "38_table_identifying_dependent_and_independent_variables",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_38",
        "hints": {"tier_1": "Which value determines the other?", "tier_2": "Cost depends on tickets.", "tier_3": ans},
        "misconception_tags": ["swapping_independent_and_dependent_variables"]
    }


# 39. Table identifying linear vs nonlinear
def arch_39_table_identifying_linear_vs_nonlinear(rng: random.Random) -> Dict[str, Any]:
    # Table A has constant diff (2, 5, 8, 11 -> diff 3). Table B has changing diff (1, 4, 9, 16 -> diff 3, 5, 7)
    ans = "Table A is linear; Table B is non-linear"
    prompt = (
        "Examine two relationship tables:\n\n"
        "- **Table A:** \\(x: 1, 2, 3, 4\\) and \\(y: 2, 5, 8, 11\\)\n"
        "- **Table B:** \\(x: 1, 2, 3, 4\\) and \\(y: 1, 4, 9, 16\\)\n\n"
        "Which table represents a **linear relationship** and which is **non-linear**? Justify your answer."
    )
    sol = (
        "**Step 1: Check Table A differences:**\n"
        "$$5 - 2 = 3, \\quad 8 - 5 = 3, \\quad 11 - 8 = 3$$\n"
        "Since the difference is constant (+3), **Table A is linear**.\n\n"
        "**Step 2: Check Table B differences:**\n"
        "$$4 - 1 = 3, \\quad 9 - 4 = 5, \\quad 16 - 9 = 7$$\n"
        "Since the differences are not constant (3, 5, 7), **Table B is non-linear**."
    )
    return {
        "id": f"g7_fn2_39_{rng.randint(100000, 999999)}",
        "subskill": "39_table_identifying_linear_vs_nonlinear",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_39",
        "hints": {"tier_1": "Linear requires a constant difference between consecutive terms.", "tier_2": "Table A diff is 3; Table B diff changes.", "tier_3": ans},
        "misconception_tags": ["assuming_all_increasing_tables_are_linear"]
    }


# 40. Table identifying direct proportion
def arch_40_table_identifying_direct_proportion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A relationship is directly proportional if the ratio \\(\\frac{y}{x}\\) is constant and the line passes through \\((0, 0)\\).\n\n"
        "Does the rule \\(y = 3x + 4\\) represent direct proportion? Explain why or why not."
    )
    sol = (
        "**Step 1:** Test the origin \\((0, 0)\\):\n"
        "When \\(x = 0\\), \\(y = 3(0) + 4 = 4 \\neq 0\\).\n\n"
        "**Step 2:** Test ratios \\(\\frac{y}{x}\\):\n"
        "For \\(x = 1\\), \\(\\frac{y}{x} = \\frac{7}{1} = 7\\).\n"
        "For \\(x = 2\\), \\(\\frac{y}{x} = \\frac{10}{2} = 5\\).\n"
        "The ratio is not constant.\n\n"
        "**Conclusion:** **No**, it is linear but not directly proportional because of the constant \\(+4\\)."
    )
    ans = "No, because y does not equal 0 when x = 0"
    return {
        "id": f"g7_fn2_40_{rng.randint(100000, 999999)}",
        "subskill": "40_table_identifying_direct_proportion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_40",
        "hints": {"tier_1": "Does it pass through (0, 0)?", "tier_2": "When x = 0, y = 4.", "tier_3": ans},
        "misconception_tags": ["confusing_linear_with_direct_proportionality"]
    }


# 41. Table ratio constant k equals y over x
def arch_41_table_ratio_constant_k_equals_y_over_x(rng: random.Random) -> Dict[str, Any]:
    # y = 14x. Find k = y/x = 14
    ans = "14"
    table_md = (
        "| \\(x\\) | 2 | 3 | 5 | 10 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 28 | 42 | 70 | 140 |\n"
    )
    prompt = (
        f"Calculate the constant of proportionality \\(k = \\frac{{y}}{{x}}\\) for this table:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Divide \\(y\\) by \\(x\\) for any column:\n"
        "$$k = \\frac{28}{2} = 14$$\n"
        "$$k = \\frac{42}{3} = 14$$\n\n"
        "The constant of proportionality is **14**."
    )
    return {
        "id": f"g7_fn2_41_{rng.randint(100000, 999999)}",
        "subskill": "41_table_ratio_constant_k_equals_y_over_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_41",
        "hints": {"tier_1": "Divide 28 by 2.", "tier_2": "k = 14.", "tier_3": ans},
        "misconception_tags": ["inverting_ratio_as_x_over_y"]
    }


# 42. Table flow diagram conversion to table
def arch_42_table_flow_diagram_conversion_to_table(rng: random.Random) -> Dict[str, Any]:
    # Diagram: x -> [* 3] -> [+ 4] -> y. Complete table for x = 1, 2, 3 -> 7, 10, 13
    ans = "7, 10, 13"
    prompt = (
        "A flow diagram processes inputs through \\([\\times 3]\\) followed by \\([+ 4]\\).\n\n"
        "Write down the table of values for outputs corresponding to inputs \\(x = 1, 2, 3\\)."
    )
    sol = (
        "**Step 1:** \\(x = 1 \\implies 1 \\times 3 + 4 = \\mathbf{7}\\)\n\n"
        "**Step 2:** \\(x = 2 \\implies 2 \\times 3 + 4 = \\mathbf{10}\\)\n\n"
        "**Step 3:** \\(x = 3 \\implies 3 \\times 3 + 4 = \\mathbf{13}\\)\n\n"
        "**Outputs:** 7, 10, 13"
    )
    return {
        "id": f"g7_fn2_42_{rng.randint(100000, 999999)}",
        "subskill": "42_table_flow_diagram_conversion_to_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_42",
        "hints": {"tier_1": "Apply 3x + 4 to 1, 2, 3.", "tier_2": "Outputs: 7, 10, 13.", "tier_3": ans},
        "misconception_tags": ["representation_translation_error"]
    }


# 43. Table converting table to flow diagram operators
def arch_43_table_converting_table_to_flow_diagram_operators(rng: random.Random) -> Dict[str, Any]:
    # Table: 1->5, 2->9, 3->13. Operators: [x 4], [+ 1]
    ans = "× 4 and + 1"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | 5 | 9 | 13 |\n"
    )
    prompt = (
        f"A flow diagram \\(x \\longrightarrow [\\text{{Op 1}}] \\longrightarrow [\\text{{Op 2}}] \\longrightarrow y\\) "
        f"generates this table:\n\n{table_md}\n"
        f"Determine the two operators in order."
    )
    sol = (
        "**Step 1:** Difference between outputs is $$9 - 5 = 4$$. This indicates an operation of **$\\times 4$**.\n\n"
        "**Step 2:** For \\(x = 1\\): $$1 \\times 4 = 4$$. To reach 5, add 1: **$+ 1$**.\n\n"
        "**Operators:** **$\\times 4$** followed by **$+ 1$**."
    )
    return {
        "id": f"g7_fn2_43_{rng.randint(100000, 999999)}",
        "subskill": "43_table_converting_table_to_flow_diagram_operators",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_43",
        "hints": {"tier_1": "Multiplier is 4.", "tier_2": "Second step is + 1.", "tier_3": ans},
        "misconception_tags": ["operator_order_swap"]
    }


# 44. Table evaluating rule with brackets
def arch_44_table_evaluating_rule_with_brackets(rng: random.Random) -> Dict[str, Any]:
    # y = 3(x + 2): for x = 4 -> 3(6) = 18
    ans = "18"
    prompt = (
        "A function table follows the rule \\(y = 3(x + 2)\\).\n\n"
        "Calculate the output \\(y\\) when the input is \\(x = 4\\)."
    )
    sol = (
        "**Step 1:** Calculate inside brackets first:\n"
        "$$x + 2 = 4 + 2 = 6$$\n\n"
        "**Step 2:** Multiply by 3:\n"
        "$$y = 3 \\times 6 = \\mathbf{18}$$"
    )
    return {
        "id": f"g7_fn2_44_{rng.randint(100000, 999999)}",
        "subskill": "44_table_evaluating_rule_with_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_44",
        "hints": {"tier_1": "Add 4 + 2 first.", "tier_2": "3 * 6 = 18.", "tier_3": ans},
        "misconception_tags": ["distributive_expansion_omission"]
    }


# 45. Table extending pattern to hundredth term
def arch_45_table_extending_pattern_to_hundredth_term(rng: random.Random) -> Dict[str, Any]:
    # y = 4n + 3. Find 100th term: 4(100) + 3 = 403
    ans = "403"
    table_md = (
        "| Position (\\(n\\)) | 1 | 2 | 3 | 100 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| Term (\\(T_n\\)) | 7 | 11 | 15 | **?** |\n"
    )
    prompt = (
        f"Extend the table to find the 100th term (\\(n = 100\\)):\n\n{table_md}"
    )
    sol = (
        "**Step 1: Determine the general formula \\(T_n\\):**\n"
        "Constant difference: $$11 - 7 = 4 \\implies 4n$$\n"
        "When \\(n = 1\\): $$4(1) + c = 7 \\implies c = 3$$\n"
        "General rule: $$T_n = 4n + 3$$\n\n"
        "**Step 2: Calculate \\(T_{100}\\):**\n"
        "$$T_{100} = 4(100) + 3 = 400 + 3 = \\mathbf{403}$$"
    )
    return {
        "id": f"g7_fn2_45_{rng.randint(100000, 999999)}",
        "subskill": "45_table_extending_pattern_to_hundredth_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn2_45",
        "hints": {"tier_1": "Find Tn = 4n + 3.", "tier_2": "Substitute n = 100.", "tier_3": ans},
        "misconception_tags": ["multiplying_first_term_by_100"]
    }


# 46. Table extending pattern to nth general term
def arch_46_table_extending_pattern_to_nth_general_term(rng: random.Random) -> Dict[str, Any]:
    # 2, 5, 8, 11 -> 3n - 1
    ans = "Tn = 3n - 1"
    table_md = (
        "| \\(n\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(T_n\\) | 2 | 5 | 8 | 11 |\n"
    )
    prompt = (
        f"Write down the formula for the general term \\(T_n\\) in terms of \\(n\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Common difference: $$5 - 2 = 3$$\n\n"
        "**Step 2:** Form: $$T_n = 3n + c$$\n"
        "For \\(n = 1\\): $$3(1) + c = 2 \\implies c = 2 - 3 = -1$$\n\n"
        "**Formula:** **\\(T_n = 3n - 1\\)**"
    )
    return {
        "id": f"g7_fn2_46_{rng.randint(100000, 999999)}",
        "subskill": "46_table_extending_pattern_to_nth_general_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_46",
        "hints": {"tier_1": "Difference is 3 -> 3n.", "tier_2": "3(1) - 1 = 2.", "tier_3": ans},
        "misconception_tags": ["confusing_n_with_term_value"]
    }


# 47. Table comparing two different tables same inputs
def arch_47_table_comparing_two_different_tables_same_inputs(rng: random.Random) -> Dict[str, Any]:
    # Table 1: y = 2x + 10. Table 2: y = 3x. For x = 10: T1 = 30, T2 = 30 (they match!). For x = 15: T1 = 40, T2 = 45
    ans = "Table 2 (45 vs 40)"
    prompt = (
        "Two functions are given for \\(x = 15\\):\n"
        "- Function 1: \\(y = 2x + 10\\)\n"
        "- Function 2: \\(y = 3x\\)\n\n"
        "Which function produces the larger output at \\(x = 15\\)?"
    )
    sol = (
        "**Step 1: Evaluate Function 1:**\n"
        "$$y_1 = 2(15) + 10 = 30 + 10 = 40$$\n\n"
        "**Step 2: Evaluate Function 2:**\n"
        "$$y_2 = 3(15) = 45$$\n\n"
        "**Conclusion:** **Function 2** produces the larger output (45 vs 40)."
    )
    return {
        "id": f"g7_fn2_47_{rng.randint(100000, 999999)}",
        "subskill": "47_table_comparing_two_different_tables_same_inputs",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn2_47",
        "hints": {"tier_1": "2(15) + 10 = 40.", "tier_2": "3(15) = 45.", "tier_3": ans},
        "misconception_tags": ["function_comparison_arithmetic_slip"]
    }


# 48. Table identifying intersection row where outputs match
def arch_48_table_identifying_intersection_row_where_outputs_match(rng: random.Random) -> Dict[str, Any]:
    # y1 = 2x + 6, y2 = 4x. Equal when 2x + 6 = 4x -> 2x = 6 -> x = 3, y = 12
    ans = "x = 3"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y_1 = 2x + 6\\) | 8 | 10 | 12 | 14 |\n"
        "| \\(y_2 = 4x\\) | 4 | 8 | 12 | 16 |\n"
    )
    prompt = (
        f"Inspect the comparison table:\n\n{table_md}\n"
        f"For what input value \\(x\\) do both functions produce identical outputs?"
    )
    sol = (
        "**Step 1:** Compare the rows for \\(y_1\\) and \\(y_2\\):\n"
        "At \\(x = 3\\), \\(y_1 = 12\\) and \\(y_2 = 12\\).\n\n"
        "**Answer:** \\(x = \\mathbf{3}\\)"
    )
    return {
        "id": f"g7_fn2_48_{rng.randint(100000, 999999)}",
        "subskill": "48_table_identifying_intersection_row_where_outputs_match",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn2_48",
        "hints": {"tier_1": "Look for the column where both y-values are equal.", "tier_2": "Column x = 3 has 12 and 12.", "tier_3": ans},
        "misconception_tags": ["reporting_output_instead_of_input_for_intersection"]
    }


# 49. Table reverse lookup maximum capacity budget
def arch_49_table_reverse_lookup_maximum_capacity_budget(rng: random.Random) -> Dict[str, Any]:
    # Tickets cost R35 each plus R50 booking fee: C = 35n + 50. Total budget R300. Max tickets: 35n + 50 <= 300 -> 35n <= 250 -> n <= 7,14 -> 7 tickets
    ans = "7 tickets"
    prompt = (
        "Concert tickets cost R35 each with a single booking fee of R50 (\\(C = 35n + 50\\)).\n\n"
        "A group has a maximum budget of R300. How many whole tickets can they buy at most?"
    )
    sol = (
        "**Step 1:** Set up the inequality:\n"
        "$$35n + 50 \\le 300$$\n\n"
        "**Step 2:** Subtract booking fee:\n"
        "$$35n \\le 250$$\n\n"
        "**Step 3:** Divide by 35:\n"
        "$$n \\le \\frac{250}{35} \\approx 7,14$$\n\n"
        "Since only whole tickets can be bought, the maximum number is **7 tickets** "
        "(cost: \\(35 \\times 7 + 50 = \\text{R295}\\))."
    )
    return {
        "id": f"g7_fn2_49_{rng.randint(100000, 999999)}",
        "subskill": "49_table_reverse_lookup_maximum_capacity_budget",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn2_49",
        "hints": {"tier_1": "Subtract R50 from R300.", "tier_2": "250 / 35 = 7,14.", "tier_3": ans},
        "misconception_tags": ["rounding_up_over_budget"]
    }


# 50. Table comprehensive diagnostic autopsy
def arch_50_table_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    # Table: 1->8, 2->13, 3->18, 4->23
    # 1. Formula: y = 5x + 3
    # 2. Output for x = 20 -> 5(20) + 3 = 103
    # 3. Input for y = 68 -> (68 - 3)/5 = 13
    ans = "1. y = 5x + 3; 2. 103; 3. 13"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | 8 | 13 | 18 | 23 |\n"
    )
    prompt = (
        f"Consider the table below:\n\n{table_md}\n"
        f"Perform a complete three-part analysis:\n"
        f"1. Determine the algebraic formula relating \\(y\\) to \\(x\\).\n"
        f"2. Calculate the output when \\(x = 20\\).\n"
        f"3. Calculate the input when \\(y = 68\\)."
    )
    sol = (
        "**Part 1: Formula:**\n"
        "Difference = $$13 - 8 = 5$$\n"
        "For \\(x = 1\\): $$5(1) + 3 = 8 \\implies \\mathbf{y = 5x + 3}$$\n\n"
        "**Part 2: Forward (\\(x = 20\\)):**\n"
        "$$y = 5(20) + 3 = 100 + 3 = \\mathbf{103}$$\n\n"
        "**Part 3: Reverse (\\(y = 68\\)):**\n"
        "$$5x + 3 = 68 \\implies 5x = 65 \\implies x = \\mathbf{13}$$\n\n"
        "**Summary:** 1. \\(y = 5x + 3\\); 2. \\(103\\); 3. \\(13\\)"
    )
    return {
        "id": f"g7_fn2_50_{rng.randint(100000, 999999)}",
        "subskill": "50_table_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_fn2_50",
        "hints": {"tier_1": "Part 1: 5x + 3; Part 2: 5(20) + 3; Part 3: (68 - 3) / 5.", "tier_2": "103 and 13.", "tier_3": ans},
        "misconception_tags": ["multi_part_table_autopsy_slip"]
    }
