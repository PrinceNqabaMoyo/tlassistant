"""Grade 11 Mathematical Literacy: FINANCE (TAXATION AND UIF) — Subskills Package Manifest."""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .uif_calculations import (
    _gen_uif_employee_contribution_below_ceiling,
    _gen_uif_employer_contribution_match,
    _gen_uif_total_monthly_fund_contribution,
    _gen_uif_salary_exceeding_ceiling_deduction,
    _gen_uif_employer_cap_above_ceiling,
    _gen_uif_annual_contribution_calculation,
    _gen_uif_piecewise_graph_interpretation,
    _gen_uif_hourly_wage_weekly_deduction,
    _gen_uif_qualifying_conditions_claims,
)
from .gross_net_deductions import (
    _gen_gross_salary_basic_plus_allowances,
    _gen_pension_fund_percentage_deduction,
    _gen_medical_aid_tiered_contribution,
    _gen_total_deductions_summation,
    _gen_net_salary_calculation,
    _gen_deductions_as_percentage_of_gross,
    _gen_taxable_income_pension_deduction,
    _gen_payslip_missing_value_deduction,
    _gen_overtime_pay_normal_vs_sunday,
)
from .tax_brackets_paye import (
    _gen_tax_bracket_identification,
    _gen_tax_bracket_1_direct_percentage,
    _gen_tax_bracket_2_threshold_excess,
    _gen_tax_bracket_3_threshold_excess,
    _gen_tax_bracket_4_threshold_excess,
    _gen_annual_salary_from_monthly_taxable,
    _gen_tax_threshold_exemption_check,
    _gen_marginal_tax_rate_identification,
    _gen_tax_liability_before_rebates,
)
from .rebates_credits_paye import (
    _gen_primary_rebate_deduction,
    _gen_secondary_rebate_over_65,
    _gen_tertiary_rebate_over_75,
    _gen_annual_net_tax_after_rebates,
    _gen_monthly_paye_deduction,
    _gen_medical_tax_credit_annual,
    _gen_net_paye_after_medical_credits,
    _gen_effective_tax_rate_calculation,
    _gen_bonus_thirteenth_cheque_tax,
)
from .vat_calculations import (
    _gen_vat_exclusive_to_vat_amount,
    _gen_vat_exclusive_to_inclusive,
    _gen_vat_extract_from_inclusive,
    _gen_vat_inclusive_to_exclusive,
    _gen_vat_zero_rated_basic_food_classification,
    _gen_vat_till_slip_multi_item_audit,
    _gen_vat_invoice_discount_then_vat,
    _gen_vat_vendor_input_vs_output,
)
from .payslip_audits_scenarios import (
    _gen_payslip_comprehensive_audit,
    _gen_salary_increase_net_impact,
    _gen_bracket_creep_inflation_impact,
    _gen_salary_package_restructuring,
    _gen_independent_contractor_vs_employee,
    _gen_tax_avoidance_vs_evasion_legal,
    _gen_tax_return_reconciliation_refund,
    _gen_budgeting_net_income_living_expenses,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: UIF Calculations & Caps (1 to 9)
    "gr11_fin_uif_employee_contribution_below_ceiling": _gen_uif_employee_contribution_below_ceiling,
    "gr11_fin_uif_employer_contribution_match": _gen_uif_employer_contribution_match,
    "gr11_fin_uif_total_monthly_fund_contribution": _gen_uif_total_monthly_fund_contribution,
    "gr11_fin_uif_salary_exceeding_ceiling_deduction": _gen_uif_salary_exceeding_ceiling_deduction,
    "gr11_fin_uif_employer_cap_above_ceiling": _gen_uif_employer_cap_above_ceiling,
    "gr11_fin_uif_annual_contribution_calculation": _gen_uif_annual_contribution_calculation,
    "gr11_fin_uif_piecewise_graph_interpretation": _gen_uif_piecewise_graph_interpretation,
    "gr11_fin_uif_hourly_wage_weekly_deduction": _gen_uif_hourly_wage_weekly_deduction,
    "gr11_fin_uif_qualifying_conditions_claims": _gen_uif_qualifying_conditions_claims,

    # Cluster 2: Gross Income, Deductions & Net Salary (10 to 18)
    "gr11_fin_gross_salary_basic_plus_allowances": _gen_gross_salary_basic_plus_allowances,
    "gr11_fin_pension_fund_percentage_deduction": _gen_pension_fund_percentage_deduction,
    "gr11_fin_medical_aid_tiered_contribution": _gen_medical_aid_tiered_contribution,
    "gr11_fin_total_deductions_summation": _gen_total_deductions_summation,
    "gr11_fin_net_salary_calculation": _gen_net_salary_calculation,
    "gr11_fin_deductions_as_percentage_of_gross": _gen_deductions_as_percentage_of_gross,
    "gr11_fin_taxable_income_pension_deduction": _gen_taxable_income_pension_deduction,
    "gr11_fin_payslip_missing_value_deduction": _gen_payslip_missing_value_deduction,
    "gr11_fin_overtime_pay_normal_vs_sunday": _gen_overtime_pay_normal_vs_sunday,

    # Cluster 3: SARS Progressive Income Tax Brackets (19 to 27)
    "gr11_fin_tax_bracket_identification": _gen_tax_bracket_identification,
    "gr11_fin_tax_bracket_1_direct_percentage": _gen_tax_bracket_1_direct_percentage,
    "gr11_fin_tax_bracket_2_threshold_excess": _gen_tax_bracket_2_threshold_excess,
    "gr11_fin_tax_bracket_3_threshold_excess": _gen_tax_bracket_3_threshold_excess,
    "gr11_fin_tax_bracket_4_threshold_excess": _gen_tax_bracket_4_threshold_excess,
    "gr11_fin_annual_salary_from_monthly_taxable": _gen_annual_salary_from_monthly_taxable,
    "gr11_fin_tax_threshold_exemption_check": _gen_tax_threshold_exemption_check,
    "gr11_fin_marginal_tax_rate_identification": _gen_marginal_tax_rate_identification,
    "gr11_fin_tax_liability_before_rebates": _gen_tax_liability_before_rebates,

    # Cluster 4: Tax Rebates, Medical Credits & Net PAYE (28 to 36)
    "gr11_fin_primary_rebate_deduction": _gen_primary_rebate_deduction,
    "gr11_fin_secondary_rebate_over_65": _gen_secondary_rebate_over_65,
    "gr11_fin_tertiary_rebate_over_75": _gen_tertiary_rebate_over_75,
    "gr11_fin_annual_net_tax_after_rebates": _gen_annual_net_tax_after_rebates,
    "gr11_fin_monthly_paye_deduction": _gen_monthly_paye_deduction,
    "gr11_fin_medical_tax_credit_annual": _gen_medical_tax_credit_annual,
    "gr11_fin_net_paye_after_medical_credits": _gen_net_paye_after_medical_credits,
    "gr11_fin_effective_tax_rate_calculation": _gen_effective_tax_rate_calculation,
    "gr11_fin_bonus_thirteenth_cheque_tax": _gen_bonus_thirteenth_cheque_tax,

    # Cluster 5: Value Added Tax (VAT) (37 to 44)
    "gr11_fin_vat_exclusive_to_vat_amount": _gen_vat_exclusive_to_vat_amount,
    "gr11_fin_vat_exclusive_to_inclusive": _gen_vat_exclusive_to_inclusive,
    "gr11_fin_vat_extract_from_inclusive": _gen_vat_extract_from_inclusive,
    "gr11_fin_vat_inclusive_to_exclusive": _gen_vat_inclusive_to_exclusive,
    "gr11_fin_vat_zero_rated_basic_food_classification": _gen_vat_zero_rated_basic_food_classification,
    "gr11_fin_vat_till_slip_multi_item_audit": _gen_vat_till_slip_multi_item_audit,
    "gr11_fin_vat_invoice_discount_then_vat": _gen_vat_invoice_discount_then_vat,
    "gr11_fin_vat_vendor_input_vs_output": _gen_vat_vendor_input_vs_output,

    # Cluster 6: Payslip Audits & Scenarios (45 to 52)
    "gr11_fin_payslip_comprehensive_audit": _gen_payslip_comprehensive_audit,
    "gr11_fin_salary_increase_net_impact": _gen_salary_increase_net_impact,
    "gr11_fin_bracket_creep_inflation_impact": _gen_bracket_creep_inflation_impact,
    "gr11_fin_salary_package_restructuring": _gen_salary_package_restructuring,
    "gr11_fin_independent_contractor_vs_employee": _gen_independent_contractor_vs_employee,
    "gr11_fin_tax_avoidance_vs_evasion_legal": _gen_tax_avoidance_vs_evasion_legal,
    "gr11_fin_tax_return_reconciliation_refund": _gen_tax_return_reconciliation_refund,
    "gr11_fin_budgeting_net_income_living_expenses": _gen_budgeting_net_income_living_expenses,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())
