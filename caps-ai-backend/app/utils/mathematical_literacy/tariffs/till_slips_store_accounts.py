"""Till Slips, Store Accounts & Invoices Subskills (Subskills 45 to 51).

45. fin_doc_slip_cash_tendered_and_change_calculation
46. fin_doc_slip_itemised_total_subtotal_audit
47. fin_doc_slip_vat_inclusive_vs_exempt_breakdown
48. fin_doc_slip_discount_voucher_or_loyalty_points
49. fin_doc_store_account_statement_credit_limit
50. fin_doc_store_account_minimum_monthly_installment
51. fin_doc_store_account_interest_and_service_fees
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_doc_slip_cash_tendered_and_change_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate the cash change returned at a supermarket till point."""
    name = r.choice(SA_NAMES)
    total_due = round(r.choice([124.65, 142.80, 168.45, 186.55, 215.70, 248.90]), 2)
    # Tender next round banknote: R 150, R 200, or R 300
    if total_due < 150:
        tendered = 150.00
    elif total_due < 200:
        tendered = 200.00
    else:
        tendered = 300.00

    change = round(tendered - total_due, 2)
    ans_str = _fmt_curr(change)

    prompt = (
        f"{name} makes purchases at a supermarket checkout till with a total balance due of **{_fmt_curr(total_due)}**.\n"
        f"{name} hands the cashier **{_fmt_curr(tendered)} in cash**.\n\n"
        f"Calculate the **change amount** the cashier must return to {name}.\n"
        f"Use the formula: $$\\text{{Change}} = \\text{{Cash Tendered}} - \\text{{Total Due}}$$"
    )
    sol = (
        f"Step 1: Identify cash tendered and balance due:\n"
        f"• Cash Tendered = {_fmt_curr(tendered)}\n"
        f"• Total Balance Due = {_fmt_curr(total_due)}\n\n"
        f"Step 2: Method setup – subtract balance due from cash tendered:\n"
        f"• Change = {_fmt_curr(tendered)} - {_fmt_curr(total_due)} "
        f"✓ [1 Mark: Method – subtracting total balance due from cash tendered]\n\n"
        f"Step 3: Calculate change:\n"
        f"Change = {ans_str} ✓ [1 Mark: Accuracy – correct change in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(total_due)} from {_fmt_curr(tendered)}",
        f"1 Mark: Accuracy – correct change {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract the total purchase amount ({_fmt_curr(total_due)}) from the cash handed over ({_fmt_curr(tendered)}).",
        "tier_2": f"Calculate: {tendered:.2f} - {total_due:.2f}.",
        "tier_3": f"{tendered:.2f} - {total_due:.2f} = {change:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_slip_cash_tendered_and_change_calculation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_slip_itemised_total_subtotal_audit(r: random.Random) -> Dict[str, Any]:
    """Sum itemised lines on a till slip to audit the correct balance due."""
    name = r.choice(SA_NAMES)
    item_prices = [
        ("Whole wheat bread", round(r.choice([16.99, 17.50, 18.99]), 2)),
        ("Full cream milk 2L", round(r.choice([32.99, 34.50, 36.99]), 2)),
        ("Eggs 18-pack", round(r.choice([48.99, 52.00, 56.50]), 2)),
        ("Cheddar cheese 400g", round(r.choice([54.90, 58.00, 62.50]), 2)),
        ("Plastic carrier bag", 0.90)
    ]
    total_due = round(sum(p[1] for p in item_prices), 2)
    ans_str = _fmt_curr(total_due)

    items_table_rows = "\n".join([f"| {p[0]} | {_fmt_curr(p[1])} |" for p in item_prices])

    prompt = (
        f"{name} examines a grocery store till slip with the following itemised list:\n\n"
        f"| Item Description | Amount |\n"
        f"| :--- | :---: |\n"
        f"{items_table_rows}\n\n"
        f"Calculate the **correct total balance due** for this till slip."
    )
    sol = (
        f"Step 1: List all itemised prices on the slip:\n"
        f"• Bread = {_fmt_curr(item_prices[0][1])}\n"
        f"• Milk = {_fmt_curr(item_prices[1][1])}\n"
        f"• Eggs = {_fmt_curr(item_prices[2][1])}\n"
        f"• Cheese = {_fmt_curr(item_prices[3][1])}\n"
        f"• Carrier bag = {_fmt_curr(item_prices[4][1])}\n\n"
        f"Step 2: Method setup – sum all items together:\n"
        f"• Total Due = {_fmt_curr(item_prices[0][1])} + {_fmt_curr(item_prices[1][1])} + {_fmt_curr(item_prices[2][1])} + {_fmt_curr(item_prices[3][1])} + {_fmt_curr(item_prices[4][1])} "
        f"✓ [1 Mark: Method – summing all individual items on the till slip]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Balance Due = {ans_str} ✓ [1 Mark: Accuracy – correct sum in Rands]"
    )
    rubric = [
        "1 Mark: Method – summing all 5 items on the till slip",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": "Add up the prices of all 5 items listed in the table.",
        "tier_2": f"Calculate: {' + '.join([f'{p[1]:.2f}' for p in item_prices])}.",
        "tier_3": f"Sum = {total_due:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_slip_itemised_total_subtotal_audit", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_slip_vat_inclusive_vs_exempt_breakdown(r: random.Random) -> Dict[str, Any]:
    """Verify the VAT breakdown table on a store tax invoice (15% taxable total vs 0% zero-rated total)."""
    name = r.choice(SA_NAMES)
    taxable_excl = round(r.choice([120.00, 140.00, 160.00, 180.00, 200.00]), 2)
    zero_rated_total = round(r.choice([35.50, 48.00, 56.20, 64.00]), 2)
    vat_amt = round(taxable_excl * 0.15, 2)
    total_payable = round(taxable_excl + vat_amt + zero_rated_total, 2)
    ans_str = _fmt_curr(total_payable)

    prompt = (
        f"A supermarket till slip displays the following tax invoice summary footer:\n\n"
        f"| Tax Code | Taxable Base (Excl) | VAT Rate | VAT Amount |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Zero VAT (Exempt Foodstuffs) | {_fmt_curr(zero_rated_total)} | 0% | R 0,00 |\n"
        f"| Standard VAT Goods | {_fmt_curr(taxable_excl)} | 15% | {_fmt_curr(vat_amt)} |\n\n"
        f"Calculate the **Final Total Amount Payable** on this till slip.\n"
        f"Use the formula: $$\\text{{Total}} = \\text{{Zero-Rated Total}} + \\text{{Taxable Base}} + \\text{{VAT Amount}}$$"
    )
    sol = (
        f"Step 1: Identify all components of the total payable:\n"
        f"• Zero-rated total = {_fmt_curr(zero_rated_total)}\n"
        f"• Taxable goods (excluding VAT) = {_fmt_curr(taxable_excl)}\n"
        f"• 15% VAT on taxable goods = {_fmt_curr(vat_amt)}\n\n"
        f"Step 2: Method setup – sum all three amounts:\n"
        f"• Total Payable = {_fmt_curr(zero_rated_total)} + {_fmt_curr(taxable_excl)} + {_fmt_curr(vat_amt)} "
        f"✓ [1 Mark: Method – adding zero-rated base, taxable base, and VAT amount]\n\n"
        f"Step 3: Calculate total:\n"
        f"Total Payable = {ans_str} ✓ [1 Mark: Accuracy – correct final payable amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating {_fmt_curr(zero_rated_total)} + {_fmt_curr(taxable_excl)} + {_fmt_curr(vat_amt)}",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"Add the zero-rated goods ({_fmt_curr(zero_rated_total)}), the taxable goods base ({_fmt_curr(taxable_excl)}), and the VAT ({_fmt_curr(vat_amt)}).",
        "tier_2": f"Calculate: {zero_rated_total:.2f} + {taxable_excl:.2f} + {vat_amt:.2f}.",
        "tier_3": f"Sum = {total_payable:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_slip_vat_inclusive_vs_exempt_breakdown", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_slip_discount_voucher_or_loyalty_points(r: random.Random) -> Dict[str, Any]:
    """Apply a promotional discount voucher to determine the final amount paid."""
    name = r.choice(SA_NAMES)
    store = r.choice(["Woolworths", "Checkers", "Edgars", "Mr Price", "Pick n Pay"])
    subtotal = round(r.choice([350.00, 480.00, 550.00, 680.00, 750.00]), 2)
    voucher_val = round(r.choice([50.00, 75.00, 100.00, 120.00]), 2)

    final_due = round(subtotal - voucher_val, 2)
    ans_str = _fmt_curr(final_due)

    prompt = (
        f"{name} shops at {store} with a basket subtotal of **{_fmt_curr(subtotal)}**.\n"
        f"At the till point, {name} redeems a store promotional discount voucher worth **{_fmt_curr(voucher_val)}**.\n\n"
        f"Calculate the **final amount due** that {name} must pay after the voucher discount is deducted."
    )
    sol = (
        f"Step 1: Identify purchase subtotal and discount voucher value:\n"
        f"• Subtotal = {_fmt_curr(subtotal)}\n"
        f"• Discount Voucher = {_fmt_curr(voucher_val)}\n\n"
        f"Step 2: Method setup – subtract voucher value from subtotal:\n"
        f"• Final Due = {_fmt_curr(subtotal)} - {_fmt_curr(voucher_val)} "
        f"✓ [1 Mark: Method – subtracting voucher discount from purchase subtotal]\n\n"
        f"Step 3: Calculate net amount due:\n"
        f"Final Due = {ans_str} ✓ [1 Mark: Accuracy – correct final amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(voucher_val)} from {_fmt_curr(subtotal)}",
        f"1 Mark: Accuracy – correct final amount {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract the discount voucher ({_fmt_curr(voucher_val)}) from the subtotal ({_fmt_curr(subtotal)}).",
        "tier_2": f"Calculate: {subtotal:.2f} - {voucher_val:.2f}.",
        "tier_3": f"{subtotal:.2f} - {voucher_val:.2f} = {final_due:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_slip_discount_voucher_or_loyalty_points", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_store_account_statement_credit_limit(r: random.Random) -> Dict[str, Any]:
    """Read a store account statement to calculate available credit: Credit Limit - Current Balance."""
    name = r.choice(SA_NAMES)
    store = r.choice(["Truworths", "Foschini (TFG)", "Ackermans", "Miladys", "Markhams"])
    credit_limit = round(r.choice([3500.00, 5000.00, 6000.00, 7500.00, 10000.00]), 2)
    current_balance = round(r.choice([1250.00, 1850.50, 2400.00, 3100.00]), 2)

    available_credit = round(credit_limit - current_balance, 2)
    ans_str = _fmt_curr(available_credit)

    prompt = (
        f"{name} receives a monthly store account statement from **{store}** displaying the following credit summary:\n\n"
        f"• **Approved Credit Limit**: {_fmt_curr(credit_limit)}\n"
        f"• **Current Balance Owed**: {_fmt_curr(current_balance)}\n\n"
        f"Calculate {name}'s **available credit** (the maximum additional purchases {name} can make on this account).\n"
        f"Use the formula: $$\\text{{Available Credit}} = \\text{{Credit Limit}} - \\text{{Current Balance Owed}}$$"
    )
    sol = (
        f"Step 1: Identify credit parameters from statement:\n"
        f"• Credit Limit = {_fmt_curr(credit_limit)}\n"
        f"• Current Balance Owed = {_fmt_curr(current_balance)}\n\n"
        f"Step 2: Method setup – subtract current balance owed from credit limit:\n"
        f"• Available Credit = {_fmt_curr(credit_limit)} - {_fmt_curr(current_balance)} "
        f"✓ [1 Mark: Method – subtracting current balance owed from credit limit]\n\n"
        f"Step 3: Calculate available credit:\n"
        f"Available Credit = {ans_str} ✓ [1 Mark: Accuracy – correct available credit in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(current_balance)} from {_fmt_curr(credit_limit)}",
        f"1 Mark: Accuracy – correct available credit {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract what {name} currently owes ({_fmt_curr(current_balance)}) from the approved limit ({_fmt_curr(credit_limit)}).",
        "tier_2": f"Calculate: {credit_limit:.2f} - {current_balance:.2f}.",
        "tier_3": f"{credit_limit:.2f} - {current_balance:.2f} = {available_credit:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_store_account_statement_credit_limit", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_store_account_minimum_monthly_installment(r: random.Random) -> Dict[str, Any]:
    """Calculate the minimum monthly payment due on a store credit account (e.g. 5% of balance or R150 minimum)."""
    name = r.choice(SA_NAMES)
    balance = round(r.choice([2500.00, 3200.00, 4000.00, 5200.00, 6800.00]), 2)
    pct_rate = 5.0  # 5% of balance

    installment = round(balance * (pct_rate / 100), 2)
    ans_str = _fmt_curr(installment)

    prompt = (
        f"{name}'s store card statement has an outstanding balance of **{_fmt_curr(balance)}**.\n"
        f"The credit terms require a minimum monthly installment of **5% of the outstanding balance**.\n\n"
        f"Calculate the **minimum monthly installment** {name} must pay this month."
    )
    sol = (
        f"Step 1: Identify outstanding balance and minimum installment percentage:\n"
        f"• Outstanding Balance = {_fmt_curr(balance)}\n"
        f"• Minimum percentage = 5% = 0,05\n\n"
        f"Step 2: Method setup – calculate 5% of the balance:\n"
        f"• Minimum Installment = 5% × {_fmt_curr(balance)} = (5 ÷ 100) × {balance} "
        f"✓ [1 Mark: Method – calculating 5% of outstanding store card balance]\n\n"
        f"Step 3: Calculate minimum installment:\n"
        f"Minimum Installment = {ans_str} ✓ [1 Mark: Accuracy – correct installment in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(balance)} by 0,05",
        f"1 Mark: Accuracy – correct installment {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate 5% of {_fmt_curr(balance)}.",
        "tier_2": f"Multiply {balance:.2f} by 0,05.",
        "tier_3": f"{balance:.2f} × 0,05 = {installment:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_store_account_minimum_monthly_installment", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_store_account_interest_and_service_fees(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly finance interest and monthly customer club service fee on a store card."""
    name = r.choice(SA_NAMES)
    balance = round(r.choice([1500.00, 2000.00, 2500.00, 3000.00, 4000.00]), 2)
    monthly_interest_pct = 1.75  # 1.75% per month (approx 21% p.a.)
    monthly_club_fee = 28.50     # Customer protection / club fee

    interest_charge = round(balance * (monthly_interest_pct / 100), 2)
    total_charges = round(interest_charge + monthly_club_fee, 2)
    ans_str = _fmt_curr(total_charges)

    prompt = (
        f"{name}'s store card has an outstanding revolving balance of **{_fmt_curr(balance)}**.\n"
        f"The store charges:\n"
        f"• **Monthly finance interest**: 1,75% of the balance\n"
        f"• **Monthly account service & club fee**: {_fmt_curr(monthly_club_fee)}\n\n"
        f"Calculate the **total fees and interest** added to {name}'s account for the month."
    )
    sol = (
        f"Step 1: Calculate monthly finance interest on the balance:\n"
        f"• Interest = 1,75% of {_fmt_curr(balance)} = (1,75 ÷ 100) × {balance} = {_fmt_curr(interest_charge)}\n\n"
        f"Step 2: Method setup – add monthly club fee:\n"
        f"• Total Charges = Interest + Monthly Club Fee\n"
        f"• Total Charges = {_fmt_curr(interest_charge)} + {_fmt_curr(monthly_club_fee)} "
        f"✓ [1 Mark: Method – evaluating 1,75% interest on balance and adding club fee]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Charges = {ans_str} ✓ [1 Mark: Accuracy – correct total fees in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (1,75% × {_fmt_curr(balance)}) + {_fmt_curr(monthly_club_fee)}",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"First find 1,75% of {_fmt_curr(balance)}: {balance} × 0,0175 = {_fmt_curr(interest_charge)}.",
        "tier_2": f"Add the monthly fee of {_fmt_curr(monthly_club_fee)} to that interest.",
        "tier_3": f"{interest_charge:.2f} + {monthly_club_fee:.2f} = {total_charges:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_store_account_interest_and_service_fees", prompt, ans_str, sol, rubric, hints, 2, r=r)
