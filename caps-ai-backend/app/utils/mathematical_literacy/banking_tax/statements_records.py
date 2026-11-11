"""Bank Statements & Transaction Feeds Subskills (Subskills 9 to 17).

9. bank_stmt_identify_debits_and_credits
10. bank_stmt_calculate_missing_running_balance
11. bank_stmt_reconstruct_opening_balance
12. bank_stmt_calculate_total_monthly_bank_charges
13. bank_stmt_bank_charges_ratio_to_closing_balance
14. bank_stmt_bounced_debit_order_insufficient_funds
15. bank_stmt_reconcile_statement_with_receipts
16. bank_stmt_minimum_balance_interest_qualification
17. bank_stmt_e_wallet_cash_send_fee_tracking
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_stmt_identify_debits_and_credits(r: random.Random) -> Dict[str, Any]:
    """Identify whether a listed transaction on a bank statement is a debit or a credit."""
    name = r.choice(SA_NAMES)
    trans_types = [
        ("Salary electronic payment received from employer", "Credit (money paid into account)", ["Debit (money withdrawn from account)", "Neither debit nor credit", "Bank penalty fee"]),
        ("Cash withdrawal at an ATM", "Debit (money withdrawn from account)", ["Credit (money paid into account)", "Interest earned on credit balance", "Neither debit nor credit"]),
        ("Monthly debit order paid for medical aid cover", "Debit (money withdrawn from account)", ["Credit (money paid into account)", "Government tax credit", "Neither debit nor credit"]),
        ("Interest earned on positive savings account balance", "Credit (money paid into account)", ["Debit (money withdrawn from account)", "Bank administration fee", "Overdraft penalty"]),
        ("Card swipe purchase at a grocery supermarket", "Debit (money withdrawn from account)", ["Credit (money paid into account)", "Capital investment refund", "Neither debit nor credit"]),
        ("Deposit of birthday cash gift made by a relative", "Credit (money paid into account)", ["Debit (money withdrawn from account)", "Stop order payment", "Neither debit nor credit"]),
    ]
    description, ans_str, distractors = r.choice(trans_types)

    prompt = (
        f"{name} is examining a monthly bank statement. One of the line items reads:\n\n"
        f"**Transaction**: *\"{description}\"*\n\n"
        f"Classify this entry as a **debit transaction** or a **credit transaction** and explain its effect on the balance."
    )
    sol = (
        f"Step 1: Understand accounting rules for bank statements:\n"
        f"• Credit (+): Any transaction where funds enter the account (deposits, salaries, interest earned). It increases the account balance.\n"
        f"• Debit (-): Any transaction where funds leave the account (purchases, withdrawals, fees, debit orders). It decreases the account balance.\n\n"
        f"Step 2: Method setup – classify the given entry:\n"
        f"• \"{description}\"\n"
        f"✓ [1 Mark: Method – applying credit/debit criteria to banking statement ledger]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct classification]"
    )
    rubric = [
        "1 Mark: Method – distinguishing incoming funds (credit) from outgoing funds (debit)",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": "Does this transaction add money to the bank account, or does it take money out?",
        "tier_2": "Money coming in is a credit (+); money going out is a debit (-).",
        "tier_3": f"This transaction is classified as: {ans_str}."
    }
    return _make_q(
        "bank_stmt_identify_debits_and_credits",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_stmt_calculate_missing_running_balance(r: random.Random) -> Dict[str, Any]:
    """Calculate a missing running balance cell on a bank statement."""
    name = r.choice(SA_NAMES)
    start_bal = round(r.choice([3250.50, 4800.00, 5600.75, 7120.40, 8450.20]), 2)
    is_credit = r.choice([True, False])

    if is_credit:
        amt = round(r.choice([500.00, 750.00, 1200.00, 1500.00, 2400.00]), 2)
        trans_desc = f"Electronic transfer deposit from {r.choice(SA_NAMES)}"
        new_bal = round(start_bal + amt, 2)
        operation_text = f"{_fmt_curr(start_bal)} + {_fmt_curr(amt)}"
        sign_str = "+"
    else:
        amt = round(r.choice([350.00, 450.00, 680.00, 850.00, 1200.00]), 2)
        trans_desc = "Debit card purchase at Shoprite"
        new_bal = round(start_bal - amt, 2)
        operation_text = f"{_fmt_curr(start_bal)} - {_fmt_curr(amt)}"
        sign_str = "-"

    ans_str = _fmt_curr(new_bal)

    prompt = (
        f"Below is an extract from {name}'s monthly bank statement:\n\n"
        f"| Date | Description | Debit (Paid Out) | Credit (Paid In) | Running Balance |\n"
        f"| :--- | :--- | :---: | :---: | :---: |\n"
        f"| 14/03 | Balance Carried Forward | | | {_fmt_curr(start_bal)} |\n"
        f"| 15/03 | {trans_desc} | {' ' + _fmt_curr(amt) if not is_credit else ''} | {'' if not is_credit else ' ' + _fmt_curr(amt)} | **[ A ]** |\n\n"
        f"Calculate the missing running balance marked **[ A ]** on 15/03."
    )
    sol = (
        f"Step 1: Identify previous balance and transaction nature:\n"
        f"• Previous Balance = {_fmt_curr(start_bal)}\n"
        f"• Transaction: {trans_desc} ({'Credit' if is_credit else 'Debit'} of {_fmt_curr(amt)})\n\n"
        f"Step 2: Method setup for running balance calculation:\n"
        f"• Running Balance = Previous Balance {sign_str} Transaction Amount\n"
        f"• Running Balance = {operation_text} "
        f"✓ [1 Mark: Method – {'adding credit' if is_credit else 'subtracting debit'} to running balance]\n\n"
        f"Step 3: Calculate final balance:\n"
        f"Running Balance [ A ] = {ans_str} ✓ [1 Mark: Accuracy – correct running balance]"
    )
    rubric = [
        f"1 Mark: Method – setting up {operation_text}",
        f"1 Mark: Accuracy – correct balance {ans_str}"
    ]
    hints = {
        "tier_1": f"Check whether the transaction is in the Debit or Credit column.",
        "tier_2": f"Since it is a {'Credit (money in)' if is_credit else 'Debit (money out)'}, {'add it to' if is_credit else 'subtract it from'} {_fmt_curr(start_bal)}.",
        "tier_3": f"Calculate: {operation_text} = {new_bal:.2f}, giving {ans_str}."
    }
    return _make_q("bank_stmt_calculate_missing_running_balance", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_reconstruct_opening_balance(r: random.Random) -> Dict[str, Any]:
    """Reconstruct opening balance prior to a salary deposit using the first statement line."""
    name = r.choice(SA_NAMES)
    open_bal = round(r.choice([15.50, 45.20, 50.50, 84.75, 120.30, 210.25]), 2)
    salary = round(r.choice([7500.00, 8000.00, 8500.00, 9200.00, 10500.00, 12000.00]), 2)
    first_closing = round(open_bal + salary, 2)
    ans_str = _fmt_curr(open_bal)

    prompt = (
        f"{name} receives a monthly bank statement. The first line of the statement shows:\n\n"
        f"| Date | Description | Credit | Balance |\n"
        f"| :--- | :--- | :---: | :---: |\n"
        f"| 25/01 | Salary Deposit | {_fmt_curr(salary)} | {_fmt_curr(first_closing)} |\n\n"
        f"Calculate what opening balance {name} had in the account immediately BEFORE the salary deposit was processed."
    )
    sol = (
        f"Step 1: Understand running balance mechanics:\n"
        f"• New Balance = Opening Balance + Salary Deposit\n"
        f"• Therefore: Opening Balance = Balance after Salary - Salary Deposit\n\n"
        f"Step 2: Method setup – reverse the salary credit:\n"
        f"Opening Balance = {_fmt_curr(first_closing)} - {_fmt_curr(salary)} "
        f"✓ [1 Mark: Method – subtracting salary deposit from resulting balance]\n\n"
        f"Step 3: Calculate opening balance:\n"
        f"Opening Balance = {first_closing} - {salary} = {_fmt_curr(open_bal)}\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct opening balance prior to salary]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(salary)} from {_fmt_curr(first_closing)}",
        f"1 Mark: Accuracy – correct opening balance {ans_str}"
    ]
    hints = {
        "tier_1": f"The account had {_fmt_curr(first_closing)} after receiving {_fmt_curr(salary)}.",
        "tier_2": f"Subtract the salary from the closing balance: {first_closing} - {salary}.",
        "tier_3": f"{first_closing:.2f} - {salary:.2f} = {open_bal:.2f}, giving {ans_str}."
    }
    return _make_q("bank_stmt_reconstruct_opening_balance", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_calculate_total_monthly_bank_charges(r: random.Random) -> Dict[str, Any]:
    """Sum multiple bank charges and administration fees from a monthly statement."""
    name = r.choice(SA_NAMES)
    admin_fee = 5.50
    atm_fees = round(r.choice([8.00, 12.00, 16.00]), 2)
    sms_fee = round(r.choice([3.60, 4.80, 6.00]), 2)
    debit_order_fee = round(r.choice([4.50, 6.00, 9.00]), 2)
    branch_fee = round(r.choice([15.00, 20.00, 25.00]), 2)

    total_fees = round(admin_fee + atm_fees + sms_fee + debit_order_fee + branch_fee, 2)
    ans_str = _fmt_curr(total_fees)

    prompt = (
        f"{name}'s bank statement lists the following monthly fees and transaction charges:\n"
        f"• Monthly account administration fee: {_fmt_curr(admin_fee)}\n"
        f"• ATM cash withdrawal fees: {_fmt_curr(atm_fees)}\n"
        f"• SMS transaction notification alerts: {_fmt_curr(sms_fee)}\n"
        f"• Debit order processing fees: {_fmt_curr(debit_order_fee)}\n"
        f"• Branch over-the-counter service charge: {_fmt_curr(branch_fee)}\n\n"
        f"Calculate the **total bank charges** deducted from {name}'s account for the month."
    )
    sol = (
        f"Step 1: Identify all individual fee components:\n"
        f"• Admin fee: {_fmt_curr(admin_fee)}\n"
        f"• ATM fees: {_fmt_curr(atm_fees)}\n"
        f"• SMS alerts: {_fmt_curr(sms_fee)}\n"
        f"• Debit order fees: {_fmt_curr(debit_order_fee)}\n"
        f"• Branch fee: {_fmt_curr(branch_fee)}\n\n"
        f"Step 2: Method setup – sum all charges:\n"
        f"Total Fees = {_fmt_curr(admin_fee)} + {_fmt_curr(atm_fees)} + {_fmt_curr(sms_fee)} + {_fmt_curr(debit_order_fee)} + {_fmt_curr(branch_fee)} "
        f"✓ [1 Mark: Method – summing all individual banking fee items]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Fees = {ans_str} ✓ [1 Mark: Accuracy – correct sum of monthly bank charges]"
    )
    rubric = [
        "1 Mark: Method – summing all 5 fee items together",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": "Add up every fee listed in the statement extract.",
        "tier_2": f"Calculate: {admin_fee} + {atm_fees} + {sms_fee} + {debit_order_fee} + {branch_fee}.",
        "tier_3": f"Sum = {total_fees:.2f}, which is {ans_str}."
    }
    return _make_q("bank_stmt_calculate_total_monthly_bank_charges", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_bank_charges_ratio_to_closing_balance(r: random.Random) -> Dict[str, Any]:
    """Calculate the ratio and percentage of bank charges to month-end balance."""
    name = r.choice(SA_NAMES)
    fees = r.choice([45.00, 54.00, 60.00, 75.00, 90.00])
    balance = r.choice([450.00, 600.00, 650.00, 750.00, 900.00, 1200.00])
    pct = round((fees / balance) * 100, 1)
    ans_str = f"{_fmt(pct)}%"

    prompt = (
        f"{name}'s bank statement shows total monthly banking fees of {_fmt_curr(fees)}. "
        f"At month-end, {name}'s closing bank balance is {_fmt_curr(balance)}. "
        f"Express the total bank charges as a percentage of the month-end closing balance, "
        f"rounded to one decimal place."
    )
    sol = (
        f"Step 1: Set up the ratio of banking fees to closing balance:\n"
        f"• Ratio = Fees ÷ Closing Balance = {_fmt_curr(fees)} ÷ {_fmt_curr(balance)}\n\n"
        f"Step 2: Method setup – convert ratio to percentage:\n"
        f"Percentage = ({fees} ÷ {balance}) × 100% "
        f"✓ [1 Mark: Method – dividing fees by closing balance and multiplying by 100%]\n\n"
        f"Step 3: Calculate percentage:\n"
        f"Percentage = {ans_str} ✓ [1 Mark: Accuracy – correct percentage rounded to 1 dp]"
    )
    rubric = [
        f"1 Mark: Method – setting up ({fees} / {balance}) × 100%",
        f"1 Mark: Accuracy – correct percentage {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the fees ({_fmt_curr(fees)}) by the closing balance ({_fmt_curr(balance)}).",
        "tier_2": f"Multiply the result by 100 to convert to a percentage.",
        "tier_3": f"({fees} / {balance}) × 100 = {pct}%, so the answer is {ans_str}."
    }
    return _make_q("bank_stmt_bank_charges_ratio_to_closing_balance", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_bounced_debit_order_insufficient_funds(r: random.Random) -> Dict[str, Any]:
    """Calculate penalty fees and balance effect of a returned/bounced debit order due to insufficient funds."""
    name = r.choice(SA_NAMES)
    balance_before = round(r.choice([120.00, 150.50, 180.00, 220.00]), 2)
    debit_order_amt = round(r.choice([350.00, 450.00, 500.00, 650.00]), 2)
    bounced_fee = round(r.choice([55.00, 75.00, 95.00, 115.00]), 2)

    new_balance = round(balance_before - bounced_fee, 2)
    ans_str = _fmt_curr(new_balance)

    prompt = (
        f"{name}'s cheque account has an available balance of {_fmt_curr(balance_before)}. "
        f"An insurance debit order of {_fmt_curr(debit_order_amt)} is presented for payment. "
        f"Because the available balance is insufficient, the bank declines the transaction "
        f"and charges an unpaid / returned debit order penalty fee of {_fmt_curr(bounced_fee)}. "
        f"Calculate {name}'s new bank balance after this penalty fee is deducted."
    )
    sol = (
        f"Step 1: Understand returned debit order mechanics:\n"
        f"• The original debit order of {_fmt_curr(debit_order_amt)} is NOT paid (bounced).\n"
        f"• The bank deducts an unpaid penalty fee of {_fmt_curr(bounced_fee)} from the existing balance.\n\n"
        f"Step 2: Method setup – deduct penalty fee from starting balance:\n"
        f"New Balance = Starting Balance - Penalty Fee\n"
        f"New Balance = {_fmt_curr(balance_before)} - {_fmt_curr(bounced_fee)} "
        f"✓ [1 Mark: Method – deducting unpaid debit order penalty fee from available balance]\n\n"
        f"Step 3: Calculate remaining balance:\n"
        f"New Balance = {balance_before} - {bounced_fee} = {ans_str} "
        f"✓ [1 Mark: Accuracy – correct resulting bank balance]"
    )
    rubric = [
        f"1 Mark: Method – subtracting penalty fee {_fmt_curr(bounced_fee)} from balance {_fmt_curr(balance_before)}",
        f"1 Mark: Accuracy – correct new balance {ans_str}"
    ]
    hints = {
        "tier_1": f"The debit order itself was not paid, so only the penalty fee ({_fmt_curr(bounced_fee)}) was deducted.",
        "tier_2": f"Subtract: {balance_before:.2f} - {bounced_fee:.2f}.",
        "tier_3": f"{balance_before:.2f} - {bounced_fee:.2f} = {new_balance:.2f}, giving {ans_str}."
    }
    return _make_q("bank_stmt_bounced_debit_order_insufficient_funds", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_reconcile_statement_with_receipts(r: random.Random) -> Dict[str, Any]:
    """Reconcile paper till slips / card receipts with bank statement to detect an unrecognized charge."""
    name = r.choice(SA_NAMES)
    known_swipes = [
        ("Pick n Pay", round(r.choice([145.50, 220.00, 310.20]), 2)),
        ("Total Garage Fuel", round(r.choice([450.00, 500.00, 600.00]), 2)),
        ("Clicks Pharmacy", round(r.choice([89.90, 115.50, 160.00]), 2)),
    ]
    mystery_amt = round(r.choice([99.00, 149.00, 199.00, 250.00]), 2)
    mystery_desc = "Unknown Online Subscription POS"

    ans_str = _fmt_curr(mystery_amt)

    prompt = (
        f"{name} keeps paper till receipts for three purchases made during the week:\n"
        f"1. {known_swipes[0][0]}: {_fmt_curr(known_swipes[0][1])}\n"
        f"2. {known_swipes[1][0]}: {_fmt_curr(known_swipes[1][1])}\n"
        f"3. {known_swipes[2][0]}: {_fmt_curr(known_swipes[2][1])}\n\n"
        f"When checking the online bank statement, the total debits for the week equal "
        f"{_fmt_curr(sum(s[1] for s in known_swipes) + mystery_amt)}, including an unrecognized entry titled "
        f"*\"{mystery_desc}\"*. Calculate the amount of this unrecognized charge."
    )
    sol = (
        f"Step 1: Calculate the sum of verified paper till slips:\n"
        f"Verified Total = {_fmt_curr(known_swipes[0][1])} + {_fmt_curr(known_swipes[1][1])} + {_fmt_curr(known_swipes[2][1])} "
        f"= {_fmt_curr(sum(s[1] for s in known_swipes))}\n\n"
        f"Step 2: Method setup – subtract verified total from statement debits:\n"
        f"Discrepancy = Total Statement Debits - Verified Slips\n"
        f"Discrepancy = {_fmt_curr(sum(s[1] for s in known_swipes) + mystery_amt)} - {_fmt_curr(sum(s[1] for s in known_swipes))} "
        f"✓ [1 Mark: Method – subtracting sum of known slips from total statement debits]\n\n"
        f"Step 3: Calculate unrecognized amount:\n"
        f"Discrepancy = {ans_str} ✓ [1 Mark: Accuracy – correct unreconciled charge]"
    )
    rubric = [
        "1 Mark: Method – summing verified receipts and finding difference with bank statement",
        f"1 Mark: Accuracy – correct charge {ans_str}"
    ]
    hints = {
        "tier_1": "Sum the three till slip receipts first.",
        "tier_2": "Subtract the sum of receipts from the total debits shown on the bank statement.",
        "tier_3": f"The difference is {ans_str}."
    }
    return _make_q("bank_stmt_reconcile_statement_with_receipts", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_stmt_minimum_balance_interest_qualification(r: random.Random) -> Dict[str, Any]:
    """Evaluate whether an account qualified for interest based on maintaining a minimum threshold balance."""
    name = r.choice(SA_NAMES)
    min_req = 2500.00
    dip_below = r.choice([True, False])

    if dip_below:
        lowest_bal = round(r.choice([1850.00, 2100.50, 2350.00, 2480.00]), 2)
        ans_str = f"No, because the balance dropped to {_fmt_curr(lowest_bal)}, which is below the R 2 500,00 minimum requirement"
        distractors = [
            f"Yes, because the closing balance ended above R 2 500,00",
            f"Yes, because minimum balance rules only apply on the first day of the month",
            f"No, because the account holder must have at least R 10 000,00 to earn any interest"
        ]
        explanation = f"On one day, the balance dropped to {_fmt_curr(lowest_bal)}, violating the continuous R 2 500,00 threshold."
    else:
        lowest_bal = round(r.choice([2550.00, 2700.00, 3100.00, 3450.00]), 2)
        ans_str = f"Yes, because the balance remained at or above R 2 500,00 throughout the entire month (lowest balance was {_fmt_curr(lowest_bal)})"
        distractors = [
            f"No, because the bank requires a fixed deposit to earn interest",
            f"No, because the balance must reach R 5 000,00 every month",
            f"Yes, but only if no debit card purchases were made"
        ]
        explanation = f"The lowest balance was {_fmt_curr(lowest_bal)}, which remained above the R 2 500,00 minimum throughout the cycle."

    prompt = (
        f"{name}'s savings account terms specify: *\"To earn credit interest, the account must maintain "
        f"a minimum daily balance of at least R 2 500,00 throughout the entire monthly statement cycle.\"*\n\n"
        f"During the month, {name}'s lowest recorded daily balance was {_fmt_curr(lowest_bal)}. "
        f"Did {name}'s account qualify to earn interest for this month?"
    )
    sol = (
        f"Step 1: Identify bank term condition:\n"
        f"• Minimum daily balance requirement = R 2 500,00\n"
        f"• Account's lowest recorded daily balance = {_fmt_curr(lowest_bal)}\n\n"
        f"Step 2: Method setup – compare lowest balance with requirement:\n"
        f"• {explanation}\n"
        f"✓ [1 Mark: Method – comparing daily minimum balance against policy threshold]\n\n"
        f"Step 3: Final Determination:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct qualification verdict]"
    )
    rubric = [
        "1 Mark: Method – evaluating daily minimum balance against R 2 500,00 threshold",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": f"Compare {name}'s lowest daily balance ({_fmt_curr(lowest_bal)}) to the minimum requirement of R 2 500,00.",
        "tier_2": f"If the lowest balance is less than R 2 500,00, the condition is not met.",
        "tier_3": f"The correct verdict is: {ans_str}."
    }
    return _make_q(
        "bank_stmt_minimum_balance_interest_qualification",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_stmt_e_wallet_cash_send_fee_tracking(r: random.Random) -> Dict[str, Any]:
    """Calculate the fee for sending money via eWallet / Instant Money / CashSend."""
    name = r.choice(SA_NAMES)
    recipient = r.choice(SA_NAMES)
    send_amt = r.choice([250, 400, 500, 750, 1000, 1500])

    # Fee tier: R0-R500: R9.50; R501-R1500: R14.00
    if send_amt <= 500:
        fee = 9.50
    else:
        fee = 14.00

    total_debited = round(send_amt + fee, 2)
    ans_str = _fmt_curr(total_debited)

    prompt = (
        f"{name} uses mobile banking to send {_fmt_curr(send_amt)} to {recipient} via eWallet / Instant Money. "
        f"The bank fee schedule charges an electronic transfer fee of {_fmt_curr(fee)} for this amount. "
        f"Calculate the **total amount debited** from {name}'s bank account to complete the transfer."
    )
    sol = (
        f"Step 1: Identify transfer amount and service fee:\n"
        f"• Amount sent to recipient = {_fmt_curr(send_amt)}\n"
        f"• Bank cashsend fee = {_fmt_curr(fee)}\n\n"
        f"Step 2: Method setup – calculate total debit to sender's account:\n"
        f"Total Debited = Transfer Amount + Bank Fee\n"
        f"Total Debited = {_fmt_curr(send_amt)} + {_fmt_curr(fee)} "
        f"✓ [1 Mark: Method – adding transfer amount to bank processing fee]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Debited = {ans_str} ✓ [1 Mark: Accuracy – correct total debited amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – adding {_fmt_curr(send_amt)} and {_fmt_curr(fee)}",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"The sender must pay both the money being sent ({_fmt_curr(send_amt)}) and the transaction fee ({_fmt_curr(fee)}).",
        "tier_2": f"Add the two amounts: {send_amt} + {fee}.",
        "tier_3": f"{send_amt} + {fee:.2f} = {total_debited:.2f}, giving {ans_str}."
    }
    return _make_q("bank_stmt_e_wallet_cash_send_fee_tracking", prompt, ans_str, sol, rubric, hints, 2, r=r)
