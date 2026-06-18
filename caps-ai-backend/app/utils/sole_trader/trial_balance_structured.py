from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .column_help import headers_to_column_help
from .core import fmt_money, make_journal, round_money
from .journal_table import build_journal_row
from .names import pick_business_name, pick_business_names, pick_person_names


AccountRow = Dict[str, Any]

SECTION_LABELS = {
    "balance_sheet": "Balance Sheet accounts",
    "nominal": "Nominal accounts",
}

SECTION_ORDER = {
    "balance_sheet": 0,
    "nominal": 1,
}


def _trial_balance_headers() -> List[str]:
    return ["Account", "Fol.", "Debit", "Credit"]


def _title_fields() -> List[Dict[str, Any]]:
    return [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Statement", "editable": True},
    ]


def _base_trial_balance_guidelines() -> List[str]:
    return [
        "Complete the Trial Balance under the correct section headings: Balance Sheet accounts and Nominal accounts.",
        "Use the Fol. column where it is being assessed, but do not invent folio numbers if the question does not ask for them.",
        "Write each balance once only and place it in either the debit or credit column, not both.",
        "Where totals are required, add the debit and credit columns separately as the last step.",
    ]


def _trial_balance_title_answers(*, business: str, month: str, year: int) -> Dict[str, Any]:
    return {
        "title_business": business,
        "title_period": f"{month} {year}",
        "title_journal": ["Trial Balance", "Trial balance", "Trial Balance (TB)"],
    }


def _account_catalog() -> List[Dict[str, Any]]:
    return [
        {
            "name": "Capital",
            "folio": "B1",
            "side": "credit",
            "section": "balance_sheet",
            "category": "equity",
            "values": [42000, 48500, 55200, 61800, 74200, 86500],
            "clue": "Owner's claim on the business",
        },
        {
            "name": "Drawings",
            "folio": "B2",
            "side": "debit",
            "section": "balance_sheet",
            "category": "equity",
            "values": [950, 1280, 1640, 1980, 2450, 3120],
            "clue": "Amount withdrawn by the owner for personal use",
        },
        {
            "name": "Equipment",
            "folio": "B3",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [14800, 17600, 21400, 26500, 31800],
            "clue": "Equipment used in the business",
        },
        {
            "name": "Trading stock",
            "folio": "B4",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [7400, 8600, 9800, 11200, 12850],
            "clue": "Trading stock on hand at month end",
        },
        {
            "name": "Debtors control",
            "folio": "B5",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [4200, 5600, 6850, 8120, 9440],
            "clue": "Total amount owed by debtors",
        },
        {
            "name": "Bank",
            "folio": "B6",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [18250, 22400, 26800, 31550, 40200],
            "clue": "Cash at bank",
        },
        {
            "name": "Petty cash",
            "folio": "B7",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [320, 480, 620, 800, 950],
            "clue": "Petty cash on hand",
        },
        {
            "name": "Cash float",
            "folio": "B8",
            "side": "debit",
            "section": "balance_sheet",
            "category": "asset",
            "values": [1200, 1450, 1800, 2200],
            "clue": "Cash float amount",
        },
        {
            "name": "Creditors control",
            "folio": "B9",
            "side": "credit",
            "section": "balance_sheet",
            "category": "liability",
            "values": [4800, 6200, 7450, 9180, 11200],
            "clue": "Total amount owed to creditors",
        },
        {
            "name": "Mortgage loan: AB Bank",
            "folio": "B10",
            "side": "credit",
            "section": "balance_sheet",
            "category": "liability",
            "values": [9500, 12400, 15800, 18600],
            "clue": "Loan owing to AB Bank",
        },
        {
            "name": "Sales",
            "folio": "N1",
            "side": "credit",
            "section": "nominal",
            "category": "income",
            "values": [22800, 27400, 31800, 38600, 45200],
            "clue": "Sales income earned",
        },
        {
            "name": "Cost of sales",
            "folio": "N2",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [11200, 13800, 16200, 19400, 22600],
            "clue": "Cost of goods sold",
        },
        {
            "name": "Wages",
            "folio": "N3",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [2400, 3200, 4800, 5600, 7200],
            "clue": "Wages expense",
        },
        {
            "name": "Stationery",
            "folio": "N4",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [650, 820, 1050, 1320, 1680],
            "clue": "Stationery expense",
        },
        {
            "name": "Advertising",
            "folio": "N5",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [980, 1240, 1560, 1980, 2440],
            "clue": "Advertising expense",
        },
        {
            "name": "Debtors allowances",
            "folio": "N6",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [240, 360, 480, 620, 780],
            "clue": "Allowances granted to debtors",
        },
        {
            "name": "Rent income",
            "folio": "N7",
            "side": "credit",
            "section": "nominal",
            "category": "income",
            "values": [600, 850, 1200, 1500, 1800],
            "clue": "Rent income earned",
        },
        {
            "name": "Discount received",
            "folio": "N8",
            "side": "credit",
            "section": "nominal",
            "category": "income",
            "values": [180, 250, 320, 410, 520],
            "clue": "Discount received from creditors",
        },
        {
            "name": "Interest on current account",
            "folio": "N9",
            "side": "credit",
            "section": "nominal",
            "category": "income",
            "values": [120, 180, 240, 360, 480],
            "clue": "Interest earned on the current account",
        },
        {
            "name": "Bad debts",
            "folio": "N10",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [180, 240, 320, 450, 600],
            "clue": "Amounts written off as irrecoverable",
        },
        {
            "name": "Bad debts recovered",
            "folio": "N11",
            "side": "credit",
            "section": "nominal",
            "category": "income",
            "values": [120, 180, 240, 320, 450],
            "clue": "Amounts recovered after being written off",
        },
        {
            "name": "Donations",
            "folio": "N12",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [120, 180, 240, 300, 420],
            "clue": "Goods or cash donated by the business",
        },
        {
            "name": "Interest on overdraft",
            "folio": "N13",
            "side": "debit",
            "section": "nominal",
            "category": "expense",
            "values": [150, 220, 300, 380, 450],
            "clue": "Interest charged by the bank on an overdraft",
        },
    ]


def _catalog_by_name() -> Dict[str, Dict[str, Any]]:
    return {item["name"]: dict(item) for item in _account_catalog()}


def _folio_number(folio: str) -> int:
    digits = "".join(ch for ch in str(folio or "") if ch.isdigit())
    return int(digits or "0")


def _sort_entries(entries: Sequence[AccountRow]) -> List[AccountRow]:
    return sorted(
        [dict(row) for row in entries],
        key=lambda row: (SECTION_ORDER.get(str(row.get("section")), 99), _folio_number(str(row.get("folio", "")))),
    )


