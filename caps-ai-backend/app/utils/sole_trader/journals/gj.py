from __future__ import annotations

import random
import re
from typing import Any, Dict, List, Optional

from ..aliases import find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, fmt_money, make_journal, round_money
from ..names import pick_business_name, pick_person_name
from ..schemas import GJ_HEADERS


def _gj_expected_text(value: Any) -> str:
    if isinstance(value, list):
        parts = [str(v).strip() for v in value if str(v).strip()]
        return " or ".join(parts)
    return "" if value is None else str(value).strip()


def _gj_off_journal_rule(item: Optional[Dict[str, str]]) -> str:
    if not item:
        return ""
    text = str(item.get("text") or "").strip()
    journal = str(item.get("journal") or "").strip()
    why = str(item.get("why") or "").strip()
    if not text and not journal and not why:
        return ""
    base = f"{text} does not belong in the GJ"
    if journal:
        base += f"; record it in the {journal}"
    if why:
        base += f" because {why}"
    return base + "."


def _gj_extra_row_teaching_hint(*, header_label: str) -> Dict[str, str]:
    header = str(header_label or "cell").strip()
    return {
        "role_in_requirement": f"This {header} cell belongs to an extra distractor transaction line and should stay blank if no further GJ entry must be recorded.",
        "evidence_from_question": "Compare the number of valid GJ transactions in the prompt with the number of row pairs provided in the table.",
        "rule_or_principle": "Only transactions that belong in the General Journal should be recorded there. Extra unused GJ rows stay blank.",
        "how_to_derive": "Record each valid GJ transaction first. If all valid entries are complete, leave the extra pair of rows blank.",
        "transfer_tip": "In similar questions, an extra blank transaction line may be included as a distractor to test whether you know that no further GJ entry is required.",
    }


def _build_gj_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    transaction_line: str,
    row_type: str = "entry",
    off_journal_item: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    if row_type == "extra":
        return _gj_extra_row_teaching_hint(header_label=header_label)

    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = _gj_expected_text(expected)
    tx_text = str(transaction_line or "").strip()
    off_journal_rule = _gj_off_journal_rule(off_journal_item)

    role = f"This cell records the {header or 'required GJ detail'} for the journal entry."
    evidence = f"Use the transaction wording: {tx_text}" if tx_text else "Use the transaction details given in the question."
    rule = "The General Journal records transactions that do not belong in the special journals, including adjustments, corrections, transfers, and other special entries."
    method = "Identify the debit account, the credit account, and then place the amount in the correct money or control column."
    transfer_tip = "In similar GJ questions, first decide why the entry is in the GJ, then identify the debit and credit effect before completing the row."

    if header_norm in {"no", "d", "day"}:
        role = "This cell records the transaction reference or day used to identify the GJ entry."
        rule = "Use the given reference or day format shown by the question layout."
        method = f"Copy the given reference/day into the correct identification column. Here it is {expected_text or 'blank'}."
    elif header_norm == "details":
        role = "This cell records the debit account on the first line or the credit account on the second line of the GJ entry."
        rule = "Each GJ transaction uses double entry: one line for the debit account and one line for the credit account."
        method = f"Read which account must be debited or credited for this line and enter it here. Here it is {expected_text}." if expected_text else method
    elif header_norm in {"fol", "fol."}:
        role = "This cell records a folio reference when one is required."
        rule = "Folio references are only entered if the question requires them; otherwise they may remain blank."
        method = f"Enter the folio only if one is required. Here it is {expected_text or 'blank'}."
    elif header_norm == "debit":
        role = "This cell records the debit amount for the General Ledger account used on this line."
        rule = "Use the Debit column when the account on this line is a General Ledger account being debited."
        method = f"Enter the debit amount for this line. Here it is {expected_text or 'blank because the amount belongs in another money column'}."
    elif header_norm == "credit":
        role = "This cell records the credit amount for the General Ledger account used on this line."
        rule = "Use the Credit column when the account on this line is a General Ledger account being credited."
        method = f"Enter the credit amount for this line. Here it is {expected_text or 'blank because the amount belongs in another money column'}."
    elif "debtors’ control" in header_norm or "debtors' control" in header_norm:
        role = "This cell records the portion of the GJ transaction that affects Debtors Control."
        rule = "Use the Debtors Control columns when the journal entry changes the total debtors balance through a debtor-related GJ transaction."
        method = f"Place the amount in the correct Debtors Control debit or credit column. Here it is {expected_text or 'blank because Debtors Control is not affected on this line'}."
    elif "creditors’ control" in header_norm or "creditors' control" in header_norm:
        role = "This cell records the portion of the GJ transaction that affects Creditors Control."
        rule = "Use the Creditors Control columns when the journal entry changes the total creditors balance through a creditor-related GJ transaction."
        method = f"Place the amount in the correct Creditors Control debit or credit column. Here it is {expected_text or 'blank because Creditors Control is not affected on this line'}."

    if off_journal_rule:
        rule = f"{rule} {off_journal_rule}".strip()
        method = f"{method} Ignore the off-journal item when completing the GJ table.".strip()

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def _make_gj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    debtor = pick_person_name(r=r)
    supplier = pick_business_name(r=r)
    amount = float(r.randrange(250, 3200 + 1, 50))
    variant = r.choice(["cash_sale", "credit_purchase", "debtor_return", "cash_payment"])
    if variant == "cash_sale":
        doc = f"CRR{r.randrange(10, 99)}"
        text = f"{doc} Cash sale of goods, R{amount:.2f}"
        return {"text": text, "journal": "CRJ", "why": "cash receipts are recorded in the CRJ, not in the GJ"}
    if variant == "credit_purchase":
        doc = f"INV{r.randrange(100, 999)}"
        text = f"{doc} Bought trading stock on credit from {supplier}, R{amount:.2f}"
        return {"text": text, "journal": "CJ", "why": "credit purchases are recorded in the CJ, not in the GJ"}
    if variant == "debtor_return":
        doc = f"CN{r.randrange(100, 999)}"
        text = f"{doc} Issued a credit note to {debtor} for goods returned, R{amount:.2f}"
        return {"text": text, "journal": "DAJ", "why": "debtor returns and allowances are recorded in the DAJ, not in the GJ"}
    cheque_no = f"{r.randrange(120, 299)}"
    text = f"Cheque no. {cheque_no} paid to {supplier}, R{amount:.2f}"
    return {"text": text, "journal": "CPJ", "why": "cash payments are recorded in the CPJ, not in the GJ"}


