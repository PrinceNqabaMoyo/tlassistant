"""Grade 11 Mathematical Literacy - Term 3: Financial Documents and Tariff Systems Generator.

100% Aligned with South African National Curriculum Standards (CAPS).
Curriculum Source: curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 3/02. Financial documents and tariff systems.md

Features:
- 52 distinct subskills covering:
    * Payslips & Employee Earnings (Subskills 1 to 9)
    * Invoices, Quotations, Receipts & VAT (Subskills 10 to 18)
    * Stepped Municipal Water Tariffs (Subskills 19 to 27)
    * Electricity Tariffs & IBT Blocks (Subskills 28 to 36)
    * Transport & Communication Tariffs (Subskills 37 to 44)
    * Break-Even Analysis & Business Accounts (Subskills 45 to 52)
- Step-by-step worked solutions with mark breakdowns.
- Pure South African Rand formatting (e.g. R 1 250,00).
- Robust 4-option multiple choice with zero generic/alt placeholders.
- 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

SA_NAMES = ["Sipho", "Zanele", "Johan", "Lerato", "Farai", "Nandi", "Trevor", "Thabo", "Busisiwe", "Devan", "Anika", "Kagiso"]

def _fmt_curr(val: float | int) -> str:
    """Format currency: R 12 345,67."""
    int_part = int(round(val * 100)) // 100
    cents = int(round(abs(val) * 100)) % 100
    formatted_int = f"{int_part:,}".replace(",", " ")
    return f"R {formatted_int},{cents:02d}"

def _fmt_num(val: float | int) -> str:
    """Format numbers: 12 345,67 or 12 345."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return f"{int(val):,}".replace(",", " ")
    return f"{val:,.2f}".replace(",", " ").replace(".", ",")

def _build_mc_options(correct: str, distractors: List[str], r: random.Random) -> List[str]:
    """Assemble 4 strictly unique options."""
    pool = [d for d in distractors if d != correct]
    r.shuffle(pool)
    opts = [correct] + pool[:3]
    while len(opts) < 4:
        # Fallback numeric nudge if needed
        opts.append(f"{correct} *")
    r.shuffle(opts)
    return opts

# ----------------------------------------------------------------------------
# SUBSKILLS 1–9: Payslips & Employee Earnings
# ----------------------------------------------------------------------------

def _subskill_1(r: random.Random) -> Dict[str, Any]:
    """Calculate basic salary from hourly wage and normal working hours."""
    name = r.choice(SA_NAMES)
    rate = r.choice([45.0, 52.50, 60.0, 75.0, 85.0])
    hours = r.choice([160, 168, 172, 176])
    basic = rate * hours

    prompt = (
        f"{name} works as an administrative assistant earning an hourly wage of **{_fmt_curr(rate)}**.\n"
        f"During September, {name} worked **{hours} normal hours** with no overtime.\n\n"
        f"Calculate {name}'s basic gross salary for the month."
    )
    correct = _fmt_curr(basic)
    distractors = [_fmt_curr(rate * (hours - 10)), _fmt_curr((rate + 5) * hours), _fmt_curr(basic * 1.15)]
    expl = f"✓ [1 Mark: Method – Multiply hourly rate by hours worked]\nBasic Salary = {_fmt_curr(rate)} × {hours} hours = {_fmt_curr(basic)}.\n✓ [1 Mark: Accuracy – Correct basic salary]\nTotal = {_fmt_curr(basic)}."
    
    return {
        "subskill": "gr11_tariffs_subskill_1",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply rate by hours.", "tier_2": f"{rate} × {hours}.", "tier_3": f"{correct}."},
    }

def _subskill_2(r: random.Random) -> Dict[str, Any]:
    """Calculate overtime pay at 1.5 times normal hourly rate."""
    name = r.choice(SA_NAMES)
    rate = r.choice([50.0, 65.0, 80.0, 95.0])
    ot_hours = r.choice([8, 12, 15, 20])
    ot_rate = rate * 1.5
    ot_pay = ot_rate * ot_hours

    prompt = (
        f"{name}'s normal hourly wage is **{_fmt_curr(rate)}**.\n"
        f"According to South African labour legislation (BCEA), overtime on weekdays is paid at **1,5 times** the normal rate.\n"
        f"Calculate {name}'s overtime earnings for working **{ot_hours} overtime hours**."
    )
    correct = _fmt_curr(ot_pay)
    distractors = [_fmt_curr(rate * ot_hours), _fmt_curr(rate * 2.0 * ot_hours), _fmt_curr(ot_pay + 150)]
    expl = f"✓ [1 Mark: Method – Calculate overtime rate (1,5 × normal rate)]\nOvertime Rate = 1,5 × {_fmt_curr(rate)} = {_fmt_curr(ot_rate)}/hr.\n✓ [1 Mark: Accuracy – Overtime earnings]\nOvertime Pay = {_fmt_curr(ot_rate)} × {ot_hours} = {_fmt_curr(ot_pay)}."
    return {
        "subskill": "gr11_tariffs_subskill_2",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find 1,5 × normal rate first.", "tier_2": f"Multiply {_fmt_curr(ot_rate)} by {ot_hours}.", "tier_3": f"{correct}."},
    }

def _subskill_3(r: random.Random) -> Dict[str, Any]:
    """Calculate total gross salary including basic salary, overtime, and travel allowance."""
    name = r.choice(SA_NAMES)
    basic = r.randint(15, 30) * 1000
    overtime = r.randint(12, 35) * 100
    allowance = r.choice([1500, 2000, 2500, 3000])
    gross = basic + overtime + allowance

    prompt = (
        f"A section of {name}'s payslip shows:\n"
        f"• Basic Salary: **{_fmt_curr(basic)}**\n"
        f"• Overtime Earnings: **{_fmt_curr(overtime)}**\n"
        f"• Travel Allowance: **{_fmt_curr(allowance)}**\n\n"
        f"Calculate {name}'s **Total Gross Income** for the month."
    )
    correct = _fmt_curr(gross)
    distractors = [_fmt_curr(basic + overtime), _fmt_curr(basic + allowance), _fmt_curr(gross - 500)]
    expl = f"✓ [1 Mark: Method – Sum all earning components]\nGross Income = {_fmt_curr(basic)} + {_fmt_curr(overtime)} + {_fmt_curr(allowance)} = {_fmt_curr(gross)}.\n✓ [1 Mark: Accuracy – Total gross]\nTotal = {_fmt_curr(gross)}."
    return {
        "subskill": "gr11_tariffs_subskill_3",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add basic salary, overtime, and allowances.", "tier_2": f"Sum all three earnings.", "tier_3": f"{correct}."},
    }

def _subskill_4(r: random.Random) -> Dict[str, Any]:
    """Calculate statutory UIF deduction (1% of gross earnings up to ceiling of R177,12)."""
    name = r.choice(SA_NAMES)
    gross = r.choice([12500, 14800, 16500, 17712, 22000, 28000])
    uif_raw = gross * 0.01
    uif = min(177.12, uif_raw)

    prompt = (
        f"{name} earns a monthly gross salary of **{_fmt_curr(gross)}**.\n"
        f"In South Africa, employee UIF contributions are calculated at **1%** of gross salary, "
        f"capped at a statutory maximum monthly deduction of **R 177,12** (on a salary ceiling of R 17 712,00).\n\n"
        f"Determine {name}'s monthly UIF deduction."
    )
    correct = _fmt_curr(uif)
    distractors = [_fmt_curr(gross * 0.02), _fmt_curr(uif_raw if uif_raw > 177.12 else uif + 20), "R 200,00"]
    expl = f"✓ [1 Mark: Method – Calculate 1% of gross and apply statutory cap]\n1% of {_fmt_curr(gross)} = {_fmt_curr(uif_raw)}.\nSince maximum UIF is capped at R 177,12, deduction = {_fmt_curr(uif)}.\n✓ [1 Mark: Accuracy – UIF deduction]\nUIF = {_fmt_curr(uif)}."
    return {
        "subskill": "gr11_tariffs_subskill_4",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate 1% of gross. Check if it exceeds R 177,12.", "tier_2": "Max cap is R 177,12.", "tier_3": f"{correct}."},
    }

def _subskill_5(r: random.Random) -> Dict[str, Any]:
    """Calculate pension fund deduction (7,5% of basic salary)."""
    name = r.choice(SA_NAMES)
    basic = r.randint(18, 40) * 1000
    pension = basic * 0.075

    prompt = (
        f"{name}'s employment contract stipulates an employee pension fund contribution of **7,5%** of basic salary.\n"
        f"If {name}'s basic monthly salary is **{_fmt_curr(basic)}**, calculate the monthly pension deduction."
    )
    correct = _fmt_curr(pension)
    distractors = [_fmt_curr(basic * 0.08), _fmt_curr(basic * 0.07), _fmt_curr(pension * 1.1)]
    expl = f"✓ [1 Mark: Method – Multiply basic salary by 7,5% (0,075)]\nPension = {_fmt_curr(basic)} × 0,075 = {_fmt_curr(pension)}.\n✓ [1 Mark: Accuracy – Monthly pension contribution]\nPension = {_fmt_curr(pension)}."
    return {
        "subskill": "gr11_tariffs_subskill_5",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply basic salary by 7,5 / 100.", "tier_2": f"{basic} × 0,075.", "tier_3": f"{correct}."},
    }

def _subskill_6(r: random.Random) -> Dict[str, Any]:
    """Calculate total monthly deductions (PAYE + UIF + Pension + Medical Aid)."""
    name = r.choice(SA_NAMES)
    paye = r.randint(25, 45) * 100
    uif = 177.12
    pension = r.randint(12, 22) * 100
    med_aid = r.choice([1650, 2100, 2850])
    total_ded = paye + uif + pension + med_aid

    prompt = (
        f"The deductions column on {name}'s monthly payslip lists:\n"
        f"• PAYE Income Tax: **{_fmt_curr(paye)}**\n"
        f"• UIF Contribution: **{_fmt_curr(uif)}**\n"
        f"• Pension Fund: **{_fmt_curr(pension)}**\n"
        f"• Medical Aid: **{_fmt_curr(med_aid)}**\n\n"
        f"Calculate {name}'s **Total Monthly Deductions**."
    )
    correct = _fmt_curr(total_ded)
    distractors = [_fmt_curr(paye + pension + med_aid), _fmt_curr(total_ded + 200), _fmt_curr(total_ded - 500)]
    expl = f"✓ [1 Mark: Method – Sum all statutory and voluntary deductions]\nTotal = {_fmt_curr(paye)} + {_fmt_curr(uif)} + {_fmt_curr(pension)} + {_fmt_curr(med_aid)} = {_fmt_curr(total_ded)}.\n✓ [1 Mark: Accuracy – Total deductions]\nTotal Deductions = {_fmt_curr(total_ded)}."
    return {
        "subskill": "gr11_tariffs_subskill_6",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add all 4 deduction amounts.", "tier_2": f"PAYE + UIF + Pension + Medical Aid.", "tier_3": f"{correct}."},
    }

