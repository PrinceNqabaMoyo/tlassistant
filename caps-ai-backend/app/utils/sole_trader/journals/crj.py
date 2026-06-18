from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import COST_OF_SALES_ALIASES, DEBTORS_CONTROL_ALIASES, find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, journal_editable_cols_by_difficulty, make_journal, round_money
from ..names import pick_business_name, pick_person_name, pick_person_names
from ..schemas import CRJ_HEADERS


def _crj_headers() -> List[str]:
    return list(CRJ_HEADERS)


def _pick_crj_markup(r: random.Random) -> Dict[str, Any]:
    percent_value = float(r.randrange(30, 111, 5))
    cost_factor = 100.0 / (100.0 + percent_value)
    return {
        "percent_value": percent_value,
        "percent_label": f"{int(percent_value)}",
        "cost_factor": cost_factor,
        "cost_factor_label": f"{cost_factor:.4f}".rstrip("0").rstrip("."),
    }


def _crj_analysis_amount(*, doc: Any, details: str, bank: Optional[float], sales: Optional[float], debtors_control: Optional[float], sundry_details: str = "") -> Optional[float]:
    if bank is None:
        return None
    doc_norm = str(doc or "").strip().upper()
    if doc_norm in {"B/S", "BS"}:
        return None
    if sales is not None or debtors_control is not None:
        return bank
    return bank


def _crj_extra_row_teaching_hint(*, header_label: str) -> Dict[str, str]:
    header = str(header_label or "cell").strip()
    return {
        "role_in_requirement": f"This {header} cell belongs to an extra distractor row and should stay blank if no further CRJ transaction must be recorded.",
        "evidence_from_question": "Check how many transactions actually belong in the CRJ, then compare that with the rows provided in the table.",
        "rule_or_principle": "Only transactions that belong in the CRJ are entered. If an extra row is provided after all valid CRJ entries have been recorded, leave that row blank.",
        "how_to_derive": "After recording each valid CRJ transaction, stop. Do not force the off-journal item or any non-required item into this extra row.",
        "transfer_tip": "In similar journal questions, an extra blank row may be included as a distractor to test whether you know that no additional CRJ entry is required.",
    }


def _crj_expected_text(value: Any) -> str:
    if isinstance(value, list):
        parts = [str(v).strip() for v in value if str(v).strip()]
        return " or ".join(parts)
    return "" if value is None else str(value).strip()


def _crj_hint_text(cell_hint: Any) -> str:
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


def _crj_off_journal_rule(item: Optional[Dict[str, str]]) -> str:
    if not item:
        return ""
    text = str(item.get("text") or "").strip()
    journal = str(item.get("journal") or "").strip()
    why = str(item.get("why") or "").strip()
    if not text and not journal and not why:
        return ""
    base = f"{text} does not belong in the CRJ"
    if journal:
        base += f"; record it in the {journal}"
    if why:
        base += f" because {why}"
    return base + "."


