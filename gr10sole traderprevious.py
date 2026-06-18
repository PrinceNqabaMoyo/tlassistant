from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional, Tuple

from .sole_trader.journals.crj import make_crj_single_row_question as _st_make_crj_single_row_question
from .sole_trader.journals.cpj import make_cpj_single_row_question as _st_make_cpj_single_row_question
from .sole_trader.journals.dj import make_dj_single_row_question as _st_make_dj_single_row_question
from .sole_trader.journals.daj import make_daj_single_row_question as _st_make_daj_single_row_question
from .sole_trader.journals.cj import make_cj_single_row_question as _st_make_cj_single_row_question
from .sole_trader.journals.caj import make_caj_single_row_question as _st_make_caj_single_row_question
from .sole_trader.journals.pcj import make_pcj_single_row_question as _st_make_pcj_single_row_question
from .sole_trader.journals.gj import make_gj_single_row_question as _st_make_gj_single_row_question


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_st_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
    }


def _make_typed(*, prompt: str, sample_answer: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_st_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
    }


def _make_calc(*, prompt: str, correct_value: float, unit: str = "") -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_st_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(correct_value),
        "unit": unit,
        "expected_answer_type": "number",
    }


def _make_accounting_cycle_question(*, r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Put these steps of the accounting cycle in the correct order (write them as a list):\n\n"
        "- Post to the ledger\n"
        "- Prepare a trial balance\n"
        "- Record transactions in journals\n"
    )

    sample_answer = (
        "1) Record transactions in journals\n"
        "2) Post to the ledger\n"
        "3) Prepare a trial balance"
    )

    return _make_typed(
        prompt=prompt,
        sample_answer=sample_answer,
    )


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _build_journal_row(*, row_index: int, values: List[Optional[str]], editable_cols: List[int]) -> List[Dict[str, Any]]:
    cells: List[Dict[str, Any]] = []
    for c, v in enumerate(values):
        cell_id = f"r{row_index}_c{c}"
        cells.append({
            "cell_id": cell_id,
            "value": "" if v is None else str(v),
            "editable": c in set(editable_cols),
        })
    return cells


def _journal_editable_cols_by_difficulty(*, difficulty: str, base_editable_cols: List[int], total_cols: int) -> List[int]:
    """On medium/hard, let learners decide which columns to use by making most cells editable."""
    diff = str(difficulty or "easy").strip().lower()
    if diff in ("medium", "hard"):
        # Keep the prefilled transaction identity columns locked (Doc, Day, Details).
        return list(range(3, int(total_cols)))
    return base_editable_cols


