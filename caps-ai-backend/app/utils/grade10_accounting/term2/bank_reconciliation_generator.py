from __future__ import annotations

import json
import random
import uuid
from typing import Any, Dict, List, Optional, Tuple


# Standardized misconception taxonomy tags
MISCONCEPTION_DEBIT_CREDIT_INVERSION = "debit_credit_inversion"
MISCONCEPTION_BANK_CHARGES_SIGN_ERROR = "bank_charges_sign_error"
MISCONCEPTION_OMITTED_DIRECT_DEPOSITS = "omitted_direct_deposits"
MISCONCEPTION_TIMING_VS_ERROR_CONFUSION = "timing_vs_error_confusion"
MISCONCEPTION_UNFAVOURABLE_BALANCE_SIGN_ERROR = "unfavourable_balance_sign_error"


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _make_id(prefix: str, seed: Optional[int] = None) -> str:
    if seed is not None:
        return f"{prefix}_{abs(hash(seed)) % 10000000:07d}"
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _fmt_money(amount: float) -> str:
    """Format money with South African space thousands separator."""
    rounded = _round_money(amount)
    if rounded == int(rounded):
        s = f"{int(rounded):,}".replace(",", " ")
    else:
        s = f"{rounded:,.2f}".replace(",", " ")
    return f"R{s}"


BUSINESS_NAMES = [
    "Sipho General Dealer",
    "Khanyi Supermarket",
    "Thabo Auto Spares",
    "Vusi Electronics",
    "Zola Fashions",
    "Lindiwe Bookshop",
    "Bongani Hardware",
    "Nomvula Furniture",
]

MONTHS = ["March", "May", "June", "August", "September", "November"]


