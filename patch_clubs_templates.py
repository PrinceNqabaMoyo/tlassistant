import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\term2\clubs_nonprofit_generator.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add imports
import_insert = """
from ...sole_trader.core import fmt_money as _fmt_money
from ...sole_trader.core import make_id as _make_id
from ...sole_trader.core import round_money as _round_money
from ...sole_trader.journal_question import make_journal as _make_journal
from ...sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ...sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty
from ...grade10_accounting.scenario_builder import build_scenario
"""

if "_make_journal" not in content:
    content = content.replace("from typing import Any, Dict, List, Optional", "from typing import Any, Dict, List, Optional\n" + import_insert)

# 2. Add mk_journal_table
helpers = """
def _t_account_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Amount",
        "Date",
        "Details",
        "Fol",
        "Amount",
    ]

def _fmt_amount(x: float) -> str:
    return f"{float(x):,.0f}"

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
            "Enter amounts without a currency symbol.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_club_tbl_gen")
    out["expected_answer_type"] = "journal"
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out

"""

if "_mk_journal_table" not in content:
    content = content.replace("def _make_mcq", helpers + "\ndef _make_mcq")

# 3. Add templates
templates = """

def _make_membership_fees_account(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    fee = r.choice([300, 500, 600, 750, 1000])
    members = r.randint(180, 350)
    
    opening_accrued = r.randint(5, 15) * fee
    opening_advance = r.randint(2, 8) * fee
    
    bank_received = members * fee - r.randint(2, 5) * fee + opening_accrued
    
    closing_accrued = r.randint(3, 10) * fee
    closing_advance = r.randint(1, 5) * fee
    
    written_off = r.randint(1, 4) * fee
    
    total_credits = opening_accrued + closing_advance + bank_received
    total_debits = opening_advance + closing_accrued + written_off
    income = _round_money(total_credits - total_debits)

    headers = _t_account_headers()
    rows = [
        [f"{year-1}. Dec 31", "Accrued income (Balance b/d)", "b/d", _fmt_amount(opening_accrued), f"{year-1}. Dec 31", "Income received in advance (Balance b/d)", "b/d", _fmt_amount(opening_advance)],
        ["", "", "", "", f"{year}. Dec 31", "Bank", "CRJ", _fmt_amount(bank_received)],
        [f"{year}. Dec 31", "Income received in advance (Balance c/d)", "c/d", _fmt_amount(closing_advance), f"{year}. Dec 31", "Accrued income (Balance c/d)", "c/d", _fmt_amount(closing_accrued)],
        [f"{year}. Dec 31", "Bad debts", "GJ", _fmt_amount(written_off), "", "", "", ""],
        [f"{year}. Dec 31", "Income and Expenditure", "GJ", _fmt_amount(income), "", "", "", ""],
        ["", "Totals", "", _fmt_amount(total_credits), "", "Totals", "", _fmt_amount(total_credits)],
    ]

    info_lines = [
        f"1. Balances at beginning of {year}:",
        f"   - Accrued membership fees: R{opening_accrued:,.0f}",
        f"   - Membership fees received in advance: R{opening_advance:,.0f}",
        f"2. Cash received during the year:",
        f"   - Membership fees received and deposited: R{bank_received:,.0f}",
        f"3. Balances at end of {year}:",
        f"   - Accrued membership fees: R{closing_accrued:,.0f}",
        f"   - Membership fees received in advance: R{closing_advance:,.0f}",
        f"4. Adjustments:",
        f"   - Write off unpaid fees of R{written_off:,.0f} as irrecoverable.",
    ]

    prompt = f\"\"\"{club}

#### REQUIRED:
Prepare the Membership Fees account in the General Ledger for the year ended 31 December {year}. Close off the account appropriately.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\"

    return _mk_journal_table(
        prompt=prompt,
        journal_type="clubs_membership_fees",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[3, 7],
        title_fields=[
            {"label": "General ledger", "value": club},
            {"label": "MEMBERSHIP FEES", "value": ""},
        ],
        archetype_key="g11_clubs_membership_fees_account",
    )

def _make_receipts_payments_statement(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    
    opening_bank = r.randint(25000, 60000)
    
    membership_fees = r.randint(150000, 300000)
    refreshments_sales = r.randint(40000, 80000)
    donations = r.randint(10000, 25000)
    total_receipts = membership_fees + refreshments_sales + donations
    
    wages = r.randint(60000, 100000)
    refreshments_purchases = r.randint(25000, 50000)
    equipment = r.randint(20000, 45000)
    honorarium = r.randint(10000, 20000)
    total_payments = wages + refreshments_purchases + equipment + honorarium
    
    closing_bank = opening_bank + total_receipts - total_payments
    
    headers = ["Details", "Amount"]
    rows = [
        ["Balance at beginning of year", _fmt_amount(opening_bank)],
        ["RECEIPTS", ""],
        ["Membership fees", _fmt_amount(membership_fees)],
        ["Sale of refreshments", _fmt_amount(refreshments_sales)],
        ["Donations", _fmt_amount(donations)],
        ["Total receipts", _fmt_amount(total_receipts)],
        ["", ""],
        ["PAYMENTS", ""],
        ["Wages", _fmt_amount(wages)],
        ["Purchase of refreshments", _fmt_amount(refreshments_purchases)],
        ["Equipment", _fmt_amount(equipment)],
        ["Honorarium", _fmt_amount(honorarium)],
        ["Total payments", _fmt_amount(total_payments)],
        ["", ""],
        ["Balance at end of year", _fmt_amount(closing_bank)],
    ]

    info_lines = [
        f"- Bank balance on 1 January {year}: R{opening_bank:,.0f}",
        f"- Membership fees received: R{membership_fees:,.0f}",
        f"- Sale of refreshments: R{refreshments_sales:,.0f}",
        f"- Donations received: R{donations:,.0f}",
        f"- Wages paid: R{wages:,.0f}",
        f"- Cash purchases of refreshments: R{refreshments_purchases:,.0f}",
        f"- Equipment purchased for cash: R{equipment:,.0f}",
        f"- Honorarium paid: R{honorarium:,.0f}",
    ]

    prompt = f\"\"\"{club}

#### REQUIRED:
Prepare the Statement of Receipts and Payments for the year ended 31 December {year}.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\"

    return _mk_journal_table(
        prompt=prompt,
        journal_type="clubs_receipts_payments",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[
            {"label": club, "value": ""},
            {"label": "STATEMENT OF RECEIPTS AND PAYMENTS", "value": f"for the year ended 31 December {year}"},
        ],
        archetype_key="g11_clubs_receipts_payments",
    )

def _make_income_expenditure_statement(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    
    membership_fees = r.randint(180000, 350000)
    profit_refreshments = r.randint(15000, 35000)
    donations = r.randint(10000, 25000)
    total_income = membership_fees + profit_refreshments + donations
    
    wages = r.randint(80000, 120000)
    honorarium = r.randint(15000, 25000)
    depreciation = r.randint(10000, 30000)
    water_lights = r.randint(20000, 40000)
    sundry_expenses = r.randint(5000, 15000)
    total_expenditure = wages + honorarium + depreciation + water_lights + sundry_expenses
    
    surplus = total_income - total_expenditure
    
    headers = ["Details", "Amount"]
    rows = [
        ["INCOME", ""],
        ["Membership fees", _fmt_amount(membership_fees)],
        ["Profit on refreshments", _fmt_amount(profit_refreshments)],
        ["Donations", _fmt_amount(donations)],
        ["Total income", _fmt_amount(total_income)],
        ["", ""],
        ["EXPENDITURE", ""],
        ["Wages", _fmt_amount(wages)],
        ["Honorarium", _fmt_amount(honorarium)],
        ["Depreciation", _fmt_amount(depreciation)],
        ["Water and electricity", _fmt_amount(water_lights)],
        ["Sundry expenses", _fmt_amount(sundry_expenses)],
        ["Total expenditure", _fmt_amount(total_expenditure)],
        ["", ""],
        ["Surplus for the year" if surplus >= 0 else "Deficit for the year", _fmt_amount(surplus)],
    ]

    info_lines = [
        f"- Membership fees (accrual basis): R{membership_fees:,.0f}",
        f"- Profit on sale of refreshments: R{profit_refreshments:,.0f}",
        f"- Donations received: R{donations:,.0f}",
        f"- Wages paid (including accruals): R{wages:,.0f}",
        f"- Honorarium (agreed for the year): R{honorarium:,.0f}",
        f"- Depreciation on equipment: R{depreciation:,.0f}",
        f"- Water and electricity: R{water_lights:,.0f}",
        f"- Sundry expenses: R{sundry_expenses:,.0f}",
    ]

    prompt = f\"\"\"{club}

#### REQUIRED:
Prepare the Statement of Income and Expenditure for the year ended 31 December {year}.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\"

    return _mk_journal_table(
        prompt=prompt,
        journal_type="clubs_income_expenditure",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[
            {"label": club, "value": ""},
            {"label": "STATEMENT OF INCOME AND EXPENDITURE", "value": f"for the year ended 31 December {year}"},
        ],
        archetype_key="g11_clubs_income_expenditure",
    )

"""

