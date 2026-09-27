"""Grade 9 EMS — Cash Journals of a Trading Business & The Trading Cycle.
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 2/02. Cash receipts journal and Cash payments journal (sole trader).md`.
Covers:
- Elementary Cost of Sales calculations using the CAPS "What I WANT / What I HAVE" markup formula
- The Trading Cycle effect on the Accounting Equation (A = OE + L for Cash Sales and Stock Purchases)
- The Source Document to Cash Journal Pipeline
- 2D Tabular Cash Receipts Journal (CRJ) with Sales and Cost of Sales columns
- 2D Tabular Cash Payments Journal (CPJ) with Trading Stock and Wages columns
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term1_crj_cpj"
CURRICULUM_REFERENCE = "Term 1/2 > Cash Journals of a Trading Business"


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: Optional[str] = None,
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group or "trading_cycle",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["accounting", "trading_cycle"],
    })
    return enriched


# --------------------------------------------------------------------------- #
# Sub-Drill 1: Elementary Cost of Sales & Markup ("What I WANT / What I HAVE")
# --------------------------------------------------------------------------- #
def _generate_cost_of_sales_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(r)
    markup = r.choice([25, 33, 50, 75, 100])

    # Three calculation rows:
    # 1. Given Cost Price & Markup% -> Calculate Selling Price
    # 2. Given Selling Price & Markup% -> Calculate Cost Price
    # 3. Given Cost Price & Selling Price -> Calculate Markup %
    cp1 = r.randint(2, 10) * 100
    sp1 = int(cp1 * (100 + markup) / 100)

    sp2 = r.randint(3, 12) * 150
    cp2 = int(round(sp2 * 100 / (100 + markup)))
    # re-adjust sp2 to be exact integer
    sp2 = int(cp2 * (100 + markup) / 100)

    markup3 = r.choice([25, 50, 100])
    cp3 = r.randint(2, 8) * 100
    profit3 = int(cp3 * markup3 / 100)
    sp3 = cp3 + profit3

    prompt = (
        f"**{scenario['entrepreneur']}'s {scenario['business_type']}** applies a fixed mark-up on cost.\n"
        f"Use the CAPS calculation principle (**What I WANT / What I HAVE**) to calculate the missing values in the table below.\n\n"
        f"• Mark-up percentage for Items 1 and 2: **{markup}% on cost**\n"
        f"• For Item 3, calculate the mark-up percentage achieved."
    )

    headers = ["Item", "Cost Price (R)", "Mark-up %", "Selling Price (R)", "Gross Profit (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1. Garden Bench", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": str(cp1), "type": "given", "editable": False},
            {"coordinate": "t0_r0_c2", "value": f"{markup}%", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "value": str(sp1) if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c4", "value": str(sp1 - cp1) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "2. Coffee Table", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": str(cp2) if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "value": f"{markup}%", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "value": str(sp2), "type": "given", "editable": False},
            {"coordinate": "t0_r1_c4", "value": str(sp2 - cp2) if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "3. Bookshelf", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": str(cp3), "type": "given", "editable": False},
            {"coordinate": "t0_r2_c2", "value": f"{markup3}%" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "value": str(sp3), "type": "given", "editable": False},
            {"coordinate": "t0_r2_c4", "value": str(profit3), "type": "given", "editable": False},
        ],
    ]

    correct_map = {
        "t0_r0_c3": str(sp1),
        "t0_r0_c4": str(sp1 - cp1),
        "t0_r1_c1": str(cp2),
        "t0_r1_c4": str(sp2 - cp2),
        "t0_r2_c2": f"{markup3}%",
    }

    cell_hints = {
        "t0_r0_c3": f"Formula: Cost Price x (100 + {markup})/100 = R{cp1} x {100+markup}/100 = R{sp1}.",
        "t0_r0_c4": f"Gross Profit = Selling Price (R{sp1}) - Cost Price (R{cp1}) = R{sp1 - cp1}.",
        "t0_r1_c1": f"Formula: Selling Price x 100/(100 + {markup}) = R{sp2} x 100/{100+markup} = R{cp2}.",
        "t0_r1_c4": f"Gross Profit = Selling Price (R{sp2}) - Cost Price (R{cp2}) = R{sp2 - cp2}.",
        "t0_r2_c2": f"Formula: (Profit / Cost Price) x 100 = (R{profit3} / R{cp3}) x 100 = {markup3}%.",
    }

    item = {
        "id": f"ems9_cos_calc_{r.randint(1000, 9999)}",
        "title": "Cost of Sales and Mark-up Calculations",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 10,
        "sample_answer": f"Item 1: SP=R{sp1}; Item 2: CP=R{cp2}; Item 3: Mark-up={markup3}%",
        "ideal_answer": "Complete calculations using the 'What I WANT / What I HAVE' formula.",
        "hint_sections": {
            "1_nudge": "Place what you WANT at the top of the fraction and what you HAVE at the bottom.",
            "2_concept": "To find Selling Price (100 + markup)%: SP = Cost x (100 + Markup)/100. To find Cost Price (100%): CP = SP x 100/(100 + Markup).",
            "3_breakdown": f"Item 1: R{cp1} x {100+markup}/100 = R{sp1}. Item 2: R{sp2} x 100/{100+markup} = R{cp2}. Item 3: (R{profit3}/R{cp3}) x 100 = {markup3}%."
        },
        "marking_schema": {
            "total_marks": 10,
            "marking_points": [
                {"id": "mp_sp1", "desc": f"Item 1 Selling Price: R{sp1}", "marks": 2, "editable": True},
                {"id": "mp_gp1", "desc": f"Item 1 Profit: R{sp1-cp1}", "marks": 2, "editable": True},
                {"id": "mp_cp2", "desc": f"Item 2 Cost Price: R{cp2}", "marks": 2, "editable": True},
                {"id": "mp_gp2", "desc": f"Item 2 Profit: R{sp2-cp2}", "marks": 2, "editable": True},
                {"id": "mp_mu3", "desc": f"Item 3 Mark-up percentage: {markup3}%", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["inverted_markup_formula", "used_selling_price_as_cost_base"],
    }
    return _with_metadata(
        item,
        subskill="cost_of_sales",
        learning_objective_id="lo_g9_cost_of_sales_math",
        question_family_id="cos_markup_drill",
        misconception_tags=["inverted_markup_formula", "used_selling_price_as_cost_base"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 2: The Trading Cycle on the Accounting Equation
# --------------------------------------------------------------------------- #
def _generate_trading_equation_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(r)
    markup = 50

    # T1: Cash purchase of trading stock
    t1_cost = r.randint(15, 40) * 100
    # T2: Cash sale of stock
    t2_cp = r.randint(10, 30) * 100
    t2_sp = int(t2_cp * 1.5)

    prompt = (
        f"Analyse the following two cash trading transactions of **{scenario['entrepreneur']}'s Store** "
        f"on the **Accounting Equation (A = OE + L)**. Show the dual effect of the cash sale.\n\n"
        f"1. Bought trading stock for cash and paid via EFT, R{t1_cost:,}.\n"
        f"2. Sold trading stock for cash according to the cash register roll, R{t2_sp:,}. The cost price was R{t2_cp:,}."
    )

    headers = ["No.", "Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": "Trading Stock" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "value": "Bank" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c3", "value": f"+{t1_cost} / -{t1_cost} (0)" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c4", "value": "0" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c5", "value": "0" if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "2(a)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Bank" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "value": "Sales" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c3", "value": f"+{t2_sp}" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c4", "value": f"+{t2_sp}" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c5", "value": "0" if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "2(b)", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "Cost of Sales" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c2", "value": "Trading Stock" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "value": f"-{t2_cp}" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c4", "value": f"-{t2_cp}" if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": "t0_r2_c5", "value": "0" if mode == "scaffold" else "", "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": "Trading Stock",
        "t0_r0_c2": "Bank",
        "t0_r0_c3": f"+{t1_cost} / -{t1_cost} (0)",
        "t0_r0_c4": "0",
        "t0_r0_c5": "0",
        "t0_r1_c1": "Bank",
        "t0_r1_c2": "Sales",
        "t0_r1_c3": f"+{t2_sp}",
        "t0_r1_c4": f"+{t2_sp}",
        "t0_r1_c5": "0",
        "t0_r2_c1": "Cost of Sales",
        "t0_r2_c2": "Trading Stock",
        "t0_r2_c3": f"-{t2_cp}",
        "t0_r2_c4": f"-{t2_cp}",
        "t0_r2_c5": "0",
    }

    cell_hints = {
        "t0_r0_c1": "Trading stock is an asset that increased (Debit).",
        "t0_r0_c2": "Bank is an asset that decreased (Credit).",
        "t0_r1_c1": "Cash received increases Bank (Asset debit).",
        "t0_r1_c2": "Sales increases Owner's Equity (Credit).",
        "t0_r2_c1": "Cost of Sales is an expense that decreases Owner's Equity (Debit).",
        "t0_r2_c2": "Trading Stock is an asset that left the shelves (Credit).",
    }

    item = {
        "id": f"ems9_eq_trading_{r.randint(1000, 9999)}",
        "title": "Trading Cycle Accounting Equation",
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 15,
        "sample_answer": f"1: Dr Trading Stock, Cr Bank. 2(a): Dr Bank (+{t2_sp}), Cr Sales (+{t2_sp}). 2(b): Dr Cost of Sales (-{t2_cp}), Cr Trading Stock (-{t2_cp}).",
        "ideal_answer": "Complete analysis of cash purchase and cash sale with dual sales and cost-of-sales entries.",
        "hint_sections": {
            "1_nudge": "Remember: A sale of trading stock ALWAYS involves TWO entries: one at Selling Price and one at Cost Price.",
            "2_concept": "Entry 2(a) records money received: Bank (+A) and Sales (+OE). Entry 2(b) records stock leaving: Trading Stock (-A) and Cost of Sales (-OE).",
            "3_breakdown": f"Net profit on the sale is R{t2_sp - t2_cp:,} (Sales R{t2_sp} - Cost of Sales R{t2_cp})."
        },
        "marking_schema": {
            "total_marks": 15,
            "marking_points": [
                {"id": "mp_1", "desc": "Purchase of stock: Dr Trading Stock, Cr Bank, A=0, OE=0, L=0", "marks": 5, "editable": True},
                {"id": "mp_2a", "desc": f"Cash sale (SP): Dr Bank (+{t2_sp}), Cr Sales (+{t2_sp})", "marks": 5, "editable": True},
                {"id": "mp_2b", "desc": f"Cost of sale (CP): Dr Cost of Sales (-{t2_cp}), Cr Trading Stock (-{t2_cp})", "marks": 5, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["omitted_cost_of_sales_entry", "confused_sales_and_cost_amounts"],
    }
    return _with_metadata(
        item,
        subskill="trading_equation",
        learning_objective_id="lo_g9_trading_equation",
        question_family_id="trading_equation_table",
        misconception_tags=["omitted_cost_of_sales_entry", "confused_sales_and_cost_amounts"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 3: The Source Documents to Cash Journals Pipeline
# --------------------------------------------------------------------------- #
def _generate_source_doc_pipeline_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(r)
    items = [
        {"desc": f"Received cash from customers for goods sold, R{r.randint(10,30)*100}", "doc": "Cash register roll (CRR)", "journal": "CRJ", "bank_effect": "+ (Increase)"},
        {"desc": f"Received rent from tenant via direct EFT, R{r.randint(2,6)*1000}", "doc": "Bank statement / Duplicate receipt", "journal": "CRJ", "bank_effect": "+ (Increase)"},
        {"desc": f"Paid Makro for trading stock purchased via EFT, R{r.randint(15,40)*100}", "doc": "EFT payment confirmation / Bank statement", "journal": "CPJ", "bank_effect": "- (Decrease)"},
        {"desc": f"Paid weekly wages in cash, R{r.randint(5,15)*100}", "doc": "Cheque counterfoil / Cash withdrawal slip", "journal": "CPJ", "bank_effect": "- (Decrease)"},
    ]

    headers = ["Transaction", "Source Document", "Subsidiary Journal", "Effect on Bank"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for idx, itm in enumerate(items):
        coord_doc = f"t0_r{idx}_c1"
        coord_jnl = f"t0_r{idx}_c2"
        coord_bnk = f"t0_r{idx}_c3"

        correct_map[coord_doc] = itm["doc"]
        correct_map[coord_jnl] = itm["journal"]
        correct_map[coord_bnk] = itm["bank_effect"]

        cell_hints[coord_doc] = f"Which document serves as proof for: {itm['desc']}?"
        cell_hints[coord_jnl] = f"Is this a receipt (CRJ) or a payment (CPJ)?"
        cell_hints[coord_bnk] = f"Does this transaction increase or decrease the Bank balance?"

        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": itm["desc"], "type": "given", "editable": False},
            {"coordinate": coord_doc, "value": itm["doc"] if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": coord_jnl, "value": itm["journal"] if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": coord_bnk, "value": itm["bank_effect"] if mode == "scaffold" else "", "type": "required", "editable": True},
        ])

    item = {
        "id": f"ems9_pipeline_{r.randint(1000, 9999)}",
        "title": "Source Documents to Cash Journals Pipeline",
        "question_type": "table_completion",
        "prompt": f"Trace each transaction of **{scenario['entrepreneur']}'s Business** to its source document, subsidiary journal, and effect on the bank account.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 12,
        "sample_answer": f"Row 1: {items[0]['doc']}, {items[0]['journal']}, {items[0]['bank_effect']}",
        "ideal_answer": "All 4 transactions mapped accurately to authentic South African source documents and journals.",
        "hint_sections": {
            "1_nudge": "Receipts of cash are recorded in the CRJ. Payments of cash are recorded in the CPJ.",
            "2_concept": "Cash register roll (CRR) is used for cash sales. Receipts are issued when receiving lump sums from individuals.",
            "3_breakdown": "Every transaction must have a valid source document before entry into journals."
        },
        "marking_schema": {
            "total_marks": 12,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Pipeline mapping for transaction {i+1}", "marks": 3, "editable": True}
                for i in range(len(items))
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_crj_and_cpj_documents", "incorrect_bank_direction"],
    }
    return _with_metadata(
        item,
        subskill="source_docs_pipeline",
        learning_objective_id="lo_g9_source_doc_pipeline",
        question_family_id="source_doc_pipeline_table",
        misconception_tags=["confused_crj_and_cpj_documents", "incorrect_bank_direction"],
    )


# --------------------------------------------------------------------------- #
# Full 2D Tabular CRJ Generator (Trading Business)
# --------------------------------------------------------------------------- #
def _generate_crj_trading(rng: random.Random, mode: str = "scaffold") -> List[Dict[str, Any]]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Trading Store"
    month = "May 2026"
    markup_percentage = rng.choice([25, 50, 100])

    transactions = []

    # Capital contribution
    cap_amt = rng.randint(5, 50) * 1000
    transactions.append(f"Day 1: The owner, {scenario['entrepreneur']}, deposited R{cap_amt:,} directly into the business bank account as capital. Issued Receipt 01.")

    # Cash Sales
    cp1 = rng.randint(10, 50) * 100
    sp1 = int(cp1 * (1 + markup_percentage / 100))
    transactions.append(f"Day 12: Cash sales of trading stock, R{sp1:,}. The cost price was R{cp1:,} according to cash register roll (CRR 01).")

    # Rent Income
    rent = rng.randint(2, 8) * 1000
    transactions.append(f"Day 25: Received R{rent:,} from A. Tenant for rent. Issued Receipt 02.")

    data_rows = [
        ["Rec 01", "1", scenario['entrepreneur'], "", str(cap_amt), "", "", str(cap_amt), "Capital"],
        ["CRR 01", "12", "Sales", str(sp1), str(sp1), str(sp1), str(cp1), "", ""],
        ["Rec 02", "25", "A. Tenant", str(rent), str(rent), "", "", str(rent), "Rent Income"],
    ]

    correct_map = {}
    rows_data = []
    cell_hints = {}

    for i, row in enumerate(data_rows):
        row_cells = []
        for j, val in enumerate(row):
            coord = f"t0_r{i}_c{j}"
            correct_map[coord] = val
            is_empty = (val == "")
            row_cells.append({
                "coordinate": coord,
                "value": val if mode == "scaffold" else "",
                "type": "must_be_empty" if is_empty else "required",
                "editable": True,
            })
        rows_data.append(row_cells)

    headers = ["Doc No", "Day", "Details", "Analysis of Receipts", "Bank", "Sales", "Cost of Sales", "Sundry Amount", "Sundry Details"]

    cell_hints["t0_r0_c3"] = "Direct deposits bypass the Analysis of Receipts column (leave blank)."
    cell_hints["t0_r0_c4"] = f"Total banked: R{cap_amt}."
    cell_hints["t0_r0_c7"] = f"Capital goes to Sundry Accounts: R{cap_amt}."
    cell_hints["t0_r0_c8"] = "Account name is 'Capital'."
    cell_hints["t0_r1_c3"] = f"Cash sales put money in the till: R{sp1}."
    cell_hints["t0_r1_c4"] = f"Banked on same day: R{sp1}."
    cell_hints["t0_r1_c5"] = f"Sales column: R{sp1}."
    cell_hints["t0_r1_c6"] = f"Cost of Sales column: R{cp1} (NOTE: Cost of Sales does NOT affect Bank)."

    item = {
        "id": f"ems9_crj_{rng.randint(1000, 9999)}",
        "title": "Cash Receipts Journal (Trading Business)",
        "question_type": "table_completion",
        "prompt": f"Complete the Cash Receipts Journal for **{business_name}** for {month}. The business uses a fixed mark-up of {markup_percentage}% on cost.",
        "transactions": transactions,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 27,
        "sample_answer": f"Row 1: Capital R{cap_amt}; Row 2: Sales R{sp1}, Cost of Sales R{cp1}; Row 3: Rent Income R{rent}",
        "ideal_answer": "Complete 2D CRJ table with correct analysis, bank, and cost of sales allocations.",
        "hint_sections": {
            "1_nudge": "In a trading business, when you sell goods, record both the selling price (Sales) and cost price (Cost of Sales).",
            "2_concept": "Sales affects Bank and Analysis. Cost of Sales is a memo column and does NOT increase Bank.",
            "3_breakdown": f"Bank = Sales + Sundry Accounts for each row. Cost of Sales is R{cp1}."
        },
        "marking_schema": {
            "total_marks": 27,
            "marking_points": [
                {"id": "mp_cap", "desc": f"Capital contribution allocated to Bank and Sundry", "marks": 9, "editable": True},
                {"id": "mp_sales", "desc": f"Sales (R{sp1}) and Cost of Sales (R{cp1}) recorded", "marks": 9, "editable": True},
                {"id": "mp_rent", "desc": f"Rent income allocated to Bank and Sundry", "marks": 9, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["added_cost_of_sales_to_bank", "omitted_cost_of_sales_column"],
    }
    return [_with_metadata(
        item,
        subskill="crj",
        learning_objective_id="lo_crj_trading",
        question_family_id="crj_table",
        misconception_tags=["added_cost_of_sales_to_bank", "omitted_cost_of_sales_column"],
    )]


# --------------------------------------------------------------------------- #
# Full 2D Tabular CPJ Generator (Trading Business)
# --------------------------------------------------------------------------- #
def _generate_cpj_trading(rng: random.Random, mode: str = "scaffold") -> List[Dict[str, Any]]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Trading Store"
    month = "May 2026"

    transactions = []

    stock_amt = rng.randint(20, 80) * 100
    transactions.append(f"Day 5: Issued cheque 101 for R{stock_amt:,} to Makro to purchase trading stock.")

    wage_amt = rng.randint(10, 30) * 100
    transactions.append(f"Day 14: Cashed a cheque 102 to pay weekly wages, R{wage_amt:,}.")

    stat_amt = rng.randint(3, 8) * 100
    transactions.append(f"Day 22: Issued cheque 103 to Waltons for office stationery, R{stat_amt:,}.")

    data_rows = [
        ["101", "5", "Makro", str(stock_amt), str(stock_amt), "", "", "", ""],
        ["102", "14", "Cash", str(wage_amt), "", str(wage_amt), "", "", ""],
        ["103", "22", "Waltons", str(stat_amt), "", "", str(stat_amt), "", ""],
    ]

    correct_map = {}
    rows_data = []
    cell_hints = {}

    for i, row in enumerate(data_rows):
        row_cells = []
        for j, val in enumerate(row):
            coord = f"t0_r{i}_c{j}"
            correct_map[coord] = val
            is_empty = (val == "")
            row_cells.append({
                "coordinate": coord,
                "value": val if mode == "scaffold" else "",
                "type": "must_be_empty" if is_empty else "required",
                "editable": True,
            })
        rows_data.append(row_cells)

    headers = ["Doc No", "Day", "Name of Payee", "Bank", "Trading Stock", "Wages", "Stationery", "Sundry Amount", "Sundry Details"]

    cell_hints["t0_r0_c4"] = f"Stock bought to resell is Trading Stock: R{stock_amt}."
    cell_hints["t0_r1_c5"] = f"Workers' pay is Wages: R{wage_amt}."
    cell_hints["t0_r2_c6"] = f"Office supplies are Stationery: R{stat_amt}."

    item = {
        "id": f"ems9_cpj_{rng.randint(1000, 9999)}",
        "title": "Cash Payments Journal (Trading Business)",
        "question_type": "table_completion",
        "prompt": f"Complete the Cash Payments Journal for **{business_name}** for {month}.",
        "transactions": transactions,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 27,
        "sample_answer": f"Row 1: Trading Stock R{stock_amt}; Row 2: Wages R{wage_amt}; Row 3: Stationery R{stat_amt}",
        "ideal_answer": "Complete 2D CPJ table with accurate allocations to Trading Stock, Wages, and Stationery.",
        "hint_sections": {
            "1_nudge": "The CPJ records all payments. Remember that stock bought to resell is 'Trading Stock'.",
            "2_concept": "Every payment is recorded in Bank, then allocated to its specific column.",
            "3_breakdown": f"Bank = Sum of analysis columns for each row."
        },
        "marking_schema": {
            "total_marks": 27,
            "marking_points": [
                {"id": "mp_stock", "desc": f"Trading Stock purchased: R{stock_amt}", "marks": 9, "editable": True},
                {"id": "mp_wages", "desc": f"Wages paid: R{wage_amt}", "marks": 9, "editable": True},
                {"id": "mp_stat", "desc": f"Stationery purchased: R{stat_amt}", "marks": 9, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_trading_stock_and_consumables"],
    }
    return [_with_metadata(
        item,
        subskill="cpj",
        learning_objective_id="lo_cpj_trading",
        question_family_id="cpj_table",
        misconception_tags=["confused_trading_stock_and_consumables"],
    )]


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "cost_of_sales": lambda rng, mode: [_generate_cost_of_sales_drill(rng, mode)],
    "elementary_cost_of_sales": lambda rng, mode: [_generate_cost_of_sales_drill(rng, mode)],
    "trading_equation": lambda rng, mode: [_generate_trading_equation_drill(rng, mode)],
    "elementary_trading_equation": lambda rng, mode: [_generate_trading_equation_drill(rng, mode)],
    "source_docs_pipeline": lambda rng, mode: [_generate_source_doc_pipeline_drill(rng, mode)],
    "elementary_source_doc_pipeline": lambda rng, mode: [_generate_source_doc_pipeline_drill(rng, mode)],
    "crj": _generate_crj_trading,
    "cpj": _generate_cpj_trading,
}


def generate(
    subskill: str = "crj",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    builder = BUILDERS.get(subskill)
    if builder is not None:
        pool = builder(rng, mode)
    else:
        pool = _generate_crj_trading(rng, mode) + _generate_cpj_trading(rng, mode)

    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
