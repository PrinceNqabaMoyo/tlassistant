"""Grade 7 Mathematics - Collect, Organise and Summarise Data: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Collect organise and summarise data.md
"""
import random
import math
from typing import Dict, Any, List


def _svg_tally(count: int, width: int = 240, height: int = 60) -> str:
    """Renders groups of 5 tallies (4 vertical, 1 diagonal slash) and remainder."""
    groups_of_5 = count // 5
    rem = count % 5
    
    lines = []
    x_offset = 20
    for g in range(groups_of_5):
        # 4 vertical strokes
        for v in range(4):
            x = x_offset + g * 50 + v * 8
            lines.append(f'<line x1="{x}" y1="15" x2="{x}" y2="45" stroke="#1e293b" stroke-width="2.5"/>')
        # 1 diagonal slash across the 4
        x_start = x_offset + g * 50 - 4
        x_end = x_offset + g * 50 + 28
        lines.append(f'<line x1="{x_start}" y1="42" x2="{x_end}" y2="18" stroke="#dc2626" stroke-width="2.5"/>')
        
    start_rem = x_offset + groups_of_5 * 50
    for r in range(rem):
        x = start_rem + r * 8
        lines.append(f'<line x1="{x}" y1="15" x2="{x}" y2="45" stroke="#1e293b" stroke-width="2.5"/>')
        
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{"".join(lines)}'
        f'</svg>'
    )


# 01. Population vs sample definitions
def arch_01_population_vs_sample_definitions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In statistical research, explain the precise difference between a **population** and a **sample**.\n\n"
        "Provide one realistic example from a school environment."
    )
    sol = (
        "**Step 1: Definitions:**\n"
        "- **Population:** The entire group of individuals, objects, or events that you want to draw conclusions about.\n"
        "- **Sample:** A smaller subset selected from the population to represent the whole group.\n\n"
        "**Step 2: School Example:**\n"
        "- **Population:** All 800 learners in a high school.\n"
        "- **Sample:** 50 learners chosen randomly across different grades."
    )
    ans = "Population is the entire group being studied; Sample is a representative subset chosen from the population."
    return {
        "id": f"g7_data_01_{rng.randint(100000, 999999)}",
        "subskill": "01_population_vs_sample_definitions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_01",
        "hints": {
            "tier_1": "Population = entire group; Sample = smaller part.",
            "tier_2": "Think of testing a spoon of soup (sample) from the entire pot (population).",
            "tier_3": ans
        },
        "misconception_tags": ["confused_population_and_sample"]
    }


# 02. Identify population and sample in context
def arch_02_identify_population_and_sample_in_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Scenario: A researcher wants to know how many hours of sleep Grade 7 teenagers in Durban get each night. "
        "She surveys 120 Grade 7 learners selected from four different schools across Durban.\n\n"
        "1. Identify the **population** of this study.\n"
        "2. Identify the **sample** of this study."
    )
    sol = (
        "**1. Population:** All Grade 7 learners in Durban.\n"
        "**2. Sample:** The 120 Grade 7 learners surveyed from the four schools."
    )
    ans = "1. All Grade 7 learners in Durban; 2. The 120 surveyed Grade 7 learners"
    return {
        "id": f"g7_data_02_{rng.randint(100000, 999999)}",
        "subskill": "02_identify_population_and_sample_in_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_02",
        "hints": {
            "tier_1": "Who does she want to learn about? (Population). Who did she actually ask? (Sample).",
            "tier_2": "Population: All Gr7s in Durban; Sample: 120 learners.",
            "tier_3": ans
        },
        "misconception_tags": ["population_restricted_to_sample_size"]
    }


# 03. Sample bias identification and critique
def arch_03_sample_bias_identification_and_critique(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Scenario: Thabo wants to find out the favourite sport of all learners in his school. "
        "He stands outside the soccer field during first-team soccer practice and surveys 40 learners there.\n\n"
        "1. Is Thabo's sample **representative** or **biased**?\n"
        "2. Explain why, suggesting how he could improve his sampling method."
    )
    sol = (
        "**Step 1:** The sample is **biased**.\n\n"
        "**Step 2:** Surveying learners at a soccer field over-represents soccer fans, ignoring learners who participate "
        "in netball, hockey, rugby, chess, or no sports.\n\n"
        "**Improvement:** He should survey learners randomly during assembly or at the school gate so every learner has an equal chance of being chosen."
    )
    ans = "1. Biased; 2. It only surveys soccer fans at soccer practice; survey randomly at school entrance or assembly instead."
    return {
        "id": f"g7_data_03_{rng.randint(100000, 999999)}",
        "subskill": "03_sample_bias_identification_and_critique",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_03",
        "hints": {
            "tier_1": "Are soccer practice attendees likely to love soccer?",
            "tier_2": "It is biased because the location favors one sport.",
            "tier_3": ans
        },
        "misconception_tags": ["sample_bias_unrecognized"]
    }


# 04. Sample size sufficiency critique
def arch_04_sample_size_sufficiency_critique(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Scenario: A high school has 1 500 learners. A learner surveys 5 of his close friends to determine "
        "if the school tuckshop should sell healthier fruit options.\n\n"
        "Explain two major reasons why this sample is NOT representative of the school's population."
    )
    sol = (
        "**Reason 1 (Sample size):** 5 learners is far too small a sample size to reflect the opinions of 1 500 learners (only 0,33% of the population).\n\n"
        "**Reason 2 (Lack of diversity / Bias):** Surveying only close friends introduces friendship bias (friends often share similar preferences and ages) and ignores all other grades."
    )
    ans = "1. Sample size of 5 is far too small for 1 500 learners; 2. Asking only close friends introduces bias and ignores the rest of the school."
    return {
        "id": f"g7_data_04_{rng.randint(100000, 999999)}",
        "subskill": "04_sample_size_sufficiency_critique",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_04",
        "hints": {
            "tier_1": "Think about the sample size (5 out of 1500) and who was asked (friends).",
            "tier_2": "Too small + only asked friends.",
            "tier_3": ans
        },
        "misconception_tags": ["sample_size_sufficiency_misjudgment"]
    }


# 05. Data collection methods comparison questionnaire vs interview
def arch_05_data_collection_methods_comparison_questionnaire_vs_interview(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Compare using a **written questionnaire** versus conducting **face-to-face interviews** for data collection:\n\n"
        "1. Give one advantage of using a written questionnaire.\n"
        "2. Give one advantage of conducting face-to-face interviews."
    )
    sol = (
        "**1. Advantage of Questionnaire:** Can be distributed quickly to a large number of respondents at low cost; provides respondent anonymity.\n\n"
        "**2. Advantage of Interview:** The interviewer can clarify confusing questions, ask follow-up questions, and include respondents who cannot read or write."
    )
    ans = "1. Questionnaire: reaches many people quickly and cheaply / anonymous; 2. Interview: can clarify questions and ask follow-ups."
    return {
        "id": f"g7_data_05_{rng.randint(100000, 999999)}",
        "subskill": "05_data_collection_methods_comparison_questionnaire_vs_interview",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_05",
        "hints": {
            "tier_1": "Which is faster for 500 people? Which is better for explaining hard questions?",
            "tier_2": "Questionnaires reach many people; interviews allow explanation.",
            "tier_3": ans
        },
        "misconception_tags": ["data_collection_method_suitability_error"]
    }


# 06. Questionnaire design avoiding leading questions
def arch_06_questionnaire_design_avoiding_leading_questions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A questionnaire asks: 'Don't you agree that homework is boring and should be abolished?'\n\n"
        "1. Why is this a poorly designed survey question (what type of question is this)?\n"
        "2. Rewrite the question so that it is neutral and unbiased."
    )
    sol = (
        "**Step 1:** This is a **leading question** (biased question) because it pushes the respondent to agree that homework is boring.\n\n"
        "**Step 2: Neutral rewrite:** 'What is your opinion regarding homework? (A) Very helpful, (B) Somewhat helpful, (C) Not helpful' "
        "or 'Do you feel the amount of homework assigned is appropriate? Yes / No / Unsure'."
    )
    ans = "1. Leading (biased) question; 2. Rewrite neutrally: 'What is your opinion on homework? (Helpful / Not helpful / Neutral)'"
    return {
        "id": f"g7_data_06_{rng.randint(100000, 999999)}",
        "subskill": "06_questionnaire_design_avoiding_leading_questions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_06",
        "hints": {
            "tier_1": "Does the question lead the person to a specific answer?",
            "tier_2": "A leading question biases the results.",
            "tier_3": ans
        },
        "misconception_tags": ["leading_question_unrecognized"]
    }


