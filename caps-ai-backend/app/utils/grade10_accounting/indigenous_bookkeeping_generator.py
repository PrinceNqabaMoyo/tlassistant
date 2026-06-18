from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional
from .indigenous_bookkeeping_generator_v2 import generate_questions as generate_questions_v2


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "guidelines": [explanation],
    }


def _make_typed(*, prompt: str, sample_answer: str, grading_rubric: Optional[List[str]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric or [],
        "marks": 2 if not grading_rubric else len(grading_rubric) * 2,
        "guidelines": [f"Ensure your answer includes: {', '.join(grading_rubric)}"] if grading_rubric else [],
    }


def _make_table(*, prompt: str, headers: List[str], rows: List[List[str]], guidelines: Optional[List[str]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_table"),
        "question_type": "table",
        "prompt": prompt,
        "table": {
            "headers": headers,
            "rows": rows,
        },
        "guidelines": guidelines or [],
        "expected_answer_type": "table_data",
    }


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, str]],
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {
            "headers": headers,
            "rows": rows,
        },
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_wordbank",
    }


def _make_calc(*, prompt: str, correct_value: float, unit: str = "", working_formula: str = "") -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_indigenous_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(correct_value),
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "guidelines": [f"Formula: {working_formula}"] if working_formula else [],
    }


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _calc_sp_from_cp_mu(*, r: random.Random) -> Dict[str, Any]:
    cp = r.choice([20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
    mu_pct = r.choice([10, 15, 20, 25, 30, 40, 50])
    sp = _round_money(cp * (1.0 + (mu_pct / 100.0)))
    return _make_calc(
        prompt=(
            f"A trader buys goods for R{cp:.2f} (cost price). The mark-up is {mu_pct}%. "
            f"Calculate the selling price (SP)."
        ),
        correct_value=sp,
        unit="R",
        working_formula="SP = CP + (CP * Markup%)",
    )


def _calc_cp_from_sp_mu(*, r: random.Random) -> Dict[str, Any]:
    cp = r.choice([20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
    mu_pct = r.choice([10, 15, 20, 25, 30, 40, 50])
    sp = _round_money(cp * (1.0 + (mu_pct / 100.0)))
    cp_back = _round_money(sp / (1.0 + (mu_pct / 100.0)))
    return _make_calc(
        prompt=(
            f"A trader sells an item for R{sp:.2f}. The mark-up is {mu_pct}% on cost. "
            f"Calculate the cost price (CP) / cost of sales."
        ),
        correct_value=cp_back,
        unit="R",
        working_formula="CP = SP / (1 + Markup%)",
    )


def _calc_mu_amount(*, r: random.Random) -> Dict[str, Any]:
    """Calculate mark-up amount given CP and SP."""
    cp = r.choice([20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
    mu_pct = r.choice([10, 15, 20, 25, 30, 40, 50])
    sp = _round_money(cp * (1.0 + (mu_pct / 100.0)))
    mu_amount = _round_money(sp - cp)
    return _make_calc(
        prompt=(
            f"A trader buys goods for R{cp:.2f} (cost price) and sells them for R{sp:.2f} (selling price). "
            f"Calculate the mark-up amount."
        ),
        correct_value=mu_amount,
        unit="R",
        working_formula="Markup Amount = SP - CP",
    )


def _calc_mu_pct(*, r: random.Random) -> Dict[str, Any]:
    """Calculate mark-up percentage given CP and SP."""
    cp = r.choice([20, 25, 30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
    mu_pct = r.choice([10, 15, 20, 25, 30, 40, 50])
    sp = _round_money(cp * (1.0 + (mu_pct / 100.0)))
    mu_pct_back = _round_money(((sp - cp) / cp) * 100)
    return _make_calc(
        prompt=(
            f"A trader buys goods for R{cp:.2f} and sells them for R{sp:.2f}. "
            f"Calculate the mark-up percentage on cost price."
        ),
        correct_value=mu_pct_back,
        unit="%",
        working_formula="Markup % = (Markup Amount / CP) * 100",
    )


def _calc_profit_or_loss(*, r: random.Random) -> Dict[str, Any]:
    """Calculate daily profit/loss given income and expenses."""
    income = r.choice([200, 300, 400, 500, 600, 750, 800, 1000, 1200, 1500])
    cos = r.randint(int(income * 0.3), int(income * 0.6))
    expenses = r.choice([20, 30, 40, 50, 60, 80, 100, 120])
    profit = _round_money(income - cos - expenses)
    return _make_calc(
        prompt=(
            f"An informal trader earns R{income:.2f} in sales for the day. "
            f"The cost of the goods sold was R{cos:.2f} and other expenses were R{expenses:.2f}. "
            f"Calculate the trader's profit (or loss) for the day."
        ),
        correct_value=profit,
        unit="R",
        working_formula="Profit/Loss = Income - Cost of Sales - Expenses",
    )


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    concepts_pool: List[Dict[str, Any]] = []
    activity1_pool: List[Dict[str, Any]] = []
    activity2_pool: List[Dict[str, Any]] = []

    concepts_pool.append(
        _make_mcq(
            prompt="Which statement best describes many informal businesses?",
            options=[
                "They usually buy and sell on credit to grow quickly.",
                "They often buy stock cash and sell mostly for cash with low inventory.",
                "They always keep large inventory to avoid stockouts.",
                "They must keep a fixed asset register for all assets.",
            ],
            correct_index=1,
            explanation="Many informal businesses operate cash-based with low inventory due to limited capital and storage.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="In a trading business, what does 'cost of sales' mean?",
            options=[
                "The total profit made on goods sold.",
                "The price the trader paid for the goods sold (cost price).",
                "The selling price charged to customers.",
                "The wages paid to employees.",
            ],
            correct_index=1,
            explanation="Cost of sales is what the goods sold cost the trader (the cost price of those goods).",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Which formula is correct?",
            options=[
                "CP + MU = SP",
                "SP + MU = CP",
                "MU + Profit = CP",
                "CP \u00d7 MU = SP always",
            ],
            correct_index=0,
            explanation="Selling price equals cost price plus mark-up.",
        )
    )

    concepts_pool.append(
        _make_typed(
            prompt="Explain ONE difference between informal (indigenous) bookkeeping and formal bookkeeping.",
            sample_answer="Informal bookkeeping is simple and survival-focused (often cash-only and minimal records), while formal bookkeeping follows consistent policies and standards (e.g. GAAP) with structured records.",
            grading_rubric=["Informal is simple/cash-only", "Formal follows standards like GAAP"],
        )
    )

    # --- Three branches of formal accounting ---

    concepts_pool.append(
        _make_mcq(
            prompt="Accounting activities in a formal business are divided into three groups. Which of the following is NOT one of them?",
            options=[
                "Financial accounting",
                "Managerial accounting",
                "Tools in managing resources",
                "Informal accounting",
            ],
            correct_index=3,
            explanation="The three groups are financial accounting, managerial accounting, and tools in managing resources. Informal accounting is not one of them.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Which branch of accounting includes the recording of financial transactions and the preparation of Financial Statements?",
            options=[
                "Managerial accounting",
                "Financial accounting",
                "Tools in managing resources",
                "Indigenous bookkeeping",
            ],
            correct_index=1,
            explanation="Financial accounting includes the logical, systematic and accurate recording of financial transactions as well as the analysis, interpretation and communication of Financial Statements.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Managerial accounting puts emphasis on which of the following?",
            options=[
                "Recording daily cash transactions only.",
                "Analysis, interpretation and communication of financial and managerial information for decision-making.",
                "Keeping a fixed asset register.",
                "Calculating VAT on all sales.",
            ],
            correct_index=1,
            explanation="Managerial accounting includes concepts such as costing and budgeting, with emphasis on analysis, interpretation and communication of information for decision-making purposes.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="'Tools in managing resources' in formal accounting includes which of the following?",
            options=[
                "Basic internal controls, internal audit processes and code of ethics.",
                "Only the recording of daily sales.",
                "Calculating mark-up percentages.",
                "Buying stock from suppliers on credit.",
            ],
            correct_index=0,
            explanation="Tools in managing resources include basic internal controls, internal audit processes and code of ethics, with emphasis on knowledge, understanding and adherence to ethics.",
        )
    )

    # --- GAAP ---

    concepts_pool.append(
        _make_mcq(
            prompt="What does GAAP stand for?",
            options=[
                "Generally Accepted Accounting Practice",
                "General Audit and Accounting Principles",
                "Government Approved Accounting Procedures",
                "Gross Annual Accounting Profit",
            ],
            correct_index=0,
            explanation="GAAP stands for Generally Accepted Accounting Practice — a system of accounting concepts, principles, methods and procedures.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Why was GAAP developed?",
            options=[
                "So that each business can record financial information in its own unique way.",
                "To ensure uniform rules for recording and reporting financial information, eliminating undesirable alternatives.",
                "To allow informal businesses to avoid keeping records.",
                "To make sure only large businesses pay tax.",
            ],
            correct_index=1,
            explanation="GAAP was developed so that all businesses follow uniform rules for measurement and disclosure of financial results, to avoid chaos if each business used its own methods.",
        )
    )

    # --- Direct vs Indirect labour ---

    concepts_pool.append(
        _make_mcq(
            prompt="What is 'direct labour'?",
            options=[
                "Labour not linked to the product, such as cleaning staff.",
                "Labour that is directly involved with the production of the product.",
                "The owner's personal salary from another job.",
                "The cost of transporting goods to customers.",
            ],
            correct_index=1,
            explanation="Direct labour is labour that is directly involved with the production of the product, e.g. the person who makes the item to be sold.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Which of the following is an example of indirect labour?",
            options=[
                "The person who makes the beaded jewellery to sell.",
                "The person who sews the clothes in a clothing business.",
                "A person hired to clean the workshop or help sell products.",
                "The owner who personally manufactures each item.",
            ],
            correct_index=2,
            explanation="Indirect labour is the cost of labour not directly linked to the product produced, e.g. wages for a cleaner or a salesperson.",
        )
    )

    # --- Income ---

    concepts_pool.append(
        _make_mcq(
            prompt="In accounting, 'income' for a business refers to:",
            options=[
                "Money the owner borrows from the bank.",
                "Money that the business earns, e.g. fee income (services) or sales (goods).",
                "The total expenses of the business.",
                "The cost of goods purchased from suppliers.",
            ],
            correct_index=1,
            explanation="Income is money that the entrepreneur earns for the business. Examples include fee income (for services) or sales (for goods sold).",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="A hairdresser earns money by cutting hair. This type of income is best described as:",
            options=[
                "Sales",
                "Cost of sales",
                "Fee income",
                "Mark-up",
            ],
            correct_index=2,
            explanation="Fee income is earned for rendering a service (like cutting hair). Sales refers to income from selling goods.",
        )
    )

    # --- Expenses ---

    concepts_pool.append(
        _make_mcq(
            prompt="Which of the following is an example of a business expense?",
            options=[
                "Money received from a customer for goods sold.",
                "Capital contributed by the owner.",
                "Wages, telephone, water and electricity, or stationery costs.",
                "The selling price of goods.",
            ],
            correct_index=2,
            explanation="Expenses are amounts the entrepreneur has to spend to run the business, such as wages, salaries, telephone, water and electricity, stationery, etc.",
        )
    )

    # --- Advantages of informal businesses ---

    concepts_pool.append(
        _make_mcq(
            prompt="What is ONE advantage of an informal trader keeping low stock levels?",
            options=[
                "The trader can charge higher prices.",
                "Stock is always fresh and buyers can purchase in small amounts.",
                "The trader never needs to buy new stock.",
                "Low stock means the business makes more profit.",
            ],
            correct_index=1,
            explanation="An advantage of low stock is that stock (e.g. vegetables) is always fresh, and buyers don't have to buy large quantities.",
        )
    )

    concepts_pool.append(
        _make_mcq(
            prompt="Why do many informal businesses have few fixed assets?",
            options=[
                "They are not allowed to own assets by law.",
                "They have limited capital and may only need a table or basic tools to operate.",
                "Fixed assets are only for businesses registered with SARS.",
                "Informal businesses always rent all their equipment.",
            ],
            correct_index=1,
            explanation="Informal businesses typically have limited capital. They may only need a table or basic tools, and often use assets already owned by the owner.",
        )
    )

    # --- Indigenous vs Formal bookkeeping summary ---

    concepts_pool.append(
        _make_mcq(
            prompt="Which statement best summarises the difference between indigenous and formal bookkeeping?",
            options=[
                "Indigenous bookkeeping is easy to administer and designed by the owner; formal bookkeeping follows GAAP and accounting standards.",
                "Indigenous bookkeeping uses computers; formal bookkeeping uses paper.",
                "Both systems are identical but use different names.",
                "Formal bookkeeping has no rules; indigenous bookkeeping follows strict standards.",
            ],
            correct_index=0,
            explanation="Indigenous bookkeeping is easy to administer with simple records designed by the owner. Formal bookkeeping has a structured approach complying with GAAP principles and accounting norms.",
        )
    )

    # --- Typed questions requiring LLM evaluation ---

    concepts_pool.append(
        _make_typed(
            prompt="Explain why GAAP (Generally Accepted Accounting Practice) is important for formal businesses.",
            sample_answer="GAAP provides uniform rules for recording and reporting financial information. Without it, each business would record information differently, causing chaos. GAAP ensures consistency, comparability and reliability of financial statements.",
            grading_rubric=["uniform rules / procedures", "consistency / comparability", "reliability"],
        )
    )

    concepts_pool.append(
        _make_typed(
            prompt="Give TWO reasons why an informal business owner might choose not to use formal bookkeeping.",
            sample_answer="1. The business is small with few transactions, so formal records are unnecessary. 2. The owner may lack accounting knowledge or training and finds it easier to simply track cash in and cash out.",
            grading_rubric=["few transactions / small business", "lack of formal accounting knowledge", "easier to track just cash"],
        )
    )

    concepts_pool.append(
        _make_typed(
            prompt="Explain the difference between direct labour and indirect labour. Give ONE example of each.",
            sample_answer="Direct labour is labour directly involved in producing the product (e.g. a person who makes beaded jewellery). Indirect labour is labour not directly linked to production (e.g. a cleaner or a person who helps sell the products).",
            grading_rubric=["Direct labour creates product", "Example of direct labour", "Indirect labour does not create product", "Example of indirect labour"],
        )
    )

    activity1_items = [
        "Capital needed",
        "Income per day",
        "Expenses per day",
        "Cost of sales",
        "Selling price",
        "Labour cost",
        "Fixed assets needed",
        "Stock kept",
        "Bookkeeping",
    ]
    activity1_rows = [[item, ""] for item in activity1_items]
    activity1_guidelines = [
        "Capital: include start-up money and any asset contributed.",
        "Income per day: estimate daily cash received.",
        "Expenses per day: small daily costs (licence, wages, electricity, stationery, etc.).",
        "Cost of sales: what you pay suppliers for the goods/materials.",
        "Selling price: based on costs + expenses + margin; can be negotiable.",
        "Labour cost: often owner labour; wages if employees.",
        "Fixed assets: usually minimal (table, tools, equipment).",
        "Stock kept: low stock due to limited capital/storage.",
        "Bookkeeping: informal, may just track income minus expenses for profit.",
    ]

    activity1_pool.append(
        _make_table(
            prompt="Activity 1: Think of an informal business you would like to start. Complete the planning table.",
            headers=["Item", "Your plan"],
            rows=activity1_rows,
            guidelines=activity1_guidelines,
        )
    )

    activity1_pool.append(_calc_sp_from_cp_mu(r=r))
    activity1_pool.append(_calc_cp_from_sp_mu(r=r))
    activity1_pool.append(_calc_mu_amount(r=r))
    activity1_pool.append(_calc_mu_pct(r=r))
    activity1_pool.append(_calc_profit_or_loss(r=r))

    compare_headings = [
        "Capital",
        "Fixed assets",
        "Inventory",
        "Selling price",
        "Cost of sales",
        "Labour cost",
        "Income",
        "Expenses",
        "Credit transactions",
        "Bookkeeping",
    ]

    shuffled = compare_headings[:]
    r.shuffle(shuffled)
    picked = shuffled[:6]

    activity2_rows = [[h, "", ""] for h in picked]

    compare_phrases = {
        "Capital": {
            "informal": "Owner's own funds; borrowing limited.",
            "formal": "May borrow from financial institutions; depends on business.",
        },
        "Fixed assets": {
            "informal": "Little or no fixed assets.",
            "formal": "Can have many fixed assets; keep a fixed asset register.",
        },
        "Inventory": {
            "informal": "Low inventory; limited storage space.",
            "formal": "Usually has storage; inventory depends on size of business.",
        },
        "Selling price": {
            "informal": "Changes quickly; owner decides; mostly cash sales.",
            "formal": "Cost + profit margin; less changeable; cash and credit sales.",
        },
        "Cost of sales": {
            "informal": "Goods are bought for cash.",
            "formal": "Goods can be bought for cash and on credit.",
        },
        "Labour cost": {
            "informal": "Owner often does the labour; wages if a few workers.",
            "formal": "Employees may be registered; deductions (UIF/SARS) apply.",
        },
        "Income": {
            "informal": "Cash basis; income is easy to determine.",
            "formal": "Cash discounts and bad debts can affect cash received.",
        },
        "Expenses": {
            "informal": "Few overheads; mostly cash expenses.",
            "formal": "Higher overheads; expenses can be cash and credit.",
        },
        "Credit transactions": {
            "informal": "Normally no credit transactions.",
            "formal": "Can buy and sell on credit; risk of bad debts.",
        },
        "Bookkeeping": {
            "informal": "No formal bookkeeping; minimal records.",
            "formal": "Formal bookkeeping due to tax/standards requirements.",
        },
    }

    distractors = [
        "Prices never change because GAAP fixes them.",
        "Inventory is always huge to avoid stockouts.",
        "All sales must include VAT by default.",
        "No one needs to keep records in formal businesses.",
        "All informal businesses sell mostly on credit.",
        "Cost of sales means the profit made on sales.",
    ]

    def _wb_item(text: str) -> Dict[str, str]:
        return {"id": _make_id("wb"), "text": text, "label": text}

    correct_map: Dict[str, Dict[str, str]] = {}
    word_bank_items: List[Dict[str, str]] = []

    for row_idx, heading in enumerate(picked):
        phrases = compare_phrases.get(heading)
        if not phrases:
            continue
        informal_id = _make_id("wb")
        formal_id = _make_id("wb")
        word_bank_items.append({"id": informal_id, "text": phrases["informal"], "label": phrases["informal"]})
        word_bank_items.append({"id": formal_id, "text": phrases["formal"], "label": phrases["formal"]})
        correct_map[str(row_idx)] = {"1": informal_id, "2": formal_id}

    r.shuffle(distractors)
    for d in distractors[: max(3, len(picked) // 2)]:
        word_bank_items.append(_wb_item(d))

    r.shuffle(word_bank_items)
    activity2_pool.append(
        _make_table_wordbank(
            prompt="Select a phrase from the word bank, then place it into the correct Informal or Formal column.",
            headers=["Heading", "Informal", "Formal"],
            rows=[[h, "", ""] for h in picked],
            word_bank=word_bank_items,
            correct_map=correct_map,
            guidelines=[
                "Pick one phrase from the word bank and place it into the correct column.",
                "Each row needs one Informal phrase and one Formal phrase.",
            ],
        )
    )

    activity2_pool.append(
        _make_mcq(
            prompt="In general, which is true about selling price in many informal businesses?",
            options=[
                "It changes quickly depending on cost and the owner's decision.",
                "It is fixed for the whole year by GAAP.",
                "It must always include VAT.",
                "It is always the same as cost of sales.",
            ],
            correct_index=0,
            explanation="In informal trading, prices may change often depending on purchase price and owner's choices.",
        )
    )

    activity2_pool.append(
        _make_mcq(
            prompt="Which statement best compares informal vs formal credit transactions?",
            options=[
                "Informal: mostly cash; Formal: can buy/sell on credit.",
                "Informal: mostly credit; Formal: cash only.",
                "Both are always cash only.",
                "Both must sell on credit to be sustainable.",
            ],
            correct_index=0,
            explanation="Informal businesses are often cash-based; formal businesses often trade on both cash and credit.",
        )
    )

    if subskill in ("concepts", "concept"):
        base_pool = concepts_pool
    elif subskill in ("activity_1", "activity1"):
        base_pool = activity1_pool
    elif subskill in ("activity_2", "activity2"):
        base_pool = activity2_pool
    else:
        base_pool = concepts_pool + activity1_pool + activity2_pool

    if not base_pool:
        base_pool = concepts_pool

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        q = r.choice(base_pool)
        q_copy = dict(q)
        q_copy["difficulty"] = difficulty
        q_copy["subskill"] = subskill
        out.append(q_copy)

    return out


generate_questions = generate_questions_v2
