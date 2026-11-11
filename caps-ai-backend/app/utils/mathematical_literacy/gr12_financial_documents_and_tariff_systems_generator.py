"""Grade 12 Mathematical Literacy - Term 1: FINANCIAL DOCUMENTS AND TARIFF SYSTEMS Generator.

Exhaustively grounded in:
  - curriculum_source_files/Textbook_MathematicalLiteracy_Gr12_Financial-documents-and-tariff-systems.pdf
  - Via Afrika Mathematical Literacy Grade 12 (LB Pages 34-57)
  - South African National Curriculum Standards (CAPS pp. 50-52)

Features:
  - 52 distinct subskill archetypes covering:
      * Municipal Water & Sanitation Tariffs (Subskills 1 to 8)
      * Domestic & Commercial Electricity Tariffs (Subskills 9 to 16)
      * Telecommunications, Mobile Data & Broadband Tariffs (Subskills 17 to 24)
      * Public Transport, Commuter Economics & Logistics (Subskills 25 to 32)
      * Banking Fee Structures & Account Statements (Subskills 33 to 40)
      * Small Business Costing, Pricing & Break-Even Analysis (Subskills 41 to 46)
      * Financial Statements, Budgets & National Economic Data (Subskills 47 to 52)
  - Full step-by-step pedagogical worked solutions with explicit mark allocations:
      Step 1: Formula / Document Line Item Identification [1 Mark: Method]
      Step 2: Technical Substitution & Progressive Calculation [1 Mark: Method]
      Step 3: Solution Formulation & Final Units [1 Mark: Accuracy]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 1 245,50).
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .gr12_financial_documents_and_tariffs import BUILDERS, DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Mathematical Literacy: Financial Documents and Tariff Systems."""
    r = random.Random(seed)
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill

        if not chosen_subskill and archetype_index is not None:
            if 0 <= archetype_index < len(SUBSKILLS):
                chosen_subskill = SUBSKILLS[archetype_index]
            else:
                chosen_subskill = SUBSKILLS[archetype_index % len(SUBSKILLS)]

        if not chosen_subskill or chosen_subskill not in DISPATCH_TABLE:
            chosen_subskill = r.choice(SUBSKILLS)

        gen_fn = DISPATCH_TABLE[chosen_subskill]
        item = gen_fn(r)
        results.append(item)

    return results


def get_subskills() -> List[str]:
    """Return all 52 supported subskill keys in curriculum sequence."""
    return list(SUBSKILLS)
