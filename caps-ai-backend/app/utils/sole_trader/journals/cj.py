from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import CREDITORS_CONTROL_ALIASES, TRADING_STOCK_ALIASES, find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, choose_journal_identity_layout, fmt_money, journal_editable_cols_by_difficulty, make_journal, round_money
from ..schemas import CJ_HEADERS


def _make_cj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    creditor = r.choice(["RN Wholesalers", "Sam Distributors", "SA Traders", "Davido Traders"])
    amount = float(r.randrange(250, 3500 + 1, 50))
    variant = r.choice(["cash_payment", "debit_note", "cash_purchase"])
    if variant == "cash_payment":
        text = f"Cheque paid to {creditor} in settlement of account, R{amount:.2f}"
        return {"text": text, "journal": "CPJ", "why": "it is a cash payment and not a credit purchase"}
    if variant == "debit_note":
        doc = f"DN{r.randrange(100, 999)}"
        text = f"{doc} Debit note issued to {creditor} for goods returned, R{amount:.2f}"
        return {"text": text, "journal": "CAJ", "why": "returns to creditors are recorded in the Creditors Allowances Journal"}
    doc = f"CRR{r.randrange(10, 99)}"
    text = f"{doc} Bought trading stock for cash, R{amount:.2f}"
    return {"text": text, "journal": "CPJ", "why": "cash purchases are recorded in the Cash Payments Journal"}


def make_cj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    mode_norm = str(mode or "").strip().lower()

    doc = str(r.choice([101, 102, 103, 104, 105, 121, 135]))
    day = int(r.choice([1, 3, 6, 9, 12, 15, 18, 22, 27]))
    creditor = r.choice(["RN Wholesalers", "Sam Distributors", "SA Traders", "BB Stationery", "MZ Suppliers"])
    fol = r.choice(["C1", "C2", "C3", "C4"])

    kind = r.choice(["buy_stock", "buy_stationery", "sundry"])

    creditors_control: Optional[float] = None
    trading_stock: Optional[float] = None
    stationery: Optional[float] = None
    sundry_amount: Optional[float] = None
    sundry_details: str = ""

    if kind == "buy_stock":
        amount = float(r.choice([950, 1400, 1800, 2400, 3200, 4800, 6500]))
        creditors_control = amount
        trading_stock = amount
        stationery = None
        sundry_amount = None
        sundry_details = ""
        tx_line = f"{day} {month}: Invoice {doc} received from {creditor} for trading stock on credit, R{amount:.2f}."
    elif kind == "buy_stationery":
        amount = float(r.choice([120, 180, 240, 320, 450, 600, 820]))
        creditors_control = amount
        trading_stock = None
        stationery = amount
        sundry_amount = None
        sundry_details = ""
        tx_line = f"{day} {month}: Invoice {doc} received from {creditor} for stationery on credit, R{amount:.2f}."
    else:
        amount = float(r.choice([150, 220, 300, 480, 650, 900, 1200]))
        item = r.choice(["Equipment", "Packing material", "Delivery expense", "Telephone"])
        creditors_control = amount
        trading_stock = None
        stationery = None
        sundry_amount = amount
        sundry_details = item
        tx_line = f"{day} {month}: Invoice {doc} received from {creditor} for {item.lower()} on credit, R{amount:.2f}."

    headers = list(CJ_HEADERS)
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

    # Cell-level help for classification and net invoice amount.
    if cc_col is not None:
        cell_hints[f"r0_c{cc_col}"] = {
            "title": "Creditors control",
            "steps": [
                "Creditors control is the net amount of the invoice (amount owed to the creditor).",
                "If there is a trade discount: Net = Gross − trade discount.",
            ],
        }
    if ts_col is not None:
        cell_hints[f"r0_c{ts_col}"] = {
            "title": "Trading stock vs other items",
            "steps": [
                "Trading stock = goods bought for resale.",
                "If the purchase is not trading stock or stationery, use the Sundry accounts column.",
            ],
        }

    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditor", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditors’ Control", "rowSpan": 2, "colSpan": 1},
            {"label": "Trading stock", "rowSpan": 2, "colSpan": 1},
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
        f"Creditors Journal (CJ) for {month}\n\n"
        "Context:\n"
        f"- {tx_line}\n"
        f"- Folio (Creditors Ledger): {fol}\n\n"
        "Required:\n"
        "Complete the CJ entry."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["CJ", "Creditors Journal", "Creditors Journal (CJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="cj",
        table_variant="grade_project",
        headers=headers,
        header_rows=header_rows,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        column_help=headers_to_column_help(journal_type="cj", headers=headers),
        guidelines=[
            "Creditors’ Control is the total of the invoice (amount owed to the creditor).",
            "Use Trading stock / Stationery when applicable; otherwise use Sundry accounts (Amount + Details).",
        ],
    )