def _gj_money_col_for_side(side: str) -> Optional[str]:
    s = str(side or "").strip().lower()
    if s == "main_debit":
        return "Debit"
    if s == "main_credit":
        return "Credit"
    if s == "dc_debit":
        return "Debtors’ control debit"
    if s == "dc_credit":
        return "Debtors’ control credit"
    if s == "cc_debit":
        return "Creditors’ control debit"
    if s == "cc_credit":
        return "Creditors’ control credit"
    return None


def _make_gj_provisional_totals(*, r: random.Random) -> Dict[str, float]:
    return {
        "Debtors’ control debit": float(r.choice([120, 180, 240, 350, 420, 624, 825, 960, 1800])),
        "Debtors’ control credit": float(r.choice([90, 116, 160, 230, 270, 316, 384, 454, 970])),
        "Creditors’ control debit": float(r.choice([70, 105, 120, 150, 180, 268, 350, 702, 1150])),
        "Creditors’ control credit": float(r.choice([90, 160, 230, 270, 348, 384, 454, 870, 1220])),
    }


def _make_gj_transaction(*, r: random.Random, amount: float, kind: Optional[str] = None) -> Dict[str, Any]:
    amt = float(round_money(amount))
    if kind is None:
        kind = r.choice([
            "bad_debts_written_off",
            "bad_debts_recovered",
            "discount_allowed_cancelled_dishonoured_cheque",
            "interest_on_overdue_debtors",
            "interest_on_overdue_creditors",
            "withdrawal_of_goods_by_owner",
            "donation_of_stock",
            "drawings_of_stationery",
            "correction_of_error",
            "transfer_debtor_to_creditor",
            "transfer_creditor_to_debtor",
        ])

    if kind == "bad_debts_written_off":
        debtor = pick_person_name(r=r)
        return {
            "kind": kind,
            "debit_account": "Bad debts",
            "debit_side": "main_debit",
            "credit_account": debtor,
            "credit_side": "dc_credit",
            "amount": amt,
            "narrative": f"{debtor}, a debtor, was declared insolvent. The irrecoverable balance of R{amt:.2f} must be written off.",
        }

    if kind == "bad_debts_recovered":
        debtor = pick_person_name(r=r)
        debit_account = r.choice(["Bank", "Equipment"])
        return {
            "kind": kind,
            "debit_account": debit_account,
            "debit_side": "main_debit",
            "credit_account": "Bad debts recovered",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Received {debit_account.lower()} from {debtor}, a debtor whose account had previously been written off. Value received: R{amt:.2f}.",
        }

    if kind == "discount_allowed_cancelled_dishonoured_cheque":
        debtor = pick_person_name(r=r)
        return {
            "kind": kind,
            "debit_account": debtor,
            "debit_side": "dc_debit",
            "credit_account": "Discount allowed",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"A dishonoured cheque from {debtor} has already been recorded in the books. The discount allowed of R{amt:.2f} must still be cancelled.",
        }

    if kind == "interest_on_overdue_debtors":
        debtor = pick_person_name(r=r)
        credit_account = r.choice(["Interest on overdue debtors", "Interest receivable"])
        return {
            "kind": kind,
            "debit_account": debtor,
            "debit_side": "dc_debit",
            "credit_account": credit_account,
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Charge interest on the overdue account of {debtor}. Interest amount to record: R{amt:.2f}.",
        }

    if kind == "interest_on_overdue_creditors":
        creditor = pick_business_name(r=r)
        return {
            "kind": kind,
            "debit_account": "Interest on overdue creditors",
            "debit_side": "main_debit",
            "credit_account": creditor,
            "credit_side": "cc_credit",
            "amount": amt,
            "narrative": f"Interest on the overdue account of creditor {creditor} must be recorded. Interest amount: R{amt:.2f}.",
        }

    if kind == "withdrawal_of_goods_by_owner":
        return {
            "kind": kind,
            "debit_account": "Drawings",
            "debit_side": "main_debit",
            "credit_account": "Trading stock",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"The owner withdrew trading stock for personal use. Cost price of the goods withdrawn: R{amt:.2f}.",
        }

    if kind == "donation_of_stock":
        return {
            "kind": kind,
            "debit_account": "Donations",
            "debit_side": "main_debit",
            "credit_account": "Trading stock",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Trading stock was donated to a local charity. Cost price of the stock donated: R{amt:.2f}.",
        }

    if kind == "drawings_of_stationery":
        return {
            "kind": kind,
            "debit_account": "Drawings",
            "debit_side": "main_debit",
            "credit_account": "Stationery",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"The owner took stationery worth R{amt:.2f} for personal use.",
        }

    if kind == "transfer_debtor_to_creditor":
        person = pick_person_name(r=r)
        return {
            "kind": kind,
            "debit_account": f"{person} (Creditor)",
            "debit_side": "cc_debit",
            "credit_account": f"{person} (Debtor)",
            "credit_side": "dc_credit",
            "amount": amt,
            "narrative": f"Transfer a debit balance of R{amt:.2f} for {person} from the Debtors’ Ledger to the Creditors’ Ledger.",
        }

    if kind == "transfer_creditor_to_debtor":
        person = pick_person_name(r=r)
        return {
            "kind": kind,
            "debit_account": f"{person} (Debtor)",
            "debit_side": "dc_debit",
            "credit_account": f"{person} (Creditor)",
            "credit_side": "cc_credit",
            "amount": amt,
            "narrative": f"Transfer a debit balance of R{amt:.2f} for {person} from the Creditors’ Ledger to the Debtors’ Ledger.",
        }

    error_case = r.choice([
        "stock_recorded_as_stationery",
        "stationery_recorded_as_trading_stock",
        "repairs_posted_to_land_and_buildings",
        "fixed_deposit_interest",
        "allowance_posted_wrong_creditor",
        "return_posted_wrong_debtor",
        "wages_posted_instead_of_creditors_for_wages",
    ])

    if error_case == "stock_recorded_as_stationery":
        return {
            "kind": kind,
            "debit_account": "Trading stock",
            "debit_side": "main_debit",
            "credit_account": "Stationery",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Trading stock purchased for R{amt:.2f} was incorrectly recorded as stationery. Correct the error.",
            "error_case": error_case,
        }

    if error_case == "stationery_recorded_as_trading_stock":
        return {
            "kind": kind,
            "debit_account": "Stationery",
            "debit_side": "main_debit",
            "credit_account": "Trading stock",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Stationery purchased for R{amt:.2f} was incorrectly recorded as trading stock. Correct the error.",
            "error_case": error_case,
        }

    if error_case == "repairs_posted_to_land_and_buildings":
        return {
            "kind": kind,
            "debit_account": "Repairs",
            "debit_side": "main_debit",
            "credit_account": "Land and buildings",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"Repairs to the roof of the building cost R{amt:.2f}, but the amount was posted to Land and buildings in error. Correct the error.",
            "error_case": error_case,
        }

    if error_case == "fixed_deposit_interest":
        bank = r.choice(["ABSA", "RSA Bank", "Angel Bank", "MB Bank"])
        principal = float(r.choice([16000, 32000, 50000, 100000]))
        total_received = principal + amt
        return {
            "kind": kind,
            "debit_account": f"Fixed deposit: {bank}",
            "debit_side": "main_debit",
            "credit_account": "Interest on fixed deposit",
            "credit_side": "main_credit",
            "amount": amt,
            "narrative": f"The business received R{total_received:.2f} from {bank} for a fixed deposit that matured. Included in the amount is interest on fixed deposit of R{amt:.2f}. The full amount was credited to the Fixed Deposit account. Correct the error.",
            "error_case": error_case,
        }

    if error_case == "allowance_posted_wrong_creditor":
        correct = pick_business_name(r=r)
        wrong = pick_business_name(r=r)
        while wrong == correct:
            wrong = pick_business_name(r=r)
        return {
            "kind": kind,
            "debit_account": correct,
            "debit_side": "cc_debit",
            "credit_account": wrong,
            "credit_side": "cc_credit",
            "amount": amt,
            "narrative": f"A creditor allowance of R{amt:.2f} from {correct} was wrongly posted to {wrong}. Correct the error.",
            "error_case": error_case,
        }

    if error_case == "return_posted_wrong_debtor":
        correct = pick_person_name(r=r)
        wrong = pick_person_name(r=r)
        while wrong == correct:
            wrong = pick_person_name(r=r)
        return {
            "kind": kind,
            "debit_account": wrong,
            "debit_side": "dc_debit",
            "credit_account": correct,
            "credit_side": "dc_credit",
            "amount": amt,
            "narrative": f"Goods returned by {correct}, a debtor, for R{amt:.2f} were incorrectly posted to the account of {wrong}. Correct the error.",
            "error_case": error_case,
        }

    return {
        "kind": kind,
        "debit_account": "Creditors for wages",
        "debit_side": "main_debit",
        "credit_account": "Wages",
        "credit_side": "main_credit",
        "amount": amt,
        "narrative": f"A cheque drawn for creditors for wages for R{amt:.2f} was incorrectly posted to the Wages account. Correct the error.",
        "error_case": "wages_posted_instead_of_creditors_for_wages",
    }


