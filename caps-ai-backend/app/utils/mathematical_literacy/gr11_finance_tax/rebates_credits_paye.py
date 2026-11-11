"""Cluster 4: Tax Rebates, Medical Credits & Net PAYE (Subskills 28 to 36)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    SARS_REBATES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_primary_rebate_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_primary_rebate_deduction"
    name = r.choice(SA_NAMES)
    age = r.randint(25, 58)
    tax_before = r.randint(35000, 65000)
    primary_rebate = SARS_REBATES["primary"]  # 17 235
    tax_after = max(0.0, round(tax_before - primary_rebate, 2))
    correct_ans = _fmt_curr(tax_after)

    prompt = (
        f"{name} is **{age} years old** and has calculated an annual tax liability of {_fmt_curr(tax_before)} before rebates.\n"
        f"In South Africa, all individual taxpayers qualify for the **Primary Tax Rebate of R 17 235** per year.\n\n"
        f"Calculate {name}'s net annual tax liability after deducting the primary rebate."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Tax rebates are direct reductions of the tax amount owed, not deductions from taxable income: "
        f"$$\\text{{Net Tax}} = \\text{{Tax Before Rebates}} - \\text{{Primary Rebate}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Net Tax}} = {_fmt_curr(tax_before)} - {_fmt_curr(primary_rebate)}$$ "
        f"✓ [1 Mark: Method – subtracting primary rebate from gross tax]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Tax}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency calculation]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract R 17 235 from the tax before rebates.",
        tier_2=f"{_fmt_curr(tax_before)} - R 17 235,00 = {correct_ans}.",
        tier_3=f"Net tax = {correct_ans}.",
        r=r,
    )


def _gen_secondary_rebate_over_65(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_secondary_rebate_over_65"
    name = r.choice(SA_NAMES)
    age = r.randint(66, 73)
    tax_before = r.randint(45000, 75000)
    primary = SARS_REBATES["primary"]      # 17 235
    secondary = SARS_REBATES["secondary"]  # 9 444
    total_rebate = primary + secondary     # 26 679
    net_tax = max(0.0, round(tax_before - total_rebate, 2))
    correct_ans = _fmt_curr(net_tax)

    prompt = (
        f"{name} is a retired specialist aged **{age} years** with a gross annual tax before rebates of {_fmt_curr(tax_before)}.\n\n"
        f"SARS Tax Rebates table:\n"
        f"  • Primary rebate (all natural persons): **R 17 235**\n"
        f"  • Secondary rebate (persons 65 and older): **R 9 444**\n\n"
        f"Calculate {name}'s net annual income tax liability after subtracting all qualifying rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Taxpayers aged 65 to 74 qualify for BOTH the Primary and Secondary rebates: "
        f"$$\\text{{Total Rebate}} = \\text{{R 17 235}} + \\text{{R 9 444}} = \\text{{R 26 679}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Net Tax}} = {_fmt_curr(tax_before)} - (\\text{{R 17 235,00}} + \\text{{R 9 444,00}}) = {_fmt_curr(tax_before)} - \\text{{R 26 679,00}}$$ "
        f"✓ [1 Mark: Method – summing primary and secondary rebates and subtracting from gross tax]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Tax}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate net tax currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add primary rebate (R 17 235) and secondary rebate (R 9 444), then subtract from tax.",
        tier_2=f"Total rebate = R 26 679. Net tax = {_fmt_curr(tax_before)} - R 26 679 = {correct_ans}.",
        tier_3=f"Net tax = {correct_ans}.",
        r=r,
    )


def _gen_tertiary_rebate_over_75(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_tertiary_rebate_over_75"
    name = r.choice(SA_NAMES)
    age = r.randint(76, 84)
    tax_before = r.randint(50000, 85000)
    primary = SARS_REBATES["primary"]      # 17 235
    secondary = SARS_REBATES["secondary"]  # 9 444
    tertiary = SARS_REBATES["tertiary"]    # 3 145
    total_rebate = primary + secondary + tertiary  # 29 824
    net_tax = max(0.0, round(tax_before - total_rebate, 2))
    correct_ans = _fmt_curr(net_tax)

    prompt = (
        f"{name} is a senior citizen aged **{age} years** with an annual tax liability of {_fmt_curr(tax_before)} before rebates.\n\n"
        f"SARS Tax Rebates table:\n"
        f"  • Primary rebate (all persons): **R 17 235**\n"
        f"  • Secondary rebate (persons 65 and older): **R 9 444**\n"
        f"  • Tertiary rebate (persons 75 and older): **R 3 145**\n\n"
        f"Calculate {name}'s net annual tax liability after deducting all three statutory rebates."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Taxpayers aged 75 and older qualify for ALL THREE rebates (Primary + Secondary + Tertiary): "
        f"$$\\text{{Total Rebate}} = 17\\,235 + 9\\,444 + 3\\,145 = \\text{{R 29 824}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Net Tax}} = {_fmt_curr(tax_before)} - \\text{{R 29 824,00}}$$ "
        f"✓ [1 Mark: Method – summing all 3 age-tiered rebates and subtracting from gross tax]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Tax}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency calculation]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add primary (R 17 235), secondary (R 9 444), and tertiary (R 3 145) rebates.",
        tier_2=f"Total rebates = R 29 824. Subtract from {_fmt_curr(tax_before)}.",
        tier_3=f"Net tax = {correct_ans}.",
        r=r,
    )


def _gen_annual_net_tax_after_rebates(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_annual_net_tax_after_rebates"
    name = r.choice(SA_NAMES)
    income = r.randint(280000, 360000)
    excess = income - 237100
    gross_tax = round(42678 + (excess * 0.26), 2)
    rebate = SARS_REBATES["primary"]
    net_tax = round(gross_tax - rebate, 2)
    correct_ans = _fmt_curr(net_tax)

    prompt = (
        f"{name} (aged 38) earns an annual taxable income of {_fmt_curr(income)}.\n\n"
        f"SARS Bracket 2 rule: **Tax = R 42 678 + 26% of taxable income above R 237 100**\n"
        f"Primary rebate: **R 17 235**\n\n"
        f"Calculate {name}'s final net annual income tax liability."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate gross tax using the Bracket 2 formula, then subtract the primary rebate: "
        f"$$\\text{{Net Tax}} = \\text{{Gross Tax}} - \\text{{Primary Rebate}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Excess}} = {_fmt_curr(income)} - \\text{{R 237 100,00}} = {_fmt_curr(excess)}$$\n"
        f"$$\\text{{Gross Tax}} = \\text{{R 42 678,00}} + ({_fmt_curr(excess)} \\times 0,26) = {_fmt_curr(gross_tax)}$$\n"
        f"$$\\text{{Net Tax}} = {_fmt_curr(gross_tax)} - \\text{{R 17 235,00}}$$ "
        f"✓ [1 Mark: Method – calculating bracket tax and subtracting primary rebate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Tax}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate net annual tax]"
    )

    options, _ = _build_options(correct_ans, r)
    d_spec = {
        "diagram_role": "context",
        "kind": "step_tariff",
        "title": f"SARS Income Tax Bracket 2 Calculation ({name})",
        "blocks": [{"limit": 237100, "rate": 18}, {"limit": 305526, "rate": 26}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate gross tax using Bracket 2, then subtract R 17 235.",
        tier_2=f"Gross tax = {_fmt_curr(gross_tax)}. Net tax = {_fmt_curr(gross_tax)} - R 17 235 = {correct_ans}.",
        tier_3=f"Net tax = {correct_ans}.",
        r=r,
    )


def _gen_monthly_paye_deduction(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_monthly_paye_deduction"
    name = r.choice(SA_NAMES)
    annual_tax = r.randint(36000, 78000)
    monthly_paye = round(annual_tax / 12.0, 2)
    correct_ans = _fmt_curr(monthly_paye)

    prompt = (
        f"After applying statutory tax rates and rebates, {name}'s net annual income tax liability is **{_fmt_curr(annual_tax)}**.\n\n"
        f"Calculate the monthly **PAYE (Pay-As-You-Earn)** amount that must be deducted from {name}'s payslip each month."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Employers deduct PAYE in equal monthly installments over the 12 calendar months: "
        f"$$\\text{{Monthly PAYE}} = \\frac{{\\text{{Net Annual Tax}}}}{{12}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Monthly PAYE}} = \\frac{{{_fmt_curr(annual_tax)}}}{{12}}$$ "
        f"✓ [1 Mark: Method – dividing net annual tax liability by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Monthly PAYE}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate monthly currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the annual tax amount by 12.",
        tier_2=f"{_fmt_curr(annual_tax)} ÷ 12 = {correct_ans}.",
        tier_3=f"Monthly PAYE = {correct_ans}.",
        r=r,
    )


def _gen_medical_tax_credit_annual(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_medical_tax_credit_annual"
    name = r.choice(SA_NAMES)
    # SARS Medical Scheme Fees Tax Credit (MTC):
    # Main member: R 364/month
    # First dependant: R 364/month
    # Additional dependants: R 246/month each
    rate_main = 364.00
    rate_first = 364.00
    rate_add = 246.00
    extra_deps = r.randint(1, 3)
    monthly_mtc = rate_main + rate_first + (extra_deps * rate_add)
    annual_mtc = round(monthly_mtc * 12.0, 2)
    correct_ans = _fmt_curr(annual_mtc)

    total_dependants = 1 + extra_deps  # 1 first dep + extra
    prompt = (
        f"{name} contributes to a registered medical aid scheme for themselves and **{total_dependants} dependants** (spouse + {extra_deps} children).\n\n"
        f"SARS Section 6A Medical Scheme Fees Tax Credits:\n"
        f"  • Taxpayer (main member): **R 364 per month**\n"
        f"  • First dependant: **R 364 per month**\n"
        f"  • Each additional dependant: **R 246 per month**\n\n"
        f"Calculate the **total annual Medical Tax Credit** that will reduce {name}'s tax liability."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate total monthly credits for main member, first dependant, and remaining dependants, then multiply by 12 months.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Monthly MTC}} = \\text{{R 364}} + \\text{{R 364}} + ({extra_deps} \\times \\text{{R 246}}) = {_fmt_curr(monthly_mtc)}$$\n"
        f"$$\\text{{Annual MTC}} = {_fmt_curr(monthly_mtc)} \\times 12$$ "
        f"✓ [1 Mark: Method – summing monthly credits and annualizing by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Annual Medical Tax Credit}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate annual currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Monthly = R 364 + R 364 + ({extra_deps} × R 246). Multiply total by 12.",
        tier_2=f"Monthly = {_fmt_curr(monthly_mtc)}. Annual = {_fmt_curr(monthly_mtc)} × 12 = {correct_ans}.",
        tier_3=f"Annual MTC = {correct_ans}.",
        r=r,
    )


def _gen_net_paye_after_medical_credits(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_net_paye_after_medical_credits"
    name = r.choice(SA_NAMES)
    paye_before_mtc = r.randint(3200, 5800)
    mtc_monthly = r.choice([364.00, 728.00, 974.00, 1220.00])
    net_paye = round(paye_before_mtc - mtc_monthly, 2)
    correct_ans = _fmt_curr(net_paye)

    prompt = (
        f"{name}'s preliminary monthly PAYE deduction before medical tax credits is {_fmt_curr(paye_before_mtc)}.\n"
        f"{name} qualifies for a monthly Medical Scheme Fees Tax Credit of **{_fmt_curr(mtc_monthly)}**.\n\n"
        f"Calculate {name}'s **final monthly PAYE deduction** after applying the medical tax credit."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Medical tax credits are deducted directly from the monthly PAYE tax amount: "
        f"$$\\text{{Final Monthly PAYE}} = \\text{{Monthly PAYE Before Credit}} - \\text{{Monthly Medical Tax Credit}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Final PAYE}} = {_fmt_curr(paye_before_mtc)} - {_fmt_curr(mtc_monthly)}$$ "
        f"✓ [1 Mark: Method – subtracting monthly medical tax credit from monthly PAYE]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Final PAYE}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency deduction]"
    )

    options, _ = _build_options(correct_ans, r)
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Monthly PAYE and Medical Tax Credits ({name})",
        "categories": ["Preliminary PAYE", "Medical Credits", "Net PAYE"],
        "values": [paye_before_mtc, mtc_monthly, net_paye],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the medical tax credit from preliminary PAYE.",
        tier_2=f"{_fmt_curr(paye_before_mtc)} - {_fmt_curr(mtc_monthly)} = {correct_ans}.",
        tier_3=f"Final PAYE = {correct_ans}.",
        r=r,
    )


def _gen_effective_tax_rate_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_effective_tax_rate_calculation"
    name = r.choice(SA_NAMES)
    taxable_income = r.choice([250000, 300000, 350000, 400000])
    net_tax_paid = round(taxable_income * r.uniform(0.12, 0.19), 2)
    eff_rate = round((net_tax_paid / taxable_income) * 100.0, 2)
    correct_ans = f"{_fmt(eff_rate)}%"

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(taxable_income)} and pays a total net annual tax of {_fmt_curr(net_tax_paid)}.\n\n"
        f"Formula: $$\\text{{Effective Tax Rate}} = \\frac{{\\text{{Net Annual Tax Paid}}}}{{\\text{{Annual Taxable Income}}}} \\times 100\\%$$\n\n"
        f"Calculate {name}'s **effective tax rate** (percentage of taxable income actually paid as tax)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The effective tax rate represents the average percentage of total income paid in tax across all brackets.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Effective Tax Rate}} = \\frac{{{_fmt_curr(net_tax_paid)}}}{{{_fmt_curr(taxable_income)}}} \\times 100\\%$$ "
        f"✓ [1 Mark: Method – dividing net tax paid by taxable income and multiplying by 100]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Effective Tax Rate}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate percentage rounded to 2 decimals]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide net tax paid by taxable income and multiply by 100.",
        tier_2=f"({_fmt_curr(net_tax_paid)} ÷ {_fmt_curr(taxable_income)}) × 100.",
        tier_3=f"Effective rate = {correct_ans}.",
        r=r,
    )


def _gen_bonus_thirteenth_cheque_tax(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_bonus_thirteenth_cheque_tax"
    name = r.choice(SA_NAMES)
    monthly_basic = r.randint(18000, 32000)
    marginal_rate = r.choice([0.26, 0.31])
    bonus_tax = round(monthly_basic * marginal_rate, 2)
    net_bonus = round(monthly_basic - bonus_tax, 2)
    correct_ans = _fmt_curr(net_bonus)

    rate_pct = int(marginal_rate * 100)
    prompt = (
        f"In December, {name} receives a 13th cheque (annual bonus) equal to one month's basic salary of {_fmt_curr(monthly_basic)}.\n"
        f"Because this bonus is additional income on top of annual earnings, it is taxed at {name}'s marginal rate of **{rate_pct}%**.\n\n"
        f"Calculate the **net take-home bonus amount** {name} will receive after tax."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate the tax on the bonus by multiplying by the marginal tax rate ({rate_pct}%), then subtract this tax from the gross bonus: "
        f"$$\\text{{Net Bonus}} = \\text{{Gross Bonus}} - (\\text{{Gross Bonus}} \\times {rate_pct}\\%)$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Tax on Bonus}} = {_fmt_curr(monthly_basic)} \\times {_fmt(marginal_rate)} = {_fmt_curr(bonus_tax)}$$\n"
        f"$$\\text{{Net Bonus}} = {_fmt_curr(monthly_basic)} - {_fmt_curr(bonus_tax)}$$ "
        f"✓ [1 Mark: Method – applying marginal tax rate to bonus and subtracting from gross bonus]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net Take-home Bonus}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate net bonus currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Tax = {_fmt_curr(monthly_basic)} × {rate_pct}%. Subtract this tax from the bonus.",
        tier_2=f"Tax = {_fmt_curr(bonus_tax)}. Net bonus = {_fmt_curr(monthly_basic)} - {_fmt_curr(bonus_tax)} = {correct_ans}.",
        tier_3=f"Net bonus = {correct_ans}.",
        r=r,
    )
