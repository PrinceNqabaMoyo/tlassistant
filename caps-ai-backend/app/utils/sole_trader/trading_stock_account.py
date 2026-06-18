from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .column_help import headers_to_column_help
from .core import fmt_money, round_money
from .journal_question import make_journal
from .journal_table import build_prefixed_row
from .names import pick_business_name


MAX_TRADING_STOCK_GENERATION_ATTEMPTS = 25
MONTH_SEQUENCE = [
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


class _TradingStockScenarioValidationError(ValueError):
    pass


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


def _make_trading_stock_account_headers() -> List[str]:
    return _general_ledger_account_headers()


def _round_to_step(amount: float, step: int = 50) -> float:
    return round_money(round(float(amount) / float(step)) * float(step))


def _pick_trading_stock_business(*, r: random.Random) -> str:
    return pick_business_name(r=r)


def _pick_trading_stock_period(*, r: random.Random) -> Tuple[str, int]:
    month = r.choice(MONTH_SEQUENCE)
    year = int(r.choice([2023, 2024, 2025, 2026]))
    return month, year


def _next_month(*, month: str, year: int) -> Tuple[str, int]:
    try:
        month_index = MONTH_SEQUENCE.index(str(month))
    except ValueError:
        return "January", int(year) + 1
    if month_index == len(MONTH_SEQUENCE) - 1:
        return MONTH_SEQUENCE[0], int(year) + 1
    return MONTH_SEQUENCE[month_index + 1], int(year)


def _offset_amount(*, amount: float, step: int, delta_steps: int, direction: int = 1) -> float:
    adjusted = float(amount) + (float(step) * float(delta_steps) * float(direction))
    minimum = float(step)
    while adjusted <= 0.0:
        adjusted += float(step)
    return round_money(max(minimum, adjusted))


def _trading_stock_guidelines(*, include_balance_guidance: bool = True, include_source_column_guidance: bool = True) -> List[str]:
    guidelines = [
        "The Trading Stock account records stock moving into or out of the business at cost price.",
        "If stock on hand increases, post the amount on the debit side (left). If stock on hand decreases, post the amount on the credit side (right).",
    ]
    if include_source_column_guidance:
        guidelines.append("Use the Trading Stock column total from CPJ, CJ, CAJ and PCJ. Use the Cost of Sales column total from CRJ, DJ and DAJ.")
    if include_balance_guidance:
        guidelines.append("Balance c/d is the closing stock on the last day of the month. Carry the same amount forward as Balance b/d on day 1 of the next month.")
    return guidelines


def _append_special_entry_info_lines(
    info_lines: List[str],
    *,
    petty_cash_pcj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
) -> None:
    if petty_cash_pcj:
        info_lines.append(f"Petty-cash purchases of stock (PCJ Trading Stock column): {fmt_money(petty_cash_pcj)}")
    if drawings_gj:
        info_lines.append(f"Drawings of stock by the owner (GJ): {fmt_money(drawings_gj)}")
    if stock_deficit_gj:
        info_lines.append(f"Stock deficit after stock count - stock missing or stolen (GJ): {fmt_money(stock_deficit_gj)}")
    if donations_gj:
        info_lines.append(f"Stock donated out of the business (GJ): {fmt_money(donations_gj)}")
    if stationery_gj:
        info_lines.append(f"Stationery correction - stock used for stationery and corrected out of Trading Stock (GJ): {fmt_money(stationery_gj)}")


def _build_casted_journal_prompt(
    *,
    bank_cpj: float,
    creditors_cj: float,
    creditors_returns_caj: float,
    debtors_returns_cost: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    opening: float,
) -> str:
    cpj_bank_total = _offset_amount(amount=bank_cpj, step=100.0, delta_steps=6)
    cpj_stationery = _offset_amount(amount=bank_cpj, step=50.0, delta_steps=4, direction=-1)
    cpj_creditors_payments = _offset_amount(amount=bank_cpj, step=100.0, delta_steps=8, direction=1)
    cpj_discount_received = _offset_amount(amount=bank_cpj, step=50.0, delta_steps=3, direction=-1)

    cj_creditors_control = _offset_amount(amount=creditors_cj, step=100.0, delta_steps=7, direction=1)
    cj_stationery = _offset_amount(amount=creditors_cj, step=100.0, delta_steps=5, direction=-1)
    cj_equipment = _offset_amount(amount=creditors_cj, step=100.0, delta_steps=9, direction=1)

    caj_creditors_control = _offset_amount(amount=creditors_returns_caj, step=50.0, delta_steps=5, direction=1)
    caj_stationery = _offset_amount(amount=creditors_returns_caj, step=50.0, delta_steps=2, direction=-1)
    caj_sundry_returns = _offset_amount(amount=creditors_returns_caj, step=50.0, delta_steps=4, direction=1)

    daj_debtors_allowances = _offset_amount(amount=debtors_returns_cost, step=100.0, delta_steps=5, direction=1)

    crj_bank = _offset_amount(amount=cost_of_sales_crj, step=100.0, delta_steps=12, direction=1)
    crj_sales = round_money(cost_of_sales_crj * 1.4)

    dj_sales = round_money(cost_of_sales_dj * 1.35)

    return (
        "Information: Journal totals (casting)\n\n"
        "Cash Payments Journal (CPJ)\n"
        f"- Bank: {fmt_money(cpj_bank_total)}\n"
        f"- Trading stock: {fmt_money(bank_cpj)}\n"
        f"- Stationery: {fmt_money(cpj_stationery)}\n"
        f"- Creditors control (payments): {fmt_money(cpj_creditors_payments)}\n"
        f"- Discount received: {fmt_money(cpj_discount_received)}\n\n"
        "Creditors Journal (CJ)\n"
        f"- Creditors control: {fmt_money(cj_creditors_control)}\n"
        f"- Trading stock: {fmt_money(creditors_cj)}\n"
        f"- Stationery: {fmt_money(cj_stationery)}\n"
        f"- Equipment: {fmt_money(cj_equipment)}\n\n"
        "Creditors Allowances Journal (CAJ)\n"
        f"- Creditors control: {fmt_money(caj_creditors_control)}\n"
        f"- Trading stock: {fmt_money(creditors_returns_caj)}\n"
        f"- Stationery: {fmt_money(caj_stationery)}\n"
        f"- Sundry returns: {fmt_money(caj_sundry_returns)}\n\n"
        "Debtors Allowances Journal (DAJ)\n"
        f"- Debtors allowances: {fmt_money(daj_debtors_allowances)}\n"
        f"- Cost of sales (returns at cost): {fmt_money(debtors_returns_cost)}\n\n"
        "Cash Receipts Journal (CRJ)\n"
        f"- Bank: {fmt_money(crj_bank)}\n"
        f"- Sales: {fmt_money(crj_sales)}\n"
        f"- Cost of sales (cash sales): {fmt_money(cost_of_sales_crj)}\n\n"
        "Debtors Journal (DJ)\n"
        f"- Sales: {fmt_money(dj_sales)}\n"
        f"- Cost of sales (credit sales): {fmt_money(cost_of_sales_dj)}\n\n"
        f"Additional information: Opening trading stock balance: {fmt_money(opening)}"
    )


def _build_trading_stock_values(*, r: random.Random, difficulty: str) -> Dict[str, float]:
    diff = str(difficulty or "easy").strip().lower()
    if diff == "hard":
        opening = round_money(r.randrange(26000, 52001, 100))
        bank_cpj = round_money(r.randrange(7000, 16001, 50))
        creditors_cj = round_money(r.randrange(9000, 22001, 50))
        cost_of_sales_crj = round_money(r.randrange(3500, 9001, 50))
        cost_of_sales_dj = round_money(r.randrange(3500, 9501, 50))
    elif diff == "medium":
        opening = round_money(r.randrange(18000, 36001, 100))
        bank_cpj = round_money(r.randrange(4500, 11001, 50))
        creditors_cj = round_money(r.randrange(6500, 14001, 50))
        cost_of_sales_crj = round_money(r.randrange(2500, 6501, 50))
        cost_of_sales_dj = round_money(r.randrange(2500, 7001, 50))
    else:
        opening = round_money(r.randrange(12000, 24001, 100))
        bank_cpj = round_money(r.randrange(2500, 7001, 50))
        creditors_cj = round_money(r.randrange(3500, 9001, 50))
        cost_of_sales_crj = round_money(r.randrange(1500, 4501, 50))
        cost_of_sales_dj = round_money(r.randrange(1500, 4501, 50))

    total_cost_of_sales = round_money(cost_of_sales_crj + cost_of_sales_dj)
    debtors_returns_daj = max(
        100.0,
        _round_to_step(total_cost_of_sales * float(r.choice([0.05, 0.075, 0.10] if diff == "easy" else ([0.05, 0.075, 0.10, 0.125] if diff == "medium" else [0.075, 0.10, 0.125, 0.15])))),
    )
    creditors_returns_caj = max(
        100.0,
        _round_to_step(creditors_cj * float(r.choice([0.05, 0.075, 0.10] if diff == "easy" else ([0.05, 0.10, 0.125] if diff == "medium" else [0.075, 0.10, 0.125, 0.15])))),
    )

    if diff == "hard":
        petty_cash_pcj = round_money(r.randrange(500, 1601, 50))
        drawings_gj = round_money(r.randrange(500, 2201, 50))
        stock_deficit_gj = round_money(r.randrange(400, 1401, 50))
        donations_gj = round_money(r.randrange(300, 1201, 50))
        stationery_gj = round_money(r.randrange(300, 1001, 50))
    elif diff == "medium":
        petty_cash_pcj = round_money(r.randrange(300, 901, 50))
        drawings_gj = round_money(r.randrange(300, 1501, 50))
        stock_deficit_gj = round_money(r.randrange(250, 901, 50))
        donations_gj = round_money(r.randrange(200, 801, 50))
        stationery_gj = round_money(r.randrange(200, 701, 50))
    else:
        petty_cash_pcj = round_money(r.randrange(150, 451, 50))
        drawings_gj = round_money(r.randrange(200, 701, 50))
        stock_deficit_gj = round_money(r.randrange(150, 501, 50))
        donations_gj = round_money(r.randrange(100, 401, 50))
        stationery_gj = round_money(r.randrange(100, 351, 50))

    minimum_closing = 2500.0 if diff == "easy" else (4000.0 if diff == "medium" else 6000.0)
    closing = round_money(
        opening
        + bank_cpj
        + creditors_cj
        + petty_cash_pcj
        + debtors_returns_daj
        - creditors_returns_caj
        - cost_of_sales_crj
        - cost_of_sales_dj
        - drawings_gj
        - stock_deficit_gj
        - donations_gj
        - stationery_gj
    )
    while closing < minimum_closing:
        opening = round_money(opening + 500.0)
        closing = round_money(closing + 500.0)

    return {
        "opening": opening,
        "bank_cpj": bank_cpj,
        "creditors_cj": creditors_cj,
        "petty_cash_pcj": petty_cash_pcj,
        "debtors_returns_daj": debtors_returns_daj,
        "creditors_returns_caj": creditors_returns_caj,
        "cost_of_sales_crj": cost_of_sales_crj,
        "cost_of_sales_dj": cost_of_sales_dj,
        "drawings_gj": drawings_gj,
        "stock_deficit_gj": stock_deficit_gj,
        "donations_gj": donations_gj,
        "stationery_gj": stationery_gj,
    }


def _trading_stock_totals(values: Dict[str, float]) -> Tuple[float, float, float]:
    numeric_values = {key: float(values.get(key, 0.0)) for key in values}
    debit_total = round_money(
        numeric_values.get("opening", 0.0)
        + numeric_values.get("bank_cpj", 0.0)
        + numeric_values.get("creditors_cj", 0.0)
        + numeric_values.get("petty_cash_pcj", 0.0)
        + numeric_values.get("debtors_returns_daj", 0.0)
    )
    credit_total = round_money(
        numeric_values.get("creditors_returns_caj", 0.0)
        + numeric_values.get("cost_of_sales_crj", 0.0)
        + numeric_values.get("cost_of_sales_dj", 0.0)
        + numeric_values.get("drawings_gj", 0.0)
        + numeric_values.get("stock_deficit_gj", 0.0)
        + numeric_values.get("donations_gj", 0.0)
        + numeric_values.get("stationery_gj", 0.0)
    )
    closing = round_money(debit_total - credit_total)
    return debit_total, credit_total, closing


def _validate_trading_stock_values(values: Dict[str, float]) -> None:
    numeric_values = {key: float(values.get(key, 0.0)) for key in values}
    if any(amount < 0.0 for amount in numeric_values.values()):
        raise _TradingStockScenarioValidationError("Trading stock scenario contains a negative amount.")

    debit_total, credit_total, closing = _trading_stock_totals(numeric_values)
    if numeric_values.get("opening", 0.0) <= 0.0:
        raise _TradingStockScenarioValidationError("Trading stock opening balance must be positive.")
    if numeric_values.get("bank_cpj", 0.0) <= 0.0 or numeric_values.get("creditors_cj", 0.0) <= 0.0:
        raise _TradingStockScenarioValidationError("Trading stock purchase sources must include positive CPJ and CJ amounts.")
    if numeric_values.get("cost_of_sales_crj", 0.0) <= 0.0 or numeric_values.get("cost_of_sales_dj", 0.0) <= 0.0:
        raise _TradingStockScenarioValidationError("Trading stock scenario must include positive CRJ and DJ cost-of-sales amounts.")
    if debit_total <= 0.0 or credit_total <= 0.0:
        raise _TradingStockScenarioValidationError("Trading stock scenario totals must both be positive.")
    if numeric_values.get("creditors_returns_caj", 0.0) >= numeric_values.get("creditors_cj", 0.0):
        raise _TradingStockScenarioValidationError("Returns to creditors must stay below credit purchases.")
    total_cost_of_sales = round_money(numeric_values.get("cost_of_sales_crj", 0.0) + numeric_values.get("cost_of_sales_dj", 0.0))
    if numeric_values.get("debtors_returns_daj", 0.0) >= total_cost_of_sales:
        raise _TradingStockScenarioValidationError("Returns from debtors must stay below total cost of sales.")
    if closing <= 0.0:
        raise _TradingStockScenarioValidationError("Trading stock closing balance must remain positive.")


def _validate_trading_stock_account_output(
    *,
    journal: Dict[str, Any],
    correct_map: Dict[str, Any],
    table_index: int,
    month: str,
    values: Dict[str, float],
) -> None:
    row_lookup = dict(journal.get("row_lookup") or {})
    for required_tag in [
        "opening_balance",
        "bank_cpj",
        "creditors_cj",
        "debtors_returns_daj",
        "creditors_returns_caj",
        "cost_of_sales_crj",
        "cost_of_sales_dj",
        "totals",
    ]:
        if required_tag not in row_lookup:
            raise _TradingStockScenarioValidationError(f"Trading stock account is missing required row '{required_tag}'.")

    optional_value_tags = [
        "petty_cash_pcj",
        "drawings_gj",
        "stock_deficit_gj",
        "donations_gj",
        "stationery_gj",
    ]
    for optional_tag in optional_value_tags:
        has_row = optional_tag in row_lookup
        has_value = float(values.get(optional_tag, 0.0)) > 0.0
        if has_row != has_value:
            raise _TradingStockScenarioValidationError(f"Trading stock optional row '{optional_tag}' does not match its scenario value.")

    debit_total, credit_total, closing = _trading_stock_totals(values)
    balanced_total = fmt_money(max(debit_total, credit_total))
    balance_cd_tag = "balance_cd_credit" if closing > 0.0 else "balance_cd_debit"
    balance_bd_tag = "balance_bd_debit" if closing > 0.0 else "balance_bd_credit"
    if balance_cd_tag not in row_lookup or balance_bd_tag not in row_lookup:
        raise _TradingStockScenarioValidationError("Trading stock balance carry-down/carry-forward rows are inconsistent with the closing balance.")

    def _expect(row_tag: str, column_index: int, expected: str) -> None:
        key = _cell_key(table_index, row_lookup, row_tag, column_index)
        row_index = row_lookup[row_tag]
        row = journal.get("rows", [])[row_index]
        rendered_value = str(((row[column_index] or {}).get("value")) or "")
        actual = str(correct_map.get(key) or rendered_value)
        if actual != expected:
            raise _TradingStockScenarioValidationError(
                f"Trading stock rendered value mismatch for {row_tag} col {column_index}: expected '{expected}', got '{actual}'."
            )

    _expect("opening_balance", 0, month)
    _expect("opening_balance", 1, "1")
    _expect("opening_balance", 2, "Balance b/d")
    _expect("opening_balance", 3, "b/d")
    _expect("opening_balance", 4, fmt_money(float(values.get("opening", 0.0))))
    _expect("bank_cpj", 2, "Bank")
    _expect("bank_cpj", 3, "CPJ")
    _expect("creditors_cj", 2, "Creditors control")
    _expect("creditors_cj", 3, "CJ")
    _expect("debtors_returns_daj", 2, "Cost of sales")
    _expect("debtors_returns_daj", 3, "DAJ")
    _expect("creditors_returns_caj", 7, "Creditors control")
    _expect("creditors_returns_caj", 8, "CAJ")
    _expect("cost_of_sales_crj", 7, "Cost of sales")
    _expect("cost_of_sales_crj", 8, "CRJ")
    _expect("cost_of_sales_dj", 7, "Cost of sales")
    _expect("cost_of_sales_dj", 8, "DJ")
    _expect("totals", 2, "Totals")
    _expect("totals", 4, balanced_total)
    _expect("totals", 7, "Totals")
    _expect("totals", 9, balanced_total)
    _expect(balance_cd_tag, 8 if closing > 0.0 else 3, "c/d")
    _expect(balance_bd_tag, 3 if closing > 0.0 else 8, "b/d")
    _expect(balance_cd_tag, 9 if closing > 0.0 else 4, fmt_money(abs(closing)))
    _expect(balance_bd_tag, 4 if closing > 0.0 else 9, fmt_money(abs(closing)))


def _validate_returns_percentage_variant(*, values: Dict[str, float]) -> None:
    creditors_cj = float(values.get("creditors_cj", 0.0))
    creditors_returns_caj = float(values.get("creditors_returns_caj", 0.0))
    debtors_returns_daj = float(values.get("debtors_returns_daj", 0.0))
    total_cost_of_sales = round_money(float(values.get("cost_of_sales_crj", 0.0)) + float(values.get("cost_of_sales_dj", 0.0)))
    if creditors_cj <= 0.0 or total_cost_of_sales <= 0.0:
        raise _TradingStockScenarioValidationError("Returns-percentage question requires positive denominators.")
    returns_to_creditors_pct = (creditors_returns_caj / creditors_cj) * 100.0
    returns_from_debtors_pct = (debtors_returns_daj / total_cost_of_sales) * 100.0
    if not (0.0 < returns_to_creditors_pct < 100.0):
        raise _TradingStockScenarioValidationError("Returns to creditors percentage must be between 0 and 100.")
    if not (0.0 < returns_from_debtors_pct < 100.0):
        raise _TradingStockScenarioValidationError("Returns from debtors percentage must be between 0 and 100.")


def _validate_trade_discount_variant(*, cash_paid: float, disc_rate: float, cash_purchases_before_discount: float, values: Dict[str, float]) -> None:
    if cash_paid <= 0.0:
        raise _TradingStockScenarioValidationError("Trade-discount question requires a positive cash-paid amount.")
    if disc_rate <= 0.0 or disc_rate >= 100.0:
        raise _TradingStockScenarioValidationError("Trade-discount rate must fall between 0 and 100.")
    if cash_purchases_before_discount <= cash_paid:
        raise _TradingStockScenarioValidationError("Cash purchases before discount must exceed the discounted cash paid.")
    discount_amount = round_money(cash_purchases_before_discount - cash_paid)
    if discount_amount <= 0.0:
        raise _TradingStockScenarioValidationError("Trade-discount amount must be positive.")
    variant_values = dict(values)
    variant_values["bank_cpj"] = cash_purchases_before_discount
    _validate_trading_stock_values(variant_values)


def _make_trading_stock_with_retry(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    builder: Callable[..., Dict[str, Any]],
) -> Dict[str, Any]:
    last_error: Optional[_TradingStockScenarioValidationError] = None
    for _ in range(MAX_TRADING_STOCK_GENERATION_ATTEMPTS):
        try:
            return builder(r=r, difficulty=difficulty, mode=mode)
        except _TradingStockScenarioValidationError as exc:
            last_error = exc
            continue
    if last_error is not None:
        raise last_error
    raise _TradingStockScenarioValidationError("Could not generate a valid trading stock question.")


def _cell_key(table_index: int, row_lookup: Dict[str, int], row_tag: str, column_index: int) -> str:
    return f"t{table_index}_r{row_lookup[row_tag]}_c{column_index}"


def _set_trading_stock_hint(
    *,
    cell_hints: Dict[str, str],
    derivation_map: Dict[str, str],
    cell_key: str,
    hint_text: str,
    derivation_text: str = "",
) -> None:
    cell_hints[cell_key] = hint_text
    if derivation_text:
        derivation_map[cell_key] = derivation_text


def _append_trading_stock_teaching_hint(
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

    def _merge(field_name: str, extra_text: str) -> None:
        if not extra_text:
            return
        current = str(existing.get(field_name) or "").strip()
        existing[field_name] = f"{current} {extra_text}".strip() if current else extra_text

    _merge("role_in_requirement", role_in_requirement)
    _merge("evidence_from_question", evidence_from_question)
    _merge("rule_or_principle", rule_or_principle)
    _merge("how_to_derive", how_to_derive)
    _merge("transfer_tip", transfer_tip)
    if existing:
        cell_teaching_map[cell_key] = existing


def _populate_trading_stock_teaching_map(
    *,
    table_index: int,
    row_lookup: Dict[str, int],
    cell_teaching_map: Dict[str, Dict[str, str]],
    opening: float,
    bank_cpj: float,
    creditors_cj: float,
    petty_cash_pcj: float,
    debtors_returns_daj: float,
    creditors_returns_caj: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
    debit_total: float,
    credit_total: float,
    closing: float,
) -> None:
    def _entry_teaching(
        *,
        tag: str,
        side: str,
        day_rule: str,
        evidence_text: str,
        details_text: str,
        folio_text: str,
        amount_rule: str,
        derivation_text: str,
        transfer_tip: str,
    ) -> None:
        if tag not in row_lookup:
            return
        is_debit = side == "debit"
        day_key = _cell_key(table_index, row_lookup, tag, 1 if is_debit else 6)
        details_key = _cell_key(table_index, row_lookup, tag, 2 if is_debit else 7)
        folio_key = _cell_key(table_index, row_lookup, tag, 3 if is_debit else 8)
        amount_key = _cell_key(table_index, row_lookup, tag, 4 if is_debit else 9)
        opposite_amount_key = _cell_key(table_index, row_lookup, tag, 9 if is_debit else 4)

        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=day_key,
            role_in_requirement="Complete the Day cell for this posting.",
            evidence_from_question=evidence_text,
            rule_or_principle=day_rule,
            how_to_derive=day_rule,
            transfer_tip="Opening balances are usually on day 1; month-end journal totals and adjustments are usually on day 31.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=details_key,
            role_in_requirement="Complete the Details cell for this ledger entry.",
            evidence_from_question=evidence_text,
            rule_or_principle=f"Use '{details_text}' as the Details entry for this posting.",
            how_to_derive=f"This row should show '{details_text}' in Details.",
            transfer_tip="A common mistake is copying the journal name into Details instead of the account name or balance reference.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=folio_key,
            role_in_requirement="Complete the Fol column for this posting.",
            evidence_from_question=evidence_text,
            rule_or_principle=f"Use '{folio_text}' because this entry comes from that journal or balance reference.",
            how_to_derive=f"The correct folio for this row is '{folio_text}'.",
            transfer_tip="Do not confuse the source journal in Fol with the Details entry.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=amount_key,
            role_in_requirement=f"Enter the amount on the {side} side of the Trading Stock account.",
            evidence_from_question=evidence_text,
            rule_or_principle=amount_rule,
            how_to_derive=derivation_text,
            transfer_tip=transfer_tip,
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=opposite_amount_key,
            role_in_requirement="Decide whether the opposite amount cell should stay blank.",
            evidence_from_question=evidence_text,
            rule_or_principle=f"Only the {side} side receives the amount on this row.",
            how_to_derive=f"Post the amount only on the {side} side and leave the opposite side blank.",
            transfer_tip="If you write the amount on both sides, the account will not balance correctly.",
        )

    _entry_teaching(
        tag="opening_balance",
        side="debit",
        day_rule="Opening balances are brought down on day 1.",
        evidence_text="Use the opening balance information in the question.",
        details_text="Balance b/d",
        folio_text="b/d",
        amount_rule="Opening trading stock is an asset balance brought down on the debit side.",
        derivation_text=f"Opening balance brought down = {fmt_money(opening)}.",
        transfer_tip="Opening balances are carried from the previous period and are not treated like current-month purchases.",
    )
    _entry_teaching(
        tag="bank_cpj",
        side="debit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Trading Stock column total from the Cash Payments Journal, not the Bank or Creditors Control columns.",
        details_text="Bank",
        folio_text="CPJ",
        amount_rule="Purchases increase Trading Stock, so the amount is debited.",
        derivation_text=f"Cash purchases from CPJ = {fmt_money(bank_cpj)}.",
        transfer_tip="Do not post purchases on the credit side; buying stock increases the asset.",
    )
    _entry_teaching(
        tag="creditors_cj",
        side="debit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Trading Stock column total from the Creditors Journal, not the Creditors Control total or another expense column.",
        details_text="Creditors control",
        folio_text="CJ",
        amount_rule="Credit purchases still increase Trading Stock, so the amount is debited.",
        derivation_text=f"Credit purchases from CJ = {fmt_money(creditors_cj)}.",
        transfer_tip="The payment method changes the source journal, not the debit side of Trading Stock.",
    )
    _entry_teaching(
        tag="petty_cash_pcj",
        side="debit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Trading Stock column total from the Petty Cash Journal, not another petty-cash expense column.",
        details_text="Petty cash",
        folio_text="PCJ",
        amount_rule="Petty-cash purchases increase Trading Stock, so the amount is debited.",
        derivation_text=f"Petty-cash purchases from PCJ = {fmt_money(petty_cash_pcj)}.",
        transfer_tip="A small source document still follows the same debit rule as any other stock purchase.",
    )
    _entry_teaching(
        tag="debtors_returns_daj",
        side="debit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Cost of Sales column amount from the Debtors Allowances Journal, not the Debtors Allowances column at selling price.",
        details_text="Cost of sales",
        folio_text="DAJ",
        amount_rule="Goods returned by debtors come back into stock at cost price, so the amount is debited.",
        derivation_text=f"Returns from debtors at cost from DAJ = {fmt_money(debtors_returns_daj)}.",
        transfer_tip="Use the cost-price figure, not the selling price of the returned goods.",
    )
    _entry_teaching(
        tag="creditors_returns_caj",
        side="credit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Trading Stock column total from the Creditors Allowances Journal, not another returns or stationery column.",
        details_text="Creditors control",
        folio_text="CAJ",
        amount_rule="Stock returned to suppliers leaves the business, so the amount is credited.",
        derivation_text=f"Returns to creditors from CAJ = {fmt_money(creditors_returns_caj)}.",
        transfer_tip="A return to a supplier reduces the stock asset, so it does not stay on the debit side.",
    )
    _entry_teaching(
        tag="cost_of_sales_crj",
        side="credit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Cost of Sales column amount from the Cash Receipts Journal, not the Bank or Sales totals.",
        details_text="Cost of sales",
        folio_text="CRJ",
        amount_rule="When stock is sold, Trading Stock decreases at cost price and is credited.",
        derivation_text=f"Cost of sales on cash sales from CRJ = {fmt_money(cost_of_sales_crj)}.",
        transfer_tip="Do not use the sales value here; the Trading Stock account is prepared at cost price.",
    )
    _entry_teaching(
        tag="cost_of_sales_dj",
        side="credit",
        day_rule="Month-end journal totals are posted on day 31.",
        evidence_text="Use the Cost of Sales column amount from the Debtors Journal, not the Sales total.",
        details_text="Cost of sales",
        folio_text="DJ",
        amount_rule="Credit sales still reduce Trading Stock at cost price, so the amount is credited.",
        derivation_text=f"Cost of sales on credit sales from DJ = {fmt_money(cost_of_sales_dj)}.",
        transfer_tip="The customer bought on credit, but the stock still leaves the business at cost.",
    )
    _entry_teaching(
        tag="drawings_gj",
        side="credit",
        day_rule="General Journal adjustments are posted on day 31.",
        evidence_text="Use the owner-withdrawal information from the General Journal.",
        details_text="Drawings",
        folio_text="GJ",
        amount_rule="Goods taken by the owner reduce Trading Stock, so the amount is credited.",
        derivation_text=f"Drawings from GJ = {fmt_money(drawings_gj)}.",
        transfer_tip="Owner withdrawals are not purchases or sales; they reduce stock on hand.",
    )
    _entry_teaching(
        tag="stock_deficit_gj",
        side="credit",
        day_rule="General Journal adjustments are posted on day 31.",
        evidence_text="Use the stock-deficit adjustment from the General Journal after a stock count shows goods are missing, stolen, or damaged.",
        details_text="Stock deficit",
        folio_text="GJ",
        amount_rule="A shortage reduces Trading Stock, so the amount is credited.",
        derivation_text=f"Stock deficit from GJ = {fmt_money(stock_deficit_gj)}.",
        transfer_tip="A deficit is a decrease in the asset, not an additional purchase.",
    )
    _entry_teaching(
        tag="donations_gj",
        side="credit",
        day_rule="General Journal adjustments are posted on day 31.",
        evidence_text="Use the donation adjustment from the General Journal when goods are given away without being sold.",
        details_text="Donations",
        folio_text="GJ",
        amount_rule="Donated goods leave the business, so the amount is credited.",
        derivation_text=f"Donations from GJ = {fmt_money(donations_gj)}.",
        transfer_tip="Donated stock reduces the stock asset even though no sale took place.",
    )
    _entry_teaching(
        tag="stationery_gj",
        side="credit",
        day_rule="General Journal adjustments are posted on day 31.",
        evidence_text="Use the General Journal correction when stock was wrongly treated as Trading Stock but was actually used as stationery.",
        details_text="Stationery",
        folio_text="GJ",
        amount_rule="This correction moves value out of Trading Stock, so the amount is credited.",
        derivation_text=f"Stationery correction from GJ = {fmt_money(stationery_gj)}.",
        transfer_tip="If stock was used for another purpose, remove it from Trading Stock on the credit side.",
    )

    if "balance_cd_credit" in row_lookup:
        _entry_teaching(
            tag="balance_cd_credit",
            side="credit",
            day_rule="Balance c/d is entered on the last day of the month.",
            evidence_text="Use the totals on both sides of the account to find the balancing figure.",
            details_text="Balance c/d",
            folio_text="c/d",
            amount_rule="When debit entries exceed credit entries, the balancing figure is placed on the credit side.",
            derivation_text=f"Balance c/d = Total debit − Total credit = {fmt_money(debit_total)} − {fmt_money(credit_total)} = {fmt_money(closing)}.",
            transfer_tip="Do not add Balance c/d before comparing the two sides of the account. The same amount is then carried to the next month as Balance b/d.",
        )
    if "balance_cd_debit" in row_lookup:
        _entry_teaching(
            tag="balance_cd_debit",
            side="debit",
            day_rule="Balance c/d is entered on the last day of the month.",
            evidence_text="Use the totals on both sides of the account to find the balancing figure.",
            details_text="Balance c/d",
            folio_text="c/d",
            amount_rule="When credit entries exceed debit entries, the balancing figure is placed on the debit side.",
            derivation_text=f"Balance c/d = Total credit − Total debit = {fmt_money(credit_total)} − {fmt_money(debit_total)} = {fmt_money(abs(closing))}.",
            transfer_tip="The balancing figure always goes on the side with the smaller total before balancing. The same amount is then carried to the next month as Balance b/d.",
        )
    if "totals" in row_lookup:
        debit_total_key = _cell_key(table_index, row_lookup, "totals", 4)
        credit_total_key = _cell_key(table_index, row_lookup, "totals", 9)
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=debit_total_key,
            role_in_requirement="Calculate the debit total for the Trading Stock account.",
            evidence_from_question="Add all debit-side entries, including Balance c/d if it appears on the debit side.",
            rule_or_principle="After the balancing figure is inserted, total debit must equal total credit.",
            how_to_derive=f"Debit total = {fmt_money(debit_total)}.",
            transfer_tip="If the totals disagree, first re-check whether each amount is on the correct side.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=credit_total_key,
            role_in_requirement="Calculate the credit total for the Trading Stock account.",
            evidence_from_question="Add all credit-side entries, including Balance c/d if it appears on the credit side.",
            rule_or_principle="After the balancing figure is inserted, total credit must equal total debit.",
            how_to_derive=f"Credit total = {fmt_money(credit_total)}.",
            transfer_tip="Totals are a check on the whole account, so use them to catch side-placement mistakes.",
        )
    if "balance_bd_debit" in row_lookup:
        _entry_teaching(
            tag="balance_bd_debit",
            side="debit",
            day_rule="The new month's balance b/d is entered on day 1.",
            evidence_text="Carry forward the previous Balance c/d to the next month.",
            details_text="Balance b/d",
            folio_text="b/d",
            amount_rule="Balance b/d equals the previous closing balance and stays on the same side.",
            derivation_text=f"Balance b/d = previous Balance c/d = {fmt_money(abs(closing))}.",
            transfer_tip="Do not recalculate this amount; it is carried forward from the balanced account after Balance c/d has been found.",
        )
    if "balance_bd_credit" in row_lookup:
        _entry_teaching(
            tag="balance_bd_credit",
            side="credit",
            day_rule="The new month's balance b/d is entered on day 1.",
            evidence_text="Carry forward the previous Balance c/d to the next month.",
            details_text="Balance b/d",
            folio_text="b/d",
            amount_rule="Balance b/d equals the previous closing balance and stays on the same side.",
            derivation_text=f"Balance b/d = previous Balance c/d = {fmt_money(abs(closing))}.",
            transfer_tip="Do not switch sides when carrying the balance forward to the next month. Copy the exact closing balance forward as Balance b/d.",
        )


