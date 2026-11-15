"""Grade 10 Mathematics — Term 2 — Functions Archetypes 26 to 50.

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Functions syllabus.
Covers:
- Hyperbola f(x) = a/x + q: asymptotes, axes of symmetry, branches, intercepts, equation from point
- Exponential f(x) = a*b^x + q: asymptote, y-intercept, growth/decay, range, equation from point
- Trigonometric functions: sine, cosine, tangent (amplitude, period, asymptotes, max/min, equations)
- Graph intersections, graphical inequalities, vertical distance between curves
- Function transformations (reflections in axes, vertical translations) and contextual models

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .functions_archetypes_01_25 import (
    TERM,
    CAPS_WEIGHT,
    SUGGESTED_DURATION,
    TOPIC_ID,
    LEARNING_OBJECTIVE,
    _fmt_num,
    _coord,
    _signed,
    _make_svg_axes_frame,
    _base_contract,
)


def _build_26(rng: random.Random) -> Dict[str, Any]:
    sub = "26_hyperbola_vertical_and_horizontal_asymptotes"
    a = rng.choice([-8, -6, -4, 4, 6, 8])
    q = rng.choice([-5, -3, -2, 1, 3, 5])
    prompt = f"State the equations of the **vertical** and **horizontal asymptotes** of the hyperbola $f(x) = \\dfrac{{{a}}}{{x}} {_signed(q)}$."
    va = "x = 0"
    ha = f"y = {q}"
    ans = f"\\text{{Vertical asymptote: }} {va};\\, \\text{{Horizontal asymptote: }} {ha}"
    opts = [
        ans,
        f"\\text{{Vertical asymptote: }} y = 0;\\, \\text{{Horizontal asymptote: }} x = {q}",
        f"\\text{{Vertical asymptote: }} x = {q};\\, \\text{{Horizontal asymptote: }} y = 0",
        f"\\text{{Vertical asymptote: }} {va};\\, \\text{{Horizontal asymptote: }} y = {a}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Denominator cannot be zero: x != 0", "to": f"Vertical asymptote is {va} (the y-axis).", "rule": "vertical asymptote", "op": "denominator undefined"},
        {"from": f"As x approaches +/- infinity, {a}/x approaches 0", "to": f"Horizontal asymptote is {ha}.", "rule": "horizontal asymptote", "op": "limit as x -> inf"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "In Grade 10, the vertical asymptote of $y = \\dfrac{a}{x} + q$ is always the line $x = 0$.",
        "The horizontal asymptote is determined by the vertical shift: $y = q$.",
        f"Vertical asymptote: ${va}$; Horizontal asymptote: ${ha}$.",
        ["swaps_vertical_and_horizontal_asymptotes", "confuses_a_with_horizontal_asymptote"],
        marks=2,
    )


def _build_27(rng: random.Random) -> Dict[str, Any]:
    sub = "27_hyperbola_axes_of_symmetry"
    a = rng.choice([-10, -5, 5, 10])
    q = rng.choice([-4, -2, 1, 3, 6])
    axis1 = f"y = x {_signed(q)}"
    axis2 = f"y = -x {_signed(q)}"
    ans = f"{axis1} \\text{{ and }} {axis2}"
    opts = [
        ans,
        f"y = x \\text{{ and }} y = -x",
        f"x = {q} \\text{{ and }} y = {q}",
        f"y = x {_signed(-q)} \\text{{ and }} y = -x {_signed(-q)}",
    ]
    rng.shuffle(opts)
    prompt = f"Determine the equations of the two **axes of symmetry** for the hyperbola $f(x) = \\dfrac{{{a}}}{{x}} {_signed(q)}$."
    steps = [
        {"from": "Standard axes of symmetry for y = a/x", "to": "y = x and y = -x (gradients +1 and -1)", "rule": "symmetry lines", "op": "parent symmetry"},
        {"from": f"Shift vertically by q = {q}", "to": f"Axes are shifted by q: {ans}", "rule": "translation of symmetry", "op": "apply shift"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The axes of symmetry of a hyperbola have gradients $m = 1$ and $m = -1$.",
        f"Both lines pass through the intersection of the asymptotes $(0; {q})$, giving $y = x + q$ and $y = -x + q$.",
        f"Equations: ${ans}$.",
        ["forgets_vertical_shift_in_symmetry_lines", "confuses_asymptotes_with_axes_of_symmetry"],
        marks=2,
    )


def _build_28(rng: random.Random) -> Dict[str, Any]:
    sub = "28_hyperbola_effect_of_parameter_a"
    a = rng.choice([-8, -4, 4, 8])
    is_pos = a > 0
    quads = "quadrants 1 and 3 (relative to the asymptotes)" if is_pos else "quadrants 2 and 4 (relative to the asymptotes)"
    other_quads = "quadrants 2 and 4 (relative to the asymptotes)" if is_pos else "quadrants 1 and 3 (relative to the asymptotes)"
    prompt = f"For the hyperbolic function $f(x) = \\dfrac{{{a}}}{{x}} + 2$, identify which quadrants the branches of the hyperbola lie in, and describe the sign effect of $a = {a}$."
    ans = f"Branches lie in {quads}"
    opts = [
        ans,
        f"Branches lie in {other_quads}",
        "Branches lie entirely in quadrants 1 and 2",
        "Branches lie entirely in quadrants 3 and 4",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Parameter a = {a}", "to": f"a is {'positive (a > 0)' if is_pos else 'negative (a < 0)'}.", "rule": "sign of a", "op": "evaluate sign"},
        {"from": "Quadrant rule", "to": f"When a > 0, branches lie in Q1 & Q3. When a < 0, branches lie in Q2 & Q4. Conclusion: {quads}.", "rule": "hyperbola quadrant rule", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "If $a > 0$, positive $x$ yields positive $y$ (Q1) and negative $x$ yields negative $y$ (Q3).",
        "If $a < 0$, positive $x$ yields negative $y$ (Q4) and negative $x$ yields positive $y$ (Q2).",
        f"The branches lie in {quads}.",
        ["swaps_quadrant_locations", "ignores_sign_of_a"],
        marks=2,
    )


def _build_29(rng: random.Random) -> Dict[str, Any]:
    sub = "29_hyperbola_domain_and_range"
    a = rng.choice([-6, -3, 3, 6])
    q = rng.choice([-5, -2, 1, 4])
    dom = "\\{x: x \\in \\mathbb{R},\\, x \\neq 0\\}"
    ran = f"\\{{y: y \\in \\mathbb{{R}},\\, y \\neq {q}\\}}"
    ans = f"\\text{{Domain: }} {dom};\\, \\text{{Range: }} {ran}"
    opts = [
        ans,
        f"\\text{{Domain: }} \\{{x: x \\in \\mathbb{{R}},\\, x \\neq {q}\\}};\\, \\text{{Range: }} \\{{y: y \\in \\mathbb{{R}},\\, y \\neq 0\\}}",
        f"\\text{{Domain: }} \\{{x: x \\in \\mathbb{{R}}\\}};\\, \\text{{Range: }} \\{{y: y \\in \\mathbb{{R}}\\ge {q}\\}}",
        f"\\text{{Domain: }} [{q}; \\infty);\\, \\text{{Range: }} (-\\infty; {q}]",
    ]
    rng.shuffle(opts)
    prompt = f"State the **domain** and **range** of the hyperbola $f(x) = \\dfrac{{{a}}}{{x}} {_signed(q)}$ using set-builder notation."
    steps = [
        {"from": f"Division by zero is undefined: x != 0", "to": f"Domain = {dom}", "rule": "domain exclusion", "op": "exclude x = 0"},
        {"from": f"Since {a}/x cannot equal 0, y cannot equal {q}", "to": f"Range = {ran}", "rule": "range exclusion", "op": "exclude horizontal asymptote"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The domain excludes the vertical asymptote ($x = 0$).",
        f"The range excludes the horizontal asymptote ($y = {q}$).",
        f"Domain: ${dom}$; Range: ${ran}$.",
        ["swaps_domain_and_range_exclusions", "treats_hyperbola_as_having_unrestricted_domain"],
        marks=2,
    )


def _build_30(rng: random.Random) -> Dict[str, Any]:
    sub = "30_hyperbola_x_and_y_intercepts"
    # Choose a and q such that a is divisible by q
    q = rng.choice([-4, -2, 2, 4])
    mult = rng.choice([-3, -2, -1, 1, 2, 3])
    a = -q * mult
    x_int = mult
    prompt = f"Determine the $x$-intercept of the hyperbola $y = \\dfrac{{{a}}}{{x}} {_signed(q)}$, and explain why there is no $y$-intercept."
    ans = f"x\\text{{-intercept: }} {_coord(x_int, 0)};\\, \\text{{No }} y\\text{{-intercept because }} x = 0 \\text{{ is undefined}}"
    steps = [
        {"from": "x-intercept: set y = 0", "to": f"0 = \\dfrac{{{a}}}{{x}} {_signed(q)} \\implies \\dfrac{{{a}}}{{x}} = {-q} \\implies x = \\dfrac{{{a}}}{{{-q}}} = {x_int}", "rule": "solve x-intercept", "op": "set y = 0"},
        {"from": "y-intercept: set x = 0", "to": f"y = \\dfrac{{{a}}}{{0}} {_signed(q)} \\implies \\text{{division by zero is undefined}}", "rule": "y-axis asymptote", "op": "check x = 0"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "To find the $x$-intercept, set $y = 0$ and solve for $x$.",
        "Setting $x = 0$ results in division by zero, meaning the graph never crosses the $y$-axis (it is an asymptote).",
        f"$x$-intercept: ${x_int}$, so ${_coord(x_int, 0)}$. No $y$-intercept.",
        ["attempts_to_calculate_y_intercept_at_x_equals_0", "sign_error_solving_fraction"],
        marks=3,
    )


def _build_31(rng: random.Random) -> Dict[str, Any]:
    sub = "31_hyperbola_equation_from_asymptote_and_point"
    q = rng.choice([-4, -2, 1, 3, 5])
    x1 = rng.choice([-4, -2, 2, 4])
    a = x1 * rng.choice([-3, -2, 2, 3])
    y1 = (a // x1) + q
    eq = f"y = \\dfrac{{{a}}}{{x}} {_signed(q)}"
    # Inline SVG sketch of hyperbola
    elements = [
        f'<line x1="10" y1="{150 - q*10}" x2="390" y2="{150 - q*10}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />',
        f'<text x="20" y="{150 - q*10 - 6}" fill="#ef4444" font-size="11px">y = {q}</text>',
        f'<circle cx="{200 + x1*12}" cy="{150 - y1*10}" r="4" class="dot" />',
        f'<text x="{208 + x1*12}" y="{150 - y1*10 + 4}" class="label">P({x1}; {y1})</text>',
    ]
    diag = {
        "kind": "inline_svg",
        "svg": _make_svg_axes_frame(elements),
        "diagram_role": "context",
        "caption": f"Hyperbola with horizontal asymptote y = {q} passing through P({x1}; {y1}).",
    }
    prompt = f"The sketch shows a hyperbola with horizontal asymptote $y = {q}$ that passes through the point $P{_coord(x1, y1)}$. Determine its equation in the form $y = \\dfrac{{a}}{{x}} + q$."
    steps = [
        {"from": f"Horizontal asymptote is y = {q}", "to": f"Therefore q = {q}, so y = \\dfrac{{a}}{{x}} {_signed(q)}", "rule": "horizontal asymptote", "op": "substitute q"},
        {"from": f"Substitute point P{_coord(x1, y1)}", "to": f"{y1} = \\dfrac{{a}}{{{x1}}} {_signed(q)} \\implies \\dfrac{{a}}{{{x1}}} = {y1 - q} \\implies a = ({y1 - q}) \\times {x1} = {a}", "rule": "solve for a", "op": "substitute point"},
        {"from": "Write final equation", "to": eq, "rule": "equation synthesis", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        "The horizontal asymptote $y = q$ directly gives the value of $q$.",
        f"Substitute $x = {x1}$ and $y = {y1}$ into $y = \\dfrac{{a}}{{x}} {_signed(q)}$ and solve for $a$.",
        f"${y1} - ({q}) = \\dfrac{{a}}{{{x1}}} \\implies a = {a}$, so ${eq}$.",
        ["forgets_horizontal_asymptote_equals_q", "sign_error_multiplying_fraction"],
        marks=3,
        diagram_spec=diag,
    )


def _build_32(rng: random.Random) -> Dict[str, Any]:
    sub = "32_exponential_horizontal_asymptote"
    b = rng.choice([2, 3])
    q = rng.choice([-5, -3, -1, 2, 4, 6])
    a = rng.choice([1, 2])
    a_str = "" if a == 1 else f"{a} \\cdot "
    prompt = f"State the equation of the **horizontal asymptote** of the exponential function $f(x) = {a_str}{b}^x {_signed(q)}$, and explain why the curve never touches this line."
    ha = f"y = {q}"
    ans = f"{ha}; \\text{{ because }} {b}^x > 0 \\text{{ for all real }} x"
    opts = [
        ans,
        f"x = {q}; \\text{{ because }} x \\neq {q}",
        f"y = 0; \\text{{ because all exponentials approach }} 0",
        f"y = {b}; \\text{{ because base is }} {b}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"As x -> -infinity, {b}^x approaches 0", "to": f"f(x) approaches 0 {_signed(q)} = {q}, so asymptote is {ha}.", "rule": "asymptote definition", "op": "limit analysis"},
        {"from": f"Since {b}^x > 0 for all real x", "to": f"f(x) is strictly greater than {q} (never equals {q}).", "rule": "strict inequality", "op": "reasoning"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "For an exponential function $y = a \\cdot b^x + q$, the horizontal asymptote is always $y = q$.",
        "Since $b^x > 0$ for all real numbers $x$, the value of $a \\cdot b^x$ is never zero, so the graph never touches the line $y = q$.",
        f"Asymptote: ${ha}$, because ${b}^x > 0$.",
        ["confuses_horizontal_with_vertical_asymptote", "thinks_asymptote_is_always_y_equals_0"],
        marks=2,
    )


def _build_33(rng: random.Random) -> Dict[str, Any]:
    sub = "33_exponential_y_intercept_calculation"
    b = rng.choice([2, 3, 5])
    a = rng.choice([-3, -2, -1, 1, 2, 3])
    q = rng.choice([-6, -4, -1, 2, 5, 8])
    y_int = a * 1 + q
    a_str = "" if a == 1 else ("-" if a == -1 else f"{a} \\cdot ")
    prompt = f"Determine the $y$-intercept of the exponential function $g(x) = {a_str}{b}^x {_signed(q)}$ as an ordered coordinate pair."
    ans = f"{_coord(0, y_int)}"
    steps = [
        {"from": "y-intercept occurs where x = 0", "to": f"g(0) = {a} \\cdot ({b}^0) {_signed(q)}", "rule": "set x = 0", "op": "substitute x = 0"},
        {"from": f"Recall exponent rule: {b}^0 = 1", "to": f"g(0) = {a}(1) {_signed(q)} = {y_int}", "rule": "zero exponent rule", "op": "evaluate power"},
        {"from": "Write as coordinate pair", "to": ans, "rule": "coordinate pair", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "To find the $y$-intercept, substitute $x = 0$.",
        f"Remember that any non-zero base to the power of zero equals 1: ${b}^0 = 1$.",
        f"$g(0) = {a}(1) {_signed(q)} = {y_int}$, so the $y$-intercept is ${_coord(0, y_int)}$.",
        ["treats_base_to_power_zero_as_zero", "swaps_x_and_y_in_coordinate_pair"],
        marks=2,
    )


def _build_34(rng: random.Random) -> Dict[str, Any]:
    sub = "34_exponential_growth_vs_decay"
    is_growth = rng.choice([True, False])
    if is_growth:
        b = rng.choice([2, 3, 4])
        fn_tex = f"f(x) = {b}^x"
        type_word = "exponential growth"
        reason = f"the base b = {b} > 1, so y increases as x increases"
    else:
        den = rng.choice([2, 3, 4])
        fn_tex = f"f(x) = \\left(\\dfrac{{1}}{{{den}}}\\right)^x"
        type_word = "exponential decay"
        reason = f"the base 0 < b = 1/{den} < 1, so y decreases as x increases"

    other_type = "exponential decay" if is_growth else "exponential growth"
    prompt = f"Classify the function ${fn_tex}$ as either **exponential growth** or **exponential decay**, and justify your answer."
    ans = f"{type_word}; because {reason}"
    opts = [
        ans,
        f"{other_type}; because base is positive",
        "Linear growth; because gradient is constant",
        "Quadratic growth; because it has power",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": fn_tex, "to": f"Identify base b.", "rule": "base inspection", "op": "check base"},
        {"from": "Rule: b > 1 is growth; 0 < b < 1 is decay", "to": ans, "rule": "classification", "op": "classify"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Exponentials with base $b > 1$ represent exponential growth (increasing graph).",
        "Exponentials with base $0 < b < 1$ (or $b^{-x}$) represent exponential decay (decreasing graph).",
        f"Classification: {ans}.",
        ["confuses_growth_and_decay_base_thresholds", "misidentifies_fractional_base"],
        marks=2,
    )


def _build_35(rng: random.Random) -> Dict[str, Any]:
    sub = "35_exponential_domain_and_range"
    b = rng.choice([2, 3])
    a = rng.choice([1, 2, -1, -2])
    q = rng.choice([-5, -3, 1, 4])
    a_str = "" if a == 1 else ("-" if a == -1 else f"{a} \\cdot ")
    dom = "\\{x: x \\in \\mathbb{R}\\}"
    if a > 0:
        ran = f"({q};\\, \\infty)"
        dist = f"[{q};\\, \\infty)"
    else:
        ran = f"(-\\infty;\\, {q})"
        dist = f"(-\\infty;\\, {q}]"

    prompt = f"State the **domain** and **range** of the exponential function $f(x) = {a_str}{b}^x {_signed(q)}$."
    ans = f"\\text{{Domain: }} {dom};\\, \\text{{Range: }} {ran}"
    opts = [
        ans,
        f"\\text{{Domain: }} {dom};\\, \\text{{Range: }} {dist}",
        f"\\text{{Domain: }} {ran};\\, \\text{{Range: }} {dom}",
        f"\\text{{Domain: }} [{q}; \\infty);\\, \\text{{Range: }} \\{{y: y \\neq {q}\\}}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Domain of exponential function", "to": f"x can be any real number: {dom}", "rule": "domain rule", "op": "identify domain"},
        {"from": f"Horizontal asymptote is y = {q}", "to": f"Since a {' > 0 (curve lies above asymptote)' if a>0 else ' < 0 (curve lies below asymptote)'}, range is {ran} (open interval because asymptote is never reached).", "rule": "range rule", "op": "identify range"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The domain of an exponential function is always all real numbers: $x \\in \\mathbb{R}$.",
        f"The range is bounded by the asymptote $y = {q}$, using an open bracket $($ because the curve never touches the asymptote.",
        f"Domain: ${dom}$; Range: ${ran}$.",
        ["uses_closed_bracket_on_asymptote", "inverts_range_direction"],
        marks=2,
    )


def _build_36(rng: random.Random) -> Dict[str, Any]:
    sub = "36_exponential_equation_from_asymptote_and_point"
    b = rng.choice([2, 3])
    q = rng.choice([-4, -2, 1, 3])
    a = rng.choice([1, 2])
    x1 = rng.choice([1, 2])
    y1 = a * (b ** x1) + q
    a_str = "" if a == 1 else f"{a} \\cdot "
    eq = f"y = {a_str}{b}^x {_signed(q)}"
    # Inline SVG sketch of exponential graph
    elements = [
        f'<line x1="10" y1="{150 - q*10}" x2="390" y2="{150 - q*10}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />',
        f'<text x="20" y="{150 - q*10 - 6}" fill="#ef4444" font-size="11px">y = {q}</text>',
        f'<circle cx="{200 + x1*20}" cy="{150 - y1*6}" r="4" class="dot" />',
        f'<text x="{208 + x1*20}" y="{150 - y1*6 + 4}" class="label">P({x1}; {y1})</text>',
    ]
    diag = {
        "kind": "inline_svg",
        "svg": _make_svg_axes_frame(elements),
        "diagram_role": "context",
        "caption": f"Exponential function with base {b} and asymptote y = {q} passing through P({x1}; {y1}).",
    }
    prompt = f"The sketch shows an exponential function of the form $y = a \\cdot {b}^x + q$ with horizontal asymptote $y = {q}$ passing through point $P{_coord(x1, y1)}$. Determine the value of $a$ and write down the equation."
    steps = [
        {"from": f"Horizontal asymptote is y = {q}", "to": f"q = {q} \\implies y = a \\cdot {b}^x {_signed(q)}", "rule": "substitute asymptote", "op": "identify q"},
        {"from": f"Substitute point P{_coord(x1, y1)}", "to": f"{y1} = a \\cdot ({b}^{{{x1}}}) {_signed(q)} \\implies {y1 - q} = a \\cdot {b**x1} \\implies a = {a}", "rule": "solve for a", "op": "substitute point"},
        {"from": "Write final equation", "to": eq, "rule": "equation synthesis", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        f"The horizontal asymptote $y = {q}$ gives $q = {q}$.",
        f"Substitute $x = {x1}$ and $y = {y1}$ into $y = a \\cdot {b}^x {_signed(q)}$ to solve for $a$.",
        f"${y1} - ({q}) = a \\cdot {b**x1} \\implies a = {a}$, so ${eq}$.",
        ["forgets_asymptote_value_in_substitution", "sign_error_solving_for_a"],
        marks=3,
        diagram_spec=diag,
    )


def _build_37(rng: random.Random) -> Dict[str, Any]:
    sub = "37_trig_sine_amplitude_period_range"
    a = rng.choice([-3, -2, 2, 3])
    q = rng.choice([-2, -1, 0, 1, 2])
    amp = abs(a)
    period = "360^\\circ"
    min_val = q - amp
    max_val = q + amp
    ran = f"[{min_val};\\, {max_val}]"
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    q_str = f" {_signed(q)}" if q != 0 else ""
    prompt = f"For the trigonometric function $y = {a_str}\\sin x{q_str}$ where $x \\in [0^\\circ;\\, 360^\\circ]$, determine its **amplitude**, **period**, and **range**."
    ans = f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} {period};\\, \\text{{Range: }} {ran}"
    opts = [
        ans,
        f"\\text{{Amplitude: }} {a};\\, \\text{{Period: }} 180^\\circ;\\, \\text{{Range: }} {ran}",
        f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} {period};\\, \\text{{Range: }} [{q}; {max_val}]",
        f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} 720^\\circ;\\, \\text{{Range: }} [-1; 1]",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Amplitude is |a|", "to": f"Amplitude = |{a}| = {amp}", "rule": "amplitude definition", "op": "absolute value"},
        {"from": "Period of standard sine", "to": f"Period = {period}", "rule": "period definition", "op": "period"},
        {"from": "Range of shifted sine", "to": f"Minimum = {q} - {amp} = {min_val}; Maximum = {q} + {amp} = {max_val} \\implies Range = {ran}", "rule": "range calculation", "op": "range"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Amplitude is always positive: $\\text{Amplitude} = |a|$.",
        "The period of $y = a\\sin x + q$ is $360^\\circ$.",
        f"The range is $[q - |a|; q + |a|] = {ran}$.",
        ["writes_negative_amplitude", "confuses_period_with_tangent"],
        marks=3,
    )


def _build_38(rng: random.Random) -> Dict[str, Any]:
    sub = "38_trig_cosine_amplitude_period_range"
    a = rng.choice([-3, -2, 2, 3])
    q = rng.choice([-2, -1, 0, 1, 2])
    amp = abs(a)
    period = "360^\\circ"
    min_val = q - amp
    max_val = q + amp
    ran = f"[{min_val};\\, {max_val}]"
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    q_str = f" {_signed(q)}" if q != 0 else ""
    prompt = f"For the trigonometric function $y = {a_str}\\cos x{q_str}$ where $x \\in [0^\\circ;\\, 360^\\circ]$, determine its **amplitude**, **period**, and **range**."
    ans = f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} {period};\\, \\text{{Range: }} {ran}"
    opts = [
        ans,
        f"\\text{{Amplitude: }} {a};\\, \\text{{Period: }} 180^\\circ;\\, \\text{{Range: }} {ran}",
        f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} {period};\\, \\text{{Range: }} [{min_val}; {q}]",
        f"\\text{{Amplitude: }} {amp};\\, \\text{{Period: }} 360^\\circ;\\, \\text{{Range: }} [-1; 1]",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Amplitude", "to": f"Amplitude = |{a}| = {amp}", "rule": "amplitude rule", "op": "evaluate |a|"},
        {"from": "Period", "to": f"Period = {period}", "rule": "period rule", "op": "period"},
        {"from": "Range", "to": f"Range = [{min_val}; {max_val}]", "rule": "range calculation", "op": "range"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Amplitude is the distance from the central axis to the peak: $|a|$.",
        "The period of the cosine function is $360^\\circ$.",
        f"Range: $[q - |a|; q + |a|] = {ran}$.",
        ["writes_negative_amplitude", "confuses_cosine_range_with_sine"],
        marks=3,
    )


def _build_39(rng: random.Random) -> Dict[str, Any]:
    sub = "39_trig_tangent_period_and_asymptotes"
    a = rng.choice([1, 2, -1, -2])
    q = rng.choice([-1, 0, 1])
    period = "180^\\circ"
    asymp = "x = 90^\\circ \\text{ and } x = 270^\\circ"
    ran = "\\{y: y \\in \\mathbb{R}\\}"
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    q_str = f" {_signed(q)}" if q != 0 else ""
    prompt = f"For the tangent function $y = {a_str}\\tan x{q_str}$ defined on $x \\in [0^\\circ;\\, 360^\\circ]$, state its **period**, the equations of its **asymptotes**, and its **amplitude**."
    ans = f"\\text{{Period: }} {period};\\, \\text{{Asymptotes: }} {asymp};\\, \\text{{Amplitude: Undefined (no amplitude)}}"
    opts = [
        ans,
        f"\\text{{Period: }} 360^\\circ;\\, \\text{{Asymptotes: }} {asymp};\\, \\text{{Amplitude: }} {abs(a)}",
        f"\\text{{Period: }} {period};\\, \\text{{Asymptotes: }} x = 180^\\circ;\\, \\text{{Amplitude: Undefined}}",
        f"\\text{{Period: }} 180^\\circ;\\, \\text{{Asymptotes: }} {asymp};\\, \\text{{Amplitude: }} {abs(a)}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Period of tangent", "to": f"Tangent repeats every {period}.", "rule": "tan period", "op": "period"},
        {"from": "Asymptotes where cos(x) = 0", "to": f"Asymptotes at {asymp}.", "rule": "tan asymptotes", "op": "undefined points"},
        {"from": "Amplitude of tangent", "to": "Undefined: tan approaches +/- infinity so it has no amplitude.", "rule": "tan amplitude", "op": "amplitude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The period of the tangent function is $180^\\circ$ (half that of sine and cosine).",
        "Tangent is undefined where $\\cos x = 0$, giving asymptotes at $x = 90^\\circ$ and $x = 270^\\circ$ on $[0^\\circ; 360^\\circ]$.",
        "Tangent has no maximum or minimum, so its amplitude is undefined.",
        ["assumes_tangent_has_amplitude_a", "claims_tangent_period_is_360"],
        marks=3,
    )


def _build_40(rng: random.Random) -> Dict[str, Any]:
    sub = "40_trig_effect_of_vertical_shift_q"
    trig_name = rng.choice(["\\sin", "\\cos"])
    a = rng.choice([2, 3])
    q = rng.choice([-3, -2, 2, 3, 4])
    max_val = q + a
    min_val = q - a
    direction = "upwards" if q > 0 else "downwards"
    prompt = f"Describe how the parameter $q = {q}$ transforms $y = {a}{trig_name} x$ into $y = {a}{trig_name} x {_signed(q)}$, and state the new maximum and minimum values."
    ans = f"Shifted {abs(q)} units {direction}; \\text{{Maximum: }} {max_val};\\, \\text{{Minimum: }} {min_val}"
    opts = [
        ans,
        f"Shifted {abs(q)} units {'downwards' if q > 0 else 'upwards'}; \\text{{Maximum: }} {max_val};\\, \\text{{Minimum: }} {min_val}",
        f"Shifted {abs(q)} units {direction}; \\text{{Maximum: }} {a};\\, \\text{{Minimum: }} {-a}",
        f"Shifted horizontally by {abs(q)} units",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Vertical translation parameter q = {q}", "to": f"Entire curve shifted {abs(q)} units {direction}.", "rule": "vertical translation", "op": "shift"},
        {"from": f"Original range [-{a}; {a}]", "to": f"New maximum = {a} {_signed(q)} = {max_val}; New minimum = -{a} {_signed(q)} = {min_val}.", "rule": "extrema transformation", "op": "compute new bounds"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Adding $q$ shifts every point on the graph vertically by $q$ units.",
        f"New maximum $= |a| + q = {max_val}$; New minimum $= -|a| + q = {min_val}$.",
        f"Result: {ans}.",
        ["confuses_vertical_shift_with_amplitude_change", "arithmetic_sign_error_on_minimum"],
        marks=2,
    )


def _build_41(rng: random.Random) -> Dict[str, Any]:
    sub = "41_trig_find_equation_from_sketch"
    a = rng.choice([1, 2, 3])
    q = rng.choice([-2, -1, 1, 2])
    max_val = q + a
    min_val = q - a
    a_str = "" if a == 1 else str(a)
    eq = f"y = {a_str}\\sin x {_signed(q)}"
    # Sketch sine curve with key peak and trough
    elements = [
        f'<circle cx="{200 + 40}" cy="{150 - max_val*15}" r="4" class="dot" />',
        f'<text x="{208 + 40}" y="{150 - max_val*15 - 4}" class="label">(90°; {max_val})</text>',
        f'<circle cx="{200 + 120}" cy="{150 - min_val*15}" r="4" class="dot" />',
        f'<text x="{208 + 120}" y="{150 - min_val*15 + 14}" class="label">(270°; {min_val})</text>',
    ]
    diag = {
        "kind": "inline_svg",
        "svg": _make_svg_axes_frame(elements, origin=(120, 150), x_range=(-2, 10), y_range=(-6, 6)),
        "diagram_role": "context",
        "caption": f"Sine curve with peak at (90°; {max_val}) and trough at (270°; {min_val}).",
    }
    prompt = f"The sketch shows a sine graph of the form $y = a\\sin x + q$ on $x \\in [0^\\circ;\\, 360^\\circ]$ with a maximum turning point at $(90^\\circ;\\, {max_val})$ and a minimum turning point at $(270^\\circ;\\, {min_val})$. Determine the values of $a$ and $q$ and write down the equation."
    steps = [
        {"from": "Determine amplitude a", "to": f"a = \\dfrac{{\\text{{max}} - \\text{{min}}}}{{2}} = \\dfrac{{{max_val} - ({min_val})}}{{2}} = \\dfrac{{{2*a}}}{{2}} = {a}", "rule": "amplitude formula", "op": "compute a"},
        {"from": "Determine vertical shift q", "to": f"q = \\dfrac{{\\text{{max}} + \\text{{min}}}}{{2}} = \\dfrac{{{max_val} + ({min_val})}}{{2}} = \\dfrac{{{2*q}}}{{2}} = {q}", "rule": "midline formula", "op": "compute q"},
        {"from": "Formulate equation", "to": eq, "rule": "equation synthesis", "op": "write equation"},
    ]
    return _base_contract(
        sub, prompt, eq, None, steps,
        "Calculate amplitude: $a = \\dfrac{\\text{maximum} - \\text{minimum}}{2}$.",
        "Calculate central axis (vertical shift): $q = \\dfrac{\\text{maximum} + \\text{minimum}}{2}$.",
        f"$a = {a}$ and $q = {q}$, so the equation is ${eq}$.",
        ["swaps_formulas_for_a_and_q", "sign_error_evaluating_midline"],
        marks=3,
        diagram_spec=diag,
    )


def _build_42(rng: random.Random) -> Dict[str, Any]:
    sub = "42_graph_point_of_intersection_algebraic"
    # Intersection of line y = mx + c and parabola y = x^2 + q
    # (x - r1)(x - r2) = x^2 - (r1+r2)x + r1*r2 = 0
    r1 = rng.choice([-3, -2, -1])
    r2 = rng.choice([1, 2, 3])
    m = r1 + r2
    c_minus_q = -r1 * r2
    q = rng.choice([-5, -3, 1])
    c = q + c_minus_q
    y_at_r1 = r1**2 + q
    y_at_r2 = r2**2 + q
    pt1 = _coord(r1, y_at_r1)
    pt2 = _coord(r2, y_at_r2)
    m_str = "" if m == 1 else ("-" if m == -1 else (f"{m}" if m != 0 else ""))
    line_body = f"{m_str}x {_signed(c)}" if m != 0 else f"{c}"
    prompt = f"Calculate the coordinates of the points of intersection between the line $y = {line_body}$ and the parabola $y = x^2 {_signed(q)}$."
    ans = f"{pt1} \\text{{ and }} {pt2}"
    steps = [
        {"from": "Equate expressions: x^2 + q = mx + c", "to": f"x^2 {_signed(q)} = {line_body} \\implies x^2 - ({m})x - ({c-q}) = 0", "rule": "equate equations", "op": "rearrange to quadratic"},
        {"from": f"Factorise: (x - ({r1}))(x - ({r2})) = 0", "to": f"x = {r1} \\text{{ or }} x = {r2}", "rule": "factorisation", "op": "solve for x"},
        {"from": "Substitute x into equation to find y", "to": f"y({r1}) = {y_at_r1} \\implies {pt1};\\, y({r2}) = {y_at_r2} \\implies {pt2}", "rule": "find y coordinates", "op": "substitute x"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Set the two equations equal to each other: $x^2 + q = mx + c$.",
        "Rearrange into standard quadratic form $ax^2 + bx + c = 0$ and factorise.",
        f"Substitute $x = {r1}$ and $x = {r2}$ back to find $y$-coordinates: ${ans}$.",
        ["finds_only_x_values_and_forgets_y_coordinates", "factorisation_sign_error"],
        marks=4,
    )


def _build_43(rng: random.Random) -> Dict[str, Any]:
    sub = "43_graph_point_of_intersection_hyperbola_linear"
    # a/x = m -> x = a/m
    m = rng.choice([1, 2, 3])
    x_val = rng.choice([2, 3, 4])
    a = m * (x_val ** 2)
    # y = m*x and y = a/x
    y_val = m * x_val
    prompt = f"Determine the coordinates of the points of intersection of the line $y = {m}x$ and the hyperbola $y = \\dfrac{{{a}}}{{x}}$."
    ans = f"{_coord(-x_val, -y_val)} \\text{{ and }} {_coord(x_val, y_val)}"
    steps = [
        {"from": f"Equate: {m}x = \\dfrac{{{a}}}{{x}}", "to": f"{m}x^2 = {a} \\implies x^2 = {x_val**2}", "rule": "multiply by x", "op": "isolate x^2"},
        {"from": f"x^2 = {x_val**2}", "to": f"x = \\pm {x_val}", "rule": "square root property", "op": "solve for x"},
        {"from": "Substitute x into y = mx", "to": f"y({-x_val}) = {-y_val} \\implies {_coord(-x_val, -y_val)};\\, y({x_val}) = {y_val} \\implies {_coord(x_val, y_val)}", "rule": "find coordinates", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Set the equations equal: $mx = \\dfrac{a}{x}$.",
        "Multiply both sides by $x$ to form $mx^2 = a$, then solve for $x = \\pm \\sqrt{a/m}$.",
        f"Points of intersection: ${ans}$.",
        ["forgets_negative_root", "forgets_to_calculate_y_coordinates"],
        marks=3,
    )


def _build_44(rng: random.Random) -> Dict[str, Any]:
    sub = "44_graph_reading_coordinates_and_values"
    a = rng.choice([1, 2])
    q = rng.choice([-4, -1, 3])
    x_test = rng.choice([1, 2, 3])
    y_test = a * (x_test ** 2) + q
    elements = [
        f'<circle cx="{200 + x_test*15}" cy="{150 - y_test*10}" r="4" class="dot" />',
        f'<line x1="{200 + x_test*15}" y1="150" x2="{200 + x_test*15}" y2="{150 - y_test*10}" stroke="#94a3b8" stroke-dasharray="3,3" />',
        f'<line x1="200" y1="{150 - y_test*10}" x2="{200 + x_test*15}" y2="{150 - y_test*10}" stroke="#94a3b8" stroke-dasharray="3,3" />',
        f'<text x="{208 + x_test*15}" y="{150 - y_test*10 - 4}" class="label">P</text>',
    ]
    diag = {
        "kind": "inline_svg",
        "svg": _make_svg_axes_frame(elements),
        "diagram_role": "context",
        "caption": f"Graph of f(x) with highlighted point P.",
    }
    prompt = f"In the accompanying Cartesian diagram, the function curve $f(x) = {a}x^2 {_signed(q)}$ is plotted with marked point $P({x_test};\\, f({x_test}))$. Read and state the value of $f({x_test})$."
    steps = [
        {"from": f"Trace projection from x = {x_test}", "to": f"Point P has x = {x_test} and aligns with y = {y_test} on the vertical axis.", "rule": "read coordinate", "op": "read projection"},
        {"from": "Algebraic verification", "to": f"f({x_test}) = {a}({x_test})^2 {_signed(q)} = {y_test}", "rule": "evaluation check", "op": "verify"},
    ]
    return _base_contract(
        sub, prompt, str(y_test), None, steps,
        f"Locate $x = {x_test}$ on the horizontal axis and follow the dashed projection line up/down to point $P$.",
        "Read the corresponding $y$-value on the vertical axis.",
        f"$f({x_test}) = {y_test}$.",
        ["reads_wrong_axis", "swaps_x_and_y_values"],
        marks=2,
        diagram_spec=diag,
    )


def _build_45(rng: random.Random) -> Dict[str, Any]:
    sub = "45_graphical_inequalities_positive_negative"
    r = rng.choice([2, 3, 4])
    a = 1
    q = -(r ** 2)
    ask_positive = rng.choice([True, False])
    # f(x) = x^2 - r^2
    # f(x) > 0 for x < -r or x > r
    # f(x) <= 0 for -r <= x <= r
    if ask_positive:
        target = "f(x) > 0"
        correct = f"x < -{r} \\text{{ or }} x > {r}"
        wrong = f"-{r} < x < {r}"
    else:
        target = "f(x) \\le 0"
        correct = f"-{r} \\le x \\le {r}"
        wrong = f"x \\le -{r} \\text{{ or }} x \\ge {r}"

    opts = [
        correct,
        wrong,
        f"x > {r}",
        f"x < -{r}",
    ]
    rng.shuffle(opts)
    prompt = f"For the parabola $f(x) = x^2 - {r**2}$, determine the values of $x$ for which **${target}$**."
    steps = [
        {"from": f"Find roots of f(x) = 0", "to": f"x^2 - {r**2} = 0 \\implies x = -{r} \\text{{ or }} x = {r}", "rule": "roots of parabola", "op": "solve roots"},
        {"from": f"Parabola opens upwards (a > 0)", "to": f"The curve lies above the x-axis for x < -{r} and x > {r}; it lies on/below for -{r} <= x <= {r}.", "rule": "graphical interpretation", "op": "analyze sign"},
        {"from": f"Condition: {target}", "to": correct, "rule": "conclude", "op": "select interval"},
    ]
    return _base_contract(
        sub, prompt, correct, opts, steps,
        f"First find the $x$-intercepts where $f(x) = 0$: $x = \\pm {r}$.",
        "Since the parabola opens upwards, it is below the $x$-axis between the roots and above the $x$-axis outside the roots.",
        f"For ${target}$: ${correct}$.",
        ["swaps_inside_and_outside_intervals", "omits_equality_in_inequality"],
        marks=2,
    )


def _build_46(rng: random.Random) -> Dict[str, Any]:
    sub = "46_graphical_inequalities_comparison"
    # Parabolas f(x) and line g(x) intersect at x = r1 and x = r2 (r1 < r2)
    r1 = rng.choice([-3, -2, -1])
    r2 = rng.choice([1, 2, 3])
    # Parabola f(x) = -x^2 + q, line g(x) = mx + c
    # When is f(x) >= g(x)? Between the intersection points where parabola is above line: r1 <= x <= r2
    correct = f"{r1} \\le x \\le {r2}"
    wrong = f"x \\le {r1} \\text{{ or }} x \\ge {r2}"
    opts = [
        correct,
        wrong,
        f"x \\ge {r2}",
        f"x \\le {r1}",
    ]
    rng.shuffle(opts)
    prompt = f"A concave-down parabola $f(x)$ and a straight line $g(x)$ intersect at the points where $x = {r1}$ and $x = {r2}$. Use graphical reasoning to determine the values of $x$ for which $f(x) \\ge g(x)$."
    steps = [
        {"from": "Intersection points", "to": f"f(x) = g(x) at x = {r1} and x = {r2}.", "rule": "intersections", "op": "identify boundary"},
        {"from": "Relative positions of graphs", "to": f"Because f(x) is concave-down, the parabola arches above the straight line between the two roots.", "rule": "comparison", "op": "analyze region"},
        {"from": "f(x) >= g(x)", "to": correct, "rule": "interval synthesis", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, correct, opts, steps,
        "The inequality $f(x) \\ge g(x)$ means: where does the graph of $f$ lie on or above the graph of $g$?",
        f"Since the parabola is concave down, it lies above the line between the intersection points $x = {r1}$ and $x = {r2}$.",
        f"Solution: ${correct}$.",
        ["inverts_inequality_interval", "omits_equality_boundary"],
        marks=2,
    )


def _build_47(rng: random.Random) -> Dict[str, Any]:
    sub = "47_vertical_distance_between_two_graphs"
    # f(x) = 2x + 5, g(x) = -x + 1
    # distance at x0: |f(x0) - g(x0)|
    m1 = rng.choice([2, 3])
    c1 = rng.choice([4, 6, 8])
    m2 = rng.choice([-2, -1])
    c2 = rng.choice([-3, -1, 1])
    x0 = rng.choice([1, 2, 3])
    y_f = m1 * x0 + c1
    y_g = m2 * x0 + c2
    dist = abs(y_f - y_g)
    prompt = f"Two graphs are defined by $f(x) = {m1}x {_signed(c1)}$ and $g(x) = {m2}x {_signed(c2)}$. Calculate the vertical distance between the two graphs at $x = {x0}$."
    ans = f"{dist} \\text{{ units}}"
    steps = [
        {"from": f"Evaluate f({x0})", "to": f"f({x0}) = {m1}({x0}) {_signed(c1)} = {y_f}", "rule": "function evaluation", "op": "compute f(x0)"},
        {"from": f"Evaluate g({x0})", "to": f"g({x0}) = {m2}({x0}) {_signed(c2)} = {y_g}", "rule": "function evaluation", "op": "compute g(x0)"},
        {"from": "Vertical distance formula: |f(x) - g(x)|", "to": f"Distance = |{y_f} - ({y_g})| = {dist} \\text{{ units}}", "rule": "vertical distance", "op": "subtract values"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        f"Calculate the $y$-value on each graph by substituting $x = {x0}$.",
        "Subtract the smaller $y$-value from the larger $y$-value to find the vertical length (distance is always positive).",
        f"Distance $= |{y_f} - ({y_g})| = {dist}$ units.",
        ["negative_distance_error", "subtraction_sign_error"],
        marks=3,
    )


def _build_48(rng: random.Random) -> Dict[str, Any]:
    sub = "48_reflection_across_axes"
    reflect_x = rng.choice([True, False])
    a = rng.choice([2, 3])
    q = rng.choice([-5, -3, 2, 4])
    # Parent f(x) = ax^2 + q
    if reflect_x:
        # Reflection in x-axis: y = -f(x) = -ax^2 - q
        axis_name = "x-axis"
        new_eq = f"y = -{a}x^2 {_signed(-q)}"
        rule_desc = "Replace $y$ with $-y$ (or multiply entire function by $-1$): $y = -f(x)$."
    else:
        # Reflection in y-axis: y = f(-x) = a(-x)^2 + q = ax^2 + q
        axis_name = "y-axis"
        new_eq = f"y = {a}x^2 {_signed(q)}"
        rule_desc = "Replace $x$ with $-x$: $y = f(-x) = a(-x)^2 + q = ax^2 + q$."

    prompt = f"Given $f(x) = {a}x^2 {_signed(q)}$, determine the resulting equation obtained after reflecting $f(x)$ across the **{axis_name}**."
    steps = [
        {"from": f"Reflection in {axis_name}", "to": rule_desc, "rule": f"reflection across {axis_name}", "op": "apply reflection rule"},
        {"from": "Simplify expression", "to": new_eq, "rule": "algebraic simplification", "op": "finalize equation"},
    ]
    return _base_contract(
        sub, prompt, new_eq, None, steps,
        f"To reflect across the $x$-axis, negate the entire function: $y = -f(x)$.",
        f"To reflect across the $y$-axis, substitute $-x$ for every $x$: $y = f(-x)$.",
        f"The resulting equation is ${new_eq}$.",
        ["confuses_x_axis_and_y_axis_reflection", "fails_to_distribute_negative_to_q"],
        marks=2,
    )


def _build_49(rng: random.Random) -> Dict[str, Any]:
    sub = "49_vertical_translation_transformation"
    a = rng.choice([2, 3, -2, -3])
    q = rng.choice([-4, -2, 1, 3])
    shift = rng.choice([-5, -3, 2, 4, 6])
    direction = "upwards" if shift > 0 else "downwards"
    new_q = q + shift
    a_str = f"{a}"
    orig_eq = f"f(x) = {a_str}x^2 {_signed(q)}"
    new_eq = f"g(x) = {a_str}x^2 {_signed(new_q)}"
    prompt = f"The parabola ${orig_eq}$ is translated vertically by ${abs(shift)}$ units **{direction}** to form a new function $g(x)$. Determine the equation of $g(x)$."
    steps = [
        {"from": f"Vertical shift of {abs(shift)} units {direction}", "to": f"Add {shift} to the constant term: q_new = {q} {_signed(shift)} = {new_q}", "rule": "vertical translation", "op": "translate"},
        {"from": "Formulate new equation", "to": new_eq, "rule": "equation synthesis", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, new_eq, None, steps,
        f"A vertical shift of ${abs(shift)}$ units {direction} means adding ${shift}$ to the entire function: $g(x) = f(x) {_signed(shift)}$.",
        f"Calculate the new constant term: ${q} {_signed(shift)} = {new_q}$.",
        f"The equation of $g(x)$ is ${new_eq}$.",
        ["shifts_in_wrong_vertical_direction", "applies_shift_to_x_squared_coefficient"],
        marks=2,
    )


def _build_50(rng: random.Random) -> Dict[str, Any]:
    sub = "50_contextual_function_word_problem"
    # Projectile motion: h(t) = -5t^2 + q
    # Initial height q (e.g. from a cliff or tower)
    q = rng.choice([20, 45, 80, 125])
    # Time to hit ground: h(t) = 0 -> 5t^2 = q -> t = sqrt(q/5)
    t_ground = int(math.isqrt(q // 5))
    prompt = (
        f"A stone is dropped from a cliff in the Drakensberg mountains. Its height $h(t)$ in metres above the ground "
        f"after $t$ seconds is modelled by the quadratic function $h(t) = -5t^2 + {q}$. "
        f"Calculate how many seconds it takes for the stone to hit the ground."
    )
    ans = f"{t_ground} \\text{{ seconds}}"
    steps = [
        {"from": "When stone hits the ground, height h(t) = 0", "to": f"0 = -5t^2 + {q}", "rule": "set height to zero", "op": "equate to 0"},
        {"from": f"5t^2 = {q}", "to": f"t^2 = {q // 5}", "rule": "isolate t^2", "op": "divide by 5"},
        {"from": f"t = \\sqrt{{{q // 5}}}", "to": f"t = {t_ground} \\text{{ seconds}} (time must be positive)", "rule": "physical context restriction", "op": "evaluate square root"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "When the object hits the ground, its height is zero: set $h(t) = 0$.",
        f"Solve the quadratic equation: $5t^2 = {q} \\implies t^2 = {q//5}$.",
        f"Since time cannot be negative in a physical context, $t = {t_ground}$ seconds.",
        ["includes_negative_time_solution", "arithmetic_division_error"],
        marks=3,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_hyperbola_vertical_and_horizontal_asymptotes": _build_26,
    "27_hyperbola_axes_of_symmetry": _build_27,
    "28_hyperbola_effect_of_parameter_a": _build_28,
    "29_hyperbola_domain_and_range": _build_29,
    "30_hyperbola_x_and_y_intercepts": _build_30,
    "31_hyperbola_equation_from_asymptote_and_point": _build_31,
    "32_exponential_horizontal_asymptote": _build_32,
    "33_exponential_y_intercept_calculation": _build_33,
    "34_exponential_growth_vs_decay": _build_34,
    "35_exponential_domain_and_range": _build_35,
    "36_exponential_equation_from_asymptote_and_point": _build_36,
    "37_trig_sine_amplitude_period_range": _build_37,
    "38_trig_cosine_amplitude_period_range": _build_38,
    "39_trig_tangent_period_and_asymptotes": _build_39,
    "40_trig_effect_of_vertical_shift_q": _build_40,
    "41_trig_find_equation_from_sketch": _build_41,
    "42_graph_point_of_intersection_algebraic": _build_42,
    "43_graph_point_of_intersection_hyperbola_linear": _build_43,
    "44_graph_reading_coordinates_and_values": _build_44,
    "45_graphical_inequalities_positive_negative": _build_45,
    "46_graphical_inequalities_comparison": _build_46,
    "47_vertical_distance_between_two_graphs": _build_47,
    "48_reflection_across_axes": _build_48,
    "49_vertical_translation_transformation": _build_49,
    "50_contextual_function_word_problem": _build_50,
}
