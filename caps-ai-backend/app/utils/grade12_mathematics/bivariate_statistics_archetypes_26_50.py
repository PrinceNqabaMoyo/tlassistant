"""Grade 12 Mathematics — Statistics Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/01. Statistics.md:
Bivariate scatter plots, least squares regression line y_hat = a + bx,
mean point (x_bar; y_bar), Pearson correlation coefficient r, interpolation vs extrapolation,
outlier identification & effects, and residuals.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
)

TOPIC = "grade12_math_bivariate_statistics"
LO_PREFIX = "math12_statistics"


def classify_correlation(r_val: float) -> Tuple[str, str, str]:
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
    return (direction, strength, f"{strength} {direction} correlation")


def _scatter_regression_svg(
    xs: List[float],
    ys: List[float],
    a_val: float,
    b_val: float,
    title: str,
    outlier: Optional[Tuple[float, float]] = None,
) -> Dict[str, Any]:
    w, h = 440, 240
    pad_l, pad_r, pad_t, pad_b = 50, 30, 32, 38
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    if outlier:
        min_x = min(min_x, outlier[0])
        max_x = max(max_x, outlier[0])
        min_y = min(min_y, outlier[1])
        max_y = max(max_y, outlier[1])

    def sx(x: float) -> float:
        return pad_l + ((x - min_x) / max(max_x - min_x, 1.0)) * (w - pad_l - pad_r)

    def sy(y: float) -> float:
        return (h - pad_b) - ((y - min_y) / max(max_y - min_y, 1.0)) * (h - pad_t - pad_b)

    x1_line, x2_line = min_x, max_x
    y1_line = a_val + b_val * x1_line
    y2_line = a_val + b_val * x2_line

    dots = "".join(
        f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="3.8" fill="#0284c7"/>'
        f'<text x="{sx(x):.1f}" y="{sy(y) - 6:.1f}" font-family="sans-serif" font-size="9" text-anchor="middle" fill="#334155">({x};{y})</text>'
        for x, y in zip(xs, ys)
    )
    out_svg = ""
    if outlier:
        ox, oy = outlier
        out_svg = (
            f'<circle cx="{sx(ox):.1f}" cy="{sy(oy):.1f}" r="5" fill="#dc2626"/>'
            f'<text x="{sx(ox):.1f}" y="{sy(oy) - 8:.1f}" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#dc2626">({ox};{oy})</text>'
        )

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect width="{w}" height="{h}" fill="#ffffff" rx="6"/>'
        f'<text x="220" y="20" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e293b">{title}</text>'
        f'<line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="{pad_l}" y1="{h - pad_b}" x2="{w - pad_r}" y2="{h - pad_b}" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="{sx(x1_line):.1f}" y1="{sy(y1_line):.1f}" x2="{sx(x2_line):.1f}" y2="{sy(y2_line):.1f}" stroke="#16a34a" stroke-width="2" stroke-dasharray="5,3"/>'
        f'{dots}{out_svg}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _make_q2(
    subskill: str,
    prompt: str,
    prompt_latex: str,
    answer_latex: str,
    answer_sympy: str,
    sample_answer: str,
    marks: int = 3,
    difficulty: str = "medium",
    diagram_spec: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    steps = [
        step(from_latex=prompt_latex, to_latex_str=answer_latex, op=f"solve {subskill}", rule=subskill),
    ]
    canonical = solution_graph(goal=subskill, steps=steps, final_latex=answer_latex)
    marking_schema = {
        "total_marks": marks,
        "marking_points": [
            {"id": "mp1", "desc": "Correct bivariate method and substitution", "marks": max(1, marks - 1), "editable": True},
            {"id": "mp2", "desc": f"Final answer: {answer_latex}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Use the least squares regression formulas $\\hat{y} = a + bx$, $\\bar{y} = a + b\\bar{x}$, and Pearson's $r$.",
        "concept": "Remember that the regression line always passes through $(\\bar{x}; \\bar{y})$ and $r$ shares the sign of $b$.",
        "breakdown": sample_answer,
    }
    return make_math_question(
        prefix=f"stat12_{subskill[:12]}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{subskill}",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        answer_sympy=answer_sympy,
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_a_and_b_in_equation", "confused_extrapolation_and_interpolation"],
        keywords=["bivariate statistics", "regression", subskill.replace("_", " ")],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=max(3, marks),
        mode=subskill,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# ---------------------------------------------------------------------------
# Archetypes 26 to 50
# ---------------------------------------------------------------------------
def build_26_bivariate_scatter_plot_trend_direction(r: random.Random) -> Dict[str, Any]:
    pos = r.choice([True, False])
    a_v = r.randint(10, 25) if pos else r.randint(60, 85)
    b_v = r.choice([2, 3, 4]) if pos else r.choice([-2, -3, -4])
    xs = [2, 4, 6, 8, 10]
    ys = [a_v + b_v * x for x in xs]
    d_spec = _scatter_regression_svg(xs, ys, a_v, b_v, f"Bivariate Trend (slope b = {b_v})")
    dir_word = "positive" if pos else "negative"
    return _make_q2(
        "26_bivariate_scatter_plot_trend_direction",
        f"Refer to the scatter plot of points $(2; {ys[0]}), (4; {ys[1]}), (6; {ys[2]}), (8; {ys[3]}), (10; {ys[4]})$. State the direction of the linear relationship and whether the gradient $b$ is positive or negative.",
        rf"b = {b_v}",
        rf"\text{{{dir_word.capitalize()} linear relationship }} (b = {b_v})",
        dir_word,
        f"As $x$ increases from 2 to 10, $y$ changes with gradient $b = {b_v}$, indicating a {dir_word} linear relationship.",
        marks=2,
        diagram_spec=d_spec,
    )


def build_27_mean_point_centroid_of_bivariate_data(r: random.Random) -> Dict[str, Any]:
    x_bar = r.randint(6, 18)
    y_bar = r.randint(25, 55)
    xs = [x_bar - 4, x_bar - 2, x_bar, x_bar + 2, x_bar + 4]
    ys = [y_bar - 6, y_bar - 3, y_bar, y_bar + 3, y_bar + 6]
    sum_x, sum_y = sum(xs), sum(ys)
    return _make_q2(
        "27_mean_point_centroid_of_bivariate_data",
        f"Five paired observations have $x$-values $\\{{{'; '.join(str(x) for x in xs)}\\}}$ and $y$-values $\\{{{'; '.join(str(y) for y in ys)}\\}}$. Calculate the coordinates of the mean point $(\\bar{{x}}; \\bar{{y}})$ through which the least squares regression line passes.",
        rf"(\bar{{x}}; \bar{{y}}) = \left(\frac{{{sum_x}}}{{5}}; \frac{{{sum_y}}}{{5}}\right)",
        rf"({x_bar}; {y_bar})",
        f"({x_bar}, {y_bar})",
        f"$\\bar{{x}} = \\frac{{{sum_x}}}{{5}} = {x_bar}$ and $\\bar{{y}} = \\frac{{{sum_y}}}{{5}} = {y_bar}$. Mean point is $({x_bar}; {y_bar})$.",
        marks=3,
    )


def build_28_least_squares_slope_b_from_summations(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(5, 15)
    b_v = r.randint(2, 5)
    xs = [1, 2, 3, 4, 5]
    ys = [a_v + b_v * x for x in xs]
    n = 5
    sx, sy = sum(xs), sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sx2 = sum(x * x for x in xs)
    return _make_q2(
        "28_least_squares_slope_b_from_summations",
        f"For a dataset of $n = 5$ bivariate observations, the summary totals are $\\sum x = {sx}$, $\\sum y = {sy}$, $\\sum xy = {sxy}$, and $\\sum x^2 = {sx2}$. Calculate the gradient $b$ of the least squares regression line $\\hat{{y}} = a + bx$.",
        rf"b = \frac{{5({sxy}) - ({sx})({sy})}}{{5({sx2}) - ({sx})^2}}",
        rf"b = {b_v}",
        str(b_v),
        f"$b = \\frac{{n\\sum xy - \\sum x \\sum y}}{{n\\sum x^2 - (\\sum x)^2}} = \\frac{{5({sxy}) - ({sx})({sy})}}{{5({sx2}) - {sx*sx}}} = {b_v}$.",
        marks=3,
    )


def build_29_least_squares_intercept_a_from_means_and_b(r: random.Random) -> Dict[str, Any]:
    x_bar = r.randint(5, 14)
    b_v = r.randint(2, 6)
    a_v = r.randint(8, 30)
    y_bar = a_v + b_v * x_bar
    return _make_q2(
        "29_least_squares_intercept_a_from_means_and_b",
        f"A bivariate dataset has means $\\bar{{x}} = {x_bar}$ and $\\bar{{y}} = {y_bar}$. Given that the gradient of the least squares regression line is $b = {b_v}$, calculate the $y$-intercept $a$ and write down the equation $\\hat{{y}} = a + bx$.",
        rf"a = \bar{{y}} - b\bar{{x}} = {y_bar} - ({b_v})({x_bar})",
        rf"a = {a_v}; \quad \hat{{y}} = {a_v} + {b_v}x",
        f"a={a_v}",
        f"Using $\\bar{{y}} = a + b\\bar{{x}}$, we have $a = {y_bar} - {b_v}({x_bar}) = {a_v}$. Thus $\\hat{{y}} = {a_v} + {b_v}x$.",
        marks=2,
        difficulty="easy",
    )


def build_30_full_regression_line_equation_from_table(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(10, 35)
    b_v = r.randint(2, 5)
    xs = [2, 4, 6, 8, 10]
    ys = [a_v + b_v * x for x in xs]
    rows = " | ".join(str(x) for x in xs)
    rows_y = " | ".join(str(y) for y in ys)
    return _make_q2(
        "30_full_regression_line_equation_from_table",
        f"Determine the equation of the least squares regression line $\\hat{{y}} = a + bx$ for the bivariate data table:\n\n"
        f"| $x$ | {rows} |\n|---|{'---|'*5}\n| $y$ | {rows_y} |",
        rf"\hat{{y}} = {a_v} + {b_v}x",
        rf"\hat{{y}} = {a_v} + {b_v}x",
        f"y_hat = {a_v} + {b_v}*x",
        f"From the table, $\\bar{{x}} = 6$, $\\bar{{y}} = {a_v + 6*b_v}$, gradient $b = {b_v}$, and $a = {a_v}$. Equation: $\\hat{{y}} = {a_v} + {b_v}x$.",
        marks=3,
    )


def build_31_regression_slope_from_standard_deviations_and_r(r: random.Random) -> Dict[str, Any]:
    r_val = r.choice([0.8, 0.75, 0.9, -0.8, -0.75])
    sx = r.choice([4, 5, 8])
    sy = sx * r.choice([2, 3])
    b_val = round(r_val * (sy / sx), 2)
    r_s, b_s = num(r_val, 2), num(b_val, 2)
    return _make_q2(
        "31_regression_slope_from_standard_deviations_and_r",
        f"A bivariate dataset has standard deviations $\\sigma_x = {sx}$ and $\\sigma_y = {sy}$, and Pearson correlation coefficient $r = {r_s}$. Calculate the gradient $b$ of the least squares regression line using $b = r \\frac{{\\sigma_y}}{{\\sigma_x}}$.",
        rf"b = {r_s} \times \frac{{{sy}}}{{{sx}}}",
        rf"b = {b_s}",
        b_s,
        f"$b = r \\frac{{\\sigma_y}}{{\\sigma_x}} = {r_s} \\times \\frac{{{sy}}}{{{sx}}} = {b_s}$.",
        marks=2,
    )


def build_32_correlation_r_from_slope_and_standard_deviations(r: random.Random) -> Dict[str, Any]:
    sx = r.choice([3, 4, 5])
    sy = sx * 2
    b_val = r.choice([1.4, 1.6, 1.8, -1.4, -1.6])
    r_val = round(b_val * (sx / sy), 2)
    b_s, r_s = num(b_val, 2), num(r_val, 2)
    return _make_q2(
        "32_correlation_r_from_slope_and_standard_deviations",
        f"Given that the least squares regression slope is $b = {b_s}$, $\\sigma_x = {sx}$, and $\\sigma_y = {sy}$, calculate the Pearson correlation coefficient $r = b \\frac{{\\sigma_x}}{{\\sigma_y}}$.",
        rf"r = {b_s} \times \frac{{{sx}}}{{{sy}}}",
        rf"r = {r_s}",
        r_s,
        f"$r = b \\frac{{\\sigma_x}}{{\\sigma_y}} = {b_s} \\times \\frac{{{sx}}}{{{sy}}} = {r_s}$.",
        marks=2,
    )


def build_33_pearson_r_from_summation_formula(r: random.Random) -> Dict[str, Any]:
    ss_x = r.choice([16, 25, 36])
    ss_y = r.choice([64, 100])
    denom = int(math.isqrt(ss_x * ss_y))
    num_xy = int(denom * 0.8)
    r_val = round(num_xy / denom, 2)
    r_s = num(r_val, 2)
    return _make_q2(
        "33_pearson_r_from_summation_formula",
        f"In a bivariate study, $\\sum(x - \\bar{{x}})(y - \\bar{{y}}) = {num_xy}$, $\\sum(x - \\bar{{x}})^2 = {ss_x}$, and $\\sum(y - \\bar{{y}})^2 = {ss_y}$. Calculate Pearson's correlation coefficient $r$.",
        rf"r = \frac{{{num_xy}}}{{\sqrt{{{ss_x} \times {ss_y}}}}} = \frac{{{num_xy}}}{{{denom}}}",
        rf"r = {r_s}",
        r_s,
        f"$r = \\frac{{\\sum(x-\\bar{{x}})(y-\\bar{{y}})}}{{\\sqrt{{\\sum(x-\\bar{{x}})^2 \\sum(y-\\bar{{y}})^2}}}} = \\frac{{{num_xy}}}{{\\sqrt{{{ss_x * ss_y}}}}} = \\frac{{{num_xy}}}{{{denom}}} = {r_s}$.",
        marks=3,
    )


def build_34_correlation_strength_and_direction_classification(r: random.Random) -> Dict[str, Any]:
    opts = [
        (0.93, "very strong positive correlation"),
        (0.84, "strong positive correlation"),
        (0.64, "moderate positive correlation"),
        (0.36, "weak positive correlation"),
        (-0.92, "very strong negative correlation"),
        (-0.81, "strong negative correlation"),
        (-0.62, "moderate negative correlation"),
    ]
    r_val, desc = r.choice(opts)
    r_s = num(r_val, 2)
    return _make_q2(
        "34_correlation_strength_and_direction_classification",
        f"A statistical analysis between hours of training ($x$) and sprint time ($y$) yields a correlation coefficient of $r = {r_s}$. State the strength and direction of the linear correlation.",
        rf"r = {r_s}",
        rf"\text{{{desc.capitalize()}}}",
        desc,
        f"Since $r = {r_s}$, the relationship is a {desc}.",
        marks=2,
        difficulty="easy",
    )


def build_35_valid_range_and_sign_consistency_of_r_and_b(r: random.Random) -> Dict[str, Any]:
    b_v = r.choice([-3.4, -2.1, -1.5, 2.4, 3.8])
    r_wrong = 1.25 if b_v > 0 else 0.85
    b_s, rw_s = num(b_v, 2), num(r_wrong, 2)
    reason = "r cannot exceed 1 (since -1 <= r <= 1)" if b_v > 0 else "r and slope b must have the same algebraic sign"
    return _make_q2(
        "35_valid_range_and_sign_consistency_of_r_and_b",
        f"A learner calculates a regression line with slope $b = {b_s}$ and claims the correlation coefficient is $r = {rw_s}$. Explain why the learner's value for $r$ is mathematically impossible.",
        rf"b = {b_s}, \quad r = {rw_s}",
        rf"\text{{Invalid because {reason}}}",
        reason,
        f"For $b = {b_s}$ and $r = {rw_s}$, the claim is impossible because {reason}.",
        marks=2,
    )


def build_36_interpolation_y_hat_prediction(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(12, 30)
    b_v = r.randint(3, 6)
    x_pred = r.randint(6, 14)
    y_hat = a_v + b_v * x_pred
    return _make_q2(
        "36_interpolation_y_hat_prediction",
        f"The least squares regression line for observations recorded over the domain $x \\in [2; 20]$ is $\\hat{{y}} = {a_v} + {b_v}x$. Predict $\\hat{{y}}$ when $x = {x_pred}$ and state why this prediction is a reliable interpolation.",
        rf"\hat{{y}} = {a_v} + {b_v}({x_pred}) = {y_hat}",
        rf"\hat{{y}} = {y_hat} \quad (\text{{reliable interpolation within }} [2; 20])",
        str(y_hat),
        f"$\\hat{{y}} = {a_v} + {b_v}({x_pred}) = {y_hat}$. Because $x = {x_pred}$ lies inside the observed interval $[2; 20]$, this is interpolation and is reliable.",
        marks=3,
    )


def build_37_extrapolation_y_hat_and_reliability_critique(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(15, 35)
    b_v = r.randint(2, 5)
    x_ext = r.randint(28, 40)
    y_hat = a_v + b_v * x_ext
    return _make_q2(
        "37_extrapolation_y_hat_and_reliability_critique",
        f"A regression line $\\hat{{y}} = {a_v} + {b_v}x$ was derived from data with $x \\in [4; 16]$. Calculate the predicted value $\\hat{{y}}$ at $x = {x_ext}$, name this type of prediction, and comment on its reliability.",
        rf"\hat{{y}} = {a_v} + {b_v}({x_ext}) = {y_hat}",
        rf"\hat{{y}} = {y_hat}; \quad \text{{Extrapolation (unreliable outside }} [4; 16]\text{{)}}",
        str(y_hat),
        f"$\\hat{{y}} = {a_v} + {b_v}({x_ext}) = {y_hat}$. Since $x = {x_ext}$ lies outside $[4; 16]$, this is extrapolation and is unreliable because the linear trend may not continue.",
        marks=3,
    )


def build_38_inverse_prediction_x_from_given_y_hat(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(10, 28)
    b_v = r.randint(3, 7)
    x_ans = r.randint(5, 15)
    y_giv = a_v + b_v * x_ans
    return _make_q2(
        "38_inverse_prediction_x_from_given_y_hat",
        f"Given the least squares regression equation $\\hat{{y}} = {a_v} + {b_v}x$, determine the value of $x$ for which the predicted value is $\\hat{{y}} = {y_giv}$.",
        rf"{y_giv} = {a_v} + {b_v}x",
        rf"x = {x_ans}",
        str(x_ans),
        f"${y_giv} = {a_v} + {b_v}x \\implies {b_v}x = {y_giv - a_v} \\implies x = {x_ans}$.",
        marks=2,
        difficulty="easy",
    )


def build_39_residual_calculation_at_observed_point(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(8, 22)
    b_v = r.randint(2, 5)
    x_i = r.randint(4, 12)
    y_hat = a_v + b_v * x_i
    res = r.choice([-5, -4, -3, 3, 4, 5])
    y_i = y_hat + res
    return _make_q2(
        "39_residual_calculation_at_observed_point",
        f"A dataset has regression line $\\hat{{y}} = {a_v} + {b_v}x$. For the observed data point $({x_i}; {y_i})$, calculate the predicted value $\\hat{{y}}$ and the residual $e = y - \\hat{{y}}$.",
        rf"\hat{{y}} = {y_hat}, \quad e = {y_i} - {y_hat}",
        rf"\hat{{y}} = {y_hat}; \quad e = {res}",
        str(res),
        f"Predicted $\\hat{{y}} = {a_v} + {b_v}({x_i}) = {y_hat}$. Residual $e = y - \\hat{{y}} = {y_i} - {y_hat} = {res}$.",
        marks=3,
    )


def build_40_point_above_or_below_regression_line(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(10, 25)
    b_v = r.randint(2, 4)
    x_i = r.randint(5, 11)
    y_hat = a_v + b_v * x_i
    above = r.choice([True, False])
    diff = r.randint(3, 7)
    y_i = y_hat + diff if above else y_hat - diff
    pos_word = "above" if above else "below"
    return _make_q2(
        "40_point_above_or_below_regression_line",
        f"Given the regression line $\\hat{{y}} = {a_v} + {b_v}x$, determine whether the observed point $({x_i}; {y_i})$ lies above or below the regression line, and justify your answer.",
        rf"y = {y_i}, \quad \hat{{y}}({x_i}) = {y_hat}",
        rf"\text{{Lies {pos_word} the line since }} y = {y_i} {'>' if above else '<'} \hat{{y}} = {y_hat}",
        pos_word,
        f"At $x = {x_i}$, $\\hat{{y}} = {a_v} + {b_v}({x_i}) = {y_hat}$. Since $y = {y_i} {'>' if above else '<'} {y_hat}$, the point lies {pos_word} the regression line.",
        marks=2,
    )


def build_41_sum_of_squared_residuals_principle(r: random.Random) -> Dict[str, Any]:
    e1, e2, e3 = r.randint(1, 4), -r.randint(2, 5), r.randint(1, 3)
    ssr = e1 * e1 + e2 * e2 + e3 * e3
    return _make_q2(
        "41_sum_of_squared_residuals_principle",
        f"Three observations have vertical residuals $e_1 = {e1}$, $e_2 = {e2}$, and $e_3 = {e3}$ from a fitted line. Calculate the sum of squared residuals $\\sum (y_i - \\hat{{y}}_i)^2$ and state how the least squares regression line chooses $a$ and $b$.",
        rf"\sum e_i^2 = ({e1})^2 + ({e2})^2 + ({e3})^2 = {ssr}",
        rf"\sum e_i^2 = {ssr} \quad (\text{{least squares minimises }} \sum (y_i - \hat{{y}}_i)^2)",
        str(ssr),
        f"$\\sum e_i^2 = {e1*e1} + {e2*e2} + {e3*e3} = {ssr}$. The least squares method selects $a$ and $b$ so that $\\sum (y_i - \\hat{{y}}_i)^2$ is minimised.",
        marks=3,
    )


def build_42_finding_missing_y_coordinate_via_mean_point(r: random.Random) -> Dict[str, Any]:
    x_bar = r.randint(6, 12)
    a_v = r.randint(8, 20)
    b_v = r.randint(2, 4)
    y_bar = a_v + b_v * x_bar
    known_y = [y_bar - 5, y_bar - 2, y_bar + 1, y_bar + 4]
    k_ans = 5 * y_bar - sum(known_y)
    return _make_q2(
        "42_finding_missing_y_coordinate_via_mean_point",
        f"Five bivariate data points have $\\bar{{x}} = {x_bar}$ and least squares regression line $\\hat{{y}} = {a_v} + {b_v}x$. The five $y$-values are $\\{{{'; '.join(str(v) for v in known_y)}; k\\}}$. Calculate $\\bar{{y}}$ and hence find the value of $k$.",
        rf"\bar{{y}} = {a_v} + {b_v}({x_bar}) = {y_bar} \implies \frac{{{sum(known_y)} + k}}{{5}} = {y_bar}",
        rf"\bar{{y}} = {y_bar}; \quad k = {k_ans}",
        str(k_ans),
        f"Since $(\\bar{{x}}; \\bar{{y}})$ lies on the regression line, $\\bar{{y}} = {a_v} + {b_v}({x_bar}) = {y_bar}$. Thus ${sum(known_y)} + k = 5({y_bar}) = {5*y_bar} \\implies k = {k_ans}$.",
        marks=3,
    )


def build_43_finding_missing_x_coordinate_via_mean_point(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(6, 18)
    b_v = r.randint(2, 5)
    x_bar = r.randint(5, 11)
    y_bar = a_v + b_v * x_bar
    known_x = [x_bar - 3, x_bar - 1, x_bar + 1, x_bar + 2]
    p_ans = 5 * x_bar - sum(known_x)
    return _make_q2(
        "43_finding_missing_x_coordinate_via_mean_point",
        f"Five paired observations have $\\bar{{y}} = {y_bar}$ and regression equation $\\hat{{y}} = {a_v} + {b_v}x$. The five $x$-values are $\\{{{'; '.join(str(v) for v in known_x)}; p\\}}$. Calculate $\\bar{{x}}$ and hence find $p$.",
        rf"{y_bar} = {a_v} + {b_v}\bar{{x}} \implies \bar{{x}} = {x_bar}",
        rf"\bar{{x}} = {x_bar}; \quad p = {p_ans}",
        str(p_ans),
        f"Substitute $\\bar{{y}} = {y_bar}$ into $\\bar{{y}} = {a_v} + {b_v}\\bar{{x}}$ to get $\\bar{{x}} = {x_bar}$. Then ${sum(known_x)} + p = 5({x_bar}) \\implies p = {p_ans}$.",
        marks=3,
    )


def build_44_outlier_identification_on_scatter_plot(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(10, 20)
    b_v = r.randint(2, 4)
    xs = [2, 4, 6, 8, 10]
    ys = [a_v + b_v * x for x in xs]
    ox = r.choice([3, 5, 7])
    oy = a_v + b_v * 10 + r.randint(18, 28)
    d_spec = _scatter_regression_svg(xs, ys, a_v, b_v, f"Scatter Plot with Outlier ({ox};{oy})", outlier=(ox, oy))
    return _make_q2(
        "44_outlier_identification_on_scatter_plot",
        f"Refer to the scatter plot containing inlier points along $\\hat{{y}} = {a_v} + {b_v}x$ and one anomalous observation $({ox}; {oy})$. Identify the coordinates of the outlier and explain why it is classified as an outlier.",
        rf"\text{{Outlier}} = ({ox}; {oy})",
        rf"({ox}; {oy}) \text{{ — lies far above the linear trend }} \hat{{y}} = {a_v} + {b_v}x",
        f"({ox}, {oy})",
        f"The point $({ox}; {oy})$ has a large positive residual relative to $\\hat{{y}} = {a_v} + {b_v}x$ and deviates markedly from the linear trend.",
        marks=2,
        diagram_spec=d_spec,
    )


def build_45_outlier_removal_effect_on_correlation_r(r: random.Random) -> Dict[str, Any]:
    r_before = round(r.uniform(0.58, 0.72), 2)
    r_after = round(r.uniform(0.89, 0.97), 2)
    rb_s, ra_s = num(r_before, 2), num(r_after, 2)
    return _make_q2(
        "45_outlier_removal_effect_on_correlation_r",
        f"A positively correlated dataset initially has $r = {rb_s}$ when a severe outlier is included. After removing the outlier, the recalculated coefficient is $r = {ra_s}$. Explain why removing the outlier caused $r$ to increase closer to $1$.",
        rf"r: {rb_s} \to {ra_s}",
        rf"r \text{{ increases from }} {rb_s} \text{{ to }} {ra_s} \text{{ because scatter around the line decreases}}",
        ra_s,
        f"Removing the outlier reduces the sum of squared residuals around the line of best fit, so the remaining points cluster much more tightly along a straight line ($r$ increases from ${rb_s}$ to ${ra_s}$).",
        marks=2,
    )


def build_46_outlier_removal_effect_on_regression_slope_and_intercept(r: random.Random) -> Dict[str, Any]:
    x_max = r.randint(12, 18)
    y_low = r.randint(8, 15)
    return _make_q2(
        "46_outlier_removal_effect_on_regression_slope_and_intercept",
        f"In a positively correlated scatter plot on $x \\in [2; {x_max}]$, a single outlier is located at a large $x$-value $({x_max}; {y_low})$ far below the regression line. State how removing this outlier affects the gradient $b$ and the mean $\\bar{{y}}$.",
        rf"\text{{Remove low outlier at }} x = {x_max}",
        r"\text{Both the gradient } b \text{ and the mean } \bar{y} \text{ increase}",
        "both b and y_bar increase",
        f"Because the outlier at $({x_max}; {y_low})$ pulled the right end of the regression line and the average $\\bar{{y}}$ downward, removing it causes both the gradient $b$ and $\\bar{{y}}$ to increase.",
        marks=2,
    )


def build_47_contextual_interpretation_of_slope_b(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(25, 45)
    b_v = r.randint(4, 9)
    return _make_q2(
        "47_contextual_interpretation_of_slope_b",
        f"The relationship between weekly study hours ($x$) and test score percentage ($\\hat{{y}}$) is modelled by $\\hat{{y}} = {a_v} + {b_v}x$. Interpret the practical meaning of the gradient $b = {b_v}$ in this context.",
        rf"b = {b_v}",
        rf"\text{{For each additional hour of weekly study, the predicted test score increases by }} {b_v}\%",
        str(b_v),
        f"The slope $b = {b_v}$ means that for every $1\\text{{ hour}}$ increase in weekly study time ($x$), the predicted test mark ($\\hat{{y}}$) increases by ${b_v}\\%$.",
        marks=2,
        difficulty="easy",
    )


def build_48_contextual_interpretation_of_intercept_a(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(28, 48)
    b_v = r.randint(3, 7)
    return _make_q2(
        "48_contextual_interpretation_of_intercept_a",
        f"A fleet manager models annual vehicle maintenance cost $\\hat{{y}}$ (in thousands of Rands) against distance driven $x$ (in thousands of km) using $\\hat{{y}} = {a_v} + {b_v}x$. Interpret the practical meaning of the $y$-intercept $a = {a_v}$.",
        rf"a = {a_v} \text{{ when }} x = 0",
        rf"\text{{Fixed baseline maintenance cost of R}}{a_v}\text{{ 000 when }} x = 0\text{{ km}}",
        str(a_v),
        f"When $x = 0\\text{{ km}}$, $\\hat{{y}} = {a_v}$, representing the predicted baseline annual maintenance cost of $\\text{{R}}{a_v}\\text{{ 000}}$ even before distance is driven.",
        marks=2,
        difficulty="easy",
    )


def build_49_correlation_vs_causation_critique(r: random.Random) -> Dict[str, Any]:
    r_val = round(r.uniform(0.82, 0.94), 2)
    r_s = num(r_val, 2)
    return _make_q2(
        "49_correlation_vs_causation_critique",
        f"A coastal municipality observes a correlation coefficient of $r = {r_s}$ between daily ice-cream sales ($x$) and the number of beach rescues ($y$). A reporter claims that eating ice-cream causes swimming emergencies. Critique this claim statistically.",
        rf"r = {r_s} \not\implies \text{{causation}}",
        r"\text{Correlation does not imply causation; ambient summer temperature is the confounding variable}",
        "correlation does not imply causation",
        f"Although $r = {r_s}$ shows a strong positive correlation, correlation does not imply causation. High summer temperature is a confounding variable that independently increases both ice-cream sales and beach swimming attendance.",
        marks=2,
    )


def build_50_comprehensive_bivariate_regression_synthesis(r: random.Random) -> Dict[str, Any]:
    a_v = r.randint(15, 30)
    b_v = r.randint(3, 5)
    xs = [2, 4, 6, 8, 10]
    ys = [a_v + b_v * x for x in xs]
    x_bar, y_bar = 6, a_v + 6 * b_v
    x_pred = r.randint(5, 9)
    y_pred = a_v + b_v * x_pred
    d_spec = _scatter_regression_svg(xs, ys, a_v, b_v, f"Regression Analysis: y_hat = {a_v} + {b_v}x")
    return _make_q2(
        "50_comprehensive_bivariate_regression_synthesis",
        f"Refer to the scatter plot of the 5 data points $(2; {ys[0]}), (4; {ys[1]}), (6; {ys[2]}), (8; {ys[3]}), (10; {ys[4]})$.\n\n"
        f"1. Write down the coordinates of the mean point $(\\bar{{x}}; \\bar{{y}})$.\n"
        f"2. Determine the least squares regression line equation $\\hat{{y}} = a + bx$.\n"
        f"3. Predict $\\hat{{y}}$ when $x = {x_pred}$ and state whether this is interpolation or extrapolation.",
        rf"(\bar{{x}}; \bar{{y}}) = ({x_bar}; {y_bar}), \quad \hat{{y}} = {a_v} + {b_v}x",
        rf"1.\ ({x_bar}; {y_bar}); \quad 2.\ \hat{{y}} = {a_v} + {b_v}x; \quad 3.\ \hat{{y}}({x_pred}) = {y_pred}\ (\text{{interpolation}})",
        f"mean=({x_bar},{y_bar}), a={a_v}, b={b_v}, y_pred={y_pred}",
        f"1. $\\bar{{x}} = 6, \\bar{{y}} = {y_bar} \\implies ({x_bar}; {y_bar})$.\n2. $\\hat{{y}} = {a_v} + {b_v}x$.\n3. $\\hat{{y}}({x_pred}) = {a_v} + {b_v}({x_pred}) = {y_pred}$ (interpolation inside $[2; 10]$).",
        marks=6,
        difficulty="hard",
        diagram_spec=d_spec,
    )


ARCHETYPES_26_50: Dict[str, Any] = {
    "26_bivariate_scatter_plot_trend_direction": build_26_bivariate_scatter_plot_trend_direction,
    "27_mean_point_centroid_of_bivariate_data": build_27_mean_point_centroid_of_bivariate_data,
    "28_least_squares_slope_b_from_summations": build_28_least_squares_slope_b_from_summations,
    "29_least_squares_intercept_a_from_means_and_b": build_29_least_squares_intercept_a_from_means_and_b,
    "30_full_regression_line_equation_from_table": build_30_full_regression_line_equation_from_table,
    "31_regression_slope_from_standard_deviations_and_r": build_31_regression_slope_from_standard_deviations_and_r,
    "32_correlation_r_from_slope_and_standard_deviations": build_32_correlation_r_from_slope_and_standard_deviations,
    "33_pearson_r_from_summation_formula": build_33_pearson_r_from_summation_formula,
    "34_correlation_strength_and_direction_classification": build_34_correlation_strength_and_direction_classification,
    "35_valid_range_and_sign_consistency_of_r_and_b": build_35_valid_range_and_sign_consistency_of_r_and_b,
    "36_interpolation_y_hat_prediction": build_36_interpolation_y_hat_prediction,
    "37_extrapolation_y_hat_and_reliability_critique": build_37_extrapolation_y_hat_and_reliability_critique,
    "38_inverse_prediction_x_from_given_y_hat": build_38_inverse_prediction_x_from_given_y_hat,
    "39_residual_calculation_at_observed_point": build_39_residual_calculation_at_observed_point,
    "40_point_above_or_below_regression_line": build_40_point_above_or_below_regression_line,
    "41_sum_of_squared_residuals_principle": build_41_sum_of_squared_residuals_principle,
    "42_finding_missing_y_coordinate_via_mean_point": build_42_finding_missing_y_coordinate_via_mean_point,
    "43_finding_missing_x_coordinate_via_mean_point": build_43_finding_missing_x_coordinate_via_mean_point,
    "44_outlier_identification_on_scatter_plot": build_44_outlier_identification_on_scatter_plot,
    "45_outlier_removal_effect_on_correlation_r": build_45_outlier_removal_effect_on_correlation_r,
    "46_outlier_removal_effect_on_regression_slope_and_intercept": build_46_outlier_removal_effect_on_regression_slope_and_intercept,
    "47_contextual_interpretation_of_slope_b": build_47_contextual_interpretation_of_slope_b,
    "48_contextual_interpretation_of_intercept_a": build_48_contextual_interpretation_of_intercept_a,
    "49_correlation_vs_causation_critique": build_49_correlation_vs_causation_critique,
    "50_comprehensive_bivariate_regression_synthesis": build_50_comprehensive_bivariate_regression_synthesis,
}
