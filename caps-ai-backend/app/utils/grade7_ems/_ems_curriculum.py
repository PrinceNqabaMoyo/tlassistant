"""Curriculum document parser for Grade 7 EMS section-based progression.

Reads `.md` topic files from `curriculum_docs/EMS_Gr7/` and derives scaffold steps
with recommended question formats per section.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.utils.grade10_business_studies._bs_curriculum import (
    parse_md_sections,
    _find_md_file,
)

# Map topic keys → relative paths under curriculum_docs/
TOPIC_MD_MAP: Dict[str, str] = {
    # Term 1
    "grade7_ems_money_and_needs": "EMS_Gr7/Term 1/1-The history of money.md",
    "grade7_ems_needs_and_wants": "EMS_Gr7/Term 1/2-Needs and wants.md",
    "grade7_ems_goods_and_services": "EMS_Gr7/Term 1/3-Goods and services.md",
    "grade7_ems_businesses": "EMS_Gr7/Term 1/4-Businesses.md",
    # Term 2
    "grade7_ems_accounting_concepts": "EMS_Gr7/Term 2/5-Accounting concepts.md",
    "grade7_ems_income_and_expenses": "EMS_Gr7/Term 2/6-Income and expenses.md",
    "grade7_ems_budgets": "EMS_Gr7/Term 2/7-Budgets.md",
    # Term 3
    "grade7_ems_the_entrepreneur": "EMS_Gr7/Term 3/8-The entrepreneur.md",
    "grade7_ems_starting_a_business": "EMS_Gr7/Term 3/9-Starting a business.md",
    "grade7_ems_entrepreneurs_day": "EMS_Gr7/Term 3/10-Entrepreneur's Day.md",
    "grade7_ems_inequality_and_poverty": "EMS_Gr7/Term 3/11-Inequality and poverty.md",
}


def get_g7_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a Grade 7 EMS topic."""
    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)


def get_g7_section_for_topic(topic: str, section_key: str) -> Optional[Dict[str, Any]]:
    """Get a specific section by key for a Grade 7 topic."""
    sections = get_g7_topic_sections(topic)
    for sec in sections:
        if sec["key"] == section_key:
            return sec
    return None