def _make_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, Any],
    guidelines: Optional[List[str]] = None,
    table_variant: str = "studio",
    column_help: Optional[Dict[str, str]] = None,
    header_rows: Optional[List[List[Dict[str, Any]]]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    journal: Dict[str, Any] = {
        "journal_type": journal_type,
        "table_variant": table_variant,
        "headers": headers,
        "rows": rows,
        "column_help": column_help or {},
    }
    if header_rows:
        journal["header_rows"] = header_rows
    if title_fields:
        journal["title_fields"] = title_fields

    return {
        "id": _make_id("acct10_st_journal"),
        "question_type": "journal",
        "prompt": prompt,
        "journal": journal,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "journal",
    }


def _headers_to_column_help(*, journal_type: str, headers: List[str]) -> Dict[str, str]:
    """Lightweight per-column guidance for scaffold mode. Keys match header strings."""
    jt = str(journal_type or "").strip().lower()
    h = [str(x) for x in (headers or [])]

    if jt == "crj":
        return {
            "Doc": "Source document reference (e.g., receipt no., bank statement).",
            "Day": "Day of the month the transaction occurred.",
            "Details": "Who/what the receipt is from (e.g., debtor name, cash sales).",
            "Fol": "Folio reference to the Debtors Ledger account for that debtor.",
            "Analysis of receipts": "Breakdown amount for the transaction before posting to analysis columns.",
            "Bank": "Total amount received/deposited into bank.",
            "Sales": "Selling price of cash sales.",
            "Cost of Sales": "Cost price of goods sold (perpetual system).",
            "Debtors' Control": "Total credited to Debtors Control (amount due) when a debtor settles.",
            "Discount allowed": "Discount granted to debtors (reduces Debtors Control).",
            "Sundry amount": "Amount for other receipts not in standard columns.",
            "Sundry fol": "Folio reference to the General Ledger account.",
            "Sundry details": "Name of the General Ledger account.",
        }

    if jt == "cpj":
        return {
            "Doc": "Source document reference (e.g., cheque/EFT no., debit note).",
            "Day": "Day of the month the payment occurred.",
            "Name of payee": "Who was paid (as per cheque/EFT).",
            "Fol": "Folio reference to the Creditors Ledger account (if paying a creditor).",
            "Bank": "Total amount paid out by bank.",
            "Trading stock": "Cash purchases of trading stock.",
            "Creditors control": "Total debited to Creditors Control when paying creditors.",
            "Discount received": "Discount received from creditors.",
            "Debtors control (R/D)": "Dishonoured cheque / returned debit orders affecting debtors.",
            "Wages": "Payments for wages.",
            "Sundry amount": "Amount for other payments not in standard columns.",
            "Sundry fol": "Folio reference to the General Ledger account.",
            "Sundry details": "Name of the General Ledger account.",
        }

    if jt in ("dj", "daj"):
        base = {
            "Doc": "Invoice / credit note number.",
            "Day": "Day of the month.",
            "Debtor": "Name of the debtor.",
            "Fol": "Folio reference to the debtor's account in the Debtors Ledger.",
        }
        for hdr in h:
            if hdr.lower().startswith("sales"):
                base[hdr] = "Selling price (credit sales) posted to Sales / Debtors Control."
            if hdr.lower().startswith("debtors allowances"):
                base[hdr] = "Returns/allowances granted to debtors (reduces Debtors Control)."
            if hdr.lower().startswith("cost of sales"):
                base[hdr] = "Cost price (perpetual system)."
        return base

    if jt in ("cj", "caj"):
        base = {
            "Doc": "Invoice / debit note number.",
            "Day": "Day of the month.",
            "Creditor": "Name of the creditor.",
            "Fol": "Folio reference to the creditor's account in the Creditors Ledger.",
        }
        for hdr in h:
            if hdr.lower().startswith("creditors control"):
                base[hdr] = "Total posted to Creditors Control (summary account in General Ledger)."
            if hdr.lower().startswith("trading stock"):
                base[hdr] = "Purchases/returns of trading stock (perpetual system)."
            if hdr.lower().startswith("stationery"):
                base[hdr] = "Purchases/returns of stationery."
            if hdr.lower().startswith("equipment"):
                base[hdr] = "Purchases/returns of equipment."
            if hdr.lower().startswith("sundry"):
                base[hdr] = "Other items not covered by standard columns."
        return base

    if jt in ("general_ledger", "debtors_ledger", "creditors_ledger", "ledger"):
        # Generic T-account help; specific ledger formats will extend this later.
        return {
            "Date": "Transaction date.",
            "Details": "Counter account / explanation.",
            "Fol": "Folio reference to the journal or ledger account.",
            "Amount": "Amount posted.",
        }

    if jt == "trial_balance":
        return {
            "Account": "Account name.",
            "Debit": "Debit balance (if applicable).",
            "Credit": "Credit balance (if applicable).",
        }

    return {hdr: "" for hdr in h}


def _crj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Details",
        "Fol",
        "Analysis of receipts",
        "Bank",
        "Sales",
        "Cost of Sales",
        "Debtors' Control",
        "Discount allowed",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


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


def _dj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Debtor",
        "Fol",
        "Sales",
        "Cost of sales",
    ]


def _daj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Debtor",
        "Fol",
        "Debtors allowances",
        "Cost of sales",
    ]


def _cj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Creditor",
        "Fol",
        "Creditors control",
        "Trading stock",
        "Stationery",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def _caj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Creditor",
        "Fol",
        "Creditors control",
        "Trading stock",
        "Stationery",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def _ledger_headers() -> List[str]:
    return [
        "Account",
        "Debit (Dr)",
        "Credit (Cr)",
    ]


def _t_account_ledger_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Amount",
        "Date",
        "Details",
        "Fol",
        "Amount",
    ]


def _trial_balance_headers() -> List[str]:
    return [
        "Account",
        "Debit",
        "Credit",
    ]


def _round_percent(x: float) -> float:
    return round(float(x) + 1e-9, 4)


def _calc_cost_price_from_selling_price_and_margin(*, sp: float, profit_margin_pct: float) -> float:
    return _round_money(sp / (1.0 + (profit_margin_pct / 100.0)))


def _calc_selling_price_from_cost_price_and_margin(*, cp: float, profit_margin_pct: float) -> float:
    return _round_money(cp * (1.0 + (profit_margin_pct / 100.0)))


def _fmt_money(x: Optional[float]) -> str:
    if x is None:
        return ""
    return f"{_round_money(x):.2f}"


