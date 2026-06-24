"""Grade 11 Business Studies — Term 1: Influences on the business environments."""
from __future__ import annotations

from typing import Any, Dict, List, Callable

from .._bs_common import build_generate, make_mcq, make_typed, make_wordbank, make_matching, make_crossword, make_essay

PREFIX = "g11_bs_influences"
VAID = "g11_bs_influences"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which factor is part of the macro environment?",
            options=["Suppliers", "Customers", "Technology", "Competitors"],
            correct_index=2,
            explanation="Technology is a macro-environmental factor (PESTLE).",
            marks=2,
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how political factors can influence a business in South Africa.",
            marking_points=[
                "Government policies affect operations",
                "Labour legislation impacts employment",
                "Political stability encourages investment"
            ],
            sample_answer="Political factors such as government policies, labour legislation, and political stability directly influence business operations and investment decisions.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
        "word_bank": [],
        "matching": [],
        "crossword": [],
        "essay": [],
    }


generate_influences = build_generate(_pools)
