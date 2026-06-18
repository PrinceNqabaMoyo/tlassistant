from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from .column_help import headers_to_column_help
from .core import fmt_money, round_money
from .journal_question import make_journal
from .journal_table import build_prefixed_row, journal_editable_cols_by_difficulty
from .names import pick_business_name, pick_business_names, pick_person_names
from .schemas import CRJ_HEADERS, CJ_HEADERS, DJ_HEADERS, GJ_HEADERS


class _ScenarioValidationError(ValueError):
    pass


MAX_FULL_ACCOUNTING_CYCLE_GENERATION_ATTEMPTS = 8


def _cpj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Name of payee",
        "Fol",
        "Bank",
        "Trading stock",
        "Creditors control",
        "Discount received",
        "Debtors control (R/D)",
        "Wages",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def _caj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Creditor",
        "Fol",
        "Creditors’ Control",
        "Trading stock",
        "Stationery",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def _daj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Debtors",
        "Fol",
        "Debtors allowances",
        "Cost of sales",
    ]


def _pcj_headers() -> List[str]:
    return [
        "Doc",
        "Day",
        "Details",
        "Fol",
        "Petty cash",
        "Wages",
        "Stationery",
        "Trading stock",
        "Sundry amount",
        "Sundry fol",
        "Sundry details",
    ]


def _ledger_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Debit",
        "Credit",
        "Balance",
    ]


def _list_headers() -> List[str]:
    return [
        "Name",
        "Debit",
        "Credit",
    ]


SECTION_LABELS = {
    "balance_sheet": "Balance Sheet accounts",
    "nominal": "Nominal accounts",
}

TRIAL_BALANCE_FOLIOS = {
    "Capital": "B1",
    "Drawings": "B2",
    "Equipment": "B3",
    "Trading stock": "B4",
    "Debtors control": "B5",
    "Bank": "B6",
    "Petty cash": "B7",
    "Vehicles": "B8",
    "Creditors control": "B9",
    "Loan": "B10",
    "Sales": "N1",
    "Cost of sales": "N2",
    "Wages": "N3",
    "Stationery": "N4",
    "Debtors allowances": "N6",
    "Discount received": "N8",
    "Creditors allowances": "",
    "Discount allowed": "",
}

TRIAL_BALANCE_SECTIONS = {
    "Capital": "balance_sheet",
    "Drawings": "balance_sheet",
    "Equipment": "balance_sheet",
    "Vehicles": "balance_sheet",
    "Trading stock": "balance_sheet",
    "Debtors control": "balance_sheet",
    "Bank": "balance_sheet",
    "Petty cash": "balance_sheet",
    "Creditors control": "balance_sheet",
    "Loan": "balance_sheet",
    "Sales": "nominal",
    "Cost of sales": "nominal",
    "Wages": "nominal",
    "Stationery": "nominal",
    "Debtors allowances": "nominal",
    "Creditors allowances": "nominal",
    "Discount allowed": "nominal",
    "Discount received": "nominal",
}

TRIAL_BALANCE_ORDER = [
    "Capital",
    "Drawings",
    "Equipment",
    "Vehicles",
    "Creditors control",
    "Loan",
    "Debtors control",
    "Bank",
    "Petty cash",
    "Trading stock",
    "Sales",
    "Cost of sales",
    "Wages",
    "Stationery",
    "Debtors allowances",
    "Creditors allowances",
    "Discount allowed",
    "Discount received",
]

TRIAL_BALANCE_ACCOUNTS_BY_DIFFICULTY = {
    "easy": [
        "Capital",
        "Creditors control",
        "Debtors control",
        "Bank",
        "Trading stock",
        "Sales",
        "Cost of sales",
        "Wages",
        "Stationery",
        "Debtors allowances",
        "Discount allowed",
        "Discount received",
    ],
    "medium": [
        "Capital",
        "Drawings",
        "Creditors control",
        "Debtors control",
        "Bank",
        "Petty cash",
        "Trading stock",
        "Sales",
        "Cost of sales",
        "Wages",
        "Stationery",
        "Debtors allowances",
        "Creditors allowances",
        "Discount allowed",
        "Discount received",
    ],
    "hard": list(TRIAL_BALANCE_ORDER),
}


def _trial_balance_accounts_for_difficulty(difficulty: str) -> List[str]:
    difficulty_norm = str(difficulty or "easy").strip().lower()
    return list(TRIAL_BALANCE_ACCOUNTS_BY_DIFFICULTY.get(difficulty_norm, TRIAL_BALANCE_ACCOUNTS_BY_DIFFICULTY["easy"]))

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

TRANSACTION_FAMILY_GROUPS = {
    "crj": [
        "cash_sale",
        "debtor_receipt",
        "capital_contribution",
    ],
    "cpj": [
        "creditor_payment",
        "extra_wages_payment",
    ],
    "dj": [
        "credit_sale",
    ],
    "daj": [
        "debtor_allowance",
    ],
    "cj": [
        "credit_purchase",
        "credit_stationery_purchase",
    ],
    "caj": [
        "creditor_allowance",
    ],
    "pcj": [
        "petty_cash_stationery",
    ],
    "gj": [
        "gj_stationery_correction",
        "gj_wages_reclassification",
    ],
}

GENERAL_LEDGER_ACCOUNTS_BY_DIFFICULTY = {
    "easy": [
        "Bank",
        "Trading stock",
    ],
    "medium": [
        "Bank",
        "Trading stock",
        "Sales",
        "Wages",
        "Stationery",
        "Debtors control",
        "Creditors control",
    ],
    "hard": [
        "Bank",
        "Trading stock",
        "Sales",
        "Cost of sales",
        "Wages",
        "Stationery",
        "Capital",
        "Drawings",
        "Debtors control",
        "Creditors control",
    ],
}


def _general_ledger_accounts_for_difficulty(difficulty: str) -> List[str]:
    difficulty_norm = str(difficulty or "easy").strip().lower()
    return list(GENERAL_LEDGER_ACCOUNTS_BY_DIFFICULTY.get(difficulty_norm, GENERAL_LEDGER_ACCOUNTS_BY_DIFFICULTY["easy"]))


def _trial_balance_headers() -> List[str]:
    return [
        "Account",
        "Fol.",
        "Debit",
        "Credit",
    ]


def _general_ledger_account_headers() -> List[str]:
    return [
        "Month",
        "Day",
        "Details",
        "Fol",
        "Amount",
        "Month",
        "Day",
        "Details",
        "Fol",
        "Amount",
    ]


def _next_month(month: str) -> str:
    month_norm = str(month or "").strip()
    if month_norm not in MONTHS:
        return MONTHS[0]
    month_index = MONTHS.index(month_norm)
    return MONTHS[(month_index + 1) % len(MONTHS)]


def _month_label(month: str) -> str:
    return str(month or "")[:3]


def _month_end_day(month: str) -> int:
    if str(month) == "February":
        return 28
    if str(month) in {"April", "June", "September", "November"}:
        return 30
    return 31


def _project_transaction_count(*, difficulty: str, r: random.Random) -> int:
    difficulty_norm = str(difficulty or "easy").strip().lower()
    if difficulty_norm == "hard":
        return int(r.choice([18, 20, 22, 24, 26, 28]))
    if difficulty_norm == "medium":
        return int(r.choice([12, 13, 14, 15, 16, 18]))
    return int(r.choice([8, 9, 10, 10, 11, 12]))


def _build_project_days(*, month: str, total_transactions: int, difficulty: str, r: random.Random) -> List[int]:
    difficulty_norm = str(difficulty or "easy").strip().lower()
    if difficulty_norm == "hard":
        active_day_min, active_day_max = 16, 24
    elif difficulty_norm == "medium":
        active_day_min, active_day_max = 10, 16
    else:
        active_day_min, active_day_max = 6, 10

    day_limit = _month_end_day(month)
    max_active_days = max(1, min(int(total_transactions), int(day_limit), int(active_day_max)))
    min_active_days = max(1, min(int(active_day_min), int(max_active_days)))
    active_day_count = int(r.randint(min_active_days, max_active_days))
    active_days = sorted(r.sample(list(range(1, day_limit + 1)), k=active_day_count))

    scheduled_days = list(active_days)
    remaining_transactions = int(total_transactions) - len(scheduled_days)
    while remaining_transactions > 0:
        scheduled_days.append(int(r.choice(active_days)))
        remaining_transactions -= 1

    scheduled_days.sort()
    return scheduled_days


def _general_ledger_header_rows(*, business: str, account_name: str, folio: str, headers: List[str]) -> List[List[Dict[str, Any]]]:
    return [
        [{"label": f"General ledger of {business}", "colSpan": len(headers)}],
        [{"label": "Dr.", "colSpan": 1}, {"label": account_name, "colSpan": 8}, {"label": "Cr.", "colSpan": 1}],
        [{"label": "", "colSpan": 1}, {"label": folio, "colSpan": 8}, {"label": "", "colSpan": 1}],
    ]


