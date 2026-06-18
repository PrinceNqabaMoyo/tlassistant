from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_journal_row as _build_journal_row
from ..sole_trader.names import pick_business_name as _pick_business_name
from ..sole_trader.names import pick_person_names as _pick_person_names

from .sole_trader_ledger_helpers import build_running_ledger_teaching_hint as _build_running_ledger_teaching_hint
from .sole_trader_ledger_helpers import running_balance_ledger_headers as _running_balance_ledger_headers


def make_debtors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    business = _pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    debtor_names = _pick_person_names(r=r, k=3)
    debtor = debtor_names[0]
    distractor_debtor = debtor_names[1]
    distractor_creditor = _pick_business_name(r=r)
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    headers = _running_balance_ledger_headers()
    opening_balance = float(r.choice([3500, 4800, 5600, 7000, 8200, 9500]))
    sale_amount = float(r.choice([2500, 3200, 4000, 5000, 6200]))
    receipt_amount = min(float(r.choice([1800, 2400, 3000, 4200, 6800])), _round_money((opening_balance + sale_amount) * 0.7))
    discount_allowed = float(r.choice([0, 100, 150, 200, 225]))
    credit_note_amount = float(r.choice([0, 450, 600, 900]))
    dishonoured = bool(r.choice([True, False]))
    interest_rate_pct = float(r.choice([4.0, 6.0, 8.0]))
    invoice_no = str(r.choice(["101", "102", "105", "123"]))
    receipt_no = str(r.choice(["4002", "4020", "76", "142"]))
    credit_note_no = str(r.choice(["11", "12", "18", "25"]))

    tx: List[Dict[str, Any]] = [
        {"day": 1, "details": "Balance b/d", "fol": "b/d", "debit": 0.0, "credit": 0.0, "balance": opening_balance},
        {"day": 5, "details": f"Invoice No. {invoice_no}", "fol": "DJ3", "debit": sale_amount, "credit": 0.0, "balance": 0.0},
        {"day": 10, "details": f"Receipt No. {receipt_no}", "fol": "CRJ3", "debit": 0.0, "credit": receipt_amount, "balance": 0.0},
    ]
    if discount_allowed > 0:
        tx.append({"day": 10, "details": "Discount allowed", "fol": "CRJ3", "debit": 0.0, "credit": discount_allowed, "balance": 0.0})
    if credit_note_amount > 0:
        tx.append({"day": 15, "details": f"Credit Note No. {credit_note_no}", "fol": "DAJ3", "debit": 0.0, "credit": credit_note_amount, "balance": 0.0})
    if dishonoured:
        tx.append({"day": 20, "details": "Dishonoured cheque (R/D)", "fol": "GJ3", "debit": receipt_amount, "credit": 0.0, "balance": 0.0})
        if discount_allowed > 0:
            tx.append({"day": 20, "details": "Discount cancelled", "fol": "GJ3", "debit": discount_allowed, "credit": 0.0, "balance": 0.0})
    interest = _round_money(opening_balance * (interest_rate_pct / 100.0))
    tx.append({"day": 25, "details": "Interest income", "fol": "GJ3", "debit": interest, "credit": 0.0, "balance": 0.0})

    running = opening_balance
    for index in range(1, len(tx)):
        running = _round_money(running + float(tx[index]["debit"]) - float(tx[index]["credit"]))
        tx[index]["balance"] = running

    if diff == "easy":
        editable_cols: List[int] = [3, 4, 5]
    elif diff == "medium":
        editable_cols = [1, 2, 3, 4, 5]
    else:
        editable_cols = list(range(6))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    for row_index, transaction in enumerate(tx):
        values: List[Optional[str]] = [
            str(transaction["day"]),
            str(transaction["details"]),
            str(transaction["fol"]),
            _fmt_money(float(transaction["debit"])) if transaction["debit"] else "",
            _fmt_money(float(transaction["credit"])) if transaction["credit"] else "",
            _fmt_money(float(transaction["balance"])),
        ]
        rows.append(_build_journal_row(row_index=row_index, values=values, editable_cols=editable_cols))
        previous_balance = float(tx[row_index - 1]["balance"]) if row_index > 0 else None
        for cix, value in enumerate(values):
            if cix not in editable_cols:
                continue
            key = f"r{row_index}_c{cix}"
            correct_map[key] = value
            if mode_norm == "scaffold" and value:
                cell_teaching_map[key] = _build_running_ledger_teaching_hint(
                    header_label=headers[cix],
                    expected=value,
                    ledger_kind="debtors",
                    transaction_line=f"{transaction['details']} on {transaction['day']} {month}",
                    previous_balance=previous_balance,
                    debit_value=float(transaction["debit"]),
                    credit_value=float(transaction["credit"]),
                    balance_value=float(transaction["balance"]),
                )
        if mode_norm == "scaffold" and row_index > 0:
            cell_hints[f"r{row_index}_c5"] = f"Balance = previous balance + debit - credit = {_fmt_money(previous_balance or 0.0)} + {_fmt_money(float(transaction['debit']))} - {_fmt_money(float(transaction['credit']))}."

    prompt_lines = [
        business,
        f"Debtors Ledger ({debtor}) for {month}",
        "",
        "Information:",
        f"- Opening balance on 1 {month}: R{opening_balance:.2f}",
        f"- 5 {month}: Sold goods on credit, Invoice {invoice_no}, R{sale_amount:.2f}",
        f"- 10 {month}: Received payment, Receipt {receipt_no}, R{receipt_amount:.2f}",
        f"- A separate memo for the month mentions debtor {distractor_debtor} and supplier {distractor_creditor} in other subsidiary accounts.",
    ]
    if discount_allowed > 0:
        prompt_lines.append(f"- 10 {month}: Discount allowed, R{discount_allowed:.2f}")
    if credit_note_amount > 0:
        prompt_lines.append(f"- 15 {month}: Goods returned, Credit note {credit_note_no}, R{credit_note_amount:.2f}")
    if dishonoured:
        prompt_lines.append(f"- 20 {month}: The cheque from Receipt {receipt_no} was returned unpaid.")
        if discount_allowed > 0:
            prompt_lines.append(f"- 20 {month}: Discount allowed on Receipt {receipt_no} is cancelled.")
    prompt_lines.append(f"- 25 {month}: Interest charged at {interest_rate_pct:g}% on opening balance")
    prompt_lines.extend(["", "Required:", f"Complete the Debtors Ledger account of {debtor} and show the running balance after each posting."])

    out = _make_journal(
        prompt="\n".join(prompt_lines),
        journal_type="debtors_ledger",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Debit increases the amount the debtor owes; credit decreases it.",
            "Balance is a running total: previous balance + debit - credit.",
            f"Only transactions that belong to {debtor}'s account must be posted.",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
    )
    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    out["cell_teaching_map"] = cell_teaching_map if cell_teaching_map else None
    return out


