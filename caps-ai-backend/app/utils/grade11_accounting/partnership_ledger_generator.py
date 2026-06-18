from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..grade10_accounting.scenario_builder import build_scenario

from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_id as _make_id
from ..sole_trader.core import round_money as _round_money
from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


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
    return _fmt_money(float(x))


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_partnership_ledger_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


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
    show_answers = mode_norm == "scaffold"

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
            "Enter amounts in the correct column.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_partnership_table")
    out["expected_answer_type"] = "journal"
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str, archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_partnership_ledger_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
        "guidelines": [f"Sample expected answer: {sample_answer}"],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold":
        out["sample_answer"] = sample_answer
    return out


def _make_t_account_question(
    *,
    prompt: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    journal_type: str,
    cell_hints: Optional[Dict[str, str]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    archetype_key: str = "",
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    # For easy: user fills in amounts only (both sides). For medium/hard: more columns become editable.
    base_editable_cols = [3, 7]
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
            "Use the correct side (Dr/Cr) for each entry.",
            "Enter amounts without a currency symbol.",
            "Close off the account where required (Balance c/d, Totals).",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )

    out["id"] = _make_id("acct11_partnership_ledger")
    out["expected_answer_type"] = "journal"
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_current_account_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Based on the Grade 11 archetype: current account with drawings and profit-share items.
    partner = r.choice(["Baloyi", "Ntuli", "Mamabolo"])
    year0 = int(r.choice([20, 21, 22, 23, 24]))
    year1 = year0 + 1

    opening = float(r.choice([6700, 16000, 24500, 32000]))
    opening_is_credit = bool(r.choice([True, True, False]))

    drawings = float(r.choice([90000, 120000, 143000, 150000]))
    interest_on_capital = float(r.choice([25000, 38750, 42000]))
    salary = float(r.choice([96000, 108000, 124000, 132000]))
    bonus = float(r.choice([0, 0, 10000, 15000]))

    # Convention:
    # Current account credits: profit items (salary/interest/bonus) typically increase owner's equity.
    # Current account debits: drawings reduce owner's equity.
    credits_total = _round_money(interest_on_capital + salary + bonus)
    debits_total = _round_money(drawings)

    # Opening balance b/d goes on the side according to opening type.
    # We close the account with balance c/d on opposite side to balance totals.
    if opening_is_credit:
        credit_sum = _round_money(opening + credits_total)
        debit_sum = _round_money(debits_total)
        balance_cd = _round_money(credit_sum - debit_sum)
        balance_cd_side = "debit"
    else:
        debit_sum = _round_money(opening + debits_total)
        credit_sum = _round_money(credits_total)
        balance_cd = _round_money(debit_sum - credit_sum)
        balance_cd_side = "credit"

    total = _round_money(max(debit_sum, credit_sum))

    headers = _t_account_headers()

    # Rows are [Dr date, Dr details, Dr fol, Dr amt, Cr date, Cr details, Cr fol, Cr amt]
    rows: List[List[Optional[str]]] = []

    # Row 0: opening balance b/d
    if opening_is_credit:
        rows.append(["", "", "", "", f"{year0}. Mar 1", "Balance b/d", "b/d", _fmt_amount(opening)])
    else:
        rows.append([f"{year0}. Mar 1", "Balance b/d", "b/d", _fmt_amount(opening), "", "", "", ""])

    # Row 1: drawings (Dr)
    rows.append([f"{year1}. Feb 28", f"Drawings: {partner}", "GJ", _fmt_amount(drawings), "", "", "", ""])

    # Profit items (Cr)
    rows.append(["", "", "", "", f"{year1}. Feb 28", "Interest on capital", "GJ", _fmt_amount(interest_on_capital)])
    if bonus > 0:
        rows.append(["", "", "", "", f"{year1}. Feb 28", "Bonus", "GJ", _fmt_amount(bonus)])
    rows.append(["", "", "", "", f"{year1}. Feb 28", f"Salary: {partner}", "GJ", _fmt_amount(salary)])

    # Balance c/d
    if balance_cd_side == "debit":
        rows.append([f"{year1}. Feb 28", "Balance c/d", "c/d", _fmt_amount(balance_cd), "", "", "", ""])
    else:
        rows.append(["", "", "", "", f"{year1}. Feb 28", "Balance c/d", "c/d", _fmt_amount(balance_cd)])

    # Totals row
    rows.append(["", "Totals", "", _fmt_amount(total), "", "Totals", "", _fmt_amount(total)])

    # Next year balance b/d (optional row to show carry forward)
    if balance_cd_side == "debit":
        rows.append(["", "", "", "", f"{year1}. Mar 1", "Balance b/d", "b/d", _fmt_amount(balance_cd)])
    else:
        rows.append([f"{year1}. Mar 1", "Balance b/d", "b/d", _fmt_amount(balance_cd), "", "", "", ""])

    info_lines = [
        f"- Balance at beginning of the year: {_fmt_amount(opening)} ({'Credit' if opening_is_credit else 'Debit'})",
        f"- Total drawings for the year: {_fmt_amount(drawings)}",
        f"- Interest on capital for the year: {_fmt_amount(interest_on_capital)}",
        f"- Partner's salary for the year: {_fmt_amount(salary)}"
    ]
    if bonus > 0:
        info_lines.append(f"- Bonus awarded for the year: {_fmt_amount(bonus)}")

    prompt = f"""Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Current Account of {partner} and close off the account.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c3"] = "Drawings are debited to the current account."
        cell_hints["t0_r2_c7"] = "Interest on capital is credited to the current account (partner's earnings)."
        if bonus > 0:
            # bonus row index shifts depending on whether bonus exists
            pass
        cell_hints["t0_r0_c7" if opening_is_credit else "t0_r0_c3"] = "Opening balance b/d is brought down on the correct side."
        cell_hints["t0_r-1_c0"] = ""  # placeholder, ignored

    # ── Build rubric_map ──
    rubric_map: Dict[str, Dict[str, Any]] = {
        # Opening balance: foundational value
        "t0_r0_c7" if opening_is_credit else "t0_r0_c3": {
            "formula_structure": "Opening balance b/d",
            "foundational_values": [opening],
            "operations": [],
            "max_score": 1.0,
        },
        # Drawings
        "t0_r1_c3": {
            "formula_structure": f"Drawings: {partner}",
            "foundational_values": [drawings],
            "operations": [],
            "max_score": 1.0,
        },
        # Interest on capital
        "t0_r2_c7": {
            "formula_structure": "Interest on capital (credited)",
            "foundational_values": [interest_on_capital],
            "operations": [],
            "max_score": 1.0,
        },
    }

    # Track row indices for variable-length rows
    cr_row = 3  # next credit row after interest on capital
    if bonus > 0:
        rubric_map[f"t0_r{cr_row}_c7"] = {
            "formula_structure": "Bonus (credited)",
            "foundational_values": [bonus],
            "operations": [],
            "max_score": 1.0,
        }
        cr_row += 1

    # Salary
    rubric_map[f"t0_r{cr_row}_c7"] = {
        "formula_structure": f"Salary: {partner} (credited)",
        "foundational_values": [salary],
        "operations": [],
        "max_score": 1.0,
    }
    cr_row += 1

    # Balance c/d
    bal_row = cr_row
    bal_col = "c3" if balance_cd_side == "debit" else "c7"
    rubric_map[f"t0_r{bal_row}_{bal_col}"] = {
        "formula_structure": "Balance c/d = Total credits − Total debits (or vice versa)",
        "foundational_values": [credit_sum if opening_is_credit else debit_sum, debit_sum if opening_is_credit else credit_sum],
        "operations": ["−"],
        "max_score": 1.5,
    }

    # ── dependency_map ──
    dep_cells = ["t0_r0_c7" if opening_is_credit else "t0_r0_c3", "t0_r1_c3", "t0_r2_c7"]
    dependency_map: Dict[str, List[str]] = {
        f"t0_r{bal_row}_{bal_col}": dep_cells,
    }

    return _make_t_account_question(
        prompt=prompt,
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        journal_type="partnership_current_account",
        cell_hints=cell_hints,
        title_fields=[
            {"label": "General ledger of partnership", "value": ""},
            {"label": f"CURRENT ACCOUNT: {partner}", "value": ""},
        ],
        archetype_key="g11_partnership_current_account",
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )


def _make_appropriation_account_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Simplified appropriation account based on Grade 11 patterns.
    partner_a = r.choice(["Baloyi", "Ntuli", "Mamabolo"])
    partner_b = r.choice([p for p in ["Shabangu", "Mathe", "Seabela"] if p != partner_a])

    year = int(r.choice([20, 21, 22, 23, 24]))

    net_profit = float(r.choice([302000, 356000, 420000]))

    salary_a = float(r.choice([120000, 124000, 144000]))
    salary_b = float(r.choice([84000, 108000, 124000]))

    interest_a = float(r.choice([30000, 38750, 45000]))
    interest_b = float(r.choice([25000, 35000, 42000]))

    bonus_a = float(r.choice([0, 0, 10000]))
    bonus_b = float(r.choice([0, 0, 10000]))

    total_appropriations = _round_money(salary_a + salary_b + interest_a + interest_b + bonus_a + bonus_b)
    remaining = _round_money(net_profit - total_appropriations)
    if remaining < 0:
        # Keep it sane by reducing bonuses first.
        bonus_a = 0.0
        bonus_b = 0.0
        total_appropriations = _round_money(salary_a + salary_b + interest_a + interest_b)
        remaining = _round_money(net_profit - total_appropriations)

    share_a = _round_money(remaining * 0.5)
    share_b = _round_money(remaining - share_a)

    headers = _t_account_headers()
    rows: List[List[Optional[str]]] = []

    # Debit side: Net profit transferred in (credit side in some conventions). For this worksheet-style T-account:
    # Put Net profit on the CREDIT side (Appropriation a/c is credited with net profit).
    rows.append(["", "", "", "", f"{year}. Feb 28", "Profit and Loss", "GJ", _fmt_amount(net_profit)])

    # Debit side: appropriations to partners
    rows.append([f"{year}. Feb 28", f"Salary: {partner_a}", "GJ", _fmt_amount(salary_a), "", "", "", ""])
    rows.append([f"{year}. Feb 28", f"Salary: {partner_b}", "GJ", _fmt_amount(salary_b), "", "", "", ""])
    rows.append([f"{year}. Feb 28", f"Interest on capital: {partner_a}", "GJ", _fmt_amount(interest_a), "", "", "", ""])
    rows.append([f"{year}. Feb 28", f"Interest on capital: {partner_b}", "GJ", _fmt_amount(interest_b), "", "", "", ""])
    if bonus_a > 0:
        rows.append([f"{year}. Feb 28", f"Bonus: {partner_a}", "GJ", _fmt_amount(bonus_a), "", "", "", ""])
    if bonus_b > 0:
        rows.append([f"{year}. Feb 28", f"Bonus: {partner_b}", "GJ", _fmt_amount(bonus_b), "", "", "", ""])

    # Remaining profit shares (debit side) transferred to current accounts
    rows.append([f"{year}. Feb 28", f"Profit share: {partner_a}", "GJ", _fmt_amount(share_a), "", "", "", ""])
    rows.append([f"{year}. Feb 28", f"Profit share: {partner_b}", "GJ", _fmt_amount(share_b), "", "", "", ""])

    debit_sum = _round_money(salary_a + salary_b + interest_a + interest_b + bonus_a + bonus_b + share_a + share_b)
    credit_sum = _round_money(net_profit)

    total = _round_money(max(debit_sum, credit_sum))

    # Totals row
    rows.append(["", "Totals", "", _fmt_amount(total), "", "Totals", "", _fmt_amount(total)])

    info_lines = [
        f"- Net profit for the year: {_fmt_amount(net_profit)}",
        f"- Partner salaries: {partner_a} {_fmt_amount(salary_a)} ; {partner_b} {_fmt_amount(salary_b)}",
        f"- Interest on capital: {partner_a} {_fmt_amount(interest_a)} ; {partner_b} {_fmt_amount(interest_b)}"
    ]
    if bonus_a > 0 or bonus_b > 0:
        info_lines.append(f"- Bonuses: {partner_a} {_fmt_amount(bonus_a)} ; {partner_b} {_fmt_amount(bonus_b)}")
    info_lines.append("- The partners share the remaining profit or loss equally.")

    prompt = f"""Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Appropriation Account for the year ended {year}. Feb 28.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c7"] = "Net profit is transferred from the Profit and Loss account to the Appropriation account."

    # ── Build rubric_map (per-cell marking metadata) ──
    # Row indexing: r0=net profit(credit), r1=salary_a, r2=salary_b, etc.
    # Amounts in col 3 (debit) and col 7 (credit) are the markable cells.
    rubric_map: Dict[str, Dict[str, Any]] = {
        "t0_r0_c7": {
            "formula_structure": "Net profit transferred from Profit and Loss",
            "foundational_values": [net_profit],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r1_c3": {
            "formula_structure": f"Salary: {partner_a} (from partnership agreement)",
            "foundational_values": [salary_a],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r2_c3": {
            "formula_structure": f"Salary: {partner_b} (from partnership agreement)",
            "foundational_values": [salary_b],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r3_c3": {
            "formula_structure": f"Interest on capital: {partner_a} = Capital × Rate",
            "foundational_values": [interest_a],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r4_c3": {
            "formula_structure": f"Interest on capital: {partner_b} = Capital × Rate",
            "foundational_values": [interest_b],
            "operations": [],
            "max_score": 1.0,
        },
    }

    # Track row index for profit shares and totals (depends on whether bonuses exist)
    debit_row = 5  # next row after interest_b
    if bonus_a > 0:
        rubric_map[f"t0_r{debit_row}_c3"] = {
            "formula_structure": f"Bonus: {partner_a}",
            "foundational_values": [bonus_a],
            "operations": [],
            "max_score": 1.0,
        }
        debit_row += 1
    if bonus_b > 0:
        rubric_map[f"t0_r{debit_row}_c3"] = {
            "formula_structure": f"Bonus: {partner_b}",
            "foundational_values": [bonus_b],
            "operations": [],
            "max_score": 1.0,
        }
        debit_row += 1

    # Profit shares
    share_a_row = debit_row
    share_b_row = debit_row + 1
    totals_row = debit_row + 2

    rubric_map[f"t0_r{share_a_row}_c3"] = {
        "formula_structure": f"Profit share: {partner_a} = (Net profit − total appropriations) × share ratio",
        "foundational_values": [net_profit, total_appropriations],
        "operations": ["−", "×"],
        "max_score": 2.0,
    }
    rubric_map[f"t0_r{share_b_row}_c3"] = {
        "formula_structure": f"Profit share: {partner_b} = Remaining profit − {partner_a}'s share",
        "foundational_values": [remaining, share_a],
        "operations": ["−"],
        "max_score": 1.5,
    }

    # Totals: 0.5 mark each (Rule 1d)

    # ── dependency_map ──
    dependency_map: Dict[str, List[str]] = {
        f"t0_r{share_a_row}_c3": ["t0_r0_c7", "t0_r1_c3", "t0_r2_c3", "t0_r3_c3", "t0_r4_c3"],
        f"t0_r{share_b_row}_c3": [f"t0_r{share_a_row}_c3"],
        f"t0_r{totals_row}_c3": [f"t0_r{share_a_row}_c3", f"t0_r{share_b_row}_c3"],
        f"t0_r{totals_row}_c7": ["t0_r0_c7"],
    }

    return _make_t_account_question(
        prompt=prompt,
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        journal_type="partnership_appropriation_account",
        cell_hints=cell_hints,
        title_fields=[
            {"label": "General ledger of partnership", "value": ""},
            {"label": "APPROPRIATION ACCOUNT", "value": ""},
        ],
        archetype_key="g11_partnership_appropriation_account",
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )


def _make_capital_account_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors exercise-style capital movements: additional capital contribution and capital withdrawal.
    partner = r.choice(["Ntuli", "Mathe", "Baloyi", "Shabangu"])
    year0 = int(r.choice([20, 21, 22, 23]))
    year1 = year0 + 1

    opening_capital = float(r.choice([350_000, 430_000, 500_000, 550_000]))
    add_capital = float(r.choice([100_000, 150_000, 200_000]))
    withdraw_capital = float(r.choice([0.0, 20_000, 50_000]))

    closing = _round_money(opening_capital + add_capital - withdraw_capital)

    headers = _t_account_headers()
    rows: List[List[Optional[str]]] = [
        [f"{year0}. Mar 1", "Balance b/d", "b/d", _fmt_amount(opening_capital), "", "", "", ""],
        ["", "", "", "", f"{year1}. Feb 28", "Additional capital", "GJ", _fmt_amount(add_capital)],
    ]
    if withdraw_capital > 0:
        rows.append([f"{year1}. Feb 28", "Bank/Drawings", "GJ", _fmt_amount(withdraw_capital), "", "", "", ""])
    rows.append(["", "Totals", "", _fmt_amount(closing), "", "Totals", "", _fmt_amount(closing)])

    info_lines = [
        f"- Balance at the beginning of the year: {_fmt_amount(opening_capital)}",
        f"- Additional capital contributed during the year: {_fmt_amount(add_capital)}"
    ]
    if withdraw_capital > 0:
        info_lines.append(f"- Capital withdrawn during the year: {_fmt_amount(withdraw_capital)}")

    prompt = f"""Partnerships — Ledger accounts

#### REQUIRED:
Draw up the Capital Account of {partner} and close off the account.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    rubric_map = {
        "t0_r0_c7": {
            "formula_structure": "Opening balance",
            "foundational_values": [opening_capital],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r1_c7": {
            "formula_structure": "Additional capital",
            "foundational_values": [add_capital],
            "operations": [],
            "max_score": 1.0,
        },
    }

    dep_cells = ["t0_r0_c7", "t0_r1_c7"]
    if withdraw_capital > 0:
        rubric_map["t0_r2_c3"] = {
            "formula_structure": "Capital withdrawal",
            "foundational_values": [withdraw_capital],
            "operations": [],
            "max_score": 1.0,
        }
        dep_cells.append("t0_r2_c3")
        bal_row = 3
    else:
        bal_row = 2

    rubric_map[f"t0_r{bal_row}_c3"] = {
        "formula_structure": "Balance c/d",
        "foundational_values": [closing],
        "operations": [],
        "max_score": 1.0,
    }
    
    dependency_map = {
        f"t0_r{bal_row}_c3": dep_cells
    }

    q = _make_t_account_question(
        prompt=prompt,
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        journal_type="partnership_capital_account",
        title_fields=[
            {"label": "General ledger of partnership", "value": ""},
            {"label": f"CAPITAL ACCOUNT: {partner}", "value": ""},
        ],
        archetype_key="g11_partnership_capital_account",
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    return q


def _make_partnership_full_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q1 pattern: appropriation + both partners' current accounts (and optional capital).
    partner_a = r.choice(["Baloyi", "Ntuli", "Mamabolo"])
    partner_b = r.choice([p for p in ["Shabangu", "Mathe", "Seabela"] if p != partner_a])

    part_app = _make_appropriation_account_question(r=r, difficulty=difficulty, mode=mode)
    part_curr_a = _make_current_account_question(r=r, difficulty=difficulty, mode=mode)
    part_curr_b = _make_current_account_question(r=r, difficulty=difficulty, mode=mode)
    part_curr_b["meta"] = {"archetype_key": "g11_partnership_current_account_partner_b"}

    prompt = f"""Partnerships — Ledger accounts

Complete the following parts for partners {partner_a} and {partner_b}."""

    return _make_bundle(
        prompt=prompt,
        parts=[part_app, part_curr_a, part_curr_b],
        archetype_key="g11_partnership_full_workflow_bundle",
    )


def _make_cash_journals_eft_update_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q2.1.3: update CRJ/CPJ based on bank statement items.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    month = r.choice(["October", "March", "May"])
    year = int(r.choice([2021, 2022, 2023]))

    crj_total_bf = float(r.choice([113_800, 95_000, 68_500]))
    cpj_total_bf = float(r.choice([98_400, 75_200, 52_700]))

    rent_income = float(r.choice([8_200, 6_500, 9_600]))
    debtor_settlement = float(r.choice([3_320, 4_250, 2_800]))
    rates = float(r.choice([2_180, 1_950, 2_600]))
    bank_charges = float(r.choice([350, 420, 280]))
    trading_stock = float(r.choice([12_300, 8_900, 15_600]))
    interest_overdraft = float(r.choice([210, 180, 260]))
    insurance = float(r.choice([1_340, 1_600, 980]))
    drawings = float(r.choice([630, 700, 520]))

    crj_total = _round_money(crj_total_bf + rent_income + debtor_settlement)
    cpj_total = _round_money(cpj_total_bf + rates + bank_charges + trading_stock + interest_overdraft + insurance + drawings)

    headers = ["CRJ: Details of sundry account", "Amount", "CPJ: Details of sundry account", "Amount"]
    rows: List[List[Optional[str]]] = [
        ["Total b/f", _fmt_amount(crj_total_bf), "Total b/f", _fmt_amount(cpj_total_bf)],
        ["Rent income", _fmt_amount(rent_income), "Rates and taxes", _fmt_amount(rates)],
        ["Debtors control", _fmt_amount(debtor_settlement), "Bank charges", _fmt_amount(bank_charges)],
        ["", "", "Trading stock", _fmt_amount(trading_stock)],
        ["", "", "Interest on overdraft", _fmt_amount(interest_overdraft)],
        ["", "", "Insurance", _fmt_amount(insurance)],
        ["", "", "Drawings", _fmt_amount(drawings)],
        ["Totals", _fmt_amount(crj_total), "Totals", _fmt_amount(cpj_total)],
    ]

    info_lines = [
        f"- Provisional CRJ total before bank statement items: {_fmt_amount(crj_total_bf)}",
        f"- Provisional CPJ total before bank statement items: {_fmt_amount(cpj_total_bf)}",
        "The following items appeared on the bank statement but not in the journals:",
        f"  * Rent income received via EFT: {_fmt_amount(rent_income)}",
        f"  * Payment received from debtor in settlement of account: {_fmt_amount(debtor_settlement)}",
        f"  * Rates and taxes paid via EFT: {_fmt_amount(rates)}",
        f"  * Bank charges: {_fmt_amount(bank_charges)}",
        f"  * Trading stock purchased via EFT: {_fmt_amount(trading_stock)}",
        f"  * Interest charged on overdraft: {_fmt_amount(interest_overdraft)}",
        f"  * Insurance premium paid via debit order: {_fmt_amount(insurance)}",
        f"  * Partner's personal drawings paid via EFT: {_fmt_amount(drawings)}"
    ]

    prompt = f"""{business}

#### REQUIRED:
Update the Cash Journals by completing the table provided in the answer book.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    return _mk_journal_table(
        prompt=prompt,
        journal_type="cash_journals_update",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 3],
        force_editable_cols=[1, 3],
        title_fields=[
            {"label": "CASH RECEIPTS JOURNAL", "value": ""},
            {"label": "CASH PAYMENTS JOURNAL", "value": ""},
        ],
        archetype_key="g11_partnership_cash_journals_eft_update",
    )


