from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .column_help import headers_to_column_help
from .core import fmt_money, make_journal, round_money
from .journal_table import build_journal_row
from .names import pick_business_name, pick_business_names, pick_person_names


AccountRow = Dict[str, Any]


def _trial_balance_headers() -> List[str]:
    return [
        "Account",
        "Debit",
        "Credit",
    ]


def _title_fields() -> List[Dict[str, Any]]:
    return [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Statement", "editable": True},
    ]


def _base_trial_balance_guidelines() -> List[str]:
    return [
        "Each account balance must appear once only in the Trial Balance.",
        "Use the debit column for debit balances and the credit column for credit balances.",
        "Leave the opposite money column blank for each account.",
        "Add the debit column and credit column separately to calculate the totals.",
    ]


def _trial_balance_title_answers(*, business: str, month: str, year: int) -> Dict[str, Any]:
    return {
        "title_business": business,
        "title_period": f"{month} {year}",
        "title_journal": ["Trial Balance", "Trial balance", "Trial Balance (TB)"],
    }


def _account_catalog() -> List[Dict[str, Any]]:
    return [
        {"name": "Bank", "side": "debit", "category": "asset", "values": [18250, 22400, 26800, 31550, 40200]},
        {"name": "Trading stock", "side": "debit", "category": "asset", "values": [7400, 8600, 9800, 11200, 12850]},
        {"name": "Debtors control", "side": "debit", "category": "asset", "values": [4200, 5600, 6850, 8120, 9440]},
        {"name": "Equipment", "side": "debit", "category": "asset", "values": [14800, 18600, 22400, 26800]},
        {"name": "Stationery", "side": "debit", "category": "expense", "values": [650, 820, 1050, 1320, 1680]},
        {"name": "Wages", "side": "debit", "category": "expense", "values": [2400, 3200, 4800, 5600, 7200]},
        {"name": "Drawings", "side": "debit", "category": "equity", "values": [900, 1400, 1850, 2400, 3200]},
        {"name": "Rent income", "side": "credit", "category": "income", "values": [600, 850, 1200, 1500, 1800]},
        {"name": "Discount received", "side": "credit", "category": "income", "values": [180, 250, 320, 410]},
        {"name": "Interest on current account", "side": "credit", "category": "income", "values": [120, 180, 240, 360]},
        {"name": "Sales", "side": "credit", "category": "income", "values": [18400, 22600, 28400, 35200, 41800]},
        {"name": "Creditors control", "side": "credit", "category": "liability", "values": [4800, 6200, 7450, 9180, 11200]},
    ]


def _pick_accounts(*, r: random.Random) -> Tuple[List[AccountRow], float]:
    catalog = _account_catalog()
    while True:
        debit_names = {"Bank", "Trading stock", "Debtors control", "Equipment", "Stationery", "Wages", "Drawings"}
        credit_names = {"Sales", "Creditors control", "Rent income", "Discount received", "Interest on current account"}
        chosen_debits = [item for item in catalog if item["name"] in debit_names]
        chosen_credits = [item for item in catalog if item["name"] in credit_names]

        debit_sample = [item for item in chosen_debits if item["name"] in {"Bank", "Trading stock"}]
        other_debits = [item for item in chosen_debits if item["name"] not in {"Bank", "Trading stock"}]
        credit_sample = [item for item in chosen_credits if item["name"] in {"Sales", "Creditors control"}]
        other_credits = [item for item in chosen_credits if item["name"] not in {"Sales", "Creditors control"}]

        selected: List[AccountRow] = []
        selected.extend(debit_sample)
        selected.extend(r.sample(other_debits, k=3))
        selected.extend(credit_sample)
        selected.extend(r.sample(other_credits, k=2))

        rows: List[AccountRow] = []
        debit_total = 0.0
        credit_total = 0.0
        for item in selected:
            amount = float(r.choice(item["values"]))
            row = {
                "name": item["name"],
                "side": item["side"],
                "amount": amount,
                "source": "balance_list",
                "category": item["category"],
            }
            rows.append(row)
            if item["side"] == "debit":
                debit_total += amount
            else:
                credit_total += amount

        capital = round_money(debit_total - credit_total)
        if 30000 <= capital <= 180000:
            rows.append({
                "name": "Capital",
                "side": "credit",
                "amount": capital,
                "source": "balancing_figure",
                "category": "equity",
            })
            return rows, round_money(debit_total)


