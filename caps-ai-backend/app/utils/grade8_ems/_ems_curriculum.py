"""Curriculum document parser for Grade 8 EMS section-based progression.

Reads `.md` topic files from `curriculum_docs/EMS_Gr8/` and derives scaffold steps
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
    "grade8_ems_gov_and_society": "EMS_Gr8/Term 1/1-Government.md",
    "grade8_ems_government": "EMS_Gr8/Term 1/1-Government.md",
    "grade8_ems_national_budget": "EMS_Gr8/Term 1/2-National Budget.md",
    "grade8_ems_standard_of_living": "EMS_Gr8/Term 1/3-Standard of living.md",
    "grade8_ems_accounting_basics": "EMS_Gr8/Term 1/4-Accounting concepts.md",
    "grade8_ems_accounting_concepts": "EMS_Gr8/Term 1/4-Accounting concepts.md",
    "grade8_ems_source_documents": "EMS_Gr8/Term 1/5-Source Documents.md",
    # Term 2
    "grade8_ems_accounting_cycle": "EMS_Gr8/Term 2/6-The accounting cycle.md",
    "grade8_ems_crj": "EMS_Gr8/Term 2/7-Cash Receipts Journal of a services (1).md",
    "grade8_ems_factors_of_production": "EMS_Gr8/Term 2/8-Factors of production.md",
    "grade8_ems_markets_and_production": "EMS_Gr8/Term 2/8-Factors of production.md",
    "grade8_ems_markets": "EMS_Gr8/Term 2/9-The markets.md",
    # Term 3
    "grade8_ems_cpj_and_crj": "EMS_Gr8/Term 3/11-Cash Payments Journal of a services business.md",
    "grade8_ems_ownership": "EMS_Gr8/Term 3/12-Forms of ownership.md",
    "grade8_ems_forms_of_ownership": "EMS_Gr8/Term 3/12-Forms of ownership.md",
}


def get_g8_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a Grade 8 EMS topic."""
    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)


def get_g8_section_for_topic(topic: str, section_key: str) -> Optional[Dict[str, Any]]:
    """Get a specific section by key for a Grade 8 topic."""
    sections = get_g8_topic_sections(topic)
    for sec in sections:
        if sec["key"] == section_key:
            return sec
    return None