# 07. Questionnaire design multiple choice categories
def arch_07_questionnaire_design_multiple_choice_categories(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When designing multiple-choice response categories in a questionnaire, two important rules must be followed:\n"
        "- Categories must be **mutually exclusive** (non-overlapping).\n"
        "- Categories must be **exhaustive** (cover all possible options, often including 'Other').\n\n"
        "Look at these options for 'How much time do you spend on chores daily?':\n"
        "A) 0 to 1 hour\n"
        "B) 1 to 2 hours\n"
        "C) 2 to 3 hours\n\n"
        "Identify the flaw with these options if a learner spends exactly 1 hour on chores."
    )
    sol = (
        "**Answer:** The categories overlap at the boundaries. If a learner spends exactly 1 hour, "
        "they could choose both Option A and Option B. The categories should be written as: "
        "'Less than 1 hour', '1 to less than 2 hours', '2 hours or more'."
    )
    ans = "The categories overlap at exactly 1 hour and 2 hours (not mutually exclusive)."
    return {
        "id": f"g7_data_07_{rng.randint(100000, 999999)}",
        "subskill": "07_questionnaire_design_multiple_choice_categories",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_07",
        "hints": {
            "tier_1": "Where does someone tick if they spend exactly 1 hour?",
            "tier_2": "1 hour appears in both A and B.",
            "tier_3": ans
        },
        "misconception_tags": ["overlapping_survey_options_error"]
    }


# 08. Discrete vs continuous data in statistics
def arch_08_discrete_vs_continuous_data_in_statistics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Classify the type of data collected in each of the following investigations as **discrete** or **continuous**:\n\n"
        "1. Number of siblings in each learner's family.\n"
        "2. Time taken in seconds to run a 100 m race.\n"
        "3. Shoe sizes sold at a shop.\n"
        "4. Mass in kilograms of school backpacks."
    )
    sol = (
        "**1.** Number of siblings $\\rightarrow$ **Discrete** (counted in whole numbers).\n"
        "**2.** Time in seconds $\\rightarrow$ **Continuous** (measured on a continuous time scale).\n"
        "**3.** Shoe sizes $\\rightarrow$ **Discrete** (specific distinct manufactured sizes like 5, 5.5, 6).\n"
        "**4.** Mass in kg $\\rightarrow$ **Continuous** (measured on a continuous mass scale)."
    )
    ans = "1. Discrete; 2. Continuous; 3. Discrete; 4. Continuous"
    return {
        "id": f"g7_data_08_{rng.randint(100000, 999999)}",
        "subskill": "08_discrete_vs_continuous_data_in_statistics",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_08",
        "hints": {
            "tier_1": "Counted data = discrete; measured data = continuous.",
            "tier_2": "Siblings and shoe sizes are discrete; time and mass are continuous.",
            "tier_3": ans
        },
        "misconception_tags": ["discrete_continuous_classification_error"]
    }


