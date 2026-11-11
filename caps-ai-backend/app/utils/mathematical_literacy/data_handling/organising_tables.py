"""Cluster 2: Organising Data & Frequency Tables (Subskills 9 to 16).

Covers:
9. Tally marks conversion to numerical frequency counts (bundles of 5)
10. Total sample size calculation from frequency distribution sum
11. Relative frequency proportion and percentage calculations
12. Grouped frequency intervals and modal class identification
13. Stem-and-leaf display interpretation (reading stems, leaves, keys)
14. Two-way contingency tables (joint frequencies and marginal totals)
15. Missing frequency reconstruction from grand totals (algebraic deduction)
16. Cumulative frequency column construction and running totals
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_data_table_tally_marks_to_frequency_conversion(r: random.Random) -> Dict[str, Any]:
    category = r.choice(["Red cars", "Learners with brown eyes", "Households with solar geysers", "Grade 10 soccer players"])
    fives = r.randint(2, 6)
    singles = r.randint(1, 4)
    total_count = fives * 5 + singles
    tally_str = " ".join(["||||/"] * fives) + " " + "|" * singles

    prompt = (
        f"In a traffic survey, a learner uses standard tally marks to record the frequency of **{category}**.\n\n"
        f"The tally recorded on the observation sheet is:\n"
        f"**{tally_str}**\n\n"
        f"(Note: Each crossed bundle '||||/' represents 5 items, and each single '|' represents 1 item).\n\n"
        f"Convert this tally into the exact numerical frequency count."
    )
    ans = f"{total_count}"

    s1 = f"Count the number of full 5-bundles ({fives} × 5 = {fives * 5}) and add the remaining single tally marks ({singles})."
    s2 = f"✓ [1 Mark: Method – Tally bundle calculation]\nFrequency = ({fives} bundles × 5) + {singles} singles = {fives * 5} + {singles}."
    s3 = f"✓ [1 Mark: Accuracy – Total frequency]\nNumerical frequency = {total_count}."

    return _build_question_payload(
        "data_table_tally_marks_to_frequency_conversion",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Count how many bundles of 5 you see ({fives}), and how many single strokes ({singles}).",
        tier_2_hint=f"({fives} × 5) + {singles} = {fives * 5} + {singles}.",
        tier_3_hint=f"Total frequency = {total_count}.",
    )


def _gen_data_table_total_frequency_sum(r: random.Random) -> Dict[str, Any]:
    f1, f2, f3, f4, f5 = r.randint(8, 25), r.randint(12, 30), r.randint(15, 35), r.randint(10, 28), r.randint(5, 20)
    total_n = f1 + f2 + f3 + f4 + f5

    prompt = (
        f"A survey on weekly internet data bundle purchases by Grade 10 learners produced the following frequency table:\n\n"
        f"| Data Bundle Size | Frequency (Number of Learners) |\n"
        f"| :--- | :---: |\n"
        f"| 500 MB | {f1} |\n"
        f"| 1 GB | {f2} |\n"
        f"| 2 GB | {f3} |\n"
        f"| 5 GB | {f4} |\n"
        f"| 10 GB+ | {f5} |\n\n"
        f"Calculate the total sample size (total number of learners surveyed), n = ∑ f."
    )
    ans = f"{total_n} learners"

    s1 = f"Sum all individual class frequencies in the table to determine the total sample size (n = {f1} + {f2} + {f3} + {f4} + {f5})."
    s2 = f"✓ [1 Mark: Method – Summing all category frequencies]\nTotal n = {f1} + {f2} + {f3} + {f4} + {f5}."
    s3 = f"✓ [1 Mark: Accuracy – Total sample size]\nTotal = {total_n} learners."

    return _build_question_payload(
        "data_table_total_frequency_sum",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add all the frequencies together: {f1} + {f2} + {f3} + {f4} + {f5}.",
        tier_2_hint=f"Sum = {f1} + {f2} + {f3} + {f4} + {f5}.",
        tier_3_hint=f"Total = {total_n} learners.",
    )


def _gen_data_table_relative_frequency_percentage(r: random.Random) -> Dict[str, Any]:
    total_n = r.choice([40, 50, 80, 100, 200])
    target_f = r.choice([12, 15, 18, 24, 30, 45])
    while target_f >= total_n:
        target_f = target_f // 2
    pct = round((target_f / total_n) * 100, 1)

    prompt = (
        f"In a sample of {total_n} randomly chosen households in an eThekwini ward, exactly "
        f"{target_f} households reported having a JoJo rainwater harvesting tank installed.\n\n"
        f"Formula: Relative Frequency (%) = (Frequency ÷ Total Sample Size) × 100%\n\n"
        f"Calculate the percentage relative frequency of households with rainwater tanks (rounded to 1 decimal place)."
    )
    ans = f"{_fmt(pct)}%"

    s1 = f"Divide the category frequency ({target_f}) by the total sample size ({total_n}) and multiply by 100 to convert to a percentage."
    s2 = f"✓ [1 Mark: Method – Relative frequency formula setup]\nPercentage = ({target_f} ÷ {total_n}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Percentage relative frequency]\nRelative frequency = {_fmt(pct)}%."

    return _build_question_payload(
        "data_table_relative_frequency_percentage",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {target_f} by {total_n} and multiply by 100.",
        tier_2_hint=f"({target_f} ÷ {total_n}) × 100 = {_fmt(pct)}%.",
        tier_3_hint=f"Relative frequency = {_fmt(pct)}%.",
    )


def _gen_data_table_grouped_intervals_modal_class(r: random.Random) -> Dict[str, Any]:
    classes = ["10 – 19", "20 – 29", "30 – 39", "40 – 49", "50 – 59"]
    freqs = [r.randint(5, 15), r.randint(18, 28), r.randint(30, 45), r.randint(15, 25), r.randint(6, 14)]
    max_f = max(freqs)
    modal_idx = freqs.index(max_f)
    modal_interval = classes[modal_idx]

    prompt = (
        f"The test marks of a Grade 10 Mathematical Literacy class are organised into the following grouped frequency table:\n\n"
        f"| Mark Interval (%) | Frequency (Number of Learners) |\n"
        f"| :---: | :---: |\n"
        f"| 10 – 19 | {freqs[0]} |\n"
        f"| 20 – 29 | {freqs[1]} |\n"
        f"| 30 – 39 | {freqs[2]} |\n"
        f"| 40 – 49 | {freqs[3]} |\n"
        f"| 50 – 59 | {freqs[4]} |\n\n"
        f"1. Identify the highest frequency in the table.\n"
        f"2. State the **modal class interval** of this dataset."
    )
    ans = f"Modal class interval: {modal_interval} (highest frequency of {max_f} learners)"

    s1 = f"Identify the class interval with the greatest frequency count in the table."
    s2 = f"✓ [1 Mark: Method – Identifying maximum frequency in grouped table]\nHighest frequency = {max_f} in row '{modal_interval}'."
    s3 = f"✓ [1 Mark: Accuracy – Modal interval identification]\nModal class: {modal_interval}."

    return _build_question_payload(
        "data_table_grouped_intervals_modal_class",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the largest number in the frequency column.",
        tier_2_hint=f"The largest frequency is {max_f}, which belongs to mark interval {modal_interval}.",
        tier_3_hint=f"Modal class interval = {modal_interval}.",
    )


def _gen_data_table_stem_and_leaf_display_reading(r: random.Random) -> Dict[str, Any]:
    # Stem represents tens, leaf represents units
    stem_2 = sorted([r.randint(1, 9) for _ in range(r.randint(2, 4))])
    stem_3 = sorted([r.randint(0, 9) for _ in range(r.randint(3, 5))])
    stem_4 = sorted([r.randint(0, 9) for _ in range(r.randint(3, 5))])
    stem_5 = sorted([r.randint(0, 8) for _ in range(r.randint(2, 4))])

    leaves_str_2 = " ".join(map(str, stem_2))
    leaves_str_3 = " ".join(map(str, stem_3))
    leaves_str_4 = " ".join(map(str, stem_4))
    leaves_str_5 = " ".join(map(str, stem_5))

    total_data_points = len(stem_2) + len(stem_3) + len(stem_4) + len(stem_5)
    min_val = 20 + stem_2[0]
    max_val = 50 + stem_5[-1]

    prompt = (
        f"The ages of staff members at a community medical clinic are displayed in the stem-and-leaf plot below:\n\n"
        f"**Stem | Leaf**\n"
        f"  2   | {leaves_str_2}\n"
        f"  3   | {leaves_str_3}\n"
        f"  4   | {leaves_str_4}\n"
        f"  5   | {leaves_str_5}\n\n"
        f"**Key**: 3 | 5 represents an age of 35 years.\n\n"
        f"1. How many total staff members are recorded in this plot?\n"
        f"2. What is the age of the youngest staff member?\n"
        f"3. What is the age of the oldest staff member?"
    )
    ans = f"Total = {total_data_points} staff members; Youngest = {min_val} years; Oldest = {max_val} years"

    s1 = f"Count total leaf digits across all rows to find total sample size ({total_data_points}). Combine first stem with first leaf for minimum ({min_val}) and last stem with last leaf for maximum ({max_val})."
    s2 = f"✓ [1 Mark: Method – Reading stem-and-leaf conventions]\nTotal leaves = {len(stem_2)} + {len(stem_3)} + {len(stem_4)} + {len(stem_5)} = {total_data_points}.\nMinimum = 20 + {stem_2[0]} = {min_val}.\nMaximum = 50 + {stem_5[-1]} = {max_val}."
    s3 = f"✓ [1 Mark: Accuracy – Total count, minimum and maximum values]\n{ans}"

    return _build_question_payload(
        "data_table_stem_and_leaf_display_reading",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Count every leaf digit to find the total number of people.",
        tier_2_hint=f"The first leaf in row 2 gives {min_val} years; the last leaf in row 5 gives {max_val} years.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_table_two_way_contingency_joint_frequency(r: random.Random) -> Dict[str, Any]:
    # Grade 10 Boys vs Girls choosing Math Lit vs Core Maths
    boys_lit = r.randint(25, 45)
    boys_core = r.randint(20, 40)
    girls_lit = r.randint(30, 50)
    girls_core = r.randint(18, 35)

    tot_boys = boys_lit + boys_core
    tot_girls = girls_lit + girls_core
    tot_lit = boys_lit + girls_lit
    tot_core = boys_core + girls_core
    grand_total = tot_boys + tot_girls

    prompt = (
        f"A two-way contingency table shows subject choices for Grade 10 learners at a high school:\n\n"
        f"| Gender | Mathematical Literacy | Mathematics (Core) | Total |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Boys | {boys_lit} | {boys_core} | {tot_boys} |\n"
        f"| Girls | {girls_lit} | {girls_core} | {tot_girls} |\n"
        f"| **Total** | **{tot_lit}** | **{tot_core}** | **{grand_total}** |\n\n"
        f"1. How many girls chose Mathematical Literacy?\n"
        f"2. What percentage of the grand total of learners are boys taking Mathematics (Core)? (Round to 1 decimal place)."
    )
    pct_boys_core = round((boys_core / grand_total) * 100, 1)
    ans = f"{girls_lit} girls; {_fmt(pct_boys_core)}% of total learners"

    s1 = f"Read the intersection cell of 'Girls' and 'Mathematical Literacy' ({girls_lit}). Divide boys taking Core Maths ({boys_core}) by grand total ({grand_total}) and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Reading cell intersection and percentage calculation]\nIntersection = {girls_lit} girls.\nPercentage = ({boys_core} ÷ {grand_total}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Reading frequency and percentage]\nAnswer: {ans}."

    return _build_question_payload(
        "data_table_two_way_contingency_joint_frequency",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find where the 'Girls' row meets the 'Mathematical Literacy' column.",
        tier_2_hint=f"Boys taking Core Maths = {boys_core}. Divide by grand total {grand_total} and multiply by 100.",
        tier_3_hint=f"{ans}.",
    )


def _gen_data_table_missing_frequency_reconstruction(r: random.Random) -> Dict[str, Any]:
    f1, f2, f4, f5 = r.randint(10, 20), r.randint(12, 22), r.randint(15, 25), r.randint(8, 18)
    missing_f3 = r.randint(14, 30)
    grand_total = f1 + f2 + missing_f3 + f4 + f5
    known_sum = f1 + f2 + f4 + f5

    prompt = (
        f"In a survey of {grand_total} high school learners about their preferred beverage, one frequency value "
        f"was accidentally smudged and replaced with the letter **x**:\n\n"
        f"| Beverage | Frequency |\n"
        f"| :--- | :---: |\n"
        f"| Fruit Juice | {f1} |\n"
        f"| Milk | {f2} |\n"
        f"| Bottled Water | x |\n"
        f"| Soft Drink | {f4} |\n"
        f"| Tea / Coffee | {f5} |\n"
        f"| **Total** | **{grand_total}** |\n\n"
        f"Determine the missing frequency value, **x**."
    )
    ans = f"x = {missing_f3}"

    s1 = f"Sum all known frequencies ({f1} + {f2} + {f4} + {f5} = {known_sum}) and subtract from the grand total ({grand_total})."
    s2 = f"✓ [1 Mark: Method – Algebraic frequency subtraction from total]\nKnown sum = {f1} + {f2} + {f4} + {f5} = {known_sum}.\nx = {grand_total} − {known_sum}."
    s3 = f"✓ [1 Mark: Accuracy – Value of missing frequency x]\nx = {missing_f3}."

    return _build_question_payload(
        "data_table_missing_frequency_reconstruction",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add up all the known numbers: {f1} + {f2} + {f4} + {f5} = {known_sum}.",
        tier_2_hint=f"Subtract this sum from the total of {grand_total}.",
        tier_3_hint=f"{grand_total} − {known_sum} = {missing_f3}.",
    )


def _gen_data_table_cumulative_frequency_calculation(r: random.Random) -> Dict[str, Any]:
    f1, f2, f3, f4 = r.randint(5, 12), r.randint(8, 16), r.randint(12, 20), r.randint(6, 14)
    c1 = f1
    c2 = c1 + f2
    c3 = c2 + f3
    c4 = c3 + f4

    prompt = (
        f"A clinic records daily patient arrival counts grouped into four time intervals:\n\n"
        f"| Time Slot | Frequency (Patients) | Cumulative Frequency |\n"
        f"| :---: | :---: | :---: |\n"
        f"| 08:00 – 10:00 | {f1} | {c1} |\n"
        f"| 10:00 – 12:00 | {f2} | {c2} |\n"
        f"| 12:00 – 14:00 | {f3} | **A** |\n"
        f"| 14:00 – 16:00 | {f4} | **B** |\n\n"
        f"Calculate the values of **A** and **B** in the cumulative frequency column."
    )
    ans = f"A = {c3}; B = {c4}"

    s1 = f"Calculate running cumulative totals: A = Previous cumulative ({c2}) + Interval frequency ({f3}) = {c3}; B = A ({c3}) + Next frequency ({f4}) = {c4}."
    s2 = f"✓ [1 Mark: Method – Progressive cumulative frequency addition]\nA = {c2} + {f3} = {c3}.\nB = {c3} + {f4} = {c4}."
    s3 = f"✓ [1 Mark: Accuracy – Values of A and B]\nA = {c3}, B = {c4}."

    return _build_question_payload(
        "data_table_cumulative_frequency_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Cumulative frequency is a running total. Add each frequency to the previous cumulative total.",
        tier_2_hint=f"A = {c2} + {f3} = {c3}. B = {c3} + {f4} = {c4}.",
        tier_3_hint=f"A = {c3}; B = {c4}.",
    )
