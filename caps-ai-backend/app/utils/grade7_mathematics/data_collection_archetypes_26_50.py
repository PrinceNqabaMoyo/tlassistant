"""Grade 7 Mathematics - Collect, Organise and Summarise Data: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Collect organise and summarise data.md
"""
import random
from typing import Dict, Any, List


# 26. Mean from frequency table ungrouped
def arch_26_mean_from_frequency_table_ungrouped(rng: random.Random) -> Dict[str, Any]:
    # Scores 1..4 with frequencies 2, 3, 4, 1 -> total n = 10, sum = 2 + 6 + 12 + 4 = 24 -> mean = 2,4
    scores = [1, 2, 3, 4]
    freqs = [2, 3, 4, 1]
    products = [s * f for s, f in zip(scores, freqs)]
    total_f = sum(freqs)
    total_prod = sum(products)
    mean_val = total_prod / total_f
    m_str = f"{mean_val}".replace(".", ",")
    
    table_md = (
        "| Score ($x$) | Frequency ($f$) | $x \\times f$ |\n"
        "| :---: | :---: | :---: |\n"
        f"| 1 | {freqs[0]} | {products[0]} |\n"
        f"| 2 | {freqs[1]} | {products[1]} |\n"
        f"| 3 | {freqs[2]} | {products[2]} |\n"
        f"| 4 | {freqs[3]} | {products[3]} |\n"
        f"| **Total** | **{total_f}** | **{total_prod}** |\n"
    )
    prompt = (
        f"The table below records the quiz scores of a group of {total_f} learners:\n\n"
        f"| Score ($x$) | Frequency ($f$) |\n"
        f"| :---: | :---: |\n"
        f"| 1 | {freqs[0]} |\n"
        f"| 2 | {freqs[1]} |\n"
        f"| 3 | {freqs[2]} |\n"
        f"| 4 | {freqs[3]} |\n\n"
        f"Calculate the mean score for this group of learners."
    )
    sol = (
        f"**Step 1:** Multiply each score by its frequency to find the total points ($x \\times f$):\n\n"
        f"{table_md}\n"
        f"**Step 2:** Sum of products: $${total_prod}$$\n"
        f"Total number of learners: $${total_f}$$\n\n"
        f"**Step 3:** Calculate the mean:\n"
        f"$$\\text{{Mean}} = \\frac{{{total_prod}}}{{{total_f}}} = \\mathbf{{{m_str}}}$$"
    )
    ans = f"{m_str}"
    return {
        "id": f"g7_data_26_{rng.randint(100000, 999999)}",
        "subskill": "26_mean_from_frequency_table_ungrouped",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_data_26",
        "hints": {
            "tier_1": "Multiply each score by its frequency, then add the products.",
            "tier_2": f"Total points = {total_prod}, total learners = {total_f}.",
            "tier_3": ans
        },
        "misconception_tags": ["dividing_by_number_of_rows_instead_of_frequencies"]
    }


# 27. Median from frequency table
def arch_27_median_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    scores = [10, 11, 12, 13]
    freqs = [3, 5, 4, 3]  # total = 15. Middle is 8th item.
    # items 1-3: 10, items 4-8: 11 -> median is 11.
    prompt = (
        "The table below shows the ages of 15 learners:\n\n"
        "| Age ($x$) | Frequency ($f$) |\n"
        "| :---: | :---: |\n"
        "| 10 | 3 |\n"
        "| 11 | 5 |\n"
        "| 12 | 4 |\n"
        "| 13 | 3 |\n\n"
        "Find the **median** age."
    )
    sol = (
        "**Step 1: Total number of values ($n$):**\n"
        "$$n = 3 + 5 + 4 + 3 = 15$$\n\n"
        "**Step 2: Position of median:**\n"
        "$$\\text{Position} = \\frac{n + 1}{2} = \\frac{15 + 1}{2} = 8\\text{th value}$$\n\n"
        "**Step 3: Locate the 8th value using cumulative frequency:**\n"
        "- First 3 values are 10 (positions 1 to 3).\n"
        "- Next 5 values are 11 (positions 4 to 8).\n"
        "Therefore, the 8th value is **11**."
    )
    ans = "11"
    return {
        "id": f"g7_data_27_{rng.randint(100000, 999999)}",
        "subskill": "27_median_from_frequency_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_27",
        "hints": {
            "tier_1": "Find the middle position: (15 + 1) / 2 = 8th value.",
            "tier_2": "Count through frequencies: 3 are age 10, next 5 are age 11.",
            "tier_3": ans
        },
        "misconception_tags": ["median_of_unique_values_only"]
    }


