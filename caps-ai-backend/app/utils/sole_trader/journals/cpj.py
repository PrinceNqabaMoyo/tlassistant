from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..column_help import headers_to_column_help
from ..core import build_journal_row, journal_editable_cols_by_difficulty, make_journal, round_money
from ..names import pick_business_name, pick_business_names, pick_person_name


def _cpj_expected_text(value: Any) -> str:
    if isinstance(value, list):
        parts = [str(v).strip() for v in value if str(v).strip()]
        return " or ".join(parts)
    return "" if value is None else str(value).strip()


def _cpj_hint_text(cell_hint: Any) -> str:
    if isinstance(cell_hint, dict):
        parts: List[str] = []
        title = str(cell_hint.get("title") or "").strip()
        if title:
            parts.append(title)
        for step in (cell_hint.get("steps") or []):
            step_text = str(step or "").strip()
            if step_text:
                parts.append(step_text)
        return " ".join(parts).strip()
    return str(cell_hint or "").strip()


def _cpj_off_journal_rule(item: Optional[Dict[str, str]]) -> str:
    if not item:
        return ""
    text = str(item.get("text") or "").strip()
    journal = str(item.get("journal") or "").strip()
    why = str(item.get("why") or "").strip()
    if not text and not journal and not why:
        return ""
    base = f"{text} does not belong in the CPJ"
    if journal:
        base += f"; record it in the {journal}"
    if why:
        base += f" because {why}"
    return base + "."