def _pick_balanced_entries(*, r: random.Random) -> List[AccountRow]:
    catalog = _catalog_by_name()
    required = [
        "Drawings",
        "Equipment",
        "Trading stock",
        "Debtors control",
        "Bank",
        "Creditors control",
        "Sales",
        "Cost of sales",
        "Wages",
        "Stationery",
    ]
    optional_balance_sheet = ["Petty cash", "Cash float"]
    optional_nominal_debit = ["Advertising", "Debtors allowances"]
    optional_nominal_credit = ["Rent income", "Discount received", "Interest on current account"]

    while True:
        selected_names = list(required)
        selected_names.extend(r.sample(optional_balance_sheet, k=1))
        selected_names.extend(r.sample(optional_nominal_debit, k=1))
        selected_names.extend(r.sample(optional_nominal_credit, k=2))
        if r.random() < 0.25:
            selected_names.append("Mortgage loan: AB Bank")

        entries: List[AccountRow] = []
        debit_total = 0.0
        credit_total = 0.0
        for name in selected_names:
            item = dict(catalog[name])
            amount = float(r.choice(item["values"]))
            item["amount"] = amount
            item["source"] = "balance_list"
            entries.append(item)
            if item["side"] == "debit":
                debit_total += amount
            else:
                credit_total += amount

        capital_amount = round_money(debit_total - credit_total)
        if 30000 <= capital_amount <= 180000:
            capital = dict(catalog["Capital"])
            capital["amount"] = capital_amount
            capital["source"] = "balancing_figure"
            entries.append(capital)
            return _sort_entries(entries)


def _split_total_into_parts(*, r: random.Random, total: float, parts: int, minimum: int) -> List[float]:
    remaining = int(round(total))
    out: List[int] = []
    for index in range(parts - 1):
        max_value = remaining - minimum * (parts - index - 1)
        value = r.randint(minimum, max_value)
        out.append(value)
        remaining -= value
    out.append(remaining)
    r.shuffle(out)
    return [float(value) for value in out]


def _row_display_descriptor(row: AccountRow, *, hide_name: bool) -> str:
    return str(row.get("clue") if hide_name else row.get("name"))


def _support_line(row: AccountRow, *, hide_name: bool, include_folio: bool) -> str:
    descriptor = _row_display_descriptor(row, hide_name=hide_name)
    base = f"- {descriptor}: {fmt_money(float(row['amount']))}"
    if include_folio:
        return f"{base} | Ledger folio {row['folio']}"
    return base


def _count_by_difficulty(*, difficulty: str, easy: int, medium: int, hard: int) -> int:
    diff = str(difficulty or "easy").strip().lower()
    if diff == "hard":
        return hard
    if diff == "medium":
        return medium
    return easy


def _ordered_candidate_names(entries: Sequence[AccountRow]) -> List[str]:
    priority = [
        "Capital",
        "Drawings",
        "Creditors control",
        "Debtors control",
        "Bank",
        "Trading stock",
        "Equipment",
        "Sales",
        "Cost of sales",
        "Wages",
        "Stationery",
        "Advertising",
        "Rent income",
        "Discount received",
    ]
    available = {str(row["name"]) for row in entries}
    ordered = [name for name in priority if name in available]
    ordered.extend(sorted(available - set(ordered)))
    return ordered


def _pick_target_names(entries: Sequence[AccountRow], *, difficulty: str, count_easy: int, count_medium: int, count_hard: int, exclude: Optional[Sequence[str]] = None) -> List[str]:
    needed = _count_by_difficulty(difficulty=difficulty, easy=count_easy, medium=count_medium, hard=count_hard)
    excluded = {str(name) for name in (exclude or [])}
    names = [name for name in _ordered_candidate_names(entries) if name not in excluded]
    return names[:needed]


def _rows_with_sections(entries: Sequence[AccountRow], *, debit_total: float, credit_total: float) -> Tuple[List[AccountRow], Dict[str, int], Dict[str, int]]:
    rows: List[AccountRow] = []
    name_to_row_index: Dict[str, int] = {}
    section_row_index: Dict[str, int] = {}
    for section in ("balance_sheet", "nominal"):
        section_row_index[section] = len(rows)
        rows.append({"row_type": "section", "section": section, "label": SECTION_LABELS[section]})
        for row in entries:
            if str(row["section"]) != section:
                continue
            name_to_row_index[str(row["name"])] = len(rows)
            rows.append(dict(row))
    rows.append({"row_type": "total", "debit_total": debit_total, "credit_total": credit_total})
    return rows, name_to_row_index, section_row_index


def _pick_trial_balance_period(*, r: random.Random) -> Tuple[str, str, int]:
    opening_month, current_month = r.choice(
        [
            ("January", "February"),
            ("February", "March"),
            ("March", "April"),
            ("April", "May"),
            ("May", "June"),
            ("June", "July"),
        ]
    )
    year = int(r.choice([2024, 2025, 2026]))
    return opening_month, current_month, year


def _month_end_day(*, month: str) -> int:
    month_name = str(month or "").strip().lower()
    if month_name == "february":
        return 28
    if month_name in {"april", "june", "september", "november"}:
        return 30
    return 31


def _trial_balance_date_label(*, month: str, year: int) -> str:
    return f"{_month_end_day(month=month)} {month} {year}"


def _clone_entries(entries: Sequence[AccountRow]) -> List[AccountRow]:
    return [dict(row) for row in entries]


def _entries_by_name(entries: Sequence[AccountRow]) -> Dict[str, AccountRow]:
    return {str(row["name"]): row for row in entries}


def _trial_balance_totals(entries: Sequence[AccountRow]) -> Tuple[float, float]:
    debit_total = round_money(sum(float(row["amount"]) for row in entries if str(row["side"]) == "debit"))
    credit_total = round_money(sum(float(row["amount"]) for row in entries if str(row["side"]) == "credit"))
    return debit_total, credit_total


def _build_reference_trial_balance_journal(*, heading: str, entries: Sequence[AccountRow]) -> Dict[str, Any]:
    debit_total, credit_total = _trial_balance_totals(entries)
    headers = _trial_balance_headers()
    rows: List[List[Dict[str, Any]]] = []
    
    current_section = ""
    for row in _sort_entries(entries):
        section = str(row["section"])
        if section != current_section:
            current_section = section
            rows.append(build_journal_row(row_index=len(rows), values=[SECTION_LABELS[current_section], "", "", ""], editable_cols=[]))
        amount = float(row["amount"])
        debit_value = fmt_money(amount) if str(row["side"]) == "debit" else ""
        credit_value = fmt_money(amount) if str(row["side"]) == "credit" else ""
        rows.append(build_journal_row(row_index=len(rows), values=[str(row["name"]), str(row["folio"]), debit_value, credit_value], editable_cols=[]))
    
    rows.append(build_journal_row(row_index=len(rows), values=["Totals", "", fmt_money(debit_total), fmt_money(credit_total)], editable_cols=[]))
    
    return {
        "journal_type": "reference_trial_balance",
        "headers": headers,
        "rows": rows,
        "heading": heading,
    }


def _numbered_lines(lines: Sequence[str]) -> str:
    return "\n".join(f"{index + 1}. {line}" for index, line in enumerate(lines))


def _ensure_entry_present(*, entries: List[AccountRow], name_to_entry: Dict[str, AccountRow], catalog: Dict[str, Dict[str, Any]], name: str) -> AccountRow:
    existing = name_to_entry.get(name)
    if existing is not None:
        return existing
    row = dict(catalog[name])
    row["amount"] = 0.0
    row["source"] = "month_activity"
    entries.append(row)
    name_to_entry[name] = row
    return row


