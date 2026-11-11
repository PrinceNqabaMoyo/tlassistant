"""Grade 12 Mathematical Literacy — Finance (Interest, Banking, Inflation) Subskill Modules.
Subskills 01–52 dispatch registry and metadata.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict

from .loans_fundamentals_factors import (
    generate_01_deposit_and_net_loan,
    generate_02_monthly_interest_rate,
    generate_03_first_month_interest_charge,
    generate_04_reading_repayment_factor,
    generate_05_calculating_monthly_repayment_formula,
    generate_06_real_cost_of_loan,
    generate_07_total_interest_paid,
    generate_08_comparing_15_vs_20_year_terms,
)
from .amortization_table_modeling import (
    generate_09_closing_balance_carryover,
    generate_10_table_monthly_interest_calc,
    generate_11_balance_with_interest,
    generate_12_end_of_month_closing_balance,
    generate_13_final_month_adjustment_payment,
    generate_14_non_linear_loan_balance_curve,
    generate_15_principal_reduction_ratio,
    generate_16_total_property_acquisition_cost,
)
from .loan_optimization_deposits_rates import (
    generate_17_increasing_deposit_savings,
    generate_18_rate_hike_monthly_impact,
    generate_19_rate_cut_total_savings,
    generate_20_extra_monthly_payment_term_reduction,
    generate_21_interest_saved_extra_payment,
    generate_22_fixed_vs_variable_rate_risk,
    generate_23_prime_lending_rate_adjustments,
    generate_24_early_settlement_quotations,
)
from .vehicle_finance_balloon import (
    generate_25_vehicle_net_financed_amount,
    generate_26_calculating_balloon_payment_rands,
    generate_27_vehicle_monthly_instalment_balloon,
    generate_28_total_cost_vehicle_finance,
    generate_29_refinancing_balloon_payment,
    generate_30_comprehensive_vehicle_budget,
    generate_31_vehicle_depreciation_negative_equity,
    generate_32_comparing_cash_vs_instalment_finance,
)
from .investments_retirement_annuities import (
    generate_33_retirement_annuity_table_row,
    generate_34_compounding_accelerating_growth,
    generate_35_contributions_vs_accumulated_capital,
    generate_36_compound_formula_monthly_compounding,
    generate_37_comparing_simple_vs_compound,
    generate_38_retirement_annuity_tax_deduction,
    generate_39_fixed_deposit_tiered_rates,
    generate_40_delaying_savings_opportunity_cost,
)
from .stokvels_communal_savings import (
    generate_41_stokvel_pool_fund,
    generate_42_rotational_payout_schedule,
    generate_43_bulk_grocery_discount_savings,
    generate_44_stokvel_bank_fees_and_interest,
    generate_45_burial_society_premium_claims,
    generate_46_stokvel_yield_vs_individual_retail,
)
from .inflation_purchasing_power import (
    generate_47_annual_commodity_inflation_rate,
    generate_48_multi_year_compounded_inflation,
    generate_49_disinflation_vs_deflation,
    generate_50_household_personal_inflation_rate,
    generate_51_salary_negotiation_real_wage_growth,
    generate_52_required_salary_increase_percentage,
)

SUBSKILL_LIST: list[tuple[str, str, Callable[[random.Random], Dict[str, Any]]]] = [
    ("01_deposit_and_net_loan", "Deposit And Net Loan Principal", generate_01_deposit_and_net_loan),
    ("02_monthly_interest_rate", "Monthly Interest Rate Conversion", generate_02_monthly_interest_rate),
    ("03_first_month_interest_charge", "First Month Loan Interest Charge", generate_03_first_month_interest_charge),
    ("04_reading_repayment_factor", "Reading Monthly Repayment Factor", generate_04_reading_repayment_factor),
    ("05_calculating_monthly_repayment_formula", "Calculating Monthly Repayment Formula", generate_05_calculating_monthly_repayment_formula),
    ("06_real_cost_of_loan", "Real Cost Of Loan Calculation", generate_06_real_cost_of_loan),
    ("07_total_interest_paid", "Total Interest Paid On Loan", generate_07_total_interest_paid),
    ("08_comparing_15_vs_20_year_terms", "Comparing 15 Vs 20 Year Terms", generate_08_comparing_15_vs_20_year_terms),
    ("09_closing_balance_carryover", "Amortization Table Closing Balance Carryover", generate_09_closing_balance_carryover),
    ("10_table_monthly_interest_calc", "Amortization Table Monthly Interest Calc", generate_10_table_monthly_interest_calc),
    ("11_balance_with_interest", "Amortization Table Balance With Interest", generate_11_balance_with_interest),
    ("12_end_of_month_closing_balance", "End Of Month Closing Balance Calculation", generate_12_end_of_month_closing_balance),
    ("13_final_month_adjustment_payment", "Final Month Adjustment Payment Calculation", generate_13_final_month_adjustment_payment),
    ("14_non_linear_loan_balance_curve", "Non-Linear Loan Balance Curve Analysis", generate_14_non_linear_loan_balance_curve),
    ("15_principal_reduction_ratio", "Principal Reduction Ratio Calculation", generate_15_principal_reduction_ratio),
    ("16_total_property_acquisition_cost", "Total Property Acquisition Cost Summary", generate_16_total_property_acquisition_cost),
    ("17_increasing_deposit_savings", "Increasing Deposit Savings Impact", generate_17_increasing_deposit_savings),
    ("18_rate_hike_monthly_impact", "Interest Rate Hike Monthly Impact", generate_18_rate_hike_monthly_impact),
    ("19_rate_cut_total_savings", "Interest Rate Cut Total Savings", generate_19_rate_cut_total_savings),
    ("20_extra_monthly_payment_term_reduction", "Extra Monthly Payment Term Reduction", generate_20_extra_monthly_payment_term_reduction),
    ("21_interest_saved_extra_payment", "Interest Saved Extra Payment Calculation", generate_21_interest_saved_extra_payment),
    ("22_fixed_vs_variable_rate_risk", "Fixed Vs Variable Rate Risk Profile", generate_22_fixed_vs_variable_rate_risk),
    ("23_prime_lending_rate_adjustments", "Prime Lending Rate Adjustments", generate_23_prime_lending_rate_adjustments),
    ("24_early_settlement_quotations", "Early Settlement Quotations Calculation", generate_24_early_settlement_quotations),
    ("25_vehicle_net_financed_amount", "Vehicle Net Financed Amount", generate_25_vehicle_net_financed_amount),
    ("26_calculating_balloon_payment_rands", "Calculating Balloon Payment In Rands", generate_26_calculating_balloon_payment_rands),
    ("27_vehicle_monthly_instalment_balloon", "Vehicle Monthly Instalment With Balloon", generate_27_vehicle_monthly_instalment_balloon),
    ("28_total_cost_vehicle_finance", "Total Cost Of Vehicle Finance", generate_28_total_cost_vehicle_finance),
    ("29_refinancing_balloon_payment", "Refinancing Balloon Payment Extra Interest", generate_29_refinancing_balloon_payment),
    ("30_comprehensive_vehicle_budget", "Comprehensive Vehicle Monthly Budget", generate_30_comprehensive_vehicle_budget),
    ("31_vehicle_depreciation_negative_equity", "Vehicle Depreciation Negative Equity Risk", generate_31_vehicle_depreciation_negative_equity),
    ("32_comparing_cash_vs_instalment_finance", "Comparing Cash Vs Instalment Finance", generate_32_comparing_cash_vs_instalment_finance),
    ("33_retirement_annuity_table_row", "Retirement Annuity Table Row Calculation", generate_33_retirement_annuity_table_row),
    ("34_compounding_accelerating_growth", "Compounding Accelerating Growth Analysis", generate_34_compounding_accelerating_growth),
    ("35_contributions_vs_accumulated_capital", "Contributions Vs Accumulated Capital", generate_35_contributions_vs_accumulated_capital),
    ("36_compound_formula_monthly_compounding", "Compound Formula Monthly Compounding", generate_36_compound_formula_monthly_compounding),
    ("37_comparing_simple_vs_compound", "Comparing Simple Vs Compound Interest", generate_37_comparing_simple_vs_compound),
    ("38_retirement_annuity_tax_deduction", "Retirement Annuity Section 11F Tax Deduction", generate_38_retirement_annuity_tax_deduction),
    ("39_fixed_deposit_tiered_rates", "Fixed Deposit Tiered Interest Rates", generate_39_fixed_deposit_tiered_rates),
    ("40_delaying_savings_opportunity_cost", "Delaying Savings Opportunity Cost", generate_40_delaying_savings_opportunity_cost),
    ("41_stokvel_pool_fund", "Stokvel Monthly And Annual Pool Fund", generate_41_stokvel_pool_fund),
    ("42_rotational_payout_schedule", "Rotational Payout Schedule Analysis", generate_42_rotational_payout_schedule),
    ("43_bulk_grocery_discount_savings", "Bulk Grocery Discount Savings Stokvel", generate_43_bulk_grocery_discount_savings),
    ("44_stokvel_bank_fees_and_interest", "Stokvel Bank Account Fees And Interest", generate_44_stokvel_bank_fees_and_interest),
    ("45_burial_society_premium_claims", "Burial Society Premium Claims Allocation", generate_45_burial_society_premium_claims),
    ("46_stokvel_yield_vs_individual_retail", "Stokvel Yield Vs Individual Retail Account", generate_46_stokvel_yield_vs_individual_retail),
    ("47_annual_commodity_inflation_rate", "Annual Commodity Inflation Rate Calculation", generate_47_annual_commodity_inflation_rate),
    ("48_multi_year_compounded_inflation", "Multi-Year Compounded Inflation Projection", generate_48_multi_year_compounded_inflation),
    ("49_disinflation_vs_deflation", "Disinflation Vs True Deflation Analysis", generate_49_disinflation_vs_deflation),
    ("50_household_personal_inflation_rate", "Household Personal Inflation Rate Calculation", generate_50_household_personal_inflation_rate),
    ("51_salary_negotiation_real_wage_growth", "Salary Negotiation Real Wage Growth", generate_51_salary_negotiation_real_wage_growth),
    ("52_required_salary_increase_percentage", "Required Salary Increase Percentage", generate_52_required_salary_increase_percentage),
]

SUBSKILL_DISPATCH: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
SUBSKILL_METADATA: Dict[str, Dict[str, str]] = {}

for idx, (subskill_key, name, fn) in enumerate(SUBSKILL_LIST, start=1):
    num_str = f"{idx:02d}"
    SUBSKILL_DISPATCH[subskill_key] = fn
    SUBSKILL_DISPATCH[num_str] = fn
    SUBSKILL_DISPATCH[str(idx)] = fn
    SUBSKILL_DISPATCH[f"gr12_fin_{num_str}"] = fn

    SUBSKILL_METADATA[subskill_key] = {
        "index": num_str,
        "name": name,
        "topic": "grade12_mathlit_interest_banking_inflation",
        "key": f"gr12_fin_{num_str}",
    }


def generate_subskill(subskill: str | int, r: random.Random) -> Dict[str, Any]:
    """Generate a question for the requested subskill."""
    key = str(subskill).strip()
    fn = SUBSKILL_DISPATCH.get(key)
    if fn is None:
        # Fallback to random subskill
        fn = r.choice(list(SUBSKILL_DISPATCH.values()))
    return fn(r)
