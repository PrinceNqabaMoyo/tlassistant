from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.names import pick_business_name as _pick_business_name
from ..sole_trader.names import pick_business_names as _pick_business_names
from ..sole_trader.names import pick_person_names as _pick_person_names

from .sole_trader_ledger_helpers import build_gl_teaching_hint as _build_gl_teaching_hint
from .sole_trader_ledger_helpers import cpj_totals_headers_ledger as _cpj_totals_headers_ledger
from .sole_trader_ledger_helpers import crj_totals_headers_ledger as _crj_totals_headers_ledger
from .sole_trader_ledger_helpers import general_ledger_account_headers as _general_ledger_account_headers


def make_general_ledger_posting_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = _pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    month_short = str(month)[:3]
    next_month_short = {"jan": "Feb", "feb": "Mar", "mar": "Apr", "apr": "May", "may": "Jun", "jun": "Jul"}.get(month_short.lower(), month_short)
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    crj_bank = float(r.choice([23860, 36000, 57830, 73860]))
    crj_sales = float(r.choice([4400, 14000, 22720, 44000]))
    crj_cost_of_sales = _round_money(crj_sales * float(r.choice([0.5, 0.6])))
    crj_debtors_control = float(r.choice([2800, 3380, 4280, 8960]))
    crj_discount_allowed = float(r.choice([60, 120, 200, 270]))
    crj_current_income = float(r.choice([0, 150, 300, 405]))

    cpj_bank = float(r.choice([9930, 45360, 66350, 93200]))
    cpj_trading_stock = float(r.choice([17900, 18000, 27900, 42400]))
    cpj_creditors_control = float(r.choice([4690, 6510, 28900, 36510]))
    cpj_wages = float(r.choice([1500, 3500, 7000]))
    cpj_stationery = float(r.choice([300, 1500, 1620, 3400]))

    dj_sales = float(r.choice([8800, 12800, 14300, 22720]))
    dj_cost_of_sales = _round_money(dj_sales * float(r.choice([0.5, 0.6])))
    daj_allowances = float(r.choice([440, 1200, 3100]))
    daj_cost_of_sales = _round_money(daj_allowances * float(r.choice([0.5, 0.6])))
    cj_creditors_control = float(r.choice([18400, 20423, 58400]))
    cj_trading_stock = float(r.choice([5990, 10361, 25990]))
    cj_stationery = float(r.choice([0, 461, 690, 1500]))
    cj_equipment = float(r.choice([0, 804, 1980, 6281]))
    caj_creditors_control = float(r.choice([1900, 3167, 6900]))
    caj_trading_stock = float(r.choice([570, 1890, 4800]))
    caj_stationery = float(r.choice([0, 74, 151, 248]))
    caj_equipment = float(r.choice([0, 104, 320, 804]))

    gj_bad_debts = float(r.choice([160, 480, 840, 1440]))
    gj_interest_overdue_debtors = float(r.choice([56, 80, 102, 140]))
    gj_drawings_stock = float(r.choice([250, 500, 900]))
    gj_drawings_stationery = float(r.choice([0, 100, 180, 275]))
    gj_donation = float(r.choice([300, 600, 1200]))
    gj_wages_accrued = float(r.choice([1800, 4200, 10720]))

    debtor_names = _pick_person_names(r=r, k=3)
    creditor_names = _pick_business_names(r=r, k=3)
    bad_debt_debtor = debtor_names[0]
    interest_debtor = debtor_names[1]
    distractor_debtor = debtor_names[2]
    distractor_creditor = creditor_names[2]

    crj_values: List[Optional[str]] = ["TOTAL", "", "Totals", "", _fmt_money(crj_bank), _fmt_money(crj_sales), _fmt_money(crj_cost_of_sales), _fmt_money(crj_debtors_control), _fmt_money(crj_discount_allowed), _fmt_money(crj_current_income) if crj_current_income else "", "", "", ""]
    cpj_values: List[Optional[str]] = ["TOTAL", "", "Totals", "", _fmt_money(cpj_bank), _fmt_money(cpj_trading_stock), _fmt_money(cpj_creditors_control), "", _fmt_money(cpj_wages), _fmt_money(cpj_stationery), "", "", ""]

    journals: List[Dict[str, Any]] = [
        {"journal_type": "crj_totals_ledger", "table_variant": "grade_project", "headers": _crj_totals_headers_ledger(), "rows": [_build_prefixed_row(table_index=0, row_index=0, values=crj_values, editable_cols=[])], "column_help": {}, "allow_extra_rows": False},
        {"journal_type": "cpj_totals_ledger", "table_variant": "grade_project", "headers": _cpj_totals_headers_ledger(), "rows": [_build_prefixed_row(table_index=1, row_index=0, values=cpj_values, editable_cols=[])], "column_help": {}, "allow_extra_rows": False},
    ]

    gl_headers = _general_ledger_account_headers()
    if diff == "easy":
        editable_cols: List[int] = [4, 9] if r.random() < 0.7 else [2, 3, 4, 7, 8, 9]
    elif diff == "medium":
        editable_cols = [2, 3, 4, 7, 8, 9]
    else:
        editable_cols = list(range(len(gl_headers)))

    def _gl_header_rows(*, acct_name: str, folio: str) -> List[List[Dict[str, Any]]]:
        return [
            [{"label": f"General ledger of {business}", "colSpan": len(gl_headers)}],
            [{"label": "Dr.", "colSpan": 1}, {"label": acct_name, "colSpan": 8}, {"label": folio, "colSpan": 1}],
            [{"label": "Month"}, {"label": "Day"}, {"label": "Details"}, {"label": "Fol"}, {"label": "Amount"}, {"label": "Month"}, {"label": "Day"}, {"label": "Details"}, {"label": "Fol"}, {"label": "Amount"}],
        ]

    def _opening_for(acct: str) -> Tuple[float, float]:
        if acct.lower() in {"sales", "creditors control", "interest on overdue debtors", "creditors for wages"}:
            return 0.0, float(r.choice([0, 44400, 16200, 40720]))
        return float(r.choice([0, 500, 1240, 20600, 28300])), 0.0

    def _postings_for(acct: str) -> List[Tuple[str, str, str, float, str]]:
        account_norm = acct.lower()
        postings: List[Tuple[str, str, str, float, str]] = []
        if account_norm == "bank":
            postings.extend([("dr", "Total receipts", "CRJ", crj_bank, "30"), ("cr", "Total payments", "CPJ", cpj_bank, "30")])
        elif account_norm == "sales":
            postings.extend([("cr", "Bank", "CRJ", crj_sales, "30"), ("cr", "Debtors control", "DJ", dj_sales, "30")])
        elif account_norm == "cost of sales":
            postings.extend([("dr", "Trading stock", "CRJ", crj_cost_of_sales, "30"), ("dr", "Trading stock", "DJ", dj_cost_of_sales, "30"), ("dr", "Trading stock", "DAJ", daj_cost_of_sales, "30")])
        elif account_norm == "trading stock":
            postings.extend([("dr", "Bank", "CPJ", cpj_trading_stock, "30"), ("dr", "Creditors control", "CJ", cj_trading_stock, "30"), ("cr", "Cost of sales", "CRJ", crj_cost_of_sales, "30"), ("cr", "Cost of sales", "DJ", dj_cost_of_sales, "30"), ("cr", "Cost of sales", "DAJ", daj_cost_of_sales, "30"), ("cr", "Creditors control", "CAJ", caj_trading_stock, "30"), ("cr", "Drawings", "GJ", gj_drawings_stock, "30"), ("cr", "Donations", "GJ", gj_donation, "30")])
        elif account_norm == "debtors control":
            postings.extend([("dr", "Sales", "DJ", dj_sales, "30"), ("cr", "Bank", "CRJ", crj_debtors_control, "30"), ("cr", "Discount allowed", "CRJ", crj_discount_allowed, "30"), ("cr", "Debtors allowances", "DAJ", daj_allowances, "30"), ("cr", "Bad debts", "GJ", gj_bad_debts, "30"), ("dr", "Interest on overdue debtors", "GJ", gj_interest_overdue_debtors, "30")])
        elif account_norm == "creditors control":
            postings.extend([("dr", "Bank", "CPJ", cpj_creditors_control, "30"), ("cr", "Sundry purchases", "CJ", cj_creditors_control, "30"), ("dr", "Sundry allowances", "CAJ", caj_creditors_control, "30"), ("cr", "Creditors for wages", "GJ", gj_wages_accrued, "30")])
        elif account_norm == "stationery":
            postings.extend([("dr", "Bank", "CPJ", cpj_stationery, "30"), ("dr", "Creditors control", "CJ", cj_stationery, "30"), ("cr", "Creditors control", "CAJ", caj_stationery, "30"), ("cr", "Drawings", "GJ", gj_drawings_stationery, "30")])
        elif account_norm == "equipment":
            postings.extend([("dr", "Creditors control", "CJ", cj_equipment, "30"), ("cr", "Creditors control", "CAJ", caj_equipment, "30")])
        elif account_norm == "bad debts":
            postings.append(("dr", bad_debt_debtor, "GJ", gj_bad_debts, "30"))
        elif account_norm == "interest on overdue debtors":
            postings.append(("cr", interest_debtor, "GJ", gj_interest_overdue_debtors, "30"))
        elif account_norm == "wages":
            postings.extend([("dr", "Bank", "CPJ", cpj_wages, "30"), ("dr", "Creditors for wages", "GJ", gj_wages_accrued, "30")])
        elif account_norm == "creditors for wages":
            postings.append(("cr", "Wages", "GJ", gj_wages_accrued, "30"))
        elif account_norm == "donations":
            postings.append(("dr", "Trading stock", "GJ", gj_donation, "30"))
        elif account_norm == "drawings":
            postings.extend([("dr", "Trading stock", "GJ", gj_drawings_stock, "30"), ("dr", "Stationery", "GJ", gj_drawings_stationery, "30")])
        return [posting for posting in postings if posting[3] > 0]

    def _gl_account_table(*, table_index: int, acct: str, folio: str, opening_debit: float, opening_credit: float, postings: List[Tuple[str, str, str, float, str]]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, str], Dict[str, Dict[str, str]]]:
        rows: List[List[Dict[str, Any]]] = []
        correct: Dict[str, Any] = {}
        cell_hints: Dict[str, str] = {}
        cell_teaching_map: Dict[str, Dict[str, str]] = {}

        def _store_row(*, row_index: int, values: List[Optional[str]], row_role: str, transaction_line: str) -> None:
            row = _build_prefixed_row(table_index=table_index, row_index=row_index, values=values, editable_cols=editable_cols)
            rows.append(row)
            for cix, value in enumerate(values):
                if cix not in editable_cols:
                    continue
                key = f"t{table_index}_r{row_index}_c{cix}"
                expected = "" if value is None else str(value)
                correct[key] = expected
                if mode_norm == "scaffold" and expected:
                    if row_role == "posting" and cix in {2, 7}:
                        cell_hints[key] = f"Details usually show the contra account: the account on the other side of the {acct} entry."
                    elif row_role == "posting" and cix in {3, 8}:
                        cell_hints[key] = "Use the journal abbreviation or balance reference for the source of this entry."
                    elif cix in {4, 9}:
                        cell_hints[key] = f"Find the source line, decide which side of {acct} is affected, and then post the amount."
                    cell_teaching_map[key] = _build_gl_teaching_hint(header_label=gl_headers[cix], expected=expected, account_name=acct, transaction_line=transaction_line, row_role=row_role)

        row_index = 0
        opening_values: List[Optional[str]] = [month_short, "1", "Balance b/d", "b/d", _fmt_money(opening_debit) if opening_debit else "", month_short, "1", "Balance b/d", "b/d", _fmt_money(opening_credit) if opening_credit else ""]
        _store_row(row_index=row_index, values=opening_values, row_role="opening_balance", transaction_line=f"Opening balance for the {acct} account.")
        row_index += 1

        for side, details, fol_ref, amount, day in postings:
            values = [month_short, str(day), details, fol_ref, _fmt_money(amount), "", "", "", "", ""] if side == "dr" else ["", "", "", "", "", month_short, str(day), details, fol_ref, _fmt_money(amount)]
            _store_row(row_index=row_index, values=values, row_role="posting", transaction_line=f"Post {details} from {fol_ref} to the {acct} account.")
            row_index += 1

        debit_sum = opening_debit + sum(amount for side, _, __, amount, ___ in postings if side == "dr")
        credit_sum = opening_credit + sum(amount for side, _, __, amount, ___ in postings if side == "cr")
        difference = _round_money(debit_sum - credit_sum)
        balance = _round_money(abs(difference))

        if difference > 0:
            balance_values: List[Optional[str]] = ["", "", "", "", "", month_short, "30", "Balance c/d", "c/d", _fmt_money(balance)]
        elif difference < 0:
            balance_values = [month_short, "30", "Balance c/d", "c/d", _fmt_money(balance), "", "", "", "", ""]
        else:
            balance_values = ["", "", "", "", "", "", "", "", "", ""]
        _store_row(row_index=row_index, values=balance_values, row_role="balance_cd", transaction_line=f"Balance the {acct} account.")
        row_index += 1

        total = _fmt_money(max(debit_sum, credit_sum))
        totals_values: List[Optional[str]] = ["", "", "Totals", "", total, "", "", "Totals", "", total]
        _store_row(row_index=row_index, values=totals_values, row_role="totals", transaction_line=f"Totals for the {acct} account after balancing.")
        row_index += 1

        next_values: List[Optional[str]] = [next_month_short, "1", "Balance b/d", "b/d", _fmt_money(balance) if difference > 0 else "", next_month_short, "1", "Balance b/d", "b/d", _fmt_money(balance) if difference < 0 else ""]
        _store_row(row_index=row_index, values=next_values, row_role="balance_bd", transaction_line=f"Carry the closing balance of the {acct} account forward to the next month.")

        journal = {"journal_type": "general_ledger_account", "table_variant": "grade_project", "headers": gl_headers, "rows": rows, "header_rows": _gl_header_rows(acct_name=acct, folio=folio), "column_help": {}, "allow_extra_rows": False}
        return journal, correct, cell_hints, cell_teaching_map

    standard_accounts: List[Tuple[str, str]] = [("Bank", "B1"), ("Sales", "N1"), ("Cost of Sales", "N2"), ("Trading stock", "B6"), ("Debtors control", "B7"), ("Creditors control", "B9"), ("Stationery", "N8"), ("Wages", "N13")]
    advanced_accounts: List[Tuple[str, str]] = [("Bad debts", "N9"), ("Interest on overdue debtors", "N10"), ("Drawings", "N7"), ("Donations", "N6"), ("Creditors for wages", "B10")]
    chosen_accounts: List[Tuple[str, str]] = [r.choice(advanced_accounts)]
    while len(chosen_accounts) < int(r.choice([3, 4, 5])):
        candidate = r.choice(standard_accounts + advanced_accounts)
        if candidate not in chosen_accounts:
            chosen_accounts.append(candidate)

    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    for index, (account_name, folio) in enumerate(chosen_accounts):
        opening_debit, opening_credit = _opening_for(account_name)
        journal, correct, hints, teaching = _gl_account_table(table_index=2 + index, acct=account_name, folio=folio, opening_debit=opening_debit, opening_credit=opening_credit, postings=_postings_for(account_name))
        journals.append(journal)
        correct_map.update(correct)
        cell_hints.update(hints)
        cell_teaching_map.update(teaching)

    required_accounts = "\n".join(f"- {account_name}" for account_name, _ in chosen_accounts)
    prompt = (
        f"{business}\n"
        f"General Ledger for {month}\n\n"
        "Context:\n"
        "- A Cash Receipts Journal (CRJ) totals table is given as information.\n"
        "- A Cash Payments Journal (CPJ) totals table is given as information.\n"
        f"- DJ totals include Sales R{_fmt_money(dj_sales)} and Cost of sales R{_fmt_money(dj_cost_of_sales)}.\n"
        f"- DAJ totals include Debtors allowances R{_fmt_money(daj_allowances)} and Cost of sales reversal R{_fmt_money(daj_cost_of_sales)}.\n"
        f"- CJ totals include Creditors control R{_fmt_money(cj_creditors_control)}, Trading stock R{_fmt_money(cj_trading_stock)}, Equipment R{_fmt_money(cj_equipment)}, and Stationery R{_fmt_money(cj_stationery)}.\n"
        f"- CAJ totals include Creditors control R{_fmt_money(caj_creditors_control)}, Trading stock R{_fmt_money(caj_trading_stock)}, Equipment R{_fmt_money(caj_equipment)}, and Stationery R{_fmt_money(caj_stationery)}.\n"
        f"- GJ adjustments affecting ledger accounts include: bad debts for {bad_debt_debtor} R{_fmt_money(gj_bad_debts)}, interest on overdue debtor {interest_debtor} R{_fmt_money(gj_interest_overdue_debtors)}, drawings of stock R{_fmt_money(gj_drawings_stock)}, drawings of stationery R{_fmt_money(gj_drawings_stationery)}, donations of stock R{_fmt_money(gj_donation)}, and accrued wages R{_fmt_money(gj_wages_accrued)}.\n"
        f"- A separate source note for the month refers to debtor {distractor_debtor} and creditor {distractor_creditor} in other accounts.\n\n"
        "Required:\n"
        "Post the relevant journal totals and GJ adjustments to the following General Ledger accounts:\n"
        f"{required_accounts}\n"
        f"Balance each account on 30 {month}."
    )

    out = _make_journal(
        prompt=prompt,
        journal_type="general_ledger",
        headers=gl_headers,
        rows=journals[-1]["rows"],
        correct_map=correct_map,
        guidelines=[
            "Read the context one source at a time, identify the contra account, and then post to the correct side of the selected ledger account.",
            "In the Details column, write the contra account; in the Fol column, write the source journal or balance reference.",
            "Balance c/d is the balancing figure; Balance b/d is carried forward to the next month.",
            "Only post information that affects the accounts provided.",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
    )
    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    out["journals"] = journals
    out["journal"] = journals[-1]
    out["correct_map"] = correct_map
    out["cell_teaching_map"] = cell_teaching_map if cell_teaching_map else None
    return out
