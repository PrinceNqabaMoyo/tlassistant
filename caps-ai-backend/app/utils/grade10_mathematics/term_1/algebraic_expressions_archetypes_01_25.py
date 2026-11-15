"""Grade 10 Mathematics — Term 1 — Algebraic Expressions: Archetypes 01 to 25.

Ground truth: curriculum_docs/Mathematics_Gr10/Term 1/1 Algebraic Expressions .md
Zero LLM, 100% deterministic SymPy-backed questions with step-by-step solutions.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    make_mcq,
    make_short,
    make_steps,
    nonzero,
    num,
    solution,
    step,
    to_latex,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_algebraic_expressions"
LO = "math10_algebraic_expressions"
x = sp.Symbol("x")
y = sp.Symbol("y")
n = sp.Symbol("n")


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Correct mathematical method / expansion / factorisation", "marks": max(1, marks - 1)},
        {"criterion": "Accurate final expression / value in simplest form", "marks": 1},
    ]
    q.update({
        "term": 1,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill_name}",
        "marking_schema": schema,
    })
    return q


# --------------------------------------------------------------------------- #
# 01_classify_number_system_rational_irrational
# --------------------------------------------------------------------------- #
def _build_01_classify_number_system_rational_irrational(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    candidates = [
        ("\\sqrt{2}", "irrational", "A non-terminating, non-recurring surd cannot be written as a/b where a, b are integers."),
        ("\\sqrt{3}", "irrational", "3 is not a perfect square, so its square root is irrational."),
        ("\\sqrt{5}", "irrational", "Surds that cannot be simplified to rational numbers are irrational."),
        ("\\sqrt{7}", "irrational", "Square root of a prime number is always irrational."),
        ("\\pi", "irrational", "Pi is a transcendental number whose decimal expansion never terminates or repeats."),
        ("\\frac{3}{4}", "rational", "It is explicitly in the form a/b with non-zero integer denominator."),
        ("-\\frac{5}{8}", "rational", "Negative fractions of integers are rational numbers."),
        ("0{,}25", "rational", "It terminates after two decimal places (equal to 1/4)."),
        ("0{,}\\overline{3}", "rational", "A recurring decimal can always be expressed as an integer fraction (1/3)."),
        ("0{,}\\overline{45}", "rational", "A recurring two-digit decimal equals 45/99 = 5/11, which is rational."),
        ("\\sqrt{16}", "rational", "Square root of 16 is 4, which is an integer and therefore rational."),
        ("\\sqrt{49}", "rational", "Square root of 49 is 7, which is a rational whole number."),
        ("0", "rational", "Zero can be written as 0/1, which is rational and whole."),
        ("-12", "rational", "All integers are rational numbers with denominator 1."),
    ]
    pick_irr = (r.random() < 0.5)
    if pick_irr:
        target_pool = [c for c in candidates if c[1] == "irrational"]
        other_pool = [c for c in candidates if c[1] == "rational"]
        target = r.choice(target_pool)
        distractors = r.sample(other_pool, 3)
        prompt = "Which of the following numbers is an irrational number?"
        expl = f"${target[0]}$ is irrational: {target[2]}"
    else:
        target_pool = [c for c in candidates if c[1] == "rational"]
        other_pool = [c for c in candidates if c[1] == "irrational"]
        target = r.choice(target_pool)
        distractors = r.sample(other_pool, 3)
        prompt = "Which of the following numbers is a rational number?"
        expl = f"${target[0]}$ is rational: {target[2]}"

    options = [target[0]] + [d[0] for d in distractors]
    r.shuffle(options)
    correct_idx = options.index(target[0])

    q = make_mcq(
        prefix=TOPIC,
        prompt=prompt,
        options=[f"${o}$" for o in options],
        options_latex=options,
        correct_index=correct_idx,
        explanation=expl,
        marks=1,
        hint="A rational number can be written as a fraction a/b where a and b are integers and b != 0.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="01_classify_number_system_rational_irrational",
        learning_objective_id=f"{LO}.01_classify_number_system",
        misconception_tags=["confuses_surd_with_rational", "thinks_pi_is_rational", "fails_to_simplify_perfect_square"],
        diagnostic_tags=["number_systems", "rational_numbers"],
        keywords=["rational", "irrational", "real numbers", "surd"],
    )
    return _add_pillars(q, "01_classify_number_system_rational_irrational", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 02_identify_non_real_and_undefined_numbers
# --------------------------------------------------------------------------- #
def _build_02_identify_non_real_and_undefined_numbers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.randint(2, 9)
    scenario = r.choice(["non_real_root", "undefined_fraction", "for_which_x_non_real"])
    if scenario == "non_real_root":
        neg_val = -1 * (k ** 2)
        q = make_mcq(
            prefix=TOPIC,
            prompt=f"Which of the following represents a non-real number?",
            options=[f"$\\sqrt{{{neg_val}}}$", f"$\\sqrt{{{k**2}}}$", f"$-\\sqrt{{{k**2}}}$", f"$\\sqrt[3]{{{neg_val}}}$"],
            correct_index=0,
            explanation=f"The square root of a negative number (such as $\\sqrt{{{neg_val}}}$) is non-real in the real number system. Note that odd roots like cube roots of negative numbers are real.",
            marks=1,
            hint="An even root of a negative number is non-real.",
        )
    elif scenario == "undefined_fraction":
        val = r.randint(1, 8)
        q = make_mcq(
            prefix=TOPIC,
            prompt=f"For which value of $x$ is the fraction $\\dfrac{{{k}}}{{x - {val}}}$ undefined?",
            options=[f"$x = {val}$", f"$x = 0$", f"$x = -{val}$", f"$x = {k}$"],
            correct_index=0,
            explanation=f"Division by zero is undefined. Setting the denominator to zero gives $x - {val} = 0 \\implies x = {val}$.",
            marks=1,
            hint="Set the denominator equal to 0.",
        )
    else:
        a = r.randint(2, 7)
        q = make_mcq(
            prefix=TOPIC,
            prompt=f"For which values of $x$ is the expression $\\sqrt{{x - {a}}}$ non-real?",
            options=[f"$x < {a}$", f"$x \\ge {a}$", f"$x > {a}$", f"$x \\le -{a}$"],
            correct_index=0,
            explanation=f"The square root of a negative quantity is non-real. Thus $x - {a} < 0 \\implies x < {a}$.",
            marks=1,
            hint="The expression under a square root must be strictly negative to yield a non-real result.",
        )

    with_metadata(
        q,
        topic=TOPIC,
        subskill="02_identify_non_real_and_undefined_numbers",
        learning_objective_id=f"{LO}.02_identify_non_real",
        misconception_tags=["confuses_undefined_with_non_real", "thinks_cube_root_of_negative_is_non_real"],
        diagnostic_tags=["number_systems", "non_real"],
        keywords=["non-real", "undefined", "zero denominator", "negative square root"],
    )
    return _add_pillars(q, "02_identify_non_real_and_undefined_numbers", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 03_convert_terminating_decimal_to_fraction
# --------------------------------------------------------------------------- #
def _build_03_convert_terminating_decimal_to_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pairs = [
        (0.25, 1, 4), (0.75, 3, 4), (0.2, 1, 5), (0.4, 2, 5), (0.6, 3, 5),
        (0.8, 4, 5), (0.125, 1, 8), (0.375, 3, 8), (0.625, 5, 8), (0.875, 7, 8),
        (0.15, 3, 20), (0.35, 7, 20), (0.45, 9, 20), (0.65, 13, 20), (0.85, 17, 20),
        (0.04, 1, 25), (0.08, 2, 25), (0.16, 4, 25), (0.32, 8, 25), (0.64, 16, 25),
        (1.25, 5, 4), (1.5, 3, 2), (1.75, 7, 4), (2.4, 12, 5),
    ]
    val, num_val, den_val = r.choice(pairs)
    val_sa = num(val)
    frac_ans = sp.Rational(num_val, den_val)

    sol = solution(
        goal="convert decimal to fraction",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=val_sa, to_expr=f"\\frac{{{int(val * 1000) if val < 1 and int(val*100)%10 != 0 else int(val * 100)}}}{{100}}",
                 op="write over power of 10", rule="decimal place value"),
            step(from_expr=f"\\frac{{{num_val*4}}}{{{den_val*4}}}", to_expr=f"\\frac{{{num_val}}}{{{den_val}}}",
                 op="simplify by dividing highest common factor", rule="simplification"),
        ],
        final_expr=frac_ans,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write the decimal }} {val_sa} \\text{{ as a common fraction in simplest form.}}",
        answer_expr=frac_ans,
        answer_mode="expression",
        answer_latex=f"\\frac{{{num_val}}}{{{den_val}}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"Write {val_sa} as a fraction with denominator 10, 100, or 1000, then divide numerator and denominator by their HCF: {val_sa} = \\frac{{{num_val}}}{{{den_val}}}.",
        hint="Place the decimal digits over 100 or 1000 and divide by the highest common factor.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="03_convert_terminating_decimal_to_fraction",
        learning_objective_id=f"{LO}.03_terminating_decimal",
        misconception_tags=["fails_to_simplify_fraction", "wrong_power_of_ten_denominator"],
        diagnostic_tags=["decimals", "fractions"],
        keywords=["terminating decimal", "fraction", "simplest form"],
    )
    return _add_pillars(q, "03_convert_terminating_decimal_to_fraction", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 04_convert_recurring_single_digit_to_fraction
# --------------------------------------------------------------------------- #
def _build_04_convert_recurring_single_digit_to_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    d = r.choice([1, 2, 4, 5, 7, 8])
    frac = sp.Rational(d, 9)

    sol = solution(
        goal="convert recurring decimal to fraction",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"x = 0{{,}}\\dot{{{d}}}", to_expr=f"10x = {d}{{,}}\\dot{{{d}}}", op="multiply by 10", rule="one recurring digit"),
            step(from_expr=f"10x - x = {d}{{,}}\\dot{{{d}}} - 0{{,}}\\dot{{{d}}}", to_expr=f"9x = {d}", op="subtract equation 1 from equation 2", rule="elimination of recurring tail"),
            step(from_expr=f"9x = {d}", to_expr=f"x = \\frac{{{d}}}{{9}}", op="divide by 9", rule="solve for x"),
        ],
        final_expr=frac,
        final_latex=f"\\frac{{{d}}}{{9}}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert the recurring decimal }} 0{{,}}\\dot{{{d}}} \\text{{ to a fraction in simplest form }} \\frac{{a}}{{b}}.",
        answer_expr=frac,
        answer_mode="expression",
        answer_latex=f"\\frac{{{d}}}{{9}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"Let $x = 0{{,}}\\dot{{{d}}}$. Then $10x = {d}{{,}}\\dot{{{d}}}$. Subtracting gives $9x = {d} \\implies x = \\frac{{{d}}}{{9}}$.",
        hint="Let x equal the decimal, multiply by 10, then subtract x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="04_convert_recurring_single_digit_to_fraction",
        learning_objective_id=f"{LO}.04_recurring_single",
        misconception_tags=["divides_by_10_instead_of_9", "drops_recurring_notation"],
        diagnostic_tags=["decimals", "recurring_decimals"],
        keywords=["recurring decimal", "dot notation", "rational form"],
    )
    return _add_pillars(q, "04_convert_recurring_single_digit_to_fraction", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 05_convert_recurring_double_digit_to_fraction
# --------------------------------------------------------------------------- #
def _build_05_convert_recurring_double_digit_to_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    val_pairs = [
        (12, 4, 33), (15, 5, 33), (18, 2, 11), (21, 7, 33),
        (27, 3, 11), (36, 4, 11), (45, 5, 11), (54, 6, 11),
        (63, 7, 11), (72, 8, 11), (81, 9, 11),
    ]
    num_ab, top, bot = r.choice(val_pairs)
    frac = sp.Rational(top, bot)
    d1 = num_ab // 10
    d2 = num_ab % 10

    sol = solution(
        goal="convert two-digit recurring decimal to fraction",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"x = 0{{,}}\\dot{{{d1}}}\\dot{{{d2}}}", to_expr=f"100x = {num_ab}{{,}}\\dot{{{d1}}}\\dot{{{d2}}}", op="multiply by 100", rule="two recurring digits"),
            step(from_expr=f"100x - x = {num_ab}", to_expr=f"99x = {num_ab}", op="subtract x", rule="cancel recurring part"),
            step(from_expr=f"x = \\frac{{{num_ab}}}{{99}}", to_expr=f"x = \\frac{{{top}}}{{{bot}}}", op="simplify by HCF", rule="simplest form"),
        ],
        final_expr=frac,
        final_latex=f"\\frac{{{top}}}{{{bot}}}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} 0{{,}}\\dot{{{d1}}}\\dot{{{d2}}} \\text{{ to a fraction in simplest form.}}",
        answer_expr=frac,
        answer_mode="expression",
        answer_latex=f"\\frac{{{top}}}{{{bot}}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"Let $x = 0{{,}}\\dot{{{d1}}}\\dot{{{d2}}}$. Then $100x = {num_ab}{{,}}\\dot{{{d1}}}\\dot{{{d2}}}$. Subtracting gives $99x = {num_ab} \\implies x = \\frac{{{num_ab}}}{{99}} = \\frac{{{top}}}{{{bot}}}$.",
        hint="Multiply by 100 because two digits repeat, then subtract x to get 99x.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="05_convert_recurring_double_digit_to_fraction",
        learning_objective_id=f"{LO}.05_recurring_double",
        misconception_tags=["divides_by_100_instead_of_99", "fails_to_simplify"],
        diagnostic_tags=["recurring_decimals", "rational_conversion"],
        keywords=["recurring decimal", "two digits", "rational"],
    )
    return _add_pillars(q, "05_convert_recurring_double_digit_to_fraction", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 06_convert_recurring_mixed_decimal_to_fraction
# --------------------------------------------------------------------------- #
def _build_06_convert_recurring_mixed_decimal_to_fraction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        ("0{,}1\\dot{6}", 1, 6, "10x = 1{,}666\\ldots, 100x = 16{,}666\\ldots, 90x = 15"),
        ("0{,}8\\dot{3}", 5, 6, "10x = 8{,}333\\ldots, 100x = 83{,}333\\ldots, 90x = 75"),
        ("0{,}4\\dot{6}", 7, 15, "10x = 4{,}666\\ldots, 100x = 46{,}666\\ldots, 90x = 42"),
        ("0{,}5\\dot{3}", 8, 15, "10x = 5{,}333\\ldots, 100x = 53{,}333\\ldots, 90x = 48"),
        ("1{,}2\\dot{3}", 37, 30, "10x = 12{,}333\\ldots, 100x = 123{,}333\\ldots, 90x = 111"),
    ]
    prompt_dec, num_top, den_bot, working_note = r.choice(cases)
    frac = sp.Rational(num_top, den_bot)

    sol = solution(
        goal="convert mixed recurring decimal to fraction",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr=f"x = {prompt_dec}", to_expr=f"10x, 100x", op="multiply by 10 and 100", rule="isolate recurring part"),
            step(from_expr="100x - 10x", to_expr=f"90x = {num_top * 90 // den_bot}", op="subtract equations", rule="cancel recurring tail"),
            step(from_expr=f"x = \\frac{{{num_top * 90 // den_bot}}}{{90}}", to_expr=f"x = \\frac{{{num_top}}}{{{den_bot}}}", op="simplify", rule="simplest form"),
        ],
        final_expr=frac,
        final_latex=f"\\frac{{{num_top}}}{{{den_bot}}}",
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert the mixed recurring decimal }} {prompt_dec} \\text{{ to a fraction in simplest form.}}",
        answer_expr=frac,
        answer_mode="expression",
        answer_latex=f"\\frac{{{num_top}}}{{{den_bot}}}",
        marks=3,
        canonical_solution=sol,
        explanation=f"Let $x = {prompt_dec}$. Using {working_note}, we obtain $x = \\frac{{{num_top}}}{{{den_bot}}}$.",
        hint="Multiply by 10 to shift non-repeating digits, then by 100, and subtract.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="06_convert_recurring_mixed_decimal_to_fraction",
        learning_objective_id=f"{LO}.06_recurring_mixed",
        misconception_tags=["subtracts_wrong_multiple_of_ten", "drops_non_repeating_part"],
        diagnostic_tags=["recurring_decimals", "mixed_recurring"],
        keywords=["mixed recurring", "rational conversion"],
    )
    return _add_pillars(q, "06_convert_recurring_mixed_decimal_to_fraction", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 07_round_to_n_decimal_places
# --------------------------------------------------------------------------- #
def _build_07_round_to_n_decimal_places(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    places = r.choice([1, 2, 3])
    whole = r.randint(3, 45)
    frac_digits = [r.randint(0, 9) for _ in range(5)]
    # Ensure next digit after 'places' is decisive (not on boundary)
    val = float(f"{whole}." + "".join(str(d) for d in frac_digits))
    rounded = round(val, places)
    val_sa = num(val)
    rounded_sa = num(rounded, places)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Round off }} {val_sa} \\text{{ to }} {places} \\text{{ decimal place{'s' if places > 1 else ''}.}}",
        answer_expr=sp.Rational(str(rounded)),
        answer_mode="value",
        answer_latex=rounded_sa,
        marks=1,
        explanation=f"Inspect the digit at position {places + 1}. If it is 5 or greater, round up; otherwise leave unchanged: {rounded_sa}.",
        hint=f"Look at the digit immediately to the right of the {places} decimal place.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="07_round_to_n_decimal_places",
        learning_objective_id=f"{LO}.07_rounding",
        misconception_tags=["truncates_instead_of_rounding", "rounds_wrong_position"],
        diagnostic_tags=["rounding", "decimal_places"],
        keywords=["round off", "decimal places", "approximation"],
    )
    return _add_pillars(q, "07_round_to_n_decimal_places", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 08_round_in_practical_context
# --------------------------------------------------------------------------- #
def _build_08_round_in_practical_context(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    context = r.choice(["currency", "distance", "mass"])
    if context == "currency":
        amount = r.randint(120, 890) + r.randint(11, 89) / 100.0 + r.randint(1, 9) / 1000.0
        rounded = round(amount, 2)
        amount_sa = num(amount)
        rounded_sa = num(rounded, 2)
        q = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{A store calculation gives }} R{amount_sa}. \\text{{ Round this amount to the nearest cent (2 decimal places).}}",
            answer_expr=sp.Rational(str(rounded)),
            answer_mode="value",
            answer_latex=f"R{rounded_sa}",
            marks=1,
            explanation=f"To round to the nearest cent, round to 2 decimal places: R{rounded_sa}.",
            hint="Currency is rounded to 2 decimal places (cents).",
        )
    else:
        dist = r.randint(15, 80) + r.randint(100, 999) / 1000.0
        rounded = round(dist, 1)
        dist_sa = num(dist)
        rounded_sa = num(rounded, 1)
        q = make_short(
            prefix=TOPIC,
            prompt_latex=f"\\text{{A running track measurement gives }} {dist_sa}\\text{{ km. Round this to }} 1 \\text{{ decimal place.}}",
            answer_expr=sp.Rational(str(rounded)),
            answer_mode="value",
            answer_latex=f"{rounded_sa}",
            marks=1,
            explanation=f"The digit in the second decimal position determines whether to round up or down: {rounded_sa} km.",
            hint="Look at the hundredths digit.",
        )

    with_metadata(
        q,
        topic=TOPIC,
        subskill="08_round_in_practical_context",
        learning_objective_id=f"{LO}.08_practical_rounding",
        misconception_tags=["wrong_units_rounding", "truncates_cents"],
        diagnostic_tags=["rounding", "practical_math"],
        keywords=["rounding", "cents", "practical context"],
    )
    return _add_pillars(q, "08_round_in_practical_context", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 09_estimate_surd_between_consecutive_integers
# --------------------------------------------------------------------------- #
def _build_09_estimate_surd_between_consecutive_integers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([3, 4, 5, 6, 7, 8, 9])
    sq_low = k ** 2
    sq_high = (k + 1) ** 2
    n_val = r.randint(sq_low + 1, sq_high - 1)

    # Number line SVG
    x_min = k - 1
    x_max = k + 2
    svg_w = 460
    svg_h = 90
    step_px = (svg_w - 60) / (x_max - x_min)
    ticks = "".join(
        f'<line x1="{30 + (i - x_min)*step_px}" y1="40" x2="{30 + (i - x_min)*step_px}" y2="55" stroke="#334155" stroke-width="2" />'
        f'<text x="{30 + (i - x_min)*step_px}" y="75" font-size="14" text-anchor="middle" fill="#1e293b">{i}</text>'
        for i in range(x_min, x_max + 1)
    )
    surd_pos = 30 + (math.sqrt(n_val) - x_min) * step_px
    svg = (
        f'<svg viewBox="0 0 {svg_w} {svg_h}" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:sans-serif;">'
        f'<line x1="20" y1="48" x2="{svg_w - 20}" y2="48" stroke="#64748b" stroke-width="2.5" />'
        f'{ticks}'
        f'<circle cx="{surd_pos:.1f}" cy="48" r="6" fill="#dc2626" />'
        f'<text x="{surd_pos:.1f}" y="28" font-size="13" font-weight="bold" text-anchor="middle" fill="#dc2626">√{n_val}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
    }
    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Without using a calculator, between which two consecutive integers does $\\sqrt{{{n_val}}}$ lie?",
        options=[
            f"${k}$ and ${k+1}$",
            f"${k-1}$ and ${k}$",
            f"${k+1}$ and ${k+2}$",
            f"${sq_low}$ and ${sq_high}$",
        ],
        correct_index=0,
        explanation=f"Since ${sq_low} < {n_val} < {sq_high}$, taking the square root gives $\\sqrt{{{sq_low}}} < \\sqrt{{{n_val}}} < \\sqrt{{{sq_high}}} \\implies {k} < \\sqrt{{{n_val}}} < {k+1}$.",
        marks=2,
        hint=f"Find the perfect squares immediately below and above {n_val}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="09_estimate_surd_between_consecutive_integers",
        learning_objective_id=f"{LO}.09_estimate_surd",
        misconception_tags=["confuses_square_with_square_root", "off_by_one_integer_bound"],
        diagnostic_tags=["surds", "estimation"],
        keywords=["surd", "estimation", "consecutive integers", "perfect squares"],
        diagram_spec=diag,
    )
    return _add_pillars(q, "09_estimate_surd_between_consecutive_integers", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 10_estimate_cube_root_between_integers
# --------------------------------------------------------------------------- #
def _build_10_estimate_cube_root_between_integers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5])
    cb_low = k ** 3
    cb_high = (k + 1) ** 3
    n_val = r.randint(cb_low + 2, cb_high - 2)

    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Without using a calculator, between which two consecutive integers does $\\sqrt[3]{{{n_val}}}$ lie?",
        options=[
            f"${k}$ and ${k+1}$",
            f"${k-1}$ and ${k}$",
            f"${k+1}$ and ${k+2}$",
            f"${cb_low}$ and ${cb_high}$",
        ],
        correct_index=0,
        explanation=f"Since ${cb_low} < {n_val} < {cb_high}$, taking the cube root gives $\\sqrt[3]{{{cb_low}}} < \\sqrt[3]{{{n_val}}} < \\sqrt[3]{{{cb_high}}} \\implies {k} < \\sqrt[3]{{{n_val}}} < {k+1}$.",
        marks=2,
        hint=f"List the cubes: {k}^3 = {cb_low} and {(k+1)}^3 = {cb_high}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="10_estimate_cube_root_between_integers",
        learning_objective_id=f"{LO}.10_estimate_cube_root",
        misconception_tags=["treats_cube_root_as_square_root", "confuses_cube_and_cube_root"],
        diagnostic_tags=["cube_roots", "estimation"],
        keywords=["cube root", "estimation", "perfect cubes"],
    )
    return _add_pillars(q, "10_estimate_cube_root_between_integers", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 11_multiply_monomial_by_binomial
# --------------------------------------------------------------------------- #
def _build_11_multiply_monomial_by_binomial(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k_coeff = nonzero(r, -5, 5, exclude=[1])
    a_coeff = nonzero(r, 1, 5)
    b_coeff = nonzero(r, -7, 7)
    expr = k_coeff * x * (a_coeff * x + b_coeff)
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand monomial by binomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=expanded, op="distribute monomial into bracket",
                 rule="a(b + c) = ab + ac", common_errors=["sign_error", "missed_x_power"]),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand and simplify: }} {to_latex(expr)}",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Multiply each term inside the bracket by ${to_latex(k_coeff * x)}$: ${to_latex(expanded)}$.",
        hint="Use the distributive law: multiply the outside term by both inside terms.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="11_multiply_monomial_by_binomial",
        learning_objective_id=f"{LO}.11_monomial_by_binomial",
        misconception_tags=["sign_error_distributing", "forgets_to_add_exponents"],
        diagnostic_tags=["expansion", "distributive_law"],
        keywords=["monomial", "binomial", "expand"],
    )
    return _add_pillars(q, "11_multiply_monomial_by_binomial", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 12_multiply_monomial_by_trinomial
# --------------------------------------------------------------------------- #
def _build_12_multiply_monomial_by_trinomial(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k_coeff = nonzero(r, -4, 4, exclude=[1])
    a = nonzero(r, 1, 4)
    b = nonzero(r, -5, 5)
    c = nonzero(r, -6, 6)
    trinomial = a * x**2 + b * x + c
    expr = k_coeff * x * trinomial
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand monomial by trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=expanded, op="distribute into all three terms",
                 rule="k*x(ax^2 + bx + c) = ka*x^3 + kb*x^2 + kc*x"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} {to_latex(expr)}",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Multiply every term of the trinomial by ${to_latex(k_coeff * x)}$ to obtain ${to_latex(expanded)}$.",
        hint="Multiply the outside monomial by each of the three terms inside.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="12_multiply_monomial_by_trinomial",
        learning_objective_id=f"{LO}.12_monomial_by_trinomial",
        misconception_tags=["misses_third_term", "sign_error_on_negative_monomial"],
        diagnostic_tags=["expansion", "distributive_law"],
        keywords=["monomial", "trinomial", "expand"],
    )
    return _add_pillars(q, "12_multiply_monomial_by_trinomial", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 13_multiply_binomial_by_binomial_foil
# --------------------------------------------------------------------------- #
def _build_13_multiply_binomial_by_binomial_foil(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, -6, 6)
    c = nonzero(r, 1, 4)
    d = nonzero(r, -6, 6)
    b1 = a * x + b
    b2 = c * x + d
    product = b1 * b2
    expanded = sp.expand(product)

    sol = solution(
        goal="expand binomials via FOIL",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=product, to_expr=f"{a*c}x^2 + {a*d}x + {b*c}x + {b*d}", op="FOIL expansion", rule="(ax+b)(cx+d) = ac*x^2 + ad*x + bc*x + bd"),
            step(from_expr=f"{a*c}x^2 + {a*d}x + {b*c}x + {b*d}", to_expr=expanded, op="combine like terms", rule="add middle x terms"),
        ],
        final_expr=expanded,
    )
    q = make_steps(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand and simplify: }} ({to_latex(b1)})({to_latex(b2)})",
        canonical_solution=sol,
        marks=3,
        explanation=f"Multiply First, Outer, Inner, Last terms, then combine like terms: ${to_latex(expanded)}$.",
        hint="Use FOIL: multiply First, Outer, Inner, Last terms, then group the x terms.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="13_multiply_binomial_by_binomial_foil",
        learning_objective_id=f"{LO}.13_binomial_foil",
        misconception_tags=["forgot_middle_term", "sign_error_on_product"],
        diagnostic_tags=["expansion", "FOIL"],
        keywords=["FOIL", "binomial product", "expand"],
    )
    return _add_pillars(q, "13_multiply_binomial_by_binomial_foil", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 14_square_of_binomial_sum
# --------------------------------------------------------------------------- #
def _build_14_square_of_binomial_sum(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, 1, 7)
    binomial = a * x + b
    expr = binomial ** 2
    expanded = sp.expand(expr)

    sol = solution(
        goal="square a binomial sum",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"({a}x)^2 + 2({a}x)({b}) + ({b})^2", op="apply perfect square formula", rule="(p+q)^2 = p^2 + 2pq + q^2"),
            step(from_expr=f"({a}x)^2 + 2({a}x)({b}) + ({b})^2", to_expr=expanded, op="simplify each term", rule="arithmetic"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} ({to_latex(binomial)})^2",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Square the first term, add twice the product of the two terms, and add the square of the second term: ${to_latex(expanded)}$.",
        hint="Remember that (p + q)^2 = p^2 + 2pq + q^2, do NOT simply square both terms!",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="14_square_of_binomial_sum",
        learning_objective_id=f"{LO}.14_square_binomial_sum",
        misconception_tags=["squares_each_term_separately", "missed_2ab_term"],
        diagnostic_tags=["expansion", "perfect_square"],
        keywords=["square binomial", "perfect square", "expand"],
    )
    return _add_pillars(q, "14_square_of_binomial_sum", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 15_square_of_binomial_difference
# --------------------------------------------------------------------------- #
def _build_15_square_of_binomial_difference(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, 1, 7)
    binomial = a * x - b
    expr = binomial ** 2
    expanded = sp.expand(expr)

    sol = solution(
        goal="square a binomial difference",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"({a}x)^2 - 2({a}x)({b}) + ({b})^2", op="apply formula", rule="(p-q)^2 = p^2 - 2pq + q^2"),
            step(from_expr=f"({a}x)^2 - 2({a}x)({b}) + ({b})^2", to_expr=expanded, op="simplify", rule="arithmetic"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} ({to_latex(binomial)})^2",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Use $(p-q)^2 = p^2 - 2pq + q^2$: $({to_latex(binomial)})^2 = {to_latex(expanded)}$.",
        hint="Note the minus sign on the middle term: (p - q)^2 = p^2 - 2pq + q^2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="15_square_of_binomial_difference",
        learning_objective_id=f"{LO}.15_square_binomial_diff",
        misconception_tags=["sign_error_on_middle_term", "makes_last_term_negative"],
        diagnostic_tags=["expansion", "perfect_square"],
        keywords=["binomial difference", "square", "perfect square"],
    )
    return _add_pillars(q, "15_square_of_binomial_difference", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 16_product_of_sum_and_diff_two_squares
# --------------------------------------------------------------------------- #
def _build_16_product_of_sum_and_diff_two_squares(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 5)
    b = nonzero(r, 1, 8)
    expr = (a * x - b) * (a * x + b)
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand sum and difference of two terms",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"({a}x)^2 - ({b})^2", op="difference of squares identity", rule="(p-q)(p+q) = p^2 - q^2"),
            step(from_expr=f"({a}x)^2 - ({b})^2", to_expr=expanded, op="evaluate squares", rule="arithmetic"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} ({a}x - {b})({a}x + {b})",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"The product of a sum and difference yields the difference of two squares: $({a}x)^2 - ({b})^2 = {to_latex(expanded)}$.",
        hint="The middle terms cancel out: (p - q)(p + q) = p^2 - q^2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="16_product_of_sum_and_diff_two_squares",
        learning_objective_id=f"{LO}.16_sum_and_diff_squares",
        misconception_tags=["retains_middle_term", "adds_squares_instead_of_subtracting"],
        diagnostic_tags=["expansion", "difference_of_squares"],
        keywords=["difference of squares", "product", "conjugate"],
    )
    return _add_pillars(q, "16_product_of_sum_and_diff_two_squares", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 17_multiply_binomial_by_trinomial_special
# --------------------------------------------------------------------------- #
def _build_17_multiply_binomial_by_trinomial_special(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.choice([1, 2, 3, 4])
    sign = r.choice(["sum", "diff"])
    if sign == "sum":
        bin_expr = a * x + b
        tri_expr = (a * x)**2 - (a * b) * x + b**2
        expanded = (a * x)**3 + b**3
    else:
        bin_expr = a * x - b
        tri_expr = (a * x)**2 + (a * b) * x + b**2
        expanded = (a * x)**3 - b**3

    sol = solution(
        goal="expand special binomial by trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"({to_latex(bin_expr)})({to_latex(tri_expr)})",
                 to_expr=f"({a}x)^3 {'+' if sign == 'sum' else '-'} ({b})^3",
                 op="recognise sum/difference of cubes product", rule="(p ± q)(p^2 ∓ pq + q^2) = p^3 ± q^3"),
            step(from_expr=f"({a}x)^3 {'+' if sign == 'sum' else '-'} ({b})^3", to_expr=expanded, op="simplify", rule="powers"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand and simplify: }} ({to_latex(bin_expr)})({to_latex(tri_expr)})",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"This is the factored form of the {'sum' if sign == 'sum' else 'difference'} of two cubes $(p \\pm q)(p^2 \\mp pq + q^2) = p^3 \\pm q^3$. Thus the result is ${to_latex(expanded)}$.",
        hint="Notice the structure: (p ± q)(p^2 ∓ pq + q^2) expands to p^3 ± q^3.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="17_multiply_binomial_by_trinomial_special",
        learning_objective_id=f"{LO}.17_binomial_by_trinomial_special",
        misconception_tags=["does_not_cancel_cross_terms", "wrong_power_on_cubes"],
        diagnostic_tags=["expansion", "sum_diff_cubes"],
        keywords=["binomial", "trinomial", "sum of cubes", "difference of cubes"],
    )
    return _add_pillars(q, "17_multiply_binomial_by_trinomial_special", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 18_multiply_binomial_by_trinomial_general
# --------------------------------------------------------------------------- #
def _build_18_multiply_binomial_by_trinomial_general(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 3)
    b = nonzero(r, -4, 4)
    c = nonzero(r, 1, 3)
    d = nonzero(r, -4, 4)
    e = nonzero(r, -5, 5)
    b_expr = a * x + b
    t_expr = c * x**2 + d * x + e
    product = b_expr * t_expr
    expanded = sp.expand(product)

    sol = solution(
        goal="expand general binomial by trinomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"({to_latex(b_expr)})({to_latex(t_expr)})",
                 to_expr=f"{a}x({to_latex(t_expr)}) + ({b})({to_latex(t_expr)})",
                 op="distribute binomial terms", rule="distributive law"),
            step(from_expr=f"{a}x({to_latex(t_expr)}) + ({b})({to_latex(t_expr)})",
                 to_expr=expanded, op="collect like terms", rule="combine powers"),
        ],
        final_expr=expanded,
    )
    q = make_steps(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand and simplify: }} ({to_latex(b_expr)})({to_latex(t_expr)})",
        canonical_solution=sol,
        marks=3,
        explanation=f"Multiply each term of the trinomial by ${to_latex(a*x)}$ and then by ${b}$, then collect like terms: ${to_latex(expanded)}$.",
        hint="Multiply the trinomial by both terms of the binomial separately, then group like terms.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="18_multiply_binomial_by_trinomial_general",
        learning_objective_id=f"{LO}.18_binomial_trinomial_general",
        misconception_tags=["dropped_intermediate_terms", "sign_error_distributing"],
        diagnostic_tags=["expansion", "polynomials"],
        keywords=["binomial", "trinomial", "expand", "simplify"],
    )
    return _add_pillars(q, "18_multiply_binomial_by_trinomial_general", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 19_expand_and_simplify_two_binomial_products
# --------------------------------------------------------------------------- #
def _build_19_expand_and_simplify_two_binomial_products(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, -5, 5)
    c = nonzero(r, -5, 5)
    d = nonzero(r, -5, 5)
    p1 = (x + a) * (x + b)
    p2 = (x + c) * (x + d)
    expr = p1 - p2
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand and subtract two products",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"({to_latex(p1)}) - ({to_latex(p2)})",
                 to_expr=f"({to_latex(sp.expand(p1))}) - ({to_latex(sp.expand(p2))})",
                 op="expand both products", rule="FOIL"),
            step(from_expr=f"({to_latex(sp.expand(p1))}) - ({to_latex(sp.expand(p2))})",
                 to_expr=expanded, op="distribute negative sign and collect like terms", rule="subtraction"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} (x + {a})(x {'+' if b >= 0 else ''} {b}) - (x {'+' if c >= 0 else ''} {c})(x {'+' if d >= 0 else ''} {d})",
        answer_expr=expanded,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Expand each product keeping the second in brackets, distribute the minus sign, and collect like terms: ${to_latex(expanded)}$.",
        hint="Keep brackets around the second expanded product before distributing the negative sign.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="19_expand_and_simplify_two_binomial_products",
        learning_objective_id=f"{LO}.19_two_products",
        misconception_tags=["sign_error_after_minus", "drops_brackets_too_early"],
        diagnostic_tags=["expansion", "subtraction_of_polynomials"],
        keywords=["expand", "simplify", "brackets", "subtraction"],
    )
    return _add_pillars(q, "19_expand_and_simplify_two_binomial_products", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 20_expand_binomial_squared_minus_product
# --------------------------------------------------------------------------- #
def _build_20_expand_binomial_squared_minus_product(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 5)
    b = nonzero(r, 1, 5)
    sq_part = (x + a) ** 2
    prod_part = (x - b) * (x + b)
    expr = sq_part - prod_part
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand square minus difference of squares",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"(x + {a})^2 - (x - {b})(x + {b})",
                 to_expr=f"(x^2 + {2*a}x + {a**2}) - (x^2 - {b**2})",
                 op="expand both parts", rule="identities"),
            step(from_expr=f"(x^2 + {2*a}x + {a**2}) - (x^2 - {b**2})",
                 to_expr=expanded, op="distribute negative sign and collect terms", rule="simplify"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Simplify: }} (x + {a})^2 - (x - {b})(x + {b})",
        answer_expr=expanded,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"$(x + {a})^2 = x^2 + {2*a}x + {a**2}$ and $(x - {b})(x + {b}) = x^2 - {b**2}$. Subtracting gives $x^2 - x^2 + {2*a}x + {a**2} + {b**2} = {to_latex(expanded)}$.",
        hint="Expand (x + a)^2 using perfect square and (x - b)(x + b) using difference of squares.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="20_expand_binomial_squared_minus_product",
        learning_objective_id=f"{LO}.20_squared_minus_diff_squares",
        misconception_tags=["sign_error_on_b_squared", "forgets_middle_term_of_square"],
        diagnostic_tags=["expansion", "identities"],
        keywords=["perfect square", "difference of squares", "simplify"],
    )
    return _add_pillars(q, "20_expand_binomial_squared_minus_product", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 21_expand_product_with_two_variables
# --------------------------------------------------------------------------- #
def _build_21_expand_product_with_two_variables(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 1, 4)
    b = nonzero(r, -5, 5)
    c = nonzero(r, 1, 4)
    d = nonzero(r, -5, 5)
    b1 = a * x + b * y
    b2 = c * x + d * y
    expr = b1 * b2
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand binomials with two variables",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"{a*c}x^2 + {a*d}xy + {b*c}xy + {b*d}y^2", op="FOIL", rule="two variable expansion"),
            step(from_expr=f"{a*c}x^2 + {a*d}xy + {b*c}xy + {b*d}y^2", to_expr=expanded, op="combine middle xy terms", rule="like terms"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand and simplify: }} ({to_latex(b1)})({to_latex(b2)})",
        answer_expr=expanded,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Apply FOIL and combine the middle $xy$ terms: ${to_latex(expanded)}$.",
        hint="Multiply the terms, paying special attention to the cross terms with xy.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="21_expand_product_with_two_variables",
        learning_objective_id=f"{LO}.21_two_variables",
        misconception_tags=["combines_unlike_powers", "sign_error_on_y_terms"],
        diagnostic_tags=["expansion", "two_variables"],
        keywords=["two variables", "FOIL", "expand"],
    )
    return _add_pillars(q, "21_expand_product_with_two_variables", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 22_expand_cube_of_binomial
# --------------------------------------------------------------------------- #
def _build_22_expand_cube_of_binomial(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, -3, 3)
    expr = (x + a) ** 3
    expanded = sp.expand(expr)

    sol = solution(
        goal="expand cube of binomial",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"(x + {a})(x^2 + {2*a}x + {a**2})", op="write as (x+a)(x+a)^2", rule="power of 3"),
            step(from_expr=f"(x + {a})(x^2 + {2*a}x + {a**2})", to_expr=expanded, op="distribute and collect terms", rule="binomial expansion"),
        ],
        final_expr=expanded,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Expand: }} (x {'+' if a >= 0 else ''} {a})^3",
        answer_expr=expanded,
        answer_mode="expression",
        marks=3,
        canonical_solution=sol,
        explanation=f"Using $(x + a)^3 = x^3 + 3ax^2 + 3a^2x + a^3$: $(x {'+' if a >= 0 else ''} {a})^3 = {to_latex(expanded)}$.",
        hint="Expand (x + a)^2 first, then multiply by (x + a).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="22_expand_cube_of_binomial",
        learning_objective_id=f"{LO}.22_cube_of_binomial",
        misconception_tags=["cubes_each_term_only", "omits_intermediate_squared_terms"],
        diagnostic_tags=["expansion", "binomial_cubes"],
        keywords=["cube of binomial", "expand"],
    )
    return _add_pillars(q, "22_expand_cube_of_binomial", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 23_factorise_common_monomial_factor
# --------------------------------------------------------------------------- #
def _build_23_factorise_common_monomial_factor(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    hcf = r.choice([2, 3, 4, 5, 6])
    p = nonzero(r, 1, 5)
    q_val = nonzero(r, -6, 6)
    expr = sp.expand(hcf * x * (p * x + q_val))
    factored = sp.factor(expr)

    sol = solution(
        goal="factorise by highest common factor",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=expr, to_expr=f"{hcf}x \\cdot ({p}x + {q_val})", op="take out HCF", rule="common factor"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {to_latex(expr)}",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"The highest common factor of the numerical coefficients and variables is ${hcf}x$. Taking this out leaves ${to_latex(factored)}$.",
        hint=f"Find the largest integer and variable power that divides both terms ({hcf}x).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="23_factorise_common_monomial_factor",
        learning_objective_id=f"{LO}.23_common_monomial",
        misconception_tags=["incomplete_common_factor", "drops_variable_factor"],
        diagnostic_tags=["factorisation", "common_factor"],
        keywords=["factorise", "common factor", "HCF"],
    )
    return _add_pillars(q, "23_factorise_common_monomial_factor", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 24_factorise_common_binomial_factor
# --------------------------------------------------------------------------- #
def _build_24_factorise_common_binomial_factor(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 2, 6)
    b = nonzero(r, 2, 6)
    k = nonzero(r, 1, 5)
    bin_factor = x - k
    # a*(x - k) + b*y*(x - k)
    factored = bin_factor * (a + b * y)
    expanded = sp.expand(a * bin_factor) + sp.expand(b * y * bin_factor)

    sol = solution(
        goal="factorise common binomial factor",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"{a}(x - {k}) + {b}y(x - {k})",
                 to_expr=f"(x - {k})({a} + {b}y)",
                 op="take out common bracket (x - k)", rule="common binomial factor"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {a}(x - {k}) + {b}y(x - {k})",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"The bracket $(x - {k})$ is common to both terms. Taking it out as a common factor leaves $(x - {k})({a} + {b}y)$.",
        hint="Identify the bracket shared by both terms and factor it out.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="24_factorise_common_binomial_factor",
        learning_objective_id=f"{LO}.24_common_binomial",
        misconception_tags=["expands_brackets_unnecessarily", "drops_second_term"],
        diagnostic_tags=["factorisation", "common_bracket"],
        keywords=["common bracket", "binomial factor", "factorise"],
    )
    return _add_pillars(q, "24_factorise_common_binomial_factor", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 25_factorise_common_factor_with_sign_change
# --------------------------------------------------------------------------- #
def _build_25_factorise_common_factor_with_sign_change(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = nonzero(r, 2, 6)
    b = nonzero(r, 2, 6)
    k = nonzero(r, 1, 5)
    # a(x - k) - b(k - x) = a(x - k) + b(x - k) = (x - k)(a + b)
    factored = (x - k) * (a + b)

    sol = solution(
        goal="factorise with sign change",
        chain_type="expression",
        var="x",
        steps=[
            step(from_expr=f"{a}(x - {k}) - {b}({k} - x)",
                 to_expr=f"{a}(x - {k}) + {b}(x - {k})",
                 op="rewrite (k - x) as -(x - k) and change sign", rule="sign change: -(b-a) = (a-b)"),
            step(from_expr=f"{a}(x - {k}) + {b}(x - {k})",
                 to_expr=f"(x - {k})({a + b})",
                 op="factor out (x - k)", rule="common factor"),
        ],
        final_expr=factored,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Factorise fully: }} {a}(x - {k}) - {b}({k} - x)",
        answer_expr=factored,
        answer_mode="factored",
        marks=2,
        canonical_solution=sol,
        explanation=f"Rewrite $({k} - x)$ as $-(x - {k})$. The minus sign changes the middle sign: ${a}(x - {k}) + {b}(x - {k}) = {a + b}(x - {k})$.",
        hint="Note that (k - x) = -(x - k). Change the sign in front of the second bracket.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="25_factorise_common_factor_with_sign_change",
        learning_objective_id=f"{LO}.25_sign_change",
        misconception_tags=["fails_to_change_sign", "treats_reversed_bracket_as_identical"],
        diagnostic_tags=["factorisation", "sign_change"],
        keywords=["sign change", "common factor", "reversed bracket"],
    )
    return _add_pillars(q, "25_factorise_common_factor_with_sign_change", duration=3, weight=15)


BUILDERS_01_25: Dict[str, Any] = {
    "01_classify_number_system_rational_irrational": _build_01_classify_number_system_rational_irrational,
    "02_identify_non_real_and_undefined_numbers": _build_02_identify_non_real_and_undefined_numbers,
    "03_convert_terminating_decimal_to_fraction": _build_03_convert_terminating_decimal_to_fraction,
    "04_convert_recurring_single_digit_to_fraction": _build_04_convert_recurring_single_digit_to_fraction,
    "05_convert_recurring_double_digit_to_fraction": _build_05_convert_recurring_double_digit_to_fraction,
    "06_convert_recurring_mixed_decimal_to_fraction": _build_06_convert_recurring_mixed_decimal_to_fraction,
    "07_round_to_n_decimal_places": _build_07_round_to_n_decimal_places,
    "08_round_in_practical_context": _build_08_round_in_practical_context,
    "09_estimate_surd_between_consecutive_integers": _build_09_estimate_surd_between_consecutive_integers,
    "10_estimate_cube_root_between_integers": _build_10_estimate_cube_root_between_integers,
    "11_multiply_monomial_by_binomial": _build_11_multiply_monomial_by_binomial,
    "12_multiply_monomial_by_trinomial": _build_12_multiply_monomial_by_trinomial,
    "13_multiply_binomial_by_binomial_foil": _build_13_multiply_binomial_by_binomial_foil,
    "14_square_of_binomial_sum": _build_14_square_of_binomial_sum,
    "15_square_of_binomial_difference": _build_15_square_of_binomial_difference,
    "16_product_of_sum_and_diff_two_squares": _build_16_product_of_sum_and_diff_two_squares,
    "17_multiply_binomial_by_trinomial_special": _build_17_multiply_binomial_by_trinomial_special,
    "18_multiply_binomial_by_trinomial_general": _build_18_multiply_binomial_by_trinomial_general,
    "19_expand_and_simplify_two_binomial_products": _build_19_expand_and_simplify_two_binomial_products,
    "20_expand_binomial_squared_minus_product": _build_20_expand_binomial_squared_minus_product,
    "21_expand_product_with_two_variables": _build_21_expand_product_with_two_variables,
    "22_expand_cube_of_binomial": _build_22_expand_cube_of_binomial,
    "23_factorise_common_monomial_factor": _build_23_factorise_common_monomial_factor,
    "24_factorise_common_binomial_factor": _build_24_factorise_common_binomial_factor,
    "25_factorise_common_factor_with_sign_change": _build_25_factorise_common_factor_with_sign_change,
}
