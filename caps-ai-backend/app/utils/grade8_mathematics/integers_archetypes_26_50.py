"""
Grade 8 Mathematics - Integers Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/02. Integers.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 3 (Cont.): Subtraction & Multi-term Chains (26 - 28)
# ==============================================================================

def arch_26_subtraction_of_negative_from_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(15, 50)
    b = rng.randint(10, 45)
    while a == b:
        b = rng.randint(10, 45)
    ans = -a + b

    prompt = (
        f"Evaluate the following integer expression step-by-step:\n\n"
        f"$$(-{a}) - (-{b})$$"
    )
    sol = (
        f"**Step 1:** Rewrite the subtraction of a negative integer as addition:\n"
        f"$$(-{a}) - (-{b}) = -{a} + {b}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: $-{a} + {b} = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_subtraction_of_negative_from_negative",
        "hints": {
            "tier_1": "Change -(-b) into +b.",
            "tier_2": f"Expression becomes -{a} + {b}.",
            "tier_3": f"-{a} + {b} = {ans}."
        },
        "misconception_tags": ["negative_minus_negative_sign_error"]
    }


def arch_27_additive_inverse_zero_sum_property(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(14, 85)
    prompt = (
        f"State the mathematical property demonstrated by the equation:\n\n"
        f"$${a} + (-{a}) = 0$$\n\n"
        f"1. Name the property.\n"
        f"2. Define what an additive inverse is."
    )
    sol = (
        f"**Step 1:** This demonstrates the **additive inverse property** [1 Mark].\n\n"
        f"**Step 2:** The additive inverse of a number is the number that, when added to it, yields a sum of zero ($0$). "
        f"For any integer $a$, its additive inverse is $-a$ [1 Mark].\n\n"
        r"$$\therefore \text{Additive inverse property; } a + (-a) = 0$$"
    )
    ans = "Additive inverse property; adding a number to its opposite gives 0"
    return {
        "id": f"g8_int_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_additive_inverse_zero_sum_property",
        "hints": {
            "tier_1": "What do we call the number that cancels out another under addition?",
            "tier_2": "The property involves adding opposites to reach 0.",
            "tier_3": "It is the Additive Inverse Property."
        },
        "misconception_tags": ["multiplicative_inverse_confusion"]
    }


def arch_28_multi_term_addition_subtraction_chain(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 25)
    b = rng.randint(10, 30)
    c = rng.randint(6, 20)
    d = rng.randint(5, 18)
    ans = -a + b + c - d

    prompt = (
        f"Simplify the following multi-term integer chain:\n\n"
        f"$$(-{a}) + {b} - (-{c}) + (-{d})$$"
    )
    sol = (
        f"**Step 1:** Simplify signs across the expression:\n"
        f"$$(-{a}) + {b} - (-{c}) + (-{d}) = -{a} + {b} + {c} - {d}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Group positive and negative terms:\n"
        f"$$\\text{{Positives}} = {b} + {c} = {b + c}$$\n"
        f"$$\\text{{Negatives}} = -{a} - {d} = -{a + d}$$\n\n"
        f"**Step 3:** Calculate final value:\n"
        f"$${b + c} - {a + d} = {ans}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_multi_term_addition_subtraction_chain",
        "hints": {
            "tier_1": "Replace -(-c) with +c and +(-d) with -d.",
            "tier_2": f"Expression becomes: -{a} + {b} + {c} - {d}.",
            "tier_3": f"Final answer is {ans}."
        },
        "misconception_tags": ["chain_addition_sign_slip"]
    }


# ==============================================================================
# CLUSTER 4: Multiplication & Division (29 - 36)
# ==============================================================================

def arch_29_multiplication_positive_by_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 12)
    b = rng.randint(3, 11)
    ans = -(a * b)

    prompt = (
        f"Calculate the product:\n\n"
        f"$${a} \\times (-{b})$$\n\n"
        f"State the sign rule that applies to multiplying a positive integer by a negative integer."
    )
    sol = (
        f"**Step 1:** The product of a positive integer and a negative integer is always negative: $(+) \\times (-) = (-)$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Multiply the absolute values and attach the negative sign:\n"
        f"$${a} \\times (-{b}) = -({a} \\times {b}) = {ans}$$ [1 Mark: Calculation].\n\n"
        f"$$\\therefore {ans}$$"
    )
    ans_text = f"{ans} (positive × negative = negative)"
    return {
        "id": f"g8_int_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_multiplication_positive_by_negative",
        "hints": {
            "tier_1": "A positive multiplied by a negative always gives a negative.",
            "tier_2": f"Multiply {a} × {b} and add a negative sign.",
            "tier_3": f"{a} × (-{b}) = {ans}."
        },
        "misconception_tags": ["pos_times_neg_positive_error"]
    }


def arch_30_multiplication_negative_by_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 13)
    b = rng.randint(3, 12)
    ans = a * b

    prompt = (
        f"Evaluate the product:\n\n"
        f"$$(-{a}) \\times (-{b})$$\n\n"
        f"Show your reasoning regarding signs."
    )
    sol = (
        f"**Step 1:** The product of two negative integers is always positive: $(-) \\times (-) = (+)$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Multiply the absolute values:\n"
        f"$$(-{a}) \\times (-{b}) = +({a} \\times {b}) = {ans}$$ [1 Mark: Calculation].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_multiplication_negative_by_negative",
        "hints": {
            "tier_1": "A negative multiplied by a negative always gives a positive.",
            "tier_2": f"Calculate {a} × {b}.",
            "tier_3": f"(-{a}) × (-{b}) = {ans}."
        },
        "misconception_tags": ["neg_times_neg_negative_error"]
    }


def arch_31_product_of_three_signed_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(2, 5)
    c = rng.randint(2, 6)
    ans = -(a * b * c)

    prompt = (
        f"Determine the value of:\n\n"
        f"$$(-{a}) \\times (-{b}) \\times (-{c})$$\n\n"
        f"Show each step of multiplication."
    )
    step1 = a * b
    sol = (
        f"**Step 1:** Multiply the first two factors:\n"
        f"$$(-{a}) \\times (-{b}) = +{step1}$$ [1 Mark]\n\n"
        f"**Step 2:** Multiply the result by the third factor:\n"
        f"$$(+{step1}) \\times (-{c}) = -({step1} \\times {c}) = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_product_of_three_signed_integers",
        "hints": {
            "tier_1": "An odd number of negative factors (3) results in a negative product.",
            "tier_2": f"(-{a}) × (-{b}) = {step1}. Then {step1} × (-{c}).",
            "tier_3": f"Final answer is {ans}."
        },
        "misconception_tags": ["odd_count_negative_sign_error"]
    }


def arch_32_product_of_four_signed_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 4)
    c = rng.randint(2, 4)
    d = rng.randint(2, 4)
    ans = a * b * c * d

    prompt = (
        f"Evaluate the four-factor product:\n\n"
        f"$$(-{a}) \\times (-{b}) \\times (-{c}) \\times (-{d})$$"
    )
    p1 = a * b
    p2 = c * d
    sol = (
        f"**Step 1:** An even count of negative factors (4 negatives) produces a **positive** product [1 Mark: Rule].\n\n"
        f"**Step 2:** Pairwise multiplication:\n"
        f"$$[(-{a}) \\times (-{b})] \\times [(-{c}) \\times (-{d})] = ({p1}) \\times ({p2}) = {ans}$$ [1 Mark: Calculation]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_product_of_four_signed_integers",
        "hints": {
            "tier_1": "Count the negative signs. An even number (4) gives a positive answer.",
            "tier_2": f"Calculate ({a} × {b}) × ({c} × {d}).",
            "tier_3": f"{p1} × {p2} = {ans}."
        },
        "misconception_tags": ["even_count_negative_sign_error"]
    }


def arch_33_division_negative_by_positive(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(3, 9)
    quot = rng.randint(4, 12)
    a = b * quot
    ans = -quot

    prompt = (
        f"Calculate the quotient:\n\n"
        f"$$(-{a}) \\div {b}$$\n\n"
        f"Explain how the sign of the quotient is determined."
    )
    sol = (
        f"**Step 1:** Dividing a negative integer by a positive integer yields a negative quotient: $(-) \\div (+) = (-)$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Divide absolute values:\n"
        f"$$\\frac{{-{a}}}{{{b}}} = -\\left(\\frac{{{a}}}{{{b}}}\\right) = {ans}$$ [1 Mark: Calculation]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_division_negative_by_positive",
        "hints": {
            "tier_1": "Negative divided by positive equals negative.",
            "tier_2": f"Calculate {a} / {b} and add a negative sign.",
            "tier_3": f"-{a} ÷ {b} = {ans}."
        },
        "misconception_tags": ["division_negative_sign_error"]
    }


def arch_34_division_positive_by_negative(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(3, 8)
    quot = rng.randint(4, 11)
    a = b * quot
    ans = -quot

    prompt = (
        f"Determine the value of:\n\n"
        f"$${a} \\div (-{b})$$"
    )
    sol = (
        f"**Step 1:** Positive divided by negative yields a negative quotient: $(+) \\div (-) = (-)$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Calculate: $\\frac{{{a}}}{{-{b}}} = {ans}$ [1 Mark: Accuracy].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_division_positive_by_negative",
        "hints": {
            "tier_1": "Positive divided by negative equals negative.",
            "tier_2": f"{a} ÷ {b} = {quot}, so with the negative sign it is -{quot}.",
            "tier_3": f"{a} ÷ (-{b}) = {ans}."
        },
        "misconception_tags": ["pos_div_neg_positive_error"]
    }


def arch_35_division_negative_by_negative(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(3, 9)
    quot = rng.randint(4, 12)
    a = b * quot
    ans = quot

    prompt = (
        f"Evaluate the division problem:\n\n"
        f"$$(-{a}) \\div (-{b})$$\n\n"
        f"Show your reasoning regarding signs."
    )
    sol = (
        f"**Step 1:** The quotient of two negative integers is always positive: $(-) \\div (-) = (+)$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Calculate: $\\frac{{-{a}}}{{-{b}}} = +\\left(\\frac{{{a}}}{{{b}}}\\right) = {ans}$ [1 Mark: Calculation].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_division_negative_by_negative",
        "hints": {
            "tier_1": "Negative divided by negative always produces a positive result.",
            "tier_2": f"Calculate {a} ÷ {b}.",
            "tier_3": f"(-{a}) ÷ (-{b}) = {ans}."
        },
        "misconception_tags": ["neg_div_neg_negative_error"]
    }


def arch_36_combined_multiplication_and_division(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 6)
    k = rng.randint(2, 5)
    b = rng.randint(3, 7)
    a = c * k
    # ((-a) * b) / (-c) = (-a * b) / -c = (a * b) / c = k * b
    ans = k * b

    prompt = (
        f"Calculate the value of the rational integer expression:\n\n"
        f"$$\\frac{{(-{a}) \\times {b}}}{{-{c}}}$$\n\n"
        f"Show all steps in order."
    )
    num = -(a * b)
    sol = (
        f"**Step 1:** Multiply the numerator:\n"
        f"$$(-{a}) \\times {b} = {num}$$ [1 Mark]\n\n"
        f"**Step 2:** Divide by the denominator:\n"
        f"$$\\frac{{{num}}}{{-{c}}} = +\\left(\\frac{{{abs(num)}}}{{{c}}}\\right) = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_combined_multiplication_and_division",
        "hints": {
            "tier_1": "Evaluate the numerator first, then divide by the denominator.",
            "tier_2": f"(-{a}) × {b} = {num}. Then divide {num} by -{c}.",
            "tier_3": f"{num} ÷ (-{c}) = {ans}."
        },
        "misconception_tags": ["fraction_sign_cancellation_error"]
    }


# ==============================================================================
# CLUSTER 5: Exponents, Roots & Powers with Negative Bases (37 - 44)
# ==============================================================================

def arch_37_square_of_negative_integer_in_parentheses(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 12)
    ans = a ** 2

    prompt = (
        f"Evaluate the power expression:\n\n"
        f"$$(-{a})^2$$\n\n"
        f"Explain why the resulting value is positive."
    )
    sol = (
        f"**Step 1:** The base of the exponent is the entire integer inside brackets: $(-{a})$.\n"
        f"$$(-{a})^2 = (-{a}) \\times (-{a})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Multiplying two negative numbers yields a positive product:\n"
        f"$$(-{a}) \\times (-{a}) = +{ans}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_square_of_negative_integer_in_parentheses",
        "hints": {
            "tier_1": "(-a)² means (-a) multiplied by (-a).",
            "tier_2": "A negative times a negative equals a positive.",
            "tier_3": f"(-{a})² = {ans}."
        },
        "misconception_tags": ["bracketed_negative_square_negative_error"]
    }


def arch_38_square_of_negative_integer_without_parentheses(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 12)
    ans = -(a ** 2)

    prompt = (
        f"Evaluate the power expression:\n\n"
        f"$$-{a}^2$$\n\n"
        f"Clearly explain the difference in meaning between $$-{a}^2$$ and $$(-{a})^2$$."
    )
    sol = (
        f"**Step 1:** Without brackets, the exponent $2$ applies only to the base ${a}$, not to the negative sign.\n"
        f"$$-{a}^2 = -({a} \\times {a}) = -({a ** 2}) = {ans}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Difference: $(-{a})^2 = +{a ** 2}$ has base $-{a}$, while $-{a}^2 = -{a ** 2}$ is the additive inverse of ${a}^2$ [1 Mark: Explanation].\n\n"
        f"$$\\therefore -{a}^2 = {ans}$$"
    )
    return {
        "id": f"g8_int_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_square_of_negative_integer_without_parentheses",
        "hints": {
            "tier_1": "Without brackets, the power applies only to the number, not the minus sign.",
            "tier_2": f"Calculate {a}² first, then put a negative sign in front.",
            "tier_3": f"-{a}² = -{a ** 2} = {ans}."
        },
        "misconception_tags": ["unbracketed_power_sign_error"]
    }


def arch_39_cube_of_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    ans = -(a ** 3)

    prompt = (
        f"Calculate the value of the cube:\n\n"
        f"$$(-{a})^3$$\n\n"
        f"State whether an odd power of a negative base is always positive or negative."
    )
    sol = (
        f"**Step 1:** Expand the power:\n"
        f"$$(-{a})^3 = (-{a}) \\times (-{a}) \\times (-{a}) = (+{a ** 2}) \\times (-{a})$$ [1 Mark: Method]\n\n"
        f"**Step 2:** An odd power of a negative base is always **negative**:\n"
        f"$$(+{a ** 2}) \\times (-{a}) = {ans}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans} \\text{{ (Always negative)}}$$"
    )
    return {
        "id": f"g8_int_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_cube_of_negative_integer",
        "hints": {
            "tier_1": "(-a)³ = (-a) × (-a) × (-a).",
            "tier_2": "An odd power of a negative number stays negative.",
            "tier_3": f"(-{a})³ = {ans}."
        },
        "misconception_tags": ["negative_cube_positive_error"]
    }


def arch_40_fourth_power_of_negative_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    ans = a ** 4

    prompt = (
        f"Evaluate the fourth power:\n\n"
        f"$$(-{a})^4$$"
    )
    sol = (
        f"**Step 1:** Any even power of a negative base results in a positive integer:\n"
        f"$$(-{a})^4 = [(-{a})^2]^2 = ({a ** 2})^2$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Calculate: ${a ** 2} \\times {a ** 2} = {ans}$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_fourth_power_of_negative_integer",
        "hints": {
            "tier_1": "Even powers of negative numbers are always positive.",
            "tier_2": f"Calculate {a}⁴.",
            "tier_3": f"(-{a})⁴ = {ans}."
        },
        "misconception_tags": ["even_power_negative_sign_error"]
    }


def arch_41_cube_root_of_negative_integer(rng: random.Random) -> Dict[str, Any]:
    root = rng.randint(2, 6)
    val = -(root ** 3)
    ans = -root

    prompt = (
        f"Determine the value of the cube root:\n\n"
        f"$$\\sqrt[3]{{{val}}}$$\n\n"
        f"Explain why this real root exists, unlike $\\sqrt{{{val}}}$."
    )
    sol = (
        f"**Step 1:** The cube root seeks a number $x$ such that $x^3 = {val}$.\n"
        f"Because $({ans})^3 = ({ans}) \\times ({ans}) \\times ({ans}) = {val}$, $\\sqrt[3]{{{val}}} = {ans}$ [1 Mark: Calculation].\n\n"
        f"**Step 2:** An odd root of a negative number is a valid real number because an odd power of a negative is negative. "
        f"Even roots (like square roots) of negative numbers are non-real in $\\mathbb{{R}}$ [1 Mark: Explanation].\n\n"
        f"$$\\therefore \\sqrt[3]{{{val}}} = {ans}$$"
    )
    return {
        "id": f"g8_int_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_cube_root_of_negative_integer",
        "hints": {
            "tier_1": "What number multiplied by itself three times gives this negative value?",
            "tier_2": f"Find root: (-{root})³ = {val}.",
            "tier_3": f"Cube root of {val} is {ans}."
        },
        "misconception_tags": ["cube_root_negative_non_real_misbelief"]
    }


def arch_42_square_root_of_negative_non_real_drill(rng: random.Random) -> Dict[str, Any]:
    val = -rng.choice([16, 25, 36, 49, 64, 81, 100])

    prompt = (
        f"Consider the square root expression:\n\n"
        f"$$\\sqrt{{{val}}}$$\n\n"
        f"1. State whether this expression produces a real number ($\\in \\mathbb{{R}}$) or a non-real number ($\\notin \\mathbb{{R}}$).\n"
        f"2. Provide a rigorous mathematical reason for your answer."
    )
    sol = (
        f"**Step 1:** $\\sqrt{{{val}}}$ is **non-real** (or undefined in $\\mathbb{{R}}$) [1 Mark].\n\n"
        f"**Step 2:** Reason: The square of any real number (whether positive, zero, or negative) is always non-negative ($x^2 \\ge 0$). "
        f"There is no real number $x$ such that $x^2 = {val}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Non-real (no real number squared equals a negative number)}}$$"
    )
    ans = "Non-real; the square of any real number is always non-negative"
    return {
        "id": f"g8_int_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_square_root_of_negative_non_real_drill",
        "hints": {
            "tier_1": "Can the square of any real number ever be negative?",
            "tier_2": "Since (-x)² is positive and (+x)² is positive, no real square root of a negative exists.",
            "tier_3": "The answer is Non-real."
        },
        "misconception_tags": ["square_root_negative_real_error"]
    }


def arch_43_sum_of_squares_and_cubes_with_negative_bases(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 4)
    term1 = a ** 2  # (-a)^2 = a^2
    term2 = -(b ** 3)  # (-b)^3 = -b^3
    ans = term1 + term2

    prompt = (
        f"Evaluate the mixed power expression:\n\n"
        f"$$(-{a})^2 + (-{b})^3$$\n\n"
        f"Show intermediate calculations for both powers."
    )
    sol = (
        f"**Step 1:** Evaluate the square: $(-{a})^2 = +{term1}$ [1 Mark].\n\n"
        f"**Step 2:** Evaluate the cube: $(-{b})^3 = {term2}$ [1 Mark].\n\n"
        f"**Step 3:** Sum the results: ${term1} + ({term2}) = {term1} - {b ** 3} = {ans}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "43_sum_of_squares_and_cubes_with_negative_bases",
        "hints": {
            "tier_1": "Evaluate (-a)² first, then (-b)³, then add.",
            "tier_2": f"(-{a})² = {term1} and (-{b})³ = {term2}.",
            "tier_3": f"{term1} + ({term2}) = {ans}."
        },
        "misconception_tags": ["mixed_powers_signs_confusion"]
    }


def arch_44_difference_of_powers_with_negative_bases(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 4)
    b = rng.randint(2, 5)
    term1 = -(a ** 3)  # (-a)^3
    term2 = b ** 2  # (-b)^2
    ans = term1 - term2

    prompt = (
        f"Calculate the difference between the two powers:\n\n"
        f"$$(-{a})^3 - (-{b})^2$$\n\n"
        f"Show all steps clearly."
    )
    sol = (
        f"**Step 1:** Evaluate the first power: $(-{a})^3 = {term1}$ [1 Mark].\n\n"
        f"**Step 2:** Evaluate the second power: $(-{b})^2 = +{term2}$ [1 Mark].\n\n"
        f"**Step 3:** Subtract: ${term1} - (+{term2}) = {term1} - {term2} = {ans}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "44_difference_of_powers_with_negative_bases",
        "hints": {
            "tier_1": "Evaluate each power separately before subtracting.",
            "tier_2": f"(-{a})³ = {term1} and (-{b})² = {term2}.",
            "tier_3": f"{term1} - {term2} = {ans}."
        },
        "misconception_tags": ["power_difference_double_sign_error"]
    }


# ==============================================================================
# CLUSTER 6: Multi-Step BODMAS, Properties & Equations (45 - 50)
# ==============================================================================

def arch_45_bodmas_with_brackets_and_powers(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(2, 5)
    a = rng.randint(2, 5) * rng.choice([-1, 1])
    c = rng.randint(3, 7) * rng.choice([-1, 1])
    d = rng.randint(2, 4)
    e = rng.randint(2, 5)

    p_term = (-b) ** 2
    m_term = a * c
    d_term = -d * e
    ans = p_term - m_term + d_term

    prompt = (
        f"Evaluate the integer expression step-by-step applying the order of operations (BODMAS):\n\n"
        f"$$(-{b})^2 - ({a})({c}) + (-{d})({e})$$\n\n"
        f"1. Evaluate the power: $$(-{b})^2$$\n"
        f"2. Evaluate both products: $$({a})({c})$$ and $$(-{d})({e})$$\n"
        f"3. Combine all terms to find the final simplified integer."
    )
    sol = (
        f"**Step 1:** Exponents: $(-{b})^2 = {p_term}$ [1 Mark].\n\n"
        f"**Step 2:** Multiplication: $({a})({c}) = {m_term}$ and $(-{d})({e}) = {d_term}$ [1 Mark].\n\n"
        f"**Step 3:** Substitute and simplify: ${p_term} - ({m_term}) + ({d_term}) = {ans}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "45_bodmas_with_brackets_and_powers",
        "hints": {
            "tier_1": "BODMAS: Powers first, then multiplication, then addition/subtraction.",
            "tier_2": f"(-{b})² = {p_term}, ({a})({c}) = {m_term}, (-{d})({e}) = {d_term}.",
            "tier_3": f"{p_term} - ({m_term}) + ({d_term}) = {ans}."
        },
        "misconception_tags": ["bodmas_precedence_violation"]
    }


def arch_46_bodmas_nested_brackets_and_fractions(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(2, 4)
    k = rng.randint(3, 8)
    num_target = d * k
    b = rng.randint(2, 4)
    c = rng.randint(3, 5)
    prod = b * c
    a = -(num_target - prod)
    # (-a) + (-b)(-c) = -a + bc = num_target. Then / (-d) = -k
    ans = -k

    prompt = (
        f"Evaluate the fractional integer expression:\n\n"
        f"$$\\frac{{({a}) + (-{b})(-{c})}}{{-{d}}}$$"
    )
    sol = (
        f"**Step 1:** Evaluate the multiplication in the numerator:\n"
        f"$$(-{b})(-{c}) = +{prod}$$ [1 Mark]\n\n"
        f"**Step 2:** Add the terms in the numerator:\n"
        f"$${a} + {prod} = {num_target}$$ [1 Mark]\n\n"
        f"**Step 3:** Divide by the denominator:\n"
        f"$$\\frac{{{num_target}}}{{-{d}}} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_int_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "46_bodmas_nested_brackets_and_fractions",
        "hints": {
            "tier_1": "Simplify the entire numerator before dividing by the denominator.",
            "tier_2": f"Numerator: {a} + ({prod}) = {num_target}.",
            "tier_3": f"{num_target} ÷ (-{d}) = {ans}."
        },
        "misconception_tags": ["fraction_bar_division_precedence_error"]
    }


def arch_47_distributive_property_over_negative_addition(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(2, 6)
    b = rng.randint(4, 9)
    c = -rng.randint(3, 8)
    ans = a * (b + c)

    prompt = (
        f"Apply the **distributive property** to expand and evaluate the expression:\n\n"
        f"$${a} \\times ({b} + ({c}))$$\n\n"
        f"1. Write out the expanded expression showing the distribution of ${a}$.\n"
        f"2. Evaluate to find the final integer."
    )
    term1 = a * b
    term2 = a * c
    sol = (
        f"**Step 1:** Distribute ${a}$ to each term inside brackets:\n"
        f"$${a}({b}) + ({a})({c}) = ({term1}) + ({term2})$$ [1 Mark: Expansion]\n\n"
        f"**Step 2:** Sum the products:\n"
        f"$${term1} + {term2} = {ans}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {ans}$$"
    )
    ans_text = f"1. ({term1}) + ({term2}); 2. {ans}"
    return {
        "id": f"g8_int_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_text,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_distributive_property_over_negative_addition",
        "hints": {
            "tier_1": "Multiply the outside factor by each term inside the brackets.",
            "tier_2": f"({a}) × ({b}) = {term1} and ({a}) × ({c}) = {term2}.",
            "tier_3": f"{term1} + {term2} = {ans}."
        },
        "misconception_tags": ["distributive_sign_multiplication_error"]
    }


def arch_48_solving_one_step_equation_with_negative_integers(rng: random.Random) -> Dict[str, Any]:
    eq_type = rng.choice(["add", "mult"])
    if eq_type == "add":
        a = rng.randint(5, 20)
        target = -rng.randint(10, 30)
        ans = target - a
        prompt = f"Solve for $x$:\n\n$$x + {a} = {target}$$"
        sol = (
            f"**Step 1:** Subtract ${a}$ from both sides:\n"
            f"$$x = {target} - {a}$$ [1 Mark]\n\n"
            f"**Step 2:** Calculate: $x = {ans}$ [1 Mark]\n\n"
            f"$$\\therefore x = {ans}$$"
        )
    else:
        a = -rng.randint(2, 7)
        ans = rng.randint(4, 12) * rng.choice([-1, 1])
        prod = a * ans
        prompt = f"Solve for $x$:\n\n$${a}x = {prod}$$"
        sol = (
            f"**Step 1:** Divide both sides by ${a}$:\n"
            f"$$x = \\frac{{{prod}}}{{{a}}}$$ [1 Mark]\n\n"
            f"**Step 2:** Calculate: $x = {ans}$ [1 Mark]\n\n"
            f"$$\\therefore x = {ans}$$"
        )

    return {
        "id": f"g8_int_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_solving_one_step_equation_with_negative_integers",
        "hints": {
            "tier_1": "Use the inverse operation to isolate x.",
            "tier_2": "Remember to apply the sign rules when dividing or subtracting.",
            "tier_3": f"x = {ans}."
        },
        "misconception_tags": ["equation_inverse_operation_sign_error"]
    }


def arch_49_solving_two_step_equation_with_negative_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6) * rng.choice([-1, 1])
    ans = -rng.randint(2, 9)
    b = rng.randint(4, 18)
    rhs = a * ans + b

    prompt = (
        f"Solve for $x$ showing all algebraic steps:\n\n"
        f"$${a}x + {b} = {rhs}$$"
    )
    rhs_sub = rhs - b
    sol = (
        f"**Step 1:** Subtract ${b}$ from both sides:\n"
        f"$${a}x = {rhs} - {b} = {rhs_sub}$$ [1 Mark: Method]\n\n"
        f"**Step 2:** Divide both sides by ${a}$:\n"
        f"$$x = \\frac{{{rhs_sub}}}{{{a}}} = {ans}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore x = {ans}$$"
    )
    return {
        "id": f"g8_int_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_solving_two_step_equation_with_negative_integers",
        "hints": {
            "tier_1": "Subtract the constant term first, then divide by the coefficient of x.",
            "tier_2": f"{a}x = {rhs_sub}.",
            "tier_3": f"x = {rhs_sub} ÷ ({a}) = {ans}."
        },
        "misconception_tags": ["two_step_equation_transposition_error"]
    }


def arch_50_two_step_equation_with_brackets_and_negatives(rng: random.Random) -> Dict[str, Any]:
    a = -rng.randint(2, 5)
    b = rng.randint(2, 7)
    ans = -rng.randint(1, 8)
    rhs = a * (ans - b)

    prompt = (
        f"Solve for $x$ in the equation:\n\n"
        f"$${a}(x - {b}) = {rhs}$$\n\n"
        f"Show all working steps."
    )
    div_step = rhs // a
    sol = (
        f"**Step 1:** Divide both sides by ${a}$ (or expand brackets):\n"
        f"$$x - {b} = \\frac{{{rhs}}}{{{a}}} = {div_step}$$ [1 Mark]\n\n"
        f"**Step 2:** Add ${b}$ to both sides:\n"
        f"$$x = {div_step} + {b} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore x = {ans}$$"
    )
    return {
        "id": f"g8_int_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_two_step_equation_with_brackets_and_negatives",
        "hints": {
            "tier_1": "Either divide both sides by the outside factor, or expand the brackets first.",
            "tier_2": f"x - {b} = {div_step}.",
            "tier_3": f"x = {ans}."
        },
        "misconception_tags": ["bracket_equation_sign_distribution_error"]
    }
