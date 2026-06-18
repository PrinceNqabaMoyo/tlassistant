from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_calc as _make_calc
from ..sole_trader.core import make_id as _make_id
from ..sole_trader.core import make_mcq as _make_mcq
from ..sole_trader.core import make_typed as _make_typed
from ..sole_trader.core import make_match as _make_match
from ..sole_trader.core import make_word_bank as _make_word_bank
from ..sole_trader.core import make_inline_fill as _make_inline_fill
from ..sole_trader.core import calc_selling_price_from_cost_price_and_margin as _calc_selling_price_from_cost_price_and_margin
from ..sole_trader.core import calc_cost_price_from_selling_price_and_margin as _calc_cost_price_from_selling_price_and_margin
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.column_help import headers_to_column_help as _headers_to_column_help
from ..sole_trader.journal_table import build_journal_row as _build_journal_row
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.names import pick_business_names as _pick_business_names
from ..sole_trader.names import pick_person_names as _pick_person_names

from ..sole_trader.control_accounts import make_control_account_study_question as _st_make_control_account_study_question
from ..sole_trader.control_accounts import make_control_account_study_table as _st_make_control_account_study_table
from ..sole_trader.control_accounts import make_control_accounts_analysis_typed as _st_make_control_accounts_analysis_typed
from ..sole_trader.control_accounts import make_control_accounts_internal_control_typed as _st_make_control_accounts_internal_control_typed
from ..sole_trader.control_accounts import make_control_accounts_opening_balance_calc as _st_make_control_accounts_opening_balance_calc
from ..sole_trader.control_accounts import make_control_accounts_reconciliation_question as _st_make_control_accounts_reconciliation_question
from ..sole_trader.control_accounts import make_reconciliation_impact_matrix_question as _st_make_reconciliation_impact_matrix_question

from ..sole_trader.trading_stock_account import make_trading_stock_account_table as _st_make_trading_stock_account_table
from ..sole_trader.trading_stock_account import make_trading_stock_activity16_analysis_typed as _st_make_trading_stock_activity16_analysis_typed
from ..sole_trader.trading_stock_account import make_trading_stock_section3_analysis_typed as _st_make_trading_stock_section3_analysis_typed
from ..sole_trader.trading_stock_account import make_trading_stock_fill_missing_details_question as _st_make_trading_stock_fill_missing_details_question
from ..sole_trader.trading_stock_account import make_trading_stock_prepare_from_casted_journals_question as _st_make_trading_stock_prepare_from_casted_journals_question
from ..sole_trader.trading_stock_account import make_trading_stock_prepare_from_journals_question as _st_make_trading_stock_prepare_from_journals_question
from ..sole_trader.trading_stock_account import make_trading_stock_prepare_with_discount_calc_question as _st_make_trading_stock_prepare_with_discount_calc_question
from ..sole_trader.trading_stock_account import make_trading_stock_prepare_with_returns_percent_question as _st_make_trading_stock_prepare_with_returns_percent_question

from ..sole_trader.trading_stock_account import (
    make_trading_stock_prepare_with_two_returns_percent_question as _st_make_trading_stock_prepare_with_two_returns_percent_question,
)
from ..sole_trader.trading_stock_account import (
    make_trading_stock_markup_trade_discount_typed as _st_make_trading_stock_markup_trade_discount_typed,
)

from ..sole_trader.pools import build_pools_by_subskill as _build_pools_by_subskill

from ..sole_trader.journals.crj import make_crj_single_row_question as _st_make_crj_single_row_question
from ..sole_trader.journals.crj import make_crj_activity5_question as _st_make_crj_activity5_question
from ..sole_trader.journals.crj import make_crj_exam_style_question as _st_make_crj_exam_style_question
from ..sole_trader.journals.cpj import make_cpj_single_row_question as _st_make_cpj_single_row_question
from ..sole_trader.journals.cpj import make_cpj_activity5_question as _st_make_cpj_activity5_question
from ..sole_trader.journals.cpj import make_cpj_exam_style_question as _st_make_cpj_exam_style_question
from ..sole_trader.journals.dj import make_dj_activity_question as _st_make_dj_activity_question
from ..sole_trader.journals.dj import make_dj_exam_style_question as _st_make_dj_exam_style_question
from ..sole_trader.journals.dj import make_dj_single_row_question as _st_make_dj_single_row_question
from ..sole_trader.journals.daj import make_daj_activity_question as _st_make_daj_activity_question
from ..sole_trader.journals.daj import make_daj_exam_style_question as _st_make_daj_exam_style_question
from ..sole_trader.journals.daj import make_daj_single_row_question as _st_make_daj_single_row_question
from ..sole_trader.journals.cj import make_cj_activity_question as _st_make_cj_activity_question
from ..sole_trader.journals.cj import make_cj_exam_style_question as _st_make_cj_exam_style_question
from ..sole_trader.journals.cj import make_cj_single_row_question as _st_make_cj_single_row_question
from ..sole_trader.journals.caj import make_caj_activity_question as _st_make_caj_activity_question
from ..sole_trader.journals.caj import make_caj_exam_style_question as _st_make_caj_exam_style_question
from ..sole_trader.journals.caj import make_caj_single_row_question as _st_make_caj_single_row_question
from ..sole_trader.journals.pcj import make_pcj_single_row_question as _st_make_pcj_single_row_question
from ..sole_trader.journals.pcj import make_pcj_activity11_question as _st_make_pcj_activity11_question
from ..sole_trader.journals.pcj import make_pcj_exam_style_question as _st_make_pcj_exam_style_question
from ..sole_trader.journals.gj import make_gj_single_row_question as _st_make_gj_single_row_question
from ..sole_trader.journals.gj import make_gj_activity13_question as _st_make_gj_activity13_question
from ..sole_trader.journals.gj import make_gj_exam_style_question as _st_make_gj_exam_style_question

from ..sole_trader.full_accounting_cycle_project import (
    make_full_accounting_cycle_project_question as _st_make_full_accounting_cycle_project_question,
)

from ..sole_trader.trial_balance_structured import (
    make_trial_balance_control_balance_question as _st_make_trial_balance_control_balance_question,
)
from ..sole_trader.trial_balance_structured import (
    make_trial_balance_from_balances_question as _st_make_trial_balance_from_balances_question,
)
from ..sole_trader.trial_balance_structured import (
    make_trial_balance_partial_completion_question as _st_make_trial_balance_partial_completion_question,
)

from .sole_trader_concepts_equation import make_unified_concepts_question as _phase2_make_unified_concepts_question
from .sole_trader_generation_dispatch import apply_generation_postprocessing as _phase3_apply_generation_postprocessing
from .sole_trader_generation_dispatch import build_direct_dispatched_subskill_questions as _phase3_build_direct_dispatched_subskill_questions
from .sole_trader_generation_dispatch import select_questions_from_pool as _phase3_select_questions_from_pool
from .sole_trader_ledger_general import make_general_ledger_posting_question as _phase1_make_general_ledger_posting_question
from .sole_trader_ledger_subsidiary import make_creditors_ledger_posting_question as _phase1_make_creditors_ledger_posting_question
from .sole_trader_ledger_subsidiary import make_debtors_ledger_posting_question as _phase1_make_debtors_ledger_posting_question
from .sole_trader_pool_assembly import build_generation_pools_by_subskill as _phase3_build_generation_pools_by_subskill
from .sole_trader_transaction_analysis_orchestration import make_transaction_analysis_question as _phase2_make_transaction_analysis_question

def _make_unified_concepts_question(*, r: random.Random) -> Dict[str, Any]:
    return _phase2_make_unified_concepts_question(r=r)

def _make_transaction_analysis_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _phase2_make_transaction_analysis_question(r=r, difficulty=difficulty, mode=mode)

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
        "Fol.",
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


def _ledger_expected_text(value: Any) -> str:
    if isinstance(value, list):
        return " or ".join(str(v) for v in value if str(v).strip())
    return "" if value is None else str(value)


def _build_gl_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    account_name: str,
    transaction_line: str,
    row_role: str,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = _ledger_expected_text(expected)
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


def _build_running_ledger_teaching_hint(
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
    expected_text = _ledger_expected_text(expected)
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


def _make_ledger_posting_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    return _phase1_make_general_ledger_posting_question(r=r, difficulty=difficulty, mode=mode)


def _make_debtors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _phase1_make_debtors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode)


def _make_creditors_ledger_posting_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _phase1_make_creditors_ledger_posting_question(r=r, difficulty=difficulty, mode=mode)


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
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _st_make_control_account_study_table(r=r, variant=variant, business=business)


def _make_control_account_study_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _st_make_control_account_study_question(r=r, difficulty=difficulty, mode=mode, variant=variant, business=business)


def _make_control_accounts_reconciliation_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _st_make_control_accounts_reconciliation_question(r=r, difficulty=difficulty, mode=mode, variant=variant, business=business)


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


def _make_trial_balance_from_balances_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trial_balance_from_balances_question(r=r, difficulty=difficulty, mode=mode)


def _make_trial_balance_partial_completion_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trial_balance_partial_completion_question(r=r, difficulty=difficulty, mode=mode)


def _make_trial_balance_control_balance_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    return _st_make_trial_balance_control_balance_question(r=r, difficulty=difficulty, mode=mode)


def _make_control_accounts_internal_control_typed(
    *, r: random.Random, variant: str = "debtors", business: Optional[str] = None
) -> Dict[str, Any]:
    return _st_make_control_accounts_internal_control_typed(r=r, variant=variant, business=business)


def _make_control_accounts_opening_balance_calc(
    *,
    r: random.Random,
    difficulty: str = "easy",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _st_make_control_accounts_opening_balance_calc(r=r, difficulty=difficulty, variant=variant, business=business)


def _make_control_accounts_analysis_typed(
    *,
    r: random.Random,
    difficulty: str = "medium",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _st_make_control_accounts_analysis_typed(r=r, difficulty=difficulty, variant=variant, business=business)


def generate_questions(*, r: random.Random, n: int, subskill: str = "", difficulty: str = "", mode: str = "", variant: str = "") -> List[Dict[str, Any]]:
    out_list = _generate_questions_internal(r=r, n=n, subskill=subskill, difficulty=difficulty, mode=mode, variant=variant)
    return _phase3_apply_generation_postprocessing(out_list)

def _generate_questions_internal(*, r: random.Random, n: int, subskill: str = "", difficulty: str = "", mode: str = "", variant: str = "") -> List[Dict[str, Any]]:
    subskill_norm = str(subskill or "").strip().lower()
    qtype_norm = str(variant or "").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    var_norm = str(variant or "").strip().lower()

    builders = {
        "make_unified_concepts_question": _make_unified_concepts_question,
        "make_transaction_analysis_question": _make_transaction_analysis_question,
        "make_crj_single_row_question": _st_make_crj_single_row_question,
        "make_crj_activity5_question": _st_make_crj_activity5_question,
        "make_crj_exam_style_question": _st_make_crj_exam_style_question,
        "make_cpj_single_row_question": _st_make_cpj_single_row_question,
        "make_cpj_activity5_question": _st_make_cpj_activity5_question,
        "make_cpj_exam_style_question": _st_make_cpj_exam_style_question,
        "make_dj_single_row_question": _st_make_dj_single_row_question,
        "make_dj_activity_question": _st_make_dj_activity_question,
        "make_dj_exam_style_question": _st_make_dj_exam_style_question,
        "make_daj_single_row_question": _st_make_daj_single_row_question,
        "make_daj_activity_question": _st_make_daj_activity_question,
        "make_daj_exam_style_question": _st_make_daj_exam_style_question,
        "make_cj_single_row_question": _st_make_cj_single_row_question,
        "make_cj_activity_question": _st_make_cj_activity_question,
        "make_cj_exam_style_question": _st_make_cj_exam_style_question,
        "make_caj_single_row_question": _st_make_caj_single_row_question,
        "make_caj_activity_question": _st_make_caj_activity_question,
        "make_caj_exam_style_question": _st_make_caj_exam_style_question,
        "make_pcj_single_row_question": _st_make_pcj_single_row_question,
        "make_pcj_activity11_question": _st_make_pcj_activity11_question,
        "make_pcj_exam_style_question": _st_make_pcj_exam_style_question,
        "make_gj_single_row_question": _st_make_gj_single_row_question,
        "make_gj_activity13_question": _st_make_gj_activity13_question,
        "make_gj_exam_style_question": _st_make_gj_exam_style_question,
        "make_ledger_posting_question": _make_ledger_posting_question,
        "make_debtors_ledger_posting_question": _make_debtors_ledger_posting_question,
        "make_creditors_ledger_posting_question": _make_creditors_ledger_posting_question,
        "make_trial_balance_from_balances_question": _make_trial_balance_from_balances_question,
        "make_trial_balance_partial_completion_question": _make_trial_balance_partial_completion_question,
        "make_trial_balance_control_balance_question": _make_trial_balance_control_balance_question,
        "make_typed": _make_typed,
        "make_trading_stock_prepare_from_journals_question": _make_trading_stock_prepare_from_journals_question,
        "make_trading_stock_prepare_from_casted_journals_question": _make_trading_stock_prepare_from_casted_journals_question,
        "make_trading_stock_fill_missing_details_question": _make_trading_stock_fill_missing_details_question,
        "make_trading_stock_activity16_analysis_typed": _make_trading_stock_activity16_analysis_typed,
        "make_trading_stock_section3_analysis_typed": _make_trading_stock_section3_analysis_typed,
        "make_trading_stock_prepare_with_two_returns_percent_question": _make_trading_stock_prepare_with_two_returns_percent_question,
        "make_trading_stock_markup_trade_discount_typed": _make_trading_stock_markup_trade_discount_typed,
        "make_trading_stock_prepare_with_returns_percent_question": _make_trading_stock_prepare_with_returns_percent_question,
        "make_trading_stock_prepare_with_discount_calc_question": _make_trading_stock_prepare_with_discount_calc_question,
        "make_full_accounting_cycle_project_question": _st_make_full_accounting_cycle_project_question,
        "make_control_account_study_question": _make_control_account_study_question,
        "make_control_accounts_reconciliation_question": _make_control_accounts_reconciliation_question,
        "make_reconciliation_impact_matrix_question": _make_reconciliation_impact_matrix_question,
        "make_control_accounts_internal_control_typed": _make_control_accounts_internal_control_typed,
        "make_control_accounts_opening_balance_calc": _make_control_accounts_opening_balance_calc,
        "make_control_accounts_analysis_typed": _make_control_accounts_analysis_typed,
    }

    pools_by_subskill = _phase3_build_generation_pools_by_subskill(
        r=r,
        difficulty=difficulty,
        mode_norm=mode_norm,
        build_pools_by_subskill=_build_pools_by_subskill,
        builders=builders,
    )

    pool = pools_by_subskill.get(subskill_norm, pools_by_subskill["mixed"])

    direct_questions = _phase3_build_direct_dispatched_subskill_questions(
        subskill_norm=subskill_norm,
        total_count=n,
        var_norm=var_norm,
        r=r,
        difficulty=difficulty,
        mode_norm=mode_norm,
        builders=builders,
    )
    if direct_questions is not None:
        return direct_questions

    return _phase3_select_questions_from_pool(
        items=pool,
        qtype_norm=qtype_norm,
        total_count=n,
        r=r,
    )
