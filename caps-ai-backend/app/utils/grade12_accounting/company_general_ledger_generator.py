from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

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


def _money(x: float) -> str:
    return _fmt_money(float(x))


def _make_t_account(
    *,
    prompt: str,
    journal_type: str,
    title_fields: List[Dict[str, Any]],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    cell_hints: Optional[Dict[str, str]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    headers = _t_account_headers()

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

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

    out["id"] = _make_id("acct12_company_gl")
    out["expected_answer_type"] = "journal"
    return out


def _make_equation_table(
    *,
    prompt: str,
    rows_values: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    archetype_key: str,
    cell_hints: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    headers = ["No.", "Account debited", "Account credited", "Amount"]

    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    base_editable_cols = [1, 2, 3]
    editable_cols = _journal_editable_cols_by_difficulty(
        difficulty=diff,
        base_editable_cols=base_editable_cols,
        total_cols=len(headers),
        mode=mode_norm,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(rows_values):
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
        journal_type="company_general_ledger_equation",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct side (Dr/Cr) for each entry.",
            "Enter amounts without a currency symbol.",
            "Close off the account where required (Balance c/d, Totals).",
        ],
        table_variant="grade_project",
        title_fields=[{"label": "General ledger", "value": ""}],
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
    )
    out["id"] = _make_id("acct12_company_gl")
    out["expected_answer_type"] = "journal"
    out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_company_gl_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _choose_company(r: random.Random) -> Tuple[str, str]:
    name = r.choice(["Kwik Fix Ltd", "Qoba Ltd", "Glebo Ltd", "Aneesa Ltd", "Kopano Ltd"])
    year = str(r.choice(["2016", "2017", "2018", "2020", "2021"]))
    return name, year


def _make_accounting_equation_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
) -> Dict[str, Any]:
    # Mirrors Q3 in curriculum doc: debit/credit identification from transactions.
    issued_shares = int(r.choice([700_000, 650_000, 800_000]))
    final_dividend_cents = int(r.choice([120, 80, 100]))
    final_dividend_amount = _round_money(issued_shares * (final_dividend_cents / 100.0))

    income_tax_amount = float(r.choice([1_150_000.0, 1_020_000.0, 980_000.0]))

    buyback_shares = 50_000
    buyback_price = float(r.choice([15.0, 14.0, 16.0]))
    avg_price = float(r.choice([11.0, 10.0, 12.0]))
    claim_from_osc = _round_money(buyback_shares * avg_price)
    buyback_total = _round_money(buyback_shares * buyback_price)
    claim_from_retained = _round_money(buyback_total - claim_from_osc)

    prompt = (
        "Companies — General Ledger (Accounting equation)\n\n"
        "Required: Use the table provided to indicate the Account credited and Account debited in the General Ledger for each transaction."  # noqa: E501
    )

    rows_values: List[List[Optional[str]]] = [
        [
            "3.1",
            "Ordinary share dividends",
            "Shareholders for dividends",
            _money(final_dividend_amount),
        ],
        [
            "3.2",
            "Income tax",
            "SARS: Income tax",
            _money(income_tax_amount),
        ],
        [
            "3.3",
            "Ordinary share capital",
            "Bank",
            _money(claim_from_osc),
        ],
        [
            "",
            "Retained income",
            "Bank",
            _money(claim_from_retained),
        ],
    ]

    return _make_equation_table(
        prompt=prompt,
        rows_values=rows_values,
        difficulty=difficulty,
        mode=mode,
        archetype_key="g12_company_gl_accounting_equation_q3",
    )


def _make_q1_scenario_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Q1 archetype: one scenario (opening balances + dated transactions) drives multiple linked ledger accounts.
    company = "Nyala Ltd"
    year = "2024"
    year_next = str(int(year) + 1)

    opening_share_price = float(r.choice([5.0, 5.3, 5.5]))
    opening_shares = int(r.choice([300_000, 330_000, 350_000, 400_000]))
    opening_osc = _round_money(opening_shares * opening_share_price)

    opening_retained = float(r.choice([480_000.0, 530_000.0, 600_000.0]))
    opening_sars_credit = float(r.choice([17_000.0, 22_800.0, 30_000.0]))
    opening_shareholders = float(r.choice([160_000.0, 184_800.0, 200_000.0]))

    provisional_1 = float(r.choice([140_000.0, 160_000.0, 180_000.0]))
    provisional_2 = float(r.choice([170_000.0, 194_000.0, 210_000.0]))

    interim_dividends = float(r.choice([120_000.0, 148_500.0, 170_000.0]))

    buyback_shares = int(r.choice([25_000, 30_000, 35_000]))
    buyback_price = float(r.choice([5.9, 6.1, 6.3]))

    issued_shares = int(r.choice([80_000, 100_000, 120_000]))
    issue_price = float(r.choice([6.2, 6.34, 6.5]))

    net_profit_before_tax = float(r.choice([900_000.0, 970_000.0, 1_050_000.0]))
    tax_rate = float(r.choice([0.30, 0.28]))
    income_tax = _round_money(net_profit_before_tax * tax_rate)

    closing_shares = int(opening_shares + issued_shares - buyback_shares)
    final_dividend_cents = int(r.choice([60, 70, 80]))
    final_dividends = _round_money(closing_shares * (final_dividend_cents / 100.0))
    total_dividends = _round_money(interim_dividends + final_dividends)

    retained_for_year = _round_money(net_profit_before_tax - income_tax - total_dividends)
    if retained_for_year < 0:
        retained_for_year = 0.0

    issued_capital = _round_money(issued_shares * issue_price)
    avg_price = (opening_osc + issued_capital) / float(opening_shares + issued_shares)
    claim_from_osc = _round_money(buyback_shares * avg_price)
    buyback_total = _round_money(buyback_shares * buyback_price)
    claim_from_retained = _round_money(max(0.0, buyback_total - claim_from_osc))

    # Shared final accounts case for Retained/Appropriation options.
    final_case: Dict[str, float] = {
        "net_profit": float(net_profit_before_tax),
        "income_tax": float(income_tax),
        "interim_dividends": float(interim_dividends),
        "final_dividends": float(final_dividends),
        "total_dividends": float(total_dividends),
        "retained_for_year": float(retained_for_year),
        "opening_retained": float(opening_retained),
        "buyback_adjustment": float(claim_from_retained),
        "closing_retained": _round_money(opening_retained + retained_for_year - claim_from_retained),
        "closing_before_buyback": _round_money(opening_retained + retained_for_year),
    }

    layout_option = int(r.choice([1, 2, 3]))

    prompt = (
        "Companies — General Ledger (Q1 Scenario)\n\n"
        f"Complete the following accounts in the General Ledger of {company} for the year ended {year} December 31:\n"
        "- Ordinary Share Capital\n"
        "- Retained Income\n"
        "- SARS (Income tax)\n"
        "- Shareholders for Dividends\n"
        "- Appropriation Account\n\n"
        "INFORMATION:\n"
        f"Opening balances on {year} Jan 1:\n"
        f"- Ordinary share capital: R{_money(opening_osc)}\n"
        f"- Retained income: R{_money(opening_retained)}\n"
        f"- SARS (Income tax) (Cr): R{_money(opening_sars_credit)}\n"
        f"- Shareholders for dividends: R{_money(opening_shareholders)}\n\n"
        f"Transactions during {year}:\n"
        "- Paid the opening balances owing to SARS and shareholders by EFT.\n"
        f"- Provisional tax payments: R{_money(provisional_1)} and R{_money(provisional_2)}\n"
        f"- Interim dividends declared and paid: R{_money(interim_dividends)}\n"
        f"- Repurchased {buyback_shares} ordinary shares at R{buyback_price:.2f} each\n"
        f"- Issued {issued_shares} ordinary shares at R{issue_price:.2f} each\n"
        f"- Final dividend declared at year-end: {final_dividend_cents} cents per share\n"
        f"- Net profit before tax: R{_money(net_profit_before_tax)}; income tax at {int(tax_rate*100)}%\n"
    )

    # Ordinary Share Capital account
    osc_rows: List[List[Optional[str]]] = []
    osc_rows.append(["", "", "", "", f"{year} Jan 1", "Balance b/d", "b/d", _money(opening_osc)])
    osc_rows.append([f"{year} May 20", f"Buy back of shares ({buyback_shares})", "GJ", _money(claim_from_osc), "", "", "", ""])
    osc_rows.append(["", "", "", "", f"{year} Jul 15", f"Bank (issue {issued_shares:,} @ R{issue_price:.2f})", "CRJ", _money(issued_capital)])
    closing_osc = _round_money(opening_osc + issued_capital - claim_from_osc)
    total_osc = _round_money(opening_osc + issued_capital)
    osc_rows.append([f"{year} Dec 31", "Balance c/d", "c/d", _money(closing_osc), "", "", "", ""])
    osc_rows.append(["", "Totals", "", _money(total_osc), "", "Totals", "", _money(total_osc)])
    osc_rows.append(["", "", "", "", f"{year_next} Jan 1", "Balance b/d", "b/d", _money(closing_osc)])

    osc_q = _make_t_account(
        prompt=(
            "Companies — General Ledger (T-accounts)\n\n"
            f"{company}: The company had an opening Ordinary Share Capital balance and issued new shares during the year. The directors also bought back some shares.\n\n"
            "Required: Draw up the Ordinary Share Capital account and close off the account."
        ),
        journal_type="company_ordinary_share_capital",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "ORDINARY SHARE CAPITAL", "value": ""},
        ],
        values_rows=osc_rows,
        difficulty=difficulty,
        mode=mode,
    )
    osc_q["meta"] = {
        "archetype_key": "g12_company_gl_ordinary_share_capital",
        "opening_shares": opening_shares,
        "opening_share_price": opening_share_price,
        "issued_shares": issued_shares,
        "issue_price": issue_price,
        "buyback_shares": buyback_shares,
        "buyback_price": buyback_price,
        "claim_from_ordinary_share_capital": claim_from_osc,
        "claim_from_retained_income": claim_from_retained,
    }

    # SARS (Income tax) account
    sars_rows: List[List[Optional[str]]] = []
    sars_rows.append(["", "", "", "", f"{year} Jan 1", "Balance b/d", "b/d", _money(opening_sars_credit)])
    sars_rows.append([f"{year} Jan 12", "Bank (paid last year's tax)", "CPJ", _money(opening_sars_credit), "", "", "", ""])
    sars_rows.append([f"{year} Mar 15", "Bank (provisional tax)", "CPJ", _money(provisional_1), "", "", "", ""])
    sars_rows.append([f"{year} Sept 30", "Bank (provisional tax)", "CPJ", _money(provisional_2), "", "", "", ""])
    sars_rows.append(["", "", "", "", f"{year} Dec 31", "Income tax", "GJ", _money(income_tax)])
    paid_total = _round_money(opening_sars_credit + provisional_1 + provisional_2)
    if income_tax >= paid_total:
        bal_cd = _round_money(income_tax - paid_total)
        sars_rows.append([f"{year} Dec 31", "Balance c/d", "c/d", _money(bal_cd), "", "", "", ""])
    else:
        bal_bd = _round_money(paid_total - income_tax)
        sars_rows.append(["", "", "", "", f"{year} Dec 31", "Balance c/d", "c/d", _money(bal_bd)])
    debit_total = _round_money(paid_total + (income_tax - paid_total if income_tax >= paid_total else 0.0))
    credit_total = _round_money(income_tax + (paid_total - income_tax if paid_total > income_tax else 0.0))
    total_sars = _round_money(max(debit_total, credit_total))
    sars_rows.append(["", "Totals", "", _money(total_sars), "", "Totals", "", _money(total_sars)])

    sars_q = _make_t_account(
        prompt=(
            "Companies — General Ledger (T-accounts)\n\n"
            f"{company}: Provisional tax payments were made during the year. After audit, the income tax for the year was determined.\n\n"
            "Required: Draw up the SARS (Income tax) account and close off the account."
        ),
        journal_type="company_sars_income_tax",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "SARS (INCOME TAX)", "value": ""},
        ],
        values_rows=sars_rows,
        difficulty=difficulty,
        mode=mode,
    )
    sars_q["meta"] = {
        "archetype_key": "g12_company_gl_sars_income_tax",
        "assessed_tax": float(income_tax),
        "provisional_1": float(provisional_1),
        "provisional_2": float(provisional_2),
        "opening_balance_credit": float(opening_sars_credit),
    }

    # Shareholders for Dividends account
    sh_rows: List[List[Optional[str]]] = []
    sh_rows.append([f"{year} Jan 12", "Bank (paid last year's dividends)", "CPJ", _money(opening_shareholders), "", "", "", ""])
    sh_rows.append(["", "", "", "", f"{year} Jan 1", "Balance b/d", "b/d", _money(opening_shareholders)])
    sh_rows.append([f"{year} Dec 31", "Balance c/d", "c/d", _money(final_dividends), "", "", "", ""])
    sh_rows.append(["", "", "", "", f"{year} Dec 31", "Dividends on ordinary shares", "GJ", _money(final_dividends)])
    tot_sh = _round_money(opening_shareholders + final_dividends)
    sh_rows.append(["", "Totals", "", _money(tot_sh), "", "Totals", "", _money(tot_sh)])
    sh_rows.append(["", "", "", "", f"{year_next} Jan 1", "Balance b/d", "b/d", _money(final_dividends)])

    sh_q = _make_t_account(
        prompt=(
            "Companies — General Ledger (T-accounts)\n\n"
            f"{company}: The company paid last year's dividends, paid an interim dividend during the year, and declared a final dividend at year-end (not yet paid).\n\n"
            "Required: Draw up the Shareholders for Dividends account and close off the account."
        ),
        journal_type="company_shareholders_for_dividends",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "SHAREHOLDERS FOR DIVIDENDS", "value": ""},
        ],
        values_rows=sh_rows,
        difficulty=difficulty,
        mode=mode,
    )
    sh_q["meta"] = {
        "archetype_key": "g12_company_gl_shareholders_for_dividends",
        "issued_shares": closing_shares,
        "interim_dividend_cents": None,
        "final_dividend_cents": final_dividend_cents,
    }

    retained_q = _make_retained_income_question(
        r=r,
        difficulty=difficulty,
        mode=mode,
        company=company,
        year=year,
        layout_option=layout_option,
        case=final_case,
    )
    appropriation_q = _make_appropriation_account_question(
        r=r,
        difficulty=difficulty,
        mode=mode,
        company=company,
        year=year,
        layout_option=layout_option,
        case=final_case,
    )

    out = _make_bundle(
        prompt=prompt,
        parts=[osc_q, retained_q, sars_q, sh_q, appropriation_q],
        archetype_key="g12_company_gl_q1_scenario_bundle",
    )
    out.setdefault("meta", {})
    out["meta"]["layout_option"] = layout_option
    return out