# 28. Mode from frequency table
def arch_28_mode_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The table records the shoe sizes of 20 Grade 7 learners:\n\n"
        "| Shoe Size | Frequency |\n"
        "| :---: | :---: |\n"
        "| 4 | 3 |\n"
        "| 5 | 9 |\n"
        "| 6 | 6 |\n"
        "| 7 | 2 |\n\n"
        "State the **mode** (modal shoe size)."
    )
    sol = (
        "**Step 1:** The mode is the data value with the highest frequency.\n\n"
        "**Step 2:** Comparing frequencies: 3, 9, 6, 2.\n"
        "The highest frequency is 9, which corresponds to **Shoe Size 5**.\n\n"
        "*(Note: 9 is the frequency, not the mode itself!)*"
    )
    ans = "5"
    return {
        "id": f"g7_data_28_{rng.randint(100000, 999999)}",
        "subskill": "28_mode_from_frequency_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_data_28",
        "hints": {
            "tier_1": "Look for the shoe size with the largest frequency number.",
            "tier_2": "The largest frequency is 9, for size 5.",
            "tier_3": ans
        },
        "misconception_tags": ["confusing_mode_with_highest_frequency_value"]
    }


# 29. Range from frequency table
def arch_29_range_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The table shows the number of siblings learners have:\n\n"
        "| Siblings | Frequency |\n"
        "| :---: | :---: |\n"
        "| 0 | 5 |\n"
        "| 1 | 12 |\n"
        "| 2 | 8 |\n"
        "| 5 | 2 |\n\n"
        "Calculate the **range** of siblings."
    )
    sol = (
        "**Step 1:** The range is the difference between the maximum and minimum data values:\n"
        "$$\\text{Range} = \\text{Maximum Value} - \\text{Minimum Value}$$\n\n"
        "**Step 2:**\n"
        "$$\\text{Maximum} = 5, \\quad \\text{Minimum} = 0$$\n"
        "$$\\text{Range} = 5 - 0 = \\mathbf{5}$$"
    )
    ans = "5"
    return {
        "id": f"g7_data_29_{rng.randint(100000, 999999)}",
        "subskill": "29_range_from_frequency_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_29",
        "hints": {
            "tier_1": "Subtract the minimum number of siblings from the maximum.",
            "tier_2": "Range = 5 - 0.",
            "tier_3": ans
        },
        "misconception_tags": ["range_calculated_from_frequencies"]
    }


# 30. Missing frequency given total count
def arch_30_missing_frequency_given_total_count(rng: random.Random) -> Dict[str, Any]:
    total = 30
    known = [7, 11, 4]
    missing = total - sum(known)  # 30 - 22 = 8
    prompt = (
        f"A survey was conducted with a total of **{total}** participants regarding favourite fruit:\n\n"
        f"| Fruit | Frequency |\n"
        f"| :--- | :---: |\n"
        f"| Apple | {known[0]} |\n"
        f"| Banana | {known[1]} |\n"
        f"| Orange | $k$ |\n"
        f"| Peach | {known[2]} |\n\n"
        f"Find the missing frequency value, $k$."
    )
    sol = (
        f"**Step 1:** Set up an equation using the total count:\n"
        f"$${known[0]} + {known[1]} + k + {known[2]} = {total}$$\n\n"
        f"**Step 2:** Combine like terms:\n"
        f"$${sum(known)} + k = {total}$$\n\n"
        f"**Step 3:** Solve for $k$:\n"
        f"$$k = {total} - {sum(known)} = \\mathbf{{{missing}}}$$"
    )
    ans = f"{missing}"
    return {
        "id": f"g7_data_30_{rng.randint(100000, 999999)}",
        "subskill": "30_missing_frequency_given_total_count",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_30",
        "hints": {
            "tier_1": f"Sum of known frequencies is {sum(known)}.",
            "tier_2": f"Subtract {sum(known)} from {total}.",
            "tier_3": ans
        },
        "misconception_tags": ["arithmetic_addition_error"]
    }