def _populate_trading_stock_scaffold_metadata(
    *,
    table_index: int,
    row_lookup: Dict[str, int],
    cell_hints: Dict[str, str],
    derivation_map: Dict[str, str],
    opening: float,
    bank_cpj: float,
    creditors_cj: float,
    petty_cash_pcj: float,
    debtors_returns_daj: float,
    creditors_returns_caj: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
    debit_total: float,
    credit_total: float,
    closing: float,
) -> None:
    def _entry_hint(*, tag: str, side: str, day_text: str, details_text: str, folio_text: str, amount: float, row_text: str, amount_text: str, derivation_text: str) -> None:
        if tag not in row_lookup:
            return
        is_debit = side == "debit"
        row_key = _cell_key(table_index, row_lookup, tag, 0)
        day_key = _cell_key(table_index, row_lookup, tag, 1 if is_debit else 6)
        details_key = _cell_key(table_index, row_lookup, tag, 2 if is_debit else 7)
        folio_key = _cell_key(table_index, row_lookup, tag, 3 if is_debit else 8)
        amount_key = _cell_key(table_index, row_lookup, tag, 4 if is_debit else 9)
        opposite_amount_key = _cell_key(table_index, row_lookup, tag, 9 if is_debit else 4)
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=row_key, hint_text=row_text)
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=day_key, hint_text=day_text)
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=details_key, hint_text=f"Write '{details_text}' in Details.")
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=folio_key, hint_text=f"Use '{folio_text}' in Fol because this posting comes from {folio_text}.")
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=amount_key, hint_text=amount_text, derivation_text=derivation_text)
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=opposite_amount_key, hint_text=f"Leave this side blank. This row belongs on the {side} side of the Trading Stock account.")

    _entry_hint(
        tag="opening_balance",
        side="debit",
        day_text="Opening balances are brought down on day 1.",
        details_text="Balance b/d",
        folio_text="b/d",
        amount=opening,
        row_text="Row purpose: opening trading stock on the debit side at the start of the month.",
        amount_text="Opening stock increases the debit side of Trading Stock.",
        derivation_text=f"Opening balance brought down = {fmt_money(opening)}.",
    )
    _entry_hint(
        tag="bank_cpj",
        side="debit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Bank",
        folio_text="CPJ",
        amount=bank_cpj,
        row_text="Row purpose: cash purchases of trading stock increase the asset, so they are debited.",
        amount_text="Use the Trading Stock column total from the CPJ and post it on the debit side because purchases increase Trading Stock.",
        derivation_text=f"Cash purchases from CPJ = {fmt_money(bank_cpj)}.",
    )
    _entry_hint(
        tag="creditors_cj",
        side="debit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Creditors control",
        folio_text="CJ",
        amount=creditors_cj,
        row_text="Row purpose: credit purchases of trading stock increase the asset, so they are debited.",
        amount_text="Use the Trading Stock column total from the CJ and post it on the debit side because purchases increase Trading Stock.",
        derivation_text=f"Credit purchases from CJ = {fmt_money(creditors_cj)}.",
    )
    _entry_hint(
        tag="petty_cash_pcj",
        side="debit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Petty cash",
        folio_text="PCJ",
        amount=petty_cash_pcj,
        row_text="Row purpose: petty-cash purchases of trading stock increase the asset, so they are debited.",
        amount_text="Use the Trading Stock column total from the PCJ and post it on the debit side.",
        derivation_text=f"Petty-cash purchases from PCJ = {fmt_money(petty_cash_pcj)}.",
    )
    _entry_hint(
        tag="debtors_returns_daj",
        side="debit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Cost of sales",
        folio_text="DAJ",
        amount=debtors_returns_daj,
        row_text="Row purpose: stock returned by debtors comes back into Trading Stock at cost price, so it is debited.",
        amount_text="Use the Cost of Sales column amount from the DAJ on the debit side because returns from debtors increase stock on hand again.",
        derivation_text=f"Returns from debtors at cost from DAJ = {fmt_money(debtors_returns_daj)}.",
    )
    _entry_hint(
        tag="creditors_returns_caj",
        side="credit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Creditors control",
        folio_text="CAJ",
        amount=creditors_returns_caj,
        row_text="Row purpose: stock returned to suppliers reduces Trading Stock, so it is credited.",
        amount_text="Use the Trading Stock column total from the CAJ on the credit side because returns to creditors reduce the stock asset.",
        derivation_text=f"Returns to creditors from CAJ = {fmt_money(creditors_returns_caj)}.",
    )
    _entry_hint(
        tag="cost_of_sales_crj",
        side="credit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Cost of sales",
        folio_text="CRJ",
        amount=cost_of_sales_crj,
        row_text="Row purpose: cash sales reduce stock at cost price, so Trading Stock is credited.",
        amount_text="Use the Cost of Sales column amount from the CRJ on the credit side because stock sold leaves the business at cost.",
        derivation_text=f"Cost of sales on cash sales from CRJ = {fmt_money(cost_of_sales_crj)}.",
    )
    _entry_hint(
        tag="cost_of_sales_dj",
        side="credit",
        day_text="Post month-end journal totals on day 31.",
        details_text="Cost of sales",
        folio_text="DJ",
        amount=cost_of_sales_dj,
        row_text="Row purpose: credit sales reduce stock at cost price, so Trading Stock is credited.",
        amount_text="Use the Cost of Sales column amount from the DJ on the credit side because stock sold on credit still leaves the business at cost.",
        derivation_text=f"Cost of sales on credit sales from DJ = {fmt_money(cost_of_sales_dj)}.",
    )
    _entry_hint(
        tag="drawings_gj",
        side="credit",
        day_text="General Journal adjustments are posted on day 31.",
        details_text="Drawings",
        folio_text="GJ",
        amount=drawings_gj,
        row_text="Row purpose: stock taken by the owner reduces Trading Stock, so it is credited.",
        amount_text="Use the credit side because drawings reduce the stock asset.",
        derivation_text=f"Drawings from GJ = {fmt_money(drawings_gj)}.",
    )
    _entry_hint(
        tag="stock_deficit_gj",
        side="credit",
        day_text="General Journal adjustments are posted on day 31.",
        details_text="Stock deficit",
        folio_text="GJ",
        amount=stock_deficit_gj,
        row_text="Row purpose: a stock deficit reduces Trading Stock, so it is credited.",
        amount_text="Use the credit side because a stock shortage found during stock count reduces stock on hand.",
        derivation_text=f"Stock deficit from GJ = {fmt_money(stock_deficit_gj)}.",
    )
    _entry_hint(
        tag="donations_gj",
        side="credit",
        day_text="General Journal adjustments are posted on day 31.",
        details_text="Donations",
        folio_text="GJ",
        amount=donations_gj,
        row_text="Row purpose: donated stock leaves the business, so Trading Stock is credited.",
        amount_text="Use the credit side because goods given away as donations leave the business and reduce the asset.",
        derivation_text=f"Donations from GJ = {fmt_money(donations_gj)}.",
    )
    _entry_hint(
        tag="stationery_gj",
        side="credit",
        day_text="General Journal adjustments are posted on day 31.",
        details_text="Stationery",
        folio_text="GJ",
        amount=stationery_gj,
        row_text="Row purpose: this correction moves stock value out of Trading Stock, so it is credited.",
        amount_text="Use the credit side because this correction removes value that was wrongly left in Trading Stock when it should have been stationery.",
        derivation_text=f"Stationery correction from GJ = {fmt_money(stationery_gj)}.",
    )

    if "balance_cd_credit" in row_lookup:
        _entry_hint(
            tag="balance_cd_credit",
            side="credit",
            day_text="Balance c/d is recorded on the last day of the month.",
            details_text="Balance c/d",
            folio_text="c/d",
            amount=closing,
            row_text="Row purpose: this is the balancing figure placed on the credit side to make Total Dr = Total Cr.",
            amount_text="Balance c/d goes on the credit side when debit entries are greater than credit entries. This same amount is then carried forward as Balance b/d next month.",
            derivation_text=f"Balance c/d = Total debit − Total credit = {fmt_money(debit_total)} − {fmt_money(credit_total)} = {fmt_money(closing)}.",
        )
    if "balance_cd_debit" in row_lookup:
        _entry_hint(
            tag="balance_cd_debit",
            side="debit",
            day_text="Balance c/d is recorded on the last day of the month.",
            details_text="Balance c/d",
            folio_text="c/d",
            amount=abs(closing),
            row_text="Row purpose: this is the balancing figure placed on the debit side to make Total Dr = Total Cr.",
            amount_text="Balance c/d goes on the debit side when credit entries are greater than debit entries. This same amount is then carried forward as Balance b/d next month.",
            derivation_text=f"Balance c/d = Total credit − Total debit = {fmt_money(credit_total)} − {fmt_money(debit_total)} = {fmt_money(abs(closing))}.",
        )
    if "totals" in row_lookup:
        totals_row_key = _cell_key(table_index, row_lookup, "totals", 0)
        debit_total_key = _cell_key(table_index, row_lookup, "totals", 4)
        credit_total_key = _cell_key(table_index, row_lookup, "totals", 9)
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=totals_row_key, hint_text="Row purpose: add each side after including Balance c/d so both totals are equal.")
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=debit_total_key, hint_text="Add only the debit-side amounts to get the debit total.", derivation_text=f"Debit total = {fmt_money(debit_total)}.")
        _set_trading_stock_hint(cell_hints=cell_hints, derivation_map=derivation_map, cell_key=credit_total_key, hint_text="Add only the credit-side amounts to get the credit total.", derivation_text=f"Credit total = {fmt_money(credit_total)}.")
    if "balance_bd_debit" in row_lookup:
        _entry_hint(
            tag="balance_bd_debit",
            side="debit",
            day_text="The opening balance for the new month is brought down on day 1.",
            details_text="Balance b/d",
            folio_text="b/d",
            amount=abs(closing),
            row_text="Row purpose: carry the closing balance forward as the next month's opening balance.",
            amount_text="Balance b/d must equal the previous Balance c/d. Copy the same amount into the new month as the opening balance.",
            derivation_text=f"Balance b/d = previous Balance c/d = {fmt_money(abs(closing))}.",
        )
    if "balance_bd_credit" in row_lookup:
        _entry_hint(
            tag="balance_bd_credit",
            side="credit",
            day_text="The opening balance for the new month is brought down on day 1.",
            details_text="Balance b/d",
            folio_text="b/d",
            amount=abs(closing),
            row_text="Row purpose: carry the closing balance forward as the next month's opening balance.",
            amount_text="Balance b/d must equal the previous Balance c/d. Copy the same amount into the new month as the opening balance.",
            derivation_text=f"Balance b/d = previous Balance c/d = {fmt_money(abs(closing))}.",
        )


