"""Grade 12 Mathematics — Bivariate Statistics (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (NSC Paper 2, Question 1: 15–20 marks).
Supports full 8-mark compound exam questions and atomic 3-mark elementary sub-drills for adaptive deconstruction.
Zero-LLM: 100% deterministic SymPy calculations with South African comma decimals ({,}) and JSXGraph diagram specs.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "grade12_math_bivariate_statistics"
LO = "math12_statistics"


# --------------------------------------------------------------------------- #
# Helper: CAPS Correlation Strength Classification
# --------------------------------------------------------------------------- #
def classify_correlation(r_val: float) -> Tuple[str, str, str]:
    """Returns (direction, strength, combined_description) based on CAPS curriculum guidelines:
    |r| = 0: no correlation
    0 < |r| < 0.25: very weak
    0.25 <= |r| < 0.5: weak
    0.5 <= |r| < 0.75: moderate
    0.75 <= |r| < 0.9: strong
    0.9 <= |r| < 1.0: very strong
    |r| = 1.0: perfect
    """
    abs_r = abs(r_val)
    if abs_r == 0.0:
        return ("none", "no correlation", "no correlation")

    direction = "positive" if r_val > 0 else "negative"

    if abs_r >= 0.999:
        strength = "perfect"
    elif abs_r >= 0.9:
        strength = "very strong"
    elif abs_r >= 0.75:
        strength = "strong"
    elif abs_r >= 0.5:
        strength = "moderate"
    elif abs_r >= 0.25:
        strength = "weak"
    else:
        strength = "very weak"

    combined = f"{strength} {direction} correlation"
    return (direction, strength, combined)


# --------------------------------------------------------------------------- #
# Sub-drill 1: elementary_mean_points (3 marks)
# --------------------------------------------------------------------------- #
def _build_mean_points(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding Sub-drill: Calculating the centroid (x_bar, y_bar) through which
    the least squares regression line must pass.
    """
    n = r.randint(5, 7)
    x_base = r.randint(5, 15)
    y_base = r.randint(20, 40)

    xs = [x_base + i * r.randint(2, 4) for i in range(n)]
    ys = [y_base + int(1.8 * (x - x_base)) + r.randint(-3, 3) for x in xs]

    sum_x = sum(xs)
    sum_y = sum(ys)
    x_mean_rat = sp.Rational(sum_x, n)
    y_mean_rat = sp.Rational(sum_y, n)
    x_mean_float = float(x_mean_rat)
    y_mean_float = float(y_mean_rat)

    x_mean_str = num(x_mean_float, 2)
    y_mean_str = num(y_mean_float, 2)

    xs_str = "; ".join(str(x) for x in xs)
    ys_str = "; ".join(str(y) for y in ys)

    steps = [
        step(
            from_latex=rf"\bar{{x}} = \frac{{\sum x}}{{n}} = \frac{{{sum_x}}}{{{n}}}",
            to_latex_str=rf"\bar{{x}} = {x_mean_str}",
            op="calculate mean of independent variable x",
            rule="mean formula",
        ),
        step(
            from_latex=rf"\bar{{y}} = \frac{{\sum y}}{{n}} = \frac{{{sum_y}}}{{{n}}}",
            to_latex_str=rf"\bar{{y}} = {y_mean_str}",
            op="calculate mean of dependent variable y",
            rule="mean formula",
        ),
        step(
            from_latex=rf"(\bar{{x}}; \bar{{y}})",
            to_latex_str=rf"({x_mean_str}; {y_mean_str})",
            op="combine means into centroid coordinate",
            rule="centroid theorem",
            common_errors=["swapped_x_and_y_means", "divided_by_incorrect_n"],
        ),
    ]

    canonical = solution_graph(
        goal="determine mean point (x_bar, y_bar) for bivariate data",
        steps=steps,
        final_latex=rf"(\bar{{x}}; \bar{{y}}) = ({x_mean_str}; {y_mean_str})",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct calculation of x_bar = {sum_x}/{n} = {x_mean_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct calculation of y_bar = {sum_y}/{n} = {y_mean_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Coordinates of centroid point ({x_mean_str}; {y_mean_str})", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "swapped_x_and_y_coordinates", "penalty": -1},
            {"rule": "incorrect_rounding_of_means", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"The mean point $(\bar{x}; \bar{y})$ is the balance point (centroid) of the data. Sum all $x$ values and divide by $n$, then do the same for $y$.",
        "concept": r"The least squares regression line $\hat{y} = a + bx$ always passes through the point of means $(\bar{x}; \bar{y})$, satisfying $\bar{y} = a + b\bar{x}$.",
        "breakdown": f"1. Sum of $x$: $\\sum x = {sum_x}$, so $\\bar{{x}} = \\frac{{{sum_x}}}{{{n}}} = {x_mean_str}$.\n2. Sum of $y$: $\\sum y = {sum_y}$, so $\\bar{{y}} = \\frac{{{sum_y}}}{{{n}}} = {y_mean_str}$.\n3. Mean point: $({x_mean_str}; {y_mean_str})$.",
    }

    table_rows = "".join(f"| {x} | {y} |\n" for x, y in zip(xs, ys))
    prompt = (
        f"A bivariate dataset containing {n} paired observations is given below:\n\n"
        f"| $x$ | $y$ |\n|---|---|\n{table_rows}\n"
        f"Calculate the coordinates of the mean point $(\\bar{{x}}; \\bar{{y}})$ through which the least squares regression line must pass. "
        f"Round your answers to two decimal places where necessary."
    )

    return make_math_question(
        prefix="stat_mean_pt",
        topic=TOPIC,
        subskill="elementary_mean_points",
        learning_objective_id=f"{LO}_mean_point_centroid",
        prompt=prompt,
        prompt_latex=rf"\bar{{x}} = \frac{{{sum_x}}}{{{n}}}, \quad \bar{{y}} = \frac{{{sum_y}}}{{{n}}}",
        answer_latex=rf"(\bar{{x}}; \bar{{y}}) = ({x_mean_str}; {y_mean_str})",
        answer_sympy=f"x_bar={x_mean_str}, y_bar={y_mean_str}",
        sample_answer=f"x_bar = {sum_x} / {n} = {x_mean_str}\ny_bar = {sum_y} / {n} = {y_mean_str}\nMean point = ({x_mean_str}; {y_mean_str})",
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_x_and_y_means", "divided_by_incorrect_n", "premature_rounding_error"],
        keywords=["mean point", "centroid", "least squares regression", "bivariate statistics"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_mean_points",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 2: elementary_correlation_interpretation (3 marks)
# --------------------------------------------------------------------------- #
def _build_correlation_interpretation(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding Sub-drill: Classifying Pearson's correlation coefficient r into
    verbal strength descriptors and interpreting its contextual meaning.
    """
    options = [
        (0.94, "very strong positive", "As $x$ increases, $y$ increases substantially in an almost perfectly straight linear pattern."),
        (0.82, "strong positive", "There is a strong tendency for $y$ to increase as $x$ increases."),
        (0.63, "moderate positive", "There is a moderate upward linear relationship between $x$ and $y$."),
        (0.35, "weak positive", "There is a weak positive linear trend between $x$ and $y$, with considerable scatter."),
        (-0.93, "very strong negative", "As $x$ increases, $y$ decreases substantially in an almost perfectly straight linear pattern."),
        (-0.84, "strong negative", "There is a strong tendency for $y$ to decrease as $x$ increases."),
        (-0.68, "moderate negative", "There is a moderate downward linear relationship between $x$ and $y$."),
        (-0.38, "weak negative", "There is a weak negative linear trend between $x$ and $y$, with considerable scatter."),
    ]
    r_val, expected_desc, expected_meaning = r.choice(options)
    direction, strength, combined_desc = classify_correlation(r_val)
    r_str = num(r_val, 2)

    contexts = [
        ("hours spent playing video games per day", "test score percentage"),
        ("daily maximum temperature in °C", "number of umbrellas sold"),
        ("engine displacement in litres", "fuel consumption in litres per 100 km"),
        ("years of employee experience", "monthly productivity index"),
    ]
    var_x, var_y = r.choice(contexts)

    steps = [
        step(
            from_latex=rf"r = {r_str}",
            to_latex_str=rf"\text{{Sign is }} {'+' if r_val > 0 else '-'} \implies \text{{{direction} correlation}}",
            op="determine direction from algebraic sign of r",
            rule="sign of Pearson's correlation coefficient",
        ),
        step(
            from_latex=rf"|r| = |{r_str}| = {num(abs(r_val), 2)}",
            to_latex_str=rf"\text{{Magnitude lies in }} [0{{,}}75; 0{{,}}9) \implies \text{{{strength}}}" if 0.75 <= abs(r_val) < 0.9 else rf"\text{{Magnitude lies in }} [0{{,}}9; 1) \implies \text{{{strength}}}" if abs(r_val) >= 0.9 else rf"\text{{Magnitude lies in }} [0{{,}}5; 0{{,}}75) \implies \text{{{strength}}}" if abs(r_val) >= 0.5 else rf"\text{{Magnitude lies in }} [0{{,}}25; 0{{,}}5) \implies \text{{{strength}}}",
            op="classify strength based on CAPS absolute value boundaries",
            rule="CAPS correlation strength criteria",
            common_errors=["confused_moderate_and_strong", "ignored_negative_sign_in_direction"],
        ),
        step(
            from_latex=rf"\text{{{combined_desc}}}",
            to_latex_str=rf"\text{{Relationship: }} {expected_desc} \text{{ linear relationship}}",
            op="formulate verbal synthesis",
            rule="statistical interpretation",
        ),
    ]

    canonical = solution_graph(
        goal="interpret Pearson correlation coefficient r in direction and strength",
        steps=steps,
        final_latex=rf"\text{{{combined_desc}}}",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct direction identified: {direction}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct strength descriptor: {strength}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Contextual interpretation: describing how {var_y} relates linearly to {var_x}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "stated_correlation_implies_causation", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Look at the sign of $r$ for direction (+ or -) and the absolute value $|r|$ for the strength band.",
        "concept": "CAPS Guidelines for $|r|$: 0.9 to 1.0 (very strong), 0.75 to 0.9 (strong), 0.5 to 0.75 (moderate), 0.25 to 0.5 (weak), 0 to 0.25 (very weak).",
        "breakdown": f"1. Since $r = {r_str}$ is {'positive' if r_val > 0 else 'negative'}, the direction is {direction}.\n2. Since $|r| = {num(abs(r_val), 2)}$, this falls in the {strength} band.\n3. Combined: {combined_desc}.",
    }

    prompt = (
        f"A statistical investigation into the relationship between {var_x} ($x$) and {var_y} ($y$) "
        f"yielded a Pearson's correlation coefficient of $r = {r_str}$.\n\n"
        f"1. Describe the strength and direction of the linear relationship between the two variables. (2)\n"
        f"2. Explain what this correlation coefficient indicates regarding how {var_y} changes as {var_x} increases. (1)"
    )

    return make_math_question(
        prefix="stat_corr_interp",
        topic=TOPIC,
        subskill="elementary_correlation_interpretation",
        learning_objective_id=f"{LO}_correlation_interpretation",
        prompt=prompt,
        prompt_latex=rf"r = {r_str}",
        answer_latex=rf"\text{{{combined_desc}}}; \quad \text{{{expected_meaning}}}",
        answer_sympy=f"r={r_str}, strength={strength}, direction={direction}",
        sample_answer=(
            f"1. There is a {combined_desc}.\n"
            f"2. {expected_meaning}"
        ),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_correlation_with_causation", "wrong_strength_band", "ignored_negative_sign"],
        keywords=["correlation coefficient", "Pearson r", "bivariate statistics", "linear relationship"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_correlation_interpretation",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Complete Bivariate Regression (8 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_bivariate_statistics(r, difficulty: str) -> Dict[str, Any]:
    """Compound 8-mark NSC Paper 2 Question 1 examination archetype:
    - Least squares regression line y_hat = a + bx
    - Pearson's correlation coefficient r and strength interpretation
    - Prediction using the line (interpolation vs extrapolation) and reliability comment
    - Identification of an outlier point on the scatter plot
    """
    scenarios = [
        {
            "ctx": "A matric Mathematics teacher recorded the weekly study hours ($x$) and trial examination marks in percentage ($y$) for 10 learners.",
            "x_label": "Weekly Study Hours (hours)",
            "y_label": "Trial Examination Mark (%)",
            "x_min": 2,
            "x_max": 20,
            "y_base": 32,
            "slope_ideal": 2.8,
            "pred_interp_x": 12,
            "pred_extrap_x": 28,
            "outlier_rule": "high_mark_low_hours",  # learner with 3 hours and 78% mark
        },
        {
            "ctx": "An agricultural scientist investigated the effect of average summer temperature ($x$, in °C) on daily ice cream parlour sales ($y$, in thousands of Rands) over 10 days.",
            "x_label": "Average Temperature (°C)",
            "y_label": "Daily Sales (R'000)",
            "x_min": 18,
            "x_max": 36,
            "y_base": 14,
            "slope_ideal": 1.5,
            "pred_interp_x": 27,
            "pred_extrap_x": 45,
            "outlier_rule": "low_sales_hot_day",  # power failure day: 34°C but only R12k sales
        },
        {
            "ctx": "A logistics fleet manager recorded the age of delivery vans ($x$, in years) and their annual maintenance cost ($y$, in thousands of Rands) for 10 vehicles.",
            "x_label": "Vehicle Age (years)",
            "y_label": "Annual Maintenance Cost (R'000)",
            "x_min": 1,
            "x_max": 10,
            "y_base": 8,
            "slope_ideal": 3.2,
            "pred_interp_x": 6,
            "pred_extrap_x": 15,
            "outlier_rule": "accident_van",  # 2-year old van with major engine overhaul: R38k cost
        },
    ]
    sc = r.choice(scenarios)

    # Generate 10 bivariate data points with realistic correlation
    n = 10
    raw_xs = sorted(r.sample(range(sc["x_min"], sc["x_max"] + 1), n - 1))

    # Add the outlier x
    if sc["outlier_rule"] == "high_mark_low_hours":
        outlier_x = sc["x_min"] + 1
        outlier_y = sc["y_base"] + int(sc["slope_ideal"] * sc["x_max"] * 0.9)
    elif sc["outlier_rule"] == "low_sales_hot_day":
        outlier_x = sc["x_max"] - 1
        outlier_y = sc["y_base"] - 2
    else:  # accident_van
        outlier_x = sc["x_min"] + 1
        outlier_y = sc["y_base"] + int(sc["slope_ideal"] * sc["x_max"] * 0.8)

    # Generate inlier ys
    raw_ys = []
    for x_val in raw_xs:
        noise = r.randint(-4, 4)
        y_val = int(sc["y_base"] + sc["slope_ideal"] * (x_val - sc["x_min"]) + noise)
        raw_ys.append(y_val)

    # Insert outlier into dataset
    all_pairs = list(zip(raw_xs, raw_ys))
    insert_pos = r.randint(2, 7)
    all_pairs.insert(insert_pos, (outlier_x, outlier_y))

    xs = [p[0] for p in all_pairs]
    ys = [p[1] for p in all_pairs]

    # Deterministic SymPy computation of all least squares quantities
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_x2 = sum(x**2 for x in xs)
    sum_y2 = sum(y**2 for y in ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))

    n_sp = sp.Integer(n)
    denom_b = n_sp * sum_x2 - sum_x**2
    numer_b = n_sp * sum_xy - sum_x * sum_y

    b_exact = sp.Rational(numer_b, denom_b)
    a_exact = sp.Rational(sum_y - b_exact * sum_x, n_sp)

    denom_r = sp.sqrt(denom_b * (n_sp * sum_y2 - sum_y**2))
    r_exact = numer_b / denom_r

    b_float = float(b_exact)
    a_float = float(a_exact)
    r_float = float(r_exact)

    x_mean = float(sp.Rational(sum_x, n_sp))
    y_mean = float(sp.Rational(sum_y, n_sp))

    # Formatted strings
    a_rounded = round(a_float, 2)
    b_rounded = round(b_float, 2)
    r_rounded = round(r_float, 2)

    a_str = num(a_rounded, 2)
    b_str = num(b_rounded, 2)
    r_str = num(r_rounded, 2)
    x_mean_str = num(x_mean, 2)
    y_mean_str = num(y_mean, 2)

    reg_eq_latex = rf"\hat{{y}} = {a_str} + {b_str}x" if b_rounded >= 0 else rf"\hat{{y}} = {a_str} - {num(abs(b_rounded), 2)}x"
    direction, strength, corr_desc = classify_correlation(r_rounded)

    # Question 3: Prediction (randomly choose interpolation or extrapolation)
    is_extrapolation = r.choice([True, False])
    pred_x = sc["pred_extrap_x"] if is_extrapolation else sc["pred_interp_x"]
    pred_y_float = a_rounded + b_rounded * pred_x
    pred_y_str = num(round(pred_y_float, 2), 2)

    interp_type = "extrapolation" if is_extrapolation else "interpolation"
    reliability_comment = (
        f"This is an extrapolation (since $x = {pred_x}$ lies outside the observed data range $[{min(xs)}; {max(xs)}]$). "
        f"Therefore, the prediction is less reliable because we cannot guarantee the linear trend continues beyond the measured interval."
        if is_extrapolation else
        f"This is an interpolation (since $x = {pred_x}$ lies within the observed data range $[{min(xs)}; {max(xs)}]$). "
        f"Therefore, the prediction is considered reliable given the strong correlation."
    )

    # JSXGraph Diagram Spec
    x_padding = (max(xs) - min(xs)) * 0.2
    y_padding = (max(ys) - min(ys)) * 0.2
    diagram_spec = {
        "kind": "scatter_plot_regression",
        "bounding_box": [
            float(min(xs) - x_padding),
            float(max(ys) + y_padding),
            float(max(xs) + x_padding),
            float(min(ys) - y_padding),
        ],
        "points": [{"x": float(x), "y": float(y)} for x, y in zip(xs, ys)],
        "outlier": {"x": float(outlier_x), "y": float(outlier_y)},
        "centroid": {"x": float(x_mean), "y": float(y_mean), "label": f"({x_mean_str}; {y_mean_str})"},
        "regression_line": {
            "a": float(a_rounded),
            "b": float(b_rounded),
            "latex": reg_eq_latex,
        },
        "x_label": sc["x_label"],
        "y_label": sc["y_label"],
        "caption": f"Scatter plot and least squares regression line for {sc['x_label']} vs {sc['y_label']}.",
    }

    steps = [
        step(
            from_latex=rf"b = \frac{{n \sum xy - (\sum x)(\sum y)}}{{n \sum x^2 - (\sum x)^2}} = \frac{{{n}({sum_xy}) - ({sum_x})({sum_y})}}{{{n}({sum_x2}) - ({sum_x})^2}}",
            to_latex_str=rf"b = {b_str}",
            op="calculate slope parameter of least squares regression line",
            rule="least squares slope formula",
        ),
        step(
            from_latex=rf"a = \bar{{y}} - b\bar{{x}} = \frac{{{sum_y}}}{{{n}}} - ({b_str})\left(\frac{{{sum_x}}}{{{n}}}\right)",
            to_latex_str=rf"a = {a_str} \implies {reg_eq_latex}",
            op="calculate y-intercept parameter and assemble regression equation",
            rule="least squares intercept formula",
            common_errors=["swapped_a_and_b", "incorrect_sign_of_slope"],
        ),
        step(
            from_latex=rf"r = \frac{{n \sum xy - (\sum x)(\sum y)}}{{\sqrt{{[n \sum x^2 - (\sum x)^2][n \sum y^2 - (\sum y)^2]}}}}",
            to_latex_str=rf"r = {r_str} \implies \text{{{corr_desc}}}",
            op="compute Pearson correlation coefficient and classify strength",
            rule="Pearson's product-moment correlation",
        ),
        step(
            from_latex=rf"\hat{{y}} = {a_str} + {b_str}({pred_x})",
            to_latex_str=rf"\hat{{y}} = {pred_y_str} \quad ({interp_type})",
            op="evaluate prediction and state domain reliability",
            rule="linear extrapolation / interpolation",
        ),
        step(
            from_latex=rf"\text{{Scatter plot inspection}}",
            to_latex_str=rf"\text{{Outlier at }} ({outlier_x}; {outlier_y})",
            op="identify data point deviating significantly from linear trend",
            rule="bivariate outlier detection",
        ),
    ]

    canonical = solution_graph(
        goal="complete 8-mark bivariate regression and correlation analysis",
        steps=steps,
        final_latex=rf"{reg_eq_latex}; \quad r = {r_str}; \quad \hat{{y}}({pred_x}) = {pred_y_str}; \quad \text{{Outlier: }} ({outlier_x}; {outlier_y})",
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": f"Value of y-intercept: a = {a_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Value of slope: b = {b_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct least squares regression equation: {reg_eq_latex}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Pearson correlation coefficient r = {r_str}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Description of correlation strength and direction: {corr_desc}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Predicted value: y_hat = {pred_y_str}", "marks": 1, "editable": True},
            {"id": "mp7", "desc": f"Identification as {interp_type} with valid reliability comment", "marks": 1, "editable": True},
            {"id": "mp8", "desc": f"Identification of outlier coordinate ({outlier_x}; {outlier_y})", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "swapped_a_and_b_in_equation", "penalty": -1},
            {"rule": "omitted_y_hat_symbol_or_equation", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    table_header = "| Observation | " + " | ".join(f"#{i+1}" for i in range(n)) + " |\n"
    table_sep = "|---|" + "---|"*n + "\n"
    row_x = f"| **{sc['x_label']} ($x$)** | " + " | ".join(str(x) for x in xs) + " |\n"
    row_y = f"| **{sc['y_label']} ($y$)** | " + " | ".join(str(y) for y in ys) + " |\n"
    data_table = table_header + table_sep + row_x + row_y

    prompt = (
        f"**QUESTION 1 [8 MARKS]**\n\n"
        f"{sc['ctx']}\n\n"
        f"{data_table}\n"
        f"**1.1** Determine the equation of the least squares regression line for the data in the form $\\hat{{y}} = a + bx$. "
        f"Round $a$ and $b$ to two decimal places. (3)\n"
        f"**1.2** Write down the value of the Pearson correlation coefficient ($r$) for this dataset. "
        f"Comment on the strength and direction of the correlation. (2)\n"
        f"**1.3** Use your regression equation to predict the value of $y$ when $x = {pred_x}$. "
        f"State whether this prediction is an interpolation or extrapolation, and comment on its reliability. (2)\n"
        f"**1.4** Identify the coordinate $(x; y)$ of the single outlier point present in this dataset. (1)"
    )

    hints = {
        "nudge": "Use the STAT mode on your scientific calculator (Mode -> STAT -> A + BX) to enter the bivariate data pairs and read off A, B, and r.",
        "concept": "Least squares regression: $\\hat{y} = a + bx$. Pearson's $r \\in [-1; 1]$. Predictions within the range $[x_{min}; x_{max}]$ are interpolations (generally reliable), while predictions outside are extrapolations (less reliable).",
        "breakdown": (
            f"1.1: Calculate $a = {a_str}$ and $b = {b_str}$. The equation is ${reg_eq_latex}$.\n"
            f"1.2: The correlation coefficient is $r = {r_str}$. This indicates a {corr_desc}.\n"
            f"1.3: Substitute $x = {pred_x}$: $\\hat{{y}} = {a_str} + ({b_str})({pred_x}) = {pred_y_str}$. {reliability_comment}\n"
            f"1.4: The point $({outlier_x}; {outlier_y})$ visibly diverges from the linear trend of the other 9 observations."
        ),
    }

    return make_math_question(
        prefix="stat_cmp_bivar",
        topic=TOPIC,
        subskill="bivariate_regression_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=rf"{reg_eq_latex}, \quad r = {r_str}, \quad \hat{{y}}({pred_x}) = {pred_y_str}",
        answer_latex=rf"1.1:\ {reg_eq_latex};\ 1.2:\ r = {r_str}\ ({corr_desc});\ 1.3:\ \hat{{y}} = {pred_y_str}\ ({interp_type});\ 1.4:\ ({outlier_x}; {outlier_y})",
        answer_sympy=f"a={a_str}, b={b_str}, r={r_str}, y_pred={pred_y_str}, outlier=({outlier_x},{outlier_y})",
        sample_answer=(
            f"1.1 a = {a_str}, b = {b_str} => {reg_eq_latex}\n"
            f"1.2 r = {r_str} ({corr_desc})\n"
            f"1.3 y_hat({pred_x}) = {pred_y_str}. {reliability_comment}\n"
            f"1.4 Outlier: ({outlier_x}; {outlier_y})"
        ),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_a_and_b_in_equation", "omitted_y_hat_symbol", "confused_extrapolation_and_interpolation"],
        keywords=["least squares regression", "correlation coefficient", "Pearson r", "outlier", "interpolation", "extrapolation", "NSC Paper 2"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=12,
        mode="compound",
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# --------------------------------------------------------------------------- #
# Public Generator Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_bivariate_statistics,
    "bivariate_regression": _build_compound_bivariate_statistics,
    "elementary_mean_points": _build_mean_points,
    "mean_points": _build_mean_points,
    "elementary_correlation_interpretation": _build_correlation_interpretation,
    "correlation_interpretation": _build_correlation_interpretation,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Bivariate Statistics & Regression questions."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill if (subskill and subskill in BUILDERS) else mode
    builder = BUILDERS.get(target, BUILDERS.get(mode, _build_compound_bivariate_statistics))

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