def make_cj_activity_question(*, r: random.Random, difficulty: str, mode: str, variant_style: str = "activity") -> Dict[str, Any]:
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
    off_journal_item = _make_cj_off_journal_item(r=r)

    creditors = [
        "RN Wholesalers",
        "Sam Distributors",
        "Davido Traders",
        "SA Traders",
        "Santie Limited",
        "Brom Distributors",
        "MN Motors",
    ]

    headers = list(CJ_HEADERS)
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

    # Grouped headers (sundry accounts)
    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditor", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Creditors’ Control", "rowSpan": 2, "colSpan": 1},
            {"label": "Trading stock", "rowSpan": 2, "colSpan": 1},
            {"label": "Stationery", "rowSpan": 2, "colSpan": 1},
            {"label": "Sundry accounts", "rowSpan": 1, "colSpan": 3},
        ],
        [
            {"label": "Amount", "rowSpan": 1, "colSpan": 1},
            {"label": "Fol", "rowSpan": 1, "colSpan": 1},
            {"label": "Details", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    n_tx = 7 if style_norm == "exam" else int(r.choice([5, 6]))
    days = sorted(r.sample([1, 3, 4, 6, 7, 9, 11, 12, 15, 17, 18, 22, 24, 27, 28], k=n_tx))
    start_doc = int(r.choice([87, 101, 121]))
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
            gross = float(r.randrange(800, 18000 + 1, 100))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            cc = net
            ts = net
            narrative = (
                f"{days[i]} {month}: Invoice {docs[i]} from {creditor} for trading stock purchased on credit, "
                f"R{gross:.2f}{' less ' + str(int(trade_disc_pct)) + '% trade discount' if trade_disc_pct else ''}."
            )
        elif kind == "stationery":
            gross = float(r.randrange(200, 6000 + 1, 50))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            cc = net
            st = net
            narrative = (
                f"{days[i]} {month}: Invoice {docs[i]} from {creditor} for stationery purchased on credit, "
                f"R{gross:.2f}{' less ' + str(int(trade_disc_pct)) + '% trade discount' if trade_disc_pct else ''}."
            )
        else:
            gross = float(r.randrange(200, 6000 + 1, 50))
            net = round_money(gross * (1.0 - (trade_disc_pct / 100.0)))
            item = r.choice(["Equipment", "Packing material", "Delivery expense", "Telephone", "Drawings"])
            cc = net
            sundry_amt = net
            sundry_details = item
            narrative = (
                f"{days[i]} {month}: Invoice {docs[i]} from {creditor} for {item.lower()} purchased on credit, "
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
            # Trade discount explanation (net purchase).
            if cc_col is not None:
                cell_hints[f"r{i}_c{cc_col}"] = {
                    "title": "Trade discount (net invoice)",
                    "steps": [
                        "Trade discount is not recorded separately in the books.",
                        "Only the net purchases amount is entered.",
                        "Net = Gross − (Gross × trade discount %).",
                    ],
                }
            if sd_col is not None and tx.get("sundry_details"):
                cell_hints[f"r{i}_c{sd_col}"] = {
                    "title": "When to use Sundry accounts",
                    "steps": [
                        "If the purchase is not trading stock or stationery, enter it under Sundry.",
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
        f"Creditors Journal (CJ) for {month} {year}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Prepare the Creditors Journal for {month} {year}.{' Do not total/cast off the CJ.' if not must_total else ''}"
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["CJ", "Creditors Journal", "Creditors Journal (CJ)"]

    guidelines: List[str] = []
    if mode_norm == "scaffold":
        guidelines = [
            "Creditors’ Control is the net amount of the invoice (after any trade discount).",
            "Use Trading stock / Stationery when applicable; otherwise use Sundry accounts (Amount + Details).",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
        ]
        if must_total:
            guidelines.append("Totals row: add down each money column.")

    return make_journal(
        prompt=prompt,
        journal_type="cj",
        table_variant="studio",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        column_help=headers_to_column_help(journal_type="cj", headers=headers) if mode_norm == "scaffold" else None,
        guidelines=guidelines,
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
    )


def make_cj_exam_style_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    return make_cj_activity_question(r=r, difficulty=difficulty, mode=mode, variant_style="exam")