def _make_trading_stock_account_table(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    table_index: int,
    business: str,
    month: str,
    year: int,
    opening: float,
    bank_cpj: float,
    creditors_cj: float,
    petty_cash_pcj: float,
    debtors_returns_daj: float,
    creditors_returns_caj: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
    editable: bool,
    show_blanks: bool,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    m = month
    next_month_name, _next_year = _next_month(month=month, year=year)

    debit_total = round_money(opening + bank_cpj + creditors_cj + petty_cash_pcj + debtors_returns_daj)
    credit_total = round_money(
        creditors_returns_caj
        + cost_of_sales_crj
        + cost_of_sales_dj
        + drawings_gj
        + stock_deficit_gj
        + donations_gj
        + stationery_gj
    )
    closing = round_money(debit_total - credit_total)

    gl_headers = _make_trading_stock_account_headers()
    rows: List[List[Dict[str, Any]]] = []
    correct: Dict[str, Any] = {}
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    derivation_map: Dict[str, str] = {}
    working_map: Dict[str, str] = {}
    row_lookup: Dict[str, int] = {}

    editable_cols: List[int] = []
    if editable:
        if diff == "easy":
            editable_cols = [4, 9]
        elif diff == "medium":
            editable_cols = [2, 4, 7, 9]
        else:
            editable_cols = [1, 2, 3, 4, 6, 7, 8, 9]

    def _add_row(rix: int, values: List[Optional[str]]) -> None:
        row = build_prefixed_row(table_index=table_index, row_index=rix, values=values, editable_cols=editable_cols)
        rows.append(row)
        for cix, cell in enumerate(row):
            correct[f"t{table_index}_r{rix}_c{cix}"] = cell.get("value", "")

    def _add_named_row(tag: str, values: List[Optional[str]]) -> None:
        row_lookup[tag] = len(rows)
        _add_row(len(rows), values)

    _add_named_row("opening_balance", [m, "1", "Balance b/d", "b/d", fmt_money(opening), "", "", "", "", ""])
    _add_named_row("bank_cpj", [m, "31", "Bank", "CPJ", fmt_money(bank_cpj), "", "", "", "", ""])
    _add_named_row("creditors_cj", [m, "31", "Creditors control", "CJ", fmt_money(creditors_cj), "", "", "", "", ""])
    if petty_cash_pcj:
        _add_named_row("petty_cash_pcj", [m, "31", "Petty cash", "PCJ", fmt_money(petty_cash_pcj), "", "", "", "", ""])
    _add_named_row("debtors_returns_daj", [m, "31", "Cost of sales", "DAJ", fmt_money(debtors_returns_daj), "", "", "", "", ""])

    _add_named_row("creditors_returns_caj", ["", "", "", "", "", m, "31", "Creditors control", "CAJ", fmt_money(creditors_returns_caj)])
    _add_named_row("cost_of_sales_crj", ["", "", "", "", "", m, "31", "Cost of sales", "CRJ", fmt_money(cost_of_sales_crj)])
    _add_named_row("cost_of_sales_dj", ["", "", "", "", "", m, "31", "Cost of sales", "DJ", fmt_money(cost_of_sales_dj)])
    if drawings_gj:
        _add_named_row("drawings_gj", ["", "", "", "", "", m, "31", "Drawings", "GJ", fmt_money(drawings_gj)])
    if stock_deficit_gj:
        _add_named_row("stock_deficit_gj", ["", "", "", "", "", m, "31", "Stock deficit", "GJ", fmt_money(stock_deficit_gj)])
    if donations_gj:
        _add_named_row("donations_gj", ["", "", "", "", "", m, "31", "Donations", "GJ", fmt_money(donations_gj)])
    if stationery_gj:
        _add_named_row("stationery_gj", ["", "", "", "", "", m, "31", "Stationery", "GJ", fmt_money(stationery_gj)])

    if closing >= 0:
        _add_named_row("balance_cd_credit", ["", "", "", "", "", m, "31", "Balance c/d", "c/d", fmt_money(closing)])
        total = round_money(debit_total)
        _add_named_row("totals", ["", "", "Totals", "", fmt_money(total), "", "", "Totals", "", fmt_money(total)])
        _add_named_row("balance_bd_debit", [next_month_name, "1", "Balance b/d", "b/d", fmt_money(closing), "", "", "", "", ""])
    else:
        bal = round_money(-closing)
        _add_named_row("balance_cd_debit", [m, "31", "Balance c/d", "c/d", fmt_money(bal), "", "", "", "", ""])
        total = round_money(credit_total)
        _add_named_row("totals", ["", "", "Totals", "", fmt_money(total), "", "", "Totals", "", fmt_money(total)])
        _add_named_row("balance_bd_credit", ["", "", "", "", "", next_month_name, "1", "Balance b/d", "b/d", fmt_money(bal)])

    if show_blanks:
        for rix, row in enumerate(rows):
            for cix in editable_cols:
                key = f"t{table_index}_r{rix}_c{cix}"
                if key in correct and str(correct[key] or ""):
                    row[cix]["value"] = ""

    journal: Dict[str, Any] = {
        "title": f"{business} - Trading Stock account",
        "journal_type": "trading_stock_account",
        "headers": gl_headers,
        "rows": rows,
        "row_lookup": row_lookup,
        "column_help": headers_to_column_help(journal_type="trading_stock_account", headers=gl_headers),
    }

    if mode_norm == "scaffold":
        _populate_trading_stock_scaffold_metadata(
            table_index=table_index,
            row_lookup=row_lookup,
            cell_hints=cell_hints,
            derivation_map=derivation_map,
            opening=opening,
            bank_cpj=bank_cpj,
            creditors_cj=creditors_cj,
            petty_cash_pcj=petty_cash_pcj,
            debtors_returns_daj=debtors_returns_daj,
            creditors_returns_caj=creditors_returns_caj,
            cost_of_sales_crj=cost_of_sales_crj,
            cost_of_sales_dj=cost_of_sales_dj,
            drawings_gj=drawings_gj,
            stock_deficit_gj=stock_deficit_gj,
            donations_gj=donations_gj,
            stationery_gj=stationery_gj,
            debit_total=debit_total,
            credit_total=credit_total,
            closing=closing,
        )
        _populate_trading_stock_teaching_map(
            table_index=table_index,
            row_lookup=row_lookup,
            cell_teaching_map=cell_teaching_map,
            opening=opening,
            bank_cpj=bank_cpj,
            creditors_cj=creditors_cj,
            petty_cash_pcj=petty_cash_pcj,
            debtors_returns_daj=debtors_returns_daj,
            creditors_returns_caj=creditors_returns_caj,
            cost_of_sales_crj=cost_of_sales_crj,
            cost_of_sales_dj=cost_of_sales_dj,
            drawings_gj=drawings_gj,
            stock_deficit_gj=stock_deficit_gj,
            donations_gj=donations_gj,
            stationery_gj=stationery_gj,
            debit_total=debit_total,
            credit_total=credit_total,
            closing=closing,
        )
        journal["cell_hints"] = cell_hints
        journal["cell_teaching_map"] = cell_teaching_map
        journal["derivation_map"] = derivation_map
        journal["working_map"] = working_map

    return journal, correct


def _make_trading_stock_prepare_from_journals_question_once(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)
    values = _build_trading_stock_values(r=r, difficulty=difficulty)
    _validate_trading_stock_values(values)
    opening = float(values["opening"])
    bank_cpj = float(values["bank_cpj"])
    creditors_cj = float(values["creditors_cj"])
    petty_cash_pcj = float(values["petty_cash_pcj"])
    debtors_returns_daj = float(values["debtors_returns_daj"])
    creditors_returns_caj = float(values["creditors_returns_caj"])
    cost_of_sales_crj = float(values["cost_of_sales_crj"])
    cost_of_sales_dj = float(values["cost_of_sales_dj"])
    drawings_gj = float(values["drawings_gj"])
    stock_deficit_gj = float(values["stock_deficit_gj"])
    donations_gj = float(values["donations_gj"])
    stationery_gj = float(values["stationery_gj"])

    j0, correct0 = _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=0,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=True,
        show_blanks=True,
    )

    info_lines = [
        f"Opening stock (Balance b/d): {fmt_money(opening)}",
        f"Cash purchases of stock (CPJ Trading Stock column): {fmt_money(bank_cpj)}",
        f"Credit purchases of stock (CJ Trading Stock column): {fmt_money(creditors_cj)}",
        f"Returns from debtors at cost (DAJ Cost of Sales column): {fmt_money(debtors_returns_daj)}",
        f"Returns to creditors (CAJ Trading Stock column): {fmt_money(creditors_returns_caj)}",
        f"Cost of sales on cash sales (CRJ Cost of Sales column): {fmt_money(cost_of_sales_crj)}",
        f"Cost of sales on credit sales (DJ Cost of Sales column): {fmt_money(cost_of_sales_dj)}",
    ]
    _append_special_entry_info_lines(
        info_lines,
        petty_cash_pcj=petty_cash_pcj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
    )

    prompt = (
        f"{business}\nTrading Stock account\nMonth: {month} {year}\n\n"
        "The following totals were extracted from the journals.\n\n"
        + "\n".join(info_lines)
        + "\n\nRequired:\nPrepare and balance the Trading Stock account (at cost price)."
    )

    # ── Build rubric_map (per-cell marking metadata) ──
    # Debit entries in col 4 (rows 0-4), credit entries in col 9 (rows 5-11)
    debit_total = round_money(opening + bank_cpj + creditors_cj + petty_cash_pcj + debtors_returns_daj)
    credit_total = round_money(
        creditors_returns_caj + cost_of_sales_crj + cost_of_sales_dj
        + drawings_gj + stock_deficit_gj + donations_gj + stationery_gj
    )
    closing = round_money(debit_total - credit_total)

    row_lookup = dict(j0.get("row_lookup") or {})
    balance_cd_tag = "balance_cd_credit" if "balance_cd_credit" in row_lookup else "balance_cd_debit"

    rubric_map = {
        _cell_key(0, row_lookup, "opening_balance", 4): {"formula_structure": "Opening balance b/d", "foundational_values": [opening], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "bank_cpj", 4): {"formula_structure": "Cash purchases (CPJ)", "foundational_values": [bank_cpj], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "creditors_cj", 4): {"formula_structure": "Credit purchases (CJ)", "foundational_values": [creditors_cj], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "debtors_returns_daj", 4): {"formula_structure": "Returns from debtors (DAJ)", "foundational_values": [debtors_returns_daj], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "creditors_returns_caj", 9): {"formula_structure": "Returns to creditors (CAJ)", "foundational_values": [creditors_returns_caj], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "cost_of_sales_crj", 9): {"formula_structure": "Cost of sales - cash (CRJ)", "foundational_values": [cost_of_sales_crj], "operations": [], "max_score": 1.0},
        _cell_key(0, row_lookup, "cost_of_sales_dj", 9): {"formula_structure": "Cost of sales - credit (DJ)", "foundational_values": [cost_of_sales_dj], "operations": [], "max_score": 1.0},
    }
    if "petty_cash_pcj" in row_lookup:
        rubric_map[_cell_key(0, row_lookup, "petty_cash_pcj", 4)] = {"formula_structure": "Petty cash purchases (PCJ)", "foundational_values": [petty_cash_pcj], "operations": [], "max_score": 1.0}
    if "drawings_gj" in row_lookup:
        rubric_map[_cell_key(0, row_lookup, "drawings_gj", 9)] = {"formula_structure": "Drawings (GJ)", "foundational_values": [drawings_gj], "operations": [], "max_score": 1.0}
    if stock_deficit_gj:
        rubric_map[_cell_key(0, row_lookup, "stock_deficit_gj", 9)] = {"formula_structure": "Stock deficit (GJ)", "foundational_values": [stock_deficit_gj], "operations": [], "max_score": 1.0}
    if donations_gj:
        rubric_map[_cell_key(0, row_lookup, "donations_gj", 9)] = {"formula_structure": "Donations (GJ)", "foundational_values": [donations_gj], "operations": [], "max_score": 1.0}
    if stationery_gj:
        rubric_map[_cell_key(0, row_lookup, "stationery_gj", 9)] = {"formula_structure": "Stationery (GJ)", "foundational_values": [stationery_gj], "operations": [], "max_score": 1.0}

    # Balance c/d depends on all entries
    rubric_map[_cell_key(0, row_lookup, balance_cd_tag, 9)] = {
        "formula_structure": "Balance c/d = Total debits − Total credits",
        "foundational_values": [debit_total, credit_total],
        "operations": ["−"],
        "max_score": 1.5,
    }

    dependency_sources = [
        _cell_key(0, row_lookup, "opening_balance", 4),
        _cell_key(0, row_lookup, "bank_cpj", 4),
        _cell_key(0, row_lookup, "creditors_cj", 4),
        _cell_key(0, row_lookup, "debtors_returns_daj", 4),
        _cell_key(0, row_lookup, "creditors_returns_caj", 9),
        _cell_key(0, row_lookup, "cost_of_sales_crj", 9),
        _cell_key(0, row_lookup, "cost_of_sales_dj", 9),
    ]
    for optional_tag, column_index in [
        ("petty_cash_pcj", 4),
        ("drawings_gj", 9),
        ("stock_deficit_gj", 9),
        ("donations_gj", 9),
        ("stationery_gj", 9),
    ]:
        if optional_tag in row_lookup:
            dependency_sources.append(_cell_key(0, row_lookup, optional_tag, column_index))
    dependency_map = {
        _cell_key(0, row_lookup, balance_cd_tag, 9): dependency_sources,
    }

    _validate_trading_stock_account_output(
        journal=j0,
        correct_map=correct0,
        table_index=0,
        month=month,
        values=values,
    )

    return make_journal(
        prompt=prompt,
        journal_type="trading_stock_account",
        headers=j0["headers"],
        rows=j0["rows"],
        correct_map=correct0,
        guidelines=_trading_stock_guidelines(),
        cell_hints=j0.get("cell_hints") if str(mode or "").strip().lower() == "scaffold" else None,
        cell_teaching_map=j0.get("cell_teaching_map") if str(mode or "").strip().lower() == "scaffold" else None,
        derivation_map=j0.get("derivation_map") if str(mode or "").strip().lower() == "scaffold" else None,
        working_map=j0.get("working_map") if str(mode or "").strip().lower() == "scaffold" else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )


def make_trading_stock_prepare_from_journals_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    return _make_trading_stock_with_retry(
        r=r,
        difficulty=difficulty,
        mode=mode,
        builder=_make_trading_stock_prepare_from_journals_question_once,
    )


def _make_trading_stock_fill_missing_details_question_once(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)
    values = _build_trading_stock_values(r=r, difficulty=difficulty)
    _validate_trading_stock_values(values)
    opening = float(values["opening"])
    bank_cpj = float(values["bank_cpj"])
    creditors_cj = float(values["creditors_cj"])
    petty_cash_pcj = float(values["petty_cash_pcj"])
    debtors_returns_daj = float(values["debtors_returns_daj"])
    creditors_returns_caj = float(values["creditors_returns_caj"])
    cost_of_sales_crj = float(values["cost_of_sales_crj"])
    cost_of_sales_dj = float(values["cost_of_sales_dj"])
    drawings_gj = float(values["drawings_gj"])
    stock_deficit_gj = float(values["stock_deficit_gj"])
    donations_gj = float(values["donations_gj"])
    stationery_gj = float(values["stationery_gj"])

    j0, correct0 = _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=0,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=False,
        show_blanks=False,
    )

    _validate_trading_stock_account_output(
        journal=j0,
        correct_map=correct0,
        table_index=0,
        month=month,
        values=values,
    )

    diff = str(difficulty or "easy").strip().lower()
    row_lookup = dict(j0.get("row_lookup") or {})
    if diff == "hard":
        target_specs = [
            (["bank_cpj"], 2, "(a)"),
            (["creditors_cj"], 3, "(b)"),
            (["petty_cash_pcj", "debtors_returns_daj"], 2, "(c)"),
            (["creditors_returns_caj"], 7, "(d)"),
            (["cost_of_sales_crj"], 8, "(e)"),
            (["drawings_gj", "cost_of_sales_dj"], 7, "(f)"),
            (["stock_deficit_gj", "cost_of_sales_dj"], 8, "(g)"),
            (["donations_gj", "stationery_gj"], 7, "(h)"),
        ]
    elif diff == "medium":
        target_specs = [
            (["bank_cpj"], 2, "(a)"),
            (["creditors_cj"], 3, "(b)"),
            (["petty_cash_pcj", "debtors_returns_daj"], 2, "(c)"),
            (["creditors_returns_caj"], 7, "(d)"),
            (["cost_of_sales_crj"], 8, "(e)"),
            (["drawings_gj", "cost_of_sales_dj"], 7, "(f)"),
        ]
    else:
        target_specs = [
            (["bank_cpj"], 2, "(a)"),
            (["creditors_cj"], 3, "(b)"),
            (["creditors_returns_caj"], 7, "(c)"),
            (["cost_of_sales_crj"], 8, "(d)"),
            (["drawings_gj", "cost_of_sales_dj"], 7, "(e)"),
        ]

    targets: List[Tuple[int, int, str]] = []
    used_rows: List[int] = []
    for row_tags, cix, token in target_specs:
        chosen_row = None
        for row_tag in row_tags:
            if row_tag in row_lookup and row_lookup[row_tag] not in used_rows:
                chosen_row = row_lookup[row_tag]
                break
        if chosen_row is None:
            continue
        used_rows.append(chosen_row)
        targets.append((chosen_row, cix, token))

    if not targets:
        raise _TradingStockScenarioValidationError("Trading stock missing-details question produced no target cells.")
    if len(targets) != len(target_specs):
        raise _TradingStockScenarioValidationError("Trading stock missing-details question produced fewer blanks than expected.")

    for (rix, cix, token) in targets:
        key = f"t0_r{rix}_c{cix}"
        correct0[key] = j0["rows"][rix][cix].get("value", "")
        j0["rows"][rix][cix]["value"] = token
        j0["rows"][rix][cix]["editable"] = True

    final_token = str(targets[-1][2])

    prompt = (
        f"{business}\nTrading Stock account\nMonth: {month} {year}\n\n"
        + f"Required:\nFill in the missing details (a) to {final_token} in the Trading Stock account.\n"
        "Remember: amounts are recorded at cost price, increases in stock are debited, and decreases in stock are credited."
    )
    return make_journal(
        prompt=prompt,
        journal_type="trading_stock_account",
        headers=j0["headers"],
        rows=j0["rows"],
        correct_map=correct0,
        guidelines=[
            "Use the folio (journal) to identify where each entry comes from.",
            "Choose the relevant journal column: Trading Stock for CPJ/CJ/CAJ/PCJ and Cost of Sales for CRJ/DJ/DAJ.",
            "Balance c/d is copied forward to the next month as Balance b/d.",
        ],
        cell_hints=j0.get("cell_hints") if str(mode or "").strip().lower() == "scaffold" else None,
        cell_teaching_map=j0.get("cell_teaching_map") if str(mode or "").strip().lower() == "scaffold" else None,
        derivation_map=j0.get("derivation_map") if str(mode or "").strip().lower() == "scaffold" else None,
        working_map=j0.get("working_map") if str(mode or "").strip().lower() == "scaffold" else None,
    )


