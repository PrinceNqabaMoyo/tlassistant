"""Remediate Batch D: gr12_interest_banking_inflation, gr12_data_handling, gr12_probability (19 subskills)."""
import os
import re

# ==============================================================================
# 1. gr12_interest_banking_inflation
# ==============================================================================

# 1.1 loans_fundamentals_factors.py (subskill 01)
p1 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/loans_fundamentals_factors.py"
with open(p1, "r", encoding="utf-8") as f:
    c1 = f.read()

c1 = c1.replace(
'''    deposit = (dep_pct / 100) * sale_price
    loan_principal = sale_price - deposit

    correct_ans = f"Deposit: {_fmt_curr(deposit)}; Loan Principal: {_fmt_curr(loan_principal)}"''',
'''    deposit = (dep_pct / 100) * sale_price
    loan_principal = sale_price - deposit

    d_spec_01 = {
        "kind": "pie_chart",
        "title": f"Property Financing ({_fmt_curr(sale_price)})",
        "slices": [
            {"name": "Deposit", "value": deposit},
            {"name": "Loan Principal", "value": loan_principal},
        ],
    }

    correct_ans = f"Deposit: {_fmt_curr(deposit)}; Loan Principal: {_fmt_curr(loan_principal)}"'''
)

c1 = c1.replace(
'''    prompt = (
        f"{name} intends to purchase a residential property in an urban suburb with a selling price of {_fmt_curr(sale_price)}. "
        f"The mortgage lender requires a mandatory upfront cash deposit of {dep_pct}% before approving the bond.\\n\\n"
        f"Calculate the deposit required and the resulting net loan amount (principal borrowed) to be financed."
    )''',
'''    prompt = (
        f"Refer to the property financing scheme with a selling price of {_fmt_curr(sale_price)} for {name}.\\n"
        f"The mortgage lender requires a mandatory upfront cash deposit of {dep_pct}% before approving the bond.\\n\\n"
        f"Calculate the deposit required and the resulting net loan amount (principal borrowed) to be financed."
    )'''
)

c1 = c1.replace(
'''        tier_3=f"Subtract the deposit ({_fmt_curr(deposit)}) from {_fmt_curr(sale_price)} to find the net loan: {_fmt_curr(loan_principal)}.",
        r=r,
    )''',
'''        tier_3=f"Subtract the deposit ({_fmt_curr(deposit)}) from {_fmt_curr(sale_price)} to find the net loan: {_fmt_curr(loan_principal)}.",
        r=r,
        diagram_spec=d_spec_01,
    )'''
)

with open(p1, "w", encoding="utf-8") as f:
    f.write(c1)
print("Updated loans_fundamentals_factors.py")


# 1.2 amortization_table_modeling.py (subskill 14)
p2 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/amortization_table_modeling.py"
with open(p2, "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace(
'''def generate_14_non_linear_loan_balance_curve(r: random.Random) -> Dict[str, Any]:
    """Explain why the loan balance curve decreases slowly at first and accelerates toward the end."""
    correct_ans = "Non-linear decay: Early instalments consist mostly of interest, so principal drops slowly; as balance shrinks, interest decreases and principal repayments accelerate"''',
'''def generate_14_non_linear_loan_balance_curve(r: random.Random) -> Dict[str, Any]:
    """Explain why the loan balance curve decreases slowly at first and accelerates toward the end."""
    principal = r.choice([850000, 1000000, 1200000])
    d_spec_14 = {
        "kind": "line_graph",
        "title": f"20-Year Mortgage Balance Curve ({_fmt_curr(principal)})",
        "x_label": "Month",
        "y_label": "Loan Balance (R)",
        "series": [
            {"name": "Closing Balance", "points": [[0, principal], [60, int(principal * 0.92)], [120, int(principal * 0.78)], [180, int(principal * 0.52)], [240, 0]]}
        ],
    }
    correct_ans = "Non-linear decay: Early instalments consist mostly of interest, so principal drops slowly; as balance shrinks, interest decreases and principal repayments accelerate"'''
)

c2 = c2.replace(
'''    prompt = (
        f"A graph tracking the closing balance of a 20-year home loan over 240 months curves downward gradually "
        f"at first, and then drops much more steeply in the final 5 years.\\n\\n"
        f"Explain from an amortization perspective why this loan balance graph is curved rather than a straight line."
    )''',
'''    prompt = (
        f"Refer to the loan balance graph tracking the closing balance of a 20-year mortgage over 240 months.\\n"
        f"Explain from an amortization perspective why this loan balance curve decreases gradually at first and accelerates toward the end."
    )'''
)

c2 = c2.replace(
'''        subskill_id="14_non_linear_loan_balance_curve",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how much of each monthly payment goes to interest versus paying off the actual debt.",
        tier_2="At the start, the debt is huge, so almost all of your monthly repayment pays interest.",
        tier_3="As the debt decreases, interest drops, allowing more capital to be paid off each month.",
        r=r,
    )''',
'''        subskill_id="14_non_linear_loan_balance_curve",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how much of each monthly payment goes to interest versus paying off the actual debt.",
        tier_2="At the start, the debt is huge, so almost all of your monthly repayment pays interest.",
        tier_3="As the debt decreases, interest drops, allowing more capital to be paid off each month.",
        r=r,
        diagram_spec=d_spec_14,
    )'''
)

with open(p2, "w", encoding="utf-8") as f:
    f.write(c2)
print("Updated amortization_table_modeling.py")


# 1.3 loan_optimization_deposits_rates.py (subskills 21, 24)
p3 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/loan_optimization_deposits_rates.py"
with open(p3, "r", encoding="utf-8") as f:
    c3 = f.read()

# Subskill 21
c3 = c3.replace(
'''def generate_21_interest_saved_extra_payment(r: random.Random) -> Dict[str, Any]:
    """Calculate the exact total saving when a loan is settled early due to extra payments."""
    orig_total_cost = 1884225.60
    new_months = 180  # 15 years instead of 20
    new_pmt = 8850.94  # regular + extra
    new_total_cost = new_pmt * new_months
    total_saved = orig_total_cost - new_total_cost''',
'''def generate_21_interest_saved_extra_payment(r: random.Random) -> Dict[str, Any]:
    """Calculate the exact total saving when a loan is settled early due to extra payments."""
    orig_total_cost = r.choice([1884225.60, 2150000.00, 2400000.00])
    new_months = 180  # 15 years instead of 20
    new_pmt = r.choice([8850.94, 9500.00, 10200.00])
    new_total_cost = new_pmt * new_months
    total_saved = orig_total_cost - new_total_cost

    d_spec_21 = {
        "kind": "bar_graph",
        "title": "Mortgage Total Outlay Comparison",
        "categories": ["Standard (20 yr)", "With Extra Payments (15 yr)"],
        "series": [
            {"name": "Total Cost", "values": [orig_total_cost, new_total_cost]}
        ],
    }'''
)

