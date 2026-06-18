from __future__ import annotations

import random
from typing import Any, Callable, Dict, List


QuestionBuilder = Callable[..., Dict[str, Any]]


def build_generation_pools_by_subskill(
    *,
    r: random.Random,
    difficulty: str,
    mode_norm: str,
    build_pools_by_subskill: Callable[..., Dict[str, List[Dict[str, Any]]]],
    builders: Dict[str, QuestionBuilder],
) -> Dict[str, List[Dict[str, Any]]]:
    core_and_journal_pools = build_core_and_journal_pools(
        r=r,
        difficulty=difficulty,
        mode_norm=mode_norm,
        builders=builders,
    )
    non_journal_pools = build_non_journal_pools(
        r=r,
        difficulty=difficulty,
        mode_norm=mode_norm,
        builders=builders,
    )
    mixed_pool: List[Dict[str, Any]] = (
        core_and_journal_pools["concepts_pool"]
        + core_and_journal_pools["equation_pool"]
        + non_journal_pools["ledger_pool"]
        + non_journal_pools["trial_balance_pool"]
        + core_and_journal_pools["journals_pool"]
    )
    return build_pools_by_subskill(
        concepts_pool=core_and_journal_pools["concepts_pool"],
        equation_pool=core_and_journal_pools["equation_pool"],
        ledger_pool=non_journal_pools["ledger_pool"],
        general_ledger_pool=non_journal_pools["general_ledger_pool"],
        debtors_ledger_pool=non_journal_pools["debtors_ledger_pool"],
        creditors_ledger_pool=non_journal_pools["creditors_ledger_pool"],
        trial_balance_pool=non_journal_pools["trial_balance_pool"],
        trading_stock_account_pool=non_journal_pools["trading_stock_account_pool"],
        full_accounting_cycle_bookkeeping_pool=non_journal_pools["full_accounting_cycle_bookkeeping_pool"],
        control_accounts_pool=non_journal_pools["control_accounts_pool"],
        control_accounts_reconciliation_pool=non_journal_pools["control_accounts_reconciliation_pool"],
        reconciliation_analysis_pool=non_journal_pools["reconciliation_analysis_pool"],
        journals_pool=core_and_journal_pools["journals_pool"],
        crj_pool=core_and_journal_pools["crj_pool"],
        cpj_pool=core_and_journal_pools["cpj_pool"],
        dj_pool=core_and_journal_pools["dj_pool"],
        daj_pool=core_and_journal_pools["daj_pool"],
        cj_pool=core_and_journal_pools["cj_pool"],
        caj_pool=core_and_journal_pools["caj_pool"],
        pcj_pool=core_and_journal_pools["pcj_pool"],
        gj_pool=core_and_journal_pools["gj_pool"],
        mixed_pool=mixed_pool,
    )


