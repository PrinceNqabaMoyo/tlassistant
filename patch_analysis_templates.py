import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\term2\analysis_interpretation_generator.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import_insert = """
from ...sole_trader.core import fmt_money as _fmt_money
from ...sole_trader.core import make_id as _make_id
from ...sole_trader.core import round_money as _round_money
from ...sole_trader.journal_question import make_journal as _make_journal
from ...sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ...sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty
"""
if "_make_journal" not in content:
    content = content.replace("from typing import Any, Dict, List, Optional", "from typing import Any, Dict, List, Optional\n" + import_insert)

helpers = """
def _mk_journal_table(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
    force_editable_cols: Optional[List[int]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    archetype_key: str = "",
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    if force_editable_cols is not None:
        editable_cols = [int(c) for c in force_editable_cols]
    else:
        editable_cols = _journal_editable_cols_by_difficulty(
            difficulty=diff,
            base_editable_cols=base_editable_cols,
            total_cols=len(headers),
            mode=mode_norm,
        )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    for rix, vals in enumerate(values_rows):
        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct row labels and structure.",
            "Calculate the ratios and percentages correctly.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_anal_tbl_gen")
    out["expected_answer_type"] = "journal"
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out

"""

if "_mk_journal_table" not in content:
    content = content.replace("def _make_mcq", helpers + "\ndef _make_mcq")


templates = """

def _make_liquidity_ratios_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    trading_stock = _round_money(r.randint(20, 80) * 1000)
    debtors = _round_money(r.randint(15, 60) * 1000)
    bank = _round_money(r.randint(5, 40) * 1000)
    current_assets = _round_money(trading_stock + debtors + bank)
    
    creditors = _round_money(r.randint(10, 40) * 1000)
    bank_od = 0 if bank > 0 else _round_money(r.randint(10, 30) * 1000)
    current_liab = _round_money(creditors + bank_od)

    cr_ratio = round(current_assets / current_liab, 1) if current_liab > 0 else 0
    at_ratio = round((debtors + bank) / current_liab, 1) if current_liab > 0 else 0

    headers = ["Financial Indicator", "Calculation", f"Ratio for {year}"]
    rows = [
        ["Current ratio", f"{current_assets} : {current_liab}", f"{cr_ratio} : 1"],
        ["Acid test ratio", f"{debtors + bank} : {current_liab}", f"{at_ratio} : 1"],
    ]

    prompt = f\"\"\"The following appeared in the Balance Sheet of {biz} for the year ended 28 February {year}:
• Trading stock: {_money(trading_stock)}
• Debtors control: {_money(debtors)}
• Bank (favourable): {_money(bank)}
• Creditors control: {_money(creditors)}

#### REQUIRED:
Calculate the liquidity ratios for the year ended 28 February {year}. Show your calculation and express the final answer as a ratio (e.g. X : 1).\"\"\"

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_liquidity_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[{"label": biz, "value": "Liquidity Indicators"}],
        archetype_key="g11_analysis_liquidity",
    )

def _make_profitability_indicators_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    sales = _round_money(r.randint(2000, 8000) * 1000)
    cost_of_sales = _round_money(sales * r.uniform(0.45, 0.75))
    gp = _round_money(sales - cost_of_sales)
    gp_pct = round(gp / sales * 100, 1)
    
    op_exp = _round_money(sales * r.uniform(0.20, 0.45))
    op_exp_pct = round(op_exp / sales * 100, 1)
    
    net_profit = _round_money(sales * r.uniform(0.05, 0.20))
    np_pct = round(net_profit / sales * 100, 1)

    headers = ["Financial Indicator", f"Value for {year}"]
    rows = [
        ["Gross profit % on sales", f"{gp_pct}%"],
        ["Operating expenses % on sales", f"{op_exp_pct}%"],
        ["Net profit % on sales", f"{np_pct}%"],
    ]

    prompt = f\"\"\"{biz} had the following figures for the year ended 28 February {year}:
• Sales: {_money(sales)}
• Cost of sales: {_money(cost_of_sales)}
• Operating expenses: {_money(op_exp)}
• Net profit: {_money(net_profit)}

#### REQUIRED:
Calculate the profitability indicators as a percentage of sales (rounded to one decimal place).\"\"\"

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_profitability_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[{"label": biz, "value": "Profitability Indicators"}],
        archetype_key="g11_analysis_profitability",
    )
"""

if "_make_liquidity_ratios_table" not in content:
    content = content.replace("def _gen_gross_profit_pct", templates + "\ndef _gen_gross_profit_pct")

if "_make_liquidity_ratios_table" not in content:
    pass
else:
    old_gen_list = """_GENERATORS = [
    _gen_gross_profit_pct,
    _gen_net_profit_pct,"""
    new_gen_list = """_GENERATORS = [
    _make_liquidity_ratios_table,
    _make_profitability_indicators_table,
    _gen_gross_profit_pct,
    _gen_net_profit_pct,"""
    content = content.replace(old_gen_list, new_gen_list)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("added analysis templates")
