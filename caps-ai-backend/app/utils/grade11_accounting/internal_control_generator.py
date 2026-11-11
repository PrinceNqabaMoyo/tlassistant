"""
Grade 11 Accounting: Internal Control and Internal Audit
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "cash_and_eft_internal_controls",
    "inventory_shortage_and_shrinkage_investigation",
    "fixed_asset_register_and_vehicle_controls",
    "debtors_and_creditors_control_procedures",
    "preventative_detective_corrective_controls_matrix",
    "internal_audit_sampling_and_verification",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_cash_and_eft_controls(r: random.Random) -> Dict[str, Any]:
    rec_receipts = r.randint(48, 82) * 1000
    banked = rec_receipts - r.randint(4, 9) * 1000
    missing = rec_receipts - banked

    headers = ["Cash & EFT Audit Verification", "Answer / Amount"]
    rows = [
        [f"Cash receipts per CRJ (R{rec_receipts:,}) less Deposits per Bank Statement (R{banked:,}) — Unbanked / Missing Cash (R)", "{r0_c1}"],
        ["Control over EFT payments to prevent single-clerk fraud (Dual Authorisation / Single Password)", "{r1_c1}"],
        ["Control over daily cash takings (Bank Daily & Split Receipting from Banking / Bank Monthly)", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": missing,
        "r1_c1": "Dual Authorisation",
        "r2_c1": "Bank Daily & Split Receipting from Banking",
    }
    worked = (
        f"**Cash & EFT Internal Controls**\n\n"
        f"- **Missing Cash**: `R{rec_receipts:,} - R{banked:,} = R{missing:,}`\n"
        f"- **EFT Control**: **Dual Authorisation** (one person captures the beneficiary/payment, a senior partner releases it with a two-factor OTP).\n"
        f"- **Cash Control**: **Bank Daily & Split Receipting from Banking**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "cash_and_eft_internal_controls",
        "question_text": "Complete the internal audit findings table for cash and EFT controls.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Compare total cash received against actual bank deposits to quantify cash shortages, and apply segregation of duties to EFT and banking.",
            "Calculate the difference in Row 1, then select the correct control from brackets in Rows 2 and 3.",
            worked,
        ),
    }


def _gen_inventory_shortage(r: random.Random) -> Dict[str, Any]:
    ledger_bal = r.randint(110, 175) * 1000
    unrec_drawings = r.randint(3, 6) * 1000
    expected_stock = ledger_bal - unrec_drawings
    physical_count = expected_stock - r.randint(5, 12) * 1000
    deficit = expected_stock - physical_count

    headers = ["Trading Stock Internal Audit Schedule", "Amount (R)"]
    rows = [
        ["Trading Stock balance per General Ledger before adjustments", f"R{ledger_bal:,}"],
        ["Less: Unrecorded stock taken by Partner for personal use (Drawings)", f"(R{unrec_drawings:,})"],
        ["Expected Trading Stock on hand after recording partner drawings", "{r2_c1}"],
        ["Actual physical stock count per stocktake sheets", f"R{physical_count:,}"],
        ["Trading Stock Deficit (shortage due to shrinkage/theft)", "{r4_c1}"],
    ]
    correct_map = {
        "r2_c1": expected_stock,
        "r4_c1": deficit,
    }
    worked = (
        f"**Inventory Shortage Audit Investigation**\n\n"
        f"- **Expected Stock after unrecorded drawings**: `R{ledger_bal:,} - R{unrec_drawings:,} = R{expected_stock:,}`\n"
        f"- **Trading Stock Deficit**: `R{expected_stock:,} - R{physical_count:,} = R{deficit:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "inventory_shortage_and_shrinkage_investigation",
        "question_text": (
            f"The internal auditor compared the **Trading Stock ledger balance (R{ledger_bal:,})** with the **physical stocktake (R{physical_count:,})** "
            f"and discovered that a partner had taken stock costing **R{unrec_drawings:,}** without recording it. Calculate the true **Trading Stock Deficit**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "First deduct unrecorded drawings from the book balance to find the true expected stock on hand, then subtract the physical count.",
            "Calculate Row 3 first, then subtract Row 4 from Row 3.",
            worked,
        ),
    }


def _gen_fixed_asset_and_vehicle_controls(r: random.Random) -> Dict[str, Any]:
    km_travelled = r.choice([4000, 5000, 6000])
    norm_km_per_litre = 10
    expected_litres = km_travelled // norm_km_per_litre
    actual_litres = expected_litres + r.choice([80, 120, 150])
    excess_litres = actual_litres - expected_litres

    headers = ["Delivery Vehicle Internal Control Audit", "Quantity / Control"]
    rows = [
        [f"Expected fuel consumption for {km_travelled:,} km at 10 km per litre (litres)", "{r0_c1}"],
        [f"Actual fuel paid on business fuel card ({actual_litres} litres) — Unexplained excess fuel (litres)", "{r1_c1}"],
        ["Control to monitor vehicle routes and private mileage (Logbook & GPS Tracker / Annual Stocktake)", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": expected_litres,
        "r1_c1": excess_litres,
        "r2_c1": "Logbook & GPS Tracker",
    }
    worked = (
        f"**Delivery Vehicle Fuel & Usage Audit**\n\n"
        f"- **Expected Fuel**: `{km_travelled:,} km ÷ 10 km/L = {expected_litres} litres`\n"
        f"- **Excess Fuel Purchased**: `{actual_litres} - {expected_litres} = {excess_litres} litres` (indicates private trips or fuel siphoning).\n"
        f"- **Control**: **Logbook & GPS Tracker**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "fixed_asset_register_and_vehicle_controls",
        "question_text": (
            f"A delivery van travelled **{km_travelled:,} km** during the month (standard consumption: **10 km per litre**), "
            f"but the fuel card was charged for **{actual_litres} litres**. Complete the internal audit schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Divide kilometres travelled by 10 km/litre to find expected fuel usage, then compare with actual litres billed.",
            "Calculate Expected Litres in Row 1, subtract from Actual Litres in Row 2, and choose the vehicle control in Row 3.",
            worked,
        ),
    }


def _gen_debtors_creditors_controls(r: random.Random) -> Dict[str, Any]:
    headers = ["Control Procedure", "Cycle Controlled (Debtors & Credit Sales / Creditors & Purchases)"]
    rows = [
        ["Matching the supplier's delivery note and Goods Received Note (GRN) to the original purchase order before recording the invoice", "{r0_c1}"],
        ["Checking customer creditworthiness and credit limit before dispatching goods on credit", "{r1_c1}"],
        ["Reconciling monthly supplier statements against individual accounts in the Creditors Ledger before paying", "{r2_c1}"],
        ["Preparing a monthly Age Analysis to follow up on accounts older than 30 days", "{r3_c1}"],
    ]
    correct_map = {
        "r0_c1": "Creditors & Purchases",
        "r1_c1": "Debtors & Credit Sales",
        "r2_c1": "Creditors & Purchases",
        "r3_c1": "Debtors & Credit Sales",
    }
    worked = (
        "**Debtors vs Creditors Control Procedures**\n\n"
        "- Matching GRN to purchase order $\\rightarrow$ **Creditors & Purchases**\n"
        "- Credit limit check before dispatch $\\rightarrow$ **Debtors & Credit Sales**\n"
        "- Supplier statement reconciliation $\\rightarrow$ **Creditors & Purchases**\n"
        "- Monthly Age Analysis follow-up $\\rightarrow$ **Debtors & Credit Sales**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "debtors_and_creditors_control_procedures",
        "question_text": "Classify each internal control procedure under **Debtors & Credit Sales** or **Creditors & Purchases**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Controls over buying stock and paying suppliers belong to Creditors & Purchases; controls over selling on credit and collecting cash belong to Debtors & Credit Sales.",
            "Enter either 'Debtors & Credit Sales' or 'Creditors & Purchases' for each row.",
            worked,
        ),
    }


def _gen_control_types_matrix(r: random.Random) -> Dict[str, Any]:
    headers = ["Internal Control Activity", "Control Type (Preventative / Detective / Corrective)"]
    rows = [
        ["Requiring two senior partners to authorise EFT payments above R10,000 before release", "{r0_c1}"],
        ["Preparing a monthly Bank Reconciliation Statement to identify unrecorded items or errors", "{r1_c1}"],
        ["Charging interest on overdue accounts and suspending credit facilities of defaulting debtors", "{r2_c1}"],
        ["Counting physical stock at month-end and comparing it to the perpetual Trading Stock ledger", "{r3_c1}"],
    ]
    correct_map = {
        "r0_c1": "Preventative",
        "r1_c1": "Detective",
        "r2_c1": "Corrective",
        "r3_c1": "Detective",
    }
    worked = (
        "**Preventative, Detective & Corrective Controls**\n\n"
        "- Dual EFT authorisation stops fraud before it happens $\\rightarrow$ **Preventative**\n"
        "- Bank reconciliation uncovers errors/omissions after transactions occur $\\rightarrow$ **Detective**\n"
        "- Suspending credit and charging overdue interest remedies a breach $\\rightarrow$ **Corrective**\n"
        "- Physical stocktake vs ledger uncovers stock shortages $\\rightarrow$ **Detective**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "preventative_detective_corrective_controls_matrix",
        "question_text": "Classify each internal control activity as **Preventative**, **Detective**, or **Corrective**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Preventative controls stop errors/fraud before they occur; Detective controls discover them afterwards; Corrective controls fix the problem.",
            "Classify each row using Preventative, Detective, or Corrective.",
            worked,
        ),
    }


def _gen_internal_audit_verification(r: random.Random) -> Dict[str, Any]:
    headers = ["Account / Balance Being Audited", "Primary Source Document / Audit Evidence Checked (Bank Statement / Physical Asset & Asset Register / Signed Payslips & Timecards)"]
    rows = [
        ["Verifying the existence and condition of partnership equipment and vehicles", "{r0_c1}"],
        ["Verifying that all wage payments in the CPJ were paid to real employees for hours worked", "{r1_c1}"],
        ["Verifying the month-end favourable bank balance and EFT debit orders", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": "Physical Asset & Asset Register",
        "r1_c1": "Signed Payslips & Timecards",
        "r2_c1": "Bank Statement",
    }
    worked = (
        "**Internal Audit Verification Evidence**\n\n"
        "- Equipment & vehicles $\\rightarrow$ **Physical Asset & Asset Register**\n"
        "- Wage payments $\\rightarrow$ **Signed Payslips & Timecards** (plus biometric clock-in records)\n"
        "- Bank balance & debit orders $\\rightarrow$ **Bank Statement**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "internal_audit_sampling_and_verification",
        "question_text": "Match each internal audit verification objective to the primary audit evidence from the column header.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Internal auditors verify book entries against independent physical or third-party source documents.",
            "Match each audit test to the appropriate evidence in brackets.",
            worked,
        ),
    }


_BUILDERS = {
    "cash_and_eft_internal_controls": _gen_cash_and_eft_controls,
    "inventory_shortage_and_shrinkage_investigation": _gen_inventory_shortage,
    "fixed_asset_register_and_vehicle_controls": _gen_fixed_asset_and_vehicle_controls,
    "debtors_and_creditors_control_procedures": _gen_debtors_creditors_controls,
    "preventative_detective_corrective_controls_matrix": _gen_control_types_matrix,
    "internal_audit_sampling_and_verification": _gen_internal_audit_verification,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Internal control and internal audit"
        q["grade"] = "11"
        out.append(q)
    return out