# 09. Tally marks representation of counts
def arch_09_tally_marks_representation_of_counts(rng: random.Random) -> Dict[str, Any]:
    count = rng.choice([7, 13, 18, 23])
    g5 = count // 5
    rem = count % 5
    svg = _svg_tally(count)
    prompt = (
        f"A survey counts {count} votes for the blue team.\n\n"
        f"1. How many complete bundles of 5 (four vertical lines crossed by one diagonal line) are drawn?\n"
        f"2. How many single vertical strokes are drawn in the remainder?"
    )
    sol = (
        f"**Step 1:** Complete bundles of 5: $${count} \\div 5 = {g5} \\text{{ bundles}}$$\n\n"
        f"**Step 2:** Remainder single strokes: $${count} \\pmod 5 = {rem} \\text{{ single strokes}}$$"
    )
    ans = f"1. {g5} bundles of 5; 2. {rem} single strokes"
    return {
        "id": f"g7_data_09_{rng.randint(100000, 999999)}",
        "subskill": "09_tally_marks_representation_of_counts",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Bundles of 5", "body": f"{count} / 5 = {g5} bundles of 5."},
                {"title": "Remainder", "body": f"Remainder is {rem} strokes."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_09",
        "hints": {
            "tier_1": f"Divide {count} by 5.",
            "tier_2": f"{g5} groups of 5 with remainder {rem}.",
            "tier_3": ans
        },
        "misconception_tags": ["tally_group_of_five_counting_error"]
    }


# 10. Reading tally table frequencies
def arch_10_reading_tally_table_frequencies(rng: random.Random) -> Dict[str, Any]:
    f_soccer = 14
    f_netball = 11
    f_rugby = 8
    f_cricket = 7
    total = f_soccer + f_netball + f_rugby + f_cricket # 40
    prompt = (
        "Refer to the sports survey tally table below:\n\n"
        "| Sport | Tallies | Frequency |\n"
        "| :--- | :--- | :--- |\n"
        "| Soccer | <s>||||</s> <s>||||</s> |||| | 14 |\n"
        "| Netball | <s>||||</s> <s>||||</s> | | 11 |\n"
        "| Rugby | <s>||||</s> ||| | 8 |\n"
        "| Cricket | <s>||||</s> || | 7 |\n\n"
        "1. What is the total number of learners surveyed?\n"
        "2. Which sport had the highest frequency (the modal sport)?"
    )
    sol = (
        f"**Step 1:** Total frequency = $14 + 11 + 8 + 7 = \\mathbf{{{total}}}$ learners.\n\n"
        f"**Step 2:** The highest frequency is 14 for **Soccer**."
    )
    ans = f"1. {total} learners; 2. Soccer"
    return {
        "id": f"g7_data_10_{rng.randint(100000, 999999)}",
        "subskill": "10_reading_tally_table_frequencies",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_10",
        "hints": {
            "tier_1": "Add up all numbers in the frequency column.",
            "tier_2": "Look for the largest number in the frequency column.",
            "tier_3": ans
        },
        "misconception_tags": ["frequency_sum_arithmetic_error"]
    }


# 11. Completing frequency table from raw data
def arch_11_completing_frequency_table_from_raw_data(rng: random.Random) -> Dict[str, Any]:
    # Raw scores out of 5:
    # 3, 4, 3, 5, 2, 4, 3, 4, 5, 3
    scores = [3, 4, 3, 5, 2, 4, 3, 4, 5, 3]
    counts = {2: 1, 3: 4, 4: 3, 5: 2}
    prompt = (
        "Here are test scores (out of 5) obtained by 10 learners:\n"
        "$$3; \\quad 4; \\quad 3; \\quad 5; \\quad 2; \\quad 4; \\quad 3; \\quad 4; \\quad 5; \\quad 3$$\n\n"
        "Organise this raw data into a frequency table:\n"
        "What is the frequency of score 3, and what is the frequency of score 4?"
    )
    sol = (
        "**Tally and Count:**\n"
        "- Score 2: appears 1 time (Frequency = 1)\n"
        "- Score 3: appears 4 times (Frequency = 4)\n"
        "- Score 4: appears 3 times (Frequency = 3)\n"
        "- Score 5: appears 2 times (Frequency = 2)\n\n"
        "**Answer:** Frequency of 3 is **4**; Frequency of 4 is **3**."
    )
    ans = "Frequency of 3 = 4; Frequency of 4 = 3"
    return {
        "id": f"g7_data_11_{rng.randint(100000, 999999)}",
        "subskill": "11_completing_frequency_table_from_raw_data",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_11",
        "hints": {
            "tier_1": "Count how many times '3' appears in the list.",
            "tier_2": "Count how many times '4' appears in the list.",
            "tier_3": ans
        },
        "misconception_tags": ["raw_data_tallying_missed_value"]
    }


# 12. Frequency table finding total sample size
def arch_12_frequency_table_finding_total_sample_size(rng: random.Random) -> Dict[str, Any]:
    f1, f2, f3, f4 = 8, 12, 15, 5
    tot = f1 + f2 + f3 + f4 # 40
    prompt = (
        "A frequency table records transport to school:\n"
        "- Walking: 8\n"
        "- Bicycle: 12\n"
        "- Bus: 15\n"
        "- Car: 5\n\n"
        "1. What is the total sample size $n$?\n"
        "2. What fraction of the sample travels by bus (in simplest form)?"
    )
    g = math.gcd(f3, tot) # gcd(15, 40) = 5 -> 3/8
    sol = (
        f"**Step 1:** Total sample size: $$n = {f1} + {f2} + {f3} + {f4} = \\mathbf{{{tot}}}$$\n\n"
        f"**Step 2:** Fraction using bus: $$\\frac{{{f3}}}{{{tot}}} = \\mathbf{{\\frac{{{f3//g}}}{{{tot//g}}}}}$$"
    )
    ans = f"1. {tot}; 2. {f3//g}/{tot//g}"
    return {
        "id": f"g7_data_12_{rng.randint(100000, 999999)}",
        "subskill": "12_frequency_table_finding_total_sample_size",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_12",
        "hints": {
            "tier_1": "Sum the frequencies for total sample size.",
            "tier_2": f"Bus is 15 / {tot}. Simplify by 5.",
            "tier_3": ans
        },
        "misconception_tags": ["sample_size_fraction_simplification_error"]
    }


# 13. Grouped frequency table equal interval widths
def arch_13_grouped_frequency_table_equal_interval_widths(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When organizing test scores ranging from 0 to 50 into a grouped frequency table with intervals:\n"
        "$$0-9; \\quad 10-19; \\quad 20-29; \\quad 30-39; \\quad 40-49$$\n\n"
        "1. What is the width (class size) of each interval?\n"
        "2. In which interval should a score of 29 be placed?"
    )
    sol = (
        "**Step 1:** Count the integers in $0-9$: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 $\\rightarrow$ **width is 10**.\n\n"
        "**Step 2:** A score of 29 belongs in the **20-29** interval."
    )
    ans = "1. 10; 2. 20-29"
    return {
        "id": f"g7_data_13_{rng.randint(100000, 999999)}",
        "subskill": "13_grouped_frequency_table_equal_interval_widths",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_13",
        "hints": {
            "tier_1": "Include both endpoints when finding width: 9 - 0 + 1 = 10.",
            "tier_2": "29 is between 20 and 29 inclusive.",
            "tier_3": ans
        },
        "misconception_tags": ["interval_width_subtraction_omitted_one"]
    }


# 14. Grouped frequency table tallying scores
def arch_14_grouped_frequency_table_tallying_scores(rng: random.Random) -> Dict[str, Any]:
    scores = [12, 17, 24, 28, 29, 31, 35, 42]
    # In 20-29: 24, 28, 29 -> count 3
    prompt = (
        "Consider this dataset of exam percentages:\n"
        "$$12; \\quad 17; \\quad 24; \\quad 28; \\quad 29; \\quad 31; \\quad 35; \\quad 42$$\n\n"
        "How many scores fall into the interval **20 to 29**?"
    )
    sol = (
        "**Step 1:** Identify scores between 20 and 29 inclusive:\n"
        "- 24, 28, 29\n\n"
        "**Conclusion:** There are **3 scores** in the interval 20-29."
    )
    ans = "3 scores"
    return {
        "id": f"g7_data_14_{rng.randint(100000, 999999)}",
        "subskill": "14_grouped_frequency_table_tallying_scores",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_14",
        "hints": {
            "tier_1": "List the numbers that are >= 20 and <= 29.",
            "tier_2": "24, 28, 29.",
            "tier_3": ans
        },
        "misconception_tags": ["interval_boundary_inclusion_error"]
    }


# 15. Stem and leaf display reading values
def arch_15_stem_and_leaf_display_reading_values(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Refer to the stem-and-leaf display below:\n\n"
        "$$\\begin{array}{r|l}\n"
        "\\text{Stem} & \\text{Leaves} \\\\\n"
        "\\hline\n"
        "2 & 1 \\quad 4 \\quad 8 \\\\\n"
        "3 & 0 \\quad 5 \\quad 5 \\quad 9 \\\\\n"
        "4 & 2 \\quad 7\n"
        "\\end{array}$$\n"
        "**Key:** $2 \\mid 1 = 21$\n\n"
        "1. How many total data values are recorded in this display?\n"
        "2. List all the data values represented in the stem 3 row."
    )
    sol = (
        "**Step 1:** Count the leaves: $3 + 4 + 2 = \\mathbf{9\\text{ values}}$ in total.\n\n"
        "**Step 2:** In the stem 3 row, the leaves are 0, 5, 5, 9, representing the numbers: **30, 35, 35, 39**."
    )
    ans = "1. 9 values; 2. 30, 35, 35, 39"
    return {
        "id": f"g7_data_15_{rng.randint(100000, 999999)}",
        "subskill": "15_stem_and_leaf_display_reading_values",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_15",
        "hints": {
            "tier_1": "Count every leaf across all rows for total count.",
            "tier_2": "Combine stem 3 with each leaf: 30, 35, 35, 39.",
            "tier_3": ans
        },
        "misconception_tags": ["counted_stems_instead_of_leaves"]
    }


# 16. Stem and leaf display constructing from data
def arch_16_stem_and_leaf_display_constructing_from_data(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Here are the marks of 8 learners: 15, 23, 18, 31, 27, 23, 19, 34.\n\n"
        "Write down the ordered leaves for the stem 2 row."
    )
    sol = (
        "**Step 1:** Find all numbers in the 20s: 23, 27, 23.\n\n"
        "**Step 2:** Arrange the units digits (leaves) in ascending order: **3, 3, 7**."
    )
    ans = "3, 3, 7"
    return {
        "id": f"g7_data_16_{rng.randint(100000, 999999)}",
        "subskill": "16_stem_and_leaf_display_constructing_from_data",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_16",
        "hints": {
            "tier_1": "Look at numbers starting with 2: 23, 27, 23.",
            "tier_2": "Write leaves in order: 3, 3, 7.",
            "tier_3": ans
        },
        "misconception_tags": ["unordered_stem_and_leaf_leaves"]
    }


# 17. Stem and leaf identifying key
def arch_17_stem_and_leaf_identifying_key(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain why a **Key** (e.g., $4 \\mid 5 = 45$) is essential in any stem-and-leaf display.\n\n"
        "What might $4 \\mid 5$ represent if the dataset recorded race times in seconds and tenths of a second?"
    )
    sol = (
        "**Step 1:** A key is essential because without it, the reader cannot determine the place value represented "
        "(e.g., whether $4 \\mid 5$ means 45, 4,5, or 450).\n\n"
        "**Step 2:** For race times with tenths of a second, $4 \\mid 5$ represents **4,5 seconds**."
    )
    ans = "A key specifies the place value of stem and leaf; for race times, 4 | 5 represents 4,5 seconds."
    return {
        "id": f"g7_data_17_{rng.randint(100000, 999999)}",
        "subskill": "17_stem_and_leaf_identifying_key",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_17",
        "hints": {
            "tier_1": "Does 4 | 5 mean 45 or 4,5?",
            "tier_2": "The key defines the decimal place value.",
            "tier_3": ans
        },
        "misconception_tags": ["stem_and_leaf_key_omission_error"]
    }


# 18. Mode unimodal from raw list
def arch_18_mode_unimodal_from_raw_list(rng: random.Random) -> Dict[str, Any]:
    target_mode = rng.choice([7, 8, 9, 12, 14])
    data = [target_mode, target_mode, target_mode, target_mode - 2, target_mode + 1, target_mode + 3]
    rng.shuffle(data)
    data_str = "; ".join(str(x) for x in data)
    prompt = (
        f"Find the mode of the following data values:\n"
        f"$${data_str}$$\n\n"
        f"Define what the mode means."
    )
    sol = (
        f"**Step 1:** The **mode** is the value that occurs most frequently in a dataset.\n\n"
        f"**Step 2:** Count occurrences:\n"
        f"- {target_mode} appears 3 times (more than any other number).\n\n"
        f"**Mode = {target_mode}**."
    )
    ans = f"{target_mode}"
    return {
        "id": f"g7_data_18_{rng.randint(100000, 999999)}",
        "subskill": "18_mode_unimodal_from_raw_list",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_18",
        "hints": {
            "tier_1": "Which number appears most often?",
            "tier_2": f"{target_mode} appears 3 times.",
            "tier_3": ans
        },
        "misconception_tags": ["mode_confused_with_mean"]
    }


# 19. Mode bimodal or no mode identification
def arch_19_mode_bimodal_or_no_mode_identification(rng: random.Random) -> Dict[str, Any]:
    is_bimodal = rng.choice([True, False])
    if is_bimodal:
        prompt = (
            "Determine the mode(s) of this dataset:\n"
            "$$4; \\quad 7; \\quad 4; \\quad 9; \\quad 7; \\quad 12$$\n\n"
            "State the special term used when a dataset has two modes."
        )
        sol = (
            "**Step 1:** Both 4 and 7 appear twice, which is the highest frequency.\n\n"
            "**Step 2:** The dataset has two modes: **4 and 7**.\n\n"
            "**Term:** The dataset is **bimodal**."
        )
        ans = "Modes: 4 and 7; Term: Bimodal"
    else:
        prompt = (
            "Determine the mode of this dataset:\n"
            "$$3; \\quad 5; \\quad 8; \\quad 11; \\quad 14$$\n\n"
            "Explain your answer."
        )
        sol = (
            "**Step 1:** Every value in the dataset appears exactly once.\n\n"
            "**Conclusion:** There is **no mode** (do NOT write 0, as 0 would mean the number zero is the mode)."
        )
        ans = "No mode (each value appears only once)"
    return {
        "id": f"g7_data_19_{rng.randint(100000, 999999)}",
        "subskill": "19_mode_bimodal_or_no_mode_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_19",
        "hints": {
            "tier_1": "If two numbers tie for highest count, both are modes (bimodal). If all numbers appear once, there is no mode.",
            "tier_2": "Never write 0 for 'no mode'.",
            "tier_3": ans
        },
        "misconception_tags": ["stated_zero_as_mode_when_no_mode"]
    }


# 20. Mode from frequency table
def arch_20_mode_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A survey asked learners for their shoe sizes:\n\n"
        "| Shoe Size | Frequency |\n"
        "| :---: | :---: |\n"
        "| 4 | 5 |\n"
        "| 5 | 14 |\n"
        "| 6 | 11 |\n"
        "| 7 | 8 |\n\n"
        "1. What is the modal shoe size?\n"
        "2. Explain why the mode is 5 and NOT 14."
    )
    sol = (
        "**Step 1:** Look for the highest frequency in the frequency column: 14.\n\n"
        "**Step 2:** Read across to the corresponding shoe size: **Shoe Size 5**.\n\n"
        "**Explanation:** The mode is the data value being measured (Shoe Size 5), while 14 is merely the count (frequency) of that size."
    )
    ans = "1. Shoe size 5; 2. 5 is the actual data value; 14 is just the frequency count."
    return {
        "id": f"g7_data_20_{rng.randint(100000, 999999)}",
        "subskill": "20_mode_from_frequency_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_20",
        "hints": {
            "tier_1": "Find the biggest frequency, then look at the shoe size next to it.",
            "tier_2": "The mode is the shoe size (5), not the frequency (14).",
            "tier_3": ans
        },
        "misconception_tags": ["confused_frequency_with_mode_value"]
    }


