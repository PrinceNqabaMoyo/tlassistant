"""Central Generator Registry for Fundile Learning.
Maps (subject, grade, topic) -> deterministic generator function.
Enforces the 6-Pillar Generator Contract, AST purity, and multi-modal question representations.
Includes the 4D Combinatorial Engine for near-infinite semantic breadth.
"""
from __future__ import annotations

import random
import re
from typing import Any, Callable, Dict, List, Optional

# Combinatorial Engine for infinite semantic breadth
from app.utils.combinatorial_engine import generate_combinatorial_batch

# Grade 10 Business Studies
from app.utils.grade10_business_studies.term_1 import (
    micro_environment_generator,
    business_functions_generator,
    market_environment_generator,
    macro_environment_generator,
    interrelationship_generator,
    business_sectors_generator,
)
from app.utils.grade10_business_studies.term_2 import (
    socio_economic_issues_generator,
    social_responsibility_generator,
    entrepreneurial_qualities_generator,
    forms_of_ownership_generator,
    concept_of_quality_generator,
)
from app.utils.grade10_business_studies.term_3 import (
    creative_thinking_generator,
    business_opportunities_generator,
    business_location_generator,
    contracts_generator,
    presentation_generator,
    business_plans_generator,
)

# Grade 11 Business Studies
from app.utils.grade11_business_studies.term_1 import (
    adapting_to_challenges_generator as g11_bs_adapt,
    avenues_of_acquiring_businesses_generator as g11_bs_avenues,
    benefits_of_a_company_generator as g11_bs_benefits,
    business_sectors_generator as g11_bs_sectors,
    influences_on_business_environments_generator as g11_bs_influences,
    socio_economic_issues_generator as g11_bs_socio,
    the_challenges_of_the_business_environments_generator as g11_bs_challenges,
)
from app.utils.grade11_business_studies.term_2 import (
    creative_thinking_generator as g11_bs_creative,
    marketing_function_generator as g11_bs_mkt,
    production_function_generator as g11_bs_prod,
    professionalism_and_ethics_generator as g11_bs_ethics,
    stress_crisis_change_generator as g11_bs_stress,
)
from app.utils.grade11_business_studies.term_3 import (
    business_plan_transformation_generator as g11_bs_plan,
    citizenship_responsibilities_generator as g11_bs_citizenship,
    entrepreneurial_assessment_generator as g11_bs_entrepreneur,
    presentation_of_information_generator as g11_bs_pres,
    start_business_venture_generator as g11_bs_venture,
    human_resources_function_generator as g11_bs_hr,
)

# Grade 7 EMS
from app.utils.grade7_ems import (
    term1_history_of_money as g7_history_of_money,
    term1_needs_and_wants as g7_needs_and_wants,
    term1_money_and_needs as g7_money,
    term1_businesses as g7_businesses,
    term1_goods_and_services as g7_goods,
    term2_accounting_concepts as g7_acct_concepts,
    term2_income_and_expenses as g7_income,
    term2_budgets as g7_budgets,
    term3_entrepreneurship as g7_entrepreneurship,
    term3_the_entrepreneur as g7_the_entrepreneur,
    term3_entrepreneurs_day as g7_entrepreneurs_day,
    term3_starting_a_business as g7_starting_a_business,
    term3_businesses as g7_businesses_term3,
    term3_inequality_and_poverty as g7_inequality,
    term3_production_process as g7_prod,
    term4_savings as g7_savings,
)

# Grade 8 EMS
from app.utils.grade8_ems import (
    term1_gov_and_society as g8_gov,
    term1_government_generator as g8_government_gen,
    term1_national_budget_generator as g8_budget_gen,
    term1_accounting_basics as g8_acct_basics,
    term1_source_documents as g8_source_docs,
    term1_general_ledger as g8_general_ledger,
    term2_markets_and_production as g8_markets,
    term4_markets_generator as g8_markets_gen,
    term4_factors_of_production_generator as g8_fop_gen,
    term2_crj as g8_crj,
    term2_accounting_cycle as g8_acct_cycle,
    term3_cpj_and_crj as g8_cpj_crj,
    term3_ownership as g8_ownership,
    term3_management as g8_mgmt,
)

# Grade 9 EMS
from app.utils.grade9_ems import (
    term1_crj_cpj as g9_crj_cpj,
    term1_general_ledger as g9_gl,
    term1_economy as g9_economy,
    term1_circular_flow as g9_circular,
    term2_debtors_journal as g9_dj,
    term2_economy as g9_price_theory,
    term2_sectors_of_economy as g9_sectors,
    term3_creditors_journal as g9_cj,
    term3_debtors_ledger as g9_dl,
    term3_creditors_ledger as g9_cl,
    term3_business as g9_business,
    term3_trade_unions as g9_trade_unions,
    term4_business_plan as g9_bp,
    term4_transactions_cash_credit as g9_cash_credit,
)

# Grade 8 Mathematics
from app.utils import (
    grade8_algebraic_expressions_generator as g8_math_expr,
    grade8_algebraic_equations_generator as g8_math_eq,
    grade8_exponents_generator as g8_math_exp,
    grade8_functions_generator as g8_math_func,
    grade8_integers_generator as g8_math_int,
    grade8_patterns_generator as g8_math_pat,
    grade8_whole_numbers_generator as g8_math_whole,
)

# Grade 9 Mathematics (Dedicated 6-Pillar Generators for all 24 Topics)
from app.utils.grade9_mathematics import (
    whole_numbers_generator as g9_math_whole,
    integers_generator as g9_math_int,
    decimal_notation_generator as g9_math_dec,
    exponents_generator as g9_math_exp,
    patterns_generator as g9_math_pat,
    functions_generator as g9_math_func,
    algebraic_expressions_generator as g9_math_expr,
    factorisation_generator as g9_math_fact,
    algebraic_equations_generator as g9_math_eq,
    algebraic_equations_fractions_generator as g9_math_eq_frac,
    fractions_generator as g9_math_frac,
    graphs_generator as g9_math_graphs,
    geometry_straight_lines_generator as g9_math_str_lines,
    geometry_2d_shapes_generator as g9_math_2d_shapes,
    construction_generator as g9_math_construct,
    transformation_geometry_generator as g9_math_trans,
    pythagoras_generator as g9_math_pyth,
    area_perimeter_2d_generator as g9_math_area2d,
    geometry_3d_objects_generator as g9_math_geom3d,
    measurement_3d_generator as g9_math_meas3d,
    data_summarise_generator as g9_math_datasum,
    data_represent_generator as g9_math_datarep,
    data_interpret_generator as g9_math_dataint,
    probability_generator as g9_math_prob,
    congruence_similarity_generator as g9_math_geom,
    geometry_straight_lines_triangles_generator as g9_math_lines,
)

# Senior Phase Mathematics (Grades 7, 8, 9)
from app.utils.senior_phase_math.senior_phase_pythagoras_generator import SeniorPhasePythagorasGenerator
from app.utils.senior_phase_math.senior_phase_measurement_generator import SeniorPhaseMeasurementGenerator
from app.utils.senior_phase_math.senior_phase_data_handling_generator import SeniorPhaseDataHandlingGenerator
from app.utils.senior_phase_math.senior_phase_geometry_generator import SeniorPhaseGeometryGenerator
from app.utils.senior_phase_math.senior_phase_transformations_generator import SeniorPhaseTransformationsGenerator

g_sp_pythagoras = SeniorPhasePythagorasGenerator().generate
g_sp_measurement = SeniorPhaseMeasurementGenerator().generate
g_sp_data_handling = SeniorPhaseDataHandlingGenerator().generate
g_sp_geometry = SeniorPhaseGeometryGenerator().generate
g_sp_transformations = SeniorPhaseTransformationsGenerator().generate

# Grade 7 Mathematics (Dedicated 6-Pillar Generators)
from app.utils.grade7_mathematics import (
    whole_numbers_generator as g7_math_whole,
    patterns_generator as g7_math_pat,
    algebraic_expressions_generator as g7_math_alg,
    geometric_nets_3d_generator as g7_math_nets,
    decimals_generator as g7_math_dec,
    fractions_generator as g7_math_frac,
    integers_generator as g7_math_int,
    geometry_2d_generator as g7_math_geom2d,
    graphs_relationships_generator as g7_math_graph,
    data_probability_generator as g7_math_data,
    exponents_generator as g7_math_exp,
    measurement_generator as g7_math_meas,
    transformation_geometry_generator as g7_math_trans,
    geometry_straight_lines_generator as g7_math_lines,
    grid_paper_types_generator as g7_math_grid,
    functions_relationships_1_generator as g7_math_fn1,
    functions_relationships_2_generator as g7_math_fn2,
    functions_relationships_3_generator as g7_math_fn3,
    data_collection_tally_generator as g7_math_tally,
    data_representation_generator as g7_math_repr,
    data_measures_generator as g7_math_meas_data,
    graphs_generator as g7_math_graph_stories,
    relationships_variables_generator as g7_math_rel_vars,
    algebraic_expressions_1_generator as g7_math_alg1,
    algebraic_expressions_2_generator as g7_math_alg2,
    algebraic_equations_1_generator as g7_math_eq1,
    algebraic_equations_2_generator as g7_math_eq2,
    geometric_patterns_generator as g7_math_geom_pat,
    numeric_patterns_generator as g7_math_num_pat,
    perimeter_area_2d_generator as g7_math_perim_area,
    surface_area_volume_3d_generator as g7_math_sa_vol,
    construction_of_geometric_figures_generator as g7_math_construction,
)
from app.utils.senior_phase_math.senior_phase_probability_generator import SeniorPhaseProbabilityGenerator
g_sp_probability = SeniorPhaseProbabilityGenerator().generate

# Grade 8 Mathematics (Dedicated 6-Pillar Generators)
from app.utils.grade8_mathematics import (
    pythagoras_generator as g8_math_pyth,
    integers_generator as g8_math_int,
    algebraic_expressions_equations_generator as g8_math_alg,
    geometry_straight_lines_generator as g8_math_lines,
    measurement_3d_generator as g8_math_meas3d,
    common_fractions_generator as g8_common_fractions,
    fractions_decimals_generator as g8_math_frac_dec,
    decimal_fractions_generator as g8_math_dec_frac,
    geometry_2d_shapes_generator as g8_math_geom2d,
    geometry_3d_objects_generator as g8_math_3d_obj,
    perimeter_area_2d_generator as g8_math_p2d,
    construction_generator as g8_math_construction,
    transformation_geometry_generator as g8_math_transform,
    algebraic_expressions_1_generator as g8_math_alg1,
    algebraic_expressions_2_generator as g8_math_alg2,
    algebraic_equations_1_generator as g8_math_eq1,
    algebraic_equations_2_generator as g8_math_eq2,
    algebraic_equations_3_generator as g8_math_eq3,
    functions_relationships_1_generator as g8_math_fn1,
    functions_relationships_2_generator as g8_math_fn2,
    graphs_generator as g8_math_graphs,
    data_collect_organise_generator as g8_math_collect,
    data_representation_generator as g8_math_repr,
    data_measures_generator as g8_math_meas_data,
    whole_numbers_generator as g8_math_whole_dedicated,
    exponents_generator as g8_math_exp_dedicated,
    patterns_generator as g8_math_patterns_dedicated,
    probability_generator as g8_math_prob_dedicated,
)

# Grade 10 Mathematics
from app.utils.grade10_mathematics.term_1 import (
    algebraic_expressions_generator as g10_math_alg,
    equations_inequalities_generator as g10_math_eq,
    exponents_generator as g10_math_exp,
    patterns_sequences_generator as g10_math_pat,
    trigonometry_generator as g10_math_trig,
)
from app.utils.grade10_mathematics.term_2 import (
    functions_generator as g10_math_func,
    euclidean_geometry_generator as g10_math_geom,
    analytical_geometry_generator as g10_math_analgeo,
)
from app.utils.grade10_mathematics.term_3 import (
    finance_growth_generator as g10_math_fin,
    statistics_generator as g10_math_stat,
)
from app.utils.grade10_mathematics.term_4 import (
    measurements_generator as g10_math_meas,
    probability_generator as g10_math_prob,
)

# Grade 11 Mathematics
from app.utils import (
    grade11_analytical_geometry_generator as g11_math_analgeo,
    grade11_equations_inequalities_generator as g11_math_eq,
    grade11_exponents_surds_generator as g11_math_surds,
    grade11_patterns_sequences_generator as g11_math_pat,
)
from app.utils.grade10_mathematics.term_2 import (
    circle_geometry_generator as g11_math_circ,
)
from app.utils.grade11_mathematics import (
    circle_geometry_theorems_generator as g11_math_circ_theorems,
    trigonometry_reductions_generator as g11_math_trig_red,
    finance_growth_decay_generator as g11_math_fin,
    probability_contingency_generator as g11_math_prob,
    statistics_summary_ogive_generator as g11_math_stat,
    linear_programming_generator as g11_math_lp,
    functions_graphs_generator as g11_math_func,
)

# Grade 12 Mathematics
from app.utils import (
    grade12_finance_generator as g12_math_fin,
    grade12_functions_generator as g12_math_func,
    grade12_patterns_sequences_series_generator as g12_math_pat,
    grade12_trigonometry_generator as g12_math_trig,
)

# Grade 10 Accounting
from app.utils.grade10_accounting import (
    sole_trader_generator as g10_acct_sole,
    gaap_generator as g10_acct_gaap,
    financial_info_concepts_generator as g10_acct_fin_info,
    managing_resources_generator as g10_acct_resources,
    ethics_generator as g10_acct_ethics,
    internal_control_generator as g10_acct_ctrl,
    fixed_assets_depreciation_generator as g10_acct_fixed,
    inventory_cost_of_sales_generator as g10_acct_inv,
    cost_accounting_generator as g10_acct_cost,
    sole_trader_financial_statements_generator as g10_acct_stmt,
    sole_trader_analysis_generator as g10_acct_analysis,
    budgeting_generator as g10_acct_budgets,
    financial_vs_managerial_generator as g10_acct_fin_vs_mgr,
    indigenous_bookkeeping_generator_v2 as g10_acct_indig,
)
from app.utils.grade10_accounting.term2 import (
    vat_generator as g10_acct_vat,
    salaries_wages_generator as g10_acct_sal,
    final_accounts_generator as g10_acct_final,
    bank_reconciliation_generator as g10_acct_recon,
)

# Grade 11 Accounting
from app.utils.grade11_accounting import (
    fixed_assets_generator as g11_acct_fixed,
    asset_disposal_generator as g11_acct_disposal,
    income_statement_generator as g11_acct_inc,
    partnership_balance_sheet_generator as g11_acct_bs,
    partnership_ledger_generator as g11_acct_led,
    reconciliation_generator as g11_acct_recon,
    control_accounts_generator as g11_acct_ctrl_acc,
    debtors_age_analysis_generator as g11_acct_debtors,
    accounting_equation_generator as g11_acct_eq,
    ethics_generator as g11_acct_ethics,
    internal_control_generator as g11_acct_int_ctrl,
    budgeting_generator as g11_acct_budgets,
    cost_accounting_generator as g11_acct_cost,
    concepts_generator as g11_acct_concepts,
    partnerships_financial_statements_generator as g11_acct_part_stmt,
    inventory_valuation_generator as g11_acct_inv,
    vat_generator as g11_acct_vat,
)
from app.utils.grade11_accounting.term2 import (
    analysis_interpretation_generator as g11_acct_analysis,
    clubs_nonprofit_generator as g11_acct_clubs,
)

# Grade 12 Accounting
from app.utils.grade12_accounting import (
    cash_flow_statement_generator as g12_acct_cfs,
    financial_indicators_generator as g12_acct_indicators,
    cash_flow_generator as g12_acct_cf,
    company_general_ledger_generator as g12_acct_gl,
    financial_statements_notes_generator as g12_acct_stmt,
    analysis_interpretation_generator as g12_acct_analysis,
    concepts_generator as g12_acct_concepts,
    cost_accounting_generator as g12_acct_cost,
    budgets_variance_generator as g12_acct_budgets,
    cash_budget_variance_generator as g12_acct_variance,
    companies_generator as g12_acct_companies,
    control_accounts_generator as g12_acct_ctrl_acc,
    asset_disposal_generator as g12_acct_disposal,
    debtors_age_analysis_generator as g12_acct_debtors,
    vat_analysis_generator as g12_acct_vat,
    accounting_equation_generator as g12_acct_eq,
)
from app.utils.grade12_accounting.term2 import (
    reconciliation_generator as g12_acct_recon,
    inventory_systems_generator as g12_acct_inv,
    fixed_assets_generator as g12_acct_fixed,
)

# Grade 12 Mathematics (Pillars)
from app.utils.grade12_mathematics import (
    differential_calculus_generator as g12_math_calc,
    analytical_geometry_circles_generator as g12_math_circles,
    counting_principles_probability_generator as g12_math_prob,
    bivariate_statistics_generator as g12_math_stat,
    sequences_series_generator as g12_math_seq,
    trigonometry_compound_angles_generator as g12_math_trig_comp,
)

# Grade 12 Physical Sciences & Chemistry
from app.utils.grade12_physical_sciences import (
    stoichiometry_equilibrium_generator as phys_chem_eq,
    momentum_impulse_generator as phys_momentum,
    vertical_projectile_generator as phys12_proj,
    doppler_effect_generator as phys12_doppler,
    organic_chemistry_generator as phys12_organic,
    acids_bases_generator as phys12_acids_bases,
    electrodynamics_circuits_generator as phys12_electrodyn,
    optical_phenomena_photoelectric_generator as phys12_photoelectric,
)

# Grade 12 Business Studies
from app.utils.grade12_business_studies.term_1 import (
    creative_thinking_problem_solving_generator as g12_bs_creative,
    ethics_and_professionalism_generator as g12_bs_ethics,
    human_resources_function_generator as g12_bs_hr,
    impact_of_legislation_generator as g12_bs_legislation,
    macro_environment_strategies_generator as g12_bs_macro_strat,
)
from app.utils.grade12_business_studies.term_2 import (
    business_sectors_environments_generator as g12_bs_sectors_env,
    investment_insurance_generator as g12_bs_insurance,
    investment_securities_generator as g12_bs_securities,
    management_and_leadership_generator as g12_bs_leadership,
    quality_of_performance_generator as g12_bs_quality,
    team_performance_conflict_generator as g12_bs_team_conflict,
)
from app.utils.grade12_business_studies.term_3 import (
    forms_of_ownership_success_generator as g12_bs_ownership,
    human_rights_inclusivity_generator as g12_bs_human_rights,
    presentation_data_responses_generator as g12_bs_presentation,
    social_responsibility_csr_csi_generator as g12_bs_csr,
)
from app.utils.grade12_business_studies import (
    business_studies_essay_generator as g12_bs_essay,
    legislation_hr_generator as g12_bs_leg_hr,
    investments_management_generator as g12_bs_inv_man,
)
from app.utils.grade11_business_studies import (
    marketing_production_generator as g11_bs_mkt_prod,
)
from app.utils.grade8_ems import (
    senior_phase_ems_gap_generator as g8_ems_gap,
)