def _build_cpj_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    transaction_line: str,
    row_hint: str = "",
    off_journal_item: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = _cpj_expected_text(expected)
    tx_text = str(transaction_line or "").strip()
    off_journal_rule = _cpj_off_journal_rule(off_journal_item)

    role = f"This cell records the {header or 'required CPJ detail'} for this payment row."
    evidence = f"Use the payment transaction wording: {tx_text}" if tx_text else "Use the payment details given in the question."
    rule = "The CPJ records money paid out of the bank account by cheque, EFT, or bank-statement entry."
    method = row_hint or "Identify who was paid, determine the amount actually paid, then place the amount in the correct CPJ column."
    transfer_tip = "In similar questions, decide first whether money actually left the bank account. If not, the transaction probably belongs in another journal."

    if header_norm in {"doc", "eft"}:
        role = "This cell identifies the source document or reference for the payment recorded in the CPJ."
        rule = "Use the cheque number, EFT reference, or bank statement reference that proves the payment."
        method = f"Copy the payment reference for this row. Here it is {expected_text}." if expected_text else "Copy the payment reference linked to the bank payment."
        transfer_tip = "In similar questions, use payment references for CPJ items, not invoices, debit notes, or credit notes from returns journals."
    elif header_norm in {"name of payee", "details"}:
        role = "This cell names who was paid or what the payment relates to."
        rule = "The payee/details entry must identify the creditor, supplier, person, or account linked to the payment."
        method = f"Read who received the payment and enter that name or description. Here it is {expected_text}." if expected_text else method
        transfer_tip = "In similar questions, ask 'Who received the money?' or 'What was the payment for?' before filling this cell."
    elif header_norm == "bank":
        role = "This cell records the amount actually paid out of the bank account."
        rule = "The Bank column in the CPJ always shows the amount actually paid."
        method = f"Use the amount paid after any discount received and enter {expected_text}." if expected_text else method
        transfer_tip = "In similar questions, Bank is the actual cash outflow, not always the full amount owing."
    elif header_norm == "trading stock":
        role = "This cell records cash purchases of trading stock."
        rule = "Use the Trading stock column only when trading stock is bought for cash or paid directly from bank. Credit purchases go to the CJ, not the CPJ."
        method = f"If the payment was for trading stock paid from bank, enter the amount here. For this row it is {expected_text or 'blank because another account is affected'}."
        transfer_tip = "In similar questions, separate cash purchases from credit purchases before choosing between CPJ and CJ."
    elif header_norm == "equipment":
        role = "This cell records cash payments for equipment when the table has a special equipment column."
        rule = "Use Equipment only when the bank payment is specifically for equipment and the format provides that column."
        method = f"Enter the equipment payment here. For this row it is {expected_text or 'blank because no equipment payment is being recorded'}."
        transfer_tip = "In similar questions, use a special analysis column only when the payment matches that account exactly."
    elif header_norm.startswith("creditors control"):
        role = "This cell records the creditor amount being settled through the Creditors Control analysis."
        rule = "For settlement with a creditor discount, Creditors Control shows the full amount owing that is settled."
        method = f"Use the amount owing to the creditor, not just the amount paid. Here it is {expected_text or 'blank because this row is not settling a creditor account'}."
        transfer_tip = "In similar questions, compare amount owing, amount paid, and discount received before completing the creditor columns."
    elif header_norm == "discount received":
        role = "This cell records the discount received from a creditor when settling an account."
        rule = "Discount received equals the amount owing minus the amount actually paid."
        method = f"Calculate amount owing minus amount paid. Here the discount received is {expected_text or 'blank because no creditor discount applies'}."
        transfer_tip = "In similar questions, only use Discount received when the creditor allows the business to pay less than the amount owing."
    elif header_norm.startswith("debtors control"):
        role = "This cell records payments that affect Debtors Control, such as refunds to debtors or similar debtor-related bank payments."
        rule = "Use Debtors Control only when the payment reduces the amount owed by or to a debtor in a debtor-related payment situation."
        method = f"Enter the debtor-related payment amount here. For this row it is {expected_text or 'blank because no debtor-related payment applies'}."
        transfer_tip = "In similar questions, use this column only when the payment affects a debtor account, not an ordinary expense or creditor settlement."
    elif header_norm == "wages":
        role = "This cell records wages paid from the bank account."
        rule = "Use Wages only for wages payments. Other expenses belong in Sundry or another special column if provided."
        method = f"If the payment is wages, enter the amount here. For this row it is {expected_text or 'blank because this payment is not wages'}."
        transfer_tip = "In similar questions, identify the expense name before deciding whether it has its own CPJ column or belongs under Sundry."
    elif header_norm == "sundry amount":
        role = "This cell records the amount for payments that do not belong in the standard CPJ analysis columns."
        rule = "Use Sundry amount for payments such as telephone, insurance, repairs, bank charges, drawings, and similar items when no special column exists."
        method = f"Enter the amount for the sundry account here. For this row it is {expected_text or 'blank because another analysis column is used'}."
        transfer_tip = "In similar questions, after ruling out stock, wages, debtor, and creditor columns, place the payment under Sundry."
    elif header_norm == "sundry details":
        role = "This cell names the General Ledger account linked to the sundry payment."
        rule = "Sundry details explains what account will later be posted for the sundry amount."
        method = f"Write the account name for the sundry payment. Here it is {expected_text or 'blank because no sundry account is used on this row'}."
        transfer_tip = "In similar questions, use Sundry details to label the exact type of payment when no separate column exists."

    if off_journal_rule:
        rule = f"{rule} {off_journal_rule}".strip()
        method = f"{method} Ignore the off-journal item when completing the CPJ table.".strip()

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def _make_cpj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    creditor = pick_business_name(r=r)
    amount = float(r.randrange(250, 3500 + 1, 50))
    variant = r.choice(["credit_purchase", "debit_note", "credit_note", "cash_receipt"])
    if variant == "credit_purchase":
        invoice_no = f"INV{r.randrange(100, 999)}"
        text = f"{invoice_no} Bought trading stock on credit from {creditor}, R{amount:.2f}"
        return {"text": text, "journal": "CJ", "why": "it is a credit purchase and no money was paid yet"}
    if variant == "cash_receipt":
        receipt_no = f"{r.randrange(140, 220)}"
        source = r.choice(["rent income", "commission income", "cash sales"])
        text = f"Receipt no. {receipt_no} received for {source}, R{amount:.2f}"
        return {"text": text, "journal": "CRJ", "why": "it is a cash receipt, so it belongs in the CRJ, not the CPJ"}
    if variant == "debit_note":
        debit_note_no = f"DN{r.randrange(100, 999)}"
        text = f"{debit_note_no} Sent a debit note to {creditor} for goods returned, R{amount:.2f}"
        return {"text": text, "journal": "CAJ", "why": "a debit note for returns to a creditor is not a cash payment"}
    credit_note_no = f"CN{r.randrange(100, 999)}"
    text = f"{credit_note_no} Received a credit note from {creditor} for goods returned, R{amount:.2f}"
    return {"text": text, "journal": "CAJ", "why": "the creditor return is recorded in the CAJ, not in the CPJ"}


def _cpj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Name of payee",
        "Fol",
        "Bank",
        "Trading stock",
        "Creditors control",
        "Discount received",
        "Debtors control (R/D)",
        "Wages",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def make_cpj_single_row_question(*, r: random.Random) -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    cheque_no = str(r.choice([124, 125, 126, 127, 128, 129, 130]))
    day = int(r.choice([1, 3, 6, 8, 9, 12, 15, 24, 28]))

    creditors = pick_business_names(r=r, k=5)[:3]
    creditor_balances: Dict[str, float] = {c: float(r.randrange(2000, 14000 + 1, 100)) for c in creditors}

    headers = _cpj_headers()

    kind = r.choice(["buy_stock_cash", "pay_creditor_discount", "wages", "sundry_telephone", "sundry_repairs"])

    payee: str
    bank: float
    trading_stock: Optional[float] = None
    creditors_control: Optional[float] = None
    discount_received: Optional[float] = None
    wages: Optional[float] = None
    sundry_amount: Optional[float] = None
    sundry_details: str = ""
    transaction_line: str

    if kind == "buy_stock_cash":
        payee = r.choice(creditors)
        amount = float(r.choice([1400, 2800, 4100, 5000, 12000]))
        bank = amount
        trading_stock = amount
        transaction_line = (
            f"{day} {month}: Bought trading stock for cash and paid by cheque no. {cheque_no} to {payee}, R{amount:.2f}."
        )

    elif kind == "pay_creditor_discount":
        payee = r.choice(creditors)
        amount_due = float(r.choice([1500, 2400, 3600, 4800, 6500, 8200]))
        discount = float(r.choice([0, 50, 80, 100, 150, 200]))
        if discount >= amount_due:
            discount = 0.0
        amount_paid = round_money(amount_due - discount)
        creditor_balances[payee] = amount_due
        bank = amount_paid
        creditors_control = amount_due
        discount_received = discount
        transaction_line = (
            f"{day} {month}: Issued cheque no. {cheque_no} to {payee} in settlement of account R{amount_due:.2f}. "
            f"Discount received R{discount:.2f}."
        )

    elif kind == "wages":
        payee = "Wages"
        amount = float(r.choice([1200, 1800, 2500, 3200, 4500]))
        bank = amount
        wages = amount
        transaction_line = f"{day} {month}: Paid wages by cheque no. {cheque_no}, R{amount:.2f}."

    elif kind == "sundry_telephone":
        payee = "Telkom"
        amount = float(r.choice([350, 480, 620, 750, 980, 1250]))
        bank = amount
        sundry_amount = amount
        sundry_details = "Telephone"
        transaction_line = f"{day} {month}: Paid telephone account by cheque no. {cheque_no} to Telkom, R{amount:.2f}."

    else:
        payee = "RD Repairers"
        amount = float(r.choice([400, 650, 900, 1200, 1600, 2400]))
        bank = amount
        sundry_amount = amount
        sundry_details = "Repairs"
        transaction_line = f"{day} {month}: Paid repairs by cheque no. {cheque_no} to RD Repairers, R{amount:.2f}."

    values: List[Optional[str]] = [
        cheque_no,
        str(day),
        payee,
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    editable_cols = [3, 4, 5, 6, 7, 9, 10, 11, 12]
    row = build_journal_row(row_index=0, values=values, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    off_journal_item = _make_cpj_off_journal_item(r=r)
    off_journal_day = int(r.choice([2, 5, 7, 10, 16, 19, 23, 27]))

    def _set(col: int, expected: Any) -> None:
        correct_map[f"r0_c{col}"] = expected

    _set(3, "")
    _set(4, f"{bank:.2f}")
    _set(5, f"{trading_stock:.2f}" if trading_stock is not None else "")
    _set(6, f"{creditors_control:.2f}" if creditors_control is not None else "")
    _set(7, f"{discount_received:.2f}" if discount_received is not None else "")
    _set(9, f"{wages:.2f}" if wages is not None else "")
    _set(10, f"{sundry_amount:.2f}" if sundry_amount is not None else "")
    _set(11, "")
    _set(12, sundry_details)

    # Cell-level help for typical calculations.
    if kind == "pay_creditor_discount":
        cell_hints["r0_c4"] = {
            "title": "Bank (amount actually paid)",
            "steps": [
                "Bank = amount actually paid.",
                "Creditors control = amount due.",
                "Discount received = amount due − amount paid.",
            ],
        }
        cell_hints["r0_c6"] = {
            "title": "Creditors control",
            "steps": [
                "For settlement with discount, Creditors control shows the full amount owed (amount due).",
            ],
        }
        cell_hints["r0_c7"] = {
            "title": "Discount received",
            "steps": [
                "Discount received is the benefit gained.",
                "Discount received = amount due − amount paid.",
            ],
        }

    for c_idx, header in enumerate(headers):
        cell_id = f"r0_c{c_idx}"
        if cell_id not in correct_map:
            continue
        cell_teaching_map[cell_id] = _build_cpj_teaching_hint(
            header_label=header,
            expected=correct_map[cell_id],
            transaction_line=transaction_line,
            row_hint=_cpj_hint_text(cell_hints.get(cell_id)),
            off_journal_item=off_journal_item,
        )

    creditors_list_lines = "\n".join([f"- {creditor}: R{creditor_balances[creditor]:.2f}" for creditor in creditors])
    transactions_lines = "\n".join([
        f"- {transaction_line}",
        f"- {off_journal_day} {month}: {off_journal_item['text']}",
    ])
    prompt = (
        f"{business}\n"
        f"Cash Payments Journal (CPJ) for {month}\n\n"
        "Creditors' list:\n"
        f"{creditors_list_lines}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        "Complete only the missing cells in the CPJ entry below using the transaction that belongs in the CPJ."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["CPJ", "Cash Payments Journal", "Cash Payments Journal (CPJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="cpj",
        table_variant="studio",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="cpj", headers=headers),
        guidelines=[
            "Bank = cheque amount (amount actually paid).",
            "If settling a creditor with a discount: Creditors control = amount due; Discount received = discount.",
            "Use Trading stock / Wages when applicable; otherwise use Sundry (and write the sundry details).",
            "Only genuine cash payments belong in the CPJ; credit purchases, debit notes, and credit notes are recorded in other journals.",
        ],
    )


def _cpj_variant_defs() -> List[Dict[str, Any]]:
    return [
        {
            "id": "A",
            "headers": [
                "Doc",
                "Day",
                "Name of payee",
                "Fol",
                "Bank",
                "Trading stock",
                "Wages",
                "Debtors control (R/D)",
                "Creditors control",
                "Discount received",
                "Sundry amount",
                "Sundry fol",
                "Sundry details",
            ],
            "header_rows": None,
        },
        {
            "id": "B",
            "headers": [
                "Doc",
                "Day",
                "Name of payee",
                "Fol",
                "Bank",
                "Trading stock",
                "Debtors control (R/D)",
                "Creditors control",
                "Discount received",
                "Sundry amount",
                "Sundry fol",
                "Sundry details",
            ],
            "header_rows": None,
        },
        {
            "id": "C",
            "headers": [
                "EFT",
                "Day",
                "Name of payee",
                "Bank",
                "Trading stock",
                "Equipment",
                "Creditors control",
                "Discount received",
                "Sundry amount",
                "Sundry details",
            ],
            "header_rows": None,
        },
        {
            "id": "D",
            "headers": [
                "EFT",
                "Day",
                "Details",
                "Bank",
                "Trading stock",
                "Equipment",
                "Creditors control (Payments)",
                "Creditors control (Discount received)",
                "Sundry amount",
                "Sundry details",
            ],
            "header_rows": [
                [
                    {"label": "EFT", "rowSpan": 2, "colSpan": 1},
                    {"label": "Day", "rowSpan": 2, "colSpan": 1},
                    {"label": "Details", "rowSpan": 2, "colSpan": 1},
                    {"label": "Bank", "rowSpan": 2, "colSpan": 1},
                    {"label": "Trading stock", "rowSpan": 2, "colSpan": 1},
                    {"label": "Equipment", "rowSpan": 2, "colSpan": 1},
                    {"label": "Creditors control", "rowSpan": 1, "colSpan": 2},
                    {"label": "Sundry accounts", "rowSpan": 1, "colSpan": 2},
                ],
                [
                    {"label": "Payments", "rowSpan": 1, "colSpan": 1},
                    {"label": "Discount received", "rowSpan": 1, "colSpan": 1},
                    {"label": "Amount", "rowSpan": 1, "colSpan": 1},
                    {"label": "Details", "rowSpan": 1, "colSpan": 1},
                ],
            ],
        },
    ]


def make_cpj_activity5_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
) -> Dict[str, Any]:
    business = pick_business_name(r=r)

    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013, 2014]))
    n_tx = int(r.choice([5, 6]))
    days = sorted(r.sample([1, 2, 4, 5, 8, 10, 12, 14, 15, 18, 20, 22, 23, 26, 27, 29, 30], k=n_tx))
    must_total = bool(r.choice([True, False]))
    mode_norm = str(mode or "").strip().lower()
    off_journal_item = _make_cpj_off_journal_item(r=r)
    off_journal_day = int(r.choice([3, 6, 9, 11, 17, 21, 24, 28]))

    vdefs = _cpj_variant_defs()
    if variant_id is None:
        vdef = r.choice(vdefs)
    else:
        want = str(variant_id).strip().upper()
        vdef = next((vd for vd in vdefs if str(vd.get("id") or "").strip().upper() == want), None) or r.choice(vdefs)
    headers: List[str] = list(vdef["headers"])
    header_rows = vdef.get("header_rows")
    variant_id = str(vdef.get("id") or "A")

    def _col(name: str) -> Optional[int]:
        n = str(name).strip().lower()
        for i, h in enumerate(headers):
            if str(h).strip().lower() == n:
                return i
        return None

    def _has(name: str) -> bool:
        return _col(name) is not None

    def _fmt_money(x: Optional[float]) -> str:
        if x is None:
            return ""
        return f"{round_money(x):.2f}"

    def _build_activity_narrative(tx: Dict[str, Any]) -> str:
        doc = str(tx.get("doc") or "").strip()
        details = str(tx.get("details") or "").strip()
        bank_amt = float(tx.get("bank") or 0.0)
        doc_upper = doc.upper()
        doc_prefix = f"{doc} " if doc else ""

        if tx.get("trading_stock") is not None:
            return f"{doc_prefix}Bought trading stock for cash and paid {details}, R{bank_amt:.2f}."
        if tx.get("equipment") is not None:
            return f"{doc_prefix}Bought equipment and paid {details}, R{bank_amt:.2f}."
        if tx.get("wages") is not None:
            return f"{doc_prefix}Paid wages, R{bank_amt:.2f}."
        if tx.get("debtors_control") is not None:
            if doc_upper in {"B/S", "BS"}:
                return f"Paid {details}, R{bank_amt:.2f}, according to the bank statement."
            return f"{doc_prefix}Paid {details}, R{bank_amt:.2f}."

        label = str(tx.get("sundry_details") or "").strip()
        if doc_upper in {"B/S", "BS"}:
            return f"Paid {label or details}, R{bank_amt:.2f}, according to the bank statement."
        if label and details and details.lower() != "cash":
            return f"{doc_prefix}Paid {label.lower()} to {details}, R{bank_amt:.2f}."
        if label:
            return f"{doc_prefix}Paid {label.lower()}, R{bank_amt:.2f}."
        return f"{doc_prefix}{details}, R{bank_amt:.2f}."

    doc_header = "Doc" if _has("Doc") else "EFT"
    payee_header = "Name of payee" if _has("Name of payee") else "Details"

    start_no = int(r.choice([124, 125, 126, 130, 210, 311, 312]))
    doc_iter = iter([str(start_no + i) for i in range(60)])

    creditors = pick_business_names(r=r, k=7)
    used_creditors = r.sample(creditors, k=3)
    creditor_balances: Dict[str, float] = {c: float(r.randrange(2000, 15000 + 1, 100)) for c in used_creditors}

    tx_templates: List[Dict[str, Any]] = []

    creditor_for_settlement = r.choice(list(creditor_balances.keys()))
    amount_due = float(creditor_balances[creditor_for_settlement])
    settlement_kind = r.choice(["discount_pct", "discount_amount", "paid_and_due", "part_payment"])
    discount_pct: Optional[float] = None

    if settlement_kind == "discount_pct":
        discount_pct = float(r.choice([5, 10]))
        discount_received = round_money(amount_due * (discount_pct / 100.0))
        bank_paid = round_money(amount_due - discount_received)
        creditors_control = amount_due
    elif settlement_kind == "discount_amount":
        discount_received = float(r.choice([50, 80, 100, 150, 200, 250, 300]))
        if discount_received >= amount_due:
            discount_received = 0.0
        discount_received = round_money(discount_received)
        bank_paid = round_money(amount_due - discount_received)
        creditors_control = amount_due
    elif settlement_kind == "paid_and_due":
        bank_paid = float(r.randrange(500, int(amount_due) + 1, 50))
        bank_paid = round_money(bank_paid)
        discount_received = round_money(amount_due - bank_paid)
        creditors_control = amount_due
    else:
        bank_paid = float(r.randrange(500, int(amount_due) + 1, 50))
        bank_paid = round_money(bank_paid)
        discount_received = None
        creditors_control = bank_paid

    settlement_doc = "B/S" if r.choice([False, False, True]) else next(doc_iter)
    if settlement_kind == "discount_pct":
        if settlement_doc.upper() in {"B/S", "BS"}:
            settlement_narrative = (
                f"Paid {creditor_for_settlement} in settlement of account R{amount_due:.2f}, less {discount_pct:g}% discount, according to the bank statement."
            )
        else:
            settlement_narrative = (
                f"{settlement_doc} Paid {creditor_for_settlement} in settlement of account R{amount_due:.2f}, less {discount_pct:g}% discount."
            )
    elif settlement_kind == "discount_amount":
        if settlement_doc.upper() in {"B/S", "BS"}:
            settlement_narrative = (
                f"Paid {creditor_for_settlement} in settlement of account R{amount_due:.2f}, according to the bank statement. "
                f"Discount received R{(discount_received or 0.0):.2f}."
            )
        else:
            settlement_narrative = (
                f"{settlement_doc} Paid {creditor_for_settlement} in settlement of account R{amount_due:.2f}. "
                f"Discount received R{(discount_received or 0.0):.2f}."
            )
    elif settlement_kind == "paid_and_due":
        if settlement_doc.upper() in {"B/S", "BS"}:
            settlement_narrative = (
                f"Paid {creditor_for_settlement} R{bank_paid:.2f} in settlement of a debt of R{amount_due:.2f}, according to the bank statement."
            )
        else:
            settlement_narrative = (
                f"{settlement_doc} Paid {creditor_for_settlement} R{bank_paid:.2f} in settlement of a debt of R{amount_due:.2f}."
            )
    else:
        if settlement_doc.upper() in {"B/S", "BS"}:
            settlement_narrative = (
                f"Paid {creditor_for_settlement} R{bank_paid:.2f} as part-payment towards an account of R{amount_due:.2f}, according to the bank statement."
            )
        else:
            settlement_narrative = (
                f"{settlement_doc} Paid {creditor_for_settlement} R{bank_paid:.2f} as part-payment towards an account of R{amount_due:.2f}."
            )

    tx_templates.append({
        "doc": settlement_doc,
        "details": creditor_for_settlement,
        "narrative": settlement_narrative,
        "bank": bank_paid,
        "trading_stock": None,
        "equipment": None,
        "creditors_control": creditors_control,
        "discount_received": discount_received,
        "debtors_control": None,
        "wages": None,
        "sundry_amount": None,
        "sundry_details": "",
    })

    if _has("Trading stock"):
        stock = float(r.randrange(500, 15000 + 1, 50))
        tx_templates.append({
            "doc": next(doc_iter),
            "details": r.choice(creditors),
            "bank": stock,
            "trading_stock": stock,
            "equipment": None,
            "creditors_control": None,
            "discount_received": None,
            "debtors_control": None,
            "wages": None,
            "sundry_amount": None,
            "sundry_details": "",
        })
    if _has("Equipment"):
        eq = float(r.randrange(1000, 25000 + 1, 100))
        tx_templates.append({
            "doc": next(doc_iter),
            "details": r.choice(["Red Stores", "Codi Stores", "Junky Stores"]),
            "bank": eq,
            "trading_stock": None,
            "equipment": eq,
            "creditors_control": None,
            "discount_received": None,
            "debtors_control": None,
            "wages": None,
            "sundry_amount": None,
            "sundry_details": "",
        })

    if _has("Wages"):
        wages = float(r.randrange(800, 4000 + 1, 50))
        tx_templates.append({
            "doc": next(doc_iter),
            "details": "Cash",
            "bank": wages,
            "trading_stock": None,
            "equipment": None,
            "creditors_control": None,
            "discount_received": None,
            "debtors_control": None,
            "wages": wages,
            "sundry_amount": None,
            "sundry_details": "",
        })

    if _has("Debtors control (R/D)"):
        rd = float(r.randrange(200, 2500 + 1, 50))
        tx_templates.append({
            "doc": "B/S",
            "details": f"{pick_person_name(r=r)} (R/D)",
            "bank": rd,
            "trading_stock": None,
            "equipment": None,
            "creditors_control": None,
            "discount_received": None,
            "debtors_control": rd,
            "wages": None,
            "sundry_amount": None,
            "sundry_details": "",
        })

    sundry_menu = [
        ("Water and electricity", 400, 4000, 50),
        ("Telephone", 200, 3000, 50),
        ("Repairs", 200, 5000, 50),
        ("Insurance", 200, 6000, 100),
        ("Bank charges", 100, 2500, 10),
        ("Interest on overdraft", 50, 2000, 10),
        ("Drawings", 100, 3000, 50),
    ]

    while len(tx_templates) < n_tx:
        label, lo, hi, step = r.choice(sundry_menu)
        amt = float(r.randrange(lo, hi + 1, step))
        tx_templates.append({
            "doc": "B/S" if label in {"Bank charges", "Interest on overdraft"} else next(doc_iter),
            "details": r.choice(["Municipality", "Telkom", "RD Repairers", "Perm Bank", "FN Bank", "Cash"]),
            "bank": amt,
            "trading_stock": None,
            "equipment": None,
            "creditors_control": None,
            "discount_received": None,
            "debtors_control": None,
            "wages": None,
            "sundry_amount": amt,
            "sundry_details": label,
        })

    r.shuffle(tx_templates)
    tx_rows: List[Dict[str, Any]] = []
    for idx, tx in enumerate(tx_templates[:n_tx]):
        tx_rows.append({**tx, "day": str(days[idx]), "narrative": str(tx.get("narrative") or _build_activity_narrative(tx))})

    if mode_norm == "scaffold":
        body = tx_rows
    else:
        body = [{k: ("" if isinstance(v, str) else None) for k, v in tx_rows[0].items() if k != "day"} for _ in range(n_tx)]
        for i in range(n_tx):
            body[i]["day"] = ""

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    def _set(row_index: int, col_index: int, expected: Any) -> None:
        correct_map[f"r{row_index}_c{col_index}"] = expected

    totals_by_col: Dict[str, float] = {}

    for i, tx in enumerate(body):
        expected_tx = tx_rows[i]
        values: List[Optional[str]] = []
        for h in headers:
            hn = str(h).strip().lower()
            if hn in {"doc", "eft"}:
                values.append(tx.get("doc", ""))
            elif hn == "day":
                values.append(tx.get("day", ""))
            elif hn in {"name of payee", "details"}:
                values.append(tx.get("details", ""))
            elif hn in {"fol", "sundry fol"}:
                values.append("")
            elif hn in {"sundry details"}:
                values.append(tx.get("sundry_details", ""))
            else:
                values.append("")

        editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=list(range(len(headers))),
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        doc_col = _col(doc_header)
        if doc_col is not None:
            _set(i, doc_col, expected_tx.get("doc", ""))
        day_col = _col("Day")
        if day_col is not None:
            _set(i, day_col, expected_tx.get("day", ""))
        det_col = _col(payee_header)
        if det_col is not None:
            _set(i, det_col, expected_tx.get("details", ""))

        def _mark_money(header_name: str, amount: Optional[float]) -> None:
            c = _col(header_name)
            if c is None:
                return
            _set(i, c, _fmt_money(amount))
            if amount is not None:
                totals_by_col[header_name] = totals_by_col.get(header_name, 0.0) + float(amount)

        _mark_money("Bank", expected_tx.get("bank"))
        _mark_money("Trading stock", expected_tx.get("trading_stock"))
        _mark_money("Equipment", expected_tx.get("equipment"))
        _mark_money("Wages", expected_tx.get("wages"))
        _mark_money("Debtors control (R/D)", expected_tx.get("debtors_control"))

        _mark_money("Creditors control", expected_tx.get("creditors_control"))
        _mark_money("Creditors control (Payments)", expected_tx.get("creditors_control"))
        _mark_money("Discount received", expected_tx.get("discount_received"))
        _mark_money("Creditors control (Discount received)", expected_tx.get("discount_received"))

        _mark_money("Sundry amount", expected_tx.get("sundry_amount"))
        sd_col = _col("Sundry details")
        if sd_col is not None:
            _set(i, sd_col, expected_tx.get("sundry_details", ""))

        if mode_norm == "scaffold":
            # Hint for creditor settlement with discount.
            if expected_tx.get("discount_received") is not None and expected_tx.get("creditors_control") is not None:
                bank_col = _col("Bank")
                cc_col = _col("Creditors control")
                disc_col = _col("Discount received")
                if bank_col is not None:
                    cell_hints[f"r{i}_c{bank_col}"] = {
                        "title": "Settlement with discount",
                        "steps": [
                            "Bank = amount actually paid.",
                            "Creditors control = amount due.",
                            "Discount received = amount due − amount paid.",
                        ],
                    }
                if disc_col is not None:
                    cell_hints[f"r{i}_c{disc_col}"] = {
                        "title": "Discount received",
                        "steps": [
                            "Discount received is calculated as the difference between the amount due and the amount paid.",
                        ],
                    }

            # Hint for bank statement items.
            sdetails = str(expected_tx.get("sundry_details") or "").strip().lower()
            if sdetails in {"bank charges", "interest on overdraft"}:
                bank_col = _col("Bank")
                if bank_col is not None:
                    cell_hints[f"r{i}_c{bank_col}"] = {
                        "title": "Bank statement entry",
                        "steps": [
                            "These items are often taken from the bank statement.",
                            "Use B/S as the document reference and enter the amount in Bank and Sundry.",
                        ],
                    }

        for c_idx, header in enumerate(headers):
            cell_id = f"r{i}_c{c_idx}"
            if cell_id not in correct_map:
                continue
            cell_teaching_map[cell_id] = _build_cpj_teaching_hint(
                header_label=header,
                expected=correct_map[cell_id],
                transaction_line=str(expected_tx.get("narrative") or (str(expected_tx.get("doc") or "") + " " + str(expected_tx.get("details") or "")).strip()),
                row_hint=_cpj_hint_text(cell_hints.get(cell_id)),
                off_journal_item=off_journal_item,
            )

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = []
        for h in headers:
            hn = str(h).strip().lower()
            if hn in {"doc", "eft"}:
                totals_values.append("Total")
            elif hn == "day":
                totals_values.append("")
            else:
                totals_values.append("")
        totals_editable = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=list(range(len(headers))),
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable))
        for header_name, total in totals_by_col.items():
            c = _col(header_name)
            if c is not None:
                _set(totals_index, c, f"{round_money(total):.2f}")

        if mode_norm == "scaffold":
            for header_name, title in [
                ("Bank", "Bank totals"),
                ("Creditors control", "Creditors control totals"),
                ("Discount received", "Discount received totals"),
                ("Debtors control (R/D)", "Debtors control (R/D) totals"),
                ("Trading stock", "Trading stock totals"),
                ("Sundry amount", "Sundry totals"),
            ]:
                c = _col(header_name)
                if c is not None:
                    cell_hints[f"r{totals_index}_c{c}"] = {
                        "title": title,
                        "steps": ["Add down the column and enter the total."],
                    }
                    cell_id = f"r{totals_index}_c{c}"
                    cell_teaching_map[cell_id] = _build_cpj_teaching_hint(
                        header_label=headers[c],
                        expected=correct_map.get(cell_id),
                        transaction_line="Totals row for the CPJ",
                        row_hint=_cpj_hint_text(cell_hints.get(cell_id)),
                        off_journal_item=off_journal_item,
                    )

    creditors_list_lines = "\n".join([f"- {c}: R{creditor_balances[c]:.2f}" for c in creditor_balances])
    transactions_lines = "\n".join([
        f"{tx['day']} {month}: {tx.get('narrative') or (str(tx['doc']) + ' ' + str(tx['details'])).strip()}" for tx in tx_rows
    ] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])

    prompt = (
        f"{business}\n"
        f"Cash Payments Journal (CPJ) for {month} {year} (Variant {variant_id})\n\n"
        "Creditors’ list:\n"
        f"{creditors_list_lines}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Complete the CPJ below using only transactions that belong in the CPJ.{' Do not total/cast off the CPJ.' if not must_total else ''}"
    )

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Bank column: always enter the actual amount paid.",
            "If a creditor is paid with a discount: Creditors control = amount due; Bank = amount paid; Discount received = difference.",
            "Only genuine cash payments belong in the CPJ; credit purchases, debit notes, and credit notes are recorded in other journals.",
        ]
        if must_total:
            guidelines.append("Totals row: add down each money column and enter the totals.")

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["CPJ", "Cash Payments Journal", "Cash Payments Journal (CPJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="cpj",
        table_variant="studio",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="cpj", headers=headers) if mode_norm == "scaffold" else None,
    )


def make_cpj_exam_style_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
) -> Dict[str, Any]:
    return make_cpj_activity5_question(r=r, difficulty=difficulty, mode=mode, variant_id=variant_id)
