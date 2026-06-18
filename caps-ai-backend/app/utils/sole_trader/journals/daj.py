from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import COST_OF_SALES_ALIASES, find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, choose_journal_identity_layout, fmt_money, journal_editable_cols_by_difficulty, make_journal, round_money
from ..names import pick_person_name, pick_person_names
from ..schemas import DAJ_HEADERS


def _pick_daj_markup(r: random.Random) -> Dict[str, Any]:
    percent_value = float(r.randrange(30, 111, 5))
    cost_factor = 100.0 / (100.0 + percent_value)
    return {
        "percent_value": percent_value,
        "percent_label": f"{int(percent_value)}",
        "cost_factor": cost_factor,
        "cost_factor_label": f"{cost_factor:.4f}".rstrip("0").rstrip("."),
    }


def _make_daj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    debtor = pick_person_name(r=r)
    amount = float(r.randrange(250, 3200 + 1, 50))
    variant = r.choice(["cash_sale", "credit_sale", "dishonoured_cheque", "bad_debt"])
    if variant == "cash_sale":
        doc = f"CRR{r.randrange(10, 99)}"
        text = f"{doc} Cash sale of goods, R{amount:.2f}"
        return {"text": text, "journal": "CRJ", "why": "cash sales are recorded in the Cash Receipts Journal"}
    if variant == "credit_sale":
        doc = f"INV{r.randrange(100, 999)}"
        text = f"{doc} Sold goods on credit to {debtor}, R{amount:.2f}"
        return {"text": text, "journal": "DJ", "why": "credit sales are recorded in the Debtors Journal"}
    if variant == "dishonoured_cheque":
        text = f"Dishonoured cheque from {debtor} according to the bank statement (B/S), R{amount:.2f}"
        return {"text": text, "journal": "GJ", "why": "a dishonoured cheque reverses a previous receipt and is not a DAJ entry"}
    text = f"Written off bad debt of {debtor}, R{amount:.2f}"
    return {"text": text, "journal": "GJ", "why": "bad debts written off are recorded in the General Journal"}