def make_trading_stock_prepare_from_casted_journals_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    return _make_trading_stock_with_retry(
        r=r,
        difficulty=difficulty,
        mode=mode,
        builder=_make_trading_stock_prepare_from_casted_journals_question_once,
    )


def make_trading_stock_fill_missing_details_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    return _make_trading_stock_with_retry(
        r=r,
        difficulty=difficulty,
        mode=mode,
        builder=_make_trading_stock_fill_missing_details_question_once,
    )


def make_trading_stock_activity16_analysis_typed(*, r: random.Random) -> Dict[str, Any]:
    business = "Sophie Traders"
    prompt = (
        f"{business}\nActivity 16 (Analysis - Trading stock account)\n\n"
        "Answer the following:\n"
        "16.1 Does the business make use of the perpetual inventory system or periodic inventory system?\n"
        "16.2 Calculate the balance of stock on hand on 30 September 2010.\n"
        "16.3 Give a reason why the stock on hand decreased.\n"
        "16.4 Give the contra account for the amount on the debit side recorded from the DAJ.\n"
        "16.5 Give the contra account for the amount on the credit side recorded from the CAJ.\n"
        "16.6 If the business’ profit margin is 50% on cost price, calculate the sales price for the cash cost of sales amount.\n"
        "16.7 What is the source document for the debit recording for Bank, CPJ?\n"
        "16.8 What is the source document for the credit recording for Cost of sales, DJ?\n"
        "16.9 Give a reason for the debit recording of Stationery."
    )

    sample_answer = (
        "16.1 Perpetual inventory system\n"
        "16.2 Closing balance is the balancing figure in the Trading stock account\n"
        "16.3 Example: more stock was sold than purchased / seasonal demand changes\n"
        "16.4 Cost of sales\n"
        "16.5 Creditors control\n"
        "16.6 Sales price = 150/100 x cost of sales (cash)\n"
        "16.7 Cheque counterfoil\n"
        "16.8 Duplicate invoice\n"
        "16.9 Example: correction of an error / stationery incorrectly recorded and corrected"
    )
    return {
        "id": f"acct10_st_typed_{r.randrange(10**11, 10**12)}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "guidelines": [
            "Write each answer on its own line using the question number so your response stays easy to follow.",
            "For contra-account questions, think about which account on the opposite side of the Trading Stock entry completes the double entry.",
            "For source-document questions, use the journal and transaction type to identify the correct document.",
        ],
        "expected_answer_type": "text",
    }


