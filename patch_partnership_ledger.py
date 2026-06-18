import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\partnership_ledger_generator.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. _make_current_account_question
old_prompt_1 = """    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Current Account of {partner} and close off the account.

#### INFORMATION:
Use the balances/totals and partnership agreement information provided.\"\"\""""

new_prompt_1 = """    info_lines = [
        f"- Balance at beginning of the year: {_fmt_amount(opening)} ({'Credit' if opening_is_credit else 'Debit'})",
        f"- Total drawings for the year: {_fmt_amount(drawings)}",
        f"- Interest on capital for the year: {_fmt_amount(interest_on_capital)}",
        f"- Partner's salary for the year: {_fmt_amount(salary)}"
    ]
    if bonus > 0:
        info_lines.append(f"- Bonus awarded for the year: {_fmt_amount(bonus)}")

    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Current Account of {partner} and close off the account.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_1, new_prompt_1)

# 2. _make_appropriation_account_question
old_prompt_2 = """    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Appropriation Account for the year ended {year}. Feb 28.

#### INFORMATION:
Distribute net profit according to interest on capital, salaries/bonuses and remaining profit share.\"\"\""""

new_prompt_2 = """    info_lines = [
        f"- Net profit for the year: {_fmt_amount(net_profit)}",
        f"- Partner salaries: {partner_a} {_fmt_amount(salary_a)} ; {partner_b} {_fmt_amount(salary_b)}",
        f"- Interest on capital: {partner_a} {_fmt_amount(interest_a)} ; {partner_b} {_fmt_amount(interest_b)}"
    ]
    if bonus_a > 0 or bonus_b > 0:
        info_lines.append(f"- Bonuses: {partner_a} {_fmt_amount(bonus_a)} ; {partner_b} {_fmt_amount(bonus_b)}")
    info_lines.append("- The partners share the remaining profit or loss equally.")

    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Appropriation Account for the year ended {year}. Feb 28.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_2, new_prompt_2)


# 3. _make_capital_account_question
old_prompt_3 = """    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Capital Account of {partner} and close off the account.

#### INFORMATION:
Include any additional capital contributions or capital withdrawals during the year.\"\"\""""

new_prompt_3 = """    info_lines = [
        f"- Balance at the beginning of the year: {_fmt_amount(opening_capital)}",
        f"- Additional capital contributed during the year: {_fmt_amount(add_capital)}"
    ]
    if withdraw_capital > 0:
        info_lines.append(f"- Capital withdrawn during the year: {_fmt_amount(withdraw_capital)}")

    prompt = f\"\"\"Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Capital Account of {partner} and close off the account.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_3, new_prompt_3)

# 4. _make_cash_journals_eft_update_question
old_prompt_4 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Update the Cash Journals by completing the table provided in the answer book.

#### INFORMATION:
The business uses EFTs. Use the bank statement information for {month} {year}.\"\"\""""

new_prompt_4 = """    info_lines = [
        f"- Provisional CRJ total before bank statement items: {_fmt_amount(crj_total_bf)}",
        f"- Provisional CPJ total before bank statement items: {_fmt_amount(cpj_total_bf)}",
        "The following items appeared on the bank statement but not in the journals:",
        f"  * Rent income received via EFT: {_fmt_amount(rent_income)}",
        f"  * Payment received from debtor in settlement of account: {_fmt_amount(debtor_settlement)}",
        f"  * Rates and taxes paid via EFT: {_fmt_amount(rates)}",
        f"  * Bank charges: {_fmt_amount(bank_charges)}",
        f"  * Trading stock purchased via EFT: {_fmt_amount(trading_stock)}",
        f"  * Interest charged on overdraft: {_fmt_amount(interest_overdraft)}",
        f"  * Insurance premium paid via debit order: {_fmt_amount(insurance)}",
        f"  * Partner's personal drawings paid via EFT: {_fmt_amount(drawings)}"
    ]

    prompt = f\"\"\"{business}

#### REQUIRED:
Update the Cash Journals by completing the table provided in the answer book.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_4, new_prompt_4)

# 5. _make_adjustments_effect_matrix
old_prompt_5 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Show the effect of each adjustment on the accounting equation AND indicate the account to debit and the account to credit.

#### INFORMATION:
Use the adjustment descriptions provided in the question paper.\"\"\""""

new_prompt_5 = """    info_lines = [
        "1.1 Received R2,000 from a debtor whose account was previously written off.",
        "1.2 Trading stock to the value of R1,500 was taken by a partner for personal use.",
        "1.3 Interest on capital of R5,000 must be recorded for a partner.",
        "1.4 Provide for outstanding audit fees of R3,000."
    ]

    prompt = f\"\"\"{business}

#### REQUIRED:
Show the effect of each adjustment on the accounting equation AND indicate the account to debit and the account to credit.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_5, new_prompt_5)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched partnership_ledger_generator.py")