def _apply_month_change(*, entries: List[AccountRow], name_to_entry: Dict[str, AccountRow], catalog: Dict[str, Dict[str, Any]], effect_notes: Dict[str, List[str]], name: str, delta: float, note: str) -> None:
    row = _ensure_entry_present(entries=entries, name_to_entry=name_to_entry, catalog=catalog, name=name)
    row["amount"] = round_money(float(row.get("amount") or 0.0) + float(delta))
    effect_notes.setdefault(name, []).append(note)


def _annotate_updated_entries(*, opening_entries: Sequence[AccountRow], closing_entries: Sequence[AccountRow], effect_notes: Dict[str, List[str]], opening_label: str) -> None:
    opening_map = _entries_by_name(opening_entries)
    for row in closing_entries:
        name = str(row["name"])
        opening_row = opening_map.get(name)
        if opening_row is None:
            opening_text = f"This account did not appear in the Trial Balance at {opening_label}."
        else:
            opening_text = f"The Trial Balance at {opening_label} showed {name} at {fmt_money(float(opening_row['amount']))} on the {opening_row['side']} side."
        notes = effect_notes.get(name, [])
        if notes:
            change_text = " Transactions affecting this account: " + " ".join(notes)
        else:
            change_text = " No listed transaction changed this account, so the balance carries forward."
        row["source_text"] = (
            f"{opening_text}{change_text} The updated month-end balance is {fmt_money(float(row['amount']))} on the {row['side']} side."
        )


def _build_trial_balance_update_prompt(*, business: str, opening_month: str, current_month: str, year: int, opening_entries: Sequence[AccountRow], transaction_lines: Sequence[str], required_text: str, extra_sections: Optional[Sequence[str]] = None) -> Tuple[str, Dict[str, Any]]:
    sections = [
        business,
        f"Transactions for {current_month} {year}:\n{_numbered_lines(transaction_lines)}",
    ]
    for section in extra_sections or []:
        if str(section).strip():
            sections.append(str(section))
    sections.append(f"Required:\n{required_text}")
    
    reference_journal = _build_reference_trial_balance_journal(
        heading=f"Trial Balance at {_trial_balance_date_label(month=opening_month, year=year)}",
        entries=opening_entries,
    )
    return "\n\n".join(sections), reference_journal


def _title_teaching_hint(*, field_id: str, business: str, month: str, year: int) -> Dict[str, str]:
    if field_id == "title_business":
        return {
            "role_in_requirement": "This title field records the business name for the Trial Balance.",
            "evidence_from_question": f"The business named in the prompt is {business}.",
            "rule_or_principle": "A Trial Balance heading must identify the business clearly.",
            "how_to_derive": f"Copy the business name exactly: {business}.",
            "transfer_tip": "Complete the heading first so the statement is clearly identified.",
        }
    if field_id == "title_period":
        return {
            "role_in_requirement": "This title field records the month and year of the Trial Balance.",
            "evidence_from_question": f"The Trial Balance is prepared for {month} {year}.",
            "rule_or_principle": "The heading must show the correct date or period for the balances extracted.",
            "how_to_derive": f"Copy the period exactly: {month} {year}.",
            "transfer_tip": "Use the exact month or date stated in the question.",
        }
    return {
        "role_in_requirement": "This title field records the name of the statement.",
        "evidence_from_question": "The required statement is the Trial Balance.",
        "rule_or_principle": "The heading should identify the statement clearly.",
        "how_to_derive": "Write Trial Balance.",
        "transfer_tip": "Use the conventional statement title shown in the question.",
    }


def _section_teaching_hint(*, expected_label: str) -> Dict[str, str]:
    if expected_label == SECTION_LABELS["balance_sheet"]:
        evidence = "This section holds assets, liabilities, and equity balances."
    else:
        evidence = "This section holds income and expense balances."
    return {
        "role_in_requirement": "This row labels the Trial Balance section that the following accounts belong to.",
        "evidence_from_question": evidence,
        "rule_or_principle": "Trial Balance accounts are grouped into Balance Sheet accounts and Nominal accounts.",
        "how_to_derive": f"Write the correct section heading: {expected_label}.",
        "transfer_tip": "When a Trial Balance is sectioned, decide first whether each account is a balance sheet item or a nominal item.",
    }


def _entry_teaching_hint(*, header_label: str, expected: str, row: AccountRow) -> Dict[str, str]:
    header = str(header_label or "").strip().lower()
    section_label = SECTION_LABELS[str(row["section"])]
    side_label = "debit" if str(row["side"]) == "debit" else "credit"
    opposite_label = "credit" if side_label == "debit" else "debit"
    source_text = str(row.get("source_text") or f"Use the balance clue for {row['name']}.")

    if header == "account":
        return {
            "role_in_requirement": "This cell records the account name or row label in the Trial Balance.",
            "evidence_from_question": source_text,
            "rule_or_principle": f"Use the correct account label that matches the balance clue and belongs under {section_label}.",
            "how_to_derive": f"The clue refers to {row['name']}, so that is the row label to write.",
            "transfer_tip": "Ask what the balance represents in the business before deciding on the row label.",
        }
    if header in {"fol.", "fol"}:
        return {
            "role_in_requirement": "This cell records the ledger folio for the account in the Trial Balance.",
            "evidence_from_question": source_text,
            "rule_or_principle": f"{row['name']} belongs under {section_label}, so its folio follows that ledger section. Balance Sheet folios use B and Nominal folios use N.",
            "how_to_derive": f"Use the ledger folio for {row['name']}: {row['folio']}.",
            "transfer_tip": "Copy folio numbers carefully. They are ledger references, not values to calculate.",
        }
    if header == "debit":
        if expected:
            rule = f"{row['name']} has a debit balance and belongs in the debit column."
            method = f"Write {expected} in the debit column for {row['name']}."
        else:
            rule = f"{row['name']} does not belong in the debit column because its balance is on the {opposite_label} side."
            method = "Leave this debit cell blank because the balance belongs in the credit column."
        return {
            "role_in_requirement": f"This cell records the debit amount for {row['name']} if it carries a debit balance.",
            "evidence_from_question": source_text,
            "rule_or_principle": rule,
            "how_to_derive": method,
            "transfer_tip": "Decide on the normal balance side before writing the amount.",
        }
    if expected:
        rule = f"{row['name']} has a credit balance and belongs in the credit column."
        method = f"Write {expected} in the credit column for {row['name']}."
    else:
        rule = f"{row['name']} does not belong in the credit column because its balance is on the {opposite_label} side."
        method = "Leave this credit cell blank because the balance belongs in the debit column."
    return {
        "role_in_requirement": f"This cell records the credit amount for {row['name']} if it carries a credit balance.",
        "evidence_from_question": source_text,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": "Decide on the normal balance side before writing the amount.",
    }