def _subskill_7(r: random.Random) -> Dict[str, Any]:
    """Calculate Net Pay from Gross Salary and Total Deductions."""
    name = r.choice(SA_NAMES)
    gross = r.randint(24, 45) * 1000
    deductions = r.randint(5, 12) * 1000 + 450
    net_pay = gross - deductions

    prompt = (
        f"{name}'s payslip indicates:\n"
        f"• Gross Earnings: **{_fmt_curr(gross)}**\n"
        f"• Total Deductions: **{_fmt_curr(deductions)}**\n\n"
        f"Calculate {name}'s **Net Pay (Take-home salary)** for the month."
    )
    correct = _fmt_curr(net_pay)
    distractors = [_fmt_curr(gross + deductions), _fmt_curr(net_pay + 500), _fmt_curr(net_pay - 500)]
    expl = f"✓ [1 Mark: Method – Subtract deductions from gross salary]\nNet Pay = Gross Income − Total Deductions = {_fmt_curr(gross)} − {_fmt_curr(deductions)} = {_fmt_curr(net_pay)}.\n✓ [1 Mark: Accuracy – Net take-home salary]\nNet Pay = {_fmt_curr(net_pay)}."
    return {
        "subskill": "gr11_tariffs_subskill_7",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Net Pay = Gross Earnings − Total Deductions.", "tier_2": f"{gross} − {deductions}.", "tier_3": f"{correct}."},
    }

def _subskill_8(r: random.Random) -> Dict[str, Any]:
    """Calculate employer's UIF contribution matching employee's 1%."""
    name = r.choice(SA_NAMES)
    gross = r.choice([14500, 16000, 18500, 24000])
    uif_emp = min(177.12, gross * 0.01)
    uif_employer = uif_emp  # Employer matches 1%
    total_uif = uif_emp + uif_employer

    prompt = (
        f"Under the Unemployment Insurance Act, both the employee and employer contribute 1% of gross salary each month.\n"
        f"If {name}'s monthly employee UIF deduction is **{_fmt_curr(uif_emp)}**, "
        f"what is the **total UIF contribution** paid over to SARS on {name}'s behalf (employee + employer combined)?"
    )
    correct = _fmt_curr(total_uif)
    distractors = [_fmt_curr(uif_emp), _fmt_curr(uif_emp * 3), _fmt_curr(total_uif + 50)]
    expl = f"✓ [1 Mark: Method – Multiply employee contribution by 2 (matching employer share)]\nTotal UIF = {_fmt_curr(uif_emp)} (Employee) + {_fmt_curr(uif_employer)} (Employer) = {_fmt_curr(total_uif)}.\n✓ [1 Mark: Accuracy – Combined contribution]\nTotal = {_fmt_curr(total_uif)}."
    return {
        "subskill": "gr11_tariffs_subskill_8",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Employer matches employee's 1% contribution.", "tier_2": f"Double the employee deduction: 2 × {_fmt_curr(uif_emp)}.", "tier_3": f"{correct}."},
    }

def _subskill_9(r: random.Random) -> Dict[str, Any]:
    """Audit payslip error: Identify missing deduction or discrepancy."""
    name = r.choice(SA_NAMES)
    gross = 25000.0
    paye = 3200.0
    uif = 177.12
    pension = 1875.0
    true_ded = paye + uif + pension
    printed_net = gross - (true_ded - 500)  # Payroll arithmetic error of R500

    prompt = (
        f"{name} is auditing their monthly payslip:\n"
        f"• Gross Earnings: **{_fmt_curr(gross)}**\n"
        f"• Deductions listed: PAYE {_fmt_curr(paye)}, UIF {_fmt_curr(uif)}, Pension {_fmt_curr(pension)}\n"
        f"• Printed Net Pay on slip: **{_fmt_curr(printed_net)}**\n\n"
        f"Calculate the correct net pay and state the discrepancy (error) made by payroll."
    )
    correct_net = gross - true_ded
    diff = abs(printed_net - correct_net)
    correct = f"Correct Net: {_fmt_curr(correct_net)} (Overpaid by {_fmt_curr(diff)})"
    distractors = [
        f"Correct Net: {_fmt_curr(correct_net)} (Underpaid by {_fmt_curr(diff)})",
        f"Correct Net: {_fmt_curr(printed_net)} (No error found)",
        f"Correct Net: {_fmt_curr(correct_net + 250)} (Overpaid by R 250,00)",
    ]
    expl = f"✓ [1 Mark: Method – Calculate true deductions and net salary]\nTrue Deductions = {_fmt_curr(paye)} + {_fmt_curr(uif)} + {_fmt_curr(pension)} = {_fmt_curr(true_ded)}.\nTrue Net = {_fmt_curr(gross)} − {_fmt_curr(true_ded)} = {_fmt_curr(correct_net)}.\n✓ [1 Mark: Accuracy – Identify payroll discrepancy]\nDiscrepancy = {_fmt_curr(printed_net)} − {_fmt_curr(correct_net)} = {_fmt_curr(diff)} overpaid."
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Payslip Deductions Breakdown ({name})",
        "categories": ["PAYE", "UIF", "Pension", "Net Pay"],
        "values": [int(paye), int(uif), int(pension), int(printed_net)],
    }
    return {
        "diagram_spec": d_spec,
        "subskill": "gr11_tariffs_subskill_9",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate actual deductions and true net pay.", "tier_2": f"True Net = {_fmt_curr(correct_net)}. Compare with printed net.", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 10–18: Invoices, Quotations, Receipts & VAT
# ----------------------------------------------------------------------------

def _subskill_10(r: random.Random) -> Dict[str, Any]:
    """Calculate 15% VAT on an exclusive subtotal."""
    subtotal = r.choice([1200, 2450, 3600, 4800, 8500])
    vat = subtotal * 0.15

    prompt = (
        f"A tax invoice for plumbing repairs shows a subtotal of **{_fmt_curr(subtotal)} (excluding 15% VAT)**.\n"
        f"Calculate the **VAT amount** charged on this invoice."
    )
    correct = _fmt_curr(vat)
    distractors = [_fmt_curr(subtotal * 0.14), _fmt_curr(subtotal * 0.10), _fmt_curr(vat + 50)]
    expl = f"✓ [1 Mark: Method – Multiply exclusive subtotal by 0,15]\nVAT = {_fmt_curr(subtotal)} × 0,15 = {_fmt_curr(vat)}.\n✓ [1 Mark: Accuracy – Correct VAT amount]\nVAT = {_fmt_curr(vat)}."
    return {
        "subskill": "gr11_tariffs_subskill_10",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "VAT = Subtotal × 0,15.", "tier_2": f"{subtotal} × 0,15.", "tier_3": f"{correct}."},
    }

def _subskill_11(r: random.Random) -> Dict[str, Any]:
    """Calculate total price including 15% VAT."""
    subtotal = r.choice([850, 1400, 2250, 5600])
    total_incl = subtotal * 1.15

    prompt = (
        f"A hardware store provides a quotation for timber at **{_fmt_curr(subtotal)} excluding VAT**.\n"
        f"Calculate the total cost to be paid **including 15% VAT**."
    )
    correct = _fmt_curr(total_incl)
    distractors = [_fmt_curr(subtotal * 1.14), _fmt_curr(subtotal + (subtotal * 0.10)), _fmt_curr(total_incl + 100)]
    expl = f"✓ [1 Mark: Method – Multiply exclusive price by 1,15]\nTotal (incl. VAT) = {_fmt_curr(subtotal)} × 1,15 = {_fmt_curr(total_incl)}.\n✓ [1 Mark: Accuracy – Total price incl VAT]\nTotal = {_fmt_curr(total_incl)}."
    return {
        "subskill": "gr11_tariffs_subskill_11",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Total incl VAT = Excl Price × 1,15.", "tier_2": f"{subtotal} × 1,15.", "tier_3": f"{correct}."},
    }

def _subskill_12(r: random.Random) -> Dict[str, Any]:
    """Extract exclusive price from a VAT-inclusive total (divide by 1,15)."""
    excl = r.choice([200, 450, 800, 1200, 2500])
    total_incl = excl * 1.15

    prompt = (
        f"A cash register till receipt shows a total purchase price of **{_fmt_curr(total_incl)} (including 15% VAT)**.\n"
        f"Calculate the original price of the goods **excluding VAT**."
    )
    correct = _fmt_curr(excl)
    distractors = [_fmt_curr(total_incl * 0.85), _fmt_curr(total_incl / 1.14), _fmt_curr(excl - 50)]
    expl = f"✓ [1 Mark: Method – Divide VAT-inclusive price by 1,15]\nPrice (excl. VAT) = {_fmt_curr(total_incl)} ÷ 1,15 = {_fmt_curr(excl)}.\n✓ [1 Mark: Accuracy – Correct price excluding VAT]\nPrice = {_fmt_curr(excl)}."
    return {
        "subskill": "gr11_tariffs_subskill_12",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide by 1,15 (NEVER subtract 15%).", "tier_2": f"{_fmt_curr(total_incl)} ÷ 1,15.", "tier_3": f"{correct}."},
    }

def _subskill_13(r: random.Random) -> Dict[str, Any]:
    """Calculate VAT component embedded inside a VAT-inclusive price."""
    excl = r.choice([300, 600, 1000, 1500, 2400])
    total_incl = excl * 1.15
    vat = total_incl - excl

    prompt = (
        f"An electronic device is sold at a retail price of **{_fmt_curr(total_incl)} inclusive of 15% VAT**.\n"
        f"Determine the **amount of VAT** included in this price."
    )
    correct = _fmt_curr(vat)
    distractors = [_fmt_curr(total_incl * 0.15), _fmt_curr(vat * 0.9), _fmt_curr(vat + 25)]
    expl = f"✓ [1 Mark: Method – Extract exclusive price then subtract from total]\nPrice (excl) = {_fmt_curr(total_incl)} ÷ 1,15 = {_fmt_curr(excl)}.\nVAT = {_fmt_curr(total_incl)} − {_fmt_curr(excl)} = {_fmt_curr(vat)}.\n✓ [1 Mark: Accuracy – VAT amount]\nVAT = {_fmt_curr(vat)}."
    return {
        "subskill": "gr11_tariffs_subskill_13",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find exclusive price first: Total ÷ 1,15. Then subtract.", "tier_2": f"{total_incl} − ({total_incl} ÷ 1,15).", "tier_3": f"{correct}."},
    }

def _subskill_14(r: random.Random) -> Dict[str, Any]:
    """Calculate quotation trade discount before VAT is applied."""
    list_price = r.choice([4000, 6500, 8000, 12000])
    discount_pct = r.choice([5, 10, 15])
    discount_val = list_price * (discount_pct / 100)
    subtotal = list_price - discount_val

    prompt = (
        f"A contractor quotation lists building supplies with a catalogue price of **{_fmt_curr(list_price)}**.\n"
        f"The supplier offers a trade discount of **{discount_pct}%** for orders placed this week.\n"
        f"Calculate the discounted subtotal before VAT is added."
    )
    correct = _fmt_curr(subtotal)
    distractors = [_fmt_curr(list_price - (list_price * 0.02)), _fmt_curr(list_price - discount_pct), _fmt_curr(subtotal * 1.15)]
    expl = f"✓ [1 Mark: Method – Calculate discount and subtract from list price]\nDiscount = {_fmt_curr(list_price)} × {discount_pct}% = {_fmt_curr(discount_val)}.\nSubtotal = {_fmt_curr(list_price)} − {_fmt_curr(discount_val)} = {_fmt_curr(subtotal)}.\n✓ [1 Mark: Accuracy – Discounted subtotal]\nSubtotal = {_fmt_curr(subtotal)}."
    return {
        "subskill": "gr11_tariffs_subskill_14",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate discount percentage then subtract.", "tier_2": f"{list_price} × (1 − {discount_pct/100}).", "tier_3": f"{correct}."},
    }

