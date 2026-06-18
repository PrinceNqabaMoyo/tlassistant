"""
clubs_nonprofit_generator.py — Grade 11 Term 2
================================================
Clubs & Non-profit Organisations question generator.

Archetype classes covered:
  1. Membership fees T-account
  2. Membership fee income calculation
  3. Member count calculation
  4. Stock account (vests/tracksuits/refreshments)
  5. Profit on stock items
  6. Stock turnover rate
  7. Statement of receipts & payments
  8. Items NOT in receipts & payments
  9. Honorarium account
 10. Mark-up percentage calculation
 11. Ethics/governance questions
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ...sole_trader.core import fmt_money as _fmt_money
from ...sole_trader.core import make_id as _make_id
from ...sole_trader.core import round_money as _round_money
from ...sole_trader.journal_question import make_journal as _make_journal
from ...sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ...sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty
from ...grade10_accounting.scenario_builder import build_scenario



# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


# ---------------------------------------------------------------------------
# Name / business pools for variety
# ---------------------------------------------------------------------------

_CLUB_NAMES = [
    "Langa Youth Club", "Apex Athletic Club", "Mubs Football Club",
    "Spot On Darts Club", "Mount Coke Hiking Club", "Riverside Sports Club",
    "Greenfield Community Club", "Harmony Social Club", "Ubuntu Running Club",
    "Thandi Women's Club",
]

_STOCK_ITEMS = [
    ("athletic vests", 105, 140), ("tracksuits", 120, 168),
    ("rugby jerseys", 150, 210), ("club badges", 25, 45),
    ("club caps", 60, 90), ("sports bottles", 35, 55),
]

_REFRESHMENT_DATA = [
    ("refreshments", 18, 25), ("snacks", 12, 20), ("beverages", 8, 15),
]

_FIRST_NAMES = [
    "Thabo", "Maria", "Sipho", "Nomsa", "Bongani", "Zanele",
    "Peter", "Andile", "Lesego", "Mpho", "David", "Grace",
]

_SURNAMES = [
    "Ndlovu", "Mokoena", "Naidoo", "Maseko", "Zulu", "Pillay",
    "Botha", "Mthembu", "Van Wyk", "Govender", "Radebe", "Williams",
]


# ---------------------------------------------------------------------------
# Question factories
# ---------------------------------------------------------------------------


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


def _make_mcq(*, prompt: str, options: List[str], correct_index: int,
              explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_club_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "guidelines": [explanation],
        "visual_aid_key": "clubs_nonprofit",
    }


def _make_typed(*, prompt: str, sample_answer: str,
                grading_rubric: Optional[List[str]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_club_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric or [],
        "marks": 4 if grading_rubric and len(grading_rubric) >= 2 else 2,
        "guidelines": [f"Ensure your answer includes: {', '.join(grading_rubric)}"] if grading_rubric else [],
        "visual_aid_key": "clubs_nonprofit",
    }


def _make_calc(*, prompt: str, correct_answer: float, unit: str = "R",
               working_formula: str = "") -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_club_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": correct_answer,
        "correct_answer": correct_answer,
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "marks": 3,
        "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "clubs_nonprofit",
    }


def _make_table(*, prompt: str, headers: List[str],
                rows: List[List[Any]], correct_map: Dict[str, Any],
                rubric_map: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_club_tbl"),
        "question_type": "table",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "rubric_map": rubric_map or {},
        "expected_answer_type": "table",
        "marks": len(correct_map),
        "guidelines": [],
        "visual_aid_key": "clubs_nonprofit",
    }


# ---------------------------------------------------------------------------
# Sub-skill generators
# ---------------------------------------------------------------------------



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

    prompt = f"""{club}

#### REQUIRED:
Prepare the Membership Fees account in the General Ledger for the year ended 31 December {year}. Close off the account appropriately.

#### INFORMATION:
{chr(10).join(info_lines)}"""

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

    prompt = f"""{club}

#### REQUIRED:
Prepare the Statement of Receipts and Payments for the year ended 31 December {year}.

#### INFORMATION:
{chr(10).join(info_lines)}"""

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

    prompt = f"""{club}

#### REQUIRED:
Prepare the Statement of Income and Expenditure for the year ended 31 December {year}.