c3 = c3.replace(
'''    prompt = (
        f"A 20-year bond would normally cost {_fmt_curr(orig_total_cost)} over 240 months.\\n"
        f"By paying an extra R 1 000,00 each month (total repayment {_fmt_curr(new_pmt)}), the bond is settled "
        f"in full after only {new_months} months (15 years).\\n\\n"
        f"Calculate the net total interest saving achieved over the life of the loan."
    )''',
'''    prompt = (
        f"Refer to the mortgage comparison chart showing total repayments over time.\\n"
        f"A 20-year bond would normally cost {_fmt_curr(orig_total_cost)} over 240 months.\\n"
        f"By paying an extra R 1 000,00 each month (total repayment {_fmt_curr(new_pmt)}), the bond is settled "
        f"in full after only {new_months} months (15 years).\\n\\n"
        f"Calculate the net total interest saving achieved over the life of the loan."
    )'''
)

c3 = c3.replace(
'''        subskill_id="21_interest_saved_extra_payment",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the new total outlay: 180 months × new repayment, then subtract from the original total.",
        tier_2=f"Calculate {new_months} × {_fmt_curr(new_pmt)}.",
        tier_3=f"Subtract {_fmt_curr(new_total_cost)} from {_fmt_curr(orig_total_cost)} to get {_fmt_curr(total_saved)}.",
        r=r,
    )''',
'''        subskill_id="21_interest_saved_extra_payment",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the new total outlay: 180 months × new repayment, then subtract from the original total.",
        tier_2=f"Calculate {new_months} × {_fmt_curr(new_pmt)}.",
        tier_3=f"Subtract {_fmt_curr(new_total_cost)} from {_fmt_curr(orig_total_cost)} to get {_fmt_curr(total_saved)}.",
        r=r,
        diagram_spec=d_spec_21,
    )'''
)

# Subskill 24
c3 = c3.replace(
'''    settlement_quote = outstanding_bal + early_interest

    correct_ans = _fmt_curr(settlement_quote)''',
'''    settlement_quote = outstanding_bal + early_interest

    d_spec_24 = {
        "kind": "bar_graph",
        "title": f"Early Settlement Quotation ({_fmt_curr(settlement_quote)})",
        "categories": ["Outstanding Principal", "90-Day Penalty Interest"],
        "series": [
            {"name": "Amount", "values": [outstanding_bal, early_interest]}
        ],
    }

    correct_ans = _fmt_curr(settlement_quote)'''
)

c3 = c3.replace(
'''    prompt = (
        f"A borrower sells their house and requests an early settlement quotation for their bond.\\n"
        f"• Outstanding balance: {_fmt_curr(outstanding_bal)}\\n"
        f"• Interest rate: {_fmt_pct(annual_rate)} p.a.\\n"
        f"Under the National Credit Act (NCA), the bank charges a 90-day penalty interest fee for early cancellation without prior notice.\\n\\n"
        f"Calculate the total early settlement figure (Outstanding balance + 90 days interest based on a 365-day year)."
    )''',
'''    prompt = (
        f"Refer to the early settlement quotation summary.\\n"
        f"A borrower sells their house and requests a settlement figure for their bond:\\n"
        f"• Outstanding balance: {_fmt_curr(outstanding_bal)}\\n"
        f"• Interest rate: {_fmt_pct(annual_rate)} p.a.\\n"
        f"Under the National Credit Act (NCA), the bank charges a 90-day penalty interest fee for early cancellation.\\n\\n"
        f"Calculate the total early settlement figure (Outstanding balance + 90 days interest based on a 365-day year)."
    )'''
)

c3 = c3.replace(
'''        subskill_id="24_early_settlement_quotations",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the 90-day interest penalty by applying the annual rate to the balance for 90/365 of a year, then add it to the balance.",
        tier_2=f"Calculate 90-day interest: {_fmt_curr(outstanding_bal)} × {annual_rate}% × (90 ÷ 365) = {_fmt_curr(early_interest)}.",
        tier_3=f"Add {_fmt_curr(outstanding_bal)} + {_fmt_curr(early_interest)} = {_fmt_curr(settlement_quote)}.",
        r=r,
    )''',
'''        subskill_id="24_early_settlement_quotations",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the 90-day interest penalty by applying the annual rate to the balance for 90/365 of a year, then add it to the balance.",
        tier_2=f"Calculate 90-day interest: {_fmt_curr(outstanding_bal)} × {annual_rate}% × (90 ÷ 365) = {_fmt_curr(early_interest)}.",
        tier_3=f"Add {_fmt_curr(outstanding_bal)} + {_fmt_curr(early_interest)} = {_fmt_curr(settlement_quote)}.",
        r=r,
        diagram_spec=d_spec_24,
    )'''
)

with open(p3, "w", encoding="utf-8") as f:
    f.write(c3)
print("Updated loan_optimization_deposits_rates.py")


# 1.4 vehicle_finance_balloon.py (subskill 25)
p4 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/vehicle_finance_balloon.py"
with open(p4, "r", encoding="utf-8") as f:
    c4 = f.read()

c4 = c4.replace(
'''    net_financed = cash_price - trade_in - deposit + initiation_fee

    correct_ans = _fmt_curr(net_financed)''',
'''    net_financed = cash_price - trade_in - deposit + initiation_fee

    d_spec_25 = {
        "kind": "bar_graph",
        "title": f"Vehicle Financing Structure ({_fmt_curr(cash_price)})",
        "categories": ["Cash Price", "Trade-in", "Deposit", "Net Financed"],
        "series": [
            {"name": "Amount", "values": [cash_price, trade_in, deposit, net_financed]}
        ],
    }

    correct_ans = _fmt_curr(net_financed)'''
)

c4 = c4.replace(
'''    prompt = (
        f"A motorist purchases a new car with a sticker cash price of {_fmt_curr(cash_price)}.\\n"
        f"• The dealer allows a trade-in value of {_fmt_curr(trade_in)} for their old car.\\n"
        f"• The buyer pays a cash deposit of {_fmt_curr(deposit)}.\\n"
        f"• A mandatory bank initiation fee of {_fmt_curr(initiation_fee)} is capitalized onto the loan.\\n\\n"
        f"Calculate the net principal amount that must be financed by the vehicle finance bank."
    )''',
'''    prompt = (
        f"Refer to the vehicle financing structure with a vehicle sticker cash price of {_fmt_curr(cash_price)}.\\n"
        f"• The dealer allows a trade-in value of {_fmt_curr(trade_in)} for their old car.\\n"
        f"• The buyer pays a cash deposit of {_fmt_curr(deposit)}.\\n"
        f"• A mandatory bank initiation fee of {_fmt_curr(initiation_fee)} is capitalized onto the loan.\\n\\n"
        f"Calculate the net principal amount that must be financed by the vehicle finance bank."
    )'''
)

c4 = c4.replace(
'''        subskill_id="25_vehicle_net_financed_amount",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract trade-in and deposit from cash price, then add the capitalized initiation fee.",
        tier_2=f"Calculate: {_fmt_curr(cash_price)} - {_fmt_curr(trade_in)} - {_fmt_curr(deposit)} + {_fmt_curr(initiation_fee)}.",
        tier_3=f"Net principal financed is {correct_ans}.",
        r=r,
    )''',
'''        subskill_id="25_vehicle_net_financed_amount",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract trade-in and deposit from cash price, then add the capitalized initiation fee.",
        tier_2=f"Calculate: {_fmt_curr(cash_price)} - {_fmt_curr(trade_in)} - {_fmt_curr(deposit)} + {_fmt_curr(initiation_fee)}.",
        tier_3=f"Net principal financed is {correct_ans}.",
        r=r,
        diagram_spec=d_spec_25,
    )'''
)

