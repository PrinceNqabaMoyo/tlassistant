"""Grade 9 Mathematics - Common Fractions Generator.
Grounded in:
  - curriculum_docs/Mathematics_Gr9/Fractions Studio.md (Equivalent fractions, operations, powers & roots)
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Fractions.md (Chapter 6: Fractions, measuring with units, percentage conversions)

Subskills:
  1. fractions_equivalent_and_simplification: Simplifying fractions, mixed numbers.
  2. fractions_addition_subtraction: Operations with LCD and mixed numbers.
  3. fractions_multiplication_division: Multiplying and dividing fractions with cross-cancellation.
  4. fractions_powers_and_roots: Squares, cubes, square roots, and cube roots of common fractions.
  5. fractions_word_problems_percentages: Fraction of quantities, percentage increase/decrease.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import make_id, rng


SUBSKILLS = [
    "fractions_equivalent_and_simplification",
    "fractions_addition_subtraction",
    "fractions_multiplication_division",
    "fractions_powers_and_roots",
    "fractions_word_problems_percentages",
]


def _gen_equivalent_simplification(r: random.Random) -> Dict[str, Any]:
    # Simplify fraction or convert improper to mixed
    kind = r.choice(["simplify", "improper_to_mixed"])
    if kind == "simplify":
        common = r.choice([3, 4, 6, 8, 12])
        num_simp = r.choice([2, 3, 5, 7])
        den_simp = r.choice([7, 9, 11, 13])
        while math.gcd(num_simp, den_simp) != 1:
            den_simp += 2
            
        num = num_simp * common
        den = den_simp * common
        ans = f"{num_simp}/{den_simp}"

        prompt = f"Simplify the following common fraction to its simplest lowest terms:\n$$\\frac{{{num}}}{{{den}}}$$"
        derivation = (
            f"**Step 1: Find the Highest Common Factor (HCF) of numerator and denominator.**\n"
            f"$$\\text{{HCF}}({num}, {den}) = {common}$$\n\n"
            f"**Step 2: Divide numerator and denominator by {common}.**\n"
            f"$$\\frac{{{num} \\div {common}}}{{{den} \\div {common}}} = \\frac{{{num_simp}}}{{{den_simp}}}$$"
        )
    else:
        den = r.choice([3, 4, 5, 6, 7, 8])
        whole = r.randint(2, 6)
        rem = r.randint(1, den - 1)
        while math.gcd(rem, den) != 1:
            rem = (rem % (den - 1)) + 1
        num = whole * den + rem
        ans = f"{whole} {rem}/{den}"

        prompt = f"Convert the improper fraction $$\\frac{{{num}}}{{{den}}}$$ to a mixed number in simplest form (e.g. `2 3/4`)."
        derivation = (
            f"**Step 1: Divide numerator by denominator.**\n"
            f"$${num} \\div {den} = {whole} \\text{{ with remainder }} {rem}$$\n\n"
            f"**Step 2: Write as a mixed number.**\n"
            f"$$= {whole}\\frac{{{rem}}}{{{den}}}$$"
        )

    return {
        "id": make_id("g9_fraceq"),
        "topic": "Fractions",
        "subskill": "fractions_equivalent_and_simplification",
        "difficulty": "easy",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Divide by the Highest Common Factor to simplify.",
            "To convert to mixed number, divide numerator by denominator and keep the remainder over denominator.",
            f"Answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_addition_subtraction(r: random.Random) -> Dict[str, Any]:
    # a/b ± c/d with different denominators
    b = r.choice([3, 4, 6, 8])
    d = r.choice([2, 5, 6, 9])
    while b == d:
        d = r.choice([2, 5, 7, 10])
        
    lcd = (b * d) // math.gcd(b, d)
    a = r.randint(1, b - 1)
    c = r.randint(1, d - 1)
    
    op = r.choice(["+", "-"])
    if op == "-":
        # ensure positive result
        if a / b < c / d:
            a, b, c, d = c, d, a, b
            lcd = (b * d) // math.gcd(b, d)
        num_res = (a * (lcd // b)) - (c * (lcd // d))
    else:
        num_res = (a * (lcd // b)) + (c * (lcd // d))
        
    g = math.gcd(num_res, lcd)
    final_num = num_res // g
    final_den = lcd // g
    ans = f"{final_num}/{final_den}" if final_den != 1 else str(final_num)

    prompt = f"Calculate the exact value of the following fraction calculation:\n$$\\frac{{{a}}}{{{b}}} {op} \\frac{{{c}}}{{{d}}}$$"

    derivation = (
        f"**Step 1: Find the Lowest Common Denominator (LCD).**\n"
        f"$$\\text{{LCD}}({b}, {d}) = {lcd}$$\n\n"
        f"**Step 2: Convert fractions to equivalent fractions with denominator {lcd}.**\n"
        f"$$\\frac{{{a} \\times {lcd//b}}}{{{b} \\times {lcd//b}}} = \\frac{{{a * (lcd//b)}}}{{{lcd}}}, \\quad \\frac{{{c} \\times {lcd//d}}}{{{d} \\times {lcd//d}}} = \\frac{{{c * (lcd//d)}}}{{{lcd}}}$$\n\n"
        f"**Step 3: Combine numerators over the common denominator.**\n"
        f"$$\\frac{{{a * (lcd//b)} {op} {c * (lcd//d)}}}{{{lcd}}} = \\frac{{{num_res}}}{{{lcd}}}$$\n\n"
        f"**Step 4: Simplify to lowest terms.**\n"
        f"$$= \\frac{{{final_num}}}{{{final_den}}} = {ans}$$"
    )

    return {
        "id": make_id("g9_fracaddsub"),
        "topic": "Fractions",
        "subskill": "fractions_addition_subtraction",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Find the LCD of {b} and {d}: LCD = {lcd}.",
            f"Rewrite each fraction with denominator {lcd} and combine the numerators.",
            f"Simplified answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_multiplication_division(r: random.Random) -> Dict[str, Any]:
    n1, d1 = r.choice([2, 3, 4, 5]), r.choice([3, 5, 7, 9])
    n2, d2 = r.choice([3, 4, 7, 8]), r.choice([2, 4, 6, 8])
    while n1 == d1: n1 += 1
    while n2 == d2: n2 += 1
    
    op = r.choice(["*", "/"])
    if op == "*":
        ans_num = n1 * n2
        ans_den = d1 * d2
        g = math.gcd(ans_num, ans_den)
        ans = f"{ans_num // g}/{ans_den // g}"
        prompt = f"Calculate the following product of fractions in simplest form:\n$$\\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}}$$"
        derivation = (
            f"**Step 1: Multiply numerators and denominators.**\n"
            f"$$\\frac{{{n1} \\times {n2}}}{{{d1} \\times {d2}}} = \\frac{{{ans_num}}}{{{ans_den}}}$$\n\n"
            f"**Step 2: Simplify by dividing by HCF ({g}).**\n"
            f"$$= {ans}$$"
        )
    else:
        # n1/d1 ÷ n2/d2 = n1/d1 * d2/n2
        ans_num = n1 * d2
        ans_den = d1 * n2
        g = math.gcd(ans_num, ans_den)
        ans = f"{ans_num // g}/{ans_den // g}"
        prompt = f"Calculate the following division of fractions in simplest form:\n$$\\frac{{{n1}}}{{{d1}}} \\div \\frac{{{n2}}}{{{d2}}}$$"
        derivation = (
            f"**Step 1: Multiply by the reciprocal of the divisor.**\n"
            f"$$= \\frac{{{n1}}}{{{d1}}} \\times \\frac{{{d2}}}{{{n2}}}$$\n\n"
            f"**Step 2: Multiply and simplify.**\n"
            f"$$= \\frac{{{n1 * d2}}}{{{d1 * n2}}} = {ans}$$"
        )

    return {
        "id": make_id("g9_fracmuldiv"),
        "topic": "Fractions",
        "subskill": "fractions_multiplication_division",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "For multiplication: multiply straight across (numerator * numerator, denominator * denominator).",
            "For division: invert the second fraction and multiply (reciprocal).",
            f"The simplified answer is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_powers_and_roots(r: random.Random) -> Dict[str, Any]:
    kind = r.choice(["square", "sqrt", "cuberoot", "mixed_sqrt"])
    if kind == "square":
        n, d = r.choice([(2, 3), (3, 4), (2, 5), (4, 5)])
        ans = f"{n**2}/{d**2}"
        prompt = f"Evaluate the square of the fraction:\n$$\\left(\\frac{{{n}}}{{{d}}}\\right)^2$$"
        derivation = f"$$\\left(\\frac{{{n}}}{{{d}}}\\right)^2 = \\frac{{{n}^2}}{{{d}^2}} = \\frac{{{n**2}}}{{{d**2}}}$$"
    elif kind == "sqrt":
        n, d = r.choice([(3, 4), (5, 6), (7, 8), (4, 9), (6, 7)])
        ans = f"{n}/{d}"
        prompt = f"Calculate the square root of the fraction:\n$$\\sqrt{{\\frac{{{n**2}}}{{{d**2}}}}}$$"
        derivation = f"$$\\sqrt{{\\frac{{{n**2}}}{{{d**2}}}}} = \\frac{{\\sqrt{{{n**2}}}}}{{\\sqrt{{{d**2}}}}} = \\frac{{{n}}}{{{d}}}$$"
    elif kind == "cuberoot":
        n, d = r.choice([(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)])
        ans = f"{n}/{d}"
        prompt = f"Calculate the cube root of the fraction:\n$$\\sqrt[3]{{\\frac{{{n**3}}}{{{d**3}}}}}$$"
        derivation = f"$$\\sqrt[3]{{\\frac{{{n**3}}}{{{d**3}}}}} = \\frac{{\\sqrt[3]{{{n**3}}}}}{{\\sqrt[3]{{{d**3}}}}} = \\frac{{{n}}}{{{d}}}$$"
    else:
        # e.g., sqrt(1 9/16) = sqrt(25/16) = 5/4
        whole, rem, den = 1, 9, 16
        improper_num = whole * den + rem  # 25
        ans = "5/4"
        prompt = f"Calculate the square root of the mixed number:\n$$\\sqrt{{1\\frac{{9}}{{16}}}}$$ (express as a simple fraction)"
        derivation = (
            f"**Step 1: Convert mixed number to an improper fraction.**\n"
            f"$$1\\frac{{9}}{{16}} = \\frac{{(1 \\times 16) + 9}}{{16}} = \\frac{{25}}{{16}}$$\n\n"
            f"**Step 2: Take square root of numerator and denominator.**\n"
            f"$$\\sqrt{{\\frac{{25}}{{16}}}} = \\frac{{\\sqrt{{25}}}}{{\\sqrt{{16}}}} = \\frac{{5}}{{4}}$$"
        )

    return {
        "id": make_id("g9_fracpwr"),
        "topic": "Fractions",
        "subskill": "fractions_powers_and_roots",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Apply the power or root to numerator and denominator separately: (a/b)^n = a^n / b^n.",
            "For mixed numbers inside roots, convert to an improper fraction first.",
            f"Answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_word_problems(r: random.Random) -> Dict[str, Any]:
    kind = r.choice(["fraction_of_quantity", "percentage_increase"])
    if kind == "fraction_of_quantity":
        denom = r.choice([4, 5, 6, 8])
        numer = r.randint(2, denom - 1)
        unit_val = r.choice([25, 40, 50, 75, 120])
        total = denom * unit_val
        val = numer * unit_val
        ans = str(val)

        prompt = (
            f"A school library has {total} books. If $$\\frac{{{numer}}}{{{denom}}}$$ of the books "
            f"are non-fiction, how many non-fiction books does the library have?"
        )
        derivation = (
            f"**Step 1: Multiply fraction by total quantity.**\n"
            f"$$\\text{{Non-fiction books}} = \\frac{{{numer}}}{{{denom}}} \\times {total}$$\n"
            f"$$= {numer} \\times \\left(\\frac{{{total}}}{{{denom}}}\\right) = {numer} \\times {unit_val} = {ans}$$"
        )
    else:
        orig = r.choice([150, 240, 400, 600, 800])
        pct = r.choice([10, 15, 20, 25])
        increase = (orig * pct) // 100
        new_val = orig + increase
        ans = str(new_val)

        prompt = (
            f"The price of a school sports uniform was R{orig}. "
            f"If the price increases by **{pct}%**, calculate the **new price** in Rands."
        )
        derivation = (
            f"**Step 1: Calculate amount of increase.**\n"
            f"$$\\text{{Increase}} = {pct}\\% \\times \\text{{R}}{orig} = \\frac{{{pct}}}{{100}} \\times {orig} = \\text{{R}}{increase}$$\n\n"
            f"**Step 2: Add increase to original price.**\n"
            f"$$\\text{{New price}} = \\text{{R}}{orig} + \\text{{R}}{increase} = \\text{{R}}{ans}$$"
        )

    return {
        "id": make_id("g9_fracword"),
        "topic": "Fractions",
        "subskill": "fractions_word_problems_percentages",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Multiply the fraction by the total quantity.",
            "For percentage increase: find the percentage increase amount and add it to the original.",
            f"Calculated answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


GENERATORS = {
    "fractions_equivalent_and_simplification": _gen_equivalent_simplification,
    "fractions_addition_subtraction": _gen_addition_subtraction,
    "fractions_multiplication_division": _gen_multiplication_division,
    "fractions_powers_and_roots": _gen_powers_and_roots,
    "fractions_word_problems_percentages": _gen_word_problems,
}


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    r = rng(seed)
    results: List[Dict[str, Any]] = []

    if subskill in GENERATORS:
        for _ in range(count):
            results.append(GENERATORS[subskill](r))
        return results

    keys = list(GENERATORS.keys())
    for i in range(count):
        chosen = keys[(i + r.randint(0, len(keys) - 1)) % len(keys)]
        results.append(GENERATORS[chosen](r))

    return results


def generate_grade9_fractions_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res[0] if res else {}
