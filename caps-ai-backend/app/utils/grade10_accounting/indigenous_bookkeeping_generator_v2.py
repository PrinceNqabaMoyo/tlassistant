from __future__ import annotations

import random
import uuid
from typing import Any, Callable, Dict, List, Optional

SUBSKILLS = (
    "informal_vs_formal",
    "resource_management",
    "business_planning",
    "pricing_and_markup",
    "labour_income_expenses",
)

LEGACY_SUBSKILL_MAP = {
    "concepts": "informal_vs_formal",
    "concept": "informal_vs_formal",
    "activity_1": "business_planning",
    "activity1": "business_planning",
    "activity_2": "informal_vs_formal",
    "activity2": "informal_vs_formal",
    "compare_systems": "informal_vs_formal",
}


def _rng(seed: Optional[int]) -> random.Random:
    generator = random.Random()
    generator.seed(None if seed is None else int(seed))
    return generator


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(value: float) -> float:
    return round(float(value) + 1e-9, 2)


def _normalize_subskill(subskill: str) -> str:
    key = str(subskill or "mixed").strip().lower()
    normalized = LEGACY_SUBSKILL_MAP.get(key, key)
    return normalized if normalized in SUBSKILLS or normalized == "mixed" else "mixed"


def _normalize_question_type(question_type: str) -> str:
    key = str(question_type or "mixed").strip().lower()
    allowed = {"mixed", "mcq", "typed", "calc", "table", "table_wordbank"}
    return key if key in allowed else "mixed"


def _signature(question: Dict[str, Any]) -> str:
    return f"{question.get('question_type', '')}::{question.get('prompt', '').strip()}"


def _teach(what: str, where: str, method: str, record_link: str) -> Dict[str, str]:
    return {
        "what_to_enter": what,
        "where_to_look": where,
        "method_or_formula": method,
        "record_link": record_link,
    }


def _mcq(prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    # Shuffle options so the correct answer position varies across calls
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]
    new_correct_index = indices.index(int(correct_index))
    return {
        "id": _make_id("acct10_indigenous_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": shuffled_options,
        "correct_index": new_correct_index,
        "explanation": explanation,
        "guidelines": [explanation],
        "answer_part_hints": [{"label": "Why", "value": explanation}],
        "expected_answer_type": "mcq",
    }


def _typed(prompt: str, sample_answer: str, rubric: List[str], guidelines: Optional[List[str]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "grading_rubric": rubric,
        "guidelines": guidelines or rubric,
        "marks": max(2, len(rubric) * 2),
        "answer_part_hints": [{"label": f"Point {idx + 1}", "value": item} for idx, item in enumerate(rubric)],
        "expected_answer_type": "text",
    }


def _table(prompt: str, headers: List[str], rows: List[List[str]], sample_answer: str, hints: List[Dict[str, str]], guidelines: List[str]) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_table"),
        "question_type": "table",
        "prompt": prompt,
        "table": {"headers": headers, "rows": rows},
        "sample_answer": sample_answer,
        "answer_part_hints": hints,
        "guidelines": guidelines,
        "expected_answer_type": "table_data",
    }


def _calc(prompt: str, correct_value: float, unit: str, formula: str, formula_hint: str, derivation: Dict[str, str]) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(correct_value),
        "unit": unit,
        "working_formula": formula,
        "formula_hint": formula_hint,
        "guidelines": [formula_hint, f"Use: {formula}"],
        "answer_part_hints": [{"label": key, "value": value} for key, value in derivation.items()],
        "derivation_map": derivation,
        "expected_answer_type": "number",
    }


def _wordbank(prompt: str, left_header: str, right_header: str, rows_data: List[Dict[str, Any]], guidelines: List[str]) -> Dict[str, Any]:
    rows = []
    word_bank: List[Dict[str, str]] = []
    correct_map: Dict[str, Dict[str, str]] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    derivation_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for idx, row in enumerate(rows_data):
        left_id = f"w_{idx}_1"
        right_id = f"w_{idx}_2"
        rows.append([row["label"], "", ""])
        word_bank.append({"id": left_id, "text": row["left"], "label": row["left"]})
        word_bank.append({"id": right_id, "text": row["right"], "label": row["right"]})
        correct_map[str(idx)] = {"1": left_id, "2": right_id}
        cell_teaching_map[f"{idx}:1"] = row["left_hint"]
        cell_teaching_map[f"{idx}:2"] = row["right_hint"]
        derivation_map[f"{idx}:1"] = row["left_reason"]
        derivation_map[f"{idx}:2"] = row["right_reason"]
        cell_hints[f"{idx}:1"] = row["left_hint"]["what_to_enter"]
        cell_hints[f"{idx}:2"] = row["right_hint"]["what_to_enter"]

    return {
        "id": _make_id("acct10_indigenous_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {"headers": ["Aspect", left_header, right_header], "rows": rows},
        "word_bank": word_bank,
        "correct_map": correct_map,
        "cell_teaching_map": cell_teaching_map,
        "derivation_map": derivation_map,
        "cell_hints": cell_hints,
        "guidelines": guidelines,
        "expected_answer_type": "table_wordbank",
    }


def _pricing_values(r: random.Random, difficulty: str) -> Dict[str, float]:
    if difficulty == "hard":
        cp = float(r.choice([19, 27, 34, 46, 58, 73, 89, 115]))
        markup_pct = float(r.choice([12, 18, 22, 27, 33, 45]))
    elif difficulty == "medium":
        cp = float(r.choice([18, 24, 36, 45, 55, 68, 84, 96]))
        markup_pct = float(r.choice([15, 20, 25, 30, 35, 40]))
    else:
        cp = float(r.choice([20, 25, 30, 40, 50, 60, 75, 80]))
        markup_pct = float(r.choice([10, 15, 20, 25, 30, 40]))
    return {"cp": cp, "markup_pct": markup_pct}


def _profit_values(r: random.Random, difficulty: str) -> Dict[str, float]:
    if difficulty == "hard":
        income = float(r.choice([780, 920, 1050, 1240, 1380]))
        cost_of_sales = float(r.choice([310, 365, 440, 520, 610]))
        expenses = float(r.choice([85, 110, 135, 160, 185]))
    elif difficulty == "medium":
        income = float(r.choice([520, 650, 780, 900, 1020]))
        cost_of_sales = float(r.choice([190, 240, 310, 360, 420]))
        expenses = float(r.choice([45, 60, 75, 90, 120]))
    else:
        income = float(r.choice([300, 400, 500, 600, 750]))
        cost_of_sales = float(r.choice([120, 160, 200, 240, 300]))
        expenses = float(r.choice([20, 30, 40, 50, 60]))
    return {"income": income, "cost_of_sales": cost_of_sales, "expenses": expenses}


def _q_informal_characteristics(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Which statement best describes many informal businesses?",
        [
            "They normally depend on large credit sales and detailed ledgers from the start.",
            "They often trade mainly for cash, keep simple records and hold limited stock.",
            "They always appoint separate accounting departments before trading.",
            "They may only operate if they use full GAAP statements every day.",
        ],
        1,
        "Many informal businesses are small, cash-focused and keep limited records because they work with limited capital and simple trading systems.",
    )


def _q_informal_difference(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Explain ONE clear difference between informal (indigenous) bookkeeping and formal bookkeeping.",
        "Informal bookkeeping is simple and survival-focused, often using cash transactions with minimal records. Formal bookkeeping follows consistent policies and standards, records transactions systematically and supports reporting and decision-making.",
        [
            "State that informal bookkeeping is simple, cash-based or uses minimal records.",
            "State that formal bookkeeping is structured, controlled or based on recognised standards.",
        ],
        [
            "Describe one feature of informal bookkeeping.",
            "Contrast it with one feature of formal bookkeeping.",
        ],
    )


def _q_informal_wordbank(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rows = [
        {
            "label": "Sales method",
            "left": "Mostly cash sales",
            "right": "Cash and credit sales recorded",
            "left_hint": _teach("A cash-only style of selling", "Think about how small traders collect money", "Choose the phrase showing immediate cash collection", "Informal traders often avoid debtors records"),
            "right_hint": _teach("A system recording both cash and credit sales", "Look for the option that needs more records", "Formal systems can track cash and debtors", "Formal books support source documents and ledgers"),
            "left_reason": "Small informal traders often prefer cash sales because it is simpler and reduces unpaid debt risk.",
            "right_reason": "Formal businesses commonly record both cash and credit sales because they keep structured customer records.",
        },
        {
            "label": "Record keeping",
            "left": "Minimal records",
            "right": "Structured journals and ledgers",
            "left_hint": _teach("A basic or limited record system", "Think about the simplest system", "Choose the phrase showing few records", "Informal bookkeeping focuses on simple control"),
            "right_hint": _teach("A formal set of books", "Find the phrase with journals and ledgers", "Formal bookkeeping uses recognised books and procedures", "Used for reporting and internal control"),
            "left_reason": "Informal businesses often keep only the records needed to trade day to day.",
            "right_reason": "Formal bookkeeping uses journals and ledgers to provide reliable, organised financial information.",
        },
        {
            "label": "Stock handling",
            "left": "Low stock levels",
            "right": "Stock records and reorder planning",
            "left_hint": _teach("Limited stock kept on hand", "Think about capital and storage limits", "Informal traders often buy smaller quantities", "Low stock reduces cash tied up in goods"),
            "right_hint": _teach("A planned stock system", "Find the option about records and planning", "Formal businesses monitor stock systematically", "Stock records support control and reordering"),
            "left_reason": "Informal traders often keep small quantities because capital and storage space are limited.",
            "right_reason": "Formal businesses use stock records and reorder planning to maintain control over inventory.",
        },
    ]
    return _wordbank(
        "Place each phrase into the correct column to compare informal and formal bookkeeping.",
        "Informal bookkeeping",
        "Formal bookkeeping",
        rows,
        [
            "Informal bookkeeping is usually simpler and more cash-focused.",
            "Formal bookkeeping uses structured records and stronger control systems.",
        ],
    )


def _q_resource_stock(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Why do many informal businesses keep stock levels low?",
        [
            "Because stock is not important in a trading business.",
            "Because limited capital and storage space make it risky to keep too much stock.",
            "Because informal traders are not allowed to buy stock in bulk.",
            "Because low stock always increases profit automatically.",
        ],
        1,
        "Limited capital and limited storage space are major reasons why informal traders often keep stock levels low.",
    )


def _q_resource_controls(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Give TWO practical ways an informal trader can protect cash, stock or equipment.",
        "The trader can count and record cash daily, store money safely after trading, check stock regularly, buy only what can be sold soon, and protect equipment from theft or damage.",
        [
            "Mention one practical control over cash, stock or equipment.",
            "Mention a second practical control or protection step.",
        ],
        [
            "Think about security, storage and simple daily control.",
            "Use realistic examples from a small trading business.",
        ],
    )


def _q_resource_table(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _table(
        "Complete the table to show how an informal trader can manage key resources.",
        ["Resource to manage", "Practical action"],
        [["Cash collected each day", ""], ["Stock bought for resale", ""], ["Equipment or trading stall items", ""]],
        "Cash collected each day - Count and record cash daily, then store it safely.\nStock bought for resale - Buy realistic quantities, check stock often and avoid waste.\nEquipment or trading stall items - Store safely, clean and repair when needed.",
        [
            {"label": "Cash collected each day", "value": "Record the money collected and keep it safe after trading."},
            {"label": "Stock bought for resale", "value": "Buy enough to trade but avoid tying up too much money in slow-moving stock."},
            {"label": "Equipment or trading stall items", "value": "Protect equipment from theft or damage and keep it usable."},
        ],
        [
            "Give one realistic action for each resource.",
            "Focus on simple control steps a small trader can actually use.",
        ],
    )


def _q_resource_capital(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "How do most informal traders get the capital to start their business?",
        [
            "They borrow large loans from banks before trading.",
            "They use their own savings or money from family and use daily income to buy stock for the next day.",
            "They receive government grants that cover all start-up costs.",
            "They sell fixed assets such as buildings and vehicles to raise capital.",
        ],
        1,
        "Most informal traders start with limited personal savings or help from family. They then use each day's income to buy stock for the next day, keeping the business going with minimal outside capital.",
    )


def _q_resource_inventory_advantage(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "What is ONE advantage of an informal trader keeping low inventory?",
        [
            "The trader never has to worry about running out of goods.",
            "Stock is always fresh and customers can buy in small affordable amounts.",
            "Low inventory means the trader always makes the highest possible profit.",
            "The trader can store unlimited goods in a large warehouse.",
        ],
        1,
        "An advantage of low inventory is that stock (such as vegetables) stays fresh, and customers can buy small quantities that suit their budget.",
    )


def _q_resource_fixed_assets(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Why do informal businesses usually have very few fixed assets?",
        [
            "They are not legally allowed to own fixed assets.",
            "They have limited capital and often only need a table, basic tools or equipment already owned by the owner.",
            "Fixed assets are only useful for businesses that sell on credit.",
            "The government takes all fixed assets from informal traders.",
        ],
        1,
        "Informal businesses typically have limited capital and may only need a table or basic tools. They often use assets the owner already owns, such as a sewing machine or a wheelbarrow.",
    )


def _q_resource_daily_cycle(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Explain how an informal trader typically uses each day's income to keep the business running.",
        "The trader earns income from daily sales. From this income, the trader sets aside enough money to buy stock for the next day. Any remaining money may cover small daily expenses such as transport, food or a trading licence. What is left after all costs is the trader's profit for the day, which is used for personal survival.",
        [
            "State that daily income is used to buy stock for the next trading day.",
            "Mention that remaining money covers daily expenses or becomes profit for the owner.",
        ],
        [
            "Think about the cycle of earning and spending in a small cash-based business.",
            "Consider what happens to income after stock is replaced.",
        ],
    )


def _q_resource_cash_management(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Why is it important for an informal trader to count and record cash at the end of each trading day? Give TWO reasons.",
        "Counting and recording cash helps the trader know how much was earned for the day so they can decide how much to spend on stock and how much is profit. It also helps the trader notice if money is missing, which is a basic form of internal control over the business's most important resource.",
        [
            "Mention that daily cash counting helps determine income or profit for the day.",
            "Mention that recording cash provides basic internal control or helps detect missing money.",
        ],
        [
            "Think about how knowing daily cash helps with planning the next day.",
            "Think about how records help protect the business.",
        ],
    )


def _q_resource_wordbank(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rows = [
        {
            "label": "Capital",
            "left": "Limited personal savings; use daily income to restock",
            "right": "May borrow from financial institutions; formal capital structure",
            "left_hint": _teach("A small amount of start-up money from personal sources", "Think about how informal traders fund their business", "Informal capital is usually very limited", "Informal traders rely on daily income to continue trading"),
            "right_hint": _teach("A structured approach to funding the business", "Formal businesses have more funding options", "Formal capital can include bank loans", "Formal businesses may have shareholders or investors"),
            "left_reason": "Informal traders usually start with their own small savings and depend on daily sales income to buy stock for the next day.",
            "right_reason": "Formal businesses can access bank loans, investors and other structured funding sources to grow their capital.",
        },
        {
            "label": "Stock / Inventory",
            "left": "Low inventory; buy just enough for one day of trading",
            "right": "Larger inventory; keep stock records and plan reordering",
            "left_hint": _teach("A minimal approach to keeping goods for sale", "Think about storage space and capital limits", "Informal traders buy small quantities daily", "Low stock means stock is always fresh"),
            "right_hint": _teach("A planned approach to keeping goods for sale", "Formal businesses have storage facilities", "Stock records help track what is sold and what needs replacing", "Reorder points prevent stockouts"),
            "left_reason": "Informal traders keep low stock because they have limited capital and storage space, buying just enough for each day.",
            "right_reason": "Formal businesses keep larger inventory and use stock records to plan reordering and avoid running out of goods.",
        },
        {
            "label": "Fixed Assets",
            "left": "Very few assets; maybe a table or basic tools",
            "right": "Many assets; keep a fixed asset register",
            "left_hint": _teach("Minimal equipment needed to trade", "Think about what an informal trader actually needs", "A table, umbrella or basic tools may be enough", "Assets are often already owned by the owner"),
            "right_hint": _teach("A structured approach to tracking business assets", "Formal businesses invest in equipment, vehicles and property", "A fixed asset register records all assets", "Depreciation is calculated on fixed assets"),
            "left_reason": "Informal traders need very few fixed assets — often just a table, basic tools, or equipment they already own.",
            "right_reason": "Formal businesses may own many fixed assets and must keep a fixed asset register to track them and calculate depreciation.",
        },
    ]
    return _wordbank(
        "Match each resource description to the correct type of business system.",
        "Informal business",
        "Formal business",
        rows,
        [
            "Informal businesses manage resources with very limited capital and simple systems.",
            "Formal businesses have structured systems for managing capital, stock and fixed assets.",
        ],
    )




def _q_planning_demand(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Which factor is most important when choosing a product for a small informal business?",
        [
            "Whether the owner likes the product even if nobody wants to buy it.",
            "Whether there is customer demand and the trader can buy stock or inputs at a realistic cost.",
            "Whether the product is the most expensive item available.",
            "Whether the product requires the biggest possible start-up loan.",
        ],
        1,
        "A good business idea should match customer demand and be realistic for the trader's available resources and costs.",
    )


def _q_planning_points(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "List TWO points a learner should think about when planning an informal business.",
        "A learner should think about what product or service customers in the area need, how much start-up capital is available, where the business will trade, who will supply goods, and what daily expenses are likely.",
        [
            "Mention demand, customers, location or product choice.",
            "Mention capital, suppliers, daily expenses or other planning resources.",
        ],
        [
            "Think about demand first.",
            "Also think about money, stock and place of trade.",
        ],
    )


def _q_planning_table(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _table(
        "Complete a simple planning table for an informal trading business.",
        ["Planning area", "Your answer"],
        [["Product or service to sell", ""], ["Expected customers", ""], ["Start-up resources needed", ""], ["How the trader will price the goods or service", ""]],
        "Product or service to sell - A realistic good or service that local customers need.\nExpected customers - People in the area such as commuters, learners or households.\nStart-up resources needed - Small capital, stock, equipment and a safe trading space.\nHow the trader will price the goods or service - Start with cost price, include expenses and add a fair mark-up.",
        [
            {"label": "Product or service to sell", "value": "Choose something realistic for the local area."},
            {"label": "Expected customers", "value": "Identify who will buy the product or service."},
            {"label": "Start-up resources needed", "value": "Mention money, stock, equipment or a place to trade."},
            {"label": "Pricing", "value": "Price should cover cost and contribute to profit."},
        ],
        [
            "Choose a realistic informal business idea.",
            "Show that pricing should cover cost and a profit margin.",
        ],
    )


def _q_formula_mcq(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Which formula is correct when mark-up is added to cost price?",
        ["SP = CP + mark-up", "CP = SP + mark-up", "Mark-up = CP + SP", "SP = CP ÷ mark-up"],
        0,
        "Selling price is found by adding the mark-up to the cost price.",
    )


def _q_selling_price(r: random.Random, difficulty: str) -> Dict[str, Any]:
    values = _pricing_values(r, difficulty)
    cp = values["cp"]
    pct = values["markup_pct"]
    markup = _round_money(cp * pct / 100.0)
    sp = _round_money(cp + markup)
    return _calc(
        f"A trader buys goods for R{cp:.2f}. The mark-up is {pct:.0f}% on cost price. Calculate the selling price.",
        sp,
        "R",
        "SP = CP + (CP × Mark-up%)",
        "First calculate the mark-up amount from the cost price, then add it to the cost price.",
        {"Cost price": f"R{cp:.2f}", "Mark-up amount": f"R{markup:.2f}", "Selling price": f"R{sp:.2f}"},
    )


def _q_cost_price(r: random.Random, difficulty: str) -> Dict[str, Any]:
    values = _pricing_values(r, difficulty)
    cp = values["cp"]
    pct = values["markup_pct"]
    sp = _round_money(cp * (1.0 + pct / 100.0))
    return _calc(
        f"A trader sells an item for R{sp:.2f}. The mark-up is {pct:.0f}% on cost price. Calculate the cost price.",
        cp,
        "R",
        "CP = SP ÷ (1 + Mark-up%)",
        "Convert the mark-up percentage to a multiplier before dividing the selling price.",
        {"Selling price": f"R{sp:.2f}", "Multiplier": f"1 + {pct:.0f}/100 = {1 + pct / 100.0:.2f}", "Cost price": f"R{cp:.2f}"},
    )


def _q_markup_amount(r: random.Random, difficulty: str) -> Dict[str, Any]:
    values = _pricing_values(r, difficulty)
    cp = values["cp"]
    pct = values["markup_pct"]
    sp = _round_money(cp * (1.0 + pct / 100.0))
    markup = _round_money(sp - cp)
    return _calc(
        f"A trader buys goods for R{cp:.2f} and sells them for R{sp:.2f}. Calculate the mark-up amount.",
        markup,
        "R",
        "Mark-up amount = SP - CP",
        "Subtract the cost price from the selling price to find the mark-up amount.",
        {"Selling price": f"R{sp:.2f}", "Cost price": f"R{cp:.2f}", "Mark-up amount": f"R{markup:.2f}"},
    )


def _q_profit_loss(r: random.Random, difficulty: str) -> Dict[str, Any]:
    values = _profit_values(r, difficulty)
    income = values["income"]
    cost_of_sales = values["cost_of_sales"]
    expenses = values["expenses"]
    profit = _round_money(income - cost_of_sales - expenses)
    return _calc(
        f"An informal trader made sales of R{income:.2f} for the day. The cost of goods sold was R{cost_of_sales:.2f} and other expenses were R{expenses:.2f}. Calculate the profit or loss for the day.",
        profit,
        "R",
        "Profit/Loss = Income - Cost of Sales - Expenses",
        "Start with sales income, subtract cost of sales, then subtract the remaining operating expenses.",
        {"Income": f"R{income:.2f}", "Cost of sales": f"R{cost_of_sales:.2f}", "Expenses": f"R{expenses:.2f}", "Profit/Loss": f"R{profit:.2f}"},
    )


def _q_labour_costs(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Explain why a small trader must separate labour costs, income and other expenses when checking if the business is doing well.",
        "A trader must separate labour costs, income and other expenses so that the real profit can be seen clearly. If wages or help paid are mixed with stock costs or personal spending, the owner cannot judge whether the business is covering its costs and earning enough.",
        [
            "State that income must be compared with costs and expenses to find real profit.",
            "State that keeping categories separate improves control or decision-making.",
        ],
        [
            "Think about how profit is measured.",
            "Explain why mixed-up records make decisions harder.",
        ],
    )


def _q_labour_expense_mcq(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Which item is an operating expense rather than cost of sales for a small trader?",
        ["The amount paid to buy the goods sold", "Transport paid to bring stock for resale", "Money paid to a helper for the day", "The cost price of the items sold"],
        2,
        "A helper's daily pay is an operating expense. Cost of sales relates to the goods that were bought and then sold.",
    )


def _q_compare_advantage(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "State ONE advantage of formal bookkeeping over informal bookkeeping.",
        "Formal bookkeeping gives the owner better control over income, expenses, stock and debts because records are structured and can be used for reporting, decision-making and accountability.",
        [
            "Mention better control, structure or reliability of records.",
            "Mention a use such as reporting, decisions, accountability or tax.",
        ],
        [
            "Focus on why structured records help the business owner.",
            "Connect the advantage to decisions, reporting or control.",
        ],
    )


def _q_compare_wordbank(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rows = [
        {
            "label": "Business control",
            "left": "Owner checks trading with simple daily notes",
            "right": "Owner uses formal reports and ledgers",
            "left_hint": _teach("A simple way of checking business activity", "Look for the phrase with notes instead of full reports", "Informal control is usually basic and short-term", "Simple notes help with day-to-day survival decisions"),
            "right_hint": _teach("A structured system of control", "Look for reports and ledgers", "Formal systems rely on prepared records and summaries", "Formal reports support analysis and accountability"),
            "left_reason": "Informal businesses often use quick notes or memory-based checks to keep trading going.",
            "right_reason": "Formal businesses use reports and ledgers to measure performance and support decisions.",
        },
        {
            "label": "Credit management",
            "left": "Limited or no debtor tracking",
            "right": "Debtor balances can be tracked",
            "left_hint": _teach("A weak credit-record system", "Look for the option showing little tracking", "Informal traders often avoid or limit credit", "Without debtor records, credit control is difficult"),
            "right_hint": _teach("A formal credit-control feature", "Find the option about tracking balances", "Formal bookkeeping supports debtor control", "Customer balances can be followed up"),
            "left_reason": "Informal traders often avoid complex credit because it needs extra records and follow-up.",
            "right_reason": "Formal bookkeeping allows the business to record and monitor customer balances properly.",
        },
        {
            "label": "Decision-making",
            "left": "Decisions often based on immediate cash needs",
            "right": "Decisions informed by organised financial information",
            "left_hint": _teach("Short-term cash-based decision making", "Think about survival trading", "Choose the phrase tied to immediate money needs", "Informal traders may focus on daily cash flow"),
            "right_hint": _teach("A planned information-based approach", "Look for organised financial information", "Formal records support measured business decisions", "Profit, expenses and trends can be analysed"),
            "left_reason": "Informal traders may make decisions quickly based on daily cash available and urgent needs.",
            "right_reason": "Formal systems make it easier to compare performance and plan future decisions from reliable data.",
        },
    ]
    return _wordbank(
        "Match each phrase to the correct column to compare informal and formal business systems.",
        "Informal system",
        "Formal system",
        rows,
        [
            "Informal systems often focus on immediate trading needs.",
            "Formal systems support stronger reporting, credit control and planning.",
        ],
    )



def _q_pricing_wordbank(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rows = [
        {
            "label": "Cost Price",
            "left": "The amount paid to suppliers to buy the goods",
            "right": "Always the highest value in a profitable sale",
            "left_hint": _teach("What the trader pays", "Think about buying goods", "Cost relates to the supplier price", "Cost price is the foundation before mark-up"),
            "right_hint": _teach("Incorrect definition", "Cost is lower than selling price", "This is meant as a distractor", "Selling price is the highest value"),
            "left_reason": "Cost price is what the business pays to acquire the items for resale.",
            "right_reason": "Cost price must be lower than selling price to make a profit.",
        },
        {
            "label": "Mark-up",
            "left": "The amount added to the cost to make a profit",
            "right": "The total money received from customers",
            "left_hint": _teach("The profit portion", "Look for adding to cost", "Mark-up is the profit amount", "Mark-up is usually a percentage of cost"),
            "right_hint": _teach("Incorrect definition", "Total money received is sales", "This describes selling price", "Mark-up is just a part of the selling price"),
            "left_reason": "Mark-up is the extra amount added to cover expenses and generate profit.",
            "right_reason": "Selling price is the total money received, not the mark-up alone.",
        },
    ]
    return _wordbank(
        "Match the pricing concept with its correct description (Note: some options are incorrect/distractors).",
        "Correct Description",
        "Incorrect Description",
        rows,
        ["Identify the correct description for Cost Price and Mark-up."]
    )

def _q_pricing_explain(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Explain the difference between Cost Price and Selling Price.",
        "Cost price is what the trader pays to buy the goods from a supplier. Selling price is the amount the customer pays to the trader, which includes the cost price plus the mark-up (profit).",
        ["Define Cost Price as the amount paid to suppliers.", "Define Selling Price as the amount paid by the customer or Cost Price + Mark-up."],
    )

def _q_pricing_external_factor(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "If the supplier increases the cost price of goods, what must an informal trader normally do to keep the same profit margin?",
        [
            "Decrease the selling price to attract more buyers.",
            "Keep the selling price exactly the same and absorb the loss.",
            "Increase the selling price so the mark-up covers the higher cost.",
            "Stop selling the goods immediately.",
        ],
        2,
        "To maintain the same profit margin on a higher cost price, the trader must increase the selling price."
    )

def _q_labour_wordbank(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rows = [
        {
            "label": "Wages for a stall cleaner",
            "left": "Operating Expense",
            "right": "Cost of Sales",
            "left_hint": _teach("A daily running cost", "Think about general expenses", "Cleaners do not make the product", "General helper wages are operating expenses"),
            "right_hint": _teach("Incorrect classification", "Cost of sales is for goods", "Cleaners are indirect labour", "Cost of sales is for inventory"),
            "left_reason": "Cleaning wages are an indirect operating expense to keep the business running.",
            "right_reason": "Cost of sales only applies to the direct cost of the goods sold.",
        },
        {
            "label": "Money from selling products",
            "left": "Income (Sales)",
            "right": "Operating Expense",
            "left_hint": _teach("Money coming in", "Think about revenue", "Sales generate income", "Selling goods is the main income source"),
            "right_hint": _teach("Incorrect classification", "Expenses are money going out", "Sales bring money in", "Income is positive cash flow"),
            "left_reason": "Money received from selling goods is classified as sales income.",
            "right_reason": "Expenses are costs, not incoming money.",
        },
    ]
    return _wordbank(
        "Classify these transactions correctly for an informal business.",
        "Correct Classification",
        "Incorrect Classification",
        rows,
        ["Determine whether each item is an Income, Cost of Sales, or Operating Expense."]
    )

def _q_direct_indirect_explain(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _typed(
        "Give one example of direct labour and one example of indirect labour in a small business.",
        "Direct labour: A person who physically makes the beaded jewelry to sell. Indirect labour: A person hired to sweep the floor or act as a security guard.",
        ["Provide a valid example of direct labour (making the product).", "Provide a valid example of indirect labour (support/cleaning)."],
    )

def _q_calc_expenses_from_profit(r: random.Random, difficulty: str) -> Dict[str, Any]:
    values = _profit_values(r, difficulty)
    income = values["income"]
    cost_of_sales = values["cost_of_sales"]
    expenses = values["expenses"]
    profit = _round_money(income - cost_of_sales - expenses)
    return _calc(
        f"An informal trader made R{income:.2f} in sales today. The cost of those goods was R{cost_of_sales:.2f}. At the end of the day, the profit was R{profit:.2f}. Calculate the total operating expenses for the day.",
        expenses,
        "R",
        "Expenses = Income - Cost of Sales - Profit",
        "Subtract Cost of Sales and Profit from the Income to find the remaining Expenses.",
        {"Income": f"R{income:.2f}", "Cost of sales": f"R{cost_of_sales:.2f}", "Profit": f"R{profit:.2f}", "Expenses": f"R{expenses:.2f}"},
    )

def _q_informal_credit_mcq(r: random.Random, difficulty: str) -> Dict[str, Any]:
    return _mcq(
        "Why do informal traders often avoid selling on credit?",
        [
            "Because selling on credit is illegal.",
            "Because they have limited cash flow and cannot afford the risk of bad debts.",
            "Because credit sales do not generate profit.",
            "Because GAAP requires formal businesses to take all credit sales.",
        ],
        1,
        "Informal traders need cash to buy stock for the next day. Selling on credit ties up their limited capital and carries the risk of non-payment."
    )

def _build_pools() -> Dict[str, List[Callable[[random.Random, str], Dict[str, Any]]]]:
    return {
        "informal_vs_formal": [_q_informal_characteristics, _q_informal_difference, _q_informal_wordbank, _q_compare_advantage, _q_compare_wordbank, _q_informal_credit_mcq],
        "resource_management": [_q_resource_stock, _q_resource_controls, _q_resource_table, _q_resource_capital, _q_resource_inventory_advantage, _q_resource_fixed_assets, _q_resource_daily_cycle, _q_resource_cash_management, _q_resource_wordbank],
        "business_planning": [_q_planning_demand, _q_planning_points, _q_planning_table],
        "pricing_and_markup": [_q_formula_mcq, _q_selling_price, _q_cost_price, _q_markup_amount, _q_pricing_wordbank, _q_pricing_explain, _q_pricing_external_factor],
        "labour_income_expenses": [_q_profit_loss, _q_labour_costs, _q_labour_expense_mcq, _q_labour_wordbank, _q_direct_indirect_explain, _q_calc_expenses_from_profit],
    }


def _builder_question_type(builder: Callable[[random.Random, str], Dict[str, Any]]) -> str:
    mapping = {
        "_q_informal_characteristics": "mcq",
        "_q_informal_difference": "typed",
        "_q_informal_wordbank": "table_wordbank",
        "_q_resource_stock": "mcq",
        "_q_resource_controls": "typed",
        "_q_resource_table": "table",
        "_q_resource_capital": "mcq",
        "_q_resource_inventory_advantage": "mcq",
        "_q_resource_fixed_assets": "mcq",
        "_q_resource_daily_cycle": "typed",
        "_q_resource_cash_management": "typed",
        "_q_resource_wordbank": "table_wordbank",
        "_q_planning_demand": "mcq",
        "_q_planning_points": "typed",
        "_q_planning_table": "table",
        "_q_formula_mcq": "mcq",
        "_q_selling_price": "calc",
        "_q_cost_price": "calc",
        "_q_markup_amount": "calc",
        "_q_profit_loss": "calc",
        "_q_labour_costs": "typed",
        "_q_labour_expense_mcq": "mcq",
        "_q_compare_advantage": "typed",
        "_q_compare_wordbank": "table_wordbank",
        "_q_pricing_wordbank": "table_wordbank",
        "_q_pricing_explain": "typed",
        "_q_pricing_external_factor": "mcq",
        "_q_labour_wordbank": "table_wordbank",
        "_q_direct_indirect_explain": "typed",
        "_q_calc_expenses_from_profit": "calc",
        "_q_informal_credit_mcq": "mcq",
    }
    return mapping.get(getattr(builder, "__name__", ""), "mixed")


def _validate_question(question: Dict[str, Any]) -> bool:
    try:
        if not question.get("id") or not question.get("prompt") or not question.get("question_type"):
            return False
        qtype = question["question_type"]
        if qtype == "mcq":
            options = question.get("options") or []
            correct_index = question.get("correct_index")
            if len(options) < 2 or not isinstance(correct_index, int) or correct_index >= len(options):
                return False
        elif qtype == "typed":
            if not str(question.get("sample_answer") or "").strip():
                return False
        elif qtype == "calc":
            if not isinstance(question.get("correct_value"), (int, float)):
                return False
        elif qtype == "table":
            table = question.get("table") or {}
            if not isinstance(table.get("headers"), list) or not isinstance(table.get("rows"), list):
                return False
        elif qtype == "table_wordbank":
            if not question.get("word_bank") or not question.get("correct_map"):
                return False
        else:
            return False
        return True
    except Exception:
        return False


def _finalize(question: Dict[str, Any], subskill: str, difficulty: str) -> Optional[Dict[str, Any]]:
    question["subskill"] = subskill
    question["difficulty"] = difficulty
    if _validate_question(question):
        return question
    return None


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    resolved_subskill = _normalize_subskill(subskill)
    resolved_question_type = _normalize_question_type(question_type)
    resolved_difficulty = str(difficulty or "easy").strip().lower() or "easy"

    requested_count = int(count) if isinstance(count, int) else int(str(count or 1))
    requested_count = max(1, min(20, requested_count))

    pools = _build_pools()
    selected_subskills = list(SUBSKILLS) if resolved_subskill == "mixed" else [resolved_subskill]
    builders: List[tuple[str, Callable[[random.Random, str], Dict[str, Any]]]] = []
    for key in selected_subskills:
        builders.extend((key, builder) for builder in pools.get(key, []))

    if resolved_question_type != "mixed":
        builders = [item for item in builders if _builder_question_type(item[1]) == resolved_question_type]

    if not builders:
        return []

    generated: List[Dict[str, Any]] = []
    seen = set()
    attempts = 0
    max_attempts = max(requested_count * 10, 40)

    while len(generated) < requested_count and attempts < max_attempts:
        attempts += 1
        actual_subskill, builder = r.choice(builders)
        try:
            q_raw = builder(r, resolved_difficulty)
            question = _finalize(q_raw, actual_subskill, resolved_difficulty)
        except Exception:
            question = None
        if question is None:
            continue
        signature = _signature(question)
        if signature in seen and len(builders) > 1:
            continue
        seen.add(signature)
        generated.append(question)

    # Fallback to avoid infinite loop if still short (can duplicate)
    fallback_attempts = 0
    while len(generated) < requested_count and fallback_attempts < 20:
        fallback_attempts += 1
        actual_subskill, builder = r.choice(builders)
        try:
            q_raw = builder(r, resolved_difficulty)
            question = _finalize(q_raw, actual_subskill, resolved_difficulty)
        except Exception:
            question = None
        if question:
            generated.append(question)

    return generated[:requested_count]
