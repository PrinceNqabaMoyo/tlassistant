from __future__ import annotations

import random

from typing import Any, Dict, List

from ..sole_trader.core import fmt_money, round_money
from ..sole_trader.journal_table import journal_editable_cols_by_difficulty
from ..sole_trader.names import pick_business_name, pick_person_name

from .sole_trader_shared import make_ta_tx
from .sole_trader_transaction_analysis import build_transaction_analysis_question_output
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_bank_fee_breakdown
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_cash_handling_fee
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_cash_withdrawal_for_wages
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_interest_on_current_account
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_overdraft_interest
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_owner_taking_stock
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_owner_withdrawal
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_packing_materials_unfavourable
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_petty_cash_on_behalf_of_debtor
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_postage_paid
from .sole_trader_transaction_analysis_builders import make_transaction_analysis_vehicle_purchase_on_credit
from .sole_trader_transaction_analysis_context import build_transaction_analysis_question_seed_context
from .sole_trader_transaction_analysis_context import build_transaction_analysis_template_bank_with_core_wrappers
from .sole_trader_transaction_analysis_context import pick_transaction_analysis_schema


def make_transaction_analysis_question(
    *,
    r: random.Random,
    difficulty: str = "easy",
    mode: str = "",
) -> Dict[str, Any]:
    mode_norm = str(mode or "").strip().lower()
    diff = str(difficulty or "easy").strip().lower()
    seed_context = build_transaction_analysis_question_seed_context(
        r=r,
        pick_business_name=pick_business_name,
        pick_person_name=pick_person_name,
    )
    business = str(seed_context["business"])
    debtor = str(seed_context["debtor"])
    creditor = str(seed_context["creditor"])
    markup_pct = float(seed_context["markup_pct"])
    selling_factor = float(seed_context["selling_factor"])

    def _make_petty_cash_on_behalf_of_debtor(*, amt: float, nr: str, debtor_name: str) -> List[Dict[str, Any]]:
        # This transaction has no net effect on the accounting equation (asset swaps), but some
        # archetypes show both effects in one cell as +amt/-amt.
        return make_transaction_analysis_petty_cash_on_behalf_of_debtor(
            tx_builder=make_ta_tx,
            fmt_money=fmt_money,
            amt=amt,
            nr=nr,
            debtor_name=debtor_name,
        )

    def _make_bank_fee_breakdown(*, service_fee: float, cash_handling_fee: float, overdraft_int: float, nr: str) -> List[Dict[str, Any]]:
        # Bank statement shows multiple fees and interest - each is a separate expense affecting bank
        return make_transaction_analysis_bank_fee_breakdown(
            tx_builder=make_ta_tx,
            service_fee=service_fee,
            cash_handling_fee=cash_handling_fee,
            overdraft_int=overdraft_int,
            nr=nr,
        )

    def _make_owner_withdrawal(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Owner withdraws cash from business bank account
        return make_transaction_analysis_owner_withdrawal(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_owner_taking_stock(*, cost: float, nr: str) -> List[Dict[str, Any]]:
        # Owner takes trading stock for personal use
        return make_transaction_analysis_owner_taking_stock(
            tx_builder=make_ta_tx,
            cost=cost,
            nr=nr,
        )

    def _make_interest_on_current_account(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Interest earned on current bank account
        return make_transaction_analysis_interest_on_current_account(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_overdraft_interest(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Interest on overdraft increases the overdraft (liability increases).
        return make_transaction_analysis_overdraft_interest(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_vehicle_purchase_on_credit(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Purchase vehicle on credit - increases Assets (Vehicle) and Liabilities (Creditors)
        return make_transaction_analysis_vehicle_purchase_on_credit(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_cash_handling_fee(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Cash handling fee charged by bank - expense, reduces bank
        return make_transaction_analysis_cash_handling_fee(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_cash_withdrawal_for_wages(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Cash withdrawn from bank to pay wages - asset swap Bank to Cash, then expense
        # Two rows: 1) Bank to Cash, 2) Wages expense paid from Cash
        return make_transaction_analysis_cash_withdrawal_for_wages(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_packing_materials_unfavourable(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Packing materials paid when bank is unfavourable (overdraft)
        return make_transaction_analysis_packing_materials_unfavourable(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    def _make_postage_paid(*, amt: float, nr: str) -> List[Dict[str, Any]]:
        # Postage paid from petty cash
        return make_transaction_analysis_postage_paid(
            tx_builder=make_ta_tx,
            amt=amt,
            nr=nr,
        )

    # ---- Approach 2 + hybrid mixing with compatibility rules (A) ----
    # Pick a schema for this question, then sample transactions from multiple archetype sets
    # that are compatible with that schema.
    schema = pick_transaction_analysis_schema(r=r)

    # Archetype set keys used for mixing; this is used for sampling diversity.
    all_archetype_keys = ["activity23", "activity24"] + [f"arch_{i}" for i in range(1, 26)]

    # Build a template bank with explicit journal/source usage so journal/source schemas work.
    template_bank = build_transaction_analysis_template_bank_with_core_wrappers(
        r=r,
        pick_amount=lambda base: float(r.choice(base)),
        round_money=round_money,
        selling_factor=selling_factor,
        fmt_money=fmt_money,
        tx_builder=make_ta_tx,
        debtor=debtor,
        markup_pct=markup_pct,
        make_petty_cash_on_behalf_of_debtor=_make_petty_cash_on_behalf_of_debtor,
        make_overdraft_interest=_make_overdraft_interest,
    )
    return build_transaction_analysis_question_output(
        r=r,
        schema=schema,
        template_bank=template_bank,
        difficulty=diff,
        mode_norm=mode_norm,
        business=business,
        markup_pct=markup_pct,
        debtor=debtor,
        creditor=creditor,
        editable_cols_builder=journal_editable_cols_by_difficulty,
    )
