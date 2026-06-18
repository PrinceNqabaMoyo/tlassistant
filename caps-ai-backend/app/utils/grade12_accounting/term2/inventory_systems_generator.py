"""
inventory_systems_generator.py — Grade 12 Term 2
==================================================
Inventory Systems question generator.

Archetype classes covered:
  1. FIFO closing stock valuation
  2. Weighted average closing stock
  3. Specific identification valuation
  4. Cost of sales calculation
  5. Gross profit per method
  6. Stock theft/shortage detection
  7. Stock turnover rate
  8. Stock holding period
  9. Mark-up % comparison
 10. Perpetual vs periodic concepts (MCQ)
 11. FIFO vs weighted average comparison (typed)
 12. Ethics of price manipulation
 13. Internal control for inventory
 14. Trading account completion
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed() if seed is None else r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _rm(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


_BUSINESSES = [
    "Kima Appliances", "Energy World", "Magic Soccer Balls",
    "TechPlanet Stores", "GreenGrocer Traders", "AutoParts Wholesale",
    "DigiMart Electronics", "FreshFoods Distributors",
    "SportZone Retailers", "Office Pro Supplies",
]

_PRODUCTS = [
    "soccer balls", "energy drinks", "laptops", "printers",
    "cellphones", "tablets", "washing machines", "microwaves",
    "office chairs", "monitors",
]


def _make_mcq(*, prompt, options, correct_index, explanation):
    return {
        "id": _make_id("acct12_inv_mcq"), "question_type": "mcq",
        "prompt": prompt, "options": options,
        "correct_index": int(correct_index), "explanation": explanation,
        "expected_answer_type": "mcq", "marks": 2,
        "guidelines": [explanation], "visual_aid_key": "inventory_systems",
    }


def _make_typed(*, prompt, sample_answer, grading_rubric=None):
    gr = grading_rubric or []
    return {
        "id": _make_id("acct12_inv_typed"), "question_type": "typed",
        "prompt": prompt, "sample_answer": sample_answer,
        "expected_answer_type": "text", "grading_rubric": gr,
        "marks": 4 if len(gr) >= 2 else 2,
        "guidelines": [f"Include: {', '.join(gr)}"] if gr else [],
        "visual_aid_key": "inventory_systems",
    }


def _make_calc(*, prompt, correct_answer, unit="R", working_formula=""):
    return {
        "id": _make_id("acct12_inv_calc"), "question_type": "calc",
        "prompt": prompt, "correct_value": correct_answer,
        "correct_answer": correct_answer, "unit": unit,
        "working_formula": working_formula, "expected_answer_type": "number",
        "marks": 3, "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "inventory_systems",
    }


# ---------------------------------------------------------------------------
# FIFO
# ---------------------------------------------------------------------------

def _gen_fifo_closing_stock(r: random.Random):
    biz = r.choice(_BUSINESSES)
    product = r.choice(_PRODUCTS)

    open_units = r.randint(200, 500)
    open_price = _rm(r.randint(8, 25))

    # 3 purchases at increasing prices
    p1_units = r.randint(500, 1200)
    p1_price = _rm(open_price + r.randint(1, 5))
    p2_units = r.randint(800, 2000)
    p2_price = _rm(p1_price + r.randint(1, 5))
    p3_units = r.randint(300, 800)
    p3_price = _rm(p2_price + r.randint(1, 5))

    total_avail = open_units + p1_units + p2_units + p3_units
    sold_units = r.randint(int(total_avail * 0.5), int(total_avail * 0.85))
    closing_units = total_avail - sold_units

    # FIFO closing = most recent purchase prices
    fifo_val = 0.0
    remaining = closing_units
    # Start from most recent
    for units, price in [(p3_units, p3_price), (p2_units, p2_price),
                          (p1_units, p1_price), (open_units, open_price)]:
        if remaining <= 0:
            break
        take = min(remaining, units)
        fifo_val += take * price
        remaining -= take

    fifo_val = _rm(fifo_val)

    return _make_calc(
        prompt=(
            f"{biz} sells {product}. The business uses the FIFO method.\n\n"
            f"• Opening stock: {open_units} units @ R{open_price}\n"
            f"• Purchase 1: {p1_units} units @ R{p1_price}\n"
            f"• Purchase 2: {p2_units} units @ R{p2_price}\n"
            f"• Purchase 3: {p3_units} units @ R{p3_price}\n"
            f"• Closing stock: {closing_units} units\n\n"
            f"Calculate the value of the closing stock using the FIFO method."
        ),
        correct_answer=fifo_val, unit="R",
        working_formula=f"FIFO: Use most recent prices first for {closing_units} units = {_money(fifo_val)}",
    )


# ---------------------------------------------------------------------------
# Weighted Average
# ---------------------------------------------------------------------------

def _gen_weighted_avg_closing(r: random.Random):
    biz = r.choice(_BUSINESSES)
    product = r.choice(_PRODUCTS)

    open_units = r.randint(200, 500)
    open_price = _rm(r.randint(8, 20))
    open_val = _rm(open_units * open_price)

    p1_units = r.randint(500, 1500)
    p1_price = _rm(open_price + r.randint(1, 5))
    p1_val = _rm(p1_units * p1_price)

    p2_units = r.randint(500, 1500)
    p2_price = _rm(p1_price + r.randint(1, 5))
    p2_val = _rm(p2_units * p2_price)

    total_units = open_units + p1_units + p2_units
    total_val = _rm(open_val + p1_val + p2_val)
    avg_price = _rm(total_val / total_units)

    sold_units = r.randint(int(total_units * 0.5), int(total_units * 0.85))
    closing_units = total_units - sold_units
    closing_val = _rm(closing_units * avg_price)

    return _make_calc(
        prompt=(
            f"{biz} sells {product}. The business uses the weighted average method.\n\n"
            f"• Opening stock: {open_units} units @ R{open_price} = {_money(open_val)}\n"
            f"• Purchase 1: {p1_units} units @ R{p1_price} = {_money(p1_val)}\n"
            f"• Purchase 2: {p2_units} units @ R{p2_price} = {_money(p2_val)}\n"
            f"• Units sold: {sold_units}\n\n"
            f"Calculate the value of the closing stock using the weighted average method."
        ),
        correct_answer=closing_val, unit="R",
        working_formula=(
            f"Total cost = {_money(total_val)}. Total units = {total_units}. "
            f"Avg = {_money(total_val)} ÷ {total_units} = R{avg_price}. "
            f"Closing = {closing_units} × R{avg_price} = {_money(closing_val)}"
        ),
    )


# ---------------------------------------------------------------------------
# Cost of sales
# ---------------------------------------------------------------------------

def _gen_cost_of_sales(r: random.Random):
    biz = r.choice(_BUSINESSES)
    opening = _rm(r.randint(50, 200) * 1000)
    purchases = _rm(r.randint(200, 800) * 1000)
    closing = _rm(r.randint(60, 250) * 1000)
    stolen = _rm(r.choice([0, 2, 5, 8]) * 1000)

    cos = _rm(opening + purchases - stolen - closing)

    prompt_parts = [
        f"• Opening stock: {_money(opening)}",
        f"• Purchases: {_money(purchases)}",
        f"• Closing stock: {_money(closing)}",
    ]
    formula_parts = f"{_money(opening)} + {_money(purchases)}"
    if stolen > 0:
        prompt_parts.append(f"• Stock written off (theft): {_money(stolen)}")
        formula_parts += f" − {_money(stolen)}"
    formula_parts += f" − {_money(closing)} = {_money(cos)}"

    return _make_calc(
        prompt=f"{biz}: Calculate the cost of sales.\n\n" + "\n".join(prompt_parts),
        correct_answer=cos, unit="R",
        working_formula=formula_parts,
    )


# ---------------------------------------------------------------------------
# Gross profit comparison
# ---------------------------------------------------------------------------

def _gen_gross_profit(r: random.Random):
    biz = r.choice(_BUSINESSES)
    sales = _rm(r.randint(300, 800) * 1000)
    cos = _rm(r.randint(150, 500) * 1000)
    gp = _rm(sales - cos)

    return _make_calc(
        prompt=(
            f"{biz}: Sales = {_money(sales)}, Cost of sales = {_money(cos)}. "
            f"Calculate the gross profit."
        ),
        correct_answer=gp, unit="R",
        working_formula=f"{_money(sales)} − {_money(cos)} = {_money(gp)}",
    )


# ---------------------------------------------------------------------------
# Stock theft
# ---------------------------------------------------------------------------

def _gen_stock_theft(r: random.Random):
    biz = r.choice(_BUSINESSES)
    product = r.choice(_PRODUCTS)
    open_u = r.randint(300, 800)
    purchased = r.randint(1500, 3000)
    sold = r.randint(1200, open_u + purchased - 200)
    actual_count = r.randint(100, open_u + purchased - sold - 10)

    expected = open_u + purchased - sold
    stolen = expected - actual_count

    return _make_calc(
        prompt=(
            f"{biz} sells {product}.\n"
            f"• Opening stock: {open_u} units\n"
            f"• Purchased: {purchased} units\n"
            f"• Sold: {sold} units\n"
            f"• Physical count: {actual_count} units\n\n"
            f"Calculate the number of units stolen."
        ),
        correct_answer=float(stolen), unit="units",
        working_formula=(
            f"Expected = {open_u} + {purchased} − {sold} = {expected}. "
            f"Stolen = {expected} − {actual_count} = {stolen}"
        ),
    )


# ---------------------------------------------------------------------------
# Stock turnover & holding period
# ---------------------------------------------------------------------------

def _gen_stock_turnover_rate(r: random.Random):
    biz = r.choice(_BUSINESSES)
    open_s = _rm(r.randint(50, 200) * 1000)
    close_s = _rm(r.randint(60, 220) * 1000)
    cos = _rm(r.randint(500, 2000) * 1000)
    avg = _rm((open_s + close_s) / 2)
    rate = round(cos / avg, 1) if avg > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}: Opening stock = {_money(open_s)}, Closing stock = {_money(close_s)}, "
            f"Cost of sales = {_money(cos)}. "
            f"Calculate the stock turnover rate (times per year)."
        ),
        correct_answer=rate, unit="times",
        working_formula=(
            f"Avg = ½({_money(open_s)} + {_money(close_s)}) = {_money(avg)}. "
            f"Rate = {_money(cos)} ÷ {_money(avg)} = {rate} times"
        ),
    )


def _gen_stock_holding_period(r: random.Random):
    biz = r.choice(_BUSINESSES)
    open_s = _rm(r.randint(50, 200) * 1000)
    close_s = _rm(r.randint(60, 220) * 1000)
    cos = _rm(r.randint(500, 2000) * 1000)
    avg = _rm((open_s + close_s) / 2)
    days = round(avg / cos * 365)

    return _make_calc(
        prompt=(
            f"{biz}: Opening stock = {_money(open_s)}, Closing stock = {_money(close_s)}, "
            f"Cost of sales = {_money(cos)}. "
            f"Calculate the stock holding period in days."
        ),
        correct_answer=float(days), unit="days",
        working_formula=(
            f"Avg = ½({_money(open_s)} + {_money(close_s)}) = {_money(avg)}. "
            f"Period = {_money(avg)} ÷ {_money(cos)} × 365 = {days} days"
        ),
    )


# ---------------------------------------------------------------------------
# Mark-up %
# ---------------------------------------------------------------------------

def _gen_markup_comparison(r: random.Random):
    biz = r.choice(_BUSINESSES)
    cos = _rm(r.randint(400, 1200) * 1000)
    target_markup = r.choice([30, 40, 50, 60])
    actual_gp = _rm(cos * (target_markup - r.randint(2, 8)) / 100)
    actual_markup = round(actual_gp / cos * 100, 1)

    return _make_calc(
        prompt=(
            f"{biz} uses a target mark-up of {target_markup}% on cost. "
            f"Cost of sales = {_money(cos)}, Gross profit = {_money(actual_gp)}. "
            f"Calculate the actual mark-up percentage achieved."
        ),
        correct_answer=actual_markup, unit="%",
        working_formula=f"{_money(actual_gp)} ÷ {_money(cos)} × 100 = {actual_markup}%",
    )


# ---------------------------------------------------------------------------
# Concepts MCQ
# ---------------------------------------------------------------------------

def _gen_perpetual_periodic_mcq(r: random.Random):
    qs = [
        {
            "prompt": "Under a perpetual inventory system, cost of sales is:",
            "options": [
                "Calculated and recorded every time goods are sold",
                "Calculated only at the end of the period",
                "Never calculated separately",
                "Calculated using the weighted average method only",
            ],
            "correct": 0,
            "explanation": "In a perpetual system, cost of sales is calculated and recorded with each sale transaction.",
        },
        {
            "prompt": "FIFO stands for:",
            "options": [
                "First In, First Out — oldest stock is sold first",
                "First In, First Out — newest stock is sold first",
                "Final Inventory, First Out",
                "Fixed Inventory, Flexible Output",
            ],
            "correct": 0,
            "explanation": "FIFO means First In, First Out — the oldest stock purchased is assumed to be sold first.",
        },
        {
            "prompt": "A disadvantage of the specific identification method is:",
            "options": [
                "The cost price of identical items can be manipulated",
                "It is too difficult to track individual items",
                "It cannot be used for expensive items",
                "It always gives a lower profit than FIFO",
            ],
            "correct": 0,
            "explanation": "With specific identification, identical items at different costs can be chosen to manipulate profit.",
        },
        {
            "prompt": "Under the periodic inventory system, cost of sales is calculated as:",
            "options": [
                "Opening stock + Purchases − Closing stock",
                "Closing stock − Purchases + Opening stock",
                "Sales − Gross profit",
                "Purchases only",
            ],
            "correct": 0,
            "explanation": "Periodic: COS = Opening stock + Net purchases + Carriage − Closing stock.",
        },
    ]
    chosen = r.choice(qs)
    return _make_mcq(
        prompt=chosen["prompt"], options=chosen["options"],
        correct_index=chosen["correct"], explanation=chosen["explanation"],
    )


# ---------------------------------------------------------------------------
# Typed explanations
# ---------------------------------------------------------------------------

def _gen_fifo_vs_wavg_typed(r: random.Random):
    return _make_typed(
        prompt="Give TWO reasons why a business might prefer the FIFO stock valuation method over the weighted average method.",
        sample_answer=(
            "1. FIFO is simple and easy to use. "
            "2. Closing stock is valued at realistic/current prices. "
            "3. The movement of stock is logical — oldest stock sold first. "
            "4. Suitable for stock with a limited shelf life."
        ),
        grading_rubric=[
            "Realistic/current closing stock values",
            "Logical stock flow (oldest first)",
        ],
    )


def _gen_ethics_inventory(r: random.Random):
    return _make_typed(
        prompt=(
            "A dealer has two identical vehicles — one purchased at R100 000 and another "
            "at R130 000. When the cheaper one is sold, the dealer records the cost as R130 000. "
            "Is this ethical? Explain."
        ),
        sample_answer=(
            "No, this is unethical. The dealer is manipulating profit by recording a higher "
            "cost of sales, thereby reducing taxable profit. This is a form of tax evasion "
            "and misrepresents the financial position of the business."
        ),
        grading_rubric=[
            "Identified as unethical/manipulative",
            "Effect on profit explained (lower profit reported)",
            "Tax evasion or misrepresentation mentioned",
        ],
    )


def _gen_internal_control_inventory(r: random.Random):
    return _make_typed(
        prompt="Suggest TWO internal control measures for managing inventory.",
        sample_answer=(
            "1. Conduct regular physical stock counts and reconcile with records. "
            "2. Set reorder levels to avoid stock-outs. "
            "3. Restrict access to the storeroom to authorised personnel. "
            "4. Use security cameras and alarm systems."
        ),
        grading_rubric=[
            "Regular physical stock counts/reconciliation",
            "Access control or security measures",
        ],
    )


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

_GENERATORS = [
    _gen_fifo_closing_stock,
    _gen_weighted_avg_closing,
    _gen_cost_of_sales,
    _gen_gross_profit,
    _gen_stock_theft,
    _gen_stock_turnover_rate,
    _gen_stock_holding_period,
    _gen_markup_comparison,
    _gen_perpetual_periodic_mcq,
    _gen_fifo_vs_wavg_typed,
    _gen_ethics_inventory,
    _gen_internal_control_inventory,
]


def generate_questions(
    *, subskill="mixed", difficulty="easy", question_type="mixed",
    count=1, seed=None, mode="",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions = []
    for _ in range(count):
        q = r.choice(_GENERATORS)(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)
    return questions
