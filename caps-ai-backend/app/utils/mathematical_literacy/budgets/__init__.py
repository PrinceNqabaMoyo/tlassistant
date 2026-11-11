"""Personal Income, Expenditure and Budgets topic generator package.

Contains 52 distinct subskill archetypes covering:
- Cluster 1: Personal Income Streams, Calculations & Classification (10 subskills)
- Cluster 2: Expenditure Classification, Needs vs Wants & Prioritisation (9 subskills)
- Cluster 3: Personal & Household Monthly Budgets (10 subskills)
- Cluster 4: Event, Project & Travel Budgeting (8 subskills)
- Cluster 5: Income & Expenditure Statements & Variance Analysis (8 subskills)
- Cluster 6: Small Business, Agricultural & Poultry Enterprise Budgets (7 subskills)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .income_calculations import (
    _gen_budg_inc_fixed_var_occ_classification,
    _gen_budg_inc_salary_vs_wage_calculation,
    _gen_budg_inc_hourly_overtime_pay,
    _gen_budg_inc_sales_commission_tiered,
    _gen_budg_inc_restaurant_waiter_tips,
    _gen_budg_inc_piecework_casual_earnings,
    _gen_budg_inc_rental_income_and_levies,
    _gen_budg_inc_state_grants_combination,
    _gen_budg_inc_annual_bonus_13th_cheque,
    _gen_budg_inc_multiple_income_streams_total,
)
from .expenditure_priorities import (
    _gen_budg_exp_fixed_var_occ_classification,
    _gen_budg_exp_high_vs_low_priority,
    _gen_budg_exp_percentage_allocation_split,
    _gen_budg_exp_variable_expenses_subtotal,
    _gen_budg_exp_fixed_expenses_ratio,
    _gen_budg_exp_cost_cutting_deficit_reduction,
    _gen_budg_exp_food_grocery_weekly_to_monthly,
    _gen_budg_exp_public_transport_commuter_cost,
    _gen_budg_exp_utility_prepaid_electricity_budget,
)
from .household_budgets import (
    _gen_budg_hh_monthly_tabular_total_income,
    _gen_budg_hh_monthly_tabular_total_expenses,
    _gen_budg_hh_monthly_surplus_deficit_verdict,
    _gen_budg_hh_balanced_budget_savings_allocation,
    _gen_budg_hh_expense_fraction_of_income,
    _gen_budg_hh_annual_inflation_adjustment,
    _gen_budg_hh_income_drop_rebalancing,
    _gen_budg_hh_emergency_unforeseen_expense,
    _gen_budg_hh_two_earner_shared_contributions,
    _gen_budg_hh_zero_based_budgeting,
)
from .events_projects import (
    _gen_budg_event_birthday_party_catering,
    _gen_budg_event_ticket_cover_charge_break_even,
    _gen_budg_event_attendance_sensitivity_surplus,
    _gen_budg_proj_travel_bus_trip_comparison,
    _gen_budg_proj_holiday_drakensberg_hike,
    _gen_budg_proj_matric_dance_total_cost,
    _gen_budg_proj_home_improvement_painting,
    _gen_budg_proj_school_sports_tour_fundraiser,
)
from .statements_variance import (
    _gen_budg_stmt_actual_vs_budgeted_variance,
    _gen_budg_stmt_running_balance_ledger,
    _gen_budg_stmt_reconciliation_discrepancy,
    _gen_budg_stmt_monthly_cash_flow_statement,
    _gen_budg_stmt_bank_charges_fee_schedule,
    _gen_budg_stmt_interest_earned_on_savings,
    _gen_budg_stmt_vat_inclusive_adjustment,
    _gen_budg_stmt_unexpected_medical_impact,
)
from .agri_business_budgets import (
    _gen_budg_agri_tomato_farming_enterprise,
    _gen_budg_agri_poultry_broiler_batch_budget,
    _gen_budg_agri_layer_chicken_egg_cash_flow,
    _gen_budg_agri_feed_cost_per_bird_margin,
    _gen_budg_agri_spaza_produce_stall_break_even,
    _gen_budg_agri_livestock_goat_herd_budget,
    _gen_budg_agri_crop_irrigation_cost_comparison,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Personal Income Streams, Calculations & Classification (10)
    "budg_inc_fixed_var_occ_classification": _gen_budg_inc_fixed_var_occ_classification,
    "budg_inc_salary_vs_wage_calculation": _gen_budg_inc_salary_vs_wage_calculation,
    "budg_inc_hourly_overtime_pay": _gen_budg_inc_hourly_overtime_pay,
    "budg_inc_sales_commission_tiered": _gen_budg_inc_sales_commission_tiered,
    "budg_inc_restaurant_waiter_tips": _gen_budg_inc_restaurant_waiter_tips,
    "budg_inc_piecework_casual_earnings": _gen_budg_inc_piecework_casual_earnings,
    "budg_inc_rental_income_and_levies": _gen_budg_inc_rental_income_and_levies,
    "budg_inc_state_grants_combination": _gen_budg_inc_state_grants_combination,
    "budg_inc_annual_bonus_13th_cheque": _gen_budg_inc_annual_bonus_13th_cheque,
    "budg_inc_multiple_income_streams_total": _gen_budg_inc_multiple_income_streams_total,

    # Cluster 2: Expenditure Classification, Needs vs Wants & Prioritisation (9)
    "budg_exp_fixed_var_occ_classification": _gen_budg_exp_fixed_var_occ_classification,
    "budg_exp_high_vs_low_priority": _gen_budg_exp_high_vs_low_priority,
    "budg_exp_percentage_allocation_split": _gen_budg_exp_percentage_allocation_split,
    "budg_exp_variable_expenses_subtotal": _gen_budg_exp_variable_expenses_subtotal,
    "budg_exp_fixed_expenses_ratio": _gen_budg_exp_fixed_expenses_ratio,
    "budg_exp_cost_cutting_deficit_reduction": _gen_budg_exp_cost_cutting_deficit_reduction,
    "budg_exp_food_grocery_weekly_to_monthly": _gen_budg_exp_food_grocery_weekly_to_monthly,
    "budg_exp_public_transport_commuter_cost": _gen_budg_exp_public_transport_commuter_cost,
    "budg_exp_utility_prepaid_electricity_budget": _gen_budg_exp_utility_prepaid_electricity_budget,

    # Cluster 3: Personal & Household Monthly Budgets (10)
    "budg_hh_monthly_tabular_total_income": _gen_budg_hh_monthly_tabular_total_income,
    "budg_hh_monthly_tabular_total_expenses": _gen_budg_hh_monthly_tabular_total_expenses,
    "budg_hh_monthly_surplus_deficit_verdict": _gen_budg_hh_monthly_surplus_deficit_verdict,
    "budg_hh_balanced_budget_savings_allocation": _gen_budg_hh_balanced_budget_savings_allocation,
    "budg_hh_expense_fraction_of_income": _gen_budg_hh_expense_fraction_of_income,
    "budg_hh_annual_inflation_adjustment": _gen_budg_hh_annual_inflation_adjustment,
    "budg_hh_income_drop_rebalancing": _gen_budg_hh_income_drop_rebalancing,
    "budg_hh_emergency_unforeseen_expense": _gen_budg_hh_emergency_unforeseen_expense,
    "budg_hh_two_earner_shared_contributions": _gen_budg_hh_two_earner_shared_contributions,
    "budg_hh_zero_based_budgeting": _gen_budg_hh_zero_based_budgeting,

    # Cluster 4: Event, Project & Travel Budgeting (8)
    "budg_event_birthday_party_catering": _gen_budg_event_birthday_party_catering,
    "budg_event_ticket_cover_charge_break_even": _gen_budg_event_ticket_cover_charge_break_even,
    "budg_event_attendance_sensitivity_surplus": _gen_budg_event_attendance_sensitivity_surplus,
    "budg_proj_travel_bus_trip_comparison": _gen_budg_proj_travel_bus_trip_comparison,
    "budg_proj_holiday_drakensberg_hike": _gen_budg_proj_holiday_drakensberg_hike,
    "budg_proj_matric_dance_total_cost": _gen_budg_proj_matric_dance_total_cost,
    "budg_proj_home_improvement_painting": _gen_budg_proj_home_improvement_painting,
    "budg_proj_school_sports_tour_fundraiser": _gen_budg_proj_school_sports_tour_fundraiser,

    # Cluster 5: Income & Expenditure Statements & Variance Analysis (8)
    "budg_stmt_actual_vs_budgeted_variance": _gen_budg_stmt_actual_vs_budgeted_variance,
    "budg_stmt_running_balance_ledger": _gen_budg_stmt_running_balance_ledger,
    "budg_stmt_reconciliation_discrepancy": _gen_budg_stmt_reconciliation_discrepancy,
    "budg_stmt_monthly_cash_flow_statement": _gen_budg_stmt_monthly_cash_flow_statement,
    "budg_stmt_bank_charges_fee_schedule": _gen_budg_stmt_bank_charges_fee_schedule,
    "budg_stmt_interest_earned_on_savings": _gen_budg_stmt_interest_earned_on_savings,
    "budg_stmt_vat_inclusive_adjustment": _gen_budg_stmt_vat_inclusive_adjustment,
    "budg_stmt_unexpected_medical_impact": _gen_budg_stmt_unexpected_medical_impact,

    # Cluster 6: Small Business, Agricultural & Poultry Enterprise Budgets (7)
    "budg_agri_tomato_farming_enterprise": _gen_budg_agri_tomato_farming_enterprise,
    "budg_agri_poultry_broiler_batch_budget": _gen_budg_agri_poultry_broiler_batch_budget,
    "budg_agri_layer_chicken_egg_cash_flow": _gen_budg_agri_layer_chicken_egg_cash_flow,
    "budg_agri_feed_cost_per_bird_margin": _gen_budg_agri_feed_cost_per_bird_margin,
    "budg_agri_spaza_produce_stall_break_even": _gen_budg_agri_spaza_produce_stall_break_even,
    "budg_agri_livestock_goat_herd_budget": _gen_budg_agri_livestock_goat_herd_budget,
    "budg_agri_crop_irrigation_cost_comparison": _gen_budg_agri_crop_irrigation_cost_comparison,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())

def generate(
    seed: Optional[int] = None,
    count: int = 1,
    subskill: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Personal Income, Expenditure and Budgets."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    target_subskills = [subskill] if subskill and subskill in DISPATCH_TABLE else SUBSKILLS

    for i in range(count):
        chosen_subskill = target_subskills[i % len(target_subskills)] if subskill is None else subskill
        fn = DISPATCH_TABLE[chosen_subskill]
        # Create an independent seeded sub-generator for each question
        q_seed = r.randint(1, 10_000_000)
        q_rng = random.Random(q_seed)
        q = fn(q_rng)
        questions.append(q)

    return questions
