"""Curriculum document parser for Grade 9 EMS section-based progression.

Reads `.md` topic files from `curriculum_docs/EMS_Gr9/` and derives scaffold steps
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
    "grade9_ems_crj": "EMS_Gr9/Term 1/1-Cash Receipts Journal and Cash Payments Journal (Sole Trader).md",
    "grade9_ems_cpj": "EMS_Gr9/Term 1/1-Cash Receipts Journal and Cash Payments Journal (Sole Trader).md",
    "grade9_ems_crj_cpj": "EMS_Gr9/Term 1/1-Cash Receipts Journal and Cash Payments Journal (Sole Trader).md",
    "grade9_ems_economic_systems": "EMS_Gr9/Term 1/2-Economic Systems.md",
    "grade9_ems_general_ledger": "EMS_Gr9/Term 1/3-General Ledger and Trial Balance.md",
    "grade9_ems_circular_flow": "EMS_Gr9/Term 1/4-The Circular flow.md",
    # Term 2
    "grade9_ems_debtors_journal": "EMS_Gr9/Term 2/5-Credit transactions- Debtors 1.md",
    "grade9_ems_price_theory": "EMS_Gr9/Term 2/6-Price theory.md",
    "grade9_ems_sectors_of_economy": "EMS_Gr9/Term 2/7-Sectors of the economy.md",
    # Term 3
    "grade9_ems_trade_unions": "EMS_Gr9/Term 3/8-Trade unions.md",
    "grade9_ems_debtors_ledger": "EMS_Gr9/Term 3/9-Credit transactions Debtors (2).md",
    "grade9_ems_creditors_journal": "EMS_Gr9/Term 3/10-Credit transactions Creditors (1).md",
    "grade9_ems_business_functions": "EMS_Gr9/Term 3/11-Functions of a Business.md",
    "grade9_ems_creditors_journal_2": "EMS_Gr9/Term 3/12-Credit transactions Creditors (2).md",
}


def get_g9_topic_sections(topic: str) -> List[Dict[str, Any]]:
    """Get scaffold sections for a Grade 9 EMS topic."""
    rel_path = TOPIC_MD_MAP.get(topic)
    if not rel_path:
        return []

    md_path = _find_md_file(rel_path)
    if not md_path:
        return []

    return parse_md_sections(md_path)


def get_g9_section_for_topic(topic: str, section_key: str) -> Optional[Dict[str, Any]]:
    """Get a specific section by key for a Grade 9 topic."""
    sections = get_g9_topic_sections(topic)
    for sec in sections:
        if sec["key"] == section_key:
            return sec
    return None