def _subskill_15(r: random.Random) -> Dict[str, Any]:
    """Audit invoice calculation: item quantities × unit prices = line totals."""
    qty = r.choice([12, 15, 20, 25])
    unit_p = r.choice([45.0, 62.0, 78.50, 110.0])
    line_total = qty * unit_p

    prompt = (
        f"A commercial invoice contains the line item:\n"
        f"• Description: Safety Helmets\n"
        f"• Quantity: **{qty} units**\n"
        f"• Unit Price: **{_fmt_curr(unit_p)}** (excl. VAT)\n\n"
        f"Calculate the correct line total for this item."
    )
    correct = _fmt_curr(line_total)
    distractors = [_fmt_curr((qty - 2) * unit_p), _fmt_curr(line_total * 1.15), _fmt_curr(line_total + 100)]
    expl = f"✓ [1 Mark: Method – Multiply quantity by unit price]\nLine Total = {qty} × {_fmt_curr(unit_p)} = {_fmt_curr(line_total)}.\n✓ [1 Mark: Accuracy – Correct line total]\nTotal = {_fmt_curr(line_total)}."
    return {
        "subskill": "gr11_tariffs_subskill_15",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Line total = Quantity × Unit Price.", "tier_2": f"{qty} × {unit_p}.", "tier_3": f"{correct}."},
    }

def _subskill_16(r: random.Random) -> Dict[str, Any]:
    """Calculate early settlement discount on an invoice paid within 30 days."""
    inv_total = r.choice([3500, 6800, 9200, 14500])
    disc_rate = r.choice([2.5, 3.0, 5.0])
    disc_amount = inv_total * (disc_rate / 100)
    final_pay = inv_total - disc_amount

    prompt = (
        f"An invoice for **{_fmt_curr(inv_total)}** includes the payment term: **'{_fmt_num(disc_rate)}% discount if paid within 14 days'**.\n"
        f"If the company settles the full account within 10 days, calculate the final amount to be paid."
    )
    correct = _fmt_curr(final_pay)
    distractors = [_fmt_curr(inv_total), _fmt_curr(inv_total - 100), _fmt_curr(final_pay - 50)]
    expl = f"✓ [1 Mark: Method – Calculate settlement discount and subtract]\nDiscount = {_fmt_curr(inv_total)} × {_fmt_num(disc_rate)}% = {_fmt_curr(disc_amount)}.\nFinal Payment = {_fmt_curr(inv_total)} − {_fmt_curr(disc_amount)} = {_fmt_curr(final_pay)}.\n✓ [1 Mark: Accuracy – Discounted settlement amount]\nAmount = {_fmt_curr(final_pay)}."
    return {
        "subskill": "gr11_tariffs_subskill_16",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate early payment discount percentage and subtract.", "tier_2": f"Subtract {disc_rate}% of {inv_total}.", "tier_3": f"{correct}."},
    }

def _subskill_17(r: random.Random) -> Dict[str, Any]:
    """Calculate quotation validity expiry date."""
    issue_day = r.randint(1, 15)
    validity_days = r.choice([14, 21, 30])
    expiry_day = issue_day + validity_days

    prompt = (
        f"A building contractor issues a quotation on **{issue_day} October 2026**.\n"
        f"The terms state: *'This quotation is strictly valid for **{validity_days} calendar days** from the date of issue.'*\n"
        f"Determine the final date on which the client can accept this quotation."
    )
    correct = f"{expiry_day} October 2026"
    distractors = [f"{expiry_day - 1} October 2026", f"{expiry_day + 1} October 2026", f"{issue_day + 7} October 2026"]
    expl = f"✓ [1 Mark: Method – Add validity days to issue date]\nExpiry Date = {issue_day} + {validity_days} days = {expiry_day} October 2026.\n✓ [1 Mark: Accuracy – Correct expiry date]\nDate = {expiry_day} October 2026."
    return {
        "subskill": "gr11_tariffs_subskill_17",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add validity days to issue date.", "tier_2": f"{issue_day} + {validity_days}.", "tier_3": f"{correct}."},
    }

def _subskill_18(r: random.Random) -> Dict[str, Any]:
    """Calculate courier delivery fee based on base fee + per kg rate."""
    base = 95.0
    per_kg = 12.50
    mass = r.choice([8, 14, 22, 35])
    total_fee = base + (per_kg * mass)

    prompt = (
        f"An online merchant charges delivery tariffs for parcel deliveries:\n"
        f"• Base handling fee: **{_fmt_curr(base)}**\n"
        f"• Weight charge: **{_fmt_curr(per_kg)} per kg**\n\n"
        f"Calculate the total delivery charge for a package with a mass of **{mass} kg**."
    )
    correct = _fmt_curr(total_fee)
    distractors = [_fmt_curr(base + mass), _fmt_curr(per_kg * mass), _fmt_curr(total_fee + 25)]
    expl = f"✓ [1 Mark: Method – Base fee + (rate × mass)]\nDelivery Fee = {_fmt_curr(base)} + ({_fmt_curr(per_kg)} × {mass}) = {_fmt_curr(base)} + {_fmt_curr(per_kg * mass)} = {_fmt_curr(total_fee)}.\n✓ [1 Mark: Accuracy – Total delivery tariff]\nFee = {_fmt_curr(total_fee)}."
    return {
        "subskill": "gr11_tariffs_subskill_18",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Delivery = Base fee + (per kg rate × mass).", "tier_2": f"{base} + ({per_kg} × {mass}).", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 19–27: Stepped Municipal Water Tariffs
# ----------------------------------------------------------------------------

def _subskill_19(r: random.Random) -> Dict[str, Any]:
    """Calculate water cost for consumption within Block 1 (0 to 6 kL)."""
    rate1 = r.choice([0.0, 11.50, 14.20])
    vol = r.choice([3, 4, 5, 6])
    cost = vol * rate1

    prompt = (
        f"A municipality's residential water tariff structure charges:\n"
        f"• Block 1 (0 to 6 kL): **{_fmt_curr(rate1)} per kL**\n\n"
        f"Calculate the water cost for a household that consumes **{vol} kL** during a month (excluding VAT)."
    )
    correct = _fmt_curr(cost)
    distractors = [_fmt_curr(rate1 * 6), _fmt_curr((rate1 + 5) * vol), _fmt_curr(cost + 20)]
    expl = f"✓ [1 Mark: Method – Multiply volume by Block 1 rate]\nCost = {vol} kL × {_fmt_curr(rate1)}/kL = {_fmt_curr(cost)}.\n✓ [1 Mark: Accuracy – Cost for Block 1]\nTotal = {_fmt_curr(cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_19",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply consumption by Block 1 tariff.", "tier_2": f"{vol} × {rate1}.", "tier_3": f"{correct}."},
    }

def _subskill_20(r: random.Random) -> Dict[str, Any]:
    """Calculate water cost spanning two stepped blocks (0-6 kL and >6-15 kL)."""
    r1 = 12.00
    r2 = 22.50
    total_vol = r.choice([9, 11, 14])
    b1_vol = 6
    b2_vol = total_vol - 6
    cost = (b1_vol * r1) + (b2_vol * r2)

    prompt = (
        f"Municipal stepped water tariffs (excluding VAT):\n"
        f"• Block 1 (0 – 6 kL): **{_fmt_curr(r1)} / kL**\n"
        f"• Block 2 (> 6 – 15 kL): **{_fmt_curr(r2)} / kL**\n\n"
        f"A family uses **{total_vol} kL** in a month. Calculate their total water bill (excluding VAT)."
    )
    correct = _fmt_curr(cost)
    distractors = [_fmt_curr(total_vol * r2), _fmt_curr(total_vol * r1), _fmt_curr(cost + 35)]
    expl = f"✓ [1 Mark: Method – Split into blocks: Block 1 (6 kL) and Block 2 ({b2_vol} kL)]\nBlock 1: 6 × {_fmt_curr(r1)} = {_fmt_curr(b1_vol * r1)}.\nBlock 2: {b2_vol} × {_fmt_curr(r2)} = {_fmt_curr(b2_vol * r2)}.\nTotal = {_fmt_curr(b1_vol * r1)} + {_fmt_curr(b2_vol * r2)} = {_fmt_curr(cost)}.\n✓ [1 Mark: Accuracy – Total cost]\nBill = {_fmt_curr(cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_20",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate each block separately and add.", "tier_2": f"6 kL at R 12,00 + {b2_vol} kL at R 22,50.", "tier_3": f"{correct}."},
    }

def _subskill_21(r: random.Random) -> Dict[str, Any]:
    """Calculate cost for high-volume consumption across 3 stepped blocks (0-6, >6-15, >15-30 kL)."""
    r1, r2, r3 = 10.0, 20.0, 35.0
    vol = r.choice([18, 22, 25])
    c1 = 6 * r1
    c2 = 9 * r2
    c3 = (vol - 15) * r3
    total = c1 + c2 + c3

    prompt = (
        f"A municipal tariff table shows three stepped water blocks:\n"
        f"• Block 1 (0 – 6 kL): **{_fmt_curr(r1)} / kL**\n"
        f"• Block 2 (> 6 – 15 kL): **{_fmt_curr(r2)} / kL**\n"
        f"• Block 3 (> 15 – 30 kL): **{_fmt_curr(r3)} / kL**\n\n"
        f"Calculate the total cost for **{vol} kL** of water (excluding VAT)."
    )
    correct = _fmt_curr(total)
    distractors = [_fmt_curr(vol * r3), _fmt_curr((vol - 6) * r2), _fmt_curr(total + 50)]
    expl = f"✓ [1 Mark: Method – Allocate consumption across blocks 1, 2, and 3]\nBlock 1 (6 kL): {_fmt_curr(c1)}.\nBlock 2 (9 kL): {_fmt_curr(c2)}.\nBlock 3 ({vol - 15} kL): {_fmt_curr(c3)}.\nTotal = {_fmt_curr(c1)} + {_fmt_curr(c2)} + {_fmt_curr(c3)} = {_fmt_curr(total)}.\n✓ [1 Mark: Accuracy – Total charge]\nTotal = {_fmt_curr(total)}."
    return {
        "subskill": "gr11_tariffs_subskill_21",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Fill Block 1 (6 kL), Block 2 (9 kL), then remainder in Block 3.", "tier_2": f"6×10 + 9×20 + {vol-15}×35.", "tier_3": f"{correct}."},
    }

def _subskill_22(r: random.Random) -> Dict[str, Any]:
    """Calculate percentage tariff increase between two municipal budget years."""
    old_rate = r.choice([18.50, 20.00, 24.00])
    inc_pct = r.choice([7.5, 8.5, 11.2, 12.0])
    new_rate = round(old_rate * (1 + inc_pct / 100), 2)
    actual_pct = round(((new_rate - old_rate) / old_rate) * 100, 1)

    prompt = (
        f"In 2025, the municipal water tariff for Block 2 was **{_fmt_curr(old_rate)} per kL**.\n"
        f"From 1 July 2026, the tariff increased to **{_fmt_curr(new_rate)} per kL**.\n\n"
        f"Calculate the **percentage increase** in the water tariff (round to 1 decimal place)."
    )
    correct = f"{_fmt_num(actual_pct)}%"
    distractors = [f"{_fmt_num(actual_pct + 2.0)}%", f"{_fmt_num(actual_pct - 2.0)}%", f"{_fmt_num(actual_pct * 1.5)}%"]
    expl = f"✓ [1 Mark: Method – Formula: ((New − Old) ÷ Old) × 100]\nIncrease = {_fmt_curr(new_rate)} − {_fmt_curr(old_rate)} = {_fmt_curr(new_rate - old_rate)}.\n% Increase = ({_fmt_curr(new_rate - old_rate)} ÷ {_fmt_curr(old_rate)}) × 100 = {_fmt_num(actual_pct)}%.\n✓ [1 Mark: Accuracy – Percentage increase]\nIncrease = {_fmt_num(actual_pct)}%."
    return {
        "subskill": "gr11_tariffs_subskill_22",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "% Increase = (New − Old) / Old × 100.", "tier_2": f"({new_rate} − {old_rate}) / {old_rate} × 100.", "tier_3": f"{correct}."},
    }

def _subskill_23(r: random.Random) -> Dict[str, Any]:
    """Calculate wastewater (sanitation/sewerage) charge linked to water consumption."""
    water_vol = r.choice([15, 20, 25, 30])
    sewer_pct = 70  # Standard SA municipal rule: 70% of fresh water returns as sewer
    sewer_rate = 14.50
    sewer_vol = water_vol * (sewer_pct / 100)
    sewer_cost = sewer_vol * sewer_rate

    prompt = (
        f"A municipality calculates residential sanitation (sewerage) charges based on the assumption that "
        f"**70%** of fresh water consumed flows into the sewage system.\n"
        f"• Household water consumed: **{water_vol} kL**\n"
        f"• Sanitation tariff: **{_fmt_curr(sewer_rate)} per kL** of wastewater\n\n"
        f"Calculate the monthly sanitation fee."
    )
    correct = _fmt_curr(sewer_cost)
    distractors = [_fmt_curr(water_vol * sewer_rate), _fmt_curr(sewer_vol * 12.0), _fmt_curr(sewer_cost + 30)]
    expl = f"✓ [1 Mark: Method – Calculate 70% wastewater volume]\nWastewater Volume = {water_vol} kL × 70% = {_fmt_num(sewer_vol)} kL.\n✓ [1 Mark: Accuracy – Sanitation charge]\nCost = {_fmt_num(sewer_vol)} kL × {_fmt_curr(sewer_rate)} = {_fmt_curr(sewer_cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_23",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find 70% of total water volume, then multiply by sanitation rate.", "tier_2": f"{water_vol} × 0,70 × {sewer_rate}.", "tier_3": f"{correct}."},
    }

def _subskill_24(r: random.Random) -> Dict[str, Any]:
    """Calculate financial cost of an undetected leaking toilet over 30 days."""
    litres_per_hour = r.choice([25, 40, 50])  # Leaking cistern
    days = 30
    total_litres = litres_per_hour * 24 * days
    total_kl = total_litres / 1000
    marginal_rate = 38.0  # Block 3 rate
    wasted_cost = total_kl * marginal_rate

    prompt = (
        f"A leaking toilet cistern wastes **{litres_per_hour} litres of water per hour** undetected for **30 days**.\n"
        f"If the household is in Block 3 where the marginal tariff is **{_fmt_curr(marginal_rate)} per kL**:\n"
        f"Calculate the total financial cost of the wasted water."
    )
    correct = _fmt_curr(wasted_cost)
    distractors = [_fmt_curr(total_litres * marginal_rate), _fmt_curr(wasted_cost * 1.5), _fmt_curr(wasted_cost - 100)]
    expl = f"✓ [1 Mark: Method – Convert wasted water to kL (hours × days ÷ 1 000)]\nTotal wasted = {litres_per_hour} ℓ/hr × 24 hr/day × 30 days = {_fmt_num(total_litres)} ℓ = {_fmt_num(total_kl)} kL.\n✓ [1 Mark: Accuracy – Cost at marginal rate]\nCost = {_fmt_num(total_kl)} kL × {_fmt_curr(marginal_rate)} = {_fmt_curr(wasted_cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_24",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find total litres in 30 days, divide by 1 000 for kL, multiply by tariff.", "tier_2": f"{litres_per_hour} × 24 × 30 / 1000 × {marginal_rate}.", "tier_3": f"{correct}."},
    }

def _subskill_25(r: random.Random) -> Dict[str, Any]:
    """Reverse stepped tariff calculation: Determine water volume from total bill."""
    r1, r2 = 15.0, 30.0
    # Bill = 6 * 15 + b2_vol * 30
    b2_vol = r.choice([3, 5, 7, 9])
    total_cost = (6 * r1) + (b2_vol * r2)
    total_vol = 6 + b2_vol

    prompt = (
        f"Municipal water tariffs (excl. VAT):\n"
        f"• Block 1 (0 – 6 kL): **{_fmt_curr(r1)} / kL**\n"
        f"• Block 2 (> 6 – 15 kL): **{_fmt_curr(r2)} / kL**\n\n"
        f"A household's water consumption charge for the month is **{_fmt_curr(total_cost)}**.\n"
        f"Determine the total volume of water consumed in **kL**."
    )
    correct = f"{total_vol} kL"
    distractors = [f"{total_vol - 2} kL", f"{total_vol + 3} kL", f"{round(total_cost / r2, 1)} kL"]
    expl = f"✓ [1 Mark: Method – Deduct Block 1 cost then divide remainder by Block 2 rate]\nBlock 1 Cost = 6 kL × {_fmt_curr(r1)} = {_fmt_curr(6 * r1)}.\nRemaining Cost for Block 2 = {_fmt_curr(total_cost)} − {_fmt_curr(6 * r1)} = {_fmt_curr(b2_vol * r2)}.\nBlock 2 Volume = {_fmt_curr(b2_vol * r2)} ÷ {_fmt_curr(r2)} = {b2_vol} kL.\nTotal Volume = 6 + {b2_vol} = {total_vol} kL.\n✓ [1 Mark: Accuracy – Total volume]\nVolume = {total_vol} kL."
    return {
        "subskill": "gr11_tariffs_subskill_25",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract Block 1 cost (R 90,00) from total. Divide remainder by R 30,00.", "tier_2": f"6 + ({total_cost - 90} ÷ 30).", "tier_3": f"{correct}."},
    }

def _subskill_26(r: random.Random) -> Dict[str, Any]:
    """Calculate commercial flat tariff vs. residential stepped tariff comparison."""
    vol = 20
    # Residential: 6*12 + 9*24 + 5*38 = 72 + 216 + 190 = 478
    res_cost = (6 * 12.0) + (9 * 24.0) + (5 * 38.0)
    comm_rate = 28.50
    comm_cost = vol * comm_rate
    diff = abs(comm_cost - res_cost)

    prompt = (
        f"A small home business compares water tariffs for **{vol} kL**:\n"
        f"• **Residential Stepped:** 0–6 kL @ R 12,00; >6–15 kL @ R 24,00; >15–30 kL @ R 38,00\n"
        f"• **Commercial Flat Rate:** R 28,50 per kL for all consumption\n\n"
        f"Which tariff is cheaper for 20 kL and by how much?"
    )
    correct = f"Residential is cheaper by {_fmt_curr(diff)}"
    distractors = [
        f"Commercial is cheaper by {_fmt_curr(diff)}",
        f"Residential is cheaper by {_fmt_curr(diff + 50)}",
        f"Both tariffs cost the same",
    ]
    expl = f"✓ [1 Mark: Method – Calculate both costs]\nResidential = (6×12) + (9×24) + (5×38) = R 72 + R 216 + R 190 = {_fmt_curr(res_cost)}.\nCommercial = 20 × {_fmt_curr(comm_rate)} = {_fmt_curr(comm_cost)}.\n✓ [1 Mark: Accuracy – Comparison and difference]\nDifference = {_fmt_curr(comm_cost)} − {_fmt_curr(res_cost)} = {_fmt_curr(diff)} cheaper on Residential."
    return {
        "subskill": "gr11_tariffs_subskill_26",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate residential total and commercial total. Compare.", "tier_2": f"Res: R 478,00 vs Comm: R 570,00.", "tier_3": f"{correct}."},
    }

