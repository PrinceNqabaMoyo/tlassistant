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
)

# Grade 7 EMS
from app.utils.grade7_ems import (
    term1_money_and_needs as g7_money,
    term1_businesses as g7_businesses,
    term1_goods_and_services as g7_goods,
    term2_accounting_concepts as g7_acct_concepts,
    term2_income_and_expenses as g7_income,
    term2_budgets as g7_budgets,
    term3_entrepreneurship as g7_entrepreneurship,
    term3_inequality_and_poverty as g7_inequality,
    term3_production_process as g7_prod,
    term4_savings as g7_savings,
)

# Grade 8 EMS
from app.utils.grade8_ems import (
    term1_gov_and_society as g8_gov,
    term1_accounting_basics as g8_acct_basics,
    term1_source_documents as g8_source_docs,
    term2_markets_and_production as g8_markets,
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
    term3_business as g9_business,
    term3_trade_unions as g9_trade_unions,
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

# Grade 9 Mathematics
from app.utils import (
    grade9_algebraic_expressions_generator as g9_math_expr,
    grade9_algebraic_equations_generator as g9_math_eq,
    grade9_decimal_notation_generator as g9_math_dec,
    grade9_exponents_generator as g9_math_exp,
    grade9_fractions_generator as g9_math_frac,
    grade9_functions_generator as g9_math_func,
    grade9_integers_generator as g9_math_int,
    grade9_patterns_generator as g9_math_pat,
    grade9_whole_numbers_generator as g9_math_whole,
)
from app.utils.grade9_mathematics import (
    factorisation_generator as g9_math_fact,
    congruence_similarity_generator as g9_math_geom,
    pythagoras_generator as g9_math_pyth,
    geometry_straight_lines_triangles_generator as g9_math_lines,
    measurement_3d_generator as g9_math_meas3d,
    algebraic_equations_fractions_generator as g9_math_eq_frac,
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
    fractions_decimals_generator as g8_math_frac_dec,
    geometry_2d_shapes_generator as g8_math_geom2d,
    geometry_3d_objects_generator as g8_math_3d_obj,
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
    ethics_generator as g10_acct_ethics,
    internal_control_generator as g10_acct_ctrl,
    fixed_assets_depreciation_generator as g10_acct_fixed,
    inventory_cost_of_sales_generator as g10_acct_inv,
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
    income_statement_generator as g11_acct_inc,
    partnership_balance_sheet_generator as g11_acct_bs,
    partnership_ledger_generator as g11_acct_led,
    reconciliation_generator as g11_acct_recon,
    concepts_generator as g11_acct_concepts,
    partnerships_financial_statements_generator as g11_acct_part_stmt,
    inventory_valuation_generator as g11_acct_inv,
    vat_generator as g11_acct_vat,
    analysis_interpretation_generator as g11_acct_analysis,
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
    companies_generator as g12_acct_companies,
    debtors_age_analysis_generator as g12_acct_debtors,
    vat_analysis_generator as g12_acct_vat,
    accounting_equation_generator as g12_acct_eq,
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
)
from app.utils.natural_sciences import (
    electric_circuits_generator as ns_circuits,
    chemical_reactions_generator as ns_reactions,
    senior_phase_astronomy_generator as ns_astronomy,
    term1_life_and_living_generator as ns_life_living,
    term2_matter_materials_generator as ns_matter_materials,
    term3_energy_change_forces_generator as ns_energy_forces,
    term4_planet_earth_beyond_generator as ns_planet_earth,
)
from app.utils.mathematical_literacy import (
    finance_tax_generator as mathlit_fin,
    maps_scales_generator as mathlit_maps,
    tariffs_tax_brackets_generator as mathlit_tariffs,
    data_handling_generator as mathlit_data,
    measurement_probability_generator as mathlit_meas_prob,
)
from app.utils.technical_mathematics import (
    complex_numbers_generator as tech_cplx,
    mensuration_calculus_generator as tech_mens,
    circles_angular_movement_generator as tech_circles,
)

# Foundational Mathematics (Tang & Stokke Pedagogy)
from app.utils.foundational_math import generate_number_bonds_drill as foundational_math_drill


# ============================================================================
# ADAPTERS
# ============================================================================

def _adapt_single_item_generator(gen_func: Callable) -> Callable:
    """Wraps a single-item generator (e.g. Gr8/Gr9 math) to return a list of questions."""
    def adapter(**kw):
        count = int(kw.get("count", 1))
        seed_val = kw.get("seed")
        r = random.Random(seed_val) if seed_val is not None else random.Random()
        questions = []
        for _ in range(count):
            sub_seed = r.randint(1, 1_000_000_000)
            try:
                q = gen_func(
                    subskill=kw.get("subskill", "mixed"),
                    difficulty=kw.get("difficulty", "medium"),
                    question_type=kw.get("question_type", "mixed"),
                    seed=sub_seed,
                )
            except TypeError:
                try:
                    q = gen_func(seed=sub_seed)
                except TypeError:
                    q = gen_func()
            questions.append(q)
        return questions
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
        qtype = kw.get("question_type", "typed")

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
                return res
            except (TypeError, ValueError, KeyError) as e:
                last_err = e
                continue
        raise last_err or ValueError("Failed in multi-item generator adapter")
    return adapter


# ============================================================================
# SUBJECT DICTIONARIES
# ============================================================================

GRADE7_MATH_GENERATORS = {
    "grade7_math_geometry_of_2d_shapes": g7_math_geom2d.generate,
    "grade7_math_2d_shapes": g7_math_geom2d.generate,
    "grade7_math_geometry_of_straight_lines": g7_math_geom2d.generate,
    "grade7_math_area_and_perimeter_of_2d_shapes": g7_math_meas.generate,
    "grade7_math_perimeter_and_area": g7_math_meas.generate,
    "grade7_math_measurement": g7_math_meas.generate,
    "grade7_math_surface_area_and_volume_of_3d_objects": g7_math_meas.generate,
    "grade7_math_data_handling": g7_math_data.generate_data_handling,
    "grade7_math_statistics": g7_math_data.generate_data_handling,
    "grade7_math_transformation_geometry": g7_math_trans.generate,
    "grade7_math_construction_of_geometric_figures": g_sp_geometry,
    "grade7_math_whole_numbers": g7_math_whole.generate,
    "grade7_math_working_with_whole_numbers": g7_math_whole.generate,
    "grade7_math_integers": g7_math_int.generate,
    "grade7_math_patterns": g7_math_pat.generate,
    "grade7_math_numeric_and_geometric_patterns": g7_math_pat.generate,
    "grade7_math_numeric_patterns": g7_math_pat.generate,
    "grade7_math_algebraic_expressions": g7_math_alg.generate,
    "grade7_math_algebraic_equations": g7_math_alg.generate,
    "grade7_math_probability": g7_math_data.generate_probability,
    "grade7_math_functions": g7_math_graph.generate,
    "grade7_math_functions_and_relationships": g7_math_graph.generate,
    "grade7_math_graphs": g7_math_graph.generate,
    "grade7_math_exponents": g7_math_exp.generate,
    "grade7_math_fractions": g7_math_frac.generate,
    "grade7_math_common_fractions": g7_math_frac.generate,
    "grade7_math_decimal_notation": g7_math_dec.generate,
    "grade7_math_decimals": g7_math_dec.generate,
    "grade7_math_decimal_fractions": g7_math_dec.generate,
    "grade7_math_graph_paper_types": g_sp_measurement,
    "grade7_math_geometric_nets_3d": g7_math_nets.generate,
    "grade7_math_geometry_of_3d_objects": g7_math_nets.generate,
    "grade7_math_3d_shapes_and_nets": g7_math_nets.generate,
    "grade7_math_nets_of_3d_shapes": g7_math_nets.generate,
}

GRADE8_MATH_GENERATORS = {
    "grade8_math_algebraic_expressions": g8_math_alg.generate,
    "grade8_math_algebraic_equations": g8_math_alg.generate,
    "grade8_math_exponents": _adapt_single_item_generator(g8_math_exp.generate_grade8_exponents_question),
    "grade8_math_functions": _adapt_single_item_generator(g8_math_func.generate_grade8_functions_question),
    "grade8_math_integers": g8_math_int.generate,
    "grade8_math_patterns": _adapt_single_item_generator(g8_math_pat.generate_grade8_patterns_question),
    "grade8_math_whole_numbers": _adapt_single_item_generator(g8_math_whole.generate_grade8_whole_numbers_question),
    "grade8_math_fractions": g8_math_frac_dec.generate,
    "grade8_math_decimal_notation": g8_math_frac_dec.generate,
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
    "grade8_math_area_and_perimeter_of_2d_shapes": g_sp_measurement,
    "grade8_math_surface_area_and_volume_of_3d_objects": g8_math_meas3d.generate,
    "grade8_math_measurement_3d": g8_math_meas3d.generate,
    "grade8_math_data_handling": g_sp_data_handling,
    "grade8_math_transformation_geometry": g_sp_transformations,
    "grade8_math_construction_of_geometric_figures": g_sp_geometry,
    "grade8_math_probability": g_sp_probability,
    "grade8_math_graph_paper_types": g_sp_measurement,
}

GRADE9_MATH_GENERATORS = {
    "grade9_math_algebraic_expressions": _adapt_single_item_generator(g9_math_expr.generate_grade9_algebraic_expressions_question),
    "grade9_math_algebraic_equations": _adapt_single_item_generator(g9_math_eq.generate_grade9_algebraic_equations_question),
    "grade9_math_decimal_notation": _adapt_single_item_generator(g9_math_dec.generate_grade9_decimal_notation_question),
    "grade9_math_exponents": _adapt_single_item_generator(g9_math_exp.generate_grade9_exponents_question),
    "grade9_math_fractions": _adapt_single_item_generator(g9_math_frac.generate_grade9_fractions_question),
    "grade9_math_functions": _adapt_single_item_generator(g9_math_func.generate_grade9_functions_relationships_question),
    "grade9_math_integers": _adapt_single_item_generator(g9_math_int.generate_grade9_integers_question),
    "grade9_math_patterns": _adapt_single_item_generator(g9_math_pat.generate_grade9_patterns_question),
    "grade9_math_whole_numbers": _adapt_single_item_generator(g9_math_whole.generate_grade9_whole_numbers_question),
    "grade9_math_factorisation": g9_math_fact.generate,
    "grade9_math_algebraic_fractions": g9_math_eq_frac.generate,
    "grade9_math_congruence_similarity": g9_math_geom.generate,
    "grade9_math_geometry": g9_math_geom.generate,
    "grade9_math_theorem_of_pythagoras": g9_math_pyth.generate,
    "grade9_math_pythagoras": g9_math_pyth.generate,
    "grade9_math_geometry_of_2d_shapes": g9_math_lines.generate,
    "grade9_math_geometry_of_straight_lines": g9_math_lines.generate,
    "grade9_math_geometry_of_3d_objects": g9_math_meas3d.generate,
    "grade9_math_geometric_nets_3d": g7_math_nets.generate,
    "grade9_math_area_and_perimeter_of_2d_shapes": g_sp_measurement,
    "grade9_math_surface_area_and_volume_of_3d_objects": g9_math_meas3d.generate,
    "grade9_math_measurement_3d": g9_math_meas3d.generate,
    "grade9_math_data_handling": g_sp_data_handling,
    "grade9_math_transformation_geometry": g_sp_transformations,
    "grade9_math_construction_of_geometric_figures": g_sp_geometry,
    "grade9_math_probability": g_sp_probability,
    "grade9_math_graph_paper_types": g_sp_measurement,
    "grade9_math_graphs": _adapt_single_item_generator(g9_math_func.generate_grade9_functions_relationships_question),
    "grade9_math_algebraic_equations_fractions": g9_math_eq_frac.generate,
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
    "grade7_ems_money_and_needs": g7_money.generate,
    "grade7_ems_needs_and_wants": g7_money.generate,
    "grade7_ems_goods_and_services": g7_goods.generate,
    "grade7_ems_businesses": g7_businesses.generate,
    "grade7_ems_accounting_concepts": g7_acct_concepts.generate,
    "grade7_ems_income_and_expenses": g7_income.generate,
    "grade7_ems_budgets": g7_budgets.generate,
    "grade7_ems_entrepreneurship": g7_entrepreneurship.generate,
    "grade7_ems_the_entrepreneur": g7_entrepreneurship.generate,
    "grade7_ems_starting_a_business": g7_entrepreneurship.generate,
    "grade7_ems_entrepreneurs_day": g7_entrepreneurship.generate,
    "grade7_ems_inequality_and_poverty": g7_inequality.generate,
    "grade7_ems_savings": g7_savings.generate,
    "grade7_ems_production_process": g7_prod.generate,
    "grade7_ems_the_production_process": g7_prod.generate,
}

GRADE8_EMS_GENERATORS = {
    "grade8_ems_gov_and_society": g8_gov.generate,
    "grade8_ems_government": g8_gov.generate,
    "grade8_ems_national_budget": g8_gov.generate,
    "grade8_ems_standard_of_living": g8_gov.generate,
    "grade8_ems_accounting_basics": g8_acct_basics.generate,
    "grade8_ems_source_documents": g8_source_docs.generate,
    "grade8_ems_markets_and_production": g8_markets.generate,
    "grade8_ems_markets": g8_markets.generate,
    "grade8_ems_factors_of_production": g8_markets.generate,
    "grade8_ems_crj": g8_crj.generate,
    "grade8_ems_cash_receipts_journal": g8_crj.generate,
    "grade8_ems_cash_payments_journal": g8_cpj_crj.generate,
    "grade8_ems_accounting_cycle": g8_acct_cycle.generate,
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
    "grade9_ems_business_functions": g9_business.generate,
    "grade9_ems_trade_unions": g9_trade_unions.generate,
}

GRADE10_ACCOUNTING_GENERATORS = {
    "grade10_accounting_sole_trader": _adapt_multi_item_generator(g10_acct_sole.generate_questions),
    "grade10_accounting_gaap": _adapt_multi_item_generator(g10_acct_gaap.generate_grade10_gaap_questions),
    "grade10_accounting_ethics": _adapt_multi_item_generator(g10_acct_ethics.generate_questions),
    "grade10_accounting_internal_control": _adapt_multi_item_generator(g10_acct_ctrl.generate_questions),
    "grade10_accounting_vat": _adapt_multi_item_generator(g10_acct_vat.generate_questions),
    "grade10_accounting_salaries_wages": _adapt_multi_item_generator(g10_acct_sal.generate_questions),
    "grade10_accounting_final_accounts": _adapt_multi_item_generator(g10_acct_final.generate_questions),
    "grade10_accounting_bank_reconciliation": _adapt_multi_item_generator(g10_acct_recon.generate_questions),
    "grade10_accounting_budgets": g12_acct_budgets.generate,
    "grade10_accounting_vat_analysis": g12_acct_vat.generate,
    "grade10_accounting_equation": g12_acct_eq.generate,
    "grade10_accounting_fixed_assets": g10_acct_fixed.generate,
    "grade10_accounting_depreciation": g10_acct_fixed.generate,
    "grade10_accounting_inventory": g10_acct_inv.generate,
    "grade10_accounting_cost_of_sales": g10_acct_inv.generate,
}

GRADE11_ACCOUNTING_GENERATORS = {
    "grade11_accounting_fixed_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_income_statement": _adapt_multi_item_generator(g11_acct_inc.generate_questions),
    "grade11_accounting_partnerships": _adapt_multi_item_generator(g11_acct_bs.generate_questions),
    "grade11_accounting_partnership_ledger": _adapt_multi_item_generator(g11_acct_led.generate_questions),
    "grade11_accounting_reconciliation": _adapt_multi_item_generator(g11_acct_recon.generate_questions),
    "grade11_accounting_concepts": _adapt_multi_item_generator(g11_acct_concepts.generate_questions),
    "grade11_accounting_partnerships_financial_statements": _adapt_multi_item_generator(g11_acct_part_stmt.generate_questions),
    "grade11_accounting_partnership_financial_statements": _adapt_multi_item_generator(g11_acct_part_stmt.generate_questions),
    "grade11_accounting_inventory_valuation": _adapt_multi_item_generator(g11_acct_inv.generate_questions),
    "grade11_accounting_inventory_systems": _adapt_multi_item_generator(g11_acct_inv.generate_questions),
    "grade11_accounting_budgets": g12_acct_budgets.generate,
    "grade11_accounting_cash_budget_variance": g12_acct_budgets.generate,
    "grade11_accounting_debtors_age_analysis": g12_acct_debtors.generate,
    "grade11_accounting_vat": g11_acct_vat.generate,
    "grade11_accounting_equation": g12_acct_eq.generate,
    "grade11_accounting_cost_accounting": g12_acct_cost.generate,
    "grade11_accounting_disposal_of_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_fixed_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_analysis_interpretation": _adapt_multi_item_generator(g11_acct_analysis.generate_questions),
    "grade11_accounting_calculations_involving_percentages": _adapt_multi_item_generator(g11_acct_analysis.generate_questions),
}

GRADE12_ACCOUNTING_GENERATORS = {
    "grade12_accounting_cash_flow_statement": g12_acct_cfs.generate,
    "grade12_accounting_cash_flow": g12_acct_cfs.generate,
    "grade12_accounting_financial_indicators": g12_acct_indicators.generate,
    "grade12_accounting_analysis_interpretation": g12_acct_indicators.generate,
    "grade12_accounting_company_ledger": _adapt_multi_item_generator(g12_acct_gl.generate_questions),
    "grade12_accounting_financial_statements": _adapt_multi_item_generator(g12_acct_stmt.generate_questions),
    "grade12_accounting_concepts": _adapt_multi_item_generator(g12_acct_concepts.generate_questions),
    "grade12_accounting_cost_accounting": g12_acct_cost.generate,
    "grade12_accounting_production_cost": g12_acct_cost.generate,
    "grade12_accounting_budgets": g12_acct_budgets.generate,
    "grade12_accounting_cash_budget_variance": g12_acct_budgets.generate,
    "grade12_accounting_companies": g12_acct_companies.generate,
    "grade12_accounting_debtors_age_analysis": g12_acct_debtors.generate,
    "grade12_accounting_vat": g12_acct_vat.generate,
    "grade12_accounting_equation": g12_acct_eq.generate,
    "grade12_accounting_disposal_of_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade12_accounting_fixed_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade12_accounting_reconciliations": _adapt_multi_item_generator(g11_acct_recon.generate_questions),
    "grade12_accounting_control_accounts": _adapt_multi_item_generator(g11_acct_led.generate_questions),
    "grade12_accounting_inventories": _adapt_multi_item_generator(g11_acct_inv.generate_questions),
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
    "mathematical_literacy_data_handling": mathlit_data.generate,
    "mathematical_literacy_measurement": mathlit_meas_prob.generate,
    "mathematical_literacy_probability": mathlit_meas_prob.generate,
    "technical_mathematics_complex_numbers": tech_cplx.generate,
    "technical_mathematics_mensuration": tech_mens.generate,
    "technical_mathematics_euclidean_geometry": g11_math_circ_theorems.generate,
    "technical_mathematics_geometry": g11_math_circ_theorems.generate,
    "technical_mathematics_analytical_geometry": g12_math_circles.generate,
    "technical_mathematics_circles_angles": tech_circles.generate,
    "technical_mathematics_angular_movement": tech_circles.generate,
    "grade11_physical_sciences_chemistry": phys11_chem.generate,
    "grade11_physical_sciences_atomic_combinations": phys11_chem.generate,
    "grade11_physical_sciences_intermolecular_forces": phys11_chem.generate,
}

NATURAL_SCIENCES_GENERATORS = {
    "natural_sciences_electric_circuits": ns_circuits.generate,
    "natural_sciences_circuits": ns_circuits.generate,
    "natural_sciences_chemical_reactions": ns_reactions.generate,
    "natural_sciences_reactions": ns_reactions.generate,
    "natural_sciences_senior_phase_astronomy": ns_astronomy.generate,
    "natural_sciences_life_and_living": ns_life_living.generate,
    "natural_sciences_photosynthesis": ns_life_living.generate,
    "natural_sciences_cell_cytology": ns_life_living.generate,
    "natural_sciences_human_systems": ns_life_living.generate,
    "natural_sciences_angiosperm_reproduction": ns_life_living.generate,
    "natural_sciences_matter_and_materials": ns_matter_materials.generate,
    "natural_sciences_separating_mixtures": ns_matter_materials.generate,
    "natural_sciences_atomic_structure": ns_matter_materials.generate,
    "natural_sciences_acid_base_reactions": ns_matter_materials.generate,
    "natural_sciences_energy_and_change": ns_energy_forces.generate,
    "natural_sciences_forces_and_weight": ns_energy_forces.generate,
    "natural_sciences_heat_energy_transfer": ns_energy_forces.generate,
    "natural_sciences_cost_of_electricity": ns_energy_forces.generate,
    "natural_sciences_planet_earth_and_beyond": ns_planet_earth.generate,
    "natural_sciences_seasons_and_tides": ns_planet_earth.generate,
    "natural_sciences_lithosphere_mining": ns_planet_earth.generate,
    "natural_sciences_stellar_evolution": ns_planet_earth.generate,
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

PHYS_LS_GENERATORS = {
    # Grade 10 Physical Sciences
    "grade10_physical_sciences_waves_sound_light": phys10_waves.generate,
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
    "grade12_physical_sciences_electrodynamics": phys12_electrodyn.generate,
    "grade12_physical_sciences_electric_circuits": phys12_electrodyn.generate,
    "grade12_physical_sciences_optical_phenomena": phys12_photoelectric.generate,
    "grade12_physical_sciences_photoelectric_effect": phys12_photoelectric.generate,
    "life_sciences_meiosis_human_reproduction": ls_meiosis.generate,
    "physical_sciences_electrostatics": phys_electro.generate,
    "physical_sciences_electromagnetism": phys_electro.generate,
    # Vertical strands
    "life_sciences_photosynthesis_respiration": ls_photosynth.generate,
    "life_sciences_human_organ_systems": ls_organs.generate,
    "life_sciences_environmental_population": ls_env.generate,
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
# TOPIC ALIAS RESOLVER (Connects human labels & ATP names to generators)
# ============================================================================

from app.services.generator_aliases import TOPIC_ALIASES


def resolve_generator_key(topic: str, grade: str = "10", subject: str = "Mathematics") -> str:
    """Finds the registered generator key from topic name, slug, or alias."""
    # 1. Direct match in registry
    if topic in ALL_GENERATORS:
        return topic

    clean = topic.strip().lower().replace("_", " ").replace("-", " ")
    subj_lower = subject.lower()

    is_mathlit = "literacy" in subj_lower
    is_techmath = "technical" in subj_lower
    is_math = "math" in subj_lower and not is_techmath and not is_mathlit
    is_acct = "account" in subj_lower or "acct" in subj_lower
    is_ems = "ems" in subj_lower or "economic" in subj_lower
    is_bs = "business" in subj_lower and not is_ems
    is_phys = "physical" in subj_lower
    is_life = "life" in subj_lower
    is_ns = "natural" in subj_lower

    stop_words = {"of", "the", "and", "in", "to", "for", "a", "an", "on", "at", "by", "with", "from"}
    meaningful_words = [w for w in clean.split() if w not in stop_words and len(w) > 2]
    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "10"
    subj_code = "math" if is_math else ("accounting" if is_acct else ("ems" if is_ems else "bs"))

    # Mathematical Literacy direct topic routing (NEVER proxy to pure math)
    if is_mathlit:
        if any(w in clean for w in ["finance", "tax", "tariff", "bracket", "income", "expenditure", "budget", "document", "exchange"]):
            if "tariff" in clean or "water" in clean or "electricity" in clean:
                return "mathematical_literacy_tariffs_tax_brackets"
            return "mathematical_literacy_finance_tax"
        if any(w in clean for w in ["map", "scale", "plan", "distance", "compass"]):
            return "mathematical_literacy_maps_scales"
        if "data" in clean:
            return "mathematical_literacy_data_handling"
        if any(w in clean for w in ["measure", "weight", "volume", "length", "bmi", "capacity", "tank", "temperature", "perimeter", "area"]):
            return "mathematical_literacy_measurement"
        if "probab" in clean:
            return "mathematical_literacy_probability"
        return "mathematical_literacy_finance_tax"

    # Technical Mathematics direct routing
    if is_techmath:
        if "complex" in clean:
            return "technical_mathematics_complex_numbers"
        if any(w in clean for w in ["mensuration", "circle", "integrat"]):
            return "technical_mathematics_mensuration"
        if "trig" in clean:
            if grade_num == "11": return "grade11_math_trigonometry"
            elif grade_num == "12": return "grade12_math_trigonometry"
            return "grade10_math_trigonometry"
        if "function" in clean:
            if grade_num == "11": return "grade11_math_functions"
            elif grade_num == "12": return "grade12_math_functions"
            return "grade10_math_functions"
        if any(w in clean for w in ["circle", "angle", "angular", "movement", "arc", "sector", "radian"]):
            return "technical_mathematics_circles_angles"
        if "analytical" in clean:
            return "technical_mathematics_analytical_geometry"
        if "euclidean" in clean or "geometry" in clean:
            return "technical_mathematics_euclidean_geometry"
        return "technical_mathematics_complex_numbers"

    # Natural Sciences direct routing (Senior Phase Grade 7-9)
    if is_ns:
        if any(w in clean for w in ["life", "living", "biosphere", "biodiversity", "angiosperm", "flower", "reproduction", "pollination", "variation", "photosynthesis", "respiration", "ecosystem", "microorganism", "cell", "organelle", "organ", "system", "digestive", "circulatory", "respiratory", "excretory"]):
            return "natural_sciences_life_and_living"
        if any(w in clean for w in ["mixture", "separat", "filtration", "distillation", "chromatography", "acid", "base", "ph value", "ph scale", "litmus", "salt", "neutralis", "atom", "nuclide", "proton", "neutron", "electron", "matter", "diffusion", "particle", "periodic", "element", "compound"]):
            return "natural_sciences_matter_and_materials"
        if any(w in clean for w in ["heat", "conduction", "convection", "radiation", "insulat", "static", "force", "gravity", "mass", "weight", "cost", "kwh", "power", "tariff", "electricity"]):
            return "natural_sciences_energy_and_change"
        if any(w in clean for w in ["circuit", "electric", "current", "cell", "resistor", "series", "parallel", "ammeter", "voltmeter"]):
            return "natural_sciences_electric_circuits"
        if any(w in clean for w in ["earth", "season", "solstice", "tide", "eclipse", "sun", "moon", "solar system", "planet", "telescope", "salt", "meerkat", "ska", "star", "stellar", "nebula", "supernova", "lithosphere", "mining", "mine", "drainage"]):
            return "natural_sciences_planet_earth_and_beyond"
        if any(w in clean for w in ["reaction", "combustion", "chemical equation"]):
            return "natural_sciences_chemical_reactions"
        return "natural_sciences_life_and_living"
# Physical Sciences grade-specific chemistry / physics routing
    if is_phys:
        if grade_num == "12":
            if any(w in clean for w in ["organic", "alkane", "alkene", "alkyne", "haloalkane", "alcohol", "ester", "aldehyde", "ketone", "carboxylic", "iupac", "isomer"]):
                return "grade12_physical_sciences_organic_chemistry"
            if any(w in clean for w in ["acid", "base", "ph", "titrat", "hydrolysis", "neutralis", "amphiprotic", "ampholyte", "kw", "h3o"]):
                return "grade12_physical_sciences_acids_bases"
            if any(w in clean for w in ["electrodynamic", "generator", "motor", "alternat", "rms", "internal resistance", "lost volt", "circuit", "slip ring", "commutator"]):
                return "grade12_physical_sciences_electrodynamics"
            if any(w in clean for w in ["photoelectric", "optical", "work function", "threshold frequency", "photon", "cut off", "spectra"]):
                return "grade12_physical_sciences_optical_phenomena"
            if any(w in clean for w in ["momentum", "impulse"]):
                return "grade12_physical_sciences_momentum"
            if any(w in clean for w in ["projectile", "vertical", "skill"]):
                return "grade12_physical_sciences_vertical_projectile"
            if "doppler" in clean:
                return "grade12_physical_sciences_doppler_effect"
            if any(w in clean for w in ["rate", "extent", "equilibrium", "le chatelier", "kc", "chemical industry", "fertilizer", "haber", "contact"]):
                return "physical_sciences_chemistry_equilibrium"
            if any(w in clean for w in ["work", "energy", "power"]):
                return "physical_sciences_work_energy_power"
            if any(w in clean for w in ["galvanic", "electrolytic", "electrochem", "cell"]):
                return "physical_sciences_electrochemistry"

        if grade_num == "11":
            if any(w in clean for w in ["circuit", "ohm", "resistor", "series", "parallel", "tariff", "kwh", "cost"]):
                return "grade11_physical_sciences_electric_circuits"
            if any(w in clean for w in ["enthalpy", "delta h", "bond energy", "activated complex", "activation energy", "exothermic", "endothermic"]):
                return "grade11_physical_sciences_energy_chemical_change"
            if any(w in clean for w in ["limiting", "excess", "yield", "purity", "stoichiometr"]):
                return "grade11_physical_sciences_stoichiometry_limiting"
            if any(w in clean for w in ["atomic", "intermolecular", "bonding", "vsepr", "molecular", "lithosphere"]):
                return "grade11_physical_sciences_chemistry"
            if any(w in clean for w in ["vector", "newton", "force", "unit"]):
                return "grade11_physical_sciences_vectors_newton"
            if any(w in clean for w in ["ideal gas", "boyle", "charles", "gas"]):
                return "physical_sciences_ideal_gases_thermal"
            if any(w in clean for w in ["optics", "snell", "refraction", "critical angle", "reflection", "wavefront"]):
                return "physical_sciences_geometrical_optics"
            if any(w in clean for w in ["electrostatic", "coulomb", "electric field"]):
                return "physical_sciences_electrostatics"
            if any(w in clean for w in ["electromagnet", "faraday", "magnetic flux"]):
                return "physical_sciences_electromagnetism"

        if grade_num == "10":
            if any(w in clean for w in ["circuit", "magnet", "charge", "current", "potential difference", "emf", "resistor"]):
                return "grade10_physical_sciences_electric_circuits"
            if any(w in clean for w in ["mole", "empirical", "composition", "stoichiometr", "stoichiometry", "aqueous", "stp", "chemical change"]):
                return "grade10_physical_sciences_chemical_change"
            if any(w in clean for w in ["motion", "kinematic", "acceleration", "displacement", "velocity", "mechanical energy", "potential energy", "kinetic energy"]):
                return "grade10_physical_sciences_motion_energy"
            if any(w in clean for w in ["wave", "sound", "light", "pulse", "radiation"]):
                return "grade10_physical_sciences_waves_sound_light"
            if any(w in clean for w in ["matter", "material", "atom", "periodic", "bonding", "hydrosphere"]):
                return "grade10_physical_sciences_matter_materials"
            if any(w in clean for w in ["electrostatic"]):
                return "physical_sciences_electrostatics"

    # Pure Mathematics grade-specific topics
    if is_math:
        if grade_num in ["7", "8", "9"]:
            if any(w in clean for w in ["3d", "net", "geometric net", "polyhedr", "euler", "folding net", "solid"]) and not any(v in clean for v in ["surface area", "volume", "capacity"]):
                return "grade8_math_geometry_of_3d_objects" if grade_num == "8" else f"grade{grade_num}_math_geometric_nets_3d"
        if grade_num == "7":
            if any(w in clean for w in ["3d", "net", "polyhedr", "solid"]):
                return "grade7_math_geometric_nets_3d"
            if "pattern" in clean:
                return "grade7_math_patterns"
            if "integer" in clean:
                return "grade7_math_integers"
            if "decimal" in clean:
                return "grade7_math_decimal_notation"
            if "fraction" in clean:
                return "grade7_math_fractions"
            if any(w in clean for w in ["2d", "triangle", "quadrilateral", "polygon"]):
                return "grade7_math_geometry_of_2d_shapes"
            if any(w in clean for w in ["function", "relationship", "flow diagram", "graph"]):
                return "grade7_math_functions"
            if any(w in clean for w in ["data", "stat", "mean", "median", "mode", "range"]):
                return "grade7_math_data_handling"
            if "probab" in clean:
                return "grade7_math_probability"
            if any(w in clean for w in ["exponent", "power", "square root", "cube root", "square", "cube"]):
                return "grade7_math_exponents"
            if any(w in clean for w in ["perimeter", "area", "volume", "surface area", "measurement", "capacity"]):
                return "grade7_math_measurement"
            if any(w in clean for w in ["transform", "symmetr", "translat", "reflect", "enlarg", "reduct"]):
                return "grade7_math_transformation_geometry"
            if any(w in clean for w in ["whole", "division", "number"]):
                return "grade7_math_whole_numbers"
        if grade_num == "8":
            if any(w in clean for w in ["3d", "polyhedr", "euler", "platonic", "solid"]):
                return "grade8_math_geometry_of_3d_objects"
            if any(w in clean for w in ["pythagoras", "hypotenuse", "right-angled"]):
                return "grade8_math_pythagoras"
            if "integer" in clean:
                return "grade8_math_integers"
            if any(w in clean for w in ["expression", "equation", "distributive", "algebra"]):
                return "grade8_math_algebraic_expressions"
            if any(w in clean for w in ["straight line", "parallel", "transversal", "alternate", "corresponding", "co-interior", "lines"]):
                return "grade8_math_geometry_of_straight_lines"
            if any(w in clean for w in ["surface area", "volume", "prism", "cylinder", "measurement"]):
                return "grade8_math_surface_area_and_volume_of_3d_objects"
            if "pattern" in clean:
                return "grade8_math_patterns"
            if "whole" in clean:
                return "grade8_math_whole_numbers"
            if "exponent" in clean:
                return "grade8_math_exponents"
            if "fraction" in clean:
                return "grade8_math_fractions"
            if "decimal" in clean:
                return "grade8_math_decimal_notation"
            if any(w in clean for w in ["2d", "triangle", "quadrilateral", "shape"]):
                return "grade8_math_geometry_of_2d_shapes"
            if "percent" in clean:
                return "grade8_math_percentages"
            if "data" in clean or "stat" in clean:
                return "grade8_math_data_handling"
            if "probab" in clean:
                return "grade8_math_probability"
        if grade_num == "9":
            if any(w in clean for w in ["pythagoras", "hypotenuse", "space diagonal", "distance"]):
                return "grade9_math_theorem_of_pythagoras"
            if any(w in clean for w in ["factor", "difference of two squares", "trinomial"]):
                return "grade9_math_factorisation"
            if any(w in clean for w in ["equation", "fraction", "lcd", "quadratic"]):
                return "grade9_math_algebraic_equations_fractions"
            if any(w in clean for w in ["straight line", "triangle", "exterior angle", "isosceles"]):
                return "grade9_math_geometry_of_straight_lines"
            if any(w in clean for w in ["congruen", "similar"]):
                return "grade9_math_congruence_similarity"
            if any(w in clean for w in ["surface area", "volume", "cylinder", "prism", "capacity"]):
                return "grade9_math_surface_area_and_volume_of_3d_objects"
            if "graph" in clean:
                return "grade9_math_graphs"
            if "pattern" in clean:
                return "grade9_math_patterns"
            if "integer" in clean:
                return "grade9_math_integers"
            if "exponent" in clean:
                return "grade9_math_exponents"
            if any(w in clean for w in ["data", "stat"]):
                return "grade9_math_data_handling"
            if "probab" in clean:
                return "grade9_math_probability"
        if grade_num == "10" and any(w in clean for w in ["finance", "growth", "interest", "hire purchase"]):
            return "grade10_math_finance"
        if grade_num == "10" and ("stat" in clean or "quartile" in clean or "box" in clean):
            return "grade10_math_statistics"
        if grade_num == "10" and "probab" in clean:
            return "grade10_math_probability"
        if grade_num == "11":
            if any(w in clean for w in ["function", "graph", "parabola", "hyperbola"]):
                return "grade11_math_functions"
            if any(w in clean for w in ["circle", "euclidean", "theorem", "rider"]):
                return "grade11_math_circle_geometry"
            if any(w in clean for w in ["trig", "reduction", "identity"]):
                return "grade11_math_trigonometry"
            if any(w in clean for w in ["finance", "growth", "decay"]):
                return "grade11_math_finance"
            if "probab" in clean:
                return "grade11_math_probability"
            if "stat" in clean or "ogive" in clean:
                return "grade11_math_statistics"
            if any(w in clean for w in ["surd", "exponent"]):
                return "grade11_math_exponents_surds"
            if "equation" in clean or "inequal" in clean:
                return "grade11_math_equations_inequalities"
        if grade_num == "12":
            if any(w in clean for w in ["sequence", "series", "pattern", "sigma"]):
                return "grade12_math_sequences_series"
            if any(w in clean for w in ["trig", "compound", "double angle"]):
                return "grade12_math_trigonometry"
            if any(w in clean for w in ["calculus", "differentiat", "derivative", "cubic"]):
                return "grade12_math_differential_calculus"
            if any(w in clean for w in ["circle", "analytical", "tangent"]):
                return "grade12_math_analytical_geometry_circles"
            if any(w in clean for w in ["count", "permutation", "factorial", "probab"]):
                return "grade12_math_counting_probability"
            if any(w in clean for w in ["stat", "regression", "bivariate", "scatter"]):
                return "grade12_math_bivariate_statistics"
            if any(w in clean for w in ["finance", "annuity", "sinking", "loan"]):
                return "grade12_math_finance"
            if any(w in clean for w in ["function", "inverse", "log"]):
                return "grade12_math_functions"

    # Accounting grade-specific topics
    if is_acct:
        if grade_num == "10":
            if any(w in clean for w in ["sole trader", "crj", "cpj", "journal", "ledger", "bookkeeping", "subsidiary"]):
                return "grade10_accounting_sole_trader"
            if "gaap" in clean or "principle" in clean or "concept" in clean:
                return "grade10_accounting_gaap"
            if "ethic" in clean:
                return "grade10_accounting_ethics"
            if "internal control" in clean:
                return "grade10_accounting_internal_control"
            if "vat" in clean or "value added" in clean or "tax" in clean:
                return "grade10_accounting_vat"
            if any(w in clean for w in ["salary", "wage"]):
                return "grade10_accounting_salaries_wages"
            if any(w in clean for w in ["final account", "trial balance", "statement", "balance sheet"]):
                return "grade10_accounting_final_accounts"
            if "reconcil" in clean:
                return "grade10_accounting_bank_reconciliation"
            if "budget" in clean:
                return "grade10_accounting_budgets"
            if "equation" in clean:
                return "grade10_accounting_equation"
            if any(w in clean for w in ["fixed asset", "depreciation", "tangible asset"]):
                return "grade10_accounting_fixed_assets"
            if any(w in clean for w in ["inventory", "stock", "cost of sales", "markup", "mark up"]):
                return "grade10_accounting_inventory"
            if any(w in clean for w in ["indigenous", "informal"]):
                return "grade10_accounting_sole_trader"
            if "cost" in clean or "manufacturing" in clean:
                return "grade10_accounting_inventory"
        elif grade_num == "11":
            if any(w in clean for w in ["fixed asset", "depreciation", "tangible asset", "disposal"]):
                return "grade11_accounting_fixed_assets"
            if any(w in clean for w in ["income statement", "comprehensive income"]):
                return "grade11_accounting_income_statement"
            if "partnership" in clean:
                return "grade11_accounting_partnerships"
            if "reconcil" in clean:
                return "grade11_accounting_reconciliation"
            if any(w in clean for w in ["inventory", "stock", "valuation", "system"]):
                return "grade11_accounting_inventory_valuation"
            if any(w in clean for w in ["vat", "value added", "tax"]):
                return "grade11_accounting_vat"
            if any(w in clean for w in ["ethic", "internal control", "gaap", "concept", "principle"]):
                return "grade11_accounting_concepts"
            if any(w in clean for w in ["analysis", "interpretation", "indicator", "ratio", "percentage", "profitability", "liquidity", "solvency"]):
                return "grade11_accounting_analysis_interpretation"
            if "budget" in clean:
                return "grade11_accounting_budgets"
            if "cost" in clean or "manufacturing" in clean:
                return "grade11_accounting_cost_accounting"
            if "equation" in clean:
                return "grade11_accounting_equation"
        elif grade_num == "12":
            if "cash flow" in clean:
                return "grade12_accounting_cash_flow_statement"
            if any(w in clean for w in ["indicator", "ratio", "solvency", "liquidity"]):
                return "grade12_accounting_financial_indicators"
            if any(w in clean for w in ["interpretation", "analysis"]):
                return "grade12_accounting_analysis_interpretation"
            if any(w in clean for w in ["company", "companies", "share", "dividend"]):
                return "grade12_accounting_companies"
            if "cost" in clean or "manufacturing" in clean:
                return "grade12_accounting_cost_accounting"
            if "budget" in clean:
                return "grade12_accounting_budgets"
            if "reconcil" in clean:
                return "grade12_accounting_reconciliations"
            if "inventory" in clean:
                return "grade12_accounting_inventories"

    # EMS grade-specific topics
    if is_ems:
        if grade_num == "7" and "savings" in clean:
            return "grade7_ems_savings"
        if grade_num == "8" and "receipt" in clean:
            return "grade8_ems_cash_receipts_journal"
        if grade_num == "8" and "payment" in clean:
            return "grade8_ems_cash_payments_journal"

    # Business Studies grade-specific topics
    if is_bs:
        if grade_num == "11":
            if "creative" in clean: return "grade11_bs_creative_thinking"
            if "ethics" in clean or "professionalism" in clean: return "grade11_bs_professionalism_and_ethics"
            if "human resource" in clean or "hr" in clean: return "grade11_bs_marketing_function"
            if "team" in clean or "conflict" in clean or "stress" in clean: return "grade11_bs_stress_crisis_change"
            if "citizenship" in clean or "responsibilit" in clean: return "grade11_bs_citizenship_responsibilities"
        elif grade_num == "12":
            if "creative" in clean or "problem" in clean: return "grade12_bs_creative_thinking_problem_solving"
            if "ethics" in clean or "professionalism" in clean: return "grade12_bs_ethics_and_professionalism"
            if "human resource" in clean or "hr" in clean or "legislation" in clean: return "grade12_bs_human_resources_function"
            if "macro" in clean or "strateg" in clean: return "grade12_bs_macro_environment_strategies"
            if "business sector" in clean or "environment" in clean: return "grade12_bs_business_sectors_environments"
            if "ownership" in clean: return "grade12_bs_forms_of_ownership_success"
            if "presentation" in clean or "data response" in clean: return "grade12_bs_presentation_data_responses"
            if "human right" in clean or "inclusiv" in clean: return "grade12_bs_human_rights_inclusivity"
            if "team" in clean or "conflict" in clean: return "grade12_bs_team_performance_conflict"

    # 2. Check alias map
    if clean in TOPIC_ALIASES:
        resolved = TOPIC_ALIASES[clean]
        if (is_math or is_acct or is_bs or is_ems) and grade_num and not resolved.startswith(f"grade{grade_num}_"):
            target_prefix = f"grade{grade_num}_{subj_code}_"
            for k in ALL_GENERATORS:
                if k.startswith(target_prefix) and any(w in k for w in meaningful_words):
                    return k
        return resolved

    # 3. Subject-level direct routing for science & tech
    if is_ns or "circuit" in clean:
        return "natural_sciences_electric_circuits"
    if "reaction" in clean or "acid" in clean or "base" in clean:
        return "natural_sciences_chemical_reactions"
    if is_life or "genetics" in clean or "inheritance" in clean:
        return "life_sciences_genetics"
    if "momentum" in clean or "impulse" in clean or "collision" in clean:
        return "physical_sciences_momentum_impulse"
    if is_phys or "mechanics" in clean:
        return "physical_sciences_mechanics"

    # 4. Fuzzy search for key prefix
    if (is_math or is_acct or is_bs or is_ems) and grade_num:
        target_prefix = f"grade{grade_num}_{subj_code}_"
        for k in ALL_GENERATORS:
            if k.startswith(target_prefix) and any(w in k for w in meaningful_words):
                return k

    # 5. Fallback for Business Studies / EMS
    if is_bs:
        if grade_num == "11":
            return "grade11_bs_adapting_to_challenges"
        elif grade_num == "12":
            return "grade12_bs_macro_environment_strategies"
        return "grade10_bs_combinatorial"
    if is_ems:
        if grade_num == "7":
            return "grade7_ems_money_and_needs"
        elif grade_num == "8":
            return "grade8_ems_gov_and_society"
        elif grade_num == "9":
            return "grade9_ems_economic_systems"
        return "grade10_bs_combinatorial"

    # Default fallback: Only if topic is a math-related request or explicitly generic
    if "math" in subj_lower and any(w in clean for w in ["algebra", "expression", "general", "concept", "mixed"]):
        return "grade10_math_algebraic_expressions"

    return ""


# ============================================================================
# 6-PILLAR NORMALIZATION & ENRICHMENT
# ============================================================================

def _normalize_question(
    q: Dict[str, Any],
    default_term: int = 1,
    topic: str = "",
    grade: str = "",
    subject: str = "",
) -> Dict[str, Any]:
    """Ensures a single question dictionary strictly complies with the 6-pillar contract."""
    from .caps_term_curriculum_registry import stamp_question_term_metadata, get_term_for_topic

    qid = str(q.get("id") or q.get("question_id") or f"q_{random.randint(100000, 999999)}")
    marks = int(q.get("marks", 2))

    # Marking Schema
    schema = q.get("marking_schema")
    if not schema or not isinstance(schema, dict):
        schema = {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate method/answer", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }

    # 3-Tier Hints
    hints = q.get("hints")
    if not hints or not isinstance(hints, dict):
        base_hint = q.get("explanation") or q.get("hint_trigger") or "Apply standard curriculum procedure."
        hints = {
            "tier_1": "Carefully inspect the question parameters.",
            "tier_2": base_hint,
            "tier_3": f"Correct solution step: {q.get('correct_answer') or q.get('sample_answer') or 'Refer to memo.'}"
        }

    # Misconception tags
    tags = q.get("misconception_tags")
    if not tags:
        tag = q.get("misconception")
        tags = [tag] if tag else ["general_procedural_error"]

    # Resolve authoritative term
    resolved_term = default_term
    if topic:
        resolved_term = get_term_for_topic(topic, grade=grade, subject=subject)
    elif q.get("term"):
        resolved_term = int(q.get("term"))

    normalized = {
        **q,
        "id": qid,
        "question_id": qid,
        "term": resolved_term,
        "caps_weight_percent": int(q.get("caps_weight_percent") or 25),
        "suggested_duration_mins": int(q.get("suggested_duration_mins") or max(2, int(marks * 1.2))),
        "mode": q.get("mode") or "compound",
        "marks": marks,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": tags,
    }
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
# MASTER GENERATE FUNCTION
# ============================================================================

def generate_variant(
    topic: str,
    subskill: str = "concepts",
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
    if grade and str(grade).isdigit():
        config.setdefault("grade", int(grade))
    if seed is not None:
        config["seed"] = seed
        random.seed(seed)

    term_val = int(config.get("term", 1))

    candidates = [
        lambda: generator(subskill=subskill, difficulty=difficulty, count=count, **config),
        lambda: generator(difficulty=difficulty, count=count, **config),
        lambda: generator(difficulty=difficulty, **config),
        lambda: generator(**config),
        lambda: generator(),
    ]

    last_err = None
    for cand in candidates:
        try:
            res = cand()
            return _normalize_generator_result(res, default_term=term_val, topic=topic, grade=grade, subject=subject)
        except (TypeError, ValueError, KeyError) as e:
            last_err = e
            # If the error provides available_subskills, try the first valid subskill!
            err_str = str(e)
            if "Available:" in err_str:
                import ast
                match = re.search(r"Available:\s*(\[.*?\])", err_str)
                if match:
                    try:
                        avail = ast.literal_eval(match.group(1))
                        if avail and isinstance(avail, list):
                            first_sub = avail[0]
                            res = generator(subskill=first_sub, difficulty=difficulty, count=count, **config)
                            return _normalize_generator_result(res, default_term=term_val, topic=topic, grade=grade, subject=subject)
                    except Exception:
                        pass
            continue

    raise last_err or ValueError(f"Failed to generate variant for {topic}")


def get_generator_for_topic(topic: str, grade: str = "12", subject: str = "Mathematics") -> Optional[Callable]:
    """Retrieves generator callable for a topic, alias, or registered key."""
    gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
    return ALL_GENERATORS.get(gen_key)

