"""Subskills 47 to 52: Section 3 CAPS: Opposing arguments, misleading graphs, and critical data evaluation."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_pct,
)


def generate_47_developing_opposing_arguments_tests(r: random.Random) -> Dict[str, Any]:
    """Develop two opposing valid viewpoints from the same exam results."""
    correct_ans = "Class 1 educator argues they had the top achievers (97% vs 81%); Class 2 educator argues their entire class passed (minimum 50% vs 28%)"

    custom_options = [
        correct_ans,
        "Class 1 is superior in every statistical metric including median, IQR, and pass rate",
        "Class 2 performed worse because having a smaller range proves lower effort",
        "Neither educator has a valid statistical argument because their medians are identical",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Two Grade 12 educators present the results of their respective classes:\n"
        f"• Class 1: Minimum = 28%, Median = 59%, Maximum = 97%, Range = 69%\n"
        f"• Class 2: Minimum = 50%, Median = 59%, Maximum = 81%, Range = 31%\n\n"
        f"Demonstrate how both educators can construct opposing, statistically valid arguments claiming their class performed better."
    )
    explanation = (
        f"Step 1: Class 1's educator can focus on elite achievement: their top learners reached 97% compared to 81% in Class 2 [M].\n"
        f"Step 2: Class 2's educator can focus on foundational consistency: zero failures, with lowest score 50% vs 28% in Class 1 [M].\n"
        f"Step 3: Both viewpoints are valid interpretations derived from different aspects of the same data [A]."
    )
    return _build_question_payload(
        subskill_id="47_developing_opposing_arguments_tests",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look for a metric where Class 1 excelled and a metric where Class 2 excelled.",
        tier_2="Class 1 has a much higher maximum (97%), while Class 2 has a much higher minimum (50%).",
        tier_3="Class 1 claims superior excellence; Class 2 claims total class consistency and zero failures.",
        r=r,
    )


def generate_48_misleading_graphs_truncated_axis(r: random.Random) -> Dict[str, Any]:
    """Explain how omitting zero on the vertical axis visually exaggerates minor differences."""
    val_a = r.choice([95, 96, 97])
    val_b = r.choice([98, 99, 100])
    y_start = 90

    d_spec_48 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Customer Satisfaction Comparison (Axis baseline {y_start}%)",
        "categories": ["Brand A", "Brand B"],
        "series": [
            {"name": "Satisfaction", "values": [val_a, val_b]}
        ],
        "y_min": y_start,
    }

    correct_ans = f"Starting the vertical axis at {y_start}% instead of 0% makes a tiny {val_b - val_a}% difference look massive (visually tripling the height)"

    custom_options = [
        correct_ans,
        f"Starting at {y_start}% is necessary because numbers below {y_start}% do not exist in matric results",
        f"The graph is accurate because the bars are colored with official departmental shades",
        f"Truncating the vertical axis reduces ink consumption without altering viewer perception",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the promotional bar graph comparing customer satisfaction: Brand A = {val_a}%, Brand B = {val_b}%.\n"
        f"The vertical axis begins at {y_start}% rather than 0%, making Brand B's bar appear three times taller than Brand A's bar.\n\n"
        f"Explain why this graph is statistically misleading."
    )
    explanation = (
        f"Step 1: The actual percentage difference is small: {val_b}% - {val_a}% = {val_b - val_a}% [M].\n"
        f"Step 2: By starting the axis at {y_start}%, the baseline of 0 is omitted (truncated axis) [M].\n"
        f"Step 3: This distorts visual proportion, exaggerating a tiny gap into an apparent landslide [A]."
    )
    return _build_question_payload(
        subskill_id="48_misleading_graphs_truncated_axis",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the axis does not start at zero.",
        tier_2=f"The actual difference between {val_a}% and {val_b}% is only {val_b - val_a}%, but the bar looks 300% taller.",
        tier_3="A truncated axis distorts proportions and visually misleads the viewer.",
        r=r,
        diagram_spec=d_spec_48,
    )


def generate_49_misleading_graphs_inconsistent_intervals(r: random.Random) -> Dict[str, Any]:
    """Identify distortion caused by non-uniform or inconsistent scale intervals."""
    start_year = r.choice([2016, 2017, 2018])
    gap_years = r.choice([3, 4, 5])
    end_year = start_year + 2 + gap_years
    v1 = r.choice([120, 130, 140])
    v2 = v1 - 5
    v3 = v2 - 5
    v4 = v3 - 20

    d_spec_49 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Municipal Water Consumption ({start_year} to {end_year})",
        "x_label": "Year",
        "y_label": "Consumption (ML)",
        "categories": [str(start_year), str(start_year + 1), str(start_year + 2), str(end_year)],
        "values": [v1, v2, v3, v4],
        "series": [
            {"name": "Consumption", "points": [[start_year, v1], [start_year + 1, v2], [start_year + 2, v3], [end_year, v4]]}
        ],
    }
    correct_ans = "Non-uniform intervals: The axis jumps from 10 to 20, then abruptly to 50 and 100, visually flattening or exaggerating trends"

    custom_options = [
        correct_ans,
        "Consistent scaling: Using logarithmic increments is standard for all Grade 12 classroom charts",
        "Zero distortion: As long as numbers increase from left to right, spacing is irrelevant",
        "Color distortion: Using dark blue bars distorts human depth perception",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the municipal graph tracking annual water consumption across years: {start_year}, {start_year+1}, {start_year+2}, and {end_year}.\n"
        f"Notice that the {gap_years}-year gap from {start_year+2} to {end_year} is drawn with the exact same spacing as a single-year gap.\n\n"
        f"Explain why this graph provides a distorted representation of water consumption trends."
    )
    explanation = (
        f"Step 1: Graph axes must maintain constant, uniform physical spacing for equal time increments [M].\n"
        f"Step 2: Representing a {gap_years}-year leap with the same spacing as a 1-year interval compresses time and artificially steepens the slope [M].\n"
        f"Step 3: This non-uniform scale creates a false impression of rapid change [A]."
    )
    return _build_question_payload(
        subskill_id="49_misleading_graphs_inconsistent_intervals",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check whether equal distances on the axis represent equal periods of time.",
        tier_2=f"A {gap_years}-year gap given the same width as a 1-year gap distorts the rate of change.",
        tier_3="Inconsistent axis scaling creates misleading visual slopes.",
        r=r,
        diagram_spec=d_spec_49,
    )


def generate_50_3d_pictogram_volume_distortion(r: random.Random) -> Dict[str, Any]:
    """Analyze how 3D effects and scaling 2D/3D pictograms distort perceived ratios."""
    correct_ans = "Area/Volume distortion: Doubling both height and width quadruples the 2D area (2² = 4), making a 2x increase appear as a 4x or 8x increase"

    custom_options = [
        correct_ans,
        "Perspective distortion: 3D cylinders cannot be printed on flat recycled paper",
        "Angle distortion: A 3D tilt makes the front value appear smaller than the rear value",
        "Legibility distortion: Shadows behind the cylinders prevent reading the tick marks",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An energy company publishes a pictogram showing that crude oil imports doubled (increased by 200%) over five years.\n"
        f"To illustrate this, they doubled both the height AND the diameter of the 3D oil barrel icon.\n\n"
        f"Explain why scaling both dimensions of a 3D graphic severely misleads the audience."
    )
    explanation = (
        f"Step 1: If linear dimensions are doubled (k = 2), area increases by k² = 4 and 3D volume increases by k³ = 8 [M].\n"
        f"Step 2: The audience perceives the physical bulk (volume) of the barrel, seeing an 8-fold increase rather than a 2-fold increase [M].\n"
        f"Step 3: This is classic area/volume graphic distortion [A]."
    )
    return _build_question_payload(
        subskill_id="50_3d_pictogram_volume_distortion",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how visual volume scales when height, width, and depth are all doubled.",
        tier_2="Volume scales by k³ = 2³ = 8.",
        tier_3="The viewer perceives an 8-fold increase instead of a doubling.",
        r=r,
    )


def generate_51_evaluating_opposing_viewpoints_census(r: random.Random) -> Dict[str, Any]:
    """Evaluate conflicting interpretations of census data between government and civic opposition."""
    correct_ans = "The government highlights the percentage increase in matric passes; the opposition highlights the absolute increase in unemployed youth"

    custom_options = [
        correct_ans,
        "The government uses the mean while the opposition is legally required to use the mode",
        "Both parties agree completely on all interpretations of the raw census data",
        "The opposition challenges the arithmetic because census data cannot be summed",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"According to Census data from Stats SA, the national pass percentage improved from 68% to 76%, "
        f"while total youth population growth meant that the absolute number of unemployed young people rose by 120 000.\n\n"
        f"Describe how both the government spokesperson and the civic opposition can cite these official statistics "
        f"to reach contradictory conclusions about education policy success."
    )
    explanation = (
        f"Step 1: Government focuses on the relative percentage improvement (68% to 76%) as proof of rising standards [M].\n"
        f"Step 2: Opposition focuses on the absolute headcount (+120 000 unemployed youths) as proof of system crisis [M].\n"
        f"Step 3: Both arguments use authentic census facts selectively to advance opposing political narratives [A]."
    )
    return _build_question_payload(
        subskill_id="51_evaluating_opposing_viewpoints_census",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at how one party can emphasize the percentage rate while the other emphasizes absolute numbers.",
        tier_2="Percentage pass improved, but the absolute number of unemployed youths also increased.",
        tier_3="Selective emphasis on rates versus absolute headcounts produces opposing valid claims.",
        r=r,
    )


def generate_52_cherry_picking_selective_reporting(r: random.Random) -> Dict[str, Any]:
    """Detect bias and cherry-picking in selective time window reporting."""
    correct_ans = "Cherry-picking: Selecting only a favorable 3-month window conceals the overall 5-year downward trend of the company"

    custom_options = [
        correct_ans,
        "Sampling error: A 3-month window is too small to calculate basic arithmetic percentages",
        "Observer bias: The accountant who prepared the quarterly report owns company shares",
        "Rounding error: Monthly profit numbers must always be rounded to the nearest thousand",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial investment company advertises: 'Our fund delivered a massive 18% return!'\n"
        f"Upon investigation, it is revealed that the fund gained 18% during a single specific 3-month quarter, "
        f"while over the full 5-year period the fund experienced an overall net loss of 4%.\n\n"
        f"Identify this deceptive statistical practice and explain why it is misleading to prospective investors."
    )
    explanation = (
        f"Step 1: The advertisement selectively isolates an unrepresentative peak period [M].\n"
        f"Step 2: Isolating favourable segments while omitting the overarching reality is known as cherry-picking [M].\n"
        f"Step 3: It misleads investors into expecting ongoing double-digit growth while hiding long-term capital loss [A]."
    )
    return _build_question_payload(
        subskill_id="52_cherry_picking_selective_reporting",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the advertisement focuses only on one positive short period while ignoring the 5-year trend.",
        tier_2="Selecting only data that supports your claim while suppressing contradictory data is called cherry-picking.",
        tier_3="Cherry-picking conceals the true long-term performance.",
        r=r,
    )
