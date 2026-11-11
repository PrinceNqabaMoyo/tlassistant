"""Banking, Interest and Taxation Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 1 Topic:
1. Bank accounts, FICA regulations, cards, overdraft, security (Subskills 1 to 8)
2. Bank statements, debits/credits, running balance, reconciliation (Subskills 9 to 17)
3. Fee schedules, sliding-scale ATM tariffs, tellers, till points, packages (Subskills 18 to 25)
4. Simple interest, fractional year, term duration, hire purchase loans (Subskills 26 to 35)
5. Compound interest, step-by-step tables, inflation, Rule of 72 (Subskills 36 to 44)
6. Value Added Tax (VAT 15%), exempt foodstuffs, UIF, SARS tax brackets (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .bank_accounts import (
    _gen_bank_acc_types_comparison_savings_cheque_fixed,
    _gen_bank_acc_fica_requirements_verification,
    _gen_bank_acc_debit_vs_credit_card_mechanics,
    _gen_bank_acc_overdraft_facility_interest_cost,
    _gen_bank_acc_stop_order_vs_debit_order,
    _gen_bank_acc_notice_deposit_penalty_terms,
    _gen_bank_acc_atms_branch_electronic_comparison,
    _gen_bank_acc_security_fraud_prevention_pin,
)
from .statements_records import (
    _gen_bank_stmt_identify_debits_and_credits,
    _gen_bank_stmt_calculate_missing_running_balance,
    _gen_bank_stmt_reconstruct_opening_balance,
    _gen_bank_stmt_calculate_total_monthly_bank_charges,
    _gen_bank_stmt_bank_charges_ratio_to_closing_balance,
    _gen_bank_stmt_bounced_debit_order_insufficient_funds,
    _gen_bank_stmt_reconcile_statement_with_receipts,
    _gen_bank_stmt_minimum_balance_interest_qualification,
    _gen_bank_stmt_e_wallet_cash_send_fee_tracking,
)
from .fee_schedules import (
    _gen_bank_fee_flat_plus_sliding_scale_atm_withdrawal,
    _gen_bank_fee_branch_teller_cash_deposit_percentage,
    _gen_bank_fee_branch_vs_atm_cost_comparison,
    _gen_bank_fee_tillpoint_supermarket_cashout_savings,
    _gen_bank_fee_bundled_package_vs_pay_as_you_transact,
    _gen_bank_fee_tiered_balance_fee_waiver,
    _gen_bank_fee_sms_notification_monthly_total,
    _gen_bank_fee_forex_currency_conversion_commission,
)
from .simple_interest_loans import (
    _gen_bank_int_simple_interest_investment_future_value,
    _gen_bank_int_simple_interest_months_fractional_year,
    _gen_bank_int_simple_interest_rate_determination,
    _gen_bank_int_simple_interest_term_duration_years,
    _gen_bank_int_hire_purchase_total_repayment_cost,
    _gen_bank_int_hire_purchase_total_interest_amount,
    _gen_bank_int_hire_purchase_cash_vs_credit_difference,
    _gen_bank_int_hire_purchase_effective_interest_rate,
    _gen_bank_int_personal_unsecured_loan_monthly_installment,
    _gen_bank_int_layby_zero_interest_cancellation_penalty,
)
from .compound_investments import (
    _gen_bank_int_compound_annual_growth_formula,
    _gen_bank_int_compound_year_by_year_stepwise_table,
    _gen_bank_int_simple_vs_compound_numeric_comparison,
    _gen_bank_int_compound_interest_earned_subtraction,
    _gen_bank_int_fixed_deposit_tier_rate_selection,
    _gen_bank_int_inflation_purchasing_power_erosion,
    _gen_bank_int_rule_of_72_doubling_time,
    _gen_bank_int_compound_semi_annual_compounding,
    _gen_bank_int_endowment_policy_maturity_lump_sum,
)
from .vat_uif_taxation import (
    _gen_bank_tax_vat_inclusive_calculation_15_percent,
    _gen_bank_tax_vat_exclusive_calculation_15_percent,
    _gen_bank_tax_vat_amount_from_inclusive_or_exclusive,
    _gen_bank_tax_vat_exempt_foodstuffs_till_slip_verification,
    _gen_bank_tax_uif_deduction_employee_and_employer,
    _gen_bank_tax_sars_income_tax_bracket_calculation,
    _gen_bank_tax_sars_primary_secondary_rebate_reduction,
    _gen_bank_tax_sars_medical_scheme_fees_tax_credit,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Bank Accounts & FICA (8)
    "bank_acc_types_comparison_savings_cheque_fixed": _gen_bank_acc_types_comparison_savings_cheque_fixed,
    "bank_acc_fica_requirements_verification": _gen_bank_acc_fica_requirements_verification,
    "bank_acc_debit_vs_credit_card_mechanics": _gen_bank_acc_debit_vs_credit_card_mechanics,
    "bank_acc_overdraft_facility_interest_cost": _gen_bank_acc_overdraft_facility_interest_cost,
    "bank_acc_stop_order_vs_debit_order": _gen_bank_acc_stop_order_vs_debit_order,
    "bank_acc_notice_deposit_penalty_terms": _gen_bank_acc_notice_deposit_penalty_terms,
    "bank_acc_atms_branch_electronic_comparison": _gen_bank_acc_atms_branch_electronic_comparison,
    "bank_acc_security_fraud_prevention_pin": _gen_bank_acc_security_fraud_prevention_pin,

    # Cluster 2: Statements & Records (9)
    "bank_stmt_identify_debits_and_credits": _gen_bank_stmt_identify_debits_and_credits,
    "bank_stmt_calculate_missing_running_balance": _gen_bank_stmt_calculate_missing_running_balance,
    "bank_stmt_reconstruct_opening_balance": _gen_bank_stmt_reconstruct_opening_balance,
    "bank_stmt_calculate_total_monthly_bank_charges": _gen_bank_stmt_calculate_total_monthly_bank_charges,
    "bank_stmt_bank_charges_ratio_to_closing_balance": _gen_bank_stmt_bank_charges_ratio_to_closing_balance,
    "bank_stmt_bounced_debit_order_insufficient_funds": _gen_bank_stmt_bounced_debit_order_insufficient_funds,
    "bank_stmt_reconcile_statement_with_receipts": _gen_bank_stmt_reconcile_statement_with_receipts,
    "bank_stmt_minimum_balance_interest_qualification": _gen_bank_stmt_minimum_balance_interest_qualification,
    "bank_stmt_e_wallet_cash_send_fee_tracking": _gen_bank_stmt_e_wallet_cash_send_fee_tracking,

    # Cluster 3: Fee Schedules & Tariffs (8)
    "bank_fee_flat_plus_sliding_scale_atm_withdrawal": _gen_bank_fee_flat_plus_sliding_scale_atm_withdrawal,
    "bank_fee_branch_teller_cash_deposit_percentage": _gen_bank_fee_branch_teller_cash_deposit_percentage,
    "bank_fee_branch_vs_atm_cost_comparison": _gen_bank_fee_branch_vs_atm_cost_comparison,
    "bank_fee_tillpoint_supermarket_cashout_savings": _gen_bank_fee_tillpoint_supermarket_cashout_savings,
    "bank_fee_bundled_package_vs_pay_as_you_transact": _gen_bank_fee_bundled_package_vs_pay_as_you_transact,
    "bank_fee_tiered_balance_fee_waiver": _gen_bank_fee_tiered_balance_fee_waiver,
    "bank_fee_sms_notification_monthly_total": _gen_bank_fee_sms_notification_monthly_total,
    "bank_fee_forex_currency_conversion_commission": _gen_bank_fee_forex_currency_conversion_commission,

    # Cluster 4: Simple Interest & Loans (10)
    "bank_int_simple_interest_investment_future_value": _gen_bank_int_simple_interest_investment_future_value,
    "bank_int_simple_interest_months_fractional_year": _gen_bank_int_simple_interest_months_fractional_year,
    "bank_int_simple_interest_rate_determination": _gen_bank_int_simple_interest_rate_determination,
    "bank_int_simple_interest_term_duration_years": _gen_bank_int_simple_interest_term_duration_years,
    "bank_int_hire_purchase_total_repayment_cost": _gen_bank_int_hire_purchase_total_repayment_cost,
    "bank_int_hire_purchase_total_interest_amount": _gen_bank_int_hire_purchase_total_interest_amount,
    "bank_int_hire_purchase_cash_vs_credit_difference": _gen_bank_int_hire_purchase_cash_vs_credit_difference,
    "bank_int_hire_purchase_effective_interest_rate": _gen_bank_int_hire_purchase_effective_interest_rate,
    "bank_int_personal_unsecured_loan_monthly_installment": _gen_bank_int_personal_unsecured_loan_monthly_installment,
    "bank_int_layby_zero_interest_cancellation_penalty": _gen_bank_int_layby_zero_interest_cancellation_penalty,

    # Cluster 5: Compound Interest & Investments (9)
    "bank_int_compound_annual_growth_formula": _gen_bank_int_compound_annual_growth_formula,
    "bank_int_compound_year_by_year_stepwise_table": _gen_bank_int_compound_year_by_year_stepwise_table,
    "bank_int_simple_vs_compound_numeric_comparison": _gen_bank_int_simple_vs_compound_numeric_comparison,
    "bank_int_compound_interest_earned_subtraction": _gen_bank_int_compound_interest_earned_subtraction,
    "bank_int_fixed_deposit_tier_rate_selection": _gen_bank_int_fixed_deposit_tier_rate_selection,
    "bank_int_inflation_purchasing_power_erosion": _gen_bank_int_inflation_purchasing_power_erosion,
    "bank_int_rule_of_72_doubling_time": _gen_bank_int_rule_of_72_doubling_time,
    "bank_int_compound_semi_annual_compounding": _gen_bank_int_compound_semi_annual_compounding,
    "bank_int_endowment_policy_maturity_lump_sum": _gen_bank_int_endowment_policy_maturity_lump_sum,

    # Cluster 6: Value Added Tax, UIF & Income Tax (8)
    "bank_tax_vat_inclusive_calculation_15_percent": _gen_bank_tax_vat_inclusive_calculation_15_percent,
    "bank_tax_vat_exclusive_calculation_15_percent": _gen_bank_tax_vat_exclusive_calculation_15_percent,
    "bank_tax_vat_amount_from_inclusive_or_exclusive": _gen_bank_tax_vat_amount_from_inclusive_or_exclusive,
    "bank_tax_vat_exempt_foodstuffs_till_slip_verification": _gen_bank_tax_vat_exempt_foodstuffs_till_slip_verification,
    "bank_tax_uif_deduction_employee_and_employer": _gen_bank_tax_uif_deduction_employee_and_employer,
    "bank_tax_sars_income_tax_bracket_calculation": _gen_bank_tax_sars_income_tax_bracket_calculation,
    "bank_tax_sars_primary_secondary_rebate_reduction": _gen_bank_tax_sars_primary_secondary_rebate_reduction,
    "bank_tax_sars_medical_scheme_fees_tax_credit": _gen_bank_tax_sars_medical_scheme_fees_tax_credit,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Banking, Interest and Taxation."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