# 31. Find missing value given mean
def arch_31_find_missing_value_given_mean(rng: random.Random) -> Dict[str, Any]:
    # 4 numbers: 14, 18, 22, x with mean 20 -> total = 80 -> x = 80 - 54 = 26
    nums = [14, 18, 22]
    mean_target = 20
    n = 4
    total_target = mean_target * n
    sum_known = sum(nums)
    missing = total_target - sum_known
    
    prompt = (
        f"The mean of four numbers is **{mean_target}**.\n\n"
        f"Three of the numbers are {nums[0]}, {nums[1]}, and {nums[2]}.\n\n"
        f"Find the value of the fourth number, $x$."
    )
    sol = (
        f"**Step 1:** Calculate the required total sum of the 4 numbers:\n"
        f"$$\\text{{Total}} = \\text{{Mean}} \\times n = {mean_target} \\times {n} = {total_target}$$\n\n"
        f"**Step 2:** Find the sum of the three known numbers:\n"
        f"$${nums[0]} + {nums[1]} + {nums[2]} = {sum_known}$$\n\n"
        f"**Step 3:** Subtract the known sum from the total sum:\n"
        f"$$x = {total_target} - {sum_known} = \\mathbf{{{missing}}}$$"
    )
    ans = f"{missing}"
    return {
        "id": f"g7_data_31_{rng.randint(100000, 999999)}",
        "subskill": "31_find_missing_value_given_mean",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_data_31",
        "hints": {
            "tier_1": f"Total required sum = 4 * {mean_target} = {total_target}.",
            "tier_2": f"Subtract {sum_known} from {total_target}.",
            "tier_3": ans
        },
        "misconception_tags": ["dividing_instead_of_multiplying_mean"]
    }


# 32. Find missing value given median
def arch_32_find_missing_value_given_median(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Five numbers are arranged in ascending order:\n"
        "$$12; 15; x; 24; 28$$\n\n"
        "If the **median** of the data set is **19**, determine the value of $x$."
    )
    sol = (
        "**Step 1:** For an odd number of ordered values ($n = 5$), the median is the exact middle (3rd) value:\n"
        "$$\\text{Position} = \\frac{5 + 1}{2} = 3\\text{rd value}$$\n\n"
        "**Step 2:** In the sequence $12; 15; x; 24; 28$, the 3rd value is $x$.\n"
        "Since the median is given as 19, we have:\n"
        "$$x = \\mathbf{19}$$"
    )
    ans = "19"
    return {
        "id": f"g7_data_32_{rng.randint(100000, 999999)}",
        "subskill": "32_find_missing_value_given_median",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_data_32",
        "hints": {
            "tier_1": "The middle value in an ordered set of 5 numbers is the median.",
            "tier_2": "x is the 3rd number.",
            "tier_3": ans
        },
        "misconception_tags": ["misunderstanding_median_position"]
    }


# 33. Find missing value given range
def arch_33_find_missing_value_given_range(rng: random.Random) -> Dict[str, Any]:
    min_val = 14
    range_val = 26
    max_val = min_val + range_val
    prompt = (
        f"In a data set, the smallest value is **{min_val}** and the range is **{range_val}**.\n\n"
        f"Calculate the largest value in the data set."
    )
    sol = (
        f"**Step 1:** Recall the formula for range:\n"
        f"$$\\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}}$$\n\n"
        f"**Step 2:** Substitute known values:\n"
        f"$${range_val} = \\text{{Maximum}} - {min_val}$$\n\n"
        f"**Step 3:** Solve for the Maximum:\n"
        f"$$\\text{{Maximum}} = {min_val} + {range_val} = \\mathbf{{{max_val}}}$$"
    )
    ans = f"{max_val}"
    return {
        "id": f"g7_data_33_{rng.randint(100000, 999999)}",
        "subskill": "33_find_missing_value_given_range",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_33",
        "hints": {
            "tier_1": "Add the range to the minimum value.",
            "tier_2": f"Maximum = {min_val} + {range_val}.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracting_range_from_minimum"]
    }


# 34. Effect of outlier on mean
def arch_34_effect_of_outlier_on_mean(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the data set of test marks out of 20:\n"
        "$$12; 13; 14; 15; 16$$\n\n"
        "If an extreme outlier of **95** (an error in recording) is added to this set, "
        "explain what happens to the **mean**."
    )
    sol = (
        "**Step 1: Original Mean:**\n"
        "$$\\text{Original Mean} = \\frac{12 + 13 + 14 + 15 + 16}{5} = \\frac{70}{5} = 14$$\n\n"
        "**Step 2: New Mean with Outlier:**\n"
        "$$\\text{New Mean} = \\frac{70 + 95}{6} = \\frac{165}{6} = 27,5$$\n\n"
        "**Conclusion:**\n"
        "The mean increases substantially (from 14 to 27,5) because the mean uses every numerical value "
        "and is highly sensitive to extreme values (outliers)."
    )
    ans = "increases significantly"
    return {
        "id": f"g7_data_34_{rng.randint(100000, 999999)}",
        "subskill": "34_effect_of_outlier_on_mean",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_34",
        "hints": {
            "tier_1": "Does adding a very large number pull the average up or down?",
            "tier_2": "The mean will increase significantly.",
            "tier_3": ans
        },
        "misconception_tags": ["believing_mean_is_resistant_to_outliers"]
    }


