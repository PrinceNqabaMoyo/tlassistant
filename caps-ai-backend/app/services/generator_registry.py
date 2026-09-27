"""Central Generator Registry for Fundile Learning.
Maps (subject, grade, topic) -> deterministic generator function.
Enforces the 6-Pillar Generator Contract, AST purity, and multi-modal question representations.
Includes the 4D Combinatorial Engine for near-infinite semantic breadth.
"""
from __future__ import annotations

import random
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
)
from app.utils.grade10_mathematics.term_4 import (
    measurements_generator as g10_math_meas,
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
)

# Grade 12 Physical Sciences & Chemistry
from app.utils.grade12_physical_sciences import (
    stoichiometry_equilibrium_generator as phys_chem_eq,
    momentum_impulse_generator as phys_momentum,
)

# Grade 12 Business Studies (40-Mark Essay)
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
from app.utils.life_sciences import (
    genetics_generator as life_gen,
    dihybrid_pedigree_generator as life_dihybrid,
)
from app.utils.natural_sciences import (
    electric_circuits_generator as ns_circuits,
    chemical_reactions_generator as ns_reactions,
)
from app.utils.mathematical_literacy import (
    finance_tax_generator as mathlit_fin,
    maps_scales_generator as mathlit_maps,
)
from app.utils.technical_mathematics import (
    complex_numbers_generator as tech_cplx,
    mensuration_calculus_generator as tech_mens,
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
        sub = kw.get("subskill", "mixed")
        qtype = kw.get("question_type", "mixed")
        try:
            return gen_func(count=count, seed=seed_val, difficulty=diff, subskill=sub, question_type=qtype)
        except TypeError:
            try:
                return gen_func(count=count, seed=seed_val)
            except TypeError:
                try:
                    r = random.Random(seed_val) if seed_val is not None else random.Random()
                    return gen_func(r=r, n=count)
                except TypeError:
                    return gen_func(**kw)
    return adapter


# ============================================================================
# SUBJECT DICTIONARIES
# ============================================================================

GRADE7_MATH_GENERATORS = {
    "grade7_math_geometry_of_2d_shapes": g_sp_geometry,
    "grade7_math_geometry_of_straight_lines": g_sp_geometry,
    "grade7_math_area_and_perimeter_of_2d_shapes": g_sp_measurement,
    "grade7_math_surface_area_and_volume_of_3d_objects": g_sp_measurement,
    "grade7_math_data_handling": g_sp_data_handling,
    "grade7_math_transformation_geometry": g_sp_transformations,
    "grade7_math_construction_of_geometric_figures": g_sp_geometry,
    "grade7_math_whole_numbers": _adapt_single_item_generator(g8_math_whole.generate_grade8_whole_numbers_question),
    "grade7_math_integers": _adapt_single_item_generator(g8_math_int.generate_grade8_integers_question),
    "grade7_math_patterns": _adapt_single_item_generator(g8_math_pat.generate_grade8_patterns_question),
    "grade7_math_functions": _adapt_single_item_generator(g8_math_func.generate_grade8_functions_question),
    "grade7_math_exponents": _adapt_single_item_generator(g8_math_exp.generate_grade8_exponents_question),
    "grade7_math_fractions": _adapt_single_item_generator(g9_math_frac.generate_grade9_fractions_question),
    "grade7_math_decimal_notation": _adapt_single_item_generator(g9_math_dec.generate_grade9_decimal_notation_question),
    "grade7_math_graph_paper_types": g_sp_measurement,
}

GRADE8_MATH_GENERATORS = {
    "grade8_math_algebraic_expressions": _adapt_single_item_generator(g8_math_expr.generate_grade8_algebraic_expressions_question),
    "grade8_math_algebraic_equations": _adapt_single_item_generator(g8_math_eq.generate_grade8_algebraic_equations_question),
    "grade8_math_exponents": _adapt_single_item_generator(g8_math_exp.generate_grade8_exponents_question),
    "grade8_math_functions": _adapt_single_item_generator(g8_math_func.generate_grade8_functions_question),
    "grade8_math_integers": _adapt_single_item_generator(g8_math_int.generate_grade8_integers_question),
    "grade8_math_patterns": _adapt_single_item_generator(g8_math_pat.generate_grade8_patterns_question),
    "grade8_math_whole_numbers": _adapt_single_item_generator(g8_math_whole.generate_grade8_whole_numbers_question),
    "grade8_math_fractions": _adapt_single_item_generator(g9_math_frac.generate_grade9_fractions_question),
    "grade8_math_decimal_notation": _adapt_single_item_generator(g9_math_dec.generate_grade9_decimal_notation_question),
    "grade8_math_theorem_of_pythagoras": g_sp_pythagoras,
    "grade8_math_geometry_of_2d_shapes": g_sp_geometry,
    "grade8_math_geometry_of_straight_lines": g_sp_geometry,
    "grade8_math_area_and_perimeter_of_2d_shapes": g_sp_measurement,
    "grade8_math_surface_area_and_volume_of_3d_objects": g_sp_measurement,
    "grade8_math_data_handling": g_sp_data_handling,
    "grade8_math_transformation_geometry": g_sp_transformations,
    "grade8_math_construction_of_geometric_figures": g_sp_geometry,
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
    "grade9_math_algebraic_fractions": g9_math_fact.generate,
    "grade9_math_congruence_similarity": g9_math_geom.generate,
    "grade9_math_geometry": g9_math_geom.generate,
    "grade9_math_theorem_of_pythagoras": g_sp_pythagoras,
    "grade9_math_geometry_of_2d_shapes": g_sp_geometry,
    "grade9_math_geometry_of_straight_lines": g_sp_geometry,
    "grade9_math_area_and_perimeter_of_2d_shapes": g_sp_measurement,
    "grade9_math_surface_area_and_volume_of_3d_objects": g_sp_measurement,
    "grade9_math_data_handling": g_sp_data_handling,
    "grade9_math_transformation_geometry": g_sp_transformations,
    "grade9_math_construction_of_geometric_figures": g_sp_geometry,
    "grade9_math_graph_paper_types": g_sp_measurement,
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
}

GRADE12_MATH_GENERATORS = {
    "grade12_math_finance": _adapt_multi_item_generator(g12_math_fin.generate_questions),
    "grade12_math_functions": _adapt_multi_item_generator(g12_math_func.generate_questions),
    "grade12_math_patterns_sequences_series": _adapt_multi_item_generator(g12_math_pat.generate_questions),
    "grade12_math_trigonometry": _adapt_multi_item_generator(g12_math_trig.generate_questions),
    "grade12_math_differential_calculus": g12_math_calc.generate,
    "grade12_math_calculus": g12_math_calc.generate,
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
    "grade11_bs_marketing_production": g11_bs_mkt_prod.generate,
}

GRADE12_BS_GENERATORS = {
    "grade12_bs_essay": g12_bs_essay.generate,
    "grade12_bs_section_c": g12_bs_essay.generate,
    "grade12_bs_40_marks": g12_bs_essay.generate,
    "grade12_bs_legislation_hr": g12_bs_leg_hr.generate,
    "grade12_bs_investments_management": g12_bs_inv_man.generate,
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
    "grade8_ems_accounting_cycle": g8_acct_cycle.generate,
    "grade8_ems_cpj_and_crj": g8_cpj_crj.generate,
    "grade8_ems_ownership": g8_ownership.generate,
    "grade8_ems_forms_of_ownership": g8_ownership.generate,
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
    "grade11_accounting_vat": g12_acct_vat.generate,
    "grade11_accounting_equation": g12_acct_eq.generate,
    "grade11_accounting_cost_accounting": g12_acct_cost.generate,
    "grade11_accounting_disposal_of_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
    "grade11_accounting_fixed_tangible_assets": _adapt_multi_item_generator(g11_acct_fixed.generate_questions),
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
    "technical_mathematics_complex_numbers": tech_cplx.generate,
    "technical_mathematics_mensuration": tech_mens.generate,
}

NATURAL_SCIENCES_GENERATORS = {
    "natural_sciences_electric_circuits": ns_circuits.generate,
    "natural_sciences_circuits": ns_circuits.generate,
    "natural_sciences_chemical_reactions": ns_reactions.generate,
    "natural_sciences_reactions": ns_reactions.generate,
}

FOUNDATIONAL_MATH_GENERATORS = {
    "foundational_math_number_bonds": _adapt_single_item_generator(foundational_math_drill),
}


from app.utils.grade10_physical_sciences import waves_sound_light_generator as phys10_waves
from app.utils.grade10_physical_sciences import matter_materials_generator as phys10_matter
from app.utils.grade11_physical_sciences import vectors_newton_generator as phys11_vec
from app.utils.grade12_physical_sciences import vertical_projectile_generator as phys12_proj
from app.utils.grade12_physical_sciences import doppler_effect_generator as phys12_doppler
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
    "grade10_physical_sciences_waves_sound_light": phys10_waves.generate,
    "grade10_physical_sciences_matter_materials": phys10_matter.generate,
    "grade10_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_vectors_newton": phys11_vec.generate,
    "grade11_physical_sciences_electrostatics": phys_electro.generate,
    "grade11_physical_sciences_electromagnetism": phys_electro.generate,
    "grade12_physical_sciences_vertical_projectile": phys12_proj.generate,
    "grade12_physical_sciences_doppler_effect": phys12_doppler.generate,
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

TOPIC_ALIASES: Dict[str, str] = {
    "waves sound and light": "grade10_physical_sciences_waves_sound_light",
    "waves": "grade10_physical_sciences_waves_sound_light",
    "matter and materials": "grade10_physical_sciences_matter_materials",
    "matter": "grade10_physical_sciences_matter_materials",
    "vectors and newtons laws": "grade11_physical_sciences_vectors_newton",
    "vectors": "grade11_physical_sciences_vectors_newton",
    "vertical projectile motion": "grade12_physical_sciences_vertical_projectile",
    "vertical projectile": "grade12_physical_sciences_vertical_projectile",
    "doppler effect": "grade12_physical_sciences_doppler_effect",
    "doppler": "grade12_physical_sciences_doppler_effect",
    "meiosis": "life_sciences_meiosis_human_reproduction",
    "human reproduction": "life_sciences_meiosis_human_reproduction",

    # Foundational Math (Tang & Stokke) aliases
    "number bonds": "foundational_math_number_bonds",
    "fractions foundation": "foundational_math_number_bonds",
    "foundational math": "foundational_math_number_bonds",
    "foundational number bonds": "foundational_math_number_bonds",
    "stokke speed sprint": "foundational_math_number_bonds",
    "tang number bonds": "foundational_math_number_bonds",
    # Grade 9 Math aliases
    "factorisation": "grade9_math_factorisation",
    "algebraic fractions": "grade9_math_algebraic_fractions",
    "congruence and similarity": "grade9_math_congruence_similarity",
    "congruence": "grade9_math_congruence_similarity",
    "similarity": "grade9_math_congruence_similarity",
    # Grade 10 Math aliases
    "algebraic expressions": "grade10_math_algebraic_expressions",
    "equations & inequalities": "grade10_math_equations_inequalities",
    "equations and inequalities": "grade10_math_equations_inequalities",
    "exponents & surds": "grade10_math_exponents",
    "exponents": "grade10_math_exponents",
    "number patterns": "grade10_math_patterns_sequences",
    "patterns & sequences": "grade10_math_patterns_sequences",
    "trigonometry ratios": "grade10_math_trigonometry",
    "trigonometry": "grade10_math_trigonometry",
    "functions & graphs": "grade10_math_functions",
    "functions": "grade10_math_functions",
    "analytical geometry": "grade10_math_analytical_geometry",
    "circle & euclidean geometry": "grade10_math_euclidean_geometry",
    "euclidean geometry": "grade10_math_euclidean_geometry",
    "measurements": "grade10_math_measurements",
    "circle geometry": "grade11_math_circle_geometry",
    # Grade 11 Math aliases
    "measurement": "grade11_math_measurement",
    "linear programming": "grade11_math_linear_programming",
    "investigation and projects": "grade11_math_investigation_and_projects",
    "equations": "grade11_math_equations_inequalities",
    "surds": "grade11_math_exponents_surds",
    "circle geometry riders": "grade11_math_circle_geometry_theorems",
    "circle geometry theorems": "grade11_math_circle_geometry_theorems",
    "trigonometry reductions": "grade11_math_trigonometry_reductions",
    "trig reductions": "grade11_math_trigonometry_reductions",
    "trigonometric reductions": "grade11_math_trigonometry_reductions",
    "finance growth and decay": "grade11_math_finance_growth_decay",
    "finance growth decay": "grade11_math_finance_growth_decay",
    "finance, growth and decay": "grade11_math_finance_growth_decay",
    "grade 11 finance": "grade11_math_finance_growth_decay",
    "depreciation": "grade11_math_finance_growth_decay",
    "reducing balance": "grade11_math_finance_growth_decay",
    "nominal and effective rate": "grade11_math_finance_growth_decay",
    "nominal to effective": "grade11_math_finance_growth_decay",
    "effective rate": "grade11_math_finance_growth_decay",
    "probability contingency": "grade11_math_probability_contingency",
    "probability contingency tables": "grade11_math_probability_contingency",
    "grade 11 probability": "grade11_math_probability_contingency",
    "contingency tables": "grade11_math_probability_contingency",
    "contingency table": "grade11_math_probability_contingency",
    "two-way contingency tables": "grade11_math_probability_contingency",
    "two-way tables": "grade11_math_probability_contingency",
    "independent events": "grade11_math_probability_contingency",
    "mutually exclusive events": "grade11_math_probability_contingency",
    "statistics summary ogive": "grade11_math_statistics_summary_ogive",
    "grade 11 statistics": "grade11_math_statistics_summary_ogive",
    "ogive": "grade11_math_statistics_summary_ogive",
    "ogive curve": "grade11_math_statistics_summary_ogive",
    "five-number summary": "grade11_math_statistics_summary_ogive",
    "box and whisker": "grade11_math_statistics_summary_ogive",
    "box-and-whisker": "grade11_math_statistics_summary_ogive",
    "outliers": "grade11_math_statistics_summary_ogive",
    "skewness": "grade11_math_statistics_summary_ogive",
    # Grade 12 Math aliases
    "financial mathematics": "grade12_math_finance",
    "finance": "grade12_math_finance",
    "sequences & series": "grade12_math_patterns_sequences_series",
    "analytical trigonometry": "grade12_math_trigonometry",
    "differential calculus": "grade12_math_differential_calculus",
    "calculus": "grade12_math_differential_calculus",
    "analytical geometry circles": "grade12_math_analytical_geometry_circles",
    "circles analytical geometry": "grade12_math_analytical_geometry_circles",
    "circles": "grade12_math_analytical_geometry_circles",
    "counting principles": "grade12_math_counting_probability",
    "fundamental counting principle": "grade12_math_counting_probability",
    "counting and probability": "grade12_math_counting_probability",
    "probability": "grade12_math_counting_probability",
    "venn diagrams": "grade12_math_counting_probability",
    "permutations": "grade12_math_counting_probability",
    "bivariate statistics": "grade12_math_bivariate_statistics",
    "statistics": "grade12_math_bivariate_statistics",
    "regression": "grade12_math_bivariate_statistics",
    "least squares regression": "grade12_math_bivariate_statistics",
    "least squares": "grade12_math_bivariate_statistics",
    "correlation coefficient": "grade12_math_bivariate_statistics",
    "scatter plots": "grade12_math_bivariate_statistics",
    # Accounting aliases
    "sole trader": "grade10_accounting_sole_trader",
    "gaap": "grade10_accounting_gaap",
    "ethics": "grade10_accounting_ethics",
    "internal control": "grade10_accounting_internal_control",
    "vat": "grade10_accounting_vat",
    "salaries & wages": "grade10_accounting_salaries_wages",
    "final accounts": "grade10_accounting_final_accounts",
    "bank reconciliation": "grade10_accounting_bank_reconciliation",
    "fixed assets": "grade11_accounting_fixed_assets",
    "income statement": "grade11_accounting_income_statement",
    "partnerships": "grade11_accounting_partnerships",
    "partnerships financial statements": "grade11_accounting_partnerships_financial_statements",
    "partnership financial statements": "grade11_accounting_partnerships_financial_statements",
    "appropriation account": "grade11_accounting_partnerships_financial_statements",
    "current accounts note": "grade11_accounting_partnerships_financial_statements",
    "current account note": "grade11_accounting_partnerships_financial_statements",
    "inventory valuation": "grade11_accounting_inventory_valuation",
    "inventory systems": "grade11_accounting_inventory_valuation",
    "fifo": "grade11_accounting_inventory_valuation",
    "weighted average": "grade11_accounting_inventory_valuation",
    "fifo and weighted average": "grade11_accounting_inventory_valuation",
    "cash flow": "grade12_accounting_cash_flow_statement",
    "cash flow statement": "grade12_accounting_cash_flow_statement",
    "cash flow statements": "grade12_accounting_cash_flow_statement",
    "cash generated from operations": "grade12_accounting_cash_flow_statement",
    "taxation paid": "grade12_accounting_cash_flow_statement",
    "dividends paid": "grade12_accounting_cash_flow_statement",
    "working capital changes": "grade12_accounting_cash_flow_statement",
    "financial indicators": "grade12_accounting_financial_indicators",
    "financial ratios": "grade12_accounting_financial_indicators",
    "financial indicators & ratios": "grade12_accounting_financial_indicators",
    "analysis and interpretation": "grade12_accounting_financial_indicators",
    "analysis and interpretation of financial statements": "grade12_accounting_financial_indicators",
    "analysis of financial statements": "grade12_accounting_financial_indicators",
    "interpretation of financial statements": "grade12_accounting_financial_indicators",
    "current ratio": "grade12_accounting_financial_indicators",
    "acid test ratio": "grade12_accounting_financial_indicators",
    "acid test": "grade12_accounting_financial_indicators",
    "debtors collection period": "grade12_accounting_financial_indicators",
    "creditors payment period": "grade12_accounting_financial_indicators",
    "debt equity ratio": "grade12_accounting_financial_indicators",
    "debt to equity": "grade12_accounting_financial_indicators",
    "gearing": "grade12_accounting_financial_indicators",
    "financial risk": "grade12_accounting_financial_indicators",
    "roshe": "grade12_accounting_financial_indicators",
    "return on shareholders equity": "grade12_accounting_financial_indicators",
    "return on average shareholders equity": "grade12_accounting_financial_indicators",
    "earnings per share": "grade12_accounting_financial_indicators",
    "dividends per share": "grade12_accounting_financial_indicators",
    "eps": "grade12_accounting_financial_indicators",
    "dps": "grade12_accounting_financial_indicators",
    "cost accounting": "grade12_accounting_cost_accounting",
    "production cost statement": "grade12_accounting_cost_accounting",
    "break even analysis": "grade12_accounting_cost_accounting",
    "budgets": "grade12_accounting_budgets",
    "budgeting": "grade12_accounting_budgets",
    "cash budget variance analysis": "grade12_accounting_cash_budget_variance",
    "companies": "grade12_accounting_companies",
    "debtors age analysis": "grade12_accounting_debtors_age_analysis",
    "the accounting equation": "grade12_accounting_equation",
    "accounting equation": "grade12_accounting_equation",
    "value added tax": "grade12_accounting_vat",
    "valued added tax": "grade12_accounting_vat",
    "disposal of tangible assets": "grade11_accounting_disposal_of_tangible_assets",
    "fixed tangible assets": "grade11_accounting_fixed_tangible_assets",
    "cost accounting manufacturing": "grade12_accounting_cost_accounting",
    "reconciliations": "grade11_accounting_reconciliation",
    "calculations involving percentages": "grade12_accounting_financial_indicators",
    "preliminary information": "grade12_accounting_concepts",
    "basic concepts of accounting": "grade12_accounting_concepts",
    "accounting principles": "grade10_accounting_gaap",
    "difference between financial and managerial accounting": "grade12_accounting_concepts",
    "managing resources": "grade10_accounting_internal_control",
    "informal or indigenous bookkeeping systems": "grade10_accounting_sole_trader",
    "salaries and wages journal": "grade10_accounting_salaries_wages",
    "non profit organisations or clubs": "grade11_accounting_concepts",
    "introduction to accounting": "grade10_accounting_sole_trader",
    "inventories": "grade11_accounting_inventory_valuation",
    "control accounts": "grade11_accounting_partnership_ledger",
    "financial accounting of a sole trader": "grade10_accounting_sole_trader",
    "financial accounts and year end adjustments of a sole trader": "grade10_accounting_final_accounts",
    "financial statements of a sole trader": "grade10_accounting_final_accounts",
    "analysis and interpretation of financial statements of a sole trader": "grade10_accounting_final_accounts",
    "partnerships analysis of financial statements": "grade11_accounting_partnerships_financial_statements",
    "financial information and gaap": "grade10_accounting_gaap",
    # Business Studies aliases
    "micro environment": "grade10_bs_micro_environment",
    "market environment": "grade10_bs_market_environment",
    "macro environment": "grade10_bs_macro_environment",
    "business functions": "grade10_bs_business_functions",
    "forms of ownership": "grade10_bs_forms_of_ownership",
    "social responsibility": "grade10_bs_social_responsibility",
    "socio-economic issues": "grade10_bs_socio_economic_issues",
    "business studies essay": "grade12_bs_essay",
    "business studies section c": "grade12_bs_essay",
    "section c essay": "grade12_bs_essay",
    "impact of recent legislation on businesses": "grade12_bs_legislation_hr",
    "recent legislation": "grade12_bs_legislation_hr",
    "human resources function": "grade12_bs_legislation_hr",
    "human resources": "grade12_bs_legislation_hr",
    "investments securities": "grade12_bs_investments_management",
    "investments insurance": "grade12_bs_investments_management",
    "investments": "grade12_bs_investments_management",
    "management & leadership": "grade12_bs_investments_management",
    "management and leadership": "grade12_bs_investments_management",
    "quality of performance": "grade12_bs_investments_management",
    "marketing function": "grade11_bs_marketing_production",
    "the marketing function": "grade11_bs_marketing_production",
    "production function": "grade11_bs_marketing_production",
    "the production function": "grade11_bs_marketing_production",
    # Senior Phase Math aliases
    "theorem of pythagoras": "grade8_math_theorem_of_pythagoras",
    "pythagoras": "grade8_math_theorem_of_pythagoras",
    "geometry of 2d shapes": "grade8_math_geometry_of_2d_shapes",
    "geometry of 3d objects": "grade8_math_geometry_of_2d_shapes",
    "geometry of straight lines": "grade8_math_geometry_of_straight_lines",
    "straight lines": "grade8_math_geometry_of_straight_lines",
    "area and perimeter of 2d shapes": "grade8_math_area_and_perimeter_of_2d_shapes",
    "area and perimeter": "grade8_math_area_and_perimeter_of_2d_shapes",
    "surface area and volume of 3d objects": "grade8_math_surface_area_and_volume_of_3d_objects",
    "surface area and volume": "grade8_math_surface_area_and_volume_of_3d_objects",
    "data handling": "grade8_math_data_handling",
    "transformation geometry": "grade8_math_transformation_geometry",
    "transformations": "grade8_math_transformation_geometry",
    "construction of geometric figures": "grade8_math_construction_of_geometric_figures",
    "constructions": "grade8_math_construction_of_geometric_figures",
    # EMS aliases
    "senior phase gap": "grade8_ems_gap",
    "savings": "grade8_ems_gap",
    "production process": "grade8_ems_gap",
    "management levels": "grade8_ems_gap",
    # Science & Tech aliases
    "mechanics": "physical_sciences_mechanics",
    "physical sciences": "physical_sciences_mechanics",
    "newton's laws": "physical_sciences_mechanics",
    "vectors": "physical_sciences_mechanics",
    "inclined planes": "physical_sciences_inclined_planes",
    "momentum and impulse": "physical_sciences_momentum_impulse",
    "momentum & impulse": "physical_sciences_momentum_impulse",
    "momentum": "physical_sciences_momentum_impulse",
    "impulse": "physical_sciences_momentum_impulse",
    "collisions": "physical_sciences_momentum_impulse",
    "conservation of momentum": "physical_sciences_momentum_impulse",
    "1d momentum": "physical_sciences_momentum_impulse",
    "elastic and inelastic collisions": "physical_sciences_momentum_impulse",
    "impulse-momentum theorem": "physical_sciences_momentum_impulse",
    "chemical equilibrium": "physical_sciences_chemistry_equilibrium",
    "equilibrium and stoichiometry": "physical_sciences_chemistry_equilibrium",
    "stoichiometry": "physical_sciences_chemistry_equilibrium",
    "genetics": "life_sciences_genetics",
    "life sciences": "life_sciences_genetics",
    "genetics and inheritance": "life_sciences_genetics",
    "genetics & inheritance": "life_sciences_genetics",
    "monohybrid cross": "life_sciences_genetics",
    "punnett square": "life_sciences_genetics",
    "dihybrid cross": "life_sciences_dihybrid_cross",
    "dihybrid": "life_sciences_dihybrid_cross",
    "pedigree diagram": "life_sciences_pedigree",
    "pedigree": "life_sciences_pedigree",
    "meiosis": "life_sciences_genetics",
    "finance and tax": "mathematical_literacy_finance_tax",
    "mathematical literacy": "mathematical_literacy_finance_tax",
    "taxation": "mathematical_literacy_finance_tax",
    "income tax": "mathematical_literacy_finance_tax",
    "sars tax": "mathematical_literacy_finance_tax",
    "paye": "mathematical_literacy_finance_tax",
    "maps and scales": "mathematical_literacy_maps_scales",
    "map scales": "mathematical_literacy_maps_scales",
    "topographic map": "mathematical_literacy_maps_scales",
    "scale": "mathematical_literacy_maps_scales",
    "travel time": "mathematical_literacy_maps_scales",
    "complex numbers": "technical_mathematics_complex_numbers",
    "technical mathematics": "technical_mathematics_complex_numbers",
    "complex numbers polar": "technical_mathematics_complex_numbers",
    "polar form": "technical_mathematics_complex_numbers",
    "de moivre": "technical_mathematics_complex_numbers",
    "mensuration": "technical_mathematics_mensuration",
    "trapezoidal rule": "technical_mathematics_mensuration",
    "mid-ordinate rule": "technical_mathematics_mensuration",
    "irregular area": "technical_mathematics_mensuration",
    # Natural Sciences aliases
    "electric circuits": "natural_sciences_electric_circuits",
    "circuits": "natural_sciences_electric_circuits",
    "circuit analysis": "natural_sciences_electric_circuits",
    "ohm's law": "natural_sciences_electric_circuits",
    "series and parallel resistors": "natural_sciences_electric_circuits",
    "chemical reactions": "natural_sciences_chemical_reactions",
    "balancing equations": "natural_sciences_chemical_reactions",
    "reactions": "natural_sciences_chemical_reactions",
    "acids and bases": "natural_sciences_chemical_reactions",
    "neutralisation": "natural_sciences_chemical_reactions",
    "manufacturing": "grade12_accounting_cost_accounting",
    "cost accounting": "grade12_accounting_cost_accounting",
    "production cost statement": "grade12_accounting_cost_accounting",
    "analysis and intepretation of financial statements": "grade12_accounting_financial_indicators",
    "analysis and interpretation of financial statements": "grade12_accounting_financial_indicators",
    "polynomials": "grade12_math_functions",

    # Senior Phase Math & Arithmetic Foundation aliases
    "collect organise and summarise data": "grade8_math_data_handling",
    "interpret analyse and report on data": "grade8_math_data_handling",
    "working with whole numbers": "grade8_math_whole_numbers",
    "whole numbers": "grade8_math_whole_numbers",
    "integers": "grade8_math_integers",
    "numeric patterns": "grade8_math_patterns",
    "relationships between variables": "grade8_math_functions",
    "the decimal notation for fractions": "grade9_math_decimal_notation",
    "fractions in decimal notation": "grade9_math_decimal_notation",
    "common fractions": "grade9_math_fractions",
    "graph paper types": "grade8_math_graph_paper_types",

    # EMS Senior Phase aliases
    "cash receipts journal and cash payments journal (sole trader)": "grade9_ems_crj_cpj",
    "credit transactions (creditors 1)": "grade9_ems_creditors_journal",
    "credit transactions (creditors 2)": "grade9_ems_creditors_journal",
    "credit transactions (debtors 1)": "grade9_ems_debtors_journal",
    "credit transactions (debtors 2)": "grade9_ems_debtors_journal",
    "transactions (cash and credit)": "grade9_ems_crj_cpj",
    "cash payments journal for a services business": "grade8_ems_cpj_and_crj",
    "cash receipts journal for a services business 1": "grade8_ems_crj",
    "cash receipts journal for a services business 2": "grade8_ems_crj",
    "general ledger and trial balance of a service business": "grade8_ems_accounting_cycle",
    "levels and functions of management": "grade8_ems_gap",

    # Business Studies aliases
    "relationships & team performance": "grade10_bs_entrepreneurial_qualities",
    "relationships and team performance": "grade10_bs_entrepreneurial_qualities",
    "self management": "grade10_bs_entrepreneurial_qualities",
    "assessment of enterpreneural qualities in business": "grade10_bs_entrepreneurial_qualities",
    "assessment of entrepreneurial qualities in business": "grade10_bs_entrepreneurial_qualities",
    "citizenship & responsibilities": "grade10_bs_social_responsibility",
    "citizenship and responsibilities": "grade10_bs_social_responsibility",
    "creative thinking & problem solving": "grade10_bs_creative_thinking",
    "creative thinking and problem solving": "grade10_bs_creative_thinking",
    "ethics and professionalism": "grade10_accounting_ethics",
    "stress crisis & change management": "grade11_bs_adapting_to_challenges",
    "stress crisis and change management": "grade11_bs_adapting_to_challenges",
    "team dynamics & conflict management": "grade12_bs_essay",
    "team dynamics and conflict management": "grade12_bs_essay",
    "transformation of a business plan into an action plan": "grade10_bs_business_plans",
    "business sectors & their environments": "grade10_bs_business_sectors",
    "business sectors and their environments": "grade10_bs_business_sectors",
    "human rights inclusivity & environmental issues": "grade10_bs_social_responsibility",
    "human rights inclusivity and environmental issues": "grade10_bs_social_responsibility",
    "investement securities": "grade12_bs_investments_management",
    "presentations & data responses": "grade10_bs_presentation",
    "presentations and data responses": "grade10_bs_presentation",
    "team perfomance assessment and conflict management": "grade12_bs_essay",
    "team performance assessment and conflict management": "grade12_bs_essay",

    # Technical Mathematics aliases
    "circles angles and angular movement": "technical_mathematics_mensuration",
    "circles  angles and angular movement": "technical_mathematics_mensuration",
    "equalities and inequalities": "grade10_math_equations_inequalities",
    "finance and growth": "grade11_math_finance_growth_decay",
    "number systems": "grade10_math_algebraic_expressions",
    "functions and graphs": "grade10_math_functions",
    "logarithms": "grade11_math_exponents_surds",
    "differentiation": "grade12_math_differential_calculus",
    "euclidean geometry proportionality and similarity": "grade11_math_circle_geometry_theorems",
    "integration": "technical_mathematics_mensuration",

    # Mathematical Literacy aliases
    "assembly diagrams floor plans and packaging": "mathematical_literacy_maps_scales",
    "conversions and time": "mathematical_literacy_maps_scales",
    "conversions & time": "mathematical_literacy_maps_scales",
    "financial documents and tariff ystems": "mathematical_literacy_tariffs_tax_brackets",
    "financial documents and tariff systems": "mathematical_literacy_tariffs_tax_brackets",
    "tariffs and tax": "mathematical_literacy_tariffs_tax_brackets",
    "water and electricity tariffs": "mathematical_literacy_tariffs_tax_brackets",
    "measurement of perimeter and area": "grade10_math_measurements",
    "measuring length weight volume and temperature": "grade10_math_measurements",
    "numbers and calculations with numbers": "grade8_math_whole_numbers",
    "patterns relationships and representations": "grade8_math_functions",
    "personal income expenditure and budgets": "mathematical_literacy_tariffs_tax_brackets",
    "area and volume": "grade10_math_measurements",
    "exchange rates": "mathematical_literacy_finance_tax",
    "interest banking and inflation": "mathematical_literacy_finance_tax",
    "interest banking inflation": "mathematical_literacy_finance_tax",
    "plans and other representations": "mathematical_literacy_maps_scales",
    "weight and temperatute": "grade10_math_measurements",
    "measuring weight bmi medicine dosages": "grade10_math_measurements",
    "lengths perimeter area and volume": "grade10_math_measurements",

    # Physical Sciences (Grades 10, 11, 12) aliases
    "electrostatics": "physical_sciences_electrostatics",
    "electromagnetism": "physical_sciences_electromagnetism",
    "coulombs law": "physical_sciences_electrostatics",
    "coulomb's law": "physical_sciences_electrostatics",
    "faradays law": "physical_sciences_electromagnetism",
    "faraday's law": "physical_sciences_electromagnetism",
    "electric field": "physical_sciences_electrostatics",
    "magnetic flux": "physical_sciences_electromagnetism",
    "reaction in aqeuous solution": "natural_sciences_chemical_reactions",
    "the hydrosphere": "grade10_physical_sciences_matter_materials",
    "the particles that substances are made of": "grade10_physical_sciences_matter_materials",
    "classification of matter": "grade10_physical_sciences_matter_materials",
    "physical and chemical changes": "natural_sciences_chemical_reactions",
    "quantitative aspects of chemical change": "physical_sciences_chemistry_equilibrium",
    "representing chemical change": "natural_sciences_chemical_reactions",
    "units of measurement applied": "grade10_physical_sciences_matter_materials",
    "states of matter and the kinetic theory molecular theory": "physical_sciences_ideal_gases_thermal",
    "transverse pulses": "grade10_physical_sciences_waves_sound_light",
    "transverse waves": "grade10_physical_sciences_waves_sound_light",
    "longitudinal waves": "grade10_physical_sciences_waves_sound_light",
    "sound": "grade10_physical_sciences_waves_sound_light",
    "electromagnetic radiation": "grade10_physical_sciences_waves_sound_light",
    "magnetism": "natural_sciences_electric_circuits",
    "the atom": "grade10_physical_sciences_matter_materials",
    "the periodic table": "grade10_physical_sciences_matter_materials",
    "chemical bonding": "grade10_physical_sciences_matter_materials",
    "motion in one dimension": "physical_sciences_mechanics",
    "mechanical energy": "physical_sciences_work_energy_power",
    "vectors in two dimensions": "grade11_physical_sciences_vectors_newton",
    "newton's laws": "grade11_physical_sciences_vectors_newton",
    "the lithosphere": "grade10_physical_sciences_matter_materials",
    "atomic combinations": "grade10_physical_sciences_matter_materials",
    "energy and chemical change": "physical_sciences_electrochemistry",
    "geometrical optics": "physical_sciences_geometrical_optics",
    "units applied": "grade10_physical_sciences_matter_materials",
    "2d and 3d wavefronts": "physical_sciences_geometrical_optics",
    "intermolecular forces": "grade10_physical_sciences_matter_materials",
    "ideal gases": "physical_sciences_ideal_gases_thermal",
    "types of reaction": "natural_sciences_chemical_reactions",
    "vertical projectile motion in one dimension": "grade12_physical_sciences_vertical_projectile",
    "rate and extent of reaction": "physical_sciences_electrochemistry",
    "optical phenomena and properties of matter": "physical_sciences_geometrical_optics",
    "work energy and power": "physical_sciences_work_energy_power",
    "electrochemical reactions": "physical_sciences_electrochemistry",
    "electrodynamics": "natural_sciences_electric_circuits",
    "organic molecules": "natural_sciences_chemical_reactions",
    "the chemical industry": "physical_sciences_chemistry_equilibrium",
    "skills for science": "grade10_physical_sciences_matter_materials",

    # Life Sciences (Grades 10, 11, 12) aliases
    "biospheres to ecosystems": "life_sciences_environmental_population",
    "cells the basic units of life": "life_sciences_genetics",
    "history of life on earth": "life_sciences_environmental_population",
    "introduction to life sciences": "life_sciences_genetics",
    "the chemistry of life": "life_sciences_genetics",
    "biodiversity and classification": "life_sciences_environmental_population",
    "cell division": "life_sciences_meiosis_human_reproduction",
    "plant and animal tissues": "life_sciences_human_organ_systems",
    "support and transport systems in plants": "life_sciences_photosynthesis_respiration",
    "transport systems in animals": "life_sciences_human_organ_systems",
    "support systems in animals": "life_sciences_human_organ_systems",
    "biodiversity and classification of microorganisms": "life_sciences_environmental_population",
    "gaseous exchange": "life_sciences_human_organ_systems",
    "photosynthesis": "life_sciences_photosynthesis_respiration",
    "animal nutrition": "life_sciences_human_organ_systems",
    "biodiversity of plants": "life_sciences_environmental_population",
    "excretion in humans": "life_sciences_human_organ_systems",
    "biodiversity of animals": "life_sciences_environmental_population",
    "cellular respiration": "life_sciences_photosynthesis_respiration",
    "population ecology": "life_sciences_environmental_population",
    "human impact on the environment": "life_sciences_environmental_population",
    "dna the code of life": "life_sciences_genetics",
    "human responses to the environment": "life_sciences_human_organ_systems",
    "reproductive strategies in vertebrates": "life_sciences_meiosis_human_reproduction",
    "evolution by natural selection": "life_sciences_genetics",
    "human evolution": "life_sciences_genetics",
    "plant responses to the environment": "life_sciences_photosynthesis_respiration",
    "the human endocrine system and homeostasis": "life_sciences_human_organ_systems",

    # Natural Sciences (Grades 7, 8, 9) aliases
    "acids bases and neutral substances": "physical_sciences_electrochemistry",
    "acids bases and the ph value": "physical_sciences_electrochemistry",
    "biodiversity": "life_sciences_environmental_population",
    "energy transfer to surroundings": "physical_sciences_ideal_gases_thermal",
    "heat energy transfer": "physical_sciences_ideal_gases_thermal",
    "heat insulation and energy saving": "physical_sciences_ideal_gases_thermal",
    "historical development of astronomy": "natural_sciences_senior_phase_astronomy",
    "potential and kinetic energy": "physical_sciences_work_energy_power",
    "properties of materials": "natural_sciences_chemical_reactions",
    "relationship of the moon to the earth": "natural_sciences_senior_phase_astronomy",
    "relationship of the sun to the earth": "natural_sciences_senior_phase_astronomy",
    "separating mixtures": "natural_sciences_chemical_reactions",
    "sexual reproduction": "life_sciences_meiosis_human_reproduction",
    "sources of energy": "physical_sciences_work_energy_power",
    "the biosphere": "life_sciences_environmental_population",
    "the periodic table of elements": "grade10_physical_sciences_matter_materials",
    "variation": "life_sciences_genetics",
    "atoms": "grade10_physical_sciences_matter_materials",
    "beyond the solar system": "natural_sciences_senior_phase_astronomy",
    "energy transfer in electrical systems": "natural_sciences_electric_circuits",
    "interactions and interdependence within the environment": "life_sciences_environmental_population",
    "looking into space": "natural_sciences_senior_phase_astronomy",
    "microorganisms": "life_sciences_environmental_population",
    "particle model of matter": "physical_sciences_ideal_gases_thermal",
    "photosynthesis and respiration": "life_sciences_photosynthesis_respiration",
    "static electricity": "natural_sciences_electric_circuits",
    "the solar system": "natural_sciences_senior_phase_astronomy",
    "visible light": "physical_sciences_geometrical_optics",
    "birth life and the death of a star": "natural_sciences_senior_phase_astronomy",
    "cells as the basic units of life": "life_sciences_genetics",
    "circulatory and respiratory systems": "life_sciences_human_organ_systems",
    "compounds": "natural_sciences_chemical_reactions",
    "cost of electrical energy": "natural_sciences_electric_circuits",
    "digestive system": "life_sciences_human_organ_systems",
    "electric cells as energy systems": "natural_sciences_electric_circuits",
    "energy and the national electricity grid": "natural_sciences_electric_circuits",
    "forces": "physical_sciences_mechanics",
    "mining of mineral resources": "grade10_physical_sciences_matter_materials",
    "resistance": "natural_sciences_electric_circuits",
    "safety with electricity": "natural_sciences_electric_circuits",
    "systems in the human body": "life_sciences_human_organ_systems",
    "the atmosphere": "grade10_physical_sciences_matter_materials",
    "the earth as a system": "natural_sciences_senior_phase_astronomy",
    "glossary1": "natural_sciences_chemical_reactions",
    "glossary2": "natural_sciences_chemical_reactions",
    "glossary3": "natural_sciences_chemical_reactions",
    "glossary4": "natural_sciences_chemical_reactions",
    "graphs": "grade8_math_functions",
}


def resolve_generator_key(topic: str, grade: str = "10", subject: str = "Mathematics") -> str:
    """Finds the registered generator key from topic name, slug, or alias."""
    # 1. Direct match in registry
    if topic in ALL_GENERATORS:
        return topic

    clean = topic.strip().lower().replace("_", " ")
    subj_lower = subject.lower()

    is_math = "math" in subj_lower and "technical" not in subj_lower and "literacy" not in subj_lower
    is_acct = "acct" in subj_lower
    is_bs = "business" in subj_lower or "ems" in subj_lower
    stop_words = {"of", "the", "and", "in", "to", "for", "a", "an", "on", "at", "by", "with", "from"}
    meaningful_words = [w for w in clean.split() if w not in stop_words and len(w) > 2]

    # 2. Check alias map
    if clean in TOPIC_ALIASES:
        resolved = TOPIC_ALIASES[clean]
        grade_num = "".join(ch for ch in str(grade) if ch.isdigit())
        if (is_math or is_acct or is_bs) and grade_num and not resolved.startswith(f"grade{grade_num}_"):
            subj_code = "math" if is_math else ("acct" if is_acct else "bs")
            target_prefix = f"grade{grade_num}_{subj_code}_"
            for k in ALL_GENERATORS:
                if k.startswith(target_prefix) and any(w in k for w in meaningful_words):
                    return k
        return resolved

    # 3. Subject-level direct routing for science & tech
    if "natural" in subj_lower or "circuit" in clean:
        return "natural_sciences_electric_circuits"
    if "reaction" in clean or "acid" in clean or "base" in clean:
        return "natural_sciences_chemical_reactions"
    if "life" in subj_lower or "genetics" in clean or "inheritance" in clean:
        return "life_sciences_genetics"
    if "momentum" in clean or "impulse" in clean or "collision" in clean:
        return "physical_sciences_momentum_impulse"
    if "physical" in subj_lower or "mechanics" in clean:
        return "physical_sciences_mechanics"
    if "literacy" in subj_lower:
        return "mathematical_literacy_finance_tax"
    if "technical" in subj_lower:
        return "technical_mathematics_complex_numbers"

    # 4. Fuzzy search for key prefix
    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "10"
    if (is_math or is_acct or is_bs) and grade_num:
        subj_code = "math" if is_math else ("acct" if is_acct else "bs")
        target_prefix = f"grade{grade_num}_{subj_code}_"
        for k in ALL_GENERATORS:
            if k.startswith(target_prefix) and any(w in k for w in meaningful_words):
                return k

    # 5. Fallback for Business Studies / EMS to Combinatorial Engine
    if "business" in subj_lower or "ems" in subj_lower:
        return "grade10_bs_combinatorial"

    # Default fallback: Only if topic is a math-related request or explicitly generic
    if "math" in subj_lower and any(w in clean for w in ["algebra", "expression", "general", "concept", "mixed"]):
        return "grade10_math_algebraic_expressions"

    return ""


# ============================================================================
# 6-PILLAR NORMALIZATION & ENRICHMENT
# ============================================================================

def _normalize_question(q: Dict[str, Any], default_term: int = 1) -> Dict[str, Any]:
    """Ensures a single question dictionary strictly complies with the 6-pillar contract."""
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

    return {
        **q,
        "id": qid,
        "question_id": qid,
        "term": int(q.get("term") or default_term),
        "caps_weight_percent": int(q.get("caps_weight_percent") or 15),
        "suggested_duration_mins": int(q.get("suggested_duration_mins") or max(2, int(marks * 1.2))),
        "mode": q.get("mode") or "compound",
        "marks": marks,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": tags,
    }


def _normalize_generator_result(result: Any, default_term: int = 1) -> List[Dict[str, Any]]:
    """Ensures the generator returns a normalized list of 6-pillar question dicts."""
    raw_list: List[Dict[str, Any]] = []
    if isinstance(result, list):
        raw_list = result
    elif isinstance(result, dict):
        if result.get("success") is False:
            raise ValueError(result.get("error") or "Generation failed")
        questions = result.get("questions")
        if isinstance(questions, list):
            raw_list = questions
        else:
            raw_list = [result]
    else:
        raise ValueError("Generator returned an unsupported response shape")

    return [_normalize_question(q, default_term) for q in raw_list]


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
    if seed is not None:
        config["seed"] = seed
        random.seed(seed)

    result = generator(subskill=subskill, difficulty=difficulty, count=count, **config)
    term_val = int(config.get("term", 1))
    return _normalize_generator_result(result, default_term=term_val)


def get_generator_for_topic(topic: str, grade: str = "12", subject: str = "Mathematics") -> Optional[Callable]:
    """Retrieves generator callable for a topic, alias, or registered key."""
    gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
    return ALL_GENERATORS.get(gen_key)

