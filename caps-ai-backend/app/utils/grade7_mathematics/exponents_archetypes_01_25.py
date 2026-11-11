"""
Grade 7 Mathematics - Exponents, Squares & Cubes Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Exponents.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Notation & Concepts of Powers (01 - 08)
# ==============================================================================

def arch_01_base_and_exponent_identification(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    exp = rng.choice([3, 4, 5, 6])

    prompt = (
        f"Consider the exponential expression: $${base}^{{{exp}}}$$\n\n"
        f"1. Name the **base**.\n"
        f"2. Name the **exponent** (or index).\n"
        f"3. Explain what the exponent indicates."
    )
    sol = (
        f"**Step 1:** The base is the repeated factor: **Base = {base}** [1 Mark: Method].\n\n"
        f"**Step 2:** The exponent is the power superscript: **Exponent = {exp}** [1 Mark: Accuracy].\n\n"
        f"**Step 3:** The exponent {exp} indicates that the base {base} is multiplied by itself {exp} times."
    )
    return {
        "id": f"g7_exp_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Base = {base}; Exponent = {exp}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "01_base_and_exponent_identification",
        "hints": {
            "tier_1": "The base is the main number on the line; the exponent is the small raised number.",
            "tier_2": f"In {base}^{exp}, the base is {base}.",
            "tier_3": f"Base: {base}, Exponent: {exp}."
        }
    }


def arch_02_repeated_multiplication_to_power(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5, 6, 7])
    n = rng.choice([3, 4, 5, 6])
    repeated_str = " \\times ".join([str(base)] * n)

    prompt = (
        f"Write the following repeated multiplication in concise exponential notation:\n\n"
        f"$${repeated_str}$$"
    )
    sol = (
        f"**Step 1:** Identify the repeated factor: base is ${base}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Count the number of factors: {n} factors $\\rightarrow$ power is ${n}$:\n\n"
        f"$$\\mathbf{{{base}^{{{n}}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base}^{n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_repeated_multiplication_to_power",
        "hints": {
            "tier_1": f"Count how many times {base} is multiplied by itself.",
            "tier_2": f"There are {n} factors of {base}.",
            "tier_3": f"{base}^{n}."
        }
    }


def arch_03_power_expanded_to_repeated_multiplication(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([3, 4, 5, 6, 8])
    exp = rng.choice([3, 4, 5])
    expanded = " × ".join([str(base)] * exp)

    prompt = f"Expand the power $${base}^{{{exp}}}$$ as a repeated multiplication string and calculate its value."
    val = base ** exp
    sol = (
        f"**Step 1:** Expand: ${base}^{{{exp}}} = {expanded}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate product: $\\mathbf{{{val}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{expanded} = {val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_power_expanded_to_repeated_multiplication",
        "hints": {
            "tier_1": f"Write {base} multiplied by itself {exp} times.",
            "tier_2": f"{expanded}.",
            "tier_3": f"= {val}."
        }
    }


def arch_04_evaluating_small_base_powers(rng: random.Random) -> Dict[str, Any]:
    cases = [(2, 4, 16), (2, 5, 32), (2, 6, 64), (3, 3, 27), (3, 4, 81), (4, 3, 64), (5, 3, 125)]
    b, e, val = rng.choice(cases)

    prompt = f"Evaluate the value of the power: $${b}^{{{e}}}$$"
    sol = (
        f"**Step 1:** Repeated multiplication: ${' \\times '.join([str(b)]*e)}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate: $\\mathbf{{{val}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "04_evaluating_small_base_powers",
        "hints": {
            "tier_1": f"Multiply {b} by itself {e} times.",
            "tier_2": f"{b}^{e}.",
            "tier_3": f"Value = {val}."
        }
    }


def arch_05_powers_of_ten_evaluation(rng: random.Random) -> Dict[str, Any]:
    exp = rng.choice([2, 3, 4, 5, 6])
    val = 10 ** exp
    val_s = f"{val:,}".replace(",", " ")

    prompt = f"Calculate the exact numerical value of: $$10^{{{exp}}}$$"
    sol = (
        f"**Step 1:** For base 10, the exponent equals the number of zeros following 1 [1 Mark: Method].\n\n"
        f"**Step 2:** 1 followed by {exp} zeros:\n\n"
        f"$$\\mathbf{{{val_s}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": val_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_powers_of_ten_evaluation",
        "hints": {
            "tier_1": f"10 raised to power {exp} has {exp} zeros after the digit 1.",
            "tier_2": f"1 with {exp} zeros.",
            "tier_3": f"{val_s}."
        }
    }


def arch_06_zero_exponent_law(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([7, 14, 25, 48, 89, 135])

    prompt = (
        f"1. State the **zero exponent law**.\n"
        f"2. Evaluate the expression: $${n}^0$$"
    )
    sol = (
        f"**Step 1:** Any non-zero base raised to the power of zero equals 1: $a^0 = 1$ ($a \\neq 0$) [1 Mark: Method].\n\n"
        f"**Step 2:** Apply to ${n}$: $${n}^0 = \\mathbf{{1}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_zero_exponent_law",
        "hints": {
            "tier_1": "Any non-zero number to power 0 always equals 1.",
            "tier_2": f"{n}^0 = 1.",
            "tier_3": "Answer is 1."
        }
    }


def arch_07_first_power_identity(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(23, 145)

    prompt = f"Evaluate: $${n}^1$$"
    sol = (
        f"**Step 1:** Any base raised to the power of 1 is equal to the base itself: $a^1 = a$ [1 Mark: Method].\n\n"
        f"**Step 2:** Value: $\\mathbf{{{n}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_first_power_identity",
        "hints": {
            "tier_1": "Raising a number to power 1 means taking that number once.",
            "tier_2": f"{n}^1 = {n}.",
            "tier_3": f"Answer is {n}."
        }
    }


def arch_08_comparing_powers_inequality(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (2, 5, 32, 5, 2, 25),  # 2^5 = 32 > 5^2 = 25
        (3, 4, 81, 4, 3, 64),  # 3^4 = 81 > 4^3 = 64
        (2, 4, 16, 4, 2, 16),  # 2^4 = 4^2 = 16
        (3, 2, 9, 2, 3, 8),    # 3^2 = 9 > 2^3 = 8
    ]
    b1, e1, v1, b2, e2, v2 = rng.choice(pairs)
    sym = ">" if v1 > v2 else ("<" if v1 < v2 else "=")

    prompt = (
        f"Compare the two values by inserting $<$, $>$, or $=$:\n\n"
        f"$${b1}^{{{e1}}} \\quad [\\; ? \\;] \\quad {b2}^{{{e2}}}$$\n\n"
        f"Show the numerical value of both powers."
    )
    sol = (
        f"**Step 1:** Evaluate both powers: ${b1}^{{{e1}}} = {v1}$ and ${b2}^{{{e2}}} = {v2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compare values:\n\n"
        f"$$\\mathbf{{{b1}^{{{e1}}} {sym} {b2}^{{{e2}}}}} \\quad ({v1} {sym} {v2}) \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{b1}^{e1} {sym} {b2}^{e2}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "08_comparing_powers_inequality",
        "hints": {
            "tier_1": f"Calculate {b1}^{e1} and {b2}^{e2} separately.",
            "tier_2": f"{v1} vs {v2}.",
            "tier_3": f"{b1}^{e1} {sym} {b2}^{e2}."
        }
    }


# ==============================================================================
# CLUSTER 2: Squares & Square Roots (09 - 18)
# ==============================================================================

def arch_09_calculating_squares_1_to_15(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(4, 15)
    sq = n * n

    prompt = f"Calculate the value of: $${n}^2$$"
    sol = (
        f"**Step 1:** Expand as repeated multiplication: ${n} \\times {n}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply: ${n} \\times {n} = \\mathbf{{{sq}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sq}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_calculating_squares_1_to_15",
        "hints": {
            "tier_1": f"Multiply {n} by itself.",
            "tier_2": f"{n} × {n}.",
            "tier_3": f"{sq}."
        }
    }


def arch_10_calculating_squares_multiples_of_ten(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([20, 30, 40, 50, 60, 70, 80, 90])
    sq = base * base
    sq_s = f"{sq:,}".replace(",", " ")

    prompt = f"Calculate mentally: $${base}^2$$"
    sol = (
        f"**Step 1:** Square the leading digit and double the zeros: $({base // 10})^2 \\times 100$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute: ${(base // 10)**2} \\times 100 = \\mathbf{{{sq_s}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": sq_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_calculating_squares_multiples_of_ten",
        "hints": {
            "tier_1": f"Square {base // 10} and attach two zeros.",
            "tier_2": f"{(base // 10)**2} followed by 00.",
            "tier_3": f"{sq_s}."
        }
    }


def arch_11_square_root_perfect_squares_1_to_144(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])
    r = int(math.isqrt(n))

    prompt = f"Calculate the square root: $$\\sqrt{{{n}}}$$"
    sol = (
        f"**Step 1:** Find the positive integer that when squared gives ${n}$: ${r}^2 = {n}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Value: $\\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_square_root_perfect_squares_1_to_144",
        "hints": {
            "tier_1": f"What number multiplied by itself gives {n}?",
            "tier_2": f"{r} × {r} = {n}.",
            "tier_3": f"sqrt({n}) = {r}."
        }
    }


def arch_12_square_root_perfect_squares_169_to_400(rng: random.Random) -> Dict[str, Any]:
    cases = [(169, 13), (196, 14), (225, 15), (256, 16), (289, 17), (324, 18), (361, 19), (400, 20)]
    sq, r = rng.choice(cases)

    prompt = f"Determine the square root: $$\\sqrt{{{sq}}}$$"
    sol = (
        f"**Step 1:** Since ${r} \\times {r} = {sq}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Square root is $\\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_square_root_perfect_squares_169_to_400",
        "hints": {
            "tier_1": f"Between 10 and 20, find the number that squares to {sq}.",
            "tier_2": f"{r} × {r} = {sq}.",
            "tier_3": f"sqrt({sq}) = {r}."
        }
    }


def arch_13_square_root_of_multiples_of_hundred(rng: random.Random) -> Dict[str, Any]:
    cases = [(400, 20), (900, 30), (1600, 40), (2500, 50), (3600, 60), (4900, 70), (6400, 80), (8100, 90)]
    sq, r = rng.choice(cases)
    sq_s = f"{sq:,}".replace(",", " ")

    prompt = f"Calculate the square root: $$\\sqrt{{{sq_s}}}$$"
    sol = (
        f"**Step 1:** Take square root of leading digit(s) and halve the count of zeros [1 Mark: Method].\n\n"
        f"**Step 2:** $\\sqrt{{{sq_s}}} = \\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_square_root_of_multiples_of_hundred",
        "hints": {
            "tier_1": f"sqrt({sq // 100}) = {r // 10}, then multiply by 10.",
            "tier_2": f"{r} × {r} = {sq}.",
            "tier_3": f"Answer is {r}."
        }
    }


def arch_14_estimating_square_roots_between_consecutive_integers(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([20, 29, 45, 52, 68, 75, 95])
    low_r = int(math.isqrt(n))
    high_r = low_r + 1

    prompt = (
        f"Between which two consecutive whole numbers does $$\\sqrt{{{n}}}$$ lie on a number line?\n\n"
        f"Show the perfect squares immediately below and above **{n}**."
    )
    sol = (
        f"**Step 1:** Identify bounding perfect squares: ${low_r**2} < {n} < {high_r**2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Take square roots: $\\sqrt{{{low_r**2}}} < \\sqrt{{{n}}} < \\sqrt{{{high_r**2}}}$:\n\n"
        f"$$\\mathbf{{{low_r} < \\sqrt{{{n}}} < {high_r}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_exp_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Between {low_r} and {high_r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_estimating_square_roots_between_consecutive_integers",
        "hints": {
            "tier_1": f"Find the perfect square just below {n} and just above {n}.",
            "tier_2": f"{low_r}^2 = {low_r**2} and {high_r}^2 = {high_r**2}.",
            "tier_3": f"Between {low_r} and {high_r}."
        }
    }


def arch_15_geometric_area_to_side_length_square_root(rng: random.Random) -> Dict[str, Any]:
    side = rng.randint(6, 15)
    area = side * side

    prompt = (
        f"A square vegetable patch at a school has an area of **{area} m$^2$**.\n\n"
        f"Calculate the length of one side of the patch."
    )
    sol = (
        f"**Step 1:** Area of a square formula: $\\text{{Area}} = s^2 \\rightarrow s = \\sqrt{{\\text{{Area}}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute side length: $s = \\sqrt{{{area}}} = \\mathbf{{{side} \\text{{ m}}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{side} m",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_geometric_area_to_side_length_square_root",
        "hints": {
            "tier_1": "The side of a square is the square root of its area.",
            "tier_2": f"s = sqrt({area}).",
            "tier_3": f"Side = {side} m."
        }
    }


def arch_16_sum_and_difference_of_two_squares(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 6])
    b = rng.choice([2, 3, 4])
    sum_sq = a*a + b*b

    prompt = f"Calculate the exact value of: $${a}^2 + {b}^2$$"
    sol = (
        f"**Step 1:** Square each number first: ${a}^2 = {a*a}$ and ${b}^2 = {b*b}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Add squares: ${a*a} + {b*b} = \\mathbf{{{sum_sq}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sum_sq}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_sum_and_difference_of_two_squares",
        "hints": {
            "tier_1": f"Square {a} and {b} before adding.",
            "tier_2": f"{a*a} + {b*b}.",
            "tier_3": f"Sum = {sum_sq}."
        }
    }


def arch_17_square_of_a_sum_misconception_check(rng: random.Random) -> Dict[str, Any]:
    a = 3
    b = 4
    sq_sum = (a + b) ** 2  # 49
    sum_sq = a**2 + b**2   # 25

    prompt = (
        f"Consider the numbers $a = {a}$ and $b = {b}$:\n\n"
        f"1. Calculate $({a} + {b})^2$.\n"
        f"2. Calculate ${a}^2 + {b}^2$.\n"
        f"3. Is $({a} + {b})^2 = {a}^2 + {b}^2$? (Answer Yes or No)"
    )
    sol = (
        f"**Step 1:** $({a} + {b})^2 = {a + b}^2 = \\mathbf{{{sq_sum}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** ${a}^2 + {b}^2 = {a**2} + {b**2} = \\mathbf{{{sum_sq}}}$.\n\n"
        f"**Step 3:** Since ${sq_sum} \\neq {sum_sq}$, $(a + b)^2 \\neq a^2 + b^2$. **No** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"({a} + {b})^2 = {sq_sum}; {a}^2 + {b}^2 = {sum_sq}; No",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_square_of_a_sum_misconception_check",
        "hints": {
            "tier_1": "Add inside brackets first for (a + b)^2.",
            "tier_2": f"7^2 = 49, whereas 9 + 16 = 25.",
            "tier_3": "They are not equal (No)."
        }
    }


def arch_18_difference_of_squares_evaluation(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 15)
    b = rng.randint(3, a - 2)
    diff = a*a - b*b

    prompt = f"Calculate the difference of the two squares: $${a}^2 - {b}^2$$"
    sol = (
        f"**Step 1:** Evaluate each square: ${a}^2 = {a*a}$ and ${b}^2 = {b*b}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract: ${a*a} - {b*b} = \\mathbf{{{diff}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_difference_of_squares_evaluation",
        "hints": {
            "tier_1": f"Square {a} and square {b}, then subtract.",
            "tier_2": f"{a*a} - {b*b}.",
            "tier_3": f"Difference = {diff}."
        }
    }


# ==============================================================================
# CLUSTER 3: Cubes & Cube Roots (19 - 25)
# ==============================================================================

def arch_19_calculating_cubes_1_to_6(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(2, 6)
    cube = n * n * n

    prompt = f"Calculate the value of: $${n}^3$$"
    sol = (
        f"**Step 1:** Expand as repeated multiplication: ${n} \\times {n} \\times {n}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Multiply: ${n} \\times {n} \\times {n} = \\mathbf{{{cube}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cube}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_calculating_cubes_1_to_6",
        "hints": {
            "tier_1": f"Multiply {n} by itself, then multiply by {n} again.",
            "tier_2": f"{n} × {n} = {n*n}, then {n*n} × {n}.",
            "tier_3": f"Cube = {cube}."
        }
    }


def arch_20_calculating_cubes_7_to_10(rng: random.Random) -> Dict[str, Any]:
    cases = [(7, 343), (8, 512), (9, 729), (10, 1000)]
    n, cube = rng.choice(cases)

    prompt = f"Determine the cube of **{n}**: $${n}^3$$"
    sol = (
        f"**Step 1:** Multiply three factors of ${n}$: ${n} \\times {n} \\times {n}$ [1 Mark: Method].\n\n"
        f"**Step 2:** ${n}^3 = \\mathbf{{{cube}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cube}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_calculating_cubes_7_to_10",
        "hints": {
            "tier_1": f"{n} cubed is {n} × {n} × {n}.",
            "tier_2": f"{n*n} × {n}.",
            "tier_3": f"{cube}."
        }
    }


def arch_21_cube_root_perfect_cubes_1_to_125(rng: random.Random) -> Dict[str, Any]:
    cases = [(1, 1), (8, 2), (27, 3), (64, 4), (125, 5)]
    c, r = rng.choice(cases)

    prompt = f"Calculate the cube root: $$\\sqrt[3]{{{c}}}$$"
    sol = (
        f"**Step 1:** Find the number that cubed gives ${c}$: ${r}^3 = {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Value: $\\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_cube_root_perfect_cubes_1_to_125",
        "hints": {
            "tier_1": f"What number multiplied by itself three times gives {c}?",
            "tier_2": f"{r} × {r} × {r} = {c}.",
            "tier_3": f"cbrt({c}) = {r}."
        }
    }


def arch_22_cube_root_perfect_cubes_216_to_1000(rng: random.Random) -> Dict[str, Any]:
    cases = [(216, 6), (343, 7), (512, 8), (729, 9), (1000, 10)]
    c, r = rng.choice(cases)

    prompt = f"Calculate the cube root: $$\\sqrt[3]{{{c}}}$$"
    sol = (
        f"**Step 1:** Since ${r}^3 = {c}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Cube root: $\\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_cube_root_perfect_cubes_216_to_1000",
        "hints": {
            "tier_1": f"Find the number that cubes to {c}.",
            "tier_2": f"{r}^3 = {c}.",
            "tier_3": f"Answer is {r}."
        }
    }


def arch_23_geometric_volume_to_edge_length_cube_root(rng: random.Random) -> Dict[str, Any]:
    edge = rng.choice([3, 4, 5, 6, 8])
    vol = edge ** 3

    prompt = (
        f"A cube-shaped packing container has an internal volume of **{vol} cm$^3$**.\n\n"
        f"Calculate the length of one internal edge of the container."
    )
    sol = (
        f"**Step 1:** Volume of cube formula: $V = s^3 \\rightarrow s = \\sqrt[3]{{V}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute edge: $s = \\sqrt[3]{{{vol}}} = \\mathbf{{{edge} \\text{{ cm}}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{edge} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_geometric_volume_to_edge_length_cube_root",
        "hints": {
            "tier_1": "The side of a cube is the cube root of its volume.",
            "tier_2": f"s = cbrt({vol}).",
            "tier_3": f"Edge length = {edge} cm."
        }
    }


def arch_24_cube_of_multiples_of_ten(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([10, 20, 30, 40])
    cube = b ** 3
    cube_s = f"{cube:,}".replace(",", " ")

    prompt = f"Calculate mentally: $${b}^3$$"
    sol = (
        f"**Step 1:** Cube the leading digit and triple the count of zeros: $({b // 10})^3 \\times 1\\ 000$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compute: ${(b // 10)**3} \\times 1\\ 000 = \\mathbf{{{cube_s}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": cube_s,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_cube_of_multiples_of_ten",
        "hints": {
            "tier_1": f"Cube {b // 10} and attach three zeros.",
            "tier_2": f"{(b // 10)**3} with 000.",
            "tier_3": f"{cube_s}."
        }
    }


def arch_25_cube_root_of_multiples_of_thousand(rng: random.Random) -> Dict[str, Any]:
    cases = [(8000, 20), (27000, 30), (64000, 40), (125000, 50)]
    c, r = rng.choice(cases)
    c_s = f"{c:,}".replace(",", " ")

    prompt = f"Calculate: $$\\sqrt[3]{{{c_s}}}$$"
    sol = (
        f"**Step 1:** Take the cube root of the leading number and divide the count of zeros by 3 [1 Mark: Method].\n\n"
        f"**Step 2:** $\\sqrt[3]{{{c_s}}} = \\mathbf{{{r}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_exp_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{r}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_cube_root_of_multiples_of_thousand",
        "hints": {
            "tier_1": f"cbrt({c // 1000}) = {r // 10}, then multiply by 10.",
            "tier_2": f"{r}^3 = {c}.",
            "tier_3": f"Answer is {r}."
        }
    }
