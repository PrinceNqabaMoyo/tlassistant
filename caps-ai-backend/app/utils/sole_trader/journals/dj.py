from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import COST_OF_SALES_ALIASES, find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, choose_journal_identity_layout, fmt_money, journal_editable_cols_by_difficulty, make_journal, round_money
from ..names import pick_person_name, pick_person_names
from ..schemas import DJ_HEADERS


def _pick_dj_markup(r: random.Random) -> Dict[str, Any]:
    percent_value = float(r.randrange(30, 111, 5))
    cost_factor = 100.0 / (100.0 + percent_value)
    return {
        "percent_value": percent_value,
        "percent_label": f"{int(percent_value)}",
        "cost_factor": cost_factor,
        "cost_factor_label": f"{cost_factor:.4f}".rstrip("0").rstrip("."),
    }


def _make_dj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    debtor = pick_person_name(r=r)
    amount = float(r.randrange(250, 3200 + 1, 50))
    variant = r.choice(["cash_sale", "credit_note", "dishonoured_cheque", "bad_debt"])
    if variant == "cash_sale":
        doc = f"CRR{r.randrange(10, 99)}"
        text = f"{doc} Cash sale of goods, R{amount:.2f}"
        return {"text": text, "journal": "CRJ", "why": "cash sales are recorded in the Cash Receipts Journal"}
    if variant == "credit_note":
        doc = f"CN{r.randrange(100, 999)}"
        text = f"{doc} Issued a credit note to {debtor} for goods returned, R{amount:.2f}"
        return {"text": text, "journal": "DAJ", "why": "credit notes for debtor returns or allowances are recorded in the DAJ"}
    if variant == "dishonoured_cheque":
        text = f"Dishonoured cheque from {debtor} according to the bank statement (B/S), R{amount:.2f}"
        return {"text": text, "journal": "GJ", "why": "a dishonoured cheque reverses a previous receipt and is not a DJ entry"}
    text = f"Written off bad debt of {debtor}, R{amount:.2f}"
    return {"text": text, "journal": "GJ", "why": "bad debts written off are recorded in the General Journal"}


