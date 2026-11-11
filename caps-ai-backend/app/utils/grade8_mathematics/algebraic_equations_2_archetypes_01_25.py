"""
Grade 8 Mathematics - Algebraic Equations 2 Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_classifying_open_vs_closed_number_sentence(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(12, 25)
    b = rng.randint(4, 9)
    c = a + b
    # closed: a + b = c; open: a + x = c
    return {
        "title": "Classifying Open vs Closed Number Sentences",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "01_classifying_open_vs_closed_number_sentence",
        "difficulty": "easy",
        "question_text": (
            f"Consider the two statements:\n\n"
            f"1. **${a} + {b} = {c}$**\n"
            f"2. **${a} + x = {c}$**\n\n"
            "Classify each as either an **open number sentence** or a **closed number sentence**, and explain the difference."
        ),
        "correct_answer": f"Statement 1 is a closed number sentence because all values are known and it is definitively true. Statement 2 is an open number sentence (an equation) because it contains an unknown variable (x) whose truth depends on the value substituted.",
        "marking_schema": [
            "Statement 1: closed number sentence (all values known) [1 mark]",
            "Statement 2: open number sentence / equation (contains variable x) [1 mark]",
        ],
        "hints": [
            "A closed sentence contains only numbers and can be judged true or false immediately.",
            "An open sentence has at least one unknown variable.",
        ],
        "misconception_tags": ["open_vs_closed_sentence_confusion"],
        "diagram_spec": None,
    }


def arch_02_writing_closed_number_sentence_bus_passengers(rng: random.Random) -> Dict[str, Any]:
    start = 55
    off1 = rng.randint(10, 15)
    on1 = rng.randint(6, 12)
    on2 = rng.randint(8, 14)
    final_pass = start - off1 + on1 + on2

    return {
        "title": "Formulating a Closed Number Sentence: Passenger Movements",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "02_writing_closed_number_sentence_bus_passengers",
        "difficulty": "easy",
        "question_text": (
            f"A municipal bus starts with **{start} passengers**.\n\n"
            f"- At Stop 1: **{off1} passengers alight (get off)** and **{on1} board (get on)**.\n"
            f"- At Stop 2: **{on2} passengers board**.\n\n"
            "Write a single **closed number sentence** showing the calculation for the final number of passengers, and evaluate it."
        ),
        "correct_answer": f"{start} - {off1} + {on1} + {on2} = {final_pass}",
        "marking_schema": [
            f"Formulate arithmetic expression: {start} - {off1} + {on1} + {on2} [1 mark]",
            f"State closed equality: {start} - {off1} + {on1} + {on2} = {final_pass} [1 mark]",
        ],
        "hints": [
            f"Subtract alighting passengers (-{off1}) and add boarding passengers (+{on1}, +{on2}).",
            f"{start} - {off1} = {start - off1}.",
            f"{start - off1} + {on1} + {on2} = {final_pass}.",
        ],
        "misconception_tags": ["closed_sentence_modeling_error"],
        "diagram_spec": None,
    }


def arch_03_writing_closed_number_sentence_discount_pricing(rng: random.Random) -> Dict[str, Any]:
    discount = rng.choice([120, 150, 200])
    paid = rng.choice([450, 500, 650])
    orig = paid + discount

    return {
        "title": "Formulating a Closed Number Sentence: Discount Pricing",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "03_writing_closed_number_sentence_discount_pricing",
        "difficulty": "easy",
        "question_text": (
            f"A cellphone costs **R{paid}** after a discount of **R{discount}** is subtracted.\n\n"
            "Write a closed number sentence calculating the **original price** in Rands."
        ),
        "correct_answer": f"R{paid} + R{discount} = R{orig}",
        "marking_schema": [
            f"Write closed number sentence: {paid} + {discount} = {orig} [1 mark]",
        ],
        "hints": [
            f"The original price before discount was R{paid} + R{discount}.",
            f"{paid} + {discount} = {orig}.",
        ],
        "misconception_tags": ["discount_reversal_addition_error"],
        "diagram_spec": None,
    }


def arch_04_linear_equation_variables_both_sides_positive_integers(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(3, 8)
    a = rng.randint(5, 9)
    c = rng.randint(2, a - 2)
    diff = a - c
    b = rng.randint(2, 10)
    d = diff * ans + b

    return {
        "title": "Solving Equations with Variables on Both Sides: Positive Root",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "04_linear_equation_variables_both_sides_positive_integers",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}x + {b} = {c}x + {d}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Collect x terms: {a}x - {c}x = {d} - {b} => {diff}x = {d - b} [1 mark]",
            f"Divide by {diff}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {c}x from both sides: ({a} - {c})x = {diff}x.",
            f"Subtract {b} from both sides: {d} - {b} = {d - b}.",
            f"{diff}x = {d - b} \\implies x = {ans}.",
        ],
        "misconception_tags": ["variable_collection_subtraction_error"],
        "diagram_spec": None,
    }


def arch_05_linear_equation_variables_both_sides_negative_solution(rng: random.Random) -> Dict[str, Any]:
    ans = -rng.randint(2, 6)
    a = rng.randint(5, 8)
    c = rng.randint(2, a - 2)
    diff = a - c
    b = rng.randint(12, 25)
    d = diff * ans + b  # d < b

    return {
        "title": "Solving Equations with Variables on Both Sides: Negative Root",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "05_linear_equation_variables_both_sides_negative_solution",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}x + {b} = {c}x + {d}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Collect terms: {diff}x = {d - b} [1 mark]",
            f"Divide by {diff}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {c}x from both sides: {diff}x.",
            f"Subtract {b} from both sides: {d} - {b} = {d - b}.",
            f"Divide: {d - b} ÷ {diff} = {ans}.",
        ],
        "misconception_tags": ["negative_root_division_sign_error"],
        "diagram_spec": None,
    }


def arch_06_linear_equation_variables_both_sides_negative_coefficients(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(2, 6)
    a = 2
    c = 5
    # -2x + b = -5x + d => (-2 - (-5))x = d - b => 3x = d - b
    b = rng.randint(4, 10)
    d = 3 * ans + b

    return {
        "title": "Solving Equations with Negative Variable Coefficients on Both Sides",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "06_linear_equation_variables_both_sides_negative_coefficients",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$-{a}x + {b} = -{c}x + {d}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Add {c}x to both sides: ({c} - {a})x = 3x [1 mark]",
            f"Subtract {b}: 3x = {d - b} => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Add {c}x to both sides to make the $x$ coefficient positive: -{a}x + {c}x = 3x.",
            f"Subtract {b} from both sides: {d} - {b} = {d - b}.",
            f"3x = {d - b} \\implies x = {ans}.",
        ],
        "misconception_tags": ["negative_coefficient_transposition_error"],
        "diagram_spec": None,
    }


def arch_07_linear_equation_variables_both_sides_zero_solution(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 8)
    c = rng.randint(1, 3)
    b = rng.randint(5, 15)

    return {
        "title": "Solving Equations with Zero as the Root ($x = 0$)",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "07_linear_equation_variables_both_sides_zero_solution",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}x + {b} = {c}x + {b}$$"
        ),
        "correct_answer": "0",
        "marking_schema": [
            f"Collect terms: ({a} - {c})x = {b} - {b} = 0 [1 mark]",
            f"Conclude x = 0 [1 mark]",
        ],
        "hints": [
            f"Subtract {c}x from both sides: {a - c}x.",
            f"Subtract {b} from both sides: {b} - {b} = 0.",
            f"{a - c}x = 0 \\implies x = 0.",
        ],
        "misconception_tags": ["zero_solution_vs_no_solution_confusion"],
        "diagram_spec": None,
    }


def arch_08_equation_with_single_bracket_on_left(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.randint(2, 5)
    c = 1
    ans = rng.randint(2, 6)
    # a(x + b) = x + d => ax + a*b = x + d => (a - 1)x = d - a*b
    diff = a - 1
    d = diff * ans + a * b

    return {
        "title": "Solving Equations with Brackets on One Side: $a(x + b) = cx + d$",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "08_equation_with_single_bracket_on_left",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by expanding the bracket first:\n\n"
            f"$${a}(x + {b}) = x + {d}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Expand left side: {a}x + {a * b} = x + {d} [1 mark]",
            f"Collect like terms and solve: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Distribute {a}: {a}x + {a * b} = x + {d}.",
            f"Subtract $x$ from both sides: {diff}x.",
            f"Subtract {a * b} from {d}: {d - a * b}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["bracket_expansion_before_rearrangement_gap"],
        "diagram_spec": None,
    }


def arch_09_equation_with_single_bracket_with_negative_multiplier(rng: random.Random) -> Dict[str, Any]:
    a = 2
    b = rng.randint(2, 5)
    ans = rng.randint(2, 6)
    # -2(x - b) = x + d => -2x + 2b = x + d => 2b - d = 3x => 3*ans = 2b - d
    d = 2 * b - 3 * ans

    d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

    return {
        "title": "Solving Equations with a Negative Bracket Multiplier",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "09_equation_with_single_bracket_with_negative_multiplier",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$-{a}(x - {b}) = x {d_str}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Expand bracket: -{a}x + {a * b} = x {d_str} [1 mark]",
            f"Solve for x: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Expand -{a}(x - {b}) carefully: -{a}x + {a * b}.",
            f"Add {a}x to both sides: 3x.",
            f"Subtract {d} from {a * b}: {a * b - d}.",
            f"3x = {a * b - d} \\implies x = {ans}.",
        ],
        "misconception_tags": ["negative_bracket_multiplier_error"],
        "diagram_spec": None,
    }


def arch_10_equation_with_brackets_on_both_sides(rng: random.Random) -> Dict[str, Any]:
    a = 3
    c = 2
    b = rng.randint(1, 4)
    ans = rng.randint(2, 6)
    # 3(x + b) = 2(x + d) => 3x + 3b = 2x + 2d => x = 2d - 3b => 2d = ans + 3b
    # choose d so that (ans + 3b) is even
    if (ans + 3 * b) % 2 != 0:
        ans += 1
    d = (ans + 3 * b) // 2

    return {
        "title": "Solving Equations with Brackets on Both Sides: $a(x + b) = c(x + d)$",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "10_equation_with_brackets_on_both_sides",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}(x + {b}) = {c}(x + {d})$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Expand both sides: {a}x + {a * b} = {c}x + {c * d} [1 mark]",
            f"Rearrange and solve: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Expand LHS: {a}x + {a * b}.",
            f"Expand RHS: {c}x + {c * d}.",
            f"Subtract {c}x from both sides: ({a} - {c})x = x.",
            f"Subtract {a * b} from {c * d}: {c * d} - {a * b} = {ans}.",
        ],
        "misconception_tags": ["both_sides_bracket_expansion_error"],
        "diagram_spec": None,
    }


def arch_11_equation_with_brackets_on_both_sides_mixed_signs(rng: random.Random) -> Dict[str, Any]:
    a = 4
    c = 2
    b = rng.randint(2, 4)
    ans = rng.randint(3, 7)
    # 4(x - b) = 2(x + d) => 4x - 4b = 2x + 2d => 2x = 2d + 4b => x = d + 2b => d = ans - 2b
    d = ans + 1  # ensure positive d
    ans_actual = d + 2 * b

    return {
        "title": "Solving Equations with Brackets on Both Sides (Mixed Signs)",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "11_equation_with_brackets_on_both_sides_mixed_signs",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}(x - {b}) = {c}(x + {d})$$"
        ),
        "correct_answer": str(ans_actual),
        "marking_schema": [
            f"Expand: {a}x - {a * b} = {c}x + {c * d} [1 mark]",
            f"Solve: 2x = {c * d + a * b} => x = {ans_actual} [1 mark]",
        ],
        "hints": [
            f"LHS: {a}x - {a * b}.",
            f"RHS: {c}x + {c * d}.",
            f"Combine x terms: {a}x - {c}x = 2x.",
            f"Combine constants: {c * d} + {a * b} = {c * d + a * b}.",
            f"2x = {c * d + a * b} \\implies x = {ans_actual}.",
        ],
        "misconception_tags": ["brackets_mixed_sign_inversion_error"],
        "diagram_spec": None,
    }


def arch_12_equation_expanding_two_brackets_on_same_side(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([2, 4])
    ans = rng.randint(2, 5)
    # a(x + 1) + b(x - 2) = (a + b)x + a - 2b
    c_val = (a + b) * ans + a - 2 * b

    return {
        "title": "Solving Equations: Expanding Two Brackets on the Same Side",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "12_equation_expanding_two_brackets_on_same_side",
        "difficulty": "hard",
        "question_text": (
            f"Expand and solve for $x$:\n\n"
            f"$${a}(x + 1) + {b}(x - 2) = {c_val}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Expand: {a}x + {a} + {b}x - {2 * b} = {c_val} [1 mark]",
            f"Combine like terms: {a + b}x + {a - 2 * b} = {c_val} => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Expand first bracket: {a}x + {a}.",
            f"Expand second bracket: {b}x - {2 * b}.",
            f"Combine like terms: {a + b}x + ({a - 2 * b}) = {c_val}.",
            f"Solve for $x$: $x = {ans}$.",
        ],
        "misconception_tags": ["multiple_bracket_expansion_error"],
        "diagram_spec": None,
    }


def arch_13_equation_with_subtraction_of_bracket(rng: random.Random) -> Dict[str, Any]:
    a = 5
    b = 3
    c = 2
    d = 4
    ans = rng.randint(2, 6)
    # (5x + 3) - (2x - 4) = 3x + 7 = k
    k = 3 * ans + 7

    return {
        "title": "Solving Equations with Subtracted Parentheses",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "13_equation_with_subtraction_of_bracket",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$({a}x + {b}) - ({c}x - {d}) = {k}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Distribute negative sign: {a}x + {b} - {c}x + {d} = {k} [1 mark]",
            f"Simplify: 3x + 7 = {k} => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Be careful with the minus sign: -({c}x - {d}) = -{c}x + {d}.",
            f"Combine like terms: ({a} - {c})x + ({b} + {d}) = 3x + 7.",
            f"3x + 7 = {k} \\implies 3x = {k - 7} \\implies x = {ans}.",
        ],
        "misconception_tags": ["bracket_subtraction_negative_sign_error"],
        "diagram_spec": None,
    }


def arch_14_equation_nested_brackets_combining_like_terms(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(2, 6)
    # 2(3x - 1) - 4(x + 2) = 6x - 2 - 4x - 8 = 2x - 10
    target = 2 * ans - 10

    return {
        "title": "Solving Multi-Bracket Linear Equations",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "14_equation_nested_brackets_combining_like_terms",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$2(3x - 1) - 4(x + 2) = {target}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Expand brackets: 6x - 2 - 4x - 8 = {target} [1 mark]",
            f"Combine like terms: 2x - 10 = {target} => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Expand: 2(3x) - 2(1) - 4(x) - 4(2) = 6x - 2 - 4x - 8.",
            f"Combine: 2x - 10 = {target}.",
            f"2x = {target + 10} \\implies x = {ans}.",
        ],
        "misconception_tags": ["multi_bracket_sign_distribution_error"],
        "diagram_spec": None,
    }


def arch_15_consecutive_integers_summing_to_negative_target(rng: random.Random) -> Dict[str, Any]:
    # Three consecutive integers summing to -33: n + (n+1) + (n+2) = 3n + 3 = -33 => 3n = -36 => n = -12
    # So integers are -12, -11, -10
    base = -rng.choice([10, 11, 12, 13])
    n1 = base
    n2 = base + 1
    n3 = base + 2
    tot = n1 + n2 + n3

    return {
        "title": "Consecutive Integers Summing to a Negative Target",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "15_consecutive_integers_summing_to_negative_target",
        "difficulty": "medium",
        "question_text": (
            f"The sum of three consecutive integers is **{tot}**.\n\n"
            "1. Write an algebraic equation using $n$ as the smallest integer.\n"
            "2. Solve the equation to find all three integers."
        ),
        "correct_answer": f"1. n + (n + 1) + (n + 2) = {tot} (or 3n + 3 = {tot}). 2. The integers are {n1}, {n2}, and {n3}.",
        "marking_schema": [
            f"Equation: 3n + 3 = {tot} [1 mark]",
            f"Solve: n = {n1}; all three integers ({n1}, {n2}, {n3}) [1 mark]",
        ],
        "hints": [
            f"Let the integers be $n$, $n + 1$, and $n + 2$.",
            f"$3n + 3 = {tot}$.",
            f"$3n = {tot - 3} \\implies n = {n1}$.",
        ],
        "misconception_tags": ["negative_consecutive_integer_order_error"],
        "diagram_spec": None,
    }


def arch_16_consecutive_multiples_sum(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([5, 10])
    m = rng.randint(4, 10)
    # m*k, (m+1)*k, (m+2)*k
    n1 = m * k
    n2 = (m + 1) * k
    n3 = (m + 2) * k
    tot = n1 + n2 + n3

    return {
        "title": "Solving Equations: Consecutive Multiples",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "16_consecutive_multiples_sum",
        "difficulty": "medium",
        "question_text": (
            f"The sum of three consecutive multiples of **{k}** is **{tot}**.\n\n"
            "1. Write an equation using $x$ as the smallest multiple.\n"
            "2. Determine the value of all three multiples."
        ),
        "correct_answer": f"1. x + (x + {k}) + (x + {2*k}) = {tot} (or 3x + {3*k} = {tot}). 2. {n1}, {n2}, and {n3}.",
        "marking_schema": [
            f"Equation: 3x + {3*k} = {tot} [1 mark]",
            f"Solve: x = {n1}; list all three ({n1}, {n2}, {n3}) [1 mark]",
        ],
        "hints": [
            f"Consecutive multiples of {k} increase by {k}: $x$, $x + {k}$, $x + {2*k}$.",
            f"Sum = $3x + {3*k} = {tot}$.",
            f"$3x = {tot - 3*k} \\implies x = {n1}$.",
        ],
        "misconception_tags": ["multiples_step_size_setup_error"],
        "diagram_spec": None,
    }


def arch_17_consecutive_odd_integers_sum(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(10, 25)
    n1 = 2 * k + 1
    n2 = n1 + 2
    tot = n1 + n2

    return {
        "title": "Solving Equations: Consecutive Odd Integers",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "17_consecutive_odd_integers_sum",
        "difficulty": "medium",
        "question_text": (
            f"The sum of two consecutive odd integers is **{tot}**.\n\n"
            "1. Set up an equation with $x$ as the smaller odd integer.\n"
            "2. Solve for $x$ and state both integers."
        ),
        "correct_answer": f"1. x + (x + 2) = {tot} (or 2x + 2 = {tot}). 2. {n1} and {n2}.",
        "marking_schema": [
            f"Equation: 2x + 2 = {tot} [1 mark]",
            f"Solve: x = {n1}; state both ({n1} and {n2}) [1 mark]",
        ],
        "hints": [
            "Consecutive odd numbers increase by 2 (e.g. 11, 13).",
            f"$x + (x + 2) = 2x + 2 = {tot}$.",
            f"$2x = {tot - 2} \\implies x = {n1}$.",
        ],
        "misconception_tags": ["consecutive_odd_step_error"],
        "diagram_spec": None,
    }


def arch_18_cost_comparison_two_cellular_packages(rng: random.Random) -> Dict[str, Any]:
    base_a = 150
    rate_a = 1.0  # R1 per min
    base_b = 50
    rate_b = 2.0  # R2 per min
    # base_a + rate_a * m = base_b + rate_b * m => 150 + m = 50 + 2m => m = 100
    m_eq = 100

    return {
        "title": "Modelling Cost Comparisons: Cellphone Contract Break-Even",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "18_cost_comparison_two_cellular_packages",
        "difficulty": "hard",
        "question_text": (
            "Two cellphone network packages charge monthly fees as follows:\n\n"
            f"- **Package A:** R{base_a} monthly base fee plus R1,00 per call minute.\n"
            f"- **Package B:** R{base_b} monthly base fee plus R2,00 per call minute.\n\n"
            "1. Write an equation in terms of call minutes $m$ where both packages cost the exact same amount.\n"
            "2. Solve for $m$ to find the break-even number of call minutes."
        ),
        "correct_answer": f"1. {base_a} + m = {base_b} + 2m. 2. m = {m_eq} minutes.",
        "marking_schema": [
            f"Equate both cost formulas: {base_a} + m = {base_b} + 2m [1 mark]",
            f"Solve: m = {m_eq} minutes [1 mark]",
        ],
        "hints": [
            f"Cost of A = R{base_a} + 1m.",
            f"Cost of B = R{base_b} + 2m.",
            f"Equate them: {base_a} + m = {base_b} + 2m.",
            f"Subtract $m$ and subtract {base_b}: m = {base_a} - {base_b} = {m_eq}.",
        ],
        "misconception_tags": ["break_even_linear_modeling_error"],
        "diagram_spec": None,
    }


def arch_19_cost_comparison_two_gym_memberships(rng: random.Random) -> Dict[str, Any]:
    base_a = 200
    fee_a = 20
    base_b = 100
    fee_b = 40
    # 200 + 20v = 100 + 40v => 100 = 20v => v = 5
    v_eq = 5

    return {
        "title": "Modelling Break-Even Comparisons: Gym Memberships",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "19_cost_comparison_two_gym_memberships",
        "difficulty": "medium",
        "question_text": (
            "Two fitness clubs offer monthly payment plans:\n\n"
            f"- **Club A:** R{base_a} base fee plus R{fee_a} per visit.\n"
            f"- **Club B:** R{base_b} base fee plus R{fee_b} per visit.\n\n"
            "Formulate an equation and calculate how many visits ($v$) make the total monthly cost of both clubs identical."
        ),
        "correct_answer": f"Equation: {base_a} + {fee_a}v = {base_b} + {fee_b}v. Solution: v = {v_eq} visits.",
        "marking_schema": [
            f"Equation: {base_a} + {fee_a}v = {base_b} + {fee_b}v [1 mark]",
            f"Solve: v = {v_eq} visits [1 mark]",
        ],
        "hints": [
            f"Set total costs equal: {base_a} + {fee_a}v = {base_b} + {fee_b}v.",
            f"Subtract {fee_a}v from both sides: {fee_b - fee_a}v.",
            f"Subtract {base_b} from {base_a}: {base_a - base_b}.",
            f"{fee_b - fee_a}v = {base_a - base_b} \\implies v = {v_eq}.",
        ],
        "misconception_tags": ["cost_comparison_equating_error"],
        "diagram_spec": None,
    }


def arch_20_geometric_perimeter_isosceles_triangle_equation(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(3, 7)
    # 2 equal sides (2x + 1), base (x + 4)
    # P = 2(2x + 1) + (x + 4) = 4x + 2 + x + 4 = 5x + 6
    p = 5 * ans + 6
    leg = 2 * ans + 1
    base = ans + 4

    return {
        "title": "Geometric Modelling: Perimeter of an Isosceles Triangle",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "20_geometric_perimeter_isosceles_triangle_equation",
        "difficulty": "hard",
        "question_text": (
            f"An isosceles triangle has two equal sides of length **$(2x + 1)\\text{{ cm}}$** "
            f"and a base of **$(x + 4)\\text{{ cm}}$**. Its perimeter is **{p}\\text{{ cm}}**.\n\n"
            "1. Write an equation in terms of $x$ for the perimeter.\n"
            "2. Solve for $x$ and determine the length of the equal sides."
        ),
        "correct_answer": f"1. 2(2x + 1) + (x + 4) = {p} (or 5x + 6 = {p}). 2. x = {ans}; equal sides = {leg} cm.",
        "marking_schema": [
            f"Equation: 5x + 6 = {p} [1 mark]",
            f"Solve: x = {ans}; side = {leg} cm [1 mark]",
        ],
        "hints": [
            "An isosceles triangle has two equal sides.",
            f"Perimeter = (2x + 1) + (2x + 1) + (x + 4) = 5x + 6.",
            f"5x + 6 = {p} \\implies 5x = {p - 6} \\implies x = {ans}.",
            f"Equal side = 2({ans}) + 1 = {leg} cm.",
        ],
        "misconception_tags": ["isosceles_perimeter_duplication_omission"],
        "diagram_spec": None,
    }


def arch_21_geometric_perimeter_equilateral_vs_square(rng: random.Random) -> Dict[str, Any]:
    # 3(x + 2) = 4(x - 1) => 3x + 6 = 4x - 4 => x = 10
    return {
        "title": "Geometric Modelling: Equating Perimeters of Different Shapes",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "21_geometric_perimeter_equilateral_vs_square",
        "difficulty": "hard",
        "question_text": (
            "An equilateral triangle has sides of length **$(x + 2)\\text{{ cm}}$**.\n"
            "A square has sides of length **$(x - 1)\\text{{ cm}}$**.\n\n"
            "If both shapes have the **exact same perimeter**, write an equation and solve for $x$."
        ),
        "correct_answer": "Equation: 3(x + 2) = 4(x - 1). Solution: x = 10 cm.",
        "marking_schema": [
            "Equate perimeters: 3(x + 2) = 4(x - 1) [1 mark]",
            "Expand and solve: 3x + 6 = 4x - 4 => x = 10 cm [1 mark]",
        ],
        "hints": [
            "Equilateral triangle perimeter = 3(x + 2).",
            "Square perimeter = 4(x - 1).",
            "3x + 6 = 4x - 4.",
            "Subtract 3x and add 4: x = 10.",
        ],
        "misconception_tags": ["equating_perimeters_side_count_error"],
        "diagram_spec": None,
    }


def arch_22_geometric_perimeter_rectangle_opposite_sides_equal(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(4, 9)
    # 3x - 4 and x + 12 => 3x - x = 12 + 4 => 2x = 16 => x = 8
    # let's parameterize: 3x - a = x + b => 2x = a + b => a + b is even
    a = 4
    b = 2 * ans - a
    len_val = 3 * ans - a

    return {
        "title": "Geometric Properties: Opposite Sides of a Rectangle",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "22_geometric_perimeter_rectangle_opposite_sides_equal",
        "difficulty": "medium",
        "question_text": (
            f"The two opposite lengths of a rectangle are given by the algebraic expressions "
            f"**$({3}x - {a})\\text{{ cm}}$** and **$(x + {b})\\text{{ cm}}$**.\n\n"
            "1. Using geometric properties of a rectangle, set up an equation for $x$.\n"
            "2. Solve for $x$ and determine the actual length of the rectangle."
        ),
        "correct_answer": f"1. 3x - {a} = x + {b}. 2. x = {ans}; length = {len_val} cm.",
        "marking_schema": [
            f"Equation: 3x - {a} = x + {b} [1 mark]",
            f"Solve: x = {ans}; length = {len_val} cm [1 mark]",
        ],
        "hints": [
            "Opposite sides of a rectangle are equal in length.",
            f"Set them equal: 3x - {a} = x + {b}.",
            f"2x = {b + a} \\implies x = {ans}.",
            f"Length = 3({ans}) - {a} = {len_val} cm.",
        ],
        "misconception_tags": ["rectangle_opposite_sides_property_gap"],
        "diagram_spec": None,
    }


def arch_23_geometric_angles_triangle_interior_sum(rng: random.Random) -> Dict[str, Any]:
    # 2x + 3x + 4x = 9x = 180 => x = 20
    ans = 20
    a1 = 2 * ans  # 40
    a2 = 3 * ans  # 60
    a3 = 4 * ans  # 80

    return {
        "title": "Geometric Modelling: Interior Angles of a Triangle",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "23_geometric_angles_triangle_interior_sum",
        "difficulty": "medium",
        "question_text": (
            "The three interior angles of a triangle are **$2x^\\circ$**, **$3x^\\circ$**, and **$4x^\\circ$**.\n\n"
            "1. Set up an algebraic equation based on the angle sum of a triangle.\n"
            "2. Solve for $x$ and determine the size of the largest angle."
        ),
        "correct_answer": f"1. 2x + 3x + 4x = 180 (or 9x = 180). 2. x = {ans}°; largest angle = {a3}°.",
        "marking_schema": [
            "Equation: 9x = 180 [1 mark]",
            f"Solve: x = {ans}°; largest angle = {a3}° [1 mark]",
        ],
        "hints": [
            "The sum of the interior angles of any triangle is 180 degrees.",
            f"2x + 3x + 4x = 9x = 180.",
            f"x = 180 ÷ 9 = {ans}.",
            f"Largest angle = 4({ans}) = {a3}°.",
        ],
        "misconception_tags": ["triangle_interior_angles_sum_gap"],
        "diagram_spec": None,
    }


def arch_24_geometric_angles_vertically_opposite_equation(rng: random.Random) -> Dict[str, Any]:
    # Vertically opposite angles are equal: 4x - 10 = 2x + 30 => 2x = 40 => x = 20
    ans = 20
    ang = 4 * ans - 10  # 70

    return {
        "title": "Geometric Modelling: Vertically Opposite Angles",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "24_geometric_angles_vertically_opposite_equation",
        "difficulty": "medium",
        "question_text": (
            "Two straight intersecting lines create vertically opposite angles of "
            "**$(4x - 10)^\\circ$** and **$(2x + 30)^\\circ$**.\n\n"
            "1. Write an algebraic equation based on their geometric relationship.\n"
            "2. Solve for $x$ and determine the degree measurement of the angles."
        ),
        "correct_answer": f"1. 4x - 10 = 2x + 30. 2. x = {ans}°; angle size = {ang}°.",
        "marking_schema": [
            "Equation: 4x - 10 = 2x + 30 [1 mark]",
            f"Solve: x = {ans}°; angle = {ang}° [1 mark]",
        ],
        "hints": [
            "Vertically opposite angles are equal.",
            "4x - 10 = 2x + 30.",
            "2x = 40 \\implies x = 20.",
            f"Angle = 4(20) - 10 = {ang}°.",
        ],
        "misconception_tags": ["vertically_opposite_angles_equating_gap"],
        "diagram_spec": None,
    }


def arch_25_geometric_angles_adjacent_supplementary_equation(rng: random.Random) -> Dict[str, Any]:
    # 3x + 15 + 2x + 25 = 180 => 5x + 40 = 180 => 5x = 140 => x = 28
    ans = 28
    a1 = 3 * ans + 15  # 99
    a2 = 2 * ans + 25  # 81

    return {
        "title": "Geometric Modelling: Adjacent Angles on a Straight Line",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "25_geometric_angles_adjacent_supplementary_equation",
        "difficulty": "medium",
        "question_text": (
            "Two adjacent angles lying on a straight line are given by **$(3x + 15)^\\circ$** "
            "and **$(2x + 25)^\\circ$**.\n\n"
            "1. Formulate the algebraic equation.\n"
            "2. Solve for $x$ and calculate the size of both angles."
        ),
        "correct_answer": f"1. (3x + 15) + (2x + 25) = 180 (or 5x + 40 = 180). 2. x = {ans}°; angles are {a1}° and {a2}°.",
        "marking_schema": [
            "Equation: 5x + 40 = 180 [1 mark]",
            f"Solve: x = {ans}°; angles {a1}° and {a2}° [1 mark]",
        ],
        "hints": [
            "Angles on a straight line add up to 180 degrees.",
            f"(3x + 15) + (2x + 25) = 5x + 40 = 180.",
            f"5x = 140 \\implies x = {ans}.",
            f"Angles: 3({ans}) + 15 = {a1}° and 2({ans}) + 25 = {a2}°.",
        ],
        "misconception_tags": ["straight_line_angles_equation_setup"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_classifying_open_vs_closed_number_sentence,
    arch_02_writing_closed_number_sentence_bus_passengers,
    arch_03_writing_closed_number_sentence_discount_pricing,
    arch_04_linear_equation_variables_both_sides_positive_integers,
    arch_05_linear_equation_variables_both_sides_negative_solution,
    arch_06_linear_equation_variables_both_sides_negative_coefficients,
    arch_07_linear_equation_variables_both_sides_zero_solution,
    arch_08_equation_with_single_bracket_on_left,
    arch_09_equation_with_single_bracket_with_negative_multiplier,
    arch_10_equation_with_brackets_on_both_sides,
    arch_11_equation_with_brackets_on_both_sides_mixed_signs,
    arch_12_equation_expanding_two_brackets_on_same_side,
    arch_13_equation_with_subtraction_of_bracket,
    arch_14_equation_nested_brackets_combining_like_terms,
    arch_15_consecutive_integers_summing_to_negative_target,
    arch_16_consecutive_multiples_sum,
    arch_17_consecutive_odd_integers_sum,
    arch_18_cost_comparison_two_cellular_packages,
    arch_19_cost_comparison_two_gym_memberships,
    arch_20_geometric_perimeter_isosceles_triangle_equation,
    arch_21_geometric_perimeter_equilateral_vs_square,
    arch_22_geometric_perimeter_rectangle_opposite_sides_equal,
    arch_23_geometric_angles_triangle_interior_sum,
    arch_24_geometric_angles_vertically_opposite_equation,
    arch_25_geometric_angles_adjacent_supplementary_equation,
]