def build_core_and_journal_pools(
    *,
    r: random.Random,
    difficulty: str,
    mode_norm: str,
    builders: Dict[str, QuestionBuilder],
) -> Dict[str, List[Dict[str, Any]]]:
    concepts_pool: List[Dict[str, Any]] = [
        builders["make_unified_concepts_question"](r=r),
    ]
    equation_pool: List[Dict[str, Any]] = [
        builders["make_transaction_analysis_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    crj_pool: List[Dict[str, Any]] = [
        builders["make_crj_single_row_question"](r=r, difficulty=difficulty),
        builders["make_crj_activity5_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_crj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    cpj_pool: List[Dict[str, Any]] = [
        builders["make_cpj_single_row_question"](r=r),
        builders["make_cpj_activity5_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B", "C", "D"]))),
        builders["make_cpj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B", "C", "D"]))),
    ]
    dj_pool: List[Dict[str, Any]] = [
        builders["make_dj_single_row_question"](r=r, difficulty=difficulty),
        builders["make_dj_activity_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_dj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    daj_pool: List[Dict[str, Any]] = [
        builders["make_daj_single_row_question"](r=r, difficulty=difficulty),
        builders["make_daj_activity_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_daj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    cj_pool: List[Dict[str, Any]] = [
        builders["make_cj_single_row_question"](r=r, difficulty=difficulty),
        builders["make_cj_activity_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_cj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    caj_pool: List[Dict[str, Any]] = [
        builders["make_caj_single_row_question"](r=r, difficulty=difficulty),
        builders["make_caj_activity_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_caj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    pcj_pool: List[Dict[str, Any]] = [
        builders["make_pcj_single_row_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_pcj_activity11_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
        builders["make_pcj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
    ]
    gj_pool: List[Dict[str, Any]] = [
        builders["make_gj_single_row_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_gj_activity13_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
        builders["make_gj_exam_style_question"](r=r, difficulty=difficulty, mode=mode_norm, variant_id=str(r.choice(["A", "B"]))),
    ]
    journals_pool: List[Dict[str, Any]] = crj_pool + cpj_pool + dj_pool + daj_pool + cj_pool + caj_pool + pcj_pool + gj_pool
    return {
        "concepts_pool": concepts_pool,
        "equation_pool": equation_pool,
        "crj_pool": crj_pool,
        "cpj_pool": cpj_pool,
        "dj_pool": dj_pool,
        "daj_pool": daj_pool,
        "cj_pool": cj_pool,
        "caj_pool": caj_pool,
        "pcj_pool": pcj_pool,
        "gj_pool": gj_pool,
        "journals_pool": journals_pool,
    }


def build_non_journal_pools(
    *,
    r: random.Random,
    difficulty: str,
    mode_norm: str,
    builders: Dict[str, QuestionBuilder],
) -> Dict[str, List[Dict[str, Any]]]:
    ledger_pool: List[Dict[str, Any]] = [
        builders["make_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_debtors_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_creditors_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    general_ledger_pool: List[Dict[str, Any]] = [
        builders["make_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    debtors_ledger_pool: List[Dict[str, Any]] = [
        builders["make_debtors_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    creditors_ledger_pool: List[Dict[str, Any]] = [
        builders["make_creditors_ledger_posting_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    trial_balance_pool: List[Dict[str, Any]] = [
        builders["make_trial_balance_from_balances_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_trial_balance_partial_completion_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_trial_balance_control_balance_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    diff = str(difficulty or "easy").strip().lower()
    trading_stock_account_pool: List[Dict[str, Any]] = [
        builders["make_trading_stock_prepare_from_journals_question"](r=r, difficulty=difficulty, mode=mode_norm),
        builders["make_trading_stock_fill_missing_details_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    if diff in {"medium", "hard"}:
        trading_stock_account_pool.extend([
            builders["make_trading_stock_prepare_from_casted_journals_question"](r=r, difficulty=difficulty, mode=mode_norm),
            builders["make_trading_stock_prepare_with_returns_percent_question"](r=r, difficulty=difficulty, mode=mode_norm),
            builders["make_trading_stock_prepare_with_discount_calc_question"](r=r, difficulty=difficulty, mode=mode_norm),
            builders["make_trading_stock_section3_analysis_typed"](r=r),
        ])
    if diff == "hard":
        trading_stock_account_pool.extend([
            builders["make_trading_stock_prepare_with_two_returns_percent_question"](r=r, difficulty=difficulty, mode=mode_norm),
            builders["make_trading_stock_markup_trade_discount_typed"](r=r),
            builders["make_trading_stock_activity16_analysis_typed"](r=r),
        ])
    full_accounting_cycle_bookkeeping_pool: List[Dict[str, Any]] = [
        builders["make_full_accounting_cycle_project_question"](r=r, difficulty=difficulty, mode=mode_norm),
    ]
    control_accounts_pool: List[Dict[str, Any]] = [
        builders["make_control_account_study_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="debtors"),
        builders["make_control_account_study_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="creditors"),
    ]
    if diff == "easy":
        control_accounts_pool.extend([
            builders["make_control_accounts_opening_balance_calc"](r=r, difficulty=difficulty, variant="debtors"),
            builders["make_control_accounts_opening_balance_calc"](r=r, difficulty=difficulty, variant="creditors"),
        ])
    if diff in {"medium", "hard"}:
        control_accounts_pool.extend([
            builders["make_control_accounts_analysis_typed"](r=r, difficulty=difficulty, variant="debtors"),
            builders["make_control_accounts_analysis_typed"](r=r, difficulty=difficulty, variant="creditors"),
        ])
    if diff == "hard":
        control_accounts_pool.extend([
            builders["make_control_accounts_internal_control_typed"](r=r, variant="debtors"),
            builders["make_control_accounts_internal_control_typed"](r=r, variant="creditors"),
        ])
    control_accounts_reconciliation_pool: List[Dict[str, Any]] = [
        builders["make_control_accounts_reconciliation_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="debtors"),
        builders["make_control_accounts_reconciliation_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="creditors"),
    ]
    reconciliation_analysis_pool: List[Dict[str, Any]] = [
        builders["make_reconciliation_impact_matrix_question"](r=r, difficulty=difficulty),
        builders["make_reconciliation_impact_matrix_question"](r=r, difficulty=difficulty),
        builders["make_reconciliation_impact_matrix_question"](r=r, difficulty=difficulty),
    ]
    return {
        "ledger_pool": ledger_pool,
        "general_ledger_pool": general_ledger_pool,
        "debtors_ledger_pool": debtors_ledger_pool,
        "creditors_ledger_pool": creditors_ledger_pool,
        "trial_balance_pool": trial_balance_pool,
        "trading_stock_account_pool": trading_stock_account_pool,
        "full_accounting_cycle_bookkeeping_pool": full_accounting_cycle_bookkeeping_pool,
        "control_accounts_pool": control_accounts_pool,
        "control_accounts_reconciliation_pool": control_accounts_reconciliation_pool,
        "reconciliation_analysis_pool": reconciliation_analysis_pool,
    }