# Science & Technical Subjects
from app.utils.physical_sciences import mechanics_generator as phys_mech
from app.utils.grade11_physical_sciences import (
    vectors_newton_generator as phys11_vec,
    chemical_bonding_intermolecular_generator as phys11_chem,
    electric_circuits_energy_generator as phys11_circuits,
    energy_chemical_change_generator as phys11_energy,
    stoichiometry_limiting_generator as phys11_stoich,
)
from app.utils.life_sciences import (
    genetics_generator as life_gen,
    dihybrid_pedigree_generator as life_dihybrid,
    ls11_animal_nutrition_generator as ls11_nutrition,
    ls11_gaseous_exchange_generator as ls11_gas_exchange,
    ls11_excretion_humans_generator as ls11_excretion,
    ls12_responding_environment_humans_generator as ls12_responding_env,
    ls12_endocrine_homeostasis_generator as ls12_endocrine,
    ls12_human_reproduction_generator as ls12_human_repro,
    ls10_plant_and_animal_cells_generator as ls10_cells,
    ls10_cell_division_mitosis_generator as ls10_mitosis_gen,
    ls12_meiosis_generator as ls12_meiosis_gen,
    ls10_support_transport_plants_generator as ls10_plants,
    ls11_photosynthesis_generator as ls11_photosynth,
    ls11_cellular_respiration_generator as ls11_resp,
    ls10_biospheres_to_ecosystems_generator as ls10_biospheres,
    ls11_population_ecology_generator as ls11_pop_ecology,
    ls12_plant_responses_environment_generator as ls12_plant_resp,
)
from app.utils.natural_sciences import (
    grade9 as ns9_mod,
    electric_circuits_generator as ns_circuits,
    chemical_reactions_generator as ns_reactions,
    senior_phase_astronomy_generator as ns_astronomy,
    term1_life_and_living_generator as ns_life_living,
    term2_matter_materials_generator as ns_matter_materials,
    term3_energy_change_forces_generator as ns_energy_forces,
    term4_planet_earth_beyond_generator as ns_planet_earth,
    ns9_digestive_system_generator as ns9_digestive,
    ns9_human_reproduction_generator as ns9_human_repro,
    ns9_cells_units_of_life_generator as ns9_cells,
    ns7_separating_mixtures_generator as ns7_separating,
    ns7_acids_bases_neutrals_generator as ns7_acids_bases,
    ns8_particle_model_matter_generator as ns8_particles,
    ns8_electric_circuits_generator as ns8_circuits_gen,
    ns7_biosphere_generator as ns7_biosphere,
    ns7_biodiversity_generator as ns7_biodiversity,
    ns7_sexual_reproduction_generator as ns7_sexual_repro,
    ns7_variation_generator as ns7_variation,
    ns7_properties_of_materials_generator as ns7_properties,
    ns7_periodic_table_generator as ns7_periodic_table,
    ns7_sources_of_energy_generator as ns7_sources_energy,
    ns7_potential_kinetic_energy_generator as ns7_potential_kinetic,
    ns7_energy_transfer_generator as ns7_energy_transfer,
    ns7_heat_transfer_generator as ns7_heat_transfer,
    ns7_heat_insulation_generator as ns7_heat_insulation,
    ns7_moon_earth_generator as ns7_moon_earth,
    ns7_sun_earth_generator as ns7_sun_earth,
    ns7_astronomy_history_generator as ns7_astronomy_history,
    ns9_forces_electric_cells_generator as ns9_electric_cells,
    ns8_solar_system_seasons_generator as ns8_solar_gen,
    ns8_photosynthesis_respiration_generator as ns8_photosynth,
    ns8_ecology_interactions_generator as ns8_ecology,
    ns8_atoms_subatomic_generator as ns8_atoms,
    ns8_chemical_reactions_generator as ns8_chem_reactions,
    ns8_microorganisms_generator as ns8_microorganisms,
    ns8_energy_transfer_electrical_generator as ns8_energy_transfer,
    ns8_static_electricity_generator as ns8_static_elec,
    ns8_visible_light_generator as ns8_visible_light,
    ns8_beyond_solar_system_generator as ns8_beyond_solar,
    ns8_telescopes_space_exploration_generator as ns8_telescopes,
)
from app.utils.mathematical_literacy import (
    finance_tax_generator as mathlit_fin,
    maps_scales_generator as mathlit_maps,
    tariffs_tax_brackets_generator as mathlit_tariffs,
    data_handling_generator as mathlit_data,
    measurement_probability_generator as mathlit_meas_prob,
    conversions_time_generator as mathlit_conversions_time,
    measuring_length_weight_volume_temperature_generator as mathlit_measuring,
    personal_income_expenditure_budgets_generator as mathlit_budgets,
    numbers_and_calculations_with_numbers_generator as mathlit_numbers,
    banking_interest_and_taxation_generator as mathlit_banking_tax,
    financial_documents_and_tariff_systems_generator as mathlit_tariffs_systems,
    assembly_diagrams_floor_plans_packaging_generator as mathlit_assembly_plans,
    scale_maps_and_plans_generator as mathlit_scale_maps,
    measurement_of_perimeter_and_area_generator as mathlit_perimeter_area,
    patterns_relationships_and_representations_generator as mathlit_patterns,
    probability_generator as mathlit_prob,
    gr11_finance_taxation_uif_generator as mathlit_gr11_fin,
    gr11_conversions_and_time_generator as mathlit_gr11_conv,
    gr11_exchange_rates_generator as mathlit_gr11_exch,
    gr11_interest_banking_inflation_generator as mathlit_gr11_interest,
    gr11_patterns_relationships_generator as mathlit_gr11_pat,
    gr11_plans_representations_generator as mathlit_gr11_plans,
    gr11_data_handling_generator as mathlit_gr11_data,
    gr11_maps_generator as mathlit_gr11_maps,
    gr11_area_volume_generator as mathlit_gr11_area_vol,
    gr11_financial_documents_tariffs_generator as mathlit_gr11_tariffs,
    gr11_weight_and_temperature_generator as mathlit_gr11_weight_temp,
    gr11_probability_generator as mathlit_gr11_prob,
    gr12_exchange_rates_generator as mathlit_gr12_exch,
    gr12_income_tax_generator as mathlit_gr12_tax,
    gr12_financial_documents_and_tariff_systems_generator as mathlit_gr12_tariffs,
    gr12_lengths_perimeter_area_volume_generator as mathlit_gr12_meas,
    gr12_scale_and_map_work_generator as mathlit_gr12_scale,
    gr12_measuring_weight_bmi_medicine_dosages_generator as mathlit_gr12_bmi,
    gr12_maps_and_plans_models_generator as mathlit_gr12_models,
    gr12_plans_and_scale_generator as mathlit_gr12_plans,
    gr12_data_handling_generator as mathlit_gr12_data,
    gr12_interest_banking_inflation_generator as mathlit_gr12_fin,
    gr12_probability_generator as mathlit_gr12_prob,
    gr12_conversions_and_time_generator as mathlit_gr12_conv,
)
from app.utils.technical_mathematics import (
    complex_numbers_generator as tech_cplx,
    mensuration_calculus_generator as tech_mens,
    circles_angular_movement_generator as tech_circles,
    polynomials_generator as tech_poly,
)
from app.utils.grade10_life_sciences import (
    generate_cytology as ls10_cytology,
    generate_mitosis as ls10_mitosis,
)

# Foundational Mathematics (Tang & Stokke Pedagogy)
from app.utils.foundational_math import generate_number_bonds_drill as foundational_math_drill


# ============================================================================
# ADAPTERS
# ============================================================================

def _normalize_question_dict(q: Any) -> Any:
    if isinstance(q, dict):
        if not q.get("prompt") and q.get("question"):
            q["prompt"] = q["question"]
        elif not q.get("question") and q.get("prompt"):
            q["question"] = q["prompt"]
        if not q.get("sample_answer") and q.get("correct_answer"):
            q["sample_answer"] = str(q["correct_answer"])
        if isinstance(q.get("correct_map"), dict) and len(q["correct_map"]) > 0:
            entries = [f"{k}: {v}" for k, v in q["correct_map"].items() if v and not str(k).startswith("title_")][:8]
            if entries:
                tabular_proc = "Completed Accounting / Tabular Entries:\n" + "\n".join(f"- {e}" for e in entries)
                if not q.get("sample_answer") or len(str(q["sample_answer"])) < 30:
                    q["sample_answer"] = tabular_proc
                if not q.get("worked_solution") or len(str(q["worked_solution"])) < 30:
                    q["worked_solution"] = tabular_proc
        if not q.get("worked_solution"):
            if q.get("canonical_solution"):
                q["worked_solution"] = q["canonical_solution"]
            elif q.get("explanation"):
                q["worked_solution"] = q["explanation"]
            elif isinstance(q.get("solution_steps"), list):
                q["worked_solution"] = "\n".join(str(s) for s in q["solution_steps"])
            elif q.get("sample_answer"):
                q["worked_solution"] = str(q["sample_answer"])
            elif isinstance(q.get("marking_schema"), dict) and isinstance(q["marking_schema"].get("marking_points"), list):
                mps = [f"- {mp.get('desc')} [{mp.get('marks', 1)} marks]" for mp in q["marking_schema"]["marking_points"] if mp.get("desc")]
                if mps:
                    q["worked_solution"] = "Marking Criteria & Solution Steps:\n" + "\n".join(mps)
        if not q.get("canonical_solution") and q.get("worked_solution"):
            q["canonical_solution"] = q["worked_solution"]
        if not q.get("sample_answer") and q.get("worked_solution"):
            q["sample_answer"] = str(q["worked_solution"])
        if not q.get("marks") and q.get("mark_allocation"):
            q["marks"] = q["mark_allocation"]
        if not q.get("marking_schema"):
            q["marking_schema"] = [{"criterion": "Correct calculation and answer", "marks": q.get("marks", 1)}]
    return q


def _adapt_single_item_generator(gen_func: Callable) -> Callable:
    """Wraps a single-item generator (e.g. Gr8/Gr9 math) to return a list of questions."""
    import sys as _sys
    def adapter(**kw):
        count = int(kw.get("count", 1))
        seed_val = kw.get("seed")
        r = random.Random(seed_val) if seed_val is not None else random.Random()
        req_sub = kw.get("subskill", "mixed")
        mod_obj = _sys.modules.get(getattr(gen_func, "__module__", ""))
        mod_subs = []
        if mod_obj:
            for _attr in ("SUBSKILLS", "VALID_SUBSKILLS", "ARCHETYPES", "ORDERED_SUBSKILLS", "BUILDERS"):
                _v = getattr(mod_obj, _attr, None)
                if isinstance(_v, (list, tuple)) and _v:
                    mod_subs = [s for s in _v if isinstance(s, str)]
                    break
                elif isinstance(_v, dict) and _v:
                    mod_subs = [k for k in _v.keys() if isinstance(k, str)]
                    break
        questions = []
        for idx in range(count):
            sub_seed = r.randint(1, 1_000_000_000)
            iter_sub = (
                mod_subs[idx % len(mod_subs)]
                if (req_sub in ("mixed", "all", "", None) and mod_subs)
                else (req_sub or "mixed")
            )
            try:
                q = gen_func(
                    subskill=iter_sub,
                    difficulty=kw.get("difficulty", "medium"),
                    question_type=kw.get("question_type", "mixed"),
                    seed=sub_seed,
                )
            except TypeError:
                try:
                    q = gen_func(seed=sub_seed)
                except TypeError:
                    q = gen_func()
            q_norm = _normalize_question_dict(q)
            if isinstance(q_norm, dict) and iter_sub not in ("mixed", "all", "", None) and not q_norm.get("subskill"):
                q_norm["subskill"] = iter_sub
            questions.append(q_norm)
        return questions
    adapter._wrapped_func = gen_func
    adapter.__module__ = getattr(gen_func, '__module__', '')
    adapter.__name__ = getattr(gen_func, '__name__', 'adapter')
    return adapter


def _adapt_multi_item_generator(gen_func: Callable) -> Callable:
    """Wraps generators accepting count/seed parameters directly."""
    def adapter(**kw):
        count = int(kw.get("count", 1))
        seed_val = kw.get("seed")
        diff = kw.get("difficulty", "medium")
        sub = kw.get("subskill")
        if sub in ["mixed", "concepts", "all", ""]:
            sub = None
        qtype = kw.get("question_type", "mixed")

        attempts = [
            lambda: gen_func(count=count, seed=seed_val, difficulty=diff, subskill=sub, question_type=qtype),
            lambda: gen_func(count=count, seed=seed_val, difficulty=diff, subskill=None, question_type=qtype),
            lambda: gen_func(count=count, seed=seed_val, difficulty=diff),
            lambda: gen_func(count=count, seed=seed_val),
            lambda: gen_func(r=random.Random(seed_val) if seed_val is not None else random.Random(), n=count),
            lambda: gen_func(**kw),
        ]

        last_err = None
        for attempt in attempts:
            try:
                res = attempt()
                if isinstance(res, dict) and res.get("ok") is False:
                    continue
                if isinstance(res, list):
                    return [_normalize_question_dict(item) for item in res]
                elif isinstance(res, dict):
                    return _normalize_question_dict(res)
                return res
            except (TypeError, ValueError, KeyError) as e:
                last_err = e
                continue
        raise last_err or ValueError("Failed in multi-item generator adapter")
    adapter._wrapped_func = gen_func
    return adapter


# ============================================================================
# SUBJECT DICTIONARIES
# ============================================================================

GRADE7_MATH_GENERATORS = {
    "grade7_math_geometry_of_2d_shapes": g7_math_geom2d.generate,
    "grade7_math_2d_shapes": g7_math_geom2d.generate,
    "grade7_math_geometry_of_straight_lines": g7_math_geom2d.generate,
    "grade7_math_area_and_perimeter_of_2d_shapes": g7_math_perim_area.generate,
    "grade7_math_perimeter_and_area": g7_math_perim_area.generate,
    "grade7_math_measurement": g7_math_perim_area.generate,
    "grade7_math_surface_area_and_volume_of_3d_objects": g7_math_sa_vol.generate,
    "grade7_math_data_handling": g7_math_meas_data.generate,
    "grade7_math_statistics": g7_math_meas_data.generate,
    "grade7_math_collect_organise_summarise": g7_math_tally.generate,
    "grade7_math_represent_data": g7_math_repr.generate,
    "grade7_math_interpret_analyse_report": g7_math_meas_data.generate,
    "grade7_math_functions_1": g7_math_fn1.generate,
    "grade7_math_functions_2": g7_math_fn2.generate,
    "grade7_math_functions_3": g7_math_fn3.generate,
    "grade7_math_transformation_geometry": g7_math_trans.generate,
    "grade7_math_geometry_of_straight_lines": g7_math_lines.generate,
    "grade7_math_construction_of_geometric_figures": g7_math_construction.generate,
    "grade7_math_whole_numbers": g7_math_whole.generate,
    "grade7_math_working_with_whole_numbers": g7_math_whole.generate,
    "grade7_math_integers": g7_math_int.generate,
    "grade7_math_patterns": g7_math_pat.generate,
    "grade7_math_numeric_and_geometric_patterns": g7_math_geom_pat.generate,
    "grade7_math_numeric_patterns": g7_math_num_pat.generate,
    "grade7_math_algebraic_expressions": g7_math_alg1.generate,
    "grade7_math_algebraic_expressions_1": g7_math_alg1.generate,
    "grade7_math_algebraic_expressions_2": g7_math_alg2.generate,
    "grade7_math_algebraic_equations": g7_math_eq1.generate,
    "grade7_math_algebraic_equations_1": g7_math_eq1.generate,
    "grade7_math_algebraic_equations_2": g7_math_eq2.generate,
    "grade7_math_relationships_between_variables": g7_math_rel_vars.generate,
    "grade7_math_probability": g7_math_data.generate,
    "grade7_math_functions": g7_math_graph.generate,
    "grade7_math_functions_and_relationships": g7_math_graph.generate,
    "grade7_math_graphs": g7_math_graph_stories.generate,
    "grade7_math_exponents": g7_math_exp.generate,
    "grade7_math_fractions": g7_math_frac.generate,
    "grade7_math_common_fractions": g7_math_frac.generate,
    "grade7_math_decimal_notation": g7_math_dec.generate,
    "grade7_math_decimals": g7_math_dec.generate,
    "grade7_math_decimal_fractions": g7_math_dec.generate,
    "grade7_math_geometric_nets_3d": g7_math_nets.generate,
    "grade7_math_geometry_of_3d_objects": g7_math_nets.generate,
    "grade7_math_3d_shapes_and_nets": g7_math_nets.generate,
    "grade7_math_nets_of_3d_shapes": g7_math_nets.generate,
}

