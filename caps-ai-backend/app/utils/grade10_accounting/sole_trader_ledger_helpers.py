from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..sole_trader.core import fmt_money as _fmt_money


def running_balance_ledger_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Debit",
        "Credit",
        "Balance",
    ]


def crj_totals_headers_ledger() -> List[str]:
    return [
        "Doc",
        "Day",
        "Details",
        "Analysis of receipts",
        "Bank",
        "Sales",
        "Cost of Sales",
        "Debtors' Control",
        "Discount allowed",
        "Current income",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def cpj_totals_headers_ledger() -> List[str]:
    return [
        "Doc",
        "Day",
        "Name of payee",
        "Analysis of payments",
        "Bank",
        "Trading stock",
        "Creditors control",
        "Discount received",
        "Wages",
        "Stationery",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def general_ledger_account_headers() -> List[str]:
    return [
        "Month",
        "Day",
        "Details",
        "Fol",
        "Amount",
        "Month",
        "Day",
        "Details",
        "Fol",
        "Amount",
    ]


def ledger_expected_text(value: Any) -> str:
    if isinstance(value, list):
        return " or ".join(str(v) for v in value if str(v).strip())
    return "" if value is None else str(value)


def build_gl_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    account_name: str,
    transaction_line: str,
    row_role: str,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = ledger_expected_text(expected)
    source_ref = ""
    for ref in ["CRJ", "CPJ", "DJ", "DAJ", "CJ", "CAJ", "GJ", "b/d", "c/d"]:
        if f"from {ref}" in transaction_line or f"{ref}," in transaction_line or f" {ref}" in transaction_line:
            source_ref = ref
            break
    role = f"This cell records the {header or 'required detail'} for the {account_name} ledger account."
    evidence = transaction_line or f"Use the posting information provided for the {account_name} account."
    rule = "General Ledger entries are posted from the source journal or General Journal to the correct side of the selected account."
    method = (
        f"Step 1: locate the relevant source line{f' from {source_ref}' if source_ref else ''}. "
        f"Step 2: decide whether {account_name} is debited or credited. "
        f"Step 3: complete the details, folio, and amount for that side. "
        f"The expected entry here is {expected_text or 'blank'}."
    )
    transfer_tip = "In similar questions, work source by source: identify the journal, find the contra account, then post to the correct side of the ledger account."

    if header_norm == "month":
        role = "This cell records the month of the ledger posting."
        method = f"Copy the month shown for this ledger entry. Here it is {expected_text or 'blank'}."
    elif header_norm == "day":
        role = "This cell records the day on which the posting is made."
        method = f"Copy the day for this posting. Here it is {expected_text or 'blank'}."
    elif header_norm == "details":
        role = "This cell names the contra account or explanation for the posting."
        rule = "In a General Ledger account, the Details column usually shows the contra account: the account on the other side of the double entry."
        method = f"Step 1: read the source line. Step 2: ask which account is opposite {account_name}. Step 3: write that contra account here. Here it is {expected_text or 'blank'}."
    elif header_norm == "fol":
        role = "This cell records the folio or journal reference for the posting."
        rule = "Use the journal abbreviation or balance reference that shows where the entry came from, for example CRJ, CPJ, DJ, DAJ, CJ, CAJ, GJ, b/d, or c/d."
        method = f"Find the source of the entry and copy its folio reference exactly. Here it is {expected_text or 'blank'}."
    elif header_norm == "amount":
        role = "This cell records the money amount posted to one side of the ledger account."
        if row_role == "opening_balance":
            rule = "Balance b/d is the opening balance brought down from the previous period."
            method = f"Use the opening balance provided for the account. Here it is {expected_text or 'blank'}."
            transfer_tip = "In similar questions, start with the opening balance before posting current-period journal totals or GJ entries."
        elif row_role == "balance_cd":
            rule = "Balance c/d is the balancing figure that makes total debits equal total credits."
            method = f"Add the two sides of the account and insert the balancing figure. Here it is {expected_text or 'blank'}."
            transfer_tip = "In similar questions, total both sides first, then place Balance c/d on the smaller side."
        elif row_role == "balance_bd":
            rule = "Balance b/d in the new month is the amount carried forward from Balance c/d."
            method = f"Carry the closing balance forward exactly. Here it is {expected_text or 'blank'}."
        elif row_role == "totals":
            rule = "Totals must agree on both sides after the balancing figure has been included."
            method = f"Add down the side and copy the total. Here it is {expected_text or 'blank'}."
        else:
            method = f"Step 1: find the matching amount in the source journal or GJ line. Step 2: confirm that it affects {account_name}. Step 3: post that amount on the correct side. Here it is {expected_text or 'blank'}."

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def build_running_ledger_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    ledger_kind: str,
    transaction_line: str,
    previous_balance: Optional[float] = None,
    debit_value: Optional[float] = None,
    credit_value: Optional[float] = None,
    balance_value: Optional[float] = None,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = ledger_expected_text(expected)
    ledger_label = "Debtors Ledger" if ledger_kind == "debtors" else "Creditors Ledger"
    role = f"This cell records the {header or 'required detail'} in the {ledger_label}."
    evidence = transaction_line or f"Use the transaction details for this {ledger_label} row."
    rule = "Subsidiary ledger accounts show the movement and running balance for one debtor or creditor."
    method = f"Use the row information provided. The expected entry is {expected_text or 'blank'}."
    transfer_tip = "In similar questions, decide whether the transaction increases or decreases the account, then update the running balance."

    if header_norm == "date":
        role = "This cell records the date of the transaction in the subsidiary ledger."
        rule = "The Date column shows when the entry took place."
        method = f"Copy the transaction day exactly. Here it is {expected_text or 'blank'}."
    elif header_norm == "details":
        role = "This cell records the document or description for the entry."
        rule = "Details identify the invoice, receipt, credit note, cheque, discount, interest, or other posting description."
        method = f"Use the wording of the transaction or source document. Here it is {expected_text or 'blank'}."
    elif header_norm == "fol":
        role = "This cell records the folio or journal reference from which the item was posted."
        rule = "Use the journal abbreviation that matches the source of the posting."
        method = f"Enter the correct folio reference. Here it is {expected_text or 'blank'}."
    elif header_norm == "debit":
        role = "This cell records the debit amount for the row."
        if ledger_kind == "debtors":
            rule = "In a debtor's account, debit entries increase what the debtor owes."
        else:
            rule = "In a creditor's account, debit entries decrease what the business owes the creditor."
        method = f"Decide whether this event belongs on the debit side, then enter the amount. Here it is {expected_text or 'blank'}."
    elif header_norm == "credit":
        role = "This cell records the credit amount for the row."
        if ledger_kind == "debtors":
            rule = "In a debtor's account, credit entries reduce what the debtor owes."
        else:
            rule = "In a creditor's account, credit entries increase what the business owes the creditor."
        method = f"Decide whether this event belongs on the credit side, then enter the amount. Here it is {expected_text or 'blank'}."
    elif header_norm == "balance":
        role = "This cell records the running balance after the transaction has been posted."
        if previous_balance is not None and balance_value is not None:
            prev_text = _fmt_money(previous_balance)
            debit_text = _fmt_money(debit_value or 0.0)
            credit_text = _fmt_money(credit_value or 0.0)
            balance_text = _fmt_money(balance_value)
            if ledger_kind == "debtors":
                rule = "Debtors Ledger balance = previous balance + debit - credit."
                method = f"Calculate the new balance: {prev_text} + {debit_text} - {credit_text} = {balance_text}."
            else:
                rule = "Creditors Ledger balance = previous balance + credit - debit."
                method = f"Calculate the new balance: {prev_text} + {credit_text} - {debit_text} = {balance_text}."
        else:
            method = f"Update the balance after this row. Here it is {expected_text or 'blank'}."

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }
