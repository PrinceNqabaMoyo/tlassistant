"""Grade 7 Mathematics - Relationships Between Variables: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Relationships between variables.md
Focus: Constants vs variables, independent vs dependent, verbal-formula translation, table values, pattern representations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Constant vs variable definition and distinction
def arch_01_constant_vs_variable_definition_and_distinction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In mathematical modeling, explain the fundamental difference between a **constant quantity** "
        "and a **variable quantity**. Provide one clear example of each."
    )
    sol = (
        "**Step 1: Definitions:**\n"
        "- **Constant Quantity:** A value that does not change; it remains fixed throughout a situation or formula.\n"
        "- **Variable Quantity:** A value that can change, vary, or take on different values.\n\n"
        "**Step 2: Examples:**\n"
        "- **Constant:** The number of hours in a day (always 24) or the number of sides on a triangle (always 3).\n"
        "- **Variable:** The daily outdoor temperature or a person's age."
    )
    ans = "Constant is fixed; variable changes"
    return {
        "id": f"g7_rel_01_{rng.randint(100000, 999999)}",
        "subskill": "01_constant_vs_variable_definition_and_distinction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_01",
        "hints": {"tier_1": "Constant = stays the same, Variable = varies.", "tier_2": "Fixed vs changing.", "tier_3": ans},
        "misconception_tags": ["confusing_constant_with_variable"]
    }


# 02. Identify constant quantity in real world context
def arch_02_identify_constant_quantity_in_real_world_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A taxi charges a fixed base fee of R20 plus R12 per kilometre traveled.\n\n"
        "Which of these quantities is a **constant**?"
    )
    sol = (
        "**Step 1:** The R20 base fee does not change no matter how far you travel; it is charged once.\n\n"
        "**Conclusion:** The **fixed base fee of R20** is the constant."
    )
    ans = "The fixed base fee of R20"
    return {
        "id": f"g7_rel_02_{rng.randint(100000, 999999)}",
        "subskill": "02_identify_constant_quantity_in_real_world_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_02",
        "hints": {"tier_1": "Which number never changes?", "tier_2": "The R20 base fee.", "tier_3": ans},
        "misconception_tags": ["confusing_rate_with_fixed_constant"]
    }


# 03. Identify variable quantity in real world context
def arch_03_identify_variable_quantity_in_real_world_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A school purchases desks. Each desk costs R350. The school orders different numbers of desks each term.\n\n"
        "Identify the two quantities in this situation and state which one is a **variable**."
    )
    sol = (
        "**Step 1:** The two quantities are:\n"
        "1. The price per desk (R350) - Constant.\n"
        "2. The number of desks ordered (and total cost) - Variable.\n\n"
        "**Conclusion:** The **number of desks ordered** (and the total bill) are variable quantities."
    )
    ans = "The number of desks ordered (and total cost)"
    return {
        "id": f"g7_rel_03_{rng.randint(100000, 999999)}",
        "subskill": "03_identify_variable_quantity_in_real_world_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_03",
        "hints": {"tier_1": "Which value changes from term to term?", "tier_2": "The number of desks.", "tier_3": ans},
        "misconception_tags": ["overlooking_variable_quantities"]
    }


# 04. Distinguish constants and variables in school context
def arch_04_distinguish_constants_and_variables_in_school_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a high school, consider:\n"
        "A) The duration of a standard school period (45 minutes)\n"
        "B) The number of learners absent each day\n\n"
        "Classify each quantity as either a **constant** or a **variable**."
    )
    sol = (
        "**Step 1:** Quantity A is 45 minutes every day on the timetable: **Constant**.\n\n"
        "**Step 2:** Quantity B changes daily depending on illness and attendance: **Variable**.\n\n"
        "**Summary:** A = Constant; B = Variable"
    )
    ans = "A is Constant, B is Variable"
    return {
        "id": f"g7_rel_04_{rng.randint(100000, 999999)}",
        "subskill": "04_distinguish_constants_and_variables_in_school_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_04",
        "hints": {"tier_1": "45 minutes does not change; absentee count changes.", "tier_2": "A: Constant, B: Variable.", "tier_3": ans},
        "misconception_tags": ["contextual_classification_error"]
    }


# 05. Distinguish constants and variables in sports context
def arch_05_distinguish_constants_and_variables_in_sports_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a standard soccer match:\n"
        "1. The number of players on the field for one team at kickoff (11)\n"
        "2. The total number of goals scored in a match\n\n"
        "State which is constant and which is variable."
    )
    sol = (
        "**1. Number of players at kickoff:** Always 11 by official rules: **Constant**.\n\n"
        "**2. Total goals scored:** Differs each match (e.g. 0, 1, 3): **Variable**."
    )
    ans = "1 is Constant, 2 is Variable"
    return {
        "id": f"g7_rel_05_{rng.randint(100000, 999999)}",
        "subskill": "05_distinguish_constants_and_variables_in_sports_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_05",
        "hints": {"tier_1": "Rule numbers are constant; match scores vary.", "tier_2": "1. Constant; 2. Variable.", "tier_3": ans},
        "misconception_tags": ["sports_context_quantities_slip"]
    }


# 06. Independent variable concept input
def arch_06_independent_variable_concept_input(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain what makes a quantity an **independent variable** in a mathematical function."
    )
    sol = (
        "**Definition:**\n"
        "The **independent variable** is the input value that can be chosen freely or changed independently. "
        "Its value does not depend on the other variable, but instead dictates the outcome."
    )
    ans = "The input variable chosen freely that determines the output"
    return {
        "id": f"g7_rel_06_{rng.randint(100000, 999999)}",
        "subskill": "06_independent_variable_concept_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_06",
        "hints": {"tier_1": "It is the independent input quantity.", "tier_2": "Chosen freely.", "tier_3": ans},
        "misconception_tags": ["independent_variable_misconception"]
    }


# 07. Dependent variable concept output
def arch_07_dependent_variable_concept_output(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain what makes a quantity a **dependent variable** in a mathematical relationship."
    )
    sol = (
        "**Definition:**\n"
        "The **dependent variable** is the output quantity whose value changes in response to, or *depends upon*, "
        "the value of the independent variable."
    )
    ans = "The output variable whose value depends on the input"
    return {
        "id": f"g7_rel_07_{rng.randint(100000, 999999)}",
        "subskill": "07_dependent_variable_concept_output",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_07",
        "hints": {"tier_1": "It depends on the input.", "tier_2": "Output quantity.", "tier_3": ans},
        "misconception_tags": ["dependent_variable_misconception"]
    }


# 08. Identifying independent and dependent in car travel
def arch_08_identifying_independent_and_dependent_in_car_travel(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A car drives along the N1 highway at 100 km/h. Consider the distance traveled and the driving time.\n\n"
        "1. Which is the independent variable?\n"
        "2. Which is the dependent variable?"
    )
    sol = (
        "**Step 1:** Driving time proceeds independently: **Time is the independent variable**.\n\n"
        "**Step 2:** The total distance covered depends directly on how long you drive: **Distance is the dependent variable**.\n\n"
        "**Summary:** 1. Time; 2. Distance"
    )
    ans = "1. Time; 2. Distance"
    return {
        "id": f"g7_rel_08_{rng.randint(100000, 999999)}",
        "subskill": "08_identifying_independent_and_dependent_in_car_travel",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_08",
        "hints": {"tier_1": "Does distance depend on time, or time on distance?", "tier_2": "Distance depends on time.", "tier_3": ans},
        "misconception_tags": ["inverting_time_and_distance_dependencies"]
    }


# 09. Identifying independent and dependent in shopping
def arch_09_identifying_independent_and_dependent_in_shopping(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A customer buys kilograms of bananas at R15 per kilogram.\n\n"
        "State which variable is independent and which is dependent."
    )
    sol = (
        "**1. Independent variable:** The mass of bananas purchased in kg (customer chooses how much to buy).\n\n"
        "**2. Dependent variable:** The total price paid in Rand (depends on mass bought)."
    )
    ans = "Mass (kg) is independent, Total cost (R) is dependent"
    return {
        "id": f"g7_rel_09_{rng.randint(100000, 999999)}",
        "subskill": "09_identifying_independent_and_dependent_in_shopping",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_09",
        "hints": {"tier_1": "Cost depends on the amount bought.", "tier_2": "Mass = independent, Cost = dependent.", "tier_3": ans},
        "misconception_tags": ["shopping_variable_confusion"]
    }


# 10. Identifying independent and dependent in plant growth
def arch_10_identifying_independent_and_dependent_in_plant_growth(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A science experiment measures bean plant height every week for 6 weeks.\n\n"
        "Identify the independent variable and the dependent variable."
    )
    sol = (
        "**1. Independent variable:** Time in weeks (progresses on its own schedule).\n\n"
        "**2. Dependent variable:** Plant height in centimetres (changes as time passes)."
    )
    ans = "Time (weeks) is independent, Plant height (cm) is dependent"
    return {
        "id": f"g7_rel_10_{rng.randint(100000, 999999)}",
        "subskill": "10_identifying_independent_and_dependent_in_plant_growth",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_10",
        "hints": {"tier_1": "Time is controlled/recorded, height depends on time.", "tier_2": "Time = independent, Height = dependent.", "tier_3": ans},
        "misconception_tags": ["science_experiment_variable_inversion"]
    }


# 11. Identifying independent and dependent in mobile data
def arch_11_identifying_independent_and_dependent_in_mobile_data(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A user streams online videos. The amount of mobile data remaining on their package decreases "
        "as they watch more hours of video.\n\n"
        "Which variable depends on the other?"
    )
    sol = (
        "**Analysis:**\n"
        "The **mobile data remaining** depends on the **number of hours of video watched**.\n\n"
        "- Hours of video: Independent variable.\n"
        "- Data remaining: Dependent variable."
    )
    ans = "Data remaining depends on hours of video watched"
    return {
        "id": f"g7_rel_11_{rng.randint(100000, 999999)}",
        "subskill": "11_identifying_independent_and_dependent_in_mobile_data",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_11",
        "hints": {"tier_1": "Does data depend on hours, or hours on data?", "tier_2": "Data remaining depends on hours watched.", "tier_3": ans},
        "misconception_tags": ["mobile_data_dependence_slip"]
    }


# 12. Identifying independent and dependent in recipe scaling
def arch_12_identifying_independent_and_dependent_in_recipe_scaling(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A pancake recipe uses 2 cups of flour for every batch of 8 pancakes.\n\n"
        "If you want to make pancakes for a large gathering, what is the independent variable?"
    )
    sol = (
        "**Step 1:** You first decide how many people to feed (the number of pancakes desired).\n\n"
        "**Conclusion:** The **number of pancakes desired** is the independent variable, "
        "and the amount of flour required depends on that choice."
    )
    ans = "The number of pancakes desired"
    return {
        "id": f"g7_rel_12_{rng.randint(100000, 999999)}",
        "subskill": "12_identifying_independent_and_dependent_in_recipe_scaling",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_12",
        "hints": {"tier_1": "You choose the number of guests/pancakes first.", "tier_2": "Number of pancakes.", "tier_3": ans},
        "misconception_tags": ["recipe_scaling_inversion"]
    }


# 13. Verbal description translate to formula simple
def arch_13_verbal_description_translate_to_formula_simple(rng: random.Random) -> Dict[str, Any]:
    # "The output y is seven times the input x" -> y = 7x
    ans = "y = 7x"
    prompt = (
        "Translate the following verbal description into an algebraic formula:\n\n"
        "\"*The output \\(y\\) is seven times the input \\(x\\).*\""
    )
    sol = (
        "**Step 1:** Multiply \\(x\\) by 7:\n"
        "$$y = \\mathbf{7x}$$"
    )
    return {
        "id": f"g7_rel_13_{rng.randint(100000, 999999)}",
        "subskill": "13_verbal_description_translate_to_formula_simple",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_13",
        "hints": {"tier_1": "Write 7 multiplied by x.", "tier_2": "y = 7x.", "tier_3": ans},
        "misconception_tags": ["omitting_equals_sign_in_formula"]
    }


# 14. Verbal description translate to formula two step
def arch_14_verbal_description_translate_to_formula_two_step(rng: random.Random) -> Dict[str, Any]:
    # "Multiply the input x by 3 and add 5 to get y" -> y = 3x + 5
    ans = "y = 3x + 5"
    prompt = (
        "Write an equation for \\(y\\) in terms of \\(x\\):\n\n"
        "\"*Multiply the input \\(x\\) by 3, then add 5 to obtain the output \\(y\\).*\""
    )
    sol = (
        "**Step 1:** Multiply \\(x\\) by 3: \\(3x\\)\n\n"
        "**Step 2:** Add 5: \\(3x + 5\\)\n\n"
        "**Equation:** **\\(y = 3x + 5\\)**"
    )
    return {
        "id": f"g7_rel_14_{rng.randint(100000, 999999)}",
        "subskill": "14_verbal_description_translate_to_formula_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_14",
        "hints": {"tier_1": "3 times x, then + 5.", "tier_2": "y = 3x + 5.", "tier_3": ans},
        "misconception_tags": ["verbal_two_step_translation_slip"]
    }


# 15. Verbal description translate to formula brackets
def arch_15_verbal_description_translate_to_formula_brackets(rng: random.Random) -> Dict[str, Any]:
    # "Add 4 to the input x, then multiply the entire sum by 6 to get y" -> y = 6(x + 4)
    ans = "y = 6(x + 4)"
    prompt = (
        "Translate the following instruction into a formula using brackets:\n\n"
        "\"*Add 4 to the input \\(x\\), then multiply the entire sum by 6 to find \\(y\\).*\""
    )
    sol = (
        "**Step 1:** The sum of \\(x\\) and 4 is placed in brackets: \\((x + 4)\\)\n\n"
        "**Step 2:** Multiply the whole bracketed group by 6:\n"
        "$$y = \\mathbf{6(x + 4)}$$"
    )
    return {
        "id": f"g7_rel_15_{rng.randint(100000, 999999)}",
        "subskill": "15_verbal_description_translate_to_formula_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_15",
        "hints": {"tier_1": "Put (x + 4) in brackets and multiply by 6.", "tier_2": "y = 6(x + 4).", "tier_3": ans},
        "misconception_tags": ["omitting_brackets_in_sum_multiplication"]
    }


# 16. Formula translate to verbal description
def arch_16_formula_translate_to_verbal_description(rng: random.Random) -> Dict[str, Any]:
    # y = 5x - 2
    ans = "Multiply the input by 5, then subtract 2"
    prompt = (
        "Describe the formula \\(y = 5x - 2\\) in clear words."
    )
    sol = (
        "**Verbal translation:**\n"
        "\"*Multiply the input number by 5, and then subtract 2 from the product to get the output.*\""
    )
    return {
        "id": f"g7_rel_16_{rng.randint(100000, 999999)}",
        "subskill": "16_formula_translate_to_verbal_description",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_16",
        "hints": {"tier_1": "State the operations in order: 5x then - 2.", "tier_2": "Multiply by 5, then subtract 2.", "tier_3": ans},
        "misconception_tags": ["verbal_description_operation_order_error"]
    }


# 17. Table of variables forward evaluation consecutive
def arch_17_table_of_variables_forward_evaluation_consecutive(rng: random.Random) -> Dict[str, Any]:
    # y = 3x + 1 for x in 1, 2, 3 -> y = 4, 7, 10
    ans = "4, 7, 10"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | **?** | **?** | **?** |\n"
    )
    prompt = (
        f"Complete the output row for the relationship \\(y = 3x + 1\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** \\(x = 1 \\implies y = 3(1) + 1 = 4\\)\n\n"
        "**Step 2:** \\(x = 2 \\implies y = 3(2) + 1 = 7\\)\n\n"
        "**Step 3:** \\(x = 3 \\implies y = 3(3) + 1 = 10\\)\n\n"
        "**Outputs:** **4, 7, 10**"
    )
    return {
        "id": f"g7_rel_17_{rng.randint(100000, 999999)}",
        "subskill": "17_table_of_variables_forward_evaluation_consecutive",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_17",
        "hints": {"tier_1": "Evaluate 3(1)+1, 3(2)+1, 3(3)+1.", "tier_2": "4, 7, 10.", "tier_3": ans},
        "misconception_tags": ["batch_evaluation_error"]
    }


# 18. Table of variables forward evaluation stepped
def arch_18_table_of_variables_forward_evaluation_stepped(rng: random.Random) -> Dict[str, Any]:
    # y = 2x + 4. x = 2, 5, 8 -> y = 8, 14, 20
    ans = "8, 14, 20"
    table_md = (
        "| \\(x\\) | 2 | 5 | 8 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | **?** | **?** | **?** |\n"
    )
    prompt = (
        f"Calculate the outputs for the non-consecutive table under rule \\(y = 2x + 4\\):\n\n{table_md}"
    )
    sol = (
        "**Step 1:** \\(x = 2 \\implies 2(2) + 4 = 8\\)\n\n"
        "**Step 2:** \\(x = 5 \\implies 2(5) + 4 = 14\\)\n\n"
        "**Step 3:** \\(x = 8 \\implies 2(8) + 4 = 20\\)\n\n"
        "**Outputs:** **8, 14, 20**"
    )
    return {
        "id": f"g7_rel_18_{rng.randint(100000, 999999)}",
        "subskill": "18_table_of_variables_forward_evaluation_stepped",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_18",
        "hints": {"tier_1": "Substitute 2, 5, 8 into 2x + 4.", "tier_2": "8, 14, 20.", "tier_3": ans},
        "misconception_tags": ["assuming_x_step_is_one"]
    }


# 19. Table of variables forward evaluation large input
def arch_19_table_of_variables_forward_evaluation_large_input(rng: random.Random) -> Dict[str, Any]:
    # y = 6x - 5. For x = 40 -> 6(40) - 5 = 235
    ans = "235"
    prompt = (
        "The relationship between two variables is governed by \\(y = 6x - 5\\).\n\n"
        "Calculate the output \\(y\\) when the input is \\(x = 40\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = 40\\):\n"
        "$$y = 6(40) - 5 = 240 - 5 = \\mathbf{235}$$"
    )
    return {
        "id": f"g7_rel_19_{rng.randint(100000, 999999)}",
        "subskill": "19_table_of_variables_forward_evaluation_large_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_19",
        "hints": {"tier_1": "6 * 40 = 240.", "tier_2": "240 - 5 = 235.", "tier_3": ans},
        "misconception_tags": ["large_input_multiplication_slip"]
    }


# 20. Table of variables reverse calculation solve input
def arch_20_table_of_variables_reverse_calculation_solve_input(rng: random.Random) -> Dict[str, Any]:
    # y = 4x + 7. Find x when y = 47 -> 4x = 40 -> x = 10
    ans = "10"
    prompt = (
        "A relationship is described by \\(y = 4x + 7\\).\n\n"
        "Solve for the input \\(x\\) when the output is \\(y = 47\\)."
    )
    sol = (
        "**Step 1:** Set up equation: $$4x + 7 = 47$$\n\n"
        "**Step 2:** Subtract 7: $$4x = 40$$\n\n"
        "**Step 3:** Divide by 4: $$x = \\frac{40}{4} = \\mathbf{10}$$"
    )
    return {
        "id": f"g7_rel_20_{rng.randint(100000, 999999)}",
        "subskill": "20_table_of_variables_reverse_calculation_solve_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_20",
        "hints": {"tier_1": "Subtract 7 from 47, then divide by 4.", "tier_2": "40 / 4 = 10.", "tier_3": ans},
        "misconception_tags": ["reverse_linear_algebra_slip"]
    }


# 21. Table of variables finding the rule between rows
def arch_21_table_of_variables_finding_the_rule_between_rows(rng: random.Random) -> Dict[str, Any]:
    # 1->5, 2->8, 3->11 -> diff 3 -> y = 3x + 2
    ans = "y = 3x + 2"
    table_md = (
        "| \\(x\\) | 1 | 2 | 3 | 4 |\n"
        "| :--- | :---: | :---: | :---: | :---: |\n"
        "| \\(y\\) | 5 | 8 | 11 | 14 |\n"
    )
    prompt = (
        f"Find the algebraic formula connecting the top and bottom rows:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Find constant difference between consecutive \\(y\\)-values:\n"
        "$$8 - 5 = 3 \\implies m = 3$$\n\n"
        "**Step 2:** Determine constant \\(c\\):\n"
        "For \\(x = 1\\): \\(3(1) + c = 5 \\implies c = 2$$\n\n"
        "**Formula:** **\\(y = 3x + 2\\)**"
    )
    return {
        "id": f"g7_rel_21_{rng.randint(100000, 999999)}",
        "subskill": "21_table_of_variables_finding_the_rule_between_rows",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_21",
        "hints": {"tier_1": "Step size is 3 (3x).", "tier_2": "3(1) + 2 = 5.", "tier_3": ans},
        "misconception_tags": ["row_rule_detection_slip"]
    }


# 22. Table of variables identifying constant ratio
def arch_22_table_of_variables_identifying_constant_ratio(rng: random.Random) -> Dict[str, Any]:
    # 2->16, 3->24, 5->40. Ratio = 8
    ans = "8"
    table_md = (
        "| \\(x\\) | 2 | 3 | 5 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | 16 | 24 | 40 |\n"
    )
    prompt = (
        f"Calculate the constant ratio \\(\\frac{{y}}{{x}}\\) for this proportional relationship:\n\n{table_md}"
    )
    sol = (
        "**Step 1:** Divide each \\(y\\) by its corresponding \\(x\\):\n"
        "$$\\frac{16}{2} = 8, \\quad \\frac{24}{3} = 8, \\quad \\frac{40}{5} = 8$$\n\n"
        "The constant ratio is **8**."
    )
    return {
        "id": f"g7_rel_22_{rng.randint(100000, 999999)}",
        "subskill": "22_table_of_variables_identifying_constant_ratio",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_22",
        "hints": {"tier_1": "16 / 2 = 8.", "tier_2": "Ratio is 8.", "tier_3": ans},
        "misconception_tags": ["constant_ratio_inversion"]
    }


# 23. Match verbal table flow diagram representations
def arch_23_match_verbal_table_flow_diagram_representations(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6])
    c = rng.randint(2, 7)
    x_val = rng.randint(2, 5)
    y_val = m * x_val + c
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
        f'<text x="365" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Output y</text>'
        f'</svg>'
    )
    prompt = (
        f"A relationship is described in words as: \"*Multiply the input by {m}, then add {c}.*\"\n\n"
        f"1. Write the flow diagram operators in sequence.\n"
        f"2. State the formula \\(y\\) in terms of \\(x\\).\n"
        f"3. Find \\(y\\) when \\(x = {x_val}\\)."
    )
    sol = (
        f"**Part 1: Flow sequence:** \\([\\times {m}] \\longrightarrow [+ {c}]\\)\n\n"
        f"**Part 2: Formula:** \\(y = {m}x + {c}\\)\n\n"
        f"**Part 3: Evaluation:** \\(y = {m}({x_val}) + {c} = {m * x_val} + {c} = \\mathbf{{{y_val}}}\\)\n\n"
        f"**Summary:** 1. [× {m}] then [+ {c}]; 2. \\(y = {m}x + {c}\\); 3. {y_val}"
    )
    ans = f"1. [× {m}] then [+ {c}]; 2. y = {m}x + {c}; 3. {y_val}"
    return {
        "id": f"g7_rel_23_{rng.randint(100000, 999999)}",
        "subskill": "23_match_verbal_table_flow_diagram_representations",
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
        "learning_objective_id": "math_g7_rel_23",
        "hints": {"tier_1": f"Flow: x {m} then + {c}. Formula: {m}x + {c}. For x={x_val}: {y_val}.", "tier_2": "Follow each part.", "tier_3": ans},
        "misconception_tags": ["multi_representation_matching_slip"]
    }


# 24. Match pattern of tiles to variable relationship
def arch_24_match_pattern_of_tiles_to_variable_relationship(rng: random.Random) -> Dict[str, Any]:
    # CAPS Chapter 8: Red and yellow squares. 1 red -> 4 yellow, 2 red -> 6 yellow, 3 red -> 8 yellow -> y = 2r + 2
    ans = "y = 2r + 2"
    prompt = (
        "In a geometric tile pattern (CAPS Chapter 8):\n"
        "- 1 red square has 4 surrounding yellow squares.\n"
        "- 2 red squares have 6 surrounding yellow squares.\n"
        "- 3 red squares have 8 surrounding yellow squares.\n\n"
        "Write the formula relating the number of yellow squares (\\(y\\)) to the number of red squares (\\(r\\))."
    )
    sol = (
        "**Step 1:** Observe pattern:\n"
        "\\(r = 1 \\implies y = 4\\)\n"
        "\\(r = 2 \\implies y = 6\\)\n"
        "\\(r = 3 \\implies y = 8\\)\n\n"
        "**Step 2:** The yellow squares increase by 2 for each red square (\\(2r\\)).\n"
        "When \\(r = 1\\), \\(2(1) + 2 = 4\\).\n\n"
        "**Formula:** **\\(y = 2r + 2\\)**"
    )
    return {
        "id": f"g7_rel_24_{rng.randint(100000, 999999)}",
        "subskill": "24_match_pattern_of_tiles_to_variable_relationship",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_24",
        "hints": {"tier_1": "Yellow squares increase by 2 each time.", "tier_2": "y = 2r + 2.", "tier_3": ans},
        "misconception_tags": ["geometric_tile_pattern_formula_slip"]
    }


# 25. Match matchstick pattern to variable relationship
def arch_25_match_matchstick_pattern_to_variable_relationship(rng: random.Random) -> Dict[str, Any]:
    # Triangles: 1 triangle = 3 matches, 2 triangles = 5 matches, 3 = 7 matches -> M = 2n + 1
    ans = "M = 2n + 1"
    prompt = (
        "A row of connected matchstick triangles is formed:\n"
        "- 1 triangle requires 3 matchsticks.\n"
        "- 2 connected triangles require 5 matchsticks.\n"
        "- 3 connected triangles require 7 matchsticks.\n\n"
        "Determine the general formula for the number of matchsticks (\\(M\\)) needed for \\(n\\) triangles."
    )
    sol = (
        "**Step 1:** Constant difference between consecutive terms: $$5 - 3 = 2 \\implies 2n$$\n\n"
        "**Step 2:** For \\(n = 1\\): $$2(1) + c = 3 \\implies c = 1$$\n\n"
        "**Formula:** **\\(M = 2n + 1\\)**"
    )
    return {
        "id": f"g7_rel_25_{rng.randint(100000, 999999)}",
        "subskill": "25_match_matchstick_pattern_to_variable_relationship",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_25",
        "hints": {"tier_1": "Each new triangle adds 2 matchsticks.", "tier_2": "M = 2n + 1.", "tier_3": ans},
        "misconception_tags": ["matchstick_shared_side_miscount"]
    }
