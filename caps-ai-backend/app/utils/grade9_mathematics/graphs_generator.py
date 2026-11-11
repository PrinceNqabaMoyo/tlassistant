"""Grade 9 Mathematics - Graphs & Linear Functions (6-Pillar Generator).
Grounded in:
  - curriculum_docs/Mathematics_Gr9/Functions and relationships.md (Input/output, Cartesian representation)
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/02. Graphs.md (Chapter 15: Rates of change, gradient m, dual intercepts, y = mx + c)

Subskills:
  1. graphs_gradient_calculation: Finding gradient m = (y2 - y1) / (x2 - x1) from coordinate pairs.
  2. graphs_dual_intercept_method: Determining x-intercept (y=0) and y-intercept (x=0).
  3. graphs_equation_from_graph: Determining y = mx + c from plotted lines and coordinates.
  4. graphs_rate_of_change_context: Real-world gradient interpretation (speed, flow rate, cost per km).
  5. graphs_plotting_and_quadrants: Reading coordinate landmarks and points on Cartesian plane.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import make_id, rng


SUBSKILLS = [
    "graphs_gradient_calculation",
    "graphs_dual_intercept_method",
    "graphs_equation_from_graph",
    "graphs_rate_of_change_context",
    "graphs_plotting_and_quadrants",
]


def _gen_gradient_calc(r: random.Random) -> Dict[str, Any]:
    # Two points A(x1, y1) and B(x2, y2)
    x1 = r.randint(-4, 1)
    x2 = x1 + r.choice([1, 2, 3, 4])
    m_val = r.choice([-3, -2, -1, 1, 2, 3])
    c_val = r.randint(-4, 4)
    
    y1 = m_val * x1 + c_val
    y2 = m_val * x2 + c_val
    
    ans = str(m_val)
    prompt = (
        f"Calculate the **gradient ($m$)** of the straight line passing through the points "
        f"**$A({x1};\\ {y1})$** and **$B({x2};\\ {y2})$**."
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_graph",
        "domain": [-6, 6],
        "range": [-6, 6],
        "curves": [
            {
                "family": "linear",
                "params": {"m": m_val, "c": c_val},
                "color": "#2563eb",
                "label": f"y = {m_val}x + {c_val}",
            }
        ],
        "landmarks": [
            {"x": x1, "y": y1, "label": f"A({x1}; {y1})"},
            {"x": x2, "y": y2, "label": f"B({x2}; {y2})"},
        ],
    }

    derivation = (
        f"**Step 1: State the gradient formula.**\n"
        f"$$m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$$\n\n"
        f"**Step 2: Substitute coordinate points $A({x1};\\ {y1})$ and $B({x2};\\ {y2})$.**\n"
        f"$$m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {ans}$$\n\n"
        f"**Step 3: Conclusion.**\n"
        f"The gradient is **$m = {ans}$** (a {'positive' if m_val > 0 else 'negative'} slope)."
    )

    return {
        "id": make_id("g9_grfgrad"),
        "topic": "Graphs",
        "subskill": "graphs_gradient_calculation",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            "Use the standard gradient formula: m = (y2 - y1) / (x2 - x1).",
            f"m = ({y2} - {y1}) / ({x2} - {x1}).",
            f"m = {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** m = {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_dual_intercept(r: random.Random) -> Dict[str, Any]:
    # Line: y = mx + c with integer intercepts
    m = r.choice([-3, -2, 2, 3])
    x_int = r.choice([-4, -3, -2, 2, 3, 4])
    # 0 = m(x_int) + c => c = -m * x_int
    c = -m * x_int
    
    target = r.choice(["x_intercept", "y_intercept"])
    sign_c = f"+ {c}" if c > 0 else f"- {abs(c)}"
    eq_str = f"y = {m}x {sign_c}"

    if target == "x_intercept":
        ans = str(x_int)
        prompt = f"Determine the **$x$-intercept** of the straight line with equation **${eq_str}$** (state the value of $x$ where $y = 0$)."
        derivation = (
            f"**Step 1: Set $y = 0$ to find the $x$-intercept.**\n"
            f"$$0 = {m}x {sign_c}$$\n"
            f"$$-{m}x = {c}$$\n"
            f"$$x = \\frac{{{c}}}{{{-m}}} = {ans}$$\n\n"
            f"**Step 2: Conclusion.**\n"
            f"The $x$-intercept coordinate is $({ans};\\ 0)$."
        )
    else:
        ans = str(c)
        prompt = f"Determine the **$y$-intercept** of the straight line with equation **${eq_str}$** (state the value of $y$ where $x = 0$)."
        derivation = (
            f"**Step 1: Set $x = 0$ to find the $y$-intercept.**\n"
            f"$$y = {m}(0) {sign_c} = {ans}$$\n\n"
            f"**Step 2: Conclusion.**\n"
            f"The $y$-intercept coordinate is $(0;\\ {ans})$."
        )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_graph",
        "domain": [-6, 6],
        "range": [-8, 8],
        "curves": [
            {
                "family": "linear",
                "params": {"m": m, "c": c},
                "color": "#16a34a",
                "label": eq_str,
            }
        ],
        "landmarks": [
            {"x": x_int, "y": 0, "label": f"({x_int}; 0)"},
            {"x": 0, "y": c, "label": f"(0; {c})"},
        ],
    }

    return {
        "id": make_id("g9_grfint"),
        "topic": "Graphs",
        "subskill": "graphs_dual_intercept_method",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            "For the x-intercept set y = 0 and solve for x. For the y-intercept set x = 0 and find y.",
            f"Equation: {eq_str}.",
            f"Answer: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_equation_from_graph(r: random.Random) -> Dict[str, Any]:
    # Given y-intercept (0, c) and another point (x1, y1)
    m = r.choice([-3, -2, -1, 1, 2, 3])
    c = r.choice([-4, -3, -2, 1, 2, 3, 4])
    x1 = r.choice([1, 2, 3])
    y1 = m * x1 + c

    sign_c = f"+ {c}" if c > 0 else f"- {abs(c)}"
    m_str = "x" if m == 1 else ("-x" if m == -1 else f"{m}x")
    ans = f"{m_str}{sign_c}".replace(" ", "")

    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_graph",
        "domain": [-5, 5],
        "range": [-6, 6],
        "curves": [
            {
                "family": "linear",
                "params": {"m": m, "c": c},
                "color": "#dc2626",
                "label": "Line L",
            }
        ],
        "landmarks": [
            {"x": 0, "y": c, "label": f"(0; {c})"},
            {"x": x1, "y": y1, "label": f"({x1}; {y1})"},
        ],
    }

    prompt = (
        f"A straight line graph passes through the $y$-intercept **$(0;\\ {c})$** and the point **$({x1};\\ {y1})$**.\n\n"
        f"Determine the equation of the line in standard form **$y = mx + c$** (type the right-hand side expression in simplest form)."
    )

    derivation = (
        f"**Step 1: Identify the $y$-intercept ($c$).**\n"
        f"Since the line passes through $(0;\\ {c})$, the constant term is $c = {c}$.\n\n"
        f"**Step 2: Calculate the gradient ($m$).**\n"
        f"$$m = \\frac{{y_2 - y_1}}{{x_2 - x_1}} = \\frac{{{y1} - ({c})}}{{{x1} - 0}} = \\frac{{{y1 - c}}}{{{x1}}} = {m}$$\n\n"
        f"**Step 3: State the equation.**\n"
        f"$$y = {m_str} {sign_c}$$"
    )

    return {
        "id": make_id("g9_grfeq"),
        "topic": "Graphs",
        "subskill": "graphs_equation_from_graph",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            f"The y-intercept is at (0; {c}), so c = {c}.",
            f"Find the gradient using m = ({y1} - {c}) / ({x1} - 0) = {m}.",
            f"RHS expression: {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [3 marks]",
        "mark_allocation": 3,
    }


def _gen_rate_of_change_context(r: random.Random) -> Dict[str, Any]:
    # e.g., Speed from distance-time graph
    speed = r.choice([60, 75, 80, 90, 100])
    hours = r.choice([2, 3, 4])
    dist = speed * hours
    
    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_graph",
        "domain": [0, hours + 1],
        "range": [0, dist + 40],
        "curves": [
            {
                "family": "linear",
                "params": {"m": speed, "c": 0},
                "color": "#9333ea",
                "label": "Distance (km) vs Time (h)",
            }
        ],
        "landmarks": [
            {"x": 0, "y": 0, "label": "Start (0; 0)"},
            {"x": hours, "y": dist, "label": f"({hours}h; {dist}km)"},
        ],
    }

    ans = str(speed)
    prompt = (
        f"A distance-time graph shows that a bus travels from rest and covers **{dist} km** in **{hours} hours** at a constant speed.\n\n"
        f"Calculate the **rate of change (constant speed)** of the bus in **km/h**."
    )

    derivation = (
        f"**Step 1: Identify that the gradient of a distance-time graph represents speed.**\n"
        f"$$\\text{{Speed}} = \\text{{Gradient}} = \\frac{{\\Delta \\text{{Distance}}}}{{\\Delta \\text{{Time}}}}$$\n\n"
        f"**Step 2: Calculate rate of change.**\n"
        f"$$\\text{{Speed}} = \\frac{{{dist} \\text{{ km}}}}{{{hours} \\text{{ h}}}} = {ans} \\text{{ km/h}}$$"
    )

    return {
        "id": make_id("g9_grfrate"),
        "topic": "Graphs",
        "subskill": "graphs_rate_of_change_context",
        "difficulty": "medium",
        "question_type": "typed",
        "prompt": prompt,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            "In a distance-time graph, the gradient (slope) equals the speed.",
            f"Divide distance ({dist} km) by time ({hours} h).",
            f"Speed = {ans} km/h.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [2 marks]",
        "mark_allocation": 2,
    }


def _gen_plotting_quadrants(r: random.Random) -> Dict[str, Any]:
    x = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = r.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
    if x > 0 and y > 0:
        quad = "Quadrant 1"
    elif x < 0 and y > 0:
        quad = "Quadrant 2"
    elif x < 0 and y < 0:
        quad = "Quadrant 3"
    else:
        quad = "Quadrant 4"

    opts = ["Quadrant 1", "Quadrant 2", "Quadrant 3", "Quadrant 4"]
    ans = quad

    diagram_spec = {
        "diagram_role": "context",
        "kind": "function_graph",
        "domain": [-5, 5],
        "range": [-5, 5],
        "landmarks": [
            {"x": x, "y": y, "label": f"P({x}; {y})"},
        ],
    }

    prompt = f"In which quadrant of the Cartesian plane does the coordinate point **$P({x};\\ {y})$** lie?"

    derivation = (
        f"**Step 1: Check signs of coordinates.**\n"
        f"- $x = {x}$ ({'positive' if x > 0 else 'negative'})\n"
        f"- $y = {y}$ ({'positive' if y > 0 else 'negative'})\n\n"
        f"**Step 2: Apply quadrant definitions.**\n"
        f"- Quad 1: (+, +), Quad 2: (-, +), Quad 3: (-, -), Quad 4: (+, -)\n"
        f"Therefore, $P({x};\\ {y})$ lies in **{ans}**."
    )

    return {
        "id": make_id("g9_grfquad"),
        "topic": "Graphs",
        "subskill": "graphs_plotting_and_quadrants",
        "difficulty": "easy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": opts,
        "correct_answer": ans,
        "diagram_spec": diagram_spec,
        "hints": [
            "Top-right is Quadrant 1 (+, +), Top-left is Quadrant 2 (-, +).",
            "Bottom-left is Quadrant 3 (-, -), Bottom-right is Quadrant 4 (+, -).",
            f"Point is in {ans}.",
        ],
        "explanation": f"{derivation}\n\n**Correct Answer:** {ans} [1 mark]",
        "mark_allocation": 1,
    }


GENERATORS = {
    "graphs_gradient_calculation": _gen_gradient_calc,
    "graphs_dual_intercept_method": _gen_dual_intercept,
    "graphs_equation_from_graph": _gen_equation_from_graph,
    "graphs_rate_of_change_context": _gen_rate_of_change_context,
    "graphs_plotting_and_quadrants": _gen_plotting_quadrants,
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


def generate_grade9_graphs_question(
    subskill: str = "mixed",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    res = generate(subskill=subskill, difficulty=difficulty, count=1, seed=seed, **kwargs)
    return res[0] if res else {}