with open(p4, "w", encoding="utf-8") as f:
    f.write(c4)
print("Updated vehicle_finance_balloon.py")


# 1.5 stokvels_communal_savings.py (subskills 44, 45)
p5 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/stokvels_communal_savings.py"
with open(p5, "r", encoding="utf-8") as f:
    c5 = f.read()

# Subskill 44
c5 = c5.replace(
'''def generate_44_stokvel_bank_fees_and_interest(r: random.Random) -> Dict[str, Any]:
    """Calculate net annual yield on a stokvel bank account deducting monthly maintenance fees."""
    annual_interest_earned = 7450.00
    monthly_account_fee = 85.00
    annual_fees = monthly_account_fee * 12
    net_interest = annual_interest_earned - annual_fees''',
'''def generate_44_stokvel_bank_fees_and_interest(r: random.Random) -> Dict[str, Any]:
    """Calculate net annual yield on a stokvel bank account deducting monthly maintenance fees."""
    annual_interest_earned = r.choice([6800.00, 7450.00, 8200.00, 9100.00])
    monthly_account_fee = r.choice([75.00, 85.00, 95.00])
    annual_fees = monthly_account_fee * 12
    net_interest = annual_interest_earned - annual_fees

    d_spec_44 = {
        "kind": "bar_graph",
        "title": f"Stokvel Account Annual Yield ({_fmt_curr(net_interest)})",
        "categories": ["Gross Interest", "Bank Fees", "Net Yield"],
        "series": [
            {"name": "Amount", "values": [annual_interest_earned, annual_fees, net_interest]}
        ],
    }'''
)

c5 = c5.replace(
'''    prompt = (
        f"A stokvel deposits its accumulated savings of R 120 000 into a dedicated commercial club bank account.\\n"
        f"• Gross interest earned over the year: {_fmt_curr(annual_interest_earned)}\\n"
        f"• Monthly account maintenance fee: {_fmt_curr(monthly_account_fee)}\\n\\n"
        f"Calculate the net interest earned by the stokvel after bank account fees are deducted for the year."
    )''',
'''    prompt = (
        f"Refer to the stokvel savings account statement for accumulated savings of R 120 000.\\n"
        f"• Gross interest earned over the year: {_fmt_curr(annual_interest_earned)}\\n"
        f"• Monthly account maintenance fee: {_fmt_curr(monthly_account_fee)}\\n\\n"
        f"Calculate the net interest earned by the stokvel after bank account fees are deducted for the year."
    )'''
)

c5 = c5.replace(
'''        subskill_id="44_stokvel_bank_fees_and_interest",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total annual bank fees (monthly fee × 12) and subtract from gross interest.",
        tier_2=f"Annual fees = 12 × {_fmt_curr(monthly_account_fee)} = {_fmt_curr(annual_fees)}.",
        tier_3=f"Net interest = {_fmt_curr(annual_interest_earned)} - {_fmt_curr(annual_fees)} = {_fmt_curr(net_interest)}.",
        r=r,
    )''',
'''        subskill_id="44_stokvel_bank_fees_and_interest",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total annual bank fees (monthly fee × 12) and subtract from gross interest.",
        tier_2=f"Annual fees = 12 × {_fmt_curr(monthly_account_fee)} = {_fmt_curr(annual_fees)}.",
        tier_3=f"Net interest = {_fmt_curr(annual_interest_earned)} - {_fmt_curr(annual_fees)} = {_fmt_curr(net_interest)}.",
        r=r,
        diagram_spec=d_spec_44,
    )'''
)

# Subskill 45
c5 = c5.replace(
'''def generate_45_burial_society_premium_claims(r: random.Random) -> Dict[str, Any]:
    """Calculate the reserve balance of a communal burial society after claims and admin expenses."""
    members = 60
    premium = 150.00
    annual_premiums = members * premium * 12
    claims_paid = 2 * 25000.00  # two bereavement claims of R25 000
    admin_costs = 6000.00
    net_reserve = annual_premiums - claims_paid - admin_costs''',
'''def generate_45_burial_society_premium_claims(r: random.Random) -> Dict[str, Any]:
    """Calculate the reserve balance of a communal burial society after claims and admin expenses."""
    members = r.choice([50, 60, 70, 80])
    premium = r.choice([120.00, 150.00, 200.00])
    annual_premiums = members * premium * 12
    claims_paid = 2 * 25000.00  # two bereavement claims of R25 000
    admin_costs = 6000.00
    net_reserve = annual_premiums - claims_paid - admin_costs

    d_spec_45 = {
        "kind": "bar_graph",
        "title": f"Burial Society Financial Overview ({_fmt_curr(annual_premiums)})",
        "categories": ["Premiums Collected", "Claims Paid", "Admin Costs", "Net Reserve"],
        "series": [
            {"name": "Amount", "values": [annual_premiums, claims_paid, admin_costs, net_reserve]}
        ],
    }'''
)

c5 = c5.replace(
'''    prompt = (
        f"A registered burial society stokvel has {members} active members paying a monthly premium of {_fmt_curr(premium)}.\\n"
        f"During the year:\\n"
        f"• The society paid out 2 funeral bereavement claims of R 25 000,00 each.\\n"
        f"• Administrative catering and transport expenses totaled {_fmt_curr(admin_costs)}.\\n\\n"
        f"Calculate the total annual premium revenue collected and the remaining net reserve funds added to the society's account."
    )''',
'''    prompt = (
        f"Refer to the annual financial summary of a registered burial society stokvel with {members} active members paying a monthly premium of {_fmt_curr(premium)}.\\n"
        f"During the year:\\n"
        f"• The society paid out 2 funeral bereavement claims of R 25 000,00 each.\\n"
        f"• Administrative catering and transport expenses totaled {_fmt_curr(admin_costs)}.\\n\\n"
        f"Calculate the total annual premium revenue collected and the remaining net reserve funds added to the society's account."
    )'''
)

c5 = c5.replace(
'''        subskill_id="45_burial_society_premium_claims",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total premiums (members × monthly premium × 12), then subtract funeral claims and admin expenses.",
        tier_2=f"Annual premiums = {members} × {_fmt_curr(premium)} × 12 = {_fmt_curr(annual_premiums)}.",
        tier_3=f"Net reserve = {_fmt_curr(annual_premiums)} - {_fmt_curr(claims_paid)} - {_fmt_curr(admin_costs)} = {_fmt_curr(net_reserve)}.",
        r=r,
    )''',
'''        subskill_id="45_burial_society_premium_claims",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total premiums (members × monthly premium × 12), then subtract funeral claims and admin expenses.",
        tier_2=f"Annual premiums = {members} × {_fmt_curr(premium)} × 12 = {_fmt_curr(annual_premiums)}.",
        tier_3=f"Net reserve = {_fmt_curr(annual_premiums)} - {_fmt_curr(claims_paid)} - {_fmt_curr(admin_costs)} = {_fmt_curr(net_reserve)}.",
        r=r,
        diagram_spec=d_spec_45,
    )'''
)