def _total_row_teaching_hint(*, header_label: str, expected: str, column_side: str, entries: Sequence[AccountRow]) -> Dict[str, str]:
    names = ", ".join(row["name"] for row in entries if str(row["side"]) == column_side)
    return {
        "role_in_requirement": f"This {header_label} cell records the total of the {column_side} column.",
        "evidence_from_question": f"Use only the accounts that belong in the {column_side} column: {names}.",
        "rule_or_principle": "Add the debit and credit columns separately. Do not mix balances from opposite sides.",
        "how_to_derive": f"Add the relevant column balances to reach {expected}.",
        "transfer_tip": "Total the columns only after checking that each account sits on the correct side.",
    }


def _make_trial_balance_output(
    *,
    prompt: str,
    business: str,
    month: str,
    year: int,
    rows_data: Sequence[AccountRow],
    blanked_cells: Sequence[Tuple[int, int]],
    cell_hints: Dict[str, Any],
    derivation_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    headers = _trial_balance_headers()
    row_ids = {(int(row_index), int(col_index)) for row_index, col_index in blanked_cells}
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    entry_rows = [row for row in rows_data if row.get("row_type") not in {"section", "total"}]

    for row_index, row_data in enumerate(rows_data):
        if row_data.get("row_type") == "section":
            values: List[str] = [str(row_data["label"]), "", "", ""]
        elif row_data.get("row_type") == "total":
            values = ["Totals", "", fmt_money(float(row_data["debit_total"])), fmt_money(float(row_data["credit_total"]))]
        else:
            amount = float(row_data["amount"])
            values = [
                str(row_data["name"]),
                str(row_data["folio"]),
                fmt_money(amount) if str(row_data["side"]) == "debit" else "",
                fmt_money(amount) if str(row_data["side"]) == "credit" else "",
            ]

        editable_cols = [col_index for col_index in range(len(headers)) if (row_index, col_index) in row_ids]
        delivered_values = ["" if (row_index, col_index) in row_ids else value for col_index, value in enumerate(values)]
        rows.append(build_journal_row(row_index=row_index, values=delivered_values, editable_cols=editable_cols))

        for col_index, expected in enumerate(values):
            key = f"r{row_index}_c{col_index}"
            if (row_index, col_index) not in row_ids:
                continue
            correct_map[key] = str(expected)
            if row_data.get("row_type") == "section" and col_index == 0:
                cell_teaching_map[key] = _section_teaching_hint(expected_label=str(expected))
            elif row_data.get("row_type") == "total" and col_index in {2, 3}:
                column_side = "debit" if col_index == 2 else "credit"
                cell_teaching_map[key] = _total_row_teaching_hint(
                    header_label=headers[col_index],
                    expected=str(expected),
                    column_side=column_side,
                    entries=entry_rows,
                )
            elif row_data.get("row_type") not in {"section", "total"}:
                cell_teaching_map[key] = _entry_teaching_hint(
                    header_label=headers[col_index],
                    expected=str(expected),
                    row=row_data,
                )

    correct_map.update(_trial_balance_title_answers(business=business, month=month, year=year))
    for field in _title_fields():
        cell_teaching_map[field["cell_id"]] = _title_teaching_hint(
            field_id=str(field["cell_id"]),
            business=business,
            month=month,
            year=year,
        )

    out = make_journal(
        prompt=prompt,
        journal_type="trial_balance",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=_base_trial_balance_guidelines(),
        table_variant="grade_project",
        column_help=headers_to_column_help(journal_type="trial_balance", headers=headers),
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        title_fields=_title_fields(),
        id_prefix="acct10_st_trial_balance",
    )
    out["question_type"] = "ledger"
    out["expected_answer_type"] = "ledger"
    if derivation_map:
        out["derivation_map"] = derivation_map
    return out


def _mark_section_targets(*, blanked_cells: List[Tuple[int, int]], cell_hints: Dict[str, Any], derivation_map: Dict[str, str], section_row_index: Dict[str, int]) -> None:
    for section, row_index in section_row_index.items():
        expected_label = SECTION_LABELS[str(section)]
        blanked_cells.append((row_index, 0))
        cell_hints[f"r{row_index}_c0"] = "Use the accounts grouped under this heading to identify the correct Trial Balance section label."
        derivation_map[f"r{row_index}_c0"] = f"The correct section heading here is {expected_label}."


def _mark_label_targets(*, blanked_cells: List[Tuple[int, int]], cell_hints: Dict[str, Any], derivation_map: Dict[str, str], entries: Sequence[AccountRow], name_to_row_index: Dict[str, int], target_names: Sequence[str]) -> None:
    for name in target_names:
        row = next(item for item in entries if str(item["name"]) == name)
        row_index = name_to_row_index[name]
        blanked_cells.append((row_index, 0))
        cell_hints[f"r{row_index}_c0"] = "Use the account evidence in the question to identify the correct account name for this row."
        derivation_map[f"r{row_index}_c0"] = f"The correct account name for this row is {name}."
        row["source_text"] = str(row.get("source_text") or f"The balance clue is: {row['clue']}. The correct row label is {name}.")


def _mark_folio_targets(*, blanked_cells: List[Tuple[int, int]], cell_hints: Dict[str, Any], derivation_map: Dict[str, str], entries: Sequence[AccountRow], name_to_row_index: Dict[str, int], target_names: Sequence[str]) -> None:
    for name in target_names:
        row = next(item for item in entries if str(item["name"]) == name)
        row_index = name_to_row_index[name]
        blanked_cells.append((row_index, 1))
        cell_hints[f"r{row_index}_c1"] = f"Copy the correct ledger folio for {name}."
        derivation_map[f"r{row_index}_c1"] = f"{name} uses folio {row['folio']}."
        row["source_text"] = str(row.get("source_text") or f"The ledger reference for {name} is folio {row['folio']}.")


def _mark_money_targets(*, blanked_cells: List[Tuple[int, int]], cell_hints: Dict[str, Any], derivation_map: Dict[str, str], entries: Sequence[AccountRow], name_to_row_index: Dict[str, int], target_names: Sequence[str], blank_opposite_side: bool = True) -> None:
    for name in target_names:
        row = next(item for item in entries if str(item["name"]) == name)
        row_index = name_to_row_index[name]
        correct_col_index = 2 if str(row['side']) == 'debit' else 3
        blanked_cells.append((row_index, correct_col_index))
        if blank_opposite_side:
            blanked_cells.append((row_index, 3 if correct_col_index == 2 else 2))
        money_key = f"r{row_index}_c{correct_col_index}"
        if blank_opposite_side:
            cell_hints[money_key] = f"{name} has a {row['side']} balance, so write the amount in the {row['side']} column and leave the other side blank."
        else:
            cell_hints[money_key] = f"{name} has a {row['side']} balance, so write the amount in the {row['side']} column."
        default_source_text = f"The updated month-end balance for {name} is {fmt_money(float(row['amount']))} on the {row['side']} side."
        derivation_map[money_key] = str(row.get("source_text") or default_source_text)
        row["source_text"] = str(row.get("source_text") or default_source_text)


def _mark_totals(*, blanked_cells: List[Tuple[int, int]], cell_hints: Dict[str, Any], derivation_map: Dict[str, str], total_row_index: int, debit_total: float, credit_total: float) -> None:
    blanked_cells.extend([(total_row_index, 2), (total_row_index, 3)])
    cell_hints[f"r{total_row_index}_c2"] = "Add only the debit balances to calculate the debit total."
    cell_hints[f"r{total_row_index}_c3"] = "Add only the credit balances to calculate the credit total."
    derivation_map[f"r{total_row_index}_c2"] = f"The debit column totals {fmt_money(debit_total)}."
    derivation_map[f"r{total_row_index}_c3"] = f"The credit column totals {fmt_money(credit_total)}."


def _build_prompt_from_entries(*, business: str, month: str, year: int, entries: Sequence[AccountRow], label_targets: Sequence[str], include_folio: bool, lead_text: str, required_text: str, r: Optional[random.Random] = None, shuffle_lines: bool = False) -> str:
    lines = []
    for row in entries:
        hide_name = str(row["name"]) in set(label_targets)
        lines.append(_support_line(row, hide_name=hide_name, include_folio=include_folio))
    if shuffle_lines and r is not None:
        r.shuffle(lines)
    joined_lines = '\n'.join(lines)
    return (
        f"{business}\n"
        f"Trial Balance for {month} {year}\n\n"
        f"{lead_text}\n"
        f"{joined_lines}\n\n"
        f"Required:\n{required_text}"
    )


def _build_direct_update_scenario(*, r: random.Random, difficulty: str, business: Optional[str] = None) -> Dict[str, Any]:
    business = str(business or pick_business_name(r=r))
    opening_month, current_month, year = _pick_trial_balance_period(r=r)
    opening_label = _trial_balance_date_label(month=opening_month, year=year)
    catalog = _catalog_by_name()
    opening_entries = _pick_balanced_entries(r=r)
    closing_entries = _clone_entries(opening_entries)
    closing_map = _entries_by_name(closing_entries)
    effect_notes: Dict[str, List[str]] = {}
    transaction_lines: List[str] = []

    drawings_amount = float(r.choice([360, 480, 600, 720]))
    transaction_lines.append(f"The owner withdrew cash, {fmt_money(drawings_amount)}, for personal use.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-drawings_amount, note=f"Decrease by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Drawings", delta=drawings_amount, note=f"Increase by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")

    wages_amount = float(r.choice([600, 800, 1000, 1200]))
    transaction_lines.append(f"Paid wages by EFT, {fmt_money(wages_amount)}.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-wages_amount, note=f"Decrease by {fmt_money(wages_amount)} because wages were paid by EFT.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Wages", delta=wages_amount, note=f"Increase by {fmt_money(wages_amount)} because wages for the month were incurred and paid.")

    stationery_amount = float(r.choice([180, 240, 320, 400]))
    transaction_lines.append(f"Bought stationery on credit, {fmt_money(stationery_amount)}.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Stationery", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} for stationery bought on credit.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} because the stationery purchase is still owing to creditors.")

    debtor_receipt = float(r.choice([700, 900, 1100, 1300]))
    transaction_lines.append(f"Received an EFT from debtors in settlement of accounts, {fmt_money(debtor_receipt)}.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=debtor_receipt, note=f"Increase by {fmt_money(debtor_receipt)} because debtors paid by EFT.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=-debtor_receipt, note=f"Decrease by {fmt_money(debtor_receipt)} because the amount owing by debtors was settled.")

    if str(difficulty or "easy").strip().lower() in {"medium", "hard"}:
        sales_value = float(r.choice([1750, 2000, 2500, 3000]))
        cost_value = round_money(sales_value * 0.40)
        transaction_lines.append(f"Made credit sales of {fmt_money(sales_value)}. The cost price of the goods sold was {fmt_money(cost_value)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} for credit sales made during the month.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Sales", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} because the business earned additional sales income.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Cost of sales", delta=cost_value, note=f"Increase by {fmt_money(cost_value)} because goods sold must be transferred to cost of sales.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=-cost_value, note=f"Decrease by {fmt_money(cost_value)} because trading stock on hand was reduced by the goods sold.")

    if str(difficulty or "easy").strip().lower() == "hard":
        creditor_total = float(r.choice([720, 840, 960, 1080]))
        discount_received = float(r.choice([40, 60, 80]))
        payment = creditor_total - discount_received
        transaction_lines.append(f"Paid a creditor {fmt_money(payment)} by EFT in full settlement of {fmt_money(creditor_total)}. Discount received amounted to {fmt_money(discount_received)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-payment, note=f"Decrease by {fmt_money(payment)} because the creditor was paid by EFT.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=-creditor_total, note=f"Decrease by {fmt_money(creditor_total)} because the creditor account was settled in full.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Discount received", delta=discount_received, note=f"Increase by {fmt_money(discount_received)} because a settlement discount was received from a creditor.")

    closing_entries = _sort_entries([row for row in closing_entries if float(row.get("amount") or 0.0) > 0.0])
    _annotate_updated_entries(opening_entries=opening_entries, closing_entries=closing_entries, effect_notes=effect_notes, opening_label=opening_label)
    changed_names = [name for name in _ordered_candidate_names(closing_entries) if name in effect_notes]
    return {
        "business": business,
        "opening_month": opening_month,
        "month": current_month,
        "year": year,
        "opening_entries": opening_entries,
        "closing_entries": closing_entries,
        "transaction_lines": transaction_lines,
        "changed_names": changed_names,
    }


def _build_mixed_update_scenario(*, r: random.Random, difficulty: str, business: Optional[str] = None) -> Dict[str, Any]:
    business = str(business or pick_business_name(r=r))
    opening_month, current_month, year = _pick_trial_balance_period(r=r)
    opening_label = _trial_balance_date_label(month=opening_month, year=year)
    catalog = _catalog_by_name()
    opening_entries = _pick_balanced_entries(r=r)
    closing_entries = _clone_entries(opening_entries)
    closing_map = _entries_by_name(closing_entries)
    effect_notes: Dict[str, List[str]] = {}
    transaction_lines: List[str] = []

    # 1. Sales
    sales_value = float(r.choice([2250, 2500, 3000, 3500]))
    cost_value = round_money(sales_value * 0.40)
    transaction_lines.append(f"Made credit sales of {fmt_money(sales_value)}. The cost price of the goods sold was {fmt_money(cost_value)}.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} for credit sales made during the month.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Sales", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} because the business earned additional sales income.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Cost of sales", delta=cost_value, note=f"Increase by {fmt_money(cost_value)} because goods sold must be transferred to cost of sales.")
    _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=-cost_value, note=f"Decrease by {fmt_money(cost_value)} because trading stock on hand was reduced by the goods sold.")

    # 2. Debtor receipts / Bad Debts Recovered
    if r.random() < 0.3:
        recovery_amount = float(r.choice([150, 200, 250]))
        transaction_lines.append(f"Received a cheque for {fmt_money(recovery_amount)} from a debtor whose account was previously written off as irrecoverable.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=recovery_amount, note=f"Increase by {fmt_money(recovery_amount)} for cash received.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bad debts recovered", delta=recovery_amount, note=f"Increase by {fmt_money(recovery_amount)} for bad debts recovered.")
    else:
        dishonoured_amount = float(r.choice([360, 450, 540, 630]))
        transaction_lines.append(f"A cheque for {fmt_money(dishonoured_amount)} received from a debtor in the previous month was dishonoured and marked 'refer to drawer'.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-dishonoured_amount, note=f"Decrease by {fmt_money(dishonoured_amount)} because the bank reversed the dishonoured cheque.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=dishonoured_amount, note=f"Increase by {fmt_money(dishonoured_amount)} because the dishonoured cheque restores the amount still owing by the debtor.")

    # 3. Allowances / Returns / Donations
    if r.random() < 0.3:
        donation_amount = float(r.choice([100, 150, 200]))
        transaction_lines.append(f"Donated merchandise with a cost price of {fmt_money(donation_amount)} to a local children's home.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Donations", delta=donation_amount, note=f"Increase by {fmt_money(donation_amount)} because goods were donated.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=-donation_amount, note=f"Decrease by {fmt_money(donation_amount)} because trading stock was removed from the business.")
    else:
        allowance_amount = float(r.choice([120, 180, 240, 300]))
        transaction_lines.append(f"Granted a debtor an allowance of {fmt_money(allowance_amount)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors allowances", delta=allowance_amount, note=f"Increase by {fmt_money(allowance_amount)} because an allowance was granted to a debtor.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=-allowance_amount, note=f"Decrease by {fmt_money(allowance_amount)} because the debtor now owes less after the allowance.")

    # 4. Creditors / Trade Discount
    if r.random() < 0.3:
        purchases = float(r.choice([1000, 1500, 2000]))
        trade_discount = purchases * 0.2
        net_purchases = purchases - trade_discount
        transaction_lines.append(f"Purchased trading stock on credit for {fmt_money(purchases)}, subject to a 20% trade discount.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=net_purchases, note=f"Increase by {fmt_money(net_purchases)} for the net cost of stock purchased.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=net_purchases, note=f"Increase by {fmt_money(net_purchases)} for the amount owed to the creditor.")
    else:
        creditor_total = float(r.choice([720, 840, 960, 1080]))
        discount_received = float(r.choice([40, 60, 80]))
        payment = creditor_total - discount_received
        transaction_lines.append(f"Paid a creditor {fmt_money(payment)} by EFT in full settlement of {fmt_money(creditor_total)}. Discount received amounted to {fmt_money(discount_received)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-payment, note=f"Decrease by {fmt_money(payment)} because the creditor was paid by EFT.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=-creditor_total, note=f"Decrease by {fmt_money(creditor_total)} because the creditor account was settled in full.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Discount received", delta=discount_received, note=f"Increase by {fmt_money(discount_received)} because a settlement discount was received from a creditor.")

    # 5. Drawings / Capital
    if r.random() < 0.3:
        capital_inj = float(r.choice([5000, 10000, 15000]))
        transaction_lines.append(f"The owner transferred {fmt_money(capital_inj)} into the business bank account as an additional capital contribution.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=capital_inj, note=f"Increase by {fmt_money(capital_inj)} because money was deposited into the business.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Capital", delta=capital_inj, note=f"Increase by {fmt_money(capital_inj)} because the owner contributed additional capital.")
    else:
        drawings_amount = float(r.choice([420, 540, 660, 780]))
        transaction_lines.append(f"The owner withdrew cash, {fmt_money(drawings_amount)}, for personal use.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-drawings_amount, note=f"Decrease by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Drawings", delta=drawings_amount, note=f"Increase by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")

    # 6. Adjustments (Difficulty scaling)
    if str(difficulty or "easy").strip().lower() in ["medium", "hard"]:
        if r.random() < 0.5:
            interest_amt = float(r.choice([250, 300, 350]))
            transaction_lines.append(f"The bank statement showed interest charged on the overdraft of {fmt_money(interest_amt)}.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Interest on overdraft", delta=interest_amt, note=f"Increase by {fmt_money(interest_amt)} for interest charged.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-interest_amt, note=f"Decrease by {fmt_money(interest_amt)} because bank account was charged.")
        else:
            rent_inc = float(r.choice([1000, 1200, 1500]))
            transaction_lines.append(f"A tenant paid their rent of {fmt_money(rent_inc)} directly into the business bank account.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=rent_inc, note=f"Increase by {fmt_money(rent_inc)} for rent received.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Rent income", delta=rent_inc, note=f"Increase by {fmt_money(rent_inc)} for rent earned.")

    if str(difficulty or "easy").strip().lower() == "hard":
        if r.random() < 0.5:
            equipment_amount = float(r.choice([900, 1200, 1500]))
            transaction_lines.append(f"Bought equipment on credit for {fmt_money(equipment_amount)}.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Equipment", delta=equipment_amount, note=f"Increase by {fmt_money(equipment_amount)} because additional equipment was acquired.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=equipment_amount, note=f"Increase by {fmt_money(equipment_amount)} because the equipment purchase is still owing to creditors.")
        else:
            bad_debt_amt = float(r.choice([300, 400, 500]))
            transaction_lines.append(f"A debtor was declared insolvent. Received a dividend of 50 cents in the Rand amounting to {fmt_money(bad_debt_amt / 2)}. The rest of their account must be written off as irrecoverable.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=bad_debt_amt / 2, note=f"Increase by {fmt_money(bad_debt_amt / 2)} for the dividend received.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bad debts", delta=bad_debt_amt / 2, note=f"Increase by {fmt_money(bad_debt_amt / 2)} for the portion written off.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=-bad_debt_amt, note=f"Decrease by {fmt_money(bad_debt_amt)} to completely clear the debtor's account.")

    closing_entries = _sort_entries([row for row in closing_entries if float(row.get("amount") or 0.0) > 0.0])
    _annotate_updated_entries(opening_entries=opening_entries, closing_entries=closing_entries, effect_notes=effect_notes, opening_label=opening_label)
    changed_names = [name for name in _ordered_candidate_names(closing_entries) if name in effect_notes]
    return {
        "business": business,
        "opening_month": opening_month,
        "month": current_month,
        "year": year,
        "opening_entries": opening_entries,
        "closing_entries": closing_entries,
        "transaction_lines": transaction_lines,
        "changed_names": changed_names,
    }


def _build_control_update_scenario(*, r: random.Random, difficulty: str, business: Optional[str] = None) -> Dict[str, Any]:
    business = str(business or pick_business_name(r=r))
    opening_month, current_month, year = _pick_trial_balance_period(r=r)
    opening_label = _trial_balance_date_label(month=opening_month, year=year)
    catalog = _catalog_by_name()
    opening_entries = _pick_balanced_entries(r=r)
    closing_entries = _clone_entries(opening_entries)
    closing_map = _entries_by_name(closing_entries)
    effect_notes: Dict[str, List[str]] = {}
    transaction_lines: List[str] = []
    control_kind = r.choice(["debtors", "creditors"])

    if control_kind == "debtors":
        control_name = "Debtors control"
        sales_value = float(r.choice([2250, 2500, 3000]))
        cost_value = round_money(sales_value * 0.40)
        receipt_amount = float(r.choice([700, 900, 1100]))
        allowance_amount = float(r.choice([120, 180, 240]))
        wages_amount = float(r.choice([600, 800, 1000]))
        
        transaction_lines.extend([
            f"Made credit sales of {fmt_money(sales_value)}. The cost price of the goods sold was {fmt_money(cost_value)}.",
            f"Received an EFT from debtors in settlement of accounts, {fmt_money(receipt_amount)}.",
        ])
        
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} for credit sales made during the month.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Sales", delta=sales_value, note=f"Increase by {fmt_money(sales_value)} because the business earned additional sales income.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Cost of sales", delta=cost_value, note=f"Increase by {fmt_money(cost_value)} because goods sold must be transferred to cost of sales.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=-cost_value, note=f"Decrease by {fmt_money(cost_value)} because trading stock on hand was reduced by the goods sold.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=receipt_amount, note=f"Increase by {fmt_money(receipt_amount)} because debtors paid by EFT.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=-receipt_amount, note=f"Decrease by {fmt_money(receipt_amount)} because the amount owing by debtors was settled.")

        if r.random() < 0.5:
            transaction_lines.append(f"Granted a debtor an allowance of {fmt_money(allowance_amount)}.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors allowances", delta=allowance_amount, note=f"Increase by {fmt_money(allowance_amount)} because an allowance was granted to a debtor.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=-allowance_amount, note=f"Decrease by {fmt_money(allowance_amount)} because the debtor now owes less after the allowance.")
        else:
            carriage_amt = float(r.choice([150, 200, 250]))
            transaction_lines.append(f"Paid {fmt_money(carriage_amt)} out of petty cash for delivery of goods to a customer. This amount was charged to the debtor's account.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Petty cash", delta=-carriage_amt, note=f"Decrease by {fmt_money(carriage_amt)} for delivery costs paid.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Debtors control", delta=carriage_amt, note=f"Increase by {fmt_money(carriage_amt)} because delivery costs were levied to the debtor's account.")

        transaction_lines.append(f"Paid wages by EFT, {fmt_money(wages_amount)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-wages_amount, note=f"Decrease by {fmt_money(wages_amount)} because wages were paid by EFT.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Wages", delta=wages_amount, note=f"Increase by {fmt_money(wages_amount)} because wages for the month were incurred and paid.")
        
        list_names = pick_person_names(r=r, k=4)
        list_heading = f"Balances from the Debtors Ledger at the end of {current_month} {year}"
        minimum = 600
    else:
        control_name = "Creditors control"
        stationery_amount = float(r.choice([180, 240, 320]))
        equipment_amount = float(r.choice([900, 1200, 1500]))
        creditor_total = float(r.choice([720, 840, 960]))
        discount_received = float(r.choice([40, 60, 80]))
        payment = creditor_total - discount_received
        drawings_amount = float(r.choice([360, 480, 600]))
        
        if r.random() < 0.5:
            transaction_lines.append(f"Bought stationery on credit, {fmt_money(stationery_amount)}.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Stationery", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} for stationery bought on credit.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} because the stationery purchase is still owing to creditors.")
        else:
            transaction_lines.append(f"Bought stationery on credit for {fmt_money(stationery_amount)}. By mistake, this was posted to the Trading stock account instead. Correct the error.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Trading stock", delta=-stationery_amount, note=f"Decrease by {fmt_money(stationery_amount)} to reverse the incorrect entry.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Stationery", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} to correctly record the stationery purchase.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=stationery_amount, note=f"Increase by {fmt_money(stationery_amount)} because the stationery purchase is still owing to creditors.")

        if r.random() < 0.5:
            transaction_lines.append(f"Bought equipment on credit for {fmt_money(equipment_amount)}.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Equipment", delta=equipment_amount, note=f"Increase by {fmt_money(equipment_amount)} because additional equipment was acquired.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=equipment_amount, note=f"Increase by {fmt_money(equipment_amount)} because the equipment purchase is still owing to creditors.")
        else:
            trade_disc = equipment_amount * 0.2
            transaction_lines.append(f"Bought equipment on credit for {fmt_money(equipment_amount)}. The supplier forgot to deduct a 20% trade discount. A Debit Note was issued to correct this.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Equipment", delta=equipment_amount - trade_disc, note=f"Increase by {fmt_money(equipment_amount - trade_disc)} for the correct net cost of the equipment.")
            _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=equipment_amount - trade_disc, note=f"Increase by {fmt_money(equipment_amount - trade_disc)} for the correct net amount owed.")

        transaction_lines.append(f"Paid a creditor {fmt_money(payment)} by EFT in full settlement of {fmt_money(creditor_total)}. Discount received amounted to {fmt_money(discount_received)}.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-payment, note=f"Decrease by {fmt_money(payment)} because the creditor was paid by EFT.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Creditors control", delta=-creditor_total, note=f"Decrease by {fmt_money(creditor_total)} because the creditor account was settled in full.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Discount received", delta=discount_received, note=f"Increase by {fmt_money(discount_received)} because a settlement discount was received from a creditor.")
        
        transaction_lines.append(f"The owner withdrew cash, {fmt_money(drawings_amount)}, for personal use.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Bank", delta=-drawings_amount, note=f"Decrease by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")
        _apply_month_change(entries=closing_entries, name_to_entry=closing_map, catalog=catalog, effect_notes=effect_notes, name="Drawings", delta=drawings_amount, note=f"Increase by {fmt_money(drawings_amount)} because the owner withdrew cash for personal use.")
        
        list_names = pick_business_names(r=r, k=4)
        list_heading = f"Balances from the Creditors Ledger at the end of {current_month} {year}"
        minimum = 700

    closing_entries = _sort_entries([row for row in closing_entries if float(row.get("amount") or 0.0) > 0.0])
    _annotate_updated_entries(opening_entries=opening_entries, closing_entries=closing_entries, effect_notes=effect_notes, opening_label=opening_label)
    closing_map = _entries_by_name(closing_entries)
    control_row = closing_map[control_name]
    control_total = float(control_row["amount"])
    list_values = _split_total_into_parts(r=r, total=control_total, parts=4, minimum=minimum)
    list_lines = [f"- {name}: {fmt_money(value)}" for name, value in zip(list_names, list_values)]
    control_row["source_text"] = f"The {list_heading.lower()} total {fmt_money(control_total)}. That total must agree with the updated {control_name} balance in the Trial Balance. {control_row['source_text']}"
    changed_names = [name for name in _ordered_candidate_names(closing_entries) if name in effect_notes]
    return {
        "business": business,
        "opening_month": opening_month,
        "month": current_month,
        "year": year,
        "opening_entries": opening_entries,
        "closing_entries": closing_entries,
        "transaction_lines": transaction_lines,
        "changed_names": changed_names,
        "control_name": control_name,
        "list_heading": list_heading,
        "list_lines": list_lines,
        "control_total": control_total,
    }


def make_trial_balance_from_balances_question(*, r: random.Random, difficulty: str = "easy", mode: str = "", business: Optional[str] = None) -> Dict[str, Any]:
    test_folio = r.random() < 0.30
    test_totals = r.random() < 0.40
    scenario = _build_direct_update_scenario(r=r, difficulty=difficulty, business=business)
    business = str(scenario["business"])
    month = str(scenario["month"])
    year = int(scenario["year"])
    entries = list(scenario["closing_entries"])
    debit_total, credit_total = _trial_balance_totals(entries)
    rows_data, name_to_row_index, _ = _rows_with_sections(entries, debit_total=debit_total, credit_total=credit_total)

    label_targets = _pick_target_names(entries, difficulty=difficulty, count_easy=1, count_medium=2, count_hard=2)
    folio_targets = _pick_target_names(entries, difficulty=difficulty, count_easy=1, count_medium=2, count_hard=2, exclude=label_targets) if test_folio else []
    money_targets = [str(row["name"]) for row in entries]

    blanked_cells: List[Tuple[int, int]] = []
    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}

    _mark_label_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=label_targets,
    )
    if test_folio:
        _mark_folio_targets(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            entries=entries,
            name_to_row_index=name_to_row_index,
            target_names=folio_targets,
        )
    _mark_money_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=money_targets,
        blank_opposite_side=True,
    )
    if test_totals:
        _mark_totals(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            total_row_index=len(rows_data) - 1,
            debit_total=debit_total,
            credit_total=credit_total,
        )

    prompt, reference_journal = _build_trial_balance_update_prompt(
        business=business,
        opening_month=str(scenario["opening_month"]),
        current_month=month,
        year=year,
        opening_entries=list(scenario["opening_entries"]),
        transaction_lines=list(scenario["transaction_lines"]),
        required_text=f"Prepare the Trial Balance for {month} {year} using the Trial Balance at {_trial_balance_date_label(month=str(scenario['opening_month']), year=year)} and the transactions during {month} {year}. Carry forward balances that did not change, update the balances that did change, and complete folios only where those cells are blank.",
    )

    out = _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        rows_data=rows_data,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    out["reference_journal"] = reference_journal
    return out


def make_trial_balance_partial_completion_question(*, r: random.Random, difficulty: str = "easy", mode: str = "", business: Optional[str] = None) -> Dict[str, Any]:
    test_folio = r.random() < 0.30
    test_totals = r.random() < 0.45
    scenario = _build_mixed_update_scenario(r=r, difficulty=difficulty, business=business)
    business = str(scenario["business"])
    month = str(scenario["month"])
    year = int(scenario["year"])
    entries = list(scenario["closing_entries"])
    debit_total, credit_total = _trial_balance_totals(entries)
    rows_data, name_to_row_index, section_row_index = _rows_with_sections(entries, debit_total=debit_total, credit_total=credit_total)

    label_targets = _pick_target_names(entries, difficulty=difficulty, count_easy=3, count_medium=4, count_hard=5)
    folio_targets = _pick_target_names(entries, difficulty=difficulty, count_easy=1, count_medium=2, count_hard=3, exclude=label_targets) if test_folio else []
    money_targets = [str(row["name"]) for row in entries]

    blanked_cells: List[Tuple[int, int]] = []
    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}

    _mark_section_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        section_row_index=section_row_index,
    )
    _mark_label_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=label_targets,
    )
    if test_folio:
        _mark_folio_targets(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            entries=entries,
            name_to_row_index=name_to_row_index,
            target_names=folio_targets,
        )
    _mark_money_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=money_targets,
        blank_opposite_side=False,
    )
    if test_totals:
        _mark_totals(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            total_row_index=len(rows_data) - 1,
            debit_total=debit_total,
            credit_total=credit_total,
        )

    prompt, reference_journal = _build_trial_balance_update_prompt(
        business=business,
        opening_month=str(scenario["opening_month"]),
        current_month=month,
        year=year,
        opening_entries=list(scenario["opening_entries"]),
        transaction_lines=list(scenario["transaction_lines"]),
        required_text=f"Prepare the Trial Balance for {month} {year} using the Trial Balance at {_trial_balance_date_label(month=str(scenario['opening_month']), year=year)} and the transactions during {month} {year}. Some section headings, account names, and final month-end balances have been left blank, so identify the correct rows and place each closing balance in the correct debit or credit column. Complete folios or totals only where those cells are blank.",
    )

    out = _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        rows_data=rows_data,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    out["reference_journal"] = reference_journal
    return out


