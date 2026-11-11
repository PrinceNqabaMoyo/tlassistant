"""
Grade 7 Mathematics - Represent Data Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Represent data.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Pie Chart Interpretation & Quantities (26 - 34)
# ==============================================================================

def arch_26_read_simple_fraction_pie_chart(rng: random.Random) -> Dict[str, Any]:
    n_tot = rng.choice([80, 100, 120, 160, 200])
    sectors = [
        {"label": "Walking", "value": 50},
        {"label": "Bus", "value": 25},
        {"label": "Car", "value": 25}
    ]
    spec = {
        "kind": "pie_chart",
        "title": f"Travel to School (n = {n_tot} learners)",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the pie chart showing travel modes to school for {n_tot} learners.\n\n"
        f"1. What fraction of the circle is represented by **Walking** (50%) in simplest form?\n"
        f"2. What fraction is represented by **Bus** (25%)?"
    )
    sol = (
        f"**Step 1:** $50\\% = \\frac{{50}}{{100}} = \\mathbf{{\\frac{{1}}{{2}}}}$ of the circle [1 Mark: Method].\n\n"
        f"**Step 2:** $25\\% = \\frac{{25}}{{100}} = \\mathbf{{\\frac{{1}}{{4}}}}$ of the circle [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1/2; 1/4",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "26_read_simple_fraction_pie_chart",
        "hints": {
            "tier_1": "Convert each percentage into a simplified fraction out of 100.",
            "tier_2": "50/100 = 1/2 and 25/100 = 1/4.",
            "tier_3": "Walking is 1/2; Bus is 1/4."
        }
    }


def arch_27_calculate_quantity_from_sector_percentage(rng: random.Random) -> Dict[str, Any]:
    total_learners = rng.choice([200, 400, 600, 800])
    pct = rng.choice([20, 25, 30, 40, 50])
    quantity = int((pct / 100) * total_learners)

    sectors = [
        {"label": "Soccer", "value": pct},
        {"label": "Other Sports", "value": 100 - pct}
    ]
    spec = {
        "kind": "pie_chart",
        "title": f"Sports Choices (Total = {total_learners} learners)",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"In a school of {total_learners} learners, the pie chart shows that **{pct}%** chose Soccer.\n\n"
        f"Calculate the actual number of learners who chose Soccer."
    )
    sol = (
        f"**Step 1:** Write the percentage calculation: "
        f"$$\\text{{Quantity}} = \\frac{{{pct}}}{{100}} \\times {total_learners} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate: $$\\mathbf{{{quantity}}} \\text{{ learners}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{quantity}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "27_calculate_quantity_from_sector_percentage",
        "hints": {
            "tier_1": f"Multiply {pct}/100 by {total_learners}.",
            "tier_2": f"({pct} * {total_learners}) / 100.",
            "tier_3": f"{quantity} learners."
        }
    }


def arch_28_find_missing_sector_percentage(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([35, 40, 45])
    p2 = rng.choice([20, 25, 30])
    p3 = 100 - (p1 + p2)

    sectors = [
        {"label": "English", "value": p1},
        {"label": "isiZulu", "value": p2},
        {"label": "Afrikaans", "value": p3}
    ]
    spec = {
        "kind": "pie_chart",
        "title": "Language Survey Breakdown",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"A complete pie chart represents 100% of the data.\n\n"
        f"English represents **{p1}%** and isiZulu represents **{p2}%**.\n"
        f"Calculate the missing percentage for **Afrikaans**."
    )
    sol = (
        f"**Step 1:** The sum of all sectors in a pie chart is $100\\%$ [1 Mark: Method].\n\n"
        f"**Step 2:** Missing percentage: "
        f"$$100\\% - ({p1}\\% + {p2}\\%) = 100\\% - {p1 + p2}\\% = \\mathbf{{{p3}\\%}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{p3}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "28_find_missing_sector_percentage",
        "hints": {
            "tier_1": "Subtract the known percentages from 100%.",
            "tier_2": f"100 - ({p1} + {p2}).",
            "tier_3": f"{p3}%."
        }
    }


def arch_29_reverse_total_from_known_sector(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([10, 20, 25, 50])
    count = rng.choice([30, 45, 60, 80])
    total = int((count / pct) * 100)

    sectors = [
        {"label": "Recycling", "value": pct},
        {"label": "Other Projects", "value": 100 - pct}
    ]
    spec = {
        "kind": "pie_chart",
        "title": "Eco-Club Membership",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"In an eco-club survey, the pie chart indicates that **{pct}%** of members participate in Recycling.\n\n"
        f"If exactly **{count} members** do Recycling, calculate the **total number of members** in the eco-club."
    )
    sol = (
        f"**Step 1:** If ${pct}\\%$ corresponds to ${count}$, then $1\\% = \\frac{{{count}}}{{{pct}}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Total ($100\\%$): "
        f"$$\\text{{Total}} = \\frac{{{count}}}{{{pct}}} \\times 100 = \\mathbf{{{total}}} \\text{{ members [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "29_reverse_total_from_known_sector",
        "hints": {
            "tier_1": f"Divide {count} by {pct} to find 1%, then multiply by 100.",
            "tier_2": f"({count} * 100) / {pct}.",
            "tier_3": f"{total} members."
        }
    }


def arch_30_compare_two_sectors_on_pie_chart(rng: random.Random) -> Dict[str, Any]:
    c_pct = rng.choice([40, 45, 50])
    b_pct = 15
    d_pct = 90 - c_pct - b_pct
    diff = c_pct - b_pct
    sectors = [
        {"label": "Cats", "value": c_pct},
        {"label": "Dogs", "value": d_pct},
        {"label": "Birds", "value": b_pct},
        {"label": "Fish", "value": 10}
    ]
    spec = {
        "kind": "pie_chart",
        "title": "Pets Owned by Grade 7 Learners (%)",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the pie chart of pets owned.\n\n"
        f"How much larger is the percentage of learners owning **Cats ({c_pct}%)** compared to those owning **Birds ({b_pct}%)**?"
    )
    sol = (
        f"**Step 1:** Identify percentages: Cats = {c_pct}% and Birds = {b_pct}% [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract: $${c_pct}\\% - {b_pct}\\% = \\mathbf{{{diff}\\%}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "30_compare_two_sectors_on_pie_chart",
        "hints": {
            "tier_1": "Subtract the smaller sector percentage from the larger.",
            "tier_2": f"{c_pct} - {b_pct}.",
            "tier_3": f"{diff}%."
        }
    }


def arch_31_identify_largest_sector_mode(rng: random.Random) -> Dict[str, Any]:
    f_pct = rng.choice([44, 46, 48, 52])
    s_pct = 70 - f_pct
    sectors = [
        {"label": "Fiction", "value": f_pct},
        {"label": "Science", "value": s_pct},
        {"label": "History", "value": 18},
        {"label": "Biography", "value": 12}
    ]
    spec = {
        "kind": "pie_chart",
        "title": "Books Read by Category",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the pie chart of books read by category.\n\n"
        f"1. Which category has the largest slice (the mode)?\n"
        f"2. State its percentage."
    )
    sol = (
        f"**Step 1:** The largest sector is **Fiction** [1 Mark: Method].\n\n"
        f"**Step 2:** Its percentage is **{f_pct}%** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Fiction; {f_pct}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "31_identify_largest_sector_mode",
        "hints": {
            "tier_1": "Find the sector with the biggest angle/percentage.",
            "tier_2": f"Fiction is {f_pct}%.",
            "tier_3": f"Fiction with {f_pct}%."
        }
    }


def arch_32_simplest_fraction_for_sector(rng: random.Random) -> Dict[str, Any]:
    cases = [(20, "1/5", "20/100"), (10, "1/10", "10/100"), (75, "3/4", "75/100"), (12.5, "1/8", "12.5/100")]
    pct, frac, raw = rng.choice(cases)

    prompt = (
        f"A sector on a pie chart represents **{pct}%** of the total.\n\n"
        f"Write this percentage as a fraction in its **simplest form**."
    )
    sol = (
        f"**Step 1:** Express as fraction over 100: $\\frac{{{pct}}}{{100}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Simplify by dividing by the greatest common divisor: "
        f"$$\\mathbf{{{frac}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": frac,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_simplest_fraction_for_sector",
        "hints": {
            "tier_1": f"Write {pct}/100 and simplify.",
            "tier_2": f"Reduce to lowest terms.",
            "tier_3": f"{frac}."
        }
    }


def arch_33_budget_allocation_pie_chart(rng: random.Random) -> Dict[str, Any]:
    salary = rng.choice([12000, 16000, 20000])
    sectors = [
        {"label": "Rent", "value": 40},
        {"label": "Food", "value": 30},
        {"label": "Transport", "value": 20},
        {"label": "Savings", "value": 10}
    ]
    spec = {
        "kind": "pie_chart",
        "title": f"Monthly Budget (Salary = R{salary:,})",
        "sectors": sectors,
        "diagram_role": "context"
    }

    # Food is 30%
    food_amount = int(0.30 * salary)

    prompt = (
        f"The pie chart shows the monthly budget allocation for a household earning R{salary:,}.\n\n"
        f"Calculate the exact amount in Rands spent on **Food (30%)** each month."
    )
    sol = (
        f"**Step 1:** Write the budget formula: $$\\text{{Food}} = 30\\% \\times \\text{{R}}{salary:,} = \\frac{{30}}{{100}} \\times {salary} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate: $$\\mathbf{{\\text{{R}}{food_amount:,}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"R{food_amount}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "33_budget_allocation_pie_chart",
        "hints": {
            "tier_1": f"Find 30% of {salary}.",
            "tier_2": f"0.30 * {salary}.",
            "tier_3": f"R{food_amount}."
        }
    }


def arch_34_convert_percentage_to_degrees(rng: random.Random) -> Dict[str, Any]:
    cases = [(10, 36), (20, 72), (25, 90), (30, 108), (40, 144), (50, 180)]
    pct, deg = rng.choice(cases)

    prompt = (
        f"A full circle has $360^\\circ$.\n\n"
        f"Calculate the **sector angle in degrees** for a category representing **{pct}%** on a pie chart."
    )
    sol = (
        f"**Step 1:** Multiply the percentage by $360^\\circ$: "
        f"$$\\text{{Angle}} = \\frac{{{pct}}}{{100}} \\times 360^\\circ \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate: $$\\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_convert_percentage_to_degrees",
        "hints": {
            "tier_1": f"Multiply ({pct}/100) by 360.",
            "tier_2": f"{pct} * 3.6.",
            "tier_3": f"{deg}°."
        }
    }


# ==============================================================================
# CLUSTER 5: Angles & Pie Chart Construction (35 - 42)
# ==============================================================================

def arch_35_sector_angle_for_simple_fractions(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("one quarter (1/4)", 4, 90),
        ("one third (1/3)", 3, 120),
        ("one sixth (1/6)", 6, 60),
        ("one eighth (1/8)", 8, 45)
    ]
    name, div, deg = rng.choice(cases)

    prompt = (
        f"Calculate the sector angle in degrees for a slice that represents **{name}** of a circle."
    )
    sol = (
        f"**Step 1:** Divide $360^\\circ$ by the denominator: $$\\frac{{360^\\circ}}{{{div}}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$\\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_sector_angle_for_simple_fractions",
        "hints": {
            "tier_1": f"Divide 360° by {div}.",
            "tier_2": f"360 / {div} = {deg}.",
            "tier_3": f"{deg}°."
        }
    }


def arch_36_sector_angle_from_frequency_and_total(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([36, 60, 72, 120])
    freq = rng.choice([6, 12, 18, 24])
    deg = int((freq / total) * 360)

    prompt = (
        f"In a survey of **{total} learners**, **{freq} learners** chose blue as their favourite colour.\n\n"
        f"Calculate the size of the **sector angle** (in degrees) needed to represent blue on a pie chart."
    )
    sol = (
        f"**Step 1:** Angle formula: $$\\text{{Angle}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total}}}} \\times 360^\\circ = \\frac{{{freq}}}{{{total}}} \\times 360^\\circ \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Calculate: $$\\mathbf{{{deg}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{deg}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_sector_angle_from_frequency_and_total",
        "hints": {
            "tier_1": f"Multiply ({freq}/{total}) by 360°.",
            "tier_2": f"({freq} * 360) / {total}.",
            "tier_3": f"{deg}°."
        }
    }


def arch_37_remaining_sector_degrees(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([100, 110, 120])
    a2 = rng.choice([80, 90, 100])
    a3 = rng.choice([50, 60, 70])
    a4 = 360 - (a1 + a2 + a3)

    prompt = (
        f"A pie chart is divided into 4 sectors.\n\n"
        f"Three sectors have angles of **{a1}^\\circ**, **{a2}^\\circ**, and **{a3}^\\circ**.\n"
        f"Calculate the size of the fourth sector angle."
    )
    sol = (
        f"**Step 1:** The angles in a full circle add up to $360^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract known angles: "
        f"$$360^\\circ - ({a1}^\\circ + {a2}^\\circ + {a3}^\\circ) = 360^\\circ - {a1+a2+a3}^\\circ = \\mathbf{{{a4}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a4}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_remaining_sector_degrees",
        "hints": {
            "tier_1": "Angles around a central point always total 360°.",
            "tier_2": f"360 - ({a1} + {a2} + {a3}).",
            "tier_3": f"{a4}°."
        }
    }


def arch_38_verify_sector_angles_sum_to_360(rng: random.Random) -> Dict[str, Any]:
    valid = rng.choice([True, False])
    if valid:
        a1, a2, a3 = 120, 140, 100
        ans = "Yes, valid (sum is 360°)"
    else:
        a1, a2, a3 = 120, 140, 110  # sum = 370
        ans = "No, invalid (sum is 370°, which exceeds 360°)"

    prompt = (
        f"A learner draws a pie chart with three sectors measuring **{a1}^\\circ**, **{a2}^\\circ**, and **{a3}^\\circ**.\n\n"
        f"Determine whether this construction is mathematically correct, explaining your reasoning."
    )
    tot = a1 + a2 + a3
    sol = (
        f"**Step 1:** Sum the three angles: $${a1}^\\circ + {a2}^\\circ + {a3}^\\circ = {tot}^\\circ \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** {'Since the sum is exactly 360°, the construction is valid.' if valid else f'Since the sum is {tot}°, which does NOT equal 360°, the construction is invalid.'} [1 Mark: Accuracy]"
    )
    return {
        "id": f"g7_dat_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_verify_sector_angles_sum_to_360",
        "hints": {
            "tier_1": "Add the angles together and see if they equal exactly 360°.",
            "tier_2": f"Sum is {tot}°.",
            "tier_3": ans
        }
    }


def arch_39_frequency_from_known_angle(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([60, 90, 120, 180])
    total_survey = rng.choice([60, 120, 180, 240, 360])
    freq = int((angle / 360) * total_survey)

    prompt = (
        f"In a survey of **{total_survey} people**, a sector on a pie chart has a central angle of **{angle}^\\circ**.\n\n"
        f"How many people does this sector represent?"
    )
    sol = (
        f"**Step 1:** Fraction of circle: $$\\frac{{{angle}^\\circ}}{{360^\\circ}} = \\frac{{{angle // math_gcd(angle, 360)}}}{{{360 // math_gcd(angle, 360)}}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Multiply by total: $$\\frac{{{angle}}}{{360}} \\times {total_survey} = \\mathbf{{{freq}}} \\text{{ people}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{freq}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_frequency_from_known_angle",
        "hints": {
            "tier_1": f"Multiply ({angle}/360) by {total_survey}.",
            "tier_2": f"({angle} * {total_survey}) / 360.",
            "tier_3": f"{freq} people."
        }
    }


def math_gcd(a: int, b: int) -> int:
    import math
    return math.gcd(a, b)


def arch_40_match_frequency_table_to_pie_chart(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2, 3, 4])
    tot = 100 * mult
    s_val, n_val, c_val = 50 * mult, 25 * mult, 25 * mult
    spec = {
        "kind": "pie_chart",
        "title": f"Sports Survey (n = {tot})",
        "sectors": [
            {"label": "Soccer", "value": s_val},
            {"label": "Netball", "value": n_val},
            {"label": "Cricket", "value": c_val}
        ],
        "diagram_role": "context"
    }
    prompt = (
        f"A survey of {tot} learners showed: Soccer = {s_val}, Netball = {n_val}, Cricket = {c_val}.\n\n"
        f"Describe the appearance of the pie chart representing this data."
    )
    sol = (
        f"**Step 1:** Soccer represents $\\frac{{{s_val}}}{{{tot}}} = \\frac{{1}}{{2}}$ (a semi-circle or $180^\\circ$) [1 Mark: Method].\n\n"
        f"**Step 2:** Netball and Cricket each represent $\\frac{{{n_val}}}{{{tot}}} = \\frac{{1}}{{4}}$ (quarter circles or $90^\\circ$ each) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Half circle for Soccer (180°), quarter circle each for Netball and Cricket (90°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "40_match_frequency_table_to_pie_chart",
        "hints": {
            "tier_1": f"Calculate the fraction or angle for each sport out of {tot}.",
            "tier_2": "50% is half (180°); 25% is a quarter (90°).",
            "tier_3": "Soccer is half; Netball and Cricket are each a quarter."
        }
    }


def arch_41_compare_pie_charts_different_sample_sizes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"School A (1 000 learners) and School B (200 learners) both have pie charts where the 'Bicycle' sector is 25%.\n\n"
        f"1. Do both schools have the same **percentage** of cyclists?\n"
        f"2. Do both schools have the same **actual number** of cyclists? Justify with calculations."
    )
    sol = (
        f"**Step 1:** Yes, both have the same percentage: **25%** [1 Mark].\n\n"
        f"**Step 2:** No, the actual numbers differ because the sample sizes differ:\n"
        f"- School A: $25\\% \\times 1\\ 000 = \\mathbf{{250 \\text{{ cyclists}}}}$\n"
        f"- School B: $25\\% \\times 200 = \\mathbf{{50 \\text{{ cyclists}}}}$ [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Same percentage (25%), but School A has 250 cyclists while School B has 50 cyclists",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_compare_pie_charts_different_sample_sizes",
        "hints": {
            "tier_1": "Look at percentages first, then calculate 25% of 1000 and 25% of 200.",
            "tier_2": "Percentages are identical (25%), but 250 != 50.",
            "tier_3": "Same percentage (25%), but School A has 250 and School B has 50."
        }
    }


def arch_42_three_sector_preference_poll(rng: random.Random) -> Dict[str, Any]:
    a_pct = rng.choice([50, 60])
    d_pct = a_pct // 2
    u_pct = 100 - a_pct - d_pct
    sectors = [
        {"label": "Agree", "value": a_pct},
        {"label": "Disagree", "value": d_pct},
        {"label": "Unsure", "value": u_pct}
    ]
    spec = {
        "kind": "pie_chart",
        "title": "School Uniform Policy Poll",
        "sectors": sectors,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the pie chart of the school uniform policy poll.\n\n"
        f"What is the **ratio** in simplest form of learners who **Agree ({a_pct}%)** to learners who **Disagree ({d_pct}%)**?"
    )
    sol = (
        f"**Step 1:** Read percentages: Agree = {a_pct}%, Disagree = {d_pct}% [1 Mark: Method].\n\n"
        f"**Step 2:** Form ratio and simplify: "
        f"$${a_pct} : {d_pct} = \\mathbf{{2 : 1}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "2:1",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "42_three_sector_preference_poll",
        "hints": {
            "tier_1": f"Write {a_pct} : {d_pct} and simplify by dividing both numbers by {d_pct}.",
            "tier_2": f"{a_pct}/{d_pct} = 2 and {d_pct}/{d_pct} = 1.",
            "tier_3": "2:1."
        }
    }


# ==============================================================================
# CLUSTER 6: Data Representation Critique & Graph Selection (43 - 50)
# ==============================================================================

def arch_43_choose_graph_for_discrete_categories(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A researcher collects data on learners' favourite colours (Red, Blue, Green, Yellow).\n\n"
        f"Which type of graph is best suited to display this discrete categorical data: a **bar graph** or a **histogram**? Explain why."
    )
    sol = (
        f"**Step 1:** Best representation is a **bar graph** [1 Mark].\n\n"
        f"**Step 2:** Favourite colours are discrete categories (non-numeric, distinct groups with spaces between them), not continuous grouped numeric measurements [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bar graph; colours are discrete separate categories with spaces between them",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_choose_graph_for_discrete_categories",
        "hints": {
            "tier_1": "Are colours numbers with intervals, or separate distinct categories?",
            "tier_2": "Distinct separate categories use a bar graph with spaces.",
            "tier_3": "Bar graph."
        }
    }


def arch_44_choose_graph_for_continuous_data(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A medical clinic measures the heights of Grade 7 learners in centimetres, grouped into intervals of 5 cm (e.g. 140 - 144 cm, 145 - 149 cm).\n\n"
        f"Which type of graph is most appropriate: a **bar graph** or a **histogram**? Explain why."
    )
    sol = (
        f"**Step 1:** The most appropriate graph is a **histogram** [1 Mark].\n\n"
        f"**Step 2:** Height is continuous measurement data organised into continuous numerical intervals where bars must touch without gaps [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Histogram; height is continuous data grouped into numerical intervals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_choose_graph_for_continuous_data",
        "hints": {
            "tier_1": "Continuous measurements grouped into intervals use touching bars.",
            "tier_2": "Touching bars form a histogram.",
            "tier_3": "Histogram."
        }
    }


def arch_45_choose_graph_for_proportions_of_whole(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"You wish to show how the monthly allowance of R500 is split across four expenses, emphasizing how each part contributes to the whole 100% budget.\n\n"
        f"Which graph is the most suitable visual representation?"
    )
    sol = (
        f"**Step 1:** The most suitable representation is a **pie chart** (or circle graph) [1 Mark].\n\n"
        f"**Step 2:** A pie chart is specifically designed to display proportions or percentages that add up to a complete whole (100%) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Pie chart; it illustrates proportions of a whole (100%)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_choose_graph_for_proportions_of_whole",
        "hints": {
            "tier_1": "What circular chart shows parts of a whole 100%?",
            "tier_2": "A pie chart.",
            "tier_3": "Pie chart."
        }
    }


def arch_46_choose_graph_for_trends_over_time(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A weather station records the daily maximum temperature in Durban at 14:00 every day for 14 consecutive days.\n\n"
        f"Which graph is best suited to illustrate how the temperature changes and trends over this two-week time period?"
    )
    sol = (
        f"**Step 1:** The best representation is a **broken line graph** (or line graph) [1 Mark].\n\n"
        f"**Step 2:** Line graphs connect consecutive points to show rate of change and continuous trends over time [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Broken line graph; it displays continuous trends and changes over time",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_choose_graph_for_trends_over_time",
        "hints": {
            "tier_1": "Connecting points with line segments shows trends over time.",
            "tier_2": "A line graph.",
            "tier_3": "Broken line graph."
        }
    }


def arch_47_misleading_graph_truncated_vertical_axis(rng: random.Random) -> Dict[str, Any]:
    va = rng.randint(91, 94)
    vb = rng.randint(97, 99)
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<line x1="60" y1="20" x2="60" y2="160" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="60" y1="160" x2="360" y2="160" stroke="#1e293b" stroke-width="2"/>'
            f'<text x="50" y="160" font-size="12" text-anchor="end" fill="#dc2626" font-weight="bold">90</text>'
            f'<text x="50" y="90" font-size="12" text-anchor="end" fill="#1e293b">95</text>'
            f'<text x="50" y="30" font-size="12" text-anchor="end" fill="#1e293b">100</text>'
            f'<rect x="100" y="130" width="50" height="30" fill="#3b82f6"/>'
            f'<rect x="220" y="40" width="50" height="120" fill="#ef4444"/>'
            f'<text x="125" y="180" font-size="12" text-anchor="middle" fill="#0f172a">Brand A ({va})</text>'
            f'<text x="245" y="180" font-size="12" text-anchor="middle" fill="#0f172a">Brand B ({vb})</text>'
            f'</svg>'
        ),
        "caption": "Bar graph with vertical axis starting at 90 instead of 0",
        "diagram_role": "context"
    }

    prompt = (
        f"Look at the bar graph comparing Brand A ({va} sales) and Brand B ({vb} sales).\n\n"
        f"Why is this visual representation misleading to a consumer?"
    )
    sol = (
        f"**Step 1:** The vertical axis does not start at **zero**; it starts at **90** [1 Mark].\n\n"
        f"**Step 2:** Because the axis is truncated, Brand B's bar appears four times taller than Brand A's bar, even though the actual sales difference is only {vb - va} units ({vb} vs {va}) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Vertical axis starts at 90 instead of 0, exaggerating the difference between Brand A and Brand B",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "47_misleading_graph_truncated_vertical_axis",
        "hints": {
            "tier_1": "Look at the bottom number on the vertical axis.",
            "tier_2": "The scale starts at 90 instead of 0.",
            "tier_3": "The axis starts at 90 instead of 0, making the difference look much larger than it really is."
        }
    }


def arch_48_misleading_graph_unequal_bar_widths(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A newspaper prints a bar graph where the bar for Company B is drawn twice as wide as the bar for Company A, even though both represent the same category width.\n\n"
        f"Explain why drawing bars of unequal widths creates a misleading impression."
    )
    sol = (
        f"**Step 1:** In a standard bar graph, frequency is represented solely by the **height** of the bar, and all bars must have identical widths [1 Mark].\n\n"
        f"**Step 2:** A wider bar has a much larger area, which visually deceives the viewer into thinking Company B has far more influence or quantity than it actually does [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Unequal bar widths distort the area of the bar, giving a false visual impression",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_misleading_graph_unequal_bar_widths",
        "hints": {
            "tier_1": "Should bars in a bar graph have equal widths?",
            "tier_2": "A wider bar takes up more visual space/area.",
            "tier_3": "Unequal widths distort the area, misleading the viewer."
        }
    }


def arch_49_misleading_3d_perspective_distortion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Why do mathematics educators and statisticians advise against using tilted 3D perspective pie charts in presentations?"
    )
    sol = (
        f"**Step 1:** 3D tilting alters the visual perspective: slices in the foreground (front) appear larger and wider than slices in the background (back) [1 Mark].\n\n"
        f"**Step 2:** This distorts the angles and proportions, making smaller percentages in front look larger than bigger percentages at the back [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_dat_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "3D perspective distorts proportions; front slices look artificially larger than back slices",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_misleading_3d_perspective_distortion",
        "hints": {
            "tier_1": "What happens to objects drawn in the front of a 3D drawing compared to the back?",
            "tier_2": "Front slices look bigger than they actually are.",
            "tier_3": "3D tilting distorts the proportions, making front slices look artificially larger."
        }
    }


def arch_50_tabular_summary_to_bar_graph_conversion(rng: random.Random) -> Dict[str, Any]:
    categories = ["Red", "Blue", "Green", "Yellow"]
    step = rng.choice([5, 6, 7, 8, 9])
    counts = [2 * step, 4 * step, 3 * step, step]

    spec = {
        "kind": "bar_graph",
        "title": "T-Shirt Colours Ordered",
        "x_label": "Colour",
        "y_label": "Orders",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"A class orders house T-shirts:\n\n"
        f"| Colour | Red | Blue | Green | Yellow |\n"
        f"| :---: | :---: | :---: | :---: | :---: |\n"
        f"| Orders | {counts[0]} | {counts[1]} | {counts[2]} | {counts[3]} |\n\n"
        f"If you construct a bar graph for this data with a vertical scale marked in increments of {step}:\n"
        f"1. How many scale grid units high will the **Blue** bar be?\n"
        f"2. How many scale grid units high will the **Green** bar be?"
    )
    sol = (
        f"**Step 1:** Blue bar has {counts[1]} orders: $$\\frac{{{counts[1]}}}{{{step}}} = \\mathbf{{4 \\text{{ scale units}}}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Green bar has {counts[2]} orders: $$\\frac{{{counts[2]}}}{{{step}}} = \\mathbf{{3 \\text{{ scale units}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Blue: 4 units; Green: 3 units",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "50_tabular_summary_to_bar_graph_conversion",
        "hints": {
            "tier_1": f"Divide each count by the scale increment ({step}).",
            "tier_2": f"{counts[1]} / {step} = 4; {counts[2]} / {step} = 3.",
            "tier_3": "Blue is 4 units; Green is 3 units."
        }
    }
