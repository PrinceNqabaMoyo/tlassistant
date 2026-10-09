"""Grade 10 Accounting - Inventory and Cost of Sales Generator.
Covers:
  - Perpetual Inventory System for Sole Traders.
  - Mark-up on Cost Percentage Calculations (Cost of Sales, Selling Price, Gross Profit).
  - Formula: Cost of Sales = Sales * 100 / (100 + % Mark-up).
  - Trading Stock Deficit / Surplus adjustments at financial year-end.
  - Recording adjustments in the General Journal (Debit Trading Stock Deficit, Credit Trading Stock).

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade10_inventory_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "inventory_cost_of_sales"

    archetype = r.choice(["cost_of_sales_from_sales", "selling_price_from_cost", "trading_stock_deficit", "gross_profit_analysis"])
    if subskill == "elementary_cost_of_sales":
        archetype = "cost_of_sales_from_sales"
    elif subskill == "elementary_trading_stock_deficit":
        archetype = "trading_stock_deficit"

    if archetype == "cost_of_sales_from_sales":
        # Mark-up on cost: e.g. 25%, 50%, 60%, 100%
        markup = r.choice([25, 50, 60, 100])
        cost = r.choice([8000, 12000, 16000, 20000, 30000])
        sales = int(cost * (100 + markup) / 100)
        gp = sales - cost

        prompt = (
            f"Langa Traders sells goods for cash and on credit at a profit mark-up of \\({markup}\\%\\) on cost.\n\n"
            f"Total Sales for the month amounted to \\(\\text{{R}}\\,{sales:,}\\).\n\n"
            f"1. Calculate the Cost of Sales for the month.\n"
            f"2. Calculate the Gross Profit earned."
        )
        sample_answer = (
            rf"\text{{Cost of Sales}} = \text{{Sales}} \times \frac{{100}}{{100 + \%\,\text{{mark-up}}}} = "
            rf"\text{{R}}\,{sales:,} \times \frac{{100}}{{{100 + markup}}} = \text{{R}}\,{cost:,}\\\ "
            rf"\text{{Gross Profit}} = \text{{Sales}} - \text{{Cost of Sales}} = \text{{R}}\,{sales:,} - \text{{R}}\,{cost:,} = \text{{R}}\,{gp:,}"
        )

        return {
            "id": f"g10_acct_inv_cos_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Inventory",
            "subskill": "cost_of_sales_calculation",
            "learning_objective_id": "g10_acct_cost_of_sales",
            "archetype": "cost_of_sales_from_sales",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Cost of Sales: R{cost:,}, Gross Profit: R{gp:,}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Formula Sales * 100 / (100 + markup%)", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Cost of Sales R{cost:,}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Gross Profit R{gp:,}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "markup_on_sales_confusion", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"When mark-up is on cost, Sales represents {100 + markup}% while Cost represents 100%.",
                "tier_2": rf"Apply $\text{{Cost of Sales}} = \text{{Sales}} \times \frac{{100}}{{{100 + markup}}} = \text{{R}}\,{sales:,} \times \frac{{100}}{{{100 + markup}}}$.",
                "tier_3": rf"$\text{{Cost of Sales}} = \text{{R}}\,{cost:,}$. Gross Profit $= \text{{R}}\,{sales:,} - \text{{R}}\,{cost:,} = \text{{R}}\,{gp:,}$.",
            },
            "misconception_tags": ["markup_on_sales_confusion", "calculated_percentage_of_sales_directly"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "selling_price_from_cost":
        markup = r.choice([25, 33, 50, 75, 100])
        cost = r.choice([150, 240, 360, 480, 600])
        sp = int(cost * (100 + markup) / 100)
        profit = sp - cost

        prompt = (
            f"A business purchases an inventory item at a cost price of \\(\\text{{R}}\\,{cost:,}\\). "
            f"The business applies a profit mark-up of \\({markup}\\%\\) on cost.\n\n"
            f"1. Calculate the profit amount per item.\n"
            f"2. Calculate the selling price of the item."
        )
        sample_answer = (
            rf"\text{{Profit}} = \text{{R}}\,{cost:,} \times \frac{{{markup}}}{{100}} = \text{{R}}\,{profit:,}\\\ "
            rf"\text{{Selling Price}} = \text{{Cost}} + \text{{Profit}} = \text{{R}}\,{cost:,} + \text{{R}}\,{profit:,} = \text{{R}}\,{sp:,}"
        )

        return {
            "id": f"g10_acct_inv_sp_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Inventory",
            "subskill": "selling_price_markup",
            "learning_objective_id": "g10_acct_selling_price_markup",
            "archetype": "selling_price_from_cost",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Profit: R{profit:,}, Selling Price: R{sp:,}",
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Profit calculation R{profit:,}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Selling price R{sp:,}", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"To add {markup}% mark-up, calculate {markup}% of the cost price and add it to the cost.",
                "tier_2": rf"$\text{{Selling Price}} = \text{{R}}\,{cost:,} \times \frac{{{100 + markup}}}{{100}}$.",
                "tier_3": rf"$\text{{Profit}} = \text{{R}}\,{profit:,}$, $\text{{Selling Price}} = \text{{R}}\,{sp:,}$.",
            },
            "misconception_tags": ["deducted_markup_instead_of_adding"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "easy",
        }

    else:
        # Trading Stock Deficit
        ledger_bal = r.choice([48000, 62000, 75000, 84000])
        physical_count = ledger_bal - r.choice([1200, 1800, 2400, 3500])
        deficit = ledger_bal - physical_count

        prompt = (
            f"On 28 February 2026, the Trading Stock account in the General Ledger of Simphiwe Traders "
            f"showed a debit balance of \\(\\text{{R}}\\,{ledger_bal:,}\\).\n\n"
            f"A physical stock count conducted on the same day revealed trading stock on hand valued at "
            f"\\(\\text{{R}}\\,{physical_count:,}\\).\n\n"
            f"1. Calculate the trading stock deficit or surplus.\n"
            f"2. Record the year-end adjustment in the General Journal (show Accounts Debited and Credited)."
        )
        sample_answer = (
            rf"\text{{Trading Stock Deficit}} = \text{{R}}\,{ledger_bal:,} - \text{{R}}\,{physical_count:,} = \text{{R}}\,{deficit:,}\\\ "
            rf"\textbf{{General Journal:}}\\\ "
            rf"\text{{Debit: Trading Stock Deficit (Expense) \dots R}}\,{deficit:,}\\\ "
            rf"\text{{Credit: Trading Stock (Asset) \dots R}}\,{deficit:,}\\\ "
            rf"\text{{Narration: Trading stock written down to physical count valuation.}}"
        )

        return {
            "id": f"g10_acct_inv_deficit_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Inventory",
            "subskill": "trading_stock_deficit",
            "learning_objective_id": "g10_acct_trading_stock_deficit",
            "archetype": "trading_stock_deficit",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Deficit: R{deficit:,}; Debit: Trading Stock Deficit, Credit: Trading Stock",
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Calculation of Deficit R{deficit:,}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Debit: Trading Stock Deficit (Expense)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Credit: Trading Stock (Asset reduction)", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Journal narration", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "debit_credit_inversion", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Compare the books (ledger) with the physical stock count. If physical stock is lower than books, it is a deficit (shortage).",
                "tier_2": rf"Deficit $= \text{{R}}\,{ledger_bal:,} - \text{{R}}\,{physical_count:,} = \text{{R}}\,{deficit:,}$. Trading stock deficit is an expense.",
                "tier_3": rf"Debit Trading Stock Deficit: R{deficit:,}. Credit Trading Stock: R{deficit:,}.",
            },
            "misconception_tags": ["debit_credit_inversion", "confused_deficit_and_surplus"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade10_inventory_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
