import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\reconciliation_generator.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: _make_bank_reconciliation_statement
old_prompt_1 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Bank Reconciliation Statement as at {day} {month} {year}.2.

#### INFORMATION:
Use the given bank statement balance and the outstanding deposits and cheques.\"\"\""""

new_prompt_1 = """    info_lines = []
    if bank_statement_favourable:
        info_lines.append(f"- Favourable balance as per bank statement: {_money(bank_statement_amount)}")
    else:
        info_lines.append(f"- Unfavourable balance as per bank statement: {_money(bank_statement_amount)}")
    
    info_lines.append("- Outstanding deposits:")
    for i, dep in enumerate(outstanding_deposits, start=1):
        info_lines.append(f"  * Deposit {i}: {_money(dep)}")
    
    info_lines.append("- Outstanding cheques:")
    for no, amt in cheques:
        info_lines.append(f"  * Cheque No. {no}: {_money(amt)}")
        
    if bank_account_unfavourable:
        info_lines.append(f"- Unfavourable balance as per Bank account: {_money(bank_account_amount)}")
    else:
        info_lines.append(f"- Favourable balance as per Bank account: {_money(bank_account_amount)}")

    prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Bank Reconciliation Statement as at {day} {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_1, new_prompt_1)

# Fix 2: _make_bank_reconciliation_full_workflow_bundle -> part_totals
old_prompt_2 = """    totals_prompt = f\"\"\"{business}

#### REQUIRED:
Calculate the correct totals for the Cash Receipts Journal and Cash Payments Journal for {month} {year}.2.

#### INFORMATION:
Provisional totals are given. Additional items from the bank statement must be recorded in the relevant journal.\"\"\""""

new_prompt_2 = """    info_lines = [
        f"- Provisional CRJ total: {_money(crj_prov)}",
        f"- Provisional CPJ total: {_money(cpj_prov)}",
        "Additional items from the bank statement not yet recorded:"
    ]
    if direct_deposit_rent: info_lines.append(f"  * Direct deposit for rent: {_money(direct_deposit_rent)}")
    if interest_income: info_lines.append(f"  * Interest income: {_money(interest_income)}")
    if bank_charges: info_lines.append(f"  * Bank charges: {_money(bank_charges)}")
    if debit_order_insurance: info_lines.append(f"  * Debit order for insurance: {_money(debit_order_insurance)}")
    if dishonoured_cheque: info_lines.append(f"  * Dishonoured cheque: {_money(dishonoured_cheque)}")

    totals_prompt = f\"\"\"{business}

#### REQUIRED:
Calculate the correct totals for the Cash Receipts Journal and Cash Payments Journal for {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_2, new_prompt_2)


# Fix 3: _make_creditors_reconciliation_statement_and_control_bundle -> rs_prompt
old_prompt_3 = """    rs_prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Creditors Reconciliation Statement for {month} {year}.2 after comparing the creditor's ledger with the statement received from {supplier}.

#### INFORMATION:
Use the given balance and adjustments to reconcile to the correct ledger balance.\"\"\""""

new_prompt_3 = """    info_lines = [
        f"- Balance as per statement from {supplier}: {_money(bal_statement)}",
        f"- Discount omitted from the statement: {_money(disc_omitted)}",
        f"- Invoice recorded on another account by {supplier} in error: {_money(invoice_wrong_account)}",
        f"- Correct balance as per Creditor's Ledger: {_money(correct_balance)}"
    ]
    rs_prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Creditors Reconciliation Statement for {month} {year}.2 after comparing the creditor's ledger with the statement received from {supplier}.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_3, new_prompt_3)

# Fix 4: _make_creditors_reconciliation_statement_and_control_bundle -> cc_prompt
old_prompt_4 = """    cc_prompt = f\"\"\"{business}

#### REQUIRED:
Draw up the Creditors Control account in the General Ledger.

#### INFORMATION:
Use the reconciled creditor balances and the given payments/purchases information.\"\"\""""

new_prompt_4 = """    info_lines_cc = [
        f"- Opening balance brought down: {_money(opening)}",
        f"- Total payments (Bank/EFT) during the month: {_money(payments)}",
        f"- Total credit purchases (Sundry purchases) during the month: {_money(purchases)}",
        f"- Closing balance to be carried down: {_money(closing)}"
    ]
    cc_prompt = f\"\"\"{business}

#### REQUIRED:
Draw up the Creditors Control account in the General Ledger.

#### INFORMATION:
{chr(10).join(info_lines_cc)}\"\"\""""

content = content.replace(old_prompt_4, new_prompt_4)

# Fix 5: _make_creditors_reconciliation_plus_minus -> prompt
old_prompt_5 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Complete the creditors reconciliation effect table to reconcile the Creditor's Ledger balance of {supplier} with the statement received for {month} {year}.2.

#### INFORMATION:
Indicate an increase (+) or decrease (-) for each error/omission and calculate the corrected totals.\"\"\""""

new_prompt_5 = """    info_lines = [
        f"- Creditor's Ledger balance for {supplier}: {_money(ledger_bal)}",
        f"- Statement balance received from {supplier}: {_money(stmt_bal)}",
        "Errors and omissions identified:"
    ]
    for i, (label, le, se) in enumerate(items, start=1):
        # We need to construct a human-readable reason for the effect
        amount = max(abs(le), abs(se))
        if "Discount" in label:
            desc = f"Discount of {_money(amount)} was omitted."
        elif "Invoice amount" in label:
            desc = f"An invoice was recorded incorrectly, causing a difference of {_money(amount)}."
        elif "Invoice omitted" in label:
            desc = f"An invoice for {_money(amount)} was omitted from the statement."
        elif "Payment not yet" in label:
            desc = f"A payment of {_money(amount)} is not yet reflected on the statement."
        else:
            desc = f"{label} for {_money(amount)}."
        info_lines.append(f"  {i}. {desc}")

    prompt = f\"\"\"{business}

#### REQUIRED:
Complete the creditors reconciliation effect table to reconcile the Creditor's Ledger balance of {supplier} with the statement received for {month} {year}.2.

#### INFORMATION:
{chr(10).join(info_lines)}

Indicate an increase (+) or decrease (-) for each error/omission and calculate the corrected totals.\"\"\""""

content = content.replace(old_prompt_5, new_prompt_5)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched reconciliation_generator.py")