if "_make_membership_fees_account" not in content:
    content = content.replace("def _gen_member_count", templates + "\ndef _gen_member_count")

# Update _GENERATORS
if "_make_membership_fees_account" not in content:
    pass # we just added it above
else:
    old_gen_list = """_GENERATORS = [
    _gen_member_count,
    _gen_membership_fee_income,
    _gen_stock_profit,
    _gen_stock_theft,
    _gen_stock_turnover,
    _gen_markup_percentage,
    _gen_receipts_payments_items,
    _gen_ethics_governance,
    _gen_membership_fees_concepts,
    _gen_honorarium_offset,
    _gen_entrance_fee_members,
    _gen_refreshments_cost_of_sales,
]"""
    new_gen_list = """_GENERATORS = [
    _make_membership_fees_account,
    _make_receipts_payments_statement,
    _make_income_expenditure_statement,
    _gen_member_count,
    _gen_membership_fee_income,
    _gen_stock_profit,
    _gen_stock_theft,
    _gen_stock_turnover,
    _gen_markup_percentage,
    _gen_receipts_payments_items,
    _gen_ethics_governance,
    _gen_membership_fees_concepts,
    _gen_honorarium_offset,
    _gen_entrance_fee_members,
    _gen_refreshments_cost_of_sales,
]"""
    content = content.replace(old_gen_list, new_gen_list)

# Update subskills
old_subskill = """    pool = _GENERATORS
    if subskill_norm == "receipts_payments_items":
        pool = [_gen_receipts_payments_items]"""
new_subskill = """    pool = _GENERATORS
    if subskill_norm == "receipts_payments_items":
        pool = [_gen_receipts_payments_items]
    elif subskill_norm in ["membership", "membership_fees"]:
        pool = [_make_membership_fees_account]
    elif subskill_norm in ["receipts", "receipts_payments"]:
        pool = [_make_receipts_payments_statement]
    elif subskill_norm in ["income", "income_expenditure", "sci"]:
        pool = [_make_income_expenditure_statement]"""
content = content.replace(old_subskill, new_subskill)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("added club templates")
