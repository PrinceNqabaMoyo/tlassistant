"""
Grade 7 Mathematics - Integers Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_number_line_svg


# ==============================================================================
# CLUSTER 4: Number Lines, Ordering & Comparing (26 - 34)
# ==============================================================================

def arch_26_locating_negative_integers_between_benchmarks(rng: random.Random) -> Dict[str, Any]:
    b1 = -rng.randint(15, 25)
    b2 = b1 + rng.randint(4, 8)
    cand = rng.randint(b1 + 1, b2 - 1)
    opts = [cand, b1 - 2, b2 + 3, abs(cand)]
    rng.shuffle(opts)

    prompt = (
        f"Which of the following integers lies strictly between **{b1}** and **{b2}** on a standard number line?\n\n"
        f"Options: {', '.join(str(o) for o in opts)}"
    )
    sol = (
        f"**Step 1:** On a number line, numbers increase from left to right: ${b1} < x < {b2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Comparing candidates:\n\n"
        f"$${b1} < {cand} < {b2} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\mathbf{{{cand}}} \\text{{ is strictly between }} {b1} \\text{{ and }} {b2}$$"
    )
    return {
        "id": f"g7_int_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cand}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_locating_negative_integers_between_benchmarks",
        "hints": {
            "tier_1": f"The number must be greater than {b1} (to its right) and less than {b2} (to its left).",
            "tier_2": f"Remember that with negative numbers, {cand} is greater than {b1} because it is closer to 0.",
            "tier_3": f"Correct answer is {cand}."
        }
    }


def arch_27_comparing_integers_with_inequality_symbols(rng: random.Random) -> Dict[str, Any]:
    n1 = -rng.randint(8, 25)
    n2 = -rng.randint(8, 25)
    while n1 == n2:
        n2 = -rng.randint(8, 25)

    symbol = "<" if n1 < n2 else ">"
    reason = "further left from zero" if n1 < n2 else "closer to zero"

    prompt = (
        f"Insert the correct inequality symbol ($<$ or $>$) between the two integers to make the mathematical statement true:\n\n"
        f"$${n1} \\quad [\\; ? \\;] \\quad {n2}$$\n\n"
        f"Explain your answer with reference to the position of the numbers on a number line."
    )
    sol = (
        f"**Step 1:** Position on number line:\n\n"
        f"${n1}$ is located {reason} compared to ${n2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Statement with correct symbol:\n\n"
        f"$${n1} {symbol} {n2} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\mathbf{{{n1} {symbol} {n2}}}$$"
    )
    return {
        "id": f"g7_int_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{n1} {symbol} {n2}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_comparing_integers_with_inequality_symbols",
        "hints": {
            "tier_1": "The number further to the left on the number line is the smaller number (<).",
            "tier_2": f"Compare {n1} and {n2} relative to 0.",
            "tier_3": f"Correct statement: {n1} {symbol} {n2}."
        }
    }


def arch_28_ordering_five_integers_ascending(rng: random.Random) -> Dict[str, Any]:
    nums = [
        -rng.randint(18, 30),
        -rng.randint(5, 14),
        0,
        rng.randint(4, 12),
        rng.randint(16, 28),
    ]
    rng.shuffle(nums)
    s_nums = sorted(nums)
    ans_str = "; ".join(str(x) for x in s_nums)

    num_list_str = ", ".join(str(x) for x in nums)
    prompt = (
        f"Arrange the following five integers in **ascending order** (from smallest to largest):\n\n"
        f"$$\\{{ {num_list_str} \\}}$$"
    )
    sol = (
        f"**Step 1:** Arrange from the most negative (furthest left) through $0$ to the largest positive [1 Mark: Method].\n\n"
        f"**Step 2:** Ascending order:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_ordering_five_integers_ascending",
        "hints": {
            "tier_1": "Ascending order means starting with the smallest (most negative) number.",
            "tier_2": "Negative numbers come first, followed by zero, then positive numbers.",
            "tier_3": f"Correct order: {ans_str}."
        }
    }


def arch_29_ordering_five_integers_descending(rng: random.Random) -> Dict[str, Any]:
    nums = [
        -rng.randint(20, 35),
        -rng.randint(4, 15),
        rng.randint(-2, 2),
        rng.randint(8, 16),
        rng.randint(22, 38),
    ]
    rng.shuffle(nums)
    s_nums = sorted(nums, reverse=True)
    ans_str = "; ".join(str(x) for x in s_nums)

    num_list_str = ", ".join(str(x) for x in nums)
    prompt = (
        f"Arrange the following five integers in **descending order** (from largest to smallest):\n\n"
        f"$$\\{{ {num_list_str} \\}}$$"
    )
    sol = (
        f"**Step 1:** Descending order starts with the largest positive integer and moves leftward [1 Mark: Method].\n\n"
        f"**Step 2:** Descending sequence:\n\n"
        f"$$\\mathbf{{{ans_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_ordering_five_integers_descending",
        "hints": {
            "tier_1": "Descending order means highest number to lowest number.",
            "tier_2": "Start with the highest positive number and end with the most negative number.",
            "tier_3": f"Correct order: {ans_str}."
        }
    }


def arch_30_integer_distance_from_zero_absolute_value(rng: random.Random) -> Dict[str, Any]:
    val = -rng.randint(7, 24)
    abs_v = abs(val)

    prompt = (
        f"On a number line, consider the integer **{val}**.\n\n"
        f"1. What is the distance (in units) between **{val}** and the origin ($0$)?\n"
        f"2. Write down the absolute value: $|{val}| = \\dots$"
    )
    sol = (
        f"**Step 1:** Distance on a number line is always a non-negative scalar quantity [1 Mark: Method].\n\n"
        f"**Step 2:** The distance from ${val}$ to $0$ is **{abs_v} units**:\n\n"
        f"$$|{val}| = {abs_v} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Distance = {abs_v} units; |{val}| = {abs_v}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_integer_distance_from_zero_absolute_value",
        "hints": {
            "tier_1": "Distance can never be negative.",
            "tier_2": f"The number {val} is {abs_v} steps away from 0.",
            "tier_3": f"Distance is {abs_v} units, so |{val}| = {abs_v}."
        }
    }


def arch_31_midpoint_between_positive_and_negative_integer(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(2, 8)
    a = -rng.randint(4, 12) * 2
    # Ensure (a + b) is even
    b = a + 2 * k * rng.randint(2, 5)
    mid = (a + b) // 2

    prompt = (
        f"Find the exact midpoint integer that lies halfway between **{a}** and **+{b}** on a number line."
    )
    sol = (
        f"**Step 1:** Midpoint formula:\n\n"
        f"$$\\text{{Midpoint}} = \\frac{{{a} + ({b})}}{{2}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate:\n\n"
        f"$$\\frac{{{a + b}}}{{2}} = {mid} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\mathbf{{\\text{{Midpoint}} = {mid}}}$$"
    )
    return {
        "id": f"g7_int_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{mid}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_midpoint_between_positive_and_negative_integer",
        "hints": {
            "tier_1": "Add both numbers and divide by 2.",
            "tier_2": f"({a} + {b}) / 2 = {a + b} / 2.",
            "tier_3": f"Midpoint is {mid}."
        }
    }


def arch_32_opposite_integers_reflection_across_zero(rng: random.Random) -> Dict[str, Any]:
    val = rng.choice([-19, -14, -8, 7, 13, 21])
    opp = -val

    prompt = (
        f"1. Write down the opposite (additive inverse) of the integer **{val}**.\n"
        f"2. Show that adding the integer to its opposite equals $0$."
    )
    sol = (
        f"**Step 1:** The opposite of an integer has the same distance from zero but opposite sign:\n\n"
        f"$$\\text{{Opposite of }} ({val}) = {opp} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Verify zero sum:\n\n"
        f"$$({val}) + ({opp}) = 0 \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Opposite = {opp}; ({val}) + ({opp}) = 0",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_opposite_integers_reflection_across_zero",
        "hints": {
            "tier_1": "Change the sign to find the opposite.",
            "tier_2": f"If the number is {val}, its opposite is {opp}.",
            "tier_3": f"Opposite is {opp}, and ({val}) + ({opp}) = 0."
        }
    }


def arch_33_consecutive_integers_predecessor_and_successor(rng: random.Random) -> Dict[str, Any]:
    n = -rng.randint(5, 25)
    pred = n - 1
    succ = n + 1

    prompt = (
        f"For the negative integer **{n}**:\n\n"
        f"1. State its **predecessor** (the integer immediately before it, $n - 1$).\n"
        f"2. State its **successor** (the integer immediately after it, $n + 1$)."
    )
    sol = (
        f"**Step 1:** Predecessor ($n - 1$):\n\n"
        f"$${n} - 1 = {pred} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"**Step 2:** Successor ($n + 1$):\n\n"
        f"$${n} + 1 = {succ} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Predecessor}} = {pred}; \\quad \\text{{Successor}} = {succ}$$"
    )
    return {
        "id": f"g7_int_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Predecessor = {pred}; Successor = {succ}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_consecutive_integers_predecessor_and_successor",
        "hints": {
            "tier_1": "Predecessor is 1 step to the left (-1); Successor is 1 step to the right (+1).",
            "tier_2": f"Subtract 1 from {n} to get {pred}; add 1 to {n} to get {succ}.",
            "tier_3": f"Predecessor: {pred}, Successor: {succ}."
        }
    }


def arch_34_number_line_vector_jump_representation(rng: random.Random) -> Dict[str, Any]:
    start_v = -rng.randint(2, 6)
    jump = rng.randint(7, 14)
    end_v = start_v + jump
    svg = draw_number_line_svg(min_val=start_v - 3, max_val=end_v + 3, step=2, jumps=[(start_v, end_v, f"+{jump}")], label="Vector Addition Jump")

    prompt = (
        f"Examine the number line diagram showing a jump from **{start_v}** to **+{end_v}**.\n\n"
        f"Write down the integer addition equation represented by this arrow jump."
    )
    sol = (
        f"**Step 1:** Start at ${start_v}$ and observe arrow direction (rightward = positive jump of $+{jump}$) [1 Mark: Method].\n\n"
        f"**Step 2:** Equation:\n\n"
        f"$$({start_v}) + {jump} = {end_v} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"({start_v}) + {jump} = {end_v}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_number_line_vector_jump_representation",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "start_v": start_v, "jump": jump, "end_v": end_v},
        "hints": {
            "tier_1": "Start position + jump distance = finish position.",
            "tier_2": f"Start is {start_v}, arrow jumps right by {jump} units to {end_v}.",
            "tier_3": f"Equation: ({start_v}) + {jump} = {end_v}."
        }
    }


# ==============================================================================
# CLUSTER 5: Integer Addition & Subtraction Fundamentals (35 - 42)
# ==============================================================================

def arch_35_addition_of_two_negative_integers(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(6, 18)
    b = -rng.randint(5, 16)
    ans = a + b

    prompt = f"Calculate the value of: $$({a}) + ({b})$$"
    sol = (
        f"**Step 1:** Adding two negative numbers increases the total negative magnitude:\n\n"
        f"$$(-|{a}|) + (-|{b}|) = -({abs(a)} + {abs(b)}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate sum:\n\n"
        f"$$({a}) + ({b}) = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_addition_of_two_negative_integers",
        "hints": {
            "tier_1": "When adding two negatives, add their values and keep the negative sign.",
            "tier_2": f"-({abs(a)} + {abs(b)}).",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_36_addition_of_positive_and_negative_integer(rng: random.Random) -> Dict[str, Any]:
    pos = rng.randint(8, 24)
    neg = -rng.randint(5, 20)
    ans = pos + neg

    prompt = f"Calculate the value of: $${pos} + ({neg})$$"
    sol = (
        f"**Step 1:** Adding a negative integer is equivalent to subtracting its positive value:\n\n"
        f"$${pos} + ({neg}) = {pos} - {abs(neg)} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute:\n\n"
        f"$${pos} - {abs(neg)} = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_addition_of_positive_and_negative_integer",
        "hints": {
            "tier_1": "Adding a negative is the same as subtraction.",
            "tier_2": f"{pos} - {abs(neg)}.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_37_additive_inverse_property_zero_sum(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(12, 45)

    prompt = f"State the additive inverse property and calculate: $$(-{n}) + {n}$$"
    sol = (
        f"**Step 1:** The additive inverse of any integer $a$ is $-a$, and their sum is always zero [1 Mark: Method].\n\n"
        f"**Step 2:** Calculation:\n\n"
        f"$$(-{n}) + {n} = 0 \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "0",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_additive_inverse_property_zero_sum",
        "hints": {
            "tier_1": "Any number plus its opposite always equals 0.",
            "tier_2": f"-{n} and +{n} cancel each other out completely.",
            "tier_3": "Answer is 0."
        }
    }


def arch_38_subtracting_positive_from_smaller_positive(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 14)
    b = a + rng.randint(5, 18)
    ans = a - b

    prompt = f"Calculate the integer value of: $${a} - {b}$$"
    sol = (
        f"**Step 1:** Subtracting a larger number from a smaller number yields a negative result:\n\n"
        f"$${a} - {b} = -({b} - {a}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate:\n\n"
        f"$$-({b - a}) = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_subtracting_positive_from_smaller_positive",
        "hints": {
            "tier_1": "Since you are taking away more than you have, the result is negative.",
            "tier_2": f"Find {b} - {a} and make it negative.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_39_subtracting_positive_from_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(5, 19)
    b = rng.randint(6, 17)
    ans = a - b

    prompt = f"Calculate the value of: $$({a}) - {b}$$"
    sol = (
        f"**Step 1:** Subtracting a positive integer moves further left on the number line:\n\n"
        f"$$({a}) - {b} = -({abs(a)} + {b}) \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate result:\n\n"
        f"$$-({abs(a) + b}) = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_subtracting_positive_from_negative_integer",
        "hints": {
            "tier_1": "Start at a negative number and move further to the left.",
            "tier_2": f"Add the two numbers together and attach a negative sign.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_40_subtracting_negative_integer_double_negative_rule(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(6, 22)
    b = -rng.randint(4, 18)
    ans = a - b

    prompt = (
        f"Calculate the value of:\n\n"
        f"$${a} - ({b})$$\n\n"
        f"State the rule for subtracting a negative number."
    )
    sol = (
        f"**Step 1:** Subtracting a negative number is equivalent to adding its positive inverse ($a - (-b) = a + b$) [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate:\n\n"
        f"$${a} + {abs(b)} = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_subtracting_negative_integer_double_negative_rule",
        "hints": {
            "tier_1": "Two negative signs in a row (- -) become a plus (+).",
            "tier_2": f"{a} - ({b}) = {a} + {abs(b)}.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_41_subtracting_negative_from_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(8, 25)
    b = -rng.randint(4, 22)
    ans = a - b

    prompt = f"Calculate the value of: $$({a}) - ({b})$$"
    sol = (
        f"**Step 1:** Convert subtraction of negative to addition:\n\n"
        f"$$({a}) - ({b}) = {a} + {abs(b)} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Evaluate integer sum:\n\n"
        f"$${a} + {abs(b)} = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_subtracting_negative_from_negative_integer",
        "hints": {
            "tier_1": "Change - (-) to +.",
            "tier_2": f"{a} + {abs(b)}.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_42_three_term_addition_and_subtraction_chain(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(5, 14)
    b = rng.randint(8, 18)
    c = -rng.randint(4, 12)
    step1 = a + b
    ans = step1 - c

    prompt = (
        f"Calculate the value of the three-term integer expression step-by-step:\n\n"
        f"$$({a}) + {b} - ({c})$$"
    )
    sol = (
        f"**Step 1:** Evaluate the first addition: $({a}) + {b} = {step1}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract the third integer: ${step1} - ({c}) = {step1} + {abs(c)} = {ans}$ [1 Mark: Accuracy].\n\n"
        f"$$\\therefore \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_int_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_three_term_addition_and_subtraction_chain",
        "hints": {
            "tier_1": "Work from left to right.",
            "tier_2": f"First calculate ({a}) + {b} = {step1}. Then subtract ({c}).",
            "tier_3": f"Answer is {ans}."
        }
    }


# ==============================================================================
# CLUSTER 6: Algebraic Thinking & Missing Value Equations (43 - 50)
# ==============================================================================

def arch_43_missing_addend_positive_sum_x_plus_a_equals_b(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(12, 28)
    b = rng.randint(4, a - 2)
    x = b - a

    prompt = f"Find the value of $x$ that makes the equation true: $$x + {a} = {b}$$"
    sol = (
        f"**Step 1:** Subtract ${a}$ from both sides:\n\n"
        f"$$x = {b} - {a} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate:\n\n"
        f"$$x = {x} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {x}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_missing_addend_positive_sum_x_plus_a_equals_b",
        "hints": {
            "tier_1": "Isolate x by subtracting the number added to it.",
            "tier_2": f"x = {b} - {a}.",
            "tier_3": f"x = {x}."
        }
    }


def arch_44_missing_addend_negative_sum_x_plus_a_equals_neg_b(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(5, 16)
    b_neg = -rng.randint(4, 15)
    x = b_neg - a

    prompt = f"Solve for $x$: $$x + {a} = {b_neg}$$"
    sol = (
        f"**Step 1:** Subtract ${a}$ from both sides:\n\n"
        f"$$x = ({b_neg}) - {a} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute negative result:\n\n"
        f"$$x = {x} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {x}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_missing_addend_negative_sum_x_plus_a_equals_neg_b",
        "hints": {
            "tier_1": "Subtract the positive number from both sides.",
            "tier_2": f"x = ({b_neg}) - {a}.",
            "tier_3": f"x = {x}."
        }
    }


def arch_45_missing_subtrahend_a_minus_x_equals_neg_b(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(5, 14)
    res_neg = -rng.randint(6, 18)
    x = a - res_neg

    prompt = f"Determine the integer value of $x$: $${a} - x = {res_neg}$$"
    sol = (
        f"**Step 1:** Rearrange the equation: $x = {a} - ({res_neg})$ [1 Mark: Method].\n\n"
        f"**Step 2:** Simplify double negative:\n\n"
        f"$$x = {a} + {abs(res_neg)} = {x} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {x}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_missing_subtrahend_a_minus_x_equals_neg_b",
        "hints": {
            "tier_1": "Rearrange: x = a - (result).",
            "tier_2": f"x = {a} - ({res_neg}) = {a} + {abs(res_neg)}.",
            "tier_3": f"x = {x}."
        }
    }


def arch_46_missing_minuend_x_minus_a_equals_neg_b(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(10, 25)
    b_neg = -rng.randint(2, a - 3)
    x = b_neg + a

    prompt = f"Solve for $x$: $$x - {a} = {b_neg}$$"
    sol = (
        f"**Step 1:** Add ${a}$ to both sides:\n\n"
        f"$$x = ({b_neg}) + {a} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Compute:\n\n"
        f"$$x = {x} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {x}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_missing_minuend_x_minus_a_equals_neg_b",
        "hints": {
            "tier_1": "Add the subtracted number to both sides.",
            "tier_2": f"x = ({b_neg}) + {a}.",
            "tier_3": f"x = {x}."
        }
    }


def arch_47_evaluating_truth_value_of_integer_inequality(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(8, 20)
    b = -rng.randint(8, 20)
    while a == b:
        b = -rng.randint(8, 20)

    stated_symbol = rng.choice(["<", ">"])
    is_true = (a < b) if stated_symbol == "<" else (a > b)
    truth_str = "True" if is_true else "False"

    prompt = (
        f"Evaluate whether the following mathematical statement is **True** or **False**:\n\n"
        f"$${a} {stated_symbol} {b}$$\n\n"
        f"Justify your answer with reference to the positions of the integers on a number line."
    )
    actual_symbol = "<" if a < b else ">"
    sol = (
        f"**Step 1:** Compare ${a}$ and ${b}$ on a number line: ${a} {actual_symbol} {b}$ [1 Mark: Method].\n\n"
        f"**Step 2:** State truth value:\n\n"
        f"$$\\text{{The statement is }} \\mathbf{{{truth_str}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": truth_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_evaluating_truth_value_of_integer_inequality",
        "hints": {
            "tier_1": "Check which number is further to the left.",
            "tier_2": f"{a} is {'smaller' if a < b else 'greater'} than {b}.",
            "tier_3": f"Statement is {truth_str}."
        }
    }


def arch_48_integer_bracket_simplification_sign_rules(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 15)
    b = rng.randint(5, 14)
    c = rng.randint(6, 16)
    # -(-a) + (-b) - (+c) = a - b - c
    ans = a - b - c

    prompt = (
        f"Simplify the following expression by applying integer sign rules to clear the brackets:\n\n"
        f"$$-(-{a}) + (-{b}) - (+{c})$$"
    )
    sol = (
        f"**Step 1:** Clear brackets using sign rules:\n\n"
        f"- $-(-{a}) = +{a}$\n"
        f"- $+(-{b}) = -{b}$\n"
        f"- $-(+{c}) = -{c}$\n\n"
        f"$$\\text{{Expression}} = {a} - {b} - {c} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate final integer:\n\n"
        f"$${a} - {b} - {c} = {ans} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_int_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_integer_bracket_simplification_sign_rules",
        "hints": {
            "tier_1": "-(-) is +, +(-) is -, -(+) is -.",
            "tier_2": f"Rewrite as {a} - {b} - {c}.",
            "tier_3": f"Answer is {ans}."
        }
    }


def arch_49_integer_word_problem_multi_step_model(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Thandeka", "Kagiso", "Lwazi", "Zola"])
    start_temp = -rng.randint(3, 8)
    rise = rng.randint(10, 18)
    drop = rng.randint(rise - 4, rise + 5)
    final_temp = start_temp + rise - drop

    prompt = (
        f"In Sutherland at 04:00, **{name}** noted an outdoor temperature of **{start_temp}^\\circ\\text{{C}}**.\n\n"
        f"By 12:00, the temperature had **risen by {rise}^\\circ\\text{{C}}**.\n"
        f"By 22:00 that night, the temperature had **fallen by {drop}^\\circ\\text{{C}}** from its 12:00 reading.\n\n"
        f"Write down a single arithmetic expression and calculate the temperature at 22:00."
    )
    sol = (
        f"**Step 1:** Write the single expression:\n\n"
        f"$$\\text{{Temperature at 22:00}} = ({start_temp}) + {rise} - {drop} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Evaluate step-by-step:\n\n"
        f"$$({start_temp}) + {rise} = {start_temp + rise}^\\circ\\text{{C}}$$\n\n"
        f"$${start_temp + rise} - {drop} = {final_temp}^\\circ\\text{{C}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\text{{Night temperature is }} {final_temp}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_int_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{final_temp}°C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_integer_word_problem_multi_step_model",
        "hints": {
            "tier_1": "Start + rise - drop.",
            "tier_2": f"({start_temp}) + {rise} = {start_temp + rise}. Then subtract {drop}.",
            "tier_3": f"Final temperature is {final_temp}°C."
        }
    }


def arch_50_two_step_integer_balance_equation(rng: random.Random) -> Dict[str, Any]:
    x_val = -rng.randint(3, 9)
    c = rng.randint(5, 15)
    total = 2 * x_val + c

    prompt = f"Solve for $x$: $$2x + {c} = {total}$$"
    sol = (
        f"**Step 1:** Subtract ${c}$ from both sides:\n\n"
        f"$$2x = {total} - {c} = {total - c} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Divide by $2$:\n\n"
        f"$$x = \\frac{{{total - c}}}{{2}} = {x_val} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"$$\\therefore \\mathbf{{x = {x_val}}}$$"
    )
    return {
        "id": f"g7_int_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {x_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_two_step_integer_balance_equation",
        "hints": {
            "tier_1": f"Subtract {c} from both sides, then divide by 2.",
            "tier_2": f"2x = {total - c}.",
            "tier_3": f"x = {x_val}."
        }
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
