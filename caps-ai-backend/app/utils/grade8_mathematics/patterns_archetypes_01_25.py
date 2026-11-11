"""
Grade 8 Mathematics - Numeric and Geometric Patterns Archetypes 01 to 25.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/04. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def arch_01_arithmetic_sequence_next_three_terms_positive_diff(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(3, 15)
    diff = rng.randint(3, 9)
    terms = [start + i * diff for i in range(5)]
    next_3 = [start + (5 + i) * diff for i in range(3)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_3)

    return {
        "title": "Extending Arithmetic Sequence (Positive Difference)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "01_arithmetic_sequence_next_three_terms_positive_diff",
        "difficulty": "easy",
        "question_text": (
            f"Consider the arithmetic number sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the constant difference and write down the next three terms of the sequence separated by semicolons."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify constant difference d = +{diff} (1 mark)",
            f"Calculate the 6th, 7th, and 8th terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Find the difference between consecutive terms: ${terms[1]} - {terms[0]} = {diff}$.",
            f"Add {diff} to the last given term ({terms[-1]}) to get the next term.",
            f"Repeat adding {diff}: {terms[-1]} + {diff} = {next_3[0]}, then {next_3[1]}, and {next_3[2]}.",
        ],
        "misconception_tags": ["incorrect_common_difference", "arithmetic_addition_error"],
        "diagram_spec": None,
    }


def arch_02_arithmetic_sequence_next_three_terms_negative_diff(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(80, 150)
    diff = rng.randint(4, 12)
    terms = [start - i * diff for i in range(4)]
    next_3 = [start - (4 + i) * diff for i in range(3)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_3)

    return {
        "title": "Extending Arithmetic Sequence (Negative Difference)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "02_arithmetic_sequence_next_three_terms_negative_diff",
        "difficulty": "medium",
        "question_text": (
            f"Consider the descending number sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the constant difference and find the next three terms of the sequence."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify constant difference d = -{diff} (1 mark)",
            f"Calculate next three terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Notice that the terms are decreasing: ${terms[1]} - {terms[0]} = -{diff}$.",
            f"Subtract {diff} from the last term ({terms[-1]}).",
            f"Continue subtracting {diff} consecutively to find the 3 terms.",
        ],
        "misconception_tags": ["sign_error_descending_sequence", "subtraction_slip"],
        "diagram_spec": None,
    }


def arch_03_arithmetic_sequence_decimal_terms(rng: random.Random) -> Dict[str, Any]:
    start = rng.choice([0.2, 0.3, 0.5, 1.1, 2.4])
    step = rng.choice([0.2, 0.3, 0.4, 0.5])
    terms = [round(start + i * step, 1) for i in range(4)]
    next_3 = [round(start + (4 + i) * step, 1) for i in range(3)]
    seq_str = "; ".join(str(t).replace(".", ",") for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t).replace(".", ",") for t in next_3)

    return {
        "title": "Decimal Arithmetic Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "03_arithmetic_sequence_decimal_terms",
        "difficulty": "medium",
        "question_text": (
            f"Determine the rule and the next three terms for the decimal number sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Write the next three terms separated by semicolons using comma decimal notation."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify constant difference d = +{str(step).replace('.', ',')} (1 mark)",
            f"Compute next three decimal terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Subtract consecutive terms: ${terms[1]} - {terms[0]} = {step}$.",
            f"Add {step} to {terms[-1]}.",
            f"Keep the decimal step constant: next terms are {ans_str}.",
        ],
        "misconception_tags": ["decimal_addition_place_value_error"],
        "diagram_spec": None,
    }


def arch_04_arithmetic_sequence_fractional_terms(rng: random.Random) -> Dict[str, Any]:
    den = rng.choice([3, 4, 5, 6, 8])
    step_num = rng.choice([1, 2])
    start_num = rng.choice([1, 2, 3])
    terms = [f"\\frac{{{start_num + i * step_num}}}{{{den}}}" for i in range(4)]
    next_3 = [f"\\frac{{{start_num + (4 + i) * step_num}}}{{{den}}}" for i in range(3)]
    seq_str = "; ".join(terms) + "; \\dots"
    ans_str = "; ".join(next_3)

    return {
        "title": "Fractional Arithmetic Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "04_arithmetic_sequence_fractional_terms",
        "difficulty": "medium",
        "question_text": (
            f"Consider the fraction sequence with common denominator ${den}$:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the next three terms as fractions."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify numerator difference d = +{step_num} (1 mark)",
            f"State next three terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"The denominator remains {den}.",
            f"The numerators increase by {step_num} each step.",
            f"Add {step_num} to the numerator of the last term.",
        ],
        "misconception_tags": ["fraction_addition_denominator_error"],
        "diagram_spec": None,
    }


def arch_05_arithmetic_sequence_missing_intermediate_term(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(4, 20)
    diff = rng.randint(3, 8)
    t1 = start
    t2 = start + diff
    t3 = start + 2 * diff
    t4 = start + 3 * diff
    t5 = start + 4 * diff

    return {
        "title": "Finding Missing Intermediate Term",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "05_arithmetic_sequence_missing_intermediate_term",
        "difficulty": "medium",
        "question_text": (
            f"Find the value of the missing term $x$ in the arithmetic sequence:\n\n"
            f"$${t1};\\ {t2};\\ x;\\ {t4};\\ {t5}$$\n\n"
            f"State the value of $x$."
        ),
        "correct_answer": str(t3),
        "marking_schema": [
            f"Calculate common difference d = {t2} - {t1} = {diff} (1 mark)",
            f"Calculate x = {t2} + {diff} = {t3} (or {t4} - {diff} = {t3}) (1 mark)",
        ],
        "hints": [
            f"Find the common difference from the first two terms: ${t2} - {t1} = {diff}$.",
            f"Add this difference to {t2}: $x = {t2} + {diff}$.",
            f"Verify: ${t3} + {diff} = {t4}$, which matches the 4th term.",
        ],
        "misconception_tags": ["missing_term_averaging_error", "incorrect_difference_jump"],
        "diagram_spec": None,
    }


def arch_06_arithmetic_sequence_missing_multiple_terms(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(5, 25)
    diff = rng.randint(4, 9)
    t1 = start
    t2 = start + diff
    t3 = start + 2 * diff
    t4 = start + 3 * diff
    t5 = start + 4 * diff

    return {
        "title": "Finding Two Missing Terms in Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "06_arithmetic_sequence_missing_multiple_terms",
        "difficulty": "medium",
        "question_text": (
            f"In the linear number sequence below, two terms are missing:\n\n"
            f"$${t1};\\ a;\\ {t3};\\ b;\\ {t5}$$\n\n"
            f"Determine the values of $a$ and $b$. Express your answer in the form $a = \\dots;\\ b = \\dots$."
        ),
        "correct_answer": f"a = {t2}; b = {t4}",
        "marking_schema": [
            f"Determine step size: 2 steps from {t1} to {t3} => 2d = {t3 - t1} => d = {diff} (2 marks)",
            f"Deduce a = {t2} and b = {t4} (2 marks)",
        ],
        "hints": [
            f"Between the 1st term ({t1}) and 3rd term ({t3}) are 2 equal steps.",
            f"Step size $d = \\frac{{{t3} - {t1}}}{{2}} = {diff}$.",
            f"Then $a = {t1} + {diff} = {t2}$ and $b = {t3} + {diff} = {t4}$.",
        ],
        "misconception_tags": ["multi_step_difference_division_error"],
        "diagram_spec": None,
    }


def arch_07_geometric_sequence_doubling_tripling_next_terms(rng: random.Random) -> Dict[str, Any]:
    ratio = rng.choice([2, 3, 4])
    start = rng.choice([2, 3, 5])
    terms = [start * (ratio ** i) for i in range(4)]
    next_2 = [start * (ratio ** (4 + i)) for i in range(2)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_2)

    return {
        "title": "Extending Geometric Sequence (Constant Ratio)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "07_geometric_sequence_doubling_tripling_next_terms",
        "difficulty": "easy",
        "question_text": (
            f"Consider the sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Identify the constant ratio and write down the next two terms separated by a semicolon."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify constant ratio r = {terms[1]} / {terms[0]} = {ratio} (1 mark)",
            f"Calculate 5th and 6th terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Check the ratio: $\\frac{{{terms[1]}}}{{{terms[0]}}} = {ratio}$.",
            f"Multiply each term by {ratio} to get the next term.",
            f"5th term = ${terms[-1]} \\times {ratio} = {next_2[0]}$, 6th term = ${next_2[0]} \\times {ratio} = {next_2[1]}$.",
        ],
        "misconception_tags": ["confusing_ratio_with_difference"],
        "diagram_spec": None,
    }


def arch_08_geometric_sequence_fractional_ratio_decay(rng: random.Random) -> Dict[str, Any]:
    div = rng.choice([2, 3, 5])
    start = (div ** 4) * rng.choice([1, 2])
    terms = [start // (div ** i) for i in range(4)]
    next_2 = [terms[-1] // div, (terms[-1] // div) // div]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_2)

    return {
        "title": "Decaying Geometric Sequence (Division Ratio)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "08_geometric_sequence_fractional_ratio_decay",
        "difficulty": "medium",
        "question_text": (
            f"Consider the sequence formed by repeatedly dividing:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the constant multiplier/divisor and find the next two terms."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Identify divisor of {div} (or ratio 1/{div}) (1 mark)",
            f"Compute next two terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"Divide consecutive terms: ${terms[0]} \\div {terms[1]} = {div}$.",
            f"Each term is divided by {div} to obtain the next term.",
            f"${terms[-1]} \\div {div} = {next_2[0]}$, and ${next_2[0]} \\div {div} = {next_2[1]}$.",
        ],
        "misconception_tags": ["geometric_decay_division_error"],
        "diagram_spec": None,
    }


def arch_09_geometric_sequence_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    start = rng.choice([7, 12, 35])
    terms = [start * (10 ** i) for i in range(4)]
    next_term = start * (10 ** 4)
    seq_str = "; ".join(f"{t:,}".replace(",", " ") for t in terms) + "; \\dots"
    ans_str = f"{next_term:,}".replace(",", " ")

    return {
        "title": "Geometric Sequence (Powers of 10)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "09_geometric_sequence_powers_of_ten",
        "difficulty": "easy",
        "question_text": (
            f"Observe the sequence with a constant ratio:\n\n"
            f"$${seq_str}$$\n\n"
            f"State the constant ratio and determine the 5th term."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            "Identify ratio r = 10 (1 mark)",
            f"Determine 5th term = {ans_str} (1 mark)",
        ],
        "hints": [
            "Notice each term is multiplied by 10 (one zero is added).",
            f"Multiply the 4th term ({terms[-1]}) by 10.",
            f"The 5th term is {ans_str}.",
        ],
        "misconception_tags": ["place_value_zero_count_error"],
        "diagram_spec": None,
    }


def arch_10_sequence_classification_constant_diff_vs_ratio(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["arithmetic", "geometric"])
    if choice == "arithmetic":
        d = rng.randint(4, 8)
        s = rng.randint(2, 10)
        terms = [s + i * d for i in range(4)]
        ans = "arithmetic"
        rule = f"constant difference of +{d}"
    else:
        r = rng.choice([2, 3])
        s = rng.choice([2, 3, 5])
        terms = [s * (r ** i) for i in range(4)]
        ans = "geometric"
        rule = f"constant ratio of {r}"

    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"

    return {
        "title": "Classifying Sequence Type (Arithmetic vs Geometric)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "10_sequence_classification_constant_diff_vs_ratio",
        "difficulty": "medium",
        "question_text": (
            f"Classify the following sequence as either **arithmetic** (constant difference) or **geometric** (constant ratio):\n\n"
            f"$${seq_str}$$\n\n"
            f"Provide your answer as either 'arithmetic' or 'geometric'."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Examine differences vs ratios between terms (1 mark)",
            f"Correctly classify as {ans} with {rule} (1 mark)",
        ],
        "hints": [
            f"Test if the differences between consecutive terms are equal.",
            f"Test if the ratios $\\frac{{T_2}}{{T_1}}$ and $\\frac{{T_3}}{{T_2}}$ are equal.",
            f"Since the pattern has a {rule}, it is {ans}.",
        ],
        "misconception_tags": ["pattern_type_confusion"],
        "diagram_spec": None,
    }


def arch_11_triangular_numbers_sequence_extension(rng: random.Random) -> Dict[str, Any]:
    # Triangular numbers: 1, 3, 6, 10, 15, 21, 28, 36...
    tri = [1, 3, 6, 10, 15, 21, 28, 36]
    start_idx = 0
    given = tri[start_idx:start_idx + 4]
    next_2 = tri[start_idx + 4:start_idx + 6]
    seq_str = "; ".join(str(t) for t in given) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_2)

    return {
        "title": "Triangular Numbers Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "11_triangular_numbers_sequence_extension",
        "difficulty": "medium",
        "question_text": (
            f"Consider the sequence of triangular numbers:\n\n"
            f"$${seq_str}$$\n\n"
            f"Analyze the pattern in differences and determine the next two terms separated by a semicolon."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            "Identify increasing difference (+2, +3, +4, +5, +6...) (1 mark)",
            f"Compute 5th and 6th terms: {ans_str} (2 marks)",
        ],
        "hints": [
            "Find the differences between consecutive terms: 3 - 1 = 2, 6 - 3 = 3, 10 - 6 = 4.",
            "The difference increases by 1 each time (+2, +3, +4, +5, +6).",
            f"Next term is 10 + 5 = {next_2[0]}, and after that is {next_2[0]} + 6 = {next_2[1]}.",
        ],
        "misconception_tags": ["second_order_pattern_unrecognized"],
        "diagram_spec": None,
    }


def arch_12_square_numbers_sequence_extension(rng: random.Random) -> Dict[str, Any]:
    # Square numbers: 1, 4, 9, 16, 25, 36, 49, 64
    squares = [i ** 2 for i in range(1, 9)]
    shift = rng.choice([0, 1, -1])
    terms = [s + shift for s in squares[:5]]
    next_2 = [s + shift for s in squares[5:7]]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_2)

    return {
        "title": "Square Numbers Pattern Extension",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "12_square_numbers_sequence_extension",
        "difficulty": "medium",
        "question_text": (
            f"Consider the sequence formed by powers/squares:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the rule and write down the 6th and 7th terms separated by a semicolon."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Recognize relation to perfect squares n^2 {'+ ' + str(shift) if shift > 0 else '- 1' if shift < 0 else ''} (1 mark)",
            f"Calculate 6th and 7th terms: {ans_str} (2 marks)",
        ],
        "hints": [
            "Compare each term to perfect squares: $1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25$.",
            f"Each term is $n^2 {'+ ' + str(shift) if shift > 0 else '- 1' if shift < 0 else ''}$.",
            f"For n = 6: $6^2 {'+ ' + str(shift) if shift > 0 else '- 1' if shift < 0 else ''} = {next_2[0]}$. For n = 7: $7^2 {'+ ' + str(shift) if shift > 0 else '- 1' if shift < 0 else ''} = {next_2[1]}$.",
        ],
        "misconception_tags": ["square_pattern_shift_neglect"],
        "diagram_spec": None,
    }


def arch_13_cubic_numbers_sequence_extension(rng: random.Random) -> Dict[str, Any]:
    shift = rng.choice([0, 1])
    cubes = [i ** 3 + shift for i in range(1, 6)]
    next_term = (6 ** 3) + shift
    seq_str = "; ".join(str(t) for t in cubes[:4]) + "; \\dots"

    return {
        "title": "Cubic Numbers Sequence Extension",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "13_cubic_numbers_sequence_extension",
        "difficulty": "hard",
        "question_text": (
            f"Study the sequence of cubic numbers:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the general relationship and calculate the 5th term of the sequence."
        ),
        "correct_answer": str(cubes[4]),
        "marking_schema": [
            f"Identify cubic relationship T_n = n^3 {'+ 1' if shift == 1 else ''} (1 mark)",
            f"Calculate 5th term = 5^3 {'+ 1' if shift == 1 else ''} = {cubes[4]} (2 marks)",
        ],
        "hints": [
            "Evaluate $1^3 = 1, 2^3 = 8, 3^3 = 27, 4^3 = 64$.",
            f"Notice each term is $n^3 {'+ 1' if shift == 1 else ''}$.",
            f"The 5th term is $5^3 {'+ 1' if shift == 1 else ''} = 125 {'+ 1' if shift == 1 else ''} = {cubes[4]}$.",
        ],
        "misconception_tags": ["cubic_power_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_14_second_difference_quadratic_pattern_identification(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.randint(1, 3)
    c = rng.randint(1, 5)
    terms = [a * (n ** 2) + b * n + c for n in range(1, 6)]
    d1 = [terms[i+1] - terms[i] for i in range(4)]
    d2 = d1[1] - d1[0]
    seq_str = "; ".join(str(t) for t in terms[:4]) + "; \\dots"

    return {
        "title": "Constant Second Difference in Quadratic Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "14_second_difference_quadratic_pattern_identification",
        "difficulty": "hard",
        "question_text": (
            f"Calculate the first and second differences for the sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"State the value of the constant second difference ($d_2$)."
        ),
        "correct_answer": str(d2),
        "marking_schema": [
            f"Calculate first differences: {d1[0]}, {d1[1]}, {d1[2]} (1 mark)",
            f"Calculate constant second difference: {d2} (1 mark)",
        ],
        "hints": [
            f"Find the first differences by subtracting adjacent terms: ${terms[1]} - {terms[0]} = {d1[0]}$, ${terms[2]} - {terms[1]} = {d1[1]}$, etc.",
            f"Now subtract the first differences from each other: ${d1[1]} - {d1[0]} = {d2}$.",
            f"The constant second difference is {d2}.",
        ],
        "misconception_tags": ["first_vs_second_difference_confusion"],
        "diagram_spec": None,
    }


def arch_15_fibonacci_type_additive_sequence(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(1, 3)
    b = rng.randint(2, 5)
    terms = [a, b]
    for _ in range(4):
        terms.append(terms[-1] + terms[-2])
    given = terms[:4]
    next_2 = terms[4:6]
    seq_str = "; ".join(str(t) for t in given) + "; \\dots"
    ans_str = "; ".join(str(t) for t in next_2)

    return {
        "title": "Fibonacci-Type Additive Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "15_fibonacci_type_additive_sequence",
        "difficulty": "medium",
        "question_text": (
            f"In the sequence below, each term after the first two is found by adding the previous two terms:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the 5th and 6th terms of the sequence separated by a semicolon."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Apply rule T_n = T_{{n-1}} + T_{{n-2}} (1 mark)",
            f"Calculate 5th term = {terms[2]} + {terms[3]} = {next_2[0]} (1 mark)",
            f"Calculate 6th term = {terms[3]} + {next_2[0]} = {next_2[1]} (1 mark)",
        ],
        "hints": [
            f"Verify the rule: ${given[0]} + {given[1]} = {given[2]}$ and ${given[1]} + {given[2]} = {given[3]}$.",
            f"Add the 3rd and 4th terms to get the 5th term: ${given[2]} + {given[3]} = {next_2[0]}$.",
            f"Add the 4th and 5th terms to get the 6th term: ${given[3]} + {next_2[0]} = {next_2[1]}$.",
        ],
        "misconception_tags": ["recursive_addition_slip"],
        "diagram_spec": None,
    }


def arch_16_verbal_rule_to_numeric_sequence_generation(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(3, 7)
    c = rng.randint(2, 8)
    terms = [m * n + c for n in range(1, 5)]
    ans_str = "; ".join(str(t) for t in terms)

    return {
        "title": "Generating Sequence from Verbal Rule",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "16_verbal_rule_to_numeric_sequence_generation",
        "difficulty": "easy",
        "question_text": (
            f"A sequence is described by the verbal rule:\n\n"
            f"*\"Multiply the term position ($n$) by ${m}$ and then add ${c}$.\"*\n\n"
            f"Write down the first four terms of this sequence separated by semicolons."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Substitute n = 1, 2, 3, 4 into T_n = {m}n + {c} (2 marks)",
            f"List correct terms: {ans_str} (2 marks)",
        ],
        "hints": [
            f"For term 1 ($n=1$): ${m}(1) + {c} = {terms[0]}$.",
            f"For term 2 ($n=2$): ${m}(2) + {c} = {terms[1]}$.",
            f"Repeat for $n=3$ and $n=4$: {ans_str}.",
        ],
        "misconception_tags": ["verbal_rule_bodmas_error"],
        "diagram_spec": None,
    }


def arch_17_flow_diagram_input_to_output_calculation(rng: random.Random) -> Dict[str, Any]:
    mult = rng.randint(3, 6)
    add = rng.randint(2, 7)
    inputs = [1, 2, 3, 5, 10]
    outputs = [mult * x + add for x in inputs]
    target_in = inputs[3]
    target_out = outputs[3]

    return {
        "title": "Flow Diagram (Input to Output)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "17_flow_diagram_input_to_output_calculation",
        "difficulty": "easy",
        "question_text": (
            f"A flow diagram has the operational rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {mult}}} \\longrightarrow \\boxed{{+ {add}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"Calculate the output $y$ when the input is $x = {target_in}$."
        ),
        "correct_answer": str(target_out),
        "marking_schema": [
            f"Multiply input: {target_in} * {mult} = {target_in * mult} (1 mark)",
            f"Add constant: {target_in * mult} + {add} = {target_out} (1 mark)",
        ],
        "hints": [
            f"First follow the first box: multiply {target_in} by {mult}.",
            f"${target_in} \\times {mult} = {target_in * mult}$.",
            f"Then follow the second box: add {add}: ${target_in * mult} + {add} = {target_out}$.",
        ],
        "misconception_tags": ["flow_diagram_order_of_operations_reversal"],
        "diagram_spec": None,
    }


def arch_18_flow_diagram_output_to_input_inverse_operation(rng: random.Random) -> Dict[str, Any]:
    mult = rng.randint(3, 6)
    add = rng.randint(2, 7)
    target_in = rng.randint(4, 9)
    target_out = mult * target_in + add

    return {
        "title": "Flow Diagram (Inverse Operations / Output to Input)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "18_flow_diagram_output_to_input_inverse_operation",
        "difficulty": "medium",
        "question_text": (
            f"A flow diagram follows the rule:\n\n"
            f"$$\\text{{Input }} x \\longrightarrow \\boxed{{\\times {mult}}} \\longrightarrow \\boxed{{+ {add}}} \\longrightarrow \\text{{Output }} y$$\n\n"
            f"If the output is $y = {target_out}$, calculate the corresponding input $x$ using inverse operations."
        ),
        "correct_answer": str(target_in),
        "marking_schema": [
            f"Apply inverse operations in reverse order: (y - {add}) / {mult} (1 mark)",
            f"Calculate x = ({target_out} - {add}) / {mult} = {target_in} (1 mark)",
        ],
        "hints": [
            f"Work backwards from output {target_out}.",
            f"The inverse of adding {add} is subtracting {add}: ${target_out} - {add} = {target_out - add}$.",
            f"The inverse of multiplying by {mult} is dividing by {mult}: ${target_out - add} \\div {mult} = {target_in}$.",
        ],
        "misconception_tags": ["inverse_operations_order_error"],
        "diagram_spec": None,
    }


def arch_19_flow_diagram_determining_missing_operator_rule(rng: random.Random) -> Dict[str, Any]:
    mult = rng.randint(2, 6)
    sub = rng.randint(1, 4)
    # y = mult * x - sub
    in1, out1 = 1, mult * 1 - sub
    in2, out2 = 2, mult * 2 - sub
    in3, out3 = 3, mult * 3 - sub

    return {
        "title": "Flow Diagram (Finding Missing Operators)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "19_flow_diagram_determining_missing_operator_rule",
        "difficulty": "hard",
        "question_text": (
            f"Consider the input-output pairs from a two-stage flow diagram:\n\n"
            f"* Input $1 \\rightarrow$ Output ${out1}$\n"
            f"* Input $2 \\rightarrow$ Output ${out2}$\n"
            f"* Input $3 \\rightarrow$ Output ${out3}$\n\n"
            f"The rule has the form $\\boxed{{\\times m}} \\longrightarrow \\boxed{{- c}}$.\n"
            f"Determine the values of $m$ and $c$. Write your answer as $m = \\dots;\\ c = \\dots$."
        ),
        "correct_answer": f"m = {mult}; c = {sub}",
        "marking_schema": [
            f"Determine multiplier m from rate of change: {out2} - {out1} = {mult} (1 mark)",
            f"Solve for constant c: {mult}(1) - c = {out1} => c = {sub} (1 mark)",
        ],
        "hints": [
            f"The outputs increase by ${out2} - {out1} = {mult}$ for each step in input, so $m = {mult}$.",
            f"Substitute input 1 into $y = {mult}(1) - c = {out1}$.",
            f"${mult} - c = {out1} \\implies c = {sub}$.",
        ],
        "misconception_tags": ["two_step_rule_deduction_error"],
        "diagram_spec": None,
    }


def arch_20_table_of_values_linear_constant_difference_rule(rng: random.Random) -> Dict[str, Any]:
    diff = rng.randint(3, 7)
    c = rng.randint(1, 8)
    # y = diff * x + c
    x_vals = [1, 2, 3, 4, 10]
    y_vals = [diff * x + c for x in x_vals]

    return {
        "title": "Table of Values (Completing Missing Table Cell)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "20_table_of_values_linear_constant_difference_rule",
        "difficulty": "medium",
        "question_text": (
            f"Consider the table showing the relationship between position ($n$) and term value ($T_n$):\n\n"
            f"| $n$ | 1 | 2 | 3 | 4 | 10 |\n"
            f"| :--- | :---: | :---: | :---: | :---: | :---: |\n"
            f"| $T_n$ | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} | $k$ |\n\n"
            f"Determine the rule for $T_n$ in terms of $n$ and calculate the value of $k$."
        ),
        "correct_answer": str(y_vals[4]),
        "marking_schema": [
            f"Find constant difference d = {diff} (1 mark)",
            f"Formulate rule T_n = {diff}n + {c} (1 mark)",
            f"Calculate k = {diff}(10) + {c} = {y_vals[4]} (1 mark)",
        ],
        "hints": [
            f"Calculate the common difference: ${y_vals[1]} - {y_vals[0]} = {diff}$.",
            f"Rule: $T_n = {diff}n + ({y_vals[0]} - {diff}) = {diff}n + {c}$.",
            f"For $n = 10$: $k = {diff}(10) + {c} = {y_vals[4]}$.",
        ],
        "misconception_tags": ["table_missing_value_extrapolation_error"],
        "diagram_spec": None,
    }


def arch_21_general_term_formula_derivation_linear_simple(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([4, 6, 7, 8, 9])
    terms = [m * n for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"

    return {
        "title": "General Term Formula (Direct Multiples)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "21_general_term_formula_derivation_linear_simple",
        "difficulty": "easy",
        "question_text": (
            f"Write down the general term ($T_n$) for the sequence of multiples:\n\n"
            f"$${seq_str}$$\n\n"
            f"Express your answer in the form $T_n = \\dots$."
        ),
        "correct_answer": f"T_n = {m}n",
        "marking_schema": [
            f"Identify common difference d = {m} (1 mark)",
            f"Formulate general rule T_n = {m}n (1 mark)",
        ],
        "hints": [
            f"Find the constant difference: ${terms[1]} - {terms[0]} = {m}$.",
            f"Notice each term is simply {m} multiplied by its position $n$.",
            f"$T_n = {m}n$.",
        ],
        "misconception_tags": ["formula_notation_error"],
        "diagram_spec": None,
    }


def arch_22_general_term_formula_derivation_linear_with_constant(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(3, 8)
    c = rng.randint(1, 9)
    terms = [d * n + c for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    sign_c = f"+ {c}"

    return {
        "title": "General Term Formula (Linear dn + c)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "22_general_term_formula_derivation_linear_with_constant",
        "difficulty": "medium",
        "question_text": (
            f"Determine the general term formula ($T_n$) for the arithmetic sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"State the formula in the form $T_n = dn + c$."
        ),
        "correct_answer": f"T_n = {d}n + {c}",
        "marking_schema": [
            f"Identify constant difference d = {d} (1 mark)",
            f"Calculate constant c = T_1 - d = {terms[0]} - {d} = {c} (1 mark)",
            f"State general term T_n = {d}n + {c} (1 mark)",
        ],
        "hints": [
            f"Find the difference $d = {terms[1]} - {terms[0]} = {d}$.",
            f"Write $T_n = {d}n + c$.",
            f"Substitute $n=1$: $T_1 = {d}(1) + c = {terms[0]} \\implies c = {c}$. Thus $T_n = {d}n + {c}$.",
        ],
        "misconception_tags": ["general_term_constant_c_calculation_error"],
        "diagram_spec": None,
    }


def arch_23_general_term_formula_negative_common_difference(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(3, 7)
    c = rng.randint(40, 90)
    terms = [-d * n + c for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"

    return {
        "title": "General Term Formula (Negative Common Difference)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "23_general_term_formula_negative_common_difference",
        "difficulty": "hard",
        "question_text": (
            f"Find the general term ($T_n$) for the decreasing sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Write the rule in terms of $n$."
        ),
        "correct_answer": f"T_n = -{d}n + {c}",
        "marking_schema": [
            f"Identify common difference d = -{d} (1 mark)",
            f"Calculate constant c = T_1 - (-{d}) = {terms[0]} + {d} = {c} (1 mark)",
            f"State T_n = -{d}n + {c} (1 mark)",
        ],
        "hints": [
            f"The sequence decreases by {d} each time, so $d = -{d}$.",
            f"Set up $T_n = -{d}n + c$.",
            f"Use $T_1 = {terms[0]}$: $-{d}(1) + c = {terms[0]} \\implies c = {c}$.",
        ],
        "misconception_tags": ["negative_gradient_common_difference_error"],
        "diagram_spec": None,
    }


def arch_24_calculate_far_term_value_using_linear_rule_t20_t50(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(4, 9)
    c = rng.randint(2, 7)
    terms = [d * n + c for n in range(1, 5)]
    far_n = rng.choice([20, 25, 50, 100])
    target_val = d * far_n + c
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"

    return {
        "title": "Calculating a Far Term (T_20 / T_50)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "24_calculate_far_term_value_using_linear_rule_t20_t50",
        "difficulty": "medium",
        "question_text": (
            f"Consider the sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine the general term formula $T_n$, and use it to calculate the value of the **{far_n}th term** ($T_{{{far_n}}}$)."
        ),
        "correct_answer": str(target_val),
        "marking_schema": [
            f"Determine T_n = {d}n + {c} (2 marks)",
            f"Substitute n = {far_n}: T_{{{far_n}}} = {d}({far_n}) + {c} = {target_val} (2 marks)",
        ],
        "hints": [
            f"Find the constant difference: $d = {d}$.",
            f"Formulate $T_n = {d}n + {c}$.",
            f"Replace $n$ with {far_n}: $T_{{{far_n}}} = {d}({far_n}) + {c} = {target_val}$.",
        ],
        "misconception_tags": ["recursive_instead_of_general_rule_application"],
        "diagram_spec": None,
    }


def arch_25_calculate_position_n_given_term_value(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(3, 8)
    c = rng.randint(1, 9)
    n_pos = rng.randint(15, 35)
    term_val = d * n_pos + c
    terms = [d * n + c for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"

    return {
        "title": "Finding Term Position n from Value",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "25_calculate_position_n_given_term_value",
        "difficulty": "hard",
        "question_text": (
            f"An arithmetic sequence begins as follows:\n\n"
            f"$${seq_str}$$\n\n"
            f"Which term in this sequence has a value of ${term_val}$? (Find the position $n$ such that $T_n = {term_val}$)."
        ),
        "correct_answer": str(n_pos),
        "marking_schema": [
            f"Write equation T_n = {d}n + {c} = {term_val} (1 mark)",
            f"Solve for n: {d}n = {term_val - c} => n = {n_pos} (2 marks)",
        ],
        "hints": [
            f"The general rule is $T_n = {d}n + {c}$.",
            f"Set up the linear equation: ${d}n + {c} = {term_val}$.",
            f"Subtract {c}: ${d}n = {term_val - c}$, then divide by {d}: $n = {n_pos}$.",
        ],
        "misconception_tags": ["linear_equation_solving_error_in_sequence"],
        "diagram_spec": None,
    }
