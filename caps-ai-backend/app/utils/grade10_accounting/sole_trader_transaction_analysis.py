from __future__ import annotations

import random

from typing import Any, Callable, Dict, List, Optional, Tuple

from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row

from .sole_trader_concepts_equation import build_transaction_analysis_cell_hint as _build_transaction_analysis_cell_hint
from .sole_trader_concepts_equation import build_transaction_analysis_row_hint as _build_transaction_analysis_row_hint
from .sole_trader_concepts_equation import build_transaction_analysis_teaching_hint as _build_transaction_analysis_teaching_hint
from .sole_trader_concepts_equation import make_transaction_analysis_template_text as _make_transaction_analysis_template_text
from .sole_trader_concepts_equation import transaction_rows_compatible as _transaction_rows_compatible
from .sole_trader_shared import ta_schema_headers as _ta_schema_headers
from .sole_trader_shared import ta_schema_to_row as _ta_schema_to_row
from .sole_trader_transaction_analysis_builders import (
    make_transaction_analysis_bad_debt_recovered,
    make_transaction_analysis_bad_debt_writeoff,
    make_transaction_analysis_bank_charges,
    make_transaction_analysis_bank_fee_breakdown,
    make_transaction_analysis_capital_contribution,
    make_transaction_analysis_cash_handling_fee,
    make_transaction_analysis_cash_sales_cost,
    make_transaction_analysis_cash_withdrawal_for_wages,
    make_transaction_analysis_credit_sales_cost,
    make_transaction_analysis_creditor_allowance_return,
    make_transaction_analysis_creditor_payment_discount_received,
    make_transaction_analysis_debtor_allowance_return,
    make_transaction_analysis_debtor_settlement_discount,
    make_transaction_analysis_debtor_settlement_discount_unfavourable_bank,
    make_transaction_analysis_drawings_stock_cost,
    make_transaction_analysis_fee_income_on_credit,
    make_transaction_analysis_fixed_deposit_investment,
    make_transaction_analysis_fixed_deposit_maturity,
    make_transaction_analysis_insolvent_debtor_dividend_writeoff,
    make_transaction_analysis_insurance_accrued,
    make_transaction_analysis_interest_income,
    make_transaction_analysis_interest_on_current_account,
    make_transaction_analysis_interest_on_overdue,
    make_transaction_analysis_loan_received,
    make_transaction_analysis_loan_repayment_with_interest,
    make_transaction_analysis_overdraft_interest,
    make_transaction_analysis_owner_taking_stock,
    make_transaction_analysis_owner_withdrawal,
    make_transaction_analysis_packing_materials_unfavourable,
    make_transaction_analysis_petty_cash_imprest_restoration,
    make_transaction_analysis_petty_cash_on_behalf_of_debtor,
    make_transaction_analysis_postage_paid,
    make_transaction_analysis_purchase_by_cheque_trade_discount,
    make_transaction_analysis_purchase_on_credit_trade_discount,
    make_transaction_analysis_rd_cheque_cancel_discount,
    make_transaction_analysis_rent_received,
    make_transaction_analysis_vehicle_purchase_on_credit,
)


def build_transaction_analysis_line_map(transaction_lines: List[str]) -> Dict[str, str]:
    return {
        str(line.partition(". ")[0]).strip(): str(line).strip()
        for line in transaction_lines
        if str(line.partition(". ")[0]).strip()
    }


def build_transaction_analysis_schema_settings(schema: str) -> Dict[str, Any]:
    requires_source = schema in {"activity23", "activity24", "source_gl_amount_aol"}
    requires_journal = schema in {"journal_gl_amount_aol"}
    requires_internal = schema in {"internal_gl_amount_aol"}
    requires_subledger = schema in {"gl_subledger_amount_aol"}
    has_amount = schema in {"activity24", "gl_amount_aol", "source_gl_amount_aol", "journal_gl_amount_aol", "internal_gl_amount_aol"}
    if schema == "gl_subledger_amount_aol":
        has_amount = True
    return {
        "requires_source": requires_source,
        "requires_journal": requires_journal,
        "requires_internal": requires_internal,
        "requires_subledger": requires_subledger,
        "has_amount": has_amount,
    }


def resolve_transaction_analysis_schema_and_bank(
    *,
    schema: str,
    template_bank: List[Tuple[str, str, List[Dict[str, Any]]]],
) -> Dict[str, Any]:
    settings = build_transaction_analysis_schema_settings(schema)
    compatible_bank = [
        (a0, name0, rows0)
        for (a0, name0, rows0) in template_bank
        if _transaction_rows_compatible(
            rows=rows0,
            requires_source=bool(settings["requires_source"]),
            requires_journal=bool(settings["requires_journal"]),
            requires_internal=bool(settings["requires_internal"]),
            requires_subledger=bool(settings["requires_subledger"]),
            has_amount=bool(settings["has_amount"]),
        )
    ]
    if not compatible_bank:
        schema = "gl_amount_aol"
        settings = build_transaction_analysis_schema_settings(schema)
        compatible_bank = [
            (a0, name0, rows0)
            for (a0, name0, rows0) in template_bank
            if _transaction_rows_compatible(
                rows=rows0,
                requires_source=bool(settings["requires_source"]),
                requires_journal=bool(settings["requires_journal"]),
                requires_internal=bool(settings["requires_internal"]),
                requires_subledger=bool(settings["requires_subledger"]),
                has_amount=bool(settings["has_amount"]),
            )
        ]
    out = {"schema": schema, "compatible_bank": compatible_bank}
    out.update(settings)
    return out


def build_transaction_analysis_prompt(
    *,
    schema: str,
    business: str,
    markup_pct: float,
    debtor: str,
    creditor: str,
) -> str:
    if schema == "activity23":
        return (
            f"{business}\n\n"
            "Required:\n"
            "Analyse the following transactions under the headings provided. Indicate the General Ledger accounts debited/credited and the effect on the accounting equation.\n"
            "Use + for an increase, - for a decrease and 0 for no change. Assume that the bank has a favourable bank balance."
        )
    if schema == "activity24":
        return (
            f"{business}\n\n"
            "Required:\n"
            "Analyse the following transactions under the headings provided. Indicate the General Ledger accounts debited/credited and the effect on the accounting equation.\n"
            "Use + for an increase, - for a decrease and 0 for no change. Assume that the bank has a favourable bank balance.\n\n"
            f"Note: The business mark-up is {int(markup_pct)}% on cost where applicable."
        )
    return (
        f"{business}\n\n"
        "Required:\n"
        "Analyse the transactions according to the format provided.\n"
        "Use + for an increase, - for a decrease and 0 for no change.\n\n"
        f"Note: Mark-up on cost is {int(markup_pct)}% where applicable. Debtor: {debtor}. Creditor: {creditor}."
    )


def build_transaction_analysis_display_setup(
    *,
    schema: str,
    difficulty: str,
    mode: str,
    business: str,
    markup_pct: float,
    debtor: str,
    creditor: str,
    editable_cols_builder: Callable[..., List[int]],
) -> Dict[str, Any]:
    headers = _ta_schema_headers(schema)
    editable_cols = editable_cols_builder(
        difficulty=difficulty,
        base_editable_cols=list(range(len(headers))),
        total_cols=len(headers),
        mode=mode,
    )
    guidelines = [
        "Use + for an increase, - for a decrease and 0 for no change.",
        "Some transactions require two entries (e.g. Sales and Cost of sales, discounts, R/D).",
        "Assume Bank is favourable unless stated otherwise.",
    ]
    prompt = build_transaction_analysis_prompt(
        schema=schema,
        business=business,
        markup_pct=markup_pct,
        debtor=debtor,
        creditor=creditor,
    )
    return {
        "headers": headers,
        "editable_cols": editable_cols,
        "guidelines": guidelines,
        "prompt": prompt,
    }


def add_transaction_analysis_source_and_tail_templates(
    *,
    r: random.Random,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    tx_builder: Callable[..., Dict[str, Any]],
    make_bank_charges: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount: Callable[..., List[Dict[str, Any]]],
    make_cash_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_insolvent_debtor_dividend_writeoff: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount_unfavourable_bank: Callable[..., List[Dict[str, Any]]],
    make_overdraft_interest: Callable[..., List[Dict[str, Any]]],
) -> None:
    chg_amt = float(pick_amount([270, 380, 550]))
    add_template("arch_23", "bank_charges_source", make_bank_charges(amt=chg_amt, nr="35", source="Bank statement"))
    loan_amt0 = float(pick_amount([30000, 50000]))
    add_template("arch_23", "loan_received_source", [tx_builder(nr="36", source="Bank statement", journal="", dr="Bank", cr="Loan", amount=loan_amt0, a=+loan_amt0, o=0.0, l=+loan_amt0)])
    add_template("arch_23", "debtor_settlement_discount_source", make_debtor_settlement_discount(owed=pick_amount([3500, 5660]), disc_pct=float(r.choice([5.0, 10.0])), nr="37", source="Duplicate receipt", journal="CRJ"))

    equip_credit_amt = float(pick_amount([10000, 6900, 2400]))
    add_template("arch_24", "equipment_credit", [tx_builder(nr="38", source="Original invoice", journal="CJ", dr="Equipment", cr="Creditors control", amount=equip_credit_amt, a=+equip_credit_amt, o=0.0, l=+equip_credit_amt)])
    add_template("arch_24", "cash_sales_cost", make_cash_sales_cost(cost=pick_amount([3000, 8600]), nr="39", source="Cash register roll", journal="CRJ"))

    insol_owed = float(pick_amount([4000, 5200, 6000, 8000, 10000]))
    insol_cents = float(r.choice([25.0, 30.0, 35.0, 40.0, 50.0]))
    add_template(
        "arch_6",
        "insolvent_debtor_dividend_writeoff",
        make_insolvent_debtor_dividend_writeoff(owed=insol_owed, cents_in_rand=insol_cents, nr="14a", source="Bank statement"),
    )

    owed_unfav = float(pick_amount([2800, 3500, 5000]))
    disc_unfav = float(r.choice([2.0, 5.0, 10.0]))
    add_template("arch_12", "debtor_settlement_discount_unfavourable", make_debtor_settlement_discount_unfavourable_bank(owed=owed_unfav, disc_pct=disc_unfav, nr="14c"))
    add_template("arch_20", "overdraft_interest", make_overdraft_interest(amt=float(pick_amount([66, 200, 350, 700])), nr="14d"))


def add_transaction_analysis_mid_bank_templates(
    *,
    r: random.Random,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    round_money: Callable[[float], float],
    selling_factor: float,
    fmt_money: Callable[[float], str],
    tx_builder: Callable[..., Dict[str, Any]],
    make_credit_sales_cost: Callable[..., List[Dict[str, Any]]],
) -> None:
    t11_amt = float(round_money(3500 * 0.9 + 420))
    t11 = tx_builder(nr="29", source="Original invoice", journal="", dr="Trading stock", cr="Creditors control", amount=t11_amt, a=+t11_amt, o=0.0, l=+t11_amt)
    t11["sub_dr"] = ""
    t11["sub_cr"] = "JB Traders"
    add_template("arch_11", "stock_credit_with_delivery_subledger", [t11])

    t11b_cost = float(round_money(9100 / selling_factor))
    t11b_rows = make_credit_sales_cost(cost=t11b_cost, nr="30", source="Duplicate invoice", journal="DJ")
    t11b_rows[0]["sub_dr"] = "N Costa"
    t11b_rows[0]["sub_cr"] = ""
    t11b_rows[1]["sub_dr"] = ""
    t11b_rows[1]["sub_cr"] = ""
    add_template("arch_11", "credit_sale_subledger", t11b_rows)

    add_template(
        "arch_13",
        "stationery_error_correction",
        [
            (lambda _amt: dict(tx_builder(nr="31", source="Journal voucher", journal="GJ", dr="Stationery", cr="Trading stock", amount=_amt, a=-_amt, o=-_amt, l=0.0), tag="stationery_error_correction"))(float(pick_amount([1250])))
        ],
    )
    add_template(
        "arch_13",
        "equipment_return_damaged",
        [
            (lambda _amt: dict(tx_builder(nr="32", source="Duplicate debit note", journal="CAJ", dr="Creditors control", cr="Equipment", amount=_amt, a=-_amt, o=0.0, l=-_amt), tag="equipment_return_damaged"))(float(pick_amount([6900, 8000, 10000])))
        ],
    )

    rent_eft_amt = float(pick_amount([4680, 5000]))
    add_template("arch_19", "rent_received_eft", [tx_builder(nr="33", internal="EFT", journal="CRJ", dr="Bank", cr="Rent income", amount=rent_eft_amt, a=+rent_eft_amt, o=+rent_eft_amt, l=0.0)])
    cons_amt = float(pick_amount([210, 300, 450]))
    add_template("arch_19", "consumable_petty_cash", [tx_builder(nr="34", source="Petty cash voucher", journal="PCJ", dr="Consumable stores", cr="Petty cash", amount=cons_amt, a=-cons_amt, o=-cons_amt, l=0.0)])


def add_transaction_analysis_early_bank_templates(
    *,
    r: random.Random,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    tx_builder: Callable[..., Dict[str, Any]],
    debtor: str,
    make_interest_income: Callable[..., List[Dict[str, Any]]],
    make_rent_received: Callable[..., List[Dict[str, Any]]],
    make_fee_income_on_credit: Callable[..., List[Dict[str, Any]]],
    make_loan_received: Callable[..., List[Dict[str, Any]]],
    make_interest_on_overdue: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_writeoff: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_recovered: Callable[..., List[Dict[str, Any]]],
    make_drawings_stock_cost: Callable[..., List[Dict[str, Any]]],
    make_petty_cash_on_behalf_of_debtor: Callable[..., List[Dict[str, Any]]],
    make_capital_contribution: Callable[..., List[Dict[str, Any]]],
) -> None:
    add_template("arch_6", "interest_income_crj", make_interest_income(amt=pick_amount([110, 130, 520, 800, 1000]), nr="7", source="Bank statement", journal="CRJ"))
    add_template("arch_5", "rent_received_crj", make_rent_received(amt=pick_amount([4680, 5000]), nr="8", source="Duplicate receipt", journal="CRJ"))

    fee_amt = float(pick_amount([250, 350, 420, 560, 900, 1200]))
    add_template("arch_10", "fee_income_credit", make_fee_income_on_credit(amt=fee_amt, nr="8a", source=""))
    add_template("arch_11", "fee_income_credit", make_fee_income_on_credit(amt=fee_amt, nr="8a", source=""))

    add_template("arch_1", "loan_received_crj", make_loan_received(amt=pick_amount([30000, 50000, 220000]), nr="9", source="Bank statement", journal="CRJ"))
    add_template("arch_17", "insurance_accrued_gj", [tx_builder(nr="10", source="Journal voucher", journal="GJ", dr="Insurance", cr="Accrued expense", amount=float(900), a=0.0, o=-900.0, l=+900.0)])
    add_template("arch_9", "interest_overdue_debtor_gj", make_interest_on_overdue(principal=pick_amount([4800, 3000, 900]), rate_pct=float(r.choice([2.5, 10.0, 12.0])), months=int(r.choice([1, 2, 3, 4])), nr="11", kind="debtor", source="Journal voucher", journal="GJ"))
    add_template("arch_25", "bad_debt_writeoff_gj", make_bad_debt_writeoff(amt=pick_amount([550, 750, 880, 2160, 2600]), nr="12", source="Journal voucher", journal="GJ"))
    add_template("arch_3", "bad_debt_recovered_crj", make_bad_debt_recovered(amt=pick_amount([150, 400, 540, 1800]), nr="13", source="Duplicate receipt", journal="CRJ"))
    add_template("arch_22", "drawings_stock_gj", make_drawings_stock_cost(cost=pick_amount([300, 400, 850, 1350, 7600, 15000]), nr="14", source="Journal voucher", journal="GJ"))

    petty_on_behalf_amt = float(pick_amount([210, 300, 450, 560, 700]))
    add_template("arch_2", "petty_cash_on_behalf_debtor", make_petty_cash_on_behalf_of_debtor(amt=petty_on_behalf_amt, nr="14b", debtor_name=debtor))
    add_template("arch_8", "capital_contribution_crj", make_capital_contribution(amt=pick_amount([20000, 40000, 100000, 120000]), nr="15", source="Duplicate receipt", journal="CRJ"))


def add_transaction_analysis_top_bank_templates(
    *,
    r: random.Random,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    make_cash_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_credit_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount: Callable[..., List[Dict[str, Any]]],
    make_creditor_payment_discount_received: Callable[..., List[Dict[str, Any]]],
    make_bank_charges: Callable[..., List[Dict[str, Any]]],
) -> Dict[str, float]:
    add_template("activity23", "cash_sales_crj", make_cash_sales_cost(cost=pick_amount([1200, 2000, 3000, 4800, 8600]), nr="1", source="Cash register roll", journal="CRJ"))
    add_template("activity24", "cash_sales_crj", make_cash_sales_cost(cost=pick_amount([1200, 1800, 3000]), nr="1", source="Cash register roll", journal="CRJ"))

    add_template("arch_10", "credit_sales_dj", make_credit_sales_cost(cost=pick_amount([500, 700, 1500, 2100, 2500]), nr="2", source="Duplicate invoice", journal="DJ"))
    add_template("arch_16", "credit_sales_dj", make_credit_sales_cost(cost=pick_amount([500, 700, 1500, 2100]), nr="2", source="Duplicate invoice", journal="DJ"))

    owed0 = float(pick_amount([850, 1100, 1950, 3000, 3500, 5000, 7200]))
    disc_pct0 = float(r.choice([2.5, 4.0, 5.0, 10.0]))
    add_template("activity23", "debtor_settlement_crj", make_debtor_settlement_discount(owed=owed0, disc_pct=disc_pct0, nr="3", source="Duplicate receipt", journal="CRJ"))
    add_template("arch_17", "debtor_settlement_crj", make_debtor_settlement_discount(owed=owed0, disc_pct=disc_pct0, nr="3", source="Duplicate receipt", journal="CRJ"))

    owed1 = float(pick_amount([3000, 5000, 645, 8500, 13500]))
    disc_pct1 = float(r.choice([4.0, 5.0, 10.0]))
    add_template(
        "arch_20",
        "creditor_payment_cpj",
        make_creditor_payment_discount_received(
            owed=owed1,
            disc_pct=disc_pct1,
            nr="4",
            source="Cheque counterfoil",
            journal="CPJ",
        ),
    )

    charges_amt = float(pick_amount([210, 270, 340, 550, 610]))
    add_template("arch_6", "bank_charges_cpj", make_bank_charges(amt=charges_amt, nr="6", source="Bank statement", journal="CPJ"))
    return {
        "owed0": owed0,
        "disc_pct0": disc_pct0,
    }


def add_transaction_analysis_discount_purchase_allowance_templates(
    *,
    r: random.Random,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    round_money: Callable[[float], float],
    selling_factor: float,
    owed0: float,
    disc_pct0: float,
    make_rd_cheque_cancel_discount: Callable[..., List[Dict[str, Any]]],
    make_interest_on_overdue: Callable[..., List[Dict[str, Any]]],
    make_loan_repayment_with_interest: Callable[..., List[Dict[str, Any]]],
    make_purchase_on_credit_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_purchase_by_cheque_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_debtor_allowance_return: Callable[..., List[Dict[str, Any]]],
    make_creditor_allowance_return: Callable[..., List[Dict[str, Any]]],
) -> None:
    disc_amt0 = float(round_money(owed0 * (disc_pct0 / 100.0)))
    bank_amt0 = float(round_money(owed0 - disc_amt0))
    add_template("arch_12", "rd_cheque_gj", make_rd_cheque_cancel_discount(bank_amt=float(bank_amt0), disc=float(disc_amt0), nr="16", source="Bank statement", journal="GJ"))

    principal_c = float(pick_amount([3600, 8400]))
    rate_c = float(r.choice([6.0, 7.0, 18.0]))
    months_c = int(r.choice([2, 3, 4]))
    add_template("arch_9", "interest_overdue_creditor_gj", make_interest_on_overdue(principal=principal_c, rate_pct=rate_c, months=months_c, nr="17", kind="creditor", source="Journal voucher", journal="GJ"))

    repay = float(pick_amount([44000, 30000]))
    repay_rate = float(r.choice([10.0, 15.0, 18.0]))
    repay_months = int(r.choice([4, 12]))
    add_template("arch_14", "loan_repayment_interest_cpj", make_loan_repayment_with_interest(repayment=repay, rate_pct=repay_rate, months=repay_months, nr="18", source="EFT", journal="CPJ"))

    gross_p = float(pick_amount([10800, 14000, 3500, 5670]))
    td_p = float(r.choice([8.0, 10.0, 15.0, 20.0]))
    add_template("arch_15", "purchase_credit_cj", make_purchase_on_credit_trade_discount(gross=gross_p, td_pct=td_p, nr="19", source="Original invoice", journal="CJ"))

    gross_p2 = float(pick_amount([12300, 10000, 6000]))
    td_p2 = float(r.choice([10.0, 15.0, 20.0]))
    add_template("arch_15", "purchase_cheque_cpj", make_purchase_by_cheque_trade_discount(gross=gross_p2, td_pct=td_p2, nr="20", source="Cheque counterfoil", journal="CPJ"))

    cost_ret = float(pick_amount([400, 600, 900, 1200, 1500, 2000]))
    sell_ret = float(round_money(cost_ret * selling_factor))
    add_template("arch_18", "debtor_allowance_daj", make_debtor_allowance_return(selling_price=sell_ret, cost_price=cost_ret, nr="21", source="Duplicate credit note", journal="DAJ"))

    cost_ret2 = float(pick_amount([1200, 1500, 2000, 3500, 5670]))
    td_ret2 = float(r.choice([8.0, 10.0, 15.0, 20.0]))
    add_template("arch_21", "creditor_allowance_caj", make_creditor_allowance_return(cost_price=cost_ret2, td_pct=td_ret2, nr="22", source="Duplicate debit note", journal="CAJ"))


def add_transaction_analysis_asset_and_internal_templates(
    *,
    add_template: Callable[..., None],
    pick_amount: Callable[[List[Any]], float],
    fmt_money: Callable[[float], str],
    tx_builder: Callable[..., Dict[str, Any]],
) -> None:
    equip_amt = float(pick_amount([4500, 6800, 12000, 18500, 25000]))
    add_template(
        "arch_4",
        "equipment_credit_cj",
        [
            tx_builder(
                nr="23",
                source="Original invoice",
                journal="CJ",
                dr="Equipment",
                cr="Creditors control",
                amount=float(equip_amt),
                a=+equip_amt,
                o=0.0,
                l=+equip_amt,
            )
        ],
    )

    equip_cash = float(pick_amount([3500, 4800, 9000, 15000]))
    add_template(
        "arch_4",
        "equipment_cash_cpj",
        [
            (lambda _amt: dict(
                tx_builder(
                    nr="24",
                    source="Cheque counterfoil",
                    journal="CPJ",
                    dr="Equipment",
                    cr="Bank",
                    amount=float(_amt),
                    a=float(_amt),
                    o=0.0,
                    l=0.0,
                ),
                tag="equipment_cash_asset_swap",
                a_override=f"+{fmt_money(float(_amt))}/-{fmt_money(float(_amt))}",
            ))(equip_cash)
        ],
    )

    petty_amt = float(pick_amount([300, 500, 800, 1200, 1500]))
    add_template(
        "arch_7",
        "petty_cash_transfer",
        [
            (lambda _amt: dict(
                tx_builder(
                    nr="25",
                    source="Cheque counterfoil",
                    journal="CPJ",
                    dr="Petty cash",
                    cr="Bank",
                    amount=float(_amt),
                    a=float(_amt),
                    o=0.0,
                    l=0.0,
                ),
                tag="petty_cash_transfer_asset_swap",
                a_override=f"+{fmt_money(float(_amt))}/-{fmt_money(float(_amt))}",
            ))(petty_amt)
        ],
    )

    wages_amt = float(pick_amount([2500, 3600, 4200, 5800]))
    add_template(
        "arch_2",
        "wages_eft_internal",
        [
            tx_builder(
                nr="26",
                internal="EFT",
                journal="CPJ",
                dr="Wages",
                cr="Bank",
                amount=float(wages_amt),
                a=-wages_amt,
                o=-wages_amt,
                l=0.0,
            )
        ],
    )

    rent_paid = float(pick_amount([1800, 2400, 3000, 4500]))
    add_template(
        "arch_2",
        "rent_debit_order_internal",
        [
            tx_builder(
                nr="27",
                internal="Debit order",
                journal="CPJ",
                dr="Rent expense",
                cr="Bank",
                amount=float(rent_paid),
                a=-rent_paid,
                o=-rent_paid,
                l=0.0,
            )
        ],
    )

    ins_paid = float(pick_amount([900, 1200, 1500, 1800]))
    add_template(
        "arch_2",
        "insurance_stop_order_internal",
        [
            tx_builder(
                nr="28",
                internal="Stop order",
                journal="CPJ",
                dr="Insurance",
                cr="Bank",
                amount=float(ins_paid),
                a=-ins_paid,
                o=-ins_paid,
                l=0.0,
            )
        ],
    )


def build_transaction_analysis_tx_pool(
    *,
    r: random.Random,
    pick_amount: Callable[[List[float]], float],
    starting_tx_counter: int,
    make_cash_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_credit_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount: Callable[..., List[Dict[str, Any]]],
    make_creditor_payment_discount_received: Callable[..., List[Dict[str, Any]]],
    make_purchase_on_credit_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_purchase_by_cheque_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_bank_charges: Callable[..., List[Dict[str, Any]]],
    make_interest_income: Callable[..., List[Dict[str, Any]]],
    make_rent_received: Callable[..., List[Dict[str, Any]]],
    make_loan_received: Callable[..., List[Dict[str, Any]]],
    make_loan_repayment_with_interest: Callable[..., List[Dict[str, Any]]],
    make_capital_contribution: Callable[..., List[Dict[str, Any]]],
    make_drawings_stock_cost: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_writeoff: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_recovered: Callable[..., List[Dict[str, Any]]],
    make_interest_on_overdue: Callable[..., List[Dict[str, Any]]],
    make_insurance_accrued: Callable[..., List[Dict[str, Any]]],
    make_insolvent_debtor_dividend_writeoff: Callable[..., List[Dict[str, Any]]],
    make_fee_income_on_credit: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount_unfavourable_bank: Callable[..., List[Dict[str, Any]]],
    make_overdraft_interest: Callable[..., List[Dict[str, Any]]],
    make_fixed_deposit_maturity: Callable[..., List[Dict[str, Any]]],
    make_bank_fee_breakdown: Callable[..., List[Dict[str, Any]]],
    make_owner_withdrawal: Callable[..., List[Dict[str, Any]]],
    make_fixed_deposit_investment: Callable[..., List[Dict[str, Any]]],
    make_petty_cash_imprest_restoration: Callable[..., List[Dict[str, Any]]],
    make_owner_taking_stock: Callable[..., List[Dict[str, Any]]],
    make_interest_on_current_account: Callable[..., List[Dict[str, Any]]],
    make_vehicle_purchase_on_credit: Callable[..., List[Dict[str, Any]]],
    make_cash_handling_fee: Callable[..., List[Dict[str, Any]]],
    make_cash_withdrawal_for_wages: Callable[..., List[Dict[str, Any]]],
    make_packing_materials_unfavourable: Callable[..., List[Dict[str, Any]]],
    make_postage_paid: Callable[..., List[Dict[str, Any]]],
) -> Dict[str, Any]:
    tx_counter = int(starting_tx_counter)
    out: List[Tuple[str, List[Dict[str, Any]]]] = []
    nr = str(tx_counter)
    out.append(("cash_sales_cost", make_cash_sales_cost(cost=pick_amount([900, 1200, 1800, 2000, 3000, 4800, 8600]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("credit_sales_cost", make_credit_sales_cost(cost=pick_amount([500, 700, 1500, 2100, 2500, 4000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    owed = pick_amount([850, 1100, 1950, 3000, 3500, 5000, 7200])
    disc_pct = float(r.choice([2.5, 4.0, 5.0, 10.0]))
    out.append(("debtor_settlement_discount", make_debtor_settlement_discount(owed=owed, disc_pct=disc_pct, nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("creditor_payment_discount_received", make_creditor_payment_discount_received(owed=pick_amount([3000, 5000, 645, 8500, 13500]), disc_pct=float(r.choice([4.0, 5.0, 10.0])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("purchase_credit_trade_discount", make_purchase_on_credit_trade_discount(gross=pick_amount([10800, 14000, 3500, 5670]), td_pct=float(r.choice([8.0, 10.0, 15.0, 20.0])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("purchase_cheque_trade_discount", make_purchase_by_cheque_trade_discount(gross=pick_amount([12300, 10000, 6000]), td_pct=float(r.choice([10.0, 15.0, 20.0])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("bank_charges", make_bank_charges(amt=pick_amount([210, 270, 340, 550, 610]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("interest_income", make_interest_income(amt=pick_amount([110, 130, 520, 800, 1000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("rent_received", make_rent_received(amt=pick_amount([4680, 5000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("loan_received", make_loan_received(amt=pick_amount([30000, 50000, 220000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("loan_repayment_interest", make_loan_repayment_with_interest(repayment=pick_amount([44000, 30000]), rate_pct=float(r.choice([10.0, 15.0, 18.0])), months=int(r.choice([4, 12])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("capital_contribution", make_capital_contribution(amt=pick_amount([20000, 40000, 100000, 120000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("drawings_stock", make_drawings_stock_cost(cost=pick_amount([300, 400, 850, 1350, 7600, 15000]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("bad_debt_writeoff", make_bad_debt_writeoff(amt=pick_amount([550, 750, 880, 2160, 2600]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("bad_debt_recovered", make_bad_debt_recovered(amt=pick_amount([150, 400, 540, 1800]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("interest_overdue_debtor", make_interest_on_overdue(principal=pick_amount([4800, 3000, 900]), rate_pct=float(r.choice([2.5, 10.0, 12.0])), months=int(r.choice([1, 2, 3, 4])), nr=nr, kind="debtor")))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("interest_overdue_creditor", make_interest_on_overdue(principal=pick_amount([3600, 8400]), rate_pct=float(r.choice([6.0, 7.0, 18.0])), months=int(r.choice([2, 3, 4])), nr=nr, kind="creditor")))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("insurance_accrued", make_insurance_accrued(amt=pick_amount([900]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("insolvent_debtor_dividend_writeoff", make_insolvent_debtor_dividend_writeoff(owed=pick_amount([4000, 5200, 6000, 8000, 10000]), cents_in_rand=float(r.choice([25.0, 30.0, 35.0, 40.0, 50.0])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("fee_income_credit", make_fee_income_on_credit(amt=pick_amount([250, 350, 420, 560, 900, 1200]), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    owed_unfav = float(pick_amount([2800, 3500, 5000]))
    disc_unfav = float(r.choice([2.0, 5.0, 10.0]))
    out.append(("debtor_settlement_discount_unfavourable", make_debtor_settlement_discount_unfavourable_bank(owed=owed_unfav, disc_pct=disc_unfav, nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("overdraft_interest", make_overdraft_interest(amt=float(pick_amount([66, 200, 350, 700])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("fixed_deposit_maturity", make_fixed_deposit_maturity(principal=float(pick_amount([5000, 10000, 20000])), rate_pct=float(r.choice([6.0, 8.0, 10.0])), months=int(r.choice([6, 12])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("bank_fee_breakdown", make_bank_fee_breakdown(service_fee=float(pick_amount([100, 150, 200])), cash_handling_fee=float(pick_amount([50, 75, 100])), overdraft_int=float(pick_amount([80, 120, 200])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("owner_withdrawal", make_owner_withdrawal(amt=float(pick_amount([500, 1000, 1500, 2000])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("fixed_deposit_investment", make_fixed_deposit_investment(amt=float(pick_amount([5000, 10000, 15000])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("petty_cash_imprest", make_petty_cash_imprest_restoration(amt=float(pick_amount([500, 800, 1200])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("owner_taking_stock", make_owner_taking_stock(cost=float(pick_amount([300, 500, 750, 1000])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("interest_current_account", make_interest_on_current_account(amt=float(pick_amount([50, 100, 150, 200])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("vehicle_purchase_credit", make_vehicle_purchase_on_credit(amt=float(pick_amount([25000, 45000, 60000, 85000])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("cash_handling_fee", make_cash_handling_fee(amt=float(pick_amount([30, 50, 75, 100])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("cash_withdrawal_wages", make_cash_withdrawal_for_wages(amt=float(pick_amount([1500, 2000, 2800, 3500])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("packing_materials_unfavourable", make_packing_materials_unfavourable(amt=float(pick_amount([400, 600, 850, 1200])), nr=nr)))
    tx_counter += 1
    nr = str(tx_counter)
    out.append(("postage_paid", make_postage_paid(amt=float(pick_amount([45, 80, 120, 180])), nr=nr)))
    tx_counter += 1
    return {"tx_pool": out, "next_tx_counter": tx_counter}


def build_transaction_analysis_template_bank(
    *,
    r: random.Random,
    pick_amount: Callable[[List[Any]], float],
    round_money: Callable[[float], float],
    selling_factor: float,
    fmt_money: Callable[[float], str],
    tx_builder: Callable[..., Dict[str, Any]],
    debtor: str,
    make_cash_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_credit_sales_cost: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount: Callable[..., List[Dict[str, Any]]],
    make_creditor_payment_discount_received: Callable[..., List[Dict[str, Any]]],
    make_bank_charges: Callable[..., List[Dict[str, Any]]],
    make_interest_income: Callable[..., List[Dict[str, Any]]],
    make_rent_received: Callable[..., List[Dict[str, Any]]],
    make_fee_income_on_credit: Callable[..., List[Dict[str, Any]]],
    make_loan_received: Callable[..., List[Dict[str, Any]]],
    make_interest_on_overdue: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_writeoff: Callable[..., List[Dict[str, Any]]],
    make_bad_debt_recovered: Callable[..., List[Dict[str, Any]]],
    make_drawings_stock_cost: Callable[..., List[Dict[str, Any]]],
    make_petty_cash_on_behalf_of_debtor: Callable[..., List[Dict[str, Any]]],
    make_capital_contribution: Callable[..., List[Dict[str, Any]]],
    make_rd_cheque_cancel_discount: Callable[..., List[Dict[str, Any]]],
    make_loan_repayment_with_interest: Callable[..., List[Dict[str, Any]]],
    make_purchase_on_credit_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_purchase_by_cheque_trade_discount: Callable[..., List[Dict[str, Any]]],
    make_debtor_allowance_return: Callable[..., List[Dict[str, Any]]],
    make_creditor_allowance_return: Callable[..., List[Dict[str, Any]]],
    make_insolvent_debtor_dividend_writeoff: Callable[..., List[Dict[str, Any]]],
    make_debtor_settlement_discount_unfavourable_bank: Callable[..., List[Dict[str, Any]]],
    make_overdraft_interest: Callable[..., List[Dict[str, Any]]],
) -> List[tuple[str, str, List[Dict[str, Any]]]]:
    template_bank: List[tuple[str, str, List[Dict[str, Any]]]] = []

    def _add_template(archetype_key: str, name: str, rows0: List[Dict[str, Any]]) -> None:
        template_bank.append((archetype_key, name, rows0))

    top_bank_data = add_transaction_analysis_top_bank_templates(
        r=r,
        add_template=_add_template,
        pick_amount=pick_amount,
        make_cash_sales_cost=make_cash_sales_cost,
        make_credit_sales_cost=make_credit_sales_cost,
        make_debtor_settlement_discount=make_debtor_settlement_discount,
        make_creditor_payment_discount_received=make_creditor_payment_discount_received,
        make_bank_charges=make_bank_charges,
    )
    owed0 = float(top_bank_data["owed0"])
    disc_pct0 = float(top_bank_data["disc_pct0"])

    add_transaction_analysis_early_bank_templates(
        r=r,
        add_template=_add_template,
        pick_amount=pick_amount,
        tx_builder=tx_builder,
        debtor=debtor,
        make_interest_income=make_interest_income,
        make_rent_received=make_rent_received,
        make_fee_income_on_credit=make_fee_income_on_credit,
        make_loan_received=make_loan_received,
        make_interest_on_overdue=make_interest_on_overdue,
        make_bad_debt_writeoff=make_bad_debt_writeoff,
        make_bad_debt_recovered=make_bad_debt_recovered,
        make_drawings_stock_cost=make_drawings_stock_cost,
        make_petty_cash_on_behalf_of_debtor=make_petty_cash_on_behalf_of_debtor,
        make_capital_contribution=make_capital_contribution,
    )
    add_transaction_analysis_discount_purchase_allowance_templates(
        r=r,
        add_template=_add_template,
        pick_amount=pick_amount,
        round_money=round_money,
        selling_factor=selling_factor,
        owed0=owed0,
        disc_pct0=disc_pct0,
        make_rd_cheque_cancel_discount=make_rd_cheque_cancel_discount,
        make_interest_on_overdue=make_interest_on_overdue,
        make_loan_repayment_with_interest=make_loan_repayment_with_interest,
        make_purchase_on_credit_trade_discount=make_purchase_on_credit_trade_discount,
        make_purchase_by_cheque_trade_discount=make_purchase_by_cheque_trade_discount,
        make_debtor_allowance_return=make_debtor_allowance_return,
        make_creditor_allowance_return=make_creditor_allowance_return,
    )
    add_transaction_analysis_asset_and_internal_templates(
        add_template=_add_template,
        pick_amount=pick_amount,
        fmt_money=fmt_money,
        tx_builder=tx_builder,
    )
    add_transaction_analysis_mid_bank_templates(
        r=r,
        add_template=_add_template,
        pick_amount=pick_amount,
        round_money=round_money,
        selling_factor=selling_factor,
        fmt_money=fmt_money,
        tx_builder=tx_builder,
        make_credit_sales_cost=make_credit_sales_cost,
    )
    add_transaction_analysis_source_and_tail_templates(
        r=r,
        add_template=_add_template,
        pick_amount=pick_amount,
        tx_builder=tx_builder,
        make_bank_charges=make_bank_charges,
        make_debtor_settlement_discount=make_debtor_settlement_discount,
        make_cash_sales_cost=make_cash_sales_cost,
        make_insolvent_debtor_dividend_writeoff=make_insolvent_debtor_dividend_writeoff,
        make_debtor_settlement_discount_unfavourable_bank=make_debtor_settlement_discount_unfavourable_bank,
        make_overdraft_interest=make_overdraft_interest,
    )
    return template_bank


def prepare_transaction_analysis_prompt_and_rows(
    *,
    prompt: str,
    picked_templates: List[tuple[str, str, List[Dict[str, Any]]]],
    markup_pct: float,
    debtor: str,
    creditor: str,
) -> Dict[str, Any]:
    flat_txs: List[Dict[str, Any]] = []
    transaction_lines: List[str] = []
    tx_no = 1
    for _a0, name0, rows0 in picked_templates:
        transaction_number = ""
        for t in rows0:
            if str(t.get("nr") or "").strip():
                t["nr"] = str(tx_no)
                transaction_number = str(tx_no)
                tx_no += 1
            flat_txs.append(t)
        if transaction_number:
            transaction_lines.append(
                f"{transaction_number}. "
                f"{_make_transaction_analysis_template_text(name=name0, rows=rows0, markup_pct=markup_pct, debtor=debtor, creditor=creditor)}"
            )
    prompt_out = prompt
    if transaction_lines:
        prompt_out = f"{prompt_out}\n\nTransactions:\n{chr(10).join([''] + transaction_lines)}"
    return {
        "prompt": prompt_out,
        "flat_txs": flat_txs,
        "transaction_lines": transaction_lines,
    }


def pick_transaction_analysis_templates(
    *,
    r: random.Random,
    compatible_bank: List[tuple[str, str, List[Dict[str, Any]]]],
) -> List[tuple[str, str, List[Dict[str, Any]]]]:
    available_archetypes = sorted({a0 for (a0, _n0, _rows0) in compatible_bank})
    archetypes_in_question = r.sample(
        available_archetypes,
        k=min(len(available_archetypes), int(r.choice([3, 4, 5, 6]))),
    )

    picked_templates: List[tuple[str, str, List[Dict[str, Any]]]] = []
    used_names: set[str] = set()
    for akey in archetypes_in_question:
        candidates = [
            (a0, n0, rows0)
            for (a0, n0, rows0) in compatible_bank
            if a0 == akey and n0 not in used_names
        ]
        if not candidates:
            continue
        chosen = r.choice(candidates)
        used_names.add(chosen[1])
        picked_templates.append(chosen)

    target_templates = int(r.choice([6, 7, 8, 9, 10]))
    pool_remaining = [
        (a0, n0, rows0)
        for (a0, n0, rows0) in compatible_bank
        if n0 not in used_names
    ]
    r.shuffle(pool_remaining)
    for item in pool_remaining:
        if len(picked_templates) >= target_templates:
            break
        picked_templates.append(item)
        used_names.add(item[1])
    return picked_templates


def build_transaction_analysis_question_output(
    *,
    r: random.Random,
    schema: str,
    template_bank: List[Tuple[str, str, List[Dict[str, Any]]]],
    difficulty: str,
    mode_norm: str,
    business: str,
    markup_pct: float,
    debtor: str,
    creditor: str,
    editable_cols_builder: Callable[..., List[int]],
) -> Dict[str, Any]:
    schema_resolution = resolve_transaction_analysis_schema_and_bank(
        schema=schema,
        template_bank=template_bank,
    )
    schema = str(schema_resolution["schema"])
    compatible_bank = list(schema_resolution["compatible_bank"])

    display_setup = build_transaction_analysis_display_setup(
        schema=schema,
        difficulty=difficulty,
        mode=mode_norm,
        business=business,
        markup_pct=markup_pct,
        debtor=debtor,
        creditor=creditor,
        editable_cols_builder=editable_cols_builder,
    )
    headers = display_setup["headers"]
    editable_cols = display_setup["editable_cols"]
    guidelines = display_setup["guidelines"]
    prompt = display_setup["prompt"]

    picked_templates = pick_transaction_analysis_templates(
        r=r,
        compatible_bank=compatible_bank,
    )
    prep_data = prepare_transaction_analysis_prompt_and_rows(
        prompt=prompt,
        picked_templates=picked_templates,
        markup_pct=markup_pct,
        debtor=debtor,
        creditor=creditor,
    )
    prompt = prep_data["prompt"]
    flat_txs = prep_data["flat_txs"]
    transaction_lines = prep_data["transaction_lines"]

    render_data = build_transaction_analysis_rows(
        headers=headers,
        editable_cols=editable_cols,
        flat_txs=flat_txs,
        transaction_lines=transaction_lines,
        schema=schema,
        markup_pct=markup_pct,
    )
    header_rows = build_transaction_analysis_header_rows(schema)
    return finalize_transaction_analysis_output(
        prompt=prompt,
        headers=headers,
        rows=render_data["rows"],
        correct_map=render_data["correct_map"],
        guidelines=guidelines,
        mode_norm=mode_norm,
        cell_hints=render_data["cell_hints"],
        header_rows=header_rows,
        cell_teaching_map=render_data["cell_teaching_map"],
        derivation_map=render_data["derivation_map"],
        transaction_lines=transaction_lines,
    )



def build_transaction_analysis_rows(
    *,
    headers: List[str],
    editable_cols: List[int],
    flat_txs: List[Dict[str, Any]],
    transaction_lines: List[str],
    schema: str,
    markup_pct: float,
) -> Dict[str, Any]:
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    derivation_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    editable_col_set = {int(c) for c in (editable_cols or [])}
    tx_line_map = build_transaction_analysis_line_map(transaction_lines)

    current_tx = ""
    for row_i, t in enumerate(flat_txs):
        if str(t.get("nr") or "").strip():
            current_tx = str(t.get("nr"))
        values = _ta_schema_to_row(schema, t)
        row_hint = _build_transaction_analysis_row_hint(
            t=t,
            current_tx=current_tx,
            schema=schema,
            markup_pct=markup_pct,
        )
        transaction_line = tx_line_map.get(current_tx, "")
        display = [
            "" if cix in editable_col_set else ("" if v0 is None else v0)
            for cix, v0 in enumerate(values)
        ]
        rows.append(
            _build_prefixed_row(
                table_index=0,
                row_index=row_i,
                values=display,
                editable_cols=editable_cols,
            )
        )
        for cix, v0 in enumerate(values):
            final_value = "" if v0 is None else v0
            cell_key = f"t0_r{int(row_i)}_c{int(cix)}"
            correct_map[cell_key] = str(final_value)
            header_label = str(headers[cix] or f"Column {cix + 1}")
            cell_hint = _build_transaction_analysis_cell_hint(
                header_label=header_label,
                value=final_value,
                t=t,
                row_hint=row_hint,
            )
            if str(final_value).strip():
                derivation_map[cell_key] = f"Expected {header_label}: {final_value}"
            if cix in editable_col_set:
                teaching_hint = _build_transaction_analysis_teaching_hint(
                    header_label=header_label,
                    value=final_value,
                    t=t,
                    row_hint=row_hint,
                    transaction_line=transaction_line,
                )
                if teaching_hint:
                    cell_teaching_map[cell_key] = teaching_hint
            if str(cell_hint or "").strip():
                cell_hints[cell_key] = str(cell_hint)

    return {
        "rows": rows,
        "correct_map": correct_map,
        "derivation_map": derivation_map,
        "cell_hints": cell_hints,
        "cell_teaching_map": cell_teaching_map,
    }



def build_transaction_analysis_header_rows(schema: str) -> Optional[List[List[Dict[str, Any]]]]:
    if schema != "gl_subledger_amount_aol":
        return None
    return [
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



def finalize_transaction_analysis_output(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, Any],
    guidelines: List[str],
    mode_norm: str,
    cell_hints: Dict[str, str],
    header_rows: Optional[List[List[Dict[str, Any]]]],
    cell_teaching_map: Dict[str, Dict[str, str]],
    derivation_map: Dict[str, Any],
    transaction_lines: List[str],
) -> Dict[str, Any]:
    journal = {
        "journal_type": "accounting_equation_analysis",
        "table_variant": "grade_project",
        "headers": headers,
        "rows": rows,
        "column_help": {},
        "allow_extra_rows": False,
    }
    if header_rows:
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
    out["derivation_map"] = derivation_map
    out["cell_hints"] = cell_hints if cell_hints else None
    out["cell_teaching_map"] = cell_teaching_map if cell_teaching_map else None
    out["transaction_lines"] = transaction_lines
    return out