# 35. Effect of outlier on median
def arch_35_effect_of_outlier_on_median(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A group of 5 learners had heights (in cm): 140, 142, 145, 148, 150. (Median = 145 cm).\n\n"
        "A very tall visitor measuring 210 cm joins the group.\n\n"
        "Does the median change dramatically like the mean, or does it stay relatively stable? "
        "Calculate the new median."
    )
    sol = (
        "**Step 1: Order the 6 values:**\n"
        "$$140; 142; 145; 148; 150; 210$$\n\n"
        "**Step 2: Find the new median:**\n"
        "The middle two values are 145 and 148.\n"
        "$$\\text{New Median} = \\frac{145 + 148}{2} = \\frac{293}{2} = \\mathbf{146,5\\text{ cm}}$$\n\n"
        "**Step 3: Conclusion:**\n"
        "The median changes only slightly (from 145 cm to 146,5 cm). It is resistant (robust) to extreme outliers."
    )
    ans = "146,5"
    return {
        "id": f"g7_data_35_{rng.randint(100000, 999999)}",
        "subskill": "35_effect_of_outlier_on_median",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_35",
        "hints": {
            "tier_1": "Find the average of the two middle values: 145 and 148.",
            "tier_2": "(145 + 148) / 2 = 146,5.",
            "tier_3": ans
        },
        "misconception_tags": ["believing_median_is_distorted_by_outliers"]
    }


# 36. Effect of outlier on mode
def arch_36_effect_of_outlier_on_mode(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a small company, five workers earn R15 000 each, two earn R20 000, and the CEO earns R1 500 000.\n\n"
        "What is the **mode** of the salaries? Does the CEO's extreme salary change the mode?"
    )
    sol = (
        "**Step 1:** The mode is the most frequently occurring value.\n"
        "- R15 000 occurs 5 times.\n"
        "- R20 000 occurs 2 times.\n"
        "- R1 500 000 occurs 1 time.\n\n"
        "**Step 2:** The mode is **R15 000**.\n\n"
        "**Step 3:** The CEO's extreme salary does **not** affect the mode at all."
    )
    ans = "R15 000"
    return {
        "id": f"g7_data_36_{rng.randint(100000, 999999)}",
        "subskill": "36_effect_of_outlier_on_mode",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_36",
        "hints": {
            "tier_1": "Which salary appears most often?",
            "tier_2": "R15 000 appears 5 times.",
            "tier_3": ans
        },
        "misconception_tags": ["mode_confused_with_highest_value"]
    }


# 37. Choosing appropriate measure mean vs median with outlier
def arch_37_choosing_appropriate_measure_mean_vs_median_with_outlier(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A real estate agent lists home prices in a neighbourhood:\n"
        "$$\\text{R800 000}; \\text{R850 000}; \\text{R900 000}; \\text{R920 000}; \\text{R15 000 000}$$\n\n"
        "Which measure of central tendency (mean or median) is more appropriate to summarize a typical home price? "
        "Give a reason for your choice."
    )
    sol = (
        "**Step 1:** Evaluate the presence of outliers:\n"
        "R15 000 000 is an extreme outlier compared to the other homes (~R900 000).\n\n"
        "**Step 2:** Mean calculation:\n"
        "The mean would be heavily skewed upwards to approximately R3 694 000, which does not represent any typical home.\n\n"
        "**Step 3:** Recommendation:\n"
        "The **median** is the most appropriate measure because it is not distorted by extreme outliers."
    )
    ans = "Median"
    return {
        "id": f"g7_data_37_{rng.randint(100000, 999999)}",
        "subskill": "37_choosing_appropriate_measure_mean_vs_median_with_outlier",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_37",
        "hints": {
            "tier_1": "Notice the extreme value of R15 000 000.",
            "tier_2": "Which average is not pulled by outliers?",
            "tier_3": ans
        },
        "misconception_tags": ["always_preferring_mean_regardless_of_skew"]
    }


