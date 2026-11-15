"""Grade 10 Mathematics — Term 2 — Functions Archetypes 01 to 25.

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Functions syllabus.
Covers:
- Concept of a function, relations, dependent/independent variables
- Function notation f(x) evaluation and inverse solving for linear, quadratic, hyperbola, exponential
- Linear functions f(x) = ax + q: gradient, intercepts, equations, domain/range
- Quadratic functions f(x) = ax^2 + q: parameters a and q, turning point, axis of symmetry, intercepts, range

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

TERM = 2
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 8
TOPIC_ID = "grade10_math_functions"
LEARNING_OBJECTIVE = "math10_functions"


def _fmt_num(n: float | int) -> str:
    """Format number with SA comma decimal separator."""
    if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
        return str(int(n))
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _coord(x: float | int, y: float | int) -> str:
    """Ordered pair in SA notation (semicolon separator)."""
    return f"({_fmt_num(x)};\\, {_fmt_num(y)})"


def _signed(n: int | float, space: bool = True) -> str:
    """Format signed number with plus or minus."""
    val_str = _fmt_num(abs(n))
    if n >= 0:
        return f"+ {val_str}" if space else f"+{val_str}"
    else:
        return f"- {val_str}" if space else f"-{val_str}"


def _make_svg_axes_frame(
    elements: List[str],
    viewbox: str = "0 0 400 300",
    origin: Tuple[int, int] = (200, 150),
    scale: float = 20.0,
    x_range: Tuple[int, int] = (-8, 8),
    y_range: Tuple[int, int] = (-6, 6),
) -> str:
    """Generate high-contrast 2D Cartesian SVG frame with axes, grid, and curves."""
    ox, oy = origin
    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; }',
        '  .axis { stroke: #1e293b; stroke-width: 1.5; }',
        '  .curve { fill: none; stroke-width: 2.5; stroke-linecap: round; }',
        '  .dot { fill: #2563eb; stroke: #ffffff; stroke-width: 1.5; }',
        '  .label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #475569; }',
        '  .axis-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; font-weight: bold; fill: #1e293b; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
    ]

    # Grid lines
    for x in range(x_range[0], x_range[1] + 1):
        if x != 0:
            px = ox + x * scale
            svg_parts.append(f'<line x1="{px}" y1="10" x2="{px}" y2="{oy*2 - 10}" class="grid" />')
    for y in range(y_range[0], y_range[1] + 1):
        if y != 0:
            py = oy - y * scale
            svg_parts.append(f'<line x1="10" y1="{py}" x2="{ox*2 - 10}" y2="{py}" class="grid" />')

    # Main Axes
    svg_parts.append(f'<line x1="10" y1="{oy}" x2="{ox*2 - 10}" y2="{oy}" class="axis" />')
    svg_parts.append(f'<line x1="{ox}" y1="{oy*2 - 10}" x2="{ox}" y2="10" class="axis" />')

    # Arrows and Labels
    svg_parts.append(f'<text x="{ox*2 - 18}" y="{oy - 6}" class="axis-label">x</text>')
    svg_parts.append(f'<text x="{ox + 8}" y="20" class="axis-label">y</text>')
    svg_parts.append(f'<text x="{ox - 14}" y="{oy + 14}" class="label">O</text>')

    # Custom elements
    svg_parts.extend(elements)
    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def _base_contract(
    subskill: str,
    prompt: str,
    answer: str,
    options: Optional[List[str]],
    sol_steps: List[Dict[str, str]],
    t1: str,
    t2: str,
    t3: str,
    misconceptions: List[str],
    marks: int = 3,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Helper to enforce universal 6-pillar contract."""
    q: Dict[str, Any] = {
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": SUGGESTED_DURATION,
        "topic": TOPIC_ID,
        "learning_objective_id": LEARNING_OBJECTIVE,
        "subskill": subskill,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "mcq" if options else "short_answer",
        "total_marks": marks,
        "misconception_tags": misconceptions,
        "hints": [
            {"tier": 1, "title": "Key Concept", "text": t1},
            {"tier": 2, "title": "Formula / Method", "text": t2},
            {"tier": 3, "title": "Worked Step", "text": t3},
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{subskill}_{i+1}", "desc": s.get("rule", "Correct step"), "marks": 1, "editable": True}
                for i, s in enumerate(sol_steps[:marks])
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "solution_steps": sol_steps,
        "sample_answer": answer,
        "worked_solution": "\n".join([f"- **Step {i+1}**: {s.get('op', '')} $\\implies$ ${s.get('to', '')}$" for i, s in enumerate(sol_steps)]),
    }
    if options:
        q["options"] = options
        q["correct_index"] = options.index(answer)
        q["options_latex"] = options
    else:
        q["answer_latex"] = answer
        q["answer_value"] = answer
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_concept_function_definition_and_relation_test"
    rels = [
        ("Each learner is assigned exactly one unique student ID number.", True, "One-to-one relation: each input has exactly one unique output."),
        ("A cellphone number mapping to all contacts stored under it.", False, "One-to-many relation: a single input produces multiple outputs, violating the definition of a function."),
        ("Each vehicle in South Africa is linked to its unique licence disc registration.", True, "One-to-one relation: each car has one unique licence code."),
        ("A person mapping to all the blood types they possess.", True, "Each person has exactly one biological blood group."),
        ("An integer $x$ mapping to both $+\\sqrt{x}$ and $-\\sqrt{x}$.", False, "One-to-many relation: input $x = 4$ gives outputs $+2$ and $-2$, failing the vertical line test."),
        ("A circle defined by $x^2 + y^2 = 25$.", False, "Fails the vertical line test; a vertical line $x = 3$ intersects the circle at both $y = 4$ and $y = -4$."),
    ]
    stmt, is_func, reason = rng.choice(rels)
    prompt = f"Determine whether the following mathematical relationship defines a valid function: \"{stmt}\""
    ans = "Yes, it is a function" if is_func else "No, it is not a function"
    opts = ["Yes, it is a function", "No, it is not a function"]
    rng.shuffle(opts)
    steps = [
        {"from": stmt, "to": "Definition: every input must correspond to exactly one output.", "rule": "function definition", "op": "apply definition"},
        {"from": "Mapping evaluation", "to": f"{ans}: {reason}", "rule": "evaluation", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Recall that a function requires each input value to produce exactly one output value.",
        "Check whether any single input can produce more than one output (one-to-many fails).",
        f"Result: {ans}. {reason}",
        ["confuses_relation_with_function", "one_to_many_misconception"],
        marks=2,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_dependent_vs_independent_variable_identification"
    scenarios = [
        ("The total cost $C(m)$ of a taxi ride depends on the distance travelled in kilometres $m$.", "Distance travelled ($m$)", "Total cost ($C$)"),
        ("The height $h(t)$ of a plant measured in centimetres depends on time $t$ in weeks.", "Time in weeks ($t$)", "Height ($h$)"),
        ("The temperature $T(h)$ on Table Mountain depends on the altitude $h$ in metres above sea level.", "Altitude in metres ($h$)", "Temperature ($T$)"),
        ("The electrical energy cost $E(u)$ depends on the number of units consumed $u$ in kWh.", "Units consumed in kWh ($u$)", "Electrical energy cost ($E$)"),
    ]
    desc, indep, dep = rng.choice(scenarios)
    ask_indep = rng.choice([True, False])
    target = "independent variable (input)" if ask_indep else "dependent variable (output)"
    correct = indep if ask_indep else dep
    other = dep if ask_indep else indep
    opts = [correct, other, "Both variables are independent", "Neither variable is independent"]
    rng.shuffle(opts)
    prompt = f"In the relationship: \"{desc}\", identify the **{target}**."
    steps = [
        {"from": desc, "to": f"The independent variable is the input that changes freely ({indep}).", "rule": "independent variable", "op": "identify input"},
        {"from": "Dependent variable", "to": f"The dependent variable is the outcome ({dep}).", "rule": "dependent variable", "op": "identify output"},
        {"from": "Target", "to": f"Correct {target}: {correct}", "rule": "conclusion", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, correct, opts, steps,
        "The independent variable is the input (cause); the dependent variable is the output (effect).",
        "Ask: does cost depend on distance, or distance depend on cost?",
        f"The {target} is {correct}.",
        ["swaps_dependent_and_independent", "confuses_input_output"],
        marks=2,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_function_notation_eval_linear_integer"
    m = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    c = rng.choice([-8, -6, -4, -2, 3, 5, 7, 9])
    inp = rng.choice([-4, -3, -2, 2, 3, 4])
    ans_val = m * inp + c
    fn_latex = f"f(x) = {m}x {_signed(c)}"
    prompt = f"Given the linear function ${fn_latex}$, evaluate $f({inp})$."
    steps = [
        {"from": f"f({inp}) = {m}({inp}) {_signed(c)}", "to": f"f({inp}) = {m * inp} {_signed(c)}", "rule": "substitution", "op": f"substitute x = {inp}"},
        {"from": f"f({inp}) = {m * inp} {_signed(c)}", "to": f"f({inp}) = {ans_val}", "rule": "arithmetic", "op": "evaluate"},
    ]
    return _base_contract(
        sub, prompt, str(ans_val), None, steps,
        f"Substitute $x = {inp}$ directly into the function formula.",
        f"Multiply ${m} \\times ({inp})$, then add/subtract ${abs(c)}$.",
        f"Calculation: ${m}({inp}) {_signed(c)} = {m*inp} {_signed(c)} = {ans_val}$.",
        ["sign_error_multiplication", "order_of_operations_violation"],
        marks=2,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_function_notation_eval_linear_fraction"
    den = rng.choice([2, 3, 4, 5])
    m = den * rng.choice([-3, -2, -1, 1, 2, 3])
    c = rng.choice([-5, -2, 1, 4, 7])
    num_val = rng.choice([-3, -1, 1, 3])
    inp_frac = f"\\dfrac{{{num_val}}}{{{den}}}"
    ans_val = (m * num_val) // den + c
    prompt = f"Given $g(x) = {m}x {_signed(c)}$, calculate $g\\left({inp_frac}\\right)$."
    steps = [
        {"from": f"g\\left({inp_frac}\\right) = {m}\\left({inp_frac}\\right) {_signed(c)}", "to": f"g\\left({inp_frac}\\right) = {(m * num_val)//den} {_signed(c)}", "rule": "fraction multiplication", "op": "substitute"},
        {"from": f"{(m * num_val)//den} {_signed(c)}", "to": f"{ans_val}", "rule": "addition", "op": "simplify"},
    ]
    return _base_contract(
        sub, prompt, str(ans_val), None, steps,
        f"Replace $x$ with the fraction $\\dfrac{{{num_val}}}{{{den}}}$.",
        f"Notice that ${m}$ simplifies with the denominator ${den}$.",
        f"${m} \\times \\dfrac{{{num_val}}}{{{den}}} = {(m*num_val)//den}$, then add ${_signed(c)} = {ans_val}$.",
        ["fraction_multiplication_error", "sign_error"],
        marks=2,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_function_notation_eval_quadratic"
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    q = rng.choice([-9, -4, -1, 2, 5, 8])
    inp = rng.choice([-4, -3, -2, 2, 3, 4])
    ans_val = a * (inp ** 2) + q
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    prompt = f"Given the quadratic function $h(x) = {a_str}x^2 {_signed(q)}$, calculate $h({inp})$."
    steps = [
        {"from": f"h({inp}) = {a}({inp})^2 {_signed(q)}", "to": f"h({inp}) = {a}({inp**2}) {_signed(q)}", "rule": "exponentiation first", "op": "square input"},
        {"from": f"h({inp}) = {a * (inp**2)} {_signed(q)}", "to": f"h({inp}) = {ans_val}", "rule": "multiplication and addition", "op": "evaluate"},
    ]
    return _base_contract(
        sub, prompt, str(ans_val), None, steps,
        f"Substitute $x = {inp}$ and apply order of operations (square first, then multiply by {a}).",
        f"Remember that squaring any real number gives a positive result: $({inp})^2 = {inp**2}$.",
        f"${a}({inp**2}) {_signed(q)} = {a * (inp**2)} {_signed(q)} = {ans_val}$.",
        ["squares_negative_to_negative", "multiplies_before_squaring"],
        marks=2,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_function_notation_eval_hyperbola"
    a = rng.choice([-12, -8, -6, 6, 8, 12, 16])
    factors = [d for d in range(-6, 7) if d != 0 and a % d == 0]
    inp = rng.choice(factors)
    q = rng.choice([-5, -3, -1, 2, 4, 7])
    ans_val = (a // inp) + q
    prompt = f"Given the hyperbolic function $f(x) = \\dfrac{{{a}}}{{x}} {_signed(q)}$, evaluate $f({inp})$."
    steps = [
        {"from": f"f({inp}) = \\dfrac{{{a}}}{{{inp}}} {_signed(q)}", "to": f"f({inp}) = {a // inp} {_signed(q)}", "rule": "division", "op": "substitute"},
        {"from": f"f({inp}) = {a // inp} {_signed(q)}", "to": f"f({inp}) = {ans_val}", "rule": "arithmetic", "op": "evaluate"},
    ]
    return _base_contract(
        sub, prompt, str(ans_val), None, steps,
        f"Substitute $x = {inp}$ into the denominator of $\\dfrac{{{a}}}{{x}}$.",
        f"Divide: $\\dfrac{{{a}}}{{{inp}}} = {a // inp}$, then add ${_signed(q)}$.",
        f"${a // inp} {_signed(q)} = {ans_val}$.",
        ["division_sign_error", "treats_hyperbola_as_linear"],
        marks=2,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_function_notation_eval_exponential"
    b = rng.choice([2, 3])
    a = rng.choice([-2, -1, 1, 2])
    q = rng.choice([-4, -2, 1, 3, 5])
    inp = rng.choice([-1, 0, 1, 2, 3])
    if inp >= 0:
        ans_val = a * (b ** inp) + q
        ans_str = str(ans_val)
    else:
        # negative exponent b^-1 = 1/b
        num_res = a + q * b
        ans_str = f"\\dfrac{{{num_res}}}{{{b}}}" if num_res % b != 0 else str(num_res // b)
    a_str = "" if a == 1 else ("-" if a == -1 else f"{a} \\cdot ")
    prompt = f"Given the exponential function $g(x) = {a_str}{b}^x {_signed(q)}$, evaluate $g({inp})$."
    b_pow = f"\\dfrac{{1}}{{{b}}}" if inp == -1 else str(b ** inp)
    steps = [
        {"from": f"g({inp}) = {a} \\cdot ({b}^{{{inp}}}) {_signed(q)}", "to": f"g({inp}) = {a} \\cdot ({b_pow}) {_signed(q)}", "rule": "evaluate power", "op": "power evaluation"},
        {"from": f"g({inp}) = {ans_str}", "to": f"g({inp}) = {ans_str}", "rule": "simplification", "op": "simplify"},
    ]
    return _base_contract(
        sub, prompt, ans_str, None, steps,
        f"Calculate ${b}^{{{inp}}}$ first, then multiply by ${a}$, then add ${q}$.",
        f"Recall laws of exponents: $b^0 = 1$ and $b^{{-1}} = \\dfrac{{1}}{{b}}$.",
        f"Result: $g({inp}) = {ans_str}$.",
        ["multiplies_base_before_exponent", "exponent_zero_misconception"],
        marks=2,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_function_notation_solve_linear_input"
    m = rng.choice([-4, -3, -2, 2, 3, 4, 5])
    target_x = rng.choice([-6, -5, -3, -1, 2, 4, 7])
    c = rng.choice([-7, -4, -2, 3, 5, 8])
    k = m * target_x + c
    prompt = f"Given $f(x) = {m}x {_signed(c)}$, solve for $x$ if $f(x) = {k}$."
    steps = [
        {"from": f"{m}x {_signed(c)} = {k}", "to": f"{m}x = {k - c}", "rule": "additive inverse", "op": f"subtract {c}"},
        {"from": f"{m}x = {k - c}", "to": f"x = {target_x}", "rule": "multiplicative inverse", "op": f"divide by {m}"},
    ]
    return _base_contract(
        sub, prompt, str(target_x), None, steps,
        f"Set the function expression equal to ${k}$: ${m}x {_signed(c)} = {k}$.",
        f"Isolate $x$: subtract ${c}$ from both sides, then divide by ${m}$.",
        f"${m}x = {k - c} \\implies x = {target_x}$.",
        ["substitutes_k_for_x_instead_of_f(x)", "sign_error_isolation"],
        marks=2,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_function_notation_solve_quadratic_input"
    a = rng.choice([1, 2, 3])
    root = rng.choice([2, 3, 4, 5])
    q = rng.choice([-20, -16, -12, -8, -4])
    k = a * (root ** 2) + q
    a_str = "" if a == 1 else str(a)
    prompt = f"Given $h(x) = {a_str}x^2 {_signed(q)}$, find all values of $x$ for which $h(x) = {k}$."
    ans = f"\\pm {root}"
    opts = [f"\\pm {root}", f"{root}", f"-{root}", f"\\pm {root**2}"]
    rng.shuffle(opts)
    steps = [
        {"from": f"{a_str}x^2 {_signed(q)} = {k}", "to": f"{a_str}x^2 = {k - q}", "rule": "isolate squared term", "op": f"add {-q}"},
        {"from": f"x^2 = {(k - q)//a}", "to": f"x = \\pm {root}", "rule": "square root property", "op": "take square root"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        f"Equate ${a_str}x^2 {_signed(q)} = {k}$ and solve for $x^2$.",
        f"Remember that taking the square root yields both positive and negative solutions: $x = \\pm\\sqrt{{...}}$.",
        f"$x^2 = {(k-q)//a} \\implies x = \\pm {root}$.",
        ["forgets_negative_square_root", "square_root_arithmetic_error"],
        marks=2,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_function_notation_solve_hyperbola_input"
    a = rng.choice([-12, -8, 6, 8, 12, 16])
    target_x = rng.choice([-4, -2, 2, 4])
    q = rng.choice([-3, -1, 1, 3, 5])
    k = (a // target_x) + q
    prompt = f"Given $f(x) = \\dfrac{{{a}}}{{x}} {_signed(q)}$, find the value of $x$ for which $f(x) = {k}$."
    steps = [
        {"from": f"\\dfrac{{{a}}}{{x}} {_signed(q)} = {k}", "to": f"\\dfrac{{{a}}}{{x}} = {k - q}", "rule": "isolate fraction", "op": f"subtract {q}"},
        {"from": f"\\dfrac{{{a}}}{{x}} = {k - q}", "to": f"x = \\dfrac{{{a}}}{{{k - q}}} = {target_x}", "rule": "reciprocal/solve for x", "op": "solve for x"},
    ]
    return _base_contract(
        sub, prompt, str(target_x), None, steps,
        f"Set $\\dfrac{{{a}}}{{x}} {_signed(q)} = {k}$ and isolate $\\dfrac{{{a}}}{{x}}$.",
        f"Subtract ${q}$ from both sides to get $\\dfrac{{{a}}}{{x}} = {k - q}$, then multiply by $x$.",
        f"$x = \\dfrac{{{a}}}{{{k-q}}} = {target_x}$.",
        ["multiplies_only_one_side_by_x", "sign_error_isolation"],
        marks=2,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_function_notation_solve_exponential_input"
    b = rng.choice([2, 3])
    target_x = rng.choice([1, 2, 3, 4])
    a = rng.choice([1, 2])
    q = rng.choice([-5, -1, 2, 4])
    k = a * (b ** target_x) + q
    a_str = "" if a == 1 else f"{a} \\cdot "
    prompt = f"Given $g(x) = {a_str}{b}^x {_signed(q)}$, solve for $x$ if $g(x) = {k}$."
    steps = [
        {"from": f"{a_str}{b}^x {_signed(q)} = {k}", "to": f"{a_str}{b}^x = {k - q}", "rule": "isolate exponential term", "op": f"subtract {q}"},
        {"from": f"{b}^x = {(k - q)//a}", "to": f"{b}^x = {b}^{{{target_x}}} \\implies x = {target_x}", "rule": "equate exponents with same base", "op": "solve for x"},
    ]
    return _base_contract(
        sub, prompt, str(target_x), None, steps,
        f"Isolate the power ${b}^x$: subtract ${q}$, then divide by ${a}$.",
        f"Express ${(k-q)//a}$ as a power of base ${b}$, then equate the exponents.",
        f"${b}^x = {b}^{{{target_x}}} \\implies x = {target_x}$.",
        ["multiplies_a_into_base", "forgets_exponent_equality_rule"],
        marks=2,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_linear_gradient_and_direction"
    x1, y1 = rng.choice([(1, 2), (-2, 3), (0, -4), (3, 1), (-1, -3)])
    dx = rng.choice([1, 2, 3, 4])
    dy = rng.choice([-6, -4, -3, -2, 2, 3, 4, 6])
    x2 = x1 + dx
    y2 = y1 + dy
    g = math.gcd(abs(dy), dx)
    num_m = dy // g
    den_m = dx // g
    m_str = str(num_m) if den_m == 1 else f"\\dfrac{{{num_m}}}{{{den_m}}}"
    direction = "increasing (sloping upwards)" if num_m > 0 else "decreasing (sloping downwards)"
    prompt = f"Calculate the gradient $m$ of the straight line passing through $A{_coord(x1, y1)}$ and $B{_coord(x2, y2)}$, and state whether the line is increasing or decreasing."
    ans = f"m = {m_str}; \\text{{ {direction} }}"
    steps = [
        {"from": f"m = \\dfrac{{y_2 - y_1}}{{x_2 - x_1}}", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}}", "rule": "gradient formula", "op": "substitute"},
        {"from": f"m = \\dfrac{{{dy}}}{{{dx}}}", "to": f"m = {m_str}", "rule": "simplification", "op": "simplify fraction"},
        {"from": f"m = {m_str}", "to": direction, "rule": "gradient sign interpretation", "op": "interpret direction"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply the gradient formula: $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.",
        "If $m > 0$, the line rises from left to right (increasing); if $m < 0$, it falls (decreasing).",
        f"Gradient: $\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}} = {m_str}$, which is {direction}.",
        ["inverted_gradient_delta_x_over_delta_y", "sign_error_gradient"],
        marks=3,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_linear_dual_intercepts"
    m = rng.choice([-4, -3, -2, 2, 3, 4])
    c = m * rng.choice([-4, -3, -2, 2, 3, 4])
    # y = mx + c -> x-int at y=0: x = -c/m
    x_int = -c // m
    y_int = c
    prompt = f"Determine the $x$- and $y$-intercepts of the line $y = {m}x {_signed(c)}$ as coordinate points."
    ans = f"x\\text{{-int: }} {_coord(x_int, 0)};\\, y\\text{{-int: }} {_coord(0, y_int)}"
    steps = [
        {"from": "y-intercept: let x = 0", "to": f"y = {m}(0) {_signed(c)} = {y_int} \\implies {_coord(0, y_int)}", "rule": "y-intercept rule", "op": "set x = 0"},
        {"from": "x-intercept: let y = 0", "to": f"0 = {m}x {_signed(c)} \\implies {m}x = {-c} \\implies x = {x_int} \\implies {_coord(x_int, 0)}", "rule": "x-intercept rule", "op": "set y = 0"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "To find the $y$-intercept, set $x = 0$. To find the $x$-intercept, set $y = 0$.",
        "Always express intercepts as ordered coordinate pairs: $(x; 0)$ and $(0; y)$.",
        f"$x$-intercept: ${m}x {_signed(c)} = 0 \\implies x = {x_int}$; $y$-intercept: $y = {y_int}$.",
        ["swaps_x_and_y_intercepts", "writes_single_numbers_instead_of_coordinates"],
        marks=3,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_linear_equation_from_two_points"
    m = rng.choice([-3, -2, -1, 1, 2, 3])
    c = rng.choice([-5, -3, -1, 2, 4, 6])
    x1 = rng.choice([-3, -2, -1, 1])
    y1 = m * x1 + c
    x2 = x1 + rng.choice([2, 3, 4])
    y2 = m * x2 + c
    m_str = "" if m == 1 else ("-" if m == -1 else str(m))
    eq = f"y = {m_str}x {_signed(c)}"
    prompt = f"Determine the equation of the straight line passing through points $P{_coord(x1, y1)}$ and $Q{_coord(x2, y2)}$ in the form $y = mx + c$."
    steps = [
        {"from": "Calculate gradient m", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{{y2-y1}}}{{{x2-x1}}} = {m}", "rule": "gradient formula", "op": "compute m"},
        {"from": "Substitute point to find c", "to": f"{y1} = {m}({x1}) + c \\implies c = {c}", "rule": "solve for c", "op": "compute c"},
        {"from": "Formulate equation", "to": eq, "rule": "standard form y = mx + c", "op": "write equation"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        "First find the gradient $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.",
        "Then substitute either point into $y = mx + c$ to solve for $c$.",
        f"$m = {m}$, substituting ${_coord(x1, y1)}$ gives $c = {c}$, so ${eq}$.",
        ["gradient_formula_error", "substitutes_x_and_y_inverted"],
        marks=3,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_linear_equation_from_gradient_and_point"
    m = rng.choice([-4, -3, -2, 2, 3, 4])
    x0 = rng.choice([-4, -2, 1, 3, 5])
    c = rng.choice([-6, -3, 1, 4, 7])
    y0 = m * x0 + c
    m_str = str(m)
    eq = f"y = {m_str}x {_signed(c)}"
    prompt = f"Find the equation of the line with gradient $m = {m}$ that passes through the point $A{_coord(x0, y0)}$."
    steps = [
        {"from": "Substitute gradient into y = mx + c", "to": f"y = {m}x + c", "rule": "linear form", "op": "substitute m"},
        {"from": f"Substitute point {_coord(x0, y0)}", "to": f"{y0} = {m}({x0}) + c \\implies c = {y0} - ({m*x0}) = {c}", "rule": "solve for c", "op": "isolate c"},
        {"from": "Final equation", "to": eq, "rule": "equation synthesis", "op": "write equation"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        "Use the point-gradient formula $y - y_1 = m(x - x_1)$ or substitute $(x_0; y_0)$ into $y = mx + c$.",
        f"Substitute $x = {x0}$ and $y = {y0}$ into $y = {m}x + c$ and solve for $c$.",
        f"${y0} = {m}({x0}) + c \\implies c = {c}$, so ${eq}$.",
        ["sign_error_isolating_c", "swaps_x_and_y_in_substitution"],
        marks=2,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_linear_parallel_and_perpendicular_lines"
    is_parallel = rng.choice([True, False])
    m_base = rng.choice([-3, -2, 2, 3])
    c_base = rng.choice([-4, -1, 3, 5])
    xp = rng.choice([-3, -1, 2, 4])
    if is_parallel:
        rel_word = "parallel"
        m_target = m_base
        c_target = rng.choice([c for c in range(-6, 7) if c != c_base])
        yp = m_target * xp + c_target
        ans_eq = f"y = {m_target}x {_signed(c_target)}"
        rel_rule = "Parallel lines have equal gradients: $m_1 = m_2$."
    else:
        rel_word = "perpendicular"
        # perpendicular gradient: m2 = -1/m1
        m_target_num = -1
        m_target_den = m_base
        if m_target_den < 0:
            m_target_num = 1
            m_target_den = -m_target_den
        c_target = rng.choice([-4, -2, 1, 3, 5])
        # choose xp as multiple of m_target_den
        xp = m_target_den * rng.choice([-2, -1, 1, 2])
        yp = (m_target_num * xp) // m_target_den + c_target
        ans_eq = f"y = \\dfrac{{{m_target_num}}}{{{m_target_den}}}x {_signed(c_target)}"
        rel_rule = "Perpendicular lines have gradients whose product is $-1$: $m_1 \\times m_2 = -1$."

    prompt = f"Determine the equation of the line that is **{rel_word}** to the line $y = {m_base}x {_signed(c_base)}$ and passes through the point $P{_coord(xp, yp)}$."
    steps = [
        {"from": f"Identify required gradient ({rel_word})", "to": rel_rule, "rule": f"{rel_word} condition", "op": "find gradient"},
        {"from": "Substitute point to find c", "to": f"{yp} = m({xp}) + c \\implies c = {c_target}", "rule": "solve for c", "op": "substitute point"},
        {"from": "Formulate equation", "to": ans_eq, "rule": "equation synthesis", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans_eq, None, steps,
        f"Recall the condition for {rel_word} lines: {rel_rule}",
        f"Once you have the new gradient, use $y - y_1 = m(x - x_1)$ with $P{_coord(xp, yp)}$.",
        f"The resulting equation is ${ans_eq}$.",
        ["confuses_parallel_and_perpendicular_gradient", "forgets_negative_reciprocal"],
        marks=3,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_linear_horizontal_and_vertical_lines"
    is_horiz = rng.choice([True, False])
    xp = rng.choice([-7, -5, -2, 3, 6, 8])
    yp = rng.choice([-8, -4, -1, 2, 5, 9])
    if is_horiz:
        line_type = "horizontal"
        ans_eq = f"y = {yp}"
        wrong1 = f"x = {xp}"
        wrong2 = f"y = {xp}"
        wrong3 = f"x = {yp}"
        explanation = f"A horizontal line has gradient $m = 0$, so its equation is $y = c$. Since it passes through ${_coord(xp, yp)}$, $y = {yp}$."
    else:
        line_type = "vertical"
        ans_eq = f"x = {xp}"
        wrong1 = f"y = {yp}"
        wrong2 = f"x = {yp}"
        wrong3 = f"y = {xp}"
        explanation = f"A vertical line has an undefined gradient, so its equation is $x = k$. Since it passes through ${_coord(xp, yp)}$, $x = {xp}$."

    opts = [ans_eq, wrong1, wrong2, wrong3]
    rng.shuffle(opts)
    prompt = f"State the equation of the **{line_type}** straight line passing through the point $T{_coord(xp, yp)}$."
    steps = [
        {"from": f"{line_type} line through {_coord(xp, yp)}", "to": explanation, "rule": f"{line_type} line rule", "op": "apply rule"},
        {"from": "Equation", "to": ans_eq, "rule": "conclude", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, ans_eq, opts, steps,
        f"Horizontal lines have equations in the form $y = c$; vertical lines have equations in the form $x = k$.",
        f"Check which coordinate remains constant for all points on a {line_type} line.",
        f"Correct equation: ${ans_eq}$.",
        ["swaps_x_and_y_for_horizontal_vertical", "attempts_to_calculate_nonzero_gradient"],
        marks=2,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_linear_domain_and_range_intervals"
    m = rng.choice([2, 3, -2, -3])
    c = rng.choice([-2, 1, 3])
    x_min = rng.choice([-4, -3, -2])
    x_max = x_min + rng.choice([4, 5, 6])
    y_at_min = m * x_min + c
    y_at_max = m * x_max + c
    y_min = min(y_at_min, y_at_max)
    y_max = max(y_at_min, y_at_max)
    dom_str = f"[{x_min};\\, {x_max}]"
    ran_str = f"[{y_min};\\, {y_max}]"
    ask_domain = rng.choice([True, False])
    target = "domain" if ask_domain else "range"
    correct = dom_str if ask_domain else ran_str
    distractor = ran_str if ask_domain else dom_str
    opts = [
        correct,
        distractor,
        f"({x_min};\\, {x_max})" if ask_domain else f"({y_min};\\, {y_max})",
        "\\{x: x \\in \\mathbb{R}\\}" if ask_domain else "\\{y: y \\in \\mathbb{R}\\}",
    ]
    rng.shuffle(opts)
    prompt = f"A linear line segment is defined by $f(x) = {m}x {_signed(c)}$ for $x \\in [{x_min};\\, {x_max}]$. State the **{target}** of this function in interval notation."
    steps = [
        {"from": f"Domain of segment: x in [{x_min}; {x_max}]", "to": f"Domain = {dom_str}", "rule": "domain definition", "op": "read x-interval"},
        {"from": f"Evaluate endpoints: f({x_min}) = {y_at_min}, f({x_max}) = {y_at_max}", "to": f"Range = [{y_min}; {y_max}]", "rule": "range evaluation", "op": "evaluate y-interval"},
        {"from": f"Target: {target}", "to": correct, "rule": "conclude", "op": "select target"},
    ]
    return _base_contract(
        sub, prompt, correct, opts, steps,
        "Domain refers to all valid $x$-inputs; range refers to all corresponding $y$-outputs.",
        "For a restricted linear segment, substitute both $x$-endpoints to find the minimum and maximum $y$-values.",
        f"The {target} is ${correct}$.",
        ["swaps_domain_and_range", "uses_open_brackets_instead_of_closed"],
        marks=2,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_quadratic_turning_point_and_axis_of_symmetry"
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    q = rng.choice([-8, -5, -3, 2, 4, 7])
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    prompt = f"Given the parabola $f(x) = {a_str}x^2 {_signed(q)}$, state the coordinates of its turning point and the equation of its axis of symmetry."
    tp = f"(0;\\, {q})"
    sym = "x = 0"
    ans = f"\\text{{Turning point: }} {tp};\\, \\text{{Axis of symmetry: }} {sym}"
    steps = [
        {"from": f"f(x) = {a_str}x^2 {_signed(q)}", "to": f"For y = ax^2 + q, turning point is at x = 0 with y = q.", "rule": "turning point formula", "op": "identify vertex"},
        {"from": "Turning point", "to": f"{tp}", "rule": "coordinate pair", "op": "write coordinates"},
        {"from": "Axis of symmetry", "to": f"The vertical line through the turning point is {sym}.", "rule": "axis of symmetry", "op": "write axis"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "In Grade 10, parabolas of the form $y = ax^2 + q$ always have their axis of symmetry on the $y$-axis ($x = 0$).",
        "The turning point (vertex) is always at $(0; q)$.",
        f"Turning point: ${tp}$; Axis of symmetry: ${sym}$.",
        ["confuses_axis_of_symmetry_as_y_equals_0", "swaps_coordinates_of_turning_point"],
        marks=2,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_quadratic_effect_of_parameter_a"
    a = rng.choice([-4, -2, -0.5, 0.5, 2, 4])
    is_neg = a < 0
    is_stretch = abs(a) > 1
    shape_desc = "concave down (maximum turning point, opens downwards)" if is_neg else "concave up (minimum turning point, opens upwards)"
    width_desc = "narrower / steeper (vertically stretched)" if is_stretch else "wider / flatter (vertically compressed)"
    prompt = f"Describe the geometric effects of the parameter $a = {_fmt_num(a)}$ on the parabola $y = ax^2$ compared to the standard base function $y = x^2$."
    ans = f"{shape_desc}; {width_desc}"
    opts = [
        ans,
        f"{'concave up' if is_neg else 'concave down'}; {width_desc}",
        f"{shape_desc}; {'wider' if is_stretch else 'narrower'}",
        "Shifted vertically upwards by $a$ units",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Sign of a = {_fmt_num(a)}", "to": f"a < 0 reflects across x-axis: {shape_desc}", "rule": "reflection rule", "op": "analyze sign"},
        {"from": f"Magnitude |a| = {_fmt_num(abs(a))}", "to": f"|a| > 1 narrows the curve; |a| < 1 widens: {width_desc}", "rule": "stretch rule", "op": "analyze magnitude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The sign of $a$ determines curvature: $a > 0$ opens upwards; $a < 0$ opens downwards.",
        "The magnitude $|a|$ determines steepness: $|a| > 1$ is narrower; $0 < |a| < 1$ is wider.",
        f"Effects: {ans}.",
        ["confuses_parameter_a_with_vertical_shift", "misinterprets_reflection"],
        marks=2,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_quadratic_effect_of_parameter_q"
    q = rng.choice([-6, -5, -3, 3, 5, 7])
    a = rng.choice([-2, 2])
    direction = "upwards" if q > 0 else "downwards"
    extrema = "minimum" if a > 0 else "maximum"
    prompt = f"For the parabola $f(x) = {a}x^2 {_signed(q)}$, describe the vertical transformation caused by $q = {q}$ relative to $y = {a}x^2$, and state the {extrema} value of $f(x)$."
    ans = f"Shifted {abs(q)} units {direction}; {extrema} value is y = {q}"
    opts = [
        ans,
        f"Shifted {abs(q)} units {'downwards' if q > 0 else 'upwards'}; {extrema} value is y = {q}",
        f"Shifted {abs(q)} units {direction}; {'maximum' if a > 0 else 'minimum'} value is y = {q}",
        f"Shifted horizontally by {abs(q)} units",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Parameter q = {q}", "to": f"Vertical shift {abs(q)} units {direction}.", "rule": "vertical translation", "op": "shift"},
        {"from": f"Turning point at (0; {q})", "to": f"Since a = {a} ({'opens up' if a>0 else 'opens down'}), the {extrema} value is y = {q}.", "rule": "extrema rule", "op": "find extrema"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The parameter $q$ shifts the entire parabola vertically: $+q$ shifts up, $-q$ shifts down.",
        "The $y$-value of the turning point is the maximum (if $a < 0$) or minimum (if $a > 0$) of the function.",
        f"Transformation: {ans}.",
        ["confuses_vertical_with_horizontal_shift", "swaps_minimum_and_maximum"],
        marks=2,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_quadratic_x_and_y_intercepts"
    # Choose a and q such that -q/a is a positive perfect square
    root = rng.choice([2, 3, 4, 5])
    a = rng.choice([1, 2, -1, -2])
    q = -a * (root ** 2)
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    prompt = f"Calculate the $x$-intercepts and $y$-intercept of the parabola $y = {a_str}x^2 {_signed(q)}$. Write all intercepts as coordinate points."
    ans = f"x\\text{{-intercepts: }} {_coord(-root, 0)} \\text{{ and }} {_coord(root, 0)};\\, y\\text{{-intercept: }} {_coord(0, q)}"
    steps = [
        {"from": "y-intercept: let x = 0", "to": f"y = {a}(0)^2 {_signed(q)} = {q} \\implies {_coord(0, q)}", "rule": "y-intercept rule", "op": "set x = 0"},
        {"from": "x-intercepts: let y = 0", "to": f"{a_str}x^2 {_signed(q)} = 0 \\implies x^2 = {root**2} \\implies x = \\pm {root}", "rule": "solve quadratic", "op": "set y = 0"},
        {"from": "Coordinate points", "to": ans, "rule": "coordinate synthesis", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "For $y$-intercept, set $x = 0$. For $x$-intercepts, set $y = 0$ and solve $ax^2 + q = 0$.",
        f"Isolate $x^2 = \\dfrac{{-q}}{{a}} = {root**2}$, giving $x = \\pm {root}$.",
        f"Points: $x$-intercepts at $(\\pm {root}; 0)$, $y$-intercept at $(0; {q})$.",
        ["forgets_plus_minus_on_x_intercepts", "swaps_x_and_y_coordinates"],
        marks=3,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_quadratic_domain_and_range"
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    q = rng.choice([-7, -4, -1, 2, 5, 8])
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    dom = "\\{x: x \\in \\mathbb{R}\\}"
    if a > 0:
        ran = f"[{q};\\, \\infty)"
        dist = f"(-\\infty;\\, {q}]"
    else:
        ran = f"(-\\infty;\\, {q}]"
        dist = f"[{q};\\, \\infty)"
    prompt = f"State the **domain** and **range** of the parabola $f(x) = {a_str}x^2 {_signed(q)}$."
    ans = f"\\text{{Domain: }} {dom};\\, \\text{{Range: }} {ran}"
    opts = [
        ans,
        f"\\text{{Domain: }} {dom};\\, \\text{{Range: }} {dist}",
        f"\\text{{Domain: }} {ran};\\, \\text{{Range: }} {dom}",
        f"\\text{{Domain: }} [{q}; \\infty);\\, \\text{{Range: }} \\{{y: y \\neq {q}\\}}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Domain of any quadratic function", "to": "x can take any real value: domain is all real numbers x in R.", "rule": "domain rule", "op": "identify domain"},
        {"from": f"Parabola opens {'upwards (a > 0)' if a > 0 else 'downwards (a < 0)'}", "to": f"Turning point y-value is {q}, so range is {ran}.", "rule": "range rule", "op": "identify range"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The domain of every quadratic function is all real numbers: $x \\in \\mathbb{R}$.",
        f"If $a > 0$, the parabola has a minimum at $y = q$ (range $[q; \\infty)$). If $a < 0$, it has a maximum at $y = q$ (range $(-\\infty; q]$).",
        f"Domain: ${dom}$; Range: ${ran}$.",
        ["swaps_domain_and_range", "inverts_range_interval_direction"],
        marks=2,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_quadratic_equation_from_turning_point_and_point"
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    q = rng.choice([-6, -3, 1, 4])
    x1 = rng.choice([1, 2, 3])
    y1 = a * (x1 ** 2) + q
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    eq = f"y = {a_str}x^2 {_signed(q)}"
    # Build clean SVG sketch of the parabola with turning point and given point
    elements = [
        f'<circle cx="{200}" cy="{150 - q*8}" r="4" class="dot" />',
        f'<text x="{208}" y="{150 - q*8 + 4}" class="label">(0; {q})</text>',
        f'<circle cx="{200 + x1*12}" cy="{150 - y1*8}" r="4" class="dot" />',
        f'<text x="{208 + x1*12}" y="{150 - y1*8 + 4}" class="label">P({x1}; {y1})</text>',
    ]
    diag = {
        "kind": "inline_svg",
        "svg": _make_svg_axes_frame(elements),
        "diagram_role": "context",
        "caption": f"Parabola with vertex at (0; {q}) passing through P({x1}; {y1}).",
    }
    prompt = f"The sketch shows a parabola with turning point at $(0; {q})$ that passes through the point $P{_coord(x1, y1)}$. Determine its equation in the form $y = ax^2 + q$."
    steps = [
        {"from": f"Turning point is (0; {q})", "to": f"Therefore q = {q}, so y = ax^2 {_signed(q)}", "rule": "substitute q", "op": "identify q"},
        {"from": f"Substitute point P{_coord(x1, y1)}", "to": f"{y1} = a({x1})^2 {_signed(q)} \\implies {a * (x1**2)} = a({x1**2}) \\implies a = {a}", "rule": "solve for a", "op": "substitute point"},
        {"from": "Write final equation", "to": eq, "rule": "equation synthesis", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        "The turning point $(0; q)$ immediately gives the parameter $q$.",
        f"Substitute the coordinates $x = {x1}$ and $y = {y1}$ into $y = ax^2 {_signed(q)}$ to solve for $a$.",
        f"${y1} = a({x1}^2) {_signed(q)} \\implies a = {a}$, so ${eq}$.",
        ["sign_error_solving_for_a", "forgets_to_square_x_coordinate"],
        marks=3,
        diagram_spec=diag,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_quadratic_intervals_of_increase_and_decrease"
    a = rng.choice([-2, 2])
    q = rng.choice([-4, 1, 5])
    ask_increasing = rng.choice([True, False])
    target = "increasing" if ask_increasing else "decreasing"
    if a > 0:
        # Parabola opens upwards: decreases for x < 0, increases for x > 0
        inc_interval = "x > 0 \\text{ (or } (0;\\, \\infty)\\text{)}"
        dec_interval = "x < 0 \\text{ (or } (-\\infty;\\, 0)\\text{)}"
    else:
        # Parabola opens downwards: increases for x < 0, decreases for x > 0
        inc_interval = "x < 0 \\text{ (or } (-\\infty;\\, 0)\\text{)}"
        dec_interval = "x > 0 \\text{ (or } (0;\\, \\infty)\\text{)}"
    correct = inc_interval if ask_increasing else dec_interval
    wrong = dec_interval if ask_increasing else inc_interval
    opts = [
        correct,
        wrong,
        f"x > {q} \\text{{ (or }} ({q};\\, \\infty)\\text{{)}}",
        "\\{x: x \\in \\mathbb{R}\\}",
    ]
    rng.shuffle(opts)
    a_str = f"{a}"
    prompt = f"For the parabola $f(x) = {a_str}x^2 {_signed(q)}$, determine the interval of $x$ for which the function is **{target}**."
    steps = [
        {"from": f"Parabola f(x) = {a_str}x^2 {_signed(q)}", "to": f"Axis of symmetry is at x = 0; curve opens {'upwards (minimum at x = 0)' if a>0 else 'downwards (maximum at x = 0)'}.", "rule": "symmetry and turning point", "op": "analyze curvature"},
        {"from": f"Target: {target}", "to": f"The function is {target} on {correct}.", "rule": "interval of increase/decrease", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, correct, opts, steps,
        "A function is increasing where the graph slopes upwards from left to right, and decreasing where it slopes downwards.",
        "The turning point (at $x = 0$) is where the curve changes from increasing to decreasing (or vice versa).",
        f"The function is {target} on ${correct}$.",
        ["uses_y_coordinate_instead_of_x_for_interval", "inverts_increasing_decreasing"],
        marks=2,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_concept_function_definition_and_relation_test": _build_01,
    "02_dependent_vs_independent_variable_identification": _build_02,
    "03_function_notation_eval_linear_integer": _build_03,
    "04_function_notation_eval_linear_fraction": _build_04,
    "05_function_notation_eval_quadratic": _build_05,
    "06_function_notation_eval_hyperbola": _build_06,
    "07_function_notation_eval_exponential": _build_07,
    "08_function_notation_solve_linear_input": _build_08,
    "09_function_notation_solve_quadratic_input": _build_09,
    "10_function_notation_solve_hyperbola_input": _build_10,
    "11_function_notation_solve_exponential_input": _build_11,
    "12_linear_gradient_and_direction": _build_12,
    "13_linear_dual_intercepts": _build_13,
    "14_linear_equation_from_two_points": _build_14,
    "15_linear_equation_from_gradient_and_point": _build_15,
    "16_linear_parallel_and_perpendicular_lines": _build_16,
    "17_linear_horizontal_and_vertical_lines": _build_17,
    "18_linear_domain_and_range_intervals": _build_18,
    "19_quadratic_turning_point_and_axis_of_symmetry": _build_19,
    "20_quadratic_effect_of_parameter_a": _build_20,
    "21_quadratic_effect_of_parameter_q": _build_21,
    "22_quadratic_x_and_y_intercepts": _build_22,
    "23_quadratic_domain_and_range": _build_23,
    "24_quadratic_equation_from_turning_point_and_point": _build_24,
    "25_quadratic_intervals_of_increase_and_decrease": _build_25,
}
