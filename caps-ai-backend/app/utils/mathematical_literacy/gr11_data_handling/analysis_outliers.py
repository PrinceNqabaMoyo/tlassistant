"""Subskills 45 to 52: Outlier Detection, Misleading Graphs, Correlation vs Causation & Critical Analysis for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Mathematical outlier detection rule: Q1 - 1.5*IQR or Q3 + 1.5*IQR."""
    q1 = r.choice([40, 45, 50])
    iqr = r.choice([20, 25])
    q3 = q1 + iqr

    upper_fence = q3 + 1.5 * iqr
    lower_fence = max(0, q1 - 1.5 * iqr)

    # Pick test score: either an outlier or not
    is_outlier = r.choice([True, False])
    if is_outlier:
        test_val = int(upper_fence + r.choice([5, 10, 15]))
        conclusion = f"Yes, {test_val} is an outlier because it exceeds the upper fence Q₃ + 1,5(IQR) = {_fmt(upper_fence)}"
    else:
        test_val = int(upper_fence - r.choice([5, 8, 10]))
        conclusion = f"No, {test_val} is not an outlier because it is less than the upper fence Q₃ + 1,5(IQR) = {_fmt(upper_fence)}"

    prompt = (
        f"In a statistical data set with Lower Quartile Q₁ = {_fmt(q1)} and Upper Quartile Q₃ = {_fmt(q3)} "
        f"(IQR = {_fmt(iqr)}), a researcher identifies a high observation of {_fmt(test_val)}.\n"
        f"Using the standard statistical outlier rule (Outlier > Q₃ + 1,5 × IQR), is the value {_fmt(test_val)} "
        f"classified as an outlier?"
    )

    correct_ans = conclusion
    other = f"No, {test_val} is not an outlier because it is less than the upper fence Q₃ + 1,5(IQR) = {_fmt(upper_fence)}" if is_outlier else f"Yes, {test_val} is an outlier because it exceeds the upper fence Q₃ + 1,5(IQR) = {_fmt(upper_fence)}"
    wrong_1 = other
    wrong_2 = f"Yes, any value above {_fmt(q3)} is automatically an outlier"
    wrong_3 = f"No, outliers only exist when data values are negative"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the upper outlier boundary (fence) [1 mark].\n"
        f"Upper Fence = Q₃ + 1,5 × IQR = {_fmt(q3)} + (1,5 × {_fmt(iqr)}) = {_fmt(q3)} + {_fmt(1.5 * iqr)} = {_fmt(upper_fence)}.\n"
        f"Step 2: Compare candidate observation {_fmt(test_val)} to upper fence [1 mark].\n"
        f"Since {_fmt(test_val)} is {'>' if is_outlier else '<'} {_fmt(upper_fence)}, {conclusion.lower()}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="45",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the upper boundary: Q₃ + (1,5 × IQR). Any value greater than this is an outlier.",
        tier_2=f"Upper fence = {_fmt(q3)} + 1,5({iqr}) = {_fmt(upper_fence)}.",
        tier_3=f"Compare {test_val} with {_fmt(upper_fence)}: {conclusion}.",
        r=r,
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Impact of an extreme outlier on Mean vs Median."""
    name = r.choice(SA_NAMES)
    normal_scores = [50, 52, 54, 56, 58]
    outlier = 120

    sum_without = sum(normal_scores)
    mean_without = round(sum_without / len(normal_scores), 1)  # 54.0
    med_without = 54

    all_scores = normal_scores + [outlier]
    sum_with = sum(all_scores)
    mean_with = round(sum_with / len(all_scores), 1)  # 390 / 6 = 65.0
    # sorted all_scores: 50, 52, 54, 56, 58, 120 -> median is (54 + 56)/2 = 55.0
    med_with = 55.0

    mean_diff = round(mean_with - mean_without, 1)

    prompt = (
        f"A small class has 5 test scores: 50%, 52%, 54%, 56%, 58% (Mean = 54,0%, Median = 54%). "
        f"A 6th student who transfers into the class with bonus marks scores an extreme 120%.\n"
        f"With the 120% outlier added, the new Mean is 65,0% and the new Median is 55,0%.\n"
        f"Which statistical principle about outliers and measures of central tendency does this demonstrate?"
    )

    correct_ans = (
        "The mean is highly sensitive to extreme outliers (increasing by 11,0 percentage points), whereas the median is resistant and changed by only 1,0 percentage point"
    )
    wrong_1 = "The median is heavily distorted by extreme outliers, while the mean remains completely unaffected"
    wrong_2 = "Both the mean and median change by the exact same amount whenever any outlier is added"
    wrong_3 = "Outliers automatically cause both the mean and median to become negative numbers"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Observe change in mean [1 mark].\n"
        f"Mean increased from 54,0% to 65,0% (a large jump of 11,0%).\n"
        f"Step 2: Observe change in median [1 mark].\n"
        f"Median only shifted from 54% to 55,0% (a minor shift of 1,0%).\n"
        f"Step 3: Stated principle [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="46",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The mean takes every number into account so an extreme value pulls it up. The median only looks at order, so it changes very little.",
        tier_2="Mean shifted by 11,0% while median only shifted by 1,0%.",
        tier_3=f"Conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Misleading graphs: truncated vertical axis."""
    prompt = (
        f"An advert in a South African newspaper shows a bar chart comparing customer satisfaction for Company A (92%) "
        f"and Company B (95%). On the chart, the vertical axis starts at 90% rather than 0%.\n"
        f"Why is this graph considered MISLEADING?"
    )

    correct_ans = (
        "Truncating the vertical axis at 90% makes Company B's bar appear more than twice as tall as Company A's, visually exaggerating a tiny 3% difference"
    )
    wrong_1 = "Company A should never be compared with Company B under competition law"
    wrong_2 = "Bar charts cannot display percentages above 50%"
    wrong_3 = "The graph is not misleading because 95% is mathematically more than 10 times larger than 92%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the baseline of the vertical axis [1 mark].\n"
        f"The y-axis begins at 90% instead of 0% (truncated baseline).\n"
        f"Step 2: Analyze the visual distortion created [1 mark].\n"
        f"Company A's bar has height 92 - 90 = 2 units, while Company B's bar has height 95 - 90 = 5 units (appears 2,5 times larger for a mere 3% actual difference).\n"
        f"Step 3: Conclude misleading effect [1 mark]: {correct_ans}."
    )

    sat_a = r.choice([91, 92, 93])
    sat_b = sat_a + r.choice([2, 3, 4])
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Customer Satisfaction Comparison ({sat_a}% vs {sat_b}%)",
        "categories": ["Company A", "Company B"],
        "values": [sat_a, sat_b],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="47",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When a bar chart does not start at zero, the ratio of the visual bar heights is distorted.",
        tier_2="Starting at 90% makes a 3% difference look huge.",
        tier_3=f"Misleading effect: {correct_ans}.",
        r=r,
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Misleading graphs: uneven / irregular interval spacing."""
    prompt = (
        f"A company publishes a line graph showing profit growth over five years. "
        f"The horizontal axis labels are spaced at equal distances apart, but the dates are: "
        f"2018, 2019, 2020, 2023, 2024 (skipping 2021 and 2022 without any gap).\n"
        f"How does this uneven timeline mislead the reader?"
    )

    correct_ans = (
        "It hides a multi-year gap and makes the gradual change over 3 years appear as a steep, rapid one-year surge"
    )
    wrong_1 = "Line graphs are illegal for displaying business profits"
    wrong_2 = "Years should always be ordered in descending order from newest to oldest"
    wrong_3 = "It has no misleading effect because readers only look at the dots, not the axis"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Inspect horizontal axis intervals [1 mark].\n"
        f"The spacing between 2020 and 2023 is 3 years, but drawn the same size as 1-year intervals.\n"
        f"Step 2: Analyze gradient distortion [1 mark].\n"
        f"Compressing 3 years into the width of 1 year artificially steepens the slope of the line.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="48",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Equal physical spacing on an axis must represent equal time intervals.",
        tier_2="Skipping 2 years without showing a wider gap makes change appear three times faster than it really was.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Misleading graphs: 3D perspective distortion in pie charts."""
    prompt = (
        f"In a corporate presentation, a 3D tilted pie chart is used to show market share. "
        f"Slice A represents 25% of the market and is placed in the foreground (tilted front), "
        f"while Slice B represents 30% and is placed in the background (tilted rear).\n"
        f"Why is this 3D perspective representation misleading?"
    )

    correct_ans = (
        "Perspective distortion causes the 25% foreground slice to look physically larger on screen than the 30% background slice"
    )
    wrong_1 = "3D pie charts always round all percentages down to zero"
    wrong_2 = "Slices in the foreground are legally required to represent at least 50% of the data"
    wrong_3 = "The total angle of a 3D circle becomes 720° instead of 360°"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand 3D projection effects in graphical design [1 mark].\n"
        f"Tilting a circle creates an ellipse where front elements are magnified by perspective foreshortening.\n"
        f"Step 2: Compare visual area to statistical proportion [1 mark].\n"
        f"The 25% slice in front appears wider and thicker, misleading the viewer into thinking it is larger than the 30% slice.\n"
        f"Step 3: Conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="49",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In 3D tilted charts, items in the foreground look bigger than items in the background.",
        tier_2="The 25% slice at the front appears larger than the 30% slice at the back due to 3D perspective.",
        tier_3=f"Misleading effect: {correct_ans}.",
        r=r,
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Correlation vs Causation distinction."""
    scenario = r.choice([
        (
            "Ice cream sales and drowning incidents at Durban beaches",
            "Both peak during hot summer months due to warmer weather (a confounding variable), but eating ice cream does not cause drowning"
        ),
        (
            "The number of storks nesting in European villages and the number of human babies born",
            "Larger rural villages have more houses/chimneys for storks and also more human families having children, with zero causal link between storks and childbirth"
        ),
        (
            "Cell phone ownership and life expectancy across different countries",
            "Both are driven by overall national economic development and healthcare infrastructure (wealthier nations have more phones and better hospitals)"
        ),
    ])
    pair, explanation_text = scenario

    prompt = (
        f"A statistical analysis reveals a strong positive correlation between: **{pair}**.\n"
        f"Does this correlation prove that the first variable CAUSES the second variable? Explain why or why not."
    )

    correct_ans = f"No: Correlation does not imply causation. {explanation_text}"
    wrong_1 = "Yes: A strong correlation statistically proves that the first variable directly causes the second"
    wrong_2 = "Yes: Whenever two variables increase together, one must be the direct cause of the other"
    wrong_3 = "No: Correlation only applies when both variables are measured in kilograms"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Differentiate correlation from causation [1 mark].\n"
        f"Correlation means two variables move together statistically; causation requires proving that changes in one directly produce changes in the other.\n"
        f"Step 2: Identify underlying third (confounding) factor [1 mark].\n"
        f"{explanation_text}.\n"
        f"Step 3: Conclude principle [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="50",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember the fundamental rule: Correlation does NOT equal causation.",
        tier_2=f"Check for an external third factor (confounding variable): {explanation_text}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Comparative decision making using mean and dispersion (consistency)."""
    name = r.choice(SA_NAMES)

    # Machine A: Mean = 500 g, Range = 4 g (very consistent)
    # Machine B: Mean = 500 g, Range = 24 g (erratic)
    prompt = (
        f"A quality controller at a maize meal packaging plant tests two bagging machines:\n"
        f"• Machine 1: Mean pack mass = 500,2 g; Range = 3,5 g; IQR = 1,8 g\n"
        f"• Machine 2: Mean pack mass = 500,1 g; Range = 22,0 g; IQR = 12,4 g\n"
        f"Both machines have an average pack mass very close to the 500 g target. "
        f"Which machine should the factory manager select for production, and why?"
    )

    correct_ans = (
        "Machine 1, because its substantially smaller range (3,5 g) and IQR (1,8 g) prove it is far more consistent and reliable"
    )
    wrong_1 = "Machine 2, because having a much larger range of 22,0 g gives customers exciting variety"
    wrong_2 = "Machine 2, because its mean is slightly closer to 500 g by 0,1 g, so range can be ignored"
    wrong_3 = "Neither machine, because packaging machines must produce zero variation with range of exactly 0,0 g"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Compare means [1 mark].\n"
        f"Both machines achieve essentially the exact same mean (approx 500 g).\n"
        f"Step 2: Compare dispersion / spread [1 mark].\n"
        f"Machine 1 has a range of only 3,5 g vs 22,0 g for Machine 2. A lower range and IQR indicate tight, consistent quality control.\n"
        f"Step 3: Stated decision [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="51",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When means are equal, the better machine is the one with smaller range and IQR (most consistent).",
        tier_2="Machine 1 has a much smaller range (3,5 g vs 22,0 g).",
        tier_3=f"Recommendation: {correct_ans}.",
        r=r,
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Comprehensive data evaluation synthesizing 5-number summary and skewness."""
    name = r.choice(SA_NAMES)
    min_v, q1_v, med_v, q3_v, max_v = 15, 45, 60, 68, 98

    # IQR = 68 - 45 = 23.
    # Left whisker = 45 - 15 = 30; Right whisker = 98 - 68 = 30.
    # Median is 60 (closer to 68 than 45? 68 - 60 = 8, 60 - 45 = 15 -> slightly negatively skewed).
    prompt = (
        f"A Five-Number Summary for a district-wide Mathematical Literacy benchmark exam is:\n"
        f"• Minimum: 15% | Q₁: 45% | Median: 60% | Q₃: 68% | Maximum: 98%\n"
        f"Based on this summary, what percentage of learners scored 68% or higher, and what is the Interquartile Range (IQR)?"
    )

    iqr = q3_v - q1_v
    correct_ans = f"25% of learners scored 68% or higher; IQR = {iqr}%"
    wrong_1 = f"75% of learners scored 68% or higher; IQR = {iqr}%"
    wrong_2 = f"25% of learners scored 68% or higher; IQR = {max_v - min_v}%"
    wrong_3 = f"50% of learners scored 68% or higher; IQR = {iqr}%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand quartiles and percentage boundaries [1 mark].\n"
        f"Q₃ represents the 75th percentile. Therefore, exactly 100% - 75% = 25% of the data lies at or above Q₃ (68%).\n"
        f"Step 2: Calculate IQR [1 mark].\n"
        f"IQR = Q₃ - Q₁ = 68% - 45% = {iqr}%.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="52",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The Upper Quartile Q₃ is at the 75% mark, so 25% of the values lie above Q₃.",
        tier_2=f"Q₃ = 68%, so 25% scored ≥ 68%. IQR = Q₃ - Q₁ = 68% - 45% = {iqr}%.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )
