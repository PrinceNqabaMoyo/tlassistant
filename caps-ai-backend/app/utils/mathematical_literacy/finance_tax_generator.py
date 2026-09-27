"""Grade 10–12 Mathematical Literacy — Finance & SARS Income Tax (Deterministic 6-Pillar Generator).
Covers personal income tax, SARS sliding tax tables, age rebates, medical scheme fees tax credits,
and monthly PAYE deductions (Paper 1, Term 1).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}"
    return s.replace(".", "{,}")


# Official CAPS South African Personal Income Tax Brackets (Annual)
TAX_BRACKETS = [
    {"min": 1, "max": 237100, "base": 0, "rate": 0.18, "over": 0},
    {"min": 237101, "max": 370500, "base": 42678, "rate": 0.26, "over": 237100},
    {"min": 370501, "max": 512800, "base": 77362, "rate": 0.31, "over": 370500},
    {"min": 512801, "max": 673000, "base": 121475, "rate": 0.36, "over": 512800},
    {"min": 673001, "max": 857900, "base": 179147, "rate": 0.39, "over": 673000},
    {"min": 857901, "max": 1817000, "base": 251258, "rate": 0.41, "over": 857900},
]

PRIMARY_REBATE = 17235.0
SECONDARY_REBATE = 9444.0   # Age 65 and older
TERTIARY_REBATE = 3145.0    # Age 75 and older

# Medical scheme fees tax credits (per month)
MED_CREDIT_MAIN = 364.0
MED_CREDIT_FIRST_DEP = 364.0
MED_CREDIT_ADDITIONAL = 246.0

NAMES_POOL = ["Sipho", "Anika", "Lerato", "Johan", "Nandi", "Farai", "Zanele", "Trevor", "Thabo", "Devan"]


# --------------------------------------------------------------------------- #
# Sub-Drill: Taxable Income Calculation
# --------------------------------------------------------------------------- #
def _build_taxable_income_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(NAMES_POOL)
    monthly_gross = r.randint(25, 65) * 1000
    pension_percent = r.choice([5.0, 7.5])
    monthly_pension = round(monthly_gross * (pension_percent / 100), 2)

    annual_gross = monthly_gross * 12
    annual_pension = monthly_pension * 12
    taxable_income = annual_gross - annual_pension

    prompt = (
        f"{name} earns a gross monthly salary of **R{monthly_gross:,}** and contributes "
        f"**{_fmt_sa(pension_percent)}\\%** of their salary towards an approved pension fund each month.\n\n"
        f"1. Calculate {name}'s annual gross salary.\n"
        f"2. Calculate {name}'s annual pension fund contribution.\n"
        f"3. Calculate {name}'s annual **taxable income**."
    ).replace(",", " ")

    ans_latex = (
        rf"\text{{Gross}} = \text{{R}}{annual_gross:,}, \quad "
        rf"\text{{Pension}} = \text{{R}}{int(annual_pension):,}, \quad "
        rf"\text{{Taxable Income}} = \text{{R}}{int(taxable_income):,}"
    ).replace(",", " ")

    sample_answer = (
        f"1. Annual Gross Salary:\n"
        f"   $\\text{{R}}{monthly_gross:,} \\times 12 = \\text{{R}}{annual_gross:,}$\n\n"
        f"2. Annual Pension Contribution ({_fmt_sa(pension_percent)}%):\n"
        f"   $\\text{{R}}{annual_gross:,} \\times {_fmt_sa(pension_percent / 100)} = \\text{{R}}{int(annual_pension):,}$\n\n"
        f"3. Annual Taxable Income:\n"
        f"   $\\text{{R}}{annual_gross:,} - \\text{{R}}{int(annual_pension):,} = \\text{{R}}{int(taxable_income):,}$"
    ).replace(",", " ")

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Multiply monthly gross by 12", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Calculate annual pension contribution", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Subtract pension to find taxable income", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Multiply monthly amounts by 12 to find the annual values.",
        "tier_2": "Taxable Income = Annual Gross Income - Tax-Exempt Pension Contributions.",
        "tier_3": f"Taxable Income = R{annual_gross:,} - R{int(annual_pension):,} = R{int(taxable_income):,}.".replace(",", " "),
    }

    return {
        "id": f"mathlit_taxinc_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_taxinc_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_finance_tax",
        "subskill": "taxable_income_elementary",
        "learning_objective_id": "mathlit_taxable_income",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_multiply_by_12", "added_pension_to_taxable_income"],
        "keywords": ["taxable income", "gross salary", "pension deduction", "annual income"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_taxable_income",
        "difficulty": "easy",
        "marks": 3,
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: SARS Tax Bracket Identification & Marginal Tax
# --------------------------------------------------------------------------- #
def _build_tax_bracket_drill(r: random.Random) -> Dict[str, Any]:
    taxable_income = r.choice([290000, 340000, 420000, 480000, 560000, 620000, 750000])
    bracket = next(b for b in TAX_BRACKETS if b["min"] <= taxable_income <= b["max"])

    over_amount = taxable_income - bracket["over"]
    rate_tax = round(over_amount * bracket["rate"], 2)
    tax_before_rebate = round(bracket["base"] + rate_tax, 2)

    prompt = (
        f"A taxpayer has an annual taxable income of **R{taxable_income:,}**.\n\n"
        f"Using the official SARS Income Tax Table:\n"
        f"- Bracket 1: R1 to R237 100: 18% of taxable income\n"
        f"- Bracket 2: R237 101 to R370 500: R42 678 + 26% of taxable income above R237 100\n"
        f"- Bracket 3: R370 501 to R512 800: R77 362 + 31% of taxable income above R370 500\n"
        f"- Bracket 4: R512 801 to R673 000: R121 475 + 36% of taxable income above R512 800\n"
        f"- Bracket 5: R673 001 to R857 900: R179 147 + 39% of taxable income above R673 000\n\n"
        f"1. Identify the applicable tax bracket.\n"
        f"2. Calculate the taxable amount above the bracket threshold.\n"
        f"3. Calculate the total **tax before rebates**."
    ).replace(",", " ")

    ans_latex = (
        rf"\text{{Tax before rebate}} = \text{{R}}{bracket['base']:,} + {_fmt_sa(bracket['rate']*100)}\% \times "
        rf"\text{{R}}{over_amount:,} = \text{{R}}{tax_before_rebate:,.2f}"
    ).replace(",", " ")

    sample_answer = (
        f"1. Applicable Bracket: R{bracket['min']:,} – R{bracket['max']:,}\n"
        f"2. Amount above threshold:\n"
        f"   $\\text{{R}}{taxable_income:,} - \\text{{R}}{bracket['over']:,} = \\text{{R}}{over_amount:,}$\n"
        f"3. Tax Before Rebates:\n"
        f"   $\\text{{R}}{bracket['base']:,} + ({_fmt_sa(bracket['rate'])} \\times \\text{{R}}{over_amount:,}) = \\text{{R}}{tax_before_rebate:,.2f}$"
    ).replace(",", " ")

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct bracket identified (R{bracket['min']} - R{bracket['max']})", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Amount over threshold: R{over_amount}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Tax before rebates: R{tax_before_rebate:.2f}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "taxed_entire_amount_at_marginal_rate", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": f"Compare R{taxable_income:,} against the bracket min and max values.".replace(",", " "),
        "tier_2": "Calculate: Base Tax + Rate% x (Taxable Income - Threshold).",
        "tier_3": f"Tax before rebate = R{bracket['base']:,} + ({int(bracket['rate']*100)}% x R{over_amount:,}) = R{tax_before_rebate:,.2f}.".replace(",", " "),
    }

    return {
        "id": f"mathlit_taxbrk_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_taxbrk_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_finance_tax",
        "subskill": "tax_bracket_elementary",
        "learning_objective_id": "mathlit_tax_bracket",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["taxed_entire_amount_at_marginal_rate", "selected_wrong_tax_bracket"],
        "keywords": ["SARS tax table", "marginal rate", "threshold", "tax before rebates"],
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "mode": "elementary_tax_bracket_id",
        "difficulty": "medium",
        "marks": 3,
    }


# --------------------------------------------------------------------------- #
# Compound: Full Authentic CAPS Personal Income Tax & PAYE (8 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_tax(r: random.Random) -> Dict[str, Any]:
    name = r.choice(NAMES_POOL)
    age = r.choice([32, 45, 58, 66, 72])
    is_elderly = age >= 65
    num_dependants = r.choice([0, 1, 2, 3])

    monthly_salary = r.randint(28, 72) * 1000
    annual_salary = monthly_salary * 12

    # Find tax bracket
    bracket = next(b for b in TAX_BRACKETS if b["min"] <= annual_salary <= b["max"])
    over_amount = annual_salary - bracket["over"]
    tax_before_rebate = round(bracket["base"] + (over_amount * bracket["rate"]), 2)

    # Rebates
    rebate = PRIMARY_REBATE + (SECONDARY_REBATE if is_elderly else 0.0)

    # Medical credits
    if num_dependants == 0:
        monthly_med_credit = MED_CREDIT_MAIN
    elif num_dependants == 1:
        monthly_med_credit = MED_CREDIT_MAIN + MED_CREDIT_FIRST_DEP
    else:
        monthly_med_credit = MED_CREDIT_MAIN + MED_CREDIT_FIRST_DEP + (num_dependants - 1) * MED_CREDIT_ADDITIONAL
    annual_med_credit = monthly_med_credit * 12

    # Total tax payable
    annual_tax_payable = max(0.0, round(tax_before_rebate - rebate - annual_med_credit, 2))
    monthly_paye = round(annual_tax_payable / 12, 2)
    net_monthly_salary = round(monthly_salary - monthly_paye, 2)

    dep_desc = "no dependants" if num_dependants == 0 else (f"{num_dependants} dependant" if num_dependants == 1 else f"{num_dependants} dependants")

    prompt = (
        f"{name}, aged **{age} years**, earns a gross monthly salary of **R{monthly_salary:,}**.\n"
        f"{name} belongs to a registered medical aid scheme for themselves and **{dep_desc}**.\n\n"
        f"**Official Tax Information:**\n"
        f"- Primary Rebate (all taxpayers): R{PRIMARY_REBATE:,.0f}\n"
        f"- Secondary Rebate (age 65 and older): R{SECONDARY_REBATE:,.0f}\n"
        f"- Medical Scheme Fees Tax Credit: R{MED_CREDIT_MAIN:,.0f}/month for taxpayer, "
        f"R{MED_CREDIT_FIRST_DEP:,.0f}/month for first dependant, R{MED_CREDIT_ADDITIONAL:,.0f}/month for each additional dependant.\n\n"
        f"Calculate:\n"
        f"1. {name}'s annual gross salary.\n"
        f"2. Total tax before rebates using the SARS tax tables.\n"
        f"3. Total applicable annual tax rebates based on age.\n"
        f"4. Total annual medical scheme fees tax credit.\n"
        f"5. Total annual net income tax payable.\n"
        f"6. Monthly PAYE deduction and net monthly take-home salary."
    ).replace(",", " ")

    sample_answer = (
        f"1. Annual Gross Salary:\n"
        f"   $\\text{{R}}{monthly_salary:,} \\times 12 = \\text{{R}}{annual_salary:,}$\n\n"
        f"2. Tax Before Rebates (Bracket: R{bracket['min']:,} – R{bracket['max']:,}):\n"
        f"   $\\text{{R}}{bracket['base']:,} + ({_fmt_sa(bracket['rate'])} \\times [\\text{{R}}{annual_salary:,} - \\text{{R}}{bracket['over']:,}]) = \\text{{R}}{tax_before_rebate:,.2f}$\n\n"
        f"3. Tax Rebates (Age {age}):\n"
        f"   Primary Rebate: R{PRIMARY_REBATE:,.2f}" + (f" + Secondary Rebate: R{SECONDARY_REBATE:,.2f}" if is_elderly else "") + f" = R{rebate:,.2f}\n\n"
        f"4. Annual Medical Tax Credit ({dep_desc}):\n"
        f"   Monthly credit = R{monthly_med_credit:,.2f}\n"
        f"   Annual credit = $\\text{{R}}{monthly_med_credit:,.2f} \\times 12 = \\text{{R}}{annual_med_credit:,.2f}$\n\n"
        f"5. Annual Net Tax Payable:\n"
        f"   $\\text{{R}}{tax_before_rebate:,.2f} - \\text{{R}}{rebate:,.2f} - \\text{{R}}{annual_med_credit:,.2f} = \\text{{R}}{annual_tax_payable:,.2f}$\n\n"
        f"6. Monthly PAYE and Take-Home:\n"
        f"   Monthly PAYE = $\\text{{R}}{annual_tax_payable:,.2f} \\div 12 = \\text{{R}}{monthly_paye:,.2f}$\n"
        f"   Net Salary = $\\text{{R}}{monthly_salary:,} - \\text{{R}}{monthly_paye:,.2f} = \\text{{R}}{net_monthly_salary:,.2f}$"
    ).replace(",", " ")

    ans_latex = (
        rf"\text{{Annual Tax}} = \text{{R}}{annual_tax_payable:,.2f}, \quad "
        rf"\text{{Monthly PAYE}} = \text{{R}}{monthly_paye:,.2f}, \quad "
        rf"\text{{Net Salary}} = \text{{R}}{net_monthly_salary:,.2f}"
    ).replace(",", " ")

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Annual salary calculation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Tax before rebates calculation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct age rebate applied (Total rebate = R{rebate})", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Annual medical tax credit calculation (R{annual_med_credit})", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Net annual tax payable (R{annual_tax_payable:.2f})", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Monthly PAYE deduction (R{monthly_paye:.2f})", "marks": 1, "editable": True},
            {"id": "mp7", "desc": f"Net monthly take-home salary (R{net_monthly_salary:.2f})", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_primary_rebate", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Multiply monthly salary by 12, locate the tax bracket, then subtract the age rebates and annual medical tax credits.",
        "tier_2": "Annual Tax Payable = Tax Before Rebates - Applicable Rebates - Annual Medical Scheme Fees Tax Credits. Monthly PAYE = Annual Tax / 12.",
        "tier_3": f"Monthly PAYE = R{monthly_paye:,.2f}, Net Salary = R{net_monthly_salary:,.2f}.".replace(",", " "),
    }

    return {
        "id": f"mathlit_tax_comp_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_tax_comp_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_finance_tax",
        "subskill": "income_tax_sars_compound",
        "learning_objective_id": "mathlit_personal_income_tax",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": [
            "omitted_primary_rebate",
            "applied_wrong_age_rebate",
            "taxed_entire_amount_at_marginal_rate",
            "omitted_medical_scheme_credit",
        ],
        "keywords": ["SARS tax", "PAYE", "medical tax credit", "rebates", "personal income tax", "take-home pay"],
        "term": 1,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 12,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_tax,
    "elementary_taxable_income": _build_taxable_income_drill,
    "elementary_tax_bracket_id": _build_tax_bracket_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 10-12 Mathematical Literacy Income Tax questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_tax)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
