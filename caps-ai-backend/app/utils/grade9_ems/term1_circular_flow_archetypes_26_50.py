"""Grade 9 EMS Term 1: The Circular Flow — Semantic Archetypes 26 to 50."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term1_circular_flow_archetypes_01_25 import (
    fmt_dec,
    fmt_zar,
    make_question,
    svg_three_sector_flow,
)


def _build_26_circular_flow_participant_matching(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("A supermarket remits VAT collected at tills to SARS.", "Businesses -> Government (Money flow: indirect tax)"),
        ("A mechanic works 45 hours per week at a Johannesburg workshop.", "Households -> Businesses via Factor Market (Real flow: labour)"),
        ("Provincial health officials deliver free childhood vaccines at a clinic.", "Government -> Households (Real flow: public service)"),
        ("Parents purchase uniforms and stationery at a local store.", "Households -> Businesses via Goods Market (Money flow: spending)"),
    ]
    clue, ans = rng.choice(cases)
    distractors = [
        x[1] for x in cases if x[1] != ans
    ]
    prompt = f"Which circular-flow linkage accurately represents the transaction below?\n*{clue}*"
    sol = f"- **Correct Linkage:** {ans}."
    return make_question(
        rng=rng,
        subskill="26_circular_flow_participant_matching",
        question_type="mcq",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Match transaction to participants, market and flow type", "marks": 2, "type": "A"}],
        marking_guide="2 marks for correct origin, destination and flow classification.",
        hints={
            "tier_1": "Identify who initiates the item or payment and who receives it.",
            "tier_2": "Determine whether it is a physical service/input (Real) or Rand (Money).",
            "tier_3": ans,
        },
        misconception_tags=["misidentifies_vat_remittance_as_household_to_business"],
        options=[ans] + distractors,
        duration_mins=2,
    )


def _build_27_household_tax_and_disposable_income(rng: random.Random, mode: str) -> Dict[str, Any]:
    gross = rng.choice([28000, 32000, 36000, 40000, 44000])
    tax_pct = rng.choice([15, 18, 20, 22])
    tax_amt = gross * tax_pct / 100.0
    disp = gross - tax_amt
    prompt = (
        f"A nurse receives a monthly gross salary of {fmt_zar(gross)} from a hospital and pays {tax_pct}% in direct PAYE income tax.\n\n"
        f"(a) Calculate the monthly direct tax paid to government.\n"
        f"(b) Calculate the nurse's **disposable income** available for spending in the goods & services market."
    )
    ans = f"PAYE tax = {fmt_zar(tax_amt)}; Disposable income = {fmt_zar(disp)}"
    sol = (
        f"**(a) Direct Tax (PAYE):** ${fmt_zar(gross)} \\times {tax_pct}\\% = {fmt_zar(tax_amt)}$\n"
        f"**(b) Disposable Income:** ${fmt_zar(gross)} - {fmt_zar(tax_amt)} = {fmt_zar(disp)}$"
    )
    return make_question(
        rng=rng,
        subskill="27_household_tax_and_disposable_income",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate PAYE {fmt_zar(tax_amt)}", "marks": 2, "type": "A"},
            {"step": f"Calculate disposable income {fmt_zar(disp)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for tax; 2 marks for subtracting tax from gross income.",
        hints={
            "tier_1": "Multiply gross income by the PAYE percentage.",
            "tier_2": "Disposable income = Gross income minus Direct tax.",
            "tier_3": ans,
        },
        misconception_tags=["adds_tax_to_gross_salary_to_get_disposable_income"],
    )


def _build_28_business_revenue_tax_and_factor_payout(rng: random.Random, mode: str) -> Dict[str, Any]:
    rev = rng.choice([650000, 720000, 840000, 920000])
    wages = rng.choice([280000, 310000, 340000])
    rent_int = rng.choice([90000, 110000, 125000])
    corp_tax = rng.choice([65000, 78000, 85000])
    owner_profit = rev - (wages + rent_int + corp_tax)
    prompt = (
        f"A manufacturing firm receives {fmt_zar(rev)} in annual goods-market revenue. It pays {fmt_zar(wages)} in wages, "
        f"{fmt_zar(rent_int)} in rent & interest, and {fmt_zar(corp_tax)} in corporate income tax.\n\n"
        f"(a) Calculate the entrepreneur's remaining **profit**.\n"
        f"(b) Calculate the total **factor income** distributed back to households (`wages + rent/interest + profit`)."
    )
    tot_factor = wages + rent_int + owner_profit
    ans = f"Profit = {fmt_zar(owner_profit)}; Total factor payout to households = {fmt_zar(tot_factor)}"
    sol = (
        f"**(a) Net Profit:** ${fmt_zar(rev)} - ({fmt_zar(wages)} + {fmt_zar(rent_int)} + {fmt_zar(corp_tax)}) = {fmt_zar(owner_profit)}$\n"
        f"**(b) Total Factor Payments to Households:** ${fmt_zar(wages)} + {fmt_zar(rent_int)} + {fmt_zar(owner_profit)} = {fmt_zar(tot_factor)}$ (leaving {fmt_zar(corp_tax)} flowing to Government)."
    )
    return make_question(
        rng=rng,
        subskill="28_business_revenue_tax_and_factor_payout",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate profit {fmt_zar(owner_profit)}", "marks": 2, "type": "A"},
            {"step": f"Sum household factor payout {fmt_zar(tot_factor)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for profit subtraction; 2 marks for factor payout sum.",
        hints={
            "tier_1": "Subtract all wages, rent/interest and tax from total revenue to find profit.",
            "tier_2": "Remember corporate tax goes to Government, while wages, rent, interest and profit go to Households.",
            "tier_3": ans,
        },
        misconception_tags=["includes_corporate_tax_as_household_factor_income"],
    )


def _build_29_government_budget_tax_vs_spending(rng: random.Random, mode: str) -> Dict[str, Any]:
    direct = rng.choice([760, 820, 890, 940])
    indirect = rng.choice([540, 580, 610, 650])
    salaries_svcs = rng.choice([880, 920, 960, 1020])
    grants_tenders = rng.choice([460, 510, 550, 600])
    tot_tax = direct + indirect
    tot_spend = salaries_svcs + grants_tenders
    diff = tot_tax - tot_spend
    stance = "budget surplus" if diff >= 0 else "budget deficit"
    prompt = (
        f"In a fiscal year, national government collects R{direct} billion in direct taxes and R{indirect} billion in indirect taxes. "
        f"It spends R{salaries_svcs} billion on public salaries/services and R{grants_tenders} billion on social grants & tenders.\n\n"
        f"(a) Calculate total tax revenue and total government spending.\n"
        f"(b) Determine the fiscal balance and classify it as a **budget surplus** or **budget deficit**."
    )
    ans = f"Tax = R{tot_tax}bn; Spending = R{tot_spend}bn; {stance.capitalize()} of R{abs(diff)}bn"
    sol = (
        f"**(a) Totals:**\n"
        f"- Tax revenue $= \\text{{R}}{direct} + \\text{{R}}{indirect} = \\text{{R}}{tot_tax}\\text{{ billion}}$\n"
        f"- Government spending $= \\text{{R}}{salaries_svcs} + \\text{{R}}{grants_tenders} = \\text{{R}}{tot_spend}\\text{{ billion}}$\n\n"
        f"**(b) Fiscal Balance:** $\\text{{R}}{tot_tax} - \\text{{R}}{tot_spend} = {'+' if diff >= 0 else '-'}R{abs(diff)}\\text{{ billion}}$ (**{stance}**)."
    )
    return make_question(
        rng=rng,
        subskill="29_government_budget_tax_vs_spending",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate tax R{tot_tax}bn and spending R{tot_spend}bn", "marks": 2, "type": "A"},
            {"step": f"Find difference R{abs(diff)}bn and label {stance}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for sums; 2 marks for difference and surplus/deficit label.",
        hints={
            "tier_1": "Add direct + indirect tax for revenue; add salaries/services + grants/tenders for spending.",
            "tier_2": "If spending exceeds tax revenue, there is a budget deficit.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_budget_surplus_with_budget_deficit"],
    )


def _build_30_interdependence_households_firms_state(rng: random.Random, mode: str) -> Dict[str, Any]:
    links = [
        ("Businesses cannot produce goods without household labour and entrepreneurship, nor grow without public roads and electricity", "Households, Businesses and Government depend continuously on each other's resources, spending and services"),
        ("Households depend on businesses for groceries and jobs, and on government for schools, clinics and safety", "each participant relies on the real and money flows provided by the other two"),
        ("Government cannot fund clinics or grants without PAYE and VAT collected from working households and profitable firms", "tax revenue depends directly on active household employment and business turnover"),
        ("If households stop spending in the goods market, business profits drop and tax collections shrink", "disrupting one link weakens flows across every participant in the circular flow"),
    ]
    obs, conclusion = rng.choice(links)
    prompt = (
        f"Evaluate why *{obs}.*\n\n"
        f"Explain the principle of **economic interdependence** in the circular flow using one concrete linkage between Government and Businesses."
    )
    ans = f"Interdependence means {conclusion}; e.g., government builds roads/electricity supporting businesses, and firms pay company tax/VAT funding government"
    sol = (
        f"- **Interdependence:** {conclusion.capitalize()}.\n"
        f"- **Government $\\leftrightarrow$ Business Link:** Government provides legal courts, roads and ports enabling businesses to operate, while businesses pay company tax and collect VAT that finance public infrastructure."
    )
    return make_question(
        rng=rng,
        subskill="30_interdependence_households_firms_state",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain mutual interdependence across participants", "marks": 2, "type": "A"},
            {"step": "Give concrete two-way Government-Business linkage", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for general interdependence; 2 marks for clear Government-Business two-way flow.",
        hints={
            "tier_1": "Notice that no single participant can survive in isolation.",
            "tier_2": "Trace both what Government supplies to firms and what firms pay back to Government.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_businesses_are_independent_of_public_infrastructure"],
    )


def _build_31_unemployment_shock_circular_flow_ripple(rng: random.Random, mode: str) -> Dict[str, Any]:
    workers_lost = rng.choice([120, 150, 200, 250])
    avg_wage = rng.choice([8000, 9500, 11000, 12500])
    lost_wages = workers_lost * avg_wage
    prompt = (
        f"Suppose a regional canning factory closes, causing {workers_lost} workers earning an average of {fmt_zar(avg_wage)}/month to lose their jobs.\n\n"
        f"(a) Calculate the total monthly **money flow** lost from the factor market.\n"
        f"(b) Trace two knock-on effects on local businesses in the **goods market** and on **government tax revenue**."
    )
    ans = f"Lost factor wages = {fmt_zar(lost_wages)}/month; Goods market: lower retail sales/profits; Government: lower PAYE and VAT receipts plus higher grant claims"
    sol = (
        f"**(a) Immediate Factor Income Loss:** ${workers_lost} \\times {fmt_zar(avg_wage)} = {fmt_zar(lost_wages)}$ per month.\n"
        f"**(b) Ripple Effects:**\n"
        f"1. **Goods & Services Market:** Unemployed households cut grocery and retail spending, shrinking local shops' turnover.\n"
        f"2. **Government Finances:** Direct PAYE and indirect VAT collections fall while demand for social support increases."
    )
    return make_question(
        rng=rng,
        subskill="31_unemployment_shock_circular_flow_ripple",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate lost monthly wages {fmt_zar(lost_wages)}", "marks": 2, "type": "A"},
            {"step": "Explain fall in goods-market spending + fall in tax receipts", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for lost payroll calculation; 2 marks for goods-market and fiscal knock-on effects.",
        hints={
            "tier_1": "Multiply displaced workers by monthly average wage.",
            "tier_2": "Trace lower household income -> lower retail purchases -> lower VAT and PAYE taxes.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_factory_closure_affects_only_workers_and_not_shops_or_state"],
    )


def _build_32_tax_increase_shock_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    income = rng.choice([20000, 25000, 30000, 35000])
    old_r, new_r = rng.choice([(16, 20), (18, 22), (15, 19), (20, 24)])
    old_disp = income * (1 - old_r / 100.0)
    new_disp = income * (1 - new_r / 100.0)
    drop = old_disp - new_disp
    prompt = (
        f"If government increases a household's effective direct income tax rate from {old_r}% to {new_r}% on a monthly salary of {fmt_zar(income)}:\n\n"
        f"(a) Calculate the monthly reduction in disposable household spending power.\n"
        f"(b) Explain how this higher tax rate reduces flows through the **goods and services market**."
    )
    ans = f"Spending power drops by {fmt_zar(drop)} (from {fmt_zar(old_disp)} to {fmt_zar(new_disp)}); households buy fewer goods, lowering business revenue"
    sol = (
        f"**(a) Disposable Income Change:**\n"
        f"- Before: ${fmt_zar(income)} \\times (1 - 0.{old_r}) = {fmt_zar(old_disp)}$\n"
        f"- After: ${fmt_zar(income)} \\times (1 - 0.{new_r}) = {fmt_zar(new_disp)}$\n"
        f"- Drop $= {fmt_zar(drop)}$ per month.\n\n"
        f"**(b) Circular Flow Impact:** Higher direct taxes act as a leakage from household disposable income, reducing consumer expenditure flowing to businesses unless government immediately spends it back."
    )
    return make_question(
        rng=rng,
        subskill="32_tax_increase_shock_analysis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate disposable income drop {fmt_zar(drop)}", "marks": 2, "type": "A"},
            {"step": "Explain reduced consumer spending flowing to businesses", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for calculation; 2 marks for circular flow consumption effect.",
        hints={
            "tier_1": "Find the percentage-point tax increase applied to monthly income.",
            "tier_2": "Higher direct taxes leave less disposable cash for households to spend at shops.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_higher_tax_leaves_household_spending_unchanged"],
    )


def _build_33_public_tender_multiplier_effect(rng: random.Random, mode: str) -> Dict[str, Any]:
    tender = rng.choice([2000000, 2500000, 3000000, 4000000])
    wage_share = rng.choice([30, 35, 40])
    spend_share = rng.choice([70, 75, 80])
    wages = round(tender * wage_share / 100.0)
    retail_spend = round(wages * spend_share / 100.0)
    prompt = (
        f"Government awards a {fmt_zar(tender)} public school renovation tender to a construction firm. "
        f"The firm pays {wage_share}% as construction wages to local households, and those workers spend {spend_share}% of their wages at local shops.\n\n"
        f"(a) Calculate the wage flow entering the factor market.\n"
        f"(b) Calculate the resulting consumer expenditure flowing into local shops in the goods market."
    )
    ans = f"Wages = {fmt_zar(wages)}; Local shop spending = {fmt_zar(retail_spend)}"
    sol = (
        f"**(a) Stage 1 — Factor Market Wages (Firm $\\rightarrow$ Households):**\n"
        f"${fmt_zar(tender)} \\times {wage_share}\\% = {fmt_zar(wages)}$\n\n"
        f"**(b) Stage 2 — Goods Market Spending (Households $\\rightarrow$ Local Shops):**\n"
        f"${fmt_zar(wages)} \\times {spend_share}\\% = {fmt_zar(retail_spend)}$"
    )
    return make_question(
        rng=rng,
        subskill="33_public_tender_multiplier_effect",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate wage flow {fmt_zar(wages)}", "marks": 2, "type": "A"},
            {"step": f"Calculate local retail spending {fmt_zar(retail_spend)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for Stage 1 wages; 2 marks for Stage 2 retail spending.",
        hints={
            "tier_1": "Compute wages first from the tender sum.",
            "tier_2": f"Multiply those wages by {spend_share}% for Stage 2 spending.",
            "tier_3": ans,
        },
        misconception_tags=["takes_spend_share_of_total_tender_instead_of_wages"],
    )


def _build_34_grant_increase_retail_circulation(rng: random.Random, mode: str) -> Dict[str, Any]:
    grant_boost = rng.choice([450000, 600000, 750000, 900000])
    vat_fraction = 15 / 115
    implied_vat = round(grant_boost * vat_fraction, 2)
    prompt = (
        f"After government increases monthly social grants by {fmt_zar(grant_boost)} across a district, "
        f"recipients spend the entire increase on standard-rated clothing and household appliances (inclusive of 15% VAT).\n\n"
        f"(a) Calculate how much indirect VAT flows back to government out of that {fmt_zar(grant_boost)} spending (`amount * 15/115`).\n"
        f"(b) Explain why social grants stimulate local businesses in the circular flow."
    )
    ans = f"VAT returned = {fmt_zar(implied_vat)}; grant spending boosts retailer turnover, helping firms keep staff employed"
    sol = (
        f"**(a) Indirect VAT Clawback:**\n"
        f"${fmt_zar(grant_boost)} \\times \\frac{{15}}{{115}} = {fmt_zar(implied_vat)}$\n\n"
        f"**(b) Economic Circulation:** Higher household grant spending immediately becomes business revenue in the goods market, supporting retail jobs and returning tax revenue to the state."
    )
    return make_question(
        rng=rng,
        subskill="34_grant_increase_retail_circulation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate VAT portion {fmt_zar(implied_vat)} using 15/115", "marks": 2, "type": "A"},
            {"step": "Explain business revenue and employment stimulus", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for VAT fraction 15/115; 2 marks for business circulation insight.",
        hints={
            "tier_1": "When a Rand price already includes 15% VAT, extract VAT with 15/115.",
            "tier_2": "Trace money from grants -> households -> shops -> SARS/firms.",
            "tier_3": ans,
        },
        misconception_tags=["uses_15_over_100_on_vat_inclusive_spending"],
    )


def _build_35_leakages_in_real_world_economy(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("households depositing R120 million into fixed savings accounts instead of spending it at shops", "Savings (S) — income not immediately spent on domestic consumption"),
        ("importers wiring R340 million overseas to buy foreign smartphones", "Imports (M) — domestic Rand spending leaving the national circular flow"),
        ("SARS deducting R280 million in personal income tax from worker salaries", "Taxes (T) — income withdrawn from direct private consumption"),
        ("families hoarding R45 million in foreign-bought luxury jewellery and bank deposits", "Savings and Imports reducing immediate domestic retail turnover"),
    ]
    obs, leak = rng.choice(cases)
    distractors = [
        "Injections — foreign tourists buying domestic hotel stays and safari tours",
        "Real flows — workers producing domestic loaves of bread in bakeries",
        "Factor income — local factories distributing monthly wage packets",
    ]
    prompt = f"In an expanded real-world circular flow, *{obs}* represents which type of **leakage**?"
    sol = f"- **Leakage:** {leak}.\n- The three primary leakages from domestic circular spending are **Savings (S), Taxes (T), and Imports (M)**."
    return make_question(
        rng=rng,
        subskill="35_leakages_in_real_world_economy",
        question_type="mcq",
        prompt=prompt,
        correct_answer=leak,
        sample_answer=leak,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify specific circular flow leakage", "marks": 2, "type": "A"}],
        marking_guide="2 marks for identifying Savings, Taxes or Imports as a leakage.",
        hints={
            "tier_1": "Leakages (withdrawals) are S (Savings), T (Taxes), and M (Imports).",
            "tier_2": "Ask whether the money is saved, taxed, or sent abroad.",
            "tier_3": leak,
        },
        misconception_tags=["labels_exports_as_a_leakage"],
        options=[leak] + distractors,
        duration_mins=2,
    )


def _build_36_injections_in_real_world_economy(rng: random.Random, mode: str) -> Dict[str, Any]:
    inv = rng.choice([120, 150, 180, 210])
    gov_s = rng.choice([240, 270, 300, 330])
    exp = rng.choice([190, 220, 250, 280])
    tot_inj = inv + gov_s + exp
    sav = rng.choice([130, 150, 170])
    tax = rng.choice([210, 230, 250])
    imp = rng.choice([160, 180, 200])
    tot_leak = sav + tax + imp
    diff = tot_inj - tot_leak
    direction = "expands" if diff > 0 else ("contracts" if diff < 0 else "remains balanced")
    prompt = (
        f"In an expanded real-world economy, **Injections** (`Investment + Government Spending + Exports`) equal "
        f"R{inv}bn + R{gov_s}bn + R{exp}bn, while **Leakages** (`Savings + Taxes + Imports`) equal "
        f"R{sav}bn + R{tax}bn + R{imp}bn.\n\n"
        f"(a) Calculate total Injections and total Leakages.\n"
        f"(b) State whether the circular flow **expands** or **contracts**, and by how many R billions."
    )
    ans = f"Injections = R{tot_inj}bn; Leakages = R{tot_leak}bn; Economy {direction} (net difference R{abs(diff)}bn)"
    sol = (
        f"**(a) Totals:**\n"
        f"- Injections $= \\text{{R}}{inv} + \\text{{R}}{gov_s} + \\text{{R}}{exp} = \\text{{R}}{tot_inj}\\text{{bn}}$\n"
        f"- Leakages $= \\text{{R}}{sav} + \\text{{R}}{tax} + \\text{{R}}{imp} = \\text{{R}}{tot_leak}\\text{{bn}}$\n\n"
        f"**(b) Net Effect:** Since Injections (`R{tot_inj}bn`) {'>' if diff > 0 else '<' if diff < 0 else '='} Leakages (`R{tot_leak}bn`), the circular flow **{direction}** by **R{abs(diff)}bn**."
    )
    return make_question(
        rng=rng,
        subskill="36_injections_in_real_world_economy",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Sum Injections R{tot_inj}bn and Leakages R{tot_leak}bn", "marks": 2, "type": "A"},
            {"step": f"Conclude {direction} by R{abs(diff)}bn", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for sums; 2 marks for comparing injections vs leakages.",
        hints={
            "tier_1": "Add I + G + X for Injections and S + T + M for Leakages.",
            "tier_2": "When Injections > Leakages, spending power expands.",
            "tier_3": ans,
        },
        misconception_tags=["mixes_imports_into_injections_or_exports_into_leakages"],
    )


def _build_37_closed_vs_open_economy_comparison(rng: random.Random, mode: str) -> Dict[str, Any]:
    rows = [
        ("Foreign sector (exports/imports)", "Excluded (no trade abroad)", "Included (active international trade)"),
        ("Savings & financial institutions", "Ignored (all income spent)", "Included (savings & business loans)"),
        ("South Africa in practice", "Does not apply to SA", "Describes real-world SA economy"),
        ("Core teaching focus", "Basic internal circular links", "Complete real-world macro flows"),
    ]
    picked = rng.sample(rows, 3)
    headers = ["Feature", "Closed Economy Model", "Open Real-World Economy"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Feature | Closed Economy Model | Open Real-World Economy |", "|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        blank_col = rng.choice([1, 2])
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx == blank_col
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Closed model strips out foreign trade and savings; Open model includes them."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="37_closed_vs_open_economy_comparison",
        question_type="table_completion",
        prompt="Complete the comparison matrix distinguishing the textbook Closed Economy Model from an Open Real-World Economy.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Closed vs Open Comparison:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per comparison cell.",
        hints={
            "tier_1": "Ask whether foreign trade and bank savings are permitted.",
            "tier_2": "South Africa trades actively worldwide, making it an open economy.",
            "tier_3": md_table,
        },
        misconception_tags=["labels_south_africa_as_closed_economy"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "feat", "label": headers[0]}, {"key": "closed", "label": headers[1]}, {"key": "open", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_38_distinguishing_factor_vs_goods_market_items(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Hiring a qualified civil engineer", "Factor market", "Businesses", "Households"),
        ("Buying 2L fresh milk and brown bread", "Goods & services market", "Households", "Businesses"),
        ("Leasing arable farmland for maize planting", "Factor market", "Businesses", "Households"),
        ("Booking an airline ticket or haircut", "Goods & services market", "Households", "Businesses"),
        ("Government ordering 5 000 school desks", "Goods & services market", "Government", "Businesses"),
    ]
    picked = rng.sample(bank, 3)
    headers = ["Transaction", "Market", "Buyer", "Seller"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Transaction | Market | Buyer | Seller |", "|---|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2, 3], 2)
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Households sell factors in the factor market; firms sell finished items in the goods market."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="38_distinguishing_factor_vs_goods_market_items",
        question_type="table_completion",
        prompt="Classify each transaction by identifying the active Market, Buyer, and Seller.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Market Transaction Audit:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each correct Market, Buyer or Seller entry.",
        hints={
            "tier_1": "Check whether the item is an input to production or a finished consumer/state product.",
            "tier_2": "Notice that households switch from Sellers (factor market) to Buyers (goods market).",
            "tier_3": md_table,
        },
        misconception_tags=["marks_households_as_buyers_in_factor_market"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower(), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_39_entrepreneurship_profit_vs_labour_wage(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("Lindiwe invests her own savings, designs an app, hires two coders and earns residual surplus after paying all bills", "Nomsa works 40 hours per week coding for a fixed monthly salary", "Lindiwe provides Entrepreneurship (earning profit); Nomsa provides Labour (earning wages/salary)"),
        ("Kabelo rents a stall, buys raw spices, bears business risk and keeps net earnings", "Sipho drives the delivery van for a set hourly rate", "Kabelo supplies Entrepreneurship (earning profit); Sipho supplies Labour (earning wages)"),
        ("Thandiwe organises land, machinery and staff to launch a poultry farm and absorbs profit/loss", "Bongani feeds the flock on shift for guaranteed fortnightly pay", "Thandiwe supplies Entrepreneurship (profit); Bongani supplies Labour (wages)"),
    ]
    ent_act, lab_act, correct = rng.choice(cases)
    prompt = (
        f"Compare two individuals in the factor market:\n"
        f"- Person 1: *{ent_act}.*\n"
        f"- Person 2: *{lab_act}.*\n\n"
        f"Identify the exact **factor of production** and **remuneration** earned by each person, and state who bears financial risk if sales drop."
    )
    ans = f"{correct}; Person 1 (entrepreneur) bears the risk of loss"
    sol = (
        f"- **Classification:** {correct}.\n"
        f"- **Risk Bearing:** Person 1 (entrepreneur) bears financial risk—if costs exceed revenue, profit becomes a loss, whereas Person 2's contractual wages remain payable."
    )
    return make_question(
        rng=rng,
        subskill="39_entrepreneurship_profit_vs_labour_wage",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Identify Entrepreneurship -> Profit", "marks": 1, "type": "A"},
            {"step": "Identify Labour -> Wages/Salary", "marks": 1, "type": "A"},
            {"step": "Explain entrepreneur bears business risk", "marks": 2, "type": "A"},
        ],
        marking_guide="1+1 marks for both factor/payment matches; 2 marks for risk-bearing distinction.",
        hints={
            "tier_1": "Distinguish contractual employee pay from residual risk-bearing ownership.",
            "tier_2": "Entrepreneurs combine land, labour and capital and earn profit.",
            "tier_3": ans,
        },
        misconception_tags=["calls_manager_salary_entrepreneurial_profit"],
    )


def _build_40_natural_resources_and_capital_remuneration(rng: random.Random, mode: str) -> Dict[str, Any]:
    hectares = rng.choice([20, 25, 30, 40])
    rent_per_ha = rng.choice([1200, 1500, 1800])
    loan = rng.choice([200000, 300000, 400000])
    int_rate = rng.choice([9, 10, 12])
    tot_rent = hectares * rent_per_ha
    tot_int = loan * int_rate / 100.0
    prompt = (
        f"A commercial grain business leases {hectares} hectares of farmland at {fmt_zar(rent_per_ha)}/hectare per year "
        f"and borrows {fmt_zar(loan)} at {int_rate}% annual interest to finance irrigation equipment.\n\n"
        f"(a) Calculate the annual **rent** (natural resources) and annual **interest** (capital).\n"
        f"(b) State the total annual payment made for these two factors of production."
    )
    comb = tot_rent + tot_int
    ans = f"Rent = {fmt_zar(tot_rent)}; Interest = {fmt_zar(tot_int)}; Total = {fmt_zar(comb)}"
    sol = (
        f"**(a) Individual Payments:**\n"
        f"- **Rent** (Natural resources) $= {hectares} \\times {fmt_zar(rent_per_ha)} = {fmt_zar(tot_rent)}$\n"
        f"- **Interest** (Capital) $= {fmt_zar(loan)} \\times {int_rate}\\% = {fmt_zar(tot_int)}$\n\n"
        f"**(b) Combined Factor Payout:** ${fmt_zar(tot_rent)} + {fmt_zar(tot_int)} = {fmt_zar(comb)}$"
    )
    return make_question(
        rng=rng,
        subskill="40_natural_resources_and_capital_remuneration",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate rent {fmt_zar(tot_rent)} and interest {fmt_zar(tot_int)}", "marks": 3, "type": "A"},
            {"step": f"Sum total {fmt_zar(comb)}", "marks": 1, "type": "CA"},
        ],
        marking_guide="3 marks for rent & interest calculations; 1 mark for total sum.",
        hints={
            "tier_1": "Multiply farmland hectares by rent/ha; multiply capital loan by interest %.",
            "tier_2": "Add rent and interest together for total payout.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_rent_and_interest_definitions"],
    )


def _build_41_government_infrastructure_enabling_business(rng: random.Random, mode: str) -> Dict[str, Any]:
    infra = [
        ("upgraded provincial tarred highways between farms and ports", "cuts transport delays, vehicle wear and spoilage, expanding business sales"),
        ("reliable electricity substations and municipal water networks", "keeps factory machinery running continuously without costly generator fuel"),
        ("commercial labour courts and police patrols near industrial parks", "protects property rights and enforces contracts so investors expand output"),
        ("fibre internet corridors and public vocational training colleges", "improves worker productivity and digital commerce across firms"),
    ]
    asset, effect = rng.choice(infra)
    prompt = (
        f"Explain how government spending on **{asset}** creates a positive **real flow** to businesses "
        f"and ultimately boosts tax revenue back to the state."
    )
    ans = f"Infrastructure {effect}; higher business output and jobs generate larger company tax, PAYE and VAT inflows"
    sol = (
        f"- **Public Real Flow to Firms:** {asset.capitalize()} {effect}.\n"
        f"- **Circular Tax Feedback:** Higher business sales and expanded hiring raise corporate tax, employee PAYE and consumer VAT flowing back to Government."
    )
    return make_question(
        rng=rng,
        subskill="41_government_infrastructure_enabling_business",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain cost-saving / productivity benefit to firms", "marks": 2, "type": "A"},
            {"step": "Trace feedback into higher corporate/PAYE/VAT taxes", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for business productivity gain; 2 marks for circular tax return.",
        hints={
            "tier_1": "Think of infrastructure as a real flow from Government to Businesses.",
            "tier_2": "Follow the loop from better roads/power -> higher firm output -> higher tax inflows.",
            "tier_3": ans,
        },
        misconception_tags=["views_business_taxes_as_having_zero_public_return_to_firms"],
    )


def _build_42_vat_collection_chain_in_circular_flow(rng: random.Random, mode: str) -> Dict[str, Any]:
    excl = rng.choice([200, 400, 600, 800])
    vat = round(excl * 0.15, 2)
    incl = excl + vat
    prompt = (
        f"A shopper pays {fmt_zar(incl)} (inclusive of 15% VAT) at a clothing retailer for a jacket priced at {fmt_zar(excl)} before VAT.\n\n"
        f"(a) Calculate the exact VAT Rand amount (`{fmt_zar(incl)} - {fmt_zar(excl)}`).\n"
        f"(b) Explain why **two** different money flows leave the retailer out of that {fmt_zar(incl)} sale."
    )
    ans = f"VAT = {fmt_zar(vat)}; {fmt_zar(vat)} indirect tax goes to Government (SARS), while {fmt_zar(excl)} stays as business revenue to pay costs/factors"
    sol = (
        f"**(a) VAT Component:** ${fmt_zar(incl)} - {fmt_zar(excl)} = {fmt_zar(vat)}$\n"
        f"**(b) Split Money Flows:**\n"
        f"1. **Businesses $\\rightarrow$ Government:** {fmt_zar(vat)} is remitted as indirect tax (VAT).\n"
        f"2. **Businesses $\\rightarrow$ Factor/Supplier Market:** {fmt_zar(excl)} remains as sales revenue used to pay wages, rent, suppliers and profit."
    )
    return make_question(
        rng=rng,
        subskill="42_vat_collection_chain_in_circular_flow",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate VAT {fmt_zar(vat)}", "marks": 1, "type": "A"},
            {"step": "Identify Government VAT remittance + Business factor/cost payout", "marks": 3, "type": "A"},
        ],
        marking_guide="1 mark for VAT amount; 3 marks for splitting SARS remittance from firm revenue.",
        hints={
            "tier_1": "Subtract the pre-VAT price from the till total.",
            "tier_2": "Remember the retailer only collects VAT on government's behalf.",
            "tier_3": ans,
        },
        misconception_tags=["treats_entire_till_receipt_as_retailer_income"],
    )


def _build_43_circular_flow_diagram_missing_label_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    hh_tax = rng.choice([310, 340, 370])
    biz_tax = rng.choice([220, 250, 280])
    gov_grants = rng.choice([290, 320, 350])
    gov_tenders = rng.choice([180, 210, 240])
    hh_spend = rng.choice([1200, 1350, 1500])
    slots = [
        ("direct_tax", "Households -> Government", f"Direct & Indirect Taxes (R{hh_tax}bn)", f"Total taxes from Households & Firms = R{hh_tax + biz_tax}bn; Company Tax = R{biz_tax}bn"),
        ("grants", "Government -> Households", f"Social Grants & Public Services (R{gov_grants}bn)", f"Total Government Outlays = R{gov_grants + gov_tenders}bn; Tenders = R{gov_tenders}bn"),
        ("tenders", "Government -> Businesses", f"Tenders, Contracts & Subsidies (R{gov_tenders}bn)", f"Total Government Outlays = R{gov_grants + gov_tenders}bn; Grants = R{gov_grants}bn"),
        ("biz_tax", "Businesses -> Government", f"Corporate / Company Tax (R{biz_tax}bn)", f"Total taxes from Households & Firms = R{hh_tax + biz_tax}bn; Household Tax = R{hh_tax}bn"),
    ]
    slot_key, arrow_dir, expected_lbl, balance_clue = rng.choice(slots)
    diagram = svg_three_sector_flow(hh_tax, biz_tax, gov_grants, gov_tenders, hh_spend, masked_slot=slot_key)
    missing_val = {"direct_tax": hh_tax, "grants": gov_grants, "tenders": gov_tenders, "biz_tax": biz_tax}[slot_key]
    prompt = (
        f"Examine the Three-Sector Circular Flow model where one arrow between **{arrow_dir}** is labelled **`[?]`**.\n"
        f"Given that {balance_clue} (and Consumer Spending = R{hh_spend}bn):\n\n"
        f"(a) Identify the **economic name** of the missing flow **`[?]`**.\n"
        f"(b) Calculate its missing Rand value in R billions."
    )
    ans = f"{expected_lbl}"
    sol = (
        f"**(a) Flow Name:** Between **{arrow_dir}**, the missing money flow is **{expected_lbl.split(' (')[0]}**.\n"
        f"**(b) Value:** Subtracting the known component from the stated total yields **R{missing_val}bn**."
    )
    return make_question(
        rng=rng,
        subskill="43_circular_flow_diagram_missing_label_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Identify flow name between {arrow_dir}", "marks": 2, "type": "A"},
            {"step": f"Calculate R{missing_val}bn", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for naming the arrow flow; 2 marks for calculating the missing Rand billion value.",
        hints={
            "tier_1": f"Check which participant sends money to {arrow_dir.split(' -> ')[1]} in the schematic.",
            "tier_2": "Subtract the visible component on the matching arrow from the total given in the prompt.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_taxes_entering_state_with_grants_leaving_state"],
        diagram_spec=diagram,
    )


def _build_44_municipal_rates_and_local_circular_flow(rng: random.Random, mode: str) -> Dict[str, Any]:
    rates = rng.choice([850, 960, 1120, 1250])
    water_refuse = rng.choice([420, 490, 560, 610])
    num_houses = rng.choice([300, 400, 500])
    per_house = rates + water_refuse
    muni_total = per_house * num_houses
    prompt = (
        f"At local government level, {num_houses} suburban households each pay monthly municipal property rates of {fmt_zar(rates)} "
        f"plus {fmt_zar(water_refuse)} for refuse removal and sanitation.\n\n"
        f"(a) Calculate the total monthly revenue flowing from these households to the municipality.\n"
        f"(b) Name TWO real flows the municipality supplies back to households and local businesses."
    )
    ans = f"Municipal revenue = {fmt_zar(muni_total)}; Real flows: refuse collection, clean water, street lighting, local roads or municipal clinics"
    sol = (
        f"**(a) Municipal Money Inflow:**\n"
        f"- Per household $= {fmt_zar(rates)} + {fmt_zar(water_refuse)} = {fmt_zar(per_house)}$\n"
        f"- Total across {num_houses} homes $= {num_houses} \\times {fmt_zar(per_house)} = {fmt_zar(muni_total)}$\n\n"
        f"**(b) Return Real Flows:** Refuse removal, treated drinking water, street lights, road maintenance and local parks/libraries."
    )
    return make_question(
        rng=rng,
        subskill="44_municipal_rates_and_local_circular_flow",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate municipal inflow {fmt_zar(muni_total)}", "marks": 2, "type": "A"},
            {"step": "Name two municipal real services (1 mark each)", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for total revenue calculation; 2 marks for two municipal real services.",
        hints={
            "tier_1": "Add rates and utility charges per household, then multiply by the number of homes.",
            "tier_2": "Think of visible public services run by municipalities.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_municipal_rates_are_part_of_government_flows"],
    )


def _build_45_informal_sector_participation_in_flow(rng: random.Random, mode: str) -> Dict[str, Any]:
    traders = [
        ("a township spaza shop buying stock from a formal cash-and-carry wholesaler", 4600, 15),
        ("a street fruit hawker buying bulk crates and plastic bags at a fresh-produce market", 2400, 15),
        ("an informal hair salon purchasing shampoos and clippers from a registered distributor", 3200, 15),
        ("a home-based seamstress buying bolts of fabric and thread from a formal textile merchant", 3800, 15),
    ]
    trader, stock_cost, vat_r = rng.choice(traders)
    vat_paid = round(stock_cost * (vat_r / (100 + vat_r)), 2)
    prompt = (
        f"Even though informal enterprises may not register for company tax, consider **{trader}** "
        f"for {fmt_zar(stock_cost)} (inclusive of {vat_r}% VAT).\n\n"
        f"(a) Calculate how much indirect VAT the informal trader still contributes indirectly via formal wholesale purchases (`amount * 15/115`).\n"
        f"(b) Explain TWO ways informal businesses still form part of South Africa's circular flow."
    )
    ans = f"VAT paid on inputs = {fmt_zar(vat_paid)}; sells affordable goods to households in the goods market and buys inputs from formal wholesalers/utilities"
    sol = (
        f"**(a) Embedded VAT Paid:** ${fmt_zar(stock_cost)} \\times \\frac{{15}}{{115}} = {fmt_zar(vat_paid)}$\n"
        f"**(b) Circular Flow Links:**\n"
        f"1. **Goods Market:** Supplies accessible everyday goods and services to local households.\n"
        f"2. **Business & Tax Link:** Purchases stock, transport, airtime and electricity from formal businesses while paying indirect VAT."
    )
    return make_question(
        rng=rng,
        subskill="45_informal_sector_participation_in_flow",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate VAT paid {fmt_zar(vat_paid)}", "marks": 2, "type": "A"},
            {"step": "Explain two links to households/formal wholesalers/taxes", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for 15/115 VAT calculation; 2 marks for two circular-flow connections.",
        hints={
            "tier_1": "Use 15/115 to find the VAT embedded in the wholesale stock bill.",
            "tier_2": "Informal traders still buy from formal suppliers, pay VAT on fuel/stock and earn household income.",
            "tier_3": ans,
        },
        misconception_tags=["claims_informal_sector_operates_completely_outside_circular_flow"],
    )


def _build_46_financial_institutions_intermediary_bridge(rng: random.Random, mode: str) -> Dict[str, Any]:
    savings = rng.choice([400, 500, 650, 800])
    reserve_pct = rng.choice([10, 15, 20])
    loanable = round(savings * (1 - reserve_pct / 100.0), 1)
    prompt = (
        f"In the real-world financial sector, households save R{savings} million in commercial banks (a leakage). "
        f"After holding {reserve_pct}% in reserves, banks lend out the rest to businesses for factory expansion (investment injection).\n\n"
        f"(a) Calculate how many R millions banks channel into business investment loans.\n"
        f"(b) Explain why financial institutions prevent household savings from permanently shrinking the economy."
    )
    ans = f"Investment loans = R{fmt_dec(loanable)} million; banks recycle household savings (leakage) back into business capital spending (injection)"
    sol = (
        f"**(a) Loanable Investment Funds:**\n"
        f"- Reserves $= \\text{{R}}{savings} \\times {reserve_pct}\\% = \\text{{R}}{fmt_dec(savings * reserve_pct / 100.0)}\\text{{m}}$\n"
        f"- Investment loans $= \\text{{R}}{savings} - \\text{{R}}{fmt_dec(savings * reserve_pct / 100.0)} = \\text{{R}}{fmt_dec(loanable)}\\text{{ million}}$\n\n"
        f"**(b) Intermediary Role:** Banks gather dormant household savings and channel them to firms buying machinery and buildings, converting a leakage back into an injection."
    )
    return make_question(
        rng=rng,
        subskill="46_financial_institutions_intermediary_bridge",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate loanable funds R{fmt_dec(loanable)}m", "marks": 2, "type": "A"},
            {"step": "Explain recycling savings leakage into investment injection", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for calculation; 2 marks for financial-intermediation explanation.",
        hints={
            "tier_1": f"Subtract the {reserve_pct}% reserve from total household savings.",
            "tier_2": "Banks link household savers to borrowing businesses.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_bank_savings_vanish_forever_without_being_lent"],
    )


def _build_47_foreign_sector_imports_exports_extension(rng: random.Random, mode: str) -> Dict[str, Any]:
    exports = rng.choice([520, 580, 640, 710])
    imports = rng.choice([480, 530, 610, 690])
    net_x = exports - imports
    prompt = (
        f"Opening the closed circular flow adds the **foreign sector**: domestic mines and farms export goods worth R{exports} billion, "
        f"while local firms and consumers import machinery and fuel worth R{imports} billion.\n\n"
        f"(a) Identify which trade flow is an **injection** and which is a **leakage**.\n"
        f"(b) Calculate net exports (`Exports - Imports`) in R billions."
    )
    ans = f"Injection: Exports (R{exports}bn); Leakage: Imports (R{imports}bn); Net exports = {'+' if net_x >= 0 else '-'}R{abs(net_x)} billion"
    sol = (
        f"**(a) Direction of Money Flows:**\n"
        f"- **Exports (R{exports}bn):** **Injection** — foreign buyers send Rand/foreign currency into domestic businesses.\n"
        f"- **Imports (R{imports}bn):** **Leakage** — domestic spending flows outward to overseas producers.\n\n"
        f"**(b) Net Exports:** $\\text{{R}}{exports}\\text{{bn}} - \\text{{R}}{imports}\\text{{bn}} = {'+' if net_x >= 0 else '-'}R{abs(net_x)}\\text{{ billion}}$."
    )
    return make_question(
        rng=rng,
        subskill="47_foreign_sector_imports_exports_extension",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Classify Exports as injection and Imports as leakage", "marks": 2, "type": "A"},
            {"step": f"Calculate net exports {'+' if net_x >= 0 else '-'}R{abs(net_x)}bn", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for injection/leakage classification; 2 marks for net export arithmetic.",
        hints={
            "tier_1": "Track whether the money enters South Africa (Exports) or leaves South Africa (Imports).",
            "tier_2": "Compute Exports minus Imports.",
            "tier_3": ans,
        },
        misconception_tags=["calls_imports_an_injection_because_goods_enter_country"],
    )


def _build_48_tracing_complete_rand_cycle(rng: random.Random, mode: str) -> Dict[str, Any]:
    salary = rng.choice([20000, 24000, 28000, 32000])
    paye_pct = rng.choice([15, 20])
    after_paye = salary * (1 - paye_pct / 100.0)
    groceries_spent = after_paye * 0.5
    vat_back = round(groceries_spent * (15 / 115), 2)
    prompt = (
        f"Trace a public-sector Rand cycle starting when government pays a teacher a monthly gross salary of {fmt_zar(salary)}:\n"
        f"1. Direct PAYE tax of {paye_pct}% is deducted immediately.\n"
        f"2. The teacher spends 50% of remaining net pay on taxable household goods (15% VAT included) at a local store.\n\n"
        f"Calculate: (a) Net pay after PAYE, (b) Amount spent at the store, and (c) Total tax recovered by government (`PAYE + VAT from the store`)."
    )
    paye_amt = salary - after_paye
    tot_tax_back = round(paye_amt + vat_back, 2)
    ans = f"Net pay = {fmt_zar(after_paye)}; Store spending = {fmt_zar(groceries_spent)}; Total tax back = {fmt_zar(tot_tax_back)}"
    sol = (
        f"**(a) Net Pay after {paye_pct}% PAYE:**\n"
        f"- PAYE $= {fmt_zar(salary)} \\times {paye_pct}\\% = {fmt_zar(paye_amt)}$\n"
        f"- Net pay $= {fmt_zar(salary)} - {fmt_zar(paye_amt)} = {fmt_zar(after_paye)}$\n\n"
        f"**(b) Store Spending:** $50\\% \\times {fmt_zar(after_paye)} = {fmt_zar(groceries_spent)}$\n\n"
        f"**(c) Combined Tax Returned to State:**\n"
        f"- Indirect VAT $= {fmt_zar(groceries_spent)} \\times \\frac{{15}}{{115}} = {fmt_zar(vat_back)}$\n"
        f"- Total tax back $= {fmt_zar(paye_amt)} + {fmt_zar(vat_back)} = {fmt_zar(tot_tax_back)}$"
    )
    return make_question(
        rng=rng,
        subskill="48_tracing_complete_rand_cycle",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate net pay {fmt_zar(after_paye)}", "marks": 2, "type": "A"},
            {"step": f"Calculate store spending {fmt_zar(groceries_spent)}", "marks": 1, "type": "CA"},
            {"step": f"Calculate VAT {fmt_zar(vat_back)} and total tax {fmt_zar(tot_tax_back)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for net pay; 1 mark for store spending; 2 marks for VAT + combined tax.",
        hints={
            "tier_1": "Deduct PAYE first, then take half of net pay for store purchases.",
            "tier_2": "Extract embedded VAT using 15/115 and add it to the original PAYE amount.",
            "tier_3": ans,
        },
        misconception_tags=["applies_50_percent_to_gross_salary_before_paye"],
    )


def _build_49_diagnosing_circular_flow_misconceptions(rng: random.Random, mode: str) -> Dict[str, Any]:
    errors = [
        ("A learner claims: 'When workers go to a factory, both their labour and their monthly wages belong to the Real Flow because workers spend the money on real bread.'", "Labour is a Real Flow (Households -> Businesses), whereas monthly wages are a Money Flow moving in the opposite direction (Businesses -> Households)."),
        ("A learner claims: 'Businesses own all four factors of production originally and rent them from government.'", "Households are the original owners of all four factors of production (natural resources, labour, capital, entrepreneurship) and sell/hire them to businesses and government."),
        ("A learner claims: 'Because retailers physically add VAT onto till slips, VAT is a Direct Tax paid on company profits.'", "VAT is an Indirect Tax levied on consumer spending and remitted via retailers, whereas corporate income tax and PAYE are Direct Taxes."),
        ("A learner claims: 'A closed economy means shops close early and nobody works.'", "A closed economy means an economy with no international trade (no imports or exports with the foreign sector), while domestic production and spending continue."),
    ]
    claim, correction = rng.choice(errors)
    prompt = f"Read the incorrect economics statement below and **rewrite it accurately**:\n*{claim}*"
    sol = f"**Corrected Explanation:**\n- {correction}"
    return make_question(
        rng=rng,
        subskill="49_diagnosing_circular_flow_misconceptions",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=correction,
        sample_answer=correction,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Identify error and supply accurate economic correction", "marks": 3, "type": "A"}],
        marking_guide="3 marks for diagnosing the misconception and providing the exact correct relationship.",
        hints={
            "tier_1": "Spot which definition, owner, or flow classification was mixed up.",
            "tier_2": "Re-state the exact circular flow rule clearly.",
            "tier_3": correction,
        },
        misconception_tags=["repeats_naive_student_misconception_uncorrected"],
    )


def _build_50_circular_flow_policy_scenario_synthesis(rng: random.Random, mode: str) -> Dict[str, Any]:
    tax_cut_bn = rng.choice([24, 30, 36])
    tender_bn = rng.choice([40, 50, 60])
    vat_hike_bn = rng.choice([18, 22, 26])
    net_stimulus = tax_cut_bn + tender_bn - vat_hike_bn
    prompt = (
        f"National Treasury unveils a three-part budget package:\n"
        f"- **Measure 1:** Personal income tax (PAYE) relief leaving households with +R{tax_cut_bn}bn.\n"
        f"- **Measure 2:** New road-construction tenders paying businesses +R{tender_bn}bn.\n"
        f"- **Measure 3:** Higher fuel levies collecting R{vat_hike_bn}bn more in indirect tax.\n\n"
        f"(a) Classify Measures 1, 2, and 3 by **participant flow** and **direct vs indirect tax / expenditure**.\n"
        f"(b) Calculate the **net Rand stimulus** (`Tax relief + Tenders - Fuel levy hike`) injected into private spending."
    )
    ans = f"M1: lower direct tax (Households); M2: govt tender outflow (Businesses); M3: higher indirect tax; Net stimulus = +R{net_stimulus} billion"
    sol = (
        f"**(a) Flow Classification:**\n"
        f"- **Measure 1:** Reduced **direct tax** outflow from **Households $\\rightarrow$ Government**, raising disposable income.\n"
        f"- **Measure 2:** Government **tender spending** flowing from **Government $\\rightarrow$ Businesses** (and onward to household wages).\n"
        f"- **Measure 3:** Higher **indirect tax** outflow collected on fuel purchases.\n\n"
        f"**(b) Net Stimulus:** $+\\text{{R}}{tax_cut_bn}\\text{{bn}} + \\text{{R}}{tender_bn}\\text{{bn}} - \\text{{R}}{vat_hike_bn}\\text{{bn}} = +\\text{{R}}{net_stimulus}\\text{{ billion}}$."
    )
    return make_question(
        rng=rng,
        subskill="50_circular_flow_policy_scenario_synthesis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=6,
        marking_schema=[
            {"step": "Classify all 3 measures accurately (1 mark each)", "marks": 3, "type": "A"},
            {"step": f"Calculate net stimulus +R{net_stimulus}bn", "marks": 3, "type": "A"},
        ],
        marking_guide="3 marks for flow/tax classification of all 3 measures; 3 marks for net stimulus math.",
        hints={
            "tier_1": "Distinguish PAYE (direct), road tenders (public spending), and fuel levy (indirect).",
            "tier_2": f"Compute {tax_cut_bn} + {tender_bn} - {vat_hike_bn}.",
            "tier_3": ans,
        },
        misconception_tags=["adds_fuel_levy_hike_as_household_stimulus"],
        duration_mins=6,
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_circular_flow_participant_matching": _build_26_circular_flow_participant_matching,
    "27_household_tax_and_disposable_income": _build_27_household_tax_and_disposable_income,
    "28_business_revenue_tax_and_factor_payout": _build_28_business_revenue_tax_and_factor_payout,
    "29_government_budget_tax_vs_spending": _build_29_government_budget_tax_vs_spending,
    "30_interdependence_households_firms_state": _build_30_interdependence_households_firms_state,
    "31_unemployment_shock_circular_flow_ripple": _build_31_unemployment_shock_circular_flow_ripple,
    "32_tax_increase_shock_analysis": _build_32_tax_increase_shock_analysis,
    "33_public_tender_multiplier_effect": _build_33_public_tender_multiplier_effect,
    "34_grant_increase_retail_circulation": _build_34_grant_increase_retail_circulation,
    "35_leakages_in_real_world_economy": _build_35_leakages_in_real_world_economy,
    "36_injections_in_real_world_economy": _build_36_injections_in_real_world_economy,
    "37_closed_vs_open_economy_comparison": _build_37_closed_vs_open_economy_comparison,
    "38_distinguishing_factor_vs_goods_market_items": _build_38_distinguishing_factor_vs_goods_market_items,
    "39_entrepreneurship_profit_vs_labour_wage": _build_39_entrepreneurship_profit_vs_labour_wage,
    "40_natural_resources_and_capital_remuneration": _build_40_natural_resources_and_capital_remuneration,
    "41_government_infrastructure_enabling_business": _build_41_government_infrastructure_enabling_business,
    "42_vat_collection_chain_in_circular_flow": _build_42_vat_collection_chain_in_circular_flow,
    "43_circular_flow_diagram_missing_label_svg": _build_43_circular_flow_diagram_missing_label_svg,
    "44_municipal_rates_and_local_circular_flow": _build_44_municipal_rates_and_local_circular_flow,
    "45_informal_sector_participation_in_flow": _build_45_informal_sector_participation_in_flow,
    "46_financial_institutions_intermediary_bridge": _build_46_financial_institutions_intermediary_bridge,
    "47_foreign_sector_imports_exports_extension": _build_47_foreign_sector_imports_exports_extension,
    "48_tracing_complete_rand_cycle": _build_48_tracing_complete_rand_cycle,
    "49_diagnosing_circular_flow_misconceptions": _build_49_diagnosing_circular_flow_misconceptions,
    "50_circular_flow_policy_scenario_synthesis": _build_50_circular_flow_policy_scenario_synthesis,
}