with open(p5, "w", encoding="utf-8") as f:
    f.write(c5)
print("Updated stokvels_communal_savings.py")


# 1.6 inflation_purchasing_power.py (subskill 49)
p6 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/inflation_purchasing_power.py"
with open(p6, "r", encoding="utf-8") as f:
    c6 = f.read()

c6 = c6.replace(
'''def generate_49_disinflation_vs_deflation(r: random.Random) -> Dict[str, Any]:
    """Explain that a decreasing positive inflation rate (disinflation) still means prices are rising."""
    correct_ans = "Disinflation: Prices are still increasing, but at a slower pace; prices only decrease if inflation is negative (deflation)"''',
'''def generate_49_disinflation_vs_deflation(r: random.Random) -> Dict[str, Any]:
    """Explain that a decreasing positive inflation rate (disinflation) still means prices are rising."""
    rate_2022 = r.choice([7.8, 8.2, 8.5, 8.9])
    rate_2023 = r.choice([4.8, 5.2, 5.5, 5.8])
    d_spec_49 = {
        "kind": "line_graph",
        "title": "National CPI Inflation Rate (Stats SA)",
        "x_label": "Year",
        "y_label": "CPI Inflation Rate (%)",
        "series": [
            {"name": "CPI Inflation", "points": [[2022, rate_2022], [2023, rate_2023]]}
        ],
    }
    correct_ans = "Disinflation: Prices are still increasing, but at a slower pace; prices only decrease if inflation is negative (deflation)"'''
)

c6 = c6.replace(
'''    prompt = (
        f"A learner looks at an inflation graph published by Statistics South Africa showing the national CPI inflation "
        f"rate dropping steadily from 8,5% in 2022 to 5,2% in 2023.\\n"
        f"The learner concludes: 'Because the graph is decreasing, food and fuel became cheaper in 2023.'\\n\\n"
        f"Critique this learner's statement from a Mathematical Literacy perspective."
    )''',
'''    prompt = (
        f"Refer to the CPI inflation graph showing the national headline inflation rate dropping from {_fmt(rate_2022, 1)}% in 2022 to {_fmt(rate_2023, 1)}% in 2023.\\n"
        f"A learner concludes: 'Because the graph is decreasing, food and fuel became cheaper in 2023.'\\n\\n"
        f"Critique this learner's statement from a Mathematical Literacy perspective."
    )'''
)

c6 = c6.replace(
'''        subskill_id="49_disinflation_vs_deflation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Disinflation means the rate of price increases is slowing down, but prices are still rising.",
        tier_2="As long as inflation is positive (like 5,2%), prices are going up compared to last year.",
        tier_3="Prices only drop during deflation (negative inflation below 0%).",
        r=r,
    )''',
'''        subskill_id="49_disinflation_vs_deflation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Disinflation means the rate of price increases is slowing down, but prices are still rising.",
        tier_2=f"As long as inflation is positive (like {_fmt(rate_2023, 1)}%), prices are going up compared to last year.",
        tier_3="Prices only drop during deflation (negative inflation below 0%).",
        r=r,
        diagram_spec=d_spec_49,
    )'''
)

with open(p6, "w", encoding="utf-8") as f:
    f.write(c6)
print("Updated inflation_purchasing_power.py")


# ==============================================================================
# 2. gr12_data_handling
# ==============================================================================

# 2.1 quartiles_percentiles_spread.py (subskill 31)
q_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/quartiles_percentiles_spread.py"
with open(q_path, "r", encoding="utf-8") as f:
    cq = f.read()

cq = cq.replace(
'''def generate_31_reading_growth_charts_percentiles(r: random.Random) -> Dict[str, Any]:
    """Read child stature-for-age percentiles and interpret health status."""
    age_yrs = r.choice([8, 9, 10, 11])
    height_cm = r.choice([122, 126, 134, 138])
    correct_ans = "Between the 10th and 25th percentiles (classified as shorter than average, but within normal clinical limits)"''',
'''def generate_31_reading_growth_charts_percentiles(r: random.Random) -> Dict[str, Any]:
    """Read child stature-for-age percentiles and interpret health status."""
    age_yrs = r.choice([8, 9, 10, 11])
    height_cm = r.choice([122, 126, 134, 138])
    d_spec_31 = {
        "kind": "line_graph",
        "title": f"Road to Health Growth Chart (Age {age_yrs})",
        "x_label": "Age (years)",
        "y_label": "Height (cm)",
        "series": [
            {"name": "10th Percentile", "points": [[age_yrs, height_cm - 2]]},
            {"name": "Child Height", "points": [[age_yrs, height_cm]]},
            {"name": "25th Percentile", "points": [[age_yrs, height_cm + 4]]},
        ],
    }
    correct_ans = "Between the 10th and 25th percentiles (classified as shorter than average, but within normal clinical limits)"'''
)

cq = cq.replace(
'''    prompt = (
        f"A clinic nurse plots a {age_yrs}-year-old girl's height of {height_cm} cm on the Road to Health stature-for-age chart.\\n"
        f"On the growth chart for {age_yrs}-year-old girls, the 10th percentile curve is at {height_cm - 2} cm and the "
        f"25th percentile curve is at {height_cm + 4} cm.\\n\\n"
        f"Interpret the girl's growth percentile and health classification."
    )''',
'''    prompt = (
        f"Refer to the Road to Health growth chart for a {age_yrs}-year-old girl with height {height_cm} cm.\\n"
        f"The 10th percentile curve is at {height_cm - 2} cm and the 25th percentile curve is at {height_cm + 4} cm.\\n\\n"
        f"Interpret the girl's growth percentile and health classification."
    )'''
)

cq = cq.replace(
'''        subskill_id="31_reading_growth_charts_percentiles",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at where the child's height lies relative to the percentile curves.",
        tier_2=f"{height_cm} cm is greater than {height_cm - 2} cm (10th percentile) and less than {height_cm + 4} cm (25th percentile).",
        tier_3="The height is between the 10th and 25th percentiles (normal clinical variation).",
        r=r,
    )''',
'''        subskill_id="31_reading_growth_charts_percentiles",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at where the child's height lies relative to the percentile curves.",
        tier_2=f"{height_cm} cm is greater than {height_cm - 2} cm (10th percentile) and less than {height_cm + 4} cm (25th percentile).",
        tier_3="The height is between the 10th and 25th percentiles (normal clinical variation).",
        r=r,
        diagram_spec=d_spec_31,
    )'''
)

with open(q_path, "w", encoding="utf-8") as f:
    f.write(cq)
print("Updated quartiles_percentiles_spread.py")


# 2.2 scatter_plots_correlation.py (subskills 41, 44)
s_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/scatter_plots_correlation.py"
with open(s_path, "r", encoding="utf-8") as f:
    cs = f.read()

# Subskill 41
cs = cs.replace(
'''def generate_41_interpreting_bivariate_points(r: random.Random) -> Dict[str, Any]:
    """Interpret coordinates (x, y) on a scatter plot in a real South African context."""
    hours = r.choice([12, 15, 18, 20])
    mark = r.choice([68, 72, 75, 80])''',
'''def generate_41_interpreting_bivariate_points(r: random.Random) -> Dict[str, Any]:
    """Interpret coordinates (x, y) on a scatter plot in a real South African context."""
    hours = r.choice([12, 15, 18, 20])
    mark = r.choice([68, 72, 75, 80])

    d_spec_41 = {
        "kind": "scatter_plot",
        "title": "Study Hours vs Final Mark (%)",
        "x_label": "Weekly Study Hours",
        "y_label": "Final Mark (%)",
        "points": [[hours, mark], [hours - 4, mark - 10], [hours + 3, min(100, mark + 8)]],
    }'''
)

cs = cs.replace(
'''    prompt = (
        f"A scatter plot plots weekly study hours on the horizontal x-axis and final Mathematical Literacy marks (%) "
        f"on the vertical y-axis.\\n"
        f"One specific point plotted on the graph has coordinates ({hours}; {mark}).\\n\\n"
        f"Interpret what this point represents in the context of the study."
    )''',
'''    prompt = (
        f"Refer to the scatter plot relating weekly study hours to final examination marks (%).\\n"
        f"One specific point plotted on the graph has coordinates ({hours}; {mark}).\\n\\n"
        f"Interpret what this point represents in the context of the study."
    )'''
)

cs = cs.replace(
'''        subskill_id="41_interpreting_bivariate_points",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The first coordinate is x (horizontal axis: study hours); the second is y (vertical axis: exam mark).",
        tier_2=f"x = {hours} hours, y = {mark}%.",
        tier_3=f"A learner who dedicated {hours} hours of study scored {mark}%.",
        r=r,
    )''',
'''        subskill_id="41_interpreting_bivariate_points",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The first coordinate is x (horizontal axis: study hours); the second is y (vertical axis: exam mark).",
        tier_2=f"x = {hours} hours, y = {mark}%.",
        tier_3=f"A learner who dedicated {hours} hours of study scored {mark}%.",
        r=r,
        diagram_spec=d_spec_41,
    )'''
)

# Subskill 44
cs = cs.replace(
'''def generate_44_estimating_from_line_of_best_fit(r: random.Random) -> Dict[str, Any]:
    """Estimate a value using a drawn line of best fit (trend line)."""
    slope = r.choice([2.5, 3.0, 3.5])
    intercept = r.choice([20, 25, 30])
    x_hours = r.choice([10, 12, 14, 16])
    expected_y = int(round(slope * x_hours + intercept))''',
'''def generate_44_estimating_from_line_of_best_fit(r: random.Random) -> Dict[str, Any]:
    """Estimate a value using a drawn line of best fit (trend line)."""
    slope = r.choice([2.5, 3.0, 3.5])
    intercept = r.choice([20, 25, 30])
    x_hours = r.choice([10, 12, 14, 16])
    expected_y = int(round(slope * x_hours + intercept))

    d_spec_44 = {
        "kind": "scatter_plot",
        "title": "Revision Hours vs Exam Mark Trend Line",
        "x_label": "Revision Hours",
        "y_label": "Mark (%)",
        "points": [
            [x_hours, expected_y],
            [x_hours - 4, int(slope * (x_hours - 4) + intercept)],
            [x_hours + 4, int(slope * (x_hours + 4) + intercept)],
        ],
    }'''
)

cs = cs.replace(
'''    prompt = (
        f"A line of best fit on a scatter plot has the equation:\\n"
        f"Mark (%) = ({_fmt(slope, 1)} × Revision Hours) + {intercept}%\\n\\n"
        f"Using this trend line, estimate the examination mark for a learner who completed {x_hours} revision hours."
    )''',
'''    prompt = (
        f"Refer to the scatter plot trend line with the equation:\\n"
        f"Mark (%) = ({_fmt(slope, 1)} × Revision Hours) + {intercept}%\\n\\n"
        f"Using this trend line, estimate the examination mark for a learner who completed {x_hours} revision hours."
    )'''
)

cs = cs.replace(
'''        subskill_id="44_estimating_from_line_of_best_fit",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Substitute the number of hours into the trend line formula.",
        tier_2=f"Calculate: ({_fmt(slope, 1)} × {x_hours}) + {intercept}%.",
        tier_3=f"Estimated mark = {expected_y}%.",
        r=r,
    )''',
'''        subskill_id="44_estimating_from_line_of_best_fit",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Substitute the number of hours into the trend line formula.",
        tier_2=f"Calculate: ({_fmt(slope, 1)} × {x_hours}) + {intercept}%.",
        tier_3=f"Estimated mark = {expected_y}%.",
        r=r,
        diagram_spec=d_spec_44,
    )'''
)

with open(s_path, "w", encoding="utf-8") as f:
    f.write(cs)
print("Updated scatter_plots_correlation.py")


# 2.3 opposing_arguments_misleading_stats.py (subskills 48, 49)
m_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/opposing_arguments_misleading_stats.py"
with open(m_path, "r", encoding="utf-8") as f:
    cm = f.read()

# Subskill 48
cm = cm.replace(
'''def generate_48_misleading_graphs_truncated_axis(r: random.Random) -> Dict[str, Any]:
    """Explain how omitting zero on the vertical axis visually exaggerates minor differences."""
    val_a = r.choice([95, 96, 97])
    val_b = r.choice([98, 99, 100])
    y_start = 90''',
'''def generate_48_misleading_graphs_truncated_axis(r: random.Random) -> Dict[str, Any]:
    """Explain how omitting zero on the vertical axis visually exaggerates minor differences."""
    val_a = r.choice([95, 96, 97])
    val_b = r.choice([98, 99, 100])
    y_start = 90

    d_spec_48 = {
        "kind": "bar_graph",
        "title": f"Customer Satisfaction Comparison (Axis baseline {y_start}%)",
        "categories": ["Brand A", "Brand B"],
        "series": [
            {"name": "Satisfaction", "values": [val_a, val_b]}
        ],
        "y_min": y_start,
    }'''
)

cm = cm.replace(
'''    prompt = (
        f"A commercial brand advertises customer satisfaction: Brand A = {val_a}%, Brand B = {val_b}%.\\n"
        f"In their promotional bar graph, the vertical axis begins at {y_start}% rather than 0%.\\n"
        f"As a result, Brand B's bar appears three times taller than Brand A's bar.\\n\\n"
        f"Explain why this graph is statistically misleading."
    )''',
'''    prompt = (
        f"Refer to the promotional bar graph comparing customer satisfaction: Brand A = {val_a}%, Brand B = {val_b}%.\\n"
        f"The vertical axis begins at {y_start}% rather than 0%, making Brand B's bar appear three times taller than Brand A's bar.\\n\\n"
        f"Explain why this graph is statistically misleading."
    )'''
)

cm = cm.replace(
'''        subskill_id="48_misleading_graphs_truncated_axis",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the vertical axis does not start at 0.",
        tier_2=f"Starting the axis at {y_start}% instead of 0 chops off the bottom of the bars, exaggerating the visual gap.",
        tier_3="Omitting zero distorts visual proportion, making a small difference look massive.",
        r=r,
    )''',
'''        subskill_id="48_misleading_graphs_truncated_axis",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the vertical axis does not start at 0.",
        tier_2=f"Starting the axis at {y_start}% instead of 0 chops off the bottom of the bars, exaggerating the visual gap.",
        tier_3="Omitting zero distorts visual proportion, making a small difference look massive.",
        r=r,
        diagram_spec=d_spec_48,
    )'''
)

# Subskill 49
cm = cm.replace(
'''def generate_49_misleading_graphs_inconsistent_intervals(r: random.Random) -> Dict[str, Any]:
    """Identify distortion caused by non-uniform or inconsistent scale intervals."""
    correct_ans = "Non-uniform intervals: The axis jumps from 10 to 20, then abruptly to 50 and 100, visually flattening or exaggerating trends"''',
'''def generate_49_misleading_graphs_inconsistent_intervals(r: random.Random) -> Dict[str, Any]:
    """Identify distortion caused by non-uniform or inconsistent scale intervals."""
    d_spec_49 = {
        "kind": "line_graph",
        "title": "Municipal Water Consumption (Non-uniform intervals)",
        "x_label": "Year",
        "y_label": "Consumption (ML)",
        "series": [
            {"name": "Consumption", "points": [[2018, 120], [2019, 115], [2020, 110], [2024, 90]]}
        ],
    }
    correct_ans = "Non-uniform intervals: The axis jumps from 10 to 20, then abruptly to 50 and 100, visually flattening or exaggerating trends"'''
)

cm = cm.replace(
'''    prompt = (
        f"A municipal graph tracking annual water consumption plots years along the horizontal axis with spacing:\\n"
        f"2018 (1 cm gap) 2019 (1 cm gap) 2020 (1 cm gap) 2024.\\n"
        f"Notice that the four-year gap from 2020 to 2024 is drawn with the exact same 1 cm spacing as a single-year gap.\\n\\n"
        f"Explain why this graph provides a distorted representation of water consumption trends."
    )''',
'''    prompt = (
        f"Refer to the municipal graph tracking annual water consumption across years: 2018, 2019, 2020, and 2024.\\n"
        f"Notice that the four-year gap from 2020 to 2024 is drawn with the exact same spacing as a single-year gap.\\n\\n"
        f"Explain why this graph provides a distorted representation of water consumption trends."
    )'''
)

cm = cm.replace(
'''        subskill_id="49_misleading_graphs_inconsistent_intervals",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check if equal distances on the axis represent equal increments of time.",
        tier_2="A 4-year jump (2020 to 2024) should be 4 times wider than a 1-year jump.",
        tier_3="Inconsistent axis intervals distort the slope and mislead the reader about the rate of change.",
        r=r,
    )''',
'''        subskill_id="49_misleading_graphs_inconsistent_intervals",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check if equal distances on the axis represent equal increments of time.",
        tier_2="A 4-year jump (2020 to 2024) should be 4 times wider than a 1-year jump.",
        tier_3="Inconsistent axis intervals distort the slope and mislead the reader about the rate of change.",
        r=r,
        diagram_spec=d_spec_49,
    )'''
)

with open(m_path, "w", encoding="utf-8") as f:
    f.write(cm)
print("Updated opposing_arguments_misleading_stats.py")


# ==============================================================================
# 3. gr12_probability
# ==============================================================================

# 3.1 scale_frequency_complements.py (subskill 08)
pr1 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/scale_frequency_complements.py"
with open(pr1, "r", encoding="utf-8") as f:
    cp1 = f.read()

cp1 = cp1.replace(
'''def generate_08_probability_scale_endpoints(r: random.Random) -> Dict[str, Any]:
    """Identify impossible vs certain events on the probability continuum."""
    correct_ans = "Probability = 0 means impossible; Probability = 1 (or 100%) means certain; all probabilities must lie between 0 and 1 inclusive"''',
'''def generate_08_probability_scale_endpoints(r: random.Random) -> Dict[str, Any]:
    """Identify impossible vs certain events on the probability continuum."""
    d_spec_08 = {
        "kind": "bar_graph",
        "title": "Probability Continuum (0 to 1)",
        "categories": ["Impossible", "Unlikely", "Even Chance", "Likely", "Certain"],
        "series": [
            {"name": "Probability", "values": [0.0, 0.25, 0.5, 0.75, 1.0]}
        ],
    }
    correct_ans = "Probability = 0 means impossible; Probability = 1 (or 100%) means certain; all probabilities must lie between 0 and 1 inclusive"'''
)

cp1 = cp1.replace(
'''    prompt = (
        f"Consider the formal mathematical probability scale used in Mathematical Literacy.\\n\\n"
        f"State the meaning of the endpoints (0 and 1) on the probability continuum and specify the allowable numerical range for any probability value."
    )''',
'''    prompt = (
        f"Refer to the probability continuum scale shown in the diagram.\\n"
        f"State the meaning of the endpoints (0 and 1) on the probability continuum and specify the allowable numerical range for any probability value."
    )'''
)

cp1 = cp1.replace(
'''        subskill_id="08_probability_scale_endpoints",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What happens at probability = 0? What about probability = 1?",
        tier_2="0 means 0% chance (impossible); 1 means 100% chance (certain).",
        tier_3="All valid probabilities must lie in the closed interval [0; 1].",
        r=r,
    )''',
'''        subskill_id="08_probability_scale_endpoints",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What happens at probability = 0? What about probability = 1?",
        tier_2="0 means 0% chance (impossible); 1 means 100% chance (certain).",
        tier_3="All valid probabilities must lie in the closed interval [0; 1].",
        r=r,
        diagram_spec=d_spec_08,
    )'''
)

with open(pr1, "w", encoding="utf-8") as f:
    f.write(cp1)
print("Updated scale_frequency_complements.py")


# 3.2 independent_dependent_events.py (subskill 11)
pr2 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/independent_dependent_events.py"
with open(pr2, "r", encoding="utf-8") as f:
    cp2 = f.read()