def make_daj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    mode_norm = str(mode or "").strip().lower()

    doc = str(r.choice([7, 9, 11, 13, 16, 19, 24, 28]))
    day = int(r.choice([2, 4, 6, 9, 12, 15, 18, 22, 27]))
    debtor = pick_person_name(r=r)
    fol = r.choice(["D1", "D2", "D3", "D4"])

    markup = _pick_daj_markup(r)
    markup_pct = float(markup["percent_value"])
    markup_label = str(markup["percent_label"])
    cost_factor = float(markup["cost_factor"])
    cost_factor_label = str(markup["cost_factor_label"])
    prompt_basis = r.choice(["return_allowances_given", "return_cost_given", "allowance_only"])
    if prompt_basis == "return_allowances_given":
        allowances = float(r.choice([180, 240, 320, 450, 600, 820, 1250]))
        cost_of_sales = round_money(allowances * cost_factor)
        note_text = f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        context_line = f"- {day} {month}: Credit note {doc} issued to {debtor} for goods returned on credit. Debtors allowances R{allowances:.2f}."
    elif prompt_basis == "return_cost_given":
        cost_of_sales = float(r.choice([120, 180, 240, 320, 450, 600, 820]))
        allowances = round_money(cost_of_sales * (1.0 + (markup_pct / 100.0)))
        note_text = f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        context_line = f"- {day} {month}: Credit note {doc} issued to {debtor} for goods returned on credit. Cost price of goods returned was R{cost_of_sales:.2f}."
    else:
        allowances = float(r.choice([120, 180, 240, 320, 450, 600, 820]))
        cost_of_sales = None
        note_text = ""
        context_line = f"- {day} {month}: Credit note {doc} issued to {debtor} for an allowance on damaged goods; no goods were returned. Debtors allowances R{allowances:.2f}."

    headers = list(DAJ_HEADERS)
    values: List[Optional[str]] = ["" for _ in range(len(headers))]
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    debtors_col = find_col(headers, ["Debtors", "Debtor"])
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, debtors_col],
    )

    if doc_col in identity_layout["prefilled"]:
        values[doc_col] = doc
    if day_col in identity_layout["prefilled"]:
        values[day_col] = str(day)
    if debtors_col in identity_layout["prefilled"]:
        values[debtors_col] = debtor

    fol_col = find_col(headers, ["Fol", "Fol."])
    da_col = find_col(headers, ["Debtors Allowances", "Debtors allowances"])
    cos_col = find_col(headers, COST_OF_SALES_ALIASES)

    editable_cols: List[int] = list(identity_layout["editable"])
    for col in [fol_col, da_col, cos_col]:
        if col is not None:
            editable_cols.append(col)

    row = build_journal_row(row_index=0, values=values, editable_cols=sorted(set(editable_cols)))

    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}

    def _set(col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r0_c{col}"] = expected

    _set(doc_col, doc)
    _set(day_col, str(day))
    _set(debtors_col, debtor)
    _set(fol_col, fol if fol_col is not None else "")
    _set(da_col, fmt_money(allowances) if da_col is not None else "")
    _set(cos_col, "-" if cost_of_sales is None else fmt_money(cost_of_sales))

    if da_col is not None:
        cell_hints[f"r0_c{da_col}"] = {
            "title": "Debtors allowances",
            "steps": [
                "Debtors allowances is the selling price of the returns/allowance (credit note).",
                f"If the cost price is given for returned goods, Debtors allowances = Cost × (1 + {markup_label}%).",
            ],
        }
    if cos_col is not None:
        if cost_of_sales is None:
            cell_hints[f"r0_c{cos_col}"] = {
                "title": "No cost of sales",
                "steps": [
                    "If only an allowance is granted and no goods are returned, Cost of sales is not applicable.",
                    "Enter '-' in the Cost of sales column.",
                ],
            }
        else:
            cell_hints[f"r0_c{cos_col}"] = {
                "title": "Cost of sales",
                "steps": [
                    "For goods returned, Cost of sales is also reversed.",
                    f"If only the selling price is given and mark-up is used: Cost = Debtors allowances × {cost_factor_label}.",
                ],
            }

    prompt = (
        f"{business}\n"
        f"Debtors Allowances Journal (DAJ) for {month}\n\n"
        f"{note_text}"
        "Context:\n"
        f"{context_line}\n"
        f"- Folio (Debtors Ledger): {fol}\n\n"
        "Required:\n"
        "Complete the DAJ entry."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["DAJ", "Debtors Allowances Journal", "Debtors Allowances Journal (DAJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="daj",
        table_variant="grade_project",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        column_help=headers_to_column_help(journal_type="daj", headers=headers),
        guidelines=(
            [
                "Debtors Allowances is the selling price of the returns/allowance (credit note).",
                "Under the perpetual inventory system, Cost of sales is reversed/recorded in the DAJ for goods returned.",
                "If no goods were returned and only an allowance was granted, enter '-' for Cost of sales.",
            ]
        ),
    )


def make_daj_activity_question(*, r: random.Random, difficulty: str, mode: str, variant_style: str = "activity") -> Dict[str, Any]:
    business = r.choice([
        "Lonely Traders",
        "Ubuntu Traders",
        "Mzanzi Mart",
        "Cape Corner Stores",
        "Gauteng Grocers",
        "Durban Deals",
    ])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013, 2014]))

    mode_norm = str(mode or "").strip().lower()
    style_norm = str(variant_style or "activity").strip().lower()
    must_total = True if style_norm == "exam" else bool(r.choice([True, False]))
    markup = _pick_daj_markup(r)
    markup_label = str(markup["percent_label"])
    cost_factor = float(markup["cost_factor"])
    cost_factor_label = str(markup["cost_factor_label"])
    off_journal_item = _make_daj_off_journal_item(r=r)

    headers = list(DAJ_HEADERS)
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    debtors_col = find_col(headers, ["Debtors", "Debtor"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    da_col = find_col(headers, ["Debtors Allowances", "Debtors allowances", "Debtors' Allowances"])
    cos_col = find_col(headers, COST_OF_SALES_ALIASES)
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, debtors_col],
    )

    used_debtors = pick_person_names(r=r, k=4 if style_norm == "exam" else 3)

    # Ensure we include at least one return (has COS) and one allowance/discount (COS is '-')
    n_tx = 5 if style_norm == "exam" else int(r.choice([3, 4]))
    days = sorted(r.sample([2, 4, 6, 8, 10, 12, 14, 15, 18, 19, 22, 24, 26, 28, 30], k=n_tx))
    start_cn = int(r.choice([24, 25, 26, 12, 13]))
    docs = [str(start_cn + i) for i in range(n_tx)]

    kinds = ["return", "allowance"]
    while len(kinds) < n_tx:
        kinds.append(r.choice(["return", "return", "allowance"]))
    r.shuffle(kinds)

    tx_rows: List[Dict[str, Any]] = []
    for i in range(n_tx):
        debtor = r.choice(used_debtors)
        if kinds[i] == "return":
            allowances = float(r.randrange(80, 1200 + 1, 10))
            cost = round_money(allowances * cost_factor)
            narrative = (
                f"{days[i]} {month}: {debtor} returned goods. Issue credit note {docs[i]}. "
                f"Debtors allowances R{allowances:.2f}."
            )
        else:
            allowances = float(r.randrange(50, 600 + 1, 10))
            cost = None
            narrative = (
                f"{days[i]} {month}: {debtor} was granted an allowance/discount. Issue credit note {docs[i]}. "
                f"Debtors allowances R{allowances:.2f}."
            )

        tx_rows.append({
            "doc": docs[i],
            "day": str(days[i]),
            "debtor": debtor,
            "fol": "",
            "allowances": allowances,
            "cost_of_sales": cost,
            "narrative": narrative,
        })

    tx_rows.sort(key=lambda t: int(t["doc"]))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    off_journal_day = int(r.choice([3, 5, 7, 11, 13, 16, 20, 25, 29]))

    def _set(row_index: int, col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r{row_index}_c{col}"] = expected

    allowances_total = 0.0
    cos_total = 0.0

    for i, tx in enumerate(tx_rows):
        values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col in identity_layout["prefilled"]:
            values[doc_col] = tx["doc"]
        if day_col in identity_layout["prefilled"]:
            values[day_col] = tx["day"]
        if debtors_col in identity_layout["prefilled"]:
            values[debtors_col] = tx["debtor"]

        editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=list(identity_layout["editable"]) + [c for c in [fol_col, da_col, cos_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        _set(i, doc_col, tx["doc"])
        _set(i, day_col, tx["day"])
        _set(i, debtors_col, tx["debtor"])

        _set(i, fol_col, "")
        _set(i, da_col, fmt_money(tx["allowances"]))
        if tx["cost_of_sales"] is None:
            _set(i, cos_col, "-")
            if mode_norm == "scaffold" and cos_col is not None:
                cell_hints[f"r{i}_c{cos_col}"] = {
                    "title": "No cost of sales",
                    "steps": [
                        "If an allowance/discount is granted (no goods returned), Cost of sales is not applicable.",
                        "Enter '-' in the Cost of sales column.",
                    ],
                }
        else:
            _set(i, cos_col, fmt_money(tx["cost_of_sales"]))
            cos_total += float(tx["cost_of_sales"])
            if mode_norm == "scaffold" and cos_col is not None:
                cell_hints[f"r{i}_c{cos_col}"] = {
                    "title": "Cost of sales (returns)",
                    "steps": [
                        f"Only for returns: Cost of sales = Debtors allowances × {cost_factor_label} (mark-up {markup_label}% on cost).",
                    ],
                }

        allowances_total += float(tx["allowances"])

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col is not None:
            totals_values[doc_col] = "Total"
        totals_editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=[c for c in [da_col, cos_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable_cols))
        _set(totals_index, da_col, fmt_money(allowances_total))
        _set(totals_index, cos_col, fmt_money(cos_total))

        if mode_norm == "scaffold":
            if da_col is not None:
                cell_hints[f"r{totals_index}_c{da_col}"] = {
                    "title": "Debtors allowances total",
                    "steps": ["Add down the Debtors allowances column."],
                }
            if cos_col is not None:
                cell_hints[f"r{totals_index}_c{cos_col}"] = {
                    "title": "Cost of sales total",
                    "steps": ["Add only the Cost of sales amounts for returns (ignore '-' entries)."],
                }

    transactions_lines = "\n".join([tx["narrative"] for tx in tx_rows] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])
    prompt = (
        f"{business}\n"
        f"Debtors Allowances Journal (DAJ) for {month} {year}\n\n"
        f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Prepare the Debtors Allowances Journal for {month} {year}.{' Do not total/cast off the DAJ.' if not must_total else ''}"
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["DAJ", "Debtors Allowances Journal", "Debtors Allowances Journal (DAJ)"]

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Debtors Allowances is the selling price of the returns/allowance (credit note).",
            "If an allowance/discount is granted (no goods returned), Cost of sales is not applicable: enter '-'.",
            f"Mark-up of {markup_label}% on cost means: Cost of sales = Debtors Allowances × {cost_factor_label} (for returns).",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
        ]
        if must_total:
            guidelines.append("Totals row: add down the Debtors Allowances column; add Cost of sales for returns only.")

    return make_journal(
        prompt=prompt,
        journal_type="daj",
        table_variant="studio",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        column_help=headers_to_column_help(journal_type="daj", headers=headers) if mode_norm == "scaffold" else None,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
    )


def make_daj_exam_style_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    return make_daj_activity_question(r=r, difficulty=difficulty, mode=mode, variant_style="exam")
