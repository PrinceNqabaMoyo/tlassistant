"""Bank Accounts, Terminology & FICA Regulations Subskills (Subskills 1 to 8).

1. bank_acc_types_comparison_savings_cheque_fixed
2. bank_acc_fica_requirements_verification
3. bank_acc_debit_vs_credit_card_mechanics
4. bank_acc_overdraft_facility_interest_cost
5. bank_acc_stop_order_vs_debit_order
6. bank_acc_notice_deposit_penalty_terms
7. bank_acc_atms_branch_electronic_comparison
8. bank_acc_security_fraud_prevention_pin
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_BANKS, SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_bank_acc_types_comparison_savings_cheque_fixed(r: random.Random) -> Dict[str, Any]:
    """Compare bank account types (savings, cheque/current, fixed deposit)."""
    name = r.choice(SA_NAMES)
    scenarios = [
        (
            "has received a lump-sum inheritance of R 40 000 and wants to lock it away for 24 months to earn the highest guaranteed interest rate without touching it.",
            "Fixed deposit account",
            ["Savings account", "Cheque account", "Credit card account"],
            "Fixed deposit accounts offer the highest interest rates because money is committed for an agreed fixed term without premature withdrawals."
        ),
        (
            "is a newly employed teacher earning a monthly salary of R 18 500, requiring an account for salary deposits, automated monthly debit orders, and an optional overdraft facility.",
            "Cheque / Current account",
            ["Savings account", "Fixed deposit account", "32-day notice account"],
            "A cheque or current account is designed for regular income deposits, debit orders, and allows an agreed overdraft facility."
        ),
        (
            "is a Grade 10 learner who saves small amounts of pocket money monthly and needs immediate access to withdraw funds for school stationery and transport.",
            "Savings account",
            ["Fixed deposit account", "Cheque / Current account", "Credit card account"],
            "A savings account is ideal for saving smaller discretionary amounts with immediate liquidity and without requiring proof of regular salary."
        ),
    ]
    scenario_text, ans_str, distractors, explanation_reason = r.choice(scenarios)

    prompt = (
        f"{name} {scenario_text}\n\n"
        f"Which type of bank account is most appropriate for {name}'s requirements?"
    )
    sol = (
        f"Step 1: Identify the user's financial profile and transactional requirements:\n"
        f"• {explanation_reason}\n\n"
        f"Step 2: Method setup – compare account characteristics:\n"
        f"• Savings account: Short-term liquidity, modest interest, no overdraft.\n"
        f"• Cheque account: Day-to-day transactions, debit orders, salary deposits, overdraft option.\n"
        f"• Fixed deposit: Lump sum locked for fixed duration, higher guaranteed return.\n"
        f"✓ [1 Mark: Method – matching financial requirements with bank account characteristics]\n\n"
        f"Step 3: Final Selection:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct account type identified]"
    )
    rubric = [
        "1 Mark: Method – evaluating account capabilities against client needs",
        f"1 Mark: Accuracy – correct account type: {ans_str}"
    ]
    hints = {
        "tier_1": "Consider whether the funds need to be locked away for interest, used for daily transactions, or saved informally.",
        "tier_2": "Fixed deposits lock money away; cheque accounts handle regular salaries and debit orders; savings accounts offer flexible deposits.",
        "tier_3": f"For this scenario, the most suitable choice is the {ans_str}."
    }
    return _make_q(
        "bank_acc_types_comparison_savings_cheque_fixed",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_acc_fica_requirements_verification(r: random.Random) -> Dict[str, Any]:
    """Verify statutory documents required by FICA when opening a South African bank account."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)

    missing_doc = r.choice([
        ("Proof of residential address not older than 3 months (e.g. utility bill or lease agreement)", "Utility bill / proof of residential address"),
        ("Green barcoded South African ID book or smart ID card", "Valid green ID book or smart ID card"),
        ("Proof of income or employment (e.g. recent payslip or 3-month bank statement)", "Proof of income / 3-month bank statement")
    ])

    prompt = (
        f"{name} visits a {bank} branch to open a new cheque account under South African law "
        f"(FICA – Financial Intelligence Centre Act). {name} brings a certified matric certificate, "
        f"a valid South African Smart ID card, and a recent employment letter. "
        f"However, the bank consultant explains that one critical mandatory FICA document is missing. "
        f"Identify the missing document {name} must provide."
    )
    ans_str = "Proof of residential address not older than 3 months"
    distractors = [
        "Original grade 12 NSC certificate",
        "South African driver's license card",
        "Police clearance affidavit"
    ]
    sol = (
        f"Step 1: Understand FICA statutory requirements for opening an account:\n"
        f"• Under the Financial Intelligence Centre Act (FICA), banks must verify:\n"
        f"  1. Proof of identity (valid South African Smart ID or passport).\n"
        f"  2. Proof of residential address (municipal utility bill, formal lease, not older than 3 months).\n"
        f"  3. Proof of income / source of funds.\n\n"
        f"Step 2: Method setup – identify what is present vs missing:\n"
        f"• Present: Smart ID card (Identity), employment letter (Income source).\n"
        f"• Missing: Proof of residential address.\n"
        f"✓ [1 Mark: Method – identifying missing statutory FICA compliance document]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct missing FICA document]"
    )
    rubric = [
        "1 Mark: Method – identifying the three core pillars of FICA verification",
        f"1 Mark: Accuracy – identifying {ans_str}"
    ]
    hints = {
        "tier_1": "FICA requires proof of who you are, where you live, and where your money comes from.",
        "tier_2": "The client has provided proof of identity and proof of employment, but not where they reside.",
        "tier_3": f"The client must provide a {ans_str} (e.g. a water or electricity bill)."
    }
    return _make_q(
        "bank_acc_fica_requirements_verification",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_acc_debit_vs_credit_card_mechanics(r: random.Random) -> Dict[str, Any]:
    """Distinguish operational mechanics between debit card and credit card transactions."""
    name = r.choice(SA_NAMES)
    purchase_amt = r.choice([350, 480, 650, 890, 1200, 1500])

    prompt = (
        f"{name} purchases groceries worth {_fmt_curr(purchase_amt)} at a supermarket. "
        f"Explain what happens to {name}'s bank balance when {name} uses a **debit card** "
        f"compared to using a **credit card**."
    )
    ans_str = "Debit card immediately deducts money from the bank balance; credit card borrows money from the bank's credit limit to be settled later"
    distractors = [
        "Credit card immediately deducts money from the bank balance; debit card borrows funds with 55 days interest-free",
        "Both debit and credit cards immediately deduct money from the account balance at the till point",
        "Debit cards charge monthly interest on the purchase; credit cards do not charge interest under any circumstances"
    ]
    sol = (
        f"Step 1: Understand payment card mechanisms:\n"
        f"• Debit card: Linked directly to the account holder's personal deposit funds. "
        f"The transaction of {_fmt_curr(purchase_amt)} is deducted immediately from the account balance.\n"
        f"• Credit card: Linked to a revolving line of credit provided by the financial institution. "
        f"The bank pays the merchant, and the cardholder owes the bank, paying it back later.\n\n"
        f"Step 2: Method setup – compare cash flow timing:\n"
        f"• Debit = 'Pay now' from own funds.\n"
        f"• Credit = 'Pay later' using bank's borrowed funds (with interest if not paid within grace period).\n"
        f"✓ [1 Mark: Method – contrasting instantaneous debit deduction with deferred credit repayment]\n\n"
        f"Step 3: Final Explanation:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct distinction]"
    )
    rubric = [
        "1 Mark: Method – contrasting immediate deduction (debit) with credit facility (credit)",
        "1 Mark: Accuracy – correct conceptual identification"
    ]
    hints = {
        "tier_1": "Think about whose money is being spent at the exact moment the card is swiped.",
        "tier_2": "A debit card spends money already in your bank account; a credit card borrows money from the bank.",
        "tier_3": f"The correct answer states: {ans_str}."
    }
    return _make_q(
        "bank_acc_debit_vs_credit_card_mechanics",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_acc_overdraft_facility_interest_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the interest penalty charged on a negative cheque account overdraft balance."""
    name = r.choice(SA_NAMES)
    overdraft_amt = r.choice([1500, 2000, 2500, 3000, 4000, 5000])
    annual_rate = r.choice([18.0, 20.5, 21.0, 22.5, 24.0])
    days = r.choice([15, 20, 25, 30])

    # Interest = P * r * (days / 365)
    interest_val = round(overdraft_amt * (annual_rate / 100) * (days / 365), 2)
    ans_str = _fmt_curr(interest_val)

    prompt = (
        f"{name}'s cheque account has an agreed overdraft facility. During the month, {name}'s account "
        f"drops into a negative balance of -{_fmt_curr(overdraft_amt)} for a period of {days} days. "
        f"The bank charges an overdraft interest rate of {_fmt(annual_rate)}% per annum, calculated on a 365-day year. "
        f"Calculate the overdraft interest fee charged to {name}'s account for these {days} days."
    )
    sol = (
        f"Step 1: Understand overdraft interest calculation:\n"
        f"• Overdrawn amount = {_fmt_curr(overdraft_amt)}\n"
        f"• Annual interest rate = {_fmt(annual_rate)}% = {annual_rate / 100}\n"
        f"• Duration = {days} days out of 365 days in a year\n\n"
        f"Step 2: Method setup using simple interest formula for daily accrual:\n"
        f"Interest = Principal × Rate × (Days ÷ 365)\n"
        f"Interest = {_fmt_curr(overdraft_amt)} × ({annual_rate}/100) × ({days}/365) "
        f"✓ [1 Mark: Method – applying daily proration to annual overdraft rate]\n\n"
        f"Step 3: Calculate interest cost:\n"
        f"Interest = {overdraft_amt} × {annual_rate / 100} × ({days}/365) = {_fmt_curr(interest_val)}\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct overdraft fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(overdraft_amt)} by {annual_rate}% × ({days}/365)",
        f"1 Mark: Accuracy – correct interest fee {ans_str}"
    ]
    hints = {
        "tier_1": f"The annual interest rate is {_fmt(annual_rate)}%, but the funds were overdrawn for only {days} days.",
        "tier_2": f"Calculate: {overdraft_amt} × ({annual_rate}/100) × ({days}/365).",
        "tier_3": f"{overdraft_amt} × {annual_rate/100:.4f} × {days/365:.4f} = {interest_val:.2f}, giving {ans_str}."
    }
    return _make_q("bank_acc_overdraft_facility_interest_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_acc_stop_order_vs_debit_order(r: random.Random) -> Dict[str, Any]:
    """Distinguish between a stop order and a debit order."""
    name = r.choice(SA_NAMES)
    company = r.choice(["Vodacom", "MTN", "Discovery Health", "City of Johannesburg", "Old Mutual"])

    prompt = (
        f"{name} wants to set up automated recurring payments from a cheque account. "
        f"What is the key difference between a **debit order** (e.g. for {company}) "
        f"and a **stop order** (e.g. for a fixed monthly savings transfer)?"
    )
    ans_str = "A debit order is an authorization given to a third-party company to collect varying or fixed amounts, whereas a stop order is an instruction given directly to your bank to pay a fixed amount"
    distractors = [
        "A stop order can only be used for credit card repayments, while a debit order is for cash withdrawals only",
        "A debit order is an instruction given to your bank for fixed amounts only, while a stop order is managed entirely by third parties",
        "There is no difference between a debit order and a stop order under South African banking regulations"
    ]
    sol = (
        f"Step 1: Understand automated transaction definitions:\n"
        f"• Debit order: The account holder authorizes a third-party service provider ({company}) "
        f"to withdraw money directly from their account. The amount can vary monthly (e.g. cell phone usage or electricity).\n"
        f"• Stop order: The account holder instructs their own bank to transfer a strictly fixed amount of money "
        f"at regular specified intervals (e.g. paying fixed rent or recurring savings deposit).\n\n"
        f"Step 2: Method setup – contrast origin and flexibility:\n"
        f"• Debit order: Authorized to external company, variable or fixed amounts.\n"
        f"• Stop order: Instructed to own bank, strictly fixed amounts.\n"
        f"✓ [1 Mark: Method – identifying distinction between third-party collection vs bank instruction]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct distinction]"
    )
    rubric = [
        "1 Mark: Method – recognizing that debit orders authorize third parties while stop orders instruct the bank",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": "Consider who initiates the deduction: the third-party company or your own bank.",
        "tier_2": "A third party collects via debit order; you instruct your bank directly via stop order.",
        "tier_3": f"The correct definition is: {ans_str}."
    }
    return _make_q(
        "bank_acc_stop_order_vs_debit_order",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_bank_acc_notice_deposit_penalty_terms(r: random.Random) -> Dict[str, Any]:
    """Calculate the early withdrawal penalty fee on a 32-day notice deposit account."""
    name = r.choice(SA_NAMES)
    deposit_val = r.choice([10000, 15000, 20000, 25000, 30000, 50000])
    penalty_pct = r.choice([2.0, 2.5, 3.0, 3.5, 5.0])
    penalty_fee = round(deposit_val * penalty_pct / 100, 2)
    ans_str = _fmt_curr(penalty_fee)

    prompt = (
        f"{name} invested {_fmt_curr(deposit_val)} in a 32-day notice deposit account. "
        f"Due to an urgent household emergency, {name} withdraws the entire funds immediately "
        f"without giving the required 32 days' notice. "
        f"The bank terms state that an early withdrawal penalty fee of {_fmt(penalty_pct)}% of the withdrawn balance "
        f"will be deducted. Calculate the penalty fee {name} will be charged."
    )
    sol = (
        f"Step 1: Identify notice deposit conditions and penalty rule:\n"
        f"• Withdrawn balance = {_fmt_curr(deposit_val)}\n"
        f"• Penalty rate for failing to give 32 days notice = {_fmt(penalty_pct)}%\n\n"
        f"Step 2: Method setup – calculate percentage fee:\n"
        f"Penalty = ({penalty_pct} ÷ 100) × {_fmt_curr(deposit_val)}\n"
        f"Penalty = {penalty_pct / 100} × {deposit_val} "
        f"✓ [1 Mark: Method – applying penalty percentage to withdrawn funds]\n\n"
        f"Step 3: Calculate final fee:\n"
        f"Penalty = {ans_str} ✓ [1 Mark: Accuracy – correct penalty fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(deposit_val)} by {penalty_pct}/100",
        f"1 Mark: Accuracy – correct penalty fee {ans_str}"
    ]
    hints = {
        "tier_1": f"Find {_fmt(penalty_pct)}% of the total amount of {_fmt_curr(deposit_val)}.",
        "tier_2": f"Multiply {deposit_val} by {penalty_pct / 100}.",
        "tier_3": f"{deposit_val} × {penalty_pct / 100} = {penalty_fee:.2f}, giving {ans_str}."
    }
    return _make_q("bank_acc_notice_deposit_penalty_terms", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_acc_atms_branch_electronic_comparison(r: random.Random) -> Dict[str, Any]:
    """Compare cash withdrawal channels (supermarket till point vs own bank ATM vs other bank ATM vs branch teller)."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)

    till_fee = 1.50
    own_atm_fee = 4.50
    other_atm_fee = 10.50
    branch_teller_fee = 25.00

    draw_amt = r.choice([200, 300, 400, 500])

    prompt = (
        f"{name} holds an account with {bank} and needs to withdraw {_fmt_curr(draw_amt)} in cash. "
        f"The bank fee schedule lists the following withdrawal fees:\n"
        f"• Supermarket till point cashout: {_fmt_curr(till_fee)}\n"
        f"• {bank} native ATM: {_fmt_curr(own_atm_fee)}\n"
        f"• Another bank's ATM: {_fmt_curr(other_atm_fee)}\n"
        f"• Branch teller over the counter: {_fmt_curr(branch_teller_fee)}\n\n"
        f"Calculate how much money {name} saves by withdrawing cash at the supermarket till point "
        f"instead of at the branch teller counter."
    )
    savings = round(branch_teller_fee - till_fee, 2)
    ans_str = _fmt_curr(savings)

    sol = (
        f"Step 1: Identify fees for both withdrawal channels:\n"
        f"• Branch teller counter fee = {_fmt_curr(branch_teller_fee)}\n"
        f"• Supermarket till point cashout fee = {_fmt_curr(till_fee)}\n\n"
        f"Step 2: Method setup – calculate difference (savings):\n"
        f"Savings = Branch Teller Fee - Till Point Fee\n"
        f"Savings = {_fmt_curr(branch_teller_fee)} - {_fmt_curr(till_fee)} "
        f"✓ [1 Mark: Method – subtracting supermarket till fee from branch teller fee]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {_fmt_curr(till_fee)} from {_fmt_curr(branch_teller_fee)}",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Compare the cost of using the branch teller ({_fmt_curr(branch_teller_fee)}) with the till point ({_fmt_curr(till_fee)}).",
        "tier_2": f"Subtract: {branch_teller_fee:.2f} - {till_fee:.2f}.",
        "tier_3": f"{branch_teller_fee:.2f} - {till_fee:.2f} = {savings:.2f}, which is {ans_str}."
    }
    return _make_q("bank_acc_atms_branch_electronic_comparison", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_bank_acc_security_fraud_prevention_pin(r: random.Random) -> Dict[str, Any]:
    """Identify best practices for digital banking security and fraud prevention."""
    name = r.choice(SA_NAMES)
    scenarios = [
        (
            f"{name} receives an urgent SMS stating that their bank account has been suspended and requesting them to click an unknown link to type in their 5-digit PIN and OTP (One Time PIN).",
            "Delete the SMS immediately and never share the PIN or OTP, as authentic banks never request security PINs via SMS or web links",
            [
                "Click the link immediately to verify identity before the account is closed",
                "Reply to the SMS with the 5-digit PIN so the bank can verify ownership",
                "Forward the OTP to the number provided in the SMS"
            ]
        ),
        (
            f"While withdrawing cash at an ATM, a friendly stranger offers to assist {name} by inserting the card and asking {name} to read out their Secret PIN.",
            "Decline all assistance from strangers, cancel the transaction, and ensure the PIN is concealed from view at all times",
            [
                "Allow the stranger to assist, but only give them the last two digits of the PIN",
                "Hand the card to the stranger so they can wipe the chip with a cloth",
                "Write the PIN on the back of the card so it is easy to read"
            ]
        ),
    ]
    scenario_prompt, ans_str, distractors = r.choice(scenarios)

    prompt = (
        f"{scenario_prompt}\n\n"
        f"What is the correct and secure action {name} should take according to South African banking fraud guidelines?"
    )
    sol = (
        f"Step 1: Understand digital banking security principles:\n"
        f"• Bank PINs, passwords, and OTPs are confidential to the account holder.\n"
        f"• Authentic South African financial institutions never solicit private PINs or OTPs via SMS, email, or telephone.\n\n"
        f"Step 2: Method setup – identify fraud risk:\n"
        f"• Unsolicited links and requests for security credentials represent phishing and card-skimming threats.\n"
        f"✓ [1 Mark: Method – evaluating transaction security risk and identifying correct safety protocol]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct security response]"
    )
    rubric = [
        "1 Mark: Method – identifying banking safety and anti-fraud protocols",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": "Remember that your PIN and OTP must never be shared with anyone, not even someone claiming to be a bank official.",
        "tier_2": "Banks never ask for your confidential PIN or OTP via text message or telephone.",
        "tier_3": f"The correct action is: {ans_str}."
    }
    return _make_q(
        "bank_acc_security_fraud_prevention_pin",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )
