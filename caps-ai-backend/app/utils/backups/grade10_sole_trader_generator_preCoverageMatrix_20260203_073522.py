from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from .sole_trader.core import fmt_money as _fmt_money
from .sole_trader.core import make_calc as _make_calc
from .sole_trader.core import make_id as _make_id
from .sole_trader.core import make_mcq as _make_mcq
from .sole_trader.core import make_typed as _make_typed
from .sole_trader.core import round_money as _round_money
from .sole_trader.column_help import headers_to_column_help as _headers_to_column_help
from .sole_trader.journal_table import build_journal_row as _build_journal_row
from .sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from .sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty
from .sole_trader.journal_question import make_journal as _make_journal

from .sole_trader.control_accounts import make_control_account_study_question as _st_make_control_account_study_question
from .sole_trader.control_accounts import make_control_account_study_table as _st_make_control_account_study_table
from .sole_trader.control_accounts import make_control_accounts_internal_control_typed as _st_make_control_accounts_internal_control_typed
from .sole_trader.control_accounts import make_control_accounts_reconciliation_question as _st_make_control_accounts_reconciliation_question
from .sole_trader.control_accounts import make_reconciliation_impact_matrix_question as _st_make_reconciliation_impact_matrix_question

from .sole_trader.trading_stock_account import make_trading_stock_account_table as _st_make_trading_stock_account_table
from .sole_trader.trading_stock_account import make_trading_stock_activity16_analysis_typed as _st_make_trading_stock_activity16_analysis_typed
from .sole_trader.trading_stock_account import make_trading_stock_section3_analysis_typed as _st_make_trading_stock_section3_analysis_typed
from .sole_trader.trading_stock_account import make_trading_stock_fill_missing_details_question as _st_make_trading_stock_fill_missing_details_question
from .sole_trader.trading_stock_account import make_trading_stock_prepare_from_casted_journals_question as _st_make_trading_stock_prepare_from_casted_journals_question
from .sole_trader.trading_stock_account import make_trading_stock_prepare_from_journals_question as _st_make_trading_stock_prepare_from_journals_question
from .sole_trader.trading_stock_account import make_trading_stock_prepare_with_discount_calc_question as _st_make_trading_stock_prepare_with_discount_calc_question
from .sole_trader.trading_stock_account import make_trading_stock_prepare_with_returns_percent_question as _st_make_trading_stock_prepare_with_returns_percent_question

from .sole_trader.trading_stock_account import (
    make_trading_stock_prepare_with_two_returns_percent_question as _st_make_trading_stock_prepare_with_two_returns_percent_question,
)
from .sole_trader.trading_stock_account import (
    make_trading_stock_markup_trade_discount_typed as _st_make_trading_stock_markup_trade_discount_typed,
)

from .sole_trader.pools import build_pools_by_subskill as _build_pools_by_subskill

from .sole_trader.journals.crj import make_crj_single_row_question as _st_make_crj_single_row_question
from .sole_trader.journals.crj import make_crj_activity5_question as _st_make_crj_activity5_question
from .sole_trader.journals.crj import make_crj_exam_style_question as _st_make_crj_exam_style_question
from .sole_trader.journals.cpj import make_cpj_single_row_question as _st_make_cpj_single_row_question
from .sole_trader.journals.cpj import make_cpj_activity5_question as _st_make_cpj_activity5_question
from .sole_trader.journals.cpj import make_cpj_exam_style_question as _st_make_cpj_exam_style_question
from .sole_trader.journals.dj import make_dj_activity_question as _st_make_dj_activity_question
from .sole_trader.journals.dj import make_dj_exam_style_question as _st_make_dj_exam_style_question
from .sole_trader.journals.dj import make_dj_single_row_question as _st_make_dj_single_row_question
from .sole_trader.journals.daj import make_daj_activity_question as _st_make_daj_activity_question
from .sole_trader.journals.daj import make_daj_exam_style_question as _st_make_daj_exam_style_question
from .sole_trader.journals.daj import make_daj_single_row_question as _st_make_daj_single_row_question
from .sole_trader.journals.cj import make_cj_activity_question as _st_make_cj_activity_question
from .sole_trader.journals.cj import make_cj_exam_style_question as _st_make_cj_exam_style_question
from .sole_trader.journals.cj import make_cj_single_row_question as _st_make_cj_single_row_question
from .sole_trader.journals.caj import make_caj_activity_question as _st_make_caj_activity_question
from .sole_trader.journals.caj import make_caj_exam_style_question as _st_make_caj_exam_style_question
from .sole_trader.journals.caj import make_caj_single_row_question as _st_make_caj_single_row_question
from .sole_trader.journals.pcj import make_pcj_single_row_question as _st_make_pcj_single_row_question
from .sole_trader.journals.pcj import make_pcj_activity11_question as _st_make_pcj_activity11_question
from .sole_trader.journals.pcj import make_pcj_exam_style_question as _st_make_pcj_exam_style_question
from .sole_trader.journals.gj import make_gj_single_row_question as _st_make_gj_single_row_question
from .sole_trader.journals.gj import make_gj_activity13_question as _st_make_gj_activity13_question
from .sole_trader.journals.gj import make_gj_exam_style_question as _st_make_gj_exam_style_question

from .sole_trader.full_accounting_cycle_project import (
    make_full_accounting_cycle_project_question as _st_make_full_accounting_cycle_project_question,
)

BUSINESS_NAMES: List[str] = [
    "Khumalo Traders",
    "Mokoena Stores",
    "Dlamini Spares",
    "Mashoke Traders",
    "Lucia Traders",
    "Sunshine Traders",
    "Lonely Traders",
    "Khumalo Traders",
    "Mokoena Stores",
]

PERSON_NAMES: List[str] = [
    "A. Khumalo",
    "B. Maseko",
    "C. Naidoo",
    "D. Botha",
    "E. Nkosi",
    "F. Pillay",
    "D. Botha",
    "L. Uys",
    "G. Coetzee",
    "J. van der Linde",
    "B. de Villiers",
    "W. van Jaarsveldt",
    "G. Haasbroek",
]

SUPPLIER_NAMES: List[str] = [
    "Ducasse Traders",
    "Lund Stores",
    "Lind Traders",
    "AB Motors",
    "Marais Traders",
    "PE Traders",
    "Together Stores",
    "Lindiwe Traders",
    "Number One Motors",
    "Frans Distributors",
]


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


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


def _ta_headers_activity23() -> List[str]:
    return [
        "Nr",
        "Source document",
        "Account debited",
        "Account credited",
        "A",
        "OE",
        "L",
    ]


def _ta_headers_activity24() -> List[str]:
    return [
        "Nr",
        "Source document",
        "Account debited",
        "Account credited",
        "Amount",
        "A",
        "O",
        "L",
    ]