def _make_ledger_posting_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    day = int(r.choice([2, 5, 10, 14, 18, 22, 26, 29]))

    amount = float(r.choice([450, 800, 1200, 1800, 2400, 3600, 5200]))
    kind = r.choice(["cash_sales", "pay_wages"])

    if kind == "cash_sales":
        prompt_tx = f"{day} {month}: Cash sales, R{amount:.2f}."
        debit_account = "Bank"
        credit_account = "Sales"
        debit_amount = amount
        credit_amount = amount
    else:
        prompt_tx = f"{day} {month}: Paid wages by cheque, R{amount:.2f}."
        debit_account = "Wages"
        credit_account = "Bank"
        debit_amount = amount
        credit_amount = amount

    headers = _ledger_headers()
    values0: List[Optional[str]] = [debit_account, "", ""]
    values1: List[Optional[str]] = [credit_account, "", ""]

    diff = str(difficulty or "easy").strip().lower()
    if diff in ("medium", "hard"):
        editable_cols = [0, 1, 2]
    else:
        editable_cols = [1, 2]

    row0 = _build_journal_row(row_index=0, values=values0, editable_cols=editable_cols)
    row1 = _build_journal_row(row_index=1, values=values1, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}

    # Always mark amounts. Only mark account names on medium/hard.
    if diff in ("medium", "hard"):
        correct_map["r0_c0"] = debit_account
        correct_map["r1_c0"] = credit_account

    correct_map["r0_c1"] = _fmt_money(debit_amount)
    correct_map["r0_c2"] = ""
    correct_map["r1_c1"] = ""
    correct_map["r1_c2"] = _fmt_money(credit_amount)

    prompt = (
        f"{business}\n"
        f"Ledger posting for {month}\n\n"
        "Context:\n"
        f"- {prompt_tx}\n\n"
        "Required:\n"
        "Post the transaction to the ledger by completing the Debit/Credit columns.\n"
        "(Only one side should have an amount for each account.)"
    )

    return _make_journal(
        prompt=prompt,
        journal_type="general_ledger",
        headers=headers,
        rows=[row0, row1],
        correct_map=correct_map,
        guidelines=[
            "Debit the account that receives value; credit the account that gives value.",
            "For cash sales: Dr Bank, Cr Sales.",
            "For wages paid: Dr Wages, Cr Bank.",
        ],
    )


def _make_debtors_ledger_posting_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    day = int(r.choice([3, 5, 8, 12, 17, 22, 28]))

    debtor = r.choice(["J. Abrahams", "M. Nelson", "N. Rossouw", "B. Maseko"])
    fol = str(r.choice(["D1", "D2", "D3", "D4"]))

    kind = r.choice(["credit_sale", "settlement_discount"])
    amount = float(r.choice([480, 1200, 1500, 1800, 2400, 3600, 4800]))

    headers = _t_account_ledger_headers()
    diff = str(difficulty or "easy").strip().lower()

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    if kind == "credit_sale":
        invoice_no = str(r.choice(["51", "52", "53", "54", "55"]))
        prompt_tx = f"{day} {month}: Sold goods on credit to {debtor}, invoice {invoice_no}, R{amount:.2f}."

        values = [str(day), "Sales", "DJ", "", "", "", "", ""]
        editable_cols = [3] if diff == "easy" else [0, 1, 2, 3, 4, 5, 6, 7]
        row = _build_journal_row(row_index=0, values=values, editable_cols=editable_cols)
        rows.append(row)

        if diff in ("medium", "hard"):
            correct_map["r0_c0"] = str(day)
            correct_map["r0_c1"] = "Sales"
            correct_map["r0_c2"] = "DJ"
        correct_map["r0_c3"] = _fmt_money(amount)
        correct_map["r0_c4"] = ""
        correct_map["r0_c5"] = ""
        correct_map["r0_c6"] = ""
        correct_map["r0_c7"] = ""
    else:
        receipt_no = str(r.choice(["142", "143", "144", "145", "146"]))
        discount = float(r.choice([0, 20, 50, 80, 100, 120]))
        if discount >= amount:
            discount = 0.0
        bank = _round_money(amount - discount)
        prompt_tx = (
            f"{day} {month}: Received from {debtor} in settlement of account R{amount:.2f}. "
            f"Discount allowed R{discount:.2f}. Receipt {receipt_no}."
        )

        values0 = ["", "", "", "", str(day), "Bank", "CRJ", ""]
        values1 = ["", "", "", "", str(day), "Discount allowed", "CRJ", ""]

        editable_cols = [7] if diff == "easy" else [0, 1, 2, 3, 4, 5, 6, 7]
        row0 = _build_journal_row(row_index=0, values=values0, editable_cols=editable_cols)
        row1 = _build_journal_row(row_index=1, values=values1, editable_cols=editable_cols)
        rows.extend([row0, row1])

        if diff in ("medium", "hard"):
            correct_map["r0_c4"] = str(day)
            correct_map["r0_c5"] = "Bank"
            correct_map["r0_c6"] = "CRJ"
            correct_map["r1_c4"] = str(day)
            correct_map["r1_c5"] = "Discount allowed"
            correct_map["r1_c6"] = "CRJ"

        correct_map["r0_c0"] = ""
        correct_map["r0_c1"] = ""
        correct_map["r0_c2"] = ""
        correct_map["r0_c3"] = ""
        correct_map["r0_c7"] = _fmt_money(bank)

        correct_map["r1_c0"] = ""
        correct_map["r1_c1"] = ""
        correct_map["r1_c2"] = ""
        correct_map["r1_c3"] = ""
        correct_map["r1_c7"] = _fmt_money(discount)

    prompt = (
        f"{business}\n"
        f"Debtors Ledger ({debtor}) for {month}\n\n"
        "Context:\n"
        f"- Debtor folio: {fol}\n"
        f"- {prompt_tx}\n\n"
        "Required:\n"
        "Post the transaction to the Debtors Ledger account."
    )

    return _make_journal(
        prompt=prompt,
        journal_type="debtors_ledger",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Credit sales increase the amount owed by the debtor (Debit the debtor account).",
            "Payments/settlements decrease the amount owed (Credit the debtor account).",
            "Discount allowed is posted on the credit side of the debtor account (it reduces the amount owed).",
        ],
    )


def _make_creditors_ledger_posting_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    day = int(r.choice([1, 4, 9, 12, 18, 24, 28]))

    creditor = r.choice(["RN Wholesalers", "Sam Distributors", "SA Traders", "MZ Suppliers"])
    fol = str(r.choice(["C1", "C2", "C3", "C4"]))
    amount = float(r.choice([950, 1400, 1800, 2400, 3200, 4800, 6500]))
    invoice_no = str(r.choice(["201", "202", "203", "204", "205"]))

    diff = str(difficulty or "easy").strip().lower()
    headers = _t_account_ledger_headers()

    prompt_tx = f"{day} {month}: Bought trading stock on credit from {creditor}, invoice {invoice_no}, R{amount:.2f}."

    values = ["", "", "", "", str(day), "Trading stock", "CJ", ""]
    editable_cols = [7] if diff == "easy" else [0, 1, 2, 3, 4, 5, 6, 7]
    row = _build_journal_row(row_index=0, values=values, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}
    if diff in ("medium", "hard"):
        correct_map["r0_c4"] = str(day)
        correct_map["r0_c5"] = "Trading stock"
        correct_map["r0_c6"] = "CJ"
    correct_map["r0_c0"] = ""
    correct_map["r0_c1"] = ""
    correct_map["r0_c2"] = ""
    correct_map["r0_c3"] = ""
    correct_map["r0_c7"] = _fmt_money(amount)

    prompt = (
        f"{business}\n"
        f"Creditors Ledger ({creditor}) for {month}\n\n"
        "Context:\n"
        f"- Creditor folio: {fol}\n"
        f"- {prompt_tx}\n\n"
        "Required:\n"
        "Post the transaction to the Creditors Ledger account."
    )

    return _make_journal(
        prompt=prompt,
        journal_type="creditors_ledger",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        guidelines=[
            "Credit purchases increase the amount owed to the creditor (Credit the creditor account).",
            "Payments reduce the amount owed (Debit the creditor account).",
        ],
    )


def _make_trial_balance_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    bank = float(r.choice([1200, 2400, 3600, 4800, 6000, 7200]))
    trading_stock = float(r.choice([1800, 3600, 5400, 7200, 9000, 10800]))
    sales = float(r.choice([3600, 7200, 10800, 14400, 18000, 21600]))
    capital = _round_money(bank + trading_stock + sales)

    headers = _trial_balance_headers()

    rows_def: List[Tuple[str, str, str]] = [
        ("Bank", _fmt_money(bank), ""),
        ("Trading stock", _fmt_money(trading_stock), ""),
        ("Sales", "", _fmt_money(sales)),
        ("Capital", "", _fmt_money(capital)),
    ]

    diff = str(difficulty or "easy").strip().lower()
    if diff in ("medium", "hard"):
        editable_cols = [0, 1, 2]
    else:
        editable_cols = [1, 2]

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for i, (acct, dr, cr) in enumerate(rows_def):
        values: List[Optional[str]] = [acct, "", ""]
        rows.append(_build_journal_row(row_index=i, values=values, editable_cols=editable_cols))
        if diff in ("medium", "hard"):
            correct_map[f"r{i}_c0"] = acct
        correct_map[f"r{i}_c1"] = dr
        correct_map[f"r{i}_c2"] = cr

    prompt = (
        f"{business}\n"
        f"Trial Balance for {month}\n\n"
        "Context:\n"
        "Use the balances below to prepare a Trial Balance:\n"
        f"- Bank balance: R{bank:.2f} (Debit)\n"
        f"- Trading stock: R{trading_stock:.2f} (Debit)\n"
        f"- Sales: R{sales:.2f} (Credit)\n"
        "- Capital: (balancing figure)\n\n"
        "Required:\n"
        "Complete the Trial Balance table."
    )

    return _make_journal(
        prompt=prompt,
        journal_type="trial_balance",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Debits must equal credits in a trial balance.",
            "Asset accounts usually have debit balances; income accounts usually have credit balances.",
        ],
    )


def _make_crj_cash_sales_cost_of_sales_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    day = int(r.choice([1, 3, 6, 10, 14, 18, 22, 26, 30]))
    amount = float(r.randrange(2000, 25000 + 1, 100))

    # Continuous inventory (Grade 10): include cost of sales for cash sales.
    # Mark-up 66 2/3% on cost => cost = 60% of selling price.
    cost = _round_money(amount * 0.6)

    headers = _crj_headers()

    values: List[Optional[str]] = [
        "CRR",
        str(day),
        "Sales",
        "",  # Fol
        "",  # Analysis of receipts
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=[4, 5, 6, 7, 8, 9, 10, 11, 12],
        total_cols=len(values),
    )
    row = _build_journal_row(row_index=0, values=values, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}

    def _set(col: int, expected: Any) -> None:
        correct_map[f"r0_c{col}"] = expected

    _set(3, "")
    _set(4, "")
    _set(5, f"{amount:.2f}")
    _set(6, f"{amount:.2f}")
    _set(7, f"{cost:.2f}")
    _set(8, "")
    _set(9, "")
    _set(10, "")
    _set(11, "")
    _set(12, "")

    prompt = (
        f"{business}\n"
        f"Cash Receipts Journal (CRJ) for {month}\n\n"
        "Context:\n"
        f"- {day} {month}: Cash sales R{amount:.2f}. (Mark-up 66⅔% on cost; continuous inventory.)\n\n"
        "Required:\n"
        "Enter the transaction in the CRJ. Complete only the missing cells."
    )

    return _make_journal(
        prompt=prompt,
        journal_type="crj",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        guidelines=[
            "For cash sales: Bank = Sales (selling price).",
            "Continuous inventory: record Cost of Sales for sales.",
            "Mark-up 66⅔% on cost means: Cost = Selling price × 0.6.",
        ],
    )


