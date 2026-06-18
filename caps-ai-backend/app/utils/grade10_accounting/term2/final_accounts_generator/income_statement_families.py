from __future__ import annotations

import random
from typing import Any, Dict, List

from ....sole_trader.names import pick_business_name as _pick_business_name
from .shared import (
    _cell,
    _make_calc,
    _make_fill_in_table_question,
    _make_table_wordbank,
    _round_money,
    _teaching_hint,
    _with_validation,
)


def _gen_income_statement(r: random.Random) -> List[Dict[str, Any]]:
    """Income Statement — Trading Account + Profit and Loss Account structure."""
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    # Trading account structure matching
    items = [
        {"term": "Sales", "definition": "Revenue from goods sold during the period."},
        {"term": "Cost of Sales", "definition": "The cost price of goods that were sold."},
        {"term": "Gross Profit", "definition": "Net Sales minus Cost of Sales."},
        {"term": "Net Profit", "definition": "Gross Profit plus other income minus all expenses."},
        {"term": "Debtors' Allowances", "definition": "Returns and allowances granted to debtors, deducted from Sales."},
    ]

    distractors = ["Accumulated depreciation", "Creditors control", "Fixed deposit"]

    r.shuffle(items)
    selected = items[:4]
    terms_list = [i["term"] for i in selected] + r.sample(distractors, k=2)
    r.shuffle(terms_list)

    word_bank = [{"id": f"t{i}", "label": t} for i, t in enumerate(terms_list)]
    label_to_id = {wb["label"]: wb["id"] for wb in word_bank}

    rows = []
    correct_map = {}
    for i, item in enumerate(selected):
        rows.append([str(i + 1), item["definition"], ""])
        correct_map[str(i)] = {"2": label_to_id.get(item["term"], "")}

    pool.append(_make_table_wordbank(
        prompt="Match each description with the correct financial statement term.",
        headers=["No.", "Description", "Term"],
        rows=rows,
        word_bank=word_bank,
        correct_map=correct_map,
        guidelines=["Select the correct term from the word bank for each row."],
    ))

    # Full income statement calc
    sales = r.choice([600000, 750000, 900000])
    da = r.choice([8000, 12000, 15000])
    net_sales = sales - da
    cos = r.choice([320000, 400000, 500000])
    gp = net_sales - cos
    rent_inc = r.choice([24000, 36000, 48000])
    int_inc = r.choice([3000, 5000, 8000])
    total_expenses = r.choice([200000, 280000, 350000])
    np_ = gp + rent_inc + int_inc - total_expenses

    pool.append(_with_validation(_make_calc(
        prompt=(
            f"{biz} — Income Statement extract:\n"
            f"• Sales: R{sales:,}\n"
            f"• Debtors' Allowances: R{da:,}\n"
            f"• Cost of Sales: R{cos:,}\n"
            f"• Rent income: R{rent_inc:,}\n"
            f"• Interest income: R{int_inc:,}\n"
            f"• Total expenses: R{total_expenses:,}\n\n"
            f"Calculate the net profit."
        ),
        correct_answer=float(np_),
        working_formula=f"Net Profit = (R{sales:,} - R{da:,} - R{cos:,}) + R{rent_inc:,} + R{int_inc:,} - R{total_expenses:,}",
        formula_hint="Net Profit = (Sales - Debtors' Allowances - Cost of Sales) + Other income - Total expenses",
    ), "income_statement_net_profit", sales=sales, debtors_allowances=da, cost_of_sales=cos, rent_income=rent_inc, interest_income=int_inc, total_expenses=total_expenses))

    final_accounts_prompt_table = {
        "heading": f"{biz} — Pre-final-accounts extract",
        "headers": ["Item", "Amount"],
        "rows": [
            [_cell("Sales"), _cell(sales)],
            [_cell("Debtors' Allowances"), _cell(da)],
            [_cell("Cost of Sales"), _cell(cos)],
            [_cell("Other income (Rent + Interest)"), _cell(rent_inc + int_inc)],
            [_cell("Total expenses"), _cell(total_expenses)],
        ],
    }
    final_accounts_tables = [
        {
            "heading": "Trading Account (extract)",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Net Sales"), _cell("", editable=True, cell_id="fa-net-sales")],
                [_cell("Cost of Sales"), _cell("", editable=True, cell_id="fa-cost-of-sales")],
                [_cell("Gross Profit"), _cell("", editable=True, cell_id="fa-gross-profit")],
            ],
        },
        {
            "heading": "Profit and Loss Account (extract)",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Gross Profit"), _cell("", editable=True, cell_id="fa-pl-gross-profit")],
                [_cell("Other income"), _cell("", editable=True, cell_id="fa-other-income")],
                [_cell("Total expenses"), _cell("", editable=True, cell_id="fa-total-expenses")],
                [_cell("Net Profit"), _cell("", editable=True, cell_id="fa-net-profit")],
            ],
        },
    ]
    final_accounts_correct_map = {
        "fa-net-sales": net_sales,
        "fa-cost-of-sales": cos,
        "fa-gross-profit": gp,
        "fa-pl-gross-profit": gp,
        "fa-other-income": rent_inc + int_inc,
        "fa-total-expenses": total_expenses,
        "fa-net-profit": np_,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="final_account_table",
        prompt="Use the source extract to complete the Trading Account and Profit and Loss Account extracts below.",
        prompt_table=final_accounts_prompt_table,
        tables=final_accounts_tables,
        correct_map=final_accounts_correct_map,
        derivation_map={
            "fa-net-sales": f"Net Sales = R{int(sales):,} - R{int(da):,} = R{int(net_sales):,}.",
            "fa-gross-profit": f"Gross Profit = R{int(net_sales):,} - R{int(cos):,} = R{int(gp):,}.",
            "fa-net-profit": f"Net Profit = R{int(gp):,} + R{int(rent_inc + int_inc):,} - R{int(total_expenses):,} = R{int(np_):,}.",
        },
        cell_hints={
            "fa-net-sales": "Start with Sales and deduct Debtors' Allowances.",
            "fa-cost-of-sales": "Copy Cost of Sales directly from the source extract.",
            "fa-gross-profit": "Gross Profit is the difference between Net Sales and Cost of Sales.",
            "fa-pl-gross-profit": "Carry the Gross Profit from the Trading Account section into the Profit and Loss section unchanged.",
            "fa-other-income": "Use the combined other-income figure from the source extract.",
            "fa-total-expenses": "Copy the Total expenses figure directly from the source extract.",
            "fa-net-profit": "Net Profit = Gross Profit + Other income - Total expenses.",
        },
        cell_teaching_map={
            "fa-net-sales": _teaching_hint(
                role_in_requirement="This cell calculates the sales figure that belongs in the Trading Account after allowances are deducted.",
                evidence_from_question=f"The source extract shows Sales of R{int(sales):,} and Debtors' Allowances of R{int(da):,}.",
                rule_or_principle="Net Sales = Sales - Debtors' Allowances.",
                method_or_formula="Subtract the allowances from Sales before working out Gross Profit.",
                record_link="The Net Sales figure is then compared with Cost of Sales to calculate Gross Profit in the Trading Account.",
                how_to_derive=f"R{int(sales):,} - R{int(da):,} = R{int(net_sales):,}.",
                transfer_tip="In final-accounts work, finish the Trading Account section first because later profit figures depend on it.",
            ),
            "fa-cost-of-sales": _teaching_hint(
                role_in_requirement="This cell supplies the cost figure used in the Trading Account extract.",
                evidence_from_question=f"The source extract already gives Cost of Sales as R{int(cos):,}.",
                rule_or_principle="When a compact extract already provides Cost of Sales, copy it directly rather than recalculating it.",
                method_or_formula="Transfer the given Cost of Sales amount unchanged into the Trading Account extract.",
                record_link="This amount is compared with Net Sales to produce the Gross Profit that carries to Profit and Loss.",
                how_to_derive=f"Copy Cost of Sales = R{int(cos):,}.",
                transfer_tip="Check whether a figure is given directly or needs to be derived before starting a calculation.",
            ),
            "fa-gross-profit": _teaching_hint(
                role_in_requirement="This cell completes the Trading Account result for the period.",
                evidence_from_question=f"Use Net Sales R{int(net_sales):,} and Cost of Sales R{int(cos):,} from the Trading Account extract.",
                rule_or_principle="Gross Profit = Net Sales - Cost of Sales.",
                method_or_formula="Subtract the cost of the goods sold from the sales earned on those goods.",
                record_link="The Gross Profit figure is then carried down into the Profit and Loss Account section.",
                how_to_derive=f"R{int(net_sales):,} - R{int(cos):,} = R{int(gp):,}.",
                transfer_tip="Once Gross Profit is found, use exactly the same figure again in the Profit and Loss section.",
            ),
            "fa-pl-gross-profit": _teaching_hint(
                role_in_requirement="This cell carries the Trading Account result into the Profit and Loss Account section.",
                evidence_from_question="The Profit and Loss section starts with the Gross Profit already calculated in the Trading Account section above it.",
                rule_or_principle="Gross Profit is transferred unchanged from the Trading Account to the Profit and Loss Account.",
                method_or_formula="Copy the Gross Profit amount from the completed Trading Account section.",
                record_link="This carried figure becomes the starting point before adding other income and deducting expenses.",
                how_to_derive=f"Copy Gross Profit = R{int(gp):,}.",
                transfer_tip="When two statements are linked, always look for figures that are transferred unchanged between sections.",
            ),
            "fa-other-income": _teaching_hint(
                role_in_requirement="This cell adds the other-income component to the Profit and Loss Account.",
                evidence_from_question=f"The source extract gives Other income (Rent + Interest) of R{int(rent_inc + int_inc):,}.",
                rule_or_principle="Other income is added after Gross Profit in the Profit and Loss Account.",
                method_or_formula="Copy the combined other-income amount shown in the source extract.",
                record_link="This amount is added to Gross Profit before expenses are deducted to get Net Profit.",
                how_to_derive=f"Copy Other income = R{int(rent_inc + int_inc):,}.",
                transfer_tip="Keep Trading Account figures and other-income figures separate until you reach the Profit and Loss section.",
            ),
            "fa-total-expenses": _teaching_hint(
                role_in_requirement="This cell provides the total expense amount to deduct in the Profit and Loss Account.",
                evidence_from_question=f"The source extract already shows Total expenses of R{int(total_expenses):,}.",
                rule_or_principle="In a compact extract, a given expense total is transferred directly unless the task asks you to build it item by item.",
                method_or_formula="Copy the Total expenses amount unchanged into the Profit and Loss Account extract.",
                record_link="This expense total is deducted from Gross Profit plus Other income to determine Net Profit.",
                how_to_derive=f"Copy Total expenses = R{int(total_expenses):,}.",
                transfer_tip="Do not recompute a total that the source extract has already combined for you.",
            ),
            "fa-net-profit": _teaching_hint(
                role_in_requirement="This cell gives the final operating result after other income and expenses are considered.",
                evidence_from_question=f"Use Gross Profit R{int(gp):,}, Other income R{int(rent_inc + int_inc):,}, and Total expenses R{int(total_expenses):,}.",
                rule_or_principle="Net Profit = Gross Profit + Other income - Total expenses.",
                method_or_formula="Add Gross Profit and Other income, then deduct Total expenses.",
                record_link="This final profit figure is the one later used in capital and broader year-end carry-through questions.",
                how_to_derive=f"R{int(gp):,} + R{int(rent_inc + int_inc):,} - R{int(total_expenses):,} = R{int(np_):,}.",
                transfer_tip="Finish each earlier line correctly before calculating Net Profit, because it depends on the completed statement structure.",
            ),
        },
        working_map={
            "fa-pl-gross-profit": "The Profit and Loss Account begins with the same Gross Profit already calculated in the Trading Account section.",
            "fa-other-income": "Add the other-income figure to Gross Profit before considering the expense deduction.",
            "fa-total-expenses": "This total is deducted only after the income side of the Profit and Loss Account has been completed.",
            "fa-net-profit": "Think of the statement in order: net sales to gross profit, then gross profit plus other income, then less total expenses.",
        },
        guidelines=["Net Sales = Sales - Debtors' Allowances.", "Gross Profit = Net Sales - Cost of Sales.", "Net Profit = Gross Profit + Other income - Total expenses."],
        marks=10,
    ), "income_statement_fill", expected_cells=7, sales=sales, debtors_allowances=da, cost_of_sales=cos, other_income=rent_inc + int_inc, total_expenses=total_expenses))

    trading_scenarios = [
        {
            "sales": 420000,
            "debtors_allowances": 12000,
            "opening_stock": 38000,
            "purchases": 260000,
            "returns_outwards": 10000,
            "carriage_on_purchases": 12000,
            "closing_stock": 45000,
        },
        {
            "sales": 510000,
            "debtors_allowances": 15000,
            "opening_stock": 42000,
            "purchases": 300000,
            "returns_outwards": 14000,
            "carriage_on_purchases": 15000,
            "closing_stock": 52000,
        },
        {
            "sales": 360000,
            "debtors_allowances": 9000,
            "opening_stock": 30000,
            "purchases": 220000,
            "returns_outwards": 8000,
            "carriage_on_purchases": 9000,
            "closing_stock": 36000,
        },
    ]
    for scenario in trading_scenarios:
        net_sales = _round_money(float(scenario["sales"]) - float(scenario["debtors_allowances"]))
        net_purchases = _round_money(float(scenario["purchases"]) - float(scenario["returns_outwards"]))
        goods_available = _round_money(float(scenario["opening_stock"]) + float(net_purchases) + float(scenario["carriage_on_purchases"]))
        cost_of_sales = _round_money(float(goods_available) - float(scenario["closing_stock"]))
        gross_profit = _round_money(float(net_sales) - float(cost_of_sales))

        pool.append(_with_validation(_make_calc(
            prompt=(
                f"{biz} presents the following Trading Account information:\n"
                f"• Sales: R{int(scenario['sales']):,}\n"
                f"• Debtors' Allowances: R{int(scenario['debtors_allowances']):,}\n"
                f"• Opening stock: R{int(scenario['opening_stock']):,}\n"
                f"• Purchases: R{int(scenario['purchases']):,}\n"
                f"• Returns outwards: R{int(scenario['returns_outwards']):,}\n"
                f"• Carriage on purchases: R{int(scenario['carriage_on_purchases']):,}\n"
                f"• Closing stock: R{int(scenario['closing_stock']):,}\n\n"
                f"Calculate the gross profit."
            ),
            correct_answer=gross_profit,
            working_formula=(
                f"Gross Profit = [R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,}] - "
                f"[(R{int(scenario['opening_stock']):,} + (R{int(scenario['purchases']):,} - R{int(scenario['returns_outwards']):,}) + R{int(scenario['carriage_on_purchases']):,}) - R{int(scenario['closing_stock']):,}]"
            ),
            formula_hint="Gross Profit = Net Sales - Cost of Sales, and Cost of Sales = Opening stock + net purchases + carriage on purchases - closing stock",
        ), "trading_account_gross_profit_calc", sales=scenario["sales"], debtors_allowances=scenario["debtors_allowances"], opening_stock=scenario["opening_stock"], purchases=scenario["purchases"], returns_outwards=scenario["returns_outwards"], carriage_on_purchases=scenario["carriage_on_purchases"], closing_stock=scenario["closing_stock"]))

        trading_prompt_table = {
            "heading": f"{biz} — Trading Account source extract",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Sales"), _cell(scenario["sales"])],
                [_cell("Debtors' Allowances"), _cell(scenario["debtors_allowances"])],
                [_cell("Opening stock"), _cell(scenario["opening_stock"])],
                [_cell("Purchases"), _cell(scenario["purchases"])],
                [_cell("Returns outwards"), _cell(scenario["returns_outwards"])],
                [_cell("Carriage on purchases"), _cell(scenario["carriage_on_purchases"])],
                [_cell("Closing stock"), _cell(scenario["closing_stock"])],
            ],
        }
        trading_table = {
            "heading": "Trading Account (standalone fuller extract)",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Sales"), _cell("", editable=True, cell_id="ta-sales")],
                [_cell("Less: Debtors' Allowances"), _cell("", editable=True, cell_id="ta-da")],
                [_cell("Net Sales"), _cell("", editable=True, cell_id="ta-net-sales")],
                [_cell("Opening stock"), _cell("", editable=True, cell_id="ta-opening-stock")],
                [_cell("Net purchases"), _cell("", editable=True, cell_id="ta-net-purchases")],
                [_cell("Carriage on purchases"), _cell("", editable=True, cell_id="ta-carriage")],
                [_cell("Goods available for sale"), _cell("", editable=True, cell_id="ta-goods-available")],
                [_cell("Less: Closing stock"), _cell("", editable=True, cell_id="ta-closing-stock")],
                [_cell("Cost of Sales"), _cell("", editable=True, cell_id="ta-cost-sales")],
                [_cell("Gross Profit"), _cell("", editable=True, cell_id="ta-gross-profit")],
            ],
        }
        trading_correct_map = {
            "ta-sales": scenario["sales"],
            "ta-da": scenario["debtors_allowances"],
            "ta-net-sales": net_sales,
            "ta-opening-stock": scenario["opening_stock"],
            "ta-net-purchases": net_purchases,
            "ta-carriage": scenario["carriage_on_purchases"],
            "ta-goods-available": goods_available,
            "ta-closing-stock": scenario["closing_stock"],
            "ta-cost-sales": cost_of_sales,
            "ta-gross-profit": gross_profit,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract for {biz} to complete the fuller standalone Trading Account extract below.",
            prompt_table=trading_prompt_table,
            table=trading_table,
            correct_map=trading_correct_map,
            derivation_map={
                "ta-net-sales": f"Net Sales = R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{int(net_sales):,}.",
                "ta-net-purchases": f"Net purchases = R{int(scenario['purchases']):,} - R{int(scenario['returns_outwards']):,} = R{int(net_purchases):,}.",
                "ta-goods-available": f"Goods available = R{int(scenario['opening_stock']):,} + R{int(net_purchases):,} + R{int(scenario['carriage_on_purchases']):,} = R{int(goods_available):,}.",
                "ta-cost-sales": f"Cost of Sales = R{int(goods_available):,} - R{int(scenario['closing_stock']):,} = R{int(cost_of_sales):,}.",
                "ta-gross-profit": f"Gross Profit = R{int(net_sales):,} - R{int(cost_of_sales):,} = R{int(gross_profit):,}.",
            },
            cell_hints={
                "ta-sales": "Copy Sales directly from the source extract.",
                "ta-da": "Copy Debtors' Allowances directly from the source extract.",
                "ta-net-sales": "Deduct Debtors' Allowances from Sales first.",
                "ta-opening-stock": "Copy Opening stock directly from the source extract.",
                "ta-net-purchases": "Deduct Returns outwards from Purchases to get net purchases.",
                "ta-carriage": "Copy Carriage on purchases directly from the source extract.",
                "ta-goods-available": "Add Opening stock, Net purchases, and Carriage on purchases.",
                "ta-closing-stock": "Copy Closing stock directly from the source extract before deducting it from goods available.",
                "ta-cost-sales": "Deduct Closing stock from Goods available for sale.",
                "ta-gross-profit": "Gross Profit = Net Sales - Cost of Sales.",
            },
            cell_teaching_map={
                "ta-sales": _teaching_hint(
                    role_in_requirement="This cell carries the Sales figure into the Trading Account extract.",
                    evidence_from_question=f"The source extract gives Sales of R{int(scenario['sales']):,}.",
                    rule_or_principle="Given source figures are copied directly before derived lines such as Net Sales are calculated.",
                    method_or_formula="Transfer the Sales amount unchanged from the source extract.",
                    record_link="This copied figure is then reduced by Debtors' Allowances to produce Net Sales.",
                    how_to_derive=f"Copy Sales = R{int(scenario['sales']):,}.",
                    transfer_tip="Complete the direct carry figures first so that the later calculated rows have the correct inputs.",
                ),
                "ta-da": _teaching_hint(
                    role_in_requirement="This cell carries the deduction for Debtors' Allowances into the Trading Account.",
                    evidence_from_question=f"The source extract gives Debtors' Allowances of R{int(scenario['debtors_allowances']):,}.",
                    rule_or_principle="Debtors' Allowances are deducted from Sales to determine Net Sales.",
                    method_or_formula="Copy the Debtors' Allowances amount unchanged into its row.",
                    record_link="This line is used immediately in the Net Sales calculation below it.",
                    how_to_derive=f"Copy Debtors' Allowances = R{int(scenario['debtors_allowances']):,}.",
                    transfer_tip="Items introduced by 'Less:' are usually deductions from the line above them.",
                ),
                "ta-net-sales": _teaching_hint(
                    role_in_requirement="This cell calculates the trading revenue after allowances have been deducted.",
                    evidence_from_question=f"Use Sales R{int(scenario['sales']):,} and Debtors' Allowances R{int(scenario['debtors_allowances']):,} from the source extract.",
                    rule_or_principle="Net Sales = Sales - Debtors' Allowances.",
                    method_or_formula="Subtract the allowance deduction from the gross sales figure.",
                    record_link="Net Sales becomes the revenue side used to compare against Cost of Sales.",
                    how_to_derive=f"R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{int(net_sales):,}.",
                    transfer_tip="Always complete netted revenue lines before moving to stock and purchase calculations.",
                ),
                "ta-opening-stock": _teaching_hint(
                    role_in_requirement="This cell brings the opening stock balance into the cost-of-sales section.",
                    evidence_from_question=f"The source extract gives Opening stock of R{int(scenario['opening_stock']):,}.",
                    rule_or_principle="Opening stock is one of the components used to determine goods available for sale.",
                    method_or_formula="Copy the Opening stock amount into the Trading Account extract.",
                    record_link="This figure is later added to Net purchases and Carriage on purchases to calculate goods available.",
                    how_to_derive=f"Copy Opening stock = R{int(scenario['opening_stock']):,}.",
                    transfer_tip="Identify which stock figure is opening and which is closing before calculating Cost of Sales.",
                ),
                "ta-net-purchases": _teaching_hint(
                    role_in_requirement="This cell calculates the purchase amount after purchase returns are deducted.",
                    evidence_from_question=f"The source extract gives Purchases of R{int(scenario['purchases']):,} and Returns outwards of R{int(scenario['returns_outwards']):,}.",
                    rule_or_principle="Net purchases = Purchases - Returns outwards.",
                    method_or_formula="Reduce Purchases by the returns-outwards amount before adding stock and carriage figures.",
                    record_link="Net purchases feeds directly into the Goods available for sale total.",
                    how_to_derive=f"R{int(scenario['purchases']):,} - R{int(scenario['returns_outwards']):,} = R{int(net_purchases):,}.",
                    transfer_tip="When purchase returns are given separately, reduce Purchases before combining them with stock and carriage figures.",
                ),
                "ta-carriage": _teaching_hint(
                    role_in_requirement="This cell carries the carriage-on-purchases amount into the Trading Account.",
                    evidence_from_question=f"The source extract gives Carriage on purchases of R{int(scenario['carriage_on_purchases']):,}.",
                    rule_or_principle="Carriage on purchases forms part of the cost of bringing goods in and is added when calculating goods available for sale.",
                    method_or_formula="Copy the carriage amount unchanged into the Trading Account extract.",
                    record_link="This figure is added to Opening stock and Net purchases in the Goods available calculation.",
                    how_to_derive=f"Copy Carriage on purchases = R{int(scenario['carriage_on_purchases']):,}.",
                    transfer_tip="Do not treat carriage on purchases as an operating expense when the question places it in the Trading Account section.",
                ),
                "ta-goods-available": _teaching_hint(
                    role_in_requirement="This cell totals the goods available for sale before closing stock is deducted.",
                    evidence_from_question=f"Use Opening stock R{int(scenario['opening_stock']):,}, Net purchases R{int(net_purchases):,}, and Carriage on purchases R{int(scenario['carriage_on_purchases']):,}.",
                    rule_or_principle="Goods available for sale = Opening stock + Net purchases + Carriage on purchases.",
                    method_or_formula="Add the opening stock, adjusted purchases, and carriage amounts together.",
                    record_link="This subtotal is then reduced by Closing stock to determine Cost of Sales.",
                    how_to_derive=f"R{int(scenario['opening_stock']):,} + R{int(net_purchases):,} + R{int(scenario['carriage_on_purchases']):,} = R{int(goods_available):,}.",
                    transfer_tip="Work in statement order: first build the subtotal, then deduct the closing stock from it.",
                ),
                "ta-closing-stock": _teaching_hint(
                    role_in_requirement="This cell carries the closing stock deduction into the Trading Account.",
                    evidence_from_question=f"The source extract gives Closing stock of R{int(scenario['closing_stock']):,}.",
                    rule_or_principle="Closing stock is deducted because those goods were not sold during the current period.",
                    method_or_formula="Copy the Closing stock figure to the 'Less:' line before calculating Cost of Sales.",
                    record_link="This deduction is applied to Goods available for sale to produce Cost of Sales.",
                    how_to_derive=f"Copy Closing stock = R{int(scenario['closing_stock']):,}.",
                    transfer_tip="The word 'closing' usually signals the figure to deduct from goods available rather than add.",
                ),
                "ta-cost-sales": _teaching_hint(
                    role_in_requirement="This cell calculates the cost of the goods actually sold during the year.",
                    evidence_from_question=f"The source extract provides Opening stock, Purchases, Returns outwards, Carriage on purchases, and Closing stock.",
                    rule_or_principle="Cost of Sales = Opening stock + Net purchases + Carriage on purchases - Closing stock.",
                    method_or_formula="Subtract Closing stock from the Goods available for sale subtotal.",
                    record_link="This amount is the cost figure compared with Net Sales to determine Gross Profit.",
                    how_to_derive=f"R{int(goods_available):,} - R{int(scenario['closing_stock']):,} = R{int(cost_of_sales):,}.",
                    transfer_tip="Closing stock is deducted because those goods were not sold during the current period.",
                ),
                "ta-gross-profit": _teaching_hint(
                    role_in_requirement="This cell shows the gross profit earned from trading activities.",
                    evidence_from_question=f"Net Sales are R{int(net_sales):,} and Cost of Sales is R{int(cost_of_sales):,}.",
                    rule_or_principle="Gross Profit = Net Sales - Cost of Sales.",
                    method_or_formula="Compare the completed revenue section with the completed cost section.",
                    record_link="This Gross Profit figure is the value later transferred into the Profit and Loss Account.",
                    how_to_derive=f"R{int(net_sales):,} - R{int(cost_of_sales):,} = R{int(gross_profit):,}.",
                    transfer_tip="Complete the Net Sales and Cost of Sales sections first; Gross Profit is the comparison between those two finished totals.",
                ),
            },
            working_map={
                "ta-net-sales": "Finish the revenue side first by copying Sales and Debtors' Allowances and then calculating Net Sales.",
                "ta-goods-available": "The cost section builds step by step: Opening stock plus Net purchases plus Carriage on purchases.",
                "ta-cost-sales": "Once goods available is complete, deduct Closing stock to isolate only the cost of the goods sold.",
                "ta-gross-profit": "Gross Profit is the final comparison between the completed revenue section and the completed cost section.",
            },
            guidelines=[
                "Work from top to bottom: Net Sales first, then Cost of Sales, then Gross Profit.",
                "Convert Purchases to Net purchases before calculating Cost of Sales.",
                "Deduct Closing stock because it is not part of the current year's Cost of Sales.",
            ],
            marks=12,
        ), "trading_account_full_extract_fill", expected_cells=10, cell_expectations=trading_correct_map))

    profit_loss_scenarios = [
        {
            "gross_profit": 142000,
            "other_incomes": [("Rent income", 18000), ("Commission income", 12000)],
            "expenses": [("Salaries", 52000), ("Insurance", 11000), ("Telephone", 9000), ("Depreciation", 14000), ("General expenses", 8000)],
        },
        {
            "gross_profit": 168000,
            "other_incomes": [("Interest income", 9000), ("Discount received", 7000)],
            "expenses": [("Wages", 48000), ("Advertising", 15000), ("Rates", 12000), ("Depreciation", 13000), ("Sundry expenses", 10000)],
        },
        {
            "gross_profit": 126000,
            "other_incomes": [("Rent income", 14000), ("Interest income", 6000)],
            "expenses": [("Salaries", 46000), ("Water and electricity", 10000), ("Insurance", 9000), ("Depreciation", 12000), ("Repairs", 7000)],
        },
    ]
    for scenario in profit_loss_scenarios:
        total_other_income = _round_money(sum(float(amount) for _, amount in scenario["other_incomes"]))
        total_income_before_expenses = _round_money(float(scenario["gross_profit"]) + float(total_other_income))
        total_expenses = _round_money(sum(float(amount) for _, amount in scenario["expenses"]))
        net_profit = _round_money(float(total_income_before_expenses) - float(total_expenses))
        expense_breakdown = " + ".join(f"R{int(amount):,}" for _, amount in scenario["expenses"])

        pool.append(_with_validation(_make_calc(
            prompt=(
                f"{biz} provides the following Profit and Loss Account information:\n"
                f"• Gross Profit: R{int(scenario['gross_profit']):,}\n"
                + "\n".join(f"• {label}: R{int(amount):,}" for label, amount in scenario["other_incomes"]) + "\n"
                + "\n".join(f"• {label}: R{int(amount):,}" for label, amount in scenario["expenses"]) + "\n\n"
                + "Calculate the net profit."
            ),
            correct_answer=net_profit,
            working_formula=f"Net Profit = (Gross Profit + other income) - total expenses = (R{int(scenario['gross_profit']):,} + R{int(total_other_income):,}) - R{int(total_expenses):,}",
            formula_hint="Net Profit = Gross Profit + Other income - Total expenses",
        ), "profit_and_loss_net_profit_calc", gross_profit=scenario["gross_profit"], other_income=total_other_income, total_expenses=total_expenses))

        pl_prompt_table = {
            "heading": f"{biz} — Profit and Loss source extract",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Gross Profit"), _cell(scenario["gross_profit"])],
                *[[_cell(label), _cell(amount)] for label, amount in scenario["other_incomes"]],
                *[[_cell(label), _cell(amount)] for label, amount in scenario["expenses"]],
            ],
        }
        pl_table = {
            "heading": "Profit and Loss Account (standalone fuller extract)",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Gross Profit"), _cell("", editable=True, cell_id="pl-gross-profit")],
                [_cell(str(scenario["other_incomes"][0][0])), _cell("", editable=True, cell_id="pl-other-1")],
                [_cell(str(scenario["other_incomes"][1][0])), _cell("", editable=True, cell_id="pl-other-2")],
                [_cell("Total income before expenses"), _cell("", editable=True, cell_id="pl-total-income")],
                [_cell(str(scenario["expenses"][0][0])), _cell("", editable=True, cell_id="pl-exp-1")],
                [_cell(str(scenario["expenses"][1][0])), _cell("", editable=True, cell_id="pl-exp-2")],
                [_cell(str(scenario["expenses"][2][0])), _cell("", editable=True, cell_id="pl-exp-3")],
                [_cell(str(scenario["expenses"][3][0])), _cell("", editable=True, cell_id="pl-exp-4")],
                [_cell(str(scenario["expenses"][4][0])), _cell("", editable=True, cell_id="pl-exp-5")],
                [_cell("Total expenses"), _cell("", editable=True, cell_id="pl-total-expenses")],
                [_cell("Net Profit"), _cell("", editable=True, cell_id="pl-net-profit")],
            ],
        }
        pl_correct_map = {
            "pl-gross-profit": scenario["gross_profit"],
            "pl-other-1": scenario["other_incomes"][0][1],
            "pl-other-2": scenario["other_incomes"][1][1],
            "pl-total-income": total_income_before_expenses,
            "pl-exp-1": scenario["expenses"][0][1],
            "pl-exp-2": scenario["expenses"][1][1],
            "pl-exp-3": scenario["expenses"][2][1],
            "pl-exp-4": scenario["expenses"][3][1],
            "pl-exp-5": scenario["expenses"][4][1],
            "pl-total-expenses": total_expenses,
            "pl-net-profit": net_profit,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract for {biz} to complete the fuller standalone Profit and Loss Account extract below.",
            prompt_table=pl_prompt_table,
            table=pl_table,
            correct_map=pl_correct_map,
            derivation_map={
                "pl-total-income": f"Total income before expenses = Gross Profit R{int(scenario['gross_profit']):,} + other income R{int(total_other_income):,} = R{int(total_income_before_expenses):,}.",
                "pl-total-expenses": f"Total expenses = {expense_breakdown} = R{int(total_expenses):,}.",
                "pl-net-profit": f"Net Profit = R{int(total_income_before_expenses):,} - R{int(total_expenses):,} = R{int(net_profit):,}.",
            },
            cell_hints={
                "pl-gross-profit": "Copy Gross Profit directly from the source extract.",
                "pl-other-1": "Copy the first other-income item directly from the source extract.",
                "pl-other-2": "Copy the second other-income item directly from the source extract.",
                "pl-total-income": "Add Gross Profit and the other-income figures first.",
                "pl-exp-1": "Copy the first expense amount directly from the source extract.",
                "pl-exp-2": "Copy the second expense amount directly from the source extract.",
                "pl-exp-3": "Copy the third expense amount directly from the source extract.",
                "pl-exp-4": "Copy the fourth expense amount directly from the source extract.",
                "pl-exp-5": "Copy the fifth expense amount directly from the source extract.",
                "pl-total-expenses": "Add all the listed expense items before calculating Net Profit.",
                "pl-net-profit": "Net Profit = Total income before expenses - Total expenses.",
            },
            cell_teaching_map={
                "pl-gross-profit": _teaching_hint(
                    role_in_requirement="This cell carries the Gross Profit starting figure into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows Gross Profit of R{int(scenario['gross_profit']):,}.",
                    rule_or_principle="Gross Profit is copied into the Profit and Loss Account before other income and expenses are considered.",
                    method_or_formula="Transfer the Gross Profit figure unchanged from the source extract.",
                    record_link="This starting figure is then combined with other income to form the total income before expenses.",
                    how_to_derive=f"Copy Gross Profit = R{int(scenario['gross_profit']):,}.",
                    transfer_tip="In Profit and Loss work, begin with the profit transferred from the Trading Account before adding other income.",
                ),
                "pl-other-1": _teaching_hint(
                    role_in_requirement="This cell carries the first other-income line into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['other_incomes'][0][0]} of R{int(scenario['other_incomes'][0][1]):,}.",
                    rule_or_principle="Other income items are copied into the income side of the Profit and Loss Account before expenses are deducted.",
                    method_or_formula="Transfer the first other-income amount unchanged.",
                    record_link="This amount contributes to the total income before expenses subtotal.",
                    how_to_derive=f"Copy {scenario['other_incomes'][0][0]} = R{int(scenario['other_incomes'][0][1]):,}.",
                    transfer_tip="Treat each income line separately before combining them into a total.",
                ),
                "pl-other-2": _teaching_hint(
                    role_in_requirement="This cell carries the second other-income line into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['other_incomes'][1][0]} of R{int(scenario['other_incomes'][1][1]):,}.",
                    rule_or_principle="Each other-income item is shown before the subtotal of income before expenses is calculated.",
                    method_or_formula="Transfer the second other-income amount unchanged.",
                    record_link="This amount is added with Gross Profit and the first other-income item to reach total income before expenses.",
                    how_to_derive=f"Copy {scenario['other_incomes'][1][0]} = R{int(scenario['other_incomes'][1][1]):,}.",
                    transfer_tip="Complete all income lines first so the income subtotal is accurate before you move to expenses.",
                ),
                "pl-total-income": _teaching_hint(
                    role_in_requirement="This cell totals the income side of the Profit and Loss Account before expenses are deducted.",
                    evidence_from_question=f"The source extract gives Gross Profit of R{int(scenario['gross_profit']):,} and other income totalling R{int(total_other_income):,}.",
                    rule_or_principle="The Profit and Loss Account begins with Gross Profit and then adds other income before expenses are deducted.",
                    method_or_formula="Add Gross Profit and the two other-income amounts to get the income-side subtotal.",
                    record_link="This completed subtotal is then compared with Total expenses to calculate Net Profit.",
                    how_to_derive=f"R{int(scenario['gross_profit']):,} + R{int(total_other_income):,} = R{int(total_income_before_expenses):,}.",
                    transfer_tip="Keep the income side complete before you move to the expense side of the Profit and Loss Account.",
                ),
                "pl-exp-1": _teaching_hint(
                    role_in_requirement="This cell carries the first expense item into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['expenses'][0][0]} of R{int(scenario['expenses'][0][1]):,}.",
                    rule_or_principle="Each listed expense is copied into the expense section before the total-expenses line is calculated.",
                    method_or_formula="Transfer the first expense amount unchanged.",
                    record_link="This amount contributes to the Total expenses subtotal used to calculate Net Profit.",
                    how_to_derive=f"Copy {scenario['expenses'][0][0]} = R{int(scenario['expenses'][0][1]):,}.",
                    transfer_tip="Keep income lines and expense lines in separate sections so the final subtotal logic stays clear.",
                ),
                "pl-exp-2": _teaching_hint(
                    role_in_requirement="This cell carries the second expense item into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['expenses'][1][0]} of R{int(scenario['expenses'][1][1]):,}.",
                    rule_or_principle="Expense lines are copied individually before being totaled.",
                    method_or_formula="Transfer the second expense amount unchanged.",
                    record_link="This amount is included in the Total expenses calculation.",
                    how_to_derive=f"Copy {scenario['expenses'][1][0]} = R{int(scenario['expenses'][1][1]):,}.",
                    transfer_tip="Check each expense line against the source extract before totaling the expense section.",
                ),
                "pl-exp-3": _teaching_hint(
                    role_in_requirement="This cell carries the third expense item into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['expenses'][2][0]} of R{int(scenario['expenses'][2][1]):,}.",
                    rule_or_principle="Each expense is copied once only into the statement before the final total is calculated.",
                    method_or_formula="Transfer the third expense amount unchanged.",
                    record_link="This amount contributes to the Total expenses subtotal.",
                    how_to_derive=f"Copy {scenario['expenses'][2][0]} = R{int(scenario['expenses'][2][1]):,}.",
                    transfer_tip="Keep a running mental check that every expense is being listed once and only once.",
                ),
                "pl-exp-4": _teaching_hint(
                    role_in_requirement="This cell carries the fourth expense item into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['expenses'][3][0]} of R{int(scenario['expenses'][3][1]):,}.",
                    rule_or_principle="Expense rows are copied before the section total is computed.",
                    method_or_formula="Transfer the fourth expense amount unchanged.",
                    record_link="This amount is one of the components of the Total expenses figure.",
                    how_to_derive=f"Copy {scenario['expenses'][3][0]} = R{int(scenario['expenses'][3][1]):,}.",
                    transfer_tip="If the statement gives many expenses, complete the individual rows first and total only afterwards.",
                ),
                "pl-exp-5": _teaching_hint(
                    role_in_requirement="This cell carries the fifth expense item into the Profit and Loss Account.",
                    evidence_from_question=f"The source extract shows {scenario['expenses'][4][0]} of R{int(scenario['expenses'][4][1]):,}.",
                    rule_or_principle="All listed operating expenses belong in the expense section before Net Profit is calculated.",
                    method_or_formula="Transfer the fifth expense amount unchanged.",
                    record_link="This amount completes the list of expenses that are then totaled.",
                    how_to_derive=f"Copy {scenario['expenses'][4][0]} = R{int(scenario['expenses'][4][1]):,}.",
                    transfer_tip="Do not start the Net Profit calculation until every expense line has been placed correctly.",
                ),
                "pl-total-expenses": _teaching_hint(
                    role_in_requirement="This cell totals all operating expenses for the period.",
                    evidence_from_question="The source extract lists each expense separately and each one belongs below the income section of the Profit and Loss Account.",
                    rule_or_principle="Total expenses are the sum of all listed expense items for the period.",
                    method_or_formula="Add every expense item shown in the expense section to reach one subtotal.",
                    record_link="This subtotal is deducted from total income before expenses to determine Net Profit.",
                    how_to_derive=f"{expense_breakdown} = R{int(total_expenses):,}.",
                    transfer_tip="Add every expense item once only; do not mix Gross Profit or other income into the expense total.",
                ),
                "pl-net-profit": _teaching_hint(
                    role_in_requirement="This cell calculates the final profit after expenses have been deducted.",
                    evidence_from_question=f"The completed income side totals R{int(total_income_before_expenses):,} and the completed expense side totals R{int(total_expenses):,}.",
                    rule_or_principle="Net Profit = total income before expenses - total expenses.",
                    method_or_formula="Subtract the completed Total expenses from the completed Total income before expenses.",
                    record_link="This final profit figure is the value later carried into capital / equity calculations in broader integrated tasks.",
                    how_to_derive=f"R{int(total_income_before_expenses):,} - R{int(total_expenses):,} = R{int(net_profit):,}.",
                    transfer_tip="Finish both totals before calculating Net Profit so you can subtract one complete side from the other.",
                ),
            },
            working_map={
                "pl-total-income": "Complete the income side first by combining Gross Profit and both other-income lines.",
                "pl-total-expenses": "After all five expense rows are copied, combine them into one expense subtotal.",
                "pl-net-profit": "Net Profit is the final comparison between the completed income subtotal and the completed expense subtotal.",
            },
            guidelines=[
                "Add Gross Profit and other income before dealing with the expense total.",
                "Add all listed expenses to get one Total expenses figure.",
                "Net Profit is the difference between total income before expenses and total expenses.",
            ],
            marks=12,
        ), "profit_and_loss_full_extract_fill", expected_cells=11, cell_expectations=pl_correct_map))

    integrated_scenarios = [
        {
            "other_income_label": "Rent income",
            "expense_items": [("Telephone", 9000), ("Insurance", 3000), ("Depreciation", 9000), ("Salaries", 40000), ("General expenses", 12000)],
            "sales": 390000,
            "debtors_allowances": 10000,
            "cost_of_sales": 240000,
            "other_income": 22000,
            "asset_label": "Equipment",
            "bank": 96000,
            "debtors": 65000,
            "stock": 24000,
            "asset_balance": 90000,
            "accumdep": 9000,
            "creditors": 15000,
            "loan": 30000,
            "drawings": 18000,
        },
        {
            "other_income_label": "Commission income",
            "expense_items": [("Advertising", 14000), ("Rates", 6000), ("Depreciation", 12000), ("Salaries", 32000), ("General expenses", 16000)],
            "sales": 460000,
            "debtors_allowances": 12000,
            "cost_of_sales": 300000,
            "other_income": 28000,
            "asset_label": "Vehicles",
            "bank": 110000,
            "debtors": 72000,
            "stock": 32000,
            "asset_balance": 120000,
            "accumdep": 12000,
            "creditors": 21000,
            "loan": 36000,
            "drawings": 20000,
        },
        {
            "other_income_label": "Interest income",
            "expense_items": [("Water and electricity", 11000), ("Insurance", 9000), ("Depreciation", 8000), ("Wages", 26000), ("Sundry expenses", 14000)],
            "sales": 360000,
            "debtors_allowances": 8000,
            "cost_of_sales": 220000,
            "other_income": 18000,
            "asset_label": "Fixtures",
            "bank": 88000,
            "debtors": 54000,
            "stock": 22000,
            "asset_balance": 80000,
            "accumdep": 8000,
            "creditors": 17000,
            "loan": 25000,
            "drawings": 16000,
        },
    ]
    for scenario in integrated_scenarios:
        integrated_total_expenses = _round_money(sum(float(amount) for _, amount in scenario["expense_items"]))
        integrated_net_sales = _round_money(float(scenario["sales"]) - float(scenario["debtors_allowances"]))
        integrated_gross_profit = _round_money(integrated_net_sales - float(scenario["cost_of_sales"]))
        integrated_net_profit = _round_money(integrated_gross_profit + float(scenario["other_income"]) - integrated_total_expenses)
        integrated_postclosing_total = _round_money(float(scenario["bank"]) + float(scenario["debtors"]) + float(scenario["stock"]) + float(scenario["asset_balance"]))
        integrated_closing_capital = _round_money(integrated_postclosing_total - float(scenario["accumdep"]) - float(scenario["creditors"]) - float(scenario["loan"]))
        integrated_opening_capital = _round_money(integrated_closing_capital - integrated_net_profit + float(scenario["drawings"]))
        other_income_label_lower = str(scenario["other_income_label"]).lower()
        asset_label_lower = str(scenario["asset_label"]).lower()
        expense_breakdown = " + ".join(f"R{int(amount):,}" for _, amount in scenario["expense_items"])
        integrated_prompt_tables = [
            {
                "heading": f"{biz} — Adjusted nominal balances",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Sales"), _cell(scenario["sales"])],
                    [_cell("Debtors' Allowances"), _cell(scenario["debtors_allowances"])],
                    [_cell("Cost of Sales"), _cell(scenario["cost_of_sales"])],
                    [_cell(scenario["other_income_label"]), _cell(scenario["other_income"])],
                    *[[_cell(label), _cell(amount)] for label, amount in scenario["expense_items"]],
                ],
            },
            {
                "heading": f"{biz} — Balance Sheet information after adjustments",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Bank"), _cell(scenario["bank"])],
                    [_cell("Debtors control"), _cell(scenario["debtors"])],
                    [_cell("Trading stock"), _cell(scenario["stock"])],
                    [_cell(scenario["asset_label"]), _cell(scenario["asset_balance"])],
                    [_cell(f"Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell(scenario["accumdep"])],
                    [_cell("Creditors control"), _cell(scenario["creditors"])],
                    [_cell("Loan"), _cell(scenario["loan"])],
                    [_cell("Opening capital"), _cell(integrated_opening_capital)],
                    [_cell("Drawings"), _cell(scenario["drawings"])],
                ],
            },
        ]
        integrated_tables = [
            {
                "heading": "Part A: Trading Account (extract)",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Net Sales"), _cell("", editable=True, cell_id="int-net-sales")],
                    [_cell("Cost of Sales"), _cell("", editable=True, cell_id="int-cost-sales")],
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="int-gross-profit")],
                ],
            },
            {
                "heading": "Part B: Profit and Loss Account (extract)",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="int-pl-gross-profit")],
                    [_cell("Other income"), _cell("", editable=True, cell_id="int-other-income")],
                    [_cell("Total expenses"), _cell("", editable=True, cell_id="int-total-expenses")],
                    [_cell("Net Profit"), _cell("", editable=True, cell_id="int-net-profit")],
                ],
            },
            {
                "heading": "Part C: Capital calculation",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Opening capital"), _cell("", editable=True, cell_id="int-opening-capital")],
                    [_cell("Net profit"), _cell("", editable=True, cell_id="int-capital-net-profit")],
                    [_cell("Drawings"), _cell("", editable=True, cell_id="int-drawings")],
                    [_cell("Closing capital"), _cell("", editable=True, cell_id="int-closing-capital")],
                ],
            },
            {
                "heading": "Part D: Post-closing Trial Balance (extract)",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="int-bank-debit"), _cell("")],
                    [_cell("Debtors control"), _cell("", editable=True, cell_id="int-debtors-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="int-stock-debit"), _cell("")],
                    [_cell(scenario["asset_label"]), _cell("", editable=True, cell_id="int-asset-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="int-capital-credit")],
                    [_cell(f"Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell(""), _cell("", editable=True, cell_id="int-accumdep-credit")],
                    [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="int-creditors-credit")],
                    [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="int-loan-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="int-total-debit"), _cell("", editable=True, cell_id="int-total-credit")],
                ],
            },
        ]
        integrated_correct_map = {
            "int-net-sales": integrated_net_sales,
            "int-cost-sales": scenario["cost_of_sales"],
            "int-gross-profit": integrated_gross_profit,
            "int-pl-gross-profit": integrated_gross_profit,
            "int-other-income": scenario["other_income"],
            "int-total-expenses": integrated_total_expenses,
            "int-net-profit": integrated_net_profit,
            "int-opening-capital": integrated_opening_capital,
            "int-capital-net-profit": integrated_net_profit,
            "int-drawings": scenario["drawings"],
            "int-closing-capital": integrated_closing_capital,
            "int-bank-debit": scenario["bank"],
            "int-debtors-debit": scenario["debtors"],
            "int-stock-debit": scenario["stock"],
            "int-asset-debit": scenario["asset_balance"],
            "int-capital-credit": integrated_closing_capital,
            "int-accumdep-credit": scenario["accumdep"],
            "int-creditors-credit": scenario["creditors"],
            "int-loan-credit": scenario["loan"],
            "int-total-debit": integrated_postclosing_total,
            "int-total-credit": integrated_postclosing_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the adjusted balances below to complete the multipart year-end task for {other_income_label_lower} and {asset_label_lower}: (A) Trading Account extract, (B) Profit and Loss Account extract, (C) calculate closing capital, and (D) complete the Post-closing Trial Balance extract.",
            prompt_tables=integrated_prompt_tables,
            tables=integrated_tables,
            correct_map=integrated_correct_map,
            derivation_map={
                "int-net-sales": f"Net Sales = R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{integrated_net_sales:,}",
                "int-gross-profit": f"Gross Profit = R{integrated_net_sales:,} - R{int(scenario['cost_of_sales']):,} = R{integrated_gross_profit:,}",
                "int-total-expenses": f"{expense_breakdown} = R{integrated_total_expenses:,}",
                "int-net-profit": f"Net Profit = R{integrated_gross_profit:,} + R{int(scenario['other_income']):,} - R{integrated_total_expenses:,} = R{integrated_net_profit:,}",
                "int-closing-capital": f"Closing capital = R{integrated_opening_capital:,} + R{integrated_net_profit:,} - R{int(scenario['drawings']):,} = R{integrated_closing_capital:,}",
            },
            cell_hints={
                "int-net-sales": "Start with Sales and deduct Debtors' Allowances.",
                "int-cost-sales": "Copy Cost of Sales directly from the adjusted nominal balances source table.",
                "int-gross-profit": "Gross Profit comes from the Trading Account only.",
                "int-pl-gross-profit": "Bring the Gross Profit from Part A into Part B unchanged.",
                "int-other-income": "Copy the other-income figure from the source table into Part B.",
                "int-total-expenses": "Add all listed expense items before calculating Net Profit.",
                "int-net-profit": "Net Profit = Gross Profit + Other income - Total expenses.",
                "int-opening-capital": "Use the opening capital shown in the Balance Sheet information source table.",
                "int-capital-net-profit": "Carry the Net Profit figure from Part B into Part C.",
                "int-drawings": "Copy Drawings from the Balance Sheet information source table.",
                "int-closing-capital": "Use opening capital, add net profit, then deduct drawings.",
                "int-asset-debit": f"Copy the {asset_label_lower} cost balance to the debit side of the Post-closing Trial Balance.",
                "int-capital-credit": "The Post-closing Trial Balance uses the closing capital figure from Part C.",
                "int-accumdep-credit": "Accumulated depreciation is a contra-asset with a credit balance.",
                "int-total-debit": "Add the asset-side balances in Part D and check that the credit side agrees.",
            },
            cell_teaching_map={
                "int-net-sales": _teaching_hint(
                    role_in_requirement="This cell calculates sales after deducting returns and allowances.",
                    evidence_from_question=f"Use Sales R{int(scenario['sales']):,} and Debtors' Allowances R{int(scenario['debtors_allowances']):,} from the adjusted nominal balances.",
                    rule_or_principle="Net Sales = Sales - Debtors' Allowances.",
                    how_to_derive=f"R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{integrated_net_sales:,}.",
                    transfer_tip="In Trading Account work, always net down Sales before calculating Gross Profit.",
                ),
                "int-total-expenses": _teaching_hint(
                    role_in_requirement="This cell groups all operating expenses for the Profit and Loss Account.",
                    evidence_from_question="Use every expense item listed in the adjusted nominal balances table, but exclude Cost of Sales because it belongs in the Trading Account.",
                    rule_or_principle="Total expenses in the Profit and Loss Account are the sum of all listed expenses for the period.",
                    how_to_derive=f"{expense_breakdown} = R{integrated_total_expenses:,}.",
                    transfer_tip="Separate Trading Account items from Profit and Loss items before you add expenses.",
                ),
                "int-net-profit": _teaching_hint(
                    role_in_requirement="This cell gives the final profit for the period after other income and expenses.",
                    evidence_from_question=f"Use Gross Profit R{integrated_gross_profit:,}, {scenario['other_income_label']} R{int(scenario['other_income']):,}, and Total expenses R{integrated_total_expenses:,}.",
                    rule_or_principle="Net Profit = Gross Profit + Other income - Total expenses.",
                    how_to_derive=f"R{integrated_gross_profit:,} + R{int(scenario['other_income']):,} - R{integrated_total_expenses:,} = R{integrated_net_profit:,}.",
                    transfer_tip="Treat other income as an addition after Gross Profit, then deduct all operating expenses.",
                ),
                "int-opening-capital": _teaching_hint(
                    role_in_requirement="This cell starts the capital calculation with the owner's opening equity.",
                    evidence_from_question=f"The Balance Sheet information table shows Opening capital at R{integrated_opening_capital:,}.",
                    rule_or_principle="When a capital-calculation section is given, use the opening capital from the source data as the starting figure.",
                    how_to_derive=f"Copy Opening capital = R{integrated_opening_capital:,}.",
                    transfer_tip="Capital sections often mix copied figures with derived figures, so identify which entries are direct carries first.",
                ),
                "int-closing-capital": _teaching_hint(
                    role_in_requirement="This cell calculates the owner's final equity after year-end results and drawings.",
                    evidence_from_question="Use Opening capital, Net profit, and Drawings from the tables above.",
                    rule_or_principle="Closing capital = Opening capital + Net profit - Drawings.",
                    how_to_derive=f"R{integrated_opening_capital:,} + R{integrated_net_profit:,} - R{int(scenario['drawings']):,} = R{integrated_closing_capital:,}",
                    transfer_tip="In exam-style integrated questions, carry the net profit forward into the capital section before completing the Post-closing Trial Balance.",
                ),
                "int-capital-credit": _teaching_hint(
                    role_in_requirement="This cell transfers the closing capital from Part C into the Post-closing Trial Balance.",
                    evidence_from_question="Part D depends on the answer you calculated in Part C for Closing capital.",
                    rule_or_principle="The Post-closing Trial Balance uses the final capital balance after profit and drawings have been accounted for.",
                    how_to_derive=f"Copy the closing capital amount R{integrated_closing_capital:,} into the credit column for Capital.",
                    transfer_tip="In multipart questions, always ask whether a later table needs a carry-forward from an earlier part.",
                ),
                "int-total-debit": _teaching_hint(
                    role_in_requirement="This cell gives the debit total of the Post-closing Trial Balance extract.",
                    evidence_from_question=f"Use Bank R{int(scenario['bank']):,}, Debtors control R{int(scenario['debtors']):,}, Trading stock R{int(scenario['stock']):,}, and {scenario['asset_label']} R{int(scenario['asset_balance']):,}.",
                    rule_or_principle="A correct Post-closing Trial Balance must balance, so total debits must equal total credits.",
                    how_to_derive=f"R{int(scenario['bank']):,} + R{int(scenario['debtors']):,} + R{int(scenario['stock']):,} + R{int(scenario['asset_balance']):,} = R{integrated_postclosing_total:,}.",
                    transfer_tip="Use the total row as a final check that your carried figures from earlier parts are consistent.",
                ),
            },
            guidelines=[
                "Carry answers forward from one part to the next.",
                "The net profit from Part B is used in Part C.",
                "The closing capital from Part C is used in Part D.",
            ],
            marks=24,
        ), "integrated_final_accounts_project", expected_cells=21, net_sales=integrated_net_sales, gross_profit=integrated_gross_profit, net_profit=integrated_net_profit, closing_capital=integrated_closing_capital, postclosing_total=integrated_postclosing_total))

        integrated_asset_carrying = _round_money(float(scenario["asset_balance"]) - float(scenario["accumdep"]))
        integrated_total_assets = _round_money(float(scenario["bank"]) + float(scenario["debtors"]) + float(scenario["stock"]) + integrated_asset_carrying)
        integrated_equity_liabilities_total = _round_money(integrated_closing_capital + float(scenario["creditors"]) + float(scenario["loan"]))
        integrated_paper_tables = [
            {
                "heading": "Part A: Trading Account (extract)",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Net Sales"), _cell("", editable=True, cell_id="int-net-sales")],
                    [_cell("Cost of Sales"), _cell("", editable=True, cell_id="int-cost-sales")],
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="int-gross-profit")],
                ],
            },
            {
                "heading": "Part B: Profit and Loss Account (extract)",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="int-pl-gross-profit")],
                    [_cell("Other income"), _cell("", editable=True, cell_id="int-other-income")],
                    [_cell("Total expenses"), _cell("", editable=True, cell_id="int-total-expenses")],
                    [_cell("Net Profit"), _cell("", editable=True, cell_id="int-net-profit")],
                ],
            },
            {
                "heading": "Part C: Capital calculation",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Opening capital"), _cell("", editable=True, cell_id="int-opening-capital")],
                    [_cell("Net profit"), _cell("", editable=True, cell_id="int-capital-net-profit")],
                    [_cell("Drawings"), _cell("", editable=True, cell_id="int-drawings")],
                    [_cell("Closing capital"), _cell("", editable=True, cell_id="int-closing-capital")],
                ],
            },
            {
                "heading": "Part D: Balance Sheet extract",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="int-bs-bank")],
                    [_cell("Debtors control"), _cell("", editable=True, cell_id="int-bs-debtors")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="int-bs-stock")],
                    [_cell(scenario["asset_label"]), _cell("", editable=True, cell_id="int-bs-asset-cost")],
                    [_cell(f"Less: Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell("", editable=True, cell_id="int-bs-accumdep")],
                    [_cell(f"Carrying value of {str(scenario['asset_label']).lower()}"), _cell("", editable=True, cell_id="int-bs-asset-carrying")],
                    [_cell("Total assets"), _cell("", editable=True, cell_id="int-bs-total-assets")],
                    [_cell("Capital"), _cell("", editable=True, cell_id="int-bs-capital")],
                    [_cell("Creditors control"), _cell("", editable=True, cell_id="int-bs-creditors")],
                    [_cell("Loan"), _cell("", editable=True, cell_id="int-bs-loan")],
                    [_cell("Total equity and liabilities"), _cell("", editable=True, cell_id="int-bs-total-equity-liabilities")],
                ],
            },
            {
                "heading": "Part E: Post-closing Trial Balance (extract)",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="int-bank-debit"), _cell("")],
                    [_cell("Debtors control"), _cell("", editable=True, cell_id="int-debtors-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="int-stock-debit"), _cell("")],
                    [_cell(scenario["asset_label"]), _cell("", editable=True, cell_id="int-asset-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="int-capital-credit")],
                    [_cell(f"Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell(""), _cell("", editable=True, cell_id="int-accumdep-credit")],
                    [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="int-creditors-credit")],
                    [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="int-loan-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="int-total-debit"), _cell("", editable=True, cell_id="int-total-credit")],
                ],
            },
        ]
        integrated_paper_correct_map = {
            "int-net-sales": integrated_net_sales,
            "int-cost-sales": scenario["cost_of_sales"],
            "int-gross-profit": integrated_gross_profit,
            "int-pl-gross-profit": integrated_gross_profit,
            "int-other-income": scenario["other_income"],
            "int-total-expenses": integrated_total_expenses,
            "int-net-profit": integrated_net_profit,
            "int-opening-capital": integrated_opening_capital,
            "int-capital-net-profit": integrated_net_profit,
            "int-drawings": scenario["drawings"],
            "int-closing-capital": integrated_closing_capital,
            "int-bs-bank": scenario["bank"],
            "int-bs-debtors": scenario["debtors"],
            "int-bs-stock": scenario["stock"],
            "int-bs-asset-cost": scenario["asset_balance"],
            "int-bs-accumdep": scenario["accumdep"],
            "int-bs-asset-carrying": integrated_asset_carrying,
            "int-bs-total-assets": integrated_total_assets,
            "int-bs-capital": integrated_closing_capital,
            "int-bs-creditors": scenario["creditors"],
            "int-bs-loan": scenario["loan"],
            "int-bs-total-equity-liabilities": integrated_equity_liabilities_total,
            "int-bank-debit": scenario["bank"],
            "int-debtors-debit": scenario["debtors"],
            "int-stock-debit": scenario["stock"],
            "int-asset-debit": scenario["asset_balance"],
            "int-capital-credit": integrated_closing_capital,
            "int-accumdep-credit": scenario["accumdep"],
            "int-creditors-credit": scenario["creditors"],
            "int-loan-credit": scenario["loan"],
            "int-total-debit": integrated_postclosing_total,
            "int-total-credit": integrated_postclosing_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the adjusted balances below to complete the fuller paper-style year-end task for {other_income_label_lower} and {asset_label_lower}: (A) Trading Account extract, (B) Profit and Loss Account extract, (C) calculate closing capital, (D) complete the Balance Sheet extract, and (E) complete the Post-closing Trial Balance extract.",
            prompt_tables=integrated_prompt_tables,
            tables=integrated_paper_tables,
            correct_map=integrated_paper_correct_map,
            derivation_map={
                "int-net-sales": f"Net Sales = R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{integrated_net_sales:,}",
                "int-gross-profit": f"Gross Profit = R{integrated_net_sales:,} - R{int(scenario['cost_of_sales']):,} = R{integrated_gross_profit:,}",
                "int-total-expenses": f"{expense_breakdown} = R{integrated_total_expenses:,}",
                "int-net-profit": f"Net Profit = R{integrated_gross_profit:,} + R{int(scenario['other_income']):,} - R{integrated_total_expenses:,} = R{integrated_net_profit:,}",
                "int-closing-capital": f"Closing capital = R{integrated_opening_capital:,} + R{integrated_net_profit:,} - R{int(scenario['drawings']):,} = R{integrated_closing_capital:,}",
                "int-bs-asset-carrying": f"Carrying value = cost R{int(scenario['asset_balance']):,} - accumulated depreciation R{int(scenario['accumdep']):,} = R{integrated_asset_carrying:,}",
                "int-bs-total-assets": f"Total assets = Bank R{int(scenario['bank']):,} + Debtors R{int(scenario['debtors']):,} + Stock R{int(scenario['stock']):,} + carrying value R{integrated_asset_carrying:,} = R{integrated_total_assets:,}",
            },
            cell_hints={
                "int-net-sales": "Start with Sales and deduct Debtors' Allowances.",
                "int-total-expenses": "Add all listed expense items before calculating Net Profit.",
                "int-closing-capital": "Use opening capital, add net profit, then deduct drawings.",
                "int-bs-asset-carrying": f"Show the {asset_label_lower} at cost, deduct accumulated depreciation, then calculate the carrying value.",
                "int-bs-total-assets": "Combine the current assets and the carrying value of the non-current asset.",
                "int-bs-capital": "Carry the closing capital from Part C into the Balance Sheet extract.",
                "int-total-debit": "Use the same asset-side balances from the Balance Sheet information when totaling the Post-closing Trial Balance.",
            },
            cell_teaching_map={
                "int-net-sales": _teaching_hint(
                    role_in_requirement="This cell calculates sales after deducting returns and allowances.",
                    evidence_from_question=f"Use Sales R{int(scenario['sales']):,} and Debtors' Allowances R{int(scenario['debtors_allowances']):,} from the adjusted nominal balances.",
                    rule_or_principle="Net Sales = Sales - Debtors' Allowances.",
                    how_to_derive=f"R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{integrated_net_sales:,}.",
                    transfer_tip="In Trading Account work, always net down Sales before calculating Gross Profit.",
                ),
                "int-bs-asset-carrying": _teaching_hint(
                    role_in_requirement=f"This cell converts the {asset_label_lower} cost figure into a Balance Sheet carrying value.",
                    evidence_from_question=f"The Balance Sheet information gives {scenario['asset_label']} at R{int(scenario['asset_balance']):,} and accumulated depreciation at R{int(scenario['accumdep']):,}.",
                    rule_or_principle="Balance Sheet carrying value for a depreciable asset = cost - accumulated depreciation.",
                    how_to_derive=f"R{int(scenario['asset_balance']):,} - R{int(scenario['accumdep']):,} = R{integrated_asset_carrying:,}.",
                    transfer_tip="When a paper gives both cost and accumulated depreciation, do not place the cost straight into the Balance Sheet without first finding the carrying value.",
                ),
                "int-bs-total-assets": _teaching_hint(
                    role_in_requirement="This cell totals the asset side of the Balance Sheet extract.",
                    evidence_from_question="Use Bank, Debtors control, Trading stock, and the carrying value of the non-current asset from the earlier Balance Sheet rows.",
                    rule_or_principle="Total assets equal the sum of all asset balances carried into the Balance Sheet extract.",
                    how_to_derive=f"R{int(scenario['bank']):,} + R{int(scenario['debtors']):,} + R{int(scenario['stock']):,} + R{integrated_asset_carrying:,} = R{integrated_total_assets:,}.",
                    transfer_tip="Finish each Balance Sheet subsection first, then total the asset side as a final carry-through check.",
                ),
                "int-total-debit": _teaching_hint(
                    role_in_requirement="This cell gives the debit total of the Post-closing Trial Balance extract.",
                    evidence_from_question=f"Use Bank R{int(scenario['bank']):,}, Debtors control R{int(scenario['debtors']):,}, Trading stock R{int(scenario['stock']):,}, and {scenario['asset_label']} R{int(scenario['asset_balance']):,}.",
                    rule_or_principle="A correct Post-closing Trial Balance must balance, so total debits must equal total credits.",
                    how_to_derive=f"R{int(scenario['bank']):,} + R{int(scenario['debtors']):,} + R{int(scenario['stock']):,} + R{int(scenario['asset_balance']):,} = R{integrated_postclosing_total:,}.",
                    transfer_tip="Use the total row as a final check that your carried figures from earlier parts are consistent.",
                ),
            },
            guidelines=[
                "Carry answers forward from one part to the next.",
                "The net profit from Part B is used in Part C.",
                "The closing capital from Part C is used in both the Balance Sheet extract and the Post-closing Trial Balance.",
                "On the Balance Sheet extract, reduce the non-current asset by accumulated depreciation before totaling assets.",
            ],
            marks=34,
        ), "integrated_final_accounts_project", expected_cells=32, net_sales=integrated_net_sales, gross_profit=integrated_gross_profit, net_profit=integrated_net_profit, closing_capital=integrated_closing_capital, postclosing_total=integrated_postclosing_total))

    return pool
