from __future__ import annotations

import random

from typing import Any, Callable, Dict, List, Tuple

from .sole_trader_transaction_analysis import build_transaction_analysis_template_bank
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_bad_debt_recovered
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_bad_debt_writeoff
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_bank_charges
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_capital_contribution
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_cash_sales_cost
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_credit_sales_cost
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_creditor_allowance_return
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_creditor_payment_discount_received
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_debtor_allowance_return
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_debtor_settlement_discount
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_debtor_settlement_discount_unfavourable_bank
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_drawings_stock_cost
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_fee_income_on_credit
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_insurance_accrued
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_insolvent_debtor_dividend_writeoff
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_interest_income
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_interest_on_overdue
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_loan_received
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_loan_repayment_with_interest
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_purchase_by_cheque_trade_discount
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_purchase_on_credit_trade_discount
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_rd_cheque_cancel_discount
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_rent_received


def build_transaction_analysis_question_seed_context(
    *,
    r: random.Random,
    pick_business_name: Callable[..., str],
    pick_person_name: Callable[..., str],
) -> Dict[str, Any]:
    business = pick_business_name(r=r)
    debtor = pick_person_name(r=r)
    creditor = pick_business_name(r=r)
    markup_pct = float(r.choice([25.0, 40.0, 50.0, 60.0, 65.0, 70.0, 75.0, 80.0, 150.0]))
    selling_factor = 1.0 + (markup_pct / 100.0)
    return {
        "business": business,
        "debtor": debtor,
        "creditor": creditor,
        "markup_pct": markup_pct,
        "selling_factor": selling_factor,
    }


def pick_transaction_analysis_schema(*, r: random.Random) -> str:
    return str(
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


def build_transaction_analysis_template_bank_with_core_wrappers(
    *,
    r: random.Random,
    pick_amount: Callable[[List[Any]], float],
    round_money: Callable[[float], float],
    selling_factor: float,
    fmt_money: Callable[[float], str],
    tx_builder: Callable[..., Dict[str, Any]],
    debtor: str,
    markup_pct: float,
    make_petty_cash_on_behalf_of_debtor: Callable[..., List[Dict[str, Any]]],
    make_overdraft_interest: Callable[..., List[Dict[str, Any]]],
) -> List[Tuple[str, str, List[Dict[str, Any]]]]:
    def _make_cash_sales_cost(*, cost: float, nr: str, source: str = "Cash register roll", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_cash_sales_cost(
            tx_builder=tx_builder,
            round_money=round_money,
            selling_factor=selling_factor,
            markup_pct=markup_pct,
            cost=cost,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_credit_sales_cost(*, cost: float, nr: str, source: str = "Duplicate invoice", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_credit_sales_cost(
            tx_builder=tx_builder,
            round_money=round_money,
            selling_factor=selling_factor,
            markup_pct=markup_pct,
            cost=cost,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_debtor_settlement_discount(*, owed: float, disc_pct: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_debtor_settlement_discount(
            tx_builder=tx_builder,
            round_money=round_money,
            fmt_money=fmt_money,
            owed=owed,
            disc_pct=disc_pct,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_rd_cheque_cancel_discount(*, bank_amt: float, disc: float, nr: str, source: str = "Bank statement", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_rd_cheque_cancel_discount(
            tx_builder=tx_builder,
            fmt_money=fmt_money,
            bank_amt=bank_amt,
            disc=disc,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_creditor_payment_discount_received(*, owed: float, disc_pct: float, nr: str, source: str = "Cheque counterfoil", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_creditor_payment_discount_received(
            tx_builder=tx_builder,
            round_money=round_money,
            owed=owed,
            disc_pct=disc_pct,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_purchase_on_credit_trade_discount(*, gross: float, td_pct: float, nr: str, source: str = "Original invoice", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_purchase_on_credit_trade_discount(
            tx_builder=tx_builder,
            round_money=round_money,
            gross=gross,
            td_pct=td_pct,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_purchase_by_cheque_trade_discount(*, gross: float, td_pct: float, nr: str, source: str = "Cheque counterfoil", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_purchase_by_cheque_trade_discount(
            tx_builder=tx_builder,
            round_money=round_money,
            fmt_money=fmt_money,
            gross=gross,
            td_pct=td_pct,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_bank_charges(*, amt: float, nr: str, source: str = "Bank statement", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_bank_charges(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_interest_income(*, amt: float, nr: str, source: str = "Bank statement", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_interest_income(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_rent_received(*, amt: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_rent_received(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_loan_received(*, amt: float, nr: str, source: str = "Bank statement", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_loan_received(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_loan_repayment_with_interest(*, repayment: float, rate_pct: float, months: int, nr: str, source: str = "EFT", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_loan_repayment_with_interest(
            tx_builder=tx_builder,
            round_money=round_money,
            repayment=repayment,
            rate_pct=rate_pct,
            months=months,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_capital_contribution(*, amt: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_capital_contribution(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_drawings_stock_cost(*, cost: float, nr: str, source: str = "Journal voucher", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_drawings_stock_cost(
            tx_builder=tx_builder,
            cost=cost,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_bad_debt_writeoff(*, amt: float, nr: str, source: str = "Journal voucher", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_bad_debt_writeoff(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_bad_debt_recovered(*, amt: float, nr: str, source: str = "Duplicate receipt", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_bad_debt_recovered(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_fee_income_on_credit(*, amt: float, nr: str, source: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_fee_income_on_credit(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
            source=source,
        )

    def _make_debtor_allowance_return(*, selling_price: float, cost_price: float, nr: str, source: str = "Duplicate credit note", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_debtor_allowance_return(
            tx_builder=tx_builder,
            selling_price=selling_price,
            cost_price=cost_price,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_creditor_allowance_return(*, cost_price: float, td_pct: float, nr: str, source: str = "Duplicate debit note", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_creditor_allowance_return(
            tx_builder=tx_builder,
            round_money=round_money,
            cost_price=cost_price,
            td_pct=td_pct,
            nr=nr,
            source=source,
            journal=journal,
        )

    def _make_interest_on_overdue(*, principal: float, rate_pct: float, months: int, nr: str, kind: str, source: str = "Journal voucher", journal: str = "") -> List[Dict[str, Any]]:
        return make_transaction_analysis_interest_on_overdue(
            tx_builder=tx_builder,
            round_money=round_money,
            principal=principal,
            rate_pct=rate_pct,
            months=months,
            nr=nr,
            kind=kind,
            source=source,
            journal=journal,
        )

    def _make_insurance_accrued(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        return make_transaction_analysis_insurance_accrued(
            tx_builder=tx_builder,
            amt=amt,
            nr=nr,
        )

    def _make_insolvent_debtor_dividend_writeoff(*, owed: float, cents_in_rand: float, nr: str, source: str = "Bank statement") -> List[Dict[str, Any]]:
        return make_transaction_analysis_insolvent_debtor_dividend_writeoff(
            tx_builder=tx_builder,
            round_money=round_money,
            fmt_money=fmt_money,
            owed=owed,
            cents_in_rand=cents_in_rand,
            nr=nr,
            source=source,
        )

    def _make_debtor_settlement_discount_unfavourable_bank(*, owed: float, disc_pct: float, nr: str) -> List[Dict[str, Any]]:
        return make_transaction_analysis_debtor_settlement_discount_unfavourable_bank(
            tx_builder=tx_builder,
            round_money=round_money,
            owed=owed,
            disc_pct=disc_pct,
            nr=nr,
        )

    return build_transaction_analysis_template_bank(
        r=r,
        pick_amount=pick_amount,
        round_money=round_money,
        selling_factor=selling_factor,
        fmt_money=fmt_money,
        tx_builder=tx_builder,
        debtor=debtor,
        make_cash_sales_cost=_make_cash_sales_cost,
        make_credit_sales_cost=_make_credit_sales_cost,
        make_debtor_settlement_discount=_make_debtor_settlement_discount,
        make_creditor_payment_discount_received=_make_creditor_payment_discount_received,
        make_bank_charges=_make_bank_charges,
        make_interest_income=_make_interest_income,
        make_rent_received=_make_rent_received,
        make_fee_income_on_credit=_make_fee_income_on_credit,
        make_loan_received=_make_loan_received,
        make_interest_on_overdue=_make_interest_on_overdue,
        make_bad_debt_writeoff=_make_bad_debt_writeoff,
        make_bad_debt_recovered=_make_bad_debt_recovered,
        make_drawings_stock_cost=_make_drawings_stock_cost,
        make_petty_cash_on_behalf_of_debtor=make_petty_cash_on_behalf_of_debtor,
        make_capital_contribution=_make_capital_contribution,
        make_rd_cheque_cancel_discount=_make_rd_cheque_cancel_discount,
        make_loan_repayment_with_interest=_make_loan_repayment_with_interest,
        make_purchase_on_credit_trade_discount=_make_purchase_on_credit_trade_discount,
        make_purchase_by_cheque_trade_discount=_make_purchase_by_cheque_trade_discount,
        make_debtor_allowance_return=_make_debtor_allowance_return,
        make_creditor_allowance_return=_make_creditor_allowance_return,
        make_insolvent_debtor_dividend_writeoff=_make_insolvent_debtor_dividend_writeoff,
        make_debtor_settlement_discount_unfavourable_bank=_make_debtor_settlement_discount_unfavourable_bank,
        make_overdraft_interest=make_overdraft_interest,
    )
