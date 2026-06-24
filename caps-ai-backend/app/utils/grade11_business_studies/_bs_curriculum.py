"""Grade 11 Business Studies curriculum parser.

Extends the Grade 10 parser with G11-specific topic-to-md mappings.
"""
from __future__ import annotations

from typing import Any, Dict, List

from app.utils.grade10_business_studies._bs_curriculum import (
    parse_md_sections,
    get_topic_sections,
    get_section_for_topic,
    _find_md_file,
)

# Map topic keys → relative paths under curriculum_docs/
# These are the actual curriculum .md files that drive progression.
TOPIC_MD_MAP: Dict[str, str] = {
    # Term 1
    "grade11_bs_influences_on_business_environments": "BusinessStudies_Gr11/Term 1/1 Influences on business environments.md",
    "grade11_bs_challenges_of_the_business_environments": "BusinessStudies_Gr11/Term 1/2 The challenges of the business environments.md",
    "grade11_bs_adapting_to_challenges": "BusinessStudies_Gr11/Term 1/3 Adapting to the challenges in the business environments.md",
    "grade11_bs_socio_economic_issues": "BusinessStudies_Gr11/Term 1/4 Contemporary socio-economic issues and businesses.md",
    "grade11_bs_business_sectors": "BusinessStudies_Gr11/Term 1/5 Business Sectors.md",
    "grade11_bs_benefits_of_a_company": "BusinessStudies_Gr11/Term 1/6 Benefits of a company over other forms of ownership.md",
    "grade11_bs_avenues_of_acquiring_businesses": "BusinessStudies_Gr11/Term 1/7 Avenues of acquiring businesses.md",
    # Term 2
    "grade11_bs_creative_thinking": "BusinessStudies_Gr11/Term 2/8 Creative thinking and problem solving.md",
    "grade11_bs_stress_crisis_change": "BusinessStudies_Gr11/Term 2/9 Stress, crisis and change management.md",
    "grade11_bs_marketing_function": "BusinessStudies_Gr11/Term 2/10 The marketing function.md",
    "grade11_bs_production_function": "BusinessStudies_Gr11/Term 2/11 The production function.md",
    "grade11_bs_professionalism_and_ethics": "BusinessStudies_Gr11/Term 2/12 Professionalism and ethics.md",
    # Term 3
    "grade11_bs_entrepreneurial_assessment": "BusinessStudies_Gr11/Term 3/13-Assessment of entrepreneurial qu.md",
    "grade11_bs_citizenship_responsibilities": "BusinessStudies_Gr11/Term 3/14-Citizenship and responsibilities.md",
    "grade11_bs_business_plan_transformation": "BusinessStudies_Gr11/Term 3/15-Transformation of a business plan into an action plan.md",
    "grade11_bs_start_business_venture": "BusinessStudies_Gr11/Term 3/16- Start a business venture based on an action plan.md",
    "grade11_bs_presentation_of_information": "BusinessStudies_Gr11/Term 3/17 Presentation of business information.md",
}


def get_g11_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a Grade 11 topic."""
    from app.utils.grade10_business_studies._bs_curriculum import _curriculum_docs_dir
    import os

    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)
