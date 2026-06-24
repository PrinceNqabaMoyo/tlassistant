"""Grade 12 Business Studies curriculum parser.

Extends the Grade 10 parser with G12-specific topic-to-md mappings.
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
TOPIC_MD_MAP: Dict[str, str] = {
    # Term 1
    "grade12_bs_macro_environment_strategies": "BusinessStudies_Gr12/Term1/Macro environment-Business strategies.md",
    "grade12_bs_impact_of_legislation": "BusinessStudies_Gr12/Term1/The implications of the legislation on the human resources function.md",
    "grade12_bs_human_resources_function": "BusinessStudies_Gr12/Term1/The implications of the legislation on the human resources function.md",
    "grade12_bs_creative_thinking_problem_solving": "BusinessStudies_Gr12/Term1/Creative thinking and Problem Solving.md",
    "grade12_bs_ethics_and_professionalism": "BusinessStudies_Gr12/Term1/Ethics and professionalism.md",
    # Term 2
    "grade12_bs_business_sectors_environments": "BusinessStudies_Gr12/Term2/6 Business sectors and their environm.md",
    "grade12_bs_quality_of_performance": "BusinessStudies_Gr12/Term2/7 Quality of performance.md",
    "grade12_bs_management_and_leadership": "BusinessStudies_Gr12/Term2/8 Management and leadership.md",
    "grade12_bs_investment_securities": "BusinessStudies_Gr12/Term2/9 Investment Securities.md",
    "grade12_bs_investment_insurance": "BusinessStudies_Gr12/Term2/10 Investment Insurance.md",
    "grade12_bs_team_performance_conflict": "BusinessStudies_Gr12/Term2/11 Team performance assessment and con.md",
    # Term 3
    "grade12_bs_human_rights_inclusivity": "BusinessStudies_Gr12/Term 3/12 Human rights, inclusivity and en.md",
    "grade12_bs_social_responsibility_csr_csi": "BusinessStudies_Gr12/Term 3/13-Social responsibility and corpor.md",
    "grade12_bs_presentation_data_responses": "BusinessStudies_Gr12/Term 3/14 Presentation and data responses.md",
    "grade12_bs_forms_of_ownership_success": "BusinessStudies_Gr12/Term 3/15 Forms of ownership Criteria for success or failure.md",
}


def get_g12_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a Grade 12 topic."""
    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)