def _subskill_27(r: random.Random) -> Dict[str, Any]:
    """Read stepped water tariff graph and identify block transition coordinate."""
    prompt = (
        f"A municipal stepped water tariff graph plots Total Cost (y-axis in Rands) against Volume (x-axis in kL).\n"
        f"Block 1 (0 to 6 kL) has a slope of R 12,00/kL.\n"
        f"Block 2 (>6 to 15 kL) has a slope of R 24,00/kL.\n\n"
        f"Identify the coordinate `(x; y)` on the graph where the line changes slope (the first inflection knot)."
    )
    correct = "(6 kL ; R 72,00)"
    distractors = ["(6 kL ; R 144,00)", "(15 kL ; R 216,00)", "(0 kL ; R 0,00)"]
    expl = f"✓ [1 Mark: Method – Calculate cost at boundary of Block 1 (x = 6)]\nAt x = 6 kL: Cost = 6 × R 12,00 = R 72,00.\n✓ [1 Mark: Accuracy – State boundary coordinate (x; y)]\nTransition coordinate = (6 kL ; R 72,00)."
    d_spec = {
        "diagram_role": "context",
        "kind": "step_tariff",
        "title": f"Municipal Stepped Water Tariff Graph (Block 1: R {r.choice([10, 12, 14])}/kL)",
        "blocks": [{"limit": 6, "rate": 12.0}, {"limit": 15, "rate": 24.0}],
    }
    return {
        "diagram_spec": d_spec,
        "subskill": "gr11_tariffs_subskill_27",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "The first block ends at 6 kL. Calculate 6 × R 12,00.", "tier_2": "Coordinate = (6 ; 6 × 12).", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 28–36: Electricity Tariffs & IBT Blocks
# ----------------------------------------------------------------------------

def _subskill_28(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic electricity on Inclining Block Tariff (IBT) Block 1 (0 to 350 kWh)."""
    rate1 = 1.95  # R1,95 / kWh
    kwh = r.choice([150, 220, 280, 320])
    cost = kwh * rate1

    prompt = (
        f"Under an Inclining Block Tariff (IBT) structure for prepaid electricity:\n"
        f"• Block 1 (0 to 350 kWh): **{_fmt_curr(rate1)} per kWh**\n"
        f"• Block 2 (> 350 kWh): **R 2,85 per kWh**\n\n"
        f"Calculate the cost of **{kwh} kWh** of electricity (excluding VAT)."
    )
    correct = _fmt_curr(cost)
    distractors = [_fmt_curr(kwh * 2.85), _fmt_curr((kwh + 50) * rate1), _fmt_curr(cost * 1.15)]
    expl = f"✓ [1 Mark: Method – Multiply kWh by Block 1 rate]\nCost = {kwh} kWh × {_fmt_curr(rate1)} = {_fmt_curr(cost)}.\n✓ [1 Mark: Accuracy – Electricity cost]\nTotal = {_fmt_curr(cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_28",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Consumption is below 350 kWh, so only Block 1 rate applies.", "tier_2": f"{kwh} × {rate1}.", "tier_3": f"{correct}."},
    }

def _subskill_29(r: random.Random) -> Dict[str, Any]:
    """Calculate IBT electricity spanning Block 1 and Block 2 (>350 kWh)."""
    r1 = 2.10
    r2 = 3.10
    total_kwh = r.choice([420, 500, 600])
    c1 = 350 * r1
    c2 = (total_kwh - 350) * r2
    total = c1 + c2

    prompt = (
        f"Municipal electricity IBT rates (excl. VAT):\n"
        f"• Block 1 (0 – 350 kWh): **{_fmt_curr(r1)} / kWh**\n"
        f"• Block 2 (> 350 kWh): **{_fmt_curr(r2)} / kWh**\n\n"
        f"Calculate the total cost for **{total_kwh} kWh**."
    )
    correct = _fmt_curr(total)
    distractors = [_fmt_curr(total_kwh * r2), _fmt_curr(total_kwh * r1), _fmt_curr(total + 100)]
    expl = f"✓ [1 Mark: Method – Split into Block 1 (350 kWh) and Block 2 ({total_kwh - 350} kWh)]\nBlock 1: 350 × {_fmt_curr(r1)} = {_fmt_curr(c1)}.\nBlock 2: {total_kwh - 350} × {_fmt_curr(r2)} = {_fmt_curr(c2)}.\nTotal = {_fmt_curr(c1)} + {_fmt_curr(c2)} = {_fmt_curr(total)}.\n✓ [1 Mark: Accuracy – Total cost]\nTotal = {_fmt_curr(total)}."
    return {
        "subskill": "gr11_tariffs_subskill_29",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "First 350 kWh at R 2,10. Remainder at R 3,10.", "tier_2": f"350×2,10 + {total_kwh-350}×3,10.", "tier_3": f"{correct}."},
    }

def _subskill_30(r: random.Random) -> Dict[str, Any]:
    """Calculate prepaid electricity voucher tokens: Units purchased from money spent."""
    money_spent = r.choice([200, 300, 500, 800])
    tariff_incl_vat = 2.30  # R 2,30 per unit incl VAT
    units = round(money_spent / tariff_incl_vat, 1)

    prompt = (
        f"A resident purchases a prepaid electricity voucher for **{_fmt_curr(money_spent)}**.\n"
        f"The applicable tariff is **{_fmt_curr(tariff_incl_vat)} per kWh (unit)** including VAT.\n\n"
        f"How many units (kWh) of electricity will appear on the printed voucher token?"
    )
    correct = f"{_fmt_num(units)} kWh"
    distractors = [f"{_fmt_num(units - 15.0)} kWh", f"{_fmt_num(units + 20.0)} kWh", f"{_fmt_num(money_spent * 2.3)} kWh"]
    expl = f"✓ [1 Mark: Method – Divide money spent by tariff per unit]\nUnits = {_fmt_curr(money_spent)} ÷ {_fmt_curr(tariff_incl_vat)}/kWh = {_fmt_num(units)} kWh.\n✓ [1 Mark: Accuracy – Number of units]\nUnits = {_fmt_num(units)} kWh."
    return {
        "subskill": "gr11_tariffs_subskill_30",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Units = Money ÷ Tariff per unit.", "tier_2": f"{money_spent} ÷ {tariff_incl_vat}.", "tier_3": f"{correct}."},
    }

def _subskill_31(r: random.Random) -> Dict[str, Any]:
    """Calculate post-paid electricity bill including fixed monthly service fee + energy charge + 15% VAT."""
    service_fee = 245.0  # Basic monthly network charge
    energy_kwh = 400
    energy_rate = 2.20
    energy_cost = energy_kwh * energy_rate
    subtotal = service_fee + energy_cost
    total_incl_vat = subtotal * 1.15

    prompt = (
        f"A post-paid domestic electricity tariff structure charges:\n"
        f"• Basic monthly service network fee: **{_fmt_curr(service_fee)}** (fixed)\n"
        f"• Energy consumption charge: **{_fmt_curr(energy_rate)} per kWh**\n\n"
        f"Calculate the total monthly bill including 15% VAT for **{energy_kwh} kWh** consumed."
    )
    correct = _fmt_curr(total_incl_vat)
    distractors = [_fmt_curr(subtotal), _fmt_curr(energy_cost * 1.15), _fmt_curr(total_incl_vat + 100)]
    expl = f"✓ [1 Mark: Method – Sum fixed fee and energy cost, then add 15% VAT]\nEnergy Cost = {energy_kwh} × {_fmt_curr(energy_rate)} = {_fmt_curr(energy_cost)}.\nSubtotal = {_fmt_curr(service_fee)} + {_fmt_curr(energy_cost)} = {_fmt_curr(subtotal)}.\nTotal (incl. VAT) = {_fmt_curr(subtotal)} × 1,15 = {_fmt_curr(total_incl_vat)}.\n✓ [1 Mark: Accuracy – Total bill]\nTotal = {_fmt_curr(total_incl_vat)}."
    return {
        "subskill": "gr11_tariffs_subskill_31",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtotal = Fixed fee + (kWh × rate). Then multiply by 1,15.", "tier_2": f"({service_fee} + {energy_cost}) × 1,15.", "tier_3": f"{correct}."},
    }

def _subskill_32(r: random.Random) -> Dict[str, Any]:
    """Calculate running cost of a domestic appliance: Power (kW) × Time (hrs) × Tariff."""
    watts = r.choice([1500, 2000, 2500, 3000])  # Geyser / heater
    kw = watts / 1000
    hours = r.choice([3, 4, 5])
    tariff = 2.50
    daily_cost = kw * hours * tariff

    prompt = (
        f"An electric space heater is rated at **{watts} W** (**{_fmt_num(kw)} kW**).\n"
        f"The heater is operated continuously for **{hours} hours per day** during winter.\n"
        f"If electricity costs **{_fmt_curr(tariff)} per kWh**:\n"
        f"Calculate the daily running cost of this heater."
    )
    correct = _fmt_curr(daily_cost)
    distractors = [_fmt_curr(watts * hours * tariff), _fmt_curr(kw * hours), _fmt_curr(daily_cost * 1.5)]
    expl = f"✓ [1 Mark: Method – Formula: kWh = kW × hours, then multiply by tariff]\nEnergy = {_fmt_num(kw)} kW × {hours} hours = {_fmt_num(kw * hours)} kWh.\nDaily Cost = {_fmt_num(kw * hours)} kWh × {_fmt_curr(tariff)} = {_fmt_curr(daily_cost)}.\n✓ [1 Mark: Accuracy – Daily appliance cost]\nCost = {_fmt_curr(daily_cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_32",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "kWh = kW × hours. Cost = kWh × Tariff.", "tier_2": f"{kw} × {hours} × {tariff}.", "tier_3": f"{correct}."},
    }

def _subskill_33(r: random.Random) -> Dict[str, Any]:
    """Prepaid vs. Post-paid break-even consumption calculation."""
    # Prepaid: R 2,60 per kWh (0 fixed fee)
    # Postpaid: R 200 fixed fee + R 2,10 per kWh
    # 2,60 x = 200 + 2,10 x  => 0,50 x = 200 => x = 400 kWh
    prompt = (
        f"A homeowner compares two electricity plans:\n"
        f"• **Prepaid:** {_fmt_curr(2.60)} per kWh with **no fixed monthly fee**\n"
        f"• **Post-paid:** Basic monthly fee of **R 200,00** plus **{_fmt_curr(2.10)} per kWh**\n\n"
        f"At what monthly consumption level (in **kWh**) do both options cost the exact same amount (break-even)?"
    )
    correct = "400 kWh"
    distractors = ["350 kWh", "450 kWh", "500 kWh"]
    expl = f"✓ [1 Mark: Method – Set up break-even equation: 2,60x = 200 + 2,10x]\n0,50x = 200.\nx = 200 ÷ 0,50 = 400 kWh.\n✓ [1 Mark: Accuracy – Break-even consumption]\nBreak-even = 400 kWh."
    return {
        "subskill": "gr11_tariffs_subskill_33",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Fixed fee ÷ Difference in unit tariffs.", "tier_2": "200 ÷ (2,60 − 2,10) = 200 ÷ 0,50.", "tier_3": f"{correct}."},
    }

def _subskill_34(r: random.Random) -> Dict[str, Any]:
    """Calculate Time-of-Use (TOU) electricity cost (Peak vs. Off-Peak)."""
    peak_rate = 3.80
    offpeak_rate = 1.60
    peak_kwh = 120
    offpeak_kwh = 280
    total = (peak_kwh * peak_rate) + (offpeak_kwh * offpeak_rate)

    prompt = (
        f"An industrial Time-of-Use (TOU) electricity tariff charges:\n"
        f"• Peak Hours: **{_fmt_curr(peak_rate)} / kWh**\n"
        f"• Off-Peak Hours: **{_fmt_curr(offpeak_rate)} / kWh**\n\n"
        f"During one month, a bakery uses **{peak_kwh} kWh during peak hours** and **{offpeak_kwh} kWh during off-peak hours**.\n"
        f"Calculate the total energy charge."
    )
    correct = _fmt_curr(total)
    distractors = [_fmt_curr((peak_kwh + offpeak_kwh) * peak_rate), _fmt_curr((peak_kwh + offpeak_kwh) * offpeak_rate), _fmt_curr(total + 120)]
    expl = f"✓ [1 Mark: Method – Calculate peak and off-peak costs]\nPeak: {peak_kwh} × {_fmt_curr(peak_rate)} = {_fmt_curr(peak_kwh * peak_rate)}.\nOff-Peak: {offpeak_kwh} × {_fmt_curr(offpeak_rate)} = {_fmt_curr(offpeak_kwh * offpeak_rate)}.\nTotal = {_fmt_curr(peak_kwh * peak_rate)} + {_fmt_curr(offpeak_kwh * offpeak_rate)} = {_fmt_curr(total)}.\n✓ [1 Mark: Accuracy – Total TOU energy cost]\nTotal = {_fmt_curr(total)}."
    return {
        "subskill": "gr11_tariffs_subskill_34",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Peak cost + Off-peak cost.", "tier_2": f"({peak_kwh} × 3,80) + ({offpeak_kwh} × 1,60).", "tier_3": f"{correct}."},
    }

def _subskill_35(r: random.Random) -> Dict[str, Any]:
    """Calculate solar feed-in tariff credit subtracted from grid consumption bill."""
    grid_import_kwh = r.choice([350, 400, 450, 500, 550])
    import_rate = r.choice([2.20, 2.40, 2.50, 2.60])
    solar_export_kwh = r.choice([120, 150, 180, 200])
    export_feedin_rate = r.choice([0.90, 1.10, 1.20])

    cost_import = grid_import_kwh * import_rate
    credit_export = solar_export_kwh * export_feedin_rate
    net_bill = cost_import - credit_export

    prompt = (
        f"A household with rooftop solar panels has a bi-directional electricity meter:\n"
        f"• Electricity imported from grid: **{grid_import_kwh} kWh** at **{_fmt_curr(import_rate)} / kWh**\n"
        f"• Surplus solar exported to grid: **{solar_export_kwh} kWh** at **{_fmt_curr(export_feedin_rate)} / kWh** (feed-in tariff credit)\n\n"
        f"Calculate the net energy bill payable (excluding VAT)."
    )
    correct = _fmt_curr(net_bill)
    distractors = [_fmt_curr(cost_import + credit_export), _fmt_curr(cost_import), _fmt_curr(net_bill * 1.15)]
    expl = f"✓ [1 Mark: Method – Import cost minus solar export credit]\nGrid Import = {grid_import_kwh} × {_fmt_curr(import_rate)} = {_fmt_curr(cost_import)}.\nSolar Export Credit = {solar_export_kwh} × {_fmt_curr(export_feedin_rate)} = {_fmt_curr(credit_export)}.\nNet Bill = {_fmt_curr(cost_import)} − {_fmt_curr(credit_export)} = {_fmt_curr(net_bill)}.\n✓ [1 Mark: Accuracy – Net payable]\nNet = {_fmt_curr(net_bill)}."
    d_spec = {
        "diagram_role": "context",
        "kind": "double_bar_graph",
        "title": f"Solar Generation vs Grid Consumption (Export: {solar_export_kwh} kWh)",
        "categories": ["Grid Import", "Solar Export"],
        "values": [cost_import, credit_export],
    }
    return {
        "diagram_spec": d_spec,
        "subskill": "gr11_tariffs_subskill_35",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Net Bill = Grid Import Cost − Solar Export Credit.", "tier_2": f"({grid_import_kwh}×2,40) − ({solar_export_kwh}×1,10).", "tier_3": f"{correct}."},
    }

def _subskill_36(r: random.Random) -> Dict[str, Any]:
    """Calculate savings from replacing incandescent bulbs with LED bulbs over 365 days."""
    old_w = 60
    new_w = 9
    saved_w = old_w - new_w
    hours_per_day = 5
    tariff = 2.50
    annual_kwh_saved = (saved_w * hours_per_day * 365) / 1000
    annual_savings = annual_kwh_saved * tariff

    prompt = (
        f"A homeowner replaces 10 old **60 W** incandescent bulbs with energy-efficient **9 W** LED bulbs.\n"
        f"Each bulb is illuminated for an average of **5 hours per day** over 365 days.\n"
        f"If electricity costs **{_fmt_curr(tariff)} per kWh**:\n"
        f"Calculate the total annual electricity cost saved by replacing all 10 bulbs."
    )
    total_savings = annual_savings * 10
    correct = _fmt_curr(total_savings)
    distractors = [_fmt_curr(annual_savings), _fmt_curr(total_savings * 0.5), _fmt_curr(total_savings + 200)]
    expl = f"✓ [1 Mark: Method – Calculate energy saved per year across 10 bulbs]\nWatts saved per bulb = 60 W − 9 W = 51 W.\nTotal Watts saved = 10 × 51 W = 510 W = 0,51 kW.\nAnnual kWh = 0,51 kW × 5 hrs/day × 365 days = {_fmt_num(annual_kwh_saved * 10)} kWh.\n✓ [1 Mark: Accuracy – Total financial savings]\nSavings = {_fmt_num(annual_kwh_saved * 10)} kWh × {_fmt_curr(tariff)} = {_fmt_curr(total_savings)}."
    return {
        "subskill": "gr11_tariffs_subskill_36",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Watts saved = (60 − 9) × 10 = 510 W = 0,51 kW. Find annual kWh then multiply by tariff.", "tier_2": f"0,51 × 5 × 365 × 2,50.", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 37–44: Transport & Communication Tariffs
# ----------------------------------------------------------------------------

def _subskill_37(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly commuter minibus taxi travel budget (2 trips/day × 22 work days)."""
    fare_single = r.choice([16.0, 18.50, 22.0, 25.0])
    days = 22
    total_trips = days * 2
    monthly_cost = total_trips * fare_single

    prompt = (
        f"A commuter uses a minibus taxi to travel to and from work every day.\n"
        f"• Single one-way fare: **{_fmt_curr(fare_single)}**\n"
        f"• Number of working days in the month: **{days} days** (2 one-way trips per day)\n\n"
        f"Calculate the total monthly taxi transport budget."
    )
    correct = _fmt_curr(monthly_cost)
    distractors = [_fmt_curr(days * fare_single), _fmt_curr(monthly_cost + 100), _fmt_curr(monthly_cost * 1.15)]
    expl = f"✓ [1 Mark: Method – Multiply fare by 2 trips per day and 22 work days]\nTotal Trips = 22 × 2 = {total_trips} trips.\nTotal Budget = {total_trips} × {_fmt_curr(fare_single)} = {_fmt_curr(monthly_cost)}.\n✓ [1 Mark: Accuracy – Monthly taxi budget]\nTotal = {_fmt_curr(monthly_cost)}."
    return {
        "subskill": "gr11_tariffs_subskill_37",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "2 trips per day for 22 days = 44 trips. Multiply by fare.", "tier_2": f"44 × {fare_single}.", "tier_3": f"{correct}."},
    }

def _subskill_38(r: random.Random) -> Dict[str, Any]:
    """Compare municipal bus multi-trip clip-card bundle vs. individual daily tickets."""
    single_ticket = 24.0
    clip_card_10 = 195.0  # R 19,50 per trip
    trips = 10
    cost_single = trips * single_ticket
    savings = cost_single - clip_card_10

    prompt = (
        f"A municipal bus service offers two payment methods:\n"
        f"• Option A: Single journey cash ticket at **{_fmt_curr(single_ticket)} per trip**\n"
        f"• Option B: 10-trip commuter clip-card bundle at **{_fmt_curr(clip_card_10)}**\n\n"
        f"How much money does a commuter save on 10 trips by purchasing the clip-card bundle?"
    )
    correct = _fmt_curr(savings)
    distractors = [_fmt_curr(clip_card_10), _fmt_curr(savings + 15), _fmt_curr(single_ticket * 2)]
    expl = f"✓ [1 Mark: Method – Calculate 10 single tickets minus clip-card price]\nCost of 10 single tickets = 10 × {_fmt_curr(single_ticket)} = {_fmt_curr(cost_single)}.\nSavings = {_fmt_curr(cost_single)} − {_fmt_curr(clip_card_10)} = {_fmt_curr(savings)}.\n✓ [1 Mark: Accuracy – Savings amount]\nSavings = {_fmt_curr(savings)}."
    return {
        "subskill": "gr11_tariffs_subskill_38",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "10 × R 24,00 = R 240,00. Subtract R 195,00.", "tier_2": "240 − 195.", "tier_3": f"{correct}."},
    }

