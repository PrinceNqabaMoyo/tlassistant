"""Subskills 9 to 16: SARS Tax Brackets and Marginal Rate Calculations (LB pages 222-227)."""
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


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Tax 09: Bracket identification: Determining which tax bracket applies."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([145000, 185000, 290000, 395000, 520000, 680000])

    bracket_num = 1
    bracket_desc = "Tax Bracket 1 (R 0 to R 160 000)"
    if taxable <= 160000:
        bracket_num = 1
        bracket_desc = "Tax Bracket 1 (R 0 to R 160 000)"
    elif taxable <= 250000:
        bracket_num = 2
        bracket_desc = "Tax Bracket 2 (R 160 001 to R 250 000)"
    elif taxable <= 346000:
        bracket_num = 3
        bracket_desc = "Tax Bracket 3 (R 250 001 to R 346 000)"
    elif taxable <= 484000:
        bracket_num = 4
        bracket_desc = "Tax Bracket 4 (R 346 001 to R 484 000)"
    elif taxable <= 617000:
        bracket_num = 5
        bracket_desc = "Tax Bracket 5 (R 484 001 to R 617 000)"
    else:
        bracket_num = 6
        bracket_desc = "Tax Bracket 6 (R 617 001 and above)"

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(taxable)}.\n\n"
        f"Referring to the SARS Statutory Rates of Tax table:\n"
        f"• Bracket 1: R 0 to R 160 000 (18%)\n"
        f"• Bracket 2: R 160 001 to R 250 000 (R 28 800 + 25% of amount above R 160 000)\n"
        f"• Bracket 3: R 250 001 to R 346 000 (R 51 300 + 30% of amount above R 250 000)\n"
        f"• Bracket 4: R 346 001 to R 484 000 (R 80 100 + 35% of amount above R 346 000)\n"
        f"• Bracket 5: R 484 001 to R 617 000 (R 128 400 + 38% of amount above R 484 000)\n"
        f"• Bracket 6: R 617 001 and above (R 178 940 + 40% of amount above R 617 000)\n\n"
        f"In which tax bracket does {name}'s taxable income fall?"
    )
    correct_ans = bracket_desc
    custom_opts = [
        "Tax Bracket 1 (R 0 to R 160 000)",
        "Tax Bracket 2 (R 160 001 to R 250 000)",
        "Tax Bracket 3 (R 250 001 to R 346 000)",
        "Tax Bracket 4 (R 346 001 to R 484 000)",
        "Tax Bracket 5 (R 484 001 to R 617 000)",
        "Tax Bracket 6 (R 617 001 and above)",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Check interval [1 Mark]: Identify where {_fmt_curr(taxable)} lies.\n"
        f"Step 2: Compare ranges [1 Mark]: It is strictly within {bracket_desc}.\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}."
    )
    t1 = "Locate the given income between the minimum and maximum boundaries of each tax bracket."
    t2 = f"{_fmt_curr(taxable)} falls inside {bracket_desc}."
    t3 = f"The correct bracket is: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_09", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Tax 10: Calculating tax before rebates for Bracket 1 (18%)."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([95000, 115000, 120560, 142000, 155000])

    prompt = (
        f"{name} earns an annual taxable income of {_fmt_curr(taxable)}, which falls in Tax Bracket 1 (R 0 to R 160 000).\n"
        f"The statutory rate of tax for Bracket 1 is: 18% of taxable income.\n\n"
        f"Calculate {name}'s total annual tax BEFORE any rebates are deducted."
    )
    tax = round(taxable * 0.18, 2)
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Tax = 18% × Taxable Income\n"
        f"Step 2: Substitution [1 Mark]: 0,18 × {_fmt_curr(taxable)} = {taxable * 0.18:.2f}\n"
        f"Step 3: Solution [1 Mark]: Tax before rebates = {correct_ans}"
    )
    t1 = "Multiply the taxable income by 18% (or 0,18)."
    t2 = f"{_fmt_curr(taxable)} × 0,18."
    t3 = f"Tax before rebates = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_10", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Tax 11: Calculating tax before rebates for Bracket 2."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([177636, 195000, 210000, 221220, 240000])

    base = 28800.0
    rate = 0.25
    thresh = 160000.0
    excess = taxable - thresh
    tax = round(base + rate * excess, 2)

    prompt = (
        f"{name} earns an annual taxable income of {_fmt_curr(taxable)}, falling into Tax Bracket 2.\n\n"
        f"Statutory formula for Bracket 2 (R 160 001 to R 250 000):\n"
        f"Tax = R 28 800 + 25% of taxable income above R 160 000\n\n"
        f"Calculate {name}'s annual tax BEFORE rebates."
    )
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Amount above threshold [1 Mark]: {_fmt_curr(taxable)} - R 160 000 = {_fmt_curr(excess)}\n"
        f"Step 2: 25% of excess [1 Mark]: 0,25 × {_fmt_curr(excess)} = {_fmt_curr(rate * excess)}\n"
        f"Step 3: Add base tax [1 Mark]: R 28 800 + {_fmt_curr(rate * excess)} = {correct_ans}"
    )
    t1 = "Subtract R 160 000 from the taxable income, multiply by 25%, and add R 28 800."
    t2 = f"Excess = {_fmt_curr(excess)}; 25% = {_fmt_curr(rate * excess)}; Base = R 28 800."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_11", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Tax 12: Calculating tax before rebates for Bracket 3."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([265000, 283756, 305000, 325000, 340000])

    base = 51300.0
    rate = 0.30
    thresh = 250000.0
    excess = taxable - thresh
    tax = round(base + rate * excess, 2)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(taxable)} (Tax Bracket 3).\n\n"
        f"Statutory formula for Bracket 3 (R 250 001 to R 346 000):\n"
        f"Tax = R 51 300 + 30% of taxable income above R 250 000\n\n"
        f"Calculate {name}'s annual tax before rebates."
    )
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Excess amount [1 Mark]: {_fmt_curr(taxable)} - R 250 000 = {_fmt_curr(excess)}\n"
        f"Step 2: Marginal tax [1 Mark]: 0,30 × {_fmt_curr(excess)} = {_fmt_curr(rate * excess)}\n"
        f"Step 3: Add base tax [1 Mark]: R 51 300 + {_fmt_curr(rate * excess)} = {correct_ans}"
    )
    t1 = "Subtract R 250 000, multiply the difference by 30%, and add R 51 300."
    t2 = f"Excess = {_fmt_curr(excess)}; 30% = {_fmt_curr(rate * excess)}."
    t3 = f"Total tax before rebate = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_12", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Tax 13: Calculating tax before rebates for Bracket 4."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([365000, 382729.80, 400000, 435000, 470000])

    base = 80100.0
    rate = 0.35
    thresh = 346000.0
    excess = taxable - thresh
    tax = round(base + rate * excess, 2)

    prompt = (
        f"{name} earns an annual taxable income of {_fmt_curr(taxable)} (Tax Bracket 4).\n\n"
        f"Statutory formula for Bracket 4 (R 346 001 to R 484 000):\n"
        f"Tax = R 80 100 + 35% of taxable income above R 346 000\n\n"
        f"Calculate {name}'s annual tax before rebates."
    )
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Excess [1 Mark]: {_fmt_curr(taxable)} - R 346 000 = {_fmt_curr(excess)}\n"
        f"Step 2: 35% of excess [1 Mark]: 0,35 × {_fmt_curr(excess)} = {_fmt_curr(rate * excess)}\n"
        f"Step 3: Total [1 Mark]: R 80 100 + {_fmt_curr(rate * excess)} = {correct_ans}"
    )
    t1 = "Subtract R 346 000, multiply by 35% (0,35), and add R 80 100."
    t2 = f"Excess = {_fmt_curr(excess)}; 35% of excess = {_fmt_curr(rate * excess)}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_13", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Tax 14: Calculating tax before rebates for Bracket 5."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([510000, 540000, 575000, 605000])

    base = 128400.0
    rate = 0.38
    thresh = 484000.0
    excess = taxable - thresh
    tax = round(base + rate * excess, 2)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(taxable)} (Tax Bracket 5).\n\n"
        f"Statutory formula for Bracket 5 (R 484 001 to R 617 000):\n"
        f"Tax = R 128 400 + 38% of taxable income above R 484 000\n\n"
        f"Calculate {name}'s annual tax before rebates."
    )
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Excess [1 Mark]: {_fmt_curr(taxable)} - R 484 000 = {_fmt_curr(excess)}\n"
        f"Step 2: 38% of excess [1 Mark]: 0,38 × {_fmt_curr(excess)} = {_fmt_curr(rate * excess)}\n"
        f"Step 3: Total [1 Mark]: R 128 400 + {_fmt_curr(rate * excess)} = {correct_ans}"
    )
    t1 = "Subtract R 484 000, multiply by 0,38, and add R 128 400."
    t2 = f"Excess = {_fmt_curr(excess)}; 38% = {_fmt_curr(rate * excess)}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_14", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Tax 15: Calculating tax before rebates for Bracket 6 / Top Bracket."""
    name = r.choice(SA_NAMES)
    taxable = r.choice([680000, 750000, 850000, 950000])

    base = 178940.0
    rate = 0.40
    thresh = 617000.0
    excess = taxable - thresh
    tax = round(base + rate * excess, 2)

    prompt = (
        f"{name} has an annual taxable income of {_fmt_curr(taxable)}, which falls into Tax Bracket 6.\n\n"
        f"Statutory formula for Bracket 6 (R 617 001 and above):\n"
        f"Tax = R 178 940 + 40% of taxable income above R 617 000\n\n"
        f"Calculate {name}'s annual tax before rebates."
    )
    correct_ans = _fmt_curr(tax)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Excess [1 Mark]: {_fmt_curr(taxable)} - R 617 000 = {_fmt_curr(excess)}\n"
        f"Step 2: 40% of excess [1 Mark]: 0,40 × {_fmt_curr(excess)} = {_fmt_curr(rate * excess)}\n"
        f"Step 3: Total [1 Mark]: R 178 940 + {_fmt_curr(rate * excess)} = {correct_ans}"
    )
    t1 = "Subtract R 617 000, multiply by 40% (0,40), and add R 178 940."
    t2 = f"Excess = {_fmt_curr(excess)}; 40% = {_fmt_curr(rate * excess)}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "tax_gr12_15", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Tax 16: Explaining the mathematical meaning of the fixed base amount in bracket formulas."""
    prompt = (
        f"In the SARS tax table, the formula for Bracket 3 (R 250 001 to R 346 000) is:\n"
        f"Tax = R 51 300 + 30% of taxable income above R 250 000.\n\n"
        f"What is the exact mathematical origin and meaning of the fixed amount 'R 51 300'?"
    )
    correct_ans = (
        "It is the exact cumulative tax calculated on all income up to R 250 000 across Brackets 1 and 2 "
        "(18% on first R 160 000 + 25% on next R 90 000)"
    )
    custom_opts = [
        correct_ans,
        "It is the standard primary rebate granted to all individual taxpayers by the Minister of Finance",
        "It is a penalty fee charged by SARS for entering a higher tax bracket",
        "It is the minimum annual contribution required for the Government Employees Pension Fund",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Breakdown of previous brackets [1 Mark]:\n"
        f"  • Bracket 1 tax: 18% × R 160 000 = R 28 800\n"
        f"  • Bracket 2 tax: 25% × (R 250 000 - R 160 000) = 25% × R 90 000 = R 22 500\n"
        f"Step 2: Cumulative sum [1 Mark]: R 28 800 + R 22 500 = R 51 300\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "In a progressive tax system, earlier slices of income are taxed at lower rates."
    t2 = "The fixed base is the sum of maximum taxes payable on all lower brackets."
    t3 = f"Correct explanation: {correct_ans}."

    return _build_question_payload(
        "tax_gr12_16", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )
