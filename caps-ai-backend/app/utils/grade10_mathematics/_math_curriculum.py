"""Grade 10 Mathematics curriculum metadata (scaffold sections + subskills).

Drives the frontend topic registry and the scaffold step ordering. Mirrors the
role of ``_bs_curriculum.py`` for Business Studies but is hand-defined here
(maths scaffolds are subskill-ordered rather than format-pool driven).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

TOPICS: Dict[str, Dict[str, Any]] = {
    "grade10_math_algebraic_expressions": {
        "title": "Algebraic Expressions",
        "term": 1,
        "subskills": [
            {"key": "real_numbers", "title": "The real number system"},
            {"key": "rounding", "title": "Rounding off"},
            {"key": "products", "title": "Products (expanding)"},
            {"key": "factorise_common", "title": "Common factors"},
            {"key": "factorise_diff_squares", "title": "Difference of two squares"},
            {"key": "factorise_trinomial", "title": "Quadratic trinomials"},
            {"key": "simplify_fractions", "title": "Simplifying algebraic fractions"},
        ],
        "sections": [
            {"key": "real_numbers", "title": "The real number system", "formats": ["real_numbers"]},
            {"key": "rounding", "title": "Rounding off", "formats": ["rounding"]},
            {"key": "products", "title": "Products", "formats": ["products"]},
            {"key": "factorisation", "title": "Factorisation", "formats": ["factorise_common", "factorise_diff_squares", "factorise_trinomial"]},
            {"key": "fractions", "title": "Algebraic fractions", "formats": ["simplify_fractions"]},
        ],
    },
    "grade10_math_trigonometry": {
        "title": "Trigonometry",
        "term": 1,
        "subskills": [
            {"key": "identify_sides", "title": "Opposite, adjacent & hypotenuse"},
            {"key": "ratio_from_triangle", "title": "Trig ratios from a triangle"},
            {"key": "calculator_value", "title": "Using a calculator"},
            {"key": "special_angles", "title": "Special angles (no calculator)"},
            {"key": "find_length", "title": "Finding a side length"},
            {"key": "find_angle", "title": "Finding an angle"},
            {"key": "solve_equation", "title": "Solving trig equations"},
        ],
        "sections": [
            {"key": "identify_sides", "title": "Opposite, adjacent & hypotenuse", "formats": ["identify_sides"]},
            {"key": "ratios", "title": "Trig ratios (SohCahToa)", "formats": ["ratio_from_triangle"]},
            {"key": "calculator", "title": "Calculator skills", "formats": ["calculator_value"]},
            {"key": "special_angles", "title": "Special angles", "formats": ["special_angles"]},
            {"key": "find_length", "title": "Finding a side length", "formats": ["find_length"]},
            {"key": "find_angle", "title": "Finding an angle", "formats": ["find_angle"]},
            {"key": "solve_equation", "title": "Solving trig equations", "formats": ["solve_equation"]},
        ],
    },
}


def get_topic_meta(topic: str) -> Optional[Dict[str, Any]]:
    return TOPICS.get(topic)


def get_topic_sections(topic: str) -> List[Dict[str, Any]]:
    meta = TOPICS.get(topic)
    return list(meta["sections"]) if meta else []


def get_section_for_topic(topic: str, key: str) -> Optional[Dict[str, Any]]:
    for sec in get_topic_sections(topic):
        if sec["key"] == key:
            return sec
    return None


def list_topics() -> List[Dict[str, Any]]:
    return [
        {
            "topic": key,
            "title": meta["title"],
            "term": meta["term"],
            "subskills": meta["subskills"],
        }
        for key, meta in TOPICS.items()
    ]