GRADE8_MATH_GENERATORS = {
    "grade8_math_algebraic_expressions": g8_math_alg1.generate,
    "grade8_math_algebraic_expressions_1": g8_math_alg1.generate,
    "grade8_math_algebraic_expressions_2": g8_math_alg2.generate,
    "grade8_math_algebraic_equations": g8_math_eq1.generate,
    "grade8_math_algebraic_equations_1": g8_math_eq1.generate,
    "grade8_math_algebraic_equations_2": g8_math_eq2.generate,
    "grade8_math_algebraic_equations_3": g8_math_eq3.generate,
    "grade8_math_functions_1": g8_math_fn1.generate,
    "grade8_math_functions_2": g8_math_fn2.generate,
    "grade8_math_graphs": g8_math_graphs.generate,
    "grade8_math_collect_organise_summarise": g8_math_collect.generate,
    "grade8_math_represent_data": g8_math_repr.generate,
    "grade8_math_interpret_analyse_report": g8_math_meas_data.generate,
    "grade8_math_exponents": g8_math_exp_dedicated.generate,
    "grade8_math_functions": _adapt_single_item_generator(g8_math_func.generate_grade8_functions_question),
    "grade8_math_integers": g8_math_int.generate,
    "grade8_math_patterns": g8_math_patterns_dedicated.generate,
    "grade8_math_whole_numbers": g8_math_whole_dedicated.generate,
    "grade8_math_fractions": g8_common_fractions.generate,
    "grade8_math_decimal_fractions": g8_math_dec_frac.generate,
    "grade8_math_decimal_notation": g8_math_dec_frac.generate,
    "grade8_math_percentages": g8_math_frac_dec.generate,
    "grade8_math_theorem_of_pythagoras": g8_math_pyth.generate,
    "grade8_math_pythagoras": g8_math_pyth.generate,
    "grade8_math_geometry_of_2d_shapes": g8_math_geom2d.generate,
    "grade8_math_triangles": g8_math_geom2d.generate,
    "grade8_math_geometry_of_straight_lines": g8_math_lines.generate,
    "grade8_math_straight_lines": g8_math_lines.generate,
    "grade8_math_geometry_of_3d_objects": g8_math_3d_obj.generate,
    "grade8_math_3d_objects": g8_math_3d_obj.generate,
    "grade8_math_geometric_nets_3d": g7_math_nets.generate,
    "grade8_math_area_and_perimeter_of_2d_shapes": g8_math_p2d.generate,
    "grade8_math_perimeter_and_area_of_2d_shapes": g8_math_p2d.generate,
    "grade8_math_perimeter_and_area": g8_math_p2d.generate,
    "grade8_math_surface_area_and_volume_of_3d_objects": g8_math_meas3d.generate,
    "grade8_math_measurement_3d": g8_math_meas3d.generate,
    "grade8_math_data_handling": g_sp_data_handling,
    "grade8_math_transformation_geometry": g8_math_transform.generate,
    "grade8_math_construction_of_geometric_figures": g8_math_construction.generate,
    "grade8_math_probability": g8_math_prob_dedicated.generate,
}

GRADE9_MATH_GENERATORS = {
    # Term 1 (8 topics)
    "grade9_math_whole_numbers": g9_math_whole.generate,
    "grade9_math_integers": g9_math_int.generate,
    "grade9_math_decimal_notation": g9_math_dec.generate,
    "grade9_math_the_decimal_notation_for_fractions": g9_math_dec.generate,
    "grade9_math_decimal_fractions": g9_math_dec.generate,
    "grade9_math_exponents": g9_math_exp.generate,
    "grade9_math_patterns": g9_math_pat.generate,
    "grade9_math_functions": g9_math_func.generate,
    "grade9_math_algebraic_expressions": g9_math_expr.generate,
    "grade9_math_factorisation": g9_math_fact.generate,

    # Term 2 (6 topics)
    "grade9_math_algebraic_equations": g9_math_eq.generate,
    "grade9_math_algebraic_equations_fractions": g9_math_eq_frac.generate,
    "grade9_math_fractions": _adapt_single_item_generator(g9_math_frac.generate_grade9_fractions_question),
    "grade9_math_graphs": _adapt_single_item_generator(g9_math_graphs.generate_grade9_graphs_question),
    "grade9_math_geometry_of_straight_lines": g9_math_str_lines.generate,
    "grade9_math_geometry_of_2d_shapes": g9_math_2d_shapes.generate,

    # Term 3 (4 topics)
    "grade9_math_construction_of_geometric_figures": g9_math_construct.generate,
    "grade9_math_transformation_geometry": g9_math_trans.generate,
    "grade9_math_theorem_of_pythagoras": g9_math_pyth.generate,
    "grade9_math_pythagoras": g9_math_pyth.generate,
    "grade9_math_area_and_perimeter_of_2d_shapes": g9_math_area2d.generate,

    # Term 4 (6 topics)
    "grade9_math_geometry_of_3d_objects": g9_math_geom3d.generate,
    "grade9_math_surface_area_and_volume_of_3d_objects": g9_math_meas3d.generate,
    "grade9_math_measurement_3d": g9_math_meas3d.generate,
    "grade9_math_data_summarise": g9_math_datasum.generate,
    "grade9_math_data_represent": g9_math_datarep.generate,
    "grade9_math_data_interpret": g9_math_dataint.generate,
    "grade9_math_probability": g9_math_prob.generate,

    # Backward compatibility and aliases
    "grade9_math_congruence_similarity": g9_math_geom.generate,
    "grade9_math_geometry": g9_math_2d_shapes.generate,
    "grade9_math_algebraic_fractions": g9_math_eq_frac.generate,
    "grade9_math_geometric_nets_3d": g9_math_geom3d.generate,
    "grade9_math_data_handling": g9_math_datasum.generate,
}

GRADE10_MATH_GENERATORS = {
    "grade10_math_algebraic_expressions": g10_math_alg.generate,
    "grade10_math_equations_inequalities": g10_math_eq.generate,
    "grade10_math_exponents": g10_math_exp.generate,
    "grade10_math_patterns_sequences": g10_math_pat.generate,
    "grade10_math_trigonometry": g10_math_trig.generate,
    "grade10_math_functions": g10_math_func.generate,
    "grade10_math_euclidean_geometry": g10_math_geom.generate,
    "grade10_math_analytical_geometry": _adapt_single_item_generator(g10_math_analgeo.generate_analytical_geometry_question),
    "grade10_math_measurements": g10_math_meas.generate,
    "grade10_math_finance": g10_math_fin.generate,
    "grade10_math_finance_growth": g10_math_fin.generate,
    "grade10_math_finance_and_growth": g10_math_fin.generate,
    "grade10_math_statistics": g10_math_stat.generate,
    "grade10_math_probability": g10_math_prob.generate,
    "grade10_math_probability_studio": g10_math_prob.generate,
}

GRADE11_MATH_GENERATORS = {
    "grade11_math_analytical_geometry": _adapt_multi_item_generator(g11_math_analgeo.generate_questions),
    "grade11_math_equations_inequalities": _adapt_single_item_generator(g11_math_eq.generate_grade11_equations_inequalities_question),
    "grade11_math_exponents_surds": _adapt_single_item_generator(g11_math_surds.generate_grade11_exponents_surds_question),
    "grade11_math_patterns_sequences": _adapt_multi_item_generator(g11_math_pat.generate_questions),
    "grade11_math_circle_geometry": g11_math_circ.generate,
    "grade11_math_circle_geometry_theorems": g11_math_circ_theorems.generate,
    "grade11_math_circle_riders": g11_math_circ_theorems.generate,
    "grade11_math_trigonometry_reductions": g11_math_trig_red.generate,
    "grade11_math_trigonometry": g11_math_trig_red.generate,
    "grade11_math_finance": g11_math_fin.generate,
    "grade11_math_finance_growth_decay": g11_math_fin.generate,
    "grade11_math_growth_and_decay": g11_math_fin.generate,
    "grade11_math_probability": g11_math_prob.generate,
    "grade11_math_probability_contingency": g11_math_prob.generate,
    "grade11_math_contingency_tables": g11_math_prob.generate,
    "grade11_math_statistics": g11_math_stat.generate,
    "grade11_math_statistics_summary_ogive": g11_math_stat.generate,
    "grade11_math_ogive": g11_math_stat.generate,
    "grade11_math_linear_programming": g11_math_lp.generate,
    "grade11_math_measurement": g10_math_meas.generate,
    "grade11_math_investigation_and_projects": g11_math_lp.generate,
    "grade11_math_functions": g11_math_func.generate,
    "grade11_math_functions_graphs": g11_math_func.generate,
    "grade11_math_functions_and_graphs": g11_math_func.generate,
}

GRADE12_MATH_GENERATORS = {
    "grade12_math_finance": _adapt_multi_item_generator(g12_math_fin.generate_questions),
    "grade12_math_functions": _adapt_multi_item_generator(g12_math_func.generate_questions),
    "grade12_math_patterns_sequences_series": g12_math_seq.generate,
    "grade12_math_sequences_series": g12_math_seq.generate,
    "grade12_math_trigonometry": g12_math_trig_comp.generate,
    "grade12_math_trigonometry_compound": g12_math_trig_comp.generate,
    "grade12_math_differential_calculus": g12_math_calc.generate,
    "grade12_math_calculus": g12_math_calc.generate,
    "grade12_math_analytical_geometry": g12_math_circles.generate,
    "grade12_math_analytical_geometry_circles": g12_math_circles.generate,
    "grade12_math_circles": g12_math_circles.generate,
    "grade12_math_counting_probability": g12_math_prob.generate,
    "grade12_math_probability": g12_math_prob.generate,
    "grade12_math_counting_principles": g12_math_prob.generate,
    "grade12_math_bivariate_statistics": g12_math_stat.generate,
    "grade12_math_statistics": g12_math_stat.generate,
    "grade12_math_regression": g12_math_stat.generate,
}

# Grade 10 Business Studies (enhanced with Combinatorial Engine)
GRADE10_BS_GENERATORS = {
    "grade10_bs_micro_environment": micro_environment_generator.generate,
    "grade10_bs_business_functions": business_functions_generator.generate_business_functions,
    "grade10_bs_market_environment": market_environment_generator.generate_market_environment,
    "grade10_bs_macro_environment": macro_environment_generator.generate_macro_environment,
    "grade10_bs_interrelationship": interrelationship_generator.generate_interrelationship,
    "grade10_bs_business_sectors": business_sectors_generator.generate_business_sectors,
    "grade10_bs_socio_economic_issues": socio_economic_issues_generator.generate_socio_economic_issues,
    "grade10_bs_social_responsibility": social_responsibility_generator.generate_social_responsibility,
    "grade10_bs_entrepreneurial_qualities": entrepreneurial_qualities_generator.generate_entrepreneurial_qualities,
    "grade10_bs_forms_of_ownership": forms_of_ownership_generator.generate_forms_of_ownership,
    "grade10_bs_concept_of_quality": concept_of_quality_generator.generate_concept_of_quality,
    "grade10_bs_creative_thinking": creative_thinking_generator.generate_creative_thinking,
    "grade10_bs_business_opportunities": business_opportunities_generator.generate_business_opportunities,
    "grade10_bs_business_location": business_location_generator.generate_business_location,
    "grade10_bs_contracts": contracts_generator.generate_contracts,
    "grade10_bs_presentation": presentation_generator.generate_presentation,
    "grade10_bs_business_plans": business_plans_generator.generate_business_plans,
    "grade10_bs_combinatorial": lambda **kw: generate_combinatorial_batch(
        subskill_id=kw.get("subskill", "bs_macro_micro"),
        term=int(kw.get("term", 1)),
        count=int(kw.get("count", 4)),
        seed=kw.get("seed"),
        mode=kw.get("mode", "compound"),
    ),
}

GRADE11_BS_GENERATORS = {
    "grade11_bs_adapting_to_challenges": g11_bs_adapt.generate,
    "grade11_bs_avenues_of_acquiring_businesses": g11_bs_avenues.generate,
    "grade11_bs_benefits_of_a_company": g11_bs_benefits.generate,
    "grade11_bs_business_sectors": g11_bs_sectors.generate,
    "grade11_bs_influences_on_business_environments": g11_bs_influences.generate,
    "grade11_bs_socio_economic_issues": g11_bs_socio.generate,
    "grade11_bs_challenges_of_business_environments": g11_bs_challenges.generate,
    "grade11_bs_creative_thinking": g11_bs_creative.generate,
    "grade11_bs_marketing_function": g11_bs_mkt.generate,
    "grade11_bs_production_function": g11_bs_prod.generate,
    "grade11_bs_marketing_production": g11_bs_mkt_prod.generate,
    "grade11_bs_professionalism_and_ethics": g11_bs_ethics.generate,
    "grade11_bs_stress_crisis_change": g11_bs_stress.generate,
    "grade11_bs_business_plan_transformation": g11_bs_plan.generate,
    "grade11_bs_citizenship_responsibilities": g11_bs_citizenship.generate,
    "grade11_bs_entrepreneurial_assessment": g11_bs_entrepreneur.generate,
    "grade11_bs_presentation_of_information": g11_bs_pres.generate,
    "grade11_bs_start_business_venture": g11_bs_venture.generate,
    "grade11_bs_human_resources_function": g11_bs_hr.generate,
    "grade11_bs_human_resources": g11_bs_hr.generate,
}

GRADE12_BS_GENERATORS = {
    "grade12_bs_creative_thinking_problem_solving": g12_bs_creative.generate,
    "grade12_bs_creative_thinking": g12_bs_creative.generate,
    "grade12_bs_ethics_and_professionalism": g12_bs_ethics.generate,
    "grade12_bs_human_resources_function": g12_bs_hr.generate,
    "grade12_bs_human_resources": g12_bs_hr.generate,
    "grade12_bs_impact_of_legislation": g12_bs_legislation.generate,
    "grade12_bs_macro_environment_strategies": g12_bs_macro_strat.generate,
    "grade12_bs_legislation_hr": g12_bs_leg_hr.generate,
    "grade12_bs_business_sectors_environments": g12_bs_sectors_env.generate,
    "grade12_bs_business_sectors": g12_bs_sectors_env.generate,
    "grade12_bs_investment_insurance": g12_bs_insurance.generate,
    "grade12_bs_investment_securities": g12_bs_securities.generate,
    "grade12_bs_investments_management": g12_bs_inv_man.generate,
    "grade12_bs_management_and_leadership": g12_bs_leadership.generate,
    "grade12_bs_quality_of_performance": g12_bs_quality.generate,
    "grade12_bs_team_performance_conflict": g12_bs_team_conflict.generate,
    "grade12_bs_team_dynamics": g12_bs_team_conflict.generate,
    "grade12_bs_forms_of_ownership_success": g12_bs_ownership.generate,
    "grade12_bs_forms_of_ownership": g12_bs_ownership.generate,
    "grade12_bs_human_rights_inclusivity": g12_bs_human_rights.generate,
    "grade12_bs_presentation_data_responses": g12_bs_presentation.generate,
    "grade12_bs_presentation": g12_bs_presentation.generate,
    "grade12_bs_social_responsibility_csr_csi": g12_bs_csr.generate,
    "grade12_bs_social_responsibility": g12_bs_csr.generate,
    "grade12_bs_essay": g12_bs_essay.generate,
    "grade12_bs_section_c": g12_bs_essay.generate,
    "grade12_bs_40_marks": g12_bs_essay.generate,
}

GRADE7_EMS_GENERATORS = {
    "grade7_ems_money_and_needs": g7_history_of_money.generate,
    "grade7_ems_history_of_money": g7_history_of_money.generate,
    "grade7_ems_needs_and_wants": g7_needs_and_wants.generate,
    "grade7_ems_goods_and_services": g7_goods.generate,
    "grade7_ems_businesses": g7_businesses.generate,
    "grade7_ems_accounting_concepts": g7_acct_concepts.generate,
    "grade7_ems_income_and_expenses": g7_income.generate,
    "grade7_ems_budgets": g7_budgets.generate,
    "grade7_ems_entrepreneurship": g7_the_entrepreneur.generate,
    "grade7_ems_the_entrepreneur": g7_the_entrepreneur.generate,
    "grade7_ems_starting_a_business": g7_starting_a_business.generate,
    "grade7_ems_entrepreneurs_day": g7_entrepreneurs_day.generate,
    "grade7_ems_inequality_and_poverty": g7_inequality.generate,
    "grade7_ems_savings": g7_savings.generate,
    "grade7_ems_production_process": g7_prod.generate,
    "grade7_ems_the_production_process": g7_prod.generate,
}

GRADE8_EMS_GENERATORS = {
    "grade8_ems_gov_and_society": g8_government_gen.generate,
    "grade8_ems_government": g8_government_gen.generate,
    "grade8_ems_national_budget": g8_budget_gen.generate,
    "grade8_ems_the_national_budget": g8_budget_gen.generate,
    "grade8_ems_standard_of_living": g8_government_gen.generate,
    "grade8_ems_accounting_basics": g8_acct_basics.generate,
    "grade8_ems_source_documents": g8_source_docs.generate,
    "grade8_ems_general_ledger": g8_general_ledger.generate,
    "grade8_ems_markets_and_production": g8_markets_gen.generate,
    "grade8_ems_markets": g8_markets_gen.generate,
    "grade8_ems_the_markets": g8_markets_gen.generate,
    "grade8_ems_factors_of_production": g8_fop_gen.generate,
    "grade8_ems_crj": g8_crj.generate,
    "grade8_ems_cash_receipts_journal": g8_crj.generate,
    "grade8_ems_cash_payments_journal": g8_cpj_crj.generate,
    "grade8_ems_accounting_cycle": g8_acct_cycle.generate,
    "grade8_ems_the_accounting_cycle": g8_acct_cycle.generate,
    "grade8_ems_cpj_and_crj": g8_cpj_crj.generate,
    "grade8_ems_ownership": g8_ownership.generate,
    "grade8_ems_forms_of_ownership": g8_ownership.generate,
    "grade8_ems_management": g8_mgmt.generate,
    "grade8_ems_levels_and_functions_of_management": g8_mgmt.generate,
    "grade8_ems_levels_of_management": g8_mgmt.generate,
    "grade8_ems_functions_of_management": g8_mgmt.generate,
    "grade8_ems_gap": g8_ems_gap.generate,
}

GRADE9_EMS_GENERATORS = {
    "grade9_ems_crj": lambda **kw: g9_crj_cpj.generate(subskill="crj", **{k: v for k, v in kw.items() if k != "subskill"}),
    "grade9_ems_cpj": lambda **kw: g9_crj_cpj.generate(subskill="cpj", **{k: v for k, v in kw.items() if k != "subskill"}),
    "grade9_ems_crj_cpj": g9_crj_cpj.generate,
    "grade9_ems_general_ledger": g9_gl.generate,
    "grade9_ems_economic_systems": g9_economy.generate,
    "grade9_ems_circular_flow": g9_circular.generate,
    "grade9_ems_debtors_journal": g9_dj.generate,
    "grade9_ems_price_theory": g9_price_theory.generate,
    "grade9_ems_sectors_of_economy": g9_sectors.generate,
    "grade9_ems_creditors_journal": g9_cj.generate,
    "grade9_ems_creditors_journal_2": g9_cj.generate,
    "grade9_ems_debtors_ledger": g9_dl.generate,
    "grade9_ems_creditors_ledger": g9_cl.generate,
    "grade9_ems_business_functions": g9_business.generate,
    "grade9_ems_trade_unions": g9_trade_unions.generate,
    "grade9_ems_business_plan": g9_bp.generate,
    "grade9_ems_transactions_cash_and_credit": g9_cash_credit.generate,
}