def make_trading_stock_section3_analysis_typed(*, r: random.Random) -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)

    selling_price = float(r.randrange(8000, 40000 + 1, 100))
    markup_pct = float(r.choice([20, 25, 30, 40, 50]))
    cost_of_sales = round_money(selling_price / (1.0 + (markup_pct / 100.0)))

    prompt = (
        f"{business}\nTrading Stock account (Section 3)\nMonth: {month} {year}\n\n"
        "Answer the following questions:\n"
        "3.1 Give the contra account for cash purchases of trading stock.\n"
        "3.2 Give the contra account for credit purchases of trading stock.\n"
        "3.3 Give the contra account for returns to creditors (trading stock returned).\n"
        "3.4 Give the contra account for returns from debtors recorded at cost price in the Trading Stock account.\n"
        "3.5 Where is closing trading stock shown in the financial statements?\n"
        "3.6 Name the journal used to record cash purchases of trading stock.\n"
        "3.7 Name the journal used to record credit purchases of trading stock.\n"
        "3.8 Name the journal used to record returns to creditors.\n"
        "3.9 Goods were sold on credit for "
        + fmt_money(selling_price)
        + f". The mark-up is {markup_pct:g}% on cost price. Calculate the cost of sales." 
    )

    sample_answer = (
        "3.1 Bank (CPJ)\n"
        "3.2 Creditors control (CJ)\n"
        "3.3 Creditors control (CAJ)\n"
        "3.4 Cost of sales (DAJ)\n"
        "3.5 Closing stock is shown as a current asset in the Statement of Financial Position and is used in Cost of Sales in the Income Statement.\n"
        "3.6 Cash Payments Journal (CPJ)\n"
        "3.7 Creditors Journal (CJ)\n"
        "3.8 Creditors Allowances Journal (CAJ)\n"
        f"3.9 Cost of sales = selling price / (1 + mark-up%) = {fmt_money(selling_price)} / (1 + {markup_pct:g}/100) = {fmt_money(cost_of_sales)}"
    )

    return {
        "id": f"acct10_st_typed_{r.randrange(10**11, 10**12)}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "guidelines": [
            "Answer each numbered item on a separate line.",
            "If the question asks for a contra account, identify the other account in the double entry.",
            "For mark-up calculations, convert from selling price back to cost before giving the final amount.",
        ],
        "expected_answer_type": "text",
    }