def _make_eft_advantages_typed(*, r: random.Random, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    prompt = f"""{business}

#### REQUIRED:
State THREE advantages of using Electronic Funds Transfers (EFTs).

#### INFORMATION:
Think about speed, safety, convenience and business efficiency."""
    sample = "Any THREE of: safe; convenient; quick; can be done outside banking hours; less time-consuming (no queues); instant feedback; lower charges."
    return _make_typed(prompt=prompt, sample_answer=sample, mode=mode, archetype_key="g11_partnership_eft_advantages_typed")


def _make_eft_environment_changes_typed(*, r: random.Random, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    prompt = f"""{business}

#### REQUIRED:
Explain TWO aspects of the business environment that must be changed/adapted to implement EFTs effectively.

#### INFORMATION:
Consider technology, staff training and internal controls."""
    sample = (
        "Any TWO valid points: up-to-date computer system; reliable internet connectivity; staff training / employ qualified staff; "
        "new rules and procedures (internal controls); revised source documents for EFTs; delegated authority with added supervision."
    )
    return _make_typed(prompt=prompt, sample_answer=sample, mode=mode, archetype_key="g11_partnership_eft_environment_changes_typed")


def _make_adjustments_effect_matrix(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Exercise 1 tables: effect of adjustments on accounting equation + debit/credit.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    headers = [
        "No.",
        "Assets",
        "Owner's equity",
        "Liabilities",
        "Account to debit",
        "Account to credit",
    ]

    rows: List[List[Optional[str]]] = [
        ["1.1", "", "", "", "", ""],
        ["1.2", "", "", "", "", ""],
        ["1.3", "", "", "", "", ""],
        ["1.4", "", "", "", "", ""],
    ]

    info_lines = [
        "1.1 Received R2,000 from a debtor whose account was previously written off.",
        "1.2 Trading stock to the value of R1,500 was taken by a partner for personal use.",
        "1.3 Interest on capital of R5,000 must be recorded for a partner.",
        "1.4 Provide for outstanding audit fees of R3,000."
    ]

    prompt = f"""{business}

#### REQUIRED:
Show the effect of each adjustment on the accounting equation AND indicate the account to debit and the account to credit.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    # Students must type symbols (+/-) and account names; make columns 1-5 editable.
    return _mk_journal_table(
        prompt=prompt,
        journal_type="adjustment_effects_matrix",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2, 3, 4, 5],
        force_editable_cols=[1, 2, 3, 4, 5],
        archetype_key="g11_partnership_adjustments_effect_matrix",
    )


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

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()

    pool: List[Dict[str, Any]] = []

    # Each call generates deterministic content from r.
    pool.append(_make_current_account_question(r=r, difficulty=difficulty, mode=mode))
    pool.append(_make_appropriation_account_question(r=r, difficulty=difficulty, mode=mode))
    pool.append(_make_capital_account_question(r=r, difficulty=difficulty, mode=mode))
    pool.append(_make_partnership_full_bundle(r=r, difficulty=difficulty, mode=mode))
    pool.append(_make_cash_journals_eft_update_question(r=r, difficulty=difficulty, mode=mode))
    pool.append(_make_eft_advantages_typed(r=r, mode=mode))
    pool.append(_make_eft_environment_changes_typed(r=r, mode=mode))
    pool.append(_make_adjustments_effect_matrix(r=r, difficulty=difficulty, mode=mode))

    if subskill_norm in {"current", "current_account", "partners_current"}:
        pool = [pool[0]]
    elif subskill_norm in {"appropriation", "appropriation_account"}:
        pool = [pool[1]]
    elif subskill_norm in {"capital", "capital_account"}:
        pool = [pool[2]]
    elif subskill_norm in {"bundle", "workflow", "full"}:
        pool = [pool[3]]
    elif subskill_norm in {"cash", "cash-journals", "journals"}:
        pool = [pool[4], pool[5], pool[6]]
    elif subskill_norm in {"eft", "eft-journals", "eft_journals", "cash-eft"}:
        pool = [pool[4]]
    elif subskill_norm in {"eft-advantages", "eft_advantages"}:
        pool = [pool[5]]
    elif subskill_norm in {"eft-environment", "eft_environment", "eft-changes", "eft_changes"}:
        pool = [pool[6]]
    elif subskill_norm in {"adjustments", "equation", "matrix"}:
        pool = [pool[7]]

    if qtype_norm != "mixed":
        pool = [q for q in pool if str(q.get("question_type") or "").strip().lower() == qtype_norm]

    if not pool:
        pool = [_make_current_account_question(r=r, difficulty=difficulty, mode=mode)]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out
