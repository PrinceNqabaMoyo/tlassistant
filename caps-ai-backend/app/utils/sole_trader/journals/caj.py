from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import CREDITORS_CONTROL_ALIASES, TRADING_STOCK_ALIASES, find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, choose_journal_identity_layout, fmt_money, journal_editable_cols_by_difficulty, make_journal, round_money
from ..schemas import CAJ_HEADERS


def _make_caj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    creditor = r.choice(["RN Wholesalers", "Sam Distributors", "SA Traders", "Davido Traders"])
    amount = float(r.randrange(250, 3500 + 1, 50))
    variant = r.choice(["cash_payment", "credit_purchase", "cash_purchase"])
    if variant == "cash_payment":
        text = f"Cheque paid to {creditor} in settlement of account, R{amount:.2f}"
        return {"text": text, "journal": "CPJ", "why": "it is a cash payment and not a creditor allowance"}
    if variant == "credit_purchase":
        doc = f"INV{r.randrange(100, 999)}"
        text = f"{doc} Bought trading stock on credit from {creditor}, R{amount:.2f}"
        return {"text": text, "journal": "CJ", "why": "credit purchases are recorded in the Creditors Journal"}
    doc = f"CRR{r.randrange(10, 99)}"
    text = f"{doc} Bought stationery for cash, R{amount:.2f}"
    return {"text": text, "journal": "CPJ", "why": "cash purchases are recorded in the Cash Payments Journal"}


def make_caj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    mode_norm = str(mode or "").strip().lower()

    doc = str(r.choice([301, 302, 303, 304, 305, 318, 329]))
    day = int(r.choice([1, 3, 6, 9, 12, 15, 18, 22, 27]))
    creditor = r.choice(["RN Wholesalers", "Sam Distributors", "SA Traders", "BB Stationery", "MZ Suppliers"])
    fol = r.choice(["C1", "C2", "C3", "C4"])

    kind = r.choice(["return_stock", "return_stationery", "sundry"])

    creditors_control: Optional[float] = None
    trading_stock: Optional[float] = None
    stationery: Optional[float] = None
    sundry_amount: Optional[float] = None
    sundry_details: str = ""

    if kind == "return_stock":
        amount = float(r.choice([180, 240, 320, 450, 600, 820, 1250]))
        creditors_control = amount
        trading_stock = amount
        stationery = None
        sundry_amount = None
        sundry_details = ""
        tx_line = f"{day} {month}: Credit note {doc} received from {creditor} for trading stock returns/allowance, R{amount:.2f}."
    elif kind == "return_stationery":
        amount = float(r.choice([80, 120, 150, 200, 240, 320, 450]))
        creditors_control = amount
        trading_stock = None
        stationery = amount
        sundry_amount = None
        sundry_details = ""
        tx_line = f"{day} {month}: Credit note {doc} received from {creditor} for stationery returns/allowance, R{amount:.2f}."
    else:
        amount = float(r.choice([90, 120, 180, 240, 320, 450, 600]))
        item = r.choice(["Equipment", "Packing material", "Delivery expense", "Telephone"])
        creditors_control = amount
        trading_stock = None
        stationery = None
        sundry_amount = amount
        sundry_details = item
        tx_line = f"{day} {month}: Credit note {doc} received from {creditor} for {item.lower()} returns/allowance, R{amount:.2f}."

    headers = list(CAJ_HEADERS)
    values: List[Optional[str]] = ["" for _ in range(len(headers))]
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    creditor_col = find_col(headers, ["Creditor", "Creditors"])
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, creditor_col],
    )

    if doc_col in identity_layout["prefilled"]:
        values[doc_col] = doc
    if day_col in identity_layout["prefilled"]:
        values[day_col] = str(day)
    if creditor_col in identity_layout["prefilled"]:
        values[creditor_col] = creditor

    fol_col = find_col(headers, ["Fol", "Fol."])
    cc_col = find_col(headers, CREDITORS_CONTROL_ALIASES)
    ts_col = find_col(headers, TRADING_STOCK_ALIASES)
    stat_col = find_col(headers, ["Stationery"])
    sa_col = find_col(headers, ["Sundry amount"])
    sf_col = find_col(headers, ["Sundry fol"])
    sd_col = find_col(headers, ["Sundry details"])

    editable_cols: List[int] = list(identity_layout["editable"])
    for col in [fol_col, cc_col, ts_col, stat_col, sa_col, sf_col, sd_col]:
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
    _set(creditor_col, creditor)
    _set(fol_col, fol if fol_col is not None else "")
    _set(cc_col, fmt_money(round_money(creditors_control)) if creditors_control is not None else "")
    _set(ts_col, fmt_money(round_money(trading_stock)) if trading_stock is not None else "")
    _set(stat_col, fmt_money(round_money(stationery)) if stationery is not None else "")
    _set(sa_col, fmt_money(round_money(sundry_amount)) if sundry_amount is not None else "")
    _set(sf_col, "")
    _set(sd_col, sundry_details)

    if cc_col is not None:
        cell_hints[f"r0_c{cc_col}"] = {
            "title": "Creditors control",
            "steps": [
                "Creditors control is the net amount of the debit note (amount owed decreases).",
                "If there is a trade discount: Net = Gross − trade discount.",
            ],
        }
    if ts_col is not None:
        cell_hints[f"r0_c{ts_col}"] = {
            "title": "Trading stock vs other items",
            "steps": [
                "Trading stock returns/allowances are recorded in the Trading stock analysis column.",
                "If the item is not trading stock or stationery, use Sundry accounts.",
            ],
        }

    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditor", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditors control", "rowSpan": 2, "colSpan": 1},
            {"label": "Trading Stock", "rowSpan": 2, "colSpan": 1},
            {"label": "Stationery", "rowSpan": 2, "colSpan": 1},
            {"label": "Sundry accounts", "rowSpan": 1, "colSpan": 3},
        ],
        [
            {"label": "Amount", "rowSpan": 1, "colSpan": 1},
            {"label": "Fol", "rowSpan": 1, "colSpan": 1},
            {"label": "Details", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    prompt = (
        f"{business}\n"
        f"Creditors Allowances Journal (CAJ) for {month}\n\n"
        "Context:\n"
        f"- {tx_line}\n"
        f"- Folio (Creditors Ledger): {fol}\n\n"
        "Required:\n"
        "Complete the CAJ entry."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["CAJ", "Creditors Allowances Journal", "Creditors Allowances Journal (CAJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="caj",
        table_variant="grade_project",
        headers=headers,
        header_rows=header_rows,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        column_help=headers_to_column_help(journal_type="caj", headers=headers),
        guidelines=[
            "Creditors control is the total of the credit note (amount owed decreases).",
            "Use Trading Stock / Stationery when applicable; otherwise use Sundry accounts (Amount + Details).",
        ],
    )


def make_caj_activity_question(*, r: random.Random, difficulty: str, mode: str, variant_style: str = "activity") -> Dict[str, Any]:
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
    off_journal_item = _make_caj_off_journal_item(r=r)

    creditors = [
        "RN Wholesalers",
        "Sam Distributors",
        "Davido Traders",
        "SA Traders",
        "Santie Limited",
        "Brom Distributors",
        "MN Motors",
    ]

    headers = list(CAJ_HEADERS)
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    creditor_col = find_col(headers, ["Creditor", "Creditors"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    cc_col = find_col(headers, CREDITORS_CONTROL_ALIASES)
    ts_col = find_col(headers, TRADING_STOCK_ALIASES)
    stat_col = find_col(headers, ["Stationery"])
    sa_col = find_col(headers, ["Sundry amount"])
    sf_col = find_col(headers, ["Sundry fol"])
    sd_col = find_col(headers, ["Sundry details"])
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, creditor_col],
    )

    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditor", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditors control", "rowSpan": 2, "colSpan": 1},
            {"label": "Trading Stock", "rowSpan": 2, "colSpan": 1},
            {"label": "Stationery", "rowSpan": 2, "colSpan": 1},
            {"label": "Sundry accounts", "rowSpan": 1, "colSpan": 3},
        ],
        [
            {"label": "Amount", "rowSpan": 1, "colSpan": 1},
            {"label": "Fol", "rowSpan": 1, "colSpan": 1},
            {"label": "Details", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    n_tx = 6 if style_norm == "exam" else int(r.choice([4, 5]))
    days = sorted(r.sample([2, 4, 6, 8, 10, 12, 14, 15, 18, 19, 22, 24, 26, 28, 30], k=n_tx))
    start_doc = int(r.choice([45, 101, 201]))
    docs = [str(start_doc + i) for i in range(n_tx)]

    kinds = ["trading_stock", "stationery", "sundry"]
    tx_rows: List[Dict[str, Any]] = []
    for i in range(n_tx):
        creditor = r.choice(creditors)
        kind = r.choice(kinds)
        trade_disc_pct = float(r.choice([0, 0, 10, 20]))

        ts = None
        st = None
        sundry_amt = None
        sundry_details = ""

        if kind == "trading_stock":
            gross = float(r.randrange(200, 8000 + 1, 100))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            cc = net
            ts = net
            narrative = (
                f"{days[i]} {month}: Debit note {docs[i]} issued to {creditor} for trading stock returns/allowance, "
                f"R{gross:.2f}{' less ' + str(int(trade_disc_pct)) + '% trade discount' if trade_disc_pct else ''}."
            )
        elif kind == "stationery":
            gross = float(r.randrange(80, 2000 + 1, 40))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            cc = net
            st = net
            narrative = (
                f"{days[i]} {month}: Debit note {docs[i]} issued to {creditor} for stationery returns/allowance, "
                f"R{gross:.2f}{' less ' + str(int(trade_disc_pct)) + '% trade discount' if trade_disc_pct else ''}."
            )
        else:
            gross = float(r.randrange(80, 4000 + 1, 40))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            item = r.choice(["Equipment", "Packing material", "Delivery expense", "Telephone", "Drawings"])
            cc = net
            sundry_amt = net
            sundry_details = item
            narrative = (
                f"{days[i]} {month}: Debit note {docs[i]} issued to {creditor} for {item.lower()} returns/allowance, "
                f"R{gross:.2f}{' less ' + str(int(trade_disc_pct)) + '% trade discount' if trade_disc_pct else ''}."
            )

        tx_rows.append({
            "doc": docs[i],
            "day": str(days[i]),
            "creditor": creditor,
            "fol": "",
            "creditors_control": cc,
            "trading_stock": ts,
            "stationery": st,
            "sundry_amount": sundry_amt,
            "sundry_details": sundry_details,
            "narrative": narrative,
        })

    tx_rows.sort(key=lambda t: int(t["doc"]))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}

    def _set(row_index: int, col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r{row_index}_c{col}"] = expected

    totals: Dict[str, float] = {}

    for i, tx in enumerate(tx_rows):
        values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col in identity_layout["prefilled"]:
            values[doc_col] = tx["doc"]
        if day_col in identity_layout["prefilled"]:
            values[day_col] = tx["day"]
        if creditor_col in identity_layout["prefilled"]:
            values[creditor_col] = tx["creditor"]

        editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=list(identity_layout["editable"]) + [c for c in [fol_col, cc_col, ts_col, stat_col, sa_col, sf_col, sd_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        _set(i, doc_col, tx["doc"])
        _set(i, day_col, tx["day"])
        _set(i, creditor_col, tx["creditor"])

        _set(i, fol_col, "")
        _set(i, cc_col, fmt_money(tx["creditors_control"]))
        _set(i, ts_col, fmt_money(tx["trading_stock"]))
        _set(i, stat_col, fmt_money(tx["stationery"]))
        _set(i, sa_col, fmt_money(tx["sundry_amount"]))
        _set(i, sf_col, "")
        _set(i, sd_col, tx["sundry_details"])

        if mode_norm == "scaffold":
            if cc_col is not None:
                cell_hints[f"r{i}_c{cc_col}"] = {
                    "title": "Trade discount (net debit note)",
                    "steps": [
                        "Trade discount is not recorded separately in the books.",
                        "Only the net returns/allowances amount is entered.",
                        "Net = Gross − (Gross × trade discount %).",
                    ],
                }
            if sd_col is not None and tx.get("sundry_details"):
                cell_hints[f"r{i}_c{sd_col}"] = {
                    "title": "When to use Sundry accounts",
                    "steps": [
                        "If the return/allowance is not trading stock or stationery, enter it under Sundry.",
                        "Write the General Ledger account name in Sundry details.",
                    ],
                }

        for key, val in [
            ("Creditors Control", tx["creditors_control"]),
            ("Trading stock", tx["trading_stock"]),
            ("Stationery", tx["stationery"]),
            ("Sundry amount", tx["sundry_amount"]),
        ]:
            if val is not None:
                totals[key] = totals.get(key, 0.0) + float(val)

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col is not None:
            totals_values[doc_col] = "Total"
        totals_editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=[c for c in [cc_col, ts_col, stat_col, sa_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable_cols))
        _set(totals_index, cc_col, fmt_money(totals.get("Creditors Control")))
        _set(totals_index, ts_col, fmt_money(totals.get("Trading stock")))
        _set(totals_index, stat_col, fmt_money(totals.get("Stationery")))
        _set(totals_index, sa_col, fmt_money(totals.get("Sundry amount")))

        if mode_norm == "scaffold":
            for col, title in [
                (cc_col, "Creditors control total"),
                (ts_col, "Trading stock total"),
                (stat_col, "Stationery total"),
                (sa_col, "Sundry total"),
            ]:
                if col is not None:
                    cell_hints[f"r{totals_index}_c{col}"] = {
                        "title": title,
                        "steps": ["Add down the column and enter the total."],
                    }

    transactions_lines = "\n".join([tx["narrative"] for tx in tx_rows] + [off_journal_item["text"]])
    prompt = (
        f"{business}\n"
        f"Creditors Allowances Journal (CAJ) for {month} {year}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Prepare the Creditors Allowances Journal for {month} {year}.{' Do not total/cast off the CAJ.' if not must_total else ''}"
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["CAJ", "Creditors Allowances Journal", "Creditors Allowances Journal (CAJ)"]

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Creditors control is the net amount of the debit note (after any trade discount).",
            "Use Trading Stock / Stationery when applicable; otherwise use Sundry accounts (Amount + Details).",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
        ]
        if must_total:
            guidelines.append("Totals row: add down each money column.")

    return make_journal(
        prompt=prompt,
        journal_type="caj",
        table_variant="studio",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        column_help=headers_to_column_help(journal_type="caj", headers=headers) if mode_norm == "scaffold" else None,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
    )


def make_caj_exam_style_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    return make_caj_activity_question(r=r, difficulty=difficulty, mode=mode, variant_style="exam")