def make_trial_balance_control_balance_question(*, r: random.Random, difficulty: str = "easy", mode: str = "", business: Optional[str] = None) -> Dict[str, Any]:
    test_folio = r.random() < 0.30
    test_totals = r.random() < 0.35
    scenario = _build_control_update_scenario(r=r, difficulty=difficulty, business=business)
    business = str(scenario["business"])
    month = str(scenario["month"])
    year = int(scenario["year"])
    entries = list(scenario["closing_entries"])
    control_name = str(scenario["control_name"])
    debit_total, credit_total = _trial_balance_totals(entries)
    rows_data, name_to_row_index, _ = _rows_with_sections(entries, debit_total=debit_total, credit_total=credit_total)

    changed_name_set = set(str(name) for name in scenario["changed_names"])
    changed_order = [name for name in _ordered_candidate_names(entries) if name in changed_name_set and name != control_name]
    extra_label_targets = changed_order[: _count_by_difficulty(difficulty=difficulty, easy=0, medium=1, hard=2)]
    label_targets = [control_name] + extra_label_targets
    folio_targets = changed_order[: _count_by_difficulty(difficulty=difficulty, easy=1, medium=1, hard=2)] if test_folio else []
    money_targets = [control_name] + changed_order[: _count_by_difficulty(difficulty=difficulty, easy=1, medium=2, hard=3)]

    blanked_cells: List[Tuple[int, int]] = []
    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}

    _mark_label_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=label_targets,
    )
    if test_folio:
        _mark_folio_targets(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            entries=entries,
            name_to_row_index=name_to_row_index,
            target_names=folio_targets,
        )
    _mark_money_targets(
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
        entries=entries,
        name_to_row_index=name_to_row_index,
        target_names=money_targets,
        blank_opposite_side=False,
    )
    if test_totals:
        _mark_totals(
            blanked_cells=blanked_cells,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            total_row_index=len(rows_data) - 1,
            debit_total=debit_total,
            credit_total=credit_total,
        )

    control_row = next(row for row in entries if str(row["name"]) == control_name)
    control_amount_key = f"r{name_to_row_index[control_name]}_c{2 if str(control_row['side']) == 'debit' else 3}"
    cell_hints[control_amount_key] = f"Add the balances in {scenario['list_heading']} to determine the updated {control_name} balance."
    derivation_map[control_amount_key] = str(control_row.get("source_text") or "")

    prompt, reference_journal = _build_trial_balance_update_prompt(
        business=business,
        opening_month=str(scenario["opening_month"]),
        current_month=month,
        year=year,
        opening_entries=list(scenario["opening_entries"]),
        transaction_lines=list(scenario["transaction_lines"]),
        extra_sections=[f"{scenario['list_heading']}:\n" + '\n'.join(scenario['list_lines'])],
        required_text=f"Prepare the Trial Balance for {month} {year} using the Trial Balance at {_trial_balance_date_label(month=str(scenario['opening_month']), year=year)}, the transactions during {month} {year}, and the subsidiary list totals. Determine the updated control-account balance from the list, place it on the correct side, and complete any missing row labels, folios, or totals where those cells are blank.",
    )

    out = _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        rows_data=rows_data,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
    out["reference_journal"] = reference_journal
    return out