def make_dj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    mode_norm = str(mode or "").strip().lower()

    doc = str(r.choice([12, 14, 18, 21, 25, 31, 42, 56]))
    day = int(r.choice([2, 4, 6, 9, 12, 15, 18, 22, 27]))
    debtor = pick_person_name(r=r)
    fol = r.choice(["D1", "D2", "D3", "D4"])

    markup = _pick_dj_markup(r)
    markup_pct = float(markup["percent_value"])
    markup_label = str(markup["percent_label"])
    cost_factor = float(markup["cost_factor"])
    cost_factor_label = str(markup["cost_factor_label"])
    prompt_basis = r.choice(["sales_given", "cost_given"])
    if prompt_basis == "sales_given":
        sales = float(r.choice([920, 1250, 1840, 2100, 3210, 5050, 6800]))
        cost_of_sales = round_money(sales * cost_factor)
        context_line = f"- {day} {month}: Invoice {doc} issued to {debtor} on credit for R{sales:.2f}."
    else:
        cost_of_sales = float(r.choice([480, 650, 920, 1250, 1840, 2100, 3210]))
        sales = round_money(cost_of_sales * (1.0 + (markup_pct / 100.0)))
        context_line = f"- {day} {month}: Sold goods on credit to {debtor}. Cost price of goods sold was R{cost_of_sales:.2f}. Issue invoice {doc}."

    headers = list(DJ_HEADERS)
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
    sales_col = find_col(headers, ["Sales"])
    cos_col = find_col(headers, COST_OF_SALES_ALIASES)

    editable_cols: List[int] = list(identity_layout["editable"])
    for col in [fol_col, sales_col, cos_col]:
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
    _set(sales_col, fmt_money(sales) if sales_col is not None else "")
    _set(cos_col, fmt_money(cost_of_sales) if cos_col is not None else "")

    if cos_col is not None:
        cell_hints[f"r0_c{cos_col}"] = {
            "title": "Cost of sales",
            "steps": [
                "Under the perpetual inventory system, Cost of sales is recorded in the DJ.",
                f"If only Sales and mark-up are given: Cost = Sales × {cost_factor_label}.",
            ],
        }
    if sales_col is not None:
        cell_hints[f"r0_c{sales_col}"] = {
            "title": "Sales",
            "steps": [
                "The Sales column in the DJ records the selling price of goods sold on credit.",
                f"If the cost price is given instead, Sales = Cost × (1 + {markup_label}%).",
            ],
        }

    prompt = (
        f"{business}\n"
        f"Debtors Journal (DJ) for {month}\n\n"
        f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        "Context:\n"
        f"{context_line}\n"
        f"- Folio (Debtors Ledger): {fol}\n\n"
        "Required:\n"
        "Complete the DJ entry."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["DJ", "Debtors Journal", "Debtors Journal (DJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="dj",
        table_variant="grade_project",
        headers=headers,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        column_help=headers_to_column_help(journal_type="dj", headers=headers),
        guidelines=[
            "Sales is the selling price on credit.",
            "Under the perpetual inventory system, Cost of sales is recorded in the DJ.",
        ],
    )


def make_dj_activity_question(*, r: random.Random, difficulty: str, mode: str, variant_style: str = "activity") -> Dict[str, Any]:
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
    markup = _pick_dj_markup(r)
    markup_label = str(markup["percent_label"])
    cost_factor = float(markup["cost_factor"])
    cost_factor_label = str(markup["cost_factor_label"])
    off_journal_item = _make_dj_off_journal_item(r=r)

    used_debtors = pick_person_names(r=r, k=4 if style_norm == "exam" else 3)

    headers = list(DJ_HEADERS)
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    debtors_col = find_col(headers, ["Debtors", "Debtor"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    sales_col = find_col(headers, ["Sales"])
    cos_col = find_col(headers, COST_OF_SALES_ALIASES)
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, debtors_col],
    )

    n_tx = 6 if style_norm == "exam" else 5
    days = sorted(r.sample([2, 4, 5, 7, 9, 10, 12, 14, 15, 17, 18, 22, 26, 27, 28], k=n_tx))
    start_invoice = int(r.choice([51, 52, 53, 54, 55, 101, 102, 103]))
    docs = [str(start_invoice + i) for i in range(n_tx)]

    tx_rows: List[Dict[str, Any]] = []
    for i in range(n_tx):
        debtor = r.choice(used_debtors)
        kind = r.choice(["sales_given", "sales_given", "cost_given"])
        if kind == "sales_given":
            sales = float(r.randrange(480, 6800 + 1, 10))
            cost = round_money(sales * cost_factor)
            tx_rows.append({
                "doc": docs[i],
                "day": str(days[i]),
                "debtor": debtor,
                "fol": "",
                "sales": sales,
                "cost_of_sales": cost,
                "narrative": f"{days[i]} {month}: Sold goods on credit to {debtor} for R{sales:.2f}. Issue invoice {docs[i]}.",
            })
        else:
            cost = float(r.randrange(300, 4800 + 1, 10))
            sales = round_money(cost * (1.0 + (float(markup["percent_value"]) / 100.0)))
            tx_rows.append({
                "doc": docs[i],
                "day": str(days[i]),
                "debtor": debtor,
                "fol": "",
                "sales": sales,
                "cost_of_sales": cost,
                "narrative": f"{days[i]} {month}: Sold goods on credit to {debtor}. Cost price of goods sold was R{cost:.2f}. Issue invoice {docs[i]}.",
            })

    tx_rows.sort(key=lambda t: int(t["doc"]))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    off_journal_day = int(r.choice([3, 6, 8, 11, 13, 16, 20, 24, 29]))

    def _set(row_index: int, col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r{row_index}_c{col}"] = expected

    sales_total = 0.0
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
            base_editable_cols=list(identity_layout["editable"]) + [c for c in [fol_col, sales_col, cos_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        _set(i, doc_col, tx["doc"])
        _set(i, day_col, tx["day"])
        _set(i, debtors_col, tx["debtor"])

        _set(i, fol_col, "")
        _set(i, sales_col, fmt_money(tx["sales"]))
        _set(i, cos_col, fmt_money(tx["cost_of_sales"]))

        if mode_norm == "scaffold" and cos_col is not None:
            cell_hints[f"r{i}_c{cos_col}"] = {
                "title": "Cost of sales (mark-up)",
                "steps": [
                    f"Mark-up of {markup_label}% on cost means: Cost = Selling price × {cost_factor_label}.",
                    f"So Cost of sales = Sales × {cost_factor_label}.",
                ],
            }

        sales_total += float(tx["sales"])
        cos_total += float(tx["cost_of_sales"])

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col is not None:
            totals_values[doc_col] = "Total"
        totals_editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=[c for c in [sales_col, cos_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable_cols))
        _set(totals_index, sales_col, fmt_money(sales_total))
        _set(totals_index, cos_col, fmt_money(cos_total))

        if mode_norm == "scaffold":
            if sales_col is not None:
                cell_hints[f"r{totals_index}_c{sales_col}"] = {
                    "title": "Sales total",
                    "steps": ["Add down the Sales column."],
                }
            if cos_col is not None:
                cell_hints[f"r{totals_index}_c{cos_col}"] = {
                    "title": "Cost of sales total",
                    "steps": ["Add down the Cost of sales column."],
                }

    transactions_lines = "\n".join([tx["narrative"] for tx in tx_rows] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])
    prompt = (
        f"{business}\n"
        f"Debtors Journal (DJ) for {month} {year}\n\n"
        f"Note: The business uses a mark-up of {markup_label}% on cost price.\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Prepare the Debtors Journal for {month} {year}.{' Do not total/cast off the DJ.' if not must_total else ''}"
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["DJ", "Debtors Journal", "Debtors Journal (DJ)"]

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Sales is the selling price on credit.",
            f"Mark-up of {markup_label}% on cost means: Cost of sales = Selling price × {cost_factor_label}.",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
        ]
        if must_total:
            guidelines.append("Totals row: add down the Sales and Cost of sales columns.")

    return make_journal(
        prompt=prompt,
        journal_type="dj",
        table_variant="studio",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        column_help=headers_to_column_help(journal_type="dj", headers=headers) if mode_norm == "scaffold" else None,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
    )


def make_dj_exam_style_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    return make_dj_activity_question(r=r, difficulty=difficulty, mode=mode, variant_style="exam")