# 38. Choosing appropriate measure mode for shoe size
def arch_38_choosing_appropriate_measure_mode_for_shoe_size(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A shoe store manager wants to order new stock for school shoes. "
        "Should she calculate the mean shoe size, the median shoe size, or the mode? "
        "Explain why."
    )
    sol = (
        "**Step 1:** Consider the purpose of ordering stock:\n"
        "The store manager needs to know which specific shoe sizes sell the most often.\n\n"
        "**Step 2:** Analysis:\n"
        "- A mean shoe size like 5,7 cannot be ordered or sold.\n"
        "- The **mode** identifies the most popular, frequently requested size.\n\n"
        "**Conclusion:**\n"
        "The **mode** is the most useful measure for ordering inventory/stock."
    )
    ans = "Mode"
    return {
        "id": f"g7_data_38_{rng.randint(100000, 999999)}",
        "subskill": "38_choosing_appropriate_measure_mode_for_shoe_size",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_38",
        "hints": {
            "tier_1": "Which measure tells the shop owner which item is purchased most frequently?",
            "tier_2": "Mode represents the most frequent item.",
            "tier_3": ans
        },
        "misconception_tags": ["recommending_mean_for_discrete_categories"]
    }


# 39. Stem and leaf find range
def arch_39_stem_and_leaf_find_range(rng: random.Random) -> Dict[str, Any]:
    # Stem | Leaves:
    # 2 | 1, 4, 8 -> min = 21
    # 3 | 0, 5
    # 4 | 2, 7 -> max = 47
    min_v = 21
    max_v = 47
    range_v = max_v - min_v
    prompt = (
        "The stem-and-leaf plot displays test scores:\n\n"
        "$$\\begin{array}{r|l}\n"
        "2 & 1\\quad 4\\quad 8 \\\\\n"
        "3 & 0\\quad 5 \\\\\n"
        "4 & 2\\quad 7\n"
        "\\end{array}$$\n\n"
        "**Key:** $2 \\mid 1 = 21$\n\n"
        "Calculate the **range** of the test scores."
    )
    sol = (
        "**Step 1:** Read the minimum and maximum scores from the plot:\n"
        f"- Minimum score: Stem 2, leaf 1 = **{min_v}**\n"
        f"- Maximum score: Stem 4, leaf 7 = **{max_v}**\n\n"
        "**Step 2:** Calculate the range:\n"
        f"$$\\text{{Range}} = {max_v} - {min_v} = \\mathbf{{{range_v}}}$$"
    )
    ans = f"{range_v}"
    return {
        "id": f"g7_data_39_{rng.randint(100000, 999999)}",
        "subskill": "39_stem_and_leaf_find_range",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_39",
        "hints": {
            "tier_1": "Lowest score is 21, highest is 47.",
            "tier_2": "Range = 47 - 21.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracting_leaves_only"]
    }


# 40. Stem and leaf find median
def arch_40_stem_and_leaf_find_median(rng: random.Random) -> Dict[str, Any]:
    # 9 scores: 12, 15, 18, 20, 23, 27, 31, 34, 38
    # Median is 5th value: 23
    prompt = (
        "The stem-and-leaf plot shows the marks of 9 learners:\n\n"
        "$$\\begin{array}{r|l}\n"
        "1 & 2\\quad 5\\quad 8 \\\\\n"
        "2 & 0\\quad 3\\quad 7 \\\\\n"
        "3 & 1\\quad 4\\quad 8\n"
        "\\end{array}$$\n\n"
        "**Key:** $1 \\mid 2 = 12$\n\n"
        "Find the **median** mark."
    )
    sol = (
        "**Step 1:** Total number of scores is $n = 9$.\n\n"
        "**Step 2:** Find median position:\n"
        "$$\\text{Position} = \\frac{9 + 1}{2} = 5\\text{th score}$$\n\n"
        "**Step 3:** Count the scores in order:\n"
        "1st: 12, 2nd: 15, 3rd: 18, 4th: 20, **5th: 23**.\n\n"
        "Therefore, the median is **23**."
    )
    ans = "23"
    return {
        "id": f"g7_data_40_{rng.randint(100000, 999999)}",
        "subskill": "40_stem_and_leaf_find_median",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_40",
        "hints": {
            "tier_1": "With 9 numbers, the median is the 5th value.",
            "tier_2": "Count through the leaves in row 1 and row 2.",
            "tier_3": ans
        },
        "misconception_tags": ["median_calculated_on_leaves_alone"]
    }


