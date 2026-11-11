"""Subskills 41 to 46: Bivariate data, scatter plots, trend lines, correlation, and causality."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_41_interpreting_bivariate_points(r: random.Random) -> Dict[str, Any]:
    """Interpret coordinates (x, y) on a scatter plot in a real South African context."""
    hours = r.choice([12, 15, 18, 20])
    mark = r.choice([68, 72, 75, 80])

    d_spec_41 = {
        "diagram_role": "context",
        "kind": "scatter_plot",
        "title": "Study Hours vs Final Mark (%)",
        "x_label": "Weekly Study Hours",
        "y_label": "Final Mark (%)",
        "points": [[hours, mark], [hours - 4, mark - 10], [hours + 3, min(100, mark + 8)]],
    }

    correct_ans = f"A learner who dedicated {hours} hours of study achieved an examination mark of {mark}%"
    custom_options = [
        correct_ans,
        f"A learner who dedicated {mark} hours of study achieved an examination mark of {hours}%",
        f"The class average was {hours} hours and the overall passing mark was {mark}%",
        f"Studying for {hours} hours guarantees an increase of {mark}% in all subjects",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the scatter plot relating weekly study hours to final examination marks (%).\n"
        f"One specific point plotted on the graph has coordinates ({hours}; {mark}).\n\n"
        f"Interpret what this point represents in the context of the study."
    )
    explanation = (
        f"Step 1: The x-coordinate represents the independent variable: study hours = {hours} hours [M].\n"
        f"Step 2: The y-coordinate represents the dependent variable: exam mark = {mark}% [M].\n"
        f"Step 3: Conclusion: A learner who studied for {hours} hours achieved {mark}% [A]."
    )
    return _build_question_payload(
        subskill_id="41_interpreting_bivariate_points",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Identify which variable is plotted on the horizontal x-axis and which is on the vertical y-axis.",
        tier_2=f"The first value ({hours}) is study hours; the second value ({mark}) is the test mark.",
        tier_3=f"It represents a learner who studied {hours} hours and achieved {mark}%.",
        r=r,
        diagram_spec=d_spec_41,
    )


def generate_42_identifying_correlation_direction(r: random.Random) -> Dict[str, Any]:
    """Identify positive, negative, or zero correlation from bivariate contexts."""
    contexts = [
        (
            "Vehicle age (in years) versus resale market value (in Rands)",
            "Negative correlation: As the vehicle age increases, the resale value decreases"
        ),
        (
            "Hours spent studying past exam papers versus final examination score",
            "Positive correlation: As study hours increase, the examination score generally increases"
        ),
        (
            "Learner shoe size versus score in a Mathematical Literacy trial exam",
            "Zero (no) correlation: Shoe size has no statistical relationship with mathematical performance"
        ),
        (
            "Outside ambient temperature (°C) versus sales of hot soup in a school tuckshop",
            "Negative correlation: As temperature rises, soup sales decrease"
        ),
    ]
    scenario, correct_ans = r.choice(contexts)

    custom_options = [
        correct_ans,
        "Perfect non-linear inverse quadratic correlation",
        "Deterministic correlation with zero variance",
        "Spurious inverse correlation with zero sample significance",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Consider the relationship between the following two variables:\n"
        f"• {scenario}\n\n"
        f"Identify the direction of correlation (positive, negative, or zero) and justify your answer."
    )
    explanation = (
        f"Step 1: Analyze how changes in the first variable affect the second variable [M].\n"
        f"Step 2: If both increase together, it is positive; if one increases as the other decreases, it is negative [M].\n"
        f"Step 3: {correct_ans} [A]."
    )
    return _build_question_payload(
        subskill_id="42_identifying_correlation_direction",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider whether the second variable goes up, down, or stays unrelated when the first variable increases.",
        tier_2="Check the real-world connection between the two variables.",
        tier_3=f"The correct classification is: {correct_ans}.",
        r=r,
    )


def generate_43_identifying_correlation_strength(r: random.Random) -> Dict[str, Any]:
    """Evaluate how closely data points cluster around a linear trend line."""
    correct_ans = "Strong positive correlation: The points lie very close to an upward-sloping trend line with minimal dispersion"

    custom_options = [
        correct_ans,
        "Weak positive correlation: The points are widely scattered all over the entire grid",
        "Strong negative correlation: As x increases, y drops rapidly toward zero",
        "Zero correlation: The trend line is perfectly horizontal",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"On a scatter plot comparing test revision hours with exam scores, the points slope upwards from left to right "
        f"and cluster tightly along a straight trend line, with very few outliers.\n\n"
        f"Describe both the strength and direction of this correlation."
    )
    explanation = (
        f"Step 1: Upward slope indicates a positive correlation [M].\n"
        f"Step 2: Tight clustering along the line indicates strong correlation [M].\n"
        f"Step 3: It is classified as a strong positive correlation [A]."
    )
    return _build_question_payload(
        subskill_id="43_identifying_correlation_strength",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="An upward slope means positive; tight clustering around the line means strong.",
        tier_2="Points that stay close to the line indicate strong correlation.",
        tier_3="Strong positive correlation.",
        r=r,
    )


def generate_44_estimating_from_line_of_best_fit(r: random.Random) -> Dict[str, Any]:
    """Estimate a value using a drawn line of best fit (trend line)."""
    slope = r.choice([2.5, 3.0, 3.5])
    intercept = r.choice([20, 25, 30])
    x_hours = r.choice([10, 12, 14, 16])
    expected_y = int(round(slope * x_hours + intercept))

    d_spec_44 = {
        "diagram_role": "context",
        "kind": "scatter_plot",
        "title": "Revision Hours vs Exam Mark Trend Line",
        "x_label": "Revision Hours",
        "y_label": "Mark (%)",
        "points": [
            [x_hours, expected_y],
            [x_hours - 4, int(slope * (x_hours - 4) + intercept)],
            [x_hours + 4, int(slope * (x_hours + 4) + intercept)],
        ],
    }

    correct_ans = f"Approximately {expected_y}% (between {expected_y - 2}% and {expected_y + 2}%)"
    custom_options = [
        f"Approximately {expected_y}% (between {expected_y - 2}% and {expected_y + 2}%)",
        f"Approximately {expected_y + 12}% (between {expected_y + 10}% and {expected_y + 14}%)",
        f"Approximately {expected_y - 15}% (between {expected_y - 17}% and {expected_y - 13}%)",
        f"Exactly 100% (the maximum ceiling of the graph)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the scatter plot trend line with the equation:\n"
        f"Mark (%) = ({_fmt(slope, 1)} × Revision Hours) + {intercept}%\n\n"
        f"Using this trend line, estimate the examination mark for a learner who completed {x_hours} revision hours."
    )
    explanation = (
        f"Step 1: Substitute {x_hours} hours into the trend line equation [M].\n"
        f"Step 2: Calculate ({_fmt(slope, 1)} × {x_hours}) + {intercept} = {_fmt(slope * x_hours, 1)} + {intercept} = {expected_y}% [M].\n"
        f"Step 3: Estimated mark = approximately {expected_y}% [A]."
    )
    return _build_question_payload(
        subskill_id="44_estimating_from_line_of_best_fit",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Substitute the given hours into the line of best fit formula.",
        tier_2=f"Calculate ({_fmt(slope, 1)} × {x_hours}) + {intercept}%.",
        tier_3=f"The expected mark is approximately {expected_y}%.",
        r=r,
        diagram_spec=d_spec_44,
    )


def generate_45_interpolation_vs_extrapolation(r: random.Random) -> Dict[str, Any]:
    """Distinguish between interpolation (within known range) and extrapolation (beyond known range)."""
    min_x = 5
    max_x = 25
    x_outside = 45

    correct_ans = f"Extrapolation: Estimating at {x_outside} hours lies far beyond the observed data range ({min_x} to {max_x} hours) and is highly unreliable"
    custom_options = [
        correct_ans,
        f"Interpolation: Estimating at {x_outside} hours is reliable because the trend line continues indefinitely to infinity",
        f"Interpolation: Any prediction made using a mathematical formula is statistically guaranteed",
        f"Extrapolation: The prediction is valid only if all learners study for exactly {x_outside} hours",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A scatter plot of learner revision hours records data between {min_x} hours and {max_x} hours.\n"
        f"A researcher uses the trend line to predict the exam mark for a learner who studies {x_outside} hours.\n\n"
        f"State whether this prediction is an interpolation or an extrapolation, and evaluate its statistical reliability."
    )
    explanation = (
        f"Step 1: The value {x_outside} hours lies outside the domain of observed data ({min_x} to {max_x}) [M].\n"
        f"Step 2: Predicting beyond observed data boundaries is extrapolation [M].\n"
        f"Step 3: Extrapolation is unreliable because the linear trend may not hold (e.g. fatigue, diminishing returns) [A]."
    )
    return _build_question_payload(
        subskill_id="45_interpolation_vs_extrapolation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check whether {x_outside} is inside or outside the range {min_x} to {max_x}.",
        tier_2="Predictions beyond the observed range are extrapolations.",
        tier_3="Extrapolation is risky and statistically unreliable.",
        r=r,
    )


def generate_46_correlation_vs_causation_fallacy(r: random.Random) -> Dict[str, Any]:
    """Identify the correlation versus causation fallacy."""
    correct_ans = "Correlation does not imply causation: A third lurking variable (hot weather) causes both ice cream sales and swimming drownings"

    custom_options = [
        correct_ans,
        "Direct causation: Eating ice cream impairs swimming reflexes and directly causes drowning",
        "Spurious measurement error: The statistics for both variables were recorded incorrectly",
        "Inverse causation: Drownings motivate grieving citizens to consume comfort ice cream",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A municipal health report discovers a very strong positive correlation (r = 0,92) between the number of "
        f"ice creams sold at Durban beachfront kiosks and the number of drowning incidents reported each week.\n"
        f"A journalist concludes: 'Eating ice cream causes drowning and should be banned at the beach.'\n\n"
        f"Critique this conclusion using principles of statistical causation."
    )
    explanation = (
        f"Step 1: Strong statistical correlation indicates an association, not a direct cause-and-effect relationship [M].\n"
        f"Step 2: Hot sunny weather (lurking variable) increases both ice cream consumption and beach swimming attendance [M].\n"
        f"Step 3: The journalist committed the correlation vs causation fallacy [A]."
    )
    return _build_question_payload(
        subskill_id="46_correlation_vs_causation_fallacy",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember the golden rule: Correlation does not prove causation.",
        tier_2="Think about what common factor increases both ice cream sales and swimming at the beach.",
        tier_3="Hot weather causes both; ice cream does not cause drownings.",
        r=r,
    )
