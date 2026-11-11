"""Bank Fee Schedules & Tariff Formulas Subskills (Subskills 18 to 25).

18. bank_fee_flat_plus_sliding_scale_atm_withdrawal
19. bank_fee_branch_teller_cash_deposit_percentage
20. bank_fee_branch_vs_atm_cost_comparison
21. bank_fee_tillpoint_supermarket_cashout_savings
22. bank_fee_bundled_package_vs_pay_as_you_transact
23. bank_fee_tiered_balance_fee_waiver
24. bank_fee_sms_notification_monthly_total
25. bank_fee_forex_currency_conversion_commission
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import SA_BANKS, SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_fee_flat_plus_sliding_scale_atm_withdrawal(r: random.Random) -> Dict[str, Any]:
    """Calculate ATM cash withdrawal fee using the formula: Base fee for first R100 + fee per additional R100 (or part thereof)."""
    name = r.choice(SA_NAMES)
    base_fee = round(r.choice([2.25, 2.35, 3.50, 4.00]), 2)
    per_hundred = round(r.choice([1.10, 1.15, 1.20, 1.25]), 2)
    # Withdrawal amount between R250 and R1500
    withdrawal = r.choice([250, 350, 450, 650, 750, 850, 1050, 1250, 1400])

    # First R100 covered by base_fee
    additional_amt = max(0, withdrawal - 100)
    additional_units = math.ceil(additional_amt / 100)
    total_fee = round(base_fee + (additional_units * per_hundred), 2)
    ans_str = _fmt_curr(total_fee)

    prompt = (
        f"{name} wants to withdraw {_fmt_curr(withdrawal)} in cash from a bank ATM. "
        f"The bank fee schedule states:\n"
        f"• **Base fee**: {_fmt_curr(base_fee)} for the first R 100\n"
        f"• **Additional fee**: {_fmt_curr(per_hundred)} for every additional R 100 (or part thereof)\n\n"
        f"Calculate the total ATM withdrawal transaction fee {name} will be charged."
    )
    sol = (
        f"Step 1: Break down the withdrawal amount into the base tier and additional units:\n"
        f"• Total withdrawal = {_fmt_curr(withdrawal)}\n"
        f"• First R 100 = {_fmt_curr(base_fee)}\n"
        f"• Remaining amount = {_fmt_curr(withdrawal)} - R 100 = {_fmt_curr(additional_amt)}\n\n"
        f"Step 2: Method setup – calculate additional R 100 blocks (or part thereof):\n"
        f"• Number of additional R 100 blocks = {additional_amt} ÷ 100 = {additional_amt / 100} -> round up to {additional_units} blocks\n"
        f"• Total Fee = Base Fee + ({additional_units} × {_fmt_curr(per_hundred)})\n"
        f"• Total Fee = {_fmt_curr(base_fee)} + ({additional_units} × {per_hundred}) "
        f"✓ [1 Mark: Method – applying base fee plus {additional_units} units at {_fmt_curr(per_hundred)}]\n\n"
        f"Step 3: Calculate total fee:\n"
        f"Total Fee = {base_fee} + {additional_units * per_hundred:.2f} = {ans_str}\n"
        f"✓ [1 Mark: Accuracy – correct withdrawal fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {additional_units} additional blocks at {_fmt_curr(per_hundred)} plus base {_fmt_curr(base_fee)}",
        f"1 Mark: Accuracy – correct total fee {ans_str}"
    ]
    hints = {
        "tier_1": f"The first R 100 costs {_fmt_curr(base_fee)}. Subtract R 100 from {_fmt_curr(withdrawal)}.",
        "tier_2": f"Divide the remaining {_fmt_curr(additional_amt)} by 100 and round UP to get {additional_units} blocks.",
        "tier_3": f"{base_fee:.2f} + ({additional_units} × {per_hundred:.2f}) = {total_fee:.2f}, giving {ans_str}."
    }
    d_spec = {
        "diagram_role": "context",
        "kind": "step_tariff",
        "title": f"ATM Withdrawal Fee Schedule (Withdrawal: R {withdrawal})",
        "blocks": [
            {"limit": 100, "rate": base_fee},
            {"limit": 500, "rate": round(base_fee + 4 * per_hundred, 2)},
            {"limit": 1000, "rate": round(base_fee + 9 * per_hundred, 2)},
        ],
    }
    return _make_q("bank_fee_flat_plus_sliding_scale_atm_withdrawal", prompt, ans_str, sol, rubric, hints, 2, r=r, diagram_spec=d_spec)


def _gen_bank_fee_branch_teller_cash_deposit_percentage(r: random.Random) -> Dict[str, Any]:
    """Calculate branch teller cash deposit fee: Base Fee + percentage of deposit value."""
    name = r.choice(SA_NAMES)
    base_fee = round(r.choice([2.50, 3.00, 3.50, 4.50]), 2)
    pct = round(r.choice([0.85, 0.95, 1.15, 1.25, 2.0]), 2)
    deposit = r.choice([350, 450, 650, 875, 1200, 1500, 2400, 3200])

    pct_fee = round(deposit * (pct / 100), 2)
    total_fee = round(base_fee + pct_fee, 2)
    ans_str = _fmt_curr(total_fee)

    prompt = (
        f"{name} deposits {_fmt_curr(deposit)} in cash with a bank teller inside the branch. "
        f"The bank uses the following fee formula:\n\n"
        f"$$\\text{{Transaction fee}} = {_fmt_curr(base_fee)} + {_fmt(pct)}\\%\\text{{ of deposit amount}}$$\n\n"
        f"Calculate the total deposit fee charged to {name}'s account."
    )
    sol = (
        f"Step 1: Identify components of the tariff formula:\n"
        f"• Base fee = {_fmt_curr(base_fee)}\n"
        f"• Percentage rate = {_fmt(pct)}% = {pct / 100}\n"
        f"• Deposit amount = {_fmt_curr(deposit)}\n\n"
        f"Step 2: Method setup – calculate percentage component and add base fee:\n"
        f"Percentage Fee = ({pct} ÷ 100) × {_fmt_curr(deposit)} = {_fmt_curr(pct_fee)}\n"
        f"Total Fee = {_fmt_curr(base_fee)} + {_fmt_curr(pct_fee)} "
        f"✓ [1 Mark: Method – applying percentage rate to deposit and adding fixed base fee]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Fee = {base_fee} + {pct_fee:.2f} = {ans_str}\n"
        f"✓ [1 Mark: Accuracy – correct deposit fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {pct}% of {_fmt_curr(deposit)} and adding base {_fmt_curr(base_fee)}",
        f"1 Mark: Accuracy – correct fee {ans_str}"
    ]
    hints = {
        "tier_1": f"First calculate {_fmt(pct)}% of {_fmt_curr(deposit)}.",
        "tier_2": f"Add the fixed base fee of {_fmt_curr(base_fee)} to that percentage amount.",
        "tier_3": f"{base_fee:.2f} + ({deposit} × {pct/100:.4f}) = {total_fee:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_branch_teller_cash_deposit_percentage", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_branch_vs_atm_cost_comparison(r: random.Random) -> Dict[str, Any]:
    """Compare cash deposit fee between branch teller vs ATM for a specific cash amount."""
    name = r.choice(SA_NAMES)
    deposit = r.choice([1200, 1500, 2000, 2500, 3000, 3500])

    # Teller: 2.5% of deposit
    teller_pct = 2.5
    teller_fee = round(deposit * (teller_pct / 100), 2)

    # ATM: R 1.00 basic + R 1.20 per R 100
    atm_basic = 1.00
    atm_per_hundred = 1.20
    atm_blocks = math.ceil(deposit / 100)
    atm_fee = round(atm_basic + (atm_blocks * atm_per_hundred), 2)

    diff = round(teller_fee - atm_fee, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"{name} needs to deposit {_fmt_curr(deposit)} in cash. The bank offers two deposit channels:\n"
        f"• **Bank Teller**: charges a flat **2,5% of the deposit value**\n"
        f"• **Bank ATM**: charges **R 1,00 basic fee + R 1,20 per R 100 (or part thereof)**\n\n"
        f"Calculate how much money {name} will save by depositing the cash at the ATM instead of with the bank teller."
    )
    sol = (
        f"Step 1: Calculate the fee for each channel:\n"
        f"• **Bank Teller Fee**:\n"
        f"  Teller Fee = 2,5% of {_fmt_curr(deposit)} = (2,5 ÷ 100) × {deposit} = {_fmt_curr(teller_fee)}\n"
        f"• **ATM Fee**:\n"
        f"  Blocks of R 100 = {deposit} ÷ 100 = {atm_blocks}\n"
        f"  ATM Fee = R 1,00 + ({atm_blocks} × R 1,20) = R 1,00 + {_fmt_curr(atm_blocks * atm_per_hundred)} = {_fmt_curr(atm_fee)}\n\n"
        f"Step 2: Method setup – calculate the difference (savings):\n"
        f"Savings = Teller Fee - ATM Fee\n"
        f"Savings = {_fmt_curr(teller_fee)} - {_fmt_curr(atm_fee)} "
        f"✓ [1 Mark: Method – calculating both fees correctly and setting up difference]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating teller fee ({_fmt_curr(teller_fee)}) and ATM fee ({_fmt_curr(atm_fee)})",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate the teller fee: 2,5% × {_fmt_curr(deposit)}.",
        "tier_2": f"Calculate the ATM fee: R 1,00 + ({deposit // 100} × R 1,20).",
        "tier_3": f"{teller_fee:.2f} - {atm_fee:.2f} = {diff:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_branch_vs_atm_cost_comparison", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_tillpoint_supermarket_cashout_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate savings from supermarket tillpoint cashout vs other bank's ATM."""
    name = r.choice(SA_NAMES)
    draw_amt = r.choice([400, 500, 600, 800, 1000])
    till_fee = round(r.choice([1.00, 1.50, 2.00]), 2)

    # Other bank ATM: R 7.50 + R 1.20 per R100
    other_atm_base = 7.50
    other_atm_per_100 = 1.20
    units = draw_amt // 100
    other_atm_fee = round(other_atm_base + (units * other_atm_per_100), 2)

    savings = round(other_atm_fee - till_fee, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} needs to withdraw {_fmt_curr(draw_amt)} in cash on a Saturday.\n"
        f"• Option A: Withdraw at a supermarket tillpoint for a fee of {_fmt_curr(till_fee)}.\n"
        f"• Option B: Withdraw at another bank's ATM, charging {_fmt_curr(other_atm_base)} base + {_fmt_curr(other_atm_per_100)} per R 100 withdrawn.\n\n"
        f"Calculate the amount of money {name} saves by choosing the tillpoint cashout instead of the other bank's ATM."
    )
    sol = (
        f"Step 1: Calculate the cost of the other bank ATM withdrawal:\n"
        f"• Base fee = {_fmt_curr(other_atm_base)}\n"
        f"• Units of R 100 = {draw_amt} ÷ 100 = {units} units\n"
        f"• Variable charge = {units} × {_fmt_curr(other_atm_per_100)} = {_fmt_curr(units * other_atm_per_100)}\n"
        f"• Total other ATM fee = {_fmt_curr(other_atm_base)} + {_fmt_curr(units * other_atm_per_100)} = {_fmt_curr(other_atm_fee)}\n\n"
        f"Step 2: Method setup – calculate savings:\n"
        f"Savings = Other ATM Fee - Tillpoint Fee\n"
        f"Savings = {_fmt_curr(other_atm_fee)} - {_fmt_curr(till_fee)} "
        f"✓ [1 Mark: Method – evaluating other ATM tariff and finding difference with tillpoint]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating other bank ATM fee ({_fmt_curr(other_atm_fee)}) and subtracting till fee",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the total cost of withdrawing at the other bank's ATM first.",
        "tier_2": f"Other ATM fee = {other_atm_base} + ({units} × {other_atm_per_100}) = {other_atm_fee:.2f}.",
        "tier_3": f"{other_atm_fee:.2f} - {till_fee:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_tillpoint_supermarket_cashout_savings", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_bundled_package_vs_pay_as_you_transact(r: random.Random) -> Dict[str, Any]:
    """Compare a fixed monthly bundled fee vs Pay-As-You-Transact (PAYT) pricing."""
    name = r.choice(SA_NAMES)
    bundle_fee = round(r.choice([105.00, 115.00, 125.00]), 2)

    # PAYT fees:
    payt_admin = 6.00
    debit_card_swipes = r.choice([12, 15, 18, 20])
    swipe_rate = 1.50
    atm_draws = r.choice([3, 4, 5])
    atm_rate = 9.50
    debit_orders = r.choice([4, 5])
    debit_order_rate = 3.50

    payt_total = round(
        payt_admin + (debit_card_swipes * swipe_rate) + (atm_draws * atm_rate) + (debit_orders * debit_order_rate),
        2
    )

    cheaper_option = "Bundled Account" if bundle_fee < payt_total else "Pay-As-You-Transact (PAYT)"
    diff = round(abs(bundle_fee - payt_total), 2)
    ans_str = f"{cheaper_option} by {_fmt_curr(diff)}"

    prompt = (
        f"{name} is deciding between two banking fee pricing plans:\n"
        f"• **Bundled Option**: Fixed fee of {_fmt_curr(bundle_fee)} per month for unlimited electronic card swipes, ATM withdrawals, and debit orders.\n"
        f"• **Pay-As-You-Transact (PAYT) Option**: {_fmt_curr(payt_admin)} monthly admin fee plus itemised fees:\n"
        f"  - Card purchases: {_fmt_curr(swipe_rate)} each\n"
        f"  - ATM cash withdrawals: {_fmt_curr(atm_rate)} each\n"
        f"  - Debit orders: {_fmt_curr(debit_order_rate)} each\n\n"
        f"In an average month, {name} performs {debit_card_swipes} card purchases, {atm_draws} ATM withdrawals, and {debit_orders} debit orders.\n"
        f"Determine which pricing plan is cheaper and by how much."
    )
    sol = (
        f"Step 1: Calculate the total cost under PAYT:\n"
        f"• Admin fee = {_fmt_curr(payt_admin)}\n"
        f"• Card purchases = {debit_card_swipes} × {_fmt_curr(swipe_rate)} = {_fmt_curr(debit_card_swipes * swipe_rate)}\n"
        f"• ATM withdrawals = {atm_draws} × {_fmt_curr(atm_rate)} = {_fmt_curr(atm_draws * atm_rate)}\n"
        f"• Debit orders = {debit_orders} × {_fmt_curr(debit_order_rate)} = {_fmt_curr(debit_orders * debit_order_rate)}\n"
        f"• PAYT Total = {payt_admin} + {debit_card_swipes * swipe_rate:.2f} + {atm_draws * atm_rate:.2f} + {debit_orders * debit_order_rate:.2f} = {_fmt_curr(payt_total)}\n\n"
        f"Step 2: Method setup – compare with bundled fee:\n"
        f"• Bundled Fee = {_fmt_curr(bundle_fee)}\n"
        f"• Difference = |{bundle_fee} - {payt_total}| = {_fmt_curr(diff)}\n"
        f"✓ [1 Mark: Method – summing itemised PAYT costs and comparing with bundled fee]\n\n"
        f"Step 3: Final verdict:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct cheaper option and difference in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating PAYT total ({_fmt_curr(payt_total)}) and comparing to {_fmt_curr(bundle_fee)}",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate the total PAYT cost by adding the admin fee and all individual transaction charges.",
        "tier_2": f"PAYT total = {_fmt_curr(payt_total)}. Compare this with the bundled fee of {_fmt_curr(bundle_fee)}.",
        "tier_3": f"The cheaper choice is the {ans_str}."
    }
    return _make_q("bank_fee_bundled_package_vs_pay_as_you_transact", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_tiered_balance_fee_waiver(r: random.Random) -> Dict[str, Any]:
    """Calculate annual fee savings if account maintains balance above monthly waiver threshold."""
    name = r.choice(SA_NAMES)
    monthly_fee = round(r.choice([85.00, 95.00, 110.00, 120.00]), 2)
    waiver_threshold = 10000.00
    annual_savings = round(monthly_fee * 12, 2)
    ans_str = _fmt_curr(annual_savings)

    prompt = (
        f"{name}'s cheque account charges a monthly account maintenance fee of {_fmt_curr(monthly_fee)}. "
        f"The bank terms state that if the account holder maintains a minimum positive daily balance "
        f"of at least {_fmt_curr(waiver_threshold)} every day of the month, the entire monthly maintenance fee is waived (100% discount).\n\n"
        f"If {name} maintains a balance above this threshold for an entire calendar year (12 months), "
        f"calculate how much money {name} will save in bank maintenance fees over the year."
    )
    sol = (
        f"Step 1: Identify monthly savings and annual duration:\n"
        f"• Waived monthly fee = {_fmt_curr(monthly_fee)}\n"
        f"• Number of months in a year = 12\n\n"
        f"Step 2: Method setup – multiply monthly fee by 12:\n"
        f"Annual Savings = {_fmt_curr(monthly_fee)} × 12 "
        f"✓ [1 Mark: Method – multiplying waived monthly charge by 12 months]\n\n"
        f"Step 3: Calculate annual savings:\n"
        f"Annual Savings = {ans_str} ✓ [1 Mark: Accuracy – correct annual fee savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(monthly_fee)} by 12",
        f"1 Mark: Accuracy – correct annual savings {ans_str}"
    ]
    hints = {
        "tier_1": f"{name} saves {_fmt_curr(monthly_fee)} every single month.",
        "tier_2": f"Multiply the monthly fee by 12 months: {monthly_fee} × 12.",
        "tier_3": f"{monthly_fee:.2f} × 12 = {annual_savings:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_tiered_balance_fee_waiver", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_sms_notification_monthly_total(r: random.Random) -> Dict[str, Any]:
    """Calculate the total cost of SMS transaction alerts for a month."""
    name = r.choice(SA_NAMES)
    num_sms = r.choice([15, 20, 24, 28, 32, 40])
    sms_rate = round(r.choice([0.40, 0.45, 0.50]), 2)
    total_cost = round(num_sms * sms_rate, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name} subscribes to real-time SMS transaction notification alerts on a bank account. "
        f"The bank charges {_fmt_curr(sms_rate)} per SMS notification sent. "
        f"During the month, {name} received {num_sms} transaction notification SMSs. "
        f"Calculate the total SMS notification fee charged to {name}'s account for the month."
    )
    sol = (
        f"Step 1: Identify unit rate and volume of SMS alerts:\n"
        f"• Rate per SMS = {_fmt_curr(sms_rate)}\n"
        f"• Total SMS alerts received = {num_sms}\n\n"
        f"Step 2: Method setup – multiply number of alerts by unit rate:\n"
        f"Total SMS Cost = {num_sms} × {_fmt_curr(sms_rate)} "
        f"✓ [1 Mark: Method – multiplying number of SMSs by rate per SMS]\n\n"
        f"Step 3: Calculate total cost:\n"
        f"Total SMS Cost = {ans_str} ✓ [1 Mark: Accuracy – correct monthly SMS fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {num_sms} by {_fmt_curr(sms_rate)}",
        f"1 Mark: Accuracy – correct total fee {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply the number of alerts ({num_sms}) by the price per alert ({_fmt_curr(sms_rate)}).",
        "tier_2": f"Calculate: {num_sms} × {sms_rate}.",
        "tier_3": f"{num_sms} × {sms_rate:.2f} = {total_cost:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_sms_notification_monthly_total", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_fee_forex_currency_conversion_commission(r: random.Random) -> Dict[str, Any]:
    """Calculate foreign transaction fee commission charged on an international card purchase."""
    name = r.choice(SA_NAMES)
    zar_spend = r.choice([800, 1200, 1500, 2400, 3500])
    commission_pct = 2.75
    fee = round(zar_spend * (commission_pct / 100), 2)
    total_paid = round(zar_spend + fee, 2)
    ans_str = _fmt_curr(fee)

    prompt = (
        f"{name} buys an online software license from an international website. "
        f"After currency conversion, the base purchase price is {_fmt_curr(zar_spend)}. "
        f"The South African issuing bank charges a foreign transaction cross-border commission fee "
        f"of {commission_pct}% on all international card transactions. "
        f"Calculate the bank commission fee charged on this transaction."
    )
    sol = (
        f"Step 1: Identify the foreign transaction amount and bank fee percentage:\n"
        f"• Base transaction value = {_fmt_curr(zar_spend)}\n"
        f"• Cross-border commission rate = {commission_pct}%\n\n"
        f"Step 2: Method setup – calculate commission fee:\n"
        f"Commission Fee = ({commission_pct} ÷ 100) × {_fmt_curr(zar_spend)}\n"
        f"Commission Fee = {commission_pct / 100} × {zar_spend} "
        f"✓ [1 Mark: Method – multiplying ZAR value by cross-border commission rate]\n\n"
        f"Step 3: Calculate fee:\n"
        f"Commission Fee = {ans_str} ✓ [1 Mark: Accuracy – correct forex commission fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(zar_spend)} by {commission_pct}/100",
        f"1 Mark: Accuracy – correct commission fee {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate {commission_pct}% of {_fmt_curr(zar_spend)}.",
        "tier_2": f"Multiply {zar_spend} by {commission_pct / 100}.",
        "tier_3": f"{zar_spend} × {commission_pct / 100:.4f} = {fee:.2f}, giving {ans_str}."
    }
    return _make_q("bank_fee_forex_currency_conversion_commission", prompt, ans_str, sol, rubric, hints, 2, r=r)