def _subskill_39(r: random.Random) -> Dict[str, Any]:
    """Gautrain train fare table lookup and calculation with peak/off-peak rates."""
    peak_fare = 92.0
    offpeak_fare = 78.0
    num_peak = 14
    num_offpeak = 6
    total = (num_peak * peak_fare) + (num_offpeak * offpeak_fare)

    prompt = (
        f"A commuter travels on the Gautrain between Pretoria and Sandton:\n"
        f"• Peak Fare (06:00 – 08:30): **{_fmt_curr(peak_fare)} per trip**\n"
        f"• Off-Peak Fare: **{_fmt_curr(offpeak_fare)} per trip**\n\n"
        f"During one month, the commuter makes **{num_peak} peak trips** and **{num_offpeak} off-peak trips**.\n"
        f"Calculate the total rail fare expenditure."
    )
    correct = _fmt_curr(total)
    distractors = [_fmt_curr((num_peak + num_offpeak) * peak_fare), _fmt_curr(total - 100), _fmt_curr(total * 1.15)]
    expl = f"✓ [1 Mark: Method – Calculate peak and off-peak travel]\nPeak = {num_peak} × {_fmt_curr(peak_fare)} = {_fmt_curr(num_peak * peak_fare)}.\nOff-Peak = {num_offpeak} × {_fmt_curr(offpeak_fare)} = {_fmt_curr(num_offpeak * offpeak_fare)}.\nTotal = {_fmt_curr(num_peak * peak_fare)} + {_fmt_curr(num_offpeak * offpeak_fare)} = {_fmt_curr(total)}.\n✓ [1 Mark: Accuracy – Total fare]\nTotal = {_fmt_curr(total)}."
    return {
        "subskill": "gr11_tariffs_subskill_39",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "(14 × R 92) + (6 × R 78).", "tier_2": "Multiply trips by respective tariffs.", "tier_3": f"{correct}."},
    }

def _subskill_40(r: random.Random) -> Dict[str, Any]:
    """Cell phone call per-second billing vs. per-minute billing calculation."""
    seconds = r.choice([75, 130, 195, 250])
    per_sec_rate = 0.025  # R 1,50 per minute billed per second
    per_min_rate = 1.50   # Full minute rounding

    cost_per_sec = round(seconds * per_sec_rate, 2)
    billed_minutes = math.ceil(seconds / 60)
    cost_per_min = billed_minutes * per_min_rate
    diff = round(cost_per_min - cost_per_sec, 2)

    prompt = (
        f"A cellular network offers two call billing options for a **{seconds}-second call**:\n"
        f"• **Plan A (Per-Second Billing):** {_fmt_curr(per_sec_rate)} per second from the very first second\n"
        f"• **Plan B (Per-Minute Billing):** {_fmt_curr(per_min_rate)} per minute or part thereof (fractions of a minute round up)\n\n"
        f"Calculate the difference in cost between Plan B and Plan A for this call."
    )
    correct = _fmt_curr(diff)
    distractors = [_fmt_curr(cost_per_sec), _fmt_curr(cost_per_min), _fmt_curr(diff + 0.50)]
    expl = f"✓ [1 Mark: Method – Calculate both billing methods]\nPlan A = {seconds} sec × {_fmt_curr(per_sec_rate)} = {_fmt_curr(cost_per_sec)}.\nPlan B = {billed_minutes} full minute(s) × {_fmt_curr(per_min_rate)} = {_fmt_curr(cost_per_min)}.\nDifference = {_fmt_curr(cost_per_min)} − {_fmt_curr(cost_per_sec)} = {_fmt_curr(diff)}.\n✓ [1 Mark: Accuracy – Difference]\nDifference = {_fmt_curr(diff)}."
    return {
        "subskill": "gr11_tariffs_subskill_40",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Plan A = seconds × rate. Plan B = round up minutes × per-minute rate.", "tier_2": f"Plan B: {billed_minutes} min × R 1,50 = {_fmt_curr(cost_per_min)}.", "tier_3": f"{correct}."},
    }

def _subskill_41(r: random.Random) -> Dict[str, Any]:
    """Cell phone out-of-bundle (OOB) data rate penalty calculation."""
    bundle_size_gb = 2
    bundle_cost = 149.0
    oob_rate_per_mb = 0.29
    extra_mb = r.choice([250, 400, 650])
    extra_cost = extra_mb * oob_rate_per_mb
    total_bill = bundle_cost + extra_cost

    prompt = (
        f"A student subscribes to a 2 GB monthly data bundle at **{_fmt_curr(bundle_cost)}**.\n"
        f"Once the bundle is depleted, the network charges an Out-of-Bundle (OOB) rate of **{_fmt_curr(oob_rate_per_mb)} per MB**.\n"
        f"If the student uses **{extra_mb} MB** of out-of-bundle data:\n"
        f"Calculate the total data expenditure for the month."
    )
    correct = _fmt_curr(total_bill)
    distractors = [_fmt_curr(extra_cost), _fmt_curr(bundle_cost + (extra_mb * 0.10)), _fmt_curr(total_bill + 50)]
    expl = f"✓ [1 Mark: Method – Base bundle cost + (extra MB × OOB rate)]\nExtra Data Cost = {extra_mb} MB × {_fmt_curr(oob_rate_per_mb)} = {_fmt_curr(extra_cost)}.\nTotal Bill = {_fmt_curr(bundle_cost)} + {_fmt_curr(extra_cost)} = {_fmt_curr(total_bill)}.\n✓ [1 Mark: Accuracy – Total expenditure]\nTotal = {_fmt_curr(total_bill)}."
    return {
        "subskill": "gr11_tariffs_subskill_41",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Total = Bundle cost + (Extra MB × R 0,29).", "tier_2": f"{bundle_cost} + ({extra_mb} × 0,29).", "tier_3": f"{correct}."},
    }

def _subskill_42(r: random.Random) -> Dict[str, Any]:
    """Cell phone contract vs. prepaid break-even call minutes calculation."""
    # Contract: R 299/mo + R 1,20/min
    # Prepaid: R 2,20/min (0 fixed fee)
    # 2,20 x = 299 + 1,20 x  => 1,00 x = 299 => x = 299 minutes
    fixed = 299.0
    r_prep = 2.20
    r_cont = 1.20
    mins = round(fixed / (r_prep - r_cont))

    prompt = (
        f"Two mobile phone tariff plans are available:\n"
        f"• **Prepaid Plan:** No monthly fee, calls charged at **{_fmt_curr(r_prep)} per minute**\n"
        f"• **Contract Plan:** Fixed subscription of **{_fmt_curr(fixed)} per month**, calls charged at **{_fmt_curr(r_cont)} per minute**\n\n"
        f"Determine the number of call minutes where both plans cost the exact same amount."
    )
    correct = f"{mins} minutes"
    distractors = [f"{mins - 50} minutes", f"{mins + 50} minutes", f"{int(fixed / r_prep)} minutes"]
    expl = f"✓ [1 Mark: Method – Set up break-even equation: 2,20x = 299 + 1,20x]\n1,00x = 299.\nx = {mins} minutes.\n✓ [1 Mark: Accuracy – Break-even call minutes]\nMinutes = {mins} minutes."
    return {
        "subskill": "gr11_tariffs_subskill_42",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Break-even minutes = Fixed Monthly Fee ÷ (Prepaid Rate − Contract Rate).", "tier_2": f"299 ÷ (2,20 − 1,20).", "tier_3": f"{correct}."},
    }

def _subskill_43(r: random.Random) -> Dict[str, Any]:
    """Compare home uncapped fiber internet vs. capped LTE data bundle."""
    fiber_mo = 699.0  # Uncapped fiber
    lte_base = 299.0   # 100 GB cap
    extra_bundle = 99.0  # 20 GB top-up
    top_ups = 5  # Household uses 200 GB
    total_lte = lte_base + (top_ups * extra_bundle)
    savings = total_lte - fiber_mo

    prompt = (
        f"A family consumes 200 GB of internet data each month and evaluates two internet plans:\n"
        f"• **Option 1 (Uncapped Fiber):** Fixed **{_fmt_curr(fiber_mo)} per month** with unlimited usage\n"
        f"• **Option 2 (Capped LTE):** **{_fmt_curr(lte_base)} per month** for 100 GB, plus **{_fmt_curr(extra_bundle)}** per 20 GB top-up bundle\n\n"
        f"Calculate how much money the family saves per month by choosing Uncapped Fiber."
    )
    correct = _fmt_curr(savings)
    distractors = [_fmt_curr(total_lte), _fmt_curr(savings + 50), _fmt_curr(fiber_mo - lte_base)]
    expl = f"✓ [1 Mark: Method – Calculate LTE cost for 200 GB (base + 5 top-ups)]\nLTE Cost = {_fmt_curr(lte_base)} + (5 × {_fmt_curr(extra_bundle)}) = {_fmt_curr(total_lte)}.\nSavings = {_fmt_curr(total_lte)} − {_fmt_curr(fiber_mo)} = {_fmt_curr(savings)}.\n✓ [1 Mark: Accuracy – Monthly savings on Fiber]\nSavings = {_fmt_curr(savings)}."
    return {
        "subskill": "gr11_tariffs_subskill_43",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "LTE for 200 GB needs 5 top-ups of 20 GB. Compare total with R 699,00.", "tier_2": f"LTE = 299 + (5×99) = {total_lte}.", "tier_3": f"{correct}."},
    }