def _allocate_list_balances(*, total: float, names: List[str], r: random.Random) -> Dict[str, float]:
    rounded_total = float(round_money(total))
    if not names:
        return {}
    if len(names) == 1:
        return {str(names[0]): rounded_total}
    unit = 50
    total_units = max(int(round(rounded_total / unit)), len(names))
    remaining_units = total_units
    min_other_units = 1
    other_count = len(names) - 1
    min_primary_units = max(total_units // 2, 1)
    max_primary_units = max(min_primary_units, total_units - (other_count * min_other_units))
    primary_units = int(r.randint(min_primary_units, max_primary_units))
    allocations = [primary_units]
    remaining_units -= primary_units
    for index in range(other_count - 1):
        max_units = remaining_units - ((other_count - index - 1) * min_other_units)
        units = int(r.randint(min_other_units, max_units))
        allocations.append(units)
        remaining_units -= units
    allocations.append(remaining_units)
    return {
        str(name): float(round_money(float(units * unit)))
        for name, units in zip(names, allocations)
    }


def _numbered_lines(lines: List[str]) -> str:
    return "\n".join(f"{index + 1}. {line}" for index, line in enumerate(lines))


def _build_general_ledger_rows(
    *,
    month: str,
    next_month: str,
    opening_side: str,
    opening_amount: float,
    debit_entries: List[Tuple[int, str, str, float]],
    credit_entries: List[Tuple[int, str, str, float]],
) -> List[List[Optional[str]]]:
    debit_rows: List[List[Optional[str]]] = []
    credit_rows: List[List[Optional[str]]] = []
    debit_total = 0.0
    credit_total = 0.0

    if str(opening_side) == "debit" and float(opening_amount):
        debit_rows.append([_month_label(month), "1", "Balance b/d", "b/d", _fmt(opening_amount)])
        debit_total = float(round_money(opening_amount))
    elif str(opening_side) == "credit" and float(opening_amount):
        credit_rows.append([_month_label(month), "1", "Balance b/d", "b/d", _fmt(opening_amount)])
        credit_total = float(round_money(opening_amount))

    for day, details, fol, amount in debit_entries:
        debit_rows.append([_month_label(month), str(day), details, fol, _fmt(amount)])
        debit_total = float(round_money(debit_total + amount))
    for day, details, fol, amount in credit_entries:
        credit_rows.append([_month_label(month), str(day), details, fol, _fmt(amount)])
        credit_total = float(round_money(credit_total + amount))

    if debit_total >= credit_total:
        balance = float(round_money(debit_total - credit_total))
        credit_rows.append([_month_label(month), str(_month_end_day(month)), "Balance c/d", "c/d", _fmt(balance)])
        total = float(round_money(debit_total))
        closing_side = "debit"
    else:
        balance = float(round_money(credit_total - debit_total))
        debit_rows.append([_month_label(month), str(_month_end_day(month)), "Balance c/d", "c/d", _fmt(balance)])
        total = float(round_money(credit_total))
        closing_side = "credit"

    rows: List[List[Optional[str]]] = []
    row_count = max(len(debit_rows), len(credit_rows))
    empty_side: List[Optional[str]] = ["", "", "", "", ""]
    for index in range(row_count):
        left = debit_rows[index] if index < len(debit_rows) else empty_side
        right = credit_rows[index] if index < len(credit_rows) else empty_side
        rows.append(list(left) + list(right))

    rows.append(["", "", "Totals", "", _fmt(total), "", "", "Totals", "", _fmt(total)])
    if closing_side == "debit":
        rows.append([_month_label(next_month), "1", "Balance b/d", "b/d", _fmt(balance), "", "", "", "", ""])
    else:
        rows.append(["", "", "", "", "", _month_label(next_month), "1", "Balance b/d", "b/d", _fmt(balance)])
    return rows


def _build_trial_balance_rows(entries: List[Dict[str, Any]]) -> List[List[Optional[str]]]:
    rows: List[List[Optional[str]]] = []
    current_section = ""
    debit_total = 0.0
    credit_total = 0.0

    def _sort_key(entry: Dict[str, Any]) -> Tuple[int, int, str]:
        name = str(entry.get("name") or "")
        section = str(entry.get("section") or "nominal")
        section_rank = 0 if section == "balance_sheet" else 1
        order_rank = TRIAL_BALANCE_ORDER.index(name) if name in TRIAL_BALANCE_ORDER else len(TRIAL_BALANCE_ORDER)
        return section_rank, order_rank, name

    for entry in sorted(entries, key=_sort_key):
        section = str(entry.get("section") or "nominal")
        if section != current_section:
            current_section = section
            rows.append([SECTION_LABELS[current_section], "", "", ""])
        debit_value = float(entry.get("debit") or 0.0)
        credit_value = float(entry.get("credit") or 0.0)
        rows.append([
            str(entry.get("name") or ""),
            str(entry.get("folio") or ""),
            _fmt(debit_value if debit_value else None),
            _fmt(credit_value if credit_value else None),
        ])
        debit_total = float(round_money(debit_total + debit_value))
        credit_total = float(round_money(credit_total + credit_value))

    rows.append(["Totals", "", _fmt(debit_total), _fmt(credit_total)])
    return rows


def _parse_money_text(value: Optional[str]) -> float:
    text = str(value or "").strip()
    if not text:
        return 0.0
    return float(round_money(float(text)))


def _general_ledger_closing_balance(rows: List[List[Optional[str]]]) -> Tuple[str, float]:
    if not rows:
        return "debit", 0.0
    last_row = list(rows[-1])
    debit_value = _parse_money_text(last_row[4] if len(last_row) > 4 else "")
    credit_value = _parse_money_text(last_row[9] if len(last_row) > 9 else "")
    if credit_value:
        return "credit", float(round_money(credit_value))
    return "debit", float(round_money(debit_value))


def _trial_balance_entry_balance_map(entries: List[Dict[str, Any]]) -> Dict[str, Tuple[str, float]]:
    balances: Dict[str, Tuple[str, float]] = {}
    for entry in entries:
        name = str(entry.get("name") or "")
        debit_value = float(round_money(float(entry.get("debit") or 0.0)))
        credit_value = float(round_money(float(entry.get("credit") or 0.0)))
        if debit_value and credit_value:
            raise _ScenarioValidationError(f"Trial Balance account {name} has values on both sides.")
        if debit_value:
            balances[name] = ("debit", debit_value)
        elif credit_value:
            balances[name] = ("credit", credit_value)
    return balances


def _trial_balance_totals_from_rows(rows: List[List[Optional[str]]]) -> Tuple[float, float]:
    if not rows:
        return 0.0, 0.0
    totals_row = list(rows[-1])
    return (
        float(round_money(_parse_money_text(totals_row[2] if len(totals_row) > 2 else ""))),
        float(round_money(_parse_money_text(totals_row[3] if len(totals_row) > 3 else ""))),
    )


def _set_correct(correct_map: Dict[str, Any], *, table_index: int, row_index: int, col_index: int, value: Any) -> None:
    correct_map[f"t{int(table_index)}_r{int(row_index)}_c{int(col_index)}"] = "" if value is None else str(value)


def _fmt(x: Optional[float]) -> str:
    return fmt_money(x) if x is not None else ""


def _make_table(
    *,
    table_index: int,
    journal_type: str,
    headers: List[str],
    rows_values: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    editable_base_cols: Optional[List[int]] = None,
    header_rows: Optional[List[List[Dict[str, Any]]]] = None,
    column_help: Optional[Dict[str, str]] = None,
    prefilled_cells: Optional[Dict[Tuple[int, int], str]] = None,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    show_answers = str(mode or "").strip().lower() == "scaffold"
    total_cols = len(headers)
    base = editable_base_cols if editable_base_cols is not None else list(range(total_cols))
    editable_cols = journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=base,
        total_cols=total_cols,
        mode=mode,
    )

    rows: List[List[Dict[str, Any]]] = []
    correct: Dict[str, Any] = {}
    for rix, vals in enumerate(rows_values):
        display_vals: List[Optional[str]]
        if show_answers:
            display_vals = vals
        else:
            display_vals = []
            for cix, _ in enumerate(vals):
                prefilled_value = (prefilled_cells or {}).get((rix, cix)) if prefilled_cells else None
                display_vals.append(prefilled_value if prefilled_value is not None else "")
        row_editable_cols = [c for c in editable_cols if (rix, c) not in (prefilled_cells or {})]
        rows.append(
            build_prefixed_row(
                table_index=table_index,
                row_index=rix,
                values=display_vals,
                editable_cols=row_editable_cols,
            )
        )
        for cix, v in enumerate(vals):
            _set_correct(correct, table_index=table_index, row_index=rix, col_index=cix, value="" if v is None else v)

    journal = {
        "journal_type": journal_type,
        "table_variant": "grade_project",
        "headers": headers,
        "rows": rows,
        "column_help": column_help or {},
        "allow_extra_rows": False,
    }
    if header_rows:
        journal["header_rows"] = header_rows
    return journal, correct


def _make_full_accounting_cycle_project_question_once(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    mode_norm = str(mode or "").strip().lower()
    difficulty_norm = str(difficulty or "easy").strip().lower()

    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    next_month = _next_month(month)
    year = int(r.choice([2024, 2025, 2026]))

    # Difficulty-scaled project size and date spread.
    n_tx = _project_transaction_count(difficulty=difficulty_norm, r=r)

    # Use a simple mark-up factor for cost-of-sales when needed.
    markup_pct = 50.0
    cost_factor = 1.0 / (1.0 + (markup_pct / 100.0))

    debtor_count = 3
    creditor_count = 2
    if difficulty_norm == "medium":
        debtor_count = 4
        creditor_count = 3
    elif difficulty_norm == "hard":
        debtor_count = 4
        creditor_count = 3

    debtors = pick_person_names(r=r, k=debtor_count)
    creditors = pick_business_names(r=r, k=creditor_count, unique_surnames=True)
    shared_counterparty = ""
    if difficulty_norm == "hard" and debtors and creditors:
        shared_counterparty = str(creditors[-1])
        debtors[-1] = shared_counterparty

    main_debtor = debtors[0]
    main_creditor = creditors[0]

    # Opening balances (difficulty-aware and still coherent)
    opening_bank = round_money(float(r.randrange(8000, 25001, 100)))
    opening_stock = round_money(float(r.randrange(6000, 20001, 100)))
    opening_debtors = round_money(float(r.randrange(2000, 12001, 50)))
    opening_creditors = round_money(float(r.randrange(2000, 12001, 50)))
    opening_drawings = 0.0
    opening_petty_cash = 0.0
    opening_equipment = 0.0
    opening_vehicles = 0.0
    opening_loan = 0.0
    opening_wages_balance = 0.0
    opening_stationery_balance = 0.0

    if difficulty_norm in {"medium", "hard"}:
        opening_drawings = float(round_money(float(r.randrange(500, 3001, 50))))
        opening_petty_cash = float(round_money(float(r.randrange(100, 801, 50))))
        opening_bank = float(round_money(opening_bank - opening_petty_cash))

    if difficulty_norm == "hard":
        opening_equipment = float(round_money(float(r.randrange(4000, 18001, 100))))
        opening_vehicles = float(round_money(float(r.randrange(5000, 22001, 100))))
        opening_loan = float(round_money(float(r.randrange(3000, 15001, 100))))
        opening_wages_balance = float(round_money(float(r.randrange(200, 1201, 50))))
        opening_stationery_balance = float(round_money(float(r.randrange(100, 701, 50))))

    opening_equity = round_money(
        (opening_bank + opening_stock + opening_debtors + opening_petty_cash + opening_equipment + opening_vehicles + opening_wages_balance + opening_stationery_balance)
        + opening_drawings
        - opening_creditors
        - opening_loan
    )
    opening_debtors_list = _allocate_list_balances(total=float(opening_debtors), names=debtors, r=r)
    opening_creditors_list = _allocate_list_balances(total=float(opening_creditors), names=creditors, r=r)

    bank = float(opening_bank)
    petty_cash = float(opening_petty_cash)
    stock = float(opening_stock)
    debtors_control = float(opening_debtors)
    creditors_control = float(opening_creditors)
    debtor_balances = dict(opening_debtors_list)
    creditor_balances = dict(opening_creditors_list)

    sales_total = 0.0
    cost_of_sales_total = 0.0
    debtors_allowances_total = 0.0
    creditors_allowances_total = 0.0
    wages_total = 0.0
    stationery_total = 0.0
    discount_allowed_total = 0.0
    discount_received_total = 0.0
    capital_contributions_total = 0.0

    # Build transaction days and refs
    days = _build_project_days(month=month, total_transactions=n_tx, difficulty=difficulty_norm, r=r)
    receipt_no = int(r.choice([150, 151, 152, 153, 154]))
    cheque_no = int(r.choice([310, 311, 312, 313, 314]))
    inv_no = int(r.choice([80, 88, 90, 101]))
    crn_no = int(r.choice([50, 56, 57]))
    dbn_no = int(r.choice([30, 35, 36, 37]))
    pcv_no = int(r.choice([80, 86, 87, 88]))
    transaction_lines: List[str] = []

    # Tables (values-only, then rendered via build_prefixed_row)
    crj_vals: List[List[Optional[str]]] = []
    cpj_vals: List[List[Optional[str]]] = []
    dj_vals: List[List[Optional[str]]] = []
    daj_vals: List[List[Optional[str]]] = []
    cj_vals: List[List[Optional[str]]] = []
    caj_vals: List[List[Optional[str]]] = []
    pcj_vals: List[List[Optional[str]]] = []
    gj_vals: List[List[Optional[str]]] = []
    debtors_movements: List[Tuple[str, str, float, float]] = []
    creditors_movements: List[Tuple[str, str, float, float]] = []
    debtor_movements_by_name: Dict[str, List[Tuple[str, str, float, float]]] = {str(name): [] for name in debtors}
    creditor_movements_by_name: Dict[str, List[Tuple[str, str, float, float]]] = {str(name): [] for name in creditors}
    bank_debit_entries: List[Tuple[int, str, str, float]] = []
    bank_credit_entries: List[Tuple[int, str, str, float]] = []
    stock_debit_entries: List[Tuple[int, str, str, float]] = []
    stock_credit_entries: List[Tuple[int, str, str, float]] = []
    general_ledger_targets = _general_ledger_accounts_for_difficulty(difficulty_norm)
    general_ledger_movements: Dict[str, Dict[str, Any]] = {
        "Bank": {"opening_side": "debit", "opening_amount": float(opening_bank), "debit_entries": [], "credit_entries": []},
        "Trading stock": {"opening_side": "debit", "opening_amount": float(opening_stock), "debit_entries": [], "credit_entries": []},
        "Sales": {"opening_side": "credit", "opening_amount": 0.0, "debit_entries": [], "credit_entries": []},
        "Cost of sales": {"opening_side": "debit", "opening_amount": 0.0, "debit_entries": [], "credit_entries": []},
        "Wages": {"opening_side": "debit", "opening_amount": float(opening_wages_balance), "debit_entries": [], "credit_entries": []},
        "Stationery": {"opening_side": "debit", "opening_amount": float(opening_stationery_balance), "debit_entries": [], "credit_entries": []},
        "Capital": {"opening_side": "credit", "opening_amount": float(opening_equity), "debit_entries": [], "credit_entries": []},
        "Drawings": {"opening_side": "debit", "opening_amount": float(opening_drawings), "debit_entries": [], "credit_entries": []},
        "Debtors control": {"opening_side": "debit", "opening_amount": float(opening_debtors), "debit_entries": [], "credit_entries": []},
        "Creditors control": {"opening_side": "credit", "opening_amount": float(opening_creditors), "debit_entries": [], "credit_entries": []},
    }

    def _gl_add(account: str, side: str, day: int, details: str, fol: str, amount: float) -> None:
        movement = general_ledger_movements.get(str(account))
        amount_value = float(round_money(amount))
        if movement is None or amount_value == 0.0:
            return
        if str(side) == "credit":
            movement["credit_entries"].append((int(day), str(details), str(fol), amount_value))
            return
        movement["debit_entries"].append((int(day), str(details), str(fol), amount_value))

    def _append_debtor_movement(name: str, dt: str, details: str, dr: float, cr: float) -> None:
        debtor_movements_by_name.setdefault(str(name), []).append((str(dt), str(details), float(dr), float(cr)))

    def _append_creditor_movement(name: str, dt: str, details: str, dr: float, cr: float) -> None:
        creditor_movements_by_name.setdefault(str(name), []).append((str(dt), str(details), float(dr), float(cr)))

    sale_amt = round_money(float(r.randrange(800, 4201, 50)))
    cost_amt = round_money(sale_amt * cost_factor)
    dj_vals.append([str(inv_no), str(days[0]), main_debtor, "", _fmt(sale_amt), _fmt(cost_amt)])
    transaction_lines.append(f"Invoice {inv_no}: Sold goods on credit to {main_debtor}, {fmt_money(sale_amt)}. Cost price of the goods sold, {fmt_money(cost_amt)}.")
    sales_total += sale_amt
    cost_of_sales_total += cost_amt
    debtors_control = float(round_money(debtors_control + sale_amt))
    debtor_balances[main_debtor] = float(round_money(float(debtor_balances.get(main_debtor, 0.0)) + sale_amt))
    stock = float(round_money(stock - cost_amt))
    _gl_add("Debtors control", "debit", int(days[0]), main_debtor, "DJ", sale_amt)
    _gl_add("Sales", "credit", int(days[0]), "Debtors control", "DJ", sale_amt)
    _gl_add("Cost of sales", "debit", int(days[0]), "Trading stock", "DJ", cost_amt)
    _gl_add("Trading stock", "credit", int(days[0]), "Cost of sales", "DJ", cost_amt)
    debtors_movements.append((f"{int(days[0]):02d} {_month_label(month)}", "Sales", sale_amt, 0.0))
    _append_debtor_movement(main_debtor, f"{int(days[0]):02d} {_month_label(month)}", "Sales", sale_amt, 0.0)
    stock_credit_entries.append((int(days[0]), "Cost of sales", "DJ", cost_amt))
    inv_no += 1

    # 2) Debtor pays with discount (CRJ)
    disc_allowed = round_money(float(r.randrange(20, 201, 10)))
    if disc_allowed >= sale_amt:
        disc_allowed = 0.0
    bank_in = round_money(sale_amt - disc_allowed)
    crj_vals.append([
        str(receipt_no),
        str(days[1]),
        main_debtor,
        "",
        "",
        _fmt(bank_in),
        "",
        "",
        _fmt(sale_amt),
        _fmt(disc_allowed),
        "",
        "",
        "",
    ])
    transaction_lines.append(f"Receipt {receipt_no}: Received {fmt_money(bank_in)} from {main_debtor} in settlement of account; discount allowed {fmt_money(disc_allowed)}.")
    receipt_no += 1
    bank = float(round_money(bank + bank_in))
    debtors_control = float(round_money(debtors_control - sale_amt))
    debtor_balances[main_debtor] = float(round_money(float(debtor_balances.get(main_debtor, 0.0)) - sale_amt))
    discount_allowed_total += disc_allowed
    _gl_add("Bank", "debit", int(days[1]), "Debtors control", "CRJ", bank_in)
    _gl_add("Debtors control", "credit", int(days[1]), main_debtor, "CRJ", sale_amt)
    debtors_movements.append((f"{int(days[1]):02d} {_month_label(month)}", "Receipt", 0.0, sale_amt))
    _append_debtor_movement(main_debtor, f"{int(days[1]):02d} {_month_label(month)}", "Receipt", 0.0, sale_amt)
    bank_debit_entries.append((int(days[1]), "Debtors control", "CRJ", bank_in))

    # 3) Credit purchase of stock (CJ)
    purch_amt = round_money(float(r.randrange(900, 5201, 50)))
    cj_vals.append([str(inv_no), str(days[2]), main_creditor, "", _fmt(purch_amt), _fmt(purch_amt), "", "", "", ""])
    transaction_lines.append(f"Invoice {inv_no}: Bought trading stock on credit from {main_creditor}, {fmt_money(purch_amt)}.")
    inv_no += 1
    creditors_control = float(round_money(creditors_control + purch_amt))
    creditor_balances[main_creditor] = float(round_money(float(creditor_balances.get(main_creditor, 0.0)) + purch_amt))
    stock = float(round_money(stock + purch_amt))
    _gl_add("Trading stock", "debit", int(days[2]), "Creditors control", "CJ", purch_amt)
    _gl_add("Creditors control", "credit", int(days[2]), main_creditor, "CJ", purch_amt)
    creditors_movements.append((f"{int(days[2]):02d} {_month_label(month)}", "Purchases", 0.0, purch_amt))
    _append_creditor_movement(main_creditor, f"{int(days[2]):02d} {_month_label(month)}", "Purchases", 0.0, purch_amt)
    stock_debit_entries.append((int(days[2]), "Creditors control", "CJ", purch_amt))

    # 4) Pay creditor with discount (CPJ)
    disc_received = round_money(float(r.randrange(20, 201, 10)))
    if disc_received >= purch_amt:
        disc_received = 0.0
    bank_out = round_money(purch_amt - disc_received)
    cpj_vals.append([
        str(cheque_no),
        str(days[3]),
        main_creditor,
        "",
        _fmt(bank_out),
        "",
        _fmt(purch_amt),
        _fmt(disc_received),
        "",
        "",
        "",
        "",
        "",
    ])
    transaction_lines.append(f"Cheque {cheque_no}: Paid {main_creditor}, {fmt_money(bank_out)} by cheque; discount received {fmt_money(disc_received)}.")
    cheque_no += 1
    bank = float(round_money(bank - bank_out))
    creditors_control = float(round_money(creditors_control - purch_amt))
    creditor_balances[main_creditor] = float(round_money(float(creditor_balances.get(main_creditor, 0.0)) - purch_amt))
    discount_received_total += disc_received
    _gl_add("Creditors control", "debit", int(days[3]), main_creditor, "CPJ", purch_amt)
    _gl_add("Bank", "credit", int(days[3]), "Creditors control", "CPJ", bank_out)
    creditors_movements.append((f"{int(days[3]):02d} {_month_label(month)}", "Payment", purch_amt, 0.0))
    _append_creditor_movement(main_creditor, f"{int(days[3]):02d} {_month_label(month)}", "Payment", purch_amt, 0.0)
    bank_credit_entries.append((int(days[3]), "Creditors control", "CPJ", bank_out))

    # 5) Debtors allowance (DAJ) with goods returned
    allow_amt = round_money(float(r.randrange(100, 801, 50)))
    allow_cost = round_money(allow_amt * cost_factor)
    daj_vals.append([str(crn_no), str(days[4]), main_debtor, "", _fmt(allow_amt), _fmt(allow_cost)])
    transaction_lines.append(f"Credit note {crn_no}: Granted an allowance to {main_debtor}, {fmt_money(allow_amt)}. Cost price of the returned goods, {fmt_money(allow_cost)}.")
    crn_no += 1
    debtors_allowances_total += allow_amt
    debtors_control = float(round_money(debtors_control - allow_amt))
    debtor_balances[main_debtor] = float(round_money(float(debtor_balances.get(main_debtor, 0.0)) - allow_amt))
    stock = float(round_money(stock + allow_cost))
    cost_of_sales_total = float(round_money(cost_of_sales_total - allow_cost))
    _gl_add("Debtors control", "credit", int(days[4]), main_debtor, "DAJ", allow_amt)
    _gl_add("Cost of sales", "credit", int(days[4]), "Trading stock", "DAJ", allow_cost)
    _gl_add("Trading stock", "debit", int(days[4]), "Cost of sales", "DAJ", allow_cost)
    debtors_movements.append((f"{int(days[4]):02d} {_month_label(month)}", "Allowances", 0.0, allow_amt))
    _append_debtor_movement(main_debtor, f"{int(days[4]):02d} {_month_label(month)}", "Allowances", 0.0, allow_amt)
    stock_debit_entries.append((int(days[4]), "Cost of sales", "DAJ", allow_cost))

    # 6) Creditors allowance (CAJ) with goods returned to creditor
    cred_allow = round_money(float(r.randrange(100, 801, 50)))
    caj_vals.append([str(dbn_no), str(days[5]), main_creditor, "", _fmt(cred_allow), _fmt(cred_allow), "", "", "", ""])
    transaction_lines.append(f"Debit note {dbn_no}: Returned goods to {main_creditor}, {fmt_money(cred_allow)}.")
    dbn_no += 1
    creditors_allowances_total += cred_allow
    creditors_control = float(round_money(creditors_control - cred_allow))
    creditor_balances[main_creditor] = float(round_money(float(creditor_balances.get(main_creditor, 0.0)) - cred_allow))
    stock = float(round_money(stock - cred_allow))
    _gl_add("Creditors control", "debit", int(days[5]), main_creditor, "CAJ", cred_allow)
    _gl_add("Trading stock", "credit", int(days[5]), "Creditors control", "CAJ", cred_allow)
    creditors_movements.append((f"{int(days[5]):02d} {_month_label(month)}", "Allowances", cred_allow, 0.0))
    _append_creditor_movement(main_creditor, f"{int(days[5]):02d} {_month_label(month)}", "Allowances", cred_allow, 0.0)
    stock_credit_entries.append((int(days[5]), "Creditors control", "CAJ", cred_allow))

    # 7) Pay wages (CPJ)
    wages = round_money(float(r.randrange(300, 2001, 50)))
    cpj_vals.append([
        str(cheque_no),
        str(days[6]),
        "Wages",
        "",
        _fmt(wages),
        "",
        "",
        "",
        "",
        _fmt(wages),
        "",
        "",
        "",
    ])
    transaction_lines.append(f"Cheque {cheque_no}: Paid wages, {fmt_money(wages)}.")
    cheque_no += 1
    bank = float(round_money(bank - wages))
    wages_total += wages
    _gl_add("Wages", "debit", int(days[6]), "Bank", "CPJ", wages)
    _gl_add("Bank", "credit", int(days[6]), "Wages", "CPJ", wages)
    bank_credit_entries.append((int(days[6]), "Wages", "CPJ", wages))

    # 8) Petty cash stationery (PCJ)
    if petty_cash >= 10.0:
        max_stationery = int(float(round_money(petty_cash)) // 10) * 10
        stationery_upper = min(300, max_stationery)
        if stationery_upper >= 50:
            stationery = round_money(float(r.randrange(50, stationery_upper + 1, 10)))
            pcj_vals.append([
                str(pcv_no),
                str(days[7]),
                "Stationery",
                "",
                _fmt(stationery),
                "",
                _fmt(stationery),
                "",
                "",
                "",
                "",
            ])
            transaction_lines.append(f"PCV {pcv_no}: Bought stationery from petty cash, {fmt_money(stationery)}.")
            pcv_no += 1
            petty_cash = float(round_money(petty_cash - stationery))
            stationery_total += stationery
            _gl_add("Stationery", "debit", int(days[7]), "Petty cash", "PCJ", stationery)

    # If we need more transactions, add a broader mix of realistic journal families.
    extra_days = days[8:]
    hard_seed_families: List[str] = []
    if difficulty_norm == "hard" and extra_days:
        if stock >= 100.0:
            hard_seed_families.append("gj_stationery_correction")
        elif stationery_total >= 100.0:
            hard_seed_families.append("gj_wages_reclassification")

        for candidate_family in [
            "credit_stationery_purchase",
            "credit_purchase",
            "creditor_payment" if any(float(creditor_balances.get(name, 0.0)) >= 150.0 for name in creditors) else "",
            "debtor_receipt" if any(float(debtor_balances.get(name, 0.0)) >= 150.0 for name in debtors) else "",
            "petty_cash_stationery",
        ]:
            if candidate_family and candidate_family not in hard_seed_families:
                hard_seed_families.append(candidate_family)
                break

    for extra_index, d in enumerate(extra_days):
        available_families = ["credit_sale", "cash_sale"]
        positive_debtors = [name for name in debtors if float(debtor_balances.get(name, 0.0)) >= 150.0]
        positive_creditors = [name for name in creditors if float(creditor_balances.get(name, 0.0)) >= 150.0]

        if difficulty_norm in {"medium", "hard"}:
            available_families.append("credit_purchase")
            available_families.append("capital_contribution")
            available_families.append("extra_wages_payment")
            if positive_debtors:
                available_families.append("debtor_receipt")
            if positive_creditors:
                available_families.append("creditor_payment")

        if difficulty_norm == "hard":
            available_families.append("credit_stationery_purchase")
            if stock >= 100.0:
                available_families.append("gj_stationery_correction")
            if stationery_total >= 100.0:
                available_families.append("gj_wages_reclassification")
            if positive_debtors:
                available_families.append("debtor_allowance")
            if positive_creditors:
                available_families.append("creditor_allowance")
            available_families.append("petty_cash_stationery")

        family_pool: List[str] = []
        for family_name in available_families:
            weight = 1
            if difficulty_norm == "easy":
                if family_name == "credit_sale":
                    weight = 3
                elif family_name == "cash_sale":
                    weight = 2
            elif difficulty_norm == "medium":
                if family_name in {"credit_sale", "cash_sale", "credit_purchase", "debtor_receipt", "creditor_payment", "extra_wages_payment"}:
                    weight = 2
                elif family_name == "capital_contribution":
                    weight = 1
            else:
                if family_name in {"credit_sale", "cash_sale"}:
                    weight = 1
                elif family_name in {
                    "credit_purchase",
                    "capital_contribution",
                    "debtor_receipt",
                    "creditor_payment",
                    "extra_wages_payment",
                    "credit_stationery_purchase",
                    "gj_stationery_correction",
                    "gj_wages_reclassification",
                    "debtor_allowance",
                    "creditor_allowance",
                    "petty_cash_stationery",
                }:
                    weight = 2
            family_pool.extend([family_name] * weight)

        seeded_family = hard_seed_families[extra_index] if extra_index < len(hard_seed_families) else ""
        if seeded_family and seeded_family in available_families:
            family = seeded_family
        else:
            family = str(r.choice(family_pool or available_families))

        if family == "credit_sale":
            amt = round_money(float(r.randrange(600, 3201, 50)))
            cost = round_money(amt * cost_factor)
            debtor = r.choice(debtors)
            dj_vals.append([str(inv_no), str(d), debtor, "", _fmt(amt), _fmt(cost)])
            transaction_lines.append(f"Invoice {inv_no}: Sold goods on credit to {debtor}, {fmt_money(amt)}. Cost price of the goods sold, {fmt_money(cost)}.")
            inv_no += 1
            sales_total += amt
            cost_of_sales_total += cost
            debtors_control = float(round_money(debtors_control + amt))
            debtor_balances[debtor] = float(round_money(float(debtor_balances.get(debtor, 0.0)) + amt))
            stock = float(round_money(stock - cost))
            _gl_add("Debtors control", "debit", int(d), debtor, "DJ", amt)
            _gl_add("Sales", "credit", int(d), "Debtors control", "DJ", amt)
            _gl_add("Cost of sales", "debit", int(d), "Trading stock", "DJ", cost)
            _gl_add("Trading stock", "credit", int(d), "Cost of sales", "DJ", cost)
            _append_debtor_movement(debtor, f"{int(d):02d} {_month_label(month)}", "Sales", amt, 0.0)
            if debtor == main_debtor:
                debtors_movements.append((f"{int(d):02d} {_month_label(month)}", "Sales", amt, 0.0))
            stock_credit_entries.append((int(d), "Cost of sales", "DJ", cost))
        elif family == "cash_sale":
            amt = round_money(float(r.randrange(500, 2501, 50)))
            cost = round_money(amt * cost_factor)
            crj_vals.append([
                "CRR",
                str(d),
                "Cash sales",
                "",
                "",
                _fmt(amt),
                _fmt(amt),
                _fmt(cost),
                "",
                "",
                "",
                "",
                "",
            ])
            transaction_lines.append(f"Cash receipt register {d}: Cash sales, {fmt_money(amt)}. Cost price of the goods sold, {fmt_money(cost)}.")
            bank = float(round_money(bank + amt))
            sales_total += amt
            cost_of_sales_total += float(cost)
            stock = float(round_money(stock - cost))
            _gl_add("Bank", "debit", int(d), "Sales", "CRJ", amt)
            _gl_add("Sales", "credit", int(d), "Bank", "CRJ", amt)
            _gl_add("Cost of sales", "debit", int(d), "Trading stock", "CRJ", float(cost))
            _gl_add("Trading stock", "credit", int(d), "Cost of sales", "CRJ", float(cost))
            bank_debit_entries.append((int(d), "Sales", "CRJ", amt))
            stock_credit_entries.append((int(d), "Cost of sales", "CRJ", float(cost)))
        elif family == "debtor_receipt":
            debtor = r.choice(positive_debtors)
            gross_receipt = round_money(min(float(debtor_balances.get(debtor, 0.0)), float(r.randrange(200, 2201, 50))))
            discount = round_money(min(float(r.randrange(0, 151, 10)), max(0.0, gross_receipt - 50.0)))
            bank_in = round_money(gross_receipt - discount)
            crj_vals.append([
                str(receipt_no),
                str(d),
                debtor,
                "",
                "",
                _fmt(bank_in),
                "",
                "",
                _fmt(gross_receipt),
                _fmt(discount),
                "",
                "",
                "",
            ])
            transaction_lines.append(f"Receipt {receipt_no}: Received {fmt_money(bank_in)} from {debtor} in settlement of account; discount allowed {fmt_money(discount)}.")
            receipt_no += 1
            bank = float(round_money(bank + bank_in))
            debtors_control = float(round_money(debtors_control - gross_receipt))
            debtor_balances[debtor] = float(round_money(float(debtor_balances.get(debtor, 0.0)) - gross_receipt))
            discount_allowed_total += discount
            _gl_add("Bank", "debit", int(d), "Debtors control", "CRJ", bank_in)
            _gl_add("Debtors control", "credit", int(d), debtor, "CRJ", gross_receipt)
            _append_debtor_movement(debtor, f"{int(d):02d} {_month_label(month)}", "Receipt", 0.0, gross_receipt)
            if debtor == main_debtor:
                debtors_movements.append((f"{int(d):02d} {_month_label(month)}", "Receipt", 0.0, gross_receipt))
            bank_debit_entries.append((int(d), "Debtors control", "CRJ", bank_in))
        elif family == "credit_purchase":
            creditor = r.choice(creditors)
            extra_purch_amt = round_money(float(r.randrange(700, 3601, 50)))
            cj_vals.append([str(inv_no), str(d), creditor, "", _fmt(extra_purch_amt), _fmt(extra_purch_amt), "", "", "", ""])
            transaction_lines.append(f"Invoice {inv_no}: Bought trading stock on credit from {creditor}, {fmt_money(extra_purch_amt)}.")
            inv_no += 1
            creditors_control = float(round_money(creditors_control + extra_purch_amt))
            creditor_balances[creditor] = float(round_money(float(creditor_balances.get(creditor, 0.0)) + extra_purch_amt))
            stock = float(round_money(stock + extra_purch_amt))
            _gl_add("Trading stock", "debit", int(d), "Creditors control", "CJ", extra_purch_amt)
            _gl_add("Creditors control", "credit", int(d), creditor, "CJ", extra_purch_amt)
            _append_creditor_movement(creditor, f"{int(d):02d} {_month_label(month)}", "Purchases", 0.0, extra_purch_amt)
            if creditor == main_creditor:
                creditors_movements.append((f"{int(d):02d} {_month_label(month)}", "Purchases", 0.0, extra_purch_amt))
            stock_debit_entries.append((int(d), "Creditors control", "CJ", extra_purch_amt))
        elif family == "capital_contribution":
            capital_amt = round_money(float(r.randrange(1000, 6001, 100)))
            crj_vals.append([
                str(receipt_no),
                str(d),
                "Capital",
                "",
                "",
                _fmt(capital_amt),
                "",
                "",
                "",
                "",
                _fmt(capital_amt),
                TRIAL_BALANCE_FOLIOS["Capital"],
                "Capital contribution",
            ])
            transaction_lines.append(f"Receipt {receipt_no}: The owner contributed additional capital of {fmt_money(capital_amt)}.")
            receipt_no += 1
            bank = float(round_money(bank + capital_amt))
            capital_contributions_total = float(round_money(capital_contributions_total + capital_amt))
            _gl_add("Bank", "debit", int(d), "Capital", "CRJ", capital_amt)
            _gl_add("Capital", "credit", int(d), "Bank", "CRJ", capital_amt)
            bank_debit_entries.append((int(d), "Capital", "CRJ", capital_amt))
        elif family == "extra_wages_payment":
            extra_wages = round_money(float(r.randrange(250, 1801, 50)))
            cpj_vals.append([
                str(cheque_no),
                str(d),
                "Wages",
                "",
                _fmt(extra_wages),
                "",
                "",
                "",
                "",
                _fmt(extra_wages),
                "",
                "",
                "",
            ])
            transaction_lines.append(f"Cheque {cheque_no}: Paid additional wages, {fmt_money(extra_wages)}.")
            cheque_no += 1
            bank = float(round_money(bank - extra_wages))
            wages_total += extra_wages
            _gl_add("Wages", "debit", int(d), "Bank", "CPJ", extra_wages)
            _gl_add("Bank", "credit", int(d), "Wages", "CPJ", extra_wages)
            bank_credit_entries.append((int(d), "Wages", "CPJ", extra_wages))
        elif family == "creditor_payment":
            creditor = r.choice(positive_creditors)
            gross_payment = round_money(min(float(creditor_balances.get(creditor, 0.0)), float(r.randrange(200, 2601, 50))))
            discount = round_money(min(float(r.randrange(0, 151, 10)), max(0.0, gross_payment - 50.0)))
            bank_out = round_money(gross_payment - discount)
            cpj_vals.append([
                str(cheque_no),
                str(d),
                creditor,
                "",
                _fmt(bank_out),
                "",
                _fmt(gross_payment),
                _fmt(discount),
                "",
                "",
                "",
                "",
                "",
            ])
            transaction_lines.append(f"Cheque {cheque_no}: Paid {creditor}, {fmt_money(bank_out)} by cheque; discount received {fmt_money(discount)}.")
            cheque_no += 1
            bank = float(round_money(bank - bank_out))
            creditors_control = float(round_money(creditors_control - gross_payment))
            creditor_balances[creditor] = float(round_money(float(creditor_balances.get(creditor, 0.0)) - gross_payment))
            discount_received_total += discount
            _gl_add("Creditors control", "debit", int(d), creditor, "CPJ", gross_payment)
            _gl_add("Bank", "credit", int(d), "Creditors control", "CPJ", bank_out)
            _append_creditor_movement(creditor, f"{int(d):02d} {_month_label(month)}", "Payment", gross_payment, 0.0)
            if creditor == main_creditor:
                creditors_movements.append((f"{int(d):02d} {_month_label(month)}", "Payment", gross_payment, 0.0))
            bank_credit_entries.append((int(d), "Creditors control", "CPJ", bank_out))
        elif family == "debtor_allowance":
            debtor = r.choice(positive_debtors)
            allow_amt = round_money(min(float(debtor_balances.get(debtor, 0.0)), float(r.randrange(100, 701, 50))))
            allow_cost = round_money(allow_amt * cost_factor)
            daj_vals.append([str(crn_no), str(d), debtor, "", _fmt(allow_amt), _fmt(allow_cost)])
            transaction_lines.append(f"Credit note {crn_no}: Granted an allowance to {debtor}, {fmt_money(allow_amt)}. Cost price of the returned goods, {fmt_money(allow_cost)}.")
            crn_no += 1
            debtors_allowances_total += allow_amt
            debtors_control = float(round_money(debtors_control - allow_amt))
            debtor_balances[debtor] = float(round_money(float(debtor_balances.get(debtor, 0.0)) - allow_amt))
            stock = float(round_money(stock + allow_cost))
            cost_of_sales_total = float(round_money(cost_of_sales_total - allow_cost))
            _gl_add("Debtors control", "credit", int(d), debtor, "DAJ", allow_amt)
            _gl_add("Cost of sales", "credit", int(d), "Trading stock", "DAJ", allow_cost)
            _gl_add("Trading stock", "debit", int(d), "Cost of sales", "DAJ", allow_cost)
            _append_debtor_movement(debtor, f"{int(d):02d} {_month_label(month)}", "Allowances", 0.0, allow_amt)
            if debtor == main_debtor:
                debtors_movements.append((f"{int(d):02d} {_month_label(month)}", "Allowances", 0.0, allow_amt))
            stock_debit_entries.append((int(d), "Cost of sales", "DAJ", allow_cost))
        elif family == "credit_stationery_purchase":
            creditor = r.choice(creditors)
            stationery_credit_amt = round_money(float(r.randrange(100, 901, 50)))
            cj_vals.append([str(inv_no), str(d), creditor, "", _fmt(stationery_credit_amt), "", _fmt(stationery_credit_amt), "", "", ""])
            transaction_lines.append(f"Invoice {inv_no}: Bought stationery on credit from {creditor}, {fmt_money(stationery_credit_amt)}.")
            inv_no += 1
            creditors_control = float(round_money(creditors_control + stationery_credit_amt))
            creditor_balances[creditor] = float(round_money(float(creditor_balances.get(creditor, 0.0)) + stationery_credit_amt))
            stationery_total += stationery_credit_amt
            _gl_add("Stationery", "debit", int(d), "Creditors control", "CJ", stationery_credit_amt)
            _gl_add("Creditors control", "credit", int(d), creditor, "CJ", stationery_credit_amt)
            _append_creditor_movement(creditor, f"{int(d):02d} {_month_label(month)}", "Stationery", 0.0, stationery_credit_amt)
            if creditor == main_creditor:
                creditors_movements.append((f"{int(d):02d} {_month_label(month)}", "Stationery", 0.0, stationery_credit_amt))
        elif family == "gj_stationery_correction":
            correction_amt = round_money(min(float(stock), float(r.randrange(100, 701, 50))))
            gj_vals.append([str(d), "Stationery", TRIAL_BALANCE_FOLIOS.get("Stationery", ""), _fmt(correction_amt), "", "", "", "", ""])
            gj_vals.append([str(d), "Trading stock", TRIAL_BALANCE_FOLIOS.get("Trading stock", ""), "", _fmt(correction_amt), "", "", "", ""])
            transaction_lines.append(f"General Journal adjustment on {d}: Stationery bought was wrongly posted to Trading stock. Correct the error, {fmt_money(correction_amt)}.")
            stationery_total += correction_amt
            stock = float(round_money(stock - correction_amt))
            _gl_add("Stationery", "debit", int(d), "Trading stock", "GJ", correction_amt)
            _gl_add("Trading stock", "credit", int(d), "Stationery", "GJ", correction_amt)
            stock_credit_entries.append((int(d), "Stationery correction", "GJ", correction_amt))
        elif family == "gj_wages_reclassification":
            correction_amt = round_money(min(float(stationery_total), float(r.randrange(100, 601, 50))))
            gj_vals.append([str(d), "Wages", TRIAL_BALANCE_FOLIOS.get("Wages", ""), _fmt(correction_amt), "", "", "", "", ""])
            gj_vals.append([str(d), "Stationery", TRIAL_BALANCE_FOLIOS.get("Stationery", ""), "", _fmt(correction_amt), "", "", "", ""])
            transaction_lines.append(f"General Journal adjustment on {d}: Wages were wrongly posted to Stationery. Correct the error, {fmt_money(correction_amt)}.")
            wages_total += correction_amt
            stationery_total = float(round_money(stationery_total - correction_amt))
            _gl_add("Wages", "debit", int(d), "Stationery", "GJ", correction_amt)
            _gl_add("Stationery", "credit", int(d), "Wages", "GJ", correction_amt)
        elif family == "creditor_allowance":
            creditor = r.choice(positive_creditors)
            cred_allow = round_money(min(float(creditor_balances.get(creditor, 0.0)), float(r.randrange(100, 701, 50))))
            caj_vals.append([str(dbn_no), str(d), creditor, "", _fmt(cred_allow), _fmt(cred_allow), "", "", "", ""])
            transaction_lines.append(f"Debit note {dbn_no}: Returned goods to {creditor}, {fmt_money(cred_allow)}.")
            dbn_no += 1
            creditors_allowances_total += cred_allow
            creditors_control = float(round_money(creditors_control - cred_allow))
            creditor_balances[creditor] = float(round_money(float(creditor_balances.get(creditor, 0.0)) - cred_allow))
            stock = float(round_money(stock - cred_allow))
            _gl_add("Creditors control", "debit", int(d), creditor, "CAJ", cred_allow)
            _gl_add("Trading stock", "credit", int(d), "Creditors control", "CAJ", cred_allow)
            _append_creditor_movement(creditor, f"{int(d):02d} {_month_label(month)}", "Allowances", cred_allow, 0.0)
            if creditor == main_creditor:
                creditors_movements.append((f"{int(d):02d} {_month_label(month)}", "Allowances", cred_allow, 0.0))
            stock_credit_entries.append((int(d), "Creditors control", "CAJ", cred_allow))
        else:
            if petty_cash >= 10.0:
                max_extra_stationery = int(float(round_money(petty_cash)) // 10) * 10
                stationery_upper = min(240, max_extra_stationery)
                if stationery_upper >= 40:
                    extra_stationery = round_money(float(r.randrange(40, stationery_upper + 1, 10)))
                    pcj_vals.append([
                        str(pcv_no),
                        str(d),
                        "Stationery",
                        "",
                        _fmt(extra_stationery),
                        "",
                        _fmt(extra_stationery),
                        "",
                        "",
                        "",
                        "",
                    ])
                    transaction_lines.append(f"PCV {pcv_no}: Bought stationery from petty cash, {fmt_money(extra_stationery)}.")
                    pcv_no += 1
                    petty_cash = float(round_money(petty_cash - extra_stationery))
                    stationery_total += extra_stationery
                    _gl_add("Stationery", "debit", int(d), "Petty cash", "PCJ", extra_stationery)

    # Debtors/Creditors lists (simple: main balances + two others)
    debtors_list: Dict[str, Tuple[float, float]] = {}
    for nm in debtors:
        balance = float(round_money(float(debtor_balances.get(nm, 0.0))))
        if balance >= 0.0:
            debtors_list[nm] = (balance, 0.0)
        else:
            debtors_list[nm] = (0.0, float(round_money(abs(balance))))

    creditors_list: Dict[str, Tuple[float, float]] = {}
    for nm in creditors:
        balance = float(round_money(float(creditor_balances.get(nm, 0.0))))
        if balance >= 0.0:
            creditors_list[nm] = (0.0, balance)
        else:
            creditors_list[nm] = (float(round_money(abs(balance))), 0.0)

    debtors_control = float(round_money(sum(float(values[0]) - float(values[1]) for values in debtors_list.values())))
    creditors_control = float(round_money(sum(float(values[1]) - float(values[0]) for values in creditors_list.values())))
    if debtors_control != float(round_money(sum(float(debtor_balances.get(nm, 0.0)) for nm in debtors))):
        raise _ScenarioValidationError("Debtors list does not reconcile to Debtors control.")
    if creditors_control != float(round_money(sum(float(creditor_balances.get(nm, 0.0)) for nm in creditors))):
        raise _ScenarioValidationError("Creditors list does not reconcile to Creditors control.")

    # Ledger tables (running balance, simplified)
    def _make_ledger_rows(*, opening: float, name: str, movements: List[Tuple[str, str, float, float]]) -> List[List[Optional[str]]]:
        bal = float(opening)
        out_rows: List[List[Optional[str]]] = []
        out_rows.append([f"01 {month[:3]}", "Balance b/d", "b/d", _fmt(opening if opening > 0 else None), _fmt(-opening if opening < 0 else None), _fmt(abs(opening))])
        for dt, details, dr, cr in movements:
            bal = float(round_money(bal + dr - cr))
            out_rows.append([dt, details, "", _fmt(dr if dr else None), _fmt(cr if cr else None), _fmt(abs(bal))])
        return out_rows

    debtors_movements = sorted(debtors_movements, key=lambda item: item[0])
    creditors_movements = sorted(creditors_movements, key=lambda item: item[0])
    for name in list(debtor_movements_by_name.keys()):
        debtor_movements_by_name[name] = sorted(list(debtor_movements_by_name.get(name) or []), key=lambda item: item[0])
    for name in list(creditor_movements_by_name.keys()):
        creditor_movements_by_name[name] = sorted(list(creditor_movements_by_name.get(name) or []), key=lambda item: item[0])

    displayed_debtor_name = max(
        debtors,
        key=lambda nm: (len(debtor_movements_by_name.get(str(nm), [])), float(abs(debtor_balances.get(str(nm), 0.0))), str(nm)),
    )
    displayed_creditor_name = max(
        creditors,
        key=lambda nm: (len(creditor_movements_by_name.get(str(nm), [])), float(abs(creditor_balances.get(str(nm), 0.0))), str(nm)),
    )

    debtors_ledger_rows = _make_ledger_rows(
        opening=float(opening_debtors_list[displayed_debtor_name]),
        name=displayed_debtor_name,
        movements=list(debtor_movements_by_name.get(str(displayed_debtor_name), [])),
    )
    creditors_ledger_rows = _make_ledger_rows(
        opening=-float(opening_creditors_list[displayed_creditor_name]),
        name=displayed_creditor_name,
        movements=list(creditor_movements_by_name.get(str(displayed_creditor_name), [])),
    )
    general_ledger_rows_by_account: Dict[str, List[List[Optional[str]]]] = {}
    for account_name in general_ledger_targets:
        movement = general_ledger_movements.get(account_name)
        if movement is None:
            continue
        opening_amount = float(movement.get("opening_amount") or 0.0)
        debit_entries = sorted(list(movement.get("debit_entries") or []), key=lambda item: item[0])
        credit_entries = sorted(list(movement.get("credit_entries") or []), key=lambda item: item[0])
        if opening_amount == 0.0 and not debit_entries and not credit_entries:
            continue
        general_ledger_rows_by_account[account_name] = _build_general_ledger_rows(
            month=month,
            next_month=next_month,
            opening_side=str(movement.get("opening_side") or "debit"),
            opening_amount=opening_amount,
            debit_entries=debit_entries,
            credit_entries=credit_entries,
        )

    # Trial balance (kept balancing by computing equity as residual at end)
    closing_bank = round_money(bank)
    closing_stock = round_money(stock)
    closing_debtors = round_money(debtors_control)
    closing_creditors = round_money(creditors_control)
    closing_drawings = round_money(opening_drawings)
    closing_petty_cash = round_money(petty_cash)
    closing_equipment = round_money(opening_equipment)
    closing_vehicles = round_money(opening_vehicles)
    closing_loan = round_money(opening_loan)

    # Expense balances
    wages_bal = round_money(opening_wages_balance + wages_total)
    stationery_bal = round_money(opening_stationery_balance + stationery_total)

    # Income and contra-income
    sales_bal = round_money(sales_total)
    cos_bal = round_money(cost_of_sales_total)
    debtors_allow_bal = round_money(debtors_allowances_total)
    disc_allowed_bal = round_money(discount_allowed_total)
    disc_received_bal = round_money(discount_received_total)

    closing_capital = round_money(opening_equity + capital_contributions_total)

    tb_entries: List[Dict[str, Any]] = []
    allowed_tb_accounts = set(_trial_balance_accounts_for_difficulty(difficulty_norm))

    def _tb_add(name: str, dr: Optional[float], cr: Optional[float]) -> None:
        if str(name) not in allowed_tb_accounts:
            return
        amount_dr = float(round_money(float(dr))) if dr is not None else 0.0
        amount_cr = float(round_money(float(cr))) if cr is not None else 0.0
        if amount_dr == 0.0 and amount_cr == 0.0:
            return
        tb_entries.append(
            {
                "name": name,
                "folio": TRIAL_BALANCE_FOLIOS.get(name, ""),
                "section": TRIAL_BALANCE_SECTIONS.get(name, "nominal"),
                "debit": amount_dr,
                "credit": amount_cr,
            }
        )

    _tb_add("Capital", None, float(closing_capital))
    _tb_add("Drawings", float(closing_drawings), None)
    _tb_add("Equipment", float(closing_equipment), None)
    _tb_add("Vehicles", float(closing_vehicles), None)
    _tb_add("Creditors control", None, float(closing_creditors))
    _tb_add("Loan", None, float(closing_loan))
    _tb_add("Debtors control", float(closing_debtors), None)
    _tb_add("Bank", float(closing_bank), None)
    _tb_add("Petty cash", float(closing_petty_cash), None)
    _tb_add("Trading stock", float(closing_stock), None)
    _tb_add("Sales", None, float(sales_bal))
    _tb_add("Cost of sales", float(cos_bal), None)
    _tb_add("Wages", float(wages_bal), None)
    _tb_add("Stationery", float(stationery_bal), None)
    _tb_add("Debtors allowances", float(debtors_allow_bal), None)
    _tb_add("Discount allowed", float(disc_allowed_bal), None)
    _tb_add("Discount received", None, float(disc_received_bal))
    tb_balance_map = _trial_balance_entry_balance_map(tb_entries)
    expected_general_ledger_balances: Dict[str, Tuple[str, float]] = {
        "Bank": ("debit", float(closing_bank)),
        "Trading stock": ("debit", float(closing_stock)),
        "Sales": ("credit", float(sales_bal)),
        "Cost of sales": ("debit", float(cos_bal)),
        "Wages": ("debit", float(wages_bal)),
        "Stationery": ("debit", float(stationery_bal)),
        "Capital": ("credit", float(closing_capital)),
        "Drawings": ("debit", float(closing_drawings)),
        "Debtors control": ("debit", float(closing_debtors)),
        "Creditors control": ("credit", float(closing_creditors)),
    }
    for account_name, rows_values in general_ledger_rows_by_account.items():
        ledger_side, ledger_amount = _general_ledger_closing_balance(rows_values)
        expected_side, expected_amount = expected_general_ledger_balances.get(account_name, (ledger_side, ledger_amount))
        expected_amount = float(round_money(expected_amount))
        if ledger_side != expected_side or float(round_money(ledger_amount)) != expected_amount:
            raise _ScenarioValidationError(f"General Ledger balance mismatch for {account_name}.")
        trial_balance_side_amount = tb_balance_map.get(account_name)
        if expected_amount == 0.0:
            if trial_balance_side_amount is not None:
                raise _ScenarioValidationError(f"Zero-balance account {account_name} leaked into the Trial Balance.")
            continue
        if trial_balance_side_amount is None:
            raise _ScenarioValidationError(f"Trial Balance is missing {account_name}.")
        if trial_balance_side_amount[0] != expected_side or float(round_money(trial_balance_side_amount[1])) != expected_amount:
            raise _ScenarioValidationError(f"Trial Balance balance mismatch for {account_name}.")
    tb_rows = _build_trial_balance_rows(tb_entries)
    tb_debit_total = float(round_money(sum(float(entry.get("debit") or 0.0) for entry in tb_entries)))
    tb_credit_total = float(round_money(sum(float(entry.get("credit") or 0.0) for entry in tb_entries)))
    if tb_debit_total != tb_credit_total:
        tb_snapshot = "; ".join(
            f"{str(entry.get('name') or '')}: {'Dr' if float(entry.get('debit') or 0.0) else 'Cr'} {float(round_money(float(entry.get('debit') or entry.get('credit') or 0.0))):.2f}"
            for entry in tb_entries
        )
        raise _ScenarioValidationError(
            f"Final Trial Balance does not balance. Debit={tb_debit_total:.2f}, Credit={tb_credit_total:.2f}. Entries={tb_snapshot}"
        )
    row_debit_total, row_credit_total = _trial_balance_totals_from_rows(tb_rows)
    if row_debit_total != tb_debit_total or row_credit_total != tb_credit_total:
        raise _ScenarioValidationError("Rendered Trial Balance totals do not match calculated totals.")
    tb_prefilled_cells: Dict[Tuple[int, int], str] = {}
    if tb_rows:
        totals_row_index = len(tb_rows) - 1
        if difficulty_norm == "easy" or (difficulty_norm == "medium" and bool(r.choice([True, False]))):
            tb_prefilled_cells[(totals_row_index, 2)] = str(tb_rows[totals_row_index][2] or "")
            tb_prefilled_cells[(totals_row_index, 3)] = str(tb_rows[totals_row_index][3] or "")

    # Render tables
    journals: List[Dict[str, Any]] = []
    correct_map: Dict[str, Any] = {}

    t = 0
    j, c = _make_table(table_index=t, journal_type="crj", headers=list(CRJ_HEADERS), rows_values=crj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="cpj", headers=_cpj_headers(), rows_values=cpj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="dj", headers=list(DJ_HEADERS), rows_values=dj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="daj", headers=_daj_headers(), rows_values=daj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="cj", headers=list(CJ_HEADERS), rows_values=cj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="caj", headers=_caj_headers(), rows_values=caj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    j, c = _make_table(table_index=t, journal_type="pcj", headers=_pcj_headers(), rows_values=pcj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    gj_index = t
    j, c = _make_table(table_index=t, journal_type="gj", headers=list(GJ_HEADERS), rows_values=gj_vals, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    general_ledger_table_indices: Dict[str, int] = {}
    for account_name in general_ledger_targets:
        rows_values = general_ledger_rows_by_account.get(account_name)
        if not rows_values:
            continue
        t += 1
        general_ledger_table_indices[account_name] = t
        j, c = _make_table(
            table_index=t,
            journal_type="general_ledger",
            headers=_general_ledger_account_headers(),
            rows_values=rows_values,
            difficulty=difficulty,
            mode=mode_norm,
            header_rows=_general_ledger_header_rows(
                business=business,
                account_name=account_name,
                folio=TRIAL_BALANCE_FOLIOS.get(account_name, ""),
                headers=_general_ledger_account_headers(),
            ),
        )
        journals.append(j)
        correct_map.update(c)

    bank_gl_index = int(general_ledger_table_indices.get("Bank", -1))
    stock_gl_index = int(general_ledger_table_indices.get("Trading stock", -1))
    sales_gl_index = int(general_ledger_table_indices.get("Sales", -1))
    debtors_control_gl_index = int(general_ledger_table_indices.get("Debtors control", -1))
    creditors_control_gl_index = int(general_ledger_table_indices.get("Creditors control", -1))

    t += 1
    # Debtors ledger
    debt_ledger_index = t
    j, c = _make_table(table_index=t, journal_type="debtors_ledger", headers=_ledger_headers(), rows_values=debtors_ledger_rows, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    # Creditors ledger
    cred_ledger_index = t
    j, c = _make_table(table_index=t, journal_type="creditors_ledger", headers=_ledger_headers(), rows_values=creditors_ledger_rows, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    # Debtors list
    debt_rows: List[List[Optional[str]]] = []
    for nm in debtors:
        dr, cr = debtors_list[nm]
        debt_rows.append([nm, _fmt(dr) if dr else "", _fmt(cr) if cr else ""])
    debt_rows.append(["TOTAL", _fmt(sum(float(values[0]) for values in debtors_list.values())), _fmt(sum(float(values[1]) for values in debtors_list.values()))])
    debt_list_index = t
    j, c = _make_table(table_index=t, journal_type="list", headers=_list_headers(), rows_values=debt_rows, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    # Creditors list
    cred_rows: List[List[Optional[str]]] = []
    for nm in creditors:
        dr, cr = creditors_list[nm]
        cred_rows.append([nm, _fmt(dr) if dr else "", _fmt(cr) if cr else ""])
    cred_rows.append(["TOTAL", _fmt(sum(float(values[0]) for values in creditors_list.values())), _fmt(sum(float(values[1]) for values in creditors_list.values()))])
    cred_list_index = t
    j, c = _make_table(table_index=t, journal_type="list", headers=_list_headers(), rows_values=cred_rows, difficulty=difficulty, mode=mode_norm)
    journals.append(j)
    correct_map.update(c)

    t += 1
    # Trial balance
    tb_index = t
    j, c = _make_table(
        table_index=t,
        journal_type="trial_balance",
        headers=_trial_balance_headers(),
        rows_values=tb_rows,
        difficulty=difficulty,
        mode=mode_norm,
        column_help=headers_to_column_help(journal_type="trial_balance", headers=_trial_balance_headers()),
        prefilled_cells=tb_prefilled_cells,
    )
    journals.append(j)
    correct_map.update(c)

    tb_balance_section_row_index = next((index for index, row in enumerate(tb_rows) if str(row[0] or "") == SECTION_LABELS["balance_sheet"]), -1)
    tb_nominal_section_row_index = next((index for index, row in enumerate(tb_rows) if str(row[0] or "") == SECTION_LABELS["nominal"]), -1)
    tb_first_folio_row_index = next((index for index, row in enumerate(tb_rows) if str(row[1] or "").strip()), -1)

    opening_trial_balance_lines = [
        f"- Capital: {fmt_money(float(opening_equity))} (Credit)",
        f"- Creditors control: {fmt_money(float(opening_creditors))} (Credit)",
        f"- Debtors control: {fmt_money(float(opening_debtors))} (Debit)",
        f"- Bank: {fmt_money(float(opening_bank))} (Debit)",
        f"- Trading stock: {fmt_money(float(opening_stock))} (Debit)",
    ]
    if float(opening_drawings):
        opening_trial_balance_lines.insert(1, f"- Drawings: {fmt_money(float(opening_drawings))} (Debit)")
    if float(opening_equipment):
        opening_trial_balance_lines.insert(2 if float(opening_drawings) else 1, f"- Equipment: {fmt_money(float(opening_equipment))} (Debit)")
    if float(opening_vehicles):
        opening_trial_balance_lines.insert(3 if float(opening_drawings) or float(opening_equipment) else 1, f"- Vehicles: {fmt_money(float(opening_vehicles))} (Debit)")
    if float(opening_petty_cash):
        opening_trial_balance_lines.append(f"- Petty cash: {fmt_money(float(opening_petty_cash))} (Debit)")
    if float(opening_loan):
        opening_trial_balance_lines.insert(1, f"- Loan: {fmt_money(float(opening_loan))} (Credit)")
    if float(opening_wages_balance):
        opening_trial_balance_lines.append(f"- Wages: {fmt_money(float(opening_wages_balance))} (Debit)")
    if float(opening_stationery_balance):
        opening_trial_balance_lines.append(f"- Stationery: {fmt_money(float(opening_stationery_balance))} (Debit)")
    opening_debtors_lines = [f"- {name}: {fmt_money(float(opening_debtors_list[name]))} Dr" for name in debtors]
    opening_debtors_lines.append(f"- Total: {fmt_money(float(opening_debtors))} Dr")
    opening_creditors_lines = [f"- {name}: {fmt_money(float(opening_creditors_list[name]))} Cr" for name in creditors]
    opening_creditors_lines.append(f"- Total: {fmt_money(float(opening_creditors))} Cr")
    opening_policy_lines = [f"- Goods are sold at cost plus {markup_pct:g}%."]
    if shared_counterparty:
        opening_policy_lines.append(f"- {shared_counterparty} appears in both the opening debtors list and opening creditors list.")
    prompt = "\n\n".join(
        [
            business,
            f"Project: Accounting cycle bookkeeping ({month} {year})",
            "Information:\n" + "\n".join(opening_policy_lines),
            f"Opening Trial Balance at 1 {month} {year}:\n" + "\n".join(opening_trial_balance_lines),
            f"Opening debtors list at 1 {month} {year}:\n" + "\n".join(opening_debtors_lines),
            f"Opening creditors list at 1 {month} {year}:\n" + "\n".join(opening_creditors_lines),
            f"Transactions for {month} {year}:\n" + _numbered_lines(transaction_lines),
            "Required:\n"
            "1) Record the transactions in the relevant journals. Use the General Journal if a correction entry is given.\n"
            "2) Post to the General Ledger and the debtors and creditors ledgers provided.\n"
            "3) Prepare the debtors list and creditors list.\n"
            "4) Prepare the Trial Balance under Balance Sheet accounts and Nominal accounts.",
        ]
    )

    guidelines = [
        "Journals record daily transactions of the same type before those effects are transferred to ledger accounts.",
        "Closing a journal means totaling the month and transferring its effect to the relevant accounts in the General Ledger or subsidiary ledgers.",
        "Ledger posting transfers journal information to accounts so that each account shows its own movement and running balance.",
        "Balancing a ledger means comparing the two sides, inserting Balance c/d where needed, and carrying the balance forward as Balance b/d.",
        "Debtors and creditors lists summarise subsidiary accounts at month end, so the list totals must reconcile to the related control accounts.",
        "DJ flows into the Debtors Ledger, then the Debtors List, then Debtors control, and finally the Trial Balance.",
        "CJ flows into the Creditors Ledger, then the Creditors List, then Creditors control, and finally the Trial Balance.",
        "CRJ and CPJ affect Bank together with control or nominal accounts, while GJ is used for adjustments and corrections that do not belong in a special journal.",
    ]

    cell_hints: Dict[str, str] = {}
    working_map: Dict[str, str] = {}
    dependency_map: Dict[str, List[str]] = {}

    if bank_gl_index >= 0:
        cell_hints[f"t{bank_gl_index}_r0_c2"] = "Begin the Bank account with Balance b/d on the debit side."
        working_map[f"t{bank_gl_index}_r0_c2"] = "The opening Bank balance comes from the opening Trial Balance and becomes the starting point for all CRJ and CPJ bank movements."
        if len(general_ledger_rows_by_account.get("Bank", [])) > 1:
            cell_hints[f"t{bank_gl_index}_r1_c3"] = "Use the folio to show which journal supplied this Bank posting, for example CRJ or CPJ."
            working_map[f"t{bank_gl_index}_r1_c3"] = "A ledger folio traces the Bank entry back to the journal where the transaction was first recorded."
        bank_balance_row = list(general_ledger_rows_by_account.get("Bank", [[]])[-1]) if general_ledger_rows_by_account.get("Bank") else []
        if bank_balance_row:
            bank_balance_detail_col = 2 if any(str(value or "").strip() for value in bank_balance_row[:5]) else 7
            cell_hints[f"t{bank_gl_index}_r{len(general_ledger_rows_by_account['Bank']) - 1}_c{bank_balance_detail_col}"] = "Carry the closing Bank balance forward as Balance b/d for the next month."
            working_map[f"t{bank_gl_index}_r{len(general_ledger_rows_by_account['Bank']) - 1}_c{bank_balance_detail_col}"] = "After balancing the Bank account, the month-end balance becomes the opening balance for the next period."
    if stock_gl_index >= 0:
        cell_hints[f"t{stock_gl_index}_r0_c2"] = "Begin the Trading stock account with Balance b/d on the debit side."
        working_map[f"t{stock_gl_index}_r0_c2"] = "Trading stock starts with the opening balance, then changes through purchases, cost of sales, allowances, and corrections."
    if sales_gl_index >= 0:
        cell_hints[f"t{sales_gl_index}_r0_c7"] = "Sales is credited when goods are sold. Post the journal effect to the Sales account on the correct side."
        working_map[f"t{sales_gl_index}_r0_c7"] = "A credit sale starts in the DJ, then the sales value is posted to Sales in the General Ledger while the customer is posted to Debtors control and the debtor's personal account."
    if debtors_control_gl_index >= 0:
        working_map[f"t{debtors_control_gl_index}_r0_c2"] = "Debtors control summarises the total effect of all debtor postings. Its closing balance must agree with the net debtors list before the Trial Balance is prepared."
    if creditors_control_gl_index >= 0:
        working_map[f"t{creditors_control_gl_index}_r0_c7" if str(general_ledger_movements.get('Creditors control', {}).get('opening_side') or '') == 'credit' else f"t{creditors_control_gl_index}_r0_c2"] = "Creditors control summarises the total effect of all creditor postings. Its closing balance must agree with the net creditors list before the Trial Balance is prepared."

    cell_hints[f"t2_r0_c2"] = "A DJ entry records a credit sale. That debtor must later be posted to the Debtors Ledger and included in Debtors control."
    working_map[f"t2_r0_c2"] = "Flow: DJ -> Debtors Ledger -> Debtors List -> Debtors control -> Trial Balance."
    dependency_map[f"t2_r0_c2"] = [f"t{debt_ledger_index}_r1_c1", f"t{debt_list_index}_r0_c1"]

    cell_hints[f"t4_r0_c2"] = "A CJ entry records a credit purchase. That supplier must later be posted to the Creditors Ledger and included in Creditors control."
    working_map[f"t4_r0_c2"] = "Flow: CJ -> Creditors Ledger -> Creditors List -> Creditors control -> Trial Balance."
    dependency_map[f"t4_r0_c2"] = [f"t{cred_ledger_index}_r1_c1", f"t{cred_list_index}_r0_c2"]

    cell_hints[f"t0_r0_c2"] = "CRJ entries usually increase Bank and may settle debtor accounts or record other receipts such as capital contributed."
    working_map[f"t0_r0_c2"] = "Flow: CRJ -> Bank plus the related control or nominal account -> Trial Balance."

    cell_hints[f"t1_r0_c2"] = "CPJ entries usually decrease Bank and may settle creditor accounts or pay expenses such as wages."
    working_map[f"t1_r0_c2"] = "Flow: CPJ -> Bank plus the related control or nominal account -> Trial Balance."

    cell_hints[f"t{debt_ledger_index}_r0_c1"] = f"Start the debtor's account for {displayed_debtor_name} with the opening balance brought down from the opening debtors list."
    working_map[f"t{debt_ledger_index}_r0_c1"] = f"The debtors ledger tracks the personal account of {displayed_debtor_name}. Its closing balance contributes to the debtors list at month end."
    cell_hints[f"t{cred_ledger_index}_r0_c1"] = f"Start the creditor's account for {displayed_creditor_name} with the opening balance brought down from the opening creditors list."
    working_map[f"t{cred_ledger_index}_r0_c1"] = f"The creditors ledger tracks the personal account of {displayed_creditor_name}. Its closing balance contributes to the creditors list at month end."

    cell_hints[f"t{debt_list_index}_r{len(debt_rows) - 1}_c1"] = "Add all debit balances in the debtors list. Debit balances still owe the business money."
    cell_hints[f"t{debt_list_index}_r{len(debt_rows) - 1}_c2"] = "Add any credit balances in the debtors list separately. These reduce the net Debtors control balance."
    cell_hints[f"t{cred_list_index}_r{len(cred_rows) - 1}_c1"] = "Add any debit balances in the creditors list separately. These reduce the net Creditors control balance."
    cell_hints[f"t{cred_list_index}_r{len(cred_rows) - 1}_c2"] = "Add all credit balances in the creditors list. Credit balances are amounts still owed to suppliers."
    working_map[f"t{debt_list_index}_r{len(debt_rows) - 1}_c1"] = "The debtors list summarises month-end personal balances. Net debtors list total = debit column total minus credit column total, and it must reconcile to Debtors control."
    working_map[f"t{cred_list_index}_r{len(cred_rows) - 1}_c2"] = "The creditors list summarises month-end personal balances. Net creditors list total = credit column total minus debit column total, and it must reconcile to Creditors control."
    dependency_map[f"t{debt_list_index}_r{len(debt_rows) - 1}_c1"] = [f"t{debt_list_index}_r{i}_c1" for i in range(len(debt_rows) - 1)]
    dependency_map[f"t{debt_list_index}_r{len(debt_rows) - 1}_c2"] = [f"t{debt_list_index}_r{i}_c2" for i in range(len(debt_rows) - 1)]
    dependency_map[f"t{cred_list_index}_r{len(cred_rows) - 1}_c1"] = [f"t{cred_list_index}_r{i}_c1" for i in range(len(cred_rows) - 1)]
    dependency_map[f"t{cred_list_index}_r{len(cred_rows) - 1}_c2"] = [f"t{cred_list_index}_r{i}_c2" for i in range(len(cred_rows) - 1)]

    if tb_balance_section_row_index >= 0:
        cell_hints[f"t{tb_index}_r{tb_balance_section_row_index}_c0"] = "Start the Trial Balance with the Balance Sheet accounts section heading."
        working_map[f"t{tb_index}_r{tb_balance_section_row_index}_c0"] = "Balance Sheet accounts are assets, liabilities, and owner's equity balances carried at month end."
    if tb_nominal_section_row_index >= 0:
        cell_hints[f"t{tb_index}_r{tb_nominal_section_row_index}_c0"] = "Use the Nominal accounts heading where the income and expense accounts begin."
        working_map[f"t{tb_index}_r{tb_nominal_section_row_index}_c0"] = "Nominal accounts include income, expenses, and related adjustments for the period."
    if tb_first_folio_row_index >= 0:
        tb_folio_account_name = str(tb_rows[tb_first_folio_row_index][0] or "this account")
        cell_hints[f"t{tb_index}_r{tb_first_folio_row_index}_c1"] = f"Copy the ledger folio for {tb_folio_account_name} into the Trial Balance folio column."
        working_map[f"t{tb_index}_r{tb_first_folio_row_index}_c1"] = f"The Trial Balance folio for {tb_folio_account_name} points back to the ledger account from which the balance was taken."
    cell_hints[f"t{tb_index}_r{len(tb_rows) - 1}_c2"] = "Add the debit column after placing each balance once in the correct section."
    cell_hints[f"t{tb_index}_r{len(tb_rows) - 1}_c3"] = "Add the credit column after placing each balance once in the correct section."
    working_map[f"t{tb_index}_r{len(tb_rows) - 1}_c2"] = "The Trial Balance debit total is the sum of all debit balances carried from the ledgers after posting and balancing."
    working_map[f"t{tb_index}_r{len(tb_rows) - 1}_c3"] = "The Trial Balance credit total is the sum of all credit balances carried from the ledgers after posting and balancing."
    tb_account_row_indices = [
        index
        for index, row in enumerate(tb_rows)
        if str(row[0] or "") not in {SECTION_LABELS["balance_sheet"], SECTION_LABELS["nominal"], "Totals"}
    ]
    dependency_map[f"t{tb_index}_r{len(tb_rows) - 1}_c2"] = [f"t{tb_index}_r{i}_c2" for i in tb_account_row_indices]
    dependency_map[f"t{tb_index}_r{len(tb_rows) - 1}_c3"] = [f"t{tb_index}_r{i}_c3" for i in tb_account_row_indices]

    out = make_journal(
        prompt=prompt,
        journal_type="full_accounting_cycle_project",
        headers=list(CRJ_HEADERS),
        rows=[],
        correct_map={},
        table_variant="grade_project",
        guidelines=guidelines,
        cell_hints=cell_hints,
        working_map=working_map if mode_norm == "scaffold" else None,
        dependency_map=dependency_map if mode_norm == "scaffold" else None,
    )
    if gj_vals:
        out.setdefault("cell_hints", {})[f"t{gj_index}_r0_c1"] = "Use the General Journal for correction entries: debit the correct account first, then credit the account that was wrongly used."
        if mode_norm == "scaffold":
            out.setdefault("working_map", {})[f"t{gj_index}_r0_c1"] = "The General Journal is used for adjustments and corrections that do not belong in the CRJ, CPJ, DJ, CJ, DAJ, CAJ, or PCJ."
    out["journals"] = journals
    out["journal"] = journals[-1] if journals else out.get("journal")
    out["correct_map"] = correct_map
    return out


def make_full_accounting_cycle_project_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    last_error: Optional[_ScenarioValidationError] = None
    for _ in range(MAX_FULL_ACCOUNTING_CYCLE_GENERATION_ATTEMPTS):
        try:
            return _make_full_accounting_cycle_project_question_once(r=r, difficulty=difficulty, mode=mode)
        except _ScenarioValidationError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise _ScenarioValidationError("Could not generate a valid full accounting cycle project.")
