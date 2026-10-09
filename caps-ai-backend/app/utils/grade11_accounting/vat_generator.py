"""Grade 11 Accounting — Term 1: Value Added Tax (VAT) Generator.
Deterministic 6-pillar CAPS question generator covering:
- Standard rate (15%), zero-rated, and exempt supplies classification.
- Calculations: VAT-inclusive, VAT-exclusive, and VAT amount (15/115 and 15/100).
- VAT Control Account (Input VAT on debit vs Output VAT on credit, net amount payable to / receivable from SARS).
- Adjustments to VAT: Bad debts, returns, discounts, personal drawings.
- Ethics & Internal Controls: SARS compliance, fraudulent input claims, record keeping.

Strictly adheres to:
- Rule 20: Term & Calendar Metadata (Term 1, caps_weight_percent: 15)
- Rule 21: Deconstructibility (mode="compound" | "elementary_*")
- Rule 22: Misconception taxonomy (input_output_inversion, net_vs_gross_confusion, incorrect_fraction_on_inclusive)
- Rule 23: Teacher-editable marking schema
- Rule 24: Deterministic 3-tier pre-baked hints
- Rule 26b: Zero-Meta-Curriculum Invariant
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

VAT_RATE = 0.15

_BUSINESSES = [
    "Maluleke & Partners", "Ndlovu & Steyn Traders", "Bester & Khumalo Dealers",
    "Apex Wholesale Partnerships", "Zondi & Naidoo Supplies", "Ubuntu Traders",
    "Kgalagadi Merchants", "Protea Commercial Partners", "Dlamini & Pillay Enterprise"
]

_ZERO_RATED_ITEMS = [
    "Brown bread", "Maize meal", "Fresh milk", "Samp", "Mealie rice",
    "Dried beans", "Lentils", "Pilchards in tins", "Fresh fruit and vegetables",
    "Illuminating paraffin"
]

_EXEMPT_ITEMS = [
    "Public transport by bus or minibus taxi", "Rail commuter transport",
    "Long-term residential rental accommodation", "Educational services provided by a school",
    "Life insurance premiums", "Interest paid on bank loans"
]

_STANDARD_RATED_ITEMS = [
    "Stationery for office use", "Trading inventory (clothing)", "Motor vehicle repairs",
    "Telephone and internet account", "Audit and legal fees", "Advertising brochures",
    "Packing material", "Cleaning detergents"
]


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _fmt_money(x: float) -> str:
    return f"R {x:,.2f}".replace(",", " ")


# ============================================================================
# ARCHETYPE 1: VAT CONTROL ACCOUNT & NET SARS POSITION (Compound Exam Style)
# ============================================================================

def _gen_vat_control_account_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    business = r.choice(_BUSINESSES)
    month = r.choice(["March", "April", "May", "August", "September", "October"])
    year = r.choice([2024, 2025, 2026])

    # Realistic amounts
    sales_excl = r.choice([120000, 150000, 180000, 210000, 240000])
    output_vat_sales = _round_money(sales_excl * VAT_RATE)
    
    purchases_excl = r.choice([70000, 85000, 95000, 110000, 130000])
    input_vat_purchases = _round_money(purchases_excl * VAT_RATE)
    
    operating_expenses_incl = r.choice([16100, 20700, 25300, 29900])
    input_vat_expenses = _round_money(operating_expenses_incl * 15 / 115)
    
    bad_debt_incl = r.choice([2300, 3450, 4600, 5750])
    input_vat_bad_debt = _round_money(bad_debt_incl * 15 / 115)
    
    drawings_cost_excl = r.choice([3000, 4500, 6000])
    output_vat_drawings = _round_money(drawings_cost_excl * VAT_RATE)

    total_output_vat = _round_money(output_vat_sales + output_vat_drawings)
    total_input_vat = _round_money(input_vat_purchases + input_vat_expenses + input_vat_bad_debt)
    
    net_position = _round_money(total_output_vat - total_input_vat)
    is_payable = net_position > 0
    sars_status = "payable to SARS (Current Liability)" if is_payable else "receivable / refundable from SARS (Current Asset)"

    if mode == "elementary_control_account" or mode == "elementary":
        prompt = (
            f"In the books of {business} for {month} {year}:\n"
            f"- Total Output VAT on sales and drawings is {_fmt_money(total_output_vat)}.\n"
            f"- Total Input VAT on purchases and operating expenses is {_fmt_money(total_input_vat)}.\n\n"
            f"Calculate the net amount payable to or receivable from SARS and state whether it is a current asset or current liability."
        )
        sample = (
            f"Net VAT Position = Output VAT - Input VAT\n"
            f"= {_fmt_money(total_output_vat)} - {_fmt_money(total_input_vat)}\n"
            f"= {_fmt_money(abs(net_position))} ({sars_status})"
        )
        marks = 4
        schema = {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Difference calculation (Output VAT - Input VAT)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct classification as {sars_status}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "tier_1": "Compare Output VAT (collected on behalf of SARS) with Input VAT (paid on business expenses).",
            "tier_2": "If Output VAT > Input VAT, the business owes money to SARS (payable, liability). If Input VAT > Output VAT, SARS owes a refund (receivable, asset).",
            "tier_3": f"Net amount = {_fmt_money(total_output_vat)} - {_fmt_money(total_input_vat)} = {_fmt_money(abs(net_position))} {sars_status}.",
        }
    else:
        prompt = (
            f"You are provided with the following transactions of {business} for the two-month VAT period ended {month} {year}. "
            f"All standard-rated transactions are subject to VAT at 15%.\n\n"
            f"1. Total credit and cash sales of merchandise (excluding VAT): {_fmt_money(sales_excl)}.\n"
            f"2. Merchandise purchased from VAT-registered suppliers (excluding VAT): {_fmt_money(purchases_excl)}.\n"
            f"3. Operating expenses paid by cheque, all supporting tax invoices verified (VAT inclusive): {_fmt_money(operating_expenses_incl)}.\n"
            f"4. An amount of {_fmt_money(bad_debt_incl)} (VAT inclusive) was written off as irrecoverable after a debtor was declared insolvent.\n"
            f"5. A partner withdrew merchandise for personal use with a cost price of {_fmt_money(drawings_cost_excl)} (excluding VAT). No entry has yet been made.\n\n"
            f"REQUIRED:\n"
            f"(a) Calculate the total Output VAT for the period.\n"
            f"(b) Calculate the total Input VAT claimable for the period.\n"
            f"(c) Determine the final amount payable to or receivable from SARS on {month} {year}.\n"
            f"(d) State where the net balance of the VAT Control Account will be shown on the Statement of Financial Position."
        )
        sample = (
            f"(a) Output VAT:\n"
            f"    - Sales: {_fmt_money(sales_excl)} x 15% = {_fmt_money(output_vat_sales)}\n"
            f"    - Drawings: {_fmt_money(drawings_cost_excl)} x 15% = {_fmt_money(output_vat_drawings)}\n"
            f"    Total Output VAT = {_fmt_money(total_output_vat)}\n\n"
            f"(b) Input VAT:\n"
            f"    - Purchases: {_fmt_money(purchases_excl)} x 15% = {_fmt_money(input_vat_purchases)}\n"
            f"    - Operating expenses: {_fmt_money(operating_expenses_incl)} x 15/115 = {_fmt_money(input_vat_expenses)}\n"
            f"    - Bad debts adjustment: {_fmt_money(bad_debt_incl)} x 15/115 = {_fmt_money(input_vat_bad_debt)}\n"
            f"    Total Input VAT = {_fmt_money(total_input_vat)}\n\n"
            f"(c) Net VAT Position: {_fmt_money(total_output_vat)} - {_fmt_money(total_input_vat)} = {_fmt_money(abs(net_position))} ({sars_status})\n\n"
            f"(d) Statement of Financial Position: Trade and other payables under Current Liabilities (if payable) or Trade and other receivables under Current Assets (if receivable)."
        )
        marks = 12
        schema = {
            "total_marks": 12,
            "marking_points": [
                {"id": "mp_1", "desc": "Output VAT on sales", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Output VAT on drawings", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Input VAT on purchases", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Input VAT on expenses (15/115)", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": "Input VAT adjustment on bad debts (15/115)", "marks": 2, "editable": True},
                {"id": "mp_6", "desc": "Net VAT position and Balance Sheet disclosure", "marks": 2, "editable": True},
            ],
            "deductions": [
                {"rule": "inverted_input_output", "penalty": -2}
            ],
            "carry_forward_rule": "consequential_accuracy",
        }
        hints = {
            "tier_1": "Separate all transactions into Output VAT (sales and drawings) and Input VAT (purchases, expenses, bad debts adjustment).",
            "tier_2": "For VAT-exclusive amounts multiply by 15/100 (0.15). For VAT-inclusive amounts multiply by 15/115.",
            "tier_3": f"Output VAT = {_fmt_money(total_output_vat)}. Input VAT = {_fmt_money(total_input_vat)}. Net = {_fmt_money(abs(net_position))} {sars_status}.",
        }

    return {
        "id": _make_id("acct11_vat_control"),
        "topic": "grade11_accounting_vat",
        "subskill": "vat_control_account_and_sars_position",
        "learning_objective_id": "acct11_vat_control_sars",
        "prompt": prompt,
        "sample_answer": sample,
        "correct_answer": f"{_fmt_money(abs(net_position))} {sars_status}",
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": [
            "net_vs_gross_confusion",
            "input_output_inversion",
            "incorrect_fraction_on_inclusive"
        ],
        "keywords": ["VAT", "Output VAT", "Input VAT", "SARS", "VAT Control", "15%"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 10 if mode == "compound" else 4,
        "mode": mode,
        "difficulty": "medium",
        "marks": marks,
    }


# ============================================================================
# ARCHETYPE 2: VAT CALCULATIONS (Inclusive, Exclusive, Fraction Rules)
# ============================================================================

def _gen_vat_calculations_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    business = r.choice(_BUSINESSES)
    
    # 3 distinct calculation rows
    # Row 1: Excl given -> find VAT and Incl
    excl_1 = r.choice([12000, 18500, 24000, 36000, 45000])
    vat_1 = _round_money(excl_1 * 0.15)
    incl_1 = _round_money(excl_1 + vat_1)

    # Row 2: Incl given -> find Excl and VAT
    excl_2_base = r.choice([8000, 14000, 22000, 28000, 52000])
    incl_2 = _round_money(excl_2_base * 1.15)
    vat_2 = _round_money(incl_2 * 15 / 115)
    excl_2 = _round_money(incl_2 - vat_2)

    # Row 3: VAT amount given -> find Excl and Incl
    vat_3 = r.choice([1500, 2250, 3750, 4500, 6750])
    excl_3 = _round_money(vat_3 / 0.15)
    incl_3 = _round_money(excl_3 + vat_3)

    prompt = (
        f"The bookkeeper of {business} needs to complete the VAT reconciliation table for tax audit purposes. "
        f"Calculate the missing amounts marked (A), (B), (C), and (D). The standard VAT rate is 15%.\n\n"
        f"| Transaction / Invoice | Exclusive Amount (100%) | VAT Amount (15%) | Inclusive Amount (115%) |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| 1. Office Equipment | {_fmt_money(excl_1)} | (A) | {_fmt_money(incl_1)} |\n"
        f"| 2. Stock Purchase | (B) | (C) | {_fmt_money(incl_2)} |\n"
        f"| 3. Commercial Services | {_fmt_money(excl_3)} | {_fmt_money(vat_3)} | (D) |\n\n"
        f"REQUIRED:\n"
        f"Show all working for (A), (B), (C), and (D)."
    )

    sample = (
        f"(A) VAT on Office Equipment = {_fmt_money(excl_1)} x 15% = {_fmt_money(vat_1)}\n"
        f"(B) Exclusive Amount for Stock Purchase = {_fmt_money(incl_2)} x 100/115 = {_fmt_money(excl_2)}\n"
        f"(C) VAT on Stock Purchase = {_fmt_money(incl_2)} x 15/115 = {_fmt_money(vat_2)}\n"
        f"(D) Inclusive Amount for Services = {_fmt_money(excl_3)} + {_fmt_money(vat_3)} = {_fmt_money(incl_3)}"
    )

    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp_a", "desc": "Calculation of (A) VAT from exclusive", "marks": 2, "editable": True},
            {"id": "mp_b", "desc": "Calculation of (B) Exclusive from inclusive (x 100/115)", "marks": 2, "editable": True},
            {"id": "mp_c", "desc": "Calculation of (C) VAT from inclusive (x 15/115)", "marks": 2, "editable": True},
            {"id": "mp_d", "desc": "Calculation of (D) Inclusive from exclusive + VAT", "marks": 2, "editable": True},
        ],
        "deductions": [
            {"rule": "used_15_over_100_on_inclusive", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Identify whether the given figure represents 100% (exclusive) or 115% (inclusive).",
        "tier_2": "To find VAT from an inclusive figure, use: Inclusive x 15/115. Never multiply an inclusive figure by 15% directly.",
        "tier_3": f"(A) = {_fmt_money(vat_1)}; (B) = {_fmt_money(excl_2)}; (C) = {_fmt_money(vat_2)}; (D) = {_fmt_money(incl_3)}.",
    }

    return {
        "id": _make_id("acct11_vat_calc"),
        "topic": "grade11_accounting_vat",
        "subskill": "vat_inclusive_exclusive_calculations",
        "learning_objective_id": "acct11_vat_calculations",
        "prompt": prompt,
        "sample_answer": sample,
        "correct_answer": f"(A) {_fmt_money(vat_1)}, (B) {_fmt_money(excl_2)}, (C) {_fmt_money(vat_2)}, (D) {_fmt_money(incl_3)}",
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": [
            "incorrect_fraction_on_inclusive",
            "net_vs_gross_confusion"
        ],
        "keywords": ["VAT", "Inclusive", "Exclusive", "15/115", "100/115"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "mode": mode,
        "difficulty": "medium",
        "marks": 8,
    }


# ============================================================================
# ARCHETYPE 3: SUPPLY CLASSIFICATION & VAT ETHICS
# ============================================================================

def _gen_vat_classification_ethics_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    business = r.choice(_BUSINESSES)
    zero_item = r.choice(_ZERO_RATED_ITEMS)
    exempt_item = r.choice(_EXEMPT_ITEMS)
    standard_item = r.choice(_STANDARD_RATED_ITEMS)

    prompt = (
        f"You are the senior accountant at {business}. Answer the following questions relating to Value Added Tax:\n\n"
        f"1. Classify each of the following supplies as **Standard-rated (15%)**, **Zero-rated (0%)**, or **Exempt**:\n"
        f"   (a) Sale of {zero_item}.\n"
        f"   (b) Long-term payment for {exempt_item}.\n"
        f"   (c) Purchase of {standard_item}.\n\n"
        f"2. Explain the fundamental economic difference between a **Zero-rated supply** and an **Exempt supply** "
        f"from the perspective of claiming Input VAT.\n\n"
        f"3. A partner at {business} purchased a luxury home entertainment system for their private residence "
        f"and instructed the accounts clerk to enter the invoice into the CPJ and claim Input VAT. "
        f"Explain why this practice is unethical and illegal, and state the potential consequence from SARS."
    )

    sample = (
        f"1. Classification:\n"
        f"   (a) {zero_item}: Zero-rated (0% VAT)\n"
        f"   (b) {exempt_item}: Exempt (No VAT charged)\n"
        f"   (c) {standard_item}: Standard-rated (15% VAT)\n\n"
        f"2. Economic difference:\n"
        f"   - On Zero-rated supplies, VAT is charged at 0%, but the registered vendor CAN claim back Input VAT paid on goods/services used to produce them.\n"
        f"   - On Exempt supplies, no VAT is charged, and the vendor CANNOT claim any Input VAT incurred in providing the exempt service.\n\n"
        f"3. Ethics & SARS consequences:\n"
        f"   - It is fraudulent/tax evasion to claim Input VAT on private personal expenditure because Input VAT is strictly deductible only for expenses incurred in the course of making taxable business supplies.\n"
        f"   - Consequences: SARS penalties (up to 200% understatement penalty), interest on overdue tax, and possible criminal prosecution."
    )

    schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp_class_a", "desc": f"Zero-rated classification for {zero_item}", "marks": 1, "editable": True},
            {"id": "mp_class_b", "desc": f"Exempt classification for {exempt_item}", "marks": 1, "editable": True},
            {"id": "mp_class_c", "desc": f"Standard-rated classification for {standard_item}", "marks": 1, "editable": True},
            {"id": "mp_diff", "desc": "Difference in claiming Input VAT (allowed for zero-rated, prohibited for exempt)", "marks": 3, "editable": True},
            {"id": "mp_ethics", "desc": "Explanation of tax fraud / personal expenditure prohibition and SARS penalty", "marks": 3, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Zero-rated goods are basic foodstuffs to protect low-income households. Exempt supplies are specific public services and finance.",
        "tier_2": "Key distinction: Can a vendor claim Input VAT on purchases for zero-rated goods? Yes. For exempt goods? No.",
        "tier_3": f"Zero-rated: {zero_item}. Exempt: {exempt_item}. Standard: {standard_item}. Private purchases claimed as business VAT violate SARS tax law.",
    }

    return {
        "id": _make_id("acct11_vat_ethics"),
        "topic": "grade11_accounting_vat",
        "subskill": "vat_classification_and_ethics",
        "learning_objective_id": "acct11_vat_ethics_classification",
        "prompt": prompt,
        "sample_answer": sample,
        "correct_answer": f"Zero-rated: {zero_item}; Exempt: {exempt_item}; Standard: {standard_item}",
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": [
            "zero_rated_vs_exempt_confusion",
            "vat_fraud_misconception"
        ],
        "keywords": ["Zero-rated", "Exempt", "Standard-rated", "Input VAT", "Tax Fraud", "SARS"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "difficulty": "medium",
        "marks": 9,
    }


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def generate(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: str = "mixed",
    archetype: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Grade 11 Accounting Value Added Tax question."""
    r = _rng(seed)

    if archetype == "control_account" or subskill in ["control_account", "vat_control"]:
        return _gen_vat_control_account_question(r, mode=mode)
    elif archetype == "calculations" or subskill in ["calculations", "vat_calculations"]:
        return _gen_vat_calculations_question(r, mode=mode)
    elif archetype == "ethics" or subskill in ["classification", "ethics", "vat_ethics"]:
        return _gen_vat_classification_ethics_question(r, mode=mode)
    else:
        # Default distribution across all 3 archetypes
        choice = r.choice(["control", "calculations", "ethics"])
        if choice == "control":
            return _gen_vat_control_account_question(r, mode=mode)
        elif choice == "calculations":
            return _gen_vat_calculations_question(r, mode=mode)
        else:
            return _gen_vat_classification_ethics_question(r, mode=mode)
