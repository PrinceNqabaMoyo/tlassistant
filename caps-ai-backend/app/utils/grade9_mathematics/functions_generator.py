"""Grade 9 Mathematics - Functions & Relationships Generator.
Grounded in:
  - curriculum_docs/Mathematics_Gr9/Functions and relationships.md (Input/output, flow diagrams, tables, formulae)
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/05. Functions and relationships.md (Chapter 12: From counting to calculating, rules y = mx + c)

Subskills:
  1. functions_flow_diagram_output: Calculating output y from input x through flow diagrams.
  2. functions_table_completion: Completing input/output values in tables.
  3. functions_determine_formula: Determining algebraic rule y = mx + c from table values.
  4. functions_inverse_input: Finding input x given output y.
  5. functions_equivalent_representations: Matching verbal rules, equations, and tables.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import make_id, rng


SUBSKILLS = [
    "functions_flow_diagram_output",
    "functions_table_completion",
    "functions_determine_formula",
    "functions_inverse_input",
    "functions_equivalent_representations",
]


def _gen_flow_diagram(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-3, -2, 2, 3, 4, 5])
    c = r.choice([-7, -5, -3, 2, 4, 6])
    x_val = r.choice([-3, -2, 0, 2, 4, 5])
    
    y_val = m * x_val + c
    ans = str(y_val)

    m_str = f"\\times ({m})" if m < 0 else f"\\times {m}"
    c_str = f"- {abs(c)}" if c < 0 else f"+ {c}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_flow",
        "input_label": "x",
        "input_val": x_val,
        "operations": [
            {"op": f"× {m}"},
            {"op": f"{'+ ' if c > 0 else '- '}{abs(c)}"},
        ],
        "output_label": "y",
    }

    prompt = (
        f"A mathematical flow diagram processes an input number $x$ as follows:\n\n"
        f"$$\\text{{Input }} x \\longrightarrow [ {m_str} ] \\longrightarrow [ {c_str} ] \\longrightarrow \\text{{Output }} y$$\n\n"
        f"Calculate the **output value ($y$)** when the input value is **$x = {x_val}$**."
    )

    derivation = (
        f"**Step 1: Write down the functional equation.**\n"
        f"$$y = {m}x {c_str}$$\n\n"
        f"**Step 2: Substitute $x = {x_val}$.**\n"
        f"$$y = ({m})({x_val}) {c_str} = {m * x_val} {c_str} = {ans}$$"
    )

    return {
        "id": make_id("g9_funcflow"),
        "topic": "Functions and relationships",
        "subskill": "functions_flow_diagram_output",
        "difficulty": "easy",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            f"Multiply input {x_val} by {m} first.",
            f"Then add {c} to the result.",
            f"Output y = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_table_completion(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2, 3, 4, -2, -3])
    c = r.choice([-4, -2, 1, 3, 5])
    
    xs = [-2, -1, 0, 1, 2, 3]
    ys = [m * x + c for x in xs]
    
    # Target one output
    target_idx = r.choice([0, 1, 4, 5])
    target_x = xs[target_idx]
    ans = str(ys[target_idx])

    # Table format
    header = "| $x$ | " + " | ".join(str(x) for x in xs) + " |"
    sep = "| :---: | " + " | ".join([":---:"] * len(xs)) + " |"
    y_row_items = [str(y) if i != target_idx else "**?**" for i, y in enumerate(ys)]
    y_row = "| $y$ | " + " | ".join(y_row_items) + " |"
    table_md = f"{header}\n{sep}\n{y_row}"

    c_str = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    prompt = (
        f"The table below represents the linear function rule **$y = {m}x{c_str}$**:\n\n"
        f"{table_md}\n\n"
        f"Calculate the missing value indicated by **?** when $x = {target_x}$."
    )

    derivation = (
        f"**Step 1: Identify input value for missing position.**\n"
        f"$$x = {target_x}$$\n\n"
        f"**Step 2: Substitute into function formula.**\n"
        f"$$y = {m}({target_x}){c_str} = {m * target_x}{c_str} = {ans}$$"
    )

    return {
        "id": make_id("g9_functbl"),
        "topic": "Functions and relationships",
        "subskill": "functions_table_completion",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Use the formula y = {m}x{c_str}.",
            f"Substitute x = {target_x}.",
            f"y = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_determine_formula(r: random.Random) -> Dict[str, Any]:
    m = r.choice([-4, -3, -2, 2, 3, 4, 5])
    c = r.choice([-5, -3, -1, 1, 2, 4, 6])
    
    xs = [1, 2, 3, 4]
    ys = [m * x + c for x in xs]
    
    header = "| $x$ | " + " | ".join(str(x) for x in xs) + " |"
    sep = "| :---: | " + " | ".join([":---:"] * len(xs)) + " |"
    y_row = "| $y$ | " + " | ".join(str(y) for y in ys) + " |"
    table_md = f"{header}\n{sep}\n{y_row}"

    sign_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    ans = f"{m}x{sign_c}".replace(" ", "")

    prompt = (
        f"Consider the table of values for a linear function:\n\n"
        f"{table_md}\n\n"
        f"Determine the algebraic rule in terms of $x$ for $y$ (write the expression on the right-hand side of $y =$ in simplest form)."
    )

    derivation = (
        f"**Step 1: Determine the constant rate of change (gradient $m$).**\n"
        f"$$m = \\frac{{\\Delta y}}{{\\Delta x}} = \\frac{{{ys[1]} - ({ys[0]})}}{{{xs[1]} - {xs[0]}}} = {m}$$\n\n"
        f"**Step 2: Determine constant term ($c$).**\n"
        f"When $x = 0$, $y = c$.\n"
        f"$$c = y_1 - m(x_1) = {ys[0]} - ({m})(1) = {c}$$\n\n"
        f"**Step 3: State the formula.**\n"
        f"$$y = {m}x{sign_c}$$"
    )

    return {
        "id": make_id("g9_funcrule"),
        "topic": "Functions and relationships",
        "subskill": "functions_determine_formula",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            "Find the difference between consecutive y-values (change in y).",
            f"Rate of change is {m}. Now find constant c when x = 0.",
            f"The rule is {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_inverse_input(r: random.Random) -> Dict[str, Any]:
    m = r.choice([2, 3, 4, 5])
    c = r.choice([-6, -4, -2, 3, 5, 7])
    x_val = r.randint(3, 9)
    y_val = m * x_val + c
    
    sign_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
    ans = str(x_val)

    prompt = (
        f"A function is defined by the formula **$y = {m}x{sign_c}$**.\n\n"
        f"Determine the **input value ($x$)** that produces an output value of **$y = {y_val}$**."
    )

    derivation = (
        f"**Step 1: Set up the equation with given $y$.**\n"
        f"$${m}x{sign_c} = {y_val}$$\n\n"
        f"**Step 2: Isolate the term with $x$.**\n"
        f"$${m}x = {y_val} - ({c})$$\n"
        f"$${m}x = {y_val - c}$$\n\n"
        f"**Step 3: Solve for $x$.**\n"
        f"$$x = \\frac{{{y_val - c}}}{{{m}}} = {ans}$$"
    )

    return {
        "id": make_id("g9_funcinv"),
        "topic": "Functions and relationships",
        "subskill": "functions_inverse_input",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "hints": [
            f"Substitute y = {y_val} into y = {m}x{sign_c}.",
            f"Solve the linear equation for x: {m}x = {y_val - c}.",
            f"x = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** x = {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_equivalent_representations(r: random.Random) -> Dict[str, Any]:
    # Match verbal rule to algebraic equation
    m = r.choice([2, 3, 4])
    c = r.choice([1, 2, 3, 5])
    verbal = f"Multiply the input number by {m} and then add {c} to the product."
    correct_eq = f"y = {m}x + {c}"
    
    distractors = [
        f"y = {c}x + {m}",
        f"y = {m}(x + {c})",
        f"y = \\frac{{x}}{{{m}}} + {c}",
        f"y = {m}x - {c}",
    ]
    r.shuffle(distractors)
    opts = [correct_eq] + distractors[:3]
    r.shuffle(opts)

    prompt = (
        f"Which of the following equations correctly represents this verbal instruction:\n\n"
        f"> *\"{verbal}\"*"
    )

    return {
        "id": make_id("g9_funcrep"),
        "topic": "Functions and relationships",
        "subskill": "functions_equivalent_representations",
        "difficulty": "easy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": opts,
        "correct_answer": correct_eq,
        "hints": [
            f"'Multiply input by {m}' gives {m}x.",
            f"'Add {c} to product' gives + {c}.",
            f"Equation is {correct_eq}.",
        ],
        "explanation": f"**Analysis:**\nMultiplying input $x$ by ${m}$ yields ${m}x$. Adding ${c}$ yields ${correct_eq}$.\n\n**Correct Answer:** {correct_eq} [1 mark]",
        "mark_allocation": 1,
    }


GENERATORS = {
    "functions_flow_diagram_output": _gen_flow_diagram,
    "functions_table_completion": _gen_table_completion,
    "functions_determine_formula": _gen_determine_formula,
    "functions_inverse_input": _gen_inverse_input,
    "functions_equivalent_representations": _gen_equivalent_representations,
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


def generate_grade9_functions_relationships_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res[0] if res else {}
