"""Cluster 3: SARS Progressive Income Tax Brackets (PAYE) (Subskills 19 to 27)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    SARS_TAX_BRACKETS,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_tax_bracket_identification(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_bracket_identification"
    name = r.choice(SA_NAMES)
    bracket_idx = r.choice([1, 2, 3, 4])  # 1-based bracket number
    b = SARS_TAX_BRACKETS[bracket_idx - 1]
    min_i, max_i = b[0], b[1]
    income = r.randint(int(min_i) + 5000, int(min_i + 80000) if max_i == float("inf") else int(max_i) - 5000)
    correct_ans = f"Bracket {bracket_idx} (R {int(min_i):,} to R {int(max_i):,})".replace(",", " ")

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(income)}.\n\n"
        f"Refer to the SARS Individual Tax Bracket table below:\n"
        f"  • **Bracket 1**: R 0 – R 237 100\n"
        f"  • **Bracket 2**: R 237 101 – R 370 500\n"
        f"  • **Bracket 3**: R 370 501 – R 512 800\n"
        f"  • **Bracket 4**: R 512 801 – R 673 000\n"
        f"  • **Bracket 5**: R 673 001 – R 857 900\n\n"
        f"Identify the specific **tax bracket** into which {name}'s annual income falls."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Compare the annual taxable income ({_fmt_curr(income)}) against the statutory bracket intervals.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The income of {_fmt_curr(income)} is greater than {_fmt_curr(min_i)} and less than or equal to {_fmt_curr(max_i)}.\n"
        f"Therefore, it falls in Bracket {bracket_idx}. ✓ [1 Mark: Method – matching income with lower and upper bracket bounds]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct bracket identification]"
    )

    custom = [
        f"Bracket 1 (R 0 to R 237 100)",
        f"Bracket 2 (R 237 101 to R 370 500)",
        f"Bracket 3 (R 370 501 to R 512 800)",
        f"Bracket 4 (R 512 801 to R 673 000)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Locate the range that contains the given salary.",
        tier_2=f"{_fmt_curr(income)} lies between {_fmt_curr(min_i)} and {_fmt_curr(max_i)}.",
        tier_3=f"Bracket = {correct_ans}.",
        r=r,
    )


def _gen_tax_bracket_1_direct_percentage(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_bracket_1_direct_percentage"
    name = r.choice(SA_NAMES)
    income = r.randint(140000, 230000)
    tax_val = round(income * 0.18, 2)
    correct_ans = _fmt_curr(tax_val)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(income)}.\n"
        f"According to the SARS tax table for Bracket 1 (R 0 – R 237 100), tax is charged at **18% of taxable income**.\n\n"
        f"Calculate {name}'s tax before rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In Bracket 1, tax is calculated directly as 18% of the full taxable income without any threshold excess subtraction.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Tax Before Rebates}} = {_fmt_curr(income)} \\times 18\\% = {_fmt_curr(income)} \\times 0,18$$ "
        f"✓ [1 Mark: Method – multiplying taxable income by 18%]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Tax Before Rebates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency calculation]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply taxable income by 18% (0,18).",
        tier_2=f"{_fmt_curr(income)} × 0,18 = {correct_ans}.",
        tier_3=f"Tax = {correct_ans}.",
        r=r,
    )


def _gen_tax_bracket_2_threshold_excess(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_bracket_2_threshold_excess"
    name = r.choice(SA_NAMES)
    income = r.randint(260000, 360000)
    threshold = 237100
    base_tax = 42678
    rate = 0.26
    excess = income - threshold
    tax_val = round(base_tax + (excess * rate), 2)
    correct_ans = _fmt_curr(tax_val)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(income)}.\n\n"
        f"SARS Tax Bracket 2 (R 237 101 – R 370 500) tax rule:\n"
        f"$$\\text{{Tax}} = \\text{{R 42 678}} + 26\\% \\text{{ of taxable income above R 237 100}}$$\n\n"
        f"Calculate {name}'s income tax before rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Subtract the lower threshold (R 237 100) from the income to find the excess amount taxed at 26%, then add the base tax.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Excess above threshold}} = {_fmt_curr(income)} - \\text{{R 237 100,00}} = {_fmt_curr(excess)}$$\n"
        f"$$\\text{{Tax on excess}} = {_fmt_curr(excess)} \\times 0,26 = {_fmt_curr(excess * rate)}$$\n"
        f"$$\\text{{Total Tax Before Rebates}} = \\text{{R 42 678,00}} + {_fmt_curr(excess * rate)}$$ "
        f"✓ [1 Mark: Method – subtracting threshold and calculating base + 26% of excess]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Tax Before Rebates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract R 237 100 from income, multiply by 0,26, then add R 42 678.",
        tier_2=f"Excess = {_fmt_curr(excess)}. Tax = R 42 678 + ({_fmt_curr(excess)} × 0,26).",
        tier_3=f"Tax = {correct_ans}.",
        r=r,
    )


def _gen_tax_bracket_3_threshold_excess(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_bracket_3_threshold_excess"
    name = r.choice(SA_NAMES)
    income = r.randint(390000, 500000)
    threshold = 370500
    base_tax = 77362
    rate = 0.31
    excess = income - threshold
    tax_val = round(base_tax + (excess * rate), 2)
    correct_ans = _fmt_curr(tax_val)

    prompt = (
        f"{name} earns an annual taxable remuneration of {_fmt_curr(income)}.\n\n"
        f"SARS Tax Bracket 3 (R 370 501 – R 512 800) tax rule:\n"
        f"$$\\text{{Tax}} = \\text{{R 77 362}} + 31\\% \\text{{ of taxable income above R 370 500}}$$\n\n"
        f"Calculate {name}'s income tax before rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the taxable amount exceeding R 370 500, apply 31%, and add the base tax of R 77 362.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Excess}} = {_fmt_curr(income)} - \\text{{R 370 500,00}} = {_fmt_curr(excess)}$$\n"
        f"$$\\text{{Tax on excess}} = {_fmt_curr(excess)} \\times 0,31 = {_fmt_curr(excess * rate)}$$\n"
        f"$$\\text{{Total Tax Before Rebates}} = \\text{{R 77 362,00}} + {_fmt_curr(excess * rate)}$$ "
        f"✓ [1 Mark: Method – applying Bracket 3 formula with 31% excess]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Tax Before Rebates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract R 370 500 from income, multiply by 0,31, then add R 77 362.",
        tier_2=f"Excess = {_fmt_curr(excess)}. Tax = R 77 362 + ({_fmt_curr(excess)} × 0,31).",
        tier_3=f"Tax = {correct_ans}.",
        r=r,
    )


def _gen_tax_bracket_4_threshold_excess(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_bracket_4_threshold_excess"
    name = r.choice(SA_NAMES)
    income = r.randint(530000, 660000)
    threshold = 512800
    base_tax = 121475
    rate = 0.36
    excess = income - threshold
    tax_val = round(base_tax + (excess * rate), 2)
    correct_ans = _fmt_curr(tax_val)

    prompt = (
        f"{name} works as an engineering manager with an annual taxable income of {_fmt_curr(income)}.\n\n"
        f"SARS Tax Bracket 4 (R 512 801 – R 673 000) tax rule:\n"
        f"$$\\text{{Tax}} = \\text{{R 121 475}} + 36\\% \\text{{ of taxable income above R 512 800}}$$\n\n"
        f"Calculate {name}'s gross tax liability before rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Determine the excess income above R 512 800, tax it at 36%, and add the fixed base tax of R 121 475.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Excess}} = {_fmt_curr(income)} - \\text{{R 512 800,00}} = {_fmt_curr(excess)}$$\n"
        f"$$\\text{{Tax on excess}} = {_fmt_curr(excess)} \\times 0,36 = {_fmt_curr(excess * rate)}$$\n"
        f"$$\\text{{Tax Before Rebates}} = \\text{{R 121 475,00}} + {_fmt_curr(excess * rate)}$$ "
        f"✓ [1 Mark: Method – applying Bracket 4 formula correctly]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Tax Before Rebates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract R 512 800 from income, multiply by 0,36, then add R 121 475.",
        tier_2=f"Excess = {_fmt_curr(excess)}. Tax = R 121 475 + ({_fmt_curr(excess)} × 0,36).",
        tier_3=f"Tax = {correct_ans}.",
        r=r,
    )


def _gen_annual_salary_from_monthly_taxable(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_annual_salary_from_monthly_taxable"
    name = r.choice(SA_NAMES)
    monthly = r.randint(18000, 42000)
    annual = monthly * 12
    correct_ans = _fmt_curr(annual)

    prompt = (
        f"{name}'s monthly taxable income on their pay slip is {_fmt_curr(monthly)}.\n"
        f"In South Africa, SARS progressive tax tables are structured on an **annual income basis**.\n\n"
        f"Calculate {name}'s equivalent annual taxable income."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Convert monthly earnings to annual remuneration by multiplying by 12 calendar months: "
        f"$$\\text{{Annual Income}} = \\text{{Monthly Income}} \\times 12$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Annual Income}} = {_fmt_curr(monthly)} \\times 12$$ "
        f"✓ [1 Mark: Method – multiplying monthly taxable income by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Annual Income}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate annual currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly salary by 12.",
        tier_2=f"{_fmt_curr(monthly)} × 12 = {correct_ans}.",
        tier_3=f"Annual income = {correct_ans}.",
        r=r,
    )


def _gen_tax_threshold_exemption_check(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_threshold_exemption_check"
    name = r.choice(SA_NAMES)
    # SARS Tax-Free Threshold for person under 65: Primary rebate R 17 235 / 0.18 = R 95 750 / year
    threshold_under_65 = 95750.00
    is_exempt = r.choice([True, False])
    if is_exempt:
        annual_inc = r.randint(65000, 92000)
        correct_ans = f"Exempt from PAYE (Income {_fmt_curr(annual_inc)} is below the tax threshold of R 95 750)"
    else:
        annual_inc = r.randint(105000, 160000)
        correct_ans = f"Liable to pay PAYE (Income {_fmt_curr(annual_inc)} exceeds the tax threshold of R 95 750)"

    prompt = (
        f"{name} (aged 24) earns an annual taxable income of {_fmt_curr(annual_inc)}.\n"
        f"In South Africa, the **tax-free threshold** for taxpayers under 65 years of age is **R 95 750** per year.\n\n"
        f"Determine whether {name} is liable to pay personal income tax (PAYE)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"If annual taxable income is less than or equal to the tax threshold (R 95 750), the primary rebate exceeds or equals "
        f"the tax before rebates, meaning zero net tax is owed.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Compare {_fmt_curr(annual_inc)} against the threshold threshold of R 95 750,00. "
        f"✓ [1 Mark: Method – comparing income against statutory threshold]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate liability status]"
    )

    custom = [
        f"Exempt from PAYE (Income {_fmt_curr(annual_inc)} is below the tax threshold of R 95 750)",
        f"Liable to pay PAYE (Income {_fmt_curr(annual_inc)} exceeds the tax threshold of R 95 750)",
        "Exempt because all citizens under 25 pay zero tax",
        "Liable because everyone who works in South Africa must pay at least R 1 000 tax",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Compare the annual income to R 95 750.",
        tier_2=f"Income is {_fmt_curr(annual_inc)}. Threshold is R 95 750.",
        tier_3=f"Status: {correct_ans}.",
        r=r,
    )


def _gen_marginal_tax_rate_identification(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_marginal_tax_rate_identification"
    name = r.choice(SA_NAMES)
    bracket_idx = r.choice([1, 2, 3, 4])
    b = SARS_TAX_BRACKETS[bracket_idx - 1]
    rate_pct = int(b[3] * 100)
    income = r.randint(int(b[0]) + 10000, int(b[1]) - 10000 if b[1] != float("inf") else int(b[0]) + 50000)
    correct_ans = f"{rate_pct}%"

    prompt = (
        f"{name} earns an annual taxable remuneration of {_fmt_curr(income)}.\n"
        f"This income places {name} into SARS **Bracket {bracket_idx}**.\n\n"
        f"What is {name}'s **marginal tax rate** (the tax percentage applied to each additional Rand of income earned)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The marginal tax rate is the specific percentage rate that applies to the highest bracket of income earned.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"According to the SARS tax table, Bracket {bracket_idx} levies a tax rate of {rate_pct}% on income within this band. "
        f"✓ [1 Mark: Method – identifying marginal rate for Bracket {bracket_idx}]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Marginal Tax Rate}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate marginal percentage]"
    )

    custom = ["18%", "26%", "31%", "36%"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Look up the percentage for Bracket {bracket_idx} in the tax table.",
        tier_2=f"Bracket {bracket_idx} has a rate of {rate_pct}%.",
        tier_3=f"Marginal rate = {correct_ans}.",
        r=r,
    )


def _gen_tax_liability_before_rebates(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tax_liability_before_rebates"
    name = r.choice(SA_NAMES)
    income = r.randint(250000, 350000)
    excess = income - 237100
    tax_val = round(42678 + (excess * 0.26), 2)
    correct_ans = _fmt_curr(tax_val)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(income)}.\n"
        f"Using the tax formula for Bracket 2: **Tax = R 42 678 + 26% of taxable income above R 237 100**.\n\n"
        f"Calculate {name}'s **gross tax liability before rebates** are applied."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Compute the excess above R 237 100, calculate 26% of this excess, and add R 42 678.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Excess}} = {_fmt_curr(income)} - \\text{{R 237 100,00}} = {_fmt_curr(excess)}$$\n"
        f"$$\\text{{Tax on excess}} = {_fmt_curr(excess)} \\times 0,26 = {_fmt_curr(excess * 0.26)}$$\n"
        f"$$\\text{{Gross Tax}} = \\text{{R 42 678,00}} + {_fmt_curr(excess * 0.26)}$$ "
        f"✓ [1 Mark: Method – evaluating bracket formula setup]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Gross Tax Before Rebates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency sum]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract R 237 100 from income, multiply by 0,26, then add R 42 678.",
        tier_2=f"Excess = {_fmt_curr(excess)}. Tax = R 42 678 + ({_fmt_curr(excess)} × 0,26).",
        tier_3=f"Gross tax = {correct_ans}.",
        r=r,
    )