def _generate_recon_dataset(r: random.Random) -> Dict[str, Any]:
    """Generate deterministic, mathematically consistent Bank Reconciliation data."""
    business_name = r.choice(BUSINESS_NAMES)
    month = r.choice(MONTHS)
    year = 2026

    # 1. Provisional totals of cash journals before reconciliation adjustments
    prov_crj = float(r.choice([28500, 34200, 41800, 52600, 68400]))
    prov_cpj = float(r.choice([19400, 26800, 33500, 44200, 51000]))

    # 2. Bank statement unrecorded items (adjustments to cash journals)
    # CRJ adjustments:
    direct_deposit_tenant = float(r.choice([3500, 4200, 5000, 6500, 7200]))
    interest_income = float(r.choice([180, 240, 310, 450, 520]))
    total_crj_adjustments = direct_deposit_tenant + interest_income

    # CPJ adjustments:
    bank_charges = float(r.choice([220, 280, 340, 460, 550]))
    insurance_debit_order = float(r.choice([1200, 1650, 1900, 2400, 2800]))
    dishonoured_cheque = float(r.choice([650, 850, 1100, 1400]))
    total_cpj_adjustments = bank_charges + insurance_debit_order + dishonoured_cheque

    # Updated journal totals
    final_crj = prov_crj + total_crj_adjustments
    final_cpj = prov_cpj + total_cpj_adjustments

    # Bank account balance in General Ledger
    # Let opening GL balance be known
    opening_gl_bank = float(r.choice([12400, 18600, 24500, -3200, -5400]))
    # Net movement in Bank account = CRJ - CPJ
    net_bank_movement = final_crj - final_cpj
    closing_gl_bank = opening_gl_bank + net_bank_movement

    # 3. Timing differences & Bank Reconciliation items
    outstanding_deposit = float(r.choice([6400, 8500, 11200, 14800, 18500]))
    unpresented_cheque_1 = ("EFT 104", float(r.choice([1850, 2400, 3100, 4200])))
    unpresented_cheque_2 = ("EFT 112", float(r.choice([950, 1450, 2150, 2900])))
    total_unpresented = unpresented_cheque_1[1] + unpresented_cheque_2[1]

    # Bank error: Bank incorrectly debited/credited the account
    # E.g., Bank incorrectly debited an amount of R500 belonging to another client
    bank_error_amount = float(r.choice([350, 450, 600, 750, 900]))
    # Since bank incorrectly debited, the correction is on the Credit side of BRS
    correction_of_bank_error_credit = bank_error_amount

    # In the Bank Reconciliation Statement:
    # Credit side items = Outstanding deposit + Bank error correction + (Bank statement if favourable, or Bank Account if unfavourable)
    # Debit side items = Outstanding EFTs + (Bank statement if unfavourable, or Bank Account if favourable)
    #
    # Relationship:
    # Closing Bank Account balance in Ledger (if favourable = Debit)
    # On BRS:
    # Debit column:
    # - Outstanding EFT 1: unpresented_cheque_1[1]
    # - Outstanding EFT 2: unpresented_cheque_2[1]
    # - Balance as per Bank Account (favourable): closing_gl_bank (if closing_gl_bank > 0, entered on Debit side of BRS? Wait!)
    # Let's verify standard CAPS Grade 10 Bank Reconciliation Statement layout:
    # In SA CAPS Accounting:
    # Bank Reconciliation Statement:
    # Column 1: Debit, Column 2: Credit
    # Standard format:
    # - Credit: Balance as per Bank Statement (favourable) [Credit in bank's books means bank owes us]
    # - Debit: Balance as per Bank Statement (unfavourable / overdrawn)
    # - Credit: Outstanding deposit (bank must still credit us)
    # - Debit: Outstanding cheques / EFT payments (bank will debit when presented)
    # - Credit: Correction of bank error (incorrect debit by bank)
    # - Debit: Correction of bank error (incorrect credit by bank)
    # - Debit: Balance as per Bank Account (favourable) [General Ledger balance]
    #   OR Credit: Balance as per Bank Account (unfavourable / overdrawn)
    #
    # Then Total Debit MUST equal Total Credit!
    # Let's verify this mathematically:
    # Let BS_bal be balance as per bank statement.
    # If closing_gl_bank is favourable (> 0):
    # Total Debit = total_unpresented + closing_gl_bank + (BS_bal if unfavourable)
    # Total Credit = outstanding_deposit + correction_of_bank_error_credit + (BS_bal if favourable)
    # Since Total Debit = Total Credit:
    # total_unpresented + closing_gl_bank = outstanding_deposit + correction_of_bank_error_credit + BS_bal (if favourable)
    # Therefore:
    # BS_bal = (total_unpresented + closing_gl_bank) - (outstanding_deposit + correction_of_bank_error_credit)

    raw_bs_bal = (total_unpresented + closing_gl_bank) - (outstanding_deposit + correction_of_bank_error_credit)
    if raw_bs_bal >= 0:
        bs_favourable = True
        bank_statement_balance = raw_bs_bal
    else:
        bs_favourable = False
        bank_statement_balance = abs(raw_bs_bal)

    # Recalculate totals to guarantee exact balance
    if bs_favourable:
        total_credit = outstanding_deposit + correction_of_bank_error_credit + bank_statement_balance
        total_debit = total_unpresented + (closing_gl_bank if closing_gl_bank >= 0 else 0)
        # If closing_gl_bank is negative, it would go on credit side:
        if closing_gl_bank < 0:
            total_credit += abs(closing_gl_bank)
    else:
        total_credit = outstanding_deposit + correction_of_bank_error_credit + (abs(closing_gl_bank) if closing_gl_bank < 0 else 0)
        total_debit = total_unpresented + bank_statement_balance + (closing_gl_bank if closing_gl_bank >= 0 else 0)

    return {
        "business_name": business_name,
        "month": month,
        "year": year,
        "prov_crj": prov_crj,
        "prov_cpj": prov_cpj,
        "direct_deposit_tenant": direct_deposit_tenant,
        "interest_income": interest_income,
        "total_crj_adjustments": total_crj_adjustments,
        "final_crj": final_crj,
        "bank_charges": bank_charges,
        "insurance_debit_order": insurance_debit_order,
        "dishonoured_cheque": dishonoured_cheque,
        "total_cpj_adjustments": total_cpj_adjustments,
        "final_cpj": final_cpj,
        "opening_gl_bank": opening_gl_bank,
        "closing_gl_bank": closing_gl_bank,
        "outstanding_deposit": outstanding_deposit,
        "unpresented_cheque_1": unpresented_cheque_1,
        "unpresented_cheque_2": unpresented_cheque_2,
        "total_unpresented": total_unpresented,
        "bank_error_amount": bank_error_amount,
        "correction_of_bank_error_credit": correction_of_bank_error_credit,
        "bs_favourable": bs_favourable,
        "bank_statement_balance": bank_statement_balance,
        "total_debit": total_debit,
        "total_credit": total_credit,
    }


