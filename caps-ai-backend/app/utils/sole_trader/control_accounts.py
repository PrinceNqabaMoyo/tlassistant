
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from .core import fmt_money as _fmt_money
from .core import make_typed as _make_typed
from .core import round_money as _round_money
from .journal_question import make_journal as _make_journal
from .journal_table import build_journal_row as _build_journal_row
from .journal_table import build_prefixed_row as _build_prefixed_row
from .names import pick_business_name, pick_business_names, pick_person_names


class _ControlAccountsScenarioValidationError(ValueError):
    pass


MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS = 20


def _normalize_control_accounts_variant(variant: str) -> str:
    var = str(variant or "debtors").strip().lower()
    return var if var in ("debtors", "creditors") else "debtors"


def _normalize_control_accounts_difficulty(difficulty: str) -> str:
    diff = str(difficulty or "easy").strip().lower()
    return diff if diff in ("easy", "medium", "hard") else "easy"


def _next_month_abbrev(month: str) -> str:
    return {
        "January": "Feb",
        "February": "Mar",
        "March": "Apr",
        "April": "May",
        "May": "Jun",
        "June": "Jul",
        "July": "Aug",
        "August": "Sep",
        "September": "Oct",
        "October": "Nov",
        "November": "Dec",
        "December": "Jan",
        "Jan": "Feb",
        "Feb": "Mar",
        "Mar": "Apr",
        "Apr": "May",
        "Jun": "Jul",
        "Jul": "Aug",
        "Aug": "Sep",
        "Sep": "Oct",
        "Oct": "Nov",
        "Nov": "Dec",
        "Dec": "Jan",
    }.get(month, "Jun")


def _flatten_masked_columns(mask_map: Dict[int, List[int]]) -> List[int]:
    cols = set()
    for values in (mask_map or {}).values():
        for col in values or []:
            cols.add(int(col))
    return sorted(cols)


def _missing_field_labels(mask_map: Dict[int, List[int]]) -> List[str]:
    column_to_label = {
        0: "month",
        1: "day",
        2: "details",
        3: "folios",
        4: "amounts",
        5: "month",
        6: "day",
        7: "details",
        8: "folios",
        9: "amounts",
    }
    labels: List[str] = []
    for col in _flatten_masked_columns(mask_map):
        label = column_to_label.get(col)
        if label and label not in labels:
            labels.append(label)
    return labels


def _join_labels(labels: List[str]) -> str:
    cleaned = [str(label).strip() for label in (labels or []) if str(label).strip()]
    if not cleaned:
        return "missing values"
    if len(cleaned) == 1:
        return cleaned[0]
    if len(cleaned) == 2:
        return f"{cleaned[0]} and {cleaned[1]}"
    return f"{', '.join(cleaned[:-1])} and {cleaned[-1]}"


def _control_account_posting_rule(*, variant: str, folio: str, details: str, side: str) -> str:
    fol = str(folio or "").strip()
    detail_text = str(details or "").strip()
    if detail_text == "Balance c/d":
        return "The closing balance is the amount needed to make the debit and credit totals equal."
    if detail_text == "Balance b/d":
        return "The balance brought down at the start of the next period must be the same amount as the previous Balance c/d."
    if detail_text == "Totals":
        return "A balanced control account has equal debit and credit totals."
    if fol == "DJ":
        return "Credit sales increase Debtors control and are posted on the debit side."
    if fol == "CRJ":
        return (
            "Receipts from debtors reduce Debtors control and are posted on the credit side."
            if variant == "debtors"
            else "A CRJ amount only affects Creditors control when the business receives a refund or has an overpayment adjustment."
        )
    if fol == "DAJ":
        return "Debtors allowances reduce Debtors control and are posted on the credit side."
    if fol == "CJ":
        return "Credit purchases increase Creditors control and are posted on the credit side."
    if fol == "CPJ":
        return (
            "Bank and discount received reduce Creditors control and are posted on the debit side."
            if variant == "creditors"
            else "A CPJ amount in Debtors control usually means the business paid on behalf of a debtor, so the debtor owes more."
        )
    if fol == "CAJ":
        return "Creditors allowances reduce Creditors control and are posted on the debit side."
    if fol == "GJ":
        return f"The General Journal entry must match the adjustment reason and appear on the {side} side shown in the control account."
    if fol in {"b/d", "c/d"}:
        return "The balance lines must agree between the end of one period and the start of the next period."
    return f"Use the source named in the folio to confirm why the posting appears on the {side} side."


def _build_study_cell_guidance(
    *,
    variant: str,
    row_index: int,
    column_index: int,
    answer_values: List[Optional[str]],
    month_abbrev: str,
    next_month_abbrev: str,
) -> Tuple[str, Dict[str, str]]:
    side = "debit" if column_index <= 4 else "credit"
    if column_index <= 4:
        details = str(answer_values[2] or "").strip()
        folio = str(answer_values[3] or "").strip()
        amount = str(answer_values[4] or "").strip()
    else:
        details = str(answer_values[7] or "").strip()
        folio = str(answer_values[8] or "").strip()
        amount = str(answer_values[9] or "").strip()

    col_kind = {
        0: "month",
        1: "day",
        2: "details",
        3: "folio",
        4: "amount",
        5: "month",
        6: "day",
        7: "details",
        8: "folio",
        9: "amount",
    }.get(column_index, "value")

    label = details or folio or f"row {row_index + 1}"
    rule_text = _control_account_posting_rule(variant=variant, folio=folio, details=details, side=side)

    if details == "Balance c/d":
        return (
            f"Balance c/d is the closing balance needed to balance the account on the {side} side.",
            {
                "role_in_requirement": "Calculate the closing balance carried down.",
                "evidence_from_question": "Use the postings already shown for the month, then balance the two sides of the control account.",
                "rule_or_principle": rule_text,
                "how_to_derive": "Add the opposite side first, add the entries already shown on this side, then use the difference as Balance c/d.",
                "transfer_tip": "The same amount must appear as Balance b/d on the first day of the next month.",
            },
        )
    if details == "Balance b/d":
        return (
            "Balance b/d must be copied from the previous Balance c/d without changing the amount.",
            {
                "role_in_requirement": "Carry the closing balance forward to the next period.",
                "evidence_from_question": f"The row dated {next_month_abbrev} 1 is the opening balance row for the next month.",
                "rule_or_principle": rule_text,
                "how_to_derive": "Copy the previous Balance c/d amount exactly.",
                "transfer_tip": "Do not recalculate this balance. Carry it forward unchanged.",
            },
        )
    if details == "Totals":
        return (
            f"Add the {side}-side amounts to complete the totals row.",
            {
                "role_in_requirement": "Enter the total for this side of the control account.",
                "evidence_from_question": "The totals row closes off the ledger account for the month.",
                "rule_or_principle": rule_text,
                "how_to_derive": f"Add every amount already shown on the {side} side, including Balance c/d when it appears on that side.",
                "transfer_tip": "Both totals must be equal after the account is balanced.",
            },
        )
    if col_kind == "details":
        return (
            f"Use the account detail that matches the {folio or 'source'} posting on the {side} side.",
            {
                "role_in_requirement": f"Name the account detail for the {side}-side posting.",
                "evidence_from_question": f"Use the row dated {month_abbrev} and the folio {folio or 'shown in the row'} to identify the posting.",
                "rule_or_principle": rule_text,
                "how_to_derive": "Match the journal or balance label to the description transferred into the control account.",
                "transfer_tip": "Keep the account name in Details and the source abbreviation in Fol.",
            },
        )
    if col_kind == "folio":
        return (
            f"Use the source or ledger folio for the {label} posting.",
            {
                "role_in_requirement": "Enter the folio or source abbreviation for this posting.",
                "evidence_from_question": f"The Details column identifies the posting as {label}.",
                "rule_or_principle": rule_text,
                "how_to_derive": "Use the journal, balance label, or ledger source that produced this posting.",
                "transfer_tip": "Folio abbreviations such as DJ, CRJ, CJ, CPJ, DAJ, CAJ, GJ, b/d and c/d must stay in the Fol column.",
            },
        )
    if col_kind == "amount":
        return (
            f"Use the amount for {label} on the {side} side of the control account.",
            {
                "role_in_requirement": "Enter the amount for this posting.",
                "evidence_from_question": f"Use the source information table and the row labelled {label}.",
                "rule_or_principle": rule_text,
                "how_to_derive": "Transfer the matching amount from the source information table, or calculate it by balancing the account if this row is the balance or totals row.",
                "transfer_tip": "When the row is a balance row, confirm that the next Balance b/d agrees with it.",
            },
        )
    if col_kind == "day":
        return (
            "Copy the day from the matching month-end or opening-balance entry.",
            {
                "role_in_requirement": "Enter the day for this posting.",
                "evidence_from_question": "Use the posting pattern already shown in the table for opening balances or month-end transfers.",
                "rule_or_principle": "Month-end transfers must use the closing date of the accounting period.",
                "how_to_derive": "Match this line to the same day used by the corresponding transfer or balance row.",
                "transfer_tip": "Most month-end transfers in this table use day 31, while opening balances use day 1.",
            },
        )
    if col_kind == "month":
        return (
            "Copy the month from the matching accounting-period row.",
            {
                "role_in_requirement": "Enter the month abbreviation for this posting.",
                "evidence_from_question": "Use the other rows in the control account to see whether this is the current month or the next month.",
                "rule_or_principle": "Balance b/d for the next period uses the next month, while month-end transfers stay in the current month.",
                "how_to_derive": "Match the row to either the current month entries or the next-month opening-balance row.",
                "transfer_tip": "Only the final Balance b/d row changes to the next month.",
            },
        )
    return (
        f"Use the row information for {label} to complete the missing cell on the {side} side.",
        {
            "role_in_requirement": "Complete the missing value in this control-account row.",
            "evidence_from_question": "Use the rest of the row and the source information table.",
            "rule_or_principle": rule_text,
            "how_to_derive": "Match the row to the related source or balancing step.",
            "transfer_tip": "Check that the posting side, folio and amount are consistent with the rest of the account.",
        },
    )


def _validate_control_account_study_prompt(
    *,
    difficulty: str,
    prompt: str,
    month: str,
    year: int,
    account_label: str,
    mask_map: Dict[int, List[int]],
    variant: str,
) -> None:
    prompt_norm = str(prompt or "").lower()
    expected_phrase = (
        f"study the information for {month.lower()} {year} provided in the table and complete the {account_label.lower()} account that follows"
    )
    if expected_phrase not in prompt_norm:
        raise _ControlAccountsScenarioValidationError("Control account study prompt must use the exam-style table wording.")
    if "|" in str(prompt or ""):
        raise _ControlAccountsScenarioValidationError("Control account study prompt must not leak raw table separators.")

    labels = _missing_field_labels(mask_map)
    for label in labels:
        singular = label[:-1] if label.endswith("s") else label
        if label not in prompt_norm and singular not in prompt_norm:
            raise _ControlAccountsScenarioValidationError("Control account study prompt does not match the missing cell types.")

    if difficulty == "easy":
        total_row = 6 if variant == "debtors" else 7
        if not any(int(row_index) != total_row for row_index in (mask_map or {}).keys()):
            raise _ControlAccountsScenarioValidationError("Easy control account study variation must blank more than totals only.")


def _append_control_accounts_teaching_hint(
    *,
    cell_teaching_map: Dict[str, Dict[str, str]],
    cell_key: str,
    role_in_requirement: str = "",
    evidence_from_question: str = "",
    rule_or_principle: str = "",
    how_to_derive: str = "",
    transfer_tip: str = "",
) -> None:
    existing = dict(cell_teaching_map.get(cell_key) or {})
    if role_in_requirement:
        existing["role_in_requirement"] = str(role_in_requirement)
    if evidence_from_question:
        existing["evidence_from_question"] = str(evidence_from_question)
    if rule_or_principle:
        existing["rule_or_principle"] = str(rule_or_principle)
    if how_to_derive:
        existing["how_to_derive"] = str(how_to_derive)
    if transfer_tip:
        existing["transfer_tip"] = str(transfer_tip)
    if existing:
        cell_teaching_map[cell_key] = existing


def _validate_control_account_study_output(
    *,
    variant: str,
    opening: float,
    closing: float,
    debit_total: float,
    credit_total: float,
    correct_map: Dict[str, Any],
) -> None:
    if opening <= 0.0:
        raise _ControlAccountsScenarioValidationError("Control account study question requires a positive opening balance.")
    if closing <= 0.0:
        raise _ControlAccountsScenarioValidationError("Control account study question requires a positive closing balance.")
    if _round_money(debit_total) != _round_money(credit_total):
        raise _ControlAccountsScenarioValidationError("Control account study totals do not balance.")

    closing_text = _fmt_money(closing)
    total_text = _fmt_money(debit_total)
    if variant == "debtors":
        expected_pairs = {
            "t0_r5_c9": closing_text,
            "t0_r6_c4": total_text,
            "t0_r6_c9": total_text,
            "t0_r7_c4": closing_text,
        }
    else:
        expected_pairs = {
            "t0_r6_c4": closing_text,
            "t0_r7_c4": total_text,
            "t0_r7_c9": total_text,
            "t0_r8_c9": closing_text,
        }
    for cell_key, expected_value in expected_pairs.items():
        if str(correct_map.get(cell_key) or "") != str(expected_value):
            raise _ControlAccountsScenarioValidationError(f"Control account study output mismatch at {cell_key}.")


def _build_answer_part_hints(entries: List[Tuple[str, str, List[str]]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for label, value, guidance_lines in entries:
        text_value = str(value or "").strip()
        sections: List[Dict[str, str]] = []
        cleaned_guidance = [str(line).strip() for line in (guidance_lines or []) if str(line).strip()]
        if cleaned_guidance:
            sections.append({
                "title": "How to approach it",
                "text": "\n".join(f"{idx + 1}. {line}" for idx, line in enumerate(cleaned_guidance)),
            })
        if text_value:
            sections.append({"title": "Memo point", "text": text_value})
        out.append({
            "label": str(label or "Answer part").strip(),
            "value": text_value,
            "sections": sections,
        })
    return out


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


def _debtors_creditors_list_headers() -> List[str]:
    return [
        "Name",
        "Debit",
        "Credit",
    ]


def _reconciliation_impact_headers() -> List[str]:
    return [
        "No.",
        "Debtors control (Dr)",
        "Debtors control (Cr)",
        "Debtors list (Dr)",
        "Debtors list (Cr)",
        "Creditors control (Dr)",
        "Creditors control (Cr)",
        "Creditors list (Dr)",
        "Creditors list (Cr)",
    ]


def _old_make_reconciliation_impact_matrix_question(*, r: random.Random, difficulty: Optional[str] = None) -> Dict[str, Any]:
    headers = _reconciliation_impact_headers()

    items: List[Tuple[str, Dict[str, float]]] = []
    items.append(("A credit invoice was recorded twice and posted twice.", {"dc_dr": 0.0, "dc_cr": 200.0, "dl_dr": 0.0, "dl_cr": 200.0}))
    items.append(("The total of the Debtors Journal was undercast.", {"dc_dr": 240.0}))
    items.append(("The total of the Creditors Journal was overcast.", {"cc_cr": 180.0}))
    items.append(("A receipt was posted to the wrong person’s account.", {"dl_cr": 144.0}))
    items.append(("An amount in the debtors control column in the CRJ was not posted.", {"dc_cr": 180.0}))
    r.shuffle(items)
    items = items[: int(r.choice([3, 4, 5]))]

    key_to_col = {
        "dc_dr": 1,
        "dc_cr": 2,
        "dl_dr": 3,
        "dl_cr": 4,
        "cc_dr": 5,
        "cc_cr": 6,
        "cl_dr": 7,
        "cl_cr": 8,
    }

    diff = str(difficulty or "easy").strip().lower()
    editable_cols = list(range(1, len(headers)))
    if diff in ("", "easy"):
        editable_cols = list(range(1, len(headers)))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    prompt_lines = [
        "On reconciliation, indicate how each error affects the control accounts and lists.",
        "Enter the correction amount(s) in the appropriate column(s).",
        "",
        "Errors and omissions:",
    ]

    for i, (txt, impacts) in enumerate(items, start=1):
        prompt_lines.append(f"{i}. {txt}")
        values: List[Optional[str]] = [str(i)] + ["" for _ in range(len(headers) - 1)]
        rows.append(_build_journal_row(row_index=i - 1, values=values, editable_cols=editable_cols))
        correct_map[f"r{i-1}_c0"] = str(i)

        for k, amt in impacts.items():
            if k not in key_to_col:
                continue
            if float(amt) == 0.0:
                continue
            cix = key_to_col[k]
            correct_map[f"r{i-1}_c{cix}"] = _fmt_money(float(amt))

        for c in range(1, len(headers)):
            cell_id = f"r{i-1}_c{c}"
            if cell_id not in correct_map:
                correct_map[cell_id] = ""

    prompt_lines.extend(["", "Required:", "Complete the reconciliation impact table."])

    return _make_journal(
        prompt="\n".join(prompt_lines),
        journal_type="reconciliation_impact",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Journal totals errors affect the control account.",
            "Posting errors to individual accounts affect the list.",
        ],
    )


_RECONCILIATION_IMPACT_KEY_TO_COL = {
    "dc_dr": 1,
    "dc_cr": 2,
    "dl_dr": 3,
    "dl_cr": 4,
    "cc_dr": 5,
    "cc_cr": 6,
    "cl_dr": 7,
    "cl_cr": 8,
}


def _normalize_reconciliation_analysis_difficulty(difficulty: Optional[str]) -> str:
    diff = str(difficulty or "easy").strip().lower()
    return diff if diff in ("easy", "medium", "hard") else "easy"


def _normalize_reconciliation_analysis_row_family(category: str) -> str:
    category_norm = str(category or "").strip().lower()
    if category_norm == "both_control_and_list":
        return "both"
    if category_norm in ("control_only", "list_only", "cross_ledger"):
        return category_norm
    if "both" in category_norm:
        return "both"
    return "control_only"


def _infer_reconciliation_analysis_logic_source(*, spec: Dict[str, Any], row_family: str) -> str:
    spec_id = str(spec.get("id") or "").strip().lower()
    template = str(spec.get("template") or "").strip().lower()
    if row_family == "cross_ledger" or "instead of the creditors list" in template or "instead of the debtors list" in template:
        return "cross_ledger_transfer"
    if any(token in spec_id for token in ("wrong_personal_posting", "wrong_debtor", "posted_to_wrong")):
        return "personal_account_posting"
    if any(token in spec_id for token in ("journal", "control_column", "discount_posted_to_control", "recovered_bad_debt_included_in_control")):
        return "journal_total_logic"
    return "transaction_classification"


def _reconciliation_analysis_row_family_text(row_family: str) -> str:
    family = str(row_family or "").strip().lower()
    if family == "control_only":
        return "This is a control-only error, so the correction changes a control account and not the list."
    if family == "list_only":
        return "This is a list-only error, so the correction changes personal-account or list balances and not the control account."
    if family == "cross_ledger":
        return "This is a cross-ledger error, so the correction removes the balance from the wrong ledger list and places it in the correct opposite ledger list."
    return "This row affects both a control account and a list, so you must place the correction in each affected destination column."


def _reconciliation_analysis_logic_source_text(logic_source: str) -> str:
    source = str(logic_source or "").strip().lower()
    if source == "journal_total_logic":
        return "Use journal-total logic: journal total and control-column errors affect the control account destination rather than a personal account list."
    if source == "personal_account_posting":
        return "Use personal-account posting logic: the overall transaction total is already accounted for, but one or more personal-account postings in the list are wrong."
    if source == "cross_ledger_transfer":
        return "Use cross-ledger transfer logic: move the balance out of the wrong ledger list and into the correct opposite ledger list."
    return "Use transaction-classification logic: reverse the wrong treatment and record the correct effect where the transaction should have been classified."


def _reconciliation_analysis_impacted_columns_text(*, impacts: Dict[str, Any], headers: List[str]) -> str:
    labels: List[str] = []
    for impact_key, amount in sorted(dict(impacts or {}).items(), key=lambda item: _RECONCILIATION_IMPACT_KEY_TO_COL.get(str(item[0]), 99)):
        if not amount:
            continue
        cix = _RECONCILIATION_IMPACT_KEY_TO_COL.get(str(impact_key))
        if cix is None or cix >= len(headers):
            continue
        labels.append(str(headers[cix]))
    return ", ".join(labels)


def _reconciliation_analysis_catalog() -> List[Dict[str, Any]]:
    return [
        {
            "id": "debtors_invoice_recorded_twice",
            "difficulties": ("easy", "medium", "hard"),
            "category": "both_control_and_list",
            "subsystem": "debtors",
            "amounts": [180.0, 200.0, 240.0, 300.0],
            "template": "A credit invoice for goods sold to {name} was recorded twice in the Debtors Journal and posted twice, {amount}.",
            "name_pool": ["T. Tanli", "N. Mokoena", "L. Jacobs", "S. Nkosi"],
            "impact_keys": ("dc_cr", "dl_cr"),
            "explanation": "The same sale was processed twice, so both the Debtors control account and the Debtors list are overstated. The correction reduces both with a credit.",
        },
        {
            "id": "debtors_journal_undercast",
            "difficulties": ("easy", "medium", "hard"),
            "category": "control_only",
            "subsystem": "debtors",
            "amounts": [180.0, 240.0, 260.0, 300.0],
            "template": "The total of the Debtors Journal was undercast by {amount}.",
            "impact_keys": ("dc_dr",),
            "explanation": "Only the Debtors control account is affected because this is a journal-total error. An undercast means the control account must be increased with a debit.",
        },
        {
            "id": "creditors_journal_overcast",
            "difficulties": ("easy", "medium", "hard"),
            "category": "control_only",
            "subsystem": "creditors",
            "amounts": [160.0, 180.0, 220.0, 300.0],
            "template": "The total of the Creditors Journal was overcast by {amount}.",
            "impact_keys": ("cc_dr",),
            "explanation": "Only the Creditors control account is affected because this is a journal-total error. An overcast means creditors were overstated, so the correction is a debit.",
        },
        {
            "id": "creditors_allowances_undercast",
            "difficulties": ("easy", "medium", "hard"),
            "category": "control_only",
            "subsystem": "creditors",
            "amounts": [120.0, 180.0, 240.0, 300.0],
            "template": "The total of the Creditors Allowances Journal was undercast by {amount}.",
            "impact_keys": ("cc_dr",),
            "explanation": "Only the Creditors control account is affected because this is a journal-total error. An undercast means the reduction in creditors was too small, so the correction is a debit.",
        },
        {
            "id": "receipt_posted_to_wrong_debtor",
            "difficulties": ("medium", "hard"),
            "category": "list_only",
            "subsystem": "debtors",
            "amounts": [120.0, 144.0, 180.0, 240.0],
            "template": "An amount received from {source_name} was posted to the credit side of the account of {wrong_name}, {amount}.",
            "name_pool": ["C. Maduna", "C. Maduma", "S. Mokoena", "L. Botha", "N. Zungu"],
            "impact_keys": ("dl_dr", "dl_cr"),
            "explanation": "The Debtors control account is already correct because the total receipt was recorded correctly. The list must be corrected by increasing the correct debtor and decreasing the wrong debtor.",
        },
        {
            "id": "debtors_allowances_wrong_personal_posting",
            "difficulties": ("easy", "medium", "hard"),
            "category": "list_only",
            "subsystem": "debtors",
            "amounts": [80.0, 100.0, 120.0, 150.0],
            "template": "An amount in the Debtors Allowances Journal was posted to debtor {name}'s account as too much by {amount}.",
            "name_pool": ["N. Zungu", "T. Mbele", "R. Nkosi", "P. Dlamini"],
            "impact_keys": ("dl_dr",),
            "explanation": "The personal account was credited too much, which reduced the debtor too much. The correction is a debit in the Debtors list only.",
        },
        {
            "id": "discount_posted_to_control_too",
            "difficulties": ("medium", "hard"),
            "category": "control_only",
            "subsystem": "debtors",
            "amounts": [180.0, 240.0, 300.0, 360.0],
            "template": "The totals of the discount allowed column and the debtors control column in the CRJ were both posted to the Debtors control account. The duplicate discount posting was {amount}.",
            "impact_keys": ("dc_dr",),
            "explanation": "The Debtors control amount should be posted, but the discount allowed total must not also be posted there. The duplicate credit must be cancelled with a debit to Debtors control.",
        },
        {
            "id": "debtors_control_column_not_posted",
            "difficulties": ("easy", "medium", "hard"),
            "category": "control_only",
            "subsystem": "debtors",
            "amounts": [120.0, 180.0, 200.0, 260.0],
            "template": "An amount of {amount} in the debtors control column of the CRJ was not posted.",
            "impact_keys": ("dc_cr",),
            "explanation": "Only the Debtors control account is affected. The CRJ control column should reduce debtors, so the missing posting is a credit.",
        },
        {
            "id": "creditors_invoice_treated_as_credit_note",
            "difficulties": ("medium", "hard"),
            "category": "both_control_and_list",
            "subsystem": "creditors",
            "amounts": [90.0, 99.0, 120.0, 180.0],
            "template": "A credit invoice for goods purchased from {name} was treated as a credit note, {amount}.",
            "name_pool": ["Kubeka Suppliers", "Mthembu Stores", "Reddy and Sons", "Patel Traders"],
            "impact_keys": ("cc_cr", "cl_cr"),
            "multiplier": 2.0,
            "explanation": "The transaction should have increased creditors, but it was processed as a decrease. The correction must reverse the wrong decrease and record the increase, so both the control account and list are credited by double the amount.",
        },
        {
            "id": "creditor_debit_balance_in_debtors_list",
            "difficulties": ("medium", "hard"),
            "category": "cross_ledger",
            "subsystem": "both",
            "amounts": [40.0, 80.0, 120.0, 180.0],
            "template": "A creditor with a debit balance of {amount} was included in the Debtors list instead of the Creditors list.",
            "impact_keys": ("dl_cr", "cl_dr"),
            "explanation": "The amount must be removed from the Debtors list and inserted on the debit side of the Creditors list. The control accounts are unaffected because the error is in the lists.",
        },
        {
            "id": "recovered_bad_debt_included_in_control",
            "difficulties": ("medium", "hard"),
            "category": "control_only",
            "subsystem": "debtors",
            "amounts": [180.0, 240.0, 300.0, 322.0],
            "template": "A recovered bad debt received from {name} was included in the debtors control column of the CRJ, {amount}.",
            "name_pool": ["S. Sechele", "D. Khumalo", "R. Nkosi", "P. Mokoena"],
            "impact_keys": ("dc_dr",),
            "explanation": "A recovered bad debt is no longer part of the Debtors list, so it must not reduce Debtors control. Reverse the wrong credit with a debit to Debtors control.",
        },
        {
            "id": "creditors_allowance_recorded_too_small",
            "difficulties": ("medium", "hard"),
            "category": "both_control_and_list",
            "subsystem": "creditors",
            "amounts": [220.0, 320.0, 400.0, 490.0],
            "template": "A credit note to {name} was recorded and posted as too small by {amount}.",
            "name_pool": ["D. Kubeka", "Riso Dealers", "Priti Distributors", "A. Mthembu"],
            "impact_keys": ("cc_dr", "cl_dr"),
            "explanation": "Both the Creditors control account and the supplier's personal account were reduced by too little. The correction is a debit to both because creditors must be reduced further.",
        },
    ]


def _instantiate_reconciliation_analysis_item(*, r: random.Random, spec: Dict[str, Any]) -> Dict[str, Any]:
    amount = float(r.choice(spec.get("amounts") or [100.0]))
    payload: Dict[str, Any] = {"amount": f"R{_fmt_money(amount)}"}
    name_pool = list(spec.get("name_pool") or [])
    template = str(spec.get("template") or "")
    if "{name}" in template and name_pool:
        payload["name"] = str(r.choice(name_pool))
    if "{source_name}" in template and len(name_pool) >= 2:
        source_name, wrong_name = r.sample(name_pool, k=2)
        payload["source_name"] = str(source_name)
        payload["wrong_name"] = str(wrong_name)
    impact_amount = _round_money(amount * float(spec.get("multiplier") or 1.0))
    row_family = _normalize_reconciliation_analysis_row_family(str(spec.get("category") or ""))
    return {
        "id": str(spec.get("id") or ""),
        "text": template.format(**payload),
        "impacts": {str(key): impact_amount for key in tuple(spec.get("impact_keys") or ())},
        "explanation": str(spec.get("explanation") or "").strip(),
        "category": str(spec.get("category") or "").strip(),
        "subsystem": str(spec.get("subsystem") or "").strip(),
        "row_family": row_family,
        "logic_source": _infer_reconciliation_analysis_logic_source(spec=spec, row_family=row_family),
    }


def _select_reconciliation_analysis_specs(*, r: random.Random, difficulty: str) -> List[Dict[str, Any]]:
    diff = _normalize_reconciliation_analysis_difficulty(difficulty)
    eligible = [spec for spec in _reconciliation_analysis_catalog() if diff in tuple(spec.get("difficulties") or ())]
    by_id = {str(spec["id"]): spec for spec in eligible}
    if diff == "easy":
        target_ids = [
            "debtors_journal_undercast",
            "creditors_journal_overcast",
            "debtors_control_column_not_posted",
            "debtors_allowances_wrong_personal_posting",
            "creditors_allowances_undercast",
        ]
    elif diff == "medium":
        target_ids = [
            "debtors_invoice_recorded_twice",
            "receipt_posted_to_wrong_debtor",
            "creditors_invoice_treated_as_credit_note",
            "creditor_debit_balance_in_debtors_list",
            "debtors_journal_undercast",
            "creditors_journal_overcast",
            "discount_posted_to_control_too",
        ]
    else:
        target_ids = [
            "debtors_invoice_recorded_twice",
            "receipt_posted_to_wrong_debtor",
            "creditors_invoice_treated_as_credit_note",
            "creditor_debit_balance_in_debtors_list",
            "recovered_bad_debt_included_in_control",
            "creditors_allowance_recorded_too_small",
            "debtors_journal_undercast",
            "creditors_journal_overcast",
            "debtors_control_column_not_posted",
        ]
    selected = [by_id[item_id] for item_id in target_ids if item_id in by_id]
    r.shuffle(selected)
    return selected


def _make_reconciliation_analysis_once(*, r: random.Random, difficulty: Optional[str] = None) -> Dict[str, Any]:
    diff = _normalize_reconciliation_analysis_difficulty(difficulty)
    headers = _reconciliation_impact_headers()
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    derivation_map: Dict[str, str] = {}
    rendered_rows: List[Dict[str, Any]] = []

    prompt_lines = [
        "Activity: Reconciliation analysis",
        "",
        "Required:",
        "Use the answer sheet to show how each error or omission must be recorded to reconcile the control accounts with the debtors and creditors lists.",
        "",
        "Information:",
    ]

    for row_index, spec in enumerate(_select_reconciliation_analysis_specs(r=r, difficulty=diff), start=1):
        rendered = _instantiate_reconciliation_analysis_item(r=r, spec=spec)
        rendered_rows.append(rendered)
        prompt_lines.append(f"{row_index}. {rendered['text']}")
        values: List[Optional[str]] = [str(row_index)] + ["" for _ in range(len(headers) - 1)]
        rows.append(_build_journal_row(row_index=row_index - 1, values=values, editable_cols=list(range(1, len(headers)))))
        correct_map[f"r{row_index - 1}_c0"] = str(row_index)

        explanation = str(rendered.get("explanation") or "").strip()
        row_family = str(rendered.get("row_family") or "").strip()
        logic_source = str(rendered.get("logic_source") or "").strip()
        family_text = _reconciliation_analysis_row_family_text(row_family)
        logic_source_text = _reconciliation_analysis_logic_source_text(logic_source)
        impacted_columns_text = _reconciliation_analysis_impacted_columns_text(impacts=dict(rendered.get("impacts") or {}), headers=headers)
        for impact_key, amount in dict(rendered.get("impacts") or {}).items():
            cix = _RECONCILIATION_IMPACT_KEY_TO_COL.get(str(impact_key))
            if cix is None:
                continue
            cell_id = f"r{row_index - 1}_c{cix}"
            amount_text = _fmt_money(float(amount))
            column_label = headers[cix]
            direction_text = "increases" if str(impact_key).endswith("_dr") else "decreases"
            cell_reason = f"{family_text} {logic_source_text} Enter the amount in {column_label} because row {row_index} {direction_text} that balance. {explanation}"
            correct_map[cell_id] = amount_text
            cell_hints[cell_id] = cell_reason
            derivation_map[cell_id] = cell_reason
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key=cell_id,
                role_in_requirement=f"Choose the correct destination column for row {row_index}.",
                evidence_from_question=f"Look at error {row_index}: {rendered['text']}",
                rule_or_principle=f"{family_text} {logic_source_text}",
                how_to_derive=f"Identify the row family first, then place the amount in {column_label}. {explanation}",
                transfer_tip=f"First decide whether the row affects the control account, the list, or both. For this row the affected columns are: {impacted_columns_text}.",
            )

        for cix in range(1, len(headers)):
            cell_id = f"r{row_index - 1}_c{cix}"
            if cell_id not in correct_map:
                correct_map[cell_id] = ""
            if cell_id not in cell_hints:
                column_label = headers[cix]
                blank_reason = f"Leave {column_label} blank for row {row_index}. {family_text} {logic_source_text} The affected columns for this row are {impacted_columns_text}, so this correction does not belong in {column_label}. {explanation}"
                cell_hints[cell_id] = blank_reason
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=cell_id,
                    role_in_requirement=f"Decide whether row {row_index} belongs in {column_label}.",
                    evidence_from_question=f"Compare error {row_index} with the meaning of the answer-sheet columns.",
                    rule_or_principle=f"Only columns directly affected by the error must contain an amount. {family_text}",
                    how_to_derive=blank_reason,
                    transfer_tip=f"If a column is not one of the affected destinations ({impacted_columns_text}), leave it blank.",
                )

    prompt_lines.extend([
        "",
        "Answer sheet:",
        "Enter each correction amount in the correct debit or credit column. Leave the other columns blank.",
    ])

    out = _make_journal(
        prompt="\n".join(prompt_lines),
        journal_type="reconciliation_impact",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Journal totals errors affect a control account, not the list.",
            "Errors in a personal account affect the list, not the control account.",
            "When a transaction is completely misclassified, both the control account and the list may need a correction.",
            "Choose debit when the correction increases that balance and credit when the correction reduces that balance.",
        ],
        cell_hints=cell_hints,
        cell_teaching_map=cell_teaching_map,
        derivation_map=derivation_map,
    )
    out["reconciliation_analysis_rows"] = rendered_rows
    out["difficulty"] = diff
    return out


def _validate_reconciliation_analysis_output(question: Dict[str, Any]) -> None:
    diff = _normalize_reconciliation_analysis_difficulty(question.get("difficulty"))
    expected_count = {"easy": 5, "medium": 7, "hard": 9}[diff]
    rendered_rows = list(question.get("reconciliation_analysis_rows") or [])
    if len(rendered_rows) != expected_count:
        raise _ControlAccountsScenarioValidationError("Reconciliation analysis row count does not match the difficulty requirement.")

    prompt_text = str(question.get("prompt") or question.get("question_text") or question.get("question") or "")
    if "|" in prompt_text:
        raise _ControlAccountsScenarioValidationError("Reconciliation analysis prompt must not leak raw table separators.")
    prompt_lines = [line.strip() for line in prompt_text.splitlines() if line.strip()]
    numbered_lines = [line for line in prompt_lines if line[:1].isdigit() and ". " in line]
    if len(numbered_lines) != len(rendered_rows):
        raise _ControlAccountsScenarioValidationError("Reconciliation analysis prompt numbering does not match the rendered row count.")

    rows = list(((question.get("journal") or {}).get("rows") or question.get("rows") or []))
    if len(rows) != len(rendered_rows):
        raise _ControlAccountsScenarioValidationError("Reconciliation analysis answer-sheet rows do not match the rendered row count.")

    correct_map = dict(question.get("correct_map") or {})
    cell_hints = dict(question.get("cell_hints") or {})
    cell_teaching_map = dict(question.get("cell_teaching_map") or {})
    derivation_map = dict(question.get("derivation_map") or {})
    seen_subsystems = set()
    seen_categories = set()
    for row_index, rendered in enumerate(rendered_rows):
        impacts = dict(rendered.get("impacts") or {})
        if not impacts:
            raise _ControlAccountsScenarioValidationError("Every reconciliation analysis row must affect at least one column.")
        row_family = str(rendered.get("row_family") or "").strip()
        if row_family not in ("control_only", "list_only", "both", "cross_ledger"):
            raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis row family is invalid for row {row_index + 1}.")
        logic_source = str(rendered.get("logic_source") or "").strip()
        if logic_source not in ("journal_total_logic", "personal_account_posting", "cross_ledger_transfer", "transaction_classification"):
            raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis logic source is invalid for row {row_index + 1}.")
        row_number_key = f"r{row_index}_c0"
        if str(correct_map.get(row_number_key) or "") != str(row_index + 1):
            raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis row numbering mismatch at {row_number_key}.")
        seen_subsystems.add(str(rendered.get("subsystem") or ""))
        seen_categories.add(str(rendered.get("category") or ""))
        for cix in range(1, len(_reconciliation_impact_headers())):
            cell_id = f"r{row_index}_c{cix}"
            expected = ""
            for impact_key, col_index in _RECONCILIATION_IMPACT_KEY_TO_COL.items():
                if col_index == cix and impact_key in impacts:
                    expected = _fmt_money(float(impacts[impact_key]))
                    break
            if str(correct_map.get(cell_id) or "") != expected:
                raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis output mismatch at {cell_id}.")
            if cell_id not in cell_hints and cell_id not in cell_teaching_map:
                raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis hint coverage is missing for {cell_id}.")
            if expected and cell_id not in derivation_map:
                raise _ControlAccountsScenarioValidationError(f"Reconciliation analysis derivation is missing for populated cell {cell_id}.")

    if diff in ("medium", "hard") and not {"debtors", "creditors"}.issubset(seen_subsystems):
        raise _ControlAccountsScenarioValidationError("Medium and hard reconciliation analysis questions must include both debtors and creditors.")
    if diff == "hard" and "cross_ledger" not in seen_categories:
        raise _ControlAccountsScenarioValidationError("Hard reconciliation analysis must include a cross-ledger row.")


def make_reconciliation_impact_matrix_question(*, r: random.Random, difficulty: Optional[str] = None) -> Dict[str, Any]:
    last_error: Optional[_ControlAccountsScenarioValidationError] = None
    for _ in range(MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS):
        try:
            out = _make_reconciliation_analysis_once(r=r, difficulty=difficulty)
            _validate_reconciliation_analysis_output(out)
            return out
        except _ControlAccountsScenarioValidationError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise _ControlAccountsScenarioValidationError("Could not generate a valid reconciliation analysis question.")


def _control_account_header_rows(*, business: str, account_label: str, folio: str) -> List[List[Dict[str, Any]]]:
    headers = _general_ledger_account_headers()
    return [
        [{"label": f"General ledger of {business}", "colSpan": len(headers)}],
        [{"label": "Dr.", "colSpan": 1}, {"label": account_label, "colSpan": 8}, {"label": "Cr.", "colSpan": 1}],
        [{"label": "", "colSpan": 1}, {"label": folio, "colSpan": 8}, {"label": "", "colSpan": 1}],
    ]


def _make_control_account_study_table(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    var = _normalize_control_accounts_variant(variant)
    diff = _normalize_control_accounts_difficulty(difficulty)
    mode_norm = str(mode or "").strip().lower()

    business = str(business or pick_business_name(r=r)).strip()
    month = r.choice(["May", "June", "September", "October"])
    year = int(r.choice([2018, 2019, 2020, 2022]))
    m = month[:3]
    next_m = _next_month_abbrev(month)

    headers = _general_ledger_account_headers()

    acct = "Debtors control" if var == "debtors" else "Creditors control"

    opening = float(r.choice([21450, 41000, 54750, 89560]))
    bank = float(r.choice([12000, 24000, 26640, 40000]))
    discount = float(r.choice([600, 750, 1800, 3200]))
    allowances = float(r.choice([7500, 980, 1122, 2108]))
    journal_adj = float(r.choice([936, 1400, 1950, 3200]))

    if var == "debtors":
        sales = float(r.choice([52500, 270000, 310920]))
        journal_debits = float(r.choice([300, 624, 820, 1820]))
        journal_credits = journal_adj
        closing = _round_money(opening + sales + journal_debits - (bank + discount + allowances + journal_credits))
        debit_total = _round_money(opening + sales + journal_debits)
        credit_total = _round_money(bank + discount + allowances + journal_credits + closing)
    else:
        purchases = float(r.choice([49800, 60000, 72000]))
        journal_debits = journal_adj
        journal_credits = float(r.choice([290, 670, 1290]))
        closing = _round_money(opening + purchases + journal_credits - (bank + discount + allowances + journal_debits))
        debit_total = _round_money(bank + discount + allowances + journal_debits + closing)
        credit_total = _round_money(opening + purchases + journal_credits)

    if diff == "easy":
        editable_cols = [2, 3, 4, 7, 8, 9]
    elif diff == "medium":
        editable_cols = [1, 2, 3, 4, 6, 7, 8, 9]
    else:
        editable_cols = list(range(len(headers)))

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    working_map: Dict[str, str] = {}

    def _mask_values(values: List[Optional[str]], masked_cols: List[int]) -> List[Optional[str]]:
        display = list(values)
        for cix in masked_cols:
            if 0 <= cix < len(display) and str(display[cix] or "").strip():
                display[cix] = "?"
        return display

    def _add_row(rix: int, answer_values: List[Optional[str]], masked_cols: Optional[List[int]] = None) -> None:
        display_values = _mask_values(answer_values, masked_cols or [])
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display_values, editable_cols=editable_cols))
        for cix, answer_value in enumerate(answer_values):
            correct_map[f"t0_r{rix}_c{cix}"] = "" if answer_value is None else str(answer_value)

    if var == "debtors":
        if diff == "easy":
            mask_map = r.choice([
                {2: [7], 6: [4, 9]},
                {1: [2], 5: [9]},
                {0: [4], 7: [4]},
                {4: [2], 6: [9]},
                {1: [3], 6: [4]},
            ])
        elif diff == "medium":
            mask_map = r.choice([
                {2: [7], 4: [2, 7], 5: [9], 6: [4, 9], 7: [4]},
                {1: [2, 3], 2: [9], 4: [4, 7], 6: [4], 7: [0, 4]},
            ])
        else:
            mask_map = r.choice([
                {1: [2, 3, 4], 2: [7, 8, 9], 4: [2, 3, 4, 7, 8, 9], 5: [7, 8, 9], 6: [4, 9], 7: [2, 3, 4]},
                {0: [0, 1, 2, 3, 4], 2: [5, 6, 7, 8, 9], 4: [2, 4, 7, 9], 5: [8, 9], 6: [2, 4, 7, 9], 7: [0, 1, 2, 3, 4]},
            ])
        _add_row(0, [m, "1", "Balance b/d", "b/d", _fmt_money(opening), "", "", "", "", ""], mask_map.get(0))
        _add_row(1, [m, "31", "Sales", "DJ", _fmt_money(sales), "", "", "", "", ""], mask_map.get(1))
        _add_row(2, ["", "", "", "", "", m, "31", "Bank and discount allowed", "CRJ", _fmt_money(_round_money(bank + discount))], mask_map.get(2))
        _add_row(3, ["", "", "", "", "", m, "31", "Debtors allowances", "DAJ", _fmt_money(allowances)], mask_map.get(3))
        _add_row(4, [m, "31", "Sundry accounts", "GJ", _fmt_money(journal_debits), "", "", "Sundry accounts", "GJ", _fmt_money(journal_credits)], mask_map.get(4))
        _add_row(5, ["", "", "", "", "", m, "31", "Balance c/d", "c/d", _fmt_money(closing)], mask_map.get(5))
        _add_row(6, ["", "", "Totals", "", _fmt_money(debit_total), "", "", "Totals", "", _fmt_money(credit_total)], mask_map.get(6))
        _add_row(7, [next_m, "1", "Balance b/d", "b/d", _fmt_money(closing), "", "", "", "", ""], mask_map.get(7))
        if mode_norm == "scaffold":
            cell_hints["t0_r2_c7"] = "Use the CRJ entry that reduces what debtors owe. The details must name the combined effect shown on the credit side."
            cell_hints["t0_r4_c2"] = "The GJ line uses Sundry accounts when more than one account explains the adjustment."
            cell_hints["t0_r5_c9"] = "Balance c/d is the closing amount still owed by debtors after all month-end entries."
            cell_hints["t0_r6_c4"] = "Add all debit-side amounts. The totals row must match on both sides."
            cell_hints["t0_r6_c9"] = "Add all credit-side amounts, including Balance c/d."
            cell_hints["t0_r7_c4"] = "Balance b/d on day 1 of the next month equals the previous Balance c/d."
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r2_c7",
                role_in_requirement="Name the credit-side details for the CRJ posting.",
                evidence_from_question="This line is dated at month-end and carries folio CRJ on the credit side of the Debtors control account.",
                rule_or_principle="Receipts from debtors reduce the Debtors control account and are posted on the credit side.",
                how_to_derive="Look for the month-end CRJ transfer affecting debtors and state the account description used for that transfer.",
                transfer_tip="Do not write the journal name in Details unless the account itself is named that way.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r5_c9",
                role_in_requirement="Calculate the closing balance carried down.",
                evidence_from_question="Balance c/d appears on the credit side because the Debtors control account must balance after the month-end postings.",
                rule_or_principle="Opening balance plus debit increases must equal credit decreases plus closing balance.",
                how_to_derive="Add the debit side, add the credit-side entries before the balance, then use the difference as Balance c/d.",
                transfer_tip="The same amount must reappear as Balance b/d on the debit side next month.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r6_c4",
                role_in_requirement="Enter the debit total of the account.",
                evidence_from_question="The totals row must show equal totals on both sides of the control account.",
                rule_or_principle="A balanced ledger account has equal debit and credit totals.",
                how_to_derive="Add Balance b/d, Sales, and any GJ debit entries.",
                transfer_tip="Check the opposite total cell after calculating this one.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r7_c4",
                role_in_requirement="Carry the closing balance forward to the next month.",
                evidence_from_question="The last row is day 1 of the next month and is labelled Balance b/d.",
                rule_or_principle="Balance c/d becomes Balance b/d at the start of the next period.",
                how_to_derive="Copy the final Balance c/d amount exactly.",
                transfer_tip="Do not recalculate a new number here; carry forward the same amount.",
            )
    else:
        if diff == "easy":
            mask_map = r.choice([
                {7: [4, 9]},
                {1: [7], 6: [4]},
                {3: [2], 7: [9]},
                {0: [9], 8: [9]},
                {4: [2], 6: [4]},
            ])
        elif diff == "medium":
            mask_map = r.choice([
                {1: [7], 4: [2, 3, 4], 6: [2, 3, 4], 7: [4, 9], 8: [9]},
                {0: [8, 9], 3: [2, 4], 4: [2, 3], 6: [4], 7: [4, 9]},
            ])
        else:
            mask_map = r.choice([
                {1: [7, 8, 9], 3: [2, 3, 4], 4: [2, 3, 4], 5: [2, 3, 4], 6: [2, 3, 4], 7: [2, 3, 4], 8: [7, 8, 9]},
                {0: [5, 6, 7, 8, 9], 1: [7, 9], 3: [0, 1, 2, 3, 4], 4: [2, 4], 6: [2, 3, 4], 7: [0, 2, 4], 8: [7, 8, 9]},
            ])
        _add_row(0, ["", "", "", "", "", m, "1", "Balance b/d", "b/d", _fmt_money(opening)], mask_map.get(0))
        _add_row(1, ["", "", "", "", "", m, "31", "Sundry purchases", "CJ", _fmt_money(purchases)], mask_map.get(1))
        _add_row(2, ["", "", "", "", "", m, "31", "Journal credits", "GJ", _fmt_money(journal_credits)], mask_map.get(2))
        _add_row(3, [m, "31", "Bank and discount received", "CPJ", _fmt_money(_round_money(bank + discount)), "", "", "", "", ""], mask_map.get(3))
        _add_row(4, [m, "31", "Sundry allowances", "CAJ", _fmt_money(allowances), "", "", "", "", ""], mask_map.get(4))
        _add_row(5, [m, "31", "Journal debits", "GJ", _fmt_money(journal_debits), "", "", "", "", ""], mask_map.get(5))
        _add_row(6, [m, "31", "Balance c/d", "c/d", _fmt_money(closing), "", "", "", "", ""], mask_map.get(6))
        _add_row(7, ["", "", "Totals", "", _fmt_money(debit_total), "", "", "Totals", "", _fmt_money(credit_total)], mask_map.get(7))
        _add_row(8, ["", "", "", "", "", next_m, "1", "Balance b/d", "b/d", _fmt_money(closing)], mask_map.get(8))
        if mode_norm == "scaffold":
            cell_hints["t0_r1_c7"] = "Use the CJ posting that increases what the business owes to suppliers."
            cell_hints["t0_r3_c2"] = "Payments to creditors reduce the balance, so this CPJ entry appears on the debit side."
            cell_hints["t0_r6_c4"] = "Balance c/d is the closing amount still owed to creditors after all adjustments."
            cell_hints["t0_r7_c4"] = "Add the debit-side amounts, including Balance c/d."
            cell_hints["t0_r7_c9"] = "Add the credit-side amounts. The totals must be equal."
            cell_hints["t0_r8_c9"] = "Balance b/d next month equals the previous Balance c/d."
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r1_c7",
                role_in_requirement="Name the credit-side details for the CJ posting.",
                evidence_from_question="This month-end line uses folio CJ on the credit side of the Creditors control account.",
                rule_or_principle="Credit purchases increase the Creditors control account and are posted on the credit side.",
                how_to_derive="Find the month-end CJ transfer and use the matching account description.",
                transfer_tip="Keep the journal folio in Fol and the account description in Details.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r6_c4",
                role_in_requirement="Calculate the closing balance carried down.",
                evidence_from_question="Balance c/d appears on the debit side because the Creditors control account must balance after the month-end postings.",
                rule_or_principle="Opening balance plus credit increases must equal debit decreases plus closing balance.",
                how_to_derive="Add the credit side, add the debit entries before the balance, then use the difference as Balance c/d.",
                transfer_tip="The same amount must reappear on the credit side next month as Balance b/d.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r7_c4",
                role_in_requirement="Enter the debit total of the account.",
                evidence_from_question="The totals row must balance the Creditors control account.",
                rule_or_principle="A balanced ledger account has equal debit and credit totals.",
                how_to_derive="Add Bank and discount received, Sundry allowances, Journal debits, and Balance c/d.",
                transfer_tip="Compare this total with the credit-side total to confirm equality.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t0_r8_c9",
                role_in_requirement="Carry the closing balance forward to the next month.",
                evidence_from_question="The final row is the next month on the credit side and is labelled Balance b/d.",
                rule_or_principle="Balance c/d becomes Balance b/d in the next accounting period.",
                how_to_derive="Copy the Balance c/d amount exactly into the Balance b/d row.",
                transfer_tip="Do not change the side when carrying the balance forward.",
            )

    _validate_control_account_study_output(
        variant=var,
        opening=opening,
        closing=closing,
        debit_total=debit_total,
        credit_total=credit_total,
        correct_map=correct_map,
    )

    source_headers = ["Date", "Source information", "Folio", "Amount"]
    source_rows: List[List[Dict[str, Any]]] = []

    def _add_source_row(rix: int, values: List[Optional[str]]) -> None:
        source_rows.append(_build_prefixed_row(table_index=97, row_index=rix, values=values, editable_cols=[]))

    if var == "debtors":
        source_entries = [
            [f"{m} 1", "Opening balance brought down from the previous month", "b/d", _fmt_money(opening)],
            [f"{m} 31", "Total credit sales transferred from the Debtors Journal", "DJ", _fmt_money(sales)],
            [f"{m} 31", "Total bank and discount allowed transferred from the CRJ", "CRJ", _fmt_money(_round_money(bank + discount))],
            [f"{m} 31", "Total debtors allowances transferred from the DAJ", "DAJ", _fmt_money(allowances)],
            [f"{m} 31", "General Journal debit transfer: Sundry accounts", "GJ", _fmt_money(journal_debits)],
            [f"{m} 31", "General Journal credit transfer: Sundry accounts", "GJ", _fmt_money(journal_credits)],
        ]
    else:
        source_entries = [
            [f"{m} 1", "Opening balance brought down from the previous month", "b/d", _fmt_money(opening)],
            [f"{m} 31", "Total credit purchases transferred from the Creditors Journal", "CJ", _fmt_money(purchases)],
            [f"{m} 31", "Total bank and discount received transferred from the CPJ", "CPJ", _fmt_money(_round_money(bank + discount))],
            [f"{m} 31", "Total creditors allowances transferred from the CAJ", "CAJ", _fmt_money(allowances)],
            [f"{m} 31", "General Journal debit transfer: Sundry accounts", "GJ", _fmt_money(journal_debits)],
            [f"{m} 31", "General Journal credit transfer: Sundry accounts", "GJ", _fmt_money(journal_credits)],
        ]

    for rix, entry in enumerate(source_entries):
        _add_source_row(rix, entry)

    prompt_journal = {
        "heading": f"Source information for {month} {year}",
        "journal_type": "control_account_source_info",
        "table_variant": "grade_project",
        "headers": source_headers,
        "rows": source_rows,
        "allow_extra_rows": False,
    }

    if mode_norm == "scaffold":
        for row_index, masked_cols in mask_map.items():
            answer_values = [str(correct_map.get(f"t0_r{row_index}_c{col_index}") or "") for col_index in range(len(headers))]
            for col_index in masked_cols or []:
                cell_key = f"t0_r{row_index}_c{col_index}"
                hint_text, teaching_hint = _build_study_cell_guidance(
                    variant=var,
                    row_index=row_index,
                    column_index=col_index,
                    answer_values=answer_values,
                    month_abbrev=m,
                    next_month_abbrev=next_m,
                )
                if hint_text:
                    cell_hints[cell_key] = hint_text
                if teaching_hint:
                    _append_control_accounts_teaching_hint(
                        cell_teaching_map=cell_teaching_map,
                        cell_key=cell_key,
                        role_in_requirement=teaching_hint.get("role_in_requirement", ""),
                        evidence_from_question=teaching_hint.get("evidence_from_question", ""),
                        rule_or_principle=teaching_hint.get("rule_or_principle", ""),
                        how_to_derive=teaching_hint.get("how_to_derive", ""),
                        transfer_tip=teaching_hint.get("transfer_tip", ""),
                    )

    missing_fields = _join_labels(_missing_field_labels(mask_map))
    prompt_lines = [
        f"{business}",
        f"{acct} for {month} {year}",
        "",
        "Information:",
        "Study the source information table below.",
        "",
        "Required:",
        f"1. Study the information for {month} {year} provided in the table and complete the {acct} account that follows by filling in the missing {missing_fields} indicated by ?.",
        "2. Calculate the totals and carry the balance down and forward where required.",
        "3. Use the correct side of the account when deciding where each balance belongs.",
    ]
    prompt = "\n".join(prompt_lines)
    _validate_control_account_study_prompt(
        difficulty=diff,
        prompt=prompt,
        month=month,
        year=year,
        account_label=acct,
        mask_map=mask_map,
        variant=var,
    )

    out = _make_journal(
        prompt=prompt,
        journal_type="control_account",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Debtors control normally closes with a debit balance carried down on the credit side and brought down on the debit side.",
            "Creditors control normally closes with a credit balance carried down on the debit side and brought down on the credit side.",
            "Totals must balance: Total Dr = Total Cr.",
            "Balance c/d is carried down and becomes Balance b/d next month.",
        ],
        header_rows=_control_account_header_rows(
            business=business,
            account_label=acct,
            folio="B7" if var == "debtors" else "B8",
        ),
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
        cell_teaching_map=cell_teaching_map if mode_norm == "scaffold" else None,
        working_map=working_map if mode_norm == "scaffold" else None,
        table_variant="grade_project",
    )
    out["control_accounts_family"] = "study_table"
    out["control_accounts_variant"] = var
    out["difficulty"] = diff
    out["prompt_journal"] = prompt_journal
    return out


def make_control_account_study_table(
    *,
    r: random.Random,
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    return _make_control_account_study_table(r=r, difficulty="easy", mode="", variant=variant, business=business)


def make_control_account_study_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    last_error: Optional[_ControlAccountsScenarioValidationError] = None
    for _ in range(MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS):
        try:
            return _make_control_account_study_table(r=r, difficulty=difficulty, mode=mode, variant=variant, business=business)
        except _ControlAccountsScenarioValidationError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise _ControlAccountsScenarioValidationError("Could not generate a valid control account study question.")


def _make_control_accounts_reconciliation_once(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    var = str(variant or "debtors").strip().lower()
    if var not in ("debtors", "creditors"):
        var = "debtors"

    business = str(business or pick_business_name(r=r)).strip()
    month = r.choice(["September", "November", "March", "August"])
    year = int(r.choice([2010, 2011]))
    m = month[:3]
    next_m = {"Mar": "Apr", "Aug": "Sep", "Sep": "Oct", "Nov": "Dec"}.get(m, "Oct")

    gl_headers = _general_ledger_account_headers()
    list_headers = _debtors_creditors_list_headers()

    if var == "debtors":
        acct = "Debtors control"
        fol = "B7"
        names = pick_person_names(r=r, k=7)
        base_list: Dict[str, Tuple[float, float]] = {nm: (float(r.choice([600, 800, 1200, 1980, 2400, 4520, 5380, 5890, 7202])), 0.0) for nm in names}
        nm_credit = r.choice(names)
        base_list[nm_credit] = (0.0, float(r.choice([240, 320, 640, 720])))
        dj_sales = float(r.choice([18200, 32622]))
        crj_bank_disc = float(r.choice([19300, 28560]))
        daj_allow = float(r.choice([960, 3100]))
        gj_debits = float(r.choice([0, 840]))
        gj_credits = float(r.choice([0, 640]))
        cpj_rd = float(r.choice([0, 240, 300]))
        pcj_paid = float(r.choice([0, 18, 160]))
    else:
        acct = "Creditors control"
        fol = "B8"
        names = pick_business_names(r=r, k=5, unique_surnames=True)
        base_list = {nm: (0.0, float(r.choice([284, 689, 2065, 4460, 7507]))) for nm in names}
        nm_debit = r.choice(names)
        base_list[nm_debit] = (float(r.choice([180, 244, 340, 500])), 0.0)
        cj_purchases = float(r.choice([21800, 42700]))
        cpj_pay_disc = float(r.choice([30200, 31881]))
        caj_allow = float(r.choice([2300, 7108]))
        gj_debits = float(r.choice([0, 3520]))
        gj_credits = float(r.choice([0, 1300]))
        crj_bank = float(r.choice([0, 140, 220]))

    def _sum_list(lst: Dict[str, Tuple[float, float]]) -> Tuple[float, float]:
        return _round_money(sum(v[0] for v in lst.values())), _round_money(sum(v[1] for v in lst.values()))

    dr_open, cr_open = _sum_list(base_list)
    opening_control = _round_money(dr_open - cr_open) if var == "debtors" else _round_money(cr_open - dr_open)

    if var == "debtors":
        closing_control = _round_money(opening_control + dj_sales + cpj_rd + pcj_paid + gj_debits - crj_bank_disc - daj_allow - gj_credits)
    else:
        closing_control = _round_money(opening_control + cj_purchases + gj_credits + crj_bank - cpj_pay_disc - caj_allow - gj_debits)

    corrected_list = dict(base_list)

    def _align_list_to_closing_balance(lst: Dict[str, Tuple[float, float]]) -> Dict[str, Tuple[float, float]]:
        aligned = dict(lst)
        debit_total, credit_total = _sum_list(aligned)
        current_net = _round_money(debit_total - credit_total) if var == "debtors" else _round_money(credit_total - debit_total)
        delta = _round_money(closing_control - current_net)
        anchor_name = str(next(iter(aligned.keys())))
        debit_value, credit_value = aligned[anchor_name]
        if delta == 0.0:
            return aligned
        if var == "debtors":
            if delta > 0.0:
                aligned[anchor_name] = (_round_money(debit_value + delta), credit_value)
            else:
                remaining = abs(delta)
                if debit_value >= remaining:
                    aligned[anchor_name] = (_round_money(debit_value - remaining), credit_value)
                else:
                    aligned[anchor_name] = (0.0, _round_money(credit_value + remaining - debit_value))
        else:
            if delta > 0.0:
                aligned[anchor_name] = (debit_value, _round_money(credit_value + delta))
            else:
                remaining = abs(delta)
                if credit_value >= remaining:
                    aligned[anchor_name] = (debit_value, _round_money(credit_value - remaining))
                else:
                    aligned[anchor_name] = (_round_money(debit_value + remaining - credit_value), 0.0)
        return aligned

    corrected_list = _align_list_to_closing_balance(corrected_list)
    supplied_list = dict(corrected_list)
    errors: List[str] = []

    supplied_opening_control = float(opening_control)
    supplied_dj_sales = float(dj_sales) if var == "debtors" else 0.0
    supplied_crj_bank_disc = float(crj_bank_disc) if var == "debtors" else 0.0
    supplied_daj_allow = float(daj_allow) if var == "debtors" else 0.0
    supplied_cpj_rd = float(cpj_rd) if var == "debtors" else 0.0
    supplied_pcj_paid = float(pcj_paid) if var == "debtors" else 0.0
    supplied_debt_gj_debits = float(gj_debits) if var == "debtors" else 0.0
    supplied_debt_gj_credits = float(gj_credits) if var == "debtors" else 0.0

    supplied_cj_purchases = float(cj_purchases) if var == "creditors" else 0.0
    supplied_cpj_pay_disc = float(cpj_pay_disc) if var == "creditors" else 0.0
    supplied_caj_allow = float(caj_allow) if var == "creditors" else 0.0
    supplied_cred_gj_debits = float(gj_debits) if var == "creditors" else 0.0
    supplied_cred_gj_credits = float(gj_credits) if var == "creditors" else 0.0
    supplied_crj_bank = float(crj_bank) if var == "creditors" else 0.0

    def _pick_amt(amts: List[float]) -> float:
        return float(r.choice(amts))

    def _apply_receipt_posted_short() -> None:
        nm = r.choice(names)
        adj = _pick_amt([50, 90, 100, 120, 150])
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + adj), c)
        errors.append(f"A receipt by {nm} was posted to the debtor’s account R{adj:.2f} short.")

    def _apply_discount_not_posted() -> None:
        nm = r.choice(names)
        disc = _pick_amt([20, 40, 60, 80])
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + disc), c)
        errors.append(f"Discount allowed of R{disc:.2f} was recorded, but not posted to {nm}’s account.")

    def _apply_pcj_not_posted() -> None:
        nm = r.choice(names)
        amt = _pick_amt([18, 40, 60, 80, 160])
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + amt), c)
        errors.append(f"Petty cash of R{amt:.2f} paid on behalf of {nm} was not posted to the debtor’s account.")

    def _apply_wrong_person_posting_debtors() -> None:
        nm1, nm2 = r.sample(names, k=2)
        move = _pick_amt([80, 120, 200, 300, 500])
        d1, c1 = supplied_list[nm1]
        d2, c2 = supplied_list[nm2]
        supplied_list[nm1] = (_round_money(d1 + move), c1)
        supplied_list[nm2] = (_round_money(max(0.0, d2 - move)), c2)
        errors.append(f"An invoice for R{move:.2f} was posted to {nm1} instead of {nm2}.")

    def _apply_wrong_amount_posted_debtors() -> None:
        nm = r.choice(names)
        delta = _pick_amt([20, 36, 40, 59])
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + delta), c)
        errors.append(f"An invoice to {nm} was posted R{delta:.2f} less than the correct amount.")

    def _apply_posted_wrong_side_debtors() -> None:
        nm = r.choice(names)
        amt = _pick_amt([80, 120, 160, 200])
        d, c = supplied_list[nm]
        if d >= amt:
            supplied_list[nm] = (_round_money(d - amt), _round_money(c + amt))
        else:
            supplied_list[nm] = (0.0, _round_money(c + amt))
        errors.append(f"An invoice of R{amt:.2f} issued to {nm} was posted on the wrong side of the account.")

    def _apply_credit_balance_transfer_not_done() -> None:
        nm = r.choice(names)
        amt = _pick_amt([200, 320, 640, 720, 800])
        d, c = supplied_list[nm]
        supplied_list[nm] = (d, _round_money(max(c, amt)))
        errors.append(f"{nm}’s credit balance of R{amt:.2f} should have been transferred to the creditors ledger. No entry was made.")

    def _apply_opening_balance_incorrect() -> None:
        nonlocal supplied_opening_control
        amt = _pick_amt([100, 180, 240, 260, 300])
        direction = r.choice(["under", "over"])
        if direction == "under":
            supplied_opening_control = _round_money(supplied_opening_control - amt)
            errors.append(f"The opening balance of the control account was understated by R{amt:.2f}.")
        else:
            supplied_opening_control = _round_money(supplied_opening_control + amt)
            errors.append(f"The opening balance of the control account was overstated by R{amt:.2f}.")

    def _apply_dj_undercast() -> None:
        nonlocal supplied_dj_sales
        nm = r.choice(names)
        amt = _pick_amt([180, 240, 260, 300, 640])
        supplied_dj_sales = _round_money(supplied_dj_sales - amt)
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(max(0.0, d - amt)), c)
        errors.append(f"The Debtors Journal was undercast by R{amt:.2f}.")

    def _apply_daj_undercast() -> None:
        nonlocal supplied_daj_allow
        nm = r.choice(names)
        amt = _pick_amt([20, 35, 40, 53, 60])
        supplied_daj_allow = _round_money(supplied_daj_allow - amt)
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + amt), c)
        errors.append(f"The total of the Debtors Allowances Journal was undercast by R{amt:.2f}.")

    def _apply_crj_undercast() -> None:
        nonlocal supplied_crj_bank_disc
        amt = _pick_amt([120, 150, 200, 260])
        supplied_crj_bank_disc = _round_money(supplied_crj_bank_disc - amt)
        errors.append(f"The total of the Cash Receipts Journal was undercast by R{amt:.2f}.")

    def _apply_crj_not_posted_to_control() -> None:
        nonlocal supplied_crj_bank_disc
        amt = _pick_amt([100, 180, 240, 300])
        supplied_crj_bank_disc = _round_money(supplied_crj_bank_disc - amt)
        errors.append(f"An amount of R{amt:.2f} in the debtors control column of the CRJ was not posted to the control account.")

    def _apply_dishonoured_cheque_cancels_discount() -> None:
        nonlocal supplied_crj_bank_disc
        nm = r.choice(names)
        amt = _pick_amt([120, 150, 200, 240])
        supplied_crj_bank_disc = _round_money(supplied_crj_bank_disc - amt)
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(d + amt), c)
        errors.append(f"A cheque by {nm} for R{amt:.2f} was dishonoured and the cancellation was not posted.")

    def _apply_cj_undercast() -> None:
        nonlocal supplied_cj_purchases
        nm = r.choice(names)
        amt = _pick_amt([180, 240, 260, 300, 500, 700])
        supplied_cj_purchases = _round_money(supplied_cj_purchases - amt)
        d, c = supplied_list[nm]
        supplied_list[nm] = (d, _round_money(max(0.0, c - amt)))
        errors.append(f"The total of the Creditors Journal was undercast by R{amt:.2f}.")

    def _apply_invoice_posted_wrong_creditor() -> None:
        nm1, nm2 = r.sample(names, k=2)
        move = _pick_amt([500, 700, 900, 1400])
        d1, c1 = supplied_list[nm1]
        d2, c2 = supplied_list[nm2]
        supplied_list[nm1] = (d1, _round_money(c1 + move))
        supplied_list[nm2] = (d2, _round_money(max(0.0, c2 - move)))
        errors.append(f"An invoice for R{move:.2f} was posted to {nm1} instead of {nm2}.")

    def _apply_invoice_posted_wrong_side_creditors() -> None:
        nm = r.choice(names)
        amt = _pick_amt([180, 240, 300, 500])
        d, c = supplied_list[nm]
        if c >= amt:
            supplied_list[nm] = (_round_money(d + amt), _round_money(c - amt))
        else:
            supplied_list[nm] = (_round_money(d + amt), 0.0)
        errors.append(f"A credit purchase of R{amt:.2f} was posted on the wrong side of {nm}’s account.")

    def _apply_credit_note_wrong_amount_creditors() -> None:
        nm = r.choice(names)
        amt = _pick_amt([35, 53, 90, 175])
        d, c = supplied_list[nm]
        supplied_list[nm] = (d, _round_money(c + amt))
        errors.append(f"A credit note of R{amt:.2f} was posted incorrectly to {nm}’s account.")

    def _apply_caj_undercast() -> None:
        nonlocal supplied_caj_allow
        amt = _pick_amt([90, 175, 240, 300])
        supplied_caj_allow = _round_money(supplied_caj_allow - amt)
        errors.append(f"The total of the Creditors Allowances Journal was undercast by R{amt:.2f}.")

    def _apply_allowances_posted_as_purchases() -> None:
        nonlocal supplied_cj_purchases, supplied_caj_allow
        amt = _pick_amt([90, 175, 240, 300])
        supplied_cj_purchases = _round_money(supplied_cj_purchases + amt)
        supplied_caj_allow = _round_money(max(0.0, supplied_caj_allow - amt))
        errors.append(f"A credit note of R{amt:.2f} was incorrectly treated as a credit purchase.")

    def _apply_debit_balance_transfer_not_done_creditors() -> None:
        nm = r.choice(names)
        amt = _pick_amt([180, 244, 340, 500, 640])
        d, c = supplied_list[nm]
        supplied_list[nm] = (_round_money(max(d, amt)), c)
        errors.append(f"{nm}’s debit balance of R{amt:.2f} should have been transferred to the debtors ledger. No entry was made.")

    def _apply_bank_discount_not_posted_creditors() -> None:
        nm = r.choice(names)
        amt = _pick_amt([40, 60, 80, 120])
        d, c = supplied_list[nm]
        supplied_list[nm] = (d, _round_money(c + amt))
        errors.append(f"Discount received of R{amt:.2f} was recorded, but not posted to {nm}’s account.")

    if var == "debtors":
        easy_catalog = [
            _apply_daj_undercast,
            _apply_receipt_posted_short,
            _apply_wrong_amount_posted_debtors,
            _apply_discount_not_posted,
            _apply_pcj_not_posted,
            _apply_dishonoured_cheque_cancels_discount,
            _apply_credit_balance_transfer_not_done,
        ]
        medium_catalog = [
            _apply_daj_undercast,
            _apply_dj_undercast,
            _apply_crj_undercast,
            _apply_crj_not_posted_to_control,
            _apply_receipt_posted_short,
            _apply_wrong_person_posting_debtors,
            _apply_wrong_amount_posted_debtors,
            _apply_posted_wrong_side_debtors,
            _apply_discount_not_posted,
            _apply_pcj_not_posted,
            _apply_dishonoured_cheque_cancels_discount,
            _apply_credit_balance_transfer_not_done,
            _apply_opening_balance_incorrect,
        ]
        if diff == "easy":
            family_label = "recon_balance_and_list_only"
            catalog = easy_catalog
            mandatory_fns: List[Any] = []
            k = int(r.choice([3, 4]))
        elif diff == "medium":
            family_label = str(r.choice(["recon_control_plus_list_plus_terms", "recon_control_plus_list_plus_strategy"]))
            catalog = medium_catalog
            mandatory_fns = [
                _apply_opening_balance_incorrect,
                _apply_wrong_amount_posted_debtors,
            ] if family_label == "recon_control_plus_list_plus_terms" else [
                _apply_credit_balance_transfer_not_done,
                _apply_dishonoured_cheque_cancels_discount,
            ]
            k = int(r.choice([5, 6]))
        else:
            family_label = str(r.choice([
                "recon_full_debtors_exam",
                "recon_control_plus_list_plus_terms",
                "recon_control_plus_list_plus_strategy",
            ]))
            catalog = medium_catalog
            if family_label == "recon_full_debtors_exam":
                mandatory_fns = [
                    _apply_opening_balance_incorrect,
                    _apply_dj_undercast,
                    _apply_credit_balance_transfer_not_done,
                ]
            elif family_label == "recon_control_plus_list_plus_terms":
                mandatory_fns = [
                    _apply_opening_balance_incorrect,
                    _apply_crj_not_posted_to_control,
                    _apply_wrong_amount_posted_debtors,
                ]
            else:
                mandatory_fns = [
                    _apply_credit_balance_transfer_not_done,
                    _apply_dishonoured_cheque_cancels_discount,
                    _apply_wrong_person_posting_debtors,
                ]
            k = int(r.choice([6, 7]))
    else:
        easy_catalog = [
            _apply_caj_undercast,
            _apply_credit_note_wrong_amount_creditors,
            _apply_bank_discount_not_posted_creditors,
            _apply_debit_balance_transfer_not_done_creditors,
        ]
        medium_catalog = [
            _apply_cj_undercast,
            _apply_caj_undercast,
            _apply_invoice_posted_wrong_creditor,
            _apply_invoice_posted_wrong_side_creditors,
            _apply_credit_note_wrong_amount_creditors,
            _apply_allowances_posted_as_purchases,
            _apply_bank_discount_not_posted_creditors,
            _apply_debit_balance_transfer_not_done_creditors,
            _apply_opening_balance_incorrect,
        ]
        if diff == "easy":
            family_label = "recon_balance_and_list_only"
            catalog = easy_catalog
            mandatory_fns = []
            k = int(r.choice([3, 4]))
        elif diff == "medium":
            family_label = str(r.choice(["recon_control_plus_list_plus_terms", "recon_control_plus_list_plus_strategy"]))
            catalog = medium_catalog
            mandatory_fns = [
                _apply_opening_balance_incorrect,
                _apply_credit_note_wrong_amount_creditors,
            ] if family_label == "recon_control_plus_list_plus_terms" else [
                _apply_debit_balance_transfer_not_done_creditors,
                _apply_bank_discount_not_posted_creditors,
            ]
            k = int(r.choice([5, 6]))
        else:
            family_label = str(r.choice([
                "recon_full_creditors_exam",
                "recon_control_plus_list_plus_terms",
                "recon_control_plus_list_plus_supplier_control",
            ]))
            catalog = medium_catalog
            if family_label == "recon_full_creditors_exam":
                mandatory_fns = [
                    _apply_opening_balance_incorrect,
                    _apply_cj_undercast,
                    _apply_debit_balance_transfer_not_done_creditors,
                ]
            elif family_label == "recon_control_plus_list_plus_terms":
                mandatory_fns = [
                    _apply_opening_balance_incorrect,
                    _apply_caj_undercast,
                    _apply_credit_note_wrong_amount_creditors,
                ]
            else:
                mandatory_fns = [
                    _apply_allowances_posted_as_purchases,
                    _apply_debit_balance_transfer_not_done_creditors,
                    _apply_invoice_posted_wrong_creditor,
                ]
            k = int(r.choice([6, 7]))

    k = min(k, len(catalog))
    selected_fns: List[Any] = []
    for fn in mandatory_fns:
        if fn not in selected_fns:
            selected_fns.append(fn)
    remaining_catalog = [fn for fn in catalog if fn not in selected_fns]
    remaining_needed = max(0, k - len(selected_fns))
    if remaining_needed > 0:
        selected_fns.extend(r.sample(remaining_catalog, k=min(remaining_needed, len(remaining_catalog))))
    for fn in selected_fns:
        fn()

    if var == "debtors":
        supplied_closing = _round_money(
            supplied_opening_control
            + supplied_dj_sales
            + supplied_cpj_rd
            + supplied_pcj_paid
            + supplied_debt_gj_debits
            - supplied_crj_bank_disc
            - supplied_daj_allow
            - supplied_debt_gj_credits
        )
    else:
        supplied_closing = _round_money(
            supplied_opening_control
            + supplied_cj_purchases
            + supplied_cred_gj_credits
            + supplied_crj_bank
            - supplied_cpj_pay_disc
            - supplied_caj_allow
            - supplied_cred_gj_debits
        )

    def _control_header_rows() -> List[List[Dict[str, Any]]]:
        return [
            [{"label": f"General ledger of {business}", "colSpan": len(gl_headers)}],
            [{"label": "Dr.", "colSpan": 1}, {"label": acct, "colSpan": 8}, {"label": "Cr.", "colSpan": 1}],
            [{"label": "", "colSpan": 1}, {"label": fol, "colSpan": 8}, {"label": "", "colSpan": 1}],
        ]

    def _make_control_table(
        *,
        table_index: int,
        opening: float,
        closing: float,
        editable: bool,
        dj_sales_amt: float = 0.0,
        crj_bank_disc_amt: float = 0.0,
        daj_allow_amt: float = 0.0,
        cpj_rd_amt: float = 0.0,
        pcj_paid_amt: float = 0.0,
        debt_gj_debits_amt: float = 0.0,
        debt_gj_credits_amt: float = 0.0,
        cj_purchases_amt: float = 0.0,
        cpj_pay_disc_amt: float = 0.0,
        caj_allow_amt: float = 0.0,
        cred_gj_debits_amt: float = 0.0,
        cred_gj_credits_amt: float = 0.0,
        crj_bank_amt: float = 0.0,
    ) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, str], Dict[str, str]]:
        editable_cols: List[int] = []
        if editable:
            editable_cols = [4, 9] if diff == "easy" else list(range(len(gl_headers)))

        rows: List[List[Dict[str, Any]]] = []
        correct: Dict[str, Any] = {}
        hints: Dict[str, str] = {}
        working_map: Dict[str, str] = {}

        def _add(rix: int, values: List[Optional[str]]) -> None:
            rows.append(_build_prefixed_row(table_index=table_index, row_index=rix, values=values, editable_cols=editable_cols))
            for cix, answer_value in enumerate(values):
                correct[f"t{table_index}_r{rix}_c{cix}"] = "" if answer_value is None else str(answer_value)

        if var == "debtors":
            _add(0, [m, "1", "Balance b/d", "b/d", _fmt_money(opening), "", "", "", "", ""])
            _add(1, [m, "30", "Sales", "DJ", _fmt_money(dj_sales_amt), "", "", "", "", ""])
            if cpj_rd_amt:
                _add(2, [m, "30", "Bank (R/D)", "CPJ", _fmt_money(cpj_rd_amt), "", "", "", "", ""])
            if pcj_paid_amt:
                _add(3, [m, "30", "Petty cash", "PCJ", _fmt_money(pcj_paid_amt), "", "", "", "", ""])
            if debt_gj_debits_amt:
                _add(4, [m, "30", "Journal debits", "GJ", _fmt_money(debt_gj_debits_amt), "", "", "", "", ""])
            _add(5, ["", "", "", "", "", m, "30", "Bank and discount allowed", "CRJ", _fmt_money(crj_bank_disc_amt)])
            _add(6, ["", "", "", "", "", m, "30", "Debtors allowances", "DAJ", _fmt_money(daj_allow_amt)])
            if debt_gj_credits_amt:
                _add(7, ["", "", "", "", "", m, "30", "Journal credits", "GJ", _fmt_money(debt_gj_credits_amt)])
            _add(8, ["", "", "", "", "", m, "30", "Balance c/d", "c/d", _fmt_money(closing)])
            total = _fmt_money(_round_money(opening + dj_sales_amt + cpj_rd_amt + pcj_paid_amt + debt_gj_debits_amt))
            _add(9, ["", "", "Totals", "", total, "", "", "Totals", "", total])
            _add(10, [next_m, "1", "Balance b/d", "b/d", _fmt_money(closing), "", "", "", "", ""])
            if mode_norm == "scaffold" and editable:
                hints[f"t{table_index}_r8_c9"] = "Balance c/d is the closing balance (amount owed by debtors) carried down."
                hints[f"t{table_index}_r9_c4"] = "Totals (Dr): add the debit amounts, including Balance c/d."
                hints[f"t{table_index}_r9_c9"] = "Totals must balance: Total Dr = Total Cr."
                working_map[f"t{table_index}_r5_c7"] = f"t{table_index}_r5_c9"
        else:
            _add(0, ["", "", "", "", "", m, "1", "Balance b/d", "b/d", _fmt_money(opening)])
            _add(1, ["", "", "", "", "", m, "30", "Sundry purchases", "CJ", _fmt_money(cj_purchases_amt)])
            if cred_gj_credits_amt:
                _add(2, ["", "", "", "", "", m, "30", "Journal credits", "GJ", _fmt_money(cred_gj_credits_amt)])
            if crj_bank_amt:
                _add(3, ["", "", "", "", "", m, "30", "Bank", "CRJ", _fmt_money(crj_bank_amt)])
            _add(4, [m, "30", "Bank and discount received", "CPJ", _fmt_money(cpj_pay_disc_amt), "", "", "", "", ""])
            _add(5, [m, "30", "Sundry allowances", "CAJ", _fmt_money(caj_allow_amt), "", "", "", "", ""])
            if cred_gj_debits_amt:
                _add(6, [m, "30", "Journal debits", "GJ", _fmt_money(cred_gj_debits_amt), "", "", "", "", ""])
            _add(7, [m, "30", "Balance c/d", "c/d", _fmt_money(closing), "", "", "", "", ""])
            total = _fmt_money(_round_money(opening + cj_purchases_amt + cred_gj_credits_amt + crj_bank_amt))
            _add(8, ["", "", "Totals", "", total, "", "", "Totals", "", total])
            _add(9, ["", "", "", "", "", next_m, "1", "Balance b/d", "b/d", _fmt_money(closing)])
            if mode_norm == "scaffold" and editable:
                hints[f"t{table_index}_r7_c4"] = "Balance c/d is the closing balance (amount owed to creditors)."
                hints[f"t{table_index}_r8_c4"] = "Totals (Dr): add the debit amounts, including Balance c/d."
                hints[f"t{table_index}_r8_c9"] = "Totals must balance: Total Dr = Total Cr."
                working_map[f"t{table_index}_r4_c2"] = f"t{table_index}_r4_c4"

        journal = {
            "journal_type": "control_account",
            "table_variant": "grade_project",
            "headers": gl_headers,
            "rows": rows,
            "header_rows": _control_header_rows(),
            "column_help": {},
            "allow_extra_rows": False,
        }
        return journal, correct, hints, working_map

    def _make_list_table(*, table_index: int, lst: Dict[str, Tuple[float, float]], editable: bool) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        editable_cols: List[int] = []
        if editable:
            editable_cols = [1, 2] if diff == "easy" else [0, 1, 2]

        rows: List[List[Dict[str, Any]]] = []
        correct: Dict[str, Any] = {}
        for i, nm in enumerate(lst.keys()):
            d, c = lst[nm]
            rendered_values = [
                nm,
                "" if editable or not d else _fmt_money(d),
                "" if editable or not c else _fmt_money(c),
            ]
            rows.append(_build_prefixed_row(table_index=table_index, row_index=i, values=rendered_values, editable_cols=editable_cols))
            correct[f"t{table_index}_r{i}_c0"] = nm
            correct[f"t{table_index}_r{i}_c1"] = _fmt_money(d) if d else ""
            correct[f"t{table_index}_r{i}_c2"] = _fmt_money(c) if c else ""

        dr_tot, cr_tot = _sum_list(lst)
        total_values = [
            "TOTAL",
            "" if editable or not dr_tot else _fmt_money(dr_tot),
            "" if editable or not cr_tot else _fmt_money(cr_tot),
        ]
        rows.append(_build_prefixed_row(table_index=table_index, row_index=len(lst), values=total_values, editable_cols=editable_cols))
        correct[f"t{table_index}_r{len(lst)}_c0"] = "TOTAL"
        correct[f"t{table_index}_r{len(lst)}_c1"] = _fmt_money(dr_tot) if dr_tot else ""
        correct[f"t{table_index}_r{len(lst)}_c2"] = _fmt_money(cr_tot) if cr_tot else ""

        journal = {
            "journal_type": "list",
            "table_variant": "grade_project",
            "headers": list_headers,
            "rows": rows,
            "heading": f"{'Debtors' if var == 'debtors' else 'Creditors'} list",
            "column_help": {},
            "allow_extra_rows": False,
        }
        return journal, correct

    def _add_reconciliation_list_hints(*, table_index: int, lst: Dict[str, Tuple[float, float]]) -> None:
        list_label = "Debtors" if var == "debtors" else "Creditors"
        for i, (nm, balances) in enumerate(lst.items()):
            d = _round_money(float((balances or (0.0, 0.0))[0] or 0.0))
            c = _round_money(float((balances or (0.0, 0.0))[1] or 0.0))
            name_key = f"t{table_index}_r{i}_c0"
            debit_key = f"t{table_index}_r{i}_c1"
            credit_key = f"t{table_index}_r{i}_c2"
            if diff != "easy":
                cell_hints[name_key] = f"Use the corrected account name for this {list_label.lower()} list row. Keep the same account holder unless an error moved the balance to the opposite ledger."
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=name_key,
                    role_in_requirement=f"Identify the correct {list_label.lower()} account for this row.",
                    evidence_from_question="Use the corrected list after applying all errors and omissions.",
                    rule_or_principle="A corrected list keeps the account holder with the balance that remains in that ledger after all adjustments.",
                    how_to_derive="Match the corrected balance to the correct customer or supplier name.",
                    transfer_tip="If a balance is transferred to the opposite ledger, it should not remain under this list entry.",
                )
            if d > 0.0:
                cell_hints[debit_key] = f"Enter the corrected debit balance for {nm}. Use the final adjusted amount that still belongs in the {list_label.lower()} ledger."
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=debit_key,
                    role_in_requirement=f"Enter the debit balance for {nm} in the corrected {list_label.lower()} list.",
                    evidence_from_question="Start from the supplied list and apply each listed correction that affects this account.",
                    rule_or_principle="Only the balance that remains on the debit side after all corrections belongs in this cell.",
                    how_to_derive=f"Adjust {nm}'s balance using the relevant errors, then place the final debit amount here.",
                    transfer_tip="If the balance moves to the credit side or to the opposite ledger, do not leave a debit amount here.",
                )
            else:
                cell_hints[debit_key] = f"Leave the debit column blank for {nm} if the corrected balance is not a debit balance in this {list_label.lower()} list."
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=debit_key,
                    role_in_requirement=f"Decide whether {nm} needs a debit entry in the corrected list.",
                    evidence_from_question="Compare the corrected balance of this account with the debit and credit columns.",
                    rule_or_principle="Only one side should contain the final balance for a single corrected list row.",
                    how_to_derive=f"After applying all corrections for {nm}, if no debit balance remains, leave this cell blank.",
                    transfer_tip="A transferred or credit balance must not stay in this debit column.",
                )
            if c > 0.0:
                cell_hints[credit_key] = f"Enter the corrected credit balance for {nm}. Use the final adjusted amount that still belongs in the {list_label.lower()} ledger."
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=credit_key,
                    role_in_requirement=f"Enter the credit balance for {nm} in the corrected {list_label.lower()} list.",
                    evidence_from_question="Start from the supplied list and apply each listed correction that affects this account.",
                    rule_or_principle="Only the balance that remains on the credit side after all corrections belongs in this cell.",
                    how_to_derive=f"Adjust {nm}'s balance using the relevant errors, then place the final credit amount here.",
                    transfer_tip="If the balance moves to the debit side or to the opposite ledger, do not leave a credit amount here.",
                )
            else:
                cell_hints[credit_key] = f"Leave the credit column blank for {nm} if the corrected balance is not a credit balance in this {list_label.lower()} list."
                _append_control_accounts_teaching_hint(
                    cell_teaching_map=cell_teaching_map,
                    cell_key=credit_key,
                    role_in_requirement=f"Decide whether {nm} needs a credit entry in the corrected list.",
                    evidence_from_question="Compare the corrected balance of this account with the debit and credit columns.",
                    rule_or_principle="Only one side should contain the final balance for a single corrected list row.",
                    how_to_derive=f"After applying all corrections for {nm}, if no credit balance remains, leave this cell blank.",
                    transfer_tip="A transferred or debit balance must not stay in this credit column.",
                )

    journals: List[Dict[str, Any]] = []
    correct_map: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    working_map: Dict[str, str] = {}

    if var == "debtors":
        j0, _, _, _ = _make_control_table(
            table_index=0,
            opening=supplied_opening_control,
            closing=supplied_closing,
            editable=False,
            dj_sales_amt=supplied_dj_sales,
            crj_bank_disc_amt=supplied_crj_bank_disc,
            daj_allow_amt=supplied_daj_allow,
            cpj_rd_amt=supplied_cpj_rd,
            pcj_paid_amt=supplied_pcj_paid,
            debt_gj_debits_amt=supplied_debt_gj_debits,
            debt_gj_credits_amt=supplied_debt_gj_credits,
        )
    else:
        j0, _, _, _ = _make_control_table(
            table_index=0,
            opening=supplied_opening_control,
            closing=supplied_closing,
            editable=False,
            cj_purchases_amt=supplied_cj_purchases,
            cpj_pay_disc_amt=supplied_cpj_pay_disc,
            caj_allow_amt=supplied_caj_allow,
            cred_gj_debits_amt=supplied_cred_gj_debits,
            cred_gj_credits_amt=supplied_cred_gj_credits,
            crj_bank_amt=supplied_crj_bank,
        )
    j1, _ = _make_list_table(table_index=1, lst=supplied_list, editable=False)
    j0["heading"] = f"Supplied {'Debtors' if var == 'debtors' else 'Creditors'} control account"
    j1["heading"] = f"Supplied {'Debtors' if var == 'debtors' else 'Creditors'} list"
    if var == "debtors":
        j2, c2, h2, w2 = _make_control_table(
            table_index=2,
            opening=opening_control,
            closing=closing_control,
            editable=True,
            dj_sales_amt=dj_sales,
            crj_bank_disc_amt=crj_bank_disc,
            daj_allow_amt=daj_allow,
            cpj_rd_amt=cpj_rd,
            pcj_paid_amt=pcj_paid,
            debt_gj_debits_amt=gj_debits,
            debt_gj_credits_amt=gj_credits,
        )
    else:
        j2, c2, h2, w2 = _make_control_table(
            table_index=2,
            opening=opening_control,
            closing=closing_control,
            editable=True,
            cj_purchases_amt=cj_purchases,
            cpj_pay_disc_amt=cpj_pay_disc,
            caj_allow_amt=caj_allow,
            cred_gj_debits_amt=gj_debits,
            cred_gj_credits_amt=gj_credits,
            crj_bank_amt=crj_bank,
        )
    j3, c3 = _make_list_table(table_index=3, lst=corrected_list, editable=True)
    j2["heading"] = f"Corrected {'Debtors' if var == 'debtors' else 'Creditors'} control account"
    j3["heading"] = f"Corrected {'Debtors' if var == 'debtors' else 'Creditors'} list"

    journals.extend([j0, j1, j2, j3])
    correct_map.update(c2)
    correct_map.update(c3)
    cell_hints.update(h2)
    working_map.update(w2)

    dr_tot, cr_tot = _sum_list(corrected_list)
    net = _round_money(dr_tot - cr_tot) if var == "debtors" else _round_money(cr_tot - dr_tot)
    reconciliation_meta = {
        "business": business,
        "month": month,
        "year": year,
        "variant": var,
        "difficulty": diff,
        "family": family_label,
        "correct_opening": opening_control,
        "correct_closing": closing_control,
        "net_list_total": net,
        "errors": list(errors),
        "correct_debtors_sales_total": dj_sales if var == "debtors" else 0.0,
        "correct_debtors_crj_total": crj_bank_disc if var == "debtors" else 0.0,
        "correct_creditors_cj_total": cj_purchases if var == "creditors" else 0.0,
        "correct_creditors_cpj_total": cpj_pay_disc if var == "creditors" else 0.0,
        "corrected_list": {name: [vals[0], vals[1]] for name, vals in corrected_list.items()},
    }
    followup_specs = _build_control_accounts_reconciliation_followup_specs(meta=reconciliation_meta)

    if mode_norm == "scaffold":
        if var == "debtors":
            cell_hints[f"t2_r0_c4"] = "Balance b/d is the corrected opening balance brought into the control account at the start of the month."
            cell_hints[f"t2_r1_c4"] = "Use the corrected DJ total for sales on the debit side of the Debtors control account."
            cell_hints[f"t2_r5_c9"] = "Use the corrected CRJ total for Bank and discount allowed on the credit side."
            cell_hints[f"t2_r6_c9"] = "Use the corrected DAJ total because allowances reduce the amount owed by debtors."
            cell_hints[f"t2_r8_c9"] = "Balance c/d is the closing balance after all corrected monthly entries have been posted."
            cell_hints[f"t2_r9_c4"] = "Total the debit side, including Balance c/d, so both sides of the control account balance."
            cell_hints[f"t2_r9_c9"] = "The credit total must equal the debit total once the account is balanced."
            cell_hints[f"t2_r10_c4"] = "Balance b/d next month must equal the previous Balance c/d."
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r0_c4",
                role_in_requirement="Enter the corrected opening balance in the Debtors control account.",
                evidence_from_question="Use the corrected control account, not the supplied incorrect one.",
                rule_or_principle="Balance b/d is the balance brought down from the previous period before the current month's postings.",
                how_to_derive="Start with the corrected opening balance before applying this month's journals and errors.",
                transfer_tip="Do not confuse the opening balance with the closing balance carried down at month end.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r1_c4",
                role_in_requirement="Post the corrected Debtors Journal total.",
                evidence_from_question="Use the corrected DJ total after applying all error adjustments.",
                rule_or_principle="Credit sales increase the Debtors control account on the debit side.",
                how_to_derive="Correct the DJ total first, then enter that amount on the debit side of the control account.",
                transfer_tip="Do not use the supplied incorrect DJ amount if an error changed it.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r5_c9",
                role_in_requirement="Post the corrected CRJ total to the credit side.",
                evidence_from_question="The CRJ entry reduces the amount owed by debtors.",
                rule_or_principle="Receipts from debtors reduce Debtors control and are posted on the credit side.",
                how_to_derive="Use the corrected CRJ total after fixing any listed receipt-related errors.",
                transfer_tip="The bank-and-discount row belongs on the credit side because it reduces what debtors owe.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r6_c9",
                role_in_requirement="Post the corrected Debtors Allowances total.",
                evidence_from_question="Allowances reduce debtors and therefore reduce the control account.",
                rule_or_principle="A debtors allowance is a credit entry in the Debtors control account.",
                how_to_derive="Correct the DAJ amount from the error list, then post the final total here.",
                transfer_tip="Use the allowances journal total, not an individual debtor adjustment amount, unless the scenario says otherwise.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r8_c9",
                role_in_requirement="Calculate the closing balance carried down.",
                evidence_from_question="Balance c/d is the final amount still owed by debtors after all corrected entries.",
                rule_or_principle="The balance c/d is the figure that makes the debit and credit totals equal.",
                how_to_derive="Add the debit side, add the credit-side entries before Balance c/d, and use the difference as the closing balance.",
                transfer_tip="This same amount must appear next month as Balance b/d.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r9_c4",
                role_in_requirement="Enter the debit total of the corrected control account.",
                evidence_from_question="Use every corrected debit amount, including Balance c/d.",
                rule_or_principle="A control account balances only when total debits equal total credits.",
                how_to_derive="Add Balance b/d, Sales, and any other debit-side corrected entries.",
                transfer_tip="After calculating this total, the credit total must match it exactly.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r10_c4",
                role_in_requirement="Carry the closing balance forward to the next month.",
                evidence_from_question="The first row of the next month repeats the previous Balance c/d as Balance b/d.",
                rule_or_principle="Balance b/d in the new month must equal Balance c/d from the previous month.",
                how_to_derive="Copy the closing balance carried down to the opening balance brought down next month.",
                transfer_tip="Do not recalculate this amount separately; it is the same figure as Balance c/d.",
            )
        else:
            cell_hints[f"t2_r0_c9"] = "Balance b/d is the corrected opening balance brought into the Creditors control account at the start of the month."
            cell_hints[f"t2_r1_c9"] = "Use the corrected CJ total for purchases on the credit side of the Creditors control account."
            cell_hints[f"t2_r4_c4"] = "Use the corrected CPJ total for Bank and discount received on the debit side."
            cell_hints[f"t2_r5_c4"] = "Use the corrected CAJ total because allowances reduce the amount owed to creditors."
            cell_hints[f"t2_r7_c4"] = "Balance c/d is the closing balance after all corrected monthly entries have been posted."
            cell_hints[f"t2_r8_c4"] = "Total the debit side, including Balance c/d, so both sides of the control account balance."
            cell_hints[f"t2_r8_c9"] = "The credit total must equal the debit total once the account is balanced."
            cell_hints[f"t2_r9_c9"] = "Balance b/d next month must equal the previous Balance c/d."
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r0_c9",
                role_in_requirement="Enter the corrected opening balance in the Creditors control account.",
                evidence_from_question="Use the corrected control account, not the supplied incorrect one.",
                rule_or_principle="Balance b/d is the balance brought down from the previous period before the current month's postings.",
                how_to_derive="Start with the corrected opening balance before applying this month's journals and errors.",
                transfer_tip="Do not confuse the opening balance with the closing balance carried down at month end.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r1_c9",
                role_in_requirement="Post the corrected Creditors Journal total.",
                evidence_from_question="Use the corrected CJ total after applying all error adjustments.",
                rule_or_principle="Credit purchases increase the Creditors control account on the credit side.",
                how_to_derive="Correct the CJ total first, then enter that amount on the credit side of the control account.",
                transfer_tip="Do not use the supplied incorrect CJ amount if an error changed it.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r4_c4",
                role_in_requirement="Post the corrected CPJ total to the debit side.",
                evidence_from_question="The CPJ entry reduces the amount owed to creditors.",
                rule_or_principle="Payments to creditors reduce Creditors control and are posted on the debit side.",
                how_to_derive="Use the corrected CPJ total after fixing any listed payment-related errors.",
                transfer_tip="The bank-and-discount row belongs on the debit side because it reduces what is owed to creditors.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r5_c4",
                role_in_requirement="Post the corrected Creditors Allowances total.",
                evidence_from_question="Allowances reduce creditors and therefore reduce the control account.",
                rule_or_principle="A creditors allowance is a debit entry in the Creditors control account.",
                how_to_derive="Correct the CAJ amount from the error list, then post the final total here.",
                transfer_tip="Use the allowances journal total, not an individual supplier adjustment amount, unless the scenario says otherwise.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r7_c4",
                role_in_requirement="Calculate the closing balance carried down.",
                evidence_from_question="Balance c/d is the final amount still owed to creditors after all corrected entries.",
                rule_or_principle="The balance c/d is the figure that makes the debit and credit totals equal.",
                how_to_derive="Add the credit side, add the debit-side entries before Balance c/d, and use the difference as the closing balance.",
                transfer_tip="This same amount must appear next month as Balance b/d.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r8_c4",
                role_in_requirement="Enter the debit total of the corrected control account.",
                evidence_from_question="Use every corrected debit amount, including Balance c/d.",
                rule_or_principle="A control account balances only when total debits equal total credits.",
                how_to_derive="Add Bank and discount received, Sundry allowances, and any other debit-side corrected entries including Balance c/d.",
                transfer_tip="After calculating this total, the credit total must match it exactly.",
            )
            _append_control_accounts_teaching_hint(
                cell_teaching_map=cell_teaching_map,
                cell_key="t2_r9_c9",
                role_in_requirement="Carry the closing balance forward to the next month.",
                evidence_from_question="The first row of the next month repeats the previous Balance c/d as Balance b/d.",
                rule_or_principle="Balance b/d in the new month must equal Balance c/d from the previous month.",
                how_to_derive="Copy the closing balance carried down to the opening balance brought down next month.",
                transfer_tip="Do not recalculate this amount separately; it is the same figure as Balance c/d.",
            )

        _add_reconciliation_list_hints(table_index=3, lst=corrected_list)
        total_row_index = len(base_list)
        cell_hints[f"t3_r{total_row_index}_c1"] = "TOTAL (Debit): add all debtor/creditor debit balances in the list."
        cell_hints[f"t3_r{total_row_index}_c2"] = "TOTAL (Credit): add all debtor/creditor credit balances in the list."
        cell_hints[f"t2_r8_c9" if var == "debtors" else f"t2_r7_c4"] = "Net check: the corrected control account closing balance must equal the net list total."
        _append_control_accounts_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=f"t3_r{total_row_index}_c1",
            role_in_requirement="Calculate the debit total of the corrected list.",
            evidence_from_question="Use the corrected balances in the list after taking every error into account.",
            rule_or_principle="The list total is the sum of the balances shown in that column.",
            how_to_derive="Add all debit balances in the corrected list.",
            transfer_tip="Only include balances that remain in that ledger after any transfer to the opposite ledger.",
        )
        _append_control_accounts_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=f"t3_r{total_row_index}_c2",
            role_in_requirement="Calculate the credit total of the corrected list.",
            evidence_from_question="Use the corrected balances in the list after taking every error into account.",
            rule_or_principle="The list total is the sum of the balances shown in that column.",
            how_to_derive="Add all credit balances in the corrected list.",
            transfer_tip="A transferred balance should disappear from this list if it moves to the opposite ledger.",
        )

    prompt_lines = [f"{business}"]
    if diff == "hard":
        prompt_lines.extend([
            f"{'Debtors' if var == 'debtors' else 'Creditors'} reconciliation",
            "",
            "Information A",
            f"General ledger figures for {month} {year}",
            "",
            "Information B",
            f"List extracted at the end of {month} {year}",
            "",
            "Information C",
            "Errors and omissions:",
        ])
    else:
        prompt_lines.extend([
            f"Control Accounts and Reconciliation ({'Debtors' if var == 'debtors' else 'Creditors'})",
            f"Month: {month} {year}",
            "",
            "Errors and omissions:",
        ])
    for i, e in enumerate(errors, start=1):
        prompt_lines.append(f"{i}. {e}")
    if diff == "hard":
        prompt_lines.extend(
            [
                "",
                "Required:",
                "1.1 Complete the corrected control account and balance it.",
                "1.2 Complete the corrected list.",
                "Show all calculations in brackets where applicable.",
            ]
        )
        if followup_specs:
            prompt_lines.extend([spec["prompt"] for spec in followup_specs])
    else:
        prompt_lines.extend(
            [
                "",
                "Required:",
                "1) Complete the corrected control account and balance it.",
                "2) Complete the corrected list.",
            ]
        )
        if followup_specs:
            prompt_lines.extend([
                "",
                "Extension items:",
                *[spec["prompt"] for spec in followup_specs],
            ])

    out = _make_journal(
        prompt="\n".join(prompt_lines),
        journal_type="control_accounts_reconciliation",
        headers=gl_headers,
        rows=j2["rows"],
        correct_map=correct_map,
        guidelines=[
            "If balances are not the same, investigate journal totals vs postings to individual accounts.",
            "Balance c/d is carried down and becomes Balance b/d next month.",
        ],
        cell_hints=cell_hints if mode_norm == "scaffold" else None,
        cell_teaching_map=cell_teaching_map if mode_norm == "scaffold" else None,
        working_map=working_map if mode_norm == "scaffold" else None,
    )
    out["prompt_journals"] = [j0, j1]
    out["journals"] = journals
    out["journal"] = journals[-1]
    out["correct_map"] = correct_map
    out["control_accounts_family"] = family_label
    out["control_accounts_variant"] = var
    out["difficulty"] = diff
    out["reconciliation_meta"] = reconciliation_meta
    out["reconciliation_followups"] = [{"prompt": str(spec.get("prompt") or ""), "label": str(spec.get("label") or "")} for spec in followup_specs]
    return out


def _build_control_accounts_reconciliation_followup_specs(*, meta: Dict[str, Any]) -> List[Dict[str, Any]]:
    diff = _normalize_control_accounts_difficulty(meta.get("difficulty"))
    var = _normalize_control_accounts_variant(meta.get("variant"))
    family = str(meta.get("family") or "").strip().lower()
    if diff == "easy":
        return []

    specs: List[Dict[str, Any]] = []
    if var == "debtors":
        crj_total = float(meta.get("correct_debtors_crj_total") or 0.0)
        discount_total = _round_money(max(20.0, crj_total * 0.05)) if crj_total > 0.0 else 0.0
        numbering = ["3)", "4)", "5)"] if diff != "hard" else ["1.3", "1.4", "1.5"]
        if family == "recon_control_plus_list_plus_terms":
            specs.extend([
                {
                    "label": "Credit term",
                    "prompt": f"{numbering[0]} Define the term credit term.",
                    "value": "The period allowed to a debtor to settle the amount owing.",
                    "guidance": [
                        "Give a short definition, not an example.",
                        "Focus on the time allowed before payment is due.",
                    ],
                },
                {
                    "label": "Actual cash received from debtors",
                    "prompt": f"{numbering[1]} Use the corrected CRJ total to calculate the actual cash received from debtors if discount allowed amounted to {_fmt_money(discount_total)}.",
                    "value": f"CRJ total {_fmt_money(crj_total)} - discount allowed {_fmt_money(discount_total)} = {_fmt_money(_round_money(crj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CRJ total from the control account, not the supplied incorrect amount.",
                        "Subtract discount allowed to isolate the cash received.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Reason for agreement",
                    "prompt": f"{numbering[2]} Explain why the corrected debtors list must agree with the corrected closing balance of the Debtors control account.",
                    "value": "The list is the total of the individual debtor balances that make up the Debtors control balance after all corrections, so the net list total must equal the corrected control closing balance.",
                    "guidance": [
                        "Mention that the control account summarises the individual debtor accounts.",
                        "State that both records must reflect the same corrected balances after all errors are fixed.",
                    ],
                })
        elif family == "recon_control_plus_list_plus_strategy":
            specs.extend([
                {
                    "label": "Actual cash received from debtors",
                    "prompt": f"{numbering[0]} Use the corrected CRJ total to calculate the actual cash received from debtors if discount allowed amounted to {_fmt_money(discount_total)}.",
                    "value": f"CRJ total {_fmt_money(crj_total)} - discount allowed {_fmt_money(discount_total)} = {_fmt_money(_round_money(crj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CRJ total from the control account.",
                        "Subtract discount allowed to isolate the cash portion.",
                    ],
                },
                {
                    "label": "Advice on improving collections",
                    "prompt": f"{numbering[1]} State two practical actions {meta.get('business') or 'the business'} can use to improve collections from debtors.",
                    "value": "Any valid points: send statements promptly; enforce credit limits; follow up overdue accounts quickly.",
                    "guidance": [
                        "Give practical actions the owner can implement.",
                        "Tie the advice to collection and overdue-account control.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Transfer procedure",
                    "prompt": f"{numbering[2]} State one control step that should be followed when a debtor has a credit balance that must be transferred to the creditors ledger.",
                    "value": "Any valid point: authorise the transfer, process it through the General Journal, and update both subsidiary ledgers so the balance appears in the correct ledger.",
                    "guidance": [
                        "Focus on authorisation, correct journal processing, and updating the opposite ledger.",
                        "Show that the balance must not remain in both ledgers.",
                    ],
                })
        else:
            specs.extend([
                {
                    "label": "Actual cash received from debtors",
                    "prompt": f"{numbering[0]} Use the corrected CRJ total to calculate the actual cash received from debtors if discount allowed amounted to {_fmt_money(discount_total)}.",
                    "value": f"CRJ total {_fmt_money(crj_total)} - discount allowed {_fmt_money(discount_total)} = {_fmt_money(_round_money(crj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CRJ total from the control account, not the supplied amount.",
                        "Subtract discount allowed to isolate the cash received.",
                    ],
                },
                {
                    "label": "Reason for agreement",
                    "prompt": f"{numbering[1]} Explain how the owner should verify that the final debtors list agrees with the corrected Debtors control balance.",
                    "value": "Add the corrected debtors list and compare the net list total with the corrected closing balance of the Debtors control account; the two amounts must agree.",
                    "guidance": [
                        "Mention the corrected list total and the corrected control closing balance.",
                        "State that the two amounts must agree after all corrections are made.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Advice on improving collections",
                    "prompt": f"{numbering[2]} Give one valid recommendation for improving the collection of overdue debtors.",
                    "value": "Any valid point: send statements promptly; enforce credit limits; follow up overdue accounts quickly.",
                    "guidance": [
                        "Give a practical action, not a definition.",
                        "Tie the advice directly to debtor collection and credit control.",
                    ],
                })
        return specs
    else:
        cpj_total = float(meta.get("correct_creditors_cpj_total") or 0.0)
        discount_total = _round_money(max(20.0, cpj_total * 0.04)) if cpj_total > 0.0 else 0.0
        numbering = ["3)", "4)", "5)"] if diff != "hard" else ["1.3", "1.4", "1.5"]
        if family == "recon_control_plus_list_plus_terms":
            specs.extend([
                {
                    "label": "Credit limit",
                    "prompt": f"{numbering[0]} Define the term credit limit.",
                    "value": "The maximum amount that may be owed on a credit account.",
                    "guidance": [
                        "Define the ceiling or maximum amount allowed.",
                        "Do not confuse it with the payment period.",
                    ],
                },
                {
                    "label": "Actual cash paid to creditors",
                    "prompt": f"{numbering[1]} Use the corrected CPJ total to calculate the actual cash paid to creditors if discount received amounted to {_fmt_money(discount_total)}.",
                    "value": f"CPJ total {_fmt_money(cpj_total)} - discount received {_fmt_money(discount_total)} = {_fmt_money(_round_money(cpj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CPJ total from the control account, not the supplied incorrect amount.",
                        "Subtract discount received to isolate the cash paid.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Reason for agreement",
                    "prompt": f"{numbering[2]} Explain why the corrected creditors list must agree with the corrected closing balance of the Creditors control account.",
                    "value": "The list is the total of the individual supplier balances that make up the Creditors control balance after all corrections, so the net list total must equal the corrected control closing balance.",
                    "guidance": [
                        "Mention that the control account summarises the individual supplier accounts.",
                        "State that both records must reflect the same corrected balances after all errors are fixed.",
                    ],
                })
        elif family == "recon_control_plus_list_plus_supplier_control":
            specs.extend([
                {
                    "label": "Actual cash paid to creditors",
                    "prompt": f"{numbering[0]} Use the corrected CPJ total to calculate the actual cash paid to creditors if discount received amounted to {_fmt_money(discount_total)}.",
                    "value": f"CPJ total {_fmt_money(cpj_total)} - discount received {_fmt_money(discount_total)} = {_fmt_money(_round_money(cpj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CPJ total from the control account.",
                        "Subtract discount received to isolate the cash portion.",
                    ],
                },
                {
                    "label": "Supplier control procedure",
                    "prompt": f"{numbering[1]} State two procedures {meta.get('business') or 'the business'} should use to improve control over supplier accounts.",
                    "value": "Any valid points: match invoices to orders and delivery notes; check goods before payment; review supplier statements monthly.",
                    "guidance": [
                        "Give practical procedures that prevent payment and posting errors.",
                        "Focus on supplier records, delivery checks, and reconciliations.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Transfer procedure",
                    "prompt": f"{numbering[2]} State one control step that should be followed when a supplier has a debit balance that must be transferred to the debtors ledger.",
                    "value": "Any valid point: authorise the transfer, process it through the General Journal, and update both subsidiary ledgers so the balance appears in the correct ledger.",
                    "guidance": [
                        "Focus on authorisation, correct journal processing, and updating the opposite ledger.",
                        "Show that the balance must not remain in both ledgers.",
                    ],
                })
        else:
            specs.extend([
                {
                    "label": "Actual cash paid to creditors",
                    "prompt": f"{numbering[0]} Use the corrected CPJ total to calculate the actual cash paid to creditors if discount received amounted to {_fmt_money(discount_total)}.",
                    "value": f"CPJ total {_fmt_money(cpj_total)} - discount received {_fmt_money(discount_total)} = {_fmt_money(_round_money(cpj_total - discount_total))}",
                    "guidance": [
                        "Use the corrected CPJ total from the control account, not the supplied amount.",
                        "Subtract discount received to isolate the cash paid.",
                    ],
                },
                {
                    "label": "Reason for agreement",
                    "prompt": f"{numbering[1]} Explain how the owner should verify that the final creditors list agrees with the corrected Creditors control balance.",
                    "value": "Add the corrected creditors list and compare the net list total with the corrected closing balance of the Creditors control account; the two amounts must agree.",
                    "guidance": [
                        "Mention the corrected list total and the corrected control closing balance.",
                        "State that the two amounts must agree after all corrections are made.",
                    ],
                },
            ])
            if diff == "hard":
                specs.append({
                    "label": "Supplier control procedure",
                    "prompt": f"{numbering[2]} Give one valid supplier-control procedure that would reduce posting or payment errors.",
                    "value": "Any valid point: match invoices to orders and delivery notes; check goods before payment; review supplier statements monthly.",
                    "guidance": [
                        "Give a practical procedure, not a definition.",
                        "Tie the answer directly to supplier records, checks, and reconciliations.",
                    ],
                })
        return specs


def _build_control_accounts_reconciliation_followups(*, question: Dict[str, Any]) -> List[Dict[str, Any]]:
    meta = dict(question.get("reconciliation_meta") or {})
    specs = _build_control_accounts_reconciliation_followup_specs(meta=meta)
    return _build_answer_part_hints([
        (
            str(spec.get("label") or "Answer part"),
            str(spec.get("value") or ""),
            list(spec.get("guidance") or []),
        )
        for spec in specs
    ])


def _validate_control_accounts_reconciliation_output(question: Dict[str, Any]) -> None:
    meta = dict(question.get("reconciliation_meta") or {})
    if not meta:
        raise _ControlAccountsScenarioValidationError("Control accounts reconciliation output is missing reconciliation metadata.")

    var = _normalize_control_accounts_variant(meta.get("variant"))
    correct_closing = _round_money(float(meta.get("correct_closing") or 0.0))
    list_payload = dict(meta.get("corrected_list") or {})
    debit_total = _round_money(sum(float((vals or [0.0, 0.0])[0]) for vals in list_payload.values()))
    credit_total = _round_money(sum(float((vals or [0.0, 0.0])[1]) for vals in list_payload.values()))
    net_total = _round_money(debit_total - credit_total) if var == "debtors" else _round_money(credit_total - debit_total)
    if net_total != correct_closing:
        raise _ControlAccountsScenarioValidationError("Corrected list total does not reconcile to the corrected control closing balance.")

    correct_map = dict(question.get("correct_map") or {})
    corrected_control = None
    journals = list(question.get("journals") or [])
    if len(journals) >= 3:
        corrected_control = journals[2]
    closing_key = ""
    if isinstance(corrected_control, dict):
        for row in list(corrected_control.get("rows") or []):
            if var == "debtors" and len(row) > 9 and str((row[7] or {}).get("value") or "") == "Balance c/d":
                closing_key = str((row[9] or {}).get("cell_id") or "")
                break
            if var == "creditors" and len(row) > 4 and str((row[2] or {}).get("value") or "") == "Balance c/d":
                closing_key = str((row[4] or {}).get("cell_id") or "")
                break
    if not closing_key or str(correct_map.get(closing_key) or "") != _fmt_money(correct_closing):
        raise _ControlAccountsScenarioValidationError("Corrected control account closing balance does not match the expected answer map.")

    list_total_row = len(list_payload)
    debit_key = f"t3_r{list_total_row}_c1"
    credit_key = f"t3_r{list_total_row}_c2"
    expected_debit = _fmt_money(debit_total) if debit_total else ""
    expected_credit = _fmt_money(credit_total) if credit_total else ""
    if str(correct_map.get(debit_key) or "") != expected_debit:
        raise _ControlAccountsScenarioValidationError("Corrected list debit total does not match the expected answer map.")
    if str(correct_map.get(credit_key) or "") != expected_credit:
        raise _ControlAccountsScenarioValidationError("Corrected list credit total does not match the expected answer map.")

    diff = _normalize_control_accounts_difficulty(meta.get("difficulty"))
    followup_specs = _build_control_accounts_reconciliation_followup_specs(meta=meta)
    answer_part_hints = list(question.get("answer_part_hints") or [])
    prompt_text = str(question.get("prompt") or "")
    if diff == "easy":
        if followup_specs or answer_part_hints:
            raise _ControlAccountsScenarioValidationError("Easy control accounts reconciliation should not emit follow-up parts.")
    else:
        if len(answer_part_hints) != len(followup_specs):
            raise _ControlAccountsScenarioValidationError("Control accounts reconciliation follow-up memo count does not match the follow-up specification count.")
        for spec in followup_specs:
            prompt_line = str(spec.get("prompt") or "").strip()
            label = str(spec.get("label") or "").strip()
            if prompt_line and prompt_line not in prompt_text:
                raise _ControlAccountsScenarioValidationError(f"Control accounts reconciliation prompt is missing follow-up line: {prompt_line}")
            if label and not any(str(item.get("label") or "").strip() == label for item in answer_part_hints if isinstance(item, dict)):
                raise _ControlAccountsScenarioValidationError(f"Control accounts reconciliation answer_part_hints is missing follow-up label: {label}")

    cell_hints = dict(question.get("cell_hints") or {})
    cell_teaching_map = dict(question.get("cell_teaching_map") or {})
    if cell_hints or cell_teaching_map:
        required_hint_keys = [debit_key, credit_key]
        if var == "debtors":
            required_hint_keys.extend(["t2_r8_c9", "t2_r9_c4", "t2_r10_c4"])
        else:
            required_hint_keys.extend(["t2_r7_c4", "t2_r8_c4", "t2_r9_c9"])
        for cell_key in required_hint_keys:
            if cell_key not in cell_hints and cell_key not in cell_teaching_map:
                raise _ControlAccountsScenarioValidationError(f"Control accounts reconciliation hint coverage is missing for {cell_key}.")


def make_control_accounts_reconciliation_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    last_error: Optional[_ControlAccountsScenarioValidationError] = None
    for _ in range(MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS):
        try:
            out = _make_control_accounts_reconciliation_once(r=r, difficulty=difficulty, mode=mode, variant=variant, business=business)
            out["answer_part_hints"] = _build_control_accounts_reconciliation_followups(question=out)
            _validate_control_accounts_reconciliation_output(out)
            return out
        except _ControlAccountsScenarioValidationError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise _ControlAccountsScenarioValidationError("Could not generate a valid control accounts reconciliation question.")


def make_control_accounts_internal_control_typed(
    *,
    r: random.Random,
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    var = str(variant or "debtors").strip().lower()
    if var not in ("debtors", "creditors"):
        var = "debtors"

    business = str(business or pick_business_name(r=r)).strip()
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    guidelines = [
        "A strong internal control measure should either prevent an error or make it easier to detect quickly.",
        "Good answers usually refer to reconciliation, segregation of duties, document control, authorisation, or matching procedures.",
        "Tie the control measure to the risk named in the scenario.",
    ]

    if var == "debtors":
        prompt = (
            f"{business}\n"
            f"Internal control over Debtors ({month})\n\n"
            "Information:\n"
            "The owner noticed that debtors' accounts are sometimes posted late and the Debtors Control account does not always agree with the debtors list at month-end.\n\n"
            "Required:\n"
            "List TWO internal control procedures that must be applied in the business to maintain proper control over debts."
        )
        answers = r.sample([
            "Reconcile the Debtors Control account to the debtors list every month and investigate differences immediately.",
            "Separate the duties for granting credit, recording source documents, posting debtor accounts and checking the postings.",
            "Pre-number invoices, receipts and credit notes and account for all missing documents.",
            "Approve credit limits before goods are sold on credit and review overdue accounts regularly.",
        ], k=2)
    else:
        prompt = (
            f"{business}\n"
            f"Internal control over Creditors ({month})\n\n"
            "Information:\n"
            "The owner noticed that supplier transactions are not always checked carefully and the Creditors Control account does not always agree with the creditors list at month-end.\n\n"
            "Required:\n"
            "List TWO internal control procedures that must be applied in the business to maintain proper control over creditors."
        )
        answers = r.sample([
            "Reconcile the Creditors Control account to the creditors list every month and investigate differences immediately.",
            "Separate the duties for ordering goods, receiving goods, recording source documents, posting creditor accounts and checking the postings.",
            "Pre-number invoices, debit notes and credit notes and account for all missing documents.",
            "Match supplier invoices to orders and delivery notes before the transaction is recorded or paid.",
        ], k=2)

    prompt_norm = prompt.lower()
    if "two" not in prompt_norm or "maintain proper control" not in prompt_norm:
        raise _ControlAccountsScenarioValidationError("Internal control prompt lost its exam-style wording.")

    sample_answer = "\n".join(f"{idx + 1}. {answer}" for idx, answer in enumerate(answers))
    out = _make_typed(prompt=prompt, sample_answer=sample_answer)
    out["guidelines"] = guidelines
    out["control_accounts_family"] = "internal_control_typed"
    out["control_accounts_variant"] = var
    out["answer_part_hints"] = _build_answer_part_hints([
        ("Control measure 1", answers[0], guidelines),
        ("Control measure 2", answers[1], guidelines),
    ])
    return out


def make_control_accounts_opening_balance_calc(
    *,
    r: random.Random,
    difficulty: str = "easy",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    diff = _normalize_control_accounts_difficulty(difficulty)
    var = _normalize_control_accounts_variant(variant)
    last_error: Optional[_ControlAccountsScenarioValidationError] = None
    previous_period_map = {
        "March": ("February", 28),
        "June": ("May", 31),
        "September": ("August", 31),
        "November": ("October", 31),
    }

    for _ in range(MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS):
        try:
            business_name = str(business or pick_business_name(r=r)).strip()
            month = r.choice(["March", "June", "September", "November"])
            year = int(r.choice([2020, 2021, 2022]))
            previous_month, previous_day = previous_period_map[month]

            if var == "debtors":
                debit_total = float(r.choice([14300.0, 16240.0, 18460.0, 21980.0, 28440.0]))
                credit_total = float(r.choice([240.0, 480.0, 620.0, 960.0]))
                which = "debtors"
                formula = "Debit total - Credit total"
                explanation = "Debtors control opens with the net amount owed by debtors to the business."
                opening_question = f"Calculate the amount owed by debtors on 1 {month} {year}."
                correct_value = _round_money(debit_total - credit_total)
            else:
                credit_total = float(r.choice([18240.0, 21680.0, 27420.0, 28600.0, 31860.0]))
                debit_total = float(r.choice([180.0, 340.0, 520.0, 860.0]))
                which = "creditors"
                formula = "Credit total - Debit total"
                explanation = "Creditors control opens with the net amount the business owes to creditors."
                opening_question = f"Calculate the amount owed to creditors on 1 {month} {year}."
                correct_value = _round_money(credit_total - debit_total)

            if correct_value <= 0.0:
                raise _ControlAccountsScenarioValidationError("Opening balance calculation question produced a non-positive net balance.")

            if diff == "easy":
                prompt_lines = [
                    f"{business_name}",
                    f"{month} {year} {which.title()} list totals:",
                    f"Debit total: R{_fmt_money(debit_total)}",
                    f"Credit total: R{_fmt_money(credit_total)}",
                    "",
                    "Required:",
                    f"Calculate the opening balance of the {'Debtors' if var == 'debtors' else 'Creditors'} control account.",
                ]
            else:
                prompt_lines = [
                    f"{business_name}",
                    "Additional information:",
                    f"The {which.title()} list totals on {previous_day} {previous_month} {year} are as follows:",
                    f"Debit: R{_fmt_money(debit_total)}",
                    f"Credit: R{_fmt_money(credit_total)}",
                    "",
                    "Required:",
                    opening_question,
                ]
                if diff == "hard":
                    prompt_lines.append(
                        f"Use the net {which} list total to determine the opening balance that will appear in the {'Debtors' if var == 'debtors' else 'Creditors'} Control account."
                    )

            substitution_line = f"Substitution: R{_fmt_money(debit_total)} - R{_fmt_money(credit_total)}" if var == "debtors" else f"Substitution: R{_fmt_money(credit_total)} - R{_fmt_money(debit_total)}"
            derivation_lines = [
                f"Formula: {formula}",
                substitution_line,
                f"Opening balance on 1 {month} {year}: R{_fmt_money(correct_value)}",
                explanation,
            ]

            prompt = "\n".join(prompt_lines)
            prompt_norm = prompt.lower()
            if diff in {"medium", "hard"}:
                if "list totals on" not in prompt_norm:
                    raise _ControlAccountsScenarioValidationError("Opening balance calc medium/hard prompt must be anchored to list totals on a stated date.")
                if var == "debtors" and "amount owed by debtors" not in prompt_norm:
                    raise _ControlAccountsScenarioValidationError("Debtors opening balance calc must ask for the amount owed by debtors.")
                if var == "creditors" and "amount owed to creditors" not in prompt_norm:
                    raise _ControlAccountsScenarioValidationError("Creditors opening balance calc must ask for the amount owed to creditors.")

            out = _make_typed(prompt=prompt, sample_answer="\n".join(derivation_lines))
            out["question_type"] = "calc"
            out["correct_value"] = float(correct_value)
            out["unit"] = "R"
            out["expected_answer_type"] = "number"
            out["guidelines"] = [
                explanation,
                "Use the net total of the list, not only one side of the list.",
                "Debtors control normally opens with a debit balance; creditors control normally opens with a credit balance.",
            ]
            out["derivation_map"] = {"value": "\n".join(derivation_lines)}
            out["control_accounts_family"] = "opening_balance_calc"
            out["control_accounts_variant"] = var
            out["difficulty"] = diff
            out["answer_part_hints"] = _build_answer_part_hints([
                ("Formula", derivation_lines[0], out["guidelines"]),
                ("Substitution", derivation_lines[1], out["guidelines"]),
                ("Opening balance", derivation_lines[2], out["guidelines"]),
            ])
            return out
        except _ControlAccountsScenarioValidationError as exc:
            last_error = exc
            continue

    if last_error is not None:
        raise last_error
    raise _ControlAccountsScenarioValidationError("Could not generate a valid control account opening balance question.")


def _parse_control_accounts_analysis_entry(entry_text: str) -> List[str]:
    text = str(entry_text or "").strip()
    if not text:
        return ["", "", "", "", ""]

    tokens = text.split()
    if tokens and len(tokens[0]) == 4 and tokens[0].isdigit():
        tokens = tokens[1:]
    if len(tokens) < 3:
        raise _ControlAccountsScenarioValidationError("Control accounts analysis entry is too short to render as a table row.")

    month = tokens[0]
    day = tokens[1]
    tail = tokens[2:]
    if len(tail) >= 2 and str(tail[-2]).startswith("R"):
        amount_text = f"{tail[-2]} {tail[-1]}"
        tail = tail[:-2]
    elif tail and str(tail[-1]).startswith("R"):
        amount_text = str(tail[-1])
        tail = tail[:-1]
    else:
        raise _ControlAccountsScenarioValidationError("Control accounts analysis entry is missing a renderable amount.")

    fol_candidates = {"DJ", "CJ", "CRJ", "CPJ", "DAJ", "CAJ", "GJ", "PCJ", "b/d", "c/d"}
    fol = str(tail[-1]) if tail and str(tail[-1]) in fol_candidates else ""
    details_tokens = tail[:-1] if fol else tail
    details = " ".join(str(token) for token in details_tokens).strip()
    amount = str(amount_text).replace("R", "", 1).strip()
    return [month, day, details, fol, amount]


def _build_control_accounts_analysis_prompt_journal(*, business: str, info_lines: List[str]) -> Dict[str, Any]:
    if not info_lines:
        raise _ControlAccountsScenarioValidationError("Control accounts analysis prompt journal requires info lines.")

    header_line = str(info_lines[0] or "").strip()
    account_label = header_line
    fol = ""
    if header_line.lower().startswith("dr ") and header_line.lower().endswith(" cr"):
        account_label = header_line[3:-3].strip()
    if "(" in account_label and ")" in account_label:
        open_idx = account_label.rfind("(")
        close_idx = account_label.rfind(")")
        if close_idx > open_idx >= 0:
            fol = account_label[open_idx + 1:close_idx].strip()
            account_label = account_label[:open_idx].strip()

    rows: List[List[Dict[str, Any]]] = []
    for row_index, info_line in enumerate(info_lines[1:]):
        raw_parts = [part.strip() for part in str(info_line or "").split("|")]
        left_values = _parse_control_accounts_analysis_entry(raw_parts[0] if raw_parts else "")
        right_values = _parse_control_accounts_analysis_entry(raw_parts[1] if len(raw_parts) > 1 else "")
        rows.append(_build_prefixed_row(
            table_index=98,
            row_index=row_index,
            values=[*left_values, *right_values],
            editable_cols=[],
        ))

    return {
        "journal_type": "control_account_prompt",
        "table_variant": "grade_project",
        "headers": _general_ledger_account_headers(),
        "rows": rows,
        "header_rows": [
            [{"label": f"General ledger of {business}", "colSpan": 10}],
            [{"label": "Dr.", "colSpan": 1}, {"label": account_label, "colSpan": 8}, {"label": "Cr.", "colSpan": 1}],
            [{"label": "", "colSpan": 1}, {"label": fol, "colSpan": 8}, {"label": "", "colSpan": 1}],
        ],
        "allow_extra_rows": False,
    }


def make_control_accounts_analysis_typed(
    *,
    r: random.Random,
    difficulty: str = "medium",
    variant: str = "debtors",
    business: Optional[str] = None,
) -> Dict[str, Any]:
    diff = _normalize_control_accounts_difficulty(difficulty)
    if diff == "easy":
        diff = "medium"
    var = _normalize_control_accounts_variant(variant)
    last_error: Optional[_ControlAccountsScenarioValidationError] = None

    for _ in range(MAX_CONTROL_ACCOUNTS_GENERATION_ATTEMPTS):
        try:
            if var == "debtors":
                guidelines = [
                    "Use the exact amount, side and journal clue named in the question before answering.",
                    "For debtors, the amount owed is the debit list total less the credit list total.",
                    "DAJ entries reduce debtors, DJ entries increase debtors, and GJ entries need a valid adjustment reason.",
                    "Verify the closing balance against the net debtors list for the same date.",
                ]
                if diff == "medium":
                    business_name = str(business or pick_business_name(r=r)).strip()
                    title = "March 2011 Debtors control account analysis"
                    info_lines = [
                        "Dr Debtors Control (B7) Cr",
                        "2011 Mar 1 Balance b/d R13 680 | 2011 Mar 30 Bank and discount allowed CRJ R19 300",
                        "2011 Mar 30 Sales DJ R18 200 | 2011 Mar 30 Debtors allowances DAJ R3 100",
                        "2011 Mar 30 Bank CPJ R240 | 2011 Mar 30 Journal credits GJ R640",
                        "2011 Mar 30 Petty cash PCJ R160 | 2011 Mar 30 Balance c/d R10 080",
                        "2011 Mar 30 Journal debits GJ R840",
                    ]
                    additional_lines = ["Debtors list on 28 February 2011: Debit R14 300; Credit R620."]
                    reason_840 = r.choice([
                        "Interest charged on overdue debtor accounts.",
                        "Correction of an error in a debtor's account.",
                        "Transfer of an account from the creditors ledger to the debtors ledger.",
                    ])
                    if r.random() < 0.5:
                        family_label = "analysis_typed_medium_debtors_opening"
                        question_answer_pairs = [
                            ("What is the amount owed by debtors on 1 March 2011?", "R13 680."),
                            ("State the contra account for the amount of R3 100 on the credit side.", "Debtors allowances."),
                            ("Name the source document supporting the entry 'Sales, DJ, R18 200'.", "Duplicate invoice."),
                            ("Give one valid reason for the amount of R840 on the debit side (Journal debits, GJ).", reason_840),
                        ]
                    else:
                        family_label = "analysis_typed_medium_debtors_source_doc"
                        question_answer_pairs = [
                            ("What is the amount owed by debtors on 1 March 2011?", "R13 680."),
                            ("State the contra account for the amount of R240 on the debit side.", "Bank."),
                            ("Give one valid reason for the amount of R160 on the debit side (Petty cash, PCJ).", "Carriage on purchases paid on behalf of a debtor and debited to that debtor's account."),
                            ("Name the source document supporting the entry 'Journal credits, GJ, R640'.", "Journal voucher."),
                        ]
                else:
                    business_name = str(business or pick_business_name(r=r)).strip()
                    title = "May 2019 Debtors control account exam-style analysis"
                    info_lines = [
                        "Dr Debtors Control (B7) Cr",
                        "2019 May 1 Balance b/d R41 000 | 2019 May 31 Debtors allowances DAJ R7 500",
                        "2019 May 31 Sales DJ R52 500 | 2019 May 31 Bank CRJ R12 000",
                        "2019 May 31 Bank CPJ R2 100 | 2019 May 31 Discount allowed CRJ R600",
                        "2019 May 31 Sundry accounts GJ R1 400 | 2019 May 31 Sundry accounts GJ R13 200",
                        "2019 May 31 Balance c/d R63 700 | 2019 May 31 Totals R97 000",
                        "2019 Jun 1 Balance b/d R63 700",
                    ]
                    additional_lines = ["Debtors list on 31 May 2019: Debit R64 300; Credit R600."]
                    reason_credit = r.choice([
                        "Bad debts written off.",
                        "Correction of an error in a debtor's account.",
                        "Transfer of an account to the creditors ledger.",
                    ])
                    reason_debit = r.choice([
                        "Interest charged on overdue debtor accounts.",
                        "Correction of an error in a debtor's account.",
                        "Transfer of an account from the creditors ledger to the debtors ledger.",
                    ])
                    if r.random() < 0.5:
                        family_label = "analysis_typed_hard_debtors_q7a"
                        question_answer_pairs = [
                            ("Provide the detail for the entry of R7 500 on the credit side.", "Debtors allowances."),
                            ("Give the journal folio for the entry of R52 500 on the debit side.", "DJ."),
                            ("Name the source document supporting the R7 500 credit-side entry.", "Credit note."),
                            ("Give one valid reason for the R13 200 on the credit side (Sundry accounts, GJ).", reason_credit),
                            ("Give the totals at the end of the month on both sides.", "R97 000 on both sides."),
                            ("Give the closing balance on 31 May 2019.", "R63 700."),
                            ("Explain how the owner should verify that the closing balance is correct.", "Compare the closing Debtors Control balance with the net debtors list total for 31 May 2019; the two must agree."),
                        ]
                    else:
                        family_label = "analysis_typed_hard_debtors_q7b"
                        question_answer_pairs = [
                            ("Provide the detail for the entry of R12 000 on the credit side.", "Bank."),
                            ("Name the source document supporting the R7 500 credit-side entry.", "Credit note."),
                            ("Give one valid reason for the R1 400 on the debit side (Sundry accounts, GJ).", reason_debit),
                            ("Give the journal folio for the entry of R52 500 on the debit side.", "DJ."),
                            ("Give the totals at the end of the month on both sides.", "R97 000 on both sides."),
                            ("Give the closing balance on 31 May 2019.", "R63 700."),
                            ("Give the opening balance on 1 June 2019.", "R63 700."),
                            ("Explain how the owner should verify that the closing balance is correct.", "Compare the closing Debtors Control balance with the net debtors list total for 31 May 2019; the two must agree."),
                        ]
            else:
                guidelines = [
                    "Use the exact amount, side and journal clue named in the question before answering.",
                    "For creditors, the amount owed is the credit list total less the debit list total.",
                    "CAJ entries reduce creditors, CJ entries increase creditors, and GJ entries need a valid adjustment reason.",
                    "Verify the closing balance against the net creditors list for the same date.",
                ]
                if diff == "medium":
                    business_name = str(business or pick_business_name(r=r)).strip()
                    title = "March 2011 Creditors control account analysis"
                    info_lines = [
                        "Dr Creditors Control (B8) Cr",
                        "2011 Mar 31 Bank and discount received CPJ R35 400 | 2011 Mar 1 Balance b/d R28 260",
                        "2011 Mar 31 Sundry allowances CAJ R2 300 | 2011 Mar 31 Sundry purchases CJ R21 800",
                        "2011 Mar 31 Journal debits GJ R840 | 2011 Mar 31 Journal credits GJ R610",
                        "2011 Mar 31 Balance c/d R12 270 | 2011 Mar 31 Bank CRJ R140",
                        "2011 Apr 1 Balance b/d R12 270",
                    ]
                    additional_lines = ["Creditors list on 1 March 2011: Debit R340; Credit R28 600."]
                    reason_610 = r.choice([
                        "Correction of an error in a creditor's account.",
                        "Interest charged on an overdue creditor account.",
                        "Transfer of an account between creditors and debtors ledgers.",
                    ])
                    if r.random() < 0.5:
                        family_label = "analysis_typed_medium_creditors_main"
                        question_answer_pairs = [
                            ("What is the amount owed to creditors on 1 March 2011?", "R28 260."),
                            ("State the contra account for the amount of R21 800 on the credit side.", "Sundry purchases / Total purchases."),
                            ("Name the source document supporting 'Sundry allowances, CAJ, R2 300'.", "Duplicate debit note or original credit note."),
                            ("Give one valid reason for the recording 'Journal credits, GJ, R610'.", reason_610),
                        ]
                    else:
                        family_label = "analysis_typed_medium_creditors_balance"
                        question_answer_pairs = [
                            ("What is the amount owed to creditors on 1 March 2011?", "R28 260."),
                            ("State the contra account for the amount of R35 400 on the debit side.", "Bank and discount received."),
                            ("What is the amount owed to creditors on 31 March 2011?", "R12 270."),
                            ("Name the source document supporting 'Bank, CRJ, R140'.", "Duplicate receipt."),
                        ]
                else:
                    business_name = str(business or pick_business_name(r=r)).strip()
                    title = "March 2011 Creditors control account exam-style analysis"
                    info_lines = [
                        "Dr Creditors Control (B8) Cr",
                        "2011 Mar 31 Bank and discount received CPJ R35 400 | 2011 Mar 1 Balance b/d R28 260",
                        "2011 Mar 31 Sundry allowances CAJ R2 300 | 2011 Mar 31 Sundry purchases CJ R21 800",
                        "2011 Mar 31 Journal debits GJ R840 | 2011 Mar 31 Journal credits GJ R610",
                        "2011 Mar 31 Balance c/d R12 270 | 2011 Mar 31 Bank CRJ R140",
                        "2011 Apr 1 Balance b/d R12 270",
                    ]
                    additional_lines = [
                        "Creditors list on 1 March 2011: Debit R340; Credit R28 600.",
                        "Creditors list on 31 March 2011: Debit R520; Credit R12 790.",
                    ]
                    reason_610 = r.choice([
                        "Correction of an error in a creditor's account.",
                        "Interest charged on an overdue creditor account.",
                        "Transfer of an account between creditors and debtors ledgers.",
                    ])
                    family_label = "analysis_typed_hard_creditors_q2"
                    question_answer_pairs = [
                        ("What is the amount owed to creditors on 1 March 2011?", "R28 260."),
                        ("State the contra account for the amount of R21 800 on the credit side.", "Sundry purchases / Total purchases."),
                        ("State the contra account for the amount of R35 400 on the debit side.", "Bank and discount received."),
                        ("Give one valid reason for the recording 'Journal credits, GJ, R610'.", reason_610),
                        ("Name the source document supporting 'Sundry allowances, CAJ, R2 300'.", "Duplicate debit note or original credit note."),
                        ("Name the source document supporting 'Bank, CRJ, R140'.", "Duplicate receipt."),
                        ("What is the amount owed to creditors on 31 March 2011?", "R12 270."),
                        ("Explain how the owner should verify the closing balance on 31 March 2011.", "Compare the closing Creditors Control balance with the net creditors list total for 31 March 2011; the two must agree."),
                    ]

            prompt_lines = [
                business_name,
                title,
                "",
                "Information:",
                "Study the control account table below and answer the questions that follow.",
            ]
            if diff == "hard":
                prompt_lines.append("Use the Balance c/d row and the related list information when you verify the closing balance.")
            prompt_lines.extend(["", "Additional information:"])
            prompt_lines.extend(additional_lines)
            prompt_lines.extend(["", "Required:"])
            prompt_lines.extend([f"{idx + 1}. {question}" for idx, (question, _) in enumerate(question_answer_pairs)])
            prompt = "\n".join(prompt_lines)
            sample_answer = "\n".join(f"{idx + 1}. {answer}" for idx, (_, answer) in enumerate(question_answer_pairs))

            prompt_norm = prompt.lower()
            if "key facts" in prompt_norm or "write short answers" in prompt_norm or "learner should identify" in prompt_norm:
                raise _ControlAccountsScenarioValidationError("Control accounts analysis prompt regressed to generic summary wording.")
            if diff == "hard" and ("balance c/d" not in prompt_norm or "list" not in prompt_norm):
                raise _ControlAccountsScenarioValidationError("Hard control accounts analysis must stay tied to closing-balance verification.")

            out = _make_typed(prompt=prompt, sample_answer=sample_answer)
            out["guidelines"] = guidelines
            out["control_accounts_family"] = family_label
            out["control_accounts_variant"] = var
            out["difficulty"] = diff
            out["prompt_journal"] = _build_control_accounts_analysis_prompt_journal(
                business=business_name,
                info_lines=info_lines,
            )
            out["answer_part_hints"] = _build_answer_part_hints([
                (f"{idx + 1}. {question}", answer, guidelines)
                for idx, (question, answer) in enumerate(question_answer_pairs)
            ])
            return out
        except _ControlAccountsScenarioValidationError as exc:
            last_error = exc
            continue

    if last_error is not None:
        raise last_error
    raise _ControlAccountsScenarioValidationError("Could not generate a valid control accounts analysis question.")