def _make_q2_scenario_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Q2 archetype: board-report style scenario driving OSC, Retained Income, SARS and Appropriation.
    company = "Royal Structures Ltd"
    year_end = "30 June 2023"
    year_start = "1 July 2022"
    year_next = "1 July 2023"

    opening_shares = int(r.choice([450_000, 500_000, 550_000]))
    opening_avg_price = float(r.choice([5.0, 5.2, 5.4]))
    opening_osc = _round_money(opening_shares * opening_avg_price)

    opening_retained = float(r.choice([850_000.0, 950_000.0, 1_050_000.0]))
    opening_sars_credit = float(r.choice([10_000.0, 17_000.0, 25_000.0]))

    issued_shares = int(r.choice([150_000, 200_000, 250_000]))
    issue_price = float(r.choice([6.1, 6.4, 6.7]))
    issued_capital = _round_money(issued_shares * issue_price)

    interim_dividend_cents = int(r.choice([15, 20, 25]))
    interim_dividends = _round_money((opening_shares + issued_shares) * (interim_dividend_cents / 100.0))

    provisional_1 = float(r.choice([240_000.0, 270_000.0, 300_000.0]))
    provisional_2 = float(r.choice([230_000.0, 250_000.0, 280_000.0]))

    buyback_shares = int(r.choice([50_000, 60_000, 70_000]))
    buyback_price = float(r.choice([6.8, 7.0, 7.2]))

    closing_shares = int(opening_shares + issued_shares - buyback_shares)
    final_dividend_cents = int(r.choice([50, 60, 70]))
    final_dividends = _round_money(closing_shares * (final_dividend_cents / 100.0))
    total_dividends = _round_money(interim_dividends + final_dividends)

    net_profit_before_tax = float(r.choice([1_500_000.0, 1_700_000.0, 1_900_000.0]))
    tax_rate = float(r.choice([0.30, 0.28]))
    income_tax = _round_money(net_profit_before_tax * tax_rate)

    retained_for_year = _round_money(net_profit_before_tax - income_tax - total_dividends)
    if retained_for_year < 0:
        retained_for_year = 0.0

    total_issued_shares = int(opening_shares + issued_shares)
    avg_price = (opening_osc + issued_capital) / float(total_issued_shares)
    claim_from_osc = _round_money(buyback_shares * avg_price)
    buyback_total = _round_money(buyback_shares * buyback_price)
    claim_from_retained = _round_money(max(0.0, buyback_total - claim_from_osc))

    final_case: Dict[str, float] = {
        "net_profit": float(net_profit_before_tax),
        "income_tax": float(income_tax),
        "interim_dividends": float(interim_dividends),
        "final_dividends": float(final_dividends),
        "total_dividends": float(total_dividends),
        "retained_for_year": float(retained_for_year),
        "opening_retained": float(opening_retained),
        "buyback_adjustment": float(claim_from_retained),
        "closing_retained": _round_money(opening_retained + retained_for_year - claim_from_retained),
        "closing_before_buyback": _round_money(opening_retained + retained_for_year),
    }

    # Q2 shows alternative methods; we map them to the 3 layout options already implemented.
    layout_option = int(r.choice([1, 2, 3]))

    prompt = (
        "Companies — General Ledger (Q2 Report Scenario)\n\n"
        f"{company} is a company that manufactures trailers, mobile houses and mobile offices.\n"
        "Required: Prepare the following ledger accounts for the year ended "
        f"{year_end}:\n"
        "- Ordinary Share Capital\n"
        "- Retained Income\n"
        "- SARS (Income tax)\n"
        "- Appropriation Account\n\n"
        "INFORMATION:\n"
        f"Opening balances on {year_start}:\n"
        f"- Ordinary share capital: R{_money(opening_osc)}\n"
        f"- Retained income: R{_money(opening_retained)}\n"
        f"- SARS (Income tax) (Cr): R{_money(opening_sars_credit)}\n\n"
        "Transactions:\n"
        f"- Issued {issued_shares} ordinary shares at R{issue_price:.2f} each.\n"
        f"- Paid provisional tax: R{_money(provisional_1)} and R{_money(provisional_2)}.\n"
        f"- Interim dividends paid: {interim_dividend_cents} cents per share.\n"
        f"- Final dividend declared: {final_dividend_cents} cents per share (not yet paid).\n"
        f"- Bought back {buyback_shares} shares at R{buyback_price:.2f} per share.\n"
        f"- Net profit before tax: R{_money(net_profit_before_tax)}; income tax at {int(tax_rate*100)}%\n"
    )

    # Ordinary Share Capital (simplified but reconciled)
    osc_rows: List[List[Optional[str]]] = []
    osc_rows.append(["", "", "", "", "2022 Jul 1", "Balance b/d", "b/d", _money(opening_osc)])
    osc_rows.append(["2023 Jun 30", f"Buy back of shares ({buyback_shares})", "GJ", _money(claim_from_osc), "", "", "", ""])
    osc_rows.append(["", "", "", "", "2022 Jul 1", f"Bank (issue {issued_shares:,} @ R{issue_price:.2f})", "CRJ", _money(issued_capital)])
    closing_osc = _round_money(opening_osc + issued_capital - claim_from_osc)
    total_osc = _round_money(opening_osc + issued_capital)
    osc_rows.append(["2023 Jun 30", "Balance c/d", "c/d", _money(closing_osc), "", "", "", ""])
    osc_rows.append(["", "Totals", "", _money(total_osc), "", "Totals", "", _money(total_osc)])
    osc_rows.append(["", "", "", "", year_next, "Balance b/d", "b/d", _money(closing_osc)])

    osc_q = _make_t_account(
        prompt=(
            "Companies — General Ledger (T-accounts)\n\n"
            f"{company}: Shares were issued and a portion of shares were bought back during the year.\n\n"
            "Required: Draw up the Ordinary Share Capital account and close off the account."
        ),
        journal_type="company_ordinary_share_capital",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "ORDINARY SHARE CAPITAL", "value": ""},
        ],
        values_rows=osc_rows,
        difficulty=difficulty,
        mode=mode,
    )
    osc_q["meta"] = {
        "archetype_key": "g12_company_gl_ordinary_share_capital",
        "opening_shares": opening_shares,
        "opening_avg_price": opening_avg_price,
        "issued_shares": issued_shares,
        "issue_price": issue_price,
        "buyback_shares": buyback_shares,
        "buyback_price": buyback_price,
        "claim_from_ordinary_share_capital": claim_from_osc,
        "claim_from_retained_income": claim_from_retained,
    }

    # SARS (Income tax)
    sars_rows: List[List[Optional[str]]] = []
    sars_rows.append(["", "", "", "", "2022 Jul 1", "Balance b/d", "b/d", _money(opening_sars_credit)])
    sars_rows.append(["2022 Jul 20", "Bank", "CPJ", _money(opening_sars_credit), "", "", "", ""])
    sars_rows.append(["2022 Dec 31", "Bank", "CPJ", _money(provisional_1), "", "", "", ""])
    sars_rows.append(["2023 Jun 30", "Bank", "CPJ", _money(provisional_2), "", "", "", ""])
    sars_rows.append(["", "", "", "", "2023 Jun 30", "Income tax", "GJ", _money(income_tax)])
    paid_total = _round_money(opening_sars_credit + provisional_1 + provisional_2)
    if income_tax >= paid_total:
        bal_cd = _round_money(income_tax - paid_total)
        sars_rows.append(["2023 Jun 30", "Balance c/d", "c/d", _money(bal_cd), "", "", "", ""])
    else:
        bal_bd = _round_money(paid_total - income_tax)
        sars_rows.append(["", "", "", "", "2023 Jun 30", "Balance c/d", "c/d", _money(bal_bd)])
    debit_total = _round_money(paid_total + (income_tax - paid_total if income_tax >= paid_total else 0.0))
    credit_total = _round_money(income_tax + (paid_total - income_tax if paid_total > income_tax else 0.0))
    total_sars = _round_money(max(debit_total, credit_total))
    sars_rows.append(["", "Totals", "", _money(total_sars), "", "Totals", "", _money(total_sars)])

    sars_q = _make_t_account(
        prompt=(
            "Companies — General Ledger (T-accounts)\n\n"
            f"{company}: Provisional tax payments were made during the year. After audit, the income tax for the year was determined.\n\n"
            "Required: Draw up the SARS (Income tax) account and close off the account."
        ),
        journal_type="company_sars_income_tax",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "SARS (INCOME TAX)", "value": ""},
        ],
        values_rows=sars_rows,
        difficulty=difficulty,
        mode=mode,
    )
    sars_q["meta"] = {
        "archetype_key": "g12_company_gl_sars_income_tax",
        "assessed_tax": float(income_tax),
        "provisional_1": float(provisional_1),
        "provisional_2": float(provisional_2),
        "opening_balance_credit": float(opening_sars_credit),
    }

    retained_q = _make_retained_income_question(
        r=r,
        difficulty=difficulty,
        mode=mode,
        company=company,
        year="2023",
        layout_option=layout_option,
        case=final_case,
    )
    appropriation_q = _make_appropriation_account_question(
        r=r,
        difficulty=difficulty,
        mode=mode,
        company=company,
        year="2023",
        layout_option=layout_option,
        case=final_case,
    )

    out = _make_bundle(
        prompt=prompt,
        parts=[osc_q, retained_q, sars_q, appropriation_q],
        archetype_key="g12_company_gl_q2_scenario_bundle",
    )
    out.setdefault("meta", {})
    out["meta"]["layout_option"] = layout_option
    out["meta"]["issued_shares"] = issued_shares
    out["meta"]["buyback_shares"] = buyback_shares
    return out


