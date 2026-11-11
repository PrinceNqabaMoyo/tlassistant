"""Value Added Tax (VAT), UIF & Personal Income Tax Subskills (Subskills 45 to 52).

45. bank_tax_vat_inclusive_calculation_15_percent
46. bank_tax_vat_exclusive_calculation_15_percent
47. bank_tax_vat_amount_from_inclusive_or_exclusive
48. bank_tax_vat_exempt_foodstuffs_till_slip_verification
49. bank_tax_uif_deduction_employee_and_employer
50. bank_tax_sars_income_tax_bracket_calculation
51. bank_tax_sars_primary_secondary_rebate_reduction
52. bank_tax_sars_medical_scheme_fees_tax_credit
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_tax_vat_inclusive_calculation_15_percent(r: random.Random) -> Dict[str, Any]:
    """Calculate the VAT-inclusive price from a VAT-exclusive price using standard 15% VAT."""
    name = r.choice(SA_NAMES)
    item = r.choice(["office printer", "lawnmower", "plumbing repair service", "mechanic service quote", "catering invoice"])
    exclusive_cost = r.choice([400, 650, 850, 1200, 1500, 2400, 3600, 4800])
    vat_amt = round(exclusive_cost * 0.15, 2)
    inclusive_price = round(exclusive_cost * 1.15, 2)
    ans_str = _fmt_curr(inclusive_price)

    prompt = (
        f"{name} receives a quotation for a {item} with an amount of {_fmt_curr(exclusive_cost)} **excluding 15% VAT**.\n\n"
        f"Calculate the **total price including 15% VAT**.\n"
        f"Use the formula: $$\\text{{VAT Inclusive Price}} = \\text{{VAT Exclusive Price}} \\times 1,15$$"
    )
    sol = (
        f"Step 1: Understand VAT-inclusive pricing:\n"
        f"• VAT rate in South Africa = 15%\n"
        f"• VAT Inclusive = 100% (cost) + 15% (tax) = 115% = 1,15 × Exclusive cost\n\n"
        f"Step 2: Method setup – multiply exclusive amount by 1,15:\n"
        f"• VAT Inclusive = {_fmt_curr(exclusive_cost)} × 1,15 "
        f"✓ [1 Mark: Method – multiplying VAT-exclusive amount by 1,15 (or calculating 15% and adding)]\n\n"
        f"Step 3: Calculate final price:\n"
        f"VAT Inclusive = {ans_str} ✓ [1 Mark: Accuracy – correct VAT inclusive amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(exclusive_cost)} by 1,15 (or adding 15% VAT {_fmt_curr(vat_amt)})",
        f"1 Mark: Accuracy – correct price {ans_str}"
    ]
    hints = {
        "tier_1": f"Either calculate 15% of {_fmt_curr(exclusive_cost)} and add it, or multiply by 1,15 directly.",
        "tier_2": f"Calculate: {exclusive_cost} × 1,15.",
        "tier_3": f"{exclusive_cost} × 1,15 = {inclusive_price:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_vat_inclusive_calculation_15_percent", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_vat_exclusive_calculation_15_percent(r: random.Random) -> Dict[str, Any]:
    """Calculate the VAT-exclusive price from a VAT-inclusive price (reversing 15% VAT)."""
    name = r.choice(SA_NAMES)
    item = r.choice(["smart television", "laptop computer", "microwave oven", "bicycle", "tool kit"])
    exclusive_base = r.choice([500, 800, 1000, 1200, 1600, 2000, 2500, 3200])
    inclusive_price = round(exclusive_base * 1.15, 2)
    ans_str = _fmt_curr(exclusive_base)

    prompt = (
        f"{name} purchases a {item} for {_fmt_curr(inclusive_price)} **including 15% VAT**.\n\n"
        f"Calculate the price of the {item} **EXCLUDING VAT**.\n"
        f"Use the formula: $$\\text{{VAT Exclusive Price}} = \\text{{VAT Inclusive Price}} \\div 1,15$$"
    )
    sol = (
        f"Step 1: Understand reverse VAT concept:\n"
        f"• The inclusive price represents 115% of the original cost:\n"
        f"  $$\\text{{Inclusive Price}} = \\text{{Exclusive Price}} \\times 1,15$$\n"
        f"• Common error to avoid: Never subtract 15% of the inclusive price!\n\n"
        f"Step 2: Method setup – divide by 1,15:\n"
        f"• VAT Exclusive = {_fmt_curr(inclusive_price)} ÷ 1,15 "
        f"✓ [1 Mark: Method – dividing VAT-inclusive amount by 1,15]\n\n"
        f"Step 3: Calculate exclusive price:\n"
        f"VAT Exclusive = {ans_str} ✓ [1 Mark: Accuracy – correct pre-VAT cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – dividing {_fmt_curr(inclusive_price)} by 1,15",
        f"1 Mark: Accuracy – correct exclusive price {ans_str}"
    ]
    hints = {
        "tier_1": "Divide the inclusive price by 1,15 (do not multiply by 0,85).",
        "tier_2": f"Calculate: {inclusive_price:.2f} ÷ 1,15.",
        "tier_3": f"{inclusive_price:.2f} ÷ 1,15 = {exclusive_base:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_vat_exclusive_calculation_15_percent", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_vat_amount_from_inclusive_or_exclusive(r: random.Random) -> Dict[str, Any]:
    """Calculate only the VAT amount from a VAT-inclusive purchase price."""
    name = r.choice(SA_NAMES)
    item = r.choice(["refrigerator", "washing machine", "sound bar", "generator", "dining table"])
    exclusive_base = r.choice([2000, 3000, 4000, 5000, 6000, 8000])
    inclusive_price = round(exclusive_base * 1.15, 2)
    vat_amt = round(inclusive_price - exclusive_base, 2)
    ans_str = _fmt_curr(vat_amt)

    prompt = (
        f"{name} pays {_fmt_curr(inclusive_price)} (including 15% VAT) for a new {item}.\n\n"
        f"Calculate **how much VAT (in Rands)** was paid on this purchase.\n"
        f"Use the formula: $$\\text{{VAT Amount}} = \\text{{VAT Inclusive Price}} - (\\text{{VAT Inclusive Price}} \\div 1,15)$$"
    )
    sol = (
        f"Step 1: Calculate the VAT-exclusive price:\n"
        f"• Exclusive Price = {_fmt_curr(inclusive_price)} ÷ 1,15 = {_fmt_curr(exclusive_base)}\n\n"
        f"Step 2: Method setup – subtract exclusive price from inclusive price:\n"
        f"• VAT Amount = Inclusive Price - Exclusive Price\n"
        f"• VAT Amount = {_fmt_curr(inclusive_price)} - {_fmt_curr(exclusive_base)} "
        f"✓ [1 Mark: Method – determining pre-VAT base and subtracting from inclusive price]\n\n"
        f"Step 3: Calculate VAT amount:\n"
        f"VAT Amount = {ans_str} ✓ [1 Mark: Accuracy – correct VAT amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – dividing by 1,15 and subtracting from {_fmt_curr(inclusive_price)}",
        f"1 Mark: Accuracy – correct VAT portion {ans_str}"
    ]
    hints = {
        "tier_1": f"First find the price excluding VAT: {_fmt_curr(inclusive_price)} ÷ 1,15.",
        "tier_2": f"Subtract that exclusive price ({_fmt_curr(exclusive_base)}) from the inclusive price ({_fmt_curr(inclusive_price)}).",
        "tier_3": f"{inclusive_price:.2f} - {exclusive_base:.2f} = {vat_amt:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_vat_amount_from_inclusive_or_exclusive", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_vat_exempt_foodstuffs_till_slip_verification(r: random.Random) -> Dict[str, Any]:
    """Analyze a grocery till slip containing VAT-exempt basic foodstuffs (marked with *) and verify VAT calculation."""
    name = r.choice(SA_NAMES)
    bread_price = round(r.choice([14.99, 16.50, 17.99]), 2)
    milk_price = round(r.choice([16.99, 18.50, 19.99]), 2)
    chips_price = round(r.choice([8.99, 11.50, 12.99]), 2)  # Taxable
    soap_price = round(r.choice([14.50, 18.00, 22.50]), 2)   # Taxable

    # Exempt: brown bread, fresh milk
    exempt_total = round(bread_price + milk_price, 2)
    taxable_excl = round(chips_price + soap_price, 2)
    vat_15 = round(taxable_excl * 0.15, 2)
    total_due = round(exempt_total + taxable_excl + vat_15, 2)
    ans_str = _fmt_curr(vat_15)

    prompt = (
        f"{name} checks a supermarket cash register till slip:\n\n"
        f"| Item | Price | Tax Status |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Brown bread loaf | {_fmt_curr(bread_price)} | Zero-rated / Exempt (*) |\n"
        f"| Fresh full cream milk 1L | {_fmt_curr(milk_price)} | Zero-rated / Exempt (*) |\n"
        f"| Potato chips 125g | {_fmt_curr(chips_price)} | Standard 15% VAT |\n"
        f"| Laundry soap bar | {_fmt_curr(soap_price)} | Standard 15% VAT |\n\n"
        f"Items marked with an asterisk (*) are zero-rated basic foodstuffs exempt from VAT.\n"
        f"Calculate the **correct 15% VAT amount** that must be charged on this purchase."
    )
    sol = (
        f"Step 1: Distinguish between VAT-exempt items and taxable items:\n"
        f"• Exempt items (*): Brown bread ({_fmt_curr(bread_price)}) + Milk ({_fmt_curr(milk_price)}) = {_fmt_curr(exempt_total)} (0% VAT)\n"
        f"• Standard VAT items: Chips ({_fmt_curr(chips_price)}) + Soap ({_fmt_curr(soap_price)}) = {_fmt_curr(taxable_excl)}\n\n"
        f"Step 2: Method setup – calculate 15% VAT on taxable items only:\n"
        f"• VAT = 15% of {_fmt_curr(taxable_excl)} = 0,15 × {taxable_excl}\n"
        f"✓ [1 Mark: Method – excluding zero-rated foods and applying 15% only to taxable items]\n\n"
        f"Step 3: Calculate VAT amount:\n"
        f"VAT = {ans_str} ✓ [1 Mark: Accuracy – correct VAT charge in Rands]"
    )
    rubric = [
        f"1 Mark: Method – summing taxable items ({_fmt_curr(taxable_excl)}) and multiplying by 15%",
        f"1 Mark: Accuracy – correct VAT {ans_str}"
    ]
    hints = {
        "tier_1": "Do NOT calculate VAT on the brown bread or fresh milk; they are basic foodstuffs exempt from VAT.",
        "tier_2": f"Add only the chips and soap: {_fmt_curr(chips_price)} + {_fmt_curr(soap_price)} = {_fmt_curr(taxable_excl)}.",
        "tier_3": f"Calculate 15% of {_fmt_curr(taxable_excl)}: {taxable_excl} × 0,15 = {vat_15:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_vat_exempt_foodstuffs_till_slip_verification", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_uif_deduction_employee_and_employer(r: random.Random) -> Dict[str, Any]:
    """Calculate employee and employer UIF contributions (1% employee, 1% employer, with statutory cap)."""
    name = r.choice(SA_NAMES)
    gross_salary = r.choice([6500, 8500, 11000, 13500, 16000, 20000])

    # In South Africa, UIF is 1% of remuneration, capped at monthly threshold of R 17 712 (max deduction R 177.12)
    uif_cap_salary = 17712.00
    uif_max_deduction = 177.12

    if gross_salary <= uif_cap_salary:
        employee_uif = round(gross_salary * 0.01, 2)
        total_uif_contribution = round(employee_uif * 2, 2)
        rule_text = f"1% of {_fmt_curr(gross_salary)} = {_fmt_curr(employee_uif)}"
    else:
        employee_uif = uif_max_deduction
        total_uif_contribution = round(uif_max_deduction * 2, 2)
        rule_text = f"The salary exceeds the R 17 712,00 cap, so the statutory maximum of {_fmt_curr(uif_max_deduction)} applies"

    ans_str = _fmt_curr(employee_uif)

    prompt = (
        f"{name} earns a gross monthly salary of {_fmt_curr(gross_salary)}.\n"
        f"Under South African labour legislation, the Unemployment Insurance Fund (UIF) deduction "
        f"is **1% of gross earnings**, up to a maximum salary threshold of R 17 712,00 per month "
        f"(maximum deduction of R 177,12 per month).\n\n"
        f"Calculate the **monthly UIF deduction** from {name}'s salary."
    )
    sol = (
        f"Step 1: Check if the salary exceeds the statutory UIF threshold (R 17 712,00):\n"
        f"• Gross salary = {_fmt_curr(gross_salary)}\n"
        f"• {rule_text}\n\n"
        f"Step 2: Method setup – calculate 1% employee contribution:\n"
        f"• Employee UIF = 1% × (Gross Salary or Cap) "
        f"✓ [1 Mark: Method – applying 1% UIF deduction rule with statutory cap check]\n\n"
        f"Step 3: Final deduction amount:\n"
        f"UIF Deduction = {ans_str} ✓ [1 Mark: Accuracy – correct UIF deduction in Rands]"
    )
    rubric = [
        f"1 Mark: Method – applying 1% UIF formula (subject to R 177,12 statutory cap)",
        f"1 Mark: Accuracy – correct UIF {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate 1% of {_fmt_curr(gross_salary)} by dividing by 100.",
        "tier_2": "Remember that if 1% of the salary exceeds R 177,12, the deduction is capped at R 177,12.",
        "tier_3": f"For a salary of {_fmt_curr(gross_salary)}, the UIF deduction is {ans_str}."
    }
    return _make_q("bank_tax_uif_deduction_employee_and_employer", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_sars_income_tax_bracket_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate gross annual personal income tax from a simplified SARS tax bracket."""
    name = r.choice(SA_NAMES)
    # Using authentic SARS Bracket 2: R 237 100 to R 370 500: Tax is R 42 678 + 26% of taxable income above R 237 100
    base_tax = 42678.00
    threshold = 237100.00
    marginal_rate = 26.0

    taxable_income = r.choice([250000, 275000, 290000, 310000, 335000, 360000])
    above_threshold = taxable_income - threshold
    marginal_tax = round(above_threshold * (marginal_rate / 100), 2)
    total_tax = round(base_tax + marginal_tax, 2)
    ans_str = _fmt_curr(total_tax)

    prompt = (
        f"{name} earns a taxable annual income of {_fmt_curr(taxable_income)}.\n"
        f"According to the SARS personal income tax brackets, {name} falls in the following tax bracket:\n\n"
        f"| Taxable Income | Rates of Tax |\n"
        f"| :--- | :--- |\n"
        f"| R 237 101 – R 370 500 | **R 42 678 + 26% of taxable income above R 237 100** |\n\n"
        f"Calculate {name}'s **gross annual income tax payable** (before rebates)."
    )
    sol = (
        f"Step 1: Identify bracket parameters and calculate excess above threshold:\n"
        f"• Taxable income = {_fmt_curr(taxable_income)}\n"
        f"• Base threshold = {_fmt_curr(threshold)}\n"
        f"• Amount above threshold = {_fmt_curr(taxable_income)} - {_fmt_curr(threshold)} = {_fmt_curr(above_threshold)}\n\n"
        f"Step 2: Method setup – calculate 26% marginal tax on excess and add base tax:\n"
        f"• Marginal tax = 26% of {_fmt_curr(above_threshold)} = ({marginal_rate} ÷ 100) × {above_threshold} = {_fmt_curr(marginal_tax)}\n"
        f"• Gross Tax = Base Tax + Marginal Tax = {_fmt_curr(base_tax)} + {_fmt_curr(marginal_tax)} "
        f"✓ [1 Mark: Method – applying SARS bracket formula: Base Tax + 26% × (Income - Threshold)]\n\n"
        f"Step 3: Calculate gross annual tax:\n"
        f"Gross Tax = {ans_str} ✓ [1 Mark: Accuracy – correct gross tax in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {_fmt_curr(base_tax)} + (26% × ({taxable_income} - {threshold}))",
        f"1 Mark: Accuracy – correct gross tax {ans_str}"
    ]
    hints = {
        "tier_1": f"First find how much {name}'s income exceeds {_fmt_curr(threshold)}: {taxable_income} - {threshold}.",
        "tier_2": f"Find 26% of that excess, then add the fixed base tax of {_fmt_curr(base_tax)}.",
        "tier_3": f"{base_tax} + (0,26 × {above_threshold}) = {total_tax:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_sars_income_tax_bracket_calculation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_sars_primary_secondary_rebate_reduction(r: random.Random) -> Dict[str, Any]:
    """Apply SARS annual primary tax rebate to reduce gross tax to net tax payable."""
    name = r.choice(SA_NAMES)
    gross_tax = r.choice([32500, 38000, 42000, 48500, 54000])
    primary_rebate = 17235.00  # SARS standard primary tax rebate for under 65

    net_tax = round(gross_tax - primary_rebate, 2)
    ans_str = _fmt_curr(net_tax)

    prompt = (
        f"{name} is 34 years old and has calculated a gross annual income tax of {_fmt_curr(gross_tax)} from the SARS tax tables.\n"
        f"SARS allows the following annual personal tax rebates:\n"
        f"• **Primary Rebate (all natural persons under 65)**: {_fmt_curr(primary_rebate)}\n"
        f"• **Secondary Rebate (persons 65 and older)**: R 9 444,00\n\n"
        f"Calculate {name}'s **net annual income tax payable** after applying the eligible rebate."
    )
    sol = (
        f"Step 1: Identify eligible rebate based on taxpayer's age:\n"
        f"• {name} is 34 years old (< 65 years), so only the **Primary Rebate** of {_fmt_curr(primary_rebate)} applies.\n\n"
        f"Step 2: Method setup – subtract rebate from gross tax liability:\n"
        f"• Net Tax = Gross Tax - Primary Rebate\n"
        f"• Net Tax = {_fmt_curr(gross_tax)} - {_fmt_curr(primary_rebate)} "
        f"✓ [1 Mark: Method – subtracting primary tax rebate from gross annual tax]\n\n"
        f"Step 3: Calculate net tax payable:\n"
        f"Net Tax = {ans_str} ✓ [1 Mark: Accuracy – correct net tax in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting primary rebate {_fmt_curr(primary_rebate)} from gross tax {_fmt_curr(gross_tax)}",
        f"1 Mark: Accuracy – correct net tax {ans_str}"
    ]
    hints = {
        "tier_1": f"Since {name} is under 65, subtract the Primary Rebate ({_fmt_curr(primary_rebate)}) from the gross tax.",
        "tier_2": f"Calculate: {gross_tax:.2f} - {primary_rebate:.2f}.",
        "tier_3": f"{gross_tax:.2f} - {primary_rebate:.2f} = {net_tax:.2f}, giving {ans_str}."
    }
    return _make_q("bank_tax_sars_primary_secondary_rebate_reduction", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_tax_sars_medical_scheme_fees_tax_credit(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly medical scheme fees tax credit for principal member and dependents."""
    name = r.choice(SA_NAMES)
    num_dependents = r.choice([1, 2, 3])

    # SARS Medical Scheme Fees Tax Credit rates (monthly):
    # Main member: R364/month
    # First dependent: R364/month
    # Each additional dependent: R246/month
    main_member_credit = 364.00
    first_dep_credit = 364.00
    add_dep_credit = 246.00

    if num_dependents == 1:
        total_credit = main_member_credit + first_dep_credit
        dep_desc = "1 dependent (spouse)"
    elif num_dependents == 2:
        total_credit = main_member_credit + first_dep_credit + add_dep_credit
        dep_desc = "2 dependents (spouse and 1 child)"
    else:
        total_credit = main_member_credit + first_dep_credit + (2 * add_dep_credit)
        dep_desc = "3 dependents (spouse and 2 children)"

    total_credit = round(total_credit, 2)
    ans_str = _fmt_curr(total_credit)

    prompt = (
        f"{name} pays monthly medical aid contributions for {name} and {dep_desc}.\n"
        f"SARS grants a monthly Medical Scheme Fees Tax Credit to reduce personal income tax:\n"
        f"• Main member: {_fmt_curr(main_member_credit)} per month\n"
        f"• First dependent: {_fmt_curr(first_dep_credit)} per month\n"
        f"• Each additional dependent: {_fmt_curr(add_dep_credit)} per month\n\n"
        f"Calculate the **total monthly medical tax credit** {name} is entitled to receive."
    )
    sol = (
        f"Step 1: Identify eligible credit for each family member:\n"
        f"• Main member: {_fmt_curr(main_member_credit)}\n"
        f"• First dependent: {_fmt_curr(first_dep_credit)}\n"
        f"{f'• Additional dependents: {num_dependents - 1} × ' + _fmt_curr(add_dep_credit) if num_dependents > 1 else ''}\n\n"
        f"Step 2: Method setup – sum all medical tax credits:\n"
        f"• Total Monthly Credit = Main Member Credit + Dependents Credits "
        f"✓ [1 Mark: Method – applying SARS medical scheme tax credit schedule for {1 + num_dependents} beneficiaries]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Credit = {ans_str} ✓ [1 Mark: Accuracy – correct monthly medical tax credit in Rands]"
    )
    rubric = [
        f"1 Mark: Method – summing applicable SARS medical tax credits for {1 + num_dependents} members",
        f"1 Mark: Accuracy – correct credit {ans_str}"
    ]
    hints = {
        "tier_1": f"Add the credit for the main member ({_fmt_curr(main_member_credit)}) and the first dependent ({_fmt_curr(first_dep_credit)}).",
        "tier_2": f"If there are additional dependents, add {_fmt_curr(add_dep_credit)} for each.",
        "tier_3": f"The total monthly medical tax credit is {ans_str}."
    }
    return _make_q("bank_tax_sars_medical_scheme_fees_tax_credit", prompt, ans_str, sol, rubric, hints, 2, r=r)