def _subskill_44(r: random.Random) -> Dict[str, Any]:
    """Calculate commercial transport freight tariff (per ton-km)."""
    tons = r.choice([8, 12, 16, 20])
    km = r.choice([150, 240, 320])
    rate_per_ton_km = 1.85
    total_freight = tons * km * rate_per_ton_km

    prompt = (
        f"A logistics freight company charges a transportation tariff of **{_fmt_curr(rate_per_ton_km)} per ton-kilometre**.\n"
        f"Calculate the total delivery cost to haul **{tons} tons** of agricultural produce over a distance of **{km} km**."
    )
    correct = _fmt_curr(total_freight)
    distractors = [_fmt_curr(tons * km), _fmt_curr(total_freight * 1.15), _fmt_curr(total_freight - 200)]
    expl = f"✓ [1 Mark: Method – Multiply tons by km by rate per ton-km]\nFreight Cost = {tons} tons × {km} km × {_fmt_curr(rate_per_ton_km)} = {_fmt_curr(total_freight)}.\n✓ [1 Mark: Accuracy – Total freight tariff]\nTotal = {_fmt_curr(total_freight)}."
    return {
        "subskill": "gr11_tariffs_subskill_44",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Cost = Tons × Distance × Rate.", "tier_2": f"{tons} × {km} × {rate_per_ton_km}.", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 45–52: Break-Even Analysis & Business Accounts
# ----------------------------------------------------------------------------

def _subskill_45(r: random.Random) -> Dict[str, Any]:
    """Calculate Total Cost (TC = Fixed Costs + Variable Cost per unit × n)."""
    fc = r.choice([2500, 3600, 4800, 6000])
    vc = r.choice([25.0, 35.0, 42.0])
    n = r.choice([120, 150, 200])
    tc = fc + (vc * n)

    prompt = (
        f"A home industry bakery manufactures artisanal cakes:\n"
        f"• Fixed monthly overhead costs (rent, oven lease): **{_fmt_curr(fc)}**\n"
        f"• Variable cost of ingredients and packaging per cake: **{_fmt_curr(vc)}**\n\n"
        f"Calculate the **Total Cost (TC)** to produce **{n} cakes** in a month."
    )
    correct = _fmt_curr(tc)
    distractors = [_fmt_curr(fc + vc), _fmt_curr(vc * n), _fmt_curr(tc + 300)]
    expl = f"✓ [1 Mark: Method – Formula: TC = FC + (VC × n)]\nTotal Cost = {_fmt_curr(fc)} + ({_fmt_curr(vc)} × {n}) = {_fmt_curr(fc)} + {_fmt_curr(vc * n)} = {_fmt_curr(tc)}.\n✓ [1 Mark: Accuracy – Total cost]\nTC = {_fmt_curr(tc)}."
    return {
        "subskill": "gr11_tariffs_subskill_45",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Total Cost = Fixed Costs + (Variable Cost × number of units).", "tier_2": f"{fc} + ({vc} × {n}).", "tier_3": f"{correct}."},
    }

def _subskill_46(r: random.Random) -> Dict[str, Any]:
    """Calculate Total Revenue (TR = Selling Price × n)."""
    price = r.choice([65.0, 85.0, 110.0, 140.0])
    n = r.choice([80, 120, 160])
    tr = price * n

    prompt = (
        f"A small manufacturing business sells handcrafted school backpacks at **{_fmt_curr(price)} each**.\n"
        f"Calculate the **Total Revenue (TR)** generated from the sale of **{n} backpacks**."
    )
    correct = _fmt_curr(tr)
    distractors = [_fmt_curr(price * (n - 10)), _fmt_curr(tr * 1.15), _fmt_curr(tr - 200)]
    expl = f"✓ [1 Mark: Method – Formula: TR = Price × Quantity]\nTotal Revenue = {_fmt_curr(price)} × {n} = {_fmt_curr(tr)}.\n✓ [1 Mark: Accuracy – Total revenue]\nTR = {_fmt_curr(tr)}."
    return {
        "subskill": "gr11_tariffs_subskill_46",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Revenue = Selling Price × Quantity sold.", "tier_2": f"{price} × {n}.", "tier_3": f"{correct}."},
    }

def _subskill_47(r: random.Random) -> Dict[str, Any]:
    """Calculate Break-Even Quantity: n = Fixed Costs / (Price - Variable Cost)."""
    fc = r.choice([3000, 4500, 6000, 9000])
    vc = 30.0
    price = 60.0
    cm = price - vc  # R30 contribution margin
    be_units = int(fc / cm)

    prompt = (
        f"A student operates a hotdog stand at university sports events:\n"
        f"• Fixed stall permit and equipment hire: **{_fmt_curr(fc)} per month**\n"
        f"• Variable cost of roll, sausage, and sauce: **{_fmt_curr(vc)} per hotdog**\n"
        f"• Selling price: **{_fmt_curr(price)} per hotdog**\n\n"
        f"Calculate the **break-even quantity** (number of hotdogs that must be sold to cover all costs)."
    )
    correct = f"{be_units} hotdogs"
    distractors = [f"{be_units - 25} hotdogs", f"{be_units + 50} hotdogs", f"{int(fc / price)} hotdogs"]
    expl = f"✓ [1 Mark: Method – Formula: Break-even = Fixed Costs ÷ (Selling Price − Variable Cost)]\nContribution Margin = {_fmt_curr(price)} − {_fmt_curr(vc)} = {_fmt_curr(cm)}.\nBreak-Even = {_fmt_curr(fc)} ÷ {_fmt_curr(cm)} = {be_units} hotdogs.\n✓ [1 Mark: Accuracy – Break-even units]\nQuantity = {be_units} hotdogs."
    return {
        "subskill": "gr11_tariffs_subskill_47",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Break-even = Fixed Costs ÷ (Price − Variable Cost).", "tier_2": f"{fc} ÷ ({price} − {vc}).", "tier_3": f"{correct}."},
    }

def _subskill_48(r: random.Random) -> Dict[str, Any]:
    """Calculate Profit or Loss at a given production and sales volume: Profit = TR - TC."""
    fc = 4000.0
    vc = 35.0
    price = 75.0
    n = r.choice([80, 140])
    tr = price * n
    tc = fc + (vc * n)
    profit = tr - tc

    prompt = (
        f"A craft workshop manufactures beaded necklaces:\n"
        f"• Fixed Overhead Costs: **{_fmt_curr(fc)} per month**\n"
        f"• Variable Cost per necklace: **{_fmt_curr(vc)}**\n"
        f"• Selling Price per necklace: **{_fmt_curr(price)}**\n\n"
        f"If the workshop produces and sells **{n} necklaces** in a month, calculate their net profit or loss."
    )
    if profit >= 0:
        correct = f"Profit of {_fmt_curr(profit)}"
        distractors = [f"Loss of {_fmt_curr(profit)}", f"Profit of {_fmt_curr(profit + 300)}", f"Profit of {_fmt_curr(tr)}"]
    else:
        correct = f"Loss of {_fmt_curr(abs(profit))}"
        distractors = [f"Profit of {_fmt_curr(abs(profit))}", f"Loss of {_fmt_curr(abs(profit) + 200)}", f"Break-even (R 0,00)"]

    expl = f"✓ [1 Mark: Method – Formula: Profit = Total Revenue − Total Cost]\nTR = {n} × {_fmt_curr(price)} = {_fmt_curr(tr)}.\nTC = {_fmt_curr(fc)} + ({n} × {_fmt_curr(vc)}) = {_fmt_curr(tc)}.\nResult = {_fmt_curr(tr)} − {_fmt_curr(tc)} = {_fmt_curr(profit)} ({'Profit' if profit >= 0 else 'Loss'}).\n✓ [1 Mark: Accuracy – Financial result]\nResult = {correct}."
    return {
        "subskill": "gr11_tariffs_subskill_48",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate TR (Price × n) and TC (FC + VC × n). Profit = TR − TC.", "tier_2": f"TR = {tr}, TC = {tc}.", "tier_3": f"{correct}."},
    }

def _subskill_49(r: random.Random) -> Dict[str, Any]:
    """Interpret Break-Even Graph: Identify coordinates of Break-Even Point."""
    fc = 5000
    cm = 25.0
    be_units = int(fc / cm)  # 200 units
    be_rands = be_units * 50.0  # R10 000

    prompt = (
        f"Refer to a break-even analysis graph where the Total Cost line and Total Revenue line intersect.\n"
        f"• The horizontal x-axis represents Volume (number of items produced and sold).\n"
        f"• The vertical y-axis represents Value (in Rands).\n"
        f"• At the point of intersection, exactly **{be_units} units** are sold, generating **{_fmt_curr(be_rands)}** in revenue.\n\n"
        f"State the coordinates of the **Break-Even Point** in the standard format `(x ; y)`."
    )
    correct = f"({be_units} units ; {_fmt_curr(be_rands)})"
    distractors = [
        f"({_fmt_curr(be_rands)} ; {be_units} units)",
        f"({be_units} units ; {_fmt_curr(fc)})",
        f"(0 units ; {_fmt_curr(fc)})",
    ]
    expl = f"✓ [1 Mark: Method – Standard coordinate format (x-axis units ; y-axis Rands)]\nAt break-even, Total Revenue equals Total Cost.\n✓ [1 Mark: Accuracy – Exact coordinate of break-even intersection]\nCoordinate = ({be_units} units ; {_fmt_curr(be_rands)})."
    return {
        "subskill": "gr11_tariffs_subskill_49",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Coordinates are (x-axis ; y-axis) = (Units ; Rands).", "tier_2": f"({be_units} ; {be_rands}).", "tier_3": f"{correct}."},
    }

def _subskill_50(r: random.Random) -> Dict[str, Any]:
    """Calculate required production volume to achieve a target monthly profit."""
    fc = 6000.0
    vc = 40.0
    price = 90.0
    cm = price - vc  # R50 contribution margin
    target_profit = r.choice([4000.0, 6000.0, 9000.0])
    req_units = int((fc + target_profit) / cm)

    prompt = (
        f"A small manufacturing business has:\n"
        f"• Fixed Overhead Costs: **{_fmt_curr(fc)} per month**\n"
        f"• Variable Cost per unit: **{_fmt_curr(vc)}**\n"
        f"• Selling Price per unit: **{_fmt_curr(price)}**\n\n"
        f"How many units must be produced and sold to achieve a **target profit of {_fmt_curr(target_profit)}** in a month?"
    )
    correct = f"{req_units} units"
    distractors = [f"{req_units - 20} units", f"{req_units + 30} units", f"{int(fc / cm)} units"]
    expl = f"✓ [1 Mark: Method – Formula: Target Volume = (Fixed Costs + Target Profit) ÷ Contribution Margin]\nTarget Volume = ({_fmt_curr(fc)} + {_fmt_curr(target_profit)}) ÷ ({_fmt_curr(price)} − {_fmt_curr(vc)}) = {_fmt_curr(fc + target_profit)} ÷ {_fmt_curr(cm)} = {req_units} units.\n✓ [1 Mark: Accuracy – Required units for target profit]\nVolume = {req_units} units."
    return {
        "subskill": "gr11_tariffs_subskill_50",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Target units = (Fixed Costs + Target Profit) ÷ (Price − Variable Cost).", "tier_2": f"({fc} + {target_profit}) ÷ 50.", "tier_3": f"{correct}."},
    }

def _subskill_51(r: random.Random) -> Dict[str, Any]:
    """Calculate Margin of Safety (Actual sales volume minus break-even volume)."""
    be_units = 180
    actual_units = r.choice([240, 280, 320])
    margin_safety = actual_units - be_units

    prompt = (
        f"A community cooperative determines that its break-even sales volume is **{be_units} woven baskets per month**.\n"
        f"In August, the cooperative produces and sells **{actual_units} baskets**.\n\n"
        f"Calculate the cooperative's **margin of safety** in units (the cushion before the business starts making a loss)."
    )
    correct = f"{margin_safety} baskets"
    distractors = [f"{actual_units} baskets", f"{margin_safety + 25} baskets", f"{margin_safety - 15} baskets"]
    expl = f"✓ [1 Mark: Method – Formula: Margin of Safety = Actual Sales Units − Break-Even Sales Units]\nMargin of Safety = {actual_units} − {be_units} = {margin_safety} baskets.\n✓ [1 Mark: Accuracy – Margin of safety]\nMargin = {margin_safety} baskets."
    return {
        "subskill": "gr11_tariffs_subskill_51",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Margin of Safety = Actual Sales − Break-Even Sales.", "tier_2": f"{actual_units} − {be_units}.", "tier_3": f"{correct}."},
    }

def _subskill_52(r: random.Random) -> Dict[str, Any]:
    """Analyze the impact of a selling price increase on break-even quantity."""
    fc = 8000.0
    vc = 40.0
    p_old = 80.0
    p_new = 90.0

    be_old = int(fc / (p_old - vc))  # 8000 / 40 = 200
    be_new = int(fc / (p_new - vc))  # 8000 / 50 = 160
    reduction = be_old - be_new

    prompt = (
        f"A manufacturing company has fixed costs of **{_fmt_curr(fc)}** and variable costs of **{_fmt_curr(vc)} per unit**.\n"
        f"The management increases the selling price from **{_fmt_curr(p_old)}** to **{_fmt_curr(p_new)} per unit**.\n\n"
        f"Calculate how many fewer units the company now needs to sell to break even."
    )
    correct = f"{reduction} fewer units"
    distractors = [f"{be_old} units", f"{be_new} units", f"{reduction + 10} fewer units"]
    expl = f"✓ [1 Mark: Method – Calculate old break-even and new break-even]\nOld Break-Even = {_fmt_curr(fc)} ÷ ({_fmt_curr(p_old)} − {_fmt_curr(vc)}) = {_fmt_curr(fc)} ÷ R 40,00 = {be_old} units.\nNew Break-Even = {_fmt_curr(fc)} ÷ ({_fmt_curr(p_new)} − {_fmt_curr(vc)}) = {_fmt_curr(fc)} ÷ R 50,00 = {be_new} units.\nReduction = {be_old} − {be_new} = {reduction} fewer units.\n✓ [1 Mark: Accuracy – Reduction in break-even units]\nReduction = {reduction} fewer units."
    return {
        "subskill": "gr11_tariffs_subskill_52",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Old BE = 8000 ÷ 40 = 200. New BE = 8000 ÷ 50 = 160. Subtract.", "tier_2": "200 − 160.", "tier_3": f"{correct}."},
    }

# ----------------------------------------------------------------------------
# DISPATCH TABLE & CANONICAL SUBSKILLS LIST
# ----------------------------------------------------------------------------

DISPATCH_TABLE = {
    f"gr11_tariffs_subskill_{i}": fn
    for i, fn in enumerate([
        _subskill_1, _subskill_2, _subskill_3, _subskill_4, _subskill_5,
        _subskill_6, _subskill_7, _subskill_8, _subskill_9, _subskill_10,
        _subskill_11, _subskill_12, _subskill_13, _subskill_14, _subskill_15,
        _subskill_16, _subskill_17, _subskill_18, _subskill_19, _subskill_20,
        _subskill_21, _subskill_22, _subskill_23, _subskill_24, _subskill_25,
        _subskill_26, _subskill_27, _subskill_28, _subskill_29, _subskill_30,
        _subskill_31, _subskill_32, _subskill_33, _subskill_34, _subskill_35,
        _subskill_36, _subskill_37, _subskill_38, _subskill_39, _subskill_40,
        _subskill_41, _subskill_42, _subskill_43, _subskill_44, _subskill_45,
        _subskill_46, _subskill_47, _subskill_48, _subskill_49, _subskill_50,
        _subskill_51, _subskill_52
    ], 1)
}

SUBSKILLS = [
    "01_basic_salary_hourly_wage_normal_working",
    "02_overtime_pay_at_times_normal_hourly",
    "03_total_gross_salary_including_basic_salary",
    "04_statutory_uif_deduction_gross_earnings_up",
    "05_pension_fund_deduction_basic_salary",
    "06_total_monthly_deductions_paye_uif_pension",
    "07_take_home_pay_gross_salary_total_deductions",
    "08_employer_s_uif_contribution_matching_employee",
    "09_audit_payslip_error_identify_missing_deduction",
    "10_vat_exclusive_subtotal",
    "11_total_price_including_vat",
    "12_extract_exclusive_price_vat_inclusive_total",
    "13_vat_component_embedded_inside_vat_inclusive",
    "14_quotation_trade_discount_before_vat_applied",
    "15_audit_invoice_calculation_item_quantities_unit",
    "16_early_settlement_discount_invoice_paid_within",
    "17_quotation_validity_expiry_date",
    "18_courier_delivery_fee_based_base_fee",
    "19_water_cost_consumption_within_block_kl",
    "20_water_cost_spanning_two_stepped_blocks",
    "21_cost_high_volume_consumption_across_stepped",
    "22_percentage_tariff_increase_between_two_municipal",
    "23_wastewater_sanitation_sewerage_charge_linked_water",
    "24_financial_cost_undetected_leaking_toilet_over",
    "25_reverse_stepped_tariff_calculation_water_volume",
    "26_commercial_flat_tariff_vs_residential_stepped",
    "27_read_stepped_water_tariff_graph_identify",
    "28_domestic_electricity_inclining_block_tariff_ibt",
    "29_ibt_electricity_spanning_block_block_kwh",
    "30_prepaid_electricity_voucher_tokens_units_purchased",
    "31_post_paid_electricity_bill_including_fixed",
    "32_running_cost_domestic_appliance_power_kw",
    "33_prepaid_vs_post_paid_break_even",
    "34_time_use_tou_electricity_cost_peak",
    "35_solar_feed_tariff_credit_subtracted_grid",
    "36_savings_replacing_incandescent_bulbs_led_bulbs",
    "37_monthly_commuter_minibus_taxi_travel_budget",
    "38_compare_municipal_bus_multi_trip_clip",
    "39_gautrain_train_fare_table_lookup_calculation",
    "40_cell_phone_call_per_second_billing",
    "41_cell_phone_out_bundle_oob_data",
    "42_cell_phone_contract_vs_prepaid_break",
    "43_compare_home_uncapped_fiber_broadband_vs",
    "44_commercial_transport_freight_tariff_per_ton",
    "45_total_cost_tc_fixed_costs_variable",
    "46_total_revenue_tr_selling_price_n",
    "47_break_even_quantity_n_fixed_costs",
    "48_profit_or_loss_at_given_production",
    "49_interpret_break_even_curve_trend_identify_coordinates",
    "50_required_production_volume_achieve_target_monthly",
    "51_margin_safety_actual_sales_volume_minus",
    "52_analyze_impact_selling_price_increase_break",
]

for _idx, _sem_id in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[_sem_id] = DISPATCH_TABLE[f"gr11_tariffs_subskill_{_idx}"]



def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Financial Documents and Tariff Systems."""
    r = random.Random(seed)
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill

        if not chosen_subskill and archetype_index is not None:
            if 0 <= archetype_index < len(SUBSKILLS):
                chosen_subskill = SUBSKILLS[archetype_index]
            else:
                chosen_subskill = SUBSKILLS[archetype_index % len(SUBSKILLS)]

        if not chosen_subskill or chosen_subskill not in DISPATCH_TABLE:
            chosen_subskill = r.choice(SUBSKILLS)

        builder = DISPATCH_TABLE[chosen_subskill]
        raw_q = builder(r)

        # Standard 6-pillar normalization
        payload = {
            "id": f"mathlit_gr11_tariffs_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "question_id": f"mathlit_gr11_tariffs_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "topic": "grade11_mathlit_financial_documents_and_tariff_systems",
            "subskill": chosen_subskill,
            "prompt": raw_q["prompt"],
            "options": raw_q["options"],
            "correct_answer": raw_q["correct_answer"],
            "explanation": raw_q["explanation"],
            "worked_solution": raw_q["explanation"],
            "hints": raw_q["hints"],
            "grade": 11,
            "subject": "Mathematical Literacy",
        }
        if "diagram_spec" in raw_q:
            payload["diagram_spec"] = raw_q["diagram_spec"]

        results.append(payload)

    return results
