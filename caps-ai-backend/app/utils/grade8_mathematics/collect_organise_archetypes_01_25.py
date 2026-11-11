"""
Grade 8 Mathematics - Collect, Organise & Summarise Data Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Collect organise and summarise data.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def arch_01_population_vs_sample_identification(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A researcher investigates the favorite sport of all 1 200 learners at Sunrise High School by interviewing 50 learners from various grades.",
         "All 1 200 learners at Sunrise High School", "The 50 interviewed learners"),
        ("A city council surveys 200 residents in Ward 4 to determine whether residents in Ward 4 support a new community park.",
         "All residents living in Ward 4", "The 200 surveyed residents"),
        ("A quality control manager tests 30 light bulbs from a factory batch of 5 000 bulbs.",
         "The entire batch of 5 000 light bulbs", "The 30 tested light bulbs"),
    ]
    context, pop, samp = rng.choice(scenarios)
    target = rng.choice(["Population", "Sample"])
    ans = pop if target == "Population" else samp

    return {
        "title": "Population vs Sample Identification",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "01_population_vs_sample_identification",
        "difficulty": "easy",
        "question_text": (
            f"Consider the research investigation described below:\n\n"
            f"**\"{context}\"**\n\n"
            f"Identify the **{target}** of this study."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Identify {target}: '{ans}' (1 mark)",
        ],
        "hints": [
            "The population is the entire group being studied.",
            "The sample is the smaller subset chosen from the population to provide data.",
            f"The {target} is: {ans}.",
        ],
        "misconception_tags": ["population_sample_confusion"],
        "diagram_spec": None,
    }


def arch_02_identifying_sample_size_adequacy(rng: random.Random) -> Dict[str, Any]:
    pop_size = rng.choice([3000, 5000, 10000])
    samp_size = rng.choice([5, 8, 12])

    return {
        "title": "Evaluating Sample Size Adequacy",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "02_identifying_sample_size_adequacy",
        "difficulty": "easy",
        "question_text": (
            f"A student surveys only **{samp_size} learners** to draw conclusions about the preferences of **{pop_size:,} learners** at a large school.\n\n"
            "Explain why this sample is **not representative**."
        ),
        "correct_answer": "The sample size is too small to reflect the diverse opinions and characteristics of the entire population.",
        "marking_schema": [
            "State that sample size is too small to be representative: 1 mark",
        ],
        "hints": [
            f"Consider the ratio of {samp_size} to {pop_size:,}.",
            "A sample that is too small cannot capture the varied views across different ages, grades, and backgrounds.",
            "The sample size is far too small to be representative.",
        ],
        "misconception_tags": ["sample_size_representativeness_misunderstanding"],
        "diagram_spec": None,
    }


def arch_03_identifying_sampling_bias_location(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("A survey on whether people enjoy reading books is conducted exclusively inside a public library.",
         "library", "People at a library are already enthusiastic readers, creating positive bias."),
        ("A survey on whether teenagers enjoy soccer is conducted outside the gates of a major soccer stadium during a derby match.",
         "soccer stadium", "Spectators attending the match already enjoy soccer, skewing the results."),
        ("A survey on whether fast food should be banned is conducted inside a hamburger restaurant.",
         "hamburger restaurant", "Customers at a fast-food restaurant are more likely to support fast food."),
    ]
    scenario, loc, reason = rng.choice(cases)

    return {
        "title": "Identifying Sampling Bias Location",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "03_identifying_sampling_bias_location",
        "difficulty": "medium",
        "question_text": (
            f"Read the following research method:\n\n"
            f"**\"{scenario}\"**\n\n"
            f"Explain why conducting the survey at this specific location causes **bias**."
        ),
        "correct_answer": reason,
        "marking_schema": [
            f"Explain location bias: {reason} (1 mark)",
        ],
        "hints": [
            "Bias occurs when a sample systematically favors certain outcomes over others.",
            f"Consider who visits a {loc}.",
            f"Explanation: {reason}",
        ],
        "misconception_tags": ["sampling_bias_location_unawareness"],
        "diagram_spec": None,
    }


def arch_04_random_sampling_methods(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Characteristics of Simple Random Sampling",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "04_random_sampling_methods",
        "difficulty": "easy",
        "question_text": (
            "In statistical data collection, what does it mean for a sample to be chosen **at random**?"
        ),
        "correct_answer": "Every member of the population has an equal chance of being selected.",
        "marking_schema": [
            "State that every member has an equal chance of selection: 1 mark",
        ],
        "hints": [
            "Random sampling eliminates human bias in choosing participants.",
            "Each individual item or person must have the exact same probability of being picked.",
            "Definition: Every member of the population has an equal chance of being selected.",
        ],
        "misconception_tags": ["random_sampling_equal_probability_definition"],
        "diagram_spec": None,
    }


def arch_05_questionnaire_open_vs_closed_questions(rng: random.Random) -> Dict[str, Any]:
    q_pairs = [
        ("What is your favorite school subject? (Choose: English / Mathematics / Science / History)", "closed", "It provides a fixed set of predefined options to choose from."),
        ("Describe in your own words what you like most about your school.", "open-ended", "It allows respondents to express their own thoughts freely without restricted options."),
        ("Do you own a smartphone? (Yes / No)", "closed", "It offers only two predetermined choices."),
        ("How can the school tuckshop improve its healthy food menu?", "open-ended", "It invites freeform suggestions and personal opinions."),
    ]
    question_str, q_type, reason = rng.choice(q_pairs)

    return {
        "title": "Questionnaire: Open vs Closed Questions",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "05_questionnaire_open_vs_closed_questions",
        "difficulty": "easy",
        "question_text": (
            f"Consider the following survey question:\n\n"
            f"**\"{question_str}\"**\n\n"
            f"Is this an **open-ended** or a **closed** question? Give a reason."
        ),
        "correct_answer": f"{q_type.capitalize()}, because {reason}",
        "marking_schema": [
            f"Classify as {q_type} with valid reason: 1 mark",
        ],
        "hints": [
            "A closed question provides predefined options or answers (e.g. Yes/No, multiple choice).",
            "An open-ended question allows the respondent to answer in their own words.",
            f"Answer: {q_type.capitalize()} ({reason}).",
        ],
        "misconception_tags": ["open_closed_question_classification_error"],
        "diagram_spec": None,
    }


def arch_06_questionnaire_identifying_leading_or_biased_questions(rng: random.Random) -> Dict[str, Any]:
    biased_q = [
        ("Don't you agree that homework is stressful and should be abolished?",
         "It uses leading phrasing ('Don't you agree') that pushes the respondent toward agreeing."),
        ("Since vegetables taste awful, wouldn't you prefer pizza for lunch every day?",
         "It imposes a negative opinion ('vegetables taste awful') before asking the question."),
        ("Wouldn't you agree that soccer is the most thrilling sport ever invented?",
         "It prompts the respondent to accept that soccer is thrilling rather than asking neutrally."),
    ]
    b_text, b_reason = rng.choice(biased_q)

    return {
        "title": "Identifying Leading Questions in Surveys",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "06_questionnaire_identifying_leading_or_biased_questions",
        "difficulty": "medium",
        "question_text": (
            f"Critique the following questionnaire item:\n\n"
            f"**\"{b_text}\"**\n\n"
            f"Explain why this question is considered **leading** (biased)."
        ),
        "correct_answer": b_reason,
        "marking_schema": [
            f"Identify leading wording: {b_reason} (1 mark)",
        ],
        "hints": [
            "A leading question suggests a particular answer or assumes a point of view.",
            "Neutral questions avoid words like 'Don't you agree' or emotional adjectives.",
            f"Explanation: {b_reason}.",
        ],
        "misconception_tags": ["leading_question_bias_identification_error"],
        "diagram_spec": None,
    }


def arch_07_tally_table_counting_frequencies_from_raw_data(rng: random.Random) -> Dict[str, Any]:
    options = ["Apple", "Banana", "Orange", "Pear"]
    counts = [rng.randint(3, 7) for _ in options]
    data_list = []
    for opt, cnt in zip(options, counts):
        data_list.extend([opt] * cnt)
    rng.shuffle(data_list)

    target_fruit = rng.choice(options)
    target_count = counts[options.index(target_fruit)]
    data_str = ", ".join(data_list)

    return {
        "title": "Tally Table: Frequency from Raw Data",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "07_tally_table_counting_frequencies_from_raw_data",
        "difficulty": "easy",
        "question_text": (
            f"A survey asked learners to choose their favorite fruit. The responses were recorded as follows:\n\n"
            f"{data_str}\n\n"
            f"What is the frequency of **{target_fruit}**?"
        ),
        "correct_answer": str(target_count),
        "marking_schema": [
            f"Count occurrences of {target_fruit}: {target_count} (1 mark)",
        ],
        "hints": [
            f"Tally each time '{target_fruit}' appears in the list.",
            "Group tallies into bundles of five (|||| with a slash).",
            f"Frequency = {target_count}.",
        ],
        "misconception_tags": ["tally_counting_missed_entry_slip"],
        "diagram_spec": None,
    }


def arch_08_tally_table_calculating_missing_frequency_given_total(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([30, 40, 50])
    f1 = rng.randint(6, 12)
    f2 = rng.randint(8, 14)
    f3 = rng.randint(4, 9)
    missing_f = total - (f1 + f2 + f3)

    return {
        "title": "Tally Table: Calculating Missing Frequency",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "08_tally_table_calculating_missing_frequency_given_total",
        "difficulty": "medium",
        "question_text": (
            f"A frequency table records transport modes for a total of **{total} learners**:\n\n"
            f"| Mode | Frequency |\n"
            f"| :--- | :---: |\n"
            f"| Bus | {f1} |\n"
            f"| Taxi | {f2} |\n"
            f"| Walking | {f3} |\n"
            f"| Bicycle | $x$ |\n"
            f"| **Total** | **{total}** |\n\n"
            f"Calculate the missing frequency $x$ for Bicycle."
        ),
        "correct_answer": str(missing_f),
        "marking_schema": [
            f"Subtract known frequencies from total: {total} - ({f1} + {f2} + {f3}) = {missing_f} (1 mark)",
        ],
        "hints": [
            "The sum of all frequencies must equal the total number of learners.",
            f"${f1} + {f2} + {f3} + x = {total}$.",
            f"$x = {total} - {f1 + f2 + f3} = {missing_f}$.",
        ],
        "misconception_tags": ["frequency_sum_subtraction_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_09_tally_table_identifying_mode_category(rng: random.Random) -> Dict[str, Any]:
    cats = ["Red", "Blue", "Green", "Yellow"]
    freqs = [rng.randint(5, 12) for _ in cats]
    max_idx = rng.randint(0, 3)
    freqs[max_idx] = max(freqs) + rng.randint(3, 6)
    mode_cat = cats[max_idx]

    return {
        "title": "Identifying Mode Category from Frequency Table",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "09_tally_table_identifying_mode_category",
        "difficulty": "easy",
        "question_text": (
            "Refer to the frequency table below showing favorite colors:\n\n"
            f"| Color | Frequency |\n"
            f"| :--- | :---: |\n"
            f"| {cats[0]} | {freqs[0]} |\n"
            f"| {cats[1]} | {freqs[1]} |\n"
            f"| {cats[2]} | {freqs[2]} |\n"
            f"| {cats[3]} | {freqs[3]} |\n\n"
            "Which color is the **mode** (modal category)?"
        ),
        "correct_answer": mode_cat,
        "marking_schema": [
            f"Identify category with highest frequency: {mode_cat} ({freqs[max_idx]}) (1 mark)",
        ],
        "hints": [
            "The mode is the category with the highest frequency.",
            f"Compare frequencies: {freqs[0]}, {freqs[1]}, {freqs[2]}, {freqs[3]}.",
            f"Highest frequency is {freqs[max_idx]}, which corresponds to {mode_cat}.",
        ],
        "misconception_tags": ["mode_value_vs_frequency_confusion"],
        "diagram_spec": None,
    }


def arch_10_tally_table_calculating_percentage_frequency(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([20, 25, 40, 50])
    count = rng.choice([4, 5, 8, 10, 12])
    pct = int((count / total) * 100)

    return {
        "title": "Percentage Frequency Calculation",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "10_tally_table_calculating_percentage_frequency",
        "difficulty": "medium",
        "question_text": (
            f"In a survey of **{total} learners**, exactly **{count} learners** walk to school.\n\n"
            f"What percentage of the surveyed learners walk to school?"
        ),
        "correct_answer": f"{pct}%",
        "marking_schema": [
            f"Calculate percentage: ({count} / {total}) * 100% = {pct}% (1 mark)",
        ],
        "hints": [
            f"Formula: $\\text{{Percentage}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total}}}} \\times 100\\%$.",
            f"$\\frac{{{count}}}{{{total}}} \\times 100\\% = {pct}\\%$.",
            f"Answer: {pct}%.",
        ],
        "misconception_tags": ["percentage_frequency_total_scaling_error"],
        "diagram_spec": None,
    }


def arch_11_grouped_data_identifying_class_interval_for_score(rng: random.Random) -> Dict[str, Any]:
    intervals = ["40 - 49", "50 - 59", "60 - 69", "70 - 79"]
    chosen_idx = rng.randint(0, 3)
    target_interval = intervals[chosen_idx]
    low = 40 + chosen_idx * 10
    score = low + rng.randint(1, 8)

    return {
        "title": "Grouped Data: Class Interval Placement",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "11_grouped_data_identifying_class_interval_for_score",
        "difficulty": "easy",
        "question_text": (
            "Test scores are grouped into class intervals: **40 - 49**, **50 - 59**, **60 - 69**, and **70 - 79**.\n\n"
            f"In which class interval should a test mark of **{score}%** be placed?"
        ),
        "correct_answer": target_interval,
        "marking_schema": [
            f"Place score in interval: {target_interval} (1 mark)",
        ],
        "hints": [
            f"Check which range contains the mark {score}.",
            f"{score} lies between {low} and {low + 9}.",
            f"Interval: {target_interval}.",
        ],
        "misconception_tags": ["class_interval_boundary_confusion"],
        "diagram_spec": None,
    }


def arch_12_grouped_data_determining_interval_width(rng: random.Random) -> Dict[str, Any]:
    width = rng.choice([5, 10, 20])
    start = rng.choice([10, 20, 30])
    int_str = f"{start} - {start + width - 1}"

    return {
        "title": "Determining Class Interval Width",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "12_grouped_data_determining_interval_width",
        "difficulty": "medium",
        "question_text": (
            f"Consider the class interval of discrete integer scores **{int_str}**.\n\n"
            f"What is the **class width** (the number of discrete integer values contained in this interval)?"
        ),
        "correct_answer": str(width),
        "marking_schema": [
            f"Calculate width: ({start + width - 1} - {start}) + 1 = {width} (1 mark)",
        ],
        "hints": [
            "For inclusive discrete integer intervals, width = (upper limit - lower limit) + 1.",
            f"Width = $({start + width - 1} - {start}) + 1 = {width}$.",
            f"Class width = {width}.",
        ],
        "misconception_tags": ["class_width_off_by_one_subtraction_error"],
        "diagram_spec": None,
    }


def arch_13_grouped_data_explaining_non_overlapping_intervals(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Why Class Intervals Must Not Overlap",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "13_grouped_data_explaining_non_overlapping_intervals",
        "difficulty": "medium",
        "question_text": (
            "Explain why class intervals for test percentages are written as **50 - 59** and **60 - 69**, "
            "rather than **50 - 60** and **60 - 70**."
        ),
        "correct_answer": "To prevent ambiguity and double-counting scores at boundary points such as 60.",
        "marking_schema": [
            "Explain that non-overlapping intervals ensure every value belongs to exactly one interval without ambiguity: 1 mark",
        ],
        "hints": [
            "Consider what would happen if a learner scored exactly 60%.",
            "If intervals were 50-60 and 60-70, it would be unclear which interval 60 belongs to, risking double-counting.",
            "Non-overlapping intervals ensure each data point falls into exactly one unique category.",
        ],
        "misconception_tags": ["interval_boundary_double_counting_misconception"],
        "diagram_spec": None,
    }


def arch_14_grouped_data_identifying_modal_class_interval(rng: random.Random) -> Dict[str, Any]:
    intervals = ["20 - 29", "30 - 39", "40 - 49", "50 - 59"]
    freqs = [rng.randint(3, 8), rng.randint(4, 9), rng.randint(12, 18), rng.randint(5, 10)]
    modal_idx = freqs.index(max(freqs))
    modal_int = intervals[modal_idx]

    return {
        "title": "Identifying Modal Class Interval",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "14_grouped_data_identifying_modal_class_interval",
        "difficulty": "easy",
        "question_text": (
            "Consider the grouped frequency distribution below:\n\n"
            f"| Score Interval | Frequency |\n"
            f"| :--- | :---: |\n"
            f"| {intervals[0]} | {freqs[0]} |\n"
            f"| {intervals[1]} | {freqs[1]} |\n"
            f"| {intervals[2]} | {freqs[2]} |\n"
            f"| {intervals[3]} | {freqs[3]} |\n\n"
            "Identify the **modal class interval**."
        ),
        "correct_answer": modal_int,
        "marking_schema": [
            f"Identify interval with highest frequency ({max(freqs)}): {modal_int} (1 mark)",
        ],
        "hints": [
            "The modal class interval is the interval that contains the highest frequency.",
            f"The highest frequency is {max(freqs)}.",
            f"Modal class interval: {modal_int}.",
        ],
        "misconception_tags": ["modal_interval_frequency_inversion"],
        "diagram_spec": None,
    }


def arch_15_grouped_data_calculating_total_sample_size_from_frequencies(rng: random.Random) -> Dict[str, Any]:
    freqs = [rng.randint(6, 15) for _ in range(4)]
    total = sum(freqs)

    return {
        "title": "Total Sample Size from Frequency Distribution",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "15_grouped_data_calculating_total_sample_size_from_frequencies",
        "difficulty": "easy",
        "question_text": (
            "A grouped frequency table has frequencies of **"
            f"{freqs[0]}, {freqs[1]}, {freqs[2]}, and {freqs[3]}** across its four intervals.\n\n"
            "Calculate the total number of observations ($N$) in this sample."
        ),
        "correct_answer": str(total),
        "marking_schema": [
            f"Sum all frequencies: {freqs[0]} + {freqs[1]} + {freqs[2]} + {freqs[3]} = {total} (1 mark)",
        ],
        "hints": [
            "The total sample size is the sum of all class frequencies: $N = \\sum f$.",
            f"$N = {freqs[0]} + {freqs[1]} + {freqs[2]} + {freqs[3]}$.",
            f"Total = {total}.",
        ],
        "misconception_tags": ["frequency_sum_omission_slip"],
        "diagram_spec": None,
    }


def arch_16_grouped_data_frequency_percentage_calculation(rng: random.Random) -> Dict[str, Any]:
    f_target = rng.choice([6, 8, 10, 12])
    total = rng.choice([25, 40, 50])
    pct = (f_target / total) * 100

    pct_str = f"{pct:.1f}".rstrip("0").rstrip(".").replace(".", ",")

    return {
        "title": "Percentage of Learners in Class Interval",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "16_grouped_data_frequency_percentage_calculation",
        "difficulty": "medium",
        "question_text": (
            f"In a test administered to **{total} learners**, **{f_target} learners** scored within the 70 - 79 interval.\n\n"
            f"What percentage of the learners scored in this interval?"
        ),
        "correct_answer": f"{pct_str}%",
        "marking_schema": [
            f"Calculate percentage: ({f_target}/{total}) * 100% = {pct_str}% (1 mark)",
        ],
        "hints": [
            f"Divide frequency by total and multiply by 100%: $\\frac{{{f_target}}}{{{total}}} \\times 100\\%$.",
            f"Percentage = {pct_str}%.",
        ],
        "misconception_tags": ["percentage_calculation_order_slip"],
        "diagram_spec": None,
    }


def arch_17_stem_and_leaf_interpreting_key(rng: random.Random) -> Dict[str, Any]:
    stem = rng.choice([2, 3, 4, 5])
    leaf = rng.choice([1, 4, 7, 8])
    val = stem * 10 + leaf

    return {
        "title": "Interpreting Stem-and-Leaf Key",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "17_stem_and_leaf_interpreting_key",
        "difficulty": "easy",
        "question_text": (
            f"In a stem-and-leaf display representing learner test percentages, the key is given as:\n\n"
            f"$$\\text{{Key: }} {stem} \\mid {leaf} = {val}\\%$$\n\n"
            f"What test percentage is represented by the entry **${stem} \\mid {leaf}$**?"
        ),
        "correct_answer": f"{val}%",
        "marking_schema": [
            f"Interpret key: {val}% (1 mark)",
        ],
        "hints": [
            "The stem represents the tens digit and the leaf represents the units digit.",
            f"${stem} \\text{{ tens}} + {leaf} \\text{{ units}} = {val}$.",
            f"Value = {val}%.",
        ],
        "misconception_tags": ["stem_and_leaf_key_misinterpretation"],
        "diagram_spec": None,
    }


def arch_18_stem_and_leaf_identifying_minimum_and_maximum(rng: random.Random) -> Dict[str, Any]:
    min_stem, min_leaf = 2, rng.choice([1, 3, 5])
    max_stem, max_leaf = 5, rng.choice([4, 6, 9])
    min_val = min_stem * 10 + min_leaf
    max_val = max_stem * 10 + max_leaf

    return {
        "title": "Reading Minimum and Maximum from Stem-and-Leaf",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "18_stem_and_leaf_identifying_minimum_and_maximum",
        "difficulty": "medium",
        "question_text": (
            "Refer to the stem-and-leaf display below:\n\n"
            "$$\\begin{array}{r|l}\n"
            f"2 & {min_leaf} \\quad 7 \\quad 8 \\\\\n"
            "3 & 0 \\quad 4 \\quad 5 \\\\\n"
            "4 & 2 \\quad 3 \\quad 6 \\\\\n"
            f"5 & 1 \\quad {max_leaf}\n"
            "\\end{array}$$\n"
            "$$\\text{Key: } 3 \\mid 4 = 34$$\n\n"
            "Write down the **minimum** and **maximum** values in this data set."
        ),
        "correct_answer": f"Minimum = {min_val}, Maximum = {max_val}",
        "marking_schema": [
            f"Minimum = {min_val} [1 mark], Maximum = {max_val} [1 mark]",
        ],
        "hints": [
            f"The minimum value is the first leaf of the first stem: $2 \\mid {min_leaf} = {min_val}$.",
            f"The maximum value is the last leaf of the last stem: $5 \\mid {max_leaf} = {max_val}$.",
            f"Minimum = {min_val}; Maximum = {max_val}.",
        ],
        "misconception_tags": ["stem_and_leaf_extremes_omission"],
        "diagram_spec": None,
    }


def arch_19_stem_and_leaf_calculating_range(rng: random.Random) -> Dict[str, Any]:
    min_val = rng.randint(21, 26)
    max_val = rng.randint(55, 68)
    rng_val = max_val - min_val

    return {
        "title": "Calculating Range from Stem-and-Leaf Display",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "19_stem_and_leaf_calculating_range",
        "difficulty": "medium",
        "question_text": (
            "In an ordered stem-and-leaf display, the lowest value is **"
            f"{min_val}** and the highest value is **{max_val}**.\n\n"
            "Calculate the **range** of this data set."
        ),
        "correct_answer": str(rng_val),
        "marking_schema": [
            f"Range = maximum - minimum = {max_val} - {min_val} = {rng_val} (1 mark)",
        ],
        "hints": [
            "Formula: $\\text{Range} = \\text{Maximum} - \\text{Minimum}$.",
            f"$\\text{{Range}} = {max_val} - {min_val} = {rng_val}$.",
            f"Range = {rng_val}.",
        ],
        "misconception_tags": ["range_formula_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_20_stem_and_leaf_identifying_mode(rng: random.Random) -> Dict[str, Any]:
    mode_stem = rng.choice([3, 4])
    mode_leaf = rng.choice([2, 5, 8])
    mode_val = mode_stem * 10 + mode_leaf

    return {
        "title": "Finding Mode from Stem-and-Leaf Display",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "20_stem_and_leaf_identifying_mode",
        "difficulty": "medium",
        "question_text": (
            "Look at the stem-and-leaf display below:\n\n"
            "$$\\begin{array}{r|l}\n"
            f"3 & 1 \\quad {mode_leaf} \\quad {mode_leaf} \\quad {mode_leaf} \\quad 7 \\\\\n"
            "4 & 0 \\quad 3 \\quad 6 \\\\\n"
            "5 & 2 \\quad 5\n"
            "\\end{array}$$\n"
            "$$\\text{Key: } 3 \\mid 1 = 31$$\n\n"
            "Identify the **mode** of this data set."
        ),
        "correct_answer": str(mode_val),
        "marking_schema": [
            f"Identify most repeated value: {mode_val} (appears 3 times) (1 mark)",
        ],
        "hints": [
            "The mode is the value that appears most frequently.",
            f"On stem 3, leaf {mode_leaf} repeats three times.",
            f"The mode is $3 \\mid {mode_leaf} = {mode_val}$.",
        ],
        "misconception_tags": ["stem_and_leaf_mode_leaf_only_error"],
        "diagram_spec": None,
    }


def arch_21_stem_and_leaf_finding_median_odd_count(rng: random.Random) -> Dict[str, Any]:
    # 9 numbers
    leaves_stem2 = [2, 4, 7]
    leaves_stem3 = [1, 3, 5]
    leaves_stem4 = [0, 6, 8]
    # Total 9 items: median is 5th item
    # 1: 22, 2: 24, 3: 27, 4: 31, 5: 33 (median)
    med_val = 33

    return {
        "title": "Finding Median from Stem-and-Leaf (Odd Count)",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "21_stem_and_leaf_finding_median_odd_count",
        "difficulty": "medium",
        "question_text": (
            "Refer to the ordered stem-and-leaf display below containing 9 data values:\n\n"
            "$$\\begin{array}{r|l}\n"
            "2 & 2 \\quad 4 \\quad 7 \\\\\n"
            "3 & 1 \\quad 3 \\quad 5 \\\\\n"
            "4 & 0 \\quad 6 \\quad 8\n"
            "\\end{array}$$\n"
            "$$\\text{Key: } 2 \\mid 2 = 22$$\n\n"
            "Determine the **median** of this data set."
        ),
        "correct_answer": str(med_val),
        "marking_schema": [
            f"Find 5th ordered position: {med_val} (2 marks)",
        ],
        "hints": [
            "With $N = 9$ values, the median is at position $\\frac{9 + 1}{2} = 5^{\\text{th}}$ item.",
            "Count leaves from the top: 22, 24, 27, 31, 33.",
            f"The 5th value is {med_val}.",
        ],
        "misconception_tags": ["median_position_counting_error"],
        "diagram_spec": None,
    }


def arch_22_stem_and_leaf_finding_median_even_count(rng: random.Random) -> Dict[str, Any]:
    # 10 values: median is average of 5th and 6th items
    # 2 | 2, 4, 6, 8
    # 3 | 0, 4, 6
    # 4 | 1, 3, 5
    # 1:22, 2:24, 3:26, 4:28, 5:30, 6:34, ...
    # median = (30 + 34)/2 = 32
    med_val = 32

    return {
        "title": "Finding Median from Stem-and-Leaf (Even Count)",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "22_stem_and_leaf_finding_median_even_count",
        "difficulty": "hard",
        "question_text": (
            "Refer to the ordered stem-and-leaf display below containing 10 scores:\n\n"
            "$$\\begin{array}{r|l}\n"
            "2 & 2 \\quad 4 \\quad 6 \\quad 8 \\\\\n"
            "3 & 0 \\quad 4 \\quad 6 \\\\\n"
            "4 & 1 \\quad 3 \\quad 5\n"
            "\\end{array}$$\n"
            "$$\\text{Key: } 3 \\mid 0 = 30$$\n\n"
            "Calculate the **median** score."
        ),
        "correct_answer": str(med_val),
        "marking_schema": [
            f"Average 5th (30) and 6th (34) values: (30 + 34)/2 = {med_val} (2 marks)",
        ],
        "hints": [
            "With $N = 10$ values, the median is the average of the 5th and 6th ordered values.",
            "5th value = 30; 6th value = 34.",
            f"Median = $\\frac{{30 + 34}}{{2}} = {med_val}$.",
        ],
        "misconception_tags": ["median_even_count_single_middle_error"],
        "diagram_spec": None,
    }


def arch_23_stem_and_leaf_total_count_of_observations(rng: random.Random) -> Dict[str, Any]:
    n_leaves = rng.randint(12, 18)

    return {
        "title": "Counting Observations from Stem-and-Leaf",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "23_stem_and_leaf_total_count_of_observations",
        "difficulty": "easy",
        "question_text": (
            f"A stem-and-leaf display contains a total of **{n_leaves} leaves** across four stems.\n\n"
            "How many individual data observations ($N$) are represented in this display?"
        ),
        "correct_answer": str(n_leaves),
        "marking_schema": [
            f"State total observations = total leaves = {n_leaves} (1 mark)",
        ],
        "hints": [
            "In any stem-and-leaf display, each individual leaf corresponds to exactly one data value.",
            f"Since there are {n_leaves} leaves, there are {n_leaves} observations.",
            f"Total = {n_leaves}.",
        ],
        "misconception_tags": ["stem_counting_as_observation_error"],
        "diagram_spec": None,
    }


def arch_24_stem_and_leaf_counting_values_above_or_below_threshold(rng: random.Random) -> Dict[str, Any]:
    # Stem 3 (30s) and Stem 4 (40s)
    # Threshold 40: values >= 40
    n_stem4 = rng.randint(3, 6)
    n_stem5 = rng.randint(2, 4)
    total_above = n_stem4 + n_stem5

    return {
        "title": "Counting Values Above a Threshold in Stem-and-Leaf",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "24_stem_and_leaf_counting_values_above_or_below_threshold",
        "difficulty": "medium",
        "question_text": (
            "In a stem-and-leaf display, there are 4 leaves on stem 2, 5 leaves on stem 3, "
            f"**{n_stem4} leaves on stem 4**, and **{n_stem5} leaves on stem 5** (Key: $3 \\mid 2 = 32$).\n\n"
            "How many data values in this sample are **greater than or equal to 40**?"
        ),
        "correct_answer": str(total_above),
        "marking_schema": [
            f"Add leaves on stems 4 and 5: {n_stem4} + {n_stem5} = {total_above} (1 mark)",
        ],
        "hints": [
            "Values >= 40 correspond to all data on stem 4 (the 40s) and stem 5 (the 50s).",
            f"Count: {n_stem4} + {n_stem5} = {total_above}.",
            f"Answer: {total_above} values.",
        ],
        "misconception_tags": ["threshold_leaf_counting_misalignment"],
        "diagram_spec": None,
    }


def arch_25_stem_and_leaf_constructing_leaves_from_raw_scores(rng: random.Random) -> Dict[str, Any]:
    units = sorted(rng.sample(range(0, 10), 4))
    tens = rng.choice([3, 4, 5])
    raw_scores = [tens * 10 + u for u in units]
    raw_str = ", ".join(str(s) for s in raw_scores)
    ans_leaves = " ".join(str(u) for u in units)

    return {
        "title": "Constructing Leaves for a Specific Stem",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "25_stem_and_leaf_constructing_leaves_from_raw_scores",
        "difficulty": "medium",
        "question_text": (
            f"From a raw list of marks, four scores belong in the {tens}0s: **{raw_str}**.\n\n"
            f"Write down the ordered leaves that should be entered next to **stem {tens}** (separated by spaces)."
        ),
        "correct_answer": ans_leaves,
        "marking_schema": [
            f"List ordered units digits: {ans_leaves} (1 mark)",
        ],
        "hints": [
            f"The stem is {tens}. Extract the units digit from each score in the {tens}0s.",
            f"Sort the units digits in ascending order: {ans_leaves}.",
            f"Leaves for stem {tens}: {ans_leaves}.",
        ],
        "misconception_tags": ["unordered_leaves_in_stem_and_leaf"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_population_vs_sample_identification,
    arch_02_identifying_sample_size_adequacy,
    arch_03_identifying_sampling_bias_location,
    arch_04_random_sampling_methods,
    arch_05_questionnaire_open_vs_closed_questions,
    arch_06_questionnaire_identifying_leading_or_biased_questions,
    arch_07_tally_table_counting_frequencies_from_raw_data,
    arch_08_tally_table_calculating_missing_frequency_given_total,
    arch_09_tally_table_identifying_mode_category,
    arch_10_tally_table_calculating_percentage_frequency,
    arch_11_grouped_data_identifying_class_interval_for_score,
    arch_12_grouped_data_determining_interval_width,
    arch_13_grouped_data_explaining_non_overlapping_intervals,
    arch_14_grouped_data_identifying_modal_class_interval,
    arch_15_grouped_data_calculating_total_sample_size_from_frequencies,
    arch_16_grouped_data_frequency_percentage_calculation,
    arch_17_stem_and_leaf_interpreting_key,
    arch_18_stem_and_leaf_identifying_minimum_and_maximum,
    arch_19_stem_and_leaf_calculating_range,
    arch_20_stem_and_leaf_identifying_mode,
    arch_21_stem_and_leaf_finding_median_odd_count,
    arch_22_stem_and_leaf_finding_median_even_count,
    arch_23_stem_and_leaf_total_count_of_observations,
    arch_24_stem_and_leaf_counting_values_above_or_below_threshold,
    arch_25_stem_and_leaf_constructing_leaves_from_raw_scores,
]
