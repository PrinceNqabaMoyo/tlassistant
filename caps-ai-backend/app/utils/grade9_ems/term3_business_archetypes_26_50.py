"""Grade 9 EMS - Term 3 Functions of a Business: Archetypes 26 to 50.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Functions of a business.md,
curriculum_docs/EMS_Gr9/Term 3/11-Functions of a Business.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African business & risk management contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS

from .term3_business_archetypes_01_25 import (
    _build_mcq,
    _build_short,
    _build_table,
    _esc,
    _fmt_r,
    _make_cell,
    get_ems_scenario,
)


def arch_26_risk_management_definition_and_four_responses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Every department at **{sc['business']}** in **{sc['area']}** manages uncertainty proactively through **risk management**.\n\n"
        "What does **risk management** require an enterprise to do?"
    )
    correct = "Identify potential threats to assets, staff, or cash flow, assess their likelihood and impact, and put controls or insurance in place to prevent or reduce loss."
    distractors = [
        "Shut down every business operation whenever normal market competition appears.",
        "Ignore machinery faults until a warehouse fire forces permanent closure.",
        "Transfer all company payroll obligations directly onto retail customers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_26",
        subskill="26_risk_management_definition_and_four_responses",
        title="Risk Management Purpose & Strategy",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Risk management** helps **{sc['business']}** spot operational, financial, legal, and reputational threats early so losses are avoided, reduced, or insured."
        ),
        hints={
            "tier_1": "Good managers don't wait for disasters — they identify, assess, and mitigate.",
            "tier_2": "Identify threats -> evaluate impact/likelihood -> mitigate via controls or insurance.",
            "tier_3": correct,
        },
        misconception_tags=["equating_risk_management_with_eliminating_all_risk"],
    )


def arch_27_general_management_strategic_and_succession_risks(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** depends heavily on its founder without written contingency plans or trained deputies.\n\n"
        "Identify **two** strategic risks faced by the **General Management** function and propose **one** risk-control measure for each."
    )
    expected = (
        "1. Key-person/succession risk -> mitigate by mentoring deputy managers and documenting procedures; "
        "2. Rigid outdated strategy when competitors shift -> mitigate by regular environmental/SWOT reviews and contingency planning."
    )
    sol = (
        f"**General Management Risk Controls ({sc['business']}) [4 marks]:**\n\n"
        "1. **Leadership / Succession Risk:** Train deputy supervisors and maintain clear written SOPs so operations continue if the founder is absent **[2]**.\n"
        "2. **Strategic Blindness Risk:** Conduct quarterly target reviews and draft backup **contingency plans** for load-shedding, supply shocks, or rivals **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_27",
        subskill="27_general_management_strategic_and_succession_risks",
        title="General Management Strategic & Succession Risks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "What happens if the sole leader falls ill or market trends shift unexpectedly?",
            "tier_2": "Include succession/deputy training and contingency/strategic reviews.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Key-person/succession risk + deputy training or SOPs", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Market/operational disruption risk + contingency planning", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_general_management_faces_no_operational_risks"],
    )


def arch_28_administration_data_loss_cybersecurity_and_popia_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"The **Administration team** at **{sc['business']}** in **{sc['area']}** stores client ID numbers, contracts, and payroll records digitally.\n\n"
        "Which pair of controls best protects Administration against **data loss** and **POPIA privacy breaches**?"
    )
    correct = "Automated encrypted off-site/cloud backups combined with strong passwords and role-based access permissions."
    distractors = [
        "Saving every customer file on one unencrypted desktop computer without backups.",
        "Posting signed customer tax details on public social media pages for verification.",
        "Writing all bank PINs on sticky notes taped to public reception desks.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_28",
        subskill="28_administration_data_loss_cybersecurity_and_popia_risk",
        title="Administration Risks: Data Loss & POPIA",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Under South Africa's **POPIA**, Administration at **{sc['business']}** must guard personal information using encrypted cloud backups, access controls, and secure disposal."
        ),
        hints={
            "tier_1": "Protect data both from hardware theft/crash AND unauthorised viewing.",
            "tier_2": "Encrypted off-site/cloud backups + role-based passwords/access controls.",
            "tier_3": correct,
        },
        misconception_tags=["storing_sensitive_business_records_without_backup_or_encryption"],
    )


def arch_29_purchasing_supplier_failure_and_stock_shortage_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** buys 100% of its packaging exclusively from **{sup}**.\n\n"
        "1. Explain **one** major supply-chain risk of relying on a single supplier.\n"
        "2. State **two** risk-management strategies Purchasing should implement before a shortage occurs."
    )
    expected = (
        f"1. If {sup} faces transport strikes, bankruptcy, or sudden price hikes, production/sales halt immediately. "
        "2. Qualify backup secondary suppliers, hold minimum buffer/safety stock, and verify delivery quality on arrival."
    )
    sol = (
        f"**Purchasing Risk Management ({sc['business']} & {sup}) [4 marks]:**\n\n"
        f"1. **Single-Supplier Risk:** Any strike, flood, or insolvency at **{sup}** cuts off raw inputs and halts sales **[2]**.\n"
        "2. **Mitigation Strategies:** Maintain **approved backup suppliers**, hold a calculated **safety buffer stock**, and inspect incoming batches against signed contracts **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_29",
        subskill="29_purchasing_supplier_failure_and_stock_shortage_risk",
        title="Purchasing Risk: Single-Supplier Dependence",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "What happens if one sole supplier stops delivering, and how do you avoid being stranded?",
            "tier_2": "Single-source vulnerability -> backup suppliers + buffer/safety stock.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Single-supplier outage / price hike stops operations", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Secondary/backup suppliers + safety buffer stock", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_one_cheap_supplier_needs_no_backup"],
    )


def arch_30_purchasing_reorder_point_and_buffer_stock_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    daily_use = rng.choice([25, 30, 40])
    lead_days = rng.choice([4, 5, 6])
    safety_stock = rng.choice([80, 100, 120])
    lead_demand = daily_use * lead_days
    reorder_point = lead_demand + safety_stock
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** uses **{daily_use} crates per day** of stock ordered from **{sup}**.\n"
        f"Supplier delivery takes **{lead_days} days** (lead time), and Purchasing maintains a **safety buffer of {safety_stock} crates** to prevent stock-outs.\n\n"
        "Calculate:\n"
        f"1. Units consumed during the **{lead_days}-day** delivery lead time.\n"
        "2. The exact **reorder point (in crates)** when Purchasing must place a new order."
    )
    expected = f"1. Lead-time demand = {lead_demand} crates; 2. Reorder point = {reorder_point} crates."
    sol = (
        f"**Reorder Point Calculation ({sc['business']}) [3 marks]:**\n\n"
        f"1. **Lead-Time Usage:** ${daily_use} \\times {lead_days} = {lead_demand}$ crates **[1]**\n"
        f"2. **Reorder Point:** ${lead_demand} + {safety_stock} = {reorder_point}$ crates **[2]**\n\n"
        f"*(Placing an order when stock hits **{reorder_point} crates** protects against delayed deliveries.)*"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_30",
        subskill="30_purchasing_reorder_point_and_buffer_stock_calculation",
        title="Calculating Inventory Reorder Point",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Reorder Point = (Daily Usage x Lead Time Days) + Safety Buffer Stock.",
            "tier_2": f"({daily_use} x {lead_days}) + {safety_stock}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Lead-time usage = {lead_demand} crates", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Reorder point = {reorder_point} crates", "marks": 2, "editable": True},
        ],
        misconception_tags=["ordering_only_when_stock_reaches_zero"],
    )


def arch_31_production_machinery_breakdown_and_quality_defect_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Production managers at **{sc['business']}** in **{sc['area']}** worry about sudden machine breakdowns, load-shedding, and faulty output batches.\n\n"
        "Which risk-control plan **directly mitigates** operational Production risks?"
    )
    correct = "Scheduled preventive equipment maintenance, backup power (generator/solar), worker safety training, and stage-by-stage quality inspections."
    distractors = [
        "Eliminating all safety inspections to speed up assembly belts.",
        "Offering 60-day credit extensions to slow-paying retail shoppers.",
        "Sponsoring a local marathon with branded corporate water bottles.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_31",
        subskill="31_production_machinery_breakdown_and_quality_defect_risk",
        title="Mitigating Production & Maintenance Risks",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Preventive maintenance, backup power, and strict in-line quality inspections keep **{sc['business']}** safe, consistent, and resilient against costly factory downtime."
        ),
        hints={
            "tier_1": "Match equipment/energy/defect hazards with maintenance, backup power, and QA.",
            "tier_2": "Preventive servicing + backup power + safety training + quality checks.",
            "tier_3": correct,
        },
        misconception_tags=["waiting_until_machines_fail_before_servicing"],
    )


def arch_32_production_defect_rate_and_scrap_loss_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    batch = rng.choice([1000, 1500, 2000])
    defect_pct = rng.choice([3, 4, 5])
    unit_cost = rng.choice([40, 50, 60])
    defective_units = int(batch * defect_pct / 100)
    usable_units = batch - defective_units
    scrap_loss = defective_units * unit_cost
    prompt = (
        f"During a production run of **{batch} units** at **{sc['business']}**, quality inspectors reject **{defect_pct}%** as defective scrap.\n"
        f"Each unit costs **{_fmt_r(unit_cost)}** to manufacture.\n\n"
        "Calculate:\n"
        "1. The number of **defective units** rejected and **usable units** remaining.\n"
        "2. The direct **Rand scrap loss** caused by those defects."
    )
    expected = (
        f"1. Defective = {defective_units} units; Usable = {usable_units} units. "
        f"2. Direct scrap loss = {_fmt_r(scrap_loss)}."
    )
    sol = (
        f"**Production Defect & Scrap Cost ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Defective Units ({defect_pct}%):** $\\frac{{{defect_pct}}}{{100}} \\times {batch} = {defective_units}$ units **[1]**\n"
        f"   **Usable Units:** ${batch} - {defective_units} = {usable_units}$ units **[1]**\n"
        f"2. **Rand Scrap Loss:** ${defective_units} \\times {_fmt_r(unit_cost)} = {_fmt_r(scrap_loss)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_32",
        subskill="32_production_defect_rate_and_scrap_loss_calculation",
        title="Production Defect Rate & Scrap Loss",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compute defective units first, subtract from batch, then multiply defective units by unit cost.",
            "tier_2": f"Defective = {defect_pct}% of {batch}; Loss = defective x {_fmt_r(unit_cost)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Defective units = {defective_units}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Usable units = {usable_units}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Scrap loss = {_fmt_r(scrap_loss)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["multiplying_defect_pct_by_selling_price_or_ignoring_usable_count"],
    )


def arch_33_marketing_reputation_and_unsold_inventory_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** suffers declining sales after launching a product without researching buyer preferences and running exaggerated adverts.\n\n"
        "Explain **two** Marketing risks shown here and state how each can be corrected."
    )
    expected = (
        "1. Launching unwanted products -> fix via thorough customer market research before production; "
        "2. Misleading advertising damages trust and breaches Consumer Protection Act (CPA) -> fix with honest claims and clear warranties."
    )
    sol = (
        f"**Marketing Risks & Remedies ({sc['business']}) [4 marks]:**\n\n"
        "1. **Demand Mismatch Risk:** Unsold stock piles up when tastes are guessed -> run **surveys/market research** first to align the 4 Ps **[2]**.\n"
        "2. **Misleading Claims / Legal Risk:** Exaggerated adverts alienate repeat buyers and violate South Africa's **Consumer Protection Act** -> ensure **truthful transparent promotion** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_33",
        subskill="33_marketing_reputation_and_unsold_inventory_risk",
        title="Marketing Risks: Demand Mismatch & CPA Trust",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Match guessing customer wants -> market research; false adverts -> honest CPA-compliant ads.",
            "tier_2": "Identify demand mismatch (research) + misleading claims/CPA loss of trust (honest promotion).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Demand mismatch/unsold stock solved by market research", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Trust/CPA risk from false adverts solved by honest communication", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_aggressive_ads_overcome_poor_product_fit"],
    )


def arch_34_financial_cash_flow_insolvency_and_fraud_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Even with healthy monthly sales in **{sc['area']}**, **{sc['business']}** struggles to pay urgent bills and worries about petty cash theft.\n\n"
        "Which financial controls directly address **cash-flow insolvency** and **internal fraud risks**?"
    )
    correct = "Monthly cash-flow forecasting, strict debtor credit vetting, and internal controls (segregation of duties + dual bank authorisations)."
    distractors = [
        "Giving one single clerk unchecked authority to receive cash, sign cheques, and edit ledgers.",
        "Extending unlimited interest-free credit to customers with no background checks.",
        "Eliminating financial statements so expenses remain private from managers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_34",
        subskill="34_financial_cash_flow_insolvency_and_fraud_risk",
        title="Financial Risks: Liquidity & Fraud Controls",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Cash budgets prevent liquidity crunches, credit checks reduce bad debts, and **segregation of duties** stops fraud inside **{sc['business']}**."
        ),
        hints={
            "tier_1": "Never let one person handle cash, authorise payments, and record books alone.",
            "tier_2": "Cash-flow budgets + debtor credit vetting + dual sign-off / segregation of duties.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_high_sales_automatically_prevent_cash_flow_insolvency"],
    )


def arch_35_financial_working_capital_and_cash_shortfall_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_cash = rng.choice([25000, 35000, 45000])
    cash_in = rng.choice([140000, 160000, 180000])
    cash_out = cash_in + rng.choice([55000, 65000, 75000])
    closing_bal = open_cash + cash_in - cash_out
    shortfall = abs(closing_bal)
    prompt = (
        f"The Financial manager at **{sc['business']}** in **{sc['area']}** prepares a monthly cash budget:\n"
        f"- Opening bank balance: **{_fmt_r(open_cash)}**\n"
        f"- Expected cash inflows from sales & debtors: **{_fmt_r(cash_in)}**\n"
        f"- Planned cash outflows (salaries, stock & rent): **{_fmt_r(cash_out)}**\n\n"
        "Calculate the projected **closing cash balance**, and state the minimum **bank overdraft facility** required so cheques do not bounce."
    )
    expected = (
        f"Projected closing cash balance = -{_fmt_r(shortfall)} (cash deficit of {_fmt_r(shortfall)}); "
        f"Minimum overdraft facility required = {_fmt_r(shortfall)}."
    )
    sol = (
        f"**Cash Budget Shortfall Analysis ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Net Cash Flow:** ${_fmt_r(cash_in)} - {_fmt_r(cash_out)} = -{_fmt_r(cash_out - cash_in)}$ **[1]**\n"
        f"2. **Projected Closing Balance:** ${_fmt_r(open_cash)} - {_fmt_r(cash_out - cash_in)} = -{_fmt_r(shortfall)}$ **[2]**\n"
        f"3. **Minimum Overdraft Reserve:** Arrange at least **{_fmt_r(shortfall)}** in advance (or speed up debtor receipts / defer non-urgent outlays) **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_35",
        subskill="35_financial_working_capital_and_cash_shortfall_calc",
        title="Cash Budget Deficit & Overdraft Planning",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Closing Cash = Opening Balance + Cash Inflows - Cash Outflows.",
            "tier_2": f"{_fmt_r(open_cash)} + {_fmt_r(cash_in)} - {_fmt_r(cash_out)} = negative deficit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Net cash flow deficit -{_fmt_r(cash_out - cash_in)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Closing balance -{_fmt_r(shortfall)}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Minimum overdraft needed {_fmt_r(shortfall)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgetting_to_add_opening_cash_balance_when_calculating_shortfall"],
    )


def arch_36_human_resources_staff_turnover_and_skills_shortage_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** experiences **high staff turnover** (resignations) and frequent **CCMA labour disputes**.\n\n"
        "Explain **two** operational risks of high staff turnover and give **two** HR strategies to retain skilled employees."
    )
    expected = (
        "Risks: Expensive repeated recruitment/training costs and lost institutional skill/productivity. "
        "Retention strategies: Competitive fair pay/benefits, structured SETA skills development, clear career paths, and respectful LRA-compliant grievance handling."
    )
    sol = (
        f"**HR Retention & Risk Management ({sc['business']}) [4 marks]:**\n\n"
        "1. **Turnover Risks:** Drives up **hiring and retraining costs** **[1]** while draining experienced **workplace productivity and customer continuity** **[1]**.\n"
        "2. **HR Retention Controls:** Offer **fair market pay and safe conditions**, invest in **SETA upskilling/career growth**, and resolve grievances early under **LRA/BCEA** rules **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_36",
        subskill="36_human_resources_staff_turnover_and_skills_shortage_risk",
        title="HR Risk: Staff Turnover & Retention",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think of replacement costs + skill loss, and how HR keeps good workers happy.",
            "tier_2": "Include cost/productivity loss + fair pay, training, and fair workplace practices.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Costly rehiring/retraining", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Loss of productivity / institutional experience", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Two retention actions (fair pay, training, supportive culture)", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_replacing_trained_workers_costs_nothing"],
    )


def arch_37_public_relations_negative_publicity_crisis_risk(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"A customer posts a viral complaint about defective packaging sold by **{sc['business']}** in **{sc['area']}**, sparking negative commentary online.\n\n"
        "What is the **most effective Public Relations risk-management response**?"
    )
    correct = "Have a designated spokesperson respond promptly with verified facts, apologise sincerely, recall/replace faulty items, and share preventive fixes publicly."
    distractors = [
        "Delete customer comments angrily and blame competing local businesses without evidence.",
        "Ignore local journalists completely and shut down all customer service phone lines.",
        "Double retail prices overnight to recover any lost sales revenue immediately.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_37",
        subskill="37_public_relations_negative_publicity_crisis_risk",
        title="PR Crisis Response to Negative Publicity",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Transparent, rapid accountability restores public confidence in **{sc['business']}** far faster than defensiveness or silence."
        ),
        hints={
            "tier_1": "Good crisis PR owns mistakes quickly, communicates clearly, and fixes the cause.",
            "tier_2": "Designated spokesperson -> honest prompt apology + replacement + corrective fix.",
            "tier_3": correct,
        },
        misconception_tags=["believing_deleting_complaints_repairs_brand_trust"],
    )


def arch_38_function_risk_mitigation_matching_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Encrypted daily cloud backups & strict POPIA passwords", "Administration", "Data & privacy protection"),
        ("Diversifying across two approved wholesale material vendors", "Purchasing", "Supply continuity"),
        ("Segregation of banking duties & credit vetting on debtors", "Financial", "Fraud & bad-debt control"),
        ("Scheduled preventive machine servicing & backup power", "Production", "Downtime & defect prevention"),
        ("Pre-launch consumer surveys & CPA-compliant advertising", "Marketing", "Demand & compliance control"),
        ("SETA safety training & compliant grievance procedures", "Human Resources", "Safety & CCMA compliance"),
        ("Crisis media spokesperson & community CSR partnerships", "Public Relations", "Reputation protection"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Risk-Control Measure", "Risk Focus", "Responsible Business Function"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Risk-Control Measure | Risk Focus | Business Function |", "| :--- | :--- | :--- |"]
    for idx, (ctrl, fn_name, foc) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", ctrl, "given"),
            _make_cell(f"t0_r{idx}_c1", foc, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = fn_name
        cell_hints[coord] = "Enter exact function name (Administration, Purchasing, Financial, Production, Marketing, Human Resources, or Public Relations)."
        memo_lines.append(f"| {ctrl} | {foc} | {fn_name} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Departmental Risk Controls Schedule ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bf_38",
        subskill="38_function_risk_mitigation_matching_table",
        title="Departmental Risk-Control Matching Table",
        prompt=(
            f"Assign each internal risk-control measure at **{sc['business']}** in **{sc['area']}** to its responsible **Business Function** in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Link backups->Admin, vendors->Purchasing, fraud->Financial, machines->Production, ads->Marketing, safety->HR, media->PR.",
            "tier_2": "Write exact function names in Column 3.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Assigns to {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["misassigning_departmental_risk_controls"],
    )


def arch_39_small_micro_enterprise_multi_hat_owner_challenge(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(NAMES)
    area = rng.choice(AREAS)
    prompt = (
        f"**{founder}** runs a 3-person micro-bakery in **{area}**, personally ordering flour, baking bread, delivering orders, posting flyers, and keeping cashbooks.\n\n"
        "1. Does a tiny micro-business still perform all **eight business functions**? Explain briefly.\n"
        "2. State **one** risk **{founder}** faces wearing every departmental hat alone and **one** remedy as sales grow."
    )
    expected = (
        f"1. Yes — all 8 functions still take place even without separate departments; {founder} performs multiple functions personally. "
        "2. Risk: Owner burnout, errors, or neglected financial/admin filing; Remedy: Outsource bookkeeping or hire specialised staff/supervisors as turnover expands."
    )
    sol = (
        f"**Micro-Enterprise Functions ({founder}, {area}) [4 marks]:**\n\n"
        f"1. **Presence of All 8 Functions:** Yes — small size eliminates separate departments, NOT the functions; **{founder}** still buys inputs, produces, markets, manages cash, and plans **[2]**.\n"
        "2. **Burnout Risk & Remedy:** Overwork causes accounting delays or customer neglect -> hire/outsource specialist roles (e.g., bookkeeper or delivery assistant) as revenue allows **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_39",
        subskill="39_small_micro_enterprise_multi_hat_owner_challenge",
        title="Eight Functions in Micro & Small Enterprises",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Are tasks like buying, baking, selling, and banking happening even with one owner?",
            "tier_2": "Yes, functions happen without separate rooms/staff; burnout/errors fixed by delegating or outsourcing.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Yes: all 8 functions exist, handled by one/few people", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Burnout/error risk + delegating/outsourcing/hiring specialists", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_small_firms_have_only_one_business_function"],
    )


def arch_40_large_corporation_departmentalisation_benefits(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    branches = rng.choice([6, 9, 14])
    prompt = (
        f"Now operating **{branches} branches** across South Africa, **{sc['business']}** establishes dedicated specialist departments for Finance, HR, Marketing, and Production.\n\n"
        "What is the **primary economic advantage** of dividing a large business into specialised functional departments?"
    )
    correct = "Division of labour allows trained specialists to work faster, reduce errors, and achieve higher quality and economies of scale."
    distractors = [
        "Specialised departments completely eliminate the need for any General Management oversight.",
        "Large companies stop paying VAT and municipal tariffs once they exceed five branches.",
        "Departmentalisation guarantees every employee earns identical executive bonuses.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_40",
        subskill="40_large_corporation_departmentalisation_benefits",
        title="Benefits of Departmental Specialisation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Across **{branches}** branches, **specialisation** puts qualified accountants in Finance and trained engineers in Production, improving efficiency and accountability."
        ),
        hints={
            "tier_1": "Why hire a full-time accountant and HR officer instead of asking factory bakers to do taxes?",
            "tier_2": "Division of labour & specialist expertise increase speed, quality, and accountability.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_departmentalisation_eliminates_coordination_needs"],
    )


def arch_41_technology_modernising_administration_and_finance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** replaces paper ledgers and hand-written receipts with **cloud accounting software, barcode POS scanners, and automated EFT payroll**.\n\n"
        "Give **two** measurable improvements digital technology brings to **Administration and Finance**."
    )
    expected = (
        "1. Faster real-time invoicing, instant stock updates, and fewer manual arithmetic/transposition errors; "
        "2. Automated cloud backup protection and quicker VAT/SARS/cash-flow reporting for General Management."
    )
    sol = (
        f"**Digital Modernisation at {sc['business']} [4 marks]:**\n\n"
        "1. **Speed & Accuracy:** Barcode POS and cloud software automate totals, eliminating manual addition errors and saving clerical hours **[2]**.\n"
        "2. **Real-Time Oversight & Backups:** Managers view live cash flow/inventory instantly while off-site cloud backups protect records against theft or fire **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_41",
        subskill="41_technology_modernising_administration_and_finance",
        title="Technology Impact on Admin & Finance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare slow hand-written ledgers with live cloud systems and POS scanners.",
            "tier_2": "Mention speed/fewer human errors AND live reporting/cloud backup security.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Faster processing and fewer manual calculation errors", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Real-time reporting / secure cloud backups", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_digital_systems_need_zero_cybersecurity_controls"],
    )


def arch_42_purchasing_bulk_discount_vs_storage_cost_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    order_amt = rng.choice([80000, 100000, 120000])
    disc_pct = rng.choice([6, 8, 10])
    gross_saving = int(order_amt * disc_pct / 100)
    extra_storage = rng.choice([1800, 2400, 3000])
    net_benefit = gross_saving - extra_storage
    prompt = (
        f"Supplier **{sup}** offers **{sc['business']}** in **{sc['area']}** a **{disc_pct}% bulk trade discount** on a **{_fmt_r(order_amt)}** raw-material order.\n"
        f"However, storing the larger delivery will cost **{_fmt_r(extra_storage)}** in extra warehouse space and security.\n\n"
        "Calculate the **gross bulk discount saving** and the **net financial benefit** to decide if Purchasing should accept."
    )
    expected = (
        f"Gross discount saving = {_fmt_r(gross_saving)}; "
        f"Net benefit = {_fmt_r(net_benefit)} (Yes, Purchasing should accept if stock will not perish before use)."
    )
    sol = (
        f"**Bulk Purchasing Trade-Off ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Gross Discount ({disc_pct}%):** $\\frac{{{disc_pct}}}{{100}} \\times {_fmt_r(order_amt)} = {_fmt_r(gross_saving)}$ **[2]**\n"
        f"2. **Net Financial Benefit:** ${_fmt_r(gross_saving)} - {_fmt_r(extra_storage)} = {_fmt_r(net_benefit)}$ **[1]**\n"
        "3. **Decision:** **Accept** the bulk order (positive net gain), provided materials do not spoil before production **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_42",
        subskill="42_purchasing_bulk_discount_vs_storage_cost_calculation",
        title="Bulk Discount vs Warehouse Holding Cost",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Calculate the percentage discount first, then subtract extra storage expenses.",
            "tier_2": f"Saving = {disc_pct}% of {_fmt_r(order_amt)}; subtract {_fmt_r(extra_storage)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross discount {_fmt_r(gross_saving)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Net benefit {_fmt_r(net_benefit)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Accept decision with non-spoilage caveat", "marks": 1, "editable": True},
        ],
        misconception_tags=["accepting_bulk_discounts_without_deducting_holding_costs"],
    )


def arch_43_marketing_promotional_campaign_roi_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    ad_spend = rng.choice([8000, 10000, 12000])
    extra_sales = rng.choice([45000, 50000, 60000])
    gp_pct = 40
    extra_gp = int(extra_sales * gp_pct / 100)
    net_gain = extra_gp - ad_spend
    prompt = (
        f"Marketing at **{sc['business']}** in **{sc['area']}** spends **{_fmt_r(ad_spend)}** on local radio and social adverts.\n"
        f"The campaign generates **{_fmt_r(extra_sales)}** in incremental sales at a **40% gross profit margin**.\n\n"
        "Calculate the **extra gross profit** earned and the **net campaign profit** after deducting advertising spend."
    )
    expected = f"Extra gross profit = {_fmt_r(extra_gp)}; Net campaign profit = {_fmt_r(net_gain)}."
    sol = (
        f"**Marketing Campaign Evaluation ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Incremental Gross Profit (40%):** $0{{,}}40 \\times {_fmt_r(extra_sales)} = {_fmt_r(extra_gp)}$ **[2]**\n"
        f"2. **Net Campaign Gain:** ${_fmt_r(extra_gp)} - {_fmt_r(ad_spend)} = {_fmt_r(net_gain)}$ **[2]**\n\n"
        f"*(Note: Always compare marketing spend against **gross profit**, not raw turnover.)*"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_43",
        subskill="43_marketing_promotional_campaign_roi_calculation",
        title="Marketing Campaign Return Analysis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Multiply extra sales by 40% gross margin first, then subtract ad spend.",
            "tier_2": f"40% of {_fmt_r(extra_sales)} minus {_fmt_r(ad_spend)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Extra gross profit {_fmt_r(extra_gp)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Net campaign profit {_fmt_r(net_gain)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_ad_spend_from_gross_sales_instead_of_gross_profit"],
    )


def arch_44_hr_training_investment_and_productivity_gain_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    train_cost = rng.choice([18000, 24000, 30000])
    monthly_gain = rng.choice([6000, 8000, 10000])
    payback_months = train_cost // monthly_gain
    annual_net = (monthly_gain * 12) - train_cost
    prompt = (
        f"The HR department at **{sc['business']}** in **{sc['area']}** invests **{_fmt_r(train_cost)}** in technical artisan training.\n"
        f"As defects drop and output rises, factory value-add increases by **{_fmt_r(monthly_gain)} per month**.\n\n"
        "Calculate:\n"
        "1. How many **months** it takes for the productivity gain to pay back the training investment.\n"
        "2. The **net gain** generated over a full **12-month year** after subtracting training costs."
    )
    expected = f"1. Payback = {payback_months} months; 2. Net 12-month gain = {_fmt_r(annual_net)}."
    sol = (
        f"**HR Training ROI ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Payback Period:** $\\frac{{{_fmt_r(train_cost)}}}{{{_fmt_r(monthly_gain)}}} = {payback_months}$ months **[2]**\n"
        f"2. **Annual Net Benefit (12 months):** $(12 \\times {_fmt_r(monthly_gain)}) - {_fmt_r(train_cost)} = {_fmt_r(monthly_gain * 12)} - {_fmt_r(train_cost)} = {_fmt_r(annual_net)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_44",
        subskill="44_hr_training_investment_and_productivity_gain_calc",
        title="HR Training Investment & Payback Analysis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Divide upfront training cost by monthly savings for payback; compute 12 months of gains minus cost.",
            "tier_2": f"Payback = {_fmt_r(train_cost)} / {_fmt_r(monthly_gain)}; Annual net = 12 x {_fmt_r(monthly_gain)} - {_fmt_r(train_cost)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Payback = {payback_months} months", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Annual net gain = {_fmt_r(annual_net)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_staff_training_purely_as_sunk_cost"],
    )


def arch_45_risk_impact_vs_likelihood_matrix_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    loss_amt = rng.choice([250000, 350000, 450000])
    budget_amt = rng.choice([28000, 35000, 42000])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 245" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="245" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Risk Matrix: {_esc(sc["business"])} (Mitigation Budget {_fmt_r(budget_amt)})</text>'
        '<text x="200" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">LOW IMPACT</text>'
        '<text x="455" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">HIGH IMPACT</text>'
        '<rect x="85" y="55" width="230" height="75" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="200" y="83" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">HIGH LIKELIHOOD / LOW</text>'
        '<text x="200" y="102" text-anchor="middle" font-size="10" fill="#92400e">Minor stationery delays</text>'
        '<text x="200" y="117" text-anchor="middle" font-size="10" fill="#92400e">Action: Standard checklists</text>'
        '<rect x="340" y="55" width="230" height="75" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        '<text x="455" y="83" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">PRIORITY ZONE (HIGH / HIGH)</text>'
        f'<text x="455" y="102" text-anchor="middle" font-size="10" fill="#b91c1c">Power outage &amp; data loss ({_fmt_r(loss_amt)})</text>'
        '<text x="455" y="117" text-anchor="middle" font-size="10" fill="#b91c1c">Action: Cloud backups + UPS</text>'
        '<rect x="85" y="140" width="230" height="75" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="200" y="168" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">LOW / LOW</text>'
        '<text x="200" y="188" text-anchor="middle" font-size="10" fill="#166534">Occasional bulb replacement</text>'
        '<text x="200" y="203" text-anchor="middle" font-size="10" fill="#166534">Action: Monitor &amp; accept</text>'
        '<rect x="340" y="140" width="230" height="75" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="455" y="168" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">LOW LIKELIHOOD / HIGH IMPACT</text>'
        '<text x="455" y="188" text-anchor="middle" font-size="10" fill="#1e40af">Factory fire or storm flood</text>'
        '<text x="455" y="203" text-anchor="middle" font-size="10" fill="#1e40af">Action: Transfer via Insurance</text>'
        '</svg>'
    )
    prompt = (
        f"Study the 2x2 **Risk Likelihood vs Financial Impact Matrix** for **{sc['business']}** (**{_fmt_r(budget_amt)}** risk budget; top exposure **{_fmt_r(loss_amt)}**).\n\n"
        f"1. Why does **{sc['business']}** allocate its **{_fmt_r(budget_amt)}** budget first to the **Priority Zone** (High Likelihood / High Impact)?\n"
        "2. How should a manager treat **Low Likelihood / High Impact** events (such as a factory fire) instead of leaving the firm exposed?"
    )
    expected = (
        f"1. High Likelihood + High Impact risks (e.g. {_fmt_r(loss_amt)} outage/data loss) occur frequently and cause severe financial harm, giving the highest return on {_fmt_r(budget_amt)} preventive spending. "
        "2. Transfer catastrophic rare risks via commercial insurance policies alongside fire sprinklers."
    )
    sol = (
        f"**Risk Prioritisation Analysis ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Priority Zone Focus:** Risks combining high frequency with severe **{_fmt_r(loss_amt)}** damage threaten daily survival, so **{_fmt_r(budget_amt)}** spent on cloud backups and UPS prevents repeated major losses **[2]**.\n"
        "2. **Rare Catastrophes (Low Likelihood / High Impact):** Cannot be ignored because one fire could bankrupt the firm -> **transfer the financial loss via insurance** plus fire safety gear **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_45",
        subskill="45_risk_impact_vs_likelihood_matrix_svg",
        title="Risk Likelihood vs Financial Impact Matrix",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare the top-right red box (Priority) with the bottom-right blue box (Insurance).",
            "tier_2": "Priority zone = urgent controls for frequent severe losses; rare catastrophes = insurance transfer.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Priority zone prevents frequent high-Rand losses immediately", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Transfer rare high-impact catastrophes via commercial insurance", "marks": 2, "editable": True},
        ],
        misconception_tags=["spending_mitigation_budget_on_trivial_risks_before_priority_zone"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_46_cross_function_problem_solving_product_recall_case(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    units = rng.choice([300, 450, 600])
    prompt = (
        f"A faulty seal is discovered in **{units} shipped product units** made by **{sc['business']}** in **{sc['area']}**.\n\n"
        "State **one** specific action each of these **four** functions must immediately take to resolve the crisis:\n"
        "1. **Production**  |  2. **Public Relations**  |  3. **Financial**  |  4. **Purchasing**"
    )
    expected = (
        "1. Production: Halt affected line, isolate root defect, and repair machinery/QA checks; "
        "2. Public Relations: Issue transparent recall notice, apologise, and coordinate replacements; "
        "3. Financial: Budget cash reserves for refunds/replacements and claim supplier/insurance cover; "
        "4. Purchasing: Trace faulty sealing batch with vendor and switch/audit raw material quality."
    )
    sol = (
        f"**Cross-Functional Recall Coordination ({units} units at {sc['business']}) [4 marks]:**\n\n"
        "1. **Production:** Pause the defective assembly line, fix machinery/calibration, and tighten quality inspections **[1]**.\n"
        "2. **Public Relations:** Publish an honest, urgent safety/recall notice and reassure customers with free replacements **[1]**.\n"
        "3. **Financial:** Allocate working capital for customer refunds/recall logistics and assess insurance/warranty recovery **[1]**.\n"
        "4. **Purchasing:** Investigate the batch with suppliers, hold faulty inputs, and source compliant seals **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_46",
        subskill="46_cross_function_problem_solving_product_recall_case",
        title="Cross-Functional Crisis Coordination (Product Recall)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Assign manufacturing repair, public apology, refund funding, and input tracing to the four departments.",
            "tier_2": "Production fixes line; PR handles recall messaging; Finance funds refunds; Purchasing audits vendor inputs.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Production halts line & fixes defect/QC", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "PR manages transparent recall & customer communication", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Financial funds refunds / insurance claim", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Purchasing traces faulty raw-material batch / vendor", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_one_department_handles_a_product_recall_alone"],
    )


def arch_47_insurable_vs_non_insurable_business_risks_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Warehouse fire or burglary of insured equipment", "Insurable", "Measurable physical peril"),
        ("Customer tastes shifting away from last year's fashion style", "Non-insurable", "Normal entrepreneurial market risk"),
        ("Delivery truck accident on the N3 highway", "Insurable", "Standard motor/transit peril"),
        ("Competitor opening next door with faster service", "Non-insurable", "Business competition risk"),
        ("Fidelity theft of bank funds by an employee", "Insurable", "Covered under fidelity/crime cover"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Business Risk Event", "Risk Nature", "Classification (Insurable vs Non-insurable)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Business Risk Event | Risk Nature | Classification |", "| :--- | :--- | :--- |"]
    for idx, (ev, cls, nat) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", ev, "given"),
            _make_cell(f"t0_r{idx}_c1", nat, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = cls
        cell_hints[coord] = "Enter exact word: Insurable or Non-insurable."
        memo_lines.append(f"| {ev} | {nat} | {cls} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Insurable vs Non-insurable Risks ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bf_47",
        subskill="47_insurable_vs_non_insurable_business_risks_table",
        title="Insurable vs Non-Insurable Business Risks",
        prompt=(
            f"Financial planners at **{sc['business']}** in **{sc['area']}** sort risks into coverable insurance perils versus normal commercial risks.\n\n"
            "Enter **Insurable** or **Non-insurable** in Column 3 for each risk event."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Insurers cover unpredictable accidental perils (fire, crashes, theft), NOT ordinary market competition or trend shifts.",
            "tier_2": "Write exact terms: Insurable or Non-insurable.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Classifies as {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["thinking_insurance_protects_businesses_against_market_competition"],
    )


def arch_48_sustainable_ethical_sourcing_in_purchasing_and_pr(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** shifts Purchasing orders to certified South African SMMEs using recyclable packaging.\n\n"
        "How does **ethical and sustainable procurement** create shared value for both **Purchasing** and **Public Relations**?"
    )
    correct = "It ensures reliable local input supply and environmental compliance while boosting brand goodwill, customer loyalty, and B-BBEE/community support."
    distractors = [
        "It stops Production from needing electricity or quality standards.",
        "It allows Administration to destroy historical tax invoices legally.",
        "It replaces the Financial function's responsibility to prepare balance sheets.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_48",
        subskill="48_sustainable_ethical_sourcing_in_purchasing_and_pr",
        title="Ethical Sourcing & PR Reputation Synergy",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Partnering with ethical local vendors gives **{sc['business']}** shorter reliable supply chains (Purchasing) and authentic positive community goodwill (Public Relations)."
        ),
        hints={
            "tier_1": "Connect reliable local ethical suppliers to community reputation and loyalty.",
            "tier_2": "Purchasing gains resilient ethical inputs while PR builds strong brand goodwill.",
            "tier_3": correct,
        },
        misconception_tags=["viewing_ethical_sourcing_as_disconnected_from_brand_value"],
    )


def arch_49_internal_vs_external_communication_admin_pr_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Both **Administration** and **Public Relations** handle communication at **{sc['business']}** in **{sc['area']}**.\n\n"
        "What distinguishes **Administration communication** from **Public Relations communication**?"
    )
    correct = "Administration distributes internal operational records, memos, and invoices for workflow efficiency, whereas PR communicates externally to build public image and stakeholder trust."
    distractors = [
        "Administration publishes TV commercials while PR repairs warehouse forklifts.",
        "Administration handles customer complaints while PR tracks weekly raw material scrap.",
        "Both functions exclusively manage factory payroll taxes for SARS.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_49",
        subskill="49_internal_vs_external_communication_admin_pr_distinction",
        title="Communication Roles: Administration vs PR",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"At **{sc['business']}**, **Administration** ensures internal offices and files flow smoothly, while **Public Relations** shapes public perception and media dialogue externally."
        ),
        hints={
            "tier_1": "Contrast internal office memos/records against external reputation and media.",
            "tier_2": "Admin = internal record & office flow; PR = external image & stakeholder trust.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_internal_office_admin_with_external_pr"],
    )


def arch_50_holistic_eight_functions_and_risk_governance_synthesis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Advise the board of **{sc['business']}** in **{sc['area']}** on integrating **all eight business functions** with proactive **risk management**:\n\n"
        "1. Explain how **General Management** (POLC) keeps Finance, Marketing, and Production aligned.\n"
        "2. Name **one** specific risk and **one** control measure for **Human Resources**, **Administration**, and **Purchasing**.\n"
        "3. State why failure in any **one** function threatens the profitability of the whole firm."
    )
    expected = (
        "1. General Management plans company targets, organises cross-departmental teams, leads motivation, and controls budgets/output so Marketing demand matches Production supply within Financial limits. "
        "2. HR: skills loss/strikes -> fair pay, SETA training, LRA compliance; Admin: data loss/POPIA breach -> encrypted cloud backups & passwords; Purchasing: single-supplier outage -> multiple approved vendors & safety stock. "
        "3. All 8 functions are interdependent — a bottleneck or loss in one disrupts customers, cash flow, and survival across the whole business."
    )
    sol = (
        f"**Integrated Governance Blueprint ({sc['business']}) [6 marks]:**\n\n"
        "1. **General Management Coordination (POLC):** Aligns Marketing forecasts with Production capacity and Finance cash budgets through clear goals, structure, leadership, and variance control **[2]**.\n"
        "2. **Three Departmental Risk Controls:**\n"
        "   - **HR:** Turnover/labour disputes -> fair conditions, **SETA training**, and **LRA** procedures **[1]**.\n"
        "   - **Administration:** Cyber/record loss -> encrypted **cloud backups** and **POPIA** access locks **[1]**.\n"
        "   - **Purchasing:** Supplier interruption -> **dual sourcing** and **buffer stock** **[1]**.\n"
        "3. **Systemic Interdependence:** Because inputs, cash, records, staff, and reputation flow between departments, failure in one function quickly stalls the entire business **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_50",
        subskill="50_holistic_eight_functions_and_risk_governance_synthesis",
        title="Holistic Business Functions & Risk Governance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Connect POLC coordination -> specific departmental controls -> why all 8 functions depend on each other.",
            "tier_2": "Cover POLC alignment, HR/Admin/Purchasing risk controls, and systemic interdependence.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "General Management POLC aligns Finance, Production & Marketing", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "HR risk + control (training, fair pay, LRA compliance)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Admin risk + control (cloud backups, POPIA security)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Purchasing risk + control (backup suppliers, buffer stock)", "marks": 1, "editable": True},
            {"id": "mp_5", "desc": "Explains interdependence / systemic ripple impact", "marks": 1, "editable": True},
        ],
        misconception_tags=["treating_departments_as_independent_from_risk_governance"],
    )


BUILDERS_26_50 = {
    "26_risk_management_definition_and_four_responses": arch_26_risk_management_definition_and_four_responses,
    "27_general_management_strategic_and_succession_risks": arch_27_general_management_strategic_and_succession_risks,
    "28_administration_data_loss_cybersecurity_and_popia_risk": arch_28_administration_data_loss_cybersecurity_and_popia_risk,
    "29_purchasing_supplier_failure_and_stock_shortage_risk": arch_29_purchasing_supplier_failure_and_stock_shortage_risk,
    "30_purchasing_reorder_point_and_buffer_stock_calculation": arch_30_purchasing_reorder_point_and_buffer_stock_calculation,
    "31_production_machinery_breakdown_and_quality_defect_risk": arch_31_production_machinery_breakdown_and_quality_defect_risk,
    "32_production_defect_rate_and_scrap_loss_calculation": arch_32_production_defect_rate_and_scrap_loss_calculation,
    "33_marketing_reputation_and_unsold_inventory_risk": arch_33_marketing_reputation_and_unsold_inventory_risk,
    "34_financial_cash_flow_insolvency_and_fraud_risk": arch_34_financial_cash_flow_insolvency_and_fraud_risk,
    "35_financial_working_capital_and_cash_shortfall_calc": arch_35_financial_working_capital_and_cash_shortfall_calc,
    "36_human_resources_staff_turnover_and_skills_shortage_risk": arch_36_human_resources_staff_turnover_and_skills_shortage_risk,
    "37_public_relations_negative_publicity_crisis_risk": arch_37_public_relations_negative_publicity_crisis_risk,
    "38_function_risk_mitigation_matching_table": arch_38_function_risk_mitigation_matching_table,
    "39_small_micro_enterprise_multi_hat_owner_challenge": arch_39_small_micro_enterprise_multi_hat_owner_challenge,
    "40_large_corporation_departmentalisation_benefits": arch_40_large_corporation_departmentalisation_benefits,
    "41_technology_modernising_administration_and_finance": arch_41_technology_modernising_administration_and_finance,
    "42_purchasing_bulk_discount_vs_storage_cost_calculation": arch_42_purchasing_bulk_discount_vs_storage_cost_calculation,
    "43_marketing_promotional_campaign_roi_calculation": arch_43_marketing_promotional_campaign_roi_calculation,
    "44_hr_training_investment_and_productivity_gain_calc": arch_44_hr_training_investment_and_productivity_gain_calc,
    "45_risk_impact_vs_likelihood_matrix_svg": arch_45_risk_impact_vs_likelihood_matrix_svg,
    "46_cross_function_problem_solving_product_recall_case": arch_46_cross_function_problem_solving_product_recall_case,
    "47_insurable_vs_non_insurable_business_risks_table": arch_47_insurable_vs_non_insurable_business_risks_table,
    "48_sustainable_ethical_sourcing_in_purchasing_and_pr": arch_48_sustainable_ethical_sourcing_in_purchasing_and_pr,
    "49_internal_vs_external_communication_admin_pr_distinction": arch_49_internal_vs_external_communication_admin_pr_distinction,
    "50_holistic_eight_functions_and_risk_governance_synthesis": arch_50_holistic_eight_functions_and_risk_governance_synthesis,
}