def _shuffle_entry_rows(*, r: random.Random, rows: Sequence[AccountRow]) -> List[AccountRow]:
    entry_rows = [dict(row) for row in rows]
    r.shuffle(entry_rows)
    return entry_rows


def _entry_row_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    account_name: str,
    account_side: str,
    source_text: str,
    expected_side: str,
) -> Dict[str, str]:
    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = "" if expected is None else str(expected)
    side_label = "debit" if account_side == "debit" else "credit"
    opposite_label = "credit" if account_side == "debit" else "debit"
    role = f"This cell records the {header or 'required Trial Balance detail'} for the account {account_name}."
    evidence = source_text
    rule = "A Trial Balance lists the final ledger balances, placing each account on the side where its balance normally appears."
    method = f"Use the balance given for {account_name} and place it in the {side_label} column only."
    transfer_tip = "In similar questions, identify the account name first, then decide whether its balance belongs in the debit or credit column before writing the amount."

    if header_norm == "account":
        role = "This cell records the ledger account name exactly as it must appear in the Trial Balance."
        rule = "Use the account name exactly as it appears in the extracted balances or supporting list."
        method = f"Copy the account name exactly. Here it is {expected_text or account_name}."
    elif header_norm == "debit":
        role = f"This cell records the debit balance for {account_name} if the account belongs in the debit column."
        if expected_side == "debit":
            rule = f"{account_name} has a debit balance in the Trial Balance."
            method = f"Write the amount in the debit column because {account_name} belongs on the debit side. Here it is {expected_text}."
        else:
            rule = f"{account_name} does not belong in the debit column because its balance is on the {opposite_label} side."
            method = "Leave this debit cell blank because the account balance belongs in the credit column."
    elif header_norm == "credit":
        role = f"This cell records the credit balance for {account_name} if the account belongs in the credit column."
        if expected_side == "credit":
            rule = f"{account_name} has a credit balance in the Trial Balance."
            method = f"Write the amount in the credit column because {account_name} belongs on the credit side. Here it is {expected_text}."
        else:
            rule = f"{account_name} does not belong in the credit column because its balance is on the {opposite_label} side."
            method = "Leave this credit cell blank because the account balance belongs in the debit column."

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def _total_row_teaching_hint(*, header_label: str, expected: Any, column_side: str, source_rows: Sequence[AccountRow]) -> Dict[str, str]:
    header = str(header_label or "").strip()
    expected_text = "" if expected is None else str(expected)
    source_names = ", ".join(row["name"] for row in source_rows if row["side"] == column_side)
    return {
        "role_in_requirement": f"This {header or column_side} cell records the total of the {column_side} column in the Trial Balance.",
        "evidence_from_question": f"Use only the accounts placed in the {column_side} column: {source_names}.",
        "rule_or_principle": f"Add the {column_side} column separately. Do not mix debit and credit balances in one total.",
        "how_to_derive": f"List the {column_side} balances, add them, and enter the final total. Here it is {expected_text}.",
        "transfer_tip": "In similar questions, check each row first, then total the column as the final step.",
    }


def _title_teaching_hint(*, field_id: str, business: str, month: str, year: int) -> Dict[str, str]:
    if field_id == "title_business":
        return {
            "role_in_requirement": "This title field records the business name for the Trial Balance.",
            "evidence_from_question": f"The business named in the prompt is {business}.",
            "rule_or_principle": "The heading of the Trial Balance must identify the business whose balances are being listed.",
            "how_to_derive": f"Copy the business name exactly: {business}.",
            "transfer_tip": "In similar questions, complete the heading before filling in the table so the statement is clearly identified.",
        }
    if field_id == "title_period":
        return {
            "role_in_requirement": "This title field records the month and year of the Trial Balance.",
            "evidence_from_question": f"The Trial Balance is prepared for {month} {year}.",
            "rule_or_principle": "The heading must show the correct period or date for which the balances were extracted.",
            "how_to_derive": f"Copy the period exactly: {month} {year}.",
            "transfer_tip": "In similar questions, use the exact month or date stated in the prompt.",
        }
    return {
        "role_in_requirement": "This title field records the name of the statement.",
        "evidence_from_question": "The required statement is the Trial Balance.",
        "rule_or_principle": "The heading should identify the statement clearly.",
        "how_to_derive": "Write Trial Balance.",
        "transfer_tip": "Use the conventional statement title shown in the question.",
    }