def _make_ordinary_share_capital_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    opening_shares = int(r.choice([400_000, 500_000, 600_000]))
    opening_avg_price = float(r.choice([2.0, 2.5, 3.0]))
    opening_capital = _round_money(opening_shares * opening_avg_price)

    issued_shares = int(r.choice([50_000, 80_000, 100_000]))
    issue_price = float(r.choice([6.0, 7.5, 8.0]))
    issued_capital = _round_money(issued_shares * issue_price)

    total_shares = opening_shares + issued_shares
    closing_capital = _round_money(opening_capital + issued_capital)

    avg_price = _round_money(closing_capital / float(total_shares))

    buyback_shares = int(r.choice([20_000, 30_000, 40_000]))
    buyback_price = float(r.choice([8.5, 9.0, 7.5]))

    buyback_total = _round_money(buyback_shares * buyback_price)
    claim_from_osc = _round_money(buyback_shares * avg_price)
    claim_from_retained = _round_money(buyback_total - claim_from_osc)

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: The company had an opening Ordinary Share Capital balance and issued new shares during the year. "
        "The directors also bought back some shares.\n\n"
        "Required: Draw up the Ordinary Share Capital account and close off the account."  # minimal
    )

    headers = _t_account_headers()

    # Rows: [Dr date, Dr details, Dr fol, Dr amt, Cr date, Cr details, Cr fol, Cr amt]
    rows: List[List[Optional[str]]] = []

    rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening_capital)])
    rows.append(["", "", "", "", f"{year} Jul 1", f"Bank (issue {issued_shares:,} @ R{issue_price:.2f})", "CRJ", _money(issued_capital)])

    # buyback: debit ordinary share capital for average price portion
    rows.append([f"{year} Dec 1", f"Buy back of shares ({buyback_shares:,})", "GJ", _money(claim_from_osc), "", "", "", ""])

    credit_sum = _round_money(opening_capital + issued_capital)
    debit_sum = _round_money(claim_from_osc)

    balance_cd = _round_money(credit_sum - debit_sum)
    total = _round_money(max(credit_sum, debit_sum + balance_cd))

    rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(balance_cd), "", "", "", ""])
    rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])
    rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(balance_cd)])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c7"] = "Issue of shares increases ordinary share capital (credit)."
        cell_hints["t0_r2_c3"] = "Buy back: debit ordinary share capital for the average issue price portion."
        cell_hints["t0_r3_c3"] = "Balance c/d is the closing balance."  # optional

    # ── Build rubric_map ──
    rubric_map: Dict[str, Dict[str, Any]] = {
        "t0_r0_c7": {
            "formula_structure": "Opening balance b/d",
            "foundational_values": [opening_capital],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r1_c7": {
            "formula_structure": f"Issue of shares = {issued_shares:,} × R{issue_price:.2f}",
            "foundational_values": [float(issued_shares), issue_price],
            "operations": ["×"],
            "max_score": 1.5,
        },
        "t0_r2_c3": {
            "formula_structure": f"Buy back = {buyback_shares:,} shares × average price",
            "foundational_values": [float(buyback_shares), avg_price],
            "operations": ["×"],
            "max_score": 2.0,
        },
        "t0_r3_c3": {
            "formula_structure": "Balance c/d = Total credits − Total debits",
            "foundational_values": [credit_sum, debit_sum],
            "operations": ["−"],
            "max_score": 1.5,
        },
    }
    dependency_map: Dict[str, List[str]] = {
        "t0_r2_c3": ["t0_r0_c7", "t0_r1_c7"],
        "t0_r3_c3": ["t0_r0_c7", "t0_r1_c7", "t0_r2_c3"],
    }

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_ordinary_share_capital",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "ORDINARY SHARE CAPITAL", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )

    q["meta"] = {
        "archetype_key": "g12_company_gl_ordinary_share_capital",
        "opening_shares": opening_shares,
        "opening_avg_price": opening_avg_price,
        "issued_shares": issued_shares,
        "issue_price": issue_price,
        "buyback_shares": buyback_shares,
        "buyback_price": buyback_price,
        "buyback_total": buyback_total,
        "claim_from_ordinary_share_capital": claim_from_osc,
        "claim_from_retained_income": claim_from_retained,
    }

    return q