def _make_crj_cost_of_sales_calc_question(*, r: random.Random) -> Dict[str, Any]:
    sp = float(r.randrange(1000, 30000 + 1, 100))
    cost = _round_money(sp * 0.6)

    prompt = (
        "Continuous inventory system (Grade 10):\n"
        "A trader sells goods for cash. The mark-up is 66⅔% on cost.\n\n"
        f"Selling price (cash sales) = R{sp:.2f}.\n\n"
        "Required:\n"
        "Calculate the cost of sales."
    )

    return _make_calc(
        prompt=prompt,
        correct_value=cost,
        unit="R",
    )


def _make_crj_debtor_discount_calc_question(*, r: random.Random) -> Dict[str, Any]:
    amount_due = float(r.randrange(1000, 8000 + 1, 100))
    discount_pct = float(r.choice([5, 10]))
    discount_allowed = _round_money(amount_due * (discount_pct / 100.0))
    bank = _round_money(amount_due - discount_allowed)

    prompt = (
        "Discount allowed to debtors:\n"
        f"A debtor owes R{amount_due:.2f} and is allowed a {discount_pct:g}% discount for settling.\n\n"
        "Required:\n"
        "Calculate the amount received in the bank."
    )

    return _make_calc(
        prompt=prompt,
        correct_value=bank,
        unit="R",
    )


def _make_crj_single_row_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    receipt_no = str(r.choice([142, 143, 144, 145, 146, 210]))
    day = int(r.choice([1, 4, 12, 15, 23, 27, 30]))

    debtors = r.sample([
        "A. Khumalo",
        "B. Maseko",
        "C. Naidoo",
        "D. Botha",
        "E. Nkosi",
        "F. Pillay",
    ], k=3)

    kind = r.choice(["cash_sales", "other_receipt", "debtor_settlement"])
    headers = _crj_headers()

    if kind == "cash_sales":
        amount = float(r.choice([5600, 12000, 15400, 17000, 32500]))
        details = "Cash sales"
        transaction_line = f"{day} {month}: Cash sales, receipt no. {receipt_no}, amount R{amount:.2f}."

        bank = amount
        sales = amount
        debtors_control = None
        discount_allowed = None
        sundry_amount = None
        sundry_details = ""
    elif kind == "other_receipt":
        amount = float(r.choice([800, 1200, 1500, 2400, 3200, 5000]))
        receipt_type = r.choice(["Rent received", "Commission received", "Interest on fixed deposit"])
        details = receipt_type
        transaction_line = f"{day} {month}: Received {receipt_type.lower()}, receipt no. {receipt_no}, amount R{amount:.2f}."

        bank = amount
        sales = None
        debtors_control = None
        discount_allowed = None
        sundry_amount = amount
        sundry_details = receipt_type
    else:
        debtor = r.choice(debtors)
        amount_due = float(r.choice([1200, 1850, 2400, 3600, 5400, 7800]))
        discount = float(r.choice([0, 50, 80, 100, 150, 200]))
        if discount >= amount_due:
            discount = 0.0
        amount_received = _round_money(amount_due - discount)
        details = debtor
        transaction_line = (
            f"{day} {month}: Received from debtor {debtor} in settlement of account R{amount_due:.2f}. "
            f"Discount allowed R{discount:.2f}. Receipt no. {receipt_no}."
        )

        bank = amount_received
        debtors_control = amount_due
        discount_allowed = discount
        sales = None
        sundry_amount = None
        sundry_details = ""

    values: List[Optional[str]] = [
        receipt_no,
        str(day),
        details,
        "",  # Fol (fixed)
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

    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=[4, 5, 6, 7, 8, 9, 10, 11, 12],
        total_cols=len(values),
    )
    row = _build_journal_row(row_index=0, values=values, editable_cols=editable_cols)

    correct_map: Dict[str, Any] = {}

    def _set(col: int, expected: Any):
        correct_map[f"r0_c{col}"] = expected

    _set(3, "")
    _set(4, "")
    _set(5, f"{bank:.2f}" if bank is not None else "")
    _set(6, f"{sales:.2f}" if sales is not None else "")
    _set(7, "")
    _set(8, f"{debtors_control:.2f}" if debtors_control is not None else "")
    _set(9, f"{discount_allowed:.2f}" if discount_allowed is not None else "")
    _set(10, f"{sundry_amount:.2f}" if sundry_amount is not None else "")
    _set(11, "")
    _set(12, sundry_details)

    prompt = (
        f"{business}\n"
        f"Cash Receipts Journal (CRJ) for {month}\n\n"
        "Context:\n"
        f"- Debtors: {', '.join(debtors)}\n"
        f"- Transaction: {transaction_line}\n\n"
        "Required:\n"
        "Post the transaction to the CRJ entry below. Complete only the missing cells."
    )

    return _make_journal(
        prompt=prompt,
        journal_type="crj",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        guidelines=[
            "For a debtor settlement: Debtors control = amount due; Bank = amount received; Discount allowed = discount.",
            "For cash sales: enter the amount in Bank and Sales.",
            "For other receipts (e.g., rent/commission): enter Bank, then use Sundry amount + Sundry details.",
        ],
    )