def _make_trial_balance_output(
    *,
    prompt: str,
    business: str,
    month: str,
    year: int,
    difficulty: str,
    mode: str,
    rows_data: Sequence[AccountRow],
    blanked_cells: Sequence[Tuple[int, int]],
    cell_hints: Dict[str, Any],
    derivation_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    headers = _trial_balance_headers()
    diff = str(difficulty or "easy").strip().lower()
    row_ids = {(int(r_idx), int(c_idx)) for r_idx, c_idx in blanked_cells}
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    for row_index, row_data in enumerate(rows_data):
        if row_data.get("row_type") == "total":
            values: List[Optional[str]] = ["Totals", fmt_money(float(row_data["debit_total"])), fmt_money(float(row_data["credit_total"]))]
        else:
            amount = float(row_data["amount"])
            values = [
                str(row_data["name"]),
                fmt_money(amount) if row_data["side"] == "debit" else "",
                fmt_money(amount) if row_data["side"] == "credit" else "",
            ]

        row_editable_cols = [col_index for col_index in range(len(headers)) if (row_index, col_index) in row_ids]
        row = build_journal_row(row_index=row_index, values=values, editable_cols=row_editable_cols)
        rows.append(row)

        for col_index, expected in enumerate(values):
            if (row_index, col_index) not in row_ids:
                continue
            key = f"r{row_index}_c{col_index}"
            correct_map[key] = "" if expected is None else str(expected)

            if row_data.get("row_type") == "total":
                column_side = "debit" if col_index == 1 else "credit"
                if col_index in {1, 2}:
                    cell_teaching_map[key] = _total_row_teaching_hint(
                        header_label=headers[col_index],
                        expected=correct_map[key],
                        column_side=column_side,
                        source_rows=[row for row in rows_data if row.get("row_type") != "total"],
                    )
            else:
                account_name = str(row_data["name"])
                if col_index == 0 and diff == "easy":
                    continue
                cell_teaching_map[key] = _entry_row_teaching_hint(
                    header_label=headers[col_index],
                    expected=correct_map[key],
                    account_name=account_name,
                    account_side=str(row_data["side"]),
                    source_text=str(row_data.get("source_text") or "Use the balance information given in the question."),
                    expected_side=str(row_data["side"]),
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


def make_trial_balance_from_balances_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2024, 2025, 2026]))
    entries, debit_total = _pick_accounts(r=r)
    rows = _shuffle_entry_rows(r=r, rows=entries)

    extracted_lines = []
    for row in rows:
        amount_text = fmt_money(float(row["amount"]))
        side_label = "Dr" if row["side"] == "debit" else "Cr"
        source_text = f"- {row['name']}: {amount_text} ({side_label})"
        row["source_text"] = f"The extracted ledger balance list states: {row['name']} {amount_text} ({side_label})."
        extracted_lines.append(source_text)

    extracted_text = "\n".join(extracted_lines)

    total_credit = round_money(sum(float(row["amount"]) for row in rows if row["side"] == "credit"))
    rows_with_total = [dict(row) for row in rows]
    rows_with_total.append({"row_type": "total", "debit_total": debit_total, "credit_total": total_credit})

    blanked_cells: List[Tuple[int, int]] = []
    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}
    for row_index, row in enumerate(rows):
        blanked_cells.append((row_index, 1))
        blanked_cells.append((row_index, 2))
        if str(difficulty or "easy").strip().lower() in {"medium", "hard"} and row_index in {1, 4, 6}:
            blanked_cells.append((row_index, 0))
        money_key = f"r{row_index}_c{1 if row['side'] == 'debit' else 2}"
        cell_hints[money_key] = f"{row['name']} has a {row['side']} balance, so place the amount in the {row['side']} column only."
        derivation_map[money_key] = f"Use the extracted balance for {row['name']}: {fmt_money(float(row['amount']))} on the {row['side']} side."

    total_row_index = len(rows_with_total) - 1
    blanked_cells.extend([(total_row_index, 1), (total_row_index, 2)])
    cell_hints[f"r{total_row_index}_c1"] = "Debit total: add only the debit balances in the debit column."
    cell_hints[f"r{total_row_index}_c2"] = "Credit total: add only the credit balances in the credit column."
    derivation_map[f"r{total_row_index}_c1"] = f"Add all debit balances to get {fmt_money(debit_total)}."
    derivation_map[f"r{total_row_index}_c2"] = f"Add all credit balances to get {fmt_money(total_credit)}."

    prompt = (
        f"{business}\n"
        f"Trial Balance for {month} {year}\n\n"
        "The following ledger balances were extracted at month end:\n"
        f"{extracted_text}\n\n"
        "Required:\n"
        "Prepare the Trial Balance and calculate the totals of the debit and credit columns."
    )

    return _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        difficulty=difficulty,
        mode=mode,
        rows_data=rows_with_total,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )


def make_trial_balance_partial_completion_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2024, 2025, 2026]))
    entries, debit_total = _pick_accounts(r=r)
    rows = _shuffle_entry_rows(r=r, rows=entries)
    total_credit = round_money(sum(float(row["amount"]) for row in rows if row["side"] == "credit"))

    support_lines = []
    for row in rows:
        amount_text = fmt_money(float(row["amount"]))
        row["source_text"] = f"Use the extracted balance for {row['name']}: {amount_text} on the {row['side']} side."
        support_lines.append(f"- {row['name']}: {amount_text} ({'Dr' if row['side'] == 'debit' else 'Cr'})")

    support_text = "\n".join(support_lines)

    rows_with_total = [dict(row) for row in rows]
    rows_with_total.append({"row_type": "total", "debit_total": debit_total, "credit_total": total_credit})

    diff = str(difficulty or "easy").strip().lower()
    blanked_cells: List[Tuple[int, int]] = []
    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}

    amount_blank_rows = {1, 3, 5}
    name_blank_rows = {2, 6} if diff in {"medium", "hard"} else {2}
    if diff == "hard":
        amount_blank_rows = {0, 1, 3, 4, 5, 7}
        name_blank_rows = {1, 2, 4, 6}

    for row_index, row in enumerate(rows):
        if row_index in name_blank_rows:
            blanked_cells.append((row_index, 0))
            derivation_map[f"r{row_index}_c0"] = f"Copy the account name exactly as listed: {row['name']}."
        if row_index in amount_blank_rows:
            blanked_cells.append((row_index, 1))
            blanked_cells.append((row_index, 2))
            money_key = f"r{row_index}_c{1 if row['side'] == 'debit' else 2}"
            cell_hints[money_key] = f"{row['name']} belongs in the {row['side']} column. Leave the opposite money column blank."
            derivation_map[money_key] = f"Use the given balance for {row['name']}: {fmt_money(float(row['amount']))} in the {row['side']} column."

    total_row_index = len(rows_with_total) - 1
    blanked_cells.extend([(total_row_index, 1), (total_row_index, 2)])
    cell_hints[f"r{total_row_index}_c1"] = "Add the debit column after completing all debit balances."
    cell_hints[f"r{total_row_index}_c2"] = "Add the credit column after completing all credit balances."
    derivation_map[f"r{total_row_index}_c1"] = f"The debit balances total {fmt_money(debit_total)}."
    derivation_map[f"r{total_row_index}_c2"] = f"The credit balances total {fmt_money(total_credit)}."

    prompt = (
        f"{business}\n"
        f"Trial Balance for {month} {year}\n\n"
        "The following balances were extracted from the ledger:\n"
        f"{support_text}\n\n"
        "Required:\n"
        "Complete the partially filled Trial Balance by filling in the missing account names, balances, and totals."
    )

    return _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        difficulty=difficulty,
        mode=mode,
        rows_data=rows_with_total,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )


def make_trial_balance_control_balance_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2024, 2025, 2026]))
    control_kind = r.choice(["debtors", "creditors"])

    if control_kind == "debtors":
        names = pick_person_names(r=r, k=4)
        list_values = [float(r.choice([960, 1240, 1580, 1860, 2240])) for _ in names]
        control_name = "Debtors control"
        control_side = "debit"
        list_heading = "Debtors' List"
        list_lines = [f"- {name}: {fmt_money(value)}" for name, value in zip(names, list_values)]
        control_total = round_money(sum(list_values))
        distractor_name = pick_business_names(r=r, k=1)[0]
        support_note = f"A month-end note also mentioned supplier {distractor_name} in the Creditors Ledger, but that does not change the Debtors control balance."
    else:
        names = pick_business_names(r=r, k=4)
        list_values = [float(r.choice([1180, 1520, 1940, 2280, 2640])) for _ in names]
        control_name = "Creditors control"
        control_side = "credit"
        list_heading = "Creditors' List"
        list_lines = [f"- {name}: {fmt_money(value)}" for name, value in zip(names, list_values)]
        control_total = round_money(sum(list_values))
        distractor_name = pick_person_names(r=r, k=1)[0]
        support_note = f"A month-end note also mentioned debtor {distractor_name} in the Debtors Ledger, but that does not change the Creditors control balance."

    debit_rows: List[AccountRow] = [
        {"name": "Bank", "side": "debit", "amount": float(r.choice([18200, 22400, 26850, 30520])), "source": "balance_list", "source_text": "Use the extracted Bank balance as given."},
        {"name": "Trading stock", "side": "debit", "amount": float(r.choice([7600, 8450, 9320, 10800])), "source": "balance_list", "source_text": "Use the extracted Trading stock balance as given."},
        {"name": "Equipment", "side": "debit", "amount": float(r.choice([14400, 18200, 22600])), "source": "balance_list", "source_text": "Use the extracted Equipment balance as given."},
        {"name": "Stationery", "side": "debit", "amount": float(r.choice([640, 880, 1120, 1460])), "source": "balance_list", "source_text": "Use the extracted Stationery balance as given."},
        {"name": "Drawings", "side": "debit", "amount": float(r.choice([950, 1280, 1640, 2200])), "source": "balance_list", "source_text": "Use the extracted Drawings balance as given."},
    ]
    credit_rows: List[AccountRow] = [
        {"name": "Sales", "side": "credit", "amount": float(r.choice([21400, 25800, 31200, 38600])), "source": "balance_list", "source_text": "Use the extracted Sales balance as given."},
        {"name": "Rent income", "side": "credit", "amount": float(r.choice([720, 980, 1240, 1680])), "source": "balance_list", "source_text": "Use the extracted Rent income balance as given."},
    ]

    if control_kind == "debtors":
        debit_rows.append({
            "name": control_name,
            "side": control_side,
            "amount": control_total,
            "source": "control_list",
            "source_text": f"The {list_heading} totals to {fmt_money(control_total)}, so {control_name} must show the same debit balance.",
        })
        credit_rows.append({"name": "Creditors control", "side": "credit", "amount": float(r.choice([4860, 6250, 7820, 9140])), "source": "balance_list", "source_text": "Use the extracted Creditors control balance as given."})
    else:
        credit_rows.append({
            "name": control_name,
            "side": control_side,
            "amount": control_total,
            "source": "control_list",
            "source_text": f"The {list_heading} totals to {fmt_money(control_total)}, so {control_name} must show the same credit balance.",
        })
        debit_rows.append({"name": "Debtors control", "side": "debit", "amount": float(r.choice([4260, 5580, 6920, 8240])), "source": "balance_list", "source_text": "Use the extracted Debtors control balance as given."})

    debit_sum_before_capital = round_money(sum(float(row["amount"]) for row in debit_rows))
    credit_sum_without_capital = round_money(sum(float(row["amount"]) for row in credit_rows))
    capital_amount = round_money(debit_sum_before_capital - credit_sum_without_capital)
    credit_rows.append({
        "name": "Capital",
        "side": "credit",
        "amount": capital_amount,
        "source": "balance_list",
        "source_text": "Use the extracted Capital balance as given.",
    })

    rows = _shuffle_entry_rows(r=r, rows=debit_rows + credit_rows)
    debit_total = round_money(sum(float(row["amount"]) for row in rows if row["side"] == "debit"))
    credit_total = round_money(sum(float(row["amount"]) for row in rows if row["side"] == "credit"))
    rows_with_total = [dict(row) for row in rows]
    rows_with_total.append({"row_type": "total", "debit_total": debit_total, "credit_total": credit_total})

    control_row_index = next(index for index, row in enumerate(rows) if row["name"] == control_name)
    blanked_cells: List[Tuple[int, int]] = [(control_row_index, 1), (control_row_index, 2)]
    diff = str(difficulty or "easy").strip().lower()
    if diff in {"medium", "hard"}:
        blanked_cells.append((control_row_index, 0))
        for idx in {1, 5}:
            if idx < len(rows):
                blanked_cells.extend([(idx, 1), (idx, 2)])
    total_row_index = len(rows_with_total) - 1
    blanked_cells.extend([(total_row_index, 1), (total_row_index, 2)])

    cell_hints: Dict[str, Any] = {}
    derivation_map: Dict[str, str] = {}
    control_money_key = f"r{control_row_index}_c{1 if control_side == 'debit' else 2}"
    cell_hints[control_money_key] = f"Use the total of the {list_heading} to determine the {control_name} balance."
    derivation_map[control_money_key] = f"Add the balances in the {list_heading}: {fmt_money(control_total)}. That is the {control_name} balance."
    if diff in {"medium", "hard"}:
        derivation_map[f"r{control_row_index}_c0"] = f"The missing account name is {control_name}."
    cell_hints[f"r{total_row_index}_c1"] = "After filling the missing control balance, add all debit balances for the debit total."
    cell_hints[f"r{total_row_index}_c2"] = "After filling the missing control balance, add all credit balances for the credit total."
    derivation_map[f"r{total_row_index}_c1"] = f"The debit column totals {fmt_money(debit_total)} once the control balance is included."
    derivation_map[f"r{total_row_index}_c2"] = f"The credit column totals {fmt_money(credit_total)} once the control balance is included."

    list_text = "\n".join(list_lines)

    prompt = (
        f"{business}\n"
        f"Trial Balance for {month} {year}\n\n"
        f"{list_heading}:\n"
        f"{list_text}\n\n"
        f"{support_note}\n\n"
        "Other extracted ledger balances:\n"
        f"- Bank: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Bank'))} (Dr)\n"
        f"- Trading stock: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Trading stock'))} (Dr)\n"
        f"- Equipment: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Equipment'))} (Dr)\n"
        f"- Stationery: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Stationery'))} (Dr)\n"
        f"- Drawings: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Drawings'))} (Dr)\n"
        f"- Sales: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Sales'))} (Cr)\n"
        f"- Rent income: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Rent income'))} (Cr)\n"
        f"- Capital: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Capital'))} (Cr)\n"
        + (f"- Creditors control: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Creditors control'))} (Cr)\n" if control_kind == 'debtors' else f"- Debtors control: {fmt_money(next(float(row['amount']) for row in rows if row['name'] == 'Debtors control'))} (Dr)\n")
        + "\nRequired:\nUse the subsidiary list to determine the missing control-account balance, then complete the Trial Balance and totals."
    )

    return _make_trial_balance_output(
        prompt=prompt,
        business=business,
        month=month,
        year=year,
        difficulty=difficulty,
        mode=mode,
        rows_data=rows_with_total,
        blanked_cells=blanked_cells,
        cell_hints=cell_hints,
        derivation_map=derivation_map,
    )