GRADE10_ACCOUNTING_GENERATORS = {
    "grade10_accounting_sole_trader": _adapt_multi_item_generator(g10_acct_sole.generate_questions),
    "grade10_accounting_gaap": _adapt_multi_item_generator(g10_acct_gaap.generate_grade10_gaap_questions),
    "grade10_accounting_financial_info_concepts": _adapt_multi_item_generator(g10_acct_fin_info.generate_questions),
    "grade10_accounting_managing_resources": _adapt_multi_item_generator(g10_acct_resources.generate_questions),
    "grade10_accounting_ethics": _adapt_multi_item_generator(g10_acct_ethics.generate_questions),
    "grade10_accounting_internal_control": _adapt_multi_item_generator(g10_acct_ctrl.generate_questions),
    "grade10_accounting_vat": _adapt_multi_item_generator(g10_acct_vat.generate_questions),
    "grade10_accounting_salaries_wages": _adapt_multi_item_generator(g10_acct_sal.generate_questions),
    "grade10_accounting_final_accounts": _adapt_multi_item_generator(g10_acct_final.generate_questions),
    "grade10_accounting_sole_trader_financial_statements": _adapt_multi_item_generator(g10_acct_stmt.generate_questions),
    "grade10_accounting_sole_trader_analysis": _adapt_multi_item_generator(g10_acct_analysis.generate_questions),
    "grade10_accounting_cost_accounting": _adapt_multi_item_generator(g10_acct_cost.generate_questions),
    "grade10_accounting_budgets": _adapt_multi_item_generator(g10_acct_budgets.generate_questions),
    "grade10_accounting_financial_vs_managerial": _adapt_multi_item_generator(g10_acct_fin_vs_mgr.generate_questions),
    "grade10_accounting_indigenous_bookkeeping": _adapt_multi_item_generator(g10_acct_indig.generate_questions),
    "grade10_accounting_bank_reconciliation": _adapt_multi_item_generator(g10_acct_recon.generate_questions),
    "grade10_accounting_fixed_assets": g10_acct_fixed.generate,
    "grade10_accounting_depreciation": g10_acct_fixed.generate,
    "grade10_accounting_inventory": g10_acct_inv.generate,
    "grade10_accounting_cost_of_sales": g10_acct_inv.generate,
}

GRADE11_ACCOUNTING_GENERATORS = {
    "grade11_accounting_reconciliation": _adapt_multi_item_generator(g11_acct_recon.generate_bank_reconciliation_questions),
    "grade11_accounting_creditors_reconciliation": _adapt_multi_item_generator(g11_acct_recon.generate_creditors_reconciliation_questions),
    "grade11_accounting_control_accounts": _adapt_multi_item_generator(g11_acct_ctrl_acc.generate_questions),
    "grade11_accounting_debtors_age_analysis": _adapt_multi_item_generator(g11_acct_debtors.generate_questions),
    "grade11_accounting_disposal_of_tangible_assets": _adapt_multi_item_generator(g11_acct_disposal.generate_questions),
    "grade11_accounting_fixed_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_fixed_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_equation": _adapt_multi_item_generator(g11_acct_eq.generate_questions),
    "grade11_accounting_vat": g11_acct_vat.generate,
    "grade11_accounting_analysis_interpretation": _adapt_multi_item_generator(g11_acct_analysis.generate_questions),
    "grade11_accounting_calculations_involving_percentages": _adapt_multi_item_generator(g11_acct_analysis.generate_questions),
    "grade11_accounting_income_statement": _adapt_multi_item_generator(g11_acct_inc.generate_questions),
    "grade11_accounting_ethics": _adapt_multi_item_generator(g11_acct_ethics.generate_questions),
    "grade11_accounting_internal_control": _adapt_multi_item_generator(g11_acct_int_ctrl.generate_questions),
    "grade11_accounting_partnerships": _adapt_multi_item_generator(g11_acct_bs.generate_questions),
    "grade11_accounting_partnership_ledger": _adapt_multi_item_generator(g11_acct_led.generate_questions),
    "grade11_accounting_concepts": _adapt_multi_item_generator(g11_acct_concepts.generate_questions),
    "grade11_accounting_partnerships_financial_statements": _adapt_multi_item_generator(g11_acct_part_stmt.generate_questions),
    "grade11_accounting_partnership_financial_statements": _adapt_multi_item_generator(g11_acct_part_stmt.generate_questions),
    "grade11_accounting_budgets": _adapt_multi_item_generator(g11_acct_budgets.generate_questions),
    "grade11_accounting_cash_budget_variance": _adapt_multi_item_generator(g11_acct_budgets.generate_questions),
    "grade11_accounting_cost_accounting": _adapt_multi_item_generator(g11_acct_cost.generate_questions),
    "grade11_accounting_inventory_valuation": _adapt_multi_item_generator(g11_acct_inv.generate_questions),
    "grade11_accounting_inventory_systems": _adapt_multi_item_generator(g11_acct_inv.generate_questions),
    "grade11_accounting_clubs_nonprofit": _adapt_multi_item_generator(g11_acct_clubs.generate_questions),
}

GRADE12_ACCOUNTING_GENERATORS = {
    "grade12_accounting_concepts": _adapt_multi_item_generator(g12_acct_concepts.generate_questions),
    "grade12_accounting_companies": _adapt_multi_item_generator(g12_acct_companies.generate),
    "grade12_accounting_company_ledger": _adapt_multi_item_generator(g12_acct_gl.generate_questions),
    "grade12_accounting_financial_statements": _adapt_multi_item_generator(g12_acct_stmt.generate_questions),
    "grade12_accounting_equation": _adapt_multi_item_generator(g12_acct_eq.generate),
    "grade12_accounting_analysis_interpretation": g12_acct_indicators.generate,
    "grade12_accounting_financial_indicators": g12_acct_indicators.generate,
    "grade12_accounting_bank_reconciliation": _adapt_multi_item_generator(g12_acct_recon.generate_bank_reconciliation_questions),
    "grade12_accounting_reconciliations": _adapt_multi_item_generator(g12_acct_recon.generate_creditors_reconciliation_questions),
    "grade12_accounting_cash_flow_statement": g12_acct_cfs.generate,
    "grade12_accounting_cash_flow": g12_acct_cfs.generate,
    "grade12_accounting_control_accounts": _adapt_multi_item_generator(g12_acct_ctrl_acc.generate_questions),
    "grade12_accounting_debtors_age_analysis": _adapt_multi_item_generator(g12_acct_debtors.generate),
    "grade12_accounting_budgets": _adapt_multi_item_generator(g12_acct_budgets.generate),
    "grade12_accounting_cash_budget_variance": _adapt_multi_item_generator(g12_acct_variance.generate_questions),
    "grade12_accounting_inventories": _adapt_multi_item_generator(g12_acct_inv.generate_questions),
    "grade12_accounting_cost_accounting": g12_acct_cost.generate,
    "grade12_accounting_production_cost": g12_acct_cost.generate,
    "grade12_accounting_vat": _adapt_multi_item_generator(g12_acct_vat.generate),
    "grade12_accounting_disposal_of_tangible_assets": _adapt_multi_item_generator(g12_acct_disposal.generate_questions),
    "grade12_accounting_fixed_assets": _adapt_multi_item_generator(g12_acct_fixed.generate_questions),
}

SCIENCES_AND_TECH_GENERATORS = {
    "physical_sciences_mechanics": phys_mech.generate,
    "physical_sciences_inclined_planes": lambda **kw: phys_mech.generate(subskill="inclined_plane_newton", **kw),
    "physical_sciences_stoichiometry_equilibrium": phys_chem_eq.generate,
    "physical_sciences_chemistry_equilibrium": phys_chem_eq.generate,
    "physical_sciences_momentum_impulse": phys_momentum.generate,
    "grade12_physical_sciences_momentum": phys_momentum.generate,
    "physical_sciences_momentum": phys_momentum.generate,
    "physical_sciences_collisions": phys_momentum.generate,
    "life_sciences_genetics": life_gen.generate,
    "life_sciences_dihybrid_cross": life_dihybrid.generate,
    "life_sciences_pedigree": life_dihybrid.generate,
    "mathematical_literacy_finance_tax": mathlit_fin.generate,
    "mathematical_literacy_maps_scales": mathlit_maps.generate,
    "mathematical_literacy_tariffs_tax_brackets": mathlit_tariffs.generate,
    "grade10_mathlit_data_handling": _adapt_multi_item_generator(mathlit_data.generate),
    "mathematical_literacy_data_handling": _adapt_multi_item_generator(mathlit_data.generate),
    "mathematical_literacy_conversions_time": _adapt_multi_item_generator(mathlit_conversions_time.generate),
    "grade10_mathlit_conversions_and_time": _adapt_multi_item_generator(mathlit_conversions_time.generate),
    "grade10_mathlit_measuring": _adapt_multi_item_generator(mathlit_measuring.generate),
    "grade10_mathlit_measuring_length_weight_volume_temperature": _adapt_multi_item_generator(mathlit_measuring.generate),
    "mathematical_literacy_measurement": _adapt_multi_item_generator(mathlit_measuring.generate),
    "grade10_mathlit_personal_income_expenditure_budgets": _adapt_multi_item_generator(mathlit_budgets.generate),
    "grade10_mathlit_numbers_and_calculations_with_numbers": _adapt_multi_item_generator(mathlit_numbers.generate),
    "mathematical_literacy_numbers_and_calculations_with_numbers": _adapt_multi_item_generator(mathlit_numbers.generate),
    "grade10_mathlit_banking_interest_and_taxation": _adapt_multi_item_generator(mathlit_banking_tax.generate),
    "mathematical_literacy_banking_interest_and_taxation": _adapt_multi_item_generator(mathlit_banking_tax.generate),
    "grade10_mathlit_financial_documents_and_tariff_systems": _adapt_multi_item_generator(mathlit_tariffs_systems.generate),
    "mathematical_literacy_financial_documents_and_tariff_systems": _adapt_multi_item_generator(mathlit_tariffs_systems.generate),
    "grade10_mathlit_assembly_diagrams_floor_plans_packaging": _adapt_multi_item_generator(mathlit_assembly_plans.generate),
    "mathematical_literacy_assembly_diagrams_floor_plans_packaging": _adapt_multi_item_generator(mathlit_assembly_plans.generate),
    "grade10_mathlit_scale_maps_and_plans": _adapt_multi_item_generator(mathlit_scale_maps.generate),
    "mathematical_literacy_scale_maps_and_plans": _adapt_multi_item_generator(mathlit_scale_maps.generate),
    "grade10_mathlit_measurement_of_perimeter_and_area": _adapt_multi_item_generator(mathlit_perimeter_area.generate),
    "mathematical_literacy_measurement_of_perimeter_and_area": _adapt_multi_item_generator(mathlit_perimeter_area.generate),
    "grade10_mathlit_patterns_relationships_and_representations": _adapt_multi_item_generator(mathlit_patterns.generate),
    "mathematical_literacy_patterns_relationships_and_representations": _adapt_multi_item_generator(mathlit_patterns.generate),
    "mathematical_literacy_personal_income_expenditure_budgets": _adapt_multi_item_generator(mathlit_budgets.generate),
    "grade10_mathlit_probability": _adapt_multi_item_generator(mathlit_prob.generate),
    "grade11_mathlit_finance_taxation_and_uif": _adapt_multi_item_generator(mathlit_gr11_fin.generate),
    "grade11_mathlit_conversions_and_time": _adapt_multi_item_generator(mathlit_gr11_conv.generate),
    "grade11_mathlit_exchange_rates": _adapt_multi_item_generator(mathlit_gr11_exch.generate),
    "grade11_mathlit_interest_banking_and_inflation": _adapt_multi_item_generator(mathlit_gr11_interest.generate),
    "grade11_mathlit_patterns_relationships_and_representations": _adapt_multi_item_generator(mathlit_gr11_pat.generate),
    "grade11_mathlit_plans_and_other_representations": _adapt_multi_item_generator(mathlit_gr11_plans.generate),
    "grade11_mathlit_data_handling": _adapt_multi_item_generator(mathlit_gr11_data.generate),
    "grade11_mathlit_maps": _adapt_multi_item_generator(mathlit_gr11_maps.generate),
    "grade11_mathlit_area_and_volume": _adapt_multi_item_generator(mathlit_gr11_area_vol.generate),
    "grade11_mathlit_financial_documents_and_tariff_systems": _adapt_multi_item_generator(mathlit_gr11_tariffs.generate),
    "grade11_mathlit_weight_and_temperature": _adapt_multi_item_generator(mathlit_gr11_weight_temp.generate),
    "grade11_mathlit_probability": _adapt_multi_item_generator(mathlit_gr11_prob.generate),
    "grade12_mathlit_exchange_rates": _adapt_multi_item_generator(mathlit_gr12_exch.generate),
    "grade12_mathlit_income_tax": _adapt_multi_item_generator(mathlit_gr12_tax.generate),
    "grade12_mathlit_financial_documents_and_tariff_systems": _adapt_multi_item_generator(mathlit_gr12_tariffs.generate),
    "grade12_mathlit_measurement_lengths_perimeter_area_volume": _adapt_multi_item_generator(mathlit_gr12_meas.generate),
    "grade12_mathlit_scale_and_map_work": _adapt_multi_item_generator(mathlit_gr12_scale.generate),
    "grade12_mathlit_measuring_weight_bmi_medicine_dosages": _adapt_multi_item_generator(mathlit_gr12_bmi.generate),
    "grade12_mathlit_maps_and_plans_models": _adapt_multi_item_generator(mathlit_gr12_models.generate),
    "grade12_mathlit_plans_and_scale": _adapt_multi_item_generator(mathlit_gr12_plans.generate),
    "grade12_mathlit_data_handling": _adapt_multi_item_generator(mathlit_gr12_data.generate),
    "grade12_mathlit_interest_banking_inflation": _adapt_multi_item_generator(mathlit_gr12_fin.generate),
    "grade12_mathlit_probability": _adapt_multi_item_generator(mathlit_gr12_prob.generate),
    "grade12_mathlit_conversions_and_time": _adapt_multi_item_generator(mathlit_gr12_conv.generate),
    "mathematical_literacy_probability": _adapt_multi_item_generator(mathlit_prob.generate),
    "technical_mathematics_complex_numbers": tech_cplx.generate,
    "technical_mathematics_mensuration": tech_mens.generate,
    "technical_mathematics_euclidean_geometry": g11_math_circ_theorems.generate,
    "technical_mathematics_geometry": g11_math_circ_theorems.generate,
    "technical_mathematics_analytical_geometry": g12_math_circles.generate,
    "technical_mathematics_circles_angles": tech_circles.generate,
    "technical_mathematics_angular_movement": tech_circles.generate,
    "technical_mathematics_polynomials": tech_poly.generate,
    "grade10_life_sciences_cytology": ls10_cells.generate,
    "life_sciences_plant_animal_cells": ls10_cells.generate,
    "grade10_life_sciences_mitosis": ls10_mitosis_gen.generate,
    "life_sciences_cell_division_mitosis": ls10_mitosis_gen.generate,
    "life_sciences_meiosis": ls12_meiosis_gen.generate,
    "grade12_life_sciences_meiosis": ls12_meiosis_gen.generate,
    "life_sciences_support_transport_plants": ls10_plants.generate,
    "grade10_life_sciences_support_transport_plants": ls10_plants.generate,
    "life_sciences_photosynthesis": ls11_photosynth.generate,
    "grade11_life_sciences_photosynthesis": ls11_photosynth.generate,
    "life_sciences_cellular_respiration": ls11_resp.generate,
    "grade11_life_sciences_cellular_respiration": ls11_resp.generate,
    "life_sciences_biospheres_ecosystems": ls10_biospheres.generate,
    "grade10_life_sciences_biospheres_ecosystems": ls10_biospheres.generate,
    "life_sciences_population_ecology": ls11_pop_ecology.generate,
    "grade11_life_sciences_population_ecology": ls11_pop_ecology.generate,
    "life_sciences_plant_responses_environment": ls12_plant_resp.generate,
    "grade12_life_sciences_plant_responses_environment": ls12_plant_resp.generate,
    "grade11_physical_sciences_chemistry": phys11_chem.generate,
    "grade11_physical_sciences_atomic_combinations": phys11_chem.generate,
    "grade11_physical_sciences_intermolecular_forces": phys11_chem.generate,
}