# 41. Stem and leaf find mode
def arch_41_stem_and_leaf_find_mode(rng: random.Random) -> Dict[str, Any]:
    # 52, 54, 54, 54, 61, 65, 72 -> mode 54
    prompt = (
        "Determine the **mode** from the following stem-and-leaf plot:\n\n"
        "$$\\begin{array}{r|l}\n"
        "5 & 2\\quad 4\\quad 4\\quad 4 \\\\\n"
        "6 & 1\\quad 5 \\\\\n"
        "7 & 2\n"
        "\\end{array}$$\n\n"
        "**Key:** $5 \\mid 2 = 52$"
    )
    sol = (
        "**Step 1:** Look for the leaf repeated most often in the same stem row:\n"
        "In stem 5, the leaf '4' appears three times.\n\n"
        "**Step 2:** Combine stem and leaf:\n"
        "Stem 5 with leaf 4 represents the score **54**.\n\n"
        "Therefore, the mode is **54**."
    )
    ans = "54"
    return {
        "id": f"g7_data_41_{rng.randint(100000, 999999)}",
        "subskill": "41_stem_and_leaf_find_mode",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_data_41",
        "hints": {
            "tier_1": "Which digit repeats 3 times on stem 5?",
            "tier_2": "Stem 5 and leaf 4 make 54.",
            "tier_3": ans
        },
        "misconception_tags": ["reporting_leaf_only_as_mode"]
    }


# 42. Stem and leaf find mean
def arch_42_stem_and_leaf_find_mean(rng: random.Random) -> Dict[str, Any]:
    # 5 values: 10, 12, 14, 20, 24 -> sum = 80 / 5 = 16
    prompt = (
        "Calculate the **mean** of the 5 values represented in this stem-and-leaf plot:\n\n"
        "$$\\begin{array}{r|l}\n"
        "1 & 0\\quad 2\\quad 4 \\\\\n"
        "2 & 0\\quad 4\n"
        "\\end{array}$$\n\n"
        "**Key:** $1 \\mid 0 = 10$"
    )
    sol = (
        "**Step 1:** List the individual values:\n"
        "$$10; 12; 14; 20; 24$$\n\n"
        "**Step 2:** Find the sum of the values:\n"
        "$$\\text{Sum} = 10 + 12 + 14 + 20 + 24 = 80$$\n\n"
        "**Step 3:** Divide by $n = 5$:\n"
        "$$\\text{Mean} = \\frac{80}{5} = \\mathbf{16}$$"
    )
    ans = "16"
    return {
        "id": f"g7_data_42_{rng.randint(100000, 999999)}",
        "subskill": "42_stem_and_leaf_find_mean",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_42",
        "hints": {
            "tier_1": "List the 5 numbers: 10, 12, 14, 20, 24.",
            "tier_2": "Sum = 80; Mean = 80 / 5.",
            "tier_3": ans
        },
        "misconception_tags": ["adding_leaves_without_stems"]
    }


# 43. Grouped data class intervals frequency
def arch_43_grouped_data_class_intervals_frequency(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A teacher groups the test marks of 35 learners into class intervals:\n\n"
        "| Interval | Frequency |\n"
        "| :---: | :---: |\n"
        "| $0 - 9$ | 2 |\n"
        "| $10 - 19$ | 8 |\n"
        "| $20 - 29$ | 15 |\n"
        "| $30 - 39$ | 7 |\n"
        "| $40 - 50$ | 3 |\n\n"
        "How many learners achieved a mark of **20 or more**?"
    )
    sol = (
        "**Step 1:** Identify intervals for marks 20 or higher:\n"
        "- $20 - 29$: 15 learners\n"
        "- $30 - 39$: 7 learners\n"
        "- $40 - 50$: 3 learners\n\n"
        "**Step 2:** Sum the frequencies:\n"
        "$$\\text{Total} = 15 + 7 + 3 = \\mathbf{25\\text{ learners}}$$"
    )
    ans = "25"
    return {
        "id": f"g7_data_43_{rng.randint(100000, 999999)}",
        "subskill": "43_grouped_data_class_intervals_frequency",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_43",
        "hints": {
            "tier_1": "Add the counts in the bottom three rows (20-29, 30-39, 40-50).",
            "tier_2": "15 + 7 + 3 = 25.",
            "tier_3": ans
        },
        "misconception_tags": ["omitting_top_intervals"]
    }


