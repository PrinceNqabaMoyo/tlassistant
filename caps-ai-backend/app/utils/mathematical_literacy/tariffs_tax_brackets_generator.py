"""Tariffs and SARS Tax Brackets Generator (Grades 10, 11, & 12 Mathematical Literacy).

Complies with the 6-pillar South African CAPS contract:
- Term & calendar metadata
- Deconstructible compound and elementary sub-drills
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention
"""

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Formats a float using South African comma decimal convention."""
    if abs(val - round(val)) < 1e-6:
        return f"{int(round(val)):,}".replace(",", " ")
    s = f"{val:,.{decimals}f}".replace(",", " ").replace(".", ",")
    return s


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    return f"{prefix}_{seed or 'rnd'}_{idx}"


# Authentic South African Personal Income Tax Brackets (CAPS aligned)
SARS_BRACKETS = [
    {"min": 0, "max": 237100, "base": 0, "rate": 0.18, "thresh": 0},
    {"min": 237100, "max": 370500, "base": 42678, "rate": 0.26, "thresh": 237100},
    {"min": 370500, "max": 512800, "base": 77362, "rate": 0.31, "thresh": 370500},
    {"min": 512800, "max": 673000, "base": 121475, "rate": 0.36, "thresh": 512800},
    {"min": 673000, "max": 857900, "base": 179147, "rate": 0.39, "thresh": 673000},
]

PRIMARY_REBATE = 17235
SECONDARY_REBATE = 9444
TERTIARY_REBATE = 3145


def _generate_gr10_stepped_water_tariffs(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 10 Mathematical Literacy: Stepped (block) municipal water tariffs."""
    consumption_kl = r.choice([14, 18, 22, 25, 32, 38])

    # Block rates excl VAT
    # Block 1: 0 - 6 kL @ R0.00 (or R12.50)
    # Block 2: >6 - 15 kL @ R24.50
    # Block 3: >15 - 30 kL @ R36.00
    # Block 4: >30 kL @ R52.00
    r1 = 12.50
    r2 = 24.50
    r3 = 36.00
    r4 = 52.00

    b1_vol = min(6.0, consumption_kl)
    b2_vol = max(0.0, min(9.0, consumption_kl - 6.0))
    b3_vol = max(0.0, min(15.0, consumption_kl - 15.0))
    b4_vol = max(0.0, consumption_kl - 30.0)

    cost_b1 = b1_vol * r1
    cost_b2 = b2_vol * r2
    cost_b3 = b3_vol * r3
    cost_b4 = b4_vol * r4

    subtotal_excl_vat = cost_b1 + cost_b2 + cost_b3 + cost_b4
    vat_amount = subtotal_excl_vat * 0.15
    total_incl_vat = subtotal_excl_vat + vat_amount

    qid = _make_id("ml10_water_tariff", seed, idx)

    if mode == "elementary_block_tariff_step":
        prompt = (
            f"A municipality charges the following stepped tariff for domestic water consumption:\n"
            f"- Block 1 (0 to 6 kL): R{_fmt_sa(r1)} per kL\n"
            f"- Block 2 (>6 to 15 kL): R{_fmt_sa(r2)} per kL\n\n"
            f"A household consumes a total of 10 kL of water in one month.\n"
            f"Calculate the cost for water in **Block 2 only** (excluding VAT)."
        )
        vol_b2_demo = 10 - 6
        cost_b2_demo = vol_b2_demo * r2
        ans_str = f"Cost Block 2 = R{_fmt_sa(cost_b2_demo)}"
        memo = (
            f"Volume in Block 2 [2]: $10\\text{{ kL}} - 6\\text{{ kL}} = 4\\text{{ kL}}$ [1]\n"
            f"Cost for Block 2 [1]: $4\\text{{ kL}} \\times \\text{{R}}{_fmt_sa(r2)} = \\text{{R}}{_fmt_sa(cost_b2_demo)}$ [A]"
        )
        hints = {
            "tier_1": "Only water consumed above 6 kL is charged at the Block 2 rate.",
            "tier_2": f"Subtract 6 kL from 10 kL to get 4 kL. Multiply by R{r2:.2f}.",
            "tier_3": f"4 kL * R{r2:.2f} = R{cost_b2_demo:.2f}.",
        }
        marks = 3
    else:
        # Full compound stepped tariff calculation
        prompt = (
            f"The Table below shows the stepped municipal water tariff rates (excluding 15% VAT) for residential households:\n\n"
            f"| Tariff Block | Consumption Range (kL) | Tariff per kL (excl. VAT) |\n"
            f"| :--- | :--- | :--- |\n"
            f"| **Block 1** | $0 - 6\\text{{ kL}}$ | $\\text{{R}}{_fmt_sa(r1)}$ |\n"
            f"| **Block 2** | $>6 - 15\\text{{ kL}}$ | $\\text{{R}}{_fmt_sa(r2)}$ |\n"
            f"| **Block 3** | $>15 - 30\\text{{ kL}}$ | $\\text{{R}}{_fmt_sa(r3)}$ |\n"
            f"| **Block 4** | $>30\\text{{ kL}}$ | $\\text{{R}}{_fmt_sa(r4)}$ |\n\n"
            f"During March, the Ndlovu family's water meter showed a total consumption of **{consumption_kl} kL**.\n\n"
            f"1. Explain why municipalities implement a stepped (sliding scale) tariff system rather than a flat rate per kilolitre.\n"
            f"2. Calculate the volume of water consumed in each applicable tariff block.\n"
            f"3. Calculate the total cost of the water consumed, excluding VAT.\n"
            f"4. Calculate the 15% VAT amount and the final total invoice amount payable by the Ndlovu family."
        )
        ans_str = (
            f"1. To promote water conservation and make basic water affordable for poorer households; "
            f"2. B1={b1_vol}kL, B2={b2_vol}kL, B3={b3_vol}kL, B4={b4_vol}kL; "
            f"3. Subtotal = R{_fmt_sa(subtotal_excl_vat)}; "
            f"4. VAT = R{_fmt_sa(vat_amount)}, Total = R{_fmt_sa(total_incl_vat)}"
        )
        memo = (
            f"1. Reason for stepped tariff [2]: To encourage conservation of water (scarse natural resource) by penalizing high usage, "
            f"while providing a subsidized/affordable rate for basic essential household water needs. [2]\n"
            f"2. Volume breakdown [3]:\n"
            f"   - Block 1 (0-6 kL): ${_fmt_sa(b1_vol)}\\text{{ kL}}$ [1]\n"
            f"   - Block 2 (6-15 kL): ${_fmt_sa(b2_vol)}\\text{{ kL}}$ [1]\n"
            f"   - Block 3 (15-30 kL): ${_fmt_sa(b3_vol)}\\text{{ kL}}$ [1]\n"
            f"   - Block 4 (>30 kL): ${_fmt_sa(b4_vol)}\\text{{ kL}}$\n"
            f"3. Cost excluding VAT [4]:\n"
            f"   - Block 1: ${_fmt_sa(b1_vol)} \\times \\text{{R}}{_fmt_sa(r1)} = \\text{{R}}{_fmt_sa(cost_b1)}$ [1]\n"
            f"   - Block 2: ${_fmt_sa(b2_vol)} \\times \\text{{R}}{_fmt_sa(r2)} = \\text{{R}}{_fmt_sa(cost_b2)}$ [1]\n"
            f"   - Block 3: ${_fmt_sa(b3_vol)} \\times \\text{{R}}{_fmt_sa(r3)} = \\text{{R}}{_fmt_sa(cost_b3)}$ [1]\n"
            f"   - Block 4: ${_fmt_sa(b4_vol)} \\times \\text{{R}}{_fmt_sa(r4)} = \\text{{R}}{_fmt_sa(cost_b4)}$\n"
            f"   $$\\text{{Total (excl. VAT)}} = \\text{{R}}{_fmt_sa(subtotal_excl_vat)}$$ [M+A]\n"
            f"4. VAT & Total payable [3]:\n"
            f"   $$\\text{{VAT (15\\%)}} = \\text{{R}}{_fmt_sa(subtotal_excl_vat)} \\times 0{{,}}15 = \\text{{R}}{_fmt_sa(vat_amount)}$$ [1]\n"
            f"   $$\\text{{Total Payable}} = \\text{{R}}{_fmt_sa(subtotal_excl_vat)} + \\text{{R}}{_fmt_sa(vat_amount)} = \\text{{R}}{_fmt_sa(total_incl_vat)}$$ [M+A]"
        )
        hints = {
            "tier_1": "Do not multiply the total 22 kL by a single rate! Break the water into the 4 separate blocks.",
            "tier_2": "Calculate: Block 1 cost + Block 2 cost + Block 3 cost. Then add 15% VAT.",
            "tier_3": f"Subtotal = R{subtotal_excl_vat:.2f}. VAT = R{vat_amount:.2f}. Total = R{total_incl_vat:.2f}.",
        }
        marks = 12

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 12,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "block_tariff_calculated_at_single_rate",
            "vat_applied_before_subtotal_calculated",
            "stepped_tier_volume_misallocation",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Socioeconomic rationale for stepped tariff", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Volume allocation across stepped tiers", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Step-by-step tier cost summation", "marks": 4, "editable": True},
                {"id": "mp_4", "desc": "15% VAT and gross total calculation", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "single_flat_rate_used_penalty", "penalty": -3}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr12_sars_income_tax(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 & 12 Mathematical Literacy: Progressive SARS Personal Income Tax."""
    age = r.choice([38, 45, 52, 67, 76])
    bracket = r.choice(SARS_BRACKETS[1:4])  # Brackets 2, 3, or 4
    taxable_income = r.randint(bracket["min"] + 15000, bracket["max"] - 10000)

    # Base tax calculation
    tax_above_thresh = taxable_income - bracket["thresh"]
    marginal_tax = tax_above_thresh * bracket["rate"]
    gross_tax_before_rebates = bracket["base"] + marginal_tax

    # Rebates
    if age < 65:
        rebate = PRIMARY_REBATE
        rebate_desc = f"Primary rebate (R{_fmt_sa(PRIMARY_REBATE)})"
    elif age < 75:
        rebate = PRIMARY_REBATE + SECONDARY_REBATE
        rebate_desc = f"Primary rebate (R{_fmt_sa(PRIMARY_REBATE)}) + Secondary rebate (R{_fmt_sa(SECONDARY_REBATE)})"
    else:
        rebate = PRIMARY_REBATE + SECONDARY_REBATE + TERTIARY_REBATE
        rebate_desc = f"Primary (R{_fmt_sa(PRIMARY_REBATE)}) + Secondary (R{_fmt_sa(SECONDARY_REBATE)}) + Tertiary (R{_fmt_sa(TERTIARY_REBATE)})"

    annual_tax_payable = max(0.0, gross_tax_before_rebates - rebate)
    monthly_paye = annual_tax_payable / 12.0

    qid = _make_id("ml12_sars_tax", seed, idx)

    if mode == "elementary_rebate_deduction":
        prompt = (
            f"A taxpayer aged **{age} years** has a calculated gross annual tax before rebates of **R{_fmt_sa(gross_tax_before_rebates)}**.\n\n"
            f"Using the official SARS tax rebates:\n"
            f"- Primary rebate: R{_fmt_sa(PRIMARY_REBATE)}\n"
            f"- Secondary rebate (65 and older): R{_fmt_sa(SECONDARY_REBATE)}\n"
            f"- Tertiary rebate (75 and older): R{_fmt_sa(TERTIARY_REBATE)}\n\n"
            f"1. Determine the total SARS rebate amount applicable to this taxpayer.\n"
            f"2. Calculate their final annual tax payable after rebates."
        )
        ans_str = f"1. Rebates = R{_fmt_sa(rebate)}; 2. Annual tax = R{_fmt_sa(annual_tax_payable)}"
        memo = (
            f"1. Rebate qualification [2]: Taxpayer is {age} years old $\\to$ Qualifies for {rebate_desc} = $$\\text{{R}}{_fmt_sa(rebate)}$$ [2]\n"
            f"2. Tax after rebate [2]:\n"
            f"   $$\\text{{Tax Payable}} = \\text{{R}}{_fmt_sa(gross_tax_before_rebates)} - \\text{{R}}{_fmt_sa(rebate)} = \\text{{R}}{_fmt_sa(annual_tax_payable)}$$ [M+A]"
        )
        hints = {
            "tier_1": f"Check the taxpayer's age ({age} years) against the 65 and 75 year thresholds.",
            "tier_2": f"Total rebate is R{rebate}. Subtract this directly from the gross tax.",
            "tier_3": f"Rebate = R{rebate}. Net tax = R{gross_tax_before_rebates:.2f} - R{rebate} = R{annual_tax_payable:.2f}.",
        }
        marks = 4
    else:
        # Full compound 12-mark Grade 12 SARS tax question
        tax_table_md = (
            "| Tax Bracket | Taxable Income (R) | Rate of Tax (R) |\n"
            "| :--- | :--- | :--- |\n"
            "| 1 | $1 - 237\\ 100$ | $18\\%$ of taxable income |\n"
            "| 2 | $237\\ 101 - 370\\ 500$ | $42\\ 678 + 26\\%$ of taxable income above $237\\ 100$ |\n"
            "| 3 | $370\\ 501 - 512\\ 800$ | $77\\ 362 + 31\\%$ of taxable income above $370\\ 500$ |\n"
            "| 4 | $512\\ 801 - 673\\ 000$ | $121\\ 475 + 36\\%$ of taxable income above $512\\ 800$ |\n"
            "| 5 | $673\\ 001 - 857\\ 900$ | $179\\ 147 + 39\\%$ of taxable income above $673\\ 000$ |"
        )
        prompt = (
            f"The table below shows the SARS Personal Income Tax rates for a recent tax year:\n\n"
            f"{tax_table_md}\n\n"
            f"**Tax Rebates:**\n"
            f"- Primary rebate (all natural persons): $\\text{{R}}{_fmt_sa(PRIMARY_REBATE)}$\n"
            f"- Secondary rebate (persons 65 and older): $\\text{{R}}{_fmt_sa(SECONDARY_REBATE)}$\n"
            f"- Tertiary rebate (persons 75 and older): $\\text{{R}}{_fmt_sa(TERTIARY_REBATE)}$\n\n"
            f"Mr. Dlamini is **{age} years old** and earns a taxable income of **R{_fmt_sa(taxable_income)}** for the tax year.\n\n"
            f"1. Identify the tax bracket that applies to Mr. Dlamini's taxable income.\n"
            f"2. Calculate his gross annual income tax before rebates are deducted.\n"
            f"3. State the total rebate amount that Mr. Dlamini qualifies for based on his age.\n"
            f"4. Calculate his net annual tax payable.\n"
            f"5. Calculate the monthly PAYE (Pay-As-You-Earn) tax deducted from his salary.\n"
            f"6. A friend told Mr. Dlamini: *'If your salary enters a higher tax bracket, you take home less money because your whole salary gets taxed at the higher percentage.'* Explain why this statement is incorrect using the concept of **marginal tax brackets**."
        )
        ans_str = (
            f"1. Bracket {SARS_BRACKETS.index(bracket)+1}; "
            f"2. Gross tax = R{_fmt_sa(gross_tax_before_rebates)}; "
            f"3. Rebate = R{_fmt_sa(rebate)}; "
            f"4. Net annual tax = R{_fmt_sa(annual_tax_payable)}; "
            f"5. Monthly PAYE = R{_fmt_sa(monthly_paye)}; "
            f"6. Incorrect because only the portion of income that exceeds the bracket threshold is taxed at the higher marginal rate."
        )
        memo = (
            f"1. Tax bracket [1]: Bracket {SARS_BRACKETS.index(bracket)+1} (covers R{_fmt_sa(taxable_income)}). [1]\n"
            f"2. Gross tax calculation [4]:\n"
            f"   $$\\text{{Amount above threshold}} = \\text{{R}}{_fmt_sa(taxable_income)} - \\text{{R}}{_fmt_sa(bracket['thresh'])} = \\text{{R}}{_fmt_sa(tax_above_thresh)}$$ [1]\n"
            f"   $$\\text{{Marginal tax}} = {_fmt_sa(tax_above_thresh)} \\times {_fmt_sa(bracket['rate'] * 100)}\\% = \\text{{R}}{_fmt_sa(marginal_tax)}$$ [1]\n"
            f"   $$\\text{{Gross tax}} = \\text{{R}}{_fmt_sa(bracket['base'])} + \\text{{R}}{_fmt_sa(marginal_tax)} = \\text{{R}}{_fmt_sa(gross_tax_before_rebates)}$$ [M+A]\n"
            f"3. Applicable rebate [2]:\n"
            f"   Age is {age} years $\\implies$ {rebate_desc} = $$\\text{{R}}{_fmt_sa(rebate)}$$ [2]\n"
            f"4. Net annual tax [2]:\n"
            f"   $$\\text{{Net Tax}} = \\text{{R}}{_fmt_sa(gross_tax_before_rebates)} - \\text{{R}}{_fmt_sa(rebate)} = \\text{{R}}{_fmt_sa(annual_tax_payable)}$$ [M+A]\n"
            f"5. Monthly PAYE [2]:\n"
            f"   $$\\text{{Monthly PAYE}} = \\frac{{\\text{{R}}{_fmt_sa(annual_tax_payable)}}}{{12}} = \\text{{R}}{_fmt_sa(monthly_paye)}$$ [M+A]\n"
            f"6. Progressive tax clarification [2]: The statement is FALSE. In South Africa's progressive tax system, only the portion of income exceeding the bracket threshold is taxed at the higher marginal percentage. The income below the threshold remains taxed at the lower previous rates, so take-home pay always increases when gross income increases. [2]"
        )
        hints = {
            "tier_1": f"Identify the bracket for R{taxable_income}. Subtract threshold R{bracket['thresh']}, then multiply by {bracket['rate']*100}%.",
            "tier_2": f"Add base tax R{bracket['base']}. Then check age {age} to subtract correct rebates.",
            "tier_3": f"Gross: R{gross_tax_before_rebates:.2f}. Net after R{rebate} rebate: R{annual_tax_payable:.2f}. Monthly PAYE: R{monthly_paye:.2f}.",
        }
        marks = 13

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 14,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "entire_income_taxed_at_highest_marginal_rate",
            "forgot_sars_rebate_deduction",
            "wrong_age_rebate_bracket_applied",
            "paye_divided_by_10_not_12",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Tax bracket identification", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Base and marginal tax computation", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Age-appropriate rebate identification", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Net annual tax deduction", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": "Monthly PAYE calculation", "marks": 2, "editable": True},
                {"id": "mp_6", "desc": "Marginal tax progressive rate refutation", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "rebate_subtracted_from_taxable_income_not_tax", "penalty": -2}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Tariffs & SARS Tax Brackets (Grades 10, 11, & 12)."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        gr_str = str(grade).strip()
        if gr_str == "10":
            q = _generate_gr10_stepped_water_tariffs(r, seed, i, mode)
        else:
            q = _generate_gr12_sars_income_tax(r, seed, i, mode)
        questions.append(q)

    return questions