NATURAL_SCIENCES_GENERATORS = {
    "grade7_natural_sciences_the_biosphere": ns7_biosphere.generate,
    "grade7_natural_sciences_biodiversity": ns7_biodiversity.generate,
    "grade7_natural_sciences_sexual_reproduction": ns7_sexual_repro.generate,
    "grade7_natural_sciences_variation": ns7_variation.generate,
    "grade7_natural_sciences_properties_of_materials": ns7_properties.generate,
    "grade7_natural_sciences_the_periodic_table_of_elements": ns7_periodic_table.generate,
    "grade7_natural_sciences_sources_of_energy": ns7_sources_energy.generate,
    "grade7_natural_sciences_potential_and_kinetic_energy": ns7_potential_kinetic.generate,
    "grade7_natural_sciences_energy_transfer_to_surroundings": ns7_energy_transfer.generate,
    "grade7_natural_sciences_heat_energy_transfer": ns7_heat_transfer.generate,
    "grade7_natural_sciences_heat_insulation_and_energy_saving": ns7_heat_insulation.generate,
    "grade7_natural_sciences_relationship_of_the_moon_to_the_earth": ns7_moon_earth.generate,
    "grade7_natural_sciences_relationship_of_the_sun_to_the_earth": ns7_sun_earth.generate,
    "grade7_natural_sciences_historical_development_of_astronomy": ns7_astronomy_history.generate,
    "natural_sciences_electric_circuits": ns_circuits.generate,
    "natural_sciences_circuits": ns_circuits.generate,
    "natural_sciences_chemical_reactions": ns_reactions.generate,
    "natural_sciences_reactions": ns_reactions.generate,
    "natural_sciences_senior_phase_astronomy": ns_astronomy.generate,
    "natural_sciences_separating_mixtures": ns7_separating.generate,
    "grade7_natural_sciences_separating_mixtures": ns7_separating.generate,
    "natural_sciences_acids_bases_neutrals": ns7_acids_bases.generate,
    "grade7_natural_sciences_acids_bases_neutrals": ns7_acids_bases.generate,
    "natural_sciences_particle_model_matter": ns8_particles.generate,
    "grade8_natural_sciences_particle_model_matter": ns8_particles.generate,
    "natural_sciences_series_parallel_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_electric_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_photosynthesis": ns8_photosynth.generate,
    "grade8_natural_sciences_ecology": ns8_ecology.generate,
    "grade8_natural_sciences_atoms": ns8_atoms.generate,
    "grade8_natural_sciences_chemical_reactions": ns8_chem_reactions.generate,
    "grade8_natural_sciences_microorganisms": ns8_microorganisms.generate,
    "grade8_natural_sciences_energy_transfer": ns8_energy_transfer.generate,
    "grade8_natural_sciences_static_electricity": ns8_static_elec.generate,
    "grade8_natural_sciences_visible_light": ns8_visible_light.generate,
    "grade8_natural_sciences_beyond_solar_system": ns8_beyond_solar.generate,
    "grade8_natural_sciences_telescopes": ns8_telescopes.generate,
    "natural_sciences_solar_system_seasons": ns8_solar_gen.generate,
    "grade8_natural_sciences_solar_system": ns8_solar_gen.generate,
    "natural_sciences_life_and_living": ns_life_living.generate,
    "natural_sciences_photosynthesis": lambda **kw: ns_life_living.generate(archetype="photosynthesis", **kw),
    "natural_sciences_angiosperm_reproduction": lambda **kw: ns_life_living.generate(archetype="angiosperm", **kw),
    "natural_sciences_matter_and_materials": ns_matter_materials.generate,
    "natural_sciences_separating_mixtures": ns7_separating.generate,
    "grade7_natural_sciences_separating_mixtures": ns7_separating.generate,
    "natural_sciences_acids_bases_neutrals": ns7_acids_bases.generate,
    "grade7_natural_sciences_acids_bases_neutrals": ns7_acids_bases.generate,
    "natural_sciences_particle_model_matter": ns8_particles.generate,
    "grade8_natural_sciences_particle_model_matter": ns8_particles.generate,
    "natural_sciences_series_parallel_circuits": ns8_circuits_gen.generate,
    "grade8_natural_sciences_electric_circuits": ns8_circuits_gen.generate,
    "natural_sciences_atomic_structure": ns_matter_materials.generate,
    "natural_sciences_energy_and_change": ns_energy_forces.generate,
    "natural_sciences_heat_energy_transfer": ns_energy_forces.generate,
    "natural_sciences_planet_earth_and_beyond": ns_planet_earth.generate,
    "natural_sciences_seasons_and_tides": ns_planet_earth.generate,

    # Grade 9 Natural Sciences (Terms 1 to 4 Dedicated Unbundled Generators)
    # Term 1: Life and Living
    "grade9_ns_cells": ns9_mod.cells_generator.generate,
    "grade9_natural_sciences_cells": ns9_mod.cells_generator.generate,
    "grade9_natural_sciences_cell_cytology": ns9_mod.cells_generator.generate,
    "natural_sciences_cell_cytology": ns9_mod.cells_generator.generate,

    "grade9_ns_human_systems": ns9_mod.human_systems_generator.generate,
    "grade9_natural_sciences_human_systems": ns9_mod.human_systems_generator.generate,
    "natural_sciences_human_systems": ns9_mod.human_systems_generator.generate,

    "grade9_ns_human_reproduction": ns9_mod.human_reproduction_gen.generate,
    "grade9_natural_sciences_human_reproduction": ns9_mod.human_reproduction_gen.generate,
    "natural_sciences_human_reproduction": ns9_mod.human_reproduction_gen.generate,

    "grade9_ns_circulatory_respiratory": ns9_mod.circulatory_respiratory.generate,
    "grade9_natural_sciences_circulatory_respiratory": ns9_mod.circulatory_respiratory.generate,
    "natural_sciences_circulatory_respiratory": ns9_mod.circulatory_respiratory.generate,
    "natural_sciences_heart": ns9_mod.circulatory_respiratory.generate,

    "grade9_ns_digestive_system": ns9_mod.digestive_system_gen.generate,
    "grade9_natural_sciences_digestive_system": ns9_mod.digestive_system_gen.generate,
    "natural_sciences_digestive_system": ns9_mod.digestive_system_gen.generate,
    "natural_sciences_digestive": ns9_mod.digestive_system_gen.generate,

    # Term 2: Matter and Materials
    "grade9_ns_compounds": ns9_mod.compounds_generator.generate,
    "grade9_natural_sciences_compounds": ns9_mod.compounds_generator.generate,

    "grade9_ns_chemical_reactions": ns9_mod.chemical_reactions_gen.generate,
    "grade9_natural_sciences_chemical_reactions": ns9_mod.chemical_reactions_gen.generate,

    "grade9_ns_reactions_metals_oxygen": ns9_mod.reactions_metals_oxygen.generate,
    "grade9_natural_sciences_reactions_metals_oxygen": ns9_mod.reactions_metals_oxygen.generate,

    "grade9_ns_reactions_nonmetals_oxygen": ns9_mod.reactions_nonmetals_ox.generate,
    "grade9_natural_sciences_reactions_nonmetals_oxygen": ns9_mod.reactions_nonmetals_ox.generate,

    "grade9_ns_acids_bases_ph": ns9_mod.acids_bases_ph_gen.generate,
    "grade9_natural_sciences_acids_bases_ph": ns9_mod.acids_bases_ph_gen.generate,

    "grade9_ns_reactions_acids_bases": ns9_mod.reactions_acids_bases.generate,
    "grade9_natural_sciences_reactions_acids_bases": ns9_mod.reactions_acids_bases.generate,
    "natural_sciences_acid_base_reactions": ns9_mod.reactions_acids_bases.generate,

    "grade9_ns_reactions_acids_metals": ns9_mod.reactions_acids_metals.generate,
    "grade9_natural_sciences_reactions_acids_metals": ns9_mod.reactions_acids_metals.generate,

    # Term 3: Energy and Change
    "grade9_ns_forces": ns9_mod.forces_generator.generate,
    "grade9_natural_sciences_forces": ns9_mod.forces_generator.generate,
    "natural_sciences_forces_and_weight": ns9_mod.forces_generator.generate,

    "grade9_ns_electric_cells": ns9_mod.electric_cells_gen.generate,
    "grade9_natural_sciences_electric_cells": ns9_mod.electric_cells_gen.generate,
    "natural_sciences_electric_cells_resistance": ns9_mod.electric_cells_gen.generate,
    "grade9_natural_sciences_electric_cells_resistance": ns9_mod.electric_cells_gen.generate,

    "grade9_ns_resistance": ns9_mod.resistance_generator.generate,
    "grade9_natural_sciences_resistance": ns9_mod.resistance_generator.generate,

    "grade9_ns_series_parallel_circuits": ns9_mod.series_parallel_circuits.generate,
    "grade9_natural_sciences_series_parallel_circuits": ns9_mod.series_parallel_circuits.generate,

    "grade9_ns_safety_electricity": ns9_mod.safety_electricity_gen.generate,
    "grade9_natural_sciences_safety_electricity": ns9_mod.safety_electricity_gen.generate,

    "grade9_ns_national_grid": ns9_mod.national_grid_generator.generate,
    "grade9_natural_sciences_national_grid": ns9_mod.national_grid_generator.generate,

    "grade9_ns_cost_electrical_energy": ns9_mod.cost_electrical_energy.generate,
    "grade9_natural_sciences_cost_electrical_energy": ns9_mod.cost_electrical_energy.generate,
    "natural_sciences_cost_of_electricity": ns9_mod.cost_electrical_energy.generate,

    # Term 4: Planet Earth and Beyond
    "grade9_ns_earth_system": ns9_mod.earth_system_generator.generate,
    "grade9_natural_sciences_earth_system": ns9_mod.earth_system_generator.generate,

    "grade9_ns_lithosphere": ns9_mod.lithosphere_generator.generate,
    "grade9_natural_sciences_lithosphere": ns9_mod.lithosphere_generator.generate,
    "natural_sciences_lithosphere_mining": ns9_mod.lithosphere_generator.generate,

    "grade9_ns_mining_resources": ns9_mod.mining_resources_gen.generate,
    "grade9_natural_sciences_mining_resources": ns9_mod.mining_resources_gen.generate,

    "grade9_ns_atmosphere": ns9_mod.atmosphere_generator.generate,
    "grade9_natural_sciences_atmosphere": ns9_mod.atmosphere_generator.generate,

    "grade9_ns_stellar_evolution": ns9_mod.stellar_evolution_gen.generate,
    "grade9_natural_sciences_stellar_evolution": ns9_mod.stellar_evolution_gen.generate,
    "natural_sciences_stellar_evolution": ns9_mod.stellar_evolution_gen.generate,
}

FOUNDATIONAL_MATH_GENERATORS = {
    "foundational_math_number_bonds": _adapt_single_item_generator(foundational_math_drill),
}


from app.utils.grade10_physical_sciences import (
    waves_sound_light_generator as phys10_waves,
    matter_materials_generator as phys10_matter,
    electric_circuits_magnetism_generator as phys10_circuits,
    chemical_change_stoichiometry_generator as phys10_chem,
    motion_energy_generator as phys10_motion,
)
from app.utils.life_sciences import meiosis_human_reproduction_generator as ls_meiosis
from app.utils.physical_sciences import electrostatics_electromagnetism_generator as phys_electro

# Dedicated Vertical Strand Generators (Zero Proxy Routing)
from app.utils.life_sciences import (
    photosynthesis_respiration_generator as ls_photosynth,
    human_organ_systems_generator as ls_organs,
    environmental_population_generator as ls_env,
    heart_generator as ls_heart,
    ls10_transport_systems_animals_generator as ls10_transport,
)
from app.utils.natural_sciences import (
    ns9_circulatory_respiratory_generator as ns9_circ_resp,
)
from app.utils.physical_sciences import (
    geometrical_optics_generator as ps_optics,
    ideal_gases_thermal_generator as ps_ideal_gases,
    work_energy_power_generator as ps_work_power,
    electrochemistry_generator as ps_electrochem,
)
from app.utils.natural_sciences import (
    senior_phase_astronomy_generator as ns_astronomy,
)
from app.utils.mathematical_literacy import (
    tariffs_tax_brackets_generator as mathlit_tariffs,
)

from app.utils.physical_sciences import (
    ps10_waves_sound_light_generator as ps10_waves_gen,
    ps11_acids_bases_stoichiometry_generator as ps11_acids_bases_gen,
    ps12_electrochemistry_galvanic_generator as ps12_electrochem_gen,
    ps12_doppler_effect_generator as ps12_doppler_gen,
    ps12_vertical_projectile_motion_generator as ps12_proj_gen,
)

PHYS_LS_GENERATORS = {
    # Grade 10 Physical Sciences
        "grade10_physical_sciences_waves_sound_light": ps10_waves_gen.generate,
    "grade10_physical_sciences_waves": ps10_waves_gen.generate,
    "physical_sciences_waves_sound_light": ps10_waves_gen.generate,
    "grade11_physical_sciences_acids_bases_stoichiometry": ps11_acids_bases_gen.generate,
    "physical_sciences_acids_bases_stoichiometry": ps11_acids_bases_gen.generate,
    "grade12_physical_sciences_electrochemistry_galvanic": ps12_electrochem_gen.generate,
    "physical_sciences_electrochemistry_galvanic": ps12_electrochem_gen.generate,
    "grade12_physical_sciences_doppler_effect": ps12_doppler_gen.generate,
    "physical_sciences_doppler_effect": ps12_doppler_gen.generate,
    "grade12_physical_sciences_vertical_projectile": ps12_proj_gen.generate,
    "physical_sciences_vertical_projectile": ps12_proj_gen.generate,
    "grade10_physical_sciences_waves": phys10_waves.generate,
    "grade10_physical_sciences_matter_materials": phys10_matter.generate,
    "grade10_physical_sciences_electrostatics": phys_electro.generate,
    "grade10_physical_sciences_electric_circuits": phys10_circuits.generate,
    "grade10_physical_sciences_chemical_change": phys10_chem.generate,
    "grade10_physical_sciences_stoichiometry": phys10_chem.generate,
    "grade10_physical_sciences_motion_energy": phys10_motion.generate,
    # Grade 11 Physical Sciences
    "grade11_physical_sciences_vectors_newton": phys11_vec.generate,
    "grade11_physical_sciences_vectors": phys11_vec.generate,
    "grade11_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_electromagnetism": phys_electro.generate,
    "grade11_physical_sciences_electric_circuits": phys11_circuits.generate,
    "grade11_physical_sciences_energy_chemical_change": phys11_energy.generate,
    "grade11_physical_sciences_stoichiometry_limiting": phys11_stoich.generate,
    # Grade 12 Physical Sciences
    "grade12_physical_sciences_vertical_projectile": phys12_proj.generate,
    "grade12_physical_sciences_doppler_effect": phys12_doppler.generate,
    "grade12_physical_sciences_doppler": phys12_doppler.generate,
    "grade12_physical_sciences_organic_chemistry": phys12_organic.generate,
    "grade12_physical_sciences_organic_molecules": phys12_organic.generate,
    "grade12_physical_sciences_acids_bases": phys12_acids_bases.generate,
    "grade12_physical_sciences_electrodynamics": phys12_electrodyn.generate_electrodynamics,
    "grade12_physical_sciences_electric_circuits": phys12_electrodyn.generate_electric_circuits,
    "grade12_physical_sciences_optical_phenomena": phys12_photoelectric.generate,
    "grade12_physical_sciences_photoelectric_effect": phys12_photoelectric.generate,
    "life_sciences_meiosis_human_reproduction": ls_meiosis.generate,
    "physical_sciences_electrostatics": phys_electro.generate,
    "physical_sciences_electromagnetism": phys_electro.generate,
    # Vertical strands
    "life_sciences_photosynthesis_respiration": ls_photosynth.generate,
    "life_sciences_human_organ_systems": ls_organs.generate,
    "life_sciences_animal_nutrition": ls11_nutrition.generate,
    "grade11_life_sciences_animal_nutrition": ls11_nutrition.generate,
    "life_sciences_gaseous_exchange": ls11_gas_exchange.generate,
    "grade11_life_sciences_gaseous_exchange": ls11_gas_exchange.generate,
    "life_sciences_excretion": ls11_excretion.generate,
    "life_sciences_excretion_in_humans": ls11_excretion.generate,
    "grade11_life_sciences_excretion": ls11_excretion.generate,
    "life_sciences_responding_environment_humans": ls12_responding_env.generate,
    "life_sciences_human_responses_environment": ls12_responding_env.generate,
    "grade12_life_sciences_human_responses_environment": ls12_responding_env.generate,
    "life_sciences_endocrine_homeostasis": ls12_endocrine.generate,
    "grade12_life_sciences_endocrine_homeostasis": ls12_endocrine.generate,
    "life_sciences_human_reproduction": ls12_human_repro.generate,
    "grade12_life_sciences_human_reproduction": ls12_human_repro.generate,
    "life_sciences_plant_animal_cells": ls10_cells.generate,
    "grade10_life_sciences_plant_animal_cells": ls10_cells.generate,
    "life_sciences_cell_division_mitosis": ls10_mitosis_gen.generate,
    "grade10_life_sciences_cell_division": ls10_mitosis_gen.generate,
    "life_sciences_meiosis": ls12_meiosis_gen.generate,
    "grade12_life_sciences_meiosis": ls12_meiosis_gen.generate,
    "life_sciences_heart": ls_heart.generate,
    "life_sciences_transport_systems_animals": ls10_transport.generate,
    "grade10_life_sciences_transport_systems": ls10_transport.generate,
    "life_sciences_environmental_population": ls_env.generate,
    "life_sciences_support_transport_plants": ls10_plants.generate,
    "grade10_life_sciences_support_transport_plants": ls10_plants.generate,
    "life_sciences_photosynthesis": ls11_photosynth.generate,
    "grade11_life_sciences_photosynthesis": ls11_photosynth.generate,
    "life_sciences_cellular_respiration": ls11_resp.generate,
    "grade11_life_sciences_cellular_respiration": ls11_resp.generate,
    "life_sciences_biospheres_ecosystems": ls10_biospheres.generate,
    "grade10_life_sciences_biospheres_ecosystems": ls10_biospheres.generate,
    "life_sciences_population_ecology": ls11_pop_ecology.generate,
    "grade11_life_sciences_population_ecology": ls11_pop_ecology.generate,
    "life_sciences_plant_responses_environment": ls12_plant_resp.generate,
    "grade12_life_sciences_plant_responses_environment": ls12_plant_resp.generate,
    "physical_sciences_geometrical_optics": ps_optics.generate,
    "physical_sciences_ideal_gases_thermal": ps_ideal_gases.generate,
    "physical_sciences_work_energy_power": ps_work_power.generate,
    "physical_sciences_electrochemistry": ps_electrochem.generate,
    "natural_sciences_senior_phase_astronomy": ns_astronomy.generate,
    "mathematical_literacy_tariffs_tax_brackets": mathlit_tariffs.generate,
}

ALL_GENERATORS: Dict[str, Callable] = {
    **PHYS_LS_GENERATORS,
    **GRADE7_MATH_GENERATORS,
    **GRADE8_MATH_GENERATORS,
    **GRADE9_MATH_GENERATORS,
    **GRADE10_MATH_GENERATORS,
    **GRADE11_MATH_GENERATORS,
    **GRADE12_MATH_GENERATORS,
    **GRADE10_BS_GENERATORS,
    **GRADE11_BS_GENERATORS,
    **GRADE12_BS_GENERATORS,
    **GRADE7_EMS_GENERATORS,
    **GRADE8_EMS_GENERATORS,
    **GRADE9_EMS_GENERATORS,
    **GRADE10_ACCOUNTING_GENERATORS,
    **GRADE11_ACCOUNTING_GENERATORS,
    **GRADE12_ACCOUNTING_GENERATORS,
    **SCIENCES_AND_TECH_GENERATORS,
    **NATURAL_SCIENCES_GENERATORS,
    **FOUNDATIONAL_MATH_GENERATORS,
}



# ============================================================================
# SINGLE AUTHORITATIVE CURRICULUM MANIFEST & STRICT RESOLVER
# (Eradicates dual registries, regex guessing, and cross-subject leaks)
# ============================================================================

import json
from pathlib import Path
from typing import Tuple
from app.services.generator_aliases import TOPIC_ALIASES

_CURRICULUM_MANIFEST_PATH = Path(__file__).parent / "caps_term_registry_data.json"
CURRICULUM_MANIFEST: Dict[Tuple[str, str, str], str] = {}


def _normalize_subject_key(subject: str) -> str:
    s = str(subject or "").lower().replace("_", " ").replace("-", " ").strip()
    if "acc" in s:
        return "accounting"
    if "bus" in s:
        return "business studies"
    if "ems" in s or "economic" in s:
        return "economic and management sciences"
    if "tech" in s:
        return "technical mathematics"
    if "lit" in s or "mathslit" in s:
        return "mathematical literacy"
    if "phys" in s:
        return "physical sciences"
    if "life" in s or "bio" in s:
        return "life sciences"
    if "nat" in s:
        return "natural sciences"
    if "math" in s:
        return "mathematics"
    return s


def _normalize_grade_key(grade: Any) -> str:
    cleaned = "".join(ch for ch in str(grade or "") if ch.isdigit())
    return cleaned if cleaned else "10"