def _build_crj_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    transaction_line: str,
    row_type: str,
    row_hint: str = "",
    off_journal_item: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = _crj_expected_text(expected)
    tx_text = str(transaction_line or "").strip()
    off_journal_rule = _crj_off_journal_rule(off_journal_item)

    role = f"This cell records the {header or 'required CRJ detail'} for this receipt row."
    evidence = f"Use the wording of the cash-receipt transaction: {tx_text}" if tx_text else "Use the transaction details given in the question."
    rule = "The CRJ records money received by the business and deposited into the bank account."
    method = row_hint or "Identify what was received, identify the source document, then place the amount in the correct CRJ column."
    transfer_tip = "In similar questions, first decide whether money was actually received. If not, the item probably belongs in another journal."

    if header_norm == "doc":
        role = "This cell identifies the source document or reference for the cash receipt recorded in the CRJ."
        rule = "Use the source document that proves money was received, such as a receipt number, CRR, EFT reference, or B/S reference."
        method = f"Copy the receipt or bank reference for the cash receipt. For this row use {expected_text}." if expected_text else "Copy the receipt or bank reference linked to the cash receipt."
        transfer_tip = "In similar questions, use receipt or bank references for CRJ items, not invoices, credit notes, or debit notes."
    elif header_norm == "details":
        role = "This cell describes who paid or what the receipt was for."
        rule = "The Details column must identify the debtor, source of income, or account name linked to the receipt."
        method = f"Read who paid or what was received for, then enter that label. Here it is {expected_text}." if expected_text else method
        transfer_tip = "In similar questions, ask 'Who paid?' or 'What was the receipt for?' before filling in Details."
    elif header_norm == "analysis of receipts":
        role = "This cell records the amount of the individual receipt before or alongside the daily banking total in the CRJ."
        rule = "Analysis of receipts is a money column. Enter the amount received for that separate receipt, and leave it blank only when the receipt was deposited directly into the bank and is not analysed separately."
        method = f"Use the amount of this specific receipt. Here it is {expected_text or 'left blank because this receipt is not analysed separately'}."
        transfer_tip = "In similar questions, treat Analysis of receipts as a numeric breakdown column, not as a place for account names or details."
    elif header_norm == "bank":
        role = "This cell records the amount of money actually received into the bank account."
        rule = "The Bank column in the CRJ shows the cash or bank amount actually received."
        method = f"Take the amount received after any discount adjustments and enter it in Bank. Here the amount is {expected_text}." if expected_text else method
        transfer_tip = "In similar questions, Bank is the actual money received, not always the full amount owing."
    elif header_norm == "sales":
        role = "This cell records the selling price of trading stock sold for cash."
        rule = "Use the Sales column only for cash sales. Credit sales are recorded in the Debtors Journal, not the CRJ."
        method = f"If the transaction is cash sales, copy the selling price to Sales. Here it is {expected_text or 'blank because this is not a cash sale'}."
        transfer_tip = "In similar questions, separate cash sales from credit sales before choosing between CRJ and DJ."
    elif header_norm == "cost of sales":
        role = "This cell records the cost price side of cash sales when the perpetual inventory system requires it."
        rule = "Cost of sales is recorded for cash sales only when the question format and given information allow you to determine the cost amount."
        method = f"Use the cost amount linked to the cash sale and enter {expected_text}." if expected_text else "Only complete this when the question gives or allows you to derive the cost of sales amount."
        transfer_tip = "In similar questions, do not invent a cost figure. Use cost only when it is given or can be derived from mark-up information."
    elif header_norm in {"debtors' control", "debtors control"}:
        role = "This cell records the amount by which the debtor's account is settled in the Debtors Control column."
        rule = "For debtor settlements, Debtors Control shows the full amount owing that is being settled, not just the cash received."
        method = f"Use the amount due from the debtor. Here it is {expected_text or 'blank because no debtor account is being settled'}."
        transfer_tip = "In similar questions, compare the amount owing with the amount received to see whether discount allowed is also involved."
    elif header_norm == "discount allowed":
        role = "This cell records the discount granted to a debtor when settling an account."
        rule = "Discount allowed equals the amount owing minus the amount actually received from the debtor."
        method = f"Calculate amount due minus amount received. Here the discount allowed is {expected_text or 'blank because no discount was granted'}."
        transfer_tip = "In similar questions, only use Discount allowed when the debtor pays less than the amount owing because a discount was granted."
    elif header_norm == "sundry amount":
        role = "This cell records the money amount for receipts that do not belong in the normal Sales or Debtors Control columns."
        rule = "Use Sundry amount for receipts such as rent income, commission income, or interest received when a special column is not available."
        method = f"Enter the amount for the named sundry account. Here it is {expected_text or 'blank because this row uses another main column'}."
        transfer_tip = "In similar questions, after ruling out cash sales and debtor settlements, ask whether the receipt belongs under Sundry."
    elif header_norm == "sundry details":
        role = "This cell names the General Ledger account linked to the sundry receipt."
        rule = "Sundry details explains what account will later be posted for the sundry amount."
        method = f"Write the account name that explains the sundry receipt. Here it is {expected_text or 'blank because no sundry account is used on this row'}."
        transfer_tip = "In similar questions, use Sundry details to explain exactly what type of receipt the business received."

    if off_journal_rule:
        rule = f"{rule} {off_journal_rule}".strip()
        method = f"{method} Ignore the off-journal item when completing the CRJ table.".strip()

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def _make_crj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    debtor = pick_person_name(r=r)
    amount = float(r.randrange(250, 2500 + 1, 50))
    variant = r.choice(["credit_sale", "credit_note", "bounced_cheque", "cash_payment"])
    if variant == "credit_sale":
        invoice_no = f"INV{r.randrange(100, 999)}"
        text = f"{invoice_no} Sold goods on credit to {debtor}, R{amount:.2f}"
        return {"text": text, "journal": "DJ", "why": "it is a credit sale and no money was received"}
    if variant == "cash_payment":
        cheque_no = f"{r.randrange(120, 199)}"
        payee = r.choice(["Telkom", "RD Repairers", "City Council", pick_business_name(r=r)])
        text = f"Cheque no. {cheque_no} paid to {payee}, R{amount:.2f}"
        return {"text": text, "journal": "CPJ", "why": "it is a cash payment, so money left the bank instead of being received"}
    if variant == "bounced_cheque":
        text = f"Dishonoured cheque from {debtor} according to the bank statement (B/S), R{amount:.2f}"
        return {"text": text, "journal": "GJ", "why": "the bank reversed a previous receipt, so it is not an ordinary CRJ receipt"}
    credit_note_no = f"CN{r.randrange(100, 999)}"
    text = f"{credit_note_no} Issued a credit note to {debtor} for goods returned, R{amount:.2f}"
    return {"text": text, "journal": "DAJ", "why": "a credit note records returns or allowances, not a cash receipt"}


