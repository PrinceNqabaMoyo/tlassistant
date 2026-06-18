from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .final_accounts_generator.shared import (
    _build_answer_part_hints,
    _cell,
    _float_or_zero,
    _formula_hint_from_working,
    _make_calc,
    _make_fill_in_table_question,
    _make_id,
    _make_mcq,
    _make_table_wordbank,
    _make_typed,
    _money_matches,
    _rng,
    _round_money,
    _teaching_hint,
    _with_validation,
)
from .final_accounts_generator.core_families import (
    _gen_closing_transfers,
    _gen_depreciation,
)
from .final_accounts_generator.validation import (
    _FinalAccountsScenarioValidationError,
    _validate_final_accounts_question,
)
from .final_accounts_generator.adjustment_families import (
    _gen_bad_debts_and_recoveries as _gen_bad_debts_and_recoveries_extracted,
    _gen_consumable_stores_on_hand as _gen_consumable_stores_on_hand_extracted,
    _gen_error_corrections_and_reclassification as _gen_error_corrections_and_reclassification_extracted,
    _gen_interest_adjustments as _gen_interest_adjustments_extracted,
    _gen_trading_stock_variances as _gen_trading_stock_variances_extracted,
    _gen_year_end_adjustments as _gen_year_end_adjustments_extracted,
)
from .final_accounts_generator.trial_balance_families import (
    _gen_trial_balance as _gen_trial_balance_extracted,
)
from .final_accounts_generator.income_statement_families import (
    _gen_income_statement as _gen_income_statement_extracted,
)


# ---------------------------------------------------------------------------
# Sub-skill generators
# ---------------------------------------------------------------------------