def _build_compound_question(data: Dict[str, Any], mode: str, seed: Optional[int]) -> Dict[str, Any]:
    """Build full compound Bank Reconciliation question (Journals + BRS)."""
    b_name = data["business_name"]
    month = data["month"]
    year = data["year"]

    prompt = (
        f"You are the bookkeeper for **{b_name}**. On {data['month']} 30, {year}, you received the monthly "
        f"Bank Statement from Fundile Bank. Complete the supplementary Cash Journals and the Bank Reconciliation Statement.\n\n"
        f"### Information:\n"
        f"1. **Provisional Cash Journal Totals on {month} 30**:\n"
        f"   - Cash Receipts Journal (CRJ): {_fmt_money(data['prov_crj'])}\n"
        f"   - Cash Payments Journal (CPJ): {_fmt_money(data['prov_cpj'])}\n"
        f"2. **Items on Bank Statement not yet entered in Journals**:\n"
        f"   - Direct deposit by tenant for rent: {_fmt_money(data['direct_deposit_tenant'])}\n"
        f"   - Interest on credit balance: {_fmt_money(data['interest_income'])}\n"
        f"   - Bank service fees and cash handling charges: {_fmt_money(data['bank_charges'])}\n"
        f"   - Debit order for monthly business insurance: {_fmt_money(data['insurance_debit_order'])}\n"
        f"   - Dishonoured / unpaid cheque (R/D) from debtor: {_fmt_money(data['dishonoured_cheque'])}\n"
        f"3. **Bank Reconciliation details**:\n"
        f"   - Balance as per Bank Statement on {month} 30: {_fmt_money(data['bank_statement_balance'])} "
        f"({'Favourable / Credit' if data['bs_favourable'] else 'Unfavourable / Debit'})\n"
        f"   - Deposit made on {month} 30 not yet cleared on Bank Statement: {_fmt_money(data['outstanding_deposit'])}\n"
        f"   - Outstanding unpresented EFTs: {data['unpresented_cheque_1'][0]} ({_fmt_money(data['unpresented_cheque_1'][1])}), "
        f"{data['unpresented_cheque_2'][0]} ({_fmt_money(data['unpresented_cheque_2'][1])})\n"
        f"   - Bank error: The bank incorrectly debited {_fmt_money(data['bank_error_amount'])} to {b_name}'s account.\n"
        f"   - The final Bank Account balance in the General Ledger is {_fmt_money(abs(data['closing_gl_bank']))} "
        f"({'favourable' if data['closing_gl_bank'] >= 0 else 'overdrawn/unfavourable'}).\n"
    )

    headers = ["Details", "Debit (R)", "Credit (R)"]

    # Rows for the 2D BRS Table:
    # Row 0: Balance as per Bank Statement
    # Row 1: Outstanding deposit
    # Row 2: Outstanding EFT 1
    # Row 3: Outstanding EFT 2
    # Row 4: Correction of bank error (incorrect debit)
    # Row 5: Balance as per Bank Account in General Ledger
    # Row 6: Totals

    bs_deb = "" if data["bs_favourable"] else str(int(data["bank_statement_balance"]))
    bs_cred = str(int(data["bank_statement_balance"])) if data["bs_favourable"] else ""

    gl_deb = str(int(data["closing_gl_bank"])) if data["closing_gl_bank"] >= 0 else ""
    gl_cred = "" if data["closing_gl_bank"] >= 0 else str(int(abs(data["closing_gl_bank"])))

    values_rows = [
        [f"Balance as per Bank Statement ({'favourable' if data['bs_favourable'] else 'unfavourable'})", bs_deb, bs_cred],
        [f"Outstanding deposit", "", str(int(data["outstanding_deposit"]))],
        [f"Outstanding {data['unpresented_cheque_1'][0]}", str(int(data['unpresented_cheque_1'][1])), ""],
        [f"Outstanding {data['unpresented_cheque_2'][0]}", str(int(data['unpresented_cheque_2'][1])), ""],
        [f"Correction of bank error (incorrect debit)", "", str(int(data["bank_error_amount"]))],
        [f"Balance as per Bank Account in General Ledger", gl_deb, gl_cred],
        ["Total", str(int(data["total_debit"])), str(int(data["total_credit"]))],
    ]

    correct_map: Dict[str, str] = {}
    rows_data: List[List[Dict[str, Any]]] = []
    cell_hints: Dict[str, str] = {}

    for rix, row in enumerate(values_rows):
        row_cells = []
        for cix, val in enumerate(row):
            coord = f"t0_r{rix}_c{cix}"
            is_desc = (cix == 0)
            is_editable = not is_desc

            # Set correct map
            correct_map[coord] = val

            cell_obj = {
                "coordinate": coord,
                "value": val if (mode == "scaffold" or not is_editable) else "",
                "type": "given" if not is_editable else ("must_be_empty" if val == "" else "required"),
                "editable": is_editable,
            }
            row_cells.append(cell_obj)

            # Build cell-level hints for editable cells
            if is_editable:
                if rix == 0:
                    cell_hints[coord] = (
                        "Bank Statement balance: In bank records, a favourable balance is Credit; an overdrawn balance is Debit."
                    )
                elif rix == 1:
                    cell_hints[coord] = "Outstanding deposits increase the bank balance, so enter in the Credit column."
                elif rix in (2, 3):
                    cell_hints[coord] = "Unpresented cheques and EFTs decrease bank funds when cleared, so enter in the Debit column."
                elif rix == 4:
                    cell_hints[coord] = "The bank wrongly debited your account. To reverse this, credit the reconciliation statement."
                elif rix == 5:
                    cell_hints[coord] = "Balance per Bank Account in General Ledger: A favourable asset balance is placed on Debit; overdrawn on Credit."
                elif rix == 6:
                    cell_hints[coord] = "Total both columns. Both Debit and Credit must reconcile to the exact same total."

        rows_data.append(row_cells)

    marking_points = [
        {"id": "mp_bs_bal", "desc": "Balance as per Bank Statement", "marks": 2, "editable": True},
        {"id": "mp_out_dep", "desc": "Outstanding deposit on Credit side", "marks": 2, "editable": True},
        {"id": "mp_eft1", "desc": "Outstanding EFT 104 on Debit side", "marks": 1, "editable": True},
        {"id": "mp_eft2", "desc": "Outstanding EFT 112 on Debit side", "marks": 1, "editable": True},
        {"id": "mp_error", "desc": "Correction of bank error on Credit side", "marks": 2, "editable": True},
        {"id": "mp_gl_bal", "desc": "Balance as per Bank Account in General Ledger", "marks": 2, "editable": True},
        {"id": "mp_totals", "desc": "Total Debit and Credit reconciliation agreement", "marks": 2, "editable": True},
    ]

    hint_sections = {
        "tier1_location": "Check the Bank Reconciliation Statement table columns (Debit vs Credit).",
        "tier2_directional_rule": (
            "Remember: From the bank's perspective, your money is a liability (favourable = Credit). "
            "Outstanding deposits go to Credit. Outstanding EFTs go to Debit. Both columns must agree."
        ),
        "tier3_worked_step": (
            f"Enter Bank Statement balance {_fmt_money(data['bank_statement_balance'])} in {'Credit' if data['bs_favourable'] else 'Debit'}. "
            f"Outstanding deposit {_fmt_money(data['outstanding_deposit'])} in Credit. "
            f"Outstanding EFTs {_fmt_money(data['unpresented_cheque_1'][1])} and {_fmt_money(data['unpresented_cheque_2'][1])} in Debit. "
            f"Bank error {_fmt_money(data['bank_error_amount'])} in Credit. Totals reconcile to {_fmt_money(data['total_debit'])}."
        ),
    }

    return {
        "id": _make_id("acct10_bank_recon_compound", seed),
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 10,
        "learning_objective_id": "acct_g10_t2_bank_reconciliation",
        "subject": "Accounting",
        "grade": 10,
        "mode": mode,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "hint_sections": hint_sections,
        "misconception_tags": [
            MISCONCEPTION_DEBIT_CREDIT_INVERSION,
            MISCONCEPTION_TIMING_VS_ERROR_CONFUSION,
            MISCONCEPTION_UNFAVOURABLE_BALANCE_SIGN_ERROR,
        ],
        "marking_schema": {
            "total_marks": 12,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _build_elementary_crj_cpj_question(data: Dict[str, Any], mode: str, seed: Optional[int]) -> Dict[str, Any]:
    """Build atomic elementary drill on updating CRJ and CPJ with bank statement items."""
    b_name = data["business_name"]
    month = data["month"]

    prompt = (
        f"**{b_name}**: Supplementary Cash Journals Drill.\n\n"
        f"Provisional totals on {month} 30:\n"
        f"- Provisional CRJ: {_fmt_money(data['prov_crj'])}\n"
        f"- Provisional CPJ: {_fmt_money(data['prov_cpj'])}\n\n"
        f"The following items appeared on the Bank Statement but not in the journals:\n"
        f"1. Direct deposit from tenant: {_fmt_money(data['direct_deposit_tenant'])}\n"
        f"2. Interest on credit balance: {_fmt_money(data['interest_income'])}\n"
        f"3. Bank charges and transaction fees: {_fmt_money(data['bank_charges'])}\n"
        f"4. Debit order for insurance: {_fmt_money(data['insurance_debit_order'])}\n"
        f"5. Dishonoured cheque (R/D) from a debtor: {_fmt_money(data['dishonoured_cheque'])}\n\n"
        f"Calculate the **Final Updated Totals** for both journals."
    )

    headers = ["Journal", "Provisional Total", "Adjustments", "Final Total (R)"]
    values_rows = [
        ["Cash Receipts Journal (CRJ)", str(int(data["prov_crj"])), f"+{int(data['total_crj_adjustments'])}", str(int(data["final_crj"]))],
        ["Cash Payments Journal (CPJ)", str(int(data["prov_cpj"])), f"+{int(data['total_cpj_adjustments'])}", str(int(data["final_cpj"]))],
    ]

    correct_map: Dict[str, str] = {
        "t0_r0_c3": str(int(data["final_crj"])),
        "t0_r1_c3": str(int(data["final_cpj"])),
    }

    rows_data = []
    for rix, row in enumerate(values_rows):
        row_cells = []
        for cix, val in enumerate(row):
            coord = f"t0_r{rix}_c{cix}"
            is_editable = (cix == 3)
            row_cells.append({
                "coordinate": coord,
                "value": val if (mode == "scaffold" or not is_editable) else "",
                "type": "required" if is_editable else "given",
                "editable": is_editable,
            })
        rows_data.append(row_cells)

    cell_hints = {
        "t0_r0_c3": f"Final CRJ = Provisional CRJ ({_fmt_money(data['prov_crj'])}) + Direct deposit ({_fmt_money(data['direct_deposit_tenant'])}) + Interest ({_fmt_money(data['interest_income'])}).",
        "t0_r1_c3": f"Final CPJ = Provisional CPJ ({_fmt_money(data['prov_cpj'])}) + Bank charges ({_fmt_money(data['bank_charges'])}) + Insurance ({_fmt_money(data['insurance_debit_order'])}) + Dishonoured cheque ({_fmt_money(data['dishonoured_cheque'])}).",
    }

    hint_sections = {
        "tier1_location": "Look at column 'Final Total (R)' for CRJ and CPJ.",
        "tier2_directional_rule": (
            "Receipts (CRJ) increase bank balance: add direct deposits and interest earned. "
            "Payments (CPJ) decrease bank balance: add bank charges, debit orders, and dishonoured cheques."
        ),
        "tier3_worked_step": (
            f"CRJ: {int(data['prov_crj'])} + {int(data['total_crj_adjustments'])} = {int(data['final_crj'])}. "
            f"CPJ: {int(data['prov_cpj'])} + {int(data['total_cpj_adjustments'])} = {int(data['final_cpj'])}."
        ),
    }

    return {
        "id": _make_id("acct10_bank_recon_elementary_journals", seed),
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "learning_objective_id": "acct_g10_t2_bank_reconciliation_journals",
        "subject": "Accounting",
        "grade": 10,
        "mode": mode,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "hint_sections": hint_sections,
        "misconception_tags": [
            MISCONCEPTION_BANK_CHARGES_SIGN_ERROR,
            MISCONCEPTION_OMITTED_DIRECT_DEPOSITS,
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_crj", "desc": "Final Cash Receipts Journal total", "marks": 3, "editable": True},
                {"id": "mp_cpj", "desc": "Final Cash Payments Journal total", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _build_elementary_outstanding_items_question(data: Dict[str, Any], mode: str, seed: Optional[int]) -> Dict[str, Any]:
    """Build atomic classification drill distinguishing timing differences from journal adjustments."""
    items = [
        {"desc": "Service fees and cash handling charges debited by the bank", "dest": "CPJ", "rule": "Bank charges reduce bank funds and must be entered in Cash Payments Journal."},
        {"desc": "Direct deposit by a tenant into the business bank account", "dest": "CRJ", "rule": "Direct deposits increase bank funds and must be entered in Cash Receipts Journal."},
        {"desc": "Deposit made by the business on the last day of the month not yet on bank statement", "dest": "BRS (Credit)", "rule": "Outstanding deposit is a timing difference on the Bank Reconciliation Statement (Credit)."},
        {"desc": "Electronic Funds Transfer (EFT) issued to a supplier not yet cleared", "dest": "BRS (Debit)", "rule": "Unpresented EFT is a timing difference on the Bank Reconciliation Statement (Debit)."},
        {"desc": "Debit order for monthly vehicle tracking debited on bank statement", "dest": "CPJ", "rule": "Debit orders paid by bank must be entered in Cash Payments Journal."},
    ]
    r = _rng(seed)
    chosen = r.sample(items, k=4)

    prompt = (
        "**Bank Reconciliation Classification Drill**\n\n"
        "Indicate where each of the following items should be recorded: **CRJ**, **CPJ**, "
        "**BRS (Credit)**, or **BRS (Debit)**."
    )

    headers = ["Item / Transaction", "Classification"]
    rows_data = []
    correct_map = {}
    cell_hints = {}

    for rix, item in enumerate(chosen):
        coord = f"t0_r{rix}_c1"
        correct_map[coord] = item["dest"]
        cell_hints[coord] = item["rule"]
        rows_data.append([
            {"coordinate": f"t0_r{rix}_c0", "value": item["desc"], "type": "given", "editable": False},
            {"coordinate": coord, "value": item["dest"] if mode == "scaffold" else "", "type": "required", "editable": True},
        ])

    hint_sections = {
        "tier1_location": "Look at column 'Classification'. Choose between CRJ, CPJ, BRS (Credit), and BRS (Debit).",
        "tier2_directional_rule": (
            "Items already on the Bank Statement that need updating in books belong in CRJ or CPJ. "
            "Items already in journals but not yet processed by the bank (timing differences) belong on the BRS."
        ),
        "tier3_worked_step": "CRJ for receipts, CPJ for payments, BRS Credit for deposits, BRS Debit for unpresented cheques/EFTs.",
    }

    return {
        "id": _make_id("acct10_bank_recon_elementary_classify", seed),
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "learning_objective_id": "acct_g10_t2_bank_reconciliation_classify",
        "subject": "Accounting",
        "grade": 10,
        "mode": mode,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "hint_sections": hint_sections,
        "misconception_tags": [
            MISCONCEPTION_TIMING_VS_ERROR_CONFUSION,
            MISCONCEPTION_DEBIT_CREDIT_INVERSION,
        ],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": f"mp_item_{i}", "desc": f"Correct classification for item {i+1}", "marks": 2, "editable": True}
                for i in range(len(chosen))
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate_questions(
    r: Optional[random.Random] = None,
    n: int = 1,
    subskill: str = "mixed",
    mode: str = "scaffold",
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Universal generator entrypoint for CAPS Grade 10 Accounting Term 2 Bank Reconciliation.

    Adheres strictly to the 6-pillar Generator Architecture Contract.
    """
    if r is None:
        r = _rng(seed)

    questions: List[Dict[str, Any]] = []

    for idx in range(n):
        q_seed = seed + idx if seed is not None else r.randint(1, 100000)
        data = _generate_recon_dataset(r)

        norm_mode = str(mode or "").strip().lower()
        sub = str(subskill or "").strip().lower()

        if norm_mode.startswith("elementary_") or sub.startswith("elementary_"):
            target_sub = norm_mode if norm_mode.startswith("elementary_") else sub
            if "journal" in target_sub or "crj" in target_sub or "cpj" in target_sub:
                q = _build_elementary_crj_cpj_question(data, mode, q_seed)
            elif "classify" in target_sub or "item" in target_sub:
                q = _build_elementary_outstanding_items_question(data, mode, q_seed)
            else:
                q = _build_compound_question(data, mode, q_seed)
        elif sub == "crj_cpj" or sub == "journals":
            q = _build_elementary_crj_cpj_question(data, mode, q_seed)
        elif sub == "classification" or sub == "items":
            q = _build_elementary_outstanding_items_question(data, mode, q_seed)
        else:
            q = _build_compound_question(data, mode, q_seed)

        questions.append(q)

    return questions
