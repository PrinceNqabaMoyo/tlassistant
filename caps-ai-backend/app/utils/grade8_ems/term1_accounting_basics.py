"""Grade 8 EMS — Accounting Concepts (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/01. Accounting concepts.md

Covers CAPS subskills:
  1. capital_and_owners_equity: Definition of capital, owner's financial interest, and drawings.
  2. assets_classification: Fixed/non-current assets (equipment, vehicles, buildings) vs current assets (bank, trading stock, cash float, debtors).
  3. liabilities_classification: Long-term liabilities (mortgage loans, bank loans) vs current liabilities (creditors, bank overdraft).
  4. income_and_expenses: Current income, sales, rent income vs operational expenses (wages, stationery, rent, water & electricity).
  5. profit_and_loss_calculation: Profit = Income - Expenses, Loss = Expenses - Income.
  6. accounting_equation_theory_and_drill: Standard equation A = OE + L and tabular transactional effect analysis.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "capital_and_owners_equity",
    "assets_classification",
    "liabilities_classification",
    "income_and_expenses",
    "profit_and_loss_calculation",
    "accounting_equation",
]

TOPIC_KEY = "grade8_ems_accounting_basics"
LO = "g8_ems_acct_concepts"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: str = "accounting_concepts",
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_accounting_basics",
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group,
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 2 > Accounting Concepts",
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["accounting", "financial_literacy"],
    })
    return enriched


def _gen_capital_and_oe(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]
    cap_val = rng.randint(15, 60) * 1000

    cases = [
        (
            f"When {owner} starts a service business in {scenario['area']} by investing R{cap_val} of their personal savings into the business bank account, this contribution is called:",
            "Capital",
            "Capital is the money or assets provided by the owner to start or expand a business.",
            ["Capital", "Current Income", "A Liability", "Drawings"],
        ),
        (
            f"The total financial interest or stake that {owner} holds in their business (calculated as Capital plus Profit minus Drawings) is defined as:",
            "Owner's Equity",
            "Owner's Equity represents the net worth of the business belonging to the owner (Assets minus Liabilities).",
            ["Owner's Equity", "Current Assets", "Net Liabilities", "Gross Profit"],
        ),
        (
            f"When {owner} takes R{rng.randint(5, 20) * 100} cash out of the business cash register for their personal family expenses, this transaction is recorded as:",
            "Drawings",
            "Drawings represents any money or assets taken from the business by the owner for personal use, which decreases Owner's Equity.",
            ["Drawings", "Operational Expense", "Capital Investment", "Current Liability"],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)

    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Step-by-Step Working:**\n- **Transaction / Concept Analysis:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_cap_{rng.randint(100000, 999999)}",
        "title": "Capital & Owner's Equity",
        "question_type": "mcq",
        "topic": "Accounting concepts",
        "subskill": "capital_and_owners_equity",
        "learning_objective_id": f"{LO}_capital_oe",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Think about whether this is the owner's investment, net stake, or personal withdrawal.",
            "tier_2": "Capital is investment into business; Drawings is personal withdrawal; Owner's Equity is the net interest.",
            "tier_3": f"The correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_capital_drawings_oe"],
    }, subskill="capital_and_owners_equity", learning_objective_id=f"{LO}_capital_oe", question_family_id="capital_oe_concepts")


def _gen_assets_classification(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"{owner}'s enterprise owns vehicles, office computers, and workshop machinery used to provide services over several years. These items are classified as:",
            "Fixed (Non-current) Assets",
            "Fixed assets are long-term tangible possessions of value that the business intends to keep and use for more than a year to generate income.",
            ["Fixed (Non-current) Assets", "Current Assets", "Current Liabilities", "Operational Expenses"],
        ),
        (
            f"The business has money in its commercial cheque account (Bank) and coins in the cash register (Cash float). These items are classified as:",
            "Current Assets",
            "Current assets are cash or items of value that can be converted into cash within a short period (usually within one year).",
            ["Current Assets", "Fixed (Non-current) Assets", "Long-term Liabilities", "Owner's Equity"],
        ),
        (
            f"Which of the following lists contains ONLY items that are classified as Assets in a service business?",
            "Vehicles, Bank, Equipment, Cash Float",
            "Vehicles and Equipment are Fixed Assets; Bank and Cash Float are Current Assets. All four are items of value owned by the business.",
            [
                "Vehicles, Bank, Equipment, Cash Float",
                "Bank loan, Rent expense, Stationery, Capital",
                "Current Income, Vehicles, Creditors, Wages",
                "Mortgage loan, Drawings, Machinery, Telephone",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)

    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Step-by-Step Working:**\n- **Transaction / Concept Analysis:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_asset_{rng.randint(100000, 999999)}",
        "title": "Assets Classification",
        "question_type": "mcq",
        "topic": "Accounting concepts",
        "subskill": "assets_classification",
        "learning_objective_id": f"{LO}_assets",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Assets are possessions of value owned by the business.",
            "tier_2": "Fixed/non-current assets last for years (machinery, vehicles). Current assets are cash or quickly convertible to cash (bank, float).",
            "tier_3": f"The correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_fixed_and_current_assets"],
    }, subskill="assets_classification", learning_objective_id=f"{LO}_assets", question_family_id="assets_concepts")


def _gen_liabilities_classification(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"To purchase workshop premises in {scenario['area']}, {owner} obtains a 20-year mortgage bond from Standard Bank. This debt is classified as a:",
            "Long-term (Non-current) Liability",
            "A long-term liability is a financial debt or obligation that is payable over a period longer than one year (e.g. mortgage loan).",
            ["Long-term (Non-current) Liability", "Current Liability", "Fixed Asset", "Operational Expense"],
        ),
        (
            f"The business purchased workshop tools on credit from a supplier and has 30 days to pay the account. This short-term obligation is classified as a:",
            "Current Liability",
            "A current liability is a debt or obligation that must be settled within the normal operating cycle or within 12 months (e.g. Creditors).",
            ["Current Liability", "Long-term Liability", "Current Asset", "Owner's Equity"],
        ),
        (
            f"Which of the following correctly defines a Liability in Economic and Management Sciences?",
            "Debts or monetary obligations that a business owes to outside parties",
            "A liability is an obligation to transfer economic resources (money or assets) to an external creditor as a result of past transactions.",
            [
                "Debts or monetary obligations that a business owes to outside parties",
                "Items of value owned by the business that help generate income",
                "The total amount of money the owner invested to start trading",
                "The money earned from providing services to clients during the month",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)

    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Step-by-Step Working:**\n- **Transaction / Concept Analysis:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_liab_{rng.randint(100000, 999999)}",
        "title": "Liabilities Classification",
        "question_type": "mcq",
        "topic": "Accounting concepts",
        "subskill": "liabilities_classification",
        "learning_objective_id": f"{LO}_liabilities",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Liabilities are debts owed to outside parties.",
            "tier_2": "Debts repaid over more than a year (mortgage) are long-term; debts repaid within a year (creditors, overdraft) are current.",
            "tier_3": f"The correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_long_term_and_current_liabilities"],
    }, subskill="liabilities_classification", learning_objective_id=f"{LO}_liabilities", question_family_id="liabilities_concepts")


def _gen_income_and_expenses(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"During the month, {owner}'s service business received R{rng.randint(8, 25) * 500} from clients for repair services rendered. In accounting, this inflow is called:",
            "Current Income",
            "Current Income represents revenue earned from the primary day-to-day services provided by a service enterprise.",
            ["Current Income", "Capital", "Net Profit", "Cash Float"],
        ),
        (
            f"At month-end, the enterprise paid municipal water and electricity bills, wages to assistant staff, and purchased office stationery. These payments are classified as:",
            "Expenses",
            "Expenses are operational costs incurred in running the business that consume resources and decrease profit and Owner's Equity.",
            ["Expenses", "Fixed Assets", "Liabilities", "Capital Withdrawals"],
        ),
        (
            f"Which of the following correctly pairs an Income item with an Expense item for a service business?",
            "Income: Current income; Expense: Stationery",
            "Current income (fees from clients) is revenue that increases Owner's Equity. Stationery is an operating expense that decreases Owner's Equity.",
            [
                "Income: Current income; Expense: Stationery",
                "Income: Capital; Expense: Bank loan",
                "Income: Vehicles; Expense: Cash float",
                "Income: Creditors; Expense: Debtors",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)

    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Step-by-Step Working:**\n- **Transaction / Concept Analysis:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_inc_exp_{rng.randint(100000, 999999)}",
        "title": "Income & Expenses",
        "question_type": "mcq",
        "topic": "Accounting concepts",
        "subskill": "income_and_expenses",
        "learning_objective_id": f"{LO}_income_expenses",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Income brings in money and increases profit; expenses are operating costs that decrease profit.",
            "tier_2": "Current income from services is income; stationery, rent, and wages are expenses.",
            "tier_3": f"The correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_income_with_capital"],
    }, subskill="income_and_expenses", learning_objective_id=f"{LO}_income_expenses", question_family_id="income_expenses_concepts")


def _gen_profit_and_loss(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]
    income = rng.randint(12, 35) * 1000
    is_profit = rng.choice([True, False])
    if is_profit:
        expenses = income - rng.randint(3, 10) * 1000
        diff = income - expenses
        result_type = "Profit"
        explanation = f"Income (R{income:,}) exceeds Expenses (R{expenses:,}) by R{diff:,}. Formula: Profit = Income - Expenses = R{income:,} - R{expenses:,} = R{diff:,}."
    else:
        expenses = income + rng.randint(2, 8) * 1000
        diff = expenses - income
        result_type = "Loss"
        explanation = f"Expenses (R{expenses:,}) exceed Income (R{income:,}) by R{diff:,}. Formula: Loss = Expenses - Income = R{expenses:,} - R{income:,} = R{diff:,}."

    prompt = (
        f"For the month of March, {owner}'s service business in {scenario['area']} earned total Current Income of "
        f"R{income:,} and incurred total operating Expenses of R{expenses:,}. "
        f"Calculate the financial result and state whether the business made a Profit or a Loss."
    )
    correct_ans = f"{result_type} of R{diff:,}"
    options = [
        f"{result_type} of R{diff:,}",
        f"{'Loss' if is_profit else 'Profit'} of R{diff:,}",
        f"{result_type} of R{income + expenses:,}",
        f"{'Loss' if is_profit else 'Profit'} of R{income:,}",
    ]
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)

    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Step 1:** Compare Income and Expenses.\n- Income = R{income:,}\n- Expenses = R{expenses:,}\n\n**Step 2:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_pnl_{rng.randint(100000, 999999)}",
        "title": "Profit and Loss Calculation",
        "question_type": "mcq",
        "topic": "Accounting concepts",
        "subskill": "profit_and_loss_calculation",
        "learning_objective_id": f"{LO}_profit_loss",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Compare total Income to total Expenses.",
            "tier_2": "If Income > Expenses, there is a Profit. If Expenses > Income, there is a Loss.",
            "tier_3": f"Result: {result_type} of R{diff:,}.",
        },
        "misconception_tags": ["confuses_profit_and_loss_formula"],
    }, subskill="profit_and_loss_calculation", learning_objective_id=f"{LO}_profit_loss", question_family_id="profit_loss_drill")


def _gen_accounting_equation_table(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cap_amount = rng.randint(10, 50) * 1000
    equip_amount = rng.randint(2, 8) * 1000
    rent_amount = rng.randint(1, 5) * 500

    transactions = [
        f"1. {owner} started the business by depositing R{cap_amount:,} into the business bank account.",
        f"2. Bought equipment on credit from {scenario['competitor']} for R{equip_amount:,}.",
        f"3. Paid rent via EFT for the month, R{rent_amount:,}.",
    ]
    data_rows = [
        ["1", f"+R{cap_amount}", f"+R{cap_amount}", "0"],
        ["2", f"+R{equip_amount}", "0", f"+R{equip_amount}"],
        ["3", f"-R{rent_amount}", f"-R{rent_amount}", "0"],
    ]
    cell_hints = {
        "r0_c1": f"Assets increase: Bank asset increases by R{cap_amount}.",
        "r0_c2": f"Owner's Equity increases: Capital contribution of R{cap_amount}.",
        "r0_c3": "Liabilities: No debt created (0).",
        "r1_c1": f"Assets increase: Equipment asset increases by R{equip_amount}.",
        "r1_c2": "Owner's Equity: No expense or income involved (0).",
        "r1_c3": f"Liabilities increase: Credit purchase increases creditors by R{equip_amount}.",
        "r2_c1": f"Assets decrease: Bank funds leave account by R{rent_amount}.",
        "r2_c2": f"Owner's Equity decreases: Rent is an operational expense (-R{rent_amount}).",
        "r2_c3": "Liabilities: Paid immediately, no debt (0).",
    }
    ui_rows = []
    correct_map = {}
    for i, row in enumerate(data_rows):
        ui_row = []
        for j, val in enumerate(row):
            correct_map[f"r{i}_c{j}"] = val
            ui_row.append({"value": row[0] if j == 0 else "", "cell_id": f"r{i}_c{j}", "editable": j > 0})
        ui_rows.append(ui_row)

    headers = ["No.", "Assets", "Owner's Equity", "Liabilities"]
    memo_lines = ["**Accounting Equation Memorandum (Cell-by-Cell Solution)** [9 marks]:\n"]
    for r_idx, tx in enumerate(transactions):
        memo_lines.append(f"**Transaction {tx.split('.')[0]}:** {tx.split('. ', 1)[-1]}")
        memo_lines.append(f"- **Assets**: `{data_rows[r_idx][1]}` ({cell_hints[f'r{r_idx}_c1']})")
        memo_lines.append(f"- **Owner's Equity**: `{data_rows[r_idx][2]}` ({cell_hints[f'r{r_idx}_c2']})")
        memo_lines.append(f"- **Liabilities**: `{data_rows[r_idx][3]}` ({cell_hints[f'r{r_idx}_c3']})\n")
    worked_sol = "\n".join(memo_lines)

    item = {
        "id": f"ems_accteq_{rng.randint(1000, 9999)}",
        "topic": "Accounting concepts",
        "prompt": (
            f"Analyse the following transactions for {owner}'s service business in {scenario['area']}. "
            f"Indicate the effect on the accounting equation (Assets, Owner's Equity, Liabilities) using a + for increase, "
            f"- for decrease, and 0 for no change, followed by the amount (e.g. +R5000 or 0).\n\n"
            f"Transactions:\n" + "\n".join(f"- {tx}" for tx in transactions)
        ),
        "transactions": transactions,
        "question_type": "journal",
        "journal": {
            "journal_type": "accounting_equation",
            "headers": headers,
            "rows": ui_rows,
        },
        "editable_cols": [1, 2, 3],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 9,
        "sample_answer": "Complete Accounting Equation table with Assets, Owner's Equity, and Liabilities correctly balanced.",
        "ideal_answer": "Complete Accounting Equation table with Assets, Owner's Equity, and Liabilities correctly balanced.",
        "worked_solution": worked_sol,
        "canonical_solution": worked_sol,
        "marking_points": ["Correct effects (+ / - / 0 and amounts) applied to Assets, OE, and Liabilities for all 3 transactions."],
        "hints": {
            "tier_1": "Recall the fundamental equation: Assets = Owner's Equity + Liabilities (A = OE + L).",
            "tier_2": "Identify which two accounts are affected by each transaction, whether they increase/decrease, and write + or - followed by the amount.",
            "tier_3": f"Row 1: +R{cap_amount}, +R{cap_amount}, 0. Row 2: +R{equip_amount}, 0, +R{equip_amount}. Row 3: -R{rent_amount}, -R{rent_amount}, 0.",
        },
    }
    return _with_metadata(item, subskill="accounting_equation", learning_objective_id=f"{LO}_equation_practical", question_family_id="equation_table")


def generate(subskill: str = "mixed", difficulty: str = "medium", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> Any:
    rng = _rng(seed)
    sub = str(subskill or "mixed").strip().lower()

    generators = {
        "capital_and_owners_equity": _gen_capital_and_oe,
        "assets_classification": _gen_assets_classification,
        "liabilities_classification": _gen_liabilities_classification,
        "income_and_expenses": _gen_income_and_expenses,
        "profit_and_loss_calculation": _gen_profit_and_loss,
        "accounting_equation": _gen_accounting_equation_table,
    }

    if sub in generators:
        fn = generators[sub]
        results = [fn(rng) for _ in range(count)]
    elif sub == "concepts":
        concept_fns = [_gen_capital_and_oe, _gen_assets_classification, _gen_liabilities_classification, _gen_income_and_expenses, _gen_profit_and_loss]
        results = [rng.choice(concept_fns)(rng) for _ in range(count)]
    else:
        # Mixed: sample across all 6 subskills
        all_fns = list(generators.values())
        results = [rng.choice(all_fns)(rng) for _ in range(count)]

    if count == 1 and len(results) == 1:
        return results[0]
    return results