def _make_crj_activity5_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business_names = [
        "Lonely Traders",
        "Ubuntu Traders",
        "Mzanzi Mart",
        "Cape Corner Stores",
        "Gauteng Grocers",
        "Durban Deals",
        "Soweto Spares",
        "Pretoria Provisions",
        "Jozi Junction",
        "Karoo Kiosk",
        "Vaal Vendors",
        "Limpopo Lifestyle Traders",
        "Mpumalanga Market",
        "Free State Foods",
        "Eastern Cape Emporium",
        "Northern Cape Necessities",
        "West Coast Wholesalers",
        "Garden Route Goods",
        "Highveld Hardware",
        "Sunrise Superstore",
    ]

    business = r.choice(business_names)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013, 2014]))

    # Continuous inventory (Grade 10): include cost of sales for cash sales.
    # Mark-up 66 2/3% on cost => cost = 60% of selling price.
    markup_pct = 66.6667
    cost_factor = 0.6

    debtors = ["J. Abrahams", "N. Rossouw", "M. Nelson", "T. Dlamini", "S. Pillay", "L. Mokoena"]
    used_debtors = r.sample(debtors, k=3)
    debtor_balances: Dict[str, float] = {d: float(r.randrange(1500, 6500 + 1, 100)) for d in used_debtors}

    receipt_start = int(r.choice([140, 141, 142, 143, 144, 145]))
    receipt_nos = [str(receipt_start + i) for i in range(6)]
    days = sorted(r.sample([1, 2, 4, 5, 10, 12, 14, 15, 18, 22, 23, 26, 27, 29, 30], k=6))

    discount_pct = float(r.choice([5, 10]))
    debtor_for_settlement = r.choice(list(debtor_balances.keys()))
    amount_due = debtor_balances[debtor_for_settlement]
    discount_allowed = _round_money(amount_due * (discount_pct / 100.0))
    amount_received = _round_money(amount_due - discount_allowed)

    cash_sales_1 = float(r.randrange(1000, 20000 + 1, 10))
    cash_sales_2 = float(r.randrange(1000, 20000 + 1, 10))
    rent_received = float(r.randrange(1000, 15000 + 1, 100))
    capital_contribution = float(r.randrange(5000, 40000 + 1, 100))
    bank_interest = float(r.randrange(50, 500 + 1, 10))

    tx_rows: List[Dict[str, Any]] = []
    tx_rows.append({
        "doc": receipt_nos[0],
        "day": str(days[0]),
        "details": "Capital",
        "bank": capital_contribution,
        "sales": None,
        "cost_of_sales": None,
        "debtors_control": None,
        "discount_allowed": None,
        "sundry_amount": capital_contribution,
        "sundry_details": "Capital",
    })
    tx_rows.append({
        "doc": receipt_nos[1],
        "day": str(days[1]),
        "details": "Rent income",
        "bank": rent_received,
        "sales": None,
        "cost_of_sales": None,
        "debtors_control": None,
        "discount_allowed": None,
        "sundry_amount": rent_received,
        "sundry_details": "Rent income",
    })
    tx_rows.append({
        "doc": "CRR",
        "day": str(days[2]),
        "details": "Sales",
        "bank": cash_sales_1,
        "sales": cash_sales_1,
        "cost_of_sales": _round_money(cash_sales_1 * cost_factor),
        "debtors_control": None,
        "discount_allowed": None,
        "sundry_amount": None,
        "sundry_details": "",
    })
    tx_rows.append({
        "doc": receipt_nos[3],
        "day": str(days[3]),
        "details": debtor_for_settlement,
        "bank": amount_received,
        "sales": None,
        "cost_of_sales": None,
        "debtors_control": amount_due,
        "discount_allowed": discount_allowed,
        "sundry_amount": None,
        "sundry_details": "",
    })
    tx_rows.append({
        "doc": "CRR",
        "day": str(days[4]),
        "details": "Sales",
        "bank": cash_sales_2,
        "sales": cash_sales_2,
        "cost_of_sales": _round_money(cash_sales_2 * cost_factor),
        "debtors_control": None,
        "discount_allowed": None,
        "sundry_amount": None,
        "sundry_details": "",
    })
    tx_rows.append({
        "doc": "B/S",
        "day": str(days[5]),
        "details": "Bank interest",
        "bank": bank_interest,
        "sales": None,
        "cost_of_sales": None,
        "debtors_control": None,
        "discount_allowed": None,
        "sundry_amount": bank_interest,
        "sundry_details": "Interest on current account",
    })

    mode_norm = str(mode or "").strip().lower()
    expected_rows = tx_rows
    if mode_norm == "scaffold":
        body = tx_rows
    else:
        # Practice starts with 6 blank rows; learner fills the journal from the transaction list.
        body = [{
            "doc": "",
            "day": "",
            "details": "",
            "bank": None,
            "sales": None,
            "cost_of_sales": None,
            "debtors_control": None,
            "discount_allowed": None,
            "sundry_amount": None,
            "sundry_details": "",
        } for _ in range(6)]

    headers = _crj_headers()
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

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
            # Scaffold: can show the transaction identity, but still requires the learner to fill in the journal amounts.
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
            editable_cols = _journal_editable_cols_by_difficulty(
                difficulty=difficulty,
                base_editable_cols=[4, 5, 6, 7, 8, 9, 10, 11, 12],
                total_cols=len(values),
            )
        else:
            # Practice: nothing prefilled, including Doc/Day/Details.
            values = ["" for _ in range(13)]
            editable_cols = list(range(13))

        rows.append(_build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        bank = float(expected_tx["bank"]) if expected_tx.get("bank") is not None else None
        sales = float(expected_tx["sales"]) if expected_tx.get("sales") is not None else None
        cos = float(expected_tx["cost_of_sales"]) if expected_tx.get("cost_of_sales") is not None else None
        debtors = float(expected_tx["debtors_control"]) if expected_tx.get("debtors_control") is not None else None
        disc = float(expected_tx["discount_allowed"]) if expected_tx.get("discount_allowed") is not None else None
        sundry = float(expected_tx["sundry_amount"]) if expected_tx.get("sundry_amount") is not None else None

        _set(i, 0, expected_tx.get("doc", ""))
        _set(i, 1, expected_tx.get("day", ""))
        _set(i, 2, expected_tx.get("details", ""))

        _set(i, 3, "")
        _set(i, 4, "")
        _set(i, 5, _fmt(bank))
        _set(i, 6, _fmt(sales))
        _set(i, 7, _fmt(cos))
        _set(i, 8, _fmt(debtors))
        _set(i, 9, _fmt(disc))
        _set(i, 10, _fmt(sundry))
        _set(i, 11, "")
        _set(i, 12, expected_tx.get("sundry_details", ""))

        bank_total += bank or 0.0
        sales_total += sales or 0.0
        cos_total += cos or 0.0
        debtors_total += debtors or 0.0
        discount_total += disc or 0.0
        sundry_total += sundry or 0.0

    totals_index = len(body)
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
    totals_editable = _journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=[5, 6, 7, 8, 9, 10],
        total_cols=len(totals_values),
    )
    rows.append(_build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable))

    _set(totals_index, 5, f"{_round_money(bank_total):.2f}")
    _set(totals_index, 6, f"{_round_money(sales_total):.2f}")
    _set(totals_index, 7, f"{_round_money(cos_total):.2f}")
    _set(totals_index, 8, f"{_round_money(debtors_total):.2f}")
    _set(totals_index, 9, f"{_round_money(discount_total):.2f}")
    _set(totals_index, 10, f"{_round_money(sundry_total):.2f}")

    debtors_list_lines = "\n".join([f"- {d}: R{debtor_balances[d]:.2f}" for d in debtor_balances])
    transactions_lines = "\n".join([
        f"{tx['day']} {month}: {tx['doc']} {tx['details']}" for tx in tx_rows
    ])

    prompt = (
        f"{business}\n"
        f"Cash Receipts Journal (CRJ) for {month} {year}\n\n"
        f"Note: The business uses a mark-up of {markup_pct:g}% on cost price.\n\n"
        "Debtors’ list:\n"
        f"{debtors_list_lines}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        "Complete the CRJ below."
    )

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Continuous inventory: Cost of sales is recorded for sales transactions.",
            "Mark-up of 66⅔% on cost means: Cost = Selling price × 0.6.",
            "For a debtor settlement with discount: Debtors’ control = amount due; Bank = amount received; Discount allowed = difference.",
            "Totals row: add down each money column and enter the totals.",
        ]

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
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"

    return _make_journal(
        prompt=prompt,
        journal_type="crj",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        guidelines=guidelines,
    )