# 21. Median odd number of data values
def arch_21_median_odd_number_of_data_values(rng: random.Random) -> Dict[str, Any]:
    # 7 values: 3, 5, 7, [9], 12, 15, 18
    raw = [12, 3, 18, 7, 5, 15, 9]
    ordered = sorted(raw)
    med = ordered[3] # 9
    raw_str = "; ".join(str(x) for x in raw)
    prompt = (
        f"Find the median of the following set of 7 numbers:\n"
        f"$${raw_str}$$\n\n"
        f"Show your working by first arranging the numbers in order."
    )
    sol = (
        f"**Step 1:** Arrange in ascending order:\n"
        f"$${'; '.join(str(x) for x in ordered)}$$\n\n"
        f"**Step 2:** The median is the middle value ($4\\text{{th}}$ value in a set of 7):\n"
        f"$$\\mathbf{{\\text{{Median}} = {med}}}$$"
    )
    ans = f"{med}"
    return {
        "id": f"g7_data_21_{rng.randint(100000, 999999)}",
        "subskill": "21_median_odd_number_of_data_values",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_21",
        "hints": {
            "tier_1": "First step: ALWAYS order the numbers from smallest to largest.",
            "tier_2": f"Ordered: {'; '.join(str(x) for x in ordered)}. Middle number is {med}.",
            "tier_3": ans
        },
        "misconception_tags": ["median_calculated_without_ordering"]
    }


# 22. Median even number of data values
def arch_22_median_even_number_of_data_values(rng: random.Random) -> Dict[str, Any]:
    # 6 values: 4, 8, 10, 14, 18, 22 -> median = (10+14)/2 = 12
    raw = [14, 4, 22, 8, 18, 10]
    ordered = sorted(raw)
    m1 = ordered[2] # 10
    m2 = ordered[3] # 14
    med = (m1 + m2) / 2 # 12.0
    med_str = f"{int(med) if med.is_integer() else med}"
    prompt = (
        f"Calculate the median of the following 6 numbers:\n"
        f"$${'; '.join(str(x) for x in raw)}$$"
    )
    sol = (
        f"**Step 1:** Arrange in ascending order:\n"
        f"$${'; '.join(str(x) for x in ordered)}$$\n\n"
        f"**Step 2:** For an even number of values ($n = 6$), find the average of the two middle values ({m1} and {m2}):\n"
        f"$$\\text{{Median}} = \\frac{{{m1} + {m2}}}{{2}} = \\frac{{{m1 + m2}}}{{2}} = \\mathbf{{{med_str}}}$$"
    )
    ans = f"{med_str}"
    return {
        "id": f"g7_data_22_{rng.randint(100000, 999999)}",
        "subskill": "22_median_even_number_of_data_values",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_data_22",
        "hints": {
            "tier_1": "Order the list, then take the average of the two middle numbers.",
            "tier_2": f"({m1} + {m2}) / 2 = {med_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["chose_one_of_the_two_middle_values"]
    }


# 23. Median from ordered stem and leaf
def arch_23_median_from_ordered_stem_and_leaf(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Find the median from this stem-and-leaf display of 9 learners' test percentages:\n\n"
        "$$\\begin{array}{r|l}\n"
        "\\text{Stem} & \\text{Leaves} \\\\\n"
        "\\hline\n"
        "4 & 2 \\quad 5 \\\\\n"
        "5 & 1 \\quad 4 \\quad 8 \\\\\n"
        "6 & 0 \\quad 3 \\quad 7 \\\\\n"
        "7 & 2\n"
        "\\end{array}$$\n"
        "**Key:** $5 \\mid 1 = 51$\n\n"
        "Show how you locate the 5th value (the middle value of 9)."
    )
    sol = (
        "**Step 1:** List the 9 values in order:\n"
        "$$42; \\quad 45; \\quad 51; \\quad 54; \\quad \\mathbf{58}; \\quad 60; \\quad 63; \\quad 67; \\quad 72$$\n\n"
        "**Step 2:** The middle value is the 5th number: **58**."
    )
    ans = "58"
    return {
        "id": f"g7_data_23_{rng.randint(100000, 999999)}",
        "subskill": "23_median_from_ordered_stem_and_leaf",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_23",
        "hints": {
            "tier_1": "Count to the 5th leaf in order.",
            "tier_2": "The 5th value is stem 5, leaf 8 = 58.",
            "tier_3": ans
        },
        "misconception_tags": ["stem_and_leaf_median_counting_error"]
    }


# 24. Mean calculation simple integer list
def arch_24_mean_calculation_simple_integer_list(rng: random.Random) -> Dict[str, Any]:
    # 5 numbers with integer mean
    mean_val = rng.choice([10, 12, 14, 15])
    # create 5 numbers summing to 5 * mean_val
    tot = 5 * mean_val
    nums = [mean_val - 4, mean_val - 2, mean_val + 1, mean_val + 2, mean_val + 3]
    rng.shuffle(nums)
    prompt = (
        f"Calculate the mean (average) of the following 5 numbers:\n"
        f"$${'; '.join(str(x) for x in nums)}$$\n\n"
        f"Show both the sum of the values and the division."
    )
    sol = (
        f"**Step 1:** Sum all values:\n"
        f"$$\\text{{Sum}} = {' + '.join(str(x) for x in nums)} = {tot}$$\n\n"
        f"**Step 2:** Divide by the number of values ($n = 5$):\n"
        f"$$\\text{{Mean}} = \\frac{{{tot}}}{{5}} = \\mathbf{{{mean_val}}}$$"
    )
    ans = f"{mean_val}"
    return {
        "id": f"g7_data_24_{rng.randint(100000, 999999)}",
        "subskill": "24_mean_calculation_simple_integer_list",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_24",
        "hints": {
            "tier_1": f"Add the 5 numbers together (sum = {tot}).",
            "tier_2": f"Divide {tot} by 5.",
            "tier_3": ans
        },
        "misconception_tags": ["mean_addition_error"]
    }


# 25. Mean calculation with decimal result
def arch_25_mean_calculation_with_decimal_result(rng: random.Random) -> Dict[str, Any]:
    nums = [12, 15, 18, 21]
    # Sum = 66 / 4 = 16,5
    tot = sum(nums)
    mean_val = tot / len(nums)
    m_str = f"{mean_val}".replace(".", ",")
    prompt = (
        f"Calculate the mean of the numbers: 12, 15, 18, 21.\n\n"
        f"Give your answer in decimal notation."
    )
    sol = (
        f"**Step 1:** Sum the values: $$12 + 15 + 18 + 21 = {tot}$$\n\n"
        f"**Step 2:** Divide by $n = 4$:\n"
        f"$$\\text{{Mean}} = \\frac{{{tot}}}{{4}} = \\mathbf{{{m_str}}}$$"
    )
    ans = f"{m_str}"
    return {
        "id": f"g7_data_25_{rng.randint(100000, 999999)}",
        "subskill": "25_mean_calculation_with_decimal_result",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_data_25",
        "hints": {
            "tier_1": "Sum is 66.",
            "tier_2": "66 / 4 = 16,5.",
            "tier_3": ans
        },
        "misconception_tags": ["truncated_decimal_in_mean_calculation"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
