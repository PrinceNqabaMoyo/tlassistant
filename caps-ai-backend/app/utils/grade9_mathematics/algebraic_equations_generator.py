"""Grade 9 Mathematics - Algebraic Equations 1 (Linear Equations & Brackets).
Grounded in:
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md (Inspection, additive/multiplicative inverses, brackets)
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 1.md (Chapter 14: Solving number sentences, checking solutions)

Subskills:
  1. equations_inspection: Solving by inspection using a table of values.
  2. equations_linear_two_step: Solving ax + b = c using additive and multiplicative inverses.
  3. equations_brackets: Solving linear equations containing brackets: a(x + b) = c(x + d).
  4. equations_variables_both_sides: Solving equations with variable terms on both sides.
  5. equations_check_substitution: Checking solutions by substituting into LHS and RHS.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import make_id, rng


SUBSKILLS = [
    "equations_inspection",
    "equations_linear_two_step",
    "equations_brackets",
    "equations_variables_both_sides",
    "equations_check_substitution",
]


def _gen_inspection(r: random.Random) -> Dict[str, Any]:
    # Table of values with Candidate x values
    m1, c1 = r.choice([2, 3]), r.choice([1, 2, 3, 4])
    m2, c2 = r.choice([-2, -1, 1]), r.choice([6, 7, 8, 9, 10])
    
    # Ensure a single integer intersection
    if m1 - m2 == 0:
        m2 = -1
    x_sol = (c2 - c1) // (m1 - m2) if (c2 - c1) % (m1 - m2) == 0 else 2
    c2 = m1 * x_sol + c1 - m2 * x_sol
    
    # Generate table row for x in range [x_sol - 2, x_sol + 2]
    xs = list(range(x_sol - 2, x_sol + 3))
    lhs_vals = [m1 * x + c1 for x in xs]
    rhs_vals = [m2 * x + c2 for x in xs]

    header = "| $x$ | " + " | ".join(str(x) for x in xs) + " |"
    sep = "| :---: | " + " | ".join([":---:"] * len(xs)) + " |"
    lhs_row = f"| ${m1}x + {c1}$ | " + " | ".join(str(v) for v in lhs_vals) + " |"
    rhs_row = f"| ${m2}x + {c2}$ | " + " | ".join(str(v) for v in rhs_vals) + " |"
    table_md = f"{header}\n{sep}\n{lhs_row}\n{rhs_row}"

    ans = str(x_sol)
    prompt = (
        f"Use the inspection table below to find the value of $x$ for which the left-hand side "
        f"equals the right-hand side in the equation:\n"
        f"$${m1}x + {c1} = {m2}x + {c2}$$\n\n"
        f"{table_md}"
    )

    derivation = (
        f"**Step 1: Inspect the table where LHS row equals RHS row.**\n"
        f"When $x = {x_sol}$:\n"
        f"- $\\text{{LHS}} = {m1}({x_sol}) + {c1} = {m1*x_sol + c1}$\n"
        f"- $\\text{{RHS}} = {m2}({x_sol}) + {c2} = {m2*x_sol + c2}$\n\n"
        f"**Step 2: State the solution by inspection.**\n"
        f"Both sides equal {m1*x_sol + c1} when $x = {ans}$."
    )

    return {
        "id": make_id("g9_eqinsp"),
        "topic": "Equations 1",
        "subskill": "equations_inspection",
        "difficulty": "easy",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Look for the column in the table where the values in both expression rows are identical.",
            f"Notice that when x = {ans}, both expressions equal {m1*x_sol + c1}.",
            f"x = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** x = {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_linear_two_step(r: random.Random) -> Dict[str, Any]:
    # a x + b = c
    a = r.choice([-5, -4, -3, -2, 2, 3, 4, 5, 6])
    x_val = r.randint(-7, 8)
    b = r.choice([-15, -12, -9, 8, 11, 14, 17])
    c = a * x_val + b
    
    b_str = f"- {abs(b)}" if b < 0 else f"+ {b}"
    ans = str(x_val)

    prompt = f"Solve the following linear equation for $x$:\n$${a}x {b_str} = {c}$$"

    derivation = (
        f"**Step 1: Apply additive inverse of {b} to both sides.**\n"
        f"$${a}x = {c} - ({b})$$\n"
        f"$${a}x = {c - b}$$\n\n"
        f"**Step 2: Apply multiplicative inverse (divide both sides by {a}).**\n"
        f"$$x = \\frac{{{c - b}}}{{{a}}} = {ans}$$"
    )

    return {
        "id": make_id("g9_eq2step"),
        "topic": "Equations 1",
        "subskill": "equations_linear_two_step",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Subtract {b} from both sides.",
            f"Divide both sides by {a}.",
            f"x = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** x = {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_brackets(r: random.Random) -> Dict[str, Any]:
    # a(x + b) = c(x + d) + e
    a = r.choice([2, 3, 4])
    x_val = r.randint(-5, 6)
    b = r.randint(-4, 4)
    c = r.choice([1, 2])
    d = r.randint(-3, 3)
    
    # a(x_val + b) = c(x_val + d) + e => e = a(x_val + b) - c(x_val + d)
    e = a * (x_val + b) - c * (x_val + d)
    
    b_str = f"- {abs(b)}" if b < 0 else f"+ {b}"
    d_str = f"- {abs(d)}" if d < 0 else f"+ {d}"
    c_part = f"{c}(x {d_str})" if c != 1 else f"(x {d_str})"
    e_str = f"+ {e}" if e > 0 else (f"- {abs(e)}" if e < 0 else "")
    
    ans = str(x_val)
    prompt = f"Solve for $x$ in the equation:\n$${a}(x {b_str}) = {c_part} {e_str}$$"

    derivation = (
        f"**Step 1: Expand brackets on both sides using distributive property.**\n"
        f"$${a}x {a*b:+d} = {c}x {c*d:+d} {e_str}$$\n"
        f"$${a}x {a*b:+d} = {c}x {c*d + e:+d}$$\n\n"
        f"**Step 2: Group variable terms on left and constant terms on right.**\n"
        f"$${a}x - {c}x = {c*d + e} - ({a*b})$$\n"
        f"$${a - c}x = {c*d + e - a*b}$$\n\n"
        f"**Step 3: Solve for $x$.**\n"
        f"$$x = \\frac{{{c*d + e - a*b}}}{{{a - c}}} = {ans}$$"
    )

    return {
        "id": make_id("g9_eqbrk"),
        "topic": "Equations 1",
        "subskill": "equations_brackets",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Expand all brackets first using the distributive law.",
            "Group terms with x on one side and numbers on the other side.",
            f"x = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** x = {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_variables_both_sides(r: random.Random) -> Dict[str, Any]:
    a = r.choice([3, 4, 5, 7])
    c = r.choice([1, 2])
    x_val = r.randint(-6, 7)
    b = r.randint(-12, 12)
    d = (a - c) * x_val + b
    
    b_str = f"- {abs(b)}" if b < 0 else f"+ {b}"
    d_str = f"- {abs(d)}" if d < 0 else f"+ {d}"
    ans = str(x_val)

    prompt = f"Solve the following linear equation for $x$:\n$${a}x {b_str} = {c}x {d_str}$$"

    derivation = (
        f"**Step 1: Collect like variable terms on the left.**\n"
        f"$${a}x - {c}x = {d} - ({b})$$\n"
        f"$${a - c}x = {d - b}$$\n\n"
        f"**Step 2: Divide both sides by the coefficient {a - c}.**\n"
        f"$$x = \\frac{{{d - b}}}{{{a - c}}} = {ans}$$"
    )

    return {
        "id": make_id("g9_eqvars"),
        "topic": "Equations 1",
        "subskill": "equations_variables_both_sides",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Subtract {c}x from both sides.",
            f"Isolate x: {a-c}x = {d-b}.",
            f"x = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** x = {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_check_substitution(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2, 3, 4])
    c = r.randint(-5, 5)
    true_x = r.randint(-3, 4)
    rhs = m * true_x + c
    
    test_x = true_x if r.choice([True, False]) else true_x + r.choice([-1, 1])
    is_solution = (test_x == true_x)
    
    c_str = f"- {abs(c)}" if c < 0 else f"+ {c}"
    prompt = (
        f"Determine whether **$x = {test_x}$** is the correct solution to the equation:\n"
        f"$${m}x {c_str} = {rhs}$$\n\n"
        f"Answer **Yes** or **No**."
    )
    ans = "Yes" if is_solution else "No"

    lhs_val = m * test_x + c
    derivation = (
        f"**Step 1: Substitute $x = {test_x}$ into Left-Hand Side (LHS).**\n"
        f"$$\\text{{LHS}} = {m}({test_x}) {c_str} = {m*test_x} {c_str} = {lhs_val}$$\n\n"
        f"**Step 2: Compare with Right-Hand Side (RHS).**\n"
        f"$$\\text{{RHS}} = {rhs}$$\n\n"
        f"**Step 3: Conclusion.**\n"
        f"Since $\\text{{LHS}} {'=' if is_solution else '\\neq'} \\text{{RHS}}$, $x = {test_x}$ **{'is' if is_solution else 'is not'}** a solution."
    )

    return {
        "id": make_id("g9_eqchk"),
        "topic": "Equations 1",
        "subskill": "equations_check_substitution",
        "difficulty": "easy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": ["Yes", "No"],
        "correct_answer": ans,
        "hints": [
            f"Substitute x = {test_x} into {m}x {c_str}.",
            f"LHS evaluates to {lhs_val}. Compare this with RHS ({rhs}).",
            f"Answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


GENERATORS = {
    "equations_inspection": _gen_inspection,
    "equations_linear_two_step": _gen_linear_two_step,
    "equations_brackets": _gen_brackets,
    "equations_variables_both_sides": _gen_variables_both_sides,
    "equations_check_substitution": _gen_check_substitution,
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


def generate_grade9_algebraic_equations_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res[0] if res else {}