def _make_transaction_analysis_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    mode_norm = str(mode or "").strip().lower()
    diff = str(difficulty or "easy").strip().lower()
    show_answers = mode_norm == "scaffold"

    business = r.choice(BUSINESS_NAMES)
    debtor = r.choice(PERSON_NAMES)
    creditor = r.choice(SUPPLIER_NAMES)
    markup_pct = float(r.choice([25.0, 40.0, 50.0, 60.0, 65.0, 70.0, 75.0, 80.0, 150.0]))
    selling_factor = 1.0 + (markup_pct / 100.0)

    def _fmt_sign(v: float) -> str:
        if abs(v) < 1e-9:
            return "0"
        return "+" if v > 0 else "-"

    def _fmt_amount(v: float, *, prefer_pm: bool = False) -> str:
        amt = _fmt_money(abs(v))
        if prefer_pm:
            return f"±{amt}"
        return ("+" if v > 0 else "-") + amt

    def _effects_to_signs(a: float, o: float, l: float) -> Tuple[str, str, str]:
        return (_fmt_sign(a), _fmt_sign(o), _fmt_sign(l))

    def _effects_to_signed_amounts(a: float, o: float, l: float) -> Tuple[str, str, str]:
        return (_fmt_amount(a, prefer_pm=abs(a) > 0), _fmt_amount(o, prefer_pm=abs(o) > 0), _fmt_amount(l, prefer_pm=abs(l) > 0))

    tx_counter = 1

    def _tx(
        *,
        nr: str,
        source: str = "",
        journal: str = "",
        internal: str = "",
        dr: str,
        cr: str,
        amount: Optional[float],
        a: float,
        o: float,
        l: float,
    ) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "nr": nr,
            "source": source,
            "journal": journal,
            "internal": internal,
            "dr": dr,
            "cr": cr,
            "amount": amount,
            "a": a,
            "o": o,
            "l": l,
        }
        return out

    def _make_cash_sales_cost(*, cost: float, nr: str, source: str = "Cash register roll", journal: str = "") -> List[Dict[str, Any]]:
        sales = _round_money(cost * selling_factor)
        return [
            _tx(nr=nr, source=source, journal=journal, dr="Bank", cr="Sales", amount=float(sales), a=+sales, o=+sales, l=0.0),
            _tx(nr="", source="", journal="", dr="Cost of sales", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0),
        ]

    def _make_credit_sales_cost(*, cost: float, nr: str, source: str = "Duplicate invoice", journal: str = "") -> List[Dict[str, Any]]:
        sales = _round_money(cost * selling_factor)
        return [
            _tx(nr=nr, source=source, journal=journal, dr="Debtors control", cr="Sales", amount=float(sales), a=+sales, o=+sales, l=0.0),
            _tx(nr="", source="", journal="", dr="Cost of sales", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0),
        ]

    def _make_debtor_settlement_discount(*, owed: float, disc_pct: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        disc = _round_money(owed * (disc_pct / 100.0))
        bank_amt = _round_money(owed - disc)
        return [
            _tx(nr=nr, source=source, journal=journal, dr="Bank", cr="Debtors control", amount=float(bank_amt), a=+bank_amt, o=0.0, l=0.0),
            _tx(nr="", source="", journal="", dr="Discount allowed", cr="Debtors control", amount=float(disc), a=-disc, o=-disc, l=0.0),
        ]

    def _make_rd_cheque_cancel_discount(*, bank_amt: float, disc: float, nr: str, source: str = "Bank statement") -> List[Dict[str, Any]]:
        return [
            _tx(nr=nr, source=source, journal="", dr="Debtors control", cr="Bank", amount=float(bank_amt), a=0.0, o=0.0, l=0.0),
            _tx(nr="", source="Journal voucher", journal="", dr="Debtors control", cr="Discount allowed", amount=float(disc), a=+disc, o=+disc, l=0.0),
        ]

    def _make_creditor_payment_discount_received(*, owed: float, disc_pct: float, nr: str, source: str = "Cheque counterfoil", journal: str = "") -> List[Dict[str, Any]]:
        disc = _round_money(owed * (disc_pct / 100.0))
        bank_amt = _round_money(owed - disc)
        return [
            _tx(nr=nr, source=source, journal=journal, dr="Creditors control", cr="Bank", amount=float(bank_amt), a=-bank_amt, o=0.0, l=-bank_amt),
            _tx(nr="", source="", journal="", dr="Creditors control", cr="Discount received", amount=float(disc), a=0.0, o=+disc, l=-disc),
        ]

    def _make_purchase_on_credit_trade_discount(*, gross: float, td_pct: float, nr: str, source: str = "Original invoice", journal: str = "") -> List[Dict[str, Any]]:
        net = _round_money(gross * (1.0 - (td_pct / 100.0)))
        return [_tx(nr=nr, source=source, journal=journal, dr="Trading stock", cr="Creditors control", amount=float(net), a=+net, o=0.0, l=+net)]

    def _make_purchase_by_cheque_trade_discount(*, gross: float, td_pct: float, nr: str, source: str = "Cheque counterfoil", journal: str = "") -> List[Dict[str, Any]]:
        net = _round_money(gross * (1.0 - (td_pct / 100.0)))
        return [_tx(nr=nr, source=source, journal=journal, dr="Trading stock", cr="Bank", amount=float(net), a=0.0, o=0.0, l=0.0)]

    def _make_expense_paid(*, account: str, amt: float, nr: str, source: str, credit_account: str = "Bank", journal: str = "") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal=journal, dr=account, cr=credit_account, amount=float(amt), a=-amt if credit_account.lower() in {"bank", "petty cash"} else 0.0, o=-amt, l=0.0)]

    def _make_bank_charges(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source="Bank statement", journal="", dr="Bank charges", cr="Bank", amount=float(amt), a=0.0, o=-amt, l=+amt)]

    def _make_interest_income(*, amt: float, nr: str, source: str = "Bank statement") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal="", dr="Bank", cr="Interest income", amount=float(amt), a=+amt, o=+amt, l=0.0)]

    def _make_rent_received(*, amt: float, nr: str, source: str = "Duplicate receipt") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal="", dr="Bank", cr="Rent income", amount=float(amt), a=+amt, o=+amt, l=0.0)]

    def _make_loan_received(*, amt: float, nr: str, source: str = "Bank statement") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal="", dr="Bank", cr=f"Loan", amount=float(amt), a=+amt, o=0.0, l=+amt)]

    def _make_loan_repayment_with_interest(*, repayment: float, rate_pct: float, months: int, nr: str, source: str = "EFT") -> List[Dict[str, Any]]:
        interest = _round_money(repayment * (rate_pct / 100.0) * (months / 12.0))
        capital = _round_money(repayment - interest)
        return [
            _tx(nr=nr, source=source, journal="", dr="Loan", cr="Bank", amount=float(capital), a=0.0, o=0.0, l=-capital),
            _tx(nr="", source="", journal="", dr="Interest on loan", cr="Bank", amount=float(interest), a=-interest, o=-interest, l=0.0),
        ]

    def _make_capital_contribution(*, amt: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal=journal, dr="Bank", cr="Capital", amount=float(amt), a=+amt, o=+amt, l=0.0)]

    def _make_drawings_stock_cost(*, cost: float, nr: str, source: str = "Journal voucher", journal: str = "") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal=journal, dr="Drawings", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0)]

    def _make_bad_debt_writeoff(*, amt: float, nr: str, source: str = "Journal voucher", journal: str = "") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal=journal, dr="Bad debts", cr="Debtors control", amount=float(amt), a=-amt, o=-amt, l=0.0)]

    def _make_bad_debt_recovered(*, amt: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source=source, journal=journal, dr="Bank", cr="Bad debts recovered", amount=float(amt), a=+amt, o=+amt, l=0.0)]

    def _make_debtor_allowance_return(*, selling_price: float, cost_price: float, nr: str, source: str = "Duplicate credit note", journal: str = "") -> List[Dict[str, Any]]:
        return [
            _tx(nr=nr, source=source, journal=journal, dr="Debtors allowances", cr="Debtors control", amount=float(selling_price), a=-selling_price, o=-selling_price, l=0.0),
            _tx(nr="", source="", journal="", dr="Trading stock", cr="Cost of sales", amount=float(cost_price), a=+cost_price, o=+cost_price, l=0.0),
        ]

    def _make_creditor_allowance_return(*, cost_price: float, td_pct: float, nr: str, source: str = "Duplicate debit note", journal: str = "") -> List[Dict[str, Any]]:
        net = _round_money(cost_price * (1.0 - (td_pct / 100.0)))
        return [_tx(nr=nr, source=source, journal=journal, dr="Creditors control", cr="Trading stock", amount=float(net), a=0.0, o=0.0, l=-net)]

    def _make_interest_on_overdue(*, principal: float, rate_pct: float, months: int, nr: str, kind: str) -> List[Dict[str, Any]]:
        interest = _round_money(principal * (rate_pct / 100.0) * (months / 12.0))
        if kind == "debtor":
            return [_tx(nr=nr, source="Journal voucher", journal="", dr="Debtors control", cr="Interest income", amount=float(interest), a=+interest, o=+interest, l=0.0)]
        return [_tx(nr=nr, source="Journal voucher", journal="", dr="Interest expense", cr="Creditors control", amount=float(interest), a=0.0, o=-interest, l=+interest)]

    def _make_insurance_accrued(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        return [_tx(nr=nr, source="Journal voucher", journal="", dr="Insurance", cr="Accrued expense", amount=float(amt), a=0.0, o=-amt, l=+amt)]

    def _make_insolvent_debtor_dividend_writeoff(
        *,
        owed: float,
        cents_in_rand: float,
        nr: str,
        source: str = "Bank statement",
    ) -> List[Dict[str, Any]]:
        dividend = float(_round_money(owed * (cents_in_rand / 100.0)))
        writeoff = float(_round_money(owed - dividend))
        row1 = _tx(nr=nr, source=source, journal="", dr="Bank", cr="Debtors control", amount=dividend, a=+dividend, o=0.0, l=0.0)
        row1["tag"] = "insolvency_dividend"
        row1["owed"] = float(owed)
        row1["cents_in_rand"] = float(cents_in_rand)
        row2 = _tx(nr="", source="Journal voucher", journal="", dr="Bad debts", cr="Debtors control", amount=writeoff, a=-writeoff, o=-writeoff, l=0.0)
        row2["tag"] = "insolvency_writeoff"
        row2["owed"] = float(owed)
        row2["cents_in_rand"] = float(cents_in_rand)
        return [row1, row2]

    def _make_petty_cash_on_behalf_of_debtor(*, amt: float, nr: str, debtor_name: str) -> List[Dict[str, Any]]:
        # This transaction has no net effect on the accounting equation (asset swaps), but some
        # archetypes show both effects in one cell as +amt/-amt.
        row1 = _tx(nr=nr, source="Petty cash voucher", journal="", dr="Debtors control", cr="Petty cash", amount=float(amt), a=0.0, o=0.0, l=0.0)
        row1["tag"] = "petty_cash_on_behalf_debtor"
        row1["debtor_name"] = str(debtor_name)
        row1["a_override"] = f"+{_fmt_money(float(amt))}/-{_fmt_money(float(amt))}"
        return [row1]

    def _make_fee_income_on_credit(*, amt: float, nr: str, source: str = "") -> List[Dict[str, Any]]:
        row1 = _tx(nr=nr, source=source, journal="", dr="Debtors control", cr="Fee income", amount=float(amt), a=+float(amt), o=+float(amt), l=0.0)
        row1["tag"] = "fee_income_credit"
        return [row1]

    def _make_fixed_deposit_maturity(*, principal: float, rate_pct: float, months: int, nr: str) -> List[Dict[str, Any]]:
        interest = float(_round_money(principal * (rate_pct / 100.0) * (months / 12.0)))
        row1 = _tx(nr=nr, source="Bank statement", journal="", dr="Bank", cr="Fixed deposit", amount=float(principal), a=0.0, o=0.0, l=0.0)
        row1["tag"] = "fd_maturity_principal"
        row2 = _tx(nr="", source="", journal="", dr="Bank", cr="Interest on fixed deposit", amount=float(interest), a=+interest, o=+interest, l=0.0)
        row2["tag"] = "fd_maturity_interest"
        return [row1, row2]

    def _make_bank_fee_breakdown(*, service_fee: float, cash_handling_fee: float, overdraft_int: float, nr: str) -> List[Dict[str, Any]]:
        # Bank statement shows multiple fees and interest - each is a separate expense affecting bank
        row1 = _tx(nr=nr, source="Bank statement", journal="", dr="Bank charges", cr="Bank", amount=float(service_fee), a=0.0, o=-service_fee, l=+service_fee)
        row1["tag"] = "bank_fee_service"
        row2 = _tx(nr="", source="", journal="", dr="Bank charges", cr="Bank", amount=float(cash_handling_fee), a=0.0, o=-cash_handling_fee, l=+cash_handling_fee)
        row2["tag"] = "bank_fee_cash"
        row3 = _tx(nr="", source="", journal="", dr="Interest expense", cr="Bank", amount=float(overdraft_int), a=0.0, o=-overdraft_int, l=+overdraft_int)
        row3["tag"] = "bank_fee_overdraft_int"
        return [row1, row2, row3]

    def _pick_amount(base: List[float]) -> float:
        return float(r.choice(base))

    def _build_tx_pool() -> List[Tuple[str, List[Dict[str, Any]]]]:
        nonlocal tx_counter
        out: List[Tuple[str, List[Dict[str, Any]]]] = []
        nr = str(tx_counter)
        out.append(("cash_sales_cost", _make_cash_sales_cost(cost=_pick_amount([900, 1200, 1800, 2000, 3000, 4800, 8600]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("credit_sales_cost", _make_credit_sales_cost(cost=_pick_amount([500, 700, 1500, 2100, 2500, 4000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        owed = _pick_amount([850, 1100, 1950, 3000, 3500, 5000, 7200])
        disc_pct = float(r.choice([2.5, 4.0, 5.0, 10.0]))
        out.append(("debtor_settlement_discount", _make_debtor_settlement_discount(owed=owed, disc_pct=disc_pct, nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("creditor_payment_discount_received", _make_creditor_payment_discount_received(owed=_pick_amount([3000, 5000, 645, 8500, 13500]), disc_pct=float(r.choice([4.0, 5.0, 10.0])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("purchase_credit_trade_discount", _make_purchase_on_credit_trade_discount(gross=_pick_amount([10800, 14000, 3500, 5670]), td_pct=float(r.choice([8.0, 10.0, 15.0, 20.0])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("purchase_cheque_trade_discount", _make_purchase_by_cheque_trade_discount(gross=_pick_amount([12300, 10000, 6000]), td_pct=float(r.choice([10.0, 15.0, 20.0])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("bank_charges", _make_bank_charges(amt=_pick_amount([210, 270, 340, 550, 610]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("interest_income", _make_interest_income(amt=_pick_amount([110, 130, 520, 800, 1000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("rent_received", _make_rent_received(amt=_pick_amount([4680, 5000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("loan_received", _make_loan_received(amt=_pick_amount([30000, 50000, 220000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("loan_repayment_interest", _make_loan_repayment_with_interest(repayment=_pick_amount([44000, 30000]), rate_pct=float(r.choice([10.0, 15.0, 18.0])), months=int(r.choice([4, 12])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("capital_contribution", _make_capital_contribution(amt=_pick_amount([20000, 40000, 100000, 120000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("drawings_stock", _make_drawings_stock_cost(cost=_pick_amount([300, 400, 850, 1350, 7600, 15000]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("bad_debt_writeoff", _make_bad_debt_writeoff(amt=_pick_amount([550, 750, 880, 2160, 2600]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("bad_debt_recovered", _make_bad_debt_recovered(amt=_pick_amount([150, 400, 540, 1800]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("interest_overdue_debtor", _make_interest_on_overdue(principal=_pick_amount([4800, 3000, 900]), rate_pct=float(r.choice([2.5, 10.0, 12.0])), months=int(r.choice([1, 2, 3, 4])), nr=nr, kind="debtor")))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("interest_overdue_creditor", _make_interest_on_overdue(principal=_pick_amount([3600, 8400]), rate_pct=float(r.choice([6.0, 7.0, 18.0])), months=int(r.choice([2, 3, 4])), nr=nr, kind="creditor")))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("insurance_accrued", _make_insurance_accrued(amt=_pick_amount([900]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("insolvent_debtor_dividend_writeoff", _make_insolvent_debtor_dividend_writeoff(owed=_pick_amount([4000, 5200, 6000, 8000, 10000]), cents_in_rand=float(r.choice([25.0, 30.0, 35.0, 40.0, 50.0])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("fee_income_credit", _make_fee_income_on_credit(amt=_pick_amount([250, 350, 420, 560, 900, 1200]), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        owed_unfav = float(_pick_amount([2800, 3500, 5000]))
        disc_unfav = float(r.choice([2.0, 5.0, 10.0]))
        out.append(("debtor_settlement_discount_unfavourable", _make_debtor_settlement_discount_unfavourable_bank(owed=owed_unfav, disc_pct=disc_unfav, nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("overdraft_interest", _make_overdraft_interest(amt=float(_pick_amount([66, 200, 350, 700])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("fixed_deposit_maturity", _make_fixed_deposit_maturity(principal=float(_pick_amount([5000, 10000, 20000])), rate_pct=float(r.choice([6.0, 8.0, 10.0])), months=int(r.choice([6, 12])), nr=nr)))
        tx_counter += 1
        nr = str(tx_counter)
        out.append(("bank_fee_breakdown", _make_bank_fee_breakdown(service_fee=float(_pick_amount([100, 150, 200])), cash_handling_fee=float(_pick_amount([50, 75, 100])), overdraft_int=float(_pick_amount([80, 120, 200])), nr=nr)))
        tx_counter += 1
        return out

    def _schema_headers(schema: str) -> List[str]:
        if schema == "activity23":
            return _ta_headers_activity23()
        if schema == "activity24":
            return _ta_headers_activity24()
        if schema == "gl_amount_aol":
            return ["No.", "Account debited", "Account credited", "Amount", "A", "O", "L"]
        if schema == "gl_aol":
            return ["No.", "Account debited", "Account credited", "A", "O", "L"]
        if schema == "source_gl_amount_aol":
            return ["No.", "Source document", "Account debited", "Account credited", "Amount", "A", "O", "L"]
        if schema == "journal_gl_amount_aol":
            return ["No.", "Subsidiary Journal", "Account debited", "Account credited", "Amount", "A", "O", "L"]
        if schema == "gl_subledger_amount_aol":
            return ["No.", "GL Dr", "GL Cr", "Subsidiary Dr", "Subsidiary Cr", "Amount", "A", "O", "L"]
        if schema == "internal_gl_amount_aol":
            return ["No.", "Internal Document", "Account debited", "Account credited", "Amount", "Assets", "Equity", "Liabilities"]
        if schema == "reason_effect":
            return ["No.", "Assets (Reason)", "Assets (Effect)", "Owner's Equity (Reason)", "Owner's Equity (Effect)", "Liabilities (Reason)", "Liabilities (Effect)"]
        return _ta_headers_activity24()

    def _schema_to_row(schema: str, t: Dict[str, Any]) -> List[Optional[str]]:
        nr = str(t.get("nr") or "")
        source = str(t.get("source") or "")
        jrnl = str(t.get("journal") or "")
        internal = str(t.get("internal") or "")
        dr = str(t.get("dr") or "")
        cr = str(t.get("cr") or "")
        sub_dr = str(t.get("sub_dr") or "")
        sub_cr = str(t.get("sub_cr") or "")
        amt = t.get("amount")
        a = float(t.get("a") or 0.0)
        o0 = float(t.get("o") or 0.0)
        l0 = float(t.get("l") or 0.0)

        a_s, o_s, l_s = _effects_to_signs(a, o0, l0)
        a_amt, o_amt, l_amt = _effects_to_signed_amounts(a, o0, l0)

        # Optional display overrides for special archetypes where multiple values are shown in one cell.
        a_override = t.get("a_override")
        o_override = t.get("o_override")
        l_override = t.get("l_override")
        if a_override is not None:
            a_s = str(a_override)
            a_amt = str(a_override)
        if o_override is not None:
            o_s = str(o_override)
            o_amt = str(o_override)
        if l_override is not None:
            l_s = str(l_override)
            l_amt = str(l_override)

        # For reason/effect schemas, provide a "reason" account name based on which side changes.
        # This is intentionally simple but consistent with debit/credit behavior:
        # - Asset increase usually debits an asset account; decrease usually credits it.
        # - Equity increase usually credits an income/capital account; decrease usually debits an expense/drawings account.
        # - Liability increase usually credits a liability; decrease usually debits it.
        assets_reason = ""
        if abs(a) > 1e-9:
            assets_reason = dr if a > 0 else cr
        equity_reason = ""
        if abs(o0) > 1e-9:
            equity_reason = cr if o0 > 0 else dr
        liabilities_reason = ""
        if abs(l0) > 1e-9:
            liabilities_reason = cr if l0 > 0 else dr
        if schema == "activity23":
            return [nr, source, dr, cr, a_amt, o_amt, l_amt]
        if schema == "activity24":
            return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
        if schema == "gl_amount_aol":
            return [nr, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
        if schema == "gl_aol":
            return [nr, dr, cr, a_amt, o_amt, l_amt]
        if schema == "source_gl_amount_aol":
            return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
        if schema == "journal_gl_amount_aol":
            return [nr, jrnl, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
        if schema == "gl_subledger_amount_aol":
            return [nr, dr, cr, sub_dr, sub_cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
        if schema == "internal_gl_amount_aol":
            return [nr, internal or source, dr, cr, "" if amt is None else _fmt_money(amt), a_amt, o_amt, l_amt]
        if schema == "reason_effect":
            return [nr, assets_reason, a_s, equity_reason, o_s, liabilities_reason, l_s]
        return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]

    # ---- Approach 2 + hybrid mixing with compatibility rules (A) ----
    # Pick a schema for this question, then sample transactions from multiple archetype sets
    # that are compatible with that schema.
    schema = str(
        r.choice(
            [
                "activity23",
                "activity24",
                "gl_amount_aol",
                "gl_aol",
                "source_gl_amount_aol",
                "journal_gl_amount_aol",
                "gl_subledger_amount_aol",
                "internal_gl_amount_aol",
                "reason_effect",
            ]
        )
    )

    schema_requires_source = schema in {"activity23", "activity24", "source_gl_amount_aol"}
    schema_requires_journal = schema in {"journal_gl_amount_aol"}
    schema_requires_internal = schema in {"internal_gl_amount_aol"}
    schema_requires_subledger = schema in {"gl_subledger_amount_aol"}
    schema_has_amount = schema in {"activity24", "gl_amount_aol", "source_gl_amount_aol", "journal_gl_amount_aol", "internal_gl_amount_aol"}
    if schema == "gl_subledger_amount_aol":
        schema_has_amount = True

    headers = _schema_headers(schema)
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=list(range(len(headers))),
        total_cols=len(headers),
        mode=mode_norm,
    )

    guidelines = [
        "Use + for an increase, - for a decrease and 0 for no change.",
        "Some transactions require two entries (e.g. Sales and Cost of sales, discounts, R/D).",
        "Assume Bank is favourable unless stated otherwise.",
    ]

    if schema == "activity23":
        prompt = (
            f"{business}\n\n"
            "Required:\n"
            "Analyse the following transactions under the headings provided. Indicate the General Ledger accounts debited/credited and the effect on the accounting equation.\n"
            "Use + for an increase, - for a decrease and 0 for no change. Assume that the bank has a favourable bank balance."
        )
    elif schema == "activity24":
        prompt = (
            f"{business}\n\n"
            "Required:\n"
            "Analyse the following transactions under the headings provided. Indicate the General Ledger accounts debited/credited and the effect on the accounting equation.\n"
            "Use + for an increase, - for a decrease and 0 for no change. Assume that the bank has a favourable bank balance.\n\n"
            f"Note: The business mark-up is {int(markup_pct)}% on cost where applicable."
        )
    else:
        prompt = (
            f"{business}\n\n"
            "Required:\n"
            "Analyse the transactions according to the format provided.\n"
            "Use + for an increase, - for a decrease and 0 for no change.\n\n"
            f"Note: Mark-up on cost is {int(markup_pct)}% where applicable. Debtor: {debtor}. Creditor: {creditor}."
        )

    def _has_source(rows0: List[Dict[str, Any]]) -> bool:
        return any(str(t.get("source") or "").strip() for t in rows0)

    def _has_journal(rows0: List[Dict[str, Any]]) -> bool:
        return any(str(t.get("journal") or "").strip() for t in rows0)

    def _has_internal(rows0: List[Dict[str, Any]]) -> bool:
        return any(str(t.get("internal") or "").strip() for t in rows0)

    def _has_subledger(rows0: List[Dict[str, Any]]) -> bool:
        return any(str(t.get("sub_dr") or "").strip() or str(t.get("sub_cr") or "").strip() for t in rows0)

    def _has_amount(rows0: List[Dict[str, Any]]) -> bool:
        return any(t.get("amount") is not None for t in rows0)

    def _compatible(rows0: List[Dict[str, Any]]) -> bool:
        if schema_requires_source and not _has_source(rows0):
            return False
        if schema_requires_journal and not _has_journal(rows0):
            return False
        if schema_requires_internal and not _has_internal(rows0):
            return False
        if schema_requires_subledger and not _has_subledger(rows0):
            return False
        if schema_has_amount and not _has_amount(rows0):
            return False
        return True

    # Archetype set keys used for mixing; this is used for sampling diversity.
    all_archetype_keys = ["activity23", "activity24"] + [f"arch_{i}" for i in range(1, 26)]

    # Build a template bank with explicit journal/source usage so journal/source schemas work.
    tx_counter = 1
    template_bank: List[Tuple[str, str, List[Dict[str, Any]]]] = []

    def _add_template(archetype_key: str, name: str, rows0: List[Dict[str, Any]]) -> None:
        template_bank.append((archetype_key, name, rows0))

    # Activity 23/24-ish patterns (plus also used across many archetype sets)
    # Cash sales (CRJ) + COS
    _add_template("activity23", "cash_sales_crj", _make_cash_sales_cost(cost=_pick_amount([1200, 2000, 3000, 4800, 8600]), nr="1", source="Cash register roll", journal="CRJ"))
    _add_template("activity24", "cash_sales_crj", _make_cash_sales_cost(cost=_pick_amount([1200, 1800, 3000]), nr="1", source="Cash register roll", journal="CRJ"))

    # Credit sales (DJ) + COS
    _add_template("arch_10", "credit_sales_dj", _make_credit_sales_cost(cost=_pick_amount([500, 700, 1500, 2100, 2500]), nr="2", source="Duplicate invoice", journal="DJ"))
    _add_template("arch_16", "credit_sales_dj", _make_credit_sales_cost(cost=_pick_amount([500, 700, 1500, 2100]), nr="2", source="Duplicate invoice", journal="DJ"))

    # Debtor settlement with discount allowed (CRJ)
    owed0 = _pick_amount([850, 1100, 1950, 3000, 3500, 5000, 7200])
    disc_pct0 = float(r.choice([2.5, 4.0, 5.0, 10.0]))
    _add_template("activity23", "debtor_settlement_crj", _make_debtor_settlement_discount(owed=owed0, disc_pct=disc_pct0, nr="3", source="Duplicate receipt", journal="CRJ"))
    _add_template("arch_17", "debtor_settlement_crj", _make_debtor_settlement_discount(owed=owed0, disc_pct=disc_pct0, nr="3", source="Duplicate receipt", journal="CRJ"))

    # Creditor payment less discount received (CPJ)
    owed1 = _pick_amount([3000, 5000, 645, 8500, 13500])
    disc_pct1 = float(r.choice([4.0, 5.0, 10.0]))
    _add_template(
        "arch_20",
        "creditor_payment_cpj",
        _make_creditor_payment_discount_received(
            owed=owed1,
            disc_pct=disc_pct1,
            nr="4",
            source="Cheque counterfoil",
            journal="CPJ",
        ),
    )

    # Bank charges (CPJ)
    charges_amt = float(_pick_amount([210, 270, 340, 550, 610]))
    _add_template(
        "arch_6",
        "bank_charges_cpj",
        [
            _tx(
                nr="6",
                source="Bank statement",
                journal="CPJ",
                dr="Bank charges",
                cr="Bank",
                amount=charges_amt,
                a=0.0,
                o=-charges_amt,
                l=+charges_amt,
            )
        ],
    )

    # Interest income (CRJ)
    _add_template("arch_6", "interest_income_crj", _make_interest_income(amt=_pick_amount([110, 130, 520, 800, 1000]), nr="7", source="Bank statement"))
    # Rent received (CRJ)
    _add_template("arch_5", "rent_received_crj", _make_rent_received(amt=_pick_amount([4680, 5000]), nr="8", source="Duplicate receipt"))

    # Fee/service income on credit
    fee_amt = float(_pick_amount([250, 350, 420, 560, 900, 1200]))
    _add_template("arch_10", "fee_income_credit", _make_fee_income_on_credit(amt=fee_amt, nr="8a", source=""))
    _add_template("arch_11", "fee_income_credit", _make_fee_income_on_credit(amt=fee_amt, nr="8a", source=""))

    # Loan received (CRJ)
    _add_template("arch_1", "loan_received_crj", _make_loan_received(amt=_pick_amount([30000, 50000, 220000]), nr="9", source="Bank statement"))

    # Insurance accrued (GJ)
    _add_template("arch_17", "insurance_accrued_gj", [_tx(nr="10", source="Journal voucher", journal="GJ", dr="Insurance", cr="Accrued expense", amount=float(900), a=0.0, o=-900.0, l=+900.0)])

    # Interest on overdue debtor (GJ)
    _add_template("arch_9", "interest_overdue_debtor_gj", _make_interest_on_overdue(principal=_pick_amount([4800, 3000, 900]), rate_pct=float(r.choice([2.5, 10.0, 12.0])), months=int(r.choice([1, 2, 3, 4])), nr="11", kind="debtor"))

    # Bad debt write-off (GJ)
    _add_template("arch_25", "bad_debt_writeoff_gj", _make_bad_debt_writeoff(amt=_pick_amount([550, 750, 880, 2160, 2600]), nr="12", source="Journal voucher", journal="GJ"))
    # Bad debt recovered (CRJ)
    _add_template("arch_3", "bad_debt_recovered_crj", _make_bad_debt_recovered(amt=_pick_amount([150, 400, 540, 1800]), nr="13", source="Duplicate receipt", journal="CRJ"))
    # Drawings of stock (GJ)
    _add_template("arch_22", "drawings_stock_gj", _make_drawings_stock_cost(cost=_pick_amount([300, 400, 850, 1350, 7600, 15000]), nr="14", source="Journal voucher", journal="GJ"))

    # Petty cash paid on behalf of a debtor (multi-value in Assets cell)
    petty_on_behalf_amt = float(_pick_amount([210, 300, 450, 560, 700]))
    _add_template("arch_2", "petty_cash_on_behalf_debtor", _make_petty_cash_on_behalf_of_debtor(amt=petty_on_behalf_amt, nr="14b", debtor_name=debtor))

    # Capital contribution (CRJ)
    _add_template("arch_8", "capital_contribution_crj", _make_capital_contribution(amt=_pick_amount([20000, 40000, 100000, 120000]), nr="15", source="Duplicate receipt", journal="CRJ"))

    disc_amt0 = float(_round_money(owed0 * (disc_pct0 / 100.0)))
    bank_amt0 = float(_round_money(owed0 - disc_amt0))
    _add_template(
        "arch_12",
        "rd_cheque_gj",
        [
            _tx(nr="16", source="Bank statement", journal="GJ", dr="Debtors control", cr="Bank", amount=float(bank_amt0), a=0.0, o=0.0, l=0.0),
            _tx(nr="", source="Journal voucher", journal="GJ", dr="Debtors control", cr="Discount allowed", amount=float(disc_amt0), a=+disc_amt0, o=+disc_amt0, l=0.0),
        ],
    )

    principal_c = float(_pick_amount([3600, 8400]))
    rate_c = float(r.choice([6.0, 7.0, 18.0]))
    months_c = int(r.choice([2, 3, 4]))
    _add_template("arch_9", "interest_overdue_creditor_gj", _make_interest_on_overdue(principal=principal_c, rate_pct=rate_c, months=months_c, nr="17", kind="creditor"))

    repay = float(_pick_amount([44000, 30000]))
    repay_rate = float(r.choice([10.0, 15.0, 18.0]))
    repay_months = int(r.choice([4, 12]))
    _add_template("arch_14", "loan_repayment_interest_cpj", _make_loan_repayment_with_interest(repayment=repay, rate_pct=repay_rate, months=repay_months, nr="18", source="EFT"))

    gross_p = float(_pick_amount([10800, 14000, 3500, 5670]))
    td_p = float(r.choice([8.0, 10.0, 15.0, 20.0]))
    _add_template("arch_15", "purchase_credit_cj", _make_purchase_on_credit_trade_discount(gross=gross_p, td_pct=td_p, nr="19", source="Original invoice", journal="CJ"))

    gross_p2 = float(_pick_amount([12300, 10000, 6000]))
    td_p2 = float(r.choice([10.0, 15.0, 20.0]))
    _add_template("arch_15", "purchase_cheque_cpj", _make_purchase_by_cheque_trade_discount(gross=gross_p2, td_pct=td_p2, nr="20", source="Cheque counterfoil", journal="CPJ"))

    cost_ret = float(_pick_amount([400, 600, 900, 1200, 1500, 2000]))
    sell_ret = float(_round_money(cost_ret * selling_factor))
    _add_template("arch_18", "debtor_allowance_daj", _make_debtor_allowance_return(selling_price=sell_ret, cost_price=cost_ret, nr="21", source="Duplicate credit note", journal="DAJ"))

    cost_ret2 = float(_pick_amount([1200, 1500, 2000, 3500, 5670]))
    td_ret2 = float(r.choice([8.0, 10.0, 15.0, 20.0]))
    _add_template("arch_21", "creditor_allowance_caj", _make_creditor_allowance_return(cost_price=cost_ret2, td_pct=td_ret2, nr="22", source="Duplicate debit note", journal="CAJ"))

    equip_amt = float(_pick_amount([4500, 6800, 12000, 18500, 25000]))
    _add_template(
        "arch_4",
        "equipment_credit_cj",
        [
            _tx(nr="23", source="Original invoice", journal="CJ", dr="Equipment", cr="Creditors control", amount=float(equip_amt), a=+equip_amt, o=0.0, l=+equip_amt)
        ],
    )

    equip_cash = float(_pick_amount([3500, 4800, 9000, 15000]))
    _add_template(
        "arch_4",
        "equipment_cash_cpj",
        [
            _tx(nr="24", source="Cheque counterfoil", journal="CPJ", dr="Equipment", cr="Bank", amount=float(equip_cash), a=0.0, o=0.0, l=0.0)
        ],
    )

    petty_amt = float(_pick_amount([300, 500, 800, 1200, 1500]))
    _add_template(
        "arch_7",
        "petty_cash_transfer",
        [
            _tx(nr="25", source="Cheque counterfoil", journal="CPJ", dr="Petty cash", cr="Bank", amount=float(petty_amt), a=0.0, o=0.0, l=0.0)
        ],
    )

    wages_amt = float(_pick_amount([2500, 3600, 4200, 5800]))
    _add_template(
        "arch_2",
        "wages_eft_internal",
        [
            _tx(nr="26", internal="EFT", journal="CPJ", dr="Wages", cr="Bank", amount=float(wages_amt), a=-wages_amt, o=-wages_amt, l=0.0)
        ],
    )

    rent_paid = float(_pick_amount([1800, 2400, 3000, 4500]))
    _add_template(
        "arch_2",
        "rent_debit_order_internal",
        [
            _tx(nr="27", internal="Debit order", journal="CPJ", dr="Rent expense", cr="Bank", amount=float(rent_paid), a=-rent_paid, o=-rent_paid, l=0.0)
        ],
    )

    ins_paid = float(_pick_amount([900, 1200, 1500, 1800]))
    _add_template(
        "arch_2",
        "insurance_stop_order_internal",
        [
            _tx(nr="28", internal="Stop order", journal="CPJ", dr="Insurance", cr="Bank", amount=float(ins_paid), a=-ins_paid, o=-ins_paid, l=0.0)
        ],
    )

    # --- Missing archetype sections: arch_11, arch_13, arch_19, arch_23, arch_24 ---
    # arch_11 (nested columns with subsidiary ledger accounts)
    t11_amt = float(_round_money(3500 * 0.9 + 420))
    t11 = _tx(nr="29", source="Original invoice", journal="", dr="Trading stock", cr="Creditors control", amount=t11_amt, a=+t11_amt, o=0.0, l=+t11_amt)
    t11["sub_dr"] = ""
    t11["sub_cr"] = "JB Traders"
    _add_template("arch_11", "stock_credit_with_delivery_subledger", [t11])

    t11b_amt = float(_pick_amount([9100]))
    t11b = _tx(nr="30", source="", journal="", dr="Debtors control", cr="Sales", amount=t11b_amt, a=+t11b_amt, o=+t11b_amt, l=0.0)
    t11b["sub_dr"] = "N Costa"
    t11b["sub_cr"] = ""
    _add_template("arch_11", "credit_sale_subledger", [t11b])

    # arch_13 (error correction + equipment return)
    _add_template(
        "arch_13",
        "stationery_error_correction",
        [
            (lambda _amt: _tx(nr="31", source="Journal voucher", journal="GJ", dr="Stationery", cr="Trading stock", amount=_amt, a=0.0, o=-_amt, l=0.0))(float(_pick_amount([1250])))
        ],
    )
    _add_template(
        "arch_13",
        "equipment_return_damaged",
        [
            (lambda _amt: _tx(nr="32", source="Duplicate debit note", journal="CAJ", dr="Creditors control", cr="Equipment", amount=_amt, a=0.0, o=0.0, l=-_amt))(float(_pick_amount([6900, 8000, 10000])))
        ],
    )

    # arch_19 (rent received EFT + consumable stores petty cash)
    rent_eft_amt = float(_pick_amount([4680, 5000]))
    _add_template("arch_19", "rent_received_eft", [_tx(nr="33", internal="EFT", journal="CRJ", dr="Bank", cr="Rent income", amount=rent_eft_amt, a=+rent_eft_amt, o=+rent_eft_amt, l=0.0)])
    cons_amt = float(_pick_amount([210, 300, 450]))
    _add_template("arch_19", "consumable_petty_cash", [_tx(nr="34", source="Petty cash voucher", journal="PCJ", dr="Consumable stores", cr="Petty cash", amount=cons_amt, a=-cons_amt, o=-cons_amt, l=0.0)])

    # arch_23 (source-document heavy set)
    chg_amt = float(_pick_amount([270, 380, 550]))
    _add_template("arch_23", "bank_charges_source", [_tx(nr="35", source="Bank statement", journal="", dr="Bank charges", cr="Bank", amount=chg_amt, a=0.0, o=-chg_amt, l=+chg_amt)])
    loan_amt0 = float(_pick_amount([30000, 50000]))
    _add_template("arch_23", "loan_received_source", [_tx(nr="36", source="Bank statement", journal="", dr="Bank", cr="Loan", amount=loan_amt0, a=+loan_amt0, o=0.0, l=+loan_amt0)])
    _add_template("arch_23", "debtor_settlement_discount_source", _make_debtor_settlement_discount(owed=_pick_amount([3500, 5660]), disc_pct=float(r.choice([5.0, 10.0])), nr="37", source="Duplicate receipt", journal="CRJ"))

    # arch_24 (equipment on credit + cash sales with COS)
    equip_credit_amt = float(_pick_amount([10000, 6900, 2400]))
    _add_template("arch_24", "equipment_credit", [_tx(nr="38", source="Original invoice", journal="CJ", dr="Equipment", cr="Creditors control", amount=equip_credit_amt, a=+equip_credit_amt, o=0.0, l=+equip_credit_amt)])
    _add_template("arch_24", "cash_sales_cost", _make_cash_sales_cost(cost=_pick_amount([3000, 8600]), nr="39", source="Cash register roll", journal="CRJ"))

    # Insolvent debtor: dividend received + write-off balance (two entries)
    insol_owed = float(_pick_amount([4000, 5200, 6000, 8000, 10000]))
    insol_cents = float(r.choice([25.0, 30.0, 35.0, 40.0, 50.0]))
    _add_template(
        "arch_6",
        "insolvent_debtor_dividend_writeoff",
        _make_insolvent_debtor_dividend_writeoff(owed=insol_owed, cents_in_rand=insol_cents, nr="14a", source="Bank statement"),
    )

    # Bank unfavourable (overdraft) variants
    owed_unfav = float(_pick_amount([2800, 3500, 5000]))
    disc_unfav = float(r.choice([2.0, 5.0, 10.0]))
    _add_template("arch_12", "debtor_settlement_discount_unfavourable", _make_debtor_settlement_discount_unfavourable_bank(owed=owed_unfav, disc_pct=disc_unfav, nr="14c"))
    _add_template("arch_20", "overdraft_interest", _make_overdraft_interest(amt=float(_pick_amount([66, 200, 350, 700])), nr="14d"))

    compatible_bank = [(a0, name0, rows0) for (a0, name0, rows0) in template_bank if _compatible(rows0)]

    if not compatible_bank:
        # Fallback to a simple schema if nothing is compatible.
        schema = "gl_amount_aol"
        schema_requires_source = False
        schema_requires_journal = False
        schema_requires_internal = False
        schema_requires_subledger = False
        schema_has_amount = True
        compatible_bank = [(a0, name0, rows0) for (a0, name0, rows0) in template_bank if _compatible(rows0)]

    # Choose a set of archetypes to include in this question (hybrid).
    available_archetypes = sorted({a0 for (a0, _n0, _rows0) in compatible_bank})
    archetypes_in_question = r.sample(available_archetypes, k=min(len(available_archetypes), int(r.choice([3, 4, 5, 6]))))

    picked_templates: List[Tuple[str, str, List[Dict[str, Any]]]] = []
    used_names: set[str] = set()

    for akey in archetypes_in_question:
        candidates = [(a0, n0, rows0) for (a0, n0, rows0) in compatible_bank if a0 == akey and n0 not in used_names]
        if not candidates:
            continue
        chosen = r.choice(candidates)
        used_names.add(chosen[1])
        picked_templates.append(chosen)

    # Fill up to target number of templates if we didn't hit enough.
    target_templates = int(r.choice([6, 7, 8, 9, 10]))
    pool_remaining = [(a0, n0, rows0) for (a0, n0, rows0) in compatible_bank if n0 not in used_names]
    r.shuffle(pool_remaining)
    for item in pool_remaining:
        if len(picked_templates) >= target_templates:
            break
        picked_templates.append(item)
        used_names.add(item[1])

    # Re-number the transaction rows consistently for display.
    flat_txs: List[Dict[str, Any]] = []
    tx_no = 1
    for _a0, _n0, rows0 in picked_templates:
        for t in rows0:
            if str(t.get("nr") or "").strip():
                t["nr"] = str(tx_no)
                tx_no += 1
            flat_txs.append(t)

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}

    def _set(row_index: int, col_index: int, value: Any) -> None:
        correct_map[f"t0_r{int(row_index)}_c{int(col_index)}"] = "" if value is None else str(value)

    def _add_row(row_index: int, values: List[Optional[str]], hint: str = "") -> None:
        display = values if show_answers else ["" for _ in range(len(values))]
        rows.append(_build_prefixed_row(table_index=0, row_index=row_index, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(values):
            _set(row_index, cix, "" if v0 is None else v0)
        if mode_norm == "scaffold" and str(hint or "").strip():
            cell_hints[f"t0_r{int(row_index)}_c0"] = str(hint)

    def _hint_for_row(*, t: Dict[str, Any], current_tx: str) -> str:
        nr0 = str(t.get("nr") or "")
        dr0 = str(t.get("dr") or "")
        cr0 = str(t.get("cr") or "")
        src0 = str(t.get("source") or "")
        jr0 = str(t.get("journal") or "")
        internal0 = str(t.get("internal") or "")
        sub_dr0 = str(t.get("sub_dr") or "")
        sub_cr0 = str(t.get("sub_cr") or "")
        tag0 = str(t.get("tag") or "")
        if nr0.strip():
            if tag0 == "insolvency_dividend":
                owed0 = float(t.get("owed") or 0.0)
                cents0 = float(t.get("cents_in_rand") or 0.0)
                return f"Insolvent debtor: Dividend = Amount owed × (cents in the rand ÷ 100) = {int(owed0)} × {cents0}/100. The balance is written off as bad debts (second row)."
            if tag0 == "fee_income_credit":
                return "Fee income on credit: the debtor owes the business, so Debtors Control (asset) increases; Fee/Service income increases Owner's Equity."
            if tag0 == "bank_unfavourable_receipt":
                return "Bank is unfavourable (overdraft): money received reduces the overdraft (Liabilities decrease), instead of increasing Assets."
            if tag0 == "bank_unfavourable_interest":
                return "Bank is unfavourable (overdraft): interest on overdraft increases Liabilities (overdraft) and decreases Owner's Equity (expense)."
            if tag0 == "fd_maturity_principal":
                return "Fixed deposit maturity: principal returned to Bank (asset swap: Bank increases, Fixed deposit decreases). No net effect on A/O/L."
            if tag0 == "fd_maturity_interest":
                return "Fixed deposit interest: Interest = Principal × Rate% × (Months ÷ 12). Increases Assets (Bank) and Owner's Equity (Income)."
            if "interest" in dr0.lower() or "interest" in cr0.lower():
                return "Interest calculation: Interest = Principal × Rate% × (Months ÷ 12)."
            if internal0.strip() and schema == "internal_gl_amount_aol":
                return "Use the Internal Document (e.g. EFT/Debit order/Stop order) as the source for this transaction."
            if src0.strip() and schema in {"activity23", "activity24", "source_gl_amount_aol"}:
                return "Use the Source document as given, then identify the GL accounts debited/credited and the A/OE/L effect."
            if jr0.strip() and schema == "journal_gl_amount_aol":
                return "Use the Subsidiary Journal (e.g. CRJ/CPJ/CJ/DJ) as the source for this transaction."
            if schema == "gl_subledger_amount_aol" and (sub_dr0.strip() or sub_cr0.strip()):
                return "Section 11 format: fill in the General Ledger accounts AND the Subsidiary Ledger account name (where applicable), then show the effect on A/O/L."
            return ""
        # Continuation rows (2nd entry)
        if tag0 == "insolvency_writeoff":
            return f"Second entry for transaction {current_tx}: write off the unrecovered balance as bad debts."
        if tag0 == "bank_unfavourable_discount":
            return f"Second entry for transaction {current_tx}: record Discount allowed (reduces Owner's Equity)."
        if tag0 == "bank_fee_service":
            return f"Bank fee breakdown for transaction {current_tx}: Service fee reduces Owner's Equity (expense) and increases Liabilities (overdraft)."
        if tag0 == "bank_fee_cash":
            return f"Second entry for transaction {current_tx}: Cash handling fee reduces Owner's Equity (expense)."
        if tag0 == "bank_fee_overdraft_int":
            return f"Third entry for transaction {current_tx}: Overdraft interest reduces Owner's Equity (expense)."
        if dr0.lower() == "interest on loan":
            return f"Second entry for transaction {current_tx}: record the interest portion of the repayment."
        if dr0.lower() == "cost of sales" and cr0.lower() == "trading stock":
            return f"Second entry for transaction {current_tx}: record Cost of sales."
        if dr0.lower() == "discount allowed" and cr0.lower() == "debtors control":
            return f"Second entry for transaction {current_tx}: record Discount allowed."
        if dr0.lower() == "creditors control" and cr0.lower() == "discount received":
            return f"Second entry for transaction {current_tx}: record Discount received."
        if dr0.lower() == "debtors control" and cr0.lower() == "discount allowed":
            return f"Second entry for transaction {current_tx}: reverse the discount allowed (R/D cheque)."
        if dr0.lower() == "trading stock" and cr0.lower() == "cost of sales":
            return f"Second entry for transaction {current_tx}: return stock to inventory (reverse Cost of sales)."
        return f"Second entry for transaction {current_tx}."

    current_tx = ""
    for row_i, t in enumerate(flat_txs):
        if str(t.get("nr") or "").strip():
            current_tx = str(t.get("nr"))
        _add_row(row_i, _schema_to_row(schema, t), hint=_hint_for_row(t=t, current_tx=current_tx))

    journal = {
        "journal_type": "accounting_equation_analysis",
        "table_variant": "grade_project",
        "headers": headers,
        "rows": rows,
        "column_help": {},
        "allow_extra_rows": False,
    }

    header_rows: Optional[List[List[Dict[str, Any]]]] = None
    if schema == "gl_subledger_amount_aol":
        header_rows = [
            [
                {"label": "No.", "rowSpan": 2},
                {"label": "General Ledger", "colSpan": 2},
                {"label": "Subsidiary Ledger", "colSpan": 2},
                {"label": "Amount", "rowSpan": 2},
                {"label": "Equation", "colSpan": 3},
            ],
            [
                {"label": "A/c Dr"},
                {"label": "A/c Cr"},
                {"label": "A/c Dr"},
                {"label": "A/c Cr"},
                {"label": "A"},
                {"label": "O"},
                {"label": "L"},
            ],
        ]
        journal["header_rows"] = header_rows

    out = _make_journal(
        prompt=prompt,
        journal_type="accounting_equation_analysis",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=guidelines,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        header_rows=header_rows,
    )

    out["question_type"] = "journal"
    out["expected_answer_type"] = "journal"
    out["journals"] = [journal]
    out["journal"] = journal
    out["correct_map"] = correct_map
    return out


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


def _dj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Debtor",
        "Fol",
        "Debtors allowances",
        "Cost of sales",
    ]


def _ledger_headers() -> List[str]:
    return [
        "Account",
        "Debit",
        "Credit",
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


def _running_balance_ledger_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Debit",
        "Credit",
        "Balance",
    ]


def _trial_balance_headers() -> List[str]:
    return [
        "Account",
        "Debit",
        "Credit",
    ]


def _debtors_creditors_list_headers() -> List[str]:
    return [
        "Name",
        "Debit",
        "Credit",
    ]


def _reconciliation_impact_headers() -> List[str]:
    return [
        "No.",
        "Debtors control (Dr)",
        "Debtors control (Cr)",
        "Debtors list (Dr)",
        "Debtors list (Cr)",
        "Creditors control (Dr)",
        "Creditors control (Cr)",
        "Creditors list (Dr)",
        "Creditors list (Cr)",
    ]


def _crj_totals_headers_ledger() -> List[str]:
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


def _cpj_totals_headers_ledger() -> List[str]:
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


def _general_ledger_account_headers() -> List[str]:
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


def _make_ledger_posting_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    month_short = str(month)[:3]

    next_month_short = "".join(list(month_short))
    if month_short.lower().startswith("jan"):
        next_month_short = "Feb"
    elif month_short.lower().startswith("feb"):
        next_month_short = "Mar"
    elif month_short.lower().startswith("mar"):
        next_month_short = "Apr"
    elif month_short.lower().startswith("apr"):
        next_month_short = "May"
    elif month_short.lower().startswith("may"):
        next_month_short = "Jun"
    elif month_short.lower().startswith("jun"):
        next_month_short = "Jul"

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    # Journal totals (exam-style: totals from journals are given as information)
    # Keep these internally consistent enough to produce realistic postings.
    crj_bank = float(r.choice([23860, 36000, 57830, 73860, 88400, 96500]))
    crj_sales = float(r.choice([4400, 14000, 44000, 57280]))
    crj_cost_of_sales = _round_money(crj_sales * float(r.choice([0.5, 0.6])))
    crj_discount_allowed = float(r.choice([0, 60, 120, 200, 270]))
    crj_debtors_control = float(r.choice([0, 2800, 3380, 4280, 8960, 24220]))
    crj_current_income = float(r.choice([0, 150, 200, 250, 300, 405, 500, 40720]))
    crj_sundry_amount = float(r.choice([0, 0, 0, 300, 960, 15000, 18000]))

    cpj_bank = float(r.choice([9930, 45360, 66350, 93200]))
    cpj_trading_stock = float(r.choice([17900, 18000, 27900, 42400]))
    cpj_creditors_control = float(r.choice([4690, 6510, 28900, 36510]))
    cpj_discount_received = float(r.choice([0, 90, 200, 620]))
    cpj_wages = float(r.choice([0, 1500, 3500, 7000]))
    cpj_stationery = float(r.choice([0, 300, 1500, 1620, 3400]))
    cpj_sundry_amount = float(r.choice([0, 0, 300, 380, 600, 2400, 2770]))

    # Other journals (used to build more realistic ledger postings)
    dj_sales = float(r.choice([8800, 12800, 14300, 22720]))
    dj_cost_of_sales = _round_money(dj_sales * float(r.choice([0.5, 0.6])))

    daj_allowances = float(r.choice([440, 1200, 3100]))
    daj_cost_of_sales = _round_money(daj_allowances * float(r.choice([0.5, 0.6])))

    cj_creditors_control = float(r.choice([18400, 20423, 58400]))
    cj_trading_stock = float(r.choice([5990, 10361, 25990]))
    cj_stationery = float(r.choice([0, 461, 1500]))

    caj_creditors_control = float(r.choice([1900, 3167, 6900]))
    caj_trading_stock = float(r.choice([570, 1890, 4800]))
    caj_stationery = float(r.choice([0, 74, 175]))

    gj_debits = float(r.choice([97, 1460, 3000, 7500, 12000]))
    gj_credits = float(r.choice([244, 1210, 1200, 8800, 15000]))

    crj_headers = _crj_totals_headers_ledger()
    crj_values: List[Optional[str]] = [
        "TOTAL",
        "",
        "Totals",
        "",
        _fmt_money(crj_bank),
        _fmt_money(crj_sales),
        _fmt_money(crj_cost_of_sales),
        _fmt_money(crj_debtors_control) if crj_debtors_control else "",
        _fmt_money(crj_discount_allowed) if crj_discount_allowed else "",
        _fmt_money(crj_current_income) if crj_current_income else "",
        _fmt_money(crj_sundry_amount) if crj_sundry_amount else "",
        "",
        "" if not crj_sundry_amount else "Sundry",
    ]
    crj_row0 = _build_prefixed_row(table_index=0, row_index=0, values=crj_values, editable_cols=[])
    crj_info = {
        "journal_type": "crj_totals_ledger",
        "table_variant": "grade_project",
        "headers": crj_headers,
        "rows": [crj_row0],
        "column_help": {},
        "allow_extra_rows": False,
    }

    cpj_headers = _cpj_totals_headers_ledger()
    cpj_values: List[Optional[str]] = [
        "TOTAL",
        "",
        "Totals",
        "",
        _fmt_money(cpj_bank),
        _fmt_money(cpj_trading_stock),
        _fmt_money(cpj_creditors_control),
        _fmt_money(cpj_discount_received) if cpj_discount_received else "",
        _fmt_money(cpj_wages) if cpj_wages else "",
        _fmt_money(cpj_stationery) if cpj_stationery else "",
        _fmt_money(cpj_sundry_amount) if cpj_sundry_amount else "",
        "",
        "" if not cpj_sundry_amount else "Sundry",
    ]
    cpj_row0 = _build_prefixed_row(table_index=1, row_index=0, values=cpj_values, editable_cols=[])
    cpj_info = {
        "journal_type": "cpj_totals_ledger",
        "table_variant": "grade_project",
        "headers": cpj_headers,
        "rows": [cpj_row0],
        "column_help": {},
        "allow_extra_rows": False,
    }

    gl_headers = _general_ledger_account_headers()

    def _gl_header_rows(*, acct_name: str, folio: str) -> List[List[Dict[str, Any]]]:
        return [
            [{"label": f"General ledger of {business}", "colSpan": len(gl_headers)}],
            [
                {"label": "Dr.", "colSpan": 1},
                {"label": acct_name, "colSpan": 8},
                {"label": folio, "colSpan": 1},
            ],
            [
                {"label": "Month"},
                {"label": "Day"},
                {"label": "Details"},
                {"label": "Fol"},
                {"label": "Amount"},
                {"label": "Month"},
                {"label": "Day"},
                {"label": "Details"},
                {"label": "Fol"},
                {"label": "Amount"},
            ],
        ]

    def _gl_account_table(*, table_index: int, acct: str, folio: str, opening_debit: float, opening_credit: float, postings: List[Tuple[str, str, str, float, str]]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        # postings: list of (side, details, fol, amount, day) where side in {"dr","cr"}
        editable_cols: List[int]
        if diff == "easy":
            editable_cols = [4, 9]

        rows: List[List[Dict[str, Any]]] = []
        correct: Dict[str, Any] = {}
        cell_hints: Dict[str, str] = {}

        rix = 0
        # Opening balance
        values0: List[Optional[str]] = [
            month_short,
            "1",
            "Balance b/d",
            "b/d",
            _fmt_money(opening_debit) if opening_debit else "",
            month_short,
            "1",
            "Balance b/d",
            "b/d",
            _fmt_money(opening_credit) if opening_credit else "",
        ]
        row0 = _build_prefixed_row(table_index=table_index, row_index=rix, values=values0, editable_cols=editable_cols)
        rows.append(row0)
        correct[f"t{table_index}_r{rix}_c4"] = _fmt_money(opening_debit) if opening_debit else ""
        correct[f"t{table_index}_r{rix}_c9"] = _fmt_money(opening_credit) if opening_credit else ""
        rix += 1

        # Postings
        for side, details, fref, amt, day in postings:
            if side == "dr":
                values: List[Optional[str]] = [month_short, str(day), details, fref, _fmt_money(amt), "", "", "", "", ""]
            else:
                values = ["", "", "", "", "", month_short, str(day), details, fref, _fmt_money(amt)]
            row = _build_prefixed_row(table_index=table_index, row_index=rix, values=values, editable_cols=editable_cols)
            rows.append(row)
            correct[f"t{table_index}_r{rix}_c4"] = _fmt_money(amt) if side == "dr" else ""
            correct[f"t{table_index}_r{rix}_c9"] = _fmt_money(amt) if side == "cr" else ""
            rix += 1

        # Calculate balance c/d
        debit_sum = opening_debit + sum(amt for side, _, __, amt, ___ in postings if side == "dr")
        credit_sum = opening_credit + sum(amt for side, _, __, amt, ___ in postings if side == "cr")
        delta = _round_money(debit_sum - credit_sum)

        if delta == 0.0:
            # Avoid a 0.00 Balance c/d edge case by inserting a tiny adjustment on the debit side.
            # This keeps the ledger arithmetic valid and makes Balance c/d detectable as a non-zero amount.
            adj = 0.01
            values_adj: List[Optional[str]] = [month_short, "30", "Adjustment", "GJ", _fmt_money(adj), "", "", "", "", ""]
            row_adj = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_adj, editable_cols=[])
            rows.append(row_adj)
            correct[f"t{table_index}_r{rix}_c4"] = _fmt_money(adj)
            correct[f"t{table_index}_r{rix}_c9"] = ""
            if mode_norm == "scaffold":
                cell_hints[f"t{table_index}_r{rix}_c4"] = "Adjustment: R0.01 is added on the debit side to avoid a 0.00 balance edge case."
            rix += 1

            debit_sum = _round_money(debit_sum + adj)
            delta = _round_money(debit_sum - credit_sum)

        balance = _round_money(abs(delta))

        if delta > 0:
            # Balance c/d on credit side
            values_bal: List[Optional[str]] = ["", "", "", "", "", month_short, "30", "Balance c/d", "c/d", _fmt_money(balance)]
            row_bal = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_bal, editable_cols=editable_cols)
            rows.append(row_bal)
            correct[f"t{table_index}_r{rix}_c4"] = ""
            correct[f"t{table_index}_r{rix}_c9"] = _fmt_money(balance)
            if mode_norm == "scaffold":
                cell_hints[f"t{table_index}_r{rix}_c9"] = f"Balance c/d = Total debit - Total credit = {_fmt_money(debit_sum)} - {_fmt_money(credit_sum)} = {_fmt_money(balance)}"
        elif delta < 0:
            # Balance c/d on debit side
            values_bal = [month_short, "30", "Balance c/d", "c/d", _fmt_money(balance), "", "", "", "", ""]
            row_bal = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_bal, editable_cols=editable_cols)
            rows.append(row_bal)
            correct[f"t{table_index}_r{rix}_c4"] = _fmt_money(balance)
            correct[f"t{table_index}_r{rix}_c9"] = ""
            if mode_norm == "scaffold":
                cell_hints[f"t{table_index}_r{rix}_c4"] = f"Balance c/d = Total credit - Total debit = {_fmt_money(credit_sum)} - {_fmt_money(debit_sum)} = {_fmt_money(balance)}"
        else:
            # Should not happen due to adjustment above, but keep a safe fallback.
            values_bal = ["", "", "", "", "", month_short, "30", "Balance c/d", "c/d", ""]
            row_bal = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_bal, editable_cols=[])
            rows.append(row_bal)
            correct[f"t{table_index}_r{rix}_c4"] = ""
            correct[f"t{table_index}_r{rix}_c9"] = ""
        rix += 1

        # Totals row
        total = _fmt_money(max(debit_sum, credit_sum))
        values_tot: List[Optional[str]] = ["", "", "Totals", "", total, "", "", "Totals", "", total]
        row_tot = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_tot, editable_cols=editable_cols)
        rows.append(row_tot)
        correct[f"t{table_index}_r{rix}_c4"] = total
        correct[f"t{table_index}_r{rix}_c9"] = total
        if mode_norm == "scaffold":
            cell_hints[f"t{table_index}_r{rix}_c4"] = f"Totals: add all debit amounts (including Balance c/d if on debit side). Total debit = {total}."
            cell_hints[f"t{table_index}_r{rix}_c9"] = f"Totals: add all credit amounts (including Balance c/d if on credit side). Total credit = {total}."
        rix += 1

        # Next month balance b/d (carry forward the closing balance)
        if delta > 0:
            next_debit, next_credit = _round_money(delta), 0.0
        elif delta < 0:
            next_debit, next_credit = 0.0, _round_money(abs(delta))
        else:
            next_debit, next_credit = 0.0, 0.0

        values_next: List[Optional[str]] = [
            next_month_short,
            "1",
            "Balance b/d",
            "b/d",
            _fmt_money(next_debit) if next_debit else "",
            next_month_short,
            "1",
            "Balance b/d",
            "b/d",
            _fmt_money(next_credit) if next_credit else "",
        ]
        row_next = _build_prefixed_row(table_index=table_index, row_index=rix, values=values_next, editable_cols=editable_cols)
        rows.append(row_next)
        correct[f"t{table_index}_r{rix}_c4"] = _fmt_money(next_debit) if next_debit else ""
        correct[f"t{table_index}_r{rix}_c9"] = _fmt_money(next_credit) if next_credit else ""
        if mode_norm == "scaffold":
            if next_debit:
                cell_hints[f"t{table_index}_r{rix}_c4"] = f"Balance b/d = Balance c/d carried forward to next month (debit side): {_fmt_money(next_debit)}"
            if next_credit:
                cell_hints[f"t{table_index}_r{rix}_c9"] = f"Balance b/d = Balance c/d carried forward to next month (credit side): {_fmt_money(next_credit)}"
        journal = {
            "journal_type": "general_ledger_account",
            "table_variant": "grade_project",
            "headers": gl_headers,
            "rows": rows,
            "header_rows": _gl_header_rows(acct_name=acct, folio=folio),
            "column_help": {},
            "allow_extra_rows": False,
        }
        return journal, correct, cell_hints

    # Randomly choose 2–4 accounts to post to (per user preference).
    possible_accounts: List[Tuple[str, str]] = [
        ("Bank", "B1"),
        ("Sales", "N1"),
        ("Cost of Sales", "N2"),
        ("Trading stock", "B6"),
        ("Debtors control", "B7"),
        ("Creditors control", "B9"),
        ("Stationery", "N8"),
        ("Current income", "N3"),
    ]
    k = int(r.choice([2, 3, 4]))
    chosen = r.sample(possible_accounts, k=k)

    journals: List[Dict[str, Any]] = [crj_info, cpj_info]
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}

    def _opening_for(acct: str) -> Tuple[float, float]:
        # Return opening debit, opening credit
        if acct.lower() in ("bank", "trading stock", "debtors control", "stationery"):
            return float(r.choice([0, 0, 500, 1240, 20600, 23500, 28300, 35380])), 0.0
        if acct.lower() in ("sales",):
            return 0.0, float(r.choice([0, 0, 44400, 150000]))
        if acct.lower() in ("creditors control",):
            return 0.0, float(r.choice([0, 0, 16200, 20600]))
        if acct.lower() in ("cost of sales",):
            return float(r.choice([0, 0, 56120, 93750])), 0.0
        if acct.lower() in ("current income",):
            return 0.0, float(r.choice([0, 0, 18000, 40720]))
        return 0.0, 0.0

    def _postings_for(acct: str) -> List[Tuple[str, str, str, float, str]]:
        a = acct.lower()
        p: List[Tuple[str, str, str, float, str]] = []
        # Bank: CRJ total receipts (Dr), CPJ total payments (Cr)
        if a == "bank":
            p.append(("dr", "Total receipts", "CRJ", crj_bank, "30"))
            p.append(("cr", "Total payments", "CPJ", cpj_bank, "30"))
        # Sales: CRJ bank (cash sales) and DJ debtors control
        if a == "sales":
            if crj_sales:
                p.append(("cr", "Bank", "CRJ", crj_sales, "30"))
            if dj_sales:
                p.append(("cr", "Debtors control", "DJ", dj_sales, "30"))
        # Cost of Sales: Trading stock on debit side from CRJ/DJ/DAJ
        if a == "cost of sales":
            if crj_cost_of_sales:
                p.append(("dr", "Trading stock", "CRJ", crj_cost_of_sales, "30"))
            if dj_cost_of_sales:
                p.append(("dr", "Trading stock", "DJ", dj_cost_of_sales, "30"))
            if daj_cost_of_sales:
                p.append(("dr", "Trading stock", "DAJ", daj_cost_of_sales, "30"))
        # Trading stock: bank/creditors control on debit; cost of sales and allowances on credit
        if a == "trading stock":
            if cpj_trading_stock:
                p.append(("dr", "Bank", "CPJ", cpj_trading_stock, "30"))
            if cj_trading_stock:
                p.append(("dr", "Creditors control", "CJ", cj_trading_stock, "30"))
            if crj_cost_of_sales:
                p.append(("cr", "Cost of sales", "CRJ", crj_cost_of_sales, "30"))
            if dj_cost_of_sales:
                p.append(("cr", "Cost of sales", "DJ", dj_cost_of_sales, "30"))
            if daj_cost_of_sales:
                p.append(("cr", "Cost of sales", "DAJ", daj_cost_of_sales, "30"))
            if caj_trading_stock:
                p.append(("cr", "Creditors control", "CAJ", caj_trading_stock, "30"))
        # Debtors control: Sales (Dr), journal debits (Dr), petty cash (Dr); CRJ settlement (Cr), discounts/allowances (Cr)
        if a == "debtors control":
            if dj_sales:
                p.append(("dr", "Sales", "DJ", dj_sales, "30"))
            if daj_allowances:
                p.append(("cr", "Debtors allowances", "DAJ", daj_allowances, "30"))
            if crj_debtors_control:
                p.append(("cr", "Bank", "CRJ", crj_debtors_control, "30"))
            if crj_discount_allowed:
                p.append(("cr", "Discount allowed", "CRJ", crj_discount_allowed, "30"))
            if gj_debits:
                p.append(("dr", "Journal debits", "GJ", gj_debits, "30"))
            if gj_credits:
                p.append(("cr", "Journal credits", "GJ", gj_credits, "30"))
        # Creditors control: payments (Dr), allowances (Dr), journal debits (Dr); purchases (Cr), journal credits (Cr)
        if a == "creditors control":
            if cpj_creditors_control:
                p.append(("dr", "Bank + D/R", "CPJ", cpj_creditors_control, "30"))
            if caj_creditors_control:
                p.append(("dr", "Sundry allowances", "CAJ", caj_creditors_control, "30"))
            if cj_creditors_control:
                p.append(("cr", "Sundry purchases", "CJ", cj_creditors_control, "30"))
            if gj_debits:
                p.append(("dr", "Journal debits", "GJ", gj_debits, "30"))
            if gj_credits:
                p.append(("cr", "Journal credits", "GJ", gj_credits, "30"))
        # Stationery: bank (Dr), creditors control (Dr) and returns (Cr) and drawings (Cr via GJ)
        if a == "stationery":
            if cpj_stationery:
                p.append(("dr", "Bank", "CPJ", cpj_stationery, "30"))
            if cj_stationery:
                p.append(("dr", "Creditors control", "CJ", cj_stationery, "30"))
            if caj_stationery:
                p.append(("cr", "Creditors control", "CAJ", caj_stationery, "30"))
            if gj_credits:
                p.append(("cr", "Drawings", "GJ", _round_money(gj_credits * 0.2), "30"))
        # Current income: posted from CRJ (credit)
        if a == "current income":
            if crj_current_income:
                p.append(("cr", "Bank", "CRJ", crj_current_income, "30"))
        return [x for x in p if x[3] and x[3] > 0]

    # Build ledger tables for selected accounts
    for i, (acct, folio) in enumerate(chosen):
        od, oc = _opening_for(acct)
        postings = _postings_for(acct)
        table_index = 2 + i
        j, c, ch = _gl_account_table(table_index=table_index, acct=acct, folio=folio, opening_debit=od, opening_credit=oc, postings=postings)
        journals.append(j)
        correct_map.update(c)
        cell_hints.update(ch)

    prompt = (
        f"{business}\n"
        f"General Ledger for {month}\n\n"
        "Context:\n"
        "- A Cash Receipts Journal (CRJ) totals table is given as information.\n"
        "- A Cash Payments Journal (CPJ) totals table is given as information.\n\n"
        "Required:\n"
        "Post the relevant totals to the General Ledger accounts provided."
    )

    out = _make_journal(
        prompt=prompt,
        journal_type="general_ledger",
        headers=gl_headers,
        rows=journals[-1]["rows"],
        correct_map=correct_map,
        guidelines=[
            "Use the totals from the CRJ information table.",
            "Current income is posted as a separate account (credit).",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
    )
    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    out["journals"] = journals
    out["journal"] = journals[-1]
    out["correct_map"] = correct_map
    return out


def _make_debtors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    debtor = r.choice(["M. Smart", "F. Thulo", "J. Abrahams", "N. Rossouw"])
    fol = str(r.choice(["DL1", "DL2", "DL3", "DL4", "DL5", "DL6"]))

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    headers = _running_balance_ledger_headers()

    opening_balance = float(r.choice([3500, 4800, 5600, 7000, 8200, 9500]))
    sale_amount = float(r.choice([2500, 3200, 4000, 5000, 6200]))
    receipt_amount = float(r.choice([1800, 2400, 3000, 4200, 6800]))
    if receipt_amount >= opening_balance:
        receipt_amount = _round_money(opening_balance * 0.85)
    discount_allowed = float(r.choice([0, 100, 150, 200, 225]))
    if discount_allowed >= receipt_amount:
        discount_allowed = 0.0
    credit_note_amount = float(r.choice([0, 0, 450, 600, 900]))
    dishonoured = bool(r.choice([True, False]))
    interest_rate_pct = float(r.choice([4.0, 6.0]))

    invoice_no = str(r.choice(["101", "102", "105", "x23", "x56"]))
    receipt_no = str(r.choice(["4002", "4020", "76", "142", "58"]))
    credit_note_no = str(r.choice(["11", "12", "18", "25"]))

    tx: List[Dict[str, Any]] = []
    tx.append({"day": 1, "details": "Balance b/d", "fol": "b/d", "debit": 0.0, "credit": 0.0, "balance": opening_balance})
    tx.append({"day": 5, "details": f"Invoice No. {invoice_no}", "fol": "DJ3", "debit": sale_amount, "credit": 0.0, "balance": 0.0})
    tx.append({"day": 10, "details": f"Receipt No. {receipt_no}", "fol": "CRJ3", "debit": 0.0, "credit": receipt_amount, "balance": 0.0})
    if discount_allowed > 0:
        tx.append({"day": 10, "details": "Discount allowed", "fol": "CRJ3", "debit": 0.0, "credit": discount_allowed, "balance": 0.0})
    if credit_note_amount > 0:
        tx.append({"day": 15, "details": f"Credit Note No. {credit_note_no}", "fol": "DAJ3", "debit": 0.0, "credit": credit_note_amount, "balance": 0.0})
    if dishonoured:
        tx.append({"day": 20, "details": "Dishonoured cheque (R/D)", "fol": "CPJ3", "debit": receipt_amount, "credit": 0.0, "balance": 0.0})
        if discount_allowed > 0:
            tx.append({"day": 20, "details": "Discount cancelled", "fol": "GJ3", "debit": discount_allowed, "credit": 0.0, "balance": 0.0})
    interest = _round_money(opening_balance * (interest_rate_pct / 100.0))
    tx.append({"day": 25, "details": "Interest income", "fol": "GJ3", "debit": interest, "credit": 0.0, "balance": 0.0})

    running = opening_balance
    for i in range(1, len(tx)):
        running = _round_money(running + tx[i]["debit"] - tx[i]["credit"])
        tx[i]["balance"] = running

    editable_cols: List[int]
    if diff == "easy":
        editable_cols = [3, 4, 5]
    else:
        editable_cols = list(range(6))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    working_map: Dict[str, str] = {}

    for i, t in enumerate(tx):
        values: List[Optional[str]] = [
            str(t["day"]),
            t["details"],
            t["fol"],
            _fmt_money(t["debit"]) if t["debit"] else "",
            _fmt_money(t["credit"]) if t["credit"] else "",
            _fmt_money(t["balance"]),
        ]
        rows.append(_build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        if diff != "easy":
            correct_map[f"r{i}_c0"] = str(t["day"])
            correct_map[f"r{i}_c1"] = t["details"]
            correct_map[f"r{i}_c2"] = t["fol"]
        else:
            correct_map[f"r{i}_c0"] = str(t["day"])
        correct_map[f"r{i}_c3"] = _fmt_money(t["debit"]) if t["debit"] else ""
        correct_map[f"r{i}_c4"] = _fmt_money(t["credit"]) if t["credit"] else ""
        correct_map[f"r{i}_c5"] = _fmt_money(t["balance"])

        if mode_norm == "scaffold":
            if i == 0:
                cell_hints[f"r{i}_c5"] = "Opening balance: amount the debtor owes at the start of the month."
            if "Invoice" in t["details"]:
                cell_hints[f"r{i}_c3"] = "Credit sale increases the amount owed (debit)."
            if "Receipt" in t["details"]:
                cell_hints[f"r{i}_c4"] = "Receipt reduces the amount owed (credit)."
            if t["details"] == "Discount allowed":
                cell_hints[f"r{i}_c4"] = "Discount allowed reduces the amount owed, so it is credited."
            if "Dishonoured cheque" in t["details"]:
                cell_hints[f"r{i}_c3"] = "Dishonoured cheque reverses the receipt: debtor owes again (debit)."
            if t["details"] == "Discount cancelled":
                cell_hints[f"r{i}_c3"] = "Discount cancelled is debited because the debtor now owes the full amount again."
            if t["details"] == "Interest income":
                cell_hints[f"r{i}_c3"] = f"Interest = Opening balance x rate = {_fmt_money(opening_balance)} x ({interest_rate_pct:g}%/100) = {_fmt_money(interest)}"
            if i > 0:
                prev = tx[i - 1]["balance"]
                d = t["debit"]
                c = t["credit"]
                cell_hints[f"r{i}_c5"] = f"Balance = previous balance + debit - credit = {_fmt_money(prev)} + {_fmt_money(d)} - {_fmt_money(c)} = {_fmt_money(t['balance'])}"

    prompt_lines = [
        f"{business}",
        f"Debtors Ledger ({debtor}) for {month}",
        "",
        "Information:",
        f"- Opening balance on 1 {month}: R{opening_balance:.2f}",
        f"- 5 {month}: Sold goods on credit, Invoice {invoice_no}, R{sale_amount:.2f}",
        f"- 10 {month}: Received payment, Receipt {receipt_no}, R{receipt_amount:.2f}",
    ]
    if discount_allowed > 0:
        prompt_lines.append(f"- 10 {month}: Discount allowed, R{discount_allowed:.2f}")
    if credit_note_amount > 0:
        prompt_lines.append(f"- 15 {month}: Goods returned, Credit note {credit_note_no}, R{credit_note_amount:.2f}")
    if dishonoured:
        prompt_lines.append(f"- 20 {month}: Cheque returned (R/D) for Receipt {receipt_no}")
        if discount_allowed > 0:
            prompt_lines.append(f"- 20 {month}: Discount cancelled")
    prompt_lines.append(f"- 25 {month}: Interest charged at {interest_rate_pct:g}% on opening balance")
    prompt_lines.extend(["", "Required:", "Complete the Debtors Ledger account (running balance)."])
    prompt = "\n".join(prompt_lines)

    out = _make_journal(
        prompt=prompt,
        journal_type="debtors_ledger",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Debit increases the amount the debtor owes; credit decreases it.",
            "Balance is a running total: previous balance + debit - credit.",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
        working_map=working_map if mode_norm == "scaffold" else None,
    )
    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    return out


def _make_creditors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    business = r.choice(["Lonely Traders", "Khumalo Traders", "Mokoena Stores"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    creditor = r.choice(["Marang Suppliers", "RN Wholesalers", "Sam Distributors", "MZ Suppliers"])
    fol = str(r.choice(["CL8", "CL3", "CL5", "CL6"]))

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
    for i in range(1, len(tx)):
        running = _round_money(running + tx[i]["credit"] - tx[i]["debit"])
        tx[i]["balance"] = running

    editable_cols: List[int]
    if diff == "easy":
        editable_cols = [3, 4, 5]
    else:
        editable_cols = list(range(6))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    working_map: Dict[str, str] = {}

    for i, t in enumerate(tx):
        values: List[Optional[str]] = [
            str(t["day"]),
            t["details"],
            t["fol"],
            _fmt_money(t["debit"]) if t["debit"] else "",
            _fmt_money(t["credit"]) if t["credit"] else "",
            _fmt_money(t["balance"]),
        ]
        rows.append(_build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        if diff != "easy":
            correct_map[f"r{i}_c0"] = str(t["day"])
            correct_map[f"r{i}_c1"] = t["details"]
            correct_map[f"r{i}_c2"] = t["fol"]
        else:
            correct_map[f"r{i}_c0"] = str(t["day"])
        correct_map[f"r{i}_c3"] = _fmt_money(t["debit"]) if t["debit"] else ""
        correct_map[f"r{i}_c4"] = _fmt_money(t["credit"]) if t["credit"] else ""
        correct_map[f"r{i}_c5"] = _fmt_money(t["balance"])

        if mode_norm == "scaffold":
            if i == 0:
                cell_hints[f"r{i}_c5"] = "Opening balance: amount owed to the creditor at the start of the month."
            if "Invoice" in t["details"]:
                cell_hints[f"r{i}_c4"] = "Credit purchase increases what we owe (credit column)."
            if "Debit note" in t["details"]:
                cell_hints[f"r{i}_c3"] = "Returns/allowances reduce what we owe (debit column)."
            if "Cheque" in t["details"]:
                cell_hints[f"r{i}_c3"] = "Payment reduces what we owe (debit column)."
            if trade_discount_pct > 0 and t["details"] == f"Invoice No. {invoice_no2}":
                cell_hints[f"r{i}_c4"] = f"Net invoice = Gross x (1 - discount%) = {_fmt_money(invoice_gross)} x (1 - {trade_discount_pct:g}%/100) = {_fmt_money(invoice_net)}"
            if i > 0:
                prev = tx[i - 1]["balance"]
                d = t["debit"]
                c = t["credit"]
                cell_hints[f"r{i}_c5"] = f"Balance = previous balance + credit - debit = {_fmt_money(prev)} + {_fmt_money(c)} - {_fmt_money(d)} = {_fmt_money(t['balance'])}"

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
    prompt = "\n".join(prompt_lines)

    out = _make_journal(
        prompt=prompt,
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


def _make_reconciliation_impact_matrix_question(*, r: random.Random, difficulty: Optional[str] = None) -> Dict[str, Any]:
    return _st_make_reconciliation_impact_matrix_question(r=r, difficulty=difficulty)


def _trading_stock_header_rows(*, business: str) -> List[List[Dict[str, Any]]]:
    headers = _general_ledger_account_headers()
    return [
        [{"label": f"General ledger of {business}", "colSpan": len(headers)}],
        [{"label": "Dr.", "colSpan": 1}, {"label": "", "colSpan": 8}, {"label": "Cr.", "colSpan": 1}],
    ]


def _make_control_account_study_table(
    *,
    r: random.Random,
    variant: str = "debtors",
) -> Dict[str, Any]:
    return _st_make_control_account_study_table(r=r, variant=variant)


def _make_control_account_study_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
) -> Dict[str, Any]:
    return _st_make_control_account_study_question(r=r, difficulty=difficulty, mode=mode, variant=variant)


def _make_control_accounts_reconciliation_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
) -> Dict[str, Any]:
    return _st_make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode, variant=variant)


def _make_trading_stock_account_headers() -> List[str]:
    return _general_ledger_account_headers()


def _make_trading_stock_account_table(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    table_index: int,
    business: str,
    month: str,
    year: int,
    opening: float,
    bank_cpj: float,
    creditors_cj: float,
    petty_cash_pcj: float,
    debtors_returns_daj: float,
    creditors_returns_caj: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
    editable: bool,
    show_blanks: bool,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    return _st_make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=table_index,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=editable,
        show_blanks=show_blanks,
    )


def _make_trading_stock_prepare_from_journals_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_prepare_from_journals_question(r=r, difficulty=difficulty, mode=mode)


def _make_trading_stock_fill_missing_details_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_fill_missing_details_question(r=r, difficulty=difficulty, mode=mode)


def _make_trading_stock_activity16_analysis_typed(*, r: random.Random) -> Dict[str, Any]:
    return _st_make_trading_stock_activity16_analysis_typed(r=r)


def _make_trading_stock_section3_analysis_typed(*, r: random.Random) -> Dict[str, Any]:
    return _st_make_trading_stock_section3_analysis_typed(r=r)


def _make_trading_stock_prepare_with_two_returns_percent_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_prepare_with_two_returns_percent_question(r=r, difficulty=difficulty, mode=mode)


def _make_trading_stock_markup_trade_discount_typed(*, r: random.Random) -> Dict[str, Any]:
    return _st_make_trading_stock_markup_trade_discount_typed(r=r)


def _make_trading_stock_prepare_with_returns_percent_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_prepare_with_returns_percent_question(r=r, difficulty=difficulty, mode=mode)


def _make_trading_stock_prepare_with_discount_calc_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_prepare_with_discount_calc_question(r=r, difficulty=difficulty, mode=mode)


def _make_trading_stock_prepare_from_casted_journals_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trading_stock_prepare_from_casted_journals_question(r=r, difficulty=difficulty, mode=mode)


def _make_control_accounts_internal_control_typed(
    *, r: random.Random, variant: str = "debtors"
) -> Dict[str, Any]:
    return _st_make_control_accounts_internal_control_typed(r=r, variant=variant)


def generate_questions(*, r: random.Random, n: int, subskill: str = "", difficulty: str = "", mode: str = "", variant: str = "") -> List[Dict[str, Any]]:
    subskill_norm = str(subskill or "").strip().lower()
    qtype_norm = str(difficulty or "").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    var_norm = str(variant or "").strip().lower()

    def _maybe_filter(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if qtype_norm in ("", "mixed"):
            return items
        return [q for q in items if q.get("question_type") == qtype_norm] or items

    concepts_pool: List[Dict[str, Any]] = [
        _make_control_accounts_internal_control_typed(r=r, variant=r.choice(["debtors", "creditors"])),
    ]
    accounting_cycle_pool: List[Dict[str, Any]] = [
        _make_accounting_cycle_question(r=r),
    ]
    equation_pool: List[Dict[str, Any]] = [
        _make_transaction_analysis_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]

    crj_pool: List[Dict[str, Any]] = [
        _st_make_crj_single_row_question(r=r, difficulty=difficulty),
        _st_make_crj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_crj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    cpj_pool: List[Dict[str, Any]] = [
        _st_make_cpj_single_row_question(r=r),
        _st_make_cpj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B", "C", "D"]))),
        _st_make_cpj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B", "C", "D"]))),
    ]
    dj_pool: List[Dict[str, Any]] = [
        _st_make_dj_single_row_question(r=r, difficulty=difficulty),
        _st_make_dj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_dj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    daj_pool: List[Dict[str, Any]] = [
        _st_make_daj_single_row_question(r=r, difficulty=difficulty),
        _st_make_daj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_daj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    cj_pool: List[Dict[str, Any]] = [
        _st_make_cj_single_row_question(r=r, difficulty=difficulty),
        _st_make_cj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_cj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    caj_pool: List[Dict[str, Any]] = [
        _st_make_caj_single_row_question(r=r, difficulty=difficulty),
        _st_make_caj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
        _st_make_caj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    pcj_pool: List[Dict[str, Any]] = [
        _st_make_pcj_single_row_question(r=r, difficulty=difficulty),
        _st_make_pcj_activity11_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
        _st_make_pcj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
    ]
    gj_pool: List[Dict[str, Any]] = [
        _st_make_gj_single_row_question(r=r, difficulty=difficulty),
        _st_make_gj_activity13_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
        _st_make_gj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
    ]
    journals_pool: List[Dict[str, Any]] = crj_pool + cpj_pool + dj_pool + daj_pool + cj_pool + caj_pool + pcj_pool + gj_pool

    ledger_pool: List[Dict[str, Any]] = [
        _make_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_debtors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_creditors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    general_ledger_pool: List[Dict[str, Any]] = [
        _make_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    debtors_ledger_pool: List[Dict[str, Any]] = [
        _make_debtors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]
    creditors_ledger_pool: List[Dict[str, Any]] = [
        _make_creditors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]

    trial_balance_pool: List[Dict[str, Any]] = [
        _make_typed(
            prompt="Trial balance (Grade 10):\n\nRequired:\nExplain what a trial balance is used for.",
            sample_answer="A trial balance lists ledger account balances to check that total debits equal total credits.",
        ),
    ]

    trading_stock_account_pool: List[Dict[str, Any]] = [
        _make_trading_stock_prepare_from_journals_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_trading_stock_prepare_from_casted_journals_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_trading_stock_fill_missing_details_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_trading_stock_activity16_analysis_typed(r=r),
        _make_trading_stock_section3_analysis_typed(r=r),
        _make_trading_stock_prepare_with_two_returns_percent_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_trading_stock_markup_trade_discount_typed(r=r),
        _make_trading_stock_prepare_with_returns_percent_question(r=r, difficulty=difficulty, mode=mode_norm),
        _make_trading_stock_prepare_with_discount_calc_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]

    full_accounting_cycle_bookkeeping_pool: List[Dict[str, Any]] = [
        _st_make_full_accounting_cycle_project_question(r=r, difficulty=difficulty, mode=mode_norm),
    ]

    control_accounts_pool: List[Dict[str, Any]] = [
        _make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode_norm, variant="debtors"),
        _make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode_norm, variant="creditors"),
        _make_control_account_study_question(r=r, difficulty=difficulty, mode=mode_norm, variant="debtors"),
        _make_control_account_study_question(r=r, difficulty=difficulty, mode=mode_norm, variant="creditors"),
        _make_control_accounts_internal_control_typed(r=r, variant="creditors"),
    ]
    control_accounts_reconciliation_pool: List[Dict[str, Any]] = [
        _make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode_norm, variant="debtors"),
        _make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode_norm, variant="creditors"),
    ]
    reconciliation_analysis_pool: List[Dict[str, Any]] = [
        _make_reconciliation_impact_matrix_question(r=r, difficulty=difficulty),
        _make_control_accounts_internal_control_typed(r=r, variant=r.choice(["debtors", "creditors"])),
    ]

    mixed_pool: List[Dict[str, Any]] = concepts_pool + accounting_cycle_pool + equation_pool + ledger_pool + trial_balance_pool + journals_pool

    pools_by_subskill = _build_pools_by_subskill(
        concepts_pool=concepts_pool,
        accounting_cycle_pool=accounting_cycle_pool,
        equation_pool=equation_pool,
        ledger_pool=ledger_pool,
        general_ledger_pool=general_ledger_pool,
        debtors_ledger_pool=debtors_ledger_pool,
        creditors_ledger_pool=creditors_ledger_pool,
        trial_balance_pool=trial_balance_pool,
        trading_stock_account_pool=trading_stock_account_pool,
        full_accounting_cycle_bookkeeping_pool=full_accounting_cycle_bookkeeping_pool,
        control_accounts_pool=control_accounts_pool,
        control_accounts_reconciliation_pool=control_accounts_reconciliation_pool,
        reconciliation_analysis_pool=reconciliation_analysis_pool,
        journals_pool=journals_pool,
        crj_pool=crj_pool,
        cpj_pool=cpj_pool,
        dj_pool=dj_pool,
        daj_pool=daj_pool,
        cj_pool=cj_pool,
        caj_pool=caj_pool,
        pcj_pool=pcj_pool,
        gj_pool=gj_pool,
        mixed_pool=mixed_pool,
    )

    pool = pools_by_subskill.get(subskill_norm, pools_by_subskill["mixed"])
    pool = _maybe_filter(pool)

    out: List[Dict[str, Any]] = []

    if subskill_norm == "cpj" and qtype_norm in ("", "mixed", "journal"):
        cycle = ["A", "B", "C", "D"]
        for i in range(n):
            vid = cycle[i % len(cycle)]
            if i % 2 == 0:
                out.append(_st_make_cpj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
            else:
                out.append(_st_make_cpj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
        return out

    if subskill_norm == "gj" and qtype_norm in ("", "mixed", "journal"):
        cycle = ["A", "B"]
        for i in range(n):
            vid = cycle[i % len(cycle)]
            if i % 2 == 0:
                out.append(_st_make_gj_activity13_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
            else:
                out.append(_st_make_gj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
        return out

    if subskill_norm == "pcj" and qtype_norm in ("", "mixed", "journal"):
        cycle = ["A", "B"]
        for i in range(n):
            vid = cycle[i % len(cycle)]
            if i % 2 == 0:
                out.append(_st_make_pcj_activity11_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
            else:
                out.append(_st_make_pcj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=vid))
        return out

    if subskill_norm == "dj" and qtype_norm in ("", "mixed", "journal"):
        for i in range(n):
            if i % 2 == 0:
                out.append(_st_make_dj_activity_question(r=r, difficulty=difficulty, mode=mode_norm))
            else:
                out.append(_st_make_dj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm))
        return out

    if subskill_norm == "daj" and qtype_norm in ("", "mixed", "journal"):
        for i in range(n):
            if i % 2 == 0:
                out.append(_st_make_daj_activity_question(r=r, difficulty=difficulty, mode=mode_norm))
            else:
                out.append(_st_make_daj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm))
        return out

    if subskill_norm == "cj" and qtype_norm in ("", "mixed", "journal"):
        for i in range(n):
            if i % 2 == 0:
                out.append(_st_make_cj_activity_question(r=r, difficulty=difficulty, mode=mode_norm))
            else:
                out.append(_st_make_cj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm))
        return out

    if subskill_norm == "caj" and qtype_norm in ("", "mixed", "journal"):
        for i in range(n):
            if i % 2 == 0:
                out.append(_st_make_caj_activity_question(r=r, difficulty=difficulty, mode=mode_norm))
            else:
                out.append(_st_make_caj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm))
        return out

    for _ in range(n):
        out.append(r.choice(pool))

    return out