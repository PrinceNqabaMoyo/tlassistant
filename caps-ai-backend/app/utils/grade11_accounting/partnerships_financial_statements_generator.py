"""Grade 11 Accounting — Partnerships: Financial Statements & Notes.
100% Deterministic Python generator aligned with CAPS Term 1 & Term 2 syllabus.
Covers:
- Exam Ceiling (mode="compound" - 15 marks):
  * Complete 2D tabular Current Accounts Note (Note 5) and General Ledger Appropriation Account for partners A and B.
  * Calculates: Interest on Capital at r% p.a. (with time-apportioned capital changes),
    Partner Salaries (with mid-year monthly increases), Performance Bonuses,
    Primary Distribution, and Remaining Profit/Loss distributed via agreed partnership ratio (e.g. 3:2).
  * Drawings during the year (subtracted, displayed in brackets).
  * Opening balance (credit positive, debit negative/bracketed) and Closing current account balance.
  * 2D tabular matrix with cell coordinates `t0_r{rix}_c{cix}`, cell types (`required`, `given`, `must_be_empty`),
    `correct_map`, and contextual cell hints.
  * Deduction rules: `{"rule": "must_be_empty_filled", "penalty": -1}`.
  * Misconception tags: `added_instead_of_subtracted_drawings`, `omitted_interest_on_capital`,
    `inverted_profit_sharing_ratio`, `forgot_salary_increase_months`.
- Adaptive Scaffolding Sub-drills (3-4 marks each):
  * `elementary_interest_on_capital`: Time-apportioned interest with mid-year capital change.
  * `elementary_salaries_bonus`: Monthly salary with mid-year percentage increase and bonus.
  * `elementary_profit_share_ratio`: Allocating final remaining profit/loss via integer ratios.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

try:
    from ..sa_naming_engine import generate_sa_enterprise, pick_surname
except ImportError:
    from app.utils.sa_naming_engine import generate_sa_enterprise, pick_surname


MISCONCEPTION_DRAWINGS_ADDED = "added_instead_of_subtracted_drawings"
MISCONCEPTION_OMITTED_INTEREST = "omitted_interest_on_capital"
MISCONCEPTION_INVERTED_RATIO = "inverted_profit_sharing_ratio"
MISCONCEPTION_SALARY_INCREASE = "forgot_salary_increase_months"


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_money(val: float | int) -> str:
    """Format an integer/float amount with thousand separators."""
    ival = int(round(float(val)))
    return f"{ival:,}".replace(",", " ")


def _fmt_bracket(val: float | int) -> str:
    """Format a negative or outgoing amount in accounting brackets."""
    ival = abs(int(round(float(val))))
    return f"({_fmt_money(ival)})"


def _format_cell_val(val: float | int, is_negative_bracket: bool = False) -> str:
    ival = int(round(float(val)))
    if is_negative_bracket and ival < 0:
        return _fmt_bracket(ival)
    if is_negative_bracket and ival > 0:
        # For rows like drawings that are always negative
        return _fmt_bracket(ival)
    if ival < 0:
        return _fmt_bracket(ival)
    return _fmt_money(ival)


# ============================================================================
# SUB-DRILL 1: Elementary Interest on Capital
# ============================================================================
def _build_elementary_interest_on_capital(r: random.Random) -> Dict[str, Any]:
    partner = r.choice(["Mokoena", "Naidoo", "Dlamini", "Botha", "Sithole", "Khumalo"])
    business = f"{partner} & Partner Traders"
    
    cap_start = r.choice([300_000, 400_000, 500_000, 600_000])
    cap_increase = r.choice([60_000, 100_000, 120_000, 150_000])
    rate = r.choice([8, 10, 12, 15])  # percent p.a.
    
    # Capital increased on 1 September (6 months) or 1 December (9 months)
    change_month_name, m1, m2 = r.choice([
        ("1 September 2025 (6 months into the financial year)", 6, 6),
        ("1 December 2025 (9 months into the financial year)", 9, 3),
        ("1 June 2025 (3 months into the financial year)", 3, 9),
    ])
    
    cap_end = cap_start + cap_increase
    interest_p1 = int(round(cap_start * (rate / 100.0) * (m1 / 12.0)))
    interest_p2 = int(round(cap_end * (rate / 100.0) * (m2 / 12.0)))
    total_interest = interest_p1 + interest_p2

    prompt = (
        f"The financial year of **{business}** ends on 28 February 2026.\n\n"
        f"• On 1 March 2025, the capital balance of Partner {partner} was **R{_fmt_money(cap_start)}**.\n"
        f"• On {change_month_name}, {partner} contributed an additional **R{_fmt_money(cap_increase)}** towards capital.\n"
        f"• The partnership agreement stipulates interest on capital at **{rate}% p.a.**\n\n"
        f"**Required:**\n"
        f"Calculate the total interest on capital credited to Partner {partner} for the financial year ended 28 February 2026."
    )

    sample_answer = (
        f"1. Period 1 ({m1} months @ R{_fmt_money(cap_start)}):\n"
        f"   R{_fmt_money(cap_start)} × {rate}% × {m1}/12 = R{_fmt_money(interest_p1)}\n"
        f"2. Period 2 ({m2} months @ R{_fmt_money(cap_end)}):\n"
        f"   R{_fmt_money(cap_end)} × {rate}% × {m2}/12 = R{_fmt_money(interest_p2)}\n"
        f"Total Interest on Capital = R{_fmt_money(interest_p1)} + R{_fmt_money(interest_p2)} = R{_fmt_money(total_interest)}"
    )

    marking_points = [
        {"id": "mp1", "desc": f"Interest for initial period ({m1} months): R{_fmt_money(interest_p1)}", "marks": 1, "editable": True},
        {"id": "mp2", "desc": f"Correct increased capital base: R{_fmt_money(cap_end)}", "marks": 1, "editable": True},
        {"id": "mp3", "desc": f"Interest for second period ({m2} months): R{_fmt_money(interest_p2)}", "marks": 1, "editable": True},
        {"id": "mp4", "desc": f"Total interest on capital: R{_fmt_money(total_interest)}", "marks": 1, "editable": True},
    ]

    return {
        "id": f"acc11_part_ioc_{r.randint(100000, 999999)}",
        "title": "Interest on Capital with Capital Changes",
        "topic": "Partnerships",
        "subskill": "elementary_interest_on_capital",
        "mode": "elementary_interest_on_capital",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "question_type": "calc",
        "ideal_answer": f"R{_fmt_money(total_interest)}",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": [MISCONCEPTION_OMITTED_INTEREST, "failed_to_time_apportion_capital_change"],
        "correct_map": {"interest_on_capital": str(total_interest)},
        "marking_schema": {
            "total_marks": 4,
            "marking_points": marking_points,
            "deductions": [
                {"rule": "calculated_on_closing_balance_only", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Split the financial year into two periods: before and after the capital contribution.",
            "tier2_directional_rule": (
                f"Calculate interest on R{_fmt_money(cap_start)} for {m1} months, and on R{_fmt_money(cap_end)} "
                f"(R{_fmt_money(cap_start)} + R{_fmt_money(cap_increase)}) for the remaining {m2} months."
            ),
            "tier3_worked_step": sample_answer,
        },
    }


# ============================================================================
# SUB-DRILL 2: Elementary Partner Salaries & Bonus
# ============================================================================
def _build_elementary_salaries_bonus(r: random.Random) -> Dict[str, Any]:
    partner = r.choice(["Naidoo", "Mokoena", "Van der Merwe", "Cele", "Pillay", "Baloyi"])
    business = f"{partner} Enterprises"

    salary_initial = r.choice([12_000, 14_000, 15_000, 18_000, 20_000])
    inc_pct = r.choice([10, 15, 20])
    salary_increased = int(round(salary_initial * (1 + inc_pct / 100.0)))
    
    m1 = r.choice([6, 7, 8])
    m2 = 12 - m1
    inc_month_name = "1 September" if m1 == 6 else ("1 October" if m1 == 7 else "1 November")

    salary_part1 = salary_initial * m1
    salary_part2 = salary_increased * m2
    total_salary = salary_part1 + salary_part2

    bonus = r.choice([12_000, 15_000, 18_000, 24_000])
    total_earnings = total_salary + bonus

    prompt = (
        f"Partner **{partner}** in **{business}** was entitled to the following remuneration "
        f"for the financial year ended 28 February 2026:\n\n"
        f"• A salary of **R{_fmt_money(salary_initial)} per month** for the first {m1} months of the year.\n"
        f"• Effective **{inc_month_name}**, the monthly salary increased by **{inc_pct}%** for the remaining {m2} months.\n"
        f"• A performance bonus of **R{_fmt_money(bonus)}** for meeting operational KPIs.\n\n"
        f"**Required:**\n"
        f"1. Calculate {partner}'s total salary for the financial year.\n"
        f"2. Calculate {partner}'s total remuneration (salary + bonus) for the financial year."
    )

    sample_answer = (
        f"1. Monthly salary after increase: R{_fmt_money(salary_initial)} × {100 + inc_pct}% = R{_fmt_money(salary_increased)}\n"
        f"2. Initial period ({m1} months): {m1} × R{_fmt_money(salary_initial)} = R{_fmt_money(salary_part1)}\n"
        f"3. Increased period ({m2} months): {m2} × R{_fmt_money(salary_increased)} = R{_fmt_money(salary_part2)}\n"
        f"Total Annual Salary = R{_fmt_money(salary_part1)} + R{_fmt_money(salary_part2)} = R{_fmt_money(total_salary)}\n"
        f"Total Remuneration = Total Salary (R{_fmt_money(total_salary)}) + Bonus (R{_fmt_money(bonus)}) = R{_fmt_money(total_earnings)}"
    )

    marking_points = [
        {"id": "mp1", "desc": f"Increased monthly salary: R{_fmt_money(salary_increased)}", "marks": 1, "editable": True},
        {"id": "mp2", "desc": f"Salary for first {m1} months: R{_fmt_money(salary_part1)}", "marks": 1, "editable": True},
        {"id": "mp3", "desc": f"Salary for remaining {m2} months: R{_fmt_money(salary_part2)}", "marks": 1, "editable": True},
        {"id": "mp4", "desc": f"Total annual salary (R{_fmt_money(total_salary)}) and remuneration (R{_fmt_money(total_earnings)})", "marks": 1, "editable": True},
    ]

    return {
        "id": f"acc11_part_sal_{r.randint(100000, 999999)}",
        "title": "Partner Salary and Performance Bonus Calculation",
        "topic": "Partnerships",
        "subskill": "elementary_salaries_bonus",
        "mode": "elementary_salaries_bonus",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "question_type": "calc",
        "ideal_answer": f"Total Salary: R{_fmt_money(total_salary)}; Total Remuneration: R{_fmt_money(total_earnings)}",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": [MISCONCEPTION_SALARY_INCREASE, "omitted_bonus"],
        "correct_map": {
            "total_salary": str(total_salary),
            "total_remuneration": str(total_earnings),
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": marking_points,
            "deductions": [
                {"rule": "multiplied_increased_salary_by_12", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Calculate the salary for each portion of the year separately before adding the bonus.",
            "tier2_directional_rule": (
                f"Increased salary = R{_fmt_money(salary_initial)} × {100 + inc_pct}%. "
                f"Total salary = ({m1} × R{_fmt_money(salary_initial)}) + ({m2} × R{_fmt_money(salary_increased)})."
            ),
            "tier3_worked_step": sample_answer,
        },
    }


# ============================================================================
# SUB-DRILL 3: Elementary Profit Sharing Ratio
# ============================================================================
def _build_elementary_profit_share_ratio(r: random.Random) -> Dict[str, Any]:
    partner_a, partner_b = r.choice([
        ("Mokoena", "Naidoo"),
        ("Dlamini", "Botha"),
        ("Sithole", "Van Zyl"),
        ("Khumalo", "Moodley"),
    ])
    business = f"{partner_a} & {partner_b} Traders"

    ratio_a, ratio_b = r.choice([(3, 2), (2, 1), (5, 3), (3, 1)])
    total_parts = ratio_a + ratio_b

    # Choose clean remaining profit
    multiplier = r.randint(15, 40) * 1000
    remaining_profit = total_parts * multiplier
    primary_dist = r.randint(20, 50) * 10_000
    net_profit = primary_dist + remaining_profit

    share_a = int(round(remaining_profit * (ratio_a / total_parts)))
    share_b = int(round(remaining_profit * (ratio_b / total_parts)))

    prompt = (
        f"**{business}** earned a **Net Profit of R{_fmt_money(net_profit)}** for the year ended 28 February 2026.\n\n"
        f"• Total primary distributions (salaries, interest on capital, and bonuses) allocated to the partners amounted to **R{_fmt_money(primary_dist)}**.\n"
        f"• According to the partnership agreement, the remaining profit is shared between **{partner_a}** and **{partner_b}** in the ratio **{ratio_a}:{ratio_b}**.\n\n"
        f"**Required:**\n"
        f"1. Calculate the remaining profit available for final distribution.\n"
        f"2. Calculate {partner_a}'s share of the remaining profit.\n"
        f"3. Calculate {partner_b}'s share of the remaining profit."
    )

    sample_answer = (
        f"1. Remaining Profit = Net Profit (R{_fmt_money(net_profit)}) – Primary Distribution (R{_fmt_money(primary_dist)}) = R{_fmt_money(remaining_profit)}\n"
        f"2. Total ratio parts = {ratio_a} + {ratio_b} = {total_parts}\n"
        f"3. {partner_a}'s share = R{_fmt_money(remaining_profit)} × {ratio_a}/{total_parts} = R{_fmt_money(share_a)}\n"
        f"4. {partner_b}'s share = R{_fmt_money(remaining_profit)} × {ratio_b}/{total_parts} = R{_fmt_money(share_b)}"
    )

    marking_points = [
        {"id": "mp1", "desc": f"Remaining profit calculation: R{_fmt_money(remaining_profit)}", "marks": 1, "editable": True},
        {"id": "mp2", "desc": f"{partner_a}'s share ({ratio_a}/{total_parts}): R{_fmt_money(share_a)}", "marks": 1, "editable": True},
        {"id": "mp3", "desc": f"{partner_b}'s share ({ratio_b}/{total_parts}): R{_fmt_money(share_b)}", "marks": 1, "editable": True},
    ]

    return {
        "id": f"acc11_part_ratio_{r.randint(100000, 999999)}",
        "title": "Partnership Final Profit Distribution Ratio",
        "topic": "Partnerships",
        "subskill": "elementary_profit_share_ratio",
        "mode": "elementary_profit_share_ratio",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "question_type": "calc",
        "ideal_answer": f"Remaining Profit: R{_fmt_money(remaining_profit)}; {partner_a}: R{_fmt_money(share_a)}; {partner_b}: R{_fmt_money(share_b)}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": [MISCONCEPTION_INVERTED_RATIO, "confused_net_profit_with_remaining_profit"],
        "correct_map": {
            "remaining_profit": str(remaining_profit),
            "share_partner_a": str(share_a),
            "share_partner_b": str(share_b),
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": marking_points,
            "deductions": [
                {"rule": "inverted_profit_sharing_ratio", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Deduct total primary distribution from net profit to obtain the remaining profit.",
            "tier2_directional_rule": (
                f"Sum the ratio parts ({ratio_a} + {ratio_b} = {total_parts}). "
                f"Multiply the remaining profit by {ratio_a}/{total_parts} and {ratio_b}/{total_parts}."
            ),
            "tier3_worked_step": sample_answer,
        },
    }


# ============================================================================
# EXAM CEILING (mode="compound" - 15 Marks): Complete Current Accounts Note & Appropriation
# ============================================================================
def _build_compound_partnerships_statements(r: random.Random) -> Dict[str, Any]:
    partner_a, partner_b = r.choice([
        ("Mokoena", "Naidoo"),
        ("Dlamini", "Botha"),
        ("Sithole", "Van Zyl"),
        ("Khumalo", "Chetty"),
    ])
    business = f"{partner_a} & {partner_b} Traders"
    fin_year_end = "28 February 2026"

    # 1. Capital & Interest on Capital
    cap_a_start = r.choice([350_000, 400_000, 450_000, 500_000])
    cap_a_inc = r.choice([50_000, 100_000])
    cap_b_fixed = r.choice([250_000, 300_000, 350_000])
    rate = r.choice([10, 12])  # %

    # Partner A contributed additional capital on 1 September (6 months)
    cap_a_end = cap_a_start + cap_a_inc
    interest_a = int(round(cap_a_start * (rate / 100.0) * (6 / 12.0) + cap_a_end * (rate / 100.0) * (6 / 12.0)))
    interest_b = int(round(cap_b_fixed * (rate / 100.0)))
    total_interest = interest_a + interest_b

    # 2. Salaries with mid-year increase
    sal_a_base = r.choice([14_000, 15_000, 16_000])
    sal_a_inc = int(round(sal_a_base * 1.10))  # 10% increase from 1 Sep (6 months)
    salary_a = (sal_a_base * 6) + (sal_a_inc * 6)

    sal_b_base = r.choice([11_000, 12_000, 13_000])
    sal_b_inc = sal_b_base + 1_500  # R1500 increase for last 4 months
    salary_b = (sal_b_base * 8) + (sal_b_inc * 4)
    total_salaries = salary_a + salary_b

    # 3. Performance Bonus (Only Partner A is entitled to a bonus; Partner B cell must be empty)
    bonus_a = r.choice([15_000, 18_000, 20_000])
    bonus_b = 0
    total_bonus = bonus_a

    # 4. Primary Distribution
    primary_a = salary_a + interest_a + bonus_a
    primary_b = salary_b + interest_b + bonus_b
    total_primary = primary_a + primary_b

    # 5. Remaining Profit / Loss & Ratio
    ratio_a, ratio_b = r.choice([(3, 2), (2, 1), (5, 3)])
    total_parts = ratio_a + ratio_b
    multiplier = r.randint(15, 30) * 1000
    remaining_profit = total_parts * multiplier
    net_profit = total_primary + remaining_profit

    final_a = int(round(remaining_profit * (ratio_a / total_parts)))
    final_b = int(round(remaining_profit * (ratio_b / total_parts)))
    total_final = final_a + final_b

    # Profit per Income Statement
    profit_per_is_a = primary_a + final_a
    profit_per_is_b = primary_b + final_b
    total_profit_per_is = profit_per_is_a + profit_per_is_b  # Equals net_profit

    # 6. Drawings during the year
    drawings_a = r.randint(int(profit_per_is_a * 0.70 / 1000), int(profit_per_is_a * 0.85 / 1000)) * 1000
    drawings_b = r.randint(int(profit_per_is_b * 0.70 / 1000), int(profit_per_is_b * 0.85 / 1000)) * 1000
    total_drawings = drawings_a + drawings_b

    # 7. Retained Income for the year
    retained_a = profit_per_is_a - drawings_a
    retained_b = profit_per_is_b - drawings_b
    total_retained = retained_a + retained_b

    # 8. Opening Balances (Partner A credit, Partner B debit)
    open_a = r.choice([18_000, 22_000, 28_000, 35_000])  # Credit
    open_b = -r.choice([6_000, 8_000, 10_000, 12_000])   # Debit (bracketed)
    total_open = open_a + open_b

    # 9. Closing Balances (Balance at end of year)
    close_a = open_a + retained_a
    close_b = open_b + retained_b
    total_close = close_a + close_b

    prompt = (
        f"You are provided with financial information relating to **{business}** for the financial year ended **{fin_year_end}**.\n\n"
        f"**FINANCIAL INFORMATION:**\n"
        f"1. **Capital balances on 1 March 2025:**\n"
        f"   • {partner_a}: R{_fmt_money(cap_a_start)}\n"
        f"   • {partner_b}: R{_fmt_money(cap_b_fixed)}\n"
        f"   *Note: On 1 September 2025, Partner {partner_a} contributed an additional R{_fmt_money(cap_a_inc)} towards capital. "
        f"This has been recorded.*\n\n"
        f"2. **Interest on Capital:**\n"
        f"   • Interest on capital is provided at **{rate}% p.a.** on capital balances.\n\n"
        f"3. **Partners' Salaries:**\n"
        f"   • {partner_a} earned R{_fmt_money(sal_a_base)} per month for the first 6 months. On 1 September 2025, {partner_a}'s salary "
        f"increased by 10% for the remainder of the financial year.\n"
        f"   • {partner_b} earned R{_fmt_money(sal_b_base)} per month for the first 8 months, increasing by R1 500 per month for the remaining 4 months.\n\n"
        f"4. **Performance Bonus:**\n"
        f"   • Partner {partner_a} is entitled to an annual performance bonus of **R{_fmt_money(bonus_a)}**. "
        f"Partner {partner_b} does not receive a bonus.\n\n"
        f"5. **Profit Distribution:**\n"
        f"   • Net Profit per the Income Statement before appropriation was **R{_fmt_money(net_profit)}**.\n"
        f"   • The remaining profit is shared between {partner_a} and {partner_b} in the agreed ratio of **{ratio_a}:{ratio_b}**.\n\n"
        f"6. **Drawings and Current Accounts:**\n"
        f"   • Total drawings during the year: {partner_a} R{_fmt_money(drawings_a)}; {partner_b} R{_fmt_money(drawings_b)}.\n"
        f"   • Balances on 1 March 2025:\n"
        f"     - Current account: {partner_a}: R{_fmt_money(open_a)} (Credit)\n"
        f"     - Current account: {partner_b}: R{_fmt_money(abs(open_b))} (Debit)\n\n"
        f"**REQUIRED:**\n"
        f"Complete the **Note to the Financial Statements: Current Accounts** (Note 5) for the year ended {fin_year_end}."
    )

    headers = ["Current Accounts Note", partner_a, partner_b, "Total"]

    # Table layout: (label, val_a, val_b, val_total, type_a, type_b, type_total, is_negative_row)
    rows_definition = [
        ("Salaries to partners", salary_a, salary_b, total_salaries, "required", "required", "required", False),
        ("Interest on capital", interest_a, interest_b, total_interest, "required", "required", "required", False),
        ("Bonus to partners", bonus_a, None, total_bonus, "required", "must_be_empty", "required", False),
        ("Primary distribution of profit", primary_a, primary_b, total_primary, "required", "required", "required", False),
        ("Final distribution of profit", final_a, final_b, total_final, "required", "required", "required", False),
        ("Profit per Income Statement", profit_per_is_a, profit_per_is_b, total_profit_per_is, "required", "required", "given", False),
        ("Drawings during the year", drawings_a, drawings_b, total_drawings, "required", "required", "required", True),
        ("Retained income for the year", retained_a, retained_b, total_retained, "required", "required", "required", False),
        ("Balance at beginning of year", open_a, open_b, total_open, "given", "given", "required", False),
        ("Balance at end of year", close_a, close_b, total_close, "required", "required", "required", False),
    ]

    rows_data: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (label, va, vb, vt, type_a, type_b, type_tot, is_neg) in enumerate(rows_definition):
        row_cells = []
        # Col 0: Description (given, not editable)
        row_cells.append({
            "coordinate": f"t0_r{rix}_c0",
            "cell_id": f"t0_r{rix}_c0",
            "value": label,
            "type": "given",
            "cell_type": "given",
            "editable": False,
        })

        # Col 1: Partner A
        coord_a = f"t0_r{rix}_c1"
        str_va = _format_cell_val(va, is_neg) if va is not None else ""
        correct_map[coord_a] = str_va
        row_cells.append({
            "coordinate": coord_a,
            "cell_id": coord_a,
            "value": str_va if type_a == "given" else "",
            "type": type_a,
            "cell_type": type_a,
            "editable": type_a != "given",
        })

        # Col 2: Partner B
        coord_b = f"t0_r{rix}_c2"
        str_vb = _format_cell_val(vb, is_neg) if vb is not None else ""
        correct_map[coord_b] = str_vb
        row_cells.append({
            "coordinate": coord_b,
            "cell_id": coord_b,
            "value": str_vb if type_b == "given" else "",
            "type": type_b,
            "cell_type": type_b,
            "editable": type_b != "given",
        })

        # Col 3: Total
        coord_tot = f"t0_r{rix}_c3"
        str_vt = _format_cell_val(vt, is_neg) if vt is not None else ""
        correct_map[coord_tot] = str_vt
        row_cells.append({
            "coordinate": coord_tot,
            "cell_id": coord_tot,
            "value": str_vt if type_tot == "given" else "",
            "type": type_tot,
            "cell_type": type_tot,
            "editable": type_tot != "given",
        })

        rows_data.append(row_cells)

    # Populate cell hints
    cell_hints["t0_r0_c1"] = f"{partner_a} salary = (6 × R{_fmt_money(sal_a_base)}) + (6 × R{_fmt_money(sal_a_inc)}) = R{_fmt_money(salary_a)}"
    cell_hints["t0_r0_c2"] = f"{partner_b} salary = (8 × R{_fmt_money(sal_b_base)}) + (4 × R{_fmt_money(sal_b_inc)}) = R{_fmt_money(salary_b)}"
    cell_hints["t0_r1_c1"] = f"{partner_a} interest = (R{_fmt_money(cap_a_start)} × {rate}% × 6/12) + (R{_fmt_money(cap_a_end)} × {rate}% × 6/12) = R{_fmt_money(interest_a)}"
    cell_hints["t0_r1_c2"] = f"{partner_b} interest = R{_fmt_money(cap_b_fixed)} × {rate}% = R{_fmt_money(interest_b)}"
    cell_hints["t0_r2_c1"] = f"Performance bonus awarded to {partner_a} = R{_fmt_money(bonus_a)}"
    cell_hints["t0_r2_c2"] = f"{partner_b} was not awarded a bonus. This cell MUST remain empty."
    cell_hints["t0_r3_c1"] = f"Primary distribution = Salaries + Interest + Bonus for {partner_a} = R{_fmt_money(primary_a)}"
    cell_hints["t0_r3_c2"] = f"Primary distribution = Salaries + Interest + Bonus for {partner_b} = R{_fmt_money(primary_b)}"
    cell_hints["t0_r4_c1"] = f"Remaining profit share = R{_fmt_money(remaining_profit)} × {ratio_a}/{total_parts} = R{_fmt_money(final_a)}"
    cell_hints["t0_r4_c2"] = f"Remaining profit share = R{_fmt_money(remaining_profit)} × {ratio_b}/{total_parts} = R{_fmt_money(final_b)}"
    cell_hints["t0_r6_c1"] = f"Drawings must be shown in brackets (subtracted): ({_fmt_money(drawings_a)})"
    cell_hints["t0_r6_c2"] = f"Drawings must be shown in brackets (subtracted): ({_fmt_money(drawings_b)})"
    cell_hints["t0_r7_c1"] = f"Retained income = Profit per Income Statement (R{_fmt_money(profit_per_is_a)}) – Drawings (R{_fmt_money(drawings_a)}) = R{_fmt_money(retained_a)}"
    cell_hints["t0_r7_c2"] = f"Retained income = Profit per Income Statement (R{_fmt_money(profit_per_is_b)}) – Drawings (R{_fmt_money(drawings_b)}) = R{_fmt_money(retained_b)}"
    cell_hints["t0_r9_c1"] = f"Closing Balance = Opening Balance (R{_fmt_money(open_a)}) + Retained Income (R{_fmt_money(retained_a)}) = R{_fmt_money(close_a)}"
    cell_hints["t0_r9_c2"] = f"Closing Balance = Opening Debit Balance (R{_fmt_money(open_b)}) + Retained Income (R{_fmt_money(retained_b)}) = R{_fmt_money(close_b)}"

    marking_points = [
        {"id": "mp_sal_a", "desc": f"Salaries to {partner_a}: R{_fmt_money(salary_a)}", "marks": 2, "editable": True},
        {"id": "mp_sal_b", "desc": f"Salaries to {partner_b}: R{_fmt_money(salary_b)}", "marks": 2, "editable": True},
        {"id": "mp_ioc_a", "desc": f"Interest on capital for {partner_a}: R{_fmt_money(interest_a)}", "marks": 2, "editable": True},
        {"id": "mp_ioc_b", "desc": f"Interest on capital for {partner_b}: R{_fmt_money(interest_b)}", "marks": 1, "editable": True},
        {"id": "mp_bonus", "desc": f"Bonus to {partner_a}: R{_fmt_money(bonus_a)} (Partner B empty)", "marks": 1, "editable": True},
        {"id": "mp_primary", "desc": f"Primary distribution totals: R{_fmt_money(primary_a)} / R{_fmt_money(primary_b)}", "marks": 1, "editable": True},
        {"id": "mp_final_a", "desc": f"Final profit distribution {partner_a} ({ratio_a}/{total_parts}): R{_fmt_money(final_a)}", "marks": 1, "editable": True},
        {"id": "mp_final_b", "desc": f"Final profit distribution {partner_b} ({ratio_b}/{total_parts}): R{_fmt_money(final_b)}", "marks": 1, "editable": True},
        {"id": "mp_profit_is", "desc": f"Total profit per income statement: R{_fmt_money(profit_per_is_a)} / R{_fmt_money(profit_per_is_b)}", "marks": 1, "editable": True},
        {"id": "mp_drawings", "desc": f"Drawings entered in brackets: ({_fmt_money(drawings_a)}) and ({_fmt_money(drawings_b)})", "marks": 1, "editable": True},
        {"id": "mp_retained", "desc": f"Retained income for the year: R{_fmt_money(retained_a)} / R{_fmt_money(retained_b)}", "marks": 1, "editable": True},
        {"id": "mp_closing", "desc": f"Closing current account balances: R{_fmt_money(close_a)} / R{_fmt_money(close_b)}", "marks": 1, "editable": True},
    ]

    marking_schema = {
        "total_marks": 15,
        "marking_points": marking_points,
        "deductions": [
            {"rule": "must_be_empty_filled", "penalty": -1},
            {"rule": "added_instead_of_subtracted_drawings", "penalty": -1},
            {"rule": "omitted_interest_on_capital", "penalty": -1},
            {"rule": "inverted_profit_sharing_ratio", "penalty": -1},
            {"rule": "forgot_salary_increase_months", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    ideal_answer = (
        f"Completed Current Accounts Note (Note 5):\n"
        f"• {partner_a}: Primary R{_fmt_money(primary_a)}, Final Share R{_fmt_money(final_a)}, Profit R{_fmt_money(profit_per_is_a)}, "
        f"Drawings ({_fmt_money(drawings_a)}), Closing Balance R{_fmt_money(close_a)}\n"
        f"• {partner_b}: Primary R{_fmt_money(primary_b)}, Final Share R{_fmt_money(final_b)}, Profit R{_fmt_money(profit_per_is_b)}, "
        f"Drawings ({_fmt_money(drawings_b)}), Closing Balance R{_fmt_money(close_b)}"
    )

    return {
        "id": f"acc11_part_compound_{r.randint(100000, 999999)}",
        "title": "Partnership Current Accounts Note and Profit Appropriation",
        "topic": "Partnerships",
        "subskill": "partnerships_financial_statements_compound",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 20,
        "prompt": prompt,
        "question_type": "table_completion",
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": ideal_answer,
        "sample_answer": ideal_answer,
        "marks": 15,
        "deduction_rules": [
            {"rule": "must_be_empty_filled", "penalty": -1},
        ],
        "misconception_tags": [
            MISCONCEPTION_DRAWINGS_ADDED,
            MISCONCEPTION_OMITTED_INTEREST,
            MISCONCEPTION_INVERTED_RATIO,
            MISCONCEPTION_SALARY_INCREASE,
        ],
        "marking_schema": marking_schema,
        "hints": {
            "tier1_location": "Follow the sequence in Note 5: Salaries + Interest + Bonus = Primary Distribution.",
            "tier2_directional_rule": (
                f"Remaining Profit = Net Profit (R{_fmt_money(net_profit)}) – Total Primary (R{_fmt_money(total_primary)}). "
                f"Divide this by {total_parts} parts ({ratio_a}:{ratio_b}). "
                f"Drawings must be SUBTRACTED. Add opening credit balance or subtract opening debit balance."
            ),
            "tier3_worked_step": ideal_answer,
        },
    }


# ============================================================================
# PUBLIC DISPATCHER & REGISTRY INTERFACE
# ============================================================================
BUILDERS = {
    "compound": _build_compound_partnerships_statements,
    "partnerships_financial_statements": _build_compound_partnerships_statements,
    "current_accounts_note": _build_compound_partnerships_statements,
    "elementary_interest_on_capital": _build_elementary_interest_on_capital,
    "elementary_salaries_bonus": _build_elementary_salaries_bonus,
    "elementary_profit_share_ratio": _build_elementary_profit_share_ratio,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Accounting Partnerships Financial Statements questions."""
    base_seed = 42 if seed is None else int(seed)
    
    # Resolve builder mode
    if mode in BUILDERS and mode != "compound":
        target_mode = mode
    elif subskill in BUILDERS:
        target_mode = subskill
    else:
        target_mode = "compound"

    builder = BUILDERS.get(target_mode, _build_compound_partnerships_statements)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    *,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "hard",
    mode: str = "compound",
    subskill: str = "mixed",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Alternative signature returning question list directly for adapter compatibility."""
    res = generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, mode=mode, **kwargs)
    return res.get("questions", [])