def make_creditors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    creditor = r.choice(["Marang Suppliers", "RN Wholesalers", "Sam Distributors", "MZ Suppliers"])
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    headers = _running_balance_ledger_headers()
    opening_balance = float(r.choice([6840, 9840, 11240, 12840, 15600]))
    purchase_amount = float(r.choice([4200, 5600, 6840, 7900]))
    return_amount = float(r.choice([0, 0, 900, 1200, 1830]))
    payment_amount = float(r.choice([2500, 3600, 4500, 7500]))
    if payment_amount >= opening_balance:
        payment_amount = _round_money((opening_balance + purchase_amount) * 0.5)

    trade_discount_pct = float(r.choice([0, 0, 5.0, 10.0]))
    invoice_gross = float(r.choice([6500, 8200, 9000, 10400]))
    invoice_net = _round_money(invoice_gross * (1.0 - (trade_discount_pct / 100.0)))

    invoice_no1 = str(r.choice(["201", "202", "XXX"]))
    invoice_no2 = str(r.choice(["204", "205", "XXX"]))
    debit_note_no = str(r.choice(["11", "18", "XXX"]))
    cheque_no = str(r.choice(["2211", "3010", "4512"]))

    tx: List[Dict[str, Any]] = []
    tx.append({"day": 1, "details": "Account rendered", "fol": "b/d", "debit": 0.0, "credit": 0.0, "balance": opening_balance})
    tx.append({"day": 6, "details": f"Invoice No. {invoice_no1}", "fol": "CJ3", "debit": 0.0, "credit": purchase_amount, "balance": 0.0})
    if return_amount > 0:
        tx.append({"day": 14, "details": f"Debit note No. {debit_note_no}", "fol": "CAJ3", "debit": return_amount, "credit": 0.0, "balance": 0.0})
    tx.append({"day": 22, "details": f"Cheque No. {cheque_no}", "fol": "CPJ3", "debit": payment_amount, "credit": 0.0, "balance": 0.0})
    tx.append({"day": 25, "details": f"Invoice No. {invoice_no2}", "fol": "CJ3", "debit": 0.0, "credit": invoice_net, "balance": 0.0})

    running = opening_balance
    for index in range(1, len(tx)):
        running = _round_money(running + float(tx[index]["credit"]) - float(tx[index]["debit"]))
        tx[index]["balance"] = running

    if diff == "easy":
        editable_cols: List[int] = [3, 4, 5]
    else:
        editable_cols = list(range(6))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    working_map: Dict[str, str] = {}

    for index, transaction in enumerate(tx):
        values: List[Optional[str]] = [
            str(transaction["day"]),
            str(transaction["details"]),
            str(transaction["fol"]),
            _fmt_money(float(transaction["debit"])) if transaction["debit"] else "",
            _fmt_money(float(transaction["credit"])) if transaction["credit"] else "",
            _fmt_money(float(transaction["balance"])),
        ]
        rows.append(_build_journal_row(row_index=index, values=values, editable_cols=editable_cols))

        if diff != "easy":
            correct_map[f"r{index}_c0"] = str(transaction["day"])
            correct_map[f"r{index}_c1"] = str(transaction["details"])
            correct_map[f"r{index}_c2"] = str(transaction["fol"])
        else:
            correct_map[f"r{index}_c0"] = str(transaction["day"])
        correct_map[f"r{index}_c3"] = _fmt_money(float(transaction["debit"])) if transaction["debit"] else ""
        correct_map[f"r{index}_c4"] = _fmt_money(float(transaction["credit"])) if transaction["credit"] else ""
        correct_map[f"r{index}_c5"] = _fmt_money(float(transaction["balance"]))

        if mode_norm == "scaffold":
            if index == 0:
                cell_hints[f"r{index}_c5"] = "Opening balance: amount owed to the creditor at the start of the month."
            if "Invoice" in str(transaction["details"]):
                cell_hints[f"r{index}_c4"] = "Credit purchase increases what we owe (credit column)."
            if "Debit note" in str(transaction["details"]):
                cell_hints[f"r{index}_c3"] = "Returns/allowances reduce what we owe (debit column)."
            if "Cheque" in str(transaction["details"]):
                cell_hints[f"r{index}_c3"] = "Payment reduces what we owe (debit column)."
            if trade_discount_pct > 0 and transaction["details"] == f"Invoice No. {invoice_no2}":
                cell_hints[f"r{index}_c4"] = f"Net invoice = Gross x (1 - discount%) = {_fmt_money(invoice_gross)} x (1 - {trade_discount_pct:g}%/100) = {_fmt_money(invoice_net)}"
            if index > 0:
                previous_balance = float(tx[index - 1]["balance"])
                debit_amount = float(transaction["debit"])
                credit_amount = float(transaction["credit"])
                cell_hints[f"r{index}_c5"] = f"Balance = previous balance + credit - debit = {_fmt_money(previous_balance)} + {_fmt_money(credit_amount)} - {_fmt_money(debit_amount)} = {_fmt_money(float(transaction['balance']))}"

    prompt_lines = [
        f"{business}",
        f"Creditors Ledger ({creditor}) for {month}",
        "",
        "Information:",
        f"- Opening balance on 1 {month}: R{opening_balance:.2f}",
        f"- 6 {month}: Bought goods on credit, Invoice {invoice_no1}, R{purchase_amount:.2f}",
    ]
    if return_amount > 0:
        prompt_lines.append(f"- 14 {month}: Returned unsatisfactory goods, Debit note {debit_note_no}, R{return_amount:.2f}")
    prompt_lines.append(f"- 22 {month}: Paid by cheque {cheque_no}, R{payment_amount:.2f}")
    if trade_discount_pct > 0:
        prompt_lines.append(f"- 25 {month}: Bought goods on credit, Invoice {invoice_no2}, gross R{invoice_gross:.2f}, trade discount {trade_discount_pct:g}%")
    else:
        prompt_lines.append(f"- 25 {month}: Bought goods on credit, Invoice {invoice_no2}, R{invoice_net:.2f}")
    prompt_lines.extend(["", "Required:", "Complete the Creditors Ledger account (running balance)."])

    out = _make_journal(
        prompt="\n".join(prompt_lines),
        journal_type="creditors_ledger",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Credit increases the amount owed to the creditor; debit decreases it.",
            "Balance is a running total: previous balance + credit - debit.",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
        working_map=working_map if mode_norm == "scaffold" else None,
    )

    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    return out
