"""Grade 9 Mathematics - Algebraic Expressions 1 (Language, Expansion & Simplification).
Grounded in:
  - curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md (Grade 8 to 9 leap: binomial products, squares of binomials, division)
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 1.md (Chapter 13: Constants, variables, like terms, FOIL)

Subskills:
  1. expressions_language_and_substitution: Degree, coefficients, constant term, substitution.
  2. expressions_add_sub_like_terms: Adding and subtracting polynomials with like terms.
  3. expressions_distributive_monomial: Multiplying monomial by polynomial.
  4. expressions_binomial_product: Binomial x binomial expansion using FOIL.
  5. expressions_square_of_binomial: Squaring binomials (ax ± b)^2.
  6. expressions_divide_by_monomial: Dividing polynomial by a monomial.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import make_id, rng


SUBSKILLS = [
    "expressions_language_and_substitution",
    "expressions_add_sub_like_terms",
    "expressions_distributive_monomial",
    "expressions_binomial_product",
    "expressions_square_of_binomial",
    "expressions_divide_by_monomial",
]


def _gen_language_substitution(r: random.Random) -> Dict[str, Any]:
    # e.g., for 4x^3 - 7x^2 + 5x - 9: coefficient of x^2, constant term, degree, evaluate at x = -2
    a = r.choice([2, 3, 4, 5])
    b = r.choice([-7, -6, -5, -4, 4, 6])
    c = r.choice([-9, -8, -5, 5, 8, 12])
    x_val = r.choice([-2, -1, 2])
    
    sign_b = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sign_c = f"- {abs(c)}" if c < 0 else f"+ {c}"
    expr_str = f"{a}x^2 {sign_b}x {sign_c}"
    
    val = (a * (x_val**2)) + (b * x_val) + c
    ans = str(val)

    prompt = (
        f"Consider the algebraic expression:\n$${expr_str}$$\n\n"
        f"Evaluate the numerical value of the expression when **$x = {x_val}$**."
    )

    derivation = (
        f"**Step 1: Substitute $x = {x_val}$ into each variable term (use brackets for negatives).**\n"
        f"$$\\text{{Value}} = {a}({x_val})^2 {sign_b}({x_val}) {sign_c}$$\n\n"
        f"**Step 2: Evaluate powers first.**\n"
        f"$$({x_val})^2 = {x_val**2}$$\n"
        f"$$\\text{{Value}} = {a}({x_val**2}) {sign_b}({x_val}) {sign_c}$$\n\n"
        f"**Step 3: Perform multiplication and combine terms.**\n"
        f"$$= {a * (x_val**2)} + ({b * x_val}) {sign_c} = {ans}$$"
    )

    return {
        "id": make_id("g9_algsub"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_language_and_substitution",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Replace every x with ({x_val}).",
            f"Calculate the square first: ({x_val})^2 = {x_val**2}.",
            f"The final evaluated value is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_add_sub_like_terms(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(2, 5)
    b1 = r.randint(-6, 6)
    c1 = r.randint(-9, 9)
    
    a2 = r.randint(1, 4)
    b2 = r.randint(-5, 5)
    c2 = r.randint(-8, 8)
    
    sign_b1 = f"- {abs(b1)}" if b1 < 0 else f"+ {b1}"
    sign_c1 = f"- {abs(c1)}" if c1 < 0 else f"+ {c1}"
    p1 = f"{a1}x^2 {sign_b1}x {sign_c1}"
    
    sign_b2 = f"- {abs(b2)}" if b2 < 0 else f"+ {b2}"
    sign_c2 = f"- {abs(c2)}" if c2 < 0 else f"+ {c2}"
    p2 = f"{a2}x^2 {sign_b2}x {sign_c2}"

    # Subtract p2 from p1
    net_a = a1 - a2
    net_b = b1 - b2
    net_c = c1 - c2

    res_parts = []
    if net_a == 1:
        res_parts.append("x^2")
    elif net_a == -1:
        res_parts.append("-x^2")
    elif net_a != 0:
        res_parts.append(f"{net_a}x^2")
        
    if net_b > 0:
        res_parts.append(f"+{net_b}x" if res_parts else f"{net_b}x")
    elif net_b < 0:
        res_parts.append(f"-{abs(net_b)}x")
        
    if net_c > 0:
        res_parts.append(f"+{net_c}" if res_parts else f"{net_c}")
    elif net_c < 0:
        res_parts.append(f"-{abs(net_c)}")

    ans = "".join(res_parts) or "0"

    prompt = f"Simplify the following by subtracting the polynomials:\n$$({p1}) - ({p2})$$"

    derivation = (
        f"**Step 1: Distribute the negative sign across the second bracket.**\n"
        f"$$= {p1} - {a2}x^2 {-b2:+d}x {-c2:+d}$$\n\n"
        f"**Step 2: Group like terms together.**\n"
        f"$$= ({a1} - {a2})x^2 + ({b1} - ({b2}))x + ({c1} - ({c2}))$$\n\n"
        f"**Step 3: Combine like terms.**\n"
        f"$$= {ans}$$"
    )

    return {
        "id": make_id("g9_algsubpoly"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_add_sub_like_terms",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Be careful with the negative sign before the second bracket: change the sign of each term inside.",
            "Group like terms: x^2 terms, x terms, and constant terms.",
            f"The simplified expression is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_distributive_monomial(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-4, -3, -2, 2, 3, 4])
    a = r.randint(2, 5)
    b = r.choice([-5, -4, -3, 3, 4, 5])
    c = r.choice([-6, -4, 4, 6])
    
    sign_b = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sign_c = f"- {abs(c)}" if c < 0 else f"+ {c}"
    inner = f"{a}x^2 {sign_b}x {sign_c}"
    
    term1 = m * a
    term2 = m * b
    term3 = m * c

    sign_t2 = f"+{term2}" if term2 > 0 else f"-{abs(term2)}"
    sign_t3 = f"+{term3}" if term3 > 0 else f"-{abs(term3)}"
    ans = f"{term1}x^3{sign_t2}x^2{sign_t3}x"

    prompt = f"Expand and simplify using the distributive property:\n$${m}x({inner})$$"

    derivation = (
        f"**Step 1: Multiply the monomial by each term inside the bracket.**\n"
        f"$$({m}x) \\cdot ({a}x^2) + ({m}x) \\cdot ({b}x) + ({m}x) \\cdot ({c})$$\n\n"
        f"**Step 2: Apply exponent product law ($x \\cdot x^2 = x^3$, $x \\cdot x = x^2$).**\n"
        f"$$= {term1}x^3 {sign_t2}x^2 {sign_t3}x = {ans}$$"
    )

    return {
        "id": make_id("g9_algdist"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_distributive_monomial",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Multiply {m}x by each of the 3 terms inside the bracket.",
            "Remember: x * x^2 = x^3 and watch out for signs (+ / -).",
            f"Expanded form: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_binomial_product(r: random.Random) -> Dict[str, Any]:
    # (ax + b)(cx + d)
    a = r.choice([1, 2, 3])
    b = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    c = r.choice([1, 2, 3])
    d = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    
    a_str = "x" if a == 1 else f"{a}x"
    c_str = "x" if c == 1 else f"{c}x"
    b_str = f"- {abs(b)}" if b < 0 else f"+ {b}"
    d_str = f"- {abs(d)}" if d < 0 else f"+ {d}"

    # FOIL: F = ac x^2, O = ad x, I = bc x, L = bd
    f_coeff = a * c
    mid_coeff = (a * d) + (b * c)
    l_coeff = b * d

    f_str = "x^2" if f_coeff == 1 else f"{f_coeff}x^2"
    mid_str = f"+{mid_coeff}x" if mid_coeff > 0 else (f"-{abs(mid_coeff)}x" if mid_coeff < 0 else "")
    l_str = f"+{l_coeff}" if l_coeff > 0 else f"-{abs(l_coeff)}"
    ans = f"{f_str}{mid_str}{l_str}"

    prompt = f"Expand and simplify the product of two binomials:\n$$({a_str} {b_str})({c_str} {d_str})$$"

    derivation = (
        f"**Step 1: Apply FOIL method (First, Outer, Inner, Last).**\n"
        f"- **First:** $({a_str})({c_str}) = {f_str}$\n"
        f"- **Outer:** $({a_str})({d}) = {a * d}x$\n"
        f"- **Inner:** $({b})({c_str}) = {b * c}x$\n"
        f"- **Last:** $({b})({d}) = {l_coeff}$\n\n"
        f"**Step 2: Combine middle like terms.**\n"
        f"$${a * d}x + ({b * c}x) = {mid_coeff}x$$\n\n"
        f"**Step 3: State expanded form.**\n"
        f"$$= {ans}$$"
    )

    return {
        "id": make_id("g9_algfoil"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_binomial_product",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Use FOIL: First terms, Outer terms, Inner terms, Last terms.",
            f"First: {f_str}, Middle sum: ({a*d} + {b*c})x, Last: {l_coeff}.",
            f"Expanded form is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_square_of_binomial(r: random.Random) -> Dict[str, Any]:
    # (ax ± b)^2 = a^2 x^2 ± 2ab x + b^2
    a = r.choice([1, 2, 3, 4])
    b = r.choice([2, 3, 4, 5])
    op = r.choice(["+", "-"])
    
    a_str = "x" if a == 1 else f"{a}x"
    expr = f"({a_str} {op} {b})^2"

    term1 = a ** 2
    term2 = 2 * a * b
    term3 = b ** 2

    t1_str = "x^2" if term1 == 1 else f"{term1}x^2"
    sign_t2 = f"+{term2}" if op == "+" else f"-{term2}"
    ans = f"{t1_str}{sign_t2}x+{term3}"

    prompt = f"Expand and simplify the square of the binomial:\n$${expr}$$"

    derivation = (
        f"**Step 1: Write as the product of two identical binomials.**\n"
        f"$${expr} = ({a_str} {op} {b})({a_str} {op} {b})$$\n\n"
        f"**Step 2: Apply the binomial square rule: $(A \\pm B)^2 = A^2 \\pm 2AB + B^2$.**\n"
        f"- $A^2 = ({a_str})^2 = {t1_str}$\n"
        f"- $2AB = 2({a_str})({b}) = {term2}x$\n"
        f"- $B^2 = ({b})^2 = {term3}$\n\n"
        f"**Step 3: Combine.**\n"
        f"$$= {ans}$$"
    )

    return {
        "id": make_id("g9_algbinsq"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_square_of_binomial",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Remember: (A ± B)^2 = A^2 ± 2AB + B^2.",
            f"Square the first term: {t1_str}. Double the product: {sign_t2}x. Square the last term: +{term3}.",
            f"The expanded expression is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_divide_by_monomial(r: random.Random) -> Dict[str, Any]:
    divisor_coeff = r.choice([2, 3, 4, 5])
    t1_c = divisor_coeff * r.choice([2, 3, 4])
    t2_c = divisor_coeff * r.choice([-5, -4, -3, 3, 4])
    t3_c = divisor_coeff * r.choice([-6, -4, 2, 4, 6])

    sign_t2 = f"- {abs(t2_c)}" if t2_c < 0 else f"+ {t2_c}"
    sign_t3 = f"- {abs(t3_c)}" if t3_c < 0 else f"+ {t3_c}"
    num_str = f"{t1_c}x^3 {sign_t2}x^2 {sign_t3}x"
    den_str = f"{divisor_coeff}x"

    q1 = t1_c // divisor_coeff
    q2 = t2_c // divisor_coeff
    q3 = t3_c // divisor_coeff

    q1_str = "x^2" if q1 == 1 else f"{q1}x^2"
    q2_str = f"+{q2}x" if q2 > 0 else f"-{abs(q2)}x"
    q3_str = f"+{q3}" if q3 > 0 else f"-{abs(q3)}"
    ans = f"{q1_str}{q2_str}{q3_str}"

    prompt = f"Simplify by dividing the polynomial by the monomial:\n$$\\frac{{{num_str}}}{{{den_str}}}$$"

    derivation = (
        f"**Step 1: Divide each term in the numerator separately by the denominator.**\n"
        f"$$= \\frac{{{t1_c}x^3}}{{{den_str}}} + \\frac{{{t2_c}x^2}}{{{den_str}}} + \\frac{{{t3_c}x}}{{{den_str}}}$$\n\n"
        f"**Step 2: Simplify each term using exponent quotient law.**\n"
        f"$$\\frac{{{t1_c}x^3}}{{{divisor_coeff}x}} = {q1_str}, \\quad \\frac{{{t2_c}x^2}}{{{divisor_coeff}x}} = {q2_str}, \\quad \\frac{{{t3_c}x}}{{{divisor_coeff}x}} = {q3_str}$$\n\n"
        f"**Step 3: Combine.**\n"
        f"$$= {ans}$$"
    )

    return {
        "id": make_id("g9_algdiv"),
        "topic": "Algebraic expressions 1",
        "subskill": "expressions_divide_by_monomial",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Divide each term in the numerator by {den_str}.",
            "Subtract exponents: x^3/x = x^2, x^2/x = x, x/x = 1.",
            f"The quotient is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


GENERATORS = {
    "expressions_language_and_substitution": _gen_language_substitution,
    "expressions_add_sub_like_terms": _gen_add_sub_like_terms,
    "expressions_distributive_monomial": _gen_distributive_monomial,
    "expressions_binomial_product": _gen_binomial_product,
    "expressions_square_of_binomial": _gen_square_of_binomial,
    "expressions_divide_by_monomial": _gen_divide_by_monomial,
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


def generate_grade9_algebraic_expressions_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res[0] if res else {}
