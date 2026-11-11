"""
Grade 11 Accounting: Cost Accounting (Manufacturing General Ledger Accounts & Break-Even)
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting (Term 3).
Focuses on Manufacturing General Ledger T-accounts (Raw Material Stock, WIP Stock, Finished Goods Stock,
Factory Overhead Cost) and Break-Even Analysis, distinct from Grade 12's full Production Cost Statement.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "raw_material_stock_ledger_taccount",
    "work_in_process_stock_ledger_taccount",
    "finished_goods_stock_ledger_taccount",
    "factory_overhead_cost_ledger_taccount",
    "direct_and_indirect_labour_ledger_allocation",
    "contribution_per_unit_and_breakeven_units",
    "breakeven_interpretation_and_production_volume",
]

MANUFACTURERS = [
    ("Zululand Footwear Manufacturers", "safety boots"),
    ("Highveld Solar Heaters", "solar geysers"),
    ("Ndlovu School Desks", "steel-frame desks"),
    ("Protea Sportswear Factory", "tracksuit sets"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_raw_material_stock_taccount(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    open_rm = r.randint(45, 85) * 1000
    purch_rm = r.randint(210, 340) * 1000
    carriage = r.randint(12, 24) * 1000
    tot_dr = open_rm + purch_rm + carriage

    returns = r.randint(8, 16) * 1000
    close_rm = r.randint(50, 90) * 1000
    issued_wip = tot_dr - returns - close_rm

    headers = ["Raw Material Stock Account (General Ledger)", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Balance b/d (Opening stock)", "Debit", f"R{open_rm:,}"],
        ["Bank / Creditors Control (Purchases of raw materials)", "Debit", f"R{purch_rm:,}"],
        ["Bank / Creditors Control (Carriage on purchases)", "Debit", f"R{carriage:,}"],
        ["Total Debits", "Debit", "{r3_c2}"],
        ["Creditors Control (Raw materials returned to suppliers)", "Credit", f"R{returns:,}"],
        ["Work-in-Process Stock (Direct materials issued to factory)", "Credit (balancing)", "{r5_c2}"],
        ["Balance c/d (Closing stock)", "Credit", f"R{close_rm:,}"],
    ]
    correct_map = {
        "r3_c2": tot_dr,
        "r5_c2": issued_wip,
    }
    worked = (
        f"**Raw Material Stock Ledger Account ({firm})**\n\n"
        f"- **Total Debits**: `R{open_rm:,} + R{purch_rm:,} + R{carriage:,} = R{tot_dr:,}`\n"
        f"- **Direct Materials Issued to Work-in-Process Stock**: `R{tot_dr:,} - R{returns:,} - R{close_rm:,} = R{issued_wip:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "raw_material_stock_ledger_taccount",
        "question_text": f"Complete the **Raw Material Stock Account** in the General Ledger of **{firm}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Raw Material Stock is an Asset account: Opening stock, purchases, and carriage are Debited; returns, closing stock, and materials issued to Work-in-Process are Credited.",
            "Sum the debit entries first, then subtract returns and closing stock to find Work-in-Process Stock.",
            worked,
        ),
    }


def _gen_wip_stock_taccount(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    open_wip = r.randint(30, 65) * 1000
    dmc = r.randint(180, 280) * 1000
    dlc = r.randint(140, 220) * 1000
    foh = r.randint(80, 130) * 1000
    tot_dr = open_wip + dmc + dlc + foh
    close_wip = r.randint(35, 70) * 1000
    finished_goods = tot_dr - close_wip

    headers = ["Work-in-Process Stock Account (General Ledger)", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Balance b/d (Opening WIP)", "Debit", f"R{open_wip:,}"],
        ["Direct Material Cost", "Debit", f"R{dmc:,}"],
        ["Direct Labour Cost", "Debit", f"R{dlc:,}"],
        ["Factory Overhead Cost", "Debit", f"R{foh:,}"],
        ["Total Debits", "Debit", "{r4_c2}"],
        ["Finished Goods Stock (Cost of finished goods produced)", "Credit (balancing)", "{r5_c2}"],
        ["Balance c/d (Closing WIP)", "Credit", f"R{close_wip:,}"],
    ]
    correct_map = {
        "r4_c2": tot_dr,
        "r5_c2": finished_goods,
    }
    worked = (
        f"**Work-in-Process Stock Ledger Account ({firm})**\n\n"
        f"- **Total Debits**: `R{open_wip:,} + R{dmc:,} + R{dlc:,} + R{foh:,} = R{tot_dr:,}`\n"
        f"- **Transferred to Finished Goods Stock**: `R{tot_dr:,} - R{close_wip:,} = R{finished_goods:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "work_in_process_stock_ledger_taccount",
        "question_text": f"Complete the **Work-in-Process Stock Account** in the General Ledger of **{firm}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "All three manufacturing costs (Direct Material, Direct Labour, Factory Overheads) are debited to Work-in-Process Stock.",
            "Sum Opening WIP and the three production costs, then subtract Closing WIP to find the Cost of Finished Goods Produced.",
            worked,
        ),
    }


def _gen_finished_goods_stock_taccount(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    open_fg = r.randint(60, 110) * 1000
    produced = r.randint(420, 650) * 1000
    tot_avail = open_fg + produced
    close_fg = r.randint(55, 105) * 1000
    cos = tot_avail - close_fg

    headers = ["Finished Goods Stock Account (General Ledger)", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Balance b/d (Opening finished goods)", "Debit", f"R{open_fg:,}"],
        ["Work-in-Process Stock (Completed production transferred in)", "Debit", f"R{produced:,}"],
        ["Total Finished Goods Available", "Debit", "{r2_c2}"],
        ["Cost of Sales (Finished goods sold during the year)", "Credit (balancing)", "{r3_c2}"],
        ["Balance c/d (Closing finished goods)", "Credit", f"R{close_fg:,}"],
    ]
    correct_map = {
        "r2_c2": tot_avail,
        "r3_c2": cos,
    }
    worked = (
        f"**Finished Goods Stock Ledger Account ({firm})**\n\n"
        f"- **Total Available**: `R{open_fg:,} + R{produced:,} = R{tot_avail:,}`\n"
        f"- **Transferred to Cost of Sales**: `R{tot_avail:,} - R{close_fg:,} = R{cos:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "finished_goods_stock_ledger_taccount",
        "question_text": f"Complete the **Finished Goods Stock Account** in the General Ledger of **{firm}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Finished Goods Stock receives completed goods from Work-in-Process Stock (Debit) and transfers goods sold to Cost of Sales (Credit).",
            "Add Opening Finished Goods and Work-in-Process transfer, then subtract Closing Finished Goods.",
            worked,
        ),
    }


def _gen_factory_overhead_taccount(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    open_consum = r.randint(4, 8) * 1000
    purch_consum = r.randint(18, 30) * 1000
    close_consum = r.randint(5, 9) * 1000
    ind_mat_used = open_consum + purch_consum - close_consum

    ind_labour = r.randint(35, 60) * 1000
    fac_rent = r.randint(48, 72) * 1000
    fac_depr = r.randint(20, 38) * 1000
    tot_foh = ind_mat_used + ind_labour + fac_rent + fac_depr

    headers = ["Factory Overhead Cost Account (General Ledger)", "Calculation / Detail", "Amount (R)"]
    rows = [
        ["Indirect materials used", f"Opening R{open_consum:,} + Purchases R{purch_consum:,} - Closing R{close_consum:,}", "{r0_c2}"],
        ["Indirect labour (Factory foreman and cleaners)", "Transferred from Salaries & Wages", f"R{ind_labour:,}"],
        ["Factory rent and electricity", "Allocated factory portion", f"R{fac_rent:,}"],
        ["Depreciation on factory plant and machinery", "100% factory asset", f"R{fac_depr:,}"],
        ["Total transferred to Work-in-Process Stock Account", "Credit Factory Overhead / Debit WIP Stock", "{r4_c2}"],
    ]
    correct_map = {
        "r0_c2": ind_mat_used,
        "r4_c2": tot_foh,
    }
    worked = (
        f"**Factory Overhead Cost Account ({firm})**\n\n"
        f"- **Indirect Materials Used**: `R{open_consum:,} + R{purch_consum:,} - R{close_consum:,} = R{ind_mat_used:,}`\n"
        f"- **Total Transferred to Work-in-Process Stock**: `R{ind_mat_used:,} + R{ind_labour:,} + R{fac_rent:,} + R{fac_depr:,} = R{tot_foh:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "factory_overhead_cost_ledger_taccount",
        "question_text": f"Complete the **Factory Overhead Cost Account** summary for **{firm}** at year-end.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Factory Overhead Cost is closed off at year-end by transferring its total balance to the Work-in-Process Stock account.",
            "Calculate indirect materials used in Row 1, then sum all four factory overhead items for Row 5.",
            worked,
        ),
    }


def _gen_labour_ledger_allocation(r: random.Random) -> Dict[str, Any]:
    headers = ["Employee Category", "General Ledger Cost Account Debited (Direct Labour Cost / Factory Overhead Cost / Administration Cost / Selling & Distribution Cost)"]
    rows = [
        ["Wages of assembly-line workers operating factory sewing machines", "{r0_c1}"],
        ["Salary of the factory floor supervisor and factory security guard", "{r1_c1}"],
        ["Salaries of the receptionist and head office bookkeeper", "{r2_c1}"],
        ["Commission and salaries of delivery van drivers", "{r3_c1}"],
    ]
    correct_map = {
        "r0_c1": "Direct Labour Cost",
        "r1_c1": "Factory Overhead Cost",
        "r2_c1": "Administration Cost",
        "r3_c1": "Selling & Distribution Cost",
    }
    worked = (
        "**Allocating Salaries & Wages to Manufacturing Cost Accounts**\n\n"
        "- Assembly-line machine operators $\\rightarrow$ **Direct Labour Cost**\n"
        "- Factory supervisor & factory security $\\rightarrow$ **Factory Overhead Cost** (indirect factory labour)\n"
        "- Receptionist & bookkeeper $\\rightarrow$ **Administration Cost**\n"
        "- Delivery drivers & sales reps $\\rightarrow$ **Selling & Distribution Cost**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "direct_and_indirect_labour_ledger_allocation",
        "question_text": "State the **General Ledger Cost Account** to which each employee category's remuneration is transferred.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Distinguish between hands-on factory production workers (Direct Labour) and factory support staff (Factory Overhead).",
            "Enter the exact account name from the column heading for each row.",
            worked,
        ),
    }


def _gen_breakeven_calculation(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    sp = r.choice([250, 300, 400])
    vc = int(sp * 0.60)
    contrib = sp - vc
    fixed_costs = contrib * r.choice([1200, 1500, 2000])
    bep_units = fixed_costs // contrib

    headers = ["Break-Even Analysis Component", "Formula", "Answer"]
    rows = [
        [f"Selling price per unit (R{sp}) less Variable cost per unit (R{vc}) — Contribution per unit (R)", "SP per unit - VC per unit", "{r0_c2}"],
        [f"Break-Even Point in units (Total Fixed Costs = R{fixed_costs:,})", "Total Fixed Costs ÷ Contribution per unit", "{r1_c2}"],
    ]
    correct_map = {
        "r0_c2": contrib,
        "r1_c2": bep_units,
    }
    worked = (
        f"**Break-Even Point Calculation ({firm})**\n\n"
        f"- **Contribution per unit**: `R{sp} - R{vc} = R{contrib}`\n"
        f"- **Break-Even Point**: `R{fixed_costs:,} ÷ R{contrib} = {bep_units:,} units`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "contribution_per_unit_and_breakeven_units",
        "question_text": (
            f"**{firm}** sells **{product}** at **R{sp} per unit**. Variable costs are **R{vc} per unit** and "
            f"total fixed costs are **R{fixed_costs:,}**. Calculate the Contribution per unit and the Break-Even Point in units."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Contribution per unit is the amount each unit sold contributes toward covering Total Fixed Costs.",
            "Subtract Variable Cost per unit from Selling Price per unit, then divide Total Fixed Costs by that contribution.",
            worked,
        ),
    }


def _gen_breakeven_interpretation(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    bep = 2500
    actual_prod = 3200
    contrib = 120
    safety_units = actual_prod - bep
    net_profit = safety_units * contrib

    headers = ["Break-Even Evaluation Metric", "Calculation", "Answer"]
    rows = [
        [f"Units produced and sold above Break-Even ({actual_prod:,} actual vs {bep:,} break-even)", "Actual Units - Break-Even Units", "{r0_c2}"],
        [f"Net Profit earned at {actual_prod:,} units (Contribution = R{contrib} per unit)", "Units above Break-Even × Contribution per unit", "{r1_c2}"],
        ["Financial outcome (Profit / Loss / Break-Even)", "Actual units > Break-Even units", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": safety_units,
        "r1_c2": net_profit,
        "r2_c2": "Profit",
    }
    worked = (
        f"**Break-Even Interpretation ({firm})**\n\n"
        f"- **Margin of Safety (units above break-even)**: `{actual_prod:,} - {bep:,} = {safety_units:,} units`\n"
        f"- **Net Profit**: `{safety_units:,} units × R{contrib} = R{net_profit:,}` (**Profit**)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "breakeven_interpretation_and_production_volume",
        "question_text": (
            f"**{firm}** has a break-even point of **{bep:,} units** and a contribution of **R{contrib} per unit**. "
            f"During the year, the factory produced and sold **{actual_prod:,} units**. Complete the evaluation table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Every unit sold above the Break-Even Point generates pure Net Profit equal to the Contribution per unit.",
            "Subtract Break-Even units from Actual units, then multiply by R120.",
            worked,
        ),
    }


_BUILDERS = {
    "raw_material_stock_ledger_taccount": _gen_raw_material_stock_taccount,
    "work_in_process_stock_ledger_taccount": _gen_wip_stock_taccount,
    "finished_goods_stock_ledger_taccount": _gen_finished_goods_stock_taccount,
    "factory_overhead_cost_ledger_taccount": _gen_factory_overhead_taccount,
    "direct_and_indirect_labour_ledger_allocation": _gen_labour_ledger_allocation,
    "contribution_per_unit_and_breakeven_units": _gen_breakeven_calculation,
    "breakeven_interpretation_and_production_volume": _gen_breakeven_interpretation,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Cost accounting"
        q["grade"] = "11"
        out.append(q)
    return out