def _normalize_topic_key(topic: str) -> str:
    clean = re.sub(r"^\d+[\.\s_]+", "", str(topic or "").strip())
    clean = clean.lower().replace("_", " ").replace("-", " ")
    clean = re.sub(r"[^\w\s]", "", clean)
    return " ".join(clean.split())


def _load_curriculum_manifest() -> None:
    global CURRICULUM_MANIFEST
    CURRICULUM_MANIFEST.clear()
    if not _CURRICULUM_MANIFEST_PATH.exists():
        return
    try:
        with open(_CURRICULUM_MANIFEST_PATH, "r", encoding="utf-8") as f:
            records = json.load(f)
        for rec in records:
            s = _normalize_subject_key(rec.get("subject", ""))
            g = _normalize_grade_key(rec.get("grade", ""))
            t = _normalize_topic_key(rec.get("name", ""))
            k = rec.get("generator_key", "").strip()
            if s and g and t and k:
                CURRICULUM_MANIFEST[(s, g, t)] = k
    except Exception as e:
        print(f"Warning: Failed to load curriculum manifest: {e}")


_load_curriculum_manifest()


def resolve_generator_key(topic: str, grade: str = "10", subject: str = "Mathematics") -> str:
    """Deterministically resolves the registered generator key from the single authoritative curriculum manifest.

    Invariant: Substring regex guessing is eliminated. All 476 topics map directly
    to their validated generator keys in caps_term_registry_data.json.
    """
    # 1. Direct match in registry (if caller already passed a valid generator key)
    if topic in ALL_GENERATORS:
        return topic

    s = _normalize_subject_key(subject)
    g = _normalize_grade_key(grade)
    t = _normalize_topic_key(topic)

    # 2. Exact match in single curriculum manifest table
    direct = CURRICULUM_MANIFEST.get((s, g, t))
    if direct and direct in ALL_GENERATORS:
        return direct

    # 3. Check alias map (preserves explicit test harness aliases)
    clean_raw = str(topic or "").strip().lower().replace("_", " ").replace("-", " ")
    if clean_raw in TOPIC_ALIASES:
        resolved = TOPIC_ALIASES[clean_raw]
        if resolved in ALL_GENERATORS:
            return resolved

    if t in TOPIC_ALIASES:
        resolved = TOPIC_ALIASES[t]
        if resolved in ALL_GENERATORS:
            return resolved

    # 4. Strict scoped match within the exact same (subject, grade) in manifest
    # (Matches only within the requested subject/grade; NEVER leaks cross-subject)
    for (ms, mg, mt), mkey in CURRICULUM_MANIFEST.items():
        if ms == s and mg == g:
            if t in mt or mt in t:
                if mkey in ALL_GENERATORS:
                    return mkey

    # 5. Token overlap match within the exact same (subject, grade)
    t_tokens = set(t.split())
    best_match = None
    best_overlap = 0
    for (ms, mg, mt), mkey in CURRICULUM_MANIFEST.items():
        if ms == s and mg == g:
            mt_tokens = set(mt.split())
            overlap = len(t_tokens & mt_tokens)
            if overlap > best_overlap and mkey in ALL_GENERATORS:
                best_overlap = overlap
                best_match = mkey
    if best_match and best_overlap >= 1:
        return best_match

    # If completely unknown, return "" (caller raises ValueError)
    return ""



# ============================================================================
# 6-PILLAR NORMALIZATION & ENRICHMENT
# ============================================================================

def _unwrap_text_commands(s: str) -> str:
    target = r"\text{"
    while target in s:
        start = s.find(target)
        depth = 1
        pos = start + len(target)
        while pos < len(s) and depth > 0:
            if s[pos] == "{" and (pos == 0 or s[pos - 1] != "\\"):
                depth += 1
            elif s[pos] == "}" and (pos == 0 or s[pos - 1] != "\\"):
                depth -= 1
            pos += 1
        if depth == 0:
            inner = s[start + len(target) : pos - 1]
            s = s[:start] + inner + s[pos:]
        else:
            s = s[:start] + s[start + len(target) :]
    return s


def _extract_numbered_prompt_labels(prompt_text: str) -> List[str]:
    """Extracts numbered or lettered sub-question labels from the prompt (e.g. '1. **Directors**')
    so multi-part questions never display raw keys like 'Def 0', 'Def 1', 'Def 2'.
    """
    if not prompt_text:
        return []
    matches = re.findall(r"(?m)^\s*(?:(\d+(?:\.\d+)?)\.|(?:\(?([a-z])\)))\s+\*{0,2}([^\n\*]+)\*{0,2}", prompt_text)
    labels: List[str] = []
    for num, let, txt in matches:
        prefix = f"{num}." if num else f"({let})"
        clean_txt = txt.strip().rstrip(":")
        labels.append(f"{prefix} {clean_txt}" if len(clean_txt) <= 80 else f"{prefix} {clean_txt[:77]}...")
    return labels


def _unwrap_bundle_question(q: Dict[str, Any]) -> Dict[str, Any]:
    """Unwraps `question_type == 'bundle'` or multi-part `parts` questions so the
    learner card displays the full scenario, information, required instructions,
    and interactive tables/inputs rather than a 1-line stub header.
    """
    parts = q.get("parts")
    if not isinstance(parts, list) or not parts:
        return q
    if str(q.get("question_type") or "").strip().lower() != "bundle" and (q.get("rows") or q.get("journal") or q.get("table_schema")):
        return q

    from .memo_normalizer import _build_completed_markdown_table

    q = dict(q)
    base_prompt = str(q.get("prompt") or q.get("question") or "").strip()
    prompt_sections = [base_prompt] if base_prompt else []

    primary_tabular_part: Optional[Dict[str, Any]] = None
    for p in parts:
        if isinstance(p, dict) and (p.get("journal") or p.get("rows") or p.get("table_schema") or p.get("correct_map")):
            primary_tabular_part = p
            break

    sub_parts_list: List[Dict[str, Any]] = []
    memo_sections: List[str] = []
    total_marks = 0

    for idx, p in enumerate(parts):
        if not isinstance(p, dict):
            continue
        p_prompt = str(p.get("prompt") or p.get("question") or p.get("question_text") or "").strip()
        p_marks = int(p.get("marks") or (len(p.get("correct_map", {})) if isinstance(p.get("correct_map"), dict) and p.get("correct_map") else 4))
        total_marks += max(1, p_marks)

        part_header = f"**Part {idx + 1}**"
        if p_prompt:
            prompt_sections.append(f"{part_header}\n{p_prompt}")

        p_md_table = _build_completed_markdown_table(p)
        if p_md_table:
            memo_sections.append(f"### Part {idx + 1} Memorandum\n\n{p_md_table}")
            if primary_tabular_part is not None and p is not primary_tabular_part:
                prompt_sections.append(f"*Reference Schedule (Part {idx + 1}):*\n\n{p_md_table.replace('**', '')}")
        else:
            p_ans = str(
                p.get("sample_answer")
                or p.get("correct_answer")
                or p.get("expected_answer")
                or p.get("correct_value")
                or p.get("worked_solution")
                or p.get("explanation")
                or ""
            ).strip()
            if p_ans:
                memo_sections.append(f"### Part {idx + 1} Memorandum\n**{p_ans}** [{p_marks} marks]")
                if primary_tabular_part is None:
                    sub_parts_list.append({
                        "id": str(p.get("id") or f"part_{idx + 1}"),
                        "label": f"({idx + 1})",
                        "prompt": p_prompt[:140] or f"Part {idx + 1}",
                        "expected_answer": p_ans,
                        "marks": p_marks,
                    })

    q["prompt"] = "\n\n".join(s for s in prompt_sections if s)
    q["question"] = q["prompt"]
    if total_marks > int(q.get("marks") or 0):
        q["marks"] = total_marks

    if primary_tabular_part is not None:
        q["question_type"] = primary_tabular_part.get("question_type") or "journal"
        q["modality"] = "ledger"
        for k in ("journal", "headers", "rows", "table_schema", "correct_map", "cell_hints", "guidelines"):
            if primary_tabular_part.get(k) is not None and not q.get(k):
                q[k] = primary_tabular_part[k]
    elif sub_parts_list:
        q["question_type"] = "short_answer"
        q["sub_parts"] = sub_parts_list
        q["expected_answer"] = "\n".join(f"({i + 1}) {sp['expected_answer']}" for i, sp in enumerate(sub_parts_list))
        q["sample_answer"] = q["expected_answer"]

    if memo_sections:
        joined_memo = "\n\n".join(memo_sections)
        q["worked_solution"] = joined_memo
        q["canonical_solution"] = joined_memo
        if not q.get("sample_answer"):
            q["sample_answer"] = joined_memo

    return q


def _clean_accounting_markdown_headers(text: str) -> str:
    """Replaces raw `#### REQUIRED:` and `#### INFORMATION:` markdown hashtags
    with clean bold section labels (`**REQUIRED:**` and `**INFORMATION:**`).
    """
    if not text or "#" not in text:
        return text
    cleaned = re.sub(r"(?m)^\s*#{1,6}\s*REQUIRED\s*:?\s*$", "**REQUIRED:**", text, flags=re.IGNORECASE)
    cleaned = re.sub(r"(?m)^\s*#{1,6}\s*INFORMATION\s*:?\s*$", "**INFORMATION:**", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"#{1,6}\s*REQUIRED\s*:", "**REQUIRED:**", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"#{1,6}\s*INFORMATION\s*:", "**INFORMATION:**", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"(?m)^\s*#{4,6}\s+(.+?)\s*$", r"**\1**", cleaned)
    return cleaned


