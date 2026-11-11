import json
import re

targets = [
    # Topic: financial documents and tariffs
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/telecoms_tariffs.py", "gen_subskill_17", 17),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/small_business_costing_breakeven.py", "gen_subskill_45", 45),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/budgets_financial_statements.py", "gen_subskill_47", 47),
    # Topic: income tax
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_income_tax/payslip_take_home_pay.py", "gen_subskill_44", 44),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_income_tax/irp5_assessments_refunds.py", "gen_subskill_51", 51),
    # Topic: exchange rates
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_exchange_rates/fees_commissions.py", "gen_subskill_29", 29),
    # Topic: lengths perimeter area volume
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/surface_areas_painting.py", "gen_subskill_21", 21),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/earthworks_materials.py", "gen_subskill_35", 35),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/earthworks_materials.py", "gen_subskill_40", 40),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/packaging_stacking.py", "gen_subskill_46", 46),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/costing_projects.py", "gen_subskill_49", 49),
    # Topic: scale and map work
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_scale_and_map_work/compass_bearings_elevations.py", "gen_subskill_44", 44),
    # Topic: measuring weight BMI
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/child_growth_bmi_percentiles.py", "gen_subskill_09", 9),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/child_growth_bmi_percentiles.py", "gen_subskill_10", 10),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/child_growth_bmi_percentiles.py", "gen_subskill_13", 13),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/height_weight_percentiles.py", "gen_subskill_17", 17),
    # Topic: data handling
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/scatter_plots_correlation.py", "generate_41_interpreting_bivariate_points", 41),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/scatter_plots_correlation.py", "generate_44_estimating_from_line_of_best_fit", 44),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/opposing_arguments_misleading_stats.py", "generate_48_misleading_graphs_truncated_axis", 48),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_data_handling/opposing_arguments_misleading_stats.py", "generate_49_misleading_graphs_inconsistent_intervals", 49),
    # Topic: interest banking inflation
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/loan_optimization_deposits_rates.py", "generate_21_interest_saved_extra_payment", 21),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/loan_optimization_deposits_rates.py", "generate_24_early_settlement_quotations", 24),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/vehicle_finance_balloon.py", "generate_25_vehicle_net_financed_amount", 25),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/stokvels_communal_savings.py", "generate_44_stokvel_bank_fees_and_interest", 44),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/stokvels_communal_savings.py", "generate_45_burial_society_premium_claims", 45),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_interest_banking_inflation/inflation_purchasing_power.py", "generate_49_disinflation_vs_deflation", 49),
    # Topic: probability
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/scale_frequency_complements.py", "generate_08_probability_scale_endpoints", 8),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/independent_dependent_events.py", "generate_11_two_stage_draw_with_replacement", 11),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/contingency_tables.py", "generate_22_driver_demographics_accident_risk", 22),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/tree_diagrams_multistage.py", "generate_25_tree_branch_probabilities", 25),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/tree_diagrams_multistage.py", "generate_29_medical_screening_tree_diagram", 29),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_probability/tree_diagrams_multistage.py", "generate_32_successive_draw_tree_diagram", 32),
    # Topic: conversions and time
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_conversions_and_time/spread_rates_chemicals.py", "generate_10_multi_coat_paint_tin_packaging", 10),
    ("caps-ai-backend/app/utils/mathematical_literacy/gr12_conversions_and_time/travel_timetables_transit.py", "generate_36_feasibility_of_day_trip_excursion", 36),
]

for fpath, fn_name, num in targets:
    try:
        content = open(fpath, "r", encoding="utf-8").read()
    except Exception as e:
        print(f"ERROR reading {fpath}: {e}")
        continue
    fn_idx = content.find(f"def {fn_name}")
    if fn_idx == -1:
        print(f"NOT FOUND: {fn_name} in {fpath}")
        continue
    # find next def or EOF
    next_def = content.find("\ndef ", fn_idx + 4)
    fn_body = content[fn_idx:next_def] if next_def != -1 else content[fn_idx:]
    has_dspec = bool(re.search(r'd_spec\w*\s*=', fn_body))
    passes_dspec = "diagram_spec=" in fn_body or "'diagram_spec':" in fn_body or '"diagram_spec":' in fn_body
    print(f"{fn_name} (in {fpath.split('/')[-1]}): has_dspec={has_dspec}, passes_dspec={passes_dspec}")