def generate_questions(
    *,
    mode: Optional[str] = None,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    def _maybe_filter(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if qtype_norm in ("", "mixed"):
            return items
        return [q for q in items if q.get("question_type") == qtype_norm] or items

    concepts_pool: List[Dict[str, Any]] = []
    accounting_cycle_pool: List[Dict[str, Any]] = []
    equation_pool: List[Dict[str, Any]] = []
    crj_pool: List[Dict[str, Any]] = []
    cpj_pool: List[Dict[str, Any]] = []
    dj_pool: List[Dict[str, Any]] = []
    daj_pool: List[Dict[str, Any]] = []
    cj_pool: List[Dict[str, Any]] = []
    caj_pool: List[Dict[str, Any]] = []
    pcj_pool: List[Dict[str, Any]] = []
    gj_pool: List[Dict[str, Any]] = []
    ledger_pool: List[Dict[str, Any]] = []
    trial_balance_pool: List[Dict[str, Any]] = []
    journals_pool: List[Dict[str, Any]] = []

    concepts_pool.extend([
        _make_mcq(
            prompt="A sole proprietor is best described as:",
            options=[
                "A business owned by many shareholders",
                "A one-person business where the owner receives all profits/losses",
                "A partnership of 2 to 20 partners",
                "A government-owned enterprise",
            ],
            correct_index=1,
            explanation="A sole proprietor (sole trader) is owned by one person.",
        ),
        _make_typed(
            prompt="Explain the business entity principle in a sole trader context.",
            sample_answer="The owner and the business are separate entities; business transactions must be recorded separately from the owner's personal transactions.",
        ),
    ])

    equation_pool.extend([
        _make_mcq(
            prompt="Which accounting equation is correct?",
            options=[
                "Assets = Owner's equity + Liabilities",
                "Assets = Owner's equity - Liabilities",
                "Owner's equity = Assets + Liabilities",
                "Liabilities = Owner's equity - Assets",
            ],
            correct_index=0,
            explanation="The basic accounting equation is Assets = Owner's equity + Liabilities.",
        ),
    ])

    if difficulty in ("medium", "hard"):
        sp = float(r.choice([20800, 24000, 60000, 80000]))
        pm = float(r.choice([25, 50, 66.6667]))
        cp = _calc_cost_price_from_selling_price_and_margin(sp=sp, profit_margin_pct=pm)
        equation_pool.append(
            _make_calc(
                prompt=f"A trader sells goods for R{sp:.2f}. The profit margin is {pm:g}%. Calculate the cost price.",
                correct_value=cp,
                unit="R",
            )
        )

    crj_pool.extend([
        _make_crj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_crj_single_row_question(r=r, difficulty=difficulty),
        _make_crj_cash_sales_cost_of_sales_question(r=r, difficulty=difficulty),
        _make_crj_cost_of_sales_calc_question(r=r),
        _make_crj_debtor_discount_calc_question(r=r),
    ])

    cpj_pool.extend([
        _st_make_cpj_single_row_question(r=r),
    ])

    dj_pool.extend([
        _st_make_dj_single_row_question(r=r, difficulty=difficulty),
    ])

    daj_pool.extend([
        _st_make_daj_single_row_question(r=r, difficulty=difficulty),
    ])

    cj_pool.extend([
        _st_make_cj_single_row_question(r=r, difficulty=difficulty),
    ])

    caj_pool.extend([
        _st_make_caj_single_row_question(r=r, difficulty=difficulty),
    ])

    pcj_pool.extend([
        _st_make_pcj_single_row_question(r=r, difficulty=difficulty),
    ])

    gj_pool.extend([
        _st_make_gj_single_row_question(r=r, difficulty=difficulty),
    ])

    ledger_pool.extend([
        _make_ledger_posting_question(r=r, difficulty=difficulty),
        _make_debtors_ledger_posting_question(r=r, difficulty=difficulty),
        _make_creditors_ledger_posting_question(r=r, difficulty=difficulty),
    ])

    trial_balance_pool.extend([
        _make_trial_balance_question(r=r, difficulty=difficulty),
    ])

    journals_pool.extend(crj_pool + cpj_pool + dj_pool + daj_pool + cj_pool + caj_pool + pcj_pool + gj_pool)

    accounting_cycle_pool.extend([
        _make_accounting_cycle_question(r=r),
        _make_accounting_cycle_question(r=r),
    ])

    pools_by_subskill = {
        "concepts": concepts_pool,
        "definition": concepts_pool,
        "accounting_cycle": accounting_cycle_pool,
        "accounting cycle": accounting_cycle_pool,
        "equation": equation_pool,
        "accounting equation": equation_pool,
        "ledgers": ledger_pool,
        "ledger": ledger_pool,
        "general_ledger": [
            _make_ledger_posting_question(r=r, difficulty=difficulty),
        ],
        "debtors_ledger": [
            _make_debtors_ledger_posting_question(r=r, difficulty=difficulty),
        ],
        "creditors_ledger": [
            _make_creditors_ledger_posting_question(r=r, difficulty=difficulty),
        ],
        "trial_balance": trial_balance_pool,
        "trial balance": trial_balance_pool,
        "journals": journals_pool,
        "journal": journals_pool,
        "crj": crj_pool,
        "cpj": cpj_pool,
        "dj": dj_pool,
        "daj": daj_pool,
        "cj": cj_pool,
        "caj": caj_pool,
        "pcj": pcj_pool,
        "gj": gj_pool,
        "mixed": concepts_pool + accounting_cycle_pool + equation_pool + ledger_pool + trial_balance_pool + journals_pool,
    }

    pool = pools_by_subskill.get(subskill_norm, pools_by_subskill["mixed"])
    pool = _maybe_filter(pool)

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out