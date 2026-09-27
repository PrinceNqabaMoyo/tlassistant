"""Grade 11 Accounting — Inventory Valuation (FIFO & Weighted Average).
100% Deterministic Python generator aligned with CAPS Term 1 & Term 4 syllabus.
Covers:
- Exam Ceiling (mode="compound" - 12 marks):
  * First-In-First-Out (FIFO) and Weighted Average inventory valuation methods for trading businesses.
  * Purchases batches across months with varying unit costs and carriage on purchases.
  * Calculations:
    - Value of closing inventory under FIFO and Weighted Average.
    - Cost of Sales (Opening Stock + Purchases + Carriage - Closing Stock).
    - Gross Profit on sales.
  * Qualitative analysis & comparison: Effect of FIFO vs Weighted Average on net profit and income tax liability
    during inflationary periods, and IFRS/GAAP consistency principles.
  * 2D tabular matrix with cell coordinates `t0_r{rix}_c{cix}`, cell types (`required`, `given`, `must_be_empty`),
    `correct_map`, and cell hints.
  * Deduction rules: `{"rule": "must_be_empty_filled", "penalty": -1}`.
  * Misconception tags: `allocated_carriage_incorrectly`, `used_oldest_stock_for_fifo_closing`,
    `omitted_opening_stock_in_weighted_avg`, `simple_average_instead_of_weighted_average`.
- Adaptive Scaffolding Sub-drills (3-4 marks each):
  * `elementary_fifo_closing_stock`: Calculating closing stock value by layering newest batches.
  * `elementary_weighted_avg_unit_cost`: Calculating weighted average cost per unit including carriage on purchases.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

try:
    from ..sa_naming_engine import generate_sa_enterprise, pick_surname
except ImportError:
    from app.utils.sa_naming_engine import generate_sa_enterprise, pick_surname


MISCONCEPTION_CARRIAGE = "allocated_carriage_incorrectly"
MISCONCEPTION_FIFO_OLDEST = "used_oldest_stock_for_fifo_closing"
MISCONCEPTION_OMITTED_OPENING = "omitted_opening_stock_in_weighted_avg"
MISCONCEPTION_SIMPLE_AVG = "simple_average_instead_of_weighted_average"


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_money(val: float | int) -> str:
    """Format an integer/float amount with thousand separators."""
    if isinstance(val, (int, float)) and float(val).is_integer():
        ival = int(round(float(val)))
        return f"{ival:,}".replace(",", " ")
    return f"{float(val):,.2f}".replace(",", " ").replace(".", ",")


def _format_sa_curr(val: float | int) -> str:
    """Format currency for display."""
    return f"R{_fmt_money(val)}"


# ============================================================================
# SUB-DRILL 1: Elementary FIFO Closing Stock Layering
# ============================================================================
def _build_elementary_fifo_closing_stock(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Khumalo Sportswear", "Lekganyane Footwear", "Protea Outfitters", "Mthembu Retailers"])
    product = r.choice(["hiking boots", "running shoes", "winter jackets", "school bags"])

    # Batches (earliest to latest)
    cost_batch1 = r.choice([120, 140, 160])
    cost_batch2 = cost_batch1 + r.choice([15, 20, 25])
    cost_batch3 = cost_batch2 + r.choice([15, 20, 25])  # Latest batch (rising prices)

    qty_batch3 = r.choice([80, 100, 120])
    qty_batch2 = r.choice([100, 150, 160])

    # Closing stock units: spans the latest batch and part of the previous batch
    excess_needed = r.choice([20, 30, 40, 50])
    closing_units = qty_batch3 + excess_needed

    val_layer1 = qty_batch3 * cost_batch3
    val_layer2 = excess_needed * cost_batch2
    total_fifo_val = val_layer1 + val_layer2

    prompt = (
        f"**{business}** trades in {product} and applies the **First-In-First-Out (FIFO)** method of inventory valuation "
        f"under the periodic inventory system. A physical stock count on 28 February 2026 revealed **{closing_units} units** on hand.\n\n"
        f"**Recent purchase records for the year:**\n"
        f"• 15 October 2025: {qty_batch2} units @ R{cost_batch2} each\n"
        f"• 20 January 2026 (Latest purchase): {qty_batch3} units @ R{cost_batch3} each\n\n"
        f"**Required:**\n"
        f"Calculate the value of the closing inventory on 28 February 2026 using the FIFO method. "
        f"Show the calculation for each inventory layer."
    )

    sample_answer = (
        f"Under FIFO, closing inventory consists of the most recently purchased batches:\n"
        f"1. January batch: {qty_batch3} units × R{cost_batch3} = R{_fmt_money(val_layer1)}\n"
        f"2. October batch: {excess_needed} units ({closing_units} – {qty_batch3}) × R{cost_batch2} = R{_fmt_money(val_layer2)}\n"
        f"Total FIFO Closing Stock Value = R{_fmt_money(val_layer1)} + R{_fmt_money(val_layer2)} = R{_fmt_money(total_fifo_val)}"
    )

    marking_points = [
        {"id": "mp1", "desc": f"January layer: {qty_batch3} units × R{cost_batch3} = R{_fmt_money(val_layer1)}", "marks": 1, "editable": True},
        {"id": "mp2", "desc": f"October layer: {excess_needed} units × R{cost_batch2} = R{_fmt_money(val_layer2)}", "marks": 1, "editable": True},
        {"id": "mp3", "desc": f"Total FIFO closing inventory value: R{_fmt_money(total_fifo_val)}", "marks": 1, "editable": True},
    ]

    return {
        "id": f"acc11_inv_fifo_{r.randint(100000, 999999)}",
        "title": "FIFO Closing Inventory Layering",
        "topic": "Inventory Valuation",
        "subskill": "elementary_fifo_closing_stock",
        "mode": "elementary_fifo_closing_stock",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "question_type": "calc",
        "ideal_answer": f"R{_fmt_money(total_fifo_val)}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": [MISCONCEPTION_FIFO_OLDEST, "incorrect_layer_quantities"],
        "correct_map": {"fifo_closing_inventory_value": str(total_fifo_val)},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": marking_points,
            "deductions": [
                {"rule": "used_oldest_stock_for_fifo_closing", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Under FIFO, goods purchased first are sold first, so closing stock comes from the newest purchases.",
            "tier2_directional_rule": (
                f"Take the entire newest batch ({qty_batch3} units @ R{cost_batch3}). "
                f"Take the remaining {excess_needed} units from the preceding batch @ R{cost_batch2}."
            ),
            "tier3_worked_step": sample_answer,
        },
    }


# ============================================================================
# SUB-DRILL 2: Elementary Weighted Average Unit Cost (with Carriage)
# ============================================================================
def _build_elementary_weighted_avg_unit_cost(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Sizwe Tech", "Ubuntu Electronics", "Bafana Hardware", "Zenith Traders"])
    product = r.choice(["solar lanterns", "inverters", "power tools", "router modems"])

    # Clean integers
    open_units = r.choice([100, 150, 200])
    open_cost = r.choice([60, 70, 80])
    open_val = open_units * open_cost

    purch_units = r.choice([300, 400, 500])
    purch_cost = open_cost + r.choice([10, 15, 20])
    purch_val = purch_units * purch_cost

    # Carriage on purchases
    carriage_per_purch_unit = r.choice([4, 5, 6])
    carriage_total = purch_units * carriage_per_purch_unit

    total_units = open_units + purch_units
    total_cost = open_val + purch_val + carriage_total

    # Ensure clean weighted average
    wavg_unit_cost = round(total_cost / total_units, 2)
    # Simple unweighted average for distractor comparison
    simple_avg = round((open_cost + purch_cost) / 2.0, 2)

    prompt = (
        f"**{business}** sells {product} and uses the **Weighted Average** method of inventory valuation.\n\n"
        f"**Stock and purchase details for the financial year:**\n"
        f"• Opening stock (1 March 2025): {open_units} units @ R{open_cost} each = R{_fmt_money(open_val)}\n"
        f"• Purchases during the year: {purch_units} units @ R{purch_cost} each = R{_fmt_money(purch_val)}\n"
        f"• Carriage on purchases paid: R{_fmt_money(carriage_total)}\n\n"
        f"**Required:**\n"
        f"Calculate the **Weighted Average cost per unit** at the end of the financial year. "
        f"Show the formula and full substitution."
    )

    sample_answer = (
        f"Weighted Average Cost per unit Formula:\n"
        f"= (Opening Stock Value + Purchases + Carriage on Purchases) / (Opening Stock Units + Purchases Units)\n"
        f"= (R{_fmt_money(open_val)} + R{_fmt_money(purch_val)} + R{_fmt_money(carriage_total)}) / ({open_units} + {purch_units})\n"
        f"= R{_fmt_money(total_cost)} / {total_units} units\n"
        f"= R{_fmt_money(wavg_unit_cost)} per unit"
    )

    marking_points = [
        {"id": "mp1", "desc": f"Total cost of stock available (including carriage): R{_fmt_money(total_cost)}", "marks": 1, "editable": True},
        {"id": "mp2", "desc": f"Total units available for sale: {total_units} units", "marks": 1, "editable": True},
        {"id": "mp3", "desc": f"Weighted average cost per unit: R{_fmt_money(wavg_unit_cost)}", "marks": 1, "editable": True},
    ]

    return {
        "id": f"acc11_inv_wavg_{r.randint(100000, 999999)}",
        "title": "Weighted Average Unit Cost with Carriage on Purchases",
        "topic": "Inventory Valuation",
        "subskill": "elementary_weighted_avg_unit_cost",
        "mode": "elementary_weighted_avg_unit_cost",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "question_type": "calc",
        "ideal_answer": f"R{_fmt_money(wavg_unit_cost)} per unit",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": [
            MISCONCEPTION_CARRIAGE,
            MISCONCEPTION_OMITTED_OPENING,
            MISCONCEPTION_SIMPLE_AVG,
        ],
        "correct_map": {"weighted_avg_unit_cost": str(wavg_unit_cost)},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": marking_points,
            "deductions": [
                {"rule": "omitted_carriage_on_purchases", "penalty": -1},
                {"rule": "calculated_simple_average", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Add carriage on purchases to the cost of purchases in the numerator.",
            "tier2_directional_rule": (
                "Weighted Average Cost = Total Cost of Goods Available (Opening + Purchases + Carriage) / Total Units Available."
            ),
            "tier3_worked_step": sample_answer,
        },
    }


# ============================================================================
# EXAM CEILING (mode="compound" - 12 Marks): Comprehensive Valuation & Theory
# ============================================================================
def _build_compound_inventory_valuation(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Khumalo Footwear", "Protea Outdoor Equipment", "Lekganyane Solar Supplies", "Dlamini Electronics"])
    product = r.choice(["hiking boots", "solar inverters", "running shoes", "tablets"])
    fin_year_end = "28 February 2026"

    # 1. Opening stock
    open_units = 100
    open_unit_cost = r.choice([140, 150, 160])
    open_val = open_units * open_unit_cost

    # 2. Purchases across 3 batches with rising prices (inflation)
    # Batch 1 (May)
    b1_units = 300
    b1_price = open_unit_cost + 20
    b1_carriage_unit = 10
    b1_effective_unit = b1_price + b1_carriage_unit
    b1_total_cost = b1_units * b1_effective_unit

    # Batch 2 (September)
    b2_units = 400
    b2_price = b1_price + 20
    b2_carriage_unit = 10
    b2_effective_unit = b2_price + b2_carriage_unit
    b2_total_cost = b2_units * b2_effective_unit

    # Batch 3 (January - Latest)
    b3_units = 200
    b3_price = b2_price + 20
    b3_carriage_unit = 10
    b3_effective_unit = b3_price + b3_carriage_unit
    b3_total_cost = b3_units * b3_effective_unit

    total_purch_units = b1_units + b2_units + b3_units  # 900
    total_purch_cost_excl_carriage = (b1_units * b1_price) + (b2_units * b2_price) + (b3_units * b3_price)
    total_carriage = (b1_units * b1_carriage_unit) + (b2_units * b2_carriage_unit) + (b3_units * b3_carriage_unit)
    total_purch_cost_incl_carriage = total_purch_cost_excl_carriage + total_carriage

    # Total goods available
    total_available_units = open_units + total_purch_units  # 1 000 units
    total_available_cost = open_val + total_purch_cost_incl_carriage

    # 3. Weighted Average Unit Cost (exact integer division)
    wavg_unit_cost = round(total_available_cost / total_available_units, 2)

    # 4. Closing inventory units on hand
    closing_units = r.choice([240, 250, 260])

    # 5. FIFO Closing Inventory Calculation
    # Latest batch (Batch 3) has 200 units @ b3_effective_unit
    fifo_layer1_units = b3_units  # 200
    fifo_layer1_val = fifo_layer1_units * b3_effective_unit
    fifo_layer2_units = closing_units - fifo_layer1_units  # 40 to 60 units from Batch 2
    fifo_layer2_val = fifo_layer2_units * b2_effective_unit
    fifo_closing_stock = fifo_layer1_val + fifo_layer2_val

    # 6. Weighted Average Closing Inventory Calculation
    wavg_closing_stock = int(round(closing_units * wavg_unit_cost))

    # 7. Sales & Selling Price
    units_sold = total_available_units - closing_units
    selling_price_per_unit = b3_effective_unit + r.choice([80, 100, 120])
    sales_revenue = units_sold * selling_price_per_unit

    # 8. Cost of Sales & Gross Profit
    fifo_cos = total_available_cost - fifo_closing_stock
    fifo_gp = sales_revenue - fifo_cos

    wavg_cos = total_available_cost - wavg_closing_stock
    wavg_gp = sales_revenue - wavg_cos

    diff_closing = fifo_closing_stock - wavg_closing_stock
    diff_gp = fifo_gp - wavg_gp

    prompt = (
        f"You are provided with records from **{business}**, a trading enterprise selling {product}, "
        f"for the financial year ended **{fin_year_end}**.\n\n"
        f"**INVENTORY & PURCHASES RECORDS:**\n"
        f"1. **Opening Inventory (1 March 2025):** {open_units} units @ R{open_unit_cost} each (R{_fmt_money(open_val)})\n\n"
        f"2. **Purchases during the year:**\n"
        f"   • **May 2025:** {b1_units} units @ R{b1_price} each (Carriage on purchases: R{_fmt_money(b1_units * b1_carriage_unit)})\n"
        f"   • **September 2025:** {b2_units} units @ R{b2_price} each (Carriage on purchases: R{_fmt_money(b2_units * b2_carriage_unit)})\n"
        f"   • **January 2026:** {b3_units} units @ R{b3_price} each (Carriage on purchases: R{_fmt_money(b3_units * b3_carriage_unit)})\n\n"
        f"3. **Physical Stock Count (28 February 2026):**\n"
        f"   • Exactly **{closing_units} units** were on hand in the warehouse at year end.\n\n"
        f"4. **Sales:**\n"
        f"   • {units_sold} units were sold during the year at a selling price of R{selling_price_per_unit} per unit "
        f"(Total Sales Revenue: R{_fmt_money(sales_revenue)}).\n\n"
        f"**REQUIRED:**\n"
        f"1. Complete the 2D Inventory Valuation Comparative Matrix below for both **FIFO** and **Weighted Average** methods.\n"
        f"2. Explain the qualitative effect of FIFO compared to Weighted Average on **Net Profit** and **Income Tax liability** "
        f"during times of rising purchase prices (inflation)."
    )

    headers = ["Inventory Valuation Method", "Closing Stock (R)", "Cost of Sales (R)", "Gross Profit (R)"]

    # 2D table layout with cell types: required, given, must_be_empty
    # Row 0: FIFO (required inputs for Closing Stock, COS, GP)
    # Row 1: Weighted Average (required inputs for Closing Stock, COS, GP)
    # Row 2: Regulatory Prudence Note (must_be_empty for amounts, given label)
    rows_data = [
        [
            {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": "FIFO Method", "type": "given", "cell_type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "", "type": "required", "cell_type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": "", "type": "required", "cell_type": "required", "editable": True},
            {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "", "type": "required", "cell_type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "cell_id": "t0_r1_c0", "value": "Weighted Average Method", "type": "given", "cell_type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "cell_id": "t0_r1_c1", "value": "", "type": "required", "cell_type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "cell_id": "t0_r1_c2", "value": "", "type": "required", "cell_type": "required", "editable": True},
            {"coordinate": "t0_r1_c3", "cell_id": "t0_r1_c3", "value": "", "type": "required", "cell_type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "cell_id": "t0_r2_c0", "value": "Difference (FIFO vs Weighted Average)", "type": "given", "cell_type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "cell_id": "t0_r2_c1", "value": str(diff_closing), "type": "required", "cell_type": "required", "editable": True},
            {"coordinate": "t0_r2_c2", "cell_id": "t0_r2_c2", "value": "", "type": "must_be_empty", "cell_type": "must_be_empty", "editable": True},
            {"coordinate": "t0_r2_c3", "cell_id": "t0_r2_c3", "value": str(diff_gp), "type": "required", "cell_type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": str(fifo_closing_stock),
        "t0_r0_c2": str(fifo_cos),
        "t0_r0_c3": str(fifo_gp),
        "t0_r1_c1": str(wavg_closing_stock),
        "t0_r1_c2": str(wavg_cos),
        "t0_r1_c3": str(wavg_gp),
        "t0_r2_c1": str(diff_closing),
        "t0_r2_c2": "",  # Must be empty
        "t0_r2_c3": str(diff_gp),
    }

    cell_hints = {
        "t0_r0_c1": f"FIFO Closing Stock = ({fifo_layer1_units} units @ R{b3_effective_unit}) + ({fifo_layer2_units} units @ R{b2_effective_unit}) = R{_fmt_money(fifo_closing_stock)}",
        "t0_r0_c2": f"FIFO Cost of Sales = Total Goods Available (R{_fmt_money(total_available_cost)}) – Closing Stock (R{_fmt_money(fifo_closing_stock)}) = R{_fmt_money(fifo_cos)}",
        "t0_r0_c3": f"FIFO Gross Profit = Sales (R{_fmt_money(sales_revenue)}) – Cost of Sales (R{_fmt_money(fifo_cos)}) = R{_fmt_money(fifo_gp)}",
        "t0_r1_c1": f"Weighted Average Unit Cost = R{_fmt_money(total_available_cost)} / {total_available_units} = R{_fmt_money(wavg_unit_cost)}. Closing Stock = {closing_units} × R{_fmt_money(wavg_unit_cost)} = R{_fmt_money(wavg_closing_stock)}",
        "t0_r1_c2": f"Weighted Average Cost of Sales = Total Goods Available (R{_fmt_money(total_available_cost)}) – Closing Stock (R{_fmt_money(wavg_closing_stock)}) = R{_fmt_money(wavg_cos)}",
        "t0_r1_c3": f"Weighted Average Gross Profit = Sales (R{_fmt_money(sales_revenue)}) – Cost of Sales (R{_fmt_money(wavg_cos)}) = R{_fmt_money(wavg_gp)}",
        "t0_r2_c1": f"FIFO closing inventory exceeds Weighted Average by R{_fmt_money(diff_closing)}.",
        "t0_r2_c2": "This cell MUST remain empty. Comparative Cost of Sales variance is not entered here.",
        "t0_r2_c3": f"FIFO Gross Profit exceeds Weighted Average by R{_fmt_money(diff_gp)}.",
    }

    marking_points = [
        {"id": "mp_fifo_close", "desc": f"FIFO Closing Stock: R{_fmt_money(fifo_closing_stock)}", "marks": 2, "editable": True},
        {"id": "mp_fifo_cos", "desc": f"FIFO Cost of Sales: R{_fmt_money(fifo_cos)}", "marks": 1, "editable": True},
        {"id": "mp_fifo_gp", "desc": f"FIFO Gross Profit: R{_fmt_money(fifo_gp)}", "marks": 1, "editable": True},
        {"id": "mp_wavg_cost", "desc": f"Weighted Average unit cost: R{_fmt_money(wavg_unit_cost)}", "marks": 1, "editable": True},
        {"id": "mp_wavg_close", "desc": f"Weighted Average Closing Stock: R{_fmt_money(wavg_closing_stock)}", "marks": 2, "editable": True},
        {"id": "mp_wavg_cos", "desc": f"Weighted Average Cost of Sales: R{_fmt_money(wavg_cos)}", "marks": 1, "editable": True},
        {"id": "mp_wavg_gp", "desc": f"Weighted Average Gross Profit: R{_fmt_money(wavg_gp)}", "marks": 1, "editable": True},
        {"id": "mp_diff", "desc": f"Variance differences (R{_fmt_money(diff_closing)} and R{_fmt_money(diff_gp)})", "marks": 1, "editable": True},
        {"id": "mp_qual_np", "desc": "Qualitative comparison: FIFO yields lower COS and higher Net Profit during inflation", "marks": 1, "editable": True},
        {"id": "mp_qual_tax", "desc": "Qualitative comparison: Higher FIFO profit attracts higher income tax liability", "marks": 1, "editable": True},
    ]

    marking_schema = {
        "total_marks": 12,
        "marking_points": marking_points,
        "deductions": [
            {"rule": "must_be_empty_filled", "penalty": -1},
            {"rule": "allocated_carriage_incorrectly", "penalty": -1},
            {"rule": "used_oldest_stock_for_fifo_closing", "penalty": -1},
            {"rule": "omitted_opening_stock_in_weighted_avg", "penalty": -1},
            {"rule": "simple_average_instead_of_weighted_average", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    ideal_answer = (
        f"1. **Inventory Valuation Schedule:**\n"
        f"   • FIFO: Closing Stock = R{_fmt_money(fifo_closing_stock)}; Cost of Sales = R{_fmt_money(fifo_cos)}; Gross Profit = R{_fmt_money(fifo_gp)}\n"
        f"   • Weighted Average: Closing Stock = R{_fmt_money(wavg_closing_stock)}; Cost of Sales = R{_fmt_money(wavg_cos)}; Gross Profit = R{_fmt_money(wavg_gp)}\n\n"
        f"2. **Qualitative Analysis (Inflationary Conditions):**\n"
        f"   • **Net Profit Effect:** FIFO assumes older, cheaper stock was sold first. This results in a lower Cost of Sales "
        f"and higher reported Gross and Net Profit (by R{_fmt_money(diff_gp)}). Weighted Average smooths costs, producing lower profit.\n"
        f"   • **Tax Liability Effect:** Because FIFO reports a higher taxable income, the business faces a higher income tax liability. "
        f"Weighted Average reduces tax outflow in periods of sustained inflation.\n"
        f"   • **IFRS / Prudence Principle:** Once an inventory method is chosen, it must be applied consistently from year to year. "
        f"A business cannot alternate methods to manipulate reported earnings or evade tax."
    )

    return {
        "id": f"acc11_inv_compound_{r.randint(100000, 999999)}",
        "title": "FIFO vs Weighted Average Inventory Valuation & Qualitative Impact",
        "topic": "Inventory Valuation",
        "subskill": "inventory_valuation_compound",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 15,
        "prompt": prompt,
        "question_type": "table_completion",
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": ideal_answer,
        "sample_answer": ideal_answer,
        "marks": 12,
        "deduction_rules": [
            {"rule": "must_be_empty_filled", "penalty": -1},
        ],
        "misconception_tags": [
            MISCONCEPTION_CARRIAGE,
            MISCONCEPTION_FIFO_OLDEST,
            MISCONCEPTION_OMITTED_OPENING,
            MISCONCEPTION_SIMPLE_AVG,
        ],
        "marking_schema": marking_schema,
        "hints": {
            "tier1_location": "Add carriage on purchases to the cost of purchases for each batch before layering or averaging.",
            "tier2_directional_rule": (
                f"FIFO: Layer backwards from the newest January batch ({b3_units} @ R{b3_effective_unit}) "
                f"plus {fifo_layer2_units} units from September @ R{b2_effective_unit}. "
                f"Weighted Average: Divide total goods available (R{_fmt_money(total_available_cost)}) by {total_available_units} units."
            ),
            "tier3_worked_step": ideal_answer,
        },
    }


# ============================================================================
# PUBLIC DISPATCHER & REGISTRY INTERFACE
# ============================================================================
BUILDERS = {
    "compound": _build_compound_inventory_valuation,
    "inventory_valuation": _build_compound_inventory_valuation,
    "fifo_and_weighted_average": _build_compound_inventory_valuation,
    "elementary_fifo_closing_stock": _build_elementary_fifo_closing_stock,
    "elementary_weighted_avg_unit_cost": _build_elementary_weighted_avg_unit_cost,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Accounting Inventory Valuation questions."""
    base_seed = 42 if seed is None else int(seed)

    if mode in BUILDERS and mode != "compound":
        target_mode = mode
    elif subskill in BUILDERS:
        target_mode = subskill
    else:
        target_mode = "compound"

    builder = BUILDERS.get(target_mode, _build_compound_inventory_valuation)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    *,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "hard",
    mode: str = "compound",
    subskill: str = "mixed",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Alternative signature returning question list directly for adapter compatibility."""
    res = generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, mode=mode, **kwargs)
    return res.get("questions", [])