def _make_trading_stock_prepare_with_two_returns_percent_question_once(
    *, r: random.Random, difficulty: str = "easy", mode: str = ""
) -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)

    values = _build_trading_stock_values(r=r, difficulty=difficulty)
    _validate_trading_stock_values(values)
    _validate_returns_percentage_variant(values=values)
    opening = float(values["opening"])
    bank_cpj = float(values["bank_cpj"])
    creditors_cj = float(values["creditors_cj"])
    petty_cash_pcj = float(values["petty_cash_pcj"])
    debtors_returns_daj = float(values["debtors_returns_daj"])
    creditors_returns_caj = float(values["creditors_returns_caj"])
    cost_of_sales_crj = float(values["cost_of_sales_crj"])
    cost_of_sales_dj = float(values["cost_of_sales_dj"])
    drawings_gj = float(values["drawings_gj"])
    stock_deficit_gj = float(values["stock_deficit_gj"])
    donations_gj = float(values["donations_gj"])
    stationery_gj = float(values["stationery_gj"])

    j0, correct0 = _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=0,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=True,
        show_blanks=True,
    )

    returns_to_creditors_pct = (creditors_returns_caj / creditors_cj) * 100.0 if creditors_cj else 0.0
    total_cost_of_sales = round_money(cost_of_sales_crj + cost_of_sales_dj)
    returns_from_debtors_pct = (debtors_returns_daj / total_cost_of_sales) * 100.0 if total_cost_of_sales else 0.0

    _validate_trading_stock_account_output(
        journal=j0,
        correct_map=correct0,
        table_index=0,
        month=month,
        values=values,
    )

    mode_norm = str(mode or "").strip().lower()
    if mode_norm == "scaffold":
        row_lookup = dict(j0.get("row_lookup") or {})
        cell_hints = j0.setdefault("cell_hints", {})
        cell_teaching_map = j0.setdefault("cell_teaching_map", {})
        derivation_map = j0.setdefault("derivation_map", {})

        def _append_variant_hint(cell_key: str, hint_text: str, derivation_text: str = "") -> None:
            current_hint = str(cell_hints.get(cell_key) or "").strip()
            cell_hints[cell_key] = f"{current_hint} {hint_text}".strip() if current_hint else hint_text
            if derivation_text:
                current_derivation = str(derivation_map.get(cell_key) or "").strip()
                derivation_map[cell_key] = f"{current_derivation} {derivation_text}".strip() if current_derivation else derivation_text

        creditors_returns_key = _cell_key(0, row_lookup, "creditors_returns_caj", 9)
        creditors_purchases_key = _cell_key(0, row_lookup, "creditors_cj", 4)
        debtors_returns_key = _cell_key(0, row_lookup, "debtors_returns_daj", 4)
        cash_sales_key = _cell_key(0, row_lookup, "cost_of_sales_crj", 9)
        credit_sales_key = _cell_key(0, row_lookup, "cost_of_sales_dj", 9)

        _append_variant_hint(
            creditors_returns_key,
            "For % returns to creditors, use this CAJ amount as the numerator.",
            f"Returns to creditors % = ({fmt_money(creditors_returns_caj)} / {fmt_money(creditors_cj)}) × 100 = {returns_to_creditors_pct:.1f}%.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=creditors_returns_key,
            role_in_requirement="Use this amount when calculating the percentage of returns to creditors.",
            evidence_from_question="This CAJ amount is the returns-to-creditors figure in the Trading Stock account.",
            rule_or_principle="For a percentage of returns to creditors, CAJ is the numerator and CJ is the denominator.",
            how_to_derive=f"Returns to creditors % = ({fmt_money(creditors_returns_caj)} / {fmt_money(creditors_cj)}) × 100 = {returns_to_creditors_pct:.1f}%.",
            transfer_tip="Use only credit purchases as the denominator; do not add cash purchases.",
        )
        _append_variant_hint(
            creditors_purchases_key,
            "Use the CJ trading stock total as the denominator for % returns to creditors. Do not include cash purchases.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=creditors_purchases_key,
            role_in_requirement="Use this amount when calculating the percentage of returns to creditors.",
            evidence_from_question="This CJ amount is the credit-purchases figure in the Trading Stock account.",
            rule_or_principle="The percentage of returns to creditors compares returns to the original credit purchases.",
            how_to_derive=f"Denominator for returns to creditors % = {fmt_money(creditors_cj)}.",
            transfer_tip="Do not use total purchases if the question specifically asks about credit purchases.",
        )
        _append_variant_hint(
            debtors_returns_key,
            "For % returns from debtors, use the DAJ cost-price amount as the numerator. Do not use selling price.",
            f"Returns from debtors % = ({fmt_money(debtors_returns_daj)} / {fmt_money(total_cost_of_sales)}) × 100 = {returns_from_debtors_pct:.1f}%.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=debtors_returns_key,
            role_in_requirement="Use this amount when calculating the percentage of returns from debtors.",
            evidence_from_question="This DAJ figure is the cost-price value of stock returned by debtors.",
            rule_or_principle="Returns from debtors are compared to total cost of sales at cost price.",
            how_to_derive=f"Returns from debtors % = ({fmt_money(debtors_returns_daj)} / {fmt_money(total_cost_of_sales)}) × 100 = {returns_from_debtors_pct:.1f}%.",
            transfer_tip="The Trading Stock account uses cost price, so do not convert this numerator to selling price.",
        )
        _append_variant_hint(
            cash_sales_key,
            "Add this CRJ cost-of-sales amount to the DJ cost-of-sales amount to get total cost of sales for the denominator.",
            f"Total cost of sales = {fmt_money(cost_of_sales_crj)} + {fmt_money(cost_of_sales_dj)} = {fmt_money(total_cost_of_sales)}.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=cash_sales_key,
            role_in_requirement="Use this amount as part of the denominator for the returns-from-debtors percentage.",
            evidence_from_question="This CRJ figure is the cost of sales on cash sales.",
            rule_or_principle="Total cost of sales for this question equals CRJ cost of sales plus DJ cost of sales.",
            how_to_derive=f"Total cost of sales = {fmt_money(cost_of_sales_crj)} + {fmt_money(cost_of_sales_dj)} = {fmt_money(total_cost_of_sales)}.",
            transfer_tip="The denominator uses both cash and credit cost-of-sales amounts when the question says total cost of sales.",
        )
        _append_variant_hint(
            credit_sales_key,
            "Add this DJ cost-of-sales amount to the CRJ cost-of-sales amount to get total cost of sales for the denominator.",
        )
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=credit_sales_key,
            role_in_requirement="Use this amount as part of the denominator for the returns-from-debtors percentage.",
            evidence_from_question="This DJ figure is the cost of sales on credit sales.",
            rule_or_principle="Total cost of sales for this question equals CRJ cost of sales plus DJ cost of sales.",
            how_to_derive=f"Add this amount to {fmt_money(cost_of_sales_crj)} to confirm the denominator of {fmt_money(total_cost_of_sales)}.",
            transfer_tip="If the question says total cost of sales, do not ignore either the cash-sales or credit-sales cost figure.",
        )

    info_lines = [
        f"Opening stock (Balance b/d): {fmt_money(opening)}",
        f"Cash purchases of stock (CPJ Trading Stock column): {fmt_money(bank_cpj)}",
        f"Credit purchases of stock (CJ Trading Stock column): {fmt_money(creditors_cj)}",
        f"Returns from debtors at cost (DAJ Cost of Sales column): {fmt_money(debtors_returns_daj)}",
        f"Returns to creditors (CAJ Trading Stock column): {fmt_money(creditors_returns_caj)}",
        f"Cost of sales on cash sales (CRJ Cost of Sales column): {fmt_money(cost_of_sales_crj)}",
        f"Cost of sales on credit sales (DJ Cost of Sales column): {fmt_money(cost_of_sales_dj)}",
    ]
    _append_special_entry_info_lines(
        info_lines,
        petty_cash_pcj=petty_cash_pcj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
    )

    prompt = (
        f"{business}\nTrading Stock account\nMonth: {month} {year}\n\n"
        "Information: Journal totals (casting)\n\n"
        + "\n".join(info_lines)
        + "\n\n"
        "Required:\n"
        "1) Prepare and balance the Trading Stock account (at cost price).\n"
        "2) Calculate % returns to creditors on credit purchases.\n"
        "3) Calculate % returns from debtors on total cost of sales (cash + credit)."
    )

    return make_journal(
        prompt=prompt,
        journal_type="trading_stock_account",
        headers=j0["headers"],
        rows=j0["rows"],
        correct_map=correct0,
        guidelines=[
            *_trading_stock_guidelines(),
            "returns_to_creditors% = (CAJ / CJ) × 100",
            "returns_from_debtors% = (DAJ / (CRJ + DJ)) × 100",
            f"Answer check: returns_to_creditors% = ({fmt_money(creditors_returns_caj)} / {fmt_money(creditors_cj)}) × 100 = {returns_to_creditors_pct:.1f}%",
            f"Answer check: returns_from_debtors% = ({fmt_money(debtors_returns_daj)} / {fmt_money(total_cost_of_sales)}) × 100 = {returns_from_debtors_pct:.1f}%",
        ],
        cell_hints=j0.get("cell_hints") if str(mode or "").strip().lower() == "scaffold" else None,
        cell_teaching_map=j0.get("cell_teaching_map") if str(mode or "").strip().lower() == "scaffold" else None,
        derivation_map=j0.get("derivation_map") if str(mode or "").strip().lower() == "scaffold" else None,
        working_map=j0.get("working_map") if str(mode or "").strip().lower() == "scaffold" else None,
    )


def make_trading_stock_prepare_with_two_returns_percent_question(
    *, r: random.Random, difficulty: str = "easy", mode: str = ""
) -> Dict[str, Any]:
    return _make_trading_stock_with_retry(
        r=r,
        difficulty=difficulty,
        mode=mode,
        builder=_make_trading_stock_prepare_with_two_returns_percent_question_once,
    )


def make_trading_stock_markup_trade_discount_typed(*, r: random.Random) -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)

    paid_after_discount = float(r.randrange(5000, 30000 + 1, 100))
    discount_pct = float(r.choice([5, 10, 15]))
    markup_pct = float(r.choice([25, 30, 50]))

    original_price = round_money(paid_after_discount / (1.0 - (discount_pct / 100.0)))
    selling_price = round_money(original_price * (1.0 + (markup_pct / 100.0)))

    prompt = (
        f"{business}\nTrading stock calculations\nMonth: {month} {year}\n\n"
        "A supplier allowed a trade discount on the list price.\n\n"
        f"Amount paid (after {discount_pct:g}% trade discount): {fmt_money(paid_after_discount)}\n"
        f"Mark-up: {markup_pct:g}% on cost price\n\n"
        "Required:\n"
        "1) Calculate the original cost price BEFORE the trade discount.\n"
        "2) Calculate the selling price if the goods are marked up on cost price."
    )

    sample_answer = (
        f"1) Cost before discount = paid / (1 − discount%) = {fmt_money(paid_after_discount)} / (1 − {discount_pct:g}/100) = {fmt_money(original_price)}\n"
        f"2) Selling price = cost × (1 + mark-up%) = {fmt_money(original_price)} × (1 + {markup_pct:g}/100) = {fmt_money(selling_price)}"
    )

    return {
        "id": f"acct10_st_typed_{r.randrange(10**11, 10**12)}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "guidelines": [
            "Set out each calculation vertically, one step per line.",
            "First reverse the trade discount to get the original cost price.",
            "Then apply the mark-up to the original cost price to find the selling price.",
        ],
        "expected_answer_type": "text",
    }


def make_trading_stock_prepare_with_returns_percent_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    base = make_trading_stock_prepare_from_journals_question(r=r, difficulty=difficulty, mode=mode)
    percent = r.choice([10, 12.5, 15, 20])
    base["prompt"] = (
        str(base.get("prompt", ""))
        + "\n\nAdditional requirement:\n"
        + f"Calculate the returns percentage if returns to creditors amounted to {percent}% of credit purchases."
    )
    return base


