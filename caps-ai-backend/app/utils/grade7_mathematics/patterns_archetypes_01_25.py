"""
Grade 7 Mathematics - Numeric and Geometric Patterns Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/03. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Arithmetic Sequences & Constant Difference (01 - 08)
# ==============================================================================

def arch_01_constant_difference_identification(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(3, 15)
    d = rng.choice([3, 4, 5, 6, 7, 8])
    seq = [start + i * d for i in range(5)]
    seq_s = "; ".join(str(x) for x in seq)

    prompt = (
        f"Study the ascending progression:\n\n"
        f"$${seq_s}; ...$$\n\n"
        f"1. Is there a **constant difference** between consecutive entries?\n"
        f"2. State the value of this common difference."
    )
    sol = (
        f"**Step 1:** Subtract consecutive terms: "
        f"${seq[1]} - {seq[0]} = {d}$ and ${seq[2]} - {seq[1]} = {d}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Yes, there is a constant difference of **+{d}** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Yes; +{d}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "01_constant_difference_identification",
        "hints": {
            "tier_1": "Subtract the first term from the second term.",
            "tier_2": f"{seq[1]} - {seq[0]} = {d}.",
            "tier_3": f"Yes; common difference is +{d}."
        }
    }


def arch_02_extend_increasing_arithmetic_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(2, 20)
    d = rng.choice([3, 4, 6, 7, 9])
    terms = [start + i * d for i in range(4)]
    next_3 = [start + i * d for i in range(4, 7)]
    terms_s = "; ".join(str(x) for x in terms)
    next_s = "; ".join(str(x) for x in next_3)

    prompt = (
        f"Extend the ascending progression by three additional entries:\n\n"
        f"$${terms_s}; ...$$"
    )
    sol = (
        f"**Step 1:** The rule is to add ${d}$ to each term [1 Mark: Method].\n\n"
        f"**Step 2:** Next three terms:\n"
        f"- ${terms[3]} + {d} = {next_3[0]}$\n"
        f"- ${next_3[0]} + {d} = {next_3[1]}$\n"
        f"- ${next_3[1]} + {d} = {next_3[2]}$ [1 Mark: Accuracy].\n\n"
        f"$$\\mathbf{{{next_s}}}$$"
    )
    return {
        "id": f"g7_pat_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": next_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_extend_increasing_arithmetic_sequence",
        "hints": {
            "tier_1": f"Find the difference (+{d}) and keep adding it.",
            "tier_2": f"Add {d} to {terms[3]}.",
            "tier_3": next_s
        }
    }


def arch_03_extend_decreasing_arithmetic_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(80, 120)
    d = rng.choice([4, 5, 6, 7, 8])
    terms = [start - i * d for i in range(4)]
    next_3 = [start - i * d for i in range(4, 7)]
    terms_s = "; ".join(str(x) for x in terms)
    next_s = "; ".join(str(x) for x in next_3)

    prompt = (
        f"Extend the decreasing progression by three additional entries:\n\n"
        f"$${terms_s}; ...$$"
    )
    sol = (
        f"**Step 1:** The rule is to subtract ${d}$ from each term (constant difference of $-{d}$) [1 Mark: Method].\n\n"
        f"**Step 2:** Next three terms:\n"
        f"- ${terms[3]} - {d} = {next_3[0]}$\n"
        f"- ${next_3[0]} - {d} = {next_3[1]}$\n"
        f"- ${next_3[1]} - {d} = {next_3[2]}$ [1 Mark: Accuracy].\n\n"
        f"$$\\mathbf{{{next_s}}}$$"
    )
    return {
        "id": f"g7_pat_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": next_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_extend_decreasing_arithmetic_sequence",
        "hints": {
            "tier_1": f"The numbers decrease by {d} each time.",
            "tier_2": f"Subtract {d} from {terms[3]}.",
            "tier_3": next_s
        }
    }


def arch_04_missing_term_inside_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(5, 25)
    d = rng.choice([3, 5, 7, 8])
    full = [start + i * d for i in range(5)]
    miss_idx = rng.choice([1, 2, 3])
    ans = full[miss_idx]
    display = [str(x) if i != miss_idx else "\\square" for i, x in enumerate(full)]
    disp_s = "; ".join(display)

    prompt = (
        f"Find the value of the missing term represented by $\\square$:\n\n"
        f"$${disp_s}; \\dots$$"
    )
    sol = (
        f"**Step 1:** Determine the constant difference from known adjacent terms: $d = {d}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Missing term: $${full[miss_idx - 1]} + {d} = \\mathbf{{{ans}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_missing_term_inside_sequence",
        "hints": {
            "tier_1": f"The step between consecutive terms is {d}.",
            "tier_2": f"Add {d} to {full[miss_idx - 1]}.",
            "tier_3": f"{ans}."
        }
    }


def arch_05_verbal_rule_arithmetic_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.randint(3, 12)
    d = rng.choice([4, 5, 6, 7])
    terms = [start + i * d for i in range(4)]
    terms_s = "; ".join(str(x) for x in terms)

    prompt = (
        f"Describe the pattern of this sequence in words:\n\n"
        f"$${terms_s}; \\dots$$"
    )
    sol = (
        f"**Step 1:** Identify the starting term: Starts at ${start}$ [1 Mark].\n\n"
        f"**Step 2:** Identify the operation: Add ${d}$ to the previous term to get the next term [1 Mark: Clear verbal formulation].\n\n"
        f"$$\\text{{\"Start at {start} and repeatedly add {d}\"}}$$"
    )
    return {
        "id": f"g7_pat_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Start at {start} and add {d} each time",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_verbal_rule_arithmetic_sequence",
        "hints": {
            "tier_1": "State the starting number and the rule for finding the next number.",
            "tier_2": f"Starts at {start}, add {d}.",
            "tier_3": f"Start at {start} and add {d} each time."
        }
    }


def arch_06_distinguish_constant_difference(rng: random.Random) -> Dict[str, Any]:
    is_arith = rng.choice([True, False])
    if is_arith:
        seq = [4, 9, 14, 19, 24]  # diff = +5
        ans = "Yes; constant difference of +5"
        diff_str = "Differences are 9 - 4 = 5, 14 - 9 = 5, 19 - 14 = 5 (constant)"
    else:
        seq = [2, 4, 8, 16, 32]  # geometric (r = 2)
        ans = "No; differences are 2, 4, 8, 16 (not constant)"
        diff_str = "Differences are 4 - 2 = 2, 8 - 4 = 4, 16 - 8 = 8 (not constant)"

    seq_s = "; ".join(str(x) for x in seq)

    prompt = (
        f"Does the following sequence have a **constant difference**?\n\n"
        f"$${seq_s}; \\dots$$\n\n"
        f"Justify your answer by calculating the differences between consecutive terms."
    )
    sol = (
        f"**Step 1:** Calculate differences: {diff_str} [1 Mark: Method].\n\n"
        f"**Step 2:** **{ans}** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_distinguish_constant_difference",
        "hints": {
            "tier_1": "Check if subtracting consecutive numbers always gives the same result.",
            "tier_2": diff_str,
            "tier_3": ans
        }
    }


def arch_07_input_output_table_linear(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5])
    c = rng.choice([1, 2, 3])
    # T_n = d*n + c
    t1 = d * 1 + c
    t2 = d * 2 + c
    t3 = d * 3 + c
    t5 = d * 5 + c

    prompt = (
        f"Complete the input-output table for the rule $T_n = {d}n + {c}$:\n\n"
        f"| Position ($n$) | 1 | 2 | 3 | 5 |\n"
        f"| :---: | :---: | :---: | :---: | :---: |\n"
        f"| Term Value ($T_n$) | {t1} | {t2} | {t3} | $\\mathbf{{?}}$ |\n\n"
        f"What is the value of the term at position $n = 5$?"
    )
    sol = (
        f"**Step 1:** Substitute $n = 5$ into the formula: $T_5 = {d}(5) + {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate: $${d * 5} + {c} = \\mathbf{{{t5}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{t5}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_input_output_table_linear",
        "hints": {
            "tier_1": f"Multiply 5 by {d} and add {c}.",
            "tier_2": f"{d} * 5 + {c} = {t5}.",
            "tier_3": f"{t5}."
        }
    }


def arch_08_flow_diagram_rule_evaluation(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([3, 4, 6])
    sub = rng.choice([1, 2, 3])
    inp = rng.choice([4, 7, 9])
    out = mult * inp - sub

    prompt = (
        f"A flow diagram processes inputs using two consecutive operations:\n\n"
        f"$$\\text{{Input }} n \\longrightarrow [\\times {mult}] \\longrightarrow [- {sub}] \\longrightarrow \\text{{Output}}$$\n\n"
        f"If the input is **$n = {inp}$**, calculate the final output."
    )
    sol = (
        f"**Step 1:** First operation: ${inp} \\times {mult} = {inp * mult}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Second operation: $${inp * mult} - {sub} = \\mathbf{{{out}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{out}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_flow_diagram_rule_evaluation",
        "hints": {
            "tier_1": f"Multiply {inp} by {mult}, then subtract {sub}.",
            "tier_2": f"{inp*mult} - {sub} = {out}.",
            "tier_3": f"{out}."
        }
    }


# ==============================================================================
# CLUSTER 2: Geometric & Special Sequences (09 - 16)
# ==============================================================================

def arch_09_doubling_geometric_sequence(rng: random.Random) -> Dict[str, Any]:
    start = rng.choice([3, 5, 7])
    terms = [start * (2 ** i) for i in range(4)]
    next_3 = [start * (2 ** i) for i in range(4, 7)]
    terms_s = "; ".join(str(x) for x in terms)
    next_s = "; ".join(str(x) for x in next_3)

    prompt = (
        f"Extend the geometric progression by three additional entries:\n\n"
        f"$${terms_s}; ...$$\n\n"
        f"State the multiplicative rule."
    )
    sol = (
        f"**Step 1:** The rule is to **multiply each term by 2** (doubling, constant ratio of 2) [1 Mark: Method].\n\n"
        f"**Step 2:** Next three terms:\n"
        f"- ${terms[3]} \\times 2 = {next_3[0]}$\n"
        f"- ${next_3[0]} \\times 2 = {next_3[1]}$\n"
        f"- ${next_3[1]} \\times 2 = {next_3[2]}$ [1 Mark: Accuracy].\n\n"
        f"$$\\mathbf{{{next_s}}}$$"
    )
    return {
        "id": f"g7_pat_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{next_s}; multiply by 2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_doubling_geometric_sequence",
        "hints": {
            "tier_1": "Notice each number is twice the previous number.",
            "tier_2": f"Double {terms[3]}.",
            "tier_3": f"{next_s}."
        }
    }


def arch_10_tripling_geometric_sequence(rng: random.Random) -> Dict[str, Any]:
    terms = [2, 6, 18, 54]
    next_term = 54 * 3

    prompt = (
        f"Determine the next term in the sequence:\n\n"
        f"$$2; 6; 18; 54; \\dots$$\n\n"
        f"Explain the relationship between consecutive terms."
    )
    sol = (
        f"**Step 1:** Each term is obtained by **multiplying by 3** (constant ratio $r = 3$) [1 Mark: Method].\n\n"
        f"**Step 2:** Next term: $$54 \\times 3 = \\mathbf{{{next_term}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{next_term}; multiply by 3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_tripling_geometric_sequence",
        "hints": {
            "tier_1": "Multiply 54 by 3.",
            "tier_2": "54 * 3 = 162.",
            "tier_3": "162."
        }
    }


def arch_11_square_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    terms = [1, 4, 9, 16, 25]
    next_2 = [36, 49]

    prompt = (
        f"Study the progression of perfect squares:\n\n"
        f"$$1; 4; 9; 16; 25; ...$$\n\n"
        f"1. Calculate the 6th and 7th perfect squares.\n"
        f"2. State the algebraic formula for \\(T_n\\)."
    )
    sol = (
        f"**Step 1:** Next two terms: $6^2 = \\mathbf{{36}}$ and $7^2 = \\mathbf{{49}}$ [1 Mark: Accuracy].\n\n"
        f"**Step 2:** The $n$-th term is: $$\\mathbf{{T_n = n^2}} \\text{{ [1 Mark: Formula]}}$$"
    )
    return {
        "id": f"g7_pat_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 36; 49; 2. Tn = n^2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_square_numbers_sequence",
        "hints": {
            "tier_1": "1^2=1, 2^2=4, 3^2=9... What is 6^2 and 7^2?",
            "tier_2": "6^2 = 36 and 7^2 = 49.",
            "tier_3": "36; 49; Tn = n^2."
        }
    }


def arch_12_cube_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    terms = [1, 8, 27, 64]
    next_term = 125

    prompt = (
        f"Consider the sequence of cube numbers:\n\n"
        f"$$1; 8; 27; 64; \\dots$$\n\n"
        f"Calculate the 5th term ($T_5$) and the 6th term ($T_6$)."
    )
    sol = (
        f"**Step 1:** $T_5 = 5^3 = 5 \\times 5 \\times 5 = \\mathbf{{125}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $T_6 = 6^3 = 6 \\times 6 \\times 6 = \\mathbf{{216}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "125; 216",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_cube_numbers_sequence",
        "hints": {
            "tier_1": "Cube 5 and cube 6.",
            "tier_2": "5^3 = 125, 6^3 = 216.",
            "tier_3": "125; 216."
        }
    }


def arch_13_triangular_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    terms = [1, 3, 6, 10, 15]
    next_term = 21  # 15 + 6

    prompt = (
        f"Triangular numbers represent objects that can be arranged in an equilateral triangle:\n\n"
        f"$$1; 3; 6; 10; 15; \\dots$$\n\n"
        f"1. How much is added from one term to the next?\n"
        f"2. Write down the 6th triangular number."
    )
    sol = (
        f"**Step 1:** Differences increase by 1 each time: $+2, +3, +4, +5$ [1 Mark: Method].\n\n"
        f"**Step 2:** To find the 6th term, add $+6$: $$15 + 6 = \\mathbf{{21}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. +2, +3, +4, +5, +6 (differences increase by 1); 2. 21",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_triangular_numbers_sequence",
        "hints": {
            "tier_1": "1 + 2 = 3; 3 + 3 = 6; 6 + 4 = 10; 10 + 5 = 15. Next add 6.",
            "tier_2": "15 + 6 = 21.",
            "tier_3": "Add 6; 6th term is 21."
        }
    }


def arch_14_fibonacci_sequence_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the Fibonacci progression:\n\n"
        f"$$1; 1; 2; 3; 5; 8; 13; ...$$\n\n"
        f"1. State the additive rule.\n"
        f"2. Calculate the 8th and 9th entries."
    )
    sol = (
        f"**Step 1:** Each term is the **sum of the two preceding terms** [1 Mark: Rule].\n\n"
        f"**Step 2:** Next terms:\n"
        f"- $8 + 13 = \\mathbf{{21}}$\n"
        f"- $13 + 21 = \\mathbf{{34}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Add the previous two terms; 2. 21; 34",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_fibonacci_sequence_concept",
        "hints": {
            "tier_1": "Add the last two numbers: 8 + 13.",
            "tier_2": "8 + 13 = 21, then 13 + 21 = 34.",
            "tier_3": "Add previous two terms; 21, 34."
        }
    }


def arch_15_alternating_operations_sequence(rng: random.Random) -> Dict[str, Any]:
    # +2, *2 pattern: 3, 5, 10, 12, 24, 26, 52
    terms = [3, 5, 10, 12, 24, 26]
    next_term = 26 * 2  # 52

    prompt = (
        f"Find the next term in the sequence:\n\n"
        f"$$3; 5; 10; 12; 24; 26; \\dots$$\n\n"
        f"Describe the alternating rule."
    )
    sol = (
        f"**Step 1:** The rule alternates between **adding 2** and **multiplying by 2** ($+2, \\times 2, +2, \\times 2, +2$) [1 Mark: Method].\n\n"
        f"**Step 2:** The next operation is $\\times 2$: $$26 \\times 2 = \\mathbf{{52}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "52; alternate between adding 2 and multiplying by 2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_alternating_operations_sequence",
        "hints": {
            "tier_1": "3+2=5, 5*2=10, 10+2=12, 12*2=24, 24+2=26. What operation comes next?",
            "tier_2": "Multiply 26 by 2.",
            "tier_3": "52."
        }
    }


def arch_16_classify_sequence_relationship(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ([5, 9, 13, 17], "Constant difference (+4)"),
        ([3, 6, 12, 24], "Constant ratio (x2)"),
        ([1, 4, 9, 16], "Neither (differences increase: +3, +5, +7)")
    ]
    seq, classification = rng.choice(cases)
    seq_s = "; ".join(str(x) for x in seq)

    prompt = (
        f"Classify the following sequence as having a **constant difference**, a **constant ratio**, or **neither**:\n\n"
        f"$${seq_s}; \\dots$$\n\n"
        f"Explain your reasoning."
    )
    sol = (
        f"**Step 1:** Test differences and ratios between consecutive terms [1 Mark: Method].\n\n"
        f"**Step 2:** Classification: **{classification}** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_pat_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": classification,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_classify_sequence_relationship",
        "hints": {
            "tier_1": "Subtract terms: are differences equal? Divide terms: are ratios equal?",
            "tier_2": classification,
            "tier_3": classification
        }
    }


# ==============================================================================
# CLUSTER 3: Matchstick Polygon Chains (17 - 25)
# ==============================================================================

def arch_17_matchstick_squares_chain(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 10, 12])
    total = 3 * n + 1

    svg_str = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 130" width="100%" height="130" style="background:#ffffff;">'
        f'<rect x="30" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<text x="52" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 1 (4 sticks)</text>'
        f'<rect x="150" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<rect x="195" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<text x="195" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 2 (7 sticks)</text>'
        f'<rect x="310" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<rect x="355" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<rect x="400" y="25" width="45" height="45" fill="none" stroke="#b45309" stroke-width="4"/>'
        f'<text x="377" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 3 (10 sticks) | Target n={n}</text>'
        f'</svg>'
    )
    svg_diag = {
        "kind": "inline_svg",
        "svg": svg_str,
        "caption": f"Chain of connected matchstick squares (Target n = {n})",
        "diagram_role": "context"
    }

    prompt = (
        f"A chain of connected squares is built using matchsticks:\n"
        f"- 1 square requires 4 matchsticks\n"
        f"- 2 connected squares require 7 matchsticks\n"
        f"- 3 connected squares require 10 matchsticks\n\n"
        f"1. Write down the general formula $M$ for $n$ connected squares.\n"
        f"2. Calculate the number of matchsticks needed for **{n} connected squares**."
    )
    sol = (
        f"**Step 1:** The first square uses 4 sticks, and each subsequent square adds 3 sticks. "
        f"Formula: $$\\mathbf{{M = 3n + 1}} \\text{{ [1 Mark: Formula]}}$$\n\n"
        f"**Step 2:** For $n = {n}$: $$M = 3({n}) + 1 = {3*n} + 1 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. M = 3n + 1; 2. {total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "17_matchstick_squares_chain",
        "hints": {
            "tier_1": "Formula is M = 3n + 1.",
            "tier_2": f"3 * {n} + 1.",
            "tier_3": f"M = 3n + 1; {total} matchsticks."
        }
    }


def arch_18_matchstick_triangles_chain(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([6, 8, 12, 15, 18])
    total = 2 * n + 1

    svg_str = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 130" width="100%" height="130" style="background:#ffffff;">'
        f'<polygon points="50,25 25,75 75,75" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<text x="50" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 1 (3 sticks)</text>'
        f'<polygon points="180,25 155,75 205,75" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<polygon points="205,75 180,25 230,25" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<text x="192" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 2 (5 sticks)</text>'
        f'<polygon points="340,25 315,75 365,75" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<polygon points="365,75 340,25 390,25" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<polygon points="390,25 365,75 415,75" fill="none" stroke="#b45309" stroke-width="4" stroke-linejoin="round"/>'
        f'<text x="365" y="95" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stage 3 (7 sticks) | Target n={n}</text>'
        f'</svg>'
    )
    svg_diag = {
        "kind": "inline_svg",
        "svg": svg_str,
        "caption": f"Chain of connected matchstick triangles (Target n = {n})",
        "diagram_role": "context"
    }

    prompt = (
        f"A chain of connected triangles is built with matchsticks:\n"
        f"- 1 triangle uses 3 matchsticks\n"
        f"- 2 connected triangles use 5 matchsticks\n"
        f"- 3 connected triangles use 7 matchsticks\n\n"
        f"1. State the formula for the number of matchsticks $M$ for $n$ triangles.\n"
        f"2. How many matchsticks are required to build **{n} connected triangles**?"
    )
    sol = (
        f"**Step 1:** Each new triangle shares one side with the previous, adding 2 sticks. "
        f"Formula: $$\\mathbf{{M = 2n + 1}} \\text{{ [1 Mark: Formula]}}$$\n\n"
        f"**Step 2:** For $n = {n}$: $$M = 2({n}) + 1 = {2*n} + 1 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. M = 2n + 1; 2. {total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "18_matchstick_triangles_chain",
        "hints": {
            "tier_1": "Formula is M = 2n + 1.",
            "tier_2": f"2 * {n} + 1.",
            "tier_3": f"M = 2n + 1; {total} matchsticks."
        }
    }


def arch_19_matchstick_pentagons_chain(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6, 8])
    total = 4 * n + 1

    prompt = (
        f"Connected pentagons are built in a line sharing adjacent sides:\n"
        f"- 1 pentagon: 5 matchsticks\n"
        f"- 2 pentagons: 9 matchsticks\n"
        f"- 3 pentagons: 13 matchsticks\n\n"
        f"Calculate the number of matchsticks required for **{n} connected pentagons**."
    )
    sol = (
        f"**Step 1:** The constant difference is 4 sticks per additional pentagon. Formula: $M = 4n + 1$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$M = 4({n}) + 1 = {4*n} + 1 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_matchstick_pentagons_chain",
        "hints": {
            "tier_1": "Rule is M = 4n + 1.",
            "tier_2": f"4 * {n} + 1.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_20_matchstick_hexagons_chain(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 7, 10])
    total = 5 * n + 1

    prompt = (
        f"Connected regular hexagons are built in a row:\n"
        f"- 1 hexagon: 6 matchsticks\n"
        f"- 2 hexagons: 11 matchsticks\n"
        f"- 3 hexagons: 16 matchsticks\n\n"
        f"Calculate the number of matchsticks needed to build a chain of **{n} hexagons**."
    )
    sol = (
        f"**Step 1:** Formula is $M = 5n + 1$ [1 Mark: Method].\n\n"
        f"**Step 2:** For $n = {n}$: $$M = 5({n}) + 1 = {5*n} + 1 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_matchstick_hexagons_chain",
        "hints": {
            "tier_1": "Rule is 5n + 1.",
            "tier_2": f"5 * {n} + 1.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_21_separate_independent_squares(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([8, 12, 15, 20])
    total = 4 * n

    prompt = (
        f"A learner builds **{n} separate, independent squares** (no shared sides) using matchsticks.\n\n"
        f"How many matchsticks are required in total?"
    )
    sol = (
        f"**Step 1:** Each independent square uses exactly 4 matchsticks [1 Mark: Method].\n\n"
        f"**Step 2:** Total sticks: $${n} \\times 4 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_separate_independent_squares",
        "hints": {
            "tier_1": f"Each separate square needs 4 sticks. Multiply {n} by 4.",
            "tier_2": f"{n} * 4 = {total}.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_22_separate_independent_triangles(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([9, 14, 18, 25])
    total = 3 * n

    prompt = (
        f"How many matchsticks are required to build **{n} completely separate triangles**?"
    )
    sol = (
        f"**Step 1:** Each triangle requires 3 matchsticks [1 Mark: Method].\n\n"
        f"**Step 2:** $${n} \\times 3 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_separate_independent_triangles",
        "hints": {
            "tier_1": f"Multiply {n} by 3.",
            "tier_2": f"{n} * 3 = {total}.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_23_matchstick_letter_h_pattern(rng: random.Random) -> Dict[str, Any]:
    # Letter H: 5 matchsticks for 1, connected HH: 9, HHH: 13 -> 4n + 1 (or 5 for separate 5n)
    n = rng.choice([5, 6, 8, 10])
    total = 5 * n

    prompt = (
        f"A learner constructs separate capital letters 'H' using matchsticks (2 vertical sticks on left, 2 vertical sticks on right, 1 horizontal crossbar = 5 matchsticks per 'H').\n\n"
        f"How many matchsticks are needed to form **{n} separate letter 'H' shapes**?"
    )
    sol = (
        f"**Step 1:** Each letter 'H' uses 5 matchsticks [1 Mark: Method].\n\n"
        f"**Step 2:** $${n} \\times 5 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_matchstick_letter_h_pattern",
        "hints": {
            "tier_1": f"Multiply {n} by 5.",
            "tier_2": f"{n} * 5 = {total}.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_24_matchstick_letter_e_pattern(rng: random.Random) -> Dict[str, Any]:
    # Letter E: 2 vertical + 3 horizontal = 5 matchsticks (or 4 sticks for simple E)
    n = rng.choice([4, 6, 7, 9])
    total = 4 * n

    prompt = (
        f"A simple letter 'E' is constructed from 4 matchsticks (1 vertical back stick and 3 horizontal arms).\n\n"
        f"Calculate the total matchsticks needed to build **{n} separate letter 'E's**."
    )
    sol = (
        f"**Step 1:** Each 'E' requires 4 matchsticks [1 Mark: Method].\n\n"
        f"**Step 2:** $${n} \\times 4 = \\mathbf{{{total}}} \\text{{ matchsticks [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_matchstick_letter_e_pattern",
        "hints": {
            "tier_1": f"Multiply {n} by 4.",
            "tier_2": f"{n} * 4 = {total}.",
            "tier_3": f"{total} matchsticks."
        }
    }


def arch_25_inverse_matchstick_problem(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([12, 15, 20, 25])
    matches = 3 * n + 1  # squares chain

    prompt = (
        f"A chain of connected squares is built using the rule $M = 3n + 1$.\n\n"
        f"If a learner used exactly **{matches} matchsticks**, how many connected squares did they build?"
    )
    sol = (
        f"**Step 1:** Set up the equation: $3n + 1 = {matches}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Solve for $n$:\n"
        f"$$3n = {matches} - 1 = {matches - 1}$$\n"
        f"$$n = \\frac{{{matches - 1}}}{{3}} = \\mathbf{{{n}}} \\text{{ squares [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_pat_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_inverse_matchstick_problem",
        "hints": {
            "tier_1": f"Subtract 1 from {matches}, then divide by 3.",
            "tier_2": f"({matches} - 1) / 3 = {n}.",
            "tier_3": f"{n} squares."
        }
    }