cp2 = cp2.replace(
'''def generate_11_two_stage_draw_with_replacement(r: random.Random) -> Dict[str, Any]:
    """Calculate P(A and B) when sampling with replacement: P(A) x P(B)."""
    yellow = 3
    black = 4
    total = yellow + black  # 7
    # P(Yellow first and Black second)
    p_num = yellow * black  # 12
    p_den = total * total  # 49
    frac_str = _fmt_frac(p_num, p_den)

    correct_ans = f"P(Yellow and Black) = 3/7 × 4/7 = {frac_str}"''',
'''def generate_11_two_stage_draw_with_replacement(r: random.Random) -> Dict[str, Any]:
    """Calculate P(A and B) when sampling with replacement: P(A) x P(B)."""
    yellow = r.choice([2, 3, 4])
    black = r.choice([3, 4, 5])
    total = yellow + black
    p_num = yellow * black
    p_den = total * total
    frac_str = _fmt_frac(p_num, p_den)

    d_spec_11 = {
        "kind": "tree_diagram",
        "title": f"Two-Stage Draw with Replacement ({yellow} Yellow, {black} Black)",
        "stages": [
            {"name": "First Draw", "outcomes": [{"name": "Yellow", "prob": f"{yellow}/{total}"}, {"name": "Black", "prob": f"{black}/{total}"}]},
            {"name": "Second Draw", "outcomes": [{"name": "Yellow", "prob": f"{yellow}/{total}"}, {"name": "Black", "prob": f"{black}/{total}"}]},
        ],
    }

    correct_ans = f"P(Yellow and Black) = {yellow}/{total} × {black}/{total} = {frac_str}"'''
)

cp2 = cp2.replace(
'''    prompt = (
        f"A bag contains 3 yellow beads and 4 black beads (total 7 beads).\\n"
        f"A bead is drawn at random, its colour is recorded, and it is replaced back into the bag.\\n"
        f"A second bead is then drawn and recorded.\\n\\n"
        f"Calculate the probability of drawing a yellow bead first AND a black bead second."
    )''',
'''    prompt = (
        f"Refer to the tree diagram for drawing beads from a bag with replacement.\\n"
        f"A bag contains {yellow} yellow beads and {black} black beads (total {total} beads).\\n"
        f"A bead is drawn at random, its colour is recorded, and it is replaced back into the bag.\\n"
        f"A second bead is then drawn and recorded.\\n\\n"
        f"Calculate the probability of drawing a yellow bead first AND a black bead second."
    )'''
)

cp2 = cp2.replace(
'''        subskill_id="11_two_stage_draw_with_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="With replacement means the total number of beads stays 7 for both draws.",
        tier_2="P(Yellow) = 3/7. P(Black) = 4/7. Multiply them together.",
        tier_3=f"P(Yellow and Black) = 3/7 × 4/7 = {frac_str}.",
        r=r,
    )''',
'''        subskill_id="11_two_stage_draw_with_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="With replacement means the total number of beads stays the same for both draws.",
        tier_2=f"P(Yellow) = {yellow}/{total}. P(Black) = {black}/{total}. Multiply them together.",
        tier_3=f"P(Yellow and Black) = {yellow}/{total} × {black}/{total} = {frac_str}.",
        r=r,
        diagram_spec=d_spec_11,
    )'''
)

with open(pr2, "w", encoding="utf-8") as f:
    f.write(cp2)
print("Updated independent_dependent_events.py")


# 3.3 contingency_tables.py (subskill 22)
pr3 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/contingency_tables.py"
with open(pr3, "r", encoding="utf-8") as f:
    cp3 = f.read()

cp3 = cp3.replace(
'''def generate_22_driver_demographics_accident_risk(r: random.Random) -> Dict[str, Any]:
    """Calculate and compare accident risk probabilities across age brackets from insurance data."""
    young_accidents = 42
    young_total = 200
    older_accidents = 18
    older_total = 300''',
'''def generate_22_driver_demographics_accident_risk(r: random.Random) -> Dict[str, Any]:
    """Calculate and compare accident risk probabilities across age brackets from insurance data."""
    young_accidents = r.choice([36, 40, 42, 48])
    young_total = 200
    older_accidents = r.choice([15, 18, 21, 24])
    older_total = 300

    d_spec_22 = {
        "kind": "contingency_table",
        "title": "Driver Insurance Claims by Age Bracket",
        "rows": ["< 25 yrs", ">= 25 yrs"],
        "columns": ["Accident Claim", "No Claim", "Total"],
        "matrix": [
            [young_accidents, young_total - young_accidents, young_total],
            [older_accidents, older_total - older_accidents, older_total],
        ],
    }'''
)

cp3 = cp3.replace(
'''    prompt = (
        f"A South African motor vehicle insurance firm analyzes accident claims over one year:\\n"
        f"• Drivers under 25 years old: {young_accidents} claims out of {young_total} insured drivers\\n"
        f"• Drivers 25 years and older: {older_accidents} claims out of {older_total} insured drivers\\n\\n"
        f"Calculate the claim probability percentage for both demographic groups and explain why insurers charge higher premiums to drivers under 25."
    )''',
'''    prompt = (
        f"Refer to the driver insurance claims contingency table.\\n"
        f"• Drivers under 25 years old: {young_accidents} claims out of {young_total} insured drivers\\n"
        f"• Drivers 25 years and older: {older_accidents} claims out of {older_total} insured drivers\\n\\n"
        f"Calculate the claim probability percentage for both demographic groups and explain why insurers charge higher premiums to drivers under 25."
    )'''
)

cp3 = cp3.replace(
'''        subskill_id="22_driver_demographics_accident_risk",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate claims ÷ total drivers × 100 for each age category.",
        tier_2=f"Young: {young_accidents}/200 = {_fmt_pct(p_young, 1)}. Older: {older_accidents}/300 = {_fmt_pct(p_older, 1)}.",
        tier_3="Young drivers have a significantly higher claim rate, justifying higher risk premiums.",
        r=r,
    )''',
'''        subskill_id="22_driver_demographics_accident_risk",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate claims ÷ total drivers × 100 for each age category.",
        tier_2=f"Young: {young_accidents}/200 = {_fmt_pct(p_young, 1)}. Older: {older_accidents}/300 = {_fmt_pct(p_older, 1)}.",
        tier_3="Young drivers have a significantly higher claim rate, justifying higher risk premiums.",
        r=r,
        diagram_spec=d_spec_22,
    )'''
)

with open(pr3, "w", encoding="utf-8") as f:
    f.write(cp3)
print("Updated contingency_tables.py")


# 3.4 tree_diagrams_multistage.py (subskills 25, 29, 32)
pr4 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/tree_diagrams_multistage.py"
with open(pr4, "r", encoding="utf-8") as f:
    cp4 = f.read()

# Subskill 25
cp4 = cp4.replace(
'''def generate_25_tree_branch_probabilities(r: random.Random) -> Dict[str, Any]:
    """Verify that branch probabilities emanating from any node sum to exactly 1,0."""
    p1 = 0.70
    p2 = 0.30''',
'''def generate_25_tree_branch_probabilities(r: random.Random) -> Dict[str, Any]:
    """Verify that branch probabilities emanating from any node sum to exactly 1,0."""
    p1 = r.choice([0.60, 0.65, 0.70, 0.75])
    p2 = round(1.0 - p1, 2)
    d_spec_25 = {
        "kind": "tree_diagram",
        "title": f"Branch Probabilities ({_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00)",
        "stages": [
            {"name": "Stage 1", "outcomes": [{"name": "Branch A", "prob": f"{_fmt(p1, 2)}"}, {"name": "Branch B", "prob": f"{_fmt(p2, 2)}"}]}
        ],
    }'''
)