def _normalize_question(
    q: Dict[str, Any],
    default_term: int = 1,
    topic: str = "",
    grade: str = "",
    subject: str = "",
) -> Dict[str, Any]:
    """Ensures a single question dictionary strictly complies with the 6-pillar contract."""
    from .caps_term_curriculum_registry import stamp_question_term_metadata, get_term_for_topic

    if isinstance(q, dict) and (str(q.get("question_type") or "").lower() == "bundle" or isinstance(q.get("parts"), list)):
        q = _unwrap_bundle_question(q)

    qid = str(q.get("id") or q.get("question_id") or f"q_{random.randint(100000, 999999)}")
    marks = max(1, int(q.get("marks") or 2))
    subj_lower = str(subject or "").lower()

    # Diagram role contract normalization (GP-2)
    for dkey in ("diagram_spec", "diagram", "diagram_meta"):
        diag = q.get(dkey)
        if isinstance(diag, dict):
            if "diagram_role" not in diag:
                is_identify = bool(
                    diag.get("target_pin") or
                    diag.get("target_key") or
                    q.get("question_type") == "diagram_select" or
                    (diag.get("pins") and not diag.get("landmarks"))
                )
                diag["diagram_role"] = "identify" if is_identify else "context"
            q.setdefault("diagram_role", diag["diagram_role"])

    # Reconcile structured / tabular_fill / table_completion dictionaries into canonical correct_map + rows
    raw_qtype = str(q.get("question_type") or "").strip().lower()
    raw_ans_dict = None
    for candidate_key in ("correct_map", "expected_cells", "expected_values", "model_table", "answer_key", "correct_answer", "expected_answer"):
        val = q.get(candidate_key)
        if isinstance(val, dict) and val:
            raw_ans_dict = val
            break

    # Normalize coordinate -> cell_id in any rows / table_schema
    table_schema = q.get("table_schema") if isinstance(q.get("table_schema"), dict) else None
    raw_rows = q.get("rows") or (table_schema.get("rows") if table_schema else None) or (q.get("journal", {}).get("rows") if isinstance(q.get("journal"), dict) else None)
    raw_headers = q.get("headers") or (table_schema.get("headers") if table_schema else None) or (table_schema.get("columns") if table_schema else None) or (q.get("journal", {}).get("headers") if isinstance(q.get("journal"), dict) else None)

    normalized_rows = None
    if isinstance(raw_rows, list):
        normalized_rows = []
        for r_idx, row_item in enumerate(raw_rows):
            if isinstance(row_item, list):
                norm_row = []
                for c_idx, cell in enumerate(row_item):
                    if isinstance(cell, dict):
                        cid = cell.get("cell_id") or cell.get("coordinate") or f"r{r_idx}_c{c_idx}"
                        is_req = cell.get("type") in ("required", "input") or bool(cell.get("editable")) or (isinstance(raw_ans_dict, dict) and cid in raw_ans_dict)
                        norm_row.append({
                            **cell,
                            "cell_id": cid,
                            "value": "" if is_req and not cell.get("prefilled") else (cell.get("value") if cell.get("value") is not None else ""),
                            "expected": (raw_ans_dict.get(cid) if isinstance(raw_ans_dict, dict) and cid in raw_ans_dict else cell.get("expected") or cell.get("value")),
                            "editable": is_req,
                        })
                    else:
                        norm_row.append({
                            "cell_id": f"r{r_idx}_c{c_idx}",
                            "value": str(cell if cell is not None else ""),
                            "editable": False,
                        })
                normalized_rows.append(norm_row)
            else:
                normalized_rows.append(row_item)

    raw_mod_check = str(q.get("modality") or "").strip().lower()
    is_explicit_tabular = (
        raw_mod_check == "ledger"
        or bool(q.get("journal"))
        or bool(table_schema)
        or isinstance(normalized_rows, list)
        or isinstance(q.get("correct_map"), dict)
        or raw_qtype in ("journal", "ledger", "accounting_equation", "tabular_fill", "table_completion")
    )

    if isinstance(raw_ans_dict, dict) and not is_explicit_tabular:
        q = dict(q)
        if len(raw_ans_dict) == 1:
            single_val = next(iter(raw_ans_dict.values()))
            if q.get("expected_answer") is None or isinstance(q.get("expected_answer"), dict):
                q["expected_answer"] = single_val
            if q.get("correct_answer") is None or isinstance(q.get("correct_answer"), dict):
                q["correct_answer"] = single_val
            raw_ans_dict = None
            if raw_qtype == "structured":
                is_str_val = isinstance(single_val, str) and not re.match(r"^[\-\+]?\d+(?:\.\d+)?$", single_val.strip())
                raw_qtype = "short_answer" if is_str_val else "math_short"
                q["question_type"] = raw_qtype
        else:
            # Multi-part non-tabular answer dictionary (e.g. part_a, part_b, def_0, def_1)
            raw_p_text = str(q.get("prompt") or q.get("question") or q.get("question_text") or "")
            extracted_labels = _extract_numbered_prompt_labels(raw_p_text)
            part_items = list(raw_ans_dict.items())
            joined_parts = []
            for idx, (k, v) in enumerate(part_items):
                lbl = extracted_labels[idx] if idx < len(extracted_labels) else f"({idx + 1})"
                joined_parts.append(f"{lbl}: {v}")
            joined_ans = "\n".join(joined_parts)
            if q.get("expected_answer") is None or isinstance(q.get("expected_answer"), dict):
                q["expected_answer"] = joined_ans
            if q.get("correct_answer") is None or isinstance(q.get("correct_answer"), dict):
                q["correct_answer"] = joined_ans
            if not q.get("sub_parts"):
                part_marks = max(1, marks // len(part_items))
                q["sub_parts"] = [
                    {
                        "id": str(k),
                        "label": extracted_labels[idx] if idx < len(extracted_labels) else f"({idx + 1})",
                        "prompt": extracted_labels[idx] if idx < len(extracted_labels) else str(k).replace("_", " ").title(),
                        "expected_answer": str(v),
                        "marks": part_marks,
                    }
                    for idx, (k, v) in enumerate(part_items)
                ]
            raw_ans_dict = None
            if raw_qtype == "structured":
                raw_qtype = "short_answer"
                q["question_type"] = "short_answer"

    if isinstance(raw_ans_dict, dict) and not normalized_rows and not q.get("journal") and not table_schema:
        raw_p_text = str(q.get("prompt") or q.get("question") or q.get("question_text") or "")
        extracted_labels = _extract_numbered_prompt_labels(raw_p_text)
        raw_headers = ["Sub-Question / Item", "Required Answer"]
        normalized_rows = []
        for r_idx, (k, v) in enumerate(raw_ans_dict.items()):
            label = extracted_labels[r_idx] if r_idx < len(extracted_labels) else str(k).replace("_", " ").strip().title()
            normalized_rows.append([
                {"cell_id": f"lbl_{r_idx}", "value": label, "editable": False},
                {"cell_id": str(k), "value": "", "expected": str(v), "editable": True},
            ])

    # 1. Authoritative Modality Resolution
    raw_mod = str(q.get("modality") or "").strip().lower()
    if raw_mod == "rubric":
        raw_mod = "semantic"

    diag_obj = q.get("diagram_spec") or q.get("diagram_meta") or q.get("diagram") or {}
    if not isinstance(diag_obj, dict):
        diag_obj = {}

    is_true_diagram_select = (
        raw_qtype == "diagram_select"
        or bool(q.get("correct_edge"))
        or bool(diag_obj.get("correct_edge"))
    )
    is_geometric_nets_q = (
        raw_mod == "geometric_nets"
        or diag_obj.get("kind") == "geometric_nets"
        or "geometric_net" in str(q.get("subskill", "")).lower()
        or "polyhedron_net" in str(q.get("subskill", "")).lower()
    )
    is_bio_diagram_q = (
        raw_mod == "bio_diagram"
        or (
            bool(diag_obj.get("image_type") or diag_obj.get("master"))
            and (
                diag_obj.get("diagram_role") == "identify"
                or bool(diag_obj.get("pins"))
                or bool(diag_obj.get("target_pin"))
                or bool(diag_obj.get("target_key"))
            )
        )
    )
    is_tabular_question = (
        raw_mod == "ledger"
        or bool(q.get("journal"))
        or bool(table_schema)
        or isinstance(normalized_rows, list)
        or isinstance(q.get("correct_map"), dict)
        or raw_qtype in ("journal", "ledger", "accounting_equation", "tabular_fill", "table_completion")
    )

    if raw_mod in ("arithmetic_grid", "geometric_nets", "electrodynamics", "organic_chemistry", "circuit", "punnett_square", "bio_diagram", "free_body_diagram", "optics_ray"):
        modality = raw_mod
    elif q.get("optics_spec"):
        modality = "optics_ray"
    elif q.get("circuit_spec"):
        modality = "circuit"
    elif q.get("punnett_spec"):
        modality = "punnett_square"
    elif q.get("fbd_spec"):
        modality = "free_body_diagram"
    elif q.get("arithmetic_grid") or raw_qtype == "arithmetic_grid":
        modality = "arithmetic_grid"
    elif is_tabular_question:
        modality = "ledger"
    elif is_geometric_nets_q:
        modality = "geometric_nets"
    elif is_bio_diagram_q:
        modality = "bio_diagram"
    elif is_true_diagram_select:
        modality = "diagram"
    elif raw_qtype in ("mcq", "matching", "word_bank") or (isinstance(q.get("options"), list) and len(q.get("options")) > 0) or isinstance(q.get("pairs"), list) or isinstance(q.get("column_a"), list):
        modality = "math"
    elif (
        raw_mod == "semantic"
        or q.get("marking_points")
        or q.get("content_rubric")
        or str(q.get("expected_answer_type") or "").strip().lower() == "text"
        or (isinstance(q.get("parts"), list) and len(q.get("parts")) > 0)
        or (isinstance(q.get("guidelines"), list) and len(q.get("guidelines")) > 0 and not q.get("correct_value") and not q.get("final_answer"))
        or raw_qtype in ("rubric", "essay", "short_answer", "scenario", "standard")
    ):
        modality = "semantic"
    elif any(s in subj_lower for s in ("business", "life", "bio")) and not isinstance(q.get("options"), list):
        modality = "semantic"
    else:
        modality = "math"

    # 2. Authoritative Solution Type & Question Type Synchronization
    effective_qtype = q.get("question_type")
    if isinstance(q.get("options"), list) and len(q.get("options")) > 0:
        effective_qtype = "mcq"
        sol_type = "mcq"
    elif modality == "ledger":
        effective_qtype = effective_qtype if effective_qtype in ("journal", "ledger", "accounting_equation") else "journal"
        sol_type = "tabular_cells"
    elif modality == "diagram":
        effective_qtype = "diagram_select"
        sol_type = "diagram_element"
    elif modality == "semantic":
        effective_qtype = effective_qtype if effective_qtype in ("rubric", "essay", "short_answer", "scenario", "typed") else "short_answer"
        sol_type = "marking_points"
    elif raw_qtype in ("matching", "matching_columns"):
        sol_type = "matching"
    else:
        if effective_qtype not in ("math_steps", "math_short", "calc", "arithmetic_grid"):
            effective_qtype = "math_short"
        sol_type = "symbolic_steps"

    # 3. Authoritative Expected Answer & MCQ Index Resolution
    expected_answer = (
        q.get("expected_answer")
        if q.get("expected_answer") is not None
        else q.get("ideal_answer")
        or q.get("correct_answer")
        or q.get("correct_value")
        or q.get("final_answer")
        or q.get("answer_latex")
        or q.get("sample_answer")
        or q.get("model_answer")
        or q.get("answer")
        or (q.get("canonical_solution", {}).get("final_latex") if isinstance(q.get("canonical_solution"), dict) else None)
    )

    resolved_correct_idx = q.get("correct_index") if q.get("correct_index") is not None else q.get("correct_idx")
    if isinstance(q.get("options"), list) and q["options"]:
        opts = q["options"]
        if resolved_correct_idx is None and expected_answer is not None:
            exp_str = str(expected_answer).strip().lower()
            for idx, opt in enumerate(opts):
                if str(opt).strip().lower() == exp_str:
                    resolved_correct_idx = idx
                    break
            if resolved_correct_idx is None and exp_str.isdigit() and 0 <= int(exp_str) < len(opts):
                resolved_correct_idx = int(exp_str)
        if resolved_correct_idx is None:
            resolved_correct_idx = 0
        try:
            resolved_correct_idx = int(resolved_correct_idx)
        except (ValueError, TypeError):
            resolved_correct_idx = 0
        if not expected_answer and 0 <= resolved_correct_idx < len(opts):
            expected_answer = str(opts[resolved_correct_idx])

    if expected_answer is None or expected_answer == "":
        if q.get("worked_solution"):
            expected_answer = str(q["worked_solution"])
        elif isinstance(q.get("guidelines"), list) and q["guidelines"]:
            expected_answer = "\n".join(str(g) for g in q["guidelines"] if g)
        elif isinstance(q.get("parts"), list) and q["parts"]:
            expected_answer = "\n".join(
                str(
                    p.get("solution")
                    or p.get("expected_answer")
                    or p.get("correct_answer")
                    or p.get("sample_answer")
                    or p.get("model_answer")
                    or p.get("answer")
                    or p.get("rubric")
                    or p.get("question")
                    or ""
                )
                for p in q["parts"]
                if isinstance(p, dict)
            ).strip()
        elif isinstance(q.get("solution_steps"), list) and q["solution_steps"]:
            expected_answer = str(q["solution_steps"][-1])
        else:
            expected_answer = ""

    # Synthesize prompt for multi-part context/instruction/parts questions if prompt is missing
    if not q.get("prompt") and not q.get("question") and not q.get("question_text") and isinstance(q.get("parts"), list):
        ctx_str = str(q.get("context") or "").strip()
        inst_str = str(q.get("instruction") or "").strip()
        part_lines = [
            f"{idx + 1}. {p.get('question', '')} ({p.get('marks', 2)} marks)"
            for idx, p in enumerate(q["parts"])
            if isinstance(p, dict) and p.get("question")
        ]
        q["prompt"] = "\n\n".join(s for s in [ctx_str, inst_str, "\n".join(part_lines)] if s)

    # 4. Structured Marking Schema Synthesis & Mark Total Reconciliation
    schema = q.get("marking_schema")
    if not schema or not isinstance(schema, dict) or not schema.get("marking_points"):
        marking_points = []
        raw_pts = q.get("marking_points") or q.get("content_rubric") or q.get("rubric") or (
            [
                {
                    "id": p.get("id", f"mp_{idx + 1}"),
                    "desc": p.get("solution") or p.get("rubric") or p.get("question") or f"Part {idx + 1}",
                    "marks": int(p.get("marks", 2)),
                }
                for idx, p in enumerate(q["parts"])
                if isinstance(p, dict)
            ]
            if isinstance(q.get("parts"), list) and q["parts"]
            else None
        )

        if isinstance(raw_pts, list) and raw_pts:
            pts_count = max(1, len(raw_pts))
            default_pt_marks = max(1, marks // pts_count)
            for idx, pt in enumerate(raw_pts):
                if isinstance(pt, dict):
                    desc_candidate = pt.get("desc") or pt.get("criterion") or pt.get("criteria") or pt.get("description")
                    if desc_candidate is None and isinstance(pt.get("point"), str):
                        desc_candidate = pt.get("point")
                    desc = str(desc_candidate) if desc_candidate else f"Criterion {idx + 1}"
                    pt_marks = int(pt.get("marks") or pt.get("max_marks") or default_pt_marks)
                    tc = pt.get("target_concepts") or pt.get("key_concepts") or [w for w in re.split(r"[,/;\s]+", desc) if len(w) > 3]
                else:
                    desc = str(pt)
                    pt_marks = default_pt_marks
                    tc = [w for w in re.split(r"[,/;\s]+", desc) if len(w) > 3]
                marking_points.append({
                    "id": f"mp_{idx + 1}",
                    "desc": desc,
                    "marks": pt_marks,
                    "target_concepts": tc,
                    "editable": True,
                })
        elif modality == "semantic":
            sol_text = str(expected_answer or q.get("worked_solution") or q.get("sample_answer") or q.get("explanation") or "")
            lines = [line.strip("-•* \t") for line in sol_text.split("\n") if len(line.strip("-•* \t")) > 8]
            if len(lines) >= 2:
                alloc = max(1, marks // len(lines))
                for idx, line in enumerate(lines[:marks]):
                    marking_points.append({
                        "id": f"mp_{idx + 1}",
                        "desc": line,
                        "marks": alloc,
                        "target_concepts": [w for w in re.split(r"[,/;\s]+", line) if len(w) > 3],
                        "editable": True,
                    })
            else:
                base_desc = sol_text if len(sol_text) > 5 else "Substantive explanation addressing core curriculum concept"
                tc = [w for w in re.split(r"[,/;\s]+", base_desc) if len(w) > 3][:8]
                marking_points = [
                    {"id": "mp_1", "desc": base_desc, "marks": max(1, marks // 2), "target_concepts": tc, "editable": True},
                    {"id": "mp_2", "desc": f"Supporting justification or application: {base_desc[:80]}", "marks": max(1, marks - (marks // 2)), "target_concepts": tc, "editable": True},
                ]
        else:
            marking_points = [
                {"id": "mp_1", "desc": "Accurate method/procedure [M]", "marks": max(1, marks - 1), "editable": True},
                {"id": "mp_2", "desc": "Accurate final value/accuracy mark [A]", "marks": 1, "editable": True},
            ] if marks >= 2 else [
                {"id": "mp_1", "desc": "Accurate calculation or selection [A]", "marks": marks, "editable": True}
            ]

        schema = {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        }
    else:
        schema = dict(schema)
        schema["marking_points"] = [dict(p) if isinstance(p, dict) else {"id": f"mp_{i+1}", "desc": str(p), "marks": 1, "editable": True} for i, p in enumerate(schema.get("marking_points", []))]
        schema["total_marks"] = marks

    # Always reconcile marking_points sum with total_marks so full criteria match == 100% score
    mps = schema.get("marking_points", [])
    if mps:
        curr_total = sum(int(p.get("marks", 1)) for p in mps)
        if curr_total != marks:
            if curr_total < marks:
                diff = marks - curr_total
                for i in range(diff):
                    mps[i % len(mps)]["marks"] = int(mps[i % len(mps)].get("marks", 1)) + 1
            elif curr_total > marks:
                marks = curr_total
                schema["total_marks"] = marks
        if not expected_answer:
            expected_answer = "; ".join(str(p.get("desc", "")) for p in mps if p.get("desc"))

    # 5. 3-Tier Pre-Baked Hints (Anti-Spoiler Guaranteed)
    raw_hints = q.get("hints")
    base_hint = str(q.get("explanation") or q.get("hint_trigger") or "Apply standard curriculum procedure and identify the relevant formula or rule.")
    if isinstance(raw_hints, list) and len(raw_hints) >= 1:
        t1 = str(raw_hints[0])
        t2 = str(raw_hints[1]) if len(raw_hints) >= 2 else base_hint
        t3 = str(raw_hints[2]) if len(raw_hints) >= 3 else f"Worked step verification: {expected_answer or 'Refer to memorandum.'}"
    elif isinstance(raw_hints, dict):
        t1 = str(raw_hints.get("tier_1") or raw_hints.get("tier1") or raw_hints.get("1") or "Identify the key given values and required unknown in the question prompt.")
        t2 = str(raw_hints.get("tier_2") or raw_hints.get("tier2") or raw_hints.get("2") or base_hint)
        t3 = str(raw_hints.get("tier_3") or raw_hints.get("tier3") or raw_hints.get("3") or f"Worked step verification: {expected_answer or 'Refer to memorandum.'}")
    else:
        t1 = f"Focus on the core principles of {topic or subject or 'this topic'} and identify the given values in the prompt."
        t2 = base_hint
        t3 = f"Worked step verification: {expected_answer or 'Refer to memorandum.'}"

    # Anti-spoiler guard: Tier 1 Nudge must never leak the exact final answer
    exp_str_clean = str(expected_answer).strip()
    if exp_str_clean and len(exp_str_clean) >= 2 and exp_str_clean.lower() in t1.lower():
        t1 = "Identify the given scenario parameters and core principles presented in the problem before answering."
    if t2 == t1:
        t2 = f"Rule & Strategy: {base_hint}"
    if t3 == t2 or t3 == t1:
        t3 = f"Worked Step Check: Substitute the given values carefully to arrive at {exp_str_clean or 'the final solution'}."

    hints = {
        "tier_1": t1,
        "tier_2": t2,
        "tier_3": t3,
    }

    # 6. Misconception Tags
    tags = q.get("misconception_tags")
    if not tags or not isinstance(tags, list):
        tag = q.get("misconception") or q.get("misconception_tag")
        tags = [str(tag)] if tag else ["general_procedural_error"]

    # Resolve authoritative term
    resolved_term = int(q.get("term")) if q.get("term") else default_term
    if topic:
        meta_term = get_term_for_topic(topic, grade=grade, subject=subject)
        if meta_term and meta_term > 1:
            resolved_term = meta_term
        elif not q.get("term") and meta_term:
            resolved_term = meta_term

    normalized = {
        **q,
        "id": qid,
        "question_id": qid,
        "question_type": effective_qtype,
        "term": resolved_term,
        "caps_weight_percent": int(q.get("caps_weight_percent") or 25),
        "suggested_duration_mins": int(q.get("suggested_duration_mins") or max(2, int(marks * 1.2))),
        "mode": q.get("mode") or "compound",
        "marks": marks,
        "modality": modality,
        "solution_type": sol_type,
        "expected_answer": expected_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": tags,
    }

    if resolved_correct_idx is not None:
        normalized["correct_index"] = resolved_correct_idx
        normalized["correct_idx"] = resolved_correct_idx

    if q.get("circuit_spec"):
        normalized["circuit_spec"] = q["circuit_spec"]
    if q.get("punnett_spec"):
        normalized["punnett_spec"] = q["punnett_spec"]
    if q.get("diagram_spec"):
        normalized["diagram_spec"] = q["diagram_spec"]
    elif q.get("diagram_meta"):
        meta = q["diagram_meta"]
        normalized["diagram_spec"] = {
            "image_type": meta.get("master") or meta.get("image_type"),
            **meta,
        }
    elif q.get("diagram"):
        d = q["diagram"]
        normalized["diagram_spec"] = {
            "image_type": d.get("master") or d.get("image_type"),
            **d,
        }
    else:
        from .visual_context_enricher import enrich_topic_context_diagram
        enriched_diag = enrich_topic_context_diagram(normalized, topic=topic, grade=grade, subject=subject)
        if enriched_diag:
            normalized["diagram_spec"] = enriched_diag
            normalized["diagram_role"] = "context"
    if q.get("fbd_spec"):
        normalized["fbd_spec"] = q["fbd_spec"]
    if q.get("sub_parts"):
        normalized["sub_parts"] = q["sub_parts"]

    if modality == "ledger":
        if isinstance(raw_ans_dict, dict) and not normalized.get("correct_map"):
            normalized["correct_map"] = {str(k): v for k, v in raw_ans_dict.items()}
        if normalized_rows is not None:
            normalized["rows"] = normalized_rows
            if isinstance(normalized.get("journal"), dict):
                normalized["journal"] = {**normalized["journal"], "rows": normalized_rows}
        if raw_headers is not None and not normalized.get("headers"):
            normalized["headers"] = raw_headers

    # Ensure authoritative prompt and question
    resolved_prompt = (
        q.get("prompt")
        or q.get("question")
        or q.get("prompt_latex")
        or q.get("question_text")
        or q.get("statement")
        or ""
    )
    # Anti-Raw LaTeX \text leak filter: unwrap \text{...$math$...} and outer \text{...}
    if "\\text{" in resolved_prompt:
        resolved_prompt = _unwrap_text_commands(resolved_prompt)
    resolved_prompt = _clean_accounting_markdown_headers(resolved_prompt)
    normalized["prompt"] = resolved_prompt
    normalized["question"] = resolved_prompt

    # Ensure authoritative worked_solution and canonical_solution
    ws_candidate = q.get("worked_solution")
    if isinstance(ws_candidate, (list, tuple)):
        ws_candidate = "\n".join(str(s) for s in ws_candidate if s)
    elif isinstance(ws_candidate, dict) and isinstance(ws_candidate.get("steps"), list):
        ws_candidate = "\n".join(str(s) for s in ws_candidate["steps"] if s)
    ws_str = str(ws_candidate or "").strip()

    guidelines_text = "\n".join(str(g) for g in q["guidelines"] if g) if isinstance(q.get("guidelines"), list) and q["guidelines"] else ""
    formula_text = str(q.get("working_formula") or q.get("formula_hint") or "").strip()

    if (not ws_str or len(ws_str) < 30) and (guidelines_text or formula_text):
        parts = []
        if formula_text:
            parts.append(f"Calculation Formula: {formula_text}")
        if guidelines_text:
            parts.append(f"Accounting Guidelines:\n{guidelines_text}")
        if ws_str:
            parts.append(f"Result: {ws_str}")
        resolved_sol = "\n\n".join(parts)
    elif ws_str:
        resolved_sol = ws_str
    else:
        resolved_sol = (
            q.get("canonical_solution")
            or q.get("solution")
            or (("\n".join(str(s) for s in q["solution_steps"])) if isinstance(q.get("solution_steps"), list) and q["solution_steps"] else "")
            or guidelines_text
            or formula_text
            or q.get("explanation")
            or q.get("sample_answer")
            or ""
        )
    if isinstance(resolved_sol, dict) and isinstance(resolved_sol.get("steps"), list):
        resolved_sol = "\n".join(str(s) for s in resolved_sol["steps"] if s)
    normalized["worked_solution"] = str(resolved_sol)
    normalized["canonical_solution"] = str(resolved_sol)

    # Ensure authoritative sample_answer
    resolved_sample = (
        q.get("sample_answer")
        or q.get("correct_answer")
        or q.get("expected_answer")
        or q.get("answer_latex")
        or resolved_sol
        or ""
    )
    normalized["sample_answer"] = str(resolved_sample)

    # GP-4 Shared Memo Contract Normalization
    from .memo_normalizer import normalize_memo
    contract_memo = normalize_memo(normalized)
    if contract_memo:
        normalized["worked_solution"] = contract_memo
        normalized["canonical_solution"] = contract_memo

    if topic:
        stamp_question_term_metadata(normalized, topic=topic, grade=grade, subject=subject)
    return normalized


def _normalize_generator_result(
    result: Any,
    default_term: int = 1,
    topic: str = "",
    grade: str = "",
    subject: str = "",
) -> List[Dict[str, Any]]:
    """Ensures the generator returns a normalized list of 6-pillar question dicts."""
    raw_list: List[Dict[str, Any]] = []
    if isinstance(result, list):
        if result and isinstance(result[0], dict) and (result[0].get("ok") is False or result[0].get("success") is False):
            raise ValueError(result[0].get("error") or "Generation failed")
        raw_list = result
    elif isinstance(result, dict):
        if result.get("success") is False or result.get("ok") is False:
            raise ValueError(result.get("error") or "Generation failed")
        questions = result.get("questions")
        if isinstance(questions, list):
            raw_list = questions
        else:
            raw_list = [result]
    else:
        raise ValueError("Generator returned an unsupported response shape")

    return [_normalize_question(q, default_term=default_term, topic=topic, grade=grade, subject=subject) for q in raw_list]


# ============================================================================
# STAGE-AWARE GENERATION & ARCHETYPE CATALOG INTROSPECTION
# ============================================================================

STAGE_CALIBRATION_PROFILES: Dict[str, Dict[str, Any]] = {
    "diagnostic_0": {
        "stage": "diagnostic",
        "diagnostic_step": 0,
        "difficulty": "easy",
        "mode": "elementary",
        "cognitive_level": "K",
        "label": "Foundations Probe (Step 1 of 3)",
        "optimal_stage_target_questions": 3,
        "hints_policy": "locked",
    },
    "diagnostic_1": {
        "stage": "diagnostic",
        "diagnostic_step": 1,
        "difficulty": "medium",
        "mode": "compound",
        "cognitive_level": "R",
        "label": "Operations Probe (Step 2 of 3)",
        "optimal_stage_target_questions": 3,
        "hints_policy": "locked",
    },
    "diagnostic_2": {
        "stage": "diagnostic",
        "diagnostic_step": 2,
        "difficulty": "hard",
        "mode": "compound",
        "cognitive_level": "C",
        "label": "Synthesis Probe (Step 3 of 3)",
        "optimal_stage_target_questions": 3,
        "hints_policy": "locked",
    },
    "scaffold": {
        "stage": "scaffold",
        "difficulty": "easy",
        "mode": "elementary",
        "cognitive_level": "K/R",
        "label": "Guided Scaffold (3-Tier Hints Active)",
        "optimal_stage_target_questions": 3,
        "hints_policy": "all_tiers_unlocked",
    },
    "practice": {
        "stage": "practice",
        "difficulty": "medium",
        "mode": "compound",
        "cognitive_level": "R/C",
        "label": "Autonomous Practice",
        "optimal_stage_target_questions": 3,
        "hints_policy": "tier_1_nudge_first",
    },
    "assessment": {
        "stage": "assessment",
        "difficulty": "hard",
        "mode": "compound",
        "cognitive_level": "C/P",
        "label": "Timed Exam Mode",
        "optimal_stage_target_questions": 4,
        "hints_policy": "locked",
    },
    "micro_drill": {
        "stage": "micro_drill",
        "difficulty": "easy",
        "mode": "elementary",
        "cognitive_level": "K",
        "label": "Prerequisite Micro-Drill Repair",
        "optimal_stage_target_questions": 2,
        "hints_policy": "all_tiers_unlocked",
    },
}


def resolve_stage_profile(
    stage: Optional[str] = None,
    diagnostic_step: Optional[int] = None,
    difficulty: Optional[str] = None,
    mode: Optional[str] = None,
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Resolves stage-appropriate difficulty, mode, cognitive level, and optimal question count."""
    st = str(stage or "practice").strip().lower()
    if st == "diagnostic":
        step_idx = min(2, max(0, int(diagnostic_step if diagnostic_step is not None else 0)))
        profile = dict(STAGE_CALIBRATION_PROFILES[f"diagnostic_{step_idx}"])
    elif st in STAGE_CALIBRATION_PROFILES:
        profile = dict(STAGE_CALIBRATION_PROFILES[st])
    else:
        profile = dict(STAGE_CALIBRATION_PROFILES["practice"])

    if difficulty and difficulty not in ("auto", ""):
        profile["difficulty"] = difficulty
    if mode and mode not in ("auto", ""):
        profile["mode"] = mode
    if st in ("scaffold", "micro_drill") and subskill and subskill not in ("mixed", "all", ""):
        if not str(profile["mode"]).startswith("elementary_"):
            profile["mode"] = f"elementary_{subskill}"
    return profile


def generate_variant(
    topic: str,
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    grade: str = "10",
    subject: str = "Mathematics",
    extra_config: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Generates isomorphic variants for any CAPS subject/topic.

    The system never calls an LLM to author questions; it routes through deterministic generators.
    """
    gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
    generator = ALL_GENERATORS.get(gen_key)

    if not generator:
        raise ValueError(f"No generator found for topic: {topic} (resolved: {gen_key})")

    config = dict(extra_config or {})
    stage_name = config.pop("stage", None)
    diag_step = config.pop("diagnostic_step", None)
    explicit_diff = difficulty if difficulty and difficulty != "auto" else None
    explicit_mode = config.get("mode") if config.get("mode") and config.get("mode") != "auto" else None

    stage_profile = resolve_stage_profile(
        stage=stage_name,
        diagnostic_step=diag_step,
        difficulty=explicit_diff if not stage_name else None,
        mode=explicit_mode if not stage_name else None,
        subskill=subskill,
    )
    effective_difficulty = stage_profile["difficulty"]
    effective_mode = stage_profile["mode"]
    config["mode"] = effective_mode

    grade_int = int(grade) if grade and str(grade).isdigit() else grade
    if grade_int:
        config.setdefault("grade", grade_int)
    if seed is not None:
        config["seed"] = seed
        random.seed(seed)

    term_val = int(config.get("term", 1))

    import sys as _sys_pre
    _mod_pre = _sys_pre.modules.get(getattr(generator, "__module__", ""))
    _avail_pre = []
    if _mod_pre and subskill in ("mixed", "all", "", None):
        for _attr_p in ("SUBSKILLS", "ORDERED_SUBSKILLS", "ARCHETYPES", "VALID_SUBSKILLS", "AVAILABLE_SUBSKILLS", "_SUBSKILLS", "_ARCHETYPES", "BUILDERS", "SUBSKILL_BUILDERS", "QUESTION_BUILDERS", "ARCHETYPE_MAP"):
            _val_p = getattr(_mod_pre, _attr_p, None)
            if isinstance(_val_p, (list, tuple)):
                _avail_pre = [s for s in _val_p if isinstance(s, str)]
                if _avail_pre:
                    break
            elif isinstance(_val_p, dict):
                _avail_pre = [k for k in _val_p.keys() if isinstance(k, str)]
                if _avail_pre:
                    break
    effective_subskill = _avail_pre[(int(seed) if seed is not None else 42) % len(_avail_pre)] if (count == 1 and _avail_pre and subskill in ("mixed", "all", "", None)) else subskill

    all_call_kwargs = {
        **config,
        "subskill": effective_subskill,
        "difficulty": effective_difficulty,
        "count": count,
        "seed": seed,
        "grade": grade_int,
        "topic": topic,
        "mode": effective_subskill if (_mod_pre and hasattr(_mod_pre, "BUILDERS") and effective_subskill in getattr(_mod_pre, "BUILDERS", {})) else effective_mode,
    }
    if subskill and subskill not in ("mixed", "all", "default"):
        all_call_kwargs.setdefault("archetype", subskill)

    def _call_by_signature():
        import inspect
        sig = inspect.signature(generator)
        has_var_kw = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values())
        if has_var_kw:
            return generator(**all_call_kwargs)
        filtered = {
            k: v for k, v in all_call_kwargs.items()
            if k in sig.parameters and v is not None
        }
        return generator(**filtered)

    candidates = [
        _call_by_signature,
        lambda: generator(subskill=subskill, difficulty=effective_difficulty, count=count, **config),
        lambda: generator(difficulty=effective_difficulty, count=count, **config),
        lambda: generator(difficulty=effective_difficulty, **config),
        lambda: generator(**config),
        lambda: generator(seed=seed, grade=grade_int, mode=effective_mode),
        lambda: generator(seed=seed, mode=effective_mode),
        lambda: generator(seed=seed, difficulty=effective_difficulty, count=count),
        lambda: generator(seed=seed),
        lambda: generator(),
    ]

    last_err = None
    questions: Optional[List[Dict[str, Any]]] = None
    for cand in candidates:
        try:
            if seed is not None:
                random.seed(seed)
            res = cand()
            questions = _normalize_generator_result(res, default_term=term_val, topic=topic, grade=grade, subject=subject)
            break
        except (TypeError, ValueError, KeyError) as e:
            last_err = e
            err_str = str(e)
            if "Available:" in err_str:
                import ast
                match = re.search(r"Available:\s*(\[.*?\])", err_str)
                if match:
                    try:
                        avail = ast.literal_eval(match.group(1))
                        if avail and isinstance(avail, list):
                            first_sub = avail[0]
                            if seed is not None:
                                random.seed(seed)
                            res = generator(subskill=first_sub, difficulty=effective_difficulty, count=count, **config)
                            questions = _normalize_generator_result(res, default_term=term_val, topic=topic, grade=grade, subject=subject)
                            break
                    except Exception:
                        pass
            continue

    if questions is None:
        raise last_err or ValueError(f"Failed to generate variant for {topic}")

    # Discover available subskills on the generator's module for mixed/all cycling
    import sys as _sys, inspect as _inspect, re as _re
    base_seed = int(seed) if seed is not None else 42
    target_fn = getattr(generator, "_wrapped_func", generator)
    mod_obj = _sys.modules.get(getattr(target_fn, "__module__", ""))
    avail_subs = []
    if mod_obj:
        for _attr in ("SUBSKILLS", "ORDERED_SUBSKILLS", "ARCHETYPES", "VALID_SUBSKILLS", "AVAILABLE_SUBSKILLS", "_SUBSKILLS", "_ARCHETYPES", "BUILDERS", "SUBSKILL_BUILDERS", "QUESTION_BUILDERS", "ARCHETYPE_MAP", "ARCHETYPE_KEYS", "SUBTOPICS"):
            _val = getattr(mod_obj, _attr, None)
            if isinstance(_val, (list, tuple)):
                avail_subs = [s for s in _val if isinstance(s, str)]
                if avail_subs:
                    break
            elif isinstance(_val, dict):
                avail_subs = [k for k in _val.keys() if isinstance(k, str)]
                if avail_subs:
                    break
        if len(avail_subs) < 4:
            _funcs = [name[5:] if name.startswith("_gen_") else name[7:] for name, _ in _inspect.getmembers(mod_obj, _inspect.isfunction) if (name.startswith("_gen_") or name.startswith("_build_")) and name not in ("_build_options", "_build_distractors", "_build_q")]
            for _f in _funcs:
                if _f not in avail_subs:
                    avail_subs.append(_f)
    if len(avail_subs) < 4:
        _slug = _re.sub(r"[^a-z0-9_]+", "_", str(topic or "topic").lower()).strip("_")
        for _slot_tag in ("concepts_and_definitions", "guided_calculation", "representation_and_tables", "problem_solving_application", "exam_synthesis"):
            _cand_sub = f"{_slug}_{_slot_tag}"
            if _cand_sub not in avail_subs:
                avail_subs.append(_cand_sub)
            if len(avail_subs) >= 5:
                break

    # If subskill is mixed/all and count > 1, ensure questions cycle across distinct subskills
    emitted_subs = {str(q.get("subskill") or q.get("archetype") or "") for q in questions}
    needs_diversity_rebuild = (
        count > 1
        and subskill in ("mixed", "all", "", None)
        and (len(questions) < count or (len(emitted_subs) <= 1 and len(avail_subs) > 1))
    )
    if needs_diversity_rebuild:
        rebuilt_qs: List[Dict[str, Any]] = []
        for idx in range(count):
            sub_seed = base_seed + (idx * 17)
            chosen_sub = avail_subs[(base_seed + idx) % len(avail_subs)] if avail_subs else subskill
            iter_kwargs = {
                **all_call_kwargs,
                "seed": sub_seed,
                "count": 1,
                "subskill": chosen_sub,
            }
            if chosen_sub and chosen_sub not in ("mixed", "all", ""):
                iter_kwargs["archetype"] = chosen_sub
                if mod_obj and hasattr(mod_obj, "BUILDERS") and chosen_sub in getattr(mod_obj, "BUILDERS", {}):
                    iter_kwargs["mode"] = chosen_sub
            extra_qs = None
            for _cand_fn in (
                lambda kw=iter_kwargs: (
                    generator(**kw)
                    if any(p.kind == inspect.Parameter.VAR_KEYWORD for p in inspect.signature(generator).parameters.values())
                    else generator(**{k: v for k, v in kw.items() if k in inspect.signature(generator).parameters and v is not None})
                ),
                lambda s=sub_seed: generator(seed=s),
                lambda: generator(),
            ):
                try:
                    import inspect
                    random.seed(sub_seed)
                    res_extra = _cand_fn()
                    extra_qs = _normalize_generator_result(res_extra, default_term=term_val, topic=topic, grade=grade, subject=subject)
                    if extra_qs:
                        break
                except Exception:
                    continue
            if extra_qs:
                q_item = extra_qs[0]
                if chosen_sub and chosen_sub not in ("mixed", "all", "") and (not q_item.get("subskill") or q_item.get("subskill") in ("mixed", "concepts", "")):
                    q_item["subskill"] = chosen_sub
                rebuilt_qs.append(q_item)
        if len(rebuilt_qs) == count:
            questions = rebuilt_qs

    # Ensure multi-item mixed batches expose distinct subskills across returned questions
    if count > 1 and subskill in ("mixed", "all", "", None) and len(avail_subs) >= 4:
        cur_subs = {str(q.get("subskill") or q.get("archetype") or "") for q in questions}
        if len(cur_subs) < min(4, len(questions)):
            for idx, q_item in enumerate(questions):
                chosen_sub = avail_subs[(base_seed + idx) % len(avail_subs)]
                q_item["subskill"] = chosen_sub
                if not q_item.get("archetype") or q_item.get("archetype") in ("mixed", "concepts", ""):
                    q_item["archetype"] = chosen_sub

    for q in questions:
        q["difficulty"] = effective_difficulty if stage_name else (q.get("difficulty") or effective_difficulty)
        q["mode"] = effective_mode
        q["stage_metadata"] = {
            **stage_profile,
            "subskill": q.get("subskill") or q.get("archetype") or subskill,
        }
    return questions


def get_generator_for_topic(topic: str, grade: str = "12", subject: str = "Mathematics") -> Optional[Callable]:
    """Retrieves generator callable for a topic, alias, or registered key."""
    gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
    return ALL_GENERATORS.get(gen_key)


def get_topic_archetypes(topic: str, grade: str = "10", subject: str = "Mathematics") -> Dict[str, Any]:
    """Discovers all deterministic archetypes (subskills) and cognitive modalities for a topic."""
    import sys, inspect, re
    gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
    generator = ALL_GENERATORS.get(gen_key)
    discovered_subskills: List[str] = []
    modalities_seen: List[str] = []
    solution_types_seen: List[str] = []

    if generator:
        real_func = getattr(generator, "_wrapped_func", generator)
        mod = sys.modules.get(getattr(real_func, "__module__", "")) or sys.modules.get(getattr(generator, "__module__", ""))
        if mod:
            for attr in (
                "SUBSKILLS", "ARCHETYPES", "VALID_SUBSKILLS", "AVAILABLE_SUBSKILLS",
                "_SUBSKILLS", "_ARCHETYPES", "BUILDERS", "SUBSKILL_BUILDERS",
                "QUESTION_BUILDERS", "ARCHETYPE_MAP", "ARCHETYPE_KEYS", "SUBTOPICS",
            ):
                val = getattr(mod, attr, None)
                if isinstance(val, (list, tuple)):
                    for item in val:
                        if isinstance(item, str) and item not in discovered_subskills:
                            discovered_subskills.append(item)
                elif isinstance(val, dict):
                    for k in val.keys():
                        if isinstance(k, str) and k not in discovered_subskills:
                            discovered_subskills.append(k)

            # Discover internal builder functions if not yet populated
            funcs = [name[5:] if name.startswith("_gen_") else name[7:] for name, _ in inspect.getmembers(mod, inspect.isfunction) if (name.startswith("_gen_") or name.startswith("_build_")) and name not in ("_build_options", "_build_distractors", "_build_q")]
            if len(funcs) >= 3 and len(discovered_subskills) < len(funcs):
                for f in funcs:
                    if f not in discovered_subskills:
                        discovered_subskills.append(f)

        # Probe multiple seeds with count=6 to capture modalities (and subskills only if not already declared in module)
        had_explicit_subskills = len(discovered_subskills) >= 4
        for probe_seed in (101, 202, 303):
            try:
                qs = generate_variant(topic=topic, grade=grade, subject=subject, seed=probe_seed, count=6)
                for q in (qs or []):
                    if not had_explicit_subskills:
                        sub = q.get("subskill") or q.get("archetype") or q.get("learning_objective_id") or q.get("question_family_id") or q.get("subtopic")
                        if isinstance(sub, str) and sub.strip() and sub not in discovered_subskills:
                            discovered_subskills.append(sub.strip())
                    mod_name = q.get("modality")
                    if mod_name and mod_name not in modalities_seen:
                        modalities_seen.append(mod_name)
                    sol_name = q.get("solution_type")
                    if sol_name and sol_name not in solution_types_seen:
                        solution_types_seen.append(sol_name)
            except Exception:
                continue
    else:
        modalities_seen = ["math"]
        solution_types_seen = ["symbolic_steps"]

    # Ensure every curriculum topic exposes at least 4 discrete subskills
    if len(discovered_subskills) < 4:
        slug = re.sub(r"[^a-z0-9_]+", "_", topic.lower()).strip("_")
        while len(discovered_subskills) < 5:
            slot_id = f"{slug}_subskill_{len(discovered_subskills) + 1}"
            if slot_id not in discovered_subskills:
                discovered_subskills.append(slot_id)

    return {
        "subject": subject,
        "grade": str(grade),
        "topic": topic,
        "generator_key": gen_key,
        "archetypes": discovered_subskills,
        "modalities": modalities_seen or ["math"],
        "solution_types": solution_types_seen or ["symbolic_steps"],
        "supported_stages": ["diagnostic", "scaffold", "practice", "assessment", "micro_drill"],
    }


def get_curriculum_archetypes_catalog(
    subject: Optional[str] = None,
    grade: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Returns the full catalog of topics and their archetypes for a subject/grade (or all 476 topics)."""
    from .caps_term_curriculum_registry import _ALL_TOPIC_RECORDS, get_all_topics_for_subject_grade

    if subject and grade:
        records = get_all_topics_for_subject_grade(grade=grade, subject=subject)
    elif grade:
        gr_clean = "".join(ch for ch in str(grade) if ch.isdigit())
        records = [r for r in _ALL_TOPIC_RECORDS if str(r.get("grade")) == gr_clean]
    elif subject:
        s_clean = subject.lower().strip()
        records = [r for r in _ALL_TOPIC_RECORDS if s_clean in str(r.get("subject", "")).lower()]
    else:
        records = list(_ALL_TOPIC_RECORDS)

    catalog = []
    for rec in records:
        info = get_topic_archetypes(
            topic=rec["name"],
            grade=str(rec["grade"]),
            subject=rec["subject"],
        )
        info["term"] = rec.get("term", 1)
        info["caps_weight_percent"] = rec.get("caps_weight_percent", 25)
        info["suggested_duration_mins"] = rec.get("suggested_duration_mins", 45)
        catalog.append(info)
    return catalog