def _make_company_general_ledger_full_bundle(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    company, year = _choose_company(r)

    layout_option = int(r.choice([1, 2, 3]))
    final_case = _make_final_accounts_case(r=r)

    prompt = f"""Companies — General Ledger (Full set)

#### REQUIRED:
Complete the following General Ledger accounts for {company} for the year ended {year} February 28:
- Ordinary Share Capital
- Retained Income
- SARS (Income tax)
- Shareholders for Dividends
- Appropriation Account

#### INFORMATION:
Use the information provided in each part/table."""

    parts = [
        _make_ordinary_share_capital_question(r=r, difficulty=difficulty, mode=mode, company=company, year=year),
        _make_retained_income_question(
            r=r,
            difficulty=difficulty,
            mode=mode,
            company=company,
            year=year,
            layout_option=layout_option,
            case=final_case,
        ),
        _make_sars_income_tax_question(r=r, difficulty=difficulty, mode=mode, company=company, year=year),
        _make_shareholders_for_dividends_question(r=r, difficulty=difficulty, mode=mode, company=company, year=year),
        _make_appropriation_account_question(
            r=r,
            difficulty=difficulty,
            mode=mode,
            company=company,
            year=year,
            layout_option=layout_option,
            case=final_case,
        ),
    ]

    out = _make_bundle(prompt=prompt, parts=parts, archetype_key="g12_company_gl_full_workflow_bundle")
    out.setdefault("meta", {})
    out["meta"]["layout_option"] = layout_option
    return out


def _make_shareholders_for_dividends_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    opening_payable = float(r.choice([70_000, 90_000, 130_000]))
    interim_cents = float(r.choice([0.15, 0.20, 0.25]))
    final_cents = float(r.choice([0.30, 0.35, 0.40]))

    issued_shares = int(r.choice([250_000, 310_000, 400_000, 550_000]))

    interim_total = _round_money(issued_shares * interim_cents)
    final_declared = _round_money(issued_shares * final_cents)

    paid_opening = opening_payable
    paid_interim = interim_total

    credit_sum = _round_money(opening_payable + final_declared)
    debit_sum = _round_money(paid_opening + paid_interim)

    balance_cd = _round_money(credit_sum - debit_sum)
    total = _round_money(max(credit_sum, debit_sum + balance_cd))

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: The company paid last year's dividends, paid an interim dividend during the year, and declared a final dividend at year-end (not yet paid).\n\n"
        "Required: Draw up the Shareholders for Dividends account and close off the account."
    )

    rows: List[List[Optional[str]]] = []

    rows.append([f"{year} Jul 1", "Bank (paid last year's dividends)", "CPJ", _money(paid_opening), "", "", "", ""])
    rows.append([f"{year} Dec 31", "Bank (interim dividend)", "CPJ", _money(paid_interim), "", "", "", ""])

    rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening_payable)])
    rows.append(["", "", "", "", f"{year} Feb 28", "Dividends on ordinary shares", "GJ", _money(final_declared)])

    rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(balance_cd), "", "", "", ""])
    rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])
    rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(balance_cd)])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c3"] = "Paying dividends reduces the liability (debit)."
        cell_hints["t0_r3_c7"] = "Declaring the final dividend increases the liability (credit)."

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_shareholders_for_dividends",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "SHAREHOLDERS FOR DIVIDENDS", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
    )

    q["meta"] = {
        "archetype_key": "g12_company_gl_shareholders_for_dividends",
        "issued_shares": issued_shares,
        "interim_dividend_cents": int(round(interim_cents * 100.0)),
        "final_dividend_cents": int(round(final_cents * 100.0)),
    }

    return q