def make_trading_stock_account_table(
    *,
    r: random.Random,
    difficulty: str,
    mode: str,
    table_index: int,
    business: str,
    month: str,
    year: int,
    opening: float,
    bank_cpj: float,
    creditors_cj: float,
    petty_cash_pcj: float,
    debtors_returns_daj: float,
    creditors_returns_caj: float,
    cost_of_sales_crj: float,
    cost_of_sales_dj: float,
    drawings_gj: float,
    stock_deficit_gj: float,
    donations_gj: float,
    stationery_gj: float,
    editable: bool,
    show_blanks: bool,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    return _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=table_index,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=editable,
        show_blanks=show_blanks,
    )


def _make_trading_stock_prepare_with_discount_calc_question_once(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)
    diff = str(difficulty or "easy").strip().lower()
    values = _build_trading_stock_values(r=r, difficulty=difficulty)
    _validate_trading_stock_values(values)
    opening = float(values["opening"])
    cash_paid = round_money(r.randrange(2000, 9001, 50) if diff == "easy" else (r.randrange(3500, 12001, 50) if diff == "medium" else r.randrange(5000, 18001, 50)))
    disc_rate = r.choice([5, 10] if diff == "easy" else ([5, 10, 15] if diff == "medium" else [5, 10, 15]))
    cash_purchases_before_discount = round_money(cash_paid / (1 - (disc_rate / 100.0)))

    creditors_cj = float(values["creditors_cj"])
    petty_cash_pcj = float(values["petty_cash_pcj"])
    debtors_returns_daj = float(values["debtors_returns_daj"])
    creditors_returns_caj = float(values["creditors_returns_caj"])
    cost_of_sales_crj = float(values["cost_of_sales_crj"])
    cost_of_sales_dj = float(values["cost_of_sales_dj"])
    drawings_gj = float(values["drawings_gj"])
    stock_deficit_gj = float(values["stock_deficit_gj"])
    donations_gj = float(values["donations_gj"])
    stationery_gj = float(values["stationery_gj"])

    j0, correct0 = _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=0,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=cash_purchases_before_discount,
        creditors_cj=creditors_cj,
        petty_cash_pcj=petty_cash_pcj,
        debtors_returns_daj=debtors_returns_daj,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
        editable=True,
        show_blanks=True,
    )

    scenario_values = dict(values)
    scenario_values["bank_cpj"] = cash_purchases_before_discount
    _validate_trade_discount_variant(
        cash_paid=cash_paid,
        disc_rate=disc_rate,
        cash_purchases_before_discount=cash_purchases_before_discount,
        values=scenario_values,
    )
    _validate_trading_stock_account_output(
        journal=j0,
        correct_map=correct0,
        table_index=0,
        month=month,
        values=scenario_values,
    )

    mode_norm = str(mode or "").strip().lower()
    if mode_norm == "scaffold":
        row_lookup = dict(j0.get("row_lookup") or {})
        cell_hints = j0.setdefault("cell_hints", {})
        cell_teaching_map = j0.setdefault("cell_teaching_map", {})
        derivation_map = j0.setdefault("derivation_map", {})
        bank_key = _cell_key(0, row_lookup, "bank_cpj", 4)
        existing_hint = str(cell_hints.get(bank_key) or "").strip()
        extra_hint = "For this variant, work back to the original cost before discount and post that full amount to Trading Stock. Do not post the discounted cash paid amount."
        cell_hints[bank_key] = f"{existing_hint} {extra_hint}".strip() if existing_hint else extra_hint
        existing_derivation = str(derivation_map.get(bank_key) or "").strip()
        extra_derivation = f"Cash purchases before discount = {fmt_money(cash_paid)} / (1 - {disc_rate:g}/100) = {fmt_money(cash_purchases_before_discount)}."
        derivation_map[bank_key] = f"{existing_derivation} {extra_derivation}".strip() if existing_derivation else extra_derivation
        _append_trading_stock_teaching_hint(
            cell_teaching_map=cell_teaching_map,
            cell_key=bank_key,
            role_in_requirement="Use this amount for the cash-purchases posting in the Trading Stock account.",
            evidence_from_question=f"The question gives cash paid after a {disc_rate:g}% trade discount.",
            rule_or_principle="Trading Stock must be posted at the original cost before the trade discount is deducted.",
            how_to_derive=f"Cash purchases before discount = {fmt_money(cash_paid)} / (1 - {disc_rate:g}/100) = {fmt_money(cash_purchases_before_discount)}.",
            transfer_tip="A trade discount changes the calculation of cost price; do not post the discounted payment directly to Trading Stock.",
        )

    other_info_lines = [
        f"Opening stock (Balance b/d): {fmt_money(opening)}",
        f"Credit purchases of stock (CJ Trading Stock column): {fmt_money(creditors_cj)}",
        f"Returns to creditors (CAJ Trading Stock column): {fmt_money(creditors_returns_caj)}",
        f"Returns from debtors at cost (DAJ Cost of Sales column): {fmt_money(debtors_returns_daj)}",
        f"Cost of sales on cash sales (CRJ Cost of Sales column): {fmt_money(cost_of_sales_crj)}",
        f"Cost of sales on credit sales (DJ Cost of Sales column): {fmt_money(cost_of_sales_dj)}",
    ]
    _append_special_entry_info_lines(
        other_info_lines,
        petty_cash_pcj=petty_cash_pcj,
        drawings_gj=drawings_gj,
        stock_deficit_gj=stock_deficit_gj,
        donations_gj=donations_gj,
        stationery_gj=stationery_gj,
    )

    prompt = (
        f"{business}\nTrading Stock account\nMonth: {month} {year}\n\n"
        "Cash purchases were paid for after a trade discount.\n\n"
        f"Cash paid (after {disc_rate}% trade discount): {fmt_money(cash_paid)}\n"
        + f"Trade discount rate: {disc_rate:g}%\n\n"
        + "Other journal totals for the same month:\n"
        + "\n".join(other_info_lines)
        + "\n\n"
        "Required:\n"
        "1) Calculate the cash purchases BEFORE the trade discount.\n"
        "2) Prepare and balance the Trading Stock account (at cost price)."
    )

    return make_journal(
        prompt=prompt,
        journal_type="trading_stock_account",
        headers=j0["headers"],
        rows=j0["rows"],
        correct_map=correct0,
        guidelines=[
            *_trading_stock_guidelines(),
            "Trade discount reduces the amount paid: work back to the original cost before discount before posting the CPJ Trading Stock figure.",
        ],
        cell_hints=j0.get("cell_hints") if str(mode or "").strip().lower() == "scaffold" else None,
        cell_teaching_map=j0.get("cell_teaching_map") if str(mode or "").strip().lower() == "scaffold" else None,
        derivation_map=j0.get("derivation_map") if str(mode or "").strip().lower() == "scaffold" else None,
        working_map=j0.get("working_map") if str(mode or "").strip().lower() == "scaffold" else None,
    )


def make_trading_stock_prepare_with_discount_calc_question(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    return _make_trading_stock_with_retry(
        r=r,
        difficulty=difficulty,
        mode=mode,
        builder=_make_trading_stock_prepare_with_discount_calc_question_once,
    )


def _make_trading_stock_prepare_from_casted_journals_question_once(*, r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    business = _pick_trading_stock_business(r=r)
    month, year = _pick_trading_stock_period(r=r)

    diff = str(difficulty or "easy").strip().lower()
    if diff == "hard":
        opening = round_money(r.randrange(90000, 180001, 100))
        bank_cpj = round_money(r.randrange(50000, 140001, 100))
        creditors_cj = round_money(r.randrange(50000, 160001, 100))
        creditors_returns_caj = round_money(r.randrange(8000, 28001, 50))
        debtors_returns_cost = round_money(r.randrange(8000, 28001, 50))
        cost_of_sales_crj = round_money(r.randrange(25000, 140001, 100))
        cost_of_sales_dj = round_money(r.randrange(25000, 140001, 100))
    else:
        opening = round_money(r.randrange(50000, 120001, 100))
        bank_cpj = round_money(r.randrange(20000, 90001, 100))
        creditors_cj = round_money(r.randrange(20000, 110001, 100))
        creditors_returns_caj = round_money(r.randrange(3000, 18001, 50))
        debtors_returns_cost = round_money(r.randrange(3000, 18001, 50))
        cost_of_sales_crj = round_money(r.randrange(10000, 100001, 100))
        cost_of_sales_dj = round_money(r.randrange(10000, 100001, 100))

    minimum_closing = 6000.0 if diff == "hard" else (4000.0 if diff == "medium" else 2500.0)
    closing = round_money(
        opening
        + bank_cpj
        + creditors_cj
        + debtors_returns_cost
        - creditors_returns_caj
        - cost_of_sales_crj
        - cost_of_sales_dj
    )
    while closing < minimum_closing:
        opening = round_money(opening + 1000.0)
        closing = round_money(closing + 1000.0)

    scenario_values = {
        "opening": opening,
        "bank_cpj": bank_cpj,
        "creditors_cj": creditors_cj,
        "petty_cash_pcj": 0.0,
        "debtors_returns_daj": debtors_returns_cost,
        "creditors_returns_caj": creditors_returns_caj,
        "cost_of_sales_crj": cost_of_sales_crj,
        "cost_of_sales_dj": cost_of_sales_dj,
        "drawings_gj": 0.0,
        "stock_deficit_gj": 0.0,
        "donations_gj": 0.0,
        "stationery_gj": 0.0,
    }
    _validate_trading_stock_values(scenario_values)

    j0, correct0 = _make_trading_stock_account_table(
        r=r,
        difficulty=difficulty,
        mode=mode,
        table_index=0,
        business=business,
        month=month,
        year=year,
        opening=opening,
        bank_cpj=bank_cpj,
        creditors_cj=creditors_cj,
        petty_cash_pcj=0.0,
        debtors_returns_daj=debtors_returns_cost,
        creditors_returns_caj=creditors_returns_caj,
        cost_of_sales_crj=cost_of_sales_crj,
        cost_of_sales_dj=cost_of_sales_dj,
        drawings_gj=0.0,
        stock_deficit_gj=0.0,
        donations_gj=0.0,
        stationery_gj=0.0,
        editable=True,
        show_blanks=True,
    )

    _validate_trading_stock_account_output(
        journal=j0,
        correct_map=correct0,
        table_index=0,
        month=month,
        values=scenario_values,
    )

    prompt = (
        f"{business}\nTrading Stock account\nMonth: {month} {year}\n\n"
        + _build_casted_journal_prompt(
            bank_cpj=bank_cpj,
            creditors_cj=creditors_cj,
            creditors_returns_caj=creditors_returns_caj,
            debtors_returns_cost=debtors_returns_cost,
            cost_of_sales_crj=cost_of_sales_crj,
            cost_of_sales_dj=cost_of_sales_dj,
            opening=opening,
        )
        + "\n\n"
        "Required:\nPrepare and balance the Trading Stock account."
    )

    return make_journal(
        prompt=prompt,
        journal_type="trading_stock_account",
        headers=j0["headers"],
        rows=j0["rows"],
        correct_map=correct0,
        guidelines=[
            *_trading_stock_guidelines(),
            "Each journal now shows distractor totals. Select only the Trading Stock column or the Cost of Sales column that belongs in the Trading Stock account.",
        ],
        cell_hints=j0.get("cell_hints") if str(mode or "").strip().lower() == "scaffold" else None,
        cell_teaching_map=j0.get("cell_teaching_map") if str(mode or "").strip().lower() == "scaffold" else None,
        derivation_map=j0.get("derivation_map") if str(mode or "").strip().lower() == "scaffold" else None,
        working_map=j0.get("working_map") if str(mode or "").strip().lower() == "scaffold" else None,
    )