#### INFORMATION:
{chr(10).join(info_lines)}"""

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


def _gen_member_count(r: random.Random) -> Dict[str, Any]:
    """Archetype class 3: Member count calculation."""
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    opening = r.randint(180, 350)
    new_members = r.randint(8, 30)
    expelled = r.randint(1, 6)
    resigned = r.randint(1, 5)

    closing = opening + new_members - expelled - resigned

    return _make_calc(
        prompt=(
            f"{club} had {opening} members on 1 January {year}. "
            f"During the year, {new_members} new members joined, "
            f"{expelled} members were expelled, and {resigned} members resigned. "
            f"Calculate the number of members at the end of {year}."
        ),
        correct_answer=float(closing),
        unit="members",
        working_formula=f"{opening} + {new_members} − {expelled} − {resigned} = {closing}",
    )


def _gen_membership_fee_income(r: random.Random) -> Dict[str, Any]:
    """Archetype class 2: Membership fee income for I&E."""
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    fee = r.choice([300, 500, 600, 750, 1000])
    members = r.randint(180, 350)
    new_members = r.randint(5, 20)
    expelled = r.randint(1, 5)
    total_members = members + new_members - expelled

    # Refund scenario
    resigned = r.randint(1, 4)
    refund_fraction = r.choice([0.5, 1.0])
    refund_total = _round_money(resigned * fee * refund_fraction)

    income = _round_money(total_members * fee - refund_total)

    return _make_calc(
        prompt=(
            f"{club} had {members} members on 1 January {year}. "
            f"The annual membership fee is R{fee}. During {year}: "
            f"{new_members} new members joined, {expelled} were expelled "
            f"(effective 1 January {year}), and {resigned} members resigned "
            f"mid-year and were each refunded "
            f"{'half' if refund_fraction == 0.5 else 'the full amount'} of their fees. "
            f"Calculate the membership fee income for the Statement of Income and Expenditure."
        ),
        correct_answer=income,
        unit="R",
        working_formula=(
            f"Total members = {members} + {new_members} − {expelled} = {total_members}. "
            f"Income = {total_members} × R{fee} − R{refund_total} = R{income}"
        ),
    )


def _gen_stock_profit(r: random.Random) -> Dict[str, Any]:
    """Archetype class 5: Profit on stock items (refreshments/vests)."""
    club = r.choice(_CLUB_NAMES)
    item, cost_price, sell_price = r.choice(_STOCK_ITEMS + _REFRESHMENT_DATA)
    year = r.choice([2022, 2023, 2024])

    opening_units = r.randint(10, 50)
    purchased_units = r.randint(100, 400)
    sold_units = r.randint(80, opening_units + purchased_units - 10)
    donated_units = r.randint(0, 5)
    closing_units = r.randint(10, 60)

    # Stolen = available - sold - donated - closing
    available = opening_units + purchased_units
    stolen_units = max(0, available - sold_units - donated_units - closing_units)
    # Adjust closing if needed
    closing_units = available - sold_units - donated_units - stolen_units

    opening_val = _round_money(opening_units * cost_price)
    purchased_val = _round_money(purchased_units * cost_price)
    sales_revenue = _round_money(sold_units * sell_price)
    cost_of_sold = _round_money(sold_units * cost_price)
    profit = _round_money(sales_revenue - cost_of_sold)

    return _make_calc(
        prompt=(
            f"{club} sells {item} at R{sell_price} each (cost price R{cost_price}). "
            f"During {year}, the club had {opening_units} {item} on hand at the start, "
            f"purchased {purchased_units} for cash, and sold {sold_units}. "
            f"Calculate the profit on the sale of {item}."
        ),
        correct_answer=profit,
        unit="R",
        working_formula=(
            f"Sales = {sold_units} × R{sell_price} = R{sales_revenue}. "
            f"Cost = {sold_units} × R{cost_price} = R{cost_of_sold}. "
            f"Profit = R{sales_revenue} − R{cost_of_sold} = R{profit}"
        ),
    )


def _gen_stock_theft(r: random.Random) -> Dict[str, Any]:
    """Stock theft detection within stock account."""
    club = r.choice(_CLUB_NAMES)
    item, cost_price, sell_price = r.choice(_STOCK_ITEMS)
    year = r.choice([2022, 2023, 2024])

    opening_units = r.randint(15, 50)
    purchased_units = r.randint(200, 400)
    sold_units = r.randint(150, opening_units + purchased_units - 50)
    returned_units = r.randint(5, 15)
    closing_count = r.randint(20, 60)

    available = opening_units + purchased_units - returned_units
    expected_remaining = available - sold_units
    stolen = max(0, expected_remaining - closing_count)

    return _make_calc(
        prompt=(
            f"{club} had {opening_units} {item} on 1 January {year}. "
            f"During the year, {purchased_units} were purchased and "
            f"{returned_units} defective ones were returned to the supplier. "
            f"{sold_units} {item} were sold. A physical stock count on "
            f"31 December {year} revealed {closing_count} {item} on hand. "
            f"Calculate the number of {item} that were stolen."
        ),
        correct_answer=float(stolen),
        unit="units",
        working_formula=(
            f"Available = {opening_units} + {purchased_units} − {returned_units} = {available}. "
            f"Should remain = {available} − {sold_units} = {expected_remaining}. "
            f"Stolen = {expected_remaining} − {closing_count} = {stolen}"
        ),
    )


def _gen_stock_turnover(r: random.Random) -> Dict[str, Any]:
    """Archetype class 6: Stock turnover rate."""
    club = r.choice(_CLUB_NAMES)
    item = r.choice(["refreshments", "club merchandise", "sports gear"])
    year = r.choice([2022, 2023, 2024])

    opening_stock = _round_money(r.randint(15, 40) * 1000)
    closing_stock = _round_money(r.randint(18, 45) * 1000)
    cost_of_sales = _round_money(r.randint(400, 900) * 1000)

    avg_stock = _round_money((opening_stock + closing_stock) / 2)
    days = round(avg_stock / cost_of_sales * 365)

    return _make_calc(
        prompt=(
            f"The following information relates to {item} at {club} "
            f"for the year ended 31 December {year}:\n"
            f"• Opening stock: {_money(opening_stock)}\n"
            f"• Closing stock: {_money(closing_stock)}\n"
            f"• Cost of sales: {_money(cost_of_sales)}\n\n"
            f"Calculate the stock holding period in days."
        ),
        correct_answer=float(days),
        unit="days",
        working_formula=(
            f"Average stock = ½({_money(opening_stock)} + {_money(closing_stock)}) = {_money(avg_stock)}. "
            f"Holding period = {_money(avg_stock)} ÷ {_money(cost_of_sales)} × 365 = {days} days"
        ),
    )


def _gen_markup_percentage(r: random.Random) -> Dict[str, Any]:
    """Archetype class 10: Mark-up percentage calculation."""
    club = r.choice(_CLUB_NAMES)
    item = r.choice(["refreshments", "club merchandise", "sports drinks"])
    year = r.choice([2022, 2023, 2024])

    cost_of_sales = _round_money(r.randint(300, 800) * 1000)
    profit = _round_money(r.randint(60, 300) * 1000)

    markup_pct = round(profit / cost_of_sales * 100)

    return _make_calc(
        prompt=(
            f"The following information was extracted from the {item} account "
            f"of {club} for the year ended 31 December {year}:\n"
            f"• Cost of sales: {_money(cost_of_sales)}\n"
            f"• Profit on sale of {item}: {_money(profit)}\n\n"
            f"Calculate the percentage mark-up used by the club."
        ),
        correct_answer=float(markup_pct),
        unit="%",
        working_formula=(
            f"{_money(profit)} ÷ {_money(cost_of_sales)} × 100 = {markup_pct}%"
        ),
    )


def _gen_receipts_payments_items(r: random.Random) -> Dict[str, Any]:
    """Archetype class 8: Items NOT recorded in Statement of Receipts & Payments."""
    club = r.choice(_CLUB_NAMES)

    # Non-cash items that should NOT appear in receipts & payments
    non_cash_items = [
        "Computer received as a donation",
        "Equipment purchased but not yet paid for",
        "Refreshments donated to charity",
        "Tennis balls purchased on credit",
        "Depreciation on equipment",
        "Accrued membership fees",
        "Stock written off due to theft",
        "Credit purchases of tracksuits",
    ]

    # Cash items that SHOULD appear
    cash_items = [
        "Membership fees received",
        "Wages paid by cheque",
        "Rent paid",
        "Cash sales of refreshments",
        "Bank charges",
        "Honorarium paid by cheque",
        "Purchase of stationery for cash",
        "Municipal grant received",
    ]

    # Pick some of each
    selected_non_cash = r.sample(non_cash_items, 4)
    selected_cash = r.sample(cash_items, 4)
    all_items = selected_non_cash + selected_cash
    r.shuffle(all_items)

    correct_set = set(selected_non_cash)
    options_text = "\n".join(f"• {item}" for item in all_items)

    correct_answer_text = "; ".join(sorted(correct_set))

    return _make_typed(
        prompt=(
            f"The following transactions occurred at {club} during the year. "
            f"Identify FOUR items that would NOT be recorded in the "
            f"Statement of Receipts and Payments:\n\n{options_text}"
        ),
        sample_answer=correct_answer_text,
        grading_rubric=[
            "Non-cash transactions are excluded from receipts & payments",
            "Credit transactions not involving bank are excluded",
            "Adjustments (depreciation, accruals, write-offs) are excluded",
            "Only actual cash inflows/outflows appear in the statement",
        ],
    )


def _gen_ethics_governance(r: random.Random) -> Dict[str, Any]:
    """Archetype class 11: Ethics/governance questions."""
    scenarios = [
        {
            "scenario": (
                "The club committee wants to discontinue the annual fundraising dinner "
                "because some members feel it attracts unwanted guests. The dinner generated "
                "a significant profit last year."
            ),
            "question": "Provide THREE valid points in a report addressing both the financial benefits and the concerns.",
            "answer": (
                "1. The dinner generates significant profit which funds club activities. "
                "2. Limit attendance to members and their partners to address behaviour concerns. "
                "3. Increase ticket prices to filter attendance while maintaining revenue."
            ),
            "rubric": [
                "Financial benefit of the event acknowledged",
                "Solution to address concerns proposed",
                "Balanced view considering both sides",
            ],
        },
        {
            "scenario": (
                "New members who join the club in November pay the same full annual "
                "membership fee as those who joined in January."
            ),
            "question": "Explain why new members may feel this is unfair and provide a solution.",
            "answer": (
                "Members joining late in the year pay the same fee but receive fewer months "
                "of membership benefits. Solution: Implement a pro-rata system where members "
                "pay only for the remaining months in the first year."
            ),
            "rubric": [
                "Unfairness of equal fee for unequal benefit period",
                "Pro-rata or monthly fee system proposed",
            ],
        },
        {
            "scenario": (
                "The treasurer of the club has been using the club's bank account "
                "to make personal purchases and replacing the money before the end of each month."
            ),
            "question": "Comment on this practice and suggest TWO control measures.",
            "answer": (
                "This is unethical and a breach of fiduciary duty. Control measures: "
                "1. Require dual signatories for all transactions above a set amount. "
                "2. Monthly bank reconciliation reviewed by a committee member other than the treasurer."
            ),
            "rubric": [
                "Identified as unethical/breach of duty",
                "Dual signatories control measure",
                "Independent review/reconciliation control measure",
            ],
        },
    ]

    chosen = r.choice(scenarios)
    club = r.choice(_CLUB_NAMES)

    return _make_typed(
        prompt=f"{club}: {chosen['scenario']}\n\n{chosen['question']}",
        sample_answer=chosen["answer"],
        grading_rubric=chosen["rubric"],
    )


def _gen_membership_fees_concepts(r: random.Random) -> Dict[str, Any]:
    """MCQ on clubs/NPO concepts."""
    questions = [
        {
            "prompt": "What is the difference between 'surplus' and 'deficit' in a non-profit organisation?",
            "options": [
                "Surplus means income exceeds expenditure; deficit means expenditure exceeds income",
                "Surplus means assets exceed liabilities; deficit means liabilities exceed assets",
                "Surplus is the same as gross profit; deficit is the same as net loss",
                "Surplus is cash in bank; deficit is an overdraft",
            ],
            "correct": 0,
            "explanation": "In NPOs, surplus = income > expenditure; deficit = expenditure > income. These replace 'profit' and 'loss'.",
        },
        {
            "prompt": "The accumulated fund in a non-profit organisation is equivalent to which concept in a trading entity?",
            "options": [
                "Capital/Owner's equity",
                "Retained income",
                "Current liabilities",
                "Fixed assets",
            ],
            "correct": 0,
            "explanation": "The accumulated fund represents the net assets of the NPO, equivalent to owner's equity.",
        },
        {
            "prompt": "An honorarium is best described as:",
            "options": [
                "A voluntary payment to a committee member for services rendered",
                "Membership fees paid in advance",
                "A donation received from a sponsor",
                "Interest earned on a fixed deposit",
            ],
            "correct": 0,
            "explanation": "An honorarium is a voluntary payment made to committee members (e.g., treasurer, secretary) for their services.",
        },
        {
            "prompt": "Membership fees received in advance should be classified as:",
            "options": [
                "Income received in advance (current liability / deferred income)",
                "Accrued income (current asset)",
                "Revenue for the current year",
                "A donation",
            ],
            "correct": 0,
            "explanation": "Fees received for the next financial year are income received in advance, a current liability.",
        },
        {
            "prompt": "Which of the following would NOT appear in a Statement of Receipts and Payments?",
            "options": [
                "Depreciation on equipment",
                "Membership fees received",
                "Wages paid by cheque",
                "Cash received from selling refreshments",
            ],
            "correct": 0,
            "explanation": "Depreciation is a non-cash item and does not appear in the Statement of Receipts and Payments.",
        },
        {
            "prompt": "Entrance fees in a club are:",
            "options": [
                "A one-time fee charged to new members when they join",
                "The same as annual membership fees",
                "Fees charged for using club facilities",
                "Fees paid to affiliate with a sports body",
            ],
            "correct": 0,
            "explanation": "Entrance fees are a once-off payment by new members upon joining the club.",
        },
    ]

    chosen = r.choice(questions)
    return _make_mcq(
        prompt=chosen["prompt"],
        options=chosen["options"],
        correct_index=chosen["correct"],
        explanation=chosen["explanation"],
    )


def _gen_honorarium_offset(r: random.Random) -> Dict[str, Any]:
    """Honorarium offset against membership fees calculation."""
    club = r.choice(_CLUB_NAMES)
    role = r.choice(["secretary", "treasurer", "chairperson"])
    year = r.choice([2022, 2023, 2024])
    honorarium = r.choice([500, 600, 750, 800, 1000, 1200])
    fee = r.choice([300, 500, 600])

    # Portion of honorarium retained for membership fee
    retained = fee
    paid = _round_money(honorarium - retained)

    return _make_calc(
        prompt=(
            f"The {role} of {club} earns an honorarium of {_money(float(honorarium))} "
            f"for the year ended 31 December {year}. "
            f"The committee agreed that the {role}'s membership fee of {_money(float(fee))} "
            f"should be offset against the honorarium. "
            f"How much will be paid in cash to the {role}?"
        ),
        correct_answer=paid,
        unit="R",
        working_formula=(
            f"Honorarium − Membership fee = {_money(float(honorarium))} − "
            f"{_money(float(fee))} = {_money(paid)}"
        ),
    )


def _gen_entrance_fee_members(r: random.Random) -> Dict[str, Any]:
    """Calculate number of new members from entrance fees."""
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])
    entrance_fee = r.choice([2000, 3000, 5000, 7500])
    total_entrance = entrance_fee * r.randint(5, 20)
    new_members = total_entrance // entrance_fee

    return _make_calc(
        prompt=(
            f"{club} received {_money(float(total_entrance))} in entrance fees "
            f"during {year}. The entrance fee is {_money(float(entrance_fee))} "
            f"per new member. How many new members joined the club?"
        ),
        correct_answer=float(new_members),
        unit="members",
        working_formula=(
            f"{_money(float(total_entrance))} ÷ {_money(float(entrance_fee))} = {new_members}"
        ),
    )


def _gen_refreshments_cost_of_sales(r: random.Random) -> Dict[str, Any]:
    """Calculate cost of sales on refreshments from stock account data."""
    club = r.choice(_CLUB_NAMES)
    year = r.choice([2022, 2023, 2024])

    opening = _round_money(r.randint(15, 35) * 1000)
    cash_purchases = _round_money(r.randint(300, 600) * 1000)
    credit_purchases = _round_money(r.randint(100, 350) * 1000)
    donated = _round_money(r.randint(5, 15) * 1000)
    closing = _round_money(r.randint(18, 40) * 1000)

    cost_of_sales = _round_money(
        opening + cash_purchases + credit_purchases - donated - closing
    )

    return _make_calc(
        prompt=(
            f"The following information relates to refreshments at {club} "
            f"for the year ended 31 December {year}:\n"
            f"• Opening stock: {_money(opening)}\n"
            f"• Cash purchases: {_money(cash_purchases)}\n"
            f"• Credit purchases: {_money(credit_purchases)}\n"
            f"• Refreshments donated to charity: {_money(donated)}\n"
            f"• Closing stock: {_money(closing)}\n\n"
            f"Calculate the cost of sales on refreshments."
        ),
        correct_answer=cost_of_sales,
        unit="R",
        working_formula=(
            f"{_money(opening)} + {_money(cash_purchases)} + {_money(credit_purchases)} "
            f"− {_money(donated)} − {_money(closing)} = {_money(cost_of_sales)}"
        ),
    )


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

_GENERATORS = [
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
]


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []
    
    subskill_norm = str(subskill or "mixed").strip().lower()
    
    pool = _GENERATORS
    if subskill_norm == "receipts_payments_items":
        pool = [_gen_receipts_payments_items]
    elif subskill_norm in ["membership", "membership_fees"]:
        pool = [_make_membership_fees_account]
    elif subskill_norm in ["receipts", "receipts_payments"]:
        pool = [_make_receipts_payments_statement]
    elif subskill_norm in ["income", "income_expenditure", "sci"]:
        pool = [_make_income_expenditure_statement]

    for _ in range(count):
        gen = r.choice(pool)
        q = gen(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)

    return questions