def _make_sars_income_tax_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    opening_ct = float(r.choice([0.0, 9_000.0, 15_000.0]))
    paid_opening = opening_ct if opening_ct > 0 else 0.0

    prov1 = float(r.choice([100_000.0, 112_500.0, 85_000.0]))
    prov2 = float(r.choice([120_000.0, 135_000.0, 150_000.0]))

    assessed_tax = float(r.choice([240_000.0, 300_000.0, 150_285.0]))

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: Provisional tax payments were made during the year. After audit, the income tax for the year was determined.\n\n"
        "Required: Draw up the SARS (Income tax) account and close off the account."
    )

    # Convention:
    # - Payments to SARS: debit SARS (income tax) account.
    # - Assessed tax expense: credit SARS (income tax) account.
    # - Opening credit balance b/d: credit.

    credit_sum = _round_money(opening_ct + assessed_tax)
    debit_sum = _round_money(paid_opening + prov1 + prov2)

    # Balance c/d goes on the side needed to balance.
    balance_cd = _round_money(abs(credit_sum - debit_sum))
    balance_cd_side = "debit" if credit_sum > debit_sum else "credit"
    total = _round_money(max(credit_sum, debit_sum))

    rows: List[List[Optional[str]]] = []

    if opening_ct > 0:
        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening_ct)])

    if paid_opening > 0:
        rows.append([f"{year} Jul 23", "Bank (paid last year's tax)", "CPJ", _money(paid_opening), "", "", "", ""])

    rows.append([f"{year} Dec 31", "Bank (provisional tax)", "CPJ", _money(prov1), "", "", "", ""])
    rows.append([f"{year} Feb 28", "Bank (provisional tax)", "CPJ", _money(prov2), "", "", "", ""])

    rows.append(["", "", "", "", f"{year} Feb 28", "Income tax", "GJ", _money(assessed_tax)])

    if balance_cd_side == "debit":
        rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(balance_cd), "", "", "", ""])
    else:
        rows.append(["", "", "", "", f"{year} Feb 28", "Balance c/d", "c/d", _money(balance_cd)])

    rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])

    if balance_cd_side == "debit":
        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(balance_cd)])
    else:
        rows.append([f"{year} Mar 1", "Balance b/d", "b/d", _money(balance_cd), "", "", "", ""])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r2_c3"] = "Provisional tax payments are debited to SARS (Income tax)."
        cell_hints["t0_r4_c7"] = "Assessed tax is credited to SARS (Income tax)."

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_sars_income_tax",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "SARS (INCOME TAX)", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
    )

    q["meta"] = {
        "archetype_key": "g12_company_gl_sars_income_tax",
        "assessed_tax": assessed_tax,
        "provisional_1": prov1,
        "provisional_2": prov2,
        "opening_balance_credit": opening_ct,
    }
    return q


def _make_income_tax_nominal_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    tax_expense = float(r.choice([185_000.0, 240_000.0, 300_000.0, 150_285.0]))

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: At year-end the income tax expense must be transferred to the Appropriation Account.\n\n"
        "Required: Draw up the Income Tax account (nominal) and close off the account."
    )

    # Income tax nominal account:
    # - Assessed tax is posted: Dr Income tax; Cr SARS (Income tax)
    # - Then transfer the expense to appropriation: Dr Appropriation; Cr Income tax
    rows: List[List[Optional[str]]] = []
    rows.append([f"{year} Feb 28", "SARS (Income tax)", "GJ", _money(tax_expense), "", "", "", ""])
    rows.append(["", "", "", "", f"{year} Feb 28", "Appropriation", "GJ", _money(tax_expense)])
    rows.append(["", "Totals", "", _money(tax_expense), "", "Totals", "", _money(tax_expense)])

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_income_tax_nominal",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "INCOME TAX", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
    )
    q["meta"] = {"archetype_key": "g12_company_gl_income_tax_nominal", "income_tax_expense": tax_expense}
    return q


def _make_dividends_on_ordinary_shares_nominal_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    interim = float(r.choice([85_000.0, 95_000.0, 120_000.0]))
    final = float(r.choice([110_000.0, 125_000.0, 160_000.0]))
    total = _round_money(interim + final)

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: Interim and final dividends were declared during the year.\n\n"
        "Required: Draw up the Dividends on ordinary shares account (nominal) and close off the account."
    )

    # Dividends on ordinary shares nominal account:
    # - Declaration posted: Dr Dividends; Cr Shareholders for dividends
    # - Then transfer to appropriation: Dr Appropriation; Cr Dividends
    rows: List[List[Optional[str]]] = []
    rows.append([f"{year} Feb 28", "Shareholders for dividends", "GJ", _money(total), "", "", "", ""])
    rows.append(["", "", "", "", f"{year} Feb 28", "Appropriation", "GJ", _money(total)])
    rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c3"] = f"Total dividends = Interim R{_money(interim)} + Final R{_money(final)} = R{_money(total)}"

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_dividends_nominal",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "DIVIDENDS ON ORDINARY SHARES", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
    )
    q["meta"] = {
        "archetype_key": "g12_company_gl_dividends_nominal",
        "interim_dividends": interim,
        "final_dividends": final,
        "total_dividends": total,
    }
    return q


def _make_final_accounts_case(*, r: random.Random) -> Dict[str, float]:
    # Ensure the case is internally consistent: net profit must cover income tax + dividends.
    # Otherwise the "retained for year" becomes negative and leads to invalid negative ledger amounts.
    retained_for_year = -1.0
    while retained_for_year < 0:
        net_profit = float(r.choice([320_000.0, 450_000.0, 580_000.0, 275_000.0]))
        income_tax = float(r.choice([150_000.0, 185_000.0, 240_000.0]))

        interim_dividends = float(r.choice([85_000.0, 95_000.0, 120_000.0]))
        final_dividends = float(r.choice([110_000.0, 125_000.0, 160_000.0]))
        total_dividends = _round_money(interim_dividends + final_dividends)
        retained_for_year = _round_money(net_profit - income_tax - total_dividends)

    opening_retained = float(r.choice([420_000.0, 510_000.0, 650_000.0]))
    buyback_adjustment = float(r.choice([0.0, 0.0, 18_000.0, 25_000.0, 35_000.0]))
    closing_retained = _round_money(opening_retained + retained_for_year - buyback_adjustment)
    closing_before_buyback = _round_money(closing_retained + buyback_adjustment)

    return {
        "net_profit": net_profit,
        "income_tax": income_tax,
        "interim_dividends": interim_dividends,
        "final_dividends": final_dividends,
        "total_dividends": total_dividends,
        "retained_for_year": retained_for_year,
        "opening_retained": opening_retained,
        "buyback_adjustment": buyback_adjustment,
        "closing_retained": closing_retained,
        "closing_before_buyback": closing_before_buyback,
    }


def _make_retained_income_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
    layout_option: int = 1,
    case: Optional[Dict[str, float]] = None,
) -> Dict[str, Any]:
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)

    c = case or _make_final_accounts_case(r=r)
    opening = float(c["opening_retained"])
    buyback_adjustment = float(c["buyback_adjustment"])
    retained_for_year = float(c["retained_for_year"])
    closing_retained = float(c["closing_retained"])
    closing_before_buyback = float(c["closing_before_buyback"])

    prompt = (
        "Companies — General Ledger (T-accounts)\n\n"
        f"{company}: Update the Retained Income account with the transfer from the Appropriation Account and any share buy-back adjustment.\n\n"
        "Required: Draw up the Retained Income account and close off the account."
    )

    rows: List[List[Optional[str]]] = []

    opt = int(layout_option) if int(layout_option) in {1, 2, 3} else 1

    if opt == 1:
        # Option 1 (common): opening retained on credit; transfer in from appropriation on credit; buy-back claim on debit.
        credit_sum = _round_money(opening + retained_for_year)
        debit_sum = _round_money(buyback_adjustment)
        total = _round_money(credit_sum)

        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening)])
        rows.append(["", "", "", "", f"{year} Feb 28", "Appropriation", "GJ", _money(retained_for_year)])
        if buyback_adjustment > 0:
            rows.append([f"{year} Dec 1", "Buy back of shares (claim)", "GJ", _money(buyback_adjustment), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(closing_retained), "", "", "", ""])
        rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])
        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(closing_retained)])
        archetype_key = "g12_company_gl_retained_income_option1"
    elif opt == 2:
        # Option 2: transfer retained income at start (after buy-back adjustment) to appropriation, and transfer closing from appropriation.
        opening_less_buyback = _round_money(opening - buyback_adjustment)
        credit_from_appropriation = _round_money(opening + retained_for_year)
        debit_sum = _round_money(buyback_adjustment + opening)
        credit_sum = _round_money(opening + credit_from_appropriation)
        total = _round_money(max(debit_sum + closing_retained, credit_sum))

        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening)])
        if buyback_adjustment > 0:
            rows.append([f"{year} Dec 1", "Buy back of shares (claim)", "GJ", _money(buyback_adjustment), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Appropriation", "GJ", _money(opening_less_buyback), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(closing_retained), "", "", "", ""])
        rows.append(["", "", "", "", f"{year} Feb 28", "Appropriation", "GJ", _money(credit_from_appropriation)])
        rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])
        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(closing_retained)])
        archetype_key = "g12_company_gl_retained_income_option2"
    else:
        # Option 3: transfer full opening to appropriation, and transfer closing before buy-back back from appropriation.
        opening_to_appropriation = _round_money(opening)
        credit_from_appropriation = _round_money(closing_before_buyback)
        debit_sum = _round_money(buyback_adjustment + opening_to_appropriation)
        credit_sum = _round_money(opening + credit_from_appropriation)
        total = _round_money(max(debit_sum + closing_retained, credit_sum))

        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(opening)])
        if buyback_adjustment > 0:
            rows.append([f"{year} Dec 1", "Buy back of shares (claim)", "GJ", _money(buyback_adjustment), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Appropriation", "GJ", _money(opening_to_appropriation), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Balance c/d", "c/d", _money(closing_retained), "", "", "", ""])
        rows.append(["", "", "", "", f"{year} Feb 28", "Appropriation", "GJ", _money(credit_from_appropriation)])
        rows.append(["", "Totals", "", _money(total), "", "Totals", "", _money(total)])
        rows.append(["", "", "", "", f"{year} Mar 1", "Balance b/d", "b/d", _money(closing_retained)])
        archetype_key = "g12_company_gl_retained_income_option3"

    # ── Build rubric_map for Option 1 ──
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None
    dep_map: Optional[Dict[str, List[str]]] = None
    if opt == 1:
        rubric_map = {
            "t0_r0_c7": {
                "formula_structure": "Opening retained income balance b/d",
                "foundational_values": [opening],
                "operations": [],
                "max_score": 1.0,
            },
            "t0_r1_c7": {
                "formula_structure": "Transfer from Appropriation Account",
                "foundational_values": [retained_for_year],
                "operations": [],
                "max_score": 1.0,
            },
        }
        bal_row = 2
        if buyback_adjustment > 0:
            rubric_map["t0_r2_c3"] = {
                "formula_structure": "Buy back of shares claim",
                "foundational_values": [buyback_adjustment],
                "operations": [],
                "max_score": 1.0,
            }
            bal_row = 3
        rubric_map[f"t0_r{bal_row}_c3"] = {
            "formula_structure": "Balance c/d = Opening + Retained for year − Buy back",
            "foundational_values": [opening, retained_for_year, buyback_adjustment],
            "operations": ["+", "−"],
            "max_score": 1.5,
        }
        dep_map = {
            f"t0_r{bal_row}_c3": ["t0_r0_c7", "t0_r1_c7"],
        }

    q = _make_t_account(
        prompt=prompt,
        journal_type="company_retained_income",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "RETAINED INCOME", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        rubric_map=rubric_map,
        dependency_map=dep_map,
    )
    q["meta"] = {
        "archetype_key": archetype_key,
        "opening_retained_income": opening,
        "retained_for_year": retained_for_year,
        "buyback_adjustment": buyback_adjustment,
        "closing_retained_income": closing_retained,
    }
    return q


