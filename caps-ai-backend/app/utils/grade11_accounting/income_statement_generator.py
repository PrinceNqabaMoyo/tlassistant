from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

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


def _money(x: float) -> str:
    return _fmt_money(float(x))


def _make_calc(*, prompt: str, correct_value: float, unit: str = "", explanation: str = "", working_formula: str = "", mode: str = "", archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_income_statement_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(_round_money(correct_value)),
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "guidelines": [f"Formula: {working_formula}"] if working_formula else [],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold" and str(explanation).strip():
        out["explanation"] = explanation
    return out


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_income_statement_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _fmt_bracket_expense(x: float) -> str:
    return f"({_money(abs(float(x)))})"


def _build_row_hints(rows: List[List[Optional[str]]]) -> Dict[str, str]:
    """Build cell_hints (i-button explanations) for every row in an income statement."""
    hints: Dict[str, str] = {}
    for rix, row in enumerate(rows):
        lbl = str(row[0]).strip().lstrip()
        key = f"t0_r{rix}_c2"
        ll = lbl.lower()
        if rix == 0 and "sales" in ll:
            hints[key] = "Sales = Trial balance figure adjusted for debtors allowances, returns and omitted credit sales."
        elif "cost of sales" in ll:
            hints[key] = "Cost of sales is an outgoing and must be shown in brackets. Adjust for returned goods at cost."
        elif ll == "gross profit":
            hints[key] = "Gross profit = Sales – Cost of sales."
        elif "other operating income" in ll:
            hints[key] = "Total of all other income items below this line."
        elif "rent income" in ll:
            hints[key] = "Adjust for rent received in advance or outstanding rent."
        elif "discount received" in ll:
            hints[key] = "Discount received from creditors/suppliers."
        elif "bad debts recovered" in ll:
            hints[key] = "Previously written-off debts now recovered — other income."
        elif "provision for bad debts" in ll:
            hints[key] = "Adjustment = Opening provision – Closing provision (or vice versa)."
        elif "fee income" in ll:
            hints[key] = "Fee/commission income earned."
        elif "gross operating income" in ll:
            hints[key] = "Gross operating income = Gross profit + Other operating income."
        elif "operating expenses" in ll and "operating profit" not in ll:
            hints[key] = "Total of all expense items below. Show in brackets (outgoing)."
        elif "salaries" in ll or "wages" in ll:
            hints[key] = "Include any omitted/additional salary amounts."
        elif "insurance" in ll:
            hints[key] = "Deduct prepaid portion (months not yet expired)."
        elif "water" in ll or "utilities" in ll or "electricity" in ll:
            hints[key] = "Add any outstanding/accrued amount."
        elif "telephone" in ll:
            hints[key] = "Add any accrued telephone charges."
        elif "stationery" in ll:
            hints[key] = "Deduct stationery on hand and any personal use."
        elif "bad debts" in ll and "recovered" not in ll:
            hints[key] = "Add any additional debtor written off during the year."
        elif "depreciation" in ll:
            hints[key] = "Depreciation for the year as given or calculated."
        elif "bank charges" in ll:
            hints[key] = "Include any additional bank charges from the bank statement."
        elif "consumable" in ll or "packing" in ll:
            hints[key] = "Consumable stores/packing material used during the year."
        elif "advertising" in ll:
            hints[key] = "Advertising expense — adjust for outstanding or prepaid amounts."
        elif "discount allowed" in ll:
            hints[key] = "Discount granted to debtors."
        elif "stock" in ll and ("deficit" in ll or "surplus" in ll or "theft" in ll or "loss" in ll):
            hints[key] = "Trading stock deficit/surplus or loss due to theft (uninsured portion)."
        elif "sundry" in ll:
            hints[key] = "Sundry expenses — may be a balancing figure."
        elif "motor" in ll or "vehicle" in ll:
            hints[key] = "Motor/vehicle expenses for the year."
        elif "maintenance" in ll or "repairs" in ll:
            hints[key] = "Maintenance and repairs expense."
        elif ll == "operating profit":
            hints[key] = "Operating profit = Gross operating income – Operating expenses."
        elif "interest income" in ll and "expense" not in ll:
            hints[key] = "Interest earned on fixed deposits or current account."
        elif "interest on fixed deposit" in ll:
            hints[key] = "Interest earned on fixed deposit investment."
        elif "interest on current" in ll:
            hints[key] = "Interest earned on current/cheque account per bank statement."
        elif "interest on overdue" in ll:
            hints[key] = "Interest charged on overdue debtor accounts."
        elif "profit before interest" in ll:
            hints[key] = "Profit before interest expense = Operating profit + Interest income."
        elif "interest expense" in ll:
            hints[key] = "Interest on loan/overdraft. Show in brackets (outgoing)."
        elif "net profit" in ll:
            hints[key] = "Net profit = Profit before interest expense – Interest expense."
    return hints


def _mk_statement_rows(
    *,
    sales: float,
    cost_of_sales: float,
    other_income_lines: List[Tuple[str, float]],
    expense_lines: List[Tuple[str, float]],
    interest_income_lines: List[Tuple[str, float]],
    interest_expense: float,
    workings: Optional[Dict[str, str]] = None,
    bracket_missing_labels: Optional[set] = None,
) -> Tuple[List[List[Optional[str]]], set]:
    """Build income-statement rows.

    Parameters
    ----------
    workings : dict mapping a row label (e.g. "Sales") to a calculation
        string (e.g. "945 300 – 28 620").  When provided the label becomes
        ``Sales (945 300 – 28 620)`` so the student sees the working.
    bracket_missing_labels : set of row labels (e.g. {"Cost of sales"})
        whose outgoing-bracket is deliberately omitted in the display.
        The correct_map will still contain the bracketed value; the student
        must add the brackets.  This implements the (*) rule for outgoings.

    Returns
    -------
    (rows, bracket_row_indices) where bracket_row_indices is the set of
    0-based row indices whose Amount cell is an outgoing shown in brackets.
    """
    workings = workings or {}
    bracket_missing_labels = bracket_missing_labels or set()

    gross_profit = _round_money(sales - cost_of_sales)
    other_income_total = _round_money(sum(v for _, v in other_income_lines))
    gross_operating_income = _round_money(gross_profit + other_income_total)

    operating_expenses_total = _round_money(sum(v for _, v in expense_lines))
    operating_profit = _round_money(gross_operating_income - operating_expenses_total)

    interest_income_total = _round_money(sum(v for _, v in interest_income_lines))
    profit_before_interest_expense = _round_money(operating_profit + interest_income_total)
    net_profit = _round_money(profit_before_interest_expense - interest_expense)

    bracket_row_indices: set = set()

    def _label(base: str) -> str:
        w = workings.get(base)
        return f"{base} ({w})" if w else base

    def _outgoing(base_label: str, val: float) -> str:
        """Return the amount string for an outgoing row.

        If base_label is in bracket_missing_labels the brackets are
        deliberately omitted (the student must add them).
        """
        if base_label in bracket_missing_labels:
            return _money(abs(val))
        return _fmt_bracket_expense(val)

    rows: List[List[Optional[str]]] = [
        [_label("Sales"), "", _money(sales)],
        [_label("Cost of sales"), "", _outgoing("Cost of sales", cost_of_sales)],
        [_label("Gross profit"), "", _money(gross_profit)],
        [_label("Other operating income"), "", _money(other_income_total)],
    ]
    bracket_row_indices.add(1)  # Cost of sales

    for label, val in other_income_lines:
        rows.append([f"  {_label(label)}", "", _money(val)])

    rows.append([_label("Gross operating income"), "", _money(gross_operating_income)])
    op_exp_idx = len(rows)
    rows.append([_label("Operating expenses"), "", _outgoing("Operating expenses", operating_expenses_total)])
    bracket_row_indices.add(op_exp_idx)

    for label, val in expense_lines:
        rows.append([f"  {_label(label)}", "", _money(val)])

    rows.append([_label("Operating profit"), "", _money(operating_profit)])

    if interest_income_lines:
        rows.append([_label("Interest income"), "", _money(interest_income_total)])
        for label, val in interest_income_lines:
            rows.append([f"  {_label(label)}", "", _money(val)])

    rows.append([_label("Profit before interest expense"), "", _money(profit_before_interest_expense)])
    int_exp_idx = len(rows)
    rows.append([_label("Interest expense"), "", _outgoing("Interest expense", interest_expense)])
    bracket_row_indices.add(int_exp_idx)
    rows.append([_label("Net profit for the year"), "", _money(net_profit)])
    return rows, bracket_row_indices


def _mk_income_statement_table(
    *,
    prompt: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    force_editable_cols: Optional[List[int]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    headers = ["Item", "Note", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    if force_editable_cols is not None:
        editable_cols = [int(c) for c in force_editable_cols]
    else:
        base_editable_cols = [2]
        editable_cols = _journal_editable_cols_by_difficulty(
            difficulty=diff,
            base_editable_cols=base_editable_cols,
            total_cols=len(headers),
            mode=mode_norm,
        )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        if show_answers:
            display = vals
        else:
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
        journal_type="income_statement",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct structure (headings and subtotals).",
            "Expenses should be shown in brackets where applicable.",
            "Enter amounts without a currency symbol.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_income_statement")
    return out


def _make_income_statement_archetype_multi_adjustment(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = r.choice(["28 February 2022", "30 June 2022", "28 February 2021", "28 February 2023"])

    sales_base = float(r.choice([916000, 954300, 1032000, 1797600, 1836000, 5701320]))
    debtors_allowances = float(r.choice([8000, 28620, 32000, 9860, 33030]))
    omitted_credit_sales = float(r.choice([0, 9600, 15300]))
    returned_goods_sp = float(r.choice([0, 225, 1575]))
    sales = _round_money(sales_base - debtors_allowances - returned_goods_sp + omitted_credit_sales)

    cost_of_sales_base = float(r.choice([510000, 467630, 427000, 1027200, 1080000, 3563350]))
    returned_goods_cp = float(r.choice([0, 150, 450, 900]))
    cost_of_sales = _round_money(cost_of_sales_base - returned_goods_cp)

    discount_received = float(r.choice([0, 480, 4200, 17550, 11280]))
    rent_income = float(r.choice([0, 12360, 47250, 99750, 82100, 184500]))
    bad_debts_recovered = float(r.choice([0, 190, 1000, 1342, 1890]))

    rent_adjust = float(r.choice([0, 2640, -8250, -6450, -13500]))
    rent_income_adj = _round_money(rent_income + rent_adjust)

    prov_open = float(r.choice([1000, 1500, 3500, 3935, 10150]))
    prov_close = float(r.choice([844, 1300, 2975, 2340, 8150, 918]))
    prov_adj = _round_money(abs(prov_open - prov_close))

    other_income_lines: List[Tuple[str, float]] = []
    if discount_received:
        other_income_lines.append(("Discount received", discount_received))
    if rent_income_adj:
        other_income_lines.append(("Rent income", rent_income_adj))
    if bad_debts_recovered:
        other_income_lines.append(("Bad debts recovered", bad_debts_recovered))
    if prov_adj:
        other_income_lines.append(("Provision for bad debts adjustment", prov_adj))

    salaries = float(r.choice([175000, 237940, 324000, 896250, 125000]))
    omitted_salary_gross = float(r.choice([0, 8000, 30000, 18000]))
    salaries_total = _round_money(salaries + omitted_salary_gross)

    insurance = float(r.choice([5400, 15460, 6400, 10560, 43150, 43740]))
    prepaid_months = int(r.choice([0, 0, 4, 2, 3]))
    insurance_monthly = _round_money(insurance / 12.0) if insurance else 0.0
    insurance_total = _round_money(insurance - (insurance_monthly * prepaid_months))

    water_elec = float(r.choice([7200, 25100, 48510, 17724]))
    water_accrued = float(r.choice([0, 560, 5000, 3180, 1098, 1440]))
    water_total = _round_money(water_elec + water_accrued)

    telephone = float(r.choice([21570, 30750, 12336, 26730]))
    tel_accrued = float(r.choice([0, 4670, 662]))
    telephone_total = _round_money(telephone + tel_accrued)

    stationery = float(r.choice([4700, 12520, 3490, 4100, 6500]))
    stationery_on_hand = float(r.choice([0, 700, 480, 1420]))
    stationery_personal = float(r.choice([0, 420]))
    stationery_total = _round_money(stationery - stationery_on_hand - stationery_personal)

    bad_debts = float(r.choice([6550, 1020, 5670, 19125, 8990]))
    write_off = float(r.choice([0, 300, 450, 4050, 3425, 810]))
    bad_debts_total = _round_money(bad_debts + write_off)

    depreciation = float(r.choice([0, 13458, 33030, 27970, 53830, 13987, 298350]))
    bank_charges = float(r.choice([840, 1272, 3560, 9476, 1440, 3700]))

    expense_lines: List[Tuple[str, float]] = [
        ("Salaries and wages", salaries_total),
        ("Insurance", insurance_total),
        ("Water and electricity", water_total),
        ("Telephone", telephone_total),
        ("Stationery", stationery_total),
        ("Bad debts", bad_debts_total),
        ("Bank charges", bank_charges),
    ]
    if depreciation:
        expense_lines.append(("Depreciation", depreciation))

    fixed_deposit_interest = float(r.choice([0, 500, 2750, 10000, 24300, 53250]))
    interest_income_lines: List[Tuple[str, float]] = []
    if fixed_deposit_interest:
        interest_income_lines.append(("Interest on fixed deposit", fixed_deposit_interest))

    interest_expense = float(r.choice([3250, 7485, 11640, 20000, 31500, 145000]))

    # --- Build calculation workings for adjusted rows ---
    workings: Dict[str, str] = {}
    # Sales working: base - debtors allowances +/- other adjustments
    sales_parts: List[str] = [f"{sales_base:,.0f}"]
    if debtors_allowances:
        sales_parts.append(f"– {debtors_allowances:,.0f}")
    if returned_goods_sp:
        sales_parts.append(f"– {returned_goods_sp:,.0f}")
    if omitted_credit_sales:
        sales_parts.append(f"+ {omitted_credit_sales:,.0f}")
    if len(sales_parts) > 1:
        workings["Sales"] = " ".join(sales_parts)

    # Cost of sales working
    if returned_goods_cp:
        workings["Cost of sales"] = f"{cost_of_sales_base:,.0f} – {returned_goods_cp:,.0f}"

    # Rent income working
    if rent_adjust and rent_income:
        if rent_adjust > 0:
            workings["Rent income"] = f"{rent_income:,.0f} + {rent_adjust:,.0f}"
        else:
            workings["Rent income"] = f"{rent_income:,.0f} – {abs(rent_adjust):,.0f}"

    # Provision for bad debts adjustment working
    if prov_adj:
        workings["Provision for bad debts adjustment"] = f"{prov_open:,.0f} – {prov_close:,.0f}"

    # Salaries working
    if omitted_salary_gross:
        workings["Salaries and wages"] = f"{salaries:,.0f} + {omitted_salary_gross:,.0f}"

    # Insurance working (prepaid deducted)
    if prepaid_months:
        prepaid_amt = _round_money(insurance_monthly * prepaid_months)
        workings["Insurance"] = f"{insurance:,.0f} – {prepaid_amt:,.0f}"

    # Water & electricity working
    if water_accrued:
        workings["Water and electricity"] = f"{water_elec:,.0f} + {water_accrued:,.0f}"

    # Telephone working
    if tel_accrued:
        workings["Telephone"] = f"{telephone:,.0f} + {tel_accrued:,.0f}"

    # Stationery working
    stat_parts: List[str] = [f"{stationery:,.0f}"]
    if stationery_on_hand:
        stat_parts.append(f"– {stationery_on_hand:,.0f}")
    if stationery_personal:
        stat_parts.append(f"– {stationery_personal:,.0f}")
    if len(stat_parts) > 1:
        workings["Stationery"] = " ".join(stat_parts)

    # Bad debts working
    if write_off:
        workings["Bad debts"] = f"{bad_debts:,.0f} + {write_off:,.0f}"

    # --- (*) rule: randomly omit outgoing brackets on Cost of sales ---
    bracket_missing: set = set()
    if r.random() < 0.35:
        bracket_missing.add("Cost of sales")

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
        bracket_missing_labels=bracket_missing,
    )

    prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income (Income Statement) for the financial year ended {fy_end}.

#### INFORMATION:
An extract of the pre-adjustment Trial Balance and a list of adjustments are provided. Use the correct structure, headings and subtotals. Show calculations in brackets next to the row label where applicable. Expenses/outgoings must be shown in brackets."""

    hints = _build_row_hints(rows)

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=hints,
    )
    q["meta"] = {"archetype_key": "g11_income_statement_full_statement_multi_adjustments"}
    return q


def _make_income_statement_archetype_markup_backcalc(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = r.choice(["28 February 2022", "28 February 2021", "30 June 2022"])
    markup_pct = float(r.choice([0.6, 0.5, 0.75]))

    sales = float(r.choice([1_770_400, 1_032_000, 1_836_000]))
    omitted_sales = float(r.choice([0, 9_600, 15_300]))
    sales = _round_money(sales + omitted_sales)

    cost_of_sales = _round_money(sales * (1.0 / (1.0 + markup_pct)))

    other_income_lines = [("Discount received", float(r.choice([4_600, 4_200, 17_550])))]
    expense_lines = [("Salaries and wages", float(r.choice([192_200, 237_940, 175_170])))]
    interest_income_lines = [("Interest on fixed deposit", float(r.choice([18_000, 24_300, 10_000])))]
    interest_expense = float(r.choice([17_500, 31_500, 11_640]))

    workings: Dict[str, str] = {}
    workings["Cost of sales"] = f"{_money(sales)} ÷ {1.0 + markup_pct:.2f}"

    bracket_missing: set = set()
    if r.random() < 0.35:
        bracket_missing.add("Cost of sales")

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
        bracket_missing_labels=bracket_missing,
    )

    prompt = f"""{business}

#### REQUIRED:
Complete the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
The business achieved a fixed mark-up of {int(markup_pct*100)}% on cost for the year. Use this to calculate Cost of sales as a function of Sales. Show calculations in brackets next to the row label where applicable."""

    hints = _build_row_hints(rows)
    hints["t0_r1_c2"] = f"Mark-up is {int(markup_pct*100)}% on cost: Cost = Sales ÷ (1 + {markup_pct:.2f})."

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=hints,
    )
    q["meta"] = {"archetype_key": "g11_income_statement_fixed_markup_cost_of_sales_backcalc"}
    return q


def _make_income_statement_archetype_interest_expense_balancing(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = "28 February 2023"

    sales = float(r.choice([5_706_570, 1_786_165, 1_818_270]))
    cost_of_sales = float(r.choice([3_566_850, 1_026_300, 1_089_000]))

    other_income_lines = [("Rent income", float(r.choice([75_650, 171_000, 91_500])))]
    expense_lines = [("Salaries and wages", float(r.choice([935_100, 336_000, 237_940])))]
    interest_income_lines = [("Interest on fixed deposit", float(r.choice([53_250, 24_300, 10_000])))]

    # Compute Profit before interest expense with zero interest expense.
    tmp_rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=0.0,
    )

    pb_row = next((row for row in tmp_rows if str(row[0]).strip().lower() == "profit before interest expense"), None)
    pb_val = 0.0
    if pb_row and pb_row[2]:
        s = str(pb_row[2])
        s = s.replace(",", "").replace(" ", "")
        s = "".join(ch for ch in s if (ch.isdigit() or ch in {".", "-"}))
        pb_val = float(s or "0")

    target_net_profit = float(r.choice([478_900, 334_340, 372_616]))
    interest_expense = _round_money(abs(pb_val - target_net_profit))

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
    )

    prompt = f"""{business}

#### REQUIRED:
Complete the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Some amounts may be provided in the answer book. Determine Interest expense as a balancing figure using Profit before interest expense and Net profit."""

    hints = _build_row_hints(rows)
    hints["t0_r" + str(len(rows)-2) + "_c2"] = "Interest expense is the balancing figure: Profit before interest expense – Net profit."

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=hints,
    )
    q["meta"] = {"archetype_key": "g11_income_statement_interest_expense_balancing"}
    return q


def _make_income_statement_archetype_loan_statement_interest_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q7 (xi): interest is capitalised; interest expense derived from loan statement.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = "28 February 2023"

    open_loan = float(r.choice([252_000, 300_000, 180_000]))
    closing_loan = float(r.choice([198_000, 240_000, 150_000]))
    repayments_incl_interest = float(r.choice([85_500, 60_000, 72_000]))

    interest_expense = _round_money(closing_loan + repayments_incl_interest - open_loan)
    if interest_expense < 0:
        # Keep it sensible; this archetype expects a positive derived interest.
        interest_expense = abs(interest_expense)

    calc_prompt = f"""{business}

#### REQUIRED:
Calculate the interest expense on the loan for the year ended {fy_end}.

#### INFORMATION:
Loan statement (interest is capitalised):

Balance on 1 March 2022: {_money(open_loan)}
Repayments during the year including interest: {_money(repayments_incl_interest)}
Balance on 28 February 2023: {_money(closing_loan)}"""

    calc_part = _make_calc(
        prompt=calc_prompt,
        correct_value=interest_expense,
        unit="R",
        explanation="If interest is capitalised: Closing balance = Opening balance + Interest - Repayments (incl interest). Rearranged: Interest = Closing + Repayments - Opening.",
        working_formula="Interest = Closing balance + Repayments - Opening balance",
        mode=mode,
        archetype_key="g11_income_statement_loan_statement_interest_calc",
    )

    # Build a short but valid statement that uses the derived interest.
    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))
    other_income_lines = [("Rent income", float(r.choice([171_000, 75_650, 91_500])))]
    expense_lines = [("Salaries and wages", float(r.choice([237_940, 935_100, 324_000])))]
    interest_income_lines = [("Interest on fixed deposit", float(r.choice([24_300, 53_250, 10_000])))]

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
    )

    journal_prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income (Income Statement) for the financial year ended {fy_end}.

#### INFORMATION:
Use the interest expense you calculated from the loan statement."""

    journal_part = _mk_income_statement_table(
        prompt=journal_prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    journal_part["meta"] = {"archetype_key": "g11_income_statement_full_statement_uses_loan_interest"}

    bundle_prompt = f"""{business}

You will answer the following parts for the year ended {fy_end}."""

    return _make_bundle(
        prompt=bundle_prompt,
        parts=[calc_part, journal_part],
        archetype_key="g11_income_statement_bundle_loan_statement_interest_then_statement",
    )


def _make_income_statement_archetype_stock_theft_insurance(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q6 pattern: stolen stock with partial insurance payout; loss is uninsured portion.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = "28 February 2023"

    sales = float(r.choice([5_706_570, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([3_566_850, 1_011_657.14, 604_705.88]))

    stolen_stock_value = float(r.choice([17_400, 12_000, 24_000]))
    insurance_cover_pct = float(r.choice([0.8, 0.75, 0.9]))
    uninsured_loss = _round_money(stolen_stock_value * (1.0 - insurance_cover_pct))

    other_income_lines: List[Tuple[str, float]] = [
        ("Rent income", float(r.choice([75_650, 171_000, 91_500]))),
        ("Bad debts recovered", float(r.choice([2_700, 1_000, 1_890]))),
    ]
    expense_lines: List[Tuple[str, float]] = [
        ("Salaries and wages", float(r.choice([935_100, 237_940, 324_000]))),
        ("Stock loss due to theft", uninsured_loss),
        ("Consumable stores", float(r.choice([35_350, 13_560, 12_520]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [
        ("Interest on fixed deposit", float(r.choice([53_250, 24_300, 10_000]))),
        ("Interest on overdue debtor accounts", float(r.choice([4_250, 180, 0]))),
    ]
    # Remove zeros so the rows don't look odd.
    interest_income_lines = [(a, b) for (a, b) in interest_income_lines if b]

    interest_expense = float(r.choice([145_000, 31_500, 11_640]))

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
    )

    prompt = f"""{business}

#### REQUIRED:
Complete the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Stock to the value of R{_money(stolen_stock_value)} was stolen. The insurance company agreed to pay {int(insurance_cover_pct*100)}% of the stock value. Show the loss due to theft as the uninsured portion."""

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    q["meta"] = {"archetype_key": "g11_income_statement_stock_theft_insurance_loss"}
    return q


def _make_income_statement_archetype_missing_labels(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors the doc instruction that some labels may be missing; harder difficulties may require learners to fill labels.
    scenario = build_scenario(seed=r.randint(1, 1000))
    business = scenario["business"]
    fy_end = r.choice(["28 February 2023", "28 February 2022"])

    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))

    other_income_lines: List[Tuple[str, float]] = [("Rent income", float(r.choice([171_000, 75_650, 91_500])))]
    expense_lines: List[Tuple[str, float]] = [
        ("Salaries and wages", float(r.choice([237_940, 935_100, 324_000]))),
        ("Depreciation", float(r.choice([53_830, 29_835, 13_458]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [("Interest on fixed deposit", float(r.choice([24_300, 53_250, 10_000])))]
    interest_expense = float(r.choice([31_500, 17_500, 11_640]))

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
    )

    # Blank out some labels; correct_map will still contain blanks, and difficulty may allow editing of col 0.
    for idx in [2, 3, 6, 8]:
        if 0 <= idx < len(rows):
            rows[idx][0] = ""

    prompt = f"""{business}

#### REQUIRED:
Complete the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Some labels may be missing in the table. Insert the missing labels and complete the amounts."""

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        force_editable_cols=[0, 2],
        cell_hints=_build_row_hints(rows),
    )
    q["meta"] = {"archetype_key": "g11_income_statement_missing_labels"}
    return q


def _make_income_statement_archetype_sundry_balancing(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q6 note: "Sundry expenses is the balancing figure".
    business = r.choice(["GOVEA TRADERS", "SS Traders", "MK Traders"])
    fy_end = "28 February 2023"

    sales = float(r.choice([5_706_570, 1_818_270, 1_770_400]))
    cost_of_sales = float(r.choice([3_566_850, 1_089_000, 1_011_657.14]))

    other_income_lines: List[Tuple[str, float]] = [
        ("Bad debts recovered", float(r.choice([2_700, 1_890, 1_000]))),
        ("Rent income", float(r.choice([75_650, 171_000, 91_500]))),
    ]
    expense_lines_without_sundry: List[Tuple[str, float]] = [
        ("Salaries and wages", float(r.choice([935_100, 237_940, 324_000]))),
        ("Insurance", float(r.choice([39_850, 41_580, 15_460]))),
        ("Bad debts", float(r.choice([9_800, 23_175, 6_550]))),
        ("Consumable stores", float(r.choice([35_350, 13_560, 12_520]))),
        ("Depreciation", float(r.choice([298_350, 53_830, 27_970]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [
        ("Interest on fixed deposit", float(r.choice([53_250, 24_300, 10_000]))),
        ("Interest on overdue debtor accounts", float(r.choice([4_250, 180, 0]))),
    ]
    interest_income_lines = [(a, b) for (a, b) in interest_income_lines if b]

    interest_expense = float(r.choice([145_000, 31_500, 11_640]))

    # Choose a target operating profit and derive sundry as balancing figure.
    target_operating_profit = float(r.choice([566_400, 371_536, 420_000]))

    gross_profit = _round_money(sales - cost_of_sales)
    other_income_total = _round_money(sum(v for _, v in other_income_lines))
    gross_operating_income = _round_money(gross_profit + other_income_total)
    other_exp_total = _round_money(sum(v for _, v in expense_lines_without_sundry))

    operating_expenses_total = _round_money(gross_operating_income - target_operating_profit)
    sundry = _round_money(max(0.0, operating_expenses_total - other_exp_total))

    expense_lines: List[Tuple[str, float]] = list(expense_lines_without_sundry) + [("Sundry expenses", sundry)]

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
    )

    prompt = f"""{business}

#### REQUIRED:
Complete the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Sundry expenses is the balancing figure."""

    hints = _build_row_hints(rows)
    # Find the sundry row and add a specific hint
    for rix, row in enumerate(rows):
        if "sundry" in str(row[0]).lower():
            hints[f"t0_r{rix}_c2"] = "Sundry expenses is the balancing figure: Operating expenses total – all other named expenses."

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=hints,
    )
    q["meta"] = {"archetype_key": "g11_income_statement_sundry_expenses_balancing"}
    return q


def _make_income_statement_archetype_prepaid_accrued_focus(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Focused on typical accrual/prepayment adjustments from the doc (insurance prepaid, rent received in advance, W&E outstanding).
    business = r.choice(["SS Traders", "Westville Traders", "Plumstead Hardware"])
    fy_end = "28 February 2023"

    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))

    rent_income_tb = float(r.choice([184_500, 99_750, 47_250]))
    rent_in_advance = float(r.choice([13_500, 8_250, 6_450]))
    rent_income = _round_money(rent_income_tb - rent_in_advance)

    insurance_tb = float(r.choice([43_740, 43_150, 15_460]))
    insurance_prepaid = float(r.choice([2_160, 3_300, 1_800]))
    insurance = _round_money(insurance_tb - insurance_prepaid)

    water_elec_tb = float(r.choice([48_510, 17_724, 25_100]))
    water_elec_owing = float(r.choice([1_440, 1_098, 3_180]))
    water_elec = _round_money(water_elec_tb + water_elec_owing)

    other_income_lines: List[Tuple[str, float]] = [
        ("Rent income", rent_income),
        ("Provision for bad debts adjustment", float(r.choice([1_595, 2_700, 156]))),
    ]
    expense_lines: List[Tuple[str, float]] = [
        ("Salaries and wages", float(r.choice([237_940, 935_100, 324_000]))),
        ("Insurance", insurance),
        ("Water and electricity", water_elec),
        ("Depreciation", float(r.choice([53_830, 27_970, 13_458]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [("Interest on fixed deposit", float(r.choice([24_300, 53_250, 10_000])))]
    interest_expense = float(r.choice([31_500, 11_640, 17_500]))

    workings: Dict[str, str] = {}
    workings["Rent income"] = f"{rent_income_tb:,.0f} – {rent_in_advance:,.0f}"
    workings["Insurance"] = f"{insurance_tb:,.0f} – {insurance_prepaid:,.0f}"
    workings["Water and electricity"] = f"{water_elec_tb:,.0f} + {water_elec_owing:,.0f}"

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
    )

    prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Adjust for: insurance prepaid, rent income received in advance, and water & electricity outstanding. Show calculations in brackets next to the row label where applicable."""

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    q["meta"] = {"archetype_key": "g11_income_statement_prepaid_accrued_adjustments"}
    return q


def _make_income_statement_archetype_debtors_provision_focus(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q1/Q2/Q7: bad debts recovered, write-off, and provision adjustment as core focus.
    business = r.choice(["SS Traders", "Westville Traders", "MK Traders"])
    fy_end = "28 February 2023"

    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))

    bad_debts_recovered = float(r.choice([810, 1_342, 1_890]))
    bad_debts_written_off = float(r.choice([4_050, 3_425, 2_700]))
    bad_debts_tb = float(r.choice([19_125, 8_990, 5_670]))

    prov_open = float(r.choice([3_935, 10_150, 2_975]))
    prov_close = float(r.choice([2_340, 8_150, 918]))
    prov_adj = _round_money(abs(prov_open - prov_close))

    other_income_lines: List[Tuple[str, float]] = [
        ("Bad debts recovered", bad_debts_recovered),
        ("Provision for bad debts adjustment", prov_adj),
    ]

    expense_lines: List[Tuple[str, float]] = [
        ("Bad debts", _round_money(bad_debts_tb + bad_debts_written_off)),
        ("Discount allowed", float(r.choice([3_612, 2_490, 1_000]))),
        ("Salaries and wages", float(r.choice([237_940, 324_000, 935_100]))),
    ]

    interest_income_lines: List[Tuple[str, float]] = [("Interest on fixed deposit", float(r.choice([24_300, 53_250, 10_000])))]
    interest_expense = float(r.choice([31_500, 11_640, 17_500]))

    workings: Dict[str, str] = {}
    workings["Bad debts"] = f"{bad_debts_tb:,.0f} + {bad_debts_written_off:,.0f}"
    workings["Provision for bad debts adjustment"] = f"{prov_open:,.0f} – {prov_close:,.0f}"

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
    )

    prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Adjust for bad debts recovered, a debtor written off as irrecoverable, and the provision for bad debts adjustment. Show calculations in brackets next to the row label where applicable."""

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    q["meta"] = {"archetype_key": "g11_income_statement_debtors_provision_focus"}
    return q


def _make_income_statement_archetype_fixed_deposit_bank_statement_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q7 (viii) + (ix): bank statement includes extra charges and interest; fixed deposit interest received for part of year.
    business = r.choice(["SS Traders", "Hollywood Bank Client", "MK Traders"])
    fy_end = "28 February 2023"

    # Fixed deposit interest: received for 9 months, deposit unchanged, interest not capitalized.
    monthly_interest = float(r.choice([900, 750, 1200]))
    months_received = int(r.choice([9, 10, 8]))
    fixed_deposit_interest = _round_money(monthly_interest * months_received)

    bank_charges_tb = float(r.choice([9_476, 3_560, 1_272]))
    bank_charges_extra = float(r.choice([596, 840, 230]))
    bank_charges = _round_money(bank_charges_tb + bank_charges_extra)

    interest_on_current = float(r.choice([180, 240, 300]))

    calc_prompt = f"""{business}

#### REQUIRED:
Determine the missing interest income amounts from the fixed deposit and bank statement.

#### INFORMATION:
Fixed deposit interest received for {months_received} months at R{_money(monthly_interest)} per month.
Bank statement shows interest on current account of R{_money(interest_on_current)}."""

    calc_part = _make_calc(
        prompt=calc_prompt,
        correct_value=_round_money(fixed_deposit_interest + interest_on_current),
        unit="R",
        explanation="Total interest income = fixed deposit interest received + interest on current account (bank statement).",
        mode=mode,
        archetype_key="g11_income_statement_interest_income_from_bank_and_fixed_deposit_calc",
    )

    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))
    other_income_lines: List[Tuple[str, float]] = [("Rent income", float(r.choice([171_000, 75_650, 91_500])))]
    expense_lines: List[Tuple[str, float]] = [
        ("Bank charges", bank_charges),
        ("Salaries and wages", float(r.choice([237_940, 324_000, 935_100]))),
        ("Insurance", float(r.choice([41_580, 39_850, 15_460]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [
        ("Interest on fixed deposit", fixed_deposit_interest),
        ("Interest on current account", interest_on_current),
    ]
    interest_expense = float(r.choice([31_500, 11_640, 17_500]))

    workings: Dict[str, str] = {}
    workings["Bank charges"] = f"{bank_charges_tb:,.0f} + {bank_charges_extra:,.0f}"

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
    )

    journal_prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Use the bank statement and fixed deposit details to adjust bank charges and interest income. Show calculations in brackets next to the row label where applicable."""

    journal_part = _mk_income_statement_table(
        prompt=journal_prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    journal_part["meta"] = {"archetype_key": "g11_income_statement_bank_statement_and_fixed_deposit_interest"}

    return _make_bundle(
        prompt=f"""{business}

Answer the following parts for the year ended {fy_end}.""",
        parts=[calc_part, journal_part],
        archetype_key="g11_income_statement_bundle_bank_statement_and_fixed_deposit",
    )


def _make_income_statement_archetype_advertising_contract(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q7 (xii): monthly advertising contract, paid for 11 months, rate increased part-way through year.
    business = r.choice(["SS Traders", "Local Newspaper Contract", "MK Traders"])
    fy_end = "28 February 2023"

    old_rate = float(r.choice([2500, 2000, 1800]))
    increase = float(r.choice([500, 400]))
    new_rate = _round_money(old_rate + increase)
    increase_month = r.choice(["1 November 2022", "1 October 2022"])
    months_old = int(r.choice([8, 7, 6]))
    months_new = 12 - months_old
    months_paid = 11

    advertising_paid = _round_money((months_old * old_rate) + ((months_paid - months_old) * new_rate))
    advertising_expense = _round_money((months_old * old_rate) + (months_new * new_rate))
    outstanding = _round_money(max(0.0, advertising_expense - advertising_paid))

    prompt = f"""{business}

#### REQUIRED:
Prepare the Statement of Comprehensive Income for the year ended {fy_end}.

#### INFORMATION:
Advertising is a monthly contract for the entire year. Advertising was paid for {months_paid} months only.
From {increase_month}, the contract rate increased by R{_money(increase)} per month."""

    # Include advertising line with the correct adjusted expense.
    sales = float(r.choice([1_818_270, 1_770_400, 1_032_000]))
    cost_of_sales = float(r.choice([1_089_000, 1_011_657.14, 604_705.88]))
    other_income_lines: List[Tuple[str, float]] = [("Rent income", float(r.choice([171_000, 75_650, 91_500])))]
    expense_lines: List[Tuple[str, float]] = [
        ("Advertising", advertising_expense),
        ("Salaries and wages", float(r.choice([237_940, 324_000, 935_100]))),
        ("Insurance", float(r.choice([41_580, 39_850, 15_460]))),
    ]
    interest_income_lines: List[Tuple[str, float]] = [("Interest on fixed deposit", float(r.choice([24_300, 53_250, 10_000])))]
    interest_expense = float(r.choice([31_500, 11_640, 17_500]))

    workings: Dict[str, str] = {}
    workings["Advertising"] = f"{months_old} × {old_rate:,.0f} + {months_new} × {new_rate:,.0f}"

    rows, _br_idx = _mk_statement_rows(
        sales=sales,
        cost_of_sales=cost_of_sales,
        other_income_lines=other_income_lines,
        expense_lines=expense_lines,
        interest_income_lines=interest_income_lines,
        interest_expense=interest_expense,
        workings=workings,
    )

    q = _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=_build_row_hints(rows),
    )
    q["meta"] = {
        "archetype_key": "g11_income_statement_advertising_contract_rate_change_and_outstanding",
        "advertising_outstanding": _money(outstanding),
    }
    return q


def _make_income_statement_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Archetype-inspired structure (3 columns): Item | Note | Amount
    business = r.choice(["Best Buy Shoes", "MK Traders", "Westville Traders", "Plumstead Hardware"])
    fy_end = r.choice(["28 February 2022", "30 June 2022", "28 February 2021", "28 February 2023"])

    sales = float(r.choice([916000, 945300, 1032000, 952000]))
    debtors_allowances = float(r.choice([8000, 28620, 32000, 9230]))
    net_sales = _round_money(sales - debtors_allowances)

    cost_of_sales = float(r.choice([510000, 680000, 427000, 605016]))
    cos_adj = float(r.choice([0, 450, 800, 1200]))
    net_cos = _round_money(cost_of_sales - cos_adj)

    gross_profit = _round_money(net_sales - net_cos)

    # Other operating income
    discount_received = float(r.choice([0, 480, 2893, 4200]))
    fee_income = float(r.choice([0, 15750, 5325]))
    rent_income = float(r.choice([0, 15000, 17040, 47250]))
    bad_debts_recovered = float(r.choice([0, 190, 250]))
    prov_adj_income = float(r.choice([0, 156, 300]))

    other_income = _round_money(discount_received + fee_income + rent_income + bad_debts_recovered + prov_adj_income)
    gross_operating_income = _round_money(gross_profit + other_income)

    # Operating expenses
    salaries = float(r.choice([125000, 164500, 175000]))
    salaries_adj = float(r.choice([0, 8000, 18000]))
    salaries_total = _round_money(salaries + salaries_adj)

    stationery = float(r.choice([4100, 6500, 4700]))
    stationery_adj = float(r.choice([0, -420, -700]))
    stationery_total = _round_money(stationery + stationery_adj)

    bad_debts = float(r.choice([1500, 1600, 6550]))
    bad_debts_adj = float(r.choice([0, 300, 800]))
    bad_debts_total = _round_money(bad_debts + bad_debts_adj)

    insurance = float(r.choice([5400, 6400, 7080]))
    insurance_adj = float(r.choice([0, -1800, -1200]))
    insurance_total = _round_money(insurance + insurance_adj)

    water_elec = float(r.choice([7200, 25000, 3860]))
    water_elec_adj = float(r.choice([0, 560, 340]))
    water_elec_total = _round_money(water_elec + water_elec_adj)

    bank_charges = float(r.choice([1272, 3700, 230]))
    consumable_stores = float(r.choice([0, 13000, 13560]))

    depreciation = float(r.choice([0, 13458, 22000]))

    operating_expenses = _round_money(
        consumable_stores
        + bank_charges
        + salaries_total
        + stationery_total
        + bad_debts_total
        + insurance_total
        + water_elec_total
        + depreciation
    )

    operating_profit = _round_money(gross_operating_income - operating_expenses)

    # Interest income/expense
    interest_income = float(r.choice([0, 3850, 375]))
    profit_before_interest = _round_money(operating_profit + interest_income)

    interest_expense = float(r.choice([0, 20000, 8000]))
    net_profit = _round_money(profit_before_interest - interest_expense)

    def _br(x: float) -> str:
        return f"({_money(abs(x))})" if x < 0 else _money(x)

    rows: List[List[Optional[str]]] = [
        [f"Sales", "", _money(net_sales)],
        ["Cost of sales", "", f"({_money(net_cos)})"],
        ["Gross profit", "", _money(gross_profit)],
        ["Other operating income", "", _money(other_income)],
    ]

    # Add detail lines for income if non-zero (archetype shows indented items)
    if discount_received:
        rows.append(["  Discount received", "", _money(discount_received)])
    if fee_income:
        rows.append(["  Fee income", "", _money(fee_income)])
    if rent_income:
        rows.append(["  Rent income", "", _money(rent_income)])
    if bad_debts_recovered:
        rows.append(["  Bad debts recovered", "", _money(bad_debts_recovered)])
    if prov_adj_income:
        rows.append(["  Provision for bad debts adjustment", "", _money(prov_adj_income)])

    rows.append(["Gross operating income", "", _money(gross_operating_income)])
    rows.append(["Operating expenses", "", f"({_money(operating_expenses)})"])

    # Expenses detail lines
    if consumable_stores:
        rows.append(["  Consumable stores", "", _money(consumable_stores)])
    rows.append(["  Salaries and wages", "", _money(salaries_total)])
    rows.append(["  Stationery", "", _money(stationery_total)])
    rows.append(["  Bad debts", "", _money(bad_debts_total)])
    rows.append(["  Insurance", "", _money(insurance_total)])
    rows.append(["  Water and electricity", "", _money(water_elec_total)])
    rows.append(["  Bank charges", "", _money(bank_charges)])
    if depreciation:
        rows.append(["  Depreciation", "", _money(depreciation)])

    rows.append(["Operating profit", "", _money(operating_profit)])

    if interest_income:
        rows.append(["Interest income", "", _money(interest_income)])

    rows.append(["Profit before interest expense", "", _money(profit_before_interest)])

    if interest_expense:
        rows.append(["Interest expense", "", f"({_money(interest_expense)})"])

    rows.append(["Net profit for the year", "", _money(net_profit)])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c2"] = "Net sales = Sales - Debtors allowances (if given)."
        cell_hints["t0_r1_c2"] = "Cost of sales is an expense and is shown in brackets."
        cell_hints["t0_r2_c2"] = "Gross profit = Net sales - Cost of sales."
        cell_hints["t0_r-1_c0"] = ""  # placeholder

    prompt = "Partnerships — Statement of Comprehensive Income (Income Statement)\n\nPrepare the Income Statement in the given format."

    # ── Build rubric_map dynamically (tracking row indices) ──
    rubric_map: Dict[str, Dict[str, Any]] = {}
    dependency_map: Dict[str, List[str]] = {}

    # Fixed rows: 0=Sales, 1=COS, 2=Gross Profit, 3=Other income
    rubric_map["t0_r0_c2"] = {
        "formula_structure": "Net Sales = Sales − Debtors allowances",
        "foundational_values": [sales, debtors_allowances],
        "operations": ["−"],
        "max_score": 1.5,
    }
    rubric_map["t0_r1_c2"] = {
        "formula_structure": "Cost of Sales (shown in brackets)",
        "foundational_values": [cost_of_sales, cos_adj],
        "operations": ["−"] if cos_adj else [],
        "max_score": 1.5 if cos_adj else 1.0,
    }
    rubric_map["t0_r2_c2"] = {
        "formula_structure": "Gross Profit = Net Sales − Cost of Sales",
        "foundational_values": [net_sales, net_cos],
        "operations": ["−"],
        "max_score": 1.5,
    }
    dependency_map["t0_r2_c2"] = ["t0_r0_c2", "t0_r1_c2"]

    # Track current row after the variable income detail lines
    cur_row = 4  # starts after row 3 (Other operating income)
    detail_income_cells = []
    if discount_received:
        detail_income_cells.append(f"t0_r{cur_row}_c2")
        cur_row += 1
    if fee_income:
        detail_income_cells.append(f"t0_r{cur_row}_c2")
        cur_row += 1
    if rent_income:
        detail_income_cells.append(f"t0_r{cur_row}_c2")
        cur_row += 1
    if bad_debts_recovered:
        detail_income_cells.append(f"t0_r{cur_row}_c2")
        cur_row += 1
    if prov_adj_income:
        detail_income_cells.append(f"t0_r{cur_row}_c2")
        cur_row += 1

    # Gross operating income row
    goi_row = cur_row
    rubric_map[f"t0_r{goi_row}_c2"] = {
        "formula_structure": "Gross Operating Income = Gross Profit + Other Income",
        "foundational_values": [gross_profit, other_income],
        "operations": ["+"],
        "max_score": 1.5,
    }
    dependency_map[f"t0_r{goi_row}_c2"] = ["t0_r2_c2", "t0_r3_c2"]
    cur_row += 1

    # Operating expenses row
    opex_row = cur_row
    cur_row += 1

    # Skip operating expense detail lines
    if consumable_stores:
        cur_row += 1
    cur_row += 1  # salaries
    cur_row += 1  # stationery
    cur_row += 1  # bad debts
    cur_row += 1  # insurance
    cur_row += 1  # water & elec
    cur_row += 1  # bank charges
    if depreciation:
        cur_row += 1

    # Operating profit
    op_profit_row = cur_row
    rubric_map[f"t0_r{op_profit_row}_c2"] = {
        "formula_structure": "Operating Profit = Gross Operating Income − Operating Expenses",
        "foundational_values": [gross_operating_income, operating_expenses],
        "operations": ["−"],
        "max_score": 1.5,
    }
    dependency_map[f"t0_r{op_profit_row}_c2"] = [f"t0_r{goi_row}_c2", f"t0_r{opex_row}_c2"]
    cur_row += 1

    if interest_income:
        cur_row += 1

    # Profit before interest expense
    pbi_row = cur_row
    cur_row += 1

    if interest_expense:
        cur_row += 1

    # Net profit
    np_row = cur_row
    rubric_map[f"t0_r{np_row}_c2"] = {
        "formula_structure": "Net Profit = Operating Profit + Interest Income − Interest Expense",
        "foundational_values": [operating_profit, interest_income, interest_expense],
        "operations": ["+", "−"],
        "max_score": 2.0,
    }
    dependency_map[f"t0_r{np_row}_c2"] = [f"t0_r{op_profit_row}_c2"]

    return _mk_income_statement_table(
        prompt=prompt,
        title_fields=[
            {"label": "STATEMENT OF COMPREHENSIVE INCOME / INCOME STATEMENT", "value": ""},
            {"label": "Name of business", "value": business},
            {"label": "For the year ended", "value": fy_end},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
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

    builders: List[Any] = [
        lambda: _make_income_statement_archetype_multi_adjustment(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_markup_backcalc(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_interest_expense_balancing(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_loan_statement_interest_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_stock_theft_insurance(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_missing_labels(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_sundry_balancing(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_prepaid_accrued_focus(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_debtors_provision_focus(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_fixed_deposit_bank_statement_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_statement_archetype_advertising_contract(r=r, difficulty=difficulty, mode=mode),
    ]

    # Subskill aliases so the controller can target individual archetype families if needed.
    if subskill_norm in {"markup", "mark-up", "fixed-markup", "fixed_markup", "cost-of-sales-backcalc", "cost_of_sales_backcalc"}:
        builders = [builders[1]]
    elif subskill_norm in {"interest-balancing", "interest_balancing", "interest-expense-balancing", "interest_expense_balancing"}:
        builders = [builders[2]]
    elif subskill_norm in {"loan-interest", "loan_interest", "loan-statement-interest", "loan_statement_interest"}:
        builders = [builders[3]]
    elif subskill_norm in {"theft", "stock-theft", "stock_theft", "insurance-loss", "insurance_loss"}:
        builders = [builders[4]]
    elif subskill_norm in {"missing-labels", "missing_labels", "labels"}:
        builders = [builders[5]]
    elif subskill_norm in {"sundry", "sundry-balancing", "sundry_balancing"}:
        builders = [builders[6]]
    elif subskill_norm in {"prepaid", "accrued", "prepaid-accrued", "prepaid_accrued"}:
        builders = [builders[7]]
    elif subskill_norm in {"debtors", "provision", "bad-debts", "bad_debts", "debtors-provision"}:
        builders = [builders[8]]
    elif subskill_norm in {"bank-statement", "bank_statement", "fixed-deposit", "fixed_deposit"}:
        builders = [builders[9]]
    elif subskill_norm in {"advertising", "advertising-contract", "advertising_contract"}:
        builders = [builders[10]]
    elif subskill_norm not in {"", "mixed", "income-statement", "income_statement"}:
        # Keep default pool for unknown aliases.
        builders = builders

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(builders)())

    return out
