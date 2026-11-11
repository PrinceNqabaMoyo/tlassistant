"""Constant ratio and exponential growth/decay relationships (Subskills 19-27) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Identify a constant ratio relationship from a table (y_{n+1} / y_n = constant)."""
    # e.g. Year 0 = 1000, Year 1 = 1100, Year 2 = 1210, Year 3 = 1331 (ratio = 1.10)
    ratio = 1.10
    ans_str = "Constant Ratio (Exponential) with growth factor of 1,10"

    prompt = (
        f"A financial analyst monitors the value of a high-tech stock index over 3 years:\n\n"
        f"| Year (x) | 0 | 1 | 2 | 3 |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Index Value (y) | 1 000 | 1 100 | 1 210 | 1 331 |\n\n"
        f"Identify the mathematical type of this relationship and calculate the constant ratio (growth factor)."
    )
    explanation = (
        f"Step 1: Test the ratios of consecutive terms:\n"
        f"- 1 100 ÷ 1 000 = 1,10\n"
        f"- 1 210 ÷ 1 100 = 1,10\n"
        f"- 1 331 ÷ 1 210 = 1,10. [1 mark]\n"
        f"Step 2: Note that since the ratio is constant (not the difference), it is a constant ratio / exponential growth relationship. [1 mark]\n"
        f"Step 3: State the relationship and growth factor:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "Linear with constant difference of 100",
        "Inverse Proportion with constant product",
        "Step-function relationship",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_19",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide each term by the previous term (1 100 ÷ 1 000 = 1,10).",
        "Since the ratio is constant at 1,10, the relationship is exponential / constant ratio.",
        f"Answer = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Generate table of values for a compounding inflation increase."""
    name = r.choice(SA_NAMES)
    base_cost = 3000.0
    rate = 7.4
    # Yr 1 = 3000 * 1.074 = 3222
    # Yr 2 = 3222 * 1.074 = 3460.43
    val_yr2 = round(base_cost * ((1.0 + rate / 100.0) ** 2), 2)
    ans_str = _fmt_curr(val_yr2)

    prompt = (
        f"{name}'s household grocery budget is {_fmt_curr(base_cost)} in 2024.\n"
        f"If food inflation remains constant at {_fmt(rate)}% per annum compounded annually,\n"
        f"calculate the projected monthly grocery budget after 2 years (in 2026).\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Calculate Year 1 cost (2025):\n"
        f"\\text{{Cost 2025}} = 3\\,000 + (3\\,000 \\times 0,074) = {_fmt_curr(base_cost * 1.074)}. [1 mark]\n"
        f"Step 2: Calculate Year 2 cost (2026) by compounding on the Year 1 cost:\n"
        f"\\text{{Cost 2026}} = 3\\,222 \\times 1,074 = {val_yr2:.2f} [1 mark]\n"
        f"Step 3: State the final projected budget:\n"
        f"\\text{{Projected budget}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(base_cost * (1.0 + 0.074 * 2), 2)),  # Simple
        _fmt_curr(round(val_yr2 + 150, 2)),
        _fmt_curr(round(val_yr2 - 120, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_20",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply R 3 000 by 1,074 twice (or by 1,074^2).",
        f"3 000 × (1,074)^2 = {val_yr2:.2f}.",
        f"Budget = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Compare linear growth vs constant ratio exponential growth over multiple periods."""
    initial = 1000.0
    # Linear: adds R 100 each year -> Yr 5 = 1000 + 500 = 1500
    # Exponential: grows by 10% each year -> Yr 5 = 1000 * (1.10)^5 = 1610.51
    lin_5 = initial + (100.0 * 5)
    exp_5 = round(initial * (1.10 ** 5), 2)
    diff = round(exp_5 - lin_5, 2)
    ans_str = f"Exponential growth is higher by {_fmt_curr(diff)}"

    prompt = (
        f"Two investment scenarios start with an initial deposit of {_fmt_curr(initial)}:\n"
        f"• Scenario A (Linear Growth): Adds a fixed R 100,00 each year for 5 years.\n"
        f"• Scenario B (Exponential Growth): Increases by 10,0% of the previous year's balance each year for 5 years.\n\n"
        f"Calculate the value of both investments at the end of 5 years and determine which scenario yields more, and by how much."
    )
    explanation = (
        f"Step 1: Calculate Scenario A value at Year 5:\n"
        f"A_{{linear}} = 1\\,000 + (100 \\times 5) = {_fmt_curr(lin_5)}. [1 mark]\n"
        f"Step 2: Calculate Scenario B value at Year 5:\n"
        f"A_{{exponential}} = 1\\,000(1,10)^5 = {_fmt_curr(exp_5)}. [1 mark]\n"
        f"Step 3: Subtract to compare:\n"
        f"{_fmt(exp_5)} - {_fmt(lin_5)} = {diff:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Linear growth is higher by {_fmt_curr(diff)}",
        f"Exponential growth is higher by {_fmt_curr(round(diff * 1.5, 2))}",
        "Both scenarios reach the exact same amount at Year 5",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_21",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate linear total (R 1 500) and exponential total (1 000 × 1,10^5 = R 1 610,51), then subtract.",
        f"A = {_fmt_curr(lin_5)}. B = {_fmt_curr(exp_5)}. Difference = {_fmt_curr(diff)}.",
        f"Result = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Exponential population growth projection in an urban municipality."""
    initial_pop = 120000
    growth_rate = 3.0  # 3% per year
    years = 4
    future_pop = int(round(initial_pop * ((1.0 + growth_rate / 100.0) ** years)))
    ans_str = f"{_fmt(future_pop)} residents"

    prompt = (
        f"A fast-growing municipal district in Gauteng has an estimated population of {_fmt(initial_pop)} residents.\n"
        f"Town planners project that the population will grow exponentially at a constant rate of 3,0% per year.\n"
        f"Predict the population of the district after {years} years.\n"
        f"*(Formula: P = P_0(1 + r)^n. Round to the nearest whole person.)*"
    )
    explanation = (
        f"Step 1: Identify P_0 = {initial_pop:,}, r = 0,03, n = {years}. [1 mark]\n"
        f"Step 2: Substitute into formula:\n"
        f"P = {initial_pop:,} \\times (1 + 0,03)^{years} = {initial_pop:,} \\times (1,03)^4 [1 mark]\n"
        f"Step 3: State the rounded population:\n"
        f"\\text{{Projected population}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(int(round(initial_pop * (1.0 + 0.03 * years))))} residents",  # Linear
        f"{_fmt(future_pop + 5000)} residents",
        f"{_fmt(future_pop - 4000)} residents",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_22",
        prompt,
        ans_str,
        options,
        explanation,
        f"Calculate {initial_pop:,} × (1,03)^4.",
        f"{initial_pop:,} × (1,03)^4 = {future_pop:,}.",
        f"Population = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Exponential decay / reducing balance depreciation of a vehicle."""
    initial_cost = 200000.0
    deprec_rate = 15.0  # 15% reducing balance
    years = 3
    # A = P(1 - r)^n
    factor = (1.0 - deprec_rate / 100.0) ** years  # 0.85^3
    future_val = round(initial_cost * factor, 2)
    ans_str = _fmt_curr(future_val)

    prompt = (
        f"A commercial delivery van was purchased for {_fmt_curr(initial_cost)}.\n"
        f"The van depreciates according to the reducing-balance method (exponential decay) at a rate of 15,0% per annum.\n"
        f"Calculate the book value of the delivery van after {years} years.\n"
        f"*(Formula: A = P(1 - r)^n. Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the reducing-balance depreciation formula:\n"
        f"A = P(1 - r)^n, \\text{{ where }} P = 200\\,000, r = 0,15, n = 3. [1 mark]\n"
        f"Step 2: Substitute values:\n"
        f"A = 200\\,000(1 - 0,15)^3 = 200\\,000(0,85)^3 \\approx 200\\,000 \\times {factor:.6f} [1 mark]\n"
        f"Step 3: State the final depreciated value:\n"
        f"\\text{{Book value}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(initial_cost * (1.0 - 0.15 * years), 2)),  # Straight line
        _fmt_curr(round(future_val + 10000, 2)),
        _fmt_curr(round(future_val - 8000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_23",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate 200 000 × (0,85)^3.",
        f"Book value = 200 000 × (0,85)^3 = {_fmt_curr(future_val)}.",
        f"Value = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Graph interpretation: Identifying exponential curve 'increasing at an increasing rate'."""
    prompt = (
        "In Mathematical Literacy, how is the curvature and progression of an exponential growth graph described?\n"
    )
    correct = "Increasing at an increasing rate (getting steeper and steeper over time)"
    distractors = [
        "Increasing at a constant rate (forming a straight line with uniform slope)",
        "Increasing at a decreasing rate (flattening out towards a ceiling)",
        "Decreasing at an increasing rate (plummeting vertically)",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Recall the growth dynamics of exponential / compound functions: each increment is calculated on a larger base. [1 mark]\n"
        "Step 2: Note the graphical shape: the curve curves upwards, becoming steeper as time advances. [1 mark]\n"
        "Step 3: State the canonical curriculum phrase:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_24",
        prompt,
        correct,
        options,
        explanation,
        "Exponential growth gets steeper and steeper over time.",
        "It increases at an increasing rate.",
        f"Answer = {correct}.",
        r,
        difficulty="easy",
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Graph interpretation: Identifying exponential decay 'decreasing at a decreasing rate'."""
    prompt = (
        "When plotting reducing-balance depreciation or radioactive decay against time, "
        "how is the rate of change and curve behavior described?\n"
    )
    correct = "Decreasing at a decreasing rate (falling rapidly at first, then flattening out towards zero)"
    distractors = [
        "Decreasing at a constant rate (forming a straight downward line)",
        "Decreasing at an increasing rate (falling faster and faster)",
        "Constant throughout the life of the asset",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Analyse reducing-balance depreciation: the loss in value is largest in Year 1 and gets smaller each year. [1 mark]\n"
        "Step 2: Note the graphical curve: steep drop initially, then leveling out asymptotically. [1 mark]\n"
        "Step 3: State the curriculum description:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_25",
        prompt,
        correct,
        options,
        explanation,
        "Reducing balance loses the most value early on, then flattens out.",
        "It decreases at a decreasing rate.",
        f"Answer = {correct}.",
        r,
        difficulty="easy",
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Estimate doubling time for an investment under exponential growth from a graph."""
    principal = r.choice([5000, 10000, 15000, 20000])
    rate_pct = r.choice([6, 8, 10, 12])
    double_years = round(72 / rate_pct)
    double_amt = principal * 2
    ans_str = f"Approximately {double_years} years"

    prompt = (
        f"Refer to the compound interest curve shown in the diagram where an investment of R {_fmt(principal)},00 grows over time.\n"
        f"Reading from the curve, the balance reaches R {_fmt(double_amt)},00 (double the principal) at time t ≈ {double_years} years.\n"
        f"What is the estimated doubling time of this investment?"
    )
    explanation = (
        f"Step 1: Identify initial principal: P = R {_fmt(principal)},00. [1 mark]\n"
        f"Step 2: Locate double the principal on the vertical axis (A = R {_fmt(double_amt)},00) and read across to the curve and down to time t. [1 mark]\n"
        f"Step 3: State the doubling time:\n"
        f"\\text{{Doubling time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Approximately {max(3, double_years - 4)} years",
        f"Approximately {double_years + 4} years",
        f"Approximately {double_years + 8} years",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    d_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Exponential Growth Curve (Principal R {_fmt(principal)})",
        "lines": [{"name": "Growth Curve", "points": [{"x": 0, "y": principal}, {"x": double_years, "y": double_amt}, {"x": 2 * double_years, "y": 2 * double_amt}]}],
    }
    return _build_question_payload(
        "subskill_26",
        prompt,
        ans_str,
        options,
        explanation,
        "Find where the balance reaches R 20 000 on the vertical axis and read the time.",
        "At R 20 000, t ≈ 9 years.",
        f"Doubling time = {ans_str}.",
        r,
        difficulty="easy",
        diagram_spec=d_spec,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Evaluating whether a real-world trend represents linear, exponential, or inverse proportion."""
    trends = [
        (
            "A monthly municipal electricity bill on a postpaid system with a fixed network charge plus a flat rate per kWh used.",
            "Linear with positive intercept"
        ),
        (
            "The price of bread compounding at an annual inflation rate of 6% each year over a decade.",
            "Exponential / Constant ratio growth"
        ),
        (
            "The time taken to travel a 200 km journey as driving speed increases.",
            "Inverse proportion"
        ),
    ]
    scen_text, correct_type = r.choice(trends)
    ans_str = correct_type

    prompt = (
        f"Classify the following real-world scenario into its correct mathematical relationship model:\n"
        f"\"{scen_text}\""
    )
    explanation = (
        f"Step 1: Identify how the dependent variable changes with the independent variable. [1 mark]\n"
        f"Step 2: Reason about constant difference vs constant ratio vs constant product. [1 mark]\n"
        f"Step 3: State the matching relationship model:\n"
        f"\\text{{Classification}} = {ans_str}. [1 mark]"
    )
    distractors = [
        t for _, t in trends if t != correct_type
    ] + ["Step function"]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors[:3])
    return _build_question_payload(
        "subskill_27",
        prompt,
        ans_str,
        options,
        explanation,
        "Consider whether changes are constant additions, percentage multipliers, or sharing a fixed amount.",
        f"The scenario represents {correct_type}.",
        f"Answer = {ans_str}.",
        r,
        difficulty="easy",
    )