cp4 = cp4.replace(
'''    prompt = (
        f"In a tree diagram modeling a two-stage decision process, the first stage splits into two mutually exclusive "
        f"branches with probabilities {_fmt(p1, 2)} (70%) and {_fmt(p2, 2)} (30%).\\n\\n"
        f"State the mathematical rule that governs the sum of branch probabilities originating from any single node."
    )''',
'''    prompt = (
        f"Refer to the tree diagram for a two-stage decision process.\\n"
        f"The first stage splits into two mutually exclusive branches with probabilities {_fmt(p1, 2)} and {_fmt(p2, 2)}.\\n\\n"
        f"State the mathematical rule that governs the sum of branch probabilities originating from any single node."
    )'''
)

cp4 = cp4.replace(
'''        subskill_id="25_tree_branch_probabilities",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about what happens if you add together all possible outcomes branching from one point.",
        tier_2=f"{_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00.",
        tier_3="The sum of probabilities branching from any single node must always equal 1 (or 100%).",
        r=r,
    )''',
'''        subskill_id="25_tree_branch_probabilities",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about what happens if you add together all possible outcomes branching from one point.",
        tier_2=f"{_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00.",
        tier_3="The sum of probabilities branching from any single node must always equal 1 (or 100%).",
        r=r,
        diagram_spec=d_spec_25,
    )'''
)

# Subskill 29
cp4 = cp4.replace(
'''def generate_29_medical_screening_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of a false positive in a medical diagnostic tree diagram."""
    prev = 0.01
    healthy = 0.99
    sens = 0.95
    spec = 0.95
    false_pos = 0.05
    # P(Healthy AND Positive) = healthy * false_pos = 0.99 * 0.05 = 0.0495
    p_healthy_pos = healthy * false_pos
    p_pct = p_healthy_pos * 100.0''',
'''def generate_29_medical_screening_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of a false positive in a medical diagnostic tree diagram."""
    prev = r.choice([0.01, 0.02, 0.03])
    healthy = round(1.0 - prev, 2)
    sens = 0.95
    spec = 0.95
    false_pos = 0.05
    p_healthy_pos = healthy * false_pos
    p_pct = p_healthy_pos * 100.0

    d_spec_29 = {
        "kind": "tree_diagram",
        "title": "Medical Screening Tree Diagram",
        "stages": [
            {"name": "Health Status", "outcomes": [{"name": "Diseased", "prob": f"{prev}"}, {"name": "Healthy", "prob": f"{healthy}"}]},
            {"name": "Test Result", "outcomes": [{"name": "Test Pos", "prob": f"{false_pos}"}, {"name": "Test Neg", "prob": f"{round(1.0 - false_pos, 2)}"}]},
        ],
    }'''
)

cp4 = cp4.replace(
'''    prompt = (
        f"A medical rapid test for a rare disease is evaluated on a population where 1% have the disease (prevalence = 0,01).\n"
        f"• For a healthy person, the test has a 5% false positive rate (P(Positive | Healthy) = 0,05)\n\n"
        f"Using a tree diagram path, calculate the probability that a randomly chosen patient is Healthy BUT tests Positive."
    )''',
'''    prompt = (
        f"Refer to the medical screening tree diagram where prevalence is {_fmt(prev, 2)}.\\n"
        f"For a healthy person, the test has a 5% false positive rate (P(Positive | Healthy) = 0,05).\\n\\n"
        f"Using the tree diagram path, calculate the probability that a randomly chosen patient is Healthy BUT tests Positive."
    )'''
)

cp4 = cp4.replace(
'''        subskill_id="29_medical_screening_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Follow the path: Patient is Healthy (0,99) -> Test is Positive (0,05). Multiply along the branch.",
        tier_2="Calculation: 0,99 × 0,05 = 0,0495.",
        tier_3="P(Healthy and Positive) = 0,0495 (or 4,95%).",
        r=r,
    )''',
'''        subskill_id="29_medical_screening_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Follow the path: Patient is Healthy -> Test is Positive. Multiply along the branch.",
        tier_2=f"Calculation: {healthy} × 0,05 = {p_healthy_pos:.4f}.",
        tier_3=f"P(Healthy and Positive) = {p_healthy_pos:.4f} (or {_fmt(p_pct, 2)}%).",
        r=r,
        diagram_spec=d_spec_29,
    )'''
)

# Subskill 32
cp4 = cp4.replace(
'''def generate_32_successive_draw_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Trace a tree diagram path without replacement for two successive draws."""
    # 5 blue, 3 red = 8 total
    # Draw blue then red: (5/8) * (3/7) = 15/56
    correct_ans = f"P(Blue then Red) = 5/8 × 3/7 = 15/56"''',
'''def generate_32_successive_draw_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Trace a tree diagram path without replacement for two successive draws."""
    blue = r.choice([4, 5, 6])
    red = r.choice([3, 4])
    total = blue + red
    p_num = blue * red
    p_den = total * (total - 1)
    frac_str = _fmt_frac(p_num, p_den)

    d_spec_32 = {
        "kind": "tree_diagram",
        "title": f"Successive Draws Without Replacement ({blue} Blue, {red} Red)",
        "stages": [
            {"name": "First Draw", "outcomes": [{"name": "Blue", "prob": f"{blue}/{total}"}, {"name": "Red", "prob": f"{red}/{total}"}]},
            {"name": "Second Draw", "outcomes": [{"name": "Red", "prob": f"{red}/{total - 1}"}]},
        ],
    }
    correct_ans = f"P(Blue then Red) = {blue}/{total} × {red}/{total - 1} = {frac_str}"'''
)

cp4 = cp4.replace(
'''    prompt = (
        f"A bag contains 5 blue pens and 3 red pens (total 8 pens).\\n"
        f"Two pens are drawn one after the other without replacement.\\n\\n"
        f"Using tree diagram branching principles, state the branch probabilities and calculate P(Blue first and Red second)."
    )''',
'''    prompt = (
        f"Refer to the tree diagram for drawing pens without replacement.\\n"
        f"A bag contains {blue} blue pens and {red} red pens (total {total} pens).\\n"
        f"Two pens are drawn one after the other without replacement.\\n\\n"
        f"Using tree diagram branching principles, state the branch probabilities and calculate P(Blue first and Red second)."
    )'''
)

cp4 = cp4.replace(
'''        subskill_id="32_successive_draw_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First draw has 8 pens; second draw has only 7 pens (no replacement).",
        tier_2="P(Blue first) = 5/8. P(Red second | Blue first) = 3/7. Multiply: 5/8 × 3/7.",
        tier_3="P(Blue then Red) = 15/56.",
        r=r,
    )''',
'''        subskill_id="32_successive_draw_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"First draw has {total} pens; second draw has only {total - 1} pens (no replacement).",
        tier_2=f"P(Blue first) = {blue}/{total}. P(Red second | Blue first) = {red}/{total - 1}. Multiply them.",
        tier_3=f"P(Blue then Red) = {blue}/{total} × {red}/{total - 1} = {frac_str}.",
        r=r,
        diagram_spec=d_spec_32,
    )'''
)

with open(pr4, "w", encoding="utf-8") as f:
    f.write(cp4)
print("Updated tree_diagrams_multistage.py")
