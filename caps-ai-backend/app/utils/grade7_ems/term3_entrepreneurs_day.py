"""Grade 7 EMS: Term 3 - Entrepreneur's Day Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "planning_entrepreneurs_day",
    "promotional_channels",
    "variable_costs_production",
    "calculate_profit_simple",
    "income_expenditure_statement"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_planning_entrepreneurs_day(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    item = rng.choice(["fruit smoothies", "beaded keyholders", "homemade popcorn", "decorated bookmarks", "baked cupcakes"])
    prompt = (
        f"A Grade 7 class in {area} prepares to host an Entrepreneur's Day. {person} plans a stall selling {item}.\n\n"
        f"Which step should {person} take FIRST before purchasing any materials?"
    )
    correct_opt = "Conduct market research among fellow learners to confirm demand and willingness to pay"
    options = [
        correct_opt,
        "Spend all available personal money immediately on packaging boxes",
        "Sign a long-term lease contract for commercial off-campus premises",
        "Hire adult staff members on fixed monthly contracts"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand planning for Entrepreneur's Day:\n"
        f"Before committing financial capital to produce {item}, the learner must conduct market research "
        f"to determine whether there is sufficient customer demand and what price learners can afford.\n\n"
        f"Step 2: Conclusion:\n"
        f"Market research prevents wasting money on unwanted products."
    )
    return {
        "id": f"g7_ems_day_plan_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "planning_entrepreneurs_day",
        "question_family_id": "planning_entrepreneurs_day",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Hosting an Entrepreneur's Day",
        "hints": {
            "tier_1": "What must you know about your customers before you spend money making a product?",
            "tier_2": "You need to find out if learners actually want to buy what you plan to sell.",
            "tier_3": "Conduct market research first to confirm customer demand and price expectations."
        },
        "misconception_tags": ["premature_spending_planning_error"]
    }


def _build_promotional_channels(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    stall_prod = rng.choice(["freshly squeezed lemonade", "ice lollies", "handmade cards", "pancake treats"])
    prompt = (
        f"{person} wants to advertise a {stall_prod} stall for Entrepreneur's Day at school in {area}.\n\n"
        f"Which promotional strategy is the most cost-effective and appropriate for a school market?"
    )
    correct_opt = "Colourful noticeboard posters, intercom announcements, and word-of-mouth promotion"
    options = [
        correct_opt,
        "Purchasing expensive prime-time television commercial slots on national TV",
        "Taking out a full-page colour advert in a national weekly Sunday newspaper",
        "Placing large commercial highway billboards outside the town"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Principles of school advertising (The 4 Ps - Promotion):\n"
        f"Advertising must be targeted directly at the intended market (learners and teachers) at low cost.\n\n"
        f"Step 2: Evaluate options:\n"
        f"Television and billboards are extremely expensive and reach outside audiences. School posters, intercom notices, "
        f"and word-of-mouth are targeted, highly effective, and virtually free."
    )
    return {
        "id": f"g7_ems_day_promo_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "promotional_channels",
        "question_family_id": "promotional_channels",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Principles of advertising and marketing",
        "hints": {
            "tier_1": "Consider who the customers are (school learners) and how to reach them cheaply.",
            "tier_2": "Look for promotional methods that cost little or nothing and reach learners at school.",
            "tier_3": "Posters on school noticeboards and intercom announcements are ideal for school stalls."
        },
        "misconception_tags": ["inappropriate_mass_media_choice"]
    }


def _build_variable_costs_production(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"At an Entrepreneur's Day stall in {area}, {person} rents a stall table for a fixed fee of R20, "
        f"and buys ingredients (milk, sugar, flavouring) costing R3 per ice lolly produced.\n\n"
        f"Which cost item is classified as a **variable cost**, and why?"
    )
    correct_opt = "The ingredients (R3 per lolly), because total ingredient costs change with the number of units produced"
    options = [
        correct_opt,
        "The table rental (R20), because it changes every time an ice lolly is sold",
        "Neither, because all business costs are permanently fixed",
        "Both, because all production expenses are identical"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define cost concepts:\n"
        "- Fixed cost: Costs that remain constant regardless of output volume (e.g. table rental of R20).\n"
        "- Variable cost: Costs that increase or decrease in direct proportion to the number of units produced (e.g. ingredients at R3 per unit).\n\n"
        "Step 2: Conclusion:\n"
        "The ingredients are a variable cost because total expense directly depends on how many lollies are made."
    )
    return {
        "id": f"g7_ems_day_varcost_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "variable_costs_production",
        "question_family_id": "variable_costs_production",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Fixed vs variable costs",
        "hints": {
            "tier_1": "Ask yourself: which expense changes if you produce 100 units instead of 10 units?",
            "tier_2": "Variable costs vary with production volume; fixed costs stay the same.",
            "tier_3": "Ingredients change with quantity produced, making them variable costs."
        },
        "misconception_tags": ["fixed_variable_cost_inversion"]
    }


def _build_calculate_profit_simple(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    item_sold = rng.choice(["cupcakes", "muffins", "hotdogs", "smoothies"])
    
    qty = rng.choice([30, 40, 50, 60])
    selling_price = rng.choice([8, 10, 12, 15])
    cost_per_unit = rng.choice([4, 5, 6])
    stall_fee = rng.choice([20, 25, 30])
    
    total_income = qty * selling_price
    total_expenses = (qty * cost_per_unit) + stall_fee
    profit = total_income - total_expenses
    
    prompt = (
        f"For Entrepreneur's Day, {person} in {area} sells {qty} {item_sold} at R{selling_price} each. "
        f"The production ingredients cost R{cost_per_unit} per {item_sold[:-1] if item_sold.endswith('s') else item_sold}, "
        f"and the school stall fee is R{stall_fee}.\n\n"
        f"Calculate the **net profit** earned by {person}'s stall."
    )
    correct_opt = f"R{profit}"
    distractors = [
        f"R{total_income}",
        f"R{total_expenses}",
        f"R{total_income - (qty * cost_per_unit)}",
        f"R{profit + 20}"
    ]
    options = [correct_opt] + [d for d in distractors if d != correct_opt][:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Calculate Total Income (Revenue):\n"
        f"Total Income = {qty} units × R{selling_price} = R{total_income}\n\n"
        f"Step 2: Calculate Total Expenses:\n"
        f"Ingredient Cost = {qty} × R{cost_per_unit} = R{qty * cost_per_unit}\n"
        f"Stall Fee (Fixed Cost) = R{stall_fee}\n"
        f"Total Expenses = R{qty * cost_per_unit} + R{stall_fee} = R{total_expenses}\n\n"
        f"Step 3: Calculate Net Profit:\n"
        f"Profit = Total Income - Total Expenses = R{total_income} - R{total_expenses} = R{profit}"
    )
    return {
        "id": f"g7_ems_day_prof_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "calculate_profit_simple",
        "question_family_id": "calculate_profit_simple",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Income and Expenditure Statement and profit",
        "hints": {
            "tier_1": "Profit = Total Income minus Total Expenses.",
            "tier_2": f"Total income is {qty} × R{selling_price} = R{total_income}. Now subtract all ingredient and stall costs.",
            "tier_3": f"R{total_income} - R{total_expenses} = R{profit}."
        },
        "misconception_tags": ["revenue_profit_confusion", "omitted_fixed_cost"]
    }


def _build_income_expenditure_statement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    item_sold = rng.choice(["cupcakes", "ice lollies", "fresh juices", "pancake snacks"])
    
    qty = rng.choice([30, 40, 50, 60])
    selling_price = rng.choice([8, 10, 12, 15])
    cost_per_unit = rng.choice([4, 5, 6])
    stall_fee = rng.choice([20, 25, 30])
    
    revenue = qty * selling_price
    ing_cost = qty * cost_per_unit
    total_exp = ing_cost + stall_fee
    profit = revenue - total_exp
    
    headers = ["Statement Item", "Classification", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": f"Sales Revenue ({qty} {item_sold} @ R{selling_price})", "editable": False}, {"cell_id": "r0_c1", "value": "Income", "editable": False}, {"cell_id": "r0_c2", "value": str(revenue), "editable": False}],
        [{"cell_id": "r1_c0", "value": "Production Ingredients", "editable": False}, {"cell_id": "r1_c1", "value": "Variable Cost", "editable": False}, {"cell_id": "r1_c2", "value": str(ing_cost), "editable": False}],
        [{"cell_id": "r2_c0", "value": "School Stall Rental Fee", "editable": False}, {"cell_id": "r2_c1", "value": "Fixed Cost", "editable": False}, {"cell_id": "r2_c2", "value": str(stall_fee), "editable": False}],
        [{"cell_id": "r3_c0", "value": "TOTAL EXPENSES", "editable": False}, {"cell_id": "r3_c1", "value": "Variable + Fixed Costs", "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": str(total_exp), "editable": True}],
        [{"cell_id": "r4_c0", "value": "NET PROFIT", "editable": False}, {"cell_id": "r4_c1", "value": "Revenue minus Total Expenses", "editable": False}, {"cell_id": "r4_c2", "value": "", "expected": str(profit), "editable": True}],
    ]
    correct_map = {
        "r3_c2": str(total_exp),
        "r4_c2": str(profit),
    }
    
    sol = (
        f"1. Total Expenses = Ingredients (R{ing_cost}) + Stall Fee (R{stall_fee}) = R{total_exp}.\n"
        f"2. Net Profit = Revenue (R{revenue}) - Total Expenses (R{total_exp}) = R{profit}."
    )
    return {
        "id": f"g7_ems_day_stmt_{rng.randint(100000, 999999)}",
        "title": "Entrepreneur's Day Income and Expenditure Statement",
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": f"{person} hosted an Entrepreneur's Day stall in {area} selling {qty} {item_sold} at R{selling_price} each. Ingredient costs totaled R{ing_cost} and the stall fee was R{stall_fee}.\n\nComplete the Income and Expenditure Statement below by calculating:\n1. Total Expenses (row 4)\n2. Net Profit (row 5).",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "expected_answer": f"Total Expenses = R{total_exp}; Net Profit = R{profit}",
        "sample_answer": f"Total Expenses = R{total_exp}; Net Profit = R{profit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "income_expenditure_statement",
        "question_family_id": "income_expenditure_statement",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Income and Expenditure Statement",
        "hints": {
            "tier_1": "Add the ingredient cost and stall rental fee to find Total Expenses.",
            "tier_2": f"Total Expenses = R{ing_cost} + R{stall_fee} = R{total_exp}. Subtract this from Revenue (R{revenue}) to find Net Profit.",
            "tier_3": f"Total Expenses: R{total_exp}; Net Profit: R{profit}."
        },
        "misconception_tags": ["omits_fixed_stall_fee"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "planning_entrepreneurs_day": _build_planning_entrepreneurs_day,
        "promotional_channels": _build_promotional_channels,
        "variable_costs_production": _build_variable_costs_production,
        "calculate_profit_simple": _build_calculate_profit_simple,
        "income_expenditure_statement": _build_income_expenditure_statement
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