# 44. Grouped data modal class identification
def arch_44_grouped_data_modal_class_identification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Examine the grouped frequency distribution:\n\n"
        "| Mass (kg) | Frequency |\n"
        "| :---: | :---: |\n"
        "| $40 - 44$ | 4 |\n"
        "| $45 - 49$ | 11 |\n"
        "| $50 - 54$ | 18 |\n"
        "| $55 - 59$ | 9 |\n\n"
        "State the **modal class interval**."
    )
    sol = (
        "**Step 1:** Find the interval with the highest frequency.\n\n"
        "**Step 2:** Compare frequencies: 4, 11, 18, 9.\n"
        "The highest frequency is 18, which belongs to the interval **50 - 54 kg**.\n\n"
        "Therefore, the modal class is **50 - 54 kg**."
    )
    ans = "50 - 54"
    return {
        "id": f"g7_data_44_{rng.randint(100000, 999999)}",
        "subskill": "44_grouped_data_modal_class_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_data_44",
        "hints": {
            "tier_1": "Identify which interval has the largest number in the frequency column.",
            "tier_2": "Highest frequency is 18 for 50 - 54.",
            "tier_3": ans
        },
        "misconception_tags": ["stating_frequency_instead_of_interval"]
    }


# 45. Grouped data tally and counts
def arch_45_grouped_data_tally_and_counts(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The following 8 numbers must be sorted into intervals of width 5:\n"
        "$$11; 14; 16; 18; 19; 21; 22; 24$$\n\n"
        "How many numbers fall into the interval **15 to 19** (inclusive)?"
    )
    sol = (
        "**Step 1:** List numbers between 15 and 19 inclusive:\n"
        "- 16\n"
        "- 18\n"
        "- 19\n\n"
        "**Step 2:** Count the matching values:\n"
        "There are **3** numbers in the interval 15 to 19."
    )
    ans = "3"
    return {
        "id": f"g7_data_45_{rng.randint(100000, 999999)}",
        "subskill": "45_grouped_data_tally_and_counts",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_45",
        "hints": {
            "tier_1": "Find the numbers >= 15 and <= 19.",
            "tier_2": "They are 16, 18, 19.",
            "tier_3": ans
        },
        "misconception_tags": ["boundary_inclusion_error"]
    }


# 46. Comparing two data sets using mean and range
def arch_46_comparing_two_data_sets_using_mean_and_range(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two Grade 7 classes took the same test out of 50:\n\n"
        "- **Class 7A:** Mean = 32, Range = 12\n"
        "- **Class 7B:** Mean = 32, Range = 28\n\n"
        "Both classes have the same mean. Which class performed more **consistently**? Explain your reasoning."
    )
    sol = (
        "**Step 1:** Understand consistency in statistics:\n"
        "Consistency is measured by the spread of data. A smaller range indicates that the scores "
        "are clustered closer to each other and to the mean.\n\n"
        "**Step 2:** Compare ranges:\n"
        "- Class 7A Range = 12\n"
        "- Class 7B Range = 28\n\n"
        "**Step 3:** Conclusion:\n"
        "**Class 7A** was more consistent because its range is much smaller (12 vs 28)."
    )
    ans = "Class 7A"
    return {
        "id": f"g7_data_46_{rng.randint(100000, 999999)}",
        "subskill": "46_comparing_two_data_sets_using_mean_and_range",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_46",
        "hints": {
            "tier_1": "A smaller range means scores are closer together (more consistent).",
            "tier_2": "Class 7A has a range of 12 vs 28.",
            "tier_3": ans
        },
        "misconception_tags": ["associating_larger_range_with_better_performance"]
    }


# 47. Comparing two data sets using median and mode
def arch_47_comparing_two_data_sets_using_median_and_mode(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two soccer teams scored goals over 7 matches:\n\n"
        "- **Team X:** $0, 1, 1, 1, 2, 2, 8$ (Median = 1, Mode = 1)\n"
        "- **Team Y:** $1, 2, 2, 3, 3, 3, 4$ (Median = 3, Mode = 3)\n\n"
        "Which team generally scored more goals per match? Justify your choice."
    )
    sol = (
        "**Step 1:** Compare central tendency measures:\n"
        "- Team X has a median of 1 and a mode of 1.\n"
        "- Team Y has a median of 3 and a mode of 3.\n\n"
        "**Step 2:** Note on Team X's 8 goals:\n"
        "Team X had one unusually high-scoring match (8 goals), but in most matches scored 1 goal.\n\n"
        "**Step 3:** Conclusion:\n"
        "**Team Y** generally scored more goals because its typical match produced 3 goals (higher median and mode)."
    )
    ans = "Team Y"
    return {
        "id": f"g7_data_47_{rng.randint(100000, 999999)}",
        "subskill": "47_comparing_two_data_sets_using_median_and_mode",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_47",
        "hints": {
            "tier_1": "Compare the medians (1 vs 3).",
            "tier_2": "Team Y's typical output is 3 goals.",
            "tier_3": ans
        },
        "misconception_tags": ["over_relying_on_single_isolated_high_score"]
    }


# 48. Data collection survey questionnaire bias detection
def arch_48_data_collection_survey_questionnaire_bias_detection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider this survey question given to learners:\n\n"
        "\"*Don't you agree that homework is stressful and should be abolished?*\"\n\n"
        "Explain why this question is **biased** and violates sound statistical data collection standards."
    )
    sol = (
        "**Step 1:** Definition of leading/biased question:\n"
        "A question is biased if it nudges or encourages the respondent towards a specific answer.\n\n"
        "**Step 2:** Critique:\n"
        "The phrasing \"*Don't you agree that...*\" leads the respondent to agree that homework is stressful "
        "rather than asking neutrally about their views.\n\n"
        "**Step 3:** Improvement:\n"
        "A neutral question would be: \"*What are your views on homework load? (Too much / Balanced / Too little)*\"."
    )
    ans = "It is a leading question that pushes respondents to agree"
    return {
        "id": f"g7_data_48_{rng.randint(100000, 999999)}",
        "subskill": "48_data_collection_survey_questionnaire_bias_detection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_48",
        "hints": {
            "tier_1": "Notice the phrasing 'Don't you agree...'.",
            "tier_2": "It leads the respondent to a particular answer.",
            "tier_3": ans
        },
        "misconception_tags": ["unaware_of_leading_survey_bias"]
    }


# 49. Data collection designing unbiased questions
def arch_49_data_collection_designing_unbiased_questions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Rewrite the following biased survey question to make it neutral and objective:\n\n"
        "\"*Since school uniform is uncomfortable, should learners wear casual clothes?*\""
    )
    sol = (
        "**Step 1:** Remove loaded assumptions (\"Since school uniform is uncomfortable\").\n\n"
        "**Step 2:** Provide balanced phrasing offering clear, objective options.\n\n"
        "**Neutral Version:**\n"
        "\"*Should learners wear school uniforms or casual clothes to school?*\"\n"
        "Options: [ ] School uniform  [ ] Casual clothes  [ ] No preference"
    )
    ans = "Should learners wear school uniforms or casual clothes to school?"
    return {
        "id": f"g7_data_49_{rng.randint(100000, 999999)}",
        "subskill": "49_data_collection_designing_unbiased_questions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_49",
        "hints": {
            "tier_1": "Remove the assumption that uniforms are uncomfortable.",
            "tier_2": "Offer both choices neutrally.",
            "tier_3": ans
        },
        "misconception_tags": ["retaining_presuppositions_in_redesign"]
    }


# 50. Data reporting and summarising conclusions
def arch_50_data_reporting_and_summarising_conclusions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A class investigated daily water consumption among 30 families.\n\n"
        "- Mean: 450 litres\n"
        "- Median: 380 litres\n"
        "- Mode: 350 litres\n"
        "- Range: 900 litres (minimum 200 L, maximum 1 100 L)\n\n"
        "Why is the mean (450 L) notably higher than the median (380 L)? "
        "What does this suggest about water usage across the families?"
    )
    sol = (
        "**Step 1:** Identify the skew/outliers:\n"
        "The maximum value is 1 100 L, which is substantially higher than the typical values around 350-380 L.\n\n"
        "**Step 2:** Statistical deduction:\n"
        "A few households have extremely high water consumption (e.g. 1 100 L), which pulls the mean upward.\n\n"
        "**Step 3:** Report conclusion:\n"
        "Most families consume between 350 L and 380 L of water daily, but a small number of heavy-use households "
        "inflate the overall average (mean)."
    )
    ans = "A few high-consuming households pull the mean up"
    return {
        "id": f"g7_data_50_{rng.randint(100000, 999999)}",
        "subskill": "50_data_reporting_and_summarising_conclusions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_50",
        "hints": {
            "tier_1": "Look at the maximum value of 1 100 L.",
            "tier_2": "High outliers pull the mean above the median.",
            "tier_3": ans
        },
        "misconception_tags": ["assuming_mean_equals_median_in_skewed_data"]
    }