def _gj_variant_defs() -> List[Dict[str, Any]]:
    variant_a_headers = list(GJ_HEADERS)
    variant_a_header_rows = [
        [
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Details", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Debit", "rowSpan": 2, "colSpan": 1},
            {"label": "Credit", "rowSpan": 2, "colSpan": 1},
            {"label": "Debtors’ control", "rowSpan": 1, "colSpan": 2},
            {"label": "Creditors’ control", "rowSpan": 1, "colSpan": 2},
        ],
        [
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    variant_b_headers = [
        "No",
        "D",
        "Details",
        "Fol",
        "Debit",
        "Credit",
        "Debtors’ control debit",
        "Debtors’ control credit",
        "Creditors’ control debit",
        "Creditors’ control credit",
    ]
    variant_b_header_rows = [
        [
            {"label": "No", "rowSpan": 2, "colSpan": 1},
            {"label": "D", "rowSpan": 2, "colSpan": 1},
            {"label": "Details", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Debit", "rowSpan": 2, "colSpan": 1},
            {"label": "Credit", "rowSpan": 2, "colSpan": 1},
            {"label": "Debtors’ control", "rowSpan": 1, "colSpan": 2},
            {"label": "Creditors’ control", "rowSpan": 1, "colSpan": 2},
        ],
        [
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    return [
        {"id": "A", "headers": variant_a_headers, "header_rows": variant_a_header_rows},
        {"id": "B", "headers": variant_b_headers, "header_rows": variant_b_header_rows},
    ]


def make_gj_activity13_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
    variant_style: str = "activity",
) -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013, 2014]))
    mode_norm = str(mode or "").strip().lower()
    style_norm = str(variant_style or "activity").strip().lower()
    off_journal_item = _make_gj_off_journal_item(r=r)

    def _days_in_month(*, month_name: str, year_value: int) -> int:
        m = str(month_name or "").strip().lower()
        if m in {"april", "june", "september", "november"}:
            return 30
        if m == "february":
            y = int(year_value)
            is_leap = (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))
            return 29 if is_leap else 28
        return 31

    vdefs = _gj_variant_defs()
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

    def _fmt(x: Optional[float]) -> str:
        if x is None:
            return ""
        return fmt_money(round_money(x))

    _HUMAN_INITIALS_RE = re.compile(r"^(?P<initials>(?:[A-Z]\.?\s*)+)(?P<surname>[A-Z][a-zA-Z\-']+)$")

    def _human_name_variants(name: str) -> Optional[List[str]]:
        raw = str(name or "").strip()
        m = _HUMAN_INITIALS_RE.match(raw)
        if not m:
            return None
        initials = m.group("initials").strip()
        surname = m.group("surname").strip()

        # Normalize whitespace and punctuation around initials:
        # Accept: "B. Obama" and "B Obama" (also multiple initials like "B. K. Obama").
        initials_no_dots = initials.replace(".", " ")
        initials_no_dots = " ".join(initials_no_dots.split())
        initials_with_dots = " ".join([f"{ch}." if len(ch) == 1 else ch for ch in initials_no_dots.split()])

        v1 = f"{initials_with_dots} {surname}".strip()
        v2 = f"{initials_no_dots} {surname}".strip()
        out: List[str] = []
        for v in (v1, v2, raw):
            if v and v not in out:
                out.append(v)
        return out if out else None

    n_tx = 7 if style_norm == "exam" else int(r.choice([5, 6]))
    max_day = _days_in_month(month_name=month, year_value=year)
    day_pool = [d for d in [1, 2, 4, 5, 8, 10, 12, 14, 15, 18, 20, 22, 23, 26, 27, 29, 30, 31] if d <= max_day]
    days = sorted(r.sample(day_pool, k=n_tx))

    scheme = r.choice(["letters", "numbers", "days"])
    if scheme == "letters":
        refs = [chr(ord("a") + i) for i in range(n_tx)]
    elif scheme == "numbers":
        start = int(r.choice([1, 4, 7, 10]))
        refs = [str(start + i) for i in range(n_tx)]
    else:
        refs = [str(d) for d in days]

    base_amounts = r.sample([150, 200, 250, 300, 350, 400, 450, 500, 650, 800, 900, 1200, 1400, 1800, 2400, 3600], k=n_tx)
    amounts = [float(x) for x in base_amounts]

    non_correction_archetypes = [
        "bad_debts_written_off",
        "bad_debts_recovered",
        "discount_allowed_cancelled_dishonoured_cheque",
        "interest_on_overdue_debtors",
        "interest_on_overdue_creditors",
        "withdrawal_of_goods_by_owner",
        "donation_of_stock",
        "drawings_of_stationery",
        "transfer_debtor_to_creditor",
        "transfer_creditor_to_debtor",
    ]
    correction_slots = min(n_tx, 2 if style_norm == "exam" else 1)
    chosen_archetypes = ["correction_of_error" for _ in range(correction_slots)]
    sample_size = min(max(0, n_tx - len(chosen_archetypes)), len(non_correction_archetypes))
    chosen_archetypes.extend(r.sample(non_correction_archetypes, k=sample_size))
    while len(chosen_archetypes) < n_tx:
        chosen_archetypes.append(r.choice(non_correction_archetypes + ["correction_of_error"]))
    r.shuffle(chosen_archetypes)

    tx_rows: List[Dict[str, Any]] = []
    for i in range(n_tx):
        tx = _make_gj_transaction(r=r, amount=amounts[i], kind=chosen_archetypes[i])
        tx_rows.append({
            "ref": refs[i],
            "day": str(days[i]),
            **tx,
        })

    def _blank_tx() -> Dict[str, Any]:
        return {
            "ref": "",
            "day": "",
            "debit_account": "",
            "credit_account": "",
            "debit_side": "",
            "credit_side": "",
            "amount": None,
        }

    if mode_norm == "scaffold":
        body = tx_rows
    else:
        body = [_blank_tx() for _ in range(n_tx)]

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    def _set(row_index: int, col_index: int, expected: Any) -> None:
        correct_map[f"r{row_index}_c{col_index}"] = expected

    provisional_totals = _make_gj_provisional_totals(r=r)
    totals_by_col: Dict[str, float] = dict(provisional_totals)
    opening_values: List[Optional[str]] = ["" for _ in range(len(headers))]
    opening_no_col = _col("No")
    opening_d_col = _col("D")
    opening_day_col = _col("Day")
    opening_details_col = _col("Details")
    opening_fol_col = _col("Fol")
    if opening_d_col is not None:
        opening_values[opening_d_col] = str(max_day)
    if opening_day_col is not None:
        opening_values[opening_day_col] = str(max_day)
    if opening_details_col is not None:
        opening_values[opening_details_col] = r.choice(["Totals", "Provisional totals"])
    if opening_fol_col is not None:
        opening_values[opening_fol_col] = "b/d"
    if opening_no_col is not None:
        opening_values[opening_no_col] = ""
    for header_name, total in provisional_totals.items():
        c = _col(header_name)
        if c is not None:
            opening_values[c] = _fmt(total)
    rows.append(build_journal_row(row_index=0, values=opening_values, editable_cols=[]))

    for tx_i in range(n_tx):
        expected_tx = tx_rows[tx_i]
        tx = body[tx_i]
        amt = float(expected_tx["amount"])

        for line in (0, 1):
            row_index = 1 + (tx_i * 2) + line
            is_first_line = line == 0
            values: List[Optional[str]] = []
            for h in headers:
                hn = str(h).strip().lower()
                if hn in {"no", "no."}:
                    values.append(tx.get("ref", "") if is_first_line else "")
                elif hn in {"d", "day"}:
                    values.append(tx.get("day", "") if is_first_line else "")
                elif hn == "details":
                    if is_first_line:
                        values.append(tx.get("debit_account", ""))
                    else:
                        values.append(tx.get("credit_account", ""))
                elif hn in {"fol", "fol."}:
                    values.append("")
                else:
                    values.append("")

            if mode_norm == "scaffold":
                editable_cols = list(range(len(headers)))
            else:
                editable_cols = list(range(len(headers)))
            if not is_first_line:
                # Keep numbering/date blank on the second line; learners should focus on accounts/amounts.
                for name in ("No", "D", "Day"):
                    c = _col(name)
                    if c is not None and c in editable_cols:
                        editable_cols.remove(c)

            rows.append(build_journal_row(row_index=row_index, values=values, editable_cols=editable_cols))

            no_col = _col("No")
            d_col = _col("D")
            day_col = _col("Day")
            details_col = _col("Details")

            if is_first_line:
                if variant_id == "B":
                    if no_col is not None:
                        _set(row_index, no_col, ["", expected_tx["ref"]])
                    if d_col is not None:
                        _set(row_index, d_col, ["", expected_tx["day"]])
                else:
                    if day_col is not None:
                        allowed = ["", expected_tx["day"]]
                        ref_value = str(expected_tx["ref"]).strip()
                        if ref_value and ref_value not in allowed:
                            allowed.append(ref_value)
                        _set(row_index, day_col, allowed)
            else:
                # Second line: numbering/date should remain blank.
                if variant_id == "B":
                    if no_col is not None:
                        _set(row_index, no_col, "")
                    if d_col is not None:
                        _set(row_index, d_col, "")
                else:
                    if day_col is not None:
                        _set(row_index, day_col, "")

            if details_col is not None:
                exp_details = expected_tx["debit_account"] if is_first_line else expected_tx["credit_account"]
                variants = _human_name_variants(exp_details)
                _set(row_index, details_col, variants if variants is not None else exp_details)

                if mode_norm == "scaffold":
                    k = str(expected_tx.get("kind") or "").strip().lower()
                    if is_first_line:
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Why two lines?",
                            "steps": [
                                "Each General Journal transaction is recorded using double entry:",
                                "Line 1 shows the DEBIT account.",
                                "Line 2 (the next row) shows the CREDIT account.",
                                "The amount must appear once on the debit side and once on the credit side.",
                            ],
                        }

                    if k == "bad_debts_written_off":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Bad debts written off",
                            "steps": [
                                "Writing off a bad debt reduces what debtors owe.",
                                "So Debtors’ control is CREDITED.",
                                "Bad debts is an expense, so it is DEBITED.",
                            ],
                        }
                    elif k == "bad_debts_recovered":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Bad debts recovered",
                            "steps": [
                                "When a debtor previously written off pays later, it is income.",
                                "Debit the asset received (Bank/Equipment) and credit Bad debts recovered.",
                            ],
                        }
                    elif k == "discount_allowed_cancelled_dishonoured_cheque":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Dishonoured cheque: cancel discount",
                            "steps": [
                                "Discount allowed was given earlier, but must now be reversed.",
                                "Increase what the debtor owes again: DEBIT Debtors’ control.",
                                "Reverse the discount: CREDIT Discount allowed.",
                            ],
                        }
                    elif k in {"interest_on_overdue_debtors", "interest_on_overdue_creditors"}:
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Interest entry",
                            "steps": [
                                "Interest is recorded as income (debtors) or an expense (creditors).",
                                "The control account is used because the interest affects the debtor/creditor balance.",
                            ],
                        }
                    elif k == "withdrawal_of_goods_by_owner":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Owner withdraws goods",
                            "steps": [
                                "Goods taken for personal use reduce trading stock.",
                                "So Trading stock is CREDITED.",
                                "The owner's drawings increase, so Drawings is DEBITED.",
                            ],
                        }
                    elif k == "donation_of_stock":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Donation of stock",
                            "steps": [
                                "Stock donated by the business is treated as an expense at cost price.",
                                "So Donations is DEBITED and Trading stock is CREDITED.",
                            ],
                        }
                    elif k == "drawings_of_stationery":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Owner takes stationery",
                            "steps": [
                                "When the owner takes stationery for personal use, Drawings increases.",
                                "The Stationery account must be reduced on the credit side.",
                            ],
                        }
                    elif k == "transfer_debtor_to_creditor" or k == "transfer_creditor_to_debtor":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Transfer between debtor and creditor ledgers",
                            "steps": [
                                "The same person is both a debtor and a creditor.",
                                "You move the balance between ledgers using the control accounts.",
                                "One control account is debited and the other is credited.",
                            ],
                        }
                    elif k == "correction_of_error":
                        cell_hints[f"r{row_index}_c{details_col}"] = {
                            "title": "Correction of error",
                            "steps": [
                                "Identify the wrong account used and reverse it.",
                                "Then record the correct account.",
                                "Think: which account should increase (debit) and which should decrease (credit)?",
                            ],
                        }

            side = expected_tx["debit_side"] if is_first_line else expected_tx["credit_side"]
            col_name = _gj_money_col_for_side(side)
            if col_name is not None:
                c = _col(col_name)
                if c is not None:
                    _set(row_index, c, _fmt(amt))
                    totals_by_col[col_name] = totals_by_col.get(col_name, 0.0) + amt

                    # Notes.md: add per-entry calculation hint scaffolding for calculated figures.
                    if mode_norm == "scaffold":
                        k = str(expected_tx.get("kind") or "").strip().lower()
                        if k in {"interest_on_overdue_debtors", "interest_on_overdue_creditors"}:
                            cell_hints[f"r{row_index}_c{c}"] = {
                                "title": "Interest calculation",
                                "steps": [
                                    "If the interest amount is not given directly:",
                                    "Interest = Principal × Rate × Time",
                                    "Use Time as a fraction of a year (e.g. months ÷ 12).",
                                    "Round to 2 decimal places.",
                                ],
                            }
                        elif k == "bad_debts_written_off":
                            cell_hints[f"r{row_index}_c{c}"] = {
                                "title": "Bad debts amount",
                                "steps": [
                                    "If asked to write off a debt: use the amount owing by the debtor.",
                                    "Record the same amount on both sides (double entry).",
                                ],
                            }
                        elif k == "discount_allowed_cancelled_dishonoured_cheque":
                            cell_hints[f"r{row_index}_c{c}"] = {
                                "title": "Discount cancelled amount",
                                "steps": [
                                    "Use the discount amount that was previously allowed.",
                                    "This is a reversal, so the amount is entered once on the debit side and once on the credit side.",
                                ],
                            }

            # Ensure all other money columns are marked as blank for this row
            for other in [
                "Debit",
                "Credit",
                "Debtors’ control debit",
                "Debtors’ control credit",
                "Creditors’ control debit",
                "Creditors’ control credit",
            ]:
                if other == col_name:
                    continue
                c = _col(other)
                if c is not None:
                    _set(row_index, c, "")

            for c_idx, header in enumerate(headers):
                cell_id = f"r{row_index}_c{c_idx}"
                if cell_id not in correct_map:
                    continue
                cell_teaching_map[cell_id] = _build_gj_teaching_hint(
                    header_label=header,
                    expected=correct_map[cell_id],
                    transaction_line=str(expected_tx.get("narrative") or ""),
                    off_journal_item=off_journal_item,
                )

    extra_start_index = len(rows)
    for extra_offset in range(2):
        extra_row_index = extra_start_index + extra_offset
        extra_values: List[Optional[str]] = ["" for _ in range(len(headers))]
        extra_editable_cols = list(range(len(headers)))
        rows.append(build_journal_row(row_index=extra_row_index, values=extra_values, editable_cols=extra_editable_cols))
        for c_idx, header in enumerate(headers):
            _set(extra_row_index, c_idx, "")
            cell_id = f"r{extra_row_index}_c{c_idx}"
            cell_hints[cell_id] = {
                "title": "Extra row not required",
                "steps": [
                    "This extra row pair is a distractor.",
                    "If all valid GJ transactions have already been recorded, leave this row blank.",
                ],
            }
            cell_teaching_map[cell_id] = _build_gj_teaching_hint(
                header_label=header,
                expected="",
                transaction_line="Extra GJ distractor row",
                row_type="extra",
                off_journal_item=off_journal_item,
            )

    must_total = True
    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = []
        totals_editable: List[int] = []
        for h in headers:
            hn = str(h).strip().lower()
            if hn in {"no", "no.", "day", "d"}:
                totals_values.append("")
                continue
            elif hn == "details":
                totals_values.append("")
                continue
            elif hn in {"fol", "fol."}:
                totals_values.append("")
                continue
            else:
                totals_values.append("")
                totals_editable.append(len(totals_values) - 1)
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable))
        for header_name, total in totals_by_col.items():
            c = _col(header_name)
            if c is not None:
                _set(totals_index, c, fmt_money(round_money(total)))
                cell_id = f"r{totals_index}_c{c}"
                cell_teaching_map[cell_id] = _build_gj_teaching_hint(
                    header_label=headers[c],
                    expected=correct_map.get(cell_id),
                    transaction_line="Totals row for the GJ",
                    off_journal_item=off_journal_item,
                )

    off_journal_day = int(r.choice([2, 6, 9, 11, 16, 19, 25, 28]))
    transactions_lines = "\n".join([
        f"{tx_rows[i]['ref']} {tx_rows[i]['day']} {month}: {tx_rows[i]['narrative']}" if scheme != "days" else f"{tx_rows[i]['day']} {month}: {tx_rows[i]['narrative']}"
        for i in range(n_tx)
    ] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])

    prompt = (
        f"{business}\n"
        f"General Journal (GJ) for {month} {year} (Variant {variant_id})\n\n"
        "Transactions (in this order):\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        "Record the transactions in the General Journal in the same order as given. The provisional totals row is already entered. Close off the journal properly and ignore the transaction that belongs in another journal."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Write the entries in the same order as the transactions given above.",
            "Each transaction uses two rows: debit first, credit second.",
            "The provisional totals row is already provided at the top of the journal.",
            "Leave transaction references blank if you want, but if you enter them they must match the transaction list.",
        ]
        if must_total:
            guidelines.append("Totals row: add down each money column and enter the totals.")
        guidelines.append(f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.")

    return make_journal(
        prompt=prompt,
        journal_type="GJ",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        guidelines=guidelines,
        table_variant="grade_project",
        column_help=headers_to_column_help(journal_type="gj", headers=headers) if mode_norm == "scaffold" else {},
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        title_fields=title_fields,
    )


def make_gj_exam_style_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
) -> Dict[str, Any]:
    return make_gj_activity13_question(r=r, difficulty=difficulty, mode=mode, variant_id=variant_id, variant_style="exam")


