import random
from typing import Any, Dict, List

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


# Grade 10 Business Studies generator registry.
# Each entry maps a topic key to the generator callable.
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
}

# Grade 7 EMS generator registry
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

# Grade 8 EMS generator registry
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
}

# Grade 9 EMS generator registry
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

ALL_GENERATORS = {
    **GRADE10_BS_GENERATORS,
    **GRADE7_EMS_GENERATORS,
    **GRADE8_EMS_GENERATORS,
    **GRADE9_EMS_GENERATORS,
}


def _normalize_generator_result(result: Any) -> List[Dict[str, Any]]:
    """Ensures the generator returns a list of question dicts."""
    if isinstance(result, list):
        return result
    if isinstance(result, dict):
        if result.get("success") is False:
            raise ValueError(result.get("error") or "Generation failed")
        questions = result.get("questions")
        if isinstance(questions, list):
            return questions
    raise ValueError("Generator returned an unsupported response shape")


def generate_variant(
    topic: str,
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    seed: int = None,
    extra_config: Dict[str, Any] = None,
) -> List[Dict[str, Any]]:
    """Generates an isomorphic variant of a question.

    The agent never authors questions; it always routes through this registry.
    Supports Grade 10 Business Studies and Grade 7-9 EMS topics.
    """
    generator = ALL_GENERATORS.get(topic)
    if not generator:
        raise ValueError(f"No generator registered for topic: {topic}")

    config = dict(extra_config or {})
    if seed is not None:
        config["seed"] = seed
        random.seed(seed)

    result = generator(subskill=subskill, difficulty=difficulty, count=count, **config)
    return _normalize_generator_result(result)