def _make_appropriation_account_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    company: Optional[str] = None,
    year: Optional[str] = None,
    layout_option: int = 1,
    case: Optional[Dict[str, float]] = None,
) -> Dict[str, Any]:
    """Grade 12 - Appropriation Account for dividend calculations."""
    company0, year0 = _choose_company(r)
    company = str(company or company0)
    year = str(year or year0)
    
    c = case or _make_final_accounts_case(r=r)
    net_profit = float(c["net_profit"])
    income_tax = float(c["income_tax"])
    interim_dividends = float(c["interim_dividends"])
    final_dividends = float(c["final_dividends"])
    total_dividends = float(c["total_dividends"])
    retained_for_year = float(c["retained_for_year"])
    opening_retained = float(c["opening_retained"])
    buyback_adjustment = float(c["buyback_adjustment"])
    closing_retained = float(c["closing_retained"])
    closing_before_buyback = float(c["closing_before_buyback"])

    rows: List[List[Optional[str]]] = []

    opt = int(layout_option) if int(layout_option) in {1, 2, 3} else 1
    if opt == 1:
        # Option 1: debit tax + dividends + retained for year; credit net profit.
        rows.append([f"{year} Feb 28", "Income tax", "GJ", _money(income_tax), f"{year} Feb 28", "Profit and loss", "GJ", _money(net_profit)])
        rows.append([f"{year} Feb 28", "Dividends on ordinary shares", "GJ", _money(total_dividends), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Retained income", "GJ", _money(retained_for_year), "", "", "", ""])
        tot = _money(net_profit)
        rows.append(["", "Totals", "", tot, "", "Totals", "", tot])
        archetype_key = "g12_company_gl_appropriation_account_option1"
    elif opt == 2:
        # Option 2: include opening retained (less buy-back adjustment) on credit side.
        opening_less_buyback = _round_money(opening_retained - buyback_adjustment)
        rows.append([f"{year} Feb 28", "Income tax", "GJ", _money(income_tax), f"{year} Feb 28", "Profit and loss", "GJ", _money(net_profit)])
        rows.append([f"{year} Feb 28", "Dividends on ordinary shares", "GJ", _money(total_dividends), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Retained income", "GJ", _money(closing_retained), "", "", "", ""])
        rows.append(["", "", "", "", f"{year} Feb 28", f"Retained income ({_money(opening_retained)} - {_money(buyback_adjustment)})", "GJ", _money(opening_less_buyback)])
        tot = _money(_round_money(net_profit + opening_less_buyback))
        rows.append(["", "Totals", "", tot, "", "Totals", "", tot])
        archetype_key = "g12_company_gl_appropriation_account_option2"
    else:
        # Option 3: include full opening retained on credit; transfer closing BEFORE buy-back on debit.
        rows.append([f"{year} Feb 28", "Income tax", "GJ", _money(income_tax), f"{year} Feb 28", "Profit and loss", "GJ", _money(net_profit)])
        rows.append([f"{year} Feb 28", "Dividends on ordinary shares", "GJ", _money(total_dividends), "", "", "", ""])
        rows.append([f"{year} Feb 28", "Retained income", "GJ", _money(closing_before_buyback), "", "", "", ""])
        rows.append(["", "", "", "", f"{year} Feb 28", "Retained income", "GJ", _money(opening_retained)])
        tot = _money(_round_money(net_profit + opening_retained))
        rows.append(["", "Totals", "", tot, "", "Totals", "", tot])
        archetype_key = "g12_company_gl_appropriation_account_option3"
    
    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r0_c3"] = "Income tax is transferred to the Appropriation Account (debit)."
        cell_hints["t0_r1_c3"] = f"Total dividends = Interim R{_money(interim_dividends)} + Final R{_money(final_dividends)} = R{_money(total_dividends)}"
        cell_hints["t0_r2_c3"] = "Retained income is the amount kept in the business."
    
    prompt = f"""Companies — General Ledger

#### REQUIRED:
Prepare the Appropriation Account for {company} for the year ended {year} February 28.

#### INFORMATION:
- Net profit for the year: R{_money(net_profit)}
- Income tax: R{_money(income_tax)}
- Interim dividends declared: R{_money(interim_dividends)}
- Final dividends declared: R{_money(final_dividends)}"""
    
    # ── Build rubric_map for Option 1 ──
    appro_rubric: Optional[Dict[str, Dict[str, Any]]] = None
    appro_dep: Optional[Dict[str, List[str]]] = None
    if opt == 1:
        appro_rubric = {
            "t0_r0_c3": {
                "formula_structure": "Income tax (from SARS assessment)",
                "foundational_values": [income_tax],
                "operations": [],
                "max_score": 1.0,
            },
            "t0_r0_c7": {
                "formula_structure": "Net profit from Profit and Loss",
                "foundational_values": [net_profit],
                "operations": [],
                "max_score": 1.0,
            },
            "t0_r1_c3": {
                "formula_structure": "Total dividends = Interim + Final",
                "foundational_values": [interim_dividends, final_dividends],
                "operations": ["+"],
                "max_score": 1.5,
            },
            "t0_r2_c3": {
                "formula_structure": "Retained income = Net profit − Tax − Dividends",
                "foundational_values": [net_profit, income_tax, total_dividends],
                "operations": ["−", "−"],
                "max_score": 2.0,
            },
        }
        appro_dep = {
            "t0_r2_c3": ["t0_r0_c7", "t0_r0_c3", "t0_r1_c3"],
        }

    out = _make_t_account(
        prompt=prompt,
        journal_type="company_appropriation_account",
        title_fields=[
            {"label": "General ledger of company", "value": ""},
            {"label": "APPROPRIATION ACCOUNT", "value": ""},
        ],
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        cell_hints=cell_hints,
        rubric_map=appro_rubric,
        dependency_map=appro_dep,
    )
    
    out["meta"] = {
        "archetype_key": archetype_key,
        "net_profit": net_profit,
        "income_tax": income_tax,
        "interim_dividends": interim_dividends,
        "final_dividends": final_dividends,
        "total_dividends": total_dividends,
        "retained_for_year": retained_for_year,
        "opening_retained_income": opening_retained,
        "buyback_adjustment": buyback_adjustment,
        "closing_retained_income": closing_retained,
    }
    
    return out


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

    builders: List[Any] = [
        lambda: _make_ordinary_share_capital_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_accounting_equation_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_retained_income_question(r=r, difficulty=difficulty, mode=mode, layout_option=1),
        lambda: _make_retained_income_question(r=r, difficulty=difficulty, mode=mode, layout_option=2),
        lambda: _make_retained_income_question(r=r, difficulty=difficulty, mode=mode, layout_option=3),
        lambda: _make_sars_income_tax_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_shareholders_for_dividends_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_income_tax_nominal_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_dividends_on_ordinary_shares_nominal_question(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_appropriation_account_question(r=r, difficulty=difficulty, mode=mode, layout_option=1),
        lambda: _make_appropriation_account_question(r=r, difficulty=difficulty, mode=mode, layout_option=2),
        lambda: _make_appropriation_account_question(r=r, difficulty=difficulty, mode=mode, layout_option=3),
        lambda: _make_company_general_ledger_full_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_q1_scenario_bundle(r=r, difficulty=difficulty, mode=mode),
        lambda: _make_q2_scenario_bundle(r=r, difficulty=difficulty, mode=mode),
    ]

    # Option C: mixed returns only bundle-style archetypes.
    if subskill_norm in {"mixed", ""}:
        builders = [builders[12], builders[13], builders[14]]

    if subskill_norm in {"ordinary-share-capital", "share-capital", "ordinary_share_capital"}:
        builders = [builders[0]]
    elif subskill_norm in {"accounting-equation", "accounting_equation", "equation", "q3"}:
        builders = [builders[1]]
    elif subskill_norm in {"q1", "q1-ledger-accounts", "q1_ledger_accounts", "q1-ledger", "q1_bundle"}:
        builders = [builders[13]]
    elif subskill_norm in {"q2", "q2-company-ledger-account", "q2_company_ledger_account", "q2-ledger", "q2_bundle"}:
        builders = [builders[14]]
    elif subskill_norm in {"retained", "retained-income", "retained_income"}:
        builders = [builders[2], builders[3], builders[4]]
    elif subskill_norm in {"retained-option1", "retained_option1", "retained-income-option1"}:
        builders = [builders[2]]
    elif subskill_norm in {"retained-option2", "retained_option2", "retained-income-option2"}:
        builders = [builders[3]]
    elif subskill_norm in {"retained-option3", "retained_option3", "retained-income-option3"}:
        builders = [builders[4]]
    elif subskill_norm in {"sars", "income-tax", "income_tax"}:
        builders = [builders[5]]
    elif subskill_norm in {"dividends", "shareholders-for-dividends", "shareholders_for_dividends"}:
        builders = [builders[6]]
    elif subskill_norm in {"income-tax-nominal", "income_tax_nominal", "tax-nominal", "nominal-tax"}:
        builders = [builders[7]]
    elif subskill_norm in {"dividends-nominal", "dividends_nominal", "nominal-dividends", "nominal_dividends"}:
        builders = [builders[8]]
    elif subskill_norm in {"appropriation", "appropriation-account", "appropriation_account"}:
        builders = [builders[9], builders[10], builders[11]]
    elif subskill_norm in {"appropriation-option1", "appropriation_option1", "appropriation-account-option1"}:
        builders = [builders[9]]
    elif subskill_norm in {"appropriation-option2", "appropriation_option2", "appropriation-account-option2"}:
        builders = [builders[10]]
    elif subskill_norm in {"appropriation-option3", "appropriation_option3", "appropriation-account-option3"}:
        builders = [builders[11]]
    elif subskill_norm in {"bundle", "workflow", "full"}:
        builders = [builders[12]]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        q = r.choice(builders)()
        if qtype_norm != "mixed" and str(q.get("question_type") or "").strip().lower() != qtype_norm:
            q2 = r.choice(builders)()
            if str(q2.get("question_type") or "").strip().lower() == qtype_norm:
                q = q2
        out.append(q)

    return out
