"""Financial Documents and Tariff Systems Subskills Package (51 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 1 Topic:
1. Municipal accounts, meter readings, rates, refuse, sewage (Subskills 1 to 9)
2. Electricity tariffs, stepped blocks, service charges, prepaid tokens (Subskills 10 to 18)
3. Water tariffs, free basic water, stepped tariffs, restrictions, JoJo tanks (Subskills 19 to 27)
4. Telephone tariffs, contracts, per-second billing, bundles, peak/off-peak (Subskills 28 to 35)
5. Transport tariffs, bus/train clipcards, taxi fares, e-tolls, fuel comparison (Subskills 36 to 44)
6. Till slips and store accounts, change, VAT breakdown, discounts, interest (Subskills 45 to 51)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .municipal_accounts import (
    _gen_fin_doc_muni_account_number_and_easypay_reference,
    _gen_fin_doc_muni_property_valuation_and_rates_formula,
    _gen_fin_doc_muni_electricity_meter_consumption_kwh,
    _gen_fin_doc_muni_water_meter_consumption_kl,
    _gen_fin_doc_muni_daily_average_consumption,
    _gen_fin_doc_muni_balance_carried_forward_reconciliation,
    _gen_fin_doc_muni_overdue_interest_penalty_charge,
    _gen_fin_doc_muni_refuse_removal_and_bin_levy,
    _gen_fin_doc_muni_sewage_sanitation_percentage_of_water,
)
from .electricity_tariffs import (
    _gen_fin_tar_elec_single_block_consumption,
    _gen_fin_tar_elec_two_tier_stepped_calculation,
    _gen_fin_tar_elec_three_tier_stepped_calculation,
    _gen_fin_tar_elec_fixed_service_charge_plus_stepped,
    _gen_fin_tar_elec_cents_to_rands_conversion,
    _gen_fin_tar_elec_prepaid_electricity_token_units,
    _gen_fin_tar_elec_seasonal_summer_vs_winter_tariff,
    _gen_fin_tar_elec_appliance_energy_consumption_cost,
    _gen_fin_tar_elec_average_unit_cost_comparison,
)
from .water_tariffs import (
    _gen_fin_tar_water_free_basic_water_allowance,
    _gen_fin_tar_water_two_tier_stepped_billing,
    _gen_fin_tar_water_three_tier_stepped_billing,
    _gen_fin_tar_water_drought_level_restriction_tariffs,
    _gen_fin_tar_water_convert_litres_to_kilolitres_billing,
    _gen_fin_tar_water_step_rate_table_reading_threshold,
    _gen_fin_tar_water_daily_consumption_per_person,
    _gen_fin_tar_water_dripping_tap_leak_wastage_cost,
    _gen_fin_tar_water_jojo_tank_rainwater_savings,
)
from .telephone_tariffs import (
    _gen_fin_tar_phone_contract_subscription_plus_extras,
    _gen_fin_tar_phone_per_second_billing_call_cost,
    _gen_fin_tar_phone_in_network_vs_cross_network_rate,
    _gen_fin_tar_phone_airtime_balance_deductions,
    _gen_fin_tar_phone_data_bundle_vs_out_of_bundle_cost,
    _gen_fin_tar_phone_sms_bundle_unit_cost_comparison,
    _gen_fin_tar_phone_airtime_depletion_call_duration,
    _gen_fin_tar_phone_peak_vs_off_peak_call_rate,
)
from .transport_tariffs import (
    _gen_fin_tar_trans_zone_distance_single_ticket,
    _gen_fin_tar_trans_single_vs_monthly_ticket_savings,
    _gen_fin_tar_trans_cost_per_trip_on_commuter_pass,
    _gen_fin_tar_trans_weekly_clipcard_vs_daily_return,
    _gen_fin_tar_trans_scholar_student_uniform_discount,
    _gen_fin_tar_trans_minibus_taxi_fare_route_table,
    _gen_fin_tar_trans_e_toll_highway_gantry_charges,
    _gen_fin_tar_trans_fuel_cost_vs_public_transport,
    _gen_fin_tar_trans_luggage_excess_baggage_charge,
)
from .till_slips_store_accounts import (
    _gen_fin_doc_slip_cash_tendered_and_change_calculation,
    _gen_fin_doc_slip_itemised_total_subtotal_audit,
    _gen_fin_doc_slip_vat_inclusive_vs_exempt_breakdown,
    _gen_fin_doc_slip_discount_voucher_or_loyalty_points,
    _gen_fin_doc_store_account_statement_credit_limit,
    _gen_fin_doc_store_account_minimum_monthly_installment,
    _gen_fin_doc_store_account_interest_and_service_fees,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Municipal Accounts (9)
    "fin_doc_muni_account_number_and_easypay_reference": _gen_fin_doc_muni_account_number_and_easypay_reference,
    "fin_doc_muni_property_valuation_and_rates_formula": _gen_fin_doc_muni_property_valuation_and_rates_formula,
    "fin_doc_muni_electricity_meter_consumption_kwh": _gen_fin_doc_muni_electricity_meter_consumption_kwh,
    "fin_doc_muni_water_meter_consumption_kl": _gen_fin_doc_muni_water_meter_consumption_kl,
    "fin_doc_muni_daily_average_consumption": _gen_fin_doc_muni_daily_average_consumption,
    "fin_doc_muni_balance_carried_forward_reconciliation": _gen_fin_doc_muni_balance_carried_forward_reconciliation,
    "fin_doc_muni_overdue_interest_penalty_charge": _gen_fin_doc_muni_overdue_interest_penalty_charge,
    "fin_doc_muni_refuse_removal_and_bin_levy": _gen_fin_doc_muni_refuse_removal_and_bin_levy,
    "fin_doc_muni_sewage_sanitation_percentage_of_water": _gen_fin_doc_muni_sewage_sanitation_percentage_of_water,

    # Cluster 2: Electricity Tariffs (9)
    "fin_tar_elec_single_block_consumption": _gen_fin_tar_elec_single_block_consumption,
    "fin_tar_elec_two_tier_stepped_calculation": _gen_fin_tar_elec_two_tier_stepped_calculation,
    "fin_tar_elec_three_tier_stepped_calculation": _gen_fin_tar_elec_three_tier_stepped_calculation,
    "fin_tar_elec_fixed_service_charge_plus_stepped": _gen_fin_tar_elec_fixed_service_charge_plus_stepped,
    "fin_tar_elec_cents_to_rands_conversion": _gen_fin_tar_elec_cents_to_rands_conversion,
    "fin_tar_elec_prepaid_electricity_token_units": _gen_fin_tar_elec_prepaid_electricity_token_units,
    "fin_tar_elec_seasonal_summer_vs_winter_tariff": _gen_fin_tar_elec_seasonal_summer_vs_winter_tariff,
    "fin_tar_elec_appliance_energy_consumption_cost": _gen_fin_tar_elec_appliance_energy_consumption_cost,
    "fin_tar_elec_average_unit_cost_comparison": _gen_fin_tar_elec_average_unit_cost_comparison,

    # Cluster 3: Water Tariffs (9)
    "fin_tar_water_free_basic_water_allowance": _gen_fin_tar_water_free_basic_water_allowance,
    "fin_tar_water_two_tier_stepped_billing": _gen_fin_tar_water_two_tier_stepped_billing,
    "fin_tar_water_three_tier_stepped_billing": _gen_fin_tar_water_three_tier_stepped_billing,
    "fin_tar_water_drought_level_restriction_tariffs": _gen_fin_tar_water_drought_level_restriction_tariffs,
    "fin_tar_water_convert_litres_to_kilolitres_billing": _gen_fin_tar_water_convert_litres_to_kilolitres_billing,
    "fin_tar_water_step_rate_table_reading_threshold": _gen_fin_tar_water_step_rate_table_reading_threshold,
    "fin_tar_water_daily_consumption_per_person": _gen_fin_tar_water_daily_consumption_per_person,
    "fin_tar_water_dripping_tap_leak_wastage_cost": _gen_fin_tar_water_dripping_tap_leak_wastage_cost,
    "fin_tar_water_jojo_tank_rainwater_savings": _gen_fin_tar_water_jojo_tank_rainwater_savings,

    # Cluster 4: Telephone Tariffs (8)
    "fin_tar_phone_contract_subscription_plus_extras": _gen_fin_tar_phone_contract_subscription_plus_extras,
    "fin_tar_phone_per_second_billing_call_cost": _gen_fin_tar_phone_per_second_billing_call_cost,
    "fin_tar_phone_in_network_vs_cross_network_rate": _gen_fin_tar_phone_in_network_vs_cross_network_rate,
    "fin_tar_phone_airtime_balance_deductions": _gen_fin_tar_phone_airtime_balance_deductions,
    "fin_tar_phone_data_bundle_vs_out_of_bundle_cost": _gen_fin_tar_phone_data_bundle_vs_out_of_bundle_cost,
    "fin_tar_phone_sms_bundle_unit_cost_comparison": _gen_fin_tar_phone_sms_bundle_unit_cost_comparison,
    "fin_tar_phone_airtime_depletion_call_duration": _gen_fin_tar_phone_airtime_depletion_call_duration,
    "fin_tar_phone_peak_vs_off_peak_call_rate": _gen_fin_tar_phone_peak_vs_off_peak_call_rate,

    # Cluster 5: Transport Tariffs (9)
    "fin_tar_trans_zone_distance_single_ticket": _gen_fin_tar_trans_zone_distance_single_ticket,
    "fin_tar_trans_single_vs_monthly_ticket_savings": _gen_fin_tar_trans_single_vs_monthly_ticket_savings,
    "fin_tar_trans_cost_per_trip_on_commuter_pass": _gen_fin_tar_trans_cost_per_trip_on_commuter_pass,
    "fin_tar_trans_weekly_clipcard_vs_daily_return": _gen_fin_tar_trans_weekly_clipcard_vs_daily_return,
    "fin_tar_trans_scholar_student_uniform_discount": _gen_fin_tar_trans_scholar_student_uniform_discount,
    "fin_tar_trans_minibus_taxi_fare_route_table": _gen_fin_tar_trans_minibus_taxi_fare_route_table,
    "fin_tar_trans_e_toll_highway_gantry_charges": _gen_fin_tar_trans_e_toll_highway_gantry_charges,
    "fin_tar_trans_fuel_cost_vs_public_transport": _gen_fin_tar_trans_fuel_cost_vs_public_transport,
    "fin_tar_trans_luggage_excess_baggage_charge": _gen_fin_tar_trans_luggage_excess_baggage_charge,

    # Cluster 6: Till Slips & Store Accounts (7)
    "fin_doc_slip_cash_tendered_and_change_calculation": _gen_fin_doc_slip_cash_tendered_and_change_calculation,
    "fin_doc_slip_itemised_total_subtotal_audit": _gen_fin_doc_slip_itemised_total_subtotal_audit,
    "fin_doc_slip_vat_inclusive_vs_exempt_breakdown": _gen_fin_doc_slip_vat_inclusive_vs_exempt_breakdown,
    "fin_doc_slip_discount_voucher_or_loyalty_points": _gen_fin_doc_slip_discount_voucher_or_loyalty_points,
    "fin_doc_store_account_statement_credit_limit": _gen_fin_doc_store_account_statement_credit_limit,
    "fin_doc_store_account_minimum_monthly_installment": _gen_fin_doc_store_account_minimum_monthly_installment,
    "fin_doc_store_account_interest_and_service_fees": _gen_fin_doc_store_account_interest_and_service_fees,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Financial Documents and Tariff Systems."""
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