def make_gj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    day = int(r.choice([1, 3, 6, 9, 12, 15, 18, 22, 27]))
    off_journal_item = _make_gj_off_journal_item(r=r)
    off_journal_day = int(r.choice([2, 5, 8, 11, 16, 19, 23, 27]))

    # Keep this simple and deterministic: choose one double-entry case that uses control accounts.
    kind = r.choice([
        "bad_debts_written_off",
        "discount_allowed_cancelled_dishonoured_cheque",
        "interest_on_overdue_debtors",
        "interest_on_overdue_creditors",
        "transfer_debtor_to_creditor",
        "transfer_creditor_to_debtor",
        "correction_of_error",
    ])

    amount = float(r.choice([450, 800, 1200, 1800, 2400, 3600]))
    tx = _make_gj_transaction(r=r, amount=amount, kind=kind)
    tx_line = f"{day} {month}: {tx['narrative']}"

    headers = list(GJ_HEADERS)
    rows: List[List[Dict[str, Any]]] = []

    # Find columns
    day_col = find_col(headers, ["Day"])
    details_col = find_col(headers, ["Details"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    debit_col = find_col(headers, ["Debit"])
    credit_col = find_col(headers, ["Credit"])

    dcd_col = find_col(headers, ["Debtors’ control debit", "Debtors' control debit"])
    dcc_col = find_col(headers, ["Debtors’ control credit", "Debtors' control credit"])

    ccd_col = find_col(headers, ["Creditors’ control debit", "Creditors' control debit"])
    ccc_col = find_col(headers, ["Creditors’ control credit", "Creditors' control credit"])

    editable_cols: List[int] = []
    for col in [
        fol_col,
        debit_col,
        credit_col,
        dcd_col,
        dcc_col,
        ccd_col,
        ccc_col,
    ]:
        if col is not None:
            editable_cols.append(col)

    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    def _set(row_index: int, col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r{row_index}_c{col}"] = expected

    for line in (0, 1):
        row_index = line
        is_first_line = line == 0
        values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if day_col is not None and is_first_line:
            values[day_col] = str(day)
        if details_col is not None:
            values[details_col] = tx["debit_account"] if is_first_line else tx["credit_account"]
        if fol_col is not None:
            values[fol_col] = ""
        rows.append(build_journal_row(row_index=row_index, values=values, editable_cols=sorted(set(editable_cols))))

        _set(row_index, fol_col, "")

        side = tx["debit_side"] if is_first_line else tx["credit_side"]
        col_name = _gj_money_col_for_side(side)
        target_cols = {
            "Debit": debit_col,
            "Credit": credit_col,
            "Debtors’ control debit": dcd_col,
            "Debtors’ control credit": dcc_col,
            "Creditors’ control debit": ccd_col,
            "Creditors’ control credit": ccc_col,
        }
        for name, col in target_cols.items():
            _set(row_index, col, fmt_money(round_money(tx["amount"])) if name == col_name else "")

        for c_idx, header in enumerate(headers):
            cell_id = f"r{row_index}_c{c_idx}"
            if cell_id not in correct_map:
                continue
            cell_teaching_map[cell_id] = _build_gj_teaching_hint(
                header_label=header,
                expected=correct_map[cell_id],
                transaction_line=tx_line,
                off_journal_item=off_journal_item,
            )

    if debit_col is not None:
        cell_hints[f"r0_c{debit_col}"] = {
            "title": "Debit side",
            "steps": [
                "The debit entry is recorded on the first side affected by the transaction.",
                "Enter the amount once in the correct debit column.",
            ],
        }
    if credit_col is not None:
        cell_hints[f"r1_c{credit_col}"] = {
            "title": "Credit side",
            "steps": [
                "The credit entry is recorded on the opposite side of the same transaction.",
                "Enter the amount once in the correct credit column.",
            ],
        }
    control_side = None
    control_row = None
    if str(tx.get("debit_side") or "").strip().lower() in {"dc_debit", "dc_credit", "cc_debit", "cc_credit"}:
        control_side = str(tx.get("debit_side") or "").strip().lower()
        control_row = 0
    elif str(tx.get("credit_side") or "").strip().lower() in {"dc_debit", "dc_credit", "cc_debit", "cc_credit"}:
        control_side = str(tx.get("credit_side") or "").strip().lower()
        control_row = 1
    if control_side is not None and control_row is not None:
        control_col = {
            "dc_debit": dcd_col,
            "dc_credit": dcc_col,
            "cc_debit": ccd_col,
            "cc_credit": ccc_col,
        }.get(control_side)
        if control_col is not None:
            cell_hints[f"r{control_row}_c{control_col}"] = {
                "title": "Control account column",
                "steps": [
                    "Use a control-account column when the transaction changes the total debtors or creditors balance.",
                    "The same amount must still be matched by the opposite side of the double entry.",
                ],
            }

    # Grouped header layout: Debtors’ control and Creditors’ control each span 2 subcolumns (Debit/Credit)
    header_rows = [
        [
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Details", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Debit", "rowSpan": 2, "colSpan": 1},
            {"label": "Credit", "rowSpan": 2, "colSpan": 1},
            {"label": "Debtors’ control", "rowSpan": 1, "colSpan": 2},
            {"label": "Creditors’ control", "rowSpan": 1, "colSpan": 2},
        ],
        [
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
            {"label": "Debit", "rowSpan": 1, "colSpan": 1},
            {"label": "Credit", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    prompt = (
        f"{business}\n"
        f"General Journal (GJ) for {month}\n\n"
        "Transactions:\n"
        f"- {tx_line}\n"
        f"- {off_journal_day} {month}: {off_journal_item['text']}\n\n"
        "Required:\n"
        "Complete the General Journal entry for the General Journal transaction only. Use two rows: debit first, credit second. Ignore the transaction that belongs in another journal."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month

    return make_journal(
        prompt=prompt,
        journal_type="gj",
        table_variant="grade_project",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="gj", headers=headers),
        guidelines=[
            "Use one row for the debit entry and the next row for the credit entry.",
            "Amounts must be entered once on the debit side and once on the credit side (double entry).",
            "Use Debtors’ control / Creditors’ control where applicable.",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
        ],
    )
