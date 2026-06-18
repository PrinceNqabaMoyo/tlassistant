from __future__ import annotations

from typing import Dict, List


def headers_to_column_help(*, journal_type: str, headers: List[str]) -> Dict[str, str]:
    jt = str(journal_type or "").strip().lower()
    h = [str(x) for x in (headers or [])]

    def _norm(x: str) -> str:
        return (
            str(x or "")
            .strip()
            .lower()
            .replace("’", "'")
            .replace(".", "")
        )

    if jt == "crj":
        out: Dict[str, str] = {}
        for hdr in h:
            n = _norm(hdr)
            if n in ("doc", "doc no"):
                out[hdr] = "The relevant source document number."
            elif n == "day":
                out[hdr] = "The specific day of the relevant month (heading May 2010)."
            elif n == "details":
                out[hdr] = "This column shows the source of the relevant receipt."
            elif n == "fol":
                out[hdr] = (
                    "For each debtor there needs to be a separate account in the Debtors’ Ledger. "
                    "A folio number will be used to indicate the account the amount will be posted to in the Debtors’ Ledger."
                )
            elif n == "analysis of receipts":
                out[hdr] = "The analysis column shows the breakdown of the individual amounts received as a separate receipt."
            elif n == "bank":
                out[hdr] = (
                    "The bank column shows the total amount received for the day and deposited into the business’s bank account. "
                    "If there is more than one receipt on the same day, record each receipt on its own line and enter the bank total only "
                    "on the bottom-most (last) line for that day."
                )
            elif n == "sales":
                out[hdr] = "This column contains the selling price of trading stock sold for cash."
            elif n == "cost of sales":
                out[hdr] = (
                    "This is a non-cash item but is included in the Cash Receipts Journal to allow for the regular updating of the trading stock account."
                )
            elif n in ("debtors control", "debtors' control"):
                out[hdr] = "Total of credit sales amounts received from debtors when they settle their accounts."
            elif n == "discount allowed":
                out[hdr] = "Discount granted to debtors when they pay/settle their accounts."
            elif n.startswith("sundry"):
                if "amount" in n:
                    out[hdr] = "(under sundry account) The amount received."
                elif "fol" in n:
                    out[hdr] = (
                        "(Under sundry account) The folio number will be used to indicate the account the amount will be posted to in the General Ledger."
                    )
                else:
                    out[hdr] = "(Under sundry account) The account in the General Ledger"
            else:
                out[hdr] = ""
        return out

    if jt == "cpj":
        out: Dict[str, str] = {}
        for hdr in h:
            n = _norm(hdr)
            if n in ("doc", "doc no"):
                out[hdr] = "Source document reference (e.g., cheque/EFT no., debit note)."
            elif n == "day":
                out[hdr] = "Day of the month the payment occurred."
            elif n in ("name of payee", "payee"):
                out[hdr] = "Who was paid (as per cheque/EFT)."
            elif n == "fol":
                out[hdr] = "Folio reference to the Creditors Ledger account (if paying a creditor)."
            elif n == "bank":
                out[hdr] = "Total amount paid out by bank."
            elif n == "trading stock":
                out[hdr] = "Cash purchases of trading stock."
            elif n == "wages":
                out[hdr] = "Payments for wages."
            elif n.startswith("debtors control"):
                out[hdr] = "Amounts posted to Debtors Control where applicable."
            elif n.startswith("creditors control"):
                out[hdr] = "Amounts posted to Creditors Control where applicable."
            elif n == "discount received":
                out[hdr] = "Discount received from creditors."
            elif n.startswith("sundry"):
                if "amount" in n:
                    out[hdr] = "Amount for other payments not in standard columns."
                elif "fol" in n:
                    out[hdr] = "Folio reference to the General Ledger account."
                else:
                    out[hdr] = "Name of the General Ledger account."
            else:
                out[hdr] = ""
        return out

    if jt in ("dj", "daj"):
        base: Dict[str, str] = {
            "Doc": "Invoice / credit note number.",
            "Day": "Day of the month.",
            "Debtor": "Name of the debtor.",
            "Debtors": "Name of the debtor.",
            "Fol": "Folio reference to the debtor's account in the Debtors Ledger.",
            "Fol.": "Folio reference to the debtor's account in the Debtors Ledger.",
        }
        for hdr in h:
            n = _norm(hdr)
            if n.startswith("sales"):
                base[hdr] = "Selling price (credit sales) posted to Sales / Debtors Control."
            if n.startswith("debtors allowances"):
                base[hdr] = "Returns/allowances granted to debtors (reduces Debtors Control)."
            if n.startswith("cost of sales"):
                base[hdr] = "Cost price (perpetual system)."
        return base

    if jt == "gj":
        base: Dict[str, str] = {
            "Day": "Day of the month.",
            "Details": "Account name / description used in the general journal.",
            "Fol": "Folio reference to the General Ledger account.",
            "Debit": "Amount to be debited to the account in Details (if applicable).",
            "Credit": "Amount to be credited to the account in Details (if applicable).",
            "Debtors’ control debit": "Amount to be debited to Debtors’ control (if applicable).",
            "Debtors’ control credit": "Amount to be credited to Debtors’ control (if applicable).",
            "Creditors’ control debit": "Amount to be debited to Creditors’ control (if applicable).",
            "Creditors’ control credit": "Amount to be credited to Creditors’ control (if applicable).",
        }
        for hdr in h:
            if hdr not in base:
                base[hdr] = ""
        return base

    if jt == "pcj":
        base: Dict[str, str] = {
            "Doc": "Petty cash voucher / source document number.",
            "Day": "Day of the month.",
            "Details": "What the payment was for (e.g. postage).",
            "Fol": "Folio reference (ledger / petty cash analysis reference).",
            "Petty cash": "Total petty cash payment (amount paid out of the petty cash float).",
            "Postage": "Postage expense paid from petty cash.",
            "Stationery": "Stationery expense paid from petty cash.",
            "Sundry amount": "Amount for other petty cash payments not in standard columns.",
            "Sundry fol": "Folio reference to the General Ledger account.",
            "Sundry details": "Name of the General Ledger account.",
        }
        for hdr in h:
            if hdr not in base:
                base[hdr] = ""
        return base

    if jt in ("cj", "caj"):
        base: Dict[str, str] = {
            "Doc": "Invoice / debit note number.",
            "Day": "Day of the month.",
            "Creditor": "Name of the creditor.",
            "Creditors": "Name of the creditor.",
            "Fol": "Folio reference to the creditor's account in the Creditors Ledger.",
        }
        for hdr in h:
            n = _norm(hdr)
            if n.startswith("creditors control"):
                base[hdr] = "Total posted to Creditors Control (summary account in General Ledger)."
            if n.startswith("trading stock"):
                base[hdr] = "Purchases/returns of trading stock (perpetual system)."
            if n.startswith("stationery"):
                base[hdr] = "Purchases/returns of stationery."
            if n.startswith("equipment"):
                base[hdr] = "Purchases/returns of equipment."
            if n.startswith("sundry"):
                base[hdr] = "Other items not covered by standard columns."
        return base

    if jt == "trial_balance":
        return {
            "Account": "Account name.",
            "Fol.": "Folio reference to the ledger account. Balance Sheet accounts usually use B folios and Nominal accounts usually use N folios.",
            "Fol": "Folio reference to the ledger account. Balance Sheet accounts usually use B folios and Nominal accounts usually use N folios.",
            "Debit": "Debit balance (if applicable).",
            "Credit": "Credit balance (if applicable).",
        }

    return {hdr: "" for hdr in h}
