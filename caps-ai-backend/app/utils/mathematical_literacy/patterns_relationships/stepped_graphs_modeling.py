"""Cluster 6: Advanced Representations, Step Graphs & Modeling (Subskills 45 to 52)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)

# --------------------------------------------------------------------------- #
# Subskill 45: Convert Formula to Table Entry
# --------------------------------------------------------------------------- #
def _gen_pat_rep_convert_formula_to_table_entry(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_convert_formula_to_table_entry"
    name = r.choice(SA_NAMES)
    m = r.choice([18, 22, 28, 32])
    c = r.choice([40, 60, 80])
    x_val = r.choice([7, 8, 9, 12])
    y_val = m * x_val + c
    correct_ans = f"{y_val}"

    prompt = (
        f"{name} is converting the formula **$y = {m}x + {c}$** into a table of values.\n\n"
        f"Calculate the output value $y$ for the table entry where **$x = {x_val}$**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Substitute the input value $x = {x_val}$ directly into the linear equation.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$y = ({m} \\times {x_val}) + {c} = {m * x_val} + {c}$$ ✓ [1 Mark: Method – substituting x into linear equation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$y = {y_val}$$ ✓ [1 Mark: Accuracy – accurate product and sum]"
    )

    d1 = f"{y_val + m}"
    d2 = f"{y_val - m}"
    d3 = f"{m * x_val}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply x by {m}, then add {c}.",
        tier_2=f"Calculate ({m} × {x_val}) + {c}.",
        tier_3=f"Value = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 46: Stepped Parking Tariff Graph Reading
# --------------------------------------------------------------------------- #
def _gen_pat_rep_parking_step_tariff_graph_reading(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_parking_step_tariff_graph_reading"
    name = r.choice(SA_NAMES)
    tier1 = r.choice([10.0, 15.0, 20.0])
    tier2 = tier1 * 2
    tier3 = tier1 * 3 + r.choice([5.0, 10.0])
    tier4 = tier3 + r.choice([25.0, 30.0, 35.0])

    case = r.choice([
        ("1 hour and 15 minutes", tier1, "> 1 to 2 hours"),
        ("3 hours and 30 minutes", tier2, "> 2 to 4 hours"),
        ("4 hours and 45 minutes", tier3, "> 4 to 6 hours"),
        ("7 hours and 10 minutes", tier4, "> 6 hours"),
    ])
    duration, tariff, bracket = case
    correct_ans = _fmt_curr(tariff)

    prompt = (
        f"{name} parks at a shopping centre with a stepped tariff structure:\n"
        f"  • 0 to 1 hour: Free (R 0,00)\n"
        f"  • Over 1 hour up to 2 hours: {_fmt_curr(tier1)}\n"
        f"  • Over 2 hours up to 4 hours: {_fmt_curr(tier2)}\n"
        f"  • Over 4 hours up to 6 hours: {_fmt_curr(tier3)}\n"
        f"  • Over 6 hours: {_fmt_curr(tier4)}\n\n"
        f"How much parking fee must {name} pay for parking for **{duration}**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a stepped (piecewise constant) tariff, any duration falling within an interval is charged the constant rate of that horizontal step.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The parking duration of {duration} falls into the tier bracket: **{bracket}**.\n"
        f"The horizontal step for this tier is set at {_fmt_curr(tariff)}. ✓ [1 Mark: Method – identifying correct tariff step bracket]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Parking Fee}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate tariff fee]"
    )

    d1 = _fmt_curr(tariff - tier1) if tariff > tier1 else _fmt_curr(tier2)
    d2 = _fmt_curr(tariff + tier1)
    d3 = _fmt_curr(tariff * 1.5)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    step_diag = {
        "kind": "step_tariff",
        "blocks": [
            {"range": "0–1 hr", "rate": 0.0},
            {"range": ">1–2 hr", "rate": tier1},
            {"range": ">2–4 hr", "rate": tier2},
            {"range": ">4–6 hr", "rate": tier3},
            {"range": ">6 hr", "rate": tier4},
        ],
        "caption": f"Stepped Parking Tariff Hourly Rate Profile ({name})",
    }

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the time bracket that contains the duration.",
        tier_2=f"{duration} falls into the bracket '{bracket}'.",
        tier_3=f"Fee = {correct_ans}.",
        r=r,
        diagram_spec=step_diag,
    )

# --------------------------------------------------------------------------- #
# Subskill 47: Courier Stepped Rate Bracket
# --------------------------------------------------------------------------- #
def _gen_pat_rep_postage_courier_stepped_rate(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_postage_courier_stepped_rate"
    name = r.choice(SA_NAMES)
    parcel_mass = r.choice([3.2, 4.8, 6.5, 8.2, 11.0])

    if parcel_mass <= 5.0:
        bracket = "Up to 5 kg"
        cost = 95.00
    elif parcel_mass <= 10.0:
        bracket = "Over 5 kg up to 10 kg"
        cost = 145.00
    else:
        bracket = "Over 10 kg up to 15 kg"
        cost = 195.00

    correct_ans = _fmt_curr(cost)

    prompt = (
        f"{name} sends a parcel via courier with the following stepped mass tariff:\n"
        f"  • Up to 5 kg: R 95,00\n"
        f"  • Over 5 kg up to 10 kg: R 145,00\n"
        f"  • Over 10 kg up to 15 kg: R 195,00\n\n"
        f"Calculate the courier fee for a parcel weighing **{_fmt(parcel_mass)} kg**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Locate the weight interval on the stepped scale that encloses {_fmt(parcel_mass)} kg.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The mass {_fmt(parcel_mass)} kg falls into the bracket: **{bracket}**.\n"
        f"The corresponding flat fee is {_fmt_curr(cost)}. ✓ [1 Mark: Method – matching mass to stepped tier]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Courier Fee}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency fee]"
    )

    d1 = _fmt_curr(cost - 50) if cost > 95 else _fmt_curr(145.00)
    d2 = _fmt_curr(cost + 50)
    d3 = _fmt_curr(cost * 1.2)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine which mass bracket contains the parcel.",
        tier_2=f"{_fmt(parcel_mass)} kg is in '{bracket}'.",
        tier_3=f"Fee = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 48: Water Tiered Consumption Graph Slopes
# --------------------------------------------------------------------------- #
def _gen_pat_rep_water_tiered_consumption_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_water_tiered_consumption_graph"
    name = r.choice(SA_NAMES)
    step1_rate = 0.00
    step2_rate = r.choice([15.50, 18.00, 20.00])
    step3_rate = r.choice([25.00, 28.50, 32.00])

    prompt = (
        f"Refer to the municipal stepped water tariff graph below for domestic households in {name}'s town:\n"
        f"• Block 1 (0 to 6 kL): R {_fmt_curr(step1_rate)} per kL (Free basic water)\n"
        f"• Block 2 (>6 to 20 kL): R {_fmt_curr(step2_rate)} per kL\n"
        f"• Block 3 (>20 kL): R {_fmt_curr(step3_rate)} per kL\n\n"
        f"Why is a tiered water consumption tariff drawn as a stepped graph with horizontal line segments rather than a continuous straight line?"
    )
    ans = "The tariff rate per kilolitre remains constant within each consumption bracket (block), then abruptly jumps to a higher rate when crossing into the next bracket."
    opts = [
        "The tariff rate per kilolitre remains constant within each consumption bracket (block), then abruptly jumps to a higher rate when crossing into the next bracket.",
        "Water meters only register water flow on Sundays.",
        "The municipality changes prices every hour of the day.",
        "Stepped lines indicate that water is free of bacteria.",
    ]

    s1 = f"Understand piecewise step functions: rates are fixed within discrete interval intervals, causing discontinuous step jumps."
    s2 = f"✓ [1 Mark: Method – Identifying constant block rate property]\nTariff is constant within blocks, jumping between blocks."
    s3 = f"✓ [1 Mark: Accuracy – Correct rationale]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "step_tariff",
        "title": f"Municipal Water Step Tariff ({name})",
        "steps": [
            {"from_kl": 0, "to_kl": 6, "rate": step1_rate},
            {"from_kl": 6, "to_kl": 20, "rate": step2_rate},
            {"from_kl": 20, "to_kl": 40, "rate": step3_rate},
        ],
    }

    custom = [ans] + opts[1:]
    options, _ = _build_options(ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=ans,
        options=options,
        explanation=f"Step 1: {s1}\nStep 2: {s2}\nStep 3: {s3}",
        tier_1="What happens to the price per kL when you cross into a higher block?",
        tier_2="The price stays fixed in each block, then jumps up.",
        tier_3=f"{ans}",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} is studying the municipal water tariff graph showing total water cost against kilolitres consumed.\n"
        f"The graph consists of line segments that bend and become increasingly steep as consumption rises into higher blocks.\n\n"
        f"Explain why the line segments become **progressively steeper** at higher consumption volumes."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a cost-volume graph, the gradient (slope) represents the cost per unit (tariff per kilolitre: $\\text{{Rand}}/\\text{{kL}}$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Municipal water billing uses an inclining block tariff designed to encourage water conservation. "
        f"Because the price per kL increases in each consecutive tier, each additional kilolitre costs more, "
        f"making the slope of the line steeper. ✓ [1 Mark: Method – connecting increasing gradient to inclining block tariffs]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct economic and graphical interpretation]"
    )

    custom = [
        correct_ans,
        "The gradient becomes flatter because high water users receive a bulk discount",
        "The graph is horizontal because water is completely free in higher tiers",
        "The gradient remains identical because municipal water has a constant flat tariff",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Slope represents the cost per kilolitre.",
        tier_2="In South Africa, higher water usage blocks are charged at higher rates per kL.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 49: Simple Interest Linear Growth
# --------------------------------------------------------------------------- #
def _gen_pat_rep_bank_account_simple_interest_linear_growth(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_bank_account_simple_interest_linear_growth"
    name = r.choice(SA_NAMES)
    principal = r.choice([2000, 3000, 5000, 10000])
    rate_pct = r.choice([6, 8, 10])  # %
    years = r.choice([3, 4, 5])
    annual_interest = (principal * rate_pct) / 100.0
    total_amount = principal + annual_interest * years
    correct_ans = _fmt_curr(total_amount)

    prompt = (
        f"{name} deposits {_fmt_curr(principal)} into a fixed deposit account earning simple interest at {rate_pct}% per annum.\n"
        f"The linear growth formula is: **$A = P + (P \\times i \\times t)$**, where $t$ is time in years.\n\n"
        f"Calculate the total accumulated balance in the account after **{years} years**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Under simple interest, the annual interest earned is constant every year: $I = P \\times i$. "
        f"The total balance grows linearly over time.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Annual interest}} = {_fmt_curr(principal)} \\times \\frac{{{rate_pct}}}{{100}} = {_fmt_curr(annual_interest)}\\text{{ per year}}$$\n"
        f"$$\\text{{Total interest for {years} years}} = {_fmt_curr(annual_interest)} \\times {years} = {_fmt_curr(annual_interest * years)}$$\n"
        f"$$A = {_fmt_curr(principal)} + {_fmt_curr(annual_interest * years)}$$ ✓ [1 Mark: Method – substituting into simple interest linear model]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$A = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(principal + annual_interest)  # only 1 year
    d2 = _fmt_curr(annual_interest * years)  # only interest
    d3 = _fmt_curr(total_amount + 500)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Annual interest = Principal × rate. Multiply by years and add principal.",
        tier_2=f"Interest per year = {_fmt_curr(annual_interest)}. For {years} years = {_fmt_curr(annual_interest * years)}. Add {_fmt_curr(principal)}.",
        tier_3=f"Total = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 50: Straight-Line Depreciation Model
# --------------------------------------------------------------------------- #
def _gen_pat_rep_straight_line_depreciation_model(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_straight_line_depreciation_model"
    name = r.choice(SA_NAMES)
    initial_cost = r.choice([15000, 20000, 25000, 30000])
    annual_deprec = r.choice([2000, 2500, 3000])
    years = r.choice([3, 4, 5])
    total_loss = annual_deprec * years
    book_value = initial_cost - total_loss
    correct_ans = _fmt_curr(book_value)

    prompt = (
        f"{name} purchases office computer equipment for {_fmt_curr(initial_cost)}.\n"
        f"The equipment depreciates linearly on a straight-line basis by {_fmt_curr(annual_deprec)} each year.\n"
        f"The formula is: **$\\text{{Value}} = {_fmt_curr(initial_cost)} - ({_fmt_curr(annual_deprec)} \\times t)$**, where $t$ is the age in years.\n\n"
        f"Calculate the book value of the equipment after **{years} years**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Straight-line depreciation reduces the value of the asset by the exact same fixed amount each year.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total depreciation}} = {_fmt_curr(annual_deprec)} \\times {years} = {_fmt_curr(total_loss)}$$\n"
        f"$$\\text{{Book Value}} = {_fmt_curr(initial_cost)} - {_fmt_curr(total_loss)}$$ ✓ [1 Mark: Method – subtracting accumulated depreciation from initial cost]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Book Value}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency balance]"
    )

    d1 = _fmt_curr(total_loss)  # depreciation amount instead of book value
    d2 = _fmt_curr(initial_cost - annual_deprec)  # only 1 year
    d3 = _fmt_curr(book_value - 1000)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply annual depreciation by number of years.",
        tier_2=f"Total depreciation = {years} × {_fmt_curr(annual_deprec)} = {_fmt_curr(total_loss)}. Subtract from {_fmt_curr(initial_cost)}.",
        tier_3=f"Book value = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 51: Loan Repayment Balance Reduction
# --------------------------------------------------------------------------- #
def _gen_pat_rep_loan_repayment_balance_reduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_loan_repayment_balance_reduction"
    name = r.choice(SA_NAMES)
    loan = r.choice([12000, 15000, 18000, 24000])
    monthly_pay = r.choice([500, 600, 750, 1000])
    months = r.choice([6, 8, 10, 12])
    paid = monthly_pay * months
    balance = loan - paid
    correct_ans = _fmt_curr(balance)

    prompt = (
        f"{name} borrows an interest-free student loan of {_fmt_curr(loan)}.\n"
        f"{name} repays the loan at a constant rate of {_fmt_curr(monthly_pay)} per month.\n"
        f"The remaining loan balance formula is: **$\\text{{Balance}} = {_fmt_curr(loan)} - ({_fmt_curr(monthly_pay)} \\times m)$**, where $m$ is months repaid.\n\n"
        f"Calculate the remaining loan balance after **{months} monthly payments**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Each payment linearly reduces the outstanding balance by {_fmt_curr(monthly_pay)}.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total repaid}} = {months} \\times {_fmt_curr(monthly_pay)} = {_fmt_curr(paid)}$$\n"
        f"$$\\text{{Remaining Balance}} = {_fmt_curr(loan)} - {_fmt_curr(paid)}$$ ✓ [1 Mark: Method – subtracting cumulative payments from loan principal]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Remaining Balance}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency remainder]"
    )

    d1 = _fmt_curr(paid)  # amount paid instead of remaining
    d2 = _fmt_curr(balance + monthly_pay)
    d3 = _fmt_curr(balance - monthly_pay)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply monthly payment by months elapsed.",
        tier_2=f"Total paid = {months} × {_fmt_curr(monthly_pay)} = {_fmt_curr(paid)}. Subtract from {_fmt_curr(loan)}.",
        tier_3=f"Balance = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 52: Selecting Best Mathematical Representation
# --------------------------------------------------------------------------- #
def _gen_pat_rep_summary_representation_choice(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_summary_representation_choice"
    name = r.choice(SA_NAMES)
    correct_ans = "A graphical representation (break-even line graph)"

    prompt = (
        f"{name} needs to present a cost-comparison of three competing business tenders to a school governing body.\n"
        f"The members need to immediately see at a glance where the costs cross over and which tender is cheapest across different volumes.\n\n"
        f"Which mathematical representation is **best suited** for visualizing trends and comparisons at a glance?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Different representations serve different purposes:\n"
        f"  • **Verbal**: Good for context and general explanation\n"
        f"  • **Table**: Good for exact discrete numerical values\n"
        f"  • **Formula**: Good for quick algebraic calculation with any input\n"
        f"  • **Graph**: Best for visualizing overall trends, rates of change, and points of intersection at a glance\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"To instantly identify crossovers, break-even points, and visual comparisons across multiple options, "
        f"a line graph is superior to tables or formulas. ✓ [1 Mark: Method – matching presentation objective to graphical modality]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct representation selection]"
    )

    custom = [
        correct_ans,
        "A long verbal written paragraph without numbers",
        "A raw table of unorganized numbers",
        "A complex cubic algebraic equation",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider which tool allows you to see visual crossover points at a glance.",
        tier_2="Graphs provide an immediate visual comparison of multiple options.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )
