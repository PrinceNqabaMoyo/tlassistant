from __future__ import annotations

from typing import Any, Callable, Dict, List


def make_transaction_analysis_bank_charges(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Bank statement",
    journal: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank charges", cr="Bank", amount=float(amt), a=-amt, o=-amt, l=0.0)
    row1["tag"] = "bank_charges_favourable"
    return [row1]


def make_transaction_analysis_interest_income(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Bank statement",
    journal: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Interest income", amount=float(amt), a=+amt, o=+amt, l=0.0)
    row1["tag"] = "interest_income_receipt"
    return [row1]


def make_transaction_analysis_rent_received(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Duplicate receipt",
    journal: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Rent income", amount=float(amt), a=+amt, o=+amt, l=0.0)
    row1["tag"] = "rent_received_income"
    return [row1]


def make_transaction_analysis_loan_received(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Bank statement",
    journal: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Loan", amount=float(amt), a=+amt, o=0.0, l=+amt)
    row1["tag"] = "loan_received"
    return [row1]


def make_transaction_analysis_capital_contribution(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Duplicate receipt",
    journal: str = "",
) -> List[Dict[str, Any]]:
    return [tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Capital", amount=float(amt), a=+amt, o=+amt, l=0.0)]


def make_transaction_analysis_drawings_stock_cost(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    cost: float,
    nr: str,
    source: str = "Journal voucher",
    journal: str = "",
) -> List[Dict[str, Any]]:
    return [tx_builder(nr=nr, source=source, journal=journal, dr="Drawings", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0)]


def make_transaction_analysis_bad_debt_writeoff(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Journal voucher",
    journal: str = "",
) -> List[Dict[str, Any]]:
    return [tx_builder(nr=nr, source=source, journal=journal, dr="Bad debts", cr="Debtors control", amount=float(amt), a=-amt, o=-amt, l=0.0)]


def make_transaction_analysis_bad_debt_recovered(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "Duplicate receipt",
    journal: str = "",
) -> List[Dict[str, Any]]:
    return [tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Bad debts recovered", amount=float(amt), a=+amt, o=+amt, l=0.0)]


def make_transaction_analysis_fee_income_on_credit(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
    source: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal="", dr="Debtors control", cr="Fee income", amount=float(amt), a=+float(amt), o=+float(amt), l=0.0)
    row1["tag"] = "fee_income_credit"
    return [row1]


def make_transaction_analysis_insurance_accrued(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    return [tx_builder(nr=nr, source="Journal voucher", journal="", dr="Insurance", cr="Accrued expense", amount=float(amt), a=0.0, o=-amt, l=+amt)]


def make_transaction_analysis_owner_withdrawal(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Cheque counterfoil", journal="CPJ", dr="Drawings", cr="Bank", amount=float(amt), a=-amt, o=-amt, l=0.0)
    row1["tag"] = "owner_withdrawal"
    return [row1]


def make_transaction_analysis_fixed_deposit_investment(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    fmt_money: Callable[[float], str],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Fixed deposit", cr="Bank", amount=float(amt), a=+float(amt), o=0.0, l=0.0)
    row1["tag"] = "fixed_deposit_investment"
    row1["a_override"] = f"+{fmt_money(float(amt))}/-{fmt_money(float(amt))}"
    return [row1]


def make_transaction_analysis_petty_cash_imprest_restoration(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    fmt_money: Callable[[float], str],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Cheque counterfoil", journal="CPJ", dr="Petty cash", cr="Bank", amount=float(amt), a=+float(amt), o=0.0, l=0.0)
    row1["tag"] = "petty_cash_imprest"
    row1["a_override"] = f"+{fmt_money(float(amt))}/-{fmt_money(float(amt))}"
    return [row1]


def make_transaction_analysis_owner_taking_stock(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    cost: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Journal voucher", journal="GJ", dr="Drawings", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0)
    row1["tag"] = "owner_taking_stock"
    return [row1]


def make_transaction_analysis_interest_on_current_account(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Bank", cr="Interest income", amount=float(amt), a=+amt, o=+amt, l=0.0)
    row1["tag"] = "interest_current_account"
    return [row1]


def make_transaction_analysis_overdraft_interest(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Interest expense", cr="Bank", amount=float(amt), a=0.0, o=-float(amt), l=+float(amt))
    row1["tag"] = "bank_unfavourable_interest"
    return [row1]


def make_transaction_analysis_vehicle_purchase_on_credit(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Original invoice", journal="CJ", dr="Vehicles", cr="Creditors control", amount=float(amt), a=+float(amt), o=0.0, l=+float(amt))
    row1["tag"] = "vehicle_purchase_credit"
    return [row1]


def make_transaction_analysis_cash_handling_fee(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Bank charges", cr="Bank", amount=float(amt), a=-float(amt), o=-float(amt), l=0.0)
    row1["tag"] = "cash_handling_fee"
    return [row1]


def make_transaction_analysis_packing_materials_unfavourable(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Packing materials", cr="Bank", amount=float(amt), a=0.0, o=-float(amt), l=+float(amt))
    row1["tag"] = "packing_materials_unfavourable"
    return [row1]


def make_transaction_analysis_postage_paid(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Petty cash voucher", journal="PCJ", dr="Postage", cr="Petty cash", amount=float(amt), a=-float(amt), o=-float(amt), l=0.0)
    row1["tag"] = "postage_paid"
    return [row1]


def make_transaction_analysis_cash_sales_cost(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    selling_factor: float,
    markup_pct: float,
    cost: float,
    nr: str,
    source: str = "Cash register roll",
    journal: str = "",
) -> List[Dict[str, Any]]:
    sales = round_money(cost * selling_factor)
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Sales", amount=float(sales), a=+sales, o=+sales, l=0.0)
    row1["tag"] = "cash_sales_main"
    row1["cost_price"] = float(cost)
    row1["sales_amount"] = float(sales)
    row1["markup_pct"] = float(markup_pct)
    row2 = tx_builder(nr="", source="", journal="", dr="Cost of sales", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0)
    row2["tag"] = "cash_sales_cost"
    row2["cost_price"] = float(cost)
    row2["sales_amount"] = float(sales)
    row2["markup_pct"] = float(markup_pct)
    return [row1, row2]


def make_transaction_analysis_credit_sales_cost(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    selling_factor: float,
    markup_pct: float,
    cost: float,
    nr: str,
    source: str = "Duplicate invoice",
    journal: str = "",
) -> List[Dict[str, Any]]:
    sales = round_money(cost * selling_factor)
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Debtors control", cr="Sales", amount=float(sales), a=+sales, o=+sales, l=0.0)
    row1["tag"] = "credit_sales_main"
    row1["cost_price"] = float(cost)
    row1["sales_amount"] = float(sales)
    row1["markup_pct"] = float(markup_pct)
    row2 = tx_builder(nr="", source="", journal="", dr="Cost of sales", cr="Trading stock", amount=float(cost), a=-cost, o=-cost, l=0.0)
    row2["tag"] = "credit_sales_cost"
    row2["cost_price"] = float(cost)
    row2["sales_amount"] = float(sales)
    row2["markup_pct"] = float(markup_pct)
    return [row1, row2]


def make_transaction_analysis_debtor_settlement_discount(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    fmt_money: Callable[[float], str],
    owed: float,
    disc_pct: float,
    nr: str,
    source: str = "Duplicate receipt",
    journal: str = "",
) -> List[Dict[str, Any]]:
    disc = round_money(owed * (disc_pct / 100.0))
    bank_amt = round_money(owed - disc)
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Bank", cr="Debtors control", amount=float(bank_amt), a=+bank_amt, o=0.0, l=0.0)
    row1["tag"] = "debtor_settlement_main"
    row1["owed"] = float(owed)
    row1["disc_pct"] = float(disc_pct)
    row1["discount_amount"] = float(disc)
    row1["bank_amount"] = float(bank_amt)
    row1["a_override"] = f"+{fmt_money(float(bank_amt))}/-{fmt_money(float(bank_amt))}"
    row2 = tx_builder(nr="", source="", journal="", dr="Discount allowed", cr="Debtors control", amount=float(disc), a=-disc, o=-disc, l=0.0)
    row2["tag"] = "discount_allowed_settlement"
    row2["owed"] = float(owed)
    row2["disc_pct"] = float(disc_pct)
    row2["discount_amount"] = float(disc)
    row2["bank_amount"] = float(bank_amt)
    return [row1, row2]


def make_transaction_analysis_rd_cheque_cancel_discount(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    fmt_money: Callable[[float], str],
    bank_amt: float,
    disc: float,
    nr: str,
    source: str = "Bank statement",
    journal: str = "",
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Debtors control", cr="Bank", amount=float(bank_amt), a=+float(bank_amt), o=0.0, l=0.0)
    row1["tag"] = "rd_cheque_reversal"
    row1["a_override"] = f"+{fmt_money(float(bank_amt))}/-{fmt_money(float(bank_amt))}"
    row2 = tx_builder(nr="", source="Journal voucher", journal=journal, dr="Debtors control", cr="Discount allowed", amount=float(disc), a=+disc, o=+disc, l=0.0)
    row2["tag"] = "rd_cheque_discount_reversal"
    return [row1, row2]


def make_transaction_analysis_creditor_payment_discount_received(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    owed: float,
    disc_pct: float,
    nr: str,
    source: str = "Cheque counterfoil",
    journal: str = "",
) -> List[Dict[str, Any]]:
    disc = round_money(owed * (disc_pct / 100.0))
    bank_amt = round_money(owed - disc)
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Creditors control", cr="Bank", amount=float(bank_amt), a=-bank_amt, o=0.0, l=-bank_amt)
    row1["tag"] = "creditor_payment_main"
    row1["owed"] = float(owed)
    row1["disc_pct"] = float(disc_pct)
    row1["discount_amount"] = float(disc)
    row1["bank_amount"] = float(bank_amt)
    row2 = tx_builder(nr="", source="", journal="", dr="Creditors control", cr="Discount received", amount=float(disc), a=0.0, o=+disc, l=-disc)
    row2["tag"] = "creditor_discount_received"
    row2["owed"] = float(owed)
    row2["disc_pct"] = float(disc_pct)
    row2["discount_amount"] = float(disc)
    row2["bank_amount"] = float(bank_amt)
    return [row1, row2]


def make_transaction_analysis_purchase_on_credit_trade_discount(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    gross: float,
    td_pct: float,
    nr: str,
    source: str = "Original invoice",
    journal: str = "",
) -> List[Dict[str, Any]]:
    net = round_money(gross * (1.0 - (td_pct / 100.0)))
    return [tx_builder(nr=nr, source=source, journal=journal, dr="Trading stock", cr="Creditors control", amount=float(net), a=+net, o=0.0, l=+net)]


def make_transaction_analysis_purchase_by_cheque_trade_discount(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    fmt_money: Callable[[float], str],
    gross: float,
    td_pct: float,
    nr: str,
    source: str = "Cheque counterfoil",
    journal: str = "",
) -> List[Dict[str, Any]]:
    net = round_money(gross * (1.0 - (td_pct / 100.0)))
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Trading stock", cr="Bank", amount=float(net), a=+net, o=0.0, l=0.0)
    row1["tag"] = "purchase_cheque_asset_swap"
    row1["a_override"] = f"+{fmt_money(float(net))}/-{fmt_money(float(net))}"
    return [row1]


def make_transaction_analysis_loan_repayment_with_interest(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    repayment: float,
    rate_pct: float,
    months: int,
    nr: str,
    source: str = "EFT",
    journal: str = "",
) -> List[Dict[str, Any]]:
    factor = 1.0 + ((rate_pct / 100.0) * (months / 12.0))
    capital = round_money(repayment / factor) if factor > 0 else float(repayment)
    interest = round_money(repayment - capital)
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Loan", cr="Bank", amount=float(capital), a=-capital, o=0.0, l=-capital)
    row1["tag"] = "loan_repayment_capital"
    row1["repayment_total"] = float(repayment)
    row1["rate_pct"] = float(rate_pct)
    row1["months"] = int(months)
    row1["capital_amount"] = float(capital)
    row1["interest_amount"] = float(interest)
    row2 = tx_builder(nr="", source="", journal="", dr="Interest on loan", cr="Bank", amount=float(interest), a=-interest, o=-interest, l=0.0)
    row2["tag"] = "loan_repayment_interest"
    row2["repayment_total"] = float(repayment)
    row2["rate_pct"] = float(rate_pct)
    row2["months"] = int(months)
    row2["capital_amount"] = float(capital)
    row2["interest_amount"] = float(interest)
    return [row1, row2]


def make_transaction_analysis_debtor_allowance_return(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    selling_price: float,
    cost_price: float,
    nr: str,
    source: str = "Duplicate credit note",
    journal: str = "",
) -> List[Dict[str, Any]]:
    return [
        tx_builder(nr=nr, source=source, journal=journal, dr="Debtors allowances", cr="Debtors control", amount=float(selling_price), a=-selling_price, o=-selling_price, l=0.0),
        tx_builder(nr="", source="", journal="", dr="Trading stock", cr="Cost of sales", amount=float(cost_price), a=+cost_price, o=+cost_price, l=0.0),
    ]


def make_transaction_analysis_creditor_allowance_return(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    cost_price: float,
    td_pct: float,
    nr: str,
    source: str = "Duplicate debit note",
    journal: str = "",
) -> List[Dict[str, Any]]:
    net = round_money(cost_price * (1.0 - (td_pct / 100.0)))
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Creditors control", cr="Trading stock", amount=float(net), a=-net, o=0.0, l=-net)
    row1["tag"] = "creditor_allowance_return"
    row1["cost_price"] = float(cost_price)
    row1["td_pct"] = float(td_pct)
    row1["net_amount"] = float(net)
    return [row1]


def make_transaction_analysis_interest_on_overdue(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    principal: float,
    rate_pct: float,
    months: int,
    nr: str,
    kind: str,
    source: str = "Journal voucher",
    journal: str = "",
) -> List[Dict[str, Any]]:
    interest = round_money(principal * (rate_pct / 100.0) * (months / 12.0))
    if kind == "debtor":
        row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Debtors control", cr="Interest income", amount=float(interest), a=+interest, o=+interest, l=0.0)
        row1["tag"] = "interest_overdue_debtor"
        row1["principal"] = float(principal)
        row1["rate_pct"] = float(rate_pct)
        row1["months"] = int(months)
        row1["interest_amount"] = float(interest)
        return [row1]
    row1 = tx_builder(nr=nr, source=source, journal=journal, dr="Interest expense", cr="Creditors control", amount=float(interest), a=0.0, o=-interest, l=+interest)
    row1["tag"] = "interest_overdue_creditor"
    row1["principal"] = float(principal)
    row1["rate_pct"] = float(rate_pct)
    row1["months"] = int(months)
    row1["interest_amount"] = float(interest)
    return [row1]


def make_transaction_analysis_insolvent_debtor_dividend_writeoff(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    fmt_money: Callable[[float], str],
    owed: float,
    cents_in_rand: float,
    nr: str,
    source: str = "Bank statement",
) -> List[Dict[str, Any]]:
    dividend = float(round_money(owed * (cents_in_rand / 100.0)))
    writeoff = float(round_money(owed - dividend))
    row1 = tx_builder(nr=nr, source=source, journal="", dr="Bank", cr="Debtors control", amount=dividend, a=+dividend, o=0.0, l=0.0)
    row1["tag"] = "insolvency_dividend"
    row1["owed"] = float(owed)
    row1["cents_in_rand"] = float(cents_in_rand)
    row1["a_override"] = f"+{fmt_money(float(dividend))}/-{fmt_money(float(dividend))}"
    row2 = tx_builder(nr="", source="Journal voucher", journal="", dr="Bad debts", cr="Debtors control", amount=writeoff, a=-writeoff, o=-writeoff, l=0.0)
    row2["tag"] = "insolvency_writeoff"
    row2["owed"] = float(owed)
    row2["cents_in_rand"] = float(cents_in_rand)
    return [row1, row2]


def make_transaction_analysis_debtor_settlement_discount_unfavourable_bank(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    owed: float,
    disc_pct: float,
    nr: str,
) -> List[Dict[str, Any]]:
    disc = float(round_money(owed * (disc_pct / 100.0)))
    bank_amt = float(round_money(owed - disc))
    row1 = tx_builder(nr=nr, source="Duplicate receipt", journal="", dr="Bank", cr="Debtors control", amount=bank_amt, a=0.0, o=0.0, l=-bank_amt)
    row1["tag"] = "bank_unfavourable_receipt"
    row1["owed"] = float(owed)
    row1["disc_pct"] = float(disc_pct)
    row1["discount_amount"] = float(disc)
    row1["bank_amount"] = float(bank_amt)
    row2 = tx_builder(nr="", source="", journal="", dr="Discount allowed", cr="Debtors control", amount=disc, a=0.0, o=-disc, l=0.0)
    row2["tag"] = "bank_unfavourable_discount"
    row2["owed"] = float(owed)
    row2["disc_pct"] = float(disc_pct)
    row2["discount_amount"] = float(disc)
    row2["bank_amount"] = float(bank_amt)
    return [row1, row2]


def make_transaction_analysis_cash_withdrawal_for_wages(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    amt: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Cheque counterfoil", journal="CPJ", dr="Cash", cr="Bank", amount=float(amt), a=0.0, o=0.0, l=0.0)
    row1["tag"] = "cash_withdrawal_bank_to_cash"
    row2 = tx_builder(nr="", source="Petty cash voucher", journal="PCJ", dr="Wages", cr="Cash", amount=float(amt), a=-float(amt), o=-float(amt), l=0.0)
    row2["tag"] = "wages_paid_from_cash"
    return [row1, row2]


def make_transaction_analysis_petty_cash_on_behalf_of_debtor(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    fmt_money: Callable[[float], str],
    amt: float,
    nr: str,
    debtor_name: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Petty cash voucher", journal="", dr="Debtors control", cr="Petty cash", amount=float(amt), a=0.0, o=0.0, l=0.0)
    row1["tag"] = "petty_cash_on_behalf_debtor"
    row1["debtor_name"] = str(debtor_name)
    row1["a_override"] = f"+{fmt_money(float(amt))}/-{fmt_money(float(amt))}"
    return [row1]


def make_transaction_analysis_fixed_deposit_maturity(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    round_money: Callable[[float], float],
    fmt_money: Callable[[float], str],
    principal: float,
    rate_pct: float,
    months: int,
    nr: str,
) -> List[Dict[str, Any]]:
    interest = float(round_money(principal * (rate_pct / 100.0) * (months / 12.0)))
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Bank", cr="Fixed deposit", amount=float(principal), a=+float(principal), o=0.0, l=0.0)
    row1["tag"] = "fd_maturity_principal"
    row1["a_override"] = f"+{fmt_money(float(principal))}/-{fmt_money(float(principal))}"
    row2 = tx_builder(nr="", source="", journal="", dr="Bank", cr="Interest on fixed deposit", amount=float(interest), a=+interest, o=+interest, l=0.0)
    row2["tag"] = "fd_maturity_interest"
    return [row1, row2]


def make_transaction_analysis_bank_fee_breakdown(
    *,
    tx_builder: Callable[..., Dict[str, Any]],
    service_fee: float,
    cash_handling_fee: float,
    overdraft_int: float,
    nr: str,
) -> List[Dict[str, Any]]:
    row1 = tx_builder(nr=nr, source="Bank statement", journal="", dr="Bank charges", cr="Bank", amount=float(service_fee), a=0.0, o=-service_fee, l=+service_fee)
    row1["tag"] = "bank_fee_service"
    row2 = tx_builder(nr="", source="", journal="", dr="Bank charges", cr="Bank", amount=float(cash_handling_fee), a=0.0, o=-cash_handling_fee, l=+cash_handling_fee)
    row2["tag"] = "bank_fee_cash"
    row3 = tx_builder(nr="", source="", journal="", dr="Interest expense", cr="Bank", amount=float(overdraft_int), a=0.0, o=-overdraft_int, l=+overdraft_int)
    row3["tag"] = "bank_fee_overdraft_int"
    return [row1, row2, row3]