def make_crj_single_row_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    receipt_no = str(r.choice([142, 143, 144, 145, 146, 210]))
    day = int(r.choice([1, 4, 12, 15, 23, 27, 30]))

    debtors = pick_person_names(r=r, k=3)
    debtor_balances: Dict[str, float] = {d: float(r.randrange(1200, 6000 + 1, 100)) for d in debtors}

    kind = r.choice(["cash_sales", "other_receipt", "debtor_settlement"])
    markup_info = _pick_crj_markup(r)
    markup_label = str(markup_info["percent_label"])
    cost_factor = float(markup_info["cost_factor"])
    cost_factor_label = str(markup_info["cost_factor_label"])
    headers = _crj_headers()
    values: List[Optional[str]] = ["" for _ in range(len(headers))]

    doc_col = find_col(headers, ["Doc", "Doc. no."])
    day_col = find_col(headers, ["Day"])
    details_col = find_col(headers, ["Details"])
    doc_value = receipt_no
    if day_col is not None:
        values[day_col] = str(day)

    if kind == "cash_sales":
        doc_value = "CRR"
        amount = float(r.choice([5600, 12000, 15400, 17000, 32500]))
        details = "Cash sales"
        transaction_line = f"{day} {month}: Cash sales according to CRR, amount R{amount:.2f}."

        bank = amount
        sales = amount
        cost_of_sales = round_money(amount * cost_factor)
        debtors_control = None
        discount_allowed = None
        sundry_amount = None
        sundry_details = ""

    elif kind == "other_receipt":
        amount = float(r.choice([800, 1200, 1500, 2400, 3200, 5000]))

        receipt_type = r.choice([
            "Rent received",
            "Commission received",
            "Interest received",
        ])

        if receipt_type == "Rent received":
            details = "Rent income"
            sundry_details = "Rent income"
            transaction_line = f"{day} {month}: Received rent, receipt no. {receipt_no}, amount R{amount:.2f}."
        elif receipt_type == "Commission received":
            details = "Commission income"
            sundry_details = "Commission income"
            transaction_line = f"{day} {month}: Received commission, receipt no. {receipt_no}, amount R{amount:.2f}."
        else:
            details = "Interest received"
            sundry_details = "Interest received"
            transaction_line = f"{day} {month}: Received interest, receipt no. {receipt_no}, amount R{amount:.2f}."

        bank = amount
        sales = None
        cost_of_sales = None
        debtors_control = None
        discount_allowed = None
        sundry_amount = amount
        # Note: keep as a single sundry line here; multi-line split (e.g., fixed deposit principal + interest)
        # will be handled by a separate question type.

    else:
        debtor = r.choice(debtors)
        debtor_balance_due: Optional[float] = None
        settlement_kind = r.choice([
            "discount_pct",
            "received_and_due",
            "discount_amount",
            "part_payment",
        ])

        details = debtor
        sales = None
        cost_of_sales = None
        sundry_amount = None
        sundry_details = ""
        receipt_method = r.choice(["cheque", "EFT", "direct deposit"])
        receipt_phrase = "Received a direct deposit from" if receipt_method == "direct deposit" else f"Received a {receipt_method} from"

        if settlement_kind == "discount_pct":
            amount_due = float(r.choice([1200, 1600, 1850, 2400, 3600, 5400, 7800]))
            discount_pct = float(r.choice([5, 10]))
            discount = round_money(amount_due * (discount_pct / 100.0))
            amount_received = round_money(amount_due - discount)
            transaction_line = (
                f"{day} {month}: {receipt_phrase} {debtor} in settlement of an account of R{amount_due:.2f}, "
                f"less {discount_pct:g}% discount. Receipt no. {receipt_no}."
            )
            debtor_balance_due = amount_due
            bank = amount_received
            debtors_control = amount_due
            discount_allowed = discount

        elif settlement_kind == "received_and_due":
            amount_due = float(r.choice([800, 1200, 1600, 2000, 2400, 2800, 3600, 5400]))
            discount = float(r.choice([40, 50, 80, 100, 150, 200, 250, 300]))
            if discount >= amount_due:
                discount = 0.0
            amount_received = round_money(amount_due - discount)
            transaction_line = (
                f"{day} {month}: Issued receipt no. {receipt_no} to {debtor} for R{amount_received:.2f} received by {receipt_method}, "
                f"in settlement of a debt of R{amount_due:.2f}."
            )
            debtor_balance_due = amount_due
            bank = amount_received
            debtors_control = amount_due
            discount_allowed = discount

        elif settlement_kind == "discount_amount":
            amount_due = float(r.choice([1200, 1850, 2400, 3600, 5400, 7800]))
            discount = float(r.choice([0, 50, 80, 100, 150, 200]))
            if discount >= amount_due:
                discount = 0.0
            amount_received = round_money(amount_due - discount)
            transaction_line = (
                f"{day} {month}: {receipt_phrase} {debtor} in settlement of account R{amount_due:.2f}. "
                f"Discount allowed R{discount:.2f}. Receipt no. {receipt_no}."
            )
            debtor_balance_due = amount_due
            bank = amount_received
            debtors_control = amount_due
            discount_allowed = discount

        else:
            account_balance = float(r.choice([1600, 1850, 2400, 2600, 3600, 5400, 7800]))
            amount_received = float(r.choice([200, 300, 450, 650, 800, 1200, 1500]))
            if amount_received >= account_balance:
                amount_received = round_money(account_balance * 0.5)
            transaction_line = (
                f"{day} {month}: {receipt_phrase} {debtor}; amount R{amount_received:.2f} as part-payment towards an account "
                f"of R{account_balance:.2f}. Receipt no. {receipt_no}."
            )
            debtor_balance_due = account_balance
            bank = round_money(amount_received)
            debtors_control = round_money(amount_received)
            discount_allowed = None

        if debtor_balance_due is not None:
            debtor_balances[debtor] = round_money(debtor_balance_due)

        sales = None
        sundry_amount = None
        sundry_details = ""

    if doc_col is not None:
        values[doc_col] = doc_value
    if details_col is not None:
        values[details_col] = details

    base_editable: List[int] = []
    for col in [
        find_col(headers, ["Analysis of receipts"]),
        find_col(headers, ["Bank"]),
        find_col(headers, ["Sales"]),
        find_col(headers, COST_OF_SALES_ALIASES),
        find_col(headers, DEBTORS_CONTROL_ALIASES),
        find_col(headers, ["Discount allowed"]),
        find_col(headers, ["Sundry amount"]),
        find_col(headers, ["Sundry fol"]),
        find_col(headers, ["Sundry details"]),
    ]:
        if col is not None:
            base_editable.append(col)

    editable_cols = journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=sorted(set(base_editable)),
        total_cols=len(values),
    )

    row = build_journal_row(row_index=0, values=values, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    off_journal_item = _make_crj_off_journal_item(r=r)
    off_journal_day = int(r.choice([2, 6, 9, 11, 16, 19, 25, 28]))

    def _set(col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r0_c{col}"] = expected

    analysis_amount = _crj_analysis_amount(
        doc=doc_value,
        details=details,
        bank=bank,
        sales=sales,
        debtors_control=debtors_control,
        sundry_details=sundry_details,
    )

    _set(find_col(headers, ["Fol"]), "")
    _set(find_col(headers, ["Analysis of receipts"]), f"{analysis_amount:.2f}" if analysis_amount is not None else "")
    _set(find_col(headers, ["Bank"]), f"{bank:.2f}" if bank is not None else "")
    _set(find_col(headers, ["Sales"]), f"{sales:.2f}" if sales is not None else "")
    _set(find_col(headers, COST_OF_SALES_ALIASES), f"{cost_of_sales:.2f}" if cost_of_sales is not None else "")
    _set(
        find_col(headers, DEBTORS_CONTROL_ALIASES),
        f"{debtors_control:.2f}" if debtors_control is not None else "",
    )
    _set(find_col(headers, ["Discount allowed"]), f"{discount_allowed:.2f}" if discount_allowed is not None else "")
    _set(find_col(headers, ["Sundry amount"]), f"{sundry_amount:.2f}" if sundry_amount is not None else "")
    _set(find_col(headers, ["Sundry fol"]), "")
    _set(find_col(headers, ["Sundry details"]), sundry_details)

    if details_col is not None and (k := kind) == "debtor_settlement":
        bank_col = find_col(headers, ["Bank"])
        dc_col = find_col(headers, DEBTORS_CONTROL_ALIASES)
        disc_col = find_col(headers, ["Discount allowed"])
        if bank_col is not None:
            cell_hints[f"r0_c{bank_col}"] = {
                "title": "Debtor settlement",
                "steps": [
                    "Bank = amount received.",
                    "Debtors control = amount due.",
                    "Discount allowed = amount due − amount received (if any).",
                ],
            }
        if dc_col is not None:
            cell_hints[f"r0_c{dc_col}"] = {
                "title": "Debtors control",
                "steps": [
                    "For a settlement, Debtors control records the full amount due (not the amount received).",
                ],
            }
        if disc_col is not None:
            cell_hints[f"r0_c{disc_col}"] = {
                "title": "Discount allowed",
                "steps": [
                    "Discount allowed is only used if a discount is given.",
                    "Discount = amount due − amount received.",
                ],
            }

    if kind == "cash_sales":
        sales_col = find_col(headers, ["Sales"])
        cos_col = find_col(headers, COST_OF_SALES_ALIASES)
        if sales_col is not None:
            cell_hints[f"r0_c{sales_col}"] = {
                "title": "Cash sales",
                "steps": [
                    "The Sales column records the selling price of the cash sale.",
                    f"For this question, the business uses a mark-up of {markup_label}% on cost price.",
                ],
            }
        if cos_col is not None:
            cell_hints[f"r0_c{cos_col}"] = {
                "title": "Cost of sales (cash sales)",
                "steps": [
                    "Under the perpetual inventory system, Cost of sales is recorded for cash sales.",
                    f"Cost of sales = Sales × {cost_factor_label} when the mark-up is {markup_label}% on cost.",
                ],
            }

    for c_idx, header in enumerate(headers):
        cell_id = f"r0_c{c_idx}"
        if cell_id not in correct_map:
            continue
        cell_teaching_map[cell_id] = _build_crj_teaching_hint(
            header_label=header,
            expected=correct_map[cell_id],
            transaction_line=transaction_line,
            row_type=kind,
            row_hint=_crj_hint_text(cell_hints.get(cell_id)),
            off_journal_item=off_journal_item,
        )

    debtors_list_lines = "\n".join([f"- {debtor}: R{debtor_balances[debtor]:.2f}" for debtor in debtors])
    transactions_lines = "\n".join([
        f"- {transaction_line}",
        f"- {off_journal_day} {month}: {off_journal_item['text']}",
    ])
    note_text = f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n" if kind == "cash_sales" else ""
    prompt = (
        f"{business}\n"
        f"Cash Receipts Journal (CRJ) for {month}\n\n"
        f"{note_text}"
        "Debtors' list:\n"
        f"{debtors_list_lines}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        "Complete only the missing cells in the CRJ entry below using the transaction that belongs in the CRJ."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["CRJ", "Cash Receipts Journal", "Cash Receipts Journal (CRJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="crj",
        table_variant="grade_project",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="crj", headers=headers),
        guidelines=[
            "For a debtor settlement: Debtors control = amount due; Bank = amount received; Discount allowed = discount.",
            "For cash sales: enter the amount in Bank and Sales.",
            "For other receipts (e.g. rent/commission/interest): enter Bank, then use Sundry amount + Sundry details.",
            "Only cash receipts and receipts actually received by the business belong in the CRJ; credit sales, credit notes, and dishonoured cheques belong elsewhere.",
        ],
    )


def make_crj_activity5_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013, 2014]))

    markup_info = _pick_crj_markup(r)
    markup_label = str(markup_info["percent_label"])
    cost_factor = float(markup_info["cost_factor"])
    cost_factor_label = str(markup_info["cost_factor_label"])

    used_debtors = pick_person_names(r=r, k=3)
    debtor_balances: Dict[str, float] = {d: float(r.randrange(1500, 6500 + 1, 100)) for d in used_debtors}

    receipt_start = int(r.choice([140, 141, 142, 143, 144, 145]))
    receipt_nos = [str(receipt_start + i) for i in range(6)]
    days = sorted(r.sample([1, 2, 4, 5, 10, 12, 14, 15, 18, 22, 23, 26, 27, 29, 30], k=6))

    debtor_for_settlement = r.choice(list(debtor_balances.keys()))
    amount_due = debtor_balances[debtor_for_settlement]
    settlement_kind = r.choice([
        "discount_pct",
        "received_and_due",
        "discount_amount",
        "part_payment",
    ])

    discount_pct: Optional[float] = None

    if settlement_kind == "discount_pct":
        discount_pct = float(r.choice([5, 10]))
        discount_allowed = round_money(amount_due * (discount_pct / 100.0))
        amount_received = round_money(amount_due - discount_allowed)
        settlement_debtors_control = amount_due

    elif settlement_kind == "received_and_due":
        discount_allowed = float(r.choice([40, 50, 80, 100, 150, 200, 250, 300]))
        if discount_allowed >= amount_due:
            discount_allowed = 0.0
        discount_allowed = round_money(discount_allowed)
        amount_received = round_money(amount_due - discount_allowed)
        settlement_debtors_control = amount_due

    elif settlement_kind == "discount_amount":
        discount_allowed = float(r.choice([0, 50, 80, 100, 150, 200]))
        if discount_allowed >= amount_due:
            discount_allowed = 0.0
        discount_allowed = round_money(discount_allowed)
        amount_received = round_money(amount_due - discount_allowed)
        settlement_debtors_control = amount_due

    else:
        amount_received = float(r.choice([200, 300, 450, 650, 800, 1200, 1500]))
        if amount_received >= amount_due:
            amount_received = round_money(amount_due * 0.5)
        amount_received = round_money(amount_received)
        discount_allowed = None
        settlement_debtors_control = amount_received

    receipt_ref_iter = iter(receipt_nos)
    debtor_doc = next(receipt_ref_iter)
    settlement_method = r.choice(["cheque", "EFT", "direct deposit"])
    settlement_phrase = "Received a direct deposit from" if settlement_method == "direct deposit" else f"Received a {settlement_method} from"
    if settlement_kind == "discount_pct":
        settlement_narrative = (
            f"{debtor_doc} {settlement_phrase} {debtor_for_settlement} in settlement of an account of R{amount_due:.2f}, "
            f"less {discount_pct:g}% discount."
        )
    elif settlement_kind == "received_and_due":
        settlement_narrative = (
            f"{debtor_doc} Issued receipt no. {debtor_doc} to {debtor_for_settlement} for R{amount_received:.2f} received by {settlement_method}, "
            f"in settlement of a debt of R{amount_due:.2f}."
        )
    elif settlement_kind == "discount_amount":
        settlement_narrative = (
            f"{debtor_doc} {settlement_phrase} {debtor_for_settlement} in settlement of account R{amount_due:.2f}. "
            f"Discount allowed R{(discount_allowed or 0.0):.2f}."
        )
    else:
        settlement_narrative = (
            f"{debtor_doc} {settlement_phrase} {debtor_for_settlement}; amount R{amount_received:.2f} as part-payment towards an account "
            f"of R{amount_due:.2f}."
        )

    cash_sales_1 = float(r.randrange(1000, 20000 + 1, 10))
    cash_sales_2 = float(r.randrange(1000, 20000 + 1, 10))
    rent_received = float(r.randrange(1000, 15000 + 1, 100))
    commission_received = float(r.randrange(500, 6000 + 1, 50))
    bank_interest = float(r.randrange(50, 500 + 1, 10))

    cash_sales_doc_1 = "CRR"
    cash_sales_doc_2 = "CRR"

    chosen_sundry_keys = r.sample([
        "rent_income",
        "commission_income",
        "interest_received",
    ], k=3)
    sundry_rows: List[Dict[str, Any]] = []
    for sundry_key in chosen_sundry_keys:
        doc = next(receipt_ref_iter)
        if sundry_key == "rent_income":
            sundry_rows.append({
                "doc": doc,
                "details": "Rent income",
                "narrative": f"{doc} Received rent income of R{rent_received:.2f}.",
                "bank": rent_received,
                "sales": None,
                "cost_of_sales": None,
                "debtors_control": None,
                "discount_allowed": None,
                "sundry_amount": rent_received,
                "sundry_details": "Rent income",
            })
        elif sundry_key == "commission_income":
            sundry_rows.append({
                "doc": doc,
                "details": "Commission income",
                "narrative": f"{doc} Received commission income of R{commission_received:.2f}.",
                "bank": commission_received,
                "sales": None,
                "cost_of_sales": None,
                "debtors_control": None,
                "discount_allowed": None,
                "sundry_amount": commission_received,
                "sundry_details": "Commission income",
            })
        else:
            sundry_rows.append({
                "doc": doc,
                "details": "Interest received",
                "narrative": f"{doc} Interest received, R{bank_interest:.2f}.",
                "bank": bank_interest,
                "sales": None,
                "cost_of_sales": None,
                "debtors_control": None,
                "discount_allowed": None,
                "sundry_amount": bank_interest,
                "sundry_details": "Interest received",
            })

    tx_rows: List[Dict[str, Any]] = [
        {
            "doc": cash_sales_doc_1,
            "details": "Sales",
            "narrative": f"{(cash_sales_doc_1 + ' ') if cash_sales_doc_1 else ''}Cash sales amounted to R{cash_sales_1:.2f}.",
            "bank": cash_sales_1,
            "sales": cash_sales_1,
            "cost_of_sales": round_money(cash_sales_1 * cost_factor),
            "debtors_control": None,
            "discount_allowed": None,
            "sundry_amount": None,
            "sundry_details": "",
        },
        {
            "doc": debtor_doc,
            "details": debtor_for_settlement,
            "narrative": settlement_narrative,
            "bank": amount_received,
            "sales": None,
            "cost_of_sales": None,
            "debtors_control": settlement_debtors_control,
            "discount_allowed": discount_allowed,
            "sundry_amount": None,
            "sundry_details": "",
        },
        {
            "doc": cash_sales_doc_2,
            "details": "Sales",
            "narrative": f"{(cash_sales_doc_2 + ' ') if cash_sales_doc_2 else ''}Cash sales amounted to R{cash_sales_2:.2f}.",
            "bank": cash_sales_2,
            "sales": cash_sales_2,
            "cost_of_sales": round_money(cash_sales_2 * cost_factor),
            "debtors_control": None,
            "discount_allowed": None,
            "sundry_amount": None,
            "sundry_details": "",
        },
        *sundry_rows,
    ]
    r.shuffle(tx_rows)
    for i, tx in enumerate(tx_rows):
        tx["day"] = str(days[i])

    mode_norm = str(mode or "").strip().lower()
    must_total = bool(r.choice([True, False]))
    off_journal_item = _make_crj_off_journal_item(r=r)
    off_journal_day = int(r.choice([3, 7, 10, 14, 18, 21, 24, 29]))
    expected_rows = tx_rows
    if mode_norm == "scaffold":
        body = tx_rows
    else:
        body = [{
            "doc": "",
            "day": "",
            "details": "",
            "narrative": "",
            "bank": None,
            "sales": None,
            "cost_of_sales": None,
            "debtors_control": None,
            "discount_allowed": None,
            "sundry_amount": None,
            "sundry_details": "",
        } for _ in range(len(tx_rows))]

    headers = _crj_headers()
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    def _set(row_index: int, col_index: int, expected: Any) -> None:
        correct_map[f"r{row_index}_c{col_index}"] = expected

    def _fmt(x: Optional[float]) -> str:
        return f"{x:.2f}" if x is not None else ""

    bank_total = 0.0
    sales_total = 0.0
    cos_total = 0.0
    debtors_total = 0.0
    discount_total = 0.0
    sundry_total = 0.0

    for i, tx in enumerate(body):
        expected_tx = expected_rows[i]
        if mode_norm == "scaffold":
            values: List[Optional[str]] = [
                tx["doc"],
                tx["day"],
                tx["details"],
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                tx.get("sundry_details", ""),
            ]
            editable_cols = journal_editable_cols_by_difficulty(
                difficulty=difficulty,
                base_editable_cols=[4, 5, 6, 7, 8, 9, 10, 11, 12],
                total_cols=len(values),
            )
        else:
            values = ["" for _ in range(len(headers))]
            editable_cols = list(range(len(headers)))

        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        bank = float(expected_tx["bank"]) if expected_tx.get("bank") is not None else None
        sales = float(expected_tx["sales"]) if expected_tx.get("sales") is not None else None
        cos = float(expected_tx["cost_of_sales"]) if expected_tx.get("cost_of_sales") is not None else None
        debtors_val = float(expected_tx["debtors_control"]) if expected_tx.get("debtors_control") is not None else None
        disc = float(expected_tx["discount_allowed"]) if expected_tx.get("discount_allowed") is not None else None
        sundry = float(expected_tx["sundry_amount"]) if expected_tx.get("sundry_amount") is not None else None

        expected_doc = expected_tx.get("doc", "")
        expected_doc_norm = str(expected_doc).strip().upper()
        if expected_doc_norm == "":
            _set(i, 0, ["CRR"])
        elif expected_doc_norm in {"B/S", "BS"}:
            _set(i, 0, ["B/S", "BS"])
        else:
            _set(i, 0, expected_doc)
        _set(i, 1, expected_tx.get("day", ""))
        _set(i, 2, expected_tx.get("details", ""))
        _set(i, 3, "")

        analysis_amount = _crj_analysis_amount(
            doc=expected_tx.get("doc", ""),
            details=str(expected_tx.get("details", "")),
            bank=bank,
            sales=sales,
            debtors_control=debtors_val,
            sundry_details=str(expected_tx.get("sundry_details", "") or ""),
        )

        _set(i, 4, _fmt(analysis_amount))
        _set(i, 5, _fmt(bank))
        _set(i, 6, _fmt(sales))
        _set(i, 7, _fmt(cos))
        _set(i, 8, _fmt(debtors_val))
        _set(i, 9, _fmt(disc))
        _set(i, 10, _fmt(sundry))
        _set(i, 11, "")
        _set(i, 12, expected_tx.get("sundry_details", ""))

        if mode_norm == "scaffold":
            details_norm = str(expected_tx.get("details", "") or "").strip().lower()
            if details_norm in {"sales"} and expected_tx.get("cost_of_sales") is not None:
                cell_hints[f"r{i}_c7"] = {
                    "title": "Cost of sales (perpetual inventory)",
                    "steps": [
                        f"Mark-up of {markup_label}% on cost means: Cost = Selling price × {cost_factor_label}.",
                        f"So Cost of sales = Sales × {cost_factor_label}.",
                    ],
                }
            if expected_tx.get("discount_allowed") is not None and expected_tx.get("debtors_control") is not None:
                cell_hints[f"r{i}_c9"] = {
                    "title": "Discount allowed",
                    "steps": [
                        "For debtor settlement: Discount allowed = amount due − amount received.",
                        "Debtors control records the amount due.",
                    ],
                }

        for c_idx, header in enumerate(headers):
            cell_id = f"r{i}_c{c_idx}"
            if cell_id not in correct_map:
                continue
            cell_teaching_map[cell_id] = _build_crj_teaching_hint(
                header_label=header,
                expected=correct_map[cell_id],
                transaction_line=str(expected_tx.get("narrative") or (str(expected_tx.get("doc") or "") + " " + str(expected_tx.get("details") or "")).strip()),
                row_type="cash_sales" if str(expected_tx.get("details") or "").strip().lower() == "sales" else ("debtor_settlement" if expected_tx.get("debtors_control") is not None else "other_receipt"),
                row_hint=_crj_hint_text(cell_hints.get(cell_id)),
                off_journal_item=off_journal_item,
            )

        bank_total += bank or 0.0
        sales_total += sales or 0.0
        cos_total += cos or 0.0
        debtors_total += debtors_val or 0.0
        discount_total += disc or 0.0
        sundry_total += sundry or 0.0

    extra_row_index = len(rows)
    extra_row_values = ["" for _ in range(len(headers))]
    extra_row_editable = journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=list(range(len(headers))),
        total_cols=len(extra_row_values),
    )
    rows.append(build_journal_row(row_index=extra_row_index, values=extra_row_values, editable_cols=extra_row_editable))
    for c_idx, header in enumerate(headers):
        cell_id = f"r{extra_row_index}_c{c_idx}"
        _set(extra_row_index, c_idx, "")
        cell_hints[cell_id] = {
            "title": "Extra row not required",
            "steps": [
                "This extra row is a distractor.",
                "If all valid CRJ transactions have already been recorded, leave this row blank.",
            ],
        }
        cell_teaching_map[cell_id] = _crj_extra_row_teaching_hint(header_label=header)

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = [
            "",
            "",
            "Totals",
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
        totals_editable = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=[5, 6, 7, 8, 9, 10],
            total_cols=len(totals_values),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable))

        _set(totals_index, 5, f"{round_money(bank_total):.2f}")
        _set(totals_index, 6, f"{round_money(sales_total):.2f}")
        _set(totals_index, 7, f"{round_money(cos_total):.2f}")
        _set(totals_index, 8, f"{round_money(debtors_total):.2f}")
        _set(totals_index, 9, f"{round_money(discount_total):.2f}")
        _set(totals_index, 10, f"{round_money(sundry_total):.2f}")

        if mode_norm == "scaffold":
            for c, title in [
                (5, "Bank totals"),
                (6, "Sales totals"),
                (7, "Cost of sales totals"),
                (8, "Debtors control totals"),
                (9, "Discount allowed totals"),
                (10, "Sundry totals"),
            ]:
                cell_hints[f"r{totals_index}_c{c}"] = {
                    "title": title,
                    "steps": [
                        "Add down the column and enter the total.",
                        "Only total the money columns.",
                    ],
                }
                cell_id = f"r{totals_index}_c{c}"
                cell_teaching_map[cell_id] = _build_crj_teaching_hint(
                    header_label=headers[c],
                    expected=correct_map.get(cell_id),
                    transaction_line="Totals row for the CRJ",
                    row_type="totals",
                    row_hint=_crj_hint_text(cell_hints.get(cell_id)),
                    off_journal_item=off_journal_item,
                )

    debtors_list_lines = "\n".join([f"- {d}: R{debtor_balances[d]:.2f}" for d in debtor_balances])
    transactions_lines = "\n".join([
        f"{tx['day']} {month}: {tx.get('narrative') or (str(tx['doc']) + ' ' + tx['details']).strip()}" for tx in tx_rows
    ] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])

    prompt = (
        f"{business}\n"
        f"Cash Receipts Journal (CRJ) for {month} {year}\n\n"
        f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        "Debtors’ list:\n"
        f"{debtors_list_lines}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Complete the CRJ below using only transactions that belong in the CRJ.{' Do not total/cast off the CRJ.' if not must_total else ''}"
    )

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "CRR = Cash Register Roll.",
            "Continuous inventory: Cost of sales is recorded for sales transactions.",
            f"Mark-up of {markup_label}% on cost means: Cost = Selling price × {cost_factor_label}.",
            "For a debtor settlement with discount: Debtors’ control = amount due; Bank = amount received; Discount allowed = difference.",
            "Only genuine cash receipts belong in the CRJ; cash payments, credit sales, credit notes, and dishonoured cheques are recorded in other journals.",
            "One blank row may be extra. If no further CRJ transaction is required, leave that extra row blank.",
        ]
        if must_total:
            guidelines.append("Totals row: add down each money column and enter the totals.")

    title_fields = [
        {
            "cell_id": "title_business",
            "label": "Business name",
            "editable": True,
        },
        {
            "cell_id": "title_period",
            "label": "Month/Year",
            "editable": True,
        },
        {
            "cell_id": "title_journal",
            "label": "Journal",
            "editable": True,
        },
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["CRJ", "Cash Receipts Journal", "Cash Receipts Journal (CRJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="crj",
        table_variant="studio",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="crj", headers=headers) if mode_norm == "scaffold" else None,
    )


def make_crj_exam_style_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    return make_crj_activity5_question(r=r, difficulty=difficulty, mode=mode)