def _gen_year_end_adjustments(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_year_end_adjustments_extracted(r)


def _gen_bad_debts_and_recoveries(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_bad_debts_and_recoveries_extracted(r)


def _gen_error_corrections_and_reclassification(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_error_corrections_and_reclassification_extracted(r)


def _gen_consumable_stores_on_hand(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_consumable_stores_on_hand_extracted(r)


def _gen_interest_adjustments(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_interest_adjustments_extracted(r)


def _gen_trading_stock_variances(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_trading_stock_variances_extracted(r)


def _gen_trial_balance(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_trial_balance_extracted(r)


def _gen_income_statement(r: random.Random) -> List[Dict[str, Any]]:
    return _gen_income_statement_extracted(r)
# Main entry point
# ---------------------------------------------------------------------------

def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
    rotation_ordinal: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    def _prompt_signature(question: Dict[str, Any]) -> str:
        prompt = str(question.get("prompt") or "").strip().lower()
        return " ".join(prompt.split())

    n = max(1, min(int(count), 20))
    try:
        rotation_base = max(0, int(rotation_ordinal or 0))
    except Exception:
        rotation_base = 0
    subskill_norm = str(subskill or "mixed").strip().lower()
    subskill_aliases = {
        "year_end_adjustments": "adjustments",
        "final_accounts": "income_statement",
        "post_closing_tb": "trial_balance",
        "bad_debts": "bad_debts_and_recoveries",
        "error_corrections": "error_corrections_and_reclassification",
        "reclassification": "error_corrections_and_reclassification",
        "interest_on_loan": "interest_adjustments",
        "interest_income": "interest_adjustments",
        "consumables": "consumable_stores_on_hand",
        "stationery": "consumable_stores_on_hand",
        "depreciation_core": "depreciation_core",
        "capital": "capital_calculation",
        "reversals": "reversals",
        "accrued_income": "accrued_income_and_reversals",
        "accrued_expenses": "accrued_expenses_and_reversals",
        "prepaid_expenses": "prepaid_expenses_and_reversals",
        "income_received_in_advance": "income_received_in_advance_and_reversals",
        "adjustment_journals": "adjustment_journal",
        "adjustment_analysis_table": "adjustment_analysis",
        "asset_register_table": "asset_register",
        "stock_variances": "trading_stock_variances",
        "trading_stock": "trading_stock_variances",
        "post_adjustment_tb": "post_adjustment_trial_balance",
        "post_closing_tb": "post_closing_trial_balance",
        "trading_account": "final_accounts_trading_account",
        "profit_and_loss": "final_accounts_profit_and_loss",
        "integrated_project": "integrated_final_accounts",
        "final_accounts_fill": "final_accounts_table",
    }
    resolved_subskill = subskill_aliases.get(subskill_norm, subskill_norm)

    closing_pool = _gen_closing_transfers(r)
    depreciation_pool = _gen_depreciation(r)
    adjustments_pool = _gen_year_end_adjustments(r)
    bad_debts_pool = _gen_bad_debts_and_recoveries(r)
    consumable_stores_pool = _gen_consumable_stores_on_hand(r)
    error_corrections_pool = _gen_error_corrections_and_reclassification(r)
    interest_adjustments_pool = _gen_interest_adjustments(r)
    trading_stock_variances_pool = _gen_trading_stock_variances(r)
    trial_balance_pool = _gen_trial_balance(r)
    income_stmt_pool = _gen_income_statement(r)
    base_adjustment_journal_pool = [q for q in adjustments_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    adjustment_analysis_pool = [q for q in adjustments_pool if str(q.get("question_type") or "").strip().lower() == "adjustment_analysis_table"]
    adjustment_ledger_pool = [q for q in adjustments_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    adjustment_final_accounts_pool = [q for q in adjustments_pool if str(q.get("question_type") or "").strip().lower() == "final_account_table"]
    adjustment_trial_balance_pool = [q for q in adjustments_pool if str(q.get("question_type") or "").strip().lower() == "trial_balance_table"]
    accrued_income_reversal_pool = [q for q in adjustment_ledger_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_reversal_ledger_fill"]
    accrued_expense_reversal_pool = [q for q in adjustment_ledger_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_reversal_ledger_fill"]
    prepaid_expense_reversal_pool = [q for q in adjustment_ledger_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_reversal_ledger_fill"]
    income_received_in_advance_reversal_pool = [q for q in adjustment_ledger_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_reversal_ledger_fill"]
    accrued_income_reversal_journal_pool = [q for q in base_adjustment_journal_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_reversal_journal_fill"]
    accrued_expense_reversal_journal_pool = [q for q in base_adjustment_journal_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_reversal_journal_fill"]
    prepaid_expense_reversal_journal_pool = [q for q in base_adjustment_journal_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_reversal_journal_fill"]
    income_received_in_advance_reversal_journal_pool = [q for q in base_adjustment_journal_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_reversal_journal_fill"]
    accrued_income_analysis_reversal_pool = [q for q in adjustment_analysis_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_analysis_fill"]
    accrued_expense_analysis_reversal_pool = [q for q in adjustment_analysis_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_analysis_fill"]
    prepaid_expense_analysis_reversal_pool = [q for q in adjustment_analysis_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_analysis_fill"]
    income_received_in_advance_analysis_reversal_pool = [q for q in adjustment_analysis_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_analysis_fill"]
    accrued_income_carrythrough_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_carrythrough_fill"]
    accrued_expense_carrythrough_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_carrythrough_fill"]
    prepaid_expense_carrythrough_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_carrythrough_fill"]
    income_received_in_advance_carrythrough_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_carrythrough_fill"]
    accrued_income_post_adjustment_tb_reversal_pool = [q for q in adjustment_trial_balance_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_post_adjustment_tb_fill"]
    accrued_expense_post_adjustment_tb_reversal_pool = [q for q in adjustment_trial_balance_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_post_adjustment_tb_fill"]
    prepaid_expense_post_adjustment_tb_reversal_pool = [q for q in adjustment_trial_balance_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_post_adjustment_tb_fill"]
    income_received_in_advance_post_adjustment_tb_reversal_pool = [q for q in adjustment_trial_balance_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_post_adjustment_tb_fill"]
    accrued_income_mini_project_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_income_reversal_mini_project"]
    accrued_expense_mini_project_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "accrued_expense_reversal_mini_project"]
    prepaid_expense_mini_project_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "prepaid_expense_reversal_mini_project"]
    income_received_in_advance_mini_project_pool = [q for q in adjustment_final_accounts_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "income_received_in_advance_reversal_mini_project"]
    accrued_income_reversal_linked_pool = accrued_income_reversal_pool + accrued_income_reversal_journal_pool + accrued_income_analysis_reversal_pool + accrued_income_carrythrough_pool + accrued_income_post_adjustment_tb_reversal_pool + accrued_income_mini_project_pool
    accrued_expense_reversal_linked_pool = accrued_expense_reversal_pool + accrued_expense_reversal_journal_pool + accrued_expense_analysis_reversal_pool + accrued_expense_carrythrough_pool + accrued_expense_post_adjustment_tb_reversal_pool + accrued_expense_mini_project_pool
    prepaid_expense_reversal_linked_pool = prepaid_expense_reversal_pool + prepaid_expense_reversal_journal_pool + prepaid_expense_analysis_reversal_pool + prepaid_expense_carrythrough_pool + prepaid_expense_post_adjustment_tb_reversal_pool + prepaid_expense_mini_project_pool
    income_received_in_advance_reversal_linked_pool = income_received_in_advance_reversal_pool + income_received_in_advance_reversal_journal_pool + income_received_in_advance_analysis_reversal_pool + income_received_in_advance_carrythrough_pool + income_received_in_advance_post_adjustment_tb_reversal_pool + income_received_in_advance_mini_project_pool
    depreciation_core_pool = [
        q for q in depreciation_pool
        if str(q.get("question_type") or "").strip().lower() in {"mcq", "calc"}
        or str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "depreciation_core_summary_fill"
    ]
    depreciation_ledger_pool = [q for q in depreciation_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    interest_journal_pool = [q for q in interest_adjustments_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    interest_ledger_pool = [q for q in interest_adjustments_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    trading_stock_journal_pool = [q for q in trading_stock_variances_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    trading_stock_ledger_pool = [q for q in trading_stock_variances_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    error_correction_journal_pool = [q for q in error_corrections_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    error_correction_ledger_pool = [q for q in error_corrections_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    consumable_stores_journal_pool = [q for q in consumable_stores_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    consumable_stores_ledger_pool = [q for q in consumable_stores_pool if str(q.get("question_type") or "").strip().lower() == "ledger"]
    bad_debts_journal_pool = [q for q in bad_debts_pool if str(q.get("question_type") or "").strip().lower() == "journal"]
    adjustment_journal_contributors = [
        ("year_end_adjustments", base_adjustment_journal_pool),
        ("consumable_stores_on_hand", consumable_stores_journal_pool),
        ("interest_adjustments", interest_journal_pool),
        ("trading_stock_variances", trading_stock_journal_pool),
        ("error_corrections_and_reclassification", error_correction_journal_pool),
        ("bad_debts_and_recoveries", bad_debts_journal_pool),
    ]
    ledger_posting_contributors = [
        ("depreciation", depreciation_ledger_pool),
        ("year_end_adjustments", adjustment_ledger_pool),
        ("consumable_stores_on_hand", consumable_stores_ledger_pool),
        ("interest_adjustments", interest_ledger_pool),
        ("trading_stock_variances", trading_stock_ledger_pool),
        ("error_corrections_and_reclassification", error_correction_ledger_pool),
    ]
    adjustment_journal_pool = [q for _, contributor_pool in adjustment_journal_contributors for q in contributor_pool]
    ledger_posting_pool = [q for _, contributor_pool in ledger_posting_contributors for q in contributor_pool]
    asset_register_pool = [q for q in depreciation_pool if str(q.get("question_type") or "").strip().lower() == "asset_register_table"]
    capital_calculation_pool = [
        q for q in closing_pool
        if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"closing_capital", "capital_calculation_integrated_fill"}
    ]
    final_accounts_trading_pool = [q for q in income_stmt_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"trading_account_gross_profit_calc", "trading_account_full_extract_fill"}]
    final_accounts_profit_loss_pool = [q for q in income_stmt_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"profit_and_loss_net_profit_calc", "profit_and_loss_full_extract_fill"}]
    final_accounts_table_pool = [q for q in income_stmt_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"income_statement_fill", "trading_account_full_extract_fill", "profit_and_loss_full_extract_fill"}]
    post_closing_trial_balance_pool = [q for q in trial_balance_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"post_closing_trial_balance_fill", "post_closing_trial_balance_expanded_fill"}]
    post_adjustment_trial_balance_pool = [
        q for q in trial_balance_pool
        if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() in {"post_adjustment_trial_balance_fill", "post_adjustment_trial_balance_worksheet_fill"}
    ]
    integrated_final_accounts_pool = [q for q in income_stmt_pool if str(((q.get("scenario_validation") or {}).get("family") or "")).strip().lower() == "integrated_final_accounts_project"]

    all_pools = {
        "closing_transfers": closing_pool,
        "capital_calculation": capital_calculation_pool,
        "depreciation": depreciation_pool,
        "depreciation_core": depreciation_core_pool,
        "asset_register": asset_register_pool,
        "year_end_adjustments": adjustments_pool,
        "adjustments": adjustments_pool,
        "adjustment_journal": adjustment_journal_pool,
        "adjustment_journals": adjustment_journal_pool,
        "adjustment_analysis": adjustment_analysis_pool,
        "consumable_stores_on_hand": consumable_stores_pool,
        "accrued_income_and_reversals": accrued_income_reversal_linked_pool,
        "accrued_expenses_and_reversals": accrued_expense_reversal_linked_pool,
        "prepaid_expenses_and_reversals": prepaid_expense_reversal_linked_pool,
        "income_received_in_advance_and_reversals": income_received_in_advance_reversal_linked_pool,
        "ledger_posting": ledger_posting_pool,
        "trial_balance": trial_balance_pool,
        "post_adjustment_trial_balance": post_adjustment_trial_balance_pool,
        "post_closing_trial_balance": post_closing_trial_balance_pool,
        "income_statement": income_stmt_pool,
        "final_accounts_trading_account": final_accounts_trading_pool,
        "final_accounts_profit_and_loss": final_accounts_profit_loss_pool,
        "final_accounts_table": final_accounts_table_pool,
        "integrated_final_accounts": integrated_final_accounts_pool,
        "final_accounts_fill": final_accounts_table_pool,
        "final_accounts": income_stmt_pool,
        "post_closing_tb": post_closing_trial_balance_pool,
        "post_adjustment_tb": post_adjustment_trial_balance_pool,
        "bad_debts": bad_debts_pool,
        "bad_debts_and_recoveries": bad_debts_pool,
        "error_corrections_and_reclassification": error_corrections_pool,
        "interest_adjustments": interest_adjustments_pool,
        "trading_stock_variances": trading_stock_variances_pool,
        "reversals": accrued_income_reversal_linked_pool + accrued_expense_reversal_linked_pool + prepaid_expense_reversal_linked_pool + income_received_in_advance_reversal_linked_pool,
        "mixed": closing_pool + depreciation_pool + adjustments_pool + consumable_stores_pool + error_corrections_pool + interest_adjustments_pool + trial_balance_pool + income_stmt_pool,
    }
    aggregate_rotation_pools = {
        "adjustment_journal": [(name, contributor_pool) for name, contributor_pool in adjustment_journal_contributors if contributor_pool],
        "ledger_posting": [(name, contributor_pool) for name, contributor_pool in ledger_posting_contributors if contributor_pool],
    }

    pool = all_pools.get(resolved_subskill, all_pools["mixed"])
    if not pool:
        pool = all_pools["mixed"]

    out: List[Dict[str, Any]] = []
    used_signatures = set()

    def _select_from_pool(candidate_pool: List[Dict[str, Any]]) -> Dict[str, Any]:
        selected: Optional[Dict[str, Any]] = None
        fallback_selected: Optional[Dict[str, Any]] = None
        for _attempt in range(18):
            try:
                q = r.choice(candidate_pool)
                q_copy = dict(q)
                q_copy["difficulty"] = difficulty
                q_copy["subskill"] = subskill
                _validate_final_accounts_question(question=q_copy, subskill=resolved_subskill)
                signature = _prompt_signature(q_copy)
                if signature in used_signatures:
                    if fallback_selected is None:
                        fallback_selected = q_copy
                    continue
                selected = q_copy
                used_signatures.add(signature)
                break
            except _FinalAccountsScenarioValidationError:
                continue
        if selected is None and fallback_selected is not None:
            selected = fallback_selected
            used_signatures.add(_prompt_signature(fallback_selected))
        if selected is None:
            raise _FinalAccountsScenarioValidationError(f"Could not generate a valid Final Accounts question for subskill '{resolved_subskill}'.")
        return selected

    contributor_cycle = aggregate_rotation_pools.get(resolved_subskill, [])
    if contributor_cycle:
        for index in range(n):
            selected_question: Optional[Dict[str, Any]] = None
            last_error: Optional[_FinalAccountsScenarioValidationError] = None
            for offset in range(len(contributor_cycle)):
                _, contributor_pool = contributor_cycle[(rotation_base + index + offset) % len(contributor_cycle)]
                try:
                    selected_question = _select_from_pool(contributor_pool)
                    break
                except _FinalAccountsScenarioValidationError as exc:
                    last_error = exc
                    continue
            if selected_question is None:
                if last_error is not None:
                    raise last_error
                raise _FinalAccountsScenarioValidationError(f"Could not generate a valid Final Accounts question for subskill '{resolved_subskill}'.")
            out.append(selected_question)
        return out

    for _ in range(n):
        selected = _select_from_pool(pool)
        out.append(selected)

    return out
