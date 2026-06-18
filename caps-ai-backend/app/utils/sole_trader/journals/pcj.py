from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..aliases import find_col
from ..column_help import headers_to_column_help
from ..core import build_journal_row, choose_journal_identity_layout, fmt_money, journal_editable_cols_by_difficulty, make_journal, round_money
from ..names import pick_business_name, pick_person_name, pick_person_names
from ..schemas import PCJ_HEADERS


def _pcj_expected_text(value: Any) -> str:
    if isinstance(value, list):
        parts = [str(v).strip() for v in value if str(v).strip()]
        return " or ".join(parts)
    return "" if value is None else str(value).strip()


def _pcj_off_journal_rule(item: Optional[Dict[str, str]]) -> str:
    if not item:
        return ""
    text = str(item.get("text") or "").strip()
    journal = str(item.get("journal") or "").strip()
    why = str(item.get("why") or "").strip()
    if not text and not journal and not why:
        return ""
    base = f"{text} does not belong in the PCJ"
    if journal:
        base += f"; record it in the {journal}"
    if why:
        base += f" because {why}"
    return base + "."


def _pcj_extra_row_teaching_hint(*, header_label: str) -> Dict[str, str]:
    header = str(header_label or "cell").strip()
    return {
        "role_in_requirement": f"This {header} cell belongs to an extra distractor row and should stay blank if no further PCJ transaction must be recorded.",
        "evidence_from_question": "Count how many transactions actually belong in the PCJ and compare that with the rows provided in the table.",
        "rule_or_principle": "Only small petty-cash payments supported by petty cash vouchers are entered in the PCJ. Extra unused rows stay blank.",
        "how_to_derive": "Record the valid petty-cash transactions first. If all valid entries are complete, leave the extra row blank.",
        "transfer_tip": "In similar journal questions, an extra blank row may be included as a distractor to test whether you know that no additional PCJ entry is required.",
    }


def _build_pcj_teaching_hint(
    *,
    header_label: str,
    expected: Any,
    transaction_line: str,
    row_type: str = "entry",
    off_journal_item: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    if row_type == "extra":
        return _pcj_extra_row_teaching_hint(header_label=header_label)

    header = str(header_label or "").strip()
    header_norm = header.lower()
    expected_text = _pcj_expected_text(expected)
    tx_text = str(transaction_line or "").strip()
    off_journal_rule = _pcj_off_journal_rule(off_journal_item)

    role = f"This cell records the {header or 'required PCJ detail'} for the petty-cash payment row."
    evidence = f"Use the petty-cash transaction wording: {tx_text}" if tx_text else "Use the petty-cash transaction details given in the question."
    rule = "The PCJ records small cash payments made out of the petty-cash box using petty cash vouchers."
    method = "Identify the petty cash voucher, then place the amount in the correct analysis column or under Sundry accounts."
    transfer_tip = "In similar questions, first decide whether the payment belongs in Postage, Stationery, or Sundry before filling in the money columns."

    if header_norm == "doc":
        role = "This cell records the petty cash voucher number used as the source document."
        rule = "Use the petty cash voucher number in numerical order where possible."
        method = f"Copy the petty cash voucher number given in the transaction. Here it is {expected_text}." if expected_text else method
        transfer_tip = "In similar questions, PCJ source documents are petty cash vouchers, not invoices, receipts, or cheque numbers."
    elif header_norm == "day":
        role = "This cell records the day of the month on which the petty-cash payment happened."
        rule = "The Day column shows the transaction day, not the voucher number."
        method = f"Copy the transaction day into the Day column. Here it is {expected_text}." if expected_text else method
    elif header_norm == "details":
        role = "This cell records what the petty cash was paid for."
        rule = "Details should name the account or item being paid, such as Postage, Stationery, Debtors control, Wages, or Trading stock."
        method = f"Read what was paid for, then enter that label. Here it is {expected_text}." if expected_text else method
    elif header_norm in {"fol", "fol."}:
        role = "This cell records a folio reference when one is required."
        rule = "Use a folio only when the question gives or implies a ledger posting reference. Otherwise it can stay blank."
        method = f"Enter the folio only if one is required by the transaction. Here it is {expected_text or 'blank'}."
        transfer_tip = "In similar questions, the ordinary Fol column is often blank, while debtor-related or sundry folios are only used when a ledger reference is provided."
    elif header_norm == "petty cash":
        role = "This cell records the total amount paid out for the petty cash voucher."
        rule = "Petty cash equals the full amount paid out and must be analysed into one of the other columns."
        method = f"Use the total amount on the voucher. Here it is {expected_text}." if expected_text else method
    elif header_norm == "postage":
        role = "This cell records postage payments analysed from the petty cash amount."
        rule = "Use the Postage column only for mailing or parcel expenses."
        method = f"If the payment is for postage, copy the amount here. Here it is {expected_text or 'blank because this row is not a postage payment'}."
    elif header_norm == "stationery":
        role = "This cell records stationery payments analysed from the petty cash amount."
        rule = "Use the Stationery column only for stationery bought from petty cash."
        method = f"If the payment is for stationery, copy the amount here. Here it is {expected_text or 'blank because this row is not a stationery payment'}."
    elif header_norm == "sundry amount":
        role = "This cell records petty-cash payments that do not belong in the Postage or Stationery analysis columns."
        rule = "Use Sundry amount when there is no special analysis column for that petty-cash payment."
        method = f"Enter the petty-cash amount under Sundry if the payment is not Postage or Stationery. Here it is {expected_text or 'blank because another analysis column is used'}."
    elif header_norm == "sundry fol":
        role = "This cell can record a ledger folio for the sundry account when required."
        rule = "Enter a sundry folio only if a ledger reference is provided or required; otherwise leave it blank."
        method = f"Use the given folio if one is supplied. Here it is {expected_text or 'blank'}."
    elif header_norm == "sundry details":
        role = "This cell names the General Ledger account used for the sundry petty-cash payment."
        rule = "Sundry details explains what account will later be posted for the sundry amount."
        method = f"Write the account name for the sundry payment. Here it is {expected_text or 'blank because another analysis column is used'}."

    if off_journal_rule:
        rule = f"{rule} {off_journal_rule}".strip()
        method = f"{method} Ignore the off-journal item when completing the PCJ table.".strip()

    return {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }


def _make_pcj_off_journal_item(*, r: random.Random) -> Dict[str, str]:
    supplier = pick_business_name(r=r)
    amount = float(r.randrange(150, 2000 + 1, 50))
    variant = r.choice(["cash_sale", "credit_purchase", "restore_float", "credit_sale"])
    if variant == "cash_sale":
        doc = f"CRR{r.randrange(10, 99)}"
        text = f"{doc} Cash sale of goods, R{amount:.2f}"
        return {"text": text, "journal": "CRJ", "why": "cash receipts are recorded in the CRJ, not in the PCJ"}
    if variant == "credit_purchase":
        doc = f"INV{r.randrange(100, 999)}"
        text = f"{doc} Bought trading stock on credit from {supplier}, R{amount:.2f}"
        return {"text": text, "journal": "CJ", "why": "credit purchases are recorded in the CJ, not in the PCJ"}
    if variant == "restore_float":
        cheque_no = f"{r.randrange(120, 299)}"
        text = f"Cheque no. {cheque_no} drawn to restore the petty cash float, R{amount:.2f}"
        return {"text": text, "journal": "CPJ", "why": "the cheque issued to restore petty cash is first recorded in the CPJ"}
    debtor = pick_person_name(r=r)
    doc = f"INV{r.randrange(100, 999)}"
    text = f"{doc} Sold goods on credit to {debtor}, R{amount:.2f}"
    return {"text": text, "journal": "DJ", "why": "credit sales are recorded in the DJ, not in the PCJ"}


def make_pcj_single_row_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    mode_norm = str(mode or "").strip().lower()

    doc = str(r.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    day = int(r.choice([1, 3, 6, 9, 12, 15, 18, 22, 27]))
    kind = r.choice(["postage", "stationery", "trading_stock", "wages", "debtors_control"])
    off_journal_item = _make_pcj_off_journal_item(r=r)
    off_journal_day = int(r.choice([2, 5, 7, 10, 16, 19, 23, 27]))

    petty_cash: float
    postage: Optional[float] = None
    stationery: Optional[float] = None
    sundry_amount: Optional[float] = None
    sundry_details: str = ""
    fol = ""

    if kind == "postage":
        amount = float(r.choice([20, 35, 50, 80, 100, 120, 150]))
        petty_cash = amount
        postage = amount
        details = "Postage"
        tx_line = f"{day} {month}: Paid postage from petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
    elif kind == "stationery":
        amount = float(r.choice([25, 40, 60, 85, 110, 150, 200]))
        petty_cash = amount
        stationery = amount
        details = "Stationery"
        tx_line = f"{day} {month}: Bought stationery with petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
    elif kind == "debtors_control":
        debtor = pick_person_name(r=r)
        debtor_folio = f"DL{r.randrange(1, 10)}"
        amount = float(r.choice([120, 150, 180, 200, 250, 300]))
        petty_cash = amount
        sundry_amount = amount
        sundry_details = "Debtors control"
        details = "Debtors control"
        fol = debtor_folio
        tx_line = f"{day} {month}: Paid carriage fees of R{amount:.2f} from petty cash on behalf of debtor {debtor} ({debtor_folio}). Issue petty cash voucher {doc}."
    elif kind == "trading_stock":
        amount = float(r.choice([80, 120, 150, 180, 200, 250]))
        petty_cash = amount
        sundry_amount = amount
        sundry_details = "Trading stock"
        details = "Trading stock"
        tx_line = f"{day} {month}: Bought trading stock with petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
    else:
        amount = float(r.choice([60, 90, 120, 150, 180, 220]))
        petty_cash = amount
        sundry_amount = amount
        sundry_details = "Wages"
        details = "Wages"
        tx_line = f"{day} {month}: Paid a cleaner from petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."

    headers = list(PCJ_HEADERS)
    values: List[Optional[str]] = ["" for _ in range(len(headers))]
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}

    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    details_col = find_col(headers, ["Details"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    pc_col = find_col(headers, ["Petty cash"])
    post_col = find_col(headers, ["Postage"])
    stat_col = find_col(headers, ["Stationery"])
    sa_col = find_col(headers, ["Sundry amount"])
    sf_col = find_col(headers, ["Sundry fol"])
    sd_col = find_col(headers, ["Sundry details"])
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, details_col],
    )

    if doc_col in identity_layout["prefilled"]:
        values[doc_col] = doc
    if day_col in identity_layout["prefilled"]:
        values[day_col] = str(day)
    if details_col in identity_layout["prefilled"]:
        values[details_col] = details

    editable_cols: List[int] = list(identity_layout["editable"])
    for col in [fol_col, pc_col, post_col, stat_col, sa_col, sf_col, sd_col]:
        if col is not None:
            editable_cols.append(col)

    row = build_journal_row(row_index=0, values=values, editable_cols=sorted(set(editable_cols)))
    correct_map: Dict[str, Any] = {}

    def _set(col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r0_c{col}"] = expected

    _set(doc_col, doc)
    _set(day_col, str(day))
    _set(details_col, details)
    _set(fol_col, fol)
    _set(pc_col, fmt_money(round_money(petty_cash)))
    _set(post_col, fmt_money(round_money(postage)) if postage is not None else "")
    _set(stat_col, fmt_money(round_money(stationery)) if stationery is not None else "")
    _set(sa_col, fmt_money(round_money(sundry_amount)) if sundry_amount is not None else "")
    _set(sf_col, "")
    _set(sd_col, sundry_details)

    if pc_col is not None:
        cell_hints[f"r0_c{pc_col}"] = {
            "title": "Petty cash",
            "steps": [
                "Petty cash is the total amount paid out for the voucher.",
                "The same amount must be analysed into Postage, Stationery, or Sundry.",
            ],
        }
    if kind == "debtors_control":
        if details_col is not None:
            cell_hints[f"r0_c{details_col}"] = {
                "title": "Paid on behalf of a debtor",
                "steps": [
                    "Because the payment was made on behalf of a debtor, record it under Sundry accounts.",
                    "Use 'Debtors control' in Details / Sundry details as required by the table format.",
                ],
            }
        if fol_col is not None:
            cell_hints[f"r0_c{fol_col}"] = {
                "title": "Debtors ledger folio",
                "steps": [
                    "Use the debtor folio/reference that is given with the debtor name.",
                ],
            }
    if kind == "postage" and post_col is not None:
        cell_hints[f"r0_c{post_col}"] = {
            "title": "Postage",
            "steps": [
                "Postage refers to mailing or parcel costs.",
                "Analyse the petty-cash payment into the Postage column.",
            ],
        }
    if kind == "stationery" and stat_col is not None:
        cell_hints[f"r0_c{stat_col}"] = {
            "title": "Stationery",
            "steps": [
                "Stationery refers to consumables such as paper, pens, and files.",
                "Analyse the petty-cash payment into the Stationery column.",
            ],
        }
    if kind in {"trading_stock", "wages", "debtors_control"}:
        if sa_col is not None:
            cell_hints[f"r0_c{sa_col}"] = {
                "title": "Sundry amount",
                "steps": [
                    "Use Sundry amount when the payment is not Postage or Stationery.",
                    "The Sundry amount equals the Petty cash amount for that voucher.",
                ],
            }
        if sd_col is not None:
            cell_hints[f"r0_c{sd_col}"] = {
                "title": "Sundry details",
                "steps": [
                    "Write the General Ledger account name for the sundry petty-cash payment.",
                ],
            }

    for c_idx, header in enumerate(headers):
        cell_id = f"r0_c{c_idx}"
        if cell_id not in correct_map:
            continue
        cell_teaching_map[cell_id] = _build_pcj_teaching_hint(
            header_label=header,
            expected=correct_map[cell_id],
            transaction_line=tx_line,
            off_journal_item=off_journal_item,
        )

    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Details", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Petty cash", "rowSpan": 2, "colSpan": 1},
            {"label": "Postage", "rowSpan": 2, "colSpan": 1},
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
        f"Petty Cash Journal (PCJ) for {month}\n\n"
        "Transactions:\n"
        f"- {tx_line}\n"
        f"- {off_journal_day} {month}: {off_journal_item['text']}\n\n"
        "Required:\n"
        "Complete the PCJ entry for the petty-cash transaction only. Ignore the transaction that belongs in another journal."
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = month
    correct_map["title_journal"] = ["PCJ", "Petty Cash Journal", "Petty Cash Journal (PCJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="pcj",
        table_variant="grade_project",
        headers=headers,
        header_rows=header_rows,
        rows=[row],
        correct_map=correct_map,
        title_fields=title_fields,
        cell_hints=cell_hints if cell_hints else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="pcj", headers=headers),
        guidelines=[
            "Petty cash is the total amount paid from the petty cash float.",
            "Post the amount to the correct analysis column (Postage/Stationery) or Sundry accounts.",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
            "Imprest system: petty cash is kept at a fixed amount; a cheque is drawn in the CPJ to restore the float.",
        ],
    )


def make_pcj_activity11_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
    variant_style: str = "activity",
) -> Dict[str, Any]:
    mode_norm = str(mode or "").strip().lower()
    style_norm = str(variant_style or "activity").strip().lower()
    business = pick_business_name(r=r)
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    year = int(r.choice([2010, 2011, 2012, 2013]))
    must_total = True if style_norm == "exam" else bool(r.choice([True, False]))
    off_journal_item = _make_pcj_off_journal_item(r=r)
    off_journal_day = int(r.choice([3, 6, 9, 11, 17, 21, 24, 28]))

    n_tx = 6 if style_norm == "exam" else int(r.choice([4, 5]))
    base_docs = int(r.choice([70, 71, 72, 73, 74, 75, 76, 77]))
    doc_numbers = [str(base_docs + i) for i in range(n_tx)]
    day_pool = [4, 8, 12, 15, 18, 21, 24, 27, 30]
    days = sorted(r.sample(day_pool, k=n_tx))

    debtor_names = pick_person_names(r=r, k=3 if style_norm == "exam" else 2)
    debtors = [(name, f"DL{idx + 2}") for idx, name in enumerate(debtor_names)]

    tx_kinds = ["stationery", "postage", "debtors_control"]
    extra_kinds = ["trading_stock", "wages", "cleaning_materials", "courier", "stationery", "postage"]
    while len(tx_kinds) < n_tx:
        tx_kinds.append(r.choice(extra_kinds))
    r.shuffle(tx_kinds)

    tx_rows: List[Dict[str, Any]] = []
    for i, kind in enumerate(tx_kinds):
        doc = doc_numbers[i]
        day = str(days[i])
        details = ""
        fol = ""
        petty_cash = 0.0
        postage: Optional[float] = None
        stationery: Optional[float] = None
        sundry_amount: Optional[float] = None
        sundry_details = ""
        narrative = ""

        if kind == "stationery":
            amount = float(r.choice([60, 80, 120, 150, 180, 230]))
            petty_cash = amount
            stationery = amount
            details = "Stationery"
            narrative = f"{day} {month}: Bought stationery with petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
        elif kind == "postage":
            amount = float(r.choice([50, 60, 78, 90, 110, 150]))
            petty_cash = amount
            postage = amount
            details = "Postage"
            narrative = f"{day} {month}: Paid postage from petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
        elif kind == "debtors_control":
            debtor_name, debtor_fol = r.choice(debtors)
            amount = float(r.choice([120, 150, 180, 200, 250, 300]))
            petty_cash = amount
            sundry_amount = amount
            sundry_details = "Debtors control"
            details = "Debtors control"
            fol = debtor_fol
            narrative = f"{day} {month}: Paid carriage fees of R{amount:.2f} from petty cash on behalf of debtor {debtor_name} ({debtor_fol}). Issue petty cash voucher {doc}."
        elif kind == "trading_stock":
            amount = float(r.choice([150, 180, 200, 250, 300]))
            petty_cash = amount
            sundry_amount = amount
            sundry_details = "Trading stock"
            details = "Trading stock"
            narrative = f"{day} {month}: Bought trading stock with petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
        elif kind == "wages":
            amount = float(r.choice([120, 150, 180, 200]))
            petty_cash = amount
            sundry_amount = amount
            sundry_details = "Wages"
            details = "Wages"
            narrative = f"{day} {month}: Paid a cleaner from petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
        elif kind == "cleaning_materials":
            amount = float(r.choice([70, 90, 120, 150, 180]))
            petty_cash = amount
            sundry_amount = amount
            sundry_details = "Cleaning materials"
            details = "Cleaning materials"
            narrative = f"{day} {month}: Bought cleaning materials with petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."
        else:
            amount = float(r.choice([60, 80, 110, 140, 180]))
            petty_cash = amount
            sundry_amount = amount
            sundry_details = "Courier"
            details = "Courier"
            narrative = f"{day} {month}: Paid courier charges from petty cash. Issue petty cash voucher {doc}. Amount R{amount:.2f}."

        tx_rows.append({
            "doc": doc,
            "day": day,
            "details": details,
            "fol": fol,
            "petty_cash": petty_cash,
            "postage": postage,
            "stationery": stationery,
            "sundry_amount": sundry_amount,
            "sundry_fol": "",
            "sundry_details": sundry_details,
            "kind": kind,
            "narrative": narrative,
        })

    tx_rows.sort(key=lambda t: int(str(t["doc"]).strip()))

    headers = list(PCJ_HEADERS)
    doc_col = find_col(headers, ["Doc"])
    day_col = find_col(headers, ["Day"])
    details_col = find_col(headers, ["Details"])
    fol_col = find_col(headers, ["Fol", "Fol."])
    pc_col = find_col(headers, ["Petty cash"])
    post_col = find_col(headers, ["Postage"])
    stat_col = find_col(headers, ["Stationery"])
    sa_col = find_col(headers, ["Sundry amount"])
    sf_col = find_col(headers, ["Sundry fol"])
    sd_col = find_col(headers, ["Sundry details"])
    identity_layout = choose_journal_identity_layout(
        r=r,
        mode=mode_norm,
        difficulty=difficulty,
        identity_cols=[doc_col, day_col, details_col],
    )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, Any] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    totals: Dict[str, float] = {"Petty cash": 0.0, "Postage": 0.0, "Stationery": 0.0, "Sundry amount": 0.0}

    body = tx_rows

    def _set(row_index: int, col: Optional[int], expected: Any) -> None:
        if col is None:
            return
        correct_map[f"r{row_index}_c{col}"] = expected

    for i, tx in enumerate(body):
        expected_tx = tx_rows[i]
        values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if doc_col in identity_layout["prefilled"]:
            values[doc_col] = str(expected_tx.get("doc", ""))
        if day_col in identity_layout["prefilled"]:
            values[day_col] = str(expected_tx.get("day", ""))
        if details_col in identity_layout["prefilled"]:
            values[details_col] = str(expected_tx.get("details", ""))
        if fol_col is not None:
            values[fol_col] = ""
        if sf_col is not None:
            values[sf_col] = ""

        editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=list(identity_layout["editable"]) + [c for c in [fol_col, pc_col, post_col, stat_col, sa_col, sf_col, sd_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=i, values=values, editable_cols=editable_cols))

        # Marking: always mark amounts and the structural fields, but allow practice table to be empty.
        _set(i, doc_col, expected_tx.get("doc", ""))
        _set(i, day_col, expected_tx.get("day", ""))
        _set(i, details_col, expected_tx.get("details", ""))
        _set(i, fol_col, expected_tx.get("fol", ""))

        _set(i, pc_col, fmt_money(round_money(float(expected_tx["petty_cash"]))))
        _set(i, post_col, fmt_money(round_money(float(expected_tx["postage"]))) if expected_tx.get("postage") is not None else "")
        _set(i, stat_col, fmt_money(round_money(float(expected_tx["stationery"]))) if expected_tx.get("stationery") is not None else "")
        _set(i, sa_col, fmt_money(round_money(float(expected_tx["sundry_amount"]))) if expected_tx.get("sundry_amount") is not None else "")
        _set(i, sf_col, "")
        _set(i, sd_col, expected_tx.get("sundry_details", ""))

        totals["Petty cash"] += float(expected_tx.get("petty_cash") or 0.0)
        totals["Postage"] += float(expected_tx.get("postage") or 0.0)
        totals["Stationery"] += float(expected_tx.get("stationery") or 0.0)
        totals["Sundry amount"] += float(expected_tx.get("sundry_amount") or 0.0)

        if mode_norm == "scaffold":
            if i == 0 and doc_col is not None:
                cell_hints[f"r{i}_c{doc_col}"] = {
                    "title": "Petty cash voucher (Doc)",
                    "steps": [
                        "Doc is the petty cash voucher number (source document).",
                        "Vouchers are usually recorded in numerical order.",
                    ],
                }

            if pc_col is not None:
                cell_hints[f"r{i}_c{pc_col}"] = {
                    "title": "Petty cash",
                    "steps": [
                        "Petty cash is the total amount paid out for the voucher.",
                        "The same amount must appear in one analysis column or under Sundry.",
                    ],
                }

            if expected_tx.get("kind") == "debtors_control":
                if details_col is not None:
                    cell_hints[f"r{i}_c{details_col}"] = {
                        "title": "Carriage paid on behalf of a debtor",
                        "steps": [
                            "Carriage is a delivery/transport cost.",
                            "Because it was paid on behalf of a debtor, the amount must be debited to Debtors control.",
                            "Enter the amount under Sundry accounts and write 'Debtors control' in Sundry details.",
                        ],
                    }
                if fol_col is not None:
                    cell_hints[f"r{i}_c{fol_col}"] = {
                        "title": "Debtors ledger folio",
                        "steps": [
                            "Use the debtor’s folio/reference (from the Debtors Ledger) when given.",
                        ],
                    }
            if expected_tx.get("kind") in {"trading_stock", "wages"}:
                if sa_col is not None and sd_col is not None:
                    cell_hints[f"r{i}_c{sa_col}"] = {
                        "title": "Sundry accounts",
                        "steps": [
                            "If the transaction is not Postage or Stationery, enter it under Sundry accounts.",
                            "Sundry amount = Petty cash for that voucher.",
                        ],
                    }
                    cell_hints[f"r{i}_c{sd_col}"] = {
                        "title": "Sundry details",
                        "steps": [
                            "Write the General Ledger account name (e.g. Trading stock / Wages).",
                        ],
                    }

            if expected_tx.get("kind") == "postage":
                if details_col is not None:
                    cell_hints[f"r{i}_c{details_col}"] = {
                        "title": "Postage",
                        "steps": [
                            "Postage refers to mailing/parcel costs (e.g., Post Office).",
                            "Because there is an analysis column for Postage, the amount is recorded in that column.",
                        ],
                    }
                if post_col is not None:
                    cell_hints[f"r{i}_c{post_col}"] = {
                        "title": "Postage analysis column",
                        "steps": [
                            "Enter postage payments here (analyse the petty cash amount).",
                        ],
                    }

            if expected_tx.get("kind") == "stationery":
                if details_col is not None:
                    cell_hints[f"r{i}_c{details_col}"] = {
                        "title": "Stationery",
                        "steps": [
                            "Stationery refers to consumables like paper, pens, files, etc.",
                            "Because there is an analysis column for Stationery, the amount is recorded in that column.",
                        ],
                    }
                if stat_col is not None:
                    cell_hints[f"r{i}_c{stat_col}"] = {
                        "title": "Stationery analysis column",
                        "steps": [
                            "Enter stationery payments here (analyse the petty cash amount).",
                        ],
                    }

        for c_idx, header in enumerate(headers):
            cell_id = f"r{i}_c{c_idx}"
            if cell_id not in correct_map:
                continue
            cell_teaching_map[cell_id] = _build_pcj_teaching_hint(
                header_label=header,
                expected=correct_map[cell_id],
                transaction_line=str(expected_tx.get("narrative") or ""),
                off_journal_item=off_journal_item,
            )

    extra_row_index = len(rows)
    extra_values: List[Optional[str]] = ["" for _ in range(len(headers))]
    extra_editable_cols = journal_editable_cols_by_difficulty(
        difficulty=difficulty,
        base_editable_cols=list(identity_layout["editable"]) + [c for c in [fol_col, pc_col, post_col, stat_col, sa_col, sf_col, sd_col] if c is not None],
        total_cols=len(headers),
    )
    rows.append(build_journal_row(row_index=extra_row_index, values=extra_values, editable_cols=extra_editable_cols))
    for c_idx, header in enumerate(headers):
        _set(extra_row_index, c_idx, "")
        cell_id = f"r{extra_row_index}_c{c_idx}"
        cell_hints[cell_id] = {
            "title": "Extra row not required",
            "steps": [
                "This extra row is a distractor.",
                "If all valid PCJ transactions have already been recorded, leave this row blank.",
            ],
        }
        cell_teaching_map[cell_id] = _build_pcj_teaching_hint(
            header_label=header,
            expected="",
            transaction_line="Extra PCJ distractor row",
            row_type="extra",
            off_journal_item=off_journal_item,
        )

    if must_total:
        totals_index = len(rows)
        totals_values: List[Optional[str]] = ["" for _ in range(len(headers))]
        if pc_col is not None:
            totals_values[pc_col] = fmt_money(round_money(totals["Petty cash"]))
        if post_col is not None:
            totals_values[post_col] = fmt_money(round_money(totals["Postage"]))
        if stat_col is not None:
            totals_values[stat_col] = fmt_money(round_money(totals["Stationery"]))
        if sa_col is not None:
            totals_values[sa_col] = fmt_money(round_money(totals["Sundry amount"]))

        totals_editable_cols = journal_editable_cols_by_difficulty(
            difficulty=difficulty,
            base_editable_cols=[c for c in [pc_col, post_col, stat_col, sa_col] if c is not None],
            total_cols=len(headers),
        )
        rows.append(build_journal_row(row_index=totals_index, values=totals_values, editable_cols=totals_editable_cols))
        _set(totals_index, pc_col, fmt_money(round_money(totals["Petty cash"])))
        _set(totals_index, post_col, fmt_money(round_money(totals["Postage"])))
        _set(totals_index, stat_col, fmt_money(round_money(totals["Stationery"])))
        _set(totals_index, sa_col, fmt_money(round_money(totals["Sundry amount"])))

        if mode_norm == "scaffold":
            for col, title in [
                (pc_col, "Petty cash total"),
                (post_col, "Postage total"),
                (stat_col, "Stationery total"),
                (sa_col, "Sundry total"),
            ]:
                if col is not None:
                    cell_hints[f"r{totals_index}_c{col}"] = {
                        "title": title,
                        "steps": ["Add down the column and enter the total."],
                    }

            if pc_col is not None:
                cell_hints[f"r{totals_index}_c{pc_col}"] = {
                    "title": "Imprest system (petty cash)",
                    "steps": [
                        "Imprest system means the petty cash float is kept at a fixed amount.",
                        "At month-end the totals of the PCJ show how much was spent.",
                        "A cheque is drawn (recorded in the CPJ) to restore petty cash back to the fixed float.",
                    ],
                }

        for col, header in [(pc_col, "Petty cash"), (post_col, "Postage"), (stat_col, "Stationery"), (sa_col, "Sundry amount")]:
            if col is None:
                continue
            cell_id = f"r{totals_index}_c{col}"
            cell_teaching_map[cell_id] = _build_pcj_teaching_hint(
                header_label=header,
                expected=correct_map.get(cell_id),
                transaction_line="Totals row for the PCJ",
                off_journal_item=off_journal_item,
            )

    header_rows = [
        [
            {"label": "Doc", "rowSpan": 2, "colSpan": 1},
            {"label": "Day", "rowSpan": 2, "colSpan": 1},
            {"label": "Details", "rowSpan": 2, "colSpan": 1},
            {"label": "Fol", "rowSpan": 2, "colSpan": 1},
            {"label": "Petty cash", "rowSpan": 2, "colSpan": 1},
            {"label": "Postage", "rowSpan": 2, "colSpan": 1},
            {"label": "Stationery", "rowSpan": 2, "colSpan": 1},
            {"label": "Sundry accounts", "rowSpan": 1, "colSpan": 3},
        ],
        [
            {"label": "Amount", "rowSpan": 1, "colSpan": 1},
            {"label": "Fol", "rowSpan": 1, "colSpan": 1},
            {"label": "Details", "rowSpan": 1, "colSpan": 1},
        ],
    ]

    transactions_lines = "\n".join([str(tx["narrative"]) for tx in tx_rows] + [f"{off_journal_day} {month}: {off_journal_item['text']}"])
    prompt = (
        f"{business}\n"
        f"Petty Cash Journal (PCJ) for {month} {year}\n\n"
        "Transactions:\n"
        f"{transactions_lines}\n\n"
        "Required:\n"
        f"Prepare the Petty Cash Journal for {month} {year}.{' Do not total/cast off the PCJ.' if not must_total else ''}"
    )

    title_fields = [
        {"cell_id": "title_business", "label": "Business name", "editable": True},
        {"cell_id": "title_period", "label": "Month/Year", "editable": True},
        {"cell_id": "title_journal", "label": "Journal", "editable": True},
    ]
    correct_map["title_business"] = business
    correct_map["title_period"] = f"{month} {year}"
    correct_map["title_journal"] = ["PCJ", "Petty Cash Journal", "Petty Cash Journal (PCJ)"]

    return make_journal(
        prompt=prompt,
        journal_type="pcj",
        table_variant="studio",
        headers=headers,
        header_rows=header_rows,
        rows=rows,
        correct_map=correct_map,
        title_fields=title_fields,
        guidelines=[
            "Petty cash is the total paid out for that voucher.",
            "Post to Postage/Stationery if applicable; otherwise use Sundry accounts (Amount + Details).",
            "If paid on behalf of a debtor, the amount is recorded under Sundry and posted to Debtors control.",
            f"Ignore the distractor transaction that belongs in the {off_journal_item['journal']}: {off_journal_item['why']}.",
            "Postage: mailing/parcel costs.",
            "Carriage: delivery/transport costs.",
            "Imprest system: petty cash is kept at a fixed amount; a cheque is drawn to restore the float.",
        ],
        cell_hints=cell_hints if (mode_norm == "scaffold" and cell_hints) else None,
        cell_teaching_map=cell_teaching_map if cell_teaching_map else None,
        column_help=headers_to_column_help(journal_type="pcj", headers=headers) if mode_norm == "scaffold" else None,
    )


def make_pcj_exam_style_question(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    variant_id: Optional[str] = None,
) -> Dict[str, Any]:
    return make_pcj_activity11_question(r=r, difficulty=difficulty, mode=mode, variant_id=variant_id, variant_style="exam")
